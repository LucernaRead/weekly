# WEEKLY-KIT — La Lucerna · ES × IT (Spanish text · Italian explanations)

**Edition:** Spanish target text (frozen VOL.1 core) with ALL explanations rewritten in Italian, for Italian-speaking readers.
**Pairing:** target = Español (es) · reader native = Italiano (it). VOL.1 · Week 19–25 October 2026 (W43).
**Masthead:** La Lucerna (exactly as the core ships).
**Build dir:** `hidden_files/weekly-report-es-it-build/` · **Deliverables:** `files/weekly-report-es-it/` (svg/ ×8, cards/ ×8 at 1950×2700, print PDF, web PDF).
**Method:** fan-out per SOP — core build copied, baseline proven byte-identical, only the explanation layer rewritten. The explanation method in the code is named `expl()` throughout; explanations are written directly in Italian, one-to-one with the Spanish text. The intermediary-layer term occurs 0 times in paper, this KIT, and code (grep-verified; the term itself is not quoted here). Zero CJK characters in the final SVGs (grep-verified).

## 1. Baseline proof (before any edit)

The unmodified copy of the core build (`hidden_files/weekly-report-es-build/`) reproduced all 8 shipped core SVGs **byte-identically (sha256 8/8)**:

| Page | Core SVG sha256 |
|---|---|
| p1-portada.svg | 41f0d53fb25d94a3a20cd3c344ed8bc20a317521cb357523a94e8f8698f31805 |
| p2-vida.svg | 42f8603df3d543600b42be7854b4660e027130e1bea4941492c8a88d1d1981be |
| p3-cultura.svg | ba31dbb02d0674fa36c55d9d76bb4a3448bfcf73bfefcc3c63bbafe344ecb074 |
| p4-deporte.svg | 524ad07ba7321817096c9720d91a844f5d54b772780a80032114f36312c84fe0 |
| p5-juventud.svg | bf2a0790568d5ee74d5a97ea7e6f68d9e6618f64caf6633eba6426432ea32466 |
| p6-afondo.svg | b99e70a088e950b58f23f69f36b007bd4a85f3596eebcacfa8d0ddb63455c818 |
| p7-lengua.svg | 26432db2af5b6b97f90aa780cf0d93e1d82319b0282b3a4ebf89a0266b32285e |
| p8-ejercicios.svg | 229b1b134cf77d4fafae8c7f5a871e25dd3a5186c57fa45c751909f8fc204cc3 |

The corrected P5 wording «desde el **viernes** 23» (2026-10-23 is a Friday) is present in the shipped core P5 SVG (1 occurrence) and in this edition's P5, unchanged.

## 2. Totals (identical to core)

- **150 exercises** — A2 52 · B1 70 · B2 28; by page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- 8 pages, 1950×2700, 4 columns, warm ivory — layout geometry frozen from the core.
- Build log final state: zero FLOW OVERFLOW / HEAD TOO WIDE warnings.

## 3. Key-diff registry (complete)

Only translation-type items re-aim at Italian. Every other key (145 of 150) is byte-identical to the core.

| # | Change | Core | This edition |
|---|---|---|---|
| 137 | Key becomes Italian (stem stays Spanish «El domingo dormimos una hora más.») | Key = the Chinese translation; note «confronta…» in Chinese | Key «La domenica dormiamo un'ora in più.» · note «confronta con l'originale» |
| 138 | Key becomes Italian (stem stays Spanish «El lunes es festivo en nueve comunidades.») | Key = the Chinese translation | Key «Il lunedì è festivo in nove comunità.» · note «confronta con l'originale» |
| 139 | Stem re-aimed to Italian; Spanish key byte-identical | Stem in Chinese | Stem «Il Clásico si gioca domenica alle nove di sera. → ___» · key «El Clásico se juega el domingo a las nueve de la noche.» (unchanged) · note «se juega = si gioca, si disputa» |
| 140 | Stem re-aimed to Italian; Spanish key byte-identical | Stem in Chinese | Stem «Ogni grafico deve indicare la sua fonte. → ___» · key «Cada gráfico tiene que llevar su fuente.» (unchanged) · note «tener que = dovere» |
| 150 | Apparatus (writing exercise) | Key/note/instr in Chinese | Key «(domanda aperta — il modello è qui sotto)» · note «Il modello è nella sezione H di questa pagina (82 parole)» · instr «Scrivi» |

Documented apparatus normalisations outside the registry (not keys): P5 stems #71/#72 parenthetical «(原形 buscar/estrenar)» → «(infinito: buscar/estrenar)»; P7 reader's-letter parenthetical normalised to half-width parentheses; all notes use half-width parentheses with a space before each note parenthesis in the P8 key flow (`n. key — nota` line style, as in the ES×FR / ES×DE siblings). Instruction words localised throughout: Completa · Vero o falso · Costruisci · Riscrivi · Traduci · Scrivi · Abbina le parole.

## 4. Italian furniture (verbatim, as printed)

- P1 pairing badge (brick slot, y=574): «TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»
- Footers (all pages): «La Lucerna · SETTIMANALE SPAGNOLO VOL.1 · TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»
- Gloss prefix: «Nota — »
- P1 strap: «CADA SEMANA EN ESPAÑOL · OGNI SETTIMANA · LO SPAGNOLO DEGLI SPAGNOLI» — **deviation (recorded):** the fuller wording («…LO SPAGNOLO CHE LEGGONO GLI SPAGNOLI», 931 px at 21 pt) collided with the right-anchored date line (starts x=1419); shortened by wording only.
- P1 band right lines: «DOMENICA · UN'ORA DI SONNO IN PIÙ» / «Tre appuntamenti in una notte · pagine 2 e 4» — **deviation (recorded):** the first wording («QUESTA DOMENICA · …») overlapped the frozen Spanish band headline (ends x=1343); shortened by wording only.
- P1 line under masthead: «SETTIMANALE IN SPAGNOLO · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1»
- Band titles: «VIDA · VITA QUOTIDIANA» · «CULTURA · CULTURA» · «DEPORTE · SPORT» · «JUVENTUD · GIOVENTÙ» · «A FONDO · APPROFONDIMENTO» · «LENGUA · LA LINGUA» · «EJERCICIOS Y RESPUESTAS · ESERCIZI E RISPOSTE»
- Exercise headers: «EJERCICIOS · ESERCIZI · PAGINA N» + right line «Risposte a pagina 8 · livelli misti: cerca per numero»
- P8 answers header: «RESPUESTAS · LE RISPOSTE — ordinate per pagina: cerca il numero» / «Una nota in italiano per ogni risposta · ✓ = testo modello»
- Width-driven shortenings (wording only, geometry untouched): P1 sidebar heads «Cinque chiavi · Para entender la semana» and «EN ESTA EDICIÓN · IL NUMERO»; P2 box title «LA FRASE · DA RICORDARE»; P3 section head «RECORDAR · RICORDARE INSIEME»; P7 box title «ERRORES TÍPICOS · ERRORI TIPICI».

## 5. Printed-note set verification

The core prints ALL 150 P8 notes (print-all rule). Verified **in the rendered P8 SVG** (not only the registry): entries 1–150 all present, every entry carries its note, and the printed key set matches the core's by number. Key-part diffs vs core = exactly {137, 138, 150} (see registry). **Set equality: PASS (150/150).**

## 6. Builder's proofread (own pass; independent proofread completed — see §11)

- Read all 8 pages end-to-end in the rendered cards. Spanish target text frozen (text-multiset diff vs core: every difference is explanation layer / pairing furniture / documented registry items; the one Spanish line whose wrap point moved, P5 #72 stem, is textually identical).
- All 150 keys re-derived against the Spanish texts; levels/totals identical to core; goals total 40 (P4) unchanged in the frozen text.
- P7 phrases of the week: all 8 are verbatim contiguous excerpts, each occurring exactly 2× in the full issue — identical counts to the core; page tags (Página 1/2/2/4/3/3/5/6) match the core's.
- Weekday/date claims verified against the real 2026 calendar: viernes 23 Oct ✓, sábado 24 ✓, domingo 25 (Clásico 21:00, clock change) ✓, jueves 29 ✓, sábado 31 (Halloween) ✓, domingo 1 Nov ✓, lunes 2 Nov ✓, domingo 29 Nov (elecciones) ✓, domingo 28 Mar 2027 ✓.

## 7. Geometric occlusion audit (mandatory gate)

Script: `audit_es_it.py` (paint-order SVG scan, real-font PIL/svglib metrics; ink band baseline −0.88 em…+0.30 em; line boxes expanded by half stroke width; checks COVER ≥30%, FOOTER ink >2580, EDGE spill, LINEX crossings, box titles vs borders by measurement). **Validated on a synthetic positive control first**: the control SVG (one covered text, one line-crossed text, one footer-intruding text, one clean text) produced exactly the 3 expected flags and no false flag.

Final run on the shipped SVGs: **2 flags, both pixel-adjudicated NON-DEFECTS** —
- P1 word-of-week Italian gloss, line 2 (baseline 1841.85) vs the pale rule at y=1844: measured glyph ink (incl. anti-aliased blends) ends at row 1841; rule occupies rows 1843–1844 → zero overlap. (The gloss was reworded so its second line carries no descenders: ««Fare ponte» (pagina 3): una festa vicina al fine settimana unisce tre soli in fila. Stavolta è diviso in due.»)
- P7 letter caption last line (baseline 1681.6) vs the FRASES section rule at y=1685–1686: measured ink ends at row ~1680 → ~4–5 rows clear. Same frozen adjacency as the core.

Defects found in the builder's pass and fixed **by wording only** (geometry untouched in all cases):
1. P1 strap overlapping the date line → shortened (§4).
2. P1 black-band Italian line overlapping the Spanish headline → shortened (§4).
3. P1 sidebar heads «Le cinque chiavi della settimana…» (spilled past page edge, x1=2002) and «EN ESTA EDICIÓN · IN QUESTO NUMERO» (past box border + 1 px past page edge) → shortened (§4).
4. P2 box title «LA FRASE PARA RECORDAR · DA RICORDARE» clipped by its box border (500 px vs ~390 budget) → «LA FRASE · DA RICORDARE».
5. P6 exercise flow overflow (Italian instruction lines for sections A/D wrapped longer; last items crossed the footer rule — the core ends at y=2562) → instruction lines shortened («Guarda i grafici e scegli la risposta giusta.»).
6. P7 box title «ERRORES TÍPICOS · ERRORI FREQUENTI» clipped at box border → «ERRORES TÍPICOS · ERRORI TIPICI».
7. P7 letters box: Italian note wrapped to 4 lines and its last line sat flush on the box's bottom border (baseline 1827.4, border 1833) → note shortened to 3 lines («Lettera di esempio, scritta dalla redazione. Nel VOL.2 le vostre lettere e i migliori testi di pagina 8 — scriveteci!»).
8. P8 answer-key flow overflow (Italian notes longer; col 3 ended y=2582 > 2552) → the 9 longest notes tightened (meaning preserved); final keys flow ends within bounds and prints exactly the core's note set.

## 8. Images (identical to the core; verified placed in the render)

| File | Content | Source | Licence |
|---|---|---|---|
| assets/atomuhr.jpg | NIST-F1 atomic clock (P1) | NIST — Commons File:Nist-f1.jpg | Public domain |
| assets/castanas.jpg | Street-roasted chestnuts (P3 Castanyada) | Wikimedia Commons — File:Sugar-roasted chestnuts (1).jpg | CC0 |
| assets/halloween1910.jpg | Halloween postcard, c. 1909 (P5) | Commons — File:1910 Halloween card with African American girl.jpg | Public domain |
| assets/kuerbis.jpg | USDA farmers-market pumpkins — reserve, unused (as in core) | U.S. Department of Agriculture | Public domain |

Full credit detail: build-dir `assets/CREDITS.md` (Commons API verification, 2026-10-21, from the core production). P2 clocks and P6 charts are program-drawn.

## 9. Deliverables & pins

| File | Bytes | sha256 |
|---|---|---|
| La-Lucerna-VOL1-IT-web.pdf | 3,917,512 | dc72dbc6b33291e0025ab2039ee27ac85e040ba45ed3cb8900aa8d64f760de5b |
| La-Lucerna-VOL1-IT.pdf (print) | 5,794,496 | 229224eba6a9e18c091469228d74dd285fe946dfd3133cd5e3df238c31b60cf7 |

Web PDF < 10 MB ✓ (Discord/repo limit). svg/ ×8, cards/ ×8 (1950×2700 PNG).

## 10. Status

- Builder's full proofread: DONE (this KIT, §6–§7).
- **Independent proofread: DONE — PASS (after proofreader fixes)** — see §11. The §9 PDF pins are superseded by the final pins in §11.

## 11. Independent proofread record (2026-10-21) — PASS after proofreader fixes

Fresh, skeptical pass; every builder claim verified independently (own baseline reproduction, own registry dumps, own text extraction, own geometric audit implementation validated on a synthetic positive control first). Proofreader scratch: `hidden_files/proof-esit-independent/`.

### Verified clean as shipped
- **Baseline**: an unmodified copy of the core build, run with outputs repointed to scratch, reproduced all 8 shipped core SVGs byte-identically (8/8, hashes = §1 table); the edition build likewise reproduces the shipped edition SVGs 8/8.
- **Totals**: 150 exercises (A2 52 · B1 70 · B2 28), per page 10/18/18/18/18/18/12/38, numbering continuous 1–150; build log 0 FLOW OVERFLOW / HEAD TOO WIDE.
- **Keys**: registry diff vs core = key changes exactly {137, 138, 150} and stem re-aims {139, 140}; 147/150 keys byte-identical; #139/#140 keys byte-identical to the core (also proven at the printed level). #137 «La domenica dormiamo un'ora in più.» and #138 «Il lunedì è festivo in nove comunità.» are faithful Italian renderings of their Spanish stems. All 150 keys independently re-derived from the Spanish texts in a full read of all 8 pages (incl. the P4 «40 goles» figure, chart sums 31,7+26,8+18,7=77,2, CIS/Demócrata bar proportionality ≈12 px/%, and the writing model = exactly 82 words, as printed in both editions).
- **Printed-note set equality — PASS**: both registries carry a note for every item (none empty); the printed P8 answer stream equals the registry stream entry-for-entry (1–149 verbatim; #150 follows the core's own ✓-marker print convention identically in both editions). Core printed set {1…150} = edition printed set {1…150}, EQUAL by number. The 9 tightened notes preserve meaning.
- **P7 phrases**: all 8 verbatim contiguous excerpts with correct page tags (1, 2, 2, 4, 3, 3, 5, 6); each occurs exactly 2× issue-wide (tagged page + P7), counts identical to the core.
- **Calendar**: every weekday/date claim verified against the real 2026 calendar (viernes 23 Oct — the corrected core wording, confirmed present in this edition's P5 article; sábado 24; domingo 25, Clásico 21:00 + clock change + F1 Austin; jueves 29; sábado 31; domingo 1 Nov; lunes 2 Nov; domingo 29 Nov; domingo 28 Mar 2027).
- **Italian completeness**: full read of all 8 rendered pages; every explanation element (Nota glosses, grammar summaries, instructions, apparatus, P8 notes) genuinely in Italian; zero CJK characters in all 8 final SVGs.
- **Furniture**: badge verbatim on P1; pairing footer + «Pagina N di 8» on all 8 pages; gloss prefix «Nota — ». Pixel/metric fits verified: P1 strap ink ends x=1379 vs date line starts 1419 (40 px clear); black-band Italian line starts x=1396 vs Spanish headline ends 1343; sidebar heads end 1839 / 1843 < 1885; P2 box title «LA FRASE · DA RICORDARE» ink ends 852 < box edge 961; P7 box title «ERRORES TÍPICOS · ERRORI TIPICI» ink ends 1870 < 1885; P6 exercise flow ends y=2562 (= core), P8 answer flow ends y=2502 — the builder's in-build fixes #1–#6 and #8 are confirmed effective.
- **Builder's 2 audit flags adjudicated NON-DEFECTS at pixel level**: P1 word-of-week gloss line 2 — edition ink ends row 1840, the pale hairline occupies rows 1843.4–1844.6, the visible rule is at row 1873 (the core's own gloss ink ends 1842 against the same hairline — identical inherited adjacency, zero overlap). P7 letter caption vs the FRASES rule — subsumed and eliminated by fix (a) below (caption moved up with the column stack; final audit shows no flag).
- **Images**: payloads byte-identical to the core per page (P1/P3/P5); printed credits match the core KIT table (NIST-F1 public domain, street chestnuts CC0, c.1909 Halloween card public domain) and the placed images.

### Defects found by this proofread and FIXED (explanation/furniture layer only; no geometry, no Spanish text, no key changes)
1. **P7 text-on-text collision (real defect, missed by the builder's audit).** The builder's geometric audit never tested text against text: the frozen phrase «España se divide en dos: unos hacen puente y otros, no.» (baseline 1787, ink to x≈1606) struck through line 3 of the letters box's Italian note. Root cause: the column-4 stack grew +111 px vs the core (LA PALABRA Italian summary 4 lines vs the core's 2; the letters note 3 lines vs 2; longer ERRORES summaries), pushing the letters box to y 1440–1804, into the phrase's line. Fixed by wording only: LA PALABRA summary → 3 lines («empatar = pareggiare: questa settimana due volte — Atlético a Stoccarda, Alonso e Sainz ad Austin, a pari punti.», meaning preserved) and the note → 2 lines («Esempio della redazione — nel VOL.2, le vostre lettere e i migliori testi: scriveteci!» — sample-letter attribution and the VOL.2 promise preserved; the «di pagina 8» locator survives in the frozen Spanish teaser on the same page). Letters box bottom 1804 → 1746; note last ink ≈1745 vs phrase ink top 1773 (≈27 px clear), pixel-verified on the re-rendered card.
2. **P8 top-right sub-line (freeze deviation, undocumented).** As shipped it read «VALUTAZIONE · LA GRANDE PROVA DELLA SETTIMANA + TUTTE LE RISPOSTE» — the frozen Spanish descriptor had been translated, while the core and all shipped ES siblings (FR/DE/EN) keep the Spanish descriptor and localise only the page marker. Restored to «Pagina 8 · La gran prueba de la semana + todas las respuestas».

After the fixes the edition was re-rendered from the operative build and **the entire pass was re-run from the top on the final artifacts**: only the P7 and P8 SVGs changed (P1–P6 byte-identical); registry identical (diffs still exactly {137, 138, 150} + stems {139, 140}); printed-note set still {1…150} = core; freeze diff re-classified (every remaining difference is explanation layer / pairing furniture / documented registry item — the P8 descriptor now matches the core verbatim); the proofreader's audit (paint-order, real-font metrics, line boxes expanded by half stroke width, box titles tested against their own borders, text-vs-text overlap scan) reports **zero unresolved flags and zero text-text overlaps** on P7 (the only remaining flags anywhere are the footer furniture itself, identical in the core, and the inherited P1 hairline adjacency adjudicated above). Core SVG hashes verified unchanged before and after all proofreader work.

### Documentation notes
- §6's claim that every text difference is explanation layer / furniture / registry items was inaccurate for the P8 sub-line (fixed above); §7's audit missed the P7 collision (no text-vs-text test — same blind-spot class previously caught in zh-CN×ES's titles). The intermediary-layer term occurs 0 times in the paper, this KIT, and the operative build code; two residual occurrences sit only in the one-off scratch transform script (`hidden_files/weekly-report-es-it-build/scratch/transform1.py`), as the search side of the method-rename quoting the frozen core's original calls — a builder-hygiene note, not an edition defect. The 2 CJK characters in this KIT are the quoted core string in §3 documenting a normalisation.
- Adjudicated acceptable: the P7 sub-line head «A2 → B2 ·» is the builder's furniture variant for the core's Chinese page-focus head (Spanish descriptor kept, Italian gloss kept); not a defect.

### Final pins (supersede §9)
| File | Bytes | sha256 |
|---|---|---|
| La-Lucerna-VOL1-IT-web.pdf | 3,914,495 | bbc029f0568281cf99930f135d500f147cc86f0e9afa030052a6e7487c8fd033 |
| La-Lucerna-VOL1-IT.pdf (print) | 5,794,180 | 59bafb50073cec69f9ca70b403972aca3835b4911c31616d4ec14497172ec8dd |

Web PDF < 10 MB ✓; both PDFs 8 pages; cards 8 × 1950×2700. Changed SVGs: p7-lengua.svg `7e55f143e46abdca25a16f686ef6c4cf3c50da7667e3da8ea2958af8315da2fa`, p8-ejercicios.svg `e4644ac033d7f3f34a1d604af7966fd0030b0f65b94680fe678b27907a8c6d50`; P1–P6 SVGs byte-identical to the builder's shipped set (§9-era hashes in the proofreader's scratch record). **The edition is final and cleared for repo insertion.**
