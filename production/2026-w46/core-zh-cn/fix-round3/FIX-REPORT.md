# Fix report — W46 ZH-CN family, Round 2 defect D5 (ex. 101 stem)

**Issue:** Lucerna Weekly VOL.3, ZH-CN target, dated Mon 2026-11-09 – Sun 2026-11-15 (Beijing time).
**Scope:** all 10 ZH-CN-target editions: `2026-w46-zh-cn-en` (core, `files/weekly-report-w46-zh-cn-core/`),
`-de`, `-es`, `-fr`, `-it`, `-ja`, `-ko`, `-nl`, `-pt`, `-ru`.
**Trigger:** Round 2 proofreader verdict D5
(`hidden_files/w46/zh-cn-proofread-gates-round2/proofreader-verdict-round2.md`, §5) —
the ONLY residual defect in Round 2 (D1/D3/D4 confirmed fixed; keys 150/150 confirmed).
**Worker:** fix worker, 2026-11-03. Worked locally only: no push, no insert,
no `index.json` edit, no Discord post, no chat dump, no other family touched.
No rendered SVG/PDF was hand-edited; every change went through source content
files + full re-render, with `.text.md` regenerated from the source manuscript.
**Status:** D5 fixed at the source, all 10 editions re-rendered and re-gated
clean. A Round 3 independent proofread (P7 scope per the Round 2 verdict §5)
follows; this re-gating does not replace it.

## 1. Defect D5 — ex. 101 stem (BLOCKING, frozen core, all 10 editions)

**Stem (before, identical in all 10 build dirs `content7.py:20` and all 10 P7 SVGs):**

```
我拿了一个___包裹。
```

**Key (correct, UNCHANGED):** `个`. Registry `content7.py:19` (core wording):
`a.ex("A2", "完成句子", "个", "包裹 takes the measure word 个 gè.", …)`.
P8 note 101 in every edition is the same note in the reader's language
(quoted verbatim, before = after, §4).

**Why it is a defect:** completed with the key, the sentence reads
`我拿了一个个包裹。` — a doubled classifier (`一个` + `个` before the same
noun), ungrammatical Mandarin. The issue's own P7 error clinic — on the SAME
page, in all 10 editions — corrects exactly this error:

```
wrong:  「我拿了两个包裹个」
right:  → 「我拿了两个包裹。」
gloss:  Order: number + measure word + noun.
```

And the P7 A2 column immediately above ex. 101 teaches `一个包裹 (a parcel)`
(glossline: "Measure words still matter: 一个包裹 (a parcel), 一部电影 (a film),
一场演练 (a drill)."). A learner answering ex. 101 correctly produced a
sentence the same page teaches is wrong. This departs from the earlier
"stem awkwardness" framing in the D3/D4 fix record (which left the stem
flagged-but-unchanged): the completed sentence is ungrammatical, not awkward.

**Fix (exactly as specified by the proofreader):** remove `一个` from the stem.
The key MUST NOT change; P8 note 101 MUST NOT change; the error clinic and the
A2 column are evidence, not the defect, and were NOT reworded.

## 2. Where the fix was applied

- **All 10 build dirs** — `hidden_files/weekly-report-w46-zhcn-build` (core)
  plus `hidden_files/weekly-report-w46-zh-cn-{de,es,fr,it,ja,ko,nl,pt,ru}-build`:
  `content7.py:20` only. Script: `apply_fix.py` / `apply_fix.log`
  (assertions: old stem exactly 1 occurrence per file, on line 20, with the
  key line `"个"` directly above it; after replacement old stem 0, new stem 1).
  Post-fix build-source hash diff: exactly these 10 files changed; no other
  `.py` file in any build dir changed.
- **Transform maps: NO change.** The stem occurs nowhere in
  `hidden_files/w46/maps/*.json` (grep 0 occurrences of the old stem across
  all 9 maps) — the stem is core-registry content, not explanation-layer
  content, so there was nothing to fan out through the maps. The 9 maps were
  not rewritten. (Contrast D3/D4, where P8 note strings lived in the maps.)
- **Before (stem) → after (stem), all 10 editions:**

```
我拿了一个___包裹。  →  我拿了___包裹。
```

Completed with the key: `我拿了个包裹。` — grammatical (measure word in the
blank, no doubling).

**Old key lists stay at 0 (D3/D4 undisturbed):** grep for the old lists
`["c", "b", "d", "a"]` / `["c", "d", "b", "a"]` across all 10 build dirs = 0
hits; the fixed lists `["d", "c", "b", "a"]` (content12.py) and
`["c", "d", "a", "b"]` (content56.py) occur 10 times each (once per build dir).

## 3. Re-render

Full re-render of all 10 editions from source with the family's own drivers
(the same ones the D3/D4 fix worker used — `render_all.sh` in this directory,
adapted only in its output path): per edition `run.py` → `render.py` →
`tools/webpdf.py` (web PDFs ONLY via `tools/webpdf.py`, per SOP 附则四) →
`textmd.py`. Every driver log: TOTAL 150, levels A2 56 / B1 69 / B2 25,
per-page 10/18/18/18/18/18/12/38, writing model 164, **zero** FLOW OVERFLOW /
HEAD TOO WIDE. Render logs: `render-{en,de,es,fr,it,ja,ko,nl,pt,ru}-{run,render,webpdf,textmd}.log`,
`render_all.log` (exit 0).

`.text.md` regenerated from the source manuscript in every edition; diff vs the
pre-fix copies (`textmd-before/`) is exactly **1 changed line per edition**
(line 1379, the stem; 4 diff lines incl. markers); headers preserved verbatim.
Full diffs: `textmd-diffs.txt`.

## 4. Verification — stem, key, P8 note 101

**Stem in all 10 P7 SVGs (quoted from SVG text extraction, `after-quotes.txt`):**

| Edition | P7 stem node |
|---|---|
| en | `我拿了___包裹。` |
| de | `我拿了___包裹。` |
| es | `我拿了___包裹。` |
| fr | `我拿了___包裹。` |
| it | `我拿了___包裹。` |
| ja | `我拿了___包裹。` |
| ko | `我拿了___包裹。` |
| nl | `我拿了___包裹。` |
| pt | `我拿了___包裹。` |
| ru | `我拿了___包裹。` |

Old stem `我拿了一个___包裹。` = **0 occurrences** in: all 10 build dirs' sources,
all 80 edition SVGs, all 10 `.text.md` files, and all 20 PDF text layers
(`gates/pdftotext-*.txt`). The doubled completed sentence `我拿了一个个包裹`
= 0 occurrences in all PDF text layers. The new stem occurs 1× in each web-PDF
text layer (10 total). (The old stem string still occurs ONLY as a quoted
historical record inside WEEKLY-KIT.md fix records — the D3/D4 record's
"Flagged, NOT changed" line and this record's before-quote — which are
documentation, not edition content. That scope is stated explicitly so a
naive whole-tree grep is not misread as a residual defect.)

**Error clinic + A2 column unchanged (all 10):** P7 nodes in every edition are
exactly the 3 lines `我拿了___包裹。` / `「我拿了两个包裹个」` /
`→ 「我拿了两个包裹。」`; the A2 glossline still teaches `一个包裹` (wrapped
across text nodes as before, verified in `after-quotes.txt`).

**P8 note 101, before vs after — IDENTICAL in all 10 editions**
(diff of `before-quotes.txt` vs `after-quotes.txt`, P8 101 lines: no differences):

| Edition | P8 note 101 (before = after) |
|---|---|
| en | `101. 个 — 包裹 takes the measure word 个 gè.` |
| de | `101. 个 — 包裹 nimmt das Zählwort 个 gè.` |
| es | `101. 个 — 包裹 lleva el clasificador 个 gè.` |
| fr | `101. 个 — 包裹 prend le classificateur 个 gè.` |
| it | `101. 个 — 包裹 prende il classificatore 个 gè.` |
| ja | `101. 个 — 包裹 は量詞 个 gè を取る。` |
| ko | `101. 个 — 包裹 는 양사 个 gè 를 써요.` |
| nl | `101. 个 — 包裹 neemt het telwoord 个 gè.` |
| pt | `101. 个 — 包裹 leva o classificador 个 gè.` |
| ru | `101. 个 — 包裹 берёт счётное слово 个 gè.` |

**Keys 150/150 unchanged:** registry AST dump (`dump_registry.py`, same tool
as the D3/D4 fix; `registry-dump-round3.txt`) diffed against the D3/D4
post-fix dump (`registry-dump-post-fix.txt`) shows **exactly 1 changed line** —
the ex. 101 STEM. Key 101 stays `个`; D3/D4 keys read 25.d / 26.c / 27.b /
28.a and 97.c / 98.d / 99.a / 100.b. `p8.py compare` is CLEAN 150/150,
keydiff `[]`, in all 10 editions (§6).

## 5. P8 UNTOUCHED — hash proof

Pre-fix snapshot (`pre-fix-edition-hashes.txt`, 210 files, taken before any
edit) vs post-fix state: all 10 P8 SVGs + all 10 P8 cards are **byte-identical**
(20/20). The same 20 hashes verify identically before the KIT appends and
after them (`post-fix-p8-hashes.txt`, `post-fix-edition-hashes-final.txt`).
The fix touches P7 only.

Pre-fix = post-fix SHA-256 (both snapshots agree):

| Edition | `svg/p8-ceyan.svg` | `cards/p8-ceyan.png` |
|---|---|---|
| en (core) | `937871c262133e316b40dcc33e95f786a5c21f3a13e9e08c361d339efca4f92d` | `b5c7a50d0cf4feab9086511a1fb81427d2fc73ac0423d02691c8bbb2e76d1314` |
| de | `a062bbe269f7cd863e1f843de6244b129641b271620c9fe4273ed1eb72a2a66a` | `268e4aa5cee9c5e4c5716838513af41d2bc2781b552caf3a70d6c28a8c1fda40` |
| es | `8b9e73b94ad8c7539dc13fc469806f5a8ecb6b801780f1967322cc4fadc152c0` | `2ae73144eef68580fa5b61df9f203a458d17338023e4ced45f964a3492c3e9b2` |
| fr | `8f42782927883a279ecaa2f33956cd9e097aceb14f5e10b9b555f850ba17eb32` | `63b496b3519d46c5e628d2e124f06033fd0547a3c9adf3db6f02670b3c9f3e90` |
| it | `26965d102b2dce9773ffd2cbd2bc647aabcc9aa0326b2226f83d2dcfb403b6c9` | `0a46641b8e95f0f695b9d93932248be4736086ebfd64ffbdfbd01be7cedace0b` |
| ja | `899ba552c851db91368e65927004fc0e2efb56952ddd0bb25ac375af84ff3e8f` | `90827a560139d1f54fc203251c595664a8b5819ed90569079abeee97ea702051` |
| ko | `981d8898035d9727ffea1e565d97d0762bd15d8f6f47003adbe4fd4bed646699` | `099432f580df4ee025fbaf7d3a166097259073917435d0904f0b4c90eee866d4` |
| nl | `062c08dedb5410645b9ac4ad983ea6cee334786f9273540dca23b26847c56077` | `b0c84242f601a55daf8f9bd02db34691f83f1f0709a3f312541648099792a85c` |
| pt | `95b42d0a05dfdec591d10192a58bd8e84c1781547db94d67a1664587fc7f4e85` | `46544e4f73dd6559a77894c5dc6a15ad8b62bd7d1c7a9ed47f5c3d1f727bacde` |
| ru | `cdf804c1c97bc62bc74e9f044a65c568909895df1f5cc94c4353a429e958a116` | `21daa9b9a25cf9d0477c7e95fe10144031663db85c74b1b6cab7db54bddd4495` |

## 6. Re-gate results (final artifacts, all 10 editions)

Gate scripts: `run_gates.sh` + `run_gates2.sh` (+ `measure_gates.py`), adapted
from the D3/D4 fix worker's scripts with only the output directory changed.
Evidence: `gates/` (summary.txt, summary-part2.txt, per-edition occlusion /
freeze / p8 JSON+logs, `counts-phrases-chart.json`, `kinsoku.log`,
`p8-corrected-keys.txt`, `pdf-checks.txt`, pdftotext extracts, rowcheck logs,
`freeze-baseline.json`/`.log`).

| Gate | Result (every edition) |
|---|---|
| Occlusion audit (`occlusion_audit.py`, selftest OK: planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent) | 0 flags, exit 0 |
| Freeze (`freeze.py diff --strict-cjk`, core vs each edition) | Added CJK 0 every page for en/de/es/fr/it/nl/pt/ru (exit 0). JA total added **4908**, KO total added **4304** with KO Hanzi-added 0 — identical to the Round 1/2 adjudicated figures; the `--strict-cjk` exit 1 for JA/KO is the expected CJK-script-layer behaviour, not a freeze failure. Core CJK totals per page: 932/968/877/787/901/1019/**739**/1084 — P7 741 → 739 is exactly the 2 removed characters (`一个`); all other pages unchanged. |
| p8.py extract + compare | 150/150 noted, CLEAN, missing=[], extra_count=0, keydiff `[]`, exit 0 |
| Corrected keys in native P8 rendering | 25.d / 26.c / 27.b / 99.a / 100.b in all 10, key and note trailing letter consistent (fragments in `gates/p8-corrected-keys.txt`; full P8 note 101 lines in §4) |
| Rowcheck §1 (same-baseline collisions) | CLEAN, all 8 pages × 10 (80/80). §2 crash on hardcoded `p6-verdieping.svg` is the known N/A (identical to Rounds 1–2). See the note below on the gate-script path fix. |
| Counts | 150; A2 56 / B1 69 / B2 25; per-page 10/18/18/18/18/18/12/38 |
| P7 phrases | All 8 phrases ×2, unchanged |
| P6 chart | Rects exactly (325,1274,220,30,#3e4c2a), (325,1324,330,30,#b3a06a), (325,1374,550,30,#b3a06a), (325,1424,770,30,#b3a06a) |
| Kinsoku | 0 flags, all editions |
| Web PDFs | 8 pages, ≤ 7 MB, pdftotext bytes > 0 and byte-identical web vs print (see §8; every edition exactly −6 text bytes vs pre-fix = the 2 removed CJK characters) |
| Freeze baseline (core) | Exit 0, 8/8 SHA-identical; shipped core SVGs unchanged by the run |
| Visual | P7 at full frame in all 10 editions (10 cards): fixed stem clean on one line, no overflow / re-wrap orphan from the shorter stem; error clinic + A2 column unchanged and consistent (see §7) |

**Rowcheck note (process, not a gate failure):** the copied `run_gates2.sh`
first ran rowcheck with the relative path `../files/...` from
`hidden_files/w46`, which does not exist (`FileNotFoundError` in the first
`summary-part2.txt` run). The D3/D4 worker's logs show §1 CLEAN, so their run
must have used working paths. This worker re-ran rowcheck §1 with absolute
edition paths (`rowcheck-summary.txt`, 8 CLEAN lines × 10) and patched the
script copy in this directory (`run_gates2.sh`) to use absolute paths, so the
saved script reproduces the result. The first failed invocation's logs were
overwritten by the correct re-run in `gates/rowcheck-*.log`.

## 7. Change isolation

- **Hash diff** (210 edition files, pre-fix snapshot vs post-fix, before KIT
  appends): exactly **5 files per edition** changed — `.text.md`, print PDF,
  web PDF, `svg/p7-ciyu.svg`, `cards/p7-ciyu.png`. All other 16 files per
  edition byte-identical, including all P1–P6/P8 SVGs and cards. After the KIT
  appends: 60 files changed total (the same 5 + `WEEKLY-KIT.md` per edition);
  no other file changed. (`hash-diff-pre-vs-post.txt`, `changed-files.txt`,
  `post-fix-edition-hashes-final.txt`.)
- **SVG-text multiset diff** (genuine pre/post comparison, `svg-multiset-diff.log`):
  the pre-fix build state was reconstructed by copying each build dir to /tmp,
  reverting ONLY the stem in `content7.py:20`, redirecting `OUT` to the /tmp
  copy, and running `run.py` there (shipped files untouched — verified by hash
  during the run). Text-node multisets of the /tmp pre-fix SVGs vs the shipped
  post-fix SVGs: **70/80 pages identical; the other 10 are the P7 pages, each
  differing by exactly one node** — `我拿了一个___包裹。` (pre) →
  `我拿了___包裹。` (post). The /tmp copies were deleted after the comparison.
- **Registry diff:** exactly 1 line (the stem; §4).
- **`.text.md` diffs:** exactly line 1379 per edition (§3).
- **ES `p.` fix survives:** `.text.md` lines 623 (`Responde con fechas y
  números de la p. 3.`) and 1063 (`... la p. 5.`); 0 occurrences of the old
  instruction `Responde con fechas y números de la página`; build sources
  `content34.py:96` / `content56.py:91` unchanged.
- **D3/D4 key fixes survive:** §2 grep + §4 registry diff + §6 P8 rendering.

**Visual (P7, full frame, all 10):** in every edition the fixed stem renders
as `我拿了___包裹。` on a single line under `101.` with the blank gap intact,
followed directly by ex. 102 — no overflow, no re-wrap orphan, no shift of
any neighbouring block (the stem occupies one line before and after, so the
A2 column flow is geometrically unchanged; confirmed by the multiset + hash
evidence above). The error clinic's third pair
(`我拿了两个包裹个` → `我拿了两个包裹。`, "number + measure word + noun")
and the A2 glossline (`一个包裹`) render unchanged in all 10, so the page is
now internally consistent: the clinic condemns the construction the exercise
no longer produces.

**Observation, NOT fixed (out of scope, pre-existing, RU only):** on the RU P7
card, the dark VOL.4 teaser band (rect y=2518.52, height 118, bottom 2636.52)
and the footer line (y=2624) overlap visually — the footer string sits on the
band's lower edge in dark type. The fix worker rebuilt the PRE-fix RU P7 from
the reverted source in /tmp and compared SVG element geometry: all 188 P7
elements are geometrically identical pre/post fix, so this appearance predates
the D5 fix and was left untouched per the D5-only scope. It is recorded in
the RU KIT append and referred here to the Round 3 proofreader to judge. No
other edition's P7 card showed this; the other 9 were read clean at full frame.
(The occlusion audit reports 0 flags for RU: the footer text is drawn after
the band, so it is not "covered" by the audit's definition — readability of
dark-on-dark type is a separate judgement, not a gate result.)

## 8. Final per-edition file inventory

Text-layer bytes are `pdftotext` output bytes (identical web vs print in every
edition; each exactly 6 bytes below its pre-fix figure — the 2 removed CJK
characters). Print PDFs are 8 pages each; web PDFs are 8 pages each, all
≤ 7 MB.

| Edition | `.text.md` bytes | Web PDF bytes | pdftotext bytes | Print PDF bytes |
|---|---|---:|---:|---:|---:|
| en (core) | 41,888 | 2,390,807 | 45,071 | 36,740,398 |
| de | 43,166 | 2,512,298 | 46,142 | 41,752,791 |
| es | 42,757 | 2,497,476 | 45,795 | 42,127,045 |
| fr | 44,190 | 2,405,830 | 47,164 | 38,266,481 |
| it | 42,848 | 2,420,595 | 45,872 | 39,035,680 |
| ja | 44,068 | 2,730,428 | 47,265 | 33,921,295 |
| ko | 43,875 | 2,526,513 | 46,852 | 32,301,853 |
| nl | 42,171 | 2,484,968 | 45,185 | 40,971,322 |
| pt | 42,555 | 2,450,694 | 45,677 | 39,429,621 |
| ru | 51,674 | 2,275,750 | 55,434 | 30,430,935 |

## 9. Records

- Fix record appended to all 10 KITs (`WEEKLY-KIT.md` in each edition dir;
  ES as Fix 3 after its Fix 1 D1 / Fix 2 D3+D4 records; the other 9 as the
  single post-proof fix heading following the D3/D4 record). Append-only:
  diff vs pre-append copies (`kit-before/`) shows 0 removed lines in every
  KIT; earlier sections untouched. The new record states the before/after
  quotes, the superseded "Flagged, NOT changed" line, the gate summary, and
  this edition's inventory figures (which supersede the KIT's pre-fix gate
  figures).
- This report: `hidden_files/w46/zh-cn-fix-round3/FIX-REPORT.md`.
- Evidence under `hidden_files/w46/zh-cn-fix-round3/`: fix script + log
  (`apply_fix.py`, `apply_fix.log`), registry dump + diff basis
  (`dump_registry.py`, `registry-dump-round3.txt`), render logs
  (`render_all.sh`, `render_all.log`, `render-*-{run,render,webpdf,textmd}.log`),
  gate scripts + JSONs/logs (`run_gates.sh`, `run_gates2.sh`,
  `measure_gates.py`, `gates/`, `gates-run.log`, `gates2-run.log`,
  `rowcheck-summary.txt`), pre/post hash snapshots
  (`pre-fix-edition-hashes.txt`, `pre-fix-build-hashes.txt`,
  `post-fix-edition-hashes.txt`, `post-fix-build-hashes.txt`,
  `post-fix-edition-hashes-final.txt`, `hash-diff-pre-vs-post.txt`,
  `changed-files.txt`), `.text.md` before-copies + diffs (`textmd-before/`,
  `textmd-diffs.txt`), before/after quotes (`before-quotes.txt`,
  `after-quotes.txt`), SVG multiset diff (`svg-multiset-diff.log`),
  freeze totals (`freeze-totals.txt`), KIT pre-append copies (`kit-before/`).

## 10. Unapplied work

**Nothing specified in the task could not be applied.** D5 is fixed in all 10
editions at the source, re-rendered, re-gated, and recorded as specified.
The single out-of-scope observation (RU P7 teaser/footer overlap, §7) was
deliberately left untouched per the fix-only-D5 scope and is referred to the
Round 3 proofreader.
