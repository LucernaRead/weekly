# EDITION-RECORD — 2026-w47-fr-de

读者母语：德语（de）。核心：`2026-w47-fr-zh-cn`。最终构建 run4（2026-11-11）。

## 门禁（run4，15/15 PASS）

- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['35c72f4e', '38a1a6fc', '93a010c3', 'cd216538', '32c60e8a', '083360a7', '4bc0ef75', '7e3269a2']
- text_layer: PASS — print/web pdftotext byte-equal (104794 B); web 1704484 B < 7MB; print 17424274 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1486
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1337.5, FR sub ends 837.2, band_r2 starts 1417.5

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-de.pdf`：17,424,274 B，SHA-256 `6fff7a4f688fbc4724e0b307d1db71716244a871f2a0dcb4be3d59098fd8864f`
- 网页 PDF `La-Lucerna-VOL4-fr-de-web.pdf`：1,704,484 B，SHA-256 `751125ef971d6aa2d08219a884ba4bcd5e8eb4dc684f33218ecf9fb5ddf7cbde`
- `.text.md`：46,694 B，SHA-256 `f1c60667110623744690217646de50240c7a74170dea3b9050dad926adff88f3`，1,087 行，150 题
- 8 SVG（SHA 前 8 位）：p1 `35c72f4e`、p2 `38a1a6fc`、p3 `93a010c3`、p4 `cd216538`、p5 `32c60e8a`、p6 `083360a7`、p7 `4bc0ef75`、p8 `7e3269a2`
- `ABSTRACT.txt`（德语一行，231 B，无 ASCII `"`）：见版目录。`WEEKLY-KIT.md`：见版目录。

## 修正记录
- run1：门禁 10/14。P8 Hiroshige 图因答案流溢出未放置（`P8 HIROSHIGE NOSPACE`，答案流止于 2186.75）；P1 副标题溢出页边（EDGE，起 x=-89.4）；`agenda_sub` 413.3px 超 378.5 预算；P8 图注 3 条法文字符串缺失。根因：德语 P8 内容长于核心版（词组流 1563.52 vs 核心 1428；答案流 2186.75 vs 核心 2046）。
- run1→run2：缩短 13 处（subtitle、agenda_sub、stem_e1、注记 10 处），诊断复核词干与核心版行数一致，但答案流差 141px 仍超上限；再缩短 4 处（Q53/Q93/Q83/Q79/Q80/Q89/Q120），答案流差降至 101px。run2 门禁 14/14（当时 14 门）。
- run2→run3：目视发现 P1 导读条德语行与法文标题相接（实测起 x=1230.6，法文标题止于 1236.9，重叠 6.3px；occlusion 门未报）。根因：`precheck.py` 的 PIL `text_w` 度量比真实渲染小约 42px。修复：`band_r1` → `ALCARAZ SIEGT　SENAT STIMMT MI.`；`precheck.py` 增加 +42.4 校准常数，`band_r1` 阈值改为 ≥1252；`gates.py` 增加第 15 门 `band_spans`（读印刷版 PDF span 坐标）。同轮将 es/it 的 `band_r1` 一并缩短（预防性）。run3 门禁 15/15。
- run3→run4：`.text.md` 通读发现 Q64 注记人名拼错：`Les Braves von Dont` → `Les Braves von Dhont`（导演 Lukas Dhont）。重建后仅 P8 哈希变化（`0fa5c165` → `7e3269a2`），其余 7 页不变。
- 工具修正（本轮写入共享工具，全家庭受益）：`precheck.py` 的 band 宽度模型 +42.4 校准（PIL `text_w` 低估 U+3000 两段式导读条，en/de 实测差 42.6/42.2px；法文标题止 x=1236.9、法文副标题止 x=837.2 为 PyMuPDF 实测）；`gates.py` 增加第 15 门 `band_spans`（按基线配对 span 行，勿按 bbox 顶边——两行字号不同，顶边差 ~22px）；新增 `keytable.py`（150 键表生成器）。
- 偶发：2026-11-11 约 08:50 写盘两次报 `Disk quota exceeded`（磁盘 45G 空闲，瞬时配额故障；/tmp 与 workspace 探针写均成功，de/ 目录探针约 1 分钟后恢复，无数据丢失；KIT 与 ABSTRACT 均在故障前已写好）。
- 目视：8 版印刷版 PDF（100 dpi）零问题；P1 导读条 300 dpi 放大复核，法文标题与德语行之间净空 100.6px，清晰分开。`.text.md` 全文通读：无中文残留、无错字，150 题答案注记逐条合理。P3 `POUR OU CONTRE ?` 框无德语行、P5 `debat5_note` 出现两次，均与核心版一致（核心版同）。P8 人名逐一核对：Dhont、Ménochet、Fils、Haymitch、Lawrence、Smia、Meddour、Scott Thomas、Guiz、Mipo O 均与法文正文拼写一致；Hiroshige、Doré、Atget、Moreau、Méliès 为冻结法文图注。

## 150 键复核（对 core-fr/final-fr-p8.json）
仅 Q150 不同（写作题键为读者语言说明：核心 `开放题` → de `Offene Aufgabe`）。其余 149 键与核心版逐字相同。印出注记 121/150，与核心版注记集逐项相同。

| Q | 核心键 | de 键 | 备注 |
|---|---|---|---|
| 1 | gagné | gagné |  |
| 2 | mercredi | mercredi |  |
| 3 | jeudi | jeudi |  |
| 4 | premier | premier |  |
| 5 | 12,7 | 12,7 |  |
| 6 | 22 | 22 |  |
| 7 | A | A |  |
| 8 | B | B |  |
| 9 | A | A |  |
| 10 | B | B |  |
| 11 | mercredi | mercredi |  |
| 12 | lundi | lundi |  |
| 13 | jeudi | jeudi |  |
| 14 | dimanche | dimanche |  |
| 15 | Le Sénat va voter mercredi. | Le Sénat va voter mercredi. |  |
| 16 | Nous allons goûter le beaujolais jeudi. | Nous allons goûter le beaujolais jeudi. |  |
| 17 | Tu vas raconter ton jeudi 19 novembre. | Tu vas raconter ton jeudi 19 novembre. |  |
| 18 | Vous allez regarder les finales dimanche. | Vous allez regarder les finales dimanche. |  |
| 19 | C | C |  |
| 20 | B | B |  |
| 21 | A | A |  |
| 22 | a | a |  |
| 23 | b | b |  |
| 24 | c | c |  |
| 25 | d | d |  |
| 26 | Vrai | Vrai |  |
| 27 | Faux | Faux |  |
| 28 | Vrai | Vrai |  |
| 29 | Faux | Faux |  |
| 30 | Vrai | Vrai |  |
| 31 | gamay | gamay |  |
| 32 | jeudi | jeudi |  |
| 33 | Beaujeu | Beaujeu |  |
| 34 | 1985 | 1985 |  |
| 35 | Le vin ne se vend jamais avant le troisième jeudi. | Le vin ne se vend jamais avant le troisième jeudi. |  |
| 36 | On ne boit pas d'alcool avant 18 ans. | On ne boit pas d'alcool avant 18 ans. |  |
| 37 | Le beaujolais n'est pas un vin blanc. | Le beaujolais n'est pas un vin blanc. |  |
| 38 | 75 ans | 75 ans |  |
| 39 | minuit | minuit |  |
| 40 | troisième | troisième |  |
| 41 | B | B |  |
| 42 | 13 | 13 |  |
| 43 | saucisson | saucisson |  |
| 44 | B | B |  |
| 45 | A | A |  |
| 46 | C | C |  |
| 47 | A | A |  |
| 48 | A | A |  |
| 49 | a | a |  |
| 50 | b | b |  |
| 51 | c | c |  |
| 52 | d | d |  |
| 53 | plus vite | plus vite |  |
| 54 | plus grand | plus grand |  |
| 55 | moins longue | moins longue |  |
| 56 | forfait | forfait |  |
| 57 | finale | finale |  |
| 58 | groupes | groupes |  |
| 59 | tirage | tirage |  |
| 60 | Bordeaux | Bordeaux |  |
| 61 | Milan | Milan |  |
| 62 | B | B |  |
| 63 | B | B |  |
| 64 | B | B |  |
| 65 | A | A |  |
| 66 | A | A |  |
| 67 | mercredi | mercredi |  |
| 68 | prequel | prequel |  |
| 69 | Ménochet | Ménochet |  |
| 70 | 21 | 21 |  |
| 71 | produit | produit |  |
| 72 | acheter | acheter |  |
| 73 | a | a |  |
| 74 | b | b |  |
| 75 | c | c |  |
| 76 | d | d |  |
| 77 | des billets | des billets |  |
| 78 | deux | deux |  |
| 79 | B | B |  |
| 80 | B | B |  |
| 81 | B | B |  |
| 82 | B | B |  |
| 83 | C | C |  |
| 84 | B | B |  |
| 85 | a | a |  |
| 86 | b | b |  |
| 87 | c | c |  |
| 88 | d | d |  |
| 89 | plus long | plus long |  |
| 90 | moins simple | moins simple |  |
| 91 | aussi important | aussi important |  |
| 92 | examine | examine |  |
| 93 | ont rejeté | ont rejeté |  |
| 94 | part | part |  |
| 95 | peut | peut |  |
| 96 | connus | connus |  |
| 97 | battu | battu |  |
| 98 | est arrivé | est arrivé |  |
| 99 | vote | vote |  |
| 100 | beauté | beauté |  |
| 101 | produit | produit |  |
| 102 | sortent | sortent |  |
| 103 | rejetée | rejetée |  |
| 104 | jouer | jouer |  |
| 105 | Alcaraz a battu Shelton. | Alcaraz a battu Shelton. |  |
| 106 | Le Sénat vote mercredi. | Le Sénat vote mercredi. |  |
| 107 | Il est prévu que le Sénat examine le texte. | Il est prévu que le Sénat examine le texte. |  |
| 108 | Le beaujolais nouveau arrive jeudi 19 novembre. | Le beaujolais nouveau arrive jeudi 19 novembre. |  |
| 109 | A | A |  |
| 110 | B | B |  |
| 111 | A | A |  |
| 112 | B | B |  |
| 113 | A | A |  |
| 114 | A | A |  |
| 115 | B | B |  |
| 116 | A | A |  |
| 117 | A | A |  |
| 118 | A | A |  |
| 119 | B | B |  |
| 120 | B | B |  |
| 121 | A | A |  |
| 122 | B | B |  |
| 123 | A | A |  |
| 124 | C | C |  |
| 125 | A | A |  |
| 126 | A | A |  |
| 127 | A | A |  |
| 128 | A | A |  |
| 129 | A | A |  |
| 130 | Le Sénat va voter mercredi. | Le Sénat va voter mercredi. |  |
| 131 | Si tu venais dimanche, tu verrais les finales. | Si tu venais dimanche, tu verrais les finales. |  |
| 132 | Il a goûté le beaujolais à Beaujeu. | Il a goûté le beaujolais à Beaujeu. |  |
| 133 | Selon moi, la semaine est bien remplie. | Selon moi, la semaine est bien remplie. |  |
| 134 | Il est prévu que le Sénat examine le texte mercredi. | Il est prévu que le Sénat examine le texte mercredi. |  |
| 135 | Regarder une finale, c'est déjà apprendre le français. | Regarder une finale, c'est déjà apprendre le français. |  |
| 136 | Il court plus vite que son frère. | Il court plus vite que son frère. |  |
| 137 | Nous suivons le vote du Sénat depuis lundi. | Nous suivons le vote du Sénat depuis lundi. |  |
| 138 | Ce soir, nous allons préparer nos affaires. | Ce soir, nous allons préparer nos affaires. |  |
| 139 | On ne connaît pas encore les résultats. | On ne connaît pas encore les résultats. |  |
| 140 | a | a |  |
| 141 | b | b |  |
| 142 | c | c |  |
| 143 | d | d |  |
| 144 | e | e |  |
| 145 | des billets | des billets |  |
| 146 | deux | deux |  |
| 147 | quelle heure | quelle heure |  |
| 148 | devant | devant |  |
| 149 | film | film |  |
| 150 | 开放题 | Offene Aufgabe | 仅此题不同 |
