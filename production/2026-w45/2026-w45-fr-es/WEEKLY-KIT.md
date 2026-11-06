# WEEKLY-KIT — W45 FR×ES（目标语言法语 · 读者母语西班牙语）

- 状态：**builder-complete，NOT finalized**（待独立校对 + 协调员串行上架；不上架、不发 Discord、不入 GitHub 仓）。
- 刊名：Le Lucerna（Le 仅法语）；VOL.3；刊期 2026 年 11 月 2–8 日；8 页。
- 配对全称：目标语言法语（fr），读者母语西班牙语（es）。徽记、页脚、讲解层全部西班牙语；法语目标文本逐字节冻结。
- 交付目录：`files/weekly-report-w45-fr-es/`；build 树：`hidden_files/weekly-report-w45-fr-es-build/`（transform.py 单源头，359 项）。

## 1. 计数（登记表 REG 实测，scratch 重放 `scratch/regdump/dump.py`）

- 总题 150；页分布 **10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P1–P8；P2=15、P5=17、P8=42，通用串 10/18/18/18/18/18/12/38 对 FR 是错的）。
- 级别：**A2 53 / B1 75 / B2 22**。
- 题型分布（西班牙语登记标签，合计 150）：Completar 49、Opción múltiple 26、Reescribir 7、Emparejar 21、Verdadero/Falso 5、Leer gráfico 6、Practicar 8、Corregir 4、Completar texto 8、Comprensión 5、Traducir 5、Completar diálogo 5、Escribir 1。
- 范文（P8 MODÈLE，空格切分）**86 词**。
- gloss 38（7/6/6/7/6/6，P1–P6；P7–P8 为 0）+ 词表 26（P3 10 / P4 8 / P5 8）+ Nota 类 9（P2 3 / P4 3 / P6 3）。见 §6 口径。

## 2. 本期事实（全部取自核心实测，只用于 ABSTRACT 与 KIT 叙述）

- 决赛周末：Rolex Paris Masters（Nanterre，11 月 2–8 日）；Peur sur le Parc（Plailly，末场夜场 11 月 7 日 19:00–01:00）；Le Goût du Large（Port-en-Bessin，11 月 7–8 日，第 22 届）。
- 11 月 2 日周一全法同步开学；Pitchfork Paris 第 15 届（11 月 2–8 日）；国民议会 2027 预算周按使命审议（11 月 3 日文化/媒体、4 日农业、5 日凝聚力/研究、6 日公共财政/经济；10 月 23 日社保收入部分 115–1 否决，参议院自 11 月 9 日起；日程明确标注为预定，无结果、无民调编造）。

## 3. 冻结门禁（最终 SVG，2026-10-28）

- `tools/freeze.py diff`（最终 SVG）：8 页 added CJK 均为 0，总计 0；逐页增减串数 p1 +46/−45、p2 +37/−34、p3 +37/−34、p4 +41/−37、p5 +36/−30、p6 +30/−27、p7 +43/−35、p8 +156/−138。输出：`hidden_files/weekly-report-w45-fr-es-build/freeze-diff.json`（最终版，已覆盖 r3 版）。
- 渲染 SVG 文本节点：8 页 Han 均为 0、全角括号均为 0；页脚 ES 串 8 页全 True、中文页脚全 False；“桥接”一词不出报（False）。
- 核心未改动证明：开工前 `core-prebuild.sha`，收尾复核 `sha256sum -c` 8/8 OK（核心 8 SVG 全未变）。
- 移除串分析（最终 diff）：
  - P1 无 CJK 移除 22 项：全部为 5 段冻结法语头条段在 24pt 下的重排碎片。源字面证明：本版 content12.py 前 5 个 f.para 字面与核心逐字节相同（仅追加字号/行高参数），故无一法语词丢失；P1-headline 流终 1537（限 1812）。
  - P3、P7 各 1 项无 CJK 移除：均为讲解层行尾标点“）。”（中文讲解段删除的残留），非法语。
  - P8 无 CJK 移除 33 项：全部为 (a) 电池段 20pt 重排碎片、(b) 答案流 14.5pt 重排碎片、(c) E 区改向项（#135 题干翻转 + 注记语言更换）。单项证明见 §4（全 150 键核对，裸键错配 0）。
  - 其余移除串全部含 CJK（中文讲解层替换），非法语。
- 源码字面审计（AST 常量，核心 build 树 vs 本版 build 树）：content12/34/56/7 无 CJK 核心字面的减少项仅为 OUT 路径前缀（非印刷内容）；content8 减少 7 项 = OUT 路径 + E1 题干（改向，法语句子保留于新西班牙语题干内）+ `s'intéresser aux（à+les）` 全角括号改半角 + 打印规则代码 token（`note` / `（` / `）` / `type`，非印刷文本）。无一法语键丢失。

## 4. P8 双门（FR 族硬性，两门缺一不可）

- (a) plain `tools/p8.py`（sha256 前缀 96fc2cfe…，当前新版；`--total 150`，显式 `--core-p8/--edition-p8`）：core noted 97，edition noted 97，状态 **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]。FR 核心 P8 只印 97 注记是设计，非缺陷。
- PRINT_NOTES 与核心 noted 集逐项相等（97 项）：[1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]；裸键补集 53 项：[2, 5, 6, 9, 12, 15, 16, 18, 20, 22–26, 29, 30, 35–41, 43, 45–52, 54, 61, 62, 64–66, 73, 75, 76, 85, 86, 88, 89, 91, 97–99, 101–104]。
- (b) `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（复用 p8.py extract --json 输出，不在 tools/ 内；`--total 150`）：两侧各 150 键，mismatch 仅 **[135, 150]**，两项在两侧均为 noted 项且均为已备案改向（见下），**裸键 mismatch 0**。plain 单用对裸键篡改是盲的（对照实验：nocturne→nocturnX 仍 CLEAN），故绝不可只用 plain。本版不照抄 fr-de/fr-en 的 [135,150] 结论，是逐项从印刷行核实的结果（恰好同号，但改向内容不同）。
- P8 改向明细（W43 先例方法）：
  - E1（#135）翻转为法→西：题干 “Traduce al español: « Lire un programme, c'est déjà comprendre la France. »”，键 “Leer un programa ya es entender Francia.”，注 “lire un programme = leer un programa”。
  - E2–E5 题干改为西班牙语（“Corre más rápido que su hermano.” / “Los alumnos están de vacaciones desde el 17 de octubre.” / “Esta noche vamos a preparar nuestras mochilas.” / “Todavía no se sabe quiénes son los finalistas.”），法语键不变。
  - 写作项（#150）键 → “Pregunta abierta — los puntos están en el recuadro de escritura y el modelo, en el recuadro MODÈLE de esta página”，注 “se puntúa según los puntos”。
  - P8 西班牙语写作说明追加最佳文本指向 VOL.4（página 7, « Le courrier des lecteurs »）。
- P8 注纯西班牙语：渲染 SVG 全页 Han 0、全角括号 0；P8 注全部为西班牙语。
- P8 栏头（W43 形）：COMPLETAR、OPCIONES、LECTURA、CONSTRUIR FRASES、TRADUCCIÓN、VOCABULARIO、DIÁLOGO；写作栏 ESCRIBIR；范文栏 MODÈLE · MODELO；分隔 “— PÁGINA n —”；注括号半角加空格 “ (note)”。

## 5. 几何门禁

- canonical `tools/occlusion_audit.py`（sha256 前缀 e1f92b42…）：**本版 0、核心 0、NEW 0**（`occlusion-r4.json`，最终版；自检 6 类 planted 各命中 1 次、干净对照静默）。round-4 前版 `occlusion.json` 曾有 4 项 NEW BOXTITLE，均已修复（见 §11）。
- 补充扫描（build 树 scans.py，venv PIL）：
  - 全页右缘 ADVANCE 扫描（限 1885）：仅 P8 F 配对右侧 3 行 b/d/e，x1 = 1891.2 / 1891.3 / 1899.5；已核实与核心同文、同 x、同 x1（核心 y 不同，只因电池流位置不同；属冻结法语继承，非本版缺陷），仍在内框线 1910 以内。
  - 全页框线扫描：0 命中；同基线行检查（P1 顶栏 y=92、徽记 y=574、各页页脚 y=2624）：0 重叠。
  - P6 图表标签基线锚定墨迹覆盖（getmetrics 法，禁用 getbbox ascender 法）：**0.0%**（<30% 通过）。
  - 门输出未截断（occlusion-r4.json 全量在 build 树）。
- 流末端（最终渲染日志 render-log-r4.txt）：P1 headline 1537（限 1812）、P1 hiver 2298（核心继承，见未决观察）、P1 quiz 2521（限 2540）；P2 feature 606、P2 习题 2365、P2 ET VOUS 框底 1538.6 = 核心值；P3 正文 813；P4 正文 1205、微习题 2154；P5 正文 337；P6 深读 1019、习题 2557（核心继承，见未决观察）、观点栏 1225、微习题 2020；P7 A2 954、B1 1053、B2 988、工具箱 979、短语栏 1574（限 1830）、诊所 2140（限 2268）。
- P8 流末端三口径同报（最终 SVG 实测）：电池流光标 1487 / 电池末基线 1446.4 / 电池墨迹底 1452.4；答案流光标（末栏）2414 / 答案最大基线 **2539.18 < 2540** / 答案墨迹底 2544.2（超名义 2540 仅 4.2px，距页脚规则线 2580 有 35.8px，且与核心同口径值逐字节相同：核心答案最大基线 2539.19、墨迹底 2544.2，属结构使然，非本版缺陷）。
- P7 预告：末基线 2494、墨迹底 2500.0 < 2540；预告暗带底 2540；读者园地框末基线 2235.825、墨迹底 2242.8 < 框底 2258（余 15.2px）。
- 目视：建造者已目视全部 8 张卡（2026-10-28）：溢出、重叠、压页脚、图片与出处、P1 徽记、P2 ET VOUS 框底、P6 图表、P7 读者园地框（披露 2 行在框内）、P8 电池/写作条/答案末端，全部干净。

## 6. 换行/孤儿与 gloss

- 换行方法：svglib.wrap() 对拉丁文本只按空格分词（源码已核：token 按空格与 CJK 字符切分，拉丁词不切词），故行中切词只可能发生在单个词超栏宽时，此时 wrap 会整词溢出右缘——由 ADVANCE 扫描捕获（仅上述 3 行继承项，均为完整法语短语，非切词）。
- 行末连字符扫描（全页文本节点以 -/‐ 结尾）：**0**。
- 行首孤儿标点扫描：4 项行首 `:`，全部与核心同页同 y 同文本逐字节相同（P3 y=789.65、P4 y=837.12、P5 y=430.65、P7 y=428.1），属冻结法语换行继承；西班牙语自有行首违规 0。
- gloss 口径（README #21）：gloss() 调用串按 `·` 本身切分，Nota 前缀先去前缀再切分，否则每页多计 1 项假象。gloss_count.py 已适配西班牙语前缀（接受 “Nota — ”并去前缀）。核心 = 本版，逐页相等：P1 gloss 7 / Nota 0 / 词表 0；P2 6/3/0；P3 6/0/10；P4 7/3/8；P5 6/0/8；P6 6/3/0；P7 0/0/0；P8 0/0/0；**合计 gloss 38、Nota 类 9、词表 26**。
- P1 gloss 单字化（round-2）：原多词 gloss 串拆为单字对，例 “se jouer decidirse · une finale final · une demi-finale semifinal · un quart de finale cuartos · une nocturne velada · un frisson emoción · la coquille Saint-Jacques vieira.”

## 7. 金句与 P7（逐字 + 页签 + 频次 = 核心）

联合文本计数（全 8 页渲染 SVG 文本节点拼接）：

| # | 金句（逐字） | 页签 | 频次 |
|---|---|---|---|
| 1 | Le lundi 2 novembre, on reprend les cours. | p2 | 5 |
| 2 | On ne connaît pas encore les finalistes. | p1 | 3 |
| 3 | Les cimetières se sont remplis de chrysanthèmes. | p3 | 1 |
| 4 | Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ? | p4 | 5 |
| 5 | Le festival se promène dans Paris. | p5 | 1 |
| 6 | Ce calendrier peut encore bouger. | p6 | 3 |
| 7 | Ce week-end, tout se joue. | p1 | 1 |
| 8 | Les jeunes créateurs y rencontrent leur public, en vrai. | p5 | 3 |

- P7 短语栏 8 句逐字出自本刊文章并带正确页签（上表页签即 P7 栏内页签）；P7 词框等目标语定义句冻结，仅 gloss 行本地化（本地化定义句是冻结失败）；P7 “2×”指原文 + P7 表格对（教学栏/工具箱重复 #1/#2/#4/#6 是 KIT 设计，非缺陷）。
- P7 词框冻结句（checks.py 验证 True）：#4 “Une finale qu'on ne connaît pas d'avance: plus excitante ou plus frustrante?”、#8 “Les jeunes créateurs y rencontrent leur public, en vrai.”、#6 “Ce calendrier peut encore bouger.”。

## 8. 读者来信角（P7 LE COURRIER DES LECTEURS · EL RINCÓN DE LOS LECTORES，零编造）

- 标注的编辑示例：法语示例段逐字保留，含 “Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)”（checks.py 验证 True）。
- 西班牙语点评：“Comentario de Xiao Mo (ejemplo): el passé composé es seguro; el punto y coma une ambos días. El próximo rincón comentará textos reales.”
- 披露（西班牙语，round-4 定稿 2 行）：“Nota de la redacción: ningún texto del VOL.2 llegó a tiempo (no hubo W44); aquí un ejemplo. El VOL.4 comentará textos reales. ¡Envíanos tu carta o tu mejor texto de la página 8!”（177 字）；法语冻结披露句同页在位（“Note de la rédaction: aucun texte du VOL.2 n'était arrivé…”）。
- 明确公开征集祈使句（逐字）：“¡Envíanos tu carta o tu mejor texto de la página 8!”——字面同时覆盖来信（carta）与最佳 P8 文本（mejor texto de la página 8）。
- 组合裁定（沿 fr-de 前例）：披露句“ningún texto del VOL.2”覆盖 VOL.2 征集的来信与 P8 作文两类（均未收到）；P8 写作条把本期最佳文本指向 VOL.4 第 7 页（即本期未刊登最佳作文）；预告行 “¡y por fin vuestras cartas!” 同向。FR 核心是 VOL.3，下期为 VOL.4，披露与征集均指向 VOL.4。
- 预告（LA SEMAINE PROCHAINE · VOL.4 LA SEMANA QUE VIENE）：法语段冻结；西班牙语 “La semana que viene: el Senado examina el presupuesto social, 11 de noviembre Día del Armisticio, 14–15 de noviembre mercado de Dieppe… ¡y por fin vuestras cartas!”

## 9. FR 族已裁定事实（核心实测，勿改写）

- 41e 形式为“41e édition en 2026 (40e anniversaire)”（P4）；40e 其余出现仅为 anniversaire 生日语境、编号 40./140–144.、他版 22e/15e、KIT 历史，均保留。核心源码中该句已是 41e 形式，本版无需改动，只冻结。
- P7 引用 #4 保留 P4 辩论框逐字 comparatif “plus excitante ou plus frustrante?”（B1 同步，key “plus excitante”）。
- #8 为 P5 逐字 “Les jeunes créateurs y rencontrent leur public, en vrai.” + Q106 错误 “rencontre”、key “rencontrent”。
- P6 同步为 “Ce calendrier peut encore bouger.”。
- Q120 题干 “Si j'étais libre dimanche, j'___ à Nanterre.”、选项 A. irai / B. irais / C. vais、key B、P8 注同步（si + imparfait → conditionnel + elision j'）；邻题 Q119/Q121 不动。

## 10. 家具三方对照（W43 fr-es 实测为准）

- 徽章（P1，y=574，22pt BRICK #a4553a，居中，坐标 (975,574)）：“TEXTOS EN FRANCÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES”（实测宽 1291.0px）。
- 页脚：左 “Le Lucerna · SEMANARIO FRANCÉS VOL.3 · TEXTO EN FRANCÉS · EXPLICACIONES EN ESPAÑOL”（VOL 号更新为 3），右 “Página N de 8”。
- P1 顶栏：左 “VOL. 3 · N.º 3”；中沿用 W43 串 “HEBDOMADAIRE EN FRANÇAIS · CADA SEMANA · EL FRANCÉS QUE LEEN LOS FRANCESES”；副标题 “SEMANARIO EN FRANCÉS · VOL.3 · FIN DE SEMANA DE FINALES”。
- gloss 前缀 “Nota — ”；P8 分隔 “— PÁGINA n —”；P8 括号半角加空格 “ (note)”；短双语栏头沿 W43 形：LÉXICO、FECHAS、EL DEBATE、A PRACTICAR、VOCABULARIO、RECURSOS、CLÍNICA、EL RINCÓN DE LOS LECTORES、LA LENGUA EN MANO、NIVEL BÁSICO/NIVEL INTERMEDIO/DESAFÍO。
- P8 栏头沿 W43 形：COMPLETAR、OPCIONES、LECTURA、CONSTRUIR FRASES、TRADUCCIÓN、VOCABULARIO、DIÁLOGO；写作栏 ESCRIBIR；范文栏 MODÈLE · MODELO。
- FR-as-target 一般形（徽章插在 y=574、22pt BRICK，fr-de/fr-en 实测均为 (975,574) 22pt #a4553a = W43）仅作参照，W43 实测为准。

## 11. 图片（payload = 核心，双口径哈希）

| 页 | 放置 (x, y, w×h) | base64 文本 sha256（前 16） | 解码 JPEG sha256（前 16） | 字节数 |
|---|---|---|---|---|
| P1 Atget | (65, 1874, 896×320) | ff20bc2bd2654cdc | f3705af28f175ce4 | 334,674 |
| P2 Hiroshige | (1451, 200, 434×480) | 6918cb8bbe4b4bec | 5b772facb5db886c | 646,242 |
| P3 Blanco | (1451, 200, 434×540) | bfaadf5b6b912416 | be071fdae81a71b4 | 142,340 |

- 三张内嵌 base64 payload 与核心 SVG 同法提取的值逐项相等（双口径均等）。
- credit 行取 Commons API Artist 原文：P1 “Eugène Atget (1857-1927), photographie, domaine public”；P2 “Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA”；P3 “Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public”。每张署名图均已放置（SVG `<image>` 元素 + 法语图说 + credit 行齐全，目视确认）。

## 12. W43 偏差清单（仅预期偏差）

VOL 号（3）、刊期（2026 年 11 月 2–8 日）、主题（本期事实见 §2）、P8 答案字号 14.5pt、写作条 wy 1540、电池间距 gap=6、P1 头条段 24pt/行高 1.45、P1 gloss 单字化、P6 栏头 FECHAS、P1 计划行 “Resultados: sábado noche y domingo.”、DANS CE NUMÉRO 栏头 “DANS CE NUMÉRO · CONTENIDO”、P5 单名 “PARIS CREATOR WEEK”、P7 披露缩短为 2 行。其余家具、栏头、页脚、徽记均沿 W43 实测形。

## 13. 修复轮与基线（transform.py 单源头；每轮 fix 前存该轮前全量 sha256 基线；build 目录永不 reset）

- Round 1（初译渲染）：150 题；问题三处：P1-headline FLOW OVERFLOW（ended 1939，bottom 1812，溢出 127px）；P6-ex HEAD TOO WIDE（“LIRE LE CALENDRIER · LEE EL CALENDARIO”）；P8-battery ended 1526（限 1485）、P8-keys ended 2625（限 2545）。基线 `pre-fix-hashes-r1.txt`。P1-hiver 2298、P6-ex 2557 为核心继承值，非缺陷。
- Round 2：P1 gloss 单字化 + 5 段冻结法语头条段改为 24pt/行高 1.45（文本字节不变）；P6 栏头改为 “LIRE LE CALENDRIER · CALENDARIO”；P8 全套 FR×DE 方案：电池段 21→20pt（3 处）、电池 ex 间距 gap=6（4 处）、F 配对 gap=6、答案流 15.5→14.5pt、写作条 wy 1500→1540。验证：scratch/replay-r2 全新核心拷贝 + 完整 transform.py 重放，diff 恰为修复轮 14 项后才提升入构建树（中途因 F 配对 instr 字面写错而断言失败一次，修正为 `instr="Une"` 后重放通过）。重渲染后：P1-headline 1537（= DE 值）、P8-battery 光标 1487、P8-keys 光标 2414；仅 P1/P6/P8 三 SVG 变化；但 P6-ex HEAD TOO WIDE 仍在（原因：head() 按 25pt 度量，CALENDARIO 版 24pt 下 430.5 但 25pt 下 448.3 > 栏宽 434）。
- Round 3：仅 P6 栏头改为 “LIRE LE CALENDRIER · FECHAS”（25pt 下 386.1 ≤ 434）。scratch/replay-r3 diff 恰为该 1 项。重渲染后：**零 FLOW OVERFLOW / HEAD TOO WIDE 警告**，150 题，仅 P6 SVG 变化；随后 render.py 生成卡片与双 PDF。
- Round 4（canonical 审计 4 项 NEW BOXTITLE 修复）：初版审计（edition 4 flags，core 0，NEW 4）四项均裁定为真缺陷（非测量伪报）：
  1. P1 计划框单行文本 “Resultados de las finales: sábado noche y domingo.”（19pt，453.2px > 可用 412px，越过内框线 1910）→ “Resultados: sábado noche y domingo.”（334.6px）。
  2. P1 “DANS CE NUMÉRO · EN ESTE NÚMERO”（24pt 粗体 456.1px > 412）→ 沿用 W43 实测形 “DANS CE NUMÉRO · CONTENIDO”（390.1px）。
  3. P5 “PARIS CREATOR WEEK · CREADORES”（23pt 粗体 418.4px，超 6.2px）→ 单名 “PARIS CREATOR WEEK”（247.0px；FR×EN round-4 前例）。
  4. P7 读者园地披露段 3 行，末行墨迹底 2265.6 超固定框底 2258.0 达 7.6px → 缩短为 2 行定稿（wrap 在 19.5pt/848px 下验证为 2 行）：“Nota de la redacción: ningún texto del VOL.2 llegó a tiempo (no hubo W44); aquí un ejemplo. El VOL.4 comentará textos reales. ¡Envíanos tu carta o tu mejor texto de la página 8!”（177 字）。
  - scratch/replay-r4 diff 恰为该 4 项后提升。重渲染后：零警告，150 题，仅 P1/P5/P7 三 SVG 变化；canonical 审计复测 **edition 0 flags、core 0 flags、NEW 0**。
  - P8 电池光标 1487（名义流底 1485）裁定为非缺陷：电池末行墨迹基线 1446.4（Merci!），距写作条规则线 1526 有 79.6px、距 MODÈLE 顶 1540 有 93.6px；此裁定已写入 transform.py round-4 注释，防止后轮误“修复”。
- 基线文件：`pre-fix-hashes-r1.txt`、`pre-fix-hashes-r2.txt`、`pre-fix-hashes-r3.txt`、`pre-fix-hashes-r4.txt`、`final-hashes.txt`、`render-log-r1.txt` 至 `render-log-r4.txt`、`core-prebuild.sha`，均在 build 树。

## 14. 工具链与可复现性

- transform.py：基础映射 340 项（bslib4 家具 3 + content12/34/56/7/8 全量中文讲解串 + TYPE_MAP/INSTR_MAP）+ 修复轮 19 项 = **359 项**。TYPE_MAP 西班牙语登记标签：完成句子=Completar、单选=Opción múltiple、句型转换=Reescribir、词汇配对=Emparejar、跟练=Practicar、改错=Corregir、完形填空=Completar texto、阅读判断=Verdadero/Falso、阅读理解=Comprensión、对话补全=Completar diálogo、翻译=Traducir、写作=Escribir、图表读数=Leer gráfico；INSTR_MAP：把词和释义配对→“Une palabra y definición”、填空→“Completa”、改写→“Reescribe”、配对→“Une”、改错→“Corrige”。P8 F 配对处的 `instr="配对"` 经 INSTR_MAP 后变为 `instr="Une"`（修复轮 replay 曾因此断言失败，已修正字面）。
- OUT 重定向：每 content 文件 1 处，把 weekly-report-w45-fr-core 换成 weekly-report-w45-fr-es；bslib4 页脚/页码行/gloss 前缀已替换。内容文件残留中文仅为源码注释（每文件 2 行章节注释）与 svglib.py 一行插画注释（“for 重阳”），均不印刷；渲染 SVG 文本节点 CJK = 0。
- run.py：从 FR×DE build 复制的单进程 driver（content12→34→56→7→8 顺序执行，共享 bslib4 登记），未改动。
- render.py：从 FR×DE 复制后改写：ED 指向本版交付目录；PDF 名 `Le-Lucerna-VOL3-ES.pdf`（print）、`Le-Lucerna-VOL3-ES-web.pdf`（web）；网页版配方改为核心代码本法：Pillow 默认质量（去掉 fr-de 复制件中的显式 quality=72；fr-en round-5 已证实 Pillow 默认 = q75，q72 与 q75 之争留待协调员工具链裁决）。
- 解释器实测（2026-10-28）：**run.py 与 render.py 均用 `tools/venv/bin/python` = Python 3.12.3 + Pillow 13.0.0**（系统 python3 同为 3.12.3 但 Pillow 10.2.0 且无 cairosvg，故 render.py 必须用 venv 版）。家族基线 SVG 字节复现：本版 SVG 与核心 SVG 的差异仅为讲解层替换 + §12/§13 所列有意布局改动（freeze diff + 源码字面审计证明）。
- 校对重跑一律在自有 scratch 内并重定向 OUT，绝不在交付/核心目录原地跑 build 树脚本（en-ko/fr-en mtime 刷新前例）。

## 15. 网页版 PDF 逐页验证（fr-en 噪声教训，2026-10-28）

- pdfinfo：web PDF 8 页；print PDF 8 页、1462.5 × 2025 pts。
- pdfimages：web PDF 每页 1 个 1950×2700 JPEG 流（baseline DCT），流字节数 p1 657K、p2 638K、p3 584K、p4 631K、p5 527K、p6 560K、p7 644K、p8 839K（pdfimages 列表值；提取流字节数 p1 673,229、p2 652,839、p3 597,984、p4 645,873、p5 539,714、p6 573,655、p7 659,185、p8 859,150）。
- pdftoppm -r 150 渲染 8 页（1950×2700）与卡片逐页比对：下采样（195×270）均值差 p1 1.511、p2 1.378、p3 1.310、p4 1.340、p5 1.216、p6 1.273、p7 1.444、p8 1.572（个位数；旧噪声版为 100 量级）；全分辨率均值 RGB 与卡片差 ≤1.2。**无红黄绿蓝块噪声页。**
- 新鲜性证明：同一配方在 scratch 重建候选 PDF（`scratch/webcheck/candidate.pdf`），提取的 8 页 JPEG 流与交付 web PDF 的流**逐字节相同**；两 PDF 文件仅差 26 字节 = 标题元数据（文件名不同所致）。直接 JPEG 与 PDF 内嵌流字节不同属正常（PDF 编码器重编码），不作缺陷。
- 注意：本版 web PDF 由交付卡片新鲜生成；FR 核心网页版 PDF 的噪声问题待父级定，与本版无关。

## 16. ABSTRACT.txt（交付目录内，西班牙语单行、无 ASCII 双引号，524 字符）

> Le Lucerna VOL.3, semana del 2 al 8 de noviembre de 2026: semanario en francés para lectores hispanohablantes — fin de semana de finales con el Rolex Paris Masters en Nanterre, Peur sur le Parc en Plailly y Le Goût du Large en Port-en-Bessin, vuelta al cole el 2 de noviembre, Halloween y Toussaint, Pitchfork Paris y el presupuesto 2027 en la Asamblea Nacional, con 150 ejercicios de A2 a B2, vocabulario, gramática y texto modelo. Aprender francés leyendo noticias reales: finales, horario de invierno y fiestas francesas.

## 17. 交付文件（最终 sha256）

| 文件 | 字节数 | sha256 |
|---|---|---|
| svg/p1-une.svg | — | 8f821595b01d90c83384078c1bddce478307dd9c86d109d6d80356fabb81f1ac |
| svg/p2-vie.svg | — | f9161ee2038aa85cb413a86cfd3c31bb82172c75e6c730efa84ef870edd018a8 |
| svg/p3-culture.svg | — | dfcd8a045c9fef451dedccab76d6fd24839a754496af46c9ad1e18e52ddf9f67 |
| svg/p4-sport.svg | — | dd58f4aca5224fe8750e8a8edd4d513da91a9d8e72ad6e29cb160ee66b |
| svg/p5-jeunesse.svg | — | 49df19bb0c934d7999f1dfc8ca458538183ced6c76e606aa07dcf89a5ee5fc6f |
| svg/p6-politique.svg | — | 9078e074730e28732f8cf347890fff0bc3dc6b1ac9bdacf43e0b24d41d63b4c2 |
| svg/p7-langue.svg | — | a3c534f01492d20e3f4c166c0393e7a0e6ec75a1f72af98013bf66be4b9eed19 |
| svg/p8-exercices.svg | — | 077a336a73422b35bf30175fa0c00ff421e9b079f64ea728e41df26dded262cc |
| cards/p1-une.png | 1,037,545 | 9f8eeb7d2ff444bad426b1a1561495b98d2fff16a0509b3eab2cef8570f11793 |
| cards/p2-vie.png | 1,184,413 | c19f00a6a4f19602efc59b11d0a04a96304d692b29b6232d0af034c3ac136dc9 |
| cards/p3-culture.png | 931,705 | 57ba27462b4adbdccb357c9d1c408310a72a29d89f428b1ac61912fac5031444 |
| cards/p4-sport.png | 843,501 | f92b6aa98c4332d481918ae200c0a8bb0d6d474acaff3e70db66bdeb229ae39f |
| cards/p5-jeunesse.png | 692,141 | 2a333c590d8f7c62977c4199e8887caa3ac44e2aaf0693bfad6c10923c8e9329 |
| cards/p6-politique.png | 740,506 | d87b4194327314e923c90ef188c9491e7f064b997d07ee489105ca8ef3b9608c |
| cards/p7-langue.png | 722,000 | 320fb2f08e8f968aa30bee405dedbae7b8f8fcf0ca6addb751667fd3cef9c732 |
| cards/p8-exercices.png | 1,019,342 | 5ddb881e2ef31cbe07a439e2318001966ce17ed50f41ad591d92858e24d5b127 |
| Le-Lucerna-VOL3-ES.pdf（print） | 9,747,438 | 973d46380e1469750499ac3a6309b172b12ac50e858ccc8929ce7cb6f2a488ca |
| Le-Lucerna-VOL3-ES-web.pdf（web） | 5,206,069 | db79fb5c1c01746ebb84a184cc611c3bdeb2e24f23e4b8c014a5ec52ee35640b |
| ABSTRACT.txt | 531 | 3ca65bb770840239c15b9211c25ae6fe6e6f33b14d9badd7cb65480e2461ee36 |
| WEEKLY-KIT.md | — | （本文件） |

## 18. 未决观察（非阻塞，交独立校对裁定）

- P8 答案墨迹底 2544.2 超名义 2540 但与核心相同且距页脚线 35.8px（见 §5）。
- P8 F 行右缘继承值（x1 至 1899.5，核心同文同值，内框线内）。
- 4 处行首 `:` 继承（核心同页同 y 同文本）。
- P1 hiver 流光标 2298 / P6 习题流光标 2557 核心继承紧贴值（流光标口径；卡片目视无压线、无溢出，P1 hiver 框与 P6 习题末行均距页脚有空隙）。
- P5 正文栏溢核心填充模式（P5-main 终栏 col 2 y=337；卡片目视干净）。
- 网页版 Pillow 默认质量与 q72/q75 之争，留待协调员工具链裁决（本版按核心代码本法用 Pillow 默认）。
