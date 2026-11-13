# W47 步骤 4a — PREP-LOG（生产源 commit + 封面 commit，commit only，绝不 push）
# 执行员：恢复协调员 #6 派单 · 2026-11-13
# 仓库：~/workspace/weekly-git · 起始 HEAD：b06cb15e80dc46269f52cbf963aa93f3a5f88fa0
# 磁盘（执行前）：/home/hatch 150G，用 98G（66%），<100G，可继续。

## 0. 起始状态
- `df -h`：/dev/mapper/rv 150G，Used 98G，Avail 52G，Use% 66%。
- 起始 `git status --porcelain`：286 行（56 M + 9 D + 221 ??），全部位于 covers/2026-w47/、production/covers/2026-w47/、production/2026-w47/ 之内。
- 目标：13 笔 commit（1 封面 + 12 家生产源）。

## 0a. 派单路径偏差（已核实，按意图执行）
- 派单写 `git add production/covers/2026-w47/`（含 cover.json + 12 html + 9 webp + COVER-REPORT.md），但实测：
  - 12 个 .html 块 + 9 张重制 .webp 在仓库根目录 `covers/2026-w47/`（12 M html + 9 M webp）；
  - `production/covers/2026-w47/` 下只有 cover.json（M）+ COVER-REPORT.md（??）。
- 故封面 commit 实际 staged 两处：`covers/2026-w47/` + `production/covers/2026-w47/`，共 23 文件，与派单枚举的文件清单完全一致，无其他文件。

## 0b. 派单排除式失效（已核实，改用显式文件清单）
- 派单排除式 `git add <pathspecs> -- ':!*.pdf' ':!*/cards/*' ':!*/svg/*'` 实测失效：
  git 2.43.0 下一旦出现任一 `:(exclude)` pathspec，`git add` 只 stage 已跟踪的修改文件，
  全部 untracked 源码（core 各版 content*.py / ABSTRACT.txt / assets/*.jpg 等）都不进 index。
  实测 de 家：排除式 dry-run 仅 9 文件；无排除式 422 文件。
- 改用等价的显式方法：`find <该家 11/10 个目录> -type f` 排除 `*.pdf`、`/cards/`、`/svg/`、
  `__pycache__`/`*.pyc`、`*.pre-d5`，逐文件校验后以 `--pathspec-from-file` 显式 add。
  效果与派单意图相同（只进源码 .py/.md/.txt/.json/.log/.sh + assets/ 源图），且不漏 untracked 文件。
- 例外处理：
  - `*.pre-d5`（ko 家 11 个 svglib 备份，core-ko + 10 个 ko fan-out 版）：非源码扩展名，不 commit，
    留在最终剩余清单中汇报（不擅自 commit 其他东西）。
  - `core-it/scratch/*.py`（export_core_textmd.py、validate_textmd.py）：.py 源码，按派单允许列表计入 it 家。
  - `hidden_files/w47/` 空目录（core-zh-tw 及 9 个 zh-tw fan-out 版下）：目录内 0 文件，git 不跟踪，无影响。
  - .pdf（262 个，含 >5MB 的 11 个核心版 PDF）、cards/（*.png）、svg/ 页渲染文件按派单排除，
    仍为 untracked 留在最终剩余清单中。

## 1. 封面 commit
- SHA：`5c6b6db240bf849ec26b85bf82dc57d07e5b4335`
- message：`W47 website covers: 12 blocks + 9 remade images (VOL.4)`
- 文件数：23（12 html M + 9 webp M + cover.json M + COVER-REPORT.md 新文件；单文件最大 200K，均 <5MB；无 .mp4/.webp 大文件以外的内容）
- 核实：`git diff --cached --stat` 23 files changed，348 insertions(+)，288 deletions(-)。

## 2. 生产源 commits（逐家）
方法见 §0b：每家 `find` 显式清单（排除 .pdf、/cards/、/svg/、__pycache__、*.pre-d5），
校验扩展名（仅 .py/.md/.txt/.json/.log/.sh + assets/ .jpg/.svg）与单文件 ≤5MB 后，
`git add --pathspec-from-file`，核对 staged ⊆ 清单、清单内未 stage 者均为已在 index 且与 HEAD 一致，
再 commit。以下“文件数”为该笔 commit 的 diff-tree 文件数；“清单”为 find 清单总数（差额 = 早已入 index 且未改动的文件）。

| # | target | SHA（全） | message | 文件数 | 清单 | 备注 |
|---|--------|-----------|---------|--------|------|------|
| 1 | de | 8d7281e7f07951658a0d17646a27b4a72832ce80 | W47 de production sources (VOL.4) | 224 | 231 | 7 已在 index 未改动；11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 2 | en | 819421130711a0ca84b29c216e619ddc0965a762 | W47 en production sources (VOL.4) | 276 | 277 | 1 已在 index 未改动；11 版均 kit=1 py=5 textmd=1 abstract=1；含 build-en.log |
| 3 | es | 7e83f9fbfca9182cc6c41f9a83959c5f0f129897 | W47 es production sources (VOL.4) | 188 | 188 | 11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 4 | fr | 2f963c9d0f6650dee49e51e2d5c6660950be7bc1 | W47 fr production sources (VOL.4) | 234 | 234 | 11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 5 | it | 5fcdf6ae1237c7565332376cb182cc727804cdc8 | W47 it production sources (VOL.4) | 255 | 255 | 含 core-it/scratch/*.py（2 个）；11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 6 | ja | a056c187d5fb689677b32d725ea121e76d20e368 | W47 ja production sources (VOL.4) | 228 | 228 | 11 版均 kit=1 py=5 textmd=1 abstract=1；含 core-ja/ja-gates.log |
| 7 | ko | 51fbb348faca4de521e71c7dceda08622a4da17c | W47 ko production sources (VOL.4) | 255 | 255 | 11 个 *.pre-d5 未进（见 §0b）；11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 8 | nl | 136c993074c9c545b684b8cb0e0c68f328c01099 | W47 nl production sources (VOL.4) | 273 | 265 | 264 源码 + 9 fanout-nl 删除（D×9 已核实）；11 版主目录 .text.md 齐全；11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 9 | pt | 3bc564c11a3530358459ee96358c95319fbe50b6 | W47 pt production sources (VOL.4) | 260 | 270 | 10 已在 index 未改动；11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 10 | ru | c7e98086d4b60727648448b9dcdef44a28826be7 | W47 ru production sources (VOL.4) | 247 | 267 | 20 已在 index 未改动；core-ru textmd=2（另有 2026-w47-ru-core.text.md）；其余 10 版均 kit=1 py=5 textmd=1 abstract=1 |
| 11 | zh-cn | b48601141a89b54e5d3a024bf81eb6ab3c9b718f | W47 zh-cn production sources (VOL.4) | 231 | 231 | 11 版均 kit=1 py=5 textmd=1 abstract=1 |
| 12 | zh-tw | 9c51e8bf677e68b38946f57f2a88b48a0abc9c12 | W47 zh-tw production sources (VOL.4) | 210 | 210 | 10 个目录（1 core + 9 fan-out）；10 版均 kit=1 py=5 textmd=1 abstract=1 |

- 每家 index 内文件总数（`git ls-files`）与 find 清单数逐家相等：de 231、en 277、es 188、fr 234、it 255、ja 228、ko 255、nl 265、pt 270、ru 267、zh-cn 231、zh-tw 210，合计 2911。
- 逐家运行日志：`run-de.log`、`run-rest.log`（en–ko）、`run-rest2.log`（nl–zh-tw）；每家清单：`list-<target>.txt`；staged 清单：`staged-<target>.txt`；驱动脚本：`commit_family.sh`（均在 PREP-LOG.md 同目录）。

## 3. 最终核实
- HEAD：`9c51e8bf677e68b38946f57f2a88b48a0abc9c12`；`git log --oneline -15`：
  ```
  9c51e8bf W47 zh-tw production sources (VOL.4)
  b4860114 W47 zh-cn production sources (VOL.4)
  c7e98086 W47 ru production sources (VOL.4)
  3bc564c1 W47 pt production sources (VOL.4)
  136c9930 W47 nl production sources (VOL.4)
  51fbb348 W47 ko production sources (VOL.4)
  a056c187 W47 ja production sources (VOL.4)
  5fcdf6ae W47 it production sources (VOL.4)
  2f963c9d W47 fr production sources (VOL.4)
  7e83f9fb W47 es production sources (VOL.4)
  81942113 W47 en production sources (VOL.4)
  8d7281e7 W47 de production sources (VOL.4)
  5c6b6db2 W47 website covers: 12 blocks + 9 remade images (VOL.4)
  b06cb15e §1.1 style: English W43, 11 editions re-rendered (VOL.1, D1 fix)
  b9ac29a6 tools: D5 gates + p8/occlusion/cover/run_build fixes (W47 review round)
  ```
- 本地分支：`main...origin/main [ahead 13]`——13 笔 commit 均在本地，**未执行任何 push，未碰远端**。
- `git status --porcelain`：**非空，535 行，全部为 `??`**。派单“13 笔后 status 为空”的目标未达成，原因是派单自身排除的渲染产物按设计不进这 13 笔：
  - 262 行：`*.pdf`（每版 2 个：正本 + .web.pdf；按派单 `':!*.pdf'` 排除）
  - 131 行：`*/cards/*` 目录（每版 1 个；按派单排除）
  - 131 行：`*/svg/*` 目录（每版 1 个；按派单排除）
  - 11 行：`*.pre-d5`（ko 家 svglib 备份；非源码扩展名，未擅自 commit）
  - 合计 262+131+131+11 = 535，与实测一致；除此四类外无任何剩余行（无 M、无 D、无其他 ??）。
- `git ls-files production/2026-w47/fanout-nl/`：0 行——9 个删除已入 nl commit，磁盘删除无内容损失（11 个 nl 主目录 .text.md 齐全已核实）。
- 封面 index：`covers/2026-w47/` + `production/covers/2026-w47/` 共 74 文件。
- 未做的事（按派单硬约束）：无 push、无 reset/stash、无 `git add -A`、无 `node lint.mjs --write`、无 insert.py、未改任何生产文件内容。
