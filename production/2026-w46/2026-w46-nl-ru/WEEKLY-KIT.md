# WEEKLY-KIT — De Lucerna · Голландский еженедельник VOL.3 · NL × RU

Edition slug: `2026-w46-nl-ru`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
Russian. Built by the W46 NL builder; insert is the coordinator's job.

## 1. Topics and sources

Same verified fact base as the W46 NL core and the NL × EN edition (see
`files/weekly-report-w46-nl-en/WEEKLY-KIT.md` §1): Sinterklaasjournaal
from 9 Nov, national arrival Grave 14 Nov, 88th Amsterdam arrival 15 Nov,
Sint-Maarten 11 Nov, Oranje Nations League vs Greece (13 Nov) and Germany
(16 Nov preview), Heel Nederland Leest (`Het diner`, Herman Koch),
Expeditie Robinson (Sundays 20:00 RTL 4). No invented polls, quotes,
accounts or results; no squad names used. Weekdays verified
`TZ='Europe/Amsterdam'`. Target name is ГОЛЛАНДСКИЙ (everyday Russian
form; overrides НИДЕРЛАНДСКИЙ).

## 2. Promises honoured (from W45 NL VOL.2)

Sinterklaas arrival Amsterdam 15 Nov and Sint-Maarten 11 Nov are the lead
topics. Readers' corner: no real letters or best page-8 texts had arrived
at press time — labelled editor's example + on-page disclosure in Dutch
and Russian (`Настоящих писем и лучших сочинений со страницы 8 пока нет —
печатаем пример; обещание — в VOL.4.`); promise carried forward to VOL.4.
No fabricated readers, letters, names or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (УЧЕБНЫЕ ДАННЫЕ):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × RU measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · ЧИТАЕМ ПО-ГОЛЛАНДСКИ`
  (the W45 form `ГОЛЛАНДСКИЙ, КОТОРЫЙ ЧИТАЮТ ГОЛЛАНДЦЫ` ran into the
  date text with no gap; measured replacement ends at 1284.0, date starts
  at 1407.1).
- Subtitle (40pt): `ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · СИНТЕРКЛААС ·
  СИНТ-МАРТЕН · ОРАНЬЕ` (measured 1804.2px < 1820, all theme words kept).
- Pairing badge REPLACES the strapline at y=372, 19.5pt bold BRICK:
  `ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ
  РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ` (measured 1033.4px, fits).
- Footer: `De Lucerna · ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА
  ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ` + `Страница N из 8`. Gloss prefix
  `Пояснение — `. Glosses/notes use ` — ` separators with ` · ` between
  items; P7 bridges use `; `. P8 separator `— СТРАНИЦА {n} —`. P7 quote
  page tags `(Страница N)`.
- P8 keys 13.0pt/1.14/0.3 gap (EN/DE sizing — W45 RU core sizes overflowed
  with the longer Russian notes; see Fix 3), Flow bottom 2552 and
  separators 14pt/1.16/2 at CORE values. `bridge()` renamed to `expl()`
  (signature unchanged; expl strings carry their own `Пояснение — ` prefix
  where needed). svglib unchanged except the `for Double Ninth` docstring.
- Registry labels: type tokens TRANSLATED to Russian (Выбор в тексте,
  Дополнение предложения, Сопоставление, Верно или неверно, Выбор ответа,
  Составление предложения, Перевод, Сочинение); instruction words localised
  (Заполните пропуск, Верно или нет?, Составление предложения, Сочинение,
  Перевод — all four translation items carry `Перевод`, no direction
  refinement, W45 RU precedent; match instr `Сопоставьте пары слов`). The
  disclosure variable KEEPS the name `dt_zh` (W45 RU precedent).
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is Russian. Clinic Dutch wrong/right sentences verbatim; notes in
  Russian. Translation items 137/138 re-aimed NL→RU (keys are the Russian
  translations); 139/140 prompts re-aimed RU→NL (keys stay Dutch).

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
Russian with `(Страница N)` page tags; quote-3 gloss shortened to one line
(`День святого Мартина: делиться светом, едой, вниманием.`) so the tag
does not wrap onto the next quote.

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-ru-build/` (copied from the
W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to Russian
(`gen_ru.py`, kept at `hidden_files/w46/gen_ru.py`; 336 replacements,
FAILED: 0; the pairs file `hidden_files/w46/en-reps.txt` was re-extracted
from the shipped EN transform after a /tmp wipe — 265 pairs, exact EN
wording incl. `Translate into English/Dutch` refinements and `True:`/
`False:` forms). Freeze baseline before transform: 8/8 byte-identical,
core untouched. Build: `run.py` (one process) + `render.py` (cards + print
PDF). Web PDF via `tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-RU.pdf` (6,567,363 bytes), web PDF
`De-Lucerna-VOL3-RU-web.pdf` (809,218 bytes, 55,313 text bytes),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-ru.text.md` (exported from
the source manuscript via `hidden_files/w46/export_text.py`, never from PDF).

## 8. Fix record (W46 RU)

- Fix 1 — `bridge()` rename gap: the writing-bridge line is an f-string
  call `f.bridge(f"...")` whose rep covers only the inner string, so the
  value rename missed the call (`AttributeError: Flow has no attribute
  bridge`). Added a furniture rep renaming that call to `f.expl(f"`.
- Fix 2 — P1 flow overflow: long Russian numbers-box parentheticals pushed
  the box to column 2 (same mechanism as IT Fix 2). Shortened to
  `(9 нояб.: новости)` / `(14 нояб.: Граве)`.
- Fix 3 — P8-keys flow overflow: Russian notes wrap longer, overflowing
  the core-sized P8 key flow (need 16px in col 3). P8 keys tightened to
  13.0/1.14/0.3 (EN/DE sizes); Flow bottom and separators kept at core
  values.
- Fix 4 — P1 COVER: the Russian word gloss ran 2 lines, its second line
  falling under the IN HET KORT box (drawn later). Shortened to one line:
  `«De intocht»: праздничное прибытие в город.`
- Fix 5 — P7 TEXTX: quote-3 gloss wrapped, its `(Pagina 2)` tag tail
  landing on the next quote. Shortened to one line (see §5).
- Fix 6 — P8 TEXTX: the P8 head + subhead ran 2 lines and overlapped.
  Shortened to `ANTWOORDEN · КЛЮЧ ОТВЕТОВ — найди свой номер` /
  `Каждый ответ с заметкой на русском · ✓ — сочинение`.
- Fix 7 — P7 stack graze (visual check): the letters box bottom edge sat
  on the gold rule (1956.5 vs 1937). Invitation shortened to one line
  (`Пример редакции — присылай свои!`); stack ends 1927.5, same as core.
- Fix 8 — P1 top-strip collision (visual check; the scans missed it): the
  long centre text touched the right-aligned date text
  (`ГОЛЛАНДЦЫWEEK VAN 9...`). Centre text replaced with the measured
  shorter form (see §4); clean 123px gap verified in the strip crop.

## 9. Gates (2026-11-02, recorded in `hidden_files/w46/nl-gates.log`)

- Builder self-check: TOTAL 150, by page 10/18/18/18/18/18/12/38, zero
  FLOW OVERFLOW / HEAD TOO WIDE (after Fixes 2–3).
- `occlusion_audit.py`: selftest OK, edition 0 flags, core 0 flags,
  NEW vs core: 0.
- Same-baseline furniture scan (rowcheck.py): all 8 pages CLEAN; P6
  chart-label GRAZE coverage 0.0%; gloss counts core-vs-edition OK
  (6/5/5/5/5).
- `freeze.py diff --strict-cjk`: added CJK 0, edition CJK total 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138]
  (legal re-aims: keys are the Russian translations).
- Web PDF: 809,219 bytes (<7 MB), 55,313 text bytes (>0).
- Visual check: P1 viewed clean (badge replaces strapline, top strip gap
  verified, item 6 in flow, word gloss 1 line); P7 letters-box crop viewed
  (Fix 7 verified: clean gap above the rule).

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in Russian; Dutch target
text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: `–B2, 150 упражнений для изучения голландского по голландским новостям.` After tail: `рактических упражнений по темам этой недели для изучающих голландский.`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: 0 lines (byte-identical to the pre-fix build sources).
- Record correction: this KIT's §7 web-PDF text-bytes figure 55,344 is stale; the measured value on the final artifacts is 55,313 (this KIT's §9 already stated 55,313).

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): strict-CJK added 0, edition CJK total 0; exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 39651 bytes; web PDF 809219 bytes, pdftotext 55313 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 6567209 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.
