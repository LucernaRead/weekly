# 独立校对报告 — Lucerna Weekly W45 · IT×NL（意大利语目标 × 荷兰语读者）

**结论：ZERO PROBLEMS**（无阻塞项；全部 12 门禁通过。文末列 10 项非阻塞差异/观察，均不构成 NOT PASS。）

- 校对对象：`files/weekly-report-w45-it-nl/`（svg×8、cards×8、print PDF 7,171,144 B、web PDF 3,597,474 B、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-it-core/`（VOL.2，W45 IT 核心）
- W43 同配对对照：`files/weekly-report-it-nl/`（VOL.1，已上架）
- 校对方式：从头独立重测，**不采信构建员自述代替重测**。共享工具（freeze.py / p8.py / occlusion_audit.py）各跑一遍，另写独立测量脚本交叉验证（自有 SVG 解析 + PIL 4× 墨迹度量，不 import 上述工具）。
- 纪律：只校对、不改源码、不宣布上架；未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）；未清理共享 scratch 目录。

## 0. 开工查重（stand-down 判定）

- 首次检查时，`files/weekly-report-w45-it-nl/` 与 `hidden_files/weekly-report-w45-it-nl-build/` 的最新 mtime 为 2026-10-27 23:52–23:56；运行中的渲染进程是 EN×ES 与 IT×RU 分版，与本版无关。
- 90 秒复查：**零新写盘** → 判定为已完成交付的新鲜 mtime，安全开工，未 stand down。
- 校对前后哈希比对：交付物 8 SVG + 8 卡片 + 2 PDF 与核心 8 SVG **全部不变**（见 `hash-before.txt` / `hash-after.txt`，diff 为空）。

## 1. 冻结门禁 — 通过

- **freeze.py baseline（独立重跑，核心构建目录 `hidden_files/weekly-report-w45-it-build`）**：`baseline: 8/8 SVGs byte-identical`，核心 8 文件跑前跑后重哈希一致，未被写穿。见 `freeze-baseline.txt`。
  - p1 `81051bbb…`、p2 `d42ce9ae…`、p3 `9e45586d…`、p4 `62f75269…`、p5 `c907b869…`、p6 `5545f8dd…`、p7 `9fc999f4…`、p8 `3b87e54f…`，与构建员 `core-svg-baseline.txt` 逐项一致。
- **freeze.py diff（独立重跑，全量输出见 `freeze-diff.txt` / `freeze-diff.json` / `freeze-diff-full.txt`，无截断）**：
  - 新增 CJK：8 页全部为 0；交付物 CJK：8 页 SVG 全部为 0（见 §1b）。
  - 页增减串数：P1 +27/−27、P2 +33/−29、P3 +33/−31、P4 +28/−25、P5 +42/−35、P6 +27/−24、P7 +45/−41、P8 +179/−175。全部增串均为荷兰语家具/讲解或意大利语引文；删串逐项裁定见下表。
- **删除串逐项裁定**（拉丁文删串逐条核对意大利语存活情况，见 `audit-full.txt` §U）：
  - P1 徽章替换：核心 372 槽 strapline `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA` 被徽章替换（专项裁定见 §8；W43 同配对亦无此句在版）。
  - P1 其余删串：全部为中文讲解→荷兰语（桥句、cifre 括号、settimana 脚注、版带尾缀、页脚、页码行、quiz 说明）。桥句现为 3 行（`Uitleg — il primo freddo = eerste kou · il` / `versante adriatico = Adriatische kant · la` / `previsione = prognose · assaggi = proeven.`），与核心行数一致。
  - P2–P6 删串：全部为中文讲解→荷兰语（版带尾缀、gloss 前缀、指令词、E TU? 提示、练习说明）。纯意大利语重排碎片均存活：P6 `bollettino · modello` 在版内重组后仍存在；P7 `è probabile che / è possibile che / bisogna` 拆分于荷兰语诊所行（`Na è probabile che, è possibile che en` / `bisogna che staat de aanvoegende wijs; na so` / `che en scrivono che de aantonende wijs.`），意大利语触发短语一字未失。
  - P7 删串：中文诊所注释→荷兰语；核心中文披露句→荷兰语披露句（见 §6）；gloss 中文→荷兰语；其余为家具尾缀。
  - P8 删串：中文注释→荷兰语；**7 条全角 `：`→半角 `:` 标点归一逐项核实**：#17 `mettere：io → metto`→`mettere: io → metto`、#18、#19、#20、#60、#61、#103（`nevicare：nevica`→`nevicare: nevica`）全部一致，均为讲解层标点，非正文；分隔符 `— PAGINA N —`×8 → `— Pagina N —`×8（家具）；#139 题干重定向（见 §3）；#140 题干中文→荷兰语、意大利语 key 保留。
  - **除徽章槽 strapline 与 #139 题干（转为 key）外，无任何意大利语正文串丢失。**

### 1b. 桥接与 CJK（独立重测）

- 8 页 SVG：`桥接` 均为 0；CJK 字符均为 0。
- print PDF（pypdf 逐页提取，8 页）：每页 `桥接` 0、CJK 0。
- web PDF：**无文本层**（每页 1 个 raster XObject，mediabox 1400×1938，pdftotext/pypdf 提取均为 0 字符）——这是图片型 web 版的固有形态，其 pypdf“0”为空真；内容改以 SVG 源 + 8 张卡片目视验证（见 §12），不以此冒充文本检查。
- ABSTRACT.txt：`桥接` 0、CJK 0。
- WEEKLY-KIT.md：`桥接` 0；**CJK 字符 = 1，非构建员所称的 0**——唯一一处是 KIT §5 正文里用反引号引用的全角 `：`（讨论归一化本身的元语言引用），非报纸内容。列为非阻塞差异 D3。

## 2. P7 词框硬性门 — 通过

- 定义句逐字保留（精确句级比对，非含 gloss 的跨度比对）：
  - 核心与本版完全一致：`« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone.`（identical: True）
- gloss 本地化且仅 gloss 本地化：`assaggio = proeven (gratis, p. 3).`（核心：`assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。`，原为 2 行；本版在 390px 实宽下为 1 行）。
- +3px 内边距实测：构建代码 `content7.py` L81，核心 `… * 29 + 20` → 本版 `… * 29 + 23`，仅尾常数 +3（另 letter box `ly = wy + wh + 26` 随之 +3，见 §4）；渲染几何：gloss 墨迹底 1285.6，框绘制底边 1287.5（**净空 1.9px**；含半线宽扩张框底 1288.2，净空 2.6px），BOXTITLE 门限（0.5px）通过，卡片目视框内无溢出。净空偏紧，列为观察 D4，不阻塞。
- 金句 8 句各 2×、标签与核心一致（独立提取 P7 FRASI 块 8 句，剥离 «» 后在 P1–P6 定位 + 全报计数）：
  - `arriva il primo freddo vero della stagione` — P1，计 2；`Non è una certezza, è una probabilità` — P1，计 2；`il 2 novembre è la Commemorazione dei defunti` — P2，计 2；`Fa freddo, copriti bene!` — P2，计 2；`il pubblico può assaggiare gratis` — P3，计 2；`il calcio non si ferma per il primo freddo` — P4，计 2；`la cultura continua` — P5，计 2；`Una probabilità alta non è una certezza` — P6，计 2。标签序列 **1,1,2,2,3,4,5,6**，与构建员自述一致。

## 3. P8 — 通过（CLEAN 150=150；17 项逐项对照见下）

- **p8.py compare（显式路径重跑；`--target nl` 模式会误找 NL 目标自身的 `p8-toets.svg` 而报错，属工具调用口径问题，非交付物缺陷，见 D9）**：
  - `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 83, 84, 102, 137, 138, 139]`，与构建员一致。见 `p8-compare.txt`。
- **注册表独立重测**（将本版构建与核心构建分别拷入校对目录、重定向 OUT 后单进程重跑，`reg-ed.json` / `reg-core.json`，`reg-diff.txt`）：
  - 总数 150=150；页分布 10/18/18/18/18/18/12/38 一致；级别 A2 47/B1 70/B2 33 一致；页差异 []、级别差异 []。
  - **key 差异恰为 [137, 138, 139, 150]**；**注释差异 148/150，不变者恰为 #85 `12 − 9 = 3`、#86 `4 + 5 = 9`（纯算式）**；类型差异 150/150（荷兰语类型名，设计如此）。
- **工具 17 项与注册表 4 项之差的机制**（已读 `p8.py` `detect_note`/`compare` 源码并逐项贴线验证）：
  - 工具 key 的取法：dash 体先按 ` — ` 切分；但若句段尾有括号组（全角或半角）且最后一处 ` — ` 落在括号组**之前**，则改走 paren 分支，key = 括号组起点之前的全部文本——即 key 把本地化注释的前半截也吞了进去。于是注释一本地化，工具 key 即“差异”，虽印刷 key（` — ` 之前部分）逐字节相同。
  - 14 项伪影（印刷 key 逐字节同核心，差异全在注释内）：
    - 复数标记括号：#6 `previsioni`（`previsioni = 预报（复数）`→`voorspellingen (meervoud)`）、#13 `guanti`、#14 `crisantemi`、#15 `termosifoni`、#38 `mandorle`、#71 `gratuiti`（`gratuiti = 免费的（阳性复数）`→`gratuiti = gratis (mannelijk meervoud)`）、#74 `castagne`。
    - 全角冒号 + 括号：#16 `fa`（`fare freddo：fa freddo（天气）`→`fare freddo: fa freddo (weer)`）、#20 `resta`、#77 `ci sarà`。
    - 主观评价括号：#58 `più bella`（`周日晚最美（主观评价）`→`zondagavond is het mooist (mening)`）。
    - 本版注释新增括号而核心无括号（不对称 paren 分支）：#83 `B`（核心无括号；本版 `Koudste voorbeeldstad is Turijn (3°)`）、#84 `A`（本版 `(12°)`）、#102 `fa`（本版 `het is koud (weer)`）。
  - 3 项真重定向（注册表 key 亦差异，合法）：#137 IT→NL，`Op maandag komt de eerste kou.`（注 `zie de originele zin`）；#138 IT→NL，`Het publiek kan gratis proeven.`（注 `assaggiare gratis = proeven`）；#139 反向 NL→IT，荷兰语题干 `Op zondagavond speelt Fiorentina tegen Juventus. → ___`，意大利语 key `Domenica sera si gioca Fiorentina–Juventus.`（注 `si gioca = er wordt gespeeld`，印刷为 2 行，符合 KIT“#139 特意保留 2 行”）。
  - #140 不在工具 keydiff 内：印刷 key `Ogni previsione deve essere chiara.` 两版一致（注 `dovere = moeten`），注册表 key 亦一致。
  - #150 不在工具 keydiff 内但在注册表 key 差异内：工具对 `✓` 开头句段一律取 key=`✓`，故看不见占位符翻译；注册表 key：核心 `（开放题，范文如下）` → 本版 `(open vraag — het model staat hieronder)`，按 W43 规则翻译；印刷行 `150. ✓ Het model staat in sectie H van deze pagina (81 woorden)`。
  - **#139 来源标注差异（非阻塞 D2）**：本版意大利语 key 与**核心 P8 E 区题干**逐字节一致（核心构建 `content8.py:74` 与核心 P8 印刷行 `Domenica sera si gioca Fiorentina–Juventus. → ___`），但在核心与本版的 P4 SVG 中**不存在**与之逐字节一致的文本节点（P4 最接近节点为赛程行 `Domenica 8 novembre · Genoa – Milan; Inter – Como; Fiorentina – Juventus (sera, a Firenze).` 与练习行 `Domenica sera, a Firenze, si gioca... A.`）。即“与 P4 题干逐字节一致”的说法在字面上不成立；实质成立的是“与核心 E 区原句逐字节一致”，key 本身为真实核心意大利语、反向合法，故不阻塞，仅修正说法。
- P8 注释语言：8 页 SVG CJK=0；P8 印刷注释除意大利语引文词头外均为荷兰语；分隔符 `— Pagina N —`×8；E 区题干：#137/#138 意大利语（与核心一致）、#139/#140 荷兰语（反向对）。

## 4. 几何 — 通过

- **共享工具版本核查**：`tools/occlusion_audit.py` mtime 2026-10-27 23:39（IT×JA 构建中改动处为 `shape_box` 的 path 相对命令解析，附注说明此前误读造成 IT×JA P1 31 个假 COVER 旗）。本版 SVG 仅 P1 含 1 条 path，且全为绝对 M/L 命令——新旧解析结果相同，**版本问题对本版无实质影响**；且下述独立审计（自写 path 解析，含相对命令处理）结果与工具一致。
- **occlusion_audit.py（独立重跑，自检通过）**：分版 **0 flags**、核心 **0 flags**、`--core` 比较 **NEW 0**。见 `occ-ed.txt` / `occ-core.txt` / `occ-new.txt` / `occ-selftest.txt`。
- **独立几何审计（自有代码，`audit-full.txt` §D，全量输出）**：核心 0、 本版 0（COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE 六类全覆盖）。
- **同基线碰撞（自写同基线扫描，全量）**：核心 7 = 本版 7，逐项相同，均为 P1 sommario `Pag. N` <> 标题对，gap 4.0px（既定版式，非缺陷）。
- **P6 图表标签覆盖（基线锚定墨迹法，PIL getmetrics，anchor ls；紧墨迹与 ls 框双口径）**：核心与本版最差覆盖均为 **0.0%**（门限 <30%），无 >0% 项。
- **全 8 页框线压框 + 右缘扫描（ADVANCE 法，全量）**：
  - 框线越界（>1910）：核心 0、本版 **0**。
  - 构建员右缘脚本重跑：与构建员自述一致（本版 5 条 margin、核心 4 条）。但该脚本用 `svglib._font` 对非整数字号**取整**（21.5→22、19.5→20、15.5→16），系统性高估 advance（最大 14px）。**精确字号重测（4× 字体，含 letter-spacing）**结果如下，结论更强：
    - P1 y=1728 `« il primo freddo » : il primo freddo serio`：构建员 1889.3 → 精确 advance/墨迹 **1879.5**，在 1885 内容边内（非 margin，系取整伪影）。
    - P1 y=1758.1 `dopo un autunno mite. Questa settimana`：构建员 1888.8 → 精确 **1879.0**，在 1885 内。
    - P2 y=1927 新增荷兰语指令 `Koppel woord en betekenis`：构建员 1900.7 → 精确 advance **1894.3**、墨迹 **1894.2**。即：距 1910 页框 **15.7px 内**、但超出 1885 栏边 **9.3px**（与继承的 P2 y=2195 行同类：该行精确值 1902.5，超栏边 17.5px、距页框 7.5px）。无重叠（TEXTX 0）、未越页框，**不阻塞**；构建员“距框线 9.3px”的表述混淆了 1885/1910 两条边，特此澄清。
    - P8 H 标题（本版 y=662.825，核心 y=633，同一冻结行、荷兰语 P8-ex 流程下移 30px）：构建员 1898.6 → 精确 advance **1884.6**、墨迹 **1884.5**，在 1885 内仅 0.4–0.5px（紧但通过；冻结文本，核心同值）。列为观察 D5。
  - 终值复测（独立重跑构建 + 渲染墨迹双口径）：
    - P1-headline 1497（= 核心；重跑日志一致）；P7 col3 1668.0（= 信件框底 1313.5+354.5；距 FRASI 规则线 1686 **18.0px**，墨迹底 1666.3，距规则线 19.7px；核心 col3 1673.0，确认构建员“不同于核心的 1673.0”）；P8-keys 2514/2552（重跑日志一致；渲染墨迹底 2551.1，距流程底 2552 仅 0.9px、距页脚规则线 2580 为 28.9px——构建员“余 38px”为流程游标算术 2552−2514，非墨迹净空，见 D6）；P6-ex 2569/2580（重跑日志一致；渲染墨迹底 2545.3）。
    - P2/P3/P4/P5/P6 col3 终值重跑与核心逐项相同：996.0、1281.25、875.0、1285.75、1096.5。
  - **round 范围核查**（`baseline-round*-pre/final` 哈希比对）：round 3 改动 P1/P2/P7（含卡片与 PDF）；**round 4 仅改动 P1 SVG + P1 卡片 + 两 PDF**，与“仅数字框标题相关变化”一致，其余门禁不受影响； shipped 版 = round4-final 哈希（8 SVG 全对）。
  - **round 2 的 5 旗与 round 3 的 1 旗终版全消除**（逐项现值复测）：settimana 脚注 EDGE 2048.5 → 现 1796.2；P1 数字框标题 967.0 → 现墨迹右 912.0（距 961 框边 49.0px）；P2 frase 框标题 1005.5 → 现 945.2（距 961 框边 15.8px）；P7 gloss 底 1285.6 vs 旧框底 1284.5 → 现框底 1287.5（净空 1.9px）；round 3 残旗即数字框标题，已于 round 4 消除。终版双审计均为 0。
  - P4-main gloss 框：实测 rect **x=989..1423、y=200..345.68**（与构建员一致），3 行 gloss（y=238.5/268.225/297.95，墨迹底 ≤302.7）全在框内；与先行文本无重叠（独立 TEXTX 0 + 邻接检查）；卡片目视 col2 顶端框体干净、无压文。核心同框位于 col1（x=527, y=951），系标准 Flow `_fit` 跳框（荷兰语 gloss 3 行 vs 核心 2 行），无警告（round 4 日志与重跑日志均零警告），接受为正确行为而非缺陷。

## 5. gloss — 通过

- 构建代码 gloss() 串按 `·` 拆分（README #21 方法，核心与本版独立实测）：
  - 核心：P2 6（`il cappotto 大衣 · … · il crisantemo 菊花`）、P3 5、P4 4、P5 4、P6 5，合计 **24**。
  - 本版：P2 6（`il cappotto = jas · … · il crisantemo = chrysant`）、P3 5、P4 4、P5 4、P6 5，合计 **24**，逐项 1:1（词头相同，仅释义本地化）。
- 注：以渲染 SVG 正则截取 gloss 段的方法会在核心 P2 误读为 7（截取跑进后续文本多计一个 `·`），属测量方法伪影；代码级计数为准（D8）。

## 6. 读者园地 — 通过（按协调员裁定执行）

- 核心已有意大利语元素全部保留：信件逐字一致（核心与本版精确比对 identical: True：`«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li`）+ `(esempio della redazione)` 标签在版 + VOL.3 预告承诺（P7 末 band：`Lunedì 9 novembre: chiude il Festival dei Popoli a Firenze. La Festa del Torrone continua a Cremona fino al 22 novembre. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!`）。
- 披露句本身为荷兰语，逐字摘录核实（P7 信件框内 4 行，y=1585.15/1612.13/1639.11/1666.09）：
  - `Voorbeeld van de redactie, geen echte brief: nog geen echte brieven, geen beste opstel van pagina 8 — beide in VOL.3. Schrijf ons voor VOL.3!`
  - 3 事实：(1) 系编辑部示例、非真实来信；(2) 尚无真实来信；(3) 尚无第 8 版最佳作文；显性邀请祈使句：`Schrijf ons voor VOL.3!`；VOL.3 承诺：`beide in VOL.3`。
- **最佳 P8 作文覆盖范围裁定**：披露句明言“两者皆在 VOL.3”——即真实来信与第 8 版最佳作文两项均递延至 VOL.3；预告 band 的同类承诺（`le vostre lettere vere e i testi migliori della pagina 8`）与之口径一致，但预告行**不计入邀请**（邀请仅以披露句内祈使句为准）。零编造：未虚构真实来信、读者姓名或引言。
- IT 核心 P7 并无意大利语披露句可供保留（核心披露句为中文：`这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！`），故不以“无意大利语披露句”为由判 NOT PASS（与 IT×EN 同类项 B1 非阻塞裁定、IT×DE 同结构已上架一致）。

## 7. 计数口径 — 通过（独立展开到 150）

- 注册表（独立重跑）：150 题，A2 47 / B1 70 / B2 33，页分布 10/18/18/18/18/18/12/38。
- 印刷展开（核心与本版逐页相同）：
  - 单题号标（bare `N.` 节点）：**138** = 150 − 12（3 组配对题各 4 项未单编号）。
  - 级别 chip（练习 chip）：**141** = 138 单题 chip + 3 组头 chip；原始 chip 节点 145 = 141 + P1 sommario 目录行的 4 枚级别标（x=1863，`Pag. N` 行旁，非练习 chip）。
  - 3 组配对题成组印刷核实：P2 `25–28.` + `Koppel woord en betekenis`、P4 `52–55.` + `Koppel woord en betekenis`、P8 `141–144.` + `Koppel woord en betekenis`；P8 键行 154 条 = 150 键 + F 区练习行 141–144（与键行号重复，distinct 150）。
  - **非缺题**：138 + 12 = 150；P8 compare 150=150 与注册表三方一致。

## 8. 徽章槽位专项裁定 — 接受为家具

三方实测值（P1 masthead，y/x/字号/字重/锚点）：

| | 372 槽内容 | 字号/字重 | 574 处 | strapline |
|---|---|---|---|---|
| (a) W43 IT×NL 已上架版 | `TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`（y=372, x=975, middle） | 20pt / 700 | 无 | 无（该槽即徽章） |
| (b) W45 核心 P1 | `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`（y=372, x=975, middle） | 19pt / 常规 | 无 | 即该句 |
| (c) 本版 W45 IT×NL | 与 (a) **逐字节相同的徽章串**（y=372, x=975, middle） | 20pt / 700 | 无 | 无 |

- 副标题槽（y=330）三方：核心 46pt 中文间隔体、W43 46pt `ITALIAANS WEEKBLAD · VOL.1 · …`、本版 43pt `ITALIAANS WEEKBLAD · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A`（43pt 原因见 §9）。
- 净空：徽章墨迹 (451.5, 357.0, 1498.5, 372.2)，距下方规则线顶边 390.5 为 **18.2px**，居中无溢出；卡片目视砖红徽章清晰可辨。
- W45 同族兄弟（IT×EN/DE/FR/PT）实测均为另一几何：372 槽保留 strapline（19pt）+ 徽章**插入** y=574、22pt/700（EN：`Text in Italian · Explanations in English …`；DE/FR/PT 同式）。即 README #20 所述 FR/IT 族“574/22pt 插入”确为 W45 兄弟的通行做法，但**本配对的已上架先例（W43 IT×NL）是 372 替换**。
- **裁定**：按任务裁定标准，W43 同配对已上架版胜过 README #20 泛化规则；本版与 W43 同配对在徽章串/槽位/字号上逐字节一致，**接受为家具**，不构成对“核心 372 冻结”的违反（372 槽在本配对历史上即为可替换的徽章槽；W43 与本版均以此处理，且副标题、刊头、页脚等其余冻结元素均未移动）。配对标识在 P1 masthead 上清晰可辨（徽章 + 副标题 + 页脚三处）。
- 附带说明：strapline 的缺失是该家具方案的固有代价，W43 同配对亦然；不另作缺陷。

## 9. 家具（与 W43 同配对实测对照） — 通过

- KIT §3 家具与 W43 逐项核对：徽章串/位置/字号、页脚、顶 strip、全部版带标题/副标题、gloss 前缀 `Uitleg — `、P8 分隔符、印刷指令词、注册表类型名、P8 E 区规则、dash 体、tsize=20 框标题（P1 数字框、P2 frase 框）均与 W43 一致（W43 KIT 与 SVG 实测）。
- P1 副标题 43pt vs W43 46pt（三档精确字号实测，Noto Serif SC Bold，居中 x=975）：
  - 46pt：advance 1907.6，边 21.2..1928.8（出页框 1910）——不可用；
  - 44pt：advance 1824.6，边 62.7..1887.3（出 1885 内容边 2.3px）——不可用；
  - **43pt：advance 1783.2，边 83.4..1866.6，入框**——采用，全文保留。W43 副标题 46pt 实测 advance 1790.2、边 79.9..1870.1，确可容纳（文本较短）。与构建员三档值一致（44pt 0.1px 舍入差除外）。
- P1 settimana 脚注缩短：W43 P1 无等价脚注（其 col3 脚注为 Google Trends 说明行，与 settimana 无关）；核心中文脚注（右缘 1770.0）→ round-2 荷兰语长句 575.6px（右缘 2048.5，出框）→ 现 `Data per kalender; tijden kunnen wijzigen.`（323.2px，右缘 **1796.2**，在 settimana 框 1451..1885 内）。两项免责事实保留：`Data per kalender`（日期以日历为准）+ `tijden kunnen wijzigen`（时间可能有变）。
- P1 桥句与 cifre 第 4 项括号：桥句 3 行（见 §1）、cifre 第 4 项 2 行（`11ª — la giornata di Serie A del fine` / `settimana(speelronde 11 dit weekend)`），均为恢复核心行数的缩短选词（`prognose`/`proeven`），无内容丢失。
- P8 注释修剪 #41/#50/#138：现均为单节点单行（#41 `41. abbiamo assaggiato — assaggiare gebruikt avere`；#50 `50. C — Europese wedstrijden: alleen voorbeschouwing`；#138 见 §3），key 完整。
- 级别 47/70/33 vs W43 46/71/33、范文 81 词 vs W43 90 词：均为核心驱动（W43 KIT：`150 exercises — A2 46 · B1 71 · B2 33`、`Writing model (#150): 90 words`；W45 核心注册表与范文实测见 §7/§12），非本版偏差。
- 其余紧缩：diff 全量显示均为荷兰语长度所迫的纯措辞调整（同义缩短），无内容丢失；未见 W43 家具串被无故改动。

## 10. 图片 — 通过

- raster 图片载荷（base64 payload sha256，逐页）：
  - P3 tartufo：核心与本版 `9ea4244b4d216b67…`（346,864 字符），位置 1451,200,434×265 一致；署名在版：`Foto: Wikimedia Commons — dominio pubblico`。
  - P5 castagne：核心与本版 `d6bc00b109d273c4…`（627,056 字符），位置 1451,200,434×300 一致；署名在版：`Foto: Wikimedia Commons — CC0`。
  - 其余 6 页核心与本版均无 raster `<image>`（图表/线描为矢量），载荷对照无遗漏。

## 11. ABSTRACT — 通过

- 全文（单行，无 ASCII 双引号）：
  - `La Lucerna, Italiaans weekblad voor Nederlandstaligen: de eerste kou, 2 november, de Panettone World Cup-finale in Milaan op 7-8 november, Festa del Torrone in Cremona, Serie A speelronde 11 en Forum Cultura — 150 oefeningen op A2-B2-niveau met Nederlandse uitleg; zoek: Italiaans leren met nieuws uit Italië.`
- 核查：单行 ✓；ASCII `"` 0 ✓；含刊名 La Lucerna、目标语名 Italiaans、A2-B2、150 题 ✓；真实主题关键词：Panettone、Torrone、Serie A、Forum Cultura、eerste kou、2 november ✓；学习者搜索短语：`Italiaans leren met nieuws uit Italië` ✓。

## 12. 卡片与终验 — 通过

- 8 张卡片全部逐页目视（1950×2700 RGB）：
  - P1：徽章/副标题/桥句/数字框/脚注/quiz 均干净，无溢出；P2：frase 框标题入框、配对组 25–28 完整；P3：松露照片 + 署名、gloss 框；P4：赛程表完整、col2 顶端 gloss 跳框无重叠（框体与邻文间距正常）；P5：栗子照片 + CC0 署名、周计划框；P6：图表 5 城条形与温度标全可见、无截断，`(DATI INVENTATI PER L'ESERCIZIO)` 标注在版，练习末行距页脚充足；P7：三栏 + 诊所 + parola 框 + 信件框（披露句 4 行在框内、距 FRASI 规则线 18px）+ FRASI 8 句 + 预告 band；P8：练习 113–150、E 区题干方向、F 组 141–144、H 范文、150 条键行收束于页脚之上。**无目视缺陷。**
- 题量与级别分布独立展开计数 = 150（见 §7）；范文 81 词与核心逐字一致（H 节范文体精确提取，两版 body 完全相同，见 `followup3.txt`）。
- 校对前后交付与核心哈希不变（见 §0）。
- 未清理共享 scratch 目录；校对中间产物仅存于本目录（含 `ed-copy`/`freeze-out` 两个重定向构建副本，其 transform.py 残留真实路径引用但从未被执行，执行文件均已重定向至校对目录内）。

## 非阻塞差异与观察（不构成 NOT PASS）

- **D1（右缘方法）**：构建员右缘脚本对非整数 pt 取整，高估 advance（P8 H 标题高估 14.0px、P1 行高估 9.8px）。精确重测后 margin 集由 5 条缩为 2 条（新增荷兰语行 + 继承行），0 越框结论不变且更强。建议后续轮次右缘脚本改用精确字号。
- **D2（#139 来源标注）**：key 与核心 P8 E 区题干逐字节一致，非 P4 文本节点（见 §3）。报纸本身无误，仅说法需修正。
- **D3（KIT CJK）**：KIT 含 1 个全角 `：`（元语言引用），构建员“KIT CJK 为 0”不精确；ABSTRACT 与报纸文本仍为 0。
- **D4（P7 gloss 净空偏紧）**：1.9px（绘制边）/ 2.6px（扩张框）。通过门限且目视干净，但后续若 gloss 加长将首先触线。
- **D5（P8 H 标题贴边）**：精确 advance 1884.6，距 1885 仅 0.4px。冻结文本、核心同值，无动作。
- **D6（P8-keys“余量”口径）**：构建员“38px”系流程游标算术；渲染墨迹底 2551.1，距流程底 0.9px、距页脚规则线 28.9px。均在限内，无缺陷。
- **D7（P7 col3 口径）**：构建员 1668 为信件框底（= col3 终值），墨迹底 1666.3；核心 1673.0。两种口径下本版距 FRASI 规则线分别为 18.0px / 19.7px，均合格。
- **D8（SVG gloss 截取伪影）**：正则截取法误读核心 P2 为 7 项；代码级计数（24=24）为准。
- **D9（p8.py 调用口径）**：`--target nl` 会按 NL 目标查 `p8-toets.svg` 而失败；本版正确调用为显式 `--core-p8/--edition-p8` 路径，结果 CLEAN。
- **D10（round-3 右缘文件）**：构建目录 `rightedge-ed3.txt` 为一次错误路径调用的报错输出，非门禁结论；round-4 文件有效，本校对已用新鲜重跑覆盖。

## 证据文件（本目录）

- [REPORT.md](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/REPORT.md)（本报告）
- [freeze-baseline.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/freeze-baseline.txt)（freeze 8/8）、[freeze-diff.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/freeze-diff.txt) / [freeze-diff.json](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/freeze-diff.json) / [freeze-diff-full.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/freeze-diff-full.txt)（全量增减串，无截断）
- [p8-compare.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/p8-compare.txt)（CLEAN 150=150）、[reg-diff.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/reg-diff.txt)（注册表 key/注释/类型/页/级别差异）、[reg-ed.json](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/reg-ed.json) / [reg-core.json](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/reg-core.json)（独立注册表转储）、[reg-ed-log.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/reg-ed-log.txt) / [reg-core-log.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/reg-core-log.txt)（独立重跑流程终值）
- [occ-ed.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/occ-ed.txt) / [occ-core.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/occ-core.txt) / [occ-new.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/occ-new.txt) / [occ-selftest.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/occ-selftest.txt)（共享几何审计 0/0/0）
- [audit-full.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/audit-full.txt)（独立审计全量：masthead/右缘/同基线/独立几何/图表/P7 词框/金句/gloss/P8/禁词-CJK/图片/ABSTRACT/流程墨迹/P4 gloss/副标题-脚注/W43/计数/范文/轮次/行数/删串存活/内边距）
- [followup-full.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/followup-full.txt)（右缘五线双方法 + 徽章净空 + 金句 + 定义句 + 信件逐字 + 练习标）、[followup2.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/followup2.txt)（P1 chip 构成、P8 重复号、组头、范文定位）、[followup3.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/followup3.txt)（P1/P8 精确右缘 + 范文 81 词逐字比对）
- [rightedge-builder-rerun-ed.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/rightedge-builder-rerun-ed.txt) / [rightedge-builder-rerun-core.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/rightedge-builder-rerun-core.txt)（构建员右缘脚本新鲜重跑）
- [hash-before.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/hash-before.txt) / [hash-after.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/hash-after.txt)（校对前后哈希，diff 为空）
- [proof_audit.py](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/proof_audit.py) / [proof_followup.py](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/proof_followup.py) / [reg_driver.py](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/reg_driver.py)（独立测量脚本）
- [letterbox.txt](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof/letterbox.txt)（信件框底 1668.0，距 FRASI 规则线 18.0px）

**最终结论：ZERO PROBLEMS。** 本版可进入下一环节（按既有流程由主线处理入仓/分发；本校对不宣布上架、不做投递）。
