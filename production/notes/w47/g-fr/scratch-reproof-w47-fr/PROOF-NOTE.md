# W47 fr 家庭独立重校记录（SOP §8.4）

- 校对员：独立重校，未参与建造；只校对、不修复、不重建、不 commit、不 push、不跑 lint。
- 日期：2026-11-12（EST）。范围：目标语 fr × 读者母语 en de es it ja ko nl pt ru zh-cn zh-tw，共 11 版。
- 依据：`~/workspace/weekly-git/SOP.md` §8 + §1.1；`hidden_files/w47/scratch-d5-plan/D5-PLAN.md` §1。
- 目录核对：fan-out 10 个（`2026-w47-fr-de/en/es/it/ja/ko/nl/pt/ru/zh-tw`）+ `core-fr/`（= fr-zh-cn 版）= 11 版，无多无少。无 `2026-w47-fr-zh-cn` fan-out 目录。

## 结论：(b) 有问题 —— 16 项，全部 minor，无事实错误、无 P8 答案错误、无版式破损

缺陷只分两类，均为讲解层缺失：

### D1（词汇级缺失，1 项）—— fr-ja P1 NOTE 丢了一个词的译注

- 位置：P1，lead 文章下方 NOTE 框（`解説 — …`）。
- 内容：`un vin primeur` 后无日语译注。text.md L45：`> 解説 — le Sénat 上院　un vainqueur 勝者　trancher 決める、裁く　un vin primeur　le beaujolais ボジョレー。`
- 证据（三重交叉）：① SVG `p1-une.svg`：`un vin`（y=1307.2）→ `primeur`（y=1336.93）之间无任何译注元素，下一元素即 `le beaujolais` + `ボジョレー。`；② 印 PDF 提取文本同款缺口；③ 2.5× 放大裁图目视确认（`/tmp/reproof-fr/ja-p1-note2.png`）。④ 对照：en `a new wine`、de `ein neuer Wein`、es `un vino nuevo`、it `un vino novello`、ko `새 와인`、zh-cn `新酒`、zh-tw `新酒` 均有译注；ja 自身 P2 NOTE（L221）亦有 `un vin primeur 新酒`。⑤ CJK 三版机械交叉核查：ja-only 的译注缺口仅此一处。
- 严重度：minor。词义可从 P2 NOTE / P3 词表找回，但 P1 NOTE 本身不完整。

### D2（冠词缺失，1 项）—— fr-zh-tw P2 注释行 `virgule` 丢了 `une`

- 位置：P2，`註｜…` 注释行（text.md L229）。
- 内容：`*註｜virgule 逗號　voter 投票　fêter 慶祝。*`；其余 10 版均为 `une virgule …`（core `une virgule 逗号`）。
- 证据：SVG `p2-vie.svg` 印源：zh-tw 为 `virgule `（x=1030.0），core 为 `une virgule `（x=1050.5）。`virgule` 为阴性名词，丢 `une` 即丢了性标记。
- 严重度：minor。

### D3–D16（栏目标题读者语译注缺失，14 项）

以下 5 个栏目标题在部分版本中只有法文标题、无读者语译注（SVG 印源逐项核查；同位置其他版本均有译注元素）：

| 标题 | 缺失版本 | 位置 |
|---|---|---|
| `CLINIQUE DES ERREURS`（P7） | es、it、ja、ko、nl、pt、ru、zh-tw（8 版） | P7 `### CLINIQUE DES ERREURS` 行，标题后无译注元素；对照 core `易错诊所`、en `ERRORS`、de `FEHLER` |
| `LE CINÉMA DU MERCREDI`（P5） | nl、ru（2 版） | P5 右栏标题行（SVG y=1575.6），标题后无译注元素；对照 en `FILMS`、ja `映画`、zh-tw `電影` |
| `LIRE LE CALENDRIER`（P6） | ru（1 版） | P6 `LIRE LE CALENDRIER` 行（SVG y=1865），标题后无译注元素；对照 en `DATES`、de `KALENDER` |
| `BOÎTE À OUTILS`（P7） | nl、ru（2 版） | P7 `BOÎTE À OUTILS` 行（SVG y=227/225），标题后无译注元素；对照 en `TOOLBOX`、de `WERKZEUG` |
| `DANS CE NUMÉRO`（P1） | ru（1 版） | P1 目录标题行（SVG y=1320），标题后无译注元素；对照 en `IN THIS ISSUE`、ja `目次` |

- 严重度：minor。法文标题仍在、栏目内容均有译注，不影响做题；但与全书“栏目标题配读者语译注”的通例不一致。
- 注：L921 `CLINIQUE DES ERREURS` 在 es/it/ja/ko/nl/pt/ru/zh-tw 的 text.md 中同样无译注后缀，与 SVG 一致，非 text.md 导出问题。

### 逐版缺陷计数

| 版 | 缺陷 | 编号 |
|---|---|---|
| fr-zh-cn（core-fr） | 0 | — |
| fr-en | 0 | — |
| fr-de | 0 | — |
| fr-es | 1 | D-CLINIQUE |
| fr-it | 1 | D-CLINIQUE |
| fr-ja | 2 | D1、D-CLINIQUE |
| fr-ko | 1 | D-CLINIQUE |
| fr-nl | 3 | D-CINÉMA、D-BOÎTE、D-CLINIQUE |
| fr-pt | 1 | D-CLINIQUE |
| fr-ru | 5 | D-DANS-CE-NUMÉRO、D-CINÉMA、D-LIRE、D-BOÎTE、D-CLINIQUE |
| fr-zh-tw | 2 | D2、D-CLINIQUE |
| **合计** | **16** | |

## 校对文件清单（即本次校对的文件；尺寸 + SHA-256 前 12）

| 版 | 印 PDF（8 页） | 网 PDF | text.md |
|---|---|---|---|
| fr-zh-cn（core-fr） | `La-Lucerna-VOL4.pdf` 18,475,436 `f36c32f020e4` | `La-Lucerna-VOL4-web.pdf` 1,985,431 `ff08e74903d6` | `2026-w47-fr-zh-cn.text.md` 46,471 `52024e024d32` |
| fr-en | `La-Lucerna-VOL4-fr-en.pdf` 17,031,641 `0503cff0885d` | 1,622,982 `11e5babac345` | 46,146 `82f53a7aa6af` |
| fr-de | `La-Lucerna-VOL4-fr-de.pdf` 17,035,304 `234a877ebbbb` | 1,626,645 `68c62c41b596` | 46,559 `de37011a23a0` |
| fr-es | `La-Lucerna-VOL4-fr-es.pdf` 17,031,451 `d732ed21b8be` | 1,622,812 `aa1b3076782d` | 46,645 `7c340f2d9ede` |
| fr-it | `La-Lucerna-VOL4-fr-it.pdf` 17,027,791 `5d31cbc41f0a` | 1,619,122 `20b66275d46c` | 46,528 `ac5c096d167c` |
| fr-ja | `La-Lucerna-VOL4-fr-ja.pdf` 20,148,505 `a62d3c89d9a9` | 2,019,098 `bc8eb6e62d2b` | 47,508 `df028d09d5db` |
| fr-ko | `La-Lucerna-VOL4-fr-ko.pdf` 20,086,049 `9aeba6cc400e` | 1,923,039 `98170fbd21ae` | 47,323 `f5474d61eead` |
| fr-nl | `La-Lucerna-VOL4-fr-nl.pdf` 17,029,995 `c0c12aea4176` | 1,621,369 `36493cef193a` | 46,250 `4a4a9fcc9bb5` |
| fr-pt | `La-Lucerna-VOL4-fr-pt.pdf` 17,031,944 `8c01de5f3691` | 1,623,290 `a62233ec10cd` | 46,486 `12a860a9b4e1` |
| fr-ru | `La-Lucerna-VOL4-fr-ru.pdf` 17,331,940 `3459a9b9d3ed` | 1,882,129 `ccfba10759e7` | 50,418 `9aa919b7c647` |
| fr-zh-tw | `La-Lucerna-VOL4-fr-zh-tw.pdf` 18,531,943 `de24f2a08c9b` | 2,074,668 `f54db205afbd` | 45,992 `e5c8c1cd50f0` |

- 印 PDF 均为 8 页。ABSTRACT.txt 11 版齐全，均为读者母语、单行、无 ASCII 双引号（de 231B、en 198B、es 233B、it 210B、ja 245B、ko 250B、nl 207B、pt 233B、ru 365B、zh-tw 203B、core-fr 280B）。
- 练习总数 150（P1 10、P2 15、P3 18、P4 18、P5 17、P6 18、P7 12、P8 42；A2 53 / B1 75 / B2 22；134 个级别徽章）。

## 机械门（全部通过）

- `tools/p8.py compare`（`--core-dir core-fr --edition-dir <版> --target fr --total 150`）：10 个 fan-out 版全部 **CLEAN，121/121 noted，missing=[]，extra_count=0**，keydiff=[150]。Q150 keydiff 为读者语标签差异（core `开放题` vs en `Open question`，开放写作题），按工具说明为提示信息，非失败。**初跑与收尾重跑结果一致**（见 tools/ 状态一节）。
- `tools/occlusion_audit.py`：11 版 **0 flags**，自检通过（全部植入类别均触发）。**初跑与收尾重跑结果一致**。
- D5 字体普查（修正后方法，只计无 `<tspan>` 子元素的直接 `<text>`）：11 版 SVG 中 **0 个拉丁字母、0 个带重音拉丁字母（U+00C0–U+024F）、0 个西里尔字母落在 Noto Sans CJK / Noto Serif CJK 元素内**。弯引号 U+201C/U+201D/U+2019 在 11 版 SVG 与 PDF 文本中均为 **0 次**（法语用 « »，无可路由内容）。D5 修复已生效。`pdffonts`：Newsreader 见于全部版本；fr-ru 另有 Noto Sans Medium/Bold（合 SOP）；Newsreader SemiBold 以 Regular 样式名出现为字体命名特性，非缺陷。
- P8 答案编号连续性（印 PDF 提取文本）：11 版 **1–150 全有，missing=[]**。
- 网 PDF vs 印 PDF 提取文本：11 版**逐字节一致（同一 MD5）**，文本层门通过。
- P8 字号：11 版 P8 下半页（答案区）最小字号均为 **11.62pt ≥ SOP 目标 9.75pt**。
- 核心法语层一致性：core 的 252 行候选法语行（≥25 字符、无 CJK/西里尔）在 10 个 fan-out 版 text.md 中逐字相同。脚本污染检查（印 PDF 提取文本）：拉丁版 0 CJK/0 西里尔/0 假名/0 谚文；ja 仅 CJK+假名；ko 仅谚文（0 CJK）；ru 仅西里尔；zh-tw 仅 CJK。

### tools/ 状态（中途有变，已按任务要求重跑）

- 开工时：repo HEAD `71f4e6f9`，tools/ 有未提交本地修改（`M tools/README.md, tools/cover.mjs, tools/occlusion_audit.py, tools/p8.py, tools/run_build.README.md, tools/run_build.py` + 未跟踪 `tools/d5_creambox_audit.py, tools/head_check.py`）。
- 任务中途：上述修改被提交为 `b9ac29a6`（"tools: D5 gates + p8/occlusion/cover/run_build fixes (W47 review round)"），repo HEAD 现为该提交。
- `tools/p8.py` / `tools/occlusion_audit.py` 文件本身 mtime（2026-11-12 07:54 / 11:11 UTC）早于开工，内容未变；收尾已用提交后的 tools/ **重跑 p8 compare（10 版）与 occlusion（11 版）**，结果与初跑完全一致。

## 事实核验（核心法语内容，逐项核对，全部确认）

- 日期/星期（Europe/Paris）：2026-11-16 一、17 二、18 三、19 四、20 五、21 六、22 日；11-03 二、11-04 三、11-09 一、11-26 四、12-09 三、10-23 五，均与正文一致。
- 网上事实核查（2026-11-12，browser.search）：ATP 总决赛都灵 11 月 15–22 日、半决赛 11 月 21 日（周六）、决赛 11 月 22 日（周日）、抽签 11 月 12 日（周四）、8 人名单（Zverev、Alcaraz、Shelton、Medvedev、Cobolli、Fils、Tiafoe、Jodar）与 Sinner 因膝伤缺席均确认；法国足球意大利–法国 11 月 12 日（周四）20h45 圣西罗、法国–土耳其 11 月 15 日（周日）20h45 波尔多、欧国联 A1 组法国 4 战 10 分、齐达内任主帅确认；Alcaraz 7-6(5)、7-5 胜 Shelton、巴黎大师赛决赛 11 月 8 日（周日）、首冠、第 9 个大师赛 1000 冠、2 号种子、Shelton 3 号种子、Sinner 缺席、第 41 届确认；Sinner 10 月 6 日宣布赛季结束、右膝炎症、缺席巴黎与总决赛、两届卫冕冠军确认；社保预算国民议会 10 月 23 日（周五）115–1 否决收入部分（1 票赞成、22 票弃权）、赤字 21.8→12.7 亿欧元、参议院 11 月 9 日（周一）起审议、正式表决 11 月 18 日（周三）确认；国家预算表决 10 月 20 日→11 月 3 日→11 月 4 日（周三）晚举行、458–0 否决（2 票弃权）、参议院 11 月 20 日起审议、正式表决 12 月 9 日（周三）确认；博若莱采收自 8 月 13 日、农业部预估 Bourgogne-Beaujolais 减产 22%（11 月 1 日预估）、75 周年（1951→2026）、Inter Beaujolais 500+ 活动、Sarmentelles 11 月 18–22 日、11 月 18 日夜间开桶、第三个周四规则自 1985 年、1951 年提前售酒权确认；SERD 11 月 21–29 日、主题 « Passer de l'ultra-conso à la consommation responsable »、ADEME 协调确认；11 月 18 日（周三）上映六部影片（《饥饿游戏：收割日出》Francis Lawrence、2h38、Haymitch 早于 Katniss 24 年；《Les Braves》Lukas Dhont、一战题材；《Jupiter》Alexandre Smia、Denis Ménochet 饰总统对核危机；《Malika》Mounia Meddour、Malika Bellaribi 传记、Lilya Adad；《Camembert》Kristin Scott Thomas + Guillermo Guiz、Trivial Pursuit 喜剧；《Fais-moi un signe》Mipo O、听力正常男孩与聋人父母）全部确认；马赛–勒芒 11 月 22 日（周日）20h45、法甲第 11 轮、韦洛德罗姆确认；Méliès 1861–1938、《月球旅行记》1902、Doré 1832–1883、Hiroshige 1797–1858、Atget 1857–1927、Adrien Moreau 1843–1906、CMP 7 名众议员 + 7 名参议员、黑色星期五 11 月 27 日（周五）、11 月 11 日公众假日、世界儿童日 11 月 20 日确认。
- P8 答案逐题复核：150 题答案键齐全；Q109–150 在 core 通读中逐项核对题面一致（Q109 A lundi、Q112 B goûté、Q113 A propose、Q114 A aimé、Q120 B irais、Q122 B reçoit、Q131 venais、Q134 examine、Q135–139 翻译、Q140–144 a/b/c/d/e、Q145 des billets、Q146 deux、Q147 quelle heure、Q148 devant le、Q149 film、Q150 开放题）。P7 金句全部出自本期（A2 博若莱 P3、B1 ADEME P5、B2 预算 P6），合 SOP §4。P6 虚拟式正确（examiner→examine、voter→vote、changer→change）。P7 诊所纠错正确（Q105 battu、Q106 vote、Q107 examine、Q108 jeudi 19 非 vendredi 20）。
- 两项“核查未定论”，记为非缺陷：① “seize films”（16 部新片）计数——filmscinema.fr 同周列表为 26 项（含活动放映/重映，如 BTS 现场、1928 年《Queen Kelly》），且两次抓取计数不同（17→26），计数取决于收录口径（仅新上映片），无法证实正文为错；② 50 天期限“11 月 26 日（周四）”——官方参议院/主席会议日程自 10 月 8 日起算为 11 月 26 日，正文从之；另一来源（IFRAP）自 10 月 6 日递交日起算为 11 月 25 日，属计数起点口径差异，非事实错误。

## 视觉检查（11 版 × 8 页逐页看图）

- core-fr P1–P8 全页 + 其余 10 版 P1/P8 + P2–P7 全部看过（0.45 比例渲染自印 PDF，`/tmp/reproof-fr/<版>/p1–p8.png`；/tmp 为临时文件）。无溢出、无重叠、无压页脚、无豆腐块、无截断句。
- P1 刊头 + 配对徽章、页脚配对标注：11 版齐全正确。P8 答案流完整到页底，无压脚。
- fr-ru P5 debat5_note 独立复核：2× 放大裁图（`/tmp/reproof-fr/ru-p5-debat.png`）确认 débat 注释（法文提问 + 俄文译注 `Кино или дома? …`）完整在框内、下方留白充足；**此前 creambox 3 旗标确为测量误报，不重报为缺陷**。
- 补充放大核查：ja P1 NOTE（2.5×，D1 目视确认）；zh-tw P1 标题栏（2.5×，见下）。

## 已排除的疑点（查过、不列为缺陷）

- zh-tw / core-fr P1 标题栏：实测印 PDF 中译注首字 bbox 与标题末字母 bbox 重叠 1.1pt（标题 x1=1071.3，译注 x0=1070.2）；但 8× 放大裁图（`/tmp/reproof-fr/zhtw-junction.png`）显示字形无碰撞——“阿”字左部完整，与 MERCREDI 的 "I" 之间有可见间隙，重叠量被字间距吸收。**版式紧但干净，不列为缺陷**。ja（间隙 +140.7pt）、ko（+26.0pt）无此问题。
- ja L319 `## CULTURE　文化`、L397 `une bouteille — 瓶`：与 core 逐字相同，但 文化/瓶 均为合法日文汉字，非中文残留；ko L397 为 `une bouteille — 병`（谚文），ko 版印 PDF 文本 0 CJK 字符。zh-tw 与 core 相同的 29 行均为繁简同形字（填空、葡萄酒、瓶、杯、葡萄、酒窖、加油、青年、工具箱、完形填空、第 1–8 版等），属预期内。
- de P1 标题译注 `SENAT STIMMT MI.`：`MI.` 为 Mittwoch 的标准德语缩写（同 es `MIÉRC.`、it `MERC.`、nl `WO.`），非截断。
- 各版 P1 标题译注、P8 Hiroshige 秋叶图配文（`Novembre, près d'Edo… Utagawa Hiroshige (1797-1858), estampe, domaine public LACMA`）均为装饰性配文，无事实问题；P8 MODÈLE 范文 `une photo de Méliès dans la tête` 为范文风格选择，非错误。
- 各版讲解层小幅意译（如 de `Quelle action!` → `Was für ein Ballwechsel!`、ru Q135 `Смотреть финал: учить французский`、pt/zh-tw `se terminer en beauté`）均为风格松紧，非缺陷。

## 工作文件

- 本记录：`hidden_files/w47/scratch-reproof-w47-fr/PROOF-NOTE.md`。
- 工作目录 `hidden_files/w47/scratch-reproof-w47-fr/work/`：各版 pdftotext 提取文本、line-parallel text.md diff（`md-diff-<版>.txt`，讲解层通读依据）、`census2.py`（修正后 D5 普查）、`occl-<版>.json`（occlusion 输出）。`census.py` 首版有 bug（误报拉丁入 CJK），已废弃，勿用。
- 渲染图在 `/tmp/reproof-fr/`（临时，VM 重启即失；可从印 PDF 用 venv PyMuPDF 重渲）。
- 磁盘：收尾时 /home/hatch 93G/150G（63%），未触 100G 门限。

## 未做事项

- 未修复任何问题（只记录）；未重建、未 commit、未 push、未跑 lint、未碰其他周次；未改动 `production/2026-w47/` 内任何文件。
