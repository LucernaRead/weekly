# GATE-LOG — 2026-W47 pt-en 第一轮返修（fix round 1）

- 返修 builder：叶子（第一轮返修）
- 时间：2026-11-11（EST）
- 对象：`production/2026-w47/2026-w47-pt-en/`（main clone 内）
- 解释器：`tools/venv/bin/python`（构建/门禁统一口径）
- 全部日志与 JSON 在本目录 `gates/`（`run-fix1.log`、`render-fix1.log`、`webpdf-fix1.log`、`gates-fix1.log`、`occlusion-fix1.log` + `en-occlusion-fix1.json`、`p8-extract-fix1.log`、`p8-compare-fix1.log` + `p8-compare-fix1.json`、`freeze-fix1.log`、`freeze-diff-fix1.log` + `en-freeze-diff-fix1.json`、`check-final-fix1.log` + `en-textdiff.json` / `en-p8size.json`、`old-p8-extract.log`）、`old-pdf-sha.txt`、`old-svg-sha.txt`、`new-svg-sha.txt`、`old-textmd.md`、`new-p8-extract.json`、`en-textmd-diff.json`；渲染图在 `render/`。

## 0. 身份（新旧双 PDF）

| 文件 | 旧（第一轮复校登记） | 新（本轮返修） |
|---|---|---|
| 印刷 PDF `A-Lucerna-VOL4.pdf` | 12,932,446 B；sha256 `8d2b58152bc0969151f8a7ab8becb0976221efdc62cac0d3cce877de8f160e4a` | **12,932,451 B**；sha256 `0146a4202b015f44659b4bba067a7411f90891cb640085dee5fec2010bd06af1` |
| 网页 PDF `A-Lucerna-VOL4-web.pdf` | 1,102,770 B；sha256 `40bc2f444dbc31fbf0ef49643f1f81da13c134cab5ba0ec0a3ea804574a5e49c` | **1,102,777 B**；sha256 `a974ef7ccf7c879f58e3626d874d9ce18e3da5f2a35faef43717e81706254c80` |
| 页数 / 版面 | 8 页；1462.5×2025 pt | 8 页；1462.5×2025 pt（不变） |
| 网页文字层 | 46,049 字节 | 46,073 字节 |

## 1. 构建

| 步骤 | 结果 |
|---|---|
| `transform.py` 复现（scratch 核心副本） | rc=0；`CJK 0 OK`；6 文件 diff 仅 6 处等效改动 + 1 处既有 furniture 差异（`content12.py:19` EXPLICATIONS/EXPLANATIONS，见 FIX-LOG §3） |
| `textmd.py` 再生 `.text.md` | rc=0；535 行；CJK 0；题号 150/150；与旧 `.text.md` 仅 215 行不同 |
| `run.py` | rc=0；TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词）；FLOW OVERFLOW / HEAD TOO WIDE 0 |
| `render.py` | 首跑 rc=120（Disk quota exceeded，印刷 PDF 截断作废）；清 39MB 已验证 repro 副本后重跑 **rc=0**，零溢出 |
| `webpdf.py` | rc=0；1,102,777 B；46,073 text bytes |

## 2. 机械门

| 门 | 结果 |
|---|---|
| `gates.py` | **16/16 PASS，FAILURES: none**（rc=0） |
| `tools/occlusion_audit.py` | 自检阳性对照 6 类全触发、干净对照静默；**0 flags**（rc=0） |
| `tools/p8.py extract` | **150/150**（rc=0） |
| `tools/p8.py compare` vs 核心 | **CLEAN**；missing=[]；extra_count=0；**keydiff=[137, 138]**（与上一轮一致，仅翻译题答案） |
| `tools/freeze.py baseline` | **8/8 SVGs byte-identical**（repointed files: none；核心 SVG 完整性通过，rc=0） |
| `tools/freeze.py diff` | 新增 CJK 共 9 个，全部 U+3000（P1 2、其余每页 1）；新增汉字 0 |
| `check_final.py` | 页数 8/8；词数 print=web=8,507；**词多重集 diff 0**；P8 答案区最小字号 **9.75pt**（187 spans，1,543 词） |
| U+2019 全扫（8 SVG） | **0** |
| 冒号复扫（8 SVG，`:` 后接字母 / 非空格非数字） | **0 处**（时刻写法已排除） |
| §1.1 抽查 | 纸色 #fbfaf6 ×8；金色 #d4af37 0；"double" 0；可见文本 TODO/FIXME/XXX 0；徽章三色齐全；VOL.4 ×9（+顶条 `VOL. 4` 1 次）、VOL.5 ×3（P7 披露/预告内）；`.text.md` 双空格 0 行 |

## 3. 150 键逐题复核（新旧对比）

- 新旧 `p8.py extract` JSON 对比：noted_set 完全一致（150/150），150 个答案键 **0 处差异**。
- 唯一变化：P8 注文 56/57/58/102（冒号后补空格）+ P1 标语 + P4 词表注，共 6 处，均与 FIX-LOG §2 清单逐一对应。
- 变化的 SVG：仅 p1-capa / p4-esporte / p8-avaliacao 三页（SHA 对比）；其余 5 页逐字节不变。

## 4. 目视

- 印刷 PDF 全新渲染 8 版（`render/print-p--1.png`～`print-p--8.png`）+ 网页 P1/P8（`render/web-p1--1.png`、`web-p8--8.png`），110 dpi，逐版看过。
- 重点确认：P1 刊头标语 `The Portuguese that Brazil is reading` 单行居中完整、无溢出；P4 Note 框 `o título title`；P8 答案区 56/57/58/102 空格已入版、无溢出、页脚完整。
- 其余版面与上一轮一致，无新增问题（P3 中部空白、P2/P4 栏尾孤行为核心版式；P1 数字盒贴边为既有观察项，occlusion 0）。

## 5. 结论（报事实，不作定稿决定）

- 6 处修复全部落版；全部机械门绿；150 键 0 差异；8 版目视通过。
- 按 SOP §8.4，定稿须经第二轮独立全量复校零问题；本轮为返修自查，不作定稿结论。第二轮复校由协调员另派。
