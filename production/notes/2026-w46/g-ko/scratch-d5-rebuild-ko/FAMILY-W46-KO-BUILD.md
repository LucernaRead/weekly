# W46 韩语目标家族 D5 重建报告

- 家族：W46 ko（目标语 ko，读者 de/en/es/fr/it/ja/nl/pt/ru/zh-tw；无 ko 读者）+ core-ko
- 周次：2026-11-09 → 2026-11-15（VOL.3，W46，2026-11-16 到期）
- Builder 工作目录：`hidden_files/d5-redo/scratch-2026-w46-ko/`（`baseline/`、`patched/`、`logs/`、`bin/`、`backup/`）
- 结论：**严格门禁计数 0/11 ALL-GREEN；10/11 run2 18/19（仅 G15a FAIL），fr 17/19（G15a + G2 门禁计数 artifact）**。可修缺陷全清：修复 121 处（9 文件），只降字号，不改文案。两处未过项皆已裁定（G15a 为模板行为，§0.5；fr G2 为门禁计数 artifact，§0.5）——见 §10。
- 本报告 + GATES-SUMMARY 复本另存 `hidden_files/d5-redo/notes/g-ko/scratch-d5-rebuild-ko/`（D29，cmp 核对）。

## §0 方法

### §0.1 导出器核实（步骤 0，P3b）——ADOPT

- 导出器：**`hidden_files/style-port-ko/textmd_ko.py`**（AST 手稿路由），不是任务初稿所列的 `textexp_ko.py`（SVG 路由，本家未用——与 W45 ko 先例一致，实测确认）。原生校验器 `verify_textexp_ko.py --edition` + W46 trim `--trim "3 면 단 풍 과 11 월 11 일 의 세 이 름|3 면 단 풍 과 11 월 11 일 세 이 름"`（sommaire "의" 丢字）。
- 试跑（`logs/step0/`）：**11/11 导出 rc=0，试跑输出与 fanout `.text.md.new` 逐字节相同**（条目数 de 339、en 339、es 339、fr 339、it 339、ja 340、nl 339、pt 339、ru 341、zh-cn 339、zh-tw 341）。原生校验器 vs `issues/` text.md：**11/11 ADOPT（0 UNEXPECTED）**，REWRAP 60–61、TRIM 1。
- **但与 `issues/` text.md 不是逐字节相同——这是设计使然，不是失败**：旧引擎导出用 ` · ` 分隔符，移植导出用 U+3000；试跑输出比 issues/ text.md 小约 211 字节，差异约 246–250 行。正确的基线标准是：基线导出 == fanout `.new` 逐字节相同 + 原生校验器 ADOPT + `pdf_text_diff_ko.py` 对 issues/ PDF 为 IDENTICAL（见 §0.4）。
- **R1 已知缺口（D39(3)，本轮不修，逐版核实无其他遗漏）**：`textmd_ko.py:is_prose` 漏收已渲染短拉丁串。`bin/r1_scan3.py`（权威；v1/v2 为噪声版已废）实测真缺口：
  - 拉丁读者（de/en/es/fr/it/nl/pt）4 项：caption 词 `KIMJANG`（en 为 `KIMCHI-MAKING`，`content12.py:28`）；`A2→B2`（`content12.py:101`）；读者词 `content12.py:102`（de/nl `Alle`、en `All`、es/pt `Todos`、fr `Tous`、it `Tutti`）；`D-10 ~ D-4`（`content56.py:141`）。
  - CJK/ru 读者（ja/ru/zh-tw/core）2 项：`A2→B2`、`D-10 ~ D-4`。
  - 另有 4 句斜杠提示句 `content8.py:61/63/65/67`（`저는 / 수요일에 / 가래떡을 나눠 줘요 → ___` 等），被 `is_prose` 的 `/` 规则丢弃；句中词在 md 中以 plain 形式存在，仅提示形式缺失。
  - W45 的 `D-17 ~ D-12` 与 `IPDONG` 在 W46 不存在。缺口恰为所列，无其他遗漏。

### §0.2 D1 定性（步骤 0.2）——D1+D5 一次做

- 生产 `2026-w46-ko-*/svglib.py` + `core-ko/svglib.py`，11/11：**D1 fix 0 处、Newsreader 0、`_D5_READER` 0、`_char_font` 0**，247 行 → pre-D1 旧样式。9/11 生产 svglib md5 相同（`2f86e3c0…`）；it 仅 docstring 不同（重阳 vs 英文 "Double Ninth"）；zh-tw 不同（TC index + 重陽字）。
- Fanout `fanout-2026-w46/<reader>/svglib.py` + core，11/11：**D1 fix 在位、Newsreader 8（zh-tw 7）** → 新样式（§1.1 移植）+ D1 fix，无 D5。装机自 fanout 即带 D1；重建为 **D1+D5 一次做**（与 W45 ko 先例相同）。
- Patched svglib 来源：`hidden_files/d5-redo/tools/mechanism-w47/svglib-ko-d5.py`（539 行，`_D5_READER = "latin"` 默认），**与 W47 mechanism 拷贝逐字节相同**；与 W47 production `core-ko/svglib.py` 仅差 `_D5_READER` 一行（latin vs cjk）。`_D5_READER` 在 `svglib.py:122`（latin：de/en/es/fr/it/nl/pt；ru：`"ru"`；cjk：ja/zh-cn/zh-tw + core-ko）；kinsoku `NO_START` 块在 L290–297（D5-METHOD 称 ko 模板无 kinsoku 是错的——它有）。`Page.text`/`para` 不取 `face` 参数 → 无 W45 ru F-1 式 `face` 参数 bug（自查通过）。
- 装机核实（`bin/install.py`，`logs/install.json`、`logs/install.log`）：11/11，char_font ≥1、`_QUOTE_CLS` ≥1、`_kr_index` ≥1、`py_compile` 全过；与模板 diff：latin 版 0 行、ru/cjk 版恰 2 行（`_D5_READER` 行对）；机制 `test_d5_routing.py` **FAILURES: 0**。绝不在模板上跑 `apply_variant.py`（会把 KR 下标改写为 JP）。

### §0.3 zh-tw 字体面核实（步骤 0.3，D52 教训）——已发 TC，模板 KR-only，**报协调员裁定**

- 已发 PDF 嵌面（`pdffonts`，issues/ 网 PDF）：**10/11 版 KR-only**（NotoSans/SerifCJK KR 各 ×16）；**zh-tw 为 TC-only**（NotoSans/SerifCJK TC 各 ×16 + UnifrakturMaguntia，无 Newsreader）。
- Fanout 复现已发面：各读者默认 `face="KR"`，唯 zh-tw 默认 `face="TC"`（整文件 TC 变体，content 内 `face=` 0 处）。
- **不符**：已发 zh-tw 读者文本为 **TC 面**；D5 模板为 KR-only。按任务令与 W46 ja §0.3 先例处理：以模板装机（builder 不单方面重设计模板），文字层相同，门禁无法检测字形变体差异。**已按任务令上报协调员**：governing rule 是“复现已发版的字体面”，已发为 TC 则应为 TC；机制 `base_core_for()` 称 reader zh-tw 用 core-zh-tw（TC）作基底，但 D5 模板无 TC 分支。**不得自默决定，见 §10。**
- ko 面按 D53：SC→KR 是机制规定的 D5 行为，接受、不质疑。ja 面：已发 KR（fanout ja 默认 KR），与模板一致，核实通过。

### §0.4 基线（步骤 1）——除 3 项先存记录外 CLEAN

基线 = fanout 装机 + 全套门禁（`logs/baseline-*/`）。11/11：

| 项 | 基线值 |
|---|---|
| run | TOTAL 150，FLOW 0；HEAD 1 仅 fr（P1 标题 `지금 바로 연습　Exercices immédiats` 426.4px vs 栏 422.5px，+3.9px，W45 已知 port 遗留） |
| text.md | 与 fanout `.text.md.new` 逐字节相同（core 27222、de 27917、en 27748、es 28053、fr 28079、it 28031、ja 28041、nl 27897、pt 28056、ru 30131、zh-tw 27298 字节） |
| PDF 文字层 | `pdf_text_diff_ko.py` vs issues/ PDF：**IDENTICAL，rc=0**，8/8 页；印=网多重集差 0 |
| SVG | 8/8 与 fanout SVG 逐字节相同，唯 zh-tw 7/8（见下） |
| p8 | extract 150/150；compare CLEAN，keydiff [137, 138]（zh-cn/zh-tw []——core 即参照本身） |
| G15c | ADOPT（0 UNEXPECTED），11/11，REWRAP 60–61、TRIM 1 |
| G15b | rc=1 全版，唯 pt rc=2（无 pt 读者表，D27） |
| G15a vs issues 分解 | `·`×127 + `—`×1（core `·`×118；fr `·`×126；zh-tw 另 `／`×8 + `/`×8——移植分隔符改动） |
| G3 普查 | Latin in CJK：de 429、en 409、es 433、fr 405、it 436、ja 208、nl 443、pt 434、ru 210、zh-cn 208、zh-tw 208；ru 另 Cyrillic 252；curly_in_CJK：de 2、en 1（total 4），其余 0 |
| G11 | SPILL 0 全版；OBSERVE：core 274、de 293、en 286、es 289、fr 286、it 291、ja 287、nl 291、pt 286、ru 300、zh-tw 287 |
| G12 | DEFECT 0 全版；OBSERVE 1：en P2 `김장 장보기 목록　Kimchi shopping list` +9.5、es P5 `이번 주 청년 숫자　Cifras de la semana` +4.5、ru P1 `숫자로 보는 이번 주　Неделя в цифрах` +10.5（皆与 backup 同值，先存） |
| G13 | 0 TOUCH，0 NEAR 全版 |
| G14 | defects 0 全版；observes 1：en/es/ru（同上三标题）；p8rows/页脚余量：core 200/48.9、de 230/47.2、en 228/50.4、es 232/48.7、fr 224/46.2、it 234/50.4、ja 200/48.9、nl 227/59.9、pt 234/47.7、ru 211/46.1、zh-tw 200/48.9 |
| G16 | defective 0 全版 |
| D18 间隙 | core 374.9、de 264.4、en 301.2、es 349.5、fr 334.4、it 340.0、ja 374.9、nl 365.1、pt 350.1、ru 334.1、zh-tw 374.9（已修正 letter-spacing 贪婪正则，见 §0.6） |
| D37 余量 | core 252.3、de 93.3、en 103.7、es 54.1、fr 85.1、it 151.3、ja 262.0、nl 65.5、pt 48.3、ru 73.0、zh-tw 252.3 px |
| P8 | 元素数 core 1739、de 1276、en 1271、es 1274、fr 1271、it 1268、ja 1725、nl 1277、pt 1274、ru 2537、zh-tw 1587；max_y 皆 2624.0，页脚余量 76.0px |
| 印/网字节 | 印：core 31,990,266、de 32,654,831、en 32,034,608、es 32,441,827、fr 32,242,235、it 32,437,766、ja 36,132,897、nl 32,438,750、pt 32,443,321、ru 30,571,948、zh-tw 32,048,748；网（builder/render）：core 2,480,319/2,480,316、de 2,255,013/2,255,011、en 2,232,255/2,232,251、es 2,242,793/2,242,789、fr 2,243,553/2,243,566、it 2,235,958/2,235,955、ja 2,612,262/2,612,252、nl 2,238,588/2,238,594、pt 2,244,272/2,244,272、ru 2,181,562/2,181,561、zh-tw 2,603,060/2,603,060 |

- 基线分：core 18/19、de 18/19、en 18/19、es 18/19、fr 16/19（G3 + G1/G2 HEAD）、it 18/19、ja 18/19、nl 18/19、pt 18/19、ru 18/19、zh-tw 17/19（G3 + G9 fanout p2 0 字节）。每版唯一未过项皆为 G3（修前普查）。
- 基线先存记录（D25 类，不修、不阻塞）：
  - **G9 zh-tw 7/8**：fanout `zh-tw/svg/p2-saenghwal.svg` 为 **0 字节**（整棵 fanout-2026-w46 唯一 0 字节 SVG，2026-11-10 09:16）。基线 p2 完好（969 个 text 元素、pdfdiff IDENTICAL、text.md 逐字节相同）——fanout 参照损坏，非基线缺陷。
  - **P2 中页空白加宽**：fanout 报告已诊断为结构性、已 reopen 的缺陷类（NO-GO），非 D5 发现，不修，未重测。
  - **D39(4) teaser 带底缘越页脚线：本家不存在（实测，非假设）**。基线 P7 teaser 带底缘：de 2497.2、en 2512.7、es 2526.2、fr 2526.2、it 2526.2、ja 2499.7、nl 2528.7、pt 2523.2、ru 2528.7、zh-tw 2518.7、core 2518.7——皆在页脚线 2596 之上（余 67–99px）。W45 的 en −2.9 / nl −6.3 / ru −7.3 类越线在本家不复现。
  - **P7 读者来信盒溢出：本家不存在**。基线 G11 SPILL 0 全版。W45 ko 的 4 版 P7 溢出在本家不复现。
  - **D2 / freeze.py**：`freeze.py baseline` 在 venv 下对 pre-D5 ko **abort rc=2**（guard 读 `_D5_READER` 标记；Pillow 10/system python3 预期）。fanout 时代基线已过期：fanout SVG 为 venv 构建（venv 重建 8/8 逐字节复现）。基线 G9 裁定 = PASS（"SVG 8/8 vs fanout" + 记录 abort）。patched 版（标记在位）freeze 在 venv 下正常工作。
  - **KIT pin 过期**：de KIT 印 pin 32,911,089 B（sha `ae645a2d…`）vs 基线实测 32,654,831 B——与 W45 ko 相同的 "KIT SHA lag"。fanout 印 PDF 96,813,190 B 为已知 fanout 印 PDF 尺寸异常，不入闸。以 fanout/基线实测值为准，不以 KIT pin 为准。

### §0.5 门禁口径

- 19 verdict/版：G1–G14 + G15a/G15c + G16 + D18 + D37；**G15b 仅记录**（D27：共享 `verify_textmd.py` 对 ko 格式未校准；run2：10 版 rc=1，pt rc=2 无读者表——与 W45 ko 一致的已知工具缺口）。
- G15a：印=网多重集差 0（严格）+ text.md 与 fanout `.new` 逐字节相同 + `pdf_text_diff_ko.py`（带 trim）vs issues/ PDF；vs issues 多重集差只记录并分解（`·`/`／`/`—` 三类移植分隔符）。**run1/run2 pdfdiff 皆为 DIFF，见下裁定。**
- **G15a pdfdiff DIFF 裁定（11 版皆同，模板行为，非内容缺陷；报协调员/重校）**：ko D5 模板（`svglib-ko-d5.py` L223–256）有 `BLANK = "\u00a0"` 填空机制（`_blank_run`、`_blanks`）：`___` 变为 NBSP run，以 1.1pt 墨线绘制，网 PDF 文字层因此丢 `_` 字符。run1 core pdfdiff：仅旧侧 `[('_', N)]`，p1 18 / p2 27 / p3 27 / p4 27 / p5 39 / p6 12 / p7 18 / p8 63；run1 网 PDF 0 个 ASCII `_`、0 个 U+FF3F，已发版 231 个 ASCII `_`；text.md 仍带填空（run1 与基线导出皆 69 个 `_`）。fanout（旧）svglib 无此代码；ja D5 模板（`svglib-ja-d5.py`）完全无 BLANK 代码——这就是 ja 得 pdfdiff IDENTICAL 而 ko 不得的原因。G15a 其余分量全版通过（印=网多重集差 0、text.md 逐字节相同）。builder 不重设计模板。G15a 按门禁记 FAIL，附本裁定；不得静默放过。
- **fr G2 裁定（门禁计数 artifact，交付件干净；报协调员/重校）**：run2 唯一 finding 仅在冻结的基线日志内（`logs/baseline-2026-w46-ko-fr-run.log:2`，修前 HEAD TOO WIDE `지금 바로 연습　Exercices immédiats`）；run2 日志本身干净（G1 TOTAL 150、FLOW 0、HEAD 0）。`gates.py` G2 裁定为 `len(patched_f)==0 and 'PASS' in out`，而 `head_check.py` 任一受检日志（含冻结基线日志）有 finding 即印 FAIL——fr 在此门禁下永不过，尽管 patched 交付件已修好。**不得改 `gates.py` 让它通过**（那是 gaming 门禁）。按实测报告，附本裁定。
- G11：重建 spill 集须 == 基线 spill 集（D25 先存几何，不以“0 SPILL”一刀切；本家基线 SPILL 0，run1/run2 亦 0）。
- G3：普查 0 违规；ru 另计 Noto Sans 元素（run1/run2 1050——D26 旧分支预期值）。
- G10：cjk_added {}、latin_added 0 全版（ko fanout 已拆分 reader run，D5 不新增 run——与 ja 家不同，ja latin_added 92–214）。
- G14：creambox defects 0；p8 行数因 run-split +1（见各版），页脚余量不变；advance ratio 中位 1.008、粗体中位 1.04（Newsreader 较 CJK 面宽约 4%，D5 固有）。
- D18：刊头标语行间隙，内容识别（含 "2026" 的日期行），绝不硬编码 y。D37：徽章行余量，内容识别实际副刊头行（y∈[360,400]），绝不硬编码 y=612（D39(5)）；ko P1 无 y=612 徽章行（y=616 为 section title，y=628 为 label）。D37-sub：副刊头行行末 x vs 右栏左缘 1439.5（本家 binding 行即 sub 行）+ 实墨复核（见 D41 节）。
- P8：`<text>` 元素数 + max y；11 版 max_y 皆 2624.0，余量 76.0px。

### §0.6 工具注记

- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 已验）。**任务所列 `hidden_files/d5-redo/tools/venv/bin/python` 不存在**，用规范解释器，特此注明。
- 门禁脚本 `bin/gates.py`（`bin/gates-all.sh` run1/run2；`bin/build-one.sh`：run.py → render.py（内调 `tools/webpdf.py` 生成网 PDF）→ `textmd_ko.py`）。本轮修过的脚本缺陷：
  - `build-one.sh` 的 `${SLUG##*-}` 对 zh-tw/zh-cn 得 `tw`/`cn`，`set -u` 下 `EXPL: unbound variable`，首批循环静默杀死 zh-tw 与 core-ko 构建——改 `${SLUG#2026-w46-ko-}`；`gates.py` 的读者推导同 bug（`slug.split('-')[-1]` → `removeprefix('2026-w46-ko-')`）。
  - `gates.py`：TRIM 串含未拆分的 `단풍`（永不匹配校验器的逐 CJK 字分词）——改为逐字空格，core-ko G15c HOLD→ADOPT；G6 flagline 误 match occlusion 自测行（含 'TEXTX'）——过滤自测/planted 行。
  - `build-one.sh` 日志位置 quirks：相对 logprefix 时日志写入版目录（`cd "$D"` 之后）；`gates.py` 要 `logs/<round>-<slug>-*.log`——跑门禁前先复制到位（run1/run2 各 11 份）。
  - `gates-all.sh`：core 先跑，继而 de..zh-tw；读者版 core-svg 参数为 patched core svg，基线轮与 core-ko 自身用基线 core svg。G11 对照 `logs/baseline-spill/<slug>.json`（基线轮记录）。G9 基线用 fanout-SVG 对比；G9 run1/run2 用真实 freeze.py 基线（build-copy 事后删除）。G15a 含印=网字符多重集差（去空白）、text.md 逐字节相同、pdf_text_diff_ko IDENTICAL、网-vs-issues 分解（仅记录）。P8 附加：元素数 + max_y + 2700−max_y 页脚余量。
  - `bin/measure_d18_d37.py` 两个量测 bug（已修）：（1）贪婪正则吞掉 `letter-spacing`，标语末低估、间隙高估（基线 D18 已修正，见 §0.4）；（2）`slog[0]`/`vol[0]` 单 run 逻辑在 D5 多 run 标语下失效——改为按簇分组（标语末 = 簇内最大 run 末，中心 = (最小 x + 最大末)/2；D37 按 y 分组，末 = 最大 run 末）。
  - `bin/kit_update.py` 三处修正后才跑（见 §10）：gates 路径改为 `logs/run2-<slug>/gates.json`；fixes.json 改为 kit 格式（按版分组，含 over/probe）；KIT 节措辞 "run2 ALL-GREEN" 改为实测结果。另 zh-tw 读者推导同 split bug（`KeyError: 'tw'`）——修后单独重跑 zh-tw，无重复追加（11 版 KIT 各恰 1 个 D5 节）。
- `bin/apply_fix.py`：模式定位（无硬编码行号——ja 偏 −1），每处验证精确预期模式 + 计数 + `py_compile`；`logs/fixes.json` 记录 121 处。
- `bin/probe_flow.py`：`wrap()` 在 CW=422.5 下探针（见修复 A）。

### §0.7 几何常量

- 页 1950×2700；RIGHT=1862（右栏右缘）；MX=88；CW=422.5；GUT=28；COLX=[88, 538.5, 989, 1439.5]；页脚线 y=2596；页底 2700。
- P1-headline 流底 1828；p.text 盒标题预算 400.5（x=bx+22 起，右缘 1862.0）；f.box 标题预算 404.5（x=box.x+18 起，右缘 box.x+422.5）。
- 刊头结构（基线 de P1 实测）：y=92 行 VOL.3（x=88）/ 标语（x=619.8）/ 日期（x=1596.4）；y=366 韩语标语 + y=394 读者行，皆居中 975.0。

### §0.8 事故

1. **`build-one.sh` slug bug**（首批循环）：zh-tw 与 core-ko 构建被 `EXPL: unbound variable` 静默杀死（见 §0.6）。修正后重跑，11/11 rc=0/0/0。无文件损坏（构建未开始）。
2. **`measure_d18_d37.py` 在 run1 门禁循环跑着时被改**（违反 AGENTS.md 教训；bash 按字节偏移增量读脚本）。run1 前期版（de/en/core）用旧脚本，后期版用新脚本。事后归一：run1 D18 的 de/en/core 由 run2 D18 回填（263.1 / 297.5 / 370.4——y=92 行不受任何 run1→run2 修复影响，故 run1 == run2，见各版表注）；run1 D37 不受影响（逐 run 最小余量逻辑等价）。不再犯。
3. **`kit_update.py` zh-tw `KeyError: 'tw'`**（见 §0.6）：读者推导修正后单独重跑 zh-tw；11 版 KIT 各恰 1 个 D5 节，无重复追加。

## §1 de / en / es

### 2026-w46-ko-de（读者 de）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a，见 §0.5） |
| G1 | TOTAL 150，**FLOW 1**：`!! FLOW OVERFLOW [P1-headline] col 2 y=1756 need 99 bottom 1828`（流止 y=1942） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 2） | 同左 |
| G4/G5 | 印 30,536,905B / 网 builder 2,152,533B，render 2,152,547B | 印 30,536,939B / 网 builder 2,152,579B，render 2,152,574B |
| G6 | **flags 7**（P1，见 D41 节） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 443，== 基线集 | SPILL 0，OBSERVE 439，== 基线集 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 230→231，页脚余量 47.2→47.2 | 同左 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF**（§0.5 裁定） | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 263.1px（基线 264.4；回填值，见 §0.8） | 同左 |
| D37 | 46.8px（35.1pt），row y=394 end=1392.7（基线 93.3） | 同左 |
| P8 | 1364 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A，13 处）：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| A P1-headline 流 6×`f.para` | `content12.py:40–45` | 24 | 22 | FLOW need 99px（流止 y=1942，底 1828） | run2 流止 y=1249，余 579px；G6 7 旗标同清 |
| A P1-headline 流 6×`f.ex` | `content12.py:56/58/60/62/64/66` | 19.5 | 18.5 | 同上 | 同上 |
| A P1-headline 流 `f.head` | `content12.py:54` | 25 | 24 | 同上 | 同上 |

探针（`bin/probe_flow.py`，`wrap()`，CW=422.5）：6 段 24pt = 32 行 1227.4px；22pt = 29 行 1029.8px（省约 198px）；21pt = 921.8px。P2 流（同文件 173 行后）未动。

### 2026-w46-ko-en（读者 en）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 4） | 同左 |
| G4/G5 | 印 30,545,189B / 网 builder 2,161,456B，render 2,161,457B | 印 30,545,245B / 网 builder 2,161,518B，render 2,161,518B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 435，== 基线集 | SPILL 0，OBSERVE 434，== 基线集 |
| G12 | **DEFECT 1**：P2 `김장 장보기 목록　Kimchi shopping list` fs 23，over **+10.3px**，core −18.0px（D5 回归；基线 OBSERVE +9.5） | DEFECT 0，OBSERVE 0 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 1 | defects 0，observes 0 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 297.5px（基线 301.2；回填值，见 §0.8） | 同左 |
| D37 | 57.5px（43.1pt），row y=394 end=1382.0（基线 103.7） | 同左 |
| P8 | 1376 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A 13 处 + B 1 处 = 14 处）：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| A P1-headline 流 | `content12.py:40–45`、`56/58/60/62/64/66`、`54` | para 24 / ex 19.5 / head 25 | para 22 / ex 18.5 / head 24 | FLOW need 99px | run2 流止 y=1165，余 663px |
| B P2 box 标题 `김장 장보기 목록　Kimchi shopping list` | `content12.py:202`（`f.box` 收尾行 `], tsize=21)`，D19） | tsize 23（默认） | tsize 21 | boxtitle +10.3px，框 [989, 860, 422.5, 351] | run2 墨右 1386.0，框右 1411.5，余 **25.5px** |

### 2026-w46-ko-es（读者 es）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 30,538,328B / 网 builder 2,153,904B，render 2,153,908B | 印 30,538,370B / 网 builder 2,153,952B，render 2,153,948B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 440，== 基线集 | SPILL 0，OBSERVE 436，== 基线集 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 232→233，页脚余量 48.7→48.7 | 同左 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 346.4px（基线 349.5） | 同左 |
| D37 | **3.5px**（2.6pt），row y=394 end=1436.0（基线 54.1）——名义 PASS 但实墨越线，见 D41 节 | **32.3px**（24.2pt），row y=394 end=1407.2；实墨 **+23.5px** |
| P8 | 1362 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A 13 处 + D 1 处 = 14 处）：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| A P1-headline 流 | `content12.py:40–45`、`56/58/60/62/64/66`、`54` | para 24 / ex 19.5 / head 25 | para 22 / ex 18.5 / head 24 | FLOW need 99px | run2 流止 y=1249，余 579px |
| D P1 副刊头行 y=394 | `content12.py:20` | 16 | 15 | 实墨越右栏线 **−5.8px**（名义 +3.5px，`text_w` 低估） | run2 实墨余 **+23.5px**；名义余 32.3px |

## §2 fr / it

### 2026-w46-ko-fr（读者 fr）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（G15a + G2 artifact，见 §0.5） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99）+ **HEAD 1**（`지금 바로 연습　Exercices immédiats` 426.4 vs 422.5） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | **defects 2**（patched 1 + baseline-side 1） | **defects 1**（仅 baseline-side；交付侧 0——门禁计数 artifact，见 §0.5） |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 30,549,747B / 网 builder 2,165,755B，render 2,165,753B | 印 30,549,796B / 网 builder 2,165,807B，render 2,165,804B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 427，== 基线集 | SPILL 0，OBSERVE 425，== 基线集 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 224→225，页脚余量 46.2→46.2 | 同左 |
| G15a | pw 0，pi `·`×126 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 331.3px（基线 334.4） | 同左 |
| D37 | 39.2px（29.4pt），row y=394 end=1400.3（基线 85.1） | 同左 |
| P8 | 1376 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A，13 处）：head 25→24 同时修掉 HEAD TOO WIDE（426.4 → 约 409px）。

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| A P1-headline 流 | `content12.py:40–45`、`56/58/60/62/64/66`、`54` | para 24 / ex 19.5 / head 25 | para 22 / ex 18.5 / head 24 | FLOW need 99px；HEAD +3.9px | run2 流止 y=1165，余 663px；HEAD 0 |

### 2026-w46-ko-it（读者 it）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 30,530,228B / 网 builder 2,145,400B，render 2,145,406B | 印 30,530,253B / 网 builder 2,145,426B，render 2,145,424B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 442，== 基线集 | SPILL 0，OBSERVE 438，== 基线集 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 234→235，页脚余量 50.4→50.4 | 同左 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 335.6px（基线 340.0） | 同左 |
| D37 | 110.1px（82.6pt），row y=394 end=1329.4（基线 151.3） | 同左 |
| P8 | 1356 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A，13 处）：同 de（`content12.py:40–45`、`56/58/60/62/64/66`、`54`；24/19.5/25 → 22/18.5/24；FLOW need 99px；run2 流止 y=1249，余 579px）。

## §3 ja / nl / pt

### 2026-w46-ko-ja（读者 ja）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 36,107,246B / 网 builder 2,602,310B，render 2,602,309B | 印 36,107,285B / 网 builder 2,602,348B，render 2,602,347B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 420，== 基线集 | SPILL 0，OBSERVE 417，== 基线集 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 200→201，页脚余量 48.9→48.9 | 同左 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 60，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 370.4px（基线 374.9） | 同左 |
| D37 | 263.3px（197.5pt），row y=372 end=1176.2（基线 262.0） | 同左 |
| P8 | 1812 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A，13 处；ja 行号偏 −1）：`content12.py:39–44`（para 24→22）、`55/57/59/61/63/65`（ex 19.5→18.5）、`53`（head 25→24）；FLOW need 99px；run2 流止 y=1165，余 663px。

### 2026-w46-ko-nl（读者 nl）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 30,531,603B / 网 builder 2,146,739B，render 2,146,739B | 印 30,531,643B / 网 builder 2,146,777B，render 2,146,787B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 435，== 基线集 | SPILL 0，OBSERVE 431，== 基线集 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 227→228，页脚余量 59.9→59.9 | 同左 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 360.6px（基线 365.1） | 同左 |
| D37 | 12.9px（9.7pt），row y=394 end=1426.6（基线 65.5）；实墨 **+6.8px**（run1/run2 同——最紧的过关余量，见 D41 节） | 同左 |
| P8 | 1325 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A，13 处）：同 de；run2 流止 y=1249，余 579px。

### 2026-w46-ko-pt（读者 pt）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 30,541,201B / 网 builder 2,156,721B，render 2,156,719B | 印 30,541,259B / 网 builder 2,156,779B，render 2,156,785B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 437，== 基线集 | SPILL 0，OBSERVE 436，== 基线集 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 234→235，页脚余量 47.7→47.7 | 同左 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=2（无 pt 读者表，D27；仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 346.8px（基线 350.1） | 同左 |
| D37 | **−3.6px**（−2.7pt），row y=394 end=1443.1（基线 48.3）——名义已越线；实墨 −14.5px，见 D41 节 | **25.6px**（19.2pt），row y=394 end=1413.9；实墨 **+17.2px** |
| P8 | 1362 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A 13 处 + D 1 处 = 14 处）：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| A P1-headline 流 | `content12.py:40–45`、`56/58/60/62/64/66`、`54` | para 24 / ex 19.5 / head 25 | para 22 / ex 18.5 / head 24 | FLOW need 99px | run2 流止 y=1165，余 663px |
| D P1 副刊头行 y=394 | `content12.py:20` | 16 | 15 | 名义 −3.6px；实墨越右栏线 **−14.5px** | run2 实墨余 **+17.2px**；名义余 25.6px |

## §4 ru / zh-tw

### 2026-w46-ko-ru（读者 ru）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，**FLOW 1**（同 de，need 99） | TOTAL 150，FLOW 0，HEAD 0 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0），noto_sans_elements **1050**（D26 旧分支预期值） | 同左 |
| G4/G5 | 印 30,712,200B / 网 builder 2,324,679B，render 2,324,670B | 印 30,712,215B / 网 builder 2,324,690B，render 2,324,685B |
| G6 | **flags 7**（P1） | flags [] |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 451，== 基线集 | SPILL 0，OBSERVE 447，== 基线集 |
| G12 | **DEFECT 1**：P1 `숫자로 보는 이번 주　Неделя в цифрах` fs 23，over **+14.7px**，core −22.0px（D5 回归；基线 OBSERVE +10.5） | DEFECT 0，OBSERVE 0 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | **defects 1**（同源盒），observes 0 | defects 0，observes 0 |
| G15a | pw 0，pi `·`×127 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 330.1px（基线 334.1） | 同左 |
| D37 | 65.7px（49.2pt），row y=394 end=1373.8（基线 73.0） | 同左 |
| P8 | 2642 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（A 13 处 + C 1 处 = 14 处）：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| A P1-headline 流 | `content12.py:40–45`、`56/58/60/62/64/66`、`54` | para 24 / ex 19.5 / head 25 | para 22 / ex 18.5 / head 24 | FLOW need 99px | run2 流止 y=1249，余 579px |
| C P1 box 标题 `숫자로 보는 이번 주　Неделя в цифрах` | `content12.py:53`（`f.box` 收尾行 `], tsize=20)`，D19） | tsize 23（默认） | tsize 20 | boxtitle +14.7px（creambox 同源缺陷） | run2 标题改单行，墨右 ≈920.1，框右 961.0，余 **≈41px**（流缩短后盒位移至 col 2，y=1219.34） |

ru 按 D26 旧分支（Latin AND Cyrillic → Noto Sans；fix-xru 是 W47-only，绝未引入）。

### 2026-w46-ko-zh-tw（读者 zh-tw）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，FLOW 0，HEAD 0 | 同左 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 32,027,360B / 网 builder 2,596,037B，render 2,596,049B | 印同 / 网 builder 2,596,046B，render 2,596,037B |
| G6 | flags [] | 同左 |
| G7/G8 | 150/150；CLEAN keydiff [] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 399，== 基线集 | 同左 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 200→201，页脚余量 48.9→48.9 | 同左 |
| G15a | pw 0，pi `／`×8 + `·`×127 + `—`×1 + `/`×8，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 61，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 370.4px（基线 374.9） | 同左 |
| D37 | 255.6px（191.7pt），row y=366 end=1183.9（基线 252.3） | 同左 |
| P8 | 1847 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：无（0 处）。P1-headline 流本已合身（流止 y=1426，余 402px），无可修项。zh-tw 字体面问题见 §0.3（报协调员裁定）。

## §5 core-ko（读者 zh-cn）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **False**（仅 G15a） |
| G1 | TOTAL 150，FLOW 0，HEAD 0 | 同左 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0（total 0） | 同左 |
| G4/G5 | 印 31,975,939B / 网 builder 2,471,236B，render 2,471,237B | 印同 / 网 builder 2,471,235B，render 2,471,237B |
| G6 | flags [] | 同左 |
| G7/G8 | 150/150；CLEAN keydiff [] | 同左 |
| G9/G10 | freeze 8/8；cjk_added {}，latin_added 0 | 同左 |
| G11 | SPILL 0，OBSERVE 399，== 基线集 | 同左 |
| G12 | DEFECT 0，OBSERVE 0 | 同左 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 0，p8rows 200→201，页脚余量 48.9→48.9 | 同左 |
| G15a | pw 0，pi `·`×118 + `—`×1，**pdfdiff DIFF** | 同左 |
| G15b | rc=1（仅记录） | 同左 |
| G15c | ADOPT（REWRAP 60，TRIM 1） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 370.4px（基线 374.9；回填值，见 §0.8） | 同左 |
| D37 | 255.6px（191.7pt），row y=372 end=1183.9（基线 252.3） | 同左 |
| P8 | 1854 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：无（0 处）。P1-headline 流本已合身（流止 y=1426，余 402px），无可修项。

## §6 core-ko 交叉核对——(ko, zh-cn) 由 core-ko 构建

1. **production 无 `2026-w46-ko-zh-cn` 目录**（`production/2026-w46/` 下仅 10 个读者目录 + `core-ko/`）。
2. **fanout zh-cn 目录即 core 构建目录**（`fanout-2026-w46/zh-cn/`）。
3. **已发 (ko, zh-cn) 实测**（fitz 读 issues/ PDF P1）：标语 `매주한국어로· 每周一期· 한국사람이읽는한국어를읽어요`（y=50.7pt）、徽章 `한국어판· VOL.3 · 김장· 수능· 11월11일`（y=213pt）、副标 `한국어를배우는사람을위한주간신문— 진짜한국을, 한국어로`（y=262.5pt）——与 core-ko 的 P1 字符串一致（core 基线 P1 SVG 含徽章 `한국어판` 与页脚 `Lucerna　韩语周报 VOL.3　LUCERNA KOREAN WEEKLY`）；y 偏移差（350px vs 372px）为 pre-§1.1 与 §1.1 版式位移。
4. **Closer 同步方向：patched core-ko → production/core-ko；绝不新建读者目录，绝不以 core 覆盖任何读者目录**（es/pt 前例）。

## D47——不适用：已发版 0 行 `###`

- 已发 text.md：11 版皆 **0 行 `###`**（各 8 行 `##`）。
- `textmd_ko.py`：0 处 `###`、无 24pt 阈值逻辑。
- 无行可丢，无补行。D47 通则（补行是 closer 落仓任务）本家不触发；交付 text.md 与 fanout `.new` 逐字节相同，按 D49 只核实、不补行。

## D41——G6 定性 + D37-sub 实墨复核

### G6：真缺陷，已修（非量测 artifact）

- run1 G6 9 版同型 7 旗标（皆 P1）：LINEX ×2（line box [87.4, 1843.4, 1862.6, 1844.6] 跨 `A2`/`6.` 的墨）；TEXTX ×5（`한능검` 叠 `바쁜` 46.0×4.0px、`한` 4.7×4.0px；`정기` 叠 `한` 13.5×4.0px；`바쁜` 叠 `닫혀요` 46.0×10.7px；`한` 叠 `닫혀요` 4.7×10.2px；ru 变体 4.0/14.2）。
- 定性依据：基线同位 0 旗标（D5 回归），且与 G1 FLOW OVERFLOW 同根（P1-headline 流溢出后内容挤入下行）。流修复后 run2 G6 全版 0 旗标。本轮无 W45 ru 式正体字宽量斜体、亦无 W46 fr/ja 式 creambox 行匹配误判的 artifact 案例。

### D37-sub 实墨复核（任务指定 pt/es，另加 nl/de/fr 对照）

- 方法：3× 渲染实墨（300dpi 级），副刊头行行末墨 vs 右栏左缘 1439.5。名义 `text_w` 低估真墨约 1–11px。
- run1 实墨：pt **−14.5px**、es **−5.8px**（皆真越线——es 名义 D37 曾 PASS（+3.5px），正是任务要求实墨复核的原因）；nl +6.8px（最紧的过关值）；de +42.2、fr +32.8、it +101.8、ru +64.8、en +51.5。
- run2 实墨（修复 D 后）：es **+23.5px**、pt **+17.2px**、nl +6.8px（未动）、de +42.2、fr +32.8。修复 D 已验。
- nl D37-sub 实墨仅 +6.8px：过关，无动作，记在案（§10）。

## §7 内容抽查——双向 11/11（唯已知 R1 缺口除外）

- 方法：每版 3 个短内容探针（韩语词 + 读者语词 + 读者词），双向核对（text.md → 网 PDF 文字层；网 PDF 文字层 → text.md），空白归一（`·`→空格、`／`→`/`、U+3000→空格）。长行探针与页脚家具行不作探针（长行在 PDF 中换行、家具行 PDF 独有，皆为探针构造问题，非内容问题）。
- 结果：core/ja/zh-tw 3/3 双向通过；de/en/es/fr/it/nl/pt 的韩语词与读者语 kimchi 词双向通过，第三探针（读者词 `Alle`/`All`/`Todos`/`Tous`/`Tutti`）**复现已知 R1 缺口**：在 PDF 文字层有、在 text.md 无——即 §0.1 的 D39(3) 缺口，非新缺陷；ru 探针 `김장`/`кимчи`/`Все` 3/3 通过（初版探针误拼 `кимчхи`，已纠正——ru text.md 中为 `кимчи` 2 处、`Все` 1 处）。
- 另：zh-tw 初版 new→old "失败"为已知的 `·` vs U+3000 分隔符差异，非内容差异。

## §8 同步清单（patched/ vs production/2026-w46/）

每版同步（11 版同型）：

| 类 | 文件 |
|---|---|
| 8 个源文件（行差见下） | `svglib.py`、`bslib4.py`、`content12.py`、`content34.py`、`content56.py`、`content7.py`、`content8.py`、`render.py` |
| KIT | `WEEKLY-KIT.md`（已追加 D5 节，见 §10） |
| text.md | `<slug>.text.md`（以 patched `.text.md.new` 替换——生产版为旧引擎导出，差 246–250 行旧分隔符） |
| 7 个图文件（fanout-2026-w46 `assets/`） | `apples.jpg`、`autumn.jpg`、`baseball.jpg`、`bukhansan-ui.jpg`、`lucerna-moth.svg`、`ssam.jpg`、`study.jpg`（生产 `assets/` 仅有 CREDITS.md；**勿用 W47 的同名图**——`git ls-files` 显示其在 `production/2026-w47/` 下，但为 W47 故事图，内容不同） |

- 相同、无同步：`run.py`、`ABSTRACT.txt`、`supp_*.py`、`transform-w45.py`。
- 不同步（构建产物）：`svg/`、`cards/`、PDF、run 日志、`__pycache__`。
- 每版 8 文件总行差：core 1058、de 1100、en 1100、es 1096、fr 1094、it 1100、ja 1098、nl 1096、pt 1100、ru 1098、zh-tw 1070。de 分文件：svglib 431、bslib4 111、content12 215、content34 102、content56 106、content7 62、content8 52、render 21。
- D54 render.py：生产 11 版皆有 render.py，皆为死路径（BASE 指向仓外 `files/weekly-report-w46-ko-*` + 裸印名 `Lucerna-VOL3.pdf` + 无 webpdf 调用——grep 命中 "webpdf" 仅为 docstring 提及）；fanout 版为 ED-相对（`BASE = os.path.dirname(os.path.abspath(__file__))`）+ 后缀印名 + 内调 webpdf。11 版皆同步 fanout 版。

## §9 SHA 总表（run2，2026-11-16 实测；文件在 `patched/<dir>/`）

印名：core `Lucerna-VOL3.pdf`；读者 `Lucerna-VOL3-<DE|EN|ES|FR|IT|JA|NL|PT|RU|ZHTW>.pdf`。网-render：`Lucerna-VOL3-<XX>-web.pdf`（core `Lucerna-VOL3-web.pdf`）。网-builder：`<slug>.web.pdf`。text：`<slug>.text.md.new`。render-网与 builder-网差数字节（render 内调 webpdf.py，builder 另调一次）——皆有效；KIT pin 块列印 + render-网 + builder-网 + text.md。

| 版 | 印 PDF（字节 / SHA-256） | 网 PDF render（字节 / SHA-256） | 网 PDF builder（字节 / SHA-256） | text.md（字节 / SHA-256） |
|---|---|---|---|---|
| core-ko | 31975939 / `96b6066de48958c94cb760edb6c015bba0f171682ef39f75994dc9c949a4f299` | 2471237 / `33c9619f62539e61c0e7b6c8ddf17089ddd3e66b9619271d590d075f54fa4e00` | 2471235 / `554b8fff15ee932a72430f188b4ad4fa4fb69934dff46ed5858b5a1d1eaac197` | 27222 / `ae7d12408941dee4727144c847de8bae42168cf84a6f81a15420287946b09459` |
| de | 30536939 / `1fd02eefe4ee5310c2617c9fdf8249c90860e0d1f2d3cde106ec8e0d343595fa` | 2152574 / `dbaec7289d8b20c7f05846ec852ff69ffeda2d96ccf738a0b1b44ca65441c91b` | 2152579 / `b113a780186bdfcf4ef2bf6160934325f2ef4ee8cf21df8f38269849b9bbb911` | 27917 / `a8e67ef62e6fb0420ea07b71d8a40f9eba1b441bb231cd6b29efb941ab64d6cc` |
| en | 30545245 / `34d8b63716a951c647c453005ee54f10cbce8c7b66726cec16057ab5bc84866e` | 2161518 / `8f2ef5e096af867ec1a63a7af5c0342bab10bec9a073d474a72d2e663af3a475` | 2161518 / `d9ae6216add581aa40bb3e39e4cda9d5c0090f4588f81aa94ddcc4988ca311c7` | 27748 / `f93e7100c669fa1b72e6052e220ca6ee2ef5fba611a2cc6c8d93802273062c39` |
| es | 30538370 / `79d3a25bea55842d0c214a816c42c0b67e6568722f805ab328d074edefba3acb` | 2153948 / `5af73b746f5eb411ee0a704efce6903744612114c3ac4cbcb034f9ee46a5002c` | 2153952 / `53b40a6508facaf942cd4fe64a1436869bffe715403c6d2c7e32c9bdea712c00` | 28053 / `f5c2dd38a6894012d1ef733116bdfce8e04f93ac5204e2403c244a785dc9bfad` |
| fr | 30549796 / `d53fe4f0a5a334c411d104ef801f66cab380912ad24e167ef96846b3d768d781` | 2165804 / `9dff768f19730f6073547c5bc8b9301440534dae20054958578e750f03782684` | 2165807 / `95a5baeec545c342b0020e9747a4bc2e9b0886509722cff181930ada72f1c3c6` | 28079 / `d7074cd255d8e94f4f297c4d47639858f457545689635805674cb4ad7e2e7910` |
| it | 30530253 / `741f1ab904857786bff1a8c06979893799c5ed6f69b8fcbd1aaf3048466a9616` | 2145424 / `98bcb40b51a14de729c620fe1a1d5f6863b3f5de7fa80246f20ee6efebcc0014` | 2145426 / `9b1c7889a62da47aa32065aecb89014d8954d58eb778ed7a8ea3f89faf7dfc06` | 28031 / `3a887581cc9f1ac3dfbd93a736bc0146bc8d5a2236299ed3ecde513b013e5f03` |
| ja | 36107285 / `dc871eaa923c38b814a30ff651799c28e62cd8cd2fe6c36fb2c7b07bed0ef08f` | 2602347 / `89479f88dad9343557042d91be0aacd9492129fedf7a8cc54c0d40dde5cd9c48` | 2602348 / `ccf14226c5b90eb1bda5733f3bc75b921544e4e47fee3f20215a63954a0b63de` | 28041 / `5d7a4c94480daa1339a439616fb027f0fcdd3f615d56dbbdfe8337f120aa7720` |
| nl | 30531643 / `f70a5afd5cc88cb21979fd68e4f5c26952c4db837787e2403afee5c1371b1f36` | 2146787 / `1cfd76b81a9da304b30eca6c7ee35995d238aaef60921b7ead60def0598aea53` | 2146777 / `bc3ac3ce84dd99b275e9b0bc7f2163c9c02b5646a13e408234c7624ac0b869b6` | 27897 / `dafd27b0fb7b748c58521151d0397f2f5810a895861b73d9adb900d5aedd9cea` |
| pt | 30541259 / `e71861658e0a7e3da669b382fc54f83096b8c05a86c500aee7571aba9de80b45` | 2156785 / `8bdd2ceeb52ab131260ec62cd1567f6e2154dd9e92b95d2232e6a950df16d2ae` | 2156779 / `5496bc97cc9feec62bb4c7ed602295e094504d79d3d44f2130a0ef0d51dd5794` | 28056 / `7cca4b7ff513662288a4dd081d5bfbbc2a611c82547a1162c96278fb61765acd` |
| ru | 30712215 / `d097ec30766c638c315e0abc62109310f38c51eb4be4a243c72428142b3cf73b` | 2324685 / `b37e84827d86a307a3c19537e1e3b8be0b862d48a36045829c38cc4a508cc528` | 2324690 / `8eae425afc76a03bf58a8d6373c1040a292323e2b9a6ba86cbe425db5ec8fb7f` | 30131 / `1cbba2f1ffd110c4257ecde393c324310a5bb9615a33a767bc45cabcbfa0c1da` |
| zh-tw | 32027360 / `929363c9102d178264e17c65c8a5f826ba61449990eea311dee0fdae7bed726a` | 2596037 / `074d51794b21c5e5a1140bf6afa83e0e942af9d7fc541212fed75477d41f7eaa` | 2596046 / `a1a6126589e60ce306ef602f3e2ae3e9787659e9f7f50ae7ec8de69beab7294e` | 27298 / `92f6473216072e3566b68595271973f8868b5faf290e3f80842c251407cc5ea3` |

## §10 closer 交接

- **结论**：严格门禁计数 0/11 ALL-GREEN；10/11 run2 18/19（仅 G15a FAIL），fr 17/19（G15a + G2 门禁计数 artifact）。可修缺陷全清（run1：G1 FLOW 9 版、G6 7 旗标 ×9 版、G12 DEFECT en/ru、G14 DEFECT ru、D37 pt −3.6px——run2 皆清）。修复 121 处（9 文件：A 13 处 ×9 版 = 117，B/C/D 各 1 处），只降字号，不改文案。
- **KIT 已更新**：11 版 patched KIT 皆已追加 `## 补记：D5 字体重建（2026-11-15）` 节（pin 块 + 重建节），各恰 1 节，无重复追加。单向 patched → production，绝不反向覆盖。生产 KIT 尺寸/sha16（2026-11-16）：de 13611 `76f359552b552313`、en 13301 `59dbe12123513e4b`、es 14017 `682498fa9645aa73`、fr 13279 `69a9bf510fb89d5a`、it 13584 `5ca8009850366924`、ja 14297 `d2b716cc39589f9f`、nl 13604 `68611ada07a8ba17`、pt 13972 `27459738be45150b`、ru 14861 `555c37b90ae1af45`、zh-tw 14595 `db7d8ab9180fd512`、core-ko 32245 `d822d4671a294ea2`。
- **D19：PASS**。全家仅 1 处生产 KIT 含 `content*.py:NNN` 引用（zh-tw `content56.py:125` → `f.gloss("재다 衡量 · 규모 規模 · 섞다 混淆。")`，恰为修复行本身，patched 与生产文件皆已核实）。本报告内全部 `content12.py:NNN` 引用皆指向修复行本身（para 40–45、ex 56–66 偶数、head 54、box 收尾行 en 202 / ru 53、y394 行 20；ja 偏 −1）。
- **需协调员裁定的事项**：
  1. **zh-tw 字体面**（§0.3）：已发 TC-only，D5 模板 KR-only。builder 已按模板装机（ja 先例），不得自默决定——裁定：接受 KR 面落仓，或另行设计 TC 分支。
  2. **G15a pdfdiff**（§0.5）：模板 BLANK 机制致网 PDF 文字层丢 `_`（run1 core 每页仅旧侧 `[('_', N)]`）。builder 不重设计模板——裁定：接受为模板行为落仓，或模板另修后重跑。
  3. **fr G2 门禁计数 artifact**（§0.5）：交付侧干净（G1 HEAD 0），门禁因冻结基线日志计 1。不得改门禁——裁定：接受 17/19 落仓。
  4. **nl D37-sub 实墨仅 +6.8px**（D41 节）：过关，无动作，仅记在案。
- **Closer 待办（按序）**：
  1. 按 §8 同步 11 版（8 源文件 + KIT + text.md + 7 图文件/版）；core-ko → `production/core-ko`，**绝不新建 `2026-w46-ko-zh-cn`**。
  2. 全家一个目标语 = 一个 bundle，按 W46 ja 先例（closer `d5d1f782`）一次落仓；推后核对 §9 SHA。
  3. D29 复本已备（本报告 + 11 份 run2 GATES-SUMMARY，`notes/g-ko/scratch-d5-rebuild-ko/`，cmp 核对）。
- **磁盘**：收尾 `/home/hatch` 74G/150G（50%），门内（≥100G 才停手）。scratch 1.3G。
