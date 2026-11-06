# 独立复校报告 — Lucerna Weekly W45 DE×NL（德语×荷兰语，修复后全量复校）

**结论：ZERO PROBLEMS（可定稿）。**

- 复校对象：`files/weekly-report-w45-de-nl/`（修复后版：svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-de-core/`（Die Lucerna VOL.2，150 题）
- 原阻塞：原校对报告 `hidden_files/w45/de-nl-proof/REPORT.md` 问题 1（P7 NOCH EIN WORT 框德语定义句被本地化）——本轮复校确认已修复。
- 校对方式：全部结论均从渲染产物 / SVG 坐标独立重测得出，修复员自述（KIT §17、fix-round-* 文件）一律未被采信；凡修复员说法与实测不符处，本报告以实测为准——本轮实测与修复员说法逐项一致，无不符处。
- 纪律：只校对、不改源码；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录。开工前查重：目标两目录在 90 秒复查窗口内零新写盘（最新仍为修复轮 21:07 UTC 的 gate 文件，属已完成交付的新鲜时间戳，非 stand-down 理由）；复查窗口内曾短暂出现一个 `render.py` 进程，但在核查其 cwd 前即已退出，且目标目录 mtime 全程未变——未向本版写盘，故正常开工。收尾复核：交付 SVG/PDF 哈希与开工时逐项相同，核心 8 页哈希开工前、基线运行后、收尾三次一致。
- 证据存档：本目录 `freezediff.json`（冻结差分）、`occlusion.json`（遮挡审计）、`p8.json` / `p8-core.json` / `p8-edition.json`（P8 提取与比对）、`baseline-core/`（核心基线重跑）。

## 问题清单

无。11 门必查全部通过；另有 2 条非阻塞记录（见末尾），均不影响定稿。

## 必查门实测值

### 门 1 修复验证（原阻塞已消除）

- P7 NOCH EIN WORT 框三行实测（x=1473，基线 y=1432.5 / 1461.61 / 1490.72），与任务要求逐字一致：
  - `«der Tankrabatt» (Seite 2): die`
  - `gesenkte Steuer auf Benzin und Diesel.`
  - `Brandstofkorting.`
- 德语句逐字恢复：第 2 行与核心逐字节相同；第 1 行与核心仅差全角/半角括号（核心 `（Seite 2）`，本版 `(Seite 2)`，与 DE×EN 版相同，属 DE 扇出半角括号族惯例，见 README #14）；页标恢复为 Seite；荷兰语 gloss `Brandstofkorting.` 保留，对应核心第三行讲解层。
- 框几何实测：框 rect x=1451 y=1354.5 w=434 h=150，底 **1504.5**；金句区横线 y=1508（x 65→1885），框底低于横线 3.5px；读者框 rect y=760.5 h=578，底 **1338.5**，距词框顶 1354.5 间隙 16px。全部与修复员称逐值相同。

### 门 2 改动范围验证（仅 P7 变化）

- 与修复前基线存档（`fix-round-baseline-hashes.txt`）逐项比对：P1–P6、P8 SVG 哈希逐字节一致（p1 `42ba63f4…`、p2 `da08a038…`、p3 `9da2e711…`、p4 `452c69e9…`、p5 `b034ba99…`、p6 `18d2c3c3…`、p8 `ee928685…`）；仅 P7 变化（`5700fb81… → 95dfd5fd…`）。
- 卡片：P1–P6、P8 哈希逐字节一致；仅 P7 变化（`afc348d3… → 77e87032…`）。
- P7 文本元素数：修复前副本 `p7-sprache.PRE-FIX.svg` 188 = 交付版 188；两版文本多重集差分恰为该框 3 行（删：`(pagina 2): de` / `verlaagde belasting op benzine en` / `diesel. Brandstofkorting.`；增：修复后 3 行），无其他文本增删。
- 双 PDF 变化属预期（内嵌 P7）；其余交付文件（KIT、ABSTRACT）不在 SVG/卡片哈希比对范围内，KIT 文字另见门 10。

### 门 3 Freeze 全量

- 核心基线：`tools/freeze.py baseline --build hidden_files/weekly-report-w45-de-build` → **8/8 SVG 逐字节复现**（p1 `6cbd4802…`、p2 `9362256d…`、p3 `3e8a8d16…`、p4 `b787f592…`、p5 `4dcbeb97…`、p6 `01b75ad4…`、p7 `fbaf8cdd…`、p8 `299524bd…`），核心前后哈希一致（基线运行证明核心未被触碰）。
- 冻结差分（本目录 `freezediff.json`）：P1–P8 新增 CJK **0**，各页版内 CJK 核心 N→本版 **0**（P1 168、P2 186、P3 187、P4 155、P5 193、P6 228、P7 394、P8 1429 → 全部 0）；SVG 全文“桥接”0 次。
- P1–P7 纯拉丁删除串逐项裁定（除下列全部通过；“纯拉丁”以不含 CJK 统一码块计，`。`属中文句号绕排碎片，归讲解层）：
  - P1 唯一 1 条：`DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND`——核心 P1 原生副题槽节点，被徽章原位替换，属家具替换，通过。
  - P3/P4/P6 各 1 条：`。`——中文句号绕排碎片，属讲解层碎片，通过。
  - P7 共 3 条：`Ein Beispiel der Redaktion!`——读者框标签，同坐标改为荷文标签，属家具本地化，通过（DE×EN 亦改，属实）；`«der Tankrabatt»（Seite 2）: die`——仅全角括号形式被半角形式替代，同句半角版在新增串中（见门 1），非删除，通过；`……`——中文省略号绕排碎片，通过。
  - P2、P5 纯拉丁删除串 **0 条**。德语定义句第 2 行不在删除清单中（逐字节存续）。
  - P8 纯拉丁删除串 6 条，全部为含全角右括号 `）` 的绕排碎片（核心全角括号 → 本版半角括号后键行重绕排所致），无德语测验正文丢失。
  - 新增串（P1–P7）全部为荷文讲解、家具，或双语 gloss 串内的德语词头，无新增德语正文句子。
- P1/P4 内嵌图片数据与核心逐字节相同（data URI 哈希一致：P1 `5c194278a2c3e94f…`、P4 `8d8f82ede774c0f3…`）。

### 门 4 P8 全量

- `tools/p8.py compare --target de`（目标语代码 de，P8 文件名由此解析）：**CLEAN 150=150**，missing=[]、extra=0、uncertain=[]、keydiff=[137, 138, 139, 150]；`extract` 两边均为 150/150。
- keydiff 逐项实印核实（P8 SVG 原文行 + 提取键双重核对），全部为真实重定向，无括号/dash 提取伪影：
  - 137：题干 `Der Tankrabatt läuft bis Dezember.` + 指令 `Vertaal naar het Nederlands` → 键 `De brandstofkorting loopt tot december.` + 注 `(laufen = duren)` ✓
  - 138：题干 `Ich schaue am Dienstag Fußball.` + 指令 `Vertaal naar het Nederlands` → 键 `Ik kijk op dinsdag voetbal.` + 注 `(schauen = kijken)` ✓
  - 139：题干 `Die Schule hat wieder begonnen.` + 指令 `Vertaal naar het Nederlands` → 键 `De school is weer begonnen.` + 注 `(wieder begonnen = weer begonnen)` ✓
  - 150：写作 apparatus 键 `Open opdracht — zie de punten in het schrijfblok; de voorbeeldtekst staat in het schrijfblok op deze pagina` + 注 `(Beoordeling op basis van de punten)` ✓
  - 140 正确不在 keydiff 内：题干荷兰语 `Ik slaap op zondag een uur langer.` + 指令 `Vertaal naar het Duits` → 键德语不变 `Am Sonntag schlafe ich eine Stunde länger.`，注改为荷兰语在前 `(een uur langer slapen = eine Stunde länger schlafen)` ✓
- 全角括号核查：本版 P8 SVG 全角括号出现 0 次；键注粘连形式（`december.(laufen …`、`149. A(gehe …`）与 DE×EN 同族版实印一致，属家族排法，非伪影。

### 门 5 几何遮挡全量

- `tools/occlusion_audit.py`（自检先行通过，6 类 planted flags 全触发）：**分版 0 flags、核心 0 flags、NEW vs core 0**（本目录 `occlusion.json`）。
- 同基线墨迹碰撞扫描（README #10 类，复用审计工具的真墨迹度量，全 8 页所有同基线文本组）：负间隙 **0 处**；家具带逐值：y=92 间隙 200.8px / 93.9px；y=478 间隙 801.8px；y=522 间隙 605.6px；页脚 y=2624 8 页间隙均为 783.7px。
- P6 图表标签 vs 后绘条形（条形起点 x=535，逐项实测墨迹右端）：familiezorg 528.8（间隙 **6.2px**）、thuiszorg 512.0（间隙 **23.0px**）、zorghuis 504.2（间隙 **30.8px**）；与后绘矩形重叠 **0**，三标签目视全部脱离条形（见门 11 卡面）。
- P3 TIPP 框：rect y=1444.6、底 **1583.66**，与核心逐值相同；练习区金线 y=1608，间隙 **24.34px**。
- P8 题头：F 头墨迹右端 1850.0（页内 1885 以内），无超宽。

### 门 6 Gloss 全量

- 按渲染后 `gloss()` 调用串本身以 `·` 拆分（README #21）：共 5 处调用 × 每处 5 项 = **25 项**，与核心 **1:1**，德语词头逐项对应（P2 Tankrabatt/Zapfsäule/Energiesteuer/Mehrwertsteuer/Angehörige；P3 Ferienwechsel/Schülerin/Ausflug/Advent/Lesung；P4 Englische Woche/auswärts/empfangen/Favorit/eröffnen；P5 Pausenhof/Klassenarbeit/Referat/ausschlafen/Probe；P6 Angehörige/Pflegeversicherung/Pflegedienst/Stagnation/Aufschwung）。
- 页码归属：5 处调用分属 P2–P6 章节（content12.py 的 P2 章节、content34.py 的 P3/P4 章节、content56.py 的 P5/P6 章节）；每项德语词头与荷兰语释义均在对应页渲染 SVG 文本中实测存在。
- 注：`Uitleg — ` 前缀在 P1–P6 各出现 1 次（P1 为行内讲解句，非 gloss() 框调用），与 KIT §6 第二句一致，不与 gloss 框页码 P2–P6 矛盾。

### 门 7 P7 金句全量

- 8 句德语原文在核心与本版 P7 表中位置逐字相同（y=1597/1801，四列），全刊出现次数核心与本版均为 **2, 2, 2, 2, 2, 2, 2, 2**（源文章 1 次 + P7 表 1 次），空白归一化全文检索逐句验证。
- 页码标签分布与核心一致（按表列顺序）：Seite 4·B1、Seite 2·A2、Seite 2·A2、Seite 5·B1、Seite 3·A2、Seite 4·B1、Seite 6·B2、Seite 6·B2；逐句核对：每句的源文章出现页 = 其标签页（Q1→P4、Q2→P2、Q3→P2、Q4→P5、Q5→P3、Q6→P4、Q7→P6、Q8→P6），全部逐字取自本期文章。
- P7 短语（工具箱/诊所双语条目）德语词头与核心一致；Q7 荷文译文删 `Duitse` 一词的原校对观察仍属实（德语引文本身完整无损，译文在上下文中无歧义），不列为问题。

### 门 8 读者园地全量（独立再判定：显性邀请成立）

- 页上三事实齐全（荷文事实句实印，y=1247.23/1274.92）：`Geen echte brief: nog geen brieven of beste pagina-8-tekst; belofte naar VOL.3.`——无真实来信（`nog geen brieven`）、无最佳 P8 习作（`beste pagina-8-tekst` 在 `nog geen … of …` 否定辖域内）、VOL.3 承诺（`belofte naar VOL.3`）；示例身份由标签句 `Een voorbeeld van de redactie!`（与核心标签同坐标 y=848.5）明示。
- 显性荷兰语公开征集句实印（读者框内，y=1331.11，框底 1338.5 以内）：`Schrijf ons! Stuur je echte brieven in!`——祈使 + 明确对象（真实来信），本复校独立判定：**显性邀请成立**。内容预告栏德语 `Schreiben Sie uns!`（P7 底 y=2511.4，冻结德语）与各页 UND SIE? 提示均未计入，征集成立不依赖它们。
- 无编造：示例信正文（`„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético…`）与核心逐字相同；冻结德语行（`Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`、征集德语段）与核心逐字相同；无新增读者人名/引言。

### 门 9 家具三方对照

- 徽章节点与 W43 已发同配对版 `files/weekly-report-de-nl/svg/p1-front.svg` **逐属性一致**：x=975 y=372、Noto Sans CJK SC、20pt、bold、fill #a4553a、居中（middle），字符串逐字相同：`TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`。W43 实测胜过 README #20 泛写值 19.5pt（本版取 20pt 正确，属 DE 家族原生副题槽情形）；页脚中 VOL.1→VOL.2 的差异属预期版本差异，非徽章差异。
- 页脚 8/8：`Die Lucerna · DUITS WEEKBLAD VOL.2 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS`；页码行 8/8：`Pagina N van 8`；masthead 8/8：`Die Lucerna`（目标语德语冠词正确）。

### 门 10 KIT 文字订正验证

- §6 gloss 页码：已订正为 P2 5 · P3 5 · P4 5 · P5 5 · P6 5 = 25（原“P1 5”笔误已消除），与门 6 实测一致。
- §13“桥接”表述自洽：交付 SVG 8 页全文“桥接”出现 **0 次**；KIT 全文该词出现 **2 次**，恰为第 185 行（§12 旧表述引用）与第 216 行（§13 口径句本身），与 §13 所称“交付 SVG 0 次、KIT 元语言提及 2 次”逐字相符；构建码（*.py）中该词出现 0 次。
- §3/§12“EN 同族先例”登记已修正：§3 现称 DE×EN 逐字保留德语句（与原校对实测 EN 版一致，属实）；§17 第 250 行明文记录原登记不实（DE×EN、DE×ES、DE×IT 均逐字保留）；§3 读者框标签“EN 同族先例相同”亦属实（EN 版标签确改为英文）；KIT 全文已无“EN 版同样本地化该句”的不实登记。

### 门 11 PDF / 卡片 / 题量 / ABSTRACT

- 印刷 PDF `Die-Lucerna-VOL2-NL.pdf`：**4,138,969 B、8 页、1462.5×2025 pt**，sha256 `bbd0f30b0ae2a944f635704a734a5530e474dff6d004824966642df05e695555`，与任务给定值与 KIT §11 一致。
- 网页 PDF `Die-Lucerna-VOL2-NL-web.pdf`：**4,140,002 B（<10 MB）、8 页、1400×1938 pt**，sha256 `7a667deaa87616730ff720d3265e7f45d7375d8d0fe771cd41ac237820ec01ac`，与任务给定值与 KIT §11 一致。
- 卡片 8 张：1950×2700 PNG，**全部目视**——P1 徽章/副题/顶带/头条/数字框/Fragen 框/照片+出处/quiz、P2 UND SIE?/RECHNEN 宽框/gloss 框/练习区、P3 TIPP 框与金线间隙、P4 赛程表/UND SIE?/练习区、P5 周计划宽框/UND SIE?/练习区、P6 图表三标签/免责声明单行/练习区、P7 读者框 6 段/修复后词框（德语句 + Brandstofkorting. 清晰在框）/金句格/诊所/预告、P8 测验区/写作框+范文/全部答案键——无重叠、无截断。
- 150 题分页（SVG 题号实测，伪影已排除）：P1 10（1–10）、P2 18（11–28）、P3 18（29–46，另有一枚与核心相同的正文内 `4.` 数字；P4 赛程表 `1. FSV/1. FC` 队名、P5 `31. Oktober` 日期同理非习题）、P4 18（47–64）、P5 18（65–82）、P6 18（83–100）、P7 12（101–112）、P8 38（113–150，P8 键集 150=150 且 P1–P7 合计 112），合计 150，与核心一致。
- 等级分布：各级徽章序列与核心逐页逐项相同（习题德语题面冻结 + 级别徽章未变），故 A2 66 / B1 70 / B2 14 分布与核心一致。
- ABSTRACT.txt：荷兰语单行（354 字节，1 个结尾换行），无 ASCII 双引号，含真实主题关键词（voetbalweek、Champions League、Europa League、Bundesliga speeldag 9、brandstofkorting tot 31 december、vakantiewissel、zorg thuis）与学习者搜索短语（`Duits wil leren door echt Duits nieuws te lezen`），含刊名、目标语名、A2–B2、150 oefeningen。

## 非阻塞记录（不影响定稿结论）

- 记录 1：KIT §5 所记 P6 图表间隙 thuiszorg 23.1px / zorghuis 30.6px，与本复校真墨迹实测 23.0px / 30.8px 差 0.1–0.2px，属舍入差；间隙均为正、无重叠，门 5 通过不受影响。
- 记录 2：原校对观察 3（P7 金句 Q7 荷文译文删 `Duitse` 一词）仍属实，德语引文本身完整无损，不列为问题。

## 未宣称事项

本报告不宣称上架；上架由协调员串行执行。
