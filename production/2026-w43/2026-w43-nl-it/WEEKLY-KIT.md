# De Lucerna VOL.1 — Dutch text · Italian explanations (NL × IT)

Fan-out edition of the frozen NL VOL.1 core (files/weekly-report-nl-vol1/, Dutch text + Chinese explanations). This edition keeps the Dutch target text, images and layout geometry byte-frozen and rewrites ONLY the explanation layer into Italian for Italian-speaking readers. Build dir: hidden_files/weekly-report-nl-it-build/ (a true copy of the core build; the core was never edited).

## 1. Baseline proof (method gate)

The copied core build was run UNMODIFIED first (output redirected to build-local scratch/baseline-svg/): all 8 SVGs reproduced the shipped core SVGs **byte-identically (sha256 8/8)**:

- p1 a8a2cc5d017c00203d8807f4cc04f2136d508677331ffc12942b69fde386e4b2
- p2 ea3f2a1880507fb5d49b2d98bb4d155d78f1f373843881fbbec4ae5dce7b3ee1
- p3 b61fbb1b07cc97926488953a07e5c5e1a4f2aa94312b09e1bcf82ed254b0c75a
- p4 eff3145811a040bf1905f6021c6e849718dc81b009d5d2762bf52c8a5e48c952
- p5 1098c65798e4877a14b8e2f456553afd6c1b23300d680d5ba6a916e4603335f4
- p6 c941eb447f2d24d45bd5d02ccf6e640cd36306d467aea26276060e436dbf0145
- p7 097fcfa7d713b861117203463e84534d1cc5c298d82098156da0e1833a952431
- p8 feba80260b4bc2bc4445951a821546946fa1a13b16c9acb798ba3c74c812c30f

Core registry at baseline: 150 exercises, A2 42 · B1 76 · B2 32, per-page 10/18/18/18/18/18/12/38, writing model 87 words. After all work, the core's shipped SVG hashes were re-verified — **all 8 unchanged** (same list above).

## 2. Totals (verified programmatically against the core registry)

- 150 exercises — A2 42 · B1 76 · B2 32; per-page 10/18/18/18/18/18/12/38 — identical to core.
- Type distribution identical to core, labels in Italian: Completa la frase 66 · Scelta multipla 45 · Cloze 13 · Abbinamento 8 · Forma la frase 7 · Vero o falso 6 · Traduzione 4 · Scrittura 1.
- Visible text volume: 35,404 chars (no spaces) vs core 29,851 (Italian explanation layer is longer than the Chinese one; expected).
- CJK characters in the final 8 SVGs: **0** (raw bytes and text layer). The intermediary-layer term occurs **0** times in paper, this KIT, and build code (the inherited helper was renamed `expl()`; all call sites updated).

## 3. Key-diff registry (complete)

Translation-type items legitimately re-aim at Italian. Render-level comparison of both P8 pages plus registry-level comparison give exactly:

- **#137 — key changed to Italian**: «Domenica l'orologio torna indietro: un'ora di sonno in più!» (stem is the frozen Dutch P1 band sentence).
- **#138 — key changed to Italian**: «Il tuo telefono e il tuo computer cambiano l'ora da soli.»
- **#139 — stem re-aimed** (body now Italian, answer stays Dutch): «La Dutch Design Week è a Eindhoven. → ___». Key unchanged: «De Dutch Design Week is in Eindhoven.»
- **#140 — stem re-aimed** (body now Italian, answer stays Dutch): «Domenica ho dormito un'ora in più. → ___». Key unchanged: «Zondag heb ik een uur langer geslapen.»
- **#150 — key/apparatus changed to Italian**: «(domanda aperta, testo modello sotto)» (printed in the ✓-note form, as in the core).

No other key differs. All 150 P8 notes were rewritten in Italian; the only notes identical to the core are #12, #46, #79, #84 — language-independent numeric/formula notes (e.g. «03:00 → 02:00», «19,50 + 19,50 + 32,50 = 71,50»), correct as-is. No note is empty.

## 4. Italian-column furniture (verbatim, as printed)

- P1 pairing badge (brick, size 20): «TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI» — measured 840.9 units in the 1820 slot.
- P1 subtitle: «SETTIMANALE OLANDESE · VOL.1 · DE KLOK GAAT TERUG · HERFSTVAKANTIE · ADE WORDT 30» at 36 px (core ships 40 px; the Italian string measured 1764.8/1820 at 36 px).
- Footers, all 8 pages: «De Lucerna · SETTIMANALE OLANDESE VOL.1 · TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8».
- Gloss prefix: «Nota — » (all pages).
- Masthead: «De Lucerna» exactly as the core ships.
- Section heads: IN PRIMO PIANO, ESERCIZI, SOMMARIO, IN BREVE, QUIZ LAMPO, CHE ORE SONO?, IL GRAFICO, ABOLIRE?, PAS OP! · ERRORI FREQUENTI, HET WOORD · LA PAROLA, FRASI DELLA SETTIMANA, LA PROSSIMA SETTIMANA, TEST E RISPOSTE, RISPOSTE.
- **Answer-key format note**: this edition keeps the CORE's dash style `N. key — note` (the core and all NL siblings — de/es/fr/en — use dash style). The «space before note parenthesis» rule applies to parenthesis-style editions; NL editions have no note parentheses, so no deviation in substance. Recorded here for the proofreader.
- Two furniture strings shortened by wording only after real-width measurement (see §6): P1 trends footnote and the P6 pro/contra box title.

## 5. Freeze check (text-node diff vs core SVGs)

Full multiset text diff per page (build scratch/freeze-diff.txt, 691 lines, reviewed line by line): every removed element is Chinese explanation layer / pairing furniture / Chinese instruction labels; every added element is its Italian counterpart. Dutch text outside §3's registry items is byte-identical; apparent Dutch fragments in the diff are wrap-point shifts of the same Dutch sentences around translated parentheticals. Image payloads: base64 byte-identical per page vs core (counts 1/1/2/1/1/0/0/0); print-PDF XObject counts per page identical to the core print PDF.

**Printed-note set equality (mandatory gate)**: sequence-aware parse of both P8 SVGs — core prints notes for items {1..150}, this edition prints notes for items {1..150}. **Sets EQUAL (150 = 150)**, every entry carries a note. (The core prints all 150 notes; so does this edition.)

## 6. Defects found by the builder and fixed (wording only, geometry frozen)

1. **P7 column-3 stack overflow**: Italian clinic/gloss lines wrapped longer than the Chinese ones; the stack ended at y=1825.5, overlapping the quotes section (rule at y=1698). Four clinic lines and one letters-box line shortened by wording → stack ends at **y=1678.5, exactly the core's value**.
2. **P8 answer-flow overflow**: longer Italian notes pushed the answer flow to y=2582 (page bottom 2552). Fixed per the FR×IT precedent — answer font 13.5→13.0, line height 1.16→1.12, column gap 0.5→0.4 → flow ends at y=2340, zero overflow warnings.
3. **Two over-wide furniture strings** (real-font measurement): P1 trends footnote 402.7 > 390 box slot → «Istantanea di martedì: numeri stimati» (327.4); P6 pro/contra box title 421.3 > 390 → «AFSCHAFFEN OF NIET? · ABOLIRE?» (363.7). All other 19 measured furniture strings fit (footer 908/1560, PAS OP title 346.6/390, ZO ONTHOUD box title 391.0/398).

## 7. Geometric occlusion audit (mandatory gate)

Script: build-dir audit_nl_it.py (paint-order SVG parse, PIL real-font glyph metrics, line boxes expanded by half stroke width). **Self-test on a synthetic positive control PASSES** (fires COVER/LINEX/FOOTER/TEXTX; clean page silent).

- Core (for reference): 1 flag — P1 masthead TEXTX (inherited class).
- This edition: 16 flags, **all adjudicated NON-DEFECTS with pixel evidence; 0 unresolved**:
  - 1× P1 masthead TEXTX (same inherited class): on the shipped card, wordmark ink ends at row 265 and subtitle ink starts at row 303 — **37 empty rows of air** (core: 30). Band-model artifact only.
  - 15× P8 TEXTX: two-line answer entries whose conservative ink bands (−0.88em/+0.30em) overlap 5% at line height 1.12. Exhaustive real-ink measurement of all 15 consecutive pairs: 5 pairs have bounding boxes touching by −0.44 px; definitive pixel test (both lines rasterised in one shared frame at true pitch and true x, masks verified non-empty, 146–1787 ink px per line) → **0 shared ink pixels in all 15 pairs** — descenders and ascenders never coincide horizontally. Non-defects.

## 8. P7 phrases of the week

All 8 quotes are the core's verbatim Dutch excerpts, unchanged, with unchanged page tags («(Pagina N)»): wintertijd sentence (p.1), voorjaar/najaar (p.2), Thuisbezorgd (p.2), 2.500 ontwerpers (p.3), PSV–Porto (p.4), 3.000 artiesten (p.5), 750.000 keer (p.6), 547.000 (p.6). Occurrence count in the full issue text: **exactly 2× each**, matching the core's 2× each. Only the Italian translations under each quote are new.

## 9. Images (all public domain / CC0; credits as printed, from the core KIT)

- P1 Westertoren, Amsterdam — Wim van Rossem / Anefo, Nationaal Archief — CC0.
- P2 pocket watch (zakhorloge) — photo-nic.co.uk / Wikimedia Commons — CC0.
- P3 Kinderdijk windmills — Nationaal Archief — CC0; autumn forest (herfstbos) — Vovogov90 — CC0.
- P4 Netherlands elftal 1912 — Spaarnestad Photo — public domain.
- P5 Amsterdam canal boat (gracht) — W. Punt / Anefo, Nationaal Archief — CC0.

## 10. Dates and facts spot-verified against the real 2026 calendar

Weekday claims appearing in the Italian layer, checked with `date` (Europe/Amsterdam): Oct 17 = Saturday («sabato 17 ottobre»), Oct 19 = Monday («lunedì», Noord back to school), Oct 20 = Tuesday («martedì», trends snapshot), Oct 21 = Wednesday («mercoledì», Feyenoord), Oct 22 = Thursday («giovedì», Ajax), Oct 24 = Saturday («sabato 24 ottobre», family day), Oct 25 = Sunday («Domenica 25 ottobre», wintertijd 03:00→02:00), Nov 1 = Sunday («domenica 1º novembre», Robinson start). All correct. Dutch-side dates are frozen from the proofread core. Arithmetic in notes carried over unchanged from the core (301.000 + 246.000 = 547.000; 750.000 − 547.000 ≈ 203.000; 60.500 ÷ 6.600 ≈ 9+; 19,50 + 19,50 + 32,50 = 71,50).

## 11. Deliverables (files/weekly-report-nl-it/)

- svg/ ×8, cards/ ×8 (1950×2700 PNG).
- Print PDF: De-Lucerna-VOL1-IT.pdf — **10,628,454 bytes, sha256 6f5126998ef7d56a81b70e6f1955a0caab0b21d9c9cd2660b9800af396f42473** (8 pages).
- Web PDF: De-Lucerna-VOL1-IT-web.pdf — **3,694,236 bytes (< 10 MB), sha256 9c271172c1431f1a0c5501c5ad3175229acfa378a79bd50c0d4eb20aea278e38** (8 pages).

## 12. Independent proofread record (2026-10-21, independent proofreader — not the builder)

**VERDICT: PASS — one complete independent pass, ZERO problems. No fixes were needed; nothing was re-rendered. The edition is final with the §11 pins.** Every builder claim was re-derived independently (own extraction, own registry dumps from fresh scratch builds, own audit implementation); scratch kept in hidden_files/proof-nl-it/scratch/. The core was only ever rebuilt from a copy with output paths repointed at scratch; the core's 8 shipped SVG hashes were verified against §1 at the start AND at the end of this pass — all unchanged.

1. **Baseline** — a scratch copy of the unmodified core build reproduced all 8 shipped core SVGs byte-identically (8/8, hashes = §1 table). A scratch run of the IT build reproduced all 8 shipped IT SVGs byte-identically (8/8), so the build source is the shipped artifact and source-level diffs are true diffs. Both runs: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE warnings.
2. **Freeze** — source string-literal diff (all 5 content files): every removed non-CJK string is a gloss (Dutch headword + explanation), a fullwidth→halfwidth punctuation normalisation, or the OUT path; ZERO Dutch strings changed; ZERO CJK strings added. Numeric-literal diff: identical everywhere except content12 masthead furniture (subtitle 40→36 px, pairing-badge line) and content8's three documented answer-typesetting parameters (13.5→13.0, 1.16→1.12, 0.5→0.4). Rendered-text multiset diff: P1–P7 removals are 100% CJK-containing elements; P8's 10 non-CJK removals are the same note punctuation/gloss normalisations plus one wrap-point fragment (typesetter element split; the printed entry itself matches the registry exactly). bslib4 diff = footer furniture + `expl()` rename + «Nota — » prefix only; svglib diff = one code comment.
3. **Keys** — registry diff (fresh dumps, both builds): page/level identical ×150; type labels map 1:1 with identical counts (Completa la frase 66 · Scelta multipla 45 · Cloze 13 · Abbinamento 8 · Forma la frase 7 · Vero o falso 6 · Traduzione 4 · Scrittura 1); **key diff = exactly {137, 138, 150}**: #137 «Domenica l'orologio torna indietro: un'ora di sonno in più!» (faithful to the Dutch P1 band sentence, its stem), #138 «Il tuo telefono e il tuo computer cambiano l'ora da soli.» (faithful to the P2 original «Je telefoon en je computer veranderen de tijd zelf.»), #150 apparatus Italian. **#139/#140 keys byte-identical Dutch** («De Dutch Design Week is in Eindhoven.» / «Zondag heb ik een uur langer geslapen.»), their printed P8 stems re-aimed in Italian as documented. All 150 keys independently re-derived from the Dutch text during a full read of all 8 pages — all correct, arithmetic included (301.000+246.000=547.000; 750.000−547.000≈203.000; 60.500÷6.600≈9,17, keyed «9» with note «più di 9 volte»; 19,50+19,50+32,50=71,50; 17–25 Oct = 9 days). Notes differ for 146 items; the 4 identical notes are exactly {12, 46, 79, 84}, all language-independent (times/arithmetic/a Dutch conjugation arrow). No empty keys or notes.
4. **Printed-note set equality (mandatory gate)** — sequence-aware parse of both shipped P8 SVGs: core prints notes for {1..150}, this edition prints notes for {1..150} — **SETS EQUAL (150 = 150)**. The only non-dash entry is #150, which uses the ✓-note form in BOTH editions. Every printed IT entry matches the IT registry (key + dash + note) exactly, all 150.
5. **Totals** — 150 exercises, A2 42 · B1 76 · B2 32, per page 10/18/18/18/18/18/12/38, numbering continuous 1–150, writing model 87 words. Text volume (my extractor, calibrated to the core KIT's measure): core 29,851 no-space chars (= core KIT's figure), IT 35,404 (= §2's figure).

6. **P7 phrases** — the 8 quote strings are identical between the two editions and each occurs exactly 2× in the full-issue text of BOTH editions (source page + P7); verbatim-contiguous against their source pages, page tags (Pagina 1, 2, 2, 3, 4, 5, 6, 6) all correct.
7. **Calendar** — verified with `date` (Europe/Amsterdam): Oct 17 Sat, Oct 19 Mon, Oct 20 Tue, Oct 21 Wed, Oct 22 Thu, Oct 24 Sat, Oct 25 Sun, Nov 1 Sun. Every weekday claim in the Italian layer is correct (incl. «sabato 17 ottobre», «lunedì» Noord back-to-school, «martedì» trends snapshot, «mercoledì» Feyenoord, «giovedì» Ajax, «sabato 24 ottobre» family day, «Domenica 25 ottobre» wintertijd 03:00→02:00, «domenica 1º novembre» Robinson 20:00 RTL 4). Wristler attribution (published 20 Oct 2026, data = last October's searches) is stated consistently in the Dutch text, the chart caption and the Italian caption.
8. **Furniture** — P1 badge verbatim «TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»; pairing footer + «Pagina N di 8» on all 8 pages; gloss prefix «Nota — » on all 9 gloss boxes; masthead «De Lucerna». Builder width figures independently reproduced with the elements' true font parameters: badge 840.9 (slot 1820), subtitle 1764.8 @36 px (slot 1820), footer 908.0 (slot 1560), P1 trends footnote 327.4 (slot 390), P6 box title 363.7 @21 px bold (slot 390), ZO ONTHOUD title 391.0 (slot 398), PAS OP title 346.6 (slot 390) — all fit.
9. **Geometric occlusion audit (proofreader's own implementation)** — paint-order parse, PIL real-font glyph boxes (build's own font files/SC indexes), ink band baseline −0.88em/+0.30em, line boxes expanded by half stroke width, box-title-vs-border test in both paint orders. **Positive control: all 6 planted classes fired (COVER/LINEX/FOOTER/EDGE/BORDER/TEXTX), clean text silent.** Real run: IT edition 23 flags, core 23 flags — NO COVER, NO LINEX, NO EDGE in either. The 16 per-edition FOOTER flags are the pages' own footer lines (baseline 2624, below the 2580 rule by design; identical in the core). Remaining flags, all pixel-adjudicated on the shipped cards:
   - P1 masthead TEXTX (both editions): wordmark ink rows 140–265, subtitle ink rows 303–329 → 37 empty rows between. Non-defect (band-model artifact), matching §7's figures exactly.
   - P1 word-of-week Italian gloss (2 lines, IT only): line 1 descender ink ends row 1850, the full-width rule occupies rows 1852–1853 with row 1851 fully empty; line 2 ink ends row 1871, row 1872 fully empty, the IN HET KORT box top border occupies rows 1873–1874. No ink contact at either interface (1-row clearance each). Non-defect — tight but clear.
   - P2 «adviesdata: scholen mogen afwijken.» vs its facts-box bottom edge (y=993) and P3 «Kaartjes: € 32,50; studenten € 19,50.» vs its box edge (y=1235): the 'j' descender tip reaches the border row with 2 dark px ON the row (993 / 1235), zero ink below it; the text is painted over the hairline, fully legible; the pixel pattern is IDENTICAL in the frozen core (inherited sub-pixel grazes, already through the core's own proofread + programme audit). Non-defects.
   - P5 «start zondag 1 november, 20:00 uur.» vs box edge 932: ink ends row 931 — clear (both editions). P2/P5 Italian EN JIJ closing lines vs their (taller) box bottom edges: ink ends 1377 vs edge 1383 and 1255 vs 1261 — 5 rows clear each. Non-defects.
   - P7 col-3 stack: the letters-box bottom edge is y=1678.5 in the SVG of BOTH editions (builder claim confirmed geometrically, not just visually); the quotes rule is at y=1698; last col-3 ink row on the card is 1664. Clear.
   - **P8 answer block — the decisive pixel test.** Every consecutive line pair in all 4 answer columns was measured on the shipped card within the pair's true x-overlap strip (173 logical lines = 150 entries + 15 wrapped continuations + 8 page headers). The 6 tightest pairs have ink rows on ADJACENT rows (upper line's ink ends row r, lower line's ink starts row r+1 — clearance 0 empty rows); **no pair anywhere shares an ink row → 0 shared ink pixels**, confirming §7's substance (conservative bands touch by ≈0.44 px; real ink never meets). All other pairs have ≥1 empty row. The block's lowest ink is ≈ row 2547 (column 3, #119); rows 2548–2579 are empty across the whole content width — ~33 rows clear of the footer rule at 2580. §6's "flow ends y=2340" is the final column's flow end (last baseline 2325.4 + descent), consistent with the render.
10. **Images/credits** — base64 payloads byte-identical to the core per page (1/1/2/1/1/0/0/0); all 6 printed credits match the placed images and the core KIT (Westertoren CC0; pocket watch CC0; Kinderdijk CC0; herfstbos CC0; elftal 1912 public domain — printed «publiek domein»; canal boat CC0).
11. **Scans** — CJK characters in the final SVGs: 0 (raw bytes and text layer). The intermediary-layer term (both forms): 0 occurrences in the paper, this KIT, and the operative build code (bslib4/content*/svglib/render — the helper is `expl()` throughout). Hygiene note, not an edition defect: the builder's one-off checker script scratch/verify.py quotes both forms as search patterns for its own scan (same pattern adjudicated in the EN×IT proofread); the operative code is clean.
12. **PDFs (measured by the proofreader)** — web PDF De-Lucerna-VOL1-IT-web.pdf: **3,694,236 bytes, sha256 9c271172c1431f1a0c5501c5ad3175229acfa378a79bd50c0d4eb20aea278e38** (< 10 MB), 8 pages; print PDF De-Lucerna-VOL1-IT.pdf: **10,628,454 bytes, sha256 6f5126998ef7d56a81b70e6f1955a0caab0b21d9c9cd2660b9800af396f42473**, 8 pages — both exactly as §11 claims. Cards: a fresh CairoSVG render of the shipped P7 SVG is pixel-identical to the shipped card (max diff 0); P7 and P8 cards visually inspected in full — clean.

**Cleared for repo insertion** as slug 2026-w43-nl-it with the §11 pins above. (Independent proofreader; no repo insert, no posts made — per scope.)
