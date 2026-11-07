# 独立校对报告 — Lucerna Weekly W45 NL×FR（荷兰语 × 法语）

**结论：ZERO PROBLEMS（可定稿）**

- 校对对象：`files/weekly-report-w45-nl-fr/`（SVG×8、卡片×8、印刷 PDF、网页 PDF、`WEEKLY-KIT.md`、`ABSTRACT.txt`）
- 对照核心：`files/weekly-report-w45-nl-core/`（VOL.2，masthead De Lucerna；中文讲解层核心，即 NL×ZH-CN  pairing 的核心）
- 家具对照：W43 已发同配对版 `files/weekly-report-nl-fr/`（实测 SVG）
- SOP：`files/weekly-report-SOP.md`；工具：`tools/`（`tools/README.md` #7–#22 已读；全部复测均用 `tools/venv/bin/python` 跑 `freeze.py` / `p8.py` / `occlusion_audit.py`，另加自写墨迹扫描，不采信构建员自述）
- 本校对只读不改：未改源码、未动核心/W43/分版目录、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git。校对工作文件仅见本目录（`hidden_files/w45/nl-fr-proof/`）及 `tools/scratch/proof-nlfr-baseline/`（freeze 基线复现的临时拷贝）。
- 开工查重：首次检查时分版最新 mtime 为 21:31:51 UTC，无进行中渲染进程；90 秒复查零新写盘后开工（完成交付的新鲜时间戳不作 stand-down 理由）。

## 必查门实测

### 门 1 — Freeze（通过）

- 核心基线复现：`freeze.py baseline`（核心构建目录 `hidden_files/weekly-report-w45-nl-build`）**8/8 字节复现**；运行前后核心 SVG 重哈希一致，核心未动（见文末哈希复核）。
- 冻结差分：`freeze.py diff --strict-cjk` 退出 0；分版 CJK 每页均为 0，核心每页 CJK 为 191 / 212 / 153 / 126 / 214 / 192 / 373 / 1033（与构建员称的核心计数逐页一致）；**新增 CJK 字符总数 0**；全文“桥接”0；间隔引号（`« ` / ` »`）0；文本节点内双空格 0。
- 删除串逐项裁定（freeze diff 全部 removed 字符串已逐条过目）：
  - 绝大多数含 CJK，属讲解层（中文译注/说明/题干提示/页眉副标/页脚/答案注）被法语讲解层替换，合法。
  - 仅 7 条非 CJK 删除串，逐项裁定如下，全部不是荷兰语正文删除：
    - P6 `）`：中文括号注脚换行残片，讲解层碎片。
    - P7 `bomen。` / `thuis。` / `zij zette vast。` / `。`：换行切分伪影——核心中这些荷兰语词因后随中文注脚标点而单独成节点；分版中同一荷兰语句子完整保留（`Singulier : een boom ; pluriel : bomen.`、`blijf ik thuis.`、`vastzetten : bien fixer, zij zette vast.`），仅切分方式随注脚语言改变。
    - P8 `voorgelezen`：核心中该词因换行单独成节点；分版第 41 条整行 `hebben voorgelezen — parfait de voorlezen : hebben voorgelezen` 中出现两次，保留。
    - P8 `104. blijf — rood = blijf binnen`：核心第 104 条的注文本身就是荷兰语短语（讲解层注脚），分版键 `blijf` 不变、注改为法语 `code rouge = restez à l'intérieur`，属讲解层本地化。
  - 新增串（P7/P8 已逐条过目）：全部为法语讲解层/家具，或荷兰语冻结键句因注脚语言改变而整节点重现（键句本身与核心逐字节相同，如 133–136、139、140、97–99 的荷兰语句）；无新增荷兰语文章、练习或事实。

### 门 2 — 核心层冻结专项：P7 词框定义句（通过）

- 核心原文（`weekly-report-w45-nl-core/svg/p7-taal.svg`，三行拼接）：
  > «meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.
- 本版实测（`weekly-report-w45-nl-fr/svg/p7-taal.svg`，三行拼接）：
  > «meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.
- 两者**逐字节相同**；仅其下讲解行本地化（核心 `meedoen = 参加、参与：气候周全荷兰都参 加。` → 本版 `meedoen = participer.`）。
- NL×ZH-CN 核心对照结果：对照对象即上述中文讲解层核心（W45 NL 核心），定义句逐字保留、无删改、无译成法语；PAS OP 诊所的荷兰语正误句亦逐字保留，仅第三行注脚译为法语。**无阻塞问题。**

### 门 3 — P8（通过）

- `p8.py compare`（显式 P8 路径，total 150）：核心 150 noted，分版 150 noted，状态 **CLEAN**，missing []、extra 0、uncertain []，keydiff **[7, 17, 70, 71, 76, 96, 137, 138, 148]**，与构建员称的列表一致。
- 逐项独立核实（对照两版 P8 印刷行原文）：
  - 提取伪影（印刷键逐字节相同、仅译注语言不同），通过：7（键 `B`）、17（`wortelen`）、70（`eiland`）、71（`proef`）、76（`gaat winnen`）、96（`advies`）、148（`B`）。另：104 未进 keydiff，键 `blijf` 两版相同，仅注由荷兰语短语改为法语，属讲解层，印证伪影机制。
  - 真实重定向（合法重定向理由成立），通过：137、138。两版练习题干荷兰语原文相同（137 `De Klimaatweek duurt zeven dagen. → ___`；138 `Code oranje betekent: bereid je voor. → ___`），仅翻译目标语由中文改为法语，故答案键由中文句变为法语句（137 `La Semaine du climat dure sept jours.`；138 `Le code orange signifie : préparez-vous.`），符合翻译题重定向规则。
  - 反向重定向不在 keydiff，核实成立：139、140 题干方向互换（核心题干中文 → 本版题干法语：139 `La Nuit des musées dure de 19 heures à 2 heures du matin. → ___`；140 `Je participe à la Semaine du climat. → ___`），答案键荷兰语句逐字节相同（139 `Museumnacht duurt van 19:00 uur tot 02:00 uur.`；140 `Ik doe mee aan de Klimaatweek.`），故不在 keydiff，合理。
  - 第 150 条为范文题指针（87 词范文荷兰语正文与核心一致），非键变更。

### 门 4 — 几何遮挡审计（通过）

- `occlusion_audit.py`（自检先通过，6 类 planted 全触发、干净对照静默）：分版 **0 flags**、核心 **0 flags**、NEW vs 核心 **0**。
- 同基线墨迹碰撞扫描（自写 PIL/FreeType 墨迹扫描，全 8 页同基线分组）：
  - 分版全页仅 1 处间隙 < 2px：P1 目录行 y=1436，`Musea bij nacht en boeken` 与等级 `A2→B1`。
  - 4× 超采样精测（与审计工具同方法）：标题墨迹止于 x=1799.50，等级墨迹起于 x=1799.71，**墨迹间隙 +0.21px，分离未重叠**（1× 扫描的 −1.05px 为像素量化伪影，不作数）。
  - 核心同款：核心 P1 同行同坐标同字号同文本，扫描结果相同；两版该区域卡片裁图 SHA256 相同（`800d9e73…`），像素级一致，确为核心继承。
  - 卡面目视：裁图放大确认 `boeken` 与 `A2→B1` 字形分离、无叠印、无糊连，可读。
- P1 词 gloss / 规则线几何（4× 超采样实测）：规则线 y=1853（线宽 1.2，带 1852.4–1853.6）；gloss 第 1 行墨迹 1829.8–1851.0，第 2 行 1856.7–1875.7（构建员称 1829.3–1851.3 / 1855.9–1875.9，差值 < 1px 属测量方法舍入，结论相同）；规则线穿过两行间隙，**触及 neither 行墨迹**，通过。
- 图表标签覆盖检查（P6，墨迹框 × 全部条形矩形交集实测）：4 标签 + 4 数值 + 图题共 9 项，**覆盖率全部 0.0%**（< 30% 阈值）；数值 45 / 25 / 20 / 10 合计 100，标签与条形在 y 向/x 向均无交集；图题 `DE GRAFIEK · DONNÉES D'ESSAI` 同样 0.0%。OEFENDATA 标注荷兰语原文与法语说明均已排版。

### 门 5 — Gloss（通过）

- 按渲染后 `gloss()` 字符串本身以 `·` 拆分计数（构建代码实测，头词顺序与核心一致）：
  - P2：6 = 6（het klimaat / wortelen / besparen / de verwarming / de waarschuwing / lokaal）
  - P3：5 = 5（het museum / de rondleiding / het tijdslot / tweedehands / de beurs）
  - P4：5 = 5（de balans / gelijkspelen / de speelronde / de topper / de stand）
  - P5：5 = 5（het eiland / de proef / stemmen / de aflevering / voorbij）
  - P6：5 = 5（de meteoroloog / waarschuwingsmoeheid / vastzetten / het advies / de voorstander）
- 渲染后 SVG 核查：上述全部头词在对应页渲染文本中均存在。
- P7 桥接：A2 4 项 / B1 3 项 / B2 3 项，计数与核心一致，头词与核心一致。

### 门 6 — P7 金句（通过）

- 8 句荷兰语原文与核心逐字相同，页码标签分布与核心一致：**Pagina 1、1、2、3、4、5、6、6**。
- 全版计数实测（空格拼接全文检索）：每句恰 **2×**（标注源页 1× + P7 1×），无多无少：
  - P1：`Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland`、`De herfst is de beste tijd om te planten`
  - P2：`Geel betekent: let op, het weer kan gevaarlijk zijn`
  - P3：`Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts`
  - P4：`Ajax won donderdag 22 oktober met 2–0 van Atalanta`
  - P5：`Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur`
  - P6：`Een code is geen verbod, maar een advies`、`Het weer is van ons allemaal, maar het raakt ons allemaal anders`
- 每句均在其标注源页全文中完整出现；P7 短语（金句）逐字取自本期文章、页码标签正确。

### 门 7 — 读者园地（通过，不编造）

- 页上三事实齐全（荷兰语披露 + 法语披露双语呈现）：
  1. 无真实来信：`Ter perse: nog geen echte brieven … binnen` / `Aucune vraie lettre … reçu`
  2. 无最佳 P8 作文：`… of beste pagina-8-teksten binnen` / `… ni meilleur texte de page 8 reçu`
  3. 示例 + VOL.3 承诺：`daarom dit voorbeeld; belofte naar VOL.3.` / `voici cet exemple ; promesse reportée au VOL.3.`
- 显性法语公开征集邀请（独立判定：构成显性邀请）：
  > Exemple de la rédaction. Envoyez vos vraies lettres et textes de page 8 : nous les publierons dans le VOL.3 !
  - 判定理由：第二人称祈使 `Envoyez vos vraies lettres…` 直接向全体读者发出投稿行动号召，并附刊登承诺 `nous les publierons dans le VOL.3 !`；与内容预告行（VOLGENDE WEEK 栏，158–159 行）和其他页练习提示（EN JIJ 栏）在措辞、对象、承诺上均不同，不属后两者。
- 示例处理裁定：核心的 Li 示例逐字保留（`«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)`，与核心 P7 节点逐字相同），**未**按 W43 那样本地化为 Camille/Parijs。
  - 裁定理由（就事论事，不以“W43 如此”放行或否定）：该示例是核心自带的、已明确标注为编辑部示例的内容项，保留它既满足冻结门（核心内容不动），又满足不编造门（标注为示例，不主张真实读者/真实来信）；新造一个 Camille/Parijs 人名地名反而是在示例上叠加新的虚构身份信息，并无不编造门上的收益。家具规则只管家具（徽章/页脚/字号等排版项），不管内容本地化选择，故本项以冻结 + 不编造两门判定为合规。法语征集句首的 `Exemple de la rédaction` 进一步强化了示例属性。

### 门 8 — 家具三方对照（通过，W43 实测为准）

逐元素对照 W43 已发 `weekly-report-nl-fr/svg/p1-voorpagina.svg` 实测：

| 元素 | W43 实测 | 本版实测 | 判定 |
|---|---|---|---|
| 配对徽章文本 | `TEXTES EN NÉERLANDAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES` | 逐字节相同 | 一致 |
| 徽章槽位/字号/粗细/颜色/字体 | x=975, y=568, 20pt, 700, BRICK #a4553a, Noto Sans CJK SC, 居中；实测宽 1058.8px | 全部相同（宽同为 1058.8px） | 一致 |
| 徽章家族情形 | strapline 保留于 y=372，徽章插入 y=568（暗带止于 542，标题栏起于 606 之间） | 同样：strapline y=372 逐字保留，徽章 y=568 | W43 家族情形，非 EN 同胞 strapline 替换 |
| strapline | `DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS`，y=372, 19pt, 灰 #57523f | 逐字、逐属性相同（亦与核心同行一致） | 一致 |
| 副标题 | y=330, 36pt（W43 长串，实测 advance 1734.9px） | y=330, **40pt**，实测 advance 1766.8px ≤ 1820 内宽，墨迹宽 1769px，居中后约 90–1860px，落在内边 65–1885 内 | 通过：字号差异由串长驱动，核心副标题本就是 40pt；本版串更短，40pt 仍 fit，非家具违规 |
| 顶栏中部 | y=92, 21pt，`ELKE WEEK IN HET NEDERLANDS · CHAQUE SEMAINE EN NÉERLANDAIS` | 逐字、逐属性相同 | 一致 |
| 顶栏左/右 | 左 `VOL. 1 · EERSTE EDITIE`；右当周荷兰语日期 | 左 `VOL. 2`（卷次变更，预期内）；右 `WEEK VAN 2 TOT EN MET 8 NOVEMBER 2026`（本期日期，荷兰语，预期内） | 一致（卷次/日期除外，均为预期变更） |
| 页脚（8/8 页） | `De Lucerna · HEBDOMADAIRE NÉERLANDAIS VOL.1 · TEXTE EN NÉERLANDAIS · EXPLICATIONS EN FRANÇAIS`，基线 2624，20pt 灰，`Page n sur 8` | W43 形式仅 VOL.1 → VOL.2，8/8 页齐全，页码 1–8 连续 | 一致 |
| Gloss 前缀 | `Note — `（P1 词 gloss 为 `Notes — `） | P2/P3 实测 `Note — `，P1 `Notes — `，`Note | ` 0 | 一致 |
| 暗带/标题栏几何 | 暗带 y=424 高 118（止于 542） | 相同；徽章 y=568 落在暗带与 606 标题栏之间 | 一致 |

凡与 W43 实测不符者：除上表已说明的卷次、日期、副标题字号（均有实测依据）外，**无**。

### 门 9 — PDF / 卡片（通过）

- 双 PDF 各 **8 页**：印刷 PDF `De-Lucerna-VOL2-FR.pdf` 7,939,994 B，sha256 `b3368d87d897977b089dbdda2ade9b9951a27aacf3f2421422169e1d999be4b1`；网页 PDF `De-Lucerna-VOL2-FR-web.pdf` 3,679,467 B，sha256 `db2423c9265b923103d38b34d6bbe7a307b368d7c902888e3a03feb707e49439`；尺寸与 SHA 与 KIT §12 一致；网页 PDF < 10 MB。
- SVG 与卡片 SHA 与 KIT §12 逐项核对一致（8 SVG + 8 卡片全对）。
- 卡片 8 张全部目视（1950×2700）：P1 徽章行/目录行/词 gloss/照片署名/闪电问答；P2 代码色块/配对集；P3 照片/gloss 框/练习 29–46；P4 标题 tally/照片署名折行/练习 47–64；P5 观看框括号/练习 65–82；P6 图表/练习 83–100；P7 三栏栈/词框/读者园地/金句/预告；P8 练习 113–150/答案键至 150/范文。**无重叠、无截断、无缺陷**（P4/P6 中栏下部留白为核心同款版式留白，非缺陷）。
- 题量与等级：练习骨架与核心逐项相同——P1 1–10（10）、P2 11–28 含 25–28 配对组（18）、P3 29–46（18）、P4 47–64（18；另有一 `0–2.` 赛程残片非练习题，核心同款）、P5 65–82（18）、P6 83–100（18）、P7 101–112（12）、P8 113–150（38），合计 **150 题**；P8 印刷答案集 150=150（门 3）；SVG 可恢复的等级 token 分布与核心逐页相同（其余组题/节末题的等级载于节标题，与核心一致），故等级分布与核心一致（A2 47 / B1 72 / B2 31，核心 KIT 实测值）。
- ABSTRACT：法语单行（356 字节，含结尾换行），无 ASCII 双引号；含真实主题关键词（Semaine du climat、Nuit des musées d'Amsterdam、Crossing Border Festival、12e journée d'Eredivisie、Expeditie Robinson）与学习者搜索短语（`apprendre le néerlandais en lisant l'actualité`），并含 masthead、目标语、VOL.2、150 题、A2–B2、法语讲解。
- 图片署名行与核心一致且确已排版：P1 `Foto: Vovogov90 — CC0`、P2 `Foto: Nationaal Archief — CC0`、P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`、P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek` + `domein`（折行与核心相同）；`<image>` 计数 P1–P4 各 1、P5–P8 各 0，与核心相同。

## 问题清单

无。上述 9 门全部通过，**无编号问题**。

## 附注（方法透明度）

- 校对中一次自写核查脚本曾因分支条件误读核心文件作分版（P3/P6 题干语言核查），发现后立即纠正并用正确路径重跑，报告中的法语题干提示、等级 token 结论均来自纠正后的运行；另一次 1× 墨迹扫描的 −1.05px 系像素量化伪影，已以 4× 超采样值 +0.21px 为准。
- 校对结束复核：分版 PDF SHA 与开工时一致；核心 8 SVG SHA 与开工时一致（`5424557b…`、`78e6fcd2…`、`5b9854e3…`、`cc227fd9…`、`e58064c9…`、`6583fe28…`、`65cfe2b3…`、`fe22a151…`，前缀示意，全值见工作记录）；分版目录 mtime 未变（仍为 21:31:51 UTC），核心目录未动。
- 本报告未宣称上架；上架由协调员串行执行。
