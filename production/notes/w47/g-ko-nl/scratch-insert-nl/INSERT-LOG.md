# W47 nl bundle — INSERT-LOG

- 工单：恢复协调员 #6 派单，步骤 4，第八家（nl）。commit only，绝不 push。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-insert-nl/`
- 仓库：`~/workspace/weekly-git`
- 开工核对：`df -h` 已用 98G（<100G，可开工；`df -k` 101,720,532 KB）；HEAD = `ac262bfc6561c3c755ead5dff64579ee91771ef5`（ko bundle commit，与任务一致）；`git status --porcelain` 535 行 `??`（已知渲染产物，见仓库 AGENTS.md）。
- 方法：未跑原版 `main_bundle`（其 clean-tree 检查会被 535 行 `??` 触发）；import 原版 `tools/insert.py`，用原版 `render_md` 渲染/校验，按 `main_bundle` (c)–(e) 复现，只跳过 clean-tree 检查与 push。`git add` 只加显式路径。

## Seed excerpt 核对

- W46 先例：`issues/2026-w46/2026-w46-nl-en/2026-w46-nl-en.md` excerpt =
  “Op maandag 9 november begint het Sinterklaasjournaal op televisie. Elke dag om 18:00 uur volgen kinderen op NPO Zapp hoe Sinterklaas en zijn Pieten zich voorbereiden op de reis naar Nederland.”
  = W46 core-nl P1 头条段（`production/2026-w46/core-nl/2026-w46-nl-zh-cn.text.md:11`）前两个完整句。方法证实。
- W47 core-nl P1 头条段（`production/2026-w47/core-nl/2026-w47-nl-zh-cn.text.md`，Page 1）前两个完整句：
  “Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3.”
- W47 `production/covers/2026-w47/cover.json` nl excerpt 与上述两句**完全一致**（一字不差）。
- 采用 seed excerpt（前两句，句间一空格）：
  “Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3.”
- exercises=150。nl-zh-cn 版目录经 `insert.resolve_bundle_dir` 的 core 兜底解析到 `production/2026-w47/core-nl`（内含 `2026-w47-nl-zh-cn.text.md` + `De-Lucerna-VOL4-web.pdf` + `ABSTRACT.txt`）。其余 10 版均走主目录 `production/2026-w47/2026-w47-nl-*`；未找 fanout-nl/。

## 渲染（步骤 b，fail-fast，11/11 通过）

| slug | web PDF 字节数 | web PDF SHA-256 | text.md 字节数 | text.md SHA-256 |
|---|---|---|---|---|
| 2026-w47-nl-de | 1536368 | fbf0c25a503a8fb532b60dc60d1b95b265a00659df1c69afb334b6bddf299795 | 46247 | 6825c35db04c62e1bec4f8f6e6a511597a17af0b02b17bc5260a560043575785 |
| 2026-w47-nl-en | 1534493 | c7ffd6676cfa31798994f11af35a469485e6fefd1fa3a8e079c47c7aae3b0d95 | 45136 | e3273f300f42236a06faaddd3302b5be1a4a340adca285efdff19f2b23f3f316 |
| 2026-w47-nl-es | 1540051 | 7025ce05d97599d1910ab4e27f1e1c583ae86d43ef5d64a169b22bdb77ef0721 | 47648 | 672bd4c0080c14ab11026a13ccdecf826bd759cc3f348c5751852386efe4684b |
| 2026-w47-nl-fr | 1538511 | 1b429a3ff61edb99348c4d29a790204565b07a173e966f340268af79b9c585bc | 47744 | f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a |
| 2026-w47-nl-it | 1534364 | 9eff96cf487a6beb5e26413ac9683bf771aac12f0ef9d6c2eca1de5b399fbf93 | 47194 | e9880da2da990ad87348c650cc4f82637a108284d7929de2ed901019ef77ac0a |
| 2026-w47-nl-ja | 1967732 | 2b38c2547606d2a33b436cea4337acf4a93ddfbe4acdd93ef5533781d2755b7b | 47804 | b7e5f5dc8b484da52b0a22493149d93f0bbd3a0aeb79deb56b2f28e017a80084 |
| 2026-w47-nl-ko | 1791786 | 218aebe12b4ba140a0180cfdd3fcb2719547737f1e7c59682aca83a57fed231a | 47576 | e13db87160d1477972824431d9f4e194f90f53a53b7954e659cc74484801f537 |
| 2026-w47-nl-pt | 1542854 | 40c51869695b80e165661c6adb9309c70341342d56d632c472a7ba18f9ace508 | 47365 | 67516e2163c8c769ab9574b60b472c7d97706b3c4d89182bb95faa221513727a |
| 2026-w47-nl-ru | 1674522 | 7a06f80d9238669ae1c8c1bfc848a2b814d9f0999e3e9f4c79b942dd17747dff | 57909 | dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228 |
| 2026-w47-nl-zh-cn | 1874709 | 2b6f223eaff9afa7445c54b385213e8131eeddf11b9ae9a139388b32da7f940d | 44087 | aa1f470353f9fa24bdec29028e596dd924387fe7d05956f208a57006025e2327 |
| 2026-w47-nl-zh-tw | 1976266 | 542c6f1bc8e2f71b0cdf558e169dca3d1738e981919433c63182a304a44754ec | 44308 | bf1f627d1bbf6387cb0f782e6ede2feb3fe18ffb48bd599ce3720be3238b9855 |

每版 sibling 均为 `(seed)`（issues/2026-w47 内尚无 nl 家 md）。渲染驱动：`render_bundle.py`（manifest.json + rendered/*.md 存本目录）。

## 写盘 + lint + commit（步骤 c–e）

- 写盘：11 版 × 3 文件（`.md` / `.text.md` / `.pdf`）→ `issues/2026-w47/<slug>/`；`node lint.mjs --write` 一次，RC=0。
- `node lint.mjs --require-pdf`：RC=0，`OK: 478 editions, index.json is current`（467 + 11）。
- commit：`git add` 仅显式路径（index.json + 33 个 issues/ 文件）；message 与原版一致：
  `Add 2026-w47-nl bundle (NL text · 11 natives)`。
- **Bundle commit SHA：`797e8460c6f63bac034208d2848f8114534ce600`**
- 核实：`git show --stat HEAD` 恰为 34 files（33 + index.json）；`git status --porcelain` 仍为 535 行 `??`，无其他 M/D；`git ls-files issues/2026-w47/2026-w47-nl-*` = 33。
- **绝不 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。只报本地 commit SHA。

## Scratch 清理（步骤 f）

- 核实方法：沿用 ko 家 `verify_scratch.py`（逐文件与仓内 `production/2026-w47`、`issues/2026-w47`、`tools/`、`production/covers/2026-w47` 共 13481 文件同名同大小同 SHA 比对，记 IN_REPO；其余按 SCRIPT / REPORT / DIFF / DATA / RENDER / LOG / PYC 分类；仅无 SCRIPT、REPORT、DIFF、DATA 且无断链的目录可删；不存在的目录判 KEEP）。核实脚本存本目录 `verify_scratch.py`，明细存 `scratch-verify.json`。
- nl 家（target=nl）候选目录共 **60 个，合计 4139.8 MB**。核实结果：**可删 1 个，59 个保留**。
- **已删：`scratch-fanout-nl-archive`（空目录，0 字节，经 `ls -la` + `find` 确认无任何文件/隐藏文件后 `rmdir`）。释放空间：0 MB。**删除前后 `df -h`：开工前 98G 已用 / 52G 可用，收尾 98G 已用 / 52G 可用（`df -k` 收尾 101,757,476 KB 已用；差额为本次 bundle commit 入库的 11 版 PDF 约 18MB 及并行他家工作写入，非本任务删除产生；本任务仅删了一个空目录）。
- 保留（59 个，约 4.1G）：scratch-check-nl-pt1、scratch-d5-rebuild-nl、scratch-d5-redo-nl、scratch-delta-nl-de、scratch-delta-nl-en、scratch-delta-nl-es、scratch-delta-nl-fr、scratch-delta-nl-it、scratch-delta-nl-ja、scratch-delta-nl-ko、scratch-delta-nl-pt、scratch-delta-nl-ru、scratch-delta-nl-zh-tw、scratch-fanout-nl、scratch-fix-core-nl1、scratch-fix-core-nl3、scratch-fix-nl、scratch-fix-nl-de1、scratch-fix-nl-en1、scratch-fix-nl-es1、scratch-fix-nl-es2、scratch-fix-nl-ja1、scratch-fix-nl-ru2、scratch-fix-nl4、scratch-fix-nl5、scratch-fix-nl5b、scratch-gatefix-u201c-nlpt、scratch-kit-edit-nl（EDIT-LOG.md，KIT 编辑唯一审计记录）、scratch-nl、scratch-nl-fix、scratch-proof-core-nl2、scratch-proof-core-nl3、scratch-proof-nl、scratch-proof-nl-de1、scratch-proof-nl-de1-delta、scratch-proof-nl-en1、scratch-proof-nl-en2、scratch-proof-nl-es1、scratch-proof-nl-fr1、scratch-proof-nl-it1、scratch-proof-nl-ja1、scratch-proof-nl-ko1、scratch-proof-nl-pt1、scratch-proof-nl-pt1b、scratch-proof-nl-ru1、scratch-proof-nl-zh-tw1、scratch-proof-nl2、scratch-refanout-nl、scratch-reproof-nl-de1、scratch-reproof-nl-en1、scratch-reproof-nl-es1、scratch-reproof-nl4、scratch-reproof-nl5、scratch-reproof-w47-nl、scratch-reproof2-w47-nl、scratch-reproof3-w47-nl、scratch-verify-nl、scratch-verify-nl-final（VERIFY-REPORT.md，nl 家终态核对报告）、scratch-webpdf-nl-ru-ja。每个目录都含唯一脚本、审计报告（RUN-LOG / PROOF-NOTE / FIX-LOG / GATE-LOG）、.diff 补丁记录或未匹配的审计 json，一律保留，130 齐后统一收割归档。
- 未碰：nl 为 native 的他家目录（如 scratch-proof-de-nl1、scratch-proof-en-nl1、scratch-fix-ja-nl1、scratch-fix-ru-nl1、scratch-delta-en-nl、scratch-ru-rebuild-nl 等）、跨家目录、散文件（FIX-LOG-nl-ja-fix1.md、MOVE-DONE-ja-nl.md、probe-*.txt）——不属于 nl 家。
- 本工单目录 `scratch-insert-nl/`（本日志 + `render_bundle.py` / `write_bundle.py` / `verify_scratch.py` / `manifest.json` / `rendered/` / `scratch-verify.json` / `commit-sha.txt`）保留。

## 附件（本目录）

- `render_bundle.py`（步骤 b 驱动）、`write_bundle.py`（步骤 c–e 驱动）、`verify_scratch.py`（步骤 f 审计驱动）
