# PROOF-NOTE — W47 es-ko proof3（fix1 后独立复校）

- 对象：`production/2026-w47/2026-w47-es-ko/`，西班牙语目标 × 韩语读者，VOL.4，
  刊期 2026 年 11 月 16–22 日，8 页，练习 150 题
  （A2 50 / B1 72 / B2 28）。
- 印刷 PDF `La-Lucerna-VOL4-es-ko.pdf` 8,873,692 B，
  SHA-256 `2c98a0f8f49e2e4519acdbe56b54702a315b0eb9777223c166775d88f86fcb43`；
  网页 PDF `La-Lucerna-VOL4-es-ko-web.pdf` 1,236,860 B，
  SHA-256 `2c9a90e05f99fe3a4ed024878bb229fac46042644e1bf57fef4d06e11ec0f008`；
  `2026-w47-es-ko.text.md` 47,385 B（1,823 行），
  SHA-256 `a24b79b064896d11b6ba57f5b8f6d0f12047816b78551c76ec93a141787123d6`。
  三 SHA 动工前与收工后两次实测，均与任务书一致；生产文件未动
  （mtime 仍为 13:44–13:47，复校开始于 14:02 UTC）。
- 核心 es 未变：freeze-diff 以 core-es 为基线，新增 CJK 3,458 全部入账
  （韩语音节 3,457 + 全角空格 U+3000 ×1，非韩文/空格 0；见 GATE-LOG）；
  与 proof2 的 multiset 差分恰为 4 处修复的字符
  （P1 까/지 −1，P2 녀 −1，P4 문/장/을 −1，P8 예/요 +1），其余 0。
  另：整个 `production/2026-w47/` 在本克隆中为 untracked（`??`），
  无已提交基线可 diff——核心未变以 freeze + multiset 差分为据。
- 复校员：proof3（独立，与 fix1 agent ac34df55 不同人；从头完整重校，
  含 text.md 1,823 行全文通读与 150 题三源逐题手验）。
  未修改任何生产文件，未重建生产目录，未 commit，未 push。
  run.py / render.py 均在 goals 侧 scratch 的 build-copy 中跑；
  网 PDF 只在 scratch 里重渲，绝未覆盖生产目录的网 PDF。
  全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
  解释器一律 `tools/venv/bin/python`。
- 详细门日志见同目录 `GATE-LOG.md`。
- 工作区说明：任务书指定的 `scratch-proof-es-ko2/` 已被 proof2 的
  交付件占用（PROOF-NOTE.md / GATE-LOG.md，mtime 2026-11-11 13:30，
  本轮未覆盖、未改动）；为保全证据链，本轮全部工作落在
  `scratch-proof-es-ko3/`（探针文件亦随之迁移；proof2 的 probe.txt
  在迁移前被同名覆盖一次，内容仅为一行探针记录，GATE-LOG 已记其 hash）。

## 结论：(a) 定稿零缺陷

fix1 声称的 4 处修复逐项独立重验，全部属实（源行 + 渲染 + 文字层三源）；
全套机械门绿；150 题键无一错误；8 页目视无溢出、无重叠、无新缺陷。
FIX-LOG 中仅一处记录数字有误（多行键计数，见观察 O-1），属记录误差，
不影响版面、不影响任何门禁，不列缺陷。

## 4 处修复逐项重验结果

### D-01 —— 通过：P8 #45 韩文注已补 `예요`

- 源行：`content34.py:101` 实测
  `"장소가 앞에, 동사는 두 번째예요"`，与 #44（`:99`，`시간이 앞에, 동사는
  두 번째예요`）形式一致；BEFORE 行（fix scratch
  `source-lines-BEFORE.txt`）为缺 `예요` 的旧句，确认只改此一处。
- 渲染：P8 SVG 节点 y=1599.78
  `45. En Bilbao toca la banda el domingo. — 장소가 앞에, 동사는 두 번째`，
  次行 y=1615.44 独留 `예요`（x=538.5，栏首）——两行真实；
  #44 次行 y=1570.12 为 `두 번째예요`，#133（y=2001.94）为单行完整式
  `시간이 앞에, 동사는 두 번째예요`。三者注文内容形式一致，
  断行点随词长而异（#45 茎干较长，`예요` 独落次行），属同一可接受类。
- 无溢出：run.py `flow[P8-keys] ended col 3/3 y=2538 (bottom 2560)`，
  余 22px；occlusion 0 flags；P8 卡片目视键区收在页脚之上。
- 文字层：text.md L1651–1652（`…두 번째` / `예요`）与印/网 PDF 文字层
  一致（pdftotext plain 字节一致）；exporter 重跑与已发 text.md
  字节一致。
- 多行键计数更正见 O-1：按栏归属的正确重数为真多行 3 项
  （#44、#45、#139），非 FIX-LOG 所称 7 项。

### D-02 —— 通过：P4 D 节桥接句已恢复 `(pretérito indefinido)`

- 源行：`content34.py:200` 实测
  `e.bridge("과거형(pretérito indefinido)으로 바꾸세요.")`；
  BEFORE 为 `문장을 과거형으로 바꾸세요.`，确认只改此一处。
- 渲染：P4 SVG 单节点 y=1943.5（x=989.0，sans 20.5）
  `과거형(pretérito indefinido)으로 바꾸세요.`，单行；
  真实 `wrap()` 复测同为 1 行（FIX-LOG 称 381.2/422.5，本轮复测
  1 行，见 GATE-LOG）；被拒方案
  `문장을 과거형(pretérito indefinido)으로 바꾸세요.` 复测确为 2 行、
  尾行独留 `요.`，故去宾语 `문장을` 是必要的。
- 其余 19 桥接句未受影响：全版桥接句 sweep 20 条、orphans 0 /
  widows 0；排序 diff 证明 text.md 仅此一处桥接句变化；
  freeze-direct 新增项中拉丁词经核查 0 个 core 外词
  （`pretérito/indefinido` 均在 core 内）。
- 文字层：SVG 全文 `pretérito` 出现 1 次，即此句；
  `core has 'pretérito indefinido': True | edition: True`。

### D-03 —— 通过：P1 数字框第 13 条独行 `)` 已消除

- 源行：`content12.py:47` 实测
  `13 — días faltan el lunes 16 para las elecciones del domingo 29(선거 13일)`；
  BEFORE 为 `(선거까지 13일)`，确认只改此一处。
- 渲染：P1 SVG y=1386.84 同行
  `elecciones del domingo 29(` + `선거` + `13` + `일` + `)`；
  y=1414.5 处无任何节点（该基线区间下一节点为 x=88 的
  `partidos aceptan la cita…` y=1425.38，另一栏）。
  真实 `wrap()`（serif 20.5，内宽 386.5）复测：
  改后 2 行 `['13 — días faltan el lunes 16 para las',
  'elecciones del domingo 29(선거 13일)']`；
  改前 3 行、尾行独留 `)`，与 FIX-LOG 一致。
- 目视：P1 卡片该条为两行，`)` 收在行末，无孤儿、无溢出。

### D-04 —— 通过：P2 日历框 Domingo 22 独行音节 `일)` 已消除

- 源行：`content12.py:185` 实测
  `…; 성 체칠리아 축일)`（`성녀` → `성`）；
  BEFORE 为 `…; 성녀 체칠리아 축일)`，确认只改此一处。
- 渲染：P2 SVG y=1084.88 同行
  `일` `: ` `바르사` `대` `비야레알` `; ` `성` `체칠리아` `축일` `)`，
  `축일)` 完整落在同一基线；y=1113.44 处无任何节点
  （该区间仅 y=1080.34 与 y=1116.82 的另一栏节点）。
  真实 `wrap()`（serif 21，内宽 386.5）复测：改后 3 行、
  末行 `일: 바르사 대 비야레알; 성 체칠리아 축일)`；
  改前 4 行、末行独留 `일)`，与 FIX-LOG 一致。
- 未动项核实：P5 计划框第 5 条（`content56.py:27`）仍为
  `성녀 체칠리아 축일`，真实 `wrap()` 复测 3 行、末行
  `야레알; 성녀 체칠리아 축일)` 完整；P5 SVG y=747.28
  `축일` + `)` 同行，P5 卡片目视完整。
- 目视：P2 卡片 Domingo 22 条末行 `…성 체칠리아 축일)` 完整，无孤儿。

## 已通过的核查（摘要，实测为准）

- **机械门（全部实跑，不信 KIT/FIX-LOG 数字）**：run.py rc=0，
  0 OVERFLOW / TOO WIDE，TOTAL 150（A2 50 / B1 72 / B2 28；
  按页 10/18/18/18/18/18/12/38）；P8-keys y=2538，MODELO 97 词；
  build-copy 重建 8/8 SVG 与交付件字节一致；
  render.py rc=0，重建印 PDF 8,873,692 B、SHA 与交付件完全一致
  （`2c98a0f8…`，第三次独立复现）；重建网 PDF 1,236,857 B，
  与交付件 1,236,860 B 字节不同（预期：网 PDF 字节不可复现），
  文字层与交付印 PDF 字节一致。
  occlusion 审计 0 flags（内置自检 6 类阳性全触发）；
  p8 extract 150/150；p8 compare vs core-es CLEAN
  （keydiff=[137, 138]，KIT §6.12 已裁定的翻译键重定向）；
  freeze baseline 8/8；freeze diff 新增 CJK 3,458 = 韩语音节 3,457 +
  全角空格 U+3000 ×1，未入账 0；
  freeze_direct 渲染层 8/8 PASS（frozen
  151/143/141/144/139/172/115/478，均 ≥100），源码层严格匹配 FAIL
  经逐项裁定 PASS（移除 5 项与 proof1/proof2 完全相同、均有出处；
  新增 130 项（proof2 为 128，+2 恰为 D-02 桥接句与 D-01 注文
  的新字符串，另 D-03/D-04 为旧串换新串），所含拉丁词
  （大小写不敏感、核对 core 文本+字面量）0 个 core 外词；
  其余两项 `middle`/`sans` 为工具自 SVG 属性收获的旧有项，
  proof2 名单中亦有，非新增西班牙语）；
  creambox 严格口径 27 框全部 clearance 为正（最小 +1.9；
  P1 两处 -999 为无文图框，P7 工具盒 +5.7，与 proof2 完全相同）；
  creambox.py 6 条 raw 负值与 proof2 完全相同（下一框标题/框外图注
  落入窗口的伪影）；boxtitle 全标题 25 fit / 0 over，
  最紧 P5 `EL PLAN DE LA SEMANA　이번 주 계획` 403.8/404.5（余 +0.7）；
  印/网文字层 pdftotext plain 各 48,365 B 字节一致，
  layout 版各 107,964 B 字节一致，逐页 8 页字符数逐页一致
  （4356/4652/3745/4044/4079/4968/4467/9612）；
  sweep（bridge orphans 0 / box-vs-hline 0 / widows 0，20 桥）；
  孤儿扫（视觉行口径 orphan_scan2）0；节点级 orphan_scan 16 条
  均为同行节点伪影（`축일)` 的 `)` 节点等），旧 D-03/D-04 坐标
  （y=1414.5 / y=1113.44）已无任何命中；
  P8 最小字号 PyMuPDF 实测 **10.125pt**（印/网一致，0 低于 9.75pt 下限）；
  VOL.4 ×9 / VOL.5 ×3（均为下期预告正当引用）；
  “12 de noviembre” 0 处；纸色 #fbfaf6 8 页全有；
  U+FFFD 在 8 个 SVG 与 text.md 中均为 0。
- **150 题答案键**：AST 提取源码 REG 150 条，与 p8extract 对比
  exact match **149/150**，唯一差异为 Q150（开放写作题，
  REG 键 `(열린 문제 — 모범 답안은 아래에 있어요)`，P8 印 `✓`，属预期）；
  text.md 全文通读 + keycheck 三源逐题手验全部通过
  （见 GATE-LOG 逐题小结；匹配题 25–28/52–55/141–144 键与题干定义
  逐一核实；Q87 45−30=15、Q91 «propuesto»≠cerrado、图表加总 195 分钟
  均与正文一致；H 范文 run.py 实测 97 词，与版内 “97 단어” 一致）。
- **仅 4 处变化的独立证明**：交付 text.md vs fix1-BEFORE 排序 diff
  仅 4 个修复区（加 exporter 带分隔空行）；SVG 变化仅 P1/P2/P4/P8，
  P3/P5/P6/P7 与 BEFORE 字节一致；freeze-diff multiset 差分
  （proof2 → 本轮）恰为 4 处修复的字符；
  KIT §1/§3 已更新为 build-3 SHA 与修正计数
  （papeleta 2、plazo 3、censo 2，本轮 SVG 子串计数复核一致）。
- **8 页目视**：build-copy cards/*.png（1950×2700 渲染）逐页读过。
  除 D-01～D-04 四处修复点外无溢出、无重叠、无页脚侵入；
  P6 图表条长与分钟数成比例（45/45 等长、30/30 等长、15 短；
  5/15/1 成比例）；P1 插图为编辑部线描并注明非照片；
  P3/P5/P7 图注均有 PD 来源；P5 框题单行容纳（目视与 +0.7 余量一致）；
  P4 D 节标题 `EL PRETÉRITO INDEFINIDO` 在桥接句正上方；
  P5 计划框第 5 条 `성녀 체칠리아 축일)` 目视完整。

## 观察（非缺陷）

- **O-1（FIX-LOG 记录误差，需更正）**：FIX-LOG 称“P8 multi-line items
  6 → 7（#45 joins #32, #44, #82, #92, #139, #140）”。
  用 fix1 自带的 `check_p8keys.py` 在交付件上重跑得 **5 项**，
  在 proof2 build-copy 上重跑得 **6 项**，且两次名单互不相同
  （该脚本按 y±2 全局并行、跨四栏合并同基线行，把别栏的行误算作
  续行——如 #140 的所谓“第 2 行”实为 `— PÁGINA 5 —` 分隔符
  y=2241.38 及别栏 #28/#102 的行）。
  按栏归属的正确重数：真多行键仅 **3 项（#44、#45、#139）**，
  本轮逐栏逐键核实（150 键全数归属，0 缺失）。
  结论：仅为 FIX-LOG 的派生数字错误；不影响版面（#45 两行真实、
  P8-keys 余 22px、无溢出），不影响任何门禁，不列缺陷；
  建议后续周期改用按栏归属法计数或删除该数字。
- **O-2（目视所见，旧有、未动、非缺陷）**：P2 日历框 Lunes 16 条
  末行独留 `제안)`（2 音节 + 右括号）。孤儿门定义为独行 `)` 或
  独行单音节，本项不在门内；与 P8 键已接受的短尾行同类；
  proof2 版已存在，本轮未引入、未改动。不列缺陷。
- **O-3（D-01 断行点说明）**：#45 次行独留 `예요`，#44 次行为
  `두 번째예요`，#133 为单行完整式——三者注文内容形式一致，
  断行点随茎干长度而异，属换行固有现象，非不一致。
- **O-4（D5 字体，生产级待定项，仅记录、不计入判定）**：任务书指定。
  本轮字体实测：印 PDF 含 Newsreader / Noto Sans CJK SC /
  Noto Serif CJK SC / UnifrakturMaguntia ×1；纸色 #fbfaf6 8 页全有；
  P8 最小字号 10.125pt。无新增异常。
- **O-5（网 PDF 字节）**：网 PDF 字节不可复现（本轮 scratch 重渲
  1,236,857 B vs 交付件 1,236,860 B，SHA 不同），与 fix1 记录一致；
  文字层字节一致，交付件网 PDF SHA 以磁盘实测为准。
- **O-6（工具说明）**：`cjk_audit2.py` 硬编码 proof2 的 JSON 路径，
  本轮复制后改指本轮 JSON 才得出正确值（3,458）；
  未改路径时误读旧值 3,462，已在 GATE-LOG 注明。
  import 式 `keycheck.py` 仍跑不通（stub_bslib 缺 `illus_voto`），
  本轮沿用 proof2 的 AST 版 `keycheck_ast.py`，结果等价。
