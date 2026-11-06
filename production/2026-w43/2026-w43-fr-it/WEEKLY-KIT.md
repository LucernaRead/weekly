# Le Lucerna VOL.2 — French text · Italian explanations (FR × IT)

Week 2026-W43 · Mon 19 – Sun 25 October 2026 · 8 pages · 1950×2700
Pairing: French target text (frozen VOL.2 core) + all explanations in Italian.
P1 badge: «TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»

## 1. Baseline proof (method gate)

The build dir `hidden_files/weekly-report-fr-it-build/` is a copy of the frozen
core build dir (`hidden_files/weekly-report-vol4-build/`). Run UNMODIFIED with
only its output path redirected, it reproduced all 8 shipped core SVGs
byte-identically (sha256, 8/8):

| page | sha256 |
|---|---|
| p1-une | 5f1dc8a12056a93ee851f2be3164efc1a364d918f80db2e84670862e0915cb92 |
| p2-vie | b99e94bea2216ee90bb725734748d013b40632d5786e8cc2b7613f20c567b17c |
| p3-culture | cb4dc01ed3479e8dccebde152dc10f413ada9f79c442eaffbfa4f8491b5fc0fc |
| p4-sport | 14b128b78c179cdec00c0e9d664db68465714391be7d1ded15ffeabcb6515ad8 |
| p5-jeunesse | f2d679f3a006d66ce9fd65ae7d9f73e829618a854f35a35dfdda90ff6048581c |
| p6-politique | 82021a2baf6cbbd3fb848c5be6624785e0bfb3ae697fd99d5d5237bec44c2200 |
| p7-langue | cb2bfc1c15d36d8eac9043ca0d7b342fa94eec9226cfd73b1a77c130ff14fa8c |
| p8-exercices | 5ac98ee139a1b479bcec36a143f72634f80e6196e09e9b685ccbfff464ec8f47 |

Only then was the explanation layer rewritten. `svglib.py` remains
byte-identical to the core.

## 2. Totals (verified programmatically against the core registry)

- Exercises: **145** — A2 55 · B1 65 · B2 25; per page 10 / 16 / 18 / 18 / 17 / 18 / 11 / 37.
- Registry meta (n / page / level / type): identical to the core for all 145 items.
- Printed P8 answer notes: **67** — exactly the core's printed set, reproduced via an
  explicit PRINT_NOTES set computed from the core registry by the core's own rule
  (page 8 always, or note ≤ 10 chars, or chart/error-correction types):
  {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56, 65, 71, 72, 73, 74, 80, 81, 82,
  83, 84, 85, 92, 97, 105–145}. Verified in the rendered P8: all 67 present with a
  space before each half-width parenthesis; no other notes printed (one apparent
  extra, #16, is a string collision — its note text equals #118's printed note).
- Build log: zero FLOW OVERFLOW warnings; the only warning is the core's inherited,
  previously adjudicated P4 head width note (frozen French headline).

## 3. Key-diff registry (complete)

Programmatic registry diff vs the core: keys differ for exactly 5 items; notes
differ for 122 items (121 Chinese notes translated into Italian + #119, a
French-only note whose full-width parentheses were normalised to half-width).
All other 140 keys are byte-identical to the core.

| # | change |
|---|---|
| 71 | French model answer unchanged; apparatus suffix «（参考答案）» → « (risposta modello) » |
| 72 | same as #71 |
| 73 | same as #71 |
| 132 | key → Italian translation «Leggere un sondaggio è già fare politica.»; stem re-aimed «Traduci in italiano: « Lire un sondage, c'est déjà faire de la politique. »» |
| 133 | stem re-aimed «Traduci in francese: È più alto di suo fratello.»; French key byte-identical |
| 134 | stem re-aimed «Traduci in francese: Gli studenti sono in vacanza da sabato.»; French key byte-identical |
| 135 | stem re-aimed «Traduci in francese: Stasera spostiamo gli orologi indietro di un'ora.»; French key byte-identical |
| 145 | key → Italian apparatus «Domanda aperta — i punti sono nel riquadro di scrittura e il modello è nel riquadro MODÈLE di questa pagina»; note → «si valuta in base ai punti» |

## 4. Italian-column furniture (ESTABLISHED PATTERN — reuse verbatim for ×IT)

- P1 badge (brick slot under the countdown band):
  «TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»
  (for other targets, substitute the target name from the list below)
- Footers: «Le Lucerna · SETTIMANALE FRANCESE VOL.2 · TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»
- Gloss prefix: «Nota — »
- Masthead: «Le Lucerna» exactly as the core ships.
- P1 strap: «HEBDOMADAIRE EN FRANÇAIS · OGNI SETTIMANA · IL FRANCESE CHE LEGGONO I FRANCESI»
- P1 subtitle: «SETTIMANALE IN FRANCESE · VOL.2 · AUTUNNO E FESTE»
- P1 contents-box head: «DANS CE NUMÉRO · SOMMARIO» (short variant — the literal
  «IN QUESTO NUMERO» overflows the 434 px box at 24 pt bold: 488.7 px measured;
  SOMMARIO = 380.1 px)
- P1 trends-box source line: «Le ricerche della settimana · Google Trends»
  (the full «… · Google Trends Francia» = 461.3 px and spills the 434 px box;
  "France" is preserved in the French source line printed directly below)
- Section-head suffixes: exercises «À VOUS! · TOCCA A TE»; vocab boxes «· LESSICO»;
  debate «LE DÉBAT · IL DIBATTITO»; drills «MICRO-DRILLS · ALLENAMENTO»;
  level heads «NIVEAU A2 · LIVELLO BASE» / «NIVEAU B1 · INTERMEDIO» / «NIVEAU B2 · SFIDA»;
  toolbox «BOÎTE À OUTILS · STRUMENTI»; clinic «CLINIQUE DES ERREURS · CLINICA»;
  graph «LIRE LE GRAPHIQUE · IL GRAFICO»; calendar «DATES À RETENIR · IL MESE»
- P8 heads: «A · TEXTE À TROUS · COMPLETA» / «B · CHOIX MULTIPLE · OPZIONI» /
  «C · LECTURE · LETTURA» / «D · PHRASES · COSTRUISCI FRASI» /
  «E · TRADUCTION · TRADUZIONE» / «F · LES MOTS · VOCABOLARIO» /
  «G · DIALOGUE · DIALOGO» / «H · ÉCRITURE · SCRITTURA» / «MODÈLE · MODELLO» /
  keys head «RÉPONSES · TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)»;
  page separators «— PAGINA {n} —»
- Instruction verbs: Completa / Riscrivi / Correggi / Abbina
- Italian target names for the column: INGLESE, TEDESCO, FRANCESE, SPAGNOLO,
  PORTOGHESE, OLANDESE, RUSSO, GIAPPONESE, COREANO, CINESE SEMPLIFICATO,
  CINESE TRADIZIONALE
- The one P6 level head that follows the pattern but must fit the narrow strip:
  «NIVEAU B1 · INTERMEDIO» («LIVELLO INTERMEDIO» = 463.9 px > 434 px box).

## 5. Freeze check (text-node diff vs core SVGs)

Every core text node absent from this edition's render is (a) Chinese explanation
text or its punctuation, (b) the documented #132 stem, or (c) a re-wrapped
answer-key line whose registry content is proven identical (§3). No French target
text outside the registry was lost or altered. `svglib.py` byte-identical;
per-file code diff touches only explanation strings, furniture, the footer
function, and the explanation-method name (renamed to `expl()`).

Scans of the final SVGs: CJK characters = 0 (text layer and raw bytes, all 8
pages); the intermediary-layer term = 0 occurrences (paper, this KIT, build code).

## 6. Defects found by the builder and fixed (wording only, geometry frozen)

1. **P1 contents-box head overflow (real defect)**: «DANS CE NUMÉRO · IN QUESTO
   NUMERO» at 24 pt bold measured 488.7 px from x=1473 — past its box (right edge
   1885.7) and past the page edge (ink to 1961.7). Shortened to «DANS CE NUMÉRO ·
   SOMMARIO» (380.1 px). Rebuilt; audit clean.
2. **P1 trends-box source line spill (real defect)**: «Le ricerche della settimana ·
   Google Trends Francia» at 19 pt measured 461.3 px, ink ending 1934.3 — 48.6 px
   past its box's right border. Shortened to «Le ricerche della settimana · Google
   Trends» (392.2 px). Rebuilt; audit clean.
3. P1 headline gloss: the core's full gloss overflows the headline flow in this
   column (as in the Spanish column); the compressed gloss is used (the
   «présidentielle» gloss dropped; the word is glossed again on page 6). No
   overflow in the final build log.
4. P2 «ET VOUS?» box: the Italian reader rendering is kept to the core's 2-line
   measure; the box bottom lands at the core's exact y=1548.95.

## 7. Geometric occlusion audit (mandatory gate)

Script `audit_fr_it.py` (paint order, real-font PIL metrics, line boxes expanded
by half stroke width). Synthetic positive control: PASS (COVER / LINEX / FOOTER /
TEXTX all fire; clean page silent).

First run on this edition: 5 flags. The 2 wording defects of §6 were fixed and
re-audited away. Remaining 2 flags, both core-inherited geometry, pixel-adjudicated
on THIS edition's render:

- P1 TEXTX masthead «Le Lucerna» vs subtitle: measured ink clusters rows 230–265
  (masthead) and 295–330 (subtitle) in the shared x-span — 29 empty rows between.
  NON-DEFECT.
- P4 TEXTX band «Le Lucerna» vs band line «NIVEAU B1 · NBA · Wembanyama»: ink
  clusters rows 89–115 and 126–146 — 10 empty rows between. NON-DEFECT.

Final state: **0 unresolved flags.**

## 8. P7 phrases of the week

The 7 phrase strings are byte-identical to the core (French target text is never
edited in a fan-out). Occurrence counts across the issue match the core exactly
(2 / 3 / 2 / 1 / 1 / 2 / 1, in printed order), and page tags are the core's.
Note, inherited unchanged from the core: the phrases are the core's own condensed
form of its article sentences (e.g. the page-2 article reads «…à trois heures du
matin, les horloges reculent : il est deux heures.» where P7 prints «À trois
heures, il sera deux heures.»). The fan-out preserves the core's disposition.

## 9. Images (all public domain; credits as printed, from the core KIT)

- P1: Utagawa Hiroshige (1797–1858), maple print — «estampe, domaine public · LACMA»
- P2: Eugène Atget (1857–1927), Paris photograph — «photographie, domaine public»
- P3: Flora de Filipinas (Blanco), 19th-century botanical plate — «domaine public»

## 10. Dates and facts spot-verified against the real 2026 calendar

Sun 25 Oct 2026 = EU winter-time change (3 h → 2 h) · Sat 17 Oct holidays begin ·
Mon 2 Nov classes resume · Sat 24 Oct (dialogue) · Sat 31 Oct Halloween ·
Sun 1 Nov Toussaint (#109 key C = dimanche) · chart 28+24+17+11+9+11 = 100 ·
#81: 28−24 = 4 · #84: B 27 > A 26 · #85: 52 % · Parker titles 2003/2005/2007/2014.

## 11. Deliverables

- `svg/` ×8, `cards/` ×8 PNG (1950×2700)
- Print PDF: `lucerna-fr-it-print.pdf` — 9,775,979 B — sha256 7ea801ffabd35dd9714f094e65feaa61aec827c109645ed7f9860a3871138bfd
- Web PDF: `lucerna-fr-it-web.pdf` — 7,219,575 B (< 10 MB) — sha256 5aab71bd68c3c3c5b1f35b79cd53c6427bd8835de1ba98740960e628c86f30a7
- VOL.3 teaser carried in Italian, substance unchanged (Halloween Sat 31 Oct,
  Toussaint Sun 1 Nov, first week of winter time).

## 12. Proofread status

- Builder's full proofread: DONE — all 8 pages read end-to-end in the render;
  all 145 keys re-derived and matched to the registry; dates, totals, printed
  notes, phrases verified as recorded above.
- Independent proofread: **DONE — PASS (zero problems)**. Full independent pass
  by a fresh proofreader who did not build this edition; evidence below.
  - Reproduction: core and fan-out rebuilt from source in a scratch copy —
    both byte-identical to the shipped SVGs, 8/8 each; build logs clean
    apart from the inherited P4 HEAD TOO WIDE warning (frozen core item).
  - Registry diff: item meta (number/page/level/type) identical for all 145;
    levels A2 55 · B1 65 · B2 25; key diffs exactly {71, 72, 73, 132, 145};
    note diffs 122; stems #133/#134/#135 re-aimed into Italian with the
    French keys byte-identical. No French target-text change anywhere
    (svglib and layout code identical; every content-code delta classified
    as explanation layer, pairing furniture, or a documented registry item).
  - Printed-note set equality (decisive check for this core): the core's
    printed set was recomputed from the core registry using the core's own
    print rule — 67 items {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56,
    65, 71–74, 80–85, 92, 97, 105–145}. The fan-out's explicit PRINT_NOTES
    set equals it exactly, and the rendered P8 answer block equals an
    independent simulation from the fan-out registry character-for-character
    (whitespace-normalised): the paper prints exactly the core's 67 notes,
    no drops, no extras. The #16/#118 identical note strings were resolved
    by number: #16 prints without the note, exactly as the core rule gives.
  - Keys: all 145 re-derived from the French text (the P8 battery solved
    item by item; chart re-added 28+24+17+11+9+11 = 100; #81: 28−24 = 4;
    #84: B 24+3 = 27 > A 28−2 = 26; #85: 28+24 = 52 %). #132's Italian key
    verified as a faithful translation of its printed French stem. The
    VOL.3 teaser is carried in Italian, substance unchanged.
  - P7 phrases: byte-identical to the core with the same page tags;
    whole-issue occurrence counts match the core exactly (2/3/2/1/1/2/1).
  - Calendar verified against the real 2026 calendar: Sat 17 Oct (holidays
    begin), Sat 24 Oct (dialogue), Sun 25 Oct (clock change 3 h → 2 h),
    Sat 31 Oct (Halloween), Sun 1 Nov (Toussaint), Mon 2 Nov (classes resume).
  - Italian apparatus: CJK characters = 0 in all 8 SVGs (raw bytes and text
    layer); every explanation element read in Italian; gloss prefix
    «Nota — » throughout.
  - Furniture: P1 pairing badge verbatim; pairing footer and «Pagina N di 8»
    on all 8 pages; masthead «Le Lucerna» as shipped.
  - Geometric occlusion audit (proofreader's own implementation — paint
    order, real-font glyph metrics, line boxes expanded by half the stroke
    width; validated on a synthetic positive control, 5/5 planted defects
    caught): exactly 1 flag in the whole edition — the P1 masthead/subtitle
    band overlap, inherited from the core (the core shows the same single
    flag) and pixel-adjudicated on the shipped card: masthead ink rows
    180–265, subtitle ink rows 295–330, 30 rows of clear air — non-defect.
    The two builder-fixed P1 spots re-measured on the shipped SVG:
    contents head 380.1 px, ink ends x=1853.1 < box edge 1870; trends source
    line 392.2 px, ends 1865.2 < 1870. No cover, edge, footer-band,
    box-spill, or line-crossing flags anywhere.
  - Images: embedded payloads byte-identical to the core per page; credits
    as §9 (Hiroshige · LACMA; Atget; Blanco plate — all public domain).
  - PDFs measured by the proofreader: web 7,219,575 B, sha256
    5aab71bd68c3c3c5b1f35b79cd53c6427bd8835de1ba98740960e628c86f30a7;
    print 9,775,979 B, sha256
    7ea801ffabd35dd9714f094e65feaa61aec827c109645ed7f9860a3871138bfd.
  - Banned-term scan (the banned intermediary-layer term, Chinese and
    English forms) over paper, this KIT, and build code: 0 hits.
  - Documentation correction (paper unaffected): §6 item 3 above says the
    dropped «présidentielle» gloss is "glossed again on page 6" — it is not;
    no Italian gloss of the word exists on page 6 (French occurrences only).
    The shortening itself stands as an acceptable, disclosed compression:
    the word is a transparent cognate, and page 1 itself renders the phrase
    in Italian («i sondaggi sulle presidenziali 2027» in the trends line;
    «il mandato presidenziale» inside the same gloss). No paper change.
