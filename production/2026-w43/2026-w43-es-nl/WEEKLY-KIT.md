# La Lucerna · VOL.1 · ES × NL — WEEKLY KIT

**Edition**: Spanish target text (frozen VOL.1 core) × Dutch explanations —
the edition for Dutch-speaking readers («de editie voor Nederlandstalige lezers»).
**Pairing**: target `es` × native `nl`. Masthead: **La Lucerna** (as the core ships).
**Source core**: `files/weekly-report-es-vol1/` (build `hidden_files/weekly-report-es-build/`),
which already carries the §12 P7 clinic patch, the §13 P8 footer patch and the
§14 «desde el viernes 23» correction — all inherited unchanged.
**Build dir**: `hidden_files/weekly-report-es-nl-build/` (copy of the core build).
**Deliverables** (this dir): `svg/` ×8, `cards/` ×8 (1950×2700),
`La-Lucerna-VOL1-NL.pdf` (print), `La-Lucerna-VOL1-NL-web.pdf` (web, < 10 MB).
**Status**: builder proofread complete (see §10); independent proofread
**PASS** (see §13).

## 1. Baseline proof (freeze.py)

`tools/freeze.py baseline` on the unmodified copied build: **8/8 SVGs
byte-identical** to the shipped core SVGs. Core SVG sha256 recorded before
(scratch/core-svg-hashes-before.txt) and after (…-after.txt): all 8 hashes
identical — the frozen core was never touched.
Baseline P5 verified to contain «desde el viernes 23» (1 occurrence;
«jueves 23» = 0) — the core's weekday correction is present and kept
(2026-10-23 is indeed a Friday).

## 2. Method

Explanation layer rewritten into Dutch by a count-asserted literal transform
(scratch/transform.py, confined to the build's scratch/ and disclosed here per
the standing builder-hygiene rule; it quotes the core's original call strings
only as search patterns for the method rename): **484 literal replacements**
(264 distinct strings; the count reconciles exactly with an AST inventory of
the core build: 484 CJK-bearing literal occurrences, minus 3 f-string
fragments in the footer that were replaced by a targeted code edit, plus 3
paren-normalisation pairs). The explanation method `bridge()` was renamed to
`expl()` (def + 20 call sites); the intermediary-layer term occurs **0 times**
in the paper, this KIT and the operative code. Spanish text, images and
geometry are frozen; every layout adaptation below is wording-only.

**Answer-style finding (brief discrepancy, adjudicated)**: the brief described
the core's P8 answers as "paren style", but the shipped core's content8.py
prints `f"{n}. {key} — {note}"` (**dash style**; writing items print
`f"{n}. ✓ {note}"`). The answer-generation code was therefore left
byte-identical — ES×NL prints in the core's own dash style, like the core.
`tools/p8.py` handles both styles and verifies the printed set (§6).

## 3. Totals (registry, identical to the core)

TOTAL **150** exercises · A2 52 · B1 70 · B2 28 · per page
10/18/18/18/18/18/12/38. Type counts identical to the core's (see §4 for the
Dutch type names). Real goals total on P4 is the core's **40** (frozen Spanish
text; stem #57 and key verified in proofread).

## 4. Key-diff registry (complete)

Printed-key comparison over all 150 items (p8.py extract, core vs edition):
**only #137 and #138 differ in the key itself** — the two translation items
whose key is the translated sentence:

| # | core key (Chinese) | ES×NL key (Dutch) |
|---|---|---|
| 137 | 周日我们多睡一个小时。 | Op zondag slapen we een uur langer. |
| 138 | 周一在九个自治区是假日。 | Maandag is een feestdag in negen autonome regio's. |

Their notes «对照原文» → «zie het origineel» (shortened in fix round 2, §8).

Reverse translation items — stems re-aimed at Dutch, **keys unchanged**
(verified byte-identical in the printed comparison):

| # | core stem | ES×NL stem | key (unchanged) |
|---|---|---|---|
| 139 | 国家德比周日晚九点开踢。→ ___ | De Clásico wordt zondagavond om negen uur gespeeld. → ___ | El Clásico se juega el domingo a las nueve de la noche. |
| 140 | 每个图表都必须标明来源。→ ___ | Elke grafiek moet zijn bron vermelden. → ___ | Cada gráfico tiene que llevar su fuente. |

Writing item: #150 key apparatus «（开放题，范文如下）» →
«(open vraag — de voorbeeldtekst staat hieronder)»; the printed ✓ note reads
«voorbeeldtekst in deel H (82 woorden)» (core: «范文见本版 H 区（82 词）»);
the 82-word Spanish model text is frozen.

All other 145 keys are byte-identical to the core's printed keys (Spanish,
letters, numbers). p8.py compare lists keydiff=[12, 14, 16, 17, 57, 73, 75,
83, 95, 96, 101, 105, 137, 138]: the twelve extra numbers are extractor
artefacts of note translation (its key field absorbs the first note fragment)
— each was verified in the extracted output and in the SVG: keys identical,
only the Dutch note differs (e.g. #17 prints «17. dormimos — bij nosotros
blijft het dormimos», #105 «105. más importante — más + bijv. naamwoord»).

Exercise type names (registry-level localisation, counts unchanged):
完成句子→Zinnen aanvullen (48) · 单选→Meerkeuze (47) · 完形单选→Cloze-meerkeuze
(13) · 词汇配对→Woorden combineren (12) · 句型转换→Zinnen omvormen (10) ·
判断对错→Lezen: waar/onwaar (8) · 造句→Zinnen maken (7) · 翻译→Vertalen (4) ·
写作→Schrijven (1).
Instruction tags: 填空→Vul in · 改写→Herschrijf · 把词和释义配对→Combineer ·
判断→W/NW · 造句→Zinnen maken · 翻译→Vertalen · 写作→Schrijven.
Apparatus inside exercise bodies: «(原形 buscar)»→«(infinitief buscar)»,
«(原形 estrenar)»→«(infinitief estrenar)».
Paren normalisation (Spanish apparatus notes printed on P8; full-width →
half-width, wording otherwise identical): «los relojes → cambian（ellos）»,
«el reloj se atrasa（él）», «dormir: él → duerme（o→ue）».
P7 phrase tags: the 8 tag data fields «Página N» → «Pagina N» (fix round 4);
printed tags (Pagina 1)×1, (Pagina 2)×2, (Pagina 3)×2, (Pagina 4)×1,
(Pagina 5)×1, (Pagina 6)×1 — counts equal to the core's.

## 5. Furniture as shipped (verbatim)

- P1 masthead subtitle: «SPAANS WEEKBLAD · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1»
- P1 pairing badge (19.5 pt sans bold brick, the EN×NL/FR×NL pattern):
  «TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
- P1 top strip: «CADA SEMANA EN ESPAÑOL · ELKE WEEK · HET SPAANS DAT DE SPANJAARDEN LEZEN»
- P1 banner right: «ZONDAG: EEN UUR LANGER SLAPEN» / «ÉN DE CLÁSICO · ZIE PAGINA 2 EN 4»
- Footers (all pages): «La Lucerna · SPAANS WEEKBLAD VOL.1 · TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS» / «Pagina N van 8»
- Gloss prefix (bslib `expl()`/gloss): «Uitleg — »
- P8 section separators: «— Pagina N —» (N = 1..8)
- P8 answers header: «RESPUESTAS · Antwoorden — per pagina gerangschikt; zoek op nummer» /
  «Bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst»
- Exercise heads: «EJERCICIOS · Oefeningen van pagina N»; answers pointer:
  «Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer»
- Band subtitles pair Spanish + Dutch throughout (e.g. «NIVEL A2 · El cambio de
  hora y el tiempo · De klok en het weer»); P7 band: «Tres niveles, tres
  herramientas · Drie niveaus, drie hulpmiddelen».

Deviations from the tables.json NL column (all wording-only, driven by
measured ink widths; see §8): P1 CIFRAS box title ships as «LA SEMANA EN
CIFRAS · In cijfers» and the P2 mnemonic box title as «LA FRASE PARA RECORDAR
· Spreuk» (the fuller Dutch wordings crossed their box borders); P3 section
title «RECORDAR JUNTOS · Herdenken».

## 6. Printed-note verification (tools/p8.py)

`p8.py compare --core-dir files/weekly-report-es-vol1 --edition-dir
files/weekly-report-es-nl --target es --total 150`:
**status: CLEAN — core 150 noted, edition 150 noted, missing=[], extra=0.**
The printed-note set EQUALS the core's {1..150} (the ES core prints all 150
notes; so does this edition).

## 7. Freeze diff classification (tools/freeze.py diff)

Per page (added/removed strings): p1 +29/−26 · p2 +40/−34 · p3 +35/−31 ·
p4 +32/−26 · p5 +47/−39 · p6 +18/−18 · p7 +44/−41 · p8 +182/−171.
**Added CJK characters: 0 on every page** (edition CJK total 0 except P7 = 2,
which are the full-width parentheses of the frozen Spanish letter attribution
«（carta de ejemplo, escrita por la redacción）», present identically in the
core). Every removed non-CJK string was eyeballed and classified: the replaced
P1 furniture line, the 8 «— PÁGINA N —» separators, the 3 paren-normalised
notes, and wrap fragments of lines whose explanation parenthetical changed
(identical Spanish wording, new line breaks). No Spanish body string was
added, removed or altered in content.

## 8. Defects found in production and fixed (wording-only throughout)

- **Round 1** (build warnings): P3 box title «RECORDAR JUNTOS · Samen
  herdenken» HEAD TOO WIDE → «· Herdenken» (measured 413.7 ≤ 434 at 25 pt).
  P6 exercise flow overflow (last items overprinted at the footer) → A-head
  «Beantwoord de vragen bij de grafieken.» (1 line) and C-head «Vul in:
  sondeo · media · indecisos · margen de error». P8 keys flow: longest Dutch
  notes trimmed (list in scratch/fixes1.py).
- **Round 2**: P8 keys still ended 45 px past the flow bottom — root cause
  measured with the build's own wrap metrics (keys print in serif 13.5;
  per-item advance 14 + 15.66 × lines; core fits at ≈4,769 of 4,896 px).
  22 notes shortened telegraphically (keys untouched); keys flow now ends
  y=2550 ≤ 2552, zero warnings.
- **Round 3** (occlusion audit round 1: 9 NEW flags): P1/P2/P7 box titles
  whose Dutch ink crossed box borders (ink to x=1025.5/1011.5/1949.5 vs
  borders 961/961/1885) → shortened Dutch wordings (§5), titles now inside
  their borders. P7 col-3 stack (ERRORES + LA PALABRA + CARTAS) overran the
  fixed FRASES strip by ~170 px (col3 ended 1857 vs strip ≈1686) → Dutch
  explanation lines compressed 15 → 8 lines (verified with svglib wrap at
  20.5/390); col3 now ends 1664. All TEXTX collisions cleared.
- **Round 4** (builder proofread): P7 phrase page-tags printed «(Página N)»
  (Spanish data fields missed by the CJK-driven transform) → «(Pagina N)» ×8,
  counts equal to the core.

## 9. Geometric occlusion audit (tools/occlusion_audit.py, selftest OK)

Final run over the shipped SVGs with `--core` (core: 2 flags):
**NEW vs core: 1 flag, adjudicated NON-DEFECT** —
[LINEX] p1-portada: word-of-the-week paragraph line box [64.4, 1843.4,
1885.6, 1844.6] vs the rule band. Pixel adjudication on the rendered card:
in rows 1843–1844 the only sub-200-grey pixels are the page frame and the
sidebar box borders (x≈40, 1605–1667, 1824, 1909); the paragraph's ink ends
at row 1841 with no descender ink inside the rule band — the same pattern
the programme adjudicated as a non-defect on the EN core (ink 1830–1842 vs
rule 1843–1844). The flag is a line-box/ink-box artefact, not an intersection
of actual ink.
One further edition flag is **inherited from the frozen core** (not NEW):
[BOXTITLE] p5 «Murcia y Canarias.» bottom ink 1037.5 vs border 1036.8
(0.7 px) — Spanish body text inside the DISFRACES 2026 box, byte-identical
in the shipped core; frozen, not fixable without touching the core.
Builder and audit agree: **0 unresolved NEW defects**.

## 10. Builder proofread record

Full pass over all 8 rendered cards: masthead/badge/footers correct on every
page; all Dutch glosses, ¿Y TÚ? prompts, instructions and P8 notes read
end-to-end; zero build warnings (no FLOW OVERFLOW, no HEAD TOO WIDE).
All 150 keys re-derived: 148 byte-identical to the proofread core's printed
keys (programmatic extract comparison), #137/#138 the documented Dutch
translation keys, #139/#140 stems re-aimed with keys unchanged; spot
derivations on P8 agree (e.g. #87: 31,7 + 26,8 + 18,7 = 77,2 → B; #141–144
matching c/d/b/a consistent with P6 §D). P7 phrases: the 8 Spanish quotes are
verbatim the core's, Dutch translations with (Pagina N) tags, tag counts
equal to the core's. Weekday/date claims checked against the real 2026
calendar: Fri 2026-10-23 («desde el viernes 23», frozen), Sat 10-24 (shirt
debut), Sun 10-25 21:00 (Clásico + F1), Sat 10-31 (Halloween), Mon 11-02
(holiday in 9 communities), Sun 2027-03-28 (winter time ends) — all correct.
P6 chart bars match their printed values (frozen from the core).
**Independent proofread: PASS** — see §13.

## 11. Images (credits from the core KIT §8; all placed, verified in render)

- P1: NIST atomic-clock photo (atomuhr.jpg) — public domain (NIST).
  Credit as shipped (Spanish, frozen): «Foto: NIST (EE. UU.) — dominio público».
- P3: roasted chestnuts (castanas.jpg) — CC0, Wikimedia Commons.
  Credit: «Foto: Wikimedia Commons — CC0 (dominio público)».
- P5: Halloween postcard c. 1910 (halloween1910.jpg) — public domain.
  Credit: «Fuente: Wikimedia Commons — dominio público».

## 12. PDF pins (final render)

- Print: `La-Lucerna-VOL1-NL.pdf` — **4,554,520 bytes**,
  sha256 `f3d646bb9bf3d793f2d0d3ef13ca14fe133b3ab280cfa61ef21a5907dd554d91` (D5 rebuild, 2026-11-13; see §14 D5 record)
- Web: `La-Lucerna-VOL1-NL-web.pdf` — **3,500,714 bytes** (< 10 MB),
  sha256 `effe9f9ca02abde9a25795631604b27ff392e293cedb0e5ffe4b8836706d7c0f` (D5 rebuild, 2026-11-13; see §14 D5 record)

Core integrity: core SVG sha256 set identical before/after the whole build
(§1). No repo insert and no Discord post were made (parent's steps).

## 13. Independent proofread record (2026-10-21, fresh pass, tools-mandated)

**Verdict: PASS — one complete independent pass, zero problems found; no
fix and no re-render was needed.** All gates re-run independently
(scratch: `hidden_files/proof-esnl-independent/`):

- **freeze.py baseline** (core build copy): 8/8 SVGs byte-identical to the
  shipped core; core integrity re-hashed after the run. Baseline P5:
  «desde el viernes 23» ×1, «jueves 23» ×0 (edition P5 identical).
- **freeze.py diff** reproduces §7 exactly (+29/−26 … +182/−171);
  **added CJK = 0 on all 8 pages**; P7 edition CJK total = 2, confirmed as
  the full-width parentheses of the frozen Spanish letter attribution
  «（carta de ejemplo, escrita por la redacción）», identical in the core.
  Every removed string classified: Chinese explanation layer, furniture,
  and wrap fragments; the 8 removed P7 phrase translations are the Chinese
  renderings, the 8 Spanish quotes themselves unchanged (build-level
  string comparison: all long Spanish strings of content7.py present
  verbatim in the edition build; the only absent one is a Chinese note).
- **Registry dumps from scratch copies of both builds** (one process,
  tools/README rule 7): core = edition = **150 · A2 52 · B1 70 · B2 28 ·
  per page 10/18/18/18/18/18/12/38**; type counts identical under the
  Dutch names of §4; registry keydiff = exactly **[137, 138, 150]** (the
  §4 items); no level/page/note-presence differences. Build flow logs
  confirm P8 keys end y=2550 ≤ 2552 and P7 col-3 ends 1663.96 in both
  builds; P8 last answer baseline 2535.64 in both shipped SVGs.
- **p8.py compare: CLEAN — 150 noted = 150 noted, sets EQUAL {1..150}**,
  keydiff [12, 14, 16, 17, 57, 73, 75, 83, 95, 96, 101, 105, 137, 138];
  the twelve extras were verified one by one in the SVGs (keys identical,
  Dutch notes present — they are extractor artefacts of note translation).
  #139/#140 printed keys byte-identical to the core; #150 prints
  «150. ✓ voorbeeldtekst in deel H (82 woorden)» and the Dutch intro line
  «Schrijfopdracht (geen uniek antwoord); voorbeeldtekst (82 woorden)
  hieronder.»; the frozen Spanish MODELO block is byte-identical between
  the two builds (the «Texto modelo: » label is kept by all shipped ES
  fan-outs). Items 60–63, 87, 103, 139 print language-neutral notes
  (morphology/arithmetic), identical to the core — verified individually.
  Spot re-derivations from the text agree (#87: 31,7+26,8+18,7=77,2 → B;
  #141–144 = el sondeo / el indeciso / el margen de error / la junta
  electoral, matching c/d/b/a; #57 «¡40 en toda Europa!» frozen).
- **Answer-style adjudication (§2) confirmed** against the shipped core
  P8 itself (dash style `N. key — note`, writing items `N. ✓ note`);
  recorded in tools/README item 8.
- **occlusion_audit.py** (selftest OK), edition vs core: edition 2 flags,
  core 2 flags, NEW = 1. (a) P1 LINEX — **pixel-adjudicated NON-DEFECT**:
  on the rendered card, rows 1843–1844 contain dark pixels only at the
  page frame (x≈26–40, 1910–1922) and sidebar borders (x≈1606–1666,
  1824); the paragraph's ink ends at row 1841 — identical geometry to the
  core's own flag at the same coordinates. (b) P5 BOXTITLE «Murcia y
  Canarias.» 1037.5 vs 1036.8 — the text element is **byte-identical**
  (x/y/font/size) in core and edition: inherited frozen-core graze, not
  an edition defect. No COVER/EDGE/TEXTX/FOOTER flags: the round-3 title
  shortenings, P7 col-3 compression (col-3 last baseline 1659.54, FRASES
  title at y=1724, both builds agree) and P8 flow fix all hold at ink
  level.
- **Furniture verified page by page**: badge ×1 (P1), subtitle ×1,
  footer line ×1 on all 8 pages with correct «Pagina N van 8», P8
  separators «— Pagina 1..8 —» all present, gloss prefix «Uitleg — »
  ×5 = the core's 5 gloss boxes (4 × «译注｜» + P1 «讲解｜», same
  coordinates), the three §5 wording deviations present and wording-only.
- **P7 tags**: (Pagina 1)×1, (Pagina 2)×2, (Pagina 3)×2, (Pagina 4)×1,
  (Pagina 5)×1, (Pagina 6)×1 — counts equal to the core's; zero «(Página»
  left in the edition.
- **Calendar**: Fri 2026-10-23, Sat 10-24, Sun 10-25 (Clásico 21:00),
  Sat 10-31, Mon 2026-11-02, Sun 2027-03-28 — all verified against the
  real calendar (Europe/Madrid).
- **Images**: `<image>` elements identical per page (P1/P3/P5); credit
  lines identical to the core and attached to the placed images.
- **Banned intermediary term**: 0 in the paper's SVGs and in all operative
  build code; the Chinese form 0 everywhere including this KIT. The one
  occurrence of the old method name in this KIT is the §2 rename
  disclosure itself — the same disclosure form the shipped ES×PT KIT
  uses; the scratch/transform.py search-pattern occurrences (6) stay
  confined to scratch/ as disclosed.
- **Full Dutch read** of every added string (freeze diff, all 8 pages):
  coherent, correct Dutch; no leftover Chinese explanation text.
- **PDF pins re-measured**: print `La-Lucerna-VOL1-NL.pdf` **5,801,268 B**,
  sha256 `f58dfd290e905ed43c3a46752ae761d77fc3f7abcd49556a969cd0e92c76f8e2`;
  web `La-Lucerna-VOL1-NL-web.pdf` **3,912,185 B** (< 10 MB), sha256
  `c85aa50b88354404b25691f9e92ea5d800c48b9bfd57fee838f00db4d71b4475` —
  both exactly as §12 records; both PDFs have 8 pages.

No repo insert, no Discord — parent's steps.

## 14. D5 rebuild record (2026-11-13, W43/W45/W46 D5+§1.1 joint rebuild, Phase 1)

- **Cause:** D5 defect — sans-layer Latin/Cyrillic chars landing in Noto Sans CJK instead of Newsreader (Latin readers) / Noto Sans (Russian readers). Pre-repair census for this edition: D5 Latin 494, Cyrillic 0, curly-in-CJK 0.
- **Install:** `tools/mechanism-w47/apply_variant.py --svglib <edition>/svglib.py --target es --reader nl --week 2026-w43` (after a clean `--check` dry-run). `_D5_READER = "latin"`. Routing unit test `test_d5_routing.py` FAILURES: 0. fix2 (U+201C/U+201D/U+2019 → serif) kept: this edition has 0 curly quotes.
- **Baseline:** proven clean before rebuild — `run.py` TOTAL 150, 0 warnings; `render.py` + `webpdf.py` output text-identical to the shipped edition (character-multiset diff 0); rebuilt SVGs 8/8 byte-identical to shipped. Baseline measured (shipped recipe): print PDF `a751c5961c34eddab94fdd41982b9c62f3f48550d1195f243c08971cb0d5a68c` (5,164,153 B), render web PDF `6665bf7c423664a5e91048a7b737aed1e0692400f904f0f9d3a3d2fb4b8c0b6e` (3,501,232 B). The §12 old values (5,801,268 / 3,912,185 B) are from an older recipe and are stale; the baseline values above govern.
- **Second-round fixes (font sizes only, no text change; measured advances with the patched svglib `text_w`, sans bold; column width CW=422.5, box-title inner width 404.5, P7 p.text title inner width 400.5):**
  1. `content12.py:15` masthead tagline `CADA SEMANA EN ESPAÑOL　ELKE WEEK　HET SPAANS DAT DE SPANJAARDEN LEZEN` 17→16 — D5 widened Latin (Newsreader wider than CJK SC at 17pt + letter-spacing 1.7), so the centered tagline's right end moved right and the right-aligned date's left end moved left; their gap collapsed 81.9px → −4.1px and the glyphs touched (`LEZEN` + `SEMANA` rendered as `LEZENSEMANA`, visually confirmed on the rendered P1). 16pt restores a +41.3px gap (date x=1435.0 as rendered).
  2. `content12.py:16` masthead date `SEMANA DEL 19 AL 25 DE OCTUBRE DE 2026` 17→16 (paired with the tagline; same collision).
  3. `content12.py:125` P1 head `EL OTOÑO EMPIEZA DE VERDAD` 25→24 (439.1→421.5).
  4. `content34.py:23` P3 head `RECORDAR JUNTOS　Herdenken` 25→24 (429.3→412.1).
  5. `content7.py:16` P7 head `A2　DECIR LA HORA Y EL PRESENTE` 24→21 (471.1→412.2; also clears the P7 TEXTX collision — that head overlapped `B1` by 20.5×16.8px).
  6. `content7.py:48` P7 head `B2　CREO QUE… / NO CREO QUE…` 24→23 (428.8→411.0).
  7. `content12.py:47` P1 box `LA SEMANA EN CIFRAS　In cijfers` tsize 23→22 (411.3→393.4).
  8. `content12.py:90` P1 `EN ESTA EDICIÓN　In dit nummer` p.text 24→22 (422.6→387.4; 23pt still +4.5 over).
  9. `content12.py:176` P2 box `LA FRASE PARA RECORDAR　Spreuk` tsize 23→20 (445.0→386.9; 21pt still +1.8 over).
- **P8:** lines 217→217, footer slack 56.6px unchanged; p8 compare CLEAN (keydiff [137, 138]).
- **New deliverables (D5 rebuild, 2026-11-13):** print PDF `La-Lucerna-VOL1-es-nl.pdf` sha256 `f3d646bb9bf3d793f2d0d3ef13ca14fe133b3ab280cfa61ef21a5907dd554d91` (4,554,520 B); render web PDF `La-Lucerna-VOL1-es-nl-web.pdf` sha256 `effe9f9ca02abde9a25795631604b27ff392e293cedb0e5ffe4b8836706d7c0f` (3,500,714 B); issues web PDF (`tools/webpdf.py`) `2026-w43-es-nl.web.pdf` sha256 `f9d7d20d036af3c3095c533ddfce898bb25be5fbbaa690cef573ce691d547aab` (1,065,755 B) — to be swapped into `issues/2026-w43/2026-w43-es-nl/2026-w43-es-nl.pdf` by the closer with a pin update (shipped `4a3aea12272eda5aea478ca7a0e04d03743371dd2ab50e93c3a2d4b1f4ae963a`, 1,109,277 B). Print PDF shrank ~600KB from font-subset changes (Latin moved out of the CJK font); text content unchanged (print=web text-layer multiset diff 0).
- **text.md:** D5 changes no text content; re-export after rebuild reflows line breaks (25 REWRAP), so the deliverable is the shipped `.text.md` carried over unchanged (BYTE-IDENTICAL); acceptance `verify_textexp_es.py --edition` verdict ADOPT (0 UNEXPECTED; exercise numbers 313/313 in sequence; all 8 pages token-identical). Run 1 had returned HOLD on the masthead merge (`LEZEN`+`SEMANA` → `LEZENSEMANA` in the re-export); the masthead 17→16pt fix resolves it — run 2 verifies ADOPT.
- **D5 gates (17 gates, run 2, ALL-GREEN):** run TOTAL 150, warnings 0; head_check PASS 0 defects; d5 census Latin 0 / Cyrillic 0 / curly-in-CJK 0; render RC=0; webpdf RC=0 (1,065,755 B <7MB); occlusion 0 (incl. selftest); p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8; freeze diff vs base added CJK chars TOTAL 1 (U+3000, run split); spill 0; boxtitle 0; edge 0/0; creambox PASS 0 defects (ratios n=402, median 1.040); text-layer print=web multiset diff 0; census_quotes 0 defective; family gates.py N/A. Logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-nl/` (`GATES-SUMMARY.txt` is the master table; run-1 logs archived under `run1/`). D5 report: `production/notes/2026-w43/g-es/scratch-d5-rebuild-es/D5-REPORT-2026-w43-es-nl.md`.
