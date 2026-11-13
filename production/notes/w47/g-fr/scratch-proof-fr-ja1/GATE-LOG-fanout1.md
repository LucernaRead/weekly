# GATE-LOG — W47 fr-ja proof1（独立复跑）

- 时间：2026-11-11 07:48–08:05 EST；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR：goals 侧 `hidden_files/w47/scratch-proof-fr-ja1/tmp`（未用 /tmp）。
- 探针：`/dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通（`9daeafb9…`）；goals 侧写文件探针通。开工前磁盘 SHA 已核对（见 PROOF-NOTE，与任务书完全一致）；复核后复测，core-fr 三件 SHA 未变。
- 复跑脚本：同目录 `proof_gates.py`（逐门复刻 builder `gates.py`，适配 ja：build-run1.log、fr-ja 文件名；新增第 16 门 cjk_classify；结果写本目录；**未在生产目录重跑构建**——确定性门改为沙盒副本重建）。
- 注：core-fr 无 `check_core.py`（ru/pt 系有）；fr 系等效覆盖 = freeze diff + source/string freeze + 确定性重建，均已跑并通过。

## 1. freeze 首检（任务指定先跑）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-ja/svg` → rc=0，**8/8 页**：
p1 +23/-23、CJK 224→270、净增 196；p2 +35/-33、净增 264；p3 +31/-32、净增 174；p4 +40/-38、净增 221；
p5 +37/-34、净增 210；p6 +27/-28、净增 162；p7 +34/-34、净增 303；p8 +120/-122、净增 802。**净增 CJK 合计 2,332。**
`--strict-cjk` rc=1 属预期（ja 为读者语、核心本身含 CJK；strict 门只适用 ja 目标）；新增串毛数 3,445 / 431 不同字，cjk_classify 门逐一核对全部入账（见 §2）。
（日志 `freeze-diff.log` / `freeze-diff.json` 为 strict 版，`freeze-diff-nostrict.log` / `freeze-diff-nostrict.json` 为非 strict 版）

## 2. 独立门禁 15/15 PASS（`gates-proof1.json`）

| 门 | 结果 |
|---|---|
| run（builder build-run1.log 读检） | PASS：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150，A2 53 / B1 75 / B2 22，by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion（`tools/occlusion_audit.py`） | PASS：0 flags，selftest OK（`occlusion-proof1.json`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys 150/150，printed notes 121/150（`p8-proof1.json`） |
| p8_compare（vs core P8 SVG） | PASS：CLEAN，keydiff [150]（writing key only）（`p8compare-proof1.json`） |
| source_freeze | PASS：content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name |
| string_freeze | PASS：all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values |
| text_layer | PASS：print/web pdftotext byte-equal (102,274 B); web 2,310,518 B < 7MB; print 30,566,551 B（`print-proof1.txt` / `web-proof1.txt`） |
| p8_font | PASS：P8 min font 11.625pt >= 9.75pt |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，old paper=0，#fbfaf6 x8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck（vs `core-fr/final-fr-p8.json`） | PASS：150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted |
| mcq（`check_mcq.py`） | PASS：bodies 45，rendered lines 1454，DEFECTS: 0，UNLOCATED: 0（`mcq-proof1.log`） |
| widths | PASS：31 single-line strings all within budget；4 组共行对均 ≤1757 |
| band_spans（印刷 PDF span 实测） | PASS：FR title ends 1236.9，band_r1 starts 1380.0，FR sub ends 837.2，band_r2 starts 1430.1 |
| cjk_classify（新增门） | PASS：added CJK total 3445 (431 distinct): U+3000=289, cjk_punct=105, fullwidth=337, hiragana=730, kanji=1298, katakana=686; unaccounted distinct 0 |

## 3. 确定性（沙盒副本重建，替代 gates 第 7 门）

版目录完整拷贝至本目录 `rebuild/ed/`（副本已删），删 svg 后重跑 `run.py`（rc=0，TOTAL 150，类型分布与 builder 一致），8 个 SVG sha256 与在版文件**逐字节一致 8/8**：
`8bf58ae5 / db490888 / 83ad866a / 8252ca19 / cae84c75 / 7fdd8932 / 7a37897c / 66b5fa78`（与 builder `freeze_direct` 记录的哈希逐一相同；日志 `rebuild-run.log`）。

## 4. creambox 规范扫描（`hidden_files/w47/tools/creambox.py`，日志 `creambox-proof1.log`）

- 33 盒。7 条 naive `clearance -` 行全部判定为**下一节标题误报**（BELOW-WINDOW +24.0/+37.0，下一节标题首行；inside-only 清除全部为正，P1 +48.0 / P2 +47.7 / P3 +47.7 / P4 +47.7 / P5 +47.7 / P6 +48.5 / P7-TOOLBOX 最小 +24.7、desc-clear +18.8）。
- **P7 读者园地盒（本人独立实测，非采信跨版目测）**：盒 `x=989.0 y=1878 w=873.0 h=380`，盒底 2258.0；盒内末行基线 2233.3（`る。VOL.5で実際の投稿の講評という約束を果たす。`，19.5pt）；
  PIL 真墨实测（`cards/p7-langue.png` 1:1）：奶油底边 PNG y=2257，末行真墨至 y=2234，净边距 23px；基线 (2233.4, 2310) 内无任何文本；深绿带起于 y≈2270。
  **裁定：不溢出，干净。**（日志 `p7-measure.log`，裁切图 `png/p7-courier.png`）

## 5. 孤儿句号三处（目视确认的唯一未过项；SVG 实测 + 全分辨率裁切图）

全 8 页 SVG 扫描独行标点：仅三处 lone `。`（P1 y=1366.65 / P4 y=1722.92 / P6 y=1941.225，均为 20.5pt）；
core-fr 同类仅一处、不同位置（P4 y=550.53，中文串）。详见 PROOF-NOTE 缺陷清单 D1–D3（裁切图 `png/p1-gloss.png`、`png/p4-comp.png`、`png/p6-cal.png`）。

## 6. 目视与内容手验

- 8 页逐页目视（印刷 PDF 150 dpi，`png/p1.png`–`p8.png` + 缩览 `png/v1.png`–`v8.png`）：除 D1–D3 外零问题；P1 band 无重叠（裁切 `png/p1-band.png`）。
- 网页 PDF 抽查（`png/web1.png`、`png/web7.png`，100 dpi）：与印刷版布局、图片一致；D1 在网页版同样可见。
- 150 题逐题手验（`keycheck3.log` / `keycheck3b.log`；`.text.md` 1,087 行全文通读）：text.md 答案 == P8 抽取键 150/150；
  核心键 vs 本版键仅 Q150 不同；Q148 见 PROOF-NOTE R1（只记录）；零中文残留（`来/会/去/由` 14 处逐字核对，均为标准日语用法）。
- D5 字体普查（`d5-font.log`）：本版 CJK 字体中纯拉丁 576 段 vs 核心 560 段（+16），主体为核心继承；只记录，不判 (b)。
- `"next Sunday"` 冻结核心规则：本版未见该类问题。

## 结论

机械门 15/15 + freeze 8/8 + 确定性 8/8 + 目视/手验均通过，**唯一未过项为 D1–D3（三处孤儿句号「。」独占一行）**，
故结论 **(b) 不定稿**，修复三串后重跑全套门禁 + P1/P4/P6 重验。
