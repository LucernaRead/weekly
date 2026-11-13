# GATE-LOG — W47 fr-ko proof1（re-fanout #2 版，独立复跑）

- 时间：2026-11-11 17:40–18:10 EST；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3；ko-reader 版用 venv，freeze guard 要求非 ko-target 路径 Pillow 13——本版是 fr-ko 读者版，非 ko-target 版，适用 venv）。
- 探针：开工前三 SHA 与任务书完全一致（见 PROOF-NOTE），复校结束再次复测未变；生产 SVG 哈希复测与开工记录一致（`rebuild/shipped-svg.sha256`）。
- 复跑脚本：同目录 `proof_gates2.py`（14 门，逐门复刻构建方 gates 方法，路径与输出名改为本轮 proof2；结果写本目录；**未在生产目录重跑构建**——确定性门改为 scratch 副本重建）。另有自写 fr-ko 适配脚本：`boxtitle_creambox.py`（盒标题+奶油盒 PIL 真墨）、`check_extra2.py`（孤儿+空行+Q148）、`cjk_inventory.py`（新增 CJK 全量分类）、`triple_check.py`（150 键三重交叉）、`p7_measure.py` / `p7_measure2.py`（P7 披露盒 300 dpi 渲染像素）。
- 注：上一轮（#1 版）文件已封存于 `prev-round-#1/`；本文件全部数字均为针对 #2 新版的独立重测。

## 0. 身份核对（先于一切）

| 件 | 实测 |
|---|---|
| 印 `La-Lucerna-VOL4-fr-ko.pdf` | 23,103,425 B，`a315cced…f3c82` ✓ 与任务书一致 |
| 网 `La-Lucerna-VOL4-fr-ko-web.pdf` | 2,048,869 B，`0862b544…ebd5` ✓ |
| 文 `2026-w47-fr-ko.text.md` | 47,323 B，`f5474d61…ba5c37` ✓ |
| 核心 fix4 印 / 网 / 文 | 30,446,975 B `a30af667…25a9d` / 2,241,835 B `56f50ca8…6d58e141` / 46,471 B `52024e02…63df` ✓（复核前后各测一次，未变） |

## 1. freeze 首检（任务指定先跑）

`tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-ko/svg` → rc=0，**8/8 页**（日志 `freeze-diff.log` / `freeze-diff.json`）：
p1 +26/-23，新增 188；p2 +35/-33，新增 300；p3 +37/-34，新增 168；p4 +56/-39，新增 208；p5 +47/-34，新增 216；p6 +43/-28，新增 172；p7 +35/-34，新增 368；p8 +155/-122，新增 944。**新增 CJK 合计 2,564。**

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
| p8 | 944 | 924 | 14 | 6（3 对） | 0 |
| **合计** | **2,564** | **2,538** | **17** | **8（4 对）** | **0** |

- 韩文音节 2,538：全部为韩语讲解层（标题译名、词汇注记、练习说明、答案区注记），每个字符均在 `expl.py` 的 E 值字符集内（string_freeze 门亦验 0 未入账）。
- U+3000 ×17：结构全角空格（双语标题分隔），允许。
- 『』×4 对：韩式引号，见于 P5 `LE CINÉMA DU MERCREDI` 韩注（『헝거 게임』）与 P8 答案区注记（『레 브라브』『카망베르』等），为讲解层原文标点，非结构残留。
- 与上一轮差 1 字说明：上一轮 p8 新增 945、合计 2,565；本轮 p8 为 944、合计 2,564。差异为 1 个 U+3000：#1→#2 的 P8 改动（Q148 键 `devant`→`devant le`，+3 拉丁字母）使答案流重排，少用 1 个 U+3000 分隔符。已用新旧 P8 SVG 的 CJK 多重集直接比对证实（#1 1,127 字 → #2 1,126 字，仅差 U+3000 ×1，无其他字符变化）。两轮数字各与其版一致，无矛盾。
- 汉字/假名：版内汉字仅品牌三色蛾 `三` `色` `蛾` 各 ×1（刊头蛾标，与核心同源）；假名 0 个；`Sunday` 0 命中。

## 2. freeze baseline（核心）8/8

`tools/freeze.py baseline --build production/2026-w47/core-fr --core-svg production/2026-w47/core-fr/svg --out <scratch>/freeze-core` → rc=0，**8/8 SVGs byte-identical**：
p1 `6aad8b4b…`、p2 `5709e000…`、p3 `7828cfe3…`、p4 `7e46e630…`、p5 `fff2a8d3…`、p6 `7af7cf3c…`、p7 `75237d67…`、p8 `5bee4d44…`（core 与 produced 逐页相同）；core integrity：shipped core SVGs unchanged by the run（8 文件复哈希）。`--build` 指 core-fr 版目录、`--core-svg` 指 core-fr 的 svg 目录（现行 freeze.py 强制 `--core-svg`）。

## 3. 本版确定性重建 8/8（scratch 副本，绝对路径）

- 副本：`rebuild/ed-copy`（整版复制；重定向目标 `rebuild/run-proof2.log` 绝对路径，运行前核对在 scratch 内；副本已删，哈希与日志保留）。
- `run.py` rc=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE（我的重建日志无 NOSPACE 行；构建方日志第 92 行另有一条已知良性 `P7 DORE NOSPACE: y0= 1016`，出现在 webpdf.py 之后、export_lang.py 退出之前，与 run.py 构建无关，gates 已过滤——我的 run.py 重建不含该步骤，故无此行）；by level A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42}；by type 完成句子 49 / 单选 26 / 句型转换 7 / 词汇配对 21 / 阅读判断 5 / 图表读数 6 / 跟练 8 / 改错 4 / 完形填空 8 / 阅读理解 5 / 翻译 5 / 对话补全 5 / 写作 1。
- 重建 SVG 与出货 SVG **8/8 字节一致**（`rebuild/shipped-svg.sha256` vs `rebuild/rebuilt-svg.sha256`，`diff` 无输出），其中 P8 `fc7999be…` 与 FANOUT-REPORT-fr2.md §4 的 #2 哈希一致。

## 4. 独立门禁 14/14 PASS（`proof_gates2.py` → `gates-proof2.json`）

| 门 | 结果 |
|---|---|
| run（构建方 build-r2run1.log 读检 + 我的重建日志交叉） | PASS：exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150 |
| occlusion（`tools/occlusion_audit.py`） | PASS：**0 flags**，selftest OK（`occlusion-proof2.json`） |
| p8_extract（`tools/p8.py extract --total 150`） | PASS：keys **150/150**，printed notes 121/150（`p8-proof2.json`） |
| p8_compare（vs core P8 SVG） | PASS：**CLEAN**，keydiff **[150]**（writing key only）（`p8compare-proof2.json`） |
| source_freeze | PASS：content*.py / bslib4.py / svglib.py / run.py 与核心字节相同；render.py 仅 BASE+PDF 名差异 |
| string_freeze | PASS：全部非 CJK 核心串按页存活；0 核心 E 残留；0 未入账 CJK；1 串因翻译 E 值豁免（与 de 版同为核心 `stem_e1` 前缀 `Traduisez: `） |
| text_layer | PASS：印/网 pdftotext **逐字节一致（102,735 B）**；web 2,048,869 B < 7 MB；print 23,103,425 B |
| p8_font | PASS：P8 最小字号 **11.625pt ≥ 9.75pt**（SOP §1.1 下限） |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，old paper=0，#fbfaf6 ×8 |
| chips | PASS：134 total [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck | PASS：150 keys vs core：仅 Q150 不同（writing key）；150 core keys，150 extracted |
| mcq（`check_mcq.py`，SOP §1.1 选项不折行） | PASS：bodies 45，rendered lines 1449，**DEFECTS: 0，UNLOCATED: 0**（`mcq-proof2.log`） |
| widths | PASS：31 single-line strings all within budget |
| band_spans（P1 实测 PDF spans） | PASS：FR title ends 1236.9，band_r1 starts 1436.9，FR sub ends 837.2，band_r2 starts 1563.3 |

注：构建方 gates 为 15/15（含 freeze_direct）；本轮 freeze_direct 由 §3 的 scratch 副本重建等效覆盖（8/8 字节一致），故本套为 14/14 + §2 + §3，覆盖无缺口。

## 5. 孤儿 / 空行 / Q148（`check_extra2.py` → `ko/extra-proof2.json`，EXTRA PASS，rc=0）

- 孤儿元素：total 15，**new 0**，inherited 2，remnant 0，shared_baseline 13。
  - 继承 2：P4 y=623.13 x=1007.0 `—`、P6 y=653.69 x=1007.0 `—`（与核心同页同基线同文的行首破折号）。
  - 同基线 13：P4 y=710.69 `—`、P4 y=550.53 `.`、P5 y=933.6 `——`、P5 y=964.13 `.`、P6 y=566.13 `.`、P6 y=653.69 `.`、P6 y=741.25 `.`、P8 y=1439.0 / 246.0 / 332.0 / 418.0 / 504.0 `.`、P8 y=2244.01 `）`——全部为字体分拆的行末/行首标点，与同行实词共享基线（|Δy|<1.5），非视觉孤儿。检测器已在旧版备份上验证检出能力（旧 ja 3 处真孤儿 。仍检出、旧 zh-tw 3 处 。+ P4 残留仍检出——引自 FANOUT-REPORT-fr2.md §5，本轮未放水）。
- 空行填空线：core 与 ko 完全相同 3 条——P3 y=1864.7 x=538.5、P3 y=1997.4 x=538.5、P8 y=843.0 x=989.0，blank_ok=True（Q36/Q37 为 +0 档）。
- Q148：stem_ok=True（P8 SVG 含 `On se retrouve` + `cinéma ?`，不含 `du cinéma`）、key_in_content8=True（`content8.py:170` `"devant le"`、`content8.py:176` `On se retrouve ({gnums[3]})___ cinéma ?`）、extracted=`devant le`。
- 首次运行曾因 `p8-proof2.json` 路径问题报 `extracted=None`（检测器读 `ko/p8-<tag>.json`，而 gates 写在 scratch 根）——这是检测器接线问题，不是版面问题；已修检测器（回退读 scratch 根 `p8-proof2.json`）并重跑，EXTRA PASS。

## 6. 150 键三重交叉（`triple_check.py` → `triple-check.json`）

- text.md 答案解析：**150/150**，missing []。
- 差异：**仅 1 项**——Q150（印出键 `자유 작문` vs 核心 `开放题` vs text.md `자유 작문 — 채점 포인트는 상자 안. 모범 답안은 8면 상자 안（포인트 채점）`），为写作题读者语键，设计内差异。其余 149 题：P8 印出键 = 登记键 = 核心键。
- 手验表 `q150-handcheck.txt`：123 题题干取自 text.md 阅读顺序导出；配对题（Q22–25、Q49–52、Q73–76、Q85–88、Q140–144）与对话题（Q145–149）题干不在行首，改由版面目视 + P8 答案区逐组核对，结论见 PROOF-NOTE。

## 7. 盒标题 + 奶油盒 PIL 真墨全扫（`boxtitle_creambox.py` → `boxtitle-creambox-proof2.log/json`，0 FLAGS）

- 范围：33 个奶油盒（#f0eee5）、27 个盒标题、1,715 个文本 run；方法：每标题按 SVG 标注字族/字号/字重用 PIL getbbox 量真墨（tools/tables.json 字体 + face_index，SCALE=4）；每盒末基线全部 run 取最大真墨底；全部 run 的墨框验页边。
- 结果：**FLAGS 0**。最紧盒标题余量 **+17.25**（P4 `LES PHRASES DU COMMENTATEUR`，墨右 1844.8 vs 框右 1862.0）；最紧奶油盒真墨清除 **+2.4px**（P2 ET VOUS 盒，见 §8）；源 `.box()` 标题最紧余量 +35.3（`LES PHRASES DU COMMENTATEUR` 387.2 vs 最窄盒宽 422.5）；全部 run 墨框在页内（0..1950 × 0..2700）。

## 8. P7 披露盒 + P2 紧盒：交付 PDF 渲染像素复核

- **P7 披露盒**（盒 y=1878.0，底 2258.0，x 989.0..1862.0）：
  - SVG PIL：末基线 2233.3，真墨底 2235.1，清除 +22.9。
  - 交付印刷 PDF 300 dpi 行扫描（`p7_measure2.py`）：末行真墨最后一行 svg y **2234.4**（x 1021.3..1202.1，`투고 평론 약속을 지킨다.`）；2234.4–2269.6 零墨（35.2px 干净白纸）；深绿带 `get_drawings` 实测起于 svg y=2270.0（fill (0.216, 0.251, 0.184)）。真墨清除 **+23.6px**。裁切 `png/p7-box-crop.png` 目视干净。
  - 另：`p7_measure.py` 的 `yb±80px` 窗口法会把 2270 起的绿带顶行误算为末墨 2283.1（清除 −25.1）——窗口 artifact，已用逐行扫描纠正，不采信该数。
- **P2 ET VOUS 盒**（盒 y=973.6，底 1308.6，x 1439.5..1862.0）：SVG PIL 真墨底 1306.2，清除 +2.4px；交付 PDF 300 dpi 行扫描：末墨行 svg y 1305.5，其后至 1320 零墨，渲染清除 **+3.1px**；裁切 `png/p2-tightbox-crop.png` 目视：末行 `어로 두 문장을 써서 보내세요.` 完整在奶油内。注：span em 框底 1309.9（略超盒底 1.3px）为字框度量而非墨，真墨在内，不判溢出。

## 9. D5 字体普查（记录，不修；ET 全量）

- ko：全部 1,804 个 `<text>`；`Newsreader` 983、`Noto Sans CJK SC` 661、`Noto Serif CJK SC` 155、`DejaVu Sans` 4、`UnifrakturMaguntia` 1。CJK 字体段共 816：含 CJK 452、纯拉丁 222、纯数字/标点 125、纯标点/空格 17（其中仅含 CJK 字母者 366，另 86 段为 U+3000/全角符号）。
- core：全部 1,716 个；`Newsreader` 936、`Noto Sans CJK SC` 660、`Noto Serif CJK SC` 115、`DejaVu Sans` 4、`UnifrakturMaguntia` 1。CJK 字体段共 775（414 / 219 / 125 / 17）。
- 差值：+41（+38 含 CJK、+3 纯拉丁）——基本为核心继承常量。

## 10. 目视记录

- 印刷 PDF 110 dpi 全页：`png/p1.png`–`p8.png`，P1–P8 逐页看过，无溢出/重叠/压页脚/豆腐块；页脚 `Le Lucerna　프랑스어 주간지 VOL.4　텍스트는 프랑스어　해설은 한국어` 与 `제 N 면 / 총 8 면` 8 页齐全。
- 网 PDF：`png/web-p1.png`、`web-p7.png`，与印刷版同一版式、无豆腐块；文字层逐字节一致（§4 text_layer）。
- P1 照片内小白方块：与核心 P1 嵌入图逐字节相同（base64 SHA 前 12 位 `ff20bc2bd265` 两边一致）——Atget 原片里的店招，核心继承，非本版缺陷。
- `ABSTRACT.txt`：韩文单行 250 B，无 ASCII 双引号，内容为本期真实主题（알카라스 파리 마스터스 우승、상원 수요일 예산 표결、보졸레 누보 75주년）+ 150문제、A2–B2、2026년 11월 16일–22일。
- 未 commit、未 push；生产文件未改动（复校前后三 SHA 与 SVG 哈希复测一致）；重建副本（`rebuild/ed-copy`、`freeze-core`，约 87 MB）已删，日志与哈希保留。
