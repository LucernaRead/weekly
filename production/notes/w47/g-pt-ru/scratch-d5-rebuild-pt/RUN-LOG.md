# W47 D5 重建工作日志 — pt 家庭（接替工人，2026-11-12）

接替棒：上一任 4913a46b 在 2026-11-12 04:28 EST 被第二次运行时重启打断；更早一任 9a4925f8 在 01:59 EST 被 cron 超时打断。
本日志在 `scratch-d5-rebuild-pt/` 下；上一任的脚本在 `work/`（common.sh / snapshot.sh / gates.sh / route_assert.py / textlayer.py），沿用。
工作方式：生产目录原地重建；每版报完成前核对生产印/网 PDF SHA 与报告 SHA 一致；KIT 以生产实际 SHA 为准。

## 接手核实（2026-11-12 ~04:35 EST，生产实测）

| 版 | 生产 svglib | 生产印 SHA（前 12） | 生产网 SHA（前 12） | 状态 |
|---|---|---|---|---|
| core-pt | `44a000db…`，`_D5_READER="cjk"` | `edcb8d3d6920` ✓与报告一致 | `ca9f7722ecb2` ✓ | 完成：gates-2 全绿（freeze baseline 8/8，p8 150/150，creambox PASS，census PASS，head_check PASS，textlayer 字节相同），KIT 已同步 |
| pt-de | `8f4599b1…`，latin | `a8c54d0c9b42` ✓ | `d76c126f2788` ✓ | 完成：gates-2 全绿，KIT 已同步 |
| pt-en | `8f4599b1…`，latin | `91fa99c4ed0b` ✓ | `b100c5765c5f` ✓ | 完成：gates-2 全绿，KIT 已同步 |
| pt-es | `8f4599b1…`，latin | `9e80ddac1389` ✓与 KIT 一致 | `4f918ab38188` ✓ | 完成：gates-2 全绿（gates-1 3 缺陷已修），KIT 已同步；仅缺 D5-REPORT 文件——本任补写 `D5-REPORT-pt-es.md` |
| pt-fr | `449b31ee…`，latin | `90f78551a5eb` ✓生产实测 | `83f63d47ace7` ✓生产实测 | **本任完成**：安装（fix2 已有）+ 重建；gates-1 5 缺陷（HEAD TOO WIDE ×1 + 同根 TEXTX ×1 + P1 框标题越框 ×3）逐项修后 gates-2 全绿（freeze 8/8，creambox PASS，P8 245→245 行余量 47.4px），KIT 已同步，报告 `D5-REPORT-pt-fr.md` |
| pt-it | `449b31ee…`，latin | `56f388e7ce3a` ✓生产实测 | `ab8305b734dc` ✓生产实测 | **本任完成**：安装（fix2 已有）+ 重建；gates-1 6 缺陷（HEAD TOO WIDE ×1 + 同根 TEXTX ×1 + 框标题越框 ×3 + 同根 page-frame crossings ×1）逐项修后 gates-2 全绿（freeze 8/8，creambox PASS，P8 227→227 行余量 47.3px），KIT 已同步，报告 `D5-REPORT-pt-it.md` |
| pt-nl | `8f4599b1…`，latin | `7fbf77a5d9da` ✓生产实测 | `0fc3730b1fb5` ✓生产实测 | **本任完成**：安装（fix2 一并补入）+ 重建；gates-1 5 缺陷（HEAD TOO WIDE ×1 + 同根 TEXTX ×1 + 框标题越框 ×3）逐项修后 gates-2 全绿（freeze 8/8，creambox PASS，P8 255→255 行余量 43.3px），KIT 已同步（注：KIT §6 旧 SHA 与快照盘上值不符，已在 D5 节注释，快照为准），报告 `D5-REPORT-pt-nl.md` |
| pt-ru | `9142f7c2…`，ru | `6208be63e917` ✓生产实测 | `c3b7eae275d7` ✓生产实测 | **本任完成**：安装（fix2 一并补入）+ 重建；gates-1 1 缺陷（P7 第 4 行金句俄译文一半被预告框盖住，52%）逐项修后 gates-2 全绿（freeze 8/8，creambox PASS，P8 253→253 行余量 46.3px；Noto Sans 元素 783，ru 路由真实触发；印/网文字层逐字节相同 54,970 B，`-layout` 差仅 3 空格），KIT 已同步，报告 `D5-REPORT-pt-ru.md` |
| pt-ja | `f61efb1bdac0`，无 _D5_READER | `568eb36b19a0`（旧版） | `b18b3df2a2da`（旧版） | 未做：无基线，待拍快照 + 重建（mode=cjk） |
| pt-ko | `4228b7e7fc52`，无 _D5_READER | `cdff9fe46e35`（旧版） | `f38917a69716`（旧版） | 未做：无基线，待拍快照 + 重建（mode=cjk；freeze 一步若 venv ABORT 可用系统 python3 一次，须先确认系统 python3 有 Pillow 10） |
| pt-zh-tw | `4228b7e7fc52`，无 _D5_READER | `42d7d4de02fadf`（旧版） | `8432b628db85`（旧版） | 未做：无基线，待拍快照 + 重建（mode=cjk） |

## 本任完成记录

- pt-fr：见 `D5-REPORT-pt-fr.md`（gates-1 5 缺陷 → gates-2 全绿）。
- pt-it：见 `D5-REPORT-pt-it.md`（gates-1 6 缺陷 → gates-2 全绿）。
- pt-nl：见 `D5-REPORT-pt-nl.md`（gates-1 5 缺陷 → gates-2 全绿）。
- pt-ru：见 `D5-REPORT-pt-ru.md`（gates-1 1 缺陷 → gates-2 全绿）。
- pt-es：补写 `D5-REPORT-pt-es.md`（上一任已完成，仅缺报告文件；生产 SHA 与 KIT 一致，已核实）。

磁盘：接手时 92G 已用（/home/hatch 150G）；已清 pt-es 遗留 freeze-2/build-copy（26M）。

## 接手核实（第三任，2026-11-12 ~06:35 EST，生产实测）

上一任 51df9048 在约 06:30 EST 被第四次运行时重启打断；RUN-LOG 上表为 04:35 EST 状态，已过期。

| 版 | 生产 svglib | 生产印 SHA（前 12） | 生产网 SHA（前 12） | KIT | 状态 |
|---|---|---|---|---|---|
| core-pt | `44a000db…`，cjk | `edcb8d3d6920` ✓与报告一致 | `ca9f7722ecb2` ✓ | 印+网 SHA 均在 KIT | 完成，CENSUS PASS |
| pt-de | `8f4599b1…`，latin | `a8c54d0c9b42` ✓ | `d76c126f2788` ✓ | ✓ | 完成，CENSUS PASS |
| pt-en | `8f4599b1…`，latin | `91fa99c4ed0b` ✓ | `b100c5765c5f` ✓ | ✓ | 完成，CENSUS PASS |
| pt-es | `8f4599b1…`，latin | `9e80ddac1389` ✓ | `4f918ab38188` ✓ | ✓ | 完成，CENSUS PASS |
| pt-fr | `449b31ee…`，latin | `90f78551a5eb` ✓ | `83f63d47ace7` ✓ | ✓ | 完成，CENSUS PASS |
| pt-it | `449b31ee…`，latin | `56f388e7ce3a` ✓ | `ab8305b734dc` ✓ | ✓ | 完成，CENSUS PASS |
| pt-ja | `fb698ac3…`，cjk | `9208d231d66c` ✓与报告一致 | `a9b4a30929c1` ✓ | ✓ | **上一任完成**（RUN-LOG 未及更新）：gates-2 全绿，报告 `D5-REPORT-pt-ja.md` 已在 |
| pt-nl | `8f4599b1…`，latin | `7fbf77a5d9da` ✓ | `0fc3730b1fb5` ✓ | ✓ | 完成，CENSUS PASS |
| pt-ru | `9142f7c2…`，ru | `6208be63e917` ✓ | `c3b7eae275d7` ✓ | ✓ | 完成，CENSUS PASS |
| pt-ko | `222c918a…`，cjk | `32f55755bded`（新，D5 后印） | `f38917a69716`（旧，D5 前） | 未同步 | **半完成**：D5 已装、run TOTAL 150、印已重建；run.log 遗留 HEAD TOO WIDE ×1（P2-ex C 头）；webpdf 被打断未跑，网仍是旧版；门禁未跑 |
| pt-zh-tw | `4228b7e7…`，无 _D5_READER | `42d7d4de02fa`（旧） | `8432b628db85`（旧） | 未同步 | 未做：仅有基线快照 + 普查（D5 拉丁 346），无安装 |

磁盘：接手时 93G 已用（/home/hatch 150G）。系统 python3 Pillow 10.2.0（ko freeze 例外备用，已确认）。

## 本任完成记录（第三任，2026-11-12 ~06:35–07:30 EST）

- pt-ko：接手时半完成（D5 已装、印已重建、网未建、门禁未跑，遗留 HEAD TOO WIDE ×1）。本任：content12.py 电池头 A–D 25→22 → run/render/webpdf 重建 → gates-1 仅自查 P7 quotes FAIL ×1（D5 run 拆分假象，`3일` 数字拆分；`gates.py` 增 `squashed()` 仅用于该项）→ gates-2 全绿（freeze baseline 8/8，venv；ko 族 Pillow-10 门不适用于 ko 读者版，未用系统 python3 例外）→ KIT 已同步 → 报告 `D5-REPORT-pt-ko.md`。新 SHA：印 `f3104fecd528…`（14,231,397 B）、网 `797ad196553e…`（1,307,288 B）。freeze-2 build-copy 已清（29M）。
- pt-zh-tw：接手时未做（仅基线快照，已核实与生产逐字节一致，复用）。本任：安装（mode=cjk，TC 基底，fix2 一并补入）→ round-1 HEAD TOO WIDE ×1 → 电池头 A–D 25→22 → 重建 → gates-1 仅自查 FAIL ×2（页脚 `第1版／共8版` + P7 quotes `2 比 2`，均为 D5 run 拆分假象；`gates.py` 增 `squashed()` 仅用于该两项）→ gates-2 全绿（freeze baseline 8/8）→ KIT 已同步 → 报告 `D5-REPORT-pt-zh-tw.md`。新 SHA：印 `2bbf46445f9e…`（13,804,538 B）、网 `2d0e80af74d7…`（1,463,493 B）。freeze-2 build-copy 已清（29M）。
- pt 家庭 11/11 完成：core-pt + 10 fan-out 全部生产落地、门禁全绿、KIT 已同步。未 commit、未 push、未跑 lint --write；独立重校由协调员另派。
- 磁盘：收尾时 93G 已用（/home/hatch 150G）。
