# FR×EN（W45 VOL.3）独立校对报告 — 第二轮（网页版 PDF 修复后，全新完整校对）

**结论：ZERO PROBLEMS** —— 本轮从头独立重测全部门禁，首轮 NOT PASS 的唯一阻塞项
（网页版 PDF 第 1–7 页噪声）已修复并逐页验证干净；其余门禁全部重测通过。
本校对不宣布上架；不改源码与交付物内容；未发 Discord、未往主聊天发卡片/PDF、
未建 cron、未碰 weekly-git、未改 W43 目录（只读对照）、未派生下级代理、未清理共享 scratch。
证据目录：本目录 `scratch/`（pre/post/final 哈希、web 渲染与比对、p8/keycompare JSON、
freeze-diff、REG、occlusion JSON、几何扫描、图表覆盖、重建 PDF 流比对）。

**校对对象**：`files/weekly-report-w45-fr-en/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt），
对照 `files/weekly-report-w45-fr-core/` 与 W43 同配对版 `files/weekly-report-fr-en/`。
开工查重：`files/` 与 `hidden_files/weekly-report-w45-fr-en-build/` 无属于 fr-en 树的在途写盘
（ps 仅见本会话；终查时仅见无关分版 ko-fr 的 insert 进程，cwd 与目标均非 fr-en，
不构成 stand down）；交付最新 mtime（KIT 2026-10-28 03:56:46 UTC）后静默 >120 秒才以最终哈希定稿，
**不 stand down**。

## §0 校对过程偏差，如实披露（不改变内容结论，但主线应知）

- 本轮第一次 REG 重跑时，构建树副本已拷到本 scratch，但副本内 `content*.py` 的 `OUT`
  仍指向真实交付/核心 SVG 目录（未重定向），导致分版与核心 SVG×8 的 **mtime 被刷新为
  2026-10-28 04:00:33–36 UTC**，内容被原样重写了一遍。
- 随即核对：校对前哈希（`scratch/pre-hashes.txt`）vs 事后哈希（`post-hashes.txt`、
  最终 `post-final-hashes.txt`）**diff 为空**——字节内容逐项未变，仅 mtime 变化。
- 随后已将副本 `OUT` 重定向到本 scratch（`ed-svg/`、`core-svg/`），重跑复现 16/16 逐字节相同，
  且交付/核心 mtime 不再变化（仍停在 04:00:33–36）。此后一切重跑均只写本 scratch。
- 影响评估：入仓 pin 的是 SHA-256 而非 mtime，故对定稿内容无影响；但 mtime 已不是修复员
  留下的原始值，主线如以 mtime 作审计线索应以本节为准。本节不遮掩、不把该事件记为交付物缺陷，
  因为交付物字节经哈希证明未变。

---

## §1 修复范围核实 — 仅 2 项变化，超范围变化 0 项

逐项比对 pre-fix 基线 `hidden_files/weekly-report-w45-fr-en-build/pre-fix-webpdf-round5.sha`
（交付目录全部 20 项）：

| 项 | 结果 |
|---|---|
| SVG×8 | 全部 SAME（与基线逐字节相同） |
| cards×8 | 全部 SAME |
| 印刷 PDF `Le-Lucerna-VOL3-EN.pdf` | SAME，9,746,058 B，sha `e9fb978109ddfea4874083bc210f1e34fc378d7845b09b1c6bf248d713a7e45b` |
| ABSTRACT.txt | SAME，sha `f4fba46412c7cb4e72885b56b227dd88d5da44da2282a495dc69af6a480f9137` |
| 网页版 PDF `Le-Lucerna-VOL3-EN-web.pdf` | DIFF（预期替换）：5,310,932 B / `e390000b…` → **5,249,227 B / `16d77b11fe93a5108cbbfc616d8864aab96c97ccfece5b6f3c0afbd6e5929d7d`** |
| WEEKLY-KIT.md | DIFF（预期，§13 + q72→q75 订正）：`60edf83f…` → **`b923d9d0a9ed6c4bdddfb8fd7f1b07ca603e27943970c98b295a0f8fad6b4051`**，与修复员声称一致 |

**裁定：修复范围干净，无超范围变化。**

## §2 新网页版 PDF 逐页渲染验证 — 干净，旧噪声已消除

### 2.1 规格（与修复员声称逐项相符）

- pdfinfo：8 页，936×1296 pts，PDF 1.4，Title `Le-Lucerna-VOL3-EN-web`，5,249,227 B。
- `pdfimages -list`：8 页内嵌图像均为 JPEG、1950×2700、150 ppi。
- 提取流（`pdfimages -j`，`scratch/webimg/`）：SOF 均为 **0xC0 baseline DCT**，字节数
  p1–p8 = **668,716 / 652,975 / 601,207 / 650,731 / 540,507 / 578,319 / 663,693 / 888,639**，
  与修复员声称逐字节数一致。
- 提取流与本轮按声称配方新鲜重建的候选 PDF 流**逐字节相同（8/8，`cmp` IDENTICAL）**；
  重建文件本身与交付文件同为 5,249,227 B、流相同，全文件 SHA 不同仅因 PDF 创建时间元数据不同，
  内容流不受影响。p1 流 sha `da5e155cf950ac790457fd6fdee570521c6a15cedf56dcb5aaf38a123e49033f`
  与修复员声称、与首轮 `scratch/card1-q75.jpg`、与本轮默认编码、显式 q75 编码四者一致——
  **默认质量 = q75 得证**。

### 2.2 统一口径重测（裁定首轮 0.93 vs 修复员 9.597 的口径问题）

两者**不是同一比对方法**，本轮以同一套方法对 8 页并列两种口径，结论不再依赖抄数字：

- 口径 A（全分辨率逐像素平均绝对差，pdftoppm -r 150 渲染 1950×2700 vs 卡片）：
  修复员声称的 6.388 / 6.228 / 5.773 / 6.335 / 5.141 / 5.452 / 6.562 / 9.597
  **与本轮实测逐页精确一致**。
- 口径 B（下采样：提取 JPEG 与卡片均缩至 195×270 后逐像素平均绝对差）：
  本轮 p1–p8 = **0.687 / 0.689 / 0.687 / 0.700 / 0.710 / 0.715 / 0.716 / 0.730**，
  与修复员声称的 0.687–0.730 逐页一致。
- 首轮 p8 的 0.93 属于口径 B 一类（下采样），与修复员的 9.597（口径 A）不可直接比较；
  本轮口径 B 的 p8 为 0.730，与首轮 0.93 同为 ~1 量级（差值来自重采样实现细节，不影响量级结论）。

### 2.3 逐页报告（本轮实测）

| 页 | 渲染均值 RGB | 卡片均值 RGB | 口径 A 全分辨率差 | 口径 B 下采样差 | 判定 |
|---|---|---|---|---|---|
| p1 | (219.4, 214.0, 199.1) | (219.7, 214.1, 200.2) | 6.388 | 0.687 | 干净 |
| p2 | (226.9, 221.4, 205.8) | (227.0, 221.5, 206.9) | 6.228 | 0.689 | 干净 |
| p3 | (230.0, 224.5, 209.1) | (230.1, 224.7, 210.1) | 5.773 | 0.687 | 干净 |
| p4 | (229.6, 224.0, 208.2) | (229.8, 224.1, 209.3) | 6.335 | 0.700 | 干净 |
| p5 | (232.4, 226.9, 211.6) | (232.5, 227.0, 212.7) | 5.141 | 0.710 | 干净 |
| p6 | (231.9, 226.2, 210.8) | (231.9, 226.2, 211.9) | 5.452 | 0.715 | 干净 |
| p7 | (222.0, 216.7, 201.5) | (222.2, 216.8, 202.7) | 6.562 | 0.716 | 干净 |
| p8 | (226.7, 221.1, 205.5) | (227.1, 221.4, 206.8) | 9.597 | 0.730 | 干净（参照页） |

**干净标准裁定：p1–p7 在口径 A 上均低于参照页 p8（5.1–6.6 < 9.597），
在口径 B 上与 p8 同属 0.69–0.73 的紧密簇；旧版 p1–p7 同口径为 100 量级噪声。
p1 渲染图目视（`scratch/webrender/pg-1.png`）与卡片 p1 逐行一致，无块状噪声。
首轮阻塞项已消除。** 印刷 PDF 8 页 72 dpi 渲染均值亦全部纸色（与卡片均值差 <0.2）。

## §3 KIT 核实 — §13 完整，q72→q75 订正彻底

- §13 含：触发（首轮 NOT PASS §1）、pre-fix 基线文件、修复范围、旧版字节数/SHA
  （5,310,932 / `e390000b…`）、新版字节数/SHA（5,249,227 / `16d77b11…`）、
  规格（8 页、936×1296、PDF 1.4、Title）、配方（venv Python 3.12.3 / Pillow 13.0.0、
  `save_all`、resolution=150.0、未显式传 quality）、验证值（pdfinfo、流字节数、
  全分辨率与下采样差值、交付流与候选流逐字节相同）、未改动文件比对、
  **根因结论“未查明”**（见 §4）、状态（仍为 builder-complete，NOT finalized）。
- q72 残留：全文 `q72` 出现 **4 次，全部位于“原 KIT 误记 q72，2026-10-27 网页版重建时订正”
  的订正注记中**（§8、§10 第 6 项、§12 第 4 项、§13 修复范围句）；现行主张 11 处 `q75`
  全部为 q75，无任何现行 q72 主张。**订正彻底。**
- KIT 新 SHA `b923d9d0…` 实测全值 `b923d9d0a9ed6c4bdddfb8fd7f1b07ca603e27943970c98b295a0f8fad6b4051`，相符。
- KIT 头仍为 builder-complete，NOT finalized，未擅自宣布上架。

## §4 根因诚实记录与裁定

- **如实转述：根因未查明。** 构建树与 `tools/` 均无网页版生成脚本，构建日志只记录 SVG 流，
  原始生成命令无法从产物反推；旧 p8 虽像素干净，其流字节数 855,389 亦不同于新鲜编码 888,639，
  即旧文件各页流普遍非新鲜卡片编码；p1–p7 流为何不是卡片编码，未查明——本报告不编造原因。
- **裁定：根因未查明不影响本次定稿。** 理由：新文件并非对旧文件的修补，而是用交付卡片
  按已验证配方全新重建，且本轮独立验证已闭环——8 页提取流与新鲜编码逐字节相同、
  8 页渲染与卡片逐页比对干净、SVG/卡片/印刷 PDF 经 pre-fix 基线证明未动。
  未查明的是旧文件的生成史，不是新文件的内容正确性；新文件的内容正确性不依赖根因。
- 另：FR 核心网页版同患旧缺陷的 O7 提醒仍转交主线（本轮未重开核心，仅记录核心网页版
  现值：8 页、936×1296、5,257,574 B，供主线复查时对照）。

## §5 全部门禁重测（首轮通过项全部重测，非沿用结论）

### 5.1 冻结：核心基线 8/8；法语正文零删失

- 核心 SVG 现哈希与构建树 `core-prebuild.sha` **8/8 OK**。
- 重定向后的 scratch 重跑：核心与分版构建树各重渲染 8 SVG，与交付物 **16/16 逐字节相同**。
- `tools/freeze.py diff`：P1 +23/−23、P2 +37/−34、P3 +37/−34、P4 +41/−37、P5 +33/−30、
  P6 +30/−27、P7 +43/−35、P8 +140/−119（求和口径，与首轮逐页一致；新旧 freeze JSON
  仅路径写法相对/绝对之差，内容相同）；新增 CJK 字符 **0**，分版 8 页 SVG 文本节点 CJK **均为 0**。
- 移除的非 CJK 串逐项核实，全部属于两类例外，无法语键丢失：P3/P7 各 1 个 `）。`
  （中文讲解段落换行尾标点）；P8 换行重排片段的法语键经逐句核对均在分版 P8 存活
  （如 135 题法语句、119./120. 键、132./137./138./139. 句、16./17./18. 句）。

### 5.2 P8 双门法（FR 族专属，BINDING）——通过

当前 `tools/p8.py` 即已采纳新版，sha `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`：

| 工具 | 结果 |
|---|---|
| plain（当前 tools/p8.py） | **CLEAN，noted 97=97**，missing=[]，extra=0，uncertain=[]，keydiff=[135, 150] |
| keycompare（`hidden_files/w45/p8-fr-gap-fix/keycompare.py`，全 150 键） | mismatch 2 项 [135, 150]，均为注释项（core_noted=True, edition_noted=True） |

- 裸键 53 条（150−97）**零 mismatch**，清单：2, 5, 6, 9, 12, 15, 16, 18, 20, 22–26, 29, 30,
  35–41, 43, 45–52, 54, 61, 62, 64–66, 73, 75, 76, 85, 86, 88, 89, 91, 97–99, 101–104。
- 135/150 印刷行裁定（均为读者语言层合法重定向，沿 W43 先例）：
  - 135：核心键 `读一份日程，本身就是在了解法国。` → 分版键
    `Reading a programme is already a way of understanding France.`；
    法语题面 `Translate into English: « Lire un programme, c'est déjà comprendre la France. »` 未动；
    P8 卡面印刷行与此一致。
  - 150：两侧均为注释项；分版印刷行 `150. Open task — points in the writing box;
    model text in the MODÈLE box on this page`，属写作指引英文化。
  - 其余 148 键逐字相同（REG keydiff 亦仅 [135, 150]）。
- 通过条件满足：plain ∈ {CLEAN} 且 keycompare 零裸键 mismatch。

### 5.3 gloss、登记、金句、已裁定事实

- gloss：content 模块 gloss() 调用串按 `·` 切分，核心 = 分版 =
  **P1 7 / P2 6 / P3 6 / P4 7 / P5 6 / P6 6，合计 38**；38 项法语词头逐项冻结
  （P6 第 2 项 `une mission` 词头未动，gloss 由中文 `（预算）分项` 本地化为 `a (budget) heading`）。
  渲染 SVG 中 `NOTE · ` 起始框两版均为 9 个（P1 1、P2 2、P3 1、P4 2、P5 1、P6 2、P7/P8 0）。
- 登记展开（scratch 重跑 REG）：核心与分版各 150 题，编号 1–150 连续；
  页分布 **10/15/18/18/17/18/12/42**；级别 **A2 53 / B1 75 / B2 22**；
  题型逐项相等；页/级别/题型三元组 150/150 相等；键差异仅 [135, 150]；
  注释差异 137 项（中→英，属讲解层）。
- 金句：8 句核心 = 分版逐字相同，全版 joined-text 计数
  **#1=5、#2=3、#3=1、#4=5、#5=1、#6=3、#7=1、#8=3**，与首轮一致；
  页签核实：#1（p2）、#4（p4）、#6（p6）、#8（p5）为原页逐字连续句；
  #2/#3/#5/#7 的原页正文为句边界摘录规范化（破折号/冒号→句点、句首大小写），
  与首轮口径相同，非改写。#4 辩论框逐字 comparatif 在位；#8 + Q106
  （P7 诊所 error `rencontre` / P8 键 `rencontrent`，REG 两版一致）在位。
- FR 族已裁定事实：P4 `41e édition en 2026 (40e anniversaire)` 全文唯一（`41e` 计数 1）；
  `anniversaire` 词节点 7 个；P6 小写形 `peut encore bouger, et les résultats` 未动，
  Q95 键 `peut`、Q102 键 `peut` 未动；Q120 题干/选项 `irai / irais / vais`/键 B/
  注释 `si + imparfait → conditionnel; j' = je elided` 同步，Q119 键 B、Q121 键 A 不动。
  （Q120 注释在 REG 中为英文版；核心原注释为中文同义，此为讲解层本地化，非键改动。）

### 5.4 桥接词 — 0（纸面），KIT 元语言句裁定

- 8 SVG **0 次**、构建代码（`*.py`）**0 次**、ABSTRACT **0 次**。
- KIT 第 50 行仍含 `桥接` 1 次，原文为元语言合规句：“‘桥接’一词不出报
  （SVG grep = 0；本 KIT 此句仅为合规记录，不属于版面）”。
- **裁定：该处为检测器/元语言句而非交付物违规。** 参照 fr-de 校对对 `checks.py:73` 的处理
  （检测器自身字符串不计）：该句讨论的是合规规则本身，不出现在任何版面、讲解或读者可见文本中；
  纸面（SVG）为 0，门禁通过。建议后续 KIT 改用“讲解”表述以避字面扫描误报（非阻塞观察）。

### 5.5 几何 — 通过

- canonical `tools/occlusion_audit.py`：自检通过（6 类 planted 标记各 1 次）；
  本版 **0 flags**，核心 0 flags，**NEW vs core = 0**（exit 0）。
- 全页框线扫描（外框 28/1922 × 28/2672）：本版 0 穿越，核心 0 穿越。
- ADVANCE 全页右缘扫描（>1885，非页脚）：本版与核心完全相同，仅 P8 F 组 3 行
  （advance 1891.3 / 1891.3 / 1899.6）；ink 口径下另有 P1（显示 1885.0）与 P2（1885.3）两处
  （超幅 ≤0.3px 量级，advance 口径不超，距框线 37px，属首轮 O3 已记录的口径差，非缺陷）。
- P8 F 组 3 行：分版墨迹右缘 **1891.2 / 1891.2 / 1899.5**（y=1027/1103/1141），
  核心同行同值（y=940/1016/1054，y 差 87 为电池流差值），同串、同 x=1485 起点、
  框线穿越 0，且 < 内框线 1910。**继承几何，非本版缺陷。**
- P6 图表标签基线锚定覆盖：本版 **0.0%**，核心 0.0%，门 <30% 通过（12 个文本）。
- 行首 `:` 4 处与核心同页同 x 同 y 逐字相同（P3 图说、P4 微练习、P5 指南、P7 B1 栏），属冻结继承。
- P8 答案流末端 **2489**（<2540 门，底线 2545 内）；全页最大非页脚墨迹底：
  本版 P8 2541.5、P4 2541.1，其余页 ≤2515.0，距页脚线均 ≥38.5px；核心 P8 亦为 2541.2（同构）。
- P7 预告条三口径并列：rect 底 **2540.0**（rect x=989 y=2270 w=896 h=270）；
  末基线 **2494.0**（英文末行 `Dieppe scallop fair — and your letters, at last!`）；
  墨迹底 **2498.8**。核心同口径：rect 完全相同（2270–2540），末基线 2466.0，墨迹底 2469.5
  （中文单行 vs 英文双行所致）。距页脚规则线 2580：rect 40px、墨迹 81.2px；遮挡旗 0。
  **2540 是框底而非墨迹**，不阻塞。
- 流终值（scratch 重跑日志，零 FLOW OVERFLOW / HEAD TOO WIDE）：
  P1-hiver 2298、P6-ex 2557（均与核心逐字相同，属核心继承）、P5-main 2532（核心 2502）、
  P8-battery 1497（核心 1410；末列光标值，电池区真实最大墨迹底在写作条规则线 1486 之上）、
  P8-keys 2489（核心 2167）、P2-ex 2365、P7-金句流 1574、P7-诊所流 2140，均在各自底线内或如实披露。

### 5.6 家具三方对照（W45 核心 / W43 同配对 / 本版）——一致

- 配对徽标（P1，y=574）：三方均为 **22pt、#a4553a、加粗（700）、居中（x=975，middle）**；
  文本：本版与 W43 版英文串逐字相同
  `Text in French · Explanations in English — the edition for English-speaking readers`
  （核心为中文同构串）。
- 页脚：本版 8/8 均为左 `Le Lucerna · FRENCH WEEKLY VOL.3 · TEXT IN FRENCH · EXPLANATIONS IN ENGLISH`、
  右 `Page N of 8`，与 W43 体例一致（核心为中文同构串）。
- gloss 前缀 `NOTE · `：本版 9 框、W43 9 框，核心为 `译注｜`。
- P8 分隔 `— PAGE n —`：本版与 W43 均为 1–8 全套；核心为 `— 第 n 版 —`。
- 括号式：本版与 W43 均全程使用半角括号（本版 P8 半角 `(` 124 次、全角 `（` 0 次；
  W43 半角 96 次、全角 0 次），核心使用全角（108 次）。
  注：三版 P8 均无字面字符串 `(note`；首轮“括号式 ` (note)`”应理解为半角括号注释体例，
  而非字面词——本轮按实际字符核实，体例同构结论不变。

### 5.7 读者来信角 — 通过（组合规则）

- 法语例信逐字冻结（两版相同）：
  `« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`
  明确标注为编辑部示例，无编造人名/信件/引言。
- 法英双语延期披露（两版法语层相同，英语层为忠实译文）：
  法 `Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.`；
  英 `Editor's note: no VOL.2 texts had arrived by press time (no W44 issue), so this issue prints a labelled editorial example; VOL.4 will comment on real submissions.`
- “W44 未出刊”核实为核心披露中即有（法语括号句 + 中文说明句均含此句），英语层是翻译而非新增，
  属真实陈述非编造；本校对未碰 weekly-git，未以仓内记录作此项证据。
- 征集句逐字：`Send us your letter for VOL.4!`（编辑部英文点评末句）。
- 范围裁定（按 pt 族组合规则）：征集句字面覆盖来信；披露句覆盖 VOL.2 投稿顺延
  （`VOL.4 will comment on real submissions`）；预告行 `Et vos lettres, enfin !` /
  `and your letters, at last!` 点名来信（字面未点名 P8 最佳文本，如实记录）；
  本期 P8 写作投稿的覆盖由 P8 写作条法语原文明确承载
  （两版相同：`Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »).`）。
  三者合起来，VOL.4 承诺覆盖 VOL.2 投稿 + 本期 P8 写作投稿。**通过。**

### 5.8 范文 / 图片 / 摘要 / 印刷 PDF / 全 8 卡目视

- 范文：P8 MODÈLE 框 7 行与核心逐字相同，空白分词 **86 词**（在 80–100 范围内）。
- 图片 3 张 payload = 核心，双口径一致：
  P1 巴黎街道老照片 base64 sha 前 16 `ff20bc2bd2654cdc`、解码 JPEG sha 前 16 `f3705af28f175ce4`、334,674 B，
  credit `Eugène Atget (1857-1927), photographie, domaine public` 在页；
  P2 浮世绘 base64 前 16 `6918cb8bbe4b4bec`、解码前 16 `5b772facb5db886c`、646,242 B，
  credit `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA` 在页；
  P3 菊花植物图谱 base64 前 16 `bfaadf5b6b912416`、解码前 16 `be071fdae81a71b4`、142,340 B，
  credit `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public` 在页。
- ABSTRACT：英语单行（409 字符含尾换行，1 行 + 尾换行）、无 ASCII 双引号；
  真实主题关键词 + 学习者检索短语（`French reading practice with 150 A2–B2 exercises`）。
- 印刷 PDF：8 页，1462.5×2025 pts，9,746,058 B，文字层正常（首行 `VOL. 3 · ISSUE NO. 3`），
  8 页渲染全部纸色。
- 全 8 卡目视：P1–P8 逐版看图，无重叠、无压线、无出框；P1 徽标/顶栏、P2 ET VOUS/日期行、
  P3 图说与行首 `:`、P4 41e 框与辩论框、P5 页底、P6 图表、P7 读者园地与预告黑带、
  P8 电池/写作条/答案末端均确认。
- 校对前后交付物 + 核心哈希 diff 为空（`scratch/pre-hashes.txt` vs `post-final-hashes.txt`），
  仅 §0 所述 mtime 变化（字节无变化）；pre-fix 基线比对除网页版 PDF + KIT 两项预期变化外亦为空。

## §6 非阻塞观察（纸面正确，仅文字/口径说明，不阻塞）

- O1（沿用首轮）：KIT 第 50 行元语言句含 `桥接` 1 次，见 §5.4 裁定；建议后续改用“讲解”表述。
- O2（沿用首轮）：KIT §4 称 P8 换行重排片段 13 个，实测 freeze 多重集求和为 14 个
  （+ P3/P7 各 1 个 `）。`），例外总数为 16 而非 15；纸面逐项核实无误，仅 KIT 计数 stale 1。
- O3（沿用首轮）：KIT §5“右缘（>1885）仅 P8 F 组 3 行”在 advance 口径下成立；
  严格 ink >1885 口径下另有 P1、P2 两处 ≤0.32px，非缺陷。
- O4：首轮“括号式 ` (note)`”的表述应读作半角括号注释体例（见 §5.6 注），三版均无字面 `(note` 串。
- O5：FR 核心网页版同患旧噪声缺陷的提醒仍待主线复查；本校对不重开核心。
- O6：本轮 §0 的 mtime 刷新事件（字节未变）已在 §0 完整披露，主线如需恢复原始 mtime
  可自行决定，本校对不擅自改动交付物时间戳以外的任何内容。

## §7 结论

**ZERO PROBLEMS。** 阻塞项清单：无。

后续动作（主线）：入仓时重 pin 新网页版的 pdfBytes/pdfSha256
（5,249,227 / `16d77b11fe93a5108cbbfc616d8864aab96c97ccfece5b6f3c0afbd6e5929d7d`），
印刷 PDF 哈希不变；顺带复查 FR 核心网页版是否同患旧噪声缺陷。
本报告不宣布上架。
