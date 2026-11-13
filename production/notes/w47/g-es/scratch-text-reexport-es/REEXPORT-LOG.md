# core-es text.md 重导出记录（2026-11-12）

## 任务

协调员裁定：core-es 的 `2026-w47-es-zh-cn.text.md` 必须真实反映 D5 重建后的交付 PDF。
D5 把两处框题副标缩短了（P1「数字看本周」→「数字」、P5「本周计划」→「计划」），
但 text.md 仍是 build-10 版（SHA `509c95fa…`，第 85/793 行为旧副标），与新 PDF 不一致。

## 终态核实（任务第 1 步）

- D5 报告目录 `hidden_files/w47/scratch-d5-rebuild-es/`（本目录的上一级，即 goals hidden_files）
  无 core-es 单独的 `D5-REPORT-es-…md`（报告只覆盖 10 个 fan-out 版），
  core-es 的 D5 事实以 KIT §7 D5 记录 + 磁盘实测为准，均已核实：
  - 印刷版 `La-Lucerna-VOL4.pdf` 4,317,614 B，SHA-256
    `ed100a0f6a176c3121876f39179021d0e8bcfa60ad6c54e9c7aa2cd601711185` ✓
  - 网页版 `La-Lucerna-VOL4-web.pdf` 1,162,044 B，SHA-256
    `5486101f2fdd8e8f7856d71280af300de741b43e45ff18ee39c376f3283e400f` ✓
  - 当前 SVG（2026-11-12 07:22）中 P1 `LA SEMANA EN CIFRAS` 后接 `　数字`、
    P5 `EL PLAN DE LA SEMANA` 后接 `　计划`；旧副标 `数字看本周`/`本周计划` 在 SVG 中为 0 处 ✓
  - D5 五项修复：(1)(3) 为上述两处副标缩短（内容改动）；(2)(4)(5) 为纯降字号 ✓

## 关键发现：原导出器在 D5 版 SVG 上无法复现旧文件

`extract_text2.py`（KIT §3/§7 点名的正规导出器，位于
`hidden_files/w47/scratch-es/extract_text2.py`）用 `len(text)*9` 估算 run 宽、
以 30px 为分段阈值。build-10 时一个视觉行多为单个 `<text>` 元素，该估算不触发；
D5 之后 sans 层拉丁文改走 Newsreader（比 CJK 脸的拉丁字形宽），
一个视觉行被切成多个相邻 `<text>` run，`len*9` 低估宽度达 ~90px，
导致原工具在当前 SVG 上输出 1,915 行、66 个 diff hunk（标题被打碎，
如 `LA SEMANA EN CIFRAS` / `　数字` 各占一行）。

逐字比对（去空白字符流）证明：原工具重导出与旧文件的字符内容只差
两处副标（共 5 字符：`看本周` + `本周`），其余 12 处非等价操作全是
相同字符在附近位置的删+插——即 D5 重排版移动了行断点与段落顺序，
未改任何字符。D5 确实重排了很多行（拉丁文改宽/数字变窄导致 wrap 点移动，
如 gloss 行的 `·` 从行首移到行尾、P8 答案行由两行并为一行），
fix2 也已移动过一处断点（P3 `“魂”`：build-10 在 `“` 后断行，
fix2/D5 因弯引号变窄、`魂` 上了同一行）。因此**任何忠实重导出都不可能
只差 2 行**——任务书“仅 85/793 两行变化”的预期不成立，见下。

## 导出器修订：extract_text2_d5.py（本目录）

与原工具唯一的区别：run 宽改按渲染器自己的 PIL 字体实测
（复用 core-es `svglib.py` 的 `_pil`，同一字体文件/字号/粗细；
`letter-spacing` 按 `svglib.Page.text` 的规则计入 run 尾 advance），
分段阈值改为可配 GAP（默认 10.0px）。其余逻辑（y 分组 ±4px、
栏位分桶、span>900 通栏判定仍用 `len*9`、页脚剔除、文件头）与原工具完全一致。
校准扫描（当前 SVG vs build-10 旧文件，hunk 数越少越接近旧文件）：

| GAP 阈值 | 行数 | diff hunk | 改动行 |
|---|---|---|---|
| 30（原阈值） | 1,645 | 156 | 593 |
| 25 | 1,781 | 71 | 229 |
| 20 | 1,783 | 69 | 223 |
| 15 | 1,802 | 50 | 166 |
| **10（采用）** | **1,803** | **49** | **163** |
| 5 | 1,807 | 52 | 173 |
| 原工具 `len*9` / 30 | 1,915 | 66 | 281 |

选用 GAP=10 的理由：hunk 最少；副标以任务书所述的单行形式出现
（`LA SEMANA EN CIFRAS　数字`、`EL PLAN DE LA SEMANA　计划`），
而原工具会把副标拆成两行；徽章 `B1` 与题号 `5.` 仍保持旧文件的分行
（两者真实间隙 28–29px > 10）。10px 约为 20pt 下的 0.5em，
属“同一视觉行内字距”量级，非逐行手调。

## 安装结果

- 新文件：`production/2026-w47/core-es/2026-w47-es-zh-cn.text.md`
- **1,803 行，43,771 字节，SHA-256
  `449922779d6125dbf685766c620007278cbef51107d164757a35e7710809f419`**
- 旧文件：1,822 行，43,788 字节，SHA-256
  `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`
  （备份：本目录 `text-build10-backup.md`）
- 新副标位置：第 78 行 `LA SEMANA EN CIFRAS　数字`、
  第 782 行 `EL PLAN DE LA SEMANA　计划`；全文无 `数字看本周`/`本周计划` 残留
- 与旧文件的 diff（本目录 `diff-old-vs-new.txt`）：49 hunks / 163 改动行，
  其中 2 处是副标内容改动，1 处是 fix2 已移动的 `魂` 断点，
  其余 46 处全是 D5 重排版的行断点/段落顺序移动。
- 逐字证明（去空白字符流比对）：新文件 29,564 字符 vs 旧文件 29,569 字符，
  差值恰为 −5（`看本周` 3 字 + `本周` 2 字）；其余全部非等价操作
  均为相同字符串的删+插配对（顺序移动），无任何字符增删改。
  （原工具重导出同样满足此证明；`diff-old-vs-orig-tool.txt` 为原工具版 diff。）
- 本目录的 `extract_text2_d5.py`（默认 GAP=10）重跑可逐字节复现已装文件（已验证）。

## 门禁重跑（2026-11-12，全部绿）

- p8 extract：`tools/p8.py extract --p8 …/svg/p8-ejercicios.svg --total 150`
  → **150/150**（parse: lines），rc=0（`p8-extract-reexport.json`）
- p8 compare：当前 SVG vs D5 基线 SVG（`scratch-d5-rebuild-es/core-es/baseline-svg/`）
  → **CLEAN，keydiff=[]**，rc=0（`p8-compare-reexport.json`）；
  新 extract JSON 与 D5b extract JSON 的 noted_set 与 keys 完全相等
- textcheck：`textlayer_check.py La-Lucerna-VOL4.pdf La-Lucerna-VOL4-web.pdf`
  → 印/网均为 **37,908 字符 / 7,266 词**，词多重集差 0/0，
  去空白字符流相等，rc=0（`textlayer-reexport.log`）
  ——与 KIT §7 D5 记录的数值一致，PDF 未动

## 交付说明与待协调员注意

1. **任务书“仅 2 行变化”的核实未通过**——不是导出器没修好，而是 D5 重排版
   真实移动了约 47 处行断点（字符内容已证明只差两处副标）。
   如协调员坚持逐字节只差 2 行，只能手改两行（任务书明确禁止），
   那将使 text.md 的行断点继续停留在 build-10 几何上，与 D5 PDF 的实际排版不符。
   本次按任务书“走导出工具、保证全文与源一致”交付了忠实重导出。
2. 本次修订的导出器只针对 core-es 校准（PIL 字体路径硬编码 core-es 的
   `svglib.py`）；如需推广为各版通用工具，应把字体度量抽成参数，
   不宜直接复用本文件。
3. 其余 10 个 es 版的抽查见主 agent 汇报（本目录外）；本目录只含 core-es 的重导出证据。
