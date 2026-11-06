# WEEKLY-KIT — Le Lucerna VOL.3 · FR × IT (W45)

**状态：builder-complete，NOT finalized。** 定稿由独立校对决定；本构建员不宣布上架、不投递 Discord、不入 GitHub 仓、不往主聊天发卡片/PDF。

## 1. 身份

- 配对：目标语 **法语（Francese）** × 读者母语 **意大利语（Italiano）**，全称见每页页脚。
- 刊头：`Le Lucerna`（法语专属冠词 Le）。期号：VOL.3 · N. 3。
- 刊期：2026 年 11 月 2 日（周一）至 11 月 8 日（周日），即 W45。
- 页数：8 页（4 的倍数）。目标语正文逐字冻结，讲解层全部为意大利语。

## 2. 计数（与核心逐项相等，登记表实测）

- 习题总数：**150**，编号 1–150 连续。
- 页分布：**10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P1–P8；注意 P2=15、P5=17、P8=42，为 FR 串）。
- 级别：A2 53 · B1 75 · B2 22。
- 题型（意大利语登记标签 = 核心题型）：Completamento 49 · Scelta multipla 26 · Abbinamento 21 · Completamento testo 8 · Trasformazione 7 · Lettura dati 6 · Vero/Falso 5 · Comprensione 5 · Traduzione 5 · Completamento dialogo 5 · Esercizio guidato 8 · Correzione errori 4 · Scrittura 1。
- 范文：P8 MODÈLE 框范文逐字 = 核心，**86 词**（80–100 要求内），正文行与核心行逐行相同（仅刊头行改为双语 `MODÈLE · MODELLO`）。
- 主题（核心实测）：决赛周末（Rolex Paris Masters，Nanterre，11 月 2–8 日；Peur sur le Parc，Plailly，末场夜场 11 月 7 日 19:00–01:00；Le Goût du Large，Port-en-Bessin，11 月 7–8 日，第 22 届）；11 月 2 日周一全法同步开学（无分区错峰）；冬令时第二周（法国 10 月 25 日切换，首周为 W44 内容）；万圣节 10 月 31 日、诸圣节 11 月 1 日、亡灵节 11 月 2 日为刚过去的报道；Pitchfork Paris 第 15 届，11 月 2–8 日；国民议会 2027 预算周按使命审议（11 月 3 日文化/媒体、4 日农业、5 日凝聚力/研究、6 日公共财政/经济；10 月 23 日社保收入部分 115–1 否决，参议院自 11 月 9 日起；日程明确标注为预定，无结果、无民调编造）。

## 3. 冻结门禁（freeze 8/8 + 源码字面级）

- 核心构建树未修改：`tools/freeze.py baseline` 对未改动核心构建复现 8 页 SVG 字节一致（p1 f02e628e…、p2 b192c192…、p3 5f332e9f…、p4 240f379d…、p5 a4d64e3e…、p6 47e4346d…、p7 e997123f…、p8 822dbe3d…，全值见 §15 注；复现后核心 SVG 重哈希无变化）。
- 本版交付 SVG 与核心 SVG 的文本节点对照：新增汉字字符 **8 页均为 0**（`freeze.py diff` 全页 added CJK = 0）；全 8 页渲染文本汉字 0、全角括号 0。
- 源码字面级法语冻结证明：核心 content 源码中不含汉字的字面，仅 6 个未出现在分版源码中，且全部有据（与 FR×DE 完全相同的 6 项）：① P8 E1 题干（改向为意大利语题干，法语句本身保留在新题干内，见 §6）；② P8 注释 `s'intéresser aux（à+les）` 全角括号改为半角 `(à + les)`；③④ 全角括号字面 `（` `）` 同上；⑤ 字典键 `type`（P8 注释规则改用 PRINT_NOTES 显式集合，见 §6，非印刷文本）；⑥ 核心输出路径字面（构建路径，非内容）。
- 节点级差异为重排假象：P1 headline 字号 24pt（核心 25pt）导致换行不同，单词集合不变；P4 À VOUS 桥接句尾 `giusta.` 溢至第 2 栏顶（y=220.5），与 FR×DE 的 `Sie die richtige Antwort.` 同坐标同结构（桥接句跨栏换行，家族行为，非缺陷）；P8 差异为重排 + 改向 E 项，由双门 P8 证明（§4）。

## 4. P8 双门（FR 族专属，BINDING）

- 门 ① plain `tools/p8.py compare`（显式 `--core-p8` / `--edition-p8`，`--total 150`；工具版本 sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`）：核心 noted **97**，分版 noted **97**，状态 **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]。
- 门 ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（复用 p8.py extract --json 输出，`--total 150`）：两侧各 150 键，mismatch **仅 [135, 150]**，两项在两侧均为 noted 项且均为已备案改向（§6），**裸键 mismatch 0**。
- 通过条件满足：plain ∈ {CLEAN} 且零裸键 mismatch。plain 不单用（其对裸键盲区已知）。
- 核心 noted 基线独立核对：核心渲染 `p8.py extract --json` 得 noted 97 个，编号 [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109–150]；裸键补集 53 个与任务清单一致。
- P8 注释语言纯度：全 8 页重扫，汉字 0、全角括号 0；德语跨族残留词（Schulbeginn / Jakobsmuschel / Nachtveranstaltung / Übersetzen Sie 等 12 个探针）0 命中；P8 注释全部为意大利语（法语原文、键与术语引用除外）。

## 5. 几何门禁

- canonical `tools/occlusion_audit.py`：自检 6 类 planted 全部命中、干净对照静默；**分版 0 flags，核心 0 flags，NEW vs 核心 0**（round-2）。
- 补充扫描（`hidden_files/weekly-report-w45-fr-it-build/scans.py`，venv PIL）：
  - 全页右缘扫描（ADVANCE 法，限 1885）：3 项超限，全部为核心同文法语行（P8 F 配对右侧行 b/d/e，最大 x1=1899.5，仍在内框线 1910 以内；y 坐标因 P8 重排而变，文本与 x1 与核心同值）——冻结法语重排继承，非分版缺陷。
  - 全页框线扫描：**0 命中**。
  - 同基线行检查（P1 顶栏 y=92、徽记 y=574、各页页脚 y=2624）：**0 重叠**。
  - P6 图表标签基线锚定墨迹覆盖（getmetrics 法，禁用 getbbox）：**0.0%**（<30% 通过；图表为文字表，框线在文字之前绘制）。
  - 行首检查：4 项行首 `:`，全部与核心同页同坐标同文本逐字节相同（冻结法语换行所致；P4 一项的窗口邻节点为栏头，属窗口重叠非新增）；**意大利语自有行首违规 0**。
- 流末端（基线 y，页内限；核心对照值均为同口径实测）：
  - P1 headline 栏 1537（限 1812；核心 1588）；P1 hiver 栏 2298（核心同值，距 quiz 规则线 2312 仅 14px，继承）；P1 quiz 2521（限 2540；核心同值）。
  - P2 feature 606，习题 2365；ET VOUS 框底回归核心值（round-2 审计 0 旗，见 §13 round-1 (c)）。
  - P3 正文 813；P4 正文 1174，微习题 2154；P5 正文第 2 栏溢至第 3 栏顶部（核心填充模式，非缺陷）。
  - P6 深读 1019，习题 2557（核心继承值，距页脚规则线 2580 有 23px），观点栏 1255（距图表顶 1330 有 75px），微习题 2020。
  - P7：A2 954，B1 1053，B2 988，工具箱 1008（核心 949，意大利桥接句较长，限内），短语栏 1574（限 1830；核心 1449），诊所 2140（限 2268）；**预告末基线 2494，墨迹底约 2499 < 2540**。
  - P8 三口径（§17 详述）：battery 流光标 1487（名义限 1485，+2；核心 1410）/ battery 末墨迹基线 1446.4、墨迹底约 1451.6，距写作条规则线 1486 有 34.4px；keys 流光标 2204（限 2545；核心 2167）/ keys 最大基线 2542.96（核心 2539.19，+3.77）/ 墨迹底 2548.1（核心 2544.4，+3.7），距页脚规则线 2580 有 31.9px，FOOTER 0 旗——按 fr-de 前例 adjudicate 通过（2540 不是 canonical 审计限值；中间栏填满至底为流式结构使然，核心亦然）。

## 6. P8 改向与显式注释集（W43 先例方法）

- 注释规则：意大利语注释长于核心 ≤10 字规则，改用显式 `PRINT_NOTES` 集合（与 W43 同配对版同法）；全角括号一律改为半角。
- 仅翻译项改向（逐项从印刷行核实，非照抄他版）：E1（#135）翻转为法→意——题干 `Traduci in italiano: « Lire un programme, c'est déjà comprendre la France. »`，键 `Leggere un programma è già capire la Francia.`，注释 `lire un programme = leggere un programma`。E2–E5 题干改为意大利语，法语键不变（#136 `Traduci in francese: Corre più veloce di suo fratello.`；#137 `Gli studenti sono in vacanza dal 17 ottobre.`；#138 `Stasera prepariamo le cartelle.`；#139 `Non si conoscono ancora i finalisti.`）。写作项（#150）键 → `Domanda aperta — i punti sono nel riquadro di scrittura e il modello è nel riquadro MODÈLE di questa pagina`，注释 `si valuta in base ai punti`（W43 FR×IT 同式）。P8 意大利语写作说明追加 `I migliori testi appariranno nel VOL.4 (pagina 7, « Le courrier des lecteurs »).`
- Q120 核对：题干 `Si j'étais libre dimanche, j'___ à Nanterre.`，选项 A. irai / B. irais / C. vais，键 B 不变，P8 注释同步（si + imparfait → conditionnel présent; j' è je davanti a vocale (elisione)）；Q119/Q121 不动（法语题干与键逐字 = 核心）。

## 7. gloss 分布（渲染 · 切分逐项计数，核心 = 分版；口径见注）

| 页 | gloss() 项 | Nota 项（去前缀后切分） | 词表项 |
|---|---|---|---|
| P1 | 7 | 0 | 0 |
| P2 | 6 | 3 | 0 |
| P3 | 6 | 0 | 10 |
| P4 | 7 | 3 | 8 |
| P5 | 6 | 0 | 8 |
| P6 | 6 | 3 | 0 |
| P7 | 0 | 0 | 0 |
| P8 | 0 | 0 | 0 |
| 合计 | 38 | 9 | 26 |

（口径说明：按 tools/README #21，gloss() 调用串按 `·` 本身切分（非 ` · `），逐项核对渲染存活；Nota 类桥接串先去前缀 `Nota — ` 再切分（否则 P2/P4/P6 各多计 1 项假象）；词表项为 mots/mots4/mots5 列表长度。本版 gloss_count.py 为构建树内副本，已扩展 `Nota — ` 前缀识别——tools/ 本体未动。核心对照：gloss 38（7/6/6/7/6/6）+ Nota 桥接 9 + 词表 26，三项与分版逐页相等。）

## 8. P7（词框、金句、读者角）

- 词框目标语定义句逐字冻结，仅 gloss 行本地化（源码字面级检查：content7 非汉字字面除输出路径外 0 缺失）。
- 金句 8 句均为本期正文逐字连续摘录、页签正确，联合文本计数 = 核心：
  1. `Le lundi 2 novembre, on reprend les cours.`（page 2，×5）
  2. `On ne connaît pas encore les finalistes.`（page 1，×3）
  3. `Les cimetières se sont remplis de chrysanthèmes.`（page 3，×1）
  4. `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?`（page 4，P4 辩论框逐字 comparatif，×5）
  5. `Le festival se promène dans Paris.`（page 5，×1）
  6. `Ce calendrier peut encore bouger.`（page 6；P6 同步形式；P6 深读小写形与微习题键 `peut` 非引文，未动，×3）
  7. `Ce week-end, tout se joue.`（page 1，×1）
  8. `Les jeunes créateurs y rencontrent leur public, en vrai.`（page 5；Q106 改写：error `rencontre`，key `rencontrent`，×3）
- 教学栏 / 工具箱重复 #1/#2/#4/#6 为 KIT 设计，非缺陷（“2×” = 源文章 + P7 表格对）。
- 读者角（LE COURRIER DES LECTEURS · L'ANGOLO DEI LETTORI）零编造三件套：
  - 标注的编辑示例：法语示例段逐字保留 `Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)`；
  - 意大利语延期披露（逐字）：`Nota della redazione: ancora nessuna lettera vera né migliori testi (W44 non uscito); è un esempio. Nel VOL.4 i veri! Mandateci lettere e migliori testi!`——同时陈述三事实：暂无真实来信、暂无最佳 P8 作文、均延至 VOL.4（法语披露句 `Note de la rédaction : aucun texte du VOL.2…` 亦逐字保留）；
  - 明确的公开征集祈使句（逐字，字面同时覆盖来信与最佳 P8 文本）：`Mandateci lettere e migliori testi!`
  - 范围裁定：征集句字面覆盖读者自己的文本（来信与最佳作文）；同页披露句把真实文本延期至 VOL.4，P8 写作条把最佳文本指向 VOL.4 第 7 页，预告点名 `Et vos lettres, enfin !` / `e le vostre lettere!`——组合满足来信与最佳 P8 作文两项，VOL.4 必须兑现。
- 预告（LA SEMAINE PROCHAINE · LA PROSSIMA SETTIMANA · VOL.4）：法语 `Lundi 9 novembre : le Sénat examine le budget de la Sécurité sociale. Mercredi 11 novembre : l'Armistice, un jour de mémoire. Samedi 14 et dimanche 15 novembre : la Foire aux harengs et à la coquille Saint-Jacques, à Dieppe. Et vos lettres, enfin !`；意大利语 `La prossima settimana: Senato e bilancio sociale, 11 novembre Armistizio, 14–15 novembre fiera di Dieppe — e le vostre lettere!`

## 9. FR 族已裁定事实（执行结果）

- P4：`41e édition en 2026 (40e anniversaire)`（1986=第 1 届 → 2025=第 40 届、2026=第 41 届 + 40 周年；与 FR×DE 裁定一致）。全版文本节点 grep：`40e` 仅此一处（P4 数字框，1473, 278，与核心逐字节同坐标同文本）；生日语境即此句本身，编号 `40.` / `140–144.`（习题号）、他版 `22e` / `15e` 一律保留未动；无任何版次宣称被改写（核心已为正确 41e 形，无需改动）。
- P7 #4 保留 P4 辩论框逐字 comparatif；#8 用 P5 逐字句 + Q106 改写。
- P6 同步为 `Ce calendrier peut encore bouger.`。
- Q120：见 §6。Q119/Q121 不动。

## 10. 家具三方对照（W43 同配对版 优先于 README #20 泛化）

- 徽记：(975, 574)，22pt BRICK（#a4553a），居中，与 W43 字符串逐字相同：`TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`。README #20 的 (975, 574) 22pt 描述的是法语作目标时的情形，与本版一致，无冲突。
- P1 顶栏（y=92 三段）：左 `VOL. 3 · N. 3`（W43：VOL. 2 · N. 2）；中 `HEBDOMADAIRE EN FRANÇAIS · OGNI SETTIMANA · IL FRANCESE CHE LEGGONO I FRANCESI`（与 W43 相同）；右 `SEMAINE DU 2 AU 8 NOVEMBRE 2026`（W43：19–25 OCTOBRE 2026）。
- 刊名 262（178pt）、副标题 330（46pt）`SETTIMANALE IN FRANCESE · VOL.3 · WEEKEND DELLE FINALI`（W43：VOL.2 · AUTUNNO E FESTE；实测宽 1498.5px，适配）、标语 372 法语原文与 W43 相同、暗带 478/522（法语头条为本周内容，意大利语右侧为本周短语：`LUNEDÌ SI TORNA A SCUOLA · TUTTA LA FRANCIA` / `INIZIANO IL MASTERS E IL FESTIVAL · VEDI PAGINA 2`）、规则线与暗带几何与 W43 相同。
- 页脚（每页，y=2624）：`Le Lucerna · SETTIMANALE FRANCESE VOL.3 · TESTI IN FRANCESE · SPIEGAZIONI IN ITALIANO` + `Pagina N di 8`（W43 模板，VOL 号更新）。
- 短双语栏头（与 W43 同）：TOCCA A TE、LESSICO、IL DIBATTITO、ALLENAMENTO、LIVELLO BASE / INTERMEDIO / SFIDA、STRUMENTI、CLINICA、IL MESE、SOMMARIO、L'ANGOLO DEI LETTORI、LA PROSSIMA SETTIMANA；说明词 Abbina / Completa / Riscrivi / Correggi；gloss 前缀 `Nota — `；P8 分隔 `— PAGINA {n} —`；P8 栏头 COMPLETA / OPZIONI / LETTURA / COSTRUISCI FRASI / TRADUZIONE / VOCABOLARIO / DIALOGO / SCRITTURA / MODELLO；keys 头 `RÉPONSES · TUTTE LE RISPOSTE CON NOTE (PAGINE 1–8)`。

## 11. 图片（仅明确公有领域，credit 取 Commons API Artist 字段原文；payload = 核心）

| 页 | 图 | 放置（x, y, w×h） | credit（与核心逐字相同） | payload 哈希（与核心逐字节相等） |
|---|---|---|---|---|
| P1 | atget-paris.jpg | 65, 1874, 896×320 | Eugène Atget (1857-1927), photographie, domaine public | base64 文本 sha256 `ff20bc2b…a8e5d`；解码 JPEG sha256 `f3705af2…595f`，334674 字节 |
| P2 | hiroshige-maple.jpg | 1451, 200, 434×480 | Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA | base64 文本 sha256 `6918cb8b…664ae`；解码 JPEG sha256 `5b772fac…0ee2`，646242 字节 |
| P3 | chrysanthemum-blanco.jpg | 1451, 200, 434×540 | Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public | base64 文本 sha256 `bfaadf5b…eca9`；解码 JPEG sha256 `be071fda…d0c94`，142340 字节 |

（完整哈希：P1 base64 `ff20bc2bd2654cdc075f7e09bcb5a96622650c7cb5921fe07384703067fa8e5d` / JPEG `f3705af28f175ce48d8abad95944accb7aacc45d6a8a50c47b24af5c5144595f`；P2 base64 `6918cb8bbe4b4bec2d6dd9bafb1636901ed2a46f9df8e49566749e404d1664ae` / JPEG `5b772facb5db886c18fa96c05b9c8fb1a459eaaff931a4a8c121896edf970ee2`；P3 base64 `bfaadf5b6b912416f770c1bf579c3467e47c662efd130b5656292bb86171eca9` / JPEG `be071fdae81a71b48d76383bd33147371968f44e37eef4312102d52dea6d0c94`。三张图均已核实确已放置，解码字节数与资产文件一致。）

## 12. W43 偏差清单（预期偏差，仅此清单）

1. VOL.3 vs VOL.2、刊期 11 月 2–8 日 vs 10 月 19–25 日、副标题主题 WEEKEND DELLE FINALI vs AUTUNNO E FESTE、暗带右侧本周短语（均为刊期内容更新）。
2. P8 答案字号 14.5pt vs W43/核心 15.5pt（意大利语注释更长，答案流适配）。
3. P8 battery 段字号 20pt vs 核心 21pt（cloze/阅读/对话三段），battery 习题间距 6 vs 11，F 配对间距 6 vs 14（同上）。
4. P1 头条段字号 24pt/行高 1.45 vs 核心 25pt/1.52（gloss 增长适配；法语文本字节不变，仅呈现）。
5. P1 gloss 缩短为单字 gloss（框几何适配）。
6. P2 ET VOUS 意大利语段缩短为 2 行定稿 `Lunedì mattina: dove eravate, quale libro? Due frasi alla redazione!`（框底回归核心值）。
7. P2 日期栏右注缩短为 `lundi 2 novembre · il 1° si dice le premier`（右栏几何适配；核心规则信息保留于练习）。
8. P1 LES DATES 栏头缩短为 `LES DATES · WEEKEND FINALI`，议程栏头缩短为 `PIANO SETTIMANALE · 2–8 NOVEMBRE`（框界适配）。
9. P3 词表项缩短为 `se souvenir — ricordare`（0.8px 框界适配）。
10. P7 读者角为编辑示例 + 延期披露（继承 VOL.3 核心的诚实处理；W43 为真实来信——差异来自核心内容，非分版自选）+ 新增征集祈使句 `Mandateci lettere e migliori testi!`（SOP 门禁要求）。
11. 翻译改向方法同 W43 先例，项号不同（本版 #135/#150；W43 为 #132/#145）。
12. P7 栏头短式、P8 分隔、半角括号、PRINT_NOTES 方法与 W43 相同，无偏差。
13. 其余家具、规则线、暗带、页脚模板与 W43 逐项相同。

## 13. 工具链与可复现性

- 单源头：`hidden_files/weekly-report-w45-fr-it-build/transform.py`（358 项替换：主 339 + 修复轮 19）；每轮修复先存全量 pre-fix SHA256 基线（`pre-fix-hashes-r1.txt` round-1 前 18 项，`pre-fix-hashes-r2.txt` round-2 前 18 项），修复只进 transform.py，事后以核心源码新拷贝 + 当轮 transform.py 在自有 scratch（`hidden_files/weekly-report-w45-fr-it-replay/`）重放、diff 恰为当轮改动后才提升入构建树（round-1 重放 diff 恰为 19 项修复；round-2 无渲染改动，视觉轮后文件哈希与 pre-fix-r2 全 OK）。
- 修复轮记录：
  - Round-1（round-1 渲染 + 门禁后）：P1 headline 溢出 127px → gloss 单字化 + 5 段法语头条 24pt/1.45；P1 两栏头超框 → 缩短；P2 ET VOUS 溢出 → 2 行定稿；P2 日期注过长 → 缩短；P3 词表项 0.8px 超框 → 缩短；P7 披露 4 行溢出致 COVER → 2 行定稿（仍含三事实 + 征集句）；P7 预告 3 行 → 2 行；P8 battery 41px 超 + keys 60px 超 → battery 段 20pt + 间距 6 + keys 14.5pt（wy 1500 未动，后验证无需移动）。
  - Round-2（round-2 渲染 + 全部门禁 + 8 卡目视）：0 渲染改动。目视发现仅 P4 `giusta.` 跨栏换行，与 FR×DE 同坐标同结构，裁定为家族行为非缺陷；P8 三口径按 fr-de 前例 adjudicate 通过（§5/§17）。
- 渲染：`run.py` 单进程 driver（content12 → content34 → content56 → content7 → content8，共享 bslib4 登记）；`render.py` 卡片 PNG @1950（cairosvg）、印刷 PDF（svg2pdf + pypdf）、网络 PDF（整卡 JPEG quality 72，核心配方；临时 JPEG 留构建树内，事后删除）。
- 解释器与 PIL（协调员工具链裁决用）：run.py 与 render.py 均用 `tools/venv/bin/python`，Python 3.12.3，Pillow 13.0.0；审计测量同 venv PIL。系统 python3（同为 3.12.3，Pillow 10.2.0）无 cairosvg，故 render.py 必须用 venv。家族基线字节复现：核心构建树经 freeze baseline 8/8 复现核心 SVG（venv 驱动），本版构建沿用同一驱动模式。
- 确定性证明：round-2 交付文件哈希与 pre-fix-r2 基线全 OK（KIT-only 写作后无渲染改动）；核心构建树与 W43 目录未改动（核心 SVG 复现前后哈希一致）；未碰 weekly-git、未建 cron、未发 Discord、未往主聊天发卡片/PDF。

## 14. 交付文件

- `svg/` ×8，`cards/` ×8（1950×2700），`Le-Lucerna-VOL3-IT.pdf`（印刷）9,745,168 字节，sha256 `f52d0d40c65391048ebd99c83bbc508c3dc3125b0745fee240d9c33abde5d832`；`Le-Lucerna-VOL3-IT-web.pdf`（网络）5,035,714 字节，sha256 `ea4a3a66265e7af0d22a7ba92d8d429570cf3e913f6b1b4c13511bf14bffd002`。
- `WEEKLY-KIT.md`（本文件），`ABSTRACT.txt`（意大利语单行，无 ASCII 双引号）。

## 15. 终版哈希（round-2 交付 = 最终）

```
Le-Lucerna-VOL3-IT.pdf       f52d0d40c65391048ebd99c83bbc508c3dc3125b0745fee240d9c33abde5d832
Le-Lucerna-VOL3-IT-web.pdf   ea4a3a66265e7af0d22a7ba92d8d429570cf3e913f6b1b4c13511bf14bffd002
svg/p1-une.svg               96f28e712d0925ab64d67b8ce2ac822f52c20088b2d4abacb150358c5c3393b3
svg/p2-vie.svg               1abec10f1636bcbd2ff3a66b2f47b183aed28480f2651233cab1a92158df64c9
svg/p3-culture.svg           f92f126a9a407006ef7086956c2ef465cffba2089e7121a78c0e8a8f343becd3
svg/p4-sport.svg             e9d6dd8dd7fdf8510bd38bc8e3cc3e49a1872ce06ff73db89c0b6469fae8f22e
svg/p5-jeunesse.svg          73dc4d2e70e084f8ee133306c04e693f925548e9a69984fc2d145ac873419f72
svg/p6-politique.svg         361df90209facd141f6e1edda4819b63bc2edcfb8a491d6d2bb1b5c430cf349c
svg/p7-langue.svg            967acd160d3038e9c6e667cc18f5e5b21ecd810e279669ca58df2d40c556d0de
svg/p8-exercices.svg         b790159675375f739ab9da9c77325d31f13dfb416dc95624e8b12aea06f5c6fb
cards/p1-une.png             04de20a4d5a62265e4946df458c8844da62d06c594e84d14d7b8b7736d3a3d65
cards/p2-vie.png             6d4742d9c57e653870ef4b9b2708ceb605cf1cc32d5531b5bb27341fb35a868f
cards/p3-culture.png         db7bafc7d9c1f3ecd61e3f33eb913e26a5637ad28b830c81f1b271a5f8e25bcf
cards/p4-sport.png           9d9813b85ffaabee038d9704fbde199d5c3533effca76dc128c2c3892f05e3b0
cards/p5-jeunesse.png        2a32d3296c2eab96e18b1ab3ae45c7f5ed61bcce6776c5e74770b1c739845026
cards/p6-politique.png       2352a5bc829699621f8e53b362dde1f3f1c4ac05f548c451ad7796490035c8bd
cards/p7-langue.png          f3b822419bea020a09e0476b4244cdd035bfb0499b4690de184e94932ab0f084
cards/p8-exercices.png       f3ee27f603933baf1cdf4aa734a4d44d9242e0da9a043a1c22e985a9dfe4d8af
```

## 16. ABSTRACT 原文

> Le Lucerna VOL.3, settimana dal 2 all'8 novembre 2026: settimanale in francese per lettori italiani — weekend delle finali con il Rolex Paris Masters a Nanterre, Peur sur le Parc a Plailly e Le Goût du Large a Port-en-Bessin, ritorno a scuola il 2 novembre, Halloween e Ognissanti, Pitchfork Paris e il bilancio 2027 all'Assemblea nazionale, con 150 esercizi da A2 a B2, lessico, grammatica e modello di testo. Imparare il francese leggendo notizie vere: finali, ora solare e feste francesi.

## 17. 未决观察（非阻塞，交独立校对裁定）

1. P8 keys 最大基线 2542.96 / 墨迹底 2548.1，名义限 2540 仅差 8.1px（墨迹口径）；但与核心同口径值接近（核心 2539.19 / 2544.4，仅 +3.77 / +3.7），距页脚规则线 2580 有 31.9px，遮挡审计 FOOTER 0 旗——结构使然，非分版缺陷（fr-de 前例同口径 adjudicate）。
2. P8 battery 流光标 1487（名义限 1485，+2），但末墨迹基线 1446.4、墨迹底约 1451.6，距写作条规则线 1486 有 34.4px，LINEX 0 旗——光标余量为行距尾隙，非墨迹溢出。
3. P8 F 配对右侧 3 行右缘超限（最大 1899.5）与 P3/P4/P5/P7 行首 `:` 4 项，全部为核心同文法语继承（F 行 y 坐标因 P8 重排而变，文本与 x1 与核心同值）；意大利语自有项 0。
4. P1 hiver 末 2298、P6 习题末 2557 为核心继承的紧贴值；P6 观点栏末 1255 为本版自有值（观点栏意大利语桥接句较长所致，几何合格，距图表顶 1330 有 75px），遮挡审计 0 旗。
5. P5 正文第 2 栏溢 3 个节点至第 3 栏顶部，符合核心填充模式，目视无重叠。
6. 本版未做项：独立校对、GitHub 入库、Discord 投递（投递暂停令仍有效，须主线另行决定）。
