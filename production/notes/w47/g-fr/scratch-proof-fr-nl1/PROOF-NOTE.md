# PROOF-NOTE — W47 fr-nl 独立复校 (proof1)

- 版：`production/2026-w47/2026-w47-fr-nl/`（法语核心、读者荷兰语）
- 复校员：独立复校（与构建者不同人），2026-11-11
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-nl1/`
- 只读复校：未改任何生产文件，未 commit/push。复校前后三 SHA 不变。

## 身份核对（磁盘实测，开工前）

| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `La-Lucerna-VOL4-fr-nl.pdf`（印刷） | 17,418,864 | `dc253f3a62dd312368b81ea3e75c45b503fa31675bdad69d09fbfd0661d89cd0` | ✓ 与任务所给一致 |
| `La-Lucerna-VOL4-fr-nl-web.pdf`（网页） | 1,699,797 | `9af15b3f47eba19e95882aced708fee59b295f8dd4555ebbea037da5c17be3a4` | ✓ 与任务所给一致 |
| `2026-w47-fr-nl.text.md`（注：磁盘实名，非 `text.md`） | 46,338 | `acc84a72d786ab46009f2e0676906e919f055b1ad1293915dab37a116eefaac5` | ✓ 与任务所给一致 |

## 结论：(b) 有缺陷，不定稿

发现 1 项真实缺陷（P7 奶油盒溢出，见下）。其余全部通过：机械门 15/15 自复跑通过、
freeze 8/8、150 题逐题手验 150/150 正确、8 页逐页目视除该 1 项外零问题。

> 判定口径：缺陷虽小（基线仅超 2.6px），但为真实内容溢出——字墨切过盒边、
> 渲染图上肉眼可见接缝；且核心版同位无此问题（见对比）。按“没做好的就重做”
> 的标准，不作“小而可接受”处理。

## 缺陷清单

### D1 — P7「LE COURRIER DES LECTEURS」奶油盒：荷兰文编者注末行溢出盒底（唯一缺陷）

- 位置：P7 右下奶油盒（`LE COURRIER DES LECTEURS　LEZERSBRIEVEN`），盒
  `x=989.0, y=1878.0, w=873.0, h=380.0`，盒底 **y=2258.0**。
- 溢出行：荷兰文编者注第 3 行 `belofte in om echte inzendingen te bespreken.`
  （`x=1013.0`，基线 **y=2260.6**，字体 Noto Sans CJK SC 19.5px——即 D5 字体问题同款）。
- **PIL 真墨测量**（`/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc`，
  19.5px，基线锚点 `anchor='ls'`，`getbbox` = `(0, -16.0, 418.5, 4.5)`）：
  - 真墨 y 区间 **2244.6 – 2265.1**
  - 基线在盒底之下 **2.6px**；字墨在盒底之下 **7.1px**，在盒内 **13.4px**
  - 即：整行字形被奶油/白纸分界线横切，约上 2/3 在奶油底上、下 1/3 在白纸上。
- 目视证实：150 dpi 印刷版渲染切图 `png/p7-toolbox-bottom.png`——末行
  `belofte in om echte inzendingen te bespreken.` 字形中部确有一道奶油边切过，
  与上一行（全在奶油上）对比明显。文字本身仍可读。
- 核心版对照：core-fr 同盒（同几何 y=1878 / bottom=2258.0），中文注仅 2 行，
  末基线 2233.3，盒内余量 +24.7，无溢出。荷兰文注需 3 行（2206 / 2233.3 /
  2260.6），盒高固定，第 3 行即超。属 fan-out 翻译变长引入，非核心固有。
- creambox 规范版（`hidden_files/w47/tools/creambox.py`）对应记录：
  `box y=1878 bottom=2258.0 last baseline 2260.6 clearance -2.6`，
  inside-only 末基线 2233.3 clearance +24.7。
- 修复方向（供修复员，不由本复校执行）：缩短该荷兰文注至 2 行，或抬高盒底；
  注意同盒内法文注 2 行、Xiaomo 注 3 行均在盒内，只需处理末行。

## 150 题逐题手验：150/150 正确

方法：通读 `.text.md` 全 1087 行，逐题以法文正文核对题干、选项与键；
另核对 P8 印出答案（p8 extract 150/150）与 keytable 一致；荷兰文讲解
（Uitleg / Opmerking / Grammatica / 注记）逐条核对荷兰文正确性。

- Q1–10（P1）：gagné / mercredi / jeudi / premier / 12,7 / 22 / A / B / A / B ——全对。
- Q11–25（P2）：mercredi / lundi / jeudi / dimanche；futur proche 15–18 全对；
  19 C / 20 B / 21 A；22–25 配对 a / b / c / d ——全对。
- Q26–43（P3）：26 Vrai / 27 Faux / 28 Vrai / 29 Faux / 30 Vrai；31 gamay /
  32 jeudi / 33 Beaujeu / 34 1985；35–37 否定句全对；38 75 ans / 39 minuit /
  40 troisième / 41 B / 42 13 / 43 saucisson ——全对。
- Q44–61（P4）：44 B / 45 A / 46 C / 47 A / 48 A；49–52 a / b / c / d；
  53 plus vite / 54 plus grand / 55 moins longue；56 forfait / 57 finale /
  58 groupes / 59 tirage / 60 Bordeaux / 61 Milan ——全对。
- Q62–78（P5）：62 B / 63 B / 64 B / 65 A / 66 A；67 mercredi / 68 prequel /
  69 Ménochet / 70 21 / 71 produit / 72 acheter；73–76 a / b / c / d；
  77 des billets / 78 deux ——全对。
- Q79–96（P6）：79 B / 80 B / 81 B / 82 B / 83 C / 84 B；85–88 a / b / c / d；
  89 plus long / 90 moins simple / 91 aussi important；92 examine /
  93 ont rejeté / 94 part / 95 peut / 96 connus ——全对。
- Q97–108（P7）：97 battu / 98 est arrivé / 99 vote / 100 beauté / 101 produit /
  102 sortent / 103 rejetée / 104 jouer；105–108 改错句全对 ——全对。
- Q109–150（P8）：109 A / 110 B / 111 A / 112 B / 113 A / 114 A / 115 B / 116 A /
  117 A / 118 A / 119 B / 120 B / 121 A / 122 B / 123 A / 124 C / 125 A / 126 A /
  127 A / 128 A / 129 A；130–134 句式全对；135–139 翻译全对；140–144 a / b / c /
  d / e；145 des billets / 146 deux / 147 quelle heure / 148 devant / 149 film；
  150 Open vraag（写作键，唯一与核心不同）——全对。

荷兰文抽查无误例：`trancher = beslissen, afkappen; afsnijden`；
`Plechtige stemming: wo. 18 november`；`Vroege verkoop sinds 1951, derde
donderdag sinds 1985, 75e jubileum in 2026.`；`titelverdediger / loting /
bevestigen / pauze / speeldag`；`Bioscoop of thuis? Een oud kledingstuk krijgt
een nieuwe eigenaar, of belandt in de vuilnisbak?`；`Onderscheid prévu (gepland)
van décidé (besloten).`；P7 `sortir: in première gaan.` 与 P8 注记 Q102
`sortir = uitkomen` 各在其语境正确（通用释义 vs 影院释义）；Q114 注记
`avoir + deelwoord (geen ovk.)` 语法正确（宾语在后，无配合）。

已澄清、非缺陷：
- `SERD`：Semaine européenne de la réduction des déchets 的缩写，P2 正文有全称；
  核心版同文，沿用正确。
- P4 栏底“Jeudi 12, à Milan, puis dimanche 15, à”并非截断——句在第 3 栏顶
  以“Bordeaux : deux soirs, deux matches…”续完；P7 三栏底部短语跨栏续接亦同。
- `gold` 原始 grep 4 命中均为 base64 图数据内子串，非文字；金色值 `#b49a4a` 计数为 0。

## 8 页逐页目视（150 dpi 印刷版渲染，`png/p-1.png` … `p-8.png`）

| 页 | 结果 |
|---|---|
| P1 | 零问题。Band 两行无重叠（法文标题止 1236.9，band_r1 起 1329.4，目视净空清晰）；Uitleg 盒、LES DATES 盒、右栏、Atget 图注、QUIZ ÉCLAIR 均合。 |
| P2 | 零问题。各盒、DIRE LA DATE 表、Q11–25 均合。 |
| P3 | 零问题。ZOOM 盒、DATES À RETENIR（SERD 1er jour）、MOTS DU VIN、Q26–43 均合。 |
| P4 | 零问题。栏间续句正常，LE DÉBAT、LES MOTS DU TENNIS、MICRO-DRILLS 均合。 |
| P5 | 零问题。Méliès 图、REGARDER UN FILM、MOTS DU CINÉMA、Q62–78 均合。 |
| P6 | 零问题。LE CALENDRIER（7 行全）、Q79–96、TROIS DATES、APRÈS LE VOTE 均合。 |
| P7 | **1 处缺陷 D1**（见上）。其余零问题：四栏语法、Q97–104、CLINIQUE DES ERREURS、LA SEMAINE PROCHAINE 均合。 |
| P8 | 零问题。A–H（Q109–150）、MODÈLE 盒、RÉPONSES 四栏、Hiroshige 图注、页脚均合；最小字号 11.625pt。 |

## D5 字体问题（全周级已知待定项，如实记录，不据此单方面判 (b)）

- 普查 8 页 SVG 全部 1,659 个 `<text>` 元素（按 font-family）：
  Newsreader 945（法文正文）、**Noto Sans CJK SC 692**、Noto Serif CJK SC 17、
  DejaVu Sans 4、UnifrakturMaguntia 1（刊名）。
- **692 个 Noto Sans CJK SC 元素全部为纯拉丁字符串**（无一含 CJK 字符）：
  含全部无衬线层——刊头、band、题头、徽章、页脚，以及全部荷兰文讲解层
  （Uitleg 盒、Opmerking、Grammatica 行、注记、编者注）。例：P7 末行缺陷行
  本身即 Noto Sans CJK SC 19.5px；页脚 `Le Lucerna　FRANS WEEKBLAD VOL.4…`
  亦为该字体 17px。
- 即：讲解层拉丁字符落在 Noto Sans CJK SC，违反 SOP §1.1（与任务所述一致）。
  属共享渲染器（svglib 的 sans 映射）属性、核心版亦同，非本版引入；
  待用户定夺 scope，本复校不将其计入缺陷、不擅自修。

## 机械门（自复跑，详见 GATE-LOG.md）

15/15 通过：build 日志（run2：exit 0、TOTAL 150、零溢出）、occlusion 0、
p8 150/150 注记 121/150、p8 compare CLEAN keydiff [150]、source freeze、
string freeze、freeze baseline 8/8（scratch 复建，与出厂 SVG 逐字节同）、
print/web 文字层逐字节一致（105,398 B）、P8 最小字号 11.625pt、
U+2019=0 / U+00B7=0 / 金色 0 / 旧纸色 0 / #fbfaf6 ×8、chips 134
[10,12,18,15,14,15,12,38]、keycheck 仅 Q150 不同、MCQ 0 缺陷（45 体 1481 行）、
widths 31/31、band_spans（法文标题止 1236.9、band_r1 起 1329.4、
法文副标题止 837.2、band_r2 起 1457.5）。creambox 规范版另见 D1 与裁决。

freeze diff（`freeze.py diff`，8 页全处理，exit 0）：新增 CJK 仅 P8 的
U+3000 ×8——该字符为两段式导读条 / P8 答案流的结构分隔空白（gates.py 的
norm() 亦将其归一为空白），非中文文本；其余 7 页新增 CJK 为 0，核心中文
由 224→35、283→33、194→18、238→28、244→22、226→24、411→14、1220→190。

## 报告文件

- 本文件：`scratch-proof-fr-nl1/PROOF-NOTE.md`
- 门禁日志：`scratch-proof-fr-nl1/GATE-LOG.md`
- 原始输出：`freeze-diff.json`、`freeze-baseline.log`、`freeze-baseline-ed.log`、
  `occlusion-proof1.json/.log`、`p8-proof1.json/.log`、`p8compare-proof1.json/.log`、
  `creambox-proof1.log`、`gates-proof1.json`、`verify_gates.py`、
  `mcq-proof1.log`、`print.txt`、`web.txt`、`png/p-1.png`…`p-8.png`、
  `png/p7-toolbox-bottom.png`（D1 切图）、`png/p1-top.png`、`png/p1-agenda.png`
