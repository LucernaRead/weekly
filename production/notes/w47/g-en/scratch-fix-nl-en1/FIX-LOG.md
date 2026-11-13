# FIX-LOG — W47 nl-en fix1 (proof1 D12, build 11) — PROBE OK `git hash-object -w /dev/null` = e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 RC=0 | NEW SHA print `79fa049b318d94f15f28fe23daefd2513221a77fde6511c694aee109bacf3239` / 12,665,893 B, web `d493e11f3c27c7e46e0412c79f1b9208bfe804e39eac2e2203a033fad2818538` / 1,610,562 B, text `9596c4acbb27c20c0f1581dff99ac8871ad0937ec5839397f0fa9d3087a87978` / 45,115 B | D12 POST-FIX (rebuilt P8 card, 1:1 SVG units): 142 adv 215.5px, ink [1441,1652], right margin 210.0px; 144 adv 158.6px, ink [1441,1595], right margin 267.0px; baselines 141–145 uniform 29.66px, single line, inside column [1439.5, 1862.0] (422.5px), no wrap/overflow | GATES: gates.py 9/9 ALL PASS (occlusion 0, p8 150/150 CLEAN keydiff [137,138], freeze repro 8/8, print/web pos0 ms0, P8 font 10.12pt, chips=core, §1.1 clean), freeze core baseline 8/8, cream 0, spill 31 (set identical to build 10), orphan 0/0/0, strict-CJK RC=1 adjudicated U+3000 false positive (same as build 10 O2) | UNCOMMITTED, UNPUSHED; second full proof round still required (SOP §8.4)

- 版：`2026-w47-nl-en`（荷兰语目标语 × 英语读者），VOL.4，刊期 2026-11-16–2026-11-22
- 任务：修 proof1 (b) 唯一缺陷 D12；全量重建；全部机械门重跑；更新 KIT；未 commit、未 push
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-nl-en1/`（`work/` 为 scratch 内重建副本；`tmp/` 为 TMPDIR）
- 修复员：fix1（与 proof1 不同人）。协调员已独立核对源码，D12 属实。

## 0. 开工探针（2026-11-11 20:43 UTC）

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0。探针通过后才动手。
- scratch 真实写文件成功（`probe.txt`）。
- 注意：任务称该 scratch 为“全新目录”，实盘并非全新——内含上一轮 fix1（D1 弯引号，build 8）的 `FIX-LOG.md` / `GATE-LOG.md` / `en-*8.log` / `PROBE.txt`。未覆盖：旧 `FIX-LOG.md` → `FIX-LOG-build8-D1-archived.md`，旧 `GATE-LOG.md` → `GATE-LOG-build8-D1-archived.md`（均原样保留在同一目录）；本轮日志另存新文件（`*11.log` / `FIX-LOG.md` / `GATE-LOG.md`）。
- 磁盘：`/home/hatch` 可用 57G。TMPDIR 全程 = 自有 scratch 下 `tmp/`，未用系统 /tmp（一次 `pdftotext` 误写 `/tmp/old-print.txt` 后立即删除并改写到 scratch 内重做——见 §5）。

## 1. 身份核验（修前，盘上实测，与任务值逐字节一致才继续）

| 文件 | 字节 | SHA-256 | 与任务登记 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷，build 10） | 12,665,899 | `29073788fa2fc7dfd426e6d209251f0919bdbf2cb33f79dbbc10eb15f92b2342` | 一致 |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页，build 10） | 1,610,560 | `6fd0ad3d700d686f9889faecd5e6076a6d9c309372f6871ad0faa4e41a253f98` | 一致 |
| `2026-w47-nl-en.text.md` | 45,111 | `84ed9f3555e4995de8c4450ca9180019414ad907a63ed384ab632a8293612f91` | 一致 |

三 SHA 全部一致，继续。证据：proof1 `PROOF-NOTE-build10.md` + `GATE-LOG-build10.md`（`scratch-proof-nl-en2/`）已读；其收工复核 SHA 与上述一致。

## 2. 缺陷核实（修前，独立重扫，非照搬 proof1）

- D12 属实：`content8.py:85` = `["journaal = news programme b", "groepswinst=group win c", "schoen = shoe d", "gedicht=poem a"]`（141/143 有空格，142/144 没有）；`.text.md` 第 419 行（142 题）与第 421 行（144 题）同样缺空格（任务所称“第 142/144 行”为题号，文件行号为 419/421）；`svg/p8-toets.svg` 中 `142. c — groepswinst=group win c`（y=2297.3）、`144. a — gedicht=poem a`（y=2356.6）。键无误（141–144 = b/c/d/a）。
- 独立重扫（自写 `sweep_eq.py`：`content*.py` 字符串字面量 AST 提取 + SVG `<text>` 节点 + `.text.md`，逐个 `=` 查左右空格；`==` 排除）：缺空格 `=` 仅此 2 处（6 个表面命中：源码 ×2、SVG ×2、text.md ×2），与 proof1 的 `eq-spacing-sweep.log` 逐项一致。` = ` 有空格：全版 121 处；`.text.md` 内 40 行（含 39 条 D/F 配对注释 + 1 条 gloss 行 `groepswinst = group win: first in the group…`，故与 proof1 的“39 处”无矛盾——39 是配对注释口径）。

## 3. 改动（只改 1 个源码文件，2 处字符串；先在 scratch 副本改，验证后再落生产）

| 文件 | 行 | 改动 |
|---|---|---|
| `content8.py` | 85 | `groepswinst=group win c` → `groepswinst = group win c` |
| `content8.py` | 85 | `gedicht=poem a` → `gedicht = poem a` |

- 141/143 一字不动，其余 39 处不动。P8 标题 `A　VUL DE KRONIEK IN` 未动（proof1 观察 O1，非缺陷）。
- 安全路径：`content*.py` 的 `OUT = dirname(__file__)/svg`（已逐文件验过），`render.py` 的 `BASE = dirname(__file__)`——OUT/BASE 跟源码位置走。因此先 `cp -a` 整版到 scratch `work/2026-w47-nl-en/`（`diff -r` 验过与生产逐字节一致，`cp` 所有权警告无害），在副本里改、重建、验门，全部通过后才把已验证的输出拷回生产。生产 SVG 从未被重建过程直接写过；全程 `PYTHONDONTWRITEBYTECODE=1`。
- 副本改后 `diff -r` 生产 vs 副本：仅 `content8.py:85` 一行不同；`py_compile` 通过；改后重扫副本源码：缺空格 `=` 0（剩余 4 处为待重建的旧 SVG/text.md，符合预期）。

## 4. 重建（build 11，全量，均在 scratch 副本内，`tools/venv/bin/python`）

- `run.py` rc=0：TOTAL **150**（逐页 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；complete 65 / choice 44 / matching 8 / true-or-false 7 / make-sentences 8 / cloze-choice 13 / translate 4 / writing 1；范文 81 词）；`overflow` / `TOO WIDE` 命中 0。P4 col3 ends 1229.6（D11 在位），P7 col3 ends 1927.5，P3 col3 1106.6（均与 build 10 相同）。
- 重建 SVG 8/8：与生产 build 10 逐字节比较，7 张 SAME，仅 `p8-toets.svg` DIFF；p8 文本 run 383=383，仅 2 行变（142/144 两行加空格），其余一字不动。
- `render.py` rc=0：cards 8 张（仅 `p8-toets.png` 变，其余 7 张逐字节 SAME）；印 PDF 12,665,893 B（−6 B，坐标数字长度变化所致；文字层见 §5 逐行核对无误）。
- `webpdf.py` rc=0：网 PDF 1,610,562 B（+2 B），45,438 text bytes（+4 = 4 个新增空格）。
- `export_fanout.py . en` rc=0：`.text.md` 45,115 B（+4 B）；142 单题行 + 2 match headers + 8 match items = 150；8 golden；6 gloss。
- 日志：`en-build11.log`、`en-render11.log`、`en-webpdf11.log`、`en-export11.log`（本目录）。

## 5. 新交付物（build 11）与变更范围核对

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `De-Lucerna-VOL4-nl-en.pdf`（印刷） | 12,665,893 | `79fa049b318d94f15f28fe23daefd2513221a77fde6511c694aee109bacf3239` |
| `De-Lucerna-VOL4-nl-en-web.pdf`（网页） | 1,610,562 | `d493e11f3c27c7e46e0412c79f1b9208bfe804e39eac2e2203a033fad2818538` |
| `2026-w47-nl-en.text.md` | 45,115 | `9596c4acbb27c20c0f1581dff99ac8871ad0937ec5839397f0fa9d3087a87978` |

- 变更范围（生产盘上实测，以修前 `prod-pre-copy.sha256` 全版 42 文件记录为准）：相对 build 10 恰好 7 个文件变——`content8.py`（源码修）、`svg/p8-toets.svg`、`cards/p8-toets.png`、`De-Lucerna-VOL4-nl-en.pdf`、`De-Lucerna-VOL4-nl-en-web.pdf`、`2026-w47-nl-en.text.md`、`WEEKLY-KIT.md`（追加 §11）。其余 35 个文件一字未动；core-nl 与其他版未碰；生产 `svg/` 与 `cards/` 与已验证的 scratch 构建逐字节一致。
- `.text.md` diff vs build 10：仅 419/421 两行。印/网 PDF 文字层 diff vs build 10：仅 142/144 两行（`pdftotext` 全文比对，45,434 B → 45,438 B）。印 vs 网新文字层 diff：0。P8 标题未动（SVG diff 已证仅 2 行变）。

## 6. D12 修后实测（P8 答案区，`p8_width.py`，双重度量）

重建后的 P8 卡片 `cards/p8-toets.png`（1950×2700，与 SVG 坐标 1:1）+ 构建器自用的 `svglib.text_w`（Newsreader 13.5pt）：

| 行 | advance | 像素墨右缘 | 栏右余量（栏 [1439.5, 1862.0]，宽 422.5px） |
|---|---|---|---|
| 141. b — journaal = news programme b | 238.5px | 1675 | +187.0px |
| **142. c — groepswinst = group win c** | **215.5px** | **1652** | **+210.0px** |
| 143. d — schoen = shoe d | 152.4px | 1588 | +274.0px |
| **144. a — gedicht = poem a** | **158.6px** | **1595** | **+267.0px** |
| 145. A — schoen = shoe | 142.0px | 1579 | +283.0px |

- 141–145 基线 [2267.60, 2297.26, 2326.92, 2356.58, 2386.24]，间距均匀 29.66px——无插入的换行、无溢出、无换行后顶位移。proof1 估算“约 300px”为保守估计，实测 142 行仅 215.5px、144 行仅 158.6px，余量充足。
- 注：初版 `p8_width.py` 的像素换行探针曾把 140 题（本身为合法两行答案）的续行误判为换行——已修正为基线间距法（上表），脚本与日志 `p8-width11.log` 在本目录；140 题未动，非本轮范围。

## 7. 门禁汇总（build 11，详见 `GATE-LOG.md`）

| 门 | 结果 |
|---|---|
| run.py rc=0 / TOTAL 150 / 0 溢出 | 通过 |
| SVG 重建 8/8（freeze repro 逐字节） | 通过 |
| freeze 核心 baseline 8/8 | 通过 |
| freeze diff `--strict-cjk` | RC=1，裁定误报（见下） |
| occlusion 0 flags | 通过 |
| 奶油盒 PIL 真墨扫 0 flags + 像素复核 | 通过（0 flags） |
| spill 31 候选 | 通过（与 build 10 集合逐项相同，无盒内溢出） |
| 孤儿扫 (a)/(b)/bruteforce 0/0/0 | 通过 |
| p8 extract 150/150 | 通过 |
| p8 compare CLEAN，keydiff [137, 138] | 通过（与 build 10 相同，合法重定向） |
| P8 最小字号 10.12pt ≥ 9.75pt | 通过（min=median，187 spans） |
| 印/网文字层 8/8 posdiff=0、msdiff=0 | 通过（tokens 790/828/738/735/807/748/915/2323；P8 +4 = 2 个新增空格各拆 1 个 token 为 3 个） |
| pdftotext 印=网=45,438 B；网 PDF < 7 MB | 通过 |
| §1.1 SVG 审计 | 通过（off-palette {}，无金，描边矩形 0，VOL.5=5=core，纸色填充 8） |
| P8 芯片 = core {A2:8, B1:24, B2:3} | 通过 |
| 修后 `=` 缺空格重扫（源码+SVG+text.md） | **0** |

- `freeze diff --strict-cjk` RC=1 的裁定（与 build 10 O2 同案）：新增 CJK 15 个，全为 U+3000（p1 +1、p2–p8 各 +2）；重建后全版可见文本 CJK 清单 127 个，全部是 U+3000，零汉字、零 CJK 标点。U+3000 为 SOP §1.1 强制分隔符，core 每版亦有 12–19 个；strict 规则限定 zh/ja 版。本版为 en 读者版，不适用。**误报，非缺陷。**

## 8. 记录更新

- `WEEKLY-KIT.md`（生产版目录）：追加 `## 11. Fix round 1` 一节（缺陷、改法、重建、D12 实测、门禁汇总、新三 SHA + 旧三 SHA 保留在该节内）；其余 KIT 内容不动（§6 仍记 build-10 SHA，以 §11 新 SHA 为准——按任务要求只追加一节）。
- 本目录交付物：`FIX-LOG.md`（本文件）、`GATE-LOG.md`（新写，build 11）、`sweep_eq.py`、`p8_width.py`、`gates.py`（`scratch-fanout-nl/gates.py` 的副本，防写回 builder scratch）、`geo2.py`（proof1 `geo2.py` 的副本，ED/S 常量改指本轮 scratch）、`geo2v2.json`、`en-*11.log`、`eq-sweep-*.log`、`freeze-*.log`、`p8-*.log`、`old/new-print/web.txt`、`prod-pre-copy.sha256`、`gates-en.json`。

## 9. 结论

D12 已修（源码 2 处字符串，全量重建，修后 `=` 缺空格 0 处）；P8 两行实测在栏内、无换行、无溢出；全部机械门绿（仅 strict-CJK 为已裁定的 U+3000 误报，与 build 10 同案）。生产变更恰好 7 个修复相关文件。未 commit、未 push。待协调员另派第二轮全量复校（SOP §8.4）。
