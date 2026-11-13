# GATE-LOG — W47 es-ko proof3（fix1 后独立复校）

- 对象：`production/2026-w47/2026-w47-es-ko/`；印刷 `La-Lucerna-VOL4-es-ko.pdf` 8,873,692 B
  SHA-256 `2c98a0f8f49e2e4519acdbe56b54702a315b0eb9777223c166775d88f86fcb43`；
  网页 `La-Lucerna-VOL4-es-ko-web.pdf` 1,236,860 B
  SHA-256 `2c9a90e05f99fe3a4ed024878bb229fac46042644e1bf57fef4d06e11ec0f008`；
  `2026-w47-es-ko.text.md` 47,385 B（1,823 行）
  SHA-256 `a24b79b064896d11b6ba57f5b8f6d0f12047816b78551c76ec93a141787123d6`。
  动工前与收工后两次实测三 SHA 与任务书一致，方可开工 ✓；收工复核
  mtime 未变（13:44–13:47），生产文件零改动。
- 核心 es 未变：freeze-diff（core-es 基线）新增 CJK 3,458 全部入账；
  与 proof2 的 multiset 差分恰为 4 处修复的字符（见 freeze-diff 节）。
  另：整个 `production/2026-w47/` 在本克隆中为 untracked（`??`），
  无已提交基线可 diff——核心未变以 freeze + multiset 差分为据。
- 探针：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git
  hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`
  rc=0（开工与收工两次一致）；scratch 真实写文件 ✓；
  全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
  解释器一律 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0）。
- 工作区：任务书指定的 `scratch-proof-es-ko2/` 已被 proof2 交付件占用
  （PROOF-NOTE.md / GATE-LOG.md，mtime 2026-11-11 13:30），
  本轮未覆盖、未改动；全部工作落在 `scratch-proof-es-ko3/`，
  交付件为此目录下的 PROOF-NOTE.md + GATE-LOG.md。
- 工具来源：`tools/occlusion_audit.py`、`tools/p8.py`、`tools/freeze.py`、
  `tools/webpdf.py`（共享工具）；`creambox.py` / `creambox_diag.py` /
  `boxtitle.py` / `keycheck_ast.py` / `reg_dump.py` /
  `freeze_direct_es.py` / `sweep_de.py` / `svgtext.py` / `cjk_audit2.py`
  复用自 proof2 scratch（复制到本 scratch，未改动原件；
  `cjk_audit2.py` 仅改其硬编码的 JSON 路径指向本轮文件）；
  `gates.py` / `minfont.py` / `orphan_scan.py` / `orphan_scan2.py` /
  `extract_text_es_ko.py` / `check_p8keys.py` 复用自 fix1 scratch；
  `probe_nodes.py` 为本轮新写（SVG 节点基线转储）。
- KIT 与 FIX-LOG 核对：KIT §1/§3 已更新为 build-3 SHA 与修正计数；
  KIT §1 三 SHA 与磁盘实测逐一一致 ✓；§3 papeleta 2 / plazo 3 /
  censo 2 经 P5 SVG 子串计数复核一致 ✓（另 P1 reflexión 2）。

## 机械门结果（实跑）

| 门 | 结果 |
|---|---|
| run.py（build-copy 中跑，生产文件只读） | rc=0，0 OVERFLOW / TOO WIDE，TOTAL 150（A2 50 / B1 72 / B2 28；按页 10/18/18/18/18/18/12/38）；P8-keys y=2538（bottom 2560，余 22px）；P8-ex y=872；MODELO words 97 ✓（`logs-run.txt`） |
| render.py（build-copy 中跑） | rc=0；重建印 PDF 8,873,692 B，SHA `2c98a0f8…` 与交付件完全一致；重建网 PDF 1,236,857 B（交付件 1,236,860 B，字节不同属预期） |
| SVG freeze（build-copy 重建 vs 交付 SVGs） | 8/8 byte-identical ✓ |
| SVG 变化 vs fix1-BEFORE | 仅 P1/P2/P4/P8 变化；P3/P5/P6/P7 字节一致 ✓ |
| occlusion 审计（正式，未加 --selftest；工具内置自检通过） | 0 flags ✓（`logs-occlusion.txt`，自检 6 类阳性全触发） |
| p8 extract | 150/150 ✓（`p8extract.json`） |
| p8 compare（vs core-es） | CLEAN，keydiff=[137, 138]（与 KIT §6.12 一致，翻译键重定向） ✓ |
| freeze baseline | 8/8（上行重建比对） ✓ |
| freeze diff（core-es → es-ko） | 新增 CJK 3,458 = 韩语音节 3,457 + U+3000 ×1，未入账 0；西班牙文本丢失 0（D-02 已恢复；见下） |
| freeze_direct（`freeze_direct_es.py`） | 渲染层 8/8 PASS（frozen 151/143/141/144/139/172/115/478，均 ≥100）；源码层严格匹配 FAIL，裁定见下 |
| creambox 严格口径（`creambox_diag.py`） | 27 框全部 clearance 为正，最小 +1.9（P3/P5 ¿Y TÚ? 框）；P7 工具盒（CARTAS）+5.7，与 proof2 数字一致 ✓（另 P1 两处 -999 为无文图框，见下） |
| boxtitle 全标题 text_w 实测 | 25 fit / 0 over；最紧 P5 "EL PLAN DE LA SEMANA　이번 주 계획" 403.8/404.5，余量 +0.7 ✓ |
| 印/网文字层逐页比对 | pdftotext plain 各 48,365 B 字节一致；layout 版各 107,964 B 字节一致；逐页 8 页字符数逐页一致（4356/4652/3745/4044/4079/4968/4467/9612）；重建网 PDF plain 亦与交付印 PDF 字节一致 ✓ |
| 导出器重跑 | 修复版 `extract_text_es_ko.py` 重跑导出，与已发 text.md **字节一致** ✓ |
| P8 最小字号实测 | 10.125pt（PyMuPDF，印/网一致），0 低于 9.75pt 下限 ✓ |
| VOL 号 | VOL.4 ×9，VOL.5 ×3（均为下期预告正当引用），与 proof2 一致 ✓ |
| "12 de noviembre" | 0 处 ✓ |
| §1.1 字体/配色 | 印 PDF：Newsreader / Noto Sans CJK SC / Noto Serif CJK SC / UnifrakturMaguntia ×1；纸色 #fbfaf6 8 页全有 ✓（D5 仅记录） |
| U+FFFD | 8 个 SVG 0，text.md 0，印/网 PDF 文字层 0 ✓ |
| 孤儿标点全扫（视觉行口径 orphan_scan2） | 0 ✓；节点级 orphan_scan 16 条均为同行节点伪影，旧 D-03/D-04 坐标无命中 |
| sweep | box-vs-hline 0 / bridge orphans 0 / bridge widows 0，20 桥 ✓ |

## 4 处修复逐项重验（源行 + 渲染 + 文字层三源）

### D-01（content34.py:101，P8 #45 补 `예요`）

- 源行实测：`"장소가 앞에, 동사는 두 번째예요"`；BEFORE 行
  `"장소가 앞에, 동사는 두 번째"`（`source-lines-BEFORE.txt`）。
- 渲染（`logs-nodes-d01-d04.txt`）：P8 SVG y=1599.78
  `45. En Bilbao toca la banda el domingo. — 장소가 앞에, 동사는 두 번째`，
  次行 y=1615.44（x=538.5）独留 `예요`；#44 次行 y=1570.12
  `두 번째예요`；#133 y=2001.94 单行完整式
  `시간이 앞에, 동사는 두 번째예요`。
- 文字层：text.md L1651–1652 `…두 번째` / `예요`；印/网 PDF
  pdftotext plain 字节一致。
- 溢出：P8-keys y=2538，余 22px；occlusion 0；P8 卡片目视无溢出。
- 多行键计数更正见 O-1（FIX-LOG 的 6→7 不可复现）。

### D-02（content34.py:200，P4 桥接句恢复术语）

- 源行实测：`e.bridge("과거형(pretérito indefinido)으로 바꾸세요.")`；
  BEFORE 为 `문장을 과거형으로 바꾸세요.`。
- 渲染：P4 SVG 单节点 y=1943.5（x=989.0，sans 20.5）
  `과거형(pretérito indefinido)으로 바꾸세요.`，单行；
  P4 卡片目视该句在 `D　EL PRETÉRITO INDEFINIDO` 标题正下方、单行。
- 真实 `wrap()` 复测（`bslib4.wrap`，sans 20.5，CW 422.5）：
  新句 1 行；被拒方案
  `문장을 과거형(pretérito indefinido)으로 바꾸세요.` 确为 2 行、
  尾行独留 `요.`——去宾语是必要的。
- 其余 19 桥接句未受影响：sweep 20 桥 0 orphans；排序 diff 仅此一处
  桥接句变化；SVG 全文 `pretérito` 出现 1 次（即此句）；
  freeze-diff 证实无西班牙文本丢失（`core has 'pretérito indefinido':
  True | edition: True`）。

### D-03（content12.py:47，P1 数字框 `(선거 13일)`）

- 源行实测：`13 — días faltan el lunes 16 para las elecciones del domingo 29(선거 13일)`；
  BEFORE 为 `(선거까지 13일)`。
- 渲染：P1 SVG y=1386.84 同行
  `elecciones del domingo 29(` + `선거` + `13` + `일` + `)`；
  y=1414.5 处无任何节点（区间内下一节点 y=1425.38，另一栏）。
- 真实 `wrap()` 复测（serif 20.5，内宽 386.5）：改后 2 行
  `['13 — días faltan el lunes 16 para las',
  'elecciones del domingo 29(선거 13일)']`；
  改前 3 行、尾行独留 `)`。
- 目视：P1 卡片该条两行，`)` 收在行末。

### D-04（content12.py:185，P2 日历框 `성 체칠리아 축일`）

- 源行实测：`…; 성 체칠리아 축일)`；BEFORE 为 `…; 성녀 체칠리아 축일)`。
- 渲染：P2 SVG y=1084.88 同行
  `일` `: ` `바르사` `대` `비야레알` `; ` `성` `체칠리아` `축일` `)`，
  `축일)` 完整落同一基线；y=1113.44 处无任何节点
  （区间内仅 y=1080.34 与 y=1116.82 的另一栏节点）。
- 真实 `wrap()` 复测（serif 21，内宽 386.5）：改后 3 行、末行
  `일: 바르사 대 비야레알; 성 체칠리아 축일)`；改前 4 行、末行独留 `일)`。
- 未动项：P5 计划框第 5 条（`content56.py:27`）仍为 `성녀 체칠리아 축일`，
  `wrap()` 复测 3 行、末行 `야레알; 성녀 체칠리아 축일)` 完整；
  P5 SVG y=747.28 `축일` + `)` 同行；P5 卡片目视完整。
- 目视：P2 卡片 Domingo 22 条末行 `…성 체칠리아 축일)` 完整。

## 仅 4 处变化的独立证明

- 交付 text.md vs fix1-BEFORE（`text-md-BEFORE.md`）排序 diff
  （`text-sorted.diff`，25 行）：仅 4 个修复区 + exporter 带分隔空行。
  原文 diff 的其余行移位均为带分隔符重排，无内容变化。
- SVG 变化 vs BEFORE：仅 P1/P2/P4/P8；P3/P5/P6/P7 字节一致。
- freeze-diff multiset 差分（proof2 → 本轮，逐页）：
  p1 {까 −1，지 −1}，p2 {녀 −1}，p3 {}，p4 {문 −1，장 −1，을 −1}，
  p5 {}，p6 {}，p7 {}，p8 {예 +1，요 +1}；合计 3,462 → 3,458。
  恰为 4 处修复的字符，其余 0。
- freeze-direct unaccounted 差分（proof2 → 本轮）：移除 5 项完全相同；
  新增 130 vs 128，新增项恰为 D-01 注文、D-02 桥接句、D-03 新串、
  D-04 新串 4 项，消失项恰为 D-03/D-04 旧串 2 项。

## freeze diff 明细

- 逐页 added CJK：p1 216 / p2 369 / p3 246 / p4 250 / p5 333 /
  p6 120 / p7 500 / p8 1424；TOTAL 3,458。
- 分类（`cjk_audit2.py` 改指本轮 JSON 后重跑，`logs-cjk-audit.txt`）：
  韩语音节 3,457 + 全角空格 U+3000 ×1；非韩文/空格 0；distinct 318。
  注意：未改路径初跑误读 proof2 的 JSON（3,462），已更正。
- 西班牙文本丢失 0：`core has '把句子改成过去时': True | edition: False`
  为核心中文桥接句的翻译形态（D-02 已恢复括号术语）；
  `pretérito`/`indefinido`/`Lucía`(×2)/`Diego`(×3)/`UNESCO`(×5)
  在版内全文均存在。

## freeze_direct 源码层裁定

- 工具 `freeze_direct_es.py` rc=1：`source level: FAIL; rendered: 8/8`，
  渲染层 frozen 151/143/141/144/139/172/115/478（sha8
  f9d7e9c3/c9ecac2b/fb35d9ae/2fa4d777/db2b4fdc/3580e6c4/93d341a3/87b24929）。
- Removed 5 项：与 proof1/proof2 完全相同的 5 项——页脚韩文版式改写；
  `La-Lucerna-VOL4-web.pdf` / `La-Lucerna-VOL4.pdf` → es-ko 文件名；
  Marta 信全角括号→半角（KIT §6.9 已裁定）；
  `版／共` → ` 면 / 총 `（韩文页码行家具）。5 项全部有出处，非内容改动。
- Added 130 项（proof2 为 128；+2 恰为 D-01/D-02 新串，另 D-03/D-04
  旧串换新串）：拉丁词（≥2 字母）大小写不敏感核对 core 文本节点 +
  core 源码字面量，**0 个 core 外拉丁词**（即无新增西班牙语文本）；
  新增内容均为韩文讲解、韩文注与 core 西班牙语片段的拼接。
  两项 `middle`/`sans` 为工具自 SVG 属性收获的旧有单列项，
  proof2 名单中亦有，非新增西班牙语。
- 结论：freeze_direct 源码层按裁定 PASS（工具的严格精确匹配不适用于
  es fan-out 的拼接式字面量）；渲染层 8/8 PASS。

## creambox 逐盒裁定

- 严格口径（框内末基线 vs 框底）27 框：P1 +45.7 / +8.0 / +16.0 / +44.0；
  P2 +46.6 / +47.7 / +5.3 / +5.6；P3 +47.7 / +5.3 / +1.9；P4 +47.7 / +110.8 / +5.7；
  P5 +46.6 / +47.7 / +5.4 / +1.9；P6 +55.7 / +19.4 / +35.2 / +35.2；
  P7 +42.5 / +26.5 / +5.7。最小 +1.9（P3/P5 ¿Y TÚ? 框），全部为正。
  与 proof2 逐盒数字完全相同。
- P1 两处 STRICT -999（x=88 y=1874、x=362 y=1999）为无文图框（插图区），
  框内无文本节点；图注文字在框底之外（y=2218 起），属版式设计，与 proof2
  完全相同，非溢出。
- creambox.py 6 条 raw 负值：P1 四条（AHORA TÚ / EN ESTA EDICIÓN /
  LA PALABRA / urna 图注）、P2 一条（DECIR LA HORA）、P3 一条
  （LO QUE QUEDA DE NOVIEMBRE）——均为下一框标题或框外图注落入 +45 窗口
  的伪影（KIT §8 已注），严格口径已排除；与 proof2 完全相同。
- 关键框末基线：P2 日历框 last_in=1084.9 last='축일'
  （STRICT +46.6）；P5 计划框 last_in=747.3 last='축일'（STRICT +46.6）。

## 孤儿扫明细

- 视觉行口径 `orphan_scan2.py`：TOTAL orphan flags: 0。
- 节点级 `orphan_scan.py`：16 条，全部为同行节点伪影——
  `)` 单节点但与同行文本同基线（如 P2 y=1085.0 即 D-04 的 `축일)` 之
  `)` 节点，y=1084.88 与 `축일` 同行；P5 y=747.5 同理；其余为
  日历/计划框内 `(…)` 行尾 `)` 节点与 P8 `분`/`춤` 键行内节点）。
  旧 D-03 坐标 y=1414.5 与旧 D-04 坐标 y=1113.44 均无命中。
- 弯引号：沿用 proof2 结论（CJK 节点内 0；仅 P8 Q91 两对在 Newsreader
  节点，合格）；本轮未引入新引号（排序 diff 证实仅 4 处变化）。

## keycheck（150 题三源一致）

- 源码 REG：AST 提取（`keycheck_ast.py`），content12 Q1–28、
  content34 Q29–64、content56 Q65–100、content7 Q101–112、
  content8 Q113–150，共 150。
- 结果：exact match **149/150**，唯一差异为 Q150（开放写作题，REG 键
  `(열린 문제 — 모범 답안은 아래에 있어요)`，P8 印 `✓`，属预期），rc=0。
  import 式 `keycheck.py` 仍跑不通（stub_bslib 缺 `illus_voto`），
  沿用 AST 版，结果等价。
- 逐题语义手验（text.md 全文通读 + REG 150 行逐行核对 + P8 键对照）：
  Q1–6 日期键 13/29/19/16/20/15 全对；Q7–10 选项键 C/B/A/B 全对；
  Q11–20 填空键（16/19/29/22/noviembre/empieza/dura/vuelve/recorren/llega）全对；
  Q21–24 B/A/C/B 全对；匹配题 25–28（c/b/d/a）、52–55（c/b/a/d）、141–144
  （c/d/b/a）对照 SVG 选项原文逐一核实，定义与键一致；
  Q29–33 判断题（V/V/F/F/V）与正文一致；Q34–38（cante/baile/guitarra/palmas/
  compás）全对；Q39–42（B/A/C/B）全对；Q43–46 造句键全对；
  Q47–51（A/B/C/A/B）全对；Q56–59（más importante/muchísimos/peor/mejor）全对；
  Q60–64 过去时（ganó/recibió/perdió/volvió/cerró）全对；
  Q65–69（B/A/C/B/A）全对；Q70–75（correo/papeleta/envío/identidad/censo/plazo）全对；
  Q76–79（ir a + 不定式）全对；Q80–82（V/F/V）全对；
  Q83–92（A/B/C/A/B/C/B/A/C/B）全对，其中 Q87 45−30=15、
  Q89 唯一已确认辩论为 laSexta 场、Q91 «propuesto»≠«cerrado»；
  Q93–100（tenga/sea/para que/Aunque/sondeo/muestra/indecisos/margen de error）全对；
  Q101–104（Es/Son/las/B）全对；Q105–108（más goles/tan rápido/mejor/B）全对；
  Q109–112（baje/sea/es/B）全对；Q113–120（A/B/A/A/A/B/A/A）全对；
  Q121–128（A/B/A/C/B/C/B/C）全对；Q129–132 对照 P8 C 阅读段（Lucía 在塞维利亚
  看德比、Diego 在马德里看 Madrid–Celta、两人都读纲领、标题«Dos ciudades,
  un sábado»）键 A/A/A/B 全对；Q133–136 造句键全对；Q137/138 韩文翻译键
  （已裁定的重定向键）与 Q139（hasta el jueves 19，C2 改动已同步）Q140 全对；
  Q145–149 对话填空（votar/identidad/urna/sobre/cierra）全对；Q150 开放写作题。
  **150 题键无一错误。** P8 韩文注逐条读过，仅 D-01 已修复；
  其余注均完整准确。
- 图表加总复核：RTVE 分钟 45+45+30+30+15+10×3=195（Q84 B、Q87）；
  禁止公布民调 24–28 日共 5 天（Q86 A）；H 范文 run.py 实测 97 词，
  与版内 “97 단어” 一致。

## 全文复读与 8 页目视（完成）

- text.md 1–1823 行全文通读：P1–P8 内容、日期、数字、韩文注、图注、页脚全部读过；
  无国际政治内容（仅西班牙国内选举）；P7 FRASES 8 句逐句与正文核对，逐字一致，
  韩文译准确；P8 C 阅读段与题 129–132 一致；H 范文覆盖 lunes 16、viernes 20、
  voto del 29。
- 8 页目视：build-copy cards/*.png（1950×2700 渲染，下采样 1100×1523
  阅览版存 `cards-view/`）逐页读过。除 D-01～D-04 四处修复点外，
  无溢出、无重叠、无页脚侵入；P6 图表条长与分钟数成比例（45/45 等长、30/30
  等长、15 短；5/15/1 成比例）；P1 插图为编辑部线描并注明非照片；
  P3/P5/P7 图注均有 PD 来源；P5 框题单行容纳（目视与 +0.7 余量一致）；
  P4 D 节标题 `EL PRETÉRITO INDEFINIDO` 在桥接句正上方。
- 旧有残留（非缺陷，见 PROOF-NOTE O-2）：P2 日历框 Lunes 16 条末行独留
  `제안)`（2 音节 + 右括号），proof2 版已存在，本轮未引入、未改动；
  不在孤儿门（独行 `)` / 独行单音节）定义内。

## 多行键计数更正（O-1 详证）

- FIX-LOG 称“P8 multi-line items 6 → 7（#45 joins #32, #44, #82, #92,
  #139, #140）”。用 fix1 自带的 `check_p8keys.py` 重跑：
  交付件得 **5 项**（`logs-p8keys-fix1method.txt`），proof2 build-copy 得
  **6 项**，两次名单互不相同。
- 原因：该脚本按 y±2 全局并行、跨四栏合并同基线行，把别栏的行误算作
  续行。实证：#140 的所谓“第 2 行”是 `— PÁGINA 5 —` 分隔符
  （y=2241.38，x=538.5）及别栏 #28/#102 的行（y=2241.8）；
  #45 的“第 2 行”判定亦受同法污染。
- 按栏归属重数（四栏分别归属、y±3 聚类、排除分隔符/页脚，
  150 键全数归属、0 缺失）：真多行键仅 **3 项——#44 [1554.5, 1570.1]、
  #45 [1599.8, 1615.4]、#139 [2179.9, 2195.6]**。
  #32（y=2392.68 单行）、#82（y=1584.12 单行）、#92（y=1912.96 单行）、
  #140（y=2225.22 单行）均为单行。
- 结论：仅 FIX-LOG 派生数字错误；不影响版面与任何门禁，不列缺陷。

## 结论

- 缺陷 0 项。fix1 的 4 处修复全部通过三源重验；全套机械门绿；
  150 题键无一错误；全文通读与 8 页目视无新缺陷。
- 结论 **(a) 定稿零缺陷**。
- 未修改任何生产文件，未重建生产目录，未 commit，未 push。
  交付：本日志 + PROOF-NOTE.md（均在 `scratch-proof-es-ko3/`）。
