# A Lucerna — Portugees Weekblad VOL.1 · PT × NL edition KIT

Edition: Portuguese target text (frozen VOL.1 core, Brazilian) × Dutch explanation layer.
Pairing badge (P1): «TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
Build dir: hidden_files/weekly-report-pt-nl-build/ · Deliverables: files/weekly-report-pt-nl/

## Baseline proof (freeze.py)
- Core build copied to hidden_files/weekly-report-pt-nl-build/ and run UNMODIFIED with
  tools/freeze.py baseline: **8/8 SVGs byte-identical** to the shipped core
  files/weekly-report-pt-vol1/svg/ before any edit.
- Core integrity re-verified after the build: SHA-256 of all 8 core SVGs unchanged
  (before/after hash lists identical).

## Totals (= core, printed by run.py)
- TOTAL exercises: **150** · by level **A2 44 · B1 75 · B2 31**
- By page: 1:10 · 2:18 · 3:18 · 4:18 · 5:18 · 6:18 · 7:12 · 8:38
- Writing model text (P8 H): **92 words** (printed by the build, matches core)
- No FLOW OVERFLOW in the final build log.

## Key-diff registry (complete — the ONLY key/stem changes vs core)
Derived from the core build's translation section (P8 E · TRADUZA) and verified against
the printed P8 of both editions (systematic key-segment comparison over all 150 numbers:
segments differ at exactly {137, 138, 150}):

| # | Type | Core | This edition |
|---|------|------|--------------|
| 137 | key PT→reader language | 周日，巴西重返投票站。 | **Zondag keert Brazilië terug naar de stembus.** (note: zie kop p. 1) |
| 138 | key PT→reader language | 出门前，核对你的投票地点。 | **Controleer je stemlocatie voordat je van huis gaat.** (note: Confira = controleer) |
| 139 | stem reader→PT (key PT, unchanged) | “吉他”的搜索量增长了 53%。→ ___ | **De zoekopdrachten naar «guitarra» groeiden met 53%. → ___** (key: As buscas por guitarra cresceram 53%.; note: cresceram = groeiden) |
| 140 | stem reader→PT (key PT, unchanged) | 你到达时，请核对一下投票站。→ ___ | **Controleer je stembureau zodra je aankomt. → ___** (key: Quando você chegar, confira a seção.; note: aanv. wijs toekomst + gebiedende wijs confira) |
| 150 | writing apparatus | key （开放题，范文如下）/ note 范文见本版 H 区（92 词） | key **(open vraag — voorbeeldtekst hieronder)** / note **voorbeeldtekst in deel H (92 woorden)**; section expl: Uitleg — Schrijfopdracht (geen uniek antwoord); de voorbeeldtekst (92 woorden) staat hieronder. Printed answer line: 150. ✓ voorbeeldtekst in deel H (92 woorden) |

All other 147 printed key segments are byte-identical to the core.
p8.py's informational `keydiff` list [3, 4, 8, 23, 58, 98, 101, 137, 138, 146, 147, 148]
was adjudicated item by item: at 3, 4, 8, 23, 58, 98, 101, 146, 147, 148 the extracted
key segment is identical in both editions (the tool flags first-note-segment wording
changes there); only 137/138 are true key re-aims, plus the 150 apparatus line above.

## Furniture as shipped (verbatim)
- Masthead: «A Lucerna» (as the core ships)
- P1 subtitle (34pt): «PORTUGEES WEEKBLAD · VOL.1 · O SEGUNDO TURNO · O DEBATE FINAL · O ENEM VEM AÍ»
- P1 badge (y=372 slot, bold brick): «TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
- P1 top strip: «TODA SEMANA EM PORTUGUÊS · ELKE WEEK · HET PORTUGEES DAT BRAZILIË LEEST»
- P1 band right: «ZONDAG, DAG VAN DE BESLISSING» / «Presidentsverkiezingen, 2e ronde · zie pagina 6»
- Footer left (all pages): «A Lucerna · PORTUGEES WEEKBLAD VOL.1 · TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS»
- Footer right: «Pagina N van 8»
- Gloss prefix: «Uitleg — » (every explanation string starts with it)
- P8 answer separators: «— Pagina N —»
- Exercise heads: «EXERCÍCIOS · OEFENINGEN»; exercise-page right header: «Antwoorden op pagina 8 · niveaus gemengd: zoek op nummer»
- Exercise types in Dutch: Meerkeuze · Vul in · Voltooi de zin · Gatentekst · Waar of onwaar · Waar/onwaar · Woorden koppelen · Combineer · Bouw de zin · Vertaal · Schrijven
- P8 header: «RESPOSTAS · ANTWOORDEN — per pagina geordend, zoek het nummer» / «bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst»
- Deviations from first-draft wording (shortened for width, geometry untouched):
  «EM POUCAS PALAVRAS · KORTOM» (draft IN HET KORT overshot the header rule by 37.5 units);
  «PARA NÃO ERRAR · EZELSBRUG» (fallback; EZELSBRUGGETJE overshot its box border by 15.5);
  P1 searches title «Wat Brazilië googelt · as buscas no Google» (draft overshot by 18.8);
  P1 numbers-box title «A SEMANA EM NÚMEROS · CIJFERS» (box-width forced);
  P1 searches caption «Zoekinteresse — geen stemintentie» (width-forced);
  P6 chart title «AS BUSCAS DO 1º TURNO · DE ZOEKSTIJGING RONDOM DE 1E RONDE (dados do Google)».

## Printed-note verification (tools/p8.py compare --target pt)
```
core    ../files/weekly-report-pt-vol1/svg/p8-avaliacao.svg: 150 noted
edition ../files/weekly-report-pt-nl/svg/p8-avaliacao.svg: 150 noted
status: CLEAN  missing=[] extra_count=0 uncertain=[]
```
Printed-note set EQUAL to the core's {1..150}.

## Geometric audit (tools/occlusion_audit.py, selftest first)
- Selftest: OK (all six planted classes fired, clean controls silent).
- Edition: **0 flags** · NEW vs core: **0** · exit 0.
- The core's own single flag is its frozen P1 numbers-box title cosmetic (~4px), not inherited.

## Freeze diff (tools/freeze.py diff --strict-cjk)
- CJK per page: core 177/206/150/148/232/129/347/1093 → edition **0 on all 8 pages**; added CJK chars: 0.
- All differences classified: Dutch explanation layer + furniture; the only non-CJK
  removals are the P1 tagline slot replaced by the pairing badge (family pattern),
  the 8 «— PÁGINA N —» separators → «— Pagina N —», and one re-wrapped P6 instruction line.
- Intermediary-layer term: 0 occurrences in paper, KIT, operative code (method renamed expl()).

## Defects found in builder's proofread and fixed (wording only, geometry frozen)
1. P6 exercises flow overflow (74 units) and P8 answers flow overflow (~30 units):
   Dutch notes shortened until both flows close inside their bottoms.
2. P7 frases grid overran into the fixed VOLGENDE WEEK box (last two glosses covered):
   erros-comuns note and palavra gloss each shortened by one wrap line; frases block now
   sits at the core's exact y positions (last gloss baseline 2376.7 = core).
3. P1/P2 box titles overshot their borders (see deviations above).
4. One wording pass briefly dropped «maioria absoluta» from the P6 gloss (a blanket
   string replace aimed at a P6 answer note also matched the gloss). Caught in the
   builder's end-to-end read of the rendered P6, restored, rebuilt, all gates re-run green.

## Content checks (builder's full proofread, all 8 pages read end-to-end)
- All 150 keys re-derived from the Portuguese text: match (registry above excepted).
- P7 phrases: Portuguese quotes verbatim, page tags and occurrence counts EQUAL to core.
- Calendar (real 2026): runoff Sun Oct 25 · Globo debate Fri Oct 23 · Prova do Fazendeiro
  Wed Oct 21 · Vasco × Boca Tue Oct 20 · Copa do Brasil semifinals Sun Nov 1 (November) ·
  Finados Mon Nov 2 · ENEM Sun Nov 8 & 15 — all weekday claims verified with `date -d`.
- No poll percentages anywhere: every % in the edition is Google search-interest data,
  labelled as such (core prints none; kept).
- Image credits (from core KIT, credit lines verified in the render): P1 urna.jpg —
  public domain, TSE · P3 violao.jpg — CC0 · P3 django.jpg — public domain
  (William P. Gottlieb, 1946) · P5 estudo.jpg — CC0 (Gary Todd).

## PDF pins
- Print: A-Lucerna-VOL1-NL.pdf — 6,491,054 bytes — sha256 5ec6f6a4912bfdc821051b49471560ba1fb679c6d29e900b14f49dc2f0e6c134
- Web: A-Lucerna-VOL1-NL-web.pdf — 3,685,597 bytes (< 10 MB) — sha256 2087f5512b60cd64dcf2f32d8f03f1bdb62df30cea968989d7e16db516e844c4
- svg/ ×8 · cards/ ×8 (1950×2700)

## Proofread status
- Builder's full proofread: DONE (this KIT).
- Independent proofread: **PASS** (2026-10-21, record below).

## Independent proofread record (SOP gate — full pass, zero problems)

Method: canonical tools only (tools/freeze.py, tools/p8.py, tools/occlusion_audit.py,
selftest first), fresh registry/P8 extraction, per-string diff classification, true-ink
and pixel adjudication, all 8 cards read end-to-end. Scratch:
hidden_files/proof-pt-nl/scratch/.

- **Freeze baseline**: core build re-run unmodified → 8/8 SVGs byte-identical to the
  shipped core; core SVG SHA-256 set re-verified unchanged after every run (final
  `sha256sum -c` all OK — core untouched).
- **Freeze diff (--strict-cjk)**: edition CJK = 0 on all 8 pages, added CJK = 0.
  Every non-CJK removal classified: P1 PT tagline → NL pairing badge (family pattern);
  8 «— PÁGINA N —» → «— Pagina N —»; one re-wrapped P6 word-bank line (all words
  present: segundo turno · maioria absoluta · votos válidos · intenção de voto);
  P8 answer lines whose only change is the Dutch note, plus fullwidth→halfwidth colon
  normalisation on items 16–20, 57, 102, 103 (key segments unchanged). A Latin-word
  multiset sweep of pp. 1–7 found no unexplained Portuguese word loss (only the
  English footer → Dutch footer and the P1 tagline) — i.e. no blanket-replace
  collateral beyond the builder's disclosed, restored «maioria absoluta» incident;
  the phrase verified present ×3 in the final P6 (article, gloss box, word bank).
- **Keys**: printed-key comparison over all 150 — segments differ at exactly
  {137, 138, 150} plus stems {139, 140}, as registered. p8.py's informational
  keydiff [3, 4, 8, 23, 58, 98, 101, 146, 147, 148] verified item by item against
  both P8 SVGs: key segments identical, Dutch notes present. #87 is byte-identical
  in both editions («B — 900 − 250 = 650», language-neutral). Spot re-derivations
  across all pages (23: 982+514+431+312=2.239; 57: 66.026>66.000; 83/86/87 chart
  arithmetic; 105/109/111 verb forms; 124/125/128 calendar keys) all match.
- **p8.py compare**: CLEAN — core 150 noted = edition 150 noted, sets EQUAL {1..150}.
- **Totals**: 150 exercises, numbering continuous 1–150 (visually confirmed per
  page 10/18/18/18/18/18/12/38); level-badge distribution identical to the core on
  every page; writing model text byte-identical to the core, 92 tokens counted
  (= printed «92 woorden»).
- **Occlusion audit** (selftest OK): edition **0 flags**; core 1 flag (its frozen
  P1 numbers-box title BOXTITLE, right ink 968.5 > border 961.0) — the NL title
  «A SEMANA EM NÚMEROS · CIJFERS» does not inherit it; NEW vs core = 0.
- **Geometry (ink standard)**: P7 frases block sits at the core's exact coordinates
  (quotes byte-identical, Dutch glosses at core baselines, last gloss 2376.67 =
  core; VOLGENDE WEEK box title y=2448 in both) — no cover. Shortened box titles
  verified in the render (KORTOM / EZELSBRUG / searches / numbers). P8 answer flow
  ends far above the footer band. One near-touch pixel-adjudicated NON-DEFECT:
  P4 option «c. o resultado de um jogo, com os gols» ink ends x=987, the B1 badge
  of #60 starts x=989 — 1–2 px clearance, zero ink contact, and the string +
  geometry are byte-identical frozen core content.
- **Calendar** (`date -d`, America/Sao_Paulo): runoff Sun Oct 25 ✓ · Globo debate
  Fri Oct 23 ✓ · Prova do Fazendeiro Wed Oct 21 ✓ · Vasco×Boca Tue Oct 20 ✓ ·
  Copa semis Sun Nov 1 / Sat Nov 7 / Sun Nov 8 ✓ · Finados Mon Nov 2 ✓ · ENEM
  Sun Nov 8 & 15 ✓ · Halloween Sat Oct 31 ✓.
- **Red line**: every % in the edition is Google search-interest or the guitar
  study, labelled as such in place; no poll percentages. P7 quotes: occurrence
  counts equal to the core for all 8 (extraction method as in freeze diff).
- **Images/credits**: embedded image data hashes identical to the core per page
  (P1 urna, P3 violão + Django, P5 estudo); credit lines in the render match the
  core KIT (TSE public domain · CC0 · Gottlieb 1946 PD · Gary Todd CC0).
- **Furniture**: badge, footers, «Pagina N van 8», «Uitleg — » prefix, and all 8
  «— Pagina N —» separators verified present on the correct pages.
- Intermediary-layer term: 0 in paper, KIT, and operative build code (`expl()`).

**Final pins (measured on disk, = builder's)**: print A-Lucerna-VOL1-NL.pdf —
6,491,054 B — sha256 5ec6f6a4912bfdc821051b49471560ba1fb679c6d29e900b14f49dc2f0e6c134;
web A-Lucerna-VOL1-NL-web.pdf — 3,685,597 B (< 10 MB) — sha256
2087f5512b60cd64dcf2f32d8f03f1bdb62df30cea968989d7e16db516e844c4.

**Verdict: PASS — one complete independent pass, zero problems. No fixes needed,
no re-render. Ready for parent to insert (slug 2026-w43-pt-nl).**
