# 独立校对报告 — Lucerna Weekly W45 · FR × PT（法语 × 葡萄牙语）

**结论：ZERO PROBLEMS**（阻塞项：无。本版可交付上架。下述观察 O1–O8 均为 KIT 表述精度问题、口径说明或已裁定的家族行为，纸面正确，不阻塞。）

**校对员纪律**：只校对，未派生任何下级代理，未碰 weekly-git，未改核心/W43/交付目录，未改 tools/ 下任何文件，未清理共享 scratch，未发 Discord，未往主聊天发卡片/PDF，未建 cron，未宣布上架（上架由协调员串行做）。所有重跑一律在自有 scratch（`hidden_files/w45/fr-pt-proof/work/`）内进行：核心构建树与分版构建树均先完整拷贝到 scratch 并把 OUT 重定向到 scratch 输出目录，原构建树、交付目录与核心目录全程只读；门输出未截断，证据文件见文末。

## 0. 开工查重与交付指纹（独立重测）

- 开工时 `ps` 无任何以本版（fr-pt）树为 cwd 的在途进程（唯一在途同类进程为 ko-zh-tw 的 insert，与本版无关）；交付物最新 mtime 为 `WEEKLY-KIT.md` 2026-10-28 05:34 UTC（PDF 05:26、SVG 05:26），至开工时已静默逾 90 秒复查无变化 → 安全开工，不 stand down（新鲜 mtime + 静默 = 已完工交付物，非在途写入）。
- 校对前后哈希 diff：交付物（2 PDF + 8 SVG + 8 卡）与核心 8 SVG **内容哈希 diff 为空**（证据：`work/delivery-hashes.txt` vs `work/delivery-after.txt`；核心 8 SVG 与建造树 `core-svg.sha` 亦逐项一致）。交付物 mtime 校对前后无刷新。
- 印刷 PDF `lucerna-fr-pt-print.pdf`：9,749,607 字节，sha256 `7d87195cf9b2bfccf7dafc9321edc742d39ec0a7d6f7e55429dd0e9b1abbf152`，pypdf 8 页，1462.5×2025 pts；网页 PDF `lucerna-fr-pt-web.pdf`：5,103,001 字节，sha256 `3321a487ae5e55b28fe80dd411e7d629b9771c213c3382648f90acac4bd5f329`，pypdf 8 页，936×1296 pts。两值与建造员声称逐字节一致（系独立重测，非采信）。
- 8 张卡均为 1950×2700 px；8 SVG 哈希与 KIT §15 逐项一致（p1 `87d7ec8f…`、p2 `1ab15c6d…`、p3 `3a9f0010…`、p4 `e05b7dd4…`、p5 `545a53ab…`、p6 `20cc6921…`、p7 `d086a953…`、p8 `386feaf9…`，全值见快照文件）。
- 刊头：每页 `Le Lucerna`；VOL.3 全版一致；VOL.2 仅出现在 P7 延期披露句中（正当引用核心句，非残留）；VOL.4 出现处均为下期正向引用（P7 披露+预告、P8 写作条+答案 150）。

## 1. 门 1 — 冻结与法语核对串：通过

- **核心基线**：`tools/freeze.py baseline`（自有 scratch，OUT 已重定向）**8/8 逐字节一致**，核心交付 SVG 哈希复核未变（p1 `f02e628e…`、p2 `b192c192…`、p3 `5f332e9f…`、p4 `240f379d…`、p5 `a4d64e3e…`、p6 `47e4346d…`、p7 `e997123f…`、p8 `822dbe3d…`）。
- **新增 CJK**：`freeze.py diff` 逐页：核心 CJK 总量 202/244/179/197/177/198/390/1030（P1–P8）→ 分版 **0**，**新增 CJK 8 页均为 0**。自有 Han 范围（U+4E00–U+9FFF）扫描交叉验证：分版 8 页 Han 均为 0，全角括号 8 页均为 0；核心 Han 为 192/219/156/171/159/170/328/788（两种口径的核心总量不同源于 CJK 统计范围，分版侧均为 0，结论一致）。
- **删除串逐项裁定**（freeze-diff.json 全量核查，非抽样）：
  - P1 删除 45 项，其中非汉字 22 项，**全部为头条段重排碎片，且每个碎片的全部单词均在分版全文中存活**（如 `Le Goût du Large », samedi 7 et`、`À Plailly, dans l'Oise, c'est la` 等）——法语词零损失，系 24pt/1.45 vs 核心 25pt/1.52 换行所致。
  - P2/P4/P5/P6 删除串中非汉字项为 **0**（删除串均含中文讲解层）。
  - P3/P7 各 1 项非汉字删除串，均为 `）。`（中文注释换行残片），非目标语。
  - P8 删除 138 项，其中非汉字 33 项，全部为电池段/答案行重排碎片（14.5pt 重排）+ 已备案改向：`Traduisez` 题干 ×5 → `Traduza`（见门 2）、全角括号 → 半角、中文注释 → 葡萄牙语注释；碎片中的法语词除改向项外均在分版全文中存活（个别“未存活”判定为探针分词假象，如 `（futur` 含全角括号前缀，`futur` 本词在分版中存在）。
- **冻结串逐项（核心 SVG 与分版 SVG 核对，缺一不可）**：
  - P4：`41e édition en 2026 (40e anniversaire)` 分版 P4 (1473, 278.0) 与核心同坐标；全版 `40e` 计数分版 = 核心 = **1**；`22e`/`15e`、习题号 `40.`/`140–144.` 未动（REG 逐题相等，见门 4）。
  - Q120：题干分版与核心**同坐标** P8 (527, 246.0)，20pt：`Si j'étais libre dimanche, j'___ à Nanterre. A.`；选项行同坐标 (527, 275.0)：`irai · B. irais · C. vais`；REG 键均为 **B**；P8 注同步：分版 (989, 2325.47/2344.32) `120. B (si + imparfait → conditionnel présent; j' é je antes de vogal (elisão))`，语法点（si + imparfait → conditionnel + elision j'）齐全。邻题 Q119（题干 `Elle s'intéresse ___ festivals.`，键 B）与 Q121（题干 `À mon avis, ce programme ___ très riche.`，键 A）题干与键均与核心一致（仅 y 坐标因重排微移：Q119 电池行分版 1400.625 vs 核心 1426.825；Q121 分版 362.0 vs 核心 367.0——题干与键不动，坐标移动属重排，非改写）。
  - P7 引用 #4：分版 P7 表内 (527, 1443.85/1474.65/1505.45) `« Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? » (page 4)`；P4 辩论框原文 (1473, 2238.40/2268.93/2299.46) 逐字相同；B1 教学栏同步出现该 comparatif（P7 (527, 613.2/647.4/681.6) 等）；跟进键 `plus excitante`（Q100）未动。
  - #8：分版 P7 表内 (1451, 1330.9/1361.7) `« Les jeunes créateurs y rencontrent leur public, en vrai. » (page 5)`；P5 原文同句 (1473, 1322.12 起)；Q106 改写实测：P7 诊所 (65, 2203.2/2235.825) `✗ « Les jeunes créateurs y rencontre leur public, en vrai. »`（error `rencontre`），P8 答案键 `rencontrent`（REG Q106 键与核心逐字相等）。
  - P6 同步：`Ce calendrier peut encore bouger.` 分版 P6 深读 (1007, 658.88) 引文、P6 观点栏、P7 B2 教学栏三处一致；P6 深读小写形与微习题键 `peut`（Q95）不动。
  - **结论：任一法语串与核心不符即冻结失败——本版无此情形。门 1 通过。**

## 2. 门 2 — P8 双门（FR 族硬性，缺一不可）：通过

- 工具版本：`tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b27462703d8226815046eccc0ca9`，与建造员声称的已验证新版一致。
- 门 ① plain **显式双路径 + `--total 150`**：核心 noted **97**，分版 noted **97**，状态 **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]。noted 集逐项与建造员声称一致：[1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109–150]。
- 错误口径复现（仅作记录，不采信）：`--core-dir/--edition-dir --target fr` 形式确给出 92/92 + keydiff [135, 145]（与建造员记录的路径差异一致）；默认 `--total` 会取 W43 的 149 而错分段——本校对全程禁用这两种形式，以显式路径 + extract + keycompare 三方一致为准。
- 门 ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（SVG 路径入参，`--total 150`）：两侧各 150 键，mismatch **仅 [135, 150]**，两项在两侧均为 noted 项且均为已备案改向；**裸键 mismatch 0**（FR 核心设计上只印 97 noted、53 裸键；plain CLEAN 对裸键是盲的，本门以 keycompare 补盲——绝非只用 plain）。
- **改向逐项印刷核实（非照抄他版）**：
  - #135（两侧均为 noted）：核心键 `读一份日程，本身就是在了解法国。` → 分版键 `Ler um programa já é compreender a França.`；电池区 E1 题干分版 P8 (989, 1332.0/1361.0/1390.0) `Traduza para o português: « Lire un programme, c'est déjà comprendre la France. »`（法语引文逐字保留，方向翻转为法→葡）；答案区 #135 印刷行分版 P8 (1451, 1968.75 起) `135. Ler um programa já é compreender a França. (lire un programme = ler um programa)`。
  - E2–E5 题干葡萄牙语化、法语键不变：E2 (1451, 246.0) `Traduza para o francês: Ele corre mais rápido que o irmão.`，键 `Il court plus vite que son frère.`；E3 (1451, 362.0) `Os alunos estão de férias desde 17 de outubro.`，键 `Les élèves sont en vacances depuis le 17 octobre.`；E4 (1451, 478.0) `Hoje à noite, vamos preparar as nossas mochilas.`，键 `Ce soir, nous allons préparer nos cartables.`；E5 (1451, 594.0) `Ainda não se conhecem os finalistas.`，键 `On ne connaît pas encore les finalistes.`。
  - #150（两侧均为 noted）：核心键 `开放题 — 要点见写作框，范文在第 8 版写作框内` → 分版键 `Questão aberta — os pontos estão no quadro de escrita e o modelo está no quadro MODÈLE desta página`，注释 `Avaliação por pontos`；印刷行分版 P8 (1451, 2213.8/2232.65/2251.5/2270.35) 逐字确认（p8 提取将破折号后截断为 `Questão aberta`/`开放题`，但 mismatch 集与裸键结论不受影响）。
  - P8 注释语言纯度：分版 P8 答案区 Han 0、全角括号 0；跨族残留探针（德语 Schulbeginn/Übersetzen、西班牙语 Traduce 等）全版 0 命中。
- **通过条件满足：plain ∈ {CLEAN} 且零裸键 mismatch。门 2 通过。**

## 3. 门 3 — gloss 逐项计数：通过

- 自有 AST 重计（README #21 口径：gloss() 渲染串按 `·` 本身切分；Nota 串先去前缀 `Nota — ` 再切分；词表按 mots 列表字面计数；只读解析构建源码，绝不执行构建模块）：

  | 页 | gloss() 项 | Nota 项（去前缀后切分） | 词表项 |
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

- 核心与分版逐页逐项相等（7/6/6/7/6/6 + Nota 9 + 词表 26），三口径分开记账、未混算；全部 38 项 gloss 的法语首词均在对应渲染页实测存活（缺失 0 项）。
- P7 词框定义句冻结：P7 教学区（A2/B1/B2/工具箱）法语句节点与核心逐字相同（教学区节点比对：61 个节点逐字相同；分版独有节点仅为葡萄牙语工具箱注释 3 行 + 2 个双语栏头，核心独有节点仅为对应的中文注释 2 行 + 2 个中文栏头）——**只本地化讲解行，定义句本地化 = 阻塞性冻结失败；本版无此情况**。此规则经核查适用于全部目标语言的同一做法（本版为法语目标语实例）。

## 4. 门 4 — 金句、登记、范文：通过

- **金句 8 句（联合文本计数，分版 = 核心）**：#1 `Le lundi 2 novembre, on reprend les cours.` = **5**；#2 `On ne connaît pas encore les finalistes.` = **3**；#3 `Les cimetières se sont remplis de chrysanthèmes.` = **1**；#4 `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?` = **5**；#5 `Le festival se promène dans Paris.` = **1**；#6 `Ce calendrier peut encore bouger.` = **3**；#7 `Ce week-end, tout se joue.` = **1**；#8 `Les jeunes créateurs y rencontrent leur public, en vrai.` = **3**。与任务给定核心计数逐项一致。
- **P7 短语表（印刷表实际内容）**：8 句在分版 P7 表内均带正确页签：#1 (page 2) (65, 1234.0/1264.8)、#2 (page 1) (65, 1531.45/1562.25)、#3 (page 3) (65, 1797.0/1827.8)、#4 (page 4) (527, 1443.85/1474.65/1505.45)、#5 (page 5) (527, 1740.20/1771.0)、#6 (page 6) (989, 1415.575/1446.375)、#7 (page 1) (989, 1713.025)、#8 (page 5) (1451, 1330.9/1361.7)。出处页核实：8 句的词序内容均出自所标页正文；其中 #2/#3/#5/#7 在正文中的标点形态为破折号/冒号/标题片段，P7 表将其规范为句号——**该规范化是核心原文即有的做法，分版与核心表述逐字相同**，非分版新增改写。教学栏/工具箱重复 #1/#2/#4/#6 为 KIT 设计（“2×” = 源文章 + P7 表格对），非缺陷。
- **8 句均在所标源文章页实测命中**：#1 P2、#2 P1、#3 P3、#4 P4 辩论框、#5 P5、#6 P6、#7 P1、#8 P5（各页 joined 文本逐字命中，见门 1 逐项坐标）。
- **登记（自有 scratch 拷树重跑，OUT 已重定向，单进程 content12→34→56→7→8，核心与分版各一）**：核心与分版 REG 均为 **150 题连续（1–150）**；页分布两侧逐项相等 **10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P2=15、P5=17、P8=42，FR 串）；级别两侧逐项相等 **A2 53 / B1 75 / B2 22**；逐题 page/level 150/150 相等；题型数量 1:1 本地化（Completar frases 49 · Escolha múltipla 26 · Associação 21 · Texto com lacunas 8 · Transformação 7 · Leitura de gráficos 6 · Verdadeiro ou falso 5 · Compreensão de leitura 5 · Tradução 5 · Completar diálogos 5 · Prática 8 · Correção de erros 4 · Redação 1）；REG 键仅 #135/#150 不同（即门 2 两改向项），余 148 项键逐字相等；Q119/Q120/Q121 键分别为 B/B/A，两侧一致。
- **范文 86 词实测**：分版与核心 P8 MODÈLE 框正文（右栏，MODÈLE 栏头 1538 至 RÉPONSES 栏头 1838 之间）逐字相等，**均为 86 词**（`Samedi 7 novembre, j'ai regardé les demi-finales du Masters… C'était un week-end parfait.`）；仅栏头行改为双语 `MODÈLE · MODELO`（核心为 `MODÈLE · 范文`）。

## 5. 门 5 — 几何：通过

- canonical `tools/occlusion_audit.py`（venv，先自检）：自检 6 类 planted 全部命中、干净对照静默；**分版 0 flags，核心 0 flags，NEW vs 核心 0**（证据：`work/occl-ed.json`、`occl-core.json`、`work/occl-ed-vs-core.json`）。
- 全页右缘 ADVANCE 扫描（自有 PIL advance 法，限 1885）：分版**仅 3 项**超限，全部为 P8 F 配对右侧行，最大 x1=**1899.6**，仍在内框线 1910 以内：P8 (1485, 1036.0) `b. une soirée qui dure jusqu'à la nuit`（1891.3）、(1485, 1112.0) `d. le coquillage fêté à Port-en-Bessin`（1891.3）、(1485, 1150.0) `e. plusieurs concerts en une semaine`（1899.6）；核心同文三行文本与 x1 **逐值相同**（核心 y=940/1016/1054，y 坐标因 P8 14.5pt 重排下移 +96，属冻结法语重排继承，非分版缺陷；葡萄牙语自有超限项 0）。
- 全页真墨迹右缘 vs 内外框线（1910/1922）：**0 命中**（全部墨迹右缘 ≤1910，页脚基线 2624 节点除外——页脚为豁免项）；同基线行检查：P1 顶栏 y=92 三段墨迹（左 64.75–215.25、中 541.0–1409.0、右 1495.9–1884.9，间隙 326px/87px）、徽记 y=574、页脚 y=2624（左墨迹止于 994.2、右起于 1762.7，间隙 768px）**0 重叠**；P1 深色横幅双行（478/522）：法语左段墨迹右缘 971.8/1049.0，葡萄牙语右段起端 1273.8/1208.5，间隙 302px/159.5px，**无重叠**。
- P6 图表标签基线锚定墨迹覆盖（getmetrics ascent/descent 法，禁用 getbbox）：分版与核心均为 **0.0%**（<30% 通过；实测为“无任何后绘矩形与任何文字基线锚定盒相交”，比 <30% 更强）。
- 流末端（SVG 实测基线/真墨迹，流光标为构建日志口径，见观察 O8 的口径说明）：
  - P1 headline 栏光标 1537（限 1812）；P1 hiver 末基线 2253.6 = 核心值，墨迹底约 2259（quiz 规则线 2312，余 53px；光标 2298 为尾部间隙假象）；P1 quiz 末基线 2479.9 = 核心值，墨迹底 2480.15。
  - P2 feature 642，习题 2365；ET VOUS 框底 1546.6（rect 1451,1173.1,434×373.5）vs 核心 1538.6（+8px：葡萄牙语末行墨迹底 1539.46，距框底 7.1px，距下规则线 1558 有 11.4px 框距/18.5px 墨迹距）。
  - P3 正文 813；P4 正文 1246，微习题 2154；P5 页最大基线 2486.12（核心 2456.40，+29.72；系第 2 栏习题尾行 `moi.`，见观察 O5），墨迹底 2486.37（限 2540，余 53.6px；y>2400 节点全部在 x<989 内，未溢入第 3 栏）；第 3 栏（x=1473 葡萄牙语说明栏）较核心多 2 行（39 vs 37 节点），即 (1473, 1478.0) `o público ao vivo.` 与 (1473, 1929.0) `música ouvem para aprender francês?`，均为葡萄牙语段落由 2 行绕为 3 行的本地化换行，遮挡审计 0 旗。
  - P6 深读 1049，习题末基线 2505.05（核心 2504.50），墨迹底 2510.80（页脚规则线 2580，余 69.2px；光标 2557 为尾部间隙假象，与核心同口径）；观点栏 1256（距图表顶 1330 有 74px），微习题 2050。
  - P7：A2 954，B1 1053，B2 988，工具箱 1008，短语栏 1574（限 1830），诊所 2140（限 2268）；读者框末基线 2233.3 = 核心值，墨迹底约 2239.2（框底 2258，余 18.8px）；**预告末基线 2494.0，墨迹底 2498.5 < 2540（余 41.5px）**。
  - P8：见门 5.1 专项裁决。

### 5.1 P8 流末端口径裁决（重点）：通过（依据如下，不以 fr-de 前例了事）

| 口径 | 分版 | 核心 | 差 |
|---|---|---|---|
| battery 流光标（Flow end_report，限 1485） | 1487 | 1410 | +77 |
| battery 末墨迹基线 | 1446.4（P8 (1451, 1446.4) `Merci !`） | 1455.825（P8 (65, 1455.825) `· C. des`） | −9.425（分版反而更短） |
| battery 墨迹底：canonical 真墨迹盒 | 1446.65 | 1456.08 | 距写作条规则线 1486：分版 39.35px |
| keys 流光标（Flow end_report，限 2545） | 2298 | 2167 | +131 |
| keys 最大基线（答案行，不含分隔栏头） | 2532.82（col 527 与 col 989 并列） | 2539.19（col 65，P4 组尾行 `44. B … · 45. A · 46. C · 47. B · 48. A ·`） | **−6.37（分版答案行反而更短）** |
| keys 最大基线（全部节点，含分隔栏头） | 2544.03（col 65，分隔栏头 `— Página 4 —`，17pt bold） | 2539.19（同答案行最大值；核心最大分隔栏头仅 2498.93） | +4.84 |
| keys 墨迹底：canonical 真墨迹盒（全局最大节点） | 2548.28（分隔栏头） | 2541.23（col 527 答案行） | +7.05；距页脚规则线 2580：分版 31.72px、核心 38.77px |
| keys 答案行墨迹底（不含分隔栏头） | 2536.07（col 527/989） | 2541.23 | −5.16 |
| FOOTER 旗标（canonical 审计，规则线 2580） | 0 | 0 | — |

**按列分解（答案行）**：col 65：分版 2499.18（`usa cores) · 43. 19 heures`）vs 核心 2539.19（−40.01）；col 527：分版 2532.82 vs 核心 2537.73（−4.91）；col 989：分版 2532.82 vs 核心 2526.11（+6.71）；col 1451（末列，P8 组溢流尾）：分版 2270.35 vs 核心 2137.45（+132.90）。因此全局答案最大值 −6.37 是**各列组尾填充水平不同**的结果，不是某一题的单点下跳；而全局全部节点最大值 +4.84 **完全来自 col 65 末尾的分隔栏头 `— Página 4 —`**（该列填满 P1–P3 答案后以分隔栏头收尾，下一列起为 P5 组），不是答案行的增长。

**增长来源**：内容增长的直接证据（REG 实测）：P8 组（109–150）印刷注总字符分版 **1381** vs 核心 **740**（+641，+87%），键总字符 617 vs 517（+100），字号 14.5pt vs 15.5pt 的缩小未能抵消注长增长，致 keys 流整体拉长（光标 2298 vs 2167，+131），末列尾部下移 +132.90——但末列尾行墨迹底仅 2273.6，距限值甚远；col 989 的 +6.71 亦为同机制的组内填充差异。**建造员 KIT 所述“答案最大基线 2544.0（核心 2539.2）”在口径上是错的**：2544.03 是分隔栏头基线，不是答案行基线；答案行口径下分版反而低于核心（见观察 O1）。本裁决不依赖该表述。

**过门，依据（按重要性排序）**：(a) keys 流自身的声明底限为 **2545**（content8.py `Flow(..., 2545, tag="P8-keys")`），全部节点最大基线 2544.03 < 2545，答案行 2532.82 亦然——名义 2540 是通用 CONTENT_BOTTOM 默认值，不是 keys 流的限值；(b) 页脚规则线为 **2580**，canonical 审计 FOOTER **0 旗**，真墨迹底距规则线 31.72px（答案行口径下为 43.93px），无压线、无墨迹触线；(c) 增长确为内容增长（葡萄牙语注 +87%）导致的合规下移，且分版 battery 墨迹反而短于核心、答案行墨迹亦短于核心，排除系统性下沉。**fr-de 前例（本版与核心同值、超限仅 1–3px 的纯口径案）与本案不同，本裁决不依赖该前例**，仅依赖上述限值与间隙事实。若任一事实为反（超 2545 流限、或墨迹触 2580、或 FOOTER 有旗），即应为阻塞项——实测三者皆无。

## 6. 门 6 — 换行/孤儿：通过

- 渲染日志零 FLOW OVERFLOW：自有 scratch 重跑日志与建造树 render-log-r4.txt 均无 `FLOW OVERFLOW`/`HEAD TOO WIDE` 行（流光标超限见观察 O8，属尾部间隙假象，墨迹均在限内）。
- 行首 `:`：分版 4 项，与核心**同页同坐标同文本逐字节相同**：P3 (1451, 789.65) `: on le pose sur les tombes, on ne l'offre jamais`、P4 (65, 837.12) `: quarts de finale vendredi 6`、P5 (1473, 430.65) `: clôture du festival.`、P7 (527, 428.1) `: attention à l'accord avec le sujet :`；葡萄牙语自有行首违规 **0**。
- 拉丁连字符行末切词：全版行末为 `-` 的节点数为 **0**（无单词连字符切词）；行末 en-dash 列表换行**仅 4 处**，文本与核心逐项相同（P4 (527, 864.22) `A. Paris SG – Troyes · B. Lens –`、(527, 2233.14) `vendredi 6 novembre avec Toulouse –`、(527, 2376.02) `Dimanche 8, six matchs : Rennes –`、(527, 2411.75) `Lille, Le Mans – Monaco, Le Havre –`；核心同文 y=805.0/2114.47/2257.35/2293.07，y 整体下移系 P4 重排所致）——均为球队/赛程列表的 en-dash 分隔换行，下一行续列表项，非单词切词。
- 跨栏换行逐项：P5 第 3 栏多 2 行系葡萄牙语本地化换行——**已验证，非表述接受**（见门 5：x=1473 栏 39 vs 37 节点，两行均为葡语段落第 3 行绕行）；P4 跨栏溢词见观察 O7（已裁定为 Flow 换行家族行为，非缺陷）；其余跨栏换行均为 keys/习题流的正常分栏填充，遮挡审计 0 旗。

## 7. 门 7 — 读者角：通过（零编造）

- 标注的编辑示例：P7 读者框（rect 989,1878,896×380，框底 2258）内法语示例段逐字保留 `« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).` + 葡萄牙语点评 `Xiao Mo comenta (texto-exemplo): o passé composé está seguro na narrativa do fim de semana; o ponto e vírgula liga os dois dias e vale a pena imitar. No próximo número, a secção comentará textos reais.`。
- 三事实披露（同框内，葡萄牙语披露句 + 法语编辑注双语）：
  1. 无真实来信：葡语 `sem cartas nem redações do VOL.2 até ao fecho (o W44 não saiu)`（“截至付印无 VOL.2 来信与作文”）+ 法语 `aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru)`；
  2. 无 VOL.2 P8 最佳作文：同句 `nem redações do VOL.2`（“亦无 VOL.2 作文”）——来信与作文在同一披露句内并列否定；
  3. 均延至 VOL.4：法语 `Le VOL.4 reprendra la promesse.` + 征集句 `para o VOL.4!` + P8 写作条 `Os melhores textos sairão no VOL.4 (página 7, « Le courrier des lecteurs »).`（P8 (65, 1718.0) 起）与答案 150 行指向同一页。
- **征集句逐字摘录与字面覆盖裁决**：`Enviem-nos cartas e as melhores redações da página 8 para o VOL.4!`（P7 (1013, 2233.3)，读者框末行，墨迹底约 2239.2，框底余 18.8px）。字面覆盖范围：祈使动词 `Enviem-nos` 的并列宾语为 `cartas`（来信）+ `as melhores redações da página 8`（第 8 页最佳作文）——**同一祈使句内同时覆盖来信与最佳 P8 文本，满足字面同时覆盖要求**。预告行 `e as vossas cartas, finalmente!`（P7 预告末行）**不计作征集**（按任务规则排除），本裁决不依赖预告行；内容预告行与征集句已分开算：预告行仅点名来信，征集句本身已覆盖两项，无需组合门兜底（组合门亦满足：同页披露句延期最佳 P8 文本 + 预告行点名 P8 写作佳作——但本案不需要它）。
- FR 族核心为 VOL.3，延期目标 VOL.4 正确（非 VOL.3 自指）。

## 8. 门 8 — 家具三方对照（核心/W43/本版）：通过

- 徽章串逐字节 = W43 同配对版：W43 构建源码 `content12.py:31` 与本版构建源码同行逐字相同：`TEXTOS EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`，实测本版 SVG 节点 (975, 574)，22pt BRICK 粗体居中（FR-as-target 一般形 y=574/22pt BRICK 插入，与 W43 同配对实测一致，无冲突）；真墨迹宽 1200.25px（建造员称 1200.3px，差 0.05px 属舍入）。
- 副标/标语/暗带：P1 顶栏 y=92 三段：左 `VOL. 3 · Nº 3`（W43：VOL. 2 · Nº 2）；中 `HEBDOMADAIRE EN FRANÇAIS · TODA SEMANA · O FRANCÊS QUE OS FRANCESES LEEM`（与 W43 相同）；右 `SEMAINE DU 2 AU 8 NOVEMBRE 2026`（W43：19–25 OCTOBRE 2026）。刊名 262（178pt）、副标题 330（46pt）`SEMANÁRIO EM FRANCÊS · VOL.3 · FIM DE SEMANA DECISIVO`（W43：VOL.2 · OUTONO E FESTAS）、标语 372 法语原文与 W43 相同、暗带 478/522（法语头条为本周内容，葡萄牙语右侧为本周短语）、规则线与暗带几何与 W43 相同。暗带右侧双行（右对齐于 1855）：`SEGUNDA, VOLTA ÀS AULAS · EM TODA A FRANÇA`（起端墨迹 1273.8）/ `COMEÇO DO MASTERS · ABERTURA DO FESTIVAL · VER PÁGINA 2`（起端墨迹 1208.5），与法语左段无重叠（见门 5）。
- 页脚（每页，y=2624）：`Le Lucerna · SEMANÁRIO FRANCÊS VOL.3 · TEXTOS EM FRANCÊS · EXPLICAÇÕES EM PORTUGUÊS` + `Página N de 8`（8 页逐页核实，W43 模板，VOL 号更新；W43 构建 bslib4.py:70–71 同模板，VOL.2→VOL.3）。
- 短双语栏头（与 W43 同）：PALAVRAS、O DEBATE、TREINO、NÍVEL BÁSICO / INTERMEDIÁRIO / DESAFIO、PARA LEVAR（工具箱，W43 偏差：FERRAMENTAS 超宽）、CLÍNICA、LER O CALENDÁRIO、DATAS、SUMÁRIO、EM RESUMO、QUIZ RELÂMPAGO、VOCABULÁRIO（P6 LES MOTS 流栏头与 P8 F 栏头，W43 同法）；gloss 前缀 `Nota — `；P8 分隔 `— Página {n} —`（8 个，见门 2）；P8 栏头 A `LACUNAS`、B `ESCOLHA`、C `COMPREENSÃO`（24pt 全式均 > 434 栏宽的缩短形，D/E/F/G 全式适配保留全式）；keys 头 `RÉPONSES · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)`；cloze 标签 `Opções:`。
- W43 偏差清单（KIT §12）逐项核实均为呈现/本地化类：VOL/刊期/副标题/暗带短语为刊期更新；P8 答案 14.5pt（W43/核心 15.5pt）与 battery 间距 6（核心默认 11/14）为注长适配；P1 头条 24pt/1.45（核心 25pt/1.52）仅呈现变化、法语文本字节不变；P1 gloss 单字化、P2 ET VOUS 2 行定稿、栏头缩短均为框界适配；读者角示例+披露继承核心诚实处理，新增征集句为 SOP 门禁要求（非事实主张）；翻译改向方法同 W43 先例、项号不同（本版 #135/#150；W43 为 #132/#145）。

## 9. 门 9 — 图片：通过

| 页 | 图 | 放置（x, y, w×h） | credit（与核心逐字相同，确已放置） | payload 双口径 |
|---|---|---|---|---|
| P1 | atget-paris.jpg | 65, 1874, 896×320 | Eugène Atget (1857-1927), photographie, domaine public（P1 (65, 2271.3)） | base64 文本 sha256 `ff20bc2b…fa8e5d`；解码 JPEG sha256 `f3705af2…14595f`，334674 字节 |
| P2 | hiroshige-maple.jpg | 1451, 200, 434×480 | Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA（P2 卡面目视 + SVG 节点确认） | base64 文本 sha256 `6918cb8b…1664ae`；解码 JPEG sha256 `5b772fac…970ee2`，646242 字节 |
| P3 | chrysanthemum-blanco.jpg | 1451, 200, 434×540 | Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public（P3 卡面目视 + SVG 节点确认） | base64 文本 sha256 `bfaadf5b…86171e`；解码 JPEG sha256 `be071fda…f43121`，142340 字节 |

- 三图两种口径全值在核心与本版 SVG 内嵌 payload 中逐字节相同（全值见 `work/svg_probe.json`）；三张图均已核实确已放置（SVG `<image>` 节点 + 卡面目视），解码字节数与资产文件一致。credit 行取 Commons Artist 原文（Atget 1857–1927、Hiroshige 1797–1858/LACMA、Blanco《Flora de Filipinas》19 世纪），与任务给定核心信息逐项一致。

## 10. 门 10 — 网页版 PDF：通过（fr-en 噪声教训已闭合）

- `pdfinfo`：8 页；`pdfimages -list`：每页内嵌 JPEG 均为 1950×2700、150ppi，与卡片 1:1，无缩放。
- **流同一性（门）**：按建造配方全流程重建网页 PDF（卡片 PNG → RGB JPEG quality 72 optimize → 重读 → Pillow PDF resolution 150.0），提取 8 页 JPEG 流与交付流**逐字节相同 8/8**（sha 前 16 位：p1 `856f7f88ad481deb`、p2 `6757622d7dc9279f`、p3 `0aabbede035e5066`、p4 `0d311c3d4a7f340f`、p5 `6ecd5d56af60d209`、p6 `8f33f53c84f2def9`、p7 `ee587ad6cc8ceb82`、p8 `521a6657c0b094e1`）。诚实口径说明：直接 JPEG q72 编码 ≠ 交付流（Pillow PDF 容器会重编码），故直接比对不等不构成失败；全配方重建流 8/8 一致才是决定性证据。q72 为配方参数（建造 render.py 明文 quality=72；q75 直接编码亦 ≠ 交付流，且全配方 q72 已匹配，故 q75 未用作交付）。
- **逐页像素比对**（`pdftoppm -r 150` 渲染 8 页 vs 卡片，同尺寸 1950×2700）：全幅 L 均值差 P1–P8 为 5.933 / 5.723 / 5.208 / 5.744 / 4.620 / 4.912 / 6.067 / 8.632；>30 差值像素占比 8.11% / 8.22% / 7.39% / 8.13% / 6.55% / 7.15% / 8.55% / 12.06%；4× 降采样均值差 2.656 / 2.388 / 2.161 / 2.352 / 1.932 / 2.111 / 2.588 / 3.062。**无离群页**（最高为 P8，系文字最密页的正常 JPEG 痕迹；降采样后结构一致）。**无噪声页。**
- 附带验证：卡片自交付 SVG 重建（cairosvg svg2png @1950）**8/8 逐字节一致**；印刷 PDF 自交付 SVG 重建（cairosvg svg2pdf + pypdf 合并）**逐字节一致**（9,749,607 字节，sha256 与交付完全相同）——交付链（SVG → 卡片 → 双 PDF）全部新鲜一致，fr-en 噪声教训不适用于本版。

## 11. 门 11 — transform 单独复现（ko-ru B-1 教训，阻塞级）：通过

- 自有 scratch 内全新核心拷贝（bslib4.py、svglib.py、content12/34/56/7/8.py、assets）+ 建造树 transform.py 单文件运行：**357 项替换**（content12 74 → content34 162 → content56 239 → content7 271 → content8 340 + 修复轮 r2 10 + r3 5 + r4 2 = 357），transform-log 与建造树逐字节一致。
- 变换后 6 个源码文件（bslib4.py + content12/34/56/7/8.py）与建造树**逐字节一致 6/6**（`cmp` 全 IDENTICAL；svglib.py 未参与变换，不计入）。
- 随后在自有 scratch 内把 OUT 重定向到 scratch svg 目录、单进程 driver 重渲染：产出 SVG **8/8 逐字节 = 交付**。**复现成功，非阻塞。**（建造员声称的“r4 经 pristine + transform 重放 6 源码文件逐字节一致”经独立验证属实；本校对另加了渲染级 8/8 验证，比源码级更强。）

## 12. 门 12 — ABSTRACT：通过（见观察 O3 的诚实口径说明）

- ABSTRACT.txt：葡萄牙语单行（1 行 + 末尾换行），无 ASCII 双引号，含刊头 `Le Lucerna VOL.3`、刊期 `semana de 2 a 8 de novembro de 2026`、目标语与读者语（`semanário em francês para leitores de língua portuguesa`）、级别 `do A2 ao B2`、题数 `150 exercícios`。
- 真实主题关键词逐词在刊内找出处（SVG 全文，不区分大小写）：Rolex Paris Masters（2）、Nanterre（10）、Peur sur le Parc（5/9）、Plailly（11）、Le Goût du Large（3）、Port-en-Bessin（14）、volta às aulas（3）、2 de novembro（1）、Halloween（12–14）、Toussaint（20–21）、Pitchfork Paris（2）、orçamento（7）+ 2027（4）、Assembleia Nacional（1–2）、150（印刷页多处为题号/日期组成部分；题数 150 由 REG 实测 150 题背书）、exercícios（4）、vocabulário（2）、gramática（9）、A2（52）、B2（26）。**主题关键词无编造。**
- “桥接”一词：交付纸面 SVG **0**、ABSTRACT.txt **0**、构建渲染代码（content*/bslib4/transform/render/run）**0**。建造树内仅两处元语言命中，均非纸面内容：(a) KIT §7 `Nota 桥接串`——KIT 自述元语言句，**按任务明确除外**；(b) 建造树 `checks.py:73` 的探针字面量（该探针本身就是断言纸面无此词的检查，其字面量不可能进入渲染文本）。**裁决：不构成阻塞。**

## 13. 门 13 — 全部 8 张卡目视检查：通过

- 8 张卡已逐张全幅目视（非抽样）：P1 刊头/徽章/暗带/Atget 图+credit/quiz 干净；P2 ET VOUS 框内 2 行葡语定稿完整、D·LES MOTS 栏头居栏底为核心同构（核心同页同栏亦有此栏头，y=2468；本版 y=2497，系葡语说明行加长所致，非缺陷）；P3 Blanco 图版+词表+日期栏干净；P4 辩论框与 41e 句干净（跨栏溢词见观察 O7）；P5 Creator Week 三行葡语说明与辩论框干净；P6 日程表/观点栏/图表标签干净，无覆盖；P7 读者框与预告框余量清晰（见门 7）；P8 电池区/MODÈLE/答案区末行与页脚规则线间隙清晰。**无重叠、无切字、无框外溢出、无页脚碰撞。**

## 非阻塞观察（单列一节，不得混入阻塞项）

- **O1 — KIT P8 最大基线表述口径错误（纸面正确，结论不变）**：KIT §5/§17 的“答案最大基线 2544.0”实为分隔栏头基线（2544.03），答案行最大基线实为 2532.82（低于核心 2539.19）；KIT“墨迹底约 2549.1”为保守口径，高于本校对 canonical 真墨迹盒 2548.28（差 0.82px，属方法舍入）。两种口径距 2580 均逾 31px，裁决不变，仅数值归因需订正（见门 5.1 分解）。
- **O2 — KIT P8 墨迹底口径说明**：建造员墨迹底约 2549.1 对应的是分隔栏头墨迹（本校对 2548.28），而非答案行墨迹（2536.07）；核心墨迹底约 2543.8 对应的是核心答案行墨迹（本校对全局最大 2541.23，方法差约 2.6px）。口径统一后：分版答案行墨迹低于核心，增量全部来自分隔栏头位置——结论不变。
- **O3 — ABSTRACT 收尾学习者短语的逐词口径（诚实说明，fr-it 同类前例）**：收尾句 `Aprender francês com notícias reais: fim de semana decisivo, horário de inverno e festas francesas.` 中，主题词全部真实（冬令时：法语 `heure d'hiver` 印刷多处 + 葡语 REG 注 `O horário de inverno começou a 25 de outubro`；节日：Pitchfork/Goût du Large/Peur sur le Parc 均在刊内；真实新闻：本期即为真实法语新闻文章），但 3 个葡语 paraphrase 词在印刷文本与 REG 中均无字面出现：`notícias`（0）、`festas`（0）、`francesas`（0）；`inverno` 仅见于 REG 注（印刷层用法语 `hiver`）；`texto-modelo` 为复合 paraphrase（刊内为 `MODÈLE · MODELO` 栏头与 `modelo` 一词）。按 SOP #22，摘要的学习者短语是“学习者实际搜索的短语”，其功能是可发现性而非刊内引文；且无任何编造的事件/主题，故列为观察而非阻塞——与 fr-it 校对对同类摘要 paraphrase（`ora solare`/`bilancio 2027`）的裁决一致。若协调员对此采取更严的字面口径，可将本条升级为阻塞项，但本校对按前例与 SOP #22 的短语功能裁定为通过。
- **O4 — KIT P5“正文末基线 2486.1”措辞不精确**：2486.12 实为 P5 页最大基线（第 2 栏习题尾行 `moi.`），而非文章主流程末端；数值本身经核实无误（核心同口径 2456.40），仅措辞需订正。
- **O5 — KIT 网页像素差绝对值未完全复现**：KIT 称全幅 5.0–8.6；本校对 L 口径实测为 4.620–8.632（P5 4.62 略低于 5.0 下限），4× 降采样 1.932–3.062。差异源于比对方法（L 通道 vs 全通道均值），且流同一性（8/8 逐字节）已决定性证明网页版即卡片编码，故不影响结论。
- **O6 — 流光标超限为尾部间隙假象**：P1-hiver 光标 2298 > 限 2290（+8）、P6-ex 光标 2557 > 2540（+17）、P8-battery 光标 1487 > 1485（+2），三者均为 Flow 终点光标（含尾部间隙），SVG 真墨迹底分别为约 2259 / 2510.80 / 1446.65，距下一规则线 53px / 69.2px / 39.35px——与核心同口径（核心 P1-hiver 光标 2298、P6-ex 光标 2557 亦同值），非分版缺陷。
- **O7 — P4 跨栏溢词（家族行为，已裁定）**：分版 P4 (527, 220.5)，20.5pt，`resposta certa.`——À VOUS 葡萄牙语指示句首行分版 P4 (65, 2524.47) `Leiam o artigo da página 4 e escolham a` 将 col0 填至底限，尾词溢至下一栏顶（首基线 = 流顶 200 + 20.5 = 220.5）；与已上架 fr-de/fr-it 交付物同处节点（同坐标、同字号、同机制）逐项一致；句意跨栏完整（“…escolham a / resposta certa.”），遮挡审计 0 旗，卡面目视无重叠。核心无此节点（中文指示句长度不同，未溢出）——属 Flow 跨栏换行家族行为，非缺陷，接受该裁决。
- **O8 — P2 末栏 `D · LES MOTS` 栏头居栏底**：本版 y=2497，核心同页同栏亦有此栏头（y=2468），系葡语说明行加长所致的同构现象，非缺陷（建造员 KIT §17 所述一致，经卡面目视确认）。

## 终判

**ZERO PROBLEMS — 本版可交付上架，阻塞项无。**（上架由协调员串行做；Discord 投递暂停令仍有效，本校对未投递。）

## 证据文件（`hidden_files/w45/fr-pt-proof/work/`）

- `delivery-hashes.txt`、`delivery-after.txt`（交付前后哈希快照，diff 为空）
- `freeze-diff.json`（冻结差分全量）、`svg_probe.py`、`svg_probe.json`、`svg_probe-joined.json`、`svg_probe.log`（自有 SVG 探针：节点、Han/全角括号、法语串、金句、P8 流末、P7 预告、家具、图片、右缘/框线/行首/切词）
- `occl-ed.json`、`occl-core.json`、`occl-ed-vs-core.json`（canonical 遮挡审计）
- `p8-compare.txt`、`p8-core-extract.txt/.json`、`p8-ed-extract.txt/.json`、`p8-wrongform.txt`（P8 双门；错误口径复现仅作记录）、`keycompare.txt`、`keycompare.json`（全 150 键比对）
- `gloss_probe.py`、`gloss_probe.json`、`gloss_probe.log`（自有 gloss 重计）
- `ink_probe.py`、`ink_probe.json`、`ink_probe.log`（真墨迹底/右缘/框线/P6 覆盖/同基线间距）
- `repro/`（全新核心拷贝 + transform.py 重放：transform-log 与建造树一致，6 源码文件逐字节一致，OUT 重定向重渲染 SVG 8/8 = 交付；`repro-run.log`）、`repro-core/`（核心对照重跑，SVG 8/8 = 核心，`reg.json` 两侧登记对照）、`driver_dump.py`
- `webstreams/`、`rebuiltstreams/`（交付流与全配方重建流 8/8 逐字节一致）、`webppm/`（pdftoppm 逐页渲染比对）、`rebuilt-web.pdf`、`rebuilt-print.pdf`（印刷 PDF 重建与交付逐字节一致）、`rebuiltcards/`（卡片重建 8/8 逐字节一致）
