# INDEPENDENT PROOFREADER VERDICT — ROUND 1
## Lucerna Weekly W46 · Russian target · VOL.3 · Issue Mon 9 – Sun 15 Nov 2026

Proofreader: independent Round 1 (did not build these editions). Date of round: 2026-11-02 (America/Toronto).
Scope: all 11 RU-target editions — 2026-w46-ru-de, -en, -es, -fr, -it, -ja, -ko, -nl, -pt, -zh-cn, -zh-tw.
Canonical dirs: `files/weekly-report-w46-ru-*/`; ru-zh-cn lives in `files/weekly-report-w46-ru-core/`
(there is no `weekly-report-w46-ru-zh-cn/` dir). Frozen core build sources: `hidden_files/w46/`
(`ru-transform.py`, `ru_maps.py`, `weekly-report-w46-ru-build/`). Gate outputs from this round are saved
in this directory (`hidden_files/w46/ru-proofread-gates/`): `freeze-ru-*.json/.log`,
`p8-ru-*.json/.log`, `occlusion-ru-*.json/.log`, `freeze-word-analysis.txt`, `crops/`.
No edition files were edited, re-rendered, pushed, inserted, or posted by the proofreader. No
`~/workspace/weekly-git`, no `index.json` touched.

## FINAL VERDICT

**ROUND 1 FAIL — 0 of 11 editions shippable as built.** Blocking defects D1 (all 11 editions) and
D2 (7 editions) below must be fixed in the build sources, the affected editions re-rendered, and a
full Round 2 proofread run from scratch (proofread-until-zero: any fix restarts the whole round).
Defect D3 (ja only) is minor typographic but real; fix it in the same pass.

## PER-EDITION VERDICT

| Edition | Verdict | Blocking defects |
|---|---|---|
| 2026-w46-ru-zh-cn (core dir) | FAIL | D1 |
| 2026-w46-ru-de | FAIL | D1, D2 (P3 + P4) |
| 2026-w46-ru-en | FAIL | D1, D2 (P3 + P4) |
| 2026-w46-ru-es | FAIL | D1, D2 (P3 + P4) |
| 2026-w46-ru-fr | FAIL | D1, D2 (P3 + P4) |
| 2026-w46-ru-it | FAIL | D1, D2 (P3 + P4) |
| 2026-w46-ru-ja | FAIL | D1, D3 |
| 2026-w46-ru-ko | FAIL | D1 |
| 2026-w46-ru-nl | FAIL | D1, D2 (P3 only) |
| 2026-w46-ru-pt | FAIL | D1, D2 (P3 + P4) |
| 2026-w46-ru-zh-tw | FAIL | D1 |

## DEFECT LIST

### A. Frozen-core defects (in the RU core; present identically in all 11 editions)

**D1 — BLOCKING. P5 matching exercise C (items 76–77): printed P8 answer-key letters are transposed.**
The exercise itself (P5, block C · ПОКУПКИ) is correct; the answer key is wrong, so a reader who
checks their work is taught the wrong meaning.

Evidence (core SVG `p5-molodezh.svg`, block C, nodes in document order):
- `75. посылка`, `76. возврат`, `77. промокод`, `78. пик`
- options: `a. код со скидкой` (= discount code = промокод), `b. товар возвращают в магазин`
  (= goods are returned to the shop = возврат), `c. самое большое число заказов` (= пик),
  `d. товар, который прислали по почте` (= посылка).
Correct matches: 75→d, **76→b, 77→a**, 78→c.

Printed P8 key (core `p8-test.svg`, and identically lettered in every fan-out):
- `76. a — 退货 a` (de: `76. a — Rücksendung a`; en: `76. a — return a`; es: `76. a — devolución a`;
  fr: `76. a — retour a`; it: `76. a — reso a`; ja: `76. a — 返品 a`; ko: `76. a — 반품 a`;
  nl: `76. a — retour a`; pt: `76. a — devolução a`; zh-tw: `76. a — 退貨 a`)
- `77. b — 促销码 b` (de: `77. b — Rabattcode b`; en: `77. b — promo code b`; etc.)
Correct text: 76 must be **b**, 77 must be **a**. The manuscript registry
(`2026-w46-ru-core.text.md`, §C: "76. возврат — код со скидкой (key a)", "77. промокод — товар
возвращают в магазин (key b)") encodes the same transposition, so the fix belongs in the core
registry/build source, then re-render all 11 editions.

Cross-checks performed (all correct, no further transpositions): matching blocks 25–28 (P2),
39–42 (P3), 57–60 (P4), 141–144 (P8) were each verified option-by-option against the printed
options and the P8 keys — all match. Only 76/77 are transposed. `tools/p8.py` cannot catch this:
it compares note SETS (CLEAN 150/150), not key correctness; the proofreader verified keys
against stems/options/article text directly.

### B. Edition-specific defects

**D2 — BLOCKING. Wrapped exercise-block instruction lines are displaced: the second line renders
as a stray fragment floating in mid-page (column 2, above the exercise block), while the
instruction at its home position (bottom-left block header) is left incomplete.**
Root pattern (identical in every affected case): a two-line instruction whose line 1 sits at
(x=65, y≈2564) under its block header and whose line 2 was placed at (x=527, y≈1656/1696) —
the top of column 2's exercise area, detached from line 1 by ~900 px. Visually confirmed on
rendered cards (crops saved in `crops/de-p4-fragment.png`, `crops/de-p3-fragment.png`,
`crops/it-p4-fragment.png`). The canonical occlusion audit does not flag these (no overlap),
which is why the builder's "0 flags" gate passed despite the visible defect.

- **D2a — P3 (`p3-kultura.svg`), block C instruction**, in 7 editions: de, en, es, fr, it, nl, pt.
  Line 1 at (65, 2564.45); orphan line 2 at (527, 1696.5):
  - de: `Füllen Sie die Lücken mit der richtigen` / orphan `Verbform oder dem richtigen Kasus aus.`
  - en: `Fill in the gaps with the right verb form or the` (home line, wording per SVG) / orphan `right case.`
  - es: orphan `caso correcto.`
  - fr: orphan `le bon cas.`
  - it: orphan `caso giusto.`
  - nl: `Vul in met de juiste werkwoordsvorm of de` / orphan `juiste naamval.`
  - pt: orphan `caso correto.`
  Clean (single-line instruction, no orphan): core/zh-cn, ja, ko, zh-tw.
- **D2b — P4 (`p4-sport.svg`), block B instruction**, in 6 editions: de, en, es, fr, it, pt.
  Line 1 at (65, 2553.45) under header `B · КАЛЕНДАРЬ И ДАТЫ`; orphan line 2 at (527, 1656.5):
  - de: orphan `von Seite 4 aus.` (home line ends `…mit Zahlen und Wörtern`)
  - en: orphan `page 4.`
  - es: orphan `página 4.`
  - fr: orphan `page 4.`
  - it: home line `Completa con i numeri e le parole di pagina` / orphan `4.`
  - pt: orphan `4.`
  Clean: core/zh-cn, ja, ko, nl (nl instruction fits one line), zh-tw.
  Fix: shorten/re-word the instruction to fit one line at its home position, or fix the wrap-slot
  geometry, in the affected fan-out builds; re-render; re-run occlusion + visual check.
  The proofreader scanned every page of every edition for the same class (grey 20.5 pt instruction
  text at column starts, all pages): no further displaced fragments exist. P2/P5/P6 two-line
  instructions elsewhere are correctly placed as adjacent line pairs and are NOT defects.

**D3 — MINOR (fix in the same pass). ja P8 H-note kinsoku violation: a line ends with an opening
bracket.** `ru-ja` `p8-test.svg`, H · НАПИШИТЕ САМИ note, two text nodes:
line 1 `作文（決まった答えはありません）；模範文（` — ends with `（`; line 2 `87 語）は下にあります。`.
Visually confirmed on the rendered card (`crops/ja-p8-hnote.png`): the `（` dangles at the end of
line 1. Correct text: re-wrap so the opening bracket does not end a line (e.g. move `模範文（87 語）`
whole to line 2, or break before `模範文`). No other kinsoku violations found in the ja edition
(full scan of ja text nodes for prohibited line-start/end characters: this was the only hit).

## GATE OUTPUTS SUMMARY (proofreader's own re-runs; builder outputs NOT trusted)

- **Occlusion audit** (`tools/occlusion_audit.py`, selftest OK first on every run: planted classes
  fired 1 each, clean controls silent): **0 flags in all 11 editions** (88 pages), including the
  core/zh-cn edition. Builder's `ru-*-occlusion.json` (0 flags) CONFIRMED as far as the tool
  reaches — but the tool is blind to D2 (displaced, non-overlapping text) and to D3. JSONs/logs:
  `occlusion-ru-*.json/.log`.
- **P8 compare** (`tools/p8.py compare`, core vs each fan-out, total 150): **CLEAN 150/150 in all
  10 fan-outs**; missing=[] extra=0 uncertain=[]; keydiff=[137,138,139,140] in every edition —
  the E-section translations into the reader language, by design (adjudicated legitimate).
  Core extract: 150/150 noted. Builder's `ru-*-p8.json` (CLEAN) CONFIRMED. JSONs/logs: `p8-ru-*.json/.log`.
  Limitation: p8.py checks note sets, not key correctness — D1 was found by direct key verification.
- **Freeze diff** (`tools/freeze.py diff`, core SVG vs each edition SVG; `--strict-cjk` for
  ja/ko/zh-tw): Latin editions exit 0, added CJK = 0. ja/ko/zh-tw exit 1 under `--strict-cjk`
  exactly as adjudicated in the KITs (added chars are the native script only). Word-level
  re-analysis (`freeze-word-analysis.txt`): **zero added Cyrillic words in every edition** —
  the frozen Russian body is intact. Removed Cyrillic words are only furniture/explanation
  replacements (P1 subtitle line, P6 practice-data label + disclaimer sentence, P7 heading,
  P8 heading, P8 separators in ja/ko/nl/zh-tw), each with a native-language replacement
  present and verified. Char totals: Latin editions Han=0, Kana=0, Hangul=0; ja Hangul=0;
  ko Han=0/Kana=0; zh-tw zero Simplified-only characters; zh-cn zero Traditional-only
  characters (character-level Simplified/Traditional independence CONFIRMED). Core Han nodes
  surviving verbatim: 0 in Latin/ko editions; 2 in ja (shared kanji `生活`, `文化` in section
  titles — legitimate); 51 in zh-tw (shared-form strings + native Traditional glosses — no
  Simplified-only character among them). JSONs/logs: `freeze-ru-*.json/.log` (zh-cn = self-diff
  control, all zeros).
- **Counts re-measured (not trusted from KITs):** total **150 exercises**, continuously numbered
  1–150 (96 numbered stems on P1–P7 + 16 matching sub-items in 4 groups of 4 + 34 numbered P8
  stems + 4 matching sub-items in the F group = 150; P8 key set 150/150). Per page: P1 10,
  P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38. Level split re-derived by pairing each
  printed level badge with its exercise (group badges applied to their 4 matching items):
  **A2 51, B1 75, B2 24** — exactly the KIT claim. Model writing text: 87 whitespace tokens
  (85 excluding two standalone dashes; 81 excluding dashes and numerals) — inside the 80–100
  brief under any counting; the printed "(87 words)" claim follows the token count.
- **P6 chart measured:** bars (x=685) widths 600 / 343 / 286 / 200 px for 42% / 24% / 20% / 14%
  — proportional (14.29 px per point; 24%→342.9≈343, 20%→285.7≈286, 14%→200.0); values sum to
  100%; native practice-data label + native disclaimer present in all 11 editions.
- **P7 golden sentences:** all 8 occur exactly twice in every edition (article page + P7),
  verbatim contiguous, on the pages the KIT claims (P1×2, P2, P3, P4, P5, P6×2); P7 page
  references (`Страница N`) correct in all editions.
- **Native-language correctness:** every explanation/gloss/note/abstract/footer in the reader's
  language; no untranslated Russian strings outside adjudicated design (P7 `Страница N`
  references kept in Russian per KIT §1 in every edition; P8 separators kept Russian in
  de/en/es/fr/it/pt per build spec `p8_separator: None` — see adjudications; quoted Russian
  headwords in glosses are target-language citations, not residue). Cross-language stopword
  scan of Latin editions: 0 real residue hits (fr/nl hits were own-language words). Quotes:
  `«`/`»` balanced 127/127 in every edition; no ASCII straight quotes in SVG text; no U+FFFD
  anywhere. Russian manuscript read in full (682-line `.text.md` + SVG spot-verification):
  no spelling/grammar defects found in the frozen Russian beyond D1; all other answer keys
  verified against stems, articles, chart, and fixtures.
- **Badge / masthead / footers:** pairing badged in the P1 masthead area in every edition
  (top strip + badge line; ko/zh-tw badge inserted below the kept Russian subtitle at y=574,
  others in the subtitle slot at y=372) and footer labels on all 8 pages of all 11 editions
  (footer string + page line verified per page; VOL.3 everywhere). Rendered badge text fill
  measured from SVG + confirmed by rendered-pixel counts: **#a4553a (brick/rust)** in
  de/es/fr/it/ja/ko/nl/pt/zh-tw; **#3e4c2a (olive)** in en — both exactly per build spec
  (`badge_color: BRICK` / en `OLIVE`), i.e. by design, NOT defects. Masthead `Lucerna`
  (UnifrakturMaguntia 168 px, centre-anchored x=975, fill #28251d) geometrically identical in
  all 11 editions; rendered-pixel ink identical (1988 dark-ink px in the masthead band);
  0 EDGE flags; frame clearance held (rules at 26 px margins; glyphs well inside).
- **PDFs:** every web PDF 8 pages, 2,310,354–2,760,273 bytes (≤ 7 MB), `pdftotext` 53,507–55,864
  bytes (> 0, real text layer). Print-vs-web text identical after whitespace normalisation
  (char counts equal; spot-checked core/en/ja). Every `ABSTRACT.txt`: single line, no ASCII
  double quotes, reader-native, practice framing (never "learn Russian from the news" or
  equivalents), naming the real topics + masthead VOL.3 + A2–B2 + 150 exercises.
- **Reader-facing sweep:** no week/language codes, structure labels, repo links, or
  SOP/proofread/audit wording on any rendered page (searched: W46, 2026-w46, weekly-report,
  SOP, proofread, occlusion, github, discord, insert.py, edition codes, "cover" — 0 hits).
- **Dates/weekdays independently verified** (`date -d`, Europe/Moscow): 9 Mon, 10 Tue, 11 Wed,
  12 Thu, 13 Fri, 14 Sat, 15 Sun Nov 2026; fixtures Fri 6 / Sat 7 / Sun 8 Nov; round 15 on
  Fri 20 Nov. All date/weekday claims in the issue are consistent with the calendar
  (day strip пн–вс in order; "пятницу, 6 ноября", "воскресенье, 8 ноября" correct).
- **W45 promises honoured in all 11 editions** (text-verified): 11.11 sale as P1/P5 lead;
  round-14 results honestly unknown at press time with full results carried to VOL.4
  (on-page disclosure present); reader letters not fabricated — editor's example + bilingual
  on-page disclosure present on P7 in every edition, promise carried to VOL.4 in the teaser;
  no non-Russian handover items imported.
- **Images/credits:** 4 photos (P1/P2/P4/P5), identical counts in all editions; credits present
  in Russian captions (Toxer427 CC0; Wilson Bentley public domain; 1912 squad, author unknown,
  public domain; Preston Keres/USDA public domain; all via Wikimedia Commons).
- **`.text.md` exports:** ru-zh-cn file byte-identical to the core file (52,661 bytes, `cmp`
  clean) as tasked; every edition's `.text.md` carries its own native explanations + the
  Russian content and the 6 sampled headline strings. Observation (non-blocking, not
  reader-facing): the manuscript answer section in `.text.md` prints a placeholder
  `— СТРАНИЦА ? —` where the rendered P8 has numbered separators — an export quirk only.
- **Visual checks:** P1 + P8 full-frame cards viewed for all 11 editions (contact sheets in
  `crops/`), plus full-frame pt P7 and crops of the D2/D3 sites. No overflow, overlap,
  missing glyphs/tofu, or missing credits beyond D2/D3. P2–P7 covered by the geometric gates
  plus the SVG-level scans above and the full manuscript read.

## KIT CLAIM ADJUDICATIONS

- CONFIRMED: exercise total/level split/per-page counts; occlusion 0 flags; P8 CLEAN 150/150
  with keydiff 137–140 by design; freeze exit 0 / strict-CJK adjudications; W45 promises;
  E3 stray-arrow fix (no `→ ___` in any printed key); golden sentences 8×2; chart sums/bars;
  PDF text layer + sizes; abstracts; model-text word count (as token count); badge/footer
  strings; disclosure inside the letters box; image credits; "no Cyrillic gained".
- REFUTED: the KITs' visual-check claims as a complete pass — the shipped SVGs/cards contain
  the D2 fragments (7 + 6 editions) and the D3 kinsoku line, which the builder's visual
  checks and the occlusion gate both missed. The pt KIT's note that "P1 not card-read" is
  moot: the proofreader card-read pt P1 (clean) and pt P7 (clean apart from the family-wide D1).
- ACCEPTED BY DESIGN (not defects): en olive badge (`badge_color: OLIVE` in `ru_maps.py`,
  all others BRICK); Russian P8 separators in de/en/es/fr/it/pt (`p8_separator: None` in
  `ru_maps.py` — keep-core behaviour; native separators in nl/ja/ko/zh-tw per their specs);
  "Russia play" in the en P8 key (grammatical British collective usage); P7 `Страница N`
  references kept in Russian in every edition (KIT §1 policy).
- UNVERIFIABLE in this round (scope boundary, stated honestly): source-level re-verification
  of the KIT §3 trend/fact sources (Ozon figures, film dates, poll-adjacent claims) against
  live external sources was not performed; the issue is internally consistent and all
  date/weekday arithmetic was independently verified. The builder's trend-research citations
  in KIT §3 were read but not re-fetched.

## SEED RECORD (for the coordinator's insert step)

- Target VOL number: **VOL.3**
- Exercise total (re-measured): **150** — level split **A2 51 / B1 75 / B2 24**; per page:
  P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38.
- Core P1 article opening, verbatim (target language, Russian), first 3 sentences:
  > Эта неделя в России — обычная. В понедельник, 9 ноября, люди идут на работу и в школу.
  > Никаких праздников посреди недели: пять рабочих дней подряд, а потом выходные.
  (Lead headline: `ОБЫЧНАЯ НЕДЕЛЯ — И ЭТО ХОРОШО!`; deck: `Ни одного выходного посреди недели:
  как Россия живёт первую полную неделю ноября`.)

## REQUIRED FIXES BEFORE ROUND 2

1. Core registry/build source: swap P8 key letters for exercises 76 (→ b) and 77 (→ a); fix the
   manuscript registry entry the same way; re-render all 11 editions.
2. Fan-out builds de/en/es/fr/it/nl/pt: fix the P3 block-C instruction wrap (shorten to one line
   or repair the wrap slot); builds de/en/es/fr/it/pt: same for the P4 block-B instruction.
   Re-render the affected editions.
3. ja build: re-wrap the P8 H-note so no line ends with `（`.
4. Re-run all three canonical gates per edition, then a full independent Round 2 proofread
   (fresh full read + gates + visuals). Do not ship on a partial re-check: proofread-until-zero
   restarts the whole round after any fix.

ROUND 1 FAIL (blocking defects D1 in all 11 editions; D2 in de/en/es/fr/it/nl/pt; D3 in ja).
