# PROOF-NOTE — W47 es-nl proof1 (independent proofread)

- Edition: `production/2026-w47/2026-w47-es-nl/` (Spanish target × Dutch reader),
  builder: fan-out builder, build 3, 2026-11-11
- Proofreader: proof1 subagent, 2026-11-11. Full text read (1,816 lines),
  all mechanical gates run (see GATE-LOG.md), all 8 pages + web P1/P8 visually
  inspected at 150 dpi, external facts verified by web search.
- Identity verified: print PDF 3,502,220 B
  `f88a21414c77508b8eb1a26af763e027fb5a1eed657b6fb576097ede8171dab1`;
  web PDF 850,386 B `85240de829be675577d03467f8697e8bf2f7814fb1de022a20f2290da9a4bcb3`;
  text.md 44,788 B `8801edefd46f58ea78beb576bb3a90e9babeb3c9e710def96ffef3578bcb0283`.
- **Conclusion: (b) — 6 defects, NOT publishable as-is.** No source file was
  modified; no rebuild, commit or push.

## Defects

### D1 — P6, medium, CORE (verbatim in core-es `content56.py`; present in all 10 es fan-out editions)
**Atresmedia debate misattributed to Monday 23.**
- Article: "Atresmedia convoca su propio debate a cuatro para el lunes 23,
  sin el PSOE confirmado." Timeline (EL CAMINO AL 29N): "23 NOV. — Atresmedia
  convoca un debate a cuatro (sin el PSOE)."
- Fact: the 23 Nov debate is **RTVE's Debate a 8** (spokespersons of the 8
  parliamentary groups); **Atresmedia's debate a cuatro is 26 Nov** (PP
  confirmed attendance 4 Nov; PSOE wants it on RTVE). Sources: RTVE's own JEC
  coverage plan (juntaelectoralcentral.es PDF), democrata.es 6 Nov, elfolio.es,
  cronicadecantabria.com 4 Nov.
- The 26 Nov timeline line is also muddled: "26 NOV. — El PP propone un debate
  a cuatro (sin fecha pactada)" — 26 Nov was Atresmedia's proposed date,
  accepted by the PP. Correct on the same page: cara a cara Mediaset Mon 16
  (PSOE unconfirmed at 10 Nov, verified), laSexta debate Fri 13 21:30
  (Cuerpo/Bravo/Bustinduy/Figaredo, verified), Cadena SER housing debate Wed 18
  (Bravo vs Isabel Rodríguez, verified).
- Fix: rewrite both sentences + timeline lines to RTVE 23 Nov / Atresmedia 26 Nov
  (in core, then re-fan-out).

### D2 — P6, medium, CORE (verbatim in core-es `content56.py`; also on P1)
**"Solo hay un debate cerrado" is false as of 10 Nov — and the false fact is
taught in the exercises.**
- Article: "Al cierre de esta edición, el 10 de noviembre, solo hay un debate
  cerrado: el de portavoces de laSexta, el viernes 13 a las 21:30."
  P1 repeats it: "Fue el único debate cerrado al cierre de esta edición."
- Fact: the Cadena SER housing debate (Wed 18 Nov) was also closed by 6 Nov
  (democrata.es 6 Nov: "han cerrado otro debate"; elfolio.es: "Solo hay dos
  encuentros temáticos confirmados"). The paper's own timeline lists the SER
  debate unconditionally ("18 NOV. — Debate sobre vivienda en la Cadena SER") —
  internal contradiction, on the very page whose lesson is "Un debate
  «propuesto» no es un debate «cerrado»".
- Consequence: Q89 key is wrong — key 89 B: "Tot 10 november is alleen het
  laSexta-debat bevestigd" (P8 answer list). Q90 is unaffected (laSexta fact true).
- Fix: correct the sentence (two debates closed by 10 Nov) in core, re-fan-out,
  and fix key 89.

### D3 — P5, medium, THIS EDITION (Dutch layer)
**¿Y TÚ? cream box: ink spills below the box bottom.**
- Box y 1278–1574.5; last line "impuls? Schrijf twee zinnen en stuur ze in.",
  baseline 1572.6 (clearance +1.9). True PIL ink bottom 1577.6 → **spill +3.1**
  (the 'p' of "impuls" and 'j' of "Schrijf" cross the cream edge onto white
  newsprint). Visually confirmed in `crop-p5-youtu-boxbottom.png` (3×).
  Same defect class as de-es proof1 D1. All other 26 cream rects are inside
  (tightest: P2 "ley." −0.3, P5 "compara precios…" −0.4, P4 −1.3, P3 −1.9).
- Fix: shorten the Dutch prompt or enlarge the box (this edition only).

### D4 — P5, medium, THIS EDITION (Dutch layer)
**Box title overruns the cream box (right edge).**
- "EL PLAN DE LA SEMANA　Het weekplan", size 23 bold: text width 441.2,
  right edge 1001.2 vs box right 960.5 → **overrun −36.8**. The word
  "weekplan" hangs off the cream onto white newsprint — visually confirmed in
  `crop-p5-plantitle.png` (3×). Core title "EL PLAN DE LA SEMANA　本周计划"
  fits with +26.8; only the longer Dutch title overflows.
- Fix: shorten the Dutch title or drop to the Spanish-only title (this edition).

### D5 — P7, low, THIS EDITION (Dutch layer)
**Box title overruns the cream box (right edge).**
- "ERRORES TÍPICOS　Typische fouten", size 23 bold: text width 407.0,
  right edge 1868.5 vs box right 1862.0 → **overrun −6.5**. The final "n" of
  "fouten" crosses the edge — visually confirmed in
  `crop-p7-errorestitle.png` (3×). Core title "ERRORES TÍPICOS　常见错误"
  fits with +81.7.
- Fix: shorten the Dutch title (this edition).

### D6 — P7, low, THIS EDITION (P7 layout)
**"LA PRÓXIMA SEMANA" banner rect clips the footer text.**
- Banner rect y 2493.5–2611.5 (118 tall), placed 29 units lower than in core-es
  (2464.5–2582.5) because the Dutch P7 content runs longer. Footer text
  baseline y=2624, ink top 2611.0 → the rect overlaps the footer ink by 0.5
  units; the footer cap-tops ("La Lucerna SPAANS WEEKBLAD VOL.4 LUCERNA
  SPANISH WEEKLY" / "Pagina 7 van 8") are visibly sliced at 150 dpi
  (`crop-p7-footer.png`, 3×). The banner *text* ink bottom ≈2582.5 < footer
  rule 2596 is fine (KIT §6.6) — the *rect* is the problem. Note the occlusion
  audit does not cover rect-vs-text, so this passed the mechanical gates.
  Also visible in the same crop: the footer rule (y=2596, #d8d2c4) shows as a
  light line inside the dark band.
- Fix: move the banner up / shorten it so its rect ends above the footer ink
  (core has 28.5 units clearance).

## Observation (not counted as a blocking defect)

### O1 — P2 / P4 / P5, low, CORE / mechanism (identical in core-es)
**Orphaned section headings**: the section head sits at the bottom of one
column with its body in the next column — P2 "D LAS PALABRAS" (y 2511, col3
bottom; items 25–28 in col4), P4 "B LAS PALABRAS" (col1 bottom; items 52–55
in col2), P5 "B PALABRAS DEL TEXTO" (col1 bottom; items in col2). Readable
and inherited from the shared Flow layout (core-es has the same geometry), but
a head separated from its body is a layout infelicity; worth a mechanism-level
keep-with-next fix for all editions.

## Verified clean (selected; full evidence in GATE-LOG.md)

- **Mechanical gates**: occlusion 0 flags; p8 150/150, compare CLEAN
  (keydiff [137, 138] adjudicated); freeze baseline 8/8 byte-identical;
  print/web text layers byte-identical (default/-layout/-raw, per-page word
  counts identical); P8 min font 10.125 pt (≥ 9.75 floor); formal keycheck
  150/150; levels A2 50 / B1 72 / B2 28; per-page 10/18/18/18/18/18/12/38.
- **150 keys**: every key hand-checked against its stem (matching sets 25–28,
  52–55, 141–144 all consistent with their definitions; Q34–38, Q56–64,
  Q76–79, Q93–96 incl. Q96 Aunque + indicative, Q101–150 all verified);
  Q150 model text hand-counted = 97 words ✓. Q73 "identidad" and Q88
  "solo datos oficiales, con fuente" confirmed consistent (initial confusions
  resolved against the stems).
- **External facts, all verified by web search**: snap election 29 Nov 2026
  (Sánchez called 5 Oct; campaign 13–27 Nov = 15 days; 13 days Mon 16 → Sun 29);
  LaLiga J13 fixtures/times and J12 results/standings (Barça 33 / Real Madrid
  30 / Atlético 28); UCL MD5 fixtures and MD4 results; flamenco UNESCO
  16 Nov 2010 Nairobi + Día Internacional del Flamenco; Santa Cecilia 22 Nov +
  Bilbao Banda Municipal Sun 22 12:00 Euskalduna; MiDNI (JEC lifted suspension
  5 Nov 2026, acuerdo 330/359); polling hours 9:00–20:00; poll blackout
  24–28 Nov = 5 days; Black Friday Fri 27 Nov. RTVE free-minutes chart
  (45/45/30/30/15, +10×3, total 195) follows the LOREG art. 64 scale exactly
  and is consistent with the reported JEC first-round outcome; the exact JEC
  allocation table itself was not directly retrieved (BOE-A-2026-23258 points
  to the JEC website) — recorded as verified-by-scale, not directly confirmed.
- **Sargent caption verified correct**: asset is Commons "Sargent John Singer
  Spanish Dancer.jpg" (793×1132, exact match); the work is *Spanish Dancer*
  (1880–81, private collection) per Invaluable + Google Arts & Culture.
- **§1.1**: fonts Newsreader / Noto Sans (CJK SC) / UnifrakturMaguntia
  (masthead only); UI colors exactly the spec set; P8 chips 35
  (A2 11 / B1 21 / B2 3); VOL.4 ×9 / VOL.5 ×3; ABSTRACT single-line Dutch,
  455 B, no ASCII `"`; gloss tokens match KIT §8.1; P7 toolbox clearance +9.4;
  P7 "FRASES DE LA SEMANA" all 8 sentences verbatim against P1–P6 with correct
  Dutch translations; P3 ¿Y TÚ? box bottom clean (ink −1.9); P1 "EN ESTA
  EDICIÓN In dit nummer" title fits (+6.0, visually confirmed); "programma's"
  is U+2019 with no space (render gap is the glyph, not a typo).

## Files in this scratch dir

`PROOF-NOTE.md`, `GATE-LOG.md`, `occlusion.json/.log`, `p8extract.json/.log`,
`p8compare.json/.log`, `freeze-diff.json/.log`, `freeze.log`,
`freeze-es-nl-proof1/`, `keycheck-150.json`, `keycheck.log`,
`creambox.py`, `creambox.log`, `creambox-ink.log`, `boxtitle.log`,
`quotes-colors.log`, `print*.txt`, `web*.txt`, `svg-sha-before/after.txt`,
`render/print-1..8.png`, `render/web-1..8.png`,
`crop-p3/p5-youtu-boxbottom.png`, `crop-p5-plantitle.png`,
`crop-p7-errorestitle.png`, `crop-p1-enesttitle.png`,
`crop-p7-bottom.png`, `crop-p7-footer.png`.
