# PROOF-NOTE — W47 fr-es（法语核心 × 西班牙语读者）独立复校 proof1

复校员：独立复校（与构建者不同人）。日期：2026-11-11。
目标：`production/2026-w47/2026-w47-fr-es/`（run2）。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-es1/`。
只读生产文件：未改任何生产文件，未 commit、未 push。门禁确定性重跑在 scratch 副本中进行（`rerun/`），生产目录未写入。

## 结论：(b) 有缺陷，不定稿

**缺陷 1 项（布局溢出，fan-out 引入，核心版无此问题）：**

### D-1　P7 读者园地奶油盒：西班牙语注记末行漫出盒底

- 位置：P7 右栏 `LE COURRIER DES LECTEURS / CARTAS DE LECTORES` 奶油盒（SVG `p7-langue.svg`，盒 y=1878，盒底 bottom=2258.0）。
- 实测（SVG 坐标，creambox 规范版 `hidden_files/w47/tools/creambox.py`）：
  - 盒内末行基线 2233.3，inside-only clearance +24.7，desc-clear +18.8（干净）；
  - 但西班牙语注记为 3 行，末行 `envíos reales.` 基线 y=2260.6，**比盒底低 2.6 svg 单位**，creambox 报 `BELOW-WINDOW +2.6`。
- PIL 真墨测量（印刷版 PDF，250 dpi 裁图 `png/crop3-p7-mailbox.png`，PDF 点坐标系 y_pt = 0.75 × y_svg，已用 3 个盒子验明）：
  - 奶油末行（该行 x 范围内）：svg 2257.5（= 盒底 2258.0，吻合）；
  - `envíos reales.` 深色墨行：svg 2254–2260，盒底之下仍有满色墨行 svg 2258 / 2259 / 2260（颜色 (110,103,93)，即注记灰字）；
  - 结论：末行字脚约 2.5 svg 单位（≈1.9pt ≈ 0.67mm）落在奶油盒外、白底上；250 dpi 裁图目视可见奶油边线横切 `envíos reales.` 字脚下部。
- PDF span 佐证：奶油矩形底 pt 1693.5，`envíos reales.` span bbox 底 pt 1699.7（+6.2pt，含字体下行量）；基线 pt 1695.45，比盒底低 1.95pt。
- 核心版对照：同一盒子核心版注记末基线 2233.3，盒底 2258.0，末 span bbox 底 pt 1679.2，盒内余 14.3pt——**核心版干净，此溢出是西班牙语注记比中文注记多一行造成的 fan-out 缺陷**。
- 修复方向（供 builder，不由复校员改）：把 P7 邮箱西班牙语注记缩短约一行（如收紧前两行措辞，把 `envíos reales.` 拉回盒内），或按盒子规则加深盒子——以 creambox inside-only clearance 为正为准。

除 D-1 外，本版其余全部复校项通过（见下）。

---

## 1. 身份核对（磁盘实测，先核对再开工）

| 产物 | 字节 | SHA-256（实测） | 与任务书 |
|---|---|---|---|
| `La-Lucerna-VOL4-fr-es.pdf`（印刷） | 17,418,404 | `eb2a01432212e59f5b56cba88e437b4ac2c80b16a54d36b0a85d265b0496d806` | 一致 |
| `La-Lucerna-VOL4-fr-es-web.pdf`（网页） | 1,699,232 | `1756ddfe5f1927122610661dfd50ed874e3fd4672a2d8e4549285d13482f323f` | 一致 |
| `2026-w47-fr-es.text.md` | 46,721（1,088 行） | `87bc611d595420d535418ceb0ef7118924e9876fed28e9732af584aaa4bb2635` | 一致 |

探针：`/dev/null` 缺失，先 `touch /dev/null` 垫回，`git hash-object -w --stdin` 通（`9daeafb9…`）；goals 侧写文件成功后开工。TMPDIR 用 goals 侧 scratch 下 `tmp/`。

## 2. freeze 首检（venv：Pillow 13.0.0 / FreeType 2.14.3）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-es/svg`：

- p1–p8 逐页字符串增减正常（法文冻结串存活，西班牙语讲解层替换）；
- 新增 CJK 字符合计 10 个，**全部为 U+3000（全角空格）**：p3 ×1、p6 ×1、p8 ×8，其余页 0。这是两段式导读条的分隔符（`ALCARAZ GANA　SENADO VOTA MIÉRC.` 等），本家庭各版通用结构；`string_freeze` 门记为 0 未入账 CJK 字符。无新增 CJK 汉字/假名/韩文。无简体中文残留。
- 日志：`freeze-diff.json`。

## 3. 机械门禁（独立重跑，15/15 PASS）

用 `gates.py` 的副本 `gates-proof.py`（输出改到本 scratch；第 7 门确定性重跑改在 scratch 副本 `rerun/` 中做，生产目录零写入），tag `proof1`，exit 0：

| 门 | 结果（独立重跑实测） |
|---|---|
| run | PASS — exit 0，零 overflow/wide；TOTAL 150；by level A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion | PASS — 0 flags，selftest OK |
| p8_extract | PASS — keys 150/150，printed notes 121/150 |
| p8_compare | PASS — CLEAN，keydiff [150]（仅写作题键） |
| source_freeze | PASS — content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | PASS — 核心非 CJK 串逐页存活；0 核心 E 残留；0 未入账 CJK；1 条翻译豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| freeze_direct | PASS — scratch 副本重跑，8/8 SVG SHA 全同：`bd6a40f0, 220dd45e, 1b39fa5b, dd5ec45e, 51b18d6f, c3f18dcd, c7fc6d9e, 20df945f`（与 builder run2 哈希逐位相同） |
| text_layer | PASS — 印/网 pdftotext 逐字节一致（105,094 B）；网 1,699,232 B < 7MB；印 17,418,404 B |
| p8_font | PASS — P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS — U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS — 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck | PASS — 150 键对核心 `final-fr-p8.json`，仅 Q150 不同 |
| mcq | PASS — bodies: 45，rendered lines: 1480，0 缺陷 |
| widths | PASS — 31 条单行串全部在预算内 |
| band_spans | PASS — 法文标题止 1236.9，band_r1 起 1299.7（净空 62.8）；法文副标题止 837.2，band_r2 起 1450.1 |

完整 JSON：`gates-proof1.json`；日志：`GATE-LOG.md`。

## 4. creambox 全版扫描（规范版，8 页）

`hidden_files/w47/tools/creambox.py` 扫 8 个 SVG（`creambox.log`），8 条 BELOW-WINDOW，逐条裁定：

| # | 盒 | BELOW-WINDOW | 裁定 |
|---|---|---|---|
| 1 | P1 y=1280 bottom=1652.0 | +24.0 `LE MOT DE LA SEMAINE` | 假阳性——下一栏目标题，盒内末行 clearance +48.0 / desc +41.7 |
| 2 | P2 y=886 bottom=1090.8 | +37.0 `LA SEMAINE EN CHIFFRES` | 假阳性——下一栏目标题，盒内 +47.7 |
| 3 | P3 y=200 bottom=375.4 | +37.0 `À VOUS !　¡TE TOCA!` | 假阳性——下一框标题，盒内 +47.7 |
| 4 | P4 y=200 bottom=405.1 | +37.0 `À VOUS !　¡TE TOCA!` | 假阳性——下一框标题，盒内 +47.7 |
| 5 | P5 y=2182 bottom=2357.7 | +37.0 `À VOUS !　¡TE TOCA!` | 假阳性——下一框标题，盒内 +47.7 |
| 6 | P6 y=463 bottom=789.8 | +37.0 `IL EST PRÉVU QUE + SUBJONCTIF` | 假阳性——下一栏目标题，盒内 +48.5 |
| 7 | P6 y=1330 bottom=1656.7 | +37.0 `LE DÉBAT　DEBATE` | 假阳性——下一栏目标题，盒内 +48.5 |
| 8 | **P7 y=1878 bottom=2258.0** | **+2.6 `envíos reales.`** | **真溢出 = 缺陷 D-1**（见上；核心版同盒干净） |

另两处紧盒（非 BELOW-WINDOW），核对核心版后不列为缺陷：

- P2 `ET VOUS ?` 盒（y=974 bottom=1308.6）：末行基线 1304.2，clearance +4.4，desc-clear −1.6。PDF 实测 span bbox 底比盒底低 1.1pt；**核心版同盒 desc-clear −2.2、span 低 1.5pt（比本版更紧）**——核心继承的紧度，`y` 下行尖刚触盒边，100 dpi 目视无漫出感。不列为 fan-out 缺陷。
- P1 agenda 盒（y=588 bottom=1256.0）：末行 clearance +8.0，desc-clear +2.3，与核心版逐值相同。不列为缺陷。

## 5. 八页逐页目视（印刷版 PDF，100 dpi，全页 + 三处 250 dpi 裁图）

- P1：干净。导读条法文标题止 1236.9 / 西班牙语行起 1299.7，净空清晰；副标题行无重叠；Atget 图注完整；`Nota` 盒、日期盒、`DANS CE NUMÉRO`、`LE MOT DE LA SEMAINE` 均干净。
- P2：干净。`Nota` 盒、Châtillon 图、`LE SAVIEZ-VOUS ?`、`ET VOUS ?` 盒、`DIRE LA FECHA`、`EXERCICES` Q11–25 均干净。
- P3：干净。`POUR OU CONTRE ?` 框无西班牙语行（与核心版一致，已记入 KIT §六）；ZOOM 框 `1951/1985/2026` + 西班牙语行完整；`BEAUJOLAIS EL QUIZ`、`DATES À RETENIR` 干净；Moreau 图注完整。
- P4：干净。`LES PHRASES DU COMMENTATEUR`（`¡Vamos! / ¡Qué jugada! / ¡Marca! / ¡Ganó!`）完整；`LES CHIFFRES DU SPORT`、`LES MOTS DU TENNIS`、`À SUIVRE`、`MICRO-DRILLS`、`LE DÉBAT` 干净。
- P5：干净。Méliès 图注完整；`REGARDER UN FILM`、`OÙ SORTIR`、`MOTS DU CINÉMA`、`LE CINÉMA DU MERCREDI`、`LE DÉBAT` 干净。
- P6：干净。`LE CALENDRIER` 全 7 行 + 来源行完整；`TROIS DATES`、`LE DÉBAT`、`APRÈS LE VOTE`、`LIRE LE CALENDRIER`、`LES MOTS`、`MICRO-DRILLS` 干净。
- P7：除 D-1 外干净。语法四栏、`LA PHRASE EXEMPLE` 三盒、Doré 图注、`LES PHRASES DE LA SEMAINE` Q97–104、`CLINIQUE DES ERREURS` Q105–108、`LA SEMAINE PROCHAINE` 深绿带均干净。
- P8：干净。A–H 全部题区、`MODÈLE`、`RÉPONSES` 121 条注记、Hiroshige 图注完整；P8 答案流 2166.6，图置于 2176.6，页内无重叠。
- 全页图：`png/p1.png`–`png/p8.png`；裁图：`png/crop3-p7-mailbox.png`、`png/crop3-p2-box.png`、`png/crop3-p1-agenda.png`。

## 6. 150 题逐题手验（对 `core-fr/final-fr-p8.json` + 题干 + 正文 + 注记）

- 独立抽取 `p8.py extract --total 150`（`p8-proof1.json`）：150/150 键；与核心逐键比对，**仅 Q150 不同**（核心 `开放题` → es `Pregunta abierta`，写作题读者语言说明，属预期）；其余 149 键逐字相同。keycheck 门亦同。
- 逐题核对答案与题干/正文的一致性（抽查全部 150 键的答案语义，重点核对易错点）：
  - Q1–Q6 gagné / mercredi / jeudi / premier / 12,7 / 22；Q7–Q10 A/B/A/B；Q11–14 mercredi / lundi / jeudi / dimanche；Q15–18 未来 proche 四句；Q19–21 C/B/A；Q22–25 a/b/c/d；Q26–30 Vrai/Faux/Vrai/Faux/Vrai；Q31–34 gamay/jeudi/Beaujeu/1985；Q35–37 否定改写；Q38–40 75 ans/minuit/troisième；Q41 B / Q42 13 / Q43 saucisson；Q44–48 B/A/C/A/A；Q49–52 a/b/c/d；Q53–55 plus vite/plus grand/moins longue；Q56–61 forfait/finale/groupes/tirage/Bordeaux/Milan；Q62–66 B/B/B/A/A；Q67–72 mercredi/prequel/Ménochet/21/produit/acheter；Q73–76 a/b/c/d；Q77–78 des billets/deux；Q79–84 B/B/B/B/**C**/B（Q83=C 已三重核对：核心 `final-fr-p8.json` C、P8 印出 `83. C (Votación solemne el 9 de dic.)`、核心 text.md `83. C（正式投票 12 月 9 日）`一致；9 déc. 为预算投票，18 nov. 为 Sécu 投票）；Q85–88 a/b/c/d；Q89–91 plus long/moins simple/aussi important；Q92–96 examine/ont rejeté/part/peut/connus；Q97–104 battu/est arrivé/vote/beauté/produit/sortent/rejetée/jouer；Q105–108 改错四句；Q109–116 A/B/A/B/A/A/B/A；Q117–124 A/A/B/B/A/B/A/C；Q125–129 A/A/A/A/A；Q130–139 翻译/改写五组；Q140–144 a/b/c/d/e；Q145–149 des billets/deux/quelle heure/devant/film；Q150 Pregunta abierta。
  - Q72 注：`Acheter en seconde main, c'est ___ d'occasion.` 键 `acheter`（词库填空），句式重复但语法成立，且与核心版逐字相同——核心冻结内容，不列为缺陷。
  - Q67–72 词库、`Completa con…` 指令与答案一致。
- `.text.md` 全文通读 1,088 行：CJK 字符 0；U+2019=0；U+00B7=0；西班牙语讲解/注记逐条正确（抽查全部 Nota 盒与 121 条 P8 注记，译法准确，如 `trancher→decidir, zanjar`、`la trêve→el parón`、`une navette→el ir y venir entre cámaras`、`se terminer en beauté→terminar muy bien`、`il est prévu que + subjuntivo` 等）；人名拼写与法文正文一致（Dhont、Ménochet、Fils、Haymitch、Lawrence、Smia、Meddour、Scott Thomas、Guiz、Mipo O、Hiroshige、Doré、Atget、Moreau、Méliès）；日期/数字与正文一致（16 nov. 周一、75 ans、458–0、115–1、1 260→1 500、21,8→12,7）。
- 范文 `MODÈLE` 实测 96 词（80–100 要求内）；P7 八句金句逐句核对均逐字出自 P1–P6 正文（8/8）。
- ABSTRACT.txt：一行西班牙语，233 B，无 ASCII `"`，内容准确（Alcaraz / Senado / Beaujolais 75 周年 / 150 题 / 16–22 nov.）。

## 7. D5 字体问题（全周级待定项，如实记录，不据此判 (b)，不擅自修）

网页版 PDF（PyMuPDF span 实测）所见：

- 全部西班牙语讲解层文字落在 **Noto Sans CJK SC**：`Votación del Senado: el miércoles.`（LucernaNotoSansCJKSC-Reg, 14.25pt）、`Cuenta tu 19 de noviembre…`（15pt）、`envíos reales.`（14.62pt）、页眉/页脚 `EXPLICACIONES EN ESPAÑOL`（12/12.75pt）；
- 法文导读标题 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI` 亦为 NotoSansCJKSC-Bold（34.5pt）；
- 法文正文为 Newsreader（`Dimanche 8 novembre, Carlos Alcaraz…` 18pt）；刊名 `Le Lucerna` 为 UnifrakturMaguntia（147pt）。
- 即：讲解层拉丁字符落在 Noto Sans CJK SC，违反 SOP §1.1——与任务书所述全周级待定项一致，记录在案，待用户定夺 scope；本复校不因此单方面判 (b)。

## 8. 观察项（非缺陷，仅记录）

1. W46 复用值：P6 `head_lire` 为 `LIRE LE CALENDRIER　HORARIO`（`HORARIO` 对 `LIRE LE CALENDRIER` 为宽松意译，读者可懂，沿用未改）；P3 `Minidrills` 标签未译（英文原词，沿用）；P8 注记配对键格式混用 `=` 与 ` = `（如 Q140 `sénateur = senador　a` 与 Q141 `vainqueur=ganador b`），内容均正确，KIT §六已披露未统一。皆为装饰性不一致，不列为缺陷。
2. P2 `ET VOUS ?` 盒末行下行尖触盒边（见 §4），核心版更紧——核心继承，非 fan-out 缺陷。
3. P3 `POUR OU CONTRE ?` 框无西班牙语行、P5 `debat5_note` 出现两次——均与核心版一致（KIT §六已披露）。

## 9. 报告文件

- 本文件：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-es1/PROOF-NOTE.md`
- 门禁日志：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-es1/GATE-LOG.md`
- 证据：`gates-proof1.json`、`freeze-diff.json`、`creambox.log`、`creambox-core.log`、`p8-proof1.json`、`p8compare-proof1.json`、`occlusion-proof1.json`、`mcq-proof1.log`、`print-proof1.txt`、`web-proof1.txt`、`build-proof1.log`、`build-proof1-rerun.log`、`png/p1.png`–`png/p8.png`、`png/crop3-p7-mailbox.png`、`png/crop3-p2-box.png`、`png/crop3-p1-agenda.png`
