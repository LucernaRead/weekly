# WEEKLY-KIT — Le Lucerna VOL.3 · FR × DE (W45)

**状态：builder-complete，NOT finalized。** 定稿由独立校对决定；本构建员不宣布上架、不投递 Discord、不入 GitHub 仓、不往主聊天发卡片/PDF。

## 1. 身份

- 配对：目标语 **法语（Französisch）** × 读者母语 **德语（Deutsch）**，全称见每页页脚。
- 刊头：`Le Lucerna`（法语专属冠词 Le）。期号：VOL.3 · AUSGABE NR. 3。
- 刊期：2026 年 11 月 2 日（周一）至 11 月 8 日（周日），即 W45。
- 页数：8 页（4 的倍数）。目标语正文逐字冻结，讲解层全部为德语。

## 2. 计数（与核心逐项相等）

- 习题总数：**150**，编号 1–150 连续。
- 页分布：**10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P1–P8；注意 P2=15、P5=17、P8=42，为 FR 串）。
- 级别：A2 53 · B1 75 · B2 22。
- 题型（德语登记标签 = 核心题型）：Satzergänzung 49 · Multiple Choice 26 · Zuordnung 21 · Lückentext 8 · Umformung 7 · Diagrammlesen 6 · Richtig/Falsch 5 · Leseverstehen 5 · Übersetzung 5 · Dialogergänzung 5 · Anwendungsübung 8 · Fehlerkorrektur 4 · Schreiben 1。
- 范文：P8 MODÈLE 框范文逐字 = 核心，**86 词**（80–100 要求内），正文行与核心行逐行相同（仅刊头行改为双语 `MODÈLE · MUSTERTEXT`）。
- 主题（核心实测）：决赛周末（Rolex Paris Masters，Nanterre，11 月 2–8 日；Peur sur le Parc，Plailly，末场夜场 11 月 7 日 19:00–01:00；Le Goût du Large，Port-en-Bessin，11 月 7–8 日，第 22 届）；11 月 2 日周一全法同步开学（无分区错峰）；冬令时第二周（法国 10 月 25 日切换，首周为 W44 内容）；万圣节 10 月 31 日、诸圣节 11 月 1 日、亡灵节 11 月 2 日为刚过去的报道；Pitchfork Paris 第 15 届，11 月 2–8 日；国民议会 2027 预算周按使命审议（11 月 3 日文化/媒体、4 日农业、5 日凝聚力/研究、6 日公共财政/经济；10 月 23 日社保收入部分 115–1 否决，参议院自 11 月 9 日起；日程明确标注为预定，无结果、无民调编造）。

## 3. 冻结门禁（freeze 8/8）

- 核心构建树未修改：`tools/freeze.py baseline` 对未改动核心构建复现 8 页 SVG 字节一致；本版交付 SVG 与核心 SVG 的文本节点对照：新增汉字字符 **8 页均为 0**。
- 源码字面级法语冻结证明：核心 content 源码中 541 个不含汉字的字面，仅 6 个未出现在分版源码中，且全部有据：① P8 E1 题干（改向为德语题干，法语句本身保留在新题干内，见 §6）；② P8 注释 `s'intéresser aux（à+les）` 全角括号改为半角 `(à + les)`（DE 族先例）；③④ 全角括号字面 `（` `）` 同上；⑤ 字典键 `type`（P8 注释规则改用 PRINT_NOTES 显式集合，见 §6，非印刷文本）；⑥ 核心输出路径字面（构建路径，非内容）。
- 节点级删失数为重排假象：P1  headline 字号 24pt（核心 25pt）导致换行不同，单词集合不变；P8 差异为重排 + 改向 E 项，由双门 P8 证明（§4）。

## 4. P8 双门（FR 族专属，BINDING）

- 门 ① plain `tools/p8.py compare`（显式 `--core-p8` / `--edition-p8`，`--total 150`）：核心 noted **97**，分版 noted **97**，状态 **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]。
- 门 ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（`--total 150`）：两侧各 150 键，mismatch **仅 [135, 150]**，两项在两侧均为 noted 项且均为已备案改向（§6），**裸键 mismatch 0**。
- 通过条件满足：plain ∈ {CLEAN} 且零裸键 mismatch。plain 不单用（其对裸键盲区已知）。
- 核心 noted 基线独立核对：核心渲染 `p8.py extract --json` 得 noted 97 个，编号 [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109–150]；裸键补集 53 个与任务清单一致。
- P8 注释语言纯度：全 8 页重扫，汉字 0、全角括号 0、英语残留 0；P8 注释全部为德语。

## 5. 几何门禁

- canonical `tools/occlusion_audit.py`：自检 6 类 planted 全部命中、干净对照静默；**分版 0 flags，核心 0 flags，NEW vs 核心 0**。
- 补充扫描（`hidden_files/weekly-report-w45-fr-de-build/scans.py`，venv PIL）：
  - 全页右缘扫描（ADVANCE 法，限 1885）：3 项超限，全部为核心同行同字（P8 F 配对右侧行 b/d/e，最大 x1=1899.5，仍在内框线 1910 以内）——冻结法语重排继承，非分版缺陷。
  - 全页框线扫描：**0 命中**。
  - 同基线行检查（P1 顶栏 y=92、徽记 y=574、各页页脚 y=2624）：**0 重叠**。
  - P6 图表标签基线锚定墨迹覆盖（getmetrics 法，禁用 getbbox）：**0.0%**（<30% 通过；图表为文字表，框线在文字之前绘制）。
  - 行首检查：4 项行首 `:`，全部与核心同页同坐标同文本逐字节相同（冻结法语换行所致）；**德语自有行首违规 0**。
- 流末端（基线 y，页内限）：
  - P1 headline 栏 1537（限 1812）；P1 hiver 栏 2298（核心继承值，距 quiz 规则线 2312 仅 14px，见 §10）；P1 quiz 2521（限 2540）。
  - P2 feature 707，习题 2365；ET VOUS 框底 1538.6 = 核心值（距日期规则线 1557 有 18px）。
  - P3 正文 813；P4 正文 1306，微习题 2154；P5 正文第 2 栏仅溢 3 个节点至第 3 栏顶部（核心填充模式，非缺陷）。
  - P6 深读 1019，习题 2557（核心继承值，距页脚规则线 2580 有 23px），观点栏 1316（距图表顶 1330 有 14px，本版自有值；核心重跑光标 1225），微习题 2020。
  - P7：A2 954，B1 1053，B2 988，工具箱 1008，短语栏 1574（限 1830），诊所 2140（限 2268）；**预告末基线 2494，墨迹底约 2500 < 2540**。
  - P8：battery 第 3 栏 1516（写作条规则线 1526，MODÈLE 顶 1540，均清除）；答案流末栏 2432（限 2545）；**答案最大基线 2539.2 < 2540，与核心同口径 2539.2 相同**（墨迹底约 2543.5，距页脚规则线 2580 有 36.5px；中间栏填满至底为流式结构使然，核心亦然）。

## 6. P8 改向与显式注释集（W43 先例方法）

- 注释规则：德语注释长于核心 ≤10 字规则，改用显式 `PRINT_NOTES` 集合（与 W43 同配对版同法）；全角括号一律改为半角。
- 仅翻译项改向：E1（#135）翻转为法→德——题干 `Übersetzen Sie ins Deutsche: « Lire un programme, c'est déjà comprendre la France. »`，键 `Ein Programm zu lesen heißt schon, Frankreich zu verstehen.`，注释 `lire un programme = ein Programm lesen`。E2–E5 题干改为德语，法语键不变。写作项（#150）键 → `Offene Aufgabe — Stichpunkte im Schreibrahmen; Mustertext im MODÈLE-Kasten auf dieser Seite`，注释 `Bewertung nach Stichpunkten`。P8 德语写作说明追加 `Die besten Texte erscheinen im VOL.4 (Seite 7, « Le courrier des lecteurs »).`

## 7. gloss 分布（渲染 · 切分逐项计数，核心 = 分版）

| 页 | gloss() 项 | HINWEIS 项（去前缀后切分） | 词表项 |
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

（口径说明：德语前缀 `HINWEIS · ` 自带一个分隔符，计数时先去前缀再切分；否则 P2/P4/P6 各多计 1 项假象。）

## 8. P7（词框、金句、读者角）

- 词框目标语定义句逐字冻结，仅 gloss 本地化（DE 族先例教训的反向执行：本版保留法语句）。
- 金句 8 句均为本期正文逐字连续摘录、页签正确（P7 表格对 = 源文章 + P7 表格）：
  1. `Le lundi 2 novembre, on reprend les cours.`（page 2）
  2. `On ne connaît pas encore les finalistes.`（page 1）
  3. `Les cimetières se sont remplis de chrysanthèmes.`（page 3）
  4. `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?`（page 4，P4 辩论框逐字 comparatif）
  5. `Le festival se promène dans Paris.`（page 5）
  6. `Ce calendrier peut encore bouger.`（page 6；P6 同步形式；P6 深读小写形与微习题键 `peut` 非引文，未动）
  7. `Ce week-end, tout se joue.`（page 1；校对纠正：KIT 原列 `Il est prévu que l'Assemblée examine la Culture mardi.`（page 6）实位于 P7 B2 教学栏与 P8 Q107，非印刷表第 7 项）
  8. `Les jeunes créateurs y rencontrent leur public, en vrai.`（page 5；Q106 改写：error `rencontre`，key `rencontrent`）
- 教学栏 / 工具箱重复 #1/#2/#4/#6 为 KIT 设计，非缺陷（“2×” = 源文章 + P7 表格对）。
- 读者角（LE COURRIER DES LECTEURS · LESERECKE）零编造三件套：
  - 标注的编辑示例：`Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)`（法语示例段逐字保留）；
  - 双语延期披露：法语 `Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.` + 德语 `Anmerkung der Redaktion: Kein VOL.2-Text lag vor (W44 erschien nicht); hier ein Beispiel der Redaktion. VOL.4 bespricht echte Texte.`；
  - 明确的公开征集祈使句（逐字）：`Schicken Sie uns Ihren Text!`
  - 范围裁定：征集句字面覆盖读者自己的文本（来信或作文）；同页披露句把真实文本延期至 VOL.4，P8 写作条把最佳文本指向 VOL.4 第 7 页，预告点名 `Et vos lettres, enfin !` / `und Ihre Briefe!`——组合满足来信与最佳 P8 作文两项，VOL.4 必须兑现。
- 预告（LA SEMAINE PROCHAINE · NÄCHSTE WOCHE · VOL.4）：法语 `Lundi 9 novembre : le Sénat examine le budget de la Sécurité sociale. Mercredi 11 novembre : l'Armistice, un jour de mémoire. Samedi 14 et dimanche 15 novembre : la Foire aux harengs et à la coquille Saint-Jacques, à Dieppe. Et vos lettres, enfin !`；德语 `Nächste Woche: Senat zum Sozialhaushalt, 11. November Waffenstillstandstag, 14.–15. November Muschelmarkt in Dieppe — und Ihre Briefe!`

## 9. FR 族已裁定事实（执行结果）

- P4：`41e édition en 2026 (40e anniversaire)`（1986=第 1 届 → 2025=第 40 届、2026=第 41 届 + 40 周年）；全版 grep：版次主张类仅此一处已改；生日语境 `anniversaire` 句、编号 `40.` / `140–144.`、其他版次 `22e` / `15e`、KIT 历史一律保留。
- P7 #4 保留 P4 辩论框逐字 comparatif；#8 用 P5 逐字句 + Q106 改写。
- P6 同步为 `Ce calendrier peut encore bouger.`。
- Q120：题干 `Si j'étais libre dimanche, j'___ à Nanterre.`，选项 A. irai / B. irais / C. vais，键 B 不变，P8 注释同步（si + imparfait → conditionnel + elision j'）；Q119/Q121 不动。

## 10. 家具三方对照（W43 同配对版 优先于 README #20 泛化）

- 徽记：(975, 574)，22pt BRICK，居中，与 W43 字符串逐字相同：`FRANZÖSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`。README #20 的 (975, 574) 22pt 描述的是法语作目标时的情形，与本版一致，无冲突。
- P1 顶栏（y=92 三段）：左 `VOL. 3 · AUSGABE NR. 3`（W43：VOL. 2 · AUSGABE NR. 2）；中 `HEBDOMADAIRE EN FRANÇAIS · JEDE WOCHE · FRANZÖSISCH, WIE FRANKREICH ES LIEST`（与 W43 相同）；右 `SEMAINE DU 2 AU 8 NOVEMBRE 2026`（W43：19–25 OCTOBRE 2026）。
- 刊名 262（178pt）、副标题 330（46pt）`FRANZÖSISCHE WOCHENZEITUNG · VOL.3 · FINALWOCHENENDE`（W43：VOL.2 · SPÄTHERBST & FESTE；实测宽 1492.5px，适配）、标语 372 法语原文与 W43 相同、暗带 478/522（法语头条为本周内容，德语右侧为本周短语）、规则线与暗带几何与 W43 相同。
- 页脚（每页，y=2624）：`Le Lucerna · FRANZÖSISCHE WOCHENZEITUNG VOL.3 · TEXT AUF FRANZÖSISCH · ERKLÄRUNGEN AUF DEUTSCH` + `Seite N von 8`（W43 模板，VOL 号更新）。
- 短双语栏头（与 W43 同）：WÖRTER, TERMINE, DISKUSSION, SIE SIND DRAN, ÜBUNGEN, AUFBAU, VERTIEFUNG, WERKZEUG, KLINIK, LESERECKE；说明词 Ausfüllen / Umformen / Zuordnen / Korrigieren / `Vrai ou faux?`；gloss 前缀 `HINWEIS · `；P8 分隔 `— SEITE {n} —`。

## 11. 图片（仅明确公有领域，credit 取 Commons API Artist 字段原文）

| 页 | 图 | 放置（x, y, w×h） | credit（与核心逐字相同） | payload 哈希口径 |
|---|---|---|---|---|
| P1 | atget-paris.jpg | 65, 1874, 896×320 | Eugène Atget (1857-1927), photographie, domaine public | base64 文本 sha256 `ff20bc2b…a8e5d`；解码 JPEG sha256 `f3705af2…5f`，334674 字节 |
| P2 | hiroshige-maple.jpg | 1451, 200, 434×480 | Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA | base64 文本 sha256 `6918cb8b…1664ae`；解码 JPEG sha256 `5b772fac…ee2`，646242 字节 |
| P3 | chrysanthemum-blanco.jpg | 1451, 200, 434×540 | Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public | base64 文本 sha256 `bfaadf5b…eca9`；解码 JPEG sha256 `be071fda…d0c94`，142340 字节 |

（完整哈希见构建树 `final-hashes-r5.txt` 对应的 SVG 内嵌 payload；三张图均已核实确已放置，解码字节数与资产文件一致。）

## 12. W43 偏差清单（预期偏差，仅此清单）

1. VOL.3 vs VOL.2、刊期 11 月 2–8 日 vs 10 月 19–25 日、副标题主题 FINALWOCHENENDE vs SPÄTHERBST & FESTE、暗带右侧本周短语（均为刊期内容更新）。
2. P8 答案字号 14.5pt vs W43/核心 15.5pt（德语注释更长，答案流适配）。
3. P8 写作条 wy 1540 vs 1500（battery 溢出适配；条上线 1526，MODÈLE 顶 1540）。
4. P8 battery 习题间距 6 vs 11，F 配对间距 6 vs 14（同上）。
5. P1 头条段字号 24pt/行高 1.45 vs 核心 25pt/1.52（gloss 增长适配；法语文本字节不变，仅呈现）。
6. P8 battery 段字号 20pt vs 核心 21pt（cloze/阅读/对话三段）。
7. P1 gloss 缩短为单字 gloss + `Nachtevent`（框几何适配）。
8. P2 ET VOUS 德语段缩短为 2 行定稿 `Montagmorgen: Wo waren Sie, welches Buch? Zwei Sätze an die Redaktion!`（框底回归核心值 1538.6）。
9. P7 读者角为编辑示例 + 延期披露（继承 VOL.3 核心的诚实处理；W43 为真实来信——差异来自核心内容，非分版自选）+ 新增征集祈使句 `Schicken Sie uns Ihren Text!`（SOP 门禁要求）。
10. 翻译改向方法同 W43 先例，项号不同（本版 #135/#150；W43 为 #132/#145）。
11. P7 栏头短式、P8 分隔、半角括号、PRINT_NOTES 方法与 W43 相同，无偏差。
12. 其余家具、规则线、暗带、页脚模板与 W43 逐项相同。

## 13. 工具链与可复现性

- 单源头：`hidden_files/weekly-report-w45-fr-de-build/transform.py`（355 项替换：主 340 + `翻译` 1 + 修复轮 14）；每轮修复先存全量 pre-fix SHA256 基线（`pre-fix-hashes-r1.txt`），修复只进 transform.py，事后以核心源码新拷贝 + 当轮 transform.py 在 scratch 目录重放、diff 恰为当轮改动后才提升入构建树。
- 渲染：`run.py` 单进程 driver（content12 → content34 → content56 → content7 → content8，共享 bslib4 登记）；`render.py` 卡片 PNG @1950（cairosvg）、印刷 PDF（svg2pdf + pypdf）、网络 PDF（整卡 JPEG quality 72，核心配方；临时 JPEG 留构建树内，事后删除）。
- 解释器与 PIL：run.py 与 render.py 均用 `tools/venv/bin/python`，Python 3.12.3，Pillow 13.0.0；审计测量同 venv PIL。系统 python3（同为 3.12.3，Pillow 10.2.0）无 cairosvg，故 render.py 必须用 venv。
- 确定性证明：登记表转储重跑后 8 页 SVG 哈希与交付前一致（`sha256sum -c` 全 OK）；核心构建树与 W43 目录未改动；未碰 weekly-git、未建 cron、未发 Discord。

## 14. 交付文件

- `svg/` ×8，`cards/` ×8（1950×2700），`Le-Lucerna-VOL3-DE.pdf`（印刷）9,750,981 字节，sha256 `374ca78f…750`；`Le-Lucerna-VOL3-DE-web.pdf`（网络）5,096,076 字节，sha256 `42e397b2…f`（完整值见 §15）。
- `WEEKLY-KIT.md`（本文件），`ABSTRACT.txt`（德语单行，无 ASCII 双引号）。

## 15. 终版哈希（round-5 交付）

```
Le-Lucerna-VOL3-DE.pdf       374ca78ffe2763ac9f66a1a341b8aabed4258bcdf428584db144d369aab10750
Le-Lucerna-VOL3-DE-web.pdf   42e397b2220c1f1dc1b5c199da867560918cb116377c21190a47a3ce8dbf028f
svg/p1-une.svg               03a2769c93332d96278284b57e8940376495d2531d893a68415dedd79fb396f8
svg/p2-vie.svg               1d4f73e0f16f136955c87105c7d617fb3c5fa0a7591d5c800181113680de921b
svg/p3-culture.svg           6075674d536d0374459be102e8d4aa0de54125014ca929ef5dbad8e8ddf1862b
svg/p4-sport.svg             086e1b597f5323efa3d2da6b763dca5cda05e29fd09bd5b4a9a6b83da136618a
svg/p5-jeunesse.svg          e50c2d80c35518e09f450a8e187c2ef619f816755d0800b73b4043ed6c6fed6e
svg/p6-politique.svg         ffcb9a023b096bebba8147fa4476b449f52b3674fbba927724627da370e79805
svg/p7-langue.svg            5cf8125a9e32c201322b8fc75f443180199236c19402b9a2b2f7877e4cd605ae
svg/p8-exercices.svg         439ab63dcf25f3e4f2dfdf9f775300594f4adcdba880940a66734c89a4d3a6c8
cards/p1-une.png             dd086a63aa28acbff7c43b7193efa45dfdf3ca6b2945445f53cdc70f32dac639
cards/p2-vie.png             1fc6c22b0c901fb1981018f19073eb1c1794f49418485de5143ea7a2dd06b8dd
cards/p3-culture.png         6380bb00339ce6404bb16922fb3712c126431fbab7ccfb058cdbb7786fdcc333
cards/p4-sport.png           08bfeca5fab412f2447de9a55b4ec69c9d3595f53dc3e7f6dc76f5cd8f307eb1
cards/p5-jeunesse.png        1afd8fa6bfc272b3ba003350b039db6e93f29438a1afa0987889290272cc2ebe
cards/p6-politique.png       cf6a6e52d1a369f5e86efc3ee62070860bdb5845c9b8da61d12a1cd251d46fd4
cards/p7-langue.png          af23dcbc20fd762d83062504d052cdb483f4188878f0b53bcc37a194a0136276
cards/p8-exercices.png       57b396222dada41eac4c013e5da76284aa7c3afd4261ae243b609777d8c5e896
```

## 16. ABSTRACT 原文

> Le Lucerna VOL.3, Woche vom 2. bis 8. November 2026: Französische Wochenzeitung für deutschsprachige Leser — Finalswochenende mit Rolex Paris Masters in Nanterre, Peur sur le Parc in Plailly und Le Goût du Large in Port-en-Bessin, Schulbeginn am 2. November, Halloween und Toussaint, Pitchfork Paris und Budget 2027 in der Nationalversammlung, mit 150 Übungen von A2 bis B2, Wortschatz, Grammatik und Mustertext. Französisch lernen mit echten Nachrichten: Finalwochenende, Winterzeit und französische Feste verstehen.

## 17. 未决观察（非阻塞，交独立校对裁定）

1. P8 答案最大基线 2539.2 / 墨迹底约 2543.5，名义限 2540 仅差 3.5px；但与核心同口径值逐字节相同（核心 2539.2），距页脚规则线 2580 有 36.5px，遮挡审计 FOOTER 0 旗——结构使然，非分版缺陷。
2. P8 F 配对右侧 3 行右缘超限（最大 1899.5）与 P3/P4/P5/P7 行首 `:` 4 项，全部为核心同行同字继承；德语自有项 0。
3. P1 hiver 末 2298、P6 习题末 2557 为核心继承的紧贴值，P6 观点栏末 1316 为本版自有值（核心重跑光标 1225；几何合格，距图表顶 1330 有 14px），遮挡审计 0 旗。
4. P5 正文第 2 栏溢 3 个节点至第 3 栏顶部，符合核心填充模式，目视无重叠。
5. 本版未做项：独立校对、GitHub 入库、Discord 投递（投递暂停令仍有效，须主线另行决定）。
