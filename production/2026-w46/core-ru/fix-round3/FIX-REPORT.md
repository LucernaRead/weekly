# FIX REPORT — Lucerna Weekly W46 RU family (VOL.3), Round 3 defect D4 (it edition only)
## Fix worker, 2026-11-03 (America/Toronto). Local only: no push, no insert, no Discord, no index.json, no ~/workspace/weekly-git, no edition content dumped into chat. A Round 3 independent proofread of the it edition follows; this report's re-gating does not replace it.

## Scope

ONE edition only: 2026-w46-ru-it (Russian target, Italian reader-native), folder `files/weekly-report-w46-ru-it/`. The other 10 RU editions were Round 2 PASS and the frozen RU core had to remain byte-identical. Work directory: `hidden_files/w46/ru-fix-round3/`.

Source of the defect: independent proofreader Round 2 verdict (`hidden_files/w46/ru-proofread-gates-round2/proofreader-verdict-round2.md`, ROUND 2 FAIL on the it edition only; D1/D2/D3 CONFIRMED fixed; keys 150/150 CONFIRMED; all gates clean; other 10 editions PASS). Round 1 fix record adjudicated: `hidden_files/w46/ru-fix/FIX-REPORT.md`.

## The defect (D4 — BLOCKING, pre-existing, missed in Round 1, NOT a fix regression)

Missing glyph U+0161 (š, LATIN SMALL LETTER S WITH CARON) in the it edition's P8 answer-key notes 51 and 129. The character has no glyph in the rendering fonts (Noto Serif CJK SC, 13pt, and Noto Sans CJK SC — confirmed by cmap inspection in the Round 3 font-coverage sweep; see §Font-coverage sweep). It occurred exactly twice in the entire 88-page issue, both here. The card PNG showed a tofu box (Ta☒kent, Ma☒a), the print PDF showed a tofu box, the web PDF showed a blank gap (Ta  kent) — verified by the Round 2 proofreader with raster crops in `hidden_files/w46/ru-proofread-gates-round2/crops/`.

## Source changed (at the source only; no SVG/PDF hand-edits)

Exactly ONE file, exactly TWO lines — `hidden_files/w46/ru_maps.py`, it spec (SPECS["it"], lines 1136–1415):

### Line 1318 — note 51

Before:
```
         ('国家队周四在塔什干比赛', 'La nazionale gioca giovedì a Taškent'),
```
After:
```
         ('国家队周四在塔什干比赛', 'La nazionale gioca giovedì a Tashkent'),
```

### Line 1343 — note 129

Before:
```
         ('玛莎这周是平常的一周', 'La settimana di Maša è una settimana normale'),
```
After:
```
         ('玛莎这周是平常的一周', 'La settimana di Masha è una settimana normale'),
```

The Chinese source keys are untouched; only the Italian transliterations change (`Taškent` → `Tashkent`, `Maša` → `Masha`), matching the nl edition's ASCII forms for the same notes. Diff vs the pre-fix copy (`ru-fix-round3/logs/ru_maps.py.pre-fix`): 2 changed lines (4 diff lines: 2 removed + 2 added). After the fix, š (U+0161) = 0 in the whole `ru_maps.py` file. No other line of `ru_maps.py` — and no other spec — was touched. The frozen core build source (`hidden_files/weekly-report-w46-ru-build/content56.py`, D1 keys `["d", "b", "a", "c"]`) was not edited in Round 3; it was only read by the transform.

## Rendered / registry before → after

Rendered P8 key (`files/weekly-report-w46-ru-it/svg/p8-test.svg`):

- Before: `51. B — La nazionale gioca giovedì a Taškent`
- After: `51. B — La nazionale gioca giovedì a Tashkent`
- Before: `129. B — La settimana di Maša è una settimana normale`
- After: `129. B — La settimana di Masha è una settimana normale`

Key letters unchanged: 51. B and 129. B before and after. P8 text-node diff vs the pre-fix SVG (339 nodes): exactly 2 nodes differ — nodes 222 and 309, the two lines above. All other 337 nodes, including keys 76/77, are identical.

Manuscript registry (`.text.md`, regenerated from source — see §Rebuild): the same two strings change in 4 lines — registry line 229 (ex. 51) and line 470 (ex. 129), and Answers lines 575 (51) and 661 (129). The regenerated file differs from the pre-fix file in those 4 lines only; header (`# VOL.3 · Russian text · Italian explanations`) verbatim; size unchanged at 55,223 bytes (š is 2 bytes in UTF-8, as is `sh`).

## Rebuild (it edition only — the family's own scripts, same as Round 1)

```
cd hidden_files/w46 && tools/venv/bin/python ru-transform.py it
    # exit 0; map: 232 keys, 464 replacements; no-CJK check: clean
cp hidden_files/weekly-report-w46-ru-build/check_core.py hidden_files/weekly-report-w46-ru-it-build/check_core.py
cd hidden_files/weekly-report-w46-ru-it-build && tools/venv/bin/python run.py
    # exit 0; TOTAL 150; A2 51 / B1 75 / B2 24; pages 10/18/18/18/18/18/12/38; model words 87; 0 FLOW OVERFLOW / HEAD TOO WIDE
tools/venv/bin/python render.py
    # exit 0; 8 cards; print PDF 15,000,295 bytes
tools/venv/bin/python hidden_files/w46/ru_textmd.py hidden_files/weekly-report-w46-ru-it-build <tmp>/2026-w46-ru-it.text.md "VOL.3 · Russian text · Italian explanations" "Composizione"
    # exit 0; diffed (4 lines only, above) then installed
cd tools && ./venv/bin/python webpdf.py ../files/weekly-report-w46-ru-it/svg ../files/weekly-report-w46-ru-it/Lucerna-VOL3-IT-web.pdf
    # exit 0; 8 pages; 157 distinct chars; WROTE 2,310,997 bytes, 55,066 text bytes
```

Logs: `ru-fix-round3/logs/ru-it-transform.log`, `ru-it-run.log`, `textmd-regen.log`, `webpdf.log`. Regenerated `.text.md` copy retained in `ru-fix-round3/textmd-tmp/`. No other edition's transform/run/render/webpdf was executed.

## Verification 1 — š = 0, Tashkent / Masha counts

| Artifact | š (U+0161) | Tashkent | Masha | U+FFFD |
|---|---|---|---|---|
| All 8 it SVGs (p1–p8) | 0 in every file | 1 (p8 only) | 1 (p8 only) | 0 |
| `.text.md` (55,223 bytes) | 0 | 2 (registry L229 + Answers L575) | 2 (registry L470 + Answers L661) | 0 |
| Print PDF text layer (55,066 bytes) | 0 | 1 (P8) | 1 (P8) | 0 |
| Web PDF text layer (55,066 bytes) | 0 | 1 (P8) | 1 (P8) | 0 |
| `ru_maps.py` (whole file) | 0 | — | — | — |

Each spelling is correct in every occurrence; the two strings occur in P8 notes 51 and 129 respectively and nowhere else in the rendered edition. Print-vs-web text is IDENTICAL after whitespace normalisation.

Note on remaining š characters: the character š still appears 9 times inside `WEEKLY-KIT.md` §11 — documentation only (the defect description naming U+0161, and the quoted BEFORE strings). The KIT is not a rendered artifact; the same documentation-quoting pattern was used in §10 for D1–D3. No š remains in any SVG, `.text.md`, PDF text layer, or build source output. The pre-fix `ru_maps.py` backup in `ru-fix-round3/logs/` also retains the two before-lines, by design.

## Font-coverage sweep (independent, it edition)

Script: `ru-fix-round3/font_coverage_sweep.py` (fontTools, tools venv). Every character in every SVG `<text>` node (156 distinct chars, whitespace excluded) was checked against the cmap of the rendering font face actually used for that node — family + weight, SC face index 2 of the split Noto CJK TTCs (`/usr/share/fonts/opentype/noto/NotoSerifCJK-{Regular,Bold}.ttc`, `NotoSansCJK-{Regular,Bold}.ttc`), plus UnifrakturMaguntia (`~/.local/share/fonts/UnifrakturMaguntia.ttf`, 7 chars: the masthead word).

Result: **0 missing glyphs.** No character outside its rendering font's coverage. Control: š (U+0161) is absent from BOTH the Serif SC cmap union and the Sans SC cmap union (44,777 / 44,810 chars respectively), so the sweep would have caught D4 pre-fix. No other missing glyph was found, and no additional item was fixed beyond D4 — none was found to fix. Output: `ru-fix-round3/logs/font-coverage.json` + `font-coverage.log`.

## Visual verification

- P8 card read at full frame (`files/weekly-report-w46-ru-it/cards/p8-test.png`): no overflow, no overlap, no tofu anywhere; footer clear; H-note intact.
- Crops (saved in `ru-fix-round3/crops/`): `p8-key51-card.png` — `51. B — La nazionale gioca giovedì a Tashkent`, clean; `p8-key129-card.png` — `129. B — La settimana di Masha è una settimana normale`, clean; `p8-key51-webpdf.png` and `p8-key51-printpdf.png` (150 dpi pdftoppm, page 8) — `Tashkent` clean, no tofu, no blank gap. The web/print PDF crops are raster-identical (same SVG source); their text layers and embedded fonts were verified separately (see gate table).

## D1 / D2 / D3 survival

- D1: rendered P8 keys `75. d — pacco d`, `76. b — reso b`, `77. a — codice promozionale a`, `78. c — picco c` — unchanged and correct. Manuscript registry D1 lines untouched by the Round 3 diff (only the 4 D4 lines differ).
- D2a: P3 instruction `Metti la forma verbale o il caso giusti.` — single node at (65, 2564.45), 20.5pt, unchanged.
- D2b: P4 instruction `Completa con numeri e parole di pagina 4.` — single node at (65, 2553.45), 20.5pt, unchanged.
- D3 (ja): the ja edition is a different edition; its files are byte-identical to pre-fix (see §Change isolation), so the ja P8 H-note fix survives untouched. The only shared source touched was `ru_maps.py`, and only its two it-spec lines (diff-verified).

## Re-gate results (it edition, final artifacts)

Script: `ru-fix-round3/gates.sh`; log `ru-fix-round3/logs/ru-fix-round3-gates.log`; JSONs `occlusion-round3-it.json`, `p8-round3-it.json`, `freeze-round3-it.json`; word analysis `ru-fix-round3/logs/word-analysis-it.txt`.

| Gate | Result |
|---|---|
| Counts (run log) | TOTAL 150; A2 51 / B1 75 / B2 24; pages 10/18/18/18/18/18/12/38; model words 87; 0 FLOW OVERFLOW / HEAD TOO WIDE |
| Web PDF (`tools/webpdf.py` only) | 8 pages; 2,310,997 bytes (≤ 7 MB); pdftotext 55,066 bytes (web and print); print-vs-web text IDENTICAL after whitespace normalisation; all fonts embedded + subset (pdffonts: Lucerna* CJK faces + UnifrakturMaguntia) |
| Occlusion audit (`tools/occlusion_audit.py`) | 0 flags; selftest OK (planted BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent) |
| `check_core.py` (it edition) | golden BAD 0; gloss fails 0; orphan line-starts []; same-baseline collisions 0; 8/8 golden phrases ×2 |
| `p8.py extract` (core) | 150/150 noted |
| `p8.py compare` vs core | CLEAN 150/150; missing=[] extra=0 uncertain=[]; keydiff [137, 138, 139, 140] — adjudicated: E-section translations by design (same adjudication as Rounds 1–2) |
| Freeze diff (`tools/freeze.py diff`) vs core | exit 0; added CJK chars 0 on all 8 pages; TOTAL added CJK 0 |
| Freeze word analysis | TOTAL ADD {} (zero added Cyrillic words); char totals cyr=16860 han=0 kana=0 hangul=0; p7 ADD {} (Russian text verbatim); removals are the adjudicated furniture/explanation replacements only |
| P6 chart (`chart_check.py`) | bars=[600.0, 343.0, 286.0, 200.0] at x=685 for 42/24/20/14%; labels sum 100% |
| PDF text layer | > 0 bytes (55,066), web ≤ 7 MB |

## Change isolation (sha256, pre-fix vs post-fix)

Manifests: `ru-fix-round3/logs/pre-fix-hashes.txt` (taken before any edit, 232 files under `files/weekly-report-w46-ru-*`) and `post-fix-hashes.txt` (taken after the KIT append, same relative paths).

Exactly **6 files changed**, all in the it edition:

1. `files/weekly-report-w46-ru-it/svg/p8-test.svg`
2. `files/weekly-report-w46-ru-it/cards/p8-test.png`
3. `files/weekly-report-w46-ru-it/Lucerna-VOL3-IT.pdf` (print)
4. `files/weekly-report-w46-ru-it/Lucerna-VOL3-IT-web.pdf`
5. `files/weekly-report-w46-ru-it/2026-w46-ru-it.text.md`
6. `files/weekly-report-w46-ru-it/WEEKLY-KIT.md` (§11 appended; §§1–10 byte-identical prefix, verified)

Byte-identical to pre-fix: the other 7 it SVGs, the other 7 it cards, `ABSTRACT.txt`, all 211 files of the other 10 editions + the frozen RU core directory (including the core/zh-cn `.text.md` pair). No files added or removed. The it-build directory was regenerated by the transform (expected intermediate; its `content34.py`/`content8.py` now carry the two ASCII strings), and `ru_maps.py` changed in its 2 it-spec lines only — neither is an edition file, and the output hashes above prove no spill into any other edition.

## Final inventory (it edition, final artifacts)

| File | Bytes (post-fix) | Bytes (pre-fix) |
|---|---|---|
| `.text.md` (`2026-w46-ru-it.text.md`) | 55,223 | 55,223 |
| Web PDF (`Lucerna-VOL3-IT-web.pdf`) | 2,310,997 | 2,311,010 |
| Print PDF (`Lucerna-VOL3-IT.pdf`) | 15,000,295 | 15,000,311 |
| P8 SVG (`svg/p8-test.svg`) | 61,044 | 61,044 |
| P8 card (`cards/p8-test.png`) | 941,697 | 941,897 |
| `WEEKLY-KIT.md` | 26,730 | 21,113 |
| pdftotext bytes (web PDF) | 55,066 | 55,066 |
| pdftotext bytes (print PDF) | 55,066 | 55,066 |

Note: pre-fix print PDF size was 15,000,311 bytes (from the pre-fix `stat` listing); post-fix 15,000,295 bytes (−16). SVGs: 8; cards: 8.

## KIT record

A fix record (§11, §§1–10 untouched — verified: the new KIT starts with the pre-fix KIT byte-for-byte) was appended to the it edition's `WEEKLY-KIT.md`, with the defect/fix quotes and re-gate evidence. No other edition's KIT was touched.

## Fixes NOT applied / could NOT be applied

None outstanding for D4: the defect was fixed exactly as specified (ASCII transliteration at the source, full it-edition re-render, re-gate). Nothing else was reworded, and no additional defect was found (font-coverage sweep clean; all gates clean). The following were deliberately NOT done, per the task: no push, no insert, no Discord post, no index.json edit, no `~/workspace/weekly-git` access, no other edition/family touched, no SOP edit, no proofreading beyond verifying this fix. A Round 3 independent proofread of the it edition still follows — this report's re-gating does not replace it.

## Files under hidden_files/w46/ru-fix-round3/

`FIX-REPORT.md` (this report), `gates.sh`, `font_coverage_sweep.py`, `logs/` (pre/post-fix hash manifests, pre-fix `ru_maps.py` / `.text.md` / P8 SVG / KIT copies, transform/run/textmd/webpdf/gates/font-coverage/word-analysis logs), `textmd-tmp/` (regenerated `.text.md` before install), `crops/` (P8 key 51/129 card crops, key 51 web/print PDF crops), `occlusion-round3-it.json`, `p8-round3-it.json`, `freeze-round3-it.json`.
