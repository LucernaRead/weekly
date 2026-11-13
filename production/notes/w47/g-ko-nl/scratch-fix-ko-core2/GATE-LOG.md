# GATE-LOG — fix2 门禁记录（D7 + D6 重导核验，2026-11-11）

## 1. 探针与前置核对

| 检查 | 结果 |
|---|---|
| 开工探针 `git hash-object -w` + scratch 目录可写 | 通过（`9daeafb…`）；每次写盘前重探，均通过 |
| D6 工具修复落地：5 份 textmd.py 改前 md5 | 全同 `d308c826875ad58f604f181e80f0f847`（含 A1 分支） |
| 磁盘 | `/home/hatch` 余 77G；`/tmp` 512M tmpfs 已 100% 写满——本轮中间文件全放 workspace scratch，未用 `/tmp` |
| 改后 5 份 textmd.py md5 | 全同 `bc6394a387d15d4726e194687320da20`；`ast.parse` 语法通过 |

## 2. Census 复现（改前）——与 proof5 一致

工具：本目录 `census.py`（proof5 方法复现）。
`ex/match items total: 166`，`missing: 99`，
Counter `{'e': 70, 'e match_set': 9, 'qf': 4, 'a': 4, 'b': 4, 'c': 4, 'f': 4}`，
D6 `missing: 10`（见 `census-before.log`）。
与 proof5 `ex-census.txt` 逐项比对：99 项集合相同，仅 3 行文本有截断差异
（proof5 文件内截断：`…C. 54,980` vs 源码 `…C. 54,980원` ×2、
`…B. D-1은 1일이 지났어요 ·` vs 源码 `… · C. D-1은 오늘이 시험 날이에요`），
以 AST 读出的完整源码串为准。

## 3. Diff 审计（改前 → 试跑 → 实盘）

- 试跑输出 `2026-w47-ko-zh-cn.text.md.dryrun`（452 项、34,606 B、
  SHA `da1d3a32…`）；实盘落盘后 `cmp` 与试跑逐字节一致。
- `diff before dryrun`：新增非空行 122，删除非空行 3，净增 119 项。
  标题行、页分组（Page 1–8）不变；无其他行的改动。
- 净增 119 的构成（逐行核对，账目闭合）：
  1. D7 99 次缺失 → **94 个去重字符串**（5 次重复：同一题面跨版出现，
     如 `김치의 날은 언제예요? A. 11월 22일…` 在 qf/e/a 三处；
     收集器按 norm 去重，只留一行）。
  2. D6 **10 段**（wt/wcn/lt/lcn/lko/lcn2 + etvous×3 + MODELO）。
  3. **15 行**：子串普查判“在册”、但独立行缺失的真内容——
     配对左列词 7 行（위킴 페스티벌/한능검、내장산/월출산/두륜산/설악산、
     K리그1；`김장비용` 同为左列词，但属下述移位 3 行，不在此数内）、配对右列 3 行（웨더아이 예보 11월 11일、
     KIA가 LG를 3연승으로 이겼어요、삼성이 KIA를 3승 2패로 이겼어요）、
     P6 1차전题 1 行（`1차전은 어떻게 됐어요?…`，旧文件只含 P4 版
     `한국시리즈 1차전은…`，P6 变体为其子串故普查漏计）、
     `___` 填空题干 3 行（김치의 날은 11월 ___일이에요. /
     배추 20포기는 ___원이에요. / 김장비용은 4인 가족 기준 ___원이에요.
     + 올해 수험생은 ___명이에요.，共 4 行——其中 3 行为 P2 填空、1 行为 P5 填空；
     旧文件只含 P8 带选项的同源题，故普查判在册）。
     核实：15 行中 11 行在 8 个 SVG 文本节点中逐字在册；
     4 行 `___` 题干在 SVG 中以墨线填空呈现（P2 SVG 文本节点实测：
     `김치의 날은 11월             일이에요.`），与 KIT 既有裁定一致
     （`___` 在 SVG/PDF 渲染为 1.1pt 墨线）。
  4. **3 行移位**（删+增相抵，净 0）：`김장비용`、
     `한국시리즈 1차전은 어떻게 됐어요?…`、
     `올해 수험생은 몇 명이에요? A. 551,864명 · B. 1,312명 · C. 3,271명`——
     原经 P8 的 `f.*` 路径收在 Page 8 组下，现按题面所属版归到 P2/P4/P6 组。
- 94 + 10 + 15 = 119 ✓。新增行逐行读过（`added-lines.txt`）：
  无 print 调试串、无路径/文件名串、无代码串；`/` 只出现在 ` / ` 题面分隔符中。
- 说明：任务书预期 434–442 是按“99 + 10 − 偶然重复”估的；
  实际 452 = 333 + 119，其中 15 行是子串普查的盲区（非重复、非调试串），
  3 行是页归属更正——均已逐行核实，不构成回滚理由。

## 4. Census 复跑（改后，实盘）

`census-after.log`：`ex/match items total: 166`，`missing from text.md: 0`；
`D6 missing: 0`。D7 99 + D6 10 全部在册。

## 5. 未动项核实

| 项 | 核实 |
|---|---|
| content12/34/56/7/8.py | mtime 2026-11-11 00:06–08:40（任务开工 09:24 之前），未改 |
| 8 个 SVG | mtime 08:40–08:41，未改 |
| 印刷 PDF `Lucerna-VOL4.pdf` | 46,232,227 B，SHA `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`，与 proof5 一致 |
| 网版 PDF `Lucerna-VOL4-web.pdf` | 4,232,878 B，SHA `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7`，与 proof5 一致 |
| WEEKLY-KIT.md | 仅改 line 83（`___` 23→75 处）与 line 127（text.md 34,606 B / 452 项 / SHA `da1d3a32…` + fix2 注） |
| fan-out 4 版 text.md | 未重导（并入 ko 重扩 #3）；其 textmd.py 已同步为 `bc6394a3…` |
| ru / 其他语系 / W46 | 未碰 |
| commit / push | 未做 |

## 6. 证据索引（本目录）

- `FIX-LOG.md`（本轮补丁逐行说明 + 5 份 md5 + 重导前后数值）
- `census.py`（proof5 方法复现脚本）+ `census-before.log`（99 + 10）+
  `census-after-dryrun.log`（0 + 0）+ `census-after.log`（实盘，0 + 0）
- `2026-w47-ko-zh-cn.text.md.before`（改前 333 项备份）+
  `2026-w47-ko-zh-cn.text.md.dryrun`（试跑 452 项，与实盘逐字节同）+
  `added-lines.txt`（diff 新增非空行 122）
- `missing-sorted.txt` / `proof5-missing-sorted.txt`（与 proof5 ex-census 比对用）
- `probe.txt`（开工探针）
