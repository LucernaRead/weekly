# WEEKLY-KIT — La Lucerna VOL.3 · W46 IT × Traditional Chinese (2026-w46-it-zh-tw)

## 1. Spec
- Issue: week Mon Nov 9 – Sun Nov 15, 2026; issue dated Mon Nov 9, 2026. VOL.3, Italian target.
- Format: 8 pages, 1950×2700 px, 4 columns, warm ivory paper, dark olive-green accents. Masthead: "La Lucerna" (UnifrakturMaguntia).
- Pairing / explanation layer: **Italian text + explanations in Traditional Chinese (繁體中文)**. The Italian article text is the frozen core layer, byte-identical in content to the W46 IT core (`files/weekly-report-w46-it-core/`); only the explanation layer (glosses, bridges, instructions, answer notes, furniture) is in Traditional Chinese. Verified by `freeze.py diff` (see §8): every removed string is a Chinese explanation/furniture string, every added string is Traditional Chinese (plus frozen Italian heads/grammar items).
- Exercises: 150 total, continuously numbered 1–150. By page: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38. By level: A2 47, B1 70, B2 33. P8 writing model text: 98 words (brief 80–100).
- P8: sections A cronaca 8, B generali 8, C leggi e rispondi 4, D frasi 4, E traduci 4, F matching 4, G dialogo 5, H scrittura 1. Answers generated from the exercise registration table in the build code (content12/34/56/7/8.py), not hand-typed. P8 answer style: dash style `N. key — note`; writing items `N. ✓ note`. P8 header: `RISPOSTE · 全部答案與簡析（第 1–8 版）`; note line: `每題附一句中文簡析 · 帶 ✓ 的為範文題`; page separator `— PAGINA {pg} —` (13, lh 1.14, gap 0.5).
- P7 golden sentences: the same 8 quotes as the core, each verified to occur exactly 2× in the joined SVG text (once in its article, once on P7) — see §8.

## 2. Contents per page
Identical Italian content to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §2 (P1 Prima / P2 Vita / P3 Cultura / P4 Sport / P5 Giovani / P6 Approfondimento / P7 Lingua / P8 Valutazione e risposte, exercises 1–150 in the same order). Only the explanation layer differs (this KIT §§1, 7–8). No page was restructured for this edition.

## 3. Lead topic
«San Martino» — as the core (W46 IT core KIT §3). No new lead, no new topic introduced by the explanation layer.

## 4. Trend / fact sources
Identical to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §4. The explanation layer adds NO new facts: glosses translate the Italian words, bridges paraphrase the Italian articles, and the P6 practice chart keeps its Italian data and its on-page `DATI INVENTATI PER L'ESERCIZIO` disclaimer (chart title translated, data frozen — verified in the freeze diff, §8). No international politics anywhere; Italy domestic politics (manovra) as in the core, with the same `not yet law` disclosures.

## 5. Images (public-domain / CC0 only, per SOP)
Identical to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §5 (P3 tartufo PD, P5 castagne CC0, programmatic frost/clocks/chart). No new image in this edition.

## 6. Verification, corrections, and promises
Identical to the core — see `files/weekly-report-w46-it-core/WEEKLY-KIT.md` §6 (Festival date correction, Torrone promise, manovra `not yet law`, no real letters, VOL.4 promises). Fan-out specifics: the P7 disclosure is translated into Traditional Chinese with the same meaning (editor's example, no real letters/best texts had arrived, promise carries to VOL.4, write to the editors); the P8 E-section keys 137–139 are legitimate translation re-aims (the Italian stems are re-aimed at the Traditional Chinese-speaking reader — `p8.py` keydiff, §8), key 140 keeps its Italian sentence with a Traditional Chinese stem gloss. No fabricated readers, letters, names, or quotes.

## 7. Build / repro
- Build dir: `hidden_files/weekly-report-w46-it-zh-tw-build/` (content12/34/56/7/8.py, bslib4.py, svglib.py, render.py, run.py, transform.py). Single one-process driver: `cd hidden_files/weekly-report-w46-it-zh-tw-build && ../../tools/venv/bin/python run.py` then `render.py` (tools venv; system python3 has no cairosvg). Render produces cards + print PDF only; the web PDF is built separately with `tools/webpdf.py` (never PIL whole-page JPEG).
- `transform.py` files were NOT edited (W45-harvested generation artifacts); all fixes below were applied to the `content*.py` sources and are recorded here.
- `.text.md` was exported from the edition's own build sources with the AST exporter `hidden_files/w46/it-finish/export_it_textmd.py` (source manuscript, never from PDF/SVG), and validated two-way against the shipped SVGs with `hidden_files/w46/it-finish/validate_textmd.py` — see §8.
- `svglib.py`: Core svglib with `_tc_index` / TC face selection. Functional: Traditional Chinese glyphs; no other difference.
- Fix record (source fixes, full re-render + re-gate after each round):
No source fixes. Shipped as built by the family transform pipeline; no re-render was needed (gates + proofread clean on first pass).

- Fix record — Round 1 independent-proofread fixes (2026-11-03, fix worker; all fixes at source in `content*.py`, never in rendered SVGs/PDFs; full re-render + full re-gate after the round; asserted-replacement log `hidden_files/w46/it-fix/apply_fixes.log`, 137/137 applied):
  1. D1 (all 11, CORE): `content12.py` P1 IN BREVE FESTIVAL cross-reference `(Pagina 5)` → `(Pagina 2)` — the Festival closing coverage is on P2 (`E LA SETTIMANA SCORSA?`), not P5. MANOVRA → Pagina 6 and RICERCA → Pagina 4 in the same box were already correct.
  2. D2 (all 11, CORE): `content34.py` ex. 56/57 contradicted the issue's own facts (both matches kick off 20:45 — P1, P4 article, fixture table). Stems gained NON (`Le partite di domenica sera NON cominciano ___ …`, `Le partite di giovedì NON cominciano ___ …`); keys unchanged (`più tardi` / `più presto`); P8 notes rewritten in each reader language to state both matches at 20:45 + the negation. No other exercise or key changed.
  3. D3 (all 11, CORE): `content12.py` P2 agreement fixed: `si sono chiusi il Forum Cultura … e si sono aperti la finale del Panettone e la Festa del Torrone` → `si è chiuso il Forum Cultura … e si sono aperte la finale del Panettone e la Festa del Torrone`.
  4. Q1 (all 11, CORE, query resolved as ERROR): `content7.py` B2 column `la finale è a Perugia` has no referent anywhere in the issue — the only `finale` mentions are the Panettone finale (no location given) and `quarti di finale` (Mar 2027, no location); Perugia hosts Eurochocolate (an opening, not a finale). Replaced with the verified fact `la Festa del Torrone è a Cremona` (P1 + P3). No referent was invented.
  5. Stranded line-start punctuation reflowed (0 hits after fix; scan of all SVG text nodes): P1 cifre item 1 `11 — 11月、聖馬丁節那天、週三（聖馬丁節，11 月 11 日週三）` → `11 — 11月11日週三，聖馬丁節` (one line); P5 plan item 3 `（週五：巧克力節開幕）` → `（週五巧克力節開幕）` (wrap now breaks before 巧, never before punctuation).
  6. Terminology unified to 將來時 (majority form, 7 source sites; no core KIT mandate for this term): `content7.py` 未來時 → 將來時 ×3 (P7 bridge + P8 items 102/104 notes). Rendered total: 將來時 ×10 (P5+P7 bridges + P8 76–79, 101–104), 未來時 ×0.
  7. D5: `content8.py` items 146/147/148 → `=` (`mandorle = 杏仁`, `quanto costa? = 多少錢`, `pagare con carta = 刷卡` — item 148 included under `normalize to = everywhere`, same defect class).
  Changed pages vs pre-fix snapshot (SVG sha256): P1, P2, P4, P5, P7, P8; all other pages byte-identical. ABSTRACT.txt unchanged (still valid: single line, no ASCII double quotes).

## 8. Gates
- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; TOTAL 150; levels A2 47 / B1 70 / B2 33; pages 10/18/18/18/18/18/12/38; model text 98 words. Counts re-verified on the shipped SVGs via `p8.py` (150 noted), freeze numbering coverage 1–150, and the SVG text layer; no re-render was run for this edition (see fix record).
- `tools/freeze.py diff` vs core (log `hidden_files/w46/it-finish/freeze2-zh-tw.log`): all pages compared; TOTAL added CJK characters 972. Added CJK = the Traditional Chinese explanation layer itself. String-set review: 0 Simplified-Chinese-only marker strings — this edition was written natively in Traditional and never converted from the zh-cn core. Removed strings are Chinese explanation/furniture strings only; no Italian body string was removed or added (Italian-heavy added strings are frozen box titles and P7 grammar trigger phrases, adjudicated).
- `tools/p8.py compare` vs core P8 (log `hidden_files/w46/it-finish/p8-2-zh-tw.log`): status CLEAN, 150 noted = 150 noted, missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139] — the three E-section re-aims, verified per edition in the proofread (see §6).
- `tools/occlusion_audit.py` (selftest OK every run, log `hidden_files/w46/it-finish/occlusion2-zh-tw.log`): Round 1: 0 flags. Round 2 (final): 0 flags. Every flag was adjudicated on pixels; final state 0 flags on the 8 shipped SVGs (incl. LINEX + same-baseline furniture scan + chart GRAZE element-check; P6 chart frozen Italian).
- `.text.md` validation: forward-miss 1 / reverse-miss 0. The forward miss is the registry-only writing-item note `（開放題，範文如下）` (the SVG renders the equivalent header `範文（98 詞）見下`). No content miss.
- Web PDF: `tools/webpdf.py <svg-dir> La-Lucerna-VOL3-ZHTW-web.pdf` — 1,463,313 bytes (< 7 MB); `pdftotext` 44,394 bytes, byte-identical to the print PDF's text; 8 pages.
- Golden sentences: all 8 occur exactly 2× in whitespace-normalized joined SVG text (re-checked on the final shipped SVGs).
- Scans: Simplified-Chinese residue 0 in this edition's SVGs (except the native-script editions ja/ko/zh-tw, adjudicated above); gloss headwords attested in body text (12/12); exercise numbers 1–150 complete; dates/weekdays as core (calendar-checked).
- Visual: fixed regions pixel-checked on the final cards (P1 box/subtitle, instruction sites, P7 FRASI band + gold rule, P1 top-band same-baseline scan). Proofread round 1 (gates + pixel adjudication + source scans) and round 2 (full re-gate + explanation-layer read: freeze added strings P1–P7, E-keys, gloss attestation) — zero open issues at定稿.

- Round-1 fix re-gate (2026-11-03, fix worker, logs `hidden_files/w46/it-fix/`): `freeze.py diff` vs core (freeze-zh-tw.log) — TOTAL added CJK characters 968; 0 long Italian body strings in any added/removed set (no frozen-layer drift); `p8.py compare` (p8-zh-tw.log) — status CLEAN, 150 noted = 150 noted, missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139]; `occlusion_audit.py` (occlusion-zh-tw.log, selftest OK) — 0 flags on all 8 shipped SVGs; build logs 0 FLOW OVERFLOW / 0 HEAD TOO WIDE, TOTAL 150 (10/18/18/18/18/18/12/38; A2 47 / B1 70 / B2 33); `.text.md` validation (forward-miss 1 / reverse-miss 0 (registry-only writing note; as builder's)); web PDF 1,463,313 bytes (< 7 MB), `pdftotext` 44,394 bytes, byte-identical to the print PDF's text, 8 pages; changed pages proofread on pixels (core P1/P2/P4/P7, EN P1 strapline, RU+PT P7 letters boxes, ZH-TW P1 cifre + P5 plan, NL P8 foot, KO P8) + full changed-text verification against the SVGs (`hidden_files/w46/it-fix/verify_svgtext.py`, 0 failures).

## 9. Furniture registry (measured from this edition's build sources)
- Footer (bslib4.py, y=2624): `La Lucerna · 義大利語週報 VOL.3 · 正文義大利語 · 講解繁體中文`
- Page line (bslib4.py): `第 {n} 版 / 共 {total} 版`
- Gloss prefix (bslib4.py `gloss()`): `譯注｜ `
- P1 badge: INSERTED at y=574 (22pt BRICK, strapline at y=372 kept): `義大利語正文 · 繁體中文講解 — 給繁體中文讀者的版本`
- P1 band right lines: `本週是聖馬丁週` / `聖馬丁之週 · 詳見第 2 版`
- P1 week-plan box subtitle: `本週日程 · Cosa succede, giorno per giorno`
- Masthead strapline (y=372, 19pt GREY, frozen Italian): `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA` (replaced by the badge in es/ja/nl — see badge line).
- Top strip (y=92): left `VOL. 3 · TERZA EDIZIONE`, right `SETTIMANA DAL 9 AL 15 NOVEMBRE 2026`, centre `OGNI SETTIMANA IN ITALIANO · <native strapline>` (same-baseline collision scan clean).

## 10. Files shipped (edition dir `files/weekly-report-w46-it-zh-tw/`)
- `svg/` — 8 shipped SVGs (p1-prima … p8-valutazione).
- `cards/` — 8 PNG cards (1950×2700).
- `La-Lucerna-VOL3-ZHTW.pdf` — print PDF (vector, text layer), 19,363,047 bytes.
- `La-Lucerna-VOL3-ZHTW-web.pdf` — web PDF (text layer, < 7 MB), 1,463,313 bytes.
- `2026-w46-it-zh-tw.text.md` — manuscript text export (from the source manuscript, never from PDF), 53,103 bytes, 150 exercises.
- `ABSTRACT.txt` — Traditional Chinese, one line, no ASCII double quotes.
- `WEEKLY-KIT.md` — this file.
- Gate logs: `hidden_files/w46/it-finish/freeze2-zh-tw.log`, `p8-2-zh-tw.log`, `occlusion2-zh-tw.log`.
