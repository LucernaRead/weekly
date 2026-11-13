# EDITION-RECORD — 2026-w47-fr-it

读者母语：意大利语（it）。核心：`2026-w47-fr-zh-cn`。最终构建 run2（2026-11-11）。

## 门禁（run2，15/15 PASS）

- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 3 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['aa3ae078', 'f541b51c', '52b4baf0', '249b0d98', '7a7f178e', '76cc6f87', 'd486ba6a', 'e95c7ef1']
- text_layer: PASS — print/web pdftotext byte-equal (106326 B); web 1696801 B < 7MB; print 17415946 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1479
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1307.6, FR sub ends 837.2, band_r2 starts 1481.2

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-it.pdf`：17,415,946 B，SHA-256 `79839bafd07e439122c64533a891a4810fa9bc0dc75bf557255211a06ee30b56`
- 网页 PDF `La-Lucerna-VOL4-fr-it-web.pdf`：1,696,801 B，SHA-256 `223287fef53f2c557ab3a19e2b9e453bfe50bce98ab7363fad052fdc9e5d3eaf`
- `.text.md`：46,690 B，SHA-256 `c75ba7ef0a59fcfc4b17cde8f488e9effd7afb7c66f50b5baf6ff0084400a89d`，1,088 行，150 题
- 8 SVG（SHA 前 8 位）：p1 `aa3ae078`、p2 `f541b51c`、p3 `52b4baf0`、p4 `249b0d98`、p5 `7a7f178e`、p6 `76cc6f87`、p7 `d486ba6a`、p8 `e95c7ef1`
- `ABSTRACT.txt`（意大利语一行，见版目录，无 ASCII `"`）。`WEEKLY-KIT.md`：见版目录。

## 修正记录
- 构建前诊断：词干行数 1/1/1/1/1（`stem_e3` 比核心版少 1 行），答案流差 222px（上限 124px）。批一缩短 17 处注记（Q5/Q3/Q6/Q10/Q47/Q53/Q57/Q59/Q58/Q64/Q72/Q93/Q92/Q89/Q126/Q135/Q114；Q6/Q10 为两键共用值），差值 222px → 141px。批二切分模拟：P8 末行 397px 单刀不够，P4 的 Q57 单刀 ~60px 可落行——Q57 `Finale singolare dom.` → `Finale dom.`，差值 141px → 121px。
- run1：门禁 13/15。P3 主框题 `BEAUJOLAIS　QUIZ DEL BEAUJOLAIS` 超框宽（HEAD TOO WIDE，与 es 同类缺陷）；`head_mots_fetes` 418.4px、`head_mots_photo` 452.5px 超 400.5 预算。修复：`head_dieppe_ex` → `BEAUJOLAIS　IL QUIZ`；`head_mots_fetes` → `LES MOTS DU VIN　IL VINO`；`head_mots_photo` → `MOTS DU CINÉMA　IL CINEMA`。run2 门禁 15/15。
- 本版无磁盘配额中断。
- 目视：8 版印刷版 PDF（100 dpi）零问题；P1 导读条 300 dpi 放大复核，法文标题与意大利语行之间净空 70.7px，清晰分开。`.text.md` 全文通读：无中文残留、无错字，150 题答案注记逐条合理。P3 `POUR OU CONTRE ?` 框无意大利语行、P5 `debat5_note` 出现两次，均与核心版一致（核心版同）。`bridge_dieppe` 的 `Minidrill`（单数）与 P4/P6 的 `MINIDRILL`、`head_lire` 的 `ORARIO` 均为 W46 复用值，沿用未改。P8 人名逐一核对：Dhont、Ménochet、Fils、Haymitch、Lawrence、Smia、Meddour、Scott Thomas、Guiz、Mipo O 均与法文正文拼写一致；Hiroshige、Doré、Atget、Moreau、Méliès 为冻结法文图注。

## 150 键复核（对 core-fr/final-fr-p8.json）
仅 Q150 不同（写作题键为读者语言说明：核心 `开放题` → it `Domanda aperta`）。其余 149 键与核心版逐字相同。印出注记 121/150，与核心版注记集逐项相同。

| Q | 核心键 | it 键 | 备注 |
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
| 150 | 开放题 | Domanda aperta | 仅此题不同 |
