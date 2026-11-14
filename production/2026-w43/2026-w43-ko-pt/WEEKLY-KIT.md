# Lucerna Weekly VOL.1 — KO × PT edition (Korean target × Portuguese explanations)

- **Pairing:** target language = Korean (frozen VOL.1 core, `weekly-report-ko-vol1/`);
  reader language = Portuguese (Brazilian). Every explanation — glosses, grammar
  notes, instructions, exercise apparatus, all P8 answer notes — is written
  directly in Portuguese. No intermediary language anywhere in the pipeline.
- **Masthead:** `Lucerna` (no article, exactly as the core ships; Korean edition).
- **Build dir:** `hidden_files/weekly-report-ko-pt-build/` (copy of the shipped
  KO×IT build's code, whose Korean layer is byte-identical to the core; only the
  explanation layer was rewritten). Scratch (transform script, audit script,
  control SVG, logs, registry dumps) lives in that build dir's `scratch/`.
- **Status:** builder proofread complete; independent proofread **COMPLETE — PASS, zero problems** (2026-10-21, §11).

## 1. Baseline proof (frozen core reproduced before any edit)

The core build was copied to `weekly-report-ko-pt-build/`, its output paths
repointed to the copy's own `baseline-out/`, and run UNMODIFIED:
**8/8 SVGs byte-identical (sha256) to the shipped core SVGs** in
`files/weekly-report-ko-vol1/svg/`. Registry from that run: TOTAL 150,
A2 57 · B1 66 · B2 27, per page 10/18/18/18/18/18/12/38, writing model 162 chars.
After all work, the core's shipped SVG hashes were re-verified: **unchanged (8/8)**.

## 2. Totals (this edition = core, exactly)

- Exercises: **150** — A2 57 · B1 66 · B2 27; per page 10/18/18/18/18/18/12/38.
- Types: Complete a frase 49 · Escolha múltipla 51 · Associação 16 ·
  Transforme a frase 4 · Monte a frase 8 · Verdadeiro ou falso 4 · Cloze 13 ·
  Tradução 4 · Escrita 1. Writing model: 162 chars. Register 해요체 throughout.
- Build log: zero FLOW OVERFLOW, zero HEAD TOO WIDE warnings.

## 3. Key-diff registry (complete — registry diff vs core)

Keys are byte-identical to the core for 147 of 150 items. The only differences
are the translation items, which legitimately re-aim at Portuguese:

| # | Core key (Chinese) | This edition's key (Portuguese) |
|---|---|---|
| 137 | 台风的路径还可能改变。 | A trajetória do tufão ainda pode mudar. |
| 138 | 离考试还剩 29 天。 | Faltam 29 dias para o exame. |
| 150 | (开放题，范文如下) | (pergunta aberta — o modelo está abaixo) |

- #150's note: «O modelo está na seção H desta página (162 caracteres)».
- Stems re-aimed (keys stay the frozen Korean originals):
  #139 stem «No fim de semana, confira a previsão mais recente. → ___» (key 주말에는 최신 날씨를 확인하세요.);
  #140 stem «Na sexta-feira, vou ao Parque Haneul ver a erva-prateada. → ___» (key 저는 금요일에 하늘공원에 억새를 보러 가요.).
- All **150 notes rewritten in Portuguese** (registry note-diff count = 150/150).
  Page/level metadata diff vs core: none.

## 4. Answer-key format & printed-note set

- The core's DASH style is kept: `N. key — note`, group headings stay Korean
  «— 제N면 —», #150 prints «150. ✓ O modelo está na seção H desta página (162 caracteres)».
- **Printed-note set verified from the rendered P8 SVG** (answer entries
  extracted by number): this edition prints exactly {1..150}; the core prints
  exactly {1..150} by the same extraction. **Sets EQUAL — all 150, dash style.**

## 5. Portuguese furniture (verbatim, as shipped)

- P1 badge (23pt serif bold, measured 1338.0px, centered — fits):
  «TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA»
- P1 kicker: «SEMANÁRIO COREANO · VOL.1 · 태풍 참피 · 가을야구 · 단풍»;
  strap: «한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로» (frozen).
- P1 deck: «Confira a previsão mais recente · Preparação na pág. 2».
- Gloss prefix: «Nota — » (added by the library's expl(); strings carry no prefix).
- Section heads pair Korean + Portuguese (e.g. «문화 · Cultura», «연습 · Exercícios pág. N»);
  «당신은? · E você?»; P7 «실수 병원 · A clínica dos erros», «이번 주의 틀 · A frase-modelo»,
  «독자의 편지 · Cartas dos leitores», «다음 주 · Na próxima semana (VOL.2)».
- Footers (every page): «Lucerna · SEMANÁRIO COREANO VOL.1 · TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS»
  (21.5pt sans, measured 955.6px from x=140 — clear of the right footer) /
  «Página N de 8».
- Number format: Portuguese (551.864 · 1.312 · 75.000 · 1,5 milhão). Frozen Korean
  keys keep their own printed form (e.g. key #21 «551,864» is the Korean key itself;
  its Portuguese note uses «551.864»).
- Deviations from word-for-word translation: **none in furniture.** One wording
  shortening inside content (§7): the P7 clinic note «Em «할 수 있어요», «수» vai separado.»
  (one line, matching the sibling editions' geometry) — wording only, no geometry change.
- The four P6 «V ou F» instruction tags use the short form «V ou F» (the type name
  itself stays «Verdadeiro ou falso»), same convention as the shipped EN×PT edition.

## 6. Freeze check & language scans

- Text-node diff of all 8 SVGs vs the core: every removed/added string is
  explanation layer, pairing furniture (incl. the Korean footer «제 N 면 / 총 8 면»
  → «Página N de 8»), or a §3 registry item. **No Korean target string changed.**
- Han ideographs in the edition's SVG text: **0** (the core carries 1,976 Chinese
  explanation characters; this edition's Korean target text contains no Hanja).
- The banned intermediary-layer term (either script form): **0 occurrences** in
  the paper, this KIT, and the operative build code. The explanation helper is
  named `expl()`. The one-off transform script in `scratch/` quotes the source
  edition's original strings purely as search patterns; it is not operative code.
- P7 phrase occurrence counts vs core: **4/2/2/4/2/2/2/2 — identical** (phrases 1
  and 4 legitimately recur via deck/key stems, as in the core).

## 7. Geometric occlusion audit (mandatory gate)

Own script `scratch/audit_pt.py`: paint-order parse; text ink boxes from the
production PIL fonts (advance + PIL ink bbox, bold included); line and
border-rect edge boxes expanded by half the stroke width. Classes: COVER (≥30%),
LINEX (thin line / border edge through ink), FOOTER (ink bottom > 2580),
EDGE (page-edge spill), TITLESPILL (box title ink vs its own box, incl.
stacked-box bottoms via border edges), TEXTX (text-vs-text overlap).
**Validated on a synthetic positive control first: 6/6 planted defects caught**
(one per class).

- This edition: **1 flag** — P1 TEXTX, masthead «Lucerna» (168pt) vs the kicker
  line: the CJK ink-band model (−0.88em) overstates the Latin blackletter's ink.
- Core run through the same script: **the identical 1 flag** (same artifact).
- Pixel adjudication (rendered P1 card): masthead ink rows 144–264, kicker ink
  starts row 291 — **27px clear**. Non-defect, inherited from the frozen core.
- **Unresolved NEW flags vs core: 0.**
- One build-time geometry note: the first PT draft's P7 clinic note wrapped to
  2 lines (Italian sibling: 1), pushing P7 col3 +26.52px and the teaser box to
  y 2549.76. Fixed by wording (§5) — final P7 col3 ends 1677.24 and the teaser
  box ends 2523.24, byte-for-byte the shipped sibling geometry. All other flow
  ends match the core/sibling values (P2 col3 1164.95 accounts for its own wrap
  inside its box formula; P3 col3 1365.55 = core value).

## 8. Builder's full proofread (independent proofread complete — §11)

Read all 8 pages end-to-end from the rendered text; all 150 keys re-derived
from the Korean text and confirmed. Calendar verified against 2026: CSAT
Thu Nov 19; Oct 21 → Nov 19 = 29 days (D-29 ✓); 준플레이오프 G3 Tue Oct 20,
G4 Wed Oct 21, G5 (if needed) Fri Oct 23; playoff vs Samsung Sun Oct 25;
Korean Series from Mon Nov 2; Seoul Eulalia festival last day Fri Oct 23;
Cheongsong on-site Nov 4–8. Typhoon Champi remains an OPEN forecast in every
mention (landfall explicitly undecided). Image file-photo disclaimers intact
(P1 eye = Maysak 2015, not Champi; P5 crowd ≠ NMIXX; P6 valley ≠ Seoraksan).

## 9. Images (byte-identical payloads to the core; credits as printed)

| Page | Image | Credit (as printed) |
|---|---|---|
| 1 | Super Typhoon Maysak eye, ISS-43 (2015) | NASA — Public domain |
| 2 | Students, Sias Library | Gary Todd — CC0 · 자료 사진 |
| 3 | Quail Feeding Amidst Susuki and Kikyo, Matsumura Keibun | Public domain |
| 3 | Still Life with Apples, Cézanne | Paul Cézanne — Public domain |
| 4 | Washington baseball team | Bain News Service — Public domain |
| 5 | Fort Knox concert crowd | US Army — Public domain · 자료 사진 |
| 5 | Movie theater seats, Elijah Flores | CC0 |
| 6 | Hakkoda Mountains, Jogakura Valley (file photo) | lumoplank — CC0 · 자료 사진 |

## 10. Deliverables

- `svg/` ×8, `cards/` ×8 (1950×2700 PNG).
- Print PDF `Lucerna-VOL1-PT.pdf`: **32,303,151 bytes**, sha256 `11c1a26260e6af8955f855b143833bccd9c33e3a11c6ea0d02df4643b540a2c0` (D5 rebuild, 2026-11-13)
- Web PDF `Lucerna-VOL1-PT-web.pdf`: **2,018,022 bytes** (< 7 MB ✓), sha256 `68b65e57ed39300508d1f6befc4099fff46be12ac4473c429c22908328816e0c` (D5 rebuild, 2026-11-13)
- Independent proofread: **COMPLETE — PASS, zero problems** (2026-10-21, see §11). No fixes were required; the shipped artifacts are the builder's, byte-identical to the start of the pass.

## 11. Independent proofread record (2026-10-21) — PASS, ZERO PROBLEMS

A complete, skeptical, independent pass over the final rendered artifacts. No defect was found; no file of the edition was modified (edition SVG hashes at pass end == pass start, 8/8).

- **Baseline (re-run by the proofreader):** unmodified core build run from a scratch copy with output paths repointed → all **8/8 shipped core SVGs reproduced byte-identically**, zero overflow/too-wide warnings; registry TOTAL 150, A2 57 · B1 66 · B2 27, pages 10/18/18/18/18/18/12/38, writing model 162 chars. The operative PT build likewise reproduces the shipped edition SVGs **8/8 byte-identically** — shipped artifacts are the operative build's exact output.
- **Freeze verdict (vs the CORE, not the IT sibling): FREEZE HOLDS.** Text-node multiset diff of all 8 pages: every differing string classified as (a) explanation layer (Chinese → Portuguese), (b) pairing furniture (badge / footers / glosses), (c) paired headings whose Korean head is byte-identical, (d) documented registry items 137–140, (e) Korean article body lines (P5–P6) re-typeset by `p.text` instead of `p.para` producing character-stream-identical text (whitespace-only node differences, each verified node by node against its frozen paragraph counterpart). **Zero undocumented Korean-text changes.** Han ideographs: core 1,976, edition **0** — no Chinese explanation characters, no Hanja.
- **Registry / keys (proofreader's own dumps of both builds):** page/level metadata diffs = 0; type names a clean 1:1 CN→PT rename; **key diffs EXACTLY {137, 138, 150}** — #137 «A trajetória do tufão ainda pode mudar.», #138 «Faltam 29 dias para o exame.», #150 «(pergunta aberta — o modelo está abaixo)» with note «O modelo está na seção H desta página (162 caracteres)»; **stems re-aimed EXACTLY {139, 140}** («No fim de semana, confira a previsão mais recente.» / «Na sexta-feira, vou ao Parque Haneul ver a erva-prateada.») with their Korean keys byte-identical to the core; all other 147 keys byte-identical; all 150 notes differ (Portuguese). Printed P8 spot-verified for 137/138/139/140/150 against stems and articles.
- **Printed-note sets (extracted BY NUMBER from both shipped P8 SVGs):** core = {1..150} in order; edition = {1..150} in order — **EQUAL**; dash style and «— 제N면 —» page headings kept. Count model verified: core 150 keys with ' — ' (11 '-only' lines are wrapped-note continuations + 1 em-dash-bearing key), edition 161 such lines = 150 keys + 11 wrapped-note continuations.
- **P7 phrases:** all 8 core phrases present in both editions verbatim-contiguous on their tagged pages; occurrence counts EQUAL per phrase — **[4, 2, 2, 4, 2, 2, 2, 2] core = edition**.
- **Calendar (verified against the real 2026 calendar, Asia/Seoul):** CSAT Thu Nov 19 2026 ✓, D-29 from Wed Oct 21 ✓, G5 Fri Oct 23 ✓, playoff Sun Oct 25 ✓, Korean Series from Mon Nov 2 ✓; P4 calendar box and P8 timeline all correct. Champi remains an explicitly OPEN forecast everywhere it is mentioned (P1 headline box + teaser promise properly forward-looking).
- **Geometric occlusion audit (proofreader's own implementation):** paint-order parse, PIL real-font INK boxes (bold included, INK extent not advance width), line/border boxes expanded by half stroke width; validated on a synthetic positive control first — all 6 planted defect classes fired (COVER, LINEX, BORDERX, FOOTER, EDGE, TEXTX), all clean controls silent. **Core: 0 substantive flags. Edition: 0 flags on all 8 pages.** Pixel adjudications on the shipped cards: (1) the builder's sole em-band flag (P1 masthead vs kicker) — masthead ink rows 144–265, kicker ink starts row 291, clear gap, NON-DEFECT (identical geometry in the core); (2) P2 D-day adjacency — sentence ink ends row 1797 vs rule rows 1803–1805, zero contact, NON-DEFECT; (3) the builder's in-build P7 fix — clinic note «Em «할 수 있어요», «수» vai separado.» is a single line, column-3 geometry byte-equal to the core's; teaser rect bottom at card rows …–2522 (≈ claimed 2523.24), zero interior ink between the teaser and the footer band. P1 search-box gloss area additionally inspected: the PT gloss «Quatro palavras: os temas desta edição.» sits on its own line, no collision with the source line.
- **Full-text read (all 8 pages, all 1,369 extracted lines):** Portuguese is genuine, complete, idiomatic Brazilian Portuguese for every explanation element (glosses, notes, clinic, keys apparatus, section-H intro); Korean text matches the frozen core throughout; the VOL.2 promise in the letters box («O VOL.2 publicará cartas de verdade e a melhor redação da pág. 8!») is present. Furniture verified string-exact against the shipped PT convention: badge «TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA», footers «Lucerna · SEMANÁRIO COREANO VOL.1 · TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS» / «Página N de 8», gloss prefix «Nota — », P6 tags «V ou F», masthead «Lucerna».
- **Images:** embedded payloads byte-identical to the core per page (P1 1, P2 1, P3 2, P4 1, P5 2, P6 1, P7 0, P8 0); every printed credit matches a placed image and the KIT §9 table.
- **Banned-term scan:** the intermediary-layer term = **0 occurrences** in the paper, this KIT, and the operative build code (both script forms).
- **PDF pins (measured by the proofreader):** web `Lucerna-VOL1-PT-web.pdf` = **3,102,816 bytes**, sha256 `20ae1dd972723d82c31ff88a36bd0aea18508be6301a7423e234d64b18ea834b` (< 10 MB ✓); print `Lucerna-VOL1-PT.pdf` = **34,455,961 bytes**, sha256 `0ec4749458ff88fde19199bd96f82e585a1b301ebec52d5902c60251ef17da6b` — both exactly as the builder claimed.
- **Core integrity:** the core's shipped SVG sha256 set at pass end == pass start (8/8 unchanged). The frozen core was never edited; verification builds ran only from scratch copies with repointed outputs.

**Verdict: PASS — one complete independent pass, zero problems. The edition is ready for repo insert by the parent line.**

## 12. D5 rebuild (2026-11-13)

D5 rebuild (2026-11-13–14；builder：W43 ko 家三任；不 commit、不 push；独立重校另派他人；入仓由 closer 做）。D5 报告：`production/notes/2026-w43/g-ko/scratch-d5-rebuild-ko/D5-REPORT-2026-w43-ko-pt.md`；门禁日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-pt-run2/GATES-SUMMARY.txt`。

- 装机：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`；core-ko 落盘同模板（`production/2026-w43/core-ko/svglib.py`，+333/−40）。路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 保留（`_QUOTE_CLS` 在位）。ko-ru 无 fix-xru（W43 重建标准，见家族报告 §0）。
- 基线：`run.py` TOTAL 150、0 警告（fr 例外：基线唯一警告为 port 已知良性 HEAD TOO WIDE，见 D5 报告 §二）；修前普查 D5 拉丁 424、西里尔 0、弯引号在 CJK 0；基线印 PDF 34,439,664 B、sha256 `5f1de259ca533d01e4a607f9dd7cd8bfe2784e1e2291ae40b0c4763b7681fa80`；基线网 PDF 2,113,789 B、sha256 `494f51047e8545c33a53835cdac0d7f182902aa760ce905ef4c19c83da7a157a`。
- 缺陷与修复（只动字号，文字内容未动）：
- run1 无真缺陷；唯一 FAIL 为门 17 缺脚本 SKIP（production 与 fanout 均无 `audit_ko_pt.py`），不是 FAIL，不阻塞。
- 门禁 run2：PASS=18 FAIL=1（run1：PASS=18 FAIL=1）。run TOTAL 150；head_check PASS 0 defects；d5 census 0/0/0；render RC=0；webpdf RC=0（2018022 B <7MB）；occlusion 0；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff vs base 新增 CJK 0；spill 0；boxtitle 0 DEFECT；edge 0/0；creambox PASS 0 defects（ratios n=376，中位 1.008，粗体 1.04，常规 0.988；P8 214→219 行，距页脚线余量 62.7px）；文字层 print=web 多重集差 0（各 28742 字符）；census_quotes 0 defective；D18 刊头间距 GAP=336.6；门 17：SKIP（无此脚本）。
- 新交付物（实测发运值）：印 PDF `Lucerna-VOL1-PT.pdf` 32,303,151 B、sha256 `11c1a26260e6af8955f855b143833bccd9c33e3a11c6ea0d02df4643b540a2c0`；网 PDF `Lucerna-VOL1-PT-web.pdf` 2,018,022 B、sha256 `68b65e57ed39300508d1f6befc4099fff46be12ac4473c429c22908328816e0c`（<7MB，待 closer 换入 `issues/2026-w43/2026-w43-ko-pt/2026-w43-ko-pt.pdf` 并更新 pin）；新建 text.md `2026-w43-ko-pt.text.md` 21,674 B、sha256 `2c3a4c1254545c1b535f533cab7aace885c2138bd0b764ec5133e415d687a272`，与 fanout `.text.md.new` BYTE-IDENTICAL，`verify_textexp_ko.py --edition` ADOPT。
- KIT 旧值（印 34,455,961 B / 网 3,102,816 B，旧配方）已过期——基线实测印 34,439,664 B。本节交付物行已更新为上述 D5 新值。
