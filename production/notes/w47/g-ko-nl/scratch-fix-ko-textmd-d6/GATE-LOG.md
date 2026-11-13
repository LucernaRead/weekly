# GATE-LOG — ko textmd.py D6 修复核验（2026-11-11）

## 1. Scratch 重导（只写 scratch，不写版目录）

命令（每版均用 `/usr/bin/python3`，按 KIT 解释器锁定）：
`/usr/bin/python3 <dir>/textmd.py <dir> <slug> scratch-fix-ko-textmd-d6/reexport/<slug>.text.md "<title>"`
标题取自各版现行 text.md 首行（`Lucerna Korean Weekly VOL.4 — Korean text, <读者语> explanations (2026-W47)`）。

| 版 | 旧项数 | Scratch 重导项数 | 增量 |
|---|---|---|---|
| core-ko（`2026-w47-ko-zh-cn`） | 333 | 343 | +10 |
| ko-de | 332 | 340 | +8 |
| ko-en | 332 | 340 | +8 |
| ko-es | 332 | 340 | +8 |
| ko-fr | 332 | 340 | +8 |

与评估报告预期（core 333 → 约 343；ko-de 332 → 约 340）完全一致。

## 2. Diff 摘要（scratch 重导 vs 版目录现行 text.md；完整 diff 存 `diff-all.txt`）

- 5 版全部：**只增不减，removed = 0**（core-ko +20 行、其余各 +16 行；
  每新增项 2 行：正文 1 行 + 空行 1 行）。无 fix1 内容漂移、无既有行改动。
- 新增行恰为漏载清单，无多余串、无 print 调试串：
  - core-ko（10 段）：`etvous` ×3（content12:222、content34:63、content56:45）、
    `wt`（content7:80）、`wcn`（:81）、`lt`（:90）、`lcn`（:91）、`lko`（:92）、
    `lcn2`（:93）、`MODELO`（content8:99）。
  - ko-de/en/es/fr（各 8 段）：`etvous` ×3、wt、wcn、lt、lcn（各版译文形态）、MODELO。
- 页码落点核验（scratch 重导文件内 `## Page N` 分组检查）：
  etvous → Page 2 / Page 3 / Page 5；wt、lt → Page 7；MODELO → Page 8。5 版全过。
- 关键片段核验：`안녕하세요` 在 5 版 scratch 重导中各出现 1 次（旧 text.md 为 0 次）。
- 句面注：core-ko 与 ko-es 的 `wt` 为 fix1 更新后的句面
  （`수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`，评估报告 §2.3 已记录），
  旧句 `수능 후에 김치의 날이 와요` 在两版 scratch 重导中出现 0 次（源文件已改，无残留复本）。

## 3. 版目录 text.md 未被触动

- 5 版现行 text.md 的 mtime 仍为本次任务开工前（core-ko 2026-11-11 08:47:43、
  ko-de 08:48:25，任务开工约 09:21 UTC）；本次只读了它们做 diff 基线。
- 无 commit、无 push；`git status` 只显示 2026-w47 整目录 untracked（仓库既有状态，
  非本次改动所致——本次只改了 5 份 textmd.py，未动其他文件）。
