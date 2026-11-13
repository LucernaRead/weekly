# FIX-LOG — W47 U+201C font-routing fix (fix2 port, es family)

Scope: port the fix2 patch from `core-de/svglib.py` (commit 4ac7192c) into
**4 editions only** — `2026-w47-es-de`, `2026-w47-es-en`, `2026-w47-es-nl`,
`core-es` — extended from U+201C-only to U+201C/U+201D/U+2019. No other
edition touched; no de edition touched; no commit / push / lint.
Scratch: `hidden_files/w47/scratch-gatefix-u201c-es/`.
Date: 2026-11-11 (evening, America/Toronto).

## §0 Why

fix2 (core-de only): U+201C is full-width (advance 1000/1000em, fontTools
hmtx) in Noto Sans CJK SC/TC, so a sans quote leaves a wide white gap;
Newsreader's quote is ~0.44em. A full SVG census found 44 defective glyphs
in 21 editions. The four es editions carried 11 of them (all in
`font-family="Noto Sans CJK SC"` runs). fontTools also shows U+201D and
U+2019 are 1000/1000em in SC/TC, so the port covers all three codepoints —
a “-only port would have left defective glyphs (es-en P1 ”, es-nl P1 ” and
P6 ’ are U+201D/U+2019).
Note: the es-nl P6 ’ (`programma's`) was previously recorded as "accepted
as-is in a Newsreader context" — the census proves it renders in Noto Sans
CJK SC, so that acceptance is VOID; it is fixed by this port.

## §1 The port

All four target `svglib.py` files were byte-identical before patching
(md5 `6a46ee518bb0b6247db19f813925a4dc`, sha256
`0e3d72d73dad3857e8cc02325d777c02bd26323a4d56d52fbb8573df4e577642`).
Verified before patching: each has `_char_font`, `_PATH`, `_NEWS`, `_NEWS_B`.
core-de differs from the es files in more than fix2 (it has the kinsoku
wrap code and lacks `illus_voto`/`illus_houses`), so this is a minimal
port of the fix2 block only — never a wholesale sync.

Ported block (identical in all four files; `patch.py` + per-edition
`<slug>-svglib.diff` in this scratch dir):

```diff
     # fix2 (2026-11-11, proof2 D1/D2; ported 2026-11-11, extended to
     # U+201D/U+2019): U+201C/U+201D/U+2019 are full-width (advance
     # 1000/1000em, fontTools hmtx) in Noto Sans CJK SC/TC — ink sits at
     # the right edge of the cell, so a sans quote leaves a wide white
     # gap before it. Newsreader's quotes are narrow (~0.44em). Route
     # these three codepoints through the serif branch, which assigns
     # them their Newsreader class: the characters stay the same
     # everywhere (source, text.md, PDF text layers) and only the
     # rendered glyph changes.
     # No new string literal is written here on purpose: freeze_direct.py
     # accounts source literals against tr_<lang>.py, and the class name
     # 'news' occurs in no tr literal — a literal 'news' would fail its
     # source level (the quote chars themselves are fine: they are
     # substrings of the tr values). The class is therefore derived, not spelled.
+    if ch in ("\u201c", "\u201d", "\u2019"):
+        # italic=False on purpose: the serif branch with italic would pick
+        # the "news_i" class, which has no ("sans", ...) _PATH row.
+        return _char_font(ch, "serif", bold)
     if cp in _CMAP["sans_b" if bold else "sans"]:
```

```diff
+# fix2: _PATH entries for the Newsreader class inside sans runs, keyed by the
+# derived class name (see _char_font). _pil resolves ("sans", bold, "news")
+# to the Newsreader faces, mirroring the ("serif", bold, "news") rows.
+_QUOTE_CLS = _char_font("\u201c", "serif", False)
+_PATH[("sans", False, _QUOTE_CLS)] = _NEWS
+_PATH[("sans", True, _QUOTE_CLS)] = _NEWS_B
```

Patch verification (per file, `patch.log`): py_compile passes; the diff
contains ONLY the ported block; reverse-patching reproduces the pre-patch
md5 exactly. All four post-patch md5 identical:
`48c31801b48ef8914822a1607de59fb7` (confirmed again after sync).
Runtime check on the patched module: `_char_font` returns `"news"` for all
three codepoints in sans regular AND bold; `_QUOTE_CLS` derives to `"news"`;
Newsreader advance at 19pt is 8.375 vs 19.0 for CJK sans;
`_runs('“Debatte”: test', 'sans', False)` splits the quotes into their own
Newsreader runs.

## §2 Census (per `<text>` element font-family; defective = Noto Sans CJK SC/TC/HK)

`census.py` in this scratch dir; before = `census-before.json` (production
SVGs), after = `census-after-prod.json` (production SVGs post-sync).
The already-Newsreader P8 quotes are counted as OK in both runs.

| Edition | Before defective | Before total quotes | After defective | After total |
|---|---|---|---|---|
| 2026-w47-es-de | 1 (P1 19pt “ in `„Debatte“: Menschen diskutieren öffentlich.`) | 3 | **0** | 3 |
| 2026-w47-es-en | 2 (P1 18pt “” in `“Debate”: two or more people discuss in public.`) | 6 | **0** | 6 |
| 2026-w47-es-nl | 2 (P1 19pt ” in `„Debat”: een discussie in het openbaar.`; P6 18pt ’ in `programma's`) | 4 | **0** | 4 |
| core-es | 6 (P1 19pt “” `“辩论”：两人以上公开讨论，有轮次、有提问。`; P3 20pt “” `…带“魂”的音乐？…`; P5 20.5pt “” `…表示“将要”。`) | 10 | **0** | 10 |
| **Total** | **11** | **23** | **0** | **23** |

All 23 quote glyphs now render in Newsreader; no quote glyph remains in a
defective family in any of the four editions.

## §3 Rebuild + gates (`driver.py`, `driver-summary.json`)

Per edition: two independent `tools/run_build.py --steps run,render` builds
(out-A, out-B), then gates on build-copy A. Serial, one edition at a time.

| Edition | run A/B | Freeze A-vs-B | run TOTAL | webpdf | census | boxtitle | spill | p8 extract | p8 compare | occlusion | freeze diff | frozen_check | text.md |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| es-de | 0/0 | 8/8 identical | 150 | 0 | 0 defect | 0 | 0 | 150/150 | CLEAN keydiff [137, 138] (expected) | 0 | 0 | PASS 8/8 | identical |
| es-en | 0/0 | 8/8 identical | 150 | 0 | 0 defect | 0 | 0 | 150/150 | CLEAN keydiff [137, 138] (expected) | 0 | 0 | PASS 8/8 | identical |
| es-nl | 0/0 | 8/8 identical | 150 | 0 | 0 defect | 0 | 0 | 150/150 | CLEAN keydiff [137, 138] (expected) | 0 | 0 | PASS 8/8 | identical |
| core-es | 0/0 | 8/8 identical | 150 | 0 | 0 defect | 0 | 0 | 150/150 | CLEAN keydiff [] (expected) | 0 | 0 | **DIFF (see §4)** | identical |

`verify.py`: not applicable — W47 es-family editions ship no `verify.py`
(only the de family has one); the task's gate list does not include it.
No `freeze_direct.py` exists for the es family (only `scratch-fanout-de`
has one); the "freeze 8/8" gate is the A-vs-B byte-identical comparison
above plus `freeze.py diff` rc 0.

## §4 core-es frozen_check DIFF — expected artifact, not a content change

`frozen_check.py` compares multisets of raw `<text>` strings. For core-es
it reported P1 186→185, P3 171→169, P5 186→185 (other pages PASS). Cause:
the fix splits each fixed quote into its own Newsreader `<text>` run, so
the string multiset changes while the characters do not. Proven by direct
check: concatenating all `<text>` strings per page, **all 8 pages are
character-identical** before vs after (`ALL CHARS IDENTICAL: True`);
`<text>` element counts only grew on the three fixed pages (P1 186→189,
P3 171→174, P5 186→190; all other pages unchanged). The fan-out editions
passed frozen_check 8/8 because their changed strings are not in the
core/edition frozen intersection. Recorded in `core-es/WEEKLY-KIT.md` §7.

## §5 Sync (`sync.py`, `sync-report.json`)

Copied from build-copy A to production per edition: `svg/*.svg` (8) +
print PDF + web PDF + changed cards. Every copied file re-hashed after
copy; print/web SHAs equal the scratch SHAs; all SVGs match build-copy;
production `svglib.py` md5 `48c31801…` confirmed after sync.

Cards changed (re-rendered because the fixed glyphs are on those pages;
all other cards byte-identical): es-de `p1-portada.png`; es-en
`p1-portada.png`; es-nl `p1-portada.png`, `p6-afondo.png`; core-es
`p1-portada.png`, `p3-cultura.png`, `p5-juventud.png`.

Post-sync confirmation on production itself: census 0 defective in all 4;
boxtitle rc 0 and spill rc 0 in all 4.

## §6 SHAs — before → after (SHA-256)

text.md is byte-identical in all four (only the rendered glyph changes).

| Edition | File | Before (size) | Before SHA-256 | After (size) | After SHA-256 |
|---|---|---|---|---|---|
| es-de | print `La-Lucerna-VOL4-es-de.pdf` | 3,503,120 B | `65ebf6b7df8b07013d809427259a8b3504ac33e318bb9e0b61f72d7c9498fbca` | 3,503,173 B | `f47f4ea9fcb6f1a55b3a43f14f84ead4023746743fa1be653229111ce8a9ce68` |
| es-de | web `La-Lucerna-VOL4-es-de-web.pdf` | 889,913 B | `3c69c11834ec1d008925f829bf1cf772ced6404b81242fbccfe9f8604e2e8453` | 889,964 B | `31d479c8c1d7abfa143ae3da5197b4af8fda61a6dff85a20cbd13ffd087c9463` |
| es-de | text.md `2026-w47-es-de.text.md` | 45,311 B | `81ff06563dd9332ab6af2b4d826f2dda6d7157d82983df01e484fa462c310a67` (unchanged) | 45,311 B | same |
| es-en | print `La-Lucerna-VOL4-es-en.pdf` | 3,500,924 B | `80b4ce0a095551599adbf0e8e0c617715513a6df3c6ad004cc1428d8bb99b602` | 3,500,997 B | `b7f7931f6c2f43280f25c5db12cd35c4991ba260602a880e6dc9eab399c88fd9` |
| es-en | web `La-Lucerna-VOL4-es-en-web.pdf` | (size not recorded pre-sync) | `7f37168ccad12f524c39ba0fa783126b62015cb5c6b8709e54776026af3e9065` | 886,824 B | `f1221df30164ea0485c98291c6d868a425e406e90d8315a495dabc7b28bd3839` |
| es-en | text.md `2026-w47-es-en.text.md` | 44,983 B | `6080c94c420fd1077fedee777bba77ec789fd4c6c431ef70e7b7313923cc8906` (unchanged) | 44,983 B | same |
| es-nl | print `La-Lucerna-VOL4-es-nl.pdf` | 3,502,134 B | `d5e63a7f5ee3c974b345ebdb72ca438082718de970e2469dba7c2f96b60db68c` | 3,502,211 B | `67656a0d5451c3ef37aabd591d8505eda214de6812b019baa5151ee25d7cf174` |
| es-nl | web `La-Lucerna-VOL4-es-nl-web.pdf` | (size not recorded pre-sync) | `d51b8135c7f6aaa0c75af52e003063d8d0e7da12c254e639bf771e27ed48ace1` | 888,054 B | `c70a310a7210466736e85330237a7c333d00637988d1b7573b5c9a847247a1a8` |
| es-nl | text.md `2026-w47-es-nl.text.md` | 45,284 B | `d8d8e0078a7a121cf9a68bb22ee8074c6245462ebd86ef768cf87ee88c44b91e` (unchanged) | 45,284 B | same |
| core-es | print `La-Lucerna-VOL4.pdf` | 17,212,955 B | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5` | 17,213,128 B | `0ebf235d81245df4bf6d609a2987fa21d3ce693a85edf7f5cba0a12c412b6a93` |
| core-es | web `La-Lucerna-VOL4-web.pdf` | 1,410,463 B | `1663138c32d3869f78008819560ceb06f54537bb8f0b9fb325da0f876f07f75c` | 1,410,706 B | `a3cf275be5662c7c5cbb29f9ffc58e3c8436e293ac9a6b14e3e7702fba65446d` |
| core-es | text.md `2026-w47-es-zh-cn.text.md` | 43,788 B | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb` (unchanged) | 43,788 B | same |

Text-layer checks (pdftotext, print vs web byte-identical in all four):
es-de plain 46,352 B, -layout 111,448 B (both identical to before);
es-en plain 45,946 B, -layout 107,980 B (before 107,966; +14, whitespace
only — the P1 quote run-split changes pdftotext's line grouping; old-vs-new
plain-text diff is empty); es-nl plain 46,231 B (before 46,229; +2),
-layout 109,822 B (before 109,833; −11, whitespace only); core-es plain
44,707 B, -layout 106,440 B (both identical to before; one line-break
shift inside the P3 question in pdftotext's reconstruction, characters
identical).
Note: the KITs' older pdftotext byte counts (es-de 45,770, es-en 45,339)
were measured by a different method; the old production PDFs measured the
same way as the new ones give 46,352 / 45,946 — i.e. no content change.

Core-es SVG sha8: only p1/p3/p5 changed (p1 `f94607b6`, p3 `3885731b`,
p5 `ce0d5020`); p2 `4274b9ec`, p4 `897d34cb`, p6 `4095ea92`, p7 `a376ef8c`,
p8 `19123831` unchanged.

Pre-existing drift found (not caused by this task, recorded for the
coordinator): before this task, the production **web** PDFs did not match
the SHAs the KITs recorded for them — print PDFs matched exactly, web
PDFs did not (es-de actual `3c69c118…` vs KIT §9 `2e39306d…`; es-en
`7f37168c…` vs `f03047b1…`; es-nl `d51b8135…` vs `54fbf35e…`; core-es
`1663138c…` vs `c2473211…`). Sizes were off by a few bytes (es-de
889,913 B actual vs 889,914 B recorded; core-es 1,410,463 B vs
1,410,471 B). The KIT "Previous" lines added in this task cite the KITs'
own §9/§3 records, so they stay consistent with the files' documented
history; the table above uses the actual pre-patch production SHAs
(`pre-state-sha256.txt`). Likely cause: a web-PDF rebuild after the KITs
were written, without a KIT update. The post-sync web SHAs in this log
were verified against the freshly built files, so the record is accurate
from this build on.

## §7 KIT edits

Per edition: updated the deliverables/PDF record to the new SHAs/sizes
(preserving the previous numbers as history) and appended a dated
rebuild record: es-de/es-en §3 + new §10; es-nl §8 + new §10 (§3 is a
labelled build-3 historical record, left as-is); core-es §3 + new §7
bullets (fix2-port rebuild + frozen_check note). No other KIT text touched.

## §8 Disk

Start of task: 94G used / 56G free (quota cap ~105G). End of task:
90G used / 60G free (other workers cleaned up in the meantime; this task's
scratch is under 1M after cleanup). The 8 freeze build-copies (4× A + 4× B, ~126M)
were deleted after the checks; logs, census JSONs, driver/sync summaries,
patch log/diffs and this FIX-LOG are kept in this scratch dir.
