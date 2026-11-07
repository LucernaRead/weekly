# WEEKLY-KIT — La Lucerna · W45 IT×DE (VOL.2)

Issue week: **Mon 2 – Sun 8 November 2026**. Issue dated **Mon 2 November 2026**.
Edition: **Italian text × German explanations** (target IT, native DE).
Status: **builder-complete, NOT finalized — awaiting independent proofread.**
No Discord post, no card/PDF dump into main chat, no cron, no weekly-git
touch, no edit to the core or W43 directories — this build only.

## 1. Spec

- 8 pages, 1950×2700, warm ivory paper, dark olive-green accents,
  blackletter masthead **La Lucerna** (core's masthead; target is Italian).
- Only the explanation layer was rewritten, directly into German for
  German-native readers. All Italian body text is frozen, word for word.
- No invented reader letters, names, or quotations: the P7 readers' box
  keeps the core's Italian example letter, labelled as an editors' example
  (see §5).
- The explanation layer contains no Chinese characters at all in the
  rendered edition (SVG CJK = 0 on all 8 pages, see §2); the layer is
  German notes (prefix `HINWEIS · `).
- 150 exercises, continuously numbered 1–150; levels A2 47 · B1 70 ·
  B2 33 (identical to the core). Per page: P1 10 · P2 18 · P3 18 · P4 18 ·
  P5 18 · P6 18 · P7 12 · P8 38 (identical to the core).
- By type (registry, unchanged from the core): the registry type tokens
  were left byte-identical (they are never printed), so the registry
  field diff is n / page / level / type identical for all 150 items.
- Writing model text (§H): 81 words, Italian, byte-identical to the core
  (see §7).

## 2. Freeze check (tools/freeze.py)

- Baseline first, before any edit: `freeze.py baseline` on the W45 IT core
  build reproduced **8/8 SVGs byte-identical**, and the shipped core SVGs
  re-hashed unchanged afterwards. Core hashes re-verified at the end of
  this build, still identical (p1 81051bbb…, p2 d42ce9ae…, p3 9e45586d…,
  p4 62f75269…, p5 c907b869…, p6 5545f8dd…, p7 9fc999f4…, p8 3b87e54f…).
- Final diff (core vs this edition, R2 SVGs): per page added/removed
  text-node strings p1 +28/−26, p2 +35/−29, p3 +32/−31, p4 +29/−25,
  p5 +44/−35, p6 +31/−24, p7 +44/−41, p8 +171/−166; **added CJK = 0** on
  every page (edition CJK 0, core 193/179/169/145/215/149/319/1034).
- Removed strings containing no Chinese characters, adjudicated:
  - p1–p5: **none** — every removed string carries explanation-layer
    Chinese; no Italian body string was removed.
  - p6: 1 wrap fragment (`bollettino · modello`) — the words are present
    in the edition, re-wrapped across different line breaks.
  - p7: 1 wrap fragment (`è probabile che / è possibile che / bisogna`)
    — same re-wrap cause.
  - p8: 7 lines differing only in punctuation form (full-width Chinese
    colon `：` → ASCII `:` and full-width parens `（）` → half-width
    `()` in the German notes, e.g. `103. nevica — nevicare：nevica` →
    `103. nevica — nevicare: nevica`); content identical.
- Images byte-identical per page (same base64 assets as the core);
  credit lines identical (Italian).

## 3. Furniture — three-way check (this edition / W43 shipped IT×DE / README)

W43 shipped IT×DE SVG wins verbatim wherever it speaks; the IT-family
case in README §20 applies (IT cores have no free subtitle slot: their
y=372 is frozen body strapline → badge is INSERTED, not slot-replaced).
Measured from the shipped W43 SVG, copied exactly:

- P1 badge element, byte-identical to W43 shipped (string, slot, size):
  `<text x="975" y="574" font-family="Noto Sans CJK SC" font-size="22"
  font-weight="700" fill="#a4553a" text-anchor="middle">ITALIENISCHER TEXT ·
  DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER</text>`
  (inserted y=574, 22pt, bold, BRICK #a4553a, centred; sits between the
  dark band bottom 542 and the headline head 606).
- Masthead: core's **La Lucerna** (target-language article; Italian).
- Footer, every page: `La Lucerna · ITALIENISCHE WOCHENZEITUNG VOL.2 ·
  TEXT AUF ITALIENISCH · ERKLÄRUNGEN AUF DEUTSCH` + `Seite N von 8`
  (verified present on all 8 SVGs; VOL.2 follows the W45 core — W43 said
  VOL.1; footer advance width 1038.9 px, same as W43's measure).
- Gloss prefix: `HINWEIS · ` (W43 shipped form).
- P8 separators: `— PAGINA N —` (W43 shipped form, kept from the core).
  DEVIATION NOTE: tables.json's generic DE `p8_separator` (`— SEITE N —`)
  was NOT used — the tasking brief rules that the W43 same-pair shipped
  SVG outranks the generic table, and W43 IT×DE ships PAGINA.
- P8 keys: dash style `N. key — note`, answer-generation code
  byte-identical to the core (IT is a dash-style family, README §8).
  Note brackets are half-width `()` in the German notes, as in W43 IT×DE
  (e.g. `tornare indietro = (die Uhr) zurückstellen` there); the core's
  full-width `（）` appears only inside Chinese notes, which are gone.
- Instruction words (W43 IT×DE list): Ausfüllen / Zuordnen /
  Sätze bilden / Übersetzen / Entscheiden / Schreiben.
- P1 top strip (W43 verbatim): `OGNI SETTIMANA IN ITALIANO ·
  ITALIENISCH, WIE ITALIEN ES LIEST`; subtitle line follows the W43
  pattern with W45 topics: `ITALIENISCH · VOL.2 · IL PRIMO FREDDO ·
  IL PANETTONE · LA SERIE A`.
- Bilingual section heads (Italian head + German second half)
  throughout, e.g. `LA NOTIZIA · DIE TITELSTORY`,
  `ESERCIZI · ÜBUNGEN ZU SEITE n`, `RISPOSTE · LÖSUNGEN`,
  `FRASI DELLA SETTIMANA · SÄTZE DER WOCHE (wörtlich aus dieser Ausgabe)`,
  `LA PROSSIMA SETTIMANA · NÄCHSTE WOCHE (VOL.3)`.
- No furniture string was generalised to fit README §20, and no frozen
  Italian line was moved or deleted to accommodate a badge: the badge
  insertion displaces nothing (band bottom 542 → badge 574 → head 606).

## 4. P7 word box — definition frozen (hard gate)

- Italian definition sentence, byte-identical to the core (verified on
  the whitespace-normalised rendered text):
  `« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere
  se piace. Questa settimana vive a pagina 3, alla finale del Panettone.`
- Only the gloss note below it was localised to German:
  `assaggio = Kostprobe. Seite 3: gratis kosten beim Panettone-Finale.`
  (2 lines, same as the core's Chinese note — col3 geometry unchanged.)
- The same freeze rule was applied to every other P7 element: all
  Italian clinic sentences, corrections, and the 8 quotes are
  byte-identical to the core; only German notes changed.

## 5. Readers' corner — no fabrication (hard gate)

Page print (P7, LETTERE DEI LETTORI box), Italian original first:

- Italian letter text, byte-identical to the core, including its own
  Italian example label: `«Ciao! Sono Li, studio italiano a Pechino.
  Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone —
  almeno in foto!» — Li (esempio della redazione)`
- German note below it (3 lines, same as the core's note):
  `Redaktionsbeispiel, keine Leserpost, kein bester Seite-8-Text.
  Schreiben Sie uns — die besten erscheinen in VOL.3!`
- Three-fact disclosure, mapped:
  1. No real letters — `keine Leserpost`, and the letter shown is
     labelled `Redaktionsbeispiel` / `(esempio della redazione)`.
  2. No best P8 writing — `kein bester Seite-8-Text`.
  3. Example + deferral to VOL.3 — `Redaktionsbeispiel` +
     `die besten erscheinen in VOL.3`.
- Explicit German public invitation (imperative + VOL.3 publication
  promise, inside the box, not the preview line):
  `Schreiben Sie uns — die besten erscheinen in VOL.3!`
- The VOL.3 preview band's Italian line (`le vostre lettere vere e i
  testi migliori della pagina 8`) is the Italian original of the
  deferral; it is NOT counted as the invitation (the invitation is the
  German box note above).
- No reader, letter, name, or quote was fabricated as real. The W43
  promise of real letters + best P8 writing is honoured only as this
  invitation + VOL.3 preview, exactly as in the core.

## 6. Gloss distribution (measured from the core, verified in render)

Core gloss() strings split on `·` (README §21 method — split on the
bare separator, never on the spaced form):

- P2: 6 — il cappotto · la sciarpa · i guanti · a strati ·
  il termosifone · il crisantemo
- P3: 5 — il panettone · il torrone · l'assaggio · la bancarella ·
  il cantiere
- P4: 4 — la giornata · la presentazione · gli spalti · la sera
- P5: 4 — il cosplay · gratuito · il documentario · lo schermo
- P6: 5 — la probabilità · la media · il modello · il bollettino ·
  aggiornare
- Total: **24 items, 1:1 with the core** (distribution NOT copied from
  any other family). Every headword was verified present in the rendered
  DE SVGs. The P1 bridge word list (separate from gloss()) carries 4
  items, also 1:1.
- P7 golden sentences: 8 quotes, each occurring exactly 2× in the
  whitespace-normalised joined SVG text (once in its article, once on
  P7), same as the core; the 8 P7 quote nodes are byte-identical to the
  core's, each paired with the same `(Pagina N)` tag
  (1, 1, 2, 2, 3, 4, 5, 6).

## 7. P8 gate (tools/p8.py)

- `p8.py compare` (explicit core/edition P8 paths, total 150):
  **CLEAN, 150 noted = 150 noted, missing=[] extra=[] uncertain=[]**,
  keydiff = [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 102, 137, 138, 139].
- Keydiff adjudication, item by item (printed P8 lines, byte-compared):
  - Paren-branch pseudo-diffs (12): 6, 13, 14, 15, 16, 20, 38, 58, 71,
    74, 77, 102. The core's trailing full-width paren group makes
    detect_note take the paren branch, so its extracted key includes
    the note head; the German half-width parens do the same. Printed
    answer keys are byte-identical (e.g. `6. previsioni`,
    `13. guanti`, `58. più bella`); only the note is translated and
    the brackets switch full-width → half-width (the W43 IT×DE family
    form). Not key changes.
  - True re-aims (3, legal per the W43 precedent): 137, 138, 139 are
    section-E translation items re-aimed Italian → German, exactly as
    W43 IT×DE re-aimed its section-E items: core keys were Chinese
    sentences, edition keys are their German translations
    (`Am Montag kommt die erste Kälte.` /
    `Das Publikum darf gratis kosten.` /
    `Am Sonntagabend spielt Fiorentina gegen Juventus.`); item 140
    keeps its Italian key with a German body, mirroring W43. The
    wrapped-note join artifact is noted: wrapped answer notes rejoin
    with a space (e.g. 138 reads `assaggiare gratis = gratis kosten`,
    139 reads `si gioca = es wird gespielt`), not concatenated.
- P8 notes are pure German (no Chinese characters on P8; SVG CJK = 0).
- P8 answer-note set equals the core's set (EXTRA_ONLY would have been
  acceptable; the result is the stronger CLEAN).

## 8. Geometry gates (all measured, R2 = final render)

- `occlusion_audit.py` (selftest OK, all 6 planted classes fired):
  edition **0 flags**, core **0 flags**, NEW **0 flags**, exit 0.
  R0 had 6 NEW flags, all real German-note overflows, all fixed in
  fix rounds 1–2 (see §10); R2 re-audit is clean.
- Right-edge scan (ADVANCE method: PIL advance widths per anchor):
  **0 flags** on all 8 pages against the [40, 1910] frame band
  (outer frame at 28/40). Footer advance: left string ends 1103.9,
  right page line starts 1767.9 (664 px clear, all pages).
- Same-baseline collision scan (furniture bands, incl. P1 top band
  y=92 and every footer y=2624): **0 overlaps**. P1 top band gaps:
  left ends 392.3 → centre starts 643.7 → centre ends 1306.3 → date
  starts 1450.6.
- P6 chart-label coverage, baseline-anchored ink method (PIL getmetrics,
  anchor `ls`, later-drawn rects vs label ink): **max 0%** on all chart
  labels (Torino/Milano/Bologna/Roma/Napoli + value labels); threshold
  <30% passes with full margin. Bars sit clear of labels and values.
- Flow ends (final build log): P1-headline 1497 (bottom 1828),
  P2 col3 1025.0, P3 col3 1281.25, P4 col3 904.0, P5 col3 1285.75,
  P6 col3 1096.5, P6-ex 2569 (bottom 2580, same as core),
  P7 col3 **1673.0** (13 px clear of the FRASI rule at 1686, same as
  the core), P8-ex 965 (bottom 1332), P8-keys 2529 (bottom 2552,
  23 px clear of the footer zone).
- Build warnings final: FLOW OVERFLOW 0, HEAD TOO WIDE 0.
- Visual check: all 8 cards in cards/ inspected page by page
  (overflow, overlap, footer clearance, frost drawing, P4 fixture
  table, P6 chart + caption, P7 col3 vs FRASI rule, P8 answers bottom
  vs footer). No defects seen.

## 9. Independent counts (from the rendered SVGs, not the registry)

- Exercise numbers extracted from P1–P7 SVGs + the P8 exercise region
  (chip level text followed by `N.` / `N–M.` nodes, ranges expanded):
  **150 items, set exactly 1–150, no missing, no duplicates**.
- Levels from the same extraction: **A2 47 · B1 70 · B2 33**;
  per page 10/18/18/18/18/18/12/38 — identical to the core and to §1.
- Model text: extracted from both P8 SVGs, normalised — DE == core
  byte-identical; 83 words including the `Testo modello:` label =
  **81 model words**, matching the core.
- P8 writing item prints `150. ✓ Mustertext in Abschnitt H auf dieser
  Seite (81 Wörter)`.

## 10. Build / reproduce

- Build dir: hidden_files/weekly-report-w45-it-de-build/ (bslib4.py,
  svglib.py, run.py, render.py, assets/ copied from the W45 IT core
  build; content12/34/56/7/8.py transformed by transform.py;
  transform.py + per-round sha256 baselines + raw tool outputs kept).
- Pipeline (core pipeline reused as-is):
  - Transform (from a fresh core-build copy): run transform.py once —
    it performs the base replacements, then FIX ROUND 1, then FIX
    ROUND 2 in order, with count assertions; final audit asserts no
    Chinese characters remain outside the registry type tokens
    (完成句子/单选/完形单选/词汇配对/句型转换/判断对错/造句/翻译/写作),
    which are registry-only and never printed (W43 IT×DE precedent).
  - Build (ONE process only — shared-registry rule): `cd
    hidden_files/weekly-report-w45-it-de-build &&
    ../../tools/venv/bin/python run.py`
  - Render: `../../tools/venv/bin/python render.py` (writes svg/ +
    cards/ + both PDFs into files/weekly-report-w45-it-de/).
- Interpreters (recorded separately, as required):
  - run.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0.
  - render.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0,
    cairosvg 2.9.1, pypdf 6.21.2. System python3 has no cairosvg and
    must not be used for render.py.
- Reproducibility note: run.py and render.py were always run in the
  single-driver-process form; no content module was ever imported or
  run standalone, and nothing was ever executed inside the core build
  directory (the core hashes in §2 prove it).
- Fix rounds (each preceded by a full pre-fix sha256 baseline of all
  SVG/card/PDF outputs, kept in the build dir):
  - R0 → R1 (sha256-r0.txt): P1 headline flow overflowed (German bridge
    gloss 4 lines vs core 3 pushed the cifre box into col 2, exercises
    5–6 clamped) and P8 answer flow overflowed the footer zone by ~5
    key lines (13 German notes wrapped to 2 lines). Fixes, all wording
    only, all synced into transform.py FIX ROUND 1: bridge back to 3
    lines, cifre item 4 back to 2 lines, 9 P8 notes shortened to 1 line
    each (keys 44/134, 138, 139 deliberately left 2-line; flow then
    fits). R1: FLOW OVERFLOW 0, P1-headline 1497, P8-keys 2529.
  - R1 → R2 (sha256-r1.txt): occlusion audit reported 6 NEW flags, all
    real: P1 settimana footnote ran off the page as one 662 px line;
    P1 parola note wrapped to 2 lines under the row-B rule at 1864;
    P1 settimana subtitle crossed its box border; P2 frase box title
    crossed its box border; P7 parola box title crossed its box border
    by 5.5 px (plus the footnote's box-border flag). Fixes, all synced
    into transform.py FIX ROUND 2: footnote split into two short lines
    inside its box, parola note to 1 line, subtitle shortened, frase
    title to `MERKE`, parola title dropping `DAS`. R1→R2 changed
    exactly p1/p2/p7 SVGs + their cards + both PDFs (verified by hash
    diff); R2: occlusion 0/0/0, all other gates re-run green.
- ABSTRACT.txt: German single line, no ASCII double quotes, naming the
  week's real topics (erste Kälte, Allerseelen 2. November,
  Panettone-Weltmeisterschaft Mailand 7.–8. November, Torrone-Fest
  Cremona, Serie A 11. Spieltag) + learner search phrases
  (Italienisch lesen und lernen, mit deutschen Erklärungen) + masthead,
  target language name, A2–B2, 150 exercises.

## 11. W43 deviations (this edition vs shipped W43 IT×DE)

- VOL.2 throughout (core VOL changed since W43); badge string, slot,
  size, footer template, page line, gloss prefix, P8 separator
  (PAGINA), dash answer style, and instruction-word list are otherwise
  identical to W43 IT×DE.
- Counts follow the W45 core, not W43: levels A2 47/B1 70/B2 33
  (W43: A2 46/B1 71/B2 33); model text 81 words (W43: 90 words).
- New wording-only tightenings with no W43 counterpart (all forced by
  German length vs the W45 core's tighter boxes): P1 bridge gloss
  drops the articles before versante/previsione; P1 settimana footnote
  split into two lines; P1 parola note to one line; P2 frase box title
  `MERKE`; P7 parola box title without `DAS`.
- P8 note-bracket form: half-width `()` (W43 IT×DE form), not the
  core's full-width `（）` (which only ever wrapped Chinese notes).

## 12. Deliverables

- files/weekly-report-w45-it-de/ (svg/ 8 SVGs, cards/ 8 PNGs,
  La-Lucerna-VOL2-DE.pdf, La-Lucerna-VOL2-DE-web.pdf, WEEKLY-KIT.md,
  ABSTRACT.txt).
- Print PDF: La-Lucerna-VOL2-DE.pdf — 7,174,780 bytes, sha256
  a9f74664ee9952487fc79345ba550e6292a3c725276222fe1aaf0887ac4775da,
  8 pages, mediabox identical to the core's print PDF (0/0/1462.5/
  2025), same embedded image dimensions (P3 1280×862). Observation
  (not a defect): it is smaller than the core's print PDF (21,037,777
  bytes) despite identical page geometry and image dimensions; the
  web PDF below is the size-constrained deliverable and both PDFs
  render the same 8 pages (verified: footer + badge text extractable
  from print PDF p1).
- Web PDF: La-Lucerna-VOL2-DE-web.pdf — 3,643,700 bytes, sha256
  aa4b340ecabf85f50ba92d8b48f30b02a6ef5aae0ad6dfd3f04cac2dcf8facaa,
  8 pages, under the 10 MB Discord ceiling.
- SVG sha256 (final R2): p1 e01b89b8ab6903fabeabddaed6276c9d4b65d4117930b40b01df33fa59554c19,
  p2 a07c5cc17c1ee33b6004d1f86570dec40df3dcbd89e11b4ab77cb021da2b605a,
  p3 724d29c0260b291348d3053d35605da922e8a1f069ec1d044fce1cadab15abc8,
  p4 26cfad2f9167147401e2808db6be2e98e05475d08a4100bfe36966ac77665a69,
  p5 d3d2351870a991e28a977ea038760098bef3bd917cd431705e39395b9554b8f7,
  p6 11deb4ab8c22e6240238cd6cff51dd1633467721a8ac6e2454f6b8936599ae62,
  p7 2a78df7200dfb4a6b791d75ce386ae906660a8f49cac18b2f8f8e405c8f03ff6,
  p8 e174a8a5d9e7e730e11f9ffb6360de7c5ce8d0d7d47295d6c16ae85c605407ec.
- Card sha256 (final R2): p1 911de7b76767998c2ac90d776988a92831116bb9c509fac713c8a0e7a278e3fe,
  p2 dc030f59ae639ffa447f9f4992ea2513c7cf6030aa0e36a45168198422feeec6,
  p3 302e271f1b0fc24903c253e612b65a57d592b3ef33227082660b6106ddb24b6d,
  p4 9b282b3e491b6b8fac69df6fd7178f426f8ca340a1d1fd4c77f811c5795d3d07,
  p5 535039e167e390c4d2e420992809034639da69da6d6d4a1319a96191a39ce126,
  p6 b4085a96664c293342e17e4c3d1edd1de032b2176e01ce8f6f963d9533cd7998,
  p7 fd64d6b4a0a34ed13fadd6e046980eab197e191705b46809e9f2d994f51d716d,
  p8 0eda6b19d42edaf7ca80893d0e9f26cd437da4413ca64558cf1d9a461df98faf.

## 13. Delivery

- NOT pushed to git, NOT posted to Discord, NO messages sent (per task).
  Delivery to the LucernaRead/weekly repo is the main line's job.
- NOT self-certified as finalized: a fresh full independent proof round
  is still required before delivery.
