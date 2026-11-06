# WEEKLY-KIT — De Lucerna · Settimanale olandese VOL.3 · NL × IT

Edition slug: `2026-w46-nl-it`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
Italian. Built by the W46 NL builder; insert is the coordinator's job.

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
and Italian (`Niente lettere vere, niente testi migliori — esempio;
promessa al VOL.4.`); promise carried forward to VOL.4. No fabricated
readers, letters, names or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (DATI INVENTATI):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × IT measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · OGNI SETTIMANA IN OLANDESE`.
- Subtitle at 36pt (W43 size): `SETTIMANALE OLANDESE · VOL.3 ·
  SINTERKLAAS · SINT-MAARTEN · ORANJE` (measured 1429.7px < 1820).
- Pairing badge INSERTED at y=568, 20pt bold BRICK, strapline kept verbatim:
  `TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI
  ITALIANI` (measured 857.2px, fits).
- Footer: `De Lucerna · SETTIMANALE OLANDESE VOL.3 · TESTI IN OLANDESE ·
  SPIEGAZIONI IN ITALIANO` + `Pagina N di 8`. Gloss prefix `Nota — `.
  Glosses/bridges use ` = ` separators with `; ` between items; P8 notes use
  ` = `. P8 separator `— PAGINA {n} —` kept (Dutch form, as shipped in
  W45 IT). P7 quote page tags `(Pagina N)` kept.
- P8 keys 13.0pt/1.14/0.3 gap, Flow bottom 2540, separators 13.5pt/1.17/1.5
  gap — EN/DE sizes. `bridge()` kept. svglib unchanged except the
  `for Double Ninth` docstring.
- Registry labels: type tokens TRANSLATED (Cloze, Completa la frase,
  Abbinamento, Vero o falso, Scelta multipla, Forma la frase, Traduzione,
  Scrittura — W45 IT precedent; the type pass also converts the P8
  `if e_["type"] == "Scrittura":` check). Instruction words localised
  (Completa, Vero o falso?, Forma la frase, Scrivi, Traduzione with
  per-direction `Traduci in italiano` / `Traduci in olandese`); match instr
  `Abbina la parola al significato`. The disclosure variable was renamed
  `dt_zh` → `dt_it`.
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is Italian. Clinic Dutch wrong/right sentences verbatim; notes in
  Italian. Translation items 137/138 re-aimed NL→IT (keys are the Italian
  translations); 139/140 prompts re-aimed IT→NL (keys stay Dutch).

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
Italian with `(Pagina N)` page tags; quote-2 gloss kept to one line
(`Il giorno dopo, domenica 15 novembre: l'arrivo ad Amsterdam, 88ª
edizione.`).

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-it-build/` (copied from the
W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to Italian
(`gen_it.py`, kept at `hidden_files/w46/gen_it.py`; 330 replacements,
FAILED: 0; the pairs file `hidden_files/w46/en-reps.txt` was re-extracted
from the shipped EN transform after a /tmp wipe — 265 pairs, exact EN
wording differs in places from the first extraction, e.g. `Translate into
English/Dutch` direction refinements and `True:`/`False:` forms; the IT
generator maps those exact forms). Freeze baseline before transform: 8/8
byte-identical, core untouched. Build: `run.py` (one process) +
`render.py` (cards + print PDF). Web PDF via `tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-IT.pdf` (6,641,175 bytes), web PDF
`De-Lucerna-VOL3-IT-web.pdf` (768,441 bytes, 46,429 text bytes),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-it.text.md` (exported from
the source manuscript via `hidden_files/w46/export_text.py`, never from PDF).

## 8. Fix record (W46 IT)

- Fix 1 — box titles: P1 `IN DEZE EDITIE · IN QUESTO NUMERO` (ink 1924.8)
  → `… · SOMMARIO`; P6 `DE GRAFIEK · DATI DI ESERCITAZIONE` (1924.0) →
  `… · DATI INVENTATI`; P7 `HET WOORD · PAROLA DELLA SETTIMANA` (1949.8)
  → `… · LA PAROLA`.
- Fix 2 — P1 flow overflow: the long Italian numbers-box parentheticals
  pushed the whole box from column 1 to column 2, overflowing the
  P1-headline flow (col 2 y=1788, need 99) and spilling item 6 into the
  feature box. Shortened to EN-style forms: `(9 nov.: notiziario)`,
  `(14 nov.: Grave)`, `(15 nov.: 88ª)`. Overflow gone, item 6 back in flow.
- Anticipated from the start: telegraphic P7 clinic notes (`Sinterklaas
  è un nome, senza articolo.` etc.), short disclosure/invitation, item-6
  note shortened to `Plurale → zetten.` (kept as a safety measure; the
  flow fix was the real cure), chart title `DE GRAFIEK · DATI INVENTATI`.

## 9. Gates (2026-11-02, recorded in `hidden_files/w46/nl-gates.log`)

- Builder self-check: TOTAL 150, by page 10/18/18/18/18/18/12/38, zero
  FLOW OVERFLOW / HEAD TOO WIDE (after Fix 2).
- `occlusion_audit.py`: selftest OK, edition 0 flags, core 0 flags,
  NEW vs core: 0.
- Same-baseline furniture scan (rowcheck.py): all 8 pages CLEAN; P6
  chart-label GRAZE coverage 0.0%; gloss counts core-vs-edition OK
  (6/5/5/5/5).
- `freeze.py diff --strict-cjk`: added CJK 0, edition CJK total 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138]
  (legal re-aims: keys are the Italian translations).
- Web PDF: 768,441 bytes (<7 MB), 46,429 text bytes (>0).
- Visual check: P1 viewed (badge insert, strapline kept, SOMMARIO fits,
  item 6 in flow).

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in Italian; Dutch target
text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: `i A2–B2, 150 esercizi per imparare l'olandese con le notizie olandesi.` After tail: `rcizi di pratica sui temi di questa settimana per imparare l'olandese.`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: 0 lines (byte-identical to the pre-fix build sources).

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): strict-CJK added 0, edition CJK total 0; exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 39093 bytes; web PDF 768440 bytes, pdftotext 46429 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 6641175 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.
