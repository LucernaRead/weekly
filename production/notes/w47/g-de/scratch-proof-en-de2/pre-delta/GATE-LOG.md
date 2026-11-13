# GATE-LOG — 2026-W47 en-de 第二轮独立复校机械门记录

- 版：`2026-w47-en-de`；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（未用系统 python3）
- 日期：2026-11-11；命令均在 `~/workspace/weekly-git` 仓根或笔记目录下执行；输出存本目录 `gates/`，重建日志存本目录（`rebuild-run.log`），渲染图存 `render/`（p-1..p-8、w-1..w-8，pdftoppm 110 dpi 全新渲染）。
- 对照基准：proof1（`scratch-proof-en-de1/GATE-LOG.md`）与 fix1（`scratch-fix-en-de1/GATE-LOG.md`）全部绿，仅目视缺陷 D1 一条；本次全部门在 fix1 重建后的新成品上独立重跑（只读，不改源码/成品）。

## 0. 开工探针（双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 在 `hidden_files/w47/scratch-proof-en-de2/` 真实写小文件成功（`.probe`，完工后已删除）。`df -h`：`/home/hatch` 可用 46G，无配额问题；全程未遇 EDQUOT。

## 1. 身份核对（送审成品）

- `sha256sum` + `stat`：
  - `The-Lucerna-VOL4-en-de.pdf`：29,330,766 字节，`6f82363a63477603b9de4b7ad14967bc01d6bc68e7cbd1b961b8530b52d2d5c2`
  - `The-Lucerna-VOL4-en-de.web.pdf`：2,377,894 字节，`b2b686e4f9064ef4babdf02697671e5aaf73d1a87382015546d483d09b86181a`
  - `2026-w47-en-de.text.md`：51,948 字节
- `pdfinfo`：两 PDF 均为 8 页、1462.5 × 2025 pt。

## 2. occlusion_audit.py

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-de/svg`
- 结果：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`0 flags`。**PASS**

## 3. p8.py extract

- 命令：`tools/venv/bin/python tools/p8.py extract --p8 production/2026-w47/2026-w47-en-de/svg/p8-test.svg --total 150 --json gates/p8-extract.json`
- 结果：`noted set = 60 of 150 (parse: joined)`，与 core 集合相同。**PASS**

## 4. p8.py compare

- 命令：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-en/svg/p8-test.svg --edition-p8 production/2026-w47/2026-w47-en-de/svg/p8-test.svg --total 150 --json gates/p8-compare.json`
- 结果：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140, 150]`。与 proof1/fix1 完全一致，均为预期内（德语翻译键 + 写作题短标签；W46 en-de 同样 keydiff）。**PASS**

## 5. freeze

### 5a. baseline 等效（瘦复制重跑 + 直接 sha256 比对 8/8）

- 原因：沿用 proof1/fix1 的等效做法——`freeze.py baseline` 整树复制涉磁盘配额风险；本次在笔记目录内做瘦复制 `rebuild/`（仅 *.py + assets，9.8M），同一 tools/venv 解释器、同一构建源码重跑，不碰送审目录。
- 命令：在 `rebuild/` 内跑 `tools/venv/bin/python run.py`（日志 `rebuild-run.log`：exit 0，OVERFLOW/TOO WIDE 出现 0 次，TOTAL 150，MODEL 82），再对再生的 8 个 SVG 与送审 `svg/` 逐字节 `cmp` 比对。
- 结果：`p1-front MATCH`、`p2-life MATCH`、`p3-culture MATCH`、`p4-sport MATCH`、`p5-youth MATCH`、`p6-deep MATCH`、`p7-lang MATCH`、`p8-test MATCH`。**8/8 MATCH**

### 5b. freeze.py diff（core vs edition，只读）

- 命令：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-en/svg --edition-svg production/2026-w47/2026-w47-en-de/svg --json gates/freeze-diff.json`
- 结果：P7 +64/−55（与 fix1 一致——两句缩短的 gloss 各少 1 行）；P8 +99/−99；TOTAL 新增 CJK 字符共 9 个，全部为 U+3000。无英文正文改动。**PASS**

## 6. print/web 文字层一致

- `pdftotext` 两版各 48,018 字节；提取文本逐字节相同（`cmp gates/print.txt gates/web.txt` 通过）；token 多重集差 0/0（字节相同即蕴含）。
- web PDF 2,377,894 字节 < 7 MB。**PASS**

## 7. registry / 键比对（脚本独立核查）

- registry.json：150 条，`n` 连续 1–150；分版 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22。
- 与 core-en registry 比对：key 差异仅 [137, 138, 139, 140, 150]，级别差异 0。

## 8. 其他量化核查

- U+2019 全扫 8 个 SVG：每文件 0，总数 **0**。
- P8 最小字号：`svg/p8-test.svg` font-size 集合最小值 **13.5pt**（≥ 9.75pt）。
- VOL 核对（从提取文本计数）：VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与 proof1/fix1 一致；页脚逐页核实 `Seite 1 von 8` … `Seite 8 von 8`。
- 徽章矩形计数（60×30 rx=2.7，A2/B1/B2 三色）：P1 16、P2 15、P3 16、P4 16、P5 16、P6 19、P7 13、P8 23，与 core 逐页完全一致。
- 金句 8 条：脚本核对 print 提取文本，逐字命中 8/8。
- 禁词扫描（提取文本）：`W47 / 2026-w47 / 2026-W47 / cover / SOP / proofread / TODO / Lorem / placeholder / en-de / zh-cn / XXXX / TBD` 零命中。
- 日期/星期：`date -d` 核验 13 个日期，全部与正文星期一致。
- P7 坐标核查（送审 SVG）：8 条出处行全部 x=538.5（第 2 栏），末行 y=2509.40，紧跟金句末行 y=2455.03；第 3 栏顶部为 THE DRILLS，无孤行。
- P7 目视（双 PDF 全新渲染 110 dpi）：印刷与网页 P7 的第 2 栏底 / 第 3 栏顶均确认，D1 已修。
- ABSTRACT.txt：628 字节，德文单行，零 ASCII 双引号。
- fix1 两处改动核实：text.md 第 747、775 行为缩短后的 gloss；旧串 `(gewinnt immer wieder)`、`für Geschehenes` 全文扫描 0 命中。

## 门总汇

| 门 | 结果 |
|---|---|
| occlusion（tools/venv） | 0 flags，selftest OK |
| p8 extract | 60/150 noted set，与 core 相同 |
| p8 compare | CLEAN，keydiff 仅 137–140、150（预期） |
| freeze 直接 sha256 | 8/8 MATCH（等效瘦复制重跑，笔记目录内） |
| freeze diff | 新增 CJK 仅 9 个 U+3000；P7 +64/−55（fix1 改动所致） |
| print/web 文字层 | 各 48,018 字节，逐字节相同，token 差 0/0 |
| run.py 重跑（瘦复制） | exit 0，零溢出，150 题，MODEL 82 词 |
| registry | 150 条连续，分版/分级与 KIT 一致 |
| VOL.4 | VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与 proof1 一致 |
| 徽章 | 逐页与 core 一致（16/15/16/16/16/19/13/23） |
| P8 最小字号 | 13.5pt ≥ 9.75pt |
| U+2019 全扫 | 0 |
| 金句 | 8/8 逐字命中正文 |
| P7 目视（print + web 新渲染） | 8 条出处行均紧跟金句，第 3 栏顶无孤行，D1 已修 |

机械门全部通过；本轮全量复校零问题。
