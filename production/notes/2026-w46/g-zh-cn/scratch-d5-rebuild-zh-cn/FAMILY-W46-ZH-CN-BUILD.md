# W46 简体中文目标家族 D5 重建报告

- 家族：W46 zh-cn（目标语简体中文，2026-11-09 → 2026-11-15，VOL.3）+ core-zh-cn
- 任务：D5 字体修 + §1.1 样式一次做完，同一版只渲一次；builder 工人，不 commit、不 push
- 工作目录：`hidden_files/d5-redo/scratch-2026-w46-zh-cn/`（`baseline/`、`patched/`、`logs/`、`bin/`、`backup/`）
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`
- 磁盘门：开工 73G/150G（50%）；收尾见 §10
- 先例：W45 zh-cn（builder → 重校 → closer `9c821eda`）；W46 ja/ko（builder → 重校 v1 PASS → closer `d5d1f782` / `ab8972a6`）

## §0 方法

### §0.1 范围订正——本家实为 10 版，不是任务书的 11 版 + core

任务书读者清单（11 读者 de/en/es/fr/it/ja/ko/nl/pt/ru/zh-tw + core-zh-cn）对本家是错的：

- **不存在 (zh-cn, zh-tw) 版。** 跨字体系排除组合。实测 2026-11-16：`issues/2026-w46/` 无 `2026-w46-zh-cn-zh-tw` 目录；`production/2026-w46/` 无此目录；fanout 无 zh-tw 目录；`FANOUT-REPORT-W46.md` L3 明言 "10 editions (core-zh-cn = en-reader edition + 9 fanout readers de/es/fr/it/ja/ko/nl/pt/ru)"；`~/workspace/weekly-git/AGENTS.md` 明言 "Do not create a pair directory between Simplified and Traditional Chinese (zh-cn × zh-tw). Lint blocks it."
- **实建 10 版**：9 个读者目录（de/es/fr/it/ja/ko/nl/pt/ru）+ core-zh-cn；core-zh-cn 内含 `2026-w46-zh-cn-en.text.md`，即 core 兼作 **en 读者版**（`ZH-CN-SOURCES.md` §1.1：(zh-cn, en) 为 layout item）。production 同样为 9 读者目录 + core-zh-cn，无 `2026-w46-zh-cn-en` 读者目录。
- **未虚构 zh-tw 版。** 任务步骤 0.3 的 zh-tw 字体面核实对本家空无对象（见 §0.3）。
- 本报告以下 "10 版" 均指上述 10 个真实版；"en 版" 即 core-zh-cn 构建的 (zh-cn, en)。

### §0.2 D1 定性（步骤 0.2）——D1+D5 一次做

- 生产 `2026-w46-zh-cn-*/svglib.py` + `core-zh-cn/svglib.py`，10/10：**D1 fix 0 处、Newsreader 0、`_D5_READER` 0、`_char_font` 0；272 行** → pre-D1 旧样式。
- Fanout `fanout-2026-w46/<reader>/svglib.py`，10/10：**D1 fix 1 处、Newsreader 11、`_char_font` 4、`_D5_READER` 0；601 行** → 新样式（§1.1）+ D1，无 D5。10 份 fanout svglib 逐字节相同（md5 `69c750c71dd2949658f897ce475ce4a8`）。
- **重建 = D1+D5 一次做**（自 fanout 装机，与 ja/ko 相同）。
- Patched svglib 来源：**手写移植脚本 `bin/d5_port_zhcn46.py`**，非移植模板。W47 production `core-zh-cn/svglib.py`（666 行）是另一代引擎（通用 `_IDX`、无 `face` 参数、无 `_fw`/caron 逻辑），与本家 fanout svglib 既不逐字节相同也无法作模板。W45 zh-cn 先例同样为手写移植（其 `d5_port_zhcn.py` 已随 W45 scratch 被 closer 清掉，本次重写）。移植脚本自 `tools/mechanism-w47/apply_variant.py` 的 `patch_d5()` 9 步逐字导入 `FIX2_BLOCK`/`D5_BLOCK`/`READER_CONST`（无转录）；对 SC 面引擎的适配：step-2 cmap 锚点用 `sans_SC`/`_IDX_SC`；step-3 `_FAMILY` SC 形 + `_CYR` 插入；step-4 `_FONT_FILE` 行（非 `_PATH`）；step-5 `_QUOTE_CLS` 入 `_FONT_FILE`；step-6 fix2+D5 插于 SC 面 sans 尾之前；step-7 `_D5_READER` 插于 `def _char_font(... face="SC")` 之前；step-8 `Page.text` 斜体覆盖 `sans_noto_i`；step-9 sans 注释改写。ja/ko：SC→JP/KR 计数改名（idx 定义+引用、`_IDX_SC`、类名、`face="SC"` 默认值 ×7、`Noto Serif/Sans CJK SC` 含注释、`the SC face` 注释），fix2 注释行 `Noto Sans CJK SC/TC` 占位保护后豁免；其余零残留 `\bSC\b`（断言）。含 face 参数自查（6 签名 + 3 转发）与 kinsoku `NO_START` 自查。测试中发现并修了 2 个 bug：（1）改名初版漏 `_sc_index(p)` 调用点（NameError）——全局替换 `_sc_index(`（2 处）；（2）初版残留检查漏 4 行 SC 注释——占位保护 +  plain 面名替换后通过。
- 内容文件在任何读者版均不传 `face=` kwarg（10/10 核实）——svglib `face` 默认值管一切；无 W45 ru F-1 式 `face` 参数 bug 的可能。svglib 内 `Page.text`/`para`/`wrap`/`text_w`/`_runs`/`_char_font` 均取并转发 `face`（目视 + 装机自查）。

### §0.3 字体面核实（步骤 0.3）——已发版全为 SC；ja/ko 按 W45 先例改 JP/KR

- `pdffonts` 量测已发 10 份 W46 zh-cn PDF（2026-11-16）：**处处仅 SC**——每版 `LucernaNotoSansCJKSC-Bold/Regular ×8`、`LucernaNotoSerifCJKSC-Bold/Regular ×8`、`LucernaUnifrakturMaguntia-Regular ×1`。无 Newsreader，无 JP/KR/TC 面。**已发 (zh-cn, ja) 与 (zh-cn, ko) 是 SC 面，不是 JP/KR 面**——任务书前提 "ja 面 SC→JP 与已发 JP 面一致，核实即可" 对 zh-cn 目标家族不成立。
- 处理：沿用已定家族先例，不自默决定，报协调员裁定（见 §0.7 事项 2）。W45 zh-cn 对 ja/ko 读者做了 SC→JP/KR 改名（本报告 §1），其重校独立复核 "10/10 FAILURES: 0 (de/en/es/fr/it/nl/pt/ru SC, ja JP, ko KR…)"，closer 落仓（`9c821eda`）。机制 `install_cjk_variant` 亦规定此改写；ko 的 D53（SC→KR 是机制规定的 D5 行为，接受、不质疑）同理。本家 ja/ko 照此办理。
- zh-tw 读者不存在，D52 式 zh-tw 面裁定不发生。
- ru 目标内容按 D26 旧分支（Latin AND Cyrillic → Noto Sans；fix-xru 是 W47-only，绝不引入）。kinsoku/face 移植自查见 §0.2。

### §0.4 P3b 导出器核实（步骤 0）

- 实际导出器为 `hidden_files/style-port-zh-cn/textexp_zh_cn.py`（AST 源路由；注意下划线名，非任务书所写的 `textexp_zh-cn.py`）。原生校验器 `verify_textexp_zh_cn.py <new> <reference>`。
- 基线复制件试跑：**10/10 rc=0，试跑输出与 fanout `.text.md.new` 逐字节相同**；校验器对 `issues/` text.md：**10/10 ADOPT，0 UNEXPECTED**（家具 98–99、word-split 1；条目 new 926/934 vs ref 925/933）。
- 试跑与已发 text.md 的字节差即家具改写（`·` → U+3000），系校验器设计使然，非失败。
- 已发 text.md：**0 行 `###`，8 行 `##`，每版皆然** → D47 不适用（无行可丢；导出器无 `###` 逻辑）。见 §4。
- Fanout `.text.md.new` 字节（参考）：de 43008、es 42599、fr 44032、it 42690、ja 43909、ko 43717、nl 42013、pt 42397、ru 51516、en（core）41728。已发 `issues/` text.md 字节：de 43166、en 41888、es 42757、fr 44190、it 42848、ja 44068、ko 43875、nl 42171、pt 42555、ru 51674。
- 日志：`logs/step0/`（试跑输出 + 校验日志）。

### §0.5 装机（步骤 2）——INSTALL ALL-OK

- `bin/install.py`：fanout 源复制进 `patched/`（与基线相同的文件选取：content12/34/56/7/8.py、bslib4.py、svglib.py、run.py、render.py、WEEKLY-KIT.md、ABSTRACT.txt、assets/、fanout `.text.md.new`），按读者移植 svglib，跑路由测试，写 `logs/install.json` + `logs/install.log`。
- 结果：**10/10 路由 FAILURES: 0**；`_D5_READER` 在 10 份文件皆 line 132；fix2 计数 1、`_QUOTE_CLS` 计数 4；模式 latin ×7（de/en/es/fr/it/nl/pt）、cjk ×2（ja/ko）、ru ×1；latin 7 版 svglib 逐字节相同；ru 与 de 仅差 1 行（line 132 的 `_D5_READER` 行）；ja/ko 差 24 行（模式行 + 改名）。
- 基线 `baseline/`：10 目录——9 读者目录取自 `fanout-2026-w46/<reader>/`，`core-zh-cn/` 取自 `render-zh-cn-core-w46/core/`（fanout 无 `core/` 目录）。排除 svg/、cards/、PDF、`__pycache__`、json/log、core 的 `fix/`/`proofread-gates*` 目录。
- Fanout vs production：content*.py/bslib4.py/render.py 在 10 目录**全差**（fanout = §1.1 移植新样式；production = 旧样式）；run.py 相同。故基线 = fanout 装机；§8 同步差将很大（§1.1 移植 + D5），与 ja/ko 相同。
- Fanout render.py：`BASE` 为 ED-相对 + 内部调 `tools/webpdf.py`（出印 + 网 PDF）。Production render.py：`BASE` 为死路径 `~/workspace/goals/.../files/weekly-report-w46-zh-cn-<reader>`（de 已验；core 用 `files/weekly-report-w46-zh-cn-core`）→ D54 适用：同步 fanout ED-相对版。Production KIT 均无 D5 节（grep 仅命中无关的 "verdict D5" 校对行）→ KIT 更新 = 生产 KIT 复制进 patched + 追加 D5 节（单向 patched → production）。
- FANOUT-REPORT-W46.md 参考值：10 版全 GREEN；TOTAL 150（A2 56 / B1 69 / B2 25）；p8 extract 150/150；occlusion 1 旗 0 实（斜体 caron ǒ vs 斜体 `bāogu`，约 3.5px——已知 FP，渲染核实干净）；p8 compare：core SHORT [108] 已知 FP、各版 EXTRA_ONLY [108] 已裁定、ru CLEAN；pdfdiff IDENTICAL 8/8；verify ADOPT 98/1（ja 99/1），UNEX 0；网 PDF 2,154,154–2,597,301 B；P2 间隙已加宽（accepted difference，有记录；fr P2 按 MEMORY 已重开为缺陷，本简报仅记录）；fanout svglib sha `85f5e9b4…`、24,149 B（10 版皆然）；moth SVG 1324 B sha `42487693…`；box-spill 0 新增（1 MANUAL 移 P1 徽章，除 nl 外各版皆有）。**本报告实测与该报告两处不符，见 §0.7 事项 3。**

### §0.6 门禁脚本与建造中修的口径问题

- `bin/build-one.sh <dir> <slug> <logprefix>`：run.py → render.py（内部 webpdf）→ `textexp_zh_cn.py` 到 `<dir>/<slug>.text.md.new`；输出 `rc run/render/textexp`。`bin/run-builds.sh` 批量构建并写 `.rc` 文件。
- `bin/gates_zhcn46.py`：19 verdict（G1–G14 + G15a/G15c + G16 + D18 + D37 + D37-sub；G15b 仅记录）+ 每版 GATES-SUMMARY + gates.json。G2 只扫本轮 run.log（ko fr 前例——基线 log 一并扫会把基线旧缺陷计入本轮——已规避）；G8 读 `p8-compare.json` 的 `status`/`keydiff`（非 stdout）；G15c 认 `^ADOPT:`/`^REJECT:` 行；G10 口径：**cjk_added==0 即 PASS，latin_added 为 D5 run-split 数**（ja 先例：de 208……；freeze.py 的 "unexpected" 子集只适用于 `--strict-latin` 同 slug 前后对比）；G3 ru 豁免 noto_sans（census 文档：">0 for ru-reader editions"；Cyrillic 走 Noto Sans 系 D26 设计行为）；D18/D37/D37-sub 簇感知量测（ko §0.6 教训：D5 多 run 下单 run 逻辑失效——y=92 行按 >50px 间隙分簇取 VOL/标语/日期三簇，行末取簇内最大 run 末）；`bin/remeasure_p1.py` 可对已门禁版只重算 D18/D37/D37-sub + G10（de/es/fr run1 用过）。
- 建造中修的脚本 bug：`g["textexp_rc"]` 存 int 致结尾推导崩溃（de/es 基线门禁首跑崩于汇总结尾；已修，3 版重跑）；G8/G15c 解析器（见上）；G10 口径；G3 ru 豁免；D18/D37 簇量测。每次修 script 只影响其后启动的进程（Python 启动时载入）；fr run1 门禁跑旧码，已用 `remeasure_p1.py` 纠正。
- `pdftotext` 一律显式单文件路径，禁用 glob。报告只贴紧凑表格与 SHA，不贴整份日志原文。
- 服务中途重启一次（约 07:00 前后，`/tmp` 被清空；`run1-builds.sh` 循环被杀，ko 构建中断于 0 字节日志）：按 AGENTS.md 教训自行发现、核对已完成 5 版（de/es/fr/it/ja 各 2 PDF + TOTAL 150）后，只重跑剩余 ko/nl/pt/ru/en。无文件损坏。

### §0.7 需协调员裁定的事项（3 项，非阻塞）

1. **任务书读者清单错误**：任务书称 11 读者 + core，本家实为 10 版（无 zh-tw 读者）。已按 10 版实建，未虚构 zh-tw 版。请协调员修正任务书清单。
2. **已发版字体面**：已发 10 版全为 SC 面；本家 ja/ko 已按 W45 zh-cn 先例 + D53 改 JP/KR（机制规定的 D5 行为）。若协调员另有裁定（如 ja/ko 保持 SC），请指示；目前按先例执行。
3. **FANOUT-REPORT 两处与实测不符 + G15a 丢 1 个 `—`**（详见 §5/D41 节后段与 §8）：
   - FANOUT-REPORT 称 p8 compare "EXTRA_ONLY [108] / SHORT [108]"，实测 fanout 原件本身即 CLEAN（core 150、edition 150、keydiff []）；称 pdfdiff "IDENTICAL 8/8"，实测 fanout 原件与已发版 P1 差 1 个 `—`。
   - 该 `—` 是 §1.1 移植的结构改动：production `content12.py:115` 为单段 `p.para("「包裹」 bāoguǒ — ein Paket. …")`，fanout 拆为斜体头行 `p.text("「包裹」 bāoguǒ", 21.5, italic=True)` + 正文段 `p.para("ein Paket. …")`，分隔符 `—` 被丢。基线即有此差，**非 D5 引入**；D5 修复只许降字号、不改文案，故 builder 未擅自补回。请协调员裁定：接受为 §1.1 移植已知差（G15a 保持 FAIL 记录），或另派内容修复（在头行或正文段补 `—`）。

## §1 基线（fanout 装机，全套门禁）

10/10 构建 rc=0/0/0、TOTAL 150。基线门禁 **10/10 皆为 17/21 PASS**，FAIL 恒为 3 项：G3（D5 未装）、G6（斜体 caron 旗，见 §5）、G15a（§1.1 移植丢 1 个 `—`，见 §0.7-3）。其余 17 项（含 G15b 仅记录）全部 PASS。D3 规范 p8 缺口**不存在**：p8 extract 150/150 + compare CLEAN 全版，无需 `apply_canon.py`（W45 zh-cn 的 D3 不适用本家）。

| 版 | G3 D5_lat/cyr | G6 | G8 | G10 latin_added | G11 spill/observe | G12 | G14 P8 行/页脚余量 | G15c | D18 间隙 | D37 余量 | D37-sub 余量 | 网 PDF |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| de | 468/0 | 1 旗 | CLEAN | 0 | 0/67 | 0 | 243/51.7 | ADOPT 98/1 | 381.0 | +37.0 | +242.7 | 2,339,203 |
| es | 461/0 | 1 旗 | CLEAN | 0 | 0/63 | 0 | 203/48.9 | ADOPT 98/1 | 386.0 | +11.0 | +284.8 | 2,346,793 |
| fr | 464/0 | 1 旗 | CLEAN | 0 | 0/63 | 0 | 226/50.9 | ADOPT 98/1 | 382.0 | +45.5 | +274.0 | 2,254,889 |
| it | 460/0 | 1 旗 | CLEAN | 0 | 0/66 | 0 | 229/46.2 | ADOPT 98/1 | 391.9 | +104.8 | +280.5 | 2,269,355 |
| ja | 245/0 | 1 旗 | CLEAN | 0 | 0/64 | 0 | 213/48.9 | ADOPT 99/1 | 403.3 | +222.0 | +278.0 | 2,617,777 |
| ko | 242/0 | 1 旗 | CLEAN | 0 | 0/66 | 0 | 210/50.4 | ADOPT 98/1 | 413.6 | +270.4 | +286.5 | 2,511,071 |
| nl | 466/0 | 1 旗 | CLEAN | 0 | 0/65 | 0 | 236/48.9 | ADOPT 98/1 | 404.1 | +1.3 | +248.5 | 2,328,609 |
| pt | 460/0 | 1 旗 | CLEAN | 0 | 0/74 | 0 | 222/48.9 | ADOPT 98/1 | 385.4 | +1.5 | +285.5 | 2,276,651 |
| ru | 240/329 | 1 旗 | CLEAN | 0 | 0/79 | 0 | 242/43.0 | ADOPT 98/1 | 339.9 | +8.0 | — | 2,174,884 |
| en | 444/0 | 1 旗 | CLEAN | 0 | 0/63 | 0 | 231/47.2 | ADOPT 98/1 | 400.0 | +30.5 | — | 2,255,875 |

注：G1/G2/G4/G5/G7/G9/G13/G14/G16 基线全 PASS（TOTAL 150、HEAD 0、freeze 8/8、edge 0/0、creambox 0 缺陷、quotes 0）。G15b 仅记录（rc=1：de/es/fr/it/ja/ko/nl/en；pt rc=2，未校准读者；ru rc=1）。G15a 三子项中 print/web multiset diff=0、text.md.new==fanout `.new` 为真，仅 pdfdiff vs issues 1 页有差（1 个 `—`）。基线 D37 已紧：nl +1.3、pt +1.5、ru +8.0、es +11.0——此 4 版在 D5 加宽后必溢（run1 应验）。D37-sub：ru/en 两版 P1 无 y=360–385 副刊头行（ru/en 的副刊头结构不同），记 —；其余 8 版余量 +242.7–+286.5。基线印 PDF 38,622,226 B（de，fanout 同值）——与已发印 PDF 逐字节相同（de 已验）；网 PDF 与 fanout 盘上文件字节不同（webpdf 字体子集非确定性），以文本层为准。基线 SVG 8/8 与 fanout 逐字节相同（de 已验）。

## §2 run1（D5 装机后）

10/10 构建 rc=0/0/0、TOTAL 150。G3 全过（D5_lat=0、D5_cyr=0；ru noto_sans=798 为 Cyrillic 走 Noto Sans 的设计行为，口径已豁免）。run1 终态：

| 版 | 结果 | FAIL 项 | D37（基线 → run1） | D18 | G10 latin_added |
|---|---|---|---|---|---|
| de | 17/21 | G6 1 旗、G15a | +37.0 → **−17.5** | 367.9 | 269 |
| es | 17/21 | G6 2 旗、G15a | +11.0 → **−46.5** | 375.3 | 280 |
| fr | 17/21 | G6 1 旗、G15a | +45.5 → **−6.2** | 368.7 | 265 |
| it | 18/21 | G6 1 旗、G15a | +104.8 → +56.5 | 379.2 | 279 |
| ja | 18/21 | G6 1 旗、G15a | +222.0 → +223.0 | 399.3 | 133 |
| ko | 18/21 | G6 1 旗、G15a | +270.4 → +273.0 | 381.0 | 133 |
| nl | 17/21 | G6 2 旗、G15a | +1.3 → **−59.7** | 391.4 | 277 |
| pt | 17/21 | G6 2 旗、G15a | +1.5 → **−58.1** | 374.4 | 278 |
| ru | 18/21 | G6 1 旗、G15a | +8.0 → +10.0 | 330.7 | 111 |
| en | 17/21 | G6 1 旗、**G12 1 缺陷**、G15a | +30.5 → +28.4 | 386.8 | 285 |

run1 真缺陷（可修）共 6 处，皆只降字号、不改文案：

| # | 版 | 文件:行 | 旧 → 新 | 越界量 | 预期余量 | 门禁 | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | de | content12.py:23 | 16 → 15 | D37 −17.5 | +12.6 | D37 | 版次行（居中 975），Newsreader 加宽 54.5px |
| 2 | es | content12.py:23 | 16 → 14 | D37 −46.5 | +17.4 | D37 | 同上，加宽 57.5px；15pt 仍溢 −14.5，故 14pt |
| 3 | fr | content12.py:23 | 16 → 15 | D37 −6.2 | +23.2 | D37 | 同上，加宽 51.7px |
| 4 | nl | content12.py:23 | 16 → 13.5 | D37 −59.7 | +22.2 | D37 | 同上，加宽 61.0px；14pt 仅余 +5.8 太紧，故 13.5pt |
| 5 | pt | content12.py:23 | 16 → 13.5 | D37 −58.1 | +23.5 | D37 | 同上，加宽 59.6px；14pt 仅余 +6.4 太紧，故 13.5pt |
| 6 | en | content12.py:89 | 19 → 18 | G12 +9.5 | 盒内 +12.1 | G12 | P1 日历盒脚注 `Press time: Nov 2 — later results not yet known`，单行 `p.text`，Newsreader 加宽致出盒右缘 9.5px |

es/nl/pt 的 G6 第 2 旗（版次行墨与右栏 `本周日历` 重叠 24.5/37.8/35.1px）为 D37 溢出的后果，随 D37 修复消失。ru D37 run1 +10.0 虽过但紧（实墨 1429.4 vs 名义 1429.5 一致），不修、记录。P7 读者来信盒溢出（W45 ko 曾有 4 版）本家未出现：run1 10 版 G11 皆 spill=0。G10 cjk_added=0 全版；latin_added 即 run-split 数（ja/ko 133、ru 111，其余 265–285）。G15c 全 ADOPT（同基线）。

## §3 终轮

- 修复的 6 版（de/es/fr/nl/pt/en）重建 run2；未修的 4 版（it/ja/ko/ru）run1 即终轮（ru run1 重门禁一次以确认 G3 口径修复）。
- **终轮 10/10 皆为 18/21 PASS**，残留 FAIL 恒为 2 项：G6（斜体 caron 量测 artifact，见 §5）与 G15a（§1.1 移植丢 1 个 `—`，见 §0.7-3）。无其他 FAIL。

| 版 | 终轮 | D37 终值（实测） | D18 终值 | G10 latin_added | G12 |
|---|---|---|---|---|---|
| de | run2 | +12.5（预测 +12.6） | 367.9 | 269 | 0 |
| es | run2 | +17.0（预测 +17.4） | 375.3 | 280 | 0 |
| fr | run2 | +23.0（预测 +23.2） | 368.7 | 265 | 0 |
| it | run1 | +56.5 | 379.2 | 279 | 0 |
| ja | run1 | +223.0 | 399.3 | 133 | 0 |
| ko | run1 | +273.0 | 381.0 | 133 | 0 |
| nl | run2 | +41.7（预测 +22.2） | 391.4 | 277 | 0 |
| pt | run2 | +46.7（预测 +23.5） | 374.4 | 278 | 0 |
| ru | run1 | +10.0 | 330.7 | 111 | 0 |
| en | run2 | +28.4 | 386.8 | 285 | 0（修复后） |

注：整数号修复（15/14pt）实测与线性预测吻合至 0.4px；13.5pt 两版实测比预测多约 +19–23px——分数号在渲染时比线性预测收得更窄（锚定宽与实渲宽之差），方向安全（往更窄走），无碍。en G12 修复后 defect=0；`Press time…` 行 18pt 后实墨右缘 1850.5、盒右缘 1862.0，实测余量 +11.5px（预测 +12.1）。终轮 G15c 全 ADOPT；G15b 仍仅记录（同基线）。终轮印 PDF 约 28.1MB（latin 版）/ 32.3–32.8MB（ja/ko）/ 29.1MB（ru），较基线 38.6MB 缩小——Newsreader 子集小于 CJK SC 子集所致；网 PDF 2.06–2.60MB，均 <7MB。

## §4 D47——`###` 行丢失：不适用

- 已发 10 版 text.md：**0 行 `###`，8 行 `##`**（逐版 grep 核实）。
- 导出器 `textexp_zh_cn.py` 无 `###` 逻辑；交付 text.md（patched 侧导出件）同样 0 行 `###`。
- 结论：无行可丢，D47 不适用；无补行（closer 亦无行可补）。

## §5 D41——G6 斜体旗标量测 + G15a 的 `—`

### D41-1：斜体 caron 旗（10 版终轮各 1 旗，接受并记录）

- 旗标（全版同一处）：`[TEXTX] p1-touiban.svg 'ǒ' — ink overlaps 'bāogu' by 3.2x15.8px`。位置：P1 "Wort der Woche" 正文段（y=1712.0），`bāoguǒ` 一词被拆为两 run：`bāogu`（Newsreader 21.5 斜体，x=1530.8）+ `ǒ`（Noto Serif CJK SC 21.5 正体，x=1587.8）。基线与终轮元素位置逐字节相同（同位对照通过）。
- 实墨量测（PIL 真实字体，21.5pt）：Newsreader-Italic `bāogu` 墨右 = 1530.8+56.50 = 1587.3；`ǒ` 墨左 = 1587.8+0.00 = 1587.8。**真实间隙 +0.50px，两字不相触。** 300dpi 下约 1.6 device px 净空。
- 旗标来源：occlusion audit 对斜体 run 以 Regular 字体量墨（Regular `bāogu` 墨右 1530.8+60.00 = 1590.8 → 重叠 −3.0px ≈ 旗标 3.2px）。即 `_run_span` 文档串预言的情形：audit 的保守代换，非真实重叠。垂直向 15.8px 为同基线相邻 run 的正常共线，非缺陷。
- 定性：**量测 artifact，接受并记录**；不修（无缺陷可修；降字号会改动无辜行）。

### D41-2：es/nl/pt 的第 2 旗（真缺陷，已修）

- run1：es/nl/pt 各多 1 旗——版次行墨与右栏 `本周日历` 重叠（es 24.5×6.0px、nl 37.8×6.0px、pt 35.1×9.5px）。此为 D37 溢出的直接后果（版次行末越过右栏左缘 1439.5，直抵日历头 x=1461.5）。随 §2 的 D37 降号修复，run2 3 版 G6 均回落至仅 caron 1 旗。

### G15a 的 `—`（10 版终轮各 1 页有差，报协调员裁定）

- `pdf_text_diff_zh_cn.py`（已发印 PDF vs 终轮网 PDF）：p2–p8 IDENTICAL；仅 p1 有差：`only-old=[('—', 1)]`（de 已逐字定位；其余 9 版同为 1 个 `—`，见 text.md 全空白归一对比：`only-old=[('—', 1)]` 10/10）。
- 丢失处：P1 "Wort der Woche" 盒——已发版 `「包裹」 bāoguǒ — ein Paket. Was man / am Double 11 kauft, …`（一段内换行）；重建版 `「包裹」 bāoguǒ`（斜体头行）/ `ein Paket. Was man am Double 11 kauft, …`（正文段），`—` 不见。根因见 §0.7-3（§1.1 移植拆段时丢分隔符；fanout 盘上件亦然；基线即有此差）。
- 其余 G15a 子项全过：print/web 文本 multiset diff=0（10/10）；text.md.new 与 fanout `.new` 逐字节相同（10/10）。text.md 全空白归一对比（production text.md vs patched 导出件）：除该 1 个 `—` 外零差异——家具改写（`·` → U+3000、空格收拢）与导出器空行位置差 2 行皆在归一后消失。
- G15b 仅记录（共享校验器对中文格式未校准）：终轮 rc=1（de/es/fr/it/ja/ko/nl/ru/en，残留如 `10x '配' | 9x 'lesen'`）；pt rc=2（`--reader pt` 未校准，无表）。验收以 G15a（除上述 `—` 外全过）+ G15c ADOPT + §7 全读抽样为准。

## §6 core-zh-cn 交叉核对——9 读者版由读者目录构建，en 版由 core 构建

- `production/2026-w46/` 内**无** `2026-w46-zh-cn-zh-cn` 目录（应无——无 zh-cn 读者）。
- `production/2026-w46/core-zh-cn/` 内含：`2026-w46-zh-cn-en.text.md`、WEEKLY-KIT.md、ABSTRACT.txt、content*.py、bslib4.py、assets（仅 `CREDITS.md`）、render.py、run.py、svglib.py，另有 `fix/`、`fix-keys/`、`fix-round3/`、`fix-round4/`、`proofread-gates*` 工作目录与 `zh-cn-gates.log`（不随同步）。
- 已发版构建来源（fitz 读已发 PDF P1 页脚行，与基线 P1 SVG 页脚行对照，`·`/U+3000 与空格归一后比对）：**10/10 吻合**。de/es/fr/it/ja/ko/nl/pt/ru 9 版的页脚为各读者目录的读者专属串（如 de `Lucerna · CHINESISCHE WOCHENZEITUNG VOL.3 · TEXT AUF CHINESISCH (VEREINFACHT) · ERKLÄRUNGEN AUF DEUTSCH`；fr `HEBDOMADAIRE CHINOIS VOL.3 · TEXTE EN CHINOIS SIMPLIFIÉ · EXPLICATIONS EN FRANÇAIS`；ru `КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ`）；en 版页脚为 core 串（`Lucerna · 简体中文周报VOL.3 · 简体中文正文· 英语讲解· Simplified Chinese text · English explanations`），标语亦为 core 的英文版（`每周读中文· Read real Chinese, every week`）。
- **closer 同步方向**：9 读者版同步进各自 production 读者目录（es/pt 前例：读者目录构建则绝不以 core 覆盖读者目录）；en 版同步进 `production/2026-w46/core-zh-cn/`（ko/ja 前例：core 构建则同步进 core）。core 的 `fix/` 等工作目录不动。

## §7 内容抽查——30/30

抽样方法：每版 3 个探针（P1 主标题、一个正文关键词、P8 末键标记），在终轮导出件与已发件中双向核对（空白归一）。探针 1/2 对已发 text.md 与终轮 `.text.md.new`；探针 3 对终轮 P8 SVG 行与已发 PDF P8 文本（text.md 不含 P8 答案列表）。

| 版 | 探针 1 P1 主标题 | 探针 2 高潮场 | 探针 3 P8 末键 | 结果 |
|---|---|---|---|---|
| de | ✓ | ✓（23=23） | ✓ | 3/3 |
| es | ✓ | ✓（23=23） | ✓ | 3/3 |
| fr | ✓ | ✓（23=23） | ✓ | 3/3 |
| it | ✓ | ✓（23=23） | ✓ | 3/3 |
| ja | ✓ | ✓（23=23） | ✓ | 3/3 |
| ko | ✓ | ✓（23=23） | ✓ | 3/3 |
| nl | ✓ | ✓（23=23） | ✓ | 3/3 |
| pt | ✓ | ✓（23=23） | ✓ | 3/3 |
| ru | ✓ | ✓（23=23） | ✓ | 3/3 |
| en | ✓ | ✓（23=23） | ✓ | 3/3 |

探针 1：`双11到了,包裹一波一波地来`（10 版同文）。探针 3：P8 末键 `150. ✓ …` 行（如 de `150. ✓ Offene Aufgabe — Mustertext oben in Abschnitt F (164…`）。抽查 **30/30 通过**（脚本 `bin/spotcheck7.py`）。

## §8 同步清单（patched/ → production/2026-w46/）

`diff -rq patched/ vs production/` 全量对比（`logs/sync-sha.json`；完整 unified diff 逐版在 `logs/diff-full/<slug>.diff`，各约 110KB）。行差口径：production → patched（+ 为 patched 新增、− 为 production 独有）。**9 个同步文件/版**（10 版一致）：

| 文件 | de/es/fr/it/nl/pt/ru | ja | ko | en |
|---|---|---|---|---|
| WEEKLY-KIT.md | +21/−0 | +18/−0 | +18/−0 | +21/−0 |
| svglib.py | +461/−40 | +463/−43 | +463/−42 | +461/−40 |
| bslib4.py | +31/−34 | +31/−34 | +31/−34 | +31/−34 |
| content12.py | +59/−58 | +60/−59 | +59/−58 | +60/−59 |
| content34.py | +33/−33 | +33/−33 | +33/−33 | +33/−33 |
| content56.py | +35/−35 | +35/−35 | +35/−35 | +35/−35 |
| content7.py | +17/−17 | +17/−17 | +17/−17 | +17/−17 |
| content8.py | +12/−12 | +13/−13 | +12/−12 | +12/−12 |
| render.py | +13/−1 | +13/−1 | +13/−1 | +13/−1 |

- 不变的 3 项：run.py、ABSTRACT.txt、assets/CREDITS.md（10 版皆同）。
- KIT：production KIT 前缀 0 漂移（patched KIT 以 production KIT 开头）；差异仅为追加的 D5 节（de/es/fr/nl/pt/en +21 行、it/ja/ko/ru +18 行——行数差为修复表行数：有修复的 6 版多 3 行修复记录）。
- svglib：production 272 行 → patched 693 行（+461/−40；ja/ko 另有 JP/KR 改名，+463/−43、+463/−42）。693 行 = fanout 601 行 + D5 移植新增 92 行（fix2 块、D5 块、`_QUOTE_CLS`、`_D5_READER`、kinsoku、face 贯通）。
- render.py：+13/−1，同步 fanout ED-相对版（D54；production 版 BASE 为死路径，见 §0.5）。
- **production text.md：同步**（ko 前例）。patched 侧导出件替换 production text.md：行差 +101/−99（ja +102/−100），字节 new vs prod：de 43008/43166、es 42599/42757、fr 44032/44190、it 42690/42848、ja 43909/44068、ko 43717/43875、nl 42013/42171、pt 42397/42555、ru 51516/51674、en 41728/41888。分解：家具改写（`·` → U+3000）+ 导出器空行位置差 2 行 + **1 个 `—` 丢失**（§0.7-3；协调员裁定前，closer 按本报告 §0.7-3 的裁定结果执行）。
- **不同步**：图文件（`frost.jpg`、`lanparty.jpg`、`locker.jpg`、`lucerna-moth.svg`、`popcorn.jpg`、`valley.jpg`，patched 侧独有；D20 + D58：production `assets/` 保持仅 `CREDITS.md`）。`svg/`、`cards/` 为构建输出目录，不同步。PDF（印/网）按 §9 的 SHA 表由 closer 取用，不列入 `diff -rq` 文件同步（PDF 由 `tools/webpdf.py` 从 patched/ 生成；closer 落仓时以 §9 的文件为准）。en 版 production 独有 `zh-cn-gates.log` 不动。core production 的 `fix/`、`fix-keys/`、`fix-round3/`、`fix-round4/`、`proofread-gates*` 工作目录不动。

## §9 SHA 总表（终轮交付件）

终轮：de/es/fr/nl/pt/en = run2；it/ja/ko/ru = run1。印/网 PDF 由 patched/ 侧 `render.py`（内部 `tools/webpdf.py`）生成；text.md 为 patched 侧 `textexp_zh_cn.py` 导出件（`<slug>.text.md.new`）。**无双网 PDF**（render-网与 builder-网为同一文件；门禁用此网 PDF）。网 PDF 均 < 7MB；印 PDF 约 28–33MB（fanout 印 PDF 体量异常，见 §0.5；closer 落仓时按 PDF ≤7MB/推的既有规则处理——印 PDF 不随单推上仓，见 W45/W46 ja/ko closer 惯例）。

| 版 | 终轮 | 印 PDF（字节） | 印 PDF SHA-256 | 网 PDF（字节） | 网 PDF SHA-256 | text.md.new（字节） | text.md.new SHA-256 |
|---|---|---|---|---|---|---|---|
| de | run2 | 28,070,768 | `9650172fd7d15cb7b83c961c6386d9f853de8eb3e3320d8e747c552a58c27ae9` | 2,071,994 | `f68e8c3f3c9cbb80d634a244adf98dc7822e9b1450f96443ea152b2a267dc21e` | 43,008 | `1ad562b3bbdb129ac280b28a42a1d4ee62bf1ec718ec7cf46ced40d846f6ce1f` |
| es | run2 | 28,066,629 | `57b72d44e60915d902e7ab4060083b9f3fe4b6a76b9ca275ecae0cdd112c7d23` | 2,067,735 | `835e0d3c1b97f2cda692b207ddbfe0e0fe19702ae37171416e65ad4c425a9cdb` | 42,599 | `3c8137e3e200179a7649ac9655b93bcc98023c64c75a98823fb1f6effd880c1c` |
| fr | run2 | 28,065,351 | `b520d31a5b1d520c492dfbabef83d92bb88cda01d9523cef7555b75c21fc335d` | 2,066,607 | `518f17b34fb028ea782d2bf0ec67eb0a15e52ec0a83fb39e241cf404dc8edc1c` | 44,032 | `fde5e88dba914abf7d8efd2c9c882c8805f88b58846576b92dd9c56d83b5f5da` |
| it | run1 | 28,059,937 | `7ecb4e83c8b689f5c10ca68d9f0f667e2644741f6cad229a3b9e0c1056fc64f3` | 2,061,064 | `d645a1262a9dc80b82934a4ba950831a2e37769c7c9260e792b340ab1ea56a60` | 42,690 | `48e68189e186a3341cc47a0daa12bc9b277a1fea5c893a0368a5210a0c166939` |
| ja | run1 | 32,764,445 | `3a625b9eabc27421ed99e72a857e381abea5e881bd4a1e07fd32189cfcc9601b` | 2,601,615 | `64a4d900d2e0e56cf3364ecf04dc8f5bb9da0418ec760972c143ece0c2a7dbce` | 43,909 | `7e471bf6aec3257b677110cc840d1e610d733d7dd9c3b99ef70fef8fae005515` |
| ko | run1 | 32,334,701 | `51ec0cfcf0d44229c0c5161b0eb4a36de692dde0e4db8b01fa8d1fafc5ea528d` | 2,504,829 | `1ebfece3658377c15e98d6a9baaf4672028333ca6676e949e025bca3cb8000ad` | 43,717 | `e31591d6413b5c0625c4e1f2ca62b64b6b5a5ed492e38a281f0fd576e771e6f2` |
| nl | run2 | 28,064,002 | `f5846a5942910e8be5c5577f70863ccb7e3567e91c4920d37655c54c07fba7e2` | 2,065,109 | `150f5b7a3cf8e75b49935ac46c9d091a311cfb64cf5685b48558c1b05a39a030` | 42,013 | `269862c3f52ac45623f5f970bc72e713373a0b69dafb8a0d2e1b4f6c3305130b` |
| pt | run2 | 28,068,608 | `6d836d7dceb3de6a2c484151f331ad16e51dbaf5b4807a8c6833b861272f1d60` | 2,069,845 | `c4686775eaba67996def92392f1618ec3608f0447dd66a007d4de31610c345bf` | 42,397 | `370c3537134dcf1abdebe634b3fd30b50ca269d8d0552acf071d9d3609d9bb75` |
| ru | run1 | 29,054,061 | `160e613dda71f613cbcb74ccfe0ce7ee5b312b86226f398f717ed0f59593ddd6` | 2,321,088 | `f82d449b5b581b0b442962ea8741b58b4d4fdd72f5b0f53dd4cb6229b9e0dec8` | 51,516 | `dbfeee6c30645a9f5278fa60fcdaf4e8522be900e4a8f87abeda4cc5e7bb7fde` |
| en | run2 | 28,096,951 | `e4ee13f303f51431a2fe5947985c7b2433654b06291569654bdde8afbe1b2016` | 2,086,219 | `ffed5ac9aebc529f285d80e79c2450360dfd234317593cb7d5d1fd4cac1e9e85` | 41,728 | `712ee5eb3ac8ceb66443ce51434def20e4d8a86fe0f935326873b9044a27adba` |

文件名：印 PDF `Lucerna-VOL3-<XX>.pdf`（en 版为 `Lucerna-VOL3.pdf`）；网 PDF 同名加 `-web`；text.md.new 为 `<slug>.text.md.new`。全部文件在 `patched/<dir>/` 内（印/网 PDF 在 `patched/<dir>/` 根目录；en 版在 `patched/core-zh-cn/`）。

## §10 closer 交接

- **交付状态**：10/10 终轮 18/21 PASS；ALL-GREEN 0/10（残留 2 项皆已定性：G6 caron 量测 artifact + G15a 丢 1 个 `—`，见 §0.7-3）。修复 6 处（全为只降字号）。
- **同步方向**（§6）：9 读者版 → 各自 production 读者目录；en 版 → `production/2026-w46/core-zh-cn/`。绝不以 core 覆盖读者目录。同步文件清单见 §8（9 件/版 + production text.md 替换）。图文件不同步；`svg/`、`cards/` 不同步；en 的 `zh-cn-gates.log` 与 core 的 `fix/` 等工作目录不动。
- **KIT**：patched KIT = production KIT + 追加 D5 节（已做，`bin/kit_update.py`；前缀 0 漂移）。D19：KIT 与本报告内全部 `content*.py:NNN` 引用须指向修复行本身——`d19_check.py` 校验结果见 `logs/d19-check.txt`（rc=0 方可交接；本报告 §2 表中的 6 处引用均指向修复行：content12.py:23 为版次行本身、content12.py:89 为脚注 `p.text` 行本身，无 `f.box` 引用）。
- **需协调员裁定后执行**（§0.7）：（1）任务书读者清单修正（10 版，无 zh-tw）；（2）ja/ko JP/KR 面确认（已按 W45 先例执行）；（3）G15a 丢 1 个 `—`——接受为 §1.1 移植已知差（text.md 同步时照此办理），或另派内容修复（补 `—` 后 text.md 与 PDF 须重出重验）。
- **D29 复本**：本报告 + 10 份终轮 GATES-SUMMARY 已复制进 `hidden_files/d5-redo/notes/g-zh-cn/scratch-d5-rebuild-zh-cn/`，逐份 `cmp` 核对：**11/11 一致**。终轮 GATES-SUMMARY 位置：run2 版（de/es/fr/nl/pt/en）取 `logs/run2-<slug>/GATES-SUMMARY.txt`；run1 版（it/ja/ko/ru）取 `logs/run1-<slug>/GATES-SUMMARY.txt`。
- **磁盘门（收尾）**：75G/150G（51%），门内（开工 73G/150G）。
- **其余注意**：ru 版 D37 终轮 +10.0 偏紧（实墨 1429.4），未修、已记录；nl/pt 13.5pt 修复后余量 +41.7/+46.7（预测 +22.2/+23.5，方向安全）。基线/终轮全部构建日志在 `logs/`（`baseline-*`、`run1-*`、`run2-*`），门禁 JSON 在 `logs/<round>-<slug>/gates.json`。
