# PROOF-NOTE — W47 fr-nl 独立复校 proof1（re-fanout #2 重建版）

- 版：`production/2026-w47/2026-w47-fr-nl/`（法语目标、荷兰语读者版，VOL.4）
- 复校员：独立复校 proof1（与重建者不同人），2026-11-11
- 工作区 `S/` = `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-nl2/`
- 只读复校：未改任何生产文件，未 commit/push。开工前与收尾时三 SHA 逐值复核一致。
- 解释器一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 指到 `S/tmp/`。

## 结论：(a) 零缺陷，可定稿

**缺陷 0 项。** #1 唯一缺陷 D-1（P7 披露框溢出）已按规定修法根除；Q148 已按 core fix4 落地；
15 门独立重跑 15/15 通过；150 题 key-vs-stem 逐题手验 150/150 正确；8 页 200 dpi 逐页目视干净；
回归封闭（仅 P7/P8 改动，改动与两项规定修复一一对应）。

| 件 | 大小 | SHA-256（开工前 = 收尾时，逐值核对） |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-fr-nl.pdf` | 17,418,792 B | `3b0073cc94bcfb42d9a0ecdd5cd9bbc2b3d7b5846d2f62e82db5be4c9b6957ee` |
| 网页 PDF `La-Lucerna-VOL4-fr-nl-web.pdf` | 1,699,714 B | `5217c87ac893a6b0bd89a7066d1c28acf0ff1aa780c4522114fa5360309b18b7` |
| `.text.md`（`2026-w47-fr-nl.text.md`） | 46,265 B | `d83b5831b235a7b8a9efad5343d996fc85c70d16400eed7250beb4eb4bb5ee28` |
| 核心对照 core-fr（印/网/文） | 30,446,975 / 2,241,835 / 46,471 B | `a30af667…25a9d` / `56f50ca8…58e141` / `52024e02…63df`（与任务书一致） |

SVG 8 页 SHA（前 8 位）：p1 `984a2867`、p2 `1f619509`、p3 `4ef160c4`、p4 `c9b59871`、
p5 `f2342e2a`、p6 `ce2141d5`、p7 `4eb69452`、p8 `467885cd`。

## 缺陷清单

**无。0 项缺陷。**

## 1. 本版必查逐项复核

### 1.1 P7 披露框（#1 缺陷 D-1 的修复验证）——已根除

- 源码：`expl.py:182` `courrier_disclosure` 删中句，3 行→2 行。被删中句原文（逐字）：
  `daarom drukken we een duidelijk gemarkeerd voorbeeld van de redactie af;`
  （重建报告作意译 `dit nummer drukt een gemarkeerd redactievoorbeeld.`，义同，非原文）。
  新句：`Opmerking van de redactie: bij het ter perse gaan was er geen tekst van VOL.4 binnen; VOL.5 lost de belofte in om echte inzendingen te bespreken.`
  全文 grep `dit nummer drukt` / `gemarkeerd voorbeeld` 0 命中，中句确已删除。
- creambox（canonical `hidden_files/w47/tools/creambox.py`，8 页全扫，`S/creambox-proof1.log`）：
  P7 披露盒（y=1878，框底 2258.0）末基线 **2233.3**，清除 **+24.7**，desc-clear **+18.8**，
  末行 `VOL.5 lost de belofte in om echte inzendingen te bespreken.`——与报告值逐值一致。
- 与核心同盒逐值核对（`S/creambox-core.log`）：core-fr 同盒（y=1878 / bottom=2258.0）
  末基线 **2233.3**，清除 **+24.7**，desc-clear **+18.8**——三值与本版**分毫不差**。
- PIL 真墨（印刷版 PDF，200 dpi，`S/pil_p7.py`）：披露灰墨（#6f675d）末行 **2237.8**
  （报告值 2237.8 一致）；**2258–2270 间隙灰墨 NONE**；自写全色扫描：间隙内深墨（全通道 <150）行 NONE，
  唯一近白像素为盒边抗锯齿 (250,248,244)；绿带本体 (54,63,47) 自 y≈2270 起，与间隙无关。
- 目视：200 dpi 盒底裁切 `S/png/crop-p7-boxbottom.png`——披露 2 行完整在奶油盒内，
  下方白纸间隙干净，绿带未被侵入。#1 旧版末基线 2260.6（+2.6 溢出）已消失；
  新旧 P7 SVG 哈希 `037b5c49`→`4eb69452`。

### 1.2 Q148——三重核对全部通过

- P8 SVG 文本层：题干 `On se retrouve (148)___ cinéma ?`（joined 全文检索，`du cinéma` 出现 0 次）；
  答案区 `148. devant le (Voor de bioscoop)`。
- `content8.py:170` 键 `"devant le"`；`:176` 题干含 `On se retrouve ({gnums[3]})___ cinéma ?`（无 `du`）。
- `p8.py extract` 提取 Q148 = `devant le`；核心 `final-fr-p8.json` Q148 = `devant le`。
- 语义：`devant le cinéma`（在电影院前面）与注记 `Voor de bioscoop` 一致，题干适配。
- P8 目视：对话区 `(148)___ cinéma ?`、答案区 `148. devant le` 均清晰（`S/png/p-8.png`）。

### 1.3 孤儿标点全扫——新增 0

修正后 `check_extra.py`（同基线判定版，本人 scratch 副本，`S/check_extra.py`，
`S/nl/extra-proof1.json` / `S/nl/extra-proof1.log`）：**EXTRA PASS**，
orphan elements total=0 new=0 inherited=0 remnant=0 shared_baseline=0。

### 1.4 孤行填空线 Q130 / P3 Q36 / Q37（观察项，非缺陷）

`check_extra.py` 实测（与核心同法）：

| 处 | 核心 | 本版 | 关系 |
|---|---|---|---|
| P8 Q130 | (989.0, 843.0) | (989.0, 843.0) | **分毫不差** |
| P3 Q36 | (538.5, 1864.7) | (538.5, 1924.1) | **+59.5**（任务书 nl 档） |
| P3 Q37 | (538.5, 1997.4) | (538.5, 2056.8) | **+59.5**（任务书 nl 档） |

三处与核心同位关系与任务书一致，未修核心、不判 (b)。目视：P3 Q36/Q37 的独行 `___` 在练习流内，
P8 Q130 的独行 `___` 为 D 节首句换行（`S/png/p-3.png`、`S/png/p-8.png`）。

### 1.5 150 键逐项手核 key-vs-stem——零不适配

方法（Q73 教训：三源一致也可能同错，故不只比三源）：本人 scratch 重跑注册表
（`S/regdump/` + `S/regdump/reg.json`，TOTAL 150）→ 逐题读 `.text.md` 全 1087 行题干/选项/正文事实核对。
证据表：`S/key-stem-table-MINE.txt`（150 行，n / 页 / 级别 / 类型 / 键 / 注记 / P8 提取 / 核心键）。

- 三源交叉：REG 键 = P8 提取键 = 核心键，**149/150 全同，仅 Q150 例外**（核心 `开放题` → nl
  `Open vraag — punten in het kader; model in het kader op pagina 8`，写作题读者语说明，预期内；
  P8 印出短键 `Open vraag`）。137–139 为与核心相同的翻译键，仅键的写作形式为读者语——已实测确认，
  非照抄预期：Q137 `Nous suivons le vote du Sénat depuis lundi.`、Q138
  `Ce soir, nous allons préparer nos affaires.`、Q139 `On ne connaît pas encore les résultats.`
  均与三源一致且与荷兰文提示逐句配对。
- 配对题逐项验 SVG 选项列原文（字母直接附在选项行上，非只信注册表）：Q22–25（a. la décision
  ensemble→vote；b. un vin de l'année→primeur；c. ce qu'on jette→déchet；d. le dernier match→finale）、
  Q49–52（a. ne pas jouer→forfait；b. la liste des matches→tableau；c. le sort qui fait les
  groupes→tirage；d. la pause entre deux séries→trêve）、Q73–76（a. un film qui raconte l'avant→prequel；
  b. la courte vidéo→bande-annonce；c. acheter des objets déjà utilisés→seconde main；d. le lieu où l'on
  répare→atelier）、Q85–88（a. un élu du Sénat→sénateur；b. dire non→rejeter；c. la décision
  ensemble→vote；d. le groupe qui prépare→commission）、Q140–144（a. sénateur；b. vainqueur；c. tirage；
  d. primeur；e. déchet）——字母与定义逐一对应，**Q73 a 正确**。
- 选择题逐项验选项行（`.text.md` 选项原文 + 正文事实）：Q7–10（A/B/A/B）、Q19–21（C/B/A）、Q41（B cépage）、
  Q44–48（B/A/C/A/A；Q48 依据 P4 正文「11e journée se jouera du 20 au 22 novembre」→ A. vendredi 20 正确）、
  Q62–66（B/B/B/A/A；Q64 B. Lukas Dhont）、Q79–84（B/B/B/B/**C**/B；Q83 依据 P6 日历「9 déc. Vote solennel :
  le budget de l'État」+ 正文「le vote est prévu le 9 décembre」→ C. 9 déc. 正确；Q79/Q80 依据日历行
  「23 oct. Rejet 115–1」「4 nov. Rejet 458–0」；Q84 依据「26 nov. Fin du délai de 50 jours」→ B）、
  Q109–116 完形（A/B/A/B/A/A/B/A，逐句验 cloze 短文：109 lundi（11 月 16 日确为周一，文中亦称 Lundi 16）、
  110 Beaujeu、111 résultats、112 goûté、113 propose、114 aimé、115 jouent、116 écrit）、Q117–124
  （A/A/B/B/A/B/A/C）、Q125–129 阅读（A/A/A/A/A，逐句验 Martin 一家短文原文）。
- 填空/改写/翻译/对话逐项验法语正误：Q15–18 futur proche、Q35–37 否定改写
  （`Le vin ne se vend jamais…` / `On ne boit pas d'alcool…` / `Le beaujolais n'est pas un vin blanc.`）、
  Q53–55 比较级、Q89–96 动词形（Q93 `ont rejeté`、Q94 `part` 均与 P6 正文逐字对应）、Q97–104 跟练、
  Q105–108 改错整句、Q130–134 完成句、Q135–139 翻译整句、Q145–149 对话（Q147 `quelle heure`、Q148
  `devant le`、Q149 `film`）。
- 荷兰文讲解抽查无误：`trancher = beslissen, afkappen; afsnijden`；`Plechtige stemming: wo. 18 november`；
  `Vroege verkoop sinds 1951, derde donderdag sinds 1985, 75e jubileum in 2026.`；
  `titelverdediger / loting / bevestigen / pauze / speeldag`；
  `Bioscoop of thuis? Een oud kledingstuk krijgt een nieuwe eigenaar, of belandt in de vuilnisbak?`；
  `Onderscheid prévu (gepland) van décidé (besloten).`；P7 `sortir: in première gaan.` 与 P8 注记 Q102
  `sortir = uitkomen` 各在其语境正确（影院释义 vs 通用释义）；Q114 注记 `avoir + deelwoord (geen ovk.)`
  语法正确（宾语在后，无配合）；披露句荷兰文与法文原句义同；`Geplande kalender; uitslag van 18 volgt in
  het volgende nummer.` 为核心「下期跟进」的忠实翻译（未用 VOL.5 字样，故 s11 VOL 计数与核心无差）。

## 2. 盒标题 PIL 真墨 + 溢出扫（任务项 2）

- sweep（本人 `S/sweep_spill.py`，PIL 真墨 `occlusion_audit.ink_box`，8 页全部奶油框 × 全部文本）：
  **TOTAL FLAGS: 1**（见观察项 O1）；其余 7 页 0。核心对照 0。阳性对照（#1 旧 P7，`S/oldp7/`）：2 flags
  （EDGE-B 墨 2244.9..2265.6 越框底 2258.0；TOUCH-OUT）——扫法能检出旧缺陷，新版 0/1 不是空转。
- 盒标题逐一 PIL 真墨（本人 `S/boxtitle_pil.py`，每奶油盒取顶行标题 + 盒内全部粗体行，墨边距四向实测）：
  **69 项量测，0 flags**。最紧值：左 16.0、右 21.9、上 17.5、下 43.5（全部为正，见 GATE-LOG 盒标题 clear 表）。
- 最紧三处交付 PDF 渲染像素交叉验证（200 dpi，印刷版 PDF）：
  P7 披露盒（见 §1.1，间隙深墨 NONE）；P3 DATES 盒（见观察项 O1，裁切 `S/png/crop-p3-dates-bottom.png`）；
  P2 ET VOUS 盒（见观察项 O2，裁切 `S/png/crop-p2-etvous-bottom.png`）；P1 agenda 盒
  （desc-clear +2.3：间隙 1256..1270 深墨 NONE，下一盒标题墨始于 1299.8，44px 之下，无侵入）。

## 3. 全部门禁结果摘要（详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| 独立重建 run.py（scratch 副本 `S/rerun/`） | rc=0，TOTAL 150，零 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE；SVG 8/8 与生产逐字节相同 |
| gates 15 门（`gates-proof.py nl proof1` 独立重跑） | **15/15 PASS**，exit 0（`S/gates-proof1.json`，`S/nl/gates-proof1.log`） |
| freeze baseline（core-fr，标准口径） | **8/8 byte-identical**，核心 shipped SVG 完整性复核未变 |
| freeze baseline（版内自比对） | **8/8 byte-identical**（`984a2867…467885cd` 与生产一致） |
| freeze diff（core vs edition） | 新增 CJK 8 个，全部 U+3000（仅 p8）；零新增汉字/假名/韩文 |
| p8 extract + compare | 150/150 键，注记 121/150；**CLEAN，keydiff [150]**（直接读 `S/p8compare-proof1.json` 本体：missing/extra/uncertain 全空） |
| keycheck（registry vs P8 extract vs core） | 149/150 同，仅 Q150 例外（写作题读者语说明） |
| occlusion audit（真实命令，无 --selftest） | **0 flags**；工具内置自检 planted 6 类全触发、干净对照静默 |
| creambox（canonical，8 页） | P7 披露盒 +24.7（见 §1.1）；其余 BELOW-WINDOW 7 条均为 +24.0/+37.0 的下一栏目标题假阳性 |
| spill sweep（本人 PIL 真墨扫） | 1 flag，裁定为观察项 O1（见 §5） |
| 盒标题 PIL 真墨 | 69 项 0 flags |
| print/web 文本层比对 | pdftotext **byte-equal，105,229 B**；web 1,699,714 B < 7 MB |
| web PDF scratch 重渲染 | `tools/webpdf.py` 在 scratch 重渲，文字层与生产网 PDF 文字层 **cmp 逐字节一致**，亦与印刷文字层一致；生产网 PDF 未动（字节/SHA 从不作为论据） |
| P8 最小字号 | PDF span 实测 **11.625pt** ≥ 9.75pt；SVG 文本最小 15.5pt |
| §1.1 适配检查（本人 `s11_fr_mine.py`） | PASS：纸色 #fbfaf6 ×8、色集与核心同为 19 色零出入、VOL.4/VOL.5 计数与核心逐页相等、三档徽章齐全、P8 四头齐全、SVG 文本层零真实 CJK（仅 U+3000，364 个） |
| check_s11.py / verify_ed.py | **fr 族无此二工具**：全仓与 hidden_files/w47 检出的副本均为 en 族，无法在 fr-nl 上运行；其检查意图由 gates 15 门 + 本人 s11 适配脚本覆盖（见 GATE-LOG §7） |
| 回归对照（vs #1 备份） | 见 §4 |

## 4. 与 #1 备份回归对照（KEEP/REVERT 盘点）

- SVG 逐页哈希：P1–P6 **byte-identical**（`984a2867` / `1f619509` / `4ef160c4` / `c9b59871` /
  `f2342e2a` / `ce2141d5`），仅 P7（`037b5c49`→`4eb69452`）、P8（`6a9750ef`→`467885cd`）改动。
- 源码 diff（仅 2 文件）：`expl.py:182` 删 `courrier_disclosure` 中句（D-1 规定修法）；
  `content8.py:170` 键 `devant`→`devant le`、`:176` 题干删 `du`（core fix4）。
  其余 `content12/34/56/7.py`、`bslib4.py`、`svglib.py`、`run.py`、`render.py` 全部 identical。
- `.text.md` diff 恰为 3 行：披露句（941 行）、Q148 题干（1039 行）、Q148 答案行（1083 行，`148. devant`→`devant le`）；`ABSTRACT.txt` identical。
- **KEEP/REVERT：#1 复校只报 1 项缺陷 D-1，无其他 hand patch 需要保留或回退。**
  两处源码改动与两项规定修复一一对应，无丢失、无多余改动、无回退。

## 5. 观察项（非缺陷，仅记录）

### O1 — P3「DATES À RETENIR」奶油盒末行下行尖微越盒底（sweep 唯一 flag）

- 位置：P3 右栏奶油盒 `x=1439.5, y=1639.6, w=422.5, h=330`，盒底 **1969.6**；
  末行 `woensdagavond 18.`（x=1461.5），基线 **1966.2**（盒内，clearance **+3.4**），
  desc-clear **-2.4**，PIL 真墨 1950.7..**1971.2**（越盒底 1.6px）。
- 来源：荷兰文注 3 行（1911.6 / 1938.9 / 1966.2），核心中文注仅 2 行（末基线 1938.9，
  desc-clear +24.9）——fan-out 翻译变长引入的紧度，非核心继承。
- 裁决（STRADDLE 口径）：**观察类，非缺陷**。字形未被裁切（`woensdagavond` 的 `g` 下行尖完整渲出，
  仅尖端 1.6px 落在盒外白纸上）；墨迹未与任何他元素或可见边框重叠（奶油盒无描边；
  下一元素 `POUR OU CONTRE ?` 在 y=2023.6，52px 之下）；与 #1 备份**无回归差异**
  （P3 SVG 逐字节相同，`4ef160c4`）。200 dpi 裁切 `S/png/crop-p3-dates-bottom.png` 目视确认：
  末行可读完整，盒边仅轻触 `g` 的下行尖。
- 与 D-1 的区别：D-1 是整行基线都在盒底之下（-2.6）、字墨 7.1px 越边、字形中部被奶油边横切；
  本项基线在盒内，仅下行尖微越。

### O2 — P2「ET VOUS ?」奶油盒末行下行尖微触盒边

- 盒 `x=1439.5, y=973.6, w=422.5, h=335`，盒底 **1308.6**；末行
  `twee zinnen in het Frans en stuur ze op.` 基线 **1304.2**（盒内，clearance **+4.4**），
  desc-clear **-1.6**。200 dpi 裁切 `S/png/crop-p2-etvous-bottom.png` 目视：末行完整可读，
  仅 `op` 的 `p` 下行尖轻触盒边。
- 核心版同盒（盒高 306.0，盒底 1279.6）末基线 1275.8，desc-clear **-2.2**——核心比本版更紧，
  属核心继承的版式紧度；荷兰盒已加高 29px。非缺陷。

### O3 — Q130 / Q36 / Q37 独行填空线（见 §1.4）

核心继承的版式，坐标关系符合任务书 nl 档（+59.5 带），不判缺陷。

### O4 — 其余沿用值（#1 已记，与核心一致）

P3 `POUR OU CONTRE ?` 框无荷兰语行、P5 `debat5_note` 出现两次——均与核心版一致（KIT 已披露）；
裸法文题头（`head_cine` 等）沿用 W46 nl 值，为本版既定模式；P3 ZOOM 框荷兰文注
`Vroege verkoop sinds 1951, derde donderdag sinds 1985, 75e jubileum in 2026.` 与 P8 注记 Q26
`Vroege verkoop in 1951` 为不同 E 键、措辞不同是正确的（同 pt）；
P8 注记配对键格式混用 `=` 与 ` = `（如 Q140 `sénateur = senator　a` 与 Q141 `vainqueur=winnaar b`），内容均正确。

## 6. D5 字体问题（全周级待定项，如实记录，不据此判 (b)，不擅自修）

网页版 PDF（PyMuPDF span 实测，8 页）：

- 全部荷兰语讲解层落在 **Noto Sans CJK SC**：`Stemming in de Senaat + filmpremières`（Reg, 15.75pt）、
  `VOL.5 lost de belofte in om echte inzendingen te bespreken.`（Reg, 14.62pt）；
- 法文导读标题 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI` 亦为 NotoSansCJKSC-Bold（34.5pt）；
- 法文正文为 Newsreader（`Dimanche 8 novembre, Carlos Alcaraz…` Reg, 18.0pt）。
- 字体集：Newsreader-Regula 888 / NotoSansCJKSC-Reg 560 / NotoSansCJKSC-Bol 463 /
  Newsreader-Bold 125 / NotoSerifCJKSC 19 / DejaVuSans 4（✗）/ UnifrakturMaguntia 1 / Newsreader-Italic 1。
- 与 #1 实测一致，属 SOP §1.1 全周级待定项，记录在案。

## 7. 八页逐页目视（印刷版 PDF，200 dpi 全页 + P7 盒底 200 dpi 裁切）

渲染件：`S/png/p-1.png`–`S/png/p-8.png`（本人 pdftoppm -r 200，自 verified SHA 的印刷 PDF 渲染）、
`S/png/crop-p7-boxbottom.png`、`S/png/crop-p3-dates-bottom.png`、`S/png/crop-p2-etvous-bottom.png`。

- P1：干净。导读条法文标题止 1236.9 / 荷兰语行起 1329.4；Atget 图注完整；Uitleg 盒、LES DATES 盒、
  agenda 盒、DANS CE NUMÉRO、LE MOT DE LA SEMAINE、EN BREF、QUIZ ÉCLAIR Q7–10 均干净。
- P2：干净。Uitleg 盒、Châtillon 图、LE SAVIEZ-VOUS ?、ET VOUS ? 盒（见 O2）、DIRE LA DATE 表、
  Q11–25（含 22–25 选项 a–d）均干净。
- P3：干净。ZOOM 框、DATES À RETENIR（见 O1）、LES MOTS DU VIN、Moreau 图注、Q26–43（含 Q36/Q37
  独行填空线）均干净。
- P4：干净。栏间续句正常（「Jeudi 12, à Milan, puis dimanche 15, à」在第 3 栏顶以
  「Bordeaux : deux soirs, deux matches…」续完，非截断），LE DÉBAT、LES MOTS DU TENNIS、MICRO-DRILLS
  Q56–61、LES CHIFFRES DU SPORT、À SUIVRE 均干净。
- P5：干净。Méliès 图注、Q62–66（含 Q64 B. Lukas Dhont）、Q67–72、Q73–76 选项 a–d、Q77–78 对话、
  OÙ SORTIR、MOTS DU CINÉMA、LE CINÉMA DU MERCREDI、LE DÉBAT 均干净。
- P6：干净。LE CALENDRIER 全 7 行 + 来源行（含 chart_note 荷兰行在盒内）、LIRE LE CALENDRIER Q79–84、
  LES MOTS Q85–88、LE COMPARATIF、MICRO-DRILLS Q92–96、TROIS DATES、APRÈS LE VOTE 均干净。
- P7：干净。语法四栏、三 LA PHRASE EXEMPLE 盒、Doré 图注、LES PHRASES DE LA SEMAINE Q97–104、
  CLINIQUE DES ERREURS Q105–108、LE COURRIER DES LECTEURS 披露 2 行在盒内（见 §1.1）、
  LA SEMAINE PROCHAINE 深绿带均干净。
- P8：干净。A–H 全部题区（含 G 对话 `(148)___ cinéma ?`）、MODÈLE、RÉPONSES 121 条注记
  （含 `148. devant le`）、Hiroshige 图注、Q130 独行填空线均完整；最小字号 11.625pt。

## 8. 过程事件

- **服务重启中断（2026-11-11 约 17:27）**：一次渲染调用在 pdftoppm 途中被重启杀掉，
  `p-3.png` 写坏（解码失败）。已单页重渲并校验完整（4063×5625 RGB，2,519,298 B），
  其余 7 页与全部门禁证据（均早于重启）逐项核对无损；无证据丢失。
- 生产目录零写入；未 commit、未 push。收尾时三件 SHA 再次逐值复核一致（见结论表）。

## 9. 报告文件

- 本文件：`scratch-proof-fr-nl2/PROOF-NOTE.md`
- 门禁日志：`scratch-proof-fr-nl2/GATE-LOG.md`
- 证据：`gates-proof1.json`、`nl/gates-proof1.log`、`nl/build-proof1.log`、`build-proof1-rerun.log`、
  `p8-proof1.json`、`p8compare-proof1.json`、`occlusion-proof1.json/.log`、`creambox-proof1.log`、
  `creambox-core.log`、`spill.log`、`spill-core.log`、`boxtitle-proof1.log`、`nl/extra-proof1.json`、
  `nl/extra-proof1.log`、`freeze/freeze-baseline.log`、`freeze/freeze-baseline-ed.log`、
  `freeze/freeze-diff.json`、`freeze/freeze-diff.log`、`print-proof1.txt`、`web-proof1.txt`、
  `mcq-proof1.log`、`s11.log`、`reg.json`（`regdump/`）、`regdump.log`、`key-stem-table-MINE.txt`、
  `webre/web-proof1.pdf`（scratch 重渲网 PDF）、`webre/web-proof1.txt`、`webre/web-prod.txt`、
  `png/p-1.png`–`png/p-8.png`、`png/crop-p7-boxbottom.png`、`png/crop-p3-dates-bottom.png`、
  `png/crop-p2-etvous-bottom.png`、`oldp7/p7-langue.svg`（#1 旧 P7 阳性对照）
