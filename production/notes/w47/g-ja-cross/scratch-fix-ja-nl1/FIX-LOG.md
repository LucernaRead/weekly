# FIX-LOG — 2026-W47 ja-nl 第一轮返修（D1/D2/D3）

- 返修 builder：叶子（第一轮返修；与 ja-nl builder、ja 核心 builder、第一轮复校员不同的人）
- 日期：2026-11-11
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-nl/`（目标语日语 × 读者母语荷兰语，VOL.4，刊期 2026-11-16–22）
- 缺陷：proof1 (b) 3 条（D1 中、D2 高、D3 高）；观察项 O1–O8 一律未动。
- 记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja-nl1/`（绝对路径，不写进仓内 hidden_files）
- 红线遵守：只改 `production/2026-w47/fanout-ja/2026-w47-ja-nl/` 内文件与本笔记目录；未碰 core-ja、其他家庭、tools/、issues/；未跑 insert.py、lint --write；未 git add/commit/push/reset/stash（只读 `git status` 核查范围一次）。工作树既有 `issues/2026-w43/` 修改为开工前已存在（复校 O8 同述），与本轮无关。
- 依据：SOP.md §8/§1.1 全文、`WEEKLY-KIT.md`、`EDITION-RECORD.md`、复校笔记 `scratch-proof-ja-nl1/PROOF-NOTE.md` + `GATE-LOG.md`、同家庭 ja-fr/ja-en fix1 日志（做法参照）。

## 0. 开工探针（双通才动手，08:02 UTC）

- `echo probe-ja-nl-fix1 | git -C ~/workspace/weekly-git hash-object -w --stdin` → `1043d7b1f7e73a44ca830703e3521f6f2d9b9ca1`，成功。
- `scratch-fix-ja-nl1/.probe` 真实写盘成功。磁盘 `df -h`：46G 可用。
- 构建解释器：`tools/venv/bin/python`（SOP/AGENTS 规定；与第一轮复校同一解释器）。

## 1. 修前身份核对（与任务书逐字一致）

| PDF | 字节 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4-JA-NL.pdf` | 29,099,171 | `c18c551af2249561000dd50821d4e9646597c5a2cdccf316b02ee38128d40a19` |
| 网页 `Lucerna-VOL4-JA-NL-web.pdf` | 4,476,557 | `e0678a4b892ff07080d48a51b2f8b7c9ee109916752df537849000370ad9cb81` |

双 PDF 各 8 页。text.md 45,685 字节、1379 行。

## 2. 独立核实（动手前，缺陷在盘上属实）

### D1 — P2 词条框两条荷兰语释义溢出

- SVG 实测（`svg/p2-kurashi.svg`）：4 格词框同为 y=1618/h=150（底缘 1768）；「熊手」格与「小雪」格释义各两行，第二行基线 y=1776.76，悬在框外；另两格一行、基线 1752.06，在框内。属实。
- 构建库同款量尺复核（`svglib.wrap()`，19px sans / 378.5px，与渲染同一函数）：
  - `een bamboe hark voor voorspoedige zaken` 380.1px → 2 行（`een bamboe hark voor voorspoedige` / `zaken`）
  - `wanneer er een beetje sneeuw begint te vallen` 408.7px → 2 行
  - 对照：`vieren met geklap` 157.9px / `de dag dat de verkoop begint` 257.8px → 各 1 行
- 结论：D1 属实，nl 独有 fan-out 溢出（词框高模板固定，不改高，缩短释义）。

### D2/D3 — P8 注文罗马字拼错

- 复校证据已引公开来源（スポーツ報知/日刊スポーツ：藤凌駕 ふじりょうが；美ノ海 ちゅらのうみ）；同家庭 ja-fr fix1 亦独立核查 ozumo.jp / sumo-guide.com / 日刊体育，结论一致。本轮不再重复查来源，直接核对盘上残留。
- 修前全版 grep（occurrence 计数）：`Fujiryūga` — content34.py ×3、content7.py ×1、content8.py ×1、text.md ×5、svg/p8 ×5；`Umi-no-umi` — content34.py ×1、text.md ×1、svg/p8 ×1。与复校清单一致，无多无少。
- 注文位置：content34.py:188（48）、:190（49）、:202（54）、:224（63）；content7.py:57（111）；content8.py:22（116）。答案键（第 3 参）全对，不动。
- key 47 注文 `Yoshinofuji versloeg Ōnosato op dag 1`（content34.py:186）罗马字正确，不动。core-ja KIT §3 旧拼写为上游来源，不动 core（红线）。

## 3. 修复动作

### D1 — 缩短两条荷兰语释义（只删冗词，保留原意；改前用构建库量尺验证单行）

| 词 | 改前（行数/宽度） | 改后（行数/宽度） |
|---|---|---|
| 熊手 | `een bamboe hark voor voorspoedige zaken`（2 行 / 380.1px） | `een bamboe hark voor voorspoed`（1 行 / 298.2px） |
| 小雪 | `wanneer er een beetje sneeuw begint te vallen`（2 行 / 408.7px） | `wanneer er een beetje sneeuw valt`（1 行 / 305.7px） |

- 熊手：`voorspoedige zaken`（兴旺的生意）→ `voorspoed`（兴旺），「竹耙求兴旺」原意不变；小雪：删 `begint te`，「开始下一点雪」→「下一点雪」，原意不变。
- 改动点（同一释义字符串在词条框与答案注中复用，为保持词条框与答案一致，同步缩短）：
  - `content12.py:222` 词条表「熊手」格；`:225` 词条表「小雪」格
  - `content12.py:255` ex 16 答案注 `熊手 = een bamboe hark voor voorspoed`
  - `content12.py:283` P2 配对练习答案注（keys 25–28）：`熊手 = … b` 与 `小雪 = … a`
  - `content8.py:85` P8 配对练习答案注（keys 141–144）：`熊手 = een bamboe hark voor voorspoed c`
- 有意不动：`Een geluksbrenger voor voorspoedige zaken`（P2 侧栏、ex 注、P7 金句译文）是另一条不同的荷兰语译法，不是词条框释义，不属 D1。

### D2 — `Fujiryūga` → `Fujiryōga`（5 处，只改注文字串，答案键不动）

| # | 文件:行 | key | 改前 | 改后 |
|---|---|---|---|---|
| 1 | `content34.py:190` | 49 | `Fujiryūga versloeg Hōshōryū op dag 3` | `Fujiryōga versloeg Hōshōryū op dag 3` |
| 2 | `content34.py:202` | 54 | `Kinboshi van Fujiryūga: 11e toernooi sinds debuut` | `Kinboshi van Fujiryōga: 11e toernooi sinds debuut` |
| 3 | `content34.py:224` | 63 | `Fujiryūga won een kinboshi op dag 3` | `Fujiryōga won een kinboshi op dag 3` |
| 4 | `content7.py:57` | 111 | `Kinboshi van Fujiryūga: 11e toernooi sinds debuut` | `Kinboshi van Fujiryōga: 11e toernooi sinds debuut` |
| 5 | `content8.py:22` | 116 | `Hōshōryū verloor op dag 3 van Fujiryūga` | `Hōshōryū verloor op dag 3 van Fujiryōga` |

### D3 — `Umi-no-umi` → `Chura-no-umi`（1 处）

| # | 文件:行 | key | 改前 | 改后 |
|---|---|---|---|---|
| 1 | `content34.py:188` | 48 | `Umi-no-umi verloor op dag 1 van Hōshōryū` | `Chura-no-umi verloor op dag 1 van Hōshōryū` |

### 改后源文件复核

- content*.py：`Fujiryūga` 0×、`Umi-no-umi` 0×；`Fujiryōga` ×5、`Chura-no-umi` ×1。
- 旧释义精确串 `een bamboe hark voor voorspoedige zaken` / `wanneer er een beetje sneeuw begint te vallen` 在 content*.py 中 0×；新释义 `een bamboe hark voor voorspoed` ×4、`wanneer er een beetje sneeuw valt` ×2。
- SVG / text.md 不手工改，由重渲染 + 重导出自动更新。

## 4. export 脚本重建（与 ja-en/ja-fr fix1 同样缺失）

- `export-textmd-nl.py` 在本 clone 中缺失（KIT §8/§9 引用它，但版目录内无此文件）。按 ja-en 版同名脚本改写重建于版目录内。
- 验证：先在修前 SVG 上跑，重建输出与修前 `2026-w47-ja-nl.text.md` **逐字节一致**（45,685 字节），再用于修后导出。验证用临时目录（`/tmp/nl-export-val`，symlink svg），未动原文件。

## 5. 重渲染与机械门

- 全量结果见本目录 `GATE-LOG.md`。摘要：run.py rc 0 零溢出；render.py rc 0；webpdf.py rc 0；export rc 0；freeze 8/8（仅 p2/p8 相对修前变化）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 仍恰为 [137, 138, 139, 140]；文字层 print/web 各 45,931 字节且字节一致；P8 最小字号 9.98pt（≥9.75）；U+2019 全扫 0；旧拼全版复扫 0；150 键与复校一轮 extract 逐键一致。
- text.md diff（修前副本 `text-prefixed.md`）：精确 12 行——词条框两行并一行 ×2、注 16/25/28/141 释义缩短 ×4、注 48/49/54/63/111/116 拼写 ×6；其余 0 差异。1379 → 1378 行，45,685 → 45,627 字节（−58 = 释义 −58 字节 + 罗马字 +2 字节 − 并行换行 2 字节，逐项对得上）。
- 目视：印刷 PDF 8 页自渲染（110 dpi）+ 网页 PDF 8 页；P2 词条区 200 dpi 放大——四格逐格目视，释义均单行完整在框内；P8 答案区 200 dpi 放大——6 处改动逐行清晰可读，47 Yoshinofuji 未动；P2/P8 全页已读，无溢出、无重叠、无压页脚。

## 6. KIT 更新

- `WEEKLY-KIT.md`：§7 增返修记录（text.md 1378 行）；§8 交付物字节/SHA 更新为修后值（修前值括号内保留），增“Fix round 1 gates”整节；§9 注明 export 脚本重建与验证；§11 增 F3（D1/D2/D3 全记录）。
- `EDITION-RECORD.md`：交付物表、门禁节、状态与待办同步为修后值。
- 新交付物：印刷 PDF 29,099,141 字节，SHA-256 `c8b82a8491a0d4c54a01214806cede29188e8f4bf6c81c6cf8a1b3bd5ceafa56`；网页 PDF 4,476,527 字节，SHA-256 `7a7f5fc96730e82ba8c6697a9accd10387d6aa84a731f81fe3083310df0f97b8`。
- 未做的事：第二轮全量复校（按任务书，协调员另派，不由本轮做）。
