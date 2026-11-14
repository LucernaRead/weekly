# Le Lucerna — Édition française pour lecteurs néerlandophones (FR × NL) — WEEKLY KIT

**Pairing:** French target text (frozen VOL.2 core, Chinese-explained) with the
complete explanation layer rewritten in **Dutch** for Dutch-speaking readers.
This is the first edition of the Dutch-explanations column; its furniture
strings (§5) are the column pattern for the later × NL editions.
**Issue:** VOL.2 — « Weekblad in het Frans · Herfst en feesten » — week of
19–25 October 2026 (W43). **Pages:** 8 (multiple of 4). **Exercises:** 145.
**Deliverables:** `svg/` ×8, `cards/` ×8 PNG 1950×2700,
`Le-Lucerna-VOL2-NL.pdf` (print), `Le-Lucerna-VOL2-NL-web.pdf`, this KIT.
**Build dir:** `hidden_files/weekly-report-fr-nl-build/`.
**Proofread status: builder's own full pass DONE (see §8); independent
proofread PASS — ZERO PROBLEMS (see §10).**

## 1. Method

Fan-out of the finalized French VOL.2 core, following the established method
of the FR × IT / FR × ES / FR × PT editions of the same core. The build
started from a copy of the core build (`weekly-report-vol4-build/`); the copy
first had to reproduce the shipped core SVGs byte-identically (gate, §2)
before any edit. As the structural template for the rewrite, the five content
files and `bslib4.py` of the FR × IT build were copied in (that edition had
already re-proved its French layer byte-identical to the core through its own
gates) and every Italian explanation string was then replaced with its Dutch
counterpart by an AST-level exact-match transform
(`scratch/transform_nl.py`, mapping in `scratch/mapping_nl.py`, 328
replacements, every mapping asserted to hit its recorded occurrence count).
The French target text, the images, the registry keys/notes' French content
and all layout geometry are frozen; only the explanation layer, the pairing
furniture and the documented registry items (§3) differ. Four further
wording-only fixes were applied after the transform (§5 deviations a–d) and
three more after the page read (§5 deviations e–g), each re-verified through
the full gate battery. The explanation-layer helper in `bslib4.py` carries
the neutral name `expl()` (as in the FR × IT build); a scan confirms the
intermediary-layer term occurs **0 times** in the paper, this KIT and the
operative build code. Final SVGs contain **zero CJK / full-width characters**
(the registry's internal type names in the build code remain the core's
strings; they never print — identical to every sibling fan-out, kept so the
registry stays field-comparable).

## 2. Baseline proof (pre-edit gate)

The unmodified copy of the core build, run from
`weekly-report-fr-nl-build/` with its output pointed at
`scratch/baseline-svg/`, reproduced all 8 shipped core SVGs **byte-identical
(sha256, 8/8)**. Shipped core hashes (re-verified unchanged after this build,
8/8):

| page | sha256 |
|---|---|
| p1-une.svg | 5f1dc8a12056a93ee851f2be3164efc1a364d918f80db2e84670862e0915cb92 |
| p2-vie.svg | b99e94bea2216ee90bb725734748d013b40632d5786e8cc2b7613f20c567b17c |
| p3-culture.svg | cb4dc01ed3479e8dccebde152dc10f413ada9f79c442eaffbfa4f8491b5fc0fc |
| p4-sport.svg | 14b128b78c179cdec00c0e9d664db68465714391be7d1ded15ffeabcb6515ad8 |
| p5-jeunesse.svg | f2d679f3a006d66ce9fd65ae7d9f73e829618a854f35a35dfdda90ff6048581c |
| p6-politique.svg | 82021a2baf6cbbd3fb848c5be6624785e0bfb3ae697fd99d5d5237bec44c2200 |
| p7-langue.svg | cb2bfc1c15d36d8eac9043ca0d7b342fa94eec9226cfd73b1a77c130ff14fa8c |
| p8-exercices.svg | 5ac98ee139a1b479bcec36a143f72634f80e6196e09e9b685ccbfff464ec8f47 |

Totals equal the core exactly: **145 exercises** (A2 55 · B1 65 · B2 25;
per page 10/16/18/18/17/18/11/37). Registry meta (level/type/page) identical
for all 145 items. Total visible characters: **46,536** (core: 40,645 ·
FR × DE: 46,370).

## 3. Key-diff registry (complete)

Registry diff NL vs core (machine-computed over all 145 items):

- **Keys differ for exactly 5 items** — the translation apparatus only:
  - #71/#72/#73 — French model answer unchanged; the apparatus suffix
    «（参考答案）» becomes « (modelantwoord) » (half-width parens, space before).
  - #132 — the item translates INTO the reader's language, so the key is now
    Dutch: « Een peiling lezen is al politiek bedrijven. »
  - #145 — key (apparatus) becomes « Open vraag — de punten staan in het
    schrijfkader en het model staat in het kader MODÈLE op deze pagina ».
- **Stems re-aimed for exactly 4 items** (French keys byte-identical):
  - #132 stem: « Vertaal naar het Nederlands: « Lire un sondage, c'est déjà
    faire de la politique. » »
  - #133 stem: « Vertaal naar het Frans: Hij is langer dan zijn broer. »
  - #134 stem: « Vertaal naar het Frans: De leerlingen hebben sinds zaterdag
    vakantie. »
  - #135 stem: « Vertaal naar het Frans: Vanavond zetten we de klokken een
    uur terug. »
- **Notes differ for 122 items**: 121 Chinese notes rewritten in Dutch,
  plus #119, whose French note text is unchanged but whose full-width
  parentheses are normalised to half-width (« s'intéresser aux (à + les) »).
  The 23 unchanged notes are all French grammar notes.
- All other 140 keys byte-identical to the core.

## 4. Printed-note parity (deliberate choice, verified)

The French core is one of only two cores whose P8 build FILTERS which answer
notes print (its rule prints 67 of 145). **Deliberate choice: this edition
prints exactly the core's 67-note set** — parity, not the print-all superset —
implemented with an explicit `PRINT_NOTES` set in `content8.py` (inherited
from the FR × IT template). Verified by extracting the printed sets from
both shipped P8 SVGs by exercise NUMBER (the note strings of #16/#118
collide; resolution is by number): core printed set = {1, 4, 17, 22, 26, 33,
35, 41, 44, 46, 47, 55, 56, 65, 71–74, 80–85, 92, 97, 105–145} (67); this
edition's printed set is **identical, 67 = 67**, re-verified on the final
SVGs after all wording fixes. Answer-key format: space before each note
parenthesis, half-width parens only.

## 5. NL furniture (verbatim as shipped) and deviations

- P1 brick badge: « TEKSTEN IN HET FRANS · UITLEG IN HET NEDERLANDS — DE
  EDITIE VOOR NEDERLANDSTALIGE LEZERS »
- Top strip: « VOL. 2 · NR. 2 »; strap: « HEBDOMADAIRE EN FRANÇAIS · ELKE
  WEEK · HET FRANS DAT DE FRANSEN LEZEN »; subtitle (46 pt):
  « WEEKBLAD IN HET FRANS · VOL.2 · HERFST EN FEESTEN »
- Countdown band: « DEZE ZONDAG · WINTERTIJD » /
  « Klokken een uur terug · zie pagina 2 »
- Footers (all pages): left « Le Lucerna · FRANS WEEKBLAD VOL.2 · TEKSTEN IN
  HET FRANS · UITLEG IN HET NEDERLANDS », right « Pagina N van 8 »
- Gloss prefix: « Uitleg — »
- Section suffixes: « · WOORDEN » (LES MOTS heads, P3/P4/P5/P6 boxes),
  débat « LE DÉBAT · HET DEBAT », drills « MICRO-DRILLS · TRAINING », levels
  « NIVEAU A2 · BASISNIVEAU » / « NIVEAU B1 · GEMIDDELD » /
  « NIVEAU B2 · UITDAGING », toolbox « BOÎTE À OUTILS · OP ZAK » (deviation
  c), clinic « CLINIQUE DES ERREURS · PAS OP! » (deviation d), graph
  « LIRE LE GRAPHIQUE · DE GRAFIEK », calendar « DATES À RETENIR · DE
  MAAND », zoom « ZOOM · GRAVEN VAN SCHRIJVERS », sommaire « DANS CE
  NUMÉRO · INHOUD », quiz « QUIZ ÉCLAIR · BLITZQUIZ », bref « EN BREF · IN
  HET KORT », P8 band « TOETS · DE ANTWOORDEN ONDERAAN DEZE PAGINA », keys
  head « RÉPONSES · ALLE ANTWOORDEN MET NOTEN (PAGINA 1–8) », separators
  « — PAGINA n — », cloze label « Opties: », instruction words
  « Vul in · Herschrijf · Combineer · Corrigeer ».
- The suffix « · WOORDENSCHAT » is kept where it fits (P6 LES MOTS section
  head, P8 F head). Dutch target names recorded for the later × NL columns:
  ENGELS, DUITS, FRANS, SPAANS, ITALIAANS, PORTUGEES, RUSSISCH, JAPANS,
  KOREAANS, CHINEES VEREENVOUDIGD, CHINEES TRADITIONEEL.

**Deviations (all wording-only, measured with the build's own metrics):**
(a) P1 trends-box title shortened to « De zoekopdrachten · Google Trends »:
the full form (« …van de week… ») measured 440.1 px against the 412.7 px
available inside the right-column box and spilled past its right border
(audit BOXTITLE flag).
(b) P1 trends-box bottom line shortened to « Meest gezocht: de
presidentsrace van 2027. » (380.9 px) — the full form ran past the page
edge (audit EDGE flag); this is the same line FR × PT had to shorten.
(c) P7 toolbox head « BOÎTE À OUTILS · OP ZAK »: the literal
« · GEREEDSCHAP » form measured 446 px > 434 px column at 27 pt
(HEAD TOO WIDE); « OP ZAK » (346 px) matches the column's own « zinnen om
mee te nemen » wording (cf. FR × PT's « PARA LEVAR » solution).
(d) P7 clinic head « CLINIQUE DES ERREURS · PAS OP! » (429.4 px at 25 pt):
the « · FOUTENKLINIEK » form measured 499 px (HEAD TOO WIDE) and
« · FOUTEN » left only 0.3 px of margin.
(e) P2 time-table row: the Dutch parenthesis reads « (overdag / 's
nachts) » — the fuller « (twaalf uur 's middags / middernacht) » form
ended at advance x = 1933, past the content right edge (1885).
(f) P2 match instruction shortened to « Combineer betekenissen » — the
full « Combineer woord en betekenis » ended at advance x = 1930 > 1885.
(g) Two P5 vocab entries drop the indefinite article for width: « un
réseau social — sociaal netwerk » (ink ends 1839 vs box border 1885) and
« une sortie — release, lancering » (ink ends 1796); with the article,
both lines' ink ended at 1882, ~3 px from the border — far tighter than
any shipped sibling (FR × IT: 1862/1815 on the same lines).
(h) P1 headline gloss compressed (the « présidentielle » word-gloss is
dropped for flow, as in FR × IT / FR × ES / FR × PT).

## 6. Images (public domain, carried from the core)

- P1 — Utagawa Hiroshige, « L'automne à Mama » woodblock print (LACMA,
  public domain).
- P2 — Eugène Atget, Paris street photograph (public domain).
- P3 — Blanco, *Flora de Filipinas* botanical plate, chrysanthemum
  (public domain).
Credit lines are printed in French in the core and are kept verbatim (they
are core text, not explanation layer). Embedded image payloads verified
byte-identical to the core on all 8 pages.

## 7. Geometric occlusion audit (mandatory gate)

Script: `audit_fr_nl.py` in the build dir (paint order, PIL real-font glyph
metrics, ink band baseline −0.88 em … +0.30 em, shape boxes expanded by half
the stroke width; classes COVER / LINEX / FOOTER / EDGE / TEXTX / BOXTITLE).
Validated first on a synthetic positive control: all defect classes fire
and the clean control page is silent — SELFTEST PASS.

- First run on this edition: 4 flags. Two were real defects, fixed by
  wording only (§5 a, b): 1 × BOXTITLE (trends-box title past its box),
  1 × EDGE (trends line past the page edge).
- Final run: **2 flags, both inherited from the core** (the core itself
  scores the same 2): P1 and P4 TEXTX nominal-band overlaps between the
  « Le Lucerna » masthead and the line below it. Pixel-adjudicated on the
  rendered P1 card: the title's actual ink ends at row 265 and the
  subtitle's ink begins at row 295 — a 30 px blank band separates them;
  NON-DEFECT (nominal-band artefact of the 178 pt masthead), identical
  geometry to the shipped core.
- A supplementary column-spill sweep (every start-anchored text node's
  advance end vs the content right edge 1885) found exactly 2 spills after
  the audit fixes — §5 (e) and (f) — both fixed by wording; final sweep:
  0 spills (the core itself scores 0).
- Build log: zero FLOW OVERFLOW warnings; the only HEAD TOO WIDE warning
  is the core's inherited, previously adjudicated P4 French headline note
  (« REGARDER UN MATCH EN FRANÇAIS », frozen French, renders fully inside
  its column). P2-ex flow ends at y = 2572, exactly the core's own end
  position.

## 8. Builder's proofread record

Full builder's pass over the rendered cards, all 8 pages read end-to-end:
all 145 answer keys verified — the registry diff against the core (§3)
proves every key outside the five documented apparatus items is the core's
own verified key, and the re-aimed items were checked in the render (#132's
Dutch key is a faithful rendering of its stem; #133–#135 keys remain the
correct French answers to the Dutch prompts; #71–#73 model answers
byte-identical, suffix only). Every weekday/date claim checked against the
real 2026 calendar (Sat 17 Oct holidays begin · Sat 24 Oct dialogue date ·
Sun 25 Oct clock change 03:00 → 02:00 · Sat 31 Oct Halloween · Sun 1 Nov
Toussaint · Mon 2 Nov classes resume — all correct); P6 chart re-added
(28 + 24 + 17 + 11 + 9 + 11 = 100); P7 phrases verified verbatim against
the core with correct page tags and occurrence counts equal to the core's
per phrase; the printed VOL.3 teaser is carried in Dutch with its substance
unchanged (Halloween Sat 31 Oct, Toussaint Sun 1 Nov, first winter-time
week); freeze check: a source-level literal diff vs the core shows every
removed string contains CJK or is build plumbing (output path, the core's
key-printing rule fragments) or the documented #119 parenthesis
normalisation / #132 stem re-aim — no French target text changed; targeted
scan for Italian residue words: zero hits; final SVGs: zero CJK, zero
full-width characters. **Independent proofread: PASS (see §10).**

## 9. Deliverable pins

| file | bytes | sha256 |
|---|---|---|
| Le-Lucerna-VOL2-NL-web.pdf | 5,955,883 | 4fa208d00df94e4f6cc97d3b68d1e3b75609d23723c225a6ef06bdf01cb2f2eb |
- D5 重建（2026-11-13，见文末 D5 节）：印 `The-Lucerna-VOL1-fr-nl.pdf` **8,680,274 字节**（SHA-256 `90b142516be6b2cbf43efd803c404ae0e5c8559a9bbbd2c5904e9c7707900c71`）；网 `2026-w43-fr-nl.web.pdf` **1,705,000 字节**（SHA-256 `6a8fec6be9a30435e8dd6f8ef9ef7ca9f4ec852dcfe99188a9e301b723383808`，< 7 MB）；text.md 与已发版 BYTE-IDENTICAL（SHA-256 `0c497143f4fbc68b130f7d6130949f084a81f631f64d5916622fff5e63184006`）。D5 前值：印 9,778,478 B（SHA-256 `246ca20c1491b7904410a4519346d95a2602b8a802d3c5b622885ca18e1426bd`）、网 1,742,059 字节（`bbbafbfd…`，issues 已发版）。

| Le-Lucerna-VOL2-NL.pdf | 9,778,478 | 246ca20c1491b7904410a4519346d95a2602b8a802d3c5b622885ca18e1426bd |

Web PDF (JPEG pages, quality 85) is 5.96 MB — under the ~10 MB Discord
limit. Scratch for this build (transform, mapping, drivers, baseline
copies, audit logs) lives in `hidden_files/weekly-report-fr-nl-build/scratch/`;
nothing was written to /tmp except the shared venv. Core files and core
build were never edited (§2 hash re-verification).

## 10. Independent proofread record — PASS, ZERO PROBLEMS

One complete, skeptical, independent pass over the final rendered artifacts
(proofreader's own tooling throughout; scratch in
`hidden_files/proof-fr-nl-independent/`). No defects found; no fixes were
needed, so the shipped artifacts are byte-identical to the builder's
deliverables and §9's pins stand as the final pins.

**Baseline, independently reproduced.** Fresh scratch copies of both builds
were run with outputs repointed to scratch: the unmodified core build
reproduced all 8 shipped core SVGs byte-identically (sha256 8/8, matching
the §2 table), and the NL build reproduced all 8 shipped edition SVGs
byte-identically (8/8). Build logs: zero FLOW OVERFLOW; the only HEAD TOO
WIDE warning in either build is the core's inherited P4 French headline
note (« REGARDER UN MATCH EN FRANÇAIS », frozen French; the ink audit
below confirms it spills nowhere).

**Freeze verdict: CLEAN.** Two independent methods agree. (i) AST string-
literal multiset diff of the two builds: the only non-CJK literals removed
are the documented #132 stem, two dict-key plumbing strings of the core's
own P8 print rule, and the output path; the 304 removed CJK literals are
the Chinese explanation layer. (ii) Word-level diff of the shipped SVG
text streams per page: every CJK-free difference hunk is parenthesis
normalisation (full-width → half-width, the family convention), the #132
stem prefix, or one guillemet inside a Dutch gloss — no French sentence,
headline, or exercise text changed anywhere. Final SVGs: zero CJK and zero
full-width characters on all 8 pages.

**Registry / key-diff verification (proofreader's own dumps).** Meta
(page/level/type) diffs: none. Totals identical: 145 (A2 55 · B1 65 ·
B2 25; per page 10/16/18/18/17/18/11/37). Key diffs EXACTLY {71, 72, 73,
132, 145}: #71–#73 keep their French model answers byte-identical with
only the apparatus suffix changed to « (modelantwoord) »; #132's key is
the Dutch « Een peiling lezen is al politiek bedrijven. » (faithful to
its stem); #145's apparatus is Dutch. Note diffs: exactly 122 items,
including #119, which is parenthesis-only (« s'intéresser aux (à + les) »).
The 23 unchanged notes were inspected one by one — all are French
grammar/form notes (conjugations, comparatif/futur labels, French
glosses); none is missed Chinese. Stems re-aimed EXACTLY {132, 133, 134,
135}, verified in the rendered P8; the French keys of #133/#134/#135 are
byte-identical to the core's and are the correct answers to the Dutch
prompts. All 145 keys were independently re-derived from the French text
during a full read of all 8 pages — every key checks out (incl. P6 chart
arithmetic 28 − 24 = 4, B + 3 = 27 > A − 2 = 26, 28 + 24 = 52 %).

**Printed-note set equality.** Extracted by exercise NUMBER from both
shipped P8 SVGs (all 145 entries segmented in order in each): core prints
{1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56, 65, 71–74, 80–85, 92,
97, 105–145} (67); this edition prints the IDENTICAL set — **67 = 67,
EQUAL**. Key format kept: space before each note parenthesis, half-width
parens only; separators « — PAGINA n — ».

**P7 phrases.** The section prints the same 7 phrases with the same page
tags as the core — « À trois heures, il sera deux heures. » (p. 2),
« Les élèves sont en vacances depuis samedi. » (p. 2), « On n'offre
jamais de chrysanthèmes pour un anniversaire. » (p. 3), « Wembanyama est
plus grand que la plupart des joueurs. » (p. 4), « Les fans attendent ce
jeu depuis des années. » (p. 5), « Si l'élection avait lieu dimanche,
pour qui voteriez-vous ? » (p. 6), « On gagne une heure de sommeil. »
(p. 1) — verbatim, and issue-wide occurrence counts per phrase are equal
to the core's (2/3/2/1/1/2/1).

**Calendar.** Every weekday/date claim verified against the real 2026
calendar (Europe/Paris): holidays begin Sat 17 Oct; clock change in the
night Sat 24 → Sun 25 Oct (03:00 → 02:00); dialogue date Sat 24 Oct;
Halloween Sat 31 Oct; Toussaint Sun 1 Nov (also the P8 cloze key #109);
classes resume Mon 2 Nov; the P3 dates box (dim. 25 / sam. 31 / dim. 1er /
lun. 2) is fully correct. The VOL.3 teaser keeps its full substance in
Dutch: Halloween Sat 31 Oct, Allerheiligen Sun 1 Nov, first winter-time
week. P6 chart re-added: 28 + 24 + 17 + 11 + 9 + 11 = 100, and the six
bar widths measure 504/432/306/198/162/198 = exactly 28/24/17/11/9/11 %.

**Geometric occlusion audit (proofreader's OWN implementation).**
Paint-order parse; true ink boxes from PIL/FreeType `getbbox` with the
ascender correction (bold faces included); line/border boxes expanded by
half the stroke width; classes COVER / LINEX / FOOTER (rule at y = 2580,
footer baseline exempt) / EDGE / TEXTX / BOXTITLE, plus a right-edge
advance SPILL sweep against the content edge 1885. Validated on a
synthetic positive control first: all 7 classes fired on planted defects,
the clean control page was silent (an initial ascender-origin bug in the
ink metric was caught by this control and fixed before the real run).
Result: **core 0 flags; this edition 1 flag** — P2 BOXTITLE: the last
Dutch line of the « ET VOUS ? · EN JIJ? » box (« laat sta je op zondag
op? Schrijf ons. », baseline 1544.6) has model ink bottom 1550 vs the box
border at 1549. Pixel adjudication on the rendered card: dark glyph
pixels end at row 1548 — the light border's first row — with zero ink at
rows ≥ 1549 and the border unbroken; and the shipped FR × ES and FR × PT
editions show the identical model measurement (ink bottom 1549.6) in the
same box. Adjudicated **NON-DEFECT** (descender graze at the border's top
row, the accepted pattern for this core), recorded here so it is not
re-flagged. The canonical shared audit tool (selftest passed) was run in
addition and produced the identical single flag and adjudication input.
The builder's P1/P4 masthead TEXTX claim was pixel-verified independently:
NL card ink ends row 265, subtitle ink begins row 295 — 30 blank rows,
non-defect. No COVER, LINEX, FOOTER, EDGE, TEXTX, or SPILL flag anywhere
in the edition.

**Builder's seven wording fixes (§5 a–g), each verified.** (a) Trends-box
title « De zoekopdrachten · Google Trends » present; no BOXTITLE flag on
P1. (b) « Meest gezocht: de presidentsrace van 2027. » present; no EDGE
flag. (c) Toolbox head « BOÎTE À OUTILS · OP ZAK » present in the render.
(d) Clinic head « CLINIQUE DES ERREURS · PAS OP! » present. (e) P2 clock-
table row « (overdag / 's nachts) » present; the edition-wide SPILL sweep
is clean, so its advance end is within 1885. (f) « Combineer betekenissen »
present; sweep clean. (g) Both P5 entries print as claimed (« un réseau
social — sociaal netwerk », « une sortie — release, lancering »), with no
box flag on P5.

**Furniture** verified string-by-string in the render: badge, strap,
subtitle, countdown band, gloss prefix « Uitleg — », footers « Le Lucerna
· FRANS WEEKBLAD VOL.2 · TEKSTEN IN HET FRANS · UITLEG IN HET
NEDERLANDS » / « Pagina N van 8 » on all 8 pages, separators
« — PAGINA n — », masthead « Le Lucerna ». Dutch completeness: every
explanation element on all 8 pages is genuinely Dutch (glosses,
instructions, exercise apparatus, readers'-corner and débat prompts, all
printed answer notes) and reads naturally.

**Images & credits.** Embedded image payloads byte-identical to the core
per page (1/1/1/0/0/0/0/0); the three printed credit lines are identical
to the core's and match the core KIT's table (Hiroshige / LACMA, Atget,
Blanco *Flora de Filipinas* — all public domain), one per placed image.

**Banned-term scan.** The intermediary-layer term occurs 0 times — in
both its Chinese and English forms — in the paper, this KIT, and the
operative build code; the explanation helper is `expl()`.

**Final PDF pins (measured by the proofreader, identical to §9).** Web:
5,955,883 B, sha256 4fa208d00df94e4f6cc97d3b68d1e3b75609d23723c225a6ef06bdf01cb2f2eb
(8 pages, < 10 MB). Print: 9,778,478 B, sha256
246ca20c1491b7904410a4519346d95a2602b8a802d3c5b622885ca18e1426bd.

**Core integrity.** The frozen core's 8 shipped SVG sha256 values were
re-verified after all proofread work and are unchanged (identical to the
§2 table).

**Verdict: PASS — one complete independent pass, ZERO problems.** Ready
for repo insert as slug `2026-w43-fr-nl`.

## 11、D5 重建记录（2026-11-13，D5-only）

SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader（SemiBold）。
施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：
`hidden_files/d5-redo/scratch-2026-w43-fr/logs/2026-w43-fr-nl/`；
逐版报告：`production/notes/2026-w43/g-fr/scratch-d5-rebuild-fr/D5-REPORT-2026-w43-fr-nl.md`。

**装机**：core 落盘 `apply_variant.py --patch-core fr --week 2026-w43`（core-fr
`svglib.py` +95/−3 行，`_D5_READER = "latin"`）；本版 `--svglib patched/…/svglib.py
--target fr --reader nl --week 2026-w43`，装后 `_D5_READER = "latin"`；路由单元测试 FAILURES: 0；fix2 块保留。
D1 组装先于安装：patched svglib 取本地 fanout D1 版，组装后与生产版 svglib 的 diff 恰为 D1 hunk 一处（28 行）。

**基线**（修前生产版）：run TOTAL 145，0 警告；印 PDF 与 `d1-fix/work/2026-w43-fr-nl/RESULT.txt`
的 shipped SHA/字节逐字节一致；印/网文字层差 0；自建网 vs issues 已发 web 非空字符差 0（仅空格差）；
修前普查 D5 拉丁 557、西里尔 0、弯引号在 CJK 0；基线 P8 noted 67/145。

**缺陷与修法**（run1 → run2 → run3；修法只动字号、盒高与间距，未动文字）：
head 9 项（共用 5 + chart 25→22、clinic 25→22、battB 24→21、F 24→23）；箱标题 7 处（COMMENTATEUR 20、TROIS DATES 21、scrutin 20、fêtes 21、zoom 21、sport 22、écrans 20）；spill ×2；run2 P2 LINEX → run3 消除。

P8：211→186 行，距页脚线余量 32.7→31.7 px。

**门禁 run3（全套 16 门 ALL-GREEN）**：run TOTAL 145、0 警告；head_check 0；
d5 census 0/0/0；render RC=0；webpdf RC=0（1,705,000 B < 7 MB）；occlusion 0 flags；
p8 extract noted 67/145；p8 compare **CLEAN**（keydiff=[71, 72, 73, 132, 145]）；freeze baseline 8/8；
freeze diff 新增 CJK 字符 0；spill 0；boxtitle 0 DEFECT（36 titles）；
edge 0/0；creambox PASS 0 defects；文字层 print=web 差 0（各 107,067 字符）；census_quotes
0 defective；fr 家无 gates.py。

**新交付物**：印 `The-Lucerna-VOL1-fr-nl.pdf` 8,680,274 字节（`90b14251…`）；
网 `2026-w43-fr-nl.web.pdf` 1,705,000 字节（`6a8fec6b…`）；text.md BYTE-IDENTICAL
（`0c497143…`）。练习仍为 145 题。
