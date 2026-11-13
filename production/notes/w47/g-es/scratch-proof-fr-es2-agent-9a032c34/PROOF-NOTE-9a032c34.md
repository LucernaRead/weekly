# PROOF-NOTE — W47 fr-es proof2（独立复校，re-fanout #2 重建版）

复校员：proof2（独立）。复校日期：2026-11-11。解释器一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
生产目录零写入：全部重建/渲染在本人 scratch 内完成；开工前与收尾时三件 SHA 逐值复核一致。

**工作区**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-es2/`
（下文 `S/` 即此目录；门禁日志见同目录 `GATE-LOG.md`，两文件缺一结论无效。）

## 结论：(a) 零缺陷，可定稿

**缺陷 0 项。** #1 唯一缺陷 D-1（P7 披露框溢出 +2.6）已按规定修法根除，Q148 已按 core fix4 落地，
全部 15 门独立重跑通过，150 键逐项手核零不适配，8 页逐页目视干净，回归封闭（仅 P7/P8 改动）。

| 件 | 大小 | SHA-256（开工前 = 收尾时，逐值核对） |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-fr-es.pdf` | 17,418,347 B | `77488ab05a39b269b38f16ebb0da59e500d1c9b8739e77a3ca3a9387712104f4` |
| 网页 PDF `La-Lucerna-VOL4-fr-es-web.pdf` | 1,701,681 B | `2e56003e9353fb3de400b27d9e6700e5ad834007e6be07b0dbe758442efbf0b3` |
| `.text.md` | 46,660 B | `096402b410eccd1f3d0cbcdd5cc786ec82815c967eaa0312157cd7b9b49a1d7f` |
| 核心对照 core-fr（印/网/文） | 30,446,975 / 2,241,835 / 46,471 B | `a30af667…25a9d` / `56f50ca8…58e141` / `52024e02…63df`（与任务书一致） |

SVG 8 页 SHA（前 8 位）：p1 `bd6a40f0`、p2 `220dd45e`、p3 `1b39fa5b`、p4 `dd5ec45e`、
p5 `51b18d6f`、p6 `c3f18dcd`、p7 `75d2252b`、p8 `aa084df5`。

## 1. 本版必查逐项复核

### 1.1 P7 披露框（#1 缺陷 D-1 的修复验证）——已根除

- 源码：`expl.py` `courrier_disclosure` 删中句（`este número publica un ejemplo editorial marcado.`），
  3 行→2 行；新句（`expl.py:182`）：`Nota de la redacción: al cierre no había llegado ningún texto del VOL.4. El VOL.5 cumplirá la promesa de comentar envíos reales.`
- creambox（canonical `hidden_files/w47/tools/creambox.py`，8 页全扫，`S/creambox.log`）：
  P7 披露盒（y=1878，框底 2258.0）末基线 **2233.3**，清除 **+24.7**，desc-clear **+18.8**，
  末行 `promesa de comentar envíos reales.`；P7-TOOLBOX 小结：4 盒，最小盒内清除 +24.7、最小 desc-clear +18.8。
  全书 7 条 BELOW-WINDOW 均为 +24.0/+37.0 的下一栏目标题假阳性（与 #1 同模式，盒内末行清除 ≥+47.7）。
- PIL 真墨（印刷版 PDF，200 dpi，`S/pil_p7.py` 复用 + 自写全色扫描）：
  披露灰墨（#6f675d）末行 **2237.3**（报告值 2237.3 一致）；**2258–2270 间隙零墨**（灰墨扫描与全色深墨扫描均为 NONE）。
  200 dpi 盒底裁切 `S/png/crop-p7-boxbottom.png` 目视：披露 2 行完整在奶油盒内，下方白纸间隙干净，绿带未被侵入。
- 对照 #1：旧版末基线 2260.6（+2.6 溢出）已消失；新旧 P7 SVG 哈希 `c7fc6d9e`→`75d2252b`。

### 1.2 Q148——三重核对全部通过

- P8 SVG 文本层：题干 `On se retrouve (148)___ cinéma ?`（joined 全文检索，`du cinéma` 出现 0 次）；
  答案区 `148. devant le (Delante del cine)`。
- `content8.py:170` 键 `devant le`；`:176` 题干含 `On se retrouve ({gnums[3]})___ cinéma ?`（无 `du`）。
- `p8.py extract` 提取 Q148 = `devant le`；核心 `final-fr-p8.json` Q148 = `devant le`。
- 语义：`devant le cinéma`（在电影院前面）与注记 `Delante del cine` 一致，题干适配。
- P8 目视：对话区 `(148)___ cinéma ?`、答案区 `148. devant le` 均清晰（`S/png/p-8.png`）。

### 1.3 孤儿标点全扫——新增 0

修正后 `check_extra.py`（同基线判定版，本人 scratch 副本，`S/check_extra.py`，`S/extra.log` /
`S/es/extra-proof2.json`）：**元素总数 0 新增、0 核心继承、0 记录残留、0 字体分拆同基线**（exit 0，`EXTRA PASS`）。
（es 为拉丁版，无西里尔/假名分拆元素；检测器本身已在 ru/ko 上验证过同基线逻辑。）

### 1.4 孤行填空线 Q130 / Q36 / Q37——观察类，核实与核心坐标关系

| 处 | 核心 | es 版 | 关系 |
|---|---|---|---|
| P8 Q130 | (989.0, 843.0) | (989.0, 843.0) | 分毫不差 |
| P3 Q36 | y=1864.7, x=538.5 | y=1924.1, x=538.5 | **+59.5**（任务书 es 档） |
| P3 Q37 | y=1997.4, x=538.5 | y=2056.8, x=538.5 | **+59.5**（任务书 es 档） |

三处与核心同位关系与任务书一致，未修核心、不判 (b)。目视：P3 Q36/Q37 的独行 `___` 在练习流内，
P8 Q130 的独行 `___` 为 D 节首句换行（`S/png/p-3.png`、`S/png/p-8.png`）。

### 1.5 150 键逐项手核 key-vs-stem——零不适配

方法（Q73 教训：三源一致也可能同错，故不只比三源）：本人 scratch 重跑注册表
（`S/regdump/` + `S/reg.json`，TOTAL 150）→ 逐项对题干/选项/正文事实。
证据表：`S/key-stem-table-MINE.txt`（150 行，n / 页 / 级别 / 类型 / 键 / 注记 / P8 提取 / 核心键）。

- 三源交叉：REG 键 = P8 提取键 = 核心键，**149/150 全同，仅 Q150 例外**（核心 `开放题` → es
  `Pregunta abierta — puntos en el recuadro; modelo en el recuadro de la página 8`，写作题读者语说明，预期内；
  P8 印出短键 `Pregunta abierta`）。
- 配对题逐项验选项（SVG 选项列原文）：Q22–25（a. la décision ensemble→vote；b. un vin de l'année→primeur；
  c. ce qu'on jette→déchet；d. le dernier match→finale）、Q49–52（forfait/tableau/tirage/trêve）、
  Q73–76（prequel/bande-annonce/seconde main/atelier）、Q85–88（sénateur/rejeter/vote/commission）、
  Q140–144（sénateur/vainqueur/tirage/primeur/déchet）——字母与定义逐一对应，**Q73 a 正确**。
- 选择题逐项验选项行（`.text.md` 选项原文 + 正文事实）：Q7–10（A/B/A/B）、Q19–21（C/B/A）、Q41（B cépage）、
  Q44–48（B/A/C/A/A；Q48 依据 P4 正文「11e journée se jouera du 20 au 22 novembre」→ A. vendredi 20 正确）、
  Q62–66（B/B/B/A/A；Q64 B. Lukas Dhont）、Q79–84（B/B/B/B/**C**/B；Q83 依据 P6 日历「9 déc. Vote solennel :
  le budget de l'État」+ 正文「le vote est prévu le 9 décembre」→ C. 9 déc. 正确；Q79/Q80 依据日历行
  「23 oct. Rejet 115–1」「4 nov. Rejet 458–0」；Q84 依据「26 nov. Fin du délai de 50 jours」→ B）、
  Q109–116 完形（A/B/A/B/A/A/B/A，逐句验 cloze 短文：109 lundi（11 月 16 日确为周一）、110 Beaujeu、
  111 résultats、112 goûté、113 propose、114 aimé、115 jouent、116 écrit）、Q117–124（A/A/B/B/A/B/A/C）、
  Q125–129 阅读（A/A/A/A/A，逐句验 Martin 一家短文原文）。
- 填空/改写/翻译/对话逐项验法语正误：Q15–18 futur proche、Q35–37 否定改写、Q53–55 比较级、
  Q89–96 动词形（Q93 `ont rejeté`、Q94 `part` 均与 P6 正文逐字对应）、Q97–104 跟练、Q105–108 改错整句、
  Q130–134 完成句、Q135–139 翻译整句、Q145–149 对话（Q147 `quelle heure`、Q149 `film`）。
- Q72 注（`acheter`）沿用核心冻结内容，句式成立，不列为缺陷（与 #1 同断）。

## 2. 全部门禁结果摘要（详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| 独立重建 run.py（scratch 副本） | rc=0，TOTAL 150，零 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE；SVG 8/8 与生产逐位相同 |
| gates 15 门（`gates-proof.py es proof2` 独立重跑） | **15/15 PASS**，exit 0（`S/gates-proof2.json`，`S/es/gates-proof2.log`） |
| freeze baseline（core-fr） | **8/8 byte-identical**，核心 shipped SVG 完整性复核未变 |
| freeze diff（core vs edition） | 新增 CJK 10 个，全部 U+3000（p3 +1、p6 +1、p8 +8）；零新增汉字/假名/韩文 |
| p8 extract + compare | 150/150 键，注记 121/150；**CLEAN，keydiff [150]** |
| keycheck（registry vs P8 extract vs core） | 149/150 同，仅 Q150 例外（写作题读者语说明） |
| occlusion audit（真实命令，无 --selftest） | **0 flags**；自检 planted 6 类全触发、干净对照静默 |
| creambox（canonical，8 页） | P7 披露盒 +24.7（见 §1.1）；其余 BELOW-WINDOW 均为假阳性 |
| spill sweep（本人 PIL 真墨扫，盒边穿越 + 横向溢出 + 盒外触碰） | **0 flags / 8 页**；核心对照 0；阳性对照（#1 旧 P7）检出 EDGE-B 墨 2243.6..2260.9 越框底 2258.0（扫法非空转） |
| print/web 文本层比对 | pdftotext **byte-equal，104,934 B**；web 1,701,681 B < 7 MB；web PDF 只在 scratch 渲染比对，未动生产文件 |
| P8 最小字号 | PDF span 实测 **11.625pt** ≥ 9.75pt；SVG 文本最小 15.5pt |
| §1.1 适配检查（本人 `s11_fr_mine.py`） | PASS：纸色 #fbfaf6 ×8、色集与核心同为 19 色零出入、三档徽章齐全、P8 四头齐全、SVG 文本层零真实 CJK（仅 U+3000，362 个）；P6 VOL.5 计数差已裁定（见 §4 观察项 5） |
| check_s11.py / verify_ed.py | **fr 族无此二工具**：全仓与 hidden_files/w47 检出的副本均为 en 族（core-en、p8-test.svg、registry.json），无法在 fr-es 上运行；其检查意图由 gates 15 门 + 本人 s11 适配脚本覆盖（见 GATE-LOG §7） |
| SVG 零真实 CJK | 文本元素层：仅 U+3000（p1 35 / p2 28 / p3 20 / p4 27 / p5 22 / p6 25 / p7 15 / p8 190，与 #1 一致）；`.text.md` CJK 仅 U+3000，U+2019=0，U+00B7=0 |
| D5 字体 | 只记录不判定：讲解层拉丁字符全部落在 Noto Sans CJK SC（与 #1 相同，全周级待用户裁定问题） |
| 回归对照（vs #1 备份） | 见 §3 |

## 3. 与 #1 备份回归对照（KEEP/REVERT 盘点）

- SVG 逐页哈希：P1–P6 **byte-identical**（`bd6a40f0` / `220dd45e` / `1b39fa5b` / `dd5ec45e` / `51b18d6f` / `c3f18dcd`），
  仅 P7（`c7fc6d9e`→`75d2252b`）、P8（`20df945f`→`aa084df5`）改动。
- 源码 diff（仅 2 文件）：`expl.py:182` 删 `courrier_disclosure` 中句（D-1 规定修法）；
  `content8.py:170` 键 `devant`→`devant le`、`:176` 题干删 `du`（core fix4）。
  其余 `content12/34/56/7.py`、`bslib4.py`、`svglib.py`、`run.py`、`render.py` 全部 identical。
- `.text.md` diff 恰为 3 行：披露句、Q148 题干、Q148 答案行（`148. devant`→`devant le`）；`ABSTRACT.txt` identical。
- **KEEP/REVERT：#1 复校只报 1 项缺陷 D-1，无其他 hand patch 需要保留或回退。**
  两处源码改动与两项规定修复一一对应，无丢失、无多余改动、无回退。

## 4. 观察项（非缺陷，仅记录）

1. Q130 / Q36 / Q37 独行填空线（见 §1.4）：核心继承的版式，坐标关系符合任务书 es 档。
2. P2 `ET VOUS ?` 盒末行下行尖触盒边：desc-clear −1.6；核心版同盒 −2.2（比本版更紧）——核心继承，100 dpi 目视无漫出感。
3. P1 agenda 盒：末行清除 +8.0 / desc-clear +2.3，与核心版逐值相同。
4. 沿用值（#1 已记）：P6 `head_lire` 为 `LIRE LE CALENDRIER　HORARIO`（宽松意译）；P3 `Minidrills` 标签未译；
   P8 注记配对键格式混用 `=` 与 ` = `（如 Q140 `sénateur = senador　a` 与 Q141 `vainqueur=ganador b`）；内容均正确。
5. P6 VOL.5 计数差（es 1 vs 核心 0）：`chart_note` 译法差异——核心「本页日程为计划安排，18 日投票结果下期跟进。」
   （`expl.py:129`）译为 es「Calendario previsto; el resultado de la votación del 18 nov. en el VOL.5.」
   （`expl.py:128`），「下期」显化为 VOL.5，属合法翻译；gates string_freeze 亦将其计为 1 例外（excused）。
6. P1 嵌套 moth 品牌 SVG 内含 `<title>Lucerna 三色蛾</title>`（核心版亦同，非渲染文本元素；文本层 CJK 扫描不受影响）。
7. P3 `POUR OU CONTRE ?` 框无西班牙语行、P5 `debat5_note` 出现两次——均与核心版一致（KIT 已披露）。

## 5. D5 字体问题（全周级待定项，如实记录，不据此判 (b)，不擅自修）

网页版 PDF（PyMuPDF span 实测，8 页）：

- 全部西班牙语讲解层落在 **Noto Sans CJK SC**：`Votación del Senado…`（Reg, 14.25pt）、
  `envíos reales.`（Reg, 14.62pt）、页眉 `EXPLICACIONES EN ESPAÑOL`（Reg, 12.75pt）；
- 法文导读标题 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI` 亦为 NotoSansCJKSC-Bold（34.5pt）；
- 法文正文为 Newsreader（`Dimanche 8 novembre, Carlos Alcaraz…` Reg, 18.0pt）。
- 与 #1 实测一致，属 SOP §1.1 全周级待定项，记录在案。

## 6. 八页逐页目视（印刷版 PDF，100 dpi 全页 + P7 盒底 200 dpi 裁切）

渲染件：`S/png/p-1.png`–`S/png/p-8.png`（本人 pdftoppm，自 verified SHA 的印刷 PDF 渲染）、
`S/png/p7-200.png`、`S/png/crop-p7-boxbottom.png`。

- P1：干净。导读条法文标题止 1236.9 / 西班牙语行起 1299.7；Atget 图注完整；Nota 盒、LES DATES 盒、LE VOTE EN TROIS PHRASES、EN BREF、QUIZ ÉCLAIR Q7–10 均干净。
- P2：干净。Nota 盒、Châtillon 图、LE SAVIEZ-VOUS ?、ET VOUS ? 盒、DIRE LA FECHA、EXERCICES Q11–25（含 22–25 选项 a–d）均干净。
- P3：干净。ZOOM 框、DATES À RETENIR、LES MOTS DU VIN、Moreau 图注、Q26–43（含 Q36/Q37 独行填空线）均干净。
- P4：干净。LES CHIFFRES DU SPORT、LES MOTS DU TENNIS、À SUIVRE、MICRO-DRILLS Q56–61、LE DÉBAT、Q44–52 均干净。
- P5：干净。Méliès 图注、Q62–66（含 Q64 B. Lukas Dhont）、Q67–72、Q73–76 选项 a–d、Q77–78 对话、OÙ SORTIR、LE CINÉMA DU MERCREDI 均干净。
- P6：干净。LE CALENDRIER 全 7 行 + 来源行（含 chart_note VOL.5 行在盒内）、LIRE LE CALENDRIER Q79–84、LES MOTS Q85–88、LE COMPARATIF、MICRO-DRILLS Q92–96、TROIS DATES、APRÈS LE VOTE 均干净。
- P7：干净。语法四栏、三 LA PHRASE EXEMPLE 盒、Doré 图注、LES PHRASES DE LA SEMAINE Q97–104、CLINIQUE DES ERREURS Q105–108、LE COURRIER DES LECTEURS 披露 2 行在盒内、LA SEMAINE PROCHAINE 深绿带均干净。
- P8：干净。A–H 全部题区（含 G 对话 `(148)___ cinéma ?`）、MODÈLE、RÉPONSES 121 条注记（含 `148. devant le`）、Hiroshige 图注均完整。

## 7. 需向协调员说明的事项

1. **并行冲突（同一 scratch 目录）**：复校期间发现另一进程在同一专属目录 `scratch-proof-fr-es2/` 内并行作业
   （文件：`png/p1.png`–`p8.png`、`png/crop-p7-mailbox.png`、`png/crop-p6-calendar.png`、`key-stem-table.txt`、
   `check_extra_run.py`、`pil_spill.py` + `pil-spill.log`、`check_s11_fr.py` + `check_s11_fr.log`；
   截稿时仍在运行 `pil_spill.py es`，PID 21189）。本人未使用、未修改其中任何文件；
   本报告全部证据均出自本人创建的文件与命令（以 `p-*.png`、`*-MINE.txt`、`s11_fr_mine.py`、
   `sweep_spill.py`、`es/build-proof2.log` 等区分）。唯一交叉点：门禁 runner  gate 1 读取的 scratch 根目录
   `build-proof2.log` 为对方放置的 builder 日志副本——本人独立构建日志 `es/build-proof2.log`
   （rc=0、TOTAL 150、零溢出）与之结论一致，门禁结论不受影响。建议协调员核查是否重复派单。
2. fr 族无 `check_s11.py` / `verify_ed.py`（见 §2 表格行）——非本人遗漏。
3. 生产目录零写入；未 commit、未 push。

## 8. 报告文件

- 本文件：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-es2/PROOF-NOTE.md`
- 门禁日志：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-es2/GATE-LOG.md`
- 证据：`gates-proof2.json`、`es/gates-proof2.log`、`es/build-proof2.log`、`es/p8-proof2.json`、
  `p8compare-proof2.json`、`occlusion.json`、`occlusion.log`、`creambox.log`、`spill.log`、`spill-core.log`、
  `extra.log`、`es/extra-proof2.json`、`freeze/freeze-baseline.log`、`freeze/freeze-diff.json`、
  `freeze/freeze-diff.log`、`print-proof2.txt`、`web-proof2.txt`、`mcq-proof2.log`、`s11.log`、
  `reg.json`、`key-stem-table-MINE.txt`、`sweep_spill.py`、`s11_fr_mine.py`、`check_extra.py`、
  `png/p-1.png`–`png/p-8.png`、`png/p7-200.png`、`png/crop-p7-boxbottom.png`
