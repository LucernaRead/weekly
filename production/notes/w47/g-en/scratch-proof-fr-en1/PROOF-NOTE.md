# PROOF-NOTE — W47 fr-en proof1（独立复校）

- 版：`production/2026-w47/2026-w47-fr-en/`（法语核心、读者英语）
- 复校员：独立复校（与构建者不同人）；只读生产文件，未改任何生产文件，未 commit/push。
- 日期：2026-11-11；工作目录：`hidden_files/w47/scratch-proof-fr-en1/`
- 构建解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 用 goals 侧 scratch/tmp。

## 结论：(b) 有缺陷，不定稿

1 项真实缺陷（D1，见下）。其余全部复校项通过。

## 身份核对（磁盘实测，先于开工）

| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `La-Lucerna-VOL4-fr-en.pdf` | 17,418,994 | `e97e9f7b845d42be75ca085f33c61e8ee7518bc57d79c75b586c695b1c42b7cd` | 吻合 |
| `La-Lucerna-VOL4-fr-en-web.pdf` | 1,663,511 | `2ef460c16cee6c844d0cb4be4a627399c596e0eefe469b014d7ff92dfb8592da` | 吻合 |
| `2026-w47-fr-en.text.md` | 46,190 | `349e20c97cd8632a0f3ea7e198b0974ab03edb535340f3d2606615a69f7f6db9` | 吻合 |

## 缺陷清单

### D1 — P8 答案注记 Q64 人名拼错：`Dont` 应为 `Dhont`（唯一缺陷）

- 位置：P8 RÉPONSES 区，`— PAGE 5 —` 行，`64. B (Les Braves by Dont)`。
- 实测值（印刷 PDF，PyMuPDF span）：bbox `(557.79, 1563.73)–(697.02, 1580.57)` pt，11.625pt，字体 `NotoSansCJKsc-Regular`，文本 `64. B (Les Braves by Dont)`。
- SVG 源：`svg/p8-exercices.svg`，`<text x="538.5" y="2102.96" font-family="Noto Sans CJK SC" font-size="15.5" fill="#302c28">…64. B (Les Braves by Dont)</text>`。
- 值源：`expl.py:264`，`"n_photo3": "Les Braves by Dont"`。
- text.md 同文：`64. B (Les Braves by Dont)`。
- 正确形式证据：
  - 本版 P5 正文：`« Les Braves », le drame historique de Lukas Dhont`；P5 Q64 选项 B：`B. Lukas Dhont`。
  - 核心版注记：`n_photo3 = "勇者是东特作品"`（东特 = Dhont 的正确音译）。
  - de 版同轮已修同一错字（run4：`Dont`→`Dhont`）。
- 影响：仅一处括号注记里的一个人名少一个字母 h；题键 B 本身正确，不影响答题与判分。修复 = 只改 `expl.py` 的 `n_photo3` 一值，仅 P8 哈希变（同 de 版 run4 的修复粒度）。
- PIL 真墨核实：150 dpi 印刷版 P8 与 100 dpi 网页版 P8 渲染图中，该行均清晰印为 `64. B (Les Braves by Dont)`（见 `png-print/p-8.png`、`png-web/p-8.png`）。

## 观察项（记录，不判 (b)，不擅自修）

### O-D5 — 讲解层拉丁字符落在 Noto Sans CJK SC（已知全周级待定项）

- 实测：8 页 SVG 中 `font-family="Noto Sans CJK SC"` 的 `<text>` 共 692 处（P1 76 / P2 70 / P3 75 / P4 61 / P5 62 / P6 72 / P7 77 / P8 199）；`Newsreader` 945 处，`Noto Serif CJK SC` 74 处，`DejaVu Sans` 4 处，`UnifrakturMaguntia` 1 处。
- 实例：P2 英文译注 `Tell us about your 19 November: write two sentences in French and send them in.` 落在 `font-family="Noto Sans CJK SC" font-size="20" fill="#6f675d"`（`p2-vie.svg`）。
- 印刷 PDF 嵌入字体含多份 `NotoSansCJKsc-Regular/Bold` 子集（cid），证实该字体实际用于拉丁文字。
- SOP §1.1 字体表：刊别、讲解层、栏目小字、页眉页脚——拉丁读者语言用 Newsreader；并明文「不用思源宋体自带的拉丁字形排西文」。本版讲解层英文用 Noto Sans CJK SC，与该条不符。
- 按简报要求：如实记录，不因此单方面判 (b)，不擅自修；待用户定夺 scope。本缺陷清单的 (b) 结论仅由 D1 导致，与 O-D5 无关。

## 已裁定为非缺陷（实测证据）

- **P1 Atget 照片上的白色小方块**：是源照片本身的内容（褪色墙面招牌 `AU RENDEZ-VOUS DES BONS [■] PÊCHEURS` 中间一块白色）。证据：从印刷 PDF 提取嵌入图（xref 7，1280×1595），同一白方块在源图内，位于源图约 (60%, 57%) 处。
- **P2 ET VOUS 盒 desc-clear −1.0**：creambox 仅此一盒 desc-clear 为负（盒 y=974，底 1337.6，末行基线 1332.6，clearance +5.0，末行 `in.`）。300 dpi 裁图（`crop-p2-etvous.png`）证实 `in.` 整行在奶油盒内，盒底边在其下清晰可见；`in.` 无下行字母，−1.0 纯为 0.30×字号启发式余量，非真漫出。
- **creambox BELOW-WINDOW −24.0 / −37.0（8 处）**：全部为已知假阳性类——下一栏目标题：+24.0 `LE MOT DE LA SEMAINE` 1 处；+37.0 `LA SEMAINE EN CHIFFRES` / `À VOUS !　YOUR TURN` ×3 / `IL EST PRÉVU QUE + SUBJONCTIF` / `LE DÉBAT　DEBATE` 等 7 处。33 盒 inside-only clearance 全为正，最小 +5.0（即上条 P2 盒）。
- **`三色蛾`（3 个汉字在 SVG 内）**：仅 P1 一处，在蛾标矢量图的 `<title>Lucerna 三色蛾</title>` 内（无障碍标题，非渲染文字）；印刷/网页 PDF 文字层中为 0 次；核心版同文。非中文残留。
- **freeze diff 新增 CJK 仅 U+3000 ×9**（P6 1、P7 1、P8 7）：全角空格分隔符，非汉字；无新增汉字。
- **`vote=vote` 式注记（Q22、Q87）**：法语 `vote` 的英文即 `vote`，译法正确、仅简略，非错误。

## 机械门禁（独立重跑，见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| freeze diff（core-svg vs edition-svg） | 8 页；新增 CJK 仅 U+3000 ×9；无新增汉字 |
| freeze baseline（scratch 内复现构建） | **8/8 SVG 字节一致**（d832422e / f200006f / 4867f169 / 14690fda / 8d7d907b / 087ab1a5 / 5476d2d0 / f310354a） |
| occlusion_audit.py | 0 flags，selftest OK |
| p8 extract --total 150 | keys 150/150，printed notes 121/150 |
| p8 compare vs core | CLEAN，keydiff [150] |
| source_freeze | PASS：content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | PASS：核心非 CJK 串全存活；0 核心 E 残留；0 未入账 CJK；1 条豁免（翻译 E 值） |
| text_layer | PASS：印/网 pdftotext 逐字节一致（105,574 B）；网 1,663,511 B < 7MB |
| p8_font | PASS：P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸=0，#fbfaf6 ×8 |
| chips | PASS：134 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck vs core final-fr-p8.json | PASS：仅 Q150 不同（写作题键） |
| check_mcq.py | PASS：0 defects（bodies 45，rendered lines 1481） |
| widths（svglib.text_w，31 串 + 4 组共行） | PASS：全部在预算内 |
| band_spans（印刷版 PDF span 实测） | PASS：法文标题止 1236.9，band_r1 起 1252.1（净空 15.2px），法文副标题止 837.2，band_r2 起 1467.1 |
| creambox.py 全版扫描 | 33 盒，inside-only 全正（最小 +5.0）；P7 工具盒 4 盒，最小 inside +24.7，最小 desc-clear +18.8 |

注：构建者简报称门禁 15/15，但其 en run4 记录实为 14/14（第 15 门 band_spans 是 de 轮后加的）。本复校把 band_spans 作为第 15 门独立重跑，通过。另：repo 内无名为 `check_core` 的独立工具（tools/ 与 fanout scratch 均无）；等价的核心一致性检查（freeze diff + source/string freeze + keycheck）已在本复校内直接跑过。

## 目视（印刷版 PDF 150 dpi 全 8 页 + 网页版 P1/P8 100 dpi + 2 张裁图）

- P1：干净。band 无重叠（band_r1 起 1252.1）；Atget 照已核实；QUIZ ÉCLAIR Q7–10 四栏齐整；页脚 Page 1 of 8。
- P2：干净。ET VOUS 盒末行在盒内（已裁图核实）；DIRE LA DATE 表、EXERCICES Q11–21 齐整。
- P3：干净。NOTE 盒、ZOOM 盒、DATES 表、POUR OU CONTRE、LES MOTS DU VIN 齐整；Q26–43 齐整。
- P4：干净。LES CHIFFRES、LES MOTS DU TENNIS、MICRO-DRILLS Q56–61、两处 LE DÉBAT 齐整；Q44–55 齐整。
- P5：干净。Méliès 图、REGARDER UN FILM、OÙ SORTIR、MOTS DU CINÉMA、LE CINÉMA DU MERCREDI 齐整；Q62–78 齐整。Q64 题干内 `Lukas Dhont` 拼写正确（错仅在 P8 注记）。
- P6：干净。LE CALENDRIER 表 7 行、LIRE LE CALENDRIER、LES PHRASES DES JOURNAUX、IL EST PRÉVU QUE、LE COMPARATIF、MICRO-DRILLS 齐整；P6 译注框无 `NOTE NOTE` 残留（run3→run4 修复已核实）；Q79–96 齐整。
- P7：干净。四栏 A2/B1/B2/TOOLBOX、Doré 图、LES PHRASES Q97–104、CLINIQUE Q105–108、读者来信、VOL.5 预告盒齐整。
- P8：干净。A–H 各节、MODÈLE 范文、Hiroshige 图、RÉPONSES 全 150 条齐整；仅 D1 一处错字（见上）。
- 网页版 P1/P8 与印刷版同版式同内容（文字层逐字节一致已另验）。

## 150 题逐题手验

- 键表：p8.py extract 150/150；与核心 `final-fr-p8.json` 逐键比对，仅 Q150 不同（`开放题`→`Open question`，写作题键为读者语言说明，预期内）。
- 键 vs text.md P8 答案区：150/150 一致（Q150 仅多注记后缀，键本身一致）。
- 逐题核对题干与答案：Q1–Q149 逐题对照正文/题干核实，无错键、无与正文矛盾的答案（核查要点：日期星期与题干一致；Q48 键 A `vendredi 20` 与 P4 正文「11e journée se jouera du 20 au 22 novembre」一致；Q109 `lundi 16` 与真实日历一致，`date -d` 核实 2026-11-16 星期一至 11-22 星期日）。
- text.md 全文通读 1,088 行：无中文残留（汉字 0），无 U+2019、无 U+00B7，无错字（除 D1 注记错字）；人名拼写与法文原文一致（Dhont、Ménochet、Fils、Heimlich、Lawrence、Smia、Meddour、Scott Thomas、Guiz、Méliès、Doré、Hiroshige、Atget、Moreau）。
- 150 题计数：P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42；分级 A2 53 · B1 75 · B2 22。

## 其他核实

- ABSTRACT.txt：英文一行（Alcaraz / Senate / Beaujolais 梗概，150 题，A2–B2，16–22 November 2026）。
- WEEKLY-KIT.md：与核心版一致的说明（318 键 expl，164 复用 + 154 新译 + 14 冻结法语键；note_wrap half；gloss_prefix `NOTE　`）。
- 构建者 run4 记录（run1 P6 g6 溢出、run2 P1 band 重叠、run3 P6 `NOTE NOTE`）所述的三处历史修复，本复校在成稿中逐一核实已无残留。

## 环境备注

- `/dev/null` 在本机 exec 调用之间会消失（每次 git 前须 `touch /dev/null` 重建；`sudo mknod /dev/null c 1 3` 报 Operation not permitted，容器限制；目前为普通空文件，git 可用）。已在每次 git 调用前重建，未影响核对。
- 本复校未在生产目录内重跑 `run.py`（gates.py 第 7 门会原地重写 SVG）；确定性改用 `freeze.py baseline` 在 scratch 副本内重跑，8/8 字节一致，生产文件未被触碰。
