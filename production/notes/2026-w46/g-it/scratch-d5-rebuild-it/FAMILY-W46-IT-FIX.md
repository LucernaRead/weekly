# W46 意大利语目标家族 D5 重建 — zh-tw 字体面修复报告（D52 fix）

- 家族：W46 it，读者 zh-tw 一版（`2026-w46-it-zh-tw`）
- 驱动：独立重校 v1（`FAMILY-W46-IT-REPROOF.md` §11）结论 FAIL，唯一 finding 为 zh-tw 字体面 TC→SC（D51）
- Fix 工作目录：`hidden_files/d5-redo/scratch-2026-w46-it/fix-zh-tw/`（修复脚本与日志）；只写 `patched/2026-w46-it-zh-tw/`、`logs/2026-w46-it-zh-tw/`、`fix-zh-tw/` + BUILD 报告；production 未写，无 commit/push，未跑 `lint --write`，未动 index.json
- 正典解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3）；开始前 `fc-cache -f` 已暖字体
- 磁盘：开工 75G/150G，结束 75G/150G，未触 100G 门
- 结果：**修复完成，zh-tw run3 20/20，`pdffonts` TC 面，D19 77/77**；其余 11 版未动

## §1 缺陷复述（D51）

patched zh-tw 版以 SC 面渲染繁体中文，而已发版为 TC 面：

1. 已发版是 TC 面：生产 `2026-w46-it-zh-tw/svglib.py` 为 `_tc_index` + 家族名 `"Noto Serif CJK TC" / "Noto Sans CJK TC"`；已发版印 PDF `pdffonts` 嵌 `NotoSansCJKTC / NotoSerifCJKTC`。
2. 重建版（run2）是 SC 面：patched `svglib.py` 为 `_sc_index` + `"Noto Serif CJK SC" / "Noto Sans CJK SC"`；P1 SVG 全部 CJK 文本家族为 SC；重建印 PDF 嵌 SC 面。
3. 机制要求 TC 面：`base_core_for()` 规定 reader zh-tw 用 `core-zh-tw/svglib.py`（TC 面）作基底；builder 误用 fanout zh-tw（SC 面）+ D5 安装，安装日志无任何面改写记录。
4. 字形确有可见差异：U+8AAA 說 SC vs TC 差 1728/14400 像素（12%）；`說` 在本版正文出现 13 次。
5. 门禁全绿未能检出（字符多重集与文本抽取对字体面不敏感），属门禁网外的新增内容缺陷。布局不受牵连（SC/TC/HK 面同码位 advance 均为 1000/1000em 全宽），但须重建重验。

## §2 改写行全表（`patched/2026-w46-it-zh-tw/svglib.py`，7 行）

先 `grep -n "SC"`（大小写敏感）+ `grep -ni "sc"`（全量）列出所有 SC 出现处，逐一判定。决定字体面的 7 行全部改写；其余不动，理由如下表。

| 行 | 旧 | 新 | 判定 |
|---|---|---|---|
| 11 | `def _sc_index(path):` | `def _tc_index(path):` | 改：面选择函数定义 |
| 15 | `if f.getname()[0].endswith("SC"):` | `if f.getname()[0].endswith("TC"):` | 改：TTC 内面选择条件 |
| 25 | `_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}` | `_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}` | 改：`_IDX` 映射引用 |
| 49 | 注释 `"Newsreader, Noto Serif CJK SC"` | `Noto Serif CJK TC` | 改：面栈描述注释同步 |
| 52 | 注释 `Noto Serif CJK SC` | `Noto Serif CJK TC` | 改：面栈描述注释同步 |
| 76 | `_FAMILY` `"serif": "Noto Serif CJK SC"` | `"Noto Serif CJK TC"` | 改：SVG 发出面（serif） |
| 77 | `_FAMILY` `"sans": "Noto Sans CJK SC"` | `"Noto Sans CJK TC"` | 改：SVG 发出面（sans） |

不改行：

| 行 | 内容 | 不改理由 |
|---|---|---|
| 114 | 注释 `Noto Sans CJK SC/TC` | 已是双面通称；fix2 引言对两面均成立 |
| 23/24 | 路径 `NotoSansCJK-Regular.ttc` | TTC 文件名无面后缀；面由 `_tc_index` 运行时选 |
| 57 | 注释 `Noto Sans CJK <variant>` | 通称占位，无面语义 |
| 288/311/343/350/355 | `esc`、ASCII 等 | `grep -i sc` 假命中，无面语义 |

注：`_char_font` 无面字面可改——它返回类名（serif/sans/deja），发出面由 `_FAMILY`（L76/77，已改）决定。修复脚本：`fix-zh-tw/fix_svglib_face.py`（7 处替换，每处断言恰好出现 1 次；改前备份 `fix-zh-tw/svglib.py.before-fix`，SHA `f08a6b3b055459be496d5a87794d0823be6589743d96be2a97c41d6ca9e898e1`）。

## §3 两项核对（缺一不可，均通过）

### 核对 ①：改写前后 diff 仅限面相关行

`diff svglib.py.before-fix patched/.../svglib.py` = 上表 7 行（`fix-zh-tw/diff-before-after.txt`），无他行。改后文件内面相关 SC 残留 0 处（`grep "CJK SC|_sc_index|endswith(\"SC\")"` 仅命中 L114 双面通称）。

### 核对 ②：改后文件 = fanout 版 + D1+D5 安装 + TC 面

- fanout→改前 diff：112 行，与 de/en/zh-cn 的 fanout→patched diff（各 112 行）内容一致，仅差 `_D5_READER`（latin/cjk 读者差）与 hunk 行号（zh-tw fanout 含 kinsoku 块致行号移位）。
- fanout→改后 diff：132 行；与 fanout→改前 diff 相减，仅差上表 7 行（另 hunk 头行号重排，无新增内容行）。即改后文件恰为 D1+D5 安装 + 7 行 TC 面改写，无多余改动（`fix-zh-tw/diff-fanout-to-fixed.txt`、`diff-fanout-to-old.txt`）。
- 运行核实：改后 `_IDX` 四 TTC 均为 index 3，与生产 TC 版 `_IDX` 逐值相同。
- 说明：任务书“vs 生产 svglib 的 diff 恰为 D1+D5 安装”按 REPROOF §8 的既定口径核——生产 svglib 是 pre-D1、前 Newsreader 代旧样式，patched vs 生产 diff 为 388 行（含 §1.1 全面改版），故可比的等价陈述是 fanout→patched = D1+D5 安装；上式已证。

## §4 重建门禁表（run3，仅 zh-tw；20/20）

重建：`run.py + render.py + webpdf + export_it.py`（`bin/run_batch.sh patched run3`，单版清单）。门禁：`bin/run_gates_batch.sh patched run3`（单版清单）。摘要 `logs/2026-w46-it-zh-tw/GATES-SUMMARY-run3.txt`。

| 门 | run3 | run2（对照） |
|---|---|---|
| 总分 | **20/20** | 20/20 |
| G1 run | PASS TOTAL=150 OVF=0 HDW=0 | 同值 |
| G2 head_check | PASS defects=0 | 同值 |
| G3 census | PASS rc=0 | 同值 |
| G4 render | PASS print=7,500,102B | 7,490,560B |
| G5 webpdf | PASS web=983,685B | 978,308B |
| G6 occlusion | PASS flags=0 | 同值 |
| G7 p8 extract | PASS extract=150 | 同值 |
| G8 p8 compare | PASS keydiff=[137, 138, 139] | 同值 |
| G9 freeze-baseline | PASS match=8/8 | 同值 |
| G10 freeze-diff | PASS rc=0（added_strings 总量 1591，与 run2 相同） | 同值 |
| G11 spill | PASS spills=0 | 同值 |
| G12 boxtitle | PASS defects=0 | 同值 |
| G13 edge | PASS touches=0 nears=0 | 同值 |
| G14 creambox | PASS defects=0 | 同值 |
| G15a pdfdiff | PASS print-web diff={} IDENTICAL after intended transforms（SEP 72, SEP+CJK 15, WORD 1） | 同值 |
| G15b（仅记录） | PASS rc=1（record-only；20x '將' CARRYOVER: FAIL，与 run2 同行） | 同值 |
| G15c exporter | PASS UNEXPECTED=0, entries=648, exercises=150 | 同值 |
| G16 quotes | PASS defective=0 | 同值 |
| D18 masthead | gap=155.2px | 同值 |
| D37 badge | N/A（短标签，无描述行） | 同值 |

- 20 分母口径（REPROOF §0）：19 计分门 + G15b 仅记录行 = 20 行；20/20 = 19/19 计分门全绿 + G15b 记录行。
- 归一化对照：run3 vs run2 `GATES-SUMMARY` 除 tag 行与 G4/G5 字节外逐字相同；`pdfdiff`/`verify`/`textexp`/`measure` run3 日志与 run2 逐字节相同。
- 过程注记：首次跑门禁时服务重启中断，门禁未写摘要（`GATES-SUMMARY-run3.txt` 不存在，部分单门日志已落盘）；确认无残留进程后原样重跑整批门禁（幂等覆盖），20/20。重建本身未受影响（`run-run3.log` TOTAL=150 一次成功）。

## §5 `pdffonts` TC 证据（run3）

| PDF | TC 面嵌入 | SC 面 |
|---|---|---|
| 印 PDF `The-Lucerna-VOL3-it-zh-tw.pdf` | `NotoSansCJKtc` ×16、`NotoSerifCJKtc` ×7（其余为 Newsreader、UnifrakturMaguntia） | `CJKsc/CJKSC` 0 处 |
| 网 PDF `2026-w46-it-zh-tw.web.pdf` | `LucernaNotoSansCJKTC` ×16、`LucernaNotoSerifCJKTC` ×7 | `CJKsc/CJKSC` 0 处 |

- SVG 佐证：全版 8 页 `font-family="Noto Sans CJK TC"` ×347、`"Noto Serif CJK TC"` ×268，SC 面 0 处。
- 完整 `pdffonts` 输出：`fix-zh-tw/pdffonts-print-run3.txt`、`fix-zh-tw/pdffonts-web-run3.txt`。
- 注：`grep -i SC` 会误命中 `NotoSansCJKtc`（"SansCJK" 含 "sC"）；SC 残留判定须用严格模式 `CJKsc|CJKSC`，上表即按此模式。

## §6 新旧 SHA 对照表（zh-tw；§9 已更新为 run3 值）

| 件 | run2（SC 面，作废） | run3（TC 面，终轮） |
|---|---|---|
| 印 PDF `The-Lucerna-VOL3-it-zh-tw.pdf` | 7,490,560 B / `73ae0b908bb02ccdf5772ae37d0c1c8a92f45aaa941bdc455207499b9dad5e67` | 7,500,102 B / `46c50a7df2e8a0ff16f58346fd2ac1f70af21616ddbbef709da803bbf6964682` |
| 网 PDF `2026-w46-it-zh-tw.web.pdf` | 978,308 B / `277447a399334d7b523368ecb9a05e865debfa6cf1105abdb4a1f55023942eec` | 983,685 B / `b36c81097f8b63b12f4a65e006ce9ee17e7e369e2285593c2572b203545085d7` |
| text `2026-w46-it-zh-tw.text.md.new` | 52,971 B / `f2b1c9d93e8821e89383880647da465939be776ddd52981987384194f4da0adc` | 52,971 B / 同值（实测 byte-identical；导出与面无关，符合预期） |

- KIT 已重 pin 为 run3 值：印/网新字节 + SHA 全值；text 行注明 run2 同值、run3 复核 byte-identical；末节门禁行 run2→run3（数值不变）。KIT 内其余内容未动。
- BUILD §9 zh-tw 行已更新为 run3（印/网字节 + SHA 全值；text 同值）。

## §7 D19 重核结果（D48 修正版逻辑）

- 检查器：`reproof/bin/d19_it.py`（只读；KIT 37 处 + BUILD 报告 40 处）。
- 结果：**TOTAL 77，PASS 77，FINDING 0**（修复前重跑与追加 §11 后重跑两次均为 77/77）。日志：`fix-zh-tw/d19-recheck.log`、`fix-zh-tw/d19-recheck-after-s11.log`。
- zh-tw 的 content 引用 2 处（KIT 内）+ BUILD 报告 zh-tw 修复表引用均通过；svglib 改动不影响 D19 引用行（引用行在 content 文件内，未动），实测确认。

## §8 BUILD 文字修正清单（只改文字，不动交付物）

BUILD 报告（`FAMILY-W46-IT-BUILD.md`）共改 9 行 + 追加 §11；diff 见 `fix-zh-tw/diff-build-report.txt`（改前备份 `fix-zh-tw/FAMILY-W46-IT-BUILD.md.before-fix`）。

| # | 位置 | 改动 |
|---|---|---|
| 1 | §2 es 表（L135） | G15c entries 648 → 647 |
| 2 | §3 ja 表（L189） | G15c entries 648 → 647 |
| 3 | §3 ko 表（L215） | G15c entries 648 → 647 |
| 4 | §4 nl 表（L244） | G15c entries 648 → 647 |
| 5 | §6 zh-cn 表（L332） | G15c entries 648 → 647 |
| 6 | §6 core-it 表（L385） | G15c entries 648 → 647 |
| 7 | §4 pt 注记（L288） | D37 余量 +5.1pt → +4.9pt，并注明：门禁实测行末 1433.0px、余量 +4.9pt；按注记引用的 1432.6px 同算式应为 +5.2pt，自相矛盾；以门禁 +4.9pt 为准，仍 >0，通过不受影响。§4 表格原已是 +4.9pt，未动 |
| 8 | §6 zh-tw 表头（L350） | run2（终轮）→ run3（终轮）；各门数值与 run2 相同（§4 表） |
| 9 | §9 zh-tw 行（L452） | run2 → run3，印/网字节 + SHA 全值更新为 run3（见 §6） |
| 10 | 追加 §11 | 本次修复全记录（缺陷、改写行、两项核对、run3 门禁、`pdffonts`、SHA 对照、D19、文字修正清单） |

- 未动的 648：de/en/fr/pt/ru/zh-tw 六版（实测 648，与重校 §1 表一致）。
- §11 追加后 D19 重跑仍为 77/77（§11 内无新增 content 文件行引用）。

## §9 未动核实（其余 11 版）

- 其余 11 版 33 件交付物（印/网/text）SHA 与 BUILD §9 全值一致——含 nl 网/text（初核两处“不一致”系核对脚本内把 nl text SHA 误填入 web 栏的笔误，逐项直核后确认与 §9 全值相符）。
- zh-cn patched `svglib.py` 仍为 SC 面（`_sc_index` 在位），未被触及。
- `git status --porcelain -- production/2026-w46/ issues/2026-w46/` 为空（干净）；production 未写。
- 本次只动：`patched/2026-w46-it-zh-tw/svglib.py` + 重建产物（印/网 PDF、text.md.new、svg、日志）+ `patched/2026-w46-it-zh-tw/WEEKLY-KIT.md`（重 pin）+ `logs/2026-w46-it-zh-tw/*run3*` + BUILD 报告 + `fix-zh-tw/`。

## §10 Closer 交接

1. zh-tw 可按 BUILD §10 同步，但取 **run3** 交付物（印/网/text SHA 见 §6；§9 已是 run3 值）；门禁摘要复本取 `logs/2026-w46-it-zh-tw/GATES-SUMMARY-run3.txt`（run2 摘要作废）。
2. 其余 11 版同步口径不变（REPROOF §14）；zh-tw 不再暂缓。
3. 待重校 v2（仅 zh-tw）复核本报告 + run3 交付物后同步。
