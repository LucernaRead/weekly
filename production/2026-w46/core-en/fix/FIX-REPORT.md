# FIX-REPORT — Lucerna Weekly W46, EN family, Round 1 proofread fixes

- Issue: VOL.3, Mon 2026-11-09 – Sun 2026-11-15. Target English, 11 reader-native editions: de, es, fr, it, ja, ko, nl, pt, ru, zh-cn (core dir `files/weekly-report-w46-en-core/`), zh-tw.
- Authority: `hidden_files/w46/en-proofread-gates/proofreader-verdict-round1.md` (Round 1 FAIL, all 11 editions FAIL; defects B1–B6, M1–M4). SOP: `files/weekly-report-SOP.md`.
- Worker: fix worker (subagent), 2026-11-02/03. No proofreading was done; only the verdict's listed defects were fixed, at the source, with full re-renders. A Round 2 independent proofread follows — this report's re-gating does not replace it.
- Method: every change went through a build source file (`hidden_files/weekly-report-w46-en-build/` core + `hidden_files/weekly-report-w46-en-<native>-build/` fan-outs) or `ABSTRACT.txt` (B2 only). No rendered SVG/PDF was hand-edited. All 11 editions were fully re-rendered after all fixes (`run.py` → `render.py` → `tools/webpdf.py` → `en_textmd.py`), sequentially, one edition at a time. All gate tools are the shared toolkit under `tools/`; no hand-rolled equivalents.
- Evidence in this directory (`hidden_files/w46/en-fix/`): per-edition build logs (`<ed>-{run,render,webpdf,textmd}.log`; ko second pass `ko-{run2,render2,webpdf2}.log`), `verify_fixes.py` + `verify_fixes2.log` (171/171 checks PASS on final artifacts), freeze JSONs (`freeze-<ed>.json`), P8 JSONs (`p8-<ed>.json`, `p8-core.json`), occlusion JSONs + logs (`occlusion-<ed>.json`), rowcheck logs (`rowcheck-<ed>.log`, ko second pass `rowcheck-ko2.log`), koscan logs (`koscan-ko.log`, `koscan-ko2.log`), `script_scan.py` output (recorded §6), wrap simulations (`sim_wrap.py`, `sim_ko.py`, `sim_gloss.py`, `sim_gloss2.py`, `sim_zt.py`), visual crops (`crops/`), old text.md backups (`old-textmd/`), source-edit script + log (`apply_fixes.py`, `apply_fixes.log`).

## 1. Deviations from the verdict's literal wording (require Round 2 adjudication)

Two verdict wordings could not be applied literally because the proposed strings overflow their fixed slots at the real fonts (measured with `svglib` font metrics; the box-title slot is ~416px: box x+18 to box edge, longest shipped box title ~417px). In both cases a shorter fitting question/gloss form was used, following the verdict's own documented precedents. Nothing else deviates.

- **B1 (es/pt/ru):** verdict proposes es `HOW LONG? · ¿Cuánto dura el mandato?` (469px), pt `HOW LONG? · Quanto dura o mandato?` (456px), ru `HOW LONG? · Каков срок полномочий?` (473px; 468px even without the house space before `?`). All three overflow. Shipped instead: es `HOW LONG? · ¿Cuánto dura?` (335.7px), pt `HOW LONG? · Quanto dura?` (328.7px), ru `HOW LONG? · Каков срок?` (318.8px) — all questions, following the verdict's IT precedent `Quanto dura?` (329px, shortened on the page from a longer kept form, adjudicated a correct question).
- **M4 (nl/pt):** verdict's pattern with full-caps translations measures nl 526px and pt 488px at 23pt bold against the 434px box. Shipped instead: nl `SCROOGE'S NIGHT · Scrooge-nacht` (409.8px; Dutch compound parallel to de `Scrooge-Nacht`), pt `SCROOGE'S NIGHT · A noite` (323.2px; parallel to it `La notte`). Translations themselves kept.

## 2. Fixes applied (before → after, with source)

### B4 — frozen core, all 11 editions (blocking). Lone `»` on its own line, P7 toolbox.
- Source: `content7.py:51` in the core build dir and in every fan-out build dir (identical line).
- Before: `cD.para("B1 — « Dickens wrote the story in 1843. »", 22.5)`
- After: `cD.para("B1 — « Dickens wrote the story in 1843.»", 22.5)`
- Rationale: wrap simulation with the real fonts (serif 22.5pt, width 434) reproduced the orphan (`…1843.` 426.3px + lone `»` 12.2px) and showed the fix re-breaks to `B1 — « Dickens wrote the story in` / `1843.»` (67.7px). An NBSP variant was rejected (invisible character in extracted text). The P7 B1 box example on `content7.py:32` (`« Dickens wrote the story in 1843. » — write → wrote (page 3).`) is a different string and was deliberately left untouched (11 residual `1843. »` hits in the sources are all line-32 examples).
- Verification: SVG text extraction — all 11 P7s carry `1843.»` on the B1 line and no `<text>»</text>` element; `verify_fixes.py` B4 checks pass for all 11; visually confirmed on the P7 cards of all 11 editions (2× crops `crops/b4-sheet1.png`, `crops/b4-sheet2.png`) and at full frame on the core P7 card. The B4 core fix is why all 11 editions were re-rendered.

### B5 — core (zh-cn) + zh-tw (blocking). Lone `。` alone on a line, P7 editor's-note paragraph.
- Source: core `content7.py:115` and zh-tw `content7.py:115` (`p.para(..., 20, "sans", ..., rw-48=848, 1.4)`).
- Core before: `…请把你的来信与写作寄来，VOL.4 起刊登收到的真实来信。` → after: `…请把来信与写作寄来，VOL.4 起刊登收到的真实来信。` (redundant `你的` deleted; 2 CJK chars; CJK wrap depends on character count).
- zh-tw before: `…請把你的來信與寫作寄來，VOL.4 起刊登收到的真實來信。` → after: `…請把來信與寫作寄來，VOL.4 起刊登收到的真實來信。`
- Verification: wrap simulation (before 3 lines with lone `。`; after 2 lines, `。` attached); SVG extraction — no lone-`。` line on any edition's P7; visually confirmed on both P7 cards (`crops/b5-sheet.png`) and at full frame on the core P7 card. The other 9 editions re-wrap cleanly and were not touched for B5.

### B1 — es/pt/ru only (blocking). P6 "HOW LONG?" glossed as a bare noun phrase.
- Source: `content56.py:166` in the 3 fan-out build sources. The builder's 11-edition core claim was refuted by the verdict; the core gloss `任期多长？` is a correct question and was not touched; the other 8 editions' glosses were verified correct questions and left untouched (de `Wie lange im Amt?`, fr `Quelle durée?`, it `Quanto dura?`, ja `任期はどれくらい？`, ko `임기는 얼마나?`, nl `Hoe lang?`, zh-tw `任期多長？`).
- es before: `HOW LONG? · El mandato` → after: `HOW LONG? · ¿Cuánto dura?` (deviation per §1).
- pt before: `HOW LONG? · O mandato` → after: `HOW LONG? · Quanto dura?` (deviation per §1).
- ru before: `HOW LONG? · Срок полномочий` → after: `HOW LONG? · Каков срок?` (deviation per §1).
- Verification: exact-title extraction on all 11 P6s; occlusion audit BOXTITLE class silent (titles fit their boxes); visually confirmed on all 3 P6 cards (`crops/b1-sheet.png`).

### B2 — ko only (blocking). ABSTRACT.txt typo.
- File: `files/weekly-report-w46-en-ko/ABSTRACT.txt`. One character: `댦` U+B326 → `뮌` U+BB8C. Before: `NFL 댦헨 경기` → after: `NFL 뮌헨 경기` (`뮌헨` = Munich; the body uses the correct form everywhere).
- Re-verified: single line + trailing newline, no ASCII double-quote, 479 bytes (unchanged — both characters are 3-byte UTF-8). No other ABSTRACT.txt was touched.

### B3 — ko only (blocking). P8 mid-word syllable splits, tail ≥3, ×2.
- (1) Salford split `솔 | 퍼드에서` (tail 4). Source: entry 68 note, `content56.py:37`. Before: `갈라쇼는 솔퍼드에서 생방송돼요` → after: `모금 갈라쇼는 솔퍼드에서 생방송돼요`. (Candidate `갈라쇼가…` still split S3 and was rejected; the chosen candidate was verified by a registry-based wrap simulation, `sim_ko.py`, which reproduced both S3 splits exactly pre-fix.)
- (2) `묵 | 념해요)` (tail 3). Source: entry 130 note, `content8.py:63`. Before: `전교생이 2분간 묵념해요` → after: `전교생이 2분 동안 묵념해요`. (Candidate `묵념을 해요` created a new S3 split and was rejected.)
- The notes appear only in the P8 keys paragraph (plus text.md answers), not on the P5/P8 exercise pages. The other 13 true splits (1–2-syllable tails) are below the S3 standard and were not churned.
- Verification: canonical `koscan.py` on the final ko SVGs: CANDIDATES 28, TRUE_SPLITS 13, **S3 = 0**, orphan final lines 0, line-start orphan punct 1 (the frozen P8 `! See you…` wrap convention, adjudicated O2 in Round 1). `솔퍼드` and `묵념해요` each sit unsplit on a single P8 line (extraction + visual, `crops/ko-p8-b3.png`). Ko P8-keys flow ends col 2/3 y=2535 (bottom 2545), no overflow.

### B6 — zh-tw only (blocking). Lone `。` alone on a line, P2 `B · WILL` bridge.
- Source: zh-tw `content12.py:256`, `e.expl("用 will + 動詞原形改寫（承諾與將要發生的事）。")` (bridge 20.5pt sans, width 434).
- Before: `用 will + 動詞原形改寫（承諾與將要發生的事）。` → after: `用 will + 動詞原形來改寫（承諾與將要發生的事）。` (`來` added; the praised `動詞原形` clarification kept — the alternative of dropping `原形` was rejected to preserve it).
- Verification: wrap simulation (before 2 lines with lone `。`; after 2 lines ending `）。`); extraction — no lone-`。` line on any edition's P2; visually confirmed on the zh-tw P2 card (`crops/b6-bridge.png`) and at full frame. The core wraps without the orphan and was not touched for B6.

### M1 — de/fr (minor). FINAL TEST header: English instruction untranslated.
- Source: `content8.py:11` band `sub`, 19pt sans, anchored end at x=1872. English kept + native line added (family pattern).
- de before: `FINAL TEST · Abschlusstest · Answers at the bottom of this page` → after: `… · Die Antworten stehen am Ende dieser Seite` (rendered width 988.8px, below the shipped es sub 1006.0px).
- fr before: `FINAL TEST · Test final · Answers at the bottom of this page` → after: `… · Les réponses sont en bas de cette page` (909.8px).
- Verification: exact extraction on both P8s; visually confirmed (`crops/m1-sheet.png`); occlusion audit silent (no band overflow).

### M2 — fr/ko/zh-tw (minor). Doubled gloss prefix on P2–P6 gloss boxes.
- Mechanism: `Flow.gloss()` in `bslib4.py:197` prepends the furniture prefix, and the 5 `f.gloss(...)` call strings repeated it (`content12.py:180`, `content34.py:28`, `content34.py:111`, `content56.py:26`, `content56.py:107` in each edition). P1 single-prefix lines (fr `instrline`, ko `bridge`, zh-tw `expl`) are correct and untouched. DE's `Anmerkung | Erklärung |` (two distinct labels) is accepted — untouched. es/it/ja/nl/pt/ru single prefixes clean — untouched.
- fr: leading `Note | ` stripped from the 5 call strings → rendered single `Note | …` (per FR KIT furniture claim).
- ko: leading `해설 — ` stripped from the 5 call strings → rendered single `해설 — …`.
- zh-tw: leading `譯注｜` replaced with `講解｜` in the 5 call strings → rendered distinct pair `譯注｜講解｜` (W45 shipped precedent). This corrects the ZH-TW KIT's single-prefix furniture claim; the correction is stated in the zh-tw KIT fix record.
- Verification: extraction — fr 5× single `Note |`, ko 5× single `해설 —`, zh-tw 5× `譯注｜講解｜`, de 5× distinct pair intact; visually confirmed on the P2 cards (`crops/m2-sheet.png`); all 15 boxes wrap-simulated (see §3 regression).
- Counts check: `rowcheck46.py` gloss-count compare 0 mismatches in all 11 editions.

### M3 — de (minor). "call a race = ein Rennen entscheiden" imprecise.
- Sources: both in `content56.py` — line 107 (P6 gloss) and line 148 (`f.ex` note → P8 note 95). Chosen rendering: `das Ergebnis verkünden` (closest to the family's "announce the result" wording; the alternative `den Wahlausgang verkünden` was not used).
- Gloss before: `to call a race = ein Rennen entscheiden` → after: `to call a race = das Ergebnis verkünden`.
- Note before: `call a race = ein Rennen entscheiden` → after: `call a race = das Ergebnis verkünden`.
- Verification: old wording count 0, new wording ×2 in the final SVGs; visually confirmed on the P6 card (`crops/m3-de-gloss3.png`).

### M4 — nl/pt (minor). P3 title drops the English title.
- Source: `content34.py:81` in each build dir.
- nl before: `v3.box("DE NACHT VAN SCROOGE"` → after: `v3.box("SCROOGE'S NIGHT · Scrooge-nacht"` (deviation per §1).
- pt before: `v3.box("A NOITE DE SCROOGE"` → after: `v3.box("SCROOGE'S NIGHT · A noite"` (deviation per §1).
- Translations themselves are correct and were kept. Verification: exact extraction; visually confirmed (`crops/m4-sheet.png`); occlusion BOXTITLE silent.

## 3. Regression found by re-gating and fixed (same defect class as B5/B6)

The M2 prefix removal re-wrapped two ko gloss boxes onto orphan final lines — a new defect introduced by this fix round, caught by the koscan re-run (Round 1 koscan: 0 orphans; first post-fix koscan: 1 orphan + 1 line-start orphan punct). Fixed at the source, wrap-simulated first, then ko alone was re-rendered and re-gated:

- ko P3 gloss (`content34.py:28`): `yet to come 아직 오지 않은.` → `yet to come 아직 오지 않은 것.` — final line now `은 것.` (3 lines, no orphan). Visually confirmed (`crops/ko-p3-gloss.png`).
- ko P4 gloss (`content34.py:111`): `a star 스타 선수.` → `a star 스타선수.` — box now 2 lines, period attached. Visually confirmed (`crops/ko-p4-gloss.png`).
- After the re-render: koscan S3 = 0, orphans 0, LEAD 1 (frozen P8 convention only); freeze total 2,375 (+1 Hangul char `것`, pure explanation layer); occlusion 0 flags; rowcheck clean; verify script 171/171.
- The fr and zh-tw gloss boxes were wrap-simulated with their final rendered strings after M2: all final lines substantial (fr 107–355px; zh-tw 61–260px) — no orphans, no further changes. A lone-punctuation scan across all 11 editions' final SVGs found only the (fixed) ko P4 `.`.

## 4. Observations flagged for Round 2 (out of scope, deliberately NOT changed)

- **es/fr P3 titles:** es `LA NOCHE DE SCROOGE` and fr `LA NUIT DE SCROOGE` render without the English head, contradicting the verdict's M4 statement that "the other 9 editions keep" the `SCROOGE'S NIGHT ·` pattern. Per the verdict/task scope (M4 = nl/pt only) and the no-invented-changes rule, es/fr were left untouched. Round 2 to adjudicate whether es/fr need the same M4 treatment.
- **Non-defects left untouched, as adjudicated:** FR masthead at 42pt; IT masthead flush fit; 2 residual U+FF1B fullwidth semicolons inside frozen P8 keys in Latin editions (freeze added-CJK 0 everywhere); model-text token count observation; W45-promise disclosure wording.

## 5. Build log summary (all editions: 0 warnings, TOTAL 150)

| Edition | run.py | render.py | webpdf.py (bytes / text bytes) | text.md (150 ex.) |
|---|---|---|---|---|
| core (zh-cn) | exit 0, 0 overflow, P7-tools ends y=881 | exit 0, 8 cards, print 27,918,597 | 2,017,005 / 45,003 | 37,890 chars / 43,545 bytes |
| de | exit 0, 0 overflow | exit 0, print 15,190,847 | 1,555,468 / 48,519 | 45,344 bytes |
| es | exit 0, 0 overflow (render stage interrupted once by a runtime abort mid-driver; re-run standalone, exit 0, print 15,187,759) | exit 0 | 1,552,515 / 46,197 | 45,873 bytes |
| fr | exit 0, 0 overflow | exit 0, print 15,263,470 | 1,557,915 / 49,189 | 45,876 bytes |
| it | exit 0, 0 overflow | exit 0, print 15,184,587 | 1,547,039 / 45,896 | 45,548 bytes |
| ja | exit 0, 0 overflow | exit 0, print 27,094,823 | 2,082,457 / 47,288 | 46,119 bytes |
| ko | exit 0, 0 overflow (×2 passes; P8-keys ends col 2/3 y=2535 < 2545) | exit 0 (×2), print 18,551,689 | 1,785,457 / 47,052 | 45,945 bytes |
| nl | exit 0, 0 overflow | exit 0, print 15,189,192 | 1,553,717 / 48,518 | 45,359 bytes |
| pt | exit 0, 0 overflow | exit 0, print 15,189,961 | 1,557,531 / 46,077 | 45,802 bytes |
| ru | exit 0, 0 overflow | exit 0, print 15,073,336 | 1,579,434 / 50,959 | 52,792 bytes |
| zh-tw | exit 0, 0 overflow | exit 0, print 24,611,678 | 2,204,469 / 44,908 | 43,595 bytes |

Text.md regeneration: `hidden_files/w46/en_textmd.py` reproduces the old exports byte-identically except for fix lines for 9 editions (changed line pairs vs `old-textmd/`: es 2, fr 7, it 1, ja 1, ko 8 — 5 M2 + B4 + 2 B3, the 2 regression re-breaks falling inside 2 of the M2 gloss lines — nl 2, pt 3, ru 2, zh-tw 8 — 5 M2 + B4 + B5 + B6 — all fix lines only). Core and de old text.md files were produced by a different/older exporter walk (`export_textmd.py`, hardcoded for the DE-target family, cannot run for EN editions as-is); all 11 were regenerated with the canonical exporter (uniform family format, headers verbatim — first 6 lines identical), and the format change is documented in the core/de KIT fix records. Old files preserved under `en-fix/old-textmd/`.

## 6. Re-gate results on the FINAL artifacts (all 11 editions)

Gate JSONs/logs live in this directory: `freeze-<ed>.json`, `p8-<ed>.json` (+ `p8-core.json`), `occlusion-<ed>.json` (+ `.log`), `rowcheck-<ed>.log`, `koscan-ko2.log`, `verify_fixes2.log`.

| Edition | freeze (added CJK, exit 0) | p8 compare --total 150 | occlusion (selftest OK) | rowcheck (COLLIDE / MISMATCH / GRAZE) |
|---|---|---|---|---|
| core | baseline | extract: 70 noted | 0 flags | 0 / 0 / 0.0% |
| de | 0 | EXTRA_ONLY 70→150, extra 80, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| es | 0 | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| fr | 0 | EXTRA_ONLY 70→150, extra 80, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| it | 0 | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| ja | 2,188 (= KIT claim) | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| ko | 2,375 (was 2,381; delta pure Hangul: M2 −10, B5 core −2, B3 +3, §3 fix +1, multiset sharing) | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| nl | 0 | EXTRA_ONLY 70→150, extra 80, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| pt | 0 | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| ru | 0 | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |
| zh-tw | 680 (was 679; +1 is the M2 `講解` pair, all Traditional Han) | CLEAN 70→70, missing [], uncertain [], keydiff [137,138,139,140,150] | 0 flags | 0 / 0 / 0.0% |

- P8 adjudication matches Round 1 exactly: the EXTRA_ONLY extra-number list is identical (80 numbers) for de/fr/nl; keydiff `[137,138,139,140,150]` is legitimate (137–140 translation keys, 150 open writing pointer); missing = [] and uncertain = [] everywhere; core noted = 70. Latin editions' freeze totals are 0 with the same 2 residual U+FF1B semicolons inside frozen P8 keys (core 721 CJK chars on P8 → edition 2).
- Script scan of rendered SVG texts (`script_scan.py`): Latin editions 0 non-Latin characters; ja Han 1,160 + Hiragana 928 + Katakana 402; ko Hangul 2,375 only (matches the freeze total); ru Cyrillic 5,437 only; zh-tw Han 1,728 only; core Han 1,625. No script leakage in any edition.
- Registry re-measured from the fixed core build (scratch copy, SVGs redirected to `regcheck-svg/`): 150 exercises, numbers 1–150 unique, no missing, no duplicates, every exercise keyed; per-page 10/17/18/18/18/18/12/39; levels A2 60 / B1 69 / B2 21.
- PDF checks (`verify_fixes.py`, 171 checks, 0 failures): every web PDF ≤ 7 MB, 8 pages (`pdfinfo`), `pdftotext` bytes > 0 and equal to the print-PDF extraction by the same method for every edition.
- Koscan (ko, canonical 10–45 window, source-adjudicated): S3 = 0, orphans 0 (see §2 B3 and §3).
- Visual checks: every changed page inspected at full frame or 2× crops of the changed element — P7 ×11 (B4; B5 on core + zh-tw), P6 ×3 (B1), P8 ko (B3), P2 zh-tw (B6), P8 de/fr (M1), P2 fr/ko/zh-tw + P3/P4 ko (M2 + §3 regression), P6 de (M3), P3 nl/pt (M4); plus full-frame reads of the core P7 card and the zh-tw P2 card. No overlaps, no clipping, no orphan lines remain. Crop evidence: `crops/`.

## 7. Final per-edition file inventory

Sizes in bytes (stat). "pdftotext bytes" = `pdftotext` stdout byte count, same method for web and print PDFs, equal for both per edition.

| Edition | text.md | web PDF | print PDF | pdftotext bytes (web = print) |
|---|---|---|---|---|
| core (zh-cn) `2026-w46-en-zh-cn` | 43,545 | 2,017,005 | 27,918,597 | 45,003 |
| de | 45,344 | 1,555,468 | 15,190,847 | 48,519 |
| es | 45,873 | 1,552,515 | 15,187,759 | 46,197 |
| fr | 45,876 | 1,557,915 | 15,263,470 | 49,189 |
| it | 45,548 | 1,547,039 | 15,184,587 | 45,896 |
| ja | 46,119 | 2,082,457 | 27,094,823 | 47,288 |
| ko | 45,945 | 1,785,457 | 18,551,689 | 47,052 |
| nl | 45,359 | 1,553,717 | 15,189,192 | 48,518 |
| pt | 45,802 | 1,557,531 | 15,189,961 | 46,077 |
| ru | 52,792 | 1,579,434 | 15,073,336 | 50,959 |
| zh-tw | 43,595 | 2,204,469 | 24,611,678 | 44,908 |

Each edition dir also holds 8 SVGs (`svg/`) and 8 cards (`cards/`), all re-rendered from source, plus `ABSTRACT.txt` (only ko changed, one character) and `WEEKLY-KIT.md` (fix record appended to all 11).

## 8. Files changed

Build sources (via `apply_fixes.py`, occurrence-count asserted, log `apply_fixes.log`, FAILURES: 0; plus the §3 ko edits asserted ×1 each):
- Core: `weekly-report-w46-en-build/content7.py` (B4 line 51, B5 line 115).
- de: `content7.py` (B4), `content8.py` (M1), `content56.py` (M3 ×2).
- es: `content7.py` (B4), `content56.py` (B1).
- fr: `content7.py` (B4), `content8.py` (M1), `content12.py`/`content34.py`/`content56.py` (M2 ×5).
- it: `content7.py` (B4).
- ja: `content7.py` (B4).
- ko: `content7.py` (B4), `content56.py` (B3 entry 68), `content8.py` (B3 entry 130), `content12.py`/`content34.py`/`content56.py` (M2 ×5), `content34.py` (§3 regression ×2).
- nl: `content7.py` (B4), `content34.py` (M4).
- pt: `content7.py` (B4), `content56.py` (B1), `content34.py` (M4).
- ru: `content7.py` (B4), `content56.py` (B1).
- zh-tw: `content7.py` (B4, B5), `content12.py` (B6 + M2 ×1), `content34.py`/`content56.py` (M2 ×4).
- Edition files: `files/weekly-report-w46-en-ko/ABSTRACT.txt` (B2, 1 char). All 11 `WEEKLY-KIT.md` (fix record appended). All 11 `<slug>.text.md` (regenerated; see §5). All SVGs/cards/PDFs re-rendered.
- Nothing else was changed: `~/workspace/weekly-git` untouched, `index.json` untouched, no push, no insert, no Discord post, no chat dump. The shared registry snapshot `hidden_files/w46/en-core/registry.json` was re-dumped from the fixed core build (same counts as Round 1).

## 9. B4 orphan confirmation (required restatement)

The P7 toolbox lone `»` is gone in ALL 11 editions, not just the core: every edition's P7 SVG carries the B1 toolbox sentence as two lines, `B1 — « Dickens wrote the story in` (y=443.1) and `1843.»` (y=477.3), with no `<text>»</text>` element anywhere on any P7; `verify_fixes.py` B4 checks pass 11/11; the P7 cards of all 11 editions were visually inspected at 2× resolution and the core P7 card at full frame. The fix was made in the frozen core source and propagated by full re-render of every edition.

## 10. Handoff to Round 2

- Two deviations need adjudication: B1 fitting question forms (es/pt/ru) and M4 short glosses (nl/pt) — measurements in §1.
- One observation needs a scope decision: es/fr P3 titles without the English head (§4).
- The zh-tw KIT furniture claim is corrected by its fix record (distinct pair `譯注｜講解｜`, not single `譯注｜`).
- Ko P8 retains 13 true mid-word splits with 1–2-syllable tails (below the S3 standard, per the verdict) and the frozen P8 `! See you…` line-start convention; both are pre-existing and adjudicated, not regressions.
