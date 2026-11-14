# WEEKLY-KIT — Lucerna Weekly W43 · IT × PT

**Edition**: Italian target text (frozen VOL.1 core) × Brazilian Portuguese explanations,
for Portuguese-speaking readers. Week: Mon 19 – Sun 25 Oct 2026 (W43), VOL.1.
Masthead: **La Lucerna**. Pairing badge on P1; pairing label in every footer.
Build: `hidden_files/weekly-report-it-pt-build/` (copy of the core build).
Deliverables in this dir: `svg/` ×8, `cards/` ×8 (1950×2700), print + web PDF (§11).

## 1. Baseline proof (before any edit)

The unmodified copy of the core build, output repointed to a scratch dir,
reproduced all 8 shipped core SVGs **byte-identically (sha256 8/8)**:

| page | sha256 |
|---|---|
| p1-prima | bd04af2feafaa4af6cc16b8719a64d6bfe1090d229ac2cd450d42eac46b4efd5 |
| p2-vita | ff75206e7e867f68502557ea672961ae02fefdae42e78326ef2276c0e6e25c60 |
| p3-cultura | 9ce43c3d64b1ba968f72f8e250ac260a5d9720f54ceaa62b9342f3687e42f46f |
| p4-sport | aac8356c9d6a45b444f68aba877ca1ab4bf01655383f369e9a849722fbdb585c |
| p5-giovani | 079552c83f460abeffc3b22c76e84fa2768803dc7dcd3c37cae2f4d518f3d4f7 |
| p6-approfondimento | 5d553abec8d34c21a2445f8ad5bf709d43ccfa81859c33dbf02912f3c1f7fa1f |
| p7-lingua | 9b4daf7668bc6434f0c8da88fa4dfab56eff559ead46a97e20b2e2950f2b8b0d |
| p8-valutazione | 58f37fd4035d5d840b613e6c9b8016374191fcbe634fe434105c2c3abdd9bd5b |

Registry from the unmodified copy: 150 exercises; A2 46 · B1 71 · B2 33;
per page 10/18/18/18/18/18/12/38; writing model 90 words — identical to the core.
The core's shipped SVG hashes were re-verified **unchanged after all work** (§2 table).

## 2. Totals (this edition, machine-verified from the registry)

- Exercises: **150** — A2 46 · B1 71 · B2 33; per page 10/18/18/18/18/18/12/38 (= core).
- Writing model: 90 words (Italian, frozen).
- Localized exercise types: Completar 60 · Escolha múltipla 49 · Cloze 13 ·
  Combinar 12 · Formar frases 7 · Tradução 4 · Verdadeiro ou falso 3 ·
  Transformar 1 · Escrita 1.
- Instructions localized: «Complete», «Forme a frase», «Traduza», «Escreva»,
  «Verdadeiro ou falso?», match instruction «Combine».

## 3. Key-diff registry (complete; machine diff of the two registries)

Keys differ from the core at exactly **{137, 138, 150}** — the translation-type
items re-aimed at Portuguese, plus the writing apparatus:

| # | core key | PT key |
|---|---|---|
| 137 | 周日我们多睡一个小时。 | No domingo dormimos uma hora a mais. |
| 138 | 展览一直开放到四月。 | A exposição continua aberta até abril. |
| 150 | （开放题，范文如下） | (pergunta aberta — texto modelo abaixo) |

Stems re-aimed at Portuguese (keys unchanged, still the Italian target sentences):
- #139 stem: «Sábado às 18:00, Napoli contra Roma. → ___»; key unchanged
  «Sabato alle 18:00 si gioca Napoli–Roma.», note «si gioca = joga-se».
- #140 stem: «Cada número precisa ter uma fonte. → ___»; key unchanged
  «Ogni cifra deve avere una fonte.», note «dovere = dever, precisar».

Notes: 149 of 150 notes differ from the core (all translated into Portuguese);
the only identical note is #86 «5 − 3,4 = 1,6» (language-neutral arithmetic).
#150 note: «O modelo está na seção H desta página (90 palavras)»;
writing line on P8: «Exercício de escrita (sem resposta única); o texto modelo
(90 palavras) está logo abaixo.»
Key format everywhere: `N. key (note)` — space before the parenthesis,
half-width parentheses only.

## 4. Printed-note set verification

Extracted from the **rendered** P8 SVG by exercise number: this edition prints
notes for **{1..150}**; the core prints **{1..150}**. **Sets EQUAL** — the same
set as the core (the core prints all 150 notes).

## 5. Freeze check

Multiset text diff of all 8 SVGs vs the core: every differing line is
explanation layer (Portuguese glosses, instructions, notes, E TU translations,
quote translations), pairing furniture (§6), or a §3 registry item. No Italian
target text changed. Specifically verified:
- The Manovra chart caption and honesty note are **byte-identical Italian**:
  «Tre voci pubblicate nel DPB del 15 ottobre — non è il totale della manovra
  (circa 23,5 miliardi).» and «Fonte: DPB, documento mandato a Bruxelles il
  15 ottobre 2026.»
- P7 phrases: quote+page-tag pairs identical to the core's list; each quote is
  a verbatim contiguous excerpt occurring exactly 2× issue-wide (article + P7),
  with counts identical to the core's.
- Zero CJK characters in the final SVGs.

## 6. Portuguese furniture — as shipped (verbatim)

Pattern follows the shipped FR×PT prescription (its KIT §5); the EN×PT KIT was
checked and uses the same furniture family (badge/footer/gloss identical modulo
target and masthead names) — no conflict. The IT column's P8 separator style
«— PÁGINA n —» follows the shipped IT×ES precedent of this core family.

- P1 badge (strap slot, 20pt bold, brick): «TEXTOS EM ITALIANO · EXPLICAÇÕES EM
  PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA»
- P1 subtitle: «SEMANÁRIO ITALIANO · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL CINEMA»
- Top strip middle: «OGNI SETTIMANA IN ITALIANO · TODA SEMANA · O ITALIANO QUE OS
  ITALIANOS LEEM»
- Footers (all pages): «La Lucerna · SEMANÁRIO ITALIANO VOL.1 · TEXTOS EM
  ITALIANO · EXPLICAÇÕES EM PORTUGUÊS» / «Página N de 8»
- Gloss prefix: «Nota — » (the library adds it; gloss strings carry no prefix)
- Band titles: «VITA · VIDA COTIDIANA», «CULTURA · CULTURA», «SPORT · ESPORTES»,
  «GIOVANI · JOVENS», «APPROFONDIMENTO · APROFUNDAMENTO», «LINGUA · LÍNGUA»,
  P8: «VALUTAZIONE E RISPOSTE · AVALIAÇÃO E RESPOSTAS»
- P8 keys head: «RISPOSTE · RESPOSTAS — organizadas por página: busque pelo número
  do exercício»; separators «— PÁGINA n —»; page-8 subtitle note: «Uma nota breve
  em português para cada exercício · ✓ = exercício de escrita»

### Deviations from the core (all wording-only, recorded)
1. Badge sits in the P1 strap slot at 20pt (the core's slot holds its trends
   title at 22.5pt); measured fit, no geometry change.
2. P1 trends footnote shortened to «Google Trends: valores aproximados.» at
   19pt — the snapshot date stays in the frozen Italian line above it (mirrors
   the shipped IT×ES deviation).
3. P1 numbers-box title «LA SETTIMANA IN CIFRE · EM NÚMEROS» at tsize 20 and P2
   phrase-box title «LA FRASE PER RICORDARE · MACETE» at tsize 20 (full forms
   measured too wide for their boxes).
4. Overflow-driven wording shortenings (build log must show 0 warnings; every
   flow ends inside its region, P7 col 3 ends at the core's 1674):
   P1 headline gloss and numbers-box items 2/4 glosses; P2 feature gloss;
   P6 section-A instruction («Quadros acima: escolha a resposta certa.»);
   P7 B1 explanation; P7 col-3 notes (errors 3/4, word-of-week, readers' letter);
   twelve P8 notes (#23, 40, 44, 45, 46, 58, 83, 133, 134, 135, 138, 139).
5. Audit fix (§8): P1 word-of-week translation shortened to one line —
   ««Mau tempo»: chuva e tempestades: Adam.»

## 7. Images (unchanged from the core; credits from the core KIT §8)

- P1: atomic clock — assets/atomuhr.jpg (NIST-F1, NIST, Public domain).
- P3: white truffle — assets/tartufo.jpg (Commons File:Tuber Magnatum Pico.jpg,
  Public domain); Artemisia Gentileschi, Judith (Naples version) —
  assets/artemisia.jpg (Commons, Public domain).
- P5: Chaplin, The Gold Rush still — assets/chaplin.jpg (Commons, Public domain).
- Backup unused: assets/castagne.jpg (CC0). All images placed exactly as in the core.

## 8. Geometric occlusion audit (mandatory gate)

Own implementation (`scratch/audit.py` in the build dir): SVGs parsed in paint
order; glyph boxes from real-font (PIL) metrics; line boxes expanded by half the
stroke width. **Positive control first**: a synthetic SVG with six planted
defects (63% cover, footer-band intrusion, edge spill, line-through-text,
text-text overlap 66%, title straddle) — all six flagged.
Classes checked: ≥30% glyph coverage by later opaque shapes; footer band
(y>2580); page-edge spill; line-through-ink; text-vs-text overlap; box-title
ink vs its own box borders; stacked-box bottoms.
- Result on this edition (final render): **10 flags, all class F** — the same 10
  flags the audit produces on the shipped core, at the same boxes (sidebar
  box-height convention: the last line's modelled ink touches the box's bottom
  edge). Pixel checks of the P2 E TU box and the P7 readers' box show the text
  sitting inside its box with clear space — inherited design, **not defects**.
- **1 NEW defect found and fixed**: P1 word-of-week translation wrapped to two
  lines and the section rule at y≈1864 struck through the second line
  («chama-se Adam.») — pixel-verified in the rendered card. Fixed by wording
  only (§6 deviation 5); the line now sits on one line above the rule.
- Final: **0 unresolved NEW flags vs the core.** Build log: 0 overflow /
  0 too-wide warnings (the true core build also has zero).

## 9. Proofread record

- Builder's own full pass: DONE — all 8 pages read end-to-end from the rendered
  cards; all 150 keys verified against the registry and the Italian text
  (registry machine diff §3; printed key lines read individually); totals and
  levels equal the core; every weekday/date claim checked against the real
  2026 calendar (ora solare Sun 25 Oct 03:00→02:00; DPB Thu 15 Oct; Lucca opens
  Wed 28 Oct; All Saints Sun 1 Nov; Alba fair closes Sun 6 Dec — all correct).
- **Independent proofread: PASS — zero problems** (2026-10-21, independent
  proofreader; full record below as §12).

## 12. Independent proofread record (2026-10-21)

One complete, skeptical, independent pass over the final rendered artifacts.
**No defects found; no fixes were needed** — the shipped artifacts stand
exactly as the builder delivered them (edition SVGs re-hashed 8/8 unchanged
at the end of the pass). Everything below was verified independently, not
taken from the builder's claims.

- **Baselines reproduced independently**: a scratch copy of the unmodified
  core build (output repointed) reproduces all 8 shipped core SVGs
  byte-identically (8/8), registry 150 (A2 46 · B1 71 · B2 33; pages
  10/18/18/18/18/18/12/38; model 90 words), build log 0 overflow warnings.
  A scratch copy of the shipped PT build likewise reproduces all 8 shipped
  edition SVGs byte-identically (8/8), 0 overflow warnings.
- **Freeze verdict: PASS.** Element-level text diff of all 8 pages (385
  removed lines): 364 carry the core's Chinese explanation layer; the 21
  remaining are all classified — P1 strap furniture (§6), the P8 separator
  caps (§6), P8 note-format lines (dash → parenthesis, family precedent of
  the shipped IT×ES), the #86 format line, and 3 re-wrap fragments whose
  Italian words were verified to survive unchanged in this edition
  («3. Studia la mappa di Lucca e le code»; the P6 word bank
  «manovra · rinvio · miliardo · previsione»; the P7 subjunctive header).
  No undocumented Italian-text change. Zero CJK in the final SVGs.
- **Manovra caption + honesty note byte-identical Italian** — verified by
  string match and visually on the rendered P6 card: «Tre voci pubblicate
  nel DPB del 15 ottobre — non è il totale della manovra (circa 23,5
  miliardi).» and «Fonte: DPB, documento mandato a Bruxelles il 15 ottobre
  2026.»; chart components 5,0 + 5,0 + 3,4 = 13,4 against the disclosed
  total 23,5.
- **Key-diff verification** (own registry dumps of both builds): level/page
  metadata zero mismatches for all 150; key diffs exactly {137, 138, 150}
  with the §3 strings; stems re-aimed exactly {139, 140} («Sábado às 18:00,
  Napoli contra Roma. → ___», «Cada número precisa ter uma fonte. → ___»)
  with Italian keys byte-identical; notes differ in 149/150 — the only
  identical note is #86 «5 − 3,4 = 1,6», pure arithmetic in decimal-comma
  notation shared by both languages, genuinely language-neutral. #137/#138
  Portuguese keys independently confirmed faithful to their Italian stems.
  All 150 Portuguese notes read in full: genuine, accurate Brazilian
  Portuguese (arithmetic and calendar notes re-checked: 5+5+3,4=13,4;
  5−3,4=1,6; +0,8%; 3,4% do PIB; quarta-feira 21 and 28 de outubro;
  domingo 1º de novembro; 6 de dezembro — all correct).
- **Printed-note sets**: extracted by number from both shipped P8 SVGs —
  core = {1..150}, edition = {1..150}, **EQUAL**. (Core #150 prints its
  note as the ✓ model pointer; the edition prints the equivalent
  Portuguese parenthesis note — same set by number.)
- **Totals**: 150 (A2 46 · B1 71 · B2 33), per page 10/18/18/18/18/18/12/38,
  numbering continuous 1–150 in both P8 extractions.
- **P7 phrases**: all 8 quotes verbatim-contiguous in their tagged articles;
  page tags identical in both editions (1, 1, 2, 2, 3, 4, 5, 6); each quote
  occurs exactly 2× issue-wide in both editions; Portuguese gloss
  translations genuine.
- **Calendar: PASS** against the real 2026 calendar (Europe/Rome): ora
  solare Sun 25 Oct 03:00→02:00; DPB Thu 15 Oct; Artemisia Wed 21 Oct;
  Napoli–Roma Sat 24 Oct; Lucca opens Wed 28 Oct; All Saints Sun 1 Nov;
  Alba fair closes Sun 6 Dec; week Mon 19 – Sun 25 Oct.
- **Geometric occlusion audit — own implementation** (paint-order parse;
  PIL real-font **ink-extent** boxes, not advance width, bold elements
  included; line boxes expanded by half stroke width; classes COVER /
  LINEX / FOOTER / EDGE / TEXTX / STRADDLE). Synthetic positive control
  fired all 6 planted classes and stayed silent on clean text before the
  real run. Edition: **0 COVER, 0 LINEX, 0 FOOTER, 0 EDGE, 0 TEXTX** on
  all 8 pages; 5 STRADDLE-B flags, all pixel-adjudicated **non-defects** —
  sidebar last-line grazes of the family's box-height convention: P3 and
  P5 are byte-identical frozen Italian text with coordinates identical to
  the core's own 2 flags under the same audit (ink ends 1 row above the
  border); P2 ink ends row 932 vs border top ≈932.8 (clear); P7 box 1 and
  box 2: a single descender/closing-paren tip reaches the border's top
  anti-alias row over 1–2 pixels at one x-column — the glyph is painted
  after (above) the border, fully formed and legible, no glyph body
  crossed or covered (unscaled crops inspected). Core reference under the
  same audit: 2 flags (the shared P3/P5 grazes). Note: the builder's
  audit counts (10 vs 10, class F) come from a different implementation;
  the substance agrees — no occlusion defect exists in either edition.
- **Builder's claimed fix pixel-verified**: P1 word-of-week line
  ««Mau tempo»: chuva e tempestades: Adam.» is a single line (baseline
  y=1846.3); its ink ends at row 1845, the section rule sits at rows
  1863–1864 — 18 clear rows, no strike-through.
- **Images**: embedded payloads byte-identical to the core per page (the
  P3 Artemisia image's flow y shifts +29 because the sidebar text above it
  re-wraps — payload, size and crop unchanged); printed credits
  byte-identical to the core on P1/P3/P5 and matching the core KIT (NIST
  atomic clock; truffle + Gentileschi Judith; Chaplin — all Public
  Domain).
- **Furniture cross-check**: badge, footers, «Página N de 8», «Nota — »
  gloss distribution (0/1/1/1/1/1/0/0, identical to the shipped IT×ES) and
  P8 separators «— PÁGINA n —» all match the shipped EN×PT/FR×PT PT-column
  family patterns (modulo target/masthead names) — no divergence.
- **Banned-term scan**: 0 occurrences of the intermediary-layer term
  (either language form) in the paper, this KIT, and the operative build
  code; hits exist only inside `scratch/` (transform/test scripts quoting
  the core's original call strings as rename search patterns — the
  disclosed, adjudicated exception).
- **Final PDF pins (measured independently — identical to the builder's;
  no superseding render)**: web **3,635,785 B**, sha256
  `5bd79e739df2a12955ccf0c5fdcb1b0c52e20c423ef01201eeafe729b167d93d`,
  8 pages, < 10 MB ✓; print **9,080,307 B**, sha256
  `521939bccba1e33e9daf78a26ac51c9648646e2db2ff3068192fe875d33d6425`,
  8 pages.
- **Core integrity**: the frozen core's 8 shipped SVG sha256 are
  **unchanged** after all proofread work (verified at start and end).

**Verdict: PASS — zero problems. Ready for repo insert as slug
`2026-w43-it-pt`.**

## 10. Method notes

- The explanation-layer helper is named `expl()` throughout the operative
  build. The one-off transform script (`scratch/transform_pt.py`) quotes core
  call strings as search patterns during that rename; it is confined to
  `scratch/` and is not part of the edition.
- `svglib.py` is the frozen shared library, byte-identical to the core's; it
  retains two CJK characters in a code comment. Zero CJK in the final SVGs and
  in all content/apparatus code.
- `scratch/baseline-log.txt` is mislabelled (it captured a PT-content run);
  the baseline evidence is the sha256 table in §1 plus the true core build log
  captured during verification.

## 11. Deliverables

- `svg/` ×8 · `cards/` ×8 (1950×2700)
- Print PDF `The-Lucerna-VOL1-it-pt.pdf`: **7993706 bytes** (D5 rebuild),
  sha256 3545bc095caeac83cdb17ea6a1ce8c2fcd40a2166469caf98490c98bbd5ae303
- Web PDF `2026-w43-it-pt.web.pdf`: **1140731 bytes** (D5 rebuild, tools/webpdf.py shipped file, < 7 MB),
  sha256 97d324d24fdec553ca2701bdd5c4fd0186498caf90b6a87da074e7292fe4bf79 (old 3,635,785 B value was the render.py-era web PDF)

---

## 13. D5 rebuild (2026-11-13)

D5 + §1.1 合并重建记录（2026-11-13；一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑；不 commit、不 push；独立重校另派他人）。

- 装机：`apply_variant.py --patch-core it --week 2026-w43 --i-understand-this-writes-production`（core-it 落盘 `_D5_READER = "latin"`）；本版 `apply_variant.py --svglib <版>/svglib.py --target it --reader pt --week 2026-w43`，`_D5_READER = "latin"`；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2（U+201C/U+201D/U+2019 → serif）保留。
- 基线：run TOTAL 150、0 警告；SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout SHA 一致（8679477 B）；修前普查 D5 拉丁 483 / 西里尔 0 / 弯引号 CJK 0。
- 二次修复（只动字号，文字零改动；盒修法行号指 tsize 行，D19）：`content34.py:22` P3 头 25→22; `content12.py:48` P1 盒 `LA SETTIMANA IN CIFRE · EM NÚMEROS` tsize 20→18（393.9，余 10.6px）; `content12.py:91` P1 `IN QUESTO NUMERO · SUMÁRIO` p.text 24→22（381.7，余 18.8px；23pt 仅余 1.4px 太薄，不取）; `content7.py:73` P7 `ERRORI TIPICI · CLÍNICA DE ERROS` p.text 23→21（394.9，余 5.6px）; `content7.py:84` P7 `LA PAROLA · A PALAVRA DA SEMANA` p.text 23→19（378.4，余 22.1px；20pt 仅余 2.2px 太薄，不取）。
- P8：行数 200→200，距页脚线余量 56.4 px；p8 compare CLEAN（keydiff [137, 138]）。
- 新交付物：印 PDF `The-Lucerna-VOL1-it-pt.pdf` `3545bc095caeac83cdb17ea6a1ce8c2fcd40a2166469caf98490c98bbd5ae303`（7993706 B；修前 `8cb1fdebf7829e02ad880ef14471addd8e5730256ac97ff5680560ea406a374d`，8679477 B）；网 PDF（tools/webpdf.py）`97d324d24fdec553ca2701bdd5c4fd0186498caf90b6a87da074e7292fe4bf79`（1140731 B；已发版 `64d9128badb107ceaba09ee7e3b6ed04d7b9296298e3ccb85cb625919c4a3da3`，1252808 B）；text.md 与 fanout `.text.md.new` BYTE-IDENTICAL（55095 B，SHA `78af23786f12d4fd090fd47b7495c4cc5b1dab21a294cf64b0a54e9bb4454fef`），W43 it issues/ 内无已发 `.text.md`，closer 落仓时新建补入。
- 门禁 run2 ALL-GREEN（18 门：run TOTAL 150 / head_check 0 / d5 census 0/0/0 / render RC=0 / webpdf RC=0 / occlusion 0 / p8 extract 150/150 / p8 compare CLEAN / freeze baseline 8/8 / freeze diff 新增 CJK TOTAL 0 / spill 0 / boxtitle 0 DEFECT（18 titles、231 body lines）/ edge 0/0 / creambox PASS 0 defects（n=395）/ 文字层 print=web 多重集差 0 / census_quotes 0 defective / 家族 gates.py N/A / 刊头间距 197.3 px PASS）。日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-pt/GATES-SUMMARY.txt`；D5 报告：`production/notes/2026-w43/g-it/scratch-d5-rebuild-it/D5-REPORT-2026-w43-it-pt.md`。
- 本 KIT 交付物行已更新为以上 D5 新值；旧针脚为旧配方值，已过期，以上实测发运值为准。
