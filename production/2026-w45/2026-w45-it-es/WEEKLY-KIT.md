# WEEKLY-KIT — La Lucerna · W45 IT×ES (VOL.2)

Issue week: **Mon 2 – Sun 8 November 2026**. Issue dated **Mon 2 November 2026**.
Edition: **Italian text × Spanish explanations** (target IT, native ES).
Status: **builder-complete, NOT finalized — awaiting independent proofread.**
No Discord post, no card/PDF dump into main chat, no cron, no weekly-git
touch, no edit to the core or W43 directories — this build only.

## 1. Spec

- 8 pages, 1950×2700, warm ivory paper, dark olive-green accents,
  blackletter masthead **La Lucerna** (core's masthead; target is Italian).
- Only the explanation layer was rewritten, directly into Spanish for
  Spanish-native readers. All Italian body text is frozen, word for word.
- No invented reader letters, names, or quotations: the P7 readers' box
  keeps the core's Italian example letter, labelled as an editors' example
  (see §5).
- The explanation layer contains no Chinese characters at all in the
  rendered edition (SVG CJK = 0 on all 8 pages, see §2); the layer is
  Spanish notes (prefix `Nota — `).
- 150 exercises, continuously numbered 1–150; levels A2 47 · B1 70 ·
  B2 33 (identical to the core). Per page: P1 10 · P2 18 · P3 18 · P4 18 ·
  P5 18 · P6 18 · P7 12 · P8 38 (identical to the core).
- By type (registry, unchanged from the core): the registry type tokens
  were left byte-identical (they are never printed), so the registry
  field diff is n / page / level / type identical for all 150 items.
- Writing model text (§H): 81 words, Italian, byte-identical to the core
  (see §9).
- The banned intermediary-layer term appears nowhere in the 8 SVGs or the delivered ABSTRACT.

## 2. Freeze check (tools/freeze.py)

- Baseline first, before any edit: `freeze.py baseline` on the W45 IT core
  build reproduced **8/8 SVGs byte-identical**, and the shipped core SVGs
  re-hashed unchanged afterwards. Core hashes re-verified at the end of
  this build, still identical (p1 81051bbb…, p2 d42ce9ae…, p3 9e45586d…,
  p4 62f75269…, p5 c907b869…, p6 5545f8dd…, p7 9fc999f4…, p8 3b87e54f…).
- Final diff (core vs this edition, R2 SVGs): per page added/removed
  text-node strings p1 +27/−27, p2 +34/−29, p3 +32/−31, p4 +28/−25,
  p5 +42/−35, p6 +28/−24, p7 +43/−41, p8 +168/−166; **added CJK = 0** on
  every page (edition CJK 0, core 193/179/169/145/215/149/319/1034).
- Removed strings containing no Chinese characters, adjudicated:
  - p1: 1 — the masthead strapline
    `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`,
    replaced in its slot by the pairing badge per the shipped W43 IT×ES
    precedent (the W43 core carried the identical strapline and its ES
    edition replaced it; see §3). No article body string was removed.
  - p6: 1 wrap fragment (`bollettino · modello`) — both words are present
    in the edition, re-wrapped across different line breaks.
  - p7: 1 wrap fragment (`è probabile che / è possibile che / bisogna`)
    — same re-wrap cause.
  - p8: 7 lines differing only in punctuation form (full-width Chinese
    colon `：` → ASCII `:` and full-width parens `（）` → half-width
    `()` in the Spanish notes, e.g. `17. metto — mettere：io → metto` →
    `17. metto — mettere: io → metto`); content identical.
- Images byte-identical per page (same base64 assets as the core:
  P3 tartufo 1, P5 castagne 1, other pages 0);
  credit lines identical (Italian).

## 3. Furniture — three-way check (this edition / W43 shipped IT×ES / README)

W43 shipped IT×ES SVG wins verbatim wherever it speaks, per the tasking
brief (W43 same-pair furniture outranks the README §20 generalisation).
Measured from the shipped W43 SVG, copied exactly (VOL updated 1 → 2):

- P1 badge element, byte-identical string to W43 shipped, in the W43
  shipped geometry (slot, size):
  `<text x="975" y="372" font-family="Noto Sans CJK SC" font-size="20"
  font-weight="700" fill="#a4553a" text-anchor="middle">TEXTOS EN ITALIANO ·
  EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES</text>`
  (replaces the masthead strapline slot at y=372, 20pt, bold, BRICK
  #a4553a, centred; measured advance 1077.3px, matching the W43 KIT's
  1077px. DEVIATION NOTE, stated openly: the W45 IT×DE/EN/FR siblings
  instead INSERT the badge at y=574, 22pt, keeping the strapline. This
  pair follows the W43 same-pair shipped instance, as the tasking brief
  rules; the strapline removal is the single adjudicated freeze-diff
  item in §2. If the independent proofreader rules the other way, the
  fix is mechanical: restore the strapline line and move the badge to
  y=574, 22pt.)
- P1 top strip, W43 verbatim: `OGNI SETTIMANA IN ITALIANO · CADA SEMANA ·
  EL ITALIANO QUE LEE ITALIA` (centre, 21pt); left `VOL. 2 · SECONDA
  EDIZIONE`, right `SETTIMANA DAL 2 ALL'8 NOVEMBRE 2026` (gaps
  198.6px / 91.5px, same-baseline scan clean).
- P1 edition line at y=330, 46pt serif bold: `SEMANARIO ITALIANO · VOL.2 ·
  IL PRIMO FREDDO · PANETTONE · SERIE A` (measured 1763.8px, inside the
  frame; the full form with `IL PANETTONE · LA SERIE A` measures
  1899.8px and would cross the frame, so the two articles were dropped
  from the topic list only).
- P1 dark-band right texts: `ESTA SEMANA LLEGA EL PRIMER FRÍO` /
  `La semana del primer frío · ver página 2`.
- Masthead: core's **La Lucerna** (target-language article; Italian).
- Footer, every page: `La Lucerna · SEMANARIO ITALIANO VOL.2 · TEXTO EN
  ITALIANO · EXPLICACIONES EN ESPAÑOL` + `Página N de 8`
  (verified present on all 8 SVGs; VOL.2 follows the W45 core — W43 said
  VOL.1; footer advance gap 792.1px, all pages).
- Gloss prefix: `Nota — ` (W43 shipped form).
- P8 separators: `— PAGINA N —` (W43 shipped form, kept from the core;
  the generic tables.json ES separator `— PÁGINA N —` was NOT used).
- P8 keys: dash style `N. key — note`, answer-generation code
  byte-identical to the core (IT is a dash-style family, README §8).
  Note brackets are half-width `()` in the Spanish notes, as in W43
  IT×ES; the core's full-width `（）` appears only inside Chinese
  notes, which are gone.
- Instruction words (W43 IT×ES list): Completa / Empareja /
  Forma la frase / Traduce / Verdadero o falso / Escribe.
- Bilingual section heads (Italian head + Spanish second half)
  throughout, e.g. `LA NOTIZIA · EL TITULAR`,
  `LA SETTIMANA IN CIFRE · EN CIFRAS`, `ADESSO TU · AHORA TÚ`,
  `IN QUESTO NUMERO · ÍNDICE`, `IN BREVE · EN BREVE`,
  `QUIZ LAMPO · QUIZ RELÁMPAGO`, `VITA · VIDA COTIDIANA`,
  `LA FRASE PER RICORDARE · LA CLAVE` (shortened from
  `LA FRASE PER RICORDARE · LA CLAVE` — see §10, fix round 1),
  `E TU? · ¿Y TÚ?`, `CULTURA · CULTURA`, `SPORT · DEPORTE`,
  `GIOVANI · JÓVENES`, `APPROFONDIMENTO · EN PROFUNDIDAD`,
  `LINGUA · LENGUA`, `ERRORI TIPICI · ERRORES TÍPICOS`,
  `LA PAROLA · PALABRA CLAVE`,
  `FRASI DELLA SETTIMANA · FRASES DE LA SEMANA (TEXTUALES, DE ESTE NÚMERO)`,
  `ESERCIZI · EJERCICIOS DE LA PÁGINA n`,
  `VALUTAZIONE E RISPOSTE · EJERCICIOS Y RESPUESTAS`,
  `RISPOSTE · RESPUESTAS — por página, busca el número del ejercicio`,
  `LA PROSSIMA SETTIMANA · LA PRÓXIMA SEMANA (VOL.3)`.
- No furniture string was generalised to fit README §20, and no frozen
  Italian body line was moved or deleted to accommodate a badge, other
  than the adjudicated strapline-slot replacement above.

## 4. P7 word box — definition frozen (hard gate)

- Italian definition sentence, byte-identical to the core (verified on
  the whitespace-normalised rendered text):
  `« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere
  se piace. Questa settimana vive a pagina 3, alla finale del Panettone.`
- Only the gloss note below it was localised to Spanish:
  `assaggio = degustación. Página 3: en la final del Panettone se prueba gratis.`
  (2 lines, same as the core's Chinese note; box bottom pad +6 for
  descender clearance — see §10, fix round 1.)
- The same freeze rule was applied to every other P7 element: all
  Italian clinic sentences, corrections, and the 8 quotes are
  byte-identical to the core; only Spanish notes changed.

## 5. Readers' corner — no fabrication (hard gate)

Page print (P7, LETTERE DEI LETTORI box), Italian original first:

- Italian letter text, byte-identical to the core, including its own
  Italian example label: `«Ciao! Sono Li, studio italiano a Pechino.
  Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone —
  almeno in foto!» — Li (esempio della redazione)`
- Spanish note below it (3 lines, same line count as the core's note):
  `Ejemplo de la redacción, no carta real; sin mejor texto de página 8.
  ¡Escríbenos! Las mejores salen en VOL.3.`
- Three-fact disclosure, mapped:
  1. No real letters — `no carta real`, and the letter shown is
     labelled `Ejemplo de la redacción` / `(esempio della redazione)`.
  2. No best P8 writing — `sin mejor texto de página 8`.
  3. Example + deferral to VOL.3 — `Ejemplo de la redacción` +
     `Las mejores salen en VOL.3`.
- Explicit Spanish public invitation (imperative + VOL.3 publication
  promise, inside the box, not the preview line):
  `¡Escríbenos! Las mejores salen en VOL.3.`
- The VOL.3 preview band's Italian line (`le vostre lettere vere e i
  testi migliori della pagina 8`) is the Italian original of the
  deferral; it is NOT counted as the invitation (the invitation is the
  Spanish box note above).
- Disclosure in both languages: the Italian original is the letter's
  own `(esempio della redazione)` label plus the preview band's Italian
  deferral line; the Spanish equivalent sentence is the box note above,
  which states all three facts explicitly.
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
  ES SVGs. The P1 bridge word list (separate from gloss()) carries 4
  items, also 1:1 (il primo freddo · versante adriatico · previsione ·
  assaggi).
- P7 golden sentences: 8 quotes, each occurring exactly 2× in the
  whitespace-normalised joined SVG text (content counted without the
  « » marks, which the article occurrences do not carry; once in its
  article, once on P7), same as the core; the 8 P7 quote nodes are
  byte-identical to the core's, each paired with the same `(Pagina N)`
  tag (1, 1, 2, 2, 3, 4, 5, 6) and its Spanish translation.

## 7. P8 gate (tools/p8.py)

- `p8.py compare` (explicit core/edition P8 paths, total 150):
  **CLEAN, 150 noted = 150 noted, missing=[] extra=[] uncertain=[]**,
  keydiff = [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 102, 137, 138, 139].
- Keydiff adjudication, item by item (printed P8 lines, byte-compared):
  - Paren-branch pseudo-diffs (12): 6, 13, 14, 15, 16, 20, 38, 58, 71,
    74, 77, 102. The core's trailing full-width paren group makes
    detect_note take the paren branch, so its extracted key includes
    the note head; the Spanish half-width parens do the same. Printed
    answer keys are byte-identical (e.g. `6. previsioni`,
    `13. guanti`, `58. più bella`); only the note is translated and
    the brackets switch full-width → half-width (the W43 IT×ES family
    form). Not key changes.
  - True re-aims (3, legal per the W43 precedent): 137, 138, 139 are
    section-E translation items re-aimed Italian → Spanish, exactly as
    W43 IT×ES re-aimed its section-E items: core keys were Chinese
    sentences, edition keys are their Spanish translations
    (`El lunes llega el primer frío.` /
    `El público puede probar gratis.` /
    `El domingo por la noche se juega Fiorentina–Juventus.`); item 140
    keeps its Italian key byte-identical
    (`Ogni previsione deve essere chiara.`) with a Spanish body
    (`Cada previsión debe ser clara. → ___`), mirroring W43. The
    wrapped-note join artifact is noted: wrapped answer notes rejoin
    with a space (e.g. 139 reads `si gioca = se juega`), not
    concatenated.
  - Item 150 (writing): printed as `150. ✓ El modelo está en la
    sección H (81 palabras)`; the tool does not list writing items in
    keydiff (same as the W45 IT×DE build).
- P8 notes are pure Spanish (no Chinese characters on P8; SVG CJK = 0).
- P8 answer-note set equals the core's set (EXTRA_ONLY would have been
  acceptable; the result is the stronger CLEAN).

## 8. Geometry gates (all measured, R2 = final render)

- `occlusion_audit.py` (selftest OK, all 6 planted classes fired):
  edition **0 flags**, core **0 flags**, NEW **0 flags**, exit 0.
  R0 had 17 NEW flags, R1 had 1 NEW flag, all real, all fixed in
  fix rounds 1–2 (see §10); R2 re-audit is clean.
- Right-edge scan (ADVANCE method: PIL advance widths per anchor):
  **0 flags** on all 8 pages against the [40, 1910] frame band
  (outer frame at 28/40). Footer advance: left string ends 970.5,
  right page line starts 1762.7 (792.1 px clear, all pages).
- Same-baseline collision scan (furniture bands, incl. P1 top band
  y=92 and every footer y=2624): **0 overlaps**. P1 top band gaps:
  left ends 392.3 → centre starts 590.9 → centre ends 1359.1 → date
  starts 1450.6.
- P6 chart-label coverage, baseline-anchored ink method (PIL getmetrics,
  anchor `ls`, later-drawn rects vs label ink): **max 0.0%** on all chart
  labels (Torino/Milano/Bologna/Roma/Napoli + value labels); threshold
  <30% passes with full margin. Bars sit clear of labels and values.
- Flow ends (final build log): P1-headline 1497 (bottom 1828),
  P2 col3 1054.0, P3 col3 1281.25, P4 col3 875.0, P5 col3 1314.75,
  P6 col3 1096.5, P6-ex 2569 (bottom 2580, same as core),
  P7 col3 **1679.0** (7 px clear of the FRASI rule at 1686),
  P8-ex 965 (bottom 1332), P8-keys 2499 (bottom 2552,
  53 px clear of the footer zone).
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
- Model text: extracted from both P8 SVGs, normalised — ES == core
  byte-identical; **81 model words**, matching the core.
- P8 writing item prints `150. ✓ El modelo está en la sección H
  (81 palabras)`.

## 10. Build / reproduce

- Build dir: hidden_files/weekly-report-w45-it-es-build/ (bslib4.py,
  svglib.py, run.py, render.py, assets/ copied from the W45 IT core
  build; content12/34/56/7/8.py transformed by transform.py;
  transform.py + per-round sha256 baselines + raw tool outputs kept).
- Pipeline (core pipeline reused as-is):
  - Transform (from a fresh core-build copy): run transform.py once —
    it performs the base replacements, then FIX ROUND 1, then FIX
    ROUND 2 in order, with count assertions. After each build, a
    post-build scan asserts no Chinese characters remain in the
    rendered SVGs outside the registry type tokens
    (完成句子/单选/完形单选/词汇配对/造句/句型转换/判断对错/翻译/写作),
    which are registry-only and never printed (W43 IT×ES precedent);
    final scan: SVG CJK = 0 on all 8 pages.
  - Build (ONE process only — shared-registry rule): `cd
    hidden_files/weekly-report-w45-it-es-build &&
    ../../tools/venv/bin/python run.py`
  - Render: `../../tools/venv/bin/python render.py` (writes svg/ +
    cards/ + both PDFs into files/weekly-report-w45-it-es/).
- Interpreters (recorded separately, as required):
  - run.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0.
  - render.py: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0,
    cairosvg 2.9.1, pypdf 6.21.2. System python3 has no cairosvg and
    must not be used for render.py.
- Reproducibility note: run.py and render.py were always run in the
  single-driver-process form; no content module was ever imported or
  run standalone, and nothing was ever executed inside the core build
  directory (the core hashes in §2 prove it). Each fix round was
  applied by re-copying the fresh core build and re-running the full
  transform.py (base + fix rounds in order), never by hand-editing the
  transformed files — so transform.py alone reproduces the final build.
- Fix rounds (each preceded by a full pre-fix sha256 baseline of all
  SVG/card/PDF outputs, kept in the build dir):
  - R0 → R1 (sha256-r0.txt): P1 headline flow overflowed (Spanish bridge
    gloss 4 lines vs core 3 pushed the cifre box into col 2, exercises
    5–6 clamped into row B) and P8 answer flow overflowed the footer
    zone by ~2 key lines (9 Spanish notes wrapped to 2 lines). Fixes,
    all wording only, all synced into transform.py FIX ROUND 1: bridge
    back to 3 lines (articles dropped before versante/previsione),
    cifre item 4 back to 2 lines, P2 box title shortened
    (`LA FRASE PER RICORDARE · LA CLAVE` → `FRASE PER RICORDARE ·
    LA CLAVE`, was crossing its box border by 14px), P7 parola box
    bottom pad +6 (last-line descender ink exceeded the border by
    0.5px), 8 P8 notes shortened to 1 line each (keys 44/45/56/58/133/
    134/135/138; key 139 deliberately left 2-line, like DE's 138/139).
    R1: FLOW OVERFLOW 0, P1-headline 1497, P8-keys 2499, occlusion
    1 NEW flag left.
  - R1 → R2 (sha256-r1-pre.txt): occlusion audit reported 1 NEW flag,
    real: P1 parola grey note wrapped to 2 lines and its second line
    (`otoño suave.`) was struck by the row-B rule at 1864. Fix, synced
    into transform.py FIX ROUND 2: note shortened to one measured line
    (`«il primo freddo»: el primer frío serio.`, 326.7px at 19pt).
    R1→R2 changed exactly p1 SVG + its card + both PDFs (verified by
    hash diff); R2: occlusion 0/0/0, all other gates re-run green.
- ABSTRACT.txt: Spanish single line, no ASCII double quotes, naming the
  week's real topics (primer frío, Día de Difuntos 2 de noviembre,
  Copa del Mundo del Panettone en Milán 7–8 de noviembre, Festa del
  Torrone en Cremona, Serie A 11.ª jornada) + learner search phrases
  (aprende italiano leyendo, con explicaciones en español) + masthead,
  target language name, A2–B2, 150 exercises.

## 11. W43 deviations (this edition vs shipped W43 IT×ES)

- VOL.2 throughout (core VOL changed since W43); badge string, slot,
  size, footer template, page line, gloss prefix, P8 separator
  (PAGINA), dash answer style, and instruction-word list are otherwise
  identical to W43 IT×ES.
- Counts follow the W45 core, not W43: levels A2 47/B1 70/B2 33
  (W43: A2 46/B1 71/B2 33); model text 81 words (W43: 90 words).
- Edition line at y=330 shortened (articles dropped before PANETTONE
  and SERIE A) because the full SEMANARIO form overflows the frame at
  46pt (1899.8px vs 1845px frame); W43's line fit at its own topics.
- New wording-only tightenings with no W43 counterpart (all forced by
  Spanish length vs the W45 core's tighter boxes): P1 bridge gloss
  drops the articles before versante/previsione; P1 cifre item 4 paren
  shortened; P1 parola grey note to one line; P2 box title without the
  leading `LA`; P7 parola box bottom pad +6; 8 P8 notes shortened to
  one line.
- P8 note-bracket form: half-width `()` (W43 IT×ES form), not the
  core's full-width `（）` (which only ever wrapped Chinese notes).
- Badge slot: this pair keeps the W43 shipped y=372/20pt slot
  replacement; the W45 DE/EN/FR siblings' y=574/22pt insertion is NOT
  followed here, per the tasking brief (see §3 deviation note).

## 12. Deliverables

- files/weekly-report-w45-it-es/ (svg/ 8 SVGs, cards/ 8 PNGs,
  La-Lucerna-VOL2-ES.pdf, La-Lucerna-VOL2-ES-web.pdf, WEEKLY-KIT.md,
  ABSTRACT.txt).
- Print PDF: La-Lucerna-VOL2-ES.pdf — 7,170,661 bytes, sha256
  66be437a4076c29ea4322cce60f5aecf4a2ab1384381ecf915e37651d7179e9e,
  8 pages, mediabox identical to the core's print PDF (0/0/1462.5/
  2025), same embedded image dimensions (P3 1280×862, P5 1280×960).
- Web PDF: La-Lucerna-VOL2-ES-web.pdf — 3,614,384 bytes, sha256
  a1e2a8a9dcf446d4ac4ce3c68578322f76a6c3fae38255b2f908059458495e53,
  8 pages, under the 10 MB Discord ceiling.
- SVG sha256 (final R2): p1 56573951f9bee3d2ba514a9f2c623b5ef4f428ab15b456f238c2fd1551aeb5c4,
  p2 657de6fca92a1212003c879d54e98dd45f08bc94c7852bdbdbba981ae4b4015f,
  p3 a1a9d45c38dbe3ec113480d65c82ec4cb57fe0fde91bf2ecff54757bf6e02a3e,
  p4 8c7f80126698c11bb048acfc326a039bab663c470f82bbf9a3ed3a331fc9a010,
  p5 a70a33780587a3e9a3d15d38c6dfff23127d6cec5efa26943cf6c60d3005e7d5,
  p6 0b7dadbe006a558b435f537e0c366faf1affea99e9bb9518260ead8cd1036945,
  p7 727ae8d9939af3a962425472721761bd776897e522e93da1b2d9201785c7d490,
  p8 5d8f423facd477070f7668e1969d46b18f26fb22dc7b5b1c1db24e99535d0f94.
- Card sha256 (final R2): p1 c80e0a5976677162a598dc7c154384be40a06d58b827c57f6bae3480ebc864c8,
  p2 aa937b3742640403a05121a78aed168735802e83447b36409ba85de292e5447,
  p3 d462d0ac4e30853306ab46e3797b4d1a8f4d489b38805478d4c69fe60c8f7133,
  p4 fa41f4328a3bbfd9f205fc609d9c6c7e8940ba79c144a3367c1b22afe70b3782,
  p5 6f6a42bb5bad8de0efe0980dcdb1552009646cdabf08d82d076c5741fd2822bd,
  p6 40c6999bd553c00cd39d98e710d06dbd77997aaa4e84b244fb2fa2870fcfc082,
  p7 9056fefc91e1e3358fb8ad41f5fc4a872e63e62bafc037946ac696662da476a4,
  p8 b3463317666f05e3c7cd929006f655f94ada0e06384db0a55cecd6cfe121e60f.

## 13. Delivery

- NOT pushed to git, NOT posted to Discord, NO messages sent (per task).
  Delivery to the LucernaRead/weekly repo is the main line's job.
- NOT self-certified as finalized: a fresh full independent proof round
  is still required before delivery.
