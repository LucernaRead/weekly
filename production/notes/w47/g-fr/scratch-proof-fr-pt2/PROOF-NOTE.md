# PROOF-NOTE — W47 fr-pt（法语核心 × 葡萄牙语读者）独立校对 proof1（re-fanout #2）

复校员：独立校对（与重建者不同人）。日期：2026-11-11。
目标：`production/2026-w47/2026-w47-fr-pt/`（re-fanout #2 重建版，VOL.4）。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt2/`。
生产目录零写入；core-fr 只读。门禁确定性重建在 scratch 副本中进行（`pt/rerun/`、`build-copy/`、`freeze-baseline/build-copy/`）；`git status` 上该版目录为未提交新目录，属 builder 工作状态，复校未动。

## 结论：(a) 零缺陷可定稿

首轮（fr-pt1）的唯一缺陷 D-1（P7 读者园地奶油盒注记末行漫出盒底 +2.6）已修净；Q148 错法语已修为 `devant le`。本次独立重跑全部 15 门机械门禁 + 8 项附加门禁全过，150 题逐题手验适配，八页目视干净。**无缺陷，可定稿。**

重建版改动范围（与首轮逐项比对，确认为仅两处修复，无其他变化）：
- 源码：`expl.py` 恰 1 行（P7 披露框删除中间句 `por isso publicamos um exemplo da redação claramente indicado;`）、`content8.py` 恰 2 行（Q148 键 `devant`→`devant le`；题干 `(148)___ du cinéma ?`→`(148)___ cinéma ?`），其余源码全部相同。
- SVG：仅 P7（`c3419d55`，文本元素 193→192）与 P8（`34bf3311`，两处文本改动）变化，其余 6 页与首轮逐字节相同。
- text.md：1,088 行（首轮 1,089 行——披露句删节所致）。

---

## 记录项（不计入 (a) 判定）

### R1 — Q72 句式别扭（核心冻结，首轮已记录）

- 印法：P5 `Acheter en seconde main, c'est ___ d'occasion.`，键 `acheter`（`check_mcq` 与 registry 一致，核心版逐字相同）。
- 填入后成 "c'est **acheter** d'occasion"——语法可通但句式重复拗口。属核心原文，fan-out 按 freeze 规则不得擅自偏离核心；不列为本版缺陷。

### R2 — D5 字体（全周级已知待定项，如实记录，不判、不擅自修）

- SVG 字体普查（8 页）：`Newsreader` 947 段、`Noto Sans CJK SC` 691 段、`Noto Serif CJK SC` 74 段（57 段仅为空白分隔符）、`DejaVu Sans` 4 段（P7 ✗ 标记，合理）、`UnifrakturMaguntia` 1 段（刊头黑体）。
- 其中 Noto Sans CJK SC 段中 565 段含拉丁字母且无 CJK 表意/假名/韩文（本复校计数方法），即葡萄牙语讲解层落在 Noto Sans CJK SC；与首轮同性质（首轮用另一计数法得 498 段，计数口径不同，实质相同；Noto Sans CJK SC 段数 692→691，亦为 P7 披露删行所致）。
- 网页版 PDF span 实测（首轮）：全部葡萄牙语讲解层文字落在 **LucernaNotoSansCJKSC-Reg/Bol**；法文正文为 Newsreader。即讲解层拉丁字符落在 Noto Sans CJK SC，违反 SOP §1.1——与任务书所述全周级待定项一致，记录在案，待用户定夺 scope；本复校不因此判 (b)。

### R3 — 孤儿填空行（核心继承的首轮既有观察类，不修版、不动已定稿核心）

- P8 (989.0, 843.0)：Q130 `→ ___` 单独成行，与核心逐值相同。
- P3 (538.5, 1924.1 / 2056.8)：Q36/Q37 `→ ___` 单独成行；核心同位 y=1864.7 / 1997.4（差 +59.4，约 +59.5 档）。位置档差异只记录，不判。

### R4 — P2 `ET VOUS ?` 盒紧（核心继承）

- 盒 y=974 bottom=1308.6：末行基线 1304.2，clearance +4.4，desc-clear −1.6；核心版同盒 desc-clear −2.2（比本版更紧）。下行尖刚触盒边，100 dpi 目视无漫出感（见 §5）。不列为缺陷。

---

## 1. 身份核对（磁盘实测，先核对再开工）

| 产物 | 字节 | SHA-256（实测） | 与任务书 |
|---|---|---|---|
| `La-Lucerna-VOL4-fr-pt.pdf`（印刷） | 17,420,030 | `420d79e71cc02859a5d9c8fa94c1b09ea7ae4f786c22911a4d8d2a3e7ed95521` | 一致 |
| `La-Lucerna-VOL4-fr-pt-web.pdf`（网页） | 1,702,371 | `fb88ae09d19a9b66906df2865ec15529c9f09429de22e690fbcc252ac5eff6b1` | 一致 |
| `2026-w47-fr-pt.text.md` | 46,536（1,088 行） | `172f28dc192ea023b64bffb3e84f8a7106b4ff46f9db11a6a5d08d0f6b9efbdd` | 一致 |

探针：`/dev/null` 存在，`git hash-object -w --stdin` 通（`9daeafb9…`）；TMPDIR 用本 scratch 下 `tmp/`。

## 2. freeze 首检（venv：Pillow 13.0.0 / FreeType 2.14.3）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-pt/svg`：8/8 页。新增 CJK 合计 11 个，**全部为 U+3000（全角空格）**：p2 ×1、p8 ×10，其余页 0——两段式导读条/栏目标题/注记流的分隔符，本家庭各版通用结构；`string_freeze` 门记为 0 未入账 CJK 字符。无新增 CJK 汉字/假名/韩文。无简体中文残留。

标准核心比对（`freeze.py baseline --build . --core-svg svg`，核心目录内运行）：rc=0，**8/8** 字节相同，核心 SVG 跑后重哈希未变。日志：`freeze-diff.json`、`freeze-baseline.json`。

## 3. 机械门禁（独立重跑，15/15 PASS）

用 fr-it2 版 `gates.py` 的 pt 改编副本（输出改到本 scratch `pt/`；确定性重跑改在 `build-copy/` 中做，生产目录零写入；全部 venv python 运行均加 `PYTHONDONTWRITEBYTECODE=1`），tag `proof2`，exit 0：

| 门 | 结果（独立重跑实测） |
|---|---|
| run | PASS — exit 0，零 overflow/wide；TOTAL 150；by level A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion | PASS — 0 flags，selftest OK（真实审计命令；`pt/occlusion-proof2.json` 本体 `flag_count: 0`） |
| p8_extract | PASS — keys 150/150，printed notes 121/150 |
| p8_compare | PASS — CLEAN，keydiff [150]（仅写作题键；直接读 `pt/p8compare-proof2.json` 本体，非 gates.json 转述） |
| source_freeze | PASS — content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | PASS — 核心非 CJK 串逐页存活；0 核心 E 残留；0 未入账 CJK；1 条翻译豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| freeze_direct | PASS — `build-copy/` 独立重建，8/8 SVG SHA 全同：`a8ca67ea, 1c7f056e, 13a8fe0a, d9b6af38, 2a66a9f0, 5ef9766c, c3419d55, 34bf3311`（另一次 `pt/rerun/` 重建亦 8/8） |
| text_layer | PASS — 印/网 pdftotext 逐字节一致（104,688 B）；网 1,702,371 B < 7MB；印 17,420,030 B |
| p8_font | PASS — P8 最小字号 11.625pt ≥ 10pt |
| scans | PASS — U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS — 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck | PASS — 150 键对核心 `final-fr-p8.json`，仅 Q150 不同 |
| mcq | PASS — bodies: 45，rendered lines: 1482，0 缺陷 |
| widths | PASS — 31 条单行串全部在预算内 |
| band_spans | PASS — 法文标题止 1236.9，band_r1 起 1270.9（净空 34.0）；法文副标题止 837.2，band_r2 起 1489.2 |

完整 JSON：`pt/gates-proof2.json`；日志：`GATE-LOG.md`。

## 4. 首轮 D-1 修复复验（P7 披露框）与 creambox 全版扫描

- **D-1 已修净**：P7 右栏 `LE COURRIER DES LECTEURS / CARTAS DOS LEITORES` 奶油盒（y=1878，盒底 2258.0）。披露由 3 行缩为 2 行（`expl.py:182` 删除中间句；P7 SVG 文本元素 193→192）：
  - 法文例文 3 行（1956–2015.6）、Xiaomo 注记 3 行（2066–2122.0）、法文披露 2 行（2142–2170）、葡语披露 2 行（2206–2233.3）；
  - 盒内末基线 **2233.3**，inside-only clearance **+24.7**，desc-clear +18.8——与核心版同盒逐值相同。
- PIL 真墨测量（印刷版 PDF，250 dpi，`png/crop-p7-mailbox-300dpi.png`）：奶油 render 色 (239,237,228)，纸白 (251,249,246)；奶油末行 svg 2258.3 ≈ 盒底 2258.0；披露末行真墨末行 svg **2237.6**；间隙 2258–2269 **零墨**；svg 2270.0 起为下一栏深绿带矩形顶——非溢出。
- creambox 规范版扫 8 页（`creambox-proof2.log`）：7 条 BELOW-WINDOW 全为下一栏目标题假阳性（盒内 clearance +47.7/+48.0/+48.5）；其余紧盒见 R4 与 P1 agenda 盒（与核心逐值相同）。

## 5. 八页逐页目视（印刷版 PDF，100 dpi，全页；另抽查网页版 P1/P7）

- P1：干净。导读条法文标题止 1236.9 / 葡语行起 1270.9，净空 34.0 清晰；Atget 图注完整；`Nota` 盒、日期盒、`DANS CE NUMÉRO`、`LE MOT DE LA SEMAINE` 均干净。Atget 照片中一处小白方块经核对为原图资产（atget-paris.jpg）内既有亮部（窗/招牌），非渲染缺陷。
- P2：干净。`Nota` 盒、Châtillon 图、`LE SAVIEZ-VOUS ?`、`ET VOUS ?` 盒（见 R4）、`DIRE LA DATE`、`EXERCICES` Q11–25 均干净。
- P3：干净。`POUR OU CONTRE ?` 框无葡语行（与核心版一致，已记入 KIT §六）；ZOOM 框 `1951/1985/2026` + 葡语行完整；`BEAUJOLAIS O QUIZ`、`DATES À RETENIR` 干净；Moreau 图注完整。Q36/Q37 填空行单独成行（见 R3）。
- P4：干净。`LES PHRASES DU COMMENTATEUR`（`Allez ! / Quelle action ! / Il marque ! / C'est gagné !` + 葡译）完整；`LES CHIFFRES DU SPORT`、`LES MOTS DU TENNIS`、`À SUIVRE`、`MICRO-DRILLS`、`LE DÉBAT` 干净。
- P5：干净。Méliès 图注完整；词表 `une actrice — atriz`、`une séance — sessão` 正确（任务提示：fr-it 的 P5 词表是 une actrice，法语正确词；本版同词无误）；`REGARDER UN FILM`、`OÙ SORTIR`、`MOTS DU CINÉMA`、`LE CINÉMA DU MERCREDI`、`LE DÉBAT` 干净；`debat5_note` 出现两次，与核心版一致。
- P6：干净。`LE CALENDRIER` 全 7 行 + 来源行完整（`9 déc. Vote solennel : le budget de l'État`，与 Q83=C 一致）；`TROIS DATES`、`LE DÉBAT`、`APRÈS LE VOTE`、`LIRE LE CALENDRIER`、`LES MOTS`、`MICRO-DRILLS` 干净。
- P7：干净。语法四栏、`LA PHRASE EXEMPLE` 三盒、Doré 图注、`LES PHRASES DE LA SEMAINE` Q97–104、`CLINIQUE DES ERREURS` Q105–108、邮箱盒（D-1 已修净）、`LA SEMAINE PROCHAINE` 深绿带均干净。
- P8：干净。A–H 全部题区、对话 `(148)___ cinéma ?`（无 `du`）、`MODÈLE`（96 词）、`RÉPONSES` 121 条注记（`148. devant le (À porta do cinema)`）、Hiroshige 图注完整；答案流 2106.15，图置于 2116.15，页内无重叠。
- 网页版抽查 P1/P7：与印刷版同版式，P7 邮箱盒同样修复。
- 全页图：`png/p1.png`–`png/p8.png`；裁图：`png/crop-p7-mailbox-300dpi.png`；网页抽查：`png/web-p1.png`、`png/web-p7.png`。

## 6. 150 题逐题手验（对 registry + 题干 + 正文 + 注记）

- 独立抽取 p8 键 150/150，与核心逐键比对，**仅 Q150 不同**（核心 `开放题` → pt `Pergunta aberta`，写作题读者语言说明，属预期）；其余 149 键逐字相同。`key-stem-check.txt` 逐题列表亦同。
- 逐题核对答案与题干/正文的一致性（全部 150 键的答案语义，重点核对易错点）：
  - Q1–Q6 gagné / mercredi / jeudi / premier / 12,7 / 22；Q7–Q10 A/B/A/B；Q11–14 mercredi / lundi / jeudi / dimanche；Q15–18 未来 proche 四句；Q19–21 C/B/A（Q19 儿童节 20 nov.、Q20 减废周 21 nov. 均与 P2 正文一致）；Q22–25 a/b/c/d（配对左右列逐对验：vote→décision ensemble、primeur→vin de l'année、déchet→ce qu'on jette、finale→dernier match）；Q26–30 Vrai/Faux/Vrai/Faux/Vrai；Q31–34 gamay/jeudi/Beaujeu/1985；Q35–37 否定改写；Q38–40 75 ans/minuit/troisième；Q41 B / Q42 13 / Q43 saucisson；Q44–48 B/A/C/A/A；Q49–52 a/b/c/d；Q53–55 plus vite/plus grand/moins longue；Q56–61 forfait/finale/groupes/tirage/Bordeaux/Milan；Q62–66 B/B/B/A/A；Q67–72 mercredi/prequel/Ménochet/21/produit/acheter（Q72 见 R1）；Q73–76 a/b/c/d；Q77–78 des billets/deux；Q79–84 B/B/B/A/B/**C**/B（Q83=C 已三重核对：核心 `final-fr-p8.json` C、P8 印出 `83. C (Votação solene 9 dez.)`、P6 日历 `9 déc. Vote solennel : le budget de l'État` 一致；9 déc. 为预算投票，18 nov. 为 Sécu 投票）；Q85–88 a/b/c/d；Q89–91 plus long/moins simple/aussi important；Q92–96 examine/ont rejeté/part/peut/connus；Q97–104 battu/est arrivé/vote/beauté/produit/sortent/rejetée/jouer；Q105–108 改错四句；Q109–116 A/B/A/A/A/B/A/A（完形：16 nov. 为周一 lundi、Beaujeu、résultats、goûté、propose、aimé、jouent、écrit）；Q117–124 A/A/B/B/A/B/A/C；Q125–129 A/A/A/A/A；Q130–134 句型转换（Q131 `Si tu venais dimanche, tu verrais les finales.`、Q134 `Il est prévu que le Sénat examine le texte mercredi.`）；Q135–139 葡→法翻译（`Regarder une finale…` / `Il court plus vite que son frère.` / `Nous suivons le vote du Sénat depuis lundi.` / `Ce soir, nous allons préparer nos affaires.` / `On ne connaît pas encore les résultats.`，均与葡语题干语义一致；Q137–139 为与核心相同的翻译键，只有 Q150 写作键是读者语）；Q140–144 a/b/c/d/e；Q145–149 des billets/deux/quelle heure/**devant le**/film（对话逐句验：`On se retrouve devant le cinéma ?` 语法成立）；Q150 Pergunta aberta。
  - Q102 注：注记 `sortir = estrear, sair` 为影院释义，P7 语法行 `sortir: estrear, sair` 与之统一，各自正确。
  - Q148：已修为 `devant le`（registry / `content8.py:170` / P8 extract / P8 SVG 题干 / text.md 答案五重一致）。
- `.text.md` 全文通读 1,088 行：CJK 字符 0；`«` 74 / `»` 74 成对；U+2019=0；U+00B7=0；"Dont" 0；葡萄牙语讲解/注记逐条正确；人名拼写与法文正文一致（Dhont、Ménochet、Fils、Haymitch、Lawrence、Smia、Meddour、Scott Thomas、Guiz、Mipo O、Hiroshige、Doré、Atget、Moreau、Méliès；"Dont" 0 次）；日期/数字与正文一致（16 nov. 周一、75 ans、458–0、115–1、1 260→1 500、21,8→12,7）。
- 范文 `MODÈLE` 实测 96 词（80–100 要求内）；P7 八句金句逐句核对均逐字出自 P1–P6 正文（8/8）。
- ABSTRACT.txt：一行葡萄牙语，233 B，无 ASCII `"`，内容准确（Alcaraz / Senado / Beaujolais 75 周年 / 150 题 / 16–22 nov.）。

## 7. 观察项（非缺陷，仅记录）

1. W46 复用值：P6 `head_lire` 为 `LIRE LE CALENDRIER　HORÁRIO`（`HORÁRIO` 对 `LIRE LE CALENDRIER` 为宽松意译，读者可懂，沿用未改）；P3 `bridge_dieppe`（Minidrills 复数）亦为 W46 复用值，沿用。
2. P3 ZOOM 框 `desde 1951` 与 P8 注记 Q26 `em 1951` 为不同 E 键，未统一（同 pt/nl/ru/ja/ko 各版）。
3. P2 `ET VOUS ?` 盒末行下行尖触盒边（见 R4），核心版更紧——核心继承，非 fan-out 缺陷。
4. P3 `POUR OU CONTRE ?` 框无葡语行、P5 `debat5_note` 出现两次——均与核心版一致（KIT §六已披露）。
5. 首轮 PROOF-NOTE §4 称 P5 盒 bottom=2357.7 为笔误；首轮 `creambox.log` 第 216 行实为 bottom=2387.4，与本轮一致。

## 8. 报告文件

- 本文件：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt2/PROOF-NOTE.md`
- 门禁日志：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt2/GATE-LOG.md`
- 证据：`pt/gates-proof2.json`、`pt/gates-proof2.log`、`freeze-diff.json`、`freeze-baseline.json`、`freeze-baseline.log`、`creambox-proof2.log`、`creambox-core.log`、`pt/p8-proof2.json`、`pt/p8compare-proof2.json`、`pt/occlusion-proof2.json`、`pt/extra-proof2.json`、`pt/mcq-proof2.log`、`pt/print-proof2.txt`、`pt/web-proof2.txt`、`pt/build-proof2.log`、`pt/build-proof2-rerun.log`、`pt/registry-proof2.json`、`key-stem-check.txt`、`check-s11-proof2.log`、`verify-ed-proof2.log`、`spill-boxtitle-proof2.log`、`pil-p7-proof2.log`、`png/p1.png`–`png/p8.png`、`png/crop-p7-mailbox-300dpi.png`、`png/web-p1.png`、`png/web-p7.png`
