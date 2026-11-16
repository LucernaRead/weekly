# W46 简体中文目标家族 D5 独立重校报告

- 家族：W46 zh-cn（目标语简体中文，2026-11-09 → 2026-11-15，VOL.3）+ core-zh-cn，10 版（9 读者 de/es/fr/it/ja/ko/nl/pt/ru + core-zh-cn 兼 en 读者版；无 zh-tw 版，D63 已裁定）
- 重校工作目录：`hidden_files/d5-redo/scratch-2026-w46-zh-cn-reproof/`（`reproof/patched/` 为 builder `patched/` 源文件的独立副本，`reproof/logs/` 为全部重校输出，`reproof/bin/` 为我方驱动/核查脚本；builder 文件、production、issues 均只读，未改动）
- Builder 报告：`FAMILY-W46-ZH-CN-BUILD.md`（全文通读，以它为准绳逐项复核）
- 结论：**PASS**（0 内容/门禁 finding；文本类 finding 2 条，皆为 KIT 生成文案数字口径问题，D43 closer 原地修，不需重校轮次；D60–D62 三项裁定事实依据全部独立证实）
- 磁盘：开工 75G 已用，收尾 76G 已用（<100G 门）

## §0 方法

- 独立重建：`rsync` builder `patched/` 源文件（不含 PDF/text.md.new/svg/cards/`__pycache__`，`diff -rq` 核对 SOURCES-IDENTICAL）→ `reproof/patched/`，用 builder 同款流程（`bin/build-one.sh` 只读调用，日志写我方 `reproof/logs/build/`）重渲印 PDF + 网 PDF + `textexp_zh_cn.py` 导出 text.md。10/10 `rc=0/0/0`，TOTAL 150。
- 全部门禁：builder `bin/gates_zhcn46.py` 只读调用（输出写我方 `reproof/logs/gates/<slug>/`，基线对照读 builder `baseline/` 只读，G11 读 builder `logs/baseline-spill/*.json` 只读），21 verdict/版。
- D19：我方改写版 `reproof/bin/d19_check_reproof.py`（D48 修正逻辑，KIT/content 取我方副本，fixes json 只读）。
- D60/D61/D62：我方脚本 `footer_d60.py`（fitz 页脚 + pdffonts 面计数 + P1 头行/正文行）、`d62_check_reproof.py`（PIL 10x 实墨量测 + Regular 代换复现）、`fanout_check_reproof.py`（fanout 原件 p8 + pdfdiff）、`spotcheck_reproof.py`（§7 三探针，我方副本）。
- `pdftotext` 一律显式单文件路径，未用 glob。报告只贴紧凑表格与 SHA，不贴整份日志原文。

## §1 逐版门禁复核表（重校独立跑，终轮）

10/10 皆为 **18/21 PASS**，残留 FAIL 恒为 G6 + G15a（皆已裁定，见 §5–§6）。G1/G2/G3/G4/G5/G7/G8/G9/G10/G11/G12/G13/G14/G15c/G16/D18/D37/D37-sub 全版 PASS。G15b 仅记录。

| 版 | 终轮 | G3 | G6 | G10 latin_added | G11 spill/observe | G12 | G14 P8 行/页脚余量 | G15a | G15b rc | G15c | D18 间隙 | D37 余量 | D37-sub 余量 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| de | run2 | 0/0 | 1 旗 | 269 | 0/90 | 0 | 243/51.7 | FAIL | 1 | ADOPT 98/1 | 367.9 | +12.5 | +243.6 |
| es | run2 | 0/0 | 1 旗 | 280 | 0/87 | 0 | 203/48.9 | FAIL | 1 | ADOPT 98/1 | 375.3 | +17.0 | +285.9 |
| fr | run2 | 0/0 | 1 旗 | 265 | 0/89 | 0 | 226/50.9 | FAIL | 1 | ADOPT 98/1 | 368.7 | +23.0 | +273.6 |
| it | run1 | 0/0 | 1 旗 | 279 | 0/90 | 0 | 229/46.2 | FAIL | 1 | ADOPT 98/1 | 379.2 | +56.5 | +280.8 |
| ja | run1 | 0/0 | 1 旗 | 133 | 0/96 | 0 | 213/48.9 | FAIL | 1 | ADOPT 99/1 | 399.3 | +223.0 | +279.0 |
| ko | run1 | 0/0 | 1 旗 | 133 | 0/146 | 0 | 210/50.4 | FAIL | 1 | ADOPT 98/1 | 381.0 | +273.0 | +288.5 |
| nl | run2 | 0/0 | 1 旗 | 277 | 0/87 | 0 | 236/48.9 | FAIL | 1 | ADOPT 98/1 | 391.4 | +41.7 | +249.4 |
| pt | run2 | 0/0 | 1 旗 | 278 | 0/91 | 0 | 222/48.9 | FAIL | 2 | ADOPT 98/1 | 374.4 | +46.7 | +287.1 |
| ru | run1 | 0/0* | 1 旗 | 111 | 0/105 | 0 | 242/43.0 | FAIL | 1 | ADOPT 98/1 | 330.7 | +10.0 | +240.9 |
| en | run2 | 0/0 | 1 旗 | 285 | 0/86 | 0 | 231/47.2 | FAIL | 1 | ADOPT 98/1 | 386.8 | +28.4 | +267.6 |

\* ru G3：D5_lat=0、D5_cyr=0，noto_sans=798（Cyrillic 走 Noto Sans，D26 设计行为，口径已豁免；BUILD 一致）。其余各版 noto_sans=0、curly_cjk=0。G15a 三子项：print/web multiset diff=0（10/10）、text.md.new==fanout `.new`（10/10）、pdfdiff vs issues 仅 p1 差 1 个 `—`（10/10，见 §6）。G11 spill 集与基线逐项相同（`set==baseline:True`，10/10）。G8 CLEAN keydiff=[]（10/10）；G7 p8 extract 150/150（10/10）——D3 p8 缺口不存在，W45 D3 不适用本家，独立证实。

注：BUILD §1 基线表 ru/en 两版 D37-sub 记 "—"，与门禁实测不符——builder 基线门禁输出本身即有 ru D37-sub PASS（end=1203.6，余量 +235.9）与 en PASS（end=1172.5，余量 +267.0），量测对象为标语行。属 BUILD 表格简写问题，不影响任何 verdict（我方终轮实测与 builder 终轮逐值一致，见 §2）。

## §2 归一化 diff：0 行

我方 `GATES-SUMMARY.txt` vs builder 终轮 `logs/run2-<slug>/GATES-SUMMARY.txt`（de/es/fr/nl/pt/en）与 `logs/run1-<slug>/GATES-SUMMARY.txt`（it/ja/ko/ru）：归一化（剥离 `round=` tag、G5 网 PDF 字节数、builder/my 绝对路径）后 **10 版 diff 0 行**（`reproof/bin/gates_diff_reproof.py`）。G6/G15a 行未归约——逐值一致（含 G6 旗标文本 3.2×15.8px、G15a `verdict: 1 page(s) differ`）。

## §3 交付物 SHA 核对表

印 PDF 与 text.md 与 BUILD §9 全值逐字节核对（SHA-256 全值，字节数一致）；网 PDF 为 webpdf 非确定性字节漂移，内容等价由 G15a 证实（印=网多重集差 0，10/10）。

| 版 | 印 PDF（字节 / SHA-256） | text.md.new（字节 / SHA-256） | 网 PDF（字节 / 与 builder 差） |
|---|---|---|---|
| de | 28,070,768 / `9650172f…58c27ae9` MATCH | 43,008 / `1ad562b3…6f6ce1f` MATCH | 2,072,004 / +10B |
| es | 28,066,629 / `57b72d44…c7d23` MATCH | 42,599 / `3c8137e3…80c1c` MATCH | 2,067,729 / −6B |
| fr | 28,065,351 / `b520d31a…1fc335d` MATCH | 44,032 / `fde5e88d…83b5f5da` MATCH | 2,066,586 / −21B |
| it | 28,059,937 / `7ecb4e83…a56a60` MATCH | 42,690 / `48e68189…166939` MATCH | 2,061,063 / −1B |
| ja | 32,764,445 / `3a625b9e…9601b` MATCH | 43,909 / `7e471bf6…5515` MATCH | 2,601,613 / −2B |
| ko | 32,334,701 / `51ec0cfc…000ad` MATCH | 43,717 / `e31591d6…6f2` MATCH | 2,504,815 / −14B |
| nl | 28,064,002 / `f5846a59…7ba7e2` MATCH | 42,013 / `269862c3…5130b` MATCH | 2,065,099 / −10B |
| pt | 28,068,608 / `6d836d7d…2f1d60` MATCH | 42,397 / `370c3537…9bb75` MATCH | 2,069,850 / +5B |
| ru | 29,054,061 / `160e613d…93ddd6` MATCH | 51,516 / `dbfeee6c…7bb7fde` MATCH | 2,321,094 / +6B |
| en | 28,096,951 / `e4ee13f3…01b2016` MATCH | 41,728 / `712ee5eb…7adba` MATCH | 2,086,217 / −2B |

- **印 PDF 10/10、text.md 10/10 与 BUILD §9 全值逐字节一致**（SHA-256 全值核对，见 `reproof/logs/sha-check.txt`）。
- 网 PDF 10/10 字节漂移 −21…+10B，属 webpdf 非确定性（时间戳/ID），内容等价由 G15a 证实。无双网 PDF（render-网与 builder-网为同一文件）。

## §4 D19：PASS（47 引用，0 坏）+ 文本类 finding 2 条

- 我方 D19（D48 修正逻辑，`reproof/bin/d19_check_reproof.py`，输出 `reproof/logs/d19-check.txt`）：KIT 引用 38 条 + BUILD 报告引用 9 条 = **47 引用，0 坏**；6 处修复引用全部指向修复行本身（content12.py:23 ×5：de 15pt、es 14pt、fr 15pt、nl 13.5pt、pt 13.5pt；content12.py:89 ×1：en 18pt），行内新字号字面量逐一核实；6 处修复行皆被各自 KIT 引用；无 `f.box` 引用。builder `logs/d19-check.txt` 同为 47 引用 0 坏，一致。
- **文本类 finding F1（10 版 KIT，生成文案计数口径）**：KIT D5 重建节 "终轮 runX：19/21 PASS" 与 GATES-SUMMARY "PASS 18 FAIL 2 of 21" 不符——`kit_update.py:86` 用 `len(v) − len(fails)` = 21−2 = 19，把 G15b RECORD 计为 PASS；严格 PASS 数为 18/21。证据：我方 10 版 GATES-SUMMARY 皆为 `PASS 18 FAIL 2 of 21`。修复（closer 原地改 KIT，不需重渲/重门禁）："19/21 PASS" → "18/21 PASS（另 G15b 仅记录）"，10 版同改。
- **文本类 finding F2（it/ja/ko/ru 4 版 KIT，生成文案事实错误）**：KIT "修复 0 处：run1 即 ALL-GREEN，无需降字号。" 为假——run1 终轮 it/ja/ko/ru 皆为 18/21，残留 FAIL 为 G6 + G15a（已裁定接受，但非 ALL-GREEN）；且与同一节的 "残留 FAIL：G6, G15a" 自相矛盾。修复（closer 原地改 KIT）："run1 即 ALL-GREEN" → "run1 即终轮（18/21，残留 G6 + G15a 已裁定项），无需降字号"，4 版同改。附带："run1 → 修复 → run2" 的行首标签对未修版亦不贴切（无 run2），建议同句改为 "run1 即终轮"。
- 两条皆为 KIT 生成文案的文本问题，不涉及内容、字体、门禁或交付物；按任务 verdict 规则（仅 D19 文本类 finding 允许）与 D43（closer 落仓时原地修 + 针对性复验，不需整轮重校），verdict 仍为 PASS。

## §5 D62 caron 旗核实：PASS（D62 裁定事实依据成立）

- 位置：我方重建 P1 SVG 与 builder 基线 P1 SVG 的旗标行逐版核对——`bāogu`（Newsreader-Italic 21.5，x=1530.8）+ `ǒ`（Noto Serif CJK，21.5，x=1587.8），y=1712.0，**10/10 坐标逐字节相同**（ja/ko 的 `ǒ` 字体面标注为 JP/KR，系 D60 改名，坐标相同）。
- 实墨量测（我方独立，PIL 真实字体，10x 量测后折回 21.5pt；TTC SC 面经 fontTools 名字表定位 index=2 `Noto Serif CJK SC`）：Newsreader-Italic `bāogu` 墨右 = 1530.8+56.6 = 1587.4；`ǒ` 墨左 = 1587.8+0.0 = 1587.8。**真实间隙 +0.40px，两字不相触**（builder 称 +0.50px；0.1px 差为 10x 量化取整，结论一致）。
- Audit 代换机理复现：同一量测改用 Newsreader-Regular：`bāogu` 墨右 = 1530.8+60.2 = 1591.0 → 与 `ǒ` 墨左重叠 **−3.20px，恰等于旗标 3.2px**。证实旗标源于 audit 以 Regular 量斜体的保守代换，非真实重叠。
- es/nl/pt run1 第 2 旗：builder run1 日志核实——es/nl/pt 各 2 旗，第 2 旗为版次行墨与右栏 `本周日历` 重叠（es 24.5×6.0px）；run2 3 版皆回落至仅 caron 1 旗。随 D37 修复消失，属实。
- 结论：G6 终轮 1 旗/版为量测 artifact，接受并记录；不修。

## §6 D61 `—` 核实：PASS（D61 裁定事实依据成立）

- (i) 源头：production `content12.py:115`（de）为含 `—` 的单段 `p.para("「包裹」 bāoguǒ — ein Paket. …")`；fanout/基线 115 行为无 `—` 的斜体头行 `p.text("「包裹」 bāoguǒ", 21.5, italic=True)`，116 行正文段以 `ein Paket. …` 开头、无 `—`；patched 同基线。production 全文件 `—` 计数 30 vs 基线 29，恰差 1 个。基线即缺该 `—`，非 D5 引入。core（en）同理（115 行单段含 `—`，基线拆段无 `—`）。
- (ii) pdfdiff（我方重建网 PDF vs 已发印 PDF）：**10/10 仅 p1 有差，`only-old=[('—', 1)]`，`only-new=[]`，p2–p8 全同**。fanout 原件网 PDF vs 已发版亦同（10/10，见 §10）。
- (iii) P1 视觉/位置：我方重建印 PDF p1（fitz）逐版核实——头行 `「包裹」bāoguǒ`（y=1265.4）与正文段首行（de `ein Paket.`、es `un paquete.`、fr `un colis.`、it `un pacco.`、ja `荷物。`、ko `소포.`、nl `een pakket.`、pt `uma encomenda.`、ru `посылка.`、en `a parcel, a package.`；y=1284.9 或 1291.6）皆在、分行清晰、行间距 >10px；`bāoguǒ` 后无 `—`，10/10。
- (iv) text.md：production text.md vs 我方 `.text.md.new`，`·`→U+3000 归一 + 空白归一后，**10/10 仅差 `only-old={'—': 1}`，`only-new={}`**（未归一前另有家具 `·` 139 处 de–ru / 141 处 en，系校验器设计的家具改写，非差异）。
- 结论：G15a 丢 1 个 `—` 为 §1.1 移植已知差，接受并记录；不另派内容修复。

## §7 D60 面核实：PASS（D60 裁定事实依据成立）

- 我方重建印 PDF（`pdffonts`，大小写不敏感计数；webpdf 子集名用小写 `CJKsc/jp/kr`）：**ja JP 31 处、ko KR 31 处、其余 8 版 SC 31 处**（Newsreader 26 处，ru 22 处；另 UnifrakturMaguntia 1 处）。ja/ko 无 SC 面，其余版无 JP/KR 面。
- 已发 10 版（issues PDF）：**全为 SC 面**（NotoSans/SerifCJKSC + Unifraktur；无 Newsreader、无 JP/KR/TC），10/10——ja/ko 已发版亦为 SC，非 JP/KR（任务书前提有误，D63 已裁定）。
- 对照：W47 已发 zh-cn-ja 为 JP 面、zh-cn-ko 为 KR 面；W45 已落仓 zh-cn-ja 为 JP 面、zh-cn-ko 为 KR 面（皆含 Newsreader）。与 PLAN D60 证据一致。
- 文字层与已发版一致：G15c 全版 ADOPT + §7 内容抽查 30/30（见 §8）。
- 结论：ja/ko JP/KR 面为机制规定的 D5 行为，不是缺陷，不列为 finding。

## §8 §6 core-zh-cn + §7 内容抽查

- §6：production `2026-w46/` 内**无** `2026-w46-zh-cn-zh-cn` 目录（应无）；`core-zh-cn/` 内含 `2026-w46-zh-cn-en.text.md` + KIT + 内容源 + render/run/svglib（`fix/`、`proofread-gates*`、`zh-cn-gates.log` 等工作目录不动，不随同步）。
- 页脚（fitz 读已发 PDF P1 最末 VOL.3 行 vs 基线 P1 SVG 最末 VOL.3 行；`·`/U+3000/全部空格归一后比对）：**10/10 吻合**。9 读者版为各读者专属串（如 de `Lucerna CHINESISCHE WOCHENZEITUNG VOL.3 TEXT AUF CHINESISCH (VEREINFACHT) ERKLÄRUNGEN AUF DEUTSCH`；ru 西里尔串；ja/ko 各自日韩串）；en 版为 core 串（`Lucerna 简体中文周报VOL.3 简体中文正文 英语讲解 Simplified Chinese text English explanations`）；en 标语为 core 英文版（`每周读中文· Read real Chinese, every week`，我方 en P1 SVG 在位）。SVG 行另含同行页码串（如 `Seite 1 von 8`、`Page 1 sur 8`、`第1版／共8版`），已发 PDF P1 内以独立行存在，核对无误。
- closer 同步方向：9 读者版 → 各自 production 读者目录；en 版 → `production/2026-w46/core-zh-cn/`。绝不以 core 覆盖读者目录。
- §7 内容抽查（我方副本重跑三探针：P1 主标题、"高潮场" 计数、P8 末键 150. 行）：**30/30 通过**（探针 1 `双11到了,包裹一波一波地来` 10/10；探针 2 `高潮场` 计数已发=重建=23，10/10；探针 3 P8 末键 `150. ✓ …` 行，10/10）。

## §9 §8 同步清单 / KIT pin / D1+D5 安装等价性

- `diff -rq` 我方 patched/ vs production/2026-w46/：**每版 9 个同步文件**，行差（production → patched，`+` 为 patched 新增）与 BUILD §8 表逐值一致：KIT +21/−0（de/es/fr/nl/pt/en）、+18/−0（it/ja/ko/ru）；svglib +461/−40（ja/ko +463/−43、+463/−42）；bslib4 +31/−34；content12 +59/−58（ja/en +60/−59）；content34 +33/−33；content56 +35/−35；content7 +17/−17；content8 +12/−12（ja +13/−13）；render +13/−1。行差主体为 D1 移植 + 6 处修复。
- 不变：run.py、ABSTRACT.txt、assets/CREDITS.md（10 版皆逐字节相同）；图文件不同步（frost/lanparty/locker/lucerna-moth/popcorn/valley 仅 patched 侧有，D20 + D58）；`svg/`、`cards/` 不同步；core 的 `fix/`、`fix-keys/`、`fix-round3/`、`fix-round4/`、`proofread-gates*`、`zh-cn-gates.log` 不动。`transform.py` 在 patched 与 production 两侧皆不存在（"不动"空无对象）。
- KIT：production KIT 前缀 0 漂移（10/10）；D5 节 10/10 在位。Pin 块逐项核实：`_D5_READER` 在 svglib.py:132（10/10，另有引用行 79/125/172/184）；fanout svglib Newsreader 11 处（抽查 de/ja/ru）；`_QUOTE_CLS` 4 处（抽查 de/ja/ko/ru）；字体面 SC/JP/KR（见 §7）；导出器 ADOPT（G15c 10/10）；KIT 修复表行数与 fixes json 一致（6 版各 1 行、4 版 0 行）。Pin 块按 `kit_update.py` 设计为配置 pin（不含 SHA 值）；§9 SHA 一致性由 §3 独立核对（印 10/10、text 10/10）。
- D1+D5 安装等价性：patched svglib 内 FIX2_BLOCK、D5_BLOCK、READER_CONST 首行皆在位（与 `apply_variant.py` 的 `patch_d5()` 对照）；`bin/d5_port_zhcn46.py` 实现 9 步移植 + face 参数自查（6 签名）；内容文件 10/10 无 `face=` kwarg。W47 production `core-zh-cn/svglib.py` 核实为 666 行另一代引擎（通用 `_IDX`、`_char_font(ch, kind, bold, italic=False)` 无 `face` 参数、caron 相关计数 0），无法作本家模板——BUILD 陈述属实。

## §10 FANOUT-REPORT 不符点复核：builder 实测成立，报告两处不准

- 我方在 fanout 原件上独立重跑（`reproof/bin/fanout_check_reproof.py`，输出 `reproof/logs/fanout-check.txt`）：p8 extract **150/150**、p8 compare **CLEAN（core 150、edition 150、keydiff []）**，10/10。FANOUT-REPORT-W46.md 所称 "EXTRA_ONLY [108]"（9 版）/"SHORT [108]"（core）与实测不符——原件本身即 CLEAN（报告 L74–78 的 is_header FP  adjudication 与实测不符）。
- fanout 原件网 PDF vs 已发版 pdfdiff：**10/10 仅 p1 差 1 个 `—`**（`only-old=[('—', 1)]`，`only-new=[]`，p2–p8 全同）。FANOUT-REPORT 所称 "IDENTICAL 8/8" 与实测不符。
- 结论：以 builder 实测为准；两处皆为 fanout 报告不准，非 builder 缺陷。D61 的 `—` 差在 fanout 原件层面已存在（见 §6(i)）。

## §11 D47 + 其余残留项

- D47：已发 10 版 text.md **`###` 全 0**（逐版 grep），`##` 各 8 行；导出器 `textexp_zh_cn.py` 无 `###` 逻辑（grep 0）。D47 不适用，无补行任务。
- G15b 仅记录（共享校验器对中文格式未校准）：终轮 rc=1（9 版）、rc=2（pt，未校准读者）；验收以 G15a（除 §6 的 `—` 外全过）+ G15c ADOPT + §8 抽查为准。
- P2 空白加宽：fanout 已加宽的 accepted difference，fr P2 已 reopen 待 redesign——pre-existing，非 D5 引入，非 D5 发现；本重校仅记录。
- ru D37 终轮 +10.0 偏紧：实测核实——`end=1429.5 margin=10.0 ink_end=1429.4`，实墨比名义端点内收 0.1px，通过；未修、记录。
- nl/pt 13.5pt 修复后余量：实测 nl **+41.7**、pt **+46.7**（预测 +22.2/+23.5；分数号实渲比线性预测更窄，方向安全），核实。
- P7 读者来信盒溢出：未出现——G11 spill=0 全版（10/10），W45 ko 式溢出本家无。
- D3 p8 缺口：不存在——G7 150/150 + G8 CLEAN 全版 + fanout 原件同测（§10）。

## §12 残留项（仅记录类）

| # | 项 | 状态 |
|---|---|---|
| 1 | G6 斜体 caron 旗（10 版各 1 旗） | D62 量测 artifact，接受并记录（§5） |
| 2 | G15a 丢 1 个 `—`（10 版各 p1 1 个） | D61 §1.1 移植已知差，接受并记录（§6） |
| 3 | G15b RECORD（rc=1 ×9、rc=2 pt） | 共享校验器未校准，仅记录 |
| 4 | KIT 文案 F1：10 版 "19/21 PASS" | 文本类，closer 原地改为 "18/21 PASS（另 G15b 仅记录）"（§4） |
| 5 | KIT 文案 F2：it/ja/ko/ru "run1 即 ALL-GREEN" | 文本类，closer 原地改为 "run1 即终轮（18/21，残留 G6 + G15a 已裁定项）"（§4） |
| 6 | P2 空白加宽（fr 重开） | pre-existing 待 redesign，非 D5 |
| 7 | ru D37 +10.0 偏紧 | 通过，记录 |

## §13 事故记录

- 无事故。未改 builder 文件（builder `logs/d19-check.txt`、`sync-sha.json` 的 mtime 为 2026-11-16 07:50–07:52 UTC，早于本重校开工 07:55 UTC，系 builder 自身收尾写入）；未改 production/issues（`git status` 无 2026-w46-zh-cn 条目；weekly-git 未跟踪的 W47 文件为 pre-existing）；未 commit/push；未跑 `node lint.mjs --write`；未在循环跑着的时候改脚本（构建/门禁驱动皆为我方新建脚本，builder 脚本只读调用）。
- 重校中发现并修正的我方脚本问题（皆为我方核查脚本的解析/口径问题，非 builder 缺陷）：(a) D60 面计数须大小写不敏感（webpdf 子集名用小写 `CJKsc/jp/kr`）；(b) §6 页脚须按 BUILD 方法去全部空格比对（fitz 会合并相邻 span，如 `週刊VOL.3`）；(c) D62 位置核对须限定 y=1712.0 旗标行（P1 另有一处 y=920.4 的 `ǒ`）并只比 (text, x, y)（ja/ko 面标注 JP/KR 系 D60 设计）；(d) D61(iv) 须先 `·`→U+3000 归一；(e) fanout-check 的 extract JSON 键为 `noted_set`。修正后全部复核项皆为 PASS。
