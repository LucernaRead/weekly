# FIX-LOG — 2026-W47 ja-es 第一轮返修（D1 修补）

- 返修者：叶子（第一轮返修 builder；与 ja-es builder、ja 核心 builder、各轮复校员、第一轮复校员不同人）
- 日期：2026-11-11（UTC 约 07:00–08:00）
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-es/`（未入仓，工作树 untracked）
- 缺陷来源：`hidden_files/w47/scratch-proof-ja-es1/PROOF-NOTE.md` D1（第一轮复校，6 条 P8 答案注文）
- 记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-es-fix1/`

## 0. 开工硬门禁（双探针，双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → 成功（`da0c4eb8…`）
- `…/hidden_files/w47/scratch-ja-es-fix1/.probe` 真实写入成功
- 红线遵守：只改 `production/2026-w47/fanout-ja/2026-w47-ja-es/` 内必要文件；
  未改 core-ja、未碰 W43–W46、其他目标语家庭、tools/；未跑 insert.py、lint --write；
  未 git add/commit/push/reset/stash。

## 1. 动手前独立核实（公开来源，不只采信复校笔记）

| 人名 | 误拼 | 应为 | 核实来源（公开） |
|---|---|---|---|
| 美ノ海 義久 | Umi-no-umi | **Chura-no-umi**（ちゅらのうみ） | スポーツ報知 2026-10-27「美ノ海義久（ちゅらのうみ・よしひさ）」；デイリー 2026-10-27「美ノ海義久（ちゅらのうみ・よしひさ）」；ja.wikipedia「美ノ海 義久」；sumo-guide.com「美ノ海 義久（ちゅらのうみ よしひさ）」 |
| 藤凌駕 雅治 | Fujiryūga | **Fujiryōga**（ふじりょうが） | ozumo.jp「藤凌駕は『ふじりょうが まさはる』と読む」（引日本相撲協会公式 profile）；サンスポ 2026-11-10（初金星、初土俵から 11 場所 3 日目、歴代 7 位） |

- 题面汉字（美ノ海／藤凌駕）与键值（B/A/11/○）本身无误，复校结论属实；上述来源同时佐证正文事实无误
  （初日 豊昇龍○／美ノ海●、3 日目 藤凌駕金星、11 場所目）。

## 2. 全版排查（改前）

| 位置 | `Fujiryūga` | `Umi-no-umi` |
|---|---|---|
| py 源码 | 5（content34.py:190/202/224，content7.py:57，content8.py:22） | 1（content34.py:188） |
| `2026-w47-ja-es.text.md` | 5 | 1 |
| SVG 文本节点（去 base64 后计） | 5（仅 p8-tesuto.svg） | 1（仅 p8-tesuto.svg） |
| WEEKLY-KIT.md / EDITION-RECORD.md / ABSTRACT.txt | 0 | 0 |
| **合计** | **5** | **1** |

与复校称“全版共 `Fujiryūga` 5 处、`Umi-no-umi` 1 处”逐一核对一致，无遗漏、无别处残留。
6 处与 D1 的 6 条注文（keys 48/49/54/63/111/116）一一对应。

## 3. 改动清单（逐处）

只改 3 个源码文件的 6 个注文字符串；键值、题面汉字、其余文字一字未动。

| # | key | 文件:行 | 原文 | 改后 |
|---|---|---|---|---|
| 1 | 48 | content34.py:188 | `Umi-no-umi perdió contra Hōshōryū el día 1` | `Chura-no-umi perdió contra Hōshōryū el día 1` |
| 2 | 49 | content34.py:190 | `Fujiryūga venció a Hōshōryū el día 3` | `Fujiryōga venció a Hōshōryū el día 3` |
| 3 | 54 | content34.py:202 | `El kinboshi de Fujiryūga: 11.º torneo desde su debut` | `El kinboshi de Fujiryōga: 11.º torneo desde su debut` |
| 4 | 63 | content34.py:224 | `Fujiryūga ganó un kinboshi el día 3` | `Fujiryōga ganó un kinboshi el día 3` |
| 5 | 111 | content7.py:57 | `El kinboshi de Fujiryūga: 11.º torneo desde su debut` | `El kinboshi de Fujiryōga: 11.º torneo desde su debut` |
| 6 | 116 | content8.py:22 | `Hōshōryū perdió contra Fujiryūga el día 3` | `Hōshōryū perdió contra Fujiryōga el día 3` |

改后全版复扫：错拼 `Fujiryūga` / `Umi-no-umi` 在内容文件（py + SVG
文本节点 + text.md）中均为 **0**；正确拼写 `Fujiryōga` 5×、`Chura-no-umi` 1×。
（KIT §11 F4 与 EDITION-RECORD 的修复记录中引用旧拼写作为“改前值”，属记述性引用，
非内容残留——正文、注文、SVG、text.md 均已无错拼。）

## 4. 上游溯源（只报告，不改其他版）

- **core-ja KIT 带入**：`production/2026-w47/core-ja/WEEKLY-KIT.md` §3（L83–88）趋势来源叙述中
  同样两处误拼：`Umi-no-umi` 1×、`Fujiryūga` 4×（Day 1/2/3 战绩英文记录）。
  核心版注文本身为中文、无罗马字（复校注），但 KIT 英文叙述带错拼，极可能是 fan-out 各版抄错的源头。
  core-ja 不在本任务红线内，**未改**，请协调员定夺（是否在核心 KIT 更正 + 是否复查同家他版）。
- **同家拉丁版同错**（py 源码 + text.md 计数，2026-11-11 实测）：
  de/en/fr/it/nl/pt 六个版均为 `Fujiryūga` 5× + `Umi-no-umi` 1×，与 ja-es 改前完全相同；
  ko/ru/zh-tw 三个版为 0（注文只用汉字，无罗马字，不受影响）。
  全家无一版已用正确拼写（`Fujiryōga` / `Chura-no-umi` 改前全家 0×）。
- **共用罗马字表**：`hidden_files/w47/scratch-fanout-ja/` 内无任何 map-*.json / apply.py
  （与复校 O1 一致：机制文件缺失），未发现共用罗马字表文件；错拼只能来自各版注文串本身
  与核心 KIT 叙述，无单一上游表可修。

## 5. 重建与重验（结果摘要，详见 GATE-LOG.md）

- `tools/venv/bin/python run.py` 两轮（runA/runB），均 rc 0、FLOW OVERFLOW / HEAD TOO WIDE 0；
  registry 与改前一致（TOTAL 150；A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；范文 154 字）。
- Freeze：runA vs runB 8/8 SVG 字节相同；与改前比仅 `svg/p8-tesuto.svg` 变
  （cb2813a7… → 25b95108…），p1–p7 字节相同。
- `render.py` rc 0；`tools/webpdf.py` rc 0。
- text.md：按同一 6 处替换重导，并与新 SVG 文本节点逐行比对 1349/1349 完全一致。
- 机械门：occlusion 自检 OK、实跑 **0 flags**；p8 extract **150/150**；p8 compare **CLEAN**，
  keydiff 仍恰为 [137, 138, 139, 140]；print/web pdftotext **47,036 B 逐字节一致**；
  P8 最小字号 **9.975pt ≥ 9.75pt**（次档 10.35pt，未变）；U+2019 全扫 **0**。
- 150 键逐题复核：以复校员留下的改前副本（`scratch-proof-ja-es1/rebuild/`，p8 SVG hash
  cb2813a7… 与改前一致）为基准，新旧 P8 注文逐行 diff **仅此 6 行**，其余 144 条注文逐字相同；
  键值经 p8 compare 确认未变；并人工逐条核对 P8 全部注文人名（O8 补查）：
  Ōnosato、Hōshōryū、Yoshinofuji、Chura-no-umi、Fujiryōga、Miura Riku、Kihara Ryuichi、
  Miyajima、Shōsetsu、ryuuryuu、Chiikawa 及 Tori-no-ichi / Ni-no-tori / Ichi-no-tori /
  Asakusa / Arashiyama / Kioto / Monte Takao / Weathernews / Beaujolais Nouveau /
  Hanshin Umeda —— 全部正确，无其他人名错误。
- 8 版目视：P1–P8 逐版看图（P8 全版 + 答案区两栏高清裁图），无溢出、无重叠、无压页脚；
  P8 三栏答案流齐整，6 处修正行均在流内；P6 中栏留白为核心继承版式（复校 O7），非本次引入。
- KIT §8（新双 PDF 数字）+ §11（F4）与 EDITION-RECORD.md 已更新。

## 6. 交付物（新）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-JA-ES.pdf`（印刷） | 29,102,102 | `9947b70c00a378c912ad7cffd198fd19a234ca3d6a3598589f647c3eaff0fce7` |
| `Lucerna-VOL4-JA-ES-web.pdf`（网页） | 4,482,721 | `49665374de81dd2a2ee7dad1b91396b22b69b2e64f5a038d55f03b5246a99550` |
| `2026-w47-ja-es.text.md` | 46,684 | `81993361c31fad6ea4c9bf8fbc91aed068979d6a8542a756a9fa4063519168e6` |

改前（复校核对值）：印刷 29,102,097 / `0feb6113…eacb55`；网页 4,482,717 / `b274eac2…95380`；
text.md 46,682。双 PDF 均为 8 页，网页版 < 7 MB。

## 7. 待办（不由本轮做）

- 改后须另派**第二轮全量复校**（协调员派，不由返修者做）。
- 协调员裁定：core-ja KIT §3 误拼是否更正；de/en/fr/it/nl/pt 六版同错是否排期同修。
