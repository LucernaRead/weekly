# MECHANISM-FIX-REPORT — W47 it 家庭「翻譯」标签机制修复简报（给协调员）

**日期**：2026-11-11
**修理工**：fix-export-it1
**机制目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-it/`
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-export-it1/`

## 根因（一句话）

fan-out 翻译表有意不映射 type「翻譯」（W46 前例），E 节 4 道题的 type 字符串未经翻译进入各版 `content8.py`，出口商逐字照印，导致 8 版 text.md 第 E 节 Q137–140 行残留中文「翻譯」标签。it-es fix1（commit 8f2bba56）只手修了 text.md，**重 fan-out 会把它洗掉**，所以必须先修机制。

补充核实：`Flow.ex` 不渲染 type（PDF 无此标签），P8 答案循环比对的是「写作」类型而非「翻譯」，故本修复只影响 .text.md，不动 PDF。

## 方案（已实施，改动最小、全家覆盖）

选 **(i) 翻译表补映射**，弃 (ii) 出口商本地化（需改已发版周 W46 的共享出口商、且只修 text.md 不修源头）。

改了 **2 个文件**（均在 goals 侧机制目录，无 commit、无 push）：

1. **`translations.py`**：新增 `"翻译"` 条目 → en Translate / de Übersetzen / fr Traduire / es Traducir / pt Traduzir / nl Vertalen / ru Переведите / ja 翻訳 / ko 번역하기 / zh-tw 翻譯（表 239→240 条）；头注释的"W46 前例 kept as-is"说法已更正。取值依据：en/es 为已确立的既有结果（it-en 磁盘 text.md、it-es fix1），其余取与同区类型标签一致的词形（见 FIX-LOG §3.1）。
2. **`build_edition.py`**：`consumed` 加 `"翻译": 4`（E 重定向消耗 4 处 instr，剩下 4 处 type 走表；库存 8−4=4，计数断言兜底）；**残留 CJK 门收紧为零容忍**（旧门豁免含「翻譯」的行，漏网会静默通过；现在任何残留 CJK 都让 build 当场死掉）。

未改：W46 出口商、各版文件、core-it、各版 KIT、`cjk-inventory.json`。机制侧 KIT（`scratch-fanout-it/STATUS.md`）已追加记录。

## 验证结论（实跑，非推理）

harness（`scratch-fix-export-it1/harness.py`，日志同目录）：

- **Phase 1**：真实表处理流程跑 core-it，**10 语全过**——每语「翻譯」恰好替换 4 处，标签 4/4 正确，计数断言全绿，非 CJK 语零残留 CJK，ja/ko/zh-tw 零残留表键。
- **Phase 2**：真实 W46 出口商，control 对照重导出 .text.md——
  - **it-es：修后重导出与 fix1 手修的 text.md 字节全等**（56,267 B，SHA 与 fix1 记录一致）；相对修前 `.prefixed` 恰好只差 969/971/973/975 四行 `[A·Traducir]`。
  - **it-de / it-ru（抽查）：修后重导出与已提交 text.md 恰好只差 4 行**（969/971/973/975，`[A·Übersetzen]` / `[A·Переведите]`），其余 0 行；control（未修机制）与已提交 text.md 字节全等，基线干净。
  - 三份 fixed 重导出全文 grep「翻譯」= 0。

## 重 fan-out 前置条件：✅ 已满足

用修后机制重跑 `build_edition.py`，10 版 it 的 E 节标签都会本地化，it-es 的手修不会再被洗掉。

## 协调员注意：重 fan-out 前另有一件既存 drift 须处理（不在本次 scope）

验证发现：10 版已提交的 `content8.py` 都有 fan-out 后的 proof 补丁（L80–82 的 deficit/copertura/scaglione 释义等），core-it 仍是旧文案；各版另有自己的 proof 补丁（如 it-es L35 "Domenica 22 novembre"）。**重 fan-out 从 core-it 重建，会丢掉这些补丁。** 重 fan-out 之前须先把这些补丁重打（或先合回 core-it）。本修复对此既无帮助也无损害——Phase 2 用已提交版源文件做基线，正是为了隔离这层 drift。

## 改动文件清单

| 文件 | 改动 |
|---|---|
| `scratch-fanout-it/translations.py` | 头注释更正 + 新增「翻譯」映射（10 语） |
| `scratch-fanout-it/build_edition.py` | `consumed["翻译"]=4` + 残留 CJK 门收紧为零容忍 + 注释更新 |
| `scratch-fanout-it/STATUS.md` | 追加机制修复记录一节 |
| `scratch-fix-export-it1/FIX-LOG.md`、`MECHANISM-FIX-REPORT.md`、`harness.py`、`harness.log` 及重导出产物 | 本次工作产物（待协调员审 commit 时一并处理机制侧三个文件） |

详细改动对照表与验证全表见 `FIX-LOG.md`。
