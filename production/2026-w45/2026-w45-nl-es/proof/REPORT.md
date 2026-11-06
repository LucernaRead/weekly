# 独立校对报告 — Lucerna Weekly W45 NL×ES（荷兰语 × 西班牙语）

- **对象**：`files/weekly-report-w45-nl-es/`（SVG ×8、卡片 ×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **对照**：`files/weekly-report-w45-nl-core/`（W45 荷兰语核心，VOL.2）与 `files/weekly-report-nl-es/`（W43 同配对版，家具实测基准）
- **工具**：`tools/`，渲染/校对均用 `tools/venv/bin/python`（freeze.py、p8.py、occlusion_audit.py，另加自写解码后真墨扫描与卡片裁图）
- **校对方式**：从头独立重测，不采信构建员自述；构建员的每一项自述都以实测复核，见各门“与自述对照”。
- **校对期间的接触面**：只读交付目录、核心目录、W43 目录与构建树；唯一写盘位置是本校对目录 `hidden_files/w45/nl-es-proof/`（含隔离复现拷贝）。**未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未清理任何共享 scratch 目录。**

## 结论：ZERO PROBLEMS（可定稿）

9 门全部通过，无阻塞项。下文“非阻塞观察”不影响结论，但请主线留意其中第 1、6 条（KIT措辞 imprecise、人物改名规则宜入 SOP）。

## 开工查重

- 开工时（21:43 EDT）确有一条进行中的渲染进程，但属于 **NL×RU** 分版（`weekly-report-w45-nl-ru-build/render.py`），与 NL×ES 无关。
- NL×ES 交付目录在 90 秒复查窗（21:43:46–21:45:16）内**零新写盘**（SVG 21:37、卡片 21:37、ABSTRACT 21:41、KIT 21:43 均未变），按任务规则判定为已完成交付的新鲜 mtime，安全开工，未 stand down。
- 校对结束时（21:50）交付目录 mtime 与字节均未变；核心哈希校对前后一致（见门 1）。

## 门 1 — 冻结

- **freeze.py baseline（核心复现，独立运行）**：以 `hidden_files/weekly-report-w45-nl-build` 为构建源，隔离重定向后复现已交付核心 SVG，**8/8 字节相同**（p1 `5424557b…`、p2 `78e6fcd2…`、p3 `5b9854e3…`、p4 `cc227fd9…`、p5 `e58064c9…`、p6 `6583fe28…`、p7 `65cfe2b3…`、p8 `fe22a151…`，与交付核心全值一致）。
- **分版复现（附加独立验证）**：同样用 freeze.py 基线机制对 NL×ES 构建树做隔离复现，已交付分版 SVG **8/8 字节相同**（p1 `b1737f90…`、p2 `7e39848d…`、p3 `80ba540e…`、p4 `3cce6dff…`、p5 `3b984901…`、p6 `e9daa31b…`、p7 `6131d67a…`、p8 `0b23b55f…`），且复现全程**零 FLOW OVERFLOW / HEAD TOO WIDE**。复现运行独立给出注册表：总数 150、分页 10/18/18/18/18/18/12/38、级别 A2 47 / B1 72 / B2 31、范文 87 词——与核心对照值逐项一致。复现的终态流位置亦与构建员称述一致：P1-headline 止于 y=1452、P2-ex 止于 y=2407、P7 col-3 止于 y=1925.5、P8-keys 止于 y=2339。
- **freeze.py diff（核心 vs 分版，独立运行）**：p1 +29/−28、p2 +39/−33、p3 +32/−27、p4 +28/−25、p5 +38/−33、p6 +36/−32、p7 +51/−49、p8 +178/−166（字符串个数，与构建员自述逐页一致）；**每页新增 CJK 均为 0，总计 0**；分版 SVG 全页 CJK 字符 0、全角括号 0。
  - 说明：核心本身带有中文讲解层（每页 CJK 191/212/153/126/214/192/373/1033），分版是把该层全部替换为西班牙语讲解层，而非“核心无中文”。冻结门的正确读法是**新增 CJK=0**，本版通过；不要把核心 CJK 总数误读为分版缺陷。
- **荷兰语正文删除裁定（逐条）**：删除串总计 393（含重复计数），其中含 CJK/全角字符的 388 条均为讲解层本地化（中文讲解被西班牙语讲解替换，其中的荷兰语词头在对应新增串中原样保留，如 planten、besparen、de waarschuwing）。**不含 CJK 的删除串仅 5 条**，逐条裁定如下，全部不是正文删除：
  1. P7 `«Hallo! Ik ben Li en ik leer`、P7 `Nederlands in Shanghai. In de`、P7 `mijn balkon!» — Li (voorbeeldbrief`——读者园地示例人物改名/改城（见门 6 独立裁定），除姓名/城市外例句其余荷兰语逐字未动。
  2. P7 `van de redactie)`——换行切分伪影：核心将其作独立行，分版将其并入 `(voorbeeldbrief van de redactie)` 一行，词内容未丢失。
  3. P8 `6. planten — veel mensen → planten`——P8 答案注本地化：key `planten` 未动，注由荷兰语 `veel mensen → planten` 改为西班牙语 `Sujeto plural → planten`（见门 3 的 #6 不在 keydiff 中、key 逐字节相同的一致逻辑）。
  - 换行切分伪影与正文删除的区分依据：删除串的荷兰语词/句均可在分版并合后的文本或对应新增串中找到；无任何一篇课文段落、题干、选项、图表数据、署名、金句出现整句删除。
- **校对前后核心哈希不变**：开工前、diff/p8/occlusion 后、基线后、复现后四次 sha256 均相同（见上核心全值缩写）。
- **新增串说明**：新增 431 条多于删除 393 条，差额来自西班牙语行宽重排产生的文本节点拆分（如 P8 +12），非内容增加；新增串 0 CJK。

## 门 2 — P7 词框冻结

- 定义句逐字核实：核心与分版 P7 词框中，规范化后的整页连接文本均恰好含有 1 次
  > «meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.
  分版词框原文行：`«meedoen» betekent: deelnemen,` / `erbij zijn. In de Klimaatweek doet` / `heel Nederland mee.`——与核心逐字相同，**未本地化**。
- 仅 gloss 行本地化：分版词框下 gloss 为 `meedoen = participar: en la Semana del Clima participa todo el país.`（两行并合），定义句本身未动。**通过**。

## 门 3 — P8

- **tools/p8.py compare（独立运行）**：`core 150 noted，edition 150 noted，status: CLEAN，missing=[]，extra_count=0，uncertain=[]，keydiff=[7, 17, 70, 71, 76, 96, 137, 138, 148]`——与构建员自述完全一致。EXTRA_ONLY 不适用（状态是 CLEAN）。
- **keydiff 逐项对照印刷 P8 行**（以解码后原始答案段 segment 为准，dash-token = ` — ` 前第一段）：
  - **真实重定向 2 项**：
    - #137：核心 `气候周持续七天。 — 对照第 1 版头条` → 分版 `La Semana del Clima dura siete días. — Compara el titular de la página 1`。E 类翻译题的 key 随读者语重定向（中→西），荷兰语对照句未受影响，属合法重定向。
    - #138：核心 `橙色预警意味着：做好准备。 — 第 2 版原句 · bereid je voor 做好准备` → 分版 `El código naranja significa: prepárate. — Frase de la página 2 · bereid je voor = prepárate`。同上，合法重定向；注中荷兰语 `bereid je voor` 保留。
  - **p8.py 括号分支提取伪影 7 项**（全部证实）：工具对 `key — note (尾括号片段)` 型行走 paren 分支，返回“key+注去尾括号”作伪 key，因而注一翻译伪 key 即不同；但印刷 key 本身（dash-token）两版**逐字节相同**：
    - #7：B / B；核心段 `B — 气候周共 7 天（11 月 2–8 日）`，分版段 `B — La Semana del Clima dura 7 días (2–8 de noviembre)`。
    - #17：wortelen / wortelen；注 `生根（复数主语）` → `echar raíces (sujeto plural)`。
    - #70：eiland / eiland；注 `岛（het）` → `la isla (het)`。
    - #71：proef / proef；注 `比赛项目、考验（de）` → `la prueba (de)`。
    - #76：gaat winnen / gaat winnen；注 `会赢（只是猜测）` → `va a ganar (solo una suposición)`。
    - #96：advies / advies；注 `建议（het）` → `el consejo (het)`。
    - #148：B / B；注 `柔软的（土壤）` → `blanda (la tierra)`。
    - 机制说明（#7 为例）：段中第一处 ` — ` 位于尾括号组开口之前，故工具不走 dash 分支而走 paren 分支；伪 key 差异的唯一来源是注的翻译。工具未被修改，伪影已在印刷行层面证伪，**不阻塞**。
  - **#139/#140 未列入 keydiff，正确**：两题题干由中文→西班牙语（#139 `博物馆之夜从晚上 19 点到凌晨 2 点。→ ___` → `La Museumnacht dura desde las 19:00 hasta las 02:00. → ___`；#140 `我参加气候周。→ ___` → `Participo en la Semana del Clima. → ___`），荷兰语 key 逐字节相同（#139 `Museumnacht duurt van 19:00 uur tot 02:00 uur.`；#140 `Ik doe mee aan de Klimaatweek.`），故工具不列入 keydiff 是正确的。
  - **#150（不在 keydiff，独立核实）**：
    - 工具说法成立：两版均提取为 `✓`（核心段 `✓ 范文见本版 H 区（87 词）`，分版段 `✓ El modelo está en la sección H de esta página (87 palabras)`），故工具无法、也不应列入 keydiff。
    - W43 先例成立（答案行层面）：W43 NL×ES P8 第 150 答案行与本版**逐字相同**：`150. ✓ El modelo está en la sección H de esta página (87 palabras)`。H 区题头亦由中文本地化为西班牙语（核心 `写作题（无唯一答案）；范文（87 词）见下。` → 分版 `Pregunta abierta (sin una única respuesta); el modelo (87 palabras) está abajo.`），语义完整。
    - **key 本身未错位**：范文荷兰语正文两版逐字相同，独立计词 **87 词**（在 80–100 要求内）；题干 `«Jouw week in de Klimaatweek» Schrijf 80–100 woorden…` 亦逐字相同。#150 的变化只在讲解语言，不在答案指向。
    - KIT 措辞问题（非阻塞，见“非阻塞观察”第 1 条）：KIT §5 把 H 区变化简写为 `（开放题，范文如下） → (Pregunta abierta — modelo a continuación)`，后一串是 W43 的 H 区题头原文，不是本版分版的题头原文；本版答案行与 W43 先例的对应关系本身是真实的。

## 门 4 — 几何遮挡

- **tools/occlusion_audit.py（独立运行，selftest 通过）**：分版 **0 旗**、核心 **0 旗**、NEW vs 核心 **0 旗**。与构建员终态自述一致（构建树中旧的 `occlusion.txt` 2 旗是修复前快照，已被 `occlusion-fix1.txt` 的 0/0/0 取代；本次独立运行确认终态为 0）。
- **同基线墨迹碰撞扫描（独立重测，解码后真墨，非 advance 宽度）**：
  - 方法：以 occlusion_audit.py 的真墨盒（PIL/FreeType `getbbox` + `getmetrics` ascent 基线锚定）重算 P1 `IN DEZE EDITIE` 目录行，文本先 `html.unescape` 解码（`&amp;` 等未解码读数不采用；本区无 `&amp;`，但全程按解码后文本计量）。
  - 结果：分版与核心的 7 行目录行真墨盒**逐项完全相同**（冻结行未动）。每行 Pag.→标题真墨间隙均为 **4.0px**；标题→级别间隙分别为 27.8 / **0.2** / 49.1 / 18.1 / 74.1 / 47.7 / 26.6px——**全部为正，无重叠**。构建员称的“8 旗”确为 advance 宽度伪影：advance 宽度含字距边衬故在 8 处报 gap<4px（其中 Pag.3 行报 0.4px），真墨下最紧处仍有 0.2px 正间隙。**真墨碰撞 0，伪影解释成立**。
  - 卡片裁图证实：P1 目录区全分辨率裁图（x1440–1900, y1340–1700）显示 7 行目录清晰可读、无字符粘连/覆盖；Pag.3 行 `Musea bij nacht en boeken` 与 `A2→B1` 在视觉上贴近（与 0.2px 真墨间隙一致），但字符墨迹不相交，且该几何与核心完全相同，不是分版新缺陷。
- **P6 图表标签覆盖（基线锚定墨迹法重测）**：标签字体 Noto Serif 19.5pt，基线 294/352/410/468；条形顶 304/362/420/478。真墨盒底分别为 299.25 / 357.25 / 415.0 / 468.25，净空 **4.75 / 4.75 / 5.0 / 9.75px**，**覆盖 0% ×4 行**，远低于 30% 阈值。构建员称“每行净空 4px”是 0.30×字号的近似算法，偏保守；真墨实测净空更大，结论不变。**通过**。
  - 卡片裁图证实：P6 图表区裁图（x1440–1900, y220–530）显示 4 标签与 4 条形（45/25/20/10）上下分明、无压盖。

## 门 5 — gloss 计数与金句

- **gloss() 字符串本身拆 `·` 计数**（以两版构建源的 gloss() 调用串为准，并以渲染后 SVG 的 gloss 框行并合串复核，两者一致；词头顺序 1:1）：
  - P2：核心 6 = 分版 6（het klimaat / wortelen / besparen / de verwarming / de waarschuwing / lokaal）。
  - P3：核心 5 = 分版 5（het museum / de rondleiding / het tijdslot / tweedehands / de beurs）。
  - P4：核心 5 = 分版 5（de balans / gelijkspelen / de speelronde / de topper / de stand）。
  - P5：核心 5 = 分版 5（het eiland / de proef / stemmen / de aflevering / voorbij）。
  - P6：核心 5 = 分版 5（de meteoroloog / waarschuwingsmoeheid / vastzetten / het advies / de voorstander）。
  - **全部 1:1，无增减、无错位**。分版 gloss 框前缀确为 `Nota — `（见门 7）。
- **P7 金句 8 句**：每句荷兰语原文在分版全书规范化文本中恰好出现 **2×**（课文 + P7 引用），P7 引用均带 `«»` 且其后西班牙语译文行标注页码与核心一致：**Pagina 1×2、Pagina 2×1、Pagina 3×1、Pagina 4×1、Pagina 5×1、Pagina 6×2**。逐句核实每句在其标注页的课文中实测存在：
  - P1：`Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland`、`De herfst is de beste tijd om te planten`；
  - P2：`Geel betekent: let op, het weer kan gevaarlijk zijn`；
  - P3：`Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts`；
  - P4：`Ajax won donderdag 22 oktober met 2–0 van Atalanta`；
  - P5：`Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur`；
  - P6：`Een code is geen verbod, maar een advies`、`Het weer is van ons allemaal, maar het raakt ons allemaal anders`。
  - **通过**。

## 门 6 — 读者园地（零编造）与人物改名独立裁定

- **页上三事实齐全**：
  1. 截稿时无真实来信：荷兰语披露句原文保留 `Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.`；西班牙语披露句同义 `Sin cartas reales ni mejores textos de la página 8 al cierre: publicamos este ejemplo; los prometemos para el VOL.3.`（无真实来信、无最佳 P8 作文、刊登本示例、VOL.3 承诺四要素齐全）。
  2. 无最佳 P8 作文：同上两句均含该要素。
  3. 示例 + VOL.3 承诺：同上；另 P7 下期预告行 `Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!` 仅为内容预告，**未被计入邀请或承诺**（按任务规则，预告行不算）。
- **显性西班牙语邀请（逐字核实）**：P7 BRIEVEN 框末三行并合为
  > Ejemplo de la redacción, no una carta real. ¡Envíanos tu carta real y tu mejor texto! Los publicaremos en el VOL.3!
  与构建员称述逐字一致；含祈使句 `¡Envíanos…!` + 刊登承诺 `Los publicaremos en el VOL.3`，**显性邀请成立**。
- **示例标注**：例句署名行保留荷兰语标注 `(voorbeeldbrief van de redactie)`，且西班牙语邀请句首即声明 `Ejemplo de la redacción, no una carta real`——示例身份以两种语言明示，无冒充真实来信的可能。
- **P7 栈底**：BRIEVEN 框末基线 y=1895.77，栈底 y=1925.5（复现运行同值），金句分隔线 y=1937，净空 11.5px；卡片裁图（右栏 x1440–1900, y1500–2000）显示 BRIEVEN 框完整收束于分隔线之上。**通过**。
- **人物改名独立裁定（Li/Shanghai → Lucía/Madrid）：不构成编造，不阻塞。理由（独立于两边先例）**：
  1. **不编造门的检验标准是“是否把虚构当真实呈现”，而不是“是否出现虚构名字”。** 本例在同一框内以两种语言三重声明其虚构/示例身份：署名标注 `(voorbeeldbrief van de redactie)`、荷兰语披露句 `nog geen echte brieven…`、西班牙语 `Ejemplo de la redacción, no una carta real`。读者不可能合理地把 Lucía 当作真实来信者；所谓“虚构身份”在这里是**公开的示例身份**，与编造（把虚构冒充真实）方向相反。
  2. **改动范围确为构建员所述的“仅姓名/城市”**：例句其余荷兰语逐字相同（`«Hallo! Ik ben … en ik leer Nederlands in …. In de Klimaatweek plant ik een boom op mijn balkon!»`），无姓氏、无地址、无真实人物指向、无新增事实主张；改动不改变任何语法/词汇教学点、不改变任何题答案。
  3. **冻结门的检验标准是荷兰语正文是否被删改**：例句属于自声明的编辑部示例，不是课文、题干、key 或金句；其姓名/城市 token 是示例人设占位符，不是课程正文。严格字面看确有 2 个 token 变化，但该变化已被门 1 逐条记录、被门 6 的三重反编造声明覆盖，且不构成正文删除——冻结门通过，改名不构成冻结门下的阻塞。
  4. **对两边先例的定位**：NL×FR 校对裁定“保留 Li 合规”，确立的是**保留的安全性**，不是“改动即违规”——保留安全不等于改动禁止。W43 NL×ES 同配对版确已使用 Lucía/Madrid（本校对在 W43 P7 实测确认），证明该改动在本配对内有已交付先例、非本版临时起意。但本裁定的成立**不依赖** W43 先例：即使没有 W43 先例，仅凭第 1–3 条（公开示例身份 + 仅两 token + 无事实主张），结论同样是不阻塞。反之，若改动指向可识别的真实人物、或去掉示例标注，则不论有无先例都应阻塞——本版两者皆无。
  5. **保留意见（非阻塞）**：W45 其他 NL 分版（DE/EN/FR/IT/PT/RU）P7 均保留 Li/Shanghai，唯 NL×ES 改动，是本轮唯一的家族内不一致。建议 SOP 明确写入“读者园地示例人设是否可按读者语本地化、以及本地化边界（仅名/城、无姓氏、无真实指向、标注与披露缺一不可）”，避免以后每版重议。此项不影响本版结论。

## 门 7 — 家具（以 W43 实测为准）

- **徽章（逐属性对照 W43）**：分版与 W43 **全部属性相同**：x=975、y=568、20pt、粗体（700）、砖红 `#a4553a`、居中（middle）、字符串逐字相同 `TEXTOS EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`、advance 宽度 1116.45px。插槽亦同 W43（P1 上部带区与标题区之间）。**通过**。
- **gloss 前缀**：分版 P2–P6 gloss 框首行均为 `Nota — `，与 W43 同配对实测一致。**通过**。
- **P8 分隔符**：分版 P8 答案流分隔符为 `— PAGINA 1 —` 至 `— PAGINA 8 —`（8 个），与 W43 实测逐字相同；构建员称未用 tables.json 的 `PÁGINA` 写法，属实（tables 变体在分版 P8 中出现 0 次）。核心 P8 分隔符本身也是 PAGINA 形式，故三方一致。**通过**。
- **副标题字号（接受 40pt，不用 W43 的 36pt 回退）**：分版副标题 `SEMANARIO NEERLANDÉS · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12`，40pt serif 粗体，居中 x=975，实测宽度 **1811.45px**，跨度 69.27–1880.73，位于版心 65–1885 内（左右各余 4.27px）、位于内框 52–1898 内；卡片上为单行、无溢出，遮挡审计 0 旗。反查 W43：其副标题串在 40pt 下实测 **1972.45px**（超 1820 版心），在 36pt 下为 1775.02px，故 W43 用 36pt 是被迫的；本版串在 40pt 下已能装入，故不回退是**有实测依据的接受**，不是偷懒。附注：4.27px 余量偏紧，但属版心内合法排版，非缺陷。
- **P6 两盒题缩短（核实无截断、无内容丢失）**：
  - 图表题头：分版 `DE GRAFIEK · EL GRÁFICO`（24pt，实测 312.39px，与构建员称 312px 一致）。字面长式 `DE GRAFIEK · EL GRÁFICO (DATOS DE PRÁCTICA)` 在同字号下实测 573.66px（≈构建员称 574px），确超盒内宽；缩短后题头为完整短语，非中途截断；被省的“练习数据”限定语并未丢失——图表下方 OEFENDATA 框即以西班牙语完整说明 `Datos de práctica: cifras inventadas, solo para practicar, no una encuesta real.`。
  - 正反方题头：分版 `VOOR OF TEGEN? · PROS Y CONTRAS`（21pt，实测 386.56px，与构建员称 387px 一致）。字面长式 `VOOR OF TEGEN? · ¿A FAVOR O EN CONTRA?` 实测 458.0px（与构建员称 458px 逐值一致），确超 390px 盒内宽；缩短后题头完整，盒内正文仍为 `Voor lokaal: …` / `Tegen lokaal: …`，且同页中栏题头 `VOOR OF TEGEN LOKAAL?` 未动，“本地”范围未丢失。
  - 另核 P1 数字题头 `DE WEEK IN CIJFERS · EN CIFRAS` 实测 379.95px（≈构建员称 380px），在 390px 内。**通过**。
- **页脚 8/8 标 VOL.2**：每页页脚均为 `De Lucerna · SEMANARIO NEERLANDÉS VOL.2 · TEXTO EN NEERLANDÉS · EXPLICACIONES EN ESPAÑOL` + `Página N de 8`（N=1–8，P8 另有栏目标题行 `Página 8 · De grote toets van de week + alle antwoorden`，不影响页脚判定）。**通过**。

## 门 8 — 其他

- **图片（仅公有领域/CC0，4 张署名图均已排版）**：图片元素数量与几何与核心逐页相同：P1 1 张（65,1874,896×320）、P2 1 张（1451,200,434×272）、P3 1 张（1451,200,434×250）、P4 1 张（1451,200,434×250），P5–P8 0 张，**无新增图片**。署名行与核心逐字相同：
  - P1 `Foto: Vovogov90 — CC0`；P2 `Foto: Nationaal Archief — CC0`；P3 `Foto: W. Punt / Anefo, Nationaal Archief — CC0`；P4 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein`（两行并合）。
  - 构建员称 credit 行取自 Commons API Artist 字段：本校对能独立证实的是署名行与核心/W43 资产逐字一致、无新增、无改写；Artist 字段的 API 原始返回不在本次交付物内，未作超出证据的断言。卡片上 4 图均已排版可见（P1 秋林、P2 风车、P3 运河船、P4 1912 球队）。
- **全文禁词**：解码后 SVG 文本、ABSTRACT.txt、WEEKLY-KIT.md 中 `桥接` 出现 **0 次**（8 页 SVG 逐页 0）。
- **ABSTRACT.txt**：单行（文件 1 行，348 字节），无 ASCII 双引号，西班牙语；含真实主题关键词（Semana del Clima 2–8 Noviembre、Museumnacht、Crossing Border Festival、Eredivisie jornada 12、códigos del KNMI）与学习者搜索短语（`aprende neerlandés leyendo noticias reales`、`vocabulario del clima`、`verbos separables`，另标 A2–B2 / 150 ejercicios）。**通过**。
- **8 张卡片逐页目视检查**：1950×2700 PNG ×8 全部读过（缩略图全页 + P1 目录、P6 图表、P7 BRIEVEN 三处全分辨率裁图）：**无重叠、无截断、无缺字**。P1 徽章/副标题/词框与 IN HET KORT 框分明；P7 BRIEVEN 框与金句区分离；P6 图表标签与条形分离；P8 答案流止于页脚之上。
  - 方法注：首张 P7 裁图曾误切左栏（y1750–2100, x40–1000），发现后已重切右栏 BRIEVEN 区（x1440–1900, y1500–2000）并据此裁定；终态结论以正确裁图 + SVG 几何为准。
- **PDF**：印刷 PDF 7,917,403 B、sha256 `14009e0c85cdde7871fcd09d6ddef59ad8bf683fb2675895af17bc0968096026`、8 页；网页 PDF 3,680,221 B（<10 MB）、sha256 `83443cc2b293595ae25b2a7a20e27fc3d49df2531876df51e511359e7032c733`、8 页——与任务给定值逐字节一致。页尺寸：印刷 1462.5×2025 pt（即 1950×2700 px 版式）、网页 1400×1938 pt。
- **修复轮终态验收（只验终态）**：P1/P2 流溢出缩短与遮挡 2 旗缩短均只验收终态：终态遮挡 0/0/0（门 4）、P1-headline 止 y=1452 与 P2-ex 止 y=2407 与核心流位置一致（复现运行）、P1/P2 课文与题干的荷兰语内容在冻结差分中无删除（门 1）、题号分页与核心一致（见下）。西班牙语讲解缩短未造成内容丢失。
- **题号与级别（附加核实）**：分版题号按页为 1–10 / 11–28（含 `25–28.` 合并题头）/ 29–46 / 47–64 / 65–82 / 83–100 / 101–112 / 113–150（含 `141–144.` 合并题头），并集恰为 1–150 连续（P4 的 `0–2.` 为比分区间文字，已排除，非题号），与核心逐页一致；级别 pill 文本计数与核心相同（A2 45、B1 76、B2 30，另 A2→B1、A2→B2 各 1）；注册表级别分布 A2 47 / B1 72 / B2 31 由隔离复现独立得出（非仅引构建员日志）。

## 与构建员自述不符处（均非阻塞）

1. **KIT §5 的 #150 简写不精确**：KIT 称 H 区变化为 `（开放题，范文如下） → (Pregunta abierta — modelo a continuación)`。实测：核心 H 区题头是 `写作题（无唯一答案）；范文（87 词）见下。`，分版题头是 `Pregunta abierta (sin una única respuesta); el modelo (87 palabras) está abajo.`；`(Pregunta abierta — modelo a continuación)` 是 **W43** 的题头，不是本版题头。真正与 W43 逐字相同的，是本版 **P8 第 150 答案行**。分版页面本身无误，仅 KIT 措辞把两处对应关系写混了。建议 KIT 订正此句，不影响定稿。
2. **P6 图表净空数值**：构建员称“每行净空 4px”是 0.30×字号近似值；真墨实测为 4.75 / 4.75 / 5.0 / 9.75px，覆盖 0%。构建员数值偏保守，结论（<30% 通过）不变。
3. 其余构建员自述（冻结差分逐页数、P8 CLEAN 与 keydiff 表、遮挡 0/0/0、gloss 计数、金句 2× 与页码、读者园地三事实与邀请原文、徽章/副标题/P6 缩短宽度、页脚、PDF 字节与哈希）经独立重测**全部复现一致**，无其他不符。

## 非阻塞观察（注明：不阻塞）

1. P1 目录最紧处（Pag.3 标题→`A2→B1`）真墨间隙仅 0.2px：属核心冻结几何，分版与核心逐项相同，视觉上贴近但墨迹不交；不是分版新缺陷，无需修复（改动它反而会破坏冻结）。
2. 副标题 40pt 左右余量仅 4.27px：版心内合法，单行无溢出；若未来副标题串更长，应优先触发 36pt 回退规则（W43 已有此先例）。
3. P6 正反方题头在 390px 盒内宽下余量仅 3.44px：已装入、无截断；同属“紧但合法”，无需改动。
4. 读者园地人物改名是 W45 NL 家族内唯一例外（其余分版保留 Li）：本版裁定不阻塞，但建议 SOP 明确人设本地化规则（见门 6 第 5 条）。
5. 核心 CJK 总数、文本节点数差异（分版每页 +1 至 +12 节点）均为西班牙语重排/替换的正常表现，已在门 1 说明，不视为内容增减。
6. P4 的 `0–2.`、P8 答案流的合并题头等计数伪影已在门 8 排除，不影响 1–150 连续性结论。

## 校对证据文件（本目录）

- `freeze-diff-own.txt` / `freeze-diff-own.json` / `freeze-adjudication.txt` / `freeze-classify.txt`——冻结差分与删除串逐条裁定
- `baseline-own.txt`——核心 8/8 复现；`repro-edition-own.txt` / `repro-reg-own.txt`——分版 8/8 复现与注册表
- `p8-compare-own.txt` / `p8-keydiff-own.txt` / `p8-150-139140.txt`——P8 CLEAN、keydiff 逐项印刷行、#150/#139/#140
- `occlusion-ed-own.txt` / `occlusion-core-own.txt` / `occlusion-new-own.txt`——遮挡 0/0/0；`ink-scan-own.txt`——解码后真墨扫描与 P6 图表
- `p7-gloss-golden.txt` / `p7-ed-detail.txt` / `gloss-count-golden.txt` / `golden-own.txt`——P7 词框、gloss、金句
- `furniture-own.txt`——徽章/副标题/P6 题头/分隔符/页脚 vs W43 实测
- `gate8-own.txt` / `gate8b.txt` / `counts-own.txt` / `counts2.txt`——图片/禁词/ABSTRACT/PDF/题号
- `crops/`——8 页缩略图与 P1 目录、P6 图表、P7 BRIEVEN 全分辨率裁图
- `core-before.txt` / `core-after-baseline.txt` / `core-final.txt` / `ed-before-repro.txt` / `ed-after-repro.txt`——校对前后哈希未变记录

**再次声明结论：ZERO PROBLEMS——本分版可定稿。** 本报告未宣布上架、未做任何交付目录修改；后续入 GitHub 仓库等动作由主线按既有流程决定。
