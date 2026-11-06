# De Lucerna VOL.2 — Dutch text · Italian explanations (NL × IT, W45)

Fan-out edition of the frozen W45 NL core
(`files/weekly-report-w45-nl-core/`, Dutch text + Chinese explanations).
This edition keeps the Dutch target text, images and layout geometry frozen
and rewrites ONLY the explanation layer into Italian for Italian-speaking
readers. Build dir: `hidden_files/weekly-report-w45-nl-it-build/` (a true copy
of the core build; the core was never edited — its 8 shipped SVG hashes were
re-verified unchanged at the end of the build, see §1).

**Status: builder-complete, NOT finalized.** Finalization requires an
independent proofread round. No Discord post, no chat card/PDF, no git push,
no cron was made for this edition (per task scope).

## 1. Baseline proof (method gate)

`tools/freeze.py baseline` on the W45 NL core build reproduced the core
**8/8 byte-identical** (tools venv) and re-hashed the shipped core unchanged:

- p1 5424557b1798275b88f76dd4dadaf8b10996b36eef61ac2d1597de84d2c36280
- p2 78e6fcd247a53972b339c474fc97d1cac93081bec17d111ec0238b5189fb5f5f
- p3 5b9854e3c9c1e4882abdeef465e0484f1342afe456aa1c27f20348df20b07b74
- p4 cc227fd9caf0dfab15de526367bd4b11a4ec6f744d871295bd4513e3b51c8431
- p5 e58064c9927298ad25cf0cafad69a251c023cadd4e5333809cafd13483616865
- p6 6583fe285e92969acd5149722fa372c7ad79dd9afa154d362a7efdd5310e0983
- p7 65cfe2b3e45725e39eaa8a47794f543d29733bea9a458d0fde5f906c05071da9
- p8 fe22a15107ab385b05326099c85f5175910e3d128dab561b5ec48ec094b795e0

After all work, the core's shipped SVG hashes were re-verified — **all 8
unchanged** (`sha256sum -c` on the pre-build pin file: 8/8 OK).

`tools/freeze.py diff` core-vs-edition: added CJK characters **0 on every
page** (core CJK per page 191 / 212 / 153 / 126 / 214 / 192 / 373 / 1033 →
edition 0). Every changed string belongs to the explanation layer, page
furniture, the masthead badge/footers, or the re-aimed translation items
(§5); no Dutch article, exercise body, option, fact or figure differs.

## 2. Totals (measured against the core registry)

- **150 exercises** — A2 47 · B1 72 · B2 31; per page 10 / 18 / 18 / 18 /
  18 / 18 / 12 / 38 — identical to the W45 NL core (NOT borrowed from any
  other family: these are the core WEEKLY-KIT.md §3 measured values).
- Type distribution identical to core, labels in Italian: Completa la frase
  65 · Scelta multipla 44 · Abbinamento 8 · Vero o falso 7 · Forma la frase
  8 · Cloze 13 · Traduzione 4 · Scrittura 1.
- Numbering continuous 1–150; writing model 87 words (requirement 80–100).
- Format: 8 pages (multiple of 4), page size 1950 × 2700, 4 columns.

## 3. Italian-column furniture (measured from the shipped W43 NL × IT SVGs)

W43 measured values win over README #20's generic text; the W43 comparison
below is against `files/weekly-report-nl-it/svg/` (shipped VOL.1):

- **Pairing badge (P1, INSERTED at y = 568, 20 pt bold BRICK #a4553a,
  centred x = 975):** «TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO —
  L'EDIZIONE PER I LETTORI ITALIANI» — measured 840.9 px in the 1820 slot
  (W43 shipped value 840.9 — identical string, size, weight, colour, slot).
  The Dutch strapline at y = 372 is kept verbatim (W43 IT also keeps it;
  it does NOT replace the strapline, unlike the EN family case).
- **P1 subtitle (y = 330, 36 pt bold serif, W43 IT size — core ships
  40 pt):** «SETTIMANALE OLANDESE · VOL.2 · KLIMAATWEEK · MUSEUMNACHT ·
  SPEELRONDE 12» — measured 1619.95 px (slot 1820; W43's longer VOL.1
  subtitle measured 1764.8 at 36 pt, so no shortening was needed).
- **P1 top strip:** left «VOL. 2» (core, unchanged); centre «ELKE WEEK IN
  HET NEDERLANDS · OGNI SETTIMANA IN OLANDESE» (W43 IT string, 21 pt);
  right week dates in Dutch, unchanged.
- **Footers, all 8 pages:** «De Lucerna · SETTIMANALE OLANDESE VOL.2 ·
  TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO» (20 pt sans, grey, baseline
  2624; measured 908.0 px = W43 value) with «Pagina N di 8» (N = 1–8).
  Footers verified 8/8 with VOL.2.
- **Gloss prefix:** «Nota — » on all gloss boxes (W43 IT form).
- **Masthead:** «De Lucerna» exactly as the core ships.
- **Band right (P1):** «SETTIMANA DEL CLIMA» / «Tutta la nazione partecipa
  · vedi pagina 2» (W43 IT band pattern: Italian label + Italian gloss).
- **Section heads (W43 IT forms, W45 topics):** IN PRIMO PIANO, IN CIFRE,
  TOCCA A TE, QUESTA SETTIMANA, SOMMARIO, IN BREVE, QUIZ LAMPO, VITA,
  CULTURA, SPORT, GIOVANI, APPROFONDIMENTO, LINGUA, TEST E RISPOSTE,
  RISPOSTE, LA PAROLA, FRASI DELLA SETTIMANA, LA PROSSIMA SETTIMANA,
  ERRORI FREQUENTI.
- **P8 separator:** «— PAGINA {n} —» kept from the core (as in W43).
- **Answer-key format:** this edition keeps the CORE's dash style
  `N. key — note` (the NL family is dash-style; the writing item uses the
  ✓-note form, as in the core). P8 key typography follows the W45 NL × EN
  measured values: key lines 13.0 pt / 1.14 leading / 0.3 gap, separators
  13.5 pt / 1.17 / 1.5 gap, flow bottom 2540.

## 4. Gates — all measured values

- **Pages:** 8 (multiple of 4). **Freeze:** baseline 8/8 (§1); diff added
  CJK 0 every page.
- **P8 printed-note set:** `tools/p8.py compare` (explicit P8 paths, total
  150): core 150 noted, edition 150 noted, status **CLEAN**, missing []
  extra 0 uncertain []. Keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148] —
  adjudicated BY NUMBER in §5; no key is missing, no extra key, no SHORT.
  Note-set equality holds (150 = 150).
- **Geometric occlusion audit:** `tools/occlusion_audit.py` (selftest OK):
  edition **0 flags**, core **0 flags**, NEW vs core **0** (final run after
  fix round 2).
- **Same-baseline ink scan** (`build/rowcheck.py`, README #10): **CLEAN on
  all 8 pages** (furniture bands included, P1 top band especially).
- **Chart-label coverage** (`build/rowcheck.py`, README #12 GRAZE watch):
  worst P6 chart-label bbox coverage **0.0%** — below the 30% threshold;
  chart labels and values verified against the bars (45 / 25 / 20 / 10,
  total 100); chart labeled OEFENDATA in Dutch and DATI DI PROVA in the
  Italian title/caption.
- **Gloss counts (split on `·` in the rendered gloss strings, README
  #21):** P2 6 = 6, P3 5 = 5, P4 5 = 5, P5 5 = 5, P6 5 = 5 — core 1:1 in
  every box. P1 bridge 4 items, P7 bridges 4 / 3 / 3 items, unchanged in
  count.
- **P7 golden sentences:** all 8 Dutch sentences occur exactly **2×**
  (source article page + P7), verbatim, with page tags identical to the
  core: Pagina 1, 1, 2, 3, 4, 5, 6, 6. Each sentence confirmed on its
  tagged article page (P1 ×2, P2, P3, P4, P5, P6 ×2). P7 phrases are
  verbatim excerpts from this issue's articles.
- **P7 word-box freeze (standing ruling, de-nl/de-pt):** the core's Dutch
  definition sentence is kept verbatim — ««meedoen» betekent: deelnemen,
  erbij zijn. In de Klimaatweek doet heel Nederland mee.» — and ONLY the
  gloss line beneath it is localised: «meedoen = partecipare: tutta
  l'Olanda partecipa.» Verified present verbatim on rendered P7.
- **Readers' corner (§6):** no reader, letter, name or quote invented; the
  only letter on the page is the labeled editor's example.
- **Images:** only clearly public-domain/CC0 images, reused byte-identical
  from the core build assets: P1 herfstbos, P2 kinderdijk, P3 gracht, P4
  elftal1912 (1 `<image>` element per photo page; P5/P6/P7/P8 carry no
  photo, as in the core). Every credited image is typeset on its page.
- **Image credits (from the Commons API Artist field, per the core KIT
  §5):** P1 Foto: Vovogov90 — CC0; P2 Foto: Nationaal Archief — CC0;
  P3 Foto: W. Punt / Anefo, Nationaal Archief — CC0; P4 Foto: Spaarnestad
  Photo — publiek domein. All four credit lines verified present in the
  rendered SVGs on the correct pages.
- **Banned-string scans (all 8 SVGs, text layer):** the banned intermediary term 0, CJK characters 0, spaced guillemets (« / ») 0, double
  spaces 0, ASCII double quotes in text nodes 0. Build code is likewise
  CJK-free and banned-term-free (the `bridge()` helper name is an English
  identifier inherited from the core build, as in the W45 NL × EN sibling;
  the paper contains no banned term anywhere).
- **Build warnings:** final render log shows **zero FLOW OVERFLOW / HEAD
  TOO WIDE** warnings. Final flow ends: P2-ex 2402 (bottom 2580), P7 col-3
  stack 1896.0 (phrases rule at 1937), P8-keys 2376 (bottom 2540).
- **Visual inspection:** all 8 rendered PNG cards viewed (P1, P2, P6, P7,
  P8 in full; P3, P4, P5 spot-checked against the same gates): clean, no
  overlaps, no cut-off text, no defects — including the fixed P1
  agenda/word-note area, the P2 code boxes, the P6 chart, the P7 col-3
  stack and the P8 key block foot.

## 5. What changed vs the core — and what did not

Rewritten into Italian (the whole explanation layer): every word gloss
(«Nota — » boxes), every section instruction, the error-clinic notes, the
readers'-corner disclosure and invitation, the teaser apparatus, the
phrases-of-the-week translations, all 150 answer notes, all bilingual page
headers and subtitles, the P1 numbers-box parentheticals, the P2 code-box
labels, the P6 chart title and caption's second line, the readers' prompts
(EN JIJ boxes), and the P8 answer-key header lines.

Unchanged: all Dutch articles, headlines, exercise bodies and options, all
facts and figures, all images and credits, the chart geometry and values,
and the answer keys except §5 items below.

### P8 keydiff adjudication (compare output keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148])

- **Genuine re-aims (translation items, as in the W43 NL × IT precedent):
  137, 138.** Exercises 137–138 keep their Dutch source sentences and are
  now translated **into Italian** (137 «La Settimana del clima dura sette
  giorni.», 138 «Il codice arancione significa: preparati.»). Exercises
  139–140 swap direction — the printed source is now Italian («La Notte
  dei musei dura dalle 19:00 alle 02:00. → ___», «Io partecipo alla
  Settimana del clima. → ___») and the key is the Dutch sentence,
  byte-identical to the core's keys (139 «Museumnacht duurt van 19:00 uur
  tot 02:00 uur.», 140 «Ik doe mee aan de Klimaatweek.»); 139/140 are
  therefore NOT in the keydiff, and 150's printed line is the translated
  writing-task pointer (apparatus) with the 87-word Dutch model text
  byte-identical.
- **Extraction artifacts, not key changes: 7, 17, 70, 71, 76, 96, 148.**
  Verified BY NUMBER against the printed P8 lines in both SVGs: for each
  of these seven, the printed answer token before the dash is byte-identical
  to the core (7 B, 17 wortelen, 70 eiland, 71 proef, 76 gaat winnen,
  96 advies, 148 B); only the translated note differs. p8.py's paren
  branch swallows the note into its key field exactly when a note ends in
  a parenthetical (e.g. «wortelen = mettere radici (soggetto plurale)»,
  «eiland = isola (het)», «zachte = morbido (terreno)») — the same
  artifact family as README #13, and the reason the task requires the
  key candidate to contain no parenthesis. No key is actually changed.

## 6. Readers' corner — honest note

No real reader letter exists for this issue. P7 prints a **clearly labeled
editor's example** («Li (voorbeeldbrief van de redactie)», Dutch example
letter text kept verbatim from the core) plus an on-page disclosure and
invitation. All three facts are on the page, in Dutch and in Italian:
(1) no real letters had arrived at press time, (2) no best page-8 texts
had arrived, (3) the example stands with the promise carried to VOL.3.
The explicit Italian public invitation, verbatim:

> Esempio della redazione, non una lettera vera. Mandaci lettera e testo
> di pagina 8: li pubblicheremo nel VOL.3!

(Imperative «Mandaci» + publication promise «li pubblicheremo nel VOL.3»;
the contents-preview line and other pages' exercise prompts are not counted
as the invitation.) The Italian disclosure, verbatim:

> Alla stampa: niente lettere vere, niente migliori testi di pagina 8 —
> quindi un esempio; promessa rimandata al VOL.3.

The Dutch disclosure is kept verbatim: «Ter perse: nog geen echte brieven
of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar
VOL.3.» No reader, letter, name or quote was invented for this edition.

## 7. Toolchain

- **run.py interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow
  13.0.0 (same venv that reproduced the core baseline 8/8 byte-identical;
  system python3 is also 3.12.3 but ships Pillow 10.2.0 and no cairosvg,
  so it was NOT used).
- **render.py (CairoSVG) interpreter:** tools/venv/bin/python — Python
  3.12.3, Pillow 13.0.0, cairosvg 2.9.1 (system python3 lacks cairosvg, as
  the task states).
- **Pipeline:** one-process run.py (content12 → 34 → 56 → 7 → 8, so the
  exercise registry accumulates — never run modules standalone, never
  import them inside the core build dir, per README #11) → render.py
  (SVG → 1950×2700 PNG cards → print PDF via cairosvg+pypdf → web PDF
  JPEG q85 @1400 px).
- **Transform record:** build/transform.py (line-literal replacements with
  counts; paths were repointed by sed before the transform and
  grep-verified: zero core-dir references left in *.py) plus
  build/rowcheck.py (supplementary scans, adapted from the W45 NL × EN
  build). The core build directory was copied, never modified.
- **Line-width measurement:** every width claim in this KIT was measured
  with the build's own svglib text measurement on rendered SVGs (real
  font metrics), never estimated.

## 8. Build rounds

1. **First render:** counts exact (150; levels/pages/types as §2), but P2
   exercise overflow (flow to 3032 vs bottom 2580), P8 key overflow (5
   warnings) and P7 col-3 stack to 2130.5 (phrases rule at 1937) — fixed
   per §8 items 1–3 below. Fix-round baseline: pre-fix sha256 of the
   edition's SVGs written to build/fix1-baseline-sha256.txt before the
   re-render.
2. **Fix 1:** zero build warnings; P2-ex ends 2402, P7 col-3 ends 1896,
   P8-keys ends 2376 — but occlusion audit flagged 7 NEW defects (P1
   agenda subtitle + footnote overflow, P1 word-gloss covered by the
   IN HET KORT box, P6 chart title off-page, P6 vote-box title over its
   border) — fixed per §8 item 4. Fix-round baseline: build/fix2-baseline-sha256.txt.
3. **Fix 2:** zero build warnings; occlusion edition 0 / core 0 / NEW 0;
   all gates in §4 re-run on the final render; cards + PDFs rendered
   from the final SVGs.

### Layout adjudications (apparatus only — the Dutch core was never touched)

1. **P2 exercise spacing:** P2 exercise gaps 8 → 4 (14 items) and
   section-head gaps 13 → 8 (4 heads, P2 only), per the W45 NL × EN
   precedent. Italian bridges wrap longer than the Chinese ones; without
   this the P2 match set overflowed its region (the +31 px bridge growth
   cascaded across column breaks). Final P2-ex ends 2402 (bottom 2580).
2. **P8 answer-key typography** follows the W45 NL × EN measured values
   (see §3): at the original size the longer Italian notes pushed the key
   flow to 2582 (bottom 2552). Final keys flow ends 2376 (bottom 2540).
3. **P7 column-3 stack:** the Italian clinic notes, word gloss,
   disclosure and invitation were shortened to telegraphic form (W43
   NL × IT precedent: short clinic notes) so the three-box stack ends at
   1896.0, clear of the phrases rule at 1937 (first render ended 2130.5
   and collided with the phrases section). No Dutch text, quote or
   preview text changed. Final shortened strings: clinic «Il clima è il
   tempo a lungo termine.» / «Klimaatweek è un nome: maiuscola.» /
   ««Een» è singolare: «een boom»» / «Dopo «omdat»: verbo al secondo
   posto.»; gloss «meedoen = partecipare: tutta l'Olanda partecipa.»;
   disclosure and invitation as in §6.
4. **Occlusion fixes (wording only, geometry frozen):**
   - P1 agenda subtitle → «Agenda van de week · GLI EVENTI» (304.8 px,
     box inner 390).
   - P1 agenda footnote split into two lines («Tutte le date e gli orari
     sono» / «negli articoli alle pagine 2–4.», 244.1 / 250.9 px), per the
     W45 NL × EN precedent — the single long line ran off the page
     (ink to 1972 > page 1950).
   - P1 word-of-the-week Italian gloss → ««Clima»: il tempo e la natura
     intorno a noi. La Settimana del clima tratta il nostro clima.»
     (exactly 2 wrapped lines; line 2 descender-free, so the IN HET KORT
     box top at y = 1874 stays clear — the 3-line version's last line
     «nostro clima.» was 100% covered by that box).
   - P6 chart title → «DE GRAFIEK · DATI DI PROVA» (343.9 px, box inner
     390; the longer form ran to ink 2051 > page 1950). The OEFENDATA
     label stays in the Dutch + Italian captions below the chart.
   - P6 vote-box title → «VOOR OF TEGEN? · PRO O CONTRO?» (378.0 px,
     box inner 390).

## 9. Deliverables (files/weekly-report-w45-nl-it/)

- svg/ ×8, cards/ ×8 (1950×2700 PNG).
- Print PDF: De-Lucerna-VOL2-IT.pdf — **7,915,647 bytes, sha256
  fee7c18ccf19e3884ec5e3cc94add80542392ce4ffc235a55d84327b668a3c74**
  (8 pages).
- Web PDF: De-Lucerna-VOL2-IT-web.pdf — **3,658,192 bytes (< 10 MB),
  sha256 5f1e481ac83ae22bf911cbc7c808a6623c5ee5826187905e3746960cfeec8a19**
  (8 pages).
- WEEKLY-KIT.md (this file), ABSTRACT.txt (Italian, one line, no ASCII
  double quotes).
- Edition SVG sha256 (final render):
  - p1 b00135f11671894678785408ff457c189238f33f22211ff87429e6bb6b5eb21d
  - p2 10cb6dd8a247e74c9bd670f47b708008977059b6db3868ef0174534d58777be4
  - p3 6454819376591e6bd0630e4ebf8bee6f459a6da7ffe4eadf2dcade7f69d08668
  - p4 1542119759458439f110aa049672a06d6646179df7614299cbfc305bf21274ab
  - p5 4428f969dd8c15d5aab6b59eb3b2a7a585060f19d460a5d3bf18b00c34ed047b
  - p6 e79c935eac38bc30d712f6e0c392c3052a0bf980a0830ef13d8197386a890c2a
  - p7 adbdaf99e5ddbefe85916042923615b02326587e704b2f2d38e923ac6a72e57d
  - p8 444b41a423bb617e010adec14fdb8dbce1acebcaf7e59c45977b891b5a346ae2

## 10. Delivery note

This edition is delivered as files only. NOT pushed to git, NOT posted to
Discord, NOT messaged anywhere (per task instruction). Handoff to the
parent agent for independent proofread and repo insert. This edition is
NOT self-certified: a fresh full independent proof round is still required
before finalization.
