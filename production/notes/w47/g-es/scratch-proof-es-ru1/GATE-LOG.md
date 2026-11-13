# GATE-LOG — W47 es-ru, proof1 (independent proofread), 2026-11-11

Probes first: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` RC=0; scratch write probe OK.
Do-not-write-to /tmp: all scratch work used `TMPDIR` inside the scratch dir.
Tools run via `tools/venv/bin/python`. Titles measured with PIL (Noto Sans CJK SC Regular/Bold, index 2).

## §0 Identity (KIT §7 + disk measurement authoritative)
- print PDF: 3,593,674 B, SHA-256 `1e727ff1d28dfcbaa04bf6835d873475c9080960edaae0650825b8be15925938`
- web PDF: 904,435 B, SHA-256 `b88bfd2ce822603c0711e66ae61107e5c88975c7a9fb4b78246353f041e44877`
- `text.md`: 51,957 B, 1,875 lines, SHA-256 `cee6c798e8ae7ea1f0ca0e87121c577b4fb624f4702d95ec0e29ddac34560b1f`
- All three match KIT §8 exactly.
- **TASK-NUMBERS DISCREPANCY**: the task message cites print 10,458,638 B / `8c3b2e97a88f9c86`,
  web 1,067,060 B / `3c1a7db010d3bda4`, text.md 47,030 B / `df5f1692ba67280c` — these are BUILD 1
  (stale). Disk + KIT agree on build 2 final; the proof ran on build 2 per the task's own rule
  (KIT §7 + disk-measured SHA authoritative).
- Documents read: SOP.md §1.1 + §8 in full; repo AGENTS.md in full; edition WEEKLY-KIT.md in full
  (build 2 final; self-check claims zero known defects; §6.1–§6.16 adjudications noted, incl. keydiff
  [137,138] and P8 #73 fix).

## §1 Occlusion audit (formal, no --selftest)
- `tools/occlusion_audit.py` on the edition: **0 flags**.
- Selftest (run once to validate the tool): all 6 classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired;
  clean controls silent.
- Limitation proven by this run: the audit does NOT cover cream-box content — it missed D1, D2 and the
  box-title overflow D3. Cream-box checks below were done separately (creambox.py + PIL ink + boxtitle).

## §2 p8 extract + compare
- `tools/p8.py`: 150/150 keys extracted.
- Compare: **CLEAN**, keydiff = [137, 138] — matches KIT §6.1 adjudication (translation reorientation,
  Russian-sentence keys + «См. оригинал.»).

## §3 Freeze (reproducibility)
- `tools/freeze.py` (build → shipped svg/): **8/8 byte-identical**.
- freeze_direct (build-copy/svg vs shipped svg/): **8/8**.
- Rebuilt print + web PDFs byte-identical to shipped; rebuilt text.md byte-identical.
  (First direct attempt wrongly compared core-es vs edition — wrong pair; correct pair is build-copy vs
  shipped svg/.)

## §4 Print vs web text layer
- `pdftotext` (raw, no `-layout`): **byte-identical**, 53,128 B — matches KIT.
- `-layout` mode: P1 differs by 1 space («ГЛАВНАЯ ТЕМА» +4 vs +5 spaces before «СМ. СТРАНИЦЫ») —
  layout whitespace artifact, not a text difference. Pages 2–8 identical in both modes.

## §5 Cream-box scan + PIL ink ground truth
- `creambox.py` (crude script values authoritative): 27 cream rects. Last-baseline clearances:
  P1 +73.4/+22.0/+256.0/caption-below; P2 +47.7, +5.3 («ley.»), +7.4; P3 +47.7, +5.3 («música.»),
  **+1.9 your-turn**; P4 +47.7, +110.8, +6.9; P5 +46.6, +47.7, +5.4 blackfri, **+1.9 your-turn**;
  P6 +55.7, +19.4, +35.2, +35.2; P7 +42.5 ERRORES, +26.5 word, +5.7 note; P8 none.
- PIL ink: descenders extend ~5 px below baseline for tight last lines at 19–22 px.
- PNG ground-truth ink vs cream edge:
  - **P3 your-turn: +2 px SPILL** (ink row 1596 vs cream 1594) → **D1**
  - **P5 your-turn: +3 px SPILL** (ink row 1603 vs cream 1600) → **D2**
  - P5 blackfri 0 px (1250=1250, inside); P2 calendar 0 px (542=542, inside); P2 your-turn −3 px;
    P4 your-turn −1 px; P7 note −1 px; P7 ERRORES −38 px.
- Crops viewed: `crop-p3-youturn.png`, `crop-p5-youturn.png` (р-tails visibly on white),
  `crop-p5-blackfri.png`, `crop-p2-cal.png`, `crop-p7-note.png` (inside, thin cream sliver),
  `crop-p1-ahora.png`, `crop-p1-palabra.png`, `crop-p1-caption.png` (negative-clearance adjudications).
- Note: an earlier "corrected" creambox script had a `max()` bug (tuples `(tx,ty,…)` → max picked max-x,
  not max-y); the crude values were used.

## §6 P7 toolbox (ERRORES box)
- Box y=441, bottom 1064.0; last baseline 1021.5 («creo que утверждает: изъявительное.», Noto Sans CJK SC 19.5);
  clearance +42.5 baseline / ink −38 px. Comfortable pass.

## §7 Boxtitle text_w (PIL, Noto Sans CJK SC Bold idx 2)
- 40 bold-olive texts inside cream boxes measured; **1 FAIL** → **D3**:
  «ERRORES TÍPICOS　Типичные ошибки» (Bold 23): 445.2 px wide vs budget 400.5 (+44.7 px);
  rendered ink x-range 1464–1905, 43 px past box right edge (1862) and page right margin.
- All others pass (incl. P6 chart-box first lines w=419.4/325.0 vs budget 851.0).
- Crop viewed: `crop-p7-errores-title.png`.

## §8 Curved quotes / punctuation
- U+201C/U+201D/U+2019: **0 on all 8 pages**; CJK-adjacent 0.
- Full-width punctuation (FF01/FF0C/FF1A/FF1B): 0. U+3000 total 118 (matches KIT).
- U+00B7 (·) present in Notes glossaries + P8 option separators — core convention; SOP §1.1's «·» ban
  covers title/footer/page-line/edition-name separators only, and those use U+3000 (verified: masthead,
  footer «La Lucerna　ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4　LUCERNA SPANISH WEEKLY», «VOL. 4　CUARTA EDICIÓN»).

## §9 §1.1 fonts / colors
- Page 1462.5×2025 pt; UnifrakturMaguntia 147 pt masthead; Newsreader Latin target; NotoSansCJKsc
  Russian reader; NotoSerifCJKsc only for «→» arrows (glyph fallback).
- **P8 min font 10.125 pt** (574 spans, measured — KIT claim confirmed; SOP floor 9.75 pt — within
  the allowed concession).
- Fills all palette except illustration-internal colours (#4d72b4/#7898cd blues, #d7b257/#edd17f gold-ish,
  #cac8ba, #f1e8d4, #efe8d2, #f4efe0, #34483a/#4f765d/#84a283 greens — inside inline illustrations,
  e.g. P1 urna drawing; typography/furniture all palette).

## §10 Dates (date -d, Europe/Madrid, 2026-11-11)
- 9 Mon, 10 Tue, 13 Fri, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 23 Mon, 24 Tue,
  26 Thu, 27 Fri, 28 Sat, 29 Sun — all match the paper.
- 16→29 = 13 days («Faltan 13 días» ✓); campaign 13→27 inclusive = 15 days ✓; Black Friday 27 Nov =
  Friday ✓.

## §11 keycheck-150 (`keycheck-150.json`)
- Built by `build-keycheck.py` from `es-ru-p8-extract.json` (p8 printed keys, p8-compare CLEAN) +
  exercise stems parsed from text.md. **150 entries, no dupes, no missing.**
- Page counts: P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38.
- Levels: A2 51, B1 71, B2 28.
- Types (after hand-correction — the script's backward-search fallback misassigned many):
  insertar 48, opción múltiple 60, relacionar 12, verdadero/falso 8, construir 7, reescribir 10,
  traducción 4, escribir 1. Section→type map verified against section headers and stems read directly
  (incl. P4 block lines 734–842, P7 block lines 1258–1388, P8 block lines 1455–1615).
  Per-page map applied: P1 1–6 insertar, 7–10 MC; P2 11–20 insertar, 21–24 MC, 25–28 relacionar;
  P3 29–33 V/F, 34–38 insertar, 39–42 MC, 43–45 construir, 46 reescribir; P4 47–51 MC, 52–55 relacionar,
  56–59 insertar, 60–64 reescribir; P5 65–69 MC, 70–75 insertar, 76–79 reescribir, 80–82 V/F;
  P6 83–92 MC, 93–100 insertar; P7 101–103 insertar, 104 MC, 105–107 insertar, 108 MC, 109–111 insertar,
  112 MC; P8 113–119 MC, 120–124 MC, 125–132 MC, 133–136 construir, 137–140 traducción,
  141–144 relacionar, 145–149 MC, 150 escribir.
- Set levels from set headers: 25–28 A2; 52–55 B1; 141–144 B2.
- All 150 keys verified stem-by-stem during the full read (matching sets 25–28, 52–55, 141–144
  letter-by-letter; multi-line keys #1, #44, #73, #137, #138, #139; Q76–79 ir a + infinitivo incl.
  «Va a abrirse la urna»; Q95/96 Aunque + indicative; Q150 model text counted by hand = 97 words).
- The text.md export interleaves two columns, so line order ≠ logical order: per-item forward/backward
  searches for instruction verbs misclassify types; types were assigned by section, not by nearest verb.
  Matching items appear as "N. word" lines and are duplicated with glosses in the P8 answer block —
  the answer block was excluded when parsing stems.

## §12 Visual skim (SOP §8.3) — all 8 page PNGs viewed
- P1: masthead, lead, CINCO CLAVES, LA SEMANA EN CIFRAS, AHORA TÚ, urna illustration + caption, UNA
  SEMANA TRES ESCENARIOS, BREVES, QUIZ RELÁMPAGO 7–10. No new defects.
- P2: VIDA, calendar box (all 7 entries match verified dates/events), DECIR LA HORA, LOS DÍAS DE LA
  SEMANA table, ¿SABÍAS QUE…? (24–28 blackout ✓), ¿Y TÚ?, exercises A–D. No new defects.
- P3: CULTURA, Sargent «Bailaora española» + caption, EL FLAMENCO EN TRES DATOS, ¿Y TÚ? (D1 location),
  exercises A–D. Middle-column white space is layout as designed. No new defects.
- P4: DEPORTE, LA CHAMPIONS VUELVE box, LA JORNADA 13 table (6 matches/times verified), exercises A–D.
  No new defects.
- P5: JUVENTUD, mail-vote article (9 Nov documentation dispatch ✓, MiDNI 5 Nov ✓), EL PLAN DE LA
  SEMANA, urna photo + Jebulon CC0 caption, VOTAR POR PRIMERA VEZ, ¿Y TÚ? (D2 location), exercises A–D
  (frame visible; D4). No new defects.
- P6: A FONDO, debate article, EL CAMINO AL 29N timeline (9 entries, all verified), LEER UN DEBATE,
  RTVE chart (45/45/30/30/15 + footnote naming Frente Obrero, PCTE, SALF — see O1), ¿POR QUÉ NO HAY
  ENCUESTAS? chart (5/15/1), exercises A–D. No new defects.
- P7: LENGUA, three grammar columns, Book of Hours image, ERRORES TÍPICOS box (D3 title overflow),
  LA PALABRA, CARTAS DE LOS LECTORES (filler openly labelled), FRASES DE LA SEMANA, LA PRÓXIMA SEMANA
  (VOL.5). No new defects.
- P8: EJERCICIOS Y RESPUESTAS, sections A–H, model text (97 words), swan-quill image, RESPUESTAS
  1–150 with Russian glosses. Spot-checks (83.A, 84.B, 85.C, 87.B, 90.A, 137, 150) consistent with
  keycheck. No new defects.

## §13 External facts verified online (2026-11-11)
- Election: RD 806/2026 (5 Oct, BOE 6 Oct); vote Sun 29 Nov 2026, 9:00–20:00; campaign 15 days
  Fri 13 Nov 00:00 → Fri 27 Nov 24:00; 38,728,356 voters (La Moncloa guide 3 Nov; lavozdeibiza;
  politica360.es; iberoeconomia.es). Mail-vote request deadline 19 Nov; return deadline 25 Nov
  (iberoeconomia.es).
- Mail-vote docs from 9 Nov: Correos official, 10 Nov 2026 — «Desde el 9 de noviembre, las Delegaciones
  Provinciales de la Oficina del Censo Electoral están enviando la documentación electoral».
- MiDNI: JEC lifted the suspension Thu 5 Nov 2026 (acuerdo 330/359); MiDNI authorised for voter ID,
  MiDGT stays suspended; QR generated in front of the polling station (elfolio.es, democrata.es,
  merito.es, 5–7 Nov 2026).
- Frente Amplio: left coalition for 29N (successor to Sumar's 2023 lists); Bustinduy spokesperson;
  Colau PM candidate; Delgado heads Madrid list; Urtasun culture minister (democrata.es,
  eldiariodemadrid.es, elconstitucional.es, Oct 2026).
- LaLiga MD12 (ended 8 Nov): Barça 33 (11-0-1, 48-13), Madrid 30, Atlético 28; Barça 1–2 at Atlético,
  Metropolitano, Sun 8 Nov (Fermín López brace) (comentarista.es, breakinglaliga.com, eurosport.es,
  lagrada.org).
- LaLiga MD13 Fri 20–Mon 23 Nov: Athletic–Espanyol Fri 20 21:00 San Mamés (opener); Sevilla–Betis
  Sat 21 18:30; Real Madrid–Celta Sat 21 21:00; Barcelona–Villarreal Sun 22 14:00;
  Getafe–Atlético Sun 22 21:00; Levante–Elche Mon 23 21:00 (closer) (lagrada.org,
  eldiariodetoledo.com, dazn.com, kirolbet blog, sportradar).
- UCL MD5 Tue 24–Wed 25 Nov: Real Madrid–PSV Tue 24 21:00 Bernabéu; Sabah–Barça Wed 25 18:45 Baku;
  Atlético–Viking Wed 25 21:00 Metropolitano; Slavia Prague–Villarreal Wed 25 18:45;
  Slovan Bratislava–Betis Tue 24 21:00 (elfutbolero.es, eurosport.es, cdeportiva.com).
  MD4: Barça 3–0 Aston Villa; Atlético 0–2 Bayern; Real Madrid 3–2 AEK Athens Wed 4 Nov
  (Valverde 90+2') (espn.cl, clarosports.com, futbolete.com).
- Flamenco: UNESCO inscribed 16 Nov 2010, Nairobi, Representative List; Día Internacional del
  Flamenco 16 Nov (diario.madrid.es, revistadearte.com, Instituto Andaluz del Flamenco).
- Sargent: «Spanish Dancer» oil 1880–1881, private collection; watercolour study 1879–80;
  «El Jaleo» 1882; Spanish rendering «Bailaora española» fair; public domain (d. 1925) ✓.
- Bilbao band: Banda Municipal de Bilbao, Palacio Euskalduna, Sun 22 Nov 12:00 (teoriamusical.com.es,
  checked 2 Nov against official source). Santa Cecilia 22 Nov, patron of musicians ✓.
- laSexta debate Fri 13 Nov 21:30: elfolio.es, democrata.es, diarioenpositivo.com, 6 Nov 2026;
  doblelectura.es (10 Nov): «solo hay un debate cerrado: el de portavoces de laSexta, el viernes 13
  a las 21:30». Ana Pastor moderates; Cuerpo (PSOE), Bravo (PP), Figaredo (Vox), Bustinduy
  (Frente Amplio); economy. Público en el plató confirmed for the 2 and 9 Nov encounters of the same
  strand only (detrasdelatele.es 21 Oct; elfolio.es) — see O2. Pre-campaign debates 2 and 9 Nov
  (first postponed from 2 Nov due to the Urda train tragedy); the paper's «solo hay un debate
  cerrado» refers to campaign debates — no contradiction.
- SER housing debate Wed 18 Nov: elfolio.es, democrata.es, diarioenpositivo.com, 6 Nov 2026 —
  «El segundo debate confirmado tendrá lugar el miércoles 18 de noviembre en la Cadena SER. Estará
  dedicado a la vivienda y reunirá a la ministra de Vivienda… Isabel Rodríguez, y al popular
  Juan Bravo.»
- PP / debate proposals: elfolio.es, democrata.es, diarioenpositivo.com, 6 Nov 2026; elfolio.es 9 Nov —
  cara a cara Sánchez–Feijóo for Mon 16 Nov in Mediaset (Telecinco + Cuatro simultaneously; PSOE
  accepted in principle, PP has the date reserved); debate a cuatro Thu 26 Nov in Atresmedia is the
  PP's position (PSOE wants RTVE; RTVE had also proposed its own a cuatro for 26 Nov); Atresmedia
  moved its own debate a cuatro to Mon 23 Nov (announced Mon 9 Nov; PP, Vox, Frente Amplio
  confirmed, PSOE invitation still open); PSOE proposed 9 Nov that the Academia de Televisión
  organise both main debates; PP accepted the Academia formula; dates/formats still unagreed at
  closing (10 Nov). Paper hedges all as proposals — consistent.
- Poll blackout 24–28 Nov: LOREG art. 69.7 (JEC official text) — «Durante los cinco días anteriores
  al de la votación queda prohibida la publicación y difusión o reproducción de sondeos electorales».
  For vote Sun 29 Nov, the five days before = Tue 24–Sat 28 Nov ✓.
- RTVE/JEC free-slot minutes: LOREG art. 64 scale from the JEC site — 45 min (≥20%), 30 min (5–20%),
  15 min (representation but <5%), 10 min (no run / no representation); art. 64.2 requires
  candidacies in MORE than 75% of constituencies. 2023 results: PP 33.06% → 45 ✓; PSOE 31.70% → 45 ✓;
  Vox 12.39% → 30 ✓. FA 30 / Podemos 15 consistent with JEC proration doctrine (diariodia.es,
  1 Nov, updated 9 Nov: JEC's first ruling favoured FA on seat attribution; votes divided by seats:
  FA ~26/31 Sumar seats → ~10.3% → 30; Podemos 5/31 → ~2% → 15). BOE-A-2026-23258 (4 Nov 2026)
  confirms the JEC agreed the distribution; the table itself is published on the JEC website and was
  NOT retrievable via search. Arithmetic: 45+45+30+30+15 = 165, +3×10 = 195 ✓.
  RTVE informative plan is a DIFFERENT allocation (canariasenpleno.com, 5 Nov 2026): PP 38.96%,
  PSOE 34.67%, Vox 9.45%, FA 6%, Podemos 0.86% of informative blocks; SALF excluded from informative
  blocks under the JEC 2015 instruction on significant groups (≥5%) — that exclusion does NOT
  contradict the paper's «SALF 10 minutos» of free propaganda slots (art. 64).
- PCTE limb (open, O1): Frente Obrero runs in all 52 constituencies ✓; SALF 46/52 = 88.5% ✓;
  Frente Amplio 49 ✓; PACMA correctly excluded (30 provinces only, pacma.es 3 Nov, 57.7% < 75%);
  only four formations run in all 52 (PSOE, PP, Vox, Frente Obrero — nuevaradio.org 4 Nov,
  elfolio.es 3 Nov). PCTE runs in 39 Congreso circunscripciones (nuevaradio.org + lado.mx, 4 Nov,
  citing BOE 3 Nov 2026: BOE-A-2026-23103, 534 Congreso + 361 Senado candidacies proclaimed).
  JEC doctrine (Acuerdos 671/2011, 666/2011, official JEC text): «En el Congreso de los Diputados,
  al haber 52 circunscripciones…, es preciso contar con 40 candidaturas proclamadas y en el Senado,
  al haber 60 circunscripciones…, serán precisas 46 candidaturas» — candidacy for EITHER chamber
  counts, but the threshold must be met in ONE chamber; counts cannot be mixed across chambers, and
  solo/coalition candidacies cannot be summed. 39 < 40, so PCTE fails the Congreso route by one;
  its Senado count is unverified (clm21.es 3 Nov says PCTE has lists in 45 provincias counting
  either chamber, which does not settle the 46-Senado question). Distribution under appeal until
  Tue 10 Nov 10:00 (allegations deadline), the same day the paper closed. Counter-consideration:
  the builder's other numbers all check out precisely (incl. correctly excluding PACMA and including
  SALF at 46), suggesting the builder worked from the actual JEC table — the table may list PCTE
  via the Senado route.

## §14 Adjudicated non-defects (evidence)
- «el 1 como «el uno»» (P7): RAE DPD (rae.es/dpd/primero) — in Spain the cardinal «uno» is MORE
  normal for the day-1 date, ordinal «primero» more normal in America. Paper teaches Peninsular
  Spanish — correct.
- P1 caption page refs: caption «En la página 5, cómo pedir el voto por correo… y en la página 6,
  cómo leer un debate…» (p5 mail vote, p6 debate ✓); «En la página 6 te enseñamos» belongs to the
  consejo block («escucha el debate entero, no solo el titular. En la página 6 te enseñamos…») —
  SVG nodes confirm; the text.md interleave made it look wrong.
- Creambox negative clearances (P1 AHORA TÚ +37, «Пять тем…» +12, LA PALABRA +24, caption +24;
  P2 DECIR LA HORA +37; P3 LO QUE QUEDA +37): next-section titles on paper below the box above,
  each with its own olive rule — scanner artifacts; crops viewed.
- laSexta «a hablar de economía»: elfolio.es 6 Nov likewise describes the 13 Nov debate as
  economy-focused; the paper's narrowing matches a real source (debate also covers vivienda +
  actualidad per Quadratin, 10 Nov) — not listed.

## §15 Lessons / pitfalls recorded during this run
- Never `grep -B/-A` on single-line SVG files (dumps the whole file; one such output was truncated and
  saved by the runtime to a temp file — avoid; use Python regex instead).
- `creambox.py`'s crude values are authoritative; a "corrected" script building `(tx,ty,…)` tuples
  and taking `max()` picks max-x, not max-y.
- `freeze.py baseline --build. --core-svg./svg` run in the edition dir compares the rebuild against
  the edition's own shipped SVGs (reproducibility), NOT against core-es; the direct check is
  build-copy/svg vs shipped svg/.
- Negative creambox clearances are usually next-section titles caught by the +45 px window —
  adjudicate by crop, don't trust the raw number.
- The text.md export interleaves two columns, so line order ≠ logical order: per-item
  forward/backward searches for instruction verbs misclassify exercise types; assign types by
  section (verified against section headers and stems), not by nearest verb. Matching items appear
  as "N. word" lines and are duplicated with glosses in the P8 answer block — exclude the answer
  block when parsing stems.
- The occlusion audit does not cover cream boxes (missed D1/D2/D3) — keep the separate creambox /
  PIL-ink / boxtitle gates.
