# GATE-LOG — 2026-W47 nl-es · proof1（delta build-4）全部门禁逐项实测

- 版：`production/2026-w47/2026-w47-nl-es/`（核心 `production/2026-w47/core-nl/` fix5；pre-delta `production/2026-w47/fanout-nl/2026-w47-nl-es/`）
- Python：`~/workspace/weekly-git/tools/venv/bin/python`
- scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-es1/`（全部中间文件、脚本、日志只在此）
- 结论汇总：**3 缺陷（D1–D3，§2）**；其余门禁全部通过；150 题 150/150；生产未动、未 commit、未 push。

## 0. 身份核对（三 SHA 实测，与任务给定值逐字一致）

| 成品 | SHA-256 实测 | 字节 | 日志 |
|---|---|---|---|
| 印 `De-Lucerna-VOL4-nl-es.pdf` | `45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8` | 12,669,539 | `print.txt` |
| 网 `De-Lucerna-VOL4-nl-es-web.pdf` | `47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb` | 1,616,177 | `web.txt` |
| 文 `2026-w47-nl-es.text.md` | `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` | 47,649 | `print.txt` |
| 核心印 | `b7d4a9cddbc38dd56ddd22cd2ae15a2e04ba1988670b6cf384eafbc66bd7ce47` | 25,955,578 | 终端 |
| 核心网 | `5a47449cdff7d5847aee81c1c5b0f1af54cfeda873c5b55058a6d18f0e10404c` | 2,104,000 | 终端 |
| 核心文 | `0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c` | 44,093 | 终端 |

- 生产 SVG 哈希（`prod-svg-sha.txt`）：p1 `c5764d8c…`、p2 `42ce31f4…`、p3 `1b9c22c9…`、p4 `e90c156c…`、p5 `a9ee5718…`、p6 `5807b1d4…`、p7 `8c1b3995…`、p8 `da9168d6…`；与 staging 比对：仅 p4 不同（staging p4 `278c621a…`），其余 7 页逐字节相同（D11 预期）。
- 生产 SVG 在重建前后两次核对一致：**未动**（`EDITION SVGs UNCHANGED`）。

## ① run.py 重建（scratch 副本内）— PASS

- 命令：scratch 副本 `work/ed/`（`cp -a` 版目录，删 `__pycache__`）内运行 `run.py`，输出重定向用 scratch 内绝对路径。
- 结果：rc=0；TOTAL 150；分面 10/18/18/18/18/18/12/38；级别 A2 46 / B1 73 / B2 31；模型词 81；`FLOW OVERFLOW`/`HEAD TOO WIDE` grep 计 0。
- 重建 SVG **8/8 字节一致**（`rebuilt-svg-sha.txt`）；`render.py` rc=0，8 卡片，重建印 PDF SHA `45a4c25e…` = 生产印 PDF，12,669,539 B（逐字节相同）。
- `webpdf.py`（`tools/webpdf.py <svg-dir> <out-pdf>`）rc=0：1,616,176 B（交付 1,616,177 B，差 1 字节，预期：网 PDF 字节不可复现），46,814 文字字节。
- 日志：`run-rebuild.log` / `render-rebuild.log` / `webpdf-rebuild.log`。

## ② freeze — PASS

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-core`：rc=0，**8/8 字节一致**，核心完整性确认（8 文件重哈希一致）。
- 本版自身（clean-dir 重建）：**8/8**。
- `freeze.py diff` 核心↔本版：rc=0；新增 CJK = 7 × U+3000（SOP §1.1 分隔符），其他新增 CJK 0。
- 日志：`freeze-core.log` / `freeze-diff.log` / `freeze-diff.json`。

## ③ occlusion 真实审计 + 孤儿/spill/盒底横扫 — 审计 PASS，盒标题越框见 §2 缺陷

- `tools/occlusion_audit.py`（生产 svg 目录）：rc=0，selftest OK（全部植入类触发），**0 flags**（`occlusion.log` / `occlusion.json`）。
- 注意：occlusion 对横向越框、盒标题溢出、盒底溢出、D11 类整行出盒有盲区——盒标题与 D11 类已另以 PIL 真墨 + 交付 PDF 渲染像素实测，见下。
- 孤儿横扫（`orphan_spill_nl.py`，PIL + svglib 实测 + 暴力行首标点，1452 行）：a 类 0、b 类 0，两法；行首标点暴力 0（`orphan-spill.log` / `orphan-spill.json`）。
- Spill 横扫（奶油盒）：6 处 BELOW 候选，全部判定为非溢出（下一栏自有标题/注脚：P1 +24 `HET WOORD VAN DE WEEK`；P2 +50.5 Nota 行；P2 +32 `Let op: schrijf je gedicht…`；P5 +50.5 Nota；P7 +60 `HET WOORD…` 与 +60 `BRIEVEN VAN LEZERS`）；P4 D11 盒：0 处 BELOW。真溢出 **0**。
- 盒底包含（PIL 真墨底 vs 盒底）：仅 3 盒余量 <5px，全部通过：P2 EN JIJ +2.8px、P5 EN JIJ +2.9px、P6 统计图 +4.2px。
- 第 A 节全文本墨缘扫描（PIL）：共 18 旗——16 × LEFT +0.2（墨 87.8 vs 88，系统性、核心亦同），1 × P6 标题 RIGHT +0.5，1 × P8 头行 RIGHT +0.0；其余文本均在内（`measure.log`）。

## ④ p8 extract + compare — PASS

- `tools/p8.py extract --p8 …/p8-toets.svg --total 150`：noted 集 **150/150**（`p8-extract.log` / `p8-extract-ed.json`）。
- `tools/p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 …`：状态 **CLEAN**，missing=[]、extra_count=0、uncertain=[]、keydiff=[137, 138]（仅翻译题按设计对西语重定向）（`p8-compare.log` / `p8-compare.json`）。

## ⑤ 印/网文字层 — PASS

- PyMuPDF 位置排序 token 表：印 vs 交付网、印 vs 我重建的网，逐页一致——P1 820、P2 829、P3 735、P4 742、P5 807、P6 762、P7 919、P8 2431；posdiff 0，集合相同（`textlayer_nl.py` / `textlayer.log`）。
- pdftotext 字节：印 = 网 = staging build-3 印 = 106,419 B，逐字节相同。
- 网 PDF 字节不可复现（交付 1,616,177 B vs 我重建 1,616,176 B，差 1 字节）——只比文字层，符合预期。

## ⑥ P8 最小字号 — PASS（下限 9.75pt）

- PyMuPDF：P8 整页及答案区最小 10.12pt（中位 10.12pt，184 spans）≥ 9.75pt。SVG 最小字号 13.5（`check-s11.log`）。

## ⑦ 盒标题逐一 PIL 真墨 + 交付 PDF 渲染像素 — **FAIL（D1，见 PROOF-NOTE §2）**

- 25 盒标题 PIL 横扫（`measure_nl.py` 第 B 节，正确字号）：仅 P6 DE GRAFIEK 越框（−0.5px）；次紧为 P4 Nota +19.5px、P3 Nota +20.2px、P2 ZO ONTHOUD +20.8px、P7 HET WOORD +21.8px。P6 VOOR OF TEGEN 标题 PIL +103.5px。
- 交付 PDF 渲染像素（裁定法，`edge_raster.py`，200dpi 严格 `<128`，x1850–1950/x0–100 两带，8 页）：
  - P6 标题至 1865.9（300dpi）/ **1866.08（600dpi，+4.08px）**；PDF span x1=1866.3（PIL 排宽 400.9，Cairo 404.8）；2× CairoSVG 重渲染至 1866.0–1866.5；staging build-3 印 PDF 同带 1865.9。
  - P1 桥接行至 **1865.8（+3.8px）**；P2 栏目标题至 **1865.4（+3.4px）**；家具行（P2–P6）至 **1863.8（+1.8px）**；P8 头行至 **1863.8（+1.8px）**。
  - 仅上述 R 带；P7 R 干净；核心印 PDF 同法 8 页 R 全部干净。
  - 证据：`crops/p6-title-de-grafiek.png`、`crops/p1-bridge-row.png`、`crops/p2-head-row.png`；日志 `edge-raster-core.log`、`verify-items.log`、`verify-pixels.log`、`verify-p6strip.log`。
- 旧 O3 升格为本次 D1：PIL +0.5px 与 1:1 卡片 `<128` 扫描对此类越框均不敏感（1:1 卡片对 P6/P2/P8 均回 0）。

## ⑧ 150 题逐题手验 — PASS

- 三源比对（`keycheck_nl.py`）：登记（scratch 副本重建导出，150 条）vs text.md 答案（150 条解析）vs P8 印出键（150 条）→ **150/150 MATCH**（Q150 开放写作例外）（`keycheck.log` / `keycheck-150.json` / `registry.json`）。
- 荷兰语题干 vs 核心 text.md：仅 Q139/Q140 差异（按设计）；Q1/Q25/Q141 的三源“差异”为解析器跨栏位产物，可见差异仅 gloss 语言西语 vs 中文。
- 配对题键经 P2/P8 选项表核对：Q25–28 = d/c/a/b；Q141–144 = b/c/d/a。
- 算术重算 Q22/Q45 19 天、Q43 1 天、Q44 4 小时、Q46 17 年、Q85 65、Q87 100 全部通过；小组积分与四场比分内部一致；Q150 模型文 81 词（80–100）。
- 日期/星期经 `date`（Europe/Amsterdam）核对 10 个日期全部一致；PSV 26 / Feyenoord 25 / Ajax 25 经外部检索 6+ 源确认；Heerenveen–Feyenoord 5–3 确认。
- Q63/Q126 来源在版内：text.md:187 与 P4 盒（SVG y=1054.37 / y=1084.90），核心 text.md:188 亦有。
- Q78 `Zij` 单数：与 Q79 复数构成设计对比，列观察 O1、不列缺陷。

## ⑨ 全页目视 P1–P8 — PASS（除 §2 越框在整页尺度不可见）

- 重建渲染卡 `work/ed/cards/p1-voorpagina.png` … `p8-toets.png`（8/8 逐字节一致之 SVG 重渲染）逐页目视：版式干净，无重叠、无压页脚、无截断；图片均有来源标注。
- P4 HET PROGRAMMA 盒目视确认末行下方留白充足（D11 实修）。约 2–4px 右缘越框在整页尺度下不可见，仅放大/光栅扫描可测。

## §1.1（nl 适配 check_s11_nl.py）— PASS

- 纸面 rect `#fbfaf6` 8/8 在位；颜色集核心 = 本版 = 19，无多无缺；VOL.4/VOL.5 计数与核心逐页一致。
- 徽章 rect 计数 + 颜色多集与核心逐页一致：P1 10、P2 15、P3 18、P4 18、P5 18、P6 18、P7 12、P8 35；A2 `#5c6e30`、B1 `#46581f`、B2 `#37402f` 均在版。
- P8 最小 SVG 字号 13.5；填空 (113)–(120) 与对话 (145)–(149) 均在位（nl 以裸 `113.` 形式渲染）；写作头 `H　SCHRIJF ZELF` 在位。
- 日志：`check_s11_nl.py` / `check-s11.log`（rc=0）。
- D5 字体（只记录、不修）：本版 Noto Sans CJK SC 645 / Newsreader 967 / Noto Serif CJK SC 25 / UnifrakturMaguntia 1；纯拉丁-CJK 段 58/66/59/58/61/62/63/70 = 497（核心 245）。此为 §2 越框的合理机制解释，仅记录。

## Delta 六处复核 — 全部通过

- D6 w=377.5：自测区间 329.5–425.5，连续，中点 377.5；重现 2 行；p3 逐字节同 pre-delta（`width_scan_nl.py` / `width-scan.log`）。
- D7 w=419.5：自测区间 414.5–424.5，连续，中点 419.5；重现 3 行；p7 无孤儿。
- D8 capcn_w=370.75：自测区间 349.5–392.0，连续，中点 370.75；重现 4 行；`P6 chart ends 717` 不变；无行首标点。
- D9：三源一致（`content8.py:75`、text.md:415、P8 节点），手验 `kort` 与题干契合；keydiff [137, 138]。
- D10 dt_zh_w=362.5：自测区间 319.5–405.5，连续，中点 362.5；重现 2 行；`P7 col3 ends 1927.0` 不变。
- D11：`content34.py:130-134`，sh 638.0，盒底 1229.6，末行基线 1209.49，基线余量 +20.11px ≥ +20px；PIL 真墨余量 +19.86px（delta 称 +20.60px，方法差、小差异）；盒下 7px 带 0 黑像素（卡片与交付印 PDF）；事实行 14 行，sh 611.0 → 638.0；p4 唯一改动 SVG。

## 旧版缺陷状态（逐项独立重验）

- D1 `¿SÍ O NO?` 已修（现 +103.5px）；D2 `PALABRA SEMANAL` 已修（现 +21.8px）；D3 未重现（旧报告误引题，实际 `c. eten voor Sinterklaas' paard`，余量 +72.0px）；D4 已修（`答案：` 0 次，`Respuesta:`，CJK 0）；D5 误报（来源在版内 + 外部 6+ 源确认）；D6 已修（§3 D9）；D7 已修（网 PDF 含 `LucernaNewsreader-Italic`，P1 斜体 16.12pt 印/网一致）。
- 旧 O2 现 +2.8/+2.9px（通过，偏薄）；旧 O3 升格为本次 D1。

## 观察类（不列缺陷）

- O1 Q78 `Zij` 单数设计对比；O2 盒底偏薄 3 处（+2.8/+2.9/+4.2px，通过）；O3 左缘系统性墨 x=87.8（0.2px，核心亦同）；O4 无孤儿、无 spill；O5 D5 字体记录（§1.1）；O6 P4/P6 中栏留白（核心版式继承）。

## 脚本/日志清单（scratch 内）

`dump_reg_nl.py`、`registry.json`、`width_scan_nl.py` + `width-scan.log`、`measure_nl.py` + `measure.log`、`orphan_spill_nl.py` + `orphan-spill.log` + `orphan-spill.json`、`textlayer_nl.py` + `textlayer.log`、`keycheck_nl.py` + `keycheck.log` + `keycheck-150.json`、`edge_raster.py` + `edge-raster-core.log`、`check_s11_nl.py` + `check-s11.log`、`run-rebuild.log`、`render-rebuild.log`、`webpdf-rebuild.log`、`freeze-core.log`、`freeze-diff.log` + `freeze-diff.json`、`occlusion.log` + `occlusion.json`、`p8-extract.log` + `p8-extract-ed.json`、`p8-compare.log` + `p8-compare.json`、`prod-svg-sha.txt`、`rebuilt-svg-sha.txt`、`print.txt`、`web.txt`、`print-stage.txt`、`verify-items.log`、`verify-pixels.log`、`verify-p6strip.log`、`crops/p6-title-de-grafiek.png`、`crops/p1-bridge-row.png`、`crops/p2-head-row.png`、`work/ed/`（scratch 重建副本）。
