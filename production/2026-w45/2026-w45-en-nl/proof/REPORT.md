# 独立校对报告 — Lucerna Weekly W45 EN × NL（The Lucerna VOL.2）

**结论：ZERO PROBLEMS（无阻塞项）。** 本报告仅为独立校对结论，**不宣布上架**（上架由主线串行执行）。
非阻塞观察单列于末节，不影响结论。

**校对对象：** `files/weekly-report-w45-en-nl/`（svg ×8、cards ×8、print PDF、web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
**对照：** EN 核心 `files/weekly-report-w45-en-core/`（VOL.2，刊头 The Lucerna）；W43 同配对已上架版 `files/weekly-report-en-nl/`（只读对照）
**构建树（只读核查，未修改）：** `hidden_files/weekly-report-w45-en-nl-build/`（transform.py、content 文件、build-log-r1–r4、occlusion-r2/r4、p8-compare-r2）
**校对方式：** 只校对、不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch 目录。全部重测均为校对员独立运行（tools/freeze.py、p8.py、occlusion_audit.py、自写几何/gloss/P7/读者园地/登记表脚本），构建员自述一律未采信、逐项重测。

## 0. 开工查重与哈希基线

- 开工时交付物最新 mtime 为 2026-10-28 00:41（UTC），70 秒复查零新写盘，判定为已完成交付的新鲜 mtime，**未 stand down**，安全开工。唯一在跑进程为无关的 EN×FR insert（`insert.py --target en --native fr`），未触及 EN×NL 目录。
- 校对前记录交付物与核心全部 sha256（`pre-deliverables.sha256`、`pre-core.sha256`）；校对后复核（`post-deliverables.sha256`、`post-core.sha256`），**diff 为空：交付物与核心哈希全部不变**。
- 交付物 SVG 哈希与 KIT §13 一致；双 PDF：print `The-Lucerna-VOL2-NL.pdf` 17,294,737 B、sha `d839bf9885cae89961e865aea4794f5d909a7fbf18cbc2f0f6df514d96e58f37`；web `The-Lucerna-VOL2-NL-web.pdf` 4,032,284 B、sha `1d8d5de624df09bb7d11a6765bbbaebc575943d09cfe05e9016a5f46cb480206`；与任务书及 KIT §12 完全一致。双 PDF 均为 8 页（print 页幅 1462.5×2025，web 1400×1938）；8 卡片均为 1950×2700 PNG。

## 1. 冻结（freeze.py）

- `freeze.py baseline`（核心构建树 → scratch 重定向重跑）：**8/8 逐字节复现**，核心 shipped 哈希与 KIT §1 表一致（p1 `c7e7d019…`、p2 `07f5df7e…`、p3 `d9f7cc37…`、p4 `3b8be517…`、p5 `73486e2f…`、p6 `3e2187b3…`、p7 `5a268409…`、p8 `4de34a13…`），运行前后核心重哈希不变。
- `freeze.py diff` 核心 vs 分版：每页新增 CJK = 0，分版 CJK = 0（P1–P8：核心 CJK 183/197/119/139/134/136/347/776 → 分版 0/0/0/0/0/0/0/0）。违禁词“桥接”在全部 8 张 SVG、KIT、ABSTRACT 中出现 **0 次**。
- 被删非 CJK 串逐项裁定（以全页分版文本为词元库重查；初版朴素分词因全角括号被当作 CJK 删除而产生 `isis`、`B11` 等拼接伪影，改用标点作分隔符后伪影消失）：
  - 其余全部被删串的非 CJK 词元均在同页分版全文在场（重排碎片、gloss/注释重排、题型/页脚本地化）。
  - 真正不在场的词元仅以下四类，全部合法（见末节“构建员表述修正”a、b）：
    1. P1 徽章槽位替换：`THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA` 被 W43 徽章串整槽替换，`LEARNERS/LIFE/FROM` 不在场属预期家具替换。
    2. P2–P8 页脚替换：核心页脚 `The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY` 被荷兰语页脚整串替换，`WEEKLY`（P6/P8 连带 `ENGLISH`，因该页他处无此词）不在场属预期家具替换。
    3. P1 日期本地化：`11 月 3 日…` 的 `11`（月份数字）变为荷兰语月份词 `november`（`Nov 3`、`3 november` 均在场），内容未丢。
    4. P8 题干重定向：见 §2（4 条重定向题干，非构建员简述的 2 条）。

## 2. P8（p8.py compare，显式双路径形式，独立重跑）

- 命令：`tools/p8.py compare --core-p8 …/en-core/svg/p8-exercices.svg --edition-p8 …/en-nl/svg/p8-exercices.svg --total 150`。
- 结果与构建员一致：**core 78 noted，edition 150 noted，EXTRA_ONLY，missing=[]，extra_count=72，uncertain=[]，keydiff=[137, 138, 139, 140, 150]**，exit 0。非字面 CLEAN，但按 p8.py 判定规则 EXTRA_ONLY 属 adjudicated acceptance，且与已上架 W45 EN×DE、EN×FR 兄弟独立重跑结果**完全同型**（同为 78 vs 150、missing=[]、同一 keydiff、同一 extra 集合）。
- 全 150 键对照（keys 字典直接比对，非仅 noted 集）：**145 键逐字节一致**，仅以下 5 键不同——即“其余 145 键”的准确含义（noted 集比较另见下）：
  | # | 核心印行键（REG 原文） | 分版印行键 | 裁定 |
  |---|---|---|---|
  | 137 | 耐心是制度的一部分，而不是制度的失败。 | Geduld is een deel van het systeem, geen falen van het systeem. | 合法：英→荷翻译题，题干已重定向为 `Vertaal: « Patience is part of the system, … »` |
  | 138 | 11 月 3 日周二是美国的选举日。 | Dinsdag 3 november is verkiezingsdag in de Verenigde Staten. | 合法：同上，题干 `Vertaal: Tuesday, November 3, is Election Day in the United States.`（核心该题干标签为中文 `翻译：`，见修正 a） |
  | 139 | 这周日，NFL 在马德里比赛。 | Deze zondag speelt de NFL in Madrid. | 合法：同上，题干 `Vertaal: On Sunday, the NFL plays in Madrid.`（核心标签亦为 `翻译：`） |
  | 140 | 并非每处都拨回时钟。 | Niet elke plaats zet de klok terug. | 合法：同上，题干 `Vertaal: « Not every place changes. »` |
  | 150 | 开放题 — 要点见写作框，范文在第 8 版写作框内（REG 原文；印行附注 `(Beoordeel op punten)` 对应核心附注“按要点给分”） | Open vraag — punten in het schrijfblok; voorbeeldtekst in het kader op pagina 8（附注 `(Beoordeel op punten)`） | 合法：写作装置，与 W43 NL #149 同类（W43 原文：`149. (open vraag — het voorbeeld staat in het schrijfblok op deze pagina) (beoordeling op de punten uit de opdracht)`，同为无唯一答案的开放题装置，非答案错误） |
- 5 条注释均不含括号伪影：p8.py 全部解析干净；印行附注分别为 `(part of = een deel; not a failure = geen falen)`、`(Election Day = verkiezingsdag; on Tuesday)`、`(on Sunday = op zondag; in Madrid)`、`(not every = niet elke; change = veranderen)`、`(Beoordeel op punten)`，括号仅为 P8 统一的半角括号注释包装，注释内容本身无嵌套括号。
- P8 注释纯荷兰语（按注释集合口径）：分版 P8 全部文本 CJK = 0（核心 P8 为 595 个 CJK 字符）；170 个半角括号注释段 CJK = 0，解释语言为荷兰语；注释内出现的英语词元均为被释 headword（如 `ballot = stembiljet` 的 `= ` 形式），非英语解释。P8 写作框内冻结英语任务语（如 `80 to 100 words`）不属于答案注释，不计入此口径。
- P8 印刷笔记集合相等性（EXTRA_ONLY 可接受）：核心印 78 条 ⊂ 分版印 150 条，missing=[]；多出的 72 条恰为核心过滤掉的短注集合，与 DE/FR 兄弟的 extra 集合逐项相同。分版 P8 字体：`font-size="13.5"` 计 111 次、`15.5` 计 0 次；分隔符 `— Pagina 1 —` 至 `— Pagina 8 —` 各 1 次。
- **W43 62 vs W45 78 口径说明（不得混淆）：** W43 KIT §5 实测：W43 VOL.1 核心印 62 条、W43 NL 印同一 62 条（15.5pt，集合相等）；W45 VOL.2 核心印 78 条、W45 NL 印全部 150 条（13.5pt）。两个数字分属不同期、不同核心、不同印行策略，不是同一口径的矛盾；W45 形式与 DE/FR 兄弟一致。

## 3. 几何

- `occlusion_audit.py` 自检先行通过（6 类全触发，干净对照静默）；分版重跑 **0 flags**、核心重跑 **0 flags**、**NEW 0**（与构建员 occlusion-r4.json 一致）。
- 同基线墨迹扫描（解码后 PIL ink box，全部 8 页）：**干净**；同基线碰撞扫描（同 y、墨迹重叠 >0.5px）：8 页 **0 碰撞**。
- 右缘 ADVANCE 扫描（内框右缘 1910）：8 页 **0 越过**，各页最大 advance 右端：P1 1885.0、P2 1885.0、P3 1885.0、P4 1888.6、P5 1885.0、P6 1885.0、P7 1885.0、P8 1903.8。
- 框线压框扫描（外框 28..1922 / 28..2672）：8 页 **0**。
- P6 图表覆盖（基线锚定墨迹法，PIL getmetrics，anchor ls，门限 <30%）：8 页最大覆盖 **0.0%**（P6 图表为流式文本行 `No lines : 38%` 等，其后无矩形覆盖）。
- R2→R3 的 4 NEW 旗标在终态逐项确认消除（R2 原始旗标见 occlusion-r2.json）：
  1. P1 searches 副标题 EDGE + BOXTITLE（同一文本，2 旗标）：终态文本 `Deze week gezocht · Google Trends VS`，墨迹右端 1822.0 ≤ 1950 且在框内；
  2. P1 word-of-week LINEX（第 2 行被 row-B 规则线压）：终态单行 `Midden van een termijn: tussentijdse verkiezing.`，墨迹 (1451.0, 1804.8, 1876.0, 1824.8)，终态 occlusion 无 LINEX；
  3. P8 `Levels :` LINEX（被写作条规则线压）：终态 `Levels : 145–148 [A2] · 149 [B1]`（y=1362.0，墨迹底 1365.5），P8 battery 流程终点由 R2 的 y=1513 降至 R4 的 y=1390（间隙 11→8 生效），终态 occlusion 无 LINEX。
- R4 干净验证：build-log-r4、transform-run-log、registry-edition-log 中 `FLOW OVERFLOW` / `HEAD TOO WIDE` 计 **0**。

## 4. P1 深色带行专项像素验证

- 构建员 KIT 措辞的准确所指：**0.1px 是修复前完整串的间隙，不是已发串的间隙**。transform-log 记录：初版映射 `周二选举日 · 周日已拨回时钟` → `DINSDAG VERKIEZINGSDAG · ZONDAG KLOK TERUG`，预渲染宽度检查记 “P1 dark-band right line gap 0.1px -> KLOK TERUG”（即删 ZONDAG 的原因）。校对员独立复算该修复前串：Sans Bold 24pt 下右串 advance 左端 1243.97，左冻结英语行 advance 右端 1243.94，**advance 间隙 0.03px**，与构建员 0.1px（取整/度量口径）一致，证实该数字确有所指、非凭空。
- **已发串实测：** `DINSDAG VERKIEZINGSDAG · KLOK TERUG`（x=1855 anchor=end，y=478）对冻结英语行 `AMERICA VOTES ON TUESDAY — AND THE CLOCKS FELL BACK !`（x=95，y=478）：advance 间隙 **105.28px**，墨迹间隙 **105.56px**（左墨迹右端 1243.75，右墨迹左端 1349.31）。第二行配对间隙亦宽裕（墨迹约 70px）。卡片像素复核（crop-p1-band.png，全幅目视 + 亮像素列扫描）：两行清晰分离、可读，间隙列无桥接墨迹（仅左行 `!` 的 2 个边缘像素）。
- 与 W43 已上架版同类：W43 NL 深色带已发串间隙更大（大行墨迹间隙 154.35px，小行 105.7px），且 W43 KIT 同样记载“完整串墨迹碰撞 → 删尾指针”（小行 `AMERIKA PAS OP 1 NOVEMBER`）。W45 已发串与 W43 已发串同属“删减后宽裕间隙、可读”一类。**结论：已发串真实不相触、可读性不受影响，非阻塞，按继承同类裁定。** 任务书“0.1px 在度量误差内”的担忧针对的是修复前串，不适用于已发串。

## 5. gloss（渲染后重建 + 源串双重独立实测）

- 源串（content 文件 gloss() 调用，按 · 拆分，核心独立实测）：核心 P2 3、P3 4、P4 4、P5 3、P6 4，合计 **18**；分版同分布 **18**，1:1。
- 渲染后重建（gloss 框 `#f1ead6` 矩形 + 框内 20.5pt Sans 文本拼接，按 · 拆分；初版宽口径拼接误含框外文本，收紧口径后干净）：核心与分版逐页逐项一致，分布同为 3/4/4/3/4。分版每项均在渲染 SVG 在场，且保留 W45 核心的 `=` 形式（如 `ballot = stembiljet`、`to fall back = de klok terugzetten`），非 W43 的 `,` 形式；前缀为 `Uitleg — `（核心渲染前缀为其自有 `译注｜讲解｜` 双前缀，属核心自有写法，分版单前缀为正确本地化，非缺失）。
- 注意：P1 的 `Uitleg — midterm = …` 为 bridge() 串（4 项），不在 gloss() 口径内，不计入上述 18 项。

## 6. P7

- 结构与核心一致：刊头 `LANGUAGE IN HAND · Taal in handen`（y=116）；四栏头同 y=227：`LEVEL A2 · Basis`、`LEVEL B1 · Verder`、`LEVEL B2 · Uitdaging`、`THE TOOLBOX · Gereedschap`；各栏 A2 FALLING BACK + GOING TO + VERB、B1 COMPARATIVES + THE PAST SIMPLE、B2 HEADLINE PRESENT + WHETHER = IF ?，各带 THE EXAMPLE 框；TOOLBOX 三句随身句（每级一句）；`PHRASES OF THE WEEK · Zinnen van de week (allemaal uit dit nummer)`（y=1236）、`THE ERROR CLINIC · Fouten`（y=1903）、`READERS' CORNER · Lezershoek`（y=1918）、`NEXT WEEK · VOL.3 Volgende week`（y=2248），位置与核心一一对应。
- 定义句逐字保留：A2 例 `Americans are going to vote on Tuesday.`、B1 例 `The clocks fell back on Sunday, November 1.`、B2 例 `Patience is part of the system, not a failure of it.` 及栏内定义句（`The clocks fell back.`、`She is going to vote on Tuesday.`、`The Bernabéu is bigger than most stadiums.`、`Nobody knows whether the race is called yet.`、TOOLBOX 三句）在核心与分版 P7 中出现次数**完全相等**；易错诊所 4 句英语原句逐字一致（`He don't like voting early.`、`Yesterday the clocks falled back.`、`This game is more bigger than last week's.`、`She is going to watches the film on Friday.`）；仅 gloss/语法点/注释本地化为荷兰语（如 `Grammatica | …`）。
- 金句 8 句原文逐字 + 级别序列 + 页标签 + 全期出现次数（核心 vs 分版，全期拼接文本计数）：
  1. `Tuesday, November 3, is Election Day in the United States.`（page 1，A2，100）— 3 = 3
  2. `The hour from 1 to 2 happened twice.`（page 2，A2，101）— 2 = 2
  3. `Which film would you choose ?`（page 3，B1，102）— 2 = 2
  4. `Two games, two continents, one league — that is the modern NFL.`（page 4，B1，103）— 2 = 2
  5. `The results will still be there in the morning.`（page 5，B2，104）— 2 = 2
  6. `Patience is part of the system, not a failure of it.`（page 6，B2，105）— 4 = 4
  7. `Not every place changes.`（page 2，A2，106）— 3 = 3
  8. `One Sunday is not enough — good thing the week has seven days.`（page 4，B1，107）— 2 = 2
  页标签序列 1/2/3/4/5/6/2/4、级别序列 A2/A2/B1/B1/B2/B2/A2/B1、次数序列 3/2/2/2/2/4/3/2 均与核心一致。

## 7. 读者园地

- 英语信件逐字冻结验证：核心英语信件三行在分版 P7 同 y（1956 / 1986.53 / 2017.06）逐字保留：`« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`。核心本无英语披露句，分版亦**未凭空新写任何英语披露句**。
- 荷兰语披露句逐字摘录（同 y 2076 / 2104 / 2132，框内 3 行）：
  1. `Toelichting | VOL.1 beloofde echte brieven in VOL.2, maar er kwamen geen echte brieven en`
  2. `geen VOL.1-schrijfwerk binnen. We verzinnen niets: het voorbeeld blijft, eerlijk gemarkeerd.`
  3. `Stuur je brief in — in VOL.3 publiceren we de brieven die we ontvangen!`
- 逐项核实：① 无真实来信（`geen echte brieven`）✓；② 无 VOL.1 写作投稿（`geen VOL.1-schrijfwerk`）✓；③ 示例诚实保留（`het voorbeeld blijft, eerlijk gemarkeerd`）+ 顺延至 VOL.3（第 3 行 VOL.3 刊登收到的来信）✓；显性祈使邀请（`Stuur je brief in`，祈使句）✓；VOL.3 承诺（`in VOL.3 publiceren we …`）✓。内容预告行（NEXT WEEK 的 `Woensdag Veteranendag, zondag de NFL in München; plus verslag van de midtermresultaten.`）未被算作邀请。
- 最佳 P8 作文覆盖范围裁定：披露写的是“无 VOL.1 写作投稿”（geen VOL.1-schrijfwerk binnen），范围与核心中文披露（“未收到真实来信与 VOL.1 写作投稿”）一致，即**全部 VOL.1 写作投稿皆无**，故无最佳篇可谈——不是仅称“无最佳篇”而隐瞒其余投稿。无编造、无虚构人名/引言（M. L. 信件为核心原有示例，附诚实标注）。

## 8. 家具与 transform 复现

- 副刊头：`ENGELS WEEKBLAD · VOL.2 · STEMMEN · VOETBAL · FILMS`（W43 为 VOL.1 · STADIONS · STEMMEN · POMPOENEN，卷次与主题更新属预期）。
- P8 全注释 13.5pt + 半角括号 + `— Pagina N —` 分隔符：见 §2（W43 为核心 62 条集 15.5pt，口径差异见 §2）。
- P8 battery 间隙 11→8：content8.py 中 `gap=8` 计 10 处、`gap=11` 计 0 处；transform.py 底部在 apply_shared() 之后对 B/C/D 三类（Meerkeuze / Leestekst / Zinnen aanvullen）做 gap 替换，终态流程与 R4 日志一致。
- 量宽后的框题缩短（每项在框验证，advance + 含墨迹的有框矩形数）：`THE WEEK IN NUMBERS · Cijfers` 370.5（框内 3）、`SUNDAY, NOVEMBER 8 · Zondag` 367.8（3）、`TOO CLOSE TO CALL · Onbeslist` 366.5（3）、`FIVE SENTENCES · Vijf zinnen` 341.5（3）、`A PRACTICE BALLOT · Stembiljet` 374.9（3）、`READ THE CHART · Grafiek` 336.8（2）、`D · SENTENCES · Zinnen vormen` 407.1（2），全部在框内；另 `THE WEEK IN NUMBERS` 等其余框题亦在框内。深色带行见 §4。gloss `=` 形式见 §5。
- 徽章、顶带、页脚、页码行、gloss 前缀与 W43 已上架形式逐字一致（卷次除外）：徽章 `TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`（W43=True，分版=True）；顶带 `WEEKLY IN ENGLISH · ELKE WEEK EEN NUMMER · HET ENGELS DAT AMERIKA LEEST`（同）；页脚形式 `The Lucerna · ENGELS WEEKBLAD VOL.n · TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS`（W43 为 VOL.1，分版为 VOL.2，余逐字）；页码行 `Pagina N van 8`（P1–P8 各 1）；gloss 前缀 `Uitleg — `；带后缀 LIFE · Leven / CULTURE · Cultuur / SPORT · Sport / YOUTH · Jeugd / DEEP READ · Verdieping / LANGUAGE IN HAND · Taal in handen / EXERCISES & ANSWERS · Oefeningen en antwoorden 全部在场。
- 题型名：登记表题型词汇与 W43 KIT 所列荷兰语词汇**逐项一致**（12 名：Zinnen aanvullen 33、Meerkeuze 41、Zinnen omvormen 16、Woorden combineren 20、Grafiek lezen 6、Gatentekst 8、Leestekst 4、Vertalen 4、Dialoog aanvullen 5、Fouten verbeteren 4、Meedoen 8、Schrijven 1；与核心各题型计数一一对应）。渲染说明：P1–P7 不印题型全名，只印短指令（`Vul in`、`Herschrijf`、`Combineer`，均多处在场）；P8 电池头见末节观察（D/G/H 与 W43 渲染头有差异，词汇本身一致）。
- **transform.py 单独复现验证（关键）：** 全新核心构建副本 + 当前 transform.py（287 次替换，exit 0）→ content 文件与构建树 content 文件**逐字节一致**（content12/34/56/7/8 + bslib4.py，6/6）；再重跑 → 8 张 SVG 与交付物**逐字节复现 8/8**。另 run.py 全新重跑亦 8/8 逐字节复现交付。结论：终态完全由 transform.py 复现，**不存在未同步的手工改动**。修复轮叙事（R1→R2 桥接/数字行 + P8 D 头；R2→R3 4 旗标；R3 首次间隙尝试因对 pre-mapping 串断言失败、P1 修复已应用、间隙替换移至 apply_shared() 之后作 R4）与 transform.py 现状（短桥接串、短 searches 串、单行 word-of-week、gap 替换在 apply_shared() 之后）及 transform-log 尾注一致。

## 9. 图片、摘要、卡片、题量、范文、PDF

- 图片载荷与核心逐页相等：P1 1、P2 1、P3 1、P4 1、P5 0、P6 1、P7 0、P8 0；每页 image href sha256 核心 = 分版（P1 `58010598…`、P2 `960958ec…`、P3 `989526b0…`、P4 `86b34e8f…`、P6 `85b54b4f…`）；构建资产文件与核心构建资产逐字节相等（5 图 + CREDITS.md + meta.json）。署名在版：P1 `Kenneth C. Zirkel — CC0, via Wikimedia Commons`、P2 `Public domain, via Wikimedia Commons`（1912 明信片）、P3 `Édouard Manet — CC0, via Wikimedia Commons`（并注明非电影剧照）、P4 `Frank R. Snyder — public domain, via Wikimedia Commons`、P6 `Public domain, via Wikimedia Commons`，与核心逐字一致，皆为公有领域/CC0。
- ABSTRACT.txt：荷兰语单行（375 字节，尾换行 1 个，无内换行）、ASCII 双引号 **0 个**、含真实主题关键词（verkiezingsdag 3 november、klok 1 november、Halloween、The Cat in the Hat、Godzilla Minus Zero、NFL Madrid、Grand Prix São Paulo、hoe Amerika stemt）+ 学习者搜索短语 `Engels te leren door te lezen` + `150 oefeningen` + `A2 tot B2`。
- 8 卡片全部逐页目视（非抽查）：P1–P8 无溢出、无重叠、无规则线压字、无页脚侵入；P7 读者园地披露在框内 3 行；P8 `Levels :` 行与写作条规则线分离；P6 选票框、图表标签清晰。P6 选票复选框 ☐ 在核心与分版渲染中同为方框字形，属继承表现，非分版缺陷。
- 题量与级别（登记表独立重跑，scratch 重定向）：150 题连续 1–150；A2 60 / B1 69 / B2 21；页分布 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；页/级别与核心 150 条逐条一致，键仅 137–140、150 不同（§2），题型仅中→荷本地化；登记表注释 CJK 0 条、空注释 0 条（核心亦 0 条）。
- 范文 85 词：P8 MODEL `On Tuesday, November 3, our family watched …` 以空白分词计 85 词，与核心逐字节一致（同一计数法下核心亦 85 词）。

## 非阻塞观察（不影响 ZERO PROBLEMS 结论）

1. **构建员“两条 Translate 题干”简述不完整。** 实际为 4 条重定向题干：137、140 为 `Translate :` → `Vertaal:`；138、139 核心标签为中文 `翻译：` → `Vertaal:`。英语题干句本身逐字未动，仅标签本地化；freeze 被删串中 4 条均可对应。属表述修正，非内容问题。
2. **构建员“徽章槽位替换”简述未单列页脚替换。** freeze 缺失的 `WEEKLY`/`ENGLISH` 实为 P2–P8 页脚整串替换（W43 荷兰语页脚形式），与徽章替换同属家具替换类，已在 §1 裁定。属表述补全，非内容问题。
3. **P1 深色带 0.1px 的所指。** 该数字属修复前 ZONDAG 版（§4 复算 0.03px），已发串间隙 105px。任务书压缩表述易误读为已发串相触，特此澄清；已发串本身无问题。
4. **P8 渲染电池头 vs W43 渲染头有三处不同（词汇本身一致）：** D `Zinnen vormen`（W43：`Zinnen`）、G `Dialoog aanvullen`（W43 缩短为 `Dialoog`）、H `Schrijven [B1]`（W43：`Schrijven`，分版 [B1] 承自核心 `写作 [B1]`）；A/B/C/E/F 与 W43 逐字一致。D 为量宽缩短（已披露、在框验证通过），G 为全名形式，H 为核心级别标签携带；三者均为荷兰语、在框内、无溢出，故非阻塞。
5. **KIT 与 p8 提取的 138 号间距差异。** p8 提取拼接换行时丢一空格（`3日`），登记表 REG 原文为 `11 月 3 日周二是美国的选举日。`，与 KIT 一致；属提取拼接伪影，非内容差异。
6. **P8 注释“纯荷兰语”的口径。** 指答案注释集合（无 CJK、解释语为荷兰语）；注释内英语 headword 与写作框冻结英语任务语不在此口径内（见 §2），不构成混入英语解释。
7. **P6 选票 ☐ 字形。** 核心与分版渲染同为方框，属字体继承表现，非分版引入缺陷。

## 证据文件（本校对目录）

- `hidden_files/w45/en-nl-proof/REPORT.md`（本文件）
- 哈希基线：`pre-deliverables.sha256`、`pre-core.sha256`、`post-deliverables.sha256`、`post-core.sha256`
- 冻结：`freeze-baseline.log`、`freeze-baseline.json`、`freeze-diff.log`、`freeze-diff.json`、`freeze-full-adjudication2.txt`
- P8：`p8-compare.log`、`p8-compare.json`、`p8-core.json`、`p8-ed.json`、`p8-raw-lines.txt`、`p8-notes-stems.txt`、`p8-keydiff-detail.txt`
- 几何：`occlusion-selftest.log`、`occlusion-edition.json`、`occlusion-core.json`、`geometry.log`、`geometry.py`、`p1-band-detail.txt`、`p1-band-pixels.txt`、`crop-p1-band.png`
- gloss/P7/读者园地/家具/图片：`proof_checks.log`、`proof_checks-out.txt`、`proof_checks.py`、`gloss-rendered2.txt`、`furniture-images-detail.txt`、`w43-headers-model.txt`
- 登记表与复现：`registry_repro.log`、`registry_repro.py`、`registry-edition.json`、`registry-core.json`、`registry-edition-hashes.json`、`registry-core-hashes.json`、`transform-run-log.txt`、`abstract-pdf.txt`
- 构建员原始材料（对照用，未修改）：`hidden_files/weekly-report-w45-en-nl-build/`（build-log-r1–r4、occlusion-r2/r4、transform-log.txt）
