# FIX-LOG — 2026-W47 pt-minor1（pt 家重校 4 项轻微，工人 afb0a6c0 结论 NOT CLEAN）

修复员：fix-pt-minor1（2026-11-13 ~02:26–03:05 UTC）。工作目录：`~/workspace/weekly-git/production/2026-w47/`；
scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-minor1/`。
范围：仅 4 版（pt-zh-cn、pt-de、pt-it、pt-nl），各 1 处。**未 commit、未 push，未动其他版。**
构建解释器全程 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 全程指向 scratch 下 `tmp/`。

## §0 基线（修前磁盘值，`presnap.sha256`）

| 版 | 印 PDF | 网 PDF | text.md |
|---|---|---|---|
| pt-zh-cn (core-pt) | `edcb8d3d…` 14,137,984 B | `ca9f7722…` 1,389,823 B | `3cd3793f…` 36,882 B |
| pt-de | `a8c54d0c…` 12,426,508 B | `d76c126f…` 1,063,964 B | `519ab0de…` 37,907 B |
| pt-it | `56f388e7…` 12,418,794 B | `ab8305b7…` 1,056,196 B | `37c1980c…` 37,419 B |
| pt-nl | `390ac2d5…` 12,422,999 B | `a6e383aa…` 1,060,451 B | `a4a7bea1…` 37,560 B |

## §1 四处修法（旧值 → 新值）

| # | 版 | 文件 | 旧值 | 新值 |
|---|---|---|---|---|
| F1 | pt-zh-cn | 导出器 `make_textmd_pt.py:726`（源头）→ text.md:433 | `### Frases da semana (verbatim from this issue)` | `### Frases da semana （逐字摘自本期文章）` |
| F2 | pt-de | `content7.py:52` + `tables_de.py:60` | `quando, se, quem steht danach im Futur des Subjunktivs:` | `quando, se, quem stehen danach im Futur des Subjunktivs:` |
| F3 | pt-it | `content7.py:52` + `tables_it.py:59` | `quando, se, quem vuole il futuro del congiuntivo:` | `quando, se, quem vogliono il futuro del congiuntivo:` |
| F4 | pt-nl | `content7.py:90/96` + `tables_nl.py:117` | `consciência = bewustzijn, geweten: de memorie aan verzet en cultuur.` | `consciência = bewustzijn, geweten: de herinnering aan het verzet en de cultuur.` |

- F2/F3/F4 的 tables 改了两处副本：生产目录 `2026-w47-pt-XX/tables_XX.py`（入仓记录）
  + `scratch-fanout-pt/tables_XX.py`（`textmd.py` 的实际输入；只改生产副本则重导出会把旧串翻回来）。
  两副本原有 1 处无关分歧（de "本期目录" / it "口诀" 值不同），经核实均不在 text.md 出现，不影响导出。
- 旧串清零核查：4 版生产 text.md + content7.py 中旧串 0 命中（仅剩 3 处 `# ---- frases da semana
  (verbatim from this issue) ----` 源码注释，注释非渲染内容，未动）。

## §2 F1 源头（导出器英文残留）与连带修复

- 源头：`scratch-fix-core-pt2/make_textmd_pt.py:726` 硬编码
  `self.emit("### Frases da semana (verbatim from this issue)")`。其余 10 版的同行由 fanout
  `furniture.py` TEXTMD_EXTRA 映射为读者语，唯 zh-cn（core 直出）漏了映射。
- 修法：本轮 scratch 副本 `scratch-fix-pt-minor1/make_textmd_pt.py:726` 改为
  `### Frases da semana （逐字摘自本期文章）`（ASCII 空格 + 全角括号，与 zh-tw 版第 433 行逐字节相同；
  初版误用 U+3000 空格，已纠正）。未手改 text.md。
- 导出器验证（修前）：重导出与修前已入仓 text.md **逐字节相同**（36,882 B，SHA `3cd3793f…`，
  `MATCHES PRE-FIX`；150 题，范文 88 词）。修后重导出 diff 仅第 433 行一处（`text-pre-zh-cn.md` 留存）。
- 印/网 PDF 未重建（印 PDF 该处本就正确 `FRASES DA SEMANA　本周金句（逐字摘自本期文章）`；SHA 不变）。
- **连带（F1 改核心手稿引发的 fanout 映射失效）**：核心 text.md 第 433 行改中文后，
  `scratch-fanout-pt/furniture.py` TEXTMD_EXTRA 的 `"(verbatim from this issue)"` 键失效——
  若不修，今后任何 fanout 重导出都会在 de/it/nl 等版留下中文括号。
  已将 9 处键改为 `"（逐字摘自本期文章）"`（值不变：de/fr/es/it/nl/ru/ja/ko/zh_tw 各一处），
  并给 en 补一条 `（逐字摘自本期文章）` → `(verbatim from this issue)`（en 原无此条，因旧核心本就是英文）。
  验证：以新核心重导出 en 版 text.md，与已入仓版 **diff 0 行**（`dryrun-en/`）；de/it/nl 重导出 diff 各仅意改行，
  第 433 行不变。pt-ru 的 tables 旧串问题（fix-pt-ru2 §9 留待下次 fanout 同步）不在本轮范围，未动。

## §3 重建与确定性（F2/F3/F4，scratch 先建后同步）

- 每版：`run.py` TOTAL 150 RC=0，0 FLOW OVERFLOW → `render.py` → `tools/webpdf.py svg`。
  仅 `svg/p7-lingua.svg` + `cards/p7-lingua.png` 变，其余 7 张 SVG 逐字节相同。
- 确定性：it、nl 印 PDF 两次渲染逐字节相同；de 印 PDF 三次渲染逐字节相同（`007f16d6…`，12,426,495 B）。
- F2 桥句重排：de 桥句由 3 行重排为 4 行（freeze-diff p7 +68 vs 修前 +67 串即此；无溢出、无碰撞）。
  F4 gloss 仍 2 行（svglib wrap 实测），栏位无位移。
- text.md 重导出（fanout `textmd.py`，自新核心）：de 仅 L393、it 仅 L393、nl 仅 L406；
  150 题齐全；无 PT-only 行改动（header/330 除外为 0）。
- 印文本层（修前修后多重集差 = 恰为意改）：
  - de：only-in-pre `t`×1；only-in-post `e`×1、`n`×1（新串 1 次、旧串 0 次）。
  - it：only-in-pre `e`×1、`u`×1；only-in-post `o`×2、`g`×1、`n`×1、`i`×1（新串 1 次、旧串 0 次）。
  - nl：only-in-pre `m`×2、`o`×1；only-in-post `n`×3、`e`×2、`h`×2、`t`×1、`r`×1、`g`×1、`d`×1、`i`×1；
    净 +9 字符（新串 1 次、旧串 0 次；提取换行所致 grep 0 命中已用空白归一化复核确认）。
  - de 提取字节 −1（47,966→47,965）为 pdftotext 换行/空行排序噪声（桥句重排 + A2/B2 标签行位移），
    非内容差：多重集差恰为意改单字。

## §4 全部门禁（实跑结果）

| 门 | pt-zh-cn (core-pt) | pt-de | pt-it | pt-nl |
|---|---|---|---|---|
| gates.py / gates_core.py | 16/16 PASS，FAILURES: none | 16/16 PASS，FAILURES: none | 16/16 PASS，FAILURES: none | 16/16 PASS，FAILURES: none |
| p8 extract --total 150 | 150/150 | 150/150 | 150/150 | 150/150 |
| p8 compare | CLEAN keydiff=[] | CLEAN keydiff=[137, 138]（既定） | CLEAN keydiff=[137, 138]（既定） | CLEAN keydiff=[137, 138]（既定） |
| occlusion | 0 flags（selftest OK） | 0 flags（edition + core） | 0 flags（edition + core） | 0 flags（edition + core） |
| spill | 0 SPILL（99 OBSERVE） | 0 SPILL（70 OBSERVE） | 0 SPILL（73 OBSERVE） | 0 SPILL（71 OBSERVE） |
| boxtitle | 0 DEFECT（30/350） | 0 DEFECT（26/270） | 0 DEFECT（24/264） | 0 DEFECT（24/269） |
| edge | 0 TOUCH 0 NEAR | 0 TOUCH 0 NEAR | 0 TOUCH 0 NEAR | 0 TOUCH 0 NEAR |
| D5 census | PASS | PASS | PASS | PASS |
| freeze baseline | 8/8 | 8/8 | 8/8 | 8/8 |
| freeze diff vs core | 自比 +0/−0 | CJK 9 / Latin 482（修前 481，+1 为桥句重排） | CJK 9 / Latin 461（= 修前） | CJK 9 / Latin 475（= 修前） |
| 印/网文本层多重集 | IDENTICAL（44,343 B 各） | IDENTICAL（47,965 B 各） | IDENTICAL（46,713 B 各） | IDENTICAL（47,112 B 各） |

- 注 1：de 的门禁跑在 scratch 构建上；生产同步后对生产文件重跑印/网多重集 + edge + 新旧串核查，
  全部通过（生产印 PDF 已换为三次一致的 `007f16d6…`，见 §5）。
- 注 2：it/nl KIT §6 原记 "occlusion 1 flag P1 LINEX graze" 本轮**不复现**：当前工具（selftest 6 类全触发）
  在生产 SVG 与 core-pt/svg 上均为 0 flags（门禁跑 + 生产复核两次一致）。KIT §6 已更新为 0 flags 并注明 superseded。
- 注 3：probe_xru.py 扫描的是 *-ru 全家（与本轮无关），未作 pt-de/it/nl 结论；三版字体路由由 D5 census
  PASS（LAT@NotoSans=0）覆盖。
- 注 4：text.md 相关门禁（pt-zh-cn）：p8 150/150 + compare CLEAN + 印/网多重集 + diff 仅 L433；
  答案附录未动（diff 证明）。

## §5 异常：de render 一次性膨胀（已处理）

- 现象：de 重建中第二次 `render.py` 产出 27,234,655 B 印 PDF（36,973 xrefs，对象疑似重复；
  SHA `24ff77be1c6cf9a13a99d45fa9f2b7e2006a04de19c01a490f19a7338029f19f`），
  而同源前后三次渲染均为 12,426,495 B（SHA `007f16d6…`，逐字节相同）。
- 排查：27 MB 版与 12 MB 版图片载荷完全相同（5 图，字节一致）；多出约 15 MB 在非图片流对象。
  webpdf→render 顺序复测未复现（仍为 12,426,495 B / `007f16d6…`），判为一次性 flake（疑似 cairosvg/pypdf
  偶发对象重复），非源文件问题。
- 处理：生产文件已换为三次一致的 12,426,495 B 版；27 MB 版未留存（SHA 记于此），scratch 副本已删。
  膨胀版虽通过全部 PDF 门禁（门禁即跑在其上），但不可复现，不可作为交付物。

## §6 新 SHA（生产文件实测，`postsnap.sha256`）

| 版 | 印 PDF | 网 PDF | text.md |
|---|---|---|---|
| pt-zh-cn | `edcb8d3d…` 14,137,984 B（未变） | `ca9f7722…` 1,389,823 B（未变） | `352f5097…` 36,889 B（md5 `eb651354…`） |
| pt-de | `007f16d6…` 12,426,495 B | `11a2581b…` 1,063,957 B | `5bea955b…` 37,908 B（md5 `35facfc0…`） |
| pt-it | `ac844f0f…` 12,418,795 B | `89ec1f93…` 1,056,189 B | `d55da797…` 37,422 B（md5 `c3e68d9e…`） |
| pt-nl | `ac687874…` 12,423,005 B | `0d7be4af…` 1,060,458 B | `34a38b88…` 37,571 B（md5 `ab50d15b…`） |

完整 SHA-256 见 `postsnap.sha256`（修前见 `presnap.sha256`）；生产文件与 scratch 构建逐字节核对一致
（content7.py、svg/p7、cards/p7、双 PDF、text.md 六项 ×3 版全 OK）。

## §7 KIT

- 4 版 `WEEKLY-KIT.md` 已更新：§6 现值（印/网字节 + SHA + 文本层字节；it/nl occlusion 改 0 flags 并注明），
  文末各追加 `fix-pt-minor1` 节（修法 + 门禁 + 新旧 SHA + 改动文件）。
- fanout 侧改动（goals 侧，不入仓）：`scratch-fanout-pt/furniture.py`（TEXTMD_EXTRA 9 键改 + en 补 1 条）、
  `scratch-fanout-pt/tables_{de,it,nl}.py`（各 1 处 SEG 值）。
- pt-ru fix2 留待下次 fanout 同步的 `scratch-fanout-pt/tables_ru.py` 旧串未动（与本轮无关）。

## §8 改动文件清单（未 commit、未 push）

- 生产 `2026-w47/`：core-pt `2026-w47-pt-zh-cn.text.md`、`WEEKLY-KIT.md`；
  2026-w47-pt-de/it/nl 各 `content7.py`、`tables_XX.py`、`svg/p7-lingua.svg`、`cards/p7-lingua.png`、
  `A-Lucerna-VOL4.pdf`、`A-Lucerna-VOL4-web.pdf`、`2026-w47-pt-XX.text.md`、`WEEKLY-KIT.md`。
- goals 侧：`scratch-fanout-pt/furniture.py`、`scratch-fanout-pt/tables_{de,it,nl}.py`。
- 其余版未动；仓库内其余改动均为其他工人在途工作（见 §9 核查）。

## §9 最终核查

- `git status`：本轮改动只涉上述 4 版文件。core-pt 本轮 2 项 tracked 改动（text.md + KIT，
  mtime 02:27/03:04 UTC）；同目录另 3 项 tracked 改动（content12.py、gates_core.py、svglib.py，
  mtime 06:30/08:05 UTC，在本轮开工前）为其他工人在途工作，本轮未碰。pt-de/it/nl 3 个目录整体
  untracked（fanout 尚未入仓），本轮只改其中 §8 所列文件；其余家改动与本轮无关。
- 4 版 text.md diff 各恰 1 行（zh-cn L433、de L393、it L393、nl L406）。
- 4 版 KIT §6 新 SHA 与磁盘实测一致；4 版门禁逐项见 §4，全绿。
- 磁盘：96G 已用（df 54G 可用）；本轮 scratch 约 80 MB，已清 bloat-test 副本与 27 MB 膨胀版。
- 日志：本文件；`presnap.sha256` / `postsnap.sha256`；`make_textmd_pt.py`（F1 导出器副本）；
  `build-{de,it,nl}-{run,render,webpdf}.log`；`textmd-{de,it,nl}.log`；`gates-{de,it,nl,zh-cn}/`
  （gate-run.log + 各门 JSON）；`dryrun-en/`（F1 连带验证）；`pre/`（4 份修前 text.md）；`text-pre-zh-cn.md`
  （F1 修前导出复现件）；`bloat-test-{webpdf,render}.log`（§5 复测日志；测试目录已删）。
