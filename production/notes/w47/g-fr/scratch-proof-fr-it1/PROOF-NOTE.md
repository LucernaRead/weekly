# PROOF-NOTE — W47 fr-it proof1（独立复校）

- 版：`production/2026-w47/2026-w47-fr-it/`（法语核心、读者意大利语）
- 复校员：独立复校（与构建者不同人），2026-11-11
- 结论：**(b) 有缺陷，不定稿** — 3 项缺陷（1 处版式漫出 + 2 处错字），详见下。
- 工作目录（本报告所在）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-it1/`
- 只读生产文件：复校前后重验印/网 PDF 与 text.md 的 SHA-256 未变（见 §0）；未改任何生产文件，未 commit、未 push。
- 构建解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 为 goals 侧 scratch 下 tmp。

## §0 身份核对（磁盘实测，6/6 一致）

| 文件 | 字节 | SHA-256（实测 = 任务给定） |
|---|---|---|
| 印刷 `La-Lucerna-VOL4-fr-it.pdf` | 17,415,946 | `79839baf…ee30b56` ✓ |
| 网页 `La-Lucerna-VOL4-fr-it-web.pdf` | 1,696,801 | `223287fe…dc9e5d3eaf` ✓ |
| `2026-w47-fr-it.text.md` | 46,690 | `c75ba7ef…04400a89d` ✓（注：文件名为 `2026-w47-fr-it.text.md`，非 `text.md`） |
| 核心印 `core-fr/La-Lucerna-VOL4.pdf` | 30,446,982 | `db3f2a71…f135e7` ✓ |
| 核心网 `core-fr/La-Lucerna-VOL4-web.pdf` | 2,205,749 | `26593a39…fe17823` ✓ |
| 核心 `2026-w47-fr-zh-cn.text.md` | 46,477 | `2b50c88d…660737e` ✓ |

探针：`ls /dev/null` 存在；`git hash-object -w --stdin` 通；goals 侧写文件通。

## §1 缺陷清单（3 项）

### D1 — P7 读者来信奶油盒漫出（版式缺陷）

- 位置：P7，LE COURRIER DES LECTEURS 奶油盒（`x=989.0, y=1878.0, h=380.0, bottom=2258.0`）。
- 实测：盒内末段意语注记 3 行，前两行基线 2206.0 / 2233.3，末行 `promessa di commentare invii veri.` 基线 **y=2260.6**，超出盒底 **2.6 px**。
- PIL 真墨测量（Noto Sans CJK SC 19.5 px，venv 栈，`svglib._pil("sans", False, "sans", 19.5)` + 2 倍掩膜实测）：该行墨顶 2245.1、墨底 **2265.1**，**实墨超出盒底 7.1 px**（超出的主要是行首 `promessa` 的 `p` 降部）。
- 目视：300 dpi 裁图 `p7-courrier-bottom-300dpi.png` 确认——末行压在盒沿外，`p` 降部落在盒外白底上；100 dpi 整版 P7 亦可见末行在奶油盒之外。
- 根因：意语注记段比核心中文注记多 1 行（核心末行基线 2233.3，盒内 clearance +24.7；意语 3 行，末行 2260.6）。盒高 380 为核心冻结几何。
- 范围注记（实测，非推测）：同法对 es/de/pt/nl/ru 的 P7 做 creambox 扫描，末行基线同为 2260.6、同盒底 2258.0（末行文字各为 `envíos reales.` / `echte Einsendungen zu kommentieren.` / `envios reais.` / `belofte in om echte inzendingen te bespreken` / `письма.`）；en（末行 2233.3，clearance +24.7）、ja/ko/zh-tw 无此问题。此为 fr 家庭系统性缺陷类，但本复校只判 fr-it 本版。
- 证据：`creambox.log`（P7 盒 `clearance -2.6`，BELOW-WINDOW +2.6 y=2260.6）；`p7-courrier-bottom-300dpi.png`。

### D2 — P5 词表错字：`una attrice`

- 位置：P5，MOTS DU CINÉMA　IL CINEMA 词表第 4 行。
- 实测：印为 `una attrice — attrice`；应为 `une actrice — attrice`（法语词侧须为法语冠词 `une`）。
- 源头：`expl.py:139`，键 `mots_photo` 第 4 项 `"una attrice — attrice"`。核心同键为 `"une actrice — 女演员"`（`core-fr/expl.py:152`）。
- 影响面：SVG（`p5-jeunesse.svg`）、`2026-w47-fr-it.text.md:645`、印/网 PDF 文字层（网 PDF 文字层 grep 命中）均有。
- 核查：全版词表类 E 键逐项比对法语侧（见 §4），仅此 2 处偏离；其余 `una X` 命中（`una virgola`、`una giornata`、`una palla`、`una partita`、`una settimana`、`una finale`）均为合法意语释义。

### D3 — P5 词表错字：`una séance`

- 位置：P5，同一词表第 7 行。
- 实测：印为 `una séance — spettacolo`；应为 `une séance — spettacolo`。
- 源头：`expl.py:139`，键 `mots_photo` 第 7 项 `"una séance — spettacolo"`。核心同键为 `"une séance — 场次"`（`core-fr/expl.py:154`）。
- 影响面：同 D2（SVG、text.md:651、印/网 PDF 文字层均有）。

## §2 门禁结果（独立复跑，15/15 PASS）

复跑工具：`proof_gates.py`（builder `gates.py` 的只读复刻；唯一改动：第 7 门 determinism 改为 goals 侧副本重建，绝不在生产目录内重跑）。日志：`gates-proof1.log`、`gates-proof1.json`。

| # | 门 | 实测结果 |
|---|---|---|
| 1 | run | exit 0，零 overflow/wide；TOTAL 150；A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| 2 | occlusion | 0 flags，selftest OK |
| 3 | p8_extract | keys 150/150，printed notes 121/150 |
| 4 | p8_compare | CLEAN，keydiff [150]（仅写作题键） |
| 5 | source_freeze | content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| 6 | string_freeze | 全部非 CJK 核心串每页存活；0 核心 E 残留；0 未入账 CJK；3 串豁免（翻译 E 值） |
| 7 | freeze_direct | scratch 副本重建，SVG sha256 8/8 一致：`aa3ae078 f541b51c 52b4baf0 249b0d98 7a7f178e 76cc6f87 d486ba6a e95c7ef1` |
| 8 | text_layer | 印/网 pdftotext 逐字节一致（106,326 B）；网 1,696,801 B < 7 MB；印/网各 8 页 |
| 9 | p8_font | P8 最小字号 11.625 pt ≥ 9.75 pt |
| 10 | scans | U+2019=0，U+00B7=0，gold=0，旧纸色=0，`#fbfaf6` ×8 |
| 11 | chips | 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| 12 | keycheck | 150 键对 `core-fr/final-fr-p8.json`，仅 Q150 不同 |
| 13 | mcq | bodies 45，rendered lines 1479，0 缺陷（`mcq-proof1.log`） |
| 14 | widths | 31 单行串全部在预算内 |
| 15 | band_spans | 法标题止 1236.9，band_r1 起 1307.6（净空 70.7 px），法副标题止 837.2，band_r2 起 1481.2 |

freeze 首检（`tools/freeze.py diff`，`freeze-diff.log` / `freeze-diff.json`）：8 页全出；新增 CJK 字符仅 U+3000 共 10 个（p2 1 个、p8 9 个），均为意语串内结构分隔符（如 `BEAUJOLAIS　IL QUIZ`、`140. a (sénateur = senatore　a)`），无中文残留；移除串全为中文讲解。

## §3 creambox 全版扫描（规范版 `hidden_files/w47/tools/creambox.py`）

- exit 0；33 个奶油盒；日志 `creambox.log`。
- 8 处负 clearance 的裁定：
  - 7 处为假阳性：盒内末行 clearance +47.7 / +48.0 / +48.5，负值行是下一栏目的标题（`À VOUS !　TOCCA A TE!` ×4、P2 `LA SEMAINE EN CHIFFRES`、P1 `LE MOT DE LA SEMAINE`、P6 `IL EST PRÉVU QUE + SUBJONCTIF` 与 `LE DÉBAT　DIBATTITO`）——盒外 +37.0 px 处的新标题被 +45 px 窗口捡到，非漫出。
  - 1 处真漫出：P7 读者来信盒（D1）。
- 其余盒内最小 clearance +24.7（P7-TOOLBOX 汇总）。

## §4 150 题逐题手验（text.md 1,088 行全文通读）

- text.md：CJK 字符 0、U+2019 0、U+00B7 0。
- 150 键与 `core-fr/final-fr-p8.json` 逐项比对：仅 Q150 不同（核心 `开放题` → it `Domanda aperta`）；其余 149 键逐字相同。抽查：Q26 Vrai、Q64 B（Dhont）、Q150 Domanda aperta。
- 150 题题干与 P8 答案注记逐条核对无误（题号、答案、注记一致；日期/人名/分数与正文一致，如 Q42 13、Q46 C、Q79–84 投票数 115–1 / 458–0、Q109 A lundi、Q120 B irais）。
- 意语讲解通读无错字、无中文残留；除 D2/D3 外，词表类 E 键法语侧与核心逐项比对全部一致（系统比对：全部 list 型 E 键，仅 `mots_photo` 2 处偏离）。
- Q150 注记：`Domanda aperta — punti nel riquadro; modello nel riquadro a pagina 8 (Valutazione per punti)`。
- 已知沿用项（与核心一致，不判缺陷）：P3 `POUR OU CONTRE ?` 框无意语行；P5 `debat5_note` 出现两次；`bridge_dieppe` 的 `Minidrill` 单数、`head_lire` 的 `ORARIO` 为 W46 复用值；P3 ZOOM 框与 P8 注记 Q26 为不同 E 键，未统一（`desde 1951` 式差异同 pt/nl）。

## §5 八字逐页目视（印刷 PDF 100 dpi + 300 dpi 重点）

渲染：`pg-1.png` … `pg-8.png`（100 dpi），`p1-band-300dpi.png`（P1 导读条），`p7-courrier-bottom-300dpi.png`（P7 盒底）。
- P1：干净。导读条 300 dpi 确认法标题与意语行净空清晰（70.7 px）；Atget 图、Nota 框、Q1–10 均正常。
- P2：干净。Nota 框、`LA SEMAINE EN CHIFFRES` 盒、DIRE LA DATE 表、Q11–25 均正常。
- P3：干净。ZOOM 框、DATES 表、`BEAUJOLAIS　IL QUIZ`、Q26–43 均正常。
- P4：干净。`LES MOTS DU TENNIS　PAROLE`、`LE DÉBAT` 盒、MICRO-DRILLS、Q44–61 均正常。
- P5：除 D2/D3 两处词表错字外干净（Méliès 图、电影词表其余 6 行、`LE DÉBAT` 盒、Q62–78 均正常）。
- P6：干净。`LE CALENDRIER` 表、`LIRE LE CALENDRIER　ORARIO`、比较级、MINIDRILL、Q79–96 均正常。
- P7：除 D1 漫出外干净（Doré 图、`LA PHRASE EXEMPLE` 盒、金句 Q97–104、诊所 Q105–108、`LA SEMAINE PROCHAINE` 黑底块均正常）。
- P8：干净。H 写作框、`MODÈLE` 框、答案流、Hiroshige 图与图注均正常；无溢出。
- ABSTRACT.txt：意语一行，无 ASCII `"`，内容与本版一致。WEEKLY-KIT.md 在位，内容与实测一致。

## §6 D5 字体问题（已知全周级待定项，如实记录，不据此判 (b)，不修）

- 实测（8 SVG `<text>` 元素按 `font-family` 计数）：`Noto Sans CJK SC` **691** 个、`Newsreader` 944 个、`Noto Serif CJK SC` 74 个、`UnifrakturMaguntia` 1 个、`DejaVu Sans` 4 个。
- 讲解层（sans）拉丁/意语元素一律落在 Noto Sans CJK SC：如 P1 `Voto solenne: mercoledì 18 novembre.`（19 px）、`Decidere, tagliare; interrompere.`（19 px）、眉题 `TESTI IN FRANCESE　SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`（16 px）；法文正文为 Newsreader。
- `Noto Serif CJK SC` 74 个皆为 U+3000 结构分隔 run（无中文内容）；`DejaVu Sans` 4 个为 P7 诊所 `✗` 号（符号 fallback，正常）。
- 与字体调查结论一致（`scratch-investigate-fonts/FONT-INVESTIGATION.md` §Q2：全家族级，机制在 `svglib.py` sans 分支）。待用户定夺 scope。

## 结论

**(b) 不定稿。** 15/15 机械门全过、150 题内容除 2 处错字外无误，但 P7 读者来信盒末行实墨超出盒底 7.1 px（目视可确认），另 P5 词表有 2 处法语冠词错字（`una attrice` / `una séance`）。三项均须修后重校。
