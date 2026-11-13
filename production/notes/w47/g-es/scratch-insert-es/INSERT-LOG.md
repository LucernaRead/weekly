# INSERT-LOG — W47 es bundle (2026-11-13)

Worker: 恢复协调员 #6 派单，步骤 4，第三家。commit only，绝不 push。
Repo: `~/workspace/weekly-git`，起始 HEAD `c7d8e804`（en bundle commit）；de、en 两家 22 版已入仓（index.json 含 412 editions）。
Disk at start: 97G used / 150G (`df -h`); < 100G，继续。

## 方法（与原版 main_bundle 的偏差）

- 未跑原版 `main_bundle`：其开头的 clean-tree 检查会被树上 535 行 `??`（渲染产物、必须留盘、绝不能 commit）触发而中止。
- 改为 import `tools/insert.py`，用原版 `render_md` / `resolve_bundle_dir` 渲染，再按 main_bundle (c)–(e) 逐行复现，只跳过 clean-tree 检查与 push 两步。
- 补偿：`git add` 只加显式路径（index.json + 33 个 issues/ 文件）；commit 前后核对 `git status --porcelain`——commit 前仅 ` M index.json` + 535 行 `??`（+11 个新 issues/ 目录 = 547 行）；commit 后回到 535 行 `??`，0 行 M/D/其他。
- `lint --write` 只跑了一次（步骤 c）。未跑 `push_with_verify` / `git push` / `ls-remote`。

## seed_excerpt 取法（de/en 家已确立的方法，W46 先例验证）

- W46 es-en excerpt（已入仓）：`España entra en su semana más intensa antes de las elecciones. El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.`
- 对照 W46 core-es P1 头条段：该 excerpt = 头条段前两个完整句（下一句 `El domingo 29 de noviembre, España vota en elecciones generales.` 不取）。方法确认。
- W47 core-es P1 头条段前两句（`production/2026-w47/core-es/2026-w47-es-zh-cn.text.md`，折行拼接后）：
  > La campaña electoral empezó el viernes 13, a las 00:00, y dura quince días: hasta el viernes 27 de noviembre. El sábado 28 es la jornada de reflexión: un día de silencio, sin propaganda ni actos de campaña.
- W47 cover.json es excerpt 只取第一句（同源、更短）：`La campaña electoral empezó el viernes 13, a las 00:00, y dura quince días: hasta el viernes 27 de noviembre.` 与 seed 第一句逐字一致。采用为 seed_excerpt（exercises 150，publishedAt = weekStart 2026-11-16，vol 4，8 页）。

## 渲染（b）：11/11 通过，均为 seed 模式（issues/ 里尚无 es 家 md）

| slug | edition dir | web PDF bytes | web PDF SHA-256 | text.md bytes | text.md SHA-256 |
|---|---|---:|---|---:|---|
| 2026-w47-es-de | production/2026-w47/2026-w47-es-de | 806895 | fd7edd4b84152439dd4a7458646f609cefb7c0380ce5f1b4d503528dee1819e7 | 45370 | ff0387066ca9ad21400cae865592e43ad24c029693a2e7883733e87440b57b6e |
| 2026-w47-es-en | production/2026-w47/2026-w47-es-en | 806124 | bb690dd25b6c822b9dd846b02163c747a7432d28f0c57a8b07363847ba64d204 | 45046 | 3c2ef9876638c384cd5c5b4288b55d2917e65756d1d431daf11a2474ad2a680b |
| 2026-w47-es-fr | production/2026-w47/2026-w47-es-fr | 805426 | 960de8cf8d3be5fda7e68e8bffef580f3733094a58e3b663817d8bef3aeb271a | 45834 | ad8bcbcd0c4fa340840baf16e3927bdd23363bf3478bf255c66da74d70ab45f5 |
| 2026-w47-es-it | production/2026-w47/2026-w47-es-it | 803822 | f533bb1aa13331a187ed26a4f7bf706b1db99ed7a1d79c3ed11689df345411a1 | 45211 | 491044bcfaab758cb49187d07f5aa19e16be568844867c8977a80583ee3d4755 |
| 2026-w47-es-ja | production/2026-w47/2026-w47-es-ja | 1280143 | 70d46e27721f49dcca24fc6b12bd6d27d5582d16ea46031e1c97c2674639ebf5 | 46578 | bab03d4d6c8af7dc4d160aafd89a0367f3132ffaade336b0666125ae0bf52cfb |
| 2026-w47-es-ko | production/2026-w47/2026-w47-es-ko | 1097497 | fad91509e34fdd2b2c41ac51737d728e328f2688a95064a8fdba6c39d28e7804 | 47403 | 8407be401bb75e89cadb678c40845ee38715dcdb00a912c9ffbacb6b7eac70cf |
| 2026-w47-es-nl | production/2026-w47/2026-w47-es-nl | 805809 | 8be3118b5080e616f5f92b03a792f56327c2ab3272e5fe7a3daa17a96a6107a3 | 45342 | d477656f5ef01f954068e4d002e424a16b3a872b911d22c3280c03feda911fd5 |
| 2026-w47-es-pt | production/2026-w47/2026-w47-es-pt | 804705 | 06514f66f69d41506810334604d2dcdf882e6ce1c72596cfdac16343b35fe35f | 45576 | 7db6b340f4f631b4aa2b3c3c596dbcba57aa39c8124d7b6905cc7a38f4f7ce2f |
| 2026-w47-es-ru | production/2026-w47/2026-w47-es-ru | 950846 | cc549a5a212afc4960038720aae88468041562f031b96ea81292c70033fb5551 | 52367 | ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b |
| 2026-w47-es-zh-cn | production/2026-w47/core-es（core 兜底） | 1162042 | f0f6ed1de57a12942d39ac864d1b74ac854301ddcba28e1c1a6e5b340424bd95 | 43789 | 9cc6462f702ceb49874d2eefc1254414887b7732dc35d139b9e4362f71fae254 |
| 2026-w47-es-zh-tw | production/2026-w47/2026-w47-es-zh-tw | 1265861 | 8871073245fdb336f634013e365369388196b064a998d7e307b4423a2f9e574e | 43818 | d26fdddc0fa69535e3eaf4384272834470f405c30a7c202c37d917e2817a1290 |

注：11 版 .md excerpt 全同（seed）；vol 4；week 2026-W47；publishedAt 2026-11-16。

## 写盘 + lint（c）

- 11 版 × 3 文件写入 `issues/2026-w47/<slug>/`；`node lint.mjs --write` OK。
- `node lint.mjs --require-pdf` RC=0：`OK: 423 editions, index.json is current`（423 = 此前 412 + 本 bundle 11）。
- 写盘后逐文件复核：11 个 issues/ PDF 与 .text.md 的字节数 + SHA-256 与上表渲染记录全部一致（22/22 OK）。index.json 内 es W47 版 11 个。

## Commit（d/e）

- Message（与原版一致）：`Add 2026-w47-es bundle (ES text · 11 natives)`
- **Commit SHA：`4c9bce8fb70422be36b87ae03911ed24e4d20ee2`**
- `git show --stat HEAD`：34 files（33 个 issues/ 文件 + index.json），20701 insertions(+)，1 deletion(-)。
- `git ls-files issues/2026-w47/2026-w47-es-*`：33 个文件，11 版各 3 个。
- `git status --porcelain`：commit 后与基线相同（535 行 `??`，0 行 M/D/其他）。
- **未 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。

## Scratch 清理（f）

核实方法（沿用 de/en 家方法 + 内容级补强）：枚举 52 个 es-target 候选目录共 7066 个文件，逐文件算 git blob SHA 并 `git cat-file --batch-check`（73 个 blob 与仓内对象相同）；唯一脚本判定用**内容级**（.py/.sh/.ttf/.orig 且内容 blob 不在仓内对象中、basename 不在 goal tools 内）——比 basename 法更严，可发现同名不同内容的脚本（如 en 家的 `run_gates.sh` 案例）。含 VERIFY-REPORT.md / EDIT-LOG.md 的目录强制保留。basename 法复核：拟删 6 家 basename-unique 脚本亦为 0。

### 已删（6 个目录，合计约 201 MB）

目录内只有：已 commit 生产文件的同名副本（.py 均与仓内 blob 内容一致）、轮次日志（PROOF-NOTE / GATE-LOG / FIX-LOG）、渲染产物（.png/.svg/.jpg/.pdf/.json/.diff/.log/.txt/.sha/.pyc）与校验输出，无唯一脚本（内容级 + basename 双重核查均为 0），无 VERIFY-REPORT.md / EDIT-LOG.md。

- scratch-fix-es-de1（14.2M，57 文件）
- scratch-proof-es（34.2M，54 文件）
- scratch-proof-es-de1（34.8M，102 文件）
- scratch-proof-es-en1（32.4M，100 文件）
- scratch-proof-es2（84.5M，128 文件）
- scratch-reproof-w47-es（1.2M，33 文件）
- 删除后逐一复核：6 个目录均已不存在。`df` 仍显示 97G used（GB 取整，52G avail 未变；与 de/en 家情况相同——实际释放约 201 MB）。

### 保留（上报协调员定夺）

- **46 个含唯一脚本的 es 家目录，约 1245.8 MB**（完整清单与每目录唯一脚本见 `scratch-audit-es.json`）：
  - scratch-d5-rebuild-es、scratch-es、scratch-fanout-es、scratch-fix-core-es1、scratch-fix-es、scratch-fix-es-fr1、scratch-fix-es-it2、scratch-fix-es-it3、scratch-fix-es-ko2、scratch-fix-es-ru2、scratch-fix-esru-f1、scratch-fix2-w47-es、scratch-fix3-w47-es、scratch-fix4-w47-es、scratch-fix5-w47-es、scratch-gatefix-u201c-es、scratch-proof-core-es3、scratch-proof-es-de2、scratch-proof-es-en2、scratch-proof-es-fr1、scratch-proof-es-fr2、scratch-proof-es-it1、scratch-proof-es-it2、scratch-proof-es-ja1、scratch-proof-es-ja2、scratch-proof-es-ko1、scratch-proof-es-ko2、scratch-proof-es-ko3、scratch-proof-es-nl1、scratch-proof-es-nl2、scratch-proof-es-pt1、scratch-proof-es-pt2、scratch-proof-es-ru1、scratch-proof-es-ru2、scratch-proof-es-zh-tw1、scratch-proof-es-zh-tw2、scratch-refanout-es、scratch-reproof-es-it3、scratch-reproof2-w47-es、scratch-reproof3-w47-es、scratch-reproof4-w47-es、scratch-reproof5-w47-es、scratch-reproof6-w47-es、scratch-reproof8-w47-esru、scratch-text-reexport-es、scratch-verify-es。
  - 唯一脚本例：`creambox.py` / `creambox_diag.py` / `boxtitle_core.py` / `keycheck_core.py`、`extract_text_es_*.py`、`sweep_de.py`、`gates_all2/3/4/5.sh`、`gates7.sh`、`cjk_audit*.py`、`freeze_direct*.py`、`key91*.py` / `keys137.py` / `p7geom.py` / `svgtext.py`、`commons_search.py` / `extract_text*.py`、`apply_fanout.py`。
  - 建议后续处理：把唯一脚本先归档到 goal tools 或随仓工具目录，再删目录；或协调员确认这些轮次脚本已无复用价值后整批删除。本任务按指令未动它们。
- **scratch-verify-es（24.7M，68 文件）**：含 es 家 §8.4 终态核对报告 `VERIFY-REPORT.md`（强制保留）与 `PROOF-NOTE-7.md`，另有 `gates7.sh`（唯一脚本）。
- **非 es 家目录未动**：`scratch-proof-*-es*` / `scratch-fix-*-es*`（其他家 es-native 版，如 de-es/en-es/fr-es/it-es/ja-es/ko-es/nl-es/pt-es/ru-es/zh-cn-es/zh-tw-es）、`scratch-delta-en-es` / `scratch-delta-nl-es`（en/nl 家）、`scratch-ru-rebuild-ru-es`（ru 家）、`scratch-webpdf-en-es-fr`（跨家）、`scratch-assess-textmd-d6`、`scratch-covers-pages`、`scratch-gates-rerun`、`scratch-inventory-families` 等共享目录，及 `probe-*.txt` 文件。`scratch-fix-esru-f1` / `scratch-reproof8-w47-esru` 按 es-target 候选审计，含唯一脚本（`gates-fix.sh` / `gates-r8.sh`），已保留。
- **本工单目录保留**：`scratch-insert-es/`（本日志 + `render_bundle.py` / `write_bundle.py` / `audit_scratch_es.py` / `manifest.json` / `rendered/` / `scratch-audit-es.json` / `lint-require-pdf.log`）。

## 附件（本目录）

- `render_bundle.py`（步骤 b 驱动）、`write_bundle.py`（步骤 c 驱动）、`audit_scratch_es.py`（步骤 f 审计驱动）
- `manifest.json`（11 版 pins）、`rendered/`（11 份渲染后 .md）
- `scratch-audit-es.json`（52 个候选目录的审计明细）、`lint-require-pdf.log`（lint --require-pdf 原始输出）
