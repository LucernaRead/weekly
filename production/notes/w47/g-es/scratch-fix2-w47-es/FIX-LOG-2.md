# FIX-LOG-2 — W47 es 家庭第二轮修复（G1/G2/G3，均为低）

**任务**：修第二轮独立重校 PROOF-NOTE-2.md（2026-11-12，`scratch-reproof2-w47-es/PROOF-NOTE-2.md`）的 G1（es-ja）、G2（es-pt）、G3（es-ru）。只动 `production/2026-w47/` 内 es 家 3 版目录；其余 8 版（core-es、es-de、es-en、es-fr、es-it、es-ko、es-nl、es-zh-tw）**未动**——无任何源码、PDF、text.md、KIT 改动。第一轮 F2/F3/F4 已验收在版，本轮未复动。不碰其他家庭、其他周；不 commit、不 push、不跑 lint、不改 SOP。解释器全程 `tools/venv/bin/python`。SOP §8：改源头 → 整版重渲染 → 门禁 → KIT → FIX-LOG。

**磁盘**：开工 95G 已用（150G 盘），门限 100G；收尾 95G 已用，未触发停手。

## 改前实测（与 PROOF-NOTE-2 §1 逐一核对，一致）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| es-ja | `La-Lucerna-VOL4-es-ja.pdf` 8,530,855 / `6d89a8ddf67b` | `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,428 / `c2e0230bac8c` | `2026-w47-es-ja.text.md` 46,565 / `998a9ac32500` |
| es-pt | `La-Lucerna-VOL4-es-pt.pdf` 2,914,546 / `434d8d8fe9c6` | `La-Lucerna-VOL4-es-pt-web.pdf` 805,017 / `50f4402a6a19` | `2026-w47-es-pt.text.md` 45,546 / `f9531af2c638` |
| es-ru | `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 / `0ca1beca6d74` | `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 / `2febbe24084b` | `2026-w47-es-ru.text.md` 52,347 / `dadb3e8478e5` |

改前三项逐项复核属实：ja text.md L1772 含「世界遺産」、全版无「無形文化」；pt text.md `você` 恰 5 处、均为标题；ru text.md L208 孤立 `nunca «en las 21:00».`、L327 错置 `пришлите их в редакцию.`、¿Y TÚ? 框尾句缺失（见下）。

## 源头改动（逐项前后对照）

### G1 — es-ja P8 第 30 题答案简析「世界遺産」表述不准（低）

- 位置：`2026-w47-es-ja/content34.py:64`（P8 答案区，`e.ex("A2", "正誤正誤", "Verdadero", …)`）。
- 改前：`ユネスコが2010年にフラメンコを世界遺産に登録`
- 改后：`ユネスコが2010年にフラメンコを無形文化遺産に登録`
- 答案字母 Verdadero 不动；其余 10 版同题未动（均未越界）。
- 核对：改后源码 grep `世界遺産` 0 命中（ja 全版源码）；text.md 全版「世界遺産」0 残留、「無形文化遺産」恰 1 次（P8-30，L1772）。

### G2 — es-pt 标题用 você、正文通篇 tu 形，人称混用（低）

- 改法：标题改回 tu 体（改动最小；正文不动）。
- 改前源码 grep 全版 `você` 恰 5 处、均为标题（已逐一核对，无正文残留）：
  - `2026-w47-es-pt/content12.py:51`：`f.head("AHORA TÚ　Agora você", 25)` → `f.head("AHORA TÚ　Agora tu", 25)`（P1 标题）
  - `2026-w47-es-pt/content12.py:210`：`p.text(… "¿Y TÚ?　E você?" …)` → `… "¿Y TÚ?　E tu?" …`（P2 框标题）
  - `2026-w47-es-pt/content34.py:48`：同上 → `E tu?`（P3 框标题）
  - `2026-w47-es-pt/content34.py:135`：同上 → `E tu?`（P4 框标题）
  - `2026-w47-es-pt/content56.py:53`：同上 → `E tu?`（P5 框标题）
- 核对：改后源码 grep `você` 0 命中；text.md 全版 `você` 0 残留，`Agora tu` 恰 1 次、`E tu?` 恰 4 次；印 PDF 文本层同上（`você` 0、`Agora tu` 1、`E tu?` 4）。

### G3 — es-ru 仅 text.md 两处碎片错位（低；印/网 PDF 均正确）

- 改前 text.md：
  - L208（P2 导语区、日历之前）孤立出现 `nunca «en las 21:00».`；
  - DECIR 段 L321–327 结尾为 `Y para citar un partido: «a las 21:00»,` + `пришлите их в редакцию.`（后半句是 P2 ¿Y TÚ? 框俄语说明的尾句，`content12.py:213`）；
  - L254 起的 ¿Y TÚ? 框俄语说明断在 `…Напишите два / предложения по-испански и`（L297/L300），尾句缺失。
- 改法：行号锚定手术换回两行（源码未动；重生成路径已试行并否决，见下「重生成否决与机制」）：
  1. 删 L208 `nunca «en las 21:00».`；
  2. 在 L300 `предложения по-испански и` 之后插入 `пришлите их в редакцию.`（¿Y TÚ? 框尾句归位）；
  3. L327 `пришлите их в редакцию.` → `nunca «en las 21:00».`（DECIR 段尾归位）。
- 改后 text.md diff（vs `text-pre/`）恰 3 行：`208d207`、`300a300`、`327c327`；总行数不变（1888 行）；DECIR 标题 L321 起 6 行内即见 `nunca «en las 21:00».`（L327），与其余 10 版一致（core 278→284、de 301→307、en 305→311、fr 306→312、it 305→311、ja 297→303、ko 287→293、nl 305→311、pt 307→313、zh-tw 285→291）。
- 与印 PDF 文字层核对一致：印 PDF 文本层 L145 `…que pedirlo en Correos o por internet … пришлите их в редакцию.`（¿Y TÚ? 框内）、L162 `nunca «en las 21:00».`（DECIR 段内）；改后 text.md 两处各在其位。印/网 PDF 未动、不重渲，SHA 不变（见改后 SHA 表）。

## 重建记录

`build2.sh`（`run.py` → `render.py` → `extract_text2_d5.py` 干跑导出到本目录 `text-<版>.md`，不落盘），日志 `build2.log`。

| 版 | run | render（印 / 网，字节） | text 干跑行数 |
|---|---|---|---|
| es-ja | rc=0, TOTAL 150 | rc=0，8,530,586 / 1,280,143 | 2081 |
| es-pt | rc=0, TOTAL 150 | 见下中断与恢复 | 1855（重试后补跑） |
| es-ru | —（未重建，PDF 未动） | — | 1866（干跑，仅用于否决重生成，见下） |

**中断与恢复（2026-11-12 18:12 UTC）**：es-pt 首次 `render.py` rc=143（进程被杀，日志为空；当时内存仅 ~912 MB 可用，疑为 OOM）；核查：8 个 SVG 已全部全新写入（18:11–18:12），印 PDF 已完整写入（8 页，`Agora tu` + `E tu?` ×4 在位），仅网 PDF 未生成（仍为 15:33 旧版）。重试 `render.py`（日志 `render-2026-w47-es-pt-retry.log`）rc=0，印 2,914,243 / 网 804,705（46,446 text bytes），双 PDF 齐全。ja 一次通过，无中断。

## Exporter 陷阱核查（本轮实测）

- 干跑结果（三版均用 `scratch-text-reexport-es/extract_text2_d5.py` 干跑到本目录，不落盘）：
  - es-ja：干跑 2081 行 vs 已装 1820 行，diff 1112 行——全是重分段（行断点/并行移动），且首行误标为 `# 2026-w47-es-zh-cn`（导出器硬编码 core slug）；意改在场（干跑 L2030 `無形文化遺産`）。
  - es-pt：干跑 1855 行 vs 已装 1815 行，diff 357 行，同样重分段 + 首行误标 core slug；意改 5 处标题在场（`Agora tu` ×1、`E tu?` ×4），`você` 0。
  - es-ru：干跑 1866 行 vs 已装 1888 行，diff 299 行，同样重分段 + 首行误标 core slug；**且两处碎片仍错位**——干跑中 `nunca «en las 21:00».` 与 `пришлите их в редакцию.` 相邻于 DECIR 段后（L303–304），并未归位。
- 标题丢失核查：三版干跑与改前逐一比对 `^# ` 标题行——除首行 slug 误标（导出器 artifact，已装文件首行各为本版正确 slug）外，无内容标题丢失；D5 缩字号的 3 处标题（`UNA SEMANA, TRES ESCENARIOS`、`LO QUE QUEDA DE NOVIEMBRE`、`EL FLAMENCO, EN TRES DATOS`）在改后 text.md 中仍各在位（手术替换未动其余行）。
- 结论：与第一轮 FIX-LOG 结论一致——es 家 fan-out 版**不得直接落盘重导出**（会引入数百行重排，违反“最终 diff 只含本轮改动”）；三版 text.md 均用手术式逐行替换落盘（ja 1 行、pt 5 行、ru 3 行换位），每处均先断言原文再替换。落盘后 diff 核查：
  - ja：仅 L1772 一行；
  - pt：仅 L145/247/495/660/880 五行；
  - ru：仅 208 删行、300 增行、327 换行（两处碎片归位）。
  - **无一版含非意改行。**

### 重生成否决与机制（G3）

- 首选路径（重新生成 es-ru text.md）已试行并否决，理由有二：(1) 干跑仍错位——两行在干跑输出中相邻于 DECIR 段后（L303–304），说明错位不在已装 text.md 这一份文件里，而在 SVG 元素顺序本身：DECIR 框与 ¿Y TÚ? 框上下相邻，两框的尾行文本元素在 SVG 文档顺序中被排在了一起，导出器按文档顺序读便把两行都挂在了 DECIR 段后；重导出换一个工具也改不了 SVG 顺序（D5 工具与旧工具均按 SVG 顺序读）。(2) 干跑重分段 299 行 + 首行 slug 误标，直接落盘会污染 diff。
- 因此改用行号锚定手术换回两行（F4 改后重排之疑未证实：错位实为 SVG 元素顺序问题，与 F4 的日历框缩短无直接证据关联；印 PDF 按坐标排版故正确，只有按文档顺序读的 text.md 导出受影响）。机制已如实记于此，text.md-only 修复、PDF 不动。

## 改后 SHA（2026-11-12，盘上实测；完整 SHA-256 见 `post-sha.txt`）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| es-ja | `La-Lucerna-VOL4-es-ja.pdf` 8,530,586 / `cbb3efedd9a2` | `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,143 / `70d46e27721f` | `2026-w47-es-ja.text.md` 46,571 / `29961f6fbc19` |
| es-pt | `La-Lucerna-VOL4-es-pt.pdf` 2,914,243 / `ce89b874dfc0` | `La-Lucerna-VOL4-es-pt-web.pdf` 804,705 / `06514f66f69d` | `2026-w47-es-pt.text.md` 45,531 / `e308de125b8a` |
| es-ru | `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 / `0ca1beca6d74`（未变） | `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 / `2febbe24084b`（未变） | `2026-w47-es-ru.text.md` 52,347 / `8a57918fc0f9` |

改前→改后字节变化：ja 印 −269、网 −285、text +6（「世界遺産」→「無形文化遺産」增 2 字 ×3 字节）；pt 印 −303、网 −312、text −15（5 处 `você`→`tu` 各 −3 字节）；ru 印/网 0、text 0（仅两行换位，字节数不变）。

## 门禁（`gates2.sh` 单实例，`gates2.log`，GATES_RC=0，2026-11-12 18:26 UTC）

p8 compare 用任务书语法 `--core-dir production/2026-w47/core-es --edition-dir <版> --target es --total 150`。全 3 版：freeze 8/8、occlusion 0 flags、p8 extract 150/150、p8 compare CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）、boxtitle 0 DEFECT、spill 0 SPILL、edge 0 TOUCH / 0 NEAR、D5 census PASS。

| 版 | freeze | occlusion | p8 extract / compare | boxtitle（标题/正文行） | spill（27 盒，candidates） | edge | D5 census |
|---|---|---|---|---|---|---|---|
| es-ja | 8/8 | 0 flags | 150/150，CLEAN（keydiff [137,138]） | 26 / 346，0 DEFECT，0 OBSERVE，0 marginal | 0 SPILL，84（84 OBSERVE） | 8 页，0 TOUCH / 0 NEAR | PASS（弯引号 0） |
| es-pt | 8/8 | 0 flags | 150/150，CLEAN（keydiff [137,138]） | 24 / 266，0 DEFECT，0 OBSERVE，0 marginal | 0 SPILL，69（69 OBSERVE） | 8 页，0 TOUCH / 0 NEAR | PASS（弯引号 0） |
| es-ru | 8/8 | 0 flags | 150/150，CLEAN（keydiff [137,138]） | 30 / 372，0 DEFECT，0 OBSERVE，0 marginal | 0 SPILL，72（72 OBSERVE） | 8 页，0 TOUCH / 0 NEAR | PASS（弯引号 0） |

附加核查（全部通过）：
- 印/网 PDF 各 8 页、1462.5×2025 pt、均 < 7 MB；pdftotext（无 `-layout`）逐字节一致：ja 47,487 字节、pt 46,446 字节、ru 53,420 字节（ru 与第一轮一致，PDF 未动之证）。
- P8 答案 1–150 全有（三版 text.md 正则重数，缺失 []）。
- U+201C/U+201D 普查 0：三版 text.md 各 0 次；D5 census SVG 内弯引号总数 0。
- G1 核对：ja 全版「世界遺産」0 残留（text.md 与印 PDF 文本层）、「無形文化遺産」在 P8-30 在位。
- G2 核对：pt 全版 `você` 0 残留（源码、text.md、印 PDF 文本层），标题 5 处均为 tu 体。
- G3 核对：ru text.md 两处归位（DECIR 尾行 L327、¿Y TÚ? 尾句 L300）；印 PDF 文字层对照一致；印/网 SHA 不变。

## KIT 更新

3 版 `WEEKLY-KIT.md` 各末尾追加一节「第二轮独立重校修复 G1/G2/G3（2026-11-12，PROOF-NOTE-2 (b) 返修）」，含：改动摘要、重建方式、新印/网/text.md 尺寸与完整 SHA-256、门禁全绿摘要、日志路径。es-ru 的 KIT 节注明 PDF 未变、只更新 text.md SHA。D5 行保留未动。SHA 均以重渲/落盘后盘上实测为准，未抄旧报告值。

## 不动项

- 其余 8 版（core-es、es-de、es-en、es-fr、es-it、es-ko、es-nl、es-zh-tw）只字未动。
- 未动 `tools/`、未动模板/引擎代码、未动其他家庭与周次；未 commit、未 push、未跑 lint。

## 残留问题

无。
