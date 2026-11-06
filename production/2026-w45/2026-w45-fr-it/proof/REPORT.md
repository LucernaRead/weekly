# 独立校对报告 — Lucerna Weekly W45 · FR × IT（法语 × 意大利语）

**结论：ZERO PROBLEMS**（阻塞项：无。可交付上架。下述 5 条为非阻塞观察，均为 KIT 文字表述精度问题或纸面之外的注释残留，纸面正确，不阻塞。）

**校对员纪律**：只校对，未派生任何下级代理，未碰 weekly-git，未改核心/W43/交付目录，未改 tools/ 下任何文件，未清理共享 scratch，未发 Discord，未往主聊天发卡片/PDF，未建 cron，未宣布上架（上架由协调员串行做）。所有重跑一律在自有 scratch（`hidden_files/w45/fr-it-proof/work/`）内进行：构建树与核心构建树均先完整拷贝到 scratch 并把 OUT 重定向到 scratch 输出目录，原构建树、交付目录与核心目录全程只读；门输出未截断，证据文件见文末。

## 0. 开工查重与冻结快照

- 开工时 `ps` 无任何以本版（fr-it）树为 cwd 的在途进程；唯一在途同类进程为 fr-pt 的 occlusion 审计，与本版无关。交付物最新 mtime 为 `WEEKLY-KIT.md` 2026-10-28 05:23 UTC（ABSTRACT 05:22、PDF 05:17），至开工时已静默逾 60–120 秒 → 安全开工，不 stand down。
- 校对前后哈希 diff：交付物（2 PDF + KIT + ABSTRACT + 8 SVG + 8 卡）与核心（2 PDF + 8 SVG）**内容哈希 diff 为空**（证据：`work/snapshot-before.txt` vs `work/snapshot-after.txt`；before 文件多含的 W43 一节仅为快照取法差异，非内容变化）。交付物 mtime 校对前后无刷新（SVG 仍为 2026-10-28 05:17 UTC），无须披露 mtime 刷新。

## 1. 交付指纹（独立重测，与建造员声称一致）

- 印刷 PDF `Le-Lucerna-VOL3-IT.pdf`：9,745,168 B，sha256 `f52d0d40c65391048ebd99c83bbc508c3dc3125b0745fee240d9c33abde5d832`，pypdf 8 页，1462.5×2025 pts。
- 网页 PDF `Le-Lucerna-VOL3-IT-web.pdf`：5,035,714 B，sha256 `ea4a3a66265e7af0d22a7ba92d8d429570cf3e913f6b1b4c13511bf14bffd002`，pypdf 8 页，936×1296 pts。
- 8 张卡均为 1950×2700 px；8 SVG 哈希与 KIT §15 逐项一致（p1 `96f28e71…`、p2 `1abec10f…`、p3 `f92f126a…`、p4 `e9d6dd8d…`、p5 `73dc4d2e…`、p6 `361df902…`、p7 `967acd16…`、p8 `b7901596…`，全值见快照文件）。
- 刊头：每页 `Le Lucerna`；VOL.3 全版一致；VOL.2 仅出现在 P7 延期披露句中（正当引用核心句，非残留）；VOL.4 出现处均为下期正向引用（P7 披露+预告、P8 写作条+答案 150）。

## 2. 门 1 — 冻结与法语核对串：通过

- **核心基线自有 scratch 重跑**：`tools/freeze.py baseline` 对核心构建树拷贝重跑，**8/8 逐字节一致**（p1 f02e628e…、p2 b192c192…、p3 5f332e9f…、p4 240f379d…、p5 a4d64e3e…、p6 47e4346d…、p7 e997123f…、p8 822dbe3d…），且 freeze 自检“shipped core SVGs unchanged”。核心基线未动。
- **新增 CJK**：`freeze.py diff` 逐页：核心 CJK 总量 202/244/179/197/177/198/390/1030（P1–P8）→ 分版 **0**，**新增 CJK 8 页均为 0**。自有 Han 范围（U+4E00–U+9FFF）扫描交叉验证：分版 8 页 Han 均为 0，全角括号 8 页均为 0；核心 Han 为 192/219/156/171/159/170/328/788（两种口径的核心总量不同源于 CJK 统计范围，分版侧均为 0，结论一致）。
- **源码字面级冻结（自有 AST 提取，content 文件口径）**：核心字面 1329 个，其中不含汉字者去重后 **541 个**，分版源码中缺失**恰 6 个**，与 KIT 所列一一对应，逐项原因如下（分版源码汉字字面：0 个）：
  1. `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg`（content12.py:7）——核心输出路径字面，构建路径，非内容。
  2. `s'intéresser aux（à+les）`（content8.py:48）——全角括号改半角；印刷行实测分版 P8 (989, 2260.21)：`(s'intéresser aux (à + les))`。
  3. `Traduisez : « Lire un programme, c'est déjà comprendre la France. »`（content8.py:92）——E1 改向；法语句逐字保留在新题干内（分版 content8.py:92 全句 `Traduci in italiano: « Lire un programme, c'est déjà comprendre la France. »`；印刷题干首行 P8 (989, 1332)）。
  4. `（`、5. `）`（content8.py:154）——同第 2 项的全角→半角转换。
  6. `type`（content8.py:153）——核心 `e["type"]` 注释集规则键；分版改用显式 `PRINT_NOTES` 集合（content8.py:148，97 项，与 p8 提取 noted 集逐项相等，见门 2），非印刷文本。
  - 附注：若把口径扩大到 content+bslib，缺失仍为 6 项但第 6 项变为 bslib 的 f-string 切分片段（`'" preserveAspectRatio=…`），属 AST 对 f-string 分段的口径 artefact；两版 bslib 的 `image()` 源码行逐字相同且三张图片 payload 逐字节相等（门 10），对纸面无任何影响。故以 content 口径的 6 项为准。
- **P8 注汉字**：分版 P8 答案区（y>1600 且 <2580）文本 Han = **0**（核心同区为 678，系中文注释）；全版汉字 0（上文）。
- **法语冻结串逐项核对（全部从核心 SVG 与分版 SVG 逐项核对，核心 SVG 为准）**：
  - P4 `41e édition en 2026 (40e anniversaire)`：分版与核心**同为 1 处**，节点**逐字节同坐标同文本**：P4 (1473, 278)，21.5pt，节点文本 `41e édition en 2026 (40e`（续行 `anniversaire)`）。全版 `40e` 出现：分版与核心**各仅此 1 处**（joined 文本计数均为 1）。`22e édition`：分版与核心各 1 处（P1）；`15e édition`：各 2 处（P5，含题干与答案各 1）；习题号 `40.`/`140–144.` 未动（编号连续性见门 4）。
  - Q120：题干分版与核心**同坐标** P8 (527, 246)，20pt：`Si j'étais libre dimanche, j'___ à Nanterre. A.`；选项行同坐标 (527, 275)：`irai · B. irais · C. vais`；REG 键均为 **B**（分版与核心逐题相等，见门 4）；P8 注同步：分版 (989, 2260.21/2279.06) `120. B (si + imparfait → conditionnel présent; j' è je davanti a vocale (elisione))`，对应核心注 `si + imparfait → conditionnel présent; j' 是 je 在元音前的省音` 的意大利语化，语法点（si + imparfait → conditionnel + elision j'）齐全。邻题 Q119（`Elle s'intéresse ___ festivals.`，键 B）与 Q121（`À mon avis, ce programme ___ très riche.`，键 A）题干与键均与核心一致（REG 逐题相等；Q119 注仅括号半角化，Q121 注意大利语化）。
  - P7 引用 #4：分版 P7 表内 (527, 1443.85/1474.65/1505.45) `« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » (page 4)`；P4 辩论框原文 (1473, 2356.40/2384.40/2412.40) `Finalisti sconosciuti in anticipo: più emozionante o più frustrante? …` 之上的法语辩论句与核心 P4 辩论框逐字相同（joined 计数：分版与核心在 P4 各 1、P7 各 4，合计 5）；B1 教学栏同步出现该 comparatif（P7 (527, 613.2) 等）；P8 答案键相关项 Q100 键 `plus excitante` 未动。
  - #8：分版 P7 表内 (1451, 1330.9/1361.7) `« Les jeunes créateurs y rencontrent leur public, en vrai. » (page 5)`；P5 原文同句 joined 计数分版与核心各 1；Q106 改写实测：P7 诊所 (65, 2203.2/2235.825) `✗ « Les jeunes créateurs y rencontre leur public, en vrai. »`（error `rencontre`），P8 答案键 `rencontrent`（REG Q106 键与核心逐字相等，注为意大利语语法说明）。
  - P6 同步：`Ce calendrier peut encore bouger.` 分版与核心 joined 计数各 3（P6 框内 (1007, 658.88) `« Ce calendrier peut encore bouger. »` + P7 两处）；P6 深读小写形与微习题键 `peut`（Q95）未动（REG 逐题相等）。
  - **结论：任一法语串与核心不符即冻结失败——本版无此情形。门 1 通过。**

## 3. 门 2 — P8 双门（FR 族硬性，缺一不可）：通过

- 门 ① plain `tools/p8.py`（当前新版，实测 sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`，与 KIT 注明一致；`--total 150`）：核心 noted **97**，分版 noted **97**，状态 **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]。noted 集两侧逐项相等：[1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109–150]；分版 `content8.py:148` 的 `PRINT_NOTES` 显式集合与 p8 提取 noted 集**逐项相等**（另经 REG 核对，见门 4）。
- 门 ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（全 150 键，`--total 150`，以 p8.py extract --json 为输入）：两侧各 150 键，mismatch **仅 [135, 150]**（keycompare 退出码 1 系“存在 mismatch 即非零”的工具语义，非门失败；门条件为 mismatch ⊆ 已备案 noted 改向且裸键 mismatch 为 0）：
  - #135（两侧均为 noted）：核心键 `读一份日程，本身就是在了解法国。` → 分版键 `Leggere un programma è già capire la Francia.`；印刷行分版 P8 (1451, 1874.5) 起：`135. Leggere un programma è già capire la Francia. (lire un programme = leggere un programma)`；题干改向为法→意（见门 1 第 3 项），已备案。
  - #150（两侧均为 noted）：核心键 `开放题 — 要点见写作框，范文在第 8 版写作框内` → 分版键 `Domanda aperta — i punti sono nel riquadro di scrittura e il modello è nel riquadro MODÈLE di questa pagina`；印刷行分版 P8 (1451, 2138.4) 起，注 `(si valuta in base ai punti)`；p8 提取将破折号后截断为 `Domanda aperta`/`开放题`，但 mismatch 集与裸键结论不受影响。
  - **裸键 mismatch = 0**（53 个裸键全部逐字相等）。
- E2–E5 逐项从印刷行核实（题干意大利语化，法语键不变）：#136 题干 `Traduci in francese: Corre più veloce di suo fratello.`（P8 (1451, 246)），键 `Il court plus vite que son frère.`；#137 `Gli studenti sono in vacanza dal 17 ottobre.`（(1451, 362)），键不变；#138 `Stasera prepariamo le cartelle.`（(1451, 478)），键不变；#139 `Non si conoscono ancora i finalisti.`（(1451, 594)），键不变。非照抄 fr-de/fr-en/fr-es（各版题干语言与项号均不同，本版为意大利语题干 + #135/#150）。
- **通过条件满足：plain ∈ {CLEAN} 且零裸键 mismatch。门 2 通过。**

## 4. 门 3 — gloss：通过（口径与方法分项报告，不混算）

- 方法（自有 AST 计数器，tools/README #21 口径）：gloss() 调用串按 `·` 本身切分（非 ` · `）；Nota 类桥接串先去前缀再切分（分版 `Nota — `、核心 `译注｜`，否则 P2/P4/P6 各多计 1 项假象）；词表项为 mots/mots4/mots5 列表长度；页归属按文件内 `CURPAGE[0] = N` 顺序追踪。另做渲染存活核对：分版 6 个 gloss() 调用串与全部 Nota 桥接串在渲染后 joined 文本中**全部找回（缺失 0）**。
- 实测（核心 = 分版，逐页相等）：

  | 页 | gloss() 项 | Nota 桥接项 | 词表项 |
  |---|---|---|---|
  | P1 | 7 | 0 | 0 |
  | P2 | 6 | 3 | 0 |
  | P3 | 6 | 0 | 10 |
  | P4 | 7 | 3 | 8 |
  | P5 | 6 | 0 | 8 |
  | P6 | 6 | 3 | 0 |
  | P7 | 0 | 0 | 0 |
  | P8 | 0 | 0 | 0 |
  | 合计 | **38** | **9** | **26** |

  与建造员声称 gloss 38（7/6/6/7/6/6）+ Nota 桥接 9（P2/P4/P6 各 3）+ 词表 26 逐项一致，三项分开计数、未混算。
- P8 注纯意大利语：分版 P8 答案区 Han 0、全角括号 0；德语跨族残留探针（Schulbeginn / Jakobsmuschel / Nachtveranstaltung / Übersetzen Sie / Übersetzung / Schul / Lesen Sie / Woche / Montagmorgen）全版均为 **0 命中**；REG 中 PRINT_NOTES 的 97 条印刷注+键 Han 均为 0（法语原文、键与术语引用除外，属正常引用）。
- P7 词框定义句冻结：content7.py 的核心字面在分版源码中**缺失 0 项**（门 1 的 6 项缺失中无 content7 项）；P7 教学区法语句节点与核心同文本（仅栏头与 gloss/语法说明本地化为意大利语，坐标因意大利语行拉长而下移，属重排非改写）。

## 5. 门 4 — 金句、P7 短语、登记、范文：通过

- **金句 8 句（联合文本计数，分版 = 核心）**：#1 `Le lundi 2 novembre, on reprend les cours.` = **5**（P2 1 + P7 4）；#2 `On ne connaît pas encore les finalistes.` = **3**（P7 2 + P8 1）；#3 `Les cimetières se sont remplis de chrysanthèmes.` = **1**（P7 1）；#4 `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?` = **5**（P4 1 + P7 4）；#5 `Le festival se promène dans Paris.` = **1**（P7 1）；#6 `Ce calendrier peut encore bouger.` = **3**（P6 1 + P7 2）；#7 `Ce week-end, tout se joue.` = **1**（P7 1）；#8 `Les jeunes créateurs y rencontrent leur public, en vrai.` = **3**（P5 1 + P7 1 + P8 1）。与建造员声称逐项一致。
- **P7 短语表（印刷表实际内容）**：8 句在分版 P7 表内均带正确页签：#1 (page 2)、#2 (page 1)、#3 (page 3)、#4 (page 4)、#5 (page 5)、#6 (page 6)、#7 (page 1)、#8 (page 5)（#8 表内 (1451, 1330.9/1361.7) `« Les jeunes créateurs y rencontrent leur public, en vrai. » (page 5)`）。出处页核实（诚实口径）：8 句的词序内容均出自所标页正文；其中 #2/#3/#5/#7 在正文中的标点形态为破折号/冒号/标题片段（如 P1 `on ne connaît pas encore les finalistes — ils…`、P3 `…remplis de chrysanthèmes —`、P5 `…se promène dans Paris :`、P1 LE MOT 框 `Ce week-end, tout se joue : les finales…`），P7 表将其规范为句号——**该规范化是核心原文即有的做法，分版与核心表述逐字相同**，非分版新增改写。P7 “2×” = 源文章 + P7 表格对（教学栏/工具箱重复 #1/#2/#4/#6 为 KIT 设计，非缺陷）。
- **登记（自有 scratch 拷树重跑，OUT 已重定向，单进程 content12→34→56→7→8）**：核心与分版 REG 均为 **150 题连续（1–150）**；页分布两侧逐项相等 **10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P2=15、P5=17、P8=42，FR 串）；级别两侧逐项相等 **A2 53 / B1 75 / B2 22**；逐题 page/level 150/150 相等；题型数量 1:1 本地化（Completamento 49 · Scelta multipla 26 · Abbinamento 21 · Completamento testo 8 · Trasformazione 7 · Lettura dati 6 · Vero/Falso 5 · Comprensione 5 · Traduzione 5 · Completamento dialogo 5 · Esercizio guidato 8 · Correzione errori 4 · Scrittura 1，对应核心的 完成句子 49 / 单选 26 / 词汇配对 21 / 完形填空 8 / 句型转换 7 / 图表读数 6 / 阅读判断 5 / 阅读理解 5 / 翻译 5 / 对话补全 5 / 跟练 8 / 改错 4 / 写作 1）；REG 键仅 #135/#150 不同（即门 2 两改向项），余 148 项键逐字相等；Q119/Q120/Q121 键分别为 B/B/A，两侧一致。
- **范文 86 词实测**：分版与核心 P8 MODÈLE 框正文（右栏，MODÈLE 栏头 1538 至 RÉPONSES 栏头 1838 之间）逐字相等，**均为 86 词**（`Samedi 7 novembre, j'ai regardé les demi-finales du Masters… C'était un week-end parfait.`）；仅栏头行改为双语 `MODÈLE · MODELLO`（核心为 `MODÈLE · 范文`）。

## 6. 门 5 — 几何：通过

- canonical `tools/occlusion_audit.py`（venv，先自检）：自检 6 类 planted 全部命中、干净对照静默；**分版 0 flags，核心 0 flags，NEW vs 核心 0**（证据：`work/occl-ed.json`、`occl-core.json`、`occl-ed-vs-core.json`）。round-1→round-2 差异范围核对：建造树 `occlusion-r1.json` 确为 11 项 NEW 旗（含 P1 溢出、P2 ET VOUS 溢出、P7 披露 COVER、P8 LINEX 等，与 KIT 所述 round-1 情形一致），round-2 自有重跑 0 旗——修复轮范围与基线一致，无新增旗标。
- 全页右缘 ADVANCE 扫描（自有 PIL  advance 法，限 1885）：分版**仅 3 项**超限，全部为 P8 F 配对右侧行，最大 x1=**1899.5**，仍在内框线 1910 以内：P8 (y=1036.0, x1=1891.2) `b. une soirée qui dure jusqu'à la nuit`、(y=1112.0, x1=1891.3) `d. le coquillage fêté à Port-en-Bessin`、(y=1150.0, x1=1899.5) `e. plusieurs concerts en une semaine`；核心同文三行文本与 x1 **逐值相同**（核心 y=940/1016/1054，y 坐标因 P8 14.5pt 重排下移 +96，属冻结法语重排继承，非分版缺陷；意大利语自有超限项 0）。
- 框线扫描：**0 命中**（右框线 1910/1922 阈值法）；同基线行检查（P1 顶栏 y=92、徽记 y=574、各页页脚 y=2624）：**0 重叠**；P6 图表标签基线锚定墨迹覆盖（getmetrics 法，禁用 getbbox）：分版与核心均为 **0.0%**（<30% 通过）。
- 行首 `:`：分版 4 项，与核心**同页同坐标同文本逐字节相同**：P3 (1451, 789.65) `: on le pose sur les tombes, on ne l'offre jamais`、P4 (65, 837.12) `: quarts de finale vendredi 6`、P5 (1473, 430.65) `: clôture du festival.`、P7 (527, 428.1) `: attention à l'accord avec le sujet :`；意大利语自有行首违规 **0**。
- 行中切词扫描：全版无拉丁连字符行末切词（行末为 `-` 的节点数为 0）；行末 en-dash 列表换行**仅 4 处**，文本与核心逐项相同（P4 (527, 864.22) `A. Paris SG – Troyes · B. Lens –`、(527, 2173.69) `vendredi 6 novembre avec Toulouse –`、(527, 2316.57) `Dimanche 8, six matchs : Rennes –`、(527, 2352.29) `Lille, Le Mans – Monaco, Le Havre –`；核心同文 y=805.0/2114.47/2257.35/2293.07，y 整体 +59.22 系 P4 重排所致）——均为球队/赛程列表的 en-dash 分隔换行，下一行续列表项，非单词连字符切词。
- 流末端（光标口径，scratch 重跑日志，分版 vs 核心）：P1 headline 1537（核心 1588）、hiver 2298（核心同值，距 quiz 规则线 2312 仅 14px，继承）、quiz 2521（核心同值）；P2 feature 606、习题 2365；P3 正文 813；P4 正文 1174、微习题 2154；P5 正文 2502（核心同值）；P6 深读 1019（核心 989）、习题 2557（核心同值，距页脚规则线 2580 有 23px，核心继承紧贴值）、观点栏 1255（核心 1225，距图表顶 1330 有 75px）、微习题 2020（核心 1990）；P7 A2 954、B1 1053、B2 988、工具箱 1008（核心 949，限 1150 内）、短语栏 1574（核心 1449，限 1830 内）、诊所 2140（限 2268 内）。P5 栏结构说明见非阻塞观察 O1。

## 7. 门 6 — P8 流末端口径裁决（重点）：通过（依据如下，不以 fr-de 前例了事）

### 7.1 三值逐项对照（同口径实测）

| 口径 | 分版 | 核心 | 差 |
|---|---|---|---|
| battery 流光标（Flow end_report，限 1485） | 1487 | 1410 | +77 |
| battery 末墨迹基线 | 1446.4（P8 (1451, 1446.4) `Merci !`） | 1455.825 | −9.425（分版反而更短） |
| battery 墨迹底：canonical 真墨迹盒 / 保守 em 带 | 1446.7 / 约 1451.6 | 1456.1 / — | 距写作条规则线 1486：真墨迹 39.3px、保守带 34.4px |
| keys 流光标（Flow end_report，限 2545） | 2204 | 2167 | +37 |
| keys 最大基线（答案行） | 2542.96（col 989，P8 组尾行 `me) · 134. Il est prévu que le Sénat examine le texte lundi. (il est`） | 2539.19（col 65，P4 组尾行 `44. B … · 45. A · 46. C · 47. B · 48. A ·`） | +3.77（跨列比较，见 7.2） |
| keys 最大基线（全部节点，含分隔栏头） | 2544.03（col 65，分隔栏头 `— PAGINA 4 —`，17pt bold） | 2539.19（同答案行最大值） | +4.84 |
| keys 墨迹底：canonical 真墨迹盒 / 建造员保守值 | 2546.2（答案行，含 p/q 下伸笔画）/ 约 2548.1 | 2541.2 / 约 2544.4 | 距页脚规则线 2580：真墨迹 33.8px、保守值 31.9px |
| FOOTER 旗标（canonical 审计，规则线 2580） | 0 | 0 | — |

注：建造员 KIT 所述“最大基线 2542.96”仅计答案行，未计 17pt 分隔栏头 2544.03，低估全部节点最大值 1.07px；建造员墨迹底约 2548.1 为保守口径（约等于基线 + em 带），高于本校对 canonical 真墨迹盒 2546.2。两种口径下距 2580 的间隙分别为 31.9px 与 33.8px，结论不变（见非阻塞观察 O2）。

### 7.2 +3.77px 的来源（按列分解，非单一题）

keys 流 4 列（x=65/527/989/1451）最大基线对照：col 65：分版 2544.03（分隔栏头）vs 核心 2539.19（+4.84）；col 527：分版 2521.12 vs 核心 2537.73（−16.61）；col 989：分版 2542.96 vs 核心 2526.11（**+16.85**）；col 1451（末列，P8 组溢流尾）：分版 2176.1 vs 核心 2137.45（+38.65）。因此全局答案最大值 +3.77 是**两列不同组尾填充水平的差**（分版的 P8 组列 989 vs 核心的 P4 组列 65），不是某一题的单点下跳。内容增长的直接证据（REG 实测）：P8 组（109–150）印刷注总字符分版 **1377** vs 核心 **740**（+637，+86%），键总字符 628 vs 517（+111），字号 14.5pt vs 15.5pt 的缩小未能抵消注长增长，致 keys 流整体拉长（光标 2204 vs 2167，+37），P8 组列 989 填得更深；尾行 133–134 的意大利语注（如 134 注 `il est prévu que + congiuntivo`）即为该列尾部的增长载体之一，而非孤立溢出项。

### 7.3 裁决

**过门，依据（按重要性排序）**：(a) keys 流自身的声明底限为 **2545**（content8.py `Flow(..., 2545, tag="P8-keys")`），全部节点最大基线 2544.03 < 2545，答案行 2542.96 亦然——名义 2540 是通用 CONTENT_BOTTOM 默认值，不是 keys 流的限值；(b) 页脚规则线为 **2580**，canonical 审计 FOOTER **0 旗**，真墨迹底距规则线 33.8px（保守口径 31.9px），无压线、无墨迹触线；(c) 增长确为内容增长（意大利语注 +86%）导致的合规下移，且分版 battery 墨迹反而短于核心，排除系统性下沉。fr-de 前例（本版与核心同值、超限仅 1–3px）与本案不同，**本裁决不依赖该前例**，仅依赖上述限值与间隙事实。若任一事实为反（超 2545 流限、或墨迹触 2580、或 FOOTER 有旗），即应为阻塞项——实测三者皆无。

## 8. 门 7 — P7 几何与 P4 跨栏：通过

- P7 预告：末基线 **2494.0**（P7 (1013, 2494.0) `fiera di Dieppe — e le vostre lettere!`，意大利语预告末行），canonical 真墨迹底 **2498.5**（建造员称约 2499，差 0.5px 属方法舍入），距名义限 2540 有 **41.5px**；核心预告末基线 2466.0、墨迹底 2469.5（中文预告行），分版 +28 系意大利语预告行拉长所致，仍在限内。P7 除页脚（2624）外无更高基线。
- P4 `giusta.` 跨栏换行：分版节点 **(527, 220.5)，20.5pt，sans，fill #57523f**，与已上架 fr-de 交付物同处节点 **(527, 220.5)，20.5pt，sans，fill #57523f，文本 `Sie die richtige Antwort.`** 逐项同坐标同规格；机制同构：À VOUS 桥接句首行分版 P4 (65, 2524.47) `Leggi l'articolo di pagina 4 e scegli la risposta` 将 col0 填至底限，尾词 `giusta.` 溢至下一栏（col1）顶（首基线 = 流顶 200 + 20.5 = 220.5）；fr-de 同机制（德语尾句同坐标）；邻节点亦同坐标（P4 标题 (65, 237.0)、下题 (527, 315.225)）。**属家族行为（Flow 跨栏换行），非缺陷，接受该裁决。**

## 9. 门 8 — 读者来信角：通过

逐字摘录（分版 P7，x=1013 栏）：
- 法语标注示例（3 行，1956.0/1985.82/2015.64，21pt）：`« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`——与核心逐字相同，明确标注非读者来信，零编造。
- 意大利语示例点评（2 行，2066.0/2094.0，20pt，KIT 未单列但属同一角）：`Xiao Mo commenta (testo di esempio): il passé composé è solido per raccontare il fine settimana; il punto e virgola unisce i due giorni. Nel VOL.4 commenteremo testi veri.`——再次明示为示例文本。
- 法语披露（2 行，2142.0/2170.0，20pt，核心逐字保留）：`Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.`
- 意大利语披露（2 行，2206.0/2233.3，19.5pt）：`Nota della redazione: ancora nessuna lettera vera né migliori testi (W44 non uscito); è un esempio. Nel VOL.4 i veri! Mandateci lettere e migliori testi!`
- **三事实齐全**：(1) 暂无真实来信（`ancora nessuna lettera vera`）；(2) 暂无最佳 P8 作文（`né migliori testi`）；(3) 均延至 VOL.4（`Nel VOL.4 i veri!` + 法语 `Le VOL.4 reprendra la promesse.` + P8 写作条 `I migliori testi appariranno nel VOL.4 (pagina 7, « Le courrier des lecteurs »)` 与答案 150 行指向同一页）。
- **征集句裁决**：`Mandateci lettere e migliori testi!` 字面同时覆盖两项——`lettere`（来信）+ `migliori testi`（最佳文本，即最佳 P8 作文）——为同一祈使句内的并列宾语，满足“同时覆盖来信与最佳 P8 文本”的字面要求。预告行 `Et vos lettres, enfin !` / `e le vostre lettere!` **不计作征集**（按任务规则排除），本裁决不依赖预告行。

## 10. 门 9 — 家具三方对照（核心 / W43 / 本版）：通过

- 徽章串：本版与 W43 **逐字节相同**：P1 (975, 574)，22pt，bold，BRICK #a4553a，居中，`TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`；与 README #20 的 FR-as-target 一般形（y=574、22pt BRICK）一致，无冲突。
- 副标槽：P1 顶栏 y=92 三段——左 `VOL. 3 · N. 3`（W43：`VOL. 2 · N. 2`）、中 `HEBDOMADAIRE EN FRANÇAIS · OGNI SETTIMANA · IL FRANCESE CHE LEGGONO I FRANCESI`（与 W43 逐字相同）、右 `SEMAINE DU 2 AU 8 NOVEMBRE 2026`（W43：19–25 OCTOBRE 2026）；左右两段仅为期号/刊期更新。
- 刊名 262（178pt）`Le Lucerna`、副标题 330（46pt）`SETTIMANALE IN FRANCESE · VOL.3 · WEEKEND DELLE FINALI`（W43：VOL.2 · AUTUNNO E FESTE；实测 advance 宽 1498.45px ≈ KIT 1498.5px）、标语 372 法语原文与 W43 相同。
- 暗带：rect (65, 424, 1820×118, #2c2822) 与 W43 **逐值相同**；暗带文本 y=478/522 为本周内容（法语头条 + 意大利语右侧短语 `LUNEDÌ SI TORNA A SCUOLA · TUTTA LA FRANCIA` / `INIZIANO IL MASTERS E IL FESTIVAL · VEDI PAGINA 2`），属刊期内容更新。
- 规则线：页脚规则线 y=2580（65→1885，金色 1.6）在位；页脚每页 y=2624：`Le Lucerna · SETTIMANALE FRANCESE VOL.3 · TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO` + `Pagina N di 8`，为 W43 模板、VOL 号更新（8 页逐页核实）。
- 短双语栏头、gloss 前缀 `Nota — `、P8 分隔 `— PAGINA {n} —`、P8 栏头（COMPLETA / OPZIONI / LETTURA / COSTRUISCI FRASI / TRADUZIONE / VOCABOLARIO / DIALOGO / SCRITTURA / MODELLO）、keys 头 `RÉPONSES · TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)` 均与 W43 同式（VOL 号与刊期除外）。

## 11. 门 10 — 图片 payload = 核心：通过

| 页 | 图 | 放置（x, y, w×h） | base64 文本 sha256（全值） | 解码 JPEG sha256（全值） | 字节 |
|---|---|---|---|---|---|
| P1 | atget-paris.jpg | 65, 1874, 896×320 | `ff20bc2bd2654cdc075f7e09bcb5a96622650c7cb5921fe07384703067fa8e5d` | `f3705af28f175ce48d8abad95944accb7aacc45d6a8a50c47b24af5c5144595f` | 334674 |
| P2 | hiroshige-maple.jpg | 1451, 200, 434×480 | `6918cb8bbe4b4bec2d6dd9bafb1636901ed2a46f9df8e49566749e404d1664ae` | `5b772facb5db886c18fa96c05b9c8fb1a459eaaff931a4a8c121896edf970ee2` | 646242 |
| P3 | chrysanthemum-blanco.jpg | 1451, 200, 434×540 | `bfaadf5b6b912416f770c1bf579c3467e47c662efd130b5656292bb86171eca9` | `be071fdae81a71b48d76383bd33147371968f44e37eef4312102d52dea6d0c94` | 142340 |

三张图分版与核心在两种口径下哈希**全部逐字节相等**，放置坐标与核心逐值相同，解码字节数与资产文件一致。credit 行 Artist 原文且确已放置，坐标与核心逐值相同：P1 (65, 2271.3) `Eugène Atget (1857-1927), photographie, domaine public`；P2 (1451, 757.3) `Utagawa Hiroshige (1797-1858), estampe, domaine public ·` + (1451, 777.45) `LACMA`；P3 (1451, 842.95/863.10) `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public`。

## 12. 门 11 — 网页版 PDF（从本版卡片新鲜生成）：通过（无噪声页）

- **卡片 = SVG 渲染**：自有 scratch 用 cairosvg @1950 重渲染 8 页 SVG，与交付卡片 **8/8 逐字节相同**——卡片确为本版 SVG 的渲染，非他版混入。
- **网页流 = 卡片编码（决定性证据）**：自有 scratch 用建造配方（卡片 → JPEG q72 optimize → Pillow save resolution=150）重建网页 PDF，提取的 8 页 JPEG 流与交付网页 PDF 的 8 页 JPEG 流**逐字节相同**（见下表；fr-es 前例方法）。交付网页 PDF 全文件 5,035,714 B vs 重建 5,035,692 B，相差 22 B 仅为 PDF 容器/元数据差异，图像流本身相同——质量参数的门是“流 = 卡片编码”，该门通过。

  | 页 | 交付流 sha256（全值） | 字节 | 重建流是否相同 |
  |---|---|---|---|
  | 1 | `d11b03872e67071363dd718984c0901ab80d67a67613e372c6b072cd924c35dd` | 648707 | 是 |
  | 2 | `aa1d49837f26252312c1c9bbb63f75c46200d4998cbf58266723548efcbd60b8` | 625517 | 是 |
  | 3 | `e210e810028810b8c15dd5550af403afe2ebe0fa13a724418507c8c1bf5314e9` | 578873 | 是 |
  | 4 | `4cb0147017de1523523e345d1d65972e182e9154666ab570ea5ce708670519a6` | 621872 | 是 |
  | 5 | `ee20acf76af917ef10d83a8fde28d62a1de2062ff24c085c4b4762fb43d5c853` | 525905 | 是 |
  | 6 | `42c740a9cc7f7d7974b19a530e2ae9e9a144bd967592e62235ca4fa2a1a615f9` | 555523 | 是 |
  | 7 | `057ba0b0c0b2b1bef5f3884b41dd76ba704d07a3a2441b053448891e3ccebd1f` | 638906 | 是 |
  | 8 | `2153d7a451caebba7c50cd567e14fb6ec420efcbdc567c7efffc227a5bbf356e` | 820221 | 是 |

- **逐页像素比对（交付 JPEG 解码 vs 交付卡片，同尺寸 1950×2700，PIL 差分均值）**：全幅均值差 P1–P8 为 3.298 / 3.267 / 2.997 / 3.275 / 2.773 / 2.960 / 3.344 / 4.549；4× 降采样结构比对均值差为 1.252 / 1.235 / 1.155 / 1.205 / 1.124 / 1.186 / 1.264 / 1.367。**无离群页**（最高为 P8，系文字最密页的正常 JPEG 痕迹；降采样后全部 ≤1.37，结构一致）。建造员声称的全幅 4.6–8.4 / 降采样 1.8–2.8 在本校对方法下未复现出相同绝对值（本方法解码尺寸与参考不同），但“JPEG q72 痕迹、无异常页”的结论在更严格的流同一性证据下成立（见观察 O3）。
- **q72/q75 实测结论**：交付流与 q72 配方重建流逐字节相同，证实交付流即 q72 卡片编码；q75 配方不会产生相同流（未用作交付）。质量参数本身不阻塞，流同一性才是门——已通过。fr-en 噪声教训不适用于本版：网页版确从本版卡片新鲜生成，8 页逐页比对无噪声。

## 13. 门 12 — ABSTRACT：通过

- 意大利语单行：1 行（含末尾换行），492 字符，ASCII 双引号 **0** 个。全文：`Le Lucerna VOL.3, settimana dal 2 all'8 novembre 2026: settimanale in francese per lettori italiani — weekend delle finali con il Rolex Paris Masters a Nanterre, Peur sur le Parc a Plailly e Le Goût du Large a Port-en-Bessin, ritorno a scuola il 2 novembre, Halloween e Ognissanti, Pitchfork Paris e il bilancio 2027 all'Assemblea nazionale, con 150 esercizi da A2 a B2, lessico, grammatica e modello di testo. Imparare il francese leggendo notizie vere: finali, ora solare e feste francesi.`
- 关键词逐词在刊内出处（分版 joined 文本计数）：Rolex Paris Masters 2、Nanterre 10、Peur sur le Parc 5、Plailly 11、Le Goût du Large 3、Port-en-Bessin 14、2 novembre 23、Halloween 13、Ognissanti 2、Pitchfork Paris 2、Assemblea nazionale 1、bilancio 8、2027 4；11 月 2 日开学对应 `Lundi 2 novembre, on reprend les cours.`（P2 正文）+ 意大利语 `Si torna a scuola lunedì 2 novembre`（P2 注）+ 栏头 `RITORNO A SCUOLA`。
- 诚实口径说明两点：(a) 摘要中 `il bilancio 2027` 的相邻意大利语短语在刊内为 0——刊内意大利语用 `bilancio`（8×）与年份分开出现，法语正文用 `budget 2027`（3×）；按任务“逐词找出处”口径，`bilancio` 与 `2027` 均有出处，主题非编造；(b) 摘要收尾学习者短语 `Imparare il francese leggendo notizie vere: finali, ora solare e feste francesi.` 中的 `ora solare`：刊内印刷文本无此短语，但冬令时主题在刊内真实存在（法语 `L'heure d'hiver…` 习题与 P1 `DEUXIÈME SEMAINE D'HIVER` 栏；REG 注 `L'ora solare è in vigore dal 25 ottobre` 为该习题的登记注，未印刷于 P8 答案区，属登记层主题词）。两点均不构成编造主题，门 12 通过。

## 14. 门 13 — transform 单独复现（ko-ru 教训）：通过

- 自有 scratch 内：全新核心构建树拷贝 + 建造树 `transform.py`（仅此一文件拷入）运行，替换数 **358**（主 339 + 修复轮 19；transform-log 358 行），随后 OUT 重定向到 scratch 并单进程重跑：产出 SVG 与已交付纸面 **8/8 逐字节一致**，REG 与分版构建树重跑 REG **逐项相同（150/150）**。差异恰为 0——不存在“复现不能还原纸面”的情形，无 ko-ru B-1 同类问题。
- 交叉验证：分版构建树本身在 scratch 重跑亦 8/8 逐字节复现交付 SVG；核心构建树重跑 8/8 逐字节复现核心 SVG（门 1）。round-2 零渲染改动亦得证：建造树 `pre-fix-hashes-r2.txt` 的 18 项（8 SVG + 8 卡 + 2 PDF）哈希与交付文件逐项相等。

## 15. 门 14 — 核心事实债与新增主张：通过

- 核心事实债只继承、不判本版阻塞：本周主题、日期、赛程、预算周日程、P6 习题末 2557（核心同值）、P1 hiver 末 2298（核心同值）、金句标点规范化（门 5 所述核心做法）等，均继承核心原文，分版未改写。
- 本版新增主张 **0**：除本地化（意大利语讲解、栏头、注）与已备案的 P8 两改向外，无新增事实陈述；W43 偏差清单（KIT §12）逐项核实均为呈现/本地化类：VOL/刊期/副标题/暗带短语为刊期更新；P8 答案 14.5pt（W43 keys para 实测 15.5pt）与 battery  prose 20pt（核心 21pt，实测 content8.py:29/60/126）+ 间距 6（核心默认 11/14）为注长适配；P1 头条 24pt/1.45（核心 25pt/1.52，实测 content12.py:40–44）仅呈现变化、法语文本字节不变；P1 gloss 单字化、P2 ET VOUS 2 行定稿、P2 日期注、栏头缩短、P3 词表项缩短均为框界适配；读者角示例+披露继承核心诚实处理，新增征集句为 SOP 门禁要求（非事实主张）；翻译改向方法同 W43 先例、项号不同（本版 #135/#150，W43 为 #132/#145）。

## 16. 非阻塞观察（纸面正确，不阻塞；与 fr-de 校对报告的惯例一致，单列于此）

- **O1 — KIT §5/§17 的 P5 表述不精确**：KIT 称“P5 正文第 2 栏溢至第 3 栏顶部”。实测：分版与核心 P5 的栏 x 值集合完全相同（65/527/1473 栏，无 989 栏节点），P5-main 流（3 栏定义）在两版重跑中均止于 col 1/2、y=2502，#78 位置两侧同为 (599, 2388.6)。即本版 P5 不存在第 3 栏（989）溢流节点；该句疑为他版情形的沿用。纸面 = 核心结构 + occlusion 0 旗，故不阻塞，仅 KIT 文字需订正。
- **O2 — KIT P8 最大基线表述低估 1.07px**：KIT §5/§17 的 2542.96 仅计答案行，未计分隔栏头 2544.03（门 7.1）；墨迹底约 2548.1 为保守口径，高于 canonical 真墨迹盒 2546.2。两种口径距 2580 均逾 31px，裁决不变，仅数值精度需订正。
- **O3 — KIT 网页像素差绝对值未复现**：KIT 称全幅 4.6–8.4 / 降采样 1.8–2.8；本校对同尺寸 PIL 差分法实测为 2.773–4.549 / 1.124–1.367（绝对值更低）。差异源于比对方法（解码尺寸/参考不同），且流同一性（8/8 逐字节）已决定性证明网页版即卡片编码，故不影响结论。
- **O4 — 构建树注释残留（纸面外）**：建造树 `render.py` 首行注释称“Render W45 FR x DE”，但其 ED 指向的实为 fr-it 目录，渲染结果亦确为 fr-it（卡片/SVG 8/8 一致）；属陈旧注释，非纸面问题。
- **O5 — P7 读者角另有一行意大利语示例点评**（门 9 已摘录，`Xiao Mo commenta (testo di esempio)…`）：KIT §8 未单列该行，但该行明示为示例且指向 VOL.4 评论真文本，与披露口径一致，非编造，不阻塞。

## 17. 证据索引（全部位于校对目录 work/ 下，原交付/核心/构建树未动）

- `work/snapshot-before.txt`、`work/snapshot-after.txt`（校对前后哈希快照，内容 diff 为空）
- `work/svg_probe.py`、`work/svg_probe.json`（自有 SVG 探针：节点、Han/全角括号、法语串、金句、P8 流末、P7 预告、家具、图片、右缘/框线/行首/切词、P6 覆盖）
- `work/freeze-diff.txt`、`work/freeze-diff.json`、`work/freeze-baseline.txt`（canonical freeze）
- `work/p8-compare.txt`、`work/p8-compare.json`、`work/p8-core-extract.txt/.json`、`work/p8-ed-extract.txt/.json`、`work/keycompare.txt`、`work/keycompare.json`（P8 双门）
- `work/occl-selftest.txt`、`work/occl-ed.txt/.json`、`work/occl-core.txt/.json`、`work/occl-ed-vs-core.txt/.json`（canonical 几何审计）
- `work/literal_freeze.py`、`work/literal_freeze.json`（源码字面冻结）、`work/gloss_probe.py`、`work/gloss.json`（gloss 口径计数）
- `work/replay-core/`、`work/replay-ed/`、`work/reg/core.json`、`work/reg/ed.json`、`work/reg/core-log.txt`、`work/reg/ed-log.txt`（登记重跑与 SVG 8/8 复现）
- `work/transform-replay/`、`work/transform-replay-log.txt`（358 行）、`work/transform-replay-runlog.txt`、`work/reg/transform-replay.json`（transform 单独复现 8/8）
- `work/webcheck.py`、`work/web/`（`webcheck.json`、`rebuilt-web.pdf`、8 张 SVG 重渲染卡）

**终判：ZERO PROBLEMS — 本版可交付上架，阻塞项无。**
