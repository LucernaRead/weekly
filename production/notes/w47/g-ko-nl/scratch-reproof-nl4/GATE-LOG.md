# GATE-LOG — core-nl fix4 独立 re-proof（2026-11-11）

复校员独立重跑记录。每项均附：命令/方法、源日志文件（`scratch-reproof-nl4/` 内）、实测值、结论。
修复者日志（`scratch-fix-nl4/`）只作比对参考。所有时间均为本轮实测。

## 0. 前置探针与 SHA

| 项 | 命令/方法 | 源 | 实测值 | 结论 |
|---|---|---|---|---|
| /dev/null | `ls -l /dev/null` | — | 存在（crw-rw-rw-） | PASS |
| git hash-object -w | 仓库内 `echo test \| git hash-object -w --stdin` | — | rc=0（此前在家目录误跑 rc=128 系 cwd 不在仓库内，重探通过） | PASS |
| scratch 可写 | 新建 `scratch-reproof-nl4/probe.txt` | `probe.txt` | 写入成功 | PASS |
| 印 SHA | `sha256sum De-Lucerna-VOL4.pdf` | — | `2c7f2c6f…ecd3c` / 25,955,580 B | 与任务书一致 ✓ |
| 网 SHA | `sha256sum De-Lucerna-VOL4-web.pdf` | — | `434626f5…53df5` / 2,103,990 B | 与任务书一致 ✓ |
| 文 SHA | `sha256sum 2026-w47-nl-zh-cn.text.md` | — | `0b97a48d…7050c` / 44,093 B | 与任务书一致 ✓ |
| SVG 范围 | `sha256sum svg/*.svg` vs fix4 after-b / fix3 before | `svg-hashes-prebuild.txt` | = fix4 after-b 全 8；vs fix3 仅 p6/p7/p8 变 | PASS |

## 1. 构建与重现

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| run.py | `tools/venv/bin/python run.py`（原地） | `build-reproof.log` | rc=0；TOTAL 150；页 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；0 FLOW OVERFLOW / HEAD TOO WIDE；P6 chart ends 665、P6 col3 ends 1000.0、P7 col3 ends 1898.0 | PASS |
| SVG 重建一致 | 重跑前后哈希比对 | `svg-hashes-prebuild.txt` / `svg-hashes-postbuild.txt` / `h-pre.txt` / `h-post.txt` | 8/8 字节一致 | PASS |
| render.py | `tools/venv/bin/python render.py`（原地；印 PDF 字节可复现） | `render-reproof.log` | rc=0；8 cards；印 PDF 25,955,580 B，SHA `2c7f2c6f…ecd3c` 与交付一致 | PASS |
| text.md 未被构建改动 | 重跑后 `sha256sum` | — | `0b97a48d…7050c` 不变 | PASS |
| freeze baseline | `tools/freeze.py baseline --build <真核心目录> --core-svg <真核心svg目录> --out scratch-reproof-nl4/freeze` | `freeze.log` | rc=0；**8/8 MATCH**；core integrity：发货 SVG 未变 | PASS |
| text.md 重导出 | 复制 fix4 `export47.py`+stub 至 scratch，输出重定向至 `export/reexported.text.md` 后运行 | `export-reproof.log` | rc=0；44,093 B；SHA 与交付件一致；432 行；142+2+8=150；8 金句；6 gloss | PASS |

## 2. 孤儿标点 sweep（独立自写脚本，三种方法）

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| (a) 独占一行 。 | `orphan_sweep_reproof.py`：xml 解析，按基线分组、x 间隙 >60px 分段；PIL 实测推进量 | `orphan-sweep-reproof.log` / `orphan-sweep-reproof.json` | 1421 重建行；(a)=**0**（逐页 0） | PASS |
| (a) 同上 | 同脚本，svglib `text_w` 推进量第二遍 | 同上 | (a)=**0** | PASS |
| (b) 行首标点 | 同上两遍（行首 。/，/、/：/；/！/？/”/’/」/』/）/》/»） | 同上 | (b)=**0** / **0**（逐页 0） | PASS |
| 蛮力复核 | 所有以闭标点开头的 `<text>` 元， adjudicate 是否基线最左元 | 同上 | 12 片段（P1 `：`1、P8 `：`4、`）`7），最左元 **0** | PASS |
| D8 目标行 | 内容检索 p6 SVG | 同上 | 行 1 `…非真实调查。`（635.02）、行 2 `问题：…`（659.44）；2 行 | PASS |
| D10 目标行 | 内容检索 p7 SVG | 同上 | 行 1 `…最佳作文，`（1754.27）、行 2 `刊登示例信，…`（1782.67）；2 行 | PASS |
| D8 宽度带 | `width_scan_reproof.py`（生产 `wrap()`） | `width-scan-reproof.log` | 旧宽 378.5 重现孤儿；目标行带 388.5–406.5；397.5 为中值；窄化 ≤360 变 3 行 | PASS |
| D10 宽度带 | 同上 | 同上 | 旧宽 378.5 重现孤儿；目标行带 380.5–400.0；390.5 取中；窄带 338.5–~341 亦可 2 行清孤儿且不拆“作文”（见 PROOF-NOTE §3 备注） | PASS（修复正确） |

## 3. P8 与键

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| p8 extract | `tools/p8.py extract --p8 svg/p8-toets.svg --total 150 --json p8-extract.json` | `p8.log` / `p8-extract.json` | noted set **150/150**（1–150 全） | PASS |
| 三源对照 | 自写 `p8compare_reproof.py`（REG 原地重跑导出；text.md 解析；P8 键取自本轮 p8-extract.json） | `p8compare-reproof.log` / `p8-compare-reproof.json` | **MATCH 149/149，DIFF 0，MISSING 0**；#150 开放写作例外；Q140 四源一致；25–28=d/c/a/b，141–144=b/c/d/a | PASS |
| 键手验 | 通读 `keytable-150.txt` 150 条 + 外部事实复核 | `keytable-150.txt`（源自 `reg-dump.json` + text.md + P8） | 150/150 填空合理；Q140 外无同类键错；REG 键与 proof3 手验集仅 Q140 不同 | PASS |
| Q150 范文 | text.md:432 直接计数 + P8 十片段检索 | （`gates-reproof.log` 误取 110 词系正则 fallback 取错段；以本行计数为准） | 81 词（去独立 `–` 为 80），在 80–100 内；P8 10/10 片段齐全 | PASS |
| P8 最小字号 | PyMuPDF 逐 span（印 PDF 第 8 页） | `gates-reproof.log` / `gates-reproof.json` | min **10.12pt**（561 段）；直方图与修复者一致 | PASS（≥10pt） |

## 4. 几何门禁

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| occlusion（真实审计） | `tools/occlusion_audit.py <svg目录>`（非 --selftest；工具先行自测） | `occlusion.log` | selftest OK；**0 flags**（含 BOXTITLE 0） | PASS（注：BOXTITLE 仅计有描边盒，D11 盒为纯 fill 矩形，不在其内） |
| creambox 几何扫描 | proof3 `check_creambox.py` 复制至本 scratch 原样重跑 | `creambox-reproof.log` | 3 flags：P2/P5/P6 各 1 处 CREAM-BOTTOM（≤1.6px）；其余 0 | 3 处均为已知假阳性（见下） |
| creambox 真墨探针 | 自写 `inkprobe2_reproof.py`：框底 7px 带逐像素（纸定义 r≥228/g≥226/b≥210）+ 最低真墨行（墨定义 r<200 或 g<200 或 b<190） | `inkprobe2-reproof.log` | 三处带内非纸像素 **0**；真墨余量 P2 +3.4 / P5 +3.5 / P6 +3.6px | **3 处真溢出 0** |
| **溢出全扫（新增）** | 自写 `spill_sweep_reproof.py`：每奶油盒外 0–60px 邻近文本扫描（补 creambox 盲区） | `spill-sweep-reproof.log` | 唯一近距命中：**P4 `18:45 uur.` 盒底 +6.89px**（其余 BELOW 命中 ≥+24px，均为独立区块，已 adjudicate） | **FAIL — D11** |
| D11 真墨量测 | 卡片 PNG 像素探针（盒 x 跨度，y 1195–1240） | （同 spill 轮次 exec 输出，已记入 PROOF-NOTE §6） | 最低真墨行 y=1209，盒底 1202.6，真墨溢出 **+6.4px**；裁图 `render/crop-p4-programma.png` 目视确认行在盒外白地 | **FAIL — D11** |
| D3 回归 | PIL `font.getbbox` 1x 真墨（P2 左右列） | `gates-reproof.log`（右列；左列以 getbbox 校验值见 PROOF-NOTE §7） | 右 a +97.5 / b +44.5 / c +71.5 / d +55.5；左 25 +272.5 / 26 +279.5 / 27 +199.5 / 28 +258.5（边 1862） | PASS（均 ≥+44.5） |
| 金句在框/在版 | P7 `ZINNEN VAN DE WEEK` 8 句坐标 + 最低真墨行 vs 页脚带 | `inkprobe2-reproof.log` | 8 句 x=88/989、y 2038–2324；最低真墨 y=2378.0，页脚带顶 2439，余量 61.0px；无包围盒（开放式排版，见 content7.py:122） | PASS |

## 5. 印/网文字层与 PDF

| 门禁 | 命令/方法 | 源日志 | 实测值 | 结论 |
|---|---|---|---|---|
| 印/网 token 多重集 | PyMuPDF 逐页（自写 `gates_reproof.py`，0.1pt 取整） | `gates-reproof.log` / `gates-reproof.json` | 8 页 multiset diff **0**；tokens 774/715/673/671/705/663/742/1917（与修复者计数法不同，取法差异） | PASS |
| 印/网位置 | 同上 | 同上 | 仅 P1 两 token（`De`/`Lucerna`，x 394.0 vs 393.8，0.2pt），其余页 0；交付网与 scratch 重渲结果相同 | PASS（内容一致；0.2pt 为子集化微差，见备注） |
| pdftotext | `pdftotext` 印/网/重渲三方 | `print-text-reproof.txt` / `web-text-reproof.txt` / `web2-text-reproof.txt` | 44,197 B = 44,197 B = 44,197 B，**逐字节一致** | PASS |
| 网 PDF scratch 重渲 | 复制 svg 至 `webpdf/svg`，`tools/webpdf.py` 仅写 scratch（未覆盖交付件） | `webpdf.log` | rc=0；重渲 2,104,002 B（交付 2,103,990 B，+12 B）；8 页内容流逐字节一致；6 个字体子集流长度相同、字节不同（fontTools 逐次不定）；文字层一致 | 注：字节不可复现，文字层一致 |
| 引号 | 印 PDF 全文 + text.md 计数 | `gates-reproof.log` | ASCII `"` 0、反引号 0；`« »` 35/35；`“ ”` 1/1；md 同值 | PASS |
| 金句逐字 | 8 句金句在 text.md 正文检索 | `gates-reproof.log` | **8/8** | PASS |
| D5 字体（只记录） | 自写 census（`<text>` 含 `[A-Za-z]` 且无 CJK 区字符） | `gates-reproof.log` | 字体段 Noto Sans CJK SC 619 / Newsreader 1215 / Noto Serif CJK SC 305 / UnifrakturMaguntia 1；纯拉丁落 CJK **245** 段（分版 38/23/30/29/29/26/18/52） | 记录，不判 |

## 6. 源码/文本 diff

| 门禁 | 命令/方法 | 源 | 实测值 | 结论 |
|---|---|---|---|---|
| 源码变化范围 | diff 当前源 vs fix3 `freeze/build-copy`（已验该副本为 fix3） | （exec 输出） | content56 仅 D8、content8 仅 75 行、content7 仅 D10；bslib4/content12/content34 逐字节一致 | PASS |
| text.md diff vs fix3 | `diff scratch-fix-nl4/text-before-fix4.md` vs 当前 text.md | — | **仅第 416 行**（Q140 加 `kort `） | PASS |
| FIX-LOG/WEEKLY-KIT | 读 FIX-LOG 第 4 轮与 WEEKLY-KIT §15 | `core-nl/FIX-LOG.md` / `WEEKLY-KIT.md` | 记录与实测一致（除 §8 所列两则文字笔误：片段数“11”实为 12；D10 窄化论述不完整） | 记录一致 |

## 7. 目视（印 PDF 1.5x 自渲染，`render/p1–p8.png` + 裁图）

| 页 | 结果 |
|---|---|
| P1 | 干净。词首 `De Lucerna` 无异常；NU JIJ 1–6、BLIKSEMQUIZ 7–10 齐全。 |
| P2 | 基本干净。`c. eten voor Sinterklaas' paard` 在界内；“D WOORDEN”标题在第 3 栏底、内容在第 4 栏（修前既有分栏，观察，不列缺陷）。 |
| P3 | 干净。D6/D7 修复处无复发；HET PERFECTUM 桥接 `hebben/zijn。` 句号在行末。 |
| P4 | **FAIL — D11**：HET PROGRAMMA 盒末行 `18:45 uur.` 在盒外（见 §4/PROOF-NOTE §6）。其余干净；D5 第 5 条事实在盒内（前 4 行）。 |
| P5 | 干净。EN JIJ 盒末行在盒内；Q73 填空区无异常。 |
| P6 | 干净。D8 图注两行在盒内；VOOR OF TEGEN 盒内容齐全。 |
| P7 | 干净。D10 读者来信两行在盒内；金句 8 句 + 页码注齐全；VOLGENDE WEEK 带内有余量（proof2 N3 旧貌）。 |
| P8 | 干净。Q140 键含 kort；Q150 范文齐全；答案区 150 题无缺行。 |
| 裁图 | `crop-p6-d8.png`（D8 。回行末）✓；`crop-p7-d10.png`（D10 ，回行末）✓；`crop-p8-q140.png`（Q140 含 kort）✓；`crop-p4-programma.png`（D11 行在盒外）✗ |

## 8. 汇总

- **通过**：D8、D9、D10（修复正确、最小、同类）；孤儿 sweep (a)/(b) 0/0；150 题机械+手验；freeze 8/8；occlusion 0；p8 150/150；P8 ≥10.12pt；印/网文字层一致；creambox 3 处假阳性真溢出 0；D3 回归；引号/金句/Q150；text.md 重导出字节一致；构建/渲染字节可复现。
- **不通过**：**D11 一项** — P4 HET PROGRAMMA 盒末行 `18:45 uur.` 真墨溢出盒底 +6.4px（基线 +6.89px），`content34.py` 盒高公式预留不足；修前旧患（fix2 D5 引入，fix3 亦有）；creambox 脚本盲区所致漏检。
- **结论 (b)**。fix4 自身全过，但核心整体含 D11，**不确认进入 nl delta 重建**；建议 fix5 修 D11 并补 spill sweep 入常驻门禁后重新复校。
