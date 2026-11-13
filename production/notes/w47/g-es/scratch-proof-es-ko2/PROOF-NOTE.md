# PROOF-NOTE — W47 es-ko proof2（重建版独立复校）

- 对象：`production/2026-w47/2026-w47-es-ko/`，西班牙语目标 × 韩语读者，VOL.4，
  刊期 2026 年 11 月 16–22 日，8 页，练习 150 题
  （A2 50 / B1 72 / B2 28）。
- 印刷 PDF `La-Lucerna-VOL4-es-ko.pdf` 8,874,351 B，
  SHA-256 `65e3a3993f2f315f9a89c316788f6f93ed79ef69212c4b32f08f52a9976cb0f7`；
  网页 PDF `La-Lucerna-VOL4-es-ko-web.pdf` 1,237,415 B，
  SHA-256 `54494cef95ba3a7b98dc70aba67bd8a5cd03676106f14b6c928f38f417715351`；
  `2026-w47-es-ko.text.md` 47,369 B（1,818 行），
  SHA-256 `f49dd7088c16f7a40c14618019a05800b45418be8a9a137c8f83ddb8554dbc3e`。
  三 SHA 动工前与收工后两次实测，均与任务书一致。
- 核心 es 未变：core-es 实测 print `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`、
  web `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`、
  text.md `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`，
  与 KIT §8 所载 core build-10 三 SHA 逐一一致。
- 复校员：proof2（独立，从头完整重校）。未修改任何生产文件，未重建，
  未 commit，未 push。run.py / freeze baseline 均在 goals 侧 scratch 的
  build-copy 中跑；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp。
- 详细门日志见同目录 `GATE-LOG.md`。

## 结论：(b) 不定稿，共 4 项缺陷，均为轻微（minor）

修完 D-01～D-04 即可定稿。其余全部通过。

## 缺陷清单

### D-01 —— 轻微（minor），本版讲解层：P8 答案键 #45 韩文注残句（proof1 D-02 未修复）

- 位置：P8 RESPUESTAS，PÁGINA 3 节，第 45 条。
- 内容：`45. En Bilbao toca la banda el domingo. — 장소가 앞에, 동사는 두 번째`
  —— 韩文注缺系词，句子未完成（应为 `두 번째예요`），与平行注 #44、#133
  的完整形式 `시간이 앞에, 동사는 두 번째예요` 不一致。
- 三源核实：源码 `content34.py:101` 原文即 `"장소가 앞에, 동사는 두 번째"`；
  SVG `p8-ejercicios.svg` 节点 593–602（y=1599.78）`장소가 / 앞에 / , / 동사는 / 두 / 번째`
  收尾无 `예요`（节点 592 的 `번째예요` 属 #44 注的第二行）；`text.md` L1653；
  印 PDF 文字层 L2430。目视 P8 该行完整呈现，无溢出。
- KIT §8 称“D-02 已通过 revert 恢复（backup 中已有）”与事实不符：backup
  即旧版 build 2，本身就带有该残句，revert 恢复的正是残句。
- 修复方向：补 `예요`，与 #44、#133 对齐。

### D-02 —— 轻微（minor），本版讲解层：P4 D 节桥接句丢了 `(pretérito indefinido)`

- 位置：P4，`D　EL PRETÉRITO INDEFINIDO` 节桥接句。
- 内容：桥接句现为 `문장을 과거형으로 바꾸세요.`，丢了核心原文
  `把句子改成过去时（pretérito indefinido）。` 括号内的西班牙语时态名。
- 来源：harvest `ko.json:122` 值本身即如此（翻译时丢了括号术语），
  `content34.py:200` 原文即如此。本轮 20 条桥接句逐条比对拉丁词，
  仅此一条丢拉丁词，其余 19 条无一丢词。
- 缓解：时态名仍在该节标题 `D　EL PRETÉRITO INDEFINIDO`（冻结合西班牙语，
  紧贴桥接句上方），做题不致歧义；其余 9 个 es 姊妹版（ja/pt/nl/fr/de/it/
  ru/zh-tw/en）的 P4 桥接句全部保留 `(pretérito indefinido)`。
- 修复方向：恢复括号术语，如 `문장을 과거형(pretérito indefinido)으로
  바꾸세요.`，由构建者重验行宽（该桥接句现为单行，见 P4 目视）。

### D-03 —— 轻微（minor），韩文断行：P1 数字框第 13 条独行右括号 `)`

- 位置：P1，`LA SEMANA EN CIFRAS` 框，第 13 条，SVG y=1414.5，x=556.5。
- 内容：`13 — días faltan el lunes 16 para las elecciones del domingo 29`
  `(선거까지 13일)` 的韩文注换行后，右括号 `)` 独自占一整行。
  SVG 节点：y=1386.8 `elecciones del domingo 29(` + `선거까지` + `13` + `일`；
  y=1414.5 仅 `)`。P1 卡片目视确认。
- 性质：韩文注断行孤儿标点；旧版 build 1 同一坐标已有（proof1 未检出，
  其孤儿扫只覆盖桥接句）。本次重建未引入，但任务书要求重验的韩文断行
  项下必须列出。
- 修复方向：缩短该条韩文注（如去括号注）或重断行，使 `)` 不独行。

### D-04 —— 轻微（minor），韩文断行：P2 日历框第 5 条独行音节 `일)`

- 位置：P2，`EL CALENDARIO` 框，第 5 条（Domingo 22），SVG y=1113.4，
  框内末行。
- 内容：韩文注 `(일요일: 바르사 대 비야레알; 성녀 체칠리아 축일)` 换行三行，
  末行仅剩 `일)`——单词 `축일` 被拆开，`축` 留在上一行末（y=1084.9），
  单个音节 `일` + `)` 独占末行。P2 卡片目视确认。
- 性质：韩文断行孤儿音节（任务书点名重验项）；旧版 build 1 同一坐标
  已有（proof1 框内末基线记录 last='일' 即此行）。
- 修复方向：缩短该条韩文注或重断行，使末行不只剩一个音节。

## hangul 宽度修复重验结果（任务书点名项）

- Exporter 修复已生效：用修复版 `extract_text_es_ko.py`（hangul 区间
  U+AC00–U+D7AF、U+1100–U+11FF 已入 `run_w`）重跑导出，与已发
  `2026-w47-es-ko.text.md` **字节一致**。
- freeze 8/8：baseline build-copy 重跑 8/8 SVG 字节一致。
- freeze 新增 CJK 逐个分类：新增 3,462 个 CJK 字符 = 韩语音节 3,461 +
  全角空格 U+3000 ×1（标题分隔符），未入账 0，无 CJK 表意字、无假名。
- 无溢出：occlusion 0 flags；creambox 严格口径全部为正（最小 +1.9）；
  boxtitle 25 fit / 0 over；P8-keys y=2506（54px 余量）。
- 未通过：断行孤儿检查——D-03（独行 `)`）与 D-04（独行音节 `일)`），
  见缺陷清单。两者均为旧版已有的断行残留，重建未修复。
- 孤儿标点全扫（视觉行口径，按行重建而非按节点）：独行 `。` 0、
  独行右引号 0（P8 Q91 的两个 `”` 节点经坐标核实均在行中，
  紧贴 `것` 之后、`이`/`과` 之前，非独行）、独行 `：` 0、独行 `–` 0。

## 观察（非缺陷）

- **O-1（KIT 记录误差）**：KIT §1 仍引旧版 build 1 的 SHA 与字节数
  （印 8,874,275 B `ba1a…`、网 1,199,171 B `9117…`），与 §8 的重建版
  数字不一致；§1 标题虽写“build 2”，数字未更新。版面本身无误。
- **O-2（KIT 记录误差，proof1 O-3 同款）**：KIT §3 的 P5 注释词计数仍偏高
  ——papeleta 实测 2（KIT 称 3）、plazo 实测 3（KIT 称 4），两次独立计数
  一致；§8.1 门（每页 ≥2 次）对两词仍通过，非内容缺陷。
- **O-3**：P5 框题 `EL PLAN DE LA SEMANA　이번 주 계획` text_w 实测 403.8/404.5，
  余量 +0.7——通过但极紧。目视单行容纳，无溢出。
- **O-4（core 级，已裁定）**：13 日 laSexta 辩论主题——版内（沿 core KIT §5.2 裁定）
  写 13 日场只谈经济、18 日场谈住房；Europa Press 2026-11-06 同文称 13 日场为
  “vivienda y economía”。core 已记录来源冲突并选逐场区分，本版冻结继承，
  不另列缺陷。
- **O-5（D5 字体，生产级待定项，仅记录、不计入判定）**：任务书指定。
  本轮字体实测：Newsreader 1519 / Noto Sans CJK SC 622 /
  Noto Serif CJK SC 621 / UnifrakturMaguntia ×1；纸色 #fbfaf6 8 页全有；
  与 proof1 的 1507/622/622/1 之差来自重建版文本重排造成的节点切分
  变化，无新增异常。
- **O-6（工具说明）**：借来的 import 式 `keycheck.py` 在本 scratch 跑不通
  ——其 `stub_bslib`（de 向）缺少 `illus_voto`；改用 AST 版
  `keycheck_ast.py`（同一比对：源码 REG 键 vs P8 提取键），结果等价，
  149/150 + Q150 预期 `✓`。
- **O-7**：`freeze_direct` 源码层严格匹配 rc=1，经逐项裁定 PASS（见 GATE-LOG）；
  渲染层 8/8 PASS。P6 frozen 由 proof1 的 144 升至 172——核心 build-10
  文本现与版内一致。
- **O-8**：proof1 报告的 `���` 再次核实为 exec 输出转码伪影：源码码位转储
  为干净韩文 `있어요.`；8 个 SVG、text.md、印/网两份 PDF 文字层中
  U+FFFD 均为 0。

## 已通过的核查（摘要，实测为准）

- **机械门（全部实跑，不信 KIT 数字）**：run.py rc=0，0 OVERFLOW / TOO WIDE，
  TOTAL 150（A2 50 / B1 72 / B2 28）；occlusion 审计 0 flags；
  p8 extract 150/150；p8 compare vs core-es CLEAN（keydiff=[137, 138]，
  KIT §6.12 已裁定的翻译键重定向）；freeze baseline 8/8 SVG 字节一致；
  freeze diff 无西班牙文本丢失（仅一处中文桥接句内术语事，见 D-02）；
  freeze_direct 渲染层 8/8 PASS（frozen 151/143/141/144/139/172/115/478，
  均 ≥100），源码层严格匹配 FAIL 经逐项裁定 PASS（5 项移除均有出处、
  128 项新增含 0 个 core 外拉丁词）；
  creambox 严格口径全部 clearance 为正（最小 +1.9；P7 工具盒 +5.7）；
  boxtitle 全标题 25 fit / 0 over；印/网文字层 pdftotext plain 各 48,324 B
  字节一致，layout 版亦字节一致，逐页 8 页字符数一致；
  sweep（bridge orphans 0 / box-vs-hline 0 / widows 0，20 桥）；
  P8 最小字号 PyMuPDF 实测 **10.125pt**（印/网一致，在 §1.1 让步链内）；
  VOL.4 ×9 / VOL.5 ×3（均为下期预告正当引用）；“12 de noviembre” 0 处；
  三色蛾 title 仅 P1；P8 徽章配色与 KIT 一致；
  §1.1 字体/配色见 O-5；日期星期以 `date -d`（Europe/Madrid）逐一核验，
  全部与版内一致（13 周五、16 周一、17 周二、18 周三、19 周四、20 周五、
  21 周六、22 周日、23 周一、24 周二、27 周五、28 周六、29 周日）。
- **150 题答案键**：源码顺序提取 REG（content12 Q1–28、content34 Q29–64、
  content56 Q65–100、content7 Q101–112、content8 Q113–150），共 150；
  与 p8extract 对比仅 Q150 一处差异（开放写作题，P8 印 ✓，属预期）；
  逐题语义手验全部通过（见 GATE-LOG 逐题小结），匹配题键与题干定义
  逐一核实（25–28、52–55、141–144 对照 SVG 选项原文）。
  H 范文词数手数 + run.py 实测均为 **97**（与版内 “97 단어” 一致），
  覆盖 lunes 16、viernes 20、voto del 29。
- **旧版逐页对比**：SVG 文本节点逐页 diff——P3、P4 零变化；P1/P2/P5/P7/P8
  的变化全部对应 KIT §8 已记录的重建项（C2 antes→hasta 含韩文注
  `19일 전에 → 19일까지`；D-01 弯引号→ASCII；PSOE 面对面句改写；
  derbi viernes→sábado；P8 节点 1379→1377 系 `일/전에` 并为 `일까지`）；
  P6 变化 13 节点增量全部对应核心 build-10 改动（RTVE 八方辩论行 INSERT、
  SER 段前移 + 未公布时间从句、Academia 协议句、`de la Academia`、
  JEC `Acuerdo ... del 4 de noviembre`）。文字层 diff 252 行逐行核对，
  除上述记录项与纯重排外无意外变化。
- **外部事实（本轮网上复核新增改动项；未改动的核心事实沿 proof1 结论，
  全文重读无新事实出入）**：RTVE Debate a 8——Europa Press 2026-10-05：
  11 月 23 日周一，八个议会党团发言人（Popular, Socialista, Vox,
  Sumar, Republicano, Junts, EH Bildu, Vasco），版内“propone”措辞与
  提案性质相符；Academia 协议——RTVE Noticias / Demócrata / elFolio
  2026-11-09：PSOE 与 PP 于 11 月 9 日周一达成由 Academia de Televisión
  组织两场辩论，PP 提议 16 日面对面、26 日四方辩论，日期/时间/人选
  “siguen sin cerrarse”，与版内逐字相符；面对面“两党接受邀约但未公布
  时间”——双方已接受 Mediaset 11 月 16 日面对面（多源 2026-11-09/10），
  截稿时无公开时间，版内已注“no da por cerrado lo que aún se negocia”。
- **全文复读**：text.md 1–1818 行通读；无国际政治内容（仅西班牙国内选举）；
  P7 FRASES 8 句逐句与正文核对逐字一致、韩文译准确；P8 C 阅读段
  （Lucía/Diego）与题 129–132 一致；D-01 修复后 P1 词汇注与 P5 C 节副标题
  均为 ASCII 引号，目视 P1/P5 卡片为直引号。
- **8 页目视**：cards/*.png（1950×2700）逐页读过。除 D-03、D-04 两处
  断行孤儿外，无溢出、无重叠、无页脚侵入；P6 图表条长与分钟数成比例；
  P1 插图为编辑部线描并注明非照片；P3/P5/P7 图注均有 PD 来源；
  P5 框题单行容纳（目视与 +0.7 余量一致）。

## 交付文件

- `PROOF-NOTE.md`（本文件）
- `GATE-LOG.md`
- 支撑数据：`occlusion.json`、`p8extract.json`、`p8compare.json`、
  `freeze-diff.json`、`freeze-direct.json`、`keycheck-150.json`、
  `reg.txt`（见 `logs-regdump.txt`）、`logs-*.txt`、`print-plain.txt`、
  `print.txt`、`web-plain.txt`、`web.txt`
  （均在同 scratch 目录）
