# W47 zh-cn bundle — INSERT-LOG

- 派单：恢复协调员 #6，步骤 4，第十一家（zh-cn 家）
- 仓库：`~/workspace/weekly-git`；开始前 HEAD `c90f63136ab3557bd59dbe8a44632df28b674b13`（ru bundle commit）✓
- 磁盘：开始前 98G 已用（<100G，可开工）；结束后 98G（见末尾，未删 scratch，故无释放）
- 方法：import 原版 `tools/insert.py`，用原版 `render_md` 渲染/校验，按 `main_bundle` (b)–(e) 复现，只跳过 clean-tree 检查（树上 535 行 `??` 渲染产物须留盘、绝不 commit）与 push。commit only，绝不 push。
- bundle：zh-cn × 10 natives（de, en, es, fr, it, ja, ko, nl, pt, ru；排除 zh-tw，简繁不互插）
- exercises：150；vol：4；week：2026-11-16—22

## seed_excerpt 推导

W47 issues/ 里尚无 zh-cn 家 md，故 seed。取法与 de/en/es/fr/it/ja/ko/nl/pt/ru 家一致：

- W46 先例：`issues/2026-w46/2026-w46-zh-cn-en.md` 的 excerpt =
  「今年的双11，现货从10月12日就开始卖了。 京东10月12日晚上8点开始卖现货，淘宝和天猫10月20日晚上8点现货开售，现货一直卖到11月13日。」
  = W46 core-zh-cn P1 头条段前两个完整句（句间空格为 excerpt 惯例）。
- W47 core-zh-cn P1 头条「BLG赢了T1，决赛对阵GEN」首段前两句：
  「S16的半决赛打完了。」「11月8日星期日，GEN 3比0打赢了IG。」
- 交叉核对 W47 `production/covers/2026-w47/cover.json` stories.zh-cn.excerpt：
  「S16的半决赛打完了。11月8日星期日，GEN 3比0打赢了IG。11月9日星期一，BLG 3比1打赢了T1。决赛是BLG对GEN，北京时间11月15日星期日凌晨3点，在纽约的巴克莱中心打。」
  前两句与 seed 完全一致（仅句间空格差异），同源 ✓。（注：任务单称 cover.json“只取第一句”，实测 W47 zh-cn 的 cover excerpt 取的是整首段 4 句；W46 zh-cn cover excerpt 取前 3 句。无论如何，前两句一致，seed 采用无歧义。）
- 采用 seed_excerpt：`S16的半决赛打完了。 11月8日星期日，GEN 3比0打赢了IG。`

## 渲染结果（步骤 b，全部 fail-fast 通过，sibling 均为 (seed)）

| slug | web PDF 字节数 | web PDF SHA-256 | text.md 字节数 | text.md SHA-256 |
|---|---|---|---|---|
| 2026-w47-zh-cn-de | 2433265 | 31fffc7ff93c1436a44ad32761a8cfcd3c3275bb6c83b7f76480a164326475f5 | 50640 | e11d4f915226d3a252696c60641a1bfd4d0285ec464110858e599756d25d4b13 |
| 2026-w47-zh-cn-en | 2434914 | 2579a61027eb7b8be480e9d32353798a143a066b5fc5ae6bd625d50f9b5e8a07 | 49447 | 2aaf8992bbc20ebf1a0d7e652514ff0f345efd9e99e83e756779b777fd880521 |
| 2026-w47-zh-cn-es | 2428933 | 86df4f21287966b1f1b2a8566bbc6be081d96f16a0b7cc67e148b4aeda9e0717 | 51137 | b5bf366bad5f769616fdda577ee402cf2aa63e621b43e10669e97d690be9f7e7 |
| 2026-w47-zh-cn-fr | 2427467 | 638e9293509b75fdf19046c44726caea6789c1753197f4f326706e1606a295ac | 51785 | 4cf31ce982f657d7c648b20c80b6eb7dfae9d53e2fe7edeadc38a51a16c6bc5d |
| 2026-w47-zh-cn-it | 2423711 | 9aef40aa18ad7d1bb53db3bd5c3033d587c3a112f667e0f39a332419bcefea0a | 50924 | 808250dde25028d7d34d76c0bd6a4c657df28d8713d86829d463d881874390f4 |
| 2026-w47-zh-cn-ja | 2826131 | 21f0e9ba278cea69e2862ab7acd5a6f7781f0040160253ebd5c00ea75c3691bb | 52408 | b0fa1af51e9f841d7309070f6d9290de0c9590bac5739b5237ec38e9c4ae7883 |
| 2026-w47-zh-cn-ko | 2807966 | 68597c56beb09b01a243217b73fd7afbf065271e2106674fac414cd67273b656 | 52695 | 9f58f841635d07f2825a7ceeaf63494f98a11a8423dd81c1e882a4c8bb3dc0cf |
| 2026-w47-zh-cn-nl | 2426029 | fad4d6c11db0d2657864faecb5d098e9a66bda383644cea37bd5cd256ff95545 | 50025 | 79666191a8b5435549c244616133d62dbc12f1052e9de9bf642405ccb89a64c0 |
| 2026-w47-zh-cn-pt | 2430061 | bfc1a6e4b6bdd37dcb17272e319eb0f459e2fe9c00fececc066273650c962d09 | 50798 | 0c9d9d5b97aca7aec7c76fa436f4df9feb0bde02414dbda4a4634616e63f6a49 |
| 2026-w47-zh-cn-ru | 2557060 | 3e47f038c53b5b5f082f7f367fecd0bf3aa8eec1a174b2026689a3068292808c | 60498 | 1f11029b4e83fed3e52a9fa84c380836bca7da34632a30ab210faafe2536036d |

抽查 frontmatter（zh-cn-en）：title `VOL.4 · Simplified Chinese text · English explanations`，vol 4，week 2026-W47，weekStart 2026-11-16，weekEnd 2026-11-22，exercises 150，pages 8，pdfBytes/pdfSha256 与上表一致。

## 写盘 + lint（步骤 c）

- 写盘：`issues/2026-w47/<slug>/{<slug>.md, <slug>.text.md, <slug>.pdf}` × 10 版 = 30 文件。
- `node lint.mjs --write`：OK（只跑一次）。
- `node lint.mjs --require-pdf`：**RC=0**，`OK: 510 editions, index.json is current`（500 → 510）。
- 写盘前后 `git status --porcelain` 除 535 行已知 `??` 外无任何 M/D。

## Commit（步骤 d）

- message：`Add 2026-w47-zh-cn bundle (ZH-CN text · 10 natives)`（与原版一致）
- **commit SHA：`26466e69152fd85aa0da980e51f44ec6c2f5372d`**
- 核实：`git show --stat HEAD` = 31 files（30 个 issues/ 文件 + index.json）；`git ls-files issues/2026-w47/2026-w47-zh-cn-*/` = 30/30；`git status --porcelain` 仍只有 535 行已知 `??`，无其他内容。

## Push（步骤 e）

**未 push**：未跑 push_with_verify / git push / ls-remote。本地 commit 待协调员统一推。

## Scratch 清理（步骤 f）

- 清理前 df：98G 已用；清理后 df：98G 已用；**释放 0 MB**。
- **已删目录：无。**
- 原因：枚举 `hidden_files/w47/` 下 40 个 zh-cn 家顶层 scratch 目录（合计 4.6G），逐目录核查（见 `zhcn-classify.txt`，按可复现 KIT/渲染产物过滤后仍有非 KIT 文件）——**每一个目录都含有审计记录或唯一脚本**，按任务单“拿不准留着、审计记录一律保留、130 齐后统一收割归档”的规则，全部保留上报，不删：
  - 终态核对报告：`scratch-verify-zh-cn/VERIFY-REPORT.md`、`scratch-verify-zh-cn-final/VERIFY-REPORT.md`（16K）
  - KIT 编辑记录：`scratch-kit-edit-zh-cn/EDIT-LOG.md`（仅此 1 文件）
  - 独立校对记录：`scratch-reproof-w47-zh-cn/PROOF-NOTE.md`（仅此 1 文件）
  - 唯一脚本：`scratch-proof-zh-cn2/check2.py`（仅此 1 文件）
  - 其余 36 个目录各含 PROOF-NOTE.md / FIX-LOG.md / GATE-LOG.md / EDITION-RECORD.md / FANOUT-REPORT-zh-cn.md / RUN-LOG.md / RUN-SUMMARY.txt / 唯一 .py/.sh（如 gates.sh、gates-zhcn.py、keycheck.py、sweep.py、verify_pdf.py、verify150.py、textcheck.py 等）及 gate/freeze/occlusion/p8 日志。
- 保留目录清单（40 个，大小见 `zhcn-dirs-du.txt`）：
  - scratch-d5-zh-cn 264M；scratch-fanout-zh-cn 153M；scratch-fix-zh-cn 748M；
    scratch-fix-zh-cn-de1 74M；scratch-fix-zh-cn-es1 200M；scratch-fix-zh-cn-fr1 70M；
    scratch-fix-zh-cn-it1 120M；scratch-fix-zh-cn-ko1 115M；scratch-fix-zh-cn-nl1 70M；
    scratch-fix-zh-cn-pt1 137M；scratch-fix-zh-cn-ru1 79M；
  - scratch-proof-zh-cn 76M；scratch-proof-zh-cn-de1 105M；scratch-proof-zh-cn-es1 84M；
    scratch-proof-zh-cn-fr1 93M；scratch-proof-zh-cn-it1 86M；scratch-proof-zh-cn-ja1 85M；
    scratch-proof-zh-cn-ko1 89M；scratch-proof-zh-cn-nl1 96M；scratch-proof-zh-cn-pt1 95M；
    scratch-proof-zh-cn-ru1 85M；scratch-proof-zh-cn2 8.0K；scratch-proof-zh-cn3 77M；
  - scratch-reproof-w47-zh-cn 20K；scratch-reproof-zh-cn-de1 140M；scratch-reproof-zh-cn-es1 192M；
    scratch-reproof-zh-cn-fr1 199M；scratch-reproof-zh-cn-it1 123M；scratch-reproof-zh-cn-ko1 134M；
    scratch-reproof-zh-cn-nl1 231M；scratch-reproof-zh-cn-pt1 131M；scratch-reproof-zh-cn-ru1 134M；
    scratch-reproof2-w47-zh-cn 1.9M；
  - scratch-verify-zh-cn 500K；scratch-verify-zh-cn-final 16K；
  - scratch-zh-cn 327M；scratch-zh-cn-fix 364K；scratch-zh-cn-fix2 71M；
  - scratch-kit-edit-zh-cn 4.0K；scratch-insert-zh-cn 32K（本任务工作目录，含本日志）。
- 另注意：其他家族 scratch 内还有嵌套的 zh-cn 子目录（如 `scratch-runw-rerun-R3/zh-cn-ru`、`scratch-fix-de-minor1/2026-w47-de-zh-cn` 等），属他家 scratch/交叉工作范围，未动、未计入本次 40 个；130 齐后收割归档时需另行处理。
- 收割建议：130 齐后，先把各目录的审计记录（VERIFY-REPORT.md、EDIT-LOG.md、PROOF-NOTE.md、FIX-LOG.md、GATE-LOG.md、EDITION-RECORD.md、FANOUT-REPORT-zh-cn.md、RUN-LOG.md 及唯一脚本）收进仓库 `production/notes/` 再删目录。

## 本任务工作文件

- 本目录 `scratch-insert-zh-cn/`：`INSERT-LOG.md`（本文件）、`render_bundle.py`（复现驱动）、`render.log`、`write.log`、`rendered.json`（pins）、`lint-require-pdf.txt`、`commit-sha.txt`、`zhcn-dirs-du.txt`、`zhcn-inventory.txt`、`zhcn-classify.txt`
