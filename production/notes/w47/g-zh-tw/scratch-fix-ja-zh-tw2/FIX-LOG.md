# FIX-LOG — 2026-W47 ja × zh-tw 第二轮返修（叶子 fix2）

- 版：`2026-w47-ja-zh-tw`，VOL.4，2026-11-16–22
- 日期：2026-11-11（EST 08:36–09:05）
- 任务：proof1 (b) 发现的 1 类 2 处同类字形缺陷（D1/D2，日文注文 headword 被 OpenCC s2t 误转繁体），修后整期重渲染 + 全套机械门 + 150 键复核 + 8 版目视 + KIT 更新。修后交协调员派第二轮全量复校（proof2，不由本 builder 做）。
- 工作目录：`~/workspace/weekly-git`；记录目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja-zh-tw2/`。
- 红线遵守：未改 core-ja（只读核实）、未碰 W43–W46、其他目标语家庭、tools/、issues/；未跑 insert.py、未跑 lint --write、未 git add/commit/push/reset/stash。未动 proof1 观察项 O1（`三浦璃來`，非缺陷、超出本轮范围）。

## 0. 开工探针与成品身份核实（动手前，逐字核实）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `0d7da5d313a95dd054eb41a2ba74ab99a19726a5`，成功。
- 在 `hidden_files/w47/scratch-fix-ja-zh-tw2/probe.txt` 写 `probe-ok` 成功。
- `df` 显示 /home/hatch 45G 可用。
- 三份修前成品实测，与任务给定值逐字节一致：

  | 交付物 | 字节 | SHA-256 |
  |---|---|---|
  | Print PDF `Lucerna-VOL4-JA-ZH-TW.pdf` | 26,034,685 | `7f05fd508c90cb0dc7b5be2d3bcc06f01f0c04e4cf399ed6e4076b7fecedb27b` |
  | Web PDF `Lucerna-VOL4-JA-ZH-TW-web.pdf` | 4,788,782 | `cee0a8b5b373c14b21a467f4a477495e2a59c125095c8b051dbae33b45afa93e` |
  | `.text.md` `2026-w47-ja-zh-tw.text.md` | 44,361 | `3a42eb5b35c98b9b4245ae03eab971c6a0d076bcae66670379027a943478621c` |

- 任务指明的 brief 路径 `~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md` 盘上不存在；实际读的是 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`（已读全文）。SOP.md §8 与 §1.1 全文、`AGENTS.md`、proof1 的 PROOF-NOTE.md / GATE-LOG.md、fix1 的 FIX-LOG.md / GATE-LOG.md 均已读。

## 1. 缺陷独立核实（动手前，全部逐字核实）

### D1（P3 注文 `出來栄え` → `出来栄え`）

- 本版 `content34.py:20`：`f.gloss("収穫 收穫　解禁日 解禁日　出來栄え 今年的品質　味覚 味覺。")`。
- 本版正文 `content34.py:19`：`今年の出来栄えを確かめながら…`（`来` U+6765，日文新字体）；core-ja `content34.py:20` 注文：`出来栄え 今年的品质`（headword 日文原形）。
- map 词条（`scratch-fanout-ja/map-zh-tw.json`，221 条）：键 `…出来栄え 今年的品质…` → 值 `…出來栄え 今年的品質…`（s2t 直出，FIX 表未修）。
- 修前全版 `出來栄え` 整词仅 content34.py 1×；text.md:323–324 该词被行折断（行尾 `出來栄` + 次行 `え 今年的品質`），整词 grep 会漏——已用分行 sed 核实。
- P3 SVG 节点 `svg/p3-bunka.svg`：`譯註｜収穫 收穫　解禁日 解禁日　出來栄`（续行 `え 今年的品質…`）。

### D2（P4 注文 `波亂` → `波乱`）

- 本版 `content34.py:124`：`f.gloss("波亂 出乎意料　ねらう 瞄準　金星 打敗橫綱的勝利　初土俵 首次登場。")`。
- 本版正文 `content34.py:120/122`：`初日は、波乱でした。` / `3日目は、また波乱でした。`（`乱` U+4E71）；core-ja `content34.py:124` 注文：`波乱 出乎意料…`。
- map 词条：键 `波乱 出乎意料…` → 值 `波亂 出乎意料…`（s2t 直出，FIX 表未修）。
- 修前 P4 SVG 内 `波乱` 3×（标题 1 + 正文 2）与 `波亂` 1×（注文）并存，同一版内同一词两种写法；text.md:468 为 `譯註｜波亂 出乎意料…`。

### 同类排查

- 修前 `出來栄え` / `波亂` 在 content*.py 各 1×、map 各 1×，别处无第三处（text.md/SVG 内的出现即上述两处注文的渲染件）。
- 两词条的 map **键**均与现行核心逐字一致（python 核实：带引号出现于 core-ja 内容文件），故本次只改**值**，键不动（与 fix1 不同：fix1 时核心已由 `一` 改成 `义`，键须跟改；本次核心未动）。

## 2. 改动逐处清单（共 4 处，两处逻辑修复 × 源码+机制文件）

### (a) 版源码 — 2 字

`production/2026-w47/fanout-ja/2026-w47-ja-zh-tw/content34.py`

```diff
- f.gloss("収穫 收穫　解禁日 解禁日　出來栄え 今年的品質　味覚 味覺。")   # :20
+ f.gloss("収穫 收穫　解禁日 解禁日　出来栄え 今年的品質　味覚 味覺。")   # :20
- f.gloss("波亂 出乎意料　ねらう 瞄準　金星 打敗橫綱的勝利　初土俵 首次登場。")  # :124
+ f.gloss("波乱 出乎意料　ねらう 瞄準　金星 打敗橫綱的勝利　初土俵 首次登場。")  # :124
```

仅 headword 各一字；释义（`今年的品質` / `出乎意料…`）一字不动。修后 `grep 出來栄え|波亂 content*.py` = 0。

### (b) 机制文件 map — 同两词条的值（防重引入，非版面改动）

`hidden_files/w47/scratch-fanout-ja/map-zh-tw.json`（221 条，JSON 仍可解析）：

```diff
- "…出来栄え 今年的品质…" : "…出來栄え 今年的品質…"
+ "…出来栄え 今年的品质…" : "…出来栄え 今年的品質…"
- "波乱 出乎意料…" : "波亂 出乎意料…"
+ "波乱 出乎意料…" : "波乱 出乎意料…"
```

- 值 `來`→`来`、`亂`→`乱`：与 (a) 同一修复，否则重跑 apply.py 会把错字重新带入本版。
- 键不动：键须与现行核心原文逐字一致（apply.py 全局校验），两键实测均仍带引号出现于 core-ja 内容文件；改键反而会制造死键。
- 未动 `miss-zh-tw.json` / `miss2-zh-tw.json`（旧轮次“未命中”快照，历史证据，非机制输入）。

## 3. 重建（与构建同一解释器 `tools/venv/bin/python`）

| 步骤 | 日志 | 结果 |
|---|---|---|
| run.py run1 | `build-zh-tw-fix2-run1.log` | rc=0，TOTAL 150（A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38；范文 154 字），0 FLOW OVERFLOW / HEAD TOO WIDE |
| run.py run2 | `build-zh-tw-fix2-run2.log` | rc=0，同上，0 溢出 |
| 冻结 | `zh-tw-sha-fix2-run1.txt` vs `run2.txt` | **8/8 逐字节一致**（`diff` 无输出） |
| 相对修前 | `zh-tw-sha-fix2-pre.txt` vs `run2.txt` | **仅 p3-bunka.svg 与 p4-supotsu.svg 两页变化**，余 6 页 sha 不变 |
| render.py | `render-zh-tw-fix2.log` | rc=0，8 张 cards + print PDF 26,034,639 字节 |
| webpdf.py | `webpdf-zh-tw-fix2.log` | rc=0，8 页，798 distinct chars（修前 799——少掉的 2 字即本次修掉的 `來`/`亂` 字形），44,661 text bytes |
| export text.md | `export-zh-tw-fix2.log` | rc=0，44,361 字节，1325 text lines |

## 4. 中途阻塞：瞬时磁盘配额 EDQUOT（已处理，未删文件）

- 现象：全部门禁跑完后，写 `key-compare-fix2.py` 时报 `Disk quota exceeded (os error 122)`，`df` 仍显示 /home/hatch 45G 空闲——配额封顶，非磁盘满（与 fix1 的 run2 中断同类，但本次发生在门禁之后、构建之前无影响）。
- 处理（按任务规则：立即停手，只删自己笔记目录内可复现的中间件后重试一次）：先查本轮笔记目录占用——仅 72K，全部是日志/JSON 证据，无可释放的大中间件，删了也无意义，故**未删任何文件**；随即探针：`/tmp` 与笔记目录写盘均成功，配额已恢复；按规则重试一次，写盘成功。
- 附：同一事件还导致此前一次 key-review 的 heredoc 追加静默失败（文件停在 162 行、修正比对段缺失）；已改用文件脚本 `key-compare-fix2.py` 重跑并 `tee -a` 追加，补全（见 GATE-LOG §9）。
- 教训：EDQUOT 瞬时发作时，heredoc 追加可能静默丢数据而不报错——关键比对须落盘后立即验行数/关键行，不能只信 rc。

## 5. 交付物（新）

| 交付物 | 字节 | SHA-256 |
|---|---|---|
| Print PDF `Lucerna-VOL4-JA-ZH-TW.pdf` | 26,034,639（旧 26,034,685，-46） | `a2640e158bf5c13eeea572de1898d7faf7311d98fa92fc27e681fccc7abac4db` |
| Web PDF `Lucerna-VOL4-JA-ZH-TW-web.pdf` | 4,788,063（旧 4,788,782，-719，< 7 MB） | `00575aa2683794a11b6a274c091383cf89fcb12af649b8e731a9ae024712b27a` |
| `.text.md` `2026-w47-ja-zh-tw.text.md` | 44,361（与旧同） | `8c18a0e9fb47b145108a23b1144cd58bd9f7e3fc20e7ec5575d1cb55bb3d5db0` |
| 8 SVG（`svg/`） | — | run1==run2，见 §3；仅 p3/p4 变 |
| 8 cards（`cards/` PNG） | — | render.py 重渲 |
| `ABSTRACT.txt` | 235（未动） | `fdcf43b8c9d4718ea21eac14d4a5ffcf83e3fe7edc571fbd7c0da758b2faf9e6` |

- 两 PDF 均为 8 页；文字层各 44,661 字节（与修前同）。
- KIT（`WEEKLY-KIT.md`）§2/§3/§4 已更新 + §11 新增 F7；`EDITION-RECORD.md` 交付表与门禁已更新（新增 Fix2 一节；状态仍以第二轮全量复校结论为准，本修补不改“定稿”状态）。

## 6. 改动范围自查

- 本版内实际变化的文件：`content34.py`（2 字）、`svg/p3-bunka.svg`、`svg/p4-supotsu.svg`（重渲）、`cards/*.png`（8 张重渲）、两 PDF、`2026-w47-ja-zh-tw.text.md`、`WEEKLY-KIT.md`、`EDITION-RECORD.md`。
- 本版外唯一改动：`hidden_files/w47/scratch-fanout-ja/map-zh-tw.json`（2 个值各一字）。
- 未动：core-ja 任何文件（只读核实）、W43–W46、其他目标语家庭、tools/、issues/、ABSTRACT.txt、其余 content*.py、`run.py`/`render.py`/`bslib4.py`/`svglib.py`、`assets/`、`miss-zh-tw.json` / `miss2-zh-tw.json`。
- 未执行：insert.py、lint --write、git add/commit/push/reset/stash。
