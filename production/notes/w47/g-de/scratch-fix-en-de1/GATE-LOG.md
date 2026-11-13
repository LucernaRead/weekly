# GATE-LOG — 2026-W47 en-de fix1 机械门记录

- 版：`2026-w47-en-de`；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3；未用系统 python3）
- 日期：2026-11-11；命令均在 `~/workspace/weekly-git` 仓根或版目录下执行；输出存本目录 `gates/`，运行日志存本目录（`run.log`、`render.log`、`webpdf.log`、`textmd.log`、`rebuild-run.log`、`dbg2.log`）。
- 对照基准：proof1（`scratch-proof-en-de1/GATE-LOG.md`）全部绿，仅目视缺陷 D1 一条；本次全部门在重建后的新成品上重跑。

## 0. 开工探针（双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 在 `hidden_files/w47/` 真实写小文件成功（`.probe-fix-en-de1`，完工后已删除）。`df -h`：可用 46G。

## 1. 身份核对（新成品）

- `sha256sum`：
  - `The-Lucerna-VOL4-en-de.pdf`：29,330,766 字节，`6f82363a63477603b9de4b7ad14967bc01d6bc68e7cbd1b961b8530b52d2d5c2`
  - `The-Lucerna-VOL4-en-de.web.pdf`：2,377,894 字节，`b2b686e4f9064ef4babdf02697671e5aaf73d1a87382015546d483d09b86181a`
- `pdfinfo`：两 PDF 均为 8 页、1462.5 × 2025 pt。
- SVG 快照比对：修前 8 个 SVG 哈希存 `/tmp/fix-en-de1-svg-before.txt`；重建后仅 `p7-lang.svg` 变化，其余 7 个 `sha256sum -c` 均 OK。

## 2. occlusion_audit.py

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-de/svg`
- 结果：`selftest OK: planted classes fired {...}; clean controls silent`；`0 flags`。**PASS**

## 3. p8.py extract

- 命令：`tools/venv/bin/python tools/p8.py extract --p8 production/2026-w47/2026-w47-en-de/svg/p8-test.svg --total 150 --json gates/p8-extract.json`
- 结果：`noted set = 60 of 150 (parse: joined)`，与 core 集合相同（P8 SVG 未动，预期内）。**PASS**

## 4. p8.py compare

- 命令：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-en/svg/p8-test.svg --edition-p8 production/2026-w47/2026-w47-en-de/svg/p8-test.svg --total 150 --json gates/p8-compare.json`
- 结果：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140, 150]`。与 proof1 完全一致，均为预期内（德语翻译键 + 写作题短标签；W46 en-de 同样 keydiff）。**PASS**

## 5. freeze

### 5a. baseline 等效（瘦复制重跑 + 直接 sha256 比对 8/8）

- 原因：proof1 已记——`freeze.py baseline` 整树复制时磁盘配额（EDQUOT）中断；本次沿用其等效做法（同一 tools/venv 解释器、同一构建源码的瘦复制 `rebuild/`，4.3M，不含 PDF/cards），不在送审目录内重跑。
- 命令：在 `rebuild/` 内跑 `tools/venv/bin/python run.py`（日志 `rebuild-run.log`：exit 0，零 OVERFLOW / TOO WIDE，TOTAL 150，MODEL 82），再对再生的 8 个 SVG 与送审 `svg/` 逐字节 sha256 比对。
- 结果：`p1-front MATCH`、`p2-life MATCH`、`p3-culture MATCH`、`p4-sport MATCH`、`p5-youth MATCH`、`p6-deep MATCH`、`p7-lang MATCH`、`p8-test MATCH`。**8/8 MATCH**

### 5b. freeze.py diff（core vs edition，只读）

- 命令：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-en/svg --edition-svg production/2026-w47/2026-w47-en-de/svg --json gates/freeze-diff.json`
- 结果：P7 +64/−55（proof1 为 +66/−55——两句缩短的 gloss 各少 1 行，正是本次改动）；P8 +99/−99；TOTAL 新增 CJK 字符共 9 个，全部为 U+3000。无英文正文改动。**PASS**

## 6. print/web 文字层一致

- `pdftotext` 两版各 48,018 字节（proof1 为 48,076——P7 两行德语 gloss 缩短所致）；提取文本逐字节相同（`cmp` 通过）；token 多重集差 0/0。
- web PDF 2,377,894 字节 < 7 MB。**PASS**

## 7. run.py 重跑（真版）

- 命令：版目录内 `tools/venv/bin/python run.py`（日志 `run.log`）。
- 结果：**exit 0**；`OVERFLOW`/`TOO WIDE` 出现 0 次；`flow[P7-main] ended col 2/2 y=1786 (bottom 2560)`；`TOTAL exercises: 150`；`MODEL words: 82`。**PASS**

## 8. 其他量化核查

- U+2019 全扫 8 个 SVG：每文件 0，总数 **0**。
- P8 最小字号：`svg/p8-test.svg` font-size 集合最小值 **13.5pt**（≥ 9.75pt）。P8 SVG 未动，与 proof1 一致。
- VOL 核对（从提取文本计数）：VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与 proof1 一致（VOL.5 8 处均为合法下期预告，VOL.3 3 处与 core 一致）；P1 SVG byte-identical，刊头 VOL.4 未动。
- P7 坐标核查（送审 SVG）：8 条出处行全部 x=538.5（第 2 栏），末行 y=2509.40，紧跟金句末行 y=2455.03；第 3 栏顶部为 THE DRILLS（y=228），无孤行。
- P7 目视（新双 PDF 全新渲染 110 dpi）：印刷与网页 P7 的第 2 栏底 / 第 3 栏顶裁图均确认（`render/p7new-*.png`、`render/wp7new-*.png`）。
- `.text.md` 重导后 diff 仅两行 gloss（51,989 → 51,948 字节）；stub/real registry 各 150 条。

## 门总汇

| 门 | 结果 |
|---|---|
| occlusion（tools/venv） | 0 flags，selftest OK |
| p8 extract | 60/150 noted set，与 core 相同 |
| p8 compare | CLEAN，keydiff 仅 137–140、150（预期） |
| freeze 直接 sha256 | 8/8 MATCH（等效瘦复制重跑） |
| freeze diff | 新增 CJK 仅 9 个 U+3000；P7 +64/−55（改动所致） |
| print/web 文字层 | 各 48,018 字节，逐字节相同，token 差 0/0 |
| run.py 重跑 | exit 0，零溢出，150 题，MODEL 82 词 |
| VOL.4 | VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与 proof1 一致 |
| P8 最小字号 | 13.5pt ≥ 9.75pt |
| U+2019 全扫 | 0 |
| P7 目视（print + web 新渲染） | 8 条出处行均紧跟金句，第 3 栏顶无孤行 |

机械门全部通过；D1 已修，观察项未动。
