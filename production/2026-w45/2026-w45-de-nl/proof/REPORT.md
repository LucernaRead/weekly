# 独立校对报告 — Lucerna Weekly W45 DE×NL（德语×荷兰语）

**结论：不可定稿 — 存在 1 项冻结类阻塞问题（见问题 1）。其余 8 门必查全部通过；另有 3 条非阻塞观察（KIT 文字修正，无需重渲染）。**

- 校对对象：`files/weekly-report-w45-de-nl/`（svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-de-core/`（Die Lucerna VOL.2，150 题）
- 校对方式：全部结论均从渲染产物 / SVG 坐标独立重测得出，构建员自述未被采信；凡构建员说法与实测不符处，本报告以实测为准。
- 纪律：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录。开工前查重：开工时确有一个进行中的 `render.py` 进程，但其 cwd 为 `hidden_files/weekly-report-w45-de-pt-build`（DE×PT 版，与本版无关）；本版目录在 100 秒复查窗口内零新写盘（最新 mtime 20:48:32，复查时已逾 120 秒），故正常开工，非 stand-down 情形。
- 证据存档：本目录 `occlusion.json`（遮挡审计）、`freezediff.json`（冻结差分）、`baseline-core/`（核心基线重跑）。

## 问题清单（阻塞）

### 问题 1（门 1 冻结失败）：P7 NOCH EIN WORT 框的德语定义句被删除并改写为荷兰语，且所引 DE×EN 先例不实

- 核心 P7 NOCH EIN WORT 框（x=1473，框 y=1329–1479）原文三行：
  - `«der Tankrabatt»（Seite 2）: die`
  - `gesenkte Steuer auf Benzin und Diesel.`
  - `油价减税。`
- 本版 P7 同框（框 y=1354.5–1504.5）改为：
  - `«der Tankrabatt» (pagina 2): de`
  - `verlaagde belasting op benzine en`
  - `diesel. Brandstofkorting.`
- 即：德语定义句 `die gesenkte Steuer auf Benzin und Diesel.` 被整句删除，替换为荷兰语释义。这不是家具，也不是母语讲解层（讲解层是第三行的母语 gloss `油价减税。`→`Brandstofkorting.`，该行已正确荷文化）。被删句是目标语德语内容句：按 SOP §3“换母语只译讲解层，核心层不动”，德语内容句应冻结。
- 先例核查（实据，非照抄）：
  - KIT §3/§12 称“W45 DE×EN 同族版作同样处理”——**不实**。实测 W45 DE×EN P7 同框仍逐字保留德语句：`«der Tankrabatt» (Seite 2): die` / `gesenkte Steuer auf Benzin und Diesel.` / `Fuel discount.`（y=1432.5/1461.61/1490.72，与核心同坐标系）。
  - DE×ES、DE×IT 同样逐字保留该德语句（ES KIT 亦明文裁定该句“本身存续”）。
  - DE×FR、DE×PT 确与本版同样荷/法/葡文化了该句，但 FR、PT 均为 builder-complete、未定稿（PT 甚至无 KIT），不是已接受的先例，不能作为放行依据。
- 修复要求：恢复德语定义句（按核心/EN 版两行排布），保留荷兰语 gloss `Brandstofkorting.`；改后按 SOP §8.4 整期重渲染并从头再做一轮全量校对。**在修复并重校通过前，本版不可定稿、不可上架。**

## 必查门实测值

### 门 1 冻结
- 核心基线：`tools/freeze.py baseline --build hidden_files/weekly-report-w45-de-build`（核心真实构建树）→ **8/8 SVG 逐字节复现**，核心前后哈希一致（开工前与收尾复核 8 页 sha256 逐项相同，见下）。
- 核心哈希（收尾复核，与开工前一致）：p1 `6cbd4802…`、p2 `9362256d…`、p3 `3e8a8d16…`、p4 `b787f592…`、p5 `4dcbeb97…`、p6 `01b75ad4…`、p7 `fbaf8cdd…`、p8 `299524bd…`。
- 冻结差分（`freeze.py diff`，终版 JSON 见 `freezediff.json`）：P1–P8 新增 CJK **0**，各页版内 CJK 核心 N→本版 **0**（P1 168、P2 186、P3 187、P4 155、P5 193、P6 228、P7 394、P8 1429 → 全部 0）；SVG 全文“桥接”0 次（KIT 内 2 次为元语言提及，见观察 2）；P1/P4 内嵌图片数据与核心逐字节相同。
- P1–P7 纯拉丁删除串逐项裁定（除问题 1 外全部通过）：
  - P1 唯一 1 条：`DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND`——核心 P1 原生副题槽节点（x=975 y=372，19pt #57523f），被徽章原位替换，属家具替换，通过（W43 同配对先例亦同槽）。
  - P7 另 2 条：`Ein Beispiel der Redaktion!`——读者框标签（核心 P7 LESERBRIEFE 框内 y=848.5），本版同坐标改为 `Een voorbeeld van de redactie!`，属家具本地化，通过（DE×EN 亦改为 `An example from the editors!`，先例属实）；`……`——中文省略号绕排碎片，属讲解层碎片，通过。
  - P2–P6 纯拉丁删除串 **0 条**；P8 纯拉丁删除串 **0 条**。其余全部删除串均含中文（讲解层）或为双语串绕排碎片。无德语文章正句丢失（文章段落均为纯德语串，删除清单中除问题 1 的词框定义句外无其他德语内容句）。
  - 新增串（P1–P7）全部为荷文讲解、家具，或双语 gloss 串内的德语词头，无新增德语正文句子。

### 门 2 P8
- `tools/p8.py compare`：**CLEAN 150=150**，missing=[]、extra=0、uncertain=[]、keydiff=[137, 138, 139, 150]；`extract` 两边均为 150/150。
- keydiff 逐项实印核实，全部为真实重定向，无括号/dash 提取伪影：
  - 137：题干 `Der Tankrabatt läuft bis Dezember.` + 指令 `Vertaal naar het Nederlands` → 键 `De brandstofkorting loopt tot december.` + 注 `(laufen = duren)` ✓
  - 138：题干 `Ich schaue am Dienstag Fußball.` + 指令 `Vertaal naar het Nederlands` → 键 `Ik kijk op dinsdag voetbal.` + 注 `(schauen = kijken)` ✓
  - 139：题干 `Die Schule hat wieder begonnen.` + 指令 `Vertaal naar het Nederlands` → 键 `De school is weer begonnen.` + 注 `(wieder begonnen = weer begonnen)` ✓
  - 150：写作 apparatus 键 `Open opdracht — zie de punten in het schrijfblok; de voorbeeldtekst staat in het schrijfblok op deze pagina` + 注 `(Beoordeling op basis van de punten)` ✓
  - 140 正确不在 keydiff 内：题干荷兰语 `Ik slaap op zondag een uur langer.` + 指令 `Vertaal naar het Duits` → 键德语不变 `Am Sonntag schlafe ich eine Stunde länger.`，注改为荷兰语在前 `(een uur langer slapen = eine Stunde länger schlafen)` ✓
- 键注粘连形式（`December.(laufen …`、`149. A(gehe …`）与 DE×EN 同族版实印逐字一致，属家族排法，非伪影。

### 门 3 几何遮挡
- `tools/occlusion_audit.py`（自检先行通过，6 类 planted flags 全触发）：**分版 0 flags、核心 0 flags、NEW vs core 0**。
- 同基线墨迹碰撞扫描（P1 顶带，README #10 类）：y=92 三段、y=478、y=522、页脚 y=2624 四组同基线文本，墨迹间距全部为正（y=92 间隙 200.8px / 93.9px；y=478 间隙 801.8px；y=522 间隙 605.6px；页脚间隙 783.7px），同基线重叠 **0**。
- P6 图表标签 vs 后绘条形（条形起点 x=535，逐项实测墨迹右端）：familiezorg 528.8（间隙 **6.2px**）、thuiszorg 512.0（间隙 **23.0px**，KIT 记 23.1px，0.1px 舍入差）、zorghuis 504.2（间隙 **30.8px**，KIT 记 30.6px，0.2px 舍入差）；与后绘矩形重叠 **0**，三标签目视全部脱离条形。
- P1 顶带同基线扫描：见上，0 重叠。

### 门 4 Gloss
- 按渲染后 `gloss()` 调用串本身以 `·` 拆分：共 5 处调用 × 每处 5 项 = **25 项**，与核心 **1:1**，德语词头逐项对应（P2 Tankrabatt/Zapfsäule/Energiesteuer/Mehrwertsteuer/Angehörige；P3 Ferienwechsel/Schülerin/Ausflug/Advent/Lesung；P4 Englische Woche/auswärts/empfangen/Favorit/eröffnen；P5 Pausenhof/Klassenarbeit/Referat/ausschlafen/Probe；P6 Angehörige/Pflegeversicherung/Pflegedienst/Stagnation/Aufschwung）。
- 注意：gloss 页实为 P2–P6（content12.py 第 173 行属 P2 章节），KIT §6 所写“P1 5”为页码笔误，见观察 1；总数与逐项对应不受影响。

### 门 5 P7 金句
- 8 句德语原文在核心与本版中位置逐字相同（P7 表 y=1597/1801 四列），全刊出现次数核心与本版均为 **2, 2, 2, 2, 2, 2, 2, 2**（源文章 1 次 + P7 表 1 次）。
- 页码标签分布与核心一致（按表列顺序）：Seite 4·B1、Seite 2·A2、Seite 2·A2、Seite 5·B1、Seite 3·A2、Seite 4·B1、Seite 6·B2、Seite 6·B2；逐句核对：每句的源文章出现页 = 其标签页（Q1→P4、Q2→P2、Q3→P2、Q4→P5、Q5→P3、Q6→P4、Q7→P6、Q8→P6），全部逐字取自本期文章。
- P7 右栏终值实测：NOCH EIN WORT 框 rect y=1354.5 + h=150 = **1504.5**，与 KIT 称一致；金句区横线 y=1508（x 65→1885），右栏框底低于横线 3.5px，无顶线。读者框底 1338.5，征集句基线 1331.11 在框内，距下框顶 1354.5 有 16px 间隙。

### 门 6 读者园地
- 页上三事实齐全（荷文事实句实印）：`Geen echte brief: nog geen brieven of beste pagina-8-tekst; belofte naar VOL.3.`——无真实来信（nog geen brieven）、无最佳 P8 习作（beste pagina-8-tekst 在 nog geen 否定辖域内）、VOL.3 承诺（belofte naar VOL.3）；示例身份由标签句 `Een voorbeeld van de redactie!`（与核心标签同坐标 y=848.5）明示。
- 显性荷兰语公开征集句实印（读者框内，y=1331.11）：`Schrijf ons! Stuur je echte brieven in!`——祈使 + 明确对象（真实来信），构成显性邀请，判定成立。内容预告栏德语 `Schreiben Sie uns!`（P7 底 y=2511.4，冻结德语）与各页 UND SIE? 提示均未计入，征集成立不依赖它们。
- 无编造：示例信正文（`„Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético…`）与核心逐字相同；无新增读者人名/引言。

### 门 7 家具三方对照
- 徽章节点与 W43 已发同配对版 `files/weekly-report-de-nl/svg/p1-front.svg` **逐属性一致**：x=975 y=372、Noto Sans CJK SC、20pt、bold、fill #a4553a、居中，字符串逐字相同：`TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`。W43 实测胜过 README #20 泛写值 19.5pt（本版取 20pt 正确，属 DE 家族原生副题槽情形）。
- 页脚 8/8：`Die Lucerna · DUITS WEEKBLAD VOL.2 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS`；页码行 8/8：`Pagina N van 8`；masthead 8/8：`Die Lucerna`（目标语德语冠词正确）。

### 门 8 构建轮自修复复核（终版逐项无残留，除问题 1 外）
- P1 流溢出：头条、Fragen 框、quiz 7–10 目视完整；遮挡审计 0 旗（BOXTITLE 类无触发）。
- P8 题头超宽：B 头墨迹右端 433.5、C 头 880.2，全部题头墨迹右端 ≤1850（F 头 1850.0 为最右，页内 1885 以内），无超宽。
- 初版 16 个 occlusion 旗：终跑 0 旗。
- P7 右栏超高：终值 1504.5，低于金句横线 1508（见门 5）。
- P6 图表标签被条形盖住：已无重叠（见门 3）。
- P3 TIPP 框底越练习区金线：终版 TIPP 框 rect y=1444.6、底 **1583.66**，与核心逐值相同；练习区金线 y=1608，间隙 **24.34px**；UND SIE? 荷文提示确为 2 行。

### 门 9 PDF / 卡片 / 题量 / ABSTRACT
- 印刷 PDF `Die-Lucerna-VOL2-NL.pdf`：**4,138,982 B、8 页、1462.5×2025 pt**，sha256 `2f806c5df6e44c7d2e2effd5a61d47156a97bf654931ed2476860318720e5610`，与 KIT 一致。
- 网页 PDF `Die-Lucerna-VOL2-NL-web.pdf`：**4,140,214 B（<10 MB）、8 页、1400×1938 pt**，sha256 `f5c3d7603cb61d93556ac6f1c44788a5094b2c788196af7d9e5e8167712e7bfa`，与 KIT 一致。
- 卡片 8 张：1950×2700 PNG，**全部目视**——P1 徽章/副题/顶带/头条/数字框/Fragen 框/照片+出处/quiz、P2 UND SIE?/RECHNEN 宽框/gloss 框/练习区、P3 TIPP 框与金线间隙、P4 赛程表/UND SIE?/练习区、P5 周计划宽框/UND SIE?/练习区、P6 图表三标签/免责声明单行/练习区、P7 读者框 6 段/词框/金句格/诊所/预告、P8 测验区/写作框+范文/全部答案键——无重叠、无截断。
- 150 题分页：徽章计数 P1 10（1–10）、P2 18（11–28）、P3 18（29–46，另有一枚与核心相同的正文内 `4.` 数字，非习题）、P4 18（47–64）、P5 18（65–82）、P6 18（83–100）、P7 12（101–112）、P8 38（113–150），合计 150，与核心一致；习题德语题面冻结，级别徽章未变，故 A2 66 / B1 70 / B2 14 分布与核心一致。
- ABSTRACT.txt：荷兰语单行（353 字符，1 个结尾换行），无 ASCII 双引号，含真实主题关键词（voetbalweek、Champions League、Europa League、Bundesliga speeldag 9、brandstofkorting tot 31 december、vakantiewissel、zorg thuis）与学习者搜索短语（`Duits wil leren door echt Duits nieuws te lezen`），含刊名、目标语名、A2–B2、150 oefeningen。

## 非阻塞观察（不影响阻塞结论，但请随修复一并修正，无需重渲染）

- 观察 1：KIT §6 gloss 页码笔误——“P1 5”应为“P2 5”（gloss 调用在 content12.py 的 P2 章节；总数 25=25 与逐项对应无误）。
- 观察 2：KIT §13“本 KIT 中『桥接』出现 0 次”自相矛盾——KIT 第 185 行（“桥接句删……”）与第 216 行（该断言本身）共出现 2 次；交付 SVG 中确为 0 次。建议 KIT 改用“讲解”表述，删除该词。
- 观察 3：P7 金句 Q7 荷文译文删 `Duitse` 一词（`De economie komt langzaam uit de stagnatie…`，KIT 已披露理由；德语引文本身完整无损，译文在上下文中无歧义）。不列为问题，仅记录。

## 未宣称事项

本报告不宣称上架；上架由协调员串行执行。本版在问题 1 修复并经新一轮全量校对通过前，不得定稿。
