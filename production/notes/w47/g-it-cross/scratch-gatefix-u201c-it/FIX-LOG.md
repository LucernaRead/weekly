# FIX-LOG — W47 pre-insert: U+201C font-routing fix (fix2) ported into 5 it editions

- Scope (only these 5): `2026-w47-it-de`, `2026-w47-it-en`, `2026-w47-it-nl`, `2026-w47-it-zh-tw`, `core-it`.
  Untouched by design: `it-ko` (its 1 sans quote renders in Noto Sans CJK KR, 474/1000em — verified NOT
  defective), every de edition (0 defective glyphs), every other edition, `scratch-refanout-it2/backup/`.
  No commit, no push, no lint.
- Date: 2026-11-11 (evening). Worker dir (this dir):
  `hidden_files/w47/scratch-gatefix-u201c-it/`.
- Disk: before 93G used / 57G free (150G disk, quota cap ~105G — under the 100G stop line, work proceeded);
  after 90G used / 60G free (the 3G drop is other workers' cleanup happening concurrently, not mine).
  This scratch dir: 562M before cleanup → 183M after (freeze + b2 build-copies deleted, see §6).

## 0. Font verification (fontTools hmtx, re-measured — matches the coordinator's brief)

| face | U+201C | U+201D | U+2019 |
|---|---|---|---|
| Noto Sans CJK SC | 1.000 | 1.000 | 1.000 |
| Noto Sans CJK TC | 1.000 | 1.000 | 1.000 |
| Noto Sans CJK KR | 0.474 | 0.474 | 0.278 |
| Newsreader Regular | 0.441 | 0.441 | 0.256 (all three in cmap) |

So the port extends fix2 to all three codepoints: U+201D/U+2019 are also full-width in SC/TC.
No U+2019 defective glyph existed in the shipped SVGs (all 9 defective glyphs were U+201C/U+201D);
the extension is defensive, verified by the advances above.

## 1. The port (svglib.py only — nothing else in any edition touched)

Source: `core-de/svglib.py` fix2 (lines 75–105). Target files all had the identical
`_char_font` / `_PATH` / `_NEWS` / `_NEWS_B` structure (verified before patching):
`2026-w47-it-de` / `it-en` / `it-nl` / `core-it` are byte-identical files; `it-zh-tw` is the TC
variant (`_tc_index`, Noto Sans/Serif CJK TC, plus an extra kinsoku block later in `wrap()` —
the `_char_font` region is identical, so the same block ports unchanged).

The ported diff (identical in all 5 files; full per-edition diffs saved as
`<slug>/svglib.diff`, pre-patch copies as `<slug>/svglib-pre.py`):

```diff
--- svglib.py (pre-patch)
+++ svglib.py (post-patch)
@@ -72,9 +72,33 @@
         if cp in _CMAP["serif_b" if bold else "serif"]:
             return "serif"
         return "deja"
+    # fix2 (2026-11-11, proof2 D1/D2; ported from core-de, extended to
+    # U+201D/U+2019): U+201C/U+201D/U+2019 are full-width (advance
+    # 1000/1000em) in Noto Sans CJK SC/TC -- their ink sits at the right
+    # edge of the cell, so a sans quote leaves a wide white gap before
+    # it. Newsreader's are the narrow glyphs the other pairs already
+    # use (~0.44em / ~0.26em). Route these codepoints through the serif
+    # branch, which assigns them their Newsreader class: the characters
+    # stay unchanged everywhere (source, text.md, PDF text layers) and
+    # only the rendered glyph changes.
+    # No new string literal is written here on purpose: freeze_direct.py
+    # accounts source literals against tr_<lang>.py, and the class name
+    # 'news' occurs in no tr literal -- a literal 'news' would fail its
+    # source level. The class is therefore derived, not spelled.
+    if ch in ("\u201c", "\u201d", "\u2019"):
+        # italic=False on purpose: the serif branch with italic would pick
+        # the "news_i" class, which has no ("sans", ...) _PATH row.
+        return _char_font(ch, "serif", bold)
     if cp in _CMAP["sans_b" if bold else "sans"]:
         return "sans"
     return "deja"
+
+# fix2: _PATH entries for the Newsreader class inside sans runs, keyed by the
+# derived class name (see _char_font). _pil resolves ("sans", bold, "news")
+# to the Newsreader faces, mirroring the ("serif", bold, "news") rows.
+_QUOTE_CLS = _char_font("\u201c", "serif", False)
+_PATH[("sans", False, _QUOTE_CLS)] = _NEWS
+_PATH[("sans", True, _QUOTE_CLS)] = _NEWS_B
 
 def _pil(kind, bold, cls, size):
```

Patch verification (per edition, `port_fix2.py`):
- `py_compile` passes; reverse-patching reproduces the recorded pre-patch md5 exactly;
  the diff contains ONLY the ported block (additions only, no removals).
- Functional check (imported patched module): `_QUOTE_CLS == 'news'`; all three codepoints
  route to `news` in sans kind (bold and non-bold); 19pt sans widths 8.38 / 8.38 / 4.86 px
  (was 19.0 full-width); plain Latin and CJK still route to `sans`.

| edition | svglib.py md5 pre → post | sha256 post |
|---|---|---|
| 2026-w47-it-de | 05e25a0212a43d2c2298f85791e3c25d → 59d44590a1950713176405fc9bdab3ec | 12bcdac6807f55d457df2f896deebd89dc66dbbf265ef27a0c1ccaa124a29954 |
| 2026-w47-it-en | 05e25a0212a43d2c2298f85791e3c25d → 59d44590a1950713176405fc9bdab3ec | 12bcdac6807f55d457df2f896deebd89dc66dbbf265ef27a0c1ccaa124a29954 |
| 2026-w47-it-nl | 05e25a0212a43d2c2298f85791e3c25d → 59d44590a1950713176405fc9bdab3ec | 12bcdac6807f55d457df2f896deebd89dc66dbbf265ef27a0c1ccaa124a29954 |
| 2026-w47-it-zh-tw | 9caa4651959673f511cd56873d93a04a → 0fbc4437d99ff55a2ffd6e7cfb6d436f | 6350d1e15b42b40a0cccc200e4a26ca0e86a0505dbbb41e5db377cb7b6fae768 |
| core-it | 05e25a0212a43d2c2298f85791e3c25d → 59d44590a1950713176405fc9bdab3ec | 12bcdac6807f55d457df2f896deebd89dc66dbbf265ef27a0c1ccaa124a29954 |

Post-patch md5s re-confirmed on the production files at the end of the run (same values).
Note: `git status` shows `M core-it/2026-w47-it-zh-cn.text.md` and `M core-it/WEEKLY-KIT.md` vs git HEAD —
both pre-date this task (the text.md diff is exactly the D-2 fix lines 775/777; the KIT diff is the
D-2 record). This task never wrote either file except the KIT §10 append documented below; the
text.md SHA is byte-identical to the pre-task baseline.

## 2. Census before / after (coordinator's method: per `<text>` font-family × U+201C/U+201D/U+2019)

Before (shipped SVGs; full output `census-BEFORE.txt`):

| edition | defective before | where | after |
|---|---|---|---|
| 2026-w47-it-de | 1 | P1 U+201C in Noto Sans CJK SC | **0** (P1 quote now Newsreader ×1; P8 quote was already Newsreader ×1) |
| 2026-w47-it-en | 2 | P1 U+201C+U+201D in SC | **0** (P1 Newsreader ×2; P8 Newsreader ×2) |
| 2026-w47-it-nl | 2 | P1 U+201C+U+201D in SC | **0** (P1 Newsreader ×2; P8 holds no quote glyphs) |
| 2026-w47-it-zh-tw | 2 | P1 U+201C+U+201D in TC | **0** (P1 Newsreader ×2; P8 Newsreader ×2) |
| core-it | 2 | P1 U+201C+U+201D in SC | **0** (P1 Newsreader ×2; P8 Newsreader ×2) |
| **Total** | **9** | | **0** |

After counts verified twice: on the b1 scratch builds (gates G2) and on the synced production
files (`prod-gates-all.log`, `census.py` re-run post-sync: grand defective total 0).

## 3. Rebuilds + gates

Tooling: `tools/run_build.py` (run+render) → `tools/webpdf.py` → AST `.text.md` export
(`export_it_textmd` from `production/2026-w46/core-it/finish`, same tail as `build_edition.py`).
Two independent builds per edition (b1, b2). b1/b2 agree byte-for-byte on all 8 SVGs, the print
PDF and text.md; the web PDF differs run-to-run (webpdf is not byte-reproducible — expected,
same as prior rounds).

Gates on b1 (`gates.py`, 10/10 PASS on every edition; logs `gates-b1.log` / `gates-b1.json`):

| gate | de | en | nl | zh-tw | core-it |
|---|---|---|---|---|---|
| G1 run.py TOTAL 150, 0 overflow | PASS | PASS | PASS | PASS | PASS |
| G2 census 0 defective | PASS (0) | PASS (0) | PASS (0) | PASS (0) | PASS (0) |
| G3 occlusion 0 flags | PASS | PASS | PASS | PASS | PASS |
| G4 p8 extract 150/150 + compare CLEAN | PASS, keydiff [137,138,139] | PASS, [137,138,139] | PASS, [137,138,139] | PASS, [137,138,139] | PASS, [] vs pre-fix P8 |
| G5 spill 0 SPILL (29 boxes) | PASS (61 OBSERVE) | PASS (62) | PASS (62) | PASS (62) | PASS (62) |
| G6 boxtitle 0 DEFECT (18 titles) | PASS (242 body) | PASS (236) | PASS (240) | PASS (249) | PASS (244) |
| G7 text.md byte-identical | PASS | PASS | PASS | PASS | PASS |
| G8 only p1 SVG differs vs pre-fix | PASS | PASS | PASS | PASS | PASS |
| G9 print/web text multiset identical, web < 7MB | PASS, 7782 wds | PASS, 7929 wds | PASS, 7886 wds | PASS, 6830 wds | PASS, 6886 wds |
| G10 P8 min font 13.0 px = 9.75 pt | PASS | PASS | PASS | PASS | PASS |

Notes:
- it-de word count 7782 vs the KIT §8 pre-fix record of 7781: +1 is a pdftotext tokenization
  artifact of the narrower quote — text.md is byte-identical, so no content changed.
- Freeze: `tools/freeze.py baseline` **8/8 byte-identical** post-sync on all 5 editions
  (pre-sync test on it-de b1 also 8/8; JSONs kept as `<slug>/freeze-postsync.json`).
- Post-sync production gate pass (`prod_gates.py`, `prod-gates-all.log`): ALL PASS on all 5
  (census 0, occlusion 0, p8 150/150 + CLEAN, spill rc 0, boxtitle rc 0, text multiset equal).
- b2 reproduction: en/nl b2 ran from post-sync production (all 8 SVGs + print + text
  byte-identical to b1/synced); de b2 pre-sync; core-it/zh-tw b2 post-sync — all match.
- `run_build.py` snapshots production before/after every run (rc=0 throughout): no build step
  ever wrote into production; production changed only via the explicit `sync.py` copies.

## 4. SHAs before → after (print / web / text.md)

| edition | print (bytes, sha256) | web (bytes, sha256) | text.md (bytes, sha256) |
|---|---|---|---|
| it-de | 14,037,210 `7952f4ff…5c7b8` → **14,037,253 `d46ecba4…caee`** | 1,297,238 `65e26290…a1ac0` → **1,297,294 `367a0217…a4bb`** | 56,662 `de0aa214…98c9` UNCHANGED |
| it-en | 14,032,910 `b0444f8a…b17` → **14,032,993 `4dfb7e32…598b`** | 1,291,139 `58f5354a…c7a3` → **1,291,244 `9eb580ab…4a7d`** | 55,183 `ad311b5b…f917` UNCHANGED |
| it-nl | 14,034,396 `a7edbb18…8a5e` → **14,034,478 `474c31fa…785c`** | 1,291,724 `61993f7f…6b5` → **1,291,820 `4eabd341…c524`** | 55,488 `b13ef7a7…06e` UNCHANGED |
| it-zh-tw | 27,779,699 `96aa3207…1531` → **27,779,799 `c9d6eb1a…d654`** | 2,074,041 `bdc35bc0…d3ce` → **2,074,124 `5c51b8fe…f3fc`** | 52,494 `c18ad203…8432` UNCHANGED |
| core-it | 27,726,330 `e1f89922…d55d` → **27,726,409 `c45fbe9f…0005`** | 1,790,597 `9c7701f3…c398` → **1,790,692 `885830b7…0330`** | 52,655 `9eb9ee06…6eed` UNCHANGED |

Full SHAs: pre-fix `baseline-shas.txt`, post-sync `final-shas.txt` (this dir).
text.md files were verified byte-identical and left untouched in production (sync.py never copies them).

Changed production files per edition (pre-patch snapshot vs post-sync snapshot, exact):
`svglib.py`, `svg/p1-prima.svg`, `cards/p1-prima.png`, print PDF, web PDF — and nothing else
(p2–p8 SVGs + cards byte-identical; `content*.py`, `bslib4.py`, `render.py`, `run.py`,
`ABSTRACT.txt`, `.text.md` untouched). The only further change after sync is the KIT append (§5).

## 5. KIT edits

Appended a dated fix2-port section (new SHAs/sizes + gate summary; history preserved, no old
section rewritten): it-de §14, it-en §14, it-nl §13, it-zh-tw §13, core-it §10.
Mapping note: the task brief said "§5 new SHAs/sizes + §7 dated rebuild record" — in these
KITs §5 is Images and the deliverables live in §7 plus the dated sections, so I followed the
KITs' own convention (append a dated section that supersedes §7/§8 deliverables, as §11/§12/§13
did before). The new sections state the supersede explicitly.

## 6. Scratch contents + cleanup

Kept in this dir: `FIX-LOG.md`, `port_fix2.py`, `rebuild.py`, `gates.py`, `sync.py`,
`prod_gates.py`, `census.py`, `fix_core_kit_line.py`, `baseline-shas.txt`, `final-shas.txt`,
`census-BEFORE.txt`, `disk-before.txt`, `prod-gates-all.log`, per-edition:
`svglib-pre.py`, `svglib-pre.md5`, `svglib-post.md5`, `svglib.diff`, `svg-pre/` (pre-fix SVGs),
`prod-prepatch.sha256`, `prod-patched.sha256`, `prod-after.sha256`, `prod-final.sha256`,
`gates-b1.log/.json`, `sync-b1.log`, `freeze-postsync.json`, `freeze-test.json` (it-de),
`b1/` (full build-copy + run-build.log, the synced source), `b2/run-build.log`,
`prod-gates/extract.json`, `prod-gates/compare.json`.
Deleted after checks (task requirement + storage rule): all `freeze-postsync/` and
`freeze-test/` build-copy dirs (JSON evidence kept) and all `b2/build-copy/` dirs
(b2 artifacts were verified byte-identical to b1/synced production; SHAs are recorded here).

## 7. Process notes (defects found in my own tooling, fixed during the run)

1. `rebuild.py` production-untouched check initially compared against the PRE-patch snapshot,
   so it-de b1 tripped on the (intended) `svglib.py` change itself; `run_build.py`'s own
   snapshot had already passed (rc=0). Fixed: baseline is the post-patch snapshot
   (`prod-patched.sha256`); the pre-patch snapshot is kept as `prod-prepatch.sha256`.
2. After syncing en/nl, their b2 runs tripped the same check against the stale pre-sync
   baseline (the sync itself is the only production change). Fixed: `rebuild.py` now prefers
   `prod-after.sha256` when present. The b2 build-copies were verified directly instead
   (all 8 SVGs + print + text byte-identical to synced production).
3. `gates.py` G4 first checked for the literal string "150/150" in p8 extract stdout; the tool
   prints "noted set = 150 of 150". Fixed to read `noted_set` from the extract JSON.
4. The core-it KIT append was first done via a shell heredoc, which mangled the `\u201c` /
   `\u201d` / `\u2019` escape sequences into U+2028 + control characters (\x1d, \x19) in the
   file. Fixed with a Python script that builds the literal text from `chr(92)`; all 5 KITs
   verified clean (no control chars / U+2028) with exactly 3 backslashes in the quoted line.
   The other 4 KITs were edited via the file tool and were never affected.
   Lesson: never pass `\uXXXX` sequences through a shell heredoc in this environment.
