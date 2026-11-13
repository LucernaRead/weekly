# GATE-LOG — 2026-W47 it-ko proof2 全量复校门禁日志

- 版：`2026-w47-it-ko`（it × ko，VOL.4，重扩散新版）
- 复校：proof2（独立重跑，不引用 proof1/他版结论；他版数字仅作对照，不作裁决依据）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-ko1/`
- 环境：`tools/venv/bin/python`（Pillow 13.0.0；本版为 it 家，用 venv 栈）；`TMPDIR=$S/tmp`；凡 import 生产源码一律 `PYTHONDONTWRITEBYTECODE=1`；跑前先读 `OUT`/`BASE` 写目标确认为 scratch。
- 约定：GD = GATE DONE；PASS = 通过；FAIL = 失败。结论：19/19 PASS，0 FAIL，0 缺陷（详见 `PROOF-NOTE.md`）。

## G0 开工探针与 SHA 盘核 — PASS

| 项 | 实测 |
|---|---|
| `git -C ~/workspace/weekly-git hash-object -w /dev/null` | `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0 |
| probe 文件 | `$S/probe.txt` 真实写入 |
| 印 PDF `La-Lucerna-VOL4-KO.pdf` | 19,296,912 B，`d5698327bbb331d0270e5ca86c531068fe8425f0ff11251747fc4ddd9768b7a3`（与任务值一致） |
| 网 PDF `La-Lucerna-VOL4-KO-web.pdf` | 1,607,490 B，`85722a84c68bb1e03b2bde56462d23ffc0855405ae4e4911d71e04adc819086e`（一致） |
| `2026-w47-it-ko.text.md` | 57,347 B，`e9dbe37172028913924567df9445604a4bd79584fe910de4c487662b8ab45614`（一致） |
| 校对后复核（2026-11-11 21:04 UTC 前后） | 三 SHA 仍为上值；生产 `__pycache__` 的 .pyc 时间戳为 2026-11-11 12:24（建版时产生，早于本任务），无生产文件 mtime 晚于 text.md；生产未动 |

## G1 run.py 全版重跑 — PASS（`logs/run.log`）

- 命令：`scratch/rebuild/` 内运行 `run.py`（OUT 重定向为 scratch 绝对路径；读 OUT/BASE 写目标确认为 scratch 后跑）。
- 结果：RC=0；`TOTAL 150`（A2 47 / B1 70 / B2 33）；页 10/18/18/18/18/18/12/38（≤ 起点 15/20/21/21/21/21/12/40）；模型词 99；`FLOW OVERFLOW: 0`，`HEAD TOO WIDE: 0`，`NOSPACE: 0`。

## G2 SVG 重建逐字节比对 — PASS（`logs/rebuilt-svg.sha256`）

- 命令：`sha256sum rebuild/svg/*.svg` vs 生产 `svg/*.svg`。
- 结果：8/8 逐字节一致（`p1-prima` … `p8-valutazione`）。

## G3 印 PDF 重渲逐字节比对 — PASS（`logs/render.log`）

- 命令：`rebuild/render.py`（venv）→ `$S/rebuild/La-Lucerna-VOL4-KO.pdf`。
- 结果：大小 19,296,912 B，SHA `d5698327…` 与交付逐字节相同。

## G4 网 PDF 重建 + 文字层比对 — PASS（观察 O6）（`logs/webpdf.log`）

- 命令：`tools/webpdf.py $S/rebuild/La-Lucerna-VOL4-KO.pdf $S/rebuild/La-Lucerna-VOL4-KO-web.pdf`（venv）。
- 结果：RC=0；重建 PDF 1,607,485 B（比交付小 5 B），差异在若干子集字体流的压缩长度（/Length1 ±2，解压后等长）——fontTools 子集化跨进程非字节稳定，Web-PDF 字节身份从不是门禁。逐页文字层：PyMuPDF 文本（NFC + 空白折叠）8 页逐页相同，合计 46,953 B；逐页词多重集（7,414 词）相同；字体名集合与 Producer/Title 元数据相同（见 G14）。

## G5 freeze baseline（核心 it）— PASS（`logs/freeze-baseline.log`）

- 命令：`tools/freeze.py --frozen ~/workspace/weekly-git/production/2026-w47/core-it --core-svg ~/workspace/weekly-git/production/2026-w47/core-it/svg --out $S/freeze-baseline/`（venv）。
- 前置核实：核心 md5 与 KIT §11 一致（`content8.py 629b5b0a…`、`content12.py 91cdfbb9…`、`content34.py 18926942…`）；build-copy 与 `core-it` 逐文件比对：仅 5 个 content 文件各差 2 行（OUT 重定向），bslib4/svglib/run 完全相同；content 中除 scratch 路径外无 "it-ko" 字样；`--core-svg` 指向核心 svg 子目录（不是整仓，也不是本版的生产 svg）。
- 结果：8/8 逐字节一致，RC=0；核心 SVG 跑前后 md5 未变（未写生产）。

## G6 freeze diff（核心 → 本版）— PASS（`ko/freeze-diff.json`）

- 命令：`tools/freeze.py --diff $S/freeze-baseline/build-copy/svg $E/svg`（venv）。
- 结果：P1–P7 0 未解释片段；P8 由 G8/G9（p8 extract + compare + 150 键审计）覆盖。

## G7 occlusion 几何遮挡审计 — PASS（`logs/gates-ko.log`）

- 命令：`tools/occlusion_audit.py`（fuzz=1.0px，scale 2.0833）。
- 结果：**0 flags**（0 图片遮挡（*）/ 0 文本遮挡（.）/ 0 盒遮挡（+））。

## G8 p8 extract — PASS（`ko/p8-extract.json`）

- 命令：`tools/p8.py`（frozen = `$S/freeze-baseline/build-copy`，edition = `$E`）。
- 结果：noted **150/150**。

## G9 p8 compare vs 核心 — PASS（`ko/p8-compare.json`）

- 命令：`tools/p8.py` compare。
- 结果：verdict **CLEAN**；keydiff `[137, 138, 139]`（与 it 家预期一致：Q137–139 为 E 节重定向的韩语读者句键；Q140 的键在核心与本版都是意大利语，无差异是正确行为）。

## G10 §1.1 干净 — PASS（`logs/gates-ko.log`）

- 纸面 `#fbfaf6` 有；非正文全页矩形 0 个；无金 (#c9a227)、砖红、近黑（#1a1a1a/#333333 最接近票未中）；金 #998844 仅用于债券袖标与周末标记（预期）；VOL.4 ×9（含 P1 masthead 顶部细条、页脚、讲义）；VOL.5 仅 3 处节点（全为合法内容点：P1 A2 段 + P2 E TU? + P7 LETTERE，核心同；SOP §1.1 规定，下周/讲义可标 VOL.5）；徽章色 A2/B1/B2 齐全；Unicode 补充与字体（Newsreader / Noto Serif CJK KR / Noto Sans CJK KR / UnifrakturMaguntia）通过；字体谱：Noto Serif CJK KR(Normal,700,400…)、Noto Sans CJK KR(Normal,700)、Newsreader(400)、Newsreader Medium、UnifrakturMaguntia(400)；14–128px 扫描：悬空 image rect 0 个；K6/K7 不在本地（不依赖，不复制）。
- 补充（`logs/gates-ko.log` 内 `sweep.py` — 仅读，分析版内文本）：`TEXT.md` 中‘·’共 **151** 个，全部为选项 A./B./C. 与版本词表（四语言版无其他语言）；禁词（Ucraina/Russia/Putin）0 命中；abstract 引用与 markdown 一致；受限样式 0；exa 三点（P1 段落、P6 row level、P6 字号）与核心一致。

## G11 creambox 奶油盒横/纵向扫 — PASS（`logs/creambox.log`，canonical 工具 md5 `ee7a55d8b2057cf4ad42a97bb1197383`）

- 全部负 clearance 均为 +45px 窗口的假阳性（下块标题，盒下 24–44px）：P1 三处（ADESSO TU +37.0、LA PAROLA DELLA SETTIMANA +24.0、QUIZ LAMPO 说明 +44.0）、P3 一处（IL TORRAZZO +37.0）、P4 三处（斑马表素行）、P6 两处（ESERCIZI 6면 연습 +42.0）。
- 9 处 desc-clear 负值（−0.9…−1.5，0.30em 保守系数）全部经交付 PDF 像素实测澄清（G13）：真墨距盒底 +3.72~+5.58px，无越盒。
- 各盒 inside-only clearance 全部为正（+4.5~+47.7）；P7 工具盒汇总：3 盒，最小盒内 clearance +4.5（下方工具盒标题），最小 desc-clear −1.5（LA PAROLA，实测真墨余量 +3.84）。
- P4 斑马表：21/21 行与核心同位置、同文本——核心冻结设计。

## G12 横向溢出 PIL 真墨扫描 — PASS，转 G13 实测（`logs/h-overflow.log`）

- 脚本：`h-overflow-proof2.py`（KR 字体适配，45px 跨度）；扫描 2,217 个文本节点；发现 3 处 +0.4~+0.5px 旗标（P1 刊头行、P1 QUIZ LAMPO 行、P8 头带副行）。
- PIL advance 系工具模型；裁决以 G13 交付 PDF 像素为准。

## G13 交付 PDF 像素实测（行级 + 全页）— PASS（`logs/pixel-check.log`、`logs/rowlevel.log`）

- 渲染：交付印 PDF 以 200 dpi 出 8 页 `pages/pdf-p-{1..8}.png`（4063×5625，SCALE 2.0833）；核心 P8 对照 `pages/core-p8-8.png`。
- 9 个 desc-clear 盒：真墨底距盒底 **+3.72~+5.58 SVG px**（阈值灰度<200；详见 PROOF-NOTE §4.1 表）。
- 3 处 PIL 旗标行：真墨右缘 1860.96（−1.04）、1855.68（−6.32）、1851.84（−10.16），全部在 1862 边内。
- 全页右缘扫描：P1/P3/P4/P6/P7 最右 1861.44（−0.56）；P2（y 1585–1588，8 行）、P5（y 601–604，6 行）+0.40px 均为抗锯齿毛边（0 实色像素，最浅灰度 104）；P8 模型文行 +1.36px 见下；左缘 87.36px 聚类：P1 band 矩形（y 470–588）、照片左缘（y 1876–2194）、A2 徽章（y 2367–2394）+ x=88 位置文本字形毛边，非溢出；页脚最右 1859.52。
- **P8 模型文行级实测**（行带窗口，仅限该行，不伸进 gutter；徽章在栏外，不计）：基线 631.33 与 652.13 的两行真墨右缘均为 1863.36（+1.36px = 1.02pt）；越边像素 18/21 个、实色（<100）12/13 个、最深灰度 45；核心印 PDF P8 同位渲染逐像素相同（+1.36px、18/21、12/13）——冻结核心固有行为，越边为区空白纸面，无裁切/重叠（观察 O2，非缺陷）。
- 9 盒全部清白，P8 模型文两行记录为观察（详见 PROOF-NOTE §4.2，裁图 `out/crops/p8-model-right-edge.png`）。

## G14 印/网文字层逐页比对（posdiff/msdiff）— PASS（`logs/gates-ko.log`）

- 印 vs 网：8 页词多重集全同（7,414 词）；词框 posdiff（0.1pt 取整）：P2–P8 0 差异；P1 仅刊头两词 x 差 0.4–0.5pt（“La” 印 404.8/网 404.3，“Lucerna” 印 599.5/网 599.1，y 81.3 相同）——子集字体重测（观察 O7）。
- P8 min 字号：印 PDF PyMuPDF 统计最小 9.75pt（737 spans），最大 34.5pt；星体标注要素按 SOP 1.1 15.9px / 26.5px 界限计。

## G15 150 题三源逐题手验 — PASS（`logs/threeway.log`）

- 脚本：`threeway.py` —— 登记 `out/reg.json`（`dump_reg.py` 从 rebuild 的 `run.py` 导出）vs text.md 正文键 vs `translations.py` Risposte 键/notes vs P8 印出键（`ko/p8-extract.json`）。
- 结果：**MISMATCHES: 0**（Q150 写作题无字面键，按设计跳过；REG 级别/页码/题型与 KIT 一致）。首跑 70 项假阳性系脚本误吞键表后 `[빈칸 채우기]` 标记所致，修正后重跑为 0（用法修复，内容无改动）。
- 150/150 键与核心一致（keydiff [137,138,139] 除外）；notes 与 translations.py 一致（137–140 + 写作题除外）；9 条无表 notes 为冻结意大利语动词变位（16–20、60–61）与算术（85–86），逐字节照搬、无 CJK。
- 8 金句：本版与核心中各恰好 2 次（正文 + P7），逐字一致。模型词：text.md 计 99 词，与 run 日志一致。
- 标题数实测：≥26.5px 非空节点 48、不同基线 35、标题项 **43**（P1 7、P2 7、P3 6、P4 6、P5 6、P6 6、P7 3、P8 2；定义：同行多 run 合并、band 左右分列标题分计）；“56 titles” 三口径均未复现，为幻数。

## G16 内容通读（全文 1,317 行 + 事实/日期/算术）— PASS

- text.md 全文通读：无拼写/语法/截断/事实错误；韩语讲解层无他语残留（SVG 汉字/假名扫描 0 命中）。
- 日期：20 个日期 `date -d`（Europe/Rome）全验——11 月 16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、12 月 2 日周三、12 月 6 日周日、12 月 31 日周四、10 月 15 日周四、10 月 28 日周三、11 月 9 日周一、11 月 12 日周四、11 月 6–8 日周五–周日、11 月 13 日周五、11 月 14 日周六，全部与正文星期表述一致。
- 算术：13−11=2（Q85）、6+7=13（Q86）、Torrone 11 月 7–22 日=16 天·3 个周末、TFF 11 月 24 日–12 月 2 日=9 天、BookCity 数字 1,360/2,487/1,164/443 与 Q70/73/80 一致。
- 事实抽查（核心冻结内容，复核一致）：Madonna della Salute 1630 年许愿、圣殿 1631–1687 年 Longhena、植树节 1898 年起源/2013 年立法、Torrone 1441 年 10 月 25 日 Sforza–Visconti 婚礼、Eurochocolate 第 32 届、TFF 第 44 届（1982 创立）、BookCity 第 15 届、Colson Whitehead 两届普利策、Sinner 2025 年 ATP 总决赛冠军；总分榜 29/28/27/24/23/5 与 10 场比分（24 球）自洽；比分在头条/P4 正文/积分榜/结果表/题键中共六处一致。
- 意大利语动词形式（futuro、passato prossimo、congiuntivo、比较级）逐题手验，无误。

## G17 8 页逐页目视（交付印 PDF 渲染，view/p{1..8}.png）— PASS

| 页 | 目视结论 |
|---|---|
| P1 | 干净。刊头、头条带、六题练习、LA SETTIMANA 盒、IN CIFRE 盒、体育场照片、QUIZ LAMPO 条、页脚均齐全；无溢出/重叠/压页脚/豆腐；头条无首字下沉（核心同）。 |
| P2 | 干净。四栏正文、运河画、Canaletto 图注、LO SAPEVI?、E TU? 盒、全宽 IL 21 NOVEMBRE 节、练习 11–28 均齐全；P2 副标行 +0.40px 为图注行抗锯齿（G13 已澄清）。 |
| P3 | 干净。Torrazzo 照、IL WEEKEND DOLCE、E TU? 盒、练习 29–46 齐全；中段第三栏留白为核心既有格局（KIT 已披露）。 |
| P4 | 干净。斑马结果表 5 行（核心冻结设计，G11 已核）、积分榜、E TU? 盒、练习 47–64 齐全。 |
| P5 | 干净。Corot 画、I GIOVANI IN NUMERI、E TU? 盒、练习 65–82 齐全；中段第三栏留白为核心既有格局；IL PIANO 第 2/3 条韩语括注 “)” 独占一行（观察 O1，裁图 `out/crops/p5-il-piano-dangle.png`）；词表第二行以 ‘·’ 开头（KIT 已披露，观察 O5）。 |
| P6 | 干净。MINIME DI ESEMPIO 条形图（5°, 6°, 7°, 11°, 13° 单调递增）、PROPOSTA ≠ LEGGE 盒、LA STRADA DELLA MANOVRA 时间线、LEGGERE I NUMERI 盒、练习 83–100 齐全。 |
| P7 | 干净。A2/B1/B2 语法三栏、练习 101–112、但丁像、ERRORI TIPICI、LA PAROLA、LETTERE 盒、8 金句、LA PROSSIMA SETTIMANA (VOL.5) 条齐全。 |
| P8 | 干净。A–H 练习区、Vermeer 图、RISPOSTE 150 键四栏齐全；Q32 键用 “Fate dolci” 直引号（观察 O4，裁图 `out/crops/p8-key32-quotes.png`）；模型文右缘 +1.36px（观察 O2，G13 实测）；无页脚侵入。 |

- 孤儿/寡行：8 页目视无单行独占栏端/栏首；P2 栏 1→栏 2（“Giornata nazionale” 接 “degli alberi…”）、P4 栏 2→栏 3（“E la Nazionale? Le due notti azzurre” 接 “— giovedì 12 novembre…”）均为跨栏续句，后续多行，无单行 strand。

## G18 KIT K6/K7 — 未碰（任务指定另派文档收尾）

- 未读、未改、未引用 KIT K6/K7。

## G19 证据与产物清单

- 日志：`logs/`（`run`、`render`、`webpdf`、`freeze-baseline`、`gates-ko`、`h-overflow`、`creambox`、`threeway`、`pixel-check`、`rowlevel`、`dump_reg`）。
- 数据：`ko/p8-extract.json`、`ko/p8-compare.json`、`ko/freeze-diff.json`、`out/reg.json`、`logs/rebuilt-svg.sha256`。
- 渲染与裁图：`pages/`（交付印 PDF 200 dpi 8 页 + 核心 P8 对照页）、`view/p{1..8}.png`（目视用缩图）、`out/crops/`（P5 括注、P8 模型文右缘、P8 键 32 引号、P5 词表、P4 斑马表）。
- 重建：`rebuild/`（源码副本 + 重建 SVG + 重建印/网 PDF + `cards/`）、`freeze-baseline/build-copy/`（核心复现副本）。
- 结论文件：`PROOF-NOTE.md`（结论 (a) 零缺陷可定稿，9 项观察）、本文件。

## 观察项总表（不计缺陷）

O1 P5 IL PIANO 第 2/3 条 “)” 独占一行；O2 P8 模型文 +1.36px（与核心渲染逐像素相同）；O3 P2/P5 +0.40px 抗锯齿毛边；O4 Q32 “Fate dolci” 直引号 vs 正文 «»；O5 P5 词表第二行 ‘·’ 开头；O6 网 PDF 重建差 5 B（字体子集非字节稳定）；O7 P1 刊头印/网 x 差 0.4–0.5pt；O8 P4 日标签重复（核心冻结设计）；O9 P1 无首字下沉、P3/P5 中段留白（核心既有格局）。详见 `PROOF-NOTE.md` §4–§6。
