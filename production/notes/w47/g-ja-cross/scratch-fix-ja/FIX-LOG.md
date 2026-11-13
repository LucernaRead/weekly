# W47 ja 家庭修复日志 — D1/D2 罗马字修复（2026-11-12）

- 工人：W47 ja 家庭修复工人；任务：独立重校（PROOF-NOTE.md）发现的 2 条问题，修复后重渲染 11 版并复核门禁。
- 范围：目标语 ja 11 版（core-ja = ja-zh-cn + 10 fan-out）。只动 `production/2026-w47/` 下 ja 家 11 版目录；不 commit、不 push、不跑 lint。
- 解释器：全程 `tools/venv/bin/python`。磁盘门限：df 已用 ≥100G 停手（开工 93G）。

## 缺陷

- **D1（11 版全有）**：`りくりゅう` 罗马字误作 `ryuuryuu`，应为 `rikuryuu`。每版 5 处：P7 金句 gloss 1 处 + P8 答案 66、77、80、105。源头：各版 `content7.py`（2 处）+ `content56.py`（3 处）。修复：`ryuuryuu` → `rikuryuu`（只改罗马字，日文原文与答案字母不动）。
- **D2（仅 ja-ko）**：美ノ海读音误作 `우미노우미`，应为 `츄라노우미`（ちゅらのうみ）。源头：ja-ko `content34.py:188`（Q48 练习句，P8 答案 48 的注释由此生成）。修复：只改该读音注释，答案字母（B）不动。

## 改前指纹（2026-11-12 实测，与 PROOF-NOTE 表完全一致）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-ja（zh-cn） | 25,973,499 / `e5b8a65dcf65` | 4,654,724 / `a1f1a21c267f` | 44,432 / `bcfa667da57e` |
| ja-de | 25,813,853 / `9c3d99f1cbb5` | 4,387,409 / `c9934cc55414` | 46,520 / `6323cd14109c` |
| ja-en | 25,806,203 / `a063fff2f05e` | 4,379,969 / `9c9e2fd0d832` | 45,706 / `8374230f772c` |
| ja-es | 25,813,996 / `429f2dd366ba` | 4,387,628 / `26fc381b5322` | 46,684 / `81993361c31f` |
| ja-fr | 25,812,294 / `a49a45bc7ec7` | 4,386,310 / `261f69ffc4ec` | 46,882 / `420616e6b601` |
| ja-it | 25,807,650 / `4e4788733790` | 4,381,274 / `0a97c94a09c2` | 46,678 / `71a2d7d21e57` |
| ja-ko | 28,140,833 / `30fdf1f67dca` | 4,551,758 / `82c1c7c69a41` | 47,722 / `b20d5bc686ff` |
| ja-nl | 25,805,475 / `dc2140959c3c` | 4,379,017 / `e17fb93ba898` | 45,627 / `f823709e214d` |
| ja-pt | 25,814,744 / `ea1bf3b8aa5f` | 4,388,483 / `15614590c526` | 46,696 / `53bc548ba01c` |
| ja-ru | 25,970,245 / `2ab6a7d2d740` | 4,540,692 / `f70444a63e48` | 53,004 / `88e3680b5d31` |
| ja-zh-tw | 25,988,408 / `d080e8981720` | 4,789,284 / `b8f3fdad5208` | 44,361 / `8c18a0e9fb47` |

注：`ryuuryuu`/`rikuryuu` 同为 8 字符、`우미노우미`/`츄라노우미` 同为 15 UTF-8 字节，故 text.md 字节数修后不变，只变 SHA；印 PDF 字节数亦预期不变或仅差数字节。

注：KIT/EDITION-RECORD 带日期的历史记录行（如“`ryuuryuu` as specified”）保留旧拼写作为修前记录，不改写历史；现行 §1 spec 行已随修复更新为 `rikuryuu`。下文“grep 为 0”指内容文件（content*.py + svg + text.md + PDF 文字层）。

## 接替工人记录（2026-11-12，接替 6165c632）

- 改前指纹已逐版核对：11 版 ×（印/网/text.md）33 项尺寸+SHA-12 与上表完全一致；磁盘 93G（<100G 门限）。上一任只改了 core-ja 的 `content7.py`/`content56.py`（`ryuuryuu` 0×/`rikuryuu` 5×），印/网/text.md 仍为改前值；其余 10 版源头未动。
- `update_kit.py` 两处修复（接替工人修，原因见各版小节）：
  1. `repl_size` 原按“文件名与 bytes 同行”匹配：core-ja §8 无 `###` 小节致 PRINT 2 命中；各 fan-out 的 web 尺寸在文件名下一行致 WEB 0 命中。改为首个“文件名后 60 字符内第一个 `[\d,]+(?= bytes)`”匹配（只改现态行，历史记录不动）。
  2. SVG 变化检查按 `os.listdir` 顺序取目录，可能取到 `freeze/`/`freeze-prod/` 的空 `svg/` 目录，`sha256sum` 零参数读 stdin 永久阻塞（ja-de 在此挂了 5 分钟以上，CPU 0，子进程 `sha256sum` 空转；已 kill，KIT 未被改动）。改为只取含 `p8-tesuto.svg` 的非空 `svg/` 目录，`svg_sha` 空列表时断言失败。
- core-ja 与 ja-de 的 KIT 由接替工人按脚本原定内容手动补写（脚本在该两版上失败/挂起时 KIT 文件均未被改动，核对过）；其余 9 版走修复后的脚本。core-ja §1 本无罗马字 spec 行，故无 §1 改动；ja-de §1 行 34 已改 `rikuryuu`。
- **text.md 导出器陷阱（ru 家 FIX-LOG §7，补充任务）**：本轮不走重导出——`fix_edition.sh` 全程不调用任何 text.md 导出器（grep 验证：`export_textmd`/`export-textmd` 0 命中），text.md 只做手术式字符串替换 + 逐行 pairwise 校验（行数不变、恰好 5 行/6 行不同、每行仅含修复替换）。已对 core-ja、ja-de 用修前快照（`pre-src/`）独立复核：diff 恰为 5 行 intended 行，行数 1356/1356、1376/1376，无标题行丢失。其余 9 版修后同样复核（见逐版结果）。ja-de KIT F5 注：D5 后部分双语框题已拆两行（JP 23pt/ gloss 19pt）或缩至 21pt——正是导出器 ≥24pt 收集规则会丢的那类标题，重导出会丢它们；手术式替换不受影响。

## 第二接替核实（2026-11-12，第二接替工人，接替 1fbaa1fb）

- 磁盘 94G（<100G 门限）。逐版指纹实测（印/网 PDF + text.md 尺寸+SHA-12，与上表改前指纹逐版对照；PDF 文字层 pdftotext 计数；证据：`takeover-fingerprint.txt`）。
- 结论：3 版已落地（core-ja、ja-de、ja-en），1 版半成（ja-es：源头已改、成品仍为改前），7 版未动（ja-fr、ja-it、ja-ko、ja-nl、ja-pt、ja-ru、ja-zh-tw）。只补仍开着的口子，不重做已落地的版。

| 版 | 状态 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） | py/text/svg/印/网：ryuuryuu→rikuryuu |
|---|---|---|---|---|---|
| core-ja | ✅ 已落地 | 25,973,509 / `0ce5e4b872ae` | 4,654,731 / `0f9098ff3bf0` | 44,432 / `55c570f1bd0e` | 全层 0×/5× |
| ja-de | ✅ 已落地 | 25,813,856 / `4283e8a74ff9` | 4,387,416 / `c24dfb09d7d0` | 46,520 / `0d8d1de78a06` | 全层 0×/5× |
| ja-en | ✅ 已落地 | 25,806,211 / `c6a15edb8a6c` | 4,379,966 / `0560f0e4ea85` | 45,706 / `fb5a4700d3c9` | 全层 0×/5× |
| ja-es | ⚠️ 半成：py 已改（0×/5×），text/svg/印/网仍改前 | 25,813,996 / `429f2dd366ba`（= 改前） | 4,387,628 / `26fc381b5322`（= 改前） | 46,684 / `81993361c31f`（= 改前） | text/svg/印/网 5×/0× |
| ja-fr | ⬜ 未动（= 改前） | 25,812,294 / `a49a45bc7ec7` | 4,386,310 / `261f69ffc4ec` | 46,882 / `420616e6b601` | 全层 5×/0× |
| ja-it | ⬜ 未动（= 改前） | 25,807,650 / `4e4788733790` | 4,381,274 / `0a97c94a09c2` | 46,678 / `71a2d7d21e57` | 全层 5×/0× |
| ja-ko | ⬜ 未动（= 改前），D2 亦未动 | 28,140,833 / `30fdf1f67dca` | 4,551,758 / `82c1c7c69a41` | 47,722 / `b20d5bc686ff` | 全层 5×/0×；우미노우미 全层 1×、츄라노우미 0× |
| ja-nl | ⬜ 未动（= 改前） | 25,805,475 / `dc2140959c3c` | 4,379,017 / `e17fb93ba898` | 45,627 / `f823709e214d` | 全层 5×/0× |
| ja-pt | ⬜ 未动（= 改前） | 25,814,744 / `ea1bf3b8aa5f` | 4,388,483 / `15614590c526` | 46,696 / `53bc548ba01c` | 全层 5×/0× |
| ja-ru | ⬜ 未动（= 改前） | 25,970,245 / `2ab6a7d2d740` | 4,540,692 / `f70444a63e48` | 53,004 / `88e3680b5d31` | 全层 5×/0× |
| ja-zh-tw | ⬜ 未动（= 改前） | 25,988,408 / `d080e8981720` | 4,789,284 / `b8f3fdad5208` | 44,361 / `8c18a0e9fb47` | 全层 5×/0× |

- KIT 核对（逐版 SHA 与盘上最终实测一致）：
  - core-ja KIT §8 行 297–299：印 25,973,509 / `0ce5e4b872ae…`、网 4,654,731 / `0f9098ff3bf0…`、text 44,432 / `55c570f1bd0e…`，与盘上一致 ✅。历史改前行（行 257、278–282，旧 SHA）保留，未动 ✅。
  - ja-de KIT 行 141/143 与 213–215：印 25,813,856 / `4283e8a74ff9…`、网 4,387,416 / `c24dfb09d7d0…`、text 46,520 / `0d8d1de78a06…`，与盘上一致 ✅；§1 行 34 已为 `rikuryuu` ✅；历史改前行（行 205–207）保留 ✅。注：ja-de 的 `kit-update.log` 为空、RC=143（update_kit.py 在旧版 svg 扫描挂起被 kill），KIT 系上一任手动补写——本次逐值核对与盘上一致，无需重写。
  - ja-en KIT 行 132/134 与 165–167：印 25,806,211 / `c6a15edb8a6c…`、网 4,379,966 / `0560f0e4ea85…`、text 45,706 / `fb5a4700d3c9…`，与盘上一致 ✅；§1 行 36 已为 `rikuryuu` ✅。小瑕：行 167 措辞写“re-exported”（实为手术式替换，`text-diff-check.log` 已验 pairwise 5 行仅含修复替换）与行 297 写“D1/D2”（ja-en 无 D2）——第二接替已随手正为手术式替换 / D1；`update_kit.py` 模板行 174 同步改措辞，余下 8 版不再出现此写法。
- 已落地 3 版门禁复核（各版 scratch 日志）：p8 compare 全部 CLEAN（core keydiff []，de/en [137,138,139,140] 预期翻译题键）、occlusion 0 flags、D5 census PASS、freeze baseline 8/8、spill 0、boxtitle 0 DEFECT、edge 0 TOUCH、creambox PASS 0 defects；text.md pairwise 5 行仅含修复替换；印/网文字层 multiset IDENTICAL，改后 vs 改前交付文字层差恰为 5× `ryuuryuu`→`rikuryuu` 字母替换（i/k 各 5）。
- core-ja scratch 下 `FAIL` 文件为 13:23 旧失败残留（首版脚本跑 text.md 重导出验证失败），其后重跑成功、DONE 写于 14:13 且日志尾为 COMPLETE——以指纹+门禁复核为准，该版已落地，FAIL 文件不代表现态。
- ja-es 半成原因：上一任在 patched build 起步（`patched-run.log` 为空）即被运行时重启中断；`pre-src/` 完好（content7.py 2× + content56.py 3× `ryuuryuu`，确为改前源头），base 已验 8/8 与改前交付 SVG 字节一致——重跑 `fix_edition.sh ja-es` 可直接续上（脚本遇已存 `pre-src` 即保留改前快照，py 的 sed 为幂等）。
- `update_kit.py` 已验含上一任两处修复（行 71 首个 60 字符内尺寸匹配、行 106 只取含 `p8-tesuto.svg` 的 svg 目录），直接用修好的版本。

## 逐版结果

<!-- 每版完成后 append：改前/改后印/网/text.md 尺寸+SHA 前 12、门禁复核结果、KIT 更新记录 -->

### core-ja / ja-de / ja-en（上一任接替工人 1fbaa1fb 完成；第二接替工人接手核实补记）

三版均由上一任完成重建、「逐版结果」当时未留记录；第二接替工人接手时逐版指纹+门禁复核确认已落地，数据如下（改前值 = FIX-LOG 改前表；改后值 = 接手核实实测；逐门细节以各版 scratch 日志为准，不补编）：

- core-ja：改前印 25,973,499 / `e5b8a65dcf65`、网 4,654,724 / `a1f1a21c267f`、text 44,432 / `bcfa667da57e`；改后印 25,973,509 / `0ce5e4b872ae`、网 4,654,731 / `0f9098ff3bf0`、text 44,432 / `55c570f1bd0e`。全层（py/text/svg/印/网）`ryuuryuu` 0× / `rikuryuu` 5×。门禁复核：p8 compare CLEAN（keydiff []，core 对自身）、occlusion 0 flags、D5 census PASS、freeze baseline 8/8、spill 0、boxtitle 0 DEFECT、edge 0 TOUCH、creambox PASS 0 defects；text.md pairwise 5 行仅含修复替换；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）。KIT §8 行 297–299 与盘上一致。注：scratch 下 `FAIL` 文件为 13:23 旧失败残留，其后重跑成功、DONE 写于 14:13 且日志尾为 COMPLETE——以指纹+门禁复核为准，该版已落地。
- ja-de：改前印 25,813,853 / `9c3d99f1cbb5`、网 4,387,409 / `c9934cc55414`、text 46,520 / `6323cd14109c`；改后印 25,813,856 / `4283e8a74ff9`、网 4,387,416 / `c24dfb09d7d0`、text 46,520 / `0d8d1de78a06`。全层 `ryuuryuu` 0× / `rikuryuu` 5×。门禁复核：p8 compare CLEAN（keydiff [137,138,139,140] 预期翻译题键）、occlusion 0、census PASS、freeze 8/8、spill 0、boxtitle 0 DEFECT、edge 0 TOUCH、creambox PASS；text.md pairwise 5 行仅含修复替换；印/网文字层 IDENTICAL，差恰 i/k 各 5。KIT §8 行 141/143 与 213–215、§1 行 34 `rikuryuu` 均与盘上一致，历史改前行保留。注：ja-de 的 `kit-update.log` 为空、RC=143（旧版 update_kit.py 在 svg 扫描挂起被 kill），KIT 系上一任手动补写，本次逐值核对一致，无需重写。
- ja-en：改前印 25,806,203 / `a063fff2f05e`、网 4,379,969 / `9c9e2fd0d832`、text 45,706 / `8374230f772c`；改后印 25,806,211 / `c6a15edb8a6c`、网 4,379,966 / `0560f0e4ea85`、text 45,706 / `fb5a4700d3c9`。全层 `ryuuryuu` 0× / `rikuryuu` 5×。门禁复核同 ja-de（p8 CLEAN keydiff [137–140]、occlusion 0、census PASS、freeze 8/8、spill 0、boxtitle 0、edge 0、creambox PASS；text.md 5 行；文字层 IDENTICAL 差恰 i/k 各 5）。KIT §8 行 132/134 与 165–167 与盘上一致；§1 行 36 `rikuryuu`。另顺手修正的措辞：ja-en KIT 行 167“re-exported”→手术式替换、行 297“D1/D2”→“D1”（ja-en 无 D2）；`update_kit.py` 模板行 174 同步改措辞。

### ja-es（第二接替工人，2026-11-12 15:44–15:58 UTC；续接 1fbaa1fb 中断的半成版）

- 改前（= FIX-LOG 改前表）：印 25,813,996 / `429f2dd366ba`、网 4,387,628 / `26fc381b5322`、text 46,684 / `81993361c31f`；py 已由上一任改过（`ryuuryuu` 0×/`rikuryuu` 5×），text/svg/印/网仍为改前 5×/0×；`pre-src/` 完好（改前源头 2+3），base 重建 8/8 与改前交付 SVG 字节一致。
- 改后：印 25,813,986 / `258c04418960`、网 4,387,623 / `0002d6fe1481`、text 46,684 / `3ddce794e256`。text.md 手术式替换 pairwise 校验通过（恰 5 行，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 预期翻译题键）；freeze baseline 8/8；freeze diff vs base 恰为 5 条 Latin 串变化（P7 1 + P8 4）、新增 CJK 0；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH；creambox PASS 0 defects；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×。
- KIT：`update_kit.py`（已修版，措辞已正为手术式替换）RC=0，§8 head 印/网 SHA 已更新为盘上值，§1 spec 行随修复更新为 `rikuryuu`，历史改前记录保留。

### ja-fr（第二接替工人，2026-11-12 15:58–16:12 UTC）

- 改前（= FIX-LOG 改前表）：印 25,812,294 / `a49a45bc7ec7`、网 4,386,310 / `261f69ffc4ec`、text 46,882 / `420616e6b601`；py 改前 `ryuuryuu` 2+3。
- 改后：印 25,812,296 / `9d4c6114fb31`、网 4,386,312 / `ef073db3df37`、text 46,882 / `badb0a6e7d00`。text.md 手术式替换 pairwise 校验通过（恰 5 行，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 预期翻译题键）；freeze baseline 8/8；freeze diff vs base 恰为 5 条 Latin 串变化（P7 1 + P8 4）、新增 CJK 0；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH；creambox PASS 0 defects；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×。
- KIT：`update_kit.py`（已修版）RC=0，§8 head 印/网 SHA 已更新为盘上值，§1 spec 行随修复更新为 `rikuryuu`，历史改前记录保留。

### ja-it（第二接替工人，2026-11-12 16:12–16:20 UTC）

- 改前（= FIX-LOG 改前表）：印 25,807,650 / `4e4788733790`、网 4,381,274 / `0a97c94a09c2`、text 46,678 / `71a2d7d21e57`；py 改前 `ryuuryuu` 2+3。
- 改后：印 25,807,661 / `1bfe06107634`、网 4,381,297 / `db031afe2252`、text 46,678 / `9b677d40100d`。text.md 手术式替换 pairwise 校验通过（恰 5 行，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 预期翻译题键）；freeze baseline 8/8；freeze diff vs base 恰为 5 条 Latin 串变化（P7 1 + P8 4）、新增 CJK 0；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH；creambox PASS 0 defects；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×。
- KIT：`update_kit.py`（已修版）RC=0，§8 head 印/网 SHA 已更新为盘上值，§1 spec 行随修复更新为 `rikuryuu`，历史改前记录保留。

### ja-ko（第二接替工人，2026-11-12 16:20–16:28 UTC；D1+D2）

- 改前（= FIX-LOG 改前表）：印 28,140,833 / `30fdf1f67dca`、网 4,551,758 / `82c1c7c69a41`、text 47,722 / `b20d5bc686ff`；py 改前 `ryuuryuu` 2+3、`content34.py` `우미노우미` 1。
- 改后：印 28,140,910 / `88b2bfc1d8b0`、网 4,551,878 / `753d8b4a63ba`、text 47,722 / `0fbf36dd4f76`。text.md 手术式替换 pairwise 校验通过（恰 6 行：D1 5 行 + D2 第 1246 行 `48. B — 우미노우미→츄라노우미`，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变（p4-supotsu.svg 不变：P4 练习句用汉字『美ノ海』，D2 只落在 P8 答案注）。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 预期翻译题键）；freeze baseline 8/8；freeze diff vs base：P7 1 条 Latin 串、P8 5 条串（Latin 4 + 新增 CJK 2：`라`、`츄`，即 D2 替换）、新增 CJK 合计 2；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH；creambox PASS 0 defects（diff 5、moved 28，D2 韩字宽度致 run 位移，无缺陷）；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 D1 5×（i/k 各 5）+ D2 2 字（`라`、`츄`）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×，印 PDF `츄라노우미` 1 行、`우미노우미` 0；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×、text.md `츄라노우미` 1×/`우미노우미` 0×。
- KIT 插曲：首跑 `update_kit.py` RC=1——脚本行 121 误预期 ja-ko 会变 p4-supotsu.svg，断言失败在写文件前，KIT 未被改动（逐值核对：仍全为改前值）。根因：D2 改的串只落在 P8 答案注，P4 题干为汉字不受影响（freeze diff 无 P4 变化为证）。已修脚本（删 ja-ko p4 预期并注原因；另把非 ko 版的 fix-round 标题/§11 行措辞由“D1/D2”正为“D1”，ja-es/ja-fr/ja-it/ja-en 四版 KIT 同步正措辞），从已同步的生产目录重建 scratch ED 后重跑 update_kit.py，RC=0；重跑后逐值核对：§8 head 印/网 SHA（行 131/133）、§8 fix 小节（行 158–160，text 行注明恰 6 行）、§1 行 35 `rikuryuu`、D2 行、§11 行 259 均与盘上一致，历史改前行（行 149–150）保留。

### ja-nl（第二接替工人，2026-11-12 16:28–16:38 UTC）

- 改前（= FIX-LOG 改前表）：印 25,805,475 / `dc2140959c3c`、网 4,379,017 / `e17fb93ba898`、text 45,627 / `f823709e214d`；py 改前 `ryuuryuu` 2+3。
- 改后：印 25,805,479 / `d6f14754f22c`、网 4,379,026 / `97ee26ba1616`、text 45,627 / `7f8f6638e635`。text.md 手术式替换 pairwise 校验通过（恰 5 行，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 预期翻译题键）；freeze baseline 8/8；freeze diff vs base 恰为 5 条 Latin 串变化（P7 1 + P8 4）、新增 CJK 0；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH；creambox PASS 0 defects；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×。
- KIT：`update_kit.py`（已修版）RC=0，§8 head 印/网 SHA 已更新为盘上值，§1 spec 行随修复更新为 `rikuryuu`，历史改前记录保留。

### ja-pt（第二接替工人，2026-11-12 16:38–16:47 UTC）

- 改前（= FIX-LOG 改前表）：印 25,814,744 / `ea1bf3b8aa5f`、网 4,388,483 / `15614590c526`、text 46,696 / `53bc548ba01c`；py 改前 `ryuuryuu` 2+3。
- 改后：印 25,814,751 / `3cca426dcbec`、网 4,388,490 / `a573debf0755`、text 46,696 / `9c9609378189`。text.md 手术式替换 pairwise 校验通过（恰 5 行，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 预期翻译题键）；freeze baseline 8/8；freeze diff vs base 恰为 5 条 Latin 串变化（P7 1 + P8 4）、新增 CJK 0；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH；creambox PASS 0 defects；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×。
- KIT：`update_kit.py`（已修版）RC=0，§8 head 印/网 SHA 已更新为盘上值，§1 spec 行随修复更新为 `rikuryuu`，历史改前记录保留。

### ja-ru（第二接替工人，2026-11-12 16:47–16:55 UTC）

- 改前（= FIX-LOG 改前表）：印 25,970,245 / `2ab6a7d2d740`、网 4,540,692 / `f70444a63e48`、text 53,004 / `88e3680b5d31`；py 改前 `ryuuryuu` 2+3。
- 改后：印 25,970,343 / `04b2f315e267`、网 4,540,808 / `0726eda64903`、text 53,004 / `f934bcf1d9f4`。text.md 手术式替换 pairwise 校验通过（恰 5 行，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变。svglib.py 字体路由未动（拉丁标题字体问题另有跨家工人处理）。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0；noto_sans_elements=712，ru 版预期西里尔文量）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [137,138,139,140] 预期翻译题键）；freeze baseline 8/8；freeze diff vs base 恰为 5 条 Latin 串变化（P7 1 + P8 4）、新增 CJK 0；spill 0 SPILL（83 OBSERVE）；boxtitle 0 DEFECT（1 marginal——对改前 pre-src 重跑同样为 1 marginal，属 pre-existing，非修复引入）；edge 0 TOUCH；creambox PASS 0 defects（diff 3、moved 22，西里尔文重排，无缺陷）；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×。
- KIT：`update_kit.py`（已修版）RC=0，§8 head 印/网 SHA 已更新为盘上值，§1 spec 行随修复更新为 `rikuryuu`，历史改前记录保留。

### ja-zh-tw（第二接替工人，2026-11-12 16:55–17:00 UTC）

- 改前（= FIX-LOG 改前表）：印 25,988,408 / `d080e8981720`、网 4,789,284 / `b8f3fdad5208`、text 44,361 / `8c18a0e9fb47`；py 改前 `ryuuryuu` 2+3。
- 改后：印 25,988,418 / `4b09db1088b8`、网 4,789,292 / `649ac196e81a`、text 44,361 / `77fb0f36c75b`。text.md 手术式替换 pairwise 校验通过（恰 5 行，每行仅修复替换）；SVG 仅 p7-kotoba.svg + p8-tesuto.svg 变化，其余 6 页不变。
- 门禁：run TOTAL 150，FLOW/HEAD 0；head_check PASS；D5 census PASS（D5_lat 0、D5_cyr 0、curly 0）；quotes 0 defective；occlusion 0 flags（自检 OK）；p8 compare CLEAN（150/150，keydiff [139,140]——zh-tw 预期：137/138 与 core 字节相同，见 KIT §3/§11 F3）；freeze baseline 8/8；freeze diff vs base 恰为 5 条 Latin 串变化（P7 1 + P8 4）、新增 CJK 0；spill 0 SPILL（86 OBSERVE）；boxtitle 0 DEFECT、0 marginal；edge 0 TOUCH；creambox PASS 0 defects（diff 3、moved 4）；印/网文字层 multiset IDENTICAL，改后 vs 改前差恰为 5× `ryuuryuu`→`rikuryuu`（i/k 各 5）；PDF 文字层印+网 `ryuuryuu` 0×/`rikuryuu` 5×；同步后生产目录复核 freeze 8/8、census PASS、quotes 0、svg/text.md `ryuuryuu` 0×/`rikuryuu` 5×。
- KIT 插曲：首跑 `update_kit.py` RC=1——zh-tw KIT 结构与其他版不同（无 `## §8 Gates`/`## §9`，§1 标题为 Conventions 而非 Specification），§1 断言在写文件前失败，KIT 未被改动（逐值核对仍全为改前值）。已修脚本：§1 匹配通用化（`## §1 `）；zh-tw 分支改 `§4 Deliverables`（印/网/text 三 SHA 全更，Fix2 历史括号保留）；fix 小节插 §4 末、§11 条目指 §4；另正 docstring 的 p7+p8 预期措辞。从已同步的生产目录重建 scratch ED（去 cards/__pycache__/*.pdf）后重跑 update_kit.py，RC=0；重跑后逐值核对：§4（印/网/text 尺寸+SHA）、§1 行 36 `rikuryuu`、§4 fix 小节、§11 行 266 均与盘上一致；D5 章节历史 SHA（行 273–274）保留；KIT 内残留 `ryuuryuu` 仅见于 fix 描述的箭头记法（与其他版一致）。重跑日志 `scratch-fix-ja/ja-zh-tw/kit-update-rerun.log`。注意：fix_edition.sh 不以 KIT RC 门控 DONE——首跑 KIT 失败仍写了 DONE、驱动仍报 ALL DONE exit 0；本次系人工发现并补修。

## 最终全量验证（2026-11-12，第二接替工人；脚本 `/tmp/fp_verify_ja.py`，venv PyMuPDF 读 PDF 文字层）

11 版逐版核对：印/网/text.md 尺寸+SHA-12 均与本日志所记改后值完全一致；content*.py、svg、text.md 中 `ryuuryuu` 0 / `rikuryuu` 各 5；印+网 PDF 文字层 `ryuuryuu` 0 / `rikuryuu` 各 5（合计 10）；ja-ko 另查 `우미노우미` 全层 0 / `츄라노우미` 全层 5（py 1 + svg 1 + text.md 1 + 印/网 PDF 各 1）；各版 KIT 均含改后印/网/text 三 SHA；11 个 DONE 标记齐全。磁盘 94G（< 100G 门限）。唯一 FAIL 文件为 core-ja scratch 下 13:23 旧失败残留（`FAIL: exporter does not reproduce pre-fix text.md`），其后重跑已成功，见 core-ja 小结。结论：**11/11 PASS**。

- core-ja：印 25,973,509 / `0ce5e4b872ae`、网 4,654,731 / `0f9098ff3bf0`、text 44,432 / `55c570f1bd0e`
- ja-de：印 25,813,856 / `4283e8a74ff9`、网 4,387,416 / `c24dfb09d7d0`、text 46,520 / `0d8d1de78a06`
- ja-en：印 25,806,211 / `c6a15edb8a6c`、网 4,379,966 / `0560f0e4ea85`、text 45,706 / `fb5a4700d3c9`
- ja-es：印 25,813,986 / `258c04418960`、网 4,387,623 / `0002d6fe1481`、text 46,684 / `3ddce794e256`
- ja-fr：印 25,812,296 / `9d4c6114fb31`、网 4,386,312 / `ef073db3df37`、text 46,882 / `badb0a6e7d00`
- ja-it：印 25,807,661 / `1bfe06107634`、网 4,381,297 / `db031afe2252`、text 46,678 / `9b677d40100d`
- ja-ko：印 28,140,910 / `88b2bfc1d8b0`、网 4,551,878 / `753d8b4a63ba`、text 47,722 / `0fbf36dd4f76`
- ja-nl：印 25,805,479 / `d6f14754f22c`、网 4,379,026 / `97ee26ba1616`、text 45,627 / `7f8f6638e635`
- ja-pt：印 25,814,751 / `3cca426dcbec`、网 4,388,490 / `a573debf0755`、text 46,696 / `9c9609378189`
- ja-ru：印 25,970,343 / `04b2f315e267`、网 4,540,808 / `0726eda64903`、text 53,004 / `f934bcf1d9f4`
- ja-zh-tw：印 25,988,418 / `4b09db1088b8`、网 4,789,292 / `649ac196e81a`、text 44,361 / `77fb0f36c75b`
