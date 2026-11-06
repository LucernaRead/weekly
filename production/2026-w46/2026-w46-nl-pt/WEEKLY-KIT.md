# WEEKLY-KIT — De Lucerna · Semanário neerlandês VOL.3 · NL × PT

Edition slug: `2026-w46-nl-pt`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
Portuguese. Built by the W46 NL builder; insert is the coordinator's job.

## 1. Topics and sources

Same verified fact base as the W46 NL core and the NL × EN edition (see
`files/weekly-report-w46-nl-en/WEEKLY-KIT.md` §1): Sinterklaasjournaal
from 9 Nov, national arrival Grave 14 Nov, 88th Amsterdam arrival 15 Nov,
Sint-Maarten 11 Nov, Oranje Nations League vs Greece (13 Nov) and Germany
(16 Nov preview), Heel Nederland Leest (`Het diner`, Herman Koch),
Expeditie Robinson (Sundays 20:00 RTL 4). No invented polls, quotes,
accounts or results; no squad names used. Weekdays verified
`TZ='Europe/Amsterdam'`.

## 2. Promises honoured (from W45 NL VOL.2)

Sinterklaas arrival Amsterdam 15 Nov and Sint-Maarten 11 Nov are the lead
topics. Readers' corner: no real letters or best page-8 texts had arrived
at press time — labelled editor's example + on-page disclosure in Dutch
and Portuguese (`Sem cartas reais nem melhores textos — exemplo; promessa
para o VOL.4.`); promise carried forward to VOL.4. No fabricated readers,
letters, names or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (DADOS DE TREINO):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × PT measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · O NEERLANDÊS QUE OS
  NEERLANDESES LEEM`.
- Subtitle stays Dutch (40pt): `WEEKBLAD IN HET NEDERLANDS · VOL.3 ·
  SINTERKLAAS · SINT-MAARTEN · ORANJE` (same as EN).
- Pairing badge REPLACES the strapline at y=372, 19.5pt bold BRICK:
  `TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS
  LEITORES DE LÍNGUA PORTUGUESA`.
- Footer: `De Lucerna · SEMANÁRIO NEERLANDÊS VOL.3 · TEXTOS EM NEERLANDÊS
  · EXPLICAÇÕES EM PORTUGUÊS` + `Página N de 8`. Gloss prefix `Nota — `.
  Glosses use ` = ` + ` · ` separators; P7 bridges use `; `. P8 notes use
  ` = `. P8 separator `— PÁGINA {n} —` (accented W43 form). P7 quote page
  tags `(Página N)`.
- P8 keys 13.0pt/1.14/0.3 gap, Flow bottom 2540, separators 13.5pt/1.17/1.5
  gap — EN/DE sizes. `bridge()` kept. svglib unchanged except the
  `for Double Ninth` docstring.
- Registry labels: type tokens are ENGLISH (complete/choice/cloze choice/
  make sentences/translate/true or false/writing — registry-only, never
  printed, same as EN); only the printed instruction words were localised
  (Complete, Verdadeiro ou falso?, Forme a frase, Escreva, Traduzir with
  per-direction `Traduza para o português` / `Traduza para o neerlandês`).
  The two match sets carry different instrs, as shipped in W45 PT: P2
  `Ligue palavra-significado`, P8 `Associe a palavra ao significado`. The
  disclosure variable was renamed `dt_zh` → `dt_pt`.
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is Portuguese. Clinic Dutch wrong/right sentences verbatim; notes
  in Portuguese. Translation items 137/138 re-aimed NL→PT (keys are the
  Portuguese translations); 139/140 prompts re-aimed PT→NL (keys stay
  Dutch).

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
Portuguese with `(Página N)` page tags; quote-2 gloss kept to one line
(`Um dia depois, domingo, 15 de novembro: a chegada a Amesterdão, 88.ª
edição.`).

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-pt-build/` (copied from the
W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to Portuguese
(`gen_pt.py`, kept at `hidden_files/w46/gen_pt.py`; 334 replacements,
FAILED: 0; the pairs file `hidden_files/w46/en-reps.txt` was re-extracted
from the shipped EN transform after a /tmp wipe — 265 pairs, exact EN
wording incl. `Translate into English/Dutch` refinements and `True:`/
`False:` forms). Freeze baseline before transform: 8/8 byte-identical,
core untouched. Build: `run.py` (one process) + `render.py` (cards + print
PDF). Web PDF via `tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-PT.pdf` (6,668,628 bytes), web PDF
`De-Lucerna-VOL3-PT-web.pdf` (781,796 bytes, 46,692 text bytes),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-pt.text.md` (exported from
the source manuscript via `hidden_files/w46/export_text.py`, never from PDF).

## 8. Fix record (W46 PT)

- Fix 1 — box titles: P1 `DE WEEK IN CIJFERS · EM NÚMEROS` (ink 962.5 vs
  border 961.0, 1.5px over) → `… · NÚMEROS`; P6 `VOOR OF TEGEN? · A FAVOR
  OU CONTRA?` (1904.2) → `… · PRÓS E CONTRAS`.
- Anticipated from the start: short P1 bridge (3 items) and short word
  gloss (W45 PT overflow lessons), telegraphic P7 clinic notes, short
  disclosure/invitation, chart title `DE GRAFIEK · DADOS DE TREINO`,
  numbers-box parentheticals kept to EN-style short forms.

## 9. Gates (2026-11-02, recorded in `hidden_files/w46/nl-gates.log`)

- Builder self-check: TOTAL 150, by page 10/18/18/18/18/18/12/38, zero
  FLOW OVERFLOW / HEAD TOO WIDE.
- `occlusion_audit.py`: selftest OK, edition 0 flags, core 0 flags,
  NEW vs core: 0.
- Same-baseline furniture scan (rowcheck.py): all 8 pages CLEAN; P6
  chart-label GRAZE coverage 0.0%; gloss counts core-vs-edition OK
  (6/5/5/5/5).
- `freeze.py diff --strict-cjk`: added CJK 0, edition CJK total 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138]
  (legal re-aims: keys are the Portuguese translations).
- Web PDF: 781,796 bytes (<7 MB), 46,692 text bytes (>0).
- Visual check: P1 viewed clean (badge replaces strapline, Dutch subtitle
  kept, item 6 in flow, bridge 2 lines, numbers box fits).

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in Portuguese; Dutch
target text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: ` 150 exercícios para aprender neerlandês com as notícias neerlandesas.` After tail: `ícios de prática sobre os temas desta semana para aprender neerlandês.`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: exactly 1 line (the E-1 bridge below).
- E-1: P3 bridge (D · REKENEN) `transform.py` new-string `Calcula: responde com os números da página 3.` → `Calcula: responde com números da página 3.` — now one line (427.3px ≤ 434), no stranded `3.`. Verified visually on the P3 card (full frame + crop).

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): strict-CJK added 0, edition CJK total 0; exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 38265 bytes; web PDF 781803 bytes, pdftotext 46689 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 6668637 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.
