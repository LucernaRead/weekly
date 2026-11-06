# FR×EN（W45 VOL.3）独立校对报告

**结论：NOT PASS** —— 阻塞项仅 1 项（网页版 PDF 第 1–7 页不可读，见 §1）。
除该项外，SVG×8、卡片×8、印刷 PDF、KIT（除非阻塞观察）、ABSTRACT 全部通过门禁。
本校对不宣布上架；不改源码与交付物；未发 Discord、未往主聊天发卡片/PDF、未建 cron、
未碰 weekly-git、未改核心/W43 目录（只读对照）、未派生下级代理、未清理共享 scratch。
构建树只拷到本目录 `scratch/` 后重定向 OUT 重跑，从未在原地运行会写回交付/核心目录的脚本。

**校对对象**：`files/weekly-report-w45-fr-en/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt），
对照 `files/weekly-report-w45-fr-core/` 与 W43 同配对版 `files/weekly-report-fr-en/`。
开工查重：`files/weekly-report-w45-fr-en/` 与 `hidden_files/weekly-report-w45-fr-en-build/` 无在途写盘
（ps 仅见无关分版 fr-de 的只读快照进程，cwd 不属于 fr-en 树）；交付物最新 mtime 03:28:37 后
138 秒静默（>120 秒）才开工，**不 stand down**。

**证据目录**：本目录 `scratch/`（pre/post 哈希、p8/keycompare JSON、freeze-diff、REG、
重跑日志、occlusion JSON、几何扫描、图表覆盖、网页版提取/渲染图）。

---

## §1 阻塞项（1 项）—— 网页版 PDF 第 1–7 页为噪声图像，不可读

**文件**：`files/weekly-report-w45-fr-en/Le-Lucerna-VOL3-EN-web.pdf`，
5,310,932 B，sha256 `e390000bec5b31c63023803233abd1b13fe7703028cd0a2bc342506034554917`，
8 页，936×1296 pts（与构建员声称尺寸/哈希逐字相符——尺寸哈希对，内容不对）。

**实测**（三条独立解码路径一致）：

| 页 | pdftoppm 渲染均值 RGB | 判定 |
|---|---|---|
| web p1 | (165.4, 133.7, 51.9) | 噪声 |
| web p2 | (187.0, 105.3, 98.0) | 噪声 |
| web p3 | (144.2, 115.5, 179.9) | 噪声 |
| web p4 | (146.8, 125.1, 97.1) | 噪声 |
| web p5 | (157.1, 112.4, 160.2) | 噪声 |
| web p6 | (146.4, 117.4, 55.8) | 噪声 |
| web p7 | (193.4, 71.0, 153.2) | 噪声 |
| web p8 | (226.6, 221.1, 205.1) | 正常（纸色） |

- `pdfimages -j` 提取的 8 张 1950×2700 JPEG：p1 与卡片 p1 的下采样均值绝对差 115.67
  （与全部 8 卡均不匹配），p8 与卡片 p8 仅 0.93（JPEG 噪声级）。
- 全分辨率裁图：页顶约 40 行纸色+框线正确，其下全部为红/黄/绿/蓝横向块状噪声，
  无任何文字结构（证据：`scratch/pg000-top.png`、`pg000-upper.png`、`pg000-mid.png`、
  `scratch/webrender-1.jpg`、`scratch/ff-pg000.png`）。
- 字节证据：页内 JPEG 均为标准 baseline DCT、1950×2700、与 Pillow q75 量化表一致；
  但 p1 流与用同一 Pillow 对交付卡片 p1 的新鲜 q75 编码相比，仅头部 + 前约 500 扫描字节相同，
  其后 99.23% 字节不同——**该流不是卡片 p1 的编码**，不是质量参数差异。

**排除“解码器问题”的对照**（证明是文件本身，不是我的工具）：

1. 同一 Pillow 配方（`save_all` + resolution 150）对交付卡片 p1/p8 重建的测试 PDF
   （`scratch/pil-test.pdf`）渲染干净：p1 均值 (219.3, 213.9, 198.9)，p8 (226.6, 221.1, 205.4)。
2. W43 英文版网页版同法渲染干净：p1 均值 (225.4, 220.0, 204.0)。
3. 本版印刷 PDF 同法渲染 8 页全部纸色（均值 218–232）且有文字层。
4. W45 EN×FR 版网页版 p1 同法渲染干净：(218.1, 215.4, 201.1)。
5. ffmpeg 原生 mjpeg 解码与 libjpeg 系（PIL/poppler）结论相同：p1 噪声 (167.5, 133.4, 47.3)，
   p8 干净 (225.8, 221.0, 205.4)。

**范围**：同一缺陷亦见于 FR 核心网页版（p1 与核心卡片 p1 差 107.96，p8 与核心卡片 p8 差 0.91），
而 EN×FR 版干净——故为 FR 线网页版生产步骤的问题，非全局工具问题。
**本校对不重开核心**，仅向主线报告：核心网页版恐需同法复查。
**修复路径（属构建员/主线，不由本校对执行）**：仅用交付卡片重建网页版 PDF
（上法已验证干净），入仓时重 pin 新的 pdfBytes/pdfSha256；SVG、卡片、印刷 PDF、KIT、ABSTRACT
均无需改动。重建后须对新网页版逐页渲染复核（本报告的复核法：pdftoppm 全页 + 与卡片像素比对）。

**任务书原“网页版 q72 vs W43 q85 记为非阻塞观察”的处理**：
该条的前提是“内容一致、仅字节/哈希变化”，实测前提不成立，故不适用；
质量参数本身仍记为非阻塞观察 O4（实测本版为 q75 而非 KIT 所称 q72，W43 q85 属实），
阻塞的是内容噪声，与质量参数无关。

---

## §2 通过门禁（全部独立重测，构建员声称值一律未采信）

### 2.1 印刷 PDF 与页数

- 印刷 PDF `Le-Lucerna-VOL3-EN.pdf` 9,746,058 B，
  sha256 `e9fb978109ddfea4874083bc210f1e34fc378d7845b09b1c6bf248d713a7e45b`，8 页，
  1462.5×2025 pts，文字层正常（首行 `VOL. 3 · ISSUE NO. 3`），8 页渲染均纸色。
- 网页版 PDF 8 页（见 §1：页数/尺寸对，内容错）。
- 交付物 + 核心校对前后 sha256 diff 均为空（`scratch/pre-hashes.txt` vs `post-hashes.txt`、
  `pre-core-hashes.txt` vs `post-core-hashes.txt`）。

### 2.2 冻结：核心基线 8/8 逐字节；法语正文零删失

- 核心 SVG 现哈希与构建树 `core-prebuild.sha` 8/8 相同。
- scratch 重跑：核心构建树与分版构建树（OUT 重定向到本 scratch）各重渲染 8 SVG，
  **与交付物 16/16 逐字节相同**——交付物完全由构建树复现，无手工改动。
- `tools/freeze.py diff`（独立重跑，与构建员 `freeze-diff.json` 逐项相同）：
  P1 +23/−23、P2 +37/−34、P3 +37/−34、P4 +41/−37、P5 +33/−30、P6 +30/−27、P7 +43/−35、
  P8 +140/−119；新增 CJK 字符 0，分版全文 CJK 0（8 页 SVG 文本节点 CJK 均为 0）。
- 移除的非 CJK 串逐项核实，全部属于声称的两类例外，无法语键丢失：
  - P3/P7 各 1 个 `）。`：核实为中文讲解段落的换行尾标点
    （P3“改写句子（用 ne...jamais / ne...plus / ne...pas）。”，
    P7“语法点｜reprendre：复课、重新开始（pause 后）。”），属已替换的讲解层。
  - P8 14 个换行重排片段（见观察 O2 的计数订正）：逐项核对法语键均在分版 P8 中逐字存活，
    如 119. B / 120. B、132. 句、137./138./139. 句、16./17./18. 句；
    135 题法语句 `« Lire un programme, c'est déjà comprendre la France. »`
    在分版中为 `Translate into English: « Lire un programme, c'est déjà comprendre la France. »`，
    仅由 2 行重排为 3 行。
  - P1/P2/P4/P5/P6 移除非 CJK 串为 0。

### 2.3 P8 双门法（FR 族专属，BINDING）——通过

新旧两版 p8.py 各跑一次 plain（旧版 `tools/p8.py` sha `67df05f1…`，新版
`hidden_files/w45/p8-dash-fix-verify/p8.py.new` sha `96fc2cfe…`，新版需 `PYTHONPATH=tools`）：

| 工具 | 结果 |
|---|---|
| plain 旧版 | CLEAN，noted 97=97，missing=[]，extra=0，uncertain=[]，keydiff=[135, 150] |
| plain 新版 | CLEAN，noted 97=97，missing=[]，extra=0，uncertain=[]，keydiff=[135, 150] |
| keycompare 旧版 p8 | mismatch 2 项 [135, 150]，均为注释项（core_noted=True, edition_noted=True） |
| keycompare 新版 p8 | mismatch 2 项 [135, 150]，均为注释项 |

- 两版 noted 数均为 97，与验证结论一致，无差异。
- 裸键 53 条（150−97）**零 mismatch**，清单与构建员声称逐项相同：
  2, 5, 6, 9, 12, 15, 16, 18, 20, 22–26, 29, 30, 35–41, 43, 45–52, 54, 61, 62, 64–66, 73, 75, 76,
  85, 86, 88, 89, 91, 97–99, 101–104。
- 135/150 印刷行逐项裁定（均为读者语言层合法重定向，沿 W43 先例）：
  - 135：核心键 `读一份日程，本身就是在了解法国。` → 分版键
    `Reading a programme is already a way of understanding France.`；
    法语题面 `Translate into English: « Lire un programme, c'est déjà comprendre la France. »` 未动，
    属翻译题答案键的读者语言重定向。
  - 150：旧版键含注释（`开放题 — 要点见写作框，范文在第 8 版写作框内` /
    `Open task — points in the writing box; model text in the MODÈLE box on this page`），
    新版键剥离注释后为 `开放题` / `Open task`；两侧均为注释项，属写作指引英文化。
  - 其余 148 键逐字相同（REG 重跑 keydiff 亦仅 [135, 150]，见 §2.5）。
- 通过条件满足：plain ∈ {CLEAN} 且 keycompare 零裸键 mismatch。plain 单用确为裸键盲区，
  本校对未单用。

### 2.4 桥接词

- 8 SVG 0 次、构建代码（`*.py`）0 次、ABSTRACT 0 次。
- KIT 1 次（第 50 行元语言合规句，见非阻塞观察 O1）。纸面（SVG）为 0。

### 2.5 登记展开（scratch 重跑 REG，非抄数字）

核心与分版 REG 各 150 题，编号 1–150 连续；页分布均为 10/15/18/18/17/18/12/42
（P2 15、P5 17、P8 42，FR 串）；级别均为 A2 53 / B1 75 / B2 22；
题型逐项相等（完成句子 49 · 单选 26 · 词汇配对 21 · 完形填空 8 · 句型转换 7 · 图表读数 6 ·
阅读判断 5 · 阅读理解 5 · 翻译 5 · 对话补全 5 · 跟练 8 · 改错 4 · 写作 1）；
页/级别/题型三元组 150/150 相等；键差异仅 [135, 150]；注释差异 137 项（中→英，属讲解层）。

### 2.6 gloss——通过（主词框 + 附属 NOTE 框全量核实）

- gloss() 调用串按 `·` 切分（scratch 构建树实测）：核心 = 分版 = P1 7 / P2 6 / P3 6 / P4 7 / P5 6 / P6 6，
  合计 38；38 项法语词头逐项冻结（分版项均以核心词头开头，仅 gloss 本地化），
  唯一提取口径注：P6 第 2 项核心 `une mission （预算）分项` 的括号内为中文 gloss，
  分版作 `une mission a (budget) heading`，法语词头 `une mission` 未动。
- 渲染 SVG 中 NOTE/译注起始框：两版均为 9 个（P1 1、P2 2、P3 1、P4 2、P5 1、P6 2、P7/P8 0），
  除 6 个主词框外另有 P2/P4/P6 各 1 个 3 项附属框，两版逐框对应、词头冻结、gloss 英文化。
- 前缀：分版 `NOTE · ` 与 W43 同配对版逐字相同（核心为 `译注｜`）。

### 2.7 金句 P7 表——通过（附口径说明）

8 句分版与核心逐字相同，页签相同：

| # | 句 | 页签 | 全版 joined-text 计数（核心 = 分版） |
|---|---|---|---|
| #1 | Le lundi 2 novembre, on reprend les cours. | page 2 | 5 |
| #2 | On ne connaît pas encore les finalistes. | page 1 | 3 |
| #3 | Les cimetières se sont remplis de chrysanthèmes. | page 3 | 1 |
| #4 | Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? | page 4 | 5 |
| #5 | Le festival se promène dans Paris. | page 5 | 1 |
| #6 | Ce calendrier peut encore bouger. | page 6 | 3 |
| #7 | Ce week-end, tout se joue. | page 1 | 1 |
| #8 | Les jeunes créateurs y rencontrent leur public, en vrai. | page 5 | 3 |

计数口径：全部 8 页文本节点以空格连接、去 `« »`、空白归一化后，句点结尾整句的子串计数；
核心与分版 8 句逐句相等，与构建员声称逐句相等（未用 JA 族的 2× 表述）。
- 词序逐字连续摘录核实（标注页原文）：8 句的词序列均在标注页正文中连续出现。
  其中 #1/#4/#6/#8 含标点逐字 exact；#2/#3/#5/#7 为句边界摘录规范化：
  #2 原文 `…on ne connaît pas encore les finalistes — ils seront connus…`（句首 on→On，破折号→句点）；
  #3 原文 `…remplis de chrysanthèmes — blancs, jaunes, violets`（破折号→句点）；
  #5 原文 `…le festival se promène dans Paris : chaque soir…`（句首 le→Le，冒号→句点）；
  #7 原文 `Ce week-end, tout se joue : les finales, la fête, la saison.`（冒号→句点）。
  此为摘录边界标点规范化，非改写，核心复校亦以此口径通过。
- #4：P4 辩论框逐字 comparatif 在位，P7 表格、B1 栏目、工具箱 B1 行均为同句；
  #8：P5 逐字句 + Q106（P7 诊所 error `rencontre` / P8 键 `rencontrent`，REG 两版一致）。
- 教学栏/工具箱重复 #1（REPRENDRE 栏 + 例句框 + 工具箱 A2）、#2（EXPRIMER L'ATTENTE 栏）、
  #4（LE COMPARATIF 栏 + 例句框 + 工具箱 B1）、#6（P7 B2 例句框）是 KIT 设计，非缺陷。

### 2.8 FR 族已裁定事实——逐项在位

- P4 `41e édition en 2026 (40e anniversaire)` 为全文唯一 `41e` 出现（P4 `LE MASTERS EN CHIFFRES` 框，
  卡面可见）；`anniversaire` 词节点 7 个，其中生日语境 6 处（P3 3、P7 诊所 1、P8 2），
  另 1 处即该版次主张本身；题号 `40.`、`140–144.`、22e（P1 扇贝节 `22e édition`）、
  15e（P5 Pitchfork，两处）均保留，两版一致。
- P6：深读小写形 `peut encore bouger, et les résultats` 未动；微习题 Q95 键 `peut` 未动；
  P7 跟练 Q102 键 `peut` 未动；P6 `« Ce calendrier peut encore bouger. »` 框两版相同。
- Q120：题干 `Si j'étais libre dimanche, j'___ à Nanterre.`、选项 `irai / irais / vais`、
  键 B、注释 `si + imparfait → conditionnel; j' = je elided` 两版同步；Q119（键 B）、Q121（键 A）不动。

### 2.9 几何——通过（canonical 审计 + 三值 + 重点测量）

- canonical `tools/occlusion_audit.py`：自检通过（6 类 planted 标记各 1 次）；
  本版 0 flags，核心 0 flags，**NEW vs core = 0**（`scratch/occlusion.json`，exit 0）。
- 全页框线扫描（外框 28/1922 × 28/2672）：本版 0 穿越，核心 0 穿越。
- 右缘扫描：advance 口径下本版与核心完全相同，仅 P8 F 组 3 行超 1885
  （advance 1891.3/1891.3/1899.6）；ink 口径下另有 P1 测验说明行 1885.05（+0.05px）与
  P2 练习说明行 1885.32（+0.32px），advance 口径均 ≤1885，距框线 37px，见观察 O3。
- **P8 F 组 3 行（重点）**：分版墨迹右缘 1891.2/1891.2/1899.5（y=1027/1103/1141），
  核心同行同值 1891.2/1891.2/1899.5（y=940/1016/1054，y 差 87 = 电池流差值，见 §2.10），
  同串、同 x=1485 起点、框线穿越 0，且 1899.5 < 内框线 1910 < 外框线 1922。
  裁定：**继承几何**，非本版缺陷；构建员“若坚持栏右缘为硬门则需动冻结法语换行、其无权擅动”
  的前提属实（核心同行同值已证实），不阻塞。
- **P7 预告条（重点，三口径并列）**：rect 底 2540.0（rect x=989 y=2270 w=896 h=270）；
  末基线 2494.0（英文末行 `Dieppe scallop fair — and your letters, at last!`）；
  墨迹底 2498.8。核心同口径：rect 完全相同（2270–2540），末基线 2466.0，墨迹底 2469.5
  （中文单行 vs 英文双行所致）。距页脚规则线 2580：rect 40px、墨迹 81.2px；
  遮挡旗 0。裁定：**2540 是框底而非墨迹**，墨迹在框内 41.2px 处收束，与核心同框，
  不含糊、不阻塞。构建员 KIT “2270–2540”即指该 rect 跨度，属实。
- P6 图表标签基线锚定覆盖（getmetrics ink_box 法，P6 y 1330–1800、x<965 的 12 个文本）：
  本版 **0.0%**，核心 0.0%，门 <30% 通过（`scratch/chart.txt`）。
- 行首 `:` 4 处与核心同页同 x 同 y 逐字相同：P3 图说、P4 微练习、P5 指南、P7 B1 栏，
  属冻结法语换行继承。
- 全页最大非页脚墨迹底：本版 P8 2541.5、P4 2541.1，其余页 ≤2515.0；距页脚线均 ≥38.5px；
  核心 P8 亦为 2541.2（同构），审计 FOOTER 0。

### 2.10 流终值（scratch 重跑日志，零 FLOW OVERFLOW / HEAD TOO WIDE）

| 流 | 分版 | 核心 | 裁定 |
|---|---|---|---|
| P1-hiver | 2298（底线 2290） | 2298 | 核心继承，卡面无压线（P1 最大墨迹底 2480.1，距线 99.9px） |
| P6-ex | 2557（底线 2540） | 2557 | 核心继承；真实 P6 最大墨迹底仅 2511.8，距线 68.2px（2557 为光标含尾隙口径） |
| P5-main | 2532（底线 2540 内） | 2502 | 未超名义底线，卡面无压线 |
| P8-battery | 1497（底线 1485，+12） | 1410 | 见下 |
| P8-keys | 2489（底线 2545 内，<2540 门） | 2167 | 见下 |
| P2-ex / P7-金句流 / P7-诊所流 | 2365 / 1574 / 2140 | 2365 / 1449 / 2140 | 均在各自底线内 |

- P8-battery 1497：为末列光标值；电池区真实最大墨迹底 1460.0（x=1451 列末行），
  在写作条规则线 1486 之上 26px，规则线穿越 0，卡面电池与写作条/MODÈLE 框分离清晰。
- P8-keys 2489：为末列（x=1451）光标值（末基线 2459.85 + 行高 + 间隙）；
  全页答案墨迹底最大值 2541.5 在 keys 流自有底线 2545 内、距页脚线 38.5px，
  核心同构（2541.2），审计无 FOOTER 旗。任务书“<2540 门”按流终值口径通过，墨迹值如实披露于此。

### 2.11 家具三方对照（W45 核心 / W43 同配对 / 本版）——一致

- 配对徽标（P1，y=574）：三方均为 22pt、#a4553a、加粗（700）、居中（x=975，middle）；
  文本：核心中文串，本版与 W43 版英文串逐字相同
  `Text in French · Explanations in English — the edition for English-speaking readers`。
  仅读者母语文字不同（另 VOL.2→VOL.3 为期号变化）。
- 页脚：本版 8/8 均为左 `Le Lucerna · FRENCH WEEKLY VOL.3 · TEXT IN FRENCH · EXPLANATIONS IN ENGLISH`、
  右 `Page N of 8`，与 W43 体例一致（核心为中文同构串）。
- gloss 前缀 `NOTE · `、P8 分隔 `— PAGE n —`、括号式 ` (note)`（半角加空格）均与 W43 同配对逐字同构
  （核心为 `译注｜` / `— 第 n 版 —` / 全角 `（note）`）。

### 2.12 读者来信角——通过（逐字摘录 + 组合规则裁定）

- 法语例信逐字冻结（两版相同）：
  `« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`
  明确标注为编辑部示例，无编造人名/信件/引言。
- 法英双语延期披露（两版法语层相同，英语层为忠实译文）：
  - 法：`Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.`
  - 英：`Editor's note: no VOL.2 texts had arrived by press time (no W44 issue), so this issue prints a labelled editorial example; VOL.4 will comment on real submissions.`
- 期号一致性：本期 VOL.3，下期 VOL.4；披露句与预告 `LA SEMAINE PROCHAINE · VOL.4 NEXT WEEK` 一致。
- “W44 未出刊”来源裁定：**核心披露中即有**（法语括号句 + 中文说明句均含此句），
  英语层是翻译而非构建员新增；真实性佐证：工作区无任何 W44 期目录、核心 KIT 明确记录
  “W44 未出刊”（W43 VOL.2 → W45 VOL.3 的期号断档亦佐证）；本校对未碰 weekly-git，
  未以仓内记录作此项证据。真实事实陈述 ≠ 编造。
- 征集句逐字：`Send us your letter for VOL.4!`（编辑部英文点评末句，祈使 + VOL.4）。
- 范围裁定（按 pt 族组合规则先例：征集句本身不必点名作文，披露句 + 预告行组合承载）：
  征集句字面覆盖来信；披露句覆盖 VOL.2 投稿顺延（`VOL.4 will comment on real submissions`）；
  预告行 `Et vos lettres, enfin !` / `and your letters, at last!` 点名来信（未字面点名 P8 最佳文本，
  如实记录）；本期 P8 写作投稿的覆盖由 P8 写作条法语原文明确承载
  （两版相同：`Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »).`）。
  三者合起来，VOL.4 承诺覆盖 VOL.2 投稿 + 本期 P8 写作投稿，构建员声称属实；
  作文经由做 P8 写作题产生、无需另行邮寄，读者不会被误导。**通过**。

### 2.13 范文 / 图片 / 摘要——通过

- 范文：P8 MODÈLE 框 7 行与核心逐字相同，空白分词 86 词（在 80–100 范围内）。
- 图片 3 张 payload 逐页 = 核心，双口径一致：
  - P1 巴黎街道老照片：base64 文本 sha 前 16 `ff20bc2bd2654cdc`，解码 JPEG sha 前 16
    `f3705af28f175ce4`，334,674 B；credit `Eugène Atget (1857-1927), photographie, domaine public` 在页。
  - P2 浮世绘：base64 前 16 `6918cb8bbe4b4bec`，解码前 16 `5b772facb5db886c`，646,242 B；
    credit `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA` 在页。
  - P3 菊花植物图谱：base64 前 16 `bfaadf5b6b912416`，解码前 16 `be071fdae81a71b4`，142,340 B；
    credit `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public` 在页。
  - 哈希口径说明：base64 文本指 SVG 内嵌 data URI 的 base64 字符串本身的 sha256；
    解码 JPEG 指 base64 解码后 JPEG 字节的 sha256；两口径均与核心相同。
- ABSTRACT：英语单行（408 字符，1 行 + 尾换行）、无 ASCII 双引号；
  真实主题关键词（Rolex Paris Masters、Peur sur le Parc、Goût du Large、Pitchfork Paris、
  2027 budget、Assemblée nationale、2–8 November 2026）+ 学习者检索短语
 （`French reading practice with 150 A2–B2 exercises`）。

### 2.14 全 8 卡目视——通过

P1–P8 逐版看图：无重叠、无压线、无出框；P1 徽标/顶栏、P2 ET VOUS/日期行、P3 图说与行首 `:`、
P4 41e 框与辩论框、P5 页底、P6 图表、P7 读者园地与预告黑带、P8 电池/写作条/答案末端均确认。
（P1–P8 卡面即交付 cards/，与 SVG 渲染一致；印刷 PDF 8 页渲染亦全部纸色。）

---

## §3 非阻塞观察（纸面正确，仅 KIT/口径文字问题，不阻塞）

- **O1**：KIT 第 50 行合规句中出现 `桥接` 1 次（“‘桥接’一词不出报”），与“ KIT 全文 0 次”的
  严格字面口径差 1；SVG、构建代码、ABSTRACT 均为 0，纸面合规。建议后续 KIT 改用“讲解”表述。
- **O2**：KIT §4 称 P8 换行重排片段 13 个，实测 freeze 多重集为 14 个（+ P3/P7 各 1 个 `）。`，
  例外总数为 16 而非 15；纸面逐项核实无误，仅 KIT 计数 stale 1。
- **O3**：KIT §5“右缘（>1885）仅 P8 F 组 3 行”在 >1885.5 阈值下成立；严格 ink >1885 口径下
  另有 P1 1885.05、P2 1885.32 两处（≤0.32px，advance 口径不超，距框线 37px），非缺陷。
- **O4**：KIT 称网页版 JPEG q72，实测嵌入 JPEG 量化表与 Pillow 默认 q75 一致（新鲜 q75 编码
  头部一致）；W43 q85 经量化表核实属实。待网页版重建时以实际参数为准，不阻塞。
- **O5**：流终值与墨迹底的口径差已在 §2.9/§2.10 如实披露（P8-keys 2489 vs 墨迹 2541.5；
  P6-ex 2557 vs 墨迹 2511.8），均非缺陷。
- **O6**：预告行字面仅点名来信、未点名 P8 最佳文本（见 §2.12）；覆盖由 P8 写作条补足，
  组合通过，已如实记录，不构成误导。
- **O7**：FR 核心网页版与本版网页版同患 §1 缺陷（核心 p1 差 107.96、p8 差 0.91），
  提请主线复查核心网页版；本校对不重开核心。

---

## §4 结论与后续

**NOT PASS**，阻塞项清单：仅 §1 一项——`Le-Lucerna-VOL3-EN-web.pdf` 第 1–7 页不可读（噪声图像）。
其余全部交付物（SVG×8、cards×8、印刷 PDF、KIT、ABSTRACT）均通过本报告所列门禁。

后续动作（主线/构建员）：

1. 仅重建网页版 PDF（用交付 cards、已验证干净的 Pillow 配方），逐页渲染复核后替换；
2. 入仓时重 pin 新网页版的 pdfBytes/pdfSha256（印刷 PDF 哈希不变）；
3. 顺带复查 FR 核心网页版是否同患 §1 缺陷；
4. 本报告的非阻塞观察 O1–O4 可在重建时顺手修正 KIT 文字，不作重审条件。
