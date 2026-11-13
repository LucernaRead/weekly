# INSERT-LOG — W47 fr bundle（恢复协调员 #6 派单，步骤 4，第四家）

- 日期：2026-11-13 EST
- 方法：import 原版 `tools/insert.py`，用原版 `render_md` 渲染/校验，按 `main_bundle` (c)–(e) 复现，只跳过 clean-tree 检查与 push。commit only，绝不 push。
- 驱动脚本：`scratch-insert-fr/render_fr.py`（渲染表 `render-table.json`，核实脚本 `verify_scratch.py` + `scratch-verify.json`）

## 前置核对

- `df -h` 开工：/dev/mapper/rv 150G，已用 97G / 可用 53G（< 100G 停手线，可开工）。
- 仓库 `~/workspace/weekly-git` HEAD 开工前 = `4c9bce8fb70422be36b87ae03911ed24e4d20ee2`（es bundle commit，与派单一致）。
- `git status --porcelain` 开工前 = 535 行，全部为 `?? production/2026-w47/` 下已知渲染产物，无 M/D。
- index.json 开工前含 423 editions（de/en/es 三家 33 版已入仓）。

## Seed excerpt 核实（步骤 b）

- W46 先例：`issues/2026-w46/2026-w46-fr-en/2026-w46-fr-en.md` 的 excerpt =
  “Lundi 9 novembre, le Sénat ouvre la discussion sur le budget de la Sécurité sociale pour 2027. Le texte arrive dans la version du gouvernement : le 23 octobre, les députés avaient rejeté la partie « recettes » par 115 voix contre 1, et la partie « dépenses » n'avait pas été examinée.”
  与 W46 fr-en `.text.md` P1 导语段前两个完整句逐字一致 → 规则成立：excerpt = P1 导语段前两个完整句。
- W47 core-fr P1 导语段前两句：
  “Dimanche 8 novembre, Carlos Alcaraz a battu Ben Shelton 7-6(5), 7-5, en finale du Rolex Paris Masters, à Nanterre. Le vainqueur remporte son premier titre à Paris, le neuvième en Masters 1000.”
- 交叉核对 `production/covers/2026-w47/cover.json` stories.fr.excerpt = 第一句（同源、更短）；headline “Alcaraz, roi de Paris : le Sénat tranche mercredi” 与 P1 标题一致。实质一致，采用上述两句为 seed excerpt。exercises = 150。
- fr-zh-cn 版目录：`production/2026-w47/2026-w47-fr-zh-cn` 不存在，按 `resolve_bundle_dir` core 兜底取 `production/2026-w47/core-fr`（内含 `2026-w47-fr-zh-cn.text.md` + `ABSTRACT.txt` + `La-Lucerna-VOL4-web.pdf`）。

## 渲染表（11 版，全部 fail-fast 通过，sibling=(seed)）

| slug | web PDF 字节数 | web PDF SHA-256 | text.md 字节数 | text.md SHA-256 |
|---|---|---|---|---|
| 2026-w47-fr-de | 1626804 | 4eb86abfa6eeb44ec96ad55c557cda2de04cf0132264789688f5d782d4b407cf | 46690 | 67148924c68e4cdecf10f5c7f0ceaf6946bc7a321b191088f7895585ab0d5234 |
| 2026-w47-fr-en | 1623186 | 271926332039bd32fec073a891d363864dff14bda76acd57e95c026596944a54 | 46280 | 4029e89a87ecb4a7e8e010fecfb20fb39645c319d72eb8001fbd6bb1c51dbf9e |
| 2026-w47-fr-es | 1622990 | ec297b7cee22ef22024a3b986150250a52c5513813a6ba4058398f0e2c6316b7 | 46808 | 53603c0693ecce198b4c66b3b2b1486c8562f94ec29804bd3f7e635c9be002c6 |
| 2026-w47-fr-it | 1619307 | 0e27ccb79bb9c4ef8bd9bb6efc3b3221daeaf224b557b24b2a5f988ab9d2fb88 | 46687 | 51f32dd4e288ba7c79f14411234fddb5542480adf5e569128c5b097133627dac |
| 2026-w47-fr-ja | 2021505 | 4249702230de8a3448d51aad3fa69fb080087543439688e7b9f2fdcd29d734ef | 47687 | fdf935955f1e3d6e67f4a4b8b64f4091a016ce59a2ae25959b3bce9645a69573 |
| 2026-w47-fr-ko | 1924132 | 00b0f37c9a4571da76e00cecce776ed05d06c42821567945290accfb0b9a3b9a | 47510 | b9e6af86a01eb23a1a4bf726d134f29fae80d43da83ff86df88ca079b62f601d |
| 2026-w47-fr-zh-cn | 1989709 | c024e0ad6061ad5a4c16f01e9acf71632dacbc8d30febe2cdf7d4d7a6f2c315a | 46553 | 5416a602158f7904da6bd2546eaac890ec8a8a2214e2e5772e2dcd59318aa56f |
| 2026-w47-fr-nl | 1621651 | 408379aee3776fbfea9e814e32371d7b459abb3c1f157ee2f2f3e1861eab21c3 | 46452 | c5ce799c2e4e99350e3286054029e4e05e4595bd300f873bd10d3baf5f9ec44f |
| 2026-w47-fr-pt | 1623461 | 88ece6e886a9c1f3802e0fc06a1b871c35c42136aa424d830fce06cd1a7edba8 | 46656 | b61fe3b3189dbc323b2837389480f10a2a89547e278ce5936426f9f8e1c674f2 |
| 2026-w47-fr-ru | 1774094 | 4acb91b39968307ab8b1f47a3f3ed20574668e64ed519743eb2b1fedd896d918 | 50693 | 69d348831b05b30a91f6497da0f455324ba4c50145ed7ed3b8ee4e8253cea12b |
| 2026-w47-fr-zh-tw | 2077328 | 3f66ddae87f4d5c726b38d67dff27962761d04a1b02a15c7a3d802476a9e9875 | 46129 | 659dc0c5d5afbfbbfda0a2e36867329eaac648d765c39247d0a9e2dd9ee63ff7 |

- 抽查一版 frontmatter（fr-en）：vol 4，week 2026-W47（2026-11-16–2026-11-22），exercises 150，pages 8，publishedAt 2026-11-16，excerpt = seed。

## 写盘 + lint + commit

- 写盘：11 版 × 3 文件（`.md` / `.text.md` / `.pdf`）进 `issues/2026-w47/<slug>/`；`node lint.mjs --write` 一次；`node lint.mjs --require-pdf` RC=0，输出 `OK: 434 editions, index.json is current`（无本 bundle slug 报错）。
- commit（本地，未 push）：`fc6cda20b39bbb5fec303a39a0c9d5c9a249c3ef`
- message：`Add 2026-w47-fr bundle (FR text · 11 natives)`（与原版 `main_bundle` 格式一致）
- 核实：`git show --stat HEAD` = 34 files（33 个 issues/ 文件 + index.json）；`git status --porcelain` 仍为 535 行，全部 `?? production/2026-w47/`，无 M/D；`git ls-files issues/2026-w47/2026-w47-fr-*/` = 33 个文件全部入 index；index.json 现含 434 editions（423 + 11）。
- **绝不 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。

## Scratch 清理（步骤 f）

- 核实方法：`verify_scratch.py` 逐文件比对——与仓库内文件（`production/2026-w47`、`issues/2026-w47`、`tools/`、`production/covers/2026-w47`，共 13349 文件）同名同大小同 SHA 者记 IN_REPO；其余按 SCRIPT / REPORT(.md) / DIFF / DATA(.json 等) / RENDER / LOG / PYC 分类。仅当目录内无 SCRIPT、REPORT、DIFF、DATA（且无未匹配的唯一文件）时才可删。
- fr 家（target=fr）候选目录共 49 个，合计约 3.4G。核实结果：仅 1 个目录可删，其余 48 个均含唯一脚本、审计报告（RUN-LOG / GATE-LOG / PROOF-NOTE / FIX-LOG / EDIT-LOG.md）、.diff 补丁记录或未匹配的审计 json，一律保留，130 齐后统一收割归档。
- **已删（1 个，约 11 MB）：**
  - `scratch-reproof2-w47-fr-fix`（11.3 MB）：11 个 `.txt` 文本抽取 + `diffs-vs-core.txt` 日志 + `png/` 下 6 张页面渲染图，全部可由已 commit 的 issues/ PDF 复现，无脚本/报告/diff/唯一数据。
- **释放空间：约 11 MB**（删除前后 `df -h` 粗粒度均显示 97G 已用 / 53G 可用）。
- **保留（48 个，约 3.4G）：** scratch-d5-fr、scratch-d5-rebuild-fr、scratch-fanout-fr、scratch-fix-core-fr4、scratch-fix-fr、scratch-fix-fr-family1、scratch-fix-fr-minor1、scratch-fix-fr-ru1、scratch-fix-fr-ru2、scratch-fix-fr-zh-tw1、scratch-fix2-w47-fr、scratch-fr、scratch-fr-fix、scratch-fr-fix2、scratch-fr-fix3、scratch-gate-fr-ru-final、scratch-kit-edit-fr（EDIT-LOG.md）、scratch-proof-core-fr4、scratch-proof-fr、scratch-proof-fr-de1、scratch-proof-fr-de2、scratch-proof-fr-en1、scratch-proof-fr-en2、scratch-proof-fr-es1、scratch-proof-fr-es2、scratch-proof-fr-es2-agent-9a032c34、scratch-proof-fr-it1、scratch-proof-fr-it2、scratch-proof-fr-ja1、scratch-proof-fr-ko1、scratch-proof-fr-nl1、scratch-proof-fr-nl2、scratch-proof-fr-pt1、scratch-proof-fr-pt2、scratch-proof-fr-ru1、scratch-proof-fr-ru2、scratch-proof-fr-ru3、scratch-proof-fr-zh-tw1、scratch-proof-fr-zh-tw2、scratch-proof-fr2、scratch-proof-fr3、scratch-proof-fr4、scratch-refanout-fr2、scratch-reproof-fr-ru1、scratch-reproof-fr-zh-tw1、scratch-reproof-w47-fr、scratch-reproof2-w47-fr、scratch-reproof3-w47-fr。另本目录 `scratch-insert-fr`（本次插仓日志与脚本）保留。
- 未碰：fr 为 native 的他家目录（如 scratch-proof-en-fr1、scratch-delta-en-fr、scratch-fix-es-fr1 等）及无 fr 标记的目录——不属于 fr 家。
- 核实明细：`scratch-insert-fr/scratch-verify.json`。
