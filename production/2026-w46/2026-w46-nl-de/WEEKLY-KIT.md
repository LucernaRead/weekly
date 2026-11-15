# WEEKLY-KIT — De Lucerna · Niederländische Wochenzeitung VOL.3 · NL × DE

Edition slug: `2026-w46-nl-de`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
German. Built by the W46 NL builder; insert is the coordinator's job.

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
and German (`Keine echten Briefe, keine besten Texte — Beispiel;
Versprechen für VOL.4.`); promise carried forward to VOL.4. No fabricated
readers, letters, names or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (ÜBUNGSDATEN):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × DE measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH`.
- Subtitle (40pt): `NIEDERLÄNDISCH · VOL.3 · SINTERKLAAS · SINT-MAARTEN ·
  ORANJE` (measured 1432.6px < 1820, all theme words kept).
- Pairing badge INSERTED at y=568, 20pt bold BRICK, strapline kept verbatim:
  `NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR
  DEUTSCHSPRACHIGE LESER` (measured 1025.4px, fits).
- Footer: `De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.3 · TEXT AUF
  NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH` + `Seite N von 8`. Gloss prefix
  `Hinweis · ` (W43 form, not the tables.json `HINWEIS · `). Bridge prefix
  `Erklärung · `. P8 separator `— PAGINA {n} —` kept (Dutch form, as
  shipped in W45 DE). P7 quote page tags `(Pagina N)` kept (W45 DE form).
- P8 keys 13.0pt/1.14/0.3 gap; separators 13.5pt/1.17/1.5 gap; P8-keys flow
  bottom 2540 (W45 DE fix-1 sizes, same as EN). `bridge()` kept. svglib
  unchanged except the `for Double Ninth` docstring.
- Target name is `NIEDERLÄNDISCH` for the paper; the everyday word for the
  language in running text is German as written.
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is German. Clinic Dutch wrong/right sentences verbatim; notes in
  German. Translation items 137/138 re-aimed NL→DE (keys are the German
  translations); 139/140 prompts re-aimed DE→NL (keys stay Dutch).
- Notes avoid trailing ASCII parenthetical groups: W45 DE showed such
  notes flip `p8.py` to its paren branch (bare keys byte-identical, but
  keydiff noise). German gender is given as `, de-Wort` / `, het-Wort`
  instead of a trailing `(de)` / `(het)`.

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
German with `(Pagina N)` page tags.

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-de-build/` (copied from the
W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to German
(`gen_de.py`, kept at `/tmp/gen_de.py`; 335 replacements, FAILED: 0,
post-transform CJK scan 0 lines), loop-first order. Freeze baseline before
transform: 8/8 byte-identical, core untouched. Build: `run.py` (one
process) + `render.py` (cards + print PDF). Web PDF via `tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-DE.pdf` (5,604,980 bytes; SHA-256 `c85eb233c7782e69858d38c20f0d396ecc062cb23bbb50fa56b6d8d50d752887`), web PDF
`2026-w46-nl-de.web.pdf` (651,370 bytes, 44,400 text bytes; SHA-256 `b9627c7dbc29236b3244e043a76e7128eca81956dcf8989cc4b3e595d8a830cc`),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-de.text.md` (D5 rebuild export, `logs/2026-w46-nl-de/2026-w46-nl-de.text.md.run2`; the `production/` same-named file is the 2026-11-06 fanout product, do not use).

## 8. Fix record (W46 DE)

- Fix 1 — P1 box titles: `Agenda van de week · DIE EREIGNISSE DER WOCHE`
  and `IN DEZE EDITIE · IN DIESER AUSGABE` overflowed their boxes (ink to
  1933.2 / 1917.5 vs border 1885.0) → shortened to `… · TERMINE` and
  `… · INHALT`.
- Fix 2 — P1 word-gloss: the German `«Der intocht»` gloss ran 3 lines and
  was covered by the IN HET KORT box (COVER + TEXTX flags) → shortened to
  `«Der intocht»: Sinterklaas kommt mit dem Boot, danach zu Pferd, im
  Festzug.` (2 lines).
- Anticipated from W45 DE fix-1 and applied from the start: P8 sizes as
  §4, telegraphic P7 clinic notes, short disclosure/invitation (P7 col-3
  stack ends 1927.5, same as core, above the 1937 rule), match_set instr
  `Wort und Bedeutung zuordnen`, P6 box title `PRO UND KONTRA`, chart
  title `DE GRAFIEK · ÜBUNGSDATEN`.

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
  (legal re-aims: keys are the German translations; no paren-branch
  artifacts — notes avoid trailing paren groups per §4).
- Web PDF: 774,922 bytes (<7 MB), 46,586 text bytes (>0).
- Visual check: P1 and P7 viewed (badge insert, strapline kept, gloss
  2 lines, letters box above the quotes rule); remaining pages covered by
  rowcheck + occlusion gates.

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in German; Dutch target
text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: `ür Leser, die Niederländisch durch niederländische Nachrichten lernen.` After tail: `ungen zu den Themen dieser Woche für Leser, die Niederländisch lernen.`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: 0 lines (byte-identical to the pre-fix build sources).

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): strict-CJK added 0, edition CJK total 0; exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 38262 bytes; web PDF 774922 bytes, pdftotext 46586 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 6644100 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.

## D5 rebuild (2026-11-15, W46 nl family)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46` (`--check` dry-run first, all clean). Mode: latin. `_D5_READER` at `svglib.py:100` = `latin`; fix2 retained (`_QUOTE_CLS` x4 per file); `test_d5_routing.py` FAILURES: 0.
- Pre-fix D5 census (baseline): D5 Latin 496. Baseline: run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; print/web text layers vs shipped PDF stripped-diff 0; `issues/` pin matched; text.md BYTE-IDENTICAL vs `issues/`.
- Fixes (all font-size reductions, zero copy changes; probe = SVG-measured ink width, largest size leaving >=2px slack):
  - P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:177, head 25→22pt (ink 471.1→414.5px, slack 8.0)
  - P1 numbers box title `DE WEEK IN CIJFERS　IN ZAHLEN` — content12.py:50, f.box tsize 23→21.5 (ink 421.6→394.0px, slack 10.5)
  - P1 `IN HET KORT　KURZ GEMELDET` — content12.py:134, p.text 24→22.5pt (ink 424.6→398.0px, slack 2.5); ### line lost, see blocker
  - P2 box title `ZO ONTHOUD JE HET　MERK ES DIR` — content12.py:181, f.box tsize 23→20 (ink 452.0→393.0px, slack 11.5)
  - P6 `VOOR OF TEGEN?　PRO UND KONTRA` — content56.py:162, p.text 21→19.5pt (ink 426.9→396.4px, slack 4.1)
  - P7 `HET WOORD　WORT DER WOCHE` — content7.py:84, p.text 23→21.5pt (ink 416.9→389.7px, slack 10.8)
- P8 (run2): lines 227/227, max ink bottom 2560.0, slack to footer rule 2596 = 36.0px, slack to page bottom 2700 = 140.0px; `p8.py compare` CLEAN, keydiff=[137, 138].
- Pins (run2, final): print PDF `De-Lucerna-VOL3-DE.pdf` 5,604,980 bytes, SHA-256 `c85eb233c7782e69858d38c20f0d396ecc062cb23bbb50fa56b6d8d50d752887` (baseline 6,194,387 bytes, `4ba753d022db16927c76f907dcaccc6defe47949fea5c3880cb95be77630c241`); web PDF `2026-w46-nl-de.web.pdf` 651,370 bytes, SHA-256 `b9627c7dbc29236b3244e043a76e7128eca81956dcf8989cc4b3e595d8a830cc` (baseline 730,817 bytes, `6f9ce924f4c761fd22d8f0751fdbbc0b9e05e3eea2339f09176f28784085e056`); text.md 40,835 bytes, SHA-256 `67857267c3afbee3923b67c4f040975cb9fe7b0462ab0df88276107ff27f130e` — BYTE-IDENTICAL vs shipped (D47 補行后; G15a/G15c 针对性重验通过)
- Gates run2: 17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS). G15b record-only (D27). Full gate log: `logs/2026-w46-nl-de/GATES-SUMMARY-run2.txt` in scratch `hidden_files/d5-redo/scratch-2026-w46-nl/`. Family report: `hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`.
