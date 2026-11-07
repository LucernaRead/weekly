# W45 EN×KO 第二轮独立校对报告 — The Lucerna VOL.2（英语正文 × 韩语讲解）

- **校对对象**：`files/weekly-report-w45-en-ko/`（SVG ×8、卡片 PNG ×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **核心对照**：`files/weekly-report-w45-en-core/`（EN VOL.2，150 题；全部核心固定数均由本轮实测复核，未抄其他族）
- **W43 同配对对照**：`files/weekly-report-en-ko/`（VOL.1，只读对照）
- **构建树**：`hidden_files/weekly-report-w45-en-ko-build/`（只读使用；未改动。登记展开与重渲染一律在本科对证据 scratch 内完成，见 §12）
- **校对时间**：2026-10-27 21:57 EDT 起（UTC 2026-10-28 01:57 起）
- **校对员立场**：只校对、不改源码、不宣布上架。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch 目录。

## 结论：ZERO PROBLEMS

**本版通过全部重测门禁，无阻塞项。** 上一轮 4 项阻塞（P8 韩语词中切分，尾 ≥3 音节）已全部修复并经卡面确认；其余门禁本轮全部从头独立重测（上一轮通过项未假定沿用），无新增缺陷。下述“非阻塞观察”（§11）均为 KIT 文字或既往已裁定事项，纸面正确，不构成阻塞。本报告不宣布上架，上架由主线决定。

**开工查重**：开工时唯一在途进程为 ja-en 版 insert（cwd 为 `tools/` / `weekly-git`），与 en-ko 树无关，不构成 stand down；en-ko 交付物最新 mtime 为 UTC 01:50:54（KIT），构建树最新为 01:51:05，开工时静默已超 6 分钟，判定安全开工。

---

## 1. 修复专项：上一轮 4 项阻塞全部关闭（SVG 坐标 + 卡面双重确认）

修复后声称值全部独立重测属实：印刷 PDF 21,530,271 字节 sha256 `305b69f2413cb500f80f03d6229d7115e68e40d9286775eea5ea7c6cd4691949`；网页 PDF 3,898,191 字节 sha256 `380f734d1f2094eb9426827ce3b08153929f7598a7fe710f2bcd88b22642df0f`；新 P8 SVG `7cee4087c86c46b3b627c7f6cf0bc16cf5baa3c33380ae1d93143f377ea48e3c`。P8 卡片 `4868c268…`。

| # | 位置（SVG 实测） | 修复前 → 修复后（登记注，键/题面未动） | 现状（SVG 行 + 卡面裁剪目视） |
|---|---|---|---|
| #67 | P8，x=527，y=2042.51 | `두 번째 화면은 휴대전화예요` → `두 번째 화면 = 폰`；键 B 不变 | 该行现为 `67. B (두 번째 화면 = 폰)` **同行闭合**，次行 y=2062.66 起为 `68. A …`，无切分、无孤括号。卡面确认。 |
| #93 | P8，x=527，y=2390.87→2411.02 | `인내는 제도의 일부예요` → `인내는 제도의 일부`；键 C 不变 | 断为 `일\|부`，尾 1 音节（`부`）。卡面确认。 |
| #102 | P8，x=527，y=2517.58→2537.73 | `would + 동사원형` → `would + 원형`；键 `would` 不变 | 断为 `원\|형`，尾 1 音节（`형`）。卡面确认。 |
| #149 | P8，x=1451，y=1895.65→1915.8 | `선거일은 11월 3일 화요일이에요` → `선거일 = 11월 3일 화요일`；键 `Tuesday` 不变 | 断为 `선\|거일`，尾 2 音节（`거일`）。卡面确认。 |

- **易混字符串未动**：#137 键 `인내는 제도의 일부예요, 실패가 아니에요.` 与 P7 语法点 `would + 동사원형, 선택 의지예요.` 均与修复前一致（P7 该行在 P7 卡面亦可见），与 #102 注 `would + 원형` 是不同字符串，确未误改。
- **CJK 算术独立重算**：文本节点 Hangul 合计 **2438**（P1 208 / P2 237 / P3 153 / P4 176 / P5 169 / P6 185 / P7 452 / P8 858），汉字 **0**。相对上一轮 2452 的 −14 恰为 #67 −6（12→6）、#93 −2（10→8）、#102 −2（4→2）、#149 −4（12→8），与 freeze diff 的 P8 872→858 一致。freeze diff 全页 added CJK 亦为 2438（P3–P7 各比 Hangul 计数多 1，系 freeze CJK 正则把 `｜` 计入，见 §2）。
- **改动范围逐项验证（pre-fix 基线 `fix-round1-prefixed.sha256` 对照现交付）**：该基线文件实含 **20 条**（8 SVG + 8 卡片 + 2 PDF + KIT + ABSTRACT；“18 件”之说与 `fix1b-postfix.sha256` 的 18 条口径一致，后者不含 KIT/ABSTRACT，见 §11 观察）。变化者恰为 **5 件**：P8 SVG、P8 卡片、印刷 PDF、网页 PDF、KIT；**不变者 15 件**：P1–P7 SVG、P1–P7 卡片、ABSTRACT（逐字节相同）。无任何超范围变化。
- **登记 delta（scratch 重 dump，见 §10）**：相对上一轮登记，变化者恰为上述 4 条注，页/级别/类型/键全部相同。

## 2. 冻结与英语正文

- **freeze.py baseline（独立重跑）**：用原始核心构建目录 `hidden_files/weekly-report-w45-en-build`，freeze.py 自身 repoint 到本科对 scratch，**8/8 逐字节复现**：p1 `c7e7d019de01e662`、p2 `07f5df7e8e7ea076`、p3 `d9f7cc374fe1229c`、p4 `3b8be5175094bcb7`、p5 `73486e2f216e1f3b`、p6 `3e2187b37acb2883`、p7 `5a2684096010839c`、p8 `4de34a135cc831bf`。核心重哈希不变。
- **核心固定数（本轮实测）**：VOL.2，刊头 `The Lucerna`，150 题，A2 60 / B1 69 / B2 21，页分布 10/17/18/18/18/18/12/39，范文《My Tuesday, November 3》85 词（见 §10）。
- **英语正文零删失（拉丁词多重集法）**：核心拉丁词多重集 − 分版拉丁词多重集，缺失者仅为：
  - P1：标语 `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`（9 词）+ 页脚 `LUCERNA ENGLISH WEEKLY`（3 词），合计 12 词；
  - P2–P8：每页仅页脚 `LUCERNA ENGLISH WEEKLY`（3 词）。
  - 分版相对核心的拉丁词“新增” distinct 为 0。正文英文一词未少；其余 freeze diff 的纯英文“被删串”均为行重排碎片（同页同词重组），或上述两处有意家具替换（P1 标语槽原位换为 W43 同式徽章；各页页脚换为新页脚，W43 同式佐证为家具而非正文丢失）。
- **新增 CJK 与标点（SVG 文本节点实测）**：Hangul 如 §1；汉字 0；全角 `。` 0；全角括号 `（`/`）` 0；`｜` 5 处（P3–P7 各 1，均为核心同位栏目标签分隔符沿用，如核心 `五句影评｜` → 本版 `다섯 문장 평｜`、核心 `编辑说明｜` → 本版 `편집부 알림｜`），不是新增全角标点缺陷。核心全书 `｜` 远多于本版，本版 `｜` 为其子集。
- **违禁词“桥接”**：SVG + KIT + ABSTRACT 全文均为 0（中日文 `桥接`/`橋接`均计）。
- **KIT 措辞不精确（非阻塞，见 §11）**：KIT 称“full-width punct 0”，精确口径应为“`。` 0、（）0、`｜` 5 处为核心沿用分隔符”；KIT §5 仍含上一轮旧数（见 §11）。

## 3. 韩语专项（独立扫描，非采信修补后的 ko_scan.py）

窗口 **10–45**（P8 答案行间距 20.1–20.2，15 起会结构性漏掉 P8 行，故必须从 10 起）。本科对员自写扫描器（证据 `ko_scan_independent.py`，逻辑：同 x 列连续行，上一行末词元尾部 Hangul 串 + 下一行首词元首部 Hangul 串——首串用首个 Hangul 段正则提取，剥离括号/标点，`(` 起首续行不排除——两串均非空且拼接串在构建源语料中连续出现，方为候选；尾 = 续行首串音节数，≥3 阻塞）。废弃的“去空白全语料扫描”未使用、未引用。

- **本科对独立扫描结果**：同 x 列候选 **16 处，尾 ≥3 者 0**；跨 x 列候选 **0**；行首孤标点（韩语行）**0**；S2 **4 处**（与上一轮相同，见下）。
- **修补后构建员 ko_scan.py 对照重跑**：S1 0 / S2 4 / S3 0 / S4 0，与独立扫描结论一致，但本结论不依赖于它。
- **16 处候选全表（全部尾 1–2，按先例非阻塞）**：

| 页 | 断点 | 尾 | 页 | 断点 | 尾 |
|---|---|---|---|---|---|
| P3 | `명대\|사` | 1 | P8 | `의\|문문` | 2 |
| P6 | `영\|향을` | 2 | P8 | `헤이더\|가` | 1 |
| P6 | `선\|거의` | 2 | P8 | `돌핀\|스` | 1 |
| P7 | `대조\|를` | 1 | P8 | `경\|기는` | 2 |
| P7 | `바뀌\|는` | 1 | P8 | `일\|부`（#93 修复后） | 1 |
| P7 | `하\|나` | 1 | P8 | `원\|형`（#102 修复后） | 1 |
| P8 | `오하이오\|는` | 1 | P8 | `선\|거일`（#149 修复后） | 2 |
| P8 | `경기\|를` | 1 | P8 | `모\|범`（重排新生，尾 1） | 1 |

- **与上一轮 18 处候选的映射（逐项核实）**：上一轮 4 项阻塞中 #67 已消失（同行闭合），#93/#102/#149 降级为尾 1/1/2；上一轮 14 处尾 1–2 中 12 处原样保留；`지\|도` 消失（#74 注现整行 `74. c (map=선거 지도 c)`，y=2102.96 单行完整，卡面亦可见）；`칸\|에` 消失（#149 缩短引起 #150 换行点移动）；新生 `모\|범`（#150 行 `…쓰기 칸에, 모` / `범 답안은…`，尾 1）仍低于 ≥3 门槛。无一处升级为阻塞。
- **S2 4 项逐个复核，皆为非缺陷（与上一轮同类）**：
  1. P2，x=1330，y=1660：`= two times(두 번)` — 报时词汇表行，完整词条。
  2. P8，x=1451，y=369.45：`번역: On Sunday, the NFL plays in Madrid.` — 完整翻译题干。
  3. P8，x=65，y=2043.97：`13. quarter to · 14. twice (두 번 = twice) · 15. extra · 16.` — 流式答案行行尾题号。
  4. P8，x=65，y=2539.19：`55. faster · 56. b · 57. d · 58. a (fan=팬 a) · 59. c · 60.` — 同上。
- **行首孤标点**：全部韩语行首标点为 0；行首标点行若有，Hangul 数均为 0，皆为英语正文换行。
- **共享 tools/ 扫描器缺口核查**：`tools/` 内无任何韩语扫描器（仅 freeze.py / insert.py / occlusion_audit.py / p8.py / tables.py），故共享 tools 不存在同款缺口；缺口仅存在于构建树内 `ko_scan.py`（已修补），本科对结论由独立扫描器得出，不依赖该修补。

## 4. P8（显式双路径 + --total 150）

- **主路径**：`p8.py compare --core-p8 <核心> --edition-p8 <分版> --total 150`，结果 **CLEAN，核心 78 = 分版 78 noted，missing=[]，extra=0，uncertain=[]，keydiff=[137, 138, 139, 140, 150]**。78 项口径：核心印 78 条带注，不是 150（150 为总题数）；印刷注集合按题号相等，无 EXTRA_ONLY。
- **错口径负对照**：`--total 149` 在本工具版本下产出 77 noted、keydiff=[137,138,139,140,149]（第 150 项被截断/并入 149），证明 149 口径不可用；门禁结论以 --total 150 为准。任务所述“73/145”数值在本调用中未复现（可能为另一调用路径），不影响门禁结论，特此如实记录。
- **dir 形式第二路径**：`--core-dir/--edition-dir --target ko` 失败，工具把 ko 映射为 `p8-siheom.svg` 而 EN 族 P8 文件为 `p8-exercices.svg`（FileNotFoundError，证据 `p8-compare-dir.txt`）。此为工具映射问题，不是分版缺陷；直接 SVG 路径 + --total 150 有效且 CLEAN。
- **keydiff 逐项印刷行对照，全部合法**：
  - **137**：题干英语 `Translate : « Patience is part of the system, not a failure of it. »` 冻结（英语指令保留）；键 `인내는 제도의 일부예요, 실패가 아니에요.`；注 `part of = 일부분; not a failure = 실패가 아님`。方向 EN→KO。
  - **138**：题干韩语标签 + 英语原句 `번역: Tuesday, November 3, is Election Day in the United States.`（两行）；键 `11월 3일 화요일은 미국의 선거일이에요.`；注 `Election Day = 선거일; on Tuesday = 화요일에`。
  - **139**：题干 `번역: On Sunday, the NFL plays in Madrid.`；键 `일요일에 NFL이 마드리드에서 경기를 해요.`；注 `on Sunday = 일요일에; in Madrid = 마드리드에서`。
  - **140**：题干英语 `Translate : « Not every place changes. »` 冻结（英语指令保留）；键 `모든 곳이 시계를 되돌리는 건 아니에요.`（按印刷英文直译；核心键窄化为拨钟语境的情况与上一轮一致）；注 `not every = 모든 ~가 아니다; change = 바뀌다`。方向 EN→KO。
  - **150**：写作装置行，键 `열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에`，注 `기준 항목대로 채점해요`，非答案内容变更。
- **印刷注语言**：78 个印刷注段中汉字 **0** 处；75 段含 Hangul，3 段保留纯英文语法注（107 `has (have → has)`、118 `B (be going to → is going)`、120 `B (1:30 = half past one)`），皆为核心不变注（见 §10 不变注表），非中文残留。
- **印刷段口径**：印刷段变更 78 项（恰为印刷注集合）与注册注口径（变更 129 / 不变 21）不得混用，见 §10。

## 5. 几何

- **canonical `tools/occlusion_audit.py`（自检先行）**：6 类（BOXTITLE、COVER、EDGE、FOOTER、LINEX、TEXTX）全部触发、干净对照静默；**分版 0 flags、核心 0 flags、NEW vs core 0**。
- **P1 masthead TEXTX**：本轮分版与核心均为 0 flags，**无 TEXTX 旗标需要像素裁决**。为完整起见仍实测刊头真墨迹（PIL `ls` 锚定）：`The Lucerna` 墨迹 y 128.2–264.2，副标题墨迹 y 290.2–335.8（间隙 26.0），徽章墨迹 y 355.2–374.0（与副标题间隙 19.4，与暗带顶 y=424 间隙 50.0），均清晰分离。W43 同配对在现行工具下重跑另有 2 处 LINEX（P1/P6，W43 自身已上架状态），与本版无关，本版无此旗标。
- **P1 暗带间隙实测**：暗带矩形 x=65 y=424 w=1820 h=118（分版=核心=W43）。带内左右文本同基线间隙：y=478 行 advance 间隙 **247.0** / 墨迹间隙 **247.1**（左 `AMERICA VOTES…` 墨迹右缘 1243.8，右 `화요일 선거일 · 일요일 시계 되돌림` 墨迹左缘 1490.9）；y=522 行 advance **258.8** / 墨迹 **258.9**。带底 y=542 至下一墨迹顶间隙 45.5。**无一处为 0.1px**；任务所述“约 105px”在本版暗带任一实测对中均未出现（全页同基线 90–120 间隙扫描亦无暗带对），不得将 105px 抄作本版数值——105 若属他版/他版本的历史值，不转移至本版；本版实测间隙宽裕、无碰撞，结论不受影响。
- **同基线墨迹碰撞扫描**（构建树 `rowcheck.py` 逻辑拷至本科对 scratch 后只读运行）：**分版 0、核心 0**。
- **全页右缘 ADVANCE 扫描**（同上 scratch 只读运行）：分版仅 2 行，与核心逐值同构继承，均超 1885 未超 1950 页边，非本版新缺陷：
  - P8，x=1485，y=806.4：`b. an election in the middle of a term`，右缘 1899.4；
  - P8，x=1485，y=882.4：`d. the paper you mark your choice on`，右缘 1903.8。
  - 两行皆为 P8 F 词汇配对选项行（match_set 前缀致超），PIL 整数 bbox 在右对齐栏缘线上 ≤0.5px 的超量另属舍入伪影，不计缺陷。
- **P6 图表标签（基线锚定墨迹法，PIL `getmetrics` + `anchor="ls"`，不用 getbbox 升部相对框法）**：4 标签墨迹盒与核心逐值相同 — `No lines : 38%` (527.0, 1170.2, 683.0, 1189.4)、`Work on Tuesday : 29%` (527.0, 1222.8, 785.2, 1247.0)、`Travel plans : 21%` (527.0, 1275.4, 729.0, 1299.4)、`Habit : 12%` (527.0, 1328.0, 655.0, 1347.2)；被后续不透明矩形覆盖 **0.00%**（门 <30%）。P6 矩形 26 个，分版=核心；EN 版 P6 图表实为纯文本行，无绘制条形，覆盖为 0 是结构性的。
- **卡片目视（8/8 全部目视 + P8 4 处修复区裁剪放大目视）**：P1 徽章/顶带/暗带/页脚、P2 时钟与词汇表、P3 gloss 与 Manet 图、P4 体育与 1910 足球图、P5 青年、P6 图表文本行与选票框（☐ 字形显示为小框符号，与核心相同）、P7 读者园地盒与 VOL.3 深色预告盒分离、P8 练习与答案流均正常，无重叠、无缺文、无截断。唯一卡面可见的词中切分即 §3 所列尾 1–2 候选，均低于 ≥3 门槛。

## 6. gloss

- **源级 `gloss()` 调用（核心构建与分版构建对照）**：各 5 次，`·` 分段数 3/4/4/3/4，**合计 18 = P2 3 / P3 4 / P4 4 / P5 3 / P6 4**，核心=分版逐项 1:1。英文头全部保留（`to fall back`、`a costume`、`trick or treat`、`to open`、`a monster`、`a catchphrase`、`a series`、`a fixture`、`a title`、`to defend`、`a fan`、`a map`、`too close to call`、`a second screen`、`to register`、`a governor`、`to shape laws`、`patience`），仅讲解层译为韩语。
- **双前缀清理**：核心自身 5 处 `译注｜讲解｜` 双前缀（P2–P6 各 1）；本版 `gloss()` 加单前缀 `해설 — `，调用串首前缀已剥离，渲染双前缀 `해설 — 해설` 为 **0**，中文前缀 `译注｜`/`讲解｜` 为 **0**。剥离的是冗余前缀而非内容，无内容损失（W43 EN×KO 先例）。另：P1 另有 1 处同式单前缀盒 `해설 — a midterm 중간선거 · a ballot 투표용지`（非 gloss() 调用，同样单前缀），故全书 `해설 — ` 起首节点共 6 处（P1 盒 + 5 个 gloss 盒），徽章串内另含 1 处 `한국어 해설 — `（非 gloss 前缀），口径如上，不得与 5 盒混淆。

## 7. P7 定义句与金句

- **定义句**：P7 上部（y<1236）英语行多重集核心=分版（纯无 CJK 拉丁行 60=60；剥离 CJK 后的拉丁行 70=70），**定义句本地化 0 处**（定义句本身不含韩语，韩语只在独立的语法点行）。上一轮报告的“62 行”与本轮“60 行”之差为纯数字/标点碎片行的计数口径差，内容多重集相等，结论一致。
- **金句 8 句（英文原文逐字，核心=分版）**：
  1. (page 1) `Tuesday, November 3, is Election Day in the United States.` — A2
  2. (page 2) `The hour from 1 to 2 happened twice.` — A2
  3. (page 3) `Which film would you choose ?` — B1
  4. (page 4) `Two games, two continents, one league — that is the modern NFL.` — B1
  5. (page 5) `The results will still be there in the morning.` — B2
  6. (page 6) `Patience is part of the system, not a failure of it.` — B2
  7. (page 2) `Not every place changes.` — A2
  8. (page 4) `One Sunday is not enough — good thing the week has seven days.` — B1
- **级别序列**：[A2, A2, B1, B1, B2, B2, A2, B1]；**页签**：[1, 2, 3, 4, 5, 6, 2, 4]（P7 卡面练习号 100–107 的级别标与此一致：100 A2 / 101 A2 / 102 B1 / 103 B1 / 104 B2 / 105 B2 / 106 A2 / 107 B1）。
- **页签口径澄清**：金句本身标签 8 个（上列）；全 P7 的 `(page N)` 出现共 **11 处**，按页为 1:1、2:4、3:1、4:2、5:1、6:2，核心=分版；两者不得混淆。
- **全册句频（整书 8 页归一化计数）**：按金句源串顺序，核心=分版 = **[3, 2, 2, 2, 2, 4, 3, 2]**。

## 8. 读者园地

- **英语信件逐字冻结、零编造**：P7 x=1013，y=1956/1986.53/2017.06 三行，核心与分版逐字、逐坐标相同（行断点处以空格连接）：
  `« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`。
  核心无英语披露句，本版未凭空新写英语披露句。
- **韩语披露句逐字摘录**（P7 x=1013，y=2076/2104/2132，连接）：
  `편집부 알림｜VOL.1에서는 VOL.2에 실제 편지를 싣겠다고 약속했지만, 발행 때까지 실제 편지도 VOL.1 쓰기 투고도 도착하지 않았어요. 편지를 지어내지 않고 예시를 싣습니다. 여러분의 편지와 쓰기를 보내 주세요. VOL.3부터 실제 편지를 싣겠습니다.`
  - 3 事实逐项核实：① 无真实来信（`실제 편지도 … 도착하지 않았어요`）；② 无 VOL.1 写作投稿（`VOL.1 쓰기 투고도 도착하지 않았어요`）；③ 示例非编造 + 承诺顺延 VOL.3（`편지를 지어내지 않고 예시를 싣습니다` + `VOL.3부터 실제 편지를 싣겠습니다`）。
  - 显性祈使邀请：`여러분의 편지와 쓰기를 보내 주세요.`。
  - VOL.3 刊登承诺：`VOL.3부터 실제 편지를 싣겠습니다.`。
  - 内容预告行不计作征集：P7 下方 NEXT WEEK / VOL.3 预告盒（退伍军人节、NFL 慕尼黑赛、中期选举结果）仅为下期预告，邀请与承诺均已在披露段内成立。
  - **最佳 P8 作文范围裁定**：披露称 VOL.1 写作投稿未收到，覆盖范围是投稿类整体，而非另有一篇已选出的最佳作文未刊；另 P8 H（VOL.2 写作）英文提示中的 `The best texts will appear in VOL.3 (page 7, « Readers' Corner »).` 是面向 VOL.2 写作的前瞻承诺，与 VOL.1 缺投稿的说明是两回事，不得混淆。
- **读者园地盒几何**：读者园地盒 (989, 1878, 896, 300) 与其下 VOL.3 深色盒 (989, 2202, 896, 338) 核心=分版逐值相同，披露行在盒内、与 VOL.3 盒分离（卡面亦确认）。其余 P7 小级别标矩形的 y 位移源于韩语语法行重排，非读者园地盒变化，occlusion 0 亦证无重叠。

## 9. 家具 / W43 三方对照

- **徽章**：本版 P1 徽章元素与 W43 逐值相同 — x=975、y=372、19.5pt、粗体、fill `#a4553a`（BRICK）、middle 锚点、文本 `영어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`；它原位替换核心 y=372 的标语槽（核心该槽为 19.0pt 非粗体英文标语），因 372 槽是标语而非冻结正文，故 W43 同配对先例成立。
- **顶带中行**：本版与 W43 逐字相同 — `WEEKLY IN ENGLISH · 매주 발행 · 미국이 읽는 영어`（x=975，y=92，21pt）；右侧周次行按 W45 核心重推导 — `WEEK OF NOVEMBER 2 TO 8, 2026`（W43 为 2026-10-19 至 25，属正常周次差异）；左上角 `VOL. 2`（W43 为 `VOL. 1 · FIRST ISSUE`）。
- **页脚与页码行**：全 8 页相同式 — 左 `The Lucerna · 영어 주간지 VOL.2 · 텍스트는 영어 · 해설은 한국어`（x=65，y=2624），右 `제 N 면 / 총 8 면`（x=1885，y=2624）；W43 为 VOL.1 同式。
- **节头双语式**：全版为 `ENGLISH HEAD · 韩语短名`，与 W43 同式：P1 `THE BIG STORY · 헤드라인`、P2 `LIFE · 생활`、P3 `CULTURE · 문화`、P4 `SPORT · 스포츠`、P5 `YOUTH · 청년`、P6 `DEEP READ · 시사 심층`、P7 `LANGUAGE IN HAND · 정밀 해설`、P8 `EXERCISES & ANSWERS · 연습과 정답`。
- **gloss 单前缀**：见 §6（`해설 — `，双前缀 0）。
- **P8 头与分隔符**：P8 带右注 `FINAL TEST · 종합 평가 · Answers at the bottom of this page · 정답은 이 면 아래쪽에`；分隔 `— 제 N 면 —` 8 个齐全。
- **题型标签**：印刷标签齐全；SVG 出现计数：`빈칸 채우기` 24（= 核心 `填空` 24）、`바꿔 쓰기` 16 + 桥句祈使 `바꿔 쓰세요` 4 = 20（= 核心 `改写` 20）、`단어와 뜻 짝짓기` 4、`짝짓기` 6、`오류 고치기` 4、`도표 읽기` 1、`읽기 이해` 1、`번역` 3、`쓰기` 22、`대화 완성` 1 等。注意区分：注册类型 `문장 바꾸기`（16–19、42–45、60–63、78–81 题）与 `따라 연습`（100–107 金句练习）为注册表类型，核心与本版在渲染中均不印刷该词（P2–P5 印刷的节标签为 `바꿔 쓰기`，P7 金句练习不印 instr 标签），故“渲染中查无”不是缺失。
- **P7 英文 `(page N)`**：见 §7（金句标签保持英文，核心=分版）。

## 10. 题量 / 范文 / ABSTRACT / 图片 / 双 PDF

- **登记展开独立计数（本科对员用构建树 `dump_reg.py` 对本版与核心构建目录分别重 dump，见 §12 程序说明）**：本版与核心均为 **150 题**，级别 **A2 60 / B1 69 / B2 21**，页分布 **[10, 17, 18, 18, 18, 18, 12, 39]**，题号 1–150 连续。页/级别逐题错配 **0**；类型串全部为中→韩本地化（类别顺序相同，非错配）。
- **键差异**：恰为 [137, 138, 139, 140, 150]（与 p8 keydiff 一致，见 §4）。
- **注差异（注册口径）**：变更 129 项、不变 21 项；不变项为 [17, 18, 36, 42, 43, 45, 54, 55, 60, 61, 62, 63, 78, 79, 80, 81, 101, 106, 107, 118, 120]，皆为纯英文中立注；变更注 ASCII 词损失为 0。
- **范文 85 词逐字一致**：渲染 P8 MODEL 框（x≥989，y 1550–1800）逐字 = 构建源串，核心=分版，均为：`On Tuesday, November 3, our family watched the election results at home. We ate pizza, because nobody wanted to cook on such a night. On television, the map changed colour, state by state, and my father said : « Ohio is too close to call ! » I did not understand every state, but I understood the pizza and the excitement. On Sunday night, the clocks had fallen back, so I slept one hour more. It was a long night, and a very American one.` 计数口径为**空格分词 85**（含数字 token `3,` 与标点 token `:`、`«`、`!`、`»`）；纯字母 token 计为 80，属不同口径，不构成差异。H 写作题标题为《My Tuesday, November 3》（80–100 词）。
- **ABSTRACT.txt（253 字节，单行 + 换行结尾）**：`미국 중간선거일과 시계 되돌리기, 할로윈, 금요일 영화 개봉과 일요일 마드리드 NFL 경기를 한국어 해설과 함께 영어로 읽는 The Lucerna 영어 주간지 VOL.2, A2부터 B2까지 150문제로 영어 공부하기`。逐项勾选：韩语单行 ✓；无 ASCII 双引号 ✓；真实主题关键词 ✓（美国中期选举日、时钟回拨、万圣节、周五电影上映、周日马德里 NFL 赛）；学习者搜索短语 ✓（`150문제로 영어 공부하기`）；刊名 ✓（The Lucerna）、目标语 ✓（영어/영어로）、A2–B2 ✓、150 题 ✓；汉字 0；哈希与 pre-fix 基线相同，未变。
- **图片载荷逐页 = 核心**：逐页 data URI 载荷 base64 SHA-16 对比 — P1 `3ded9ef91750b108`、P2 `83f543d47bf04644`、P3 `1edd2d6b05ed3a49`、P4 `44b6a2ba28df3a01`、P6 `d041d0fce488122c`，核心=分版（解码字节 SHA 亦相等）；P5/P7/P8 两版均无图。署名在版，核心=分版逐字相同：P1 `Kenneth C. Zirkel — CC0, via Wikimedia Commons`、P2 `Public domain, via Wikimedia Commons`、P3 `Édouard Manet — CC0, via Wikimedia Commons`、P4 `Frank R. Snyder — public domain, via Wikimedia Commons`、P6 `Public domain, via Wikimedia Commons`。全部为公有领域/CC0，符合 SOP。
- **双 PDF 核查**：印刷 PDF `The-Lucerna-VOL2-KO.pdf` 21,530,271 字节、8 页（1462.5×2025.0），SHA `305b69f2413cb500f80f03d6229d7115e68e40d9286775eea5ea7c6cd4691949`；网页 PDF `The-Lucerna-VOL2-KO-web.pdf` 3,898,191 字节、8 页（1400.0×1938.0），SHA `380f734d1f2094eb9426827ce3b08153929f7598a7fe710f2bcd88b22642df0f`；与修复声称值逐值一致。卡片 PNG 均为 1950×2700 RGB。

## 11. 非阻塞观察（单列，不得计入阻塞；纸面正确，KIT 文字问题不得因此改纸面）

1. 尾 1–2 音节词中/助词切分 16 处（§3 全表），低于 ≥3 门槛，按先例判非问题；卡面可见但不影响可读性判断。
2. 右缘 2 行（P8 F 选项行，超 1885 未超 1950），核心逐值继承（§5）。
3. 披露段语体混用：披露段含 2 处合쇼체形式 — `예시를 싣습니다`、`실제 편지를 싣겠습니다`（全书 `습니다` 出现恰为此 2 处），其余韩语均为 해요체；W43 全书 `습니다` 为 0。此为语体不一致，但两句均为语法正确的编辑部正式表述，不影响事实与版式，列为非阻塞观察，不升格为阻塞（与上一轮相同）。
4. KIT §5 仍为上一轮（round-3）旧数，未随 §10 更新：freeze diff `2452`（实测 2438）、印刷 PDF 21,530,330 字节 / `9a805dba…`、网页 PDF 3,898,955 字节 / `8ce20818…`、P8 SVG `4bf81c17…`；§10 已声明新 PDF 值 supersedes §5，但 §5 的 freeze/P8 旧数未获同等 supersede 声明。纸面（SVG/PDF）以 §10 新值为准且实测一致，故仅为 KIT 文字滞后，非阻塞。
5. KIT §1 称 P8 翻译为“EN↔KO”，与 §6 逐项方向（137/140 英语指令保留译 EN→KO；138/139 韩语标签 + 英语原句）相比表述不精确；纸面以 §6 与渲染为准，非阻塞。
6. KIT §10 的 16 候选 prose 算术不成立（“14 减 #67 加 모|범”得 14 而非 16；#67 从不在 14 项尾 ≤2 集中）。正确映射见 §3（14 − 지 − 칸 + 일|부/원|형/선|거일/모|범 = 16）；原始候选文件 `fix1b-ko-candidates.txt` 本身所列 16 项与本科对独立扫描一致，故仅为 KIT prose 错误，非阻塞。
7. KIT §10 称基线“18 件”，而 `fix-round1-prefixed.sha256` 实为 20 条（`fix1b-postfix.sha256` 为 18 条，因其不含 KIT/ABSTRACT）；改动范围本身经逐项哈希验证无误（§1），仅为计数口径差，非阻塞。
8. KIT “full-width punct 0”表述不精确（§2）：精确测量为 `。` 0、（）0、`｜` 5 处核心沿用分隔符；KIT 自身 `。` 5 处全部在文档引用层（1 处门控表 + 4 处核心中文键原文引用），不在渲染文本中。
9. p8.py 的 `--core-dir/--edition-dir --target ko` 形式对 EN 族失效（映射到 `p8-siheom.svg`），是工具映射问题，不是分版缺陷；直接 SVG 路径 + `--total 150` 有效且 CLEAN。
10. P8 印刷注中 3 段保留纯英文语法注（107、118、120），为核心不变注，汉字 0，非中文残留。
11. P6 选票框的 ☐ 字形在卡面显示为小框符号，与核心相同，非本版缺陷。
12. W43 同配对在现行 canonical 工具下重跑有 2 处 LINEX（P1/P6），为 W43 自身已上架状态，与本版（0 flags）无关，不计入本版门禁。

## 12. 程序说明与校对前后哈希

- **校对前后哈希**：开工前已记录 `deliverables-before.sha256` 与 `core-before.sha256`；终态重算 `deliverables-final.sha256` 与 `core-final.sha256`，**两组 diff 均为空**（另有登记展开后的中间哈希 `deliverables-after-reg.sha256` / `core-after-reg.sha256`，亦与开工前相同），交付物与核心内容无变动。
- **程序合规（上一轮披露事项的纠正）**：本轮**未在原地运行任何会把 SVG 写回交付目录/核心目录的脚本**。登记展开做法：把分版构建树与核心构建树分别拷到本科对证据 scratch（`scratch-reg-ed/`、`scratch-reg-core/`，仅保留 import 闭包 content*/bslib4/svglib/assets + dump_reg 副本），用正则把 5 个 content 文件的 OUT 重定向到本科对 scratch SVG 目录，grep 确认闭包内无真实 `files/weekly-report` 路径残留（残留仅见于未被 import 的 render/transform，已从 scratch 闭包中删除），再分进程运行 dump_reg。Scratch 重渲染 **8/8 SVG 与交付 SVG 逐字节相同**（P8 亦为 `7cee4087…`），且运行后交付/核心哈希不变。freeze 基线重跑亦经 freeze.py 自身 repoint 到证据 scratch。rowcheck/rightedge 逻辑拷至本科对 scratch 后只读运行，未写交付目录。
- **未做事项**：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch 目录、未宣布上架。

## 证据目录

`hidden_files/w45/en-ko-proof2/`：

- `REPORT.md`（本报告）、`deliverables-before.sha256`、`deliverables-final.sha256`、`core-before.sha256`、`core-final.sha256`、`deliverables-after-reg.sha256`、`core-after-reg.sha256`、`prefix-scope-diff.txt`
- `freeze-baseline.log/.json`、`freeze-diff.log/.json`、`freeze-removed.txt`、`removed-adjudication.txt`、`english-preservation.txt`、`english-word-multiset.txt`、`cjk-counts.txt`
- `ko_scan_independent.py`、`ko-scan-proof2.txt`、`ko-scan-build-patched.txt`
- `p8-compare.txt/.json`、`p8-core-extract.txt/.json`、`p8-ed-extract.txt/.json`、`p8-compare-dir.txt`、`p8-compare-149-negative.txt`、`p8-keydiff-lines.txt`、`p8-note-language.txt`
- `gloss-p7.txt`、`gloss-p7-readers.txt`、`p7-golden.txt`、`readers-furniture.txt`
- `occlusion-selftest.txt`、`occlusion-edition.txt/.json`、`occlusion-core.txt/.json`、`occlusion-new.txt/.json`、`occlusion-w43.txt/.json`、`rowcheck-edition.txt`、`rowcheck-core.txt`、`rightedge-edition.txt`、`rightedge-core.txt`、`chart-ls.txt`
- `reg-edition.json`、`reg-core.json`、`reg-analysis.txt`、`counts-essay-images.txt`
- `scratch-freeze/`、`scratch-geom/`、`scratch-reg-ed/` + `scratch-reg-ed-svg/`、`scratch-reg-core/` + `scratch-reg-core-svg/`、`crops/`（P8 4 处修复区裁剪）
