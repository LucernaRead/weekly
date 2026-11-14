# Lucerna Weekly — Russian VOL.1 · Spanish edition (RU × ES)

The Russian core issue (VOL.1, «Первый снег») reissued for Spanish-speaking readers:
**Russian target text (frozen core) + explanations written natively in Spanish**
（目标语正文 = 俄语核心冻结；讲解 = 西语母语原生撰写）.

- Week: 19–25 October 2026 · VOL.1
- Pages: 8 (1950×2700), warm ivory — identical layout to the core
- Exercises: **150** — A2 54 · B1 72 · B2 24 (registry identical to the core)
- Print PDF: `Lucerna-VOL1-ES.pdf` (22,611,243 B, sha256 `b39cf4a64eea8f3747b3cd65eb94e599b9eebf79a78f0030278c2332a228e193`)
- Web PDF: `Lucerna-VOL1-ES-web.pdf` (3,683,458 B < 10 MB, sha256 `05f06b27e85d73064046edfda1fc3bd114f10190d217284aa1b932d2a9963b9c`)
- Build: `hidden_files/weekly-report-ru-es-build/` (seeded from the core build)
- **Independent proofread: PASS** (2026-10-21, fresh reviewer, one complete
  pass with zero problems — full record in §12 below). Not inserted into
  the repo, not posted to Discord (delivery paused).

## 1. Method

Fan-out of the frozen Russian core (`files/weekly-report-ru-vol1/`). The explanation
layer (glosses, grammar notes, instructions, all 150 answer notes) was rewritten
natively in Spanish; the Russian target text is byte-identical to the core.
The build was first proven to reproduce all 8 shipped core SVGs byte-identically
from an unmodified copy of the core build (only the output path redirected)
before any change was made — sha256 of all 8 output SVGs matched the shipped core.

## 2. Freeze verification (all against the CORE, never a sibling)

- Registry diff vs core, computed programmatically: **n / page / level identical
  for all 150**; per page 10/18/18/18/18/18/12/38; writing model 82 words — all
  identical to the core.
- Text-element multiset diff per page (ES SVGs vs core SVGs): every difference is
  explanation-layer or §4 furniture. No Russian article, stem, option or key text
  outside the §3 registry was added, removed or altered. Wrap-segmentation
  differences in the P8 keys flow are line-break artefacts of the Spanish notes'
  lengths; the registry verifies every key string verbatim.
- Image payloads: byte-identical to the core on all 8 pages (data-URI comparison).
- CJK scan: **0** CJK characters in all 8 final SVGs (Cyrillic + Latin only).
  The banned intermediary term appears nowhere in the paper, this KIT, or the
  build code (the inherited gloss method was renamed `expl()`).

## 3. Registry & key-diff vs the CORE (complete list)

**Key changes — only the documented re-aimed translation items:**

| # | Core key | ES key | Why |
|---|----------|--------|-----|
| 137 | 星期日中央陆军将对阵斯巴达克。| El domingo, el CSKA juega contra el Spartak. | RU→reader-language translation; now targets Spanish. Note: «Compáralo con la página 4» |
| 138 | 预报员预报十月末有雨夹雪。| Los meteorólogos prometen aguanieve para finales de octubre. | Same re-aim. Note: «мокрый снег = aguanieve» |
| 150 | （开放题，范文如下）| (Pregunta abierta — texto modelo a continuación) | Apparatus line. Note: «El texto modelo está en la sección H de esta página (82 palabras)» |

#139/#140: prompts re-aimed into Spanish («Las vacaciones empiezan el sábado:
doce días en total. → ___»; «¡Felicito a papá por el Día del Padre! → ___»);
their Russian keys are byte-identical to the core. Every other key is
byte-identical to the core; all remaining registry diffs are note-text only
(Chinese → Spanish). Spanish typography: space before each note parenthesis,
half-width parentheses only.

## 4. Furniture (Spanish column)

- Badge (20 pt bold, brick #a4553a, in place of the core's strap subtitle):
  «TEXTOS EN RUSO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»
- Masthead: «Lucerna» — no article (Russian takes none, as in the core)
- P1 edition line: «SEMANARIO RUSO · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ»
- Top strip centre: «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · CADA SEMANA · EL RUSO QUE LEE RUSIA»
- Footers, all 8 pages: «Lucerna · SEMANARIO RUSO VOL.1 · TEXTO EN RUSO · EXPLICACIONES EN ESPAÑOL» / «Página N de 8»
- Gloss prefix: «Nota — »; exercise types localized: Completar / Opción múltiple /
  Emparejamiento / Frases / Transformación / Cloze / Traducción / Redacción;
  instructions: Completar / Relacionar / Formar la frase / Transformar /
  Traducir al español / Traducir al ruso / Escribir
- P6 chart disclaimer appended in Spanish: «Una encuesta de práctica de la
  redacción, para entrenarse: no son estadísticas reales.»

## 5. Fit shortenings (Spanish apparatus / furniture wording only — no geometry, no Russian moved)

Found by the box-title-vs-border pass (real-font measurement), fixed by shortening
wording, then re-audited to zero crossings:

- P1 numbers-box title: «НЕДЕЛЯ В ЦИФРАХ · La semana en cifras» (ink to x=1019,
  past the box edge 961) → «НЕДЕЛЯ В ЦИФРАХ · En cifras» (ends 894).
- P1 media-box source line: «Según los medios rusos, 15–20 de octubre de 2026»
  (ink to x=1916, past the page inner frame) → «Según los medios rusos, 15–20 oct. 2026» (ends 1827).
- P1 contents-box title: «В ЭТОМ НОМЕРЕ · En este número» (ink to x=1889 vs edge 1885)
  → «В ЭТОМ НОМЕРЕ · Sumario» (ends 1806).
- P6 pro/contra title: «ЗА И ПРОТИВ · A favor y en contra» (ink to x=1887 vs edge 1885)
  → «ЗА И ПРОТИВ · Pros y contras» (ends 1835).
- **P7 column 3** initially ended at 1796.48 (core: 1682.96), crossing the phrases
  rule at y=1698. Three Spanish strings were shortened by wording only:
  error-clinic note #4 → «Genitivo tras «с»: с первого октября.» (2→1 lines);
  word-of-week gloss → «единоличный лидер = el único líder: más puntos que nadie.» (3→2 lines);
  readers'-corner note → «Ejemplo ficticio de la redacción. VOL.2: ¡cartas reales y
  los mejores textos!» (4→2 lines; both VOL.2 promises kept).
  After the fix P7 col 3 ends at exactly **1682.96** — core parity, 15 px clear of the rule.
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings. The `P6-ex ended y=2594
  (bottom 2580)` cursor reading is identical in the core build and is a
  trailing-gap cursor artefact: the geometric audit and the viewed card show the
  last P6 items (##99–100) ending well above the footer rule — not a defect.

## 6. Audits

- **Geometric occlusion audit** (`audit_ru_es.py`, paint order, production-font
  metrics, **stroke-expanded line boxes** — half stroke width each side; validated
  on a synthetic positive control in which a covering rect, a zero-height `<line>`
  crossing, and a footer-band text are all detected): **1 raw flag**, the known P2
  designed adjacency — the weather reminder line (baseline 1800) vs the twin rules
  at rows 1803–1804. **Pixel-adjudicated on the rendered ES card: text ink ends at
  row 1802 (sparse descender tips); the gold rules occupy rows 1803–1804 (full-width
  gold counts); zero contact** — identical to the core measurement. Non-defect.
  Effective flags: **0**.
- **Box-title vs border check** (dedicated pass, stroke-expanded box edges against
  every text ink band; validated on a synthetic control): found the 4 real crossings
  fixed in §5. Two residual flags, both pixel-adjudicated non-defects:
  (1) P1 КОРОТКО box, last line «странице.» — a byte-identical core element at core
  geometry (the core flags identically): pixel scan shows its descender ink ends at
  row 2300, rows 2301–2302 are clear box fill, the border sits at rows 2303–2304 —
  no contact; (2) P2 «А ВЫ?» box, last Spanish line — ink ends ≥6 rows above the
  box border at y=1497. Effective crossings: **0**.
- **Page-edge spill**: covered by the main audit — **0**.
- **All 8 cards viewed** — layout, Spanish apparatus and footers verified visually.

## 7. Content verification

- **Weekday claims re-checked against the real 2026 calendar — all correct** (no
  inherited weekday error): forecast window opens Wednesday 21 Oct; films
  Thursday 22 Oct; last school day / matchday 12 opens Friday 23 Oct; holidays
  Saturday 24 Oct – Wednesday 4 Nov = 12 days (span verified arithmetically);
  ministry window Mon 26 Oct – Tue 3 Nov = 9 days; derby Sunday 25 Oct 16:00;
  Lyceum Day Monday 19 Oct; Father's Day Sunday 18 Oct; Grandparents' Day
  Wednesday 28 Oct; Halloween Saturday 31 Oct; back to school Thursday 5 Nov;
  2026 − 1811 = 215. P6 calendar strip weekday letters (сб вс пн вт ср чт пт сб
  вс пн вт ср) all match the real calendar.
- **Answers re-checked**: chart reads 34/28/22/16 (sum 100); standings 25/24/23;
  Rodina—Orenburg 2:2; Dinamo—CSKA 3:1; UNDR ticket 900 ₽; match sets verified
  item by item (greetings b/d/c/a; films b/d/c/a; teams b/a/d/c; costumes b/d/c/a;
  P8 words c/d/b/a); dialogue cloze 145–149 = A/A/A/A/B; writing model 82 words,
  byte-identical to the core.
- **P7 phrases of the week**: all 8 quotes are the core's frozen Russian text
  (byte-identical), each present in its source article and in the phrases block,
  with the page tags (Страница 1, 2, 2, 3, 3, 4, 5, 6); only the translations are new (Spanish).
- Facts and images are the core's, unchanged: credits on P1 Yuon, P2 Bentley,
  P3 Kiprensky + Bilibin, P4 1912 team photo (public domain note), P5 USDA,
  P6 Toxer427 CC0 — each verified present beside its image.

## 8. Builder proofread record

Full pass by the builder before handoff: all 8 rendered pages read; every Spanish
gloss, instruction, grammar note, clinic rule, chart note and readers'-corner line
read against the Russian it explains; all 150 P8 notes read against their stems
and articles; Spanish checked for spelling, accents (meteorólogos, pronóstico,
página, número), inverted ¿/¡ in questions and exclamations («¿Y tú?»,
«¡Feliz Día del Padre!», «¡Felicito a papá por el Día del Padre!»), agreement and
punctuation. Dates/weekdays re-checked per §7. A scratch rebuild from the build
sources reproduces all 8 shipped SVGs byte-identically.
**Independent proofread: PASS** — completed by a fresh reviewer (see §12);
one complete pass found zero problems (SOP §8).

## 9. VOL.2 promises carried over in Spanish (must be honoured next issue)

Derby result (CSKA — Spartak) and whether the first snow fell; Grandparents' Day
(28 Oct) and Halloween (31 Oct) follow-ups; real readers' letters + the best P8
writing («Мои каникулы»), replacing the labelled editor's example in the
readers' corner (P7 note, Spanish).

## 10. Deliverables (this directory)

- `svg/` — 8 page SVGs (p1-pervaya … p8-test) · `cards/` — 8 PNGs (1950×2700)
- `Lucerna-VOL1-ES.pdf` — print PDF, 21,917,264 bytes (D5 rebuild 2026-11-14; D5 前 22,611,243 bytes) ·
  sha256 424677f81a6b02b0698a38b142a8755f6e949a9db3e04a8bfef9585cd2c27c12
- `Lucerna-VOL1-ES-web.pdf` — web PDF (JPEG pages q85 @1400px),
  **2,291,565 bytes (< 10 MB)** (D5 前 3,683,458 bytes) ·
  sha256 b94de2d0eade77a1d537070b6e44ecbd56230c71fc034ae6948639c997f8051b

## 11. Reproduction

```bash
cd hidden_files/weekly-report-ru-es-build
/tmp/wp-venv/bin/python run.py        # -> files/weekly-report-ru-es/svg/ (registry = 150)
/tmp/wp-venv/bin/python render.py     # -> cards/ + Lucerna-VOL1-ES.pdf + Lucerna-VOL1-ES-web.pdf
/tmp/wp-venv/bin/python audit_ru_es.py ../../files/weekly-report-ru-es/svg   # 1 known P2 flag, pixel-adjudicated
```
Venv `/tmp/wp-venv` (cairosvg, pillow, pypdf). Never use /opt/meta-chromium
(hangs in this VM).

## 12. Independent proofread record (2026-10-21, fresh reviewer)

**Verdict: PASS — one complete independent pass, zero problems. Nothing was
fixed or re-rendered; the shipped artifacts are unchanged.** All builder
claims in §§1–7 were verified independently, not trusted:

1. **Baseline & freeze**: both builds rebuilt in isolation — the core build
   reproduces all 8 shipped core SVGs byte-identically (8/8 sha256), and the
   ES build reproduces all 8 shipped ES SVGs byte-identically (8/8). Registry
   diff (both registries re-dumped from source): n/page/level identical for
   all 150; **key diffs exactly #137, #138, #150**, values as in §3; type
   names map 1:1 (8 localized type labels); 142 notes translated, the 8
   unchanged notes are language-neutral Russian verb-form pairs / a Russian
   holiday name, identical in the core by design. Full text-node multiset
   diff per page: every difference is explanation layer, §4 furniture, or a
   §3 registry item (bilingual heads keep their Russian half verbatim; P8
   differences are wrap segmentation of the same keys). **No Russian target
   text outside the registry was added, removed or altered.**
2. **Spanish completeness**: CJK = 0 in all 8 final SVGs (text layer and raw
   bytes); a scan of all 169 pure-Latin text nodes found no residual English,
   German or French apparatus (the only pattern hit was Spanish «que»);
   every gloss, instruction and all 150 P8 notes read in full — all Spanish,
   accents and ¿/¡ checked.
3. **Keys re-derived independently** from the printed stems and articles for
   all 150 items — all correct, including matching sets (25–28 b/d/c/a,
   39–42 b/d/c/a, 57–60 b/a/d/c, 75–78 b/d/c/a, 141–144 c/d/b/a), dialogue
   cloze 145–149 = A/A/A/A/B, chart reads (#85 B — grandparents 34 % is the
   longest bar; #86 = 22 %; #87 = 28 %; bars measured in the SVG, sum 100),
   standings 25/24/23, Rodina—Orenburg 2:2, Dinamo—CSKA 3:1, ticket 900 ₽.
   #137/#138 Spanish keys are faithful translations of the printed Russian
   stems; #139/#140 Russian keys byte-identical to the core.
4. **Totals**: 150 — A2 54 · B1 72 · B2 24; per page 10/18/18/18/18/18/12/38;
   numbering 1–150 continuous; writing model 82 words.
5. **P7 phrases**: all 8 Russian quotes verified programmatically — verbatim
   contiguous excerpts, each occurring exactly 2× in the issue (source
   article + phrases block), page tags (Страница 1, 2, 2, 3, 3, 4, 5, 6)
   all correct.
6. **Calendar**: all 13 weekday claims re-checked against the real 2026
   calendar — all correct (21 Oct Wed … 4 Nov Wed); holiday span = 12 days;
   ministry window 26 Oct–3 Nov = 9 days; 2026 − 1811 = 215; P6 strip
   letters ×12 (сб вс пн вт ср чт пт сб вс пн вт ср) and day numbers
   24–31, 1–4 all match.
7. **Furniture**: P1 badge present; pairing footer + «Página N de 8» on all
   8 pages with correct N; masthead «Lucerna» with no article (no
   Le/La/The/El Lucerna anywhere in the SVGs).
8. **Geometric occlusion audit (reviewer's own run)**: the audit script was
   first re-validated on synthetic positive controls written by the reviewer
   (COVER 100 %, zero-height-line LINEX, and FOOTER all fire; a clean page
   is silent). On the shipped SVGs: **1 raw flag** — the P2 reminder line
   (baseline 1800) vs the rules — pixel-adjudicated by the reviewer on the
   shipped card: dark text ink ends at row 1802, rows 1803–1804 are the gold
   rules across the full text width with zero dark pixels → no contact,
   non-defect, identical to the core. Box-title pass re-verified with
   production font metrics: the 4 fixed titles end at 893.6 / 1827.0 /
   1806.4 / 1834.9 px, matching §5 and inside their box edges (961 / frame /
   1885 / 1885). The 2 residuals pixel-verified: P1 «странице.» region is
   **pixel-identical to the shipped core card** (frozen core geometry; text
   body ends row 2299, no visible contact with the pale border at 2304);
   P2 «А ВЫ?» last Spanish line's ink ends at row 1490, ≥6 clear rows above
   the y=1497 border. Page-edge spill 0; footer-band intrusions 0.
9. **Images & PDFs**: image payloads byte-identical to the core on all 8
   pages (1/1/2/1/1/1/0/0); credits verified beside their images on the
   rendered cards (P1 Yuon, P2 Bentley, P3 Kiprensky + Bilibin, P4 1912
   team photo, P5 USDA, P6 Toxer427 CC0). Web PDF independently measured:
   **3,683,458 B (< 10 MB), sha256
   `05f06b27e85d73064046edfda1fc3bd114f10190d217284aa1b932d2a9963b9c`** —
   matches the §10 pin (print PDF 22,611,243 B, sha `b39cf4a6…` also matches).
10. **Banned-term scan**: the intermediary-layer term (Chinese and English
    forms) = 0 hits in the paper SVGs, this KIT, and the build code.
11. **All 8 cards viewed** by the reviewer: no covered, clipped or
    struck-through text; Spanish apparatus, boxes and footers as designed.

This edition is clear for repo insert by the main line.

## 13. D5 rebuild (2026-11-14)

D5 + §1.1 合并重建（2026-11-14；builder v3 接替 v2，v2 死于 2026-11-14 ~02:55 UTC 第 5 波 restart drain）。本节 supersedes 上述旧印/网 pin 行（以实测发运值为准；KIT 旧 SHA 不可作基线）。

- 装机：`apply_variant.py --patch-core ru --week 2026-w43`（core-ru `_D5_READER = "latin"`，+263/−28）+ 本版 `apply_variant.py --svglib patched/2026-w43-ru-es/svglib.py --target ru --reader es --week 2026-w43`（`_D5_READER = "latin"`，diff +63/−2）；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2 保留。
- 基线：run TOTAL 150，0 警告；印 PDF 22,259,857 B（MANIFEST +0.001%），网 PDF 2,335,763 B，`pdf_text_diff_ru.py` + TRIM_ARGS → IDENTICAL；修前普查 D5 拉丁 458、西里尔 0。
- 缺陷与修法（只动字号/断行与规则线位置，不动文字）：
- D2 (occlusion TEXTX, P1): `'A2' overlaps 'кино' 7.4×11.2px` — `content12.py:103` 目录标题 20→19pt。
- D3 (occlusion LINEX P2 ×6, 基线同款): `content12.py:232` 规则线 `ey−12`→`ey−8`。
- 门禁（run2）：全套 17 门 ALL-GREEN。run TOTAL 150；head_check 0；d5 census 拉丁/西里尔/弯引号在 CJK 均 0（弯引号总数 0；`noto_sans_elements=411`）；freeze baseline 8/8；freeze diff 新增 CJK 0、新增拉丁 strings 154（run 拆分）；spill 0（173 OBSERVE）；boxtitle 0 DEFECT（58 titles, 717 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（n=409, median 1.012；P8 208→208 行，slack 44.5→44.5px）；文字层 print=web 差 0（40,866 字）；text.md BYTE-IDENTICAL；census_quotes 0 defective；p8 compare CLEAN，keydiff=[137, 138]；刊头标语→日期间距 392.0px PASS。日志：`hidden_files/d5-redo/scratch-2026-w43-ru/logs/2026-w43-ru-es/GATES-SUMMARY-run2.txt`。
- 新交付物（实测）：印 PDF `Lucerna-VOL1-ru-es.pdf` **21,917,264 B**，sha256 `424677f81a6b02b0698a38b142a8755f6e949a9db3e04a8bfef9585cd2c27c12`；网 PDF `2026-w43-ru-es.web.pdf` **2,291,565 B**，sha256 `b94de2d0eade77a1d537070b6e44ecbd56230c71fc034ae6948639c997f8051b`；text.md **61,537 B**，sha256 `df78b3753f770b47ea2f2b649de5ff4bbe2363d57194ea675ca43be0aae5521c`，与 fanout `.text.md.new` BYTE-IDENTICAL。D5 报告：`production/notes/2026-w43/g-ru/scratch-d5-rebuild-ru/D5-REPORT-2026-w43-ru-es.md`。KIT 内独立校对记录（§12）引用的旧 pin（印 22,611,243 B / 网 3,683,458 B）为 D5 前实测值，系历史记录，不改。
