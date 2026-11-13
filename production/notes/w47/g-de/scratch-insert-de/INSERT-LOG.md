# INSERT-LOG — W47 de bundle (2026-11-13)

Worker: 恢复协调员 #6 派单，步骤 4，第一家。commit only，绝不 push。
Repo: `~/workspace/weekly-git`，起始 HEAD `9c51e8bf`（13 笔 commit 已落地：封面 + 12 家生产源，未 push）。
Disk at start: 98G used / 150G (`df -h`); < 100G，继续。

## 方法（与原版 main_bundle 的偏差）

- 未跑原版 `main_bundle`：其开头的 clean-tree 检查会被树上 535 行 `??`（262 个 `*.pdf` + 131 个 `cards/` + 131 个 `svg/` + 11 个 ko `*.pre-d5`，均为渲染产物、必须留盘、绝不能 commit）触发而中止。
- 改为 import `tools/insert.py`，用原版 `render_md` / `resolve_bundle_dir` / `bundle_natives` 渲染，再按 main_bundle (c)–(e) 逐行复现，只跳过 clean-tree 检查与 push 两步。
- 补偿：`git add` 只加显式路径（index.json + 33 个 issues/ 文件）；commit 前后核对 `git status --porcelain`——与基线（`status-baseline.txt`，535 行 `??`）逐行相同，0 行非 `??`。
- `lint --write` 只跑了一次（步骤 c）。

## seed_excerpt 取法（已入仓先例推导，README 里无 seed 规则）

- W46 de 全 11 版 excerpt 完全相同：`Diese Woche spielt die Bundesliga nicht: Es ist Länderspielpause. Die deutsche Nationalmannschaft trifft am Freitagabend in Belgrad auf Serbien — und am Montag danach in Berlin auf die Niederlande.`
- 对照 W46 core-de P1 头条段：该 excerpt = 头条段前两个完整句（止于 `…auf die Niederlande.`，下一句 `Es geht ums Viertelfinale.` 不取）。
- W46 cover.json de excerpt 只取第一句（同源、更短），故 cover excerpt 与 md excerpt 不必逐字相等，只需同源。
- W47 验证：core-de P1 头条段前两句 = cover.json de excerpt，逐字相同：
  > Diese Woche ist die Bundesliga zurück: Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln. Anstoß ist um 20.30 Uhr in der Allianz Arena in München.
- 采用该句为 seed_excerpt（exercises 150，publishedAt = weekStart 2026-11-16，vol 4，8 页）。

## 渲染（b）：11/11 通过，均为 seed 模式（issues/ 里尚无 de 家 md）

| slug | edition dir | web PDF bytes | web PDF SHA-256 | text.md bytes | text.md SHA-256 |
|---|---|---:|---|---:|---|
| 2026-w47-de-en | production/2026-w47/2026-w47-de-en | 1510219 | 6e50a693d200fbb2beef36254b9f57266a325d9252fe6af5d315515e27b98f04 | 49975 | 6fb1fb37415bf055d52162bb9c213b271c08dba02f13256524cb3b87d78f2418 |
| 2026-w47-de-fr | production/2026-w47/2026-w47-de-fr | 1512524 | 22525742a6bbfdc13ab0bb8df86aabd2e3f4b9d5a3f49e682cfef930f029a0d3 | 50392 | 80f1a96deb470d0cb3c798df7602bcfb36919d1292fd7b4f6c24495ccae9fbf8 |
| 2026-w47-de-es | production/2026-w47/2026-w47-de-es | 1514482 | 8e27d9c5f9353327de68d70e06a45bd192662246d85080ecd0747d425203e6a8 | 50467 | ec37787fa1d5d9ec56d962bf10e0b864227799c5908c3df4dd98fc2e2d599369 |
| 2026-w47-de-it | production/2026-w47/2026-w47-de-it | 1508883 | 87c448ebbc7923ccc4d4b873436dffa6e78b4350ac0de05d48336c3006621d99 | 50058 | 96babe5753bf972378eed6ed6ae8b195b2164720106d608fbe4206e55c21f2cb |
| 2026-w47-de-pt | production/2026-w47/2026-w47-de-pt | 1514736 | bda89b7b21802e0faa789c05aba2215d9ebb4379ec461257790531f7b8fb3589 | 50158 | b1b6a7e20abd04a0adfa3d979920919749d3280bd128b9775003e31a330597ca |
| 2026-w47-de-nl | production/2026-w47/2026-w47-de-nl | 1507329 | 049a48c9145882998f873ea6a121f67c7d4acb15d9041b07784a48a21a5aa8d0 | 49770 | 7cee007495073fcd5c882f937b2595cf1b8c2dcc247fb21b07bbf39815ddc5f7 |
| 2026-w47-de-ru | production/2026-w47/2026-w47-de-ru | 1654623 | 38bd5b1a08d12653db85056424447e7f389018234da9ebc90462059f7b66d6c6 | 56774 | f768fb76cb70b3914db941a63985f3ec6578fa390e27fb42a9283998e8ca8d45 |
| 2026-w47-de-ja | production/2026-w47/2026-w47-de-ja | 1949457 | 579e4a2ac75ac8e57ea25f0db72ba805eb0af43ef74ba65fdda89edf5ba73d90 | 52154 | e32d3cb404865284c94bef09f44bbaf9fa32ae5f883ac8b92bc3dcc2f9aaee23 |
| 2026-w47-de-ko | production/2026-w47/2026-w47-de-ko | 1789538 | ef851f6fa7d626a033b8dad4363272a78e0a4182c466be26b70cc16506ae33cc | 51730 | a8804776b2863a48b4ec09b1864ea074a3ddb7a9d61b39a3273fdcfdb83eb475 |
| 2026-w47-de-zh-cn | production/2026-w47/core-de（core 兜底） | 1861111 | 2d555df1209c10eeb54315f7ffda47bc787a763a8874b711116c5d18ac587eab | 49839 | a99c19716142773bbb25271cf5c18f724b4a7b722dd5dd6ba3800c3d8d7972c0 |
| 2026-w47-de-zh-tw | production/2026-w47/2026-w47-de-zh-tw | 1936175 | dd26b2ac11a5cd0ab35b07d6f39b8ac555b84cc0a687bc57d99f959369075122 | 49330 | 6865f9d835f17082f84bf500fc07211942d01a7c5520c87c298ceac74939ea6b |

注：`bundle_natives(de)` 的顺序为 en, fr, es, it, pt, nl, ru, ja, ko, zh-cn, zh-tw（`tables.ORDER`）。

## 写盘 + lint（c）

- 11 版 × 3 文件写入 `issues/2026-w47/<slug>/`；`node lint.mjs --write` OK。
- `node lint.mjs --require-pdf` RC=0：`OK: 401 editions, index.json is current`（401 = 此前 390 + 本 bundle 11）。
- 写盘后逐文件复核：11 个 issues/ PDF 与 .text.md 的字节数 + SHA-256 与上表渲染记录全部一致。

## Commit（d/e）

- Message（与原版一致）：`Add 2026-w47-de bundle (DE text · 11 natives)`
- **Commit SHA：`bc08bf04261c6314da7b7cb1d90b41ac39066dc3`**
- `git show --stat HEAD`：34 files（33 个 issues/ 文件 + index.json），13771 insertions(+)，43 deletions(-)。
- `git ls-files issues/2026-w47/2026-w47-de-*`：33 个文件，11 版各 3 个。
- `git status --porcelain`：与 commit 前基线逐行相同（535 行 `??`，0 行 M/D/其他）。
- **未 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。

## Scratch 清理（f）

核实方法：对 67 个 de-target 候选目录共 9985 个文件逐一 `git hash-object` + `git cat-file --batch-check`（仅 191 个 blob 与仓内对象相同）；再按 basename 查 git index 对照；最后按“是否含仓内无同名文件的唯一脚本（.py/.sh/.ttf/.orig）”分类。唯一脚本共 117 个（如 `creambox.py`、`tr_*.py`、`run_gates4.sh`、`gates-all4.sh`、`xcheck_answers.py`），只存在于 de scratch 里，repo 与 goal tools 目录均无——按“拿不准留着”规则保留其所在目录。

### 已删（22 个目录，合计 400 MB）

目录内只有：已 commit 生产文件的同名副本（.py/.sh，内容为已 superseded 的轮次变体）、轮次日志（FIX-LOG/GATE-LOG/PROOF-NOTE）、渲染产物（.svg/.png/.jpg/.pdf/.json）与校验输出（.md5/.sha256/.diff），无唯一脚本。

- scratch-de-fix3（8.0M）、scratch-de-fix4（48.0M）
- scratch-fix-de-fr2（58.5M）、scratch-fix-de-it-kit（0.2M）、scratch-fix-de-ja-ko1（59.7M）、scratch-fix-de-kit2、scratch-fix-de-ru2（29.7M）、scratch-fix-de-tren1、scratch-fix-de-trpt1
- scratch-gate-de-ru（27.2M）
- scratch-proof-de（23.3M）、scratch-proof-de-fr1（13.2M）、scratch-proof-de-ko1（19.4M）、scratch-proof-de-pt1（18.8M）、scratch-proof-de-pt2（19.3M）、scratch-proof-de-ru1（36.8M）、scratch-proof-de-zh-tw1（12.7M）、scratch-proof-de3（11.1M）
- scratch-reproof-w47-de（0.3M）、scratch-reproof2-w47-de（4.3M）、scratch-reproof2-w47-de-fix（4.8M）、scratch-reproof3-w47-de（1.7M）
- 删除后逐一复核：22 个目录均已不存在。`du` 合计 400 MB；`df` 仍显示 98G used（GB 取整，52G avail 未变）。

### 保留（上报协调员定夺）

- **45 个含唯一脚本的 de 家目录，约 2.7 GB**：scratch-d5-de、scratch-d5-rebuild-de、scratch-de、scratch-de-fix、scratch-de-fix2、scratch-fanout-de、scratch-fanout-de-rebuild-A、scratch-fanout-de-rebuild-B、scratch-fix-de、scratch-fix-de-en1、scratch-fix-de-en2、scratch-fix-de-es1、scratch-fix-de-kit1、scratch-fix-de-minor1、scratch-fix-de-pt-toolbox、scratch-fix-de-pt1、scratch-fix-de-toolbox-family、scratch-fix-de-vals1、scratch-fix-de-vals2、scratch-fix-de-vals3、scratch-fix-de-zh-tw-toolbox、scratch-fix2-w47-de、scratch-gatefix-de-en、scratch-proof-de-en1、scratch-proof-de-en2、scratch-proof-de-en3、scratch-proof-de-es1、scratch-proof-de-es2、scratch-proof-de-fr2、scratch-proof-de-it1、scratch-proof-de-it2、scratch-proof-de-ja1、scratch-proof-de-ja2、scratch-proof-de-ko2、scratch-proof-de-nl1、scratch-proof-de-nl2、scratch-proof-de-pt3、scratch-proof-de-ru2、scratch-proof-de-zh-tw2、scratch-proof-de2、scratch-proof-de4、scratch-proof-de5、scratch-reproof-de-round3（747M）、scratch-reproof-de-round4（336M）、scratch-reproof-de-round4b（331M）。
  - （核实：候选 67 个目录，已删 22 个、保留 45 个，保留合计 2779 MB；`scratch-reproof2-w47-de` 与 `scratch-reproof3-w47-de` 在已删清单内，不在保留清单内。）
  - 保留原因：各含 1–339 个唯一脚本（每目录清单见核查脚本输出逻辑；最大三家是 round3/round4/round4b 的 gates 驱动脚本 `run_gates*.sh` / `gates-all*.sh` / `xcheck_answers.py` 等）。其余内容多为已 commit 文件的副本与渲染产物，但整目录删会连带删掉这些唯一脚本。
  - 建议后续处理：把 117 个唯一脚本先归档到 goal tools 或随仓工具目录，再删目录；或协调员确认这些轮次脚本已无复用价值后整批删除。本任务按指令未动它们。
- **非 de 家目录未动**：`scratch-fix-en-de1` 等（target en）、`scratch-ru-rebuild-ru-de`（target ru）、`scratch-delta-*-de`、`scratch-scope-de2`、`scratch-webpdf-de-it-pt` 及 `probe-*.txt` 文件。
- **本工单目录保留**：`scratch-insert-de/`（本日志 + `render_de.py` / `write_commit_de.py` / `rendered.json` / `rendered-md/` / `status-baseline.txt`）。

## 附件（本目录）

- `render_de.py`（步骤 b 驱动）、`write_commit_de.py`（步骤 c–e 驱动）
- `rendered.json`（11 版 pins）、`rendered-md/`（11 份渲染后 .md）
- `status-baseline.txt`（commit 前 `git status --porcelain` 基线，535 行）
