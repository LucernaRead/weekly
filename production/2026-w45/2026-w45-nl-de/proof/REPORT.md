# 独立校对报告 — Lucerna Weekly W45 NL × DE（荷兰语正文 × 德语讲解）

## 结论：ZERO PROBLEMS（可定稿）

本报告由独立校对员从渲染产物（SVG / 卡片 / PDF）与 SVG 坐标从头重测，构建员自述一律未采信为证据，
以下每一项均为本次实测值。9 道必查门全部通过，无编号问题。**本报告不宣称上架**（上架由协调员串行执行）。

- 校对对象：`files/weekly-report-w45-nl-de/`（svg × 8、cards × 8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-nl-core/`（W45 NL 核心，VOL.2，masthead De Lucerna；讲解层为中文，
  即 NL × ZH-CN 核心形态）
- 家具对照：`files/weekly-report-nl-de/`（W43 已发 NL × DE 版实测 SVG）
- SOP：`files/weekly-report-SOP.md`；工具：`tools/`（README #7–#22 已读；本次使用 freeze.py、occlusion_audit.py、p8.py，
  外加自写墨迹/同基线/图表扫描，见门 4）
- 校对员行为边界：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录、
  未派生任何下级代理。全部写盘只在 `hidden_files/w45/nl-de-proof/`（本报告与复测证据）。

### 开工查重（stand-down 判定）

- 开工时 `files/weekly-report-w45-nl-de/` 与 `hidden_files/weekly-report-w45-nl-de-build/` 均无进行中的写盘：
  无渲染进程作用于本分版；SVG 最新 mtime 21:27、KIT 21:31，经 90 秒以上复查零新写盘（后又间隔约 7 分钟再次确认无变化）。
- 复查时发现一个正在运行的 `render.py`，经 `/proc` 核实其工作目录是 `hidden_files/weekly-report-w45-nl-pt-build`
  （NL × PT 兄弟分版），与本分版无关，不构成 stand-down 理由；校对未干预该进程。

---

## 门 1 — Freeze：通过

- **核心基线（本次独立重跑 `freeze.py baseline`，经工具自身 repoint 安全路径）：8/8 字节复现**，
  核心 P1–P8 哈希与已发核心逐一相同（P1 `5424557b…`、P2 `78e6fcd2…`、P3 `5b9854e3…`、P4 `cc227fd9…`、
  P5 `e58064c9…`、P6 `6583fe28…`、P7 `65cfe2b3…`、P8 `fe22a151…`）；工具同时确认本次运行未改动已发核心 SVG。
  校对前后两次核心 SVG 全量重哈希亦一致（core-sha-before = core-sha-after）。
- **冻结 diff（本次独立重跑 `freeze.py diff`）：与构建员 KIT 计数逐页一致** —
  P1 +29/−28、P2 +43/−33、P3 +30/−27、P4 +29/−25、P5 +42/−34、P6 +37/−32、P7 +47/−45、P8 +181/−167；
  **新增 CJK 字符全页 0，全版 0**；全文 `桥接` 0、`讲解` 0、`译注` 0（8 页 SVG 全文扫描）。
- **删除串逐项裁定：纯非中文删除串恰为 8 个，与声称的 8 个换行碎片一一对应，逐项核实均为同句重排版，
  无荷兰语正文丢失**（其余删除串均含中文讲解层，属正常本地化替换）：
  1. P5 `1. Kijk zondag om 20:00 uur op RTL 4` — 本版实测同句完整存在：
     `1. Kijk zondag om 20:00 uur op RTL 4(am Sonntag um 20:00 Uhr auf RTL 4 sehen)`（德语括号前移了断行点，荷兰语句完整）。
  2. P6 孤 `）` — 本版实测图表说明完整：`… (100 jongeren) ÜBUNGSDATEN: …`，括号尾随断行重排，无内容丢失。
  3. P7 `bomen。` / `thuis。` / `zij zette vast。` / `。`（4 个）— 均为讲解行尾碎片；本版实测桥接句完整：
     `meedoen = teilnehmen: ik doe mee; opruimen = aufräumen: wij hebben opgeruimd; vastzetten = befestigen: zij zette vast.`
     且 PAS OP 纠正句逐字完整（见门 2）。
  4. P8 `6. planten — veel mensen → planten` — 本版实测 `6. planten — Plural, also planten`：键 `planten` 不变，仅注解本地化。
  5. P8 `voorgelezen` — 本版实测 `41. hebben voorgelezen — voorlezen Perfekt: hebben voorgelezen` 逐字完整。
- **加强验证（超出删除串清单）：核心 P1–P7 全部 102 条长度 ≥40 字符的纯拉丁荷兰语句，
  在本版合页文本中逐字存活 102/102**，无正文丢失。

## 门 2 — 核心层冻结专项（de-nl standing 裁定）：通过

- **核心原文（W45 NL 核心 P7，NL × ZH-CN 形态）**：词框定义句（核心 P7 文本行 118–120 合并）
  `«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.`
  其下讲解行（中文）为 `meedoen = 参加、参与：气候周全荷兰都参加。`
- **本版实测文本（本版 P7 文本行 119–122 合并）**：定义句**逐字保留**，与核心逐字节相同；
  仅其下讲解行本地化为德语 `meedoen = teilnehmen, dabei sein.`。**定义句未被删改、未被译成德语。**
- **与 NL × ZH-CN 核心对照结果**：定义句在核心（中文讲解版）与本版（德语讲解版）中逐字一致；
  差异仅在讲解层语言（中文 → 德语），符合 standing 裁定（目标语定义句冻结、仅 gloss 本地化）。
- **PAS OP 4 条荷兰语错句/纠正句逐字保留**（含 y 坐标与核心完全相同）：
  1. `«Het klimaat is slecht weer.»` → `→ Fout: het klimaat is het weer over een lange tijd.`
  2. `«Ik doe mee aan de klimaatweek.»` → `→ «Klimaatweek» krijgt een hoofdletter: het is een naam.`
  3. `«Ik plant een bomen.»` → `→ «Een» is enkelvoud: «een boom» of «bomen».`
  4. `«Omdat het regent, ik blijf thuis.»` → `→ Na «omdat» staat het werkwoord op plaats 2: «... blijf ik thuis.»`
  仅各条下的简短注解本地化为德语（第 3 条注解断行尾 `«bomen».` 即门 1 的 P7 碎片之一，纠正句本身完整）。

## 门 3 — P8：通过

- **本次独立重跑 `p8.py compare`：`CLEAN 150=150，missing=[]，extra_count=0，uncertain=[]`，
  keydiff = [7, 17, 70, 71, 76, 96, 137, 138, 148]**，与构建员声称完全一致；另独立重跑两版 `p8.py extract`，
  各自 noted set 均为 150/150。
- **逐项核实（以两版 P8 印刷行本身为准，不以工具 key 候选为准）**：
  - **7、17、70、71、76、96、148 — 确为 p8.py 括号分支提取伪影，通过。** 印刷键（` — ` 之前段）与核心逐字节相同：
    7 `B`、17 `wortelen`、70 `eiland`、71 `proef`、76 `gaat winnen`、96 `advies`、148 `B`；
    差异只在德语注解，且德语注解末尾确为 ASCII 括号组（7 `(2.–8. November)`、17 `(Plural)`、70 `(het)`、
    71 `(de)`、76 `(nur eine Vermutung)`、96 `(het)`、148 `(Boden)`），而核心中文注解用全角括号 `（）` 不触发该分支。
    伪影说法属实。
  - **137、138 — 真实重定向，有合法重定向理由，通过。**
    137 核心印刷 `137. 气候周持续七天。 — 对照第 1 版头条` → 本版 `137. Die Klimaatweek dauert sieben Tage. — Vergleiche die Schlagzeile auf Seite 1`；
    138 核心印刷 `138. 橙色预警意味着：做好准备。 — 第 2 版原句 · bereid je voor 做好准备` →
    本版 `138. Code Orange bedeutet: Bereite dich vor. — Originalsatz von Seite 2 · bereid je voor = bereite dich vor`。
    合法性依据（已核对 P8 E 区题干本身）：核心 E 区 137/138 题干为荷兰语句 + 中文指令“翻译”，答案为中文译文（NL→ZH）；
    本版题干荷兰语句冻结不变，指令改为 `Ins Deutsche übersetzen`，答案随之改为德语译文（NL→DE）——
    输出语言 = 读者母语，两版平行，属翻译题的正常重定向，非键错误。
    （137 德语译文 `Die Klimaatweek dauert sieben Tage.` 与荷兰语源句 `De Klimaatweek duurt zeven dagen.` 语义一致；
    138 `Code Orange` 为德语颜色词对应荷兰语 `oranje`，正是该翻译题的考点。）
  - **139、140 — 不在 keydiff，核实无误**：荷兰语键逐字节保留
    （`Museumnacht duurt van 19:00 uur tot 02:00 uur.` / `Ik doe mee aan de Klimaatweek.`），仅注解本地化为德语；
    且题干已同步重定向（核心中文源句 → 本版德语句 `Die Museumsnacht dauert von 19:00 Uhr bis 02:00 Uhr.` /
    `Ich mache bei der Klimaatweek mit.`，指令 `Ins Niederländische übersetzen`），键不变合理。

## 门 4 — 几何遮挡审计：通过

- **本次独立重跑 `occlusion_audit.py`（每次自检均 OK，6 类 planted 全部触发、clean 对照静默）**：
  分版 **0 flags**、核心 **0 flags**、`--core` 比较 **NEW 0**。
- **同基线墨迹碰撞扫描（自写，复用工具的真实墨迹 `ink_box`，非 advance 宽度）**：8 页同基线（同 y）文本对中，
  间隙 < 3px 者仅 1 对：P1 y=1436 `Musea bij nacht en boeken` 与 `A2→B1`，间隙 **+0.2px（正间隙，无重叠）**，
  且与核心同位置几何逐字节相同（墨迹右缘 1799.5 → 左缘 1799.7），属继承的冻结家具，非缺陷。
- **图表标签覆盖检查（基线锚定墨迹实测，修正量法）**：P6 全部文字按真实 paint 顺序，
  被后绘不透明矩形覆盖者 **0 项**（覆盖率 0%，严于构建员声称的“最差 0.0%”的 bbox 上限量法；
  初版扫描因误用文本列表序号代替 paint 序号曾误报背景框，修正后归零——审计结论以修正后的 paint 顺序为准）。
  图表条（45/25/20/10）与标签无接触（见卡面目视）。
- **P1 词条行与 IN HET KORT 框贴边（独立实测 + 裁图目视）**：
  德语词条第 2 行墨迹底 1872.2，IN HET KORT 框顶（stroke 外缘）1873.3，**间隙 1.1px**；
  行间分隔线 y=1852.4–1853.6，位于第 1 行墨迹底（1851.0）之下、第 2 行墨迹顶（1856.7）之上，穿行间空隙，不压任何字形。
  裁图（`crops/p1-graze.png`）目视确认：德语两行字形完整、框边在文字下方、无压盖。贴边但干净，通过。
- 另经裁图确认的 fix2 点：P2 匹配题指令 `Wort und Bedeutung zuordnen`（x=1647，墨迹宽 279.9px，右缘 1926.9，页内 23.1px，
  裁图 `crops/p2-edge.png` 在页内完整）；P6 框标题 `VOOR OF TEGEN? · PRO UND KONTRA` 在框内（卡面目视）；
  P7 金句第 0 行德语 + `(Pagina 1)` 单行、无悬空 `1)`（裁图 `crops/p7-golden-row0.png`）。

## 门 5 — Gloss：通过

按渲染后 SVG gloss 框文本本身以 `·` 拆分计数（前缀段计为首项，逐项与核心对照）：

| 页 | 核心（中文注解版） | 本版（德语注解版） | 结论 |
|---|---|---|---|
| P2 | 6：het klimaat / wortelen / besparen / de verwarming / de waarschuwing / lokaal | 6：相同 6 词，德语释义 | 6=6 ✓ |
| P3 | 5：het museum / de rondleiding / het tijdslot / tweedehands / de beurs | 5：相同 5 词 | 5=5 ✓ |
| P4 | 5：de balans / gelijkspelen / de speelronde / de topper / de stand | 5：相同 5 词 | 5=5 ✓ |
| P5 | 5：het eiland / de proef / stemmen / de aflevering / voorbij | 5：相同 5 词 | 5=5 ✓ |
| P6 | 5：de meteoroloog / waarschuwingsmoeheid / vastzetten / het advies / de voorstander | 5：相同 5 词 | 5=5 ✓ |

无 gloss 串引入额外 `·`；P6 gloss 框裁图（`crops/p6-glossbox.png`）显示 5 项全部在框内。

## 门 6 — P7 金句：通过

- 8 句荷兰语原文在本版中**各恰 2×**（源文章 1× + P7 表 1×），与核心总计数一致；每句均在其标注源页出现：
  P1 ×2（`Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland`、
  `De herfst is de beste tijd om te planten`）、P2 ×1（`Geel betekent: let op, het weer kan gevaarlijk zijn`）、
  P3 ×1（`Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts`）、
  P4 ×1（`Ajax won donderdag 22 oktober met 2–0 van Atalanta`）、P5 ×1
  （`Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur`）、P6 ×2
  （`Een code is geen verbod, maar een advies`、`Het weer is van ons allemaal, maar het raakt ons allemaal anders`）。
- 页码标签分布与核心一致（P1×2 / P2 / P3 / P4 / P5 / P6×2），标签形式均为 `(Pagina N)`；
  P7 金句德语译文行均为单行（fix2 后的第 0 行为 `Vom 2. bis 8. November ist in den Niederlanden Klimaatweek. (Pagina 1)`，裁图确认）。

## 门 7 — 读者园地：通过（绝不编造；显性邀请成立）

P7 BRIEVEN VAN LEZERS 框内（裁图 `crops/p7-brieven.png`，全部行在框边内）实测：

- **荷兰语示例信冻结逐字**：`«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)`，与核心逐字相同；无新读者、来信、姓名或引言被编造。
- **三事实同时在页（德语披露句，逐字）**：`Redaktionsschluss: keine echten Briefe, keine besten Seite-8-Texte — darum ein Beispiel; Versprechen für VOL.3.`
  ① 无真实来信（keine echten Briefe）② 无最佳 P8 作文（keine besten Seite-8-Texte）③ 刊登物为示例 + VOL.3 承诺
  （darum ein Beispiel; Versprechen für VOL.3）——三项齐全；荷兰语披露句亦冻结在页。
- **显性德语公开征集真实来信的邀请（逐字，框内独立句）**：
  `Beispiel der Redaktion, kein echter Brief. Schicke uns echte Briefe und beste Seite-8-Texte — wir drucken sie in VOL.3!`
  结构逐段核对成立：标签（`Beispiel der Redaktion, kein echter Brief.`，明示非真实来信）＋
  祈使（`Schicke uns echte Briefe und beste Seite-8-Texte`，第二人称命令式）＋
  刊登承诺（`wir drucken sie in VOL.3!`）。内容预告行（VOLGENDE WEEK）与其他页练习提示均未计入此邀请；
  邀请句本身位于 BRIEVEN 框内（y 1809.97–1866.77，框内、ZINNEN 规则线上方），构成显性邀请。
- 布局：征集句末行基线 1866.77（本版 P7 实测），ZINNEN 标题基线 1975（本版 P7 实测），其间无压盖（卡面目视）。

## 门 8 — 家具三方对照（以 W43 实测 SVG 为准）：通过

逐元素对照 W43 `files/weekly-report-nl-de/svg/` 实测值（非 README #20 泛写、非 tables.json 泛写、非构建员说法）：

- **徽章（插入式，非替换标语）**：W43 与本版逐属性一致 — 文本
  `NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`，
  x=975 / y=568 / 20pt / weight 700 / fill #a4553a / middle 锚定；墨迹跨度 462.3–1487.6（宽 1025.2px，
  构建员称 1025.4px，0.2px 为字体度量舍入差，跨度本身一致）。
  荷兰语标语 y=372（19pt，`DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS`）逐字保留。
- **顶条**：W43 与本版逐属性一致 — `ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH`，
  x=975 / y=92 / 21pt，墨迹宽 705.0px（构建员称 705.1px，舍入差）。
- **副标题**：本版 `NIEDERLÄNDISCH · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12`，
  40pt/700，墨迹宽 1643.8px（以正确 serif 族实测；构建员称 1644.0px，一致），< 1820px 内宽，
  **全部主题词保留（含 MUSEUMNACHT）**；VOL.1→VOL.2 为唯一合法变更。
- **页脚（8/8）**：`De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.2 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH`，
  与 W43 形式一致（仅 VOL.1→VOL.2），墨迹宽 1140.8px 与 W43 一致；无页脚读 VOL.1。
- **页码行（8/8）**：`Seite N von 8`，与 W43 一致（非 tables.json 泛写之外的任何形式）。
- **Gloss 前缀**：W43 实测为 `Hinweis · `（P2 首行 `Hinweis · het ezelsbruggetje = …`），本版同为 `Hinweis · `；
  **W43 实测胜过 tables.json 的 `HINWEIS · `**，本版采用 W43 形式，正确。
- **P8 分隔行（8 条）**：W43 与本版均为 `— PAGINA N —` 形式；tables.json 的德语分隔 `— SEITE N —` 未采用，
  与两版已发先例一致。唯一差异：字号 W43 为 14pt、本版为 13.5pt，属 KIT §6 fix2 记录的字体收紧（与 P8 键字号同步），
  形式与文案未变，不列为家具不符。
- **P8 答案体例**：dash 式（`N. key — note`），与 NL 核心一致。

## 门 9 — PDF / 卡片：通过

- **双 PDF 各 8 页**（pypdf 实测）：印刷 PDF `De-Lucerna-VOL2-DE.pdf` 7,918,211 B，SHA-256
  `4708ee95814b843a163ef6d3433783276068e8a824584a1e1155b5e0ff71c870`；
  网页 PDF `De-Lucerna-VOL2-DE-web.pdf` 3,691,075 B（< 10 MB），SHA-256
  `c2fed9ab18fdaf2f279231818f103329c295a9cccb87e5a7f40af457d7c5433d`；均与 KIT §7 一致。
  版心：印刷 1462.5×2025pt（= 1950×2700px）、网页 1400×1938pt，均与核心同名 PDF 完全相同。
- **SVG 哈希**：8 个 SVG SHA-256 与 KIT §7 逐一相同；**卡片哈希**：8 张 PNG SHA-256 与构建目录 final 交付清单逐一相同。
- **卡片**：8 张均为 1950×2700，**全部目视**（半幅全页 + 5 处全分辨率裁图）：无重叠、无截断、无压盖；
  P1 徽章/标语/照片署名、P2–P4 照片署名、P6 图表、P7 词框/读者园地/金句、P8 答案区与范文均完整。
- **题量与分页（从 SVG 题号独立重测，与核心逐页相同）**：P1 10（1–10）、P2 18（11–28，含 25–28 匹配题组）、
  P3 18（29–46）、P4 18（47–64）、P5 18（65–82）、P6 18（83–100）、P7 12（101–112）、P8 38（答案 113–150 区），
  合计 **150 题**，编号连续 1–150，P8 答案号 1–150 无缺失；
  等级标签在 P1–P7 的 108 个带级题号上与核心逐一相同（A2 35 / B1 48 / B2 25），结合 P8 与匹配题组的注册表总量，
  与核心 KIT 的 A2 47 / B1 72 / B2 31 一致。
- **ABSTRACT.txt**：德语单行（329 字符，1 行 + 换行结尾），无 ASCII 双引号；
  含真实主题关键词（Klimaatweek 11 月 2–8 日、Museumsnacht Amsterdam 11 月 7 日、Crossing Border Festival、
  Eredivisie 第 12 轮）与学习者搜索短语（`Niederländisch lernen`、`Niederländisch durch Lesen lernen`），
  含 masthead（De Lucerna）、级别（A2–B2）与题量（150 Übungen）。
- **图片署名行（与核心逐字一致且确已排版）**：P1 `Foto: Vovogov90 — CC0`、P2 `Foto: Nationaal Archief — CC0`、
  P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`、P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein`
  （P4 署名跨两行排版，卡面目视完整）。

---

## 非问题的实测注记（已裁定，不列入问题清单）

1. 徽章墨迹宽 1025.2px（构建员称 1025.4px）、顶条 705.0px（称 705.1px）、副标题 1643.8px（称 1644.0px）：
   均为字体度量舍入差，跨度与属性本身与 W43/核心一致。
2. P1 词条行与 IN HET KORT 框间隙仅 1.1px：贴边但墨迹与框边、分隔线与字形均无接触，裁图确认字形完整，属干净通过。
3. P1 同基线 0.2px 正间隙：与核心几何逐字节相同，属继承家具，非缺陷。
4. P8 分隔行字号 13.5pt（W43 为 14pt）：属已记录的 fix2 字体收紧，形式与文案未变。
5. P2 题号正则初测仅得 14 项（11–24）：因 25–28 为匹配题组（题头 `25–28.` + 指令行），经题组行核实 18 题齐全，与核心相同，属量法 artifact。

## 问题清单

无。**ZERO PROBLEMS — 可定稿。**

## 复测证据（本目录）

- `core-sha-before.txt` / `core-sha-after.txt`（核心前后哈希一致）
- `freeze-diff.json`（冻结 diff 全量）
- `occlusion-edition.json` / `occlusion-core.json` / `occlusion-new.json`（遮挡审计）
- `p8-core.json` / `p8-ed.json`（P8 提取）
- `check_texts.py` / `scan_extra.py`（删除串、长句存活、同基线、图表覆盖扫描）
- `baseline-nlcore/`（freeze baseline 8/8 复现输出）
- `crops/`（卡面半幅 ×8 与裁图：p1-graze、p2-edge、p6-chart、p6-glossbox、p7-golden-row0、p7-brieven）
