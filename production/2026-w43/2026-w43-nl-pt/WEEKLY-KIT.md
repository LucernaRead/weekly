# WEEKLY-KIT — De Lucerna VOL.1 · NL × PT (Dutch text · Portuguese explanations)

Fan-out edition of the frozen Dutch VOL.1 core: Dutch target text unchanged,
ALL explanations (glosses, grammar notes, instructions, exercise apparatus,
all P8 answer notes) rewritten in Brazilian Portuguese for Portuguese-speaking
readers. Issue week: Mon 19 – Sun 25 Oct 2026 (W43). 8 pages, 1950×2700.
Independent proofread: **PASS** (independent proofreader, 2026-10-21 — see §11).

## 1. Baseline proof (method step 1)
- The core build (`hidden_files/weekly-report-nl-build/`) was copied to
  `hidden_files/weekly-report-nl-pt-build/` and run UNMODIFIED with output
  repointed to `scratch/baseline-svg/`.
- Result: **8/8 shipped core SVGs reproduced byte-identically (sha256)**.
- After all work, the core's shipped SVGs were re-hashed and are UNCHANGED:
  p1 a8a2cc5d…, p2 ea3f2a18…, p3 b61fbb1b…, p4 eff31458…, p5 1098c657…,
  p6 c941eb44…, p7 097fcfa7…, p8 feba8026…. Core build dir untouched.

## 2. Totals (identical to core)
- **150 exercises — A2 42 · B1 76 · B2 32**; per page 10/18/18/18/18/18/12/38.
- By type: Complete a frase 66 · Escolha múltipla 45 · Associação 8 ·
  Verdadeiro ou falso 6 · Forme a frase 7 · Cloze 13 · Traduza 4 · Escreva 1.
- Writing model (#150): 87 words, as in the core.
- Transform method: every CJK-containing string constant of the core build was
  extracted by AST (285 distinct literals) and replaced via an authored map
  (`scratch/mapping.py`, coverage 285/285). The explanation method was renamed
  (no method name refers to an intermediary layer); the intermediary-layer term
  occurs 0 times in the paper, this KIT and the operative build code. One-off
  scratch transform scripts (`scratch/transform.py`) quote the core's original
  call strings as search patterns during the rename — confined to `scratch/`.
  Zero CJK characters in the final SVGs and in the operative build code.

## 3. Key-diff registry (complete)
Page/level metadata diffs vs core: **none**. Key diffs — exactly 3, all
translation items legitimately re-aimed at Portuguese:
- **#137 key** → «Domingo o relógio atrasa: dormir uma hora a mais!»
- **#138 key** → «O seu telefone e o seu computador mudam a hora sozinhos.»
- **#150 key/apparatus** → «(pergunta aberta — modelo abaixo)», note
  «Modelo na seção H desta página (87 palavras)»
Stems re-aimed (Dutch keys byte-identical):
- **#139 stem** → «A Dutch Design Week é em Eindhoven. → ___» (key: De Dutch
  Design Week is in Eindhoven.)
- **#140 stem** → «No domingo, dormi uma hora a mais. → ___» (key: Zondag heb
  ik een uur langer geslapen.)
All other 147 keys byte-identical to the core. Notes: 141 of 150 rewritten in
Portuguese; the 9 unchanged are language-neutral (pure numbers / Dutch time
equations): #12, #16, #18, #46, #79, #84, #101, #102, #120.

## 4. Printed-note set verification (mandatory gate)
Wrap-aware extraction from both shipped P8 SVGs, entries grouped across
wrapped lines: **core prints {1..150} in order; this edition prints {1..150}
in order — EQUAL.** The core's DASH style (`N. key — note`) is kept
throughout, including separators «— PÁGINA n —».

## 5. PT furniture (as shipped, verbatim)
- Masthead: «De Lucerna» (exactly as the core).
- P1 badge: «TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA
  OS LEITORES DE LÍNGUA PORTUGUESA»
- Footers: left «De Lucerna · SEMANÁRIO NEERLANDÊS VOL.1 · TEXTOS EM
  NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS», right «Página N de 8».
- Gloss prefix: «Nota — » (single visible prefix everywhere).
- Band titles: «LEVEN · A vida», «CULTUUR · Cultura», «SPORT · Esporte»,
  «JONGEREN · Jovens», «VERDIEPING · Aprofundamento», «TAAL · A língua»,
  «TOETS EN ANTWOORDEN · Teste e respostas».
- Exercise furniture: «OEFENINGEN · Exercícios da página N» + «Respostas na
  página 8 · Níveis misturados: procure pelo número»; P8 header «ANTWOORDEN ·
  Respostas — por página: procure o número» + «Nota em português em cada
  resposta · ✓ = com modelo»; P7 phrase tags «(Página N)».

## 6. Wording deviations (all wording-only, against measured widths/flows)
Recorded because Portuguese runs longer than the core's explanation language:
- P1 top-strip centre: «ELKE WEEK IN HET NEDERLANDS · O NEERLANDÊS QUE OS
  NEERLANDESES LEEM» — the middle segment («UM NÚMERO POR SEMANA», 1094px)
  collided with the right strip text; shortened form measures 803.8px, pixel
  gap 33px.
- P1 masthead subtitle: «EM NEERLANDÊS · VOL.1 · DE KLOK GAAT TERUG ·
  HERFSTVAKANTIE · ADE WORDT 30» — the «SEMANÁRIO EM NEERLANDÊS…» form
  measured 2049px and spilled off-page; shipped form 1781px, ink cols
  74..1876. VOL.1 and the three Dutch items kept verbatim.
- P1 searches-box subtitle shortened: «Buscas da Holanda · zoeken op Google»;
  trends line «Terça, 20 de outubro: valores estimados»; clock band right
  lines «DOMINGO, O RELÓGIO ATRASA» / «Começa o horário de inverno · ver
  página 2»; numbers box title suffix «· Em números»; ADE tips box «ZO PLAN JE
  ADE · Dicas» with short PT parentheticals; P6 chart source «Fonte: Wristler,
  20/10/2026; buscas de outubro do ano passado»; P6 debate box suffix
  «· Ou manter?»; P7 clinic title «PAS OP! · Clínica de erros»; word box
  «HET WOORD · A palavra».
- P7 error-clinic glosses compressed to one line each (keeps the col-3 stack
  ending at the core's own y=1678.5, above the quotes rule at 1698); the
  readers'-letter gloss likewise shortened.
- P8 key flow: Portuguese notes wrap longer (164 key lines vs core 155) and
  overflowed the keys flow (end 2582 > bottom 2552). Fixed by shortening
  exactly 8 notes, wording only, keys untouched: #7 «Começa na noite de sábado
  para domingo», #91 «A direção é difícil de lembrar», #99 «alleen + país
  primeiro», #127 «Os 6.600 perguntaram ao contrário», #133 «sujeito + verbo
  + direção», #134 «sujeito + verbo + lugar», #135 «A pergunta vai no início»,
  #136 «verbo + resultado + lugar». After the fix the keys end at y=2458.
- P7 phrase tags accented to Portuguese «(Página N)» (the core's tags were
  unaccented Dutch-style «Pagina N»).

## 7. Geometric occlusion audit (mandatory gate)
Builder's own implementation (`scratch/audit.py`): paint-order SVG parse,
glyph metrics from the build library's own PIL fonts including bold
(font-weight=700), line boxes expanded by half the stroke width, ink band
baseline −0.88em..+0.30em. **Validated on a synthetic positive control: all 6
planted classes fired (COVER, LINEX, FOOTER, EDGE, TEXTX, BOXTITLE-R), clean
text silent.**
- Core reference run: 27 flags. This edition: **25 flags, 0 unresolved NEW.**
- Two NEW defects were found and fixed by wording (see §6): the P1 subtitle
  off-page spill and the P1 top-strip text collision.
- Remaining flags are inherited or model artifacts, each pixel-adjudicated:
  (a) the footer pair on every page sits below the y=2580 rule by design
  (identical in the core); (b) P1 masthead/subtitle em-band overlap — actual
  ink: masthead ends row 265, subtitle begins row 291 (25 clear rows, same as
  core); (c) facts-box 1px grazes on P2/P3/P5 — pixel-identical to the shipped
  core (frozen Dutch text + formula geometry; the box borders are light
  #d8cfb4); (d) EN JIJ box descender proximity on P2/P5 (cedilla/descender
  tips reach the light border's first row; glyph bodies end 5+ rows above) —
  the identical flag fires on the shipped NL×ES edition's P2 box, i.e. the
  accepted pattern for this core with Latin-script explanations; (e) P1
  word-of-week gloss line 2 vs the y=1853 rule: rule rows 1852–1854, gloss
  ink rows 1856–1872 — zero shared rows, clear.
- Freeze check: SVG text diff + AST constant-level diff vs the core build —
  every difference is explanation layer / pairing furniture / §3 registry
  items / §6 documented wording. Dutch target text outside the registry:
  **zero changes.**

## 8. Builder's proofread (own full pass; independent proofread PENDING)
- All 8 pages read end-to-end from the rendered output: Portuguese complete
  and natural throughout; instructions, glosses and all 150 notes in PT.
- All 150 keys re-derived from the Dutch text at registry level (diff = §3
  only) and spot-verified in the page read.
- P7 phrases: all 8 Dutch quotes verified verbatim-contiguous against the
  issue's own articles, correct page tags, each occurring exactly 2×
  issue-wide (source + P7).
- Calendar: every weekday/date claim checked against the real 2026 calendar
  (wintertijd Sun 25 Oct 03:00→02:00; herfstvakantie Midden/Zuid Sat 17–Sun 25
  Oct, Noord 10–18 Oct, school resumes Mon 19 Oct; DDW Sat 17–Sun 25 Oct;
  ADE Wed 21–Sun 25 Oct; PSV–Feyenoord Sun 25 Oct 14:30, Sparta–Ajax 16:45;
  midweek fixtures Tue 20 / Wed 21 / Thu 22 Oct; Wristler study published Tue
  20 Oct; Expeditie Robinson starts Sun 1 Nov 20:00) — all correct.

## 9. Images (inherited unchanged from the core; credits from the core KIT)
All verified CC0 / public domain via the Wikimedia Commons API (2026-10-21):
- P1 westertoren.jpg — Wim van Rossem / Anefo, Nationaal Archief — CC0
- P2 zakhorloge.jpg — photo-nic.co.uk — CC0
- P3 kinderdijk.jpg — Nationaal Archief — CC0
- P3 herfstbos.jpg — Vovogov90 — CC0
- P4 elftal1912.jpg — Spaarnestad Photo — public domain
- P5 gracht.jpg — W. Punt / Anefo, Nationaal Archief — CC0

## 10. Deliverables (files/weekly-report-nl-pt/)
- svg/ ×8, cards/ ×8 PNG (1950×2700)
- Print PDF: De-Lucerna-VOL1-PT.pdf — 10,634,998 bytes —
  sha256 38e086d6985787b6713a855ec881d0d949cb49499f8886d47875aacfb9d2dea3
- Web PDF: De-Lucerna-VOL1-PT-web.pdf — 3,698,287 bytes (< 10 MB) —
  sha256 7fa11ad96a2a962eed66c691477e5e83a27b952fcca7c57398445e648115fd9a
- Proofread status: builder's pass complete; **independent proofread PASS (§11)**.

## 11. Independent proofread record (2026-10-21) — PASS, zero problems

One complete, skeptical, independent pass over the final rendered artifacts,
performed from scratch copies under `hidden_files/proof-nl-pt/scratch/`.
**No defects found; no fixes were needed** — the shipped artifacts stand
exactly as the builder delivered them (edition SVGs re-hashed 8/8 unchanged).

- **Baselines reproduced independently.** Scratch copies of the unmodified
  core build and of the shipped PT build each reproduce their 8 shipped SVGs
  byte-identically (8/8 + 8/8). Core registry from my own run: 150
  (A2 42 · B1 76 · B2 32; pages 10/18/18/18/18/18/12/38; model 87 words).
- **Freeze verdict: PASS.** AST literal-set diff of every build file plus
  identifier-skeleton diff: gained literals containing CJK = 0; lost
  no-CJK literals are exactly the documented set (P1 badge strap and
  top-strip centre — pairing furniture, §6; the accented page tags and the
  P8 separator prefix — furniture; four grammar-apparatus notes whose
  full-width colon was localised to half-width, content identical);
  identifier diffs are only the explanation-method rename plus the badge's
  colour/size (GREY 19 → BRICK 19.5 bold at the y=372 badge slot, the
  column's established brick slot — furniture). No undocumented Dutch-text
  change. Zero CJK in all 8 edition SVGs.
- **Key-diff verification (my own registry dumps):** page/level metadata
  zero mismatches; key diffs exactly {137, 138, 150} with the §3 strings
  (both translation keys faithful to the Dutch stems printed on P8);
  stems re-aimed exactly {139, 140} with Dutch keys byte-identical;
  notes changed in exactly 141; the 9 unchanged notes {12, 16, 18, 46, 79,
  84, 101, 102, 120} are each genuinely language-neutral (time equations,
  Dutch gloss equations, pure arithmetic, Dutch morphology).
- **Printed-note sets (extracted by number from both shipped P8 SVGs):**
  core = {1..150}, edition = {1..150} — **EQUAL**, dash style kept; every
  entry carries its note. P8 bottom clearance: max body baseline 2537.3 in
  BOTH editions, clear of the 2580 footer band (footers at 2624 by design).
- **Totals:** 150 (A2 42 · B1 76 · B2 32), continuous 1–150. P7 phrases:
  all 8 verbatim-contiguous in their tagged articles (tags 1, 2, 2, 3, 4, 5,
  6, 6 — accented «(Página N)» as claimed), each exactly 2× issue-wide, in
  both editions.
- **Full read:** all 8 pages read end-to-end from the rendered text — every
  explanation element genuinely in Brazilian Portuguese; all 150 printed
  answers spot-to-fully re-derived against the articles (incl. chart sums
  301.000 + 246.000 = 547.000, 750.000 − 547.000 = 203.000, 60.500/6.600 ≈ 9,
  ticket sum 19,50 + 19,50 + 32,50 = 71,50).
- **Calendar: PASS.** Every weekday/date claim checked with `date`
  (Europe/Amsterdam): wintertijd Sun 25 Oct 03:00→02:00; herfstvakantie
  Midden/Zuid Sat 17–Sun 25 Oct, Noord Sat 10–Sun 18 Oct, school Mon 19 Oct;
  DDW Sat 17–Sun 25 Oct, familiedag Sat 24 Oct; ADE Wed 21–Sun 25 Oct;
  fixtures Tue 20 / Wed 21 / Thu 22 Oct, topper Sun 25 Oct 14:30 and
  Sparta–Ajax 16:45; Wristler + Google Trends Tue 20 Oct; Expeditie
  Robinson Sun 1 Nov 20:00 — all correct.
- **Geometric occlusion audit — my own implementation** (paint-order parse,
  PIL real-font INK boxes incl. bold faces, line boxes expanded by half
  stroke width; synthetic positive control fired all 7 planted classes —
  COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE/BOXBOTTOM — and stayed silent on
  clean text). COVER / LINEX / FOOTER / EDGE / TEXTX: **0 on all 8 pages in
  both editions.** Core: 21 box-class flags; PT: 23. Every PT flag
  pixel-adjudicated on the shipped cards: the caption/heading pairs fire
  identically in the core at the same coordinates with the same Dutch
  strings (containment-heuristic artifacts — captions sit below their
  frames, headings between boxes; crops inspected, all clear); the frozen
  Dutch grazes (P2/P3/P5 sidebar facts lines, ink ending at the light
  border's row) are identical in the core. The two PT-only flags are
  1-row grazes, both NON-DEFECTS: P2 sidebar last line ink ends row 1410,
  border rows 1411–1412 (zero shared rows); P5 «EN JIJ?» gloss descender
  tip reaches row 1260 = the border's top anti-alias row, zero ink at
  ≥1261, glyph bodies clear, border continuous — the family's accepted
  pattern (same class shipped on NL×ES).
- **Builder's claimed fixes pixel-verified:** ① P1 subtitle ink cols
  **74..1876** (exactly as claimed; inside the 65..1885 margins);
  ② P1 top-strip centre ink ends col 1371, right strip begins 1406 —
  35 px clear (claimed 33); ③ P8 keys bottom = the core's own 2537.3
  (see sets above); ④ P7 tags accented «(Página N)» confirmed in the
  render. Plus: masthead ink ends row 265, subtitle begins row 291
  (25 clear rows, as claimed); P1 word-of-week gloss line 2 ink rows
  1856–1872 vs the rule at 1852–1854 — zero shared rows (claim (e)
  confirmed).
- **Images/credits:** embedded payloads + geometry byte-identical to the
  core per page (1/1/2/1/1/0/0/0); printed credits identical to the core
  and matching §9 / the core KIT.
- **Banned-term scan:** 0 occurrences (both forms) in paper, KIT, and
  operative build code; hits exist only inside `scratch/` (the disclosed
  transform-script exception, §2).
- **Final PDF pins (measured by me — identical to the builder's, no
  superseding render):** web **3,698,287 B**, sha256
  `7fa11ad96a2a962eed66c691477e5e83a27b952fcca7c57398445e648115fd9a`
  (8 pages, < 10 MB ✓); print **10,634,998 B**, sha256
  `38e086d6985787b6713a855ec881d0d949cb49499f8886d47875aacfb9d2dea3`.
- **Core integrity:** the frozen core's 8 shipped SVG sha256 are unchanged
  after all my work (start vs end identical: a8a2cc5d… / ea3f2a18… /
  b61fbb1b… / eff31458… / 1098c657… / c941eb44… / 097fcfa7… / feba8026…).
