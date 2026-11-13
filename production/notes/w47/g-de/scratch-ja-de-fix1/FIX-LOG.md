# FIX-LOG — 2026-W47 ja-de 第一轮返修（D1/D2/D3）

- 返修 builder：叶子（第一轮，与 ja-de builder / core-ja builder / 各轮复校员不同人）
- 日期：2026-11-11（EST 02:27 开工）
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-de/`（未入仓，未追踪）
- 依据：SOP.md §8、§1.1；AGENTS.md；KIT；第一轮复校 PROOF-NOTE.md
  （`hidden_files/w47/scratch-proof-ja-de1/PROOF-NOTE.md`）
- 结论：**3 条缺陷全部修完，整期重渲染，全套机械门全绿，8 版目视通过。
  待第二轮全量复校（协调员另派）。**

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `da0c4eb8d9a48d171a33574b380752e183286751`，RC=0。
- `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-de-fix1/.probe`
  真实写盘成功。
- 身份复核：旧印刷 PDF 29,102,629 字节 /
  `b5d66e17d9ac29b6362d934e65a254a1bb63df5ea00ed305ce1b362cea06a239`；
  旧网页 PDF 4,483,732 字节 /
  `c55dd68cfcd6f0acc4cad79987a7ceb7fbe4c86d83cdf637c86c795497aff26a`——
  与任务给定一致。旧 SVG sha256 与复校 GATE-LOG §3 记录的 8 个值逐个一致。

## 1. 动手前独立核实（公开来源，不只采信复校笔记）

### D1 — 藤凌駕 `Fujiryūga` → `Fujiryōga` ✓ 核实成立

- Wikipedia（en）`Fujiryōga Masaharu`：shikona **Fujiryōga**（藤凌駕），
  combining … "the name Ryōga (凌駕）"。凌駕读 りょうが（ryōga），不是 りゅうが。
  来源：https://en.wikipedia.org/wiki/Fujiry%C5%8Dga_Masaharu
- 日文正文（core 冻结）只写汉字 藤凌駕，未给读音；罗马字是 fan-out 层自加的。

### D2 — 美ノ海 `Umi-no-umi` → `Churanoumi` ✓ 核实成立

- 日刊スポーツ：改名しこ名「美ノ海（ちゅらのうみ）」；「美ノ海義久
  （ちゅらのうみ・よしひさ）」。来源：
  https://www.nikkansports.com/battle/sumo/news/201805300000522.html
- `Umi-no-umi` 是对汉字字面的误读（美=umi、之=no、海=umi）；正文写的是
  美ノ海，读 ちゅらのうみ。德文版按复校给定的 `Churanoumi` 形式。

### D3 — `Das Verb im ます-Form beenden.` → `Das Verb in der ます-Form beenden.` ✓ 核实成立

- `Form` 为阴性（die Form）；第三格阴性为 der → `in der Form`。
  `im` = `in dem`，只配阳/中性。属格/与格词尾规则见 Duden Lernhelfer
  「Genus des Substantivs」：https://www.lernhelfer.de/schuelerlexikon/deutsch/artikel/genus-des-substantivs
- 全版其余 `im` 用法（`im November` / `im September` /
  `im Fukuoka Kokusai Center`）均为阳/中性，正确，未动。

## 2. 全版 grep（修前）：残留分布

修前本版内残留（SVG + .text.md + content*.py + KIT）：

| 串 | svg/p8 | svg/p7 | content34.py | content7.py | content8.py | text.md | KIT |
|---|---|---|---|---|---|---|---|
| `Fujiryūga`（含属格 `Fujiryūgas`） | 5 | 0 | 3 | 1 | 1 | 5 | 0 |
| `Umi-no-umi` | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
| `im ます-Form` | 0 | 1 | 0 | 1 | 0 | 1 | 0 |

- 5 处 `Fujiryūga` 系 = P8 keys 49（content34.py:190）、54（content34.py:202）、
  63（content34.py:224）、111（content7.py:57）、116（content8.py:22）；
  `Umi-no-umi` = key 48（content34.py:188）；`im ます-Form` = P7 诊所第 4 条
  （content7.py:69）。注：content34/7.py 里的注字符串只印在 P8 答案区，
  不印在 P3/P4/P7 正面——新旧 SVG 文本 diff 证实只有 p7/p8 变化。
- `map-de.json` / `apply.py` / `export-textmd-de.py` 在本 clone 中不存在
  （复校 O5 已记；`scratch-fanout-ja/` 只有门禁日志与 gate JSON，无 map）。
  故修复直接落在构建源码 content*.py 上；若 map 日后恢复，须把 7 处写回 map
  （见 KIT §9 NOTE 与 §11 F4），否则 fresh apply 会丢修复。

## 3. 改动清单（7 处源码字符串 + text.md 同步 7 行）

| # | 缺陷 | 文件:行 | 原文 | 改后 |
|---|---|---|---|---|
| 1 | D2 | content34.py:188 | `Umi-no-umi verlor an Tag 1 gegen Hōshōryū` | `Churanoumi verlor an Tag 1 gegen Hōshōryū`（key 48） |
| 2 | D1 | content34.py:190 | `Fujiryūga schlug Hōshōryū an Tag 3` | `Fujiryōga schlug Hōshōryū an Tag 3`（key 49） |
| 3 | D1 | content34.py:202 | `Fujiryūgas kinboshi: 11. Turnier seit dem Debüt` | `Fujiryōgas kinboshi: 11. Turnier seit dem Debüt`（key 54） |
| 4 | D1 | content34.py:224 | `Fujiryūga holte an Tag 3 einen kinboshi` | `Fujiryōga holte an Tag 3 einen kinboshi`（key 63） |
| 5 | D1 | content7.py:57 | `Fujiryūgas kinboshi: 11. Turnier seit dem Debüt` | `Fujiryōgas kinboshi: 11. Turnier seit dem Debüt`（key 111） |
| 6 | D3 | content7.py:69 | `Das Verb im ます-Form beenden.` | `Das Verb in der ます-Form beenden.`（P7 诊所 #4） |
| 7 | D1 | content8.py:22 | `Hōshōryū verlor an Tag 3 gegen Fujiryūga` | `Hōshōryū verlor an Tag 3 gegen Fujiryōga`（key 116） |

- text.md：同一 7 行 surgical 替换（diff 验证：仅 7 行变化，无其他行触动；
  字节 46,516 → 46,520，+4 = D3 `im`→`in der` 的 4 字符；其余替换等长）。
- KIT（§7 几何备注、§8a 新增返修门禁节、§9 map 缺失 NOTE、§11 F4）与
  EDITION-RECORD.md（交付物表 + 门禁节 + 状态）同步更新。
- 未改动：core-ja、W43–W46、其他目标语家庭、tools/；未跑 insert.py、
  lint --write；未 git add/commit/push/reset/stash。

## 4. 跨版残留（只报告，未修——红线）

无共用罗马字表：`tools/` 与 `production/2026-w47/` 内搜 `romaji|ROMAJI`，
只命中各版 KIT 行文，无共享表。core-ja 内容文件只用汉字（藤凌駕/美ノ海），
罗马字串是各 fan-out 版 content 文件自带的副本——每版须各自修。

最新快照（2026-11-11 约 02:45 EST 定向 grep；注意：两次 grep 之间
en/es/fr/pt 的残留数在变，疑似并行返修进行中，数字以快照时间为准）：

| 版 | `Fujiryūga` 残留 | `Umi-no-umi` 残留 |
|---|---|---|
| W47 ja-it | svg p8 ×5、text.md ×5、content34.py ×3、content7.py ×1、content8.py ×1、KIT ×1 | svg p8 ×1、content34.py ×1、text.md ×1 |
| W47 ja-nl | svg p8 ×5、text.md ×5、content34.py ×3、content7.py ×1、content8.py ×1 | svg p8 ×1、content34.py ×1、text.md ×1 |
| W47 ja-fr | text.md ×5 | text.md ×1 |
| W47 ja-pt | WEEKLY-KIT.md ×1 | — |
| W47 ja-en / ja-es | 本次快照 0（约 02:30 的全仓 grep 曾见 en svg p8 + text.md、es text.md 有残留，两次 grep 之间已清零） | — |
| W47 ja-ko / ja-ru / ja-zh-tw | 0 | 0 |
| W47 core-ja | WEEKLY-KIT.md 行文 ×5（内容文件无罗马字） | — |
| W46 全家（已刊周） | 0（无 `Fujiryūga`） | ja-de/en/es/fr/it/nl/pt 各 text.md + content34.py + freeze json + transform.py；issues/2026-w46 七版 text.md 亦有；core-ja KIT + fix-round3  artifacts 亦有 |

另：早约 02:30 的全仓 grep 还在 proof scratch 副本（各版 rerun/freeze 副本、
`scratch-fanout-ja/*-print.txt|*-web.txt` 的 pdftotext 提取文本）中见到两串——
皆为历史构建的副本/提取物，非现行源码，不计入上表。

## 5. O1（core 侧观察，不修 core、不扩范围）

复校 O1：core P8 key 47 中文简析疑为 core 笔误（"一之富士"）。
本轮实测：该串**确实存在于 core-ja**（协调员称 grep 未找到，系目录名误会——
core 目录是 `core-ja`，不是 `core-zh-cn`）：
`core-ja/content34.py:186`：`e.ex("B1", "单选", "A", "首日战胜大之里的是一之富士", …)`；
`core-ja/2026-w47-ja-zh-cn.text.md:1247`：`47. A — 首日战胜大之里的是一之富士`；
core-ja `svg/p8-tesuto.svg` 亦含该串。de 版两处均正确译为 `Yoshinofuji`，
fan-out 处理无误。core 是否改、怎么改，属 core 侧决定，本轮未动 core 一字。

## 6. 重渲染与门禁（摘要，详见 GATE-LOG.md）

- `run.py` ×2（tools/venv，Pillow 13.0.0）：均 exit 0，零溢出；freeze 8/8。
- `render.py` exit 0；`webpdf.py` exit 0（web 4,483,728 B，46,838 text bytes）。
- occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 仍恰为
  [137, 138, 139, 140]；150 键逐题复核：仅 6 条简析变，键值零差异。
- print/web 文字层 pdftotext 各 105,192 B，逐字节一致。
- P8 最小字号 9.98pt（≥9.75pt）；U+2019 全扫 0；§1.1 grep 全绿。
- 8 版目视（新印刷 PDF 100 dpi）：全部干净；P7 诊所栏与 P8 答案区放大确认。
- 新双 PDF：印刷 29,102,625 B /
  `2047035bdaa9f9ba82d4f2a6d2b5d7c4461e1442070ed5abacbe86d930001f39`；
  网页 4,483,728 B /
  `8db59bf122c73d895e9fe0d58da7e9f283f11ed1e76bc45aeb2be9a268a98f26`。
