# W47 fr-ru fix1 · GATE-LOG（修后自跑，16 门）

- 解释器（构建同一解释器）：`tools/venv/bin/python`（Pillow 13.0.0，FreeType 2.14.3，PyMuPDF 2.1）
- 版目录：`production/2026-w47/2026-w47-fr-ru/`（只读核对）；核心：`production/2026-w47/core-fr/`
- 本日志目录：`hidden_files/w47/scratch-fix-fr-ru1/`（构建副本 `build/`，新件 `render/`，全部输出均写于此，未写生产目录）
- 修前三 SHA（开工实测）：印 `c2976921…`（17,477,429 B）、网 `a6d94e5f…`（1,760,007 B）、文 `a3449fa7…`（50,453 B）
- 修后三 SHA（`render/`）：印 `0f89cf1590a0ee04bdb75baa73c512c5d6f9b7f0671199a1b8935c8cdfae39f2`（17,477,392 B）、网 `9373b750bc266644cf634f2d65bfc9d9930a9df658486409544775d8e62931e3`（1,759,960 B）、文 `9aa919b7c64738b412484c7d491fedb1d314024779e835584ef13b6c48cf978d`（50,418 B）

## 16 门自跑结果

| # | 门 | 命令 / 方法 | 结果 | 日志 |
|---|---|---|---|---|
| 1 | build | `run.py`（scratch 副本；OUT 断言先行，5 模块 OUT 全在 scratch 内） | rc=0；FLOW OVERFLOW 0；HEAD TOO WIDE 0；**TOTAL 150**（A2 53/B1 75/B2 22；分版 10/15/18/18/17/18/12/42） | `build-fix1.log` |
| 2 | render | `render_scratch.py build/svg render/ La-Lucerna-VOL4-fr-ru`（print PDF，CairoSVG+pypdf） | rc=0；8 页 PNG + 印 PDF 17,477,392 B | `render-fix1.log`、`render/cards/` |
| 3 | webpdf | `tools/webpdf.py build/svg render/…-web.pdf` | rc=0；1,759,960 B <7MB；文字层 51,246 B 非空 | `webpdf-fix1.log` |
| 4 | D1 PIL 真墨（修后） | `ink_check.py`（修后 p3 SVG；Noto Sans CJK SC 19.5pt，`getbbox(anchor="ls")`） | 2 行，末基线 **1938.9**，墨底 **1943.9**，余量 **+25.7px**（要求 ≥5px）；修前墨底 1971.2 / 余量 −1.6px | `ink-after.log`（修前 `ink-baseline.log`） |
| 5 | D1 PDF 像素（修后） | `pdf_pixel_check.py`（新印 PDF P3，fitz 600dpi 裁切） | 注 x 范围内盒底下 **0 暗像素**；盒内最深暗墨 1457.48pt（=1943.3 svg px，与 PIL 一致）；修前暗墨至 1478.00pt（越边 +1.07 svg px） | `pdf-pixel-post.log`（修前 `pdf-pixel-pre.log`） |
| 6 | 奶油盒全版扫描 | `boxscan.py`（8 页全部 #f0eee5 盒，盒内文本逐元真墨底 vs 盒底） | 修前 380 盒内文本、**1 越边（仅 D1）**；修后 379 盒内文本、**0 越边**；孤儿启发式命中集修前修后逐项相同（432=432，diff 空）→ **0 新增孤儿** | `boxscan-pre.log`、`boxscan-post.log`、`boxscan.py` |
| 7 | occlusion 审计 | `tools/occlusion_audit.py --selftest` + `--core core-fr/svg --json`（新 svg） | 自检六类全触发；**0 flags**；core 0 flags；NEW vs core 0 | `occlusion-selftest-fix1.log`、`occlusion-fix1.log`、`occlusion-fix1.json` |
| 8 | p8 extract | `tools/p8.py extract --p8 build/svg/p8-exercices.svg --total 150` | rc=0；noted 121/150（parse: joined）；keys 150 条 | `p8-extract-fix1.log`、`p8-extract-fix1.json` |
| 9 | p8 compare | `tools/p8.py compare --core-p8 core-fr/svg/p8-exercices.svg --edition-p8 build/svg/p8-exercices.svg --total 150` | rc=0；**CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=**[150]**（与修前核一致） | `p8-compare-fix1.log`、`p8-compare-fix1.json` |
| 10 | keycheck-150 | `keycheck.py`（同 run.py 路径重跑取 REG，对 p8extract 键逐题比对） | **149/150 精确**；唯一不精确 Q150（写作题，抽取截断为 `Открытый вопрос`；P8 印有全键 `150. Открытый вопрос — баллы в рамке; образец в…`（y=1996.4），属工具截断非内容差）；重跑后 SVG SHA 不变 | `keycheck-fix1.log`、`keycheck-150.json` |
| 11 | freeze baseline | 修前 `--build <版目录> --core-svg <版目录>/svg`；修后 `--build <scratch>/build --core-svg <版目录>/svg` | 修前 **8/8** 逐字节相同；修后 **7/8**，仅 p3 不同（新 sha `1f140c1118b24af5`，为设计值，rc=1 预期内）；core 完整性：盘上核心 SVG 两次重哈希未变 | `freeze-baseline-pre.log`、`freeze-baseline-post.log` |
| 12 | freeze diff | `tools/freeze.py diff --core-svg core-fr/svg --edition-svg <新/旧 svg>` | 修前 p3 +35/−34、修后 p3 **+34/−34**（仅少 1 条新增串，即删去的注第 3 行）；新增 CJK 总计仍 **15，全 U+3000**（p3 1 个、p8 14 个）；其余 7 页逐项相同 | `freeze-diff-pre.log/.json`、`freeze-diff-post.log/.json` |
| 13 | 印/网文字层 | `pdftotext`（plain + `-layout`）新印版 vs 新网版 | plain 各 **51,246 B，逐字节一致**；`-layout` 各 **107,192 B，逐字节一致**（修前各 107,298 B，−106 B 为注文缩短所致） | `print.txt`、`web.txt`、`print-layout.txt`、`web-layout.txt` |
| 14 | P8 最小字号 | PyMuPDF 逐 span（新印 + 新网 PDF，8 页） | 两版同值：P8 **11.625pt** ≥ 9.75pt 底线（SOP §1.1）；各页最小 11.625–12.75pt | `p8-minsize-fix1.log` |
| 15 | §1.1 风格 | SVG 调色板/纸色/刊号/CJK 盘点（新 svg vs 盘上 svg） | 纸 #fbfaf6 8/8 页；rect/text 填色除继承项（#ffffff 徽章白字、#cac8ba 预告灰字，均与盘上相同）外全在调色板；**VOL.4 ×12 / VOL.5 ×9 修前修后相同**；可见 CJK 仅 `<title>` 三色蛾三字（非渲染，与核心相同） | `style11-fix1.log` |
| 16 | 变更控制 | SVG diff（盘上 vs 新）+ text.md diff + 生产零写入核对 | p1/p2/p4–p8 **逐字节相同**，仅 p3 注行 3→2 行；text.md 仅第 439 行一处；版目录 47 文件与核心 50 文件开工/收工 SHA **逐项相同**；git tracked 修改 123 项修前修后相同 | `svg-diff-summary.txt`、§5 快照、`snapshot-*-pre/post.txt`、`gitstatus-pre/post.txt` |

## 存活项逐项复测（`survivors.py`，新 SVG；p7/p8 未动页为字节同一性继承 + 数值重算）

| 项 | 修前核值 | 修后实测 | 结论 |
|---|---|---|---|
| P7 披露框 | 末基线 2233.3、真墨底 2238.3、间隙 0 暗像素 | 两行基线 2206.0 / **2233.3**，末行墨底 **2238.3**（p7 SVG 与盘上逐字节相同，故间隙性质继承） | 无回退 |
| Q148 键 | `devant le`、题干无 `du` | 键 `devant le`（keycheck n=148 match）；题干（对话 G，P8 y=1226.0–1353.68）全文无独立 `du`；`(148)___ cinéma` 与键相合 | 无回退 |
| Q130 | (989.0, 843.0) | 该坐标元素存在：Newsreader 20.0 `___`（Q130 填空线） | 无回退 |
| Q36/Q37 偏移 | 全 +29.7（+30 档） | 编号元 y 差：Q36 1829.0−1799.3 = **+29.7**；Q37 1961.7−1932.0 = **+29.7** | 无回退 |
| 孤儿扫描 | 0 新增 | 见门 6：命中集 diff 为空 | 无回退 |
| p8 keydiff | [150] | CLEAN，keydiff **[150]** | 无回退 |
| 印/网文字层 | 各 107,298 B 逐字节一致 | 各 107,192 B 逐字节一致 | 无回退（字节差为注文缩短） |
| P8 最小字号 | 11.625pt | **11.625pt** | 无回退 |

## 目视

- `crop-p3-dates-fix.png`（新印 PDF P3，300dpi 裁切）：注 2 行全在奶油盒内，末行下有完整一段盒底留白；`POUR OU CONTRE ?` 未动。
- `render-p3-fix.png`（新印 PDF P3 全页，100dpi）：整页版式如常。
- 其余 7 页 SVG 与盘上逐字节相同，未逐页重看（字节同一性即目视同一性）。

## 结论

D1 已修（唯一改动：`expl.py:121` 注文缩短 1 行），PIL 真墨与 600dpi 交付 PDF 双方法均由越边转为 +25.7px 余量；16 门全绿，存活项逐项无回退；生产零写入。待独立 re-proof 后由协调员落地（新件在 `render/`，KIT 贴文见 FIX-LOG §6）。
