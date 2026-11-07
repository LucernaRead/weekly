# FIX REPORT — Lucerna Weekly W46 JA family, Round 3 defect D-KEY-42

- Issue: VOL.3, dated Mon 2026-11-09 to Sun 2026-11-15 (9–15 Nov 2026).
- Scope: all 11 JA-target editions — `2026-w46-ja-de, -en, -es, -fr,
  -it, -ko, -nl, -pt, -ru, -zh-cn, -zh-tw`. The directory
  `files/weekly-report-w46-ja-core/` IS the zh-cn edition.
- Authority: the independent proofreader's Round 2 verdict
  (`hidden_files/w46/ja-proofread-gates-round2/proofreader-verdict-round2.md`):
  ROUND 2 FAIL on ONE defect, D-KEY-42, in all 11 editions. All three
  Round 1 defects were CONFIRMED fixed (kinsoku wrap-level fix
  ACCEPTABLE; 8 zh-tw conversions CONFIRMED; zh-tw web PDF CONFIRMED);
  keys 149/150 confirmed; full re-gate passed.
- Fix worker: 2026-11-03. Worked locally only: nothing pushed,
  inserted, or posted; `~/workspace/weekly-git` and `index.json`
  never touched; no rendered SVG/PDF hand-edited; the single change
  went through the build source and a full re-render; `.text.md`
  files regenerated via `hidden_files/w46/make_textmd.py`, never
  hand-edited or extracted from PDF; web PDFs built ONLY via
  `tools/webpdf.py`.
- Status: D-KEY-42 fixed at the source in the core and propagated to
  all 10 fan-outs by regeneration; all 11 editions re-rendered and
  re-gated on the final artifacts. **A Round 3 independent proofread
  is still required; this re-gating does not replace it.**

## 1. D-KEY-42 — P8 key 42 omits a stem piece (BLOCKING, frozen core, all 11)

Stem (P3, item 42, all editions): `酉の市で / 熊手を / 買います → ___`
(造句 — build a sentence from the pieces). The printed P8 key read
`42. 熊手を買います。` — the Japanese key sentence omitted the stem
piece `酉の市で` (the location). The reader-language note in every
edition supplied the location, but the Japanese key itself was
incomplete under the issue's own 造句 convention: all 7 sibling 造句
items include every stem piece in the key (39, 40, 41, 133, 134, 135
including the `で`-location piece, 136); Q42 was the sole exception.

### 1.1 Source and fix

Single registry source: the exercise registry (`REG` in `bslib4.py`)
is populated by the `e.ex()` calls in the content files, and the P8
keys section (`content8.py`) is generated from `REG`. The key-42
sentence is the third argument of exactly one `e.ex()` call:

- File: `hidden_files/weekly-report-w46-ja-build/content34.py:95`
- Before: `e.ex("B1", "造句", "熊手を買います。", "在酉の市买熊手",`
- After: `e.ex("B1", "造句", "酉の市で熊手を買います。", "在酉の市买熊手",`

The exact quoted string `"熊手を買います。"` occurred exactly once in
the core build (verified by grep before editing); the P3 stem on the
following line and the article sentence `酉の市では、熊手を買います。`
(`content34.py:24`) are different strings and were NOT touched. No
other core file was edited. `svglib.py` was NOT touched (md5
unchanged, see §5). No `transform.py` was edited and the zh-tw MAP was
NOT edited: the 9 fan-out `transform.py` files copy the core content
files and replace only the explanation layer (the key sentence is a
frozen Japanese string, the note is the replaced 4th argument), and
`gen_ja_zhtw.py` copies the core tree and applies the MAP to the
Chinese notes only. Re-running the family build therefore propagated
the one-line core fix to all 10 fan-out builds, each at its own
`content34.py:95`, with its own reader-language note byte-identical.
Verified after regeneration: all 11 generated `content34.py:95` lines
carry `酉の市で熊手を買います。` with the notes below unchanged, and
the old exact-quoted key occurs 0 times in all 11 build copies.

### 1.2 Before/after — rendered P8 key 42 in all 11 editions (SVG text)

| edition | BEFORE (P8 key 42) | AFTER (P8 key 42) |
|---|---|---|
| zh-cn (core) | `42. 熊手を買います。 — 在酉の市买熊手` | `42. 酉の市で熊手を買います。 — 在酉の市买熊手` |
| de | `42. 熊手を買います。 — Einen Kumade auf dem Tori-no-ichi kaufen` | `42. 酉の市で熊手を買います。 — Einen Kumade auf dem Tori-no-ichi` + wrap line `kaufen` (see §3.2) |
| en | `42. 熊手を買います。 — Buying a kumade at Tori-no-ichi` | `42. 酉の市で熊手を買います。 — Buying a kumade at Tori-no-ichi` |
| es | `42. 熊手を買います。 — Comprar un kumade en Tori-no-ichi` | `42. 酉の市で熊手を買います。 — Comprar un kumade en Tori-no-ichi` |
| fr | `42. 熊手を買います。 — Acheter un kumade à Tori-no-ichi` | `42. 酉の市で熊手を買います。 — Acheter un kumade à Tori-no-ichi` |
| it | `42. 熊手を買います。 — Comprare un kumade a Tori-no-ichi` | `42. 酉の市で熊手を買います。 — Comprare un kumade a Tori-no-ichi` |
| ko | `42. 熊手を買います。 — 도리노이치에서 구마데 사기` | `42. 酉の市で熊手を買います。 — 도리노이치에서 구마데 사기` |
| nl | `42. 熊手を買います。 — Een kumade kopen op Tori-no-ichi` | `42. 酉の市で熊手を買います。 — Een kumade kopen op Tori-no-ichi` |
| pt | `42. 熊手を買います。 — Comprar um kumade em Tori-no-ichi` | `42. 酉の市で熊手を買います。 — Comprar um kumade em Tori-no-ichi` |
| ru | `42. 熊手を買います。 — Покупка кумадэ на Тори-но-ити` | `42. 酉の市で熊手を買います。 — Покупка кумадэ на Тори-но-ити` |
| zh-tw | `42. 熊手を買います。 — 在酉の市買熊手` | `42. 酉の市で熊手を買います。 — 在酉の市買熊手` |

Reader-language notes UNCHANGED in all 11 editions — before/after
pair (core, quoted from the pre-fix SVG and the post-fix SVG, and
from the source lines): BEFORE `42. 熊手を買います。 — 在酉の市买熊手`
→ AFTER `42. 酉の市で熊手を買います。 — 在酉の市买熊手`; the note
`在酉の市买熊手` is identical. The same identity holds for the other
10 notes (source line 95 in each generated build compared with its
pre-fix line; only the key argument differs). The old form
`42. 熊手を買います。` (without `酉の市で`) occurs 0 times in all 88
SVGs, in all 11 regenerated `.text.md` files, and in both PDF text
layers of all 11 editions (checked before the KIT records in §7 were
appended; the KIT records intentionally quote both forms).

## 2. Rebuild and regeneration (all 11)

- Pre-fix snapshot: `hidden_files/w46/ja-fix-round3/before-sha256.txt`
  (132 files: all SVGs, PDFs, text.md files, ABSTRACT.txt files),
  `baseline-svg-text/` (pre-fix SVG `<text>` dumps per edition),
  `key42-before.json` (pre-fix P8 key-42 elements with coordinates),
  `textmd-before/` (pre-fix `.text.md` copies), and
  `before-source-sha256.txt` (core sources, generated `content34.py`
  files, transforms, `gen_ja_zhtw.py`, MAP).
- Core rebuild: `run.py` exit 0, TOTAL 150, A2 46 / B1 75 / B2 29,
  by page 10/18/18/18/18/18/12/38, model chars 154, 0 FLOW OVERFLOW
  / HEAD TOO WIDE warnings. `render.py` exit 0, 8 cards, print PDF
  `Lucerna-VOL3.pdf` 24,795,357 bytes. Logs:
  `render-logs/core-run.log`, `render-logs/core-render.log`.
- Fan-out rebuild via `hidden_files/w46/ja-fix-round3/rebuild-fanouts.sh`
  (adapted from the Round 1 driver; same commands): all 9
  `transform.py` runs exit 0, zh-tw `gen_ja_zhtw.py` (plain
  `python3`, per its KIT) exit 0 transforming 9 files, all 10 `run.py`
  runs exit 0 with identical registry counts (TOTAL 150, A2 46 /
  B1 75 / B2 29, by page 10/18/18/18/18/18/12/38, model 154), 0
  overflow warnings in every run log, all 10 `render.py` runs exit 0.
  Full log: `render-logs/rebuild-summary.txt`; per-edition logs in
  `render-logs/`.
- `.text.md` regenerated for all 11 via `make_textmd.py` with week
  label `2026-W46 (9–15 Nov 2026)` and the pre-existing slugs;
  headers verified verbatim (`# <slug>`, blank,
  `Week: 2026-W46 (9–15 Nov 2026)`). Diffs vs the pre-fix copies are
  ONLY the key-42 lines (10 editions: one line replaced; de: the
  key-42 line replaced plus the faithful `kaufen` wrap-continuation
  line — see §3.2).
- Web PDFs via `tools/webpdf.py` only, driver
  `hidden_files/w46/ja-fix-round3/build-webpdf.sh`: all 11 exit 0
  in a single run (no interruption; the zh-tw run completed in the
  same pass). Sizes in §6; log `render-logs/webpdf-summary.txt`,
  per-edition logs `render-logs/webpdf-<code>.log`.

## 3. Verification of the fix

### 3.1 Key 42 and notes

Rendered P8 key 42 reads `酉の市で熊手を買います。` in ALL 11 editions
(quoted per edition in §1.2, each taken from its P8 SVG `<text>`
element). `p8.py` extract on the core returns key 42 =
`酉の市で熊手を買います。`; extracts on all 10 fan-outs return the
same key-42 value. The old form (without `酉の市で`) = 0 occurrences
in all SVGs / `.text.md` / PDF text layers (see §1.2). Reader-language
notes for item 42 are unchanged in all 11 editions (source-line and
SVG comparison, §1.2).

### 3.2 Line fit (measured with the build's own font metrics)

Column width is 434. Key-42 full-line widths (same `text_w`/`wrap`
metrics as the build, at each edition's rendered font size):

| edition | size | full-line width | result |
|---|---|---|---|
| zh-cn | 13.3 | 292.8 (slack 141.2) | 1 line, y unchanged 1428.984 |
| de | 12.9 | 466.1 (over by 32.1) | WRAPS: line 1 `42. 酉の市で熊手を買います。 — Einen Kumade auf dem Tori-no-ichi` (419.0) + line 2 `kaufen` (y=1383.5) |
| en | 13.3 | 407.9 (slack 26.1) | 1 line, y unchanged 1428.984 |
| es | 12.9 | 421.2 (slack 12.8) | 1 line, y unchanged 1396.854 |
| fr | 12.9 | 405.8 (slack 28.2) | 1 line, y unchanged 1368.877 |
| it | 12.9 | 419.7 (slack 14.3) | 1 line, y unchanged 1368.877 |
| ko | 12.9 | 351.0 (slack 83.0) | 1 line, y unchanged 1368.877 |
| nl | 12.9 | 411.3 (slack 22.7) | 1 line, y unchanged 1424.831 |
| pt | 12.9 | 429.3 (slack 4.7) | 1 line, y unchanged 1424.831 |
| ru | 12.9 | 406.7 (slack 27.3) | 1 line, y unchanged 1424.831 |
| zh-tw | 13.3 | 292.8 (slack 141.2) | 1 line, y unchanged 1428.984 |

The DE wrap is the specified fix's only layout consequence. It is
clean by every mechanical check: the break is at a space before
`kaufen` (line 1 ends `Tori-no-ichi`, line 2 starts `kaufen` — no
bracket, punctuation, or word split); kinsoku line-start/line-end and
orphan scans are 0 in de (and all editions, §4); the occlusion audit
is 0 flags in de; keys-flow end-y is unchanged at 2535.0 (the column-2
shift is absorbed within the column; the flow maximum sits in another
column); 0 FLOW OVERFLOW warnings. Precedent in the same edition's P8:
keys 68 and 97 already wrap onto single-word second lines (`Schrein`,
`(Donnerstag)`). No note, font size, or wording was changed to avoid
the wrap — the fix was applied exactly as specified, and the wrap is
flagged here for the Round 3 proofreader's adjudication. The full-frame
DE P8 card was visually checked: the two key-42 lines render with
normal spacing, no overlap, no intrusion into the footer.

### 3.3 Sibling 造句 keys and keys 1–150

All 7 sibling 造句 keys are unchanged and still complete (core
`p8.py` extract values, identical in all 10 fan-out extracts):
39 `七五三は子どものお祝いです。`, 40 `神社へお参りに行きます。`,
41 `千歳飴をもらいます。`, 133 `私は水よう日に友達とポッキーを分けます。`,
134 `七五三は子どものお祝いです。`, 135 `神社で千歳飴をもらいます。`,
136 `ソフトバンクは4連勝で日本一になりました。`. Keys 1–150 are
otherwise unchanged: `p8.py` compare CLEAN 150/150 for all 11, with
the keydiffs adjudicated in Round 2 unchanged (zh-cn `[]`, zh-tw
`[138]`, other 9 `[137, 138]` — legitimate redirects, values
re-verified in the per-edition extracts and unchanged).

## 4. Re-gate results on the FINAL artifacts

Driver: `hidden_files/w46/ja-fix-round3/run_gates.sh` (freeze
baseline + `--strict-cjk` diff, p8 compare, occlusion audit; log
`ja-fix-round3/gates-run.log`). Kinsoku/counts/SC scans: verbatim
copies of the Round 1 scripts (`kinsoku_scan.py`,
`counts_checks.py`, `sc_scan.py`, diff-verified identical), outputs
`ja-fix-round3/kinsoku-orphan.json`, `counts-checks.json`,
`sc-scan-AFTER.json`. PDF checks: `ja-fix-round3/pdf-checks.log`.

- Freeze baseline: 8/8 SVGs byte-identical
  (`ja-fix-round3/freeze-baseline.json`, ok 8); core integrity
  re-hash clean. Freeze diff `--strict-cjk`: exit 0 with 0 added CJK
  for zh-cn/de/en/es/fr/it/nl/pt/ru. ko exit 1, adjudicated
  legitimate: added-char set AND total byte-identical to Round 2
  (308 distinct, 3464 instances, all Hangul); the only page-string
  differences vs the Round 2 freeze JSON are the key-42 lines.
  zh-tw exit 1, adjudicated: added-char set AND total byte-identical
  to Round 2 (158 distinct, 849 instances); the only page-string
  differences vs Round 2 are the key-42 lines.
  (`ja-fix-round3/freeze-<code>.json`.)
- p8 compare: CLEAN 150/150 for all 11 editions, missing/extra/
  uncertain all empty. keydiff: zh-cn []; zh-tw [138];
  de/en/es/fr/it/ko/nl/pt/ru [137, 138] — all adjudicated legitimate
  redirects, identical to Round 2. (`ja-fix-round3/p8compare-<code>.json`;
  core extract `ja-fix-round3/p8extract-core.json`, noted set 150/150;
  per-edition extracts `p8extract-<code>.json`.)
- Occlusion audit: 0 flags in all 11 editions; the tool runs its
  synthetic selftest first and refuses to report if it fails.
  (`ja-fix-round3/occlusion-<code>.json`.)
- Kinsoku: 0 / 0 / 0 (start / end / orphan) in all 11 editions.
- Counts (all 11): stems 1–150 complete; P8 keys 1–150 complete;
  level chips raw count A2 44 / B1 74 / B2 27 (145; the run-log
  registry counts A2 46 / B1 75 / B2 29 are the authoritative split,
  identical to the seed record); P6 bars 480/720/780/1020 at x=315
  (= 30×16/24/26/34) with labels 山 34%, 神社 26%, 公園 24%,
  町 16% and the practice-data label, all present; P7 golden phrases
  8, verbatim, exactly 2× each (article + P7 list), present on the
  source page and on P7; keys-flow end-y per edition in §6 (identical
  to Round 1/2 values in every edition, including de); badges: core
  none (badge-less subtitle design, adjudicated not a defect),
  fan-outs correct at x=975/y=356.
- PDFs: every web PDF ≤ 7 MB; pdftotext bytes > 0 on every web PDF;
  web-vs-print pdftotext byte-identical for all 11; 8 pages each.
  pdftotext deltas vs Round 2: +12 bytes in 10 editions (the 4 added
  characters), +16 in de (same +12 plus the wrap line-break in the
  extracted text). (`ja-fix-round3/pdf-checks.log`; sizes in §6.)
- SC scan (zh-tw): CLEAN — 21 s2t-differing chars remaining (the
  adjudicated legitimate set 会内写参号国学寝届峡当数来横浅温点画祷里静),
  0 residue-char hits, 0 of 8 residue strings present, all 8
  Traditional forms present. (`ja-fix-round3/sc-scan-AFTER.json`.)
- Visual: P8 ×11 checked at full frame — all clean (key 42 correct
  in every edition, DE wrap tidy, no overflow, overlap, or tofu).
  Cosmetic items O-01–O-05 and the W45-promise wording were not
  changed, per the task.

## 5. Change isolation

- Hash check over the 132 snapshotted edition files: exactly 44
  changed — per edition, ONLY the P8 SVG, the print PDF, the web PDF,
  and the `.text.md` file. Unchanged (88 files): all P1–P7 SVGs in
  all 11 editions and all 11 `ABSTRACT.txt` files (byte-identical).
- SVG text-multiset diff vs the pre-fix dumps: in 10 editions exactly
  ONE text changed (the key-42 line, same total count); in de, the
  same one changed text plus the `kaufen` wrap-continuation element
  (total 1329 → 1330 texts, the wrap's second line). Key-42 line-1 y
  is unchanged in every edition. In de only, the keys after 42 in the
  same column shift down by one line height (14.6) — the expected
  consequence of the wrap; the keys-flow end-y is unchanged (see §3.2).
- `.text.md` diffs vs pre-fix copies: ONLY the key-42 lines (plus the
  de `kaufen` continuation line); headers verbatim.
- Source hashes: only the 11 `content34.py` files changed (1 core
  hand-edit + 10 regenerated copies, each at line 95 only). All other
  snapshotted sources are byte-identical: core `bslib4.py`,
  `content12/56/7/8.py`, `run.py`, `render.py`, `svglib.py`, all 10
  `transform.py` files, `gen_ja_zhtw.py`, and the zh-tw MAP.
- Round 1 fixes survive, verified: kinsoku 0 line-end / 0 line-start /
  0 orphan in all 11; abstracts byte-identical (all 11, hash-verified)
  with the Round 1 practice-framing tails; zh-tw MAP still 187 entries
  (hash-identical) with all 8 Traditional conversions present and the
  SC scan still clean; `svglib.py` md5 unchanged at
  `74177544422fe677639d769cd80499fb` with the NO_END block intact, and
  `CANON_SVGLIB_MD5` still that value in all 10 guard files (9 fan-out
  `transform.py` + `gen_ja_zhtw.py`), 0 occurrences of the old md5 in
  the guard files or the core `svglib.py`.

## 6. Final per-edition file inventory

(text.md bytes, web PDF bytes + pdftotext bytes; print PDF bytes;
8 SVGs + 8 cards per edition. Source: `ja-fix-round3/final-inventory.txt`
and `ja-fix-round3/pdf-checks.log`.)

| edition | text.md (B) | web PDF (B) | pdftotext (B) | print PDF (B) | keys-flow end-y | p8 keydiff |
|---|---|---|---|---|---|---|
| zh-cn (core) | 44,225 | 2,496,765 | 44,850 | 24,795,357 | 2514.9 | [] |
| de | 46,360 | 2,366,010 | 47,006 | 29,500,005 | 2535.0 | [137, 138] |
| en | 45,553 | 2,318,038 | 46,160 | 27,837,881 | 2532.0 | [137, 138] |
| es | 47,128 | 2,346,165 | 47,786 | 28,725,845 | 2536.2 | [137, 138] |
| fr | 47,041 | 2,344,133 | 47,681 | 28,745,818 | 2535.0 | [137, 138] |
| it | 46,902 | 2,337,476 | 47,561 | 28,720,420 | 2535.0 | [137, 138] |
| ko | 47,942 | 2,395,657 | 48,533 | 26,585,657 | 2520.4 | [137, 138] |
| nl | 46,163 | 2,340,934 | 46,815 | 28,723,682 | 2537.4 | [137, 138] |
| pt | 46,951 | 2,348,982 | 47,582 | 28,727,059 | 2533.5 | [137, 138] |
| ru | 53,638 | 2,254,305 | 54,276 | 24,646,231 | 2524.0 | [137, 138] |
| zh-tw | 44,204 | 2,872,569 | 44,829 | 27,062,375 | 2514.9 | [138] |

Print PDF filenames: `Lucerna-VOL3.pdf` (core),
`Lucerna-VOL3-{DE,EN,ES,FR,IT,KO,NL,PT,RU}.pdf`,
`Lucerna-VOL3-ZHTW.pdf`; web PDFs are the same names with `-web`
before `.pdf`; text.md files are `<slug>.text.md` (core slug
`2026-w46-ja-zh-cn`).

## 7. KIT records

A fix record with defect/fix quotes and re-gate evidence was appended
to all 11 `WEEKLY-KIT.md` files: core §12 (new section); fan-outs §6
Fix history (appended Round 3 record at the end of the section).
Earlier sections were untouched — each append was verified to leave
the pre-existing bytes unchanged. All before/after key-42 quotes in
the KIT records were taken from the verified SVG lines in §1.2 and
the per-edition notes; the DE record notes the wrap and its
measurements.

## 8. Not changed / adjudications carried

- The core's badge-less subtitle design (matches shipped W45 JA core
  exactly) — not a defect, unchanged.
- Cosmetic items O-01–O-05 — unchanged.
- W45-promise wording — unchanged.
- The ko and zh-tw freeze exit-1 results — adjudicated legitimate
  (sets/totals byte-identical to Round 2), not churned.
- The DE key-42 wrap (§3.2) — a direct consequence of the specified
  fix; no note, font, or wording was altered to avoid it. Flagged for
  the Round 3 proofreader.
- Nothing else was changed. Nothing specified in the task could not
  be applied as specified. No other defect was found or fixed; no
  proofreading beyond verifying this fix was performed.

## 9. Evidence index (all under `hidden_files/w46/ja-fix-round3/`)

`FIX-REPORT.md` (this file), `before-sha256.txt`,
`before-source-sha256.txt`, `baseline-svg-text/` (11 dumps),
`key42-before.json`, `svg-multiset-diff.json`, `textmd-before/` (11
pre-fix copies), `append_kit_records.py`, `rebuild-fanouts.sh`,
`build-webpdf.sh`, `run_gates.sh`, `gates-run.log`,
`freeze-baseline.json`, `freeze-baseline/` (baseline copy),
`freeze-<code>.json` (11), `p8compare-<code>.json` (11),
`p8extract-core.json`, `p8extract-<code>.json` (10),
`occlusion-<code>.json` (11), `kinsoku_scan.py`,
`kinsoku-orphan.json`, `counts_checks.py`, `counts-checks.json`,
`sc_scan.py`, `sc-scan-AFTER.json`, `pdf-checks.log`,
`final-inventory.txt`, `render-logs/` (core/fan-out run+render logs,
`rebuild-summary.txt`, `webpdf-summary.txt`, `webpdf-<code>.log`).
