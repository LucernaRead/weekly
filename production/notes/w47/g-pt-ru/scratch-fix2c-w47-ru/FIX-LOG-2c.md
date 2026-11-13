# W47 ru 家庭第二轮补修之二 FIX-LOG-2c（P1 注行最后一处 você 体残留）

- 任务：只修下述一处，其余什么都不动。
- 日期：2026-11-12（Thu）
- 前置已读：`scratch-fix2b-w47-ru/FIX-LOG-2b.md` §1（2b 明确记下 P1 注 `Leia a primeira página …`（`content12.py:149`，SVG-only）未动）；`~/workspace/weekly-git/AGENTS.md`（开工后按运行时提示补读；与任务一致：全程用 `tools/venv/bin/python`，未 commit、未 push、未跑 lint、未改 SOP）。
- 范围：只动 `production/2026-w47/2026-w47-ru-pt/`（`content12.py` 一行、SVG p1、印/网 PDF、WEEKLY-KIT.md）与本 scratch 目录；不碰其他家庭、其他周；不 commit、不 push、不跑 lint、不改 SOP。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python` 全程（未用系统 python3）。
- 磁盘：开工 95G 已用、收尾 95G（门限 100G，全程未触发）。
- 工作文件：本目录 `driver-pt.sh`（构建驱动）、`verify2c.py`（印/网核验）、`gates2c.sh`（门禁驱动）、`pre-2026-w47-ru-pt.text.md`（修前 text.md 快照）、`pre-pt-svg.sha256`（修前 SVG 快照）、`logs/`（run/render/webpdf 日志）、`gates/`（门禁日志/JSON）、`build-pt.log`、`summary-pt.txt`。
- 渲染：单版串行，无需杀进程；未杀任何进程。

## 1. 源头改动：仅一处

### 1.1 依据

- 本版主导人称为 tu（2b 已统一：`E tu? Escreve …`、L471 `Responde`、5 处指令行 `Completa/Forma/Junta`）。
- 最后一处 você 体残留是 P1 注行，只存在于 SVG 源、不进 text.md（text.md 全文 `grep -c Leia` = 0、`grep -c "Lê a primeira"` = 0），故此前 text.md 普查漏网。
- 同版内证：P2 注行 `content12.py:240`（`e.bridge`）已是 tu 体 `Lê a página 2 e escolhe a resposta correta.`（text.md L157 在位）。
- 他版对照：ru-fr `Lisez…` vous 体、ru-de `Lesen Sie…` Sie 体、ru-it `Leggi…` tu 体，各版均与其主导人称一致。

### 1.2 改动（断言计数 1，通过；仅该行变化，行号 149）

| 源文件 | 改前 | 改后 |
|---|---|---|
| `2026-w47-ru-pt/content12.py:149` | `p.text(NOTE_RIGHT, qy + 36, "Leia a primeira página e escolha a resposta certa　Respostas na página 8", 20, "sans", False, GREY, anchor="end")` | `p.text(NOTE_RIGHT, qy + 36, "Lê a primeira página e escolhe a resposta certa　Respostas na página 8", 20, "sans", False, GREY, anchor="end")` |

- 仅改字符串一处；该行其他参数（位置、字号 20、`sans`、GREY、`anchor="end"`）未动。
- `content12.py` SHA-256：`bec5db29067b519a3022b9167303247c783463747bc833c2ad824a54b52c27e5` → `1df2c3e78d8563bef0904561ecc99b613244f5c4cdbd2e339dbb89eea3a14ccf`。
- 附记：该行尾注释 `# fix1 R2-D2: anchor NOTE_RIGHT, string unchanged` 字面已过期（fix1 时字符串确实未变），本次按任务“只改该字符串一处”未碰注释；如协调员认为应改注释，另派一处小修。
- 未动：`Escolha múltipla`（题型标签名词，非命令式）——`content12.py` 内 9 处、text.md 内 55 处均在位。另核实：`ex()` 不渲染 `typ`（`bslib4.py:209` 只画 chip/题号/题干），故该标签在 PDF 文字层 ×0 属设计、非缺陷（见 §1.4 末的核验修正记录）。

## 2. 重渲染记录（`driver-pt.sh`，`logs/`，2026-11-12 19:24–19:25 UTC）

- `run.py` rc=0，TOTAL 150，zero FLOW OVERFLOW / HEAD TOO WIDE（`logs/pt-run.log`）。
- `render.py` rc=0；印 PDF mtime 2026-11-12 19:25:19 UTC，20,883,753 B（重建成功非仅返回码：mtime + SHA 逐项验，见 §3）。
- `webpdf.py` rc=0；网 PDF mtime 2026-11-12 19:25:40 UTC，3,337,277 B。
- text.md 未重导出（该行不进 text.md）：修后 diff vs 修前快照 **0 行**，SHA 不变 `00e972b717fb34055f76a435be87ba5fc51acbd9011ab34aba9eba373cbf5532`（65,113 B）。
- SVG 变动（vs 修前快照）：仅 p1 变，p2–p8 不变——与 P1 注行所在页一致。

## 3. 印/网核验（`verify2c.py`，全部 PASS）

- 印/网 PDF 各 8 页；印/网提取文字（归一化空白后）一致（37,889 字符）。
- 新串印/网计数：`Lê a primeira página e escolhe a resposta certa` ×1/×1；旧串 `Leia a primeira página e escolha a resposta certa` ×0/×0。
- 逐页：新串仅在印 PDF P1 出现 ×1，其余 7 页 ×0。
- 未动标记仍在位（印 PDF）：`E TU?` ×1、`Responde com a faixa` ×1、`E tu? Escreve duas frases` ×1、P2 注 `Lê a página 2 e escolhe a resposta correta.` ×1。
- 核验修正记录：初版 `verify2c.py` 曾把 `Escolha múltipla` 当作 PDF 文字层标记查（×0 导致 VERIFY FAIL）；查证 `bslib4.py:209 ex()` 后确认 `typ` 从不渲染进 SVG——该标签只活在 registry/text.md（text.md 55 处、源文件 9 处均在位），PDF 文字层 ×0 是设计而非缺陷，遂把该项改为源文件 + text.md 计数，复跑 ALL PASS。

## 4. 新旧 SHA 对照（盘上实测全值；网 PDF SHA 为本次重建实时值）

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-pt.pdf` | `34344b82815de7808a0307e9fe6d84aee874a369c298753b6e98fc74dab59992` | `6ed8d2b9ba49798121b81ce1944e9f37c5e9f0c5152763ce813f1a1b69d04117` | 20,883,686 → 20,883,753 |
| 网 PDF `Lucerna-VOL4-ru-pt-web.pdf` | `680702793672437cc43d22e247d0848911ebcd8708bdc682e1021d96def84264` | `f71d4e50cf40b4babc836acc5b2d12bb1b0230d2621d8107d3daedb0f139a9a8` | 3,337,241 → 3,337,277 |
| text.md `2026-w47-ru-pt.text.md` | `00e972b717fb34055f76a435be87ba5fc51acbd9011ab34aba9eba373cbf5532` | `00e972b717fb34055f76a435be87ba5fc51acbd9011ab34aba9eba373cbf5532`（不变） | 65,113 → 65,113 |
| `content12.py` | `bec5db29067b519a3022b9167303247c783463747bc833c2ad824a54b52c27e5` | `1df2c3e78d8563bef0904561ecc99b613244f5c4cdbd2e339dbb89eea3a14ccf` | — |

改前 SHA 与 FIX-LOG-2b §1.5 逐一核对一致。KIT 已更新：§5 印/网行（L53–54）改为上表改后实测值；§7 列表末追加补修 2c 条目（源头改动、内证与他版对照、SVG 变动页、新旧 SHA、门禁结果）；历史条目（Fix 1/Fix 2/D5/F-2/第二轮/补修 2b）一律未动。

## 5. 门禁（修后重跑，`gates/`，全部 rc=0）

| 门禁 | 结果 |
|---|---|
| `p8.py compare --total 150` | **CLEAN**：core/edition 各 150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 140]（E 节翻译题，预期） |
| `occlusion_audit.py`（svg/） | **0 flags**（selftest OK：planted classes 全触发，clean controls 静默） |
| `boxtitle_check.py` | **0 DEFECT、0 OBSERVE、0 marginal**（57 标题、683 正文行） |
| `spill_sweep.py` | **rc=0**（0 SPILL；1 条既有 `[observe]`：`ABOVE -23.91px` 的 Black Friday gloss 行，同 2b，非新缺陷） |
| `pdf_edge_scan.py`（印 PDF） | **0 TOUCH、0 NEAR**（8 页） |
| `head_check.py`（vs 本次 run.log） | **PASS 0 defects** |
| D5 census（`scratch-reproof2-w47-ru/census.py`，11 版全量） | **CJK+Latin=0、CJK+Cyrillic=0，全部 11 版**；本版弯引号 2 处全部 Newsreader |
| 引号普查（`census_quotes.py`，本版 svg） | **GRAND TOTAL defective: 0**（Newsreader U+201C×1、U+201D×1） |

## 6. 收尾核对

- 触碰范围：`production/2026-w47/2026-w47-ru-pt/`（`content12.py:149`、SVG p1、印/网 PDF、WEEKLY-KIT.md §5+§7）+ 本 scratch 目录；其余家庭/周、SOP、lint 均未碰；未 commit、未 push。
- 进程：本次构建为单版串行，无需杀进程；未杀任何进程。
- 磁盘收尾 95G 已用（门限 100G，未触发）。
- `git status` 显示 `production/2026-w47/2026-w47-ru-pt/` 整目录为 untracked（`??`）——为该克隆既有状态，非本次造成；按任务未 commit。
