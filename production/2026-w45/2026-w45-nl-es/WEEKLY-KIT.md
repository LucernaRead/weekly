# WEEKLY KIT — De Lucerna, VOL.2 (NL × ES, W45)

## 1. Identity and pairing (as printed)

- **Issue week:** Monday 2 November – Sunday 8 November 2026; issue dated Monday 2 November 2026.
- **Volume:** VOL.2 for Nederlands (sequel to W43 VOL.1).
- **Masthead:** De Lucerna (frozen from the NL core).
- **Pairing badge (P1, measured from the rendered SVG):** y=568, 20pt bold BRICK (#a4553a), centred —
  «TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES»
  (advance width 1116px, limit 1820px). Slot follows the W43 NL×ES precedent: inserted between the
  band (ends y=542) and the headline label (y=606); the y=372 strapline stays frozen body text.
- **Footer (every page, measured):** «De Lucerna · SEMANARIO NEERLANDÉS VOL.2 · TEXTO EN NEERLANDÉS ·
  EXPLICACIONES EN ESPAÑOL» (20pt, advance 985px) / «Página N de 8».
- **Top strip:** «ELKE WEEK IN HET NEDERLANDS · CADA SEMANA EN NEERLANDÉS» (21pt, 661px).
- **P1 subtitle line:** «SEMANARIO NEERLANDÉS · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12»,
  kept at the core's 40pt serif bold — measured 1811px against the 1820px page width (fits by 9px;
  the W43 36pt fallback was NOT needed here).
- **Gloss prefix:** «Nota — » (W43 NL×ES precedent).
- **P8 separators:** «— PAGINA N —» — the W43 NL×ES shipped form (measured from its P8 SVG), kept
  verbatim; tables.json's «— PÁGINA N —» variant was NOT used (W43 measured wins over the table).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Lead topic (from the core, unchanged):** «Nederland in de Klimaatweek» — Klimaatweek (2–8 Nov),
  Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov).

## 2. Core measured values (W45 NL core, verified, not assumed from other families)

- **Total: 150 exercises.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By level: A2 47, B1 72, B2 31.
- By registry type (core): 完成句子 65, 单选 44, 词汇配对 8, 判断对错 7, 造句 8, 完形单选 13, 翻译 4, 写作 1.
- Model essay (P8 H, ex. 150): 87 words (requirement 80–100).
- Numbering continuous 1–150; P8 printed answers verified against the registry (p8.py extract: noted set = 150 of 150).
- Images (frozen from the core, all reused W43 NL build assets, Commons API Artist credits):
  P1 herfstbos — Vovogov90, CC0; P2 kinderdijk — Nationaal Archief, CC0;
  P3 gracht — W. Punt / Anefo, Nationaal Archief, CC0; P4 elftal1912 — Spaarnestad Photo, public domain.
  Every credited image is laid out on its page (verified in the rendered cards); no new images were added.

## 3. Baseline proof (before any explanation-layer change)

- The W45 NL core build was copied to `hidden_files/weekly-report-w45-nl-es-build/` with OUT repointed
  to the new edition dir, then run unmodified: **all 8 SVGs byte-identical to the shipped core (8/8 cmp)**.
- The proof was re-established a second time from an isolated scratch copy (HOME-redirected run):
  scratch core build reproduces the shipped core SVGs **8/8 byte-identical**.
- The shipped core SVGs were verified untouched at the end of the build: sha256 values match the
  baseline record exactly (p1 5424557b…, p2 78e6fcd2…, p3 5b9854e3…, p4 cc227fd9…, p5 e58064c9…,
  p6 6583fe28…, p7 65cfe2b3…, p8 fe22a151… — full values in the build log).

## 4. Freeze verification (builder self-gates, all measured)

- **freeze.py diff (core vs edition SVG text nodes):** p1 +29/−28, p2 +39/−33, p3 +32/−27, p4 +28/−25,
  p5 +38/−33, p6 +36/−32, p7 +51/−49, p8 +178/−166; **added CJK characters: 0 on every page, 0 total**.
  Edition SVGs contain **0 CJK characters and 0 full-width parentheses** on all 8 pages.
- **Registry-level diff (isolated scratch runs of both builds, REG dumped to JSON):**
  page and level identical for all 150 items; **key diffs: exactly 3 — #137, #138, #150** (see §5);
  type diffs: exactly 38, all P8 items #113–150 (Huecos 13, Elección 12, Frases 4, Traducción 4,
  Relacionar 4, Redacción 1 — the W43 NL×ES precedent: P1–P7 registry type names stay as the core's,
  since type names are never printed on P1–P7 pages); note diffs: 144 translated, 6 unchanged
  language-neutral notes (wij → planten; je → bespaar; rood = blijf binnen; ik → doe mee;
  hij → gaat praten; 45 + 25 = 70).
- **Dutch target text frozen:** all articles, prompts, options, chart data, captions, credits and
  golden sentences are byte-identical to the core, except the documented exceptions in §5 and the
  readers'-corner persona entry in §7 (W43 NL×ES precedent).
- **Banned string:** the banned intermediary term appears 0 times in the edition SVGs, the KIT and
  the edition build code (content modules + bslib; the gate script holds it only as its search needle).

## 5. P8 gate (tools/p8.py compare, dash style, total 150)

- **Status: CLEAN — core 150 noted, edition 150 noted, missing=[], extra_count=0, uncertain=[].**
- **Reported keydiff: [7, 17, 70, 71, 76, 96, 137, 138, 148] — adjudicated item by item:**
  - **True redirections (2):** #137 core key «气候周持续七天。» → «La Semana del Clima dura siete días.»
    (E translation NL→ES); #138 core key «橙色预警意味着：做好准备。» → «El código naranja significa:
    prepárate.» (E translation NL→ES). #139/#140 prompts were flipped ES→NL with Dutch keys unchanged
    (W43 precedent), so they correctly do NOT appear in keydiff.
  - **Extraction artifacts (7):** #7, #17, #70, #71, #76, #96, #148. For each, the printed key is verified
    identical from the raw P8 SVG answer lines (7: B; 17: wortelen; 70: eiland; 71: proef;
    76: gaat winnen; 96: advies; 148: B). The tool's paren branch misclassifies these dash-style lines
    because their (translated) notes end in a parenthesised fragment — e.g. «wortelen = echar raíces
    (sujeto plural)» — and returns key+note-minus-fragment as the pseudo-key, so the pseudo-key
    differs exactly because the note was translated. This is the documented p8.py paren-branch
    artifact class (key candidate must contain no parenthesis); the tool was NOT modified, since the
    shared tool's paren handling is validated for paren-style families and the artifact is fully
    explained and verified here from the raw lines.
  - **#150 (not in keydiff, real change, recorded):** the H key is explanation language by design:
    «（开放题，范文如下）» → «(Pregunta abierta — modelo a continuación)», with the note
    «El modelo está en la sección H de esta página (87 palabras)» (W43 precedent). Both sides extract
    to the check mark «✓», so the tool does not flag it.
- **EXTRA_ONLY does not apply:** status is CLEAN, not EXTRA_ONLY.

## 6. Gloss counts (split on · in the rendered gloss() string itself, per README #21)

- P2: core 6 → edition 6 (het klimaat / wortelen / besparen / de verwarming / de waarschuwing / lokaal).
- P3: core 5 → edition 5 (het museum / de rondleiding / het tijdslot / tweedehands / de beurs).
- P4: core 5 → edition 5 (de balans / gelijkspelen / de speelronde / de topper / de stand).
- P5: core 5 → edition 5 (het eiland / de proef / stemmen / de aflevering / voorbij).
- P6: core 5 → edition 5 (de meteoroloog / waarschuwingsmoeheid / vastzetten / het advies / de voorstander).
- **All five gloss boxes match the core 1:1.**

## 7. P7 gates

- **Word-box definition sentence (verbatim retention, measured):** ««meedoen» betekent: deelnemen,
  erbij zijn. In de Klimaatweek doet heel Nederland mee.» — core count 1, edition count 1, byte-identical.
  Only the gloss line below it was localised («meedoen = participar: en la Semana del Clima participa
  todo el país.»). No definition sentence was translated or edited.
- **Golden sentences:** all 8 core Dutch sentences appear exactly 2× in the edition (article + P7),
  with page labels matching the core: Pagina 1 ×2, Pagina 2 ×1, Pagina 3 ×1, Pagina 4 ×1, Pagina 5 ×1,
  Pagina 6 ×2; each quote was additionally verified to occur on its labelled page's article.
- **P7 teaching phrases:** all Dutch example/clinic phrases are core-frozen and unchanged; only their
  Spanish notes were localised.
- **Readers' corner — no fabrication, all three facts on the page, explicit invitation:**
  - No real reader letter exists for this issue; no reader, letter, name or quote was invented.
  - The box prints a clearly labelled editor's example: ««Hallo! Ik ben Lucía en ik leer Nederlands in
    Madrid. In de Klimaatweek plant ik een boom op mijn balkon!» — Lucía (voorbeeldbrief van de redactie)».
    Persona adaptation Li/Shanghai → Lucía/Madrid is the W43 NL×ES documented reader-language entry
    (the example sentence is Dutch, adapted only in name/city); it remains labelled as an editor's example.
  - The three facts are on the page in Dutch (frozen disclosure) and in Spanish:
    «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte
    naar VOL.3.» / «Sin cartas reales ni mejores textos de la página 8 al cierre: publicamos este ejemplo;
    los prometemos para el VOL.3.»
  - **Explicit Spanish invitation, verbatim (imperative + publication promise):**
    «Ejemplo de la redacción, no una carta real. ¡Envíanos tu carta real y tu mejor texto! Los publicaremos
    en el VOL.3!»
    (Content-preview lines and exercise hints elsewhere were NOT counted as the invitation.)
  - P7 column-3 stack ends at y=1925.5, above the golden-sentences rule (y=1937) — 11.5px clearance.

## 8. Geometric occlusion audit (tools/occlusion_audit.py, selftest OK)

- **Final: edition 0 flags, core 0 flags, NEW vs core 0 flags.**
- **Same-baseline ink scan (additional, README #10):** 8 advance-width flags, all in the P1
  «IN DEZE EDITIE» contents rows (Pag. N / title / level) — byte-identical to the core's own 8 flags
  for the same frozen rows (advance-width artifacts; true-ink audit reports 0). The P1 top band
  (VOL.2 / strip / date, y=92) is clean.
- **Chart-label coverage (additional, README #12):** P6 chart labels vs later-drawn bars — 0% coverage
  on all 4 rows (label ink bottom to bar top clearance 4px each; no clipping, below the 30% COVER
  threshold and below any graze).
- **Fix history (each re-render preceded by a full sha256 record of the current SVGs/cards/PDFs):**
  - Fix-0: P1 headline flow and P2 exercise flow overflowed (bridge/box Spanish lines added lines and
    pushed blocks across column boundaries). Fixed by shortening only Spanish explanation text to restore
    the core's line counts: P1 bridge (4→3 lines), P1 cijfers lines 200 (4→3) and 9 (3→2),
    P2 bridges A and C (2→1 lines each). After the fix, P1-headline ends at the core's y=1452 and
    P2-ex at the core's y=2407, with zero FLOW OVERFLOW / HEAD TOO WIDE warnings.
  - Fix-1: occlusion audit found 2 NEW flags — P1 word-of-week Spanish note covered by the IN HET KORT
    box, and P7 BRIEVEN box overlapping the golden-sentences rows (Spanish notes added lines to the
    PAS OP and BRIEVEN boxes; col-3 stack ended at y=2101.5 vs the 1937 rule). Fixed by shortening only
    Spanish notes (PAS OP notes to 1/1/1/2 lines; BRIEVEN disclosure and invitation to 3 lines each;
    P1 word-of-week note to 2 lines). After the fix, occlusion reads 0/0/0 and P7 col-3 ends at 1925.5.
  - Final build: **zero FLOW OVERFLOW / HEAD TOO WIDE warnings** in the full one-process run.

## 9. Furniture comparison vs W43 NL×ES (measured, not README #20 generic)

- Badge: same slot/geometry as W43 (y=568, 20pt bold BRICK, centred, full badge string) — W43 measured wins.
- Footer: W43 form with VOL.1 → VOL.2 (target core's volume).
- Gloss prefix «Nota — », P8 answer flow 13.0pt/1.12/0.4, P8 separators «— PAGINA N —»,
  P8 type renames (38 items), E-section 2-keys-translated + 2-prompts-flipped, H key in the reader
  language — all copied from the W43 NL×ES shipped build/code, not from generic tables.
- Deviations from W43 (recorded, with reason): P1 subtitle kept at 40pt (measured 1811px fits; W43
  needed 36pt because its string measured 1972px); P6 chart title shortened to «DE GRAFIEK · EL GRÁFICO»
  and the pro/contra title to «VOOR OF TEGEN? · PROS Y CONTRAS» (both measured over the 390px box-inner
  width in their long forms: 574px and 458px); P1 cijfers title kept in the W43 short form
  «DE WEEK IN CIJFERS · EN CIFRAS» (380px vs the 390px limit).
- W43-measured values that overrode tables.json: P8 separator «PAGINA» (not «PÁGINA»); badge slot
  y=568 inserted (not a subtitle-slot replacement — the NL family has no free subtitle slot).

## 10. Toolchain

- **run.py:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0 (measured in the venv).
- **render.py (CairoSVG):** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg installed
  (system python3 is 3.12.3 / Pillow 10.2.0 but lacks cairosvg, so it was NOT used for rendering).
- **Byte-reproduction:** the unmodified core build copy reproduced the shipped core SVGs 8/8
  byte-identical under the venv interpreter (see §3); the edition build uses the same interpreter.
- **Line-width measurement:** all widths in this KIT are rendered-SVG/PIL measurements (svglib text_w
  on the production fonts), never advance-width guesses from other families.

## 11. Delivery (files only — NOT pushed to git, NOT posted to Discord, NOT messaged anywhere)

- `files/weekly-report-w45-nl-es/` — `svg/` (8 SVGs), `cards/` (8 PNGs, 1950×2700),
  `De-Lucerna-VOL2.pdf` (print, 8 pages, 7,917,403 bytes,
  sha256 14009e0c85cdde7871fcd09d6ddef59ad8bf683fb2675895af17bc0968096026),
  `De-Lucerna-VOL2-web.pdf` (web, 8 pages, 3,680,221 bytes < 10 MB,
  sha256 83443cc2b293595ae25b2a7a20e27fc3d49df2531876df51e511359e7032c733),
  `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (Spanish, one line, no ASCII double quotes).
- SVG sha256 (final): p1 b1737f90…, p2 7e39848d…, p3 80ba540e…, p4 3cce6dff…, p5 3b984901…,
  p6 e9daa31b…, p7 6131d67a…, p8 0b23b55f… (full values in the build log).
- Build tree: `hidden_files/weekly-report-w45-nl-es-build/` — build log (build-log-fix1.txt),
  pre-render sha256 records, transform_es.py, gates.py + gates-out.txt, freeze-diff.txt,
  p8-compare.txt, occlusion.txt / occlusion-fix1.txt, rowcheck.py + rowcheck-out.txt.
- **Builder status: builder-complete on all self-gates above. NOT finalised — independent proofread
  is still required before finalisation (per task instruction, no finalisation is claimed here).**

## 12. Visual inspection record (builder's own pass over rendered cards, 8/8)

- All 8 cards read end to end: no overlaps, no cut-off text, no defects. P1 badge/subtitle/word-note
  clear of the IN HET KORT box; P7 BRIEVEN box clear of the golden-sentences rule; P6 chart labels
  clear of bars; P8 answer flow ends well above the footer; footers read «Página N de 8» on all pages.
