# W47 de 家庭第二轮修复日志（SOP §8 校对-修复循环）

- 修复工人：subagent（de 家庭第二轮修复）
- 日期：2026-11-12
- 范围：**仅 de-zh-tw 一版**。其余 10 版（core-de + de-{en,es,fr,it,ja,ko,nl,pt,ru}）**未动**：未改任何源码、未重渲、未改 KIT、未改任何文件。
- 依据：`scratch-reproof2-w47-de/PROOF-NOTE-2.md`（第二轮独立重校：MAJOR 0 / MEDIUM 0 / low 1，即 R2-F1）；第一轮记录 `scratch-fix-de/FIX-LOG.md`（流程照抄）。
- 工具：全程 `~/workspace/weekly-git/tools/venv/bin/python`。不 commit、不 push、不跑 lint、不改 SOP。
- 磁盘：开工 95G 已用 / 150G（< 100G 门限），完工 95G 已用，未触发停手。
- 构建驱动：本目录的 `build_edition.py zh-tw`（`scratch-fanout-de/build_edition.py` 的逐字副本 + `tr_zh-tw.py` / `export_text_lang.py` / `stub_svg.py` / `stub_bslib.py`，日志写入本目录 `zh-tw/`，不覆盖 fan-out 日志）。

## 改前基线（盘上实测，与 PROOF-NOTE-2 一致）

| 文件 | 字节 | SHA-256 前 12 |
|---|---|---|
| text.md `2026-w47-de-zh-tw.text.md` | 49,291 | `c2d3f679b8c5` |
| 印 PDF `Die-Lucerna-VOL4-de-zh-tw.pdf` | 11,837,604 | `6658366039a8` |
| 网 PDF `Die-Lucerna-VOL4-de-zh-tw-web.pdf` | 1,938,383 | `9b83129c7472` |

## 修复内容（源头改动，仅 1 项）

- **R2-F1（low，de-zh-tw）**：P5 UND SIE 提示术语不一致，由第一轮 F1 修复引入——F1 照搬了 core zh-cn 的「降临节日历」，破坏了 zh-tw 本版主导术语「將臨期日曆」（本版其余 6 处：text.md L139「將臨期日曆（24 個小門）」、L349、L567、L585、L1185 答案 130 与 139；全版「將臨期」×14 对「降臨節」×1，仅 L613）。
- 改动：`production/2026-w47/2026-w47-de-zh-tw/content56.py` 两处（同一字符串，eh 高度公式与实际段落各一处）：
  - L53（eh wrap 公式）：`你會做降臨節日曆嗎？願望清單上寫了什麼？用德文寫兩個句子！` → `你會做將臨期日曆嗎？願望清單上寫了什麼？用德文寫兩個句子！`
  - L59（`p.para` 实际文本）：同上。
- 改的是讲解层源码，不是只改 text.md；改完重导出 text.md 并重渲。两词同为 5 字，P5 框高 eh 不变，无几何跟进修复。
- core-de（zh-cn）绝不动：核实 `core-de/content56.py`「降临节日历」×4 原样保留，core 目录无任何写入。

## 修复前后对照

| 位置 | 改前 | 改后 |
|---|---|---|
| `content56.py:53`（eh 公式内字符串） | 你會做**降臨節**日曆嗎？…… | 你會做**將臨期**日曆嗎？…… |
| `content56.py:59`（P5 提示段落） | 你會做**降臨節**日曆嗎？…… | 你會做**將臨期**日曆嗎？…… |
| text.md L613 | 你會做降臨節日曆嗎？願望清單上寫了什麼？用德文寫兩個句子！ | 你會做將臨期日曆嗎？願望清單上寫了什麼？用德文寫兩個句子！ |
| text.md 全版「降臨節」 | ×1（仅 L613） | **×0** |
| text.md 全版「將臨期日曆」 | ×5 | **×6**（L139/L349/L567/L585/L613/L1185 含答案 130、139 两处） |
| 印 PDF 文字层「降臨節」 | ×1 | **×0**；「將臨期日曆嗎」×1 |
| 网 PDF 文字层「將臨期日曆嗎」 | — | ×1 |

## 重渲记录

- `build_edition.py zh-tw`：**ALL GATES PASS**（DRIVER_RC=0），日志本目录 `zh-tw/`（`build.log` / `render.log` / `webpdf.log` / `verify.log` / `occlusion.log` / `p8extract.log` / `p8compare.log` / `freeze.log` / `export.log`）。
- run.py exit 0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE，TOTAL exercises 150；P1-headline flow ends 1554（与第一轮一致）；P8 battery ends col3 1000，P8 image height 140。
- verify.py：TOTAL 150、编号连续、SVG byte-identical、§1.1 style audit True、verbatim True、P8 floor True（min 9.94pt ≥ 9.75）。
- freeze diff exit 0：TOTAL added CJK 1335（第一轮 1328；+7 为本次术语换字本身——「將/期」等繁体字形与 core 简体字形码点不同，属内容改动，非路由变化）。
- chips 141（P1 10 / P2 15 / P3 18 / P4 15 / P5 18 / P6 18 / P7 12 / P8 35；P8 A2 22 / B1 13 / B2 0）；export 591 entries、150 exercises、42,286 chars。

## 导出器陷阱核查

- 干跑：`export_text_lang.py`（与驱动相同的 gloss 前缀 `註 — `、NOTE_WRAP full）导出到本目录 `dryrun/`，与盘上 text.md **字节一致**，与修前快照（`pre-textmd/`）diff **恰好 1 行（L613）**，真正丢行 **0**，creambox `### ` 标题 36 = 36（修前 36）。无须恢复任何行。
- 注：首次干跑误用了 gloss 键 `譯注｜` 作前缀，导致 5 行 gloss 前缀不符——为本人调用失误，驱动本身一直用 tr 值 `註 — `；以正确前缀重跑后干跑与盘上字节一致。盘上文件从未被错误干跑覆盖。
- text.md diff（修前 → 修后）只含本轮 1 项改动：L613 一行。

## 逐版门禁结果表（de-zh-tw，全绿）

| 门禁 | 结果 | rc |
|---|---|---|
| build_edition.py 全部门禁 | ALL GATES PASS（TOTAL 150；chips 141；export 591 entries；P8 min 9.94pt） | 0 |
| p8 compare `--core-dir core-de --edition-dir 2026-w47-de-zh-tw --target de --total 150` | CLEAN，150 noted，missing=[]、extra=0、uncertain=[]，keydiff [137,138,139,150]（预期） | 0 |
| occlusion_audit.py（含自检） | 自检 OK（6 类 planted 全部触发、干净对照静默）；**0 flags** | 0 |
| boxtitle_check.py | 48 titles，0 DEFECT，0 OBSERVE，1 marginal（见下） | 0 |
| spill_sweep.py | 32 boxes，98 candidates，**0 SPILL**（98 OBSERVE，框外正常邻近文本） | 0 |
| pdf_edge_scan.py | 8 页，**0 TOUCH / 0 NEAR** | 0 |
| head_check.py（build.log） | PASS，0 defects | 0 |
| D5 census（`scratch-d5-plan/mechanism/d5_census.py`） | PASS：D5_lat=0、D5_cyr=0、curly_in_cjk=0；curly_total=33 全部在 Newsreader | 0 |
| D5 census（patched schema，`census_patched.py`） | PASS，无路由回归（仅 run-split 抖动：P5/P7 curly 元素 6→5、21→20，字符数不变；P1/P8 elements ±2–4） | 0 |
| 印/网 PDF 页数 | 各 8 页 | — |
| 印/网提取文本 | default 模式逐字节一致（各 50,009 B）；raw 模式逐字节一致（各 48,959 B） | — |
| P8 答案 1–150 | 全有（p8 extract 150/150；P8 文字层含 `1.`–`150.` 全部编号，150. 为开放任务） | — |
| U+201C 普查 | text.md 直引号 `"` ×0、直单引号 `'` ×0；U+201C ×33、U+201E ×33（德文低引+高引，本版风格）、U+201D/U+2019 ×0；印 PDF 文字层 U+201C ×33、直引号 ×0；无新增直引号；U+FFFD ×0；`→` ×36 | — |

- boxtitle marginal 说明（接受并注明）：P7 `　工具箱` 标题，ink 右缘 1863.0 vs 框 1862.0，**+1.0px**，容差内；core 同版亦有相同 +1.0 marginal，第一轮 O2 / D5 / PROOF-NOTE-2 均已记为既往，非本次引入。

## KIT 更新后 SHA 表

- 脚本：本目录 `update_kit_fix2.py`（tools/venv python 运行；KIT 先备份到 `/tmp/kit-backup-zh-tw-fix2.md`）。
- §2 Deliverables 标签改为 "reproof fix round 2 rebuild, 2026-11-12; reproof fix rebuild superseded"；新增 "## §11 Reproof fix round 2 rebuild (2026-11-12)"。§10（第一轮）历史值原样保留。

| 文件 | 字节 | SHA-256（前 12 位） | 完整 SHA-256 |
|---|---|---|---|
| 印 PDF `Die-Lucerna-VOL4-de-zh-tw.pdf` | 11,836,876 | `615f0277ac4a` | `615f0277ac4a37cfb45625747ed69bcecb2e2f92ac49e1ce7c6733976c9f79d9` |
| 网 PDF `Die-Lucerna-VOL4-de-zh-tw-web.pdf` | 1,937,775 | `6064fe1ae05a` | `6064fe1ae05ad2d7f235fe4fef24dff2b329226772dd2cfee9dc7ffcc378b2f7` |
| text.md `2026-w47-de-zh-tw.text.md` | 49,291（42,286 chars，591 entries，150 exercises） | `7f49d6edac6e` | `7f49d6edac6ea97f58212ab90ed6feb00b8f5614a6c76fb37d3c596370e520e6` |

- 校验：新 SHA 完整值在 KIT 中出现；新 SHA12 各出现 2 次（§2 Deliverables 块 + §11 历史条目）；旧印 SHA12 `6658366039a8` 在 KIT 中仅剩 1 次（§10 第一轮历史条目）；§2 块内旧 SHA 0 次。网 PDF 文字层 50,009 B（与第一轮相同）。

## 未改动的 10 版

core-de、de-en、de-es、de-fr、de-it、de-ja、de-ko、de-nl、de-pt、de-ru：**只字未动**——未改源码、未重渲、未改 KIT、未改任何文件。本轮唯一改动的文件：`2026-w47-de-zh-tw/content56.py`（2 行同词替换）、重渲生成的 8 SVG / 两份 PDF / text.md、`2026-w47-de-zh-tw/WEEKLY-KIT.md`（§2 + 新增 §11）。

## 残留问题

无。
