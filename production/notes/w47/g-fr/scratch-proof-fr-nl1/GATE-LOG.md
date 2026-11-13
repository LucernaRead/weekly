# GATE-LOG — W47 fr-nl proof1（独立复校自复跑）

- 版：`production/2026-w47/2026-w47-fr-nl/`；复校时间 2026-11-11
- 解释器：一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；
  只有 creambox 用系统 python3（纯标准库，按其 README）。
- TMPDIR：本工作目录下 `tmp/`。生产文件只读；复建均在 scratch 副本上进行。

## 0. 探针与身份核对

- `ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  通（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）；goals 侧写文件成功。
- 磁盘 SHA（开工前与收工后两次一致）：
  印刷 `dc253f3a62dd312368b81ea3e75c45b503fa31675bdad69d09fbfd0661d89cd0`（17,418,864 B）
  网页 `9af15b3f47eba19e95882aced708fee59b295f8dd4555ebbea037da5c17be3a4`（1,699,797 B）
  text `acc84a72d786ab46009f2e0676906e919f055b1ad1293915dab37a116eefaac5`（46,338 B，
  磁盘实名 `2026-w47-fr-nl.text.md`）——与任务所给三 SHA 全对。

## 1. freeze 首检（`tools/freeze.py diff`）

命令：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg
--edition-svg production/2026-w47/2026-w47-fr-nl/svg --json <scratch>/freeze-diff.json`
结果：exit 0，8 页全处理。

| 页 | +串 / −串 | CJK 核心→本版 | 新增 CJK |
|---|---|---|---|
| p1 | +26 / −23 | 224 → 35 | 0 |
| p2 | +38 / −33 | 283 → 33 | 0 |
| p3 | +37 / −44 | 194 → 18 | 0 |
| p4 | +44 / −50 | 238 → 28 | 0 |
| p5 | +40 / −42 | 244 → 22 | 0 |
| p6 | +30 / −30 | 226 → 24 | 0 |
| p7 | +38 / −34 | 411 → 14 | 0 |
| p8 | +125 / −123 | 1220 → 190 | 8 × U+3000 |

说明：新增 CJK 仅 P8 的 U+3000 ×8。该字符为两段式导读条 / P8 答案流的结构分隔空白
（gates.py 的 `norm()` 亦将其归一为空白），非中文文本；其余 7 页新增 CJK 为 0。
新增串均为荷兰文，移除串均为中文——符合 fan-out 预期。

## 2. freeze baseline（确定性复建，scratch 副本）

命令：`tools/freeze.py baseline --build production/2026-w47/2026-w47-fr-nl
--core-svg production/2026-w47/2026-w47-fr-nl/svg --out <scratch>/freeze-baseline-ed`
结果：**8/8 SVGs byte-identical，rc=0**。哈希与 builder 的 freeze_direct 逐一相同：
`984a2867, 1f619509, 4ef160c4, c9b59871, f2342e2a, ce2141d5, 037b5c49, 6a9750ef`。
附带：core integrity——出厂核心 SVG 复核未变（8 文件重哈希）。
注：首次误以 `--core-svg core-fr/svg` 跑 baseline 得 0/8——为比较目标错配
（法文版重建结果与中文核心 SVG 本就不同），不作门禁结论；重跑正确目标后 8/8。

## 3. 构建日志（builder run2，读）

`nl/build-run2.log`：`run.py exit 0`；`TOTAL 150`；`P8 saved, TOTAL exercises: 150`；
`export_lang.py exit 0`；text.md 44259 字符 / 542 entries / 150 exercises；
零 `FLOW OVERFLOW` / `HEAD TOO WIDE`。`!! P7 DORE NOSPACE: y0= 1016` 为已知 stub
假象（gates.py 注明排除；真实构建 Dore 落于 y0=871.16）。

## 4. occlusion（`tools/occlusion_audit.py`）

命令：`occlusion_audit.py --json occlusion-proof1.json svg/`（版目录下）
结果：**0 flags，rc=0**；selftest OK（planted classes fired
BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1；clean controls silent）。

## 5. p8（`tools/p8.py`，--total 150）

- extract：keys **150/150**，printed notes **121/150**，rc=0（`p8-proof1.json`）。
- compare（vs `core-fr/svg/p8-exercices.svg`）：**CLEAN**，missing=[]，extra_count=0，
  uncertain=[]，**keydiff=[150]**，rc=0（`p8compare-proof1.json`）。

## 6. source freeze（字节比对）

`bslib4.py / content12.py / content34.py / content56.py / content7.py / content8.py /
svglib.py / run.py` 与 core-fr **全部字节相同**；`render.py` 差异仅 2 行：
`BASE` 与 PDF 名（`core-fr` → `2026-w47-fr-nl`，`La-Lucerna-VOL4.pdf` →
`La-Lucerna-VOL4-fr-nl.pdf`）。PASS。

## 7. string freeze（gates.py 逻辑原样复跑，`verify_gates.py`）

**PASS**：全部非 CJK 核心串按页存活；核心 E（中文）串存活 0；未入账 CJK 字符 0；
1 串以翻译 E 值豁免（核心版 stem_e1 前缀 `Traduisez : `，与 builder 报告一致）。

## 8. 文字层（pdftotext -layout）

印刷版与网页版 pdftotext **逐字节一致，105,398 B**；均为 8 页，
页尺寸 1462.5 x 2025 pts；网页版 1,699,797 B < 7 MB。PASS（`print.txt` / `web.txt`）。

## 9. P8 字号（PyMuPDF，venv）

P8 字号集合 `[11.625, 12.75, 13.5, 14.25, 14.625, 15.0, 15.375, 15.75, 16.125,
17.25, 18.0, 18.75, 19.5, 34.5]`，**最小 11.625pt ≥ 9.75pt**。各页最小：
p1 11.625 / p2 11.625 / p3 11.625 / p4 12.750 / p5 11.625 / p6 12.750 /
p7 11.625 / p8 11.625。PASS。

## 10. 扫描（SVG 全文计数）

U+2019 = 0；U+00B7 = 0；金色值 `#b49a4a` = 0；旧纸色 `#f7f1e2` = 0；
纸色 `#fbfaf6` ×8。PASS。
注：原始 `grep gold` 4 命中均为 base64 嵌入图数据内子串（`...FqGolDPq...` 等），
非文字；按门禁口径（`#b49a4a` 计数）为 0。

## 11. chips

白字计数 `fill="#ffffff"`：**134，共 [10, 12, 18, 15, 14, 15, 12, 38]**，
与期望一致。PASS。

## 12. keycheck（vs `core-fr/final-fr-p8.json`）

150 核心键 vs 150 提取键，**仅 Q150 不同**（写作键 `开放题` → `Open vraag`）。PASS。

## 13. MCQ（`scratch-fanout-fr/check_mcq.py .`）

**DEFECTS: 0，UNLOCATED: 0**，rc=0；bodies 45，rendered lines 1481。PASS（`mcq-proof1.log`）。

## 14. widths（31 单行串，svglib.text_w）

31/31 在预算内；4 组共行配对（head_quiz+quiz_sub、head_date+date_sub、
head_p2ex+p2ex_sub、head_phrases+phrases_sub）均 ≤1757。PASS。

## 15. band_spans（印刷版 PDF span，PyMuPDF，gates.py 第 15 门原样）

FR title ends **1236.9**（门限 1230–1245）✓；**band_r1 starts 1329.4**（≥1252）✓；
FR sub ends **837.2**；**band_r2 starts 1457.5**（≥950）✓。PASS。
（口径：`_sx = 1920.0 / rect.width`；按基线配对行，非 bbox 顶边。）

## 16. creambox 规范版（`hidden_files/w47/tools/creambox.py`，8 页全扫）

命令：`python3 tools/creambox.py svg/*.svg`，rc=0（`creambox-proof1.log`）。
负 clearance 8 处，逐项裁决：

| # | 页 / 盒 | clearance | inside-only | 裁决 |
|---|---|---|---|---|
| 1 | P1 y=1280（DANS CE NUMÉRO 盒） | −24.0，末行 `LE MOT DE LA SEMAINE` | +48.0（末行 `p.8`） | 假阳性：盒下标题落入 +45px 窗口（BELOW-WINDOW +24.0） |
| 2 | P2 y=886（Uitleg 盒） | −37.0，末行 `LA SEMAINE EN CHIFFRES` | +47.7 | 假阳性（BELOW-WINDOW +37.0） |
| 3 | P3 y=200（Uitleg 盒） | −37.0，末行 `À VOUS !　JOUW BEURT!` | +47.7 | 假阳性（BELOW-WINDOW +37.0） |
| 4 | P4 y=200（Uitleg 盒） | −37.0，末行 `À VOUS !　JOUW BEURT!` | +47.7 | 假阳性（BELOW-WINDOW +37.0） |
| 5 | P5 y=2182（Uitleg 盒） | −37.0，末行 `À VOUS !　JOUW BEURT!` | +47.7 | 假阳性（BELOW-WINDOW +37.0） |
| 6 | P6 y=463（LES PHRASES DES JOURNAUX 盒） | −37.0，末行 `IL EST PRÉVU QUE + SUBJONCTIF` | +48.5 | 假阳性（BELOW-WINDOW +37.0） |
| 7 | P6 y=1330（LE DÉBAT 盒） | −37.0，末行 `LE DÉBAT　DEBAT` | +48.5 | 假阳性（BELOW-WINDOW +37.0） |
| 8 | **P7 y=1878（LE COURRIER DES LECTEURS 盒）** | **−2.6，末行 `belofte in om echte inzendingen te bespreken`** | **+24.7（末行 `daarom drukken we een duidelijk gemarkeerd v…`）** | **真缺陷 D1**：末行为盒内段落续行（同段第 3 行），其字墨切过盒底，见 PROOF-NOTE.md |

另：P7-TOOLBOX 汇总 4 盒，最小盒内余量 +24.7，最小 desc-clear +18.8。
其余全部盒 clearance 均为正。

## 汇总

| 门 | 结果 |
|---|---|
| 身份 SHA（三文件） | PASS |
| freeze diff（8 页） | PASS（exit 0；新增 CJK 仅 U+3000×8 结构空白） |
| freeze baseline（复建） | PASS 8/8 |
| build 日志 | PASS（exit 0，TOTAL 150，零溢出） |
| occlusion | PASS 0 flags |
| p8 extract / compare | PASS 150/150，注记 121/150，CLEAN，keydiff [150] |
| source freeze | PASS |
| string freeze | PASS |
| 文字层 print/web | PASS 逐字节一致 105,398 B |
| P8 字号 | PASS 最小 11.625pt |
| 扫描 | PASS（U+2019/U+00B7/金色/旧纸色 均为 0） |
| chips | PASS 134 [10,12,18,15,14,15,12,38] |
| keycheck | PASS 仅 Q150 不同 |
| MCQ | PASS 0 缺陷（45 体 / 1481 行） |
| widths | PASS 31/31 |
| band_spans | PASS（1236.9 / 1329.4 / 837.2 / 1457.5） |
| creambox | **1 真缺陷（D1，P7），其余 7 负值为假阳性** |

**机械门 15/15 通过；唯一未过项为 creambox 发现的目视/几何缺陷 D1。**
结论见 `PROOF-NOTE.md`：(b) 有缺陷，不定稿。
