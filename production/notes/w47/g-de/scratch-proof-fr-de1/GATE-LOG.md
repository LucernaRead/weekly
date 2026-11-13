# GATE-LOG — W47 fr-de proof1（独立复跑）

- 时间：2026-11-11 12:32–13:00 EST；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR：goals 侧 `hidden_files/w47/scratch/tmp`（未用 /tmp）。
- 探针：`/dev/null` 缺失→已垫回（`touch /dev/null` 后 `git hash-object -w` 通，rc=0）；goals 侧写文件探针通。开工前磁盘 SHA 已核对（见 PROOF-NOTE，与任务书完全一致）。
- 复跑脚本：同目录 `proof_gates.py`（逐门复刻 builder `gates.py`，但结果写本目录；**未在生产目录重跑构建**——确定性门改为沙盒副本重建）。
- 注：core-fr 无 `check_core.py`（ru/pt 系有）；fr 系等效覆盖 = freeze diff + source/string freeze + 确定性重建，均已跑并通过。

## 1. freeze 首检（任务指定先跑）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-de/svg` → rc=0，**8/8 页**：
p1 +26/-23、CJK 224→36、新增 1（U+3000）；p2 +39/-33，新增 0；p3 +35/-44，新增 1（U+3000）；p4 +46/-50，新增 1（U+3000）；p5 +38/-42，新增 1（U+3000）；p6 +31/-30，新增 2（U+3000）；p7 +44/-34，新增 1（U+3000）；p8 +124/-123，新增 0。**新增 CJK 字符合计 7，全部为结构全角空格 U+3000，无新增 CJK 文字。**（日志 `freeze-diff.log` / `freeze-diff.json`）

## 2. 独立门禁 14/14 PASS（`gates-proof1.json`）

| 门 | 结果 |
|---|---|
| run（builder build-run4.log 读检） | PASS：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE；TOTAL 150，A2 53 / B1 75 / B2 22，by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion（`tools/occlusion_audit.py`） | PASS：0 flags，selftest OK（`occlusion-proof1.json`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys 150/150，printed notes 121/150（`p8-proof1.json`） |
| p8_compare（vs core P8 SVG） | PASS：CLEAN，keydiff [150]（writing key only）（`p8compare-proof1.json`） |
| source_freeze | PASS：content*.py / bslib4.py / svglib.py / run.py 与核心字节相同；render.py 仅 BASE+PDF 名差异 |
| string_freeze | PASS：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免 |
| text_layer | PASS：印/网 pdftotext 逐字节一致（104,794 B）；web 1,704,484 B < 7MB；print 17,424,274 B（`print-proof1.txt` / `web-proof1.txt`） |
| p8_font | PASS：P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（vs `core-fr/final-fr-p8.json`） | PASS：150 键仅 Q150 不同，核心 150 键 / 抽取 150 键 |
| mcq（`check_mcq.py`） | PASS：bodies 45，rendered lines 1486，DEFECTS: 0，UNLOCATED: 0（`mcq-proof1.log`） |
| widths | PASS：31 单行串全部在预算内；4 组共行对均 ≤1757 |
| band_spans（印刷 PDF span 实测） | PASS：FR title ends 1236.9，band_r1 starts 1337.5，FR sub ends 837.2，band_r2 starts 1417.5 |

## 3. 确定性（沙盒副本重建，替代 gates 第 7 门）

版目录完整拷贝至本目录 `rebuild/ed/`（副本已删），删 svg 后重跑 `run.py`（rc=0，TOTAL 150，类型分布与 builder 一致），8 个 SVG sha256 与在版文件**逐字节一致 8/8**：`35c72f4e / 38a1a6fc / 93a010c3 / cd216538 / 32c60e8a / 083360a7 / 4bc0ef75 / 7e3269a2`（与 builder `freeze_direct` 记录的哈希逐一相同）。

## 4. creambox 规范扫描（`hidden_files/w47/tools/creambox.py`，日志 `creambox-proof1.log`）

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；inside-only 清除全部为正，P1 +48.0 / P2 +47.7 / P3 +47.7 / P4 +47.7 / P5 +47.7 / P6 +48.5 / P7-TOOLBOX 最小 +24.7、desc-clear +18.8）。
- **1 处真溢出（D1，见 PROOF-NOTE）**：P7 盒 `y=1878 bottom=2258.0`，naive 行 `last baseline 2260.6 clearance -2.6`；per-line 表：inside-only 末基线 2233.3（+24.7），BELOW-WINDOW 行 +2.6 为同段续行 "echte Einsendungen zu kommentieren."（同 x=1013、同 19.5pt、行距 27.3，段内第 3 行），非下一标题。核心同盒末基线 2233.3（+24.7）；同盒同溢出亦见于 es/it/pt/nl/ru（-2.6），en/ja/ko/zh-tw 为 +24.7。
- PIL 真墨测量（印刷 PDF 300 dpi，见 PROOF-NOTE）：奶油底边 svg y≈2257.5，该行真墨至 svg y≈2265，**约 7.5px 真墨出盒**；深绿带起于 svg y≈2270。

## 5. 目视与内容手验

- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png`）：除 D1 外零问题；P1 band 无重叠；各页无溢出/遮挡/截断。
- 网页 PDF 抽查（`png/web-p1.png`、`web-p7.png`，100 dpi）：与印刷版布局、图片一致；P7 溢出在网页版同样存在。
- 150 题逐题手验（`.text.md` 1,089 行全文通读）：150 键全部正确；Q64 "Lukas Dhont" 已核；仅 R1（Q148 核心继承错法语）与 R2（D5 字体）两项记录，见 PROOF-NOTE。
- D5 字体普查：Noto Sans CJK SC 696 段中 423 段为纯拉丁文（德语讲解层）；核心对照 100 段。Noto Serif CJK SC 74 段全为 U+3000 分隔符；DejaVu Sans 4 段为 P7 ✗ 标记。

## 结论

机械门 14/14 + freeze 8/8 + 确定性 8/8 + 目视/手验均通过，**唯一未过项为 D1（P7 奶油盒溢出，7.5px 真墨）**，故结论 **(b) 不定稿**，修复 D1 后重跑全套门禁 + P7 重验。
