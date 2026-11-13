# CHECK-NOTE — 2026-W47 ru-zh-tw 状态核查（只读）

- 探针结果：**通过** — `git -C ~/workspace/weekly-git hash-object -w /dev/null` 返回 `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`（2026-11-11 19:35 UTC）；goals-side 真实写文件 `probe.txt` 成功。TMPDIR 全程用本 scratch 目录，未用 /tmp。
- production 三 SHA（实测，与 KIT §1 一致）：印 `2d19ad648194eeceeb03ddf9dd313326a51dd5f077ce9e9b0ae65753caeb42b4`（24,784,766 B）／网 `991b22ab217eaf925aee4c444e71b9c423c5dfa09b6471a8de8459637671d52d`（3,995,314 B）／文 `bc9c425f1c887d4ad70b7f2369671b3d36979b33d40713967977a4febd4a62c4`（60,887 B）。
- **结论：(2) 该版未建成／未定稿，需派替代工——派独立 re-proof（proof2），不是重建。** 盘上 Build 2 已重建、自检零问题，但 SOP 要求的独立重校从未派出、从未跑过；且该版在 git 里零提交、未入仓。替代工任务见文末 §6。
- 「mystery」工人 2a61b9b0 已查明：**就是 ru-zh-tw proof1 工人，其 scratch 真实存在**（`scratch-proof-ru-zh-tw1/`），所谓“无 scratch 记录、roster 无影”是记录脱节，不是工人失踪。详见 §3。

核查时间：2026-11-11 ~19:35–19:45 UTC。只读：未改任何生产文件，未 commit，未 push。

---

## 1. production 目录：存在，三件 + ABSTRACT + KIT 齐全，KIT 三 SHA 与盘上逐字一致

路径：`~/workspace/weekly-git/production/2026-w47/2026-w47-ru-zh-tw/`

| 文件 | 字节 | SHA-256（sha256sum 实测） | mtime (UTC) | 与 KIT §1 |
|---|---|---|---|---|
| `Lucerna-VOL4-ru-zh-tw.pdf`（印） | 24,784,766 | `2d19ad648194eeceeb03ddf9dd313326a51dd5f077ce9e9b0ae65753caeb42b4` | 2026-11-11 15:49 | 一致 |
| `Lucerna-VOL4-ru-zh-tw-web.pdf`（网） | 3,995,314 | `991b22ab217eaf925aee4c444e71b9c423c5dfa09b6471a8de8459637671d52d` | 2026-11-11 15:52 | 一致 |
| `2026-w47-ru-zh-tw.text.md`（文） | 60,887 | `bc9c425f1c887d4ad70b7f2369671b3d36979b33d40713967977a4febd4a62c4` | 2026-11-11 15:54 | 一致 |
| `ABSTRACT.txt` | 348 | `602879243337f313a588b59ba3e01da7e2aa6ddb227e1037d27c972f4fc06fde` | 2026-11-11 06:45 | KIT 未列 SHA（表中为 —） |
| `WEEKLY-KIT.md` | 13,620 | `98a7a529d2713d2aed1a18573db854f0afbf17c0ce1cabed20a7af54b7242336` | 2026-11-11 16:04 | — |

KIT 头部（L5）原话：`Status: DONE — zero open issues (self-check). Re-fanout 2026-11-11 (core fix1 + D1 map fix) = Build 2, final. Re-proofread follows; this self-check does not replace it.`

目录内另有构建源文件（`content12/34/56/7/8.py`、`run.py`、`render.py`、`ru_textmd.py`、`bslib4.py`、`svglib.py`、`check_core.py`，均 2026-11-11 15:44）、`svg/` 8 文件（15:44–15:45）、`cards/` 8 PNG（15:46–15:47）、`assets/` 8 图 + CREDITS.md（2026-11-10 20:34）。**目录不存在的说法不成立。**

## 2. hidden_files/w47/ 下 ru-zh-tw 相关 scratch：4 处，结论各异，无 re-proof

### 2a. `scratch-proof-ru-zh-tw1/` — proof1（Build 1），结论 (b) 有缺陷不能定稿

- 内容：`PROOF-NOTE.md`（8,553 B，mtime 11:50）、`GATE-LOG.md`（17,213 B，mtime 11:50）、`keycheck-150.json`、`freeze-diff.json` / `freeze-diff-dump.txt` / `freeze-diff-p1-5.txt`、`occlusion.json` / `occlusion-core.json`、`p8-compare.json`、裁图 PNG 约 20 张（11:18–11:40）、`boxtitle*.log`、`creambox.log`。**PROOF-NOTE / GATE-LOG 均在。**
- PROOF-NOTE.md L5 结论原话：`结论：(b) 有缺陷，不能定稿 — 缺陷 2 项（D1 Major ×1，D2 Minor ×1）。依仓库 AGENTS.md「一輪獨立複校零問題 + 幾何遮擋零標記方可入倉」，本版不得入倉，須修復後重渲染、重新複校。`
- D1（Major）：fan-out 悄悄删掉 4 处俄语核心层文字（P6 图表标题 `УЧЕБНЫЕ ДАННЫЕ`、P6 免责声明俄语句、P7 副标题 `Три уровня, три темы`、P8 副标题 `Большой тест недели + все ответы`），KIT 未披露；10 个 ru 版 text.md 里 `УЧЕБНЫЕ ДАННЫЕ` 出现次数全为 0，属流水线行为。
- D2（Minor）：P1 kicker 词距过紧，三处词对视像素连成一词（PIL 墨迹间隙 1.4–2.6px，一处 −0.1px 相触）。
- **核对对象是 Build 1**：PROOF-NOTE 身份核对表三 SHA 为印 `69239a09d74a478e975893b8ee7866facd8ed16fb8bcfe7b14f78307b03469d7`（24,785,168 B）、网 `543ce70dd628ee47313da3ffe667f2ef40df44841b299095a40bb9774200bfbd`（3,963,820 B）、文 `e4a5374c6f4bfa8e66c5e917a73cca4f54a7d78c61292695b3b3125a73a3fc1d`（60,815 B）——**与当前盘上 Build 2 的三 SHA 全部不同**。即 proof1 只覆盖已作废的 Build 1，对当前 Build 2 无效。

### 2b. `scratch-fanout-ru/` — 首轮 fan-out（Build 1 构建），FANOUT-REPORT 在

- `FANOUT-REPORT-ru.md`（12,876 B，mtime 2026-11-11 06:47）；`map-zh-tw.json`（27,791 B，06:38）、`meta-zh-tw.json`；`de/en/es/fr/it/ja/ko` 子目录 + `build_map.py` / `apply_ru.py` / `adjudicate_ru.py`。
- 报告 L54–56：`## zh-tw — DONE, zero issues`，三 SHA 即 Build 1（印 `69239a09…` / 24,785,168 B；网 `543ce70d…` / 3,963,820 B；文未在摘录行内，见 PROOF-NOTE）。L58 另记工具修：`s11_check.py` 把 `zh-tw` 截成 `tw` 误触发拉丁读者 CJK 检查，已修。

### 2c. `scratch-fix-ru-d1/` — D1 机制修复（10fed8d1），FIX-NOTE 在，含 ru-zh-tw 验证重建

- `FIX-NOTE.md`（15,301 B，mtime 12:08）、`build_map.py` / `apply_ru.py` / `verify_ru_zh_tw.py`、`maps/`（10 语）、`freeze-diff-rebuilt.json`、`freeze-diff-shipped-control.json`、`rebuild-ru-zh-tw/`（内含 `2026-w47-ru-zh-tw/` 子目录 + `run.log` 11:59 + `textmd.log` 12:00）。
- FIX-NOTE L1–6：交付是修好的机制，不是成品；只读生产文件，未改盘上 10 个版、未改 core-ru、未 commit、未 push。机制：`build_map.py` 增 KEEP_AS_IS（4 键 × 10 语）；根因为 W46 TM 前例（tm2 "lit" 桶已替换俄语段）。
- FIX-NOTE §9 / run-log L1880：`rebuild-ru-zh-tw/` **仅为验证品，不是交付物**，未跑 render/PDF/门禁。**不要把它当作成品。**

### 2d. `scratch-refanout-ru/` — 重 fan-out（03edf0cb），FANOUT-REPORT + records/zh-tw/RECORD.md 在

- `FANOUT-REPORT-ru.md`（13,452 B，mtime 16:06）、`records/zh-tw/RECORD.md`、`records/` 下 en 等 9 语、`backup-old/2026-w47-ru-zh-tw/`（44 文件备份）、`logs/`（15:44）、`maps/`（15:26）。
- FANOUT-REPORT L33 表行：zh-tw 印 24,784,766 `2d19ad64…`、网 3,995,314 `991b22ab…`、文 60,887 `bc9c425f…`——**与当前盘上三 SHA 逐字一致**。
- `records/zh-tw/RECORD.md` 关键句：
  - `Rebuilt from finalized core-ru (fix1 f11854bf) with the D1 map fix.`
  - `Old edition backed up whole-dir to hidden_files/w47/scratch-refanout-ru/backup-old/2026-w47-ru-zh-tw/ (44 files).`
  - D1：text.md L459 `УЧЕБНЫЕ ДАННЫЕ`、L504 `Три уровня, три темы`、L596 `Большой тест недели + все ответы` 在位；免责声明 text.md 无、p6 SVG 有（by design）；freeze diff 删串 distinct 253 / count-sum 308，西里尔仅 `можно` ×1，unexplained 0。
  - D2：Q25 `День студента`（content12.py:276）；D6：Q20 `желании`（content12.py:257）；kicker double spaces 落地，PIL 间隙 [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]，最小 5.9px ≥ 4。
  - 门禁：apply rc=0；run.py exit 0 TOTAL 150 零溢出；render exit 0；check_core exit 0；p8 150/150 CLEAN keydiff [137, 138, 139, 140]；occlusion 42 TEXTX 0 LINEX，42/42 CLEAR；freeze 8/8；印/网文字层多重集同一（25,845 字符）；P8 最小 9.75pt；Morozko 图在位。
  - **Verdict 原话：`Zero issues. Rebuilt, re-gated, ready for independent proofread.`**
- 报告 L111：zh-tw freeze 参考数已纠正 256 → 253（kicker 3 串不再被删）；L156：zh-tw 的表格式 KIT 系手工更新（§1 表、§2 构建链、§3 门禁）。

### 2e. 不存在的东西（已核实无）

- `scratch-reproof-ru-zh-tw*`：goals-side **不存在**；`~/workspace/weekly-git/hidden_files/w47/` 下 grep `ru-zh-tw|reproof-ru` **零命中**（无误放的仓内 scratch）。
- 除 2a–2d 外，hidden_files/w47/ 下无其他 `*ru-zh-tw*` 目录（find 仅命中上述 4 处 + 本核查 scratch + `scratch-fix-ru-d1/rebuild-ru-zh-tw`）。

## 3. run-log.md 与 ledger.md 时间线（grep 实录）

run-log.md 中 `ru-zh-tw` 共 10 行（L1681、L1684、L1807、L1808、L1809、L1880、L1884、L1885、L2526、L2908）；`2a61b9b0` 共 3 行（L1684、L1807、L1808）。

| 时间 (UTC) | 来源行 | 内容 |
|---|---|---|
| ~11:42 | run-log L1681、L1684；ledger L570 | 补派 ru-zh-tw proof1（ru 最后一版；ru proof1s 9/9 派完进行中）。L1684 原话：`并行：pt-nl 完成 → 补派 ru-zh-tw proof1（2a61b9b0；印 69239a09…、网 543ce70d…、text e4a5374c…，盘上核实），回 ~16。` |
| 11:51 | run-log L1807（~13:50 记） | proof1 正式 handoff 到达（迟到件，11:51 UTC 完成）。L1808：结论 (b)，PROOF-NOTE 在 `scratch-proof-ru-zh-tw1/`，磁盘已核实，三 SHA 与任务一致（印 24,785,168 B `69239a09…`、网 3,963,820 B `543ce70d…`、文 60,815 B `e4a5374c…`）；2 缺陷 D1（Major，机制）+ D2（Minor，核心）。 |
| ~13:50 | run-log L1809；ledger L617 | D1 协调员磁盘核实属实（全族）：核心 text.md 4 串各 1 次；10 版 text.md 4 串全 0 次。O1 裁定：SOP §3 已决定——10 版全部恢复，非选项；修法为机制 keep-as-is + 重 fan-out。D1 机制修复已派（`scratch-fix-ru-d1/`）；D2 定界调查已派。 |
| （fix 完成） | run-log L1880、L1884–L1885；ledger L628 | D1 机制修复完成（10fed8d1）并磁盘核实；交付物清单见 §2c；KIT text.md 字节勘误（实 60,815 B 非 54,642）；重 fan-out 前置两点（补回旧 map 手修值；重过全门）。 |
| （re-fanout） | run-log L2526；ledger L961 | ru re-fanout DONE（03edf0cb）：10/10 重建，门禁全过；抽查 ru-en/ru-de/ru-zh-tw 三件 SHA 与报告全表一致。 |
| ~18:00 | run-log L2795；ledger L1051、L1070 | 协调员自查仍写“仅剩 zh-tw（2a61b9b0 派于 ~11:42 UTC，无 scratch 记录、roster 无影——仍待查盘再定，不盲派）”。**此句与 L1808 矛盾**：L1808 在 13:50 已记明 PROOF-NOTE 在 `scratch-proof-ru-zh-tw1/` 且磁盘已核实。mystery 的来源是这句自查记录过时／误写，不是工人失踪。ledger L1051 同样写“zh-tw 11:42 派过的 2a61b9b0 无 scratch 记录、未在 roster，待下次自查核”。 |
| ~19:30 | run-log L2908 | `ru-zh-tw mystery：核查员已派（d233fdac，只读，scratch-check-ru-zh-tw1/；结论三选一…；绝不盲目再派）。` |

**结论：2a61b9b0 的工作产品真实存在且早已被协调员盘核过（L1808）。“无 scratch 记录”不成立。**

## 4. core-ru 已定稿（ru-zh-tw 的上游），ru 家族 9/10 已定稿、仅剩 zh-tw

- core-ru：`production/2026-w47/core-ru/` 在位；fix1 已 commit `f11854bf`（`W47 core-ru fix1: D2 option b shorten + D6 prepositional key + kicker double-space (proof1 rounds)`）。KIT 头部：`核心版定稿后因 proof1 三处核心级缺陷重开，2026-11-11 已修复重建、全门禁绿（见 §7.5），未入仓、未发布`。
- core-ru 三 SHA 实测：印 `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81`（31,429,147 B，12:21）、网 `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197`（4,025,834 B，12:10）、文 `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc`（60,953 B，12:11）——**与 records/zh-tw/RECORD.md 引用的 core SHAs 逐字一致**，即重建所用的核心确为已定稿 fix1 核心、重建前后未动。
- ru 家族：run-log L2795（~18:00）FINALIZED es, fr, it, de, ja，en 待 re-proof，pt/nl 在 fix1，ko 在 proof1；其后 L2879 ru-en re-proof (a) FINALIZED、L2893/L2904 ru-pt 与 ru-nl fix2 后 FINALIZED、L2903 ru-ko re-proof (a) FINALIZED。L2899/L2903 汇总：**ru finalized 9/10（en/nl/pt/ko + es/fr/it/de/ja），仅剩 zh-tw 待查**。re-fanout 覆盖范围含 zh-tw（报告 L33 表行 + records/zh-tw/RECORD.md），与家族位置一致：zh-tw 是 ru 家最后一块未定稿。

## 5. git 记录（只读）：ru-zh-tw 零提交、未入仓、未入 issues/

- `git log --oneline --all -- 'issues/2026-w47/2026-w47-ru-zh-tw/*' 'production/2026-w47/2026-w47-ru-zh-tw/*'`：**零行**（无任何提交触及该版）。
- `git status --porcelain -- production/2026-w47/2026-w47-ru-zh-tw issues/2026-w47/2026-w47-ru-zh-tw`：仅 `?? production/2026-w47/2026-w47-ru-zh-tw/`（整目录未跟踪）。
- `issues/2026-w47/2026-w47-ru-zh-tw/`：**不存在**（insert.py 未跑，该版未入仓）。
- 对照：core-ru fix1 有提交 f11854bf；HEAD 为 c0382fa7。git status 另见 W43 大量已修改文件（另一 agent 遗留，本核查未碰）。

## 6. 结论 (2)：需派替代工——独立 re-proof（proof2），从重校步骤接手

**为什么不是 (1)：** Build 2 虽在盘上且自检零问题，但按 SOP §8.4 与 KIT 自述（`Re-proofread follows; this self-check does not replace it`），定稿须一轮独立重校零问题。重校从未派出（无 scratch、无 run-log/ledger 派单行），proof1 只覆盖已作废的 Build 1。因此该版**未定稿**。

**为什么不是 (3)：** 全部关键证据都在盘上：Build 2 三件 SHA 与 KIT/RECORD 逐字一致，核心 fix1 已定稿且 SHA 吻合，proof1→fix→re-fanout 链条完整可追溯。无证据缺口。

**替代工具体任务（从 re-proof 步骤接手，不重建）：**

1. 工作区：goals-side `hidden_files/w47/scratch-reproof-ru-zh-tw1/`（新建；绝不在 `~/workspace/weekly-git/hidden_files/` 下建）。
2. 开工三 SHA（Build 2，须先盘核一致再开工）：印 `2d19ad648194eeceeb03ddf9dd313326a51dd5f077ce9e9b0ae65753caeb42b4`（24,784,766 B）、网 `991b22ab217eaf925aee4c444e71b9c423c5dfa09b6471a8de8459637671d52d`（3,995,314 B）、文 `bc9c425f1c887d4ad70b7f2369671b3d36979b33d40713967977a4febd4a62c4`（60,887 B）；ABSTRACT.txt 348 B。
3. 任务：按 SOP §8.4 全量独立重校 Build 2（全文通读 + 150 题手验 + 几何/遮挡/ freeze / p8 / §1.1 全门禁独立重跑 + 8 页目视），重点独立复测 proof1 的 D1（4 串是否在位：text.md L459/L504/L596 + P6 免责声明 SVG）、D2（kicker 间隙，RECORD 称 PIL 最小 5.9px，须独立量测）、D6（Q20 `желании`）、Q25（`День студента`），并核对 KIT §1/§5/§9 数字是否与盘上一致（前例：ru-pt/ru-nl 均出过 KIT 文档漂移，须当作检查项）。
4. 交付：`PROOF-NOTE.md` + `GATE-LOG.md`，结论 (a)/(b)；生产零写入（开工/收工快照一致）；不 commit、不 push、不跑 insert.py。
5. **不要重复派 proof1，不要重建该版。** 2a61b9b0 的 proof1 已完成且有结论；重建已由 re-fanout 完成。派错步骤即重复劳动。

## 附：本核查未做的事

- 未重建、未改任何生产文件、未 commit、未 push（git status 除既有 W43 修改外无新增改动由本核查引入）。
- 未核查 D2 定界调查的后续（run-log L1809 称已派；其 scratch 不在本核查清单内，未追踪——re-proof 工人须在重校中独立量测 kicker，不依赖该调查结论）。
- 未重新跑任何门禁：本核查只核对记录与 SHA，未独立复测 Build 2 的质量。质量结论以待派的 re-proof 为准。
