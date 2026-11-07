# WEEKLY-KIT — Lucerna Weekly W45 DE×ES（德语目标 × 西班牙语母语）

**状态：builder-complete，未定稿，待独立校对。** 本文件只记录构建员自测结果，不作定稿宣称。

## 0. 规格与交付物

- 期刊：Die Lucerna VOL.2，issue 周 2026-11-02（周一）至 2026-11-08（周日）。
- 配对：目标语德语（正文全部冻结），讲解层直接写给西班牙语母语读者；讲解层无“桥接”一词，无编造的读者来信／人名／引言。
- 交付目录：`files/weekly-report-w45-de-es/`：svg × 8、cards × 8（1950×2700 PNG，已实测）、印刷 PDF 8 页、网页 PDF 8 页、WEEKLY-KIT.md（本文件）、ABSTRACT.txt（西文单行，无 ASCII 双引号）。
- 构建树：`hidden_files/weekly-report-w45-de-es-build/`（content 文件、transform.py、render.py、run.py、build-log*.txt、freeze/p8/occlusion 输出、核心哈希快照）。
- 底本：W45 DE 核心 `files/weekly-report-w45-de-core/`（已定稿上架，只读，未动）；对照：W43 已发 DE×ES `files/weekly-report-de-es/`（VOL.1，只读，未动）。
- 开工查重：开工时本版交付目录与构建树均不存在，无进行中写盘；唯一运行中的渲染进程是无关的 W45 DE×EN occlusion 进程，按协调员裁定正常开工。
- 未做事项（任务禁令遵守）：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录。

## 1. 渲染环境（实测，非含糊表述）

- 全部 SVG / cards / PDF 产物均由 `tools/venv/bin/python` 生成（系统 python3 缺 cairosvg，未用于任何渲染）。
- 该解释器下 PIL 版本：13.0.0。
- 渲染方式：构建树内单进程 `run.py` 驱动（content 模块共享注册表须同一 driver 进程，README #7）；绝不在核心构建目录内 import 内容模块（README #11）。

## 2. 冻结对照（freeze.py）

- 核心基线复现：`tools/freeze.py baseline` 对 W45 DE 核心构建复现 **8/8 SVG byte-identical**。
- 核心哈希开工前后一致（开工前／最终渲染后两次重验，8/8 哈希值相同，仅路径前缀因工作目录不同）：
  - p1 `6cbd48022b5f863d`、p2 `9362256dca74f877`、p3 `3e8a8d16136a46a3`、p4 `b787f592599cc4d1`、
  - p5 `4dcbeb97c566f4df`、p6 `01b75ad49a54c803`、p7 `fbaf8cdd8a90f299`、p8 `299524bd2ad25ec4`。
- 最终 freeze diff（新增／删除串数）：p1 +24/−23、p2 +37/−32、p3 +43/−40、p4 +26/−22、p5 +44/−39、p6 +37/−33、p7 +59/−53、p8 +158/−141；**新增 CJK 字符总数 0，版本内 CJK 0**（SVG 文本实测亦为 0；`桥接／译注｜` 扫描 0 命中）。
- 碎片级 adjudication：P1–P7 纯德语删除项仅 P1 徽章槽位句 `DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND`（按 W43 先例＋README #20，徽章替换 y=372 副标题槽位）；P3/P4/P6 删除的 `。` 为核心 gloss 末尾全角句号碎片（西文版改半角 `.`）；P7 删除的 `Ein Beispiel der Redaktion!`（标签西文化，见 §8）、`«der Tankrabatt»（Seite 2）: die`（NOCH EIN WORT 段重排碎片，德语句子本身存续）、`……`（工具箱中文省略号尾）；其余“纯德语”新增项实为含西文的双语标题／注文碎片（ASCII 过滤假象）或重排碎片。
- P8 差异组成（任务“P8 仅分隔符差异”的实际 adjudication 口径）：分隔符、注文翻译、括号全角→半角（DE 族已发分版先例，README #14）、12pt 重排、键 137/138/139 重定向、150 apparatus 西文化。键内容冻结以 §3 p8 compare 为准。

## 3. P8 答案核验（tools/p8.py compare）

- 结果：**CLEAN 150=150，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 150]**；双版 extract 均为 noted 150/150。
- 逐项判定（非工具伪影，均为真实且正确的改动）：
  - 137 `El descuento en la gasolina dura hasta diciembre. (laufen = durar)` — DE→ES 翻译题键重定向，忠实于德语题干。
  - 138 `Veo fútbol el martes. (schauen = ver)` — 同上。
  - 139 `La escuela ha empezado de nuevo. (wieder begonnen = empezar de nuevo)` — 同上。
  - 140 未进 keydiff，符合预期：反向题（ES 题干→DE 键），德语键 `Am Sonntag schlafe ich eine Stunde länger.` 与核心完全一致。
  - 150 apparatus 西文化（与 W43 同款）：`Pregunta abierta — sigue los puntos del cuadro de escritura; el texto modelo está en el cuadro de esta página`／`Se califica según los puntos indicados`。
- P8 注文全为西文；P8 分隔符：`— Página {N} —`（8 页齐全）；注文括号：半角 ` (note)`（content8.py 键生成行已改，核心为全角 `（note）`，DE 族已发分版先例）。
- P8 几何：battery 终点 1500（限 1505）；keys 终点 2113（限 2560，余量 447px）。字号说明见 §8。

## 4. 遮挡审计（tools/occlusion_audit.py）

- 初检（修复前）：版本 22 flags（BOXTITLE 12、COVER 3、EDGE 5、LINEX 1、TEXTX 1），核心 0 flags；全部 22 项均为西文标题／标签过长，非继承项。
- **终检（修复后）：版本 0 flags、核心 0 flags、NEW 0**（`occlusion-final-0flags.txt`；初检清单存 `occlusion-first-22flags.txt`）。
- 22 项逐项修复（措辞修正，不动几何参数；墨宽均以生产字体实测通过）：
  - P1 Zahlen 框标题 → `DIE WOCHE IN ZAHLEN · En cifras`（384.3 ≤ 416）；P1 Fragen 副标题 → `Preguntas · Die Fragen der Woche`（308.6 ≤ 412）；P1 Fragen 底行 → `Las cinco preguntas de la semana.`（301.5 ≤ 412）；P1 sommaire → `IN DIESER AUSGABE · Contenido`（391.8 ≤ 412；`Este número` 版 417.0 超限，弃用）。
  - P2 盒标题 → `AN DER ZAPFSÄULE · El surtidor`（387.2 ≤ 412）；P3＋P5 FERIENWECHSEL 盒标题 → `FERIENWECHSEL · Vacaciones`（365.9 ≤ 412，两处同改）；P3 HERBSTWÖRTER → `HERBSTWÖRTER · Vocabulario`（373.2）；P3 DER TIPP → `DER TIPP · Consejo`（238.0）；P5 SCHULWÖRTER → `SCHULWÖRTER · Vocabulario`（357.7）；P6 DIE ZAHLEN → `DIE ZAHLEN · Cifras`（242.8）；P7 读者栏标题 → `LESERBRIEFE · Tus cartas`（W43 原文，299.9 ≤ 412）。
  - P6 图表西文标签 → `familiares`（91.8 ≤ 110）、`servicio`（72.5）、`residencia`（96.1），条形起点 x=535 不可逾越；德语标签实测止于 65+325.3=390.3 ＜ 425 起点，无碰撞。
  - P6 图表注文西文括号 → `(Ejemplo de práctica, no una encuesta real.)`（整句 1684.5 ≤ 1820）。
  - P7 金句 7 西文翻译 → `La economía alemana sale del estancamiento, pero aún no se sostiene sola.`（2 行；德语引言逐字冻结不动），页码标签上移脱离 FEHLERKLINIK 金线（1967–1969；标签墨底约 1953）。
- 同基线墨迹扫描（README #10 式）：全部 SVG 同基线文本对重叠 **0**；P1 顶条三段墨区间：65..367／544..1406／1476..1885，无碰撞；P1 深色带：德语副标题止于 1131，西文右行起于 1345，无碰撞。
- P6 图表文本与后绘矩形重叠 **0**（audit COVER 清零＋数值核查：德语标签止于 ≤390 ＜ 西文标签起点 425；西文标签止于 ≤521 ＜ 条形起点 535；百分比文字位于条形末端之后）。
- 终版构建日志零 `FLOW OVERFLOW`／`HEAD TOO WIDE`；P3-ex 终点 2582（限 2580）、P1-fussball 终点 2298（限 2290）、P1-quiz 终点 2552（限 2540）属核心 KIT §12 已说明的良性类（末题在非末列或末字形底在页脚线之上），与核心同值／同类。

## 5. gloss 计数（按 `·` 本身拆分，README #21）

| 框 | 核心 | 本版 | 判定 |
|---|---|---|---|
| P2 Tankrabatt 框 | 5 | 5 | 1:1 |
| P3 Ferienwechsel 框 | 5 | 5 | 1:1 |
| P4 Englische Woche 框 | 5 | 5 | 1:1 |
| P5 Pausenhof 框 | 5 | 5 | 1:1 |
| P6 Angehörige 框 | 5 | 5 | 1:1 |

无增删合并。gloss 前缀：`Nota — `（bslib4.py）；bridge 方法已按 W43 更名为 `expl`（bslib＋全部调用点）；gloss 格式：`德语词 = 西文释义 · …`（沿用 W43 `=` 式）。

## 6. P7 金句核验（逐字摘句）

8 句德语原文在渲染 SVG 文本中（空白归一化）各出现 **2×**（源文章＋P7 表）：

| # | 德语原文（逐字） | 页码标签 |
|---|---|---|
| 1 | Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga. | Seite 4 · B1 |
| 2 | Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter. | Seite 2 · A2 |
| 3 | Wer 50 Liter tankt, spart rund 8,35 Euro. | Seite 2 · A2 |
| 4 | Die Schule hat nach den Herbstferien wieder begonnen. | Seite 5 · B1 |
| 5 | Die Tage sind kurz, die Abende lang. | Seite 3 · A2 |
| 6 | Zwei schwere Auswärtsspiele für die deutschen Teams. | Seite 4 · B1 |
| 7 | Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst. | Seite 6 · B2 |
| 8 | Es geht langsam aufwärts — aber von allein geht es nicht. | Seite 6 · B2 |

标签分布：Seite 2 ×2、Seite 3 ×1、Seite 4 ×2、Seite 5 ×1、Seite 6 ×2，与核心一致。金句西文翻译（8 句）：1 `Cuatro noches de fútbol seguidas y luego todo un fin de semana de liga.`；2 `El impuesto sobre la energía de la gasolina y el diésel baja 14,04 céntimos por litro.`；3 `Con 50 litros se ahorran unos 8,35 euros.`；4 `Después de las vacaciones de otoño, la escuela volvió a empezar.`；5 `Los días son cortos y las noches, largas.`；6 `Dos difíciles partidos fuera de casa para los equipos alemanes.`；7 `La economía alemana sale del estancamiento, pero aún no se sostiene sola.`；8 `Mejora lentamente, pero no mejora sola.`

## 7. 家具三方对照（本版／W43 已发 DE×ES／README #20）

W43 已发同配对 SVG 逐字胜出；凡与 #20 泛化描述冲突处，以 W43 实测为准（已记录，不再泛化改动）：

- 徽章（P1，替换核心副标题槽位）：本版 SVG 实测与 W43 de-es SVG **逐字同一元素**：字符串 `TEXTOS EN ALEMÁN · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`，y=372，20pt，粗体，BRICK #a4553a，居中 x=975。**注意偏差**：README #20 泛化描述为 19.5pt，W43 已发实测为 20pt；按任务规则 W43 胜出，本版用 20pt，未按泛化描述改动。
- 页脚（每页 y=2624，8/8 齐全）：`Die Lucerna · SEMANARIO ALEMÁN VOL.2 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL` ＋ `Página {n} de 8`；VOL 号随核心（W43 为 VOL.1，本版 VOL.2，属预期差异）。
- 版头行（P1 y=330，46pt serif 粗体）：`SEMANARIO ALEMÁN · VOL.2 · FÚTBOL · GASOLINA · CUIDADOS`；顶条中行：`WÖCHENTLICH AUF DEUTSCH · CADA SEMANA · EL ALEMÁN QUE LEEN LOS ALEMANES`（W43 原文）。
- masthead：核心的 `Die Lucerna`，8 页均有（P1 花体字标＋各页版头右行）。
- gloss 前缀：`Nota — `（W43 同款）；P8 分隔符：`— Página {N} —`（W43 同款）；P8 括号：半角（W43 同款）。
- 章节／栏目标题（德语头＋西文副标题，W43 同款优先）：LEBEN · Vida cotidiana；KULTUR · Cultura；SPORT · Deportes；JUGEND · Jóvenes；VERTIEFUNG · A fondo；SPRACHE · Lengua；ÜBUNGEN & ANTWORTEN · Ejercicios y respuestas；DIE TOPMELDUNG · El titular；JETZT ÜBEN · Practica ahora；KURZ & GUT · Breves；BLITZQUIZ · Quiz relámpago；SÄTZE DER WOCHE · Frases de la semana；FEHLERKLINIK · Clínica de errores；BEISPIELE · Ejemplos；DER WERKZEUGKASTEN · Útiles；NOCH EIN WORT · Una palabra más；IN DER NÄCHSTEN AUSGABE · Próximo número (VOL.3)；P7 栏目标签 `Seite N · 级别` 保持德语（W43 实测）。
- 题型名映射：完成句子→`completar`；单选→`opción múltiple`；句型转换→`transformación`；判断对错→`verdadero/falso`；造句→`formar frases`；词汇配对→`emparejar`；完形填空→`texto con huecos`；翻译→`traducción`；对话补全→`completar el diálogo`；写作→`redacción`。指令词：填空→`Completa`；改写→`Reescribe`；判断→`¿Verdadero o falso?`；造句→`Forma la frase`；把词和释义配对→`Une las parejas`；P8 E 指令：`Traduce al español`／`Traduce al alemán`。
- P1 深色带右行：`Semana de fútbol` ／ `Champions, Europa League y Bundesliga · página 4`（实测左德语副标题止于 1131，右行起于 1345 以上，无碰撞）。

## 8. 读者园地（P7，强制项）与构建员决定说明

P7 读者栏（标题 `LESERBRIEFE · Tus cartas`）同时含三事实＋一句显性公开征集真实来信的邀请（西文），内容预告栏与他页 UND SIE 投稿提示未被计入征集：

- 征集句原文（须原样引用）：`Ejemplo de la redacción, no una carta real: hasta el cierre, sin cartas reales ni mejores textos de la página 8. ¡Envíanos tu carta real para VOL.3!`
- 三事实核对：① 示例标注为编辑部示例（标签 `¡Un ejemplo de la redacción!`）；② 截至截稿无真实来信（`sin cartas reales`）；③ 无 P8 最佳习作且顺延 VOL.3（`sin … mejores textos de la página 8`＋`para VOL.3`）；④ 显性征集句：`¡Envíanos tu carta real para VOL.3!`。
- 德语 defer 句、示例引言、邀请句保持原样未动；示例须标注为编辑部示例——已用西文标签标注。
- **构建员决定（留待独立校对裁定，非用户指令）**：读者栏标签西文化（`¡Un ejemplo de la redacción!` 替代核心德语标签）。理由：标签属讲解层家具，西文读者须能看懂“编辑部示例”标注；德语示例引言本身未动。

## 9. 编号与级别

- 150 题连续编号，分页 10/18/18/18/18/18/12/38（与核心一致，构建日志 per-page 累计 10/28/46/64/82/100/112/150）。
- 级别徽章逐项保留，未重定级：**A2 66／B1 70／B2 14**（静态展开核验：ex() 调用＋match_set 左项展开＋content8 cloze/ddefs/writing；DE 核心 B2 仅 14 属实，如实记录）。

## 10. PDF 产物

| 文件 | 页数 | 字节 | SHA-256 |
|---|---|---|---|
| Die-Lucerna-VOL2-ES.pdf（印刷） | 8 | 4,143,274 | `881865d1f2e35dca62d5e9c0219ad893a531938196057dfaf73eb1240a7195ae` |
| Die-Lucerna-VOL2-ES-web.pdf（网页） | 8 | 4,164,613 | `92e581e3bfc8b7127710c2d0e3ed151ee225b3b54d71e2e7d4a776668a88cef4` |

网页 PDF 4,164,613 字节 ＜ 10 MB。印刷 PDF 幅面 1462.5×2025 pt，网页 PDF 幅面 1400×1938 pt。命名遵循 W45 DE×EN 兄弟版先例（`Die-Lucerna-VOL2-EN.pdf`），此为构建员采纳的先例而非任务明文。

## 11. 目视复核（8 张卡面全部）

- P1：徽章／版头行／深色带／Zahlen 框／Fragen 框／sommaire 框／照片／KURZ 框／quiz／页脚——干净。
- P2：右栏 4 盒与 Rechnen 框——干净；**注意**：box4 终点 1550.66 距 Rechnen 金线（1554）仅约 3.3px clearance，虽已 clearance 但如实标注，目视确认无压线。
- P3/P5：右栏——干净；P3 TIPP 框与练习区金线间有明确空隙。
- P4：赛程表首行与右栏底——干净；UND SIE 框底距赛程标题余 20.75px。
- P6：图表标签与条形——干净；gloss 框在 Pro & Contra 框之上，无遮盖。
- P7：读者栏／金句标签／纠错诊所——干净；金句 7 标签脱离诊所金线。
- P8：答案区末行与页脚——干净；keys 末行距页脚余量充足。
- 目视未发现缺陷；未以 audit 通过代替目视。

## 12. 自修复清单

1. transform 前缀碰撞修复（首轮残留 10 处 CJK＋2 处无 CJK 静默 mangling，逐项修复并断言）：通用短串先于整句命中，如“时间状语，动词第二位” mangling “数量时间状语…”、“一周双赛” mangling P4 gloss、“选出正确答案。” mangling 各版 bridge、“走出停滞” mangling P7 金句 7；P4 配对注文 `Englische Woche=la semana inglesa a`、P6 注文 `68% familiares que cuidan`。修复后 bslib4.py＋5 个 content 文件残留 CJK 行数为 0；svglib.py 未动（其内仅一处既有中文注释，在未用 helper 的 docstring 中，不渲染；W43 构建亦保留）。
2. P6 gloss 溢出修复：西文 gloss 6 行 vs 核心 5 行，gloss 盒会被后绘的 Pro & Contra 盒遮盖；gloss 改为 V2（`die Pflegeversicherung = el seguro`，`der Pflegedienst = el servicio de cuidados`，其余不变），回落 5 行；P6-main 终点 1054，与核心 KIT 记载一致。
3. P7 右栏超长修复：工具箱 3 项缩短各省 1 行（`rund 8,35 Euro = unos 8,35 euros`；`Meiner Meinung nach = en mi opinión`；`Es ist fraglich, ob... = no está claro`）＋读者注文换 4 行版；栏底 1622 → 1477.5，距金线（1508）30.5px。
4. P8 答案区溢出修复：沿用 W43 DE×ES 机制（核心 14.5/1.3 → W43 的 13/1.26）再进一步降至 **12pt／lh 1.22／gap 8**（W45 注文更长，含两条约 110 字符的 ARD 署名注文）；keys 终点 3150 → 2113。此为 W43 机制的延伸，留待独立校对裁定。
5. P1 headline 溢出修复（西文版特有真缺陷，非核心同款）：桥接句缩短为 `Notas — Englische Woche = semana inglesa · Spieltag = jornada · empfangen = recibir en casa · Bundesliga = la Bundesliga.`（4→3 行）；Zahlen 括号缩短（`(9 partidos en la jornada 9)`、`(6 equipos alemanes en Europa)`、`(14,04 céntimos menos por litro)`，合计省约 2 行）；headline 终点降至 1555，零溢出。
6. P2/P3/P4 右栏压线修复（与核心曾修的 P3 TIPP 缺陷同类）：P2 UND SIE 换 2 行版（`¿Conduces? ¿Cuánto cuesta el litro en tu país? ¡Escribe dos frases en alemán!`）；P3 UND SIE 换 2 行版（`¿Lees más en otoño que en verano? ¿Qué libro tienes en la mesilla?`，祈使句省略因上方德语原文已明示）；P4 UND SIE 换 2 行版（`¿A quién apoyas? ¿Quién gana el sábado el partido destacado? ¡Escribe dos frases!`）。P5 col3 终点 1446.07（练习金线 1488）、P6 col3 终点 1320.33（图表金线 1408），均无需改动。
7. occlusion 22 项标题／标签修复：见 §4 逐项清单（措辞修正，不动几何参数；墨宽实测通过）。
8. P7 标签西文化决定：见 §8（留待独立校对裁定）。

## 13. 待独立校对事项（构建员不擅自定论）

- P8 字号 12pt（W43 机制的延伸）与 P7 读者标签西文化两项构建员决定。
- P2 box4 终点距 Rechnen 金线仅约 3.3px clearance（已 clearance，目视通过）。
- P7 金句 7 译文取舍：保留“alemana”（主语精确）与核心主张，省去“lentamente”（该 nuance 由相邻金句 8 的“lentamente”承载）。
