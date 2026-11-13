# La Lucerna · 西班牙语周报 VOL.4 — WEEKLY KIT (es-en)

**Edición:** VOL.4 · **Semana:** lunes 16 — domingo 22 de noviembre de 2026 · **Fecha de portada:** lunes 16 de noviembre de 2026
**Pareja de idiomas:** texto en español + explicaciones en inglés (English-speaking readers) — fan-out of the定稿 core `core-es/` (zh-cn reader edition). Target-language text frozen; only the explanation layer was rewritten in English.
**Lead story:** La campaña arranca — «La campaña arranca: trece días para el 29-N» (same as core).

---

## 1. Spec

- **Masthead: “La Lucerna”** (UnifrakturMaguntia, 196 units = 147pt). Spanish article **La** (la lucerna is feminine, as in core). Furniture in English: footer “La Lucerna　Spanish Weekly VOL.4　LUCERNA SPANISH WEEKLY”, note prefix “Note |”, section glosses in English.
- 8 pages, 1950×2700, four columns (COLX = [65, 527, 989, 1451]), paper #fbfaf6, book-green #37402f, olive #46581f (same layout system bslib4 as core; only the explanation strings and the PDF names changed).
- Difficulty ramp and exercise numbering identical to core: P1 A2 · P2 A2 · P3 A2→B1 · P4 B1 · P5 B1 · P6 B2 · P7 A2/B1/B2 · P8 assessment + writing + all answers. 150 exercises, unified numbering 1–150, answer key generated from the registry (REG).
- **Explanation-layer conventions (fan-out):** English only in glosses, Notes boxes, section instructions, P7 language columns' bridges, answer notes, masthead/footer pairing labels, “Your turn” translations, the F-MAIL editor's note, and the P6 band subtitle gloss. No Chinese anywhere in visible text (0 CJK chars in the 8 SVGs' text elements; the only CJK is the non-rendered `<title>Lucerna 三色蛾</title>` inside the inherited moth mark — identical to core, not visible, left as is).
- F-MAIL: the core's editor's-sample letter (Marta, marked ejemplo, written by the editors) is kept verbatim in Spanish; the disclosure is given in Spanish (frozen) + an English editor's note. No real letters invented; promise carried to VOL.5.
- P7 golden sentences: 8 sentences verbatim from this issue's articles, with English glosses.
- **W47 images:** same four PD/CC0 pictures as core (P3 Sargent, P5 Jebulon ballot box, P7 Book of Hours initial, P8 swan pen); captions' Spanish text frozen, credit lines unchanged.

## 2. Per-page contents

Identical to core (see `core-es/WEEKLY-KIT.md` §2). Only the explanation layer differs, per page:

| Page | Explanation layer in English |
|---|---|
| P1 | Masthead pairing “TEXT IN SPANISH　EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS”; Note gloss (5 words); “LA SEMANA EN CIFRAS　Numbers” with English parentheticals; “AHORA TÚ　Now you try”; “LA PALABRA” gloss ““Debate”: two or more people discuss in public.” (one line, 18 units); “EN ESTA EDICIÓN　In this issue”; “QUIZ RELÁMPAGO　Lightning quiz” + “Read the front page and choose　Answers on page 8” |
| P2 | “EL CALENDARIO　This week” (each day with an English parenthetical); Note gloss (4 words); “DECIR LA HORA” section is Spanish teaching text (frozen); “LOS DÍAS DE LA SEMANA　Saying the date”; “¿Y TÚ?　Your turn” + English translation; “EJERCICIOS　Page 2 exercises” + section instructions in English; C-section intro “Read the article and choose the answer.” |
| P3 | Note gloss (5 words); “LO QUE QUEDA DE NOVIEMBRE” (Spanish, frozen); “EL FLAMENCO, EN TRES DATOS” (Spanish, frozen); “¿Y TÚ?　Your turn” + English translation; exercise instructions in English |
| P4 | Note gloss (5 words); “LA CHAMPIONS VUELVE” (Spanish, frozen); “¿Y TÚ?　Your turn” + English translation; “LA JORNADA 13　LOS SEIS PARTIDOS DE LA SEMANA　Matchday 13: the six games”; exercise instructions in English |
| P5 | “EL PLAN DE LA SEMANA　The plan” (each item with an English parenthetical); Note gloss (5 words, incl. la papeleta); “VOTAR POR PRIMERA VEZ” (Spanish, frozen); “¿Y TÚ?　Your turn” + English translation (3 lines, 19 units); exercise instructions in English |
| P6 | Band subtitle gloss “Reading the campaign: debates, programmes and polls”; “EL CAMINO AL 29N” + “LEER UN DEBATE” (Spanish, frozen); “LOS MINUTOS GRATIS EN RTVE　minutos de propaganda por partido”; exercise instructions in English |
| P7 | “LENGUA　Language focus”; three bridges in English (A2 time, B1 comparatives, B2 subjunctive); “ERRORES TÍPICOS　Mistakes” (4 items, English notes); “LA PALABRA　Word of the week” (English gloss: “debate = debate: a public discussion, taking turns; the election is on the 29th.”); “CARTAS DE LOS LECTORES” (Spanish letter frozen; English editor's note); “FRASES DE LA SEMANA　Sentences of the week (quoted word for word from this issue)” (8 quotes + English glosses + page refs); “LA PRÓXIMA SEMANA　Next week (VOL.5)” |
| P8 | “EJERCICIOS Y RESPUESTAS　Exercises and answers”; H-section bridge “Writing task (no single right answer); model text (97 words) below.”; “RESPUESTAS　Answer key — arranged by page; just find the number” + “One short English note per item　✓ marks the writing task”; all 150 answers with one short English note each |

## 3. Measured totals (measured, not estimated)

- **Total: 150 exercises** (target ~150, met). By level: A2 50 · B1 72 · B2 28. By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38. By type: Sentence completion 48 · Multiple choice 47 · Vocabulary matching 12 · True or false 8 · Sentence building 7 · Sentence transformation 10 · Cloze choice 13 · Translation 4 · Writing 1. Model text 97 words.
- Build warnings: **FLOW OVERFLOW 0 · HEAD TOO WIDE 0** (final build 5).
- Golden sentences: 8/8, each appearing exactly twice in the 8 SVGs (original + P7 quote).
- Answers: `tools/p8.py extract` **150/150**; `p8.py compare` vs core **CLEAN**, missing=[] extra=0, keydiff=[137, 138] (translation items re-aimed: keys are the English sentences, per the W45/W46 ES×EN ruling; bodies 139/140 are the English source sentences with Spanish keys frozen).
- **P8 answer font size measured 10.125pt** (SVG 13.5 units × 0.75; PyMuPDF/pypdf `Tm` parse of the print PDF, P8 minimum), above the SOP §1.1 floor of 9.75pt.
- P8 keys flow ends y=2569 (nominal flow bottom 2560): no OVERFLOW warning; last key (150) baseline 2553.1, ink bottom ~2557, 39px above the footer rule (2596); visually clear of the footer. Accepted as-is (see §6.5).
- P7 col3 ends 1844.51 — identical to core; preview banner bottom 2582.5, same as core.
- P5 col3 ends 1574.55 (core 1580.55; the English box bottom was 1638.55 before the fix, 58px taller; after the fix it ends 6px above core's end).
- PDFs (fix2-port rebuild, 2026-11-11): print `La-Lucerna-VOL4-es-en.pdf` **3,500,997 B**, SHA-256 `b7f7931f6c2f43280f25c5db12cd35c4991ba260602a880e6dc9eab399c88fd9`; web `La-Lucerna-VOL4-es-en-web.pdf` **886,824 B** (< 7 MB), SHA-256 `f1221df30164ea0485c98291c6d868a425e406e90d8315a495dabc7b28bd3839`, built by `tools/webpdf.py`, text layer pdftotext **45,946 bytes**, byte-identical to the print PDF's text layer. (Previous: re-fanout 2026-11-11 print 3,500,924 B `80b4ce0a…`, web 886,730 B `f03047b1…`; build 5 print 3,500,745 B `e881ebb9…`, web 849,020 B `8ab8c66c…`.)
- PDFs (D5 rebuild, 2026-11-12, see KIT tail D5 record): print `La-Lucerna-VOL4-es-en.pdf` **2,915,634 B**, SHA-256 `3ece32511f03d5483b2a8fb20cc1bca664513dc9af2d95b60ff847024848e11e`; web `La-Lucerna-VOL4-es-en-web.pdf` **806,132 B** (< 7 MB), SHA-256 `23a06fabd738cc15d052d17a9302903200389da9376a5db3be197109a7bf9033`; 印/网 pdftotext 44,302 字符、8,430 词，逐字一致。
- 8 page PNGs 1950×2700 (cards/).
- .text.md: `2026-w47-es-en.text.md`, 1,779 lines, exported from the production SVGs in column reading order (never from the PDF); numbers 1–150 all present; 0 CJK chars; no “12 de noviembre” (the 12 November decree date stays out, per W45/W46 rule).
- Gloss-word token counts per page (core §8.1 method): every Note word occurs ≥2 times in its page's text (P1 reflexión 2 · P2 mitin/cartel/escaño 2 · P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6 · P4 parón 2 / liderato 3 · P5 papeleta 2 / censo 3 / plazo 3).

## 4. Benchmark

- Same as core (§4): 150 exercises vs the ~154 of the benchmark issue; B2 light (28, 18.7%) — same structural note as core, reported not padded.
- Print PDF is much smaller than core's (3.5 MB vs 17.2 MB) because the core embeds large CJK font subsets for its Chinese explanations; the images are byte-identical in both PDFs (verified per-page image sizes).

## 5. Sources

Same as core (`core-es/WEEKLY-KIT.md` §5): campaign calendar, debates, RTVE minutes, LaLiga matchday 13, Champions League, flamenco/Santa Cecilia, and the four PD/CC0 images. No new facts introduced; no new research done in the fan-out. The 12 November decree date was not reintroduced (no second independent source).

## 6. Adjudications (fan-out fixes)

1. **P1 word gloss wrapped to 2 lines and its ink crossed the y=1844 divider (occlusion LINEX).** Core's Chinese gloss fits 1 line. Fix: shortened the English gloss to ““Debate”: two or more people discuss in public.” at 18 units (13.5pt, top of the §1.1 explanation range); the “taking turns and asking questions” detail is preserved in the Spanish definition above it and in the P7 word-box gloss.
2. **P7 preview banner pushed down onto the footer (occlusion FOOTER + LINEX + TEXTX).** English explanations made P7 col3 end 1931.5 vs core 1844.51, so the “LA PRÓXIMA SEMANA” banner bottom reached 2669.5, overlapping the footer line and footer text. Fix (content only, no layout hacks): shortened the P7 word-box English gloss to “debate = debate: a public discussion, taking turns; the election is on the 29th.” (3→2 lines) and the F-MAIL English editor's note to “Editor's note: no real letters had arrived by press time. This issue prints a sample letter; the promise moves to VOL.5.” (5→3 lines). Col3 now ends 1844.51 — exactly core's value; banner bottom 2582.5.
3. **P8 RESPUESTAS header note overlapped the swan-photo caption (occlusion TEXTX).** The right-hand note “One short English note per item　✓ marks the writing task” shared the caption's baseline zone. Fix: moved the RESPUESTAS header (title + note) from y=1302 to y=1337 and the keys flow start from 1328 to 1363; keys end moved 2443→2569 (see §3; no overflow, visually clear).
4. **P2 C-section intro orphaned across columns (found by visual inspection + bridge sweep; invisible to occlusion/p8).** The 2-line bridge “Read the page 2 article and choose the correct answer.” split at the column break: line 1 stayed in column 2, line 2 (“correct answer.”) was drawn alone at the top of column 3, orphaned from its section. Fix: shortened the intro to one line, “Read the article and choose the answer.” (wrap-verified 1 line at 20.5 units). Sweep: all other multi-line bridges in the edition verified contiguous in-column (script `scratch-fanout-es/bridge_sweep2.py` — 0 orphans after the fix).
5. **P5 “¿Y TÚ?” box crossed the EJERCICIOS divider (visual-only; shape-vs-line blind spot in the audit, same class as core §6.7).** The English translation ran 5 lines; the box bottom reached 1638.55, 30px below the y=1608 divider, with “them in.” dangling below the rule. Fix: tightened the English to “Would you vote by post or in person? Black Friday: something useful, or a whim? Write two sentences and send them in.” at 19 units (3 lines, keeps the useful/whim choice and the instruction). Box now ends 1574.55, 33px above the divider. Full-edition box-vs-hline sweep: no other box crosses any divider.
6. **Letter full-width parentheses.** The Spanish letter carried core's full-width “（ejemplo, escrito por la redacción）”. Per the W46 ES×EN precedent (core full-width → fan-out half-width), changed to “(ejemplo, escrito por la redacción)”.
7. **P6 band subtitle gloss completed.** The harvest had shortened it to “Reading the campaign”; the other five bands translate their subtitles in full, so it now reads “Reading the campaign: debates, programmes and polls” (985.9 units wide at 18 units, end-anchored, fits the band).
8. **P8 keys end 9px past the nominal 2560 flow bottom (see §3).** Accepted: no OVERFLOW warning was raised (the flow's `_fit` passed), the last ink is 39px above the footer rule, and the rendered page is visually clean.
9. **keydiff [137, 138]** in `p8.py compare`: adjudicated, not a defect — translation items 137/138 are re-aimed per the W45/W46 ES×EN ruling (English-sentence keys; Spanish bodies frozen). All other 148 keys byte-identical to core.
10. **Non-rendered `<title>Lucerna 三色蛾</title>`** in the P1 moth mark (inherited from core, identical there): left unchanged — it is SVG metadata, never rendered, and changing shared furniture is out of the fan-out's scope.

## 7. Build commands (reproduction) and mechanical gates

- Build directory: `production/2026-w47/2026-w47-es-en/` (whole-core copy; explanation strings edited in place).
- Full build (single process): `cd production/2026-w47/2026-w47-es-en && ~/workspace/weekly-git/tools/venv/bin/python run.py` (build 5 log `hidden_files/w47/scratch-fanout-es/es-en-build5.log`: rc=0, OVERFLOW/TOO WIDE 0, TOTAL 150, MODELO 97 words; P5 col3 1574.55, P7 col3 1844.51).
- Render PNG + PDFs: `~/workspace/weekly-git/tools/venv/bin/python render.py` (rc=0; print 3,500,745 B, web 849,020 B, 45,339 text bytes).
- Occlusion audit: `tools/occlusion_audit.py production/2026-w47/2026-w47-es-en/svg` → **0 flags** (selftest six classes fired; `es-en-occlusion5.json`).
- P8: `tools/p8.py extract --p8 …/svg/p8-ejercicios.svg --total 150` → **150/150**; `p8.py compare` vs core → **CLEAN**, keydiff=[137, 138] (adjudicated, §6.9).
- Freeze: `tools/freeze.py baseline --build production/2026-w47/2026-w47-es-en --core-svg …/svg --out …/freeze-es-en-5` (tool reports per-page OK; direct sha256 of its `build-copy/svg` vs shipped `svg/`: **8/8 identical**).
- Web PDF acceptance: pdftotext print 45,339 bytes = web 45,339 bytes, byte-identical; web < 7 MB.
- P8 minimum font: 10.125pt (≥ 9.75pt floor).
- §1.1 spot checks: paper #fbfaf6 on all 8 pages; gold/brick-red/near-black 0 (moth-mark yellows #d7b257/#edd17f are the brand moth, as in core); badge tricolour A2 #5c6e30 / B1 #46581f / B2 #37402f; masthead 196 units = 147pt; VOL.4 ×9 in text (VOL.5 ×3 are all legitimate forward references to next week's issue); P8 badges: 35 rects, same counts as core (A2 11 / B1 21 / B2 3), Q113–150 all badged, none missing.
- Text export: `2026-w47-es-en.text.md` (1,779 lines) via the core's `extract_text2.py` (copied as `scratch-fanout-es/extract_text_es_en.py`, only the title slug changed).
- ABSTRACT.txt: English, one line, no ASCII double quotes (see file).

## 8. Self-proofread record

- **Round 1 (build 2, previous builder 59159d68):** run rc=0, TOTAL 150, P8-keys y=2443; render never completed (quota error on the log redirect; render.py never started).
- **Round 2 (build 3, this builder):** render completed (print 3,501,211 B, web 849,883 B); mechanical gates: p8 extract 150/150, compare CLEAN (keydiff 137/138); occlusion **5 flags** (P1 LINEX gloss/divider, P7 FOOTER+LINEX+TEXTX preview banner, P8 TEXTX header/caption); freeze direct sha256 8/8; pdftotext identical (45,358 B). Visual: P1–P2 read. **Found 5 issues** (§6.1–6.3, plus the letter parens §6.6 found by the full-width sweep).
- **Round 3 (build 4):** 5 fixes applied (P1 gloss, P7 gloss + editor's note, P8 header move, parens). Gates: run rc=0, 0 overflow; occlusion **0 flags**; p8 CLEAN; bridge sweep **1 orphan** (P2 C-intro, §6.4) found by the new sweep + visual; box-vs-hline sweep found the P5 box crossing (§6.5); P6 band gloss completed (§6.7). Visual: P1–P6 read.
- **Round 4 (build 5, final):** 3 fixes applied (P2 C-intro to 1 line, P5 “Your turn” to 3 lines at 19 units, P6 band gloss). Gates all green: run rc=0, 0 overflow; occlusion **0 flags**; p8 CLEAN; bridge sweep 0 orphans; box-vs-hline sweep clean; freeze direct sha256 8/8; pdftotext identical (45,339 B); P8 min font re-measured 10.125pt. Full re-read: .text.md 1,779 lines read end-to-end (English layer checked line by line; Spanish frozen text as in core); 8 rendered pages viewed; 150 answer keys read against their stems (all consistent with core). **This round: zero findings.**
- Final state: **zero known defects** (independent proofreading still to be done by the coordinator's reviewer).
- Not inserted, not pushed, nothing committed. No files outside `2026-w47-es-en/` and the scratch record directory were modified.

## 9. 重建（re-fanout，2026-11-11 — core build 10）

Core baseline: core-es fix build 10 (independent re-proof (a), zero findings) — print 17,212,955 B SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`, web 1,410,471 B SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`, text.md 1,822 lines SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.
Method: old edition backed up to `scratch-refanout-es/backup-old/` (verified identical), deleted, re-applied via `scratch-fanout-es/apply_fanout.py`; `classify.py` diffed fresh sources against the backup line by line — KEEP = core build-10 change, REVERT = edition hand fix restored, MERGE = derbi letter line (fresh sábado + backup ASCII parens), INSERT = RTVE debate-a-ocho timeline row. No commit, no push.
Common core changes kept: C1 (P1 CINCO CLAVES box 700→720), C2 (`antes del jueves`→`hasta el jueves`), es-ja D1 (consejo completed) + D4 (derbi sábado 21st), es-nl D1/D2, es-pt C2 (PCTE kept, 195 kept). C3 (P5 vocab `content56.py:79`) left as-is per adjudication.
Gates (all green unless noted): run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; render rc=0; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated — translation items keyed by target-language sentence); freeze 8/8 SVGs byte-identical; freeze-diff CJK accounting clean; canonical creambox.py full scan 0 own-ink overflow (the 6 raw negative lines per edition are the known below-box headings, identical to core); creambox_diag 0 own-ink negatives; boxtitle 0 overflow; keycheck 149/150 (only the #150 open-question `✓` exception); sweep 0 orphans / 0 box-vs-hline; pdftotext print = web bytes; P8 min effective font 10.125pt (≥ 9.75pt floor).
Classify: KEEP 23 / REVERT 23 / MERGE 1 / INSERT 1 / DELETE 0. Build: run1 rc=0, TOTAL 150, P8-keys y=2569 (no warnings — accepted state as in old build 5; last ink 39px above the footer rule). New print 3,500,924 B SHA `80b4ce0a095551599adbf0e8e0c617715513a6df3c6ad004cc1428d8bb99b602`; web 886,730 B SHA `f03047b1631fba034e3e65d2804a95c4c4ea40ba6af36a46e312921a7a70b5b0`; text.md 1,797 lines SHA `6080c94c420fd1077fedee777bba77ec789fd4c6c431ef70e7b7313923cc8906`; print/web text 107,966 bytes, identical.
Hand fixes: no task-listed hand fix for es-en; the reverted 23 lines restore the old edition's hand fixes (§6.1–§6.7). No new defects found by any gate in this rebuild.

## 10. Fix2-port rebuild (U+201C/U+201D/U+2019, 2026-11-11 — pre-insert)

Fix: ported the fix2 patch from `core-de/svglib.py` (commit 4ac7192c) into this edition's `svglib.py`, extended from U+201C-only to all three quote codepoints (`if ch in ("\u201c", "\u201d", "\u2019")`, class derived, not spelled, per fix2's freeze_direct note). `svglib.py` md5 `6a46ee51…` → `48c31801…`; py_compile passes; diff contains only the ported block; reverse-patch reproduces the pre-patch md5 exactly.
Census (before → after): **2 → 0 defective glyphs** — P1 `“Debate”: two or more people discuss in public.` (18pt “” in Noto Sans CJK SC) now Newsreader; 6 quote glyphs total in the edition, all Newsreader after the fix.
Gates (all green): two independent `tools/run_build.py` builds, A-vs-B SVG 8/8 byte-identical; run TOTAL 150, 0 OVERFLOW/TOO WIDE; webpdf rc 0; boxtitle 0 DEFECT; spill sweep 0; p8 extract 150/150, compare vs core CLEAN (keydiff [137, 138], adjudicated §6.9); occlusion 0 flags; `freeze.py diff` rc 0; frozen_check PASS 8/8; text.md byte-identical (SHA `6080c94c…`, 1,797 lines). Logs: `hidden_files/w47/scratch-gatefix-u201c-es/2026-w47-es-en/` (driver summary, census, patch log/diff).
New deliverables: print 3,500,997 B SHA `b7f7931f…`; web 886,824 B SHA `f1221df3…`; pdftotext print = web 45,946 bytes, -layout 107,980 bytes (before 107,966; +14, whitespace only — the P1 quote run-split changes pdftotext's line grouping). Cards: `p1-portada.png` re-rendered and synced (the fixed quotes are on P1); the other 7 cards byte-identical to before.

## D5 重建记录（2026-11-12，B档）
- 安装：`mechanism/apply_variant.py --svglib <本版>/svglib.py --target es --reader en`（mode latin）；`svglib.py` md5 `48c31801…` → `da6d8aa3…`（与 core-es D5 后一致）；路由断言 10/10，fix2 保留（普查弯引号在 CJK Sans 0，6 个弯引号全在 Newsreader）。
- 预修 3 项共用版式（与 core-es 相同西班牙语串、同栏宽，量值相同）：P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt、P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt、P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。
- 逐项修 2 项（D5 新缺陷，修前基线 0）：P1 框题 `LA SEMANA EN CIFRAS　Numbers` +10.5px、P5 框题 `EL PLAN DE LA SEMANA　The plan` +20.7px——两框标题字号 23→21pt（`f.box(..., tsize=21)`，文字一字未动，text.md 不受影响）。
- 门禁全绿：run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；render rc=0；D5 普查 0；occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，仅读者语译注差异：137/138 答案键同义、中文→英文，§6.9 已裁定类）；boxtitle 0 DEFECT；creambox PASS 0 defects（P8 197 行、页脚余量 39.9px 不变；P1 行数 120→122 系 D5 重排）；spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es：新增 CJK 字符 0（新增拉丁串 423 为读者语翻译，属预期）；印/网文字层 44,302 字符、8,430 词一致。
- 新 PDF：印刷版 2,915,634 B SHA `3ece3251…`；网页版 806,132 B SHA `23a06fab…`。`text.md` 字节不变（SHA `6080c94c…`）。日志：`hidden_files/w47/scratch-d5-rebuild-es/2026-w47-es-en/`。

## es 家庭修复 F2/F3/F4（2026-11-12，独立重校 PROOF-NOTE (b) 返修）

- 改动：F2（P6 时间轴措辞：`(sin el PSOE)` → `(sin el PSOE confirmado)`，与正文一致）。F1（缺首字下沉）按协调员裁定不修：全刊引擎级缺口，进模板 backlog，见 FIX-LOG。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0 → text.md 更新（core-es 为 D5 工具重导出；其余 10 版手术替换，diff 只含意改行；ru F4 另做词级手术，见 FIX-LOG 陷阱核查节）。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-en.pdf` 2,915,635 B，SHA-256 `a7d5aba8bd0ff869a4ceed41194589262c8c97d35dab201d9196ebe29be92fb4`；网页版 `La-Lucerna-VOL4-es-en-web.pdf` 806,124 B（< 7 MB），SHA-256 `bb690dd25b6c822b9dd846b02163c747a7432d28f0c57a8b07363847ba64d204`；text.md `2026-w47-es-en.text.md` 45,046 B，SHA-256 `3c2ef9876638c384cd5c5b4288b55d2917e65756d1d431daf11a2474ad2a680b`。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 26 titles, 261 body lines，0 DEFECT；spill 0 SPILL（27 盒，70 candidates）；edge 0 TOUCH / 0 NEAR；D5 census PASS（弯引号全在 Newsreader）；freeze baseline 8/8；印/网 pdftotext 45,867 字节逐字节一致。
- 日志：`hidden_files/w47/scratch-fix-es/`（FIX-LOG.md、build-all.log、build-resume.log、gates-all.log、text-pre/）。

## 第四轮独立重校修复 I1（2026-11-12，PROOF-NOTE-4 §2 返修）

- 改动：I1（text.md 专属，低）：两栏/两块拼接处丢空格致文字粘连；本版共 50 处（PROOF-NOTE-4 表列 37+7=44 处；机械穷举+印层逐一核验另得多 6 处同类粘连，见 FIX-LOG-4 §3）：分版粘连 43 处（数字粘连32 处、驼峰粘连3 处、数字→大写粘连2 处、句号→大写粘连2 处、逗号粘连1 处、中点粘连1 处、句号→小写粘连1 处、右括号粘连1 处）；目录粘连 7 处（`Pág. 2La semana` … `Pág. 8Ejercicios y respuestas` → 各补空格）。
- 重建：未重建（PDF 未动）；text.md 手术替换 50 处（逐处先断言原文存在再替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 40 行，行数不变（1798 行）。
- 文件：text.md `2026-w47-es-en.text.md` 45,044 B（I1 前 44,994 B，+50 B）、1798 行，SHA-256 `dd34d3a3cd4857ab26da2e679508b04ddb9344f6a38731d21b26ed1062937a3a`（改前 `cfdd39a9779d83ed59667049a01570d7fa719e7ac529ae4eeec4e9e54489a220`）；印/网 PDF 未动，SHA 不变（印 `a7d5aba8bd0f`、网 `bb690dd25b6c`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；D5 普查 PASS（弯引号 6/6 在 Newsreader）。
- 日志：`hidden_files/w47/scratch-fix4-w47-es/`（FIX-LOG-4.md、fix.py、fix2.py、fix-report.json、text-pre-*.md、gates4.sh、gates4.log、p8-extract/compare、census）。

## 第五轮独立重校修复 J1（2026-11-12，PROOF-NOTE-5 §3 返修）

- 改动：J1（text.md 专属，低）：小写词与小写词拼接粘连（I1 同类残留，第四轮 9 类模式与修复轮重扫均漏检）；本版共 2 处：`confinal` → `con final`（L1150，P6 Q88 C 尾 `con` + Q92 A 尾 `final`）；`unasondeo` → `una sondeo`（L1150，Q92 C 首词 `una` + D 框首词 `sondeo`）。
- 重建：未重建（PDF 未动）；text.md 手术替换 2 处（逐处先与同版印 PDF 文字层核对断句、再断言原文存在后替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 1 行，行数不变（1798 行）。
- 文件：text.md `2026-w47-es-en.text.md` 45,046 B（J1 前 45,044 B，+2 B）、1798 行，SHA-256 `3c2ef9876638c384cd5c5b4288b55d2917e65756d1d431daf11a2474ad2a680b`（改前 `dd34d3a3cd4857ab26da2e679508b04ddb9344f6a38731d21b26ed1062937a3a`）；印/网 PDF 未动，SHA 不变（印 `a7d5aba8bd0f`、网 `bb690dd25b6c`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）。
- 日志：`hidden_files/w47/scratch-fix5-w47-es/`（FIX-LOG-5.md、fix5.py、fix-report.json、text-pre-*.md、gates5.sh、gates5.log、p8-extract/compare、rescan.py、rescan.json）。
