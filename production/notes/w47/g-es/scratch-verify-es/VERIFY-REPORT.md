# VERIFY-REPORT — W47 es 家庭 §8.4 状态核对

- **核对员**：本轮（与 round-6 校对员 50ffaae9、fix-es-ru2 修复者 f9272fd5 均不同）
- **日期**：2026-11-13（UTC 约 04:40–05:30）
- **任务**：核对 es 家 round-6 CLEAN（2026-11-12 ~22:35 UTC，重校员 50ffaae9，PROOF-NOTE-6.md）是否仍成立，即其后 es 家有无重建改 SHA。
- **结论总览：round-6 CLEAN 不再全家成立。10 版 VERIFIED CLEAN；1 版（es-ru）SHA 已变，本人已做全新全量重校（PROOF-NOTE-7.md），结论 (b) 1 项 low 发现，须修。**

## §1 最后重校记录（round-6，2026-11-12 ~22:35 UTC）

- 工人：重校员 50ffaae9；记录：`hidden_files/w47/scratch-reproof6-w47-es/PROOF-NOTE-6.md`；run-log 4819–4821 行。
- 结论：(a) CLEAN，0 findings；es 家庭定稿（第 6 家）。
- 指纹：33 个 SHA（印/网/text.md × 11 版），见下表“round-6”列。

## §2 round-6 之后 es 家的变动（run-log 核查）

round-6 之后 es 家只有 **es-ru 一版**两度重建，其余 10 版未动：

1. **\*-ru 重建**（工人 e044c613，2026-11-12 ~23:48 UTC；run-log 4874、4918 行）：拉丁字体路由修复（Noto Sans → Newsreader）。es-ru 印 538ca756749a/3,213,297 → **277b2d26…/3,100,942**，网 8d440e9b52cf/1,061,847 → 98536828…/950,829，text.md 未变。门禁扫查报 **boxtitle 1 DEFECT**（P1 `цифрах` +22.3px）。
2. **es-ru boxtitle 修复**（工人 f9272fd5，2026-11-13 ~01:27 UTC；run-log 4972–4976 行）：P1 框标题降字号 23→21pt（`content12.py:46` 加 `tsize=21`），措辞未动。印 277b2d26…/3,100,942 → **d383753b4862/3,100,944**（+2 B），网 98536828…/950,829 → **b6246122f94d/950,823**（−6 B），text.md 未变。协调员独立核实门禁全绿，KIT 已更新。run-log 4976 行：“es-ru 至此干净；es 家其余 10 版未动。”
3. 此后再无 es 家改动（run-log 4976 行之后至 5101 行末，无 es 家记录；盘上 SHA 与上述修后值一致）。

## §3 逐版核对 — 当前磁盘 SHA vs round-6

实测：`sha256sum` 印/网/text.md 各 11 版，共 33 个。

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） | vs round-6 | 结论 |
|---|---|---|---|---|---|
| core-es（= es-zh-cn） | 4,317,615 / `6089c0fa5420` | 1,162,042 / `f0f6ed1de57a` | 43,789 / `9cc6462f702c` | 一致 | **VERIFIED CLEAN** |
| es-de | 2,916,396 / `3fdc2ce60e6a` | 806,895 / `fd7edd4b8415` | 45,370 / `ff0387066ca9` | 一致 | **VERIFIED CLEAN** |
| es-en | 2,915,635 / `a7d5aba8bd0f` | 806,124 / `bb690dd25b6c` | 45,046 / `3c2ef9876638` | 一致 | **VERIFIED CLEAN** |
| es-fr | 2,914,957 / `fd0e9f83a989` | 805,426 / `960de8cf8d3b` | 45,834 / `ad8bcbcd0c4f` | 一致 | **VERIFIED CLEAN** |
| es-it | 2,913,352 / `0cffc84e47c0` | 803,822 / `f533bb1aa133` | 45,211 / `491044bcfaab` | 一致 | **VERIFIED CLEAN** |
| es-ja | 8,530,586 / `cbb3efedd9a2` | 1,280,143 / `70d46e27721f` | 46,578 / `bab03d4d6c8a` | 一致 | **VERIFIED CLEAN** |
| es-ko | 5,229,281 / `e2ae545b1462` | 1,097,497 / `fad91509e34f` | 47,403 / `8407be401bb7` | 一致 | **VERIFIED CLEAN** |
| es-nl | 2,915,320 / `c716ce60992a` | 805,809 / `8be3118b5080` | 45,342 / `d477656f5ef0` | 一致 | **VERIFIED CLEAN** |
| es-pt | 2,914,243 / `ce89b874dfc0` | 804,705 / `06514f66f69d` | 45,576 / `7db6b340f4f6` | 一致 | **VERIFIED CLEAN** |
| **es-ru** | 3,100,944 / **`d383753b4862`** | 950,823 / **`b6246122f94d`** | 52,367 / `ac246f8709d3` | **印/网已变**（round-6：印 538ca756749a/3,213,297、网 8d440e9b52cf/1,061,847；text 未变） | **重校：(b) 1 项 low，见 §4** |
| es-zh-tw | 4,381,575 / `fd3e65ef1840` | 1,265,861 / `8871073245fd` | 43,818 / `d26fdddc0fa6` | 一致 | **VERIFIED CLEAN** |

- 10 版 VERIFIED CLEAN：最后重校结论 CLEAN 且 3 个 SHA 与磁盘逐字节一致，round-6 结论对这 10 版仍成立。
- es-ru：印/网 SHA 自 round-6 后变过，按任务第 3 条做了全新全量重校（见 §4）。

## §4 es-ru 全新全量重校（第七轮，PROOF-NOTE-7.md）

- **结论：(b) 1 项 low 发现 — 不 CLEAN。**
- **F1（low，P5）**：EJERCICIOS 分隔线（y=1608，全宽）横穿 ¿Y TÚ? 奶油框（框底 1633.55），框底超出分隔线 25.5px，框内俄文末行 `пришлите их.` 被绿线隔在框体之外一侧。字形未被线划过，文字全部可读。目视 + 几何双重核实（`p5-zoom.png`）；8 页横扫仅此一处。
- 溯源：框高随字体改道逐次变高（303.0 → 329.0 → 356.0），分隔线 y=1608 未动；D5 前基线框底 1606.55（距线仅 1.45px）；交叉出现于 11-12 字体改道期间。round-6 当时的框高无存世副本可核，不能断定是 D5 还是 *-ru 引入。
- 其余全部通过：text.md 1888 行通读无问题；150 题逐题核对全一致（p8 extract 150/150、compare CLEAN keydiff [137,138]）；日期/星期全验正确；RTVE 算术 195 分钟正确；范文 97 词机械计数正确；8 金句各 2 次逐字一致；Sargent 图注独立检索核实属实；8 页逐页看图除 F1 外干净；机械门禁全绿（D5 census PASS、occlusion 0 flags、boxtitle 0 DEFECT、spill 0、edge 0、freeze 8/8、印/网文字层逐字节一致 53,413 B）。
- **待修清单（仅此 1 项）**：
  - **F1 — es-ru P5**：分隔线横穿 ¿Y TÚ? 框（25.5px）。修法建议（协调员定）：缩短框内俄文使框高回落至分隔线之上（约省 26px ≈ 1 行），或调框内行距/字号。改后须重建 + 全部门禁 + 再做一轮全量校对（SOP §8.4）。
- 注：occlusion/spill/boxtitle 三工具均未覆盖“分隔线 vs 内容框交叉”这一缺陷类（线走行间空隙、文字在框内，故三门皆绿）；建议修后把该检查补进共享工具。本人只核对，未改工具。

## §5 KIT §7 SHA 核对（11 版）

- 方法：每版现行印/网/text 完整 SHA-256 在其 KIT 中出现次数。
- 结果：**11 版全部一致，无 wave-2 缺口。**每版印 ×1、网 ×1、text ×2（es-ru 因两次重建的历史记录为印 ×2、网 ×2、text ×4）。wave-2 清单：es 家无条目。

## §6 工作记录与约束遵守

- **只读核对**：未改任何生产文件，未 commit/push，未跑 `lint --write`，未 reset/stash/add -A；只碰 es 家 11 版；工具解释器 `tools/venv/bin/python`，只用仓内共享工具（p8.py、d5_census.py、occlusion_audit.py、boxtitle_check.py、spill_sweep.py、pdf_edge_scan.py、freeze.py）+ pdftotext/pdftoppm/`date`。
- **磁盘**：96G 已用（150G 卷），未触发 ≥100G 停线；结束仍 96G。
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-verify-es/`：`VERIFY-REPORT.md`（本文件）、`PROOF-NOTE-7.md`、`gates7.sh` / `gates7.log` / `occlusion2.log` / `occlusion.json` / `p8-extract.json` / `p8-compare.json` / `census.json` / `boxtitle/` / `spill/` / `edge/` / `freeze/` / `pg-1.png` … `pg-8.png` / `p5-zoom.png`。
- **过程自纠**：首轮 occlusion 调用误加 `--selftest`（该 flag 含义为“只跑合成自检”，不审 SVG，会造成假通过）；已发现、正确重跑（0 flags），并在 gates7.log 追加更正。报告中的 occlusion 结论以重跑为准。
- **建议下一步**：协调员定 F1 修法 → 派 es-ru 单版修复 → 重建 + 全部门禁 → 再派一轮全量重校（与本轮校对员不同人）；其余 10 版已 VERIFIED CLEAN，可按既定流程继续（insert / 封面 / 全 lint），不受 F1 阻塞——但 es 家 bundle 入仓须等 es-ru 修完重校通过（一个 bundle 一个 commit）。
