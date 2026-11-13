# W47 fr-ru re-proof · GATE-LOG（独立全量复校，逐项实测）

- 解释器：`tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3，PyMuPDF）
- 版目录（只读核对）：`production/2026-w47/2026-w47-fr-ru/`；核心：`production/2026-w47/core-fr/`
- 本日志目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-fr-ru1/`（构建副本 `build/`，新渲染 `render/`，全部输出均写于此，未写生产目录；TMPDIR 指向其内 `tmp/`）
- 三 SHA（开工 = 收尾实测）：印 `0f89cf1590a0ee04bdb75baa73c512c5d6f9b7f0671199a1b8935c8cdfae39f2`（17,477,392 B）、网 `9373b750bc266644cf634f2d65bfc9d9930a9df658486409544775d8e62931e3`（1,759,960 B）、文 `9aa919b7c64738b412484c7d491fedb1d314024779e835584ef13b6c48cf978d`（50,418 B）

## 门禁逐项实测

| # | 门 | 命令 / 方法 | 结果 | 日志 |
|---|---|---|---|---|
| 0 | 探针 + 零写入 | `git -C weekly-git hash-object -w /dev/null` + scratch 写文件；开工/收尾快照 | 探针成功；版目录 47 文件快照 diff 空；SVG SHA diff 空；核心 SVG 8/8 与 fix1 收尾逐项相同 | `snapshot-pre/post.txt`、`snapshot-svg-pre/post.sha`、`core-svg-fix3/mine3.txt` |
| 1 | build | scratch `build/` 内 `run.py`（OUT 为 `__file__` 相对路径，天然落在 scratch 内；生产 `render.py` 因 BASE 硬编码生产目录而全程未跑） | rc=0；FLOW OVERFLOW 0；HEAD TOO WIDE 0；**TOTAL 150**（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42） | `build.log` |
| 2 | render | `render_scratch.py build/svg render/ La-Lucerna-VOL4-fr-ru`（print PDF，CairoSVG+pypdf） | rc=0；8 页卡片 + 印 PDF 17,477,392 B；**SHA 与交付印 PDF 逐字节相同** `0f89cf15…` | `render.log`、`render/cards/` |
| 3 | webpdf | `tools/webpdf.py build/svg render/…-web.pdf` | rc=0；1,759,954 B（交付 1,759,960 B，差 6 B，属已知不可复现字节）；文字层 51,246 B 与交付网 PDF 相同 | `webpdf.log` |
| 4 | D1 PIL 真墨 | `ink_check.py`（重建 p3 SVG；Noto Sans CJK SC 19.5pt，`getbbox(anchor="ls")`） | **2 行**，末基线 **1938.9**（= 核心），墨底 **1943.9**，余量 **+25.7px**（要求 ≥5px）；核心同注末基线 1938.9 / 墨底 1940.9 / 余量 +28.7px | `ink-rebuilt.log`、`ink-core.log` |
| 5 | D1 PDF 像素 | `pdf_pixel_check.py`（交付印 PDF P3，fitz 600dpi 裁切） | 注 x 范围内盒底下 **0 暗像素**；盒内最深暗墨 1457.48pt（=1943.3 svg px，与 PIL 一致） | `pdf-pixel.log`、`reproof-clip.png` |
| 6 | 奶油盒全版扫描 | `boxscan.py`（8 页全部 #f0eee5 盒，盒内文本逐元真墨底 vs 盒底） | 379 盒内文本、**0 越边**；孤儿启发式 432，与 fix1 修前/修后集逐项相同（diff 空）→ **0 新增孤儿** | `boxscan.log`、`orphans-mine.txt` |
| 7 | 盒标题横向真墨 | `boxscan_h.py`（新写；盒内文本 PIL 真墨左右 vs 盒左右边；非 advance 估算） | 379 文本、**0 横向越边**；最差左余量 +16.0px（p5 `REGARDER UN FILM`），最差右余量 +16.5px（p4 `LES PHRASES DU COMMENTATEUR`） | `boxscan-h.log` |
| 8 | occlusion 审计 | `tools/occlusion_audit.py --selftest` + `--core core-fr/svg --json`（重建 svg） | 自检六类全触发；**0 flags**；core 0 flags；NEW vs core 0 | `occlusion-selftest.log`、`occlusion.log`、`occlusion.json` |
| 9 | p8 extract | `tools/p8.py extract --p8 build/svg/p8-exercices.svg --total 150` | rc=0；noted **121/150**（parse: joined）；keys 150 条 | `p8-extract.log`、`p8-extract.json` |
| 10 | p8 compare | `tools/p8.py compare --core-p8 core-fr/svg/p8-exercices.svg --edition-p8 build/svg/p8-exercices.svg --total 150` | rc=0；**CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=**[150]** | `p8-compare.log`、`p8-compare.json` |
| 11 | keycheck-150 | `keycheck.py`（同 run.py 路径重跑取 REG，对 p8extract 键逐题比对；重跑后 SVG SHA 不变） | **149/150 精确**；唯一不精确 Q150（抽取截断；P8 实印全键已重组核实与 REG 逐字一致，见 PROOF-NOTE §4） | `keycheck.log`、`keycheck-150.json` |
| 12 | freeze baseline | `tools/freeze.py baseline --build <版目录> --core-svg <版目录>/svg --out <scratch>/freeze` | **8/8 逐字节相同**（p3 `1f140c11…` 等 8 项全 OK）；core 完整性：盘上核心 SVG 两次重哈希未变。注：fix 时 7/8 是因当时生产仍为修前 p3；现生产已是 fix1，8/8 为正确复校值 | `freeze-baseline.log`、`freeze/` |
| 13 | freeze diff | `tools/freeze.py diff --core-svg core-fr/svg --edition-svg <重建 svg>` | p3 **+34/−34**；新增 CJK 总计仍 **15，全 U+3000**（p3 1 个、p8 14 个）；其余 7 页逐项相同 | `freeze-diff.log`、`freeze-diff.json` |
| 14 | 印/网文字层 | `pdftotext`（plain + `-layout`，全本 + 逐页 1–8）交付印版 vs 交付网版；重建网版同验 | plain 各 **51,246 B，逐字节一致**；`-layout` 各 **107,192 B，逐字节一致**；逐页 1–8 plain+layout 全部一致；重建网 plain 与交付网一致 | `txt/`（18 个提取文件） |
| 15 | P8 最小字号 | PyMuPDF 逐 span（交付印 + 交付网 PDF，8 页） | 两版同值：P8 **11.625pt** ≥ 9.75pt 底线（SOP §1.1）；各页最小 11.625–12.75pt | `p8-minsize.log` |
| 16 | §1.1 风格 | `style11b.py`（XML 解析；rect/text 填色、纸色、刊号、可见 CJK、字体） | 纸 #fbfaf6 8/8 页；rect/text 填色除插画 path 外全在调色板；禁用色 0；**VOL.4 ×11 + 间隔体 `VOL. 4` ×1**（核心同式）；**VOL.5 ×9**；可见真实 CJK 字形 0（仅 U+3000；`<title>Lucerna 三色蛾</title>` 不渲染）；报头 `Le Lucerna` | `style11b.log`、`paper-vol.log`、`vol-core.log` |
| 17 | 变更控制 | SVG diff（生产 vs 重建）+ text.md 核对 + 生产零写入核对 | p1–p8 **逐字节相同 8/8**；text.md:439 与 `expl.py:121` 同串；版目录 47 文件与核心 SVG 开工/收工 SHA **逐项相同** | `snapshot-*.txt`、`snapshot-svg-*.sha` |

## 存活项逐项复测（`survivors.py`，重建 SVG；外加 P8 全文三重核实）

| 项 | 实测 | 结论 |
|---|---|---|
| P7 披露框 | 两行基线 2206.0 / **2233.3**，末行墨底 **2238.3**；目视 `crop-p7-disclosure.png`：2 行全在盒内，下有留白 | 无回退 |
| Q148 键 | `devant le`（keycheck n=148 match；P8 键行 y=1956.1 `148. devant le (У кинотеатра)`；text.md 键行同串；`crop-p8-keys.png` 目视） | 无回退 |
| Q148 题干无独立 `du` | 源：`content8.py` dlg_defs + `expl.py:335` `n_g4`=`У кинотеатра`；P8 battery 对话 G 六行全文逐行读过，无独立 `du`；text.md §G 同文 | 无回退 |
| Q130 | 坐标元素存在：Newsreader 20.0 `___`（Q130 填空线，(989.0, 843.0)） | 无回退 |
| Q36/Q37 偏移 | Q36 1829.0−1799.3 = **+29.7**；Q37 1961.7−1932.0 = **+29.7** | 无回退 |
| 孤儿扫描 | 0 新增（见门 6：命中集 diff 为空） | 无回退 |
| p8 keydiff | CLEAN，keydiff **[150]** | 无回退 |
| 印/网文字层 | 各 107,192 B 逐字节一致 | 无回退 |
| P8 最小字号 | **11.625pt** | 无回退 |

## 150 题三方手验（`threeway.py` + 语义手验）

- REG vs text.md 键 **150/150**；REG vs P8 抽取键 **149/150**（仅 Q150 截断，已重组核实一致）；题干编号 text.md 149/150（Q150 写作题题干无编号，核心同构，见 PROOF-NOTE §4）。
- 语义手验（配对题五组选项字母逐一对定义原文；单题抽查 Q1/Q10/Q36/Q37/Q43/Q61/Q78/Q79/Q80/Q96/Q108/Q125/Q130/Q145–Q149/Q150；图表数与 P6 图表原文核对；日期 `date -d` 核验 16 周一 / 18 周三 / 19 周四 / 20 周五 / 22 周日）：**全部搭配正确，零错配**。详见 PROOF-NOTE §4 与 `matching-opts.log`、`q73-p5.log`、`threeway2.log`。

## 仅记录（D5）

- 拉丁解释层在 Noto Sans CJK SC：450 个该字体元素含拉丁字母；其内拉丁字母 4,456 个、西里尔字母 5,216 个；构建器无 plain Noto Sans（`svglib.py:22–23` 仅载 Noto Sans CJK）。是否可接受待用户裁定；不作门、不修。见 `d5.log`、PROOF-NOTE §5。

## 目视

- `crop-p3-dates.png`（交付印 PDF P3，300dpi）：注 2 行全在奶油盒内，末行下有完整一段盒底留白；`POUR OU CONTRE ?` 未动。
- `crop-p7-disclosure.png`（交付印 PDF P7，300dpi）：披露 2 行全在盒内，下有留白。
- `crop-p8-keys.png`（交付印 PDF P8，300dpi）：`148. devant le (У кинотеатра)` 与 `150. Открытый вопрос — баллы в рамке; образец в рамке на с. 8 (По баллам)` 两行完整印出。
- 其余 7 页 SVG 与生产逐字节相同（字节同一性即渲染同一性）；重建印 PDF 与交付逐字节同 SHA。

## 结论

D1 已修（唯一改动：`expl.py:121` 注文缩短 1 行），PIL 真墨与 600dpi 交付 PDF 双方法均由越边转为 +25.7px 余量；17 门全绿，存活项逐项无回退，150 题三方手验零错配；生产零写入。**结论 (a) 零缺陷，可定稿。**
