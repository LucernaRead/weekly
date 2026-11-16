# W46 日语目标家族 D5 重建报告

- 家族：W46 ja（目标语 ja，读者 de/en/es/fr/it/ko/nl/pt/ru/zh-cn/zh-tw；无 ja 读者）+ core-ja
- 周次：2026-11-09 → 2026-11-15（VOL.3，W46，2026-11-16 到期）
- Builder 工作目录：`hidden_files/d5-redo/scratch-2026-w46-ja/`（`baseline/`、`patched/`、`logs/`、`bin/`、`backup/`）
- 结论：**11/11 run2 ALL-GREEN**（G15b 除外，D27）。修复 15 处（F1 ×11、F2/F3/F4/F5 各 1），只降字号，不改文案。
- 本报告 + GATES-SUMMARY 复本另存 `hidden_files/d5-redo/notes/g-ja/scratch-d5-rebuild-ja/`（D29，cmp 核对）。

## §0 方法

### §0.1 导出器核实（步骤 0，P3b）——ADOPT

- 导出器：`hidden_files/style-port-ja/textexp_ja.py` + 原生校验器 `verify_textexp_ja.py --edition`。用法：`textexp_ja.py <edition-dir> <slug> <out.text.md.new> 2026-11-09 2026-11-15`（import 时读 `assets/lucerna-moth.svg`，试跑须带 `assets/`）。
- 试跑（`logs/step0/`）：**11/11 导出 rc=0，试跑输出与 fanout `.text.md.new` 逐字节相同**（条目数 de 1332、en 1324、es 1339、fr 1333、it 1335、ko 1309、nl 1336、pt 1339、ru 1343、zh-tw 1304、zh-cn 1307）。原生校验器 vs `issues/` text.md：**11/11 ADOPT（0 UNEXPECTED，FURN 0，OTHER 0）**，rc=0。
- **但与 `issues/` text.md 不是逐字节相同——这是设计使然，不是失败**：`issues/` text.md 是旧引擎导出（与 fanout 旧拷贝 `2026-w46-ja-de.text.md` 逐字节相同，sha `294d9239…`，git 最后改动 2026-11-04），用 ` · ` 分隔符（0× U+3000、252× ` · `）；移植导出用 U+3000（124× U+3000、129× ` · `）并重排。校验器分类：SEP 约 55–65、CJK 1–7、FURNOK 0–7、REWRAP 约 232–248/版。因此“text.md 与 issues/ BYTE-IDENTICAL”这一基线标准**对 W46 ja 不成立**；正确的基线证明是：基线导出 == fanout `.new` 逐字节相同 + 原生校验器 ADOPT + `pdf_text_diff_ja.py` 对 issues/ PDF 为 IDENTICAL（见 §0.4）。
- D47：已发 W46 ja text.md 含 **0 行 `###`**（11 版全是 0）；`textexp_ja.py` 完全没有 `###` 逻辑（grep `###` 与 `24` 均 0 命中）——D47 的 `###` 行丢失对 ja **不适用**（逐版核对见 D47 节）。

### §0.2 D1 定性（步骤 0.2）——D1+D5 一次做

- 生产 `2026-w46-ja-*/svglib.py` + `core-ja/svglib.py`，11/11：**D1 fix 0 处、Newsreader 0、`_D5_READER` 0、`_char_font` 0** → pre-D1 旧样式。生产 svglib sha `acc102ad…`（≠ manifest）。
- Fanout `fanout-2026-w46/<reader>/svglib.py` + core，11/11：**D1 fix 1 处、Newsreader 8、`_D5_READER` 0、`_char_font` 3** → 新样式（§1.1 移植）+ D1 fix，无 D5。装机自 fanout 即带 D1；重建为 **D1+D5 一次做**（与 W45 ja、W46 fr/it 先例相同）。
- Patched svglib 来源：`hidden_files/d5-redo/tools/mechanism-w47/svglib-ja-d5.py`（517 行，JP subscript、kinsoku 块、`_D5_READER = "latin"` 默认），**与 W47 production `core-ja/svglib.py` 逐字节相同**（install.py 实测）。其 `Page.text`/`para`/`text_w`/`wrap` 不取 `face` 参数；kinsoku 块无 `face` 引用 → 无 W45 ru F-1 式 `face` 参数 bug（自查通过）。
- D1 逆向核对：`d1_fix_ja.py` PATCH_OLD/PATCH_NEW；从 fanout svglib 剥离规范 §2a hunk 后复现 manifest pre-D1 SHA `708daaf6…`——装机时 11/11 MATCH。
- 装机核实（`logs/install.log`、`logs/install.json`）：11/11，`_D5_READER` 均在 `svglib.py:122`（latin：de/en/es/fr/it/nl/pt；ru：`"ru"`；cjk：ko/zh-tw/core-ja）；与模板 diff：latin 版 0 行、cjk/ru 版 11 行（unified-diff hunk 行数，实质只改 `_D5_READER` 一行）；fix2 提及 6 处、`_QUOTE_CLS` 4 处、kinsoku `NO_START` 在位；逐版路由抽查通过（Latin→news，ru→sans_noto；西里尔→sans_noto；fix2 引号 U+201C/U+201D/U+2019→news；CJK→sans；serif Latin→news）；`py_compile` 全过；机制 `test_d5_routing.py` **FAILURES: 0**。

### §0.3 zh-tw 字体面核实（步骤 0.3，D52 教训）——已发 TC，模板 JP，已报协调员

- 生产 `2026-w46-ja-zh-tw/svglib.py`（旧）：`_sc_index` + `_tc_index` 均定义；`_font(..., face="JP")` 默认；`_IDX`（SC）+ `_IDX_TC`。
- Fanout zh-tw svglib（移植）：`_jp_index` + `_tc_index`；`_IDX_JP` + `_IDX_TC`；族名 `Noto Sans/Serif CJK JP` 默认，`TC` 经 `face="TC"`。zh-tw fanout `*.py` 中 `face=` 100 处（content+bslib4 内 72× `face="TC"`，其余为 `face="JP"` 默认/透传）。
- 已发 PDF 嵌面：issues/ zh-tw 网 PDF 嵌 **JP 与 TC 双面**：NotoSansCJKJP Bold/Regular ×8、NotoSansCJKTC Bold/Regular ×8、NotoSerifCJKJP Bold/Regular ×8、NotoSerifCJKTC-Regular ×1。Fanout zh-tw 印 PDF（`Lucerna-VOL3-ZHTW.pdf`）：Newsreader 17 + NotoSansCJKjp Bold/Regular ×8 + NotoSansCJKtc Bold/Regular ×8 + NotoSerifCJKjp Bold ×7/Regular ×8 + NotoSerifCJKtc-Regular ×1。Core 印 PDF：仅 JP + Newsreader 17。Issues de 网 PDF：仅 JP + UnifrakturMaguntia（旧样式，无 Newsreader）。
- **不符**：已发 zh-tw 读者文本为 **TC 面**；D5 模板为 JP-only。按 W45 ja 先例处理：剥离 face → 读者文本按 JP 渲染；文字层相同；门禁无法检测字形变体差异。**已按任务令上报协调员**：governing rule 是“复现已发版的字体面”，已发为 TC 则应为 TC；机制 `base_core_for()` 规定 reader zh-tw 用 `core-zh-tw`（TC）作基底，但 D5 模板无 TC 分支，builder 不单方面重设计模板。W45 ja 同样剥离后两次重校通过。
- 剥离实测（install.py，`logs/install.json`）：content 文件 face kwargs **74 处**（`face="TC"` 63、`sub_face` 7——其中 5 处与 `face="TC"` 同行、`title_face` 2、`body_face` 2，另 1 处 `sub_face="JP"` p.band p8）+ bslib4 24 处精确替换 + 4 处残留 `, face="TC"`；剥离后 code 内 `face`/`sub_face`/`title_face`/`body_face` 标识 0 处；`py_compile` 全过。注：计数曾两次纠正（初版断言 68——实为 63+5 命名 kwargs 的合计数；`sub_face` 初计 1，实为 6——5 处藏在含 `, face="TC"` 的同行内；末尾发现 `sub_face="JP"` 1 处），最终以正则全量计数 74 为准。
- ko 面按 D53：SC→KR 是机制规定的 D5 行为，接受、不质疑。ja 面 SC→JP 与已发 JP 面一致，核实通过。

### §0.4 基线（步骤 1）——CLEAN（除 3 项先存记录）

基线 = fanout 装机 + 全套门禁（`logs/baseline-gates/`、`logs/baseline-summary.json`、`logs/baseline-spill/`）。11/11：

| 项 | 基线值（11 版一致处） |
|---|---|
| run | TOTAL 150，FLOW 0，HEAD 0 |
| text.md | 与 fanout `.text.md.new` 逐字节相同（de 46,226；en 45,422；es 46,993；fr 46,906；it 46,769；ko 47,808；nl 46,027；pt 46,817；ru 53,501；zh-tw 44,018；zh-cn 44,047 字节） |
| PDF 文字层 | `pdf_text_diff_ja.py` + trim（`「千歳飴（ちとせあめ）」—` → `「千歳飴（ちとせあめ）」`）vs issues/ PDF：**IDENTICAL，rc=0**，8/8 页 |
| SVG | 8/8 与 fanout SVG 逐字节相同（最强基线证明） |
| p8 | extract 150/150；compare CLEAN，keydiff [137, 138]（zh-tw [138]，core []——core 即参照本身） |
| G15c | ADOPT（0 UNEXPECTED），11/11 |
| G15a 多重集差 | 印=网 0；vs issues 差 125 = `·`×124 + `—`×1（zh-tw/zh-cn：141/132，另含 `／`×8 vs `/`×8——移植分隔符改动，见下） |

- vs issues 多重集差的解释（已实测分解）：旧 PDF 文字层含 `·`（移植版为 U+3000，空白归一后消去）124 处 + 周词行尾 ` — ` 1 处；zh-tw/zh-cn 另有 `／`（移植）vs `/`（旧）8 处。`pdf_text_diff_ja.py`（带 trim）判 IDENTICAL，内容无差。
- D5 普查（基线，`d5_census.py` totals）：Latin in CJK de 401、en 397、es 400、fr 400、it 401、ko 216、nl 399、pt 401、ru 210、zh-tw 204、zh-cn 204；ru 另 Cyrillic in CJK 218；curly_total 0，仅 zh-tw/zh-cn 为 2（curly_in_CJK 1）。
- 基线先存记录（D25 类，不修、不阻塞）：
  - **G11 spill 1/版**：P5 BELOW 17.74px，`の回答）によるものです。`（P5 归属行，框底 762.0，行 y=779.7），11 版同一行。Fanout 自身 `boxspill-*.log` 已裁定：0 port-introduced（旧版同坐标亦然）；OBSERVE 62–64/版。门禁口径改为“重建 spill 集 == 基线 spill 集”。
  - **G16 zh-tw 2**：p2 弯引号一对（U+201C×1、U+201D×1）在 Noto Sans CJK TC 面；D5 fix2 将其归 Newsreader，run2 已归 0。Core 同有 curly_in_CJK 1 但 G16 为 0（工具只计 TC 面）。
  - **P2 中页空白**：旧 29.2px → 新 83.3px 加宽，属已 reopen 的缺陷类（待 redesign），非 D5 发现，不修。
- 基线 D18 间隙 281.5–342.4px；D37 y612 余量 −1068.8…−1182.3pt；D37-sub 余量 −50.0…−290.1pt（core 无副刊头行，N/A）；P8 末行 y=2624.0，页脚余量 76.0px（11 版一致）。
- 基线印/网字节见 `logs/baseline-summary.json`（如 de 印 28,325,544 / 网 2,278,578；ru 印 24,247,620 / 网 2,188,190；zh-tw 印 26,664,496 / 网 2,789,194）。

### §0.5 门禁口径

- 19 verdict/版：G1–G14 + G15a/G15c + G16 + D18 + D37；**G15b 仅记录**（D27：共享 `verify_textmd.py` 对 ja 格式未校准；run2：9 版 rc=1 CARRYOVER FAIL，pt/zh-tw rc=2 无读者表——与 W45 ja 一致的已知工具缺口）。
- G15a：印=网多重集差 0（严格）+ `pdf_text_diff_ja.py`（带 fanout trim）vs issues/ PDF IDENTICAL；vs issues 多重集差只记录并分解（`·`/`／`/`—` 三类移植分隔符）。
- G11：重建 spill 集须 == 基线 spill 集（D25 先存几何，不以“0 SPILL”一刀切）。
- G3：普查 0 违规（census 省略 0 值键，解析以 0 补缺）；ru 另计 Noto Sans 元素（run2 711）。
- G10：CJK added 0；Latin added = D5 run-split 数（de 208、en 214、es 207、fr 210、it 212、ko 92、nl 208、pt 210、ru 81、zh-tw 80、core 88）。
- G14：creambox defects 0；p8 行数因 run-split 增加（见各版），页脚余量不变；advance ratio 中位 1.009–1.014、粗体中位 1.04（Newsreader 较 CJK 面宽约 4%，D5 固有）。
- D18：刊头标语行间隙，内容识别（含 “2026” 的日期行），绝不硬编码 y。D37：徽章行余量，内容识别实际行（y∈[600,625]），绝不硬编码 y=612（D39(5)）；D37-sub：副刊头行（y∈[350,362]）末尾 x vs 右栏左缘 1439.5。
- P8：`<text>` 元素数 + max y；11 版 max y 均为 2624.0，余量 76.0px。

### §0.6 工具注记

- 门禁脚本 `bin/gates_ja46.py`（`bin/gates-baseline.sh` / `gates-run1.sh` / `gates-run2.sh` / `gates-run2-resume.sh`）。本轮修过的脚本缺陷（均在基线轮后、run1 前修好；循环运行时不改脚本）：
  - spill/boxtitle/edge 三工具共用 `--json-dir` 时同名 `<slug>.json` 互相覆盖——改为各用子目录（`spill/`、`boxtitle/`、`edge/`）。
  - census/creambox/p8-extract/head-check 的 JSON 键名与初版解析不符——改读 `totals` 字典、`noted_set` 长度、`findings` 长度。
  - G16 把 TOTAL/GRAND TOTAL 行重复计入——只加总逐页 `pN-*.svg: defective=N` 行（zh-tw 基线 6→实 2）。
  - G15b 未传 `--reader` 致 rc=2——补传读者码（core-ja 传 zh-cn）。
  - D37-sub：core-ja 无副刊头行（pass null）——按 N/A 计，不判 FAIL。
  - G11：spill JSON 文件名取版目录 basename（core-ja，非 slug）+ spills 为 None 时的集合差守卫。
  - G3 显示：census 省略 0 值键——缺省补 0。
  - freeze build-copy 每版 41M——G9 后删除，只留日志 + JSON（基线轮 11 份已手动清）。
- `bin/apply_fix.py`：精确旧行 + 行号双重校验 + 文件内唯一性（`], tsize=22)` 类通用行改用 `context_above` 校验）+ `ast.parse`/`py_compile`；`size_only` 初版按字符对齐，在 `25`→`23.5`（共享首末数字）上误判——改写为“数字归一后全等且仅一处数字不同且为 5–60 的字号值”。
- `bin/install.py`：zh-tw 计数断言两次纠正（见 §0.3）；其余 10 版一次通过。
- `bin/build-one.sh`：run.py → render.py（内调 `tools/webpdf.py` 生成网 PDF）→ `textexp_ja.py`，venv python。

### §0.7 几何常量

- 页 1950×2700；RIGHT=1862（右栏右缘）；MX=88；CW=422.5；GUT=28；COLX=[88, 538.5, 989, 1439.5]；页脚线 y=2596；页底 2700。
- 刊头预算 CW=422.5；p.text 盒标题预算 400.5（x=bx+22 起，右缘 1862.0）；f.box 标题预算 404.5（x=box.x+18 起，右缘 box.x+422.5）。
- 刊头结构（fanout de P1 实测）：y=92 行 VOL.3（x=88）/ 标语（x=695.4）/ 日期（x=1557.8）；标题行 y=316；副刊头行 y=356；规则线 y=420 至 x=1862.0。

### §0.8 事故

1. **run1 构建驱动参数顺序错**（00:0x）：`build-run1.sh` 误按 `build-one.sh <slug> <dir> run1` 调用（应为 `<dir> <slug> <logprefix>`），11 版全部 `cd: No such file or directory` rc=1。按基线脚本的正确顺序重写后重跑，11/11 rc=0/0/0。无文件损坏（构建未开始）。
2. **服务重启杀死 run2 门禁循环**（约 01:00）：it 版门禁跑到 G13/G14 处中断，循环进程死亡。按规从断点续跑（`bin/gates-run2-resume.sh`，it 起）；de/en/es/fr 四版已完成件沿用，it 重跑全套。续跑后 7 版全部 ALL-GREEN。
3. **install.py zh-tw 断言两次失败**（见 §0.3）：计数纠正后通过；其余 10 版未受影响（install 逐版独立，失败版重跑全量是幂等的）。
4. **run1 zh-cn G11 FAIL 为脚本 bug**（非真缺陷）：spill 文件名 + None 守卫问题（§0.6）；run1/run2 spill 集实测相同（P5 同一行），run2 已 PASS。

## §1 de / en / es

### 2026-w46-ja-de（读者 de）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **True** | **True** |
| G1 | TOTAL 150，FLOW 0，HEAD 0 | 同左 |
| G2 | defects 0 | 同左 |
| G3 | latin 0，cyr 0，curly 0 | 同左 |
| G4/G5 | 印 24,212,680B / 网 2,165,894B | 印 24,212,672B / 网 2,165,879B |
| G6 | flags [] | 同左 |
| G7/G8 | 150/150；CLEAN keydiff [137, 138] | 同左 |
| G9/G10 | 8/8；cjk_added {}，latin_added 208 | 同左 |
| G11 | SPILL 1，OBSERVE 94，= 基线集 | 同左 |
| G12 | DEFECT 0（OBSERVE 1：P1 信用行 +6.5，见 F1） | DEFECT 0，OBSERVE 0 |
| G13 | 0 TOUCH，0 NEAR | 同左 |
| G14 | defects 0，observes 1，p8rows 840→859，页脚余量 39.9→39.9 | defects 0，observes 0，余同左 |
| G15a | pw 0，pi 125（`·`124 + `—`1），pdfdiff IDENTICAL | 同左 |
| G15b | rc=1 CARRYOVER FAIL（仅记录） | 同左 |
| G15c | ADOPT（0 UNEXPECTED） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 297.9px（基线 303.2） | 同左 |
| D37 | y612 −1111.5pt，end 328.0；sub −55.4pt，end 1384.1（基线 −100.2） | 同左 |
| P8 | 867 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表（F1，W45 F1 先例：同行、同 +6.5px，W45 11 版同修）：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| F1 P1 信用行 `出典：各発表・予報の日付は記事の中にあります` | `content12.py:86` | 18.5 | 18.0 | boxtitle +6.5px（OBSERVE，先存于 core） | W45 同行同值验证；run2 boxtitle 0 DEFECT、G14 observes 0 |

### 2026-w46-ja-en（读者 en）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **True** | **True** |
| G1–G10 | 同 de 结构；latin_added 214；p8rows 835→854，页脚余量 47.2 | 同左 |
| G11 | SPILL 1，OBSERVE 97，= 基线集 | 同左 |
| G12 | DEFECT 0（OBSERVE 1：P1 信用行 +6.5） | DEFECT 0，OBSERVE 0 |
| G14 | defects 0，observes 1 | defects 0，observes 0 |
| G15a | pw 0，pi 125，pdfdiff IDENTICAL | 同左 |
| G15c | ADOPT（0 UNEXPECTED） | 同左 |
| D18 | gap 318.4px（基线 326.1） | 同左 |
| D37 | y612 −1136.6pt；sub −50.7pt，end 1388.8（基线 −96.4） | 同左 |
| P8 | 862 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：F1 同 de（`content12.py:86`，18.5→18.0）。

### 2026-w46-ja-es（读者 es）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **True** |
| G12 | **FAIL DEFECT 1**：P7 TITLE `Estructura semanal` fs 23.0，over **+2.8px**，core −22.0px（D5 回归） | DEFECT 0 |
| G11 | SPILL 1，OBSERVE 89，= 基线集 | 同左 |
| G14 | defects 0，observes 2，p8rows 848→867，页脚余量 41.1 | defects 0，observes 0，余同左 |
| G15a/G15c | pw 0，pi 125，pdfdiff IDENTICAL；ADOPT | 同左 |
| D18 | gap 291.3px（基线 296.8） | 同左 |
| D37 | y612 −1076.4pt；sub −8.0pt，end 1431.5（基线 −55.9） | 同左 |
| P8 | 875 元素，max_y 2624.0，余量 76.0px | 同左 |
| 其余 G1–G10、G13、G16 | PASS | PASS |

修复表：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| F1 P1 信用行 | `content12.py:86` | 18.5 | 18.0 | +6.5px（OBSERVE） | 见 de |
| F2 P7 盒标题 `今週のフレーム　Estructura semanal` | `content7.py:85`（p.text） | 23 | 22.5 | boxtitle +2.8px，右缘 1862.0 | `text_w` 探针：22.5 时余量 **+6.0px**（22.0 时 +14.7；取最大可过值） |

## §2 fr / it

### 2026-w46-ja-fr（读者 fr）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **True** |
| G12 | **FAIL DEFECT 1**：P7 TITLE `Clinique des erreurs` fs 23.0，over **+9.5px**，core −22.0px（D5 回归） | DEFECT 0 |
| G11 | SPILL 1，OBSERVE 92，= 基线集 | 同左 |
| G14 | defects 0，observes 2，p8rows 842→860，页脚余量 45.9 | defects 0，observes 0，余同左 |
| G15a/G15c | pw 0，pi 125，pdfdiff IDENTICAL；ADOPT | 同左 |
| D18 | gap 276.3px（基线 281.8） | 同左 |
| D37 | y612 −1149.5pt；sub −33.2pt，end 1406.3（基线 −78.3） | 同左 |
| P8 | 868 元素，max_y 2624.0，余量 76.0px | 同左 |
| 其余 | PASS | PASS |

修复表：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| F1 P1 信用行 | `content12.py:86` | 18.5 | 18.0 | +6.5px（OBSERVE） | 见 de |
| F3 P7 盒标题 `まちがい診療所　Clinique des erreurs` | `content7.py:73`（p.text） | 23 | 22 | boxtitle +9.5px，右缘 1862.0 | `text_w` 探针：22 时余量 **+8.3px**；22.5 仍 −0.6，不取 |

### 2026-w46-ja-it（读者 it）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **True** |
| G12 | **FAIL DEFECT 1**：P1 TITLE `Settimana in numeri` fs 23.0，over **+11.5px**，core −18.0px（D5 回归） | DEFECT 0 |
| G11 | SPILL 1，OBSERVE 91，= 基线集 | 同左 |
| G14 | defects 0，observes 2，p8rows 843→862，页脚余量 43.7 | defects 0，observes 0，余同左 |
| G15a/G15c | pw 0，pi 125，pdfdiff IDENTICAL；ADOPT | 同左 |
| D18 | gap 280.5px（基线 287.4） | 同左 |
| D37 | y612 −1067.3pt；sub −98.1pt，end 1341.4（基线 −139.7） | 同左 |
| P8 | 870 元素，max_y 2624.0，余量 76.0px | 同左 |
| 其余 | PASS | PASS |

修复表：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| F1 P1 信用行 | `content12.py:86` | 18.5 | 18.0 | +6.5px（OBSERVE） | 见 de |
| F4 P1 f.box 标题 `数字で見る今週　Settimana in numeri` | `content12.py:51`（f.box 收尾行 `], tsize=22)`，D19） | tsize 23（默认） | tsize 22 | boxtitle +11.5px，右缘 961.0（盒 [538.5, 989.9, 422.5, 326.0]） | `text_w` 探针：22 时余量 **+6.6px**；22.5 仍 −2.4，不取 |

## §3 ko / nl / pt

### 2026-w46-ja-ko（读者 ko）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **True** | **True** |
| G1–G10 | TOTAL 150；latin_added 92；p8rows 2213→2332，页脚余量 44.6 | 同左 |
| G11 | SPILL 1，OBSERVE 152，= 基线集 | 同左 |
| G12 | DEFECT 0（OBSERVE 1：P1 信用行 +6.5） | DEFECT 0，OBSERVE 0 |
| G14 | defects 0，observes 1 | defects 0，observes 0 |
| G15a/G15c | pw 0，pi 125，pdfdiff IDENTICAL；ADOPT | 同左 |
| D18 | gap 335.5px（基线 342.4） | 同左 |
| D37 | y612 −1165.4pt；sub −290.1pt，end 1149.4（基线 −287.3） | 同左 |
| P8 | 2353 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：F1 同 de（`content12.py:86`，18.5→18.0）。

### 2026-w46-ja-nl（读者 nl）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **True** | **True** |
| G1–G10 | TOTAL 150；latin_added 208；p8rows 845→864，页脚余量 41.2 | 同左 |
| G11 | SPILL 1，OBSERVE 90，= 基线集 | 同左 |
| G12 | DEFECT 0（OBSERVE 1：P1 信用行 +6.5） | DEFECT 0，OBSERVE 0 |
| G14 | defects 0，observes 1 | defects 0，observes 0 |
| G15a/G15c | pw 0，pi 125，pdfdiff IDENTICAL；ADOPT | 同左 |
| D18 | gap 305.6px（基线 312.5） | 同左 |
| D37 | y612 −1105.4pt；sub −27.9pt，end 1411.6（基线 −77.3） | 同左 |
| P8 | 872 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：F1 同 de（`content12.py:86`，18.5→18.0）。

### 2026-w46-ja-pt（读者 pt）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **True** | **True** |
| G1–G10 | TOTAL 150；latin_added 210；p8rows 847→866，页脚余量 39.9 | 同左 |
| G11 | SPILL 1，OBSERVE 92，= 基线集 | 同左 |
| G12 | DEFECT 0（OBSERVE 1：P1 信用行 +6.5） | DEFECT 0，OBSERVE 0 |
| G14 | defects 0，observes 1 | defects 0，observes 0 |
| G15a/G15c | pw 0，pi 125，pdfdiff IDENTICAL；ADOPT | 同左 |
| G15b | rc=2（无读者表，仅记录，D27） | 同左 |
| D18 | gap 291.8px（基线 297.4） | 同左 |
| D37 | y612 −1132.8pt；**sub −0.9pt，end 1438.6**（基线 −50.0）——PASS 但余量仅 0.9pt，见 §10 残留项 | 同左 |
| P8 | 874 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：F1 同 de（`content12.py:86`，18.5→18.0）。

## §4 ru

### 2026-w46-ja-ru（读者 ru）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **True** |
| G3 | latin 0，cyr 0，curly 0；Noto Sans 元素 711（西里尔已归 Noto Sans） | 同左 |
| G6 | **FAIL**：p8 TEXTX，`Ответы — сгруппированы по страницам; просто найди свой номер` 与 `Короткое пояснение на русском к каждому ` 重叠 **37.8×18.8px** | flags [] |
| G11 | SPILL 1，OBSERVE 93，= 基线集 | 同左 |
| G12 | DEFECT 0（OBSERVE 1：P1 信用行 +6.5） | DEFECT 0，OBSERVE 0 |
| G14 | defects 0，observes 1，p8rows 2378→2397，页脚余量 39.9；ratio_med 1.0，bold_med 0.956，reg_med 1.019 | defects 0，observes 0，余同左 |
| G15a | pw 0，pi 125，pdfdiff IDENTICAL | 同左 |
| G15c | **FAIL HOLD**：Page 8 TOKEN DIFF，only-old=[(`номер`,1), (`Короткое`,1)]，only-new=[(`номерКороткое`,1)]；UNEXPECTED 2 块 | **ADOPT（0 UNEXPECTED）** |
| D18 | gap 277.4px（基线 281.5） | 同左 |
| D37 | y612 −1068.3pt；sub −69.2pt，end 1370.3（基线 −76.9） | 同左 |
| P8 | 2397 元素（基线 2378），max_y 2624.0，余量 76.0px | 同左 |
| 其余 G1/G2/G4/G5/G7–G10/G13/G16 | PASS | PASS |

修复表：

| 修复 | file:line | 旧字号 | 新字号 | 越界量 | 探针余量 |
|---|---|---|---|---|---|
| F1 P1 信用行 | `content12.py:86` | 18.5 | 18.0 | +6.5px（OBSERVE） | 见 de |
| F5 P8 答题区眉题 `答え　Ответы — сгруппированы по страницам; просто найди свой номер` | `content8.py:114`（p.text） | 25 | 23.5 | G6 ink 重叠 37.8px + G15c 词元合并（D41 实测，见 D41 节） | occlusion_audit ink 探针（PIL/FreeType 真实墨宽）：23.5 时余量 **+15.5px**；24 仍 −2.3，不取 |

注：ru 第二信用行 `content12.py:87`（`Даты — в статьях; не точная статистика`，19px）run1 未报溢出，不修——与 W45 ru F2（同位置行 19→17.5，越界 +22.5）不同：W46 该行更短，D5 后仍在框内。

## §5 zh-tw / zh-cn

### 2026-w46-ja-zh-tw（读者 zh-tw）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **True** | **True** |
| G1–G10 | TOTAL 150；latin_added 80；p8rows 1225→1288，页脚余量 48.9 | 同左 |
| G3 | latin 0，cyr 0，curly_cjk 0，curly_total 2（已归 Newsreader 的弯引号，fix2 既定态） | 同左 |
| G11 | SPILL 1，OBSERVE 98，= 基线集 | 同左 |
| G12 | DEFECT 0（OBSERVE 1：P1 信用行 +6.5） | DEFECT 0，OBSERVE 0 |
| G14 | defects 0，observes 1 | defects 0，observes 0 |
| G15a | pw 0，pi 141（`·`124 + `／`8 + `/`8 + `—`1），pdfdiff IDENTICAL | 同左 |
| G15b | rc=2（无读者表，仅记录，D27） | 同左 |
| G15c | ADOPT（0 UNEXPECTED） | 同左 |
| G16 | defective 0（基线 2 处 TC 面弯引号已归 Newsreader） | 同左 |
| D18 | gap 315.3px（基线 322.2） | 同左 |
| D37 | y612 −1182.3pt；sub −287.0pt，end 1152.5（基线 −285.7） | 同左 |
| P8 | 1298 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：F1 同 de（`content12.py:86`，18.5→18.0）。另见 §0.3：face 剥离 74+24+4 处。

### 2026-w46-ja-zh-cn（core-ja 构建，见 §6）

| 门 | run1 | run2 |
|---|---|---|
| ALL-GREEN | **False** | **True** |
| G11 | **FAIL（脚本 bug）**：`no baseline spill set`——spill 文件名取版目录（core-ja）+ None 守卫缺失；实测 run1 spill 集 == 基线集（P5 同一行） | PASS：SPILL 1，OBSERVE 98，= 基线集 |
| G12 | **FAIL DEFECT 1**：P1 信用行 over **+6.5px**，`core title overflows its box`（core 即参照，无 core_over 可比） | DEFECT 0 |
| G1–G10 | TOTAL 150；latin_added 88；p8rows 1225→1288，页脚余量 48.9 | 同左 |
| G3 | latin 0，cyr 0，curly_cjk 0，curly_total 2（已归 Newsreader） | 同左 |
| G14 | defects 0，observes 1 | defects 0，observes 0 |
| G15a | pw 0，pi 132（`·`115 + `／`8 + `/`8 + `—`1），pdfdiff IDENTICAL | 同左 |
| G15c | ADOPT（0 UNEXPECTED） | 同左 |
| G16 | defective 0 | 同左 |
| D18 | gap 315.3px（基线 322.2） | 同左 |
| D37 | y612 −1182.3pt；sub：无副刊头行，N/A（基线同） | 同左 |
| P8 | 1299 元素，max_y 2624.0，余量 76.0px | 同左 |

修复表：F1（`content12.py:85`——core 文件少一行，18.5→18.0）。core 的 F1 是 DEFECT（非 OBSERVE），故 11 版同修有双重依据：W45 先例 + core 自身缺陷。

## §6 core-ja 交叉核对（步骤 7）——成立：(ja, zh-cn) 由 core-ja 构建

- **目录存在性**：`production/2026-w46/` 内**无** `2026-w46-ja-zh-cn` 目录；`production/2026-w46/core-ja/` 存在，内含 `2026-w46-ja-zh-cn.text.md`、WEEKLY-KIT.md、ABSTRACT.txt、content*.py、bslib4.py、assets 等。
- **已发 PDF fitz 实测**（`issues/2026-w46/2026-w46-ja-zh-cn/2026-w46-ja-zh-cn.pdf`，8 页）：P1 刊头标语 `毎週、日本語で· 每周一期· 日本人が読んでいる日本語を読む`（`每周一期` 在位）；无读者徽章副刊头行（与 core 构建一致：core 的 D37-sub 为 N/A，各读者版均有 `日語正文　×語講解 — 給×語讀者的版本` 行）；页脚 `Lucerna · 日语周报VOL.3 · LUCERNA JAPANESE WEEKLY` / `第8 版/ 共8 版`。
- **与 D5 字面条款一致**：机制规定 zh-cn 读者用 core-ja（cjk）作基底；已发 (ja, zh-cn) 确为 core-ja 构建，无覆盖风险。Closer 将 `patched/core-ja/` 同步进 `production/2026-w46/core-ja/`。
- 另：core-ja 的 `2026-w46-ja-zh-cn.text.md.new`（run2，44,048 字节）即 zh-cn 版交付 text.md；`logs/<slug>/<slug>.text.md.new` 不存在的旧注记不适用——本家导出件在 `patched/<slug>/` 内（fr/it 先例的取件口径：以 patched/ 侧导出件为准，已实测确认 fanout 侧为旧产物）。

## D47 节：`###` 行丢失——不适用（11 版全 0）

| 版 | 已发 text.md `###` 行数 | 已发 `##` 行数 | 已发总行数 | 导出器 `###` 逻辑 | 校验器 UNEXPECTED | 多重集差 |
|---|---|---|---|---|---|---|
| de | 0 | 8 | 1357 | 无 | 0 | 0（G15c ADOPT） |
| en | 0 | 8 | 1348 | 无 | 0 | 0 |
| es | 0 | 8 | 1363 | 无 | 0 | 0 |
| fr | 0 | 8 | 1353 | 无 | 0 | 0 |
| it | 0 | 8 | 1360 | 无 | 0 | 0 |
| ko | 0 | 8 | 1332 | 无 | 0 | 0 |
| nl | 0 | 8 | 1361 | 无 | 0 | 0 |
| pt | 0 | 8 | 1363 | 无 | 0 | 0 |
| ru | 0 | 8 | 1364 | 无 | 0 | 0 |
| zh-tw | 0 | 8 | 1326 | 无 | 0 | 0 |
| zh-cn | 0 | 8 | 1329 | 无 | 0 | 0 |

- `textexp_ja.py` 无任何 `###` 发出逻辑（grep `###` 0 命中，亦无 24pt 阈值——grep `24` 0 命中）；已发版亦无 `###` 行。D47 的 24pt `###` 阈值丢行现象在本家**不存在**：无丢失行可补，builder 不补行、不改阈值，closer 亦无 D47 补行任务。

## D41 节：G6 斜体/重叠旗标先量测再定性——ru P8 一例，真缺陷，已修

- **唯一 G6 旗标**：ru run1，p8 TEXTX（见 §4）。按 D41 量测 + 基线同位对照：
  - 审计器墨宽（PIL/FreeType，`occlusion_audit.ink_box`）：25px 时 Cyrillic 行墨右缘 1048.5，`Короткое…` 行 x=1010.7，**实隙 −37.8px（真重叠，非 artifact）**；24px 仍 −2.3；23.5px 余量 +15.5；23px +33.2。
  - 基线同位：旧组合行（`答え　Ответы…`，Noto Sans CJK JP，25px）墨右缘 1020.2，`Короткое…` x=1032.3，余量 +12.0——基线干净（G6 PASS）。D5 把西里尔文改由 Noto Sans 渲染后加宽约 28px，越过界线。
  - 另有独立证据：导出器把两行读成一个词元（`номерКороткое`），致 G15c HOLD。
- 定性：**真缺陷**（非 W45 ru 式正体字宽量斜体的 artifact）。修复 F5：`content8.py:114`，25→23.5。run2：G6 flags []、G15c ADOPT（0 UNEXPECTED），墨余量约 +20px（`答え` 行亦同比例缩小，Cyrillic 行左移约 4.5px）。
- 其余 10 版 run1/run2 G6 均为 flags []，无 D41 事项。

## §7 内容抽查

抽样方法：每版取 3 个探针串（P1 主标题、一个正文/练习关键词、P8 末键标记），在 run2 导出件与已发 text.md 中双向核对（空白归一）。另 G15a（pdfdiff IDENTICAL）与 G15c（ADOPT）已证明全文逐词一致，本节为人类可读抽样。

| 版 | 探针 1 | 探针 2 | 探针 3 | 结果 |
|---|---|---|---|---|
| de | 日よう日は七五三 | ポッキーの日は11月11日 | どういたしまして | 3/3 双向在位 |
| en | 日よう日は七五三 | Pocky Day | 150. | 3/3 |
| es | 日よう日は七五三 | Pocky | 150. | 3/3 |
| fr | 日よう日は七五三 | Shichi-Go-San | 150. | 3/3 |
| it | 日よう日は七五三 | Pocky | 150. | 3/3 |
| ko | 日よう日は七五三 | 포키 | 150. | 3/3 |
| nl | 日よう日は七五三 | Pocky | 150. | 3/3 |
| pt | 日よう日は七五三 | Pocky | 150. | 3/3 |
| ru | 日よう日は七五三 | Pocky（拉丁拼写；初探针 `Покки` 在新旧两版均无，探针词有误） | 150. | 3/3（纠正后） |
| zh-tw | 日よう日は七五三 | 七五三 | 150. | 3/3 |
| zh-cn | 日よう日は七五三 | 七五三 | 150. | 3/3 |

P1 主标题逐版均为 `日よう日は七五三！`。抽查 33/33 通过。

## §8 同步清单（步骤 10）

实测 `diff -rq patched/ vs production/2026-w46/`（排除 `__pycache__`/svg/cards/PDF/`.text.md`，日志 `logs/diff-patched-vs-production.txt`；逐文件统一 diff 见 `logs/diff-full/<slug>.diff`，每版约 93KB，供重校复核）。

### 同步文件（per-edition）

| 版 | 同步文件 | 行差（production → patched） |
|---|---|---|
| de/en/es/fr/ko/nl/pt/ru（8 版同构） | WEEKLY-KIT.md、svglib.py、bslib4.py、content12.py、content34.py、content56.py、content7.py、content8.py、render.py | svglib +284/−39；bslib4 +33/−36；content12 +57/−56；content34 +28/−28；content56 +30/−30；content7 +17/−17；content8 +14/−14；render +13/−1；合计 697 行 |
| it | 同上 9 件 | content12 +58/−57（多 1 行为 F4 `tsize=22`）；其余同 8 版；合计 699 行 |
| zh-tw | 同上 9 件 | svglib +284/−53；bslib4 +54/−57；content12 +62/−61；content34 +31/−31；content56 +32/−32；content7 +27/−27；content8 +19/−19；render +13/−1；合计 803 行 |
| zh-cn（core-ja） | 同上 9 件 → `production/2026-w46/core-ja/` | content12 +56/−55；其余同 8 版；合计 695 行 |

- 行差主体是 **D1 移植**（fanout §1.1 新样式文件 vs 生产旧样式文件），非 D5 修复：D5 修复本身每版仅 1–2 行（F1–F5，见 §1–§6）；it 的 +58/−57 中多出的 1 行为 F4 的 `tsize=22`。
- `transform.py`：9 版与生产版逐字节相同，无动作；zh-tw 与 core-ja 两侧均无此文件，无动作。`run.py`：11 版与生产版逐字节相同，无动作。
- `render.py`：11 版均同步（D54）。生产版 `BASE` 为绝对路径（`~/workspace/.../files/weekly-report-w46-ja-de`，本地旧构建目录，死路径）；patched 版为 ED-相对（`os.path.dirname(os.path.abspath(__file__))`）+ 内调 `tools/webpdf.py` 生成网 PDF。
- `WEEKLY-KIT.md`：11 份均同步（patched 侧已追加 D5 节，见步骤 9；**单向 patched → production，绝不反向覆盖**）。
- `ABSTRACT.txt`：排除，不同步。故事图 JPG（`assets/*.jpg`）：不进 production（D20）。`assets/lucerna-moth.svg` 等 fanout 资产仅为构建输入，不同步。
- 生产侧独有文件不动：各版 `ja-*-freeze.json` / `ja-*-occlusion.json` / `ja-*-p8compare.json`（旧门禁产物）、core-ja 的 `build-ja.log`、`final-ja-*.json`、`fix/`、`fix-round3/`、`ja-core-*.py`、`ja-core-*.json`、`proofread-gates*` 等。
- text.md 取件口径：**以 patched/ 侧导出件为准**——`patched/<slug>/<slug>.text.md.new`（run2 终轮导出；`logs/<slug>/<slug>.text.md.new` 不存在，fr/it 先例已证实；fanout 侧 `.text.md.new` 为旧产物，绝不取）。D47：无补行（见 D47 节）。
- 同步后 closer 须核：`git status` 只含上述 9 件/版（+ text.md 取件 + issues/ PDF 更新——PDF 由 closer 按既有流程重放，不由 builder 重跑 webpdf 覆盖）。

## §9 交付物 SHA 总表（run2 终轮实测）

印/网 PDF 为 run2 构建实测值（PDF 字节非确定性，run1→run2 有数十字节浮动，属时间戳/ID 差异；closer 复制 builder 原件，不重跑 webpdf）。text.md 为确定性导出（run1→run2 同值）。

| 版 | 印 PDF（字节 / SHA-256 全值） | 网 PDF（字节 / SHA-256 全值） | text.md.new（字节 / SHA-256 全值） |
|---|---|---|---|
| de | `Lucerna-VOL3-DE.pdf` 24,212,672 / `861832c22b3c53725744d8e1067083540db5eb22d8c42a451546665a226b3ad7` | `Lucerna-VOL3-DE-web.pdf` 2,165,879 / `ea350e958d3e861ed460a053712f6b6fd5942d8f3f3724823db77b81bb3cc8f2` | 46,228 / `8481f9bbac7b8d3a2f2a5aac54270ffbb6abd69f657e8f64c7b6278391e26d69` |
| en | `Lucerna-VOL3-EN.pdf` 24,205,030 / `c8491232b704129eba2e6e482440a58ff3812312bab54e6faa2dc56700fd8217` | `Lucerna-VOL3-EN-web.pdf` 2,158,336 / `638f0be9d432984b13ee5f9e003f4afe79910c1058eeef078cc8f2b3b3b0b201` | 45,421 / `08bded92f44739baba5f572f54ae75dd60c18adac27ed79c51562c582a358e95` |
| es | `Lucerna-VOL3-ES.pdf` 24,213,421 / `6e90549cfa069624756400e9f3eb039b9fa28b8fb618e885e1946ab2e7e4206c` | `Lucerna-VOL3-ES-web.pdf` 2,166,705 / `fefeb243aa71326520eb2e1e78070e858563945f1eb94e0fd00de6a866e24b5a` | 46,996 / `7bd9da146865e6b3e6be30d724eb4a9a626e560753fe9b84307c663219778a68` |
| fr | `Lucerna-VOL3-FR.pdf` 24,211,949 / `ac61b957c7847f0a21d7ec91259242a57cb00fd241a011f7044576f2f64916ec` | `Lucerna-VOL3-FR-web.pdf` 2,165,544 / `ed14b8745d5cebd43cec613f7f576179f374d8ca35df5bd9858def4f63f1db98` | 46,910 / `cfb0950754e092900bcc0d411410de48c262c301143950541e66390f00395712` |
| it | `Lucerna-VOL3-IT.pdf` 24,204,487 / `a60532e7c1f1dcc1d58fc8eae063ef892233dd110d8628b06025b82e765560a8` | `Lucerna-VOL3-IT-web.pdf` 2,157,682 / `c29a66c43c6f2d4dd973dd19d08e049ddebdd6d64c030087903873711abfa69f` | 46,769 / `f4c570de2b458fbb86f5b720958cbe032584776bcde8020191cb38d47bc6ff52` |
| ko | `Lucerna-VOL3-KO.pdf` 26,157,353 / `1192bd9e58b6d30328f9579feb7f4ce2b3b4eed513cf936cb7e11a6c23c4857e` | `Lucerna-VOL3-KO-web.pdf` 2,324,056 / `107910d82cbfabb10598c72df681f87132d73b981ed27a3f7059067ac170b154` | 47,808 / `2ba8a376da1dc67eaf8b98cb58c04be4d4c73ad9efb06c8675b869c8d17ab3dd` |
| nl | `Lucerna-VOL3-NL.pdf` 24,207,002 / `411cc7d7e8c1e5d92f26ed9d17c6099408215e7e4d5ca3e95f62f64c1b1a1b21` | `Lucerna-VOL3-NL-web.pdf` 2,160,238 / `1f0ca9416b4243240e9aaa36f284343d7fb6c20d2282c51ffddcab2ddcaa1dcb` | 46,030 / `473f9969287831c4ba1ea732ccd8d98b5de20dabb850862f7c968723d6b05eca` |
| pt | `Lucerna-VOL3-PT.pdf` 24,214,993 / `3a877c06763ee36ee91224de585179aefb558388c2c2ade43c1fb6de01f52d09` | `Lucerna-VOL3-PT-web.pdf` 2,168,455 / `693002058b2941e56bc72195b762f250ee9e4c4dd885eb136d03abdd5c7ddf3d` | 46,819 / `b21c91fc58e148d0b04ec9f07edc2b9fefbc0b47850c1603f83be3462eaa8834` |
| ru | `Lucerna-VOL3-RU.pdf` 24,375,615 / `236107cf967ceab2da515dcb1643b3513cefa51f76fb1807a798f797a44d8c2f` | `Lucerna-VOL3-RU-web.pdf` 2,326,296 / `d560f354726892db77aa0c55428b36621a7d1ccc8f00b38d982bc6133659008a` | 53,505 / `ca05c834e4b2a379d9c8a08ff46b03fc6bd8d71a68d23a207f97802a8c5cbd87` |
| zh-tw | `Lucerna-VOL3-ZHTW.pdf` 24,387,005 / `a6881fa836dcc0b2884197eb75ef49cff0101b853b0f92b263f4c1cf885bf134` | `Lucerna-VOL3-ZHTW-web.pdf` 2,534,472 / `d80776b849b24384746d483f40676466a93cc70d3f49c35bfc7f271446e6d1d1` | 44,018 / `09f7d430201a1e15fa80efc2e8a29d4ffaaca57260713054e9f47e09464ac4a5` |
| zh-cn | `Lucerna-VOL3.pdf` 24,369,825 / `0630eb38989b29cda67cd2cd30cbd666838c826dd7c950b6592eed8d1e1d6875` | `Lucerna-VOL3-web.pdf` 2,418,539 / `e2737710c6670f2081f08e18084c7099d6951f0366edb551ac54352df30a8552` | 44,048 / `b35f8fbd0d43f96b56fd83760203f3a67094cc8cbf86fda3b3b2caf4012d452a` |

已发版值（D47/对照用；`issues/2026-w46/<slug>/`）：

| 版 | 已发 text.md（字节 / SHA-256 全值） | 已发 PDF（字节） | `###` 行数 |
|---|---|---|---|
| de | 46,360 / `294d9239fb8d56e483a1cdeb4c89062592626a83ba0431abfe2d676032e0261e` | 2,366,010 | 0 |
| en | 45,553 / `4c8ee4c9a8778a8622752256d1f965fbb322ca02ed262afdb144c9e448a5d628` | 2,318,038 | 0 |
| es | 47,128 / `bde9b738218834cf61b47f98c1d68be401584f0afde7e50a5aaacb770490ba62` | 2,346,165 | 0 |
| fr | 47,041 / `1e25a1cdb1e49ca4268c3a0f9a94b8a48a253e332b95fefab2bc7812d6d1459a` | 2,344,133 | 0 |
| it | 46,902 / `b4c11633d4163ef61efef6532224f242aaf7512c5a786d0f80309e0dc5ef8e94` | 2,337,476 | 0 |
| ko | 47,942 / `bc543b82ab0bfc05d8a52a5bd451994573f6c78b4da4fb22676da9a5ab191134` | 2,395,657 | 0 |
| nl | 46,163 / `f3b3d8a5765f54927eece5e32573b4647b7c765579df02d5eafc8c50da02628d` | 2,340,934 | 0 |
| pt | 46,951 / `81523f5fd247b47c09189e5eb8a6ef5dbd3cc93e1dacd335e81bc17dc2adba99` | 2,348,982 | 0 |
| ru | 53,638 / `4c9b16933815a433a16350f864442ca9f34a0ab26cacf2a26fed7f6a6bd07eb6` | 2,254,305 | 0 |
| zh-tw | 44,204 / `b380af5cc94f44bfdf6c3bbb7ce0cff5df67d64b048d63aa3068e7e9cb4b8d40` | 2,872,569 | 0 |
| zh-cn | 44,225 / `a1e17bd052d2378ca1073036174d1c64b5b60e74add15e4005a2285bc5724b4d` | 2,496,765 | 0 |

## §10 closer 交接

### KIT custody

- KIT 正本在 production（11 份均在位，已核实）；builder 已将生产 KIT 复制进 `patched/<slug>/WEEKLY-KIT.md` 并追加 `## 补记：D5 字体重建（2026-11-15）`（D5 pin 块 + 重建节，`bin/kit_update.py`，KIT UPDATE ALL-OK）。
- 同步方向**单向 patched → production**，绝不反向覆盖（fr 先例警告过的同步陷阱）。同步后核对：生产 KIT 含 D5 节，且旧章节逐字节未动（复制时已校验与生产版逐字节相同）。

### D19 核对结果——通过

- 核对工具 `bin/d19_check.py`（日志 `logs/d19-check.txt`，rc=0）：KIT 与本报告内全部 `content*.py:NNN` 引用逐行核对 patched 文件，**引用 46/46 在位**。
- D5 修复引用 **15/15 通过**：p.text 引用行本身含新字号字面；f.box 引用 `content12.py:51` 为收尾行 `], tsize=22)`；15 处修复在各自 KIT 的 D5 节与本报告修复表中均有引用。KIT 内旧引用（生产 KIT 原有，如 key-42 的 `content34.py:95`）行号未漂移（全部修复均为原地字面替换，无增删行），逐行在位。

### 残留项

1. **zh-tw 字体面（上报协调员，§0.3）**：已发版为 TC 面，D5 模板为 JP-only；本家按 W45 先例剥离 face（读者文本按 JP 渲染）。若协调员裁定须复现 TC 面，需机制侧出 TC 分支模板后重做 zh-tw 一版（其余 10 版不受影响）。
2. **pt D37-sub 余量仅 −0.9pt**（end 1438.6，限 1439.5）：PASS，但为全家最紧。D5 加宽所致（基线 −50.0）；es −8.0 次之。重校时肉眼复核 pt/es 的副刊头行右端。
3. **P2 中页空白加宽**（29.2px → 83.3px）：已 reopen 的缺陷类，待 redesign；非 D5 发现，本家未动。
4. **G15b 9 版 rc=1、2 版 rc=2**（仅记录，D27）：共享校验器对 ja 格式未校准；验收以 G15a + G15c + 全读为准，不阻塞。
5. **G11 spill 1/版**（P5 归属行，先存几何，fanout 已裁定 0 port-introduced）：重建集 == 基线集，不阻塞；若重校认为该行应修，须另案处理（D5 不动它）。
6. **zh-tw/zh-cn G3 curly_total=2**：已归 Newsreader 的弯引号（fix2 既定态），curly_in_CJK=0，G16=0，非违规。
7. **印/网 PDF 字节非确定性**：run1→run2 浮动数十字节；§9 以 run2 实测为准；closer 复制 builder 原件，绝不重跑 webpdf。

### closer 待办（按序）

1. 按 §8 同步清单同步 `patched/` → `production/2026-w46/`：每版 9 件（KIT、svglib.py、bslib4.py、content12/34/56/7/8.py、render.py）；zh-cn 版同步进 `production/2026-w46/core-ja/`。`transform.py`、`run.py` 与生产版相同，不动；`ABSTRACT.txt` 不同步；JPG 不同步。
2. text.md 取件：`patched/<slug>/<slug>.text.md.new` → `issues/2026-w46/<slug>/<slug>.text.md`（11 版）；D47 无补行。
3. 印/网 PDF 取件：复制 `patched/` 内 run2 PDF 原件进 `issues/`（不重跑 webpdf）；核对 §9 SHA（印/网全值）。
4. 同步后 `git status` 核对：只含上述文件；随后按既有流程 commit/push（builder 不做 commit/push）。
5. 上报协调员：zh-tw TC 面裁定（残留项 1）；pt D37-sub −0.9pt 已记录在案。
6. scratch 清理：closer/协调员决定（builder 不清 scratch；`backup/`、`logs/`、`baseline/` 留待重校）。
