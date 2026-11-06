# 独立校对报告 — Lucerna Weekly W45 DE×ES（德语目标 × 西班牙语母语）

## 结论先行：ZERO PROBLEMS（可定稿）

本轮全部从头独立重跑，不采信构建员自述；最终产物（`files/weekly-report-w45-de-es/`：svg×8、cards×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）为准。
开工查重：交付目录与构建树在 90 秒复查内零新写盘、无进行中渲染进程（最新写盘为已完成交付的 WEEKLY-KIT.md），按协调员裁定正常开工。
校对过程未改动任何交付文件、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录。

## 1. 冻结（freeze.py）

- 核心基线复现：`freeze.py baseline --build hidden_files/weekly-report-w45-de-build`（W45 DE 核心构建目录）→ **8/8 SVG byte-identical**，8 个哈希与核心 shipped 值逐一一致（p1 `6cbd4802…`、p2 `9362256d…`、p3 `3e8a8d16…`、p4 `b787f592…`、p5 `4dcbeb97…`、p6 `01b75ad4…`、p7 `fbaf8cdd…`、p8 `299524bd…`）。
  - 说明一次口径纠正：首次误用分版构建目录（`weekly-report-w45-de-es-build`）跑 baseline 得 0/8，属调用错误——该目录产出的是分版而非核心；改用核心构建目录后为 8/8。基线结论以 corrected run 为准。
- 核心开工前后哈希一致：baseline 前、后两次 sha256 全量相同（`core-hashes-before/after` 对照无 diff）。
- 最终 freeze diff（与构建员数字逐页一致）：p1 +24/−23、p2 +37/−32、p3 +43/−40、p4 +26/−22、p5 +44/−39、p6 +37/−33、p7 +59/−53、p8 +158/−141。
- **新增 CJK 字符 0；版本内 CJK 0**（8 页 SVG 文本实测均为 0）；「桥接／译注｜」0 命中。
- P1–P7 德语正文冻结判定：删项逐项核查，全部属于讲解层/家具替换——中文讲解→西文讲解、页脚/栏目标题西文化、P1 徽章槽位句（核心副标题槽位替换，见 §6）、gloss 末尾全角句号→半角、P7 标签西文化、NOCH EIN WORT 重排碎片、工具箱中文省略号尾；**无德语文章正句被删**，新增德语串仅为双语标题/gloss 中的德语词本身。P1–P7 冻结成立。
- P8 口径说明（必须如实记录，见下）：任务简写“P8 仅分隔符差异”按字面不成立——P8 +158/−141 的主体是注文从中文译为西文、括号全角→半角、12pt 重排，另加下述 keydiff 4 项。但 P8 的冻结标尺是键（key）而非注文语言：注文本就是讲解层， fan-out 必须译；键以 `p8.py compare` 为准（§2 CLEAN），故 P8 门通过，简写口径不影响结论。

## 2. P8 答案（tools/p8.py compare）

- 独立重跑：**CLEAN，core 150 noted＝edition 150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 150]**。
- 137：核心中文键「油价减税持续到十二月」→ 本版 `El descuento en la gasolina dura hasta diciembre. (laufen = durar)`。题干为德语 `Der Tankrabatt läuft bis Dezember.`，指令 `Traduce al español`，键重定向为西班牙语译文，忠实，接受。
- 138：`Ich schaue am Dienstag Fußball.` → `Veo fútbol el martes. (schauen = ver)`，同理接受。
- 139：`Die Schule hat wieder begonnen.` → `La escuela ha empezado de nuevo. (wieder begonnen = empezar de nuevo)`，同理接受。
- 140 未进 keydiff，符合预期：反向题（西文题干 `Duermo una hora más el domingo.` → 德语键），本版键 `Am Sonntag schlafe ich eine Stunde länger.` 与核心逐字一致（双版 SVG 文本实测均含该句）。
- 150：apparatus 西文化，`Pregunta abierta — sigue los puntos del cuadro de escritura; el texto modelo está en el cuadro de esta página (Se califica según los puntos indicados)`，与 W43 同款机制，接受。
- P8 分隔符 8/8 齐全：`— Página 1 —` 至 `— Página 8 —`。

## 3. 遮挡审计（tools/occlusion_audit.py）

- 独立重跑（自检先通过）：**分版 0 flags、核心 0 flags、NEW 0**。
- 首轮 22 项原址清零核查：22 项旗标原文逐项在终版 SVG 文本中检索——14 项标题/标签长串全部消失（替换为缩短版，见构建树清单对照），P6 三条长标签 `familiares que cuidan / servicio profesional / en una residencia` 已不存在（终版为单字标签 `familiares / servicio / residencia`），P6 ÜBUNGSDATEN 长注文已缩短为 `(Ejemplo de práctica, no una encuesta real.)`，P7 `Seite 6 · B2` 金线交叉已消除（终版 0 flags 且卡面目视金句标签在金线上方）。终版 0 非漏检：审计自检通过、22 项原址均已改动、卡面目视无遮挡。
- P1 顶条实测（生产字体墨盒，与任务声称一致）：左段 64.8..366.8（称 65..367）、中段 543.9..1406.2（称 544..1406）、右段 1476.2..1885.0（称 1476..1885），三段互不碰撞。
- P1 深色带实测：德语副标题墨止于 1131.5（称 1131），西文右行墨起于 1344.7（称 1345），间隙约 213px，无碰撞。
- P6 图表与后绘矩形重叠 0：德语标签墨止于 390.5／354.5／294.0（均 ＜ 西文标签起点 425）；西文标签墨止于 516.8／497.5／521.0（均 ＜ 条形起点 535，余量分别为 18.2／37.5／14.0px）；条形 rect 起点 x=535（1482／1534／1586 三条）；百分比文字位于条形末端之后。卡面目视：标签、条形、百分比三者清晰分离。
- 同基线墨迹扫描：审计 TEXTX 类 0（已含于上述 0 flags 内）。
- 终版构建日志（build-log5）：`FLOW OVERFLOW` 0、`HEAD TOO WIDE` 0。另三处 flow 游标超限（P3-ex 2582 vs 2580、P1-fussball 2298 vs 2290、P1-quiz 2552 vs 2540）为游标值而非墨迹：occlusion 0 且三页卡面目视页脚区干净，属核心 KIT §12 已说明的良性类，不构成缺陷。

## 4. gloss（按 `·` 本身拆分）

5 框各 5 项，与核心 1:1，无增删合并（gloss 句按 `·` 切分，首段含 `Nota —` 前缀）：

| 框 | 本版 5 项首词 | 核心 |
|---|---|---|
| P2 Tankrabatt | der Tankrabatt / die Zapfsäule / die Energiesteuer / die Mehrwertsteuer / der Angehörige | 5 |
| P3 Ferienwechsel | der Ferienwechsel / die Schülerin / der Ausflug / der Advent / die Lesung | 5 |
| P4 Englische Woche | die Englische Woche / auswärts / empfangen / der Favorit / eröffnen | 5 |
| P5 Pausenhof | der Pausenhof / die Klassenarbeit / das Referat / ausschlafen / die Probe | 5 |
| P6 Angehörige | der Angehörige / die Pflegeversicherung / der Pflegedienst / die Stagnation / der Aufschwung | 5 |

格式为 `德语词 = 西文释义`，前缀 `Nota — `。

## 5. P7 金句

- 8 句德语原文在全版 SVG 文本（空白归一化）中**各出现 2×**（源文章＋P7 表），逐句核实通过（句 1–8 计数均为 2）。
- P7 表页码标签（8 项）：`Seite 4 · B1、Seite 2 · A2、Seite 2 · A2、Seite 5 · B1、Seite 3 · A2、Seite 4 · B1、Seite 6 · B2、Seite 6 · B2`，与核心逐项一致；分布 Seite 2×2、3×1、4×2、5×1、6×2 成立。（全页 `Seite N` 粗计数另含 NOCH EIN WORT 的 `（Seite 2）` 引用与他处引用，不计入本表分布。）
- 金句西文译文 8 句齐全，见构建员 KIT §6（逐句与 SVG 一致）。

## 6. 家具三方对照（本版／W43 已发同配对／README #20）

- 徽章：本版 P1 SVG 元素与 W43 已发 DE×ES SVG **逐字同一元素**：`<text x="975" y="372" font-family="Noto Sans CJK SC" font-size="20" font-weight="700" fill="#a4553a" text-anchor="middle">TEXTOS EN ALEMÁN · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES</text>`。**W43 实测字号确为 20pt**，故按任务规则 W43 胜出、README #20 的 19.5pt 泛写不采纳，本版用 20pt 正确。
- 页脚 8/8 齐全（y=2624）：`Die Lucerna · SEMANARIO ALEMÁN VOL.2 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL` ＋ `Página {n} de 8`（VOL.2 随核心，W43 为 VOL.1 属预期差异）。
- masthead：核心的 `Die Lucerna` 每页均有（P1 花体字标＋各页版头右行；其余页版头＋页脚，SVG 文本每页出现 2 次）。
- 其余家具与 W43 同款：版头行、顶条中行、gloss 前缀 `Nota — `、P8 分隔符 `— Página {N} —`、P8 半角括号、章节标题德语头＋西文副标题，均实测一致。

## 7. 读者园地强制项（P7，es-ru 教训）

P7 读者栏（标题 `LESERBRIEFE · Tus cartas`）内同时具备三事实＋一句显性公开征集，全部在 P7 本栏内实测（非内容预告栏、非他页 UND SIE 提示）：

- ① 示例标注：标签 `¡Un ejemplo de la redacción!`（砖红粗体，卡面清晰）。
- ② 无真实来信：`hasta el cierre, sin cartas reales`。
- ③ 无最佳 P8 作文且顺延 VOL.3：`sin … mejores textos de la página 8` ＋ `para VOL.3`。
- 征集句原文（SVG 文本归一化后逐字一致）：`Ejemplo de la redacción, no una carta real: hasta el cierre, sin cartas reales ni mejores textos de la página 8. ¡Envíanos tu carta real para VOL.3!`
- **独立判定：末句 `¡Envíanos tu carta real para VOL.3!` 构成显性公开征集**——第二人称祈使（¡Envíanos…!）、对象明确（tu carta real）、去向明确（para VOL.3），不是内容预告（页底 `IN DER NÄCHSTEN AUSGABE` 黑带未被计入），不是练习提示。示例标注完好、无编造人名/来信（示例信署名仅为 “die Redaktion” 的编辑部示例口吻）。

## 8. 编号与级别

- 150 题连续编号，分页 **10/18/18/18/18/18/12/38**（构建日志累计 10/28/46/64/82/100/112/150；P8 compare 150 noted 亦佐证）。
- 级别徽章逐项保留、未重定级：独立计数（ex()＋reg_ex＋cloze/dialogue 元组＋3 组 match_set 各 4 题）＝ **A2 66／B1 70／B2 14**，且核心构建文件逐文件计数与分版完全一致。**B2 仅 14 属实**（P6 深读 10＋P7 B2 栏 4），未虚增。

## 9. PDF 与卡面

- 印刷版 `Die-Lucerna-VOL2-ES.pdf`：**4,143,274 B，sha256 `881865d1f2e35dca62d5e9c0219ad893a531938196057dfaf73eb1240a7195ae`，8 页，1462.5×2025 pt**——与任务给定值逐字一致。
- 网页版 `Die-Lucerna-VOL2-ES-web.pdf`：**4,164,613 B（＜10 MB），sha256 `92e581e3bfc8b7127710c2d0e3ed151ee225b3b54d71e2e7d4a776668a88cef4`，8 页，1400×1938 pt**——与任务给定值逐字一致。
- 8 张卡面全部目视（1950×2700 PNG 实测）：P1–P8 均无遮挡、无溢出、无错位；P1 顶条/深色带、P2 金线区、P6 图表、P7 金句表与读者栏、P8 键区均干净。
- ABSTRACT.txt：西文单行（1 行，末尾换行符除外）、无 ASCII 双引号、含真实主题关键词（fútbol／Champions／Bundesliga／descuento en la gasolina／cuidados／Pflege／vacaciones／vuelta al colegio）＋学习者搜索短语 `aprender alemán con fútbol`（逐字命中）。

## 10. 构建员决定事项独立裁定（非指令，逐项裁定）

**(a) P8 答案字号 12pt／lh 1.22／gap 8——接受。**
实测：content8.py keys 段确为 `kf.para(…, 12, "sans", …, 1.22, 8)`；P8 SVG 中 12pt 文本 118 个。递减链实测：核心键 14.5pt、W43 分版键 13pt、本版 12pt——偏离是渐进的、非跳变。理由成立：西文注文更长，含两条约 110 字符的 ARD 署名注文（90／92 题），13pt 下首版 flow 曾溢出（build-log 初版 keys 游标 3150 触顶），12pt 后终版 flow `P8-keys ended col 3/3 y=2113 (bottom 2560)`、零溢出。口径澄清：2113 是末列（第 4 列）游标，余量 447px 指该列；前三列按设计填满至墨底约 2556px，仍在页脚线 2580 之内、页脚基线 2624 之外，occlusion 0。可读性：P8 卡面目视键区文字小但可辨（答案核对用参考文本，非连续阅读正文）；记录为本期最小字号，后续期数不宜再缩。

**(b) P7 读者栏标签西文化（`¡Un ejemplo de la redacción!`）——接受。**
标签属讲解层家具，西文读者必须能看懂“编辑部示例”标注才有防编造意义；德语示例引言本身未动（`Liebe Lucerna, am Dienstag schaue ich Bayern bei Atlético…` 原文存续），且同栏西文段再次明示非真实来信。标注清晰度不降反升。

**(c) P2 box4 终点 1550.66 距 Rechnen 金线（1554）仅约 3.3px——接受，如实标注为“紧但已 clearance”。**
实测：ZEW 框 rect y=1254.01＋高 296.65＝底 1550.66（构建日志一致）；墨盒底 1551.36；金线中心 y=1554、线宽 2（墨盒 1553–1555）。即：框边→线中心 3.34px，框边→线上缘 2.34px，墨→线上缘 1.64px。P2 卡面目视：框底边与金线之间有一条可辨的米色缝隙，无接触、无压线。occlusion LINEX 0。结论：通过，但属全刊最紧间隙，记录在案。

**(d) P7 金句 7 译文省去“lentamente”——接受。**
核实：金句 7 德语原文含 `langsam`（`Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.`），西文译文 `La economía alemana sale del estancamiento, pero aún no se sostiene sola.` 确无 lentamente，但保留核心主张全部要素（alemana／走出停滞／复苏不能自持）。相邻金句 8 德语原文 `Es geht langsam aufwärts — aber von allein geht es nicht.` 译文 `Mejora lentamente, pero no mejora sola.` **确实承载了 lentamente**（同主题、同页相邻句，读者在同一金句表中读到该 nuance）。讲解层措辞取舍，未歪曲核心主张，接受。

## 问题清单

无。编号问题 0 项。

## 校对证据文件（本目录）

- `freeze-baseline-core.log`（核心基线 8/8）、`core-hashes-before/after.txt`、`freeze-diff.txt/.json`、`p8-compare.txt/.json`、`occlusion.txt/.json`、`analyze.txt`、`analyze2.txt`、`analyze3.txt`、`geom.txt`（P1 顶条／深色带、P2 金线、P6 图表、P8 键区墨盒实测）。
