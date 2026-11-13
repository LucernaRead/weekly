# W47 ko 家庭第二轮修复日志（FIX-LOG-2）

- 任务：修复第二轮独立重校（`scratch-reproof2-w47-ko/PROOF-NOTE-2.md`，2026-11-12）发现的 3 条问题（1 MEDIUM + 2 low），无 MAJOR；第一轮 5 项（F1–F5）已由 PROOF-NOTE-2 核实全部到位，本轮未动。
- 范围：仅 `production/2026-w47/` 下 ko 家 11 版（`core-ko/` + `2026-w47-ko-de/en/es/fr/it/ja/nl/pt/ru/zh-tw/`）。不 commit、不 push、不跑 lint、不碰其他家庭/其他周、不改 SOP。
- 磁盘开工：95G 已用 / 55G 可用；收尾：95G 已用 / 55G 可用（门限 ≥100G，未触发）。
- 工作目录：`hidden_files/w47/scratch-fix2-w47-ko/`（本日志、备份、diff、门禁汇总、KIT 更新脚本）。
- 改前指纹：`prefix-fingerprints2.txt`（与 PROOF-NOTE-2 逐版一致）；改后指纹：`post-fingerprints2.txt`。
- 结论：**3 项全修；11 版 text.md 按页核对全过；ko-ru/ko-es 门禁全绿；KIT 11 版已更新并与盘上实测逐版核对一致。**

## R2-1（MEDIUM，11 版全家）—— text.md 导出丢题：导出器全局去重已修

### 根因（与 PROOF-NOTE-2 定位一致）

`textmd.py` 的 `collect()` 末段用全局 `seen` 集按规范化字符串去重——同一字符串全书只保留首次出现。练习题干/配对词与前面页面的同形字符串（日期框、通路图、重测题干）撞上时，静默丢掉。

### 改动：文件与改法

- **文件**：`textmd.py`（各版自带副本，11 份改前 md5 均为 `bc6394a387d15d4726e194687320da20`；先改 `core-ko/textmd.py`，再原样同步到 10 个 fan-out 版；改后 11 份 md5 均为 `00d8f52d96ecad396cbc03603d98fa9b`）。
- **改法**（`core-ko/textmd.py`，行号为改后文件）：
  - L95–99：`.ex` / `.match_set` 调用收集的字符串打上 `is_ex=True`（`method in METHOD_ARGS`，即方法名为 `ex` 或 `match_set`，不限接收器名 `f/qf/e/a/b/c`）；其余两处收集点打 `is_ex=False`（模块级 List/Dict/Tuple 常量 L113、模块级纯字符串赋值 L121）。
  - L124–145：去重循环改为两域——练习项（`is_ex`）**按调用点保留**：每个 `.ex` / `.match_set` 调用点就是一个练习块，同一题干/配对词在自己的块内出现即保留，不再参与全局字符串去重，也不写入 `seen`；普通散文仍沿用旧的全局字符串去重。
- **为什么按题号/按块保留**：题号在 `textmd.py` 的收集层不存在（编号是渲染时 `REG` 累积产生的），调用点是收集层唯一可得的“块”身份——一次 `.ex` 调用 = 一道题，一次 `.match_set` 调用 = 一组配对；同一字符串出现在两个调用点，就是两道题/两个块的合法重现（P8 重测题、跨页同形配对词）。全局字符串去重把“同一字符串”误当成“同一内容”，是错的去重键。
- **不改其他家庭**：`textmd.py` 是 ko 家各版自带副本，不在 `tools/` 共享；改动只影响 ko 家 11 版的导出行为。其他家庭用各自的导出器（见末节跨家核查）。

### 逐项修复前后对照（core-ko 为例；其余 10 版同法，行号因讲解层长度略有出入）

印版正确、题干本身一字未动；只补 text.md 本版块内的缺失行。

| 项 | 位置 | 改前 text.md | 改后 text.md（core-ko 行号） |
|---|---|---|---|
| Q26 김치의 날 | P2 D 配对（`content12.py:291`） | P2 块 3 词对 4 释义，缺 Q26 | L293 独立行 `김치의 날`（P2 日期框 L251 的同形行仍在） |
| Q61 준플레이오프 | P4 D 配对（`content34.py:230`） | P4 块只剩 K리그1 1 词对 4 释义 | L509 独立行 `준플레이오프` |
| Q62 플레이오프 | P4 D 配对（同上） | 同上 | L511 独立行 `플레이오프` |
| Q63 한국시리즈 | P4 D 配对（同上） | 同上 | L513 独立行 `한국시리즈` |
| Q121 题干 | P8 B（`올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명`） | P8 B 块 6 题，缺 Q121 | L865 整行题干 |
| Q126 题干 | P8 B（`한국시리즈 1차전은 어떻게 됐어요? A. kt 8대 7 승리 · B. 삼성 3대 2 승리 · C. 비로 취소`） | P8 B 块 6 题，缺 Q126 | L875 整行题干 |
| Q142 김치의 날 | P8 F 配对（`content8.py:79`） | P8 F 块 3 词对 4 释义，缺 Q142 | L917 独立行 `김치의 날` |

### 干跑发现的第 8 项（同根因，非练习项，如实记录）

- dry-run diff（`/tmp/textmd-core-new.md` vs 改前）除上述 7 项外，还多出 1 行：**P6 对照表行标签 `김장비용`**（新文件 L663）。核实：印版 P6 对照表（`지난주와 이번 주, 한눈에 보기`）该行确为 `김장비용　10월 16일 가격　11월 9일 조사 199,456원`（印 PDF P6 文字层第 51 行）；改前 text.md P6 节只有两个单元格（`10월 16일 가격` / `11월 9일 조사 199,456원`），行标签被同一全局去重丢掉（P2 D 配对词先占）。修后两域去重把它还原。
- 因此每版重导出实际补回 **8 项**（7 道编号项 + 1 个表格行标签），diff 均为 +16 行 / −0 行；ko-es +17/−1（多 1 行 band 行改动，见 R2-3）、ko-ru +18/−2（多 2 行 gloss 改动，见 R2-2）。**无其他增删。**标题行核对：11 版 diff 中无标题行增删（`# ` 前缀未丢；重导出 title 参数取各版现行第一行去 `# ` 后原样传入，与第一轮 FIX-LOG 的事故防范一致）。

### 11 版 text.md 重导出记录

导出命令（每版）：`tools/venv/bin/python textmd.py . <slug> <slug>.text.md "<title>"`（title 取各版现行第一行，不含 `# `）。记录见 `reexport.log`；逐版 diff 见 `diff-textmd/diff-<slug>.txt`。

| 版 | items 改前→改后 | 字节 改前→改后 | diff |
|---|---|---|---|
| ko-zh-cn（core-ko） | 458→466 | 35,159→35,456 | +16/−0 |
| ko-de | 455→463 | 35,715→36,012 | +16/−0 |
| ko-en | 455→463 | 35,484→35,781 | +16/−0 |
| ko-es | 455→463 | 35,766→36,065 | +17/−1（band 行 R2-3） |
| ko-fr | 455→463 | 35,834→36,131 | +16/−0 |
| ko-it | 455→463 | 35,771→36,068 | +16/−0 |
| ko-ja | 456→464 | 35,978→36,275 | +16/−0 |
| ko-nl | 455→463 | 35,607→35,904 | +16/−0 |
| ko-pt | 455→463 | 35,638→35,935 | +16/−0 |
| ko-ru | 456→464 | 37,738→38,039 | +18/−2（2 行 gloss R2-2） |
| ko-zh-tw | 456→464 | 35,190→35,487 | +16/−0 |

### 7 项补回核对表（重校员同款方法复用 `scratch-reproof2-w47-ko/inventory_textmd.py` / `inventory_textmd2.py` / `inventory_match.py`）

11 版全部：全书查 150/150（0 缺失）、按页查 150/150（0 缺失）、配对词独立行查 16/16（0 缺失）。汇总见 `inventory-all.log`。改前基线（core-ko）：按页查缺 Q121、Q126 两项（P2 D / P4 D / P8 F 的缺词因同页他处有同形行，未被该查法捕获，已由块原文核对确认，见上表）。

## R2-2（low，仅 ko-ru）—— `조사하다 = опрашивать` → `обследовать`

- 位置：`2026-w47-ko-ru/content12.py:45`（P1 词表）与 `:174`（P2 词注），两处同文，一并改。
- 改前：`조사하다 = опрашивать`（两处）；改后：`조사하다 = обследовать`（两处）。选 `обследовать`（调查、考察）而非 `изучать`：正文是 aT 机构按 11 月 9 日基准调查泡菜成本（价格调查/统计），`обследовать` 更贴“调查”本义。
- 残留核查：`content*.py` 全家 `опрашивать` 0 处；重渲后印 PDF 与网 PDF 各含 `обследовать` 2 次、`опрашивать` 0 次（pdftotext 实测）。

## R2-3（low，仅 ko-es）—— P2 栏目标题逗号 → 과

- 位置：`2026-w47-ko-es/content12.py:166` 的 `p.band` 行。
- 改前：`레벨 A2　김장비용, 김치의 날, 한능검`；改后：`레벨 A2　김장비용과 김치의 날, 한능검`（与 core-ko 同行及其他 9 版一致）。
- 残留核查：ko-es `content*.py` 全家 `김장비용, 김치의 날` 0 处；重渲后印 PDF 与网 PDF 的 P2 band 行均为 `레벨 A2　김장비용과 김치의 날, 한능검`，与 core-ko 印版 P2 band 行一致。

## 重渲记录

流程照第一轮 FIX-LOG：`scratch-fix-ko/rebuild-fix.sh <dir> <reader> <mode>`（先以修后源码 + `svglib.pre-d5` 重建 base-venv 对照，再 `run_edition.sh … rebuild-gates`）。其余 9 版只重导出 text.md，PDF 不动（印/网 SHA 与改前逐版一致，见 SHA 表）。

### ko-ru — DONE（重建 2 次；第 1 次作废，见下）

- **第 1 次重建（作废）**：`rebuild-ko-ru.log`，`run.py` RC=0，`render.py` **RC=143（SIGTERM，被运行时杀掉）**，其后门禁仍跑完但结果无效：印 PDF 未重建（mtime 仍为 16:39，SHA 仍为改前 `96e6ab1a6113`，印 PDF 仍含 `опрашивать` ×2），网 PDF 已是新版，TEXTLAYER FAIL。`rebuild-fix.sh` / `run_edition.sh` 不设 `set -e`，总 RC 仍报 0——总 RC 不能作为重建成功的依据，必须逐项核对 `render.py` RC 与印 PDF mtime/SHA。教训与第一轮 es 的 SIGTERM 中断同类（第一轮：重跑即成）。
- **第 2 次重建（有效）**：`rebuild-ko-ru2.log`，`run.py` / `render.py` / `webpdf.py` 全部 RC=0；印 PDF 43,926,367 B `4c0c80b6b6bf…`（18:26），网 PDF 4,126,934 B `ee36501822d1…`（18:28）；text.md 38,039 B `e439f6a60a13…`。
- 门禁（`verify-ko-ru.txt`，第二版）：TOTAL 150，0 警告；census PASS（D5_latin 0 / D5_cyrillic 0 / curly_cjk 0 / curly_total 0，noto_sans_elements=1107）；quotes 0 defective；head_check 0 findings；occlusion 0 flags；p8 extract 150/150，compare CLEAN（keydiff [137, 138]）；freeze baseline 7/8（P1 已知解释器 artefact，第一轮同值，D5 已裁定非缺陷；freeze 工具因此 RC=1，非门禁失败）；freeze diff +0/−0，新增 CJK 0，新增 Latin 459（第一轮同值，D5 run-splitting 预期值）；spill 0（49 boxes，365 OBSERVE）；boxtitle 0 DEFECT（73 titles）；edge 8 页 0 TOUCH / 0 NEAR；creambox PASS 0 defects；textlayer PASS（印/网 plain pdftotext 各 59,178 字节，逐字节一致；`-layout` 提取网版少 1 字节空白字符，为 PROOF-NOTE-2 已记录的 ru 已知现象，不影响文字层门禁）。
- P8 键：`check_p8keys.py` 150 号齐全，无 missing、无 stale（12. A / 13. A / 22. 1.8 / 47. A / 74. 8 / 102. A，注释与第一轮一致；ru 版无空格拼接为检查器 SVG run 拼接假象，印 PDF 文字层空格正常，第一轮已核实）。

### ko-es — DONE（重建 1 次）

- `rebuild-ko-es.log`，`run.py` / `render.py` / `webpdf.py` 全部 RC=0；印 PDF 43,752,821 B `637bcb1b1b22…`（18:37），网 PDF 3,955,583 B `e1ae9fcc033b…`（18:39）；text.md 36,065 B `a24bd9ffaa09…`。
- 门禁（`verify-ko-es.txt`）：TOTAL 150，0 警告；census PASS（0/0/0，curly_total 0）；quotes 0 defective；head_check 0 findings；occlusion 0 flags；p8 extract 150/150，compare CLEAN（keydiff [137, 138]）；freeze baseline 7/8（P1 artefact，第一轮同值；freeze RC=1 同上）；freeze diff +0/−0，新增 CJK 0，新增 Latin 597（第一轮同值）；spill 0（49 boxes，358 OBSERVE）；boxtitle 0 DEFECT（73 titles）；edge 8 页 0 TOUCH / 0 NEAR；creambox PASS 0 defects；textlayer PASS（印/网 plain pdftotext 各 52,070 字节，逐字节一致）。
- P8 键：150 号齐全，无 missing、无 stale。P2 band 行核对见 R2-3 节。

## 逐版门禁结果表

| 版 | p8 compare | occlusion | spill | boxtitle | edge | D5 census | U+201C/D/2019（text.md + SVG） | 按页 inventory | PDF |
|---|---|---|---|---|---|---|---|---|---|
| ko-zh-cn（core） | —（基准） | —（未重建） | — | — | — | PASS（0/0/0）* | 0 | 150/150 全书+按页，16/16 配对 | 未动 |
| ko-de | CLEAN [137,138] | —（未重建） | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |
| ko-en | CLEAN [137,138] | — | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |
| ko-es | CLEAN [137,138] | 0 flags | 0 SPILL | 0 DEFECT（73） | 0/0 | PASS（0/0/0） | 0 | 150/150，16/16 | 重渲，全绿 |
| ko-fr | CLEAN [137,138] | — | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |
| ko-it | CLEAN [137,138] | — | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |
| ko-ja | CLEAN [137,138] | — | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |
| ko-nl | CLEAN [137,138] | — | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |
| ko-pt | CLEAN [137,138] | — | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |
| ko-ru | CLEAN [137,138] | 0 flags | 0 SPILL | 0 DEFECT（73） | 0/0 | PASS（0/0/0，noto 1107） | 0 | 150/150，16/16 | 重渲，全绿 |
| ko-zh-tw | CLEAN [138] | — | — | — | — | PASS（0/0/0） | 0 | 150/150，16/16 | 未动 |

\* core-ko 与其余 8 个未重建版的 D5 census 为本轮独立重跑（`gates9/census-<版>.json`，RC=0，curly_total 0）；p8 compare 为本轮独立重跑（`gates9/summary.log`，RC=0）。未重建版的 occlusion/spill/boxtitle/edge 未重跑——其 SVG 与印/网 PDF 与 PROOF-NOTE-2 核实时逐字节一致（SHA 未变），第二轮 87 门全绿的结论仍成立。
\* keydiff [137,138] 为预期翻译题键（P8 E 区合法翻译差异，第一轮已裁定）；zh-tw 仅 [138]。

## KIT 更新后 SHA 表（盘上实测，2026-11-12）

更新脚本：`update_kit.py`（断言式：逐行正则替换 + 逐版核对；第一轮标记 `fix rebuild 2026-11-12` 原样保留 3 处/版，第二轮标记为 `fix rebuild 2, 2026-11-12`：ru/es 各 3 处、其余 9 版各 1 处）。更新后以独立脚本重算 11 版 KIT 所载印/网/text 三组字节数 + SHA-256，与盘上逐版核对一致。

| 版 | 印 PDF（字节 / SHA 前 12） | 网 PDF（字节 / SHA 前 12） | text.md（字节 / SHA 前 12） |
|---|---|---|---|
| ko-zh-cn（core-ko） | 45,181,315 / `7248314a5ae2`（未动） | 4,226,882 / `ac97b284fe16`（未动） | 35,456 / `044001ac2f14` |
| ko-de | 43,754,319 / `8d217beb86ae`（未动） | 3,956,937 / `4b1a54ce3040`（未动） | 36,012 / `4f6945d36115` |
| ko-en | 43,748,448 / `f10c5065bb5b`（未动） | 3,951,102 / `59bb38b0bc77`（未动） | 35,781 / `f5e5bb278704` |
| ko-es | 43,752,821 / `637bcb1b1b22` | 3,955,583 / `e1ae9fcc033b` | 36,065 / `a24bd9ffaa09` |
| ko-fr | 43,751,522 / `1f6add20c07d`（未动） | 3,954,158 / `dc933cc18cfe`（未动） | 36,131 / `661b391e24d3` |
| ko-it | 43,746,645 / `edfda4420e46`（未动） | 3,949,052 / `f0efba8a29ab`（未动） | 36,068 / `4e7926e4ffa7` |
| ko-ja | 50,279,548 / `f8c7508f9be8`（未动） | 4,373,107 / `f9bb1d3a3929`（未动） | 36,275 / `be048d7d4164` |
| ko-nl | 43,748,187 / `662eb3e3e3f2`（未动） | 3,950,671 / `5f84566e41de`（未动） | 35,904 / `55abafb3fee8` |
| ko-pt | 43,753,908 / `70047cd27b8d`（未动） | 3,956,638 / `e4028beb886a`（未动） | 35,935 / `059743986a52` |
| ko-ru | 43,926,367 / `4c0c80b6b6bf` | 4,126,934 / `ee36501822d1` | 38,039 / `e439f6a60a13` |
| ko-zh-tw | 45,219,886 / `65118aabee9f`（未动） | 4,323,857 / `189fde45fc9e`（未动） | 35,487 / `841a26658cb7` |

- 各版 KIT Fixes log 均追加第二轮行（core #20、de #8、en #5、es #6、fr #6、it #5、ja #5、nl #4、pt #4、ru #4、zh-tw #2），Round 列为 `fix rebuild 2, 2026-11-12`。
- ru/es 的 KIT 印/网行括号内保留第一轮值作对照（fix-1 值）；其余 9 版印/网行未动。ru 网行 pdftotext 由 59,174 改为 59,178 字节（`обследовать` 比 `опрашивать` 长 1 个西里尔字母 ×2 处 ×2 字节/字母 = +4）；es 网行 pdftotext 由 52,068 改为 52,070 字节（`,` 1 字节 → `과` 3 字节 = +2）。

## 残留问题

- 无。3 项全部修复并验证；第二轮 87 门的其余结论未变（未重建版 PDF/SVG 与 PROOF-NOTE-2 核实时逐字节一致）。
- 已知非缺陷（沿用第一轮/第二轮裁定，不作改动）：freeze baseline 7/8（P1 大字 "1" 解释器 artefact，文本多重集差 0）；ko-ru 网版 `-layout` 提取比印版少 1 字节空白字符（plain pdftotext 逐字节一致）；p8 keydiff [137,138]（zh-tw [138]）为预期翻译题键；ru 版 `check_p8keys.py` 输出的无空格拼接为检查器 SVG run 拼接假象，印 PDF 文字层空格正常。
- 流程教训（已写入本日志，不另立规则）：`rebuild-fix.sh` / `run_edition.sh` 不设 `set -e`，总 RC=0 不能证明重建成功——`render.py` RC=143 时总 RC 仍为 0，印 PDF 实际未重建。以后每次重建必须逐项核对 `render.py` RC 与印 PDF mtime/SHA，SIGTERM 中断后照第一轮先例整套重跑。

## 同款全局去重缺陷是否可能影响其他家庭的 text.md（只写查到的事实，不修其他家庭）

核查方法（只读，未动其他家庭任何文件）：在 `production/2026-w47/` 全家范围内找 text.md 导出器并 grep 去重写法。

- **查到的事实**：
  - ko 家以外共有三套导出器：`ru_textmd.py`（ru 家 11 份）、`export_zhtw_textmd.py`（zh-tw 家 10 份）、`export-textmd-{en,fr,it,nl}.py`（ja 家 4 份）。其余家庭在 `production/2026-w47/` 内没有以 `*textmd*` 命名的导出器文件。
  - 上述三套导出器中**没有任何一处**含有 ko 家 `textmd.py` 的全局字符串去重写法（`seen.add(norm)` / `if norm in seen` 均 0 命中；`dedup` / `seen` / `unique` 亦 0 命中；`ru_textmd.py` 唯一的 `unique` 是一处注册表键注释，与去重无关；`ru_textmd.py` 内 `not in` / `set()` 去重写法 0 命中）。
  - 全家 `*.py` 中含 `seen` 的唯一非 ko 文件是 `core-ru/dump_cjk.py`（CJK dump 工具，不是 text.md 导出器）。
- **结论（仅就代码写法而言）**：同款“全局规范化字符串去重”缺陷**不存在于其他家庭的导出器代码中**。本次只修了 ko 家，未碰其他家庭。
- **未查的范围（留给协调员的跨家待办）**：本核查只看了导出器代码有无同款去重写法，**没有**对其他家庭的 text.md 做按页 inventory（逐题按页核对）——其他家庭的 text.md 是否因别的机制缺项，本次无法回答，需协调员另派按页核对。

## 收尾

- 3 项全修：R2-1（导出器 + 11 版 text.md 重导出 + 按页核对全过）、R2-2（ko-ru 重渲，门禁全绿）、R2-3（ko-es 重渲，门禁全绿）。KIT 11 版已更新并核对一致。未 commit、未 push、未跑 lint、未碰其他家庭/其他周、未改 SOP。
- 工作文件：`hidden_files/w47/scratch-fix2-w47-ko/`（FIX-LOG-2.md、prefix-fingerprints2.txt、post-fingerprints2.txt、backup-textmd/（改前 11 份 text.md + 改前 textmd.py）、reexport.log、diff-textmd/、inventory-all.log、gates9/、rebuild-ko-ru.log、rebuild-ko-ru2.log、rebuild-ko-es.log、verify-ko-ru.txt、verify-ko-es.txt、update_kit.py、kit-values 隐含于 post-fingerprints2.txt）。
- 磁盘收尾：95G 已用 / 55G 可用（门限 100G，未触发）。
