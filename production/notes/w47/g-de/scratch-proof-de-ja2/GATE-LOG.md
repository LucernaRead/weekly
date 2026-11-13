# GATE-LOG — 2026-W47 de-ja proof2（门禁命令与 RC 全记录）

工作目录 `S` = `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-ja2`
版目录 `E` = `~/workspace/weekly-git/production/2026-w47/2026-w47-de-ja`
venv = `~/workspace/weekly-git/tools/venv/bin/python`

## 开局探针（2026-11-11，命令环节，见本目录 probe.txt 与 PROOF-NOTE §0）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` RC=0；scratch 内真实写盘 ok。

## SHA 核对（开工前 + 复校后两次）

- `sha256sum $E/Die-Lucerna-VOL4-de-ja.pdf $E/Die-Lucerna-VOL4-de-ja-web.pdf $E/2026-w47-de-ja.text.md`
- 结果（两轮一致）：`2638a6e62c00da39933a3e921bb74d0d81d6cc00ddf2eff50000c182554f98e1` / `161f2dd0bdfefecffe06944ded2d22f22410daeb321e7bc387c745da9cbcce16` / `a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69`，字节 23,901,741 / 2,155,095 / 51,913。

## 渲染与文字层

- `pdftoppm -r 100 ${E}/Die-Lucurna-VOL4-de-ja.pdf S/png/print` → `print-1..8.png`；同法 `-r 100` web → `web-1..8.png`；`-r 200 -f 7 -l 8` print → `print200-7.png` `print200-8.png`。
- `pdftotext -layout` 双版 → `txt/print.txt` `txt/web.txt`（各 112,955 B）；`diff txt/print.txt txt/web.txt` → 空（0 行，RC=0）。
- 裁切（PIL，venv）：`png/crop-p7-toolbox-200dpi.png`、`png/crop-p8-hbox-200dpi.png`、`png/crop-p8-key67-200dpi.png`。

## 门禁（每条的 RC 与输出文件）

| # | 门禁 | 命令（摘要） | RC | 输出 |
|---|---|---|---|---|
| 1 | occlusion audit | `venv python tools/occlusion_audit.py $E/svg --json gates/occlusion.json`（含自检 6/6 + clean 对照） | 0 | `gates/occlusion.json`：**0 flags** |
| 2 | canonical creambox（全版 8 页） | `venv python creambox.py $E/svg/*.svg`（本 scratch 内逐字节副本） | — | `gates/creambox-all.log`（32 盒，最小 inside +10.4 / desc +4.5） |
| 3 | p8 extract | `tools/p8.py extract --p8 p8-uebungen.svg --total 150` | 0 | 150/150（joined） |
| 4 | p8 compare | `tools/p8.py compare --core-p8 core-de/p8-uebungen.svg --edition-p8 … --total 150` | 0 | CLEAN；keydiff=[137,138,139,150] |
| 5 | freeze diff | `tools/freeze.py diff --core-svg core-de/svg --edition-svg $E/svg --strict-cjk` | 0 | `gates/freeze.log`：TOTAL added CJK 2,994（P7 +412，P8 +1,112） |
| 6 | freeze_direct（rebuild-A 字节同） | `fd/freeze_direct.py ja $E gates/`（脚本 fd/ 内 rebuild-A 逐字节副本；tr_ja.py + cjk_inventory.json + stub_svg.py + stub_bslib.py 引自 scratch-fanout-de） | 1（按设计） | `gates/freeze-direct.log` / `gates/freeze-direct.json`：rendered 8/8；frozen 144/164/200/166/179/173/163/183；sha8 `b01ba1b1/2db0dd83/2dd3b3f2/df1bebf7/e7b235f9/89156519/b854370f/1c855c30`；removed 516 / added 524；unaccounted 仅 JP 字体开关 4 串 |
| 7 | boxtitle（rebuild-A 字节同） | `fd/boxtitle.py ja $E gates/` | 0 | `gates/boxtitle.log`：7/7 fit（≤400.5） |
| 8 | keycheck（rebuild-A 字节同） | `fd/keycheck.py ja $E gates/`（需 p8extract.json，复制自 scratch-fanout-de/ja/） | 0 | `gates/keycheck.log` / `gates/keycheck-150.json`：149/150；仅 Q150 PREFIX |
| 9 | verify.py（副本上跑，未碰原版） | `verify-copy/verify.py`（仅 BUILD 路径指向副本） | 0 | `gates/verify.log`：TOTAL 150；SVG byte-identical；§1.1 True；verbatim OK；P8 floor True 9.9375pt |
| 10 | d2scan（abutting） | `d2scan.py ja d2-scan.json`（fix scratch 工具） | 0 | `gates/d2scan.log` / `gates/d2-scan.json`：67 对，web gap >0.5pt：0 |
| 11 | P8 最小字号（PyMuPDF） | `venv python` 计算双版 `p8 min font pt` | — | 印刷/网页均为 **9.94pt** |
| 12 | 200 dpi 宽引号测量 | `quote_pixel.py` + `quote-spots.json`（de-zh-tw 同法） | — | H 框 1.80pt = 0.11em PASS；Q67 0.72pt = 0.07em PASS（详见 PROOF-NOTE §2） |
| 13 | P1 字体 flags（T1/T2 复核） | PyMuPDF rawdict span `flags`（bold bit 4 / italic bit 1） | — | 刊别行 ×3 Bold（27.0pt，`LucernaNotoSerifCJKJP-Bo`）；`« der Adventskalender »` 斜体（`LucernaNewsreader-Italic`）；全页 bold 数网页 ≥ 印刷 |
| 14 | 印/网像素差（8 页） | 100 dpi 渲染逐页 `mean|diff|`（PIL） | — | P1 0.53 / P2 0.00 / P3 0.20 / P4 0.32 / P5 0.33 / P6 0.00 / P7 0.12 / P8 0.10 |
| 15 | Q34 计数 | text.md + 8 SVG：新题干 1×/1×，旧题干 0×/0× | — | 计数与 grep 同义（U+201C 33 / U+201E 33 / U+00AB 6 / U+00BB 6） |
| 16 | chips 交叉核对 | `grep -ri "chip" scratch-fanout-de/ja/*.log`（rebuild1/2/3.log） | — | 141（P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35；P8 A2 22 / B1 13） |
| 17 | Q108 tr_ja 残留 | `grep -n "比平时更安静" scratch-fanout-de/tr_ja.py`；`grep -rn` 全版文件 | — | 仅 tr_ja.py 201 行（源查找键）；本版文件 0×；`Stiller als sonst` text.md 1×（日语选项正确） |
| 18 | 事实网查 | browser.search ×14（2026-11-11 当天） | — | 见 PROOF-NOTE §3：欧冠/欧联/德甲/国家队/圣诞市/Kepler/Ritter/Stromsteuer/预算/第 5 轮赛程 / Buß- und Bettag 法条（SächsSFG §6）全部核实 |
| 19 | 日期核实 | `date -d` / 日历比对（2026-11-03…11-29 星期） | — | 全部正确 |
| 20 | ABSTRACT 核对 | 读 `ABSTRACT.txt`（426 B，单行，日语，无 ASCII 双引号） | — | §9 合规 |
| 21 | 复核（RC/证据） | 结束前三件 SHA 重新核对 + `git status` | — | SHA 未变；`?? production/2026-w47/2026-w47-de-ja/`（未追踪，未改动） |

## 说明

- rebuild-A 脚本与 scratch-fanout-de 旧副本以 diff 逐字节比对过（`freeze_direct.py`、`boxtitle.py`、`keycheck.py`、`stub_svg.py`、`stub_bslib.py` 均无差异）；rebuild-A 没有 `tr_ja.py`，故脚本在 `fd/` 内从数据副本运行，执行路径只是工作目录差别，不改脚本内容。
- `freeze_direct` RC=1 细项：`unaccounted removed 1`（`Noto Serif CJK SC`）、`added 3`（`JP`、`Noto Sans CJK JP`、`Noto Serif CJK JP`）——KIT §5 已载明 JP 字体切换；不影响定稿。
- 本目录未写入 repo 的 `hidden_files/w47/`；未改动 repo 任何文件。
