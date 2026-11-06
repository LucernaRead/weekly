# 独立校对报告 — Lucerna Weekly W45 · FR × DE（法语 × 德语）

**结论：ZERO PROBLEMS**（阻塞项：无。下述 6 条为非阻塞观察，其中 2 条为 KIT 文字表述误差、纸面正确，按任务规则不阻塞。）

**校对员纪律**：只校对，未改源码、未宣布上架、未派生下级代理、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未写 weekly-git（仅只读列目录）、未改核心/W43 目录、未清理共享 scratch。构建树重跑登记展开时，先将构建树完整拷到自有 scratch（`hidden_files/w45/fr-de-proof/scratch/build-ed-copy/`、`build-core-copy/`）并把 OUT 重定向到自有 scratch 输出目录，原构建树与交付/核心目录全程只读。

## 0. 开工查重

- 开工时 `ps` 无任何以 fr-de 树为 cwd 的在途进程；交付物最新 mtime 为 `WEEKLY-KIT.md` 2026-10-28 03:27:52 UTC，至 03:30:33 复查时已静默 161 秒 → 安全开工，不 stand down。
- 校对前后哈希 diff：交付物（2 PDF + KIT + ABSTRACT + 8 SVG + 8 卡）与核心（2 PDF + KIT + ABSTRACT + 8 SVG）**diff 均为空**（证据：`scratch/pre-hashes.txt` vs 校对后重算）。

## 1. 交付指纹（独立重测，与构建员声称一致）

- 印刷 PDF `Le-Lucerna-VOL3-DE.pdf`：9,750,981 B，sha256 `374ca78ffe2763ac9f66a1a341b8aabed4258bcdf428584db144d369aab10750`，pdfinfo 8 页，1462.5×2025 pts。
- 网页 PDF `Le-Lucerna-VOL3-DE-web.pdf`：5,096,076 B，sha256 `42e397b2220c1f1dc1b5c199da867560918cb116377c21190a47a3ce8dbf028f`，pdfinfo 8 页，936×1296 pts。
- 8 张卡均为 1950×2700 px；8 SVG 哈希与 KIT §15 逐项一致。
- 刊头：每页 `Le Lucerna`（法语冠词 Le）；VOL.3 全版一致，VOL.2 仅出现在 P7 延期披露句中（正当引用，非残留）；VOL.4 出现处均为下期正向引用（P2 ET VOUS、P4 À SUIVRE、P7 披露+预告、P8 写作条+答案 150）。

## 2. 冻结门禁

- **新增汉字**：交付 8 页 SVG 文本节点（base64 属性天然排除）逐页扫描，Han 字符 **8 页均为 0**，全角括号 **8 页均为 0**。
- **源码字面冻结（独立重测，非抄 KIT）**：对核心与分版构建树 `content12/34/56/7/8.py` 做 AST 字面提取：核心字面 851 个，其中不含汉字者 **541 个**，分版源码中缺失 **恰 6 个**，与 KIT 所列一一对应：
  1. `Traduisez : « Lire un programme, c'est déjà comprendre la France. »`——E1 题干改向；法语句本身逐字保留在新题干内（分版 P8 节点 y=1332/1361/1390，x=989：`Übersetzen Sie ins Deutsche: « Lire un programme, c'est déjà comprendre la France. »`）。
  2. `s'intéresser aux（à+les）`——全角括号改半角，分版 P8 节点 y=2440.87：`(s'intéresser aux (à + les))`。
  3. `（`、4. `）`——同上，全角→半角转换。
  5. `type`——核心 `content8.py:153` 的 `e["type"]` 注释集规则键；分版改用显式 `PRINT_NOTES` 集合（`content8.py:148,154`），非印刷文本。
  6. `~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg`——核心输出路径字面，构建路径，非内容。
- 分版源码字面含汉字：**0 个**。
- **桥接词**：交付 SVG 全文、KIT 全文、ABSTRACT 全文、分版内容源码中 `桥接` 均为 0。唯一出现处为构建树 `checks.py:73` 自身的违禁词检测器字面（检测逻辑引用该词，非标签使用）——见非阻塞观察 5。

## 3. P8 双门（FR 族专属，BINDING，全部独立重测）

### 门 ① plain `tools/p8.py compare`（新旧两版并列）

- 旧版 = 当前 `tools/p8.py`，sha256 `67df05f1bc7234eeb48d25fff2cb85a406e8bfcd6b211b9fdc76231b6296c132`。
- 新版 = `hidden_files/w45/p8-dash-fix-verify/p8.py.new`，sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`（须 `PYTHONPATH=tools` 供其 import `tables`；首次直跑报 `ModuleNotFoundError` 属调用方式问题，非工具缺陷，按验证报告方法加 PYTHONPATH 后正常）。
- 两版结果**完全相同**：核心 noted **97**，分版 noted **97**，状态 **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[135, 150]。noted 集两版逐项相等（[1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109–150]），FR noted 数在两版下均为 97，无差异。
- 分版 `content8.py:148` 的 `PRINT_NOTES` 显式集合（97 项）与 p8 提取的 noted 集逐项相等。

### 门 ② `hidden_files/w45/p8-fr-gap-fix/keycompare.py`（全 150 键）

- 旧版 p8 驱动：mismatch **仅 [135, 150]**；新版 p8 驱动：mismatch **同样仅 [135, 150]**。两版下**裸键 mismatch 均为 0**。
- 逐项裁定（从印刷行原文）：
  - **#135（真改向，noted，两侧均为 noted）**：核心键 `读一份日程，本身就是在了解法国。`（面向中文读者的译文键）→ 分版键 `Ein Programm zu lesen heißt schon, Frankreich zu verstehen.`（面向德语读者的译文键）；分版 P8 印刷行 y=2103.0/2121.85/2140.7（x=1451）：`135. Ein Programm zu lesen heißt schon, Frankreich zu verstehen. (lire un programme = ein Programm lesen)`，注释为德语 gloss，无中文残留。改向已备案（KIT §6），通过。
  - **#150（真改向，noted，两侧均为 noted）**：核心键 `开放题 — 要点见写作框，范文在第 8 版写作框内` → 分版键 `Offene Aufgabe — Stichpunkte im Schreibrahmen; Mustertext im MODÈLE-Kasten auf dieser Seite`；分版 P8 印刷行 y=2366.9/2385.75/2404.6（x=1451），注释 `(Bewertung nach Stichpunkten)` 纯德语。新旧两版提取的 150 键字面不同（旧版含破折号后注释全文，新版剥离为 `Offene Aufgabe`），但 mismatch 集与裸键结论不变。改向已备案（KIT §6），通过。
- 通过条件满足：plain ∈ {CLEAN}（两版皆 CLEAN）且零裸键 mismatch。**P8 双门通过。**

## 4. 登记展开（自有 scratch 拷树重跑，OUT 已重定向）

- 分版与核心构建树各拷一份到自有 scratch 并重跑 `content12→34→56→7→8`：REG 均为 **150 题连续（1–150）**。
- 页分布（两边逐项相等）：**10 / 15 / 18 / 18 / 17 / 18 / 12 / 42**（P2=15、P5=17、P8=42，FR 串）。
- 级别（两边逐项相等）：**A2 53 / B1 75 / B2 22**。
- 题型（标签本地化、数量 1:1）：Satzergänzung 49、Multiple Choice 26、Zuordnung 21、Lückentext 8、Umformung 7、Diagrammlesen 6、Richtig/Falsch 5、Leseverstehen 5、Übersetzung 5、Dialogergänzung 5、Anwendungsübung 8、Fehlerkorrektur 4、Schreiben 1。
- 逐题 page/level 150/150 相等；REG 键仅 #135/#150 不同（即 P8 两改向项），余 148 项键逐字相等。
- 确定性：自有 scratch 重渲染的 8 页 SVG 与交付 SVG **逐字节相等 8/8**，核心重渲染与核心 SVG **逐字节相等 8/8**——核心基线未动、交付可复现。

## 5. gloss（渲染 · 切分逐项计数，独立重跑）

- 用构建树 `gloss_count.py`（只读）重跑，核心 = 分版，逐页与 KIT §7 一致：
  - gloss() 项 P1–P6：**7 / 6 / 6 / 7 / 6 / 6，合计 38**；P7/P8 为 0。
  - HINWEIS 项（去 `HINWEIS · ` 前缀后切分）：P2/P4/P6 **各 3，合计 9**；其余页 0。
  - 词表项：P3 **10** / P4 **8** / P5 **8，合计 26**。
- 口径说明：德语前缀自带一个分隔符，去前缀后再切分，否则 P2/P4/P6 各多计 1 项假象——本校对按去前缀口径复核，与声称一致。

## 6. 金句与 P7（词框、金句、读者角）

- **P7 教学栏法语定义句逐字冻结**：P7 教学区（y<1150）全部法语句节点在核心与分版中坐标与文本逐项相同，仅栏头与 gloss 段本地化为德语（如 `NIVEAU A2 · GRUNDLAGEN`、`Werkzeugkasten: Drei Sätze zum Mitnehmen, …`）。工具箱/教学栏重复 #1/#2/#4/#6 为 KIT 设计（源文章 + P7 表格对），非缺陷。
- **P7 表 8 句（印刷表实际内容，词序级核实）**：表内 8 句在核心与分版中完全相同，词序逐字出自所标页正文，页签全部正确：
  1. `Le lundi 2 novembre, on reprend les cours.`（page 2）✓
  2. `On ne connaît pas encore les finalistes.`（page 1；P4 亦有回响）✓
  3. `Les cimetières se sont remplis de chrysanthèmes.`（page 3）✓
  4. `Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?`（page 4，P4 辩论框逐字 comparatif，分版 P4 节点与核心同坐标同文本）✓
  5. `Le festival se promène dans Paris.`（page 5）✓
  6. `Ce calendrier peut encore bouger.`（page 6；P6 深读与 LES PHRASES DES JOURNAUX 框同步）✓
  7. `Ce week-end, tout se joue.`（page 1，P1 LE MOT 框首句）✓
  8. `Les jeunes créateurs y rencontrent leur public, en vrai.`（page 5；Q106 改写：P7 诊所 error `Les jeunes créateurs y rencontre leur public, en vrai.`，P8 答案 `106. Les jeunes créateurs y rencontrent leur public, en vrai. (Subjekt-Verb-Kongruenz: créateurs (Plural) → rencontrent, …)`）✓
- KIT §8 枚举把 `Il est prévu que l'Assemblée examine la Culture mardi.` 列为 #7、未列 `Ce week-end, tout se joue.`：该句实为 P7 B2 教学栏例句 + P8 Q107  stems（`examines` 错式），其语法点源自 P6，而非 P6 文章引文；印刷表本身与核心一致且 8 句全部合格。**此为 KIT 文字误差、纸面正确，按任务规则仅作非阻塞观察（见观察 1）。**

## 7. FR 族已裁定事实（逐项在核心原文与分版执行中核实）

- P4：`41e édition en 2026 (40e anniversaire)` 在位，分版 P4 节点 y=278/308.53（x=1473）与核心同坐标同文本；其余语境保留：`anniversaire` 句（P7 诊所 105、P8 答案 36 等）未动；编号 `40.`（P3 徽记）与 `140–144.`（P8 配对）在位；`22e`（P1 `22e édition`）、`15e`（P5 `15e édition`）在位。
- P6：`Ce calendrier peut encore bouger.` 在位（P6 LES PHRASES DES JOURNAUX 框及深读小写形）；微习题键 `peut`（Q95）未动。
- Q120：题干 `Si j'étais libre dimanche, j'___ à Nanterre.`（分版 P8 y=246.0，x=527，与核心同坐标），选项 `A. irai · B. irais · C. vais`（y=275.0），键 B（REG 与 P8 答案均确认），P8 注释同步：`120. B (si + imparfait → conditionnel présent; j' ist je vor Vokal (Elision))`。Q119（`Elle s'intéresse ___ festivals. A. à les · B. aux · C. des`，键 B）与 Q121（`À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant`，键 A）题干与键均与核心一致（REG 逐题相等）。

## 8. 几何门禁

- **canonical `tools/occlusion_audit.py`**（venv）：自检 6 类 planted 全部命中、干净对照静默；**分版 0 flags，核心 0 flags，NEW vs 核心 0**（证据：`scratch/occlusion-ed.json`、`occlusion-core.json`、`occlusion-ed-vs-core.json`）。
- **补充扫描**（扫描脚本拷到自有 scratch 重跑，与构建员 `scans-r5.txt` 逐行一致）：
  - 全页右缘（ADVANCE 法，限 1885）：3 项超限，最大 x1=1899.5，仍在内框线 1910 内。逐项核实为核心同行同字继承：P8 F 配对行 b/d/e 文本与 x0/x1 与核心逐字节相同（y 因 14.5pt 重排下移，核心 y=940/1016/1054 → 分版 y=1065/1141/1179）；**德语自有超限项 0**。
  - 全页框线扫描：**0 命中**；同基线行检查（y=92/574/2624）：**0 重叠**。
  - P6 图表标签基线锚定墨迹覆盖（getmetrics 法，禁用 getbbox）：**0.0%**（<30% 通过）。
  - 行首 `:` 4 项：P3 y=789.65、P4 y=837.12、P5 y=430.65、P7 y=428.1，核心与分版同页同坐标同文本逐字节相同；**德语自有行首违规 0**。
- **流末端（口径明示）**：
  - P8 答案：基线口径下分版最大基线 **2539.18**，核心同口径 **2539.19**，基本相同；墨迹底口径（occlusion_audit 墨迹盒法）分版 **2542.68**，核心 **2541.23**——两者均超名义限 2540 约 1–3px，距页脚规则线 2580 各有 **37.3px / 38.8px** 间隙，且 canonical 审计 FOOTER 0 旗。**裁定：按口径一致性通过**——名义 2540 非 canonical 审计限（canonical 限为墨迹过 2580），核心同口径亦超 2540，分版非新增问题。构建员“墨迹底约 2543.5”与本校对方法值差 <1px，属方法差异，不影响结论。
  - P7 预告：末基线 **2494.0**（x=1013，德语行 `November Muschelmarkt in Dieppe — und Ihre Briefe!`），墨迹底 **2498.5**，距 2540 有 41.5px；法语预告 3 行与核心逐行同坐标。
  - P1 hiver / P6 习题 / P6 观点栏（流光标口径，见 §9 观察 2 的口径说明）：P1-hiver 光标 2298 与核心重跑值相同（P1 图 rect 底 2290 两边一致）；P6-ex 光标 2557 与核心重跑值相同；P6-opinion 光标 1316 ≠ 核心重跑值 1225（见观察 2），但其墨迹（末节点基线 1277.33，墨迹底约 1282）距图表顶 1330 约 48px，无遮挡。
- **P5 正文溢栏**：分版对话题 #78（徽记 y=222、编号 y=223、题干 y=256/290，x=989/1019/1061）落于第 3 栏（col 2）顶部；核心同题在第 2 栏底部（y=2388–2456）。属同一栏填充机制下的分页差异（德语桥接行拉长所致），P5 卡面目视无任何重叠，occlusion 0 旗。**非缺陷**（见观察 3）。

## 9. 家具三方对照（W45 核心 / W43 同配对 / 本版）

- 徽记：分版与 W43 **逐字节相同**：`<text x="975" y="574" font-size="22" font-weight="700" fill="#a4553a" text-anchor="middle">FRANZÖSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER</text>`（22pt，BRICK 色 #a4553a，居中）。与 #20（975,574）22pt 描述一致，无冲突。
- P1 顶栏 y=92：中段 `HEBDOMADAIRE EN FRANÇAIS · JEDE WOCHE · FRANZÖSISCH, WIE FRANKREICH ES LIEST` 与 W43 逐字相同；左右两段仅为期号/刊期更新（VOL. 3 · AUSGABE NR. 3；SEMAINE DU 2 AU 8 NOVEMBRE 2026）。
- 刊名 y=262（178pt）、副标题 y=330（46pt）与 W43 几何相同；副标题文本为刊期更新（VOL.3 · FINALWOCHENENDE vs W43 VOL.2 · SPÄTHERBST & FESTE）。
- 页脚每页 y=2624：`Le Lucerna · FRANZÖSISCHE WOCHENZEITUNG VOL.3 · TEXT AUF FRANZÖSISCH · ERKLÄRUNGEN AUF DEUTSCH` + `Seite N von 8`，W43 模板、VOL 号更新。
- W43 偏差清单逐项核实（均为清单所列，不影响可读性）：
  1. 刊期/副标题/暗带右侧短语为刊期内容更新 ✓。
  2. P8 答案字号 **14.5pt**（分版 `kf.para`）vs W43/核心 **15.5pt** ✓（W43 P8 答案区字号实测 15.5）。
  3. P8 写作条 `wy = 1540`（分版源码）vs 1500：分版 MODÈLE 栏头基线 y=1578 vs W43/核心 1538（栏顶 = 基线 −38 → 1540 vs 1500）；分版条上线 y=1526 规则线在位，W43 无此线 ✓。
  4. P8 battery 间距：分版 `gap=6`（ex 与 match_set）vs 核心默认 11（ex）/14（match_set）✓。
  5. P1 头条段 **24pt/1.45**（分版 `content12.py:40–44` 显式）vs 核心默认 **25pt/1.52**（bslib `para` 默认）✓；法语文本字节不变，仅呈现。
  6. P8 battery  prose 段 **20pt**（分版 cloze/阅读/对话三段 `bf.para`）vs 核心 **21pt** ✓（ex 本体两边均为 20pt，不在此项内）。
  7. P1 gloss 缩短为单字德语 gloss + `Nachtevent`（P1 卡面 HINWEIS 框目视确认）✓。
  8. P2 ET VOUS 德语段缩为 2 行定稿 `Montagmorgen: Wo waren Sie, welches Buch? Zwei Sätze an die Redaktion!`（节点 y=1505.81/1534.21，x=1473），框底 rect 1538.6 与核心逐值相同 ✓。
  9. P7 读者角为编辑示例 + 延期披露：继承 VOL.3 核心的诚实处理；W43 为真实来信（`L. M., lectrice fidèle (composition du VOL.1, « Mon automne »)`，无示例标注）——差异来自核心内容，非分版自选 ✓；新增征集祈使句见 §10。
  10. 翻译改向方法同 W43 先例（德语题干 + PRINT_NOTES 式显式注释集；W43 P8 亦有 `Übersetzen Sie ins Deutsche/Französische` 题干与 `— SEITE n —` 分隔），项号不同（本版 #135/#150；W43 为 #132/#145）✓。
  11. P7 栏头短式、P8 分隔、半角括号、PRINT_NOTES 方法与 W43 相同 ✓。

## 10. 读者来信角（法德双语延期披露 + 征集句范围裁定）

- 法语例信逐字冻结：`« Mon week-end de novembre : samedi, j'ai regardé un match à la télévision ; dimanche, j'ai cuisiné une soupe et j'ai lu vingt pages. » — Exemple de la rédaction (ce texte n'est pas une lettre de lecteur).`（分版 P7 节点 y=1956.0/1985.82/2015.64，x=1013，与核心同坐标同文本），**零编造**（明确标注非读者来信）。
- 双语延期披露（期号一致性核实：本版为 VOL.3，下期为 VOL.4）：
  - 法语：`Note de la rédaction : aucun texte du VOL.2 n'était arrivé au moment de mettre sous presse (le numéro W44 n'a pas paru). Le VOL.4 reprendra la promesse.`
  - 德语：`Anmerkung der Redaktion: Kein VOL.2-Text lag vor (W44 erschien nicht); hier ein Beispiel der Redaktion. VOL.4 bespricht echte Texte.`
  - 两句均称“无 VOL.2 真信、VOL.4 兑现”，期号无矛盾。
- 征集祈使句逐字：`Schicken Sie uns Ihren Text!`（分版 P7 节点 y=2233.3，德语披露句末）。
- **范围裁定（明确、无含糊）**：征集句字面 `Ihren Text`（读者自己的文本）覆盖范围**同时包括来信与作文**——“Text”不限于 “Brief”（来信）也不限于 “Aufsatz”（作文），来信是文本、作文也是文本，故字面已覆盖两项，无需依赖窄读补救。即便按最窄读法（仅覆盖来信）适用 pt 族组合规则，组合亦满足：同页披露句把真实文本延期至 VOL.4；P8 写作条把最佳文本指向 `VOL.4 (Seite 7, « Le courrier des lecteurs »)`（分版 P8 德语写作说明逐字在位）；预告点名 `Et vos lettres, enfin !` / `und Ihre Briefe!`（分版 P7 预告末行）。**结论：组合满足来信与最佳 P8 作文两项，VOL.4 必须同时兑现（读者园地刊登真实来信 + 最佳 P8 作文）。**

## 11. 计数 / 范文 / 图片 / 摘要

- 登记展开见 §4（150 题连续、级别/页分布 = 核心）。
- 范文：P8 MODÈLE 框正文 7 行与核心逐行相同（仅栏头改为双语 `MODÈLE · MUSTERTEXT`）；空白分隔计数 **86 词**（80–100 要求内；其他口径：去纯标点 token 84、字母段 91，均在 80–100 附近且正文与核心逐字相同，计数口径不影响合格性）。
- 图片（3 张，payload 两口径均与核心逐字节相同，credit 与核心逐字相同且在页）：
  - P1 atget-paris.jpg，放置 (65, 1874, 896×320)，credit `Eugène Atget (1857-1927), photographie, domaine public`；base64 文本 sha256 `ff20bc2b…a8e5d`，解码 JPEG sha256 `f3705af2…595f`，334674 字节。
  - P2 hiroshige-maple.jpg，放置 (1451, 200, 434×480)，credit `Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA`；base64 文本 sha256 `6918cb8b…1664ae`，解码 JPEG sha256 `5b772fac…ee2`，646242 字节。
  - P3 chrysanthemum-blanco.jpg，放置 (1451, 200, 434×540)，credit `Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public`；base64 文本 sha256 `bfaadf5b…eca9`，解码 JPEG sha256 `be071fda…d0c94`，142340 字节。
  - 哈希口径已注明：base64 文本 = SVG 内嵌 base64 字符串本身的 sha256；解码 JPEG = base64 解码后字节的 sha256。
- ABSTRACT：德语单行，无 ASCII 双引号，无汉字；含真实主题关键词（Rolex Paris Masters、Nanterre、Peur sur le Parc、Plailly、Le Goût du Large、Port-en-Bessin、Schulbeginn 2. November、Halloween、Toussaint、Pitchfork Paris、Budget 2027、Nationalversammlung、150 Übungen A2–B2）+ 学习者检索短语（`Französisch lernen mit echten Nachrichten: Finalwochenende, Winterzeit und französische Feste verstehen.`）。

## 12. 全 8 卡目视

- P1–P8 卡面逐页目视：无文字重叠、无出框、无缺字、无错位。重点目视项：P1 徽记/头条/冬令时栏/图片 credit；P2 ET VOUS 2 行德语段与框底；P3 词表与菊花图；P4 辩论框 comparatif 与 `41e édition` 框；P5 第 3 栏顶对话题 #78 与侧栏无重叠；P6 图表标签与观点栏；P7 读者角披露与预告；P8 写作条/MODÈLE 框/答案流末端（末行距页脚规则线有足量间隙，卡面无压线）。

## 13. 非阻塞观察（不构成 NOT PASS 的理由）

1. **KIT §8 金句枚举误差（纸面正确）**：KIT 把 `Il est prévu que l'Assemblée examine la Culture mardi.` 列为金句 #7，但印刷的 P7 表 8 句中第 7 项实际为 `Ce week-end, tout se joue.`（page 1）；前者位于 P7 B2 教学栏与 P8 Q107（错式 `examines`），语法点源自 P6，非 P6 文章引文。印刷表与核心一致、8 句全部合格。建议 KIT 后续修订枚举，不动纸面。
2. **KIT “P6 观点栏 1316 核心继承”表述误差（几何合格）**：自有 scratch 重跑核心构建树，P6-opinion 光标为 1225，分版为 1316——1316 是分版自有值（德语 gloss 行更长），不是核心继承值。但几何仍合格：光标距图表顶 1330 有 14px，墨迹底约 1282 距图表顶约 48px，occlusion 0 旗。建议 KIT 改称“分版值、距图表顶 14px（光标口径）”，不动纸面。
3. **P5 分页与核心不同（机制相同、目视干净）**：分版 #78 溢至第 3 栏顶部，核心 #78 留在第 2 栏底部；同属栏填充机制，卡面无重叠。KIT“核心填充模式”应理解为机制级表述，非逐页分页相同。
4. **P8 末端口径说明**：名义限 2540 为构建员内部页内限，非 canonical 审计限；基线口径分版 2539.18 vs 核心 2539.19 基本相同，墨迹底口径两者均超 2540 约 1–3px 且距 2580 规则线均有 37px 以上间隙、FOOTER 0 旗。按口径一致性通过；构建员“墨迹底约 2543.5”与本校对墨迹盒法值 2542.68 差 <1px，属方法差异。
5. **构建树 `checks.py:73` 含 `桥接` 字面**：该行是违禁词检测器自身的检测字符串（`any("桥接" in …)`），非标签使用；交付 SVG、KIT、ABSTRACT、内容源码中 `桥接` 均为 0。建议后续将检测字面改为拆分写法以避字面扫描误报，不动纸面。
6. **流光标“紧贴值”口径说明**：P1-hiver 2298、P6-ex 2557、P6-opinion 1316 均为构建器内部流光标终点，非 SVG 墨迹底；SVG 实测墨迹距下一规则线更远（如 P6 末习题基线 2506.05，距 2580 约 74px）。“紧贴”仅在光标口径下成立，不构成遮挡风险。

## 14. 未做事项（按任务边界）

- 未宣布上架；未投递 Discord（投递暂停令仍有效）；未入库 GitHub；未往主聊天发卡片/PDF；未建 cron；未派生下级代理。

## 证据文件（本校对自有 scratch，只读产物）

- `hidden_files/w45/fr-de-proof/scratch/pre-hashes.txt`、`pre-core-hashes.txt`（校对前快照）
- `hidden_files/w45/fr-de-proof/scratch/p8-old-compare.json`、`p8-new-compare.json`、`p8-old-core.json`、`p8-old-ed.json`、`p8-new-core.json`、`p8-new-ed.json`
- `hidden_files/w45/fr-de-proof/scratch/keycompare-old.json`、`keycompare-new.json`
- `hidden_files/w45/fr-de-proof/scratch/occlusion-ed.json`、`occlusion-core.json`、`occlusion-ed-vs-core.json`
- `hidden_files/w45/fr-de-proof/scratch/scans-rerun.txt`、`gloss-rerun.txt`
- `hidden_files/w45/fr-de-proof/scratch/rerun-ed.log`、`rerun-core.log`、`build-ed-copy/REG.json`、`build-core-copy/REG.json`、`out-ed/`、`out-core/`（重渲染 SVG，与交付/核心逐字节相等）
