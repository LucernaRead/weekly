# W47 ja bundle — INSERT-LOG

- 工单：恢复协调员 #6 派单，步骤 4，第六家（ja）。commit only，绝不 push。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-insert-ja/`
- 仓库：`~/workspace/weekly-git`
- 开工核对：`df -h` 已用 97G（<100G，可开工）；HEAD = `2fadcc32b8d14cbb251995dec26f705e12824a22`（it bundle commit，与任务一致）；`git status --porcelain` 535 行 `??`（已知渲染产物，见仓库 AGENTS.md）。
- 方法：未跑原版 `main_bundle`（其 clean-tree 检查会被 535 行 `??` 触发）；import 原版 `tools/insert.py`，用原版 `render_md` 渲染/校验，按 `main_bundle` (c)–(e) 复现，只跳过 clean-tree 检查与 push。`git add` 只加显式路径。

## Seed excerpt 核对

- W46 先例：`issues/2026-w46/2026-w46-ja-en/2026-w46-ja-en.md` excerpt =
  “読書週間は、9日（月よう日）で終わります。 10月27日（火よう日）に始まりました。”
  = W46 core-ja P1 头条段（`production/2026-w46/core-ja/content12.py:39`）前两个完整句。方法证实。
- W47 core-ja P1 头条段（`production/2026-w47/core-ja/content12.py:40`）：
  “19日（木よう日）は、酉の市・二の酉です。浅草の鷲神社では、午前0時の一番太鼓から、24時まで市が開きます。熊手を買う人の夜です。”
- W47 `production/covers/2026-w47/cover.json` ja excerpt 首句与第二句与上述完全一致（cover excerpt 另续两句，同源更长）。
- 采用 seed excerpt（前两句，句间一空格）：
  “19日（木よう日）は、酉の市・二の酉です。 浅草の鷲神社では、午前0時の一番太鼓から、24時まで市が開きます。”
- exercises=150。ja-zh-cn 版目录经 `insert.resolve_bundle_dir` 的 core 兜底解析到 `production/2026-w47/core-ja`（内含 `2026-w47-ja-zh-cn.text.md` + `Lucerna-VOL4-web.pdf`）。

## 渲染（步骤 b，fail-fast，11/11 通过）

| slug | web PDF 字节数 | web PDF SHA-256 | text.md 字节数 | text.md SHA-256 |
|---|---|---|---|---|
| 2026-w47-ja-de | 4387416 | c24dfb09d7d0c54333c6f43aafdf697a08e99a178c5be5b762bc571c90086d4c | 46520 | 0d8d1de78a06d4df371b88425cb66f330222e6ca1a200632fdcdc48c8c95bd22 |
| 2026-w47-ja-en | 4379966 | 0560f0e4ea8520899c0b7054ded812d2a16fba6cec0f9e55cfc3bec8b99c1d8d | 45706 | fb5a4700d3c94cd17039d8b69d2626e35ed115812fdcb5ca34f17294f8860c3f |
| 2026-w47-ja-es | 4387651 | 43a26e56278f7b7cca4219c18ce508bdc2fe1662e99e2f91584e4ebcb71f09f2 | 46702 | d8e0c3018361cdce75084706e6857e642822992ecab8ac55f5865b861091ebb0 |
| 2026-w47-ja-fr | 4386312 | ef073db3df3789ef4326440df33cea387675e0ed1b5dacc17161220bf0622c5a | 46882 | badb0a6e7d00858afda9e6d1e158a915e93bd1ee41478e23bf3857cf23c72563 |
| 2026-w47-ja-it | 4381291 | 3cb1e9559b3a6e7763858cbaeae56eee9a61e54a083e8ade9c5c950e513a62fb | 46692 | 91224d88a55d5dc7ae8c3411e62d4199fe32d4028293223ba5373bd3a21125aa |
| 2026-w47-ja-ko | 4552025 | bdf5074b36981cf6bcf913a8d732a604dd37d4be9a65398c6c6a43b79f4c3f73 | 47722 | b1736ccf46f8cd2cc7646038c5163849e306210884d4b15fbb3f388a82535517 |
| 2026-w47-ja-nl | 4379026 | 97ee26ba16163696bd9a1ff30968bd71e8eab18af4cc75fcf9f2e04ded95f338 | 45627 | 7f8f6638e6352eb8ba9c1a2b3283f0e2436ea65613cf15c109ae3f067f69af4d |
| 2026-w47-ja-pt | 4388490 | a573debf07556431b5d8b20d95f088d9f8f098c84935380f9a7fb3635ab5a81e | 46696 | 9c9609378189a5b32b894b5c26adbdf4e8e1b23bbbe7b923f7a6198c4c62564a |
| 2026-w47-ja-ru | 4469712 | d130ae325fedb8325a724aef3ee3889b1db01c9ee0d5091b74644a9ab388dbd5 | 53004 | f934bcf1d9f4611d094ed6f55a1f76fc8da74663cfe647c9fed17025af3d4eec |
| 2026-w47-ja-zh-cn | 4654731 | 0f9098ff3bf0836c279960beffdb1ff619c1cdb01fceef699046c0a77be1e9ef | 44432 | 55c570f1bd0e9ea4d907960fe0fc472fe69440bacf67a83af40d0d48b977e1aa |
| 2026-w47-ja-zh-tw | 4789292 | 649ac196e81abf1a99524847e89ca4d5104080f12b644aa234aee0b94819b5cc | 44361 | 77fb0f36c75bb4713873b33793d63fc243f27fee3d4450c1d1e8f5da94ed416f |

每版 sibling 均为 `(seed)`（issues/2026-w47 内尚无 ja 家 md）。渲染驱动：`render_bundle.py`（manifest.json + rendered/*.md 存本目录）。

## 写盘 + lint + commit（步骤 c–e）

- 写盘：11 版 × 3 文件（`.md` / `.text.md` / `.pdf`）→ `issues/2026-w47/<slug>/`；`node lint.mjs --write` 一次，RC=0。
- `node lint.mjs --require-pdf`：RC=0，`OK: 456 editions, index.json is current`（445 + 11）。
- commit：`git add` 仅显式路径（index.json + 33 个 issues/ 文件）；message 与原版一致：
  `Add 2026-w47-ja bundle (JA text · 11 natives)`。
- **Bundle commit SHA：`104e4e328fa06a1f0a5e6ddb46718196e6a8d130`**
- 核实：`git show --stat HEAD` 恰为 34 files（33 + index.json）；`git status --porcelain` 仍为 535 行 `??`，无其他 M/D；`git ls-files issues/2026-w47/2026-w47-ja-*` = 33。
- **绝不 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。只报本地 commit SHA。

## Scratch 清理（步骤 f）

- 核实方法：沿用 it 家 `verify_scratch.py`（逐文件与仓内 `production/2026-w47`、`issues/2026-w47`、`tools/`、`production/covers/2026-w47` 共 13415 文件同名同大小同 SHA 比对，记 IN_REPO；其余按 SCRIPT / REPORT / DIFF / DATA / RENDER / LOG / PYC 分类；仅无 SCRIPT、REPORT、DIFF、DATA 且无断链的目录可删）。核实脚本存本目录 `verify_scratch.py`，明细存 `scratch-verify.json`。
- ja 家（target=ja）候选目录共 **53 个，合计 1282.8 MB**。核实结果：**可删 0 个，53 个全部保留**——每个目录都含唯一脚本、审计报告（RUN-LOG / PROOF-NOTE / FIX-LOG / GATE-LOG）、.diff 补丁记录或未匹配的审计 json，一律保留，130 齐后统一收割归档。
- **已删：无（0 个，0 MB）。释放空间：0 MB。**删除前后 `df -h` 均显示 97G 已用（开工前 53G 可用，收尾复核时 52G 可用——差额为并行他家工作写入，非本任务产生；本任务未删任何文件）。
- 保留（53 个，约 1.3G）：scratch-d5-ja、scratch-fanout-ja、scratch-fix-ja、scratch-fix-ja-ko1、scratch-fix-ja-map221、scratch-fix-ja-nl1、scratch-fix-ja-ru1、scratch-fix-ja-zh-tw2、scratch-fix2-w47-ja、scratch-fix3-w47-ja、scratch-gatefix-ja-koit、scratch-ja、scratch-ja-de-fix1、scratch-ja-en-fix1、scratch-ja-es-fix1、scratch-ja-fix-core1、scratch-ja-fix2、scratch-ja-fr-fix1、scratch-ja-it-fix1、scratch-ja-pt-fix1、scratch-ja-tables-sweep、scratch-ja-zh-tw-fix1、scratch-kit-edit-ja（EDIT-LOG.md，KIT 编辑唯一审计记录）、scratch-proof-ja、scratch-proof-ja-core2、scratch-proof-ja-de1、scratch-proof-ja-de2、scratch-proof-ja-en1、scratch-proof-ja-en2、scratch-proof-ja-es1、scratch-proof-ja-es2、scratch-proof-ja-fr1、scratch-proof-ja-fr2、scratch-proof-ja-it1、scratch-proof-ja-it2、scratch-proof-ja-ko1、scratch-proof-ja-ko2、scratch-proof-ja-nl1、scratch-proof-ja-nl2、scratch-proof-ja-pt1、scratch-proof-ja-pt2、scratch-proof-ja-ru1、scratch-proof-ja-ru2、scratch-proof-ja-zh-tw1、scratch-proof-ja-zh-tw2、scratch-proof-ja2、scratch-proof-ja3、scratch-reproof-w47-ja、scratch-reproof2-w47-ja、scratch-reproof3-w47-ja、scratch-reproof4-w47-ja、scratch-verify-ja、scratch-verify-ja-final（VERIFY-REPORT.md，ja 家 §8.4 终态核对报告）。
- 未碰：ja 为 native 的他家目录（如 scratch-proof-de-ja1、scratch-proof-en-ja1、scratch-delta-en-ja、scratch-proof2-it-ja1、scratch-reproof-pt-ja1 等）、跨家目录（scratch-ru-rebuild-ja、scratch-webpdf-nl-ru-ja）、散文件（FIX-LOG-nl-ja-fix1.md、MOVE-DONE-ja-nl.md、probe-*.txt）——不属于 ja 家。
- 本工单目录 `scratch-insert-ja/`（本日志 + `render_bundle.py` / `write_bundle.py` / `verify_scratch.py` / `manifest.json` / `rendered/` / `scratch-verify.json` / `commit-sha.txt`）保留。

## 附件（本目录）

- `render_bundle.py`（步骤 b 驱动）、`write_bundle.py`（步骤 c–e 驱动）、`verify_scratch.py`（步骤 f 审计驱动）
- `manifest.json`（11 版 pins）、`rendered/`（11 份渲染后 .md）、`scratch-verify.json`（53 个候选目录审计明细）、`commit-sha.txt`
