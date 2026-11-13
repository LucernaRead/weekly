# GATE-LOG — W47 fr-zh-tw proof1（独立复跑）

- 时间：2026-11-11 12:48–14:20 EST；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR：goals 侧 `hidden_files/w47/scratch/tmp`（未用 /tmp）。
- 探针：`/dev/null` 存在（`-rw-rw----`，12:48）；`git hash-object -w` 通（rc=0）；goals 侧写文件探针通。开工前磁盘 SHA 已核对（见 PROOF-NOTE，与任务书完全一致）；收工后三件 SHA 复测一致，核心三件 SHA 复测一致，生产文件未动。
- 复跑脚本：同目录 `proof_gates.py`（逐门复刻 builder `gates.py`，但结果写本目录；**未在生产目录重跑构建**——确定性门改为沙盒副本重建）。
- 注：core-fr 无 `check_core.py`（ru/pt 系有）；fr 系等效覆盖 = freeze diff + source/string freeze + 确定性重建，均已跑并通过。

## 1. freeze 首检（任务指定先跑）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-zh-tw/svg` → rc=0，**8/8 页**（日志 `freeze-diff.log` / `freeze-diff.json`）：

| 页 | +/− 串 | 新增 CJK 字符数（去重后异体字） |
|---|---|---|
| p1 | +21/−22 | 79 |
| p2 | +29/−28 | 94 |
| p3 | +23/−23 | 57 |
| p4 | +32/−32 | 89 |
| p5 | +30/−30 | 76 |
| p6 | +22/−24 | 79（含 U+3000 ×1） |
| p7 | +32/−32 | 139 |
| p8 | +99/−106 | 363（含 U+3000 ×10） |
| **合计** | | **976 字符 / 256 异体字** |

新增 CJK 逐字分类（`classify_cjk.py`，`cjk-added-classification.json`）：
- 255 异体字 ∈ 本版 `expl.py` 繁体讲解层值（其中繁体专有字 179、两岸同形字 76）；**U+3000 结构空格 1 字（11 次）**；未入账 0；核心独有 0。
- 新增集中简体字：**0**。但全文件简繁扫描另见 D1（见 §1b）——`准`未进新增集，因核心已有 3 处、本版 2 处（数量减少），属核心简体字被带入译文。

### 1b. 简体残留逐字核对（opencc s2t 全扫）

对 8 页 SVG + `expl.py` + `.text.md` 全部 CJK 字逐字 `s2t(ch) != ch` 判定：
- **唯一简体字：`准`**（`simplified-residue.json`）。
  - `expl.py:120`（zoom_note）、`:230`（n_vf1），各 1 次；`svg/p3-culture.svg` 1 次、`svg/p8-exercices.svg` 1 次；`.text.md:419`、`:1063`，各 1 次。
  - 词「獲准」→ 正体「獲準」。此为 **D1**，见 PROOF-NOTE。
- 其余全部 CJK 字：繁体专有字或两岸同形字，无简体残留。Builder 启发式简体集（为/说/学/发/头/让/认/识/读/听/传/统/华/实/质/义/习/会/还/买/卖/费/贵/动/对/应/开/车/马/门/问/边/过/达/迟/选/际/东/进/远/连/这）未含 `准`，故漏网。
- SVG 内 CJK 字不在 `expl.py` 值内：**0**（与 string_freeze 一致）。

## 2. 独立门禁 14/14 PASS（`gates-proof1.json`）

| 门 | 结果 |
|---|---|
| run（builder build-run2.log 读检） | PASS：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE；TOTAL 150，A2 53 / B1 75 / B2 22，by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion（`tools/occlusion_audit.py`） | PASS：0 flags，selftest OK（`occlusion-proof1.json`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys 150/150，printed notes 121/150（`p8-proof1.json`） |
| p8_compare（vs core P8 SVG；直接读 `p8compare-proof1.json`，未用 gates.json 的 "?" 误读） | PASS：CLEAN，keydiff [150]（writing key only） |
| source_freeze | PASS：content*.py / bslib4.py / svglib.py / run.py 与核心字节相同；render.py 仅 BASE+PDF 名差异 |
| string_freeze | PASS：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| text_layer | PASS：印/网 pdftotext 逐字节一致（101,806 B）；web 2,558,076 B < 7MB；print 30,551,968 B（`print-proof1.txt` / `web-proof1.txt`） |
| p8_font | PASS：P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（vs `core-fr/final-fr-p8.json`） | PASS：150 键仅 Q150 不同（`開放題` vs 核心 `开放题`），核心 150 键 / 抽取 150 键 |
| mcq（`check_mcq.py`） | PASS：bodies 45，rendered lines 1445，DEFECTS: 0，UNLOCATED: 0（`mcq-proof1.log`） |
| widths | PASS：31 单行串全部在预算内；4 组共行对均 ≤1757 |
| band_spans（印刷 PDF span 实测，1920 单位口径） | PASS：FR title ends 1236.9，band_r1 starts 1405.0，FR sub ends 837.2，band_r2 starts 1571.4（真 SVG 单位见 §7：1256.2 / 1427.0 / 净空 170.7，结论不变） |

## 3. 确定性（沙盒副本重建，替代 gates 第 7 门）

版目录完整拷贝至本目录 `rebuild/ed/`（副本已删），删 svg 后重跑 `run.py`（rc=0，TOTAL 150，类型分布与 builder 一致：完成句子 49、单选 26、句型转换 7、词汇配对 21、阅读判断 5、图表读数 6、跟练 8、改错 4、完形填空 8、阅读理解 5、翻译 5、对话补全 5、写作 1），8 个 SVG sha256 与在版文件**逐字节一致 8/8**：`bc9050c8 / 7e372c72 / f3280832 / 5af79c73 / a1981b77 / 81a3f8ff / 087855db / 86da3308`（与 builder `freeze_direct` 记录的哈希逐一相同）。

## 4. creambox 规范扫描（`hidden_files/w47/tools/creambox.py`，日志 `creambox-proof1.log`）

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；inside-only 清除全部为正）。
- **P7 盒 `y=1878 bottom=2258.0`（本复校独立实测裁定，见 PROOF-NOTE）**：naive 行即 `last baseline 2233.3 clearance +24.7`；per-line 表：披露段 2 行（2206.0 / 2233.3），无 BELOW-WINDOW 行；P7-TOOLBOX 汇总：4 盒，最小盒内清除 +24.7，最小 desc-clear +18.8。
- PIL 真墨测量（印刷 PDF 300 dpi，真 SVG 坐标）：奶油底边 svg y≈2257.5；末行真墨至 svg y≈2235，**盒内余白约 23px**；深绿带起于 svg y=2270.0。**P7 干净，无溢出。**
- 其余各页盒内最小清除量均为正（P1 +48.0 / P2 +47.7 / P3 +47.7 / P4 +47.7 / P5 +47.7 / P6 +48.5 量级；详见日志）。

## 5. 奶油盒右缘与丢空格扫描（`extra_scans*.py`）

- 右缘（已裁决规则）：中心落在盒内、字形越盒右缘的 span **0**（`right-edge-scan.json`；初版误报为未要求 span 中心在盒内，已修正重跑）。
- 丢空格（ru 教训类）：同基线相邻 span 对 678 组，字-字紧邻（间隙 <2 svg 单位）**0**；61 组间隙 <5 均为箭头 `→` / `___` / 前导空格 span 的 bbox 修边，SVG 坐标与核心同位，**无丢空格**（`gap-scan.json`）。

## 6. 目视与内容手验

- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png`）：除 D1（P3/P8 `准` 字肉眼不可辨字形、凭 SVG 文本核定）、D2（P2×2、P3×1 孤字 `。` 目视可见）外零问题；P1 band 无重叠；各页无溢出/遮挡/截断。
- 网页 PDF 抽查（`png/web-p1.png`、`web-p7.png`，100 dpi）：与印刷版布局、图片一致。
- 150 题逐题手验（`.text.md` 1,087 行全文通读 + 三源交叉 `q150-crosscheck.json`）：150/150 一致，仅 Q150 不同；答案区 150 条全解析、0 缺失；带注记答案 121 条，与 P8 抽取注记数一致。仅 R1（Q148 核心继承错法语）与 R2（D5 字体）两项记录，见 PROOF-NOTE。
- 行首标点全扫：孤字 `。` 共 4 处——P2×2、P3×1 为本版新增（D2）；P4×1 与核心同位（观察 O1）。P7 行首 `；`、P8 行首 `）` 均与核心同位（观察 O2）。
- D5 字体普查（`d5-font-census.json` / `d5-diff.json`）：Newsreader 931、Noto Sans CJK SC 657、Noto Serif CJK SC 62、DejaVu Sans 4、UnifrakturMaguntia 1；CJK 字体 719 段中纯拉丁 362 段（核心 723/361）；本版仅多 1 段 `CLINIQUE DES ERREURS`（双语标题按字体拆 run，非新增内容）。
- 「next Sunday」核查：本版与核心盘上全文搜 0 次，任务书记载行号已过期，无可判项。

## 7. 口径校准说明（非缺陷）

- SVG 实为 **1950×2700**（`width="1950" height="2700" viewBox="0 0 1950 2700"`），而 `gates.py` / `proof_gates.py` 的 band_spans 门与本复校初版 PIL 测量均误用 1920 宽换算。真值 = 读数 ×(1950/1920)=×1.015625：FR title ends 真值 1256.2、band_r1 starts 真值 1427.0、净空真值 170.7（读数 168.1）；P7 奶油底边真值 2258.0、末基线真值 2233.3、绿带顶真值 2270.0——与 SVG 坐标逐一吻合。门禁本身自洽（冻结参照 1236.9 亦为同口径读数），结论不变；本日志 §4 的 P7 真墨值已按真坐标重测。
- 初版 PIL 测量因该口径误读曾报出矛盾剖面（绿带提前），已用 fitz 矢量 rect（奶油 rect 真值 1878.0..2258.0、绿带 rect 真值 2270.0..2560.0）与真坐标重测纠正，不采信初版数字。

## 结论

机械门 14/14 + freeze 8/8 + 确定性 8/8 + creambox 33 盒 + 三源交叉 150/150 均通过，**未过项为 D1（简体残留 `准`，2 值 4 文件）与 D2（行首孤字 `。`，3 处）**，故结论 **(b) 不定稿**，修复 D1+D2 后重跑全套门禁 + P7/P3/P8/text.md 重验。
