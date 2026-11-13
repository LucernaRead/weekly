# W47 ru 家庭第三轮修复 FIX-LOG-3（PROOF-NOTE-3 的 H-1、H-2）

- 任务：只修 PROOF-NOTE-3 两条 low 发现（均为 G-4 同类、P1 栏目标题位置），别的什么都不动。
- 日期：2026-11-12（Thu）
- 前置已读：`scratch-reproof3-w47-ru/PROOF-NOTE-3.md`（H-1、H-2）；`scratch-fix2b-w47-ru/FIX-LOG-2b.md`（导出器干跑+回补流程）；`scratch-fix2c-w47-ru/FIX-LOG-2c.md`（构建驱动与门禁清单）。
- 范围：只动 `production/2026-w47/2026-w47-ru-it/` 与 `2026-w47-ru-pt/`（各 `content12.py` 一行、SVG p1、印/网 PDF、text.md、WEEKLY-KIT.md）与本 scratch 目录；不碰其他家庭、其他周；不 commit、不 push、不跑 lint、不改 SOP。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python` 全程（未用系统 python3）。
- 磁盘：开工 95G 已用、收尾 95G（门限 100G，全程未触发）。
- 工作文件：本目录 `apply3.py`（源头修改，断言计数）、`expected-{it,pt}.json`（backfill 预期替换）、`backfill3.py`（复用 2b 回补逻辑）、`driver.sh`（构建驱动，it/pt 各一跑）、`verify3.py`（印/网核验）、`gates3.sh`（门禁驱动）、`update_kit.py`（KIT 更新，断言计数）、`pre-2026-w47-ru-{it,pt}.text.md`（修前 text.md 快照）、`pre-{it,pt}-svg.sha256`（修前 SVG 快照）、`logs/`（run/render/textmd/backfill/webpdf 日志）、`gates/`（门禁日志/JSON）、`build-{it,pt}.log`、`summary-{it,pt}.txt`。
- 渲染：两版串行（RAM 紧张，单版一次）；render 一次即成，无需重试；未杀任何进程。

## 1. 源头改动：仅两处（各版一行）

### 1.1 依据

- 两版主导人称均为 tu（it：Leggi/scegli/Completa/Forma/Rispondi/Scrivi/Metti/Unisci；pt：Lê/escolhe/Completa/Forma/Junta/Escreve/Traduz/Responde；А ВЫ? 栏均已按 G-4 修为 `E TU?` / `E tu? …`）。
- P1 栏目标题的读者语部分偏离主导人称：it `TOCCA A VOI`（voi 全文仅此 1 处）、pt `AGORA VOCÊ`（você 全文仅此 1 处；同页下方 quiz 注已是 tu 体 `Lê a primeira página…`）。
- 俄语部分 `СЕЙЧАС ВЫ` 为正确的 вы 体，不动。
- 他版对照：ru-es `AHORA TÚ`、ru-fr `À VOUS`、ru-de `SIE SIND DRAN`、ru-nl `NU U` 各与其主导人称一致。

### 1.2 改动（`apply3.py`，每处断言旧串计数 1、新串原先 0，全部通过；仅该行变化，行号 54）

| 版 | 源文件 | 改前 | 改后 |
|---|---|---|---|
| ru-it（H-1） | `2026-w47-ru-it/content12.py:54` | `f.head("СЕЙЧАС ВЫ　TOCCA A VOI", 25)` | `f.head("СЕЙЧАС ВЫ　TOCCA A TE", 25)` |
| ru-pt（H-2） | `2026-w47-ru-pt/content12.py:54` | `f.head("СЕЙЧАС ВЫ　AGORA VOCÊ", 25)` | `f.head("СЕЙЧАС ВЫ　AGORA TU", 25)` |

- 仅改字符串的读者语部分；该行其他参数（字号 25）未动；俄语部分未动。
- `content12.py` SHA-256：it `466915dcea6d…` → `33616158bf82…`；pt `71adb8ddfe91…` → `ce4cd0ca63d7…`（全值见 §4）。

## 2. 重渲染记录（`driver.sh`，`logs/`、`build-{it,pt}.log`）

| 步骤 | ru-it（2026-11-12 19:55–20:01 UTC） | ru-pt（2026-11-12 20:01–20:07 UTC） |
|---|---|---|
| `run.py` | rc=0，TOTAL 150，zero FLOW OVERFLOW / HEAD TOO WIDE（`logs/it-run.log`） | rc=0，TOTAL 150，zero FLOW OVERFLOW / HEAD TOO WIDE（`logs/pt-run.log`） |
| `render.py` | rc=0；印 PDF mtime 2026-11-12 19:58:43 UTC，20,877,136 B（重建成功非仅返回码：mtime + SHA 逐项验，见 §4） | rc=0；印 PDF mtime 2026-11-12 20:04:44 UTC，20,883,723 B |
| `ru_textmd.py` 干跑 | rc=0（`/tmp/fix3-dryrun/`） | rc=0（`/tmp/fix3-dryrun/`） |
| `backfill3.py` | rc=0：干跑无丢行，落盘 diff 恰 L35 一行（`logs/it-backfill.log`） | rc=0：干跑丢 2 行标题（与 2b/F-2 同批，导出器 ≥24pt 规则 + D5 后缩字号所致），已原位置逐字回补——`### СМИ · O QUE DIZEM OS MEDIA`（pre L45–46，P1，`content12.py:73`，23pt）与 `### ЗА И ПРОТИВ · PRÓS E CONTRAS`（pre L448–449，P6，`content56.py:136`，22pt）；落盘 diff 恰 L35 一行（`logs/pt-backfill.log`） |
| text.md 落盘 | SHA `a46c6da64262…`，63,970 B（−1：VOI→TE）；diff vs 修前快照恰 1 行（L35） | SHA `93b60dc2d78d…`，65,110 B（−3：VOCÊ→TU）；diff vs 修前快照恰 1 行（L35） |
| `webpdf.py` | rc=0；网 PDF mtime 2026-11-12 20:01:37 UTC，3,330,610 B | rc=0；网 PDF mtime 2026-11-12 20:07:15 UTC，3,337,277 B |
| SVG 变动（vs 修前快照 `sha256sum -c`） | 仅 p1 变，p2–p8 不变 | 仅 p1 变，p2–p8 不变 |

- 附记：`run.py`/`render.py` 会重写全部 8 个 SVG 与 8 张 cards PNG 的 mtime；内容级比对（`sha256sum -c`）证明仅 p1 内容变化，p2–p8 字节一致——与 2b/2c 同一行为。

## 3. 印/网核验（`verify3.py`，全部 PASS）

- 印/网 PDF 各 8 页；印/网提取文字（归一化空白后）一致（it 37,583 字符；pt 37,887 字符——pt 较 2c 的 37,889 少 2 字符，即 `VOCÊ`→`TU` 的字符差）。
- 新串印/网计数：it `TOCCA A TE` ×1/×1（仅印 PDF P1）；pt `AGORA TU` ×1/×1（仅印 PDF P1）；旧串 it `TOCCA A VOI` / pt `AGORA VOCÊ` 印/网均为 0。
- `voi` / `você`（大小写不敏感）全版 0 处：text.md（`grep -ci` = 0）与印/网文字层均为 0。
- 未动标记仍在位（印 PDF）：it `E TU?` ×1、`СЕЙЧАС ВЫ` ×1（即修后标题的俄语部分）；pt `E TU?` ×1、`Lê a primeira página e escolhe a resposta certa` ×1、`Responde com a faixa` ×1、`E tu? Escreve duas frases` ×1。

## 4. 新旧 SHA 对照（盘上实测全值；网 PDF SHA 为本次重建实时值）

### ru-it

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-it.pdf` | `b83c981d399f25b647643d48ce2f70625e1b26f5ba3660d8e042f2144331d91a` | `dc1e476168578bd2e595a10df661a9f3b7b52a7aa56f7e79bbc84538567a7240` | 20,877,138 → 20,877,136 |
| 网 PDF `Lucerna-VOL4-ru-it-web.pdf` | `47201c0d411cc281ef974cce62004491890674dc0ac93b622b60708e4092e77f` | `6ea69cc772a60f6f9a733862f0ce8f2c38836bba2c030208df376f5f5c8f3077` | 3,330,609 → 3,330,610 |
| text.md `2026-w47-ru-it.text.md` | `ba59c4ff23683e51c5eeab362e190873eec03291c20b9b5ff291f9b8d614184e` | `a46c6da6426253c5e52c6124c10976ca5aa955d7f2db438995002b4e933f1434` | 63,971 → 63,970 |
| `content12.py` | `466915dcea6d5cbb2ebc97de447dff3a895125be5b34058588fe0bd286ad2920` | `33616158bf823095d24ac7b7f1c4391b4604cb2a166dfe995cf5cc98e14996e7` | — |

### ru-pt

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-pt.pdf` | `6ed8d2b9ba49798121b81ce1944e9f37c5e9f0c5152763ce813f1a1b69d04117` | `7624d63eec28dc6eaba2b41ada0cadd6c58743469fc42c0d51cb56093755db89` | 20,883,753 → 20,883,723 |
| 网 PDF `Lucerna-VOL4-ru-pt-web.pdf` | `f71d4e50cf40b4babc836acc5b2d12bb1b0230d2621d8107d3daedb0f139a9a8` | `a8773dcdbcdcd05d1397fbaf8136fb529945dd45f5ac1fa4b8e83241a1ba67b8` | 3,337,277 → 3,337,277 |
| text.md `2026-w47-ru-pt.text.md` | `00e972b717fb34055f76a435be87ba5fc51acbd9011ab34aba9eba373cbf5532` | `93b60dc2d78d1bd260660826585800a460d47d28ee45e7f6432096868e55ff53` | 65,113 → 65,110 |
| `content12.py` | `71adb8ddfe91efd5864f97ef5a3d96452173670207dbc534275ab1baee074446` | `ce4cd0ca63d7b7d0fc2928d39bc74d3e682247804219772e7ac0b525203ce4c7` | — |

改前 SHA 与 PROOF-NOTE-3 指纹逐一核对一致。KIT 已更新：两版 §5 印/网行（L53–54）改为上表改后实测值，§5 text.md 字节数同步为盘上实时值（it 63,970、pt 65,110；该行此前记 Fix 1 时的旧字节数，已随 G-4 等修复过期，本次一并校正）；§7 列表末追加补修 3 条目（源头改动、SVG 变动页、新旧 SHA、门禁结果）；历史条目一律未动。

## 5. 门禁（修后重跑，`gates/`，全部 rc=0）

| 门禁 | ru-it | ru-pt |
|---|---|---|
| `p8.py compare --total 150` | **CLEAN**：150/150，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 140]（E 节翻译题，预期） | **CLEAN**：同左 |
| `occlusion_audit.py`（svg/） | **0 flags** | **0 flags** |
| `boxtitle_check.py` | **0 DEFECT、0 OBSERVE、0 marginal**（55 标题、684 正文行） | **0 DEFECT、0 OBSERVE、0 marginal**（57 标题、683 正文行） |
| `spill_sweep.py` | **rc=0**（0 SPILL；1 条既有 `[observe]`：`ABOVE -23.91px` 的 Black Friday gloss 行 `= grande vendita.`，同 2b/2c，非新缺陷） | **rc=0**（0 SPILL；1 条既有 `[observe]`：同式 Black Friday gloss 行 `= grande saldo.`） |
| `pdf_edge_scan.py`（印 PDF） | **0 TOUCH、0 NEAR**（8 页） | **0 TOUCH、0 NEAR**（8 页） |
| `head_check.py`（vs 本次 run.log） | **PASS 0 defects** | **PASS 0 defects** |
| D5 census（`scratch-reproof2-w47-ru/census.py`，11 版全量） | **CJK+Latin=0、CJK+Cyrillic=0，全部 11 版**；本版弯引号 2 处全部 Newsreader（runs 5720） | 同左；本版弯引号 2 处全部 Newsreader（runs 5721） |
| 引号普查（`census_quotes.py`，本版 svg） | **GRAND TOTAL defective: 0** | **GRAND TOTAL defective: 0** |

## 6. 收尾核对

- 触碰范围：`production/2026-w47/2026-w47-ru-it/` 与 `2026-w47-ru-pt/`（各 `content12.py:54`、SVG p1、印/网 PDF、text.md、WEEKLY-KIT.md §5+§7）+ 本 scratch 目录；其余家庭/周、SOP、lint 均未碰；未 commit、未 push。
- 进程：本次构建为两版串行，无需杀进程；未杀任何进程。
- 磁盘收尾 95G 已用（门限 100G，未触发）。
- 干跑/终版中间件在 `/tmp/fix3-dryrun/`、`/tmp/fix3-final/`（临时件，VM 重启即失）；修前快照 `pre-2026-w47-ru-{it,pt}.text.md` 与 `pre-{it,pt}-svg.sha256` 留在本目录。
