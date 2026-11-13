# INSERT-LOG — W47 en bundle (2026-11-13)

Worker: 恢复协调员 #6 派单，步骤 4，第二家。commit only，绝不 push。
Repo: `~/workspace/weekly-git`，起始 HEAD `bc08bf04`（de bundle commit）；de 家 11 版已入仓（index.json 含 401 editions）。
Disk at start: 98G used / 150G (`df -h`); < 100G，继续。

## 方法（与原版 main_bundle 的偏差）

- 未跑原版 `main_bundle`：其开头的 clean-tree 检查会被树上 535 行 `??`（渲染产物、必须留盘、绝不能 commit）触发而中止。
- 改为 import `tools/insert.py`，用原版 `render_md` / `resolve_bundle_dir` 渲染，再按 main_bundle (c)–(e) 逐行复现，只跳过 clean-tree 检查与 push 两步。
- 补偿：`git add` 只加显式路径（index.json + 33 个 issues/ 文件）；commit 前后核对 `git status --porcelain`——commit 前仅 ` M index.json` + 535 行 `??`（+11 个新 issues/ 目录 = 546 行）；commit 后回到 535 行 `??`，0 行 M/D/其他。
- `lint --write` 只跑了一次（步骤 c）。未跑 `push_with_verify` / `git push` / `ls-remote`。

## seed_excerpt 取法（de 家已确立的方法，W46 先例验证）

- W46 en-de excerpt（已入仓）：`On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens across the English-speaking world. In London, Ottawa, Canberra and Washington, people stop what they are doing, and for two minutes they stand still and say nothing.`
- 对照 W46 core-en P1 头条段：该 excerpt = 头条段前两个完整句（下一句 `It is the two-minute silence — …` 不取）。
- W47 cover.json en excerpt 只取第一句（同源、更短）：`On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states.`
- W47 core-en P1 头条段前两句与 cover 第一句同源一致，采用为 seed_excerpt（exercises 150，publishedAt = weekStart 2026-11-16，vol 4，8 页）：
  > On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states. By Sunday, November 8, the count was clear enough to call: the Democrats won the House, and the Democrats won the Senate.

## 渲染（b）：11/11 通过，均为 seed 模式（issues/ 里尚无 en 家 md）

| slug | edition dir | web PDF bytes | web PDF SHA-256 | text.md bytes | text.md SHA-256 |
|---|---|---:|---|---:|---|
| 2026-w47-en-de | production/2026-w47/2026-w47-en-de | 2334821 | 86438c44ceb8c499de88e64d0d0f70c6435134a55d85433dcb30b24d332f0ff4 | 52736 | 2b2af27cc59ba25382bfacf11398fce8a330c2235c6097c22fe0cc624cd7c0ee |
| 2026-w47-en-es | production/2026-w47/2026-w47-en-es | 2337042 | 452a9d0f891ac24a6a06a127b04414bbe5fec94eb08ffbf50cad911b93f3c829 | 54556 | cb334ba784acf059ea86dfa143f960f728870a8a321eb81645f7108005376d0a |
| 2026-w47-en-fr | production/2026-w47/2026-w47-en-fr | 2336319 | 18523f7b61779902091cb6d494b2118134fa68598b4f03e7603f88e3c682f362 | 53974 | cbe3b588d970f172b131ee5642f44ca16822b299be2de68fc64de539d22bf227 |
| 2026-w47-en-it | production/2026-w47/2026-w47-en-it | 2330932 | 24ad7443e932c63624c050d9c9c6e3e79c4947180993449833e32d441fd2896e | 54115 | 3d6c872ff631d267f202e0b9ecc56ded477a63068c4e492f8747099e5c3790a0 |
| 2026-w47-en-ja | production/2026-w47/2026-w47-en-ja | 2713215 | e0ead68adf7a5be76c2b26c8fb6b2662732ac5b19b27f788c9f377795186b911 | 53756 | 2ccd31bee63d5abc4b50f35a4a77923922bfd4bb63e0b2f168211f46f04c3f4e |
| 2026-w47-en-ko | production/2026-w47/2026-w47-en-ko | 2535257 | 7c486f7d60aac42e310f7d9ad7120e1a6385d65aaceca1757ce9b4151d462e4a | 53758 | b5592fecb7afb30f1e22f865fe0a416dfd7dd9cc8b70319a7f6ad89cce6638bc |
| 2026-w47-en-nl | production/2026-w47/2026-w47-en-nl | 2331372 | 32e8baa51bf9260999812e6155113630717b2a4512430aef49d8465b758dc9c5 | 53736 | cbd9a008c530e127d6a446910443047e1df60092ed9e54ba0479b7a480696fe4 |
| 2026-w47-en-pt | production/2026-w47/2026-w47-en-pt | 2339582 | adc0a7e864dbd52c44273229b5cf804ac0e8282446b120a728aaeb01353bcdb6 | 54291 | 1b3ee4558a758ae55e2faf84daee3ad9a12bd912ff0cce5dfcef5db2e6da05c0 |
| 2026-w47-en-ru | production/2026-w47/2026-w47-en-ru | 2468694 | 8ded0e80780b33981cb31bf438c9ceb1ac804cc226f6aa985ae94507dbcca0ad | 62552 | 13e0e75ce382f9ed9ae4d390f95026febd92ed08d1689347302c623fa34351f5 |
| 2026-w47-en-zh-cn | production/2026-w47/core-en（core 兜底） | 2605509 | 9283d6e6baab5d276710362e88d4875228cfa1b47ae30e020ce6942dd11491c6 | 51573 | e271f6cbfc446ab4dd5580ea1f1222c34beac27a8eba95ee40ac9eca97fce24e |
| 2026-w47-en-zh-tw | production/2026-w47/2026-w47-en-zh-tw | 2701637 | cd585a52bc5772230d975bd4a305119563e3f07ebc0ccd80404f73c027e242de | 51321 | 63c7651e06e925927a2bcc97939418209657855c0073b8e0aac445f2bede8009 |

注：11 版 .md excerpt 全同（seed）；vol 4；week 2026-W47；publishedAt 2026-11-16。

## 写盘 + lint（c）

- 11 版 × 3 文件写入 `issues/2026-w47/<slug>/`；`node lint.mjs --write` OK。
- `node lint.mjs --require-pdf` RC=0：`OK: 412 editions, index.json is current`（412 = 此前 401 + 本 bundle 11）。
- 写盘后逐文件复核：11 个 issues/ PDF 与 .text.md 的字节数 + SHA-256 与上表渲染记录全部一致（22/22 OK）。

## Commit（d/e）

- Message（与原版一致）：`Add 2026-w47-en bundle (EN text · 11 natives)`
- **Commit SHA：`c7d8e804c3fa439b5fa4163005c971c6e31273cf`**
- `git show --stat HEAD`：34 files（33 个 issues/ 文件 + index.json），15049 insertions(+)，1 deletion(-)。
- `git ls-files issues/2026-w47/2026-w47-en-*`：33 个文件，11 版各 3 个。
- `git status --porcelain`：commit 后与基线相同（535 行 `??`，0 行 M/D/其他）。
- **未 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。

## Scratch 清理（f）

核实方法（沿用 de 家方法 + 一处补强）：枚举 51 个 en-target 候选目录共 9521 个文件，逐文件算 git blob SHA 并 `git cat-file --batch-check`（109 个 blob 与仓内对象相同）；按 basename 查 git index + goal tools 对照唯一脚本（.py/.sh/.ttf/.orig）。**补强**：对拟删目录的脚本再做内容级核查——发现 basename 法会漏判：`scratch-reproof2-w47-en/run_gates.sh` 的 basename 在 W46 生产目录里存在，但内容是 en 专用的第二轮重校驱动（写死 en 11 版路径），与仓内任何 blob 都不同，属唯一脚本，改判保留。另 `scratch-fix-en2` 未被首轮正则命中（`fix-en2` 后缀），人工补查发现 7 个唯一脚本，保留。

### 已删（3 个目录，合计约 150 MB）

目录内只有：已 commit 生产文件的同名副本（冻结轮次变体，其最终态已在仓内 `production/2026-w47/core-en/content*.py` 等跟踪文件中）、轮次日志（PROOF-NOTE/GATE-LOG）、渲染产物（.svg/.png/.jpg/.pdf）与校验输出（.json/.log/.txt），无唯一脚本（内容级核查确认：其余 .py 均为仓内跟踪文件的副本或已 superseded 变体）。

- scratch-proof-en（78M，62 文件）
- scratch-reproof-core-en1（72M，83 文件）
- scratch-reproof-w47-en（0.4M，55 文件）
- 删除后逐一复核：3 个目录均已不存在。`df` 仍显示 98G used（GB 取整，52G avail 未变；与 de 家情况相同）。

### 保留（上报协调员定夺）

- **47 个含唯一脚本的 en 家目录，约 5.7 GB**（首轮审计 45 个 + 改判保留的 scratch-reproof2-w47-en + 补查的 scratch-fix-en2；完整清单与每目录唯一脚本见 `scratch-audit-en.json`，注意审计脚本输出的“KEEP 45 个”未含这两者；另有下述 2 个单文件终态记录目录不含脚本，保留总数 49 个）：
  - scratch-d5-rebuild-en、scratch-delta-en-de/es/fr/it/ja/ko/nl/pt/ru/zh-tw（10 个）、scratch-en、scratch-en-fix2、scratch-fanout-en、scratch-fanout-en2、scratch-fix-core-en1、scratch-fix-en、scratch-fix-en-de1、scratch-fix-en-ru2、scratch-fix-en-zh-tw、scratch-fix-en2、scratch-gatefix-u201c-en、scratch-proof-en-de1/de2/es1/es2/fr1/fr2/it1/it2/ja1/ja2/ko/ko1/ko2/nl1/nl2/pt1/pt2/ru1/ru2/zh-tw/zh-tw1/zh-tw2、scratch-reproof-en2、scratch-verify-en。
  - 唯一脚本例：`creambox.py` / `creambox2.py` / `creambox_inside.py`、`tr_nl.py`、`make_textmd_w47.py`、`check_s11.py`、`keycheck*.py`、`sweep_*.py`、`run_gates_enru.sh`、`driver.sh`、`delta-build.sh` / `delta-gates.sh`、`LucernaDejaVuSans-*.ttf` / `LucernaNewsreader-Regular.ttf`（scratch-fanout-en2 内唯一字体文件）。
  - 建议后续处理：把唯一脚本先归档到 goal tools 或随仓工具目录，再删目录；或协调员确认这些轮次脚本已无复用价值后整批删除。本任务按指令未动它们。
- **scratch-reproof2-w47-en（2.2M，207 文件）**：含 en 专用 `run_gates.sh`（第二轮重校驱动，内容唯一）与 `PROOF-NOTE-2.md`（第二轮全量重校记录，结论 (a) CLEAN；终态核对报告引用它作为 10/11 版的核对依据）。
- **scratch-kit-edit-en（1 文件，EDIT-LOG.md）**：W2-26 KIT 编辑的唯一审计记录（en-ru WEEKLY-KIT.md L53 接受记录，改前/改后 SHA 与 diff 均只记于此）。
- **scratch-verify-en-final（1 文件，VERIFY-REPORT.md）**：en 家 §8.4 终态核对报告（11/11 VERIFIED CLEAN 的定稿结论，含 33/33 完整 SHA 对照表）。
- **非 en 家目录未动**：`scratch-fix-de-en1/en2`、`scratch-proof-de-en1/2/3`、`scratch-gatefix-de-en`（de 家）、`scratch-proof-*-en*` / `scratch-fix-*-en*`（其他家 en-native 版）、`scratch-webpdf-en-es-fr`（跨家）、`scratch-tools-creambox`（共享工具）、`scratch-assess-textmd-d6` 等。
- **本工单目录保留**：`scratch-insert-en/`（本日志 + `render_bundle.py` / `write_bundle.py` / `audit_scratch_en.py` / `manifest.json` / `rendered/` / `scratch-audit-en.json` / `lint-require-pdf.log`）。

## 附件（本目录）

- `render_bundle.py`（步骤 b 驱动）、`write_bundle.py`（步骤 c 驱动）、`audit_scratch_en.py`（步骤 f 审计驱动）
- `manifest.json`（11 版 pins）、`rendered/`（11 份渲染后 .md）
- `scratch-audit-en.json`（51 个候选目录的审计明细）、`lint-require-pdf.log`（lint --require-pdf 原始输出）
