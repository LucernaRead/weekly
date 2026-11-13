# PROOF-NOTE — W47 fr-pt（法语核心 × 葡萄牙语读者）独立复校 proof1

复校员：独立复校（与构建者不同人）。日期：2026-11-11。
目标：`production/2026-w47/2026-w47-fr-pt/`（run2）。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt1/`。
只读生产文件：未改任何生产文件，未 commit、未 push。门禁确定性重建在 scratch 副本中进行（`rerun/`），生产目录零写入（`git status` 上该版目录为未提交新目录，属 builder 工作状态；复校未动）。

## 结论：(b) 有缺陷，不定稿

**缺陷 1 项（布局溢出，fan-out 引入，核心版无此问题）：**

### D-1　P7 读者园地奶油盒：葡萄牙语注记末行漫出盒底

- 位置：P7 右栏 `LE COURRIER DES LECTEURS / CARTAS DOS LEITORES` 奶油盒（SVG `p7-langue.svg`，盒 y=1878，盒底 bottom=2258.0）。
- 实测（SVG 坐标，creambox 规范版 `hidden_files/w47/tools/creambox.py`）：
  - 盒内末行基线 2233.3，inside-only clearance +24.7，desc-clear +18.8（干净）；
  - 但葡萄牙语注记为 3 行，末行 `envios reais.` 基线 y=2260.6，**比盒底低 2.6 svg 单位**，creambox 报 `BELOW-WINDOW +2.6`。
- PIL 真墨测量（印刷版 PDF，250 dpi 裁图 `png/crop-p7-mailbox.png`，PDF 点坐标系 y_pt = 0.75 × y_svg；奶油边已用垂直扫描验明：svg 2258 仍为奶油色 (239,237,228)，svg 2259 起为纸白 (251,249,246)；奶油末行 svg 2257.7 ≈ 盒底 2258.0）：
  - `envios reais.` 注记灰字墨行：svg 2258–2260.8，盒底之下仍有满色墨行 svg 2259.2 / 2259.6 / 2260.0（颜色 (110,103,93)，即注记灰字）；
  - 结论：末行字脚约 2.5–2.8 svg 单位（≈1.9pt ≈ 0.67mm）落在奶油盒外、白底上；250 dpi 裁图目视可见奶油边线横切 `envios reais.` 字脚下部。
- PDF span 佐证：奶油矩形底 pt 1693.5，`envios reais.` span bbox 底 pt 1699.66（+6.16pt，含字体下行量）；基线 pt 1695.45，比盒底低 1.95pt。
- 核心版对照：同一盒子核心版注记末基线 2233.3，盒底 2258.0，末 span bbox 底 pt 1679.2，盒内余 14.3pt——**核心版干净，此溢出是葡萄牙语注记比中文注记多一行造成的 fan-out 缺陷**。
- 同类：es/de/it/nl/ru 复校均在同盒同位报出 −2.6（es1、de1 已判 (b)），属本轮 fan-out 共性缺陷类；本报告只判定 pt 版。
- 修复方向（供 builder，不由复校员改）：把 P7 邮箱葡萄牙语注记缩短约一行（如收紧前两行措辞，把 `envios reais.` 拉回盒内），或按盒子规则加深盒子——以 creambox inside-only clearance 为正为准。

除 D-1 外，本版其余全部复校项通过（见下）。

---

## 记录项（不计入本版 (b) 判定）

### R1 — Q148 错法语（核心继承，10 版共有，需 core 轨道修）

- 印法：P8 对话 "— On se retrouve (148)___ du cinéma ? — Oui, à 19 h 30."，答案键 `devant`（`p8-proof1.json` / 核心 `final-fr-p8.json` 均为 `devant`）。
- 问题：填入后成 "On se retrouve **devant du cinéma** ?"——介词 `devant` 后不接 `du`，正确应为 "devant **le** cinéma"。注记 "148. devant (À porta do cinema)" 本身无误。
- 定性：核心冻结源 `core-fr/content8.py:176` 与 pt 版 `content8.py:176` 字节相同，核心键亦为 `devant`；属核心原文缺陷，非 pt fan-out 引入，fan-out 按 freeze 规则不得擅自偏离核心。故不计入 pt 版缺陷，报请转 core 轨道修复（修核心后 10 版同受影响，须重验）。de1 复校亦已记录同一 R1。

### R2 — D5 字体（全周级已知待定项，如实记录，不判 (b)、不擅自修）

- SVG 字体普查（8 页）：`Newsreader` 947 段、`Noto Sans CJK SC` 692 段、`Noto Serif CJK SC` 74 段（全为结构分隔符 U+3000，不可见）、`DejaVu Sans` 4 段（P7 ✗ 标记，合理）、`UnifrakturMaguntia` 1 段（刊头黑体）。
- 其中 CJK 字体段中 **498 段为纯拉丁文**（无 CJK 字符、含葡语词），即葡萄牙语讲解层落在 Noto Sans CJK SC（核心对照：de1 报核心 776 段 CJK 字体中纯拉丁 100 段）。
- 网页版 PDF（PyMuPDF span 实测）：全部葡萄牙语讲解层文字落在 **LucernaNotoSansCJKSC-Reg/Bol**：`EXPLICAÇÕES EM PORTUGUÊS`（12.75pt）、`envios reais.`（14.62pt）；法文正文为 Newsreader（`Turin commence dimanche…` 18.75pt）；刊名 `Le Lucerna` 为 UnifrakturMaguntia（147pt）；法文导读标题 `ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI` 亦为 NotoSansCJKSC-Bold。
- 即：讲解层拉丁字符落在 Noto Sans CJK SC，违反 SOP §1.1——与任务书所述全周级待定项一致，记录在案，待用户定夺 scope；本复校不因此单方面判 (b)。

---

## 1. 身份核对（磁盘实测，先核对再开工）

| 产物 | 字节 | SHA-256（实测） | 与任务书 |
|---|---|---|---|
| `La-Lucerna-VOL4-fr-pt.pdf`（印刷） | 17,420,079 | `dc64cb43fcf8a87cc6234a10e0912daf5afc4b77e1299cea6a17424989e3f6c3` | 一致 |
| `La-Lucerna-VOL4-fr-pt-web.pdf`（网页） | 1,702,412 | `1b7eb1cfa8f9f7a94cc5575f937d73a08332a3750c5206f8ee5bb3ebbcd3644b` | 一致 |
| `2026-w47-fr-pt.text.md` | 46,601（1,088 行） | `45aa52c54faa11ce0d0dfcffb8682aa1198850ce2f5ea62ae0d8efe74cb9c8a6` | 一致 |

探针：`/dev/null` 存在，`git hash-object -w --stdin` 通（`9daeafb9…`）；goals 侧写文件成功后开工。TMPDIR 用 goals 侧 scratch 下 `tmp/`。

## 2. freeze 首检（venv：Pillow 13.0.0 / FreeType 2.14.3）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-pt/svg`：8/8 页。

- p1–p8 逐页字符串增减正常（法文冻结串存活，葡萄牙语讲解层替换）；
- 新增 CJK 字符合计 11 个，**全部为 U+3000（全角空格）**：p2 ×1、p8 ×10，其余页 0。这是两段式导读条/栏目标题/注记流的分隔符（`ALCARAZ VENCE　SENADO VOTA QUARTA`、`MODÈLE　Modelo`、`1. gagné　2. mercredi` 等），本家庭各版通用结构；`string_freeze` 门记为 0 未入账 CJK 字符。无新增 CJK 汉字/假名/韩文。无简体中文残留。
- 日志：`freeze-diff.json`。

## 3. 机械门禁（独立重跑，15/15 PASS）

用 `gates.py` 的副本 `gates-proof.py`（输出改到本 scratch；第 7 门确定性重跑改在 scratch 副本 `rerun/` 中做，生产目录零写入；全部 venv python 运行均加 `PYTHONDONTWRITEBYTECODE=1`），tag `proof1`，exit 0：

| 门 | 结果（独立重跑实测） |
|---|---|
| run | PASS — exit 0，零 overflow/wide；TOTAL 150；by level A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion | PASS — 0 flags，selftest OK |
| p8_extract | PASS — keys 150/150，printed notes 121/150 |
| p8_compare | PASS — CLEAN，keydiff [150]（仅写作题键） |
| source_freeze | PASS — content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | PASS — 核心非 CJK 串逐页存活；0 核心 E 残留；0 未入账 CJK；1 条翻译豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| freeze_direct | PASS — scratch 副本重跑，8/8 SVG SHA 全同：`a8ca67ea, 1c7f056e, 13a8fe0a, d9b6af38, 2a66a9f0, 5ef9766c, ea3d710b, 7d582103`（与 builder run2 哈希逐位相同；另一次独立重建亦 8/8） |
| text_layer | PASS — 印/网 pdftotext 逐字节一致（104,850 B）；网 1,702,412 B < 7MB；印 17,420,079 B |
| p8_font | PASS — P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS — U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS — 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck | PASS — 150 键对核心 `final-fr-p8.json`，仅 Q150 不同 |
| mcq | PASS — bodies: 45，rendered lines: 1483，0 缺陷 |
| widths | PASS — 31 条单行串全部在预算内 |
| band_spans | PASS — 法文标题止 1236.9，band_r1 起 1270.9（净空 34.0）；法文副标题止 837.2，band_r2 起 1489.2 |

完整 JSON：`gates-proof1.json`；日志：`GATE-LOG.md`。

## 4. creambox 全版扫描（规范版，8 页）

`hidden_files/w47/tools/creambox.py` 扫 8 个 SVG（`creambox.log`；另扫核心版作对照 `creambox-core.log`），8 条 BELOW-WINDOW，逐条裁定：

| # | 盒 | BELOW-WINDOW | 裁定 |
|---|---|---|---|
| 1 | P1 y=1280 bottom=1652.0 | +24.0 `LE MOT DE LA SEMAINE` | 假阳性——下一栏目标题（与核心版同值 −24.0），盒内末行 clearance +48.0 / desc +41.7 |
| 2 | P2 y=886 bottom=1090.8 | +37.0 `LA SEMAINE EN CHIFFRES` | 假阳性——下一栏目标题（与核心版同值 −37.0），盒内 +47.7 |
| 3 | P3 y=200 bottom=375.4 | +37.0 `À VOUS !　A TUA VEZ!` | 假阳性——下一框标题（与核心版同值 −37.0），盒内 +47.7 |
| 4 | P4 y=200 bottom=405.1 | +37.0 `À VOUS !　A TUA VEZ!` | 假阳性——下一框标题（与核心版同值 −37.0），盒内 +47.7 |
| 5 | P5 y=2182 bottom=2357.7 | +37.0 `À VOUS !　A TUA VEZ!` | 假阳性——下一框标题（与核心版同值 −37.0），盒内 +47.7 |
| 6 | P6 y=463 bottom=789.8 | +37.0 `IL EST PRÉVU QUE + SUBJONCTIF` | 假阳性——下一栏目标题（与核心版同值 −37.0），盒内 +48.5 |
| 7 | P6 y=1330 bottom=1656.7 | +37.0 `LE DÉBAT　DEBATE` | 假阳性——下一栏目标题（与核心版同值 −37.0），盒内 +48.5 |
| 8 | **P7 y=1878 bottom=2258.0** | **+2.6 `envios reais.`** | **真溢出 = 缺陷 D-1**（见上；核心版同盒干净） |

另两处紧盒（非 BELOW-WINDOW），核对核心版后不列为缺陷：

- P2 `ET VOUS ?` 盒（y=974 bottom=1308.6）：末行基线 1304.2，clearance +4.4，desc-clear −1.6。PDF 实测 span bbox 底比盒底低 1.0pt；**核心版同盒 desc-clear −2.2、盒底 1279.6（比本版更紧）**——核心继承的紧度，`y` 下行尖刚触盒边，100 dpi 目视无漫出感。不列为 fan-out 缺陷。
- P1 agenda 盒（y=588 bottom=1256.0）：末行 clearance +8.0，desc-clear +2.3，与核心版逐值相同。不列为缺陷。

## 5. 八页逐页目视（印刷版 PDF，100 dpi，全页 + 三处 250 dpi 裁图；另抽查网页版 P1/P7）

- P1：干净。导读条法文标题止 1236.9 / 葡语行起 1270.9，净空 34.0 清晰；副标题行无重叠；Atget 图注完整；`Nota` 盒、日期盒、`DANS CE NUMÉRO`、`LE MOT DE LA SEMAINE` 均干净。
- P2：干净。`Nota` 盒、Châtillon 图、`LE SAVIEZ-VOUS ?`、`ET VOUS ?` 盒、`DIRE LA DATE`、`EXERCICES` Q11–25 均干净。
- P3：干净。`POUR OU CONTRE ?` 框无葡语行（与核心版一致，已记入 KIT §六）；ZOOM 框 `1951/1985/2026` + 葡语行完整；`BEAUJOLAIS O QUIZ`、`DATES À RETENIR` 干净；Moreau 图注完整。
- P4：干净。`LES PHRASES DU COMMENTATEUR`（`Allez ! / Quelle action ! / Il marque ! / C'est gagné !` + 葡译）完整；`LES CHIFFRES DU SPORT`、`LES MOTS DU TENNIS`、`À SUIVRE`、`MICRO-DRILLS`、`LE DÉBAT` 干净。
- P5：干净。Méliès 图注完整；`REGARDER UN FILM`、`OÙ SORTIR`、`MOTS DU CINÉMA`、`LE CINÉMA DU MERCREDI`、`LE DÉBAT` 干净；`debat5_note` 出现两次，与核心版一致。
- P6：干净。`LE CALENDRIER` 全 7 行 + 来源行完整；`TROIS DATES`、`LE DÉBAT`、`APRÈS LE VOTE`、`LIRE LE CALENDRIER`、`LES MOTS`、`MICRO-DRILLS` 干净。
- P7：除 D-1 外干净。语法四栏、`LA PHRASE EXEMPLE` 三盒、Doré 图注、`LES PHRASES DE LA SEMAINE` Q97–104、`CLINIQUE DES ERREURS` Q105–108、`LA SEMAINE PROCHAINE` 深绿带均干净。
- P8：干净。A–H 全部题区、`MODÈLE`、`RÉPONSES` 121 条注记、Hiroshige 图注完整；P8 答案流 2106.15，图置于 2116.15，页内无重叠。
- 网页版抽查 P1/P7：与印刷版同版式，D-1 同盒同位可见（`web-p7.png`）。
- 全页图：`png/p1.png`–`png/p8.png`；裁图：`png/crop-p7-mailbox.png`、`png/crop-p2-box.png`、`png/crop-p1-agenda.png`；网页抽查：`png/web-p1.png`、`png/web-p7.png`。

## 6. 150 题逐题手验（对 `core-fr/final-fr-p8.json` + 题干 + 正文 + 注记）

- 独立抽取 `p8.py extract --total 150`（`p8-proof1.json`）：150/150 键；与核心逐键比对，**仅 Q150 不同**（核心 `开放题` → pt `Pergunta aberta`，写作题读者语言说明，属预期）；其余 149 键逐字相同。`keytable-proof1.txt` 逐题列表亦同。
- 逐题核对答案与题干/正文的一致性（全部 150 键的答案语义，重点核对易错点）：
  - Q1–Q6 gagné / mercredi / jeudi / premier / 12,7 / 22；Q7–Q10 A/B/A/B；Q11–14 mercredi / lundi / jeudi / dimanche；Q15–18 未来 proche 四句；Q19–21 C/B/A；Q22–25 a/b/c/d；Q26–30 Vrai/Faux/Vrai/Faux/Vrai；Q31–34 gamay/jeudi/Beaujeu/1985；Q35–37 否定改写；Q38–40 75 ans/minuit/troisième；Q41 B / Q42 13 / Q43 saucisson；Q44–48 B/A/C/A/A；Q49–52 a/b/c/d；Q53–55 plus vite/plus grand/moins longue；Q56–61 forfait/finale/groupes/tirage/Bordeaux/Milan；Q62–66 B/B/B/A/A；Q67–72 mercredi/prequel/Ménochet/21/produit/acheter；Q73–76 a/b/c/d；Q77–78 des billets/deux；Q79–84 B/B/B/B/**C**/B（Q83=C 已三重核对：核心 `final-fr-p8.json` C、P8 印出 `83. C (Votação solene 9 dez.)`、P6 日历 `9 déc. Vote solennel : le budget de l'État` 一致；9 déc. 为预算投票，18 nov. 为 Sécu 投票）；Q85–88 a/b/c/d；Q89–91 plus long/moins simple/aussi important；Q92–96 examine/ont rejeté/part/peut/connus；Q97–104 battu/est arrivé/vote/beauté/produit/sortent/rejetée/jouer；Q105–108 改错四句；Q109–116 A/B/A/B/A/A/B/A；Q117–124 A/A/B/B/A/B/A/C；Q125–129 A/A/A/A/A；Q130–139 翻译/改写五组；Q140–144 a/b/c/d/e；Q145–149 des billets/deux/quelle heure/devant/film；Q150 Pergunta aberta。
  - Q72 注：`Acheter en seconde main, c'est ___ d'occasion.` 键 `acheter`（词库填空），句式重复但语法成立，且与核心版逐字相同——核心冻结内容，不列为缺陷。
  - Q83 注：见上三重核对。
  - Q102 注：注记 `sortir = estrear, sair` 为影院释义，P7 语法行 `sortir: estrear, sair` 与之统一，各自正确。
  - Q148：见 R1（核心继承错法语）。
- `.text.md` 全文通读 1,088 行：CJK 字符 0；U+2019=0；U+00B7=0；葡萄牙语讲解/注记逐条正确（抽查全部 Nota 盒与 121 条 P8 注记，译法准确，如 `trancher→decidir, cortar`、`la trêve→a pausa`、`une navette→vaivém entre câmaras`、`se terminer en beauté→terminar em beleza`、`il est prévu que + subjuntivo` 等）；人名拼写与法文正文一致（Dhont ×4、Ménochet、Fils、Haymitch、Lawrence、Smia、Meddour、Scott Thomas、Guiz、Mipo O、Hiroshige、Doré、Atget、Moreau、Méliès；"Dont" 0 次）；日期/数字与正文一致（16 nov. 周一、75 ans、458–0、115–1、1 260→1 500、21,8→12,7）。
- 范文 `MODÈLE` 实测 96 词（80–100 要求内）；P7 八句金句逐句核对均逐字出自 P1–P6 正文（8/8）。
- ABSTRACT.txt：一行葡萄牙语，233 B，无 ASCII `"`，内容准确（Alcaraz / Senado / Beaujolais 75 周年 / 150 题 / 16–22 nov.）。

## 7. 观察项（非缺陷，仅记录）

1. W46 复用值：P6 `head_lire` 为 `LIRE LE CALENDRIER　HORÁRIO`（`HORÁRIO` 对 `LIRE LE CALENDRIER` 为宽松意译，读者可懂，沿用未改）；P3 `bridge_dieppe`（Minidrills 复数）亦为 W46 复用值，沿用。
2. P3 ZOOM 框 `desde 1951` 与 P8 注记 Q26 `em 1951` 为不同 E 键，未统一（同 pt/nl/ru/ja/ko 各版）。
3. P2 `ET VOUS ?` 盒末行下行尖触盒边（见 §4），核心版更紧——核心继承，非 fan-out 缺陷。
4. P3 `POUR OU CONTRE ?` 框无葡语行、P5 `debat5_note` 出现两次——均与核心版一致（KIT §六已披露）。

## 8. 报告文件

- 本文件：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt1/PROOF-NOTE.md`
- 门禁日志：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt1/GATE-LOG.md`
- 证据：`gates-proof1.json`、`freeze-diff.json`、`creambox.log`、`creambox-core.log`、`p8-proof1.json`、`p8compare-proof1.json`、`occlusion-proof1.json`、`mcq-proof1.log`、`print-proof1.txt`、`web-proof1.txt`、`build-proof1.log`、`build-proof1-rerun.log`、`keytable-proof1.txt`、`png/p1.png`–`png/p8.png`、`png/crop-p7-mailbox.png`、`png/crop-p2-box.png`、`png/crop-p1-agenda.png`、`png/web-p1.png`、`png/web-p7.png`
