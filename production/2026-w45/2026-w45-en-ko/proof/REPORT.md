# W45 EN×KO 独立校对报告 — The Lucerna VOL.2（英语正文 × 韩语讲解）

- **校对对象**：`files/weekly-report-w45-en-ko/`（SVG ×8、卡片 PNG ×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **核心对照**：`files/weekly-report-w45-en-core/`（EN VOL.2，150 题）
- **W43 同配对对照**：`files/weekly-report-en-ko/`（只读）
- **构建树**：`hidden_files/weekly-report-w45-en-ko-build/`（只读使用；除下述程序说明外未改动）
- **校对时间**：2026-10-27 21:19 EDT 起（UTC 2026-10-28 01:19 起），本报告完成于 UTC 2026-10-28 01:40 前后
- **校对员立场**：只校对、不改源码、不宣布上架。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未清理共享 scratch 目录。

## 结论：不能定稿 — 4 项阻塞性缺陷

**本版不是 ZERO PROBLEMS。** 除下列 4 项外，其余全部重测项通过（含冻结、P8、几何、gloss、读者园地、家具、题量、范文、ABSTRACT、图片）。4 项均为**韩语词中切分（S3，尾 ≥3 音节）**，全部在 P8 答案流，全部被构建员自带的 `ko_scan.py` 漏检（机理见 §2）。卡面目视确认这 4 处在 P8 卡上可见，不是 SVG 文本假象。

| # | 位置 | 渲染断点 | 尾音节 | 源串（构建源） | 渲染行 |
|---|---|---|---|---|---|
| B1 | P8，x=527，y=2042.51→2062.66 | `휴대\|전화예요` | 4 | `두 번째 화면은 휴대전화예요`（#67 注） | `67. B (두 번째 화면은 휴대` / `전화예요)` |
| B2 | P8，x=527，y=2390.87→2411.02 | `일\|부예요` | 3 | `인내는 제도의 일부예요`（#93 注） | `93. C (인내는 제도의 일` / `부예요)` |
| B3 | P8，x=527，y=2517.58→2537.73 | `동\|사원형` | 3 | `would + 동사원형`（#102 注） | `102. would (would + 동` / `사원형)` |
| B4 | P8，x=1451，y=1895.65→1915.8 | `선\|거일은` | 3 | `선거일은 11월 3일 화요일이에요`（#149 注） | `149. Tuesday (선` / `거일은 11월 3일 화요일이에요)` |

**判据口径**：工具 README #16 规定的“≥3 音节尾”标准；ES×KO 先例（`자치|주예요` 等）与 RU×KO 先例（`나|타내요`，尾 3，阻塞）同口径。已退役的“首段 ≤1 音节”判据不等价，不得使用。

**修复方向**（由构建线执行，本校对员不改源码）：缩短相应注或改写措辞，使断点落在词界；例如 #93 删 `의`、#102 缩为 `would + 원형`、#67/#149 改写为更短的同义注。**修复后必须单进程重渲染并以 10–45 窗口 + 括号片段覆盖重扫全书，并重跑全部门（occlusion、P8、freeze diff），不得只修 `ko_scan.py` 的判定而不修版面。** P8 注的改动会引起答案流重排，因此只扫 P8 不够，必须全书重扫。

---

## 1. 冻结与英语正文

- **freeze.py baseline（本校对员独立重跑，不采信构建员“后台输出丢失后前台重跑”的取证）**：用原始核心构建目录 `hidden_files/weekly-report-w45-en-build`，freeze.py 自身 repoint 到证据 scratch，**8/8 逐字节复现**。核心 SHA 前 16 位与交付核心一致：p1 `c7e7d019de01e662`、p2 `07f5df7e8e7ea076`、p3 `d9f7cc374fe1229c`、p4 `3b8be5175094bcb7`、p5 `73486e2f216e1f3b`、p6 `3e2187b37acb2883`、p7 `5a2684096010839c`、p8 `4de34a135cc831bf`。运行后核心重哈希不变。
- **英语正文无丢失**：全部被删串逐项裁定，均为中文讲解层/家具中文，或英文部分在本版同页保留。仅两处英文家具串缺失，均为有意家具替换：P1 核心标语 `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`（y=372，19.0pt 非粗体）被 W43 同式徽章原位替换；各页页脚 `LUCERNA ENGLISH WEEKLY` 被新页脚替换。W43 EN×KO P1 同样无该标语、页脚同式，证实为家具而非正文丢失。
- **新增 CJK 逐页计数（SVG 文本节点）**：P1 208、P2 237、P3 153、P4 176、P5 169、P6 185、P7 452、P8 872，**合计 2452 字，100% Hangul、汉字 0**。
  - 口径说明：freeze diff 的 CJK 分页合计为 2457（P3/P4/P5/P6/P7 各比 Hangul 计数多 1），差额是 freeze CJK 正则把 U+FF5C 全角竖线 `｜` 计入所致。`｜` 在 P3–P7 各 1 处，均为核心同位沿用的栏目标签分隔符（如核心 `五句影评｜` → 本版 `다섯 문장 평｜`、核心 `编辑说明｜` → 本版 `편집부 알림｜`），不是新增全角标点缺陷。核心全书 `｜` 远多于本版（P1 1、P2 2、P3 3、P4 3、P5 3、P6 3、P7 10、P8 0），本版 `｜` 是其子集。
- **全角 `。` 为 0**：SVG 全部 8 页文本节点 `。`=0，全角括号 `（`/`）`=0。KIT 中的 5 处 `。` 全部在文档引用层，不在渲染文本中：1 处在门控表里写明“`。` 0”，4 处是 §6 引用的核心中文键原文（如 `耐心是制度的一部分，而不是制度的失败。`），不构成渲染缺陷。
- **违禁词“桥接”**：SVG + KIT + ABSTRACT 均为 0。
- **KIT 措辞不准确（非阻塞，见 §11）**：KIT 称“full-width punct 0”，若把 `｜` 计入则不成立；精确表述应为“`。` 0、（）0、`｜` 5 处为核心沿用分隔符”。

## 2. 韩语专项（重点，窗口 10–45）

窗口说明：RU×KO 先例证实 15–45 窗口会结构性排除 P8 答案行，本次全部扫描使用 **10–45 窗口**。扫描范围为全书全部页面、全部栏位（未抽样），包括 P8 答案流。

### 2.1 构建员自带扫描复核

构建员自跑 `ko_scan.py`（窗口 10–45）结果 S1 0 / S2 4 / S3 0 / S4 0，本校对员重跑数字一致，但 **S3=0 不成立**，原因如下。

**漏检机理（已实证）**：`ko_scan.py` 的 S3 判定用空格分词 + `first.split("(")[0]`，且排除以 `(` 开头的续行。当断点两侧带括号时，`last+first_tok` 含 `(`/`)`，不在语料中，故漏检。这正是工具 README #16（PT×KO 先例）要求“必须覆盖括号片段”的情形。

**修正后全量扫描**（证据 `ko-scan-corrected.txt`，判定：末词元尾部 Hangul 串 + 首词元首部 Hangul 串在语料中连续）：同 x 列共 **18 处候选**，其中尾 ≥3 者恰为结论中的 4 项（B1–B4），其余 14 处尾 1–2 音节，按 RU×KO/ES×KO 先例判非问题（见 §2.4）。跨 x 列扫描（`ko-scan-crossx.txt`）为空，无缩进续行漏检。

> 废弃方法声明：曾做过一次用全量去空格语料的补充扫描（`ko-scan-supplementary.txt`），该方法会把词界换行误判为词中切分，已废弃，不得引用。

### 2.2 S2 4 项逐个复核 — 皆为非缺陷

1. P2，x=1330，y=1660：`= two times(두 번)` — 报时词汇表行（左列 `twice`），完整词条，非切分。
2. P8，x=1451，y=369.45：`번역: On Sunday, the NFL plays in Madrid.` — 完整翻译题干（韩语标签 + 英语全句）。
3. P8，x=65，y=2043.97：`13. quarter to · 14. twice (두 번 = twice) · 15. extra · 16.` — 流式答案行，行尾 `16.` 为题号标点。
4. P8，x=65，y=2539.19：`55. faster · 56. b · 57. d · 58. a (fan=팬 a) · 59. c · 60.` — 同上，行尾 `60.` 为题号标点。

### 2.3 行首孤标点与单字尾普查 — 无新增缺陷

- 行首孤标点普查（`ko-scan-extra.txt`）：全部行首标点行 Hangul 数均为 0，皆为英语正文换行（`: `、`»`、`?`、`,` 等），**韩语行首孤标点为 0**。
- 单字尾/末词元 1 音节普查：所列项均为完整词、助词/词尾收尾或词汇条目（如 P2 `두 번/한 번 더`、P4 `· a fan 팬.`、P8 答案流题号行），无新增缺陷。
- 词界换行（如 P2/P5/P7 的 `결과를|발표하다`、`두|문장을`）是正常词界断行，不是词中切分，不得计入。

### 2.4 尾 ≤2 的 14 处候选 — 非阻塞观察（不计入阻塞）

P3 `명대|사`（尾 1）、P6 `영|향을`（尾 2）、P6 `선|거의`（尾 2）、P7 `대조|를`（尾 1）、P7 `바뀌|는`（尾 1）、P7 `하|나`（尾 1）、P8 `의|문문`（尾 2）、P8 `헤이더|가`（尾 1，R3 修复后状态，见 §5）、P8 `돌핀|스`（尾 1）、P8 `경|기는`（尾 2）、P8 `지|도`（尾 1）、P8 `오하이오|는`（尾 1）、P8 `경기|를`（尾 1）、P8 `칸|에`（尾 1）。卡面可见但低于 ≥3 门槛，按先例判非问题。

## 3. P7 定义句与金句

- **定义句**：P7 上部（y<1236）英语行 62 行，核心与本版多重集相同；**定义句本地化 0 处**（定义句本身不含韩语，韩语只在独立的语法点行）。
- **金句 8 句**（以核心 content7.py 源串顺序实测，英文原文逐字保留，核心=本版）：
  1. (page 1) `Tuesday, November 3, is Election Day in the United States.` — A2
  2. (page 2) `The hour from 1 to 2 happened twice.` — A2
  3. (page 3) `Which film would you choose?` — B1
  4. (page 4) `Two games, two continents, one league — that is the modern NFL.` — B1
  5. (page 5) `The results will still be there in the morning.` — B2
  6. (page 6) `Patience is part of the system, not a failure of it.` — B2
  7. (page 2) `Not every place changes.` — A2
  8. (page 4) `One Sunday is not enough — good thing the week has seven days.` — B1
- **级别序列**：[A2, A2, B1, B1, B2, B2, A2, B1]，与 en-es/en-fr/en-it/en-pt 四版独立实测的核心序列一致（本结论以本校对员自己的核心实测为准）。
- **页标签口径澄清**（不得直接引用构建员未说明口径的数字）：
  - 金句本身标签：8 个，顺序 [1, 2, 3, 4, 5, 6, 2, 4]，核心=本版。
  - 全 P7 的 `(page N)` 出现：共 11 处，按页为 1:1、2:4、3:1、4:2、5:1、6:2，核心=本版；构建员的“(1/4/1/2/1/2)”实为此口径，数字本身经独立重测正确，但原表述未说明口径。
  - 全册句频（整书 8 页归一化计数）：按金句源串顺序，核心=本版 = [3, 2, 2, 2, 2, 4, 3, 2]（3/4 次者因该句同时出现在正文/P7 定义例/P8 翻译或练习中）。

## 4. P8

- **p8.py compare（显式双路径，EN 族必须用 `--total 150`）**：
  - 有效路径：直接 SVG 路径 + `--total 150`（默认 total 会取 W43 的 149 产生伪影，故必须显式用 150），结果 **CLEAN，核心 78 = 本版 78 noted，missing=[]，extra=0，uncertain=[]，keydiff=[137, 138, 139, 140, 150]**。78 项口径由核心 P8 渲染内容独立确立（`p8-core-extract.json` / `p8-ed-extract.json`），两版集合逐值相同；因此“EXTRA_ONLY 可接受”在此不适用（实际为 CLEAN，更强）。
  - 第二路径说明：`--core-dir/--edition-dir --target ko` 形式失败，因工具把 ko 映射为 `p8-siheom.svg`，而 EN 族 P8 文件为 `p8-exercices.svg`（FileNotFoundError，证据 `p8-compare-dir.txt`）；另以 p8.py 的分段提取作第二验证路径。dir 形式失败是工具映射问题，不是分版缺陷。
- **keydiff 逐项印刷行对照，全部合法**：
  - 137：题干英语 `Translate: « Patience is part of the system, not a failure of it. »` 冻结；键 中文 `耐心是制度的一部分，而不是制度的失败。` → 韩语 `인내는 제도의 일부예요, 실패가 아니에요.`；注 `part of 一部分；not a failure 不是失败` → `part of = 일부분; not a failure = 실패가 아님`。
  - 138：题干英语冻结（标签 `翻译：` → `번역：`）；键 中文 `11 月 3 日周二是美国的选举日。` → 韩语 `11월 3일 화요일은 미국의 선거일이에요.`。
  - 139：题干英语 `On Sunday, the NFL plays in Madrid.` 冻结；键 中文 `这周日，NFL 在马德里比赛。` → 韩语 `일요일에 NFL이 마드리드에서 경기를 해요.`。
  - 140：题干英语 `Not every place changes.` 冻结；键 中文 `并非每处都拨回时钟。` → 韩语 `모든 곳이 시계를 되돌리는 건 아니에요.`（注：核心键把句子窄化为拨钟语境，韩语键按印刷英文直译）。
  - 150：写作装置行，核心 `开放题 — 要点见写作框，范文在第 8 版写作框内` → 韩语 `열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에`，非答案内容变更。
  - **方向裁定（以渲染为准）**：4 道翻译题题面全为英语句子、键在核心为中文，即实际为 EN→ZH（本版为 EN→KO）；核心 KIT “英↔中双向”说法与渲染不符，渲染为准；本版 KIT 未重复双向说法，137/140 标 EN→KO，138/139 标题干重定向。
- **注变更口径澄清（两种口径，不得混用）**：
  - 印刷段口径（p8.py 分段提取，证据 `p8-note-change.txt`）：印刷段变更 78 项（恰为印刷注集合），不变 72 项（皆为裸键纯英文）；变更段的 ASCII 词损失为 0。
  - 注册注口径（KIT §5 的 129/21）：注册表 150 项的 note 字段比较，变更 129 项、不变 21 项；不变项为 [17, 18, 36, 42, 43, 45, 54, 55, 60, 61, 62, 63, 78, 79, 80, 81, 101, 106, 107, 118, 120]，皆为纯英文中立注（如 `she → is going to`、`1:30 = half past one`，无 CJK）；变更注 ASCII 词损失为 0；注册键差异恰为 [137, 138, 139, 140, 150]。
  - P8 注释语言：78 个印刷注段中汉字 0 处；75 段含 Hangul，3 段保留纯英文语法注（107 `has (have → has)`、118 `B (be going to → is going)`、120 `B (1:30 = half past one)`），属上述 21 项不变注，非中文残留，不构成缺陷。
  - 印刷笔记集合按题号相等（无 EXTRA_ONLY）。

## 5. 修复轮验证

- **R1→R2（声称 8 处、变化页 P2/P4/P6/P7/P8）**：
  - 注册表比较（`reg-edition.json` → `reg-edition2.json`）仅 3 项变更：#30 注缩短（删 `고양이`）、#137 键改写、#139 键删 `이번 주`。
  - 逐页 freeze diff 比较（`diff-round1.json` → `diff-round2.json`）显示变化页恰为 P2/P4/P6/P7/P8，P1/P3/P5 字节相同；轮次基线哈希比较亦证实同一页集合。
  - 8 处 distinct 编辑修复的构成：P2 2 处（be going to 指令改写 + ¿Y TÚ? 段语序调整重排）、P4 1 处（gloss `to defend` 改写）、P6 1 处（桥段 `하나의 숫자` → `숫자`）、P7 1 处（would 语法点缩短）、P8 3 处（#30、#137、#139）；P8 其余行变化为缩短引起的重排，非独立修复。
  - 措辞说明（不掩盖）：P2 指令由“计划与将要发生的事”窄化为“说计划时”，属讲解层措辞缩短，无练习内容损失。
- **R2→R3（声称仅 P8 一处）**：
  - 注册表比较（`reg-edition2.json` → `reg-edition3.json`）仅 #30 注变更：`빌 헤이더가 목소리를 맡아요` → `헤이더가 목소리를 맡아요`。
  - 轮次基线哈希比较（round2 → round3）仅 P8 哈希变更，其余 7 页相同；逐页 diff 比较亦仅 P8 变化。
  - 删 `빌 ` 后文义无损失：题干与 P3 正文均给出全名 Bill Hader（P3：`with Bill Hader as the voice of the Cat`；P8 #30 题干选项含 `C. Bill Hader`），注中仅留姓氏 `헤이더` 在语境中指代唯一；断点确实移出人名：R2 为 `헤|이더가`（人名内切分），R3 渲染为 `(헤이더` / `가 목소리를 맡아요)`，人名完整在上一行，助词 `가` 在下一行。
- **transform 3 缺陷已修（从终态验证）**：
  - 漏拷 svglib：已补，md5 `0703a8814abe388f131c89f3d7ffb946`，与核心 svglib 相同。
  - MAP 值引号破环：终态渲染成功；缺失的 2 条 MAP 已补：`对话补全` → `대화 완성`（transform.py:257–258，content8.py 与渲染 P8 G 头均已呈现）、cloze 注 `still 仍然` → `still 여전히`（渲染 P8 `(still = 여전히)` 已呈现）。
  - 终态 scratch 重跑（证据 `scratch-edition/` + `scratch-edition-render.log`）：将本版构建树（content*、bslib4、svglib、run.py、assets）拷到证据 scratch，OUT 重定向到 scratch（并 grep 确认无真实交付路径残留），单进程 `run.py` 重渲染，**8/8 SVG 与交付 SVG 逐字节相同**，总题 150，P8 键 y=1965（R3 值）。
  - 本版构建 content*/bslib4.py 中汉字 0 处，佐证无缺失 MAP 导致的中文残留。
  - 无“基线缺失”问题：核心基线与本版终态均已用 scratch 复现；若报告中提及过程记录缺口，须指明不涉及未实测项。

## 6. 几何

- **canonical `tools/occlusion_audit.py`（自检先行）**：6 类（BOXTITLE、COVER、EDGE、FOOTER、LINEX、TEXTX）全部触发、干净对照静默；**分版 0 flags、核心 0 flags、NEW vs core 0**。证据 `occlusion-selftest.txt`、`occlusion-edition.txt/.json`、`occlusion-core.txt/.json`。
- **同基线墨迹碰撞扫描**（构建树 `rowcheck.py`，同页同基线、间距 <6 为 flag）：**分版 0、核心 0**。证据 `rowcheck-edition.txt`、`rowcheck-core.txt`。框线压框由 occlusion 的 BOXTITLE 类覆盖，0 flags。
- **P6 图表标签（正确口径：基线锚定墨迹法，PIL `getmetrics` + `anchor="ls"` 的 textbbox；无锚 `getbbox` 法是错误口径，已弃用；证据 `chart-ls.txt`）**：4 标签墨迹盒与核心逐值相同 — `No lines: 38%` (527.0, 1170.2, 683.0, 1189.4)、`Work on Tuesday: 29%` (527.0, 1222.8, 785.2, 1247.0)、`Travel plans: 21%` (527.0, 1275.4, 729.0, 1299.4)、`Habit: 12%` (527.0, 1328.0, 655.0, 1347.2)；被后续不透明矩形覆盖 0.00%（门 <30%）。EN 版 P6 图表实为纯文本行（content56.py 注明“text bars in flow”，无绘制条形），故覆盖为 0 是结构性的，非测量遗漏；P6 矩形与核心逐值相同（25 个 rect）。
- **全页右缘 ADVANCE 扫描**（构建树 `rightedge.py`，解码度量 + advance 法；证据 `rightedge-edition.txt`、`rightedge-core.txt`）：仅 2 行，均超 1885 右缘线、未超 1950 页边，且核心逐值同构继承：
  - P8，x=1485，y=806.4：`b. an election in the middle of a term`，serif 23pt 非粗体，advance 414.4，右缘 1899.4（超 14.4，距页边 50.6）。
  - P8，x=1485，y=882.4：`d. the paper you mark your choice on`，同字体，advance 418.8，右缘 1903.8（超 18.8，距页边 46.2）。
  - 两行皆为 P8 F 词汇配对选项行（match_set 前缀致超），核心同坐标、同字体、同文本、同 advance，非本版新缺陷。
- **卡片目视（8/8 已全部目视，不得抽查）**：P1–P8 卡片均已目视：版面干净，无重叠、无缺文、无截断；P1 徽章/顶带/页脚、P2 时钟与词汇表、P3 gloss、P4 体育、P5 青年、P6 图表文本行与选票框、P7 读者园地盒与 VOL.3 深色预告盒分离、P8 练习与答案流均正常。唯一卡面可见的缺陷即结论中的 4 处 P8 尾 ≥3 切分；另见非阻塞现象 P3 gloss `명대|사`（尾 1）、P7 工具箱 `하|나`（尾 1）等，属尾 ≤2 候选，已判非问题。

## 7. gloss

- 渲染后 `gloss()` 串按 `·` 拆分：**核心 = 本版逐项 1:1，共 18 项**；分盒为 P2 3 / P3 4 / P4 4 / P5 3 / P6 4（content12 1 盒、content34 2 盒、content56 2 盒，共 5 次 gloss() 调用）。
- 每对英文词头均保留（如 `to fall back`、`a costume`、`trick or treat`、`to open`、`a fixture`、`a map`、`to register` 等），仅讲解层译为韩语。
- **双前缀清理**：核心自身 5 处双前缀 — gloss() 加 `译注｜` 叠加调用串首的 `讲解｜`，渲染为 `译注｜讲解｜`（P2–P6 各 1 处）；本版 gloss() 加单前缀 `해설 — `，调用串首前缀已剥离，渲染双前缀 `해설 — 해설` 为 0，单前缀 5 处；剥离的是冗余前缀而非内容，无内容损失。证据 `gloss-readers.txt`。

## 8. 读者园地

- **英语信件逐字冻结、零编造**：P7 x=1013，y=1956/1986.53/2017.06 三行，核心与本版逐字、逐坐标相同：`« On Sunday, I slept one hour more — and I still woke up late! » — M. L., a reader in Chicago (editor's example: no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`。核心无英语披露句，本版未凭空新写英语披露句（读者园地内英语仅为该冻结信件与栏头）。
- **韩语披露句逐字摘录**（P7 x=1013，y=2076/2104/2132，joined）：`편집부 알림｜VOL.1에서는 VOL.2에 실제 편지를 싣겠다고 약속했지만, 발행 때까지 실제 편지도 VOL.1 쓰기 투고도 도착하지 않았어요. 편지를 지어내지 않고 예시를 싣습니다. 여러분의 편지와 쓰기를 보내 주세요. VOL.3부터 실제 편지를 싣겠습니다.`
  - 3 事实逐项核实：① 无真实来信（`실제 편지도 … 도착하지 않았어요`）；② 无 VOL.1 写作投稿（`VOL.1 쓰기 투고도 도착하지 않았어요`）；③ 示例 + 承诺顺延 VOL.3（`편지를 지어내지 않고 예시를 싣습니다` + `VOL.3부터 실제 편지를 싣겠습니다`）。
  - 显性祈使邀请：`여러분의 편지와 쓰기를 보내 주세요.`（请寄来你们的信件与写作），为披露段内祈使句。
  - VOL.3 刊登承诺：`VOL.3부터 실제 편지를 싣겠습니다.`。
  - 内容预告行不计入邀请：P7 下方 NEXT WEEK / VOL.3 预告盒（退伍军人节、NFL 慕尼黑赛、中期选举结果）仅为下期预告，不作为邀请证据；邀请与承诺均已在披露段内成立。
  - **最佳 P8 作文覆盖范围裁定**：核心披露的“VOL.1 写作投稿”即 VOL.1 H 写作任务的投稿类；披露称该类投稿未收到，故无可刊登的“最佳作文” — 覆盖范围是投稿类整体，而非另有一篇已选出的最佳作文未刊；另 P8 H（VOL.2 写作）英文提示中的“The best texts will appear in VOL.3”是面向 VOL.2 写作的前瞻承诺，与 VOL.1 缺投稿的说明是两回事，不得混淆。
- **读者园地盒几何**：核心与本版矩形多重集相同，读者园地盒 (989, 1878, 896, 300)，其下 VOL.3 深色盒 (989, 2202, 896, 338)，披露行在盒内、与 VOL.3 盒分离（卡面亦确认）。

## 9. 家具 / W43 三方对照

- **徽章**：本版 P1 徽章元素与 W43 逐值相同 — x=975、y=372、19.5pt、粗体、fill `#a4553a`（BRICK）、middle 锚点、文本 `영어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`；它原位替换核心 y=372 的标语槽（核心该槽为 19.0pt 非粗体英文标语），因 372 槽是标语而非冻结正文，故 W43 同配对先例胜过 README #20 泛化规则（泛化规则的 574 插入仅适用于 372 为冻结正文行的情形，此处不适用）。
- **顶带中行**：本版与 W43 逐字相同 — `WEEKLY IN ENGLISH · 매주 발행 · 미국이 읽는 영어`（x=975，y=92，21pt）；右侧周次行按 W45 核心重推导 — `WEEK OF NOVEMBER 2 TO 8, 2026`（W43 为 2026-10-19 至 25，属正常周次差异）。
- **页脚与页码行**：全 8 页相同式 — 左 `The Lucerna · 영어 주간지 VOL.2 · 텍스트는 영어 · 해설은 한국어`（x=65，y=2624），右 `제 N 면 / 총 8 면`（x=1885，y=2624）；W43 为 VOL.1 同式。
- **gloss 单前缀**：见 §7（`해설 — `，5 处，双前缀 0）。
- **节头双语式**：全版为 `ENGLISH HEAD · 韩语短名`（如 `THE BIG STORY · 헤드라인`、`LIFE · 생활`、`READ THE CHART · 도표 읽기`、`READERS' CORNER · 독자 코너`），与 W43 同式；P8 带右注：`FINAL TEST · 종합 평가 · Answers at the bottom of this page · 정답은 이 면 아래쪽에`。
- **P8 分隔**：`— 제 N 면 —` 8 个齐全。
- **题型标签**：印刷标签齐全（`문장 완성`、`객관식`、`단어 짝짓기`、`바꿔 쓰기`、`빈칸 채우기`、`단어와 뜻 짝짓기`、`오류 고치기`、`도표 읽기`、`읽기 이해`、`번역`、`쓰기`、`짝짓기`、`대화 완성` 等）；注意区分：注册类型 `문장 바꾸기`（16–19、42–45、60–63、78–81 题）与 `따라 연습`（100–107 金句练习）为注册表类型，核心与本版在渲染中均不印刷该词（P2–P5 印刷的节标签为 `바꿔 쓰기`，P7 金句练习不印 instr 标签），故“渲染中查无”不是缺失。
- **P7 英文 `(page N)`**：见 §3（金句标签保持英文，核心=本版）。
- **해요체对照**：除披露段 2 处合쇼체形式外，全书韩语均为 해요체（见 §11 第 3 条）。

## 10. 题量 / 范文 / ABSTRACT / 图片

- **登记展开独立计数（本校对员用构建树 `dump_reg.py` 对本版与核心构建目录分别重 dump，证据 `reg-proof.json` / `reg-core-proof.json`）**：本版与核心均为 **150 题**，级别 **A2 60 / B1 69 / B2 21**，页分布 **[10, 17, 18, 18, 18, 18, 12, 39]**，题号 1–150 连续，逐题页/级别错配 0。
- **范文 85 词逐字一致**：渲染 P8 MODEL 框（x≥989，y 1550–1800）逐字 = 构建源串，核心=本版，均为：`On Tuesday, November 3, our family watched the election results at home. We ate pizza, because nobody wanted to cook on such a night. On television, the map changed colour, state by state, and my father said : « Ohio is too close to call ! » I did not understand every state, but I understood the pizza and the excitement. On Sunday night, the clocks had fallen back, so I slept one hour more. It was a long night, and a very American one.` 计数口径为**空格分词 85**（含数字 token `3,` 与标点 token `:`、`«`、`!`、`»`）；纯字母 token 计为 80，属不同口径，不构成差异。
- **ABSTRACT.txt（本版，253 字节，单行 + 换行结尾）**：`미국 중간선거일과 시계 되돌리기, 할로윈, 금요일 영화 개봉과 일요일 마드리드 NFL 경기를 한국어 해설과 함께 영어로 읽는 The Lucerna 영어 주간지 VOL.2, A2부터 B2까지 150문제로 영어 공부하기`。逐项勾选：韩语单行 ✓；无 ASCII 双引号 ✓；真实主题关键词 ✓（美国中期选举日、时钟回拨、万圣节、周五电影上映、周日马德里 NFL 赛）；学习者搜索短语 ✓（`150문제로 영어 공부하기`）；刊名 ✓（The Lucerna）、目标语 ✓（영어/영어로）、A2–B2 ✓、150 题 ✓；汉字 0。
- **图片载荷逐页 = 核心（构建员报告未提图片，本校对员补查）**：逐页 data URI 载荷 SHA-16 对比 — P1 `3ded9ef91750b108`、P2 `83f543d47bf04644`、P3 `1edd2d6b05ed3a49`、P4 `44b6a2ba28df3a01`、P6 `d041d0fce488122c`，核心=本版；P5/P7/P8 两版均无图。署名在版，核心=本版逐字相同：P1 `Kenneth C. Zirkel — CC0, via Wikimedia Commons`、P2 `Public domain, via Wikimedia Commons`、P3 `Édouard Manet — CC0, via Wikimedia Commons`、P4 `Frank R. Snyder — public domain, via Wikimedia Commons`、P6 `Public domain, via Wikimedia Commons`。
- **双 PDF 核查**：印刷 PDF `The-Lucerna-VOL2-KO.pdf` 21,530,330 字节、8 页（1462.5×2025.0），SHA `9a805dba23f7a6dc2d25f9e196d2fe8b9300dfdd178f43f973a76254ba0539b1`；网页 PDF `The-Lucerna-VOL2-KO-web.pdf` 3,898,955 字节、8 页（1400.0×1938.0），SHA `8ce20818fbc8ba537f08f505d0109f4bafca2e5713309e2b0eb2e0b45a4fa4df`；大小与 SHA 均与 KIT §5 记载一致。卡片 PNG SHA 与 KIT 记载的 `round3-cards-pdfs.sha256` 一致（p7 `397c2356…`、p8 `4bf81c17…`，见终态哈希表）。

## 11. 非阻塞观察（单列，不得计入阻塞）

1. 尾 1–2 音节词中/助词切分 14 处（§2.4），低于 ≥3 门槛，按先例判非问题；卡面可见但不影响可读性判断。
2. 右缘 2 行（P8 F 选项行，超 1885 未超 1950），核心逐值继承（§6）。
3. 披露段语体混用：本版披露段含 2 处合쇼체形式 — `예시를 싣습니다`、`실제 편지를 싣겠습니다`，其余韩语（包括披露段的 `도착하지 않았어요`、`보내 주세요`）均为 해요체；W43 全书 `습니다` 为 0、W45 其他 KO 版披露段亦只用 해요체（如 `실어요`）。此为语体不一致，但两句均为语法正确的编辑部正式表述，不影响事实与版式，暂列为非阻塞观察，不升格为阻塞。
4. R1→R2 的 P2 be going to 指令窄化（§5），属讲解层措辞缩短。
5. 核心 KIT “英↔中双向”说法与渲染不符（实际为 EN→ZH），以渲染为准；本版 KIT 已纠正为 EN→KO/题干重定向表述。
6. KIT “full-width punct 0”表述不精确（§1）：精确测量为 `。` 0、（）0、`｜` 5 处核心沿用分隔符。
7. p8.py 的 `--core-dir/--edition-dir --target ko` 形式对 EN 族失效（映射到 `p8-siheom.svg`），是工具映射问题，不是分版缺陷；直接 SVG 路径 + `--total 150` 有效且 CLEAN。
8. P8 印刷注中 3 段保留纯英文语法注（107、118、120），为核心不变注，汉字 0，非中文残留。
9. （待主线判断，不影响本版定稿门）P6 选票框的 ☐ 字形在卡面显示为小框符号，与核心相同，非本版缺陷。

## 12. 程序说明与校对前后哈希

- **校对前后哈希**：开工前已记录 `deliverables-before.sha256` 与 `core-before.sha256`；终态重算 `deliverables-final.sha256` 与 `core-final.sha256`，**两组 diff 均为空**，交付物与核心内容无变动。
- **程序披露（必须如实记录）**：本校对员在验证登记展开时直接运行构建树 `dump_reg.py`，该脚本导入 content 模块时会把 SVG 重写回交付目录与核心目录（确定性重渲染）。事后核对证明内容无变动（before/final SHA diff 为空，仅 mtime 被刷新），但严格说这是一次对交付目录的写操作，程序上本应先把构建树拷到 scratch 再重定向 OUT。本报告如实披露此事，供主线判断；除此之外，全部校对工具均为只读（freeze 基线重跑亦经 freeze.py 自身 repoint 到证据 scratch，核心重哈希不变；终态 scratch 重跑的 OUT 同样重定向到证据 scratch 并 grep 确认无真实交付路径残留）。
- **开工查重**：开工时唯一在途渲染进程属 ja-de 版（cwd 为 weekly-report-w45-ja-de-build），非本版；本版交付物静默已超 2 分钟，判定安全开工。
- **未做事项**：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未清理共享 scratch 目录、未宣布上架。上架由主线串行执行；本报告结论为“不能定稿”，待 4 项阻塞修复并重跑全部门后，须另行复核。

## 证据目录

`hidden_files/w45/en-ko-proof/`：

- `deliverables-before.sha256`、`deliverables-final.sha256`、`core-before.sha256`、`core-final.sha256`、`deliverables-after.sha256`、`core-after.sha256`
- `freeze-baseline.log/.json`、`freeze-diff.log/.json`、`removed-adjudication.txt`
- `ko-scan-proof.txt`、`ko-scan-extra.txt`、`ko-scan-corrected.txt`、`ko-scan-crossx.txt`（`ko-scan-supplementary.txt` 已废弃，不得引用）
- `p7-analysis.txt`、`p7-golden.txt`
- `p8-compare.txt/.json`、`p8-core-extract.txt/.json`、`p8-ed-extract.txt/.json`、`p8-compare-dir.txt`、`p8-keydiff-lines.txt`、`p8-note-change.txt`
- `gloss-readers.txt`、`readers-furniture.txt`、`furniture.txt`
- `occlusion-selftest.txt`、`occlusion-edition.txt/.json`、`occlusion-core.txt/.json`、`rowcheck-edition.txt`、`rowcheck-core.txt`、`rightedge-edition.txt`、`rightedge-core.txt`、`chart-ls.txt`
- `scratch-edition/` + `scratch-edition-render.log`、`scratch-freeze/`
- `reg-proof.json`、`reg-core-proof.json`、`counts-essay-images.txt`
