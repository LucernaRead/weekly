# 独立校对报告 — Lucerna Weekly W45 EN × FR（VOL.2）

**校对对象：** `files/weekly-report-w45-en-fr/`（SVG ×8、卡片 ×8、print/web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
**对照核心：** `files/weekly-report-w45-en-core/`（VOL.2，刊头 The Lucerna）
**同配对家具准绳：** `files/weekly-report-en-fr/`（已上架 W43 EN×FR SVG）
**结论：ZERO PROBLEMS**（阻塞项：无。非阻塞观察见 §10；上架不在本报告权限内，由主线串行执行。）
**校对方式：** 只校对、不改源码。全部构建员结论均独立重测，未采信任何一条；所有写盘只发生在本科对目录
`hidden_files/w45/en-fr-proof/`（含 scratch 复现 `repro/`）。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰
weekly-git、未改核心与 W43 目录（只读对照）、未清理共享 scratch。

## 0. 开工查重与哈希锚点

- 开工时（20:27 EDT）确有进行中的渲染进程，但逐进程查 cwd 后确认分属 EN×NL、EN×JA、EN×IT、EN×RU
  构建与 EN×ES 校对，**无一进程的 cwd 是 EN×FR 构建树**。EN×FR 目录在 120 秒复查内零新写盘
  （最后写盘：KIT 00:27:00 UTC，SVG 00:20:38 UTC 之前），按任务规则安全开工，未 stand down。
- 校对前记录全部交付物与核心 sha256（`pre-hashes.txt`），校对后复核（`post-hashes.txt`）：
  **diff 为空，校对前后交付与核心哈希全部不变。**
- 交付物核对（与任务给定值一致）：print PDF 17,295,418 B，sha256
  `408a67f7b25d2fb509ed6c6f6252fa1ffc7f0d8e9ca7c2f43e1ff923c04d0c74`；web PDF 3,884,123 B，sha256
  `5e32b328302815cec138f9b352a62f23d70152124d04f4f1385efd67dddb4706`；两 PDF 均为 8 页（pypdf 实测）；
  SVG sha 与 KIT §1 所列 8 条逐一相符。

## 1. 冻结（freeze.py，独立重跑）

- `freeze.py baseline --build hidden_files/weekly-report-w45-en-build --core-svg files/weekly-report-w45-en-core/svg`
  （输出重定向至本科对 scratch）：**8/8 逐字节复现**，且工具自带的校对前后核心重哈希一致（核心未被改动）。
- `freeze.py diff`（核心 vs 分版，我方输出 `freeze-diff.json`）：各页新增 CJK = 0，分版 CJK 总计 0
  （P1 183→0、P2 197→0、P3 119→0、P4 139→0、P5 134→0、P6 136→0、P7 347→0、P8 776→0）。
- 违禁词：SVG ×8、KIT、ABSTRACT 全量 grep，“桥接”= 0；全角括号在全部 8 页 SVG = 0（P8 见 §2）。
- 被删行裁定（以不含汉字为口径的纯行；freeze 工具的宽口径 CJK 含 U+3002 句号与全角括号，故
  下列计数以窄口径表述，宽口径下新增 CJK 仍为 0）：
  - P1（2 条）：① `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA` = y=372 刊头徽章槽位，
    分版同坐标改为法语徽章（见 §8）；② `· Nov 8 — NFL in Madrid + F1 in São` = 换行碎片——分版同 y=1701.17
    处原文为 `Nov 8 — NFL in Madrid + F1 in São`（仅行首 `·` 随重排移位），英文一词未丢。
  - P7（2 个不同字符串，共 4 次）：`6).` ×1 与 `。` ×3。`6).` 的裁定：分版 P7 同坐标 (1007, 927.76)
    处文本为 `(page 6).`，即 `6).` 被并入重排后的同一行，并非丢失；`。` 为中文句号标点，随讲解层
    本地化而消失，无英文损失。
  - P8（20 条）：全部为键行换行碎片（`·` 连接的键序列在法语注释变长后断点移动），键本身由 p8.py
    独立裁定（§2），无一丢失。
  - P2–P6：纯非 CJK 被删行 = 0。其余被删行均含汉字，属讲解层替换。
- 结论：冻结成立——无英文正文句子丢失，无新增 CJK，无违禁词。

## 2. P8（p8.py compare，--total 150 口径，独立重跑）

- 正确口径（`compare --core-dir … --edition-dir … --target fr --total 150`）：核心 noted **78** → 分版 noted **150**，
  状态 **EXTRA_ONLY，missing=[]，uncertain=[]，keydiff=[137, 138, 139, 140, 150]**，与构建员一致。
- 计数口径独立确立（`extract --total 150` 两边 JSON）：核心 noted 集 = 78 个号（含 137–150 全部），
  分版 noted 集 = 1–150 全部；核心集 ⊆ 分版集；分版 extra 的 72 号经实测恰等于 1–150 对核心集的补集
  （即核心按长度/类型规则压制的注全部在分版印全，W43 EN×FR 同 pattern，属 DECISION.md 的 adjudicated acceptance）。
- **默认 total 陷阱已实测**：不带 `--total` 时工具取 tables.json 中 fr 的 W43 题量 149，跑出核心 73 noted /
  分版 145 noted / keydiff [137, 138, 139, 140, **145**]。这证明 145 伪影是错误 total 下的分段产物，
  正确口径下不存在；同时也证明 --total 150 不是可选项，是必选项。
- keydiff 逐项印刷行对照（extract JSON 原值）：
  - 137：核心 `耐心是制度的一部分，而不是制度的失败。` → 分版
    `La patience fait partie du système, et non un échec de celui-ci.` —— 英→法合法重定向。
  - 138：核心 `11 月 3日周二是美国的选举日。` → 分版
    `Le mardi 3 novembre est le jour des élections aux États-Unis.` —— 英→法合法重定向。
  - 139：核心 `这周日，NFL 在马德里比赛。` → 分版 `Dimanche, la NFL joue à Madrid.` —— 英→法合法重定向。
  - 140：核心 `并非每处都拨回时钟。` → 分版 `Tous les endroits ne changent pas.` —— 英→法合法重定向。
  - 150：核心 `开放题 — 要点见写作框，范文在第8 版写作框内` → 分版
    `Tâche ouverte — points dans le cadre d’écriture ; texte modèle dans le cadre de cette page`
    —— 写作开放题键说明的中→法翻译，措辞与已上架 W43 EN×FR 的写作键（其 149 号键）**逐字一致**（实测）。
  - 除上述 5 项外，两边 keys 其余全部相等（程序比对：仅 137/138/139/140/150 不同）。
- 145 清零验证：终版 P8 全文 grep `(ID)` = 无；对话笔记实测为
  `145. ID (Au vote, on montre sa pièce d’identité)`（y=2145.66），内层冗余括号已无；145 键两边均为 `ID`。
- P8 注释纯法语：P8 SVG CJK = 0、全角括号 = 0、半角括号 175 对；键区 13.5pt 文本 114 条，
  最大基线 2529.27（KIT 称键流底 2530；W43 同口径最大基线亦为 2529.27，完全一致）。
- 结论：P8 印刷笔记集合关系为 EXTRA_ONLY（可接受），keydiff 5 项全部合法，145 已清零。

## 3. 任务前提勘误独立验证（核心实际为四题英→中）

从**核心 P8 渲染内容**实测（非核心 KIT 文字）：

| 题 | 核心题面（渲染文本） | 核心键 | 方向 |
|---|---|---|---|
| 137 | `Translate : « Patience is part of the system, … »`（y=1320.1，英文句） | 中文 | 英→中 |
| 138 | `翻译：Tuesday, November 3, is Election …`（y=246.5，中文指令词 + 英语句子） | 中文 | 英→中 |
| 139 | `翻译：On Sunday, the NFL plays in Madrid.`（y=369.45，中文指令词 + 英语句子） | 中文 | 英→中 |
| 140 | `Translate : « Not every place changes. »`（y=462.68，英文句） | 中文 | 英→中 |

核心构建源 content8.py 的 e_items 亦印证：四条键均为中文，四条 body 均为英文句（137/140 用
`Translate :`，138/139 用中文指令词）。核心 KIT 自述的“英↔中双向”与渲染实测不符，
渲染证据为准。分版四题统一渲染为 `Translate :` + 英语句子 + 法语键（P8 卡片目视亦确认），
指令词语言不同不等于翻译方向不同——分版处理合法。勘误成立。

## 4. 几何（occlusion_audit 自检先行；全部独立重跑）

- 自检：`occlusion_audit.py --selftest` 通过（6 类 planted flags 全触发，clean 对照静默）。
- 分版：**1 标记**（TEXTX，P1 `The Lucerna` vs 版次行，834.2×6.2px）；核心：**0 标记**；NEW = 1。
  字面意义的 NEW=0 **未被原始工具输出满足**——这一点如实记录，裁定见下（§4.1）。
- 同基线家具带（我方独立方法：occlusion 工具的 PIL ink box，非构建员 scans.py 的 advance 法）：
  y=92/116/142/478/522/2624 六带，**无一对 ink 间隙 < 40px**（<40px 列表为空）。
- 右缘 ADVANCE 扫描（分版全 8 页）：越过内容边 1885 的仅 2 条，**无一越过内框线 1910**：
  `b. an election in the middle of a term`（1899.4）与 `d. the paper you mark your choice on`（1903.8），
  均为 P8 冻结配对行；核心同字符串同 x=1485，y 仅差 +29.725（恰为一 ex-body 行距，与 KIT §5 的
  E139 换行致电池移位一致），属继承。
- P6 图表（基线锚定墨迹法：PIL getmetrics + anchor ls，逐标签对后续 rect 求最大覆盖）：
  `No lines : 38%` / `Work on Tuesday : 29%` / `Travel plans : 21%` / `Habit : 12%` 覆盖率**均为 0.0%**（门限 <30% 通过）。
- 第 2 轮紧张点重测（我方墨迹口径，见 §10 说明口径差）：
  - P8 Levels 行基线 **1470.965**（与 KIT 一致），写作条金线 y=1486（实测 `<line … y1="1486" …>`），
    我方 ink bottom 1474.5，距金线 **11.5px**；写作框 rect 顶 y=1500，H 头 y=1526——电池未压金线。
  - P1 末行故事基线 1478.8、ink bottom 1485.3，下一栏头 y=1530.475——无压框。
  - P2 末题基线 2517.825、ink bottom 2523.6，页脚规则 2580——无页脚撞线。
- 第 3 轮变化范围验证：round3 基线 → 终版哈希，仅 P8 SVG、P8 卡片与两 PDF 变化；
  P1–P7 SVG 与 round3 基线完全一致；round2 基线 → 终版仅 P1/P2/P8 变化，与所述修复轮范围一致。

### 4.1 P1 刊头 TEXTX 的独立像素级裁定（不采信构建员证据，自做三项）

① **渲染像素行扫描**（我方用 cairosvg 自渲染 P1 PNG 1950×2700，x 带 550–1400，行 130–399）：

| 版本 | 阈值 128 | 阈值 200 | 阈值 240 |
|---|---|---|---|
| 分版 FR | 刊头墨 143–292，版次行墨 295 起，**间隙 2px** | 142–293 / 295 起，**间隙 1px** | 142–293 / 295 起，**间隙 1px** |
| 核心 | 143–289 / 291 起，间隙 1px | 142–289 / 291 起，间隙 1px | 142–335 合并，间隙 0px |
| 已上架 W43 EN×FR | 与分版**逐行相同**（143–292 / 295 起等） | 与分版逐行相同 | 与分版逐行相同 |

即：分版在全部三阈值下均有真实纸面间隙，且在宽松阈值下比核心自身的间隙更稳固（核心在 240 下
已连通，分版仍有 1px 间隙）。无真实重叠。

② **字体度量框对照**（occlusion 工具自身字体解析）：刊头 tool-ink 141.75–291.25，
版次行 tool-ink 285.00–330.75，二者重叠 291.25−285.00 = 6.25 ≈ 工具报告的 6.2px——
工具重叠完全由度量框高估造成：版次行 tool-ink 顶 285.0 vs 渲染墨迹顶 295，**高估 10.0px**；
刊头 tool 底 291.25 vs 渲染墨迹底 292–293，低估约 1–2px。误差方向恰好制造出虚假重叠。

③ **W43 同工具复跑**：已上架 W43 EN×FR 用同一工具跑出**完全相同的 TEXTX 标记（834.2×6.2px，
同为 P1 刊头 vs 版次行）**，另附一个与本分版无关的 P2 BOXTITLE 标记（0.6px 量级，W43 自有）。
即该家具对在已发货版本中即带此标记。

**裁定：该 NEW=1 标记为工具测量伪影，真实缺陷 0 条。** 未移动版次行（移动将违背“W43 家具为准”
的更高优先级指令）。字面 NEW=0 的工具输出未满足，但这属于工具输出与像素事实的差异，
已由三项独立证据闭合；是否因此卡住上架由主线按 SOP 裁决——本报告结论 ZERO PROBLEMS
基于真实缺陷计数，工具输出原文如实附于 §10。

## 5. gloss（我方口径：先从核心构建源实测，再核分版）

- 分组口径说明（非照搬构建员分组）：按构建源文件分组——content12（P1–P2 素材）、content34（P3–P4）、
  content56（P5–P6）、content7（P7）、content8（P8），对每文件内全部 `gloss()` 调用串按 `·` 拆分计数。
  核心实测：content12 **3**、content34 **8**、content56 **7**、content7 **0**、content8 **0**，合计 **18**；
  分版实测：**3 / 8 / 7 / 0 / 0，合计 18**，逐文件相等。
- 词头 1:1：18 项英文词头按顺序逐项相等（content12：to fall back、a costume、trick or treat；
  content34：to open、a monster、a catchphrase、a series、a fixture、a title、to defend、a fan；
  content56：a map、too close to call、a second screen、to register、a governor、to shape laws、patience）。
  核心词头后接中文讲解，分版词头后接法语讲解——仅讲解本地化。
- 渲染核对：P1 gloss 框三行（y=1395.3 / 1425.02 / 1454.75，与核心坐标完全一致）拼合为
  `Note | a midterm = mi-mandat · a ballot = bulletin de vote · a race = course électorale · to call a race = annoncer le résultat.`
  = **4 项**；核心同框拼合亦为 4 项（中文讲解）。P1 框位置、行数、坐标未动。
- P7 金句语法点与跟练注释：content7 源中 8 条 phrases 各含 1 个语法点 + 1 条跟练注释，
  核心与分版均为 8 + 8（点为中文→法语，注释为法语或语言中性记法，无 CJK）。

## 6. P7（定义句、金句、结构）

- 4 句专栏定义句（渲染 P7 全文按文档顺序拼合后搜索，核心与分版出现次数完全一致）：
  `The clocks fell back.` ×1 / `She is going to vote on Tuesday.` ×1 /
  `The Bernabéu is bigger than most stadiums.` ×1 / `Nobody knows whether the race is called yet.` ×2
  （后者 ×2 系定义栏 + 工具箱例句栏复用，两边一致）。
- 8 句金句原文逐字（同法拼合搜索，核心与分版次数完全一致）：
  Election Day 句 ×1、1 to 2 句 ×1、Which film 句 ×1、Two games 句 ×1、results 句 ×1、
  Patience 句 ×2（金句栏 + B2 例句栏复用，两边一致）、Not every place 句 ×1、One Sunday 句 ×1。
  （单条文本元素内 substring 搜索会因换行断行而漏检，故采用拼合搜索；逐字性以拼合串为准。）
- 金句结构（content7 源 phrases 表，核心 vs 分版）：8 条顺序、原文、页标签（1, 2, 3, 4, 5, 6, 2, 4）、
  级别序列（A2, A2, B1, B1, B2, B2, A2, B1，即 100–107）、练习句与键全部一致；
  每条各有语法点 + 跟练注释（2×）——核心中文点/注释 → 分版法语点/注释。
- P7 结构：3 级专栏 + 工具箱 + 8 金句 + 4 项诊所 + 读者园地 + 预告，与核心一致；
  栏头与 W43 形式逐项一致（LEVEL A2 · Les bases / LEVEL B1 · Plus loin / LEVEL B2 · Le défi /
  THE TOOLBOX · Boîte à outils / PHRASES OF THE WEEK · Phrases de la semaine (de ce numéro) /
  THE ERROR CLINIC · Les erreurs / READERS' CORNER · Courrier des lecteurs /
  NEXT WEEK · VOL.3 La semaine prochaine / LANGUAGE IN HAND · La langue en main），
  且 y 坐标与 W43 相同（116 / 227 / 1236 / 1903 / 1918 / 2248），仅 VOL.2→VOL.3 为版本更新。

## 7. 读者园地（英语冻结 + 法语披露逐字核实）

- 英语元素逐字冻结：例证引文三行在核心与分版中坐标与文本完全一致——
  `« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader`（y=1956.0）、
  `in Chicago (editor's example : no real reader letters had arrived when this issue`（y=1986.53）、
  `went to press, so the example stays, honestly labeled)`（y=2017.06）。无编造的读者、来信、姓名或引文。
- 法语披露句逐字摘录（分版 P7，y=2076 / 2104 / 2132，框内 3 行）：
  `Note : le VOL.1 avait promis de vraies lettres pour le VOL.2, mais aucune lettre ni aucun texte de la page 8 du VOL.1 n’est arrivé. L’exemple reste, honnêtement signalé, et la promesse passe au VOL.3. Envoyez vos lettres : les meilleures paraîtront dans le VOL.3 !`
- 逐项核实：① 无真实来信抵达 VOL.2（`aucune lettre … n’est arrivé`）✓；② 无 VOL.1 第 8 版最佳写作抵达
  （`aucun texte de la page 8 du VOL.1 n’est arrivé`）✓；③ 标注例证保留、承诺顺延 VOL.3
  （`L’exemple reste, honnêtement signalé, et la promesse passe au VOL.3`）✓；
  ④ 显性祈使邀请 + VOL.3 刊登承诺（`Envoyez vos lettres : les meilleures paraîtront dans le VOL.3 !`）✓。
  内容预告行（NEXT WEEK 栏）未计入邀请，邀请句独立存在。
- 最佳 P8 作文覆盖范围显式裁定：披露句的 `aucun texte de la page 8 du VOL.1` 覆盖“最佳 P8 写作未抵达”，
  `la promesse passe au VOL.3` + 邀请句的 `les meilleures paraîtront dans le VOL.3` 覆盖“顺延刊登承诺”，
  故最佳 P8 作文的披露与承诺均已覆盖，无遗漏。
- 无凭空新写英语披露句：核心本无英语披露句，分版亦无新增英语披露句。
- VOL.3 承诺（KIT §9）核对：读者园地披露的顺延 ✓；预告栏英语原文 + 法语半句均含
  11 月 11 日退伍军人节（Wednesday, November 11 : Veterans Day）、11 月 15 日 NFL 慕尼黑赛
  （Sunday, November 15 : the NFL in Munich）、中期选举结果（the midterm results, reported）✓。

## 8. 家具（W43 偏差清单逐项核实，均以已上架 W43 EN×FR SVG 为准绳）

- gloss 前缀：分版 P1–P6 框均用 `Note | `（实测每页 1 个 Note 框起首，P7/P8 无 gloss 框与核心一致），
  未用 tables.json 泛化的 `Note — ` ✓。
- P1 几何：徽章 y=372、19.5pt、BRICK 色（`#a4553a`）、居中，文本与 W43 徽章逐字一致（仅 VOL.1→VOL.2）；
  版次行 y=330、46pt serif bold，文本为 W45 主题（ÉLECTIONS · FOOTBALL · CINÉMA）；顶条中心行与 W43
  形式一致 ✓。
- 页脚：8 页全部为左 `The Lucerna · HEBDOMADAIRE ANGLAIS VOL.2 · TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS`、
  右 `Page N sur 8` ✓。
- P8 键区：半角括号（全角括号 0）、13.5pt、键流底 2530（复现运行日志亦印 `flow[P8-keys] … (bottom 2530)`，
  最大键基线 2529.27）；分隔符 `— Page N —`（N=1–8）与 W43 一致；8 个分栏头与 W43 形式一致
  （A · CLOZE · Texte à trous / B · MULTIPLE CHOICE · QCM / C · READING · Compréhension /
  D · SENTENCES · Phrases à former / E · TRANSLATION · Traduction / F · WORDS · Mots à associer /
  G · DIALOGUE · À compléter / H · WRITING · Écriture），唯一差别是 H 头后的 `[B1]`——该标记来自 W45 核心
  原文（核心 P8 亦为 `H · WRITING · 写作 [B1]`），属冻结继承，非家具偏差。
- 题型/指令词：P8 头用 W43 形式（Texte à trous、QCM、Traduction、Écriture、Compréhension 等）；
  指令词 Complétez / Réécrivez / Corrigez / Associez 全页分布正常。
  注：W43 P3/P5 的 `C · CHOOSE · Choix multiple` 栏在 W45 核心中不存在（W45 核心 P3/P5 无 CHOOSE 栏），
  故分版无此栏属内容继承，非家具缺失。
- P7 栏头法语半句：用 W43 形式（见 §6），y 坐标与 W43 相同 ✓。
- P6 选票框 ☐ 与 P7 诊所 ✗：SVG 文本中字符与核心一致（未出现在 freeze 被删行中）；
  卡片裁剪对照（同坐标裁剪，分版 vs 核心）：☐ 与 ✗ 均渲染为相同的方框叉形字形（字体缺字 fallback 形态），
  分版与核心裁剪视觉一致，属核心固有渲染，未动。

## 9. 其余交付核查

- 图片载荷：每页 `<image>` 元素（href、x、y、宽、高）核心 vs 分版逐页相等
  （P1/P2/P3/P4/P6 各 1 张，P5/P7/P8 0 张）；署名在版：P1（Kenneth C. Zirkel — CC0, via Wikimedia Commons）、
  P2（Public domain, via Wikimedia Commons）、P3（Édouard Manet — CC0, via Wikimedia Commons，附“非电影美术”
  说明）、P4（Frank R. Snyder — public domain, via Wikimedia Commons）、P6（Public domain, via Wikimedia Commons）✓。
- ABSTRACT.txt：法语单行（无换行符、无尾换行）、无 ASCII 双引号；含刊名 Le Lucerna、VOL.2、
  法语读者（lecteurs francophones）、A2–B2、150 题、本周真实主题关键词（11 月 3 日美国大选日、
  11 月 1 日时钟回拨、Halloween、11 月 6 日电影、马德里 NFL、11 月 8 日圣保罗大奖赛、提前投票深度阅读）
  与学习者搜索短语（`pour apprendre l'anglais en lisant l'actualité américaine`）✓。
- 卡片目视：8 张逐页看过——无溢出、无压框、无页脚撞线；P1 刊头与版次行之间目视有清晰间隙；
  P6 图表标签清晰无遮挡；P8 电池、写作框、答案流均在框内，答案流末行距页脚有余量。
- 题量与级别（我方独立单进程复现：构建树拷至本科对 scratch、OUT 重定向、run.py 重跑 + 自写 registry 统计，
  全程未写 files/ 树）：复现 SVG **8/8 与 shipped 逐字节一致**；registry 总 **150**，
  页分布 **10/17/18/18/18/18/12/39**，级别 **A2 60 / B1 69 / B2 21**，编号 1–150 连续无缺 ✓。
- 范文：P8 MODEL 框 6 行拼合，核心与分版**逐字一致**；原始空白分词 = **85 词**（核心自有口径，与核心 KIT 一致）；
  注：构建员 reg-check 所印 82 词是去掉 `« » :` 后的分词口径（我方复算：同文本去标点后确为 82），
  两数皆对、口径不同，非 discrepancy。
- 双 PDF：各 8 页，字节数与 sha256 与 KIT 一致（§0）✓。
- KIT §9 承诺：VOL.3 顺延、11 月 11 日、11 月 15 日、中期选举结果均已写入 KIT §9 且与 P7 预告栏一致 ✓。

## 10. 非阻塞观察（单列，不构成阻塞项）

1. **工具输出字面 NEW=1 vs 真实缺陷 0**：occlusion_audit 原始输出 NEW=1（§4.1 已裁定为测量伪影，
   三项独立证据：像素间隙、度量框高估 10.0px、W43 相同标记）。若主线 SOP 要求字面 NEW=0 的工具输出，
   则需主线裁决是否接受像素裁定——本报告不擅自宣布该工具输出“通过”，只报告真实缺陷为 0。
2. **紧张点口径差**：KIT 的“P1-headline 止于 1502 / P2-ex 止于 2532 / Levels 墨迹底约 1476.8（距金线约 9px）”
   为 flow-cursor 口径；我方 PIL ink-box 口径测得 P1 墨迹底 1485.3、P2 墨迹底 2523.6、
   Levels 墨迹底 1474.5（距金线 11.5px）。两口径相差约 2–17px，但结论一致：三处均有明确余量、无压线。
3. **范文 85 vs 82**：仅分词口径不同（原始空白 85；去 `« » :` 后 82），文本逐字一致，非问题。
4. **W43 `Choix multiple` 计数差**：W43 有 2 处、分版 0 处，系 W45 核心无 CHOOSE 栏（内容继承），非家具缺失。
5. **P6 右栏编号视觉位移**：P6 右栏练习在分版卡片中比核心低约一行（法语指令行换行致 flow packing 差异），
   编号与内容完整（82–99 全在）、无溢出，属正常本地化重排。
6. **P7 金句拼合计数**：Patience 句与 Nobody-knows 句在 P7 拼合串中各出现 2 次，系金句栏与例句/定义栏复用，
   核心与分版次数一致，非重复错误。

## 证据文件（本科对目录）

- `hidden_files/w45/en-fr-proof/REPORT.md`（本报告）
- `hidden_files/w45/en-fr-proof/pre-hashes.txt`、`post-hashes.txt`（校对前后哈希，diff 为空）
- `hidden_files/w45/en-fr-proof/freeze-baseline.log`、`freeze-diff.log`、`freeze-diff.json`
- `hidden_files/w45/en-fr-proof/p8-compare.log`、`p8-compare.json`、`p8-core.json`、`p8-ed.json`、`p8-w43.json`
- `hidden_files/w45/en-fr-proof/occlusion-ed.log`、`occlusion-ed.json`、`occlusion-core.log`、`occlusion-core.json`、`occlusion-w43.log`
- `hidden_files/w45/en-fr-proof/proof_checks.py`、`proof_checks.log`
- `hidden_files/w45/en-fr-proof/repro/`（构建复现 scratch：8/8 逐字节一致 + registry 统计）
- `hidden_files/w45/en-fr-proof/pixel-p1-fr.png`、`pixel-p1-core.png`、`pixel-p1-w43.png`（P1 像素扫描自渲染图）
- `hidden_files/w45/en-fr-proof/crop-ballot-fr.png`、`crop-ballot-core.png`、`crop-clinic-fr.png`、`crop-clinic-core.png`

**结论重申：ZERO PROBLEMS。未宣布上架；上架与 repo 插入由主线串行执行。**
