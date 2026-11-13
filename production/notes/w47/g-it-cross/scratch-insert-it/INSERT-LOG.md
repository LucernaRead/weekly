# INSERT-LOG — W47 it bundle（恢复协调员 #6 派单，步骤 4，第五家）

- 日期：2026-11-13 EST
- 方法：import 原版 `tools/insert.py`，用原版 `render_md` 渲染/校验，按 `main_bundle` (c)–(e) 复现，只跳过 clean-tree 检查与 push。commit only，绝不 push。
- 驱动脚本：`scratch-insert-it/render_bundle.py`（渲染表 `manifest.json`）、`write_bundle.py`（写盘+lint+commit）、核实脚本 `verify_scratch.py` + `scratch-verify.json`。

## 前置核对

- `df -h` 开工：/dev/mapper/rv 150G，已用 97G / 可用 53G（< 100G 停手线，可开工）。
- 仓库 `~/workspace/weekly-git` HEAD 开工前 = `fc6cda20b39bbb5fec303a39a0c9d5c9a249c3ef`（fr bundle commit，与派单一致）。
- `git status --porcelain` 开工前 = 535 行，全部为 `?? production/2026-w47/` 下已知渲染产物，无 M/D。
- index.json 开工前含 434 editions（de/en/es/fr 四家 44 版已入仓）。

## Seed excerpt 核实（步骤 b）

- W46 先例：`issues/2026-w46/2026-w46-it-en/2026-w46-it-en.md` 的 excerpt =
  “Mercoledì 11 novembre è San Martino: secondo il proverbio, «a San Martino ogni mosto diventa vino». Si aprono le cantine, si assaggia il vino nuovo e si mangiano le castagne: è l'estate di San Martino, tre giorni di sole dopo il primo freddo.”
  与 W46 it-en `.text.md` P1 导语段前两个完整句逐字一致 → 规则成立：excerpt = P1 导语段前两个完整句。
- W47 core-it P1 导语段前两句：
  “La Lazio è ancora prima: dopo il pareggio 1–1 a Napoli, la prima della classe ha 29 punti ed è ancora imbattuta. L'Inter vince 2–0 con il Como e sale a 28 punti, la Roma batte 3–0 il Sassuolo e arriva a 27.”
- 交叉核对 `production/covers/2026-w47/cover.json` stories.it.excerpt = 第一句（同源、更短）；headline “La Lazio resta in vetta: Inter e Roma inseguono” 与 P1 标题一致。实质一致，采用上述两句为 seed excerpt。exercises = 150。
- it-zh-cn 版目录：`production/2026-w47/2026-w47-it-zh-cn` 不存在，按 `resolve_bundle_dir` core 兜底取 `production/2026-w47/core-it`（内含 `2026-w47-it-zh-cn.text.md` + `ABSTRACT.txt` + `La-Lucerna-VOL4-web.pdf`）。

## 渲染表（11 版，全部 fail-fast 通过，sibling=(seed)）

| slug | web PDF 字节数 | web PDF SHA-256 | text.md 字节数 | text.md SHA-256 |
|---|---|---|---|---|
| 2026-w47-it-de | 1218051 | 13414d0fbe1b6c0317dc84400926f61b05fcc199b40d2f0c5548aaea9eb453de | 56634 | 27f58fca0f3957476c1f2b4da8b9df2c3b668b02b8ece3a5edbff1f35e1dd5b1 |
| 2026-w47-it-en | 1215698 | e071a54f8f30872891fe0cc11580e3068413a43da32aefbe510a396706f1c6eb | 55126 | a4d863d961804993d53f53029b79484913ddf341a5520cda3e4476568db3fec1 |
| 2026-w47-it-es | 1216301 | c40c7a0067bd338134dbb56a830f4f13bc7391f93c58c78183c5e367fefb2397 | 56214 | e19cf39d5ef64ce40c87c33208807c607300546d0ba0fc669b9f851e15bf40fc |
| 2026-w47-it-fr | 1215747 | d08db2eb54b2b9929de7c2bfa8c66289e5887305941ae7568faddc6a10437158 | 56524 | b4d1ec47ff3a94685f149bb137d356e64df447d58857c086f1e6db8b63f13ac8 |
| 2026-w47-it-ja | 1697338 | e035db45098e72d99f551fea7f4bf451ed73b2c2610039c045fd571bee7fc413 | 58209 | 3dafa38c8b404d928d7cd9a16e82ac20e311f3feda977a892d8c5d4b937f0d73 |
| 2026-w47-it-ko | 1484256 | 7419a5a624e58c79d7eb96b3d91c23ea0ee7d486a88cb722494848be500796f5 | 57349 | c37668224de79c74dd1fa2707a6e6e496cb94807010d12ea36f7c66144f002e7 |
| 2026-w47-it-nl | 1213994 | 8fc2d76c044ad79d40408fa612953692813747a292d87472d1c5300051d9bda0 | 55535 | 92ddd5838d6fad7c6e8caf363ae4878cbd25aac9f95068cd60b1d805409e676c |
| 2026-w47-it-pt | 1218997 | a6e7e83654661ab214114a2d861e0815b004ea6008f7f3004f7a4a8952a54213 | 55736 | 03cc7389d3edf66c9c580d18e1169f4bf82e398ec772f22df48d4c692d8b8f0a |
| 2026-w47-it-ru | 1361661 | ce75a0349c3e62b0631a8beb2c8fa9366608cec4c69d66da56be31cd7b3838af | 67662 | 28e906435b1f47dbb2f1b6238b49b9c91061a292e458d07cf63cd132cb8fe9f2 |
| 2026-w47-it-zh-cn | 1546116 | 393e65473a1c28a79542395de67381a71cbe3bf9eebb34b027c7179958a1cf8f | 52677 | 24b37ae72af304dd55b4e2ce9b56e6e5552ebc766f19a997193fdb2b8a6cc3d9 |
| 2026-w47-it-zh-tw | 1640999 | 133b04d123f18825bc9c91f9409740ce84eb22bc340ba027d5e9aed750f0139e | 52588 | 1ae5edf7b167d6d9ff263072bca34ba464c95949582017f85fd5a354fbcc4d43 |

- 抽查一版 frontmatter（it-en）：vol 4，week 2026-W47（2026-11-16–2026-11-22），exercises 150，pages 8，publishedAt 2026-11-16，excerpt = seed。

## 写盘 + lint + commit

- 写盘：11 版 × 3 文件（`.md` / `.text.md` / `.pdf`）进 `issues/2026-w47/<slug>/`；`node lint.mjs --write` 一次；`node lint.mjs --require-pdf` RC=0，输出 `OK: 445 editions, index.json is current`（无本 bundle slug 报错）。
- commit（本地，未 push）：`2fadcc32b8d14cbb251995dec26f705e12824a22`
- message：`Add 2026-w47-it bundle (IT text · 11 natives)`（与原版 `main_bundle` 格式一致）
- 核实：`git show --stat HEAD` = 34 files（33 个 issues/ 文件 + index.json）；`git status --porcelain` 仍为 535 行，全部 `?? production/2026-w47/`，无 M/D；`git ls-files issues/2026-w47/2026-w47-it-*/` = 33 个文件全部入 index；index.json 现含 445 editions（434 + 11）。
- **绝不 push**：未跑 `push_with_verify` / `git push` / `ls-remote`。

## Scratch 清理（步骤 f）

- 核实方法：`verify_scratch.py` 逐文件比对——与仓库内文件（`production/2026-w47`、`issues/2026-w47`、`tools/`、`production/covers/2026-w47`，共 13382 文件）同名同大小同 SHA 者记 IN_REPO；其余按 SCRIPT / REPORT(.md) / DIFF / DATA(.json 等) / RENDER / LOG / PYC 分类。仅当目录内无 SCRIPT、REPORT、DIFF、DATA 且无断链时才可删。注：核实脚本第二版 `total` 计数有 bug（各目录显示 0.0MB），但 counts/verdict 不受影响；目录总大小以开工前 `du` 为准，约 5.4G。
- it 家（target=it）候选目录共 70 个，合计约 5.4G。核实结果：**0 个可删，70 个全部保留**——每个目录都含唯一脚本、审计报告（RUN-LOG / VERIFY-REPORT / PROOF-NOTE / FIX-LOG / EDIT-LOG.md）、.diff 补丁记录或未匹配的审计 json，一律保留，130 齐后统一收割归档。
- **已删：无（0 个，0 MB）。**
- **释放空间：0 MB**（删除前后 `df -h` 均显示 97G 已用 / 53G 可用）。
- **保留（70 个，约 5.4G）：** scratch-d5-it、scratch-d5-rebuild-it、scratch-fanout-it、scratch-fix-core-it-d2、scratch-fix-core-it1、scratch-fix-it、scratch-fix-it-de1、scratch-fix-it-en1、scratch-fix-it-en1r2、scratch-fix-it-es1、scratch-fix-it-ru1、scratch-fix-it-ru2、scratch-fix-it-table、scratch-fix2-w47-it、scratch-gatefix-it-edge、scratch-gatefix-it-ru、scratch-gatefix-u201c-it、scratch-inventory-it-patches、scratch-it、scratch-it-repair、scratch-it-ru-spacing、scratch-it-ru-spacing2、scratch-proof-core-it3、scratch-proof-it、scratch-proof-it-de1、scratch-proof-it-en1、scratch-proof-it-en2、scratch-proof-it-es1、scratch-proof-it-fr1、scratch-proof-it-ja1、scratch-proof-it-ko1、scratch-proof-it-nl1、scratch-proof-it-pt1、scratch-proof-it-ru1、scratch-proof-it-zh-tw1、scratch-proof2-it-de1、scratch-proof2-it-en1、scratch-proof2-it-es1、scratch-proof2-it-fr1、scratch-proof2-it-ja1、scratch-proof2-it-ko1、scratch-proof2-it-nl1、scratch-proof2-it-pt1、scratch-proof2-it-ru1、scratch-proof2-it-zh-tw1、scratch-refanout-it、scratch-refanout-it2、scratch-reproof-core-it-d2、scratch-reproof-it-de1、scratch-reproof-it-en1、scratch-reproof-it-ru1、scratch-reproof-it2-de、scratch-reproof-it2-en、scratch-reproof-it2-es、scratch-reproof-it2-fr、scratch-reproof-it2-ja、scratch-reproof-it2-ko、scratch-reproof-it2-nl、scratch-reproof-it2-pt、scratch-reproof-it2-ru、scratch-reproof-it2-zh-tw、scratch-reproof-w47-it、scratch-reproof2-w47-it、scratch-reproof3-w47-it、scratch-verify-it、scratch-verify-it-final、scratch-verify-it-final2。另本目录 `scratch-insert-it`（本次插仓日志与脚本）保留。
- 未碰：it 为 native 的他家目录（如 scratch-proof-en-it1、scratch-proof-de-it1、scratch-fix-es-it2、scratch-delta-en-it、scratch-webpdf-de-it-pt、scratch-ru-rebuild-it 等）及无 it 标记的目录——不属于 it 家；其中 scratch-delta-en-it、scratch-delta-nl-it、scratch-webpdf-de-it-pt 未纳入本次核实范围。
- 异常记录：scratch-it-ru-spacing 与 scratch-it-ru-spacing2 内各有一条断链 symlink（`2026-w47-it-ru`，指向已不存在的路径），已按保留项处理，未删除。
- 核实明细：`scratch-insert-it/scratch-verify.json`。
