# PROOF-NOTE — W47 es-ru, proof1 (independent proofread)

- Edition: `production/2026-w47/2026-w47-es-ru/` (Spanish target × Russian reader)
- Proofreader: subagent proof1, 2026-11-11. Read-only: no source file modified, no rebuild, no commit, no push.
- Identity verified against KIT §7 + disk measurement (build 2 final):
  print PDF 3,593,674 B, SHA-256 `1e727ff1d28dfcbaa04bf6835d873475c9080960edaae0650825b8be15925938`;
  web PDF 904,435 B, SHA-256 `b88bfd2ce822603c0711e66ae61107e5c88975c7a9fb4b78246353f041e44877`;
  `text.md` 51,957 B, 1,875 lines, SHA-256 `cee6c798e8ae7ea1f0ca0e87121c577b4fb624f4702d95ec0e29ddac34560b1f`.
  **The sizes/SHA prefixes in the task message (10,458,638 B / `8c3b2e97…`; 1,067,060 B / `3c1a7db0…`;
  47,030 B / `df5f1692…`) are STALE (build 1).** Per the task's own rule (KIT §7 + disk-measured SHA
  authoritative) the proof ran on KIT/disk (build 2 final). See GATE-LOG §0.
- Full text read: all 1,875 lines of `2026-w47-es-ru.text.md`. All 150 answer keys verified stem-by-stem
  by hand (see `keycheck-150.json`). All 8 page PNGs visually skimmed (SOP §8.3).
- All mechanical gates run for real (occlusion, p8 extract+compare, freeze, freeze_direct,
  print/web text-layer compare, creambox + PIL ink, boxtitle widths, curved quotes, §1.1 fonts/colors,
  dates by `date -d`, external facts by web search). Evidence in `GATE-LOG.md`.

## Conclusion: (b) — NOT zero-defect; cannot be finalized as-is

Four defects (D1–D4). Three are layout (this edition), one is content (core).

## Defect list

### D1 — minor/light — P3, your-turn box («А вы?», bottom-right cream box)
- Location: P3, «¿Y TÚ? А вы?» box, last Russian line «два предложения и пришлите их.»
- Defect: descenders (р in «предложения» / «пришлите») spill **2 px below the cream edge** onto white
  paper (ink row 1596 vs last cream row 1594; box bottom 1594.8, last baseline 1592.8, clearance +1.9 px).
  Box height was set at baseline + 1.9 px with no descender reserve — same class as es-fr proof1 D1.
- Evidence: PIL ink measurement (descenders extend ~5 px below baseline at 19 px); PNG ink scan;
  `crop-p3-youturn.png` (р-tails visibly on white). Spill stays above the divider (y=1608), no collision —
  visual defect only.
- Attribution: **this edition** (fan-out layout; the sizing rule is a shared mechanism weakness, see note).

### D2 — minor/light — P5, your-turn box («А вы?», bottom-right cream box)
- Location: P5, «¿Y TÚ? А вы?» box, same last Russian line «два предложения и пришлите их.»
- Defect: same class as D1, spill **3 px** (ink row 1603 vs last cream row 1600; box bottom 1601.5,
  last baseline 1599.6, clearance +1.9 px).
- Evidence: PIL ink measurement; PNG ink scan; `crop-p5-youturn.png` viewed.
- Attribution: **this edition**.

### D3 — medium — P7, ERRORES TÍPICOS box title
- Location: P7, right column, «ERRORES TÍPICOS　Типичные ошибки» box title.
- Defect: title (Noto Sans CJK SC Bold 23) measures **445.2 px wide vs budget 400.5 px (+44.7 px)**.
  Rendered ink reaches x=1905, **43 px past the box right edge (1862) and past the page right margin**,
  with «ошибки» sitting on white paper. The occlusion audit (0 flags) does NOT cover cream-box titles
  and did not catch this.
- Evidence: boxtitle PIL measurement (40 bold-olive cream-box titles measured, this is the only fail);
  PNG ink scan (ink x-range 1464–1905); `crop-p7-errores-title.png` viewed.
- Attribution: **this edition**.

### D4 — low — P5, section B «PALABRAS DEL TEXTO» (frame/gap mismatch)
- Location: P5 exercises, section B. Header (Russian): «Вставьте слова из рамки. Внимание: некоторые
  слова нужно проспрягать.» Frame: «sobre · papeleta · censo · identidad · plazo · urna».
- Defect: the header instruction («insert words from the frame») is false for **2 of 6 gaps**:
  - 70. «Pido el voto por ___.» → key **correo** — not in the frame («sobre» is envelope, a distractor).
  - 72. «Después ___ (инфинитив: enviar) el sobre.» → key **envío** — derived from the infinitive
    given in the gap itself, not from the frame.
  - Frame words «sobre» and «urna» are never used (unused distractors are normal; missing answers are not).
- The exercise is still solvable («voto por correo» is a set phrase from the article; «enviar» is given),
  and all six keys are correct — the defect is the instruction/frame mismatch, not the answers.
- Verified identical in frozen core-es P5 SVG (frame, same stems) → core text.
- Attribution: **core**.

## Open items (not defects — finalizer to check)

### O1 — RTVE free-minutes chart: PCTE 10 min / 195 total (P6 + Q84) — UNRESOLVED
- Paper claims (P6 chart + Q84 key B): PSOE 45, PP 45, Vox 30, Frente Amplio 30, Podemos 15,
  total **195**, + Frente Obrero / PCTE / SALF 10 each. Arithmetic is internally consistent.
- Verified: LOREG art. 64 scale (10/15/30/45) from the JEC site; 2023 results give PP 45 (33.1%),
  PSOE 45 (31.7%), Vox 30 (12.4%, 5–20% band); FA 30 / Podemos 15 are consistent with the JEC
  proration doctrine for Sumar's split (diariodia.es 1 Nov, updated 9 Nov; JEC's first ruling favoured FA);
  Frente Obrero runs in 52/52 ✓, SALF 46/52 (88.5%, >75%) ✓, PACMA only 30/52 — correctly excluded.
  JEC agreed the distribution 4 Nov 2026 (BOE-A-2026-23258).
- The problem: **the JEC table itself (published on the JEC website per that BOE resolution) could not be
  retrieved by search.** PCTE runs in **39 Congreso circunscripciones** (nuevaradio.org + lado.mx, 4 Nov,
  citing BOE 3 Nov). JEC settled doctrine (Acuerdos 671/2011, 666/2011) requires **40** proclaimed Congreso
  candidacies (or 46 Senado) to meet «más del 75 por 100» — 39/52 is exactly 75.0%, one short.
  PCTE's Senado count (needs 46/60) is unverified. If the JEC table excludes PCTE, then the chart's
  «PCTE 10 minutos», the «195 minutos en total», and Q84's key (B, 195) are all wrong
  (total would be 185 with only Frente Obrero + SALF at 10 min, assuming no other 10-min party).
  The builder's other numbers all check out precisely, which suggests the builder worked from the real
  table — but I cannot confirm the PCTE limb. **Finalizer must check the JEC table directly before
  deciding; if PCTE is out, this becomes D5 (medium, core).**

### O2 — laSexta 13 Nov debate «con público en el plató» (P6) — consistent, not directly confirmed
- Public in the studio is confirmed for the two pre-campaign «laSexta Debate» encounters (2 and 9 Nov,
  same strand, same moderator Ana Pastor, UK-inspired format — detrasdelatele.es 21 Oct; elfolio.es).
  No source found confirming it specifically for the 13 Nov campaign edition. Reasonable inference,
  not a defect.

### O3 — Image credits not independently verified (low priority)
- P5 urna photo («Foto: Jebulon — CC0, Wikimedia Commons», bronze «Suffrage universel» ballot box)
  and P7 Book of Hours image (public domain) — credits as printed, not checked against source.

## Adjudicated non-defects
- P1 caption page refs correct («En la página 5, cómo pedir el voto por correo… y en la página 6,
  cómo leer un debate…»; the «En la página 6 te enseñamos» line belongs to the consejo block — SVG nodes confirm).
- Creambox "negative clearance" flags (P1 AHORA TÚ / «Пять тем…» / LA PALABRA / caption; P2 DECIR LA HORA;
  P3 LO QUE QUEDA) are next-section titles on paper below the box above, each with its own olive rule —
  scanner artifacts, verified by crop.
- P5 blackfri / P2 calendar 0 px: descenders end exactly on the last cream row, not beyond — inside.
- «el 1 como «el uno»» (P7): NOT a defect. RAE DPD (rae.es/dpd/primero): in Spain the cardinal «uno»
  is the MORE normal form for the first day of the month («uno de enero»); ordinal «primero» is the
  American usage. The paper teaches Peninsular Spanish, so «el uno» is correct.
- laSexta 13 Nov debate «a hablar de economía»: a narrowing (the debate also covers vivienda +
  actualidad per Quadratin), but elfolio.es 6 Nov likewise describes it as economy-focused; not listed.
- P7 reader letter («Marta»): openly labelled an example written by the newsroom («ejemplo, escrito
  por la redacción») with an editor's note that no real letters had arrived — honest filler, not a defect.
- P3/P5/P6 middle-column white space: layout as designed (short middle-column blocks above the fixed
  exercise band); no missing content, no occlusion.

## External facts verified (all checked 2026-11-11; sources in GATE-LOG §9)
- Election real: RD 806/2026; vote Sun 29 Nov 2026, 9:00–20:00; campaign 15 days Fri 13 → Fri 27 Nov;
  38,728,356 voters; mail-vote request deadline Thu 19 Nov, return deadline Wed 25 Nov.
- Mail-vote documentation «a partir del lunes 9 de noviembre» ✓ (Correos official, 10 Nov 2026).
- MiDNI: JEC lifted the suspension Thu 5 Nov 2026; MiDNI authorised for voter ID ✓.
- Frente Amplio real (Bustinduy spokesperson, Colau PM candidate, Delgado heads Madrid list) ✓.
- LaLiga MD12 table (Barça 33, Madrid 30, Atlético 28; Barça 1–2 at Atlético, 8 Nov) ✓;
  MD13 six matches + times (20–23 Nov) ✓; UCL MD5 fixtures + MD4 results ✓.
- Flamenco: UNESCO inscribed 16 Nov 2010; Día Internacional del Flamenco 16 Nov ✓.
- Sargent «Bailaora española» 1880–81, public domain (d. 1925) ✓.
- Bilbao band: Palacio Euskalduna, Sun 22 Nov 12:00; Santa Cecilia 22 Nov ✓.
- Debates: laSexta Fri 13 Nov 21:30, Ana Pastor, Cuerpo/Bravo/Figaredo/Bustinduy ✓;
  SER housing debate Wed 18 Nov, Rodríguez vs Bravo ✓; cara a cara Mon 16 Nov (Mediaset, PP proposal,
  PSOE accepted in principle) ✓; debate a cuatro Thu 26 Nov (Atresmedia, PP proposal) ✓;
  Atresmedia a cuatro moved to Mon 23 Nov, PSOE unconfirmed ✓; «solo hay un debate cerrado»
  (laSexta) ✓ as of 10 Nov.
- Poll blackout 24–28 Nov: LOREG art. 69.7, five days before voting ✓ (JEC site text).
- RTVE/JEC free slots: scale + PP/PSOE/Vox/FA/Podemos/FO/SALF verified as above; PCTE limb open (O1).

## Files
- `keycheck-150.json` — all 150 keys, hand-verified stem-by-stem (p1: 10, p2: 18, p3: 18, p4: 18,
  p5: 18, p6: 18, p7: 12, p8: 38; types: insertar 48, opción múltiple 60, relacionar 12,
  verdadero/falso 8, construir 7, reescribir 10, traducción 4, escribir 1; levels A2 51 / B1 71 / B2 28).
  Note: P8 key #150 is the full printed answer «✓ См. образец в разделе H (97 слов)»; model text
  counted by hand = 97 words, confirmed.
- `GATE-LOG.md` — full gate evidence.
- `crop-*.png` — visual evidence for D1/D2/D3 and the adjudicated 0-px cases.
- `build-keycheck.py` — generator script for `keycheck-150.json` (sources: text.md + p8 extract).
