# FIX-LOG — 2026-W47 ja-fr 第一轮返修（D1/D2 罗马字）

- 返修 builder：叶子（第一轮返修；与 ja-fr builder、ja 核心 builder、各轮复校员、第一轮复校员不同的人）
- 日期：2026-11-11
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-fr/`（clone main）
- 缺陷：P8 答案注释中力士名罗马字拼错，答案键本身全对。D1：`Fujiryūga` → `Fujiryōga`（keys 49、54、63、111、116）；D2：`Umi-no-umi` → `Chura-no-umi`（key 48）。
- 记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-fr-fix1/`（绝对路径，不写进仓内 hidden_files）。
- 红线遵守：未改 core-ja、未碰 W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write、未 git add/commit/push/reset/stash。

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-fr-fix1/probe.txt` 写盘成功。
- 构建解释器：`tools/venv/bin/python`（SOP/AGENTS 规定；与第一轮复校同一解释器）。

## 1. 独立核实（动手前，查公开来源，不只采信复校笔记）

### D1 — 藤凌駕 = ふじりょうが → Fujiryōga（不是 Fujiryūga）

- ozumo.jp（引日本相扑协会官方 profile）：「藤凌駕雅治（ふじりょうが まさはる）」；「藤凌駕は『ふじりょうが まさはる』と読み」。
- sumo-guide.com 力士名鑑：「藤凌駕 雅治（ふじりょうが まさはる）」。
- ja.wikipedia「藤凌駕雅治」：「藤凌駕 雅治（ふじりょうが まさはる、2003年2月27日 - ）」。
- 日刊体育 2026-11-10（九州场所 3 日目）：藤凌駕 3 日目胜豊昇龍、初金星、初土俵から 11 场所 3 日目、年 6 场所制 7 位速度——与本版注文事实一致。
- 结论：凌駕读 `ryōga`（りょうが，长音 ō），不是 `ryūga`（りゅうが）。D1 应改成立。

### D2 — 美ノ海 = ちゅらのうみ → Chura-no-umi（不是 Umi-no-umi）

- sumo-guide.com 力士名鑑：「美ノ海 義久（ちゅらのうみ よしひさ）」。
- デイリースポーツ 2026-10-27：「美ノ海義久（ちゅらのうみ・よしひさ）」。
- rokepan：「美ノ海義久（ちゅらのうみ よしひさ）」；dメニュースポーツ力士情報：「ちゅらのうみ」。
- 结论：美读 `chura`（ちゅら，冲绳语「美」），从不读 `umi`；`Umi-no-umi` 对应的是「海ノ海」。D2 应改成立。法文版按复校给定形式 `Chura-no-umi`（与 es/pt 姊妹版一致；en 用 `Churanōmi`、de 用 `Churanoumi`，各版按自家惯例）。

## 2. 全版 grep：残留与上游溯源（修前状态）

### 2.1 本版（fr）残留——与复校清单一致，无多无少

| 文件 | 命中 |
|---|---|
| `content34.py`（P4 练习源） | L188 key 48 `Umi-no-umi …`；L190 key 49、L202 key 54、L224 key 63 `Fujiryūga …`（共 4 处） |
| `content7.py`（P7 练习源） | L57 key 111 `Kinboshi de Fujiryūga …`（1 处） |
| `content8.py`（P8 练习源） | L22 key 116 `Hōshōryū a perdu contre Fujiryūga …`（1 处） |
| `svg/p8-tesuto.svg`（生成物） | `Fujiryūga` ×5、`Umi-no-umi` ×1（重渲染后自动更新，不手工改） |
| `2026-w47-ja-fr.text.md`（导出物） | 6 行（L1264、1265、1270、1279、1333、1339；重导出后自动更新，不手工改） |
| `WEEKLY-KIT.md` | 0× |
| 日文题干（各 `e.ex` 第 5 参） | 藤凌駕／美ノ海均为汉字，正确，不动 |

注：答案注释是 `e.ex(...)` 的第 4 个参数（note）；答案键（第 3 参：B/A/11/○/A）全对，不动。P7 正文段（content7.py L51 「藤凌駕は、3日目に金星をあげました。」）为冻结日文，不动。

### 2.2 上游溯源——共用罗马字表在核心 KIT

- 位置：`production/2026-w47/core-ja/WEEKLY-KIT.md` §3 趋势来源注（英文 day 1–3 战绩摘要），L83–88：
  - L83 `Hōshōryū beat Umi-no-umi (oshidashi)`（×1）
  - L84 `Kotosakura lost to Fujiryūga`（×1）、L85 `Ōnosato beat Fujiryūga`（×1）、L87 `Hōshōryū lost to Fujiryūga`（×1）、L88 `Fujiryūga's first kinboshi`（×1）
- core-ja 的 `content*.py` 里无任何罗马字（日文核心只用汉字）；错误罗马字只存在于核心 KIT 的英文注里，fan-out 各版翻译时沿用。**核心 KIT 本身不在本次返修范围（红线：绝不改 core-ja），只报告，不改。**
- 无独立的共用罗马字表文件：全仓未找到 `map-fr.json` / `apply.py`（与第一轮复校 O6/O12 观察一致）；fan-out 机制文件缺失，content*.py 即本版唯一事实来源。

### 2.3 姊妹版受影响情况（只报告，未改任何一版；2026-11-11 07:35 UTC 实测， sibling fix 轮进行中，状态在变）

| 版 | content*.py 源 | svg/p8 | .text.md |
|---|---|---|---|
| ja-en | 已修正（07:30 UTC 改动，`Fujiryōga` / `Churanōmi`） | 0 处残留（已重渲染） | 仍 6 行旧拼写（待重导出） |
| ja-es | 已修正（07:29 UTC，`Fujiryōga` / `Chura-no-umi`） | 0 处残留（已重渲染） | 仍 6 行旧拼写（待重导出） |
| ja-pt | 已修正（07:31 UTC，`Fujiryōga` / `Chura-no-umi`） | 0 处残留（已重渲染） | 仍 6 行旧拼写（待重导出） |
| ja-de | 已修正（07:29 UTC，`Fujiryōga` / `Churanoumi`） | 0 处残留（已重渲染） | 仍 6 行旧拼写（待重导出） |
| ja-it | 仍错（5× `Fujiryūga` + 1× `Umi-no-umi`，源未动） | 仍有残留 | 6 行旧拼写 |
| ja-nl | 仍错（5× `Fujiryūga` + 1× `Umi-no-umi`，源未动） | 仍有残留 | 6 行旧拼写 |
| ja-ko / ja-ru / ja-zh-tw | 无命中（各自转写惯例不同） | — | — |

- 另：ja-it WEEKLY-KIT.md L168、ja-pt WEEKLY-KIT.md L170 引用了旧拼写（修记引文），各版自理。
- de/en/es/pt 四版的源已由并行 fix 轮在本次返修开工后（07:29–07:31 UTC）修正，其 SVG 已重渲染、text.md 待重导出；it/nl 尚未动手。

## 3. 修复动作（源文件 6 处，只改 note 字符串）

| # | 文件:行 | key | 改前 | 改后 |
|---|---|---|---|---|
| 1 | `content34.py:188` | 48 | `Umi-no-umi a perdu contre Hōshōryū le jour 1` | `Chura-no-umi a perdu contre Hōshōryū le jour 1` |
| 2 | `content34.py:190` | 49 | `Fujiryūga a battu Hōshōryū au jour 3` | `Fujiryōga a battu Hōshōryū au jour 3` |
| 3 | `content34.py:202` | 54 | `Kinboshi de Fujiryūga : 11e tournoi depuis le début` | `Kinboshi de Fujiryōga : 11e tournoi depuis le début` |
| 4 | `content34.py:224` | 63 | `Fujiryūga a gagné un kinboshi au jour 3` | `Fujiryōga a gagné un kinboshi au jour 3` |
| 5 | `content7.py:57` | 111 | `Kinboshi de Fujiryūga : 11e tournoi depuis le début` | `Kinboshi de Fujiryōga : 11e tournoi depuis le début` |
| 6 | `content8.py:22` | 116 | `Hōshōryū a perdu contre Fujiryūga au jour 3` | `Hōshōryū a perdu contre Fujiryōga au jour 3` |

- 只改 `e.ex(...)` 第 4 参（note）；答案键（第 3 参）与日文题干（第 5 参）未动。
- 改后复核：`content*.py` 中 `Fujiryūga` / `Umi-no-umi` 0×；`Fujiryōga` ×5、`Chura-no-umi` ×1。
- 另：`export-textmd-fr.py` 缺失（第一轮复校 O6），已按 SVG 文本导出法重建于本版目录内；先在修前 SVG 上验证重建脚本输出与修前 `2026-w47-ja-fr.text.md` **字节一致**（1350 行、46,880 字节），再用于修后导出。`WEEKLY-KIT.md` §9 已注明重建事由。

## 4. 重渲染与机械门

- 全量结果见本目录 `GATE-LOG.md`。摘要：run.py rc 0 零溢出；render.py rc 0；webpdf.py rc 0；export rc 0；freeze 8/8；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 仍恰为 [137, 138, 139, 140]；文字层 print/web 各 47,210 字节且字节一致；P8 最小字号 9.98pt（≥9.75）；U+2019 全扫 0；150 键逐题复核——键值与第一轮复校 extract 0 差异，仅 6 条注文不同；8 版目视 + 网页 P1/P8 全读，P8 答案区放大核实 6 处。
- 仅 `p8-tesuto.svg` 相对修前变化；p1–p7 SVG 与修前字节一致（注文只画在 P8，P4/P7 练习页本身不印注文）。text.md 46,880 → 46,882 字节（diff 精确为 6 行）。

## 5. KIT 更新

- `WEEKLY-KIT.md`：§7 增返修记录；§8 交付物字节/SHA 更新为修后值（修前值括号内保留），增“Fix round 1 gates”整节；§9 注明 export 脚本重建；§11 增 F4。
- `EDITION-RECORD.md`：交付物表、门禁节、状态与待办同步为修后值。
- 新交付物：印刷 PDF 28,348,000 字节，SHA-256 `1f3b28f4eae5b23c57bf6dac67b976d8e167efd09825ebdcdc10fa9bb9f2fdcb`；网页 PDF 4,458,587 字节，SHA-256 `4f02e8c8f9dec50844906ec8c43e0e13520aa98897a49a14685468c6f6dd2b8b`。
- 未做的事：第二轮全量复校（按任务书，协调员另派，不由本轮做）。
