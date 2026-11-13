# EDITION RECORD — 2026-w47-fr-pt（葡萄牙语读者版）

- 状态：DONE（2026-11-11，run2，门禁 15/15 PASS）
- 版目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-fr-pt/`
- 印刷 PDF：`La-Lucerna-VOL4-fr-pt.pdf`，17,420,079 字节，SHA-256 `dc64cb43fcf8a87cc6234a10e0912daf5afc4b77e1299cea6a17424989e3f6c3`
- 网页 PDF：`La-Lucerna-VOL4-fr-pt-web.pdf`（`-web.pdf`，fr 家庭惯例），1,702,412 字节，SHA-256 `1b7eb1cfa8f9f7a94cc5575f937d73a08332a3750c5206f8ee5bb3ebbcd3644b`
- `.text.md`：`2026-w47-fr-pt.text.md`，46,601 字节，SHA-256 `45aa52c54faa11ce0d0dfcffb8682aa1198850ce2f5ea62ae0d8efe74cb9c8a6`，1,088 行，150 题
- ABSTRACT.txt：233 字节（葡萄牙语）
- KIT：`WEEKLY-KIT.md`（10,197 字节）
- 讲解层：318 键，138 复用 / 180 新译 / 14 冻结；`gloss_prefix` "Nota — "，`note_wrap` "half"
- 构建与门禁解释器：`~/workspace/weekly-git/tools/venv/bin/python`（PIL 13.0.0）

## 门禁日志（run2，15/15 PASS）

- run: exit 0, zero overflow/wide; TOTAL 150；按级 A2 53 · B1 75 · B2 22；按版 10/15/18/18/17/18/12/42
- occlusion: 0 flags, selftest OK
- p8_extract: keys 150/150, printed notes 121/150
- p8_compare: CLEAN, keydiff [150] (writing key only)
- source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values（核心版 `stem_e1` 前缀 `Traduisez : `）
- freeze_direct: two builds sha256 8/8 identical: [`a8ca67ea`, `1c7f056e`, `13a8fe0a`, `d9b6af38`, `2a66a9f0`, `5ef9766c`, `ea3d710b`, `7d582103`]
- text_layer: print/web pdftotext byte-equal (104850 B); web 1702412 B < 7MB; print 17420079 B
- p8_font: P8 min font 11.625pt >= 9.75pt
- scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: bodies: 45  rendered lines: 1483
- widths: 31 single-line strings all within budget
- band_spans: FR title ends 1236.9, band_r1 starts 1270.9, FR sub ends 837.2, band_r2 starts 1489.2

run1 为 14/15：唯一失败 `widths`（`agenda_note` 400.4 > 378.5）；修复 `agenda_note` → `Votação solene: quarta 18 de novembro.` 后 run2 15/15。P8 词组流 1427.52、答案流 2106.15、Hiroshige 放置于 2116.15。

## 目视 QA（印刷版 PDF 渲染，100 dpi，8 页）

- P1–P8 零问题；P1 导读条 300 dpi 裁切（PDF-y 380–470）复核：法文标题止于 1236.9，葡语 `band_r1` 起于 1270.9，净空 34.0，清晰分离。
- P3 `POUR OU CONTRE ?` 框无葡语行、P5 `debat5_note` 出现两次，均与核心版一致。P7 Doré 图 + 图注、P8 Hiroshige 图 + 图注、MODÈLE 框均在位，无遮挡。
- `.text.md` 全文通读（1,088 行）：无中文残留、无错字；答案抽查 Q41 B、Q45 A、Q79 B、Q80 B、Q120 B、Q121 A、Q122 B、Q135 均与法文题干一致；人名逐一核对法文正文：Dhont、Ménochet、Fils、Haymitch、Francis Lawrence、Mipo O、Alexandre Smia、Mounia Meddour、Kristin Scott Thomas、Guillermo Guiz 均无误。Q150 注记：`Pergunta aberta — pontos no quadro; modelo no quadro da página 8 (Avaliação por pontos)`。

## 修正经过（摘要，详见 KIT §五）

- 构建前诊断：词干 1/1/2/1/1 与核心一致；答案流差 282px（上限 124px，本家庭至今最长）；批一 54 处注记缩短、26 条复用键转为新译，差值 → 81px。
- 构建前预扫：`head_dieppe_ex` / `head_mots_fetes` / `head_mots_photo` 三处均超宽，构建前改短（`BEAUJOLAIS　O QUIZ` / `LES MOTS DU VIN　O VINHO` / `MOTS DU CINÉMA　O CINEMA`）。
- 诊断中断两次：`/tmp` 写满（诊断工作目录移至 scratch 内 `diag-wd/pt/`）；开发侧通知打断诊断命令（重建 `pt/` 后重跑，无损失）。

## 150 键表（核心键 vs pt 键，`keytable.py pt run2`）

diff keys: [150]
| Q | 核心键 | pt 键 | 备注 |
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
| 150 | 开放题 | Pergunta aberta | 仅此题不同 |
