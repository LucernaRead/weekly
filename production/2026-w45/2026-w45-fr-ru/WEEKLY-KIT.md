# WEEKLY-KIT — W45 FR×RU (target French, readers Russian)

Builder-complete report. NOT a finalization: the independent proofread gate
is the coordinator's call. Built 2026-10-28 by the FR×RU builder (depth 2).

## 1. Spec

- Edition: W45, week 2–8 November 2026. Core: W45 FR core VOL.3 (finalized).
- Pairing: French target text frozen byte-for-byte; explanation layer fully
  Russian. Masthead article `Le` (French-only). No other edition touched;
  no Discord, no main-chat cards/PDFs, no repo insertion by this builder.
- Exercises: 150 total; per page 10 / 15 / 18 / 18 / 17 / 18 / 12 / 42.
  Levels: A2 53 / B1 75 / B2 22 (registry dump from an isolated scratch
  copy; operative build dir never imported for counting).
- Gloss: 38 items = 7 / 6 / 6 / 7 / 6 / 6 (P1–P6), counted by splitting the
  render strings on `·` itself (tools/README #21).
- Model essay: 86 words (core, unchanged). P8 design: 97 noted / 53 bare.
- Delivery dir contains exactly: `svg/`×8, `cards/`×8 (1950×2700 PNG),
  `Le-Lucerna-VOL3-RU.pdf` (print), `Le-Lucerna-VOL3-RU-web.pdf` (web),
  `WEEKLY-KIT.md` (this file), `ABSTRACT.txt`.

## 2. Furniture — three-way comparison (W43 FR×RU measured | W45 core | W45 FR×RU)

| Item | W43 FR×RU (VOL.2, proofread PASS) | W45 FR core (VOL.3) | W45 FR×RU (this edition) |
|---|---|---|---|
| P1 badge (y=574, 22pt BRICK, centred) | ТЕКСТЫ НА ФРАНЦУЗСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ | 法语正文 · 简体中文讲解 — 给简体中文读者的版本 | Same string as W43 (VOL.3 issue; badge string itself has no volume number) |
| Footer (all 8 pp.) | Le Lucerna · ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ФРАНЦУЗСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ | Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文 | Le Lucerna · ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА ФРАНЦУЗСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ |
| Page line | Страница N из 8 | 第 N 版 / 共 8 版 | Страница N из 8 |
| Gloss prefix | Пояснение — | 译注｜ | Пояснение — |
| P8 separator | — СТРАНИЦА N — | （page separators in core form） | — СТРАНИЦА N — |
| P8 note brackets | half-width ` (note)` | full-width `（note）` | half-width ` (note)` (per shipped W43 FR×RU code) |
| P1 top-left | VOL. 2 · № 2 | VOL. 3 · 总第 3 期 | VOL. 3 · № 3 |
| P1 strapline (middle) | HEBDOMADAIRE EN FRANÇAIS · ФРАНЦУЗСКИЙ, КОТОРЫЙ ЧИТАЮТ ФРАНЦУЗЫ (shortened per W43 §8 defect 3) | HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语 | Same shortened string as W43 |
| P1 subtitle | ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · ОСЕНЬ И ПРАЗДНИКИ | 法 语 周 报 · VOL.3 · 决 赛 周 末 | ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · ФИНАЛЬНЫЙ УИК-ЭНД |
| P1 dark-band right | (W43 week-specific lines) | 周一开学 · 全法同步复课 | ПОНЕДЕЛЬНИК · ВСЯ ФРАНЦИЯ ВОЗВРАЩАЕТСЯ В ШКОЛУ / Старт «Мастерса» · открытие фестиваля · см. стр. 2 |
| Section heads (FR · RU short form) | W43 pattern (bilingual heads) | Chinese bilingual heads | VIE QUOTIDIENNE · ПОВСЕДНЕВНАЯ ЖИЗНЬ; CULTURE · КУЛЬТУРА; SPORT · СПОРТ; JEUNESSE & MUSIQUE · МОЛОДЁЖЬ; POLITIQUE & CHIFFRES · ПОЛИТИКА И ЦИФРЫ; LANGUE EN MAIN · ЯЗЫК В РУКАХ; NIVEAU A2 · БАЗОВЫЙ; NIVEAU B1 · СРЕДНИЙ; NIVEAU B2 · УРОВЕНЬ-ВЫЗОВ; BOÎTE À OUTILS · В КАРМАНЕ; CLINIQUE DES ERREURS · СТОП!; LE COURRIER DES LECTEURS · ПОЧТА ЧИТАТЕЛЕЙ; EXERCICES & RÉPONSES · УПРАЖНЕНИЯ И ОТВЕТЫ; P8 top-right ТЕСТ · ОТВЕТЫ ВНИЗУ ЭТОЙ СТРАНИЦЫ; P8 title RÉPONSES · ВСЕ ОТВЕТЫ С ПРИМЕЧАНИЯМИ (СТРАНИЦЫ 1–8); H · ÉCRITURE · ПИСЬМО; MODÈLE · ОБРАЗЕЦ |
| `instr` labels | Вставьте / Перепишите / Соедините / Исправьте | Chinese labels | Вставьте (fill in) / Перепишите (rewrite) / Соедините (match) / Исправьте (correct it) |
| Registry `typ` values | Chinese (internal only) | Chinese | Chinese (internal only, never printed; FR×EN precedent) |

## 3. Frozen French target text (all verified by grep on joined SVG text)

- P4 edition claim: `41e édition en 2026 (40e anniversaire)` exactly 1×;
  old form `40e édition en 2026` 0×. (41e = edition count, 40e = anniversary.)
- Q120: stem `Si j'étais libre dimanche, j'___ à Nanterre.` 1×; options
  A. irai / B. irais / C. vais present; key B; P8 note
  `si + imparfait → conditionnel; j' = je` (elision of `je`) synced.
  Neighbours Q119/Q121 present and unchanged.
- P7 quote #4: `plus excitante ou plus frustrante ?` (French space before
  `?`) 4×, same as core (quote + grammar lines); P4 debate box verbatim.
- P7 quote #8: `Les jeunes créateurs y rencontrent leur public, en vrai.`
  1× on P7 and 1× on P5 (verbatim); Q106 rewrite: error `rencontre`,
  key `rencontrent`; P8 note `créateurs (мн. число) → rencontrent, не rencontre`.
- P6 sync: `Ce calendrier peut encore bouger.` 1× on P6 (deep-read
  lowercase form) and 2× on P7 (sentence + grammar quote), same as core.
  P6 micro-drill key `peut` untouched.
- P7 word-list French definition sentences: unchanged. Freeze diff
  (`tools/freeze.py diff` core vs edition): added CJK characters 0 on all
  8 pages; edition CJK total 0. Removed non-CJK strings classified:
  P3/P7 `）。` punctuation fragments from replaced explanation paras;
  P8 answer-line rewrap fragments (same French word groups reappear on
  the added side); P3–P6 bridge rewrap fragments (same French tokens,
  re-split by the Russian bridge wrap). Zero French body text removed.
  P7 removed non-CJK = only `）。`; P7 added non-Cyrillic = 0, so no P7
  French string was even rewrapped.

## 4. P8 dual gate

- Plain `tools/p8.py compare --core-p8 <core> --edition-p8 <edition>
  --total 150` (explicit dual paths; `--target` form and default total
  both banned): **CLEAN**, core 97 noted = edition 97 noted,
  missing=[], extra_count=0, keydiff=[135, 150].
- `hidden_files/w45/p8-fr-gap-fix/keycompare.py` full-150 comparison:
  mismatches exactly **[135, 150]**, both noted re-aims; **bare-key
  mismatches 0** (53 bare keys all identical).
- Keycompare's truncated display for 135/150 (`Читать программу` /
  `Открытый вопрос`) is an extractor artifact (it splits keys on ` — `);
  the printed lines are complete (verified in SVG text nodes):
  - 135: `135. Читать программу — уже значит понимать Францию.
    (lire un programme = читать программу)`; stem re-aimed to
    `На русский: « Lire un programme, c'est déjà comprendre la France. »`.
  - 150: `150. Открытый вопрос — баллы в рамке для письма, а образец —
    в рамке MODÈLE на этой странице (оценка по баллам)`.
- P8 notes: purely Russian. Checks: CJK in notes 0; Dutch function-word
  residue 0; English residue words 0; P8 SVG character inventory = Latin
  (French keys/terms) + Cyrillic + digits + punctuation only. French
  grammar citations (`si + imparfait`, `passé composé`, `s'intéresser
  aux`) are legitimate French terms, not residue.
- E-section stems #136–#139 are Russian source sentences with French keys
  byte-identical: #136 `Перевод: Он бежит быстрее своего брата.`;
  #137 `Перевод: Ученики на каникулах с 17 окт.`; #138 bare
  `Этим вечером будем собирать портфели.`; #139
  `Перевод: Финалисты пока неизвестны.` (see §8 for the #138 nuance).

## 5. Geometry gates (all measured, untruncated outputs kept in build dir)

- Canonical `tools/occlusion_audit.py` (selftest OK, all 6 classes fire
  on synthetics, clean controls silent): edition **0 flags**, core
  **0 flags**, NEW vs core **0**.
- Same-baseline collision scan (W43 `scratch/rowcheck.py` method, true
  PIL ink boxes, same-y grouping, gap < 6 flagged): **0 collisions**
  (covers the P1 top-band left/centre/right trio at y=92 and footers).
- Full-page right-edge scan (anchored element regex; ink right >
  1885.5): only 3 hits, all P8 F-group match lines, **inherited from
  core byte-for-byte** (same French strings, same slots, same ink
  rights): `b. une soirée qui dure jusqu'à la nuit` 1891.2,
  `d. le coquillage fêté à Port-en-Bessin` 1891.2,
  `e. plusieurs concerts en une semaine` 1899.5. They exceed the
  column edge (1885) by 6–14px but stay inside the page (1950) and the
  frame; FR×EN accepted the same inherited values.
- P6 chart-label coverage, baseline-anchored method (later filled rects
  vs text baselines): **0/178 texts = 0.00%** (gate <30%). P6 has no
  bars; its chart is text rows.
- Orphan scan, window 10–45 (lines grouped by same x/size with dy in
  [10,45]; last line inspected): edition 57 hits vs core 55. NEW hits
  (17) are all ordinary paragraph-final words in the Russian layer
  (обзор., Хэллоуин., Матчбол!, знакомый., значениями., трибуны.,
  вживую., французский?, connus., измениться., различать.,
  запомнится., баллам), билеты), неизвестны)) — not the defect classes.
  Defect-class adjudication: **0 parenthesised-fragment orphans,
  0 mid-word splits** (wrap() splits on spaces only, by construction),
  2 punctuation-start lines: P5 `: clôture du festival.` **inherited
  from core** (same hit in core scan), and P4 `» — Вот это игра!`
  (closing guillemet of `« Quelle action ! »` travelling with its
  Russian translation on a bilingual chant-gloss wrap — reads
  naturally on the card, not a defect).
- Flow ends (final build log, build4.log): P1-headline 1588 (= core),
  P1-hiver 2298 (core inherited, 8px over its 2290 flow bottom),
  P1-quiz 2521, P2-feature 671, P2 col3 ends 1567.6 (date gold rule at
  1598 → 30.4px clear), P2-ex 2456 (≤2562), P3-main 813, P4-main 1375,
  P4-micro 2154, P5-main 2532 (8px margin — do not lengthen P5),
  P6-deep 1049, P6-ex 2557 (core inherited, 23px above the 2580 footer
  line), P6-opinion 1286 (14px margin — do not lengthen), P6-micro
  2020, P7-A2 954, P7-B1 1053, P7-B2 988, P7-outils 1008, P7-phrases
  1574, P7-clinic 2140 (= core, ≤2268), P8-battery 1410 (= core),
  P8-keys 2449 (≤2545, 96px margin). Zero FLOW OVERFLOW / HEAD TOO
  WIDE warnings in the final build.
- All 8 cards visually inspected (furniture, boxes, flows, answer
  block). Crops checked: P1 top band + badge, P2 ET VOUS/date
  boundary, P6 chart, P7 readers' corner, P8 battery/writing/keys end.
  No defects found.

## 6. Images (only the core's 3 verified public-domain images)

Payload dual measurement (base64-text sha256 + decoded-JPEG sha256),
core vs edition — byte-identical on all 3:

| Page | base64-text sha256 | decoded-JPEG sha256 | bytes |
|---|---|---|---|
| P1 Atget | ff20bc2bd2654cdc075f7e09bcb5a96622650c7cb5921fe07384703067fa8e5d | f3705af28f175ce48d8abad95944accb7aacc45d6a8a50c47b24af5c5144595f | 334674 |
| P2 Hiroshige | 6918cb8bbe4b4bec2d6dd9bafb1636901ed2a46f9df8e49566749e404d1664ae | 5b772facb5db886c18fa96c05b9c8fb1a459eaaff931a4a8c121896edf970ee2 | 646242 |
| P3 Blanco | bfaadf5b6b912416f770c1bf579c3467e47c662efd130b5656292bb86171eca9 | be071fdae81a71b48d76383bd33147371968f44e37eef4312102d52dea6d0c94 | 142340 |

Each pair is identical between core and edition (same payload, both
measures). Credits verbatim from the
Commons Artist field and placed: P1
`Eugène Atget (1857-1927), photographie, domaine public`; P2
`Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA`; P3
`Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public`.

## 7. Web PDF verification (final, after the render.py fix below)

- Freshly generated from this edition's own cards (never from the core).
  `pdfinfo`: 8 pages, 936×1296 pts (= 1950×2700 at 150 dpi).
- `pdftoppm -png -r 150` renders 8 pages, each 1950×2700, aligned
  1:1 with the cards (no noise pages, no missing/extra pages). Mean
  abs diff vs cards: p1 6.62, p2 6.53, p3 5.95, p4 6.47, p5 5.36,
  p6 5.62, p7 6.77, p8 9.53 — JPEG + poppler-resampling level, not
  content difference (spot-checked visually: rendered pages match
  the cards).
- Extracted JPEG streams (`pdfimages -j`) decode cleanly on all 8
  pages: mean abs diff vs cards p1 3.29, p2 3.32, p3 2.97, p4 3.25,
  p5 2.75, p6 2.95, p7 3.32, p8 4.56 — q75-class fidelity, tracking
  fresh q75 decodes within 0.06–0.08 (fresh q72 decodes are
  near-identical by this metric, so decode metrics alone cannot
  separate q72/q75; the quality setting is known from the code:
  `render.py` QUALITY=75).
- q72/q75 byte conclusion: NO byte-match between extracted streams
  and fresh direct Pillow saves across q72/q75 × optimize True/False
  × subsampling 0/1/2 (12 combos). Cause: Pillow's PDF writer
  re-encodes during PDF save (and rewrites JFIF density to the
  150 dpi resolution), so byte-identity with direct saves is not
  achievable by construction. Effective quality is q75-class by
  decode metrics; there is no q72 evidence. (The FR×EN KIT's q75
  note and the core KIT §7 q72 snippet are thus reconciled: the
  writer path, not the save quality, breaks byte-identity.)
- NOISE BUG FOUND AND FIXED (2026-10-28, post-round-4): the first
  web PDF built by this edition decoded as psychedelic noise on
  pages 1–7 (mean diff ~100–133; page 8 clean at 4.6). Root cause,
  reproduced exactly: `render.py` reused ONE temp JPEG path
  (`/tmp/fr-ru-webpage.jpg`) for all 8 pages while `Image.open()`
  is lazy — all 8 handles pointed at the same path as each iteration
  overwrote it, so Pillow's PDF writer embedded byte-salad for
  pages 1–7; only page 8 (written last, never overwritten) stayed
  valid. An independent-temp-file rebuild decodes clean; the
  shared-path rebuild reproduces the noise byte-for-byte in
  isolation. Fix: per-page temp files in `render.py` (see §9).
  Rebuilt web PDF verified clean by all three decoders (PIL,
  ffmpeg, poppler). Cards and print PDF regenerated by the same
  re-run are byte-identical to the pre-fix run (see §8).
  FLAG FOR THE COORDINATOR: this shared-temp-plus-lazy-open pattern
  is a plausible explanation for the FR core's own web-PDF noise
  issue (parent's open item) — worth checking the core's web
  renderer for the same pattern.
  (One early viewer preview of a noisy render appeared clean; all
  deterministic decoders — PIL, ffmpeg, poppler, twice byte-identical
  — agree on noise for the old file and clean for the new file. The
  anomaly is unreproduced and not relied upon.)

## 8. PDF pins + toolchain

- Print `Le-Lucerna-VOL3-RU.pdf`: 9,751,728 bytes,
  sha256 `4c6c11f156c4a5b0415262733cd02262a8865fe8188395a50b56389a66645011`,
  8 pages (pypdf).
- Web `Le-Lucerna-VOL3-RU-web.pdf` (REBUILT after the render.py fix;
  the pre-fix file was 6,345,405 bytes, sha256
  `9f766c04…`, and decoded as noise on pages 1–7 — see §7):
  5,281,069 bytes,
  sha256 `9c9e6e20b49033f9dc572c6b3b45d8b47b5f3180445d36629f160480fe8fee80`,
  8 pages. Cards and print PDF from the same re-run are byte-identical
  to the pre-fix run (card hashes in §8 unchanged; print PDF hash
  unchanged).
- Toolchain: build driver (`import content12, …`) and `render.py` both
  run under `tools/venv/bin/python`: Python 3.12.3, Pillow 13.0.0.
  `render.py` uses venv cairosvg (system python3 lacks cairosvg).
  Cards 1950×2700 PNG; web PDF JPEG quality=75 (`WEB_QUALITY` override
  available; default used).
- SVG hashes (delivered): p1 `d74bd9e4…`, p2 `d3dd4fc7…`, p3
  `99ba2d81…`, p4 `4b57dc7a…`, p5 `ae965ac0…`, p6 `6c9bcf77…` (= round-2
  baseline, unchanged since), p7 `7820e804…`, p8 `39bc364a…`
  (full values in `pre-fix-round4.sha` comparison / sha256sum run).

## 9. Round log + baselines

- Baseline: shipped core SVGs hashed to `core-prebuild.sha`; freeze
  baseline (`tools/freeze.py baseline` on a pristine core-build copy)
  8/8 byte-identical; shipped core SVGs re-hashed unchanged at build
  start. Baseline copy: `tools/scratch/baseline-fr-w45/build-copy/`.
- Round 1: 298 asserted pairs (FR×EN inventory, old strings never
  retyped) + OUT repoint + explicit P8 keys block (PRINT_NOTES 97,
  RU separator, half-width brackets). Render defects: P1-headline
  overflow (RU gloss 7 lines vs 5), P2 ET VOUS/date collision,
  P4-micro head too wide, P7-clinic +2px, P8-battery +116, P8-keys +579.
- Round 2: P1 gloss → measured 5-line form; P2 date dy +120 (WRONG —
  broke P2-ex: a top shift of D eats 4D of four-column capacity vs
  197px slack); P4-micro head shortened; P7 clinic bridge → 2 lines;
  P8 E stems → core line counts; P8 printed-note shortenings (~50
  notes). Result: all flows green except P2-ex overflow (2981).
- Round 3: ET VOUS note → measured 3-line form (−87px) + date dy
  1690→1610 (+40 vs core). Result: all flows green, P2 col3 1567.6,
  P2-ex 2456. Baseline `pre-fix-round3.sha`.
- Round 4: occlusion-audit NEW flags (9 defect classes, all measured
  with `text_w` before fixing): P1 LES DATES title → ДАТЫ УИК-ЭНДА;
  P1 agenda footer sentence → `Итоги: суббота вечером и воскресенье.`
  (the old line's ink ran to 2276, past the page edge — p.text does
  not wrap); P1 DANS CE NUMÉRO → В НОМЕРЕ (W43 precedent); P3 mots
  title → СЛОВА; P3 word-list line → `un jour férié — праздничный
  день`; P3 DATES À RETENIR → КАЛЕНДАРЬ; P4 tennis title → ТЕННИС;
  P4 À SUIVRE → ПРОДОЛЖЕНИЕ; P5 music title → МУЗЫКА; P5 creator
  title → КРЕАТОРЫ; P7 disclosure → 2-line form (see §10).
  Result: audit 0/0/0; change scope exactly p1/p3/p4/p5/p7 vs round-3
  baseline. Baseline `pre-fix-round4.sha`.
- Reproducibility (ko-ru B-1 lesson): fresh core-build copy +
  `transform.py` sections run in order 1→2→3→4 reproduces the delivered
  SVGs **8/8 byte-identical** (repro run in
  `hidden_files/weekly-report-w45-fr-ru-build/scratch/repro/`,
  OUT redirected to scratch; stray `files/repro-out/` dir removed).
  NOTE — first repro attempt ran only `TRANSFORM_ROUND=4` (the
  section mechanism runs one round per invocation; the header says
  so, but the builder misread it). That run asserted out before
  writing any content file, so its driver run rendered pristine core
  files and rewrote the shipped core SVGs — verified afterwards
  **8/8 byte-identical** to `core-prebuild.sha` (mtimes changed, bytes
  unchanged). No harm; the correct sequential repro above is the
  proof of record.
- Post-round-4 render fix (not a paper change): `render.py` web
  section now uses per-page temp JPEG files (see §7). No SVG, card,
  or print-PDF byte changed in the re-run (verified by hash).
- Single source: `transform.py` in the build dir is the only edit
  source for the paper; no content file was edited directly; no
  script was run in place that writes SVGs back into the delivery
  dir (all scratch runs redirected OUT first, except the incident
  above, which wrote only pristine-core bytes to the core dir and
  was verified harmless).

## 10. Readers' corner (P7, verbatim from the SVG)

- French editorial example (labelled):
  `« Mon week-end de novembre : samedi, j'ai regardé un match à la
  télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt
  pages. » — Exemple de la rédaction (ce texte n'est pas une lettre
  de lecteur).`
- French editorial note (frozen):
  `Note de la rédaction : aucun texte du VOL.2 n'était arrivé au
  moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4
  reprendra la promesse.`
- Russian comment with the explicit imperative solicitation (covers
  BOTH letters and best P8 texts; the VOL.4 preview strip is not
  counted as the solicitation):
  `Комментарий редакции: passé composé уверенный, точка с запятой
  хорошо соединяет два дня. Присылайте письма и лучшие сочинения со
  стр. 8 — для VOL.4!`
- Russian three-fact disclosure (no real letters; no VOL.2 P8 best
  essays; both deferred to VOL.4; FR-family core is VOL.3):
  `Примечание редакции: настоящих писем и лучших сочинений VOL.2 со
  стр. 8 не поступило (W44 не вышел); здесь — помеченный пример,
  настоящие работы — в VOL.4.`
  (2 lines; ink bottom ≈2238 < box bottom 2258.)
- Zero fabrication: no real letters, no VOL.2 P8 best essay, both
  deferred to VOL.4.

## 11. Deviations / compressions (all deliberate, all measured)

- P1 gloss 5-line form: fractions `½/¼ финала`, `шоу` for nocturne,
  dictionary-style dropped `la` before `coquille Saint-Jacques`.
- P8 note shortenings (round 2, ~50 notes; notes print only on P8;
  hints kept accurate): e.g. #129 → `понедельник — учебный день`;
  #128 → `рано спать: в понедельник в школу`; #120 →
  `si + imparfait → conditionnel; j' = je`; #106 →
  `créateurs (мн. число) → rencontrent, не rencontre`.
- Title shortenings (round 4, §9): all chosen by measured width with
  ≥30px margin except P5 `PARIS CREATOR WEEK · КРЕАТОРЫ` (advance
  right 1880 vs border 1885; audit ink confirms inside — proofreader
  may eyeball the P5 creator box title, which sits 5px from the box
  edge by advance measure).
- #138 stem nuance (for the proofreader): bare
  `Этим вечером будем собирать портфели.` — every prefixed form
  (`Перевод: …`, `Мы …`) wrapped to 2 lines at 20pt serif in the
  battery column; the bare form keeps both cues (`Этим вечером` =
  ce soir; `будем + infinitive` = futur proche) and drops only the
  implied `мы`. French key byte-identical.
- Inherited (not defects): P1-hiver flow 2298 vs 2290 bottom; P6-ex
  2557 vs 2540 bottom; P8 F-group ink rights 1891/1899 (see §5); P5
  `: clôture du festival.` line-start colon (core-identical).

## 12. Open observations for the independent proofreader

1. #138 stem bare form (see §11) — confirm the dropped implied `мы`
   is acceptable for the translation exercise.
2. P5 creator box title margin (advance right 1880 vs border 1885) —
   audit ink passes; visual check on the P5 card confirms it sits
   inside the box.
3. P5-main ends at 2532 (8px margin) and P6-opinion at 1286 (14px
   margin) — tight by design; any lengthening breaks them.
4. The banned intermediary term appears nowhere in the delivered paper
   or build code (grep 0 across SVGs, transform.py, content files).
5. `ABSTRACT.txt`: Russian single line, no ASCII double quotes, real
   topic keywords + learner search phrase
   (`как учить французский по настоящим новостям недели`).

## 13. Reproducibility recipe

Fresh copy of `hidden_files/weekly-report-w45-fr-build/` (`*.py` +
`assets/`) → copy `transform.py` from this edition's build dir →
run `TRANSFORM_ROUND=1`, then `2`, `3`, `4` sequentially in that dir
(each run applies only its own section) → redirect OUT to scratch →
single-process driver `import content12, content34, content56,
content7, content8` → `render.py` (venv) → 8/8 SVG byte-identical to
§8; cards + PDFs regenerate from those SVGs.
