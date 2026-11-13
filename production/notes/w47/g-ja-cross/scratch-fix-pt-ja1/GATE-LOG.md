# GATE-LOG — W47 pt-ja fix1 · 自验门禁逐项实测

- 版：`production/2026-w47/2026-w47-pt-ja/`；核心对照 `production/2026-w47/core-pt/`（fix2）
- 执行：2026-11-11 UTC 17:52–18:07；全部日志在本 scratch
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-ja1/`
- 驱动：本 scratch 内 `gates_pt.py`（由上一轮 `scratch-refanout-pt/gates_pt.py` 复制，
  仅把日志/输出目录 S 改指本 scratch；helper 脚本 `creambox.py`、`creambox_diag.py`、
  `boxtitle_core.py`、`keycheck_core.py`、`sweep_de.py`、`minfont.py`、`check_final.py` 同样复制，未改逻辑）
- 判定：**全部通过**，结论 a。

## 逐项门禁

| # | 门禁 | 命令 / 来源 | 实测值 | 结论 |
|---|---|---|---|---|
| 1 | run.py rc=0，TOTAL 150，无溢出警告 | `tools/venv/bin/python -u run.py` → `ja-run.log` | rc=0；`TOTAL 150`；分级 A2 48 / B1 71 / B2 31；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；`grep -ci "overflow\|too wide"` = 0 | PASS |
| 2 | 版内自检 16/16 | `python gates.py` → `ja-gates.log` | 16 行全 `[PASS]`，`FAILURES: none`；含 `P1 VOL.4 + week dates`、`same-baseline ink collisions = 0`、`page-frame ink crossings = 0` | PASS |
| 3 | 几何遮挡真实审计 0 flags | `tools/occlusion_audit.py <svg>` → `ja-occlusion.log` / `ja-occlusion.json` | `selftest OK`（6 类阳性全触发，干净对照静默）；`…/svg: 0 flags` | PASS |
| 4 | p8 extract 150/150 | `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150` → `ja-p8-extract.log` | `noted set = 150 of 150`（1–150 全） | PASS |
| 5 | p8 compare CLEAN | `tools/p8.py compare --core-p8 core-pt/svg/p8-avaliacao.svg --edition-p8 … --total 150` → `ja-p8-compare.log` | `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`（与上一轮一致的预期翻译键差） | PASS |
| 6 | freeze baseline 8/8（本版） | `tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out <scratch>/freeze-pt-ja` → `ja-freeze.log` | `baseline: 8/8 SVGs byte-identical`；p1 `fc51c47e…`（新）、p2–p8 与修前 hash 相同；`core integrity: shipped core SVGs unchanged` | PASS |
| 7 | freeze baseline 8/8（核心对照） | `tools/freeze.py baseline --build core-pt --core-svg core-pt/svg --out <scratch>/freeze-core-pt` → `ja-freeze-core.log` | rc=0；`baseline: 8/8 SVGs byte-identical`（核心 p1 `bd87a867…` 等）；核心 SVG 未被改动 | PASS |
| 8 | freeze diff 增量闭合 | `tools/freeze.py diff --core-svg core-pt/svg --edition-svg <edition>/svg` → `ja-freeze-diff.log` / `ja-freeze-diff.json` | p1：`+27/-25 strings` 不变，CJK `167 → 254`（修前 253，**+1 即新增「人」**）；p2–p8 各页数与上一轮全同；**TOTAL added CJK 3246，不变**。注：新增 CJK 仅以 U+3000 计的字面要求不适用于 ja 版（主体系日语讲解层，新增约 3,246）；闭合核对为：p1 +1 人，且新增 surplus 为 0——核心 p1「人」=2，版 p1「人」修前 1→修后 2，已在核心预算内，故 TOTAL 不变（独立复核：strip-tags 全文计数，核心 p1 人=2、版 p1 人=2） | PASS |
| 9 | 印/网文字层逐字节一致 | `pdftotext -layout` 印、网 → `ja-print.txt` / `ja-web.txt`（`ja-gates.json`） | `print_web_text_equal: true`，107,800 字节；`pdftotext_rc: [0, 0]` | PASS |
| 10 | 印/网文字层逐 token 一致 | `check_final.py` → `ja-check-final.log` / `ja-textdiff.json` | `pages print=8 web=8`；`words print=6896 web=6896 multiset-diff=0`；`diff sample: []` | PASS |
| 11 | 斜体面一致 | `gates_pt.py` 内 italic 统计（`ja-gates.json`） | `italic_print: 1`，`italic_web: 1`，`italic_equal: true` | PASS |
| 12 | P8 最小字号 ≥ 9.75pt（SOP §1.1 下限） | `minfont.py` → `ja-minfont.log`；`check_final.py` 复核 | `P8 min effective font size = 10.125 pt (n=810)`；`below 9.75pt: 0`；答案区 span 最小 10.125pt（与上一轮同值） | PASS |
| 13 | 150 键复核无回归 | `keycheck_core.py` → `ja-keycheck.log` / `keycheck-150.json` | `REG entries: 150; p8extract keys: 150`；`exact match: 149/150`；唯一 mismatch 为 Q150（开放作文题，抽取为 `✓`，与上一轮相同的预期标记） | PASS |
| 14 | 150 键与核心比对无回归 | 见 #5 | CLEAN，keydiff [137,138]，与上一轮一致 | PASS |
| 15 | creambox / boxtitle / sweep | `creambox.py`、`creambox_diag.py`、`boxtitle_core.py`、`sweep_de.py` → 各 `.log` | creambox_rc 0、diag rc 0、boxtitle rc 0、sweep rc 0；**三份日志与上一轮逐字节相同**（`diff` 无输出）；diag 无负 ink-clearance；boxtitle 各标题净空 +33.4 / +141.8 / +143.5；sweep：`bridges found: 20`，`bridge orphans: 0`，`bridge widows: 0`；注：creambox 日志中 5 处 baseline-clearance 为负是上一轮已有的已知记录（diag 真实墨迹复核全部为正，KIT 记为 0 spill，本次逐字节复现） | PASS |
| 16 | 印版文字与上一轮的 diff 限定在 P1 | `diff scratch-refanout-pt/ja-print.txt scratch-fix-pt-ja1/ja-print.txt` | 仅第 1 页不同（72/103 行，均为 `pdftotext -layout` 空白重排）；第 2–8 页**逐字节相同**；第 1 页空白折叠后 token multiset 差恰为 `{'ブラジル人が読むポルトガル語': 1, 'ブラジルが読むポルトガル語': 1}`，即唯一内容变化是标语 | PASS |
| 17 | 标语行无碰撞（实测） | `measure_topstrip.py` → `ja-topstrip-before.log` / `ja-topstrip-after.log`；目视 `ja-p1-topstrip.png` | 见 FIX-LOG §5：advance 右缘 1208.7→1216.4，真实墨迹右缘 1276→1285，日期行墨迹左缘 1461 不变，**墨迹间隙 176px**；`gates.py` 同基线墨迹碰撞 0 | PASS |

## 三 SHA（终态，与 FIX-LOG §3 同值）

- 印 `A-Lucerna-VOL4.pdf`：`568eb36b19a0d285dfbb9058933659e3dd97afae0d5de535a5b47bb7906b6ea5`（24,991,052 B）
- 网 `A-Lucerna-VOL4-web.pdf`：`7079b9af534836635228e9d5982210dacbecc2257438c9d1d98afbf7761c5444`（1,680,802 B）
- 文 `2026-w47-pt-ja.text.md`：`90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830`（37,915 B，不变）

## 证据文件（本 scratch）

`ja-run.log`、`ja-render.log`、`ja-gates.log`、`ja-textmd.log`、`ja-textmd-diff.json`、
`ja-webpdf.log`、`ja-gates-driver.log`、`ja-gates.json`、`ja-occlusion.log`、`ja-occlusion.json`、`ja-p8-extract.log`、
`ja-p8-extract.json`、`ja-p8-compare.log`、`ja-p8-compare.json`、`ja-freeze.log`、`ja-freeze-core.log`、
`ja-freeze-diff.log`、`ja-freeze-diff.json`、`ja-creambox.log`、`ja-creambox-diag.log`、`ja-boxtitle.log`、
`ja-keycheck.log`、`keycheck-150.json`、`ja-sweep.log`、`ja-minfont.log`、`ja-check-final.log`、
`ja-textdiff.json`、`ja-p8size.json`、`ja-print.txt`、`ja-web.txt`、`ja-topstrip-before.log`、
`ja-topstrip-after.log`、`ja-p1-topstrip.png`、`svg-before.sha256`、`svg-after.sha256`、
`measure_topstrip.py`、门禁脚本副本（`gates_pt.py` 等 7 个 helper）、`freeze-pt-ja/`、`freeze-core-pt/`。
