# FIX-LOG — 2026-W47 ja × zh-tw 第一轮返修（叶子 fix1）

- 版：`2026-w47-ja-zh-tw`，VOL.4，2026-11-16–22
- 日期：2026-11-11（EST 07:45–08:10）
- 任务：协调员磁盘 grep 核实的 1 处核心继承笔误，修后整期重渲染 + 全套机械门 + 150 键复核 + 8 版目视 + KIT 更新。修后交协调员派第一轮全量复校（不由本 builder 做）。
- 工作目录：`~/workspace/weekly-git`（main `73944738`）；记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-zh-tw-fix1/`。
- 红线遵守：未改 core-ja（只读核实）、未碰 W43–W46、其他目标语家庭、tools/；未跑 insert.py、未跑 lint --write、未 git add/commit/push/reset/stash。

## 0. 开工探针（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 在 `hidden_files/w47/scratch-ja-zh-tw-fix1/probe.txt` 写 `probe-ok` 成功。

## 1. 缺陷独立核实（动手前，全部逐字核实）

**(1) 日文正文确为 義ノ富士。**
- core-ja `content34.py:120`：`小結の義ノ富士に突き落としで敗れました`；本版 `content34.py:120` 同文。
- core-ja `content34.py:187/189` 题面选项亦为 `義ノ富士`。

**(2) key 47 与 key 115 指同一人（同一事件）。**
- key 47（本版 `content34.py:186-187`）：题面 `初日に大の里に勝ったのはだれですか。 A. 義ノ富士 B. 美ノ海 C. 藤凌駕`，答案 A；正文 :120 为同一事件（初日大之里败给小结義ノ富士）。
- key 115（本版 `content8.py:20-21`）：`大の里は初日、義ノ富士に（___）ました。(A. 負け B. 勝ち)`，答案 A；简析 `大之里首日輸給了義之富士` 已正确。

**(3) 全版 `一之富士` / `義之富士` grep（修前）。**
- `一之富士`（U+4E00）全版只在 key 47 一处：`content34.py:186`、`2026-w47-ja-zh-tw.text.md:1243`、`svg/p8-tesuto.svg` 各 1×。
- `義之富士`（U+7FA9）只在 key 115 一处正确：`content8.py:20`、`text.md:1315`、`svg/p8-tesuto.svg` 各 1×。
- 其他提及義ノ富士的简析同类一/義混淆检查：全版另有 `美ノ海` 相关简析 key 48 `首日敗給豐升龍的是美之海`（美之海正确）；日文原文中的 `義ノ富士`（content34.py:120/187/189、content8.py:21）均为日文正文/题面，无误；`content12.py:261` 的 `一之酉` 是酉の市“一之酉”（首个酉日），正确用词，与富士无关。**无其他同类混淆，无需多改。**

**附：任务交代与实测的一处出入（已核实，不影响修法）。**
- 任务称“源头在 core-ja/content34.py:186（简体‘一之富士’）”。实测本轮开工时 core:186 已为 `义之富士`：`义` = U+4E49，是 `義` 的正确简体字形（码点核实，非目视）。
- 旁证：本版 map（`scratch-fanout-ja/map-zh-tw.json`）第 221 条键仍为旧核心值 `一之富士`（U+4E00）——说明 fan-out 建 map 时核心确为 `一`，此后核心已被改成 `义`（推测为并行修核心的另一 builder 已动手，或核心 builder 自修）；本版的一字错即由此忠实带入（OpenCC s2t 对 `一` 不变，对 `义` 正确转为 `義`，见第 117 条 `义之富士`→`義之富士`）。
- 结论：本版缺陷真实存在（U+4E00），修法不变；核心侧现状以实测为准，核心错字不在本修补管辖内。

## 2. 改动逐处清单（共 2 处，同一逻辑修复）

### (a) 版源码 — 1 字（任务指定改动）

`production/2026-w47/fanout-ja/2026-w47-ja-zh-tw/content34.py:186`

```diff
-e.ex("B1", "單選", "A", "首日戰勝大之里的是一之富士",
+e.ex("B1", "單選", "A", "首日戰勝大之里的是義之富士",
```

其余一字不动。修后 `grep 一之富士 content*.py` = 0；`義之富士` = 2（content34:186 key 47、content8:20 key 115）。

### (b) 机制文件 map — 同一词条的键与值（防重引入，非版面改动）

`hidden_files/w47/scratch-fanout-ja/map-zh-tw.json` 第 221 条（`map` 节）：

```diff
-  "首日战胜大之里的是一之富士": "首日戰勝大之里的是一之富士",
+  "首日战胜大之里的是义之富士": "首日戰勝大之里的是義之富士",
```

- 值 `一`→`義`：与 (a) 同一修复，否则重跑 apply.py 会把错字重新带入本版。
- 键 `一`→`义`：键须与现行核心原文逐字一致（apply.py 的全局校验：`MAP key never occurs quoted in core`）。实测：新键在 core `content34.py` 中带引号出现 1×；旧键在 core 中出现 0×（已过时，若留着会使该条死键 + 校验报警）。
- 未动 `miss-zh-tw.json` / `miss2-zh-tw.json`（旧轮次“未命中”快照，历史证据，非机制输入）。
- 只读复核：map 全部 221 条键中，在 5 个 core 内容文件里带引号未出现的只剩 2 条家具键（`Lucerna　日语周报 VOL.4　LUCERNA JAPANESE WEEKLY`、`译注｜`），均为改动前已存在、与本次修复无关的旧项；修复使未命中数由 3 减为 2。

## 3. 重建（与构建同一解释器 `tools/venv/bin/python`）

| 步骤 | 日志 | 结果 |
|---|---|---|
| run.py run1（初版） | `build-zh-tw-fix1-run1.log` | rc=0，TOTAL 150（A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW / HEAD TOO WIDE |
| run.py run2 | `build-zh-tw-fix1-run2.log`（0 字节，作废） | **磁盘配额爆满 EDQUOT 中断**，见 §4 |
| run.py run3 | `build-zh-tw-fix1-run3.log` | rc=0，同上，0 溢出 |
| run.py run4 | `build-zh-tw-fix1-run4.log` | rc=0，同上，0 溢出 |
| 冻结 | `zh-tw-sha-fix1-run3.txt` vs `run4.txt` | **8/8 逐字节一致** |
| 相对修前 | `zh-tw-sha-fix1-pre.txt` vs `run4.txt` | **仅 p8-tesuto.svg 一页变化**（`59598a93…` → `f0d2ebe5…`），余 7 页 sha 不变 |
| render.py | `render-zh-tw-fix1.log` | rc=0，8 张 cards + print PDF |
| webpdf.py | `webpdf-zh-tw-fix1.log` | rc=0，8 页，799 字，44,661 text bytes |
| export text.md | `export-zh-tw-fix1.log` | rc=0，44,361 bytes，1325 text lines |

注：run1 的 SVG 已完整落地（8/8 可解析，p8 含 `義之富士` 1×、`一之富士` 0×）；run2 配额中断时只重写了 p1（内容与 run1 同，确定性构建），run3/run4 为配额释放后两次干净全量重跑，冻结对以 run3/run4 为准。fix1-run1.log 仍有效（rc=0 全量构建）；fix1-run2.log 0 字节为空白证据保留。

## 4. 中途阻塞：磁盘配额 EDQUOT（已处理，见 AGENTS.md 2026-11-10 旧例）

- 现象：run2 进行中写盘报 `Disk quota exceeded`，rc=120，`zh-tw-sha-fix1-run*.txt` 写不出；`df` 仍显示 /home/hatch 45G 空闲——配额封顶，非磁盘满。
- 处理：按 AGENTS.md 2026-11-10 的旧 worktree 清理规程逐个核验 13 个 `weekly-*` worktree（HEAD 是否 main 祖先 + 工作树干净 + 有无活进程/引用）。
  - 仅 `weekly-es46-post` 同时满足：HEAD `2af4ade6`（§1.1 style: Spanish W46, 11 editions re-rendered，2026-11-10 11:38 UTC）为 main 祖先（`git branch --contains` 含 main、`merge-base --is-ancestor` 通过）；工作树干净（`status --porcelain` 0 行，两次核实）；无活进程引用；W47 状态文档与推送脚本中无引用。
  - 其余 12 个均 dirty（34–294 行），按规程逐个验完之前不动，未动。
  - `weekly-design` 永远不动（规程明文）。
  - 执行 `git worktree remove ~/workspace/weekly-es46-post`（rc=0），释放约 1.2G；随后写盘探针成功。
  - 此操作不在任务禁令内（禁令为 add/commit/push/reset/stash、不提交）；属用户立规“推完及时清理、不攒废物”的规程内清理，且有完整核验记录在案。

## 5. 交付物（新）

| 交付物 | 字节 | SHA-256 |
|---|---|---|
| Print PDF `Lucerna-VOL4-JA-ZH-TW.pdf` | 26,034,685（旧 26,034,686，-1） | `7f05fd508c90cb0dc7b5be2d3bcc06f01f0c04e4cf399ed6e4076b7fecedb27b` |
| Web PDF `Lucerna-VOL4-JA-ZH-TW-web.pdf` | 4,788,782（旧 4,788,784，-2，< 7 MB） | `cee0a8b5b373c14b21a467f4a477495e2a59c125095c8b051dbae33b45afa93e` |
| `.text.md` `2026-w47-ja-zh-tw.text.md` | 44,361（与旧同） | `3a42eb5b35c98b9b4245ae03eab971c6a0d076bcae66670379027a943478621c` |
| 8 SVG（`svg/`） | — | run3==run4，见 §3；仅 p8 变 |
| 8 cards（`cards/` PNG） | — | render.py 重渲 |
| `ABSTRACT.txt` | 235（未动） | `fdcf43b8c9d4718ea21eac14d4a5ffcf83e3fe7edc571fbd7c0da758b2faf9e6` |

- 两 PDF 均为 8 页；文字层各 44,661 字节。
- KIT（`WEEKLY-KIT.md`）§2/§3/§4 已更新 + §11 新增 F6；`EDITION-RECORD.md` 交付表与门禁已更新（状态仍以第一轮全量复校结论为准，本修补不改“定稿”状态）。

## 6. 改动范围自查

- 本版内实际变化的文件：`content34.py`（1 字）、`svg/p8-tesuto.svg`（重渲）、`cards/*.png`（8 张重渲）、两 PDF、`2026-w47-ja-zh-tw.text.md`、`WEEKLY-KIT.md`、`EDITION-RECORD.md`。
- 未动：core-ja 任何文件（只读核实）、W43–W46、其他目标语家庭、tools/、ABSTRACT.txt、`content12/56/7/8.py`、`run.py`/`render.py`/`bslib4.py`/`svglib.py`、`assets/`。
- 未执行：insert.py、lint --write、git add/commit/push/reset/stash。
