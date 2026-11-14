# WEEKLY-KIT — De Lucerna VOL.1 · NL×KO （荷兰语正文 × 韩语讲解）

- **配对**：네덜란드어 텍스트 · 한국어 해설 （目标语 = 荷兰语，讲解 = 韩语 해요체)
- **期次**：W43 · 2026-10-19–25（VOL.1）
- **状态**：**PASS**（独立校对完成：修复 2 处 P1 韩语孤行尾后整轮重跑，终轮零问题；记录见 §7。未入仓、未发 Discord。)
- **出货目录**：`files/weekly-report-nl-ko/`（svg ×8、cards ×8、印刷 PDF、网页 PDF)
- **建造副本**：`hidden_files/weekly-report-nl-ko-build/`（核心 build 的完整拷贝；scratch/ 内含 extract / mapping / transform / 校验脚本——建造过程文件，不入成品口径）

## 1. 建造溯源

- 核心：NL 核心 VOL.1（`files/weekly-report-nl-vol1/`，build `hidden_files/weekly-report-nl-build/`）。
- 开工前 `freeze.py baseline`：核心 8/8 逐字节复现（p1 a8a2cc5d · p2 ea3f2a18 · p3 b61fbb1b · p4 eff31458 · p5 1098c657 · p6 c941eb44 · p7 097fcfa7 · p8 feba8026）；收尾复跑仍 8/8，核心未动。
- 变换：AST 源码跨度替换（保留原格式），共 **497 处**字符串替换 = 汉字讲解串 486 处 + 徽章行 1 + OUT 改道 5 + render 改道 3 + P8 分隔头/尾 2；覆盖断言：核心全部 256 个唯一汉字串（486 处）均被映射、映射键零闲置、变换后讲解层汉字残留 = 0。`bridge()` → `expl()`（定义 1 + 调用 22)。
- OUT 改道首跑前已打印验证：5 个 content 模块 OUT → `files/weekly-report-nl-ko/svg`；render BASE → `files/weekly-report-nl-ko`；PDF 名 `De-Lucerna-VOL1-KO.pdf` / `De-Lucerna-VOL1-KO-web.pdf`。全程未在核心 build 目录内 import/运行任何模块。
- 单进程驱动 `run.py` 一次构建：注册表 **TOTAL 150 = A2 42 · B1 76 · B2 32**；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}，与核心全等。范文词数 87（核心同值，MODELO 荷语冻结）。

## 2. 机械门结果（全部实测）

| 门 | 结果 |
|---|---|
| freeze.py baseline（核心） | 开工 8/8、收尾 8/8 逐字节全等，核心未变 |
| freeze.py diff | 新增汉字（汉字偏旁义）= **0**；新增 CJK 字符 3,258 全为韩字音节（讲解层）；移除侧非讲解项 12 条逐项裁定（见 §2.1) |
| p8.py extract（核心 P8) | 核心印刷注集 = **150/150**（独立导出确认，NL 核心印全 150 注、短横式） |
| p8.py compare | **CLEAN 150 = 150**，missing=[]、extra=0；keydiff 21 条全裁定（见 §4) |
| occlusion_audit.py（自检先行 OK) | 本版 2 旗，均为核心自有冻结荷语旗（P2 `adviesdata…` 底墨 993.8 > 993.1、P3 `Kaartjes…` 1235.7 > 1235.0，亚像素、与核心同旗）；**NEW vs core = 0** |
| 同行墨迹碰撞扫描（README 第 10 条） | 同基线墨迹重叠 > 1.5px：**0** |
| 图表标签元素级检查（README 第 12 条，P6) | 4 个条形值标签 301.000 / 246.000 / 60.500 / 6.600 均为独立文本元素、后绘形状重叠 = 0，全部未被遮 |
| 韩语孤行扫描（硬项） | 折行末行单音节/单字孤行：**0**（初检命中 2 处，已修复，见 §5) |
| 残留语全扫 | 成品 SVG 汉字串 = 0、CJK 标点串 = 0；他列家具残留 = 0；禁用术语（paper / KIT / operative）= 0（scratch/ 除外，已披露） |

### 2.1 freeze diff 移除侧 12 条非讲解项裁定

- P1 徽章行 1 条：荷语家具行被韩语徽章替换（槽位裁定，见 §3)，设计内。
- P8 分隔行 8 条：`— PAGINA N —` → `— 제 N 면 —`（KO 列家具定式），设计内。
- P5 贴士 2 条 + P8 `Eindhoven` 1 条：讲解括号宽度变化引起的折行伪影——新增侧对应行荷语词逐字不变（`1. Kies twee of drie locaties per avond(` 等），源串荷语前缀逐字节冻结。

## 3. 家具逐项（KO 列定式，目标名 네덜란드어；源：EN×KO KIT §3)

| 部件 | 本版落地 |
|---|---|
| P1 徽章 | 核心 y=372 荷语副题行（19pt GREY）即徽章槽（NL×JA 同槽裁定）：替换为 `네덜란드어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`，(975, 372）居中、19.5pt sans **bold BRICK**，P1 肉眼显著 |
| P1 顶栏中段（y=92) | `ELKE WEEK IN HET NEDERLANDS · 매주 발행 · 네덜란드인이 읽는 네덜란드어` |
| P1 主标下题花（y=330, 40pt) | 全韩：`네덜란드어 주간지 · VOL.1 · 시계 · 방학 · 댄스` |
| P1 头条黑带右行 | 行1（24pt bold #b3a06a)`일요일 시계 뒤로`；行2（21pt)`겨울 시간 시작 · 2면 참조` |
| 页脚左（每页） | `De Lucerna · 네덜란드어 주간지 VOL.1 · 텍스트는 네덜란드어 · 해설은 한국어` |
| 页脚右（每页） | `제 {n} 면 / 총 8 면` |
| gloss 前缀 | `해설 — `（核心 `译注｜` 全量替换；P2–P6 各 1 处与核心逐页对齐；P1 另含 expl 行首 `해설 — ` 与徽章内 `해설 — `) |
| P8 答案分隔 | `— 제 {pg} 면 —` ×8 |
| P8 答案头 | `ANTWOORDEN · 정답 — 면별로 정리했어요, 번호로 찾으세요`；右注 `문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안 문제예요`（不含「中文」字样） |
| 栏目头 | 目标语原名 · 韩语短译：`HET NIEUWS · 헤드라인`、`LEVEN · 생활`、`CULTUUR · 문화`、`SPORT · 스포츠`、`JONGEREN · 청소년`、`VERDIEPING · 심층`、`TAAL · 언어`、`TOETS EN ANTWOORDEN · 시험과 정답`；版面级题花同式（如 `NIVEAU A2 · De wintertijd, stap voor stap · 겨울 시간 단계별로`) |
| 盒标题韩语后缀（短式） | `DE WEEK IN CIJFERS · 숫자로 보기`、`ZO ONTHOUD JE HET · 암기법`、`ZO PLAN JE ADE · 축제 팁`、`DE CIJFERS · 숫자 그래프`、`AFSCHAFFEN OF NIET? · 폐지냐 유지냐`、`PAS OP! · 실수 클리닉`、`HET WOORD · 이번 주 단어` 等——全部经遮挡审计 BOXTITLE 零新旗实测 |
| 趋势盒题（P1） | `네덜란드인의 구글 검색 · zoeken op Google`（初版过长越界，已改短，见 §5) |
| 题型标签 | 完成句子→`문장 완성` · 单选→`객관식` · 完形单选→`빈칸 채우기` · 造句→`문장 만들기` · 判断对错→`참/거짓 판단` · 词汇配对→`단어 짝짓기` · 翻译→`번역` · 写作→`쓰기` |
| instr 行 | 填空→`빈칸 채우기` · 判断→`참 / 거짓` · 造句→`문장 만들기` · 翻译→`번역` · 写作→`쓰기` · 把词和释义配对→`단어와 뜻 짝짓기`；其余指示句全韩 해요체 |
| 盒内括号注 | 半角 `(韩语）`（核心全角（）全量转半角） |

## 4. 键差异全表（p8.py compare keydiff 21 条，逐条以渲染答案行核对）

**裁定总览**：键本体 148 条与核心逐字相同；19 条为「注文差异」——p8.py 行级比对含注文，键（` — ` 前段）逐字相同，按 README 第 13 条证伪为提取口径伪影；2 条为许可的翻译题键变更（#137、#138)。

| # | 键（核心 = 本版，逐字相同） | 差异所在 |
|---|---|---|
| 5 | dertig | 注文韩译 |
| 11 | B | 注文韩译 |
| 19 | drie uur | 注文韩译 |
| 20 | achteruit | 注文韩译 |
| 24 | 2.500 | 注文韩译（注内千分位用韩式逗号 2,500) |
| 35 | thema | 注文韩译 |
| 66 | C | 注文韩译 |
| 70 | artiesten | 注文韩译 |
| 71 | locaties | 注文韩译 |
| 73 | kandidaten | 注文韩译 |
| 74 | avontuur | 注文韩译 |
| 78 | gaat winnen | 注文韩译 |
| 82 | Waar | 注文韩译 |
| 83 | 301.000 | 注文韩译 |
| 85 | 203.000 | 注文韩译 |
| 94 | zoekopdracht | 注文韩译 |
| 109 | ruzie | 注文韩译 |
| 127 | B | 注文韩译 |
| 146 | A | 注文韩译 |
| **137** | **键变更（翻译题）**：核心键 = 中文句「周日时钟拨回：多睡一小时！」→ 本版键 = 韩语句 `일요일에 시계가 뒤로 가요: 한 시간 더 자기!`；注文韩译 |
| **138** | **键变更（翻译题）**：核心键 = 中文句「你的手机和电脑会自动更改时间。」→ 本版键 = 韩语句 `휴대폰과 컴퓨터는 스스로 시간을 바꿔요.`；注文韩译 |

其余许可类（未被 keydiff 标记、注册表级核对一致）:

- **#139 / #140 题干改向**：题干（荷语）冻结、作答正文由中文源句改为韩语源句（#139 `네덜란드 디자인 위크는 에인트호번에 있어요. → ___`、#140 `일요일에 저는 한 시간 더 잤어요. → ___`），键（荷语）不变。
- **#150 装置项**：写作题，键 = 韩语注 `（열린 문제, 모범 답안은 아래에）`；答案行 `150. ✓ 모범 답안은 이 면 H 구역에 있어요 (87단어）`，词数 87 与核心同值（MODELO 荷语冻结）。
- 语言中立注逐条核：纯荷语/符号注（如 `perfectum: heb geslapen`、算式注）与核心逐字一致，未译未改。

## 5. 内容核对与自校缺陷

- **gloss 词条逐条点数**（硬规）：5 处 gloss() 调用逐条与核心全等——P2 6 条、P3 5 条、P4 5 条、P5 5 条、P6 5 条，一项不少（AST 解析核心 build 源码点数，只读未执行）。
- **P7**：8 条短语荷语逐字继承核心、页标签 `(Pagina N)` 逐字保留、出现清单与核心全等（AST 字面量对照 True）；8 条韩语 gloss 对应核心中文 gloss 逐条翻译；读者信韩语注保留 VOL.2 承诺（真实来信 + 第 8 版最佳作文）。
- **日历**（Europe/Amsterdam，核心口径）：herfstvakantie（中部/南部 10 月 17–25 日、北部 10–18 日）、DDW 10 月 17–25 日共 9 天、ADE 10 月 21–25 日、wintertijd 10 月 25 日周日 03:00 开始——讲解层日期表述与核心逐项一致，未引入国际政治。
- **自校缺陷与修复**（全量自校一轮，8 页卡片肉眼核：韩文字形无缺字/方框）：
  1. P1 趋势盒题 + 趋势注过长，墨迹越出盒界并出页（遮挡审计 EDGE + BOXTITLE 新旗 ×4）→ 改短为 `네덜란드인의 구글 검색 · zoeken op Google` 与 `10월 20일（화) Google Trends 스냅샷: 추정치예요`，重建后新旗 = 0。
  2. P7 PAS OP 注末行单音节孤行 `요.` → 注文改短（`정각보다 앞이에요` → `정각 앞이에요`），现单行收齐。
  3. P8 #99 注末行单字孤行 `에` → 注文改短（`alleen + 나라 이름이 앞에` → `alleen + 나라 이름이 앞`)。
  4. P8 #137 注 `비교해` 跨行断词 → 注文改为 `1면 헤드라인 참조`，断词消除。
  修复后全门复跑：遮挡 NEW = 0、同行碰撞 = 0、孤行 = 0、p8 CLEAN 不变。

## 6. 实测针脚（校对修复后终值，磁盘实测）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `De-Lucerna-VOL1-KO-web.pdf` | 3,228,964（< 10 MB ✓) | `5166f2be7f670c2505783dace963bacfce084c197166e409519b128ddb170ef3` |
| `De-Lucerna-VOL1-KO.pdf`（印刷） | 11,439,623 | `dd68175755ab77f7c60a016a232b130d9bf844d16a05451ffc513163232f2b1e` |

（建造者交付针脚：网页 3,597,751 B / `d28d28e5…`、印刷 15,330,894 B / `9f4476be…`，校对修复后已被上行终值取代。)

## 7. 独立校对记录（2026-10-22，校对者）

**结论：PASS。** 全部结论独立复跑/复测，未采信建造者自报。工件：`hidden_files/proof-nl-ko/`。

### 缺陷与修复（2 处，均为讲解层韩语折行孤行尾——建造者孤行扫描口径漏洞所致）
建造者扫描正则 `^[가-힣][.!?…]?$` 不含闭括号 `)`，两处以 `)` 收尾的单音节尾行漏检：
1. P1 数字盒条目 9：韩语括号注 `(에인트호번 디자인 위크의 날수)` 折出末行 `수)`（单音节孤行）→ 注文改短为 `(디자인 위크의 날수)`（「에인트호번」与荷语 in Eindhoven 重复），现 2 行收齐、末行以完整词 `날수)` 结尾。
2. P1 数字盒条目 25：`(10월 겨울 시간이 시작하는 날)` 折出末行 `는 날)`，且 `시작하|는` 词中劈尾 → 改短为 `(겨울 시간이 시작하는 날)`（「10월」与荷语 in oktober 重复），现整条括号注落在第 2 行内。
修复纪律：仅改本版 build 副本 `content12.py` 两条字符串（讲解层），单一 driver（run.py）一进程重渲 + render.py；仅 P1 SVG 变化，P2–P8 逐字节不变（sha256 对照）；注册表不变（150 = A2 42 · B1 76 · B2 32，分版分布不变）。修复后整轮重跑全部机械门（见下），终轮零问题。**口径教训（回写）：×KO 孤行扫描的整行正则须含闭括号/引号类尾随字符 `[.!?…)\]»」]*`，否则括号注尾行系统性漏检。**

### 工具门（独立复跑，修复后终轮）
- freeze.py baseline：核心 8/8 逐字节复现（开工/修复后收尾各一次，哈希与 §1 登记全合，核心零触碰）；另以本版 build 跑 baseline 对出货 SVG 8/8 逐字节（确定性自证）。
- freeze.py diff：added CJK 3,243 字全为韩字音节（逐字归类，汉字 = 0）；移除侧纯拉丁串恰 12 条，与 §2.1 裁定逐项吻合（徽章行 1 + P8 分隔 8 + P5 贴士折行伪影 2 + P8 `Eindhoven` 折行伪影 1——该词在本版 #139 注内完好在版）；荷语正文多重集闭合（差异仅家具替换/注文韩译/数字千分位韩式逗号，均在讲解层注内，键面荷式点分不变）。
- occlusion_audit.py（自检先行）：本版 2 旗与核心同旗同坐标（P2 `adviesdata…` 底墨 993.8 > 边 993.1、P3 `Kaartjes…` 1235.7 > 1235.0，各 0.7px）——卡面像素裁定：冻结荷语图注行下伸部轻触盒底边，与核心出货几何逐值相同，属冻结正文继承，非本版缺陷；**NEW vs core = 0**。
- 同行墨迹扫描（README 第 10 条，自备实现复用审计墨迹盒）：同基线碰撞 > 1.5px = **0**（核心亦 0）。

### p8.py（印刷注释门）
extract 核心独立复证 = 150/150（印全注）；compare **CLEAN 150 = 150**，missing=[]、extra=0、keydiff 21 条。P8 式样 = NL 家族短横式，与核心及家族扇出一致。

### 键差异复验（注册表逐字节比对 + 印刷行直查双证）
双注册表自改道副本一进程 dump 比对：**真实键差异恰 {137, 138, 150}**（137/138 翻译题键译韩、忠实度逐句核；150 装置键韩语化）；题干改向 {139, 140} 在 P8 题面直查（中文源句 → 韩语源句、荷语键逐字不变）；注差异 137 条译韩，未变注恰 13 条 = 语言中立注（公式/荷语语法注，含 #6/#59/#97/#140 全角冒号 `：`——与核心逐字节同的冻结注文，非残留）。keydiff 余 19 条逐项证伪（README 第 13 条）：印刷行键段（` — ` 前）与注册表键双证逐字相同，差异全在注文译韩（含千分位 `2,500` 等韩式写法）。#138 印刷行 `veranderen` 后折行空格为折点常态（注册表含空格），非缺陷。**全部 150 键自荷语题面 + 正文逐题手工重推导，零分歧**（算式复算：#46 19,50×2 + 32,50 = 71,50；#84 301.000 + 246.000 = 547.000；#85 750.000 − 547.000 ≈ 203.000；#87 60.500 ÷ 6.600 ≈ 9.17 → 「ruim 9」；范文逐词实数 87 词）。

### KO 列定式核（对 EN×KO KIT §3 逐字，修复后复核）
徽章 (975, 372) 19.5pt **bold** `#a4553a` 居中、文逐字合（目标名 네덜란드어）；顶带三段结构合（首段沿核心冻结荷语 `ELKE WEEK IN HET NEDERLANDS`，§3 公式之目标语形）；衬线行 40pt（随核心槽位）；时钟带两行在版（24pt/21pt，金字右锚）；页脚 ×8 逐字合、页码 `제 N 면 / 총 8 면` ×8；gloss 前缀 `해설 — ` 共 7 处（P1 徽章内 1 + expl 行 1 + P2–P6 gloss 盒各 1）、双前缀 = 0、旧前缀残留 = 0；P8 答案头逐字合、分隔 `— 제 N 면 —` ×8；栏目头双语式全合。

### 几何兜底 / gloss / 日历 / 残留
- 图表标签元素级（README 第 12 条）：P6 四个值标签（301.000 / 246.000 / 60.500 / 6.600）墨迹与后绘不透明图形最大覆盖率 = **0.000**；柱宽 250/204/50/5 与数值比例合（标度期望 250/204.3/50.2/5.5，取整内）。
- 建造者自校 4 项修复逐项落点实证：P1 趋势盒题/注改短后在盒内（卡面目检 + 审计无新旗）；P7 PAS OP 注现单行 `…half는 정각 앞이에요.`；P8 #99 注尾孤字 `에` 已除（整注单行）；P8 #137 注 `비교해` 断词已除（现 `1면 헤드라인 참조`）。
- 韩语孤行复扫（加宽口径，含闭括号）：整行单音节 = **0**；块末短尾候选逐项裁定仅余家具级别行/完整词尾（주세요.·돌려요.)/冻结荷语尾（je?·na.·bij».)，无缺陷（修复前命中 2 处见上）。
- gloss 逐条点数：5 处 gloss() 与核心逐条同数同序同词头 **6/5/5/5/5**（AST 点数；P6 第 4 条词头 `per inwoner` + 韩注 `1인당`）。
- P7：8 条短语页标签分布 {1:1, 2:2, 3:1, 4:1, 5:1, 6:2} 与核心逐条全等，韩译逐条忠实。
- 日历（Europe/Amsterdam 实测）：10-17 Sat、10-20 Tue（快照 (화) 合）、10-21 Wed、10-24 Sat、10-25 Sun（wintertijd 03:00 = 10 月最后一个周日）、11-01 Sun，与纸面全合。
- 残留全扫：汉字 = 0、西里尔 = 0、假名 = 0、CJK 标点 = 0（全角残留仅冻结中立注内冒号 ×4，与核心逐字节同）、他列家具 = 0、禁用术语（paper/KIT/operative）= 0。

svg ×8（p1-voorpagina / p2-leven / p3-cultuur / p4-sport / p5-jongeren / p6-verdieping / p7-taal / p8-toets）、cards ×8 同名 PNG，均在本目录。

## D5 rebuild (13 Nov 2026; this build supersedes all earlier deliverable figures in this KIT)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib 2026-w43-nl-ko/svglib.py --target nl --reader cjk --week 2026-w43` (`--check` dry-run first, RC=0). `_D5_READER = "cjk"`. Routing unit test `test_d5_routing.py`: FAILURES: 0. D1 fix2 retained.
- Pre-rebuild census (`d5_census.py`, D5 elements in the pre-D5 SVGs): 323.
- Baseline (pre-D5 rebuild, venv, disk-measured): run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; print `De-Lucerna-VOL1-KO.pdf` 14,670,583 B (sha256 `1895f1aca0764d366c69076872575a6b4301edc5c7c84298fed36df5e81db513` — pre-D5 build, superseded); web `De-Lucerna-VOL1-KO-web.pdf` 1,292,625 B (sha256 `dbf4dd2b7e40e0343b9b17d8fbb9afcde4f55799b08f56e26d9e000b123fd8af`). Text layer print vs shipped web PDF multiset diff 0 (Python `len()` chars). The KIT-recorded print/web figures predate the §1.1 style port and the D1 re-render and are superseded by the disk-measured baselines above.
- Defects found by the 17 gates (run 1) and fixed by size only — text unchanged throughout:
  - Feature heads `ETEN BESTELLEN WORDT HELDER` (P2) / `EROPUIT IN DE HERFSTVAKANTIE` (P3) HEAD TOO WIDE at 25 pt (advance 472.2/466.0 px vs column 422.5 px) → head size 25 → 22 (`content12.py` P2 head, `content34.py:20`).
  - P6 p.text `AFSCHAFFEN OF NIET?　폐지냐 유지냐` over +6.4 px (right) → size 21 → 20 (`content56.py:166`).
- P8: 213 → 213 lines, slack to footer rule 55.7 → 55.7 px (unchanged by §4; `content8.py` untouched).
- Gates (full re-run after fixes, run 2): **ALL-GREEN** — run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; head_check 0; d5 census 0; render RC=0; webpdf RC=0, web < 7 MB; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8 byte-identical; freeze diff vs baseline added CJK 0; spill 0 SPILL; boxtitle 0 DEFECT; edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web multiset 0, text.md BYTE-IDENTICAL; census_quotes 0 defective. Logs: `hidden_files/d5-redo/scratch-2026-w43-nl/gates/2026-w43-nl-ko/` (`GATES-SUMMARY.txt` master). Full record: `production/notes/2026-w43/g-nl/scratch-d5-rebuild-nl/D5-REPORT-2026-w43-nl-ko.md`.
- New deliverables (rebuilt 13 Nov 2026): print `De-Lucerna-VOL1-KO.pdf` 11,439,623 B, sha256 `dd68175755ab77f7c60a016a232b130d9bf844d16a05451ffc513163232f2b1e`; web `De-Lucerna-VOL1-KO-web.pdf` 3,228,964 B, sha256 `5166f2be7f670c2505783dace963bacfce084c197166e409519b128ddb170ef3` (< 10 MB); text-layer web `2026-w43-nl-ko.web.pdf` 1,167,749 B, sha256 `322eb67fc82eeb00f93d414d7395e2eb73cce627818535fe400f1415ea4a7dd2` (< 7 MB); `2026-w43-nl-ko.text.md` 41,009 B, sha256 `45263f5c16069696c09fd6752106763cc8c10165227209870d9801b2188a5da9`, **BYTE-IDENTICAL** to the shipped `issues/2026-w43/2026-w43-nl-ko/2026-w43-nl-ko.text.md` (exported from the build source with the scratch exporter `hidden_files/d5-redo/scratch-2026-w43-nl/export_text_w43nl.py`, W46 generic AST exporter + W43-nl italic-serif fix + `IN DEZE EDITIE` heading fix).
- Status: builder DONE, all gates green. Independent re-proof (SOP §8) is the coordinator's separate step; no commit, no push by the builder.
