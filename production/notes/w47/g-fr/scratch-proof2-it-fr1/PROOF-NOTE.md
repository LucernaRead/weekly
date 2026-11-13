# PROOF-NOTE — W47 it-fr (法语读者 × 意大利语目标) proof2 · 重扩散新版

## 结论：(a) 零缺陷，可定稿

全量重校（SOP §8.4）完成：150 题逐题复核、1317 行全文精读、8 页逐版看图、
20 门机械门禁独立重跑、三 SHA 开工/收工两次核对、印 PDF 重渲逐字节比对。
**零缺陷。** 下方“记录在案的观察”共 5 项，均非缺陷（各有实测值与判定理由），
不触发返工。

## 对象与 SHA（开工、收工两次核对一致）

- 版：`production/2026-w47/2026-w47-it-fr/`，重扩散新版（核心 fix3 commit `36bdec2e`）
- 印 `La-Lucerna-VOL4-FR.pdf` — sha256
  `6e393b3d385c606443c82b7813ddfae2623b9ee2fff128690247f1f2f0fcf00f` / 14,034,074 B
- 网 `La-Lucerna-VOL4-FR-web.pdf` — sha256
  `7276c70ff46caf931ba761ec3ca36f7b8ee467c1c1d22931f460eaa81596b77f` / 1,290,987 B
- 文 `2026-w47-it-fr.text.md` — sha256
  `a634057bfdf97f0c29492ba769c96213a6540ef15f8a1cbf17bc88ed51dc92f7` / 56,538 B / 1317 行
- KIT §7 所载印/网 SHA 与字节数与盘上一致；文本 SHA 与
  `scratch-refanout-it/FANOUT-REPORT-it.md` 所载一致。

## 工作方式（只读生产）

- 磁盘探针通过（`git hash-object -w /dev/null` 成功 + scratch 真实写盘）。
- 全部重跑在 goals-side scratch
  `hidden_files/w47/scratch-proof2-it-fr1/` 内做：整版复制到 `build/` 后跑
  run.py / render.py（BASE 重定向到 scratch 副本）；生产文件零写入，
  收工重验三 SHA + 8 个 SVG sha256 全部不变。
- `PYTHONDONTWRITEBYTECODE=1` 全程；`TMPDIR` 为自有 scratch `tmp/`。
- web PDF 未重渲染（字节不可复现），只比文字层（见门 7）。
- 门禁未复用 fan-out 的日志结论：`gates.py` / `translations.py` /
  `validate_edition_textmd.py` 复制到自有 scratch、路径重定向后独立重跑 20/20。

## 门禁汇总（详见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| run.py RC=0 / 150 题 / 0 溢出 | PASS（TOTAL 150；A2 47 / B1 70 / B2 33；P1–P8 10/18/18/18/18/18/12/38；0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE） |
| SVG 重建 8/8 字节一致 | PASS（`sha256sum -c` 8/8 OK；各页 flow 末端与 KIT §8 逐值一致） |
| 重渲印 PDF 与交付逐字节相同 | PASS（重渲 sha256 `6e393b3d…`，14,034,074 B，与交付完全一致） |
| freeze 核心 baseline 8/8 | PASS（`tools/freeze.py baseline` 8/8；交付 SVG 跑后重验不变） |
| freeze diff（P1–P7） | PASS（0 unexplained；新增 CJK 仅 U+3000 ×8） |
| occlusion | PASS（0 flags；自检 OK） |
| 奶油盒 PIL 真墨像素扫 | PASS（29 盒全过；最薄见观察 O1） |
| spill | 0（build 日志 0 溢出 + 全部 flow 末端在界内 + 奶油盒像素扫） |
| 孤儿扫 | 0 真孤儿（见“孤儿扫”节；仅 1 处行内独词换行，见观察 O3） |
| p8 extract | PASS（150/150） |
| p8 compare | PASS（CLEAN，keydiff 实测 [137, 138, 139]，与预期一致） |
| P8 最小字号 | PASS（13.0 px = 9.75 pt，§1.1 下限） |
| §1.1 | PASS（#fbfaf6；无金/砖/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点；徽章三色；无双重外框） |
| 日期星期全验 | PASS（全部星期主张逐项 `date` 核对，见下） |
| KIT §1/§7 三 SHA | PASS（见上） |
| 20 门 gates.py | 20/20 PASS（独立重跑，非复用 fan-out 日志） |

## 全文精读（1317 行，逐题）

- 意大利语目标层：与核心 freeze 0 unexplained，8 句金句逐句核对均在正文原样
  出现 ×2（`La Lazio resta in vetta`、`ventiquattro gol in dieci partite`、
  `il ponte votivo sul Canal Grande`、`oltre centocinquanta figuranti…`、
  `la squadra di Gattuso…`、`sette giorni di libri, ragioni e follie`、
  `il testo può ancora cambiare`、`approvato dal governo non vuol dire già legge`）。
- 法语讲解层：拼写、性数配合、变位、标点逐行读过，无错误；150 条答案的
  key 与 note 逐题对照题干/正文/图表复核，算术 13−11=2、6+7=13、
  99 词范文（逐词数过 = 99）全部正确。
- Q137–140 本地化标签：L969/971/973/975 为 `Traduire en français` ×3 +
  `Traduire en italien` ×1，`「翻譯」` 残留 0；Q137「Pour la Madonna della
  Salute, on traverse le pont votif.」/ Q138 / Q139 / Q140 译文均正确。
- 禁用词（Ucraina/Russia/Putin）0 命中；非 U+3000 的 CJK/西里尔字符 0；
  U+3000 ×101（家具分隔符）。
- 日期星期（`TZ=Europe/Rome date -d` 全验）：MD11 11 月 6 日周五–8 日周日；
  11 月 9 日周一、12 日周四（意–法）、15 日周日（比–意）、16 日周一、
  17 日周二（修正案截止）、19 日周四、20 日周五、21 日周六、22 日周日、
  23 日周一（BookCity 开幕）、24 日周二（Torino Film Festival 开幕）、
  29 日周日、12 月 2 日周三、12 月 6 日周日（松露集截止）、12 月 31 日周四。
  文中全部星期主张（LUN 16 / MAR 17 / GIO 19 / VEN 20 / SAB 21 / DOM 22 /
  martedì 17 / giovedì 12 / lunedì 23 / martedì 24 / VEN 6.11 / SAB 7.11 /
  DOM 8.11）逐项正确；MER 18 无条目（D12 已接受，不编造）。
- 事实交叉：积分榜（Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 /
  Udinese 5）、10 场赛果、24 球、31 球最佳攻击、Torrone 29 届 11 月 7–22 日、
  Eurochocolate 32 届 11 月 13–22 日、BookCity 15 届 1360 场、
  Torino Film Festival 44 届 11 月 24 日–12 月 2 日（9 天）、DPB 10 月 15 日、
  法案 C. 3174-bis、听证 11 月 9–12 日——与正文、表格、习题三方一致。
- 标题数实测（“56 titles”为幻数）：本版 `##` 页标题 8 个；文章头条 6 条；
  全大写标题行 27 行（含赛果表日标 5 行、时间线标签 4 行），盒标题 proper
  18 个。按任一自然口径计数均不为 56。

## 奶油盒像素裁决（交付渲染像素为准）

- 对重建卡片（与交付 SVG 字节一致、印 PDF 重渲逐字节一致，同一渲染）
  做逐盒像素扫：29 个无边框奶油盒（#f0eee5），盒内最右墨点与盒边的
  余量全部 ≥0，最薄者见 O1；其余盒余量 +7 至 +189 px。
- 四个表修标题的像素实测（PIL 真墨仅作交叉核对）：
  D1 cifre **+7–8 px**（PIL 称 +4.5，实测更宽）；D2 subtitle **0 px**
  （见 O1）；D3 frase +9 px（PIL +8.5）；D4 errori +110–111 px（PIL +111.5）。
- 方法发现：PIL `measure.py` 与 cairosvg 实际渲染对同一字符串可差约 ±5 px
  （hint 逐字进位取整所致：D2 字符串 PIL 进位 394.95 px，cairosvg 实渲
  400.5 px；D1 反向差约 3.5 px）。故 PIL 数值不得作为盒标题的裁决依据，
  本版一律以渲染像素裁决——这正是 O1 的由来。

## 孤儿扫

- 粗扫 90 旗均为误报（级别徽章 A2/B1/B2、时间线标签、盒标题、图表值、
  拆分的单行多节点）。精扫（Newsreader 正文流 + P8 键列表内逐行重建）：
  **0 处栏断孤儿**（栏顶/栏底独词）。
- 仅 1 处行内独词换行：P8 Q139 键第二行只剩 `domicile`（见观察 O3）；
  另 Q137 第二行 `Compare avec l'original` 为完整短语，非独词。

## 8 版逐版看图

- 联系表（8 页）+ P1 / P7 / P8 全页 + P1 D2 字幕裁图 + P8 Q139 裁图。
  版式干净一致：无溢出、重叠、压页脚、缺字（tofu）、图片错位。
  P3/P5 中部结构空白为核心既有版式（KIT §10 已接受），非缺陷。

## 记录在案的观察（非缺陷，不返工）

### O1 — D2 副标题像素余量 0 px：字墨恰触盒边，未越界
- 位置：`p1-prima.svg`，LA SETTIMANA 盒（x=1439.5, y=588, w=422.5, h=700，
  右边 x=1862）；节点 `Cette sem.　Cosa succede, giorno per giorno`
  （x=1461.5, y=694, 19 px, Noto Sans CJK SC，见 `svg/p1-prima.svg` 内该
  `<text>` 行）。
- 实测：单节点隔离 cairosvg 渲染最右墨 x=1861（余量 +1 px，阈值 40）；
  含子像素抗锯齿边缘则触至 x=1862（余量 0 px，列 x=1862 在盒高 700 行中
  693 行为纯纸色，仅 5–7 个像素为字形子像素边缘色 (205,245,246) 等，
  x≥1863 在任何阈值（≥5）下无墨）。字形完整、无裁切。
- 判定为非缺陷的理由：① 墨未越界，盒无边框、边几不可见，视觉上无缺陷
  （裁图 `crop-d2-subtitle.png` 为证）；② 渲染确定性（印 PDF 重渲逐字节
  一致），余量稳定，非抖动；③ 同族已接受先例：it-de D1 副标题
  （PIL +5.5）像素实测同样为 0 px（`2026-w47-it-de/cards/p1-prima.png`
  同法实测 ink-right=1862），已随 de 版定稿；④ 该法语形式已是最短式
  （全称 `Cette semaine` 更长），无更短替代。
- 注意：fan-out 报告所称 D2 “+5.5 px” 为 PIL 方法值，像素真相为 0 px；
  同理 D1 “+4.5 px”像素真相为 +7–8 px。PIL 误差 ±5 px（见“方法发现”）。

### O2 — D1 cifre 标题像素余量 +7–8 px（PIL +4.5 为悲观估计）
- 位置：`p1-prima.svg`，`LA SETTIMANA IN CIFRE　CHIFFRES`（x=556.5,
  y≈1400, 23 px 粗体），盒右 x=961。单节点实渲 ink-right=953–954。
  任务书所记“fr D1 +4.5 px 薄边”以此像素实测裁定：实际余量 +7–8 px，
  在盒内，无处理。

### O3 — P8 Q139 键第二行独词 `domicile`
- 位置：`svg/p8-valutazione.svg`，y=2172 行
  `139. Samedi, la Lazio joue à domicile contre Lecce. — in casa = à`，
  y=2187 行仅 `domicile`（x=1440，3 栏）；渲染裁图
  `crop-p8-q139.png` 为证。
- 判定为非缺陷的理由：① 非栏断孤儿——两行相邻、同属一条答案，读者
  可自然连读，无歧义、无丢失；② 2 行的 139 键已在 KIT §9 明确量测并接受
  （`139 = 2 lines`，P8 总量 4533 px < 4576 px 容量）；③ 同族接受模式：
  it-en / it-de 的 Q137 同样占 2 行；④ 全版 150 键中仅此 1 处独词换行，
  Q137 第二行是完整短语。
- 若日后想收紧，一句话可修（缩短 note `in casa = à domicile`），但
  本版不以此为由返工。

### O4 — 其余文体小注（均非缺陷）
- 动词变位注释（16–20、60–61）用全角冒号 `：`（如
  `attraversare：i veneziani → attraversano`），系核心冻结原样沿用
  （KIT §8 已记），非 fan-out 残留。
- `(bougies (pluriel))` 双括号（13/14/37 题），全版统一写法。
- P2 E TU 法语行是意大利题干的简写提示，未译出“最佳作品登 VOL.5”
  从句；该承诺的法语版在 P7 LETTERE 披露中完整给出，故读者不失信息。
- Q137 note `(Compare avec l'original)` 为指向性提示而非释义，与
  138/139 的释义式 note 不同，但作为翻译题的提示足用。
- Q58 note `le plus beau dimanche soir (un jugement)` 将阴性 `serata`
  按意译为阳性 `dimanche soir`，为释义式意译（KIT §9 原定），非语法主张。

## 只读合规

- 生产文件零修改：三 SHA 收工重验与开工一致；8 个 SVG sha256 重验一致；
  `git status` 仅见 re-fan-out 遗留的未追踪整版目录（非本次改动）。
- 未 commit、未 push、未重渲染交付的 web PDF；未改动 `core-it/`。

## 证据位置

- `hidden_files/w47/scratch-proof2-it-fr1/`：
  `PROOF-NOTE.md`（本件）、`GATE-LOG.md`、`run-rebuild.log`、
  `render/render.log`、`render/La-Lucerna-VOL4-FR-rerender.pdf`、
  `freeze-baseline.log`、`gates/gates-fr.log`、`cream-scan.log`、
  `contact-sheet.png`、`crop-d2-subtitle.png`、`crop-p8-q139.png`、
  `shipped-svg.sha256`、`cream_scan.py`。
