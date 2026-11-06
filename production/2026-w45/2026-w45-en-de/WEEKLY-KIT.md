# WEEKLY KIT — The Lucerna VOL.2 · EN × DE (target English, reader native German)

Issue week: November 2–8, 2026 (W45). Masthead: The Lucerna. Pairing: ENGLISH
text with GERMAN explanations, for German-speaking readers. This is a BUILDER
record only. It is NOT finalization: finalization requires an independent
proofread, which has not happened for this edition.

## 1. Delivery

Directory: `files/weekly-report-w45-en-de/` — svg × 8, cards × 8, print PDF,
web PDF, this KIT, `ABSTRACT.txt`.
Build tree: `hidden_files/weekly-report-w45-en-de-build/` — `transform.py`
(every fix round appended there; each round re-copied the core build fresh,
then re-ran transform + run + render), `run.py` (single-process driver),
`render.py`, logs, baselines, gate outputs.
Core (frozen, untouched): `files/weekly-report-w45-en-core/` (VOL.2).
Core build code: `hidden_files/weekly-report-w45-en-build/`.

Print PDF: `The-Lucerna-VOL2-DE.pdf` — 17,295,556 bytes.
Web PDF: `The-Lucerna-VOL2-DE-web.pdf` — 4,027,862 bytes.
SHA-256 values are in the final verification section (§11) and in
`hidden_files/weekly-report-w45-en-de-build/run4-baseline.sha256`.

## 2. Measured counts (independent registry dump, single process)

- TOTAL exercises: 150. Per page: P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 /
  P7 12 / P8 39. Note P2 17 and P8 39 — NOT the generic 10/18/18/18/18/18/12/38.
- Levels: A2 60 / B1 69 / B2 21.
- By type: Multiple Choice 41, Satzergänzung 33, Zuordnung 20, Umformung 16,
  Lückentext 8, Anwendungsübung 8, Diagrammlesen 6, Dialogergänzung 5,
  Fehlerkorrektur 4, Leseverstehen 4, Übersetzung 4, Schreiben 1.
- P8 battery: cloze 112–119, MCQ 120–128, reading 129–132, D sentences
  133–136, E translation 137–140, F matching 141–144, G dialogue 145–149,
  writing 150.
- Model text « My Tuesday, November 3 »: 85 words by whitespace-token count,
  extracted from the edition P8 SVG, identical to the core.

## 3. Frozen vs changed inventory

FROZEN (byte-identical semantics, verified by registry + text extraction):
English article text on P1–P6; all exercise stems, options and keys except
§5; P7 definition sentences and all 8 golden sentences verbatim (see §6);
the P7 English example letter and its English parenthetical disclosure
verbatim; the VOL.3 teaser English paragraph verbatim; image credits.

CHANGED (explanation layer only, fully German):
all gloss boxes, bridges, exercise instructions, section-head German halves,
box titles' German halves, furniture (badge, strapline, footers, page lines),
P8 answer notes (all German), P7 grammar points and follow-up bridges,
readers'-corner disclosure (German, §7), writing instruction German line.

## 4. Pairing furniture (W43 shipped forms win; three-way record)

Source of truth for furniture: the shipped W43 EN×DE SVGs in
`files/weekly-report-en-de/` (they override the generic README #20 rules
where they differ). Edition forms, all measured from the rendered SVGs:

- P1 badge (subtitle slot, y=372, 19.5pt bold olive #3e4c2a):
  `ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR
  DEUTSCHSPRACHIGE LESER`.
- P1 edition line: `ENGLISCHES WOCHENBLATT · VOL.2 · WAHLEN · FUSSBALL ·
  FILME` (W45 content; W43 line differed in topic words only).
- P1 strapline reused verbatim from W43: `WEEKLY IN ENGLISH · Jede Woche neu
  · Englisch, wie Amerika es liest`.
- Footer (English-form exception): `The Lucerna · ENGLISH WEEKLY VOL.2 ·
  Englischer Text · Deutsche Erklärungen`; page line `Seite N von 8`.
- Gloss prefix: `Anmerkung | ` (NOT the generic tables.json `HINWEIS · `).
- P8 separators: `— Seite N —`.
- Section heads bilingual EN · DE, e.g. `LIFE · Leben`, `CULTURE · Kultur`,
  `SPORT · Sport`, `YOUTH · Jugend`, `DEEP READ · Vertiefung`, `LANGUAGE IN
  HAND · Sprachwerkstatt`, `EXERCISES & ANSWERS · Übungen & Antworten`.
- P1 dark band: line 1 `AMERICA VOTES ON TUESDAY — AND THE CLOCKS FELL BACK
  !` / `DIENSTAG WAHLTAG · SONNTAG UMGESTELLT` (round 4, see §9); line 2
  `Election Day is Tuesday, November 3. On Sunday, November 1, America turned
  its clocks back one hour.` / `Dienstag, 3. November, Wahltag · Siehe Seite
  6`.
- Type-token map (registry only, core type → German token):
  sentence-completion→Satzergänzung, multiple-choice→Multiple Choice,
  pattern-transformation→Umformung, word-matching→Zuordnung,
  follow-up-practice→Anwendungsübung, error-correction→Fehlerkorrektur,
  cloze→Lückentext, reading-comprehension→Leseverstehen,
  translation→Übersetzung, dialogue-completion→Dialogergänzung,
  writing→Schreiben, chart-reading→Diagrammlesen. Instruction map:
  fill-in→Ergänze, rewrite→Schreibe um, match→Ordne zu, clinic
  error-correction→Korrigiere.
  Ordering trap (fixed in transform.py): shared type/instruction maps run
  LAST, after per-page maps, because several heads/titles contain a type
  word and replacing types first corrupts those heads' match strings.
- P8 rendering follows W43 EN×DE, not the core: print ALL notes (core
  prints conditionally), 13.5pt (core 15.5pt), half-width parens ` (note)`
  (core full-width), separator 16pt/1.26 (core 17pt/1.28), keys-flow bottom
  2530 (core 2545). German notes are longer, so this is required for fit.
  P8 keys flow ends 2274/2530.

## 5. P8 gates (all measured on the final files)

- `tools/p8.py compare` (explicit paths): core 78 noted → edition 150 noted;
  status EXTRA_ONLY, missing=[], extra_count=72, keydiff=[137, 138, 139, 140,
  150]. The 72 extras are the print-all-notes consequence (adjudicated
  acceptance): the edition printed-note set is a superset of the core's,
  not a subset. No bracket-style artifact: all 5 keydiffs differ in language
  content, not in parenthesis style.
- Keydiff adjudication (printed keys, byte-for-byte):
  - 137 EN→DE, body unchanged `Translate: « Patience is part of the system,
    not a failure of it. »`, key `Geduld ist Teil des Systems, nicht ein
    Versagen des Systems.`
  - 138 DE→EN, body `Übersetze: Dienstag, der 3. November, ist Wahltag in
    den Vereinigten Staaten.`, key `Tuesday, November 3, is Election Day in
    the United States.`
  - 139 DE→EN, body `Übersetze: An diesem Sonntag spielt die NFL in
    Madrid.`, key `On Sunday, the NFL plays in Madrid.`
  - 140 EN→DE, body unchanged `Translate: « Not every place changes. »`,
    key `Nicht jeder Ort stellt die Uhren zurück.`
  - 150 writing registry key → `Offene Aufgabe — Stichpunkte im
    Schreibkasten; Mustertext im Kasten auf Seite 8` / note `Bewertung nach
    Stichpunkten` (W43 form).
- Registry comparison core vs edition: page and level identical for all 150
  exercises; keys differ ONLY at 137/138/139/140/150. P8 notes are all
  German. P8 printed-note set: superset (EXTRA_ONLY accepted).
- P8 D head uses the W43 form `D · SENTENCES · Sätze formen`.

## 6. P7 gates (all measured from the rendered P7 SVG)

- Structure (measured from core, not copied from other families): top 4
  columns A2 (FALLING BACK + GOING TO + EXAMPLE) / B1 (COMPARATIVES + PAST
  SIMPLE + EXAMPLE) / B2 (HEADLINE PRESENT + WHETHER + EXAMPLE) / TOOLBOX (3
  pocket sentences + bridge); middle PHRASES OF THE WEEK (8 sentences +
  grammar point + follow-up exercise each, numbered 100–107); bottom ERROR
  CLINIC (2 columns, 108–111) + READERS' CORNER box + NEXT WEEK teaser.
- Golden sentences, all 8 found verbatim in the edition P7 SVG with core
  page labels and levels (2× each: article + P7):
  1. « Tuesday, November 3, is Election Day in the United States. » (p.1,
     A2); 2. « The hour from 1 to 2 happened twice. » (p.2, A2);
  3. « Which film would you choose? » (p.3, B1);
  4. « Two games, two continents, one league — that is the modern NFL. »
     (p.4, B1); 5. « The results will still be there in the morning. »
     (p.5, B2); 6. « Patience is part of the system, not a failure of it. »
     (p.6, B2); 7. « Not every place changes. » (p.2, A2);
  8. « One Sunday is not enough — good thing the week has seven days. »
     (p.4, B1).
- P7 definition sentences verbatim; only gloss/explanation localized to
  German. Definition localization would be a blocking failure; none found.
- P7 levels in the phrases section: 100 A2, 101 A2, 102 B1, 103 B1, 104 B2,
  105 B2, 106 A2, 107 B1.

## 7. Readers' corner (coordinator ruling, as executed)

No reader, letter, name or quotation was invented. The core's existing
English elements are kept verbatim: the example-letter paragraph
(« On Sunday, I slept one hour more — and I still woke up late! » — M. L.,
a reader in Chicago) with its English parenthetical disclosure, and the
VOL.3 teaser English paragraph. The disclosure itself is written in German
and states the 3 facts (no real letters had arrived by press time; no best
VOL.1 writing to discuss; the example stays honestly labeled and real
letters are deferred to VOL.3) PLUS an explicit German invitation in the
imperative with a VOL.3 publication promise (the teaser/promise line does
not count as the invitation):
`Anmerkung der Redaktion | Bis Redaktionsschluss sind keine echten
Leserbriefe eingetroffen, und es gibt keinen besten VOL.1-Schreibtext zu
besprechen. Das Beispiel oben bleibt daher ehrlich gekennzeichnet stehen;
echte Briefe erscheinen ab VOL.3. Schicke uns deinen Brief und deinen Text
— wir drucken sie in VOL.3!`
Wrap-verified 4 lines at 20pt sans, width 848, inside the corner box (last
baseline ≈ box bottom − 18px). No new English disclosure sentence was
written for something the core does not have.

## 8. Gloss gate (rendered SVGs, boxes reassembled across wrapped lines)

Core gloss() strings split on `·`: 18 items — P2 3 / P3 4 / P4 4 / P5 3 /
P6 4. Edition `Anmerkung | …` boxes, same method: 18 items — P2 3 / P3 4 /
P4 4 / P5 3 / P6 4, item-by-item matched. P1 bridge (4 items) is separate
and is not a gloss() call.
Edition P2 box: `to fall back = (Uhren) zurückstellen · a costume = Kostüm,
Verkleidung · trick or treat = Süßes oder Saures.` P3: `to open = (Film)
anlaufen, starten · a monster = Monster · a catchphrase = Spruch · a series
= Serie.` P4: `a fixture = Spiel (im Spielplan) · a title = Titel · to
defend = (Titel) verteidigen · a fan = Fan.` P5: `a map = (Wahl)karte · too
close to call = zu knapp, um es zu entscheiden · a second screen = zweiter
Bildschirm (Handy).` P6: `to register = sich (als Wähler) registrieren · a
governor = Gouverneur · to shape laws = Gesetze prägen · patience = Geduld.`

## 9. Fix rounds (all edits in transform.py; each round re-copied the core
## build fresh, then re-ran transform + run + render)

- R1 (280 replacements): zero residual CJK/full-width parens in build
  sources. Build warnings: P1-headline FLOW OVERFLOW (ended 1921, bottom
  1828); P2-ex FLOW OVERFLOW (match_set spilled to 2948); HEAD TOO WIDE P6
  `READ THE CHART · Diagramm lesen` (446.7px > 434) and P8 `D · SENTENCES ·
  Sätze bilden und umformen` (555.2px > 434). P8 battery ended 1513 vs
  bottom 1485 (+28).
- R2: P1 numbers-box line 1 parenthetical shortened to `(alle 435 Sitze neu
  zu wählen)` (4→3 wrapped lines); P2 bridges shortened to 1 line each
  (`Ergänze die Sätze nach der Uhrzeit.`, `Schreibe mit be going to um.`)
  plus W43 P2 spacing tightening (4 head gaps 13→8, 3 bridge gaps 9→5, 13
  exercise gaps 11→9, match_set gap 14→6); P6 head → `READ THE CHART ·
  Diagramm` (375.7px); P8 battery B/C/D loop gaps 11→8 (−51px); P8 D head →
  `Sätze formen` (384.7px). Result: zero warnings; flows P1-headline
  1823/1828, P2-ex 2390/2562, P8-battery 1390/1485, P8-keys 2274/2530.
- R3 (pre-fix baseline run2-baseline.sha256): root cause of all round-2
  occlusion flags was German box/furniture titles drawn unwrapped past
  their box or the page; all fixes shorten titles only (no flow shifts).
  P1 searches subtitle → `Diese Woche gesucht · Google Trends USA` (382px ≤
  412); P1 word-of-week German line → `Mitte der Amtszeit: midterm =
  Zwischenwahl.` (1 wrapped line); P1 numbers box → `THE WEEK IN NUMBERS ·
  Zahlen` (375.9px); P3 home box → `AT HOME THIS WEEK · Zu Hause`
  (368.1px); P4 Sunday box → `SUNDAY, NOVEMBER 8 · Spiele` (353.0px);
  P5 TOO CLOSE box → `TOO CLOSE TO CALL · Zu knapp` (365.1px); P5 col3 box →
  `FIVE SENTENCES · Fünf Sätze` (341.3px); P6 ballot box → `A PRACTICE
  BALLOT · Stimmzettel` (395.6px). Result: zero build warnings, occlusion
  0 flags, NEW 0.
- R4 (pre-fix baseline run3-baseline.sha256): visual card review found the
  P1 dark-band line 1 left English line and German right line touching
  (`BACK !DIENSTAG`): PIL advance gap is only 4.9px and CairoSVG's bold
  metrics run slightly wider, so the eye sees a join that ink-box
  measurement calls clean. Lesson: for end-anchored band pairs, require a
  comfortable advance gap, not just a non-negative ink gap. Fix: right line
  → `DIENSTAG WAHLTAG · SONNTAG UMGESTELLT` (advance gap 64.8px; band line
  2 gap 106.5px, top-band gap 201.3px also verified). Only P1 SVG/card and
  the 2 PDFs changed R3→R4. Occlusion re-run on the final files: edition 0,
  core 0, NEW 0.

## 10. Geometry gates (final files)

- Freeze: core baseline 8/8 byte-identical on 2026-10-27 and re-verified
  after the build (all 8 core SVG sha256 match the pre-build hashes in
  §11). Core untouched.
- Freeze diff core→edition (freeze-diff-r4.json): added CJK = 0 on all
  pages; edition CJK = 0; per page added/removed strings — P1 +28/−26 (core
  CJK 183→0), P2 +27/−26 (197→0), P3 +17/−17 (119→0), P4 +17/−16 (139→0),
  P5 +20/−17 (134→0), P6 +19/−16 (136→0), P7 +44/−32 (347→0), P8 +145/−104
  (776→0). Adjudication of every removed string containing English: all
  are (a) explanation-layer strings carrying CJK (gloss/answer notes citing
  an English word, Chinese instruction/bridge strings embedding English
  terms), (b) the W43 furniture strapline replacing the core's strapline
  (`THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA` — furniture,
  not body text), (c) re-wrap fragments of preserved content (P1 numbers-box
  line fragment, P8 answers-flow fragments of keys that the registry proves
  are all present), or (d) punctuation fragments (`6).`, `。`). NO frozen
  English body text was removed.
- Occlusion audit (selftest passes, 6 planted classes fire): edition 0
  flags, core 0 flags, NEW vs core 0 — files occlusion-r4.json (edition) and
  occlusion-new-r4.json (vs core). Round-2 edition flags (11) were all
  cleared by round 3; round 4 re-verified clean.
- Same-baseline text-node collision scan (decoded text, PIL metrics): 8/8
  pages clean, including the P1 top band (VOL. 2 / strapline / date) and
  furniture bands. Note the R4 lesson: this scan alone cannot catch the
  band-line near-touch; the visual check caught it.
- Right-edge scan (ADVANCE widths, all 8 pages): 0 texts past the inner
  frame (1910).
- Frame-line pressure scan (ink vs outer frame 28..1922 × 28..2672): 0 texts
  outside the outer frame on all 8 pages.
- Chart-label coverage, baseline-anchored ink method (PIL getmetrics,
  anchor ls, later opaque rects): max coverage 0.0% on all 8 pages, under
  the <30% threshold. Note: the core P6 chart is flow text lines (`No lines
  : 38%` etc.), not drawn bars with rect labels, so this check covers the
  P1 searches bars and every page's text-vs-later-rect relationship; the P6
  chart lines have no later rects over them at all.
- Edition-SVG scans: CJK = 0, bridge-word count = 0, full-width parens = 0
  on all 8 SVGs. (This KIT and ABSTRACT.txt likewise contain no CJK and no
  bridge-word.)
- Visual check: ALL 8 cards viewed (p1-front, p2-life, p3-culture, p4-sport,
  p5-jeunesse, p6-politique, p7-langue, p8-exercices) plus a full-resolution
  crop of the P1 dark band after round 4. No remaining defect.
- Inherited core rendering (NOT a fan-out defect): the P6 practice-ballot
  ☐ checkboxes render as missing-glyph boxes in both the core card and the
  edition card (same frozen string, same font pipeline). Left as-is; fixing
  it would mean changing frozen English body text.

## 11. Reproduction + final verification

- run.py interpreter: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0,
  cairosvg 2.9.1. render.py interpreter: same `tools/venv/bin/python` —
  Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1. System `python3` is also
  3.12.3 but PIL 10.2.0 and has NO cairosvg — never use it for run.py or
  render.py. Build recipe: fresh copy of the core build tree → apply
  transform.py → run.py (single process) → render.py (CairoSVG PNG @1950 +
  print PDF + web PDF JPEG q85 @1400).
- Core SVG sha256 (pre-build and post-build, identical):
  p1 c7e7d019de01e662faa35f9f1874829ae3fc0300e5d680f43404e6eab01b4c50,
  p2 07f5df7e8e7ea0768244e6c4ab4b7c1be04682e3309e34bd3c1229726590a293,
  p3 d9f7cc374fe1229ccada556a2e1d330e84fac3f4aeaa443400f3ba131dfce580,
  p4 3b8be5175094bcb71de860321ef00187101b5282d0d5ca76a88aca478b1f0006,
  p5 73486e2f216e1f3bc9f2ddabccdd74e8fb15560250ff1ec8729c339c3c5f6f3e,
  p6 3e2187b37acb2883c0aaef95f8e1bca21ec36e4327d4b5e69b8638e791152a79,
  p7 5a2684096010839c3b7c86be1b5fe45b730588c5546b3827b21b7e7080105083,
  p8 4de34a135cc831bfbbf5ec285be29d4758424dc16f37f0f9ab184d8fe18c8a9b.
- Final edition PDF sha256 (also recorded in run4-baseline.sha256):
  print 17,295,556 bytes,
  sha256 0605300932508500a7fbd13c4e506fd1b88c9ea4b86620c1e568224bdecb2d82;
  web 4,027,862 bytes,
  sha256 c0edc0c215f16aef316bc65ac2e245ddc9eece7ac614d2b4e0c5b9ddfb63f4c5.
- Honest notes: P1-headline flow ends 1823/1828 (5px slack — tight but
  clear of the row-B rule at 1844); P7-B1 column ends 1129/1150 (21px slack
  — tightest column on P7); P1 band line 1 needed a visual catch that
  measurement missed (see R4); the P6 ☐ tofu boxes are inherited from the
  core (see §10).
- W43 deviation list (places this edition could NOT copy W43 verbatim):
  W45-specific content furniture (edition line topic words, dark-band
  lines, teaser dates, box contents); German box-title shortenings forced
  by fit (P1 `Zahlen` / P3 `Zu Hause` / P4 `Spiele` / P5 `Zu knapp` /
  `Fünf Sätze` / P6 `Stimmzettel` / P6 `Diagramm` instead of `Diagramm
  lesen`); P2 one-line bridges (W43 precedent, W45 wording); P1 band line
  1 `SONNTAG UMGESTELLT` (round-4 shortening); W45-specific disclosure
  text (VOL.3 promise). Everything else follows the W43 shipped forms
  verbatim (badge, footer, gloss prefix, P8 separators, P8 rendering
  parameters, D head form, writing-key form).
