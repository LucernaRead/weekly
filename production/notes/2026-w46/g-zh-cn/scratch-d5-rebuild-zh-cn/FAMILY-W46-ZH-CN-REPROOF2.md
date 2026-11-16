# FAMILY-W46-ZH-CN-REPROOF2.md — W46 zh-cn-ru D65 fix 独立重校（reproof v2）

- 版：`2026-w46-zh-cn-ru`（W46 zh-cn 家，VOL.3）；缺陷 D65：P1 读者行（y=612 SVG）末字 Й 侵入右栏奶油框左缘
- 修复（待 closer 落仓）：`content12.py:23` 字号 16 → 15.5pt，仅此 1 行
- 准绳：`FAMILY-W46-ZH-CN-RU-FIX.md` 全文；builder 终轮 pin：`FAMILY-W46-ZH-CN-BUILD.md` §9 ru 行（印 `160e613d…93ddd6`、网 `f82d449b…`、text `dbfeee6c…`）
- 工作区：`hidden_files/d5-redo/scratch-2026-w46-zh-cn-ru-reproof2/`（`src/` = 重建源 + 重建件，`core/` = 自 production core-zh-cn 现建的 G8 参照，`gates-fix/` = 门禁日志，`logs/` = 构建/量测日志）
- 仓库 HEAD（开工/收工一致）：`b124ab6d3aa5d1ce5d1f7ab5577d2150058bb077`；磁盘：150G 盘已用 80G、可用 69–70G（< 100G 门限）
- 未做的事：未 commit/push；未跑 `lint --write`；未跑 `insert.py`；未改 `production/`、`issues/`（只读）；未写 fix worker 的任何路径（只读 `patched/`）

## §0 方法

- 源：rsync fix `patched/`（排除 PDF / text.md.new / svg / cards / `__pycache__`）进我方 `src/`，`diff -rq` 核对：除被排除的构建输出外 **SOURCES-IDENTICAL**；production `content12.py` 与 fix `patched/content12.py` 的 diff 仅第 23 行（16 → 15.5）。
- 重建：builder 同款流程，解释器 `~/workspace/weekly-git/tools/venv/bin/python`：`run.py`（rc=0，TOTAL 150：A2 56 / B1 69 / B2 25）→ `render.py`（rc=0，内调 webpdf）→ `textexp_zh_cn.py`（rc=0，1,886 行）。
- 门禁：fix 轮 `run_gates.py` 的副本，仅改路径（`patched/` → 我方 `src/`，日志路径 → 我方 `logs/`），口径/阈值未动；G8 core 参照自 production `core-zh-cn` 源现建（`run.py` rc=0，TOTAL 150；图文件按 D20/D58 同款做法自 fanout 补，moth SHA `42487693…` 与 fix core 一致）。
- bbox：fix `measure_bbox.py` 副本，仅把 `fix(rebuilt)` 指向我方重建网 PDF；框缘独立实测（P1 奶油 rect x0）。
- 目检：fitz 自我方重建网 PDF（run1）与终轮已发 issues PDF 渲染同一区域（pt x 950–1120、y 420–480，3×；全幅带图 pt x 0–1462.5、y 380–520，1.5×），已真打开看。
- G15a (b)：`git show ab8972a6:issues/2026-w46/2026-w46-zh-cn-ru/2026-w46-zh-cn-ru.pdf` 单文件提取进我方 `logs/pre-closer-ru.pdf`（2,275,749 B），只读使用。

## §1 独立重建 SHA 核对

| 交付物 | 字节 | SHA-256（全值） | vs FIX §2 |
|---|---|---|---|
| 印 PDF `Lucerna-VOL3-RU.pdf` | 29,054,076 | `f5ba3a64a50a66494b8e4ccb8394d86c0223098d465ffb72879323fcec349a43` | **全等 ✓** |
| 网 PDF `Lucerna-VOL3-RU-web.pdf`（run1） | 2,321,090 | `a14e4afb0fc1ca8734ad887e7313937bef39f8c22cae34b60358f3efd0596694` | **不等，见下（工具链非确定性，已证实，非 fix 缺陷）** |
| text.md.new `2026-w46-zh-cn-ru.text.md.new` | 51,516 | `dbfeee6c30645a9f5278fa60fcdaf4e8522be900e4a8f87abeda4cc5e7bb7fde` | **全等 ✓** |

- text.md.new 与已落仓 production `2026-w46/2026-w46-zh-cn-ru/2026-w46-zh-cn-ru.text.md`、issues `2026-w46-zh-cn-ru.text.md`、fix `.text.md.new` 三方 **逐字节一致**（`cmp` 全过）。
- SVG 8/8 与 fix `patched/svg/` **逐字节一致**；cards 一致。
- 网 PDF SHA 不等的原因（已证实为工具链非确定性，非内容差）：
  - 同源二次渲染（render2，rc=0）：印 PDF 仍字节全等（同一 SHA `f5ba3a64…`），网 PDF 又得第三个值——2,321,110 B，SHA `7975d372c60e6474e35709510aa60119582dce4297127607e45471da55aaadc4`。三次同源构建网 PDF 字节各不相同：builder run1 2,321,088 B / fix 2,321,118 B / 本轮 run1 2,321,090 B / 本轮 run2 2,321,110 B。
  - 对象级比对（我方 run1 vs fix 网 PDF）：429 个对象键全同；55 个不同对象**全部**是字体子集流（含 `/Length1`），内容流/结构对象 0 不同；解压后字体字节亦各不相同（子集化逐次重排）。
  - 文本层：我方网 PDF vs fix 网 PDF **8/8 identical**；vs 已发 issues PDF **8/8 identical**（每页字符数 2417/2548/1907/2133/1907/2274/2966/7469）；元数据无日期；P1 字体子集标签两边相同。
  - 结论：网 PDF SHA 无法被任何独立重建复现（FIX §7 自身亦记 "webpdf 字体子集非确定性"）。closer 落仓时以 fix 工人交付件（`68b66dda…`，2,321,118 B）为准，其内容已由本文本层 + SVG + 印 PDF 三重证实与我方重建一致。印 PDF 与 text.md.new 的 SHA 全等是确定性交付物的硬核对。

## §2 bbox 三值复测（主验收）

方法：fitz 读网 PDF 文本层 P1，取 y=612 SVG 行（基线 459pt 附近）span bbox x1；SVG 单位 = pt ÷ 0.75；余量 = 1439.5 − 行末。框缘 1439.5 SVG 由 P1 奶油 rect x0=1079.62pt ÷ 0.75 得出，**三版独立实测同值**（rect y 441.0–966.0pt 覆盖读者行）。

| 轮次 | 行末 bbox | 行末（SVG） | 余量 | 字体 | 行中心（SVG） |
|---|---|---|---|---|---|
| 基线 fanout（pre-D5） | 1077.23pt | 1436.3 | **+3.2** | 12.00pt | 977.4 |
| 终轮 run1（已发 issues PDF） | 1084.19pt | 1445.6 | **−6.1** | 12.00pt | 977.0 |
| **修复后（本轮重建网 PDF）** | **1073.14pt** | **1430.9** | **+8.6 ✓** | **11.62pt（= 15.5 × 0.75）** | **976.8** |

- 三值与 FIX §3 **逐位一致**（基线 +3.2 / 终轮 −6.1 皆复现，方法可信）。
- 修复后余量 **+8.6 ≥ +8，PASS**；行中心 976.8，仍居中 ~975（终轮 977.0、基线 977.4，同量级偏移，系该行固有排版）。

## §3 目检

- **修复后（`p1-crop-fix.png`，自我方重建网 PDF）**：`ЧИТАТЕЛЕЙ` 的 Й（含上标短音符）完整落在白底上，Й 与右侧奶油框左缘之间有清晰可见的白间隙，无相贴、无越线。**PASS。**
- **终轮对照（`p1-crop-final.png`，已发 issues PDF）**：同一位置 Й 的右部被奶油框切掉、短音符剩半截——缺陷复现，确认修复针对真问题。
- **带图（`p1-band-fix.png`）**：读者行居中完整，右栏 `本周日历` 奶油盒无侵入，其余 P1 元素无变化。

## §4 终轮门禁复核表

`GATES-SUMMARY 2026-w46-zh-cn-ru round=reproof2`：**PASS 19 FAIL 1 of 21**（另 G15b 仅记录）。与 FIX §5 逐值对照：

| 门 | FIX §5（fix 轮） | 本轮（reproof2） | 对照 |
|---|---|---|---|
| G1 | PASS TOTAL=150 FLOW=0 HEAD=0 | PASS，同值 | ✓ |
| G2 | PASS rc=0 findings=0 | PASS，同值 | ✓ |
| G3 | PASS D5_lat=0 D5_cyr=0 curly_cjk=0 noto_sans=798 | PASS，同值 | ✓ |
| G4 | PASS render rc=0 print 29,054,076 B | PASS，同值 | ✓ |
| G5 | PASS web 2,321,118 B | PASS web **2,321,090 B** | 字节差 −28 B，§1 工具链非确定性；< 7MB，PASS 不受影响 |
| G6 | FAIL 1 旗 caron，同文 | FAIL 1 旗，同文 `[TEXTX] p1-touiban.svg 'ǒ' — ink overlaps 'bāogu' by 3.2x15.8px` | ✓ 已裁定 D62，残留 |
| G7 | PASS 150/150 | PASS，同值 | ✓ |
| G8 | PASS CLEAN keydiff=[] | PASS，同值（我方现建 core 参照） | ✓ |
| G9 | PASS freeze 8/8 rc=0 | PASS，同值 | ✓ |
| G10 | PASS cjk 0 / latin 111 / unexp 111 | PASS，同值 | ✓ |
| G11 | PASS spill=0 observe=105 set==baseline:True | PASS，同值 | ✓ |
| G12 | PASS defect=0 observe=0 marginal=0 | PASS，同值 | ✓ |
| G13 | PASS touch=0 near=0 | PASS，同值 | ✓ |
| G14 | PASS defects=0，P8 lines 242->242 slack 43.0->43.0 | PASS，同值 | ✓ |
| G15a | PASS（pdfdiff vs issues IDENTICAL） | PASS，同值（见 §5a） | ✓ |
| G15b | RECORD rc=1，`8x 'ты' \| 7x '周' \| CARRYOVER: FAIL` | RECORD rc=1，同值（底层日志逐行一致；我方 runner 摘要行仅取了 `CARRYOVER: FAIL`，属摘要提取形式差，非量测差） | ✓ |
| G15c | PASS，934 entries vs ref 933；家具 98，word-split 1，UNEX 0 | PASS，同值（底层输出逐行一致；我方 runner 摘要行仅取了 `ADOPT: 0 UNEXPECTED`，同上） | ✓ |
| G16 | PASS defective quotes=0 | PASS，同值 | ✓ |
| D18 | PASS gap=253.5 date_x=1511.2 slogan_end=1257.7 | PASS，同值 | ✓ |
| D37 | PASS margin +12.5（工具值） | PASS margin +12.5，同值 | ✓ |
| D37-sub | PASS margin +229.9 | PASS，同值 | ✓ |

- D37 门禁值 vs bbox 值：工具 +12.5 vs bbox +8.6，差 **+3.9**（工具高估），与 FIX §8 所记 +3.9 一致；**以 bbox 为准**（D65）。
- 各门底层日志与 fix 轮逐一比对：除路径（`src/` vs `patched/`）与 G5 字节外全部一致。

## §5 G15a 两项复核（D67）

- **(a) fix 输出 vs 已落仓 run1 issues PDF：PASS。** fix 工人网 PDF vs issues PDF：pdfdiff **8/8 identical**（每页字符数 2417/2548/1907/2133/1907/2274/2966/7469）；我方重建网 PDF vs issues PDF 同样 8/8 identical。fix 未引入内容变化。
- **(b) fix 输出 vs 发前旧版 PDF（`git show ab8972a6:…`）：PASS（D61 仍在）。** pdfdiff：**P1 DIFF only-old=[('—', 1)] only-new=[]**，其余 7 页 identical。`—` 丢失（D61）仍在：旧版有、新件无。D61 未被推翻，家族级 G15a vs 发前旧版仍为 FAIL（与 FIX §5 末段的说明一致）。

## §6 D19（引用复核，D48 修正逻辑）

- FIX 报告全部 `:NN` 引用共 4 处，皆为 `content12.py:23`，**0 坏**：
  - §6：`content12.py:23` 指向修复行本身——patched 该行即读者行 `p.text(975, 612, …)`，行内含新字号字面量 `15.5`；`15.5` 在 `patched/content12.py` 全文件仅出现 1 处（即第 23 行，已 grep 核实）。
  - §6：无 `f.box` 引用、无其他修复引用——全文 grep 确认，唯一的 `:NN` 引用即上述 4 处。
  - §7 表：production `2026-w46-zh-cn-ru/content12.py:23` 16 → 15.5——production 该行旧值 `16` 已核对，patched 差分仅此 1 行。
  - §7 表：KIT fix 条目 `content12.py:23` 16 → 15.5——为 closer 追加项，指向修复行本身；落仓 KIT 现无此引用（见 §7）。
- FIX §1 其余可核对陈述：production→patched diff 仅 1 行 ✓；`15.5` 全文件唯一 ✓；图文件来源与 moth SHA `42487693…` ✓（我方 core 补图同 SHA）。

## §7 KIT F2 状态

- 已落仓 production `2026-w46-zh-cn-ru/WEEKLY-KIT.md`：**F2 "ALL-GREEN" 修正文案已在**——L175–176 为：
  - `run1 即终轮：修复 0 处（只降字号、不改文案），见下表；run2 门禁：终轮 run1：18/21 PASS（另 G15b 仅记录）；残留 FAIL：G6, G15a（…均为已裁定项…）。`
  - `修复 0 处：run1 即终轮（18/21，残留 G6 + G15a 已裁定项），无需降字号。`
- 全文 grep：`ALL-GREEN` **0 命中**；`content12.py:23` **0 命中**（尚无 fix 引用，closer 追加项，reproof v2 只记录、不替 closer 改）。
- **FIX §7 称"仍需修正"是错误的**（finding R-1，见 §8）：其 §7 表"旧值"栏引用的 "修复 0 处：run1 即 ALL-GREEN" 是 F2 修正前的旧文案（家族 REPROOF §4 F2 指出），落仓 KIT 已是修正后文案。closer 只须追加 fix 条目，**不得**重做 F2 修正。

## §8 结论 + finding 清单

**结论：PASS。** 独立重建印 PDF 与 text.md.new SHA 全等、bbox +8.6 ≥ +8、目检 PASS、门禁 19/21（仅 G6 FAIL 已裁定 + G15b RECORD）、G15a 两项复核成立、D19 0 坏。网 PDF SHA 不等已证实为工具链字体子集非确定性（§1），非 fix 缺陷，不阻塞。可派 closer（按 FIX §7 落仓：content12.py:23、印/网 PDF、issues PDF + frontmatter `pdfBytes: 2321118` / `pdfSha256: 68b66dda…`、KIT 追加 fix 条目；text.md 不动）。

| # | finding | 类别 | 处理 |
|---|---|---|---|
| R-1 | FIX §7 KIT 行"旧值"栏误引 F2 修正前文案 "run1 即 ALL-GREEN"，并指示 closer"按 F2 修正'ALL-GREEN'文案"——落仓 KIT L175–176 已是修正后文案，`ALL-GREEN` 0 命中 | 文本类（报告误引） | closer 落仓时原地忽略该半句，只追加 fix 条目（`content12.py:23` 16 → 15.5，D37 bbox +8.6 / 门禁 +12.5，终轮门禁记为 fix 轮 19/21 残留仅 G6）；无须针对性复验 KIT 以外内容 |
| R-2 | FIX 附录列 `logs-textexp.log`，fix 工作区实际无此文件（仅 logs-run / logs-render / logs-core-run / gates-fix-run） | 文本类（报告琐误） | 无须处理；textexp 本轮已独立重跑 rc=0、1,886 行 |
| O-1 | 网 PDF SHA 不可复现（三次同源构建三值：2,321,088 / 2,321,118 / 2,321,090 / 2,321,110 B），55 个差异对象全为字体子集流 | 观察（工具链属性，非 finding） | 已在 §1 记录；closer 以 fix 工人交付件 `68b66dda…` 为准；今后 reproof 以文本层 + SVG + 印 PDF SHA 为网 PDF 等价判据 |
