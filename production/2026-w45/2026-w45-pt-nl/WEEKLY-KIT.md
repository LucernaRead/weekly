# A Lucerna — Portugees Weekblad VOL.2 · PT × NL edition KIT

Edition: Portuguese target text (frozen W45 VOL.2 core, Brazilian) × Dutch
explanation layer. Pairing badge (P1): «TEKSTEN IN HET PORTUGEES · UITLEG
IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS».
Build dir: hidden_files/weekly-report-w45-pt-nl-build/ · Deliverables:
files/weekly-report-w45-pt-nl/ · Core: files/weekly-report-w45-pt-core/.

STATUS: builder-complete only. This KIT reports the builder's own gates;
it does NOT claim final approval — an independent proofread (SOP gate)
is still required before insert/publication. Nothing was pushed, no
Discord post was made, no card/PDF was sent to the main chat, no cron
was created, weekly-git was not touched, and the core and W43 directories
were only read (core SVG hashes re-verified unchanged, see §1).

## 1. Baseline proof (freeze.py)

- Core build re-run UNMODIFIED with tools/freeze.py baseline BEFORE any
  edit: **8/8 SVGs byte-identical** to the shipped core SVGs.
- Core integrity re-verified AFTER the build: all 8 core SVG SHA-256
  values match the baseline prefixes exactly (p1 0dc8089df727dfe4…,
  p2 56db3aa80e1318db…, p3 82f6fc3a94fbc11e…, p4 c5647cf6e9c080ec…,
  p5 92e86020ce81f3c8…, p6 e6097473ded2f016…, p7 a72cb75a519319f4…,
  p8 82630480322959ad…). Core untouched.
- Freeze diff (tools/freeze.py diff --strict-cjk, core vs edition):
  CJK per page core 156/177/153/148/223/118/357/1123 → edition **0 on
  all 8 pages**; added CJK characters **0**. No new CJK anywhere.
- No intermediary-layer term anywhere in paper, KIT, or operative code
  (method renamed expl() after the W43 pattern; the term itself: 0).
- Content modules were NEVER imported inside the core build directory
  (README #11); all builds ran through the single one-process run.py
  (README #7); every fix round re-copied the pristine core build and
  re-ran transform.py, so transform.py reproduces the shipped sources.

## 2. Totals (= core, printed by run.py, final round)

- TOTAL exercises: **150** · by level **A2 49 · B1 70 · B2 31**
- By page: 1:10 · 2:18 · 3:18 · 4:18 · 5:18 · 6:18 · 7:12 · 8:38
- By type (Dutch labels): Voltooi de zin 61 · Meerkeuze 49 ·
  Woorden koppelen 12 · Bouw de zin 7 · Waar of onwaar 3 ·
  Gatentekst 13 · Vertaal 4 · Schrijven 1
- Writing model text (P8 H): **93 words** (printed by the build, matches
  core; PT text byte-identical).
- Final build log: FLOW OVERFLOW **0** · HEAD TOO WIDE **0**.

## 3. Furniture registry — W43 PT × NL measured, deviations stated

Everything below was measured from the shipped W43 PT × NL SVGs
(files/weekly-report-pt-nl), NOT from the tools README generics and NOT
from the W45 PT × EN sibling. Where this edition differs from W43, the
reason is stated; where it differs from PT × EN, that is also stated.

- Masthead: «A Lucerna» (as the core ships).
- P1 subtitle (y=330, 34pt serif bold, W43 size): «PORTUGEES WEEKBLAD ·
  VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE».
  Deviation from PT × EN (38pt): the W43 same-pairing size is 34pt and
  the Dutch string fits at 34pt (audit 0 flags); no reason to take the
  English sibling's size.
- P1 badge (y=372 slot, 19pt sans bold BRICK #a4553a, W43 verbatim):
  «TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS — DE EDITIE
  VOOR NEDERLANDSTALIGE LEZERS». It replaces the core strapline line
  at y=372, exactly as W43 PT × NL and W45 PT × EN do (the core's
  y=372 line is furniture, not frozen body text).
- P1 top strip middle: «TODA SEMANA EM PORTUGUÊS · ELKE WEEK · HET
  PORTUGEES DAT BRAZILIË LEEST» (W43 verbatim).
- P1 band right: «DE WEEK VAN HET ENEM» / «2 nov Finados-weekend ·
  8 nov dag 1 van het Enem».
- Footer left (all pages): «A Lucerna · PORTUGEES WEEKBLAD VOL.2 ·
  TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS» (W43 form with
  VOL.2). Footer right: «Pagina N van 8» (8/8 verified, correct N).
- Gloss prefix: «Uitleg — » (every gloss() box).
- P8 answer separators: «— Pagina N —» (all 8, W43 shipped form).
  Note: tables.json leaves the NL column's p8_separator null
  (provisional); the shipped W43 PT × NL SVG is the authority, and this
  edition follows it — deviation from PT × EN, which kept the core's
  «— PÁGINA N —».
- Band titles PT · NL (W43 glossary): VIDA · LEVEN, CULTURA · CULTUUR,
  ESPORTE · SPORT, JOVENS · JONGEREN, APROFUNDAMENTO · VERDIEPING,
  LÍNGUA · TAAL, AVALIAÇÃO E RESPOSTAS · TOETS EN ANTWOORDEN.
- Band subs follow the W43 append pattern: the Portuguese band title is
  kept verbatim and a short Dutch gloss is appended
  (e.g. «NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Finados
  en revisie: het lange weekend in Brazilië»; P7: «Focus op taal ·
  Três níveis, três ferramentas · drie niveaus, drie hulpmiddelen»,
  W43 verbatim). Deviation from PT × EN (which replaced band subs
  wholesale): the same-pairing precedent keeps frozen Portuguese band
  titles intact.
- Section heads PT · NL (W43 glossary): A NOTÍCIA · HOOFDNIEUWS,
  AGORA VOCÊ · AAN DE SLAG, NESTA EDIÇÃO · IN DEZE EDITIE,
  EM POUCAS PALAVRAS · KORTOM, QUIZ RELÂMPAGO · BLITSQUIZ,
  PARA NÃO ERRAR · EZELSBRUG, E VOCÊ? · EN JIJ?,
  A SEMANA EM NÚMEROS · CIJFERS, OS HORÁRIOS DO DOMINGO 8 ·
  DE TIJDEN VAN ZONDAG 8, A SEMANA DO FUTEBOL · DE VOETBALKALENDER,
  ERROS COMUNS · PAS OP!, A PALAVRA · WOORD VAN DE WEEK,
  FRASES DA SEMANA · ZINNEN VAN DE WEEK (letterlijk uit deze editie),
  A PRÓXIMA SEMANA · VOLGENDE WEEK (VOL.3),
  EXERCÍCIOS · OEFENINGEN, «Antwoorden op pagina 8 · niveaus gemengd:
  zoek op nummer», RESPOSTAS · ANTWOORDEN — per pagina geordend, zoek
  het nummer / «bij elk antwoord een korte uitleg in het Nederlands ·
  ✓ = met voorbeeldtekst».
- Bridges use the W43 code pattern: bslib4.bridge() renamed to expl()
  and every bridge string carries the «Uitleg — » prefix.
- Exercise type labels (W43 glossary): 单选→Meerkeuze,
  完成句子→Voltooi de zin, 词汇配对→Woorden koppelen, 造句→Bouw de zin,
  判断对错→Waar of onwaar, 完形单选→Gatentekst, 翻译→Vertaal,
  写作→Schrijven; instructions: 填空→Vul in, 造句→Bouw de zin,
  把词和释义配对→Combineer, 翻译→Vertaal, 写作→Schrijven,
  判断→Waar of onwaar?.
- Geometry deviations from the core, all forced by measured defects
  (see §8): P7 quote-row pitch 128 → 96; P8 key size 13.5 → 13 and
  line height 1.16 → 1.12. NOT changed (unlike PT × EN): P1 numbers-box
  title kept at 23pt (W43 form «A SEMANA EM NÚMEROS · CIJFERS», audit
  clean — the English sibling's 20pt was forced by its longer title);
  P7 word-box bottom pad kept at 20 (audit clean — the English
  sibling's 30 was forced by its gloss descenders).

## 4. Key registry (complete — the ONLY key/stem changes vs core)

Printed-key comparison over all 150 numbers (dash style: token before
the first « — »; verified from the rendered P8 SVGs, not from sources):

| # | Type | Core | This edition |
|---|------|------|--------------|
| 137 | key PT→reader language | 11 月 8 日周日是高考的第一天。 | **Zondag 8 november is de eerste dag van het Enem.** (note: zie de kop van pagina 6) |
| 138 | key PT→reader language | 周日前核对确认卡。 | **Controleer je kaart vóór zondag.** (note: Confira = controleer) |
| 139 | stem reader→PT (key PT, unchanged) | “连休是 10 月 31 日到 11 月 2 日。” → ___ | **“Het lange weekend loopt van 31 oktober tot 2 november.” → ___** (key: O feriadão é de 31 de outubro a 2 de novembro.; note: feriadão = het lange weekend) |
| 140 | stem reader→PT (key PT, unchanged) | 你到达时，请出示带照片的证件。 → ___ | **Als je aankomt, toon dan je document met foto. → ___** (key: Quando você chegar, apresente o documento com foto.; note: aanvoegende wijs toekomst chegar + gebiedende wijs apresente) |
| 150 | writing apparatus | key （开放题，范文如下）/ note 范文见本版 H 区（93 词） | key **(open vraag — voorbeeldtekst hieronder)** / note **voorbeeldtekst in deel H (93 woorden)**; section expl: Uitleg — Schrijfopdracht (geen uniek antwoord); de voorbeeldtekst (93 woorden) staat hieronder. Printed answer line: 150. ✓ voorbeeldtekst in deel H (93 woorden) |

All other 146 printed key tokens are byte-identical to the core.

## 5. Printed-note verification (tools/p8.py compare --target pt)

```
core    ../files/weekly-report-w45-pt-core/svg/p8-avaliacao.svg: 150 noted
edition ../files/weekly-report-w45-pt-nl/svg/p8-avaliacao.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[]
keydiff=[2, 4, 25, 26, 27, 28, 52, 53, 54, 55, 101, 137, 138, 141, 142, 143, 144, 146]
```
Printed-note set EQUAL to the core's {1..150}. P8 answer notes are pure
Dutch throughout (CJK 0 on P8; English apparatus phrases 0, see §9).

Keydiff adjudication, item by item against the printed P8 lines
(same 18-number list as PT × EN, same adjudication class):

- TRUE re-aims: 137, 138 (see §4).
- EXTRACTION ARTIFACTS (printed key token byte-identical in both
  editions; only the Dutch note text changed): 2 (portões), 4 (13h30),
  25 (c), 26 (b), 27 (d), 28 (a), 52 (b), 53 (c), 54 (a), 55 (d),
  101 (confiro), 141 (b), 142 (d), 143 (a), 144 (c), 146 (A).
  Mechanism detail: the match-set notes (25–28 P2, 52–55 P4, 141–144
  P8) gain the Dutch «(letter)» gloss form; notes 4/101/146 change
  Chinese full-width parentheses to ASCII parentheses; note 2 is a
  plain gloss change with no parentheses on either side. The key token
  is unaffected in every case.
- 150 is NOT in the keydiff list: both editions print the ✓ apparatus
  form; only the note language changed (Chinese → Dutch), as registered
  in §4.

## 6. Geometric audit (tools/occlusion_audit.py, selftest first)

- Selftest: OK (all six planted classes fired, clean controls silent).
- Final: edition **0 flags** · core **0 flags** · NEW vs core **0** ·
  exit 0. Gate outputs: hidden_files/weekly-report-w45-pt-nl-build/
  occlusion-final.json (edition + NEW) and occlusion-core-final.json.
- Same-baseline ink collision scan (all pages, PIL true-ink boxes,
  same-baseline pairs with >1px x-overlap): **0 collisions**.
- Page-frame / right-edge scan (ADVANCE method, frames outer 28..1922
  and inner 40..1910; footer baseline 2624 exempt for the below-rule
  check): max advance-right per page 1885.0 on P1/P3/P4/P5/P6/P7/P8 and
  1897.2 on P2; min advance-left 65.0 everywhere; **0 defects** (no
  advance edge crosses either frame line, no non-footer ink below the
  2580 footer rule). The P2 1897.2 line is the FROZEN Portuguese
  match-set right option «d. o objeto que dá luz e se acende em
  memória» — byte-identical in the core SVG with the identical
  advance (1897.2), i.e. inherited, not new; it clears the inner frame
  (1910) by 12.8px, and the canonical audit (true ink) does not flag
  it. No PIL integer-bbox ≤0.5px right-edge artifact needed adjudicating
  beyond this note: the only advance-right above the 1885 content edge
  anywhere in the edition is this inherited line.
- P6 chart-label coverage, baseline-anchored ink method (PIL getbbox
  with anchor="ls", label ink vs later-drawn bars; bar rects verified
  present in the parse: 60/30/330 min bars 90/45/495 wide): all labels
  **0.0%** (portões abertos, espera, prova, 60/30/330 min). The getbbox
  advance-width method was not used.

## 7. Content checks (builder's full proofread of the render)

- Gloss counting (rendered gloss() strings split on «·» itself,
  README #21): core {P2: 6, P3: 6, P4: 5, P5: 5, P6: 4} = edition
  {P2: 6, P3: 6, P4: 5, P5: 5, P6: 4}, total **26 = 26**, and all 26
  items' Portuguese head terms survive verbatim in the render.
- P7 phrases of the week: all 8 Portuguese quotes occur exactly **2×**
  in the issue (article + P7, bare text, whitespace collapsed), each on
  its tagged page, each with its Dutch translation + «(Página N)» on P7.
  Page tags stay «Página N» (core form).
- P7 word-box freeze (blocking gate): the Portuguese definition sentence
  «« feriadão »: sábado, domingo e segunda — três dias de descanso.»
  is byte-identical in core and edition; only its gloss was localised
  to Dutch («feriadão = het lange feestweekend, drie dagen.»). This
  edition's P7 word box is the Portuguese core's box — no DE/NL-family
  NOCH EIN WORT / meedoen content was used anywhere.
- Readers' corner (zero fabrication — verified on the rendered P7):
  the example letter is the core's labelled editor's example, unchanged
  («… — EXEMPLO DA REDAÇÃO», no signature, no invented reader); the
  Portuguese disclosure is retained verbatim («Nota da redação: as
  cartas reais e os melhores textos prometidos no VOL.1 não chegaram
  até o fechamento — fica o exemplo, e a promessa passa para o
  VOL.3.»); the Dutch disclosure is synonymous («Opmerking van de
  redactie: de echte brieven en beste teksten uit VOL.1 waren nog niet
  binnen — het voorbeeld blijft, de belofte gaat naar VOL.3.») —
  together they state all three facts on the page (no real letters by
  press time, no best P8 texts, example stands + VOL.3 promise). The
  explicit Dutch invitation is on the same page, as its own sentence:
  «Voorbeeld van de redactie — geen echte brief. Stuur je brief op: de
  beste verschijnen op pagina 7 in VOL.3!» — imperative («Stuur je
  brief op») + publication promise («de beste verschijnen op pagina 7
  in VOL.3»); it is not a content-preview line and not another page's
  exercise prompt. No reader, letter, name, or quotation was invented.
- Images/credits (public domain / CC0 only): the single photograph is
  P1 estudo.jpg (students in a library) — CC0, Gary Todd / Wikimedia
  Commons, reused from the W43 PT core with the identical credit line
  printed on P1 («Foto: Gary Todd / Wikimedia Commons — CC0»). The
  embedded image blob hash in the edition P1 SVG equals the core's
  (fd231e77993f09e01dc7ef7202720b1b2a822c077a500d8176905c0830ea56be);
  the image is confirmed laid out on P1 (visible in the card). All
  other visuals are original charts/tables built from the issue's
  verified facts. No other photograph is used (see build assets/
  CREDITS.md).
- Calendar/facts: unchanged from the core (frozen Portuguese text);
  the core KIT's verification record stands (Enem day 1 Sun Nov 8,
  gates 12h–13h, exam 13h30–19h; Copa second legs Sat Nov 7 18h Arena
  MRV and Sun Nov 8 17h São Januário; no scores or league positions
  printed anywhere).

## 8. Defects found in builder's proofread and fixed (all in transform.py)

- ROUND 1 → 2 (measured run1: occlusion audit 16 NEW flags, all from
  two causes; P8 key flow 5 FLOW OVERFLOW warnings ending y=2582 past
  its 2552 bottom): (a) P7 quote rows overprinted the VOL.3 preview box
  because the Dutch letters stack ends ~290px lower than the core's —
  fixed by shortening the four ERROS COMUNS Dutch notes to one wrap
  line each, the example note to three lines, the Dutch disclosure to
  four lines, and tightening quote pitch 128 → 104; (b) P8 key flow
  overflow — fixed by key size 13.5 → 13, line height 1.16 → 1.12
  (PT × EN precedent, same measured cause). Round 2 re-render (pristine
  copy + transform): FLOW OVERFLOW 0, HEAD TOO WIDE 0, audit flags
  confined to the P7 descender touch below.
- ROUND 2 → 3 (measured run2: last quote translation baseline 2402.17
  sat 1.8px above the preview-box top 2404, so descenders touched the
  box): quote pitch 104 → 96 (rows are ~76px tall, so 96 still leaves
  ~20px air). Round 3 re-render: last translation baseline 2378.17,
  25.8px clear of the box top; final audit 0/0/0 (see §6).
- Per-round baselines (full sha256 of the edition outputs before each
  re-render) are in the build dir: run2-baseline.sha256 (run1 outputs),
  run3-baseline.sha256 (run2 outputs), final.sha256 (shipped outputs).
  Round-to-round SVG diffs confirm the fixes were surgical: P1–P6 SVGs
  identical between rounds 1 and 2; only P7/P8 changed in round 2, only
  P7 in round 3.

## 9. Residual-language re-scans (rendered SVG text, all 8 pages)

- Chinese residual: **0 per page** (CJK + fullwidth ranges on rendered
  text nodes; also 0 in all build sources after transform).
- English residual: **0 on all 8 pages** against the PT × EN apparatus
  phrase list (Note | , Page N of 8, Answers on page, Levels are mixed,
  Complete the sentence, Multiple choice, Build the sentence,
  True or false, Cloze, Vocabulary matching, Sentence building,
  Fill in, Match the pairs, IN THIS ISSUE, IN NUMBERS, Text in
  Portuguese, Explanations in English, THE EDITION FOR ENGLISH-SPEAKING,
  PORTUGUESE WEEKLY, and others) — no PT × EN apparatus leaked in.
- Other-family markers: 0 (HINWEIS, Seite, EXPLICATIONS EN,
  EXPLICACIONES EN, SPIEGAZIONI IN, Nota — ).
- Intermediary-layer term: 0 in paper, KIT, and operative code.

## 10. Visual inspection (all 8 cards, 1950×2700 PNG)

- P1: badge, subtitle, band, numbers box, photo + credit, quiz — clean.
- P2: band sub fits, time boxes fit, match set fits — clean.
- P3: gloss box, calendar box, E VOCÊ box, exercises — clean (column-end
  whitespace matches the core's retained breathing-room precedent).
- P4: fixture table, gloss box, match set, comparatives — clean (the
  «B · AS PALAVRAS» head sits at the foot of column 1 with its items
  flowing to column 2, as the flow layout dictates; no overlap).
- P5: plan box, gloss box, E VOCÊ box, exercises incl. Waar of onwaar —
  clean.
- P6: minute bars clear of labels and values, both chart boxes, source
  lines — clean.
- P7: three language columns, error clinic, word box, readers' corner
  (PT + NL disclosures, labelled example, explicit invitation), 8
  quotes clear of the preview box, VOL.3 preview box intact — clean.
- P8: exercises 113–150, model text (93 words), full key 1–150 with
  «— Pagina N —» separators, key flow ending well above the footer —
  clean.
- No overlap, no truncation, no frame pressure on any page; 8 pages
  (multiple of 4); footers 8/8 carry VOL.2 + pairing; badge/header/
  footers complete.

## 11. Retained items (with reasons)

- P1 directory row title/level-badge tight spacing (e.g. «Finados, o dia
  da memóriaA2→B1»): same as the core's retained item — same layout
  code, no overlap, readable; retained.
- P3/P5 column-end whitespace: the core's retained breathing-room
  precedent; retained.
- Registration numbers only («超 500 万» equivalent kept as the frozen
  Portuguese «Mais de 5 milhões»): the core's verified-facts policy;
  no precise figure added.

## 12. Reproducibility & interpreters

- Reproduce from a pristine copy of the core build:
  `cp -r hidden_files/weekly-report-w45-pt-build <new> &&
  cp transform.py <new>/ && cd <new> &&
  <tools/venv>/python transform.py &&
  <tools/venv>/python run.py && <tools/venv>/python render.py`
  (transform.py lives in this edition's build dir; rounds 2 and 3 were
  executed exactly this way, not by patching outputs).
- run.py interpreter: tools/venv/bin/python, Python **3.12.3**,
  PIL **13.0.0**, cairosvg **2.9.1**, pypdf **6.21.2**. render.py used
  the same tools venv interpreter (system python3 is also 3.12.3 but
  its PIL is 10.2.0 and it lacks cairosvg — never used for rendering).
- Build tree: hidden_files/weekly-report-w45-pt-nl-build/
  (transform.py, gates.py, build logs per round, run baselines,
  occlusion/freeze/p8 gate outputs, history-run1/, history-run2/).

## 13. PDF pins (measured on disk)

- Print: A-Lucerna-VOL2.pdf — 3,510,712 bytes — 8 pages, 1462×2025pt —
  sha256 c80072a24602c72eb73cfdf995aee937762e2dd2a2c8874f4f0ef7adab2c11b8
- Web: A-Lucerna-VOL2-web.pdf — 3,500,683 bytes (< 10 MB) — 8 pages —
  sha256 f076efce6e08285f7480f07e7ea34e904f35ccc8c6afa54585bfa9bf1113ae02
- Note on the print size vs the core's 15.96 MB: both print PDFs carry
  the identical P1 image XObject (3,275,520 bytes) and identical page
  geometry; the ~12.4 MB difference is the CJK font embedding the core
  needs for its Chinese explanation layer, which this edition does not
  contain. The edition print PDF's text is extractable and its image is
  present (verified with pypdf).
- svg/ ×8 · cards/ ×8 (1950×2700) · ABSTRACT.txt (Dutch, one line, no
  ASCII double quotes; abstract heading for insert: «Samenvatting»).

## 14. Proofread status

- Builder's full proofread: DONE (this KIT, all gates measured).
- Independent proofread: **NOT DONE — required before any insert or
  publication.** This KIT is builder-complete only and does not claim
  final approval.
