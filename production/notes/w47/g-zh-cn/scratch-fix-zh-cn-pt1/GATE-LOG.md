# W47 zh-cn-pt 修复 fix1 · GATE-LOG

- 解释器（构建同一解释器）：`tools/venv/bin/python`（PIL 13.0.0，PyMuPDF 2.1）
- 版目录：`production/2026-w47/2026-w47-zh-cn-pt/`；核心：`production/2026-w47/core-zh-cn/`
- 本日志目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-pt1/`
  （全部中间输出均写于此；生产目录只在同步一步写盘，未 commit、未 push）
- 依据：proof1（PROOF-NOTE.md / GATE-LOG.md，同一 goals 路径下
  `scratch-proof-zh-cn-pt1/`），每项修复前自己重测确认。

## 身份

| 文件 | 开工（任务先验，实测一致） | 修复后（生产盘上实测） |
|---|---|---|
| 印刷 PDF | 41,734,759 B，`2286485f2608d2a144d37e9451f7a1945313e54e1f6ba1b540aec1ab5484859c` | **41,734,802 B，`6644cd43e033e99b27eb02f8bbaca9b470002eb40c9ebac12fed75a73cb7dccb`** |
| 网页 PDF | 2,647,093 B，`030f52fb82087f8fe13f3465b74ee61b8c02b6e7d8a4740280ff7fa66cac76fa` | 未变（同左；本次不覆盖） |
| 文本导出 | 50,846 B，`9207974bed3d5d16c4312752ad22a4219f0033e33d9264c29c07adfe3d44cb71` | **50,834 B，`ed0858346f731013dd8b8f6c5d4c85c15a3b6d7eae61099d62e36e3bd9808d94`** |

双 PDF 均为 8 页。开工三项 SHA 与任务先验值逐字一致。

## 机械门（自跑）

| 门 | 命令 | 结果 | 日志 |
|---|---|---|---|
| rebuild（scratch 副本，基线） | 拷版内 `*.py`+`assets`+`cards` 至 `rebuild/`，5 个 content 文件 OUT 改向 scratch 内绝对路径并验明，`tools/venv/bin/python run.py` | RC=0，TOTAL 150（A2 56/B1 69/B2 25；页 10/18/18/18/18/18/12/38）；**8 SVG 与生产件逐字节一致**（基线可复现） | `run-baseline.log`、`svg-sha-baseline.txt`、`svg-sha-prod.txt` |
| rebuild（fix1） | 同上，改 3 处标题后 | RC=0，TOTAL 150，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；P7 teaser 2588.78；P8 keys 2552.7；**变化的 SVG 恰好 p1/p2/p5**，其余 5 页逐字节一致 | `run-fix1.log`、`svg-sha-fix1.txt` |
| render（scratch 副本） | `render-scratch.py`（BASE 改向 scratch，`render.py` 本体未跑） | RC=0，8 卡片 + 印 PDF；卡片变化恰好 p1/p2/p5；印 PDF 41,734,802 B | `render-fix1.log` |
| 盒标题 PIL 横扫（修前，生产 SVG） | 自写 `sweep.py`：全 8 页每个奶油盒（`#f0eee5`）内每行文字 PIL 真墨右缘 vs 盒右缘 | **3 旗**：P1 越 21.5、P2 越 4.5、P5 越 3.5——与 proof1 逐值一致 | `sweep-before.json` |
| 盒标题 PIL 横扫（修后，新 SVG） | 同上 | **0 旗**；三处标题余量 +35.5 / +29.5 / +48.5；全版最紧非标题行余量 P1 +21.9、P2 +20.5、P5 +30.5 | `sweep-after.json` |
| 盒标题 PIL 横扫（修后，生产 SVG） | 同上，对同步后的生产 `svg/` | **0 旗** | `sweep-prod-after.json` |
| 像素验证（旧印 PDF，方法校验） | `pixels.py`：`pdftoppm -r 150` P1/P2/P5 → 橄榄墨点 vs 奶油盒缘 | P1 982.4/960.6（proof1：981.7）、P2 1415.7/1410.6（proof1：1415.0）、P5 963.8/960.6（proof1：963.2）——方法复现 0.7px 内 | `pixels-before.json`、`render-old/` |
| 像素验证（新印 PDF，裁决） | 同上 | P1 922.9/960.6 **+37.8**；P2 1381.1/1410.6 **+29.4**；P5 912.6/960.6 **+48.0**——三项均 ≥ +5px | `pixels-after.json`、`render-new/` |
| occlusion | `tools/occlusion_audit.py rebuild/svg --core <core>/svg --json occlusion.json` + `--selftest` | exit 0；自检 OK（6 类 planted 全触发）；**0 flags**；core 0；NEW vs core 0——但对无描边奶油盒标题盲（见下“工具盲区”），**不以此为三项修好证据** | `occlusion.log`、`occlusion.json`、`occlusion-selftest.log` |
| p8 extract | `tools/p8.py extract --p8 rebuild/svg/p8-ceyan.svg --total 150` | exit 0；**150/150** | `p8extract.log`、`p8extract.json` |
| p8 compare | `tools/p8.py compare --core-p8 <core>/svg/p8-ceyan.svg --edition-p8 rebuild/svg/p8-ceyan.svg --total 150` | exit 0；**CLEAN**，missing=[]，extra_count=0，keydiff=[] | `p8compare.log`、`p8compare.json` |
| freeze diff --strict-cjk | `tools/freeze.py diff --core-svg <core>/svg --edition-svg rebuild/svg --strict-cjk` | exit 0；新增 CJK **0** | `freeze-diff.log`、`freeze-diff.json` |
| freeze baseline（核心） | `tools/freeze.py baseline --build <core> --core-svg <core>/svg --out freeze-baseline` | exit 0；**8/8** 字节一致，核心未变 | `freeze-baseline.log`、`freeze-baseline/` |
| 候选标题测宽 | `candidates.py`（`_runs`/`_pil`，23pt sans bold） | 见 FIX-LOG 候选表；采用的三项余量 +35.5/+29.5/+48.5；“Números desta semana”+2.5、“Palavras frequentes”−4.5 均被否决 | `candidates.py` |

## 像素法初版踩坑（已修正，记下防再犯）

- 初版盒缘在标题行带内扫描：标题字墨的抗锯齿晕边呈奶油色（≈98% 奶油 +
  2% 橄榄仍落进 `#f0eee5`±6 容差），P1 盒缘误读 982.4（真值 960.6）。
  修正：盒缘取盒顶无字条带（rect_y+2..+10）。
- 初版墨搜索全宽：P2 误取 1819.5（他栏橄榄字/山谷照）。修正：限
  [标题 x, 盒右+25]、要求绿主导暗像素（g−r≥3 且 r+g+b≤665），排除中性
  INK 正文与 x≥1439.5 的山谷照。
- 修正后方法先在旧印 PDF 上校验（复现 proof1 在 0.7px 内）才用于新 PDF。
- 几何：PDF 页为 1950 单位宽 @96dpi 基底；150dpi 渲染 3047×4219px，
  换算系数 150/96=1.5625，报告值已换回 SVG 坐标。

## 文字层 / 字号（自跑）

| 检查 | 方法 | 结果 |
|---|---|---|
| text.md diff | 新 text.md（3 处同串替换，各恰 1 次）vs 生产旧件 | 仅 3 行：行 47/271/915；新件 50,834 B，`ed085834…` |
| print 文字层（新 vs 旧） | `pdftotext -layout` + `-raw` | `-layout` 新 97,305B vs 旧 97,374B；空白归一化后、3 处标题映射回去即逐字相同；词多重集之差恰为 3 处标题的词（新：Números/da/Palavras-chave；旧：Esta/semana/em/números/desta/Palavras）；`-raw` 新 43,813B vs 旧 43,825B，同样结论 |
| print（新）vs web（旧）文字层 | 同上 | 与上行相同结论（旧印与旧网文字层本来逐字相同）——新印与旧网之差恰为 3 处标题 |
| 逐页词数（PyMuPDF） | 新印 vs 旧网 | 新 [395, 381, 292, 364, 290, 361, 540, 1898] vs 旧 [396, 381, 292, 364, 292, 361, 540, 1898]（P1 −1 词、P5 −2 词——恰为标题缩短；P2 词数不变） |
| P8 最小字号 | PyMuPDF 逐 span（新印 + 旧网） | 均为 **9.98pt** ≥ 9.75pt；P8 字号集合 9.98–34.5pt |
| 徽章 | 新 SVG `rx="2.7"` 矩形计数 | 10/15/15/15/15/15/12/38 = **135** = 核心 |
| U+2019 | 新 8 页 SVG + 新 text.md + ABSTRACT.txt | **总数 0** |
| §1.1 调色 | 新 SVG 逐页统计 | 纸色 `#fbfaf6` ×8；金色 0；VOL.5 仅 P7 合法下期预告 1 处；VOL.4 每页在位 |
| D4/D5 | 新 text.md + 新 SVG 扫查 | “第一次”恰 2 处，均带全球总决赛限定；Q56 键注 “pela primeira vez num BO5 dos Worlds” 在位（text.md + SVG 各 1）；“今年一场没输”/“今年一局没输” 0 命中；“在S16一场没输” 2 处 |
| #3 修复点存活 | `text_w`/`wrap` + 渲染核对 | P4 C-head 339.0px；P7 三头 371.9/345.3/318.5px；P4 S16 gloss 内宽 386.5 恰 6 行、渲染 6 行逐行一致；P2 词卡 4 句各 1 行；P7 teaser 2588.78；P8 keys 2552.7 |

## 目视（自新印 PDF 重新渲染，不采信 builder 的图）

- `pdftoppm -png -r 110` 新印版 P1/P2/P5 → `render-new/p110-1-1.png` 等：
  逐版目视——三处标题收进盒内，无其他位移、无溢出、无重叠。
- 放大裁切（自 150dpi 渲染）：`render-new/crop-p1-numbox.png`（“Números da
  semana”止于盒内、右侧留空）、`render-new/crop-p2-caltitle.png`
  （“Datas da semana”止于盒内、山谷照清）、`render-new/crop-p5-weekwords.png`
  （“Palavras-chave”止于盒内）。

## 工具盲区（重申，不计入本版缺陷数）

`tools/occlusion_audit.py` 的 BOXTITLE 类只考察带描边的 rect 或
`fill == "#2c2822"` 的 rect（L471–478）。奶油盒 `fill="#f0eee5"` 且无描边，
根本不在候选集里——本次修前横扫 3 旗时 occlusion 仍为 0 旗，修后亦为
0 旗。occlusion 的 0 旗对这三项是空信号，修复证据只认 PIL 真墨横扫 +
交付 PDF 150dpi 像素扫描。本轮未动工具（须工具线修 BOXTITLE 候选集）。

## 生产同步核对

- 开工快照 `snapshot-start.txt`（39 文件）与收工 `snapshot-end.txt`
  diff：**恰好 11 个文件变化**——`content12.py`、`content56.py`、
  `svg/p1-touiban.svg`、`svg/p2-shenghuo.svg`、`svg/p5-qingnian.svg`、
  `cards/p1-touiban.png`、`cards/p2-shenghuo.png`、`cards/p5-qingnian.png`、
  `Lucerna-VOL4-PT.pdf`、`2026-w47-zh-cn-pt.text.md`、`WEEKLY-KIT.md`；
  其余 28 个文件逐字节相同；网 PDF 未变。
- 同步后生产复核：新三 SHA/字节数与上表一致；生产 `svg/` PIL 横扫
  **0 旗**；生产源码 3 处新标题在位、旧标题 0 命中、OUT 行仍为生产路径；
  生产 `__pycache__/` 只有开工前已有的 2 个 .pyc（2026-11-11 14:16），
  本次凡 import 生产源码一律 `PYTHONDONTWRITEBYTECODE=1`。
- `run.py` 输出重定向只用绝对路径、目标验明在自家 scratch 内；
  未跑生产 `render.py`/`webpdf.py`/`insert.py`/`lint --write`；
  未 git add/commit/push。

## 结论

proof1 的 3 项盒标题越边缺陷（D-01～D-03）已按左锚定缩短葡语标题修净：
PIL 真墨横扫 0 旗，交付印 PDF 150dpi 像素三项余量 +37.8 / +29.4 /
+48.0（均 ≥ +5px），其余门禁逐项实测通过（见上表），#3 修复点与 D4/D5
全部存活。网 PDF 仍带 3 处旧标题（按要求未覆盖），入仓前须全家统一重建。
