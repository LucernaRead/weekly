# GATE-LOG — W47 fr-ko proof1（独立复跑）

- 时间：2026-11-11 12:48–13:10 EST；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR：goals 侧 `hidden_files/w47/scratch-proof-fr-ko1/tmp`（未用 /tmp）。
- 探针：开工前 `/dev/null` 存在、`git hash-object -w` 通（rc=0）；goals 侧写文件探针通。**注意：复核中途约 13:03 `/dev/null` 再次消失（git 报 `could not open '/dev/null'`），`touch /dev/null` 垫回后 git 恢复，未误判为配额问题。**开工前磁盘 SHA 已核对（见 PROOF-NOTE，与任务书完全一致）。
- 复跑脚本：同目录 `proof_gates.py`（逐门复刻 fr-de proof1 的同名脚本，改 ko 路径与 band 阈值；结果写本目录；**未在生产目录重跑构建**——确定性门改为沙盒副本重建）。
- 注：core-fr 无 `check_core.py`（ru/pt 系有）；fr 系等效覆盖 = freeze diff + source/string freeze + 确定性重建，均已跑并通过。

## 1. freeze 首检（任务指定先跑）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-ko/svg` → rc=0，**8/8 页**（日志 `freeze-diff.log`）：
p1 +26/-23，新增 188；p2 +35/-33，新增 300；p3 +37/-34，新增 168；p4 +56/-39，新增 208；p5 +47/-34，新增 216；p6 +43/-28，新增 172；p7 +35/-34，新增 368；p8 +155/-122，新增 945。**新增 CJK 合计 2,565。**

### 新增 CJK 全量分类（`cjk_inventory.py` → `cjk-inventory.json`，逐字符对照 expl.py E 值）

| 页 | 新增 | 韩文音节 (U+AC00–D7A3) | U+3000 结构空格 | 『』 (U+300E/U+300F) | 未入账 |
|---|---|---|---|---|---|
| p1 | 188 | 188 | 0 | 0 | 0 |
| p2 | 300 | 299 | 1 | 0 | 0 |
| p3 | 168 | 168 | 0 | 0 | 0 |
| p4 | 208 | 208 | 0 | 0 | 0 |
| p5 | 216 | 214 | 0 | 2（1 对） | 0 |
| p6 | 172 | 171 | 1 | 0 | 0 |
| p7 | 368 | 368 | 0 | 0 | 0 |
| p8 | 945 | 924 | 15 | 6（3 对） | 0 |
| **合计** | **2,565** | **2,538** | **17** | **8（4 对）** | **0** |

- 韩文音节 2,538：全部为韩语讲解层（标题译名、词汇注记、练习说明、答案区注记），每个字符均在 `expl.py` 的 E 值字符集内（string_freeze 门亦验 0 未入账）。
- U+3000 ×17：结构全角空格（双语标题分隔），允许。
- 『』×4 对：韩式引号，见于 P5 `LE CINÉMA DU MERCREDI` 韩注（『헝거 게임』）与 P8 答案区注记（『레 브라브』『카망베르』等），为讲解层原文标点，非结构残留。

## 2. 独立门禁 14/14 PASS（`gates-proof1.json`）

| 门 | 结果 |
|---|---|
| run（builder build-run1.log 读检） | PASS：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE（DORE NOSPACE 行除外，见下）；TOTAL 150，A2 53 / B1 75 / B2 22，by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion（`tools/occlusion_audit.py`） | PASS：0 flags，selftest OK（`occlusion-proof1.json`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys 150/150，printed notes 121/150（`p8-proof1.json`） |
| p8_compare（vs core P8 SVG） | PASS：CLEAN，keydiff [150]（writing key only）（`p8compare-proof1.json`） |
| source_freeze | PASS：content*.py / bslib4.py / svglib.py / run.py 与核心字节相同；render.py 仅 BASE+PDF 名差异 |
| string_freeze | PASS：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免（与 de 版同为核心 `stem_e1` 前缀 `Traduisez: `） |
| text_layer | PASS：印/网 pdftotext 逐字节一致（102,735 B）；web 2,048,862 B < 7MB；print 23,103,417 B（`print-proof1.txt` / `web-proof1.txt`） |
| p8_font | PASS：P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（vs `core-fr/final-fr-p8.json`） | PASS：150 键仅 Q150 不同，核心 150 键 / 抽取 150 键 |
| mcq（`check_mcq.py`） | PASS：bodies 45，rendered lines 1449，DEFECTS: 0，UNLOCATED: 0（`mcq-proof1.log`） |
| widths | PASS：31 单行串全部在预算内；4 组共行对均 ≤1757 |
| band_spans（印刷 PDF span 实测） | PASS：FR title ends 1236.9，band_r1 starts 1436.9（净空 200.0），FR sub ends 837.2，band_r2 starts 1563.3 |

- 附注 run 门：构建日志含一行 `P7 DORE NOSPACE: y0= 1016`（与 fr-de build 日志同类提示），export 步骤已处理（`inserted P7 Dore caption after B1 example box`），与 fr-de proof1 同口径不计入坏 token；P7 目视 Doré 图注在位、无溢出。另 gates.json 的 p8 extra 若显示 "?" 是驱动误读键名——本次直接读 `p8compare-proof1.json`，status CLEAN。

## 3. 确定性（沙盒副本重建，替代 gates 第 7 门）

版目录完整拷贝至本目录 `rebuild/ed/`（副本已删，仅留 `rebuild/run-proof1.log`），删 svg 后重跑 `run.py`（rc=0，TOTAL 150，类型分布与 builder 一致：完成句子 49 / 单选 26 / 句型转换 7 / 词汇配对 21 / 阅读判断 5 / 图表读数 6 / 跟练 8 / 改错 4 / 完形填空 8 / 阅读理解 5 / 翻译 5 / 对话补全 5 / 写作 1），8 个 SVG sha256 与在版文件**逐字节一致 8/8**：`4e1d1ac2 / c172ea06 / 591b514a / 5cf88f14 / 946a7778 / 77321a37 / b1769f84 / b533645f`（与 builder `freeze_direct` 记录的哈希逐一相同）。

## 4. creambox 规范扫描（`hidden_files/w47/tools/creambox.py`，日志 `creambox-proof1.log`）

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；inside-only 清除全部为正，P1 +48.0 / P2 +47.7 / P3 +47.7 / P4 +47.7 / P5 +47.7 / P6 +48.5 / P7-TOOLBOX 最小 +24.7、desc-clear +18.8）。
- **P7 读者园地盒（重点，自测裁定）**：`y=1878 bottom=2258.0`，naive 行即为 inside-only 行 `last baseline 2233.3 clearance +24.7`，无负值。per-line 表：两行韩文 disclosure（基线 2206.0 / 2233.3），末行 '투고 평론 약속을 지킨다.'。PIL 真墨测量（见 PROOF-NOTE）：末行真墨至 svg y≈2234.4，**清除 +23.6px**；其下零墨至 2269.6；深绿带绘图实测起于 2270.0。**结论：干净，无溢出。**（fr-de 复校员的跨版目测 "+24.7" 与本次自测一致，但本裁定不依赖它。）
- 其余 6 处负值逐盒核对：P1 `y=1280` 盒（inside-only 1604.0 +48.0，误报行 'LE MOT DE LA SEMAINE' +24.0）；P2 `y=886` 盒（1013.4 +47.7，误报 'LA SEMAINE EN CHIFFRES' +37.0）；P3/P4 `y=200` 盒（327.7 +47.7，误报 'À VOUS !　당신 차례!' +37.0）；P5 `y=2182` 盒（2309.9 +47.7，同误报 +37.0）；P6 `y=463` 盒（741.2 +48.5，误报 'IL EST PRÉVU QUE + SUBJONCTIF' +37.0）与 `y=1330` 盒（1608.1 +48.5，误报 'LE DÉBAT　토론' +37.0）。其余盒（P2 `y=647` 盒 924.2 +23.4 等）均为正。

## 5. 150 题三源交叉（`triple_check.py` → `triple-check.json`）

版 P8 keys / text.md 答案区（RÉPONSES 区域 1053–1087 行，150/150 解析）/ 核心 P8 keys：**唯一差异 Q150**（写作键：核心 `开放题` → ko `자유 작문`，预期翻译）。其余 149 键三源完全一致。Q148 `devant` 三源一致（记录项 R1，核心继承问题，只记录）。

## 6. 目视与内容手验

- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png`）：零问题；P1 band 无重叠；各页无溢出、无遮挡、无截断；图注完整；P8 答案流完整。
- 网页 PDF 抽查（`png/web-p1.png`、`web-p7.png`，100 dpi）：与印刷版布局、图片一致。
- 150 题逐题手验（`.text.md` 1,087 行全文通读）：150 键全部正确；仅 R1（Q148 核心继承错法语）与 R2（D5 字体）两项记录，见 PROOF-NOTE；另 R3（"next Sunday" 行号与盘上现状不符，本版无此串）。
- D5 字体普查：ko 版 CJK 字体段 816（452 含 CJK / 222 纯拉丁字母 / 125 纯数字标点 / 17 纯标点空格）；核心对照 776（415 / 219 / 125 / 17）；ko 仅多 3 段纯拉丁字母段。Noto Serif CJK SC 155 段（核心 116 段，差额为韩语注记与 U+3000 分隔符所在段）；DejaVu Sans 4 段为 P7 ✗ 标记。

## 结论

机械门 14/14 + freeze 8/8 + 确定性 8/8 + creambox 全版无真溢出 + 目视/手验均通过，**零缺陷**，故结论 **(a) 定稿**。记录项 R1（Q148）转 core 轨道、R2（D5）待用户定夺 scope，均不影响本版定稿。
