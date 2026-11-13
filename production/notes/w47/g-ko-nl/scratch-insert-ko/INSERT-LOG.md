# W47 ko bundle — INSERT-LOG

- 工单：恢复协调员 #6 派单，步骤 4，第七家（ko）。commit only，绝不 push。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-insert-ko/`
- 仓库：`~/workspace/weekly-git`
- 开工核对：`df -h` 已用 97G（<100G，可开工）；HEAD = `104e4e328fa06a1f0a5e6ddb46718196e6a8d130`（ja bundle commit，与任务一致）；`git status --porcelain` 535 行 `??`（已知渲染产物，见仓库 AGENTS.md）。
- 方法：未跑原版 `main_bundle`（其 clean-tree 检查会被 535 行 `??` 触发）；import 原版 `tools/insert.py`，用原版 `render_md` 渲染/校验，按 `main_bundle` (c)–(e) 复现，只跳过 clean-tree 检查与 push。`git add` 只加显式路径。

## Seed excerpt 核对

- W46 先例：`issues/2026-w46/2026-w46-ko-en/2026-w46-ko-en.md` excerpt =
  “11월 9일 월요일부터 15일 일요일까지, 이번 주는 김장이 한창인 주간이에요. 배추 값은 내렸는데 새우젓 값은 올랐어요。”
  = W46 core-ko P1 头条段（`production/2026-w46/core-ko/2026-w46-ko-zh-cn.text.md:27`）前两个完整句。方法证实。
- W47 core-ko P1 头条段（`production/2026-w47/core-ko/2026-w47-ko-zh-cn.text.md`，Page 1）：
  “11월 16일 월요일부터 22일 일요일까지, 이번 주는 수능 주간이에요. 수요일 11월 18일에는 예비소집이 있고, 목요일 11월 19일에는 수능이 있어요. 수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요.”
- W47 `production/covers/2026-w47/cover.json` ko excerpt 与上述三句完全一致（cover excerpt = 完整头条段三句；前两句与 core-ko 完全一致）。
- 采用 seed excerpt（前两句，句间一空格）：
  “11월 16일 월요일부터 22일 일요일까지, 이번 주는 수능 주간이에요. 수요일 11월 18일에는 예비소집이 있고, 목요일 11월 19일에는 수능이 있어요.”
- exercises=150。ko-zh-cn 版目录经 `insert.resolve_bundle_dir` 的 core 兜底解析到 `production/2026-w47/core-ko`（内含 `2026-w47-ko-zh-cn.text.md` + `Lucerna-VOL4-web.pdf`）。

## 渲染（步骤 b，fail-fast，11/11 通过）

| slug | web PDF 字节数 | web PDF SHA-256 | text.md 字节数 | text.md SHA-256 |
|---|---|---|---|---|
| 2026-w47-ko-de | 3956937 | 4b1a54ce3040982076796965e45135e00ac057848315e6d3374235b6ec9212e4 | 36012 | 4f6945d3611552aa90fc1fea66d4270f63ae939fb3196f616cee86215f68c16a |
| 2026-w47-ko-en | 3951102 | 59bb38b0bc771cb8eb1c89b65c828e419780317db80573369bbfacddc189b3c7 | 35781 | f5e5bb278704c676b8904b23b47a46b7444fc1529c5c43ff6e10760da54fa7e5 |
| 2026-w47-ko-es | 3955583 | e1ae9fcc033b58266bc9652b653ae27cbb56f396c477186a18d594c1cf9e09c9 | 36065 | a24bd9ffaa097d529f6fc81b98748126ad1a471d44b9323ba3de15c8313f2b06 |
| 2026-w47-ko-fr | 3954158 | dc933cc18cfee50111b035d95c9ffecc3547b9a1b85f1b56b01853ad5179bbe1 | 36131 | 661b391e24d370bc54b2c9dd615f3e0c661a99dfc2b4539db05c615f871570de |
| 2026-w47-ko-it | 3949052 | f0efba8a29ab51061e10c2d5fe854f47aad29bb9cf381043243b51a16ad11aeb | 36068 | 4e7926e4ffa795fd12055bdf4f959711b4f78037fc6c5a05dc9f890b52155ecc |
| 2026-w47-ko-ja | 4373107 | f9bb1d3a392996ba8344083be0aac90ed30873ddb2ab8f296516de656c65b7f8 | 36275 | be048d7d4164ed8466642665f18bdf765174ccfff62342642a489327f6d71a9e |
| 2026-w47-ko-nl | 3950671 | 5f84566e41ded4b03c2b40ff7c6596c1251db61b82f6c82586e191580b6e279b | 35904 | 55abafb3fee843b26e69f67b61bb30973a61b3fc9c128e7951a2d9d2b53ccc4d |
| 2026-w47-ko-pt | 3956638 | e4028beb886a1ff0be9cf753983d11e30d8c751132df27c0cfd5395ea018a418 | 35935 | 059743986a5214459fdd66f777cc64991bedb20da7273b8cda457c47a11dc388 |
| 2026-w47-ko-ru | 4047903 | 5fc509995df17bee4d98e9483a1861157efebece886c535f3a031b9131cbd2fa | 38039 | e439f6a60a13d26bfdc3ac17d502cef1592063e6fe8fecf1e15c8f52109e6841 |
| 2026-w47-ko-zh-cn | 4226882 | ac97b284fe160de403d637b5e5a6d05f3aa6a3574cae5d28022feadfab6a8373 | 35456 | 044001ac2f14e76620a3c5109ecd85a29d6875d05401fd11f071070e91c5d3f3 |
| 2026-w47-ko-zh-tw | 4323857 | 189fde45fc9e7b747611f4beb0285db17ce34f77aefff372bf16e868b82110f1 | 35487 | 841a26658cb7dcff9d3489e95caedd5558165a73efc9e37bbb262c75693b0203 |

每版 sibling 均为 `(seed)`（issues/2026-w47 内尚无 ko 家 md）。渲染驱动：`render_bundle.py`（manifest.json + rendered/*.md 存本目录）。

## 写盘 + lint + commit（步骤 c–e）

- 写盘：11 版 × 3 文件（`.md` / `.text.md` / `.pdf`）→ `issues/2026-w47/<slug>/`；`node lint.mjs --write` 一次，RC=0。
- `node lint.mjs --require-pdf`：RC=0，`OK: 467 editions, index.json is current`（456 + 11）。
- commit：`git add` 仅显式路径（index.json + 33 个 issues/ 文件）；message 与原版一致：
  `Add 2026-w47-ko bundle (KO text · 11 natives)`。
- **Bundle commit SHA：`ac262bfc6561c3c755ead5dff64579ee91771ef5`**
- 核实：`git show --stat HEAD` 恰为 34 files（33 + index.json）；`git status --porcelain` 仍为 535 行 `??`，无其他 M/D；`git ls-files issues/2026-w47/2026-w47-ko-*` = 33。
- **绝不 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。只报本地 commit SHA。

## Scratch 清理（步骤 f）

- 核实方法：沿用 ja 家 `verify_scratch.py`（逐文件与仓内 `production/2026-w47`、`issues/2026-w47`、`tools/`、`production/covers/2026-w47` 共 13448 文件同名同大小同 SHA 比对，记 IN_REPO；其余按 SCRIPT / REPORT / DIFF / DATA / RENDER / LOG / PYC 分类；仅无 SCRIPT、REPORT、DIFF、DATA 且无断链的目录可删；不存在的目录判 KEEP）。核实脚本存本目录 `verify_scratch.py`，明细存 `scratch-verify.json`。
- ko 家（target=ko）候选目录共 **42 个，合计 2620.5 MB**。核实结果：**可删 0 个，42 个全部保留**——每个目录都含唯一脚本、审计报告（RUN-LOG / PROOF-NOTE / FIX-LOG / GATE-LOG）、.diff 补丁记录或未匹配的审计 json，一律保留，130 齐后统一收割归档。
- **已删：无（0 个，0 MB）。释放空间：0 MB。**删除前后 `df -h`：开工前 97G 已用 / 53G 可用，收尾 98G 已用 / 52G 可用——差额为本次 bundle commit 入库的 11 版 PDF（约 44MB）及并行他家工作写入，非本任务删除产生；本任务未删任何文件。
- 保留（42 个，约 2.6G）：scratch-d5-ko、scratch-fanout-ko、scratch-fanout-ko3、scratch-fix-ko、scratch-fix-ko-core1、scratch-fix-ko-core2、scratch-fix-ko-de-kit、scratch-fix-ko-de1、scratch-fix-ko-en1、scratch-fix-ko-textmd-d6、scratch-fix2-w47-ko、scratch-kit-edit-ko（EDIT-LOG.md，KIT 编辑唯一审计记录）、scratch-ko、scratch-ko-fix2、scratch-ko-fix3、scratch-ko-fix3b、scratch-ko-fix4、scratch-proof-ko、scratch-proof-ko-core5、scratch-proof-ko-de1、scratch-proof-ko-de2、scratch-proof-ko-en1、scratch-proof-ko-en2、scratch-proof-ko-es1、scratch-proof-ko-fr1、scratch-proof-ko-it、scratch-proof-ko-ja、scratch-proof-ko-nl、scratch-proof-ko-pt、scratch-proof-ko-ru、scratch-proof-ko-zh-tw、scratch-proof-ko2、scratch-proof-ko3、scratch-proof-ko4、scratch-proof-ko4b、scratch-proof-ko5、scratch-reproof-w47-ko、scratch-reproof2-w47-ko、scratch-reproof3-w47-ko、scratch-verify-ko、scratch-verify-ko-final（VERIFY-REPORT.md，ko 家终态核对报告）、scratch-webpdf-ko-zh。
- 未碰：ko 为 native 的他家目录（如 scratch-proof-de-ko2、scratch-proof-en-ko1、scratch-delta-en-ko、scratch-fix-zh-tw-ko1、scratch-reproof-pt-ko1、scratch-ru-ko-port-rebuild 等）、跨家目录（scratch-gatefix-ja-koit、scratch-core-ru-morozko）、散文件（probe-fix-zh-tw-ko1.txt、probe-proof-ja-ko2.txt、probe-proof-nl-ko1.txt）——不属于 ko 家。
- 本工单目录 `scratch-insert-ko/`（本日志 + `render_bundle.py` / `write_bundle.py` / `verify_scratch.py` / `manifest.json` / `rendered/` / `scratch-verify.json` / `commit-sha.txt`）保留。

## 附件（本目录）

- `render_bundle.py`（步骤 b 驱动）、`write_bundle.py`（步骤 c–e 驱动）、`verify_scratch.py`（步骤 f 审计驱动）
- `manifest.json`（11 版 pins）、`rendered/`（11 份渲染后 .md）、`scratch-verify.json`（42 个候选目录审计明细）、`commit-sha.txt`
