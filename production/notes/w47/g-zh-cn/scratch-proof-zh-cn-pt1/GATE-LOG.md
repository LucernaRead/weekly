# W47 zh-cn-pt 第一轮独立校对 · GATE-LOG（proof1）

- 解释器（构建同一解释器）：`tools/venv/bin/python`（PIL 13.0.0，PyMuPDF 2.1）
- 版目录：`production/2026-w47/2026-w47-zh-cn-pt/`；核心：`production/2026-w47/core-zh-cn/`
- 本日志目录：`hidden_files/w47/scratch-proof-zh-cn-pt1/`（全部输出均写于此，未写版目录）
- #3 棒报告与 EDITION-RECORD 实际位置：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-zh-cn/`
  （weekly-git 内 `hidden_files/w47/briefs/` 不存在；见 PROOF-NOTE O-3）

## 身份

| 检查 | 命令 / 方法 | 结果 |
|---|---|---|
| 印刷 PDF | `sha256sum Lucerna-VOL4-PT.pdf` | `2286485f2608d2a144d37e9451f7a1945313e54e1f6ba1b540aec1ab5484859c`，41,734,759 字节，8 页 |
| 网页 PDF | `sha256sum Lucerna-VOL4-PT-web.pdf` | `030f52fb82087f8fe13f3465b74ee61b8c02b6e7d8a4740280ff7fa66cac76fa`，2,647,093 字节，8 页 |
| 文本导出 | `sha256sum 2026-w47-zh-cn-pt.text.md` | `9207974bed3d5d16c4312752ad22a4219f0033e33d9264c29c07adfe3d44cb71`，50,846 字节 |

三项 SHA 与任务先验值逐字一致。

## 机械门（自跑）

| 门 | 命令 | 结果 | 日志 |
|---|---|---|---|
| rebuild（scratch 副本） | 拷版内 `*.py`+`assets`+`cards` 至 `rebuild/`，5 个 content 文件 OUT 改向 scratch 内绝对路径并验明，`tools/venv/bin/python run.py` | RC=0，TOTAL 150（A2 56/B1 69/B2 25；页 10/18/18/18/18/18/12/38），`FLOW OVERFLOW`/`HEAD TOO WIDE` 出现 0 次；**8 SVG 与生产件逐字节一致**；P7 teaser 2588.78；P8 keys 2552.7 | `run-rebuild.log`、`svg-sha-rebuild.txt`、`svg-sha-prod.txt` |
| occlusion | `tools/venv/bin/python tools/occlusion_audit.py svg/ --core <core>/svg --json occlusion.json` | exit 0；selftest OK（6 类 planted 全触发）；**0 flags**；core 0 flags；NEW vs core 0——但对无描边奶油盒标题盲（见 PROOF-NOTE 工具盲区） | `occlusion.log`、`occlusion.json` |
| p8 extract | `tools/venv/bin/python tools/p8.py extract --p8 svg/p8-ceyan.svg --total 150 --json p8extract.json` | exit 0；**150/150** | `p8extract.log`、`p8extract.json` |
| p8 compare | `tools/venv/bin/python tools/p8.py compare --core-p8 <core>/svg/p8-ceyan.svg --edition-p8 svg/p8-ceyan.svg --total 150 --json p8compare.json` | exit 0；**CLEAN**，missing=[]，extra_count=0，keydiff=[] | `p8compare.log`、`p8compare.json` |
| freeze diff --strict-cjk | `tools/venv/bin/python tools/freeze.py diff --core-svg <core>/svg --edition-svg svg --strict-cjk --json freeze-diff.json` | exit 0；新增 CJK **0**（逐页 0/0/0/0/0/0/0/0；CJK 计数逐页小幅下降，均为英文讲解层被葡文替换） | `freeze-diff.log`、`freeze-diff.json` |
| freeze baseline（核心） | `tools/venv/bin/python tools/freeze.py baseline --build <core> --core-svg <core>/svg --out freeze-baseline` | exit 0；**8/8** 字节一致；核心 SVG 跑前跑后未变 | `freeze-baseline.log`、`freeze-baseline/` |
| keycheck-150（手验） | AST 提取题干（`extract-stems.py`→`stems.json`）+ REG（`dump-reg.py`→`reg.json`）+ P8 印刷键三源对齐 | 150 题 AST-REG 对齐 0 不符；P8-vs-REG **149/150**，唯一差 Q150（印刷 “✓”，开放题设计）；**逐题手验键与题干配对 150/150 相符** | `keytable.txt`、`stems.json`、`reg.json` |
| 盒标题全版扫查 | 自写 `sweep-boxes.py`：全 8 页每个奶油盒（`#f0eee5`）内每行文字 PIL 真墨右缘 vs 盒右缘 | **3 旗**：P1 数字框标题越 21.5px、P2 日历标题越 4.5px、P5 高频词标题越 3.5px；核心同扫 **0 旗** | `sweep-boxes.py`、`sweep-boxes.json`、`measure-pt.py`、`measure.json`、`measure.log` |
| 像素验证（交付 PDF） | `pdftoppm -r 150` 印版 P1/P2/P5 → 橄榄墨点与奶油盒缘逐行扫描 | P1 墨右缘 981.7 vs 盒缘 960.6（越 20.7px）；P2 1415.0 vs 1410.5（越 3.5px，距山谷照 24.5px）；P5 963.2 vs 960.6（越 2.2px）——与 PIL 真墨一致 | `render/print-1/2/5.png`、`render/crop-p1-numbox.png`、`render/crop-p2-caltitle.png`、`render/crop-p5-weekwords.png` |

## 文字层 / 字号（自跑）

| 检查 | 方法 | 结果 |
|---|---|---|
| print/web 文字层 | `pdftotext -layout` 与 `-raw` 两版 | `-layout` 均为 97,374B、`-raw` 均为 43,825B；空白归一化后**逐字相同**；词多重集相同（4,876 词） |
| print/web 逐页词数 | PyMuPDF 位置排序词数 | 两版逐页相同 [396, 381, 292, 364, 292, 361, 540, 1898]（KIT 绝对值 386/366/… 为另一计数口径，相等结论一致） |
| P8 最小字号 | PyMuPDF 逐 span 实测（印刷 + 网页 PDF） | 均为 **9.98pt** ≥ 9.75pt；P8 字号集合 9.98–34.5pt |
| 徽章 | SVG `rx="2.7"` 矩形计数 + 级别核对 | 10/15/15/15/15/15/12/38 = **135**，与核心逐页相同；P8 A2 11 / B1 24 / B2 3 = 核心 |
| U+2019 | 8 页 SVG `<text>` + text.md + ABSTRACT.txt | **总数 0**；U+0027 同口径 0 |
| §1.1 调色 | 逐 SVG 统计 | 纸色 `#fbfaf6` ×8；金色 0（raw 文本命中均为图片 base64 内串）；VOL.5 仅 P7 合法下期预告 1 处（与核心一致）；VOL.4 每页在位 |
| CJK 残留 / 泄漏 | freeze diff + 交集扫描 | 新增 CJK 0；核心与本版 `<text>` 交集 1087 串中未译英文散文串 0 条；ABSTRACT 331B = `tables.py` ABSTRACT['pt'] + 换行（AST 核对） |
| 金句 | text.md 计数 | 8 句各 **2 次**（正文 + P7） |
| 范文 | 源码 `MODELO` 去空格实数 | **138 字**（120–180 内），与 P8 栏注一致 |
| P4 gloss | `wrap("Notas｜"+…,"sans",20.5,内宽386.5)` + 渲染行核对 | **恰 6 行**；盒底 792.2，下一行 “GEN，” 墨顶 ≈801，清 ≈9px |

## 目视（自交付印刷 PDF 重新渲染，不采信 builder 的图）

- `pdftoppm -png -r 110` 印刷版 8 页 → `render/print-{1..8}.png`：逐版目视，见 PROOF-NOTE §1。
- `pdftoppm -png -r 110` 网页版 P1/P8 → `render/web-1.png`、`render/web-8.png`：与印刷版一致，无豆腐块。
- 放大裁切（自 150dpi 渲染）：`crop-p1-numbox.png`（标题 “números” 挂在盒外）、
  `crop-p2-caltitle.png`（末字 “a” 贴压盒边）、`crop-p5-weekwords.png`（末字 “a” 贴在盒边、微越）。

## 生产零写入核对

- 开工快照 `snapshot-start.txt`（41 文件 SHA）与收工 `snapshot-end.txt` diff：**零差异**。
- 工作区只用 `hidden_files/w47/scratch-proof-zh-cn-pt1/`（此前无此目录，独占）；
  run.py 重建只在 scratch 副本内（OUT 改向后逐文件验明目标在 scratch 内）；
  未跑 `render.py`/`webpdf.py`/`insert.py`/`lint --write`；未 git add/commit/push。

## 结论

机械门除盒标题类外全部通过；**内容/几何复核发现 3 条缺陷 D-01～D-03
（P1 数字框标题越奶油盒右缘 21.5px、P2 日历标题越 4.5px、P5 高频词标题越 3.5px，见 PROOF-NOTE）**，
按 SOP §8.4 不可定稿。另：occlusion 审计的 BOXTITLE 类对无描边奶油盒盲——工具盲区，须工具线修后复验。
满分通过项与缺陷细节见 PROOF-NOTE.md。
