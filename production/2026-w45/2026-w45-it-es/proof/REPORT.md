# 独立校对报告 — Lucerna Weekly W45 IT×ES（VOL.2）

- **校对对象**：`files/weekly-report-w45-it-es/`（svg×8、cards×8、print PDF、web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **对照核心**：`files/weekly-report-w45-it-core/`（只读；校对前后哈希不变，见 §11）
- **对照已上架同配对**：`files/weekly-report-it-es/`（W43 IT×ES，只读）
- **校对方式**：从头独立重测，不采信构建员自述；工具用 `tools/` 共享工具（freeze.py / p8.py / occlusion_audit.py）+ 自写几何脚本 `geom.py`（同目录）
- **开工查重**：开工时无进行中渲染进程；交付与构建树 mtime 在 75 秒复查内零新写盘，安全开工（最后写盘 23:29，复查至 23:34 无变化）
- **结论：ZERO PROBLEMS** — 11 门禁全部通过，无编号阻塞项。§7 徽章槽位专项裁定：接受为家具（见 §7），不构成阻塞。
- **未做事项**：未改源码、未宣布上架、未派生下级代理、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理共享 scratch 目录。

## 1. 冻结门

- `freeze.py baseline`（核心构建 `hidden_files/weekly-report-w45-it-build`）：**8/8 逐字节复现**，核心哈希与交付核心一致（p1 81051bbb…、p2 d42ce9ae…、p3 9e45586d…、p4 62f75269…、p5 c907b869…、p6 5545f8dd…、p7 9fc999f4…、p8 3b87e54f…），运行后核心重哈希不变。
- `freeze.py diff`（核心 vs 本版，逐页 added/removed 字符串计数和）：p1 +27/−27、p2 +34/−29、p3 +32/−31、p4 +28/−25、p5 +42/−35、p6 +28/−24、p7 +43/−41、p8 +168/−166——与 KIT §2 逐页一致。
- **新增 CJK = 0**（每页 edition CJK 均为 0；核心 193/179/169/145/215/149/319/1034）；直接清点本版 8 页文本节点 CJK 字符总数 = 0。
- **桥接**：8 页 SVG 中 `桥接` = 0；ABSTRACT = 0（KIT 文件本身有 1 处，见非阻塞观察 O1）。
- **意大利语正文冻结**：除下述逐项裁定的删除串外，所有非 CJK 删除串已穷尽——即全部删除串 = 中文讲解层 + 下列 10 项，无意大利语正文丢失：
  - P1 ×1：报头 strapline `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`（专项裁定见 §7）。
  - P6 ×1 换行碎片 `bollettino · modello`：两词均在本版出现（gloss 行 `probabilità · media · bollettino · modello` 及正文），仅换行不同。
  - P7 ×1 换行碎片 `è probabile che / è possibile che / bisogna`：本版有 `Tras è probabile che / è possibile che /` 续行 + `bisogna che va subjuntivo…`，内容齐全，仅换行不同。
  - P8 ×7 仅标点形式差异（全角 `：`→半角 `:`、全角 `（）`→半角 `()`），内容逐字一致：
    - 17. `metto — mettere：io → metto` → `metto — mettere: io → metto`
    - 18. `portano — portare：loro → portano` → `portano — portare: loro → portano`
    - 19. `guardano — guardare：loro → guardano` → `guardano — guardare: loro → guardano`
    - 20. `resta — restare：la scuola → resta（lei）` → `resta — restare: la scuola → resta (lei)`
    - 60. `ha vinto — vincere：ha vinto` → `ha vinto — vincere: ha vinto`
    - 61. `ha pareggiato — pareggiare：ha pareggiato` → `ha pareggiato — pareggiare: ha pareggiato`
    - 103. `nevica — nevicare：nevica` → `nevica — nevicare: nevica`
  - 讲解层全部西班牙语（CJK 0 为证）；P8 注释纯西班牙语（见 §3）。

## 2. P7 词框硬性门

- 意大利语定义句空白归一化后与核心**逐字一致**：
  `« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone.`
- 仅 gloss 本地化为西班牙语（2 行，与核心行数一致）：
  `assaggio = degustación. Página 3: en la final del Panettone se prueba gratis.`
- 无定义句本地化。P7 其余意大利语诊所句、纠错句、金句节点与核心逐节点一致（见下）。
- **P7 金句 8 句各 2×**（去 « » 后全文计数，核心与本版均为 2×；P7 金句节点与核心逐字节一致）：
  1. `arriva il primo freddo vero della stagione` — 标签 (Pagina 1)
  2. `Non è una certezza, è una probabilità` — (Pagina 1)
  3. `il 2 novembre è la Commemorazione dei defunti` — (Pagina 2)
  4. `Fa freddo, copriti bene!` — (Pagina 2)
  5. `il pubblico può assaggiare gratis` — (Pagina 3)
  6. `il calcio non si ferma per il primo freddo` — (Pagina 4)
  7. `la cultura continua` — (Pagina 5)
  8. `Una probabilità alta non è una certezza` — (Pagina 6)
- 标签序列从核心独立实测 = **(1, 1, 2, 2, 3, 4, 5, 6)**，与构建员自述一致；西班牙语译文逐句对应。

## 3. P8 门

- `p8.py compare`（核心/版本 P8 显式路径，total 150）：**CLEAN，150 noted = 150 noted，missing=[] extra=[] uncertain=[]，keydiff=[6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 102, 137, 138, 139]**。
- 逐项印刷行对照（答案区实测行；extracted key 差异机制说明如下）：
  - **前 12 项为注释翻译 + 括号/标点形式伪影，印刷答案头逐字一致，不是键变更**。机制（已用 `tools/p8.py` 的 `detect_note` 源码核实）：核心注文为中文（全角括号）或无括号时，工具取 dash 分支/键头；本版注文为西班牙语（半角括号）时，工具取 paren 分支，返回括号前全文——故 extracted key 表面不同，但印刷答案头相同：
    - 6. 头 `previsioni`：核心 `6. previsioni — previsioni = 预报（复数）` / 本版 `6. previsioni — previsioni = previsiones (plural)`
    - 13. 头 `guanti`：`guanti = 手套（复数）` / `guanti = guantes (plural)`
    - 14. 头 `crisantemi`：`crisantemi = 菊花（复数）` / `crisantemi = crisantemos (plural)`
    - 15. 头 `termosifoni`：`termosifoni = 暖气片（复数）` / `termosifoni = radiadores (plural)`
    - 16. 头 `fa`：`fa — fare freddo：fa freddo（天气）` / `fa — fare freddo: fa freddo (tiempo)`
    - 20. 头 `resta`：`resta — restare：la scuola → resta（lei）` / `resta — restare: la scuola → resta (lei)`
    - 38. 头 `mandorle`：`mandorle = 杏仁（复数）` / `mandorle = almendras (plural)`
    - 58. 头 `più bella`：`più bella — più + bella 周日晚最美（主观评价）` / `più bella — più + bella: la más bella (opinión)`（注：本版注文冒号为西班牙语注文格式一部分，仍属注文层）
    - 71. 头 `gratuiti`：`gratuiti = 免费的（阳性复数）` / `gratuiti = gratuitos (masculino, plural)`
    - 74. 头 `castagne`：`castagne — castagne arrosto 烤栗子（复数）` / `castagne — castagne arrosto = castañas asadas (plural)`
    - 77. 头 `ci sarà`：`ci sarà — esserci 将来时：ci sarà（将有）` / `ci sarà — esserci, futuro: ci sarà (habrá)`
    - 102. 头 `fa`：核心 `102. fa — fa freddo = 天气冷`（无括号，dash 分支抽出 `fa`）/ 本版 `102. fa — fa freddo = hace frío (tiempo)`（尾部 `(tiempo)` 括号使工具取 paren 分支，抽出 `fa — fa freddo = hace frío`）——**#102 确为括号分支伪影**，构建员的机制标签经源码核实成立；此前同族集合中没有 #102 一项，本次未因先例跳过，已逐行实测。
  - **后 3 项为真重定向（合法，W43 同配对先例）**：section E 翻译题意向由中文改为西班牙语，意大利语题干不变：
    - 137. 核心键 `周一第一场寒冷来了。` / 本版键 `El lunes llega el primer frío.`（题干 `Lunedì arriva il primo freddo. → ___` 不变）
    - 138. 核心键 `观众可以免费品尝。` / 本版键 `El público puede probar gratis.`（题干 `Il pubblico può assaggiare gratis. → ___` 不变）
    - 139. 核心键 `周日晚上，佛罗伦萨对尤文图斯。` / 本版键 `El domingo por la noche se juega Fiorentina–Juventus.`（题干 `Domenica sera si gioca Fiorentina–Juventus. → ___` 不变；答案注文换行 `— si` + `gioca = se juega`，空隔连接后读作 `si gioca = se juega`，与构建员所述一致）
    - 140. 键冻结为意大利语原文，两版均为 `Ogni previsione deve essere chiara.`；题干体由核心中文 `每个预报都必须清楚。→ ___` 改为西班牙语 `Cada previsión debe ser clara. → ___`（与 137–139 同向重定向的另一面：母语→意大利语方向，键保持意大利语）。
  - 150. 写作题印刷为 `150. ✓ El modelo está en la sección H (81 palabras)`；工具 keydiff 不列写作题（与构建员所述一致）。
- P8 注释纯西班牙语（P8 文本节点 CJK = 0；注文中的意大利语词均为题面 headword 引用，属既定 dash 式注文格式）。

## 4. 几何门

- `occlusion_audit.py`（自检先行：6 类 planted 全部触发，clean 对照静默）：**分版 0 flags / 核心 0 flags / NEW 0 flags，exit 0**。
- 自写几何脚本 `geom.py`（ADVANCE 右缘法；同基线碰撞；PIL getmetrics + anchor `ls` 基线锚定墨迹法）：
  - 右缘扫描（frame 带 [40, 1910]，外框 28）：**0 flags，全部 8 页**。
  - 同基线碰撞（P1 顶栏 y=92、全部页脚 y=2624、P1 波段 y=478/522）：**0 overlaps**；P1 顶栏实测间隙 198.6px / 91.5px（左止 392.3 → 中起 590.9 → 中止 1359.1 → 日期起 1450.6），与构建员所述一致。
  - P6 图表标签覆盖（Torino/Milano/Bologna/Roma/Napoli + 3°/4°/5°/9°/12°，后绘橄榄绿条 vs 标签墨迹）：**max 0.0%**（门限 <30%）。
  - 全 8 页框线压框：occlusion 审计 BOXTITLE/EDGE 0 + 右缘 0 + 8 张卡片目视（§11）无压框；P7 词框末行墨迹在框内（卡片目视 + 审计 0）。
  - P7 栏 3 与 FRASI 横线：横线实测 **y=1686.0**（全幅线 x 65..1885）；栏 3 流终值 1679.0（构建日志）→ 距横线 7px（流终口径）；自测墨迹底 1680.0（读者园地末行 `mejores salen en VOL.3.`，基线 1673.95 + desc）→ 距横线 **6px**（墨迹口径）。1px 为口径差，非缺陷；横线未被任何墨迹穿过（审计 LINEX 0）。
  - P8 答案底：流终值 2499（构建日志，bottom 2552）；自测末行答案墨迹底 2540.40（第 37 行，基线 2536.40）；页脚线实测 y=2580.0。见非阻塞观察 O2（KIT 的 53px 清量口径不复现，但任何口径下均无溢出）。
- 修复范围复测：
  - **R1→R2 哈希差分**（sha256-r1.txt vs sha256-r2.txt）：仅 4 项变化——p1 SVG、p1 卡片、web PDF、print PDF；其余 14 项（p2–p8 SVG/卡片）逐字节不变。与构建员所述一致。
  - **R0→R1 修复终版消除验证**：终版构建日志 FLOW OVERFLOW 0、HEAD TOO WIDE 0；P1 头条流终值 1497（bottom 1828），卡片目视头条 + 练习 5–6 位置正常，无钳制；P8 键流终值 2499；P2 盒标题实测 `FRASE PER RICORDARE · LA CLAVE`（去首 LA），卡片目视在框内；P7 词框末行墨迹在框内（审计 BOXTITLE 0 + 卡片目视）；R1 唯一 NEW 标记（LINEX：P1 parola 灰注第二行 `otoño suave.` 被 1864 行线划过）终版已消除——本版 P1 已无 `otoño suave`/`otoño` 文本，parola 注文为单行节点 `«il primo freddo»: el primer frío serio.`（19pt 实测 326.7px 口径节点存在，单行）。

## 5. gloss 门

- 核心 gloss() 源串按 `·` 裸分隔符拆分（从核心构建 content12/34/56.py 独立实测，**非照搬他族**）：
  - P2：6 — il cappotto · la sciarpa · i guanti · a strati · il termosifone · il crisantemo
  - P3：5 — il panettone · il torrone · l'assaggio · la bancarella · il cantiere
  - P4：4 — la giornata · la presentazione · gli spalti · la sera
  - P5：4 — il cosplay · gratuito · il documentario · lo schermo
  - P6：5 — la probabilità · la media · il modello · il bollettino · aggiornare
  - **合计 24**，与构建员所述分布一致。
- 渲染后核验：24 个 headword 全部在本版渲染文本中出现；渲染 gloss 行（`Nota — ` 起）按 `·` 拆分逐页计数 = 6/5/4/4/5，**与核心 1:1**。
- P1 桥接词表：核心源串拆分 4 项（il primo freddo · il versante adriatico · la previsione · assaggi）；本版渲染 `Nota — il primo freddo = el primer frío · versante adriatico = Adriático · previsione = previsión · assaggi = degustaciones.`，**4 项 1:1**（versante/previsione 前冠词省略为已披露的紧缩，词头可辨，无内容丢失）。

## 6. 读者园地（按协调员裁定执行）

- 保留核心已有的意大利语元素（逐字核实）：
  - 信件逐字：`«Ciao! Sono Li, studio italiano a Pechino. Lunedì metto il cappotto e la sciarpa, sabato assaggio il panettone — almeno in foto!» — Li`（分行节点与核心逐字一致）
  - 标签：`(esempio della redazione)`（保留）
  - 预告承诺：下期预告带意大利语原文 `le vostre lettere vere e i testi migliori della pagina 8`（保留，**不计入邀请**）
- 西班牙语披露句逐字摘录（P7 LETTERE 框内，3 行，与核心中文注文行数一致）：
  `Ejemplo de la redacción, no carta real; sin mejor texto de página 8. ¡Escríbenos! Las mejores salen en VOL.3.`
- 3 事实映射：① 无真实来信 — `no carta real`（+ 信件自带 `(esempio della redazione)` / `Ejemplo de la redacción`）；② 无最佳 P8 作文 — `sin mejor texto de página 8`；③ 示例 + 顺延 VOL.3 — `Ejemplo de la redacción` + `Las mejores salen en VOL.3`。
- 显性西班牙语邀请（框内，非预告行）逐字摘录：`¡Escríbenos! Las mejores salen en VOL.3.`——祈使句 + VOL.3 刊登承诺，成立。
- **最佳 P8 作文覆盖范围裁定**：邀请中的 `Las mejores` 在上下文中（紧接 `sin mejor texto de página 8` 的披露句内）指代读者投稿中的最佳作品（含最佳 P8 作文），与预告带意大利语原文 `i testi migliori della pagina 8` 的承诺范围一致；披露句已明言本期无最佳 P8 作文，邀请仅为面向 VOL.3 的征集承诺，不构成对本期已刊登最佳作文的虚构。参照 PT/IT 族同类范围裁定先例的处理方式（披露与邀请分离、预告行不计入邀请），本项通过。
- IT 核心 P7 并无意大利语披露句可供保留（核心披露句为中文注文，仅有 `(esempio della redazione)` 标签为意大利语）：按任务书明示，**不以“无意大利语披露句”为由判 NOT PASS**（IT×EN 同类项 B1 已裁定为非阻塞，IT×DE 同结构已上架）。
- 零编造：无虚构读者、来信、姓名或引言。

## 7. 徽章槽位专项裁定（本版唯一开放点）——裁定：接受为家具，不阻塞

裁定标准（任务书）：家具规则为 W43 同配对已上架版胜过 README #20 泛化规则；若本版与 W43 同配对逐字节一致，接受；若有差异，或替换行为删除了 W45 核心冻结正文而 W43 并无此行为，则阻塞。

三方实测：

- (a) **W43 IT×ES 已上架版 P1**：徽章节点 `(x=975, y=372, font-size=20, font-weight=700, fill=#a4553a, text-anchor=middle)`，串为 `TEXTOS EN ITALIANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`；**strapline 在全版中不存在**——确为替换行为（非插入）。实测 advance 1077.3px（与 W43 KIT 的 1077px 一致）。
- (b) **W45 核心 P1 的 372 槽内容**：`(x=975, y=372, font-size=19, fill=#57523f, middle)`，串为 `IL GIORNALE SETTIMANALE PER IMPARARE — L'ITALIA VERA, IN ITALIANO, DALL'ITALIA`——即冻结差分中唯一的 P1 非 CJK 删除串。372 槽在核心确为意大利语标语（非空闲槽位）。
- (c) **本版 P1**：徽章节点与 W43 已上架版**全部属性 + 字符串逐字节一致**（975/372/20pt/700/#a4553a/middle + 同串）；strapline 在全版中不存在——与 W43 已上架版的处理**逐字节一致**。

裁定：本版遵循 W43 同配对已上架实例（372/20pt 替换），与同族 IT×DE/EN/FR 的 574/22pt 插入不同，但按任务书裁定标准，**同配对先例胜出**；替换行为删除的 W45 核心冻结正文（strapline）与 W43 的替换行为性质相同（W43 已上架版同样无 strapline），不构成“W43 并无此行为”的情形。**故不以与 DE/EN/FR 不同为由判阻塞**。配对标识在 P1 masthead 上清晰可辨：徽章串本身（砖红 20pt 粗体，居中于版头线下方）+ 顶栏 `OGNI SETTIMANA IN ITALIANO · CADA SEMANA · EL ITALIANO QUE LEE ITALIA` + 页脚配对串，卡片目视清晰。

范围说明：工作区内无 W43 意大利语核心 SVG 文件，故 W43 核心 strapline 与 W45 核心 strapline 的逐字同一性无法从 W43 核心文件直接复验；但裁定不依赖该点——W43 已上架版自身的替换行为（徽章占 372 槽、strapline 缺席）已直接实测，且本版与之逐字节一致。

## 8. 家具（与 W43 同配对实测对照）

- 徽章串、槽位、字号：见 §7，与 W43 一致（VOL 1→2 除外）。
- 页脚模板：8 页均为 `La Lucerna · SEMANARIO ITALIANO VOL.2 · TEXTO EN ITALIANO · EXPLICACIONES EN ESPAÑOL` + `Página N de 8`；与 W43 模板逐字一致，仅 VOL.1→VOL.2（跟随 W45 核心）。页脚 advance 间隙 792.1px（左止 970.5 → 右起 1762.7，全部 8 页）。
- 页码行：`Página N de 8`，与 W43 一致。
- gloss 前缀：`Nota — `，与 W43 一致（P2–P6 实测）。
- P8 分隔符：`— PAGINA N —`（N=1..8），与 W43 一致；未用 tables.json 通用 ES 形 `— PÁGINA N —`。
- 破折号答式：`N. key — note`，与核心一致（IT 为 dash 式族）；P8 注文括号为半角 `()`（W43 IT×ES 形），核心全角 `（）`仅见于中文注文（已全部替换）。
- 指令词表：Completa / Empareja / Forma la frase / Traduce / Verdadero o falso / Escribe 全部出现，与 W43 词表成员一致（Completa 出现次数本版 65 vs W43 63，为 W45 核心题量驱动，非家具差异）。
- P1 顶栏：`OGNI SETTIMANA IN ITALIANO · CADA SEMANA · EL ITALIANO QUE LEE ITALIA`（21pt 居中）+ 左 `VOL. 2 · SECONDA EDIZIONE` + 右 `SETTIMANA DAL 2 ALL'8 NOVEMBRE 2026`，与 W43 顶栏逐字一致（VOL 与日期跟随本期核心）。
- P1 暗带右文：`ESTA SEMANA LLEGA EL PRIMER FRÍO` / `La semana del primer frío · ver página 2`，实测存在。
- 报头：核心的 **La Lucerna**（意大利语冠词），与 W43 一致。
- 版面行紧缩：实测 edition 行（y=330，46pt serif 粗体）`SEMANARIO ITALIANO · VOL.2 · IL PRIMO FREDDO · PANETTONE · SERIE A` = 1763.8px；全式 `… · IL PANETTONE · LA SERIE A` = 1899.8px（超 1845px 框带，确会压框）。去 `IL PANETTONE` 前的 IL 与 `LA SERIE A` 前的 LA 为纯措辞紧缩，主题词齐全，无内容丢失。
- 其余紧缩（均为西班牙语长度所迫的纯措辞调整，无内容丢失，已逐项核实）：P1 桥接冠词省略（§5）、P1 cifre 第 4 项括号缩短（`settimana(11.ª jornada)`）、P1 parola 灰注单行化（§4）、P2 盒标题去首 `LA`（`FRASE PER RICORDARE · LA CLAVE`，卡片目视在框内）、P7 词框底 pad +6（审计 0）、8 条 P8 注文缩为单行（键 44/45/56/58/133/134/135/138 终版均为单节点，139 故意保留 2 行）。
- 核心驱动差异（非偏差）：级别 A2 47/B1 70/B2 33（W43：46/71/33）；范文 81 词（W43：90 词）——均跟随 W45 核心（§11 独立计数复现）。

## 9. 图片

- 各页图片嵌入载荷（base64 长度 + SHA 前缀）核心 vs 本版逐页一致：P1 0、P2 0、**P3 1（tartufo，1451/200/434×265）**、P4 0、**P5 1（castagne，1451/200/434×300）**、P6 0、P7 0、P8 0。
- 署名在版且与核心逐字一致（意大利语）：P3 `Foto: Wikimedia Commons — dominio pubblico`；P5 `Foto: Wikimedia Commons — CC0`；卡片目视两图均清晰呈现、署名可见。

## 10. ABSTRACT

- `ABSTRACT.txt`：西班牙语单行（wc -l = 1）、无 ASCII 双引号（grep `"` = 0）。
- 全文：`La Lucerna VOL.2, 2–8 de noviembre de 2026: el primer frío en Italia, el Día de Difuntos el 2 de noviembre, la Copa del Mundo del Panettone en Milán el 7–8 de noviembre, la Festa del Torrone en Cremona y la Serie A en la 11.ª jornada – aprende italiano leyendo, con explicaciones en español, niveles A2–B2, 150 ejercicios con soluciones.`
- 含真实主题关键词（primer frío、Día de Difuntos 2 de noviembre、Copa del Mundo del Panettone Milán 7–8 de noviembre、Festa del Torrone Cremona、Serie A 11.ª jornada）+ 学习者搜索短语（`aprende italiano leyendo, con explicaciones en español`）+ 刊名、目标语名、A2–B2、150 题。事实均取自本期内容。

## 11. 卡片目视 + 独立计数 + 哈希不变

- **8 张卡片全部逐页目视**（p1-prima、p2-vita、p3-cultura、p4-sport、p5-giovani、p6-approfondimento、p7-lingua、p8-valutazione）：
  - P1：徽章清晰、头条/热搜/目录/快讯/quiz 行无溢出重叠，页脚清晰。
  - P2：gloss 框、FRASE 框标题在框内，练习区完整，页脚清晰。
  - P3：tartufo 照片 + 署名清晰，gloss 框完整，练习区完整。
  - P4：赛程表行列清晰，无重叠，练习区完整。
  - P5：castagne 照片 + CC0 署名清晰，练习区完整。
  - P6：图表 5 城标签 + 数值全部清晰、未被条形遮盖，图表说明（练习数据）可见，练习区完整。
  - P7：三级专栏、诊所、词框（定义句 + 西班牙语 gloss 在框内）、读者园地（信件 + 标签 + 3 行西班牙语注文）、FRASI 8 金句 + 译文、预告带均清晰；读者园地末行与 FRASI 横线间有可见空隙；页脚清晰。
  - P8：练习 A–H 区 + 全部答案（PAGINA 1–8 分隔）完整，末行 150 远离页脚，页脚清晰。
  - 目视缺陷：**0**。
- **题量与级别分布（从渲染 SVG 独立展开计数，非登记表）**：按“级别芯片节点 + `N.`/`N–M.` 节点”展开（P8 仅取 1382 上方练习区）：**150 题，集合恰为 1–150，无缺重**；级别 **A2 47 / B1 70 / B2 33**；页分布 **10/18/18/18/18/18/12/38**——与核心及 KIT §1 一致。
- **范文**：从两版 P8 练习区提取 `Testo modello:` 段，空白归一化后**逐字节一致，81 词**，与核心一致。
- **校对前后交付与核心哈希不变**：pre-hashes 与 post-hashes diff 为空；交付 SVG/卡片/PDF 哈希与 KIT §12 逐项一致（print PDF 7,170,661 B sha256 `66be437a…7179e9e`；web PDF 3,614,384 B sha256 `a1e2a8a9…495e53`）；print PDF 8 页、mediabox 0/0/1462.5/2025 与核心 print PDF 一致；web PDF 8 页（<10 MB）。
- 共享 scratch 目录未清理；核心/W43 目录未改动（仅只读对照）。

## 非阻塞观察（与构建员自述不符处，即使非阻塞亦列出）

- **O1 — KIT 的“桥接 0 命中”表述在字面上不成立**：KIT §1 句 `The banned intermediary-layer term appears nowhere: 桥接 = 0 hits in all 8 SVGs, this KIT, and the delivered ABSTRACT.` 本身含 1 次 `桥接`（第 29 行），故“this KIT 0 命中”按字面为假。实质无影响：8 页 SVG 0 命中、ABSTRACT 0 命中，讲解层确无桥接层；仅为 KIT 自述句的自指瑕疵。
- **O2 — KIT 的 P8“53px 清量”口径不复现**：流终值 2499 / 流 bottom 2552 经构建日志核实；但 2552 距页脚线 2580 为 28px、距页脚墨迹顶 2600 为 48px、距页脚基线 2624 为 72px；自测末行答案墨迹底 2540.4 距页脚线为 39.6px、距页脚墨迹顶为 59.6px——**无一口径得 53px**（53 恰等于 2552−2499 的行框高，疑为口径混淆）。任何口径下均无溢出，审计 FOOTER 0，故非阻塞；建议 KIT 修正该数字的口径说明。
- **O3 — P7 栏 3 清量口径差 1px**：流终口径 1679.0→7px、墨迹口径 1680.0→6px（§4）；横线未被穿过，非阻塞。
- **O4 — P7 LETTERE 框整体下移 6px**：读者园地各节点 y 较核心统一 +6（框题 1381.5→1387.5、信件各行同幅），文本逐字一致；与 P7 词框底 pad +6 推动下游内容的布局后果一致，几何审计 0、卡片目视正常，非阻塞。
- **O5 — P8 注文中的意大利语词头**：如 #24 `Ognissanti este año…`、#56/#57 意大利语比较级词头，均为 dash 式注文的题面词头引用，非未翻译文本；P8 文本节点 CJK = 0、注文主体为西班牙语。
- **O6 — 指令词出现次数与 W43 的微差**：Completa 本版 65 次 vs W43 63 次，为 W45 核心题面驱动；指令词表成员与 W43 一致，非家具偏差。

## 证据文件（同目录）

- `REPORT.md`（本报告）
- `pre-hashes.txt` / `post-hashes.txt`（校对前后交付 + 核心哈希；diff 为空）
- `diff.txt` / `diff.json`（freeze diff 独立重跑）
- `p8.txt` / `p8-core-extract.txt` / `p8-es-extract.txt` / `p8-core.json` / `p8-es.json`（p8 compare/extract 独立重跑）
- `occlusion.txt` / `occlusion.json`（occlusion audit 独立重跑）
- `geom.py` / `geom.txt`（自写几何复测：右缘/同基线/图表覆盖/P7 横线/P8 答案底）
- `baseline-it/`（freeze baseline 重跑输出；核心 8/8 复现，核心未改动）

## 最终结论

**ZERO PROBLEMS** — 本版通过全部 11 门禁独立重测，可进入主线交付流程（GitHub 入仓由主线执行；本校对不宣布上架、不做投递）。
