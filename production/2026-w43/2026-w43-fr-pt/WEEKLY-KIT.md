# Le Lucerna — Édition française pour lecteurs lusophones (FR × PT) — WEEKLY KIT

**Pairing:** French target text (frozen VOL.2 core, Chinese-explained) with the
complete explanation layer rewritten in **Brazilian Portuguese** for
Portuguese-speaking readers.
**Issue:** VOL.2 — « Semanário em francês · Outono e festas » — week of
19–25 October 2026 (W43). **Pages:** 8 (multiple of 4). **Exercises:** 145.
**Deliverables:** `svg/` ×8, `cards/` ×8 PNG 1950×2700,
`lucerna-fr-pt-print.pdf`, `lucerna-fr-pt-web.pdf`, this KIT.
**Build dir:** `hidden_files/weekly-report-fr-pt-build/`.
**Proofread status: builder's own full pass DONE (see §8); independent
proofread DONE — PASS, see §10 (one explanation-layer defect found and
fixed during the proofread; §9 pins are the post-fix finals).**

## 1. Method

Fan-out of the finalized French VOL.2 core, following the established method
of the FR × IT / FR × ES editions of the same core. The build started from a
copy of the core build (`weekly-report-vol4-build/`); the copy first had to
reproduce the shipped core SVGs byte-identically (gate, §2) before any edit.
As the structural template for the rewrite, the five content files of the
FR × IT build were copied in (that edition had already re-proved its French
layer byte-identical to the core through its own gates) and every Italian
explanation string was then replaced with its Portuguese counterpart by an
AST-level exact-match transform (`scratch/transform_pt.py`, 322 replacements,
every mapping asserted to hit). The French target text, the images, the
registry keys/notes' French content and all layout geometry are frozen; only
the explanation layer, the pairing furniture and the documented registry
items (§3) differ. The explanation-layer helper in `bslib4.py` carries the
neutral name `expl()` (as in the FR × IT build); a scan confirms the
intermediary-layer term occurs **0 times** in the paper, this KIT and the
operative build code. Final SVGs contain **zero CJK / full-width characters**.

## 2. Baseline proof (pre-edit gate)

The unmodified copy of the core build, run from
`weekly-report-fr-pt-build/` with its output pointed at
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
for all 145 items.

## 3. Key-diff registry (complete)

Registry diff PT vs core (machine-computed over all 145 items):

- **Keys differ for exactly 5 items** — the translation apparatus only:
  - #71/#72/#73 — French model answer unchanged; the apparatus suffix
    «（参考答案）» becomes « (resposta-modelo) » (half-width parens, space before).
  - #132 — the item translates INTO the reader's language, so the key is now
    Portuguese: « Ler uma pesquisa já é fazer política. »
  - #145 — key (apparatus) becomes « Questão aberta — os pontos estão no
    quadro de escrita e o modelo está no quadro MODÈLE desta página ».
- **Stems re-aimed for exactly 4 items** (French keys byte-identical):
  - #132 stem: « Traduza para o português: « Lire un sondage, c'est déjà
    faire de la politique. » »
  - #133 stem: « Traduza para o francês: Ele é mais alto que o irmão. »
  - #134 stem: « Traduza para o francês: Os alunos estão de férias desde
    sábado. »
  - #135 stem: « Traduza para o francês: Hoje à noite atrasamos os relógios
    em uma hora. »
- **Notes differ for 122 items**: 121 Chinese notes rewritten in Portuguese,
  plus #119, whose French note text is unchanged but whose full-width
  parentheses are normalised to half-width (« s'intéresser aux (à + les) »).
- All other 140 keys byte-identical to the core.

## 4. Printed-note parity (deliberate choice, verified)

The French core is one of only two cores whose P8 build FILTERS which answer
notes print (its rule prints 67 of 145). **Deliberate choice: this edition
prints exactly the core's 67-note set** — parity, not the print-all superset —
implemented with an explicit `PRINT_NOTES` set in `content8.py`. Verified by
extracting the printed sets from both shipped P8 SVGs by exercise NUMBER
(the note strings of #16/#118 collide; resolution is by number): core printed
set = {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56, 65, 71–74, 80–85,
92, 97, 105–145} (67); this edition's printed set is **identical, 67 = 67**,
re-verified on the final SVGs after all wording fixes. Answer-key format:
space before each note parenthesis, half-width parens only.

## 5. PT furniture (verbatim as shipped) and deviations

- P1 brick badge: « TEXTOS EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO
  PARA OS LEITORES DE LÍNGUA PORTUGUESA »
- Top strip: « VOL. 2 · Nº 2 »; strap: « HEBDOMADAIRE EN FRANÇAIS · TODA
  SEMANA · O FRANCÊS QUE OS FRANCESES LEEM »; subtitle (46 pt):
  « SEMANÁRIO EM FRANCÊS · VOL.2 · OUTONO E FESTAS »
- Countdown band: « NESTE DOMINGO · HORÁRIO DE INVERNO » /
  « Relógios atrasam uma hora · ver página 2 »
- Footers (all pages): left « Le Lucerna · SEMANÁRIO FRANCÊS VOL.2 · TEXTOS
  EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS », right « Página N de 8 »
- Gloss prefix: « Nota — »
- Section suffixes: « · VOCABULÁRIO » (LES MOTS heads, P8 F), debate
  « LE DÉBAT · O DEBATE », drills « MICRO-DRILLS · TREINO », levels
  « NIVEAU A2 · NÍVEL BÁSICO » / « NIVEAU B1 · INTERMEDIÁRIO » /
  « NIVEAU B2 · DESAFIO », toolbox « · FERRAMENTAS » pattern replaced per
  deviation (b), clinic « CLINIQUE DES ERREURS · CLÍNICA », graph
  « LIRE LE GRAPHIQUE · O GRÁFICO », calendar « DATES À RETENIR · O MÊS »,
  zoom « ZOOM · TÚMULOS DE ESCRITORES », sommaire « DANS CE NUMÉRO · SUMÁRIO »,
  quiz « QUIZ ÉCLAIR · QUIZ RELÂMPAGO », bref « EN BREF · EM RESUMO »,
  P8 band « AVALIAÇÃO · AS RESPOSTAS, NO FIM DESTA PÁGINA », keys head
  « RÉPONSES · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8) », separators
  « — PÁGINA n — », cloze label « Opções: ».
- Note: the EN × PT edition was being built in parallel; at the time this
  edition's furniture was fixed, `files/weekly-report-en-pt/` held cards and
  SVGs but no WEEKLY-KIT, so there were no finally-shipped EN × PT strings to
  follow and the prescribed PT-column strings above stand as shipped.

**Deviations (all wording-only, measured with the build's own metrics):**
(a) The four « LES MOTS … » box titles on P3/P4/P5/P6 take the suffix
« · PALAVRAS » instead of « · VOCABULÁRIO »: at 23 pt bold the VOCABULÁRIO
form measured up to 454.8 px against the 412 px available inside the
right-column boxes and spilled past the boxes' right border (audit BOXTITLE
flags ×4); PALAVRAS measures ≤ 406.6 px and sits inside. The suffix
« · VOCABULÁRIO » is kept where it fits (P6 LES MOTS match head, P8 F head).
(b) The P7 toolbox head reads « BOÎTE À OUTILS · PARA LEVAR »: the
« · FERRAMENTAS » form measured 444.8 px > 434 px column (HEAD TOO WIDE);
« PARA LEVAR » (408.4 px) matches the column's own « frases para levar com
você » wording.
(c) Three P2 exercise instructions were compressed so each wraps to one
line; at two lines each they cascaded the P2 exercise flow 376 px past its
bottom (match block overflow in the last column). As shipped:
« Complete as frases conforme a hora. » / « Reescreva no futur proche
(aller + inf.). » / « Leia o artigo da página 2 e escolha. » — after the fix
the P2-ex flow ends at y = 2572, exactly the core's own end position.
(d) P1 headline gloss compressed (the « présidentielle » word-gloss is
dropped for flow, as in FR × IT / FR × ES): « sondage pesquisa · en tête na
liderança · un tour um turno · voter votar · un candidat um candidato. »
(e) P1 trends-box bottom line shortened to « A mais buscada: a presidencial
de 2027. » — the full form measured 491.1 px from x = 1473 and spilled past
the page edge (audit EDGE flag); the shipped form measures 348.5 px.

## 6. Images (public domain, carried from the core)

- P1 — Utagawa Hiroshige, « L'automne à Mama » woodblock print (LACMA,
  public domain).
- P2 — Eugène Atget, Paris street photograph (public domain).
- P3 — Blanco, *Flora de Filipinas* botanical plate, chrysanthemum
  (public domain).
Credit lines are printed in French in the core and are kept verbatim (they
are core text, not explanation layer).

## 7. Geometric occlusion audit (mandatory gate)

Script: `audit_fr_pt.py` in the build dir (paint order, PIL real-font glyph
metrics, ink band baseline −0.88 em … +0.30 em, shape boxes expanded by half
the stroke width). Validated first on a synthetic positive control: all
defect classes fire (COVER, LINEX, FOOTER, TEXTX) and the clean control page
is silent — SELFTEST PASS.

- First run on this edition: 8 flags. Real defects found and fixed by
  wording only (§5 a, e): 4 × BOXTITLE (vocab box titles past their boxes'
  right border), 1 × EDGE (trends line past the page edge), 1 × LINEX on the
  P6 vocab title (disappeared with the shorter title).
- Final run: **2 flags, both inherited from the core** (the core itself
  scores the same 2; FR × IT also shipped with the same 2): P1 and P4
  TEXTX nominal-band overlaps between the « Le Lucerna » masthead and the
  line below it. Pixel-adjudicated on the rendered cards: on P1 the title's
  actual ink ends at row 266 and the subtitle's ink begins at row 285 — a
  19 px blank band separates them; NON-DEFECT (nominal-band artefact of the
  178 pt masthead), identical geometry to the shipped core.
- Build log: zero FLOW OVERFLOW warnings; the only HEAD TOO WIDE warning is
  the core's inherited, previously adjudicated P4 French headline note
  (« REGARDER UN MATCH EN FRANÇAIS », frozen French, renders fully inside
  its column). All flow end positions are within their regions; P2-ex ends
  exactly at the core's own end position.

## 8. Builder's proofread record

Full builder's pass over the rendered cards, all 8 pages read end-to-end:
all 145 answer keys re-derived from the French text and matched against the
registry and the printed P8; every weekday/date claim checked against the
real 2026 calendar (Sat 17 Oct holidays begin · Sat 24 Oct dialogue date ·
Sun 25 Oct clock change 03:00 → 02:00 · Sat 31 Oct Halloween · Sun 1 Nov
Toussaint · Mon 2 Nov classes resume — all correct); P6 chart re-added
(28 + 24 + 17 + 11 + 9 + 11 = 100; #81: 28 − 24 = 4; #84: B 27 > A 26;
#85: 52 %); P7 phrases verified verbatim-contiguous against the core with
correct page tags and occurrence counts equal to the core's (2/3/2/1/1/2/1
in printed order, compared against the core — the core's phrases are its own
condensed form); the printed VOL.3 teaser is carried in Portuguese with its
substance unchanged; freeze check: a whitespace-insensitive text-stream
diff of all 8 pages vs the core shows every difference is explanation layer,
pairing furniture, a §3 registry item, or the #119 parenthesis normalisation
— no French target text changed. **Independent proofread: DONE — PASS
(see §10).**

## 9. Deliverable pins

| file | bytes | sha256 |
|---|---|---|
| lucerna-fr-pt-web.pdf | 5,939,894 | ef431d401391d2c88102d77b451c52bdb8fa8d6dcfcbd745dd6b54ca48b604e2 |
| lucerna-fr-pt-print.pdf | 9,780,768 | f7994e18436cf7e5e2101c0aed4801b05d7d1340009f19aad466c1d296040d33 |

(These pins supersede the builder's originals — 5,939,993 /
421c77c9… and 9,780,766 / 258a9619… — after the §10 proofread fix;
only the P5 SVG changed, the other seven are byte-identical to the
builder's render.)

Web PDF (JPEG pages, quality 85) is 5.94 MB — under the ~10 MB Discord
limit. Scratch for this build (transform, drivers, baseline copies, audit
logs) lives in `hidden_files/weekly-report-fr-pt-build/scratch/`; nothing was
written to /tmp except the shared venv. Core files and core build were never
edited (§2 hash re-verification).

## 10. Independent proofread record (2026-10-21) — PASS

Complete independent pass by a fresh proofreader over the rendered
artifacts; everything below was re-derived, not taken from the builder's
claims. Proofreader scratch: `hidden_files/proof-frpt-independent/`.

**Defect found and fixed (1).** The P5 fill-in word bank printed
« Complete com viral / partager / abonnés / commentaire. » — but item
#67's stem (« Une vidéo ___ est vue… ») and the edition's own key require
the feminine form « virale » (key #67, note « vidéo virale = um vídeo
viral »). The core and both sibling fan-outs (FR × IT, FR × ES) print
« virale » in the bank; the PT transform had normalised it to the
Portuguese lemma. Fixed by wording only in the explanation layer
(`content56.py`: « viral » → « virale » in that instruction line; no
geometry, no French text, no key change), the whole issue re-rendered,
and this entire pass re-run from the top on the final artifacts. Only
the P5 SVG changed; the other seven SVGs are byte-identical to the
builder's render, and the fixed build reproduces all eight shipped
SVGs byte-identically in an independent scratch copy.

**Freeze verdict: PASS.** The unmodified core build, run from a scratch
copy, reproduced all 8 shipped core SVGs byte-identically (independent
baseline proof). Element-level text diff of all 8 pages, core vs this
edition: every difference is explanation layer, pairing furniture, a §3
registry item, or the #119 parenthesis normalisation — no undocumented
French-text change. Final SVGs: zero CJK, zero full-width characters.

**Registry verification (independent dumps of both builds).** Meta
(page/level/type) identical for all 145 items; totals 145 (A2 55 · B1 65
· B2 25; per page 10/16/18/18/17/18/11/37). Key diffs exactly
{71, 72, 73 (suffix « (resposta-modelo) »), 132, 145}; stems re-aimed
exactly {132, 133, 134, 135}; note diffs exactly 122 (incl. #119,
paren-only). The 23 unchanged notes are all French grammar notes (no
untranslated Chinese). All 145 keys re-derived from the French text;
#132's Portuguese key is a faithful rendering of its stem; #133–#135
keys remain the correct French answers to the Portuguese prompts.

**Printed-note sets (extracted by number from both shipped P8 SVGs):**
core = {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56, 65, 71–74,
80–85, 92, 97, 105–145} (67); this edition = the identical set (67).
**EQUAL.** The #16/#118 note-string collision (« nous → allons »)
resolves correctly by number: #118 prints its note, #16 does not, in
both editions.

**Portuguese completeness and quality.** Every explanation element on
all 8 pages read in full: genuinely Brazilian Portuguese throughout;
zero Italian-residue markers in the full text; structural alignment
spot-checked against FR × IT (e.g. the P2 « Nota — reculer… » gloss is a
true translation of the Italian sibling's, not a copy). One minor
editorial compression noted, non-blocking: the P2 « ET VOUS ? » prompt
is shortened vs the core (the writing invitation stands; it is an
unnumbered reader prompt).

**P7 phrases.** Verbatim-contiguous with correct page tags; occurrence
counts equal to the core's per phrase — 2/3/2/1/1/2/1 in printed order,
counted programmatically over the whole issue in both editions.

**Calendar: PASS** (real 2026 calendar, Europe/Paris). Sat 17 Oct
holidays begin · Sat 24 Oct (« samedi », #140) · Sun 25 Oct clock change
03:00 → 02:00 · Sat 31 Oct Halloween · Sun 1 Nov Toussaint (P8 #109's
« domingo » correct) · Mon 2 Nov classes resume — all as printed. P6
chart re-added: 28 + 24 + 17 + 11 + 9 + 11 = 100.

**Geometric occlusion audit (proofreader's own implementation).**
Paint-order parse, PIL real-font glyph metrics, line boxes expanded by
half stroke width; classes COVER / LINEX / FOOTER / EDGE / TEXTX /
BOXTITLE. Validated on a synthetic positive control first (all six
classes fire; clean text silent — SELFTEST PASS). Result on the final
artifacts: **0 flags on all 8 pages** (the frozen core also scores 0
under real-ink metrics; the builder's 2 nominal-band TEXTX flags are
em-band artefacts — pixel check of the P1 masthead on the rendered
card: title ink ends at row 265, subtitle ink begins at row 286, a
20-row blank gap; non-defect, identical geometry to the core).

**Builder's five in-build fixes — pixel-verified on the rendered
cards.** (a) « · PALAVRAS » box titles inside their boxes: P3 ink ends
x=1856 vs border 1885; P4 1853 vs 1885; P5 1878 vs 1885; P6 1411 vs
1423. (b) P7 toolbox head ink ends 1860 vs column right 1885.
(c) P2's three instructions are single lines as shipped, and P2's last
body baseline (2528.6) is identical to the core's own — the exercise
flow ends exactly where the core's ends. (d) P1 headline gloss as
disclosed in §5(d). (e) P1 trend line ink ends x=1825, 97 px inside the
inner frame. The proofread fix's own line (P5 word bank) wraps exactly
as its pre-fix form did and raises no audit flag.

**Images and credits.** Embedded image payloads byte-identical to the
core on all 8 pages; the three placed images' printed credits match
the core KIT (P1 Hiroshige / LACMA, P2 Atget, P3 Blanco *Flora de
Filipinas* — all public domain).

**Furniture consistency with EN × PT.** EN × PT has since shipped (no
KIT yet); its P1 badge, footer pattern and « Nota — » gloss prefix —
extracted from its SVGs — are identical in form to this edition's,
modulo target language. Only trivial difference: EN × PT prints its P8
separators title-case (« — Página n — ») where this edition follows the
FR family's shipped caps style (« — PÁGINA n — »). Flagged for the
parent; no change made here.

**Banned-term scan:** 0 occurrences in the paper, this KIT and the
operative build code (re-scanned after the fix).

**Final pins (measured by the proofreader; supersede the builder's —
see §9):** web PDF 5,939,894 B, sha256
ef431d401391d2c88102d77b451c52bdb8fa8d6dcfcbd745dd6b54ca48b604e2
(< 10 MB, 8 pages); print PDF 9,780,768 B, sha256
f7994e18436cf7e5e2101c0aed4801b05d7d1340009f19aad466c1d296040d33
(8 pages). **Core integrity:** the frozen core's 8 shipped SVG hashes
are unchanged after all proofread work (start vs end hashes identical,
8/8).

**Verdict: PASS — one complete independent pass with zero remaining
problems.** Ready for repo insert as slug `2026-w43-fr-pt`
(discordThread = Français thread) whenever the parent line proceeds.
