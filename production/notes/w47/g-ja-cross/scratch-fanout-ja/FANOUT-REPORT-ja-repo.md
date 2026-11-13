# FANOUT-REPORT — Lucerna Weekly 2026-W47 日本語 (ja) 家庭

> **来源说明（第 8 棒，2026-11-11 05:29–06:20 UTC）**：本文件在第 8 棒开工时盘上**不存在**。
> `hidden_files/w47/` 里只有 `scratch-proof-ja-en1/`、`scratch-proof-ja-de1/`；
> `hidden_files/w47/scratch-fanout-ja/`、各版 `map-*.json`、`apply.py`、`gen-map-*.py`
> 及历棒门禁 JSON/日志均不在盘上（疑似 VM 重启丢失）。本文件由第 8 棒新建，
> 只记录第 8 棒实测结果；前棒（第 1–7 棒）的审计节与 03:45 UTC 订正无法从盘上恢复，
> 以各版 `WEEKLY-KIT.md` 的记录为准。协调员如另有保存位置，请补入。
>
> 关键裁定（任务备忘，全数遵守）：练习小节头一律冻结为日语；E 组 4 个中文句答案键
> 必须译成读者语（预期 p8 compare keydiff 恰为 [137,138,139,140]，zh-tw 例外见下）；
> map = 221 键；P8 题干 10.35pt 不动；刊头 147pt、头条 42pt、边距 66pt；
> りくりゅう romaji `ryuuryuu`；ちいかわ按读者语译名（绝不用中文 `吉伊卡哇` 塞进他语版，
> zh-tw 读者语本身即用 `吉伊卡哇`）；趋势盒来源行须短到塞进 400px 盒；
> `match_set` instr 译文须短；F-MAIL 只印编辑部示例 + 双语延期披露；
> 各版 U+2019 弯撇号全扫须为 0。

## 第 8 棒（2026-11-11，审计 + 收尾 ko、zh-tw）

开工探针双通：`git hash-object -w --stdin` 成功；`hidden_files/w47/scratch-fanout-ja/.probe-stick8` 真实写盘成功。
工作范围：只动 `production/2026-w47/fanout-ja/` 与 `hidden_files/w47/scratch-fanout-ja/`；
未改 core-ja、未碰 W43–W46/其他家庭/tools/；未跑 insert.py、lint --write，未 git add/commit/push/reset/stash。

**任务交代与盘上实际的出入**：交代称 zh-tw“状态未知”、ko“是否全套自查未知”——
盘上实际 10 版交付物全齐，ko 与 zh-tw 的 KIT 均已记全套门禁通过。
第 8 棒对 ko、zh-tw 逐项重跑全部门禁（run.py 两遍 freeze、occlusion、p8 extract/compare、
文字层、P8 字号、U+2019、§1.1、8 版目视），全部复现，零问题，无需补做；
对其余 8 版重跑 occlusion、p8 extract/compare、文字层、P8 字号、U+2019、§1.1，
并核对双 PDF 字节+SHA 与 KIT 记录一致。**ja 家庭 10/10 完成，待办 0。**

### 逐版一行

| 版 | 状态 | 印版 字节 / SHA-256（前 8 位） | 网版 字节 / SHA-256（前 8 位） | 门禁（第 8 棒重跑） | 备注 |
|---|---|---|---|---|---|
| en | 完成，已核实 | 27,440,477 / `c29f6f98…` | 4,428,571 / `9d10efc5…` | occl 0；p8 150/150；compare CLEAN keydiff [137–140]；文字层一致 46,044 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致 |
| de | 完成，已核实 | 29,102,629 / `b5d66e17…` | 4,483,732 / `c55dd68c…` | occl 0；p8 150/150；CLEAN [137–140]；文字层一致 46,834 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致 |
| fr | 完成，已核实 | 28,347,993 / `5903a36b…` | 4,458,579 / `99fd99af…` | occl 0；p8 150/150；CLEAN [137–140]；文字层一致 47,208 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致 |
| es | 完成，已核实 | 29,102,097 / `0feb6113…` | 4,482,717 / `b274eac2…` | occl 0；p8 150/150；CLEAN [137–140]；文字层一致 47,034 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致 |
| it | 完成，已核实 | 29,099,162 / `75986cd7…` | 4,476,984 / `b3ea6d183…` | occl 0；p8 150/150；CLEAN [137–140]；文字层一致 47,000 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致 |
| pt | 完成，已核实 | 29,103,006 / `5e7542bc…` | 4,485,027 / `49914939…` | occl 0；p8 150/150；CLEAN [137–140]；文字层一致 46,976 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致 |
| nl | 完成，已核实 | 29,099,171 / `c18c551a…` | 4,476,557 / `e0678a4b…` | occl 0；p8 150/150；CLEAN [137–140]；文字层一致 45,989 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致 |
| ru | 完成，已核实 | 25,858,425 / `abc44c9c…` | 4,396,999 / `e2fc5382…` | occl 0；p8 150/150；CLEAN [137–140]；文字层一致 53,247 B；P8 min 9.975pt；U+2019 0 | SHA 与 KIT 一致；ちいかわ=`Чикава` |
| ko | 完成，第 8 棒审计通过 | 28,189,461 / `fbcfe840…` | 4,550,459 / `d52edd4e…` | run 0 溢出 TOTAL 150；freeze 8/8；occl 0；p8 150/150；CLEAN [137–140]；文字层一致 47,997 B；P8 min 9.975pt；U+2019 0；8 版目视干净 | 见下方审计结论 |
| zh-tw | 完成，第 8 棒审计通过 | 26,034,686 / `7b23a2c4…` | 4,788,784 / `cafe8303…` | run 0 溢出 TOTAL 150；freeze 8/8；occl 0；p8 150/150；CLEAN **[139, 140]**；文字层一致 44,661 B；P8 min 9.975pt；U+2019 0；8 版目视干净 | keydiff [139,140] 为预期，见下方 |

每版一份 `EDITION-RECORD.md`（在各自版目录内，含完整 SHA 与门禁明细）。
第 8 棒证据：`hidden_files/w47/scratch-fanout-ja/` 下 `*-stick8.*`
（run 日志、SVG 指纹、occlusion/p8 JSON、print/web pdftotext）。

### ko 审计结论（单列）

- run.py（`tools/venv/bin/python`，与构建同一解释器）exit 0、TOTAL 150、0 溢出；
  连跑两遍 freeze **8/8**，且重跑后 SVG 指纹与交付前指纹逐字节一致——交付 PDF 有效，无需重渲。
- occlusion 0 旗（selftest 6 类全触发）；p8 150/150；compare **CLEAN**，keydiff 恰为 **[137, 138, 139, 140]**。
- 文字层 print/web 逐字节一致（47,997 B）；P8 最小字号 9.975pt，次档 10.35pt。
- U+2019 全扫 0；简体残留 `吉伊卡哇`/`参考答案`/`酉之市`/`提名` 均为 0×；`치이카와`、`ryuuryuu` 如裁定。
- 8 版目视干净：P7 韩语披露 4 行、teaser 未压页脚；P8 E 组 137–140 韩语答案无误。
  仅存的版面现象均非 fan-out 缺陷：P1 趋势盒第 1 条末尾单字「敗」换行、P4 栏顶
  「5) でお知らせします。」跨栏续接、P2/P4 栏中空白——皆为核心冻结正文或 W46 已披露模式。
- **结论：ko 完成，零问题，无补做。**

### zh-tw 审计结论（单列）

- 与 ko 同套门禁全部重跑通过：run 0 溢出 TOTAL 150；freeze **8/8**（SVG 指纹与交付前一致）；
  occlusion 0 旗；p8 150/150；compare **CLEAN**，keydiff **[139, 140]**——恰为预期：
  137/138 无简体特有字，与核心逐字节一致，故不进入 keydiff（KIT §11 F3 已裁定，不得当缺陷“修”）。
- 文字层逐字节一致（44,661 B）；P8 最小字号 9.975pt；U+2019 全扫 0；
  残留：`参考答案` 0×、`參考答案` 1×、`吉伊卡哇` 4×（读者语正确译名）；`售`/`呢` 为简繁同形字误报。
- 8 版目视干净：P7 繁体披露 3 行；P7 B1 桥接「りくりゅう 雙人滑 ちいかわ 吉伊卡哇」；
  P8 E 组 137–140 繁体答案无误。
- **结论：zh-tw 完成，零问题，无续做。**

### 遗留说明（非待办，是证据缺口，如实记录）

1. **map 文件丢失**：`map-*.json`、`apply.py`、`gen-map-*.py` 不在盘上，221 键对齐无法直接重验。
   间接证据：ko/zh-tw 重跑 run.py 复现交付 SVG 逐字节一致 + p8 compare CLEAN + 目视干净 + 残留扫查 0。
   map 的生成方法以各版 KIT §11 记录为准。
2. **P7 teaser ends / P8 keys flow ends 的 KIT 数值**未用原测量脚本重测（脚本随旧 scratch 目录丢失）；
   以几何审计 0 旗 + 8 版目视为证。
3. **前棒报告缺失**：第 1–7 棒的 FANOUT-REPORT 章节与 03:45 UTC 订正未找到；本文件只含第 8 棒。
   协调员如另有保存位置，请补入——第 8 棒未据记忆补写前棒内容。
4. fanout-ja/ 与 hidden_files/w47/ 目前整体未入 git（`??` 状态）；是否移动/入仓由协调员定，第 8 棒未动。

### 待办

无。10/10 完成。
