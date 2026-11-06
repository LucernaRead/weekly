# WEEKLY-KIT — De Lucerna · Semanario neerlandés VOL.3 · NL × ES

Edition slug: `2026-w46-nl-es`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
Spanish. Built by the W46 NL builder; insert is the coordinator's job.

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
and Spanish (`Sin cartas reales ni mejores textos: ejemplo; promesa para
el VOL.4.`); promise carried forward to VOL.4. No fabricated readers,
letters, names or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (DATOS DE PRÁCTICA):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × ES measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS`.
- Subtitle (40pt): `SEMANARIO NEERLANDÉS · VOL.3 · SINTERKLAAS ·
  SINT-MAARTEN · ORANJE` (measured 1600.0px < 1820, all theme words kept).
- Pairing badge INSERTED at y=568, 20pt bold BRICK, strapline kept verbatim:
  `TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS
  LECTORES HISPANOHABLANTES` (measured 1116.5px, fits).
- Footer: `De Lucerna · SEMANARIO NEERLANDÉS VOL.3 · TEXTO EN NEERLANDÉS ·
  EXPLICACIONES EN ESPAÑOL` + `Página N de 8`. Gloss prefix `Nota — `.
  Glosses/bridges use `: ` separators; P8 notes use ` = `. P8 separator
  `— PAGINA {n} —` kept (Dutch form, as shipped in W45 ES). P7 quote page
  tags `(Pagina N)` kept (W45 ES form).
- P8 keys 13.0pt/1.12/0.4 gap, Flow bottom and separators at core values
  (2552; 14pt/1.16/2) — W45 ES precedent. `bridge()` kept. svglib unchanged
  except the `for Double Ninth` docstring.
- Registry labels: type tokens stay Chinese (registry-only, never printed
  — same precedent as FR); only the printed instruction words were
  localised. The disclosure variable was renamed `dt_zh` → `dt_es`
  (W45 ES had kept the `dt_zh` name; renaming is cosmetic and consistent
  with DE/FR).
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is Spanish. Clinic Dutch wrong/right sentences verbatim; notes in
  Spanish. Translation items 137/138 re-aimed NL→ES (keys are the Spanish
  translations); 139/140 prompts re-aimed ES→NL (keys stay Dutch). All
  four carry instr `Traducir` (W45 ES precedent).

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
Spanish with `(Pagina N)` page tags; quote-2 gloss kept to one line
(`Al día siguiente, domingo 15 de noviembre: Ámsterdam, 88.ª edición.`).

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-es-build/` (copied from the
W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to Spanish
(`gen_es.py`, kept at `hidden_files/w46/gen_es.py`; 292 replacements,
FAILED: 0; post-transform CJK scan lines are all Chinese registry type
tokens by design — verified zero non-type CJK lines). The pairs file was
re-extracted from the shipped EN transform after a /tmp wipe
(`hidden_files/w46/en-reps.txt`, 265 pairs; the duplicate rep is deduped).
Freeze baseline before transform: 8/8 byte-identical, core untouched.
Build: `run.py` (one process) + `render.py` (cards + print PDF). Web PDF
via `tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-ES.pdf` (6,642,975 bytes), web PDF
`De-Lucerna-VOL3-ES-web.pdf` (776,058 bytes, 46,675 text bytes),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-es.text.md` (exported from
the source manuscript via `hidden_files/w46/export_text.py`, never from PDF).

## 8. Fix record (W46 ES)

- Fix 1 — box titles: P6 `VOOR OF TEGEN? · ¿A FAVOR O EN CONTRA?` (ink
  1931.0) → `… · PRO Y CONTRA`; P7 `HET WOORD · PALABRA DE LA SEMANA`
  (1918.0) → `… · LA PALABRA`.
- Fix 2 — box titles: P1 `Agenda van de week · LOS ACONTECIMIENTOS`
  (1893.2) → `… · AGENDA`; `IN DEZE EDITIE · EN ESTE NÚMERO` (1892.2) →
  `… · SUMARIO`.
- Anticipated from the start: telegraphic P7 clinic notes, short
  disclosure/invitation (P7 col-3 stack ends 1927.5, same as core, above
  the 1937 rule), match_set instr `Relacionar`, chart title
  `DE GRAFIEK · DATOS DE PRÁCTICA`.

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
  (legal re-aims: keys are the Spanish translations).
- Web PDF: 776,058 bytes (<7 MB), 46,675 text bytes (>0).
- Visual check: P1 and P7 viewed (badge insert, strapline kept, letters
  box above the quotes rule).

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in Spanish; Dutch target
text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: `150 ejercicios para aprender neerlandés con las noticias neerlandesas.` After tail: `s de práctica sobre los temas de esta semana para aprender neerlandés.`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: 0 lines (byte-identical to the pre-fix build sources).

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): strict-CJK added 0, edition CJK total 0; exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 37510 bytes; web PDF 776057 bytes, pdftotext 46675 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 6642975 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.
