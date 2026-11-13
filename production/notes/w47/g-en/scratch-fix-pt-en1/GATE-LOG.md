# GATE-LOG — 2026-W47 pt-en 第二轮返修（fix1，D-B1/D-B2）

- 返修员：fix1（第二轮返修）
- 时间：2026-11-11（EST）
- 对象：`production/2026-w47/2026-w47-pt-en/`（core-pt fix2 重建版，proof1 结论 (b) 返修）
- 解释器（全部）：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3；各工具 runtime 行自证）+ `pdftotext`/`pdftoppm`。`PYTHONDONTWRITEBYTECODE=1` 全程开启，`TMPDIR` 指向本 scratch `tmp/`。
- 全部日志与 JSON 在本目录（`run-fix2.log`、`render-fix2.log`、`webpdf-fix2.log`、`textmd-fix2.log`、`gates-fix2.log`、`occlusion-fix2.log` + `occlusion-fix2.json`、`p8-extract-fix2.log` + `p8-extract-fix2.json`、`p8-compare-fix2.log` + `p8-compare-fix2.json`、`keycheck-fix2.log` + `keycheck-150.json`、`freeze-baseline-ed-fix2.log` / `freeze-baseline-core-fix2.log`、`freeze-diff-fix2.log` + `freeze-diff-fix2.json`、`creambox-fix2.log`、`creambox-diag-fix2.log`、`boxtitle-fix2.log`、`boxtitle-trueink-fix2.log`、`sweep-fix2.log`、`check-final-fix2.log` + `en-textdiff.json` / `en-p8size.json`、`check-s11-fix2.log`、`verify-ed-fix2.log`、`minfont-fix2.log`、`orphan-sweep-fix2.log`、`print-fix2.txt` / `web-fix2.txt` / `print-fix2-p[1-8].txt` / `web-fix2-p[1-8].txt`、`render-copy-fix2.log` / `webpdf-copy-fix2.log` / `web-rerender-fix2.pdf` / `web-fix2-prod.txt` / `web-fix2-rerender.txt` / `print-rerender-fix2.txt`、`measure_candidates.log`、`gates-all-fix2.log`；渲染图在 `render/`（8 页印版 + 网版 P1/P8 + P1/P7 标题裁图）。

## 0. 身份（修前三 SHA 与任务书先验逐字一致；修后三件见 §16）

| 文件 | 修前（proof1 登记） | 修后（本轮返修） |
|---|---|---|
| 印刷 PDF `A-Lucerna-VOL4.pdf` | 12,932,439 B；`782e7cb9d9109f4282667fd6dde71ab981933fa5290a9cd4882aaa49322cca6d` | **12,932,441 B**；`7e235e4591c034815ed90bcc21cef48a3b40bb1eb39bb0ebb1c8f027fbcb2e42` |
| 网页 PDF `A-Lucerna-VOL4-web.pdf` | 1,139,921 B；`e02cf58cbee4cf5daac47fccc9319faf8158b6b31523ba220794f415a5e9bb61` | **1,139,917 B**；`aad718e1efccbbcf24f4a1d6ac05fbe1bc59bf3b431037384f5645896bd7fc6c` |
| 文字 `2026-w47-pt-en.text.md` | 37,333 B；`513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`；534 行 | **不变**（同 SHA、同字节数、534 行；重导 diff 0 行） |

## 1. 构建

| 步骤 | 结果 |
|---|---|
| `run.py`（版目录内） | rc=0；TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词）；FLOW OVERFLOW 0，HEAD TOO WIDE 0；REGISTRY STATS 重 dump（同上） |
| `render.py`（版目录内） | rc=0；印刷 PDF 12,932,441 B，8 页，1462.5×2025 pt |
| `webpdf.py`（版目录内） | rc=0；1,139,917 B；46,071 text bytes |
| `textmd.py` 再生 `.text.md` | rc=0；534 行；CJK 0；题号 150/150；与修前 `.text.md` **diff 0 行**（SHA 不变） |
| SVG 变化 | 仅 p1-capa（`164d2c52…`→`8d3e2875…`）与 p7-lingua（`3760e251…`→`7cb27481…`）两页哈希变；其余 6 页逐字节不变 |

## 2. 机械门

| 门 | 结果 | 证据 |
|---|---|---|
| `gates.py` | **16/16 PASS，FAILURES: none**（rc=0） | `gates-fix2.log` |
| occlusion 真实审计（非 `--selftest`） | **0 flags**（rc=0）；内置自检 6 类全触发、干净对照静默 | `occlusion-fix2.log`、`occlusion-fix2.json` |
| p8 extract | **150/150**（rc=0） | `p8-extract-fix2.log`、`p8-extract-fix2.json` |
| p8 compare vs 核心 | **CLEAN**，missing=[]，extra_count=0，keydiff=[137, 138]（预期，翻译题答案） | `p8-compare-fix2.log`、`p8-compare-fix2.json` |
| keycheck | **149/150**（rc=0）；唯一不符 #150（开放作文，提取为 `✓`，预期）；150 键与 proof1 提取逐字相同（diff=[]） | `keycheck-fix2.log`、`keycheck-150.json` |
| freeze baseline（版） | **8/8 byte-identical**（repointed files: none；核心 SVG 完整性通过） | `freeze-baseline-ed-fix2.log` |
| freeze baseline（核心对照） | **8/8 byte-identical**（`--build` 指 core-pt 构建目录、`--core-svg` 指 core-pt 的 svg 目录；核心 SVG 完整性通过，rc=0） | `freeze-baseline-core-fix2.log` |
| freeze diff（核心对照） | 新增 CJK 共 **9 个，全部 U+3000**（P1 2、其余每页 1）；新增汉字 0 | `freeze-diff-fix2.log`、`freeze-diff-fix2.json` |
| creambox（canonical `hidden_files/w47/tools/creambox.py`） | rc=0；0 溢出（真墨裁决见下行） | `creambox-fix2.log` |
| creambox 真墨裁决（diag，PIL） | 31 个 OWN 末行；真墨底余最小 **+2.1px**（P2 `Palmeiras–Flamengo clash`），其余 +4.8 及以上；**0 溢出**。canonical 版 `desc-clear` 有 6 处 −0.9~−1.1（P2/P3/P4/P5/P7 末行，如 `send them in.` / `culture.`）：系工具的 0.30×字号保守下行余量估计（基线余量仅 +5.1 时即为负），同行真墨底余为 +4.8/+4.9，修前亦然（proof1 diag 逐行相同，仅 P1 盒底 1220.2→1218.2 一处变——盒高减 2 所致），非溢出 | `creambox-diag-fix2.log`（与 proof1 `creambox-diag.log` diff 仅 P1 盒底/末行基线两行） |
| boxtitle 全版横向 PIL 真墨重扫 | **31/31 盒标题 0 溢出**；advance 口径最小余量 +15.1（D-B1），真墨最小余量 +15.5（D-B1）；其余 29 标题最小正余量 +22.2（与 proof1 相同） | `boxtitle-fix2.log`、`boxtitle-trueink-fix2.log` |
| sweep（盒外行/纯填充盒） | box-vs-hline **0**；bridges 20，orphans 0，widows 0 | `sweep-fix2.log` |
| check_final（print/web 文字层） | 页数 8/8；词数 print=web=**8,507**；**词多重集 diff 0**；P8 答案区最小字号 **9.75pt**（187 spans，1,543 词） | `check-final-fix2.log`、`en-textdiff.json`、`en-p8size.json` |
| print/web `pdftotext -layout` 字节比对 | 全文逐字节相同 **110,438 B**；逐页 8/8 相同（修前 110,367 B；+71 B 为 P1 盒高减 2 单位后 `-layout` 空格重排，词多重集 diff 仍为 0） | `print-fix2.txt`、`web-fix2.txt`、`print-fix2-p[1-8].txt`、`web-fix2-p[1-8].txt` |
| check_s11（pt-adapted §1.1） | **ALL §1.1/P8 CHECKS PASS**（rc=0，见 §3 说明） | `check-s11-fix2.log` |
| verify_ed（pt-en fix verification） | **ALL pt-en FIX VERIFICATIONS PASS**（rc=0；D1/D2/D3 存活 + D-B1/D-B2 修后值 + text.md 不变 + 150 键不变） | `verify-ed-fix2.log` |
| P8 最小字号（minfont.py，PDF 实测） | **9.75pt**，低于 9.75pt 0 处（n=375） | `minfont-fix2.log` |
| 孤儿标点全版重扫 | A（`:` 后接字母）**0**；B（行首孤儿标点）**0**；C（行末 `:`）6 处全为合法引导冒号；D（双空格）**0**；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，空白占位符固有格式；text.md 冒号后接字母 0 处；CJK 仅 U+FF5C ×6；U+2019 0 | `orphan-sweep-fix2.log` |
| 重渲比对（仅 scratch 副本 `build-copy-fix2`，已删） | 印 PDF 重渲 **SHA 与交付逐字相同**（`7e235e45…`）；网 PDF 重渲文字层与交付网 PDF **逐字节相同** 110,438 B；重渲印 PDF 文字层亦逐字节相同 | `render-copy-fix2.log`、`webpdf-copy-fix2.log`、`web-rerender-fix2.pdf`、`web-fix2-rerender.txt`、`print-rerender-fix2.txt` |
| D-B1/D-B2 修后 PIL 真墨 + 交付 PDF 像素双法复测 | 真墨：D-B1 墨迹右缘 1396.0、余量 **+15.5**；D-B2 墨迹右缘 1840.5、余量 **+21.5**（见 §4）。像素：交付印 PDF 渲染裁图 `render/crop-p1-title.png` 与 `render/crop-p7-title.png` 目视——两标题末字均在奶油盒内、留有余量 | `boxtitle-trueink-fix2.log`、`render/crop-p1-title.png`、`render/crop-p7-title.png` |

## 3. check_s11 / verify_ed 说明（无 pt 家族原版，须如实记录）

- `tools/` 下无 `check_s11.py` / `verify_ed.py`（已核实）；pt 家族各 scratch 亦无。en 家族的 `check_s11.py` 硬编码 core-en 与 `2026-w47-en-*` 的 SVG 文件名（p1-front.svg 等）及 en 专属 P8 串（`113. [A2] A. vote`、`WRITING`），无法在 pt-en 上运行；en 家族的 `verify_ed.py` 只验 en-core fix1 专属项（Q39/40 Ashes、SAY IT），亦无法移植。
- 本轮在 scratch 内写了两份 pt-adapted 等价脚本（同类检查口径，路径/文件名指向 core-pt 与 pt-en）：
  - `check_s11-pt.py`：纸色、色集、VOL.4/VOL.5 逐页计数、徽章矩形数与颜色多重集、P8 原始最小字号 13 单位（= 9.75pt 有效值）、P8 题号项、Q120 芯片（level 取自 `keycheck-150.json`）。**初版误植了 en-core 的 `(N)` 括号空白标记检查**（`(113)` 等 12 项 FAIL）；核查证实 core-pt 自身亦无任何 `(11x)`/`(14x)` 串——pt 家族 P8 的 Q113–120/Q145–149 是 `N.` 编号项 + `___` 空白（核心与本版均为 21 处），遂改为 pt 口径（编号项齐全 + 空白数与核心相等 21=21），重跑 **rc=0 全绿**。初版误报已在 `check-s11-fix2.log` 的定稿版中被更正版覆盖；误报原因与核查过程记于 FIX-LOG §7。
  - `verify_ed-pt.py`：D1/D2/D3 存活（源 + SVG + 旧形 0 处）、D-B1/D-B2 源字号 21 + SVG 真墨余量、text.md SHA 不变 + 534 行、p8 提取键与 proof1 逐字相同——**rc=0 全绿**。
- pt 家族亦无 `registry.json` 成品（core-pt、pt-de 均无 `dump_reg.py`/`registry.json`；en 家族的 `dump_reg.py` 是 en-core 专属脚本，输出写进 en 家族 scratch）。本轮 registry 重 dump 即 run.py 的 REGISTRY STATS（TOTAL 150）+ p8 extract 重 dump；未新建 `registry.json` 成品，不改版目录文件清单。

## 4. D-B1/D-B2 修后实测值

| 缺陷 | 位置 | 修前真墨右缘 / 盒右缘 | 修法 | 修后字号 | 修后真墨右缘 | 修后余量（真墨） | 修后余量（advance） |
|---|---|---|---|---|---|---|---|
| D-B1 | P1 `A SEMANA EM NÚMEROS　In numbers` | 1434.0 / 1411.5（−22.5） | (b) 23→21pt | 21 | **1396.0** | **+15.5** | +15.1（advance 右缘 1396.5；`boxtitle-fix2.log` 行 `right=1396.4 clear=+15.1`，title_w=389.4） |
| D-B2 | P7 `ERROS COMUNS　Common mistakes` | 1876.5 / 1862.0（−14.5） | (b) 23→21pt | 21 | **1840.5** | **+21.5** | +21.6（advance 右缘 1840.5） |

- 注：任务书称 D-B1 修前真墨 1433.0/−21.5；本次独立实测与 proof1 逐字一致（1434.0/−22.5），以实测值为准。
- 修法选型实测见 `measure_candidates.log`：22pt 两处均不满足 ≥+4（−3.5/+3.5）；21pt 为满足门槛的最小整数档。(a) 缩短副标题在 23pt 下 D-B1 `… Numbers` 仅 +3.5（不满足）、且须改措辞并波及 tables_en.py SEG 键；(c) 左移于 D-B1 不可行（需 ≥26 单位，标题起点将落到盒左缘 989.0 之外）。

## 5. D1/D2/D3 存活复验（修后逐项，`verify_ed-pt.py` + 渲染文字层）

| # | 修复 | 核实 | 结果 |
|---|---|---|---|
| D1 | P1 刊头标语 | `tables_en.py` 新标语 `The Portuguese that Brazil is reading` 在位；旧形 `The Portuguese Brazil is reading` 全版构建源 0 处；渲染 P1 文字层同值 | 存活 |
| D2 | P4 词表注 | `tables_en.py:36` `"冠军": "title"`；旧值 `champion` 0 处；渲染 P4 Note 行 `o título title` | 存活 |
| D3-56/57/58/102 | P8 注冒号 | 发货 `svg/p8-avaliacao.svg` 内 `3 &gt; 1: mais`、`5 &gt; 4: mais`、`16:30 &lt; 17:00: mais cedo`、`cair numa sexta-feira: falls on a Friday` 各 1 处；旧形 0 处 | 存活 |
| 全版冒号复扫 | `:` 后直接接字母 | 8 个 SVG + text.md 均为 **0 处** | 存活 |
| p8 键 | 150 键 | 新旧 p8 extract JSON 对比：**0 处差异**（noted_set 150/150） | 存活 |

## 6. 8 页逐页目视（交付印刷 PDF 全新渲染，110dpi；网版 P1/P8 抽查）

- P1：干净；D-B1 标题已回盒内（`crop-p1-title.png` 放大裁切：`In numbers` 末尾 `s` 在盒内，右侧留白清晰）。D1 标语单行完整；头条、数字盒、日程、目录、每周一词、快讯、Q1–10 均干净。
- P2：干净。Q11–28、PARA NÃO ERRAR、Note 框、日程四格均干净；中部大空白为核心版式。
- P3：干净。Q29–46、6 词 Note 框、Zumbi 图注（Parreiras 1927）均干净。
- P4：干净。D2 `o título title` 在版；OS FINALISTAS 数据盒、足球周表、截稿注（10 November）、Q47–64 均干净。
- P5：干净。Q65–82、Gary Todd 图注 CC0、五步计划均干净。
- P6：干净。Q83–100、时间线盒、图表（10+5=15）均干净；Note 框 `o chute a lucky guess` 在盒内。
- P7：干净；D-B2 标题已回盒内（`crop-p7-title.png` 放大裁切：`mistakes` 末尾 `s` 在盒内）。三级语法栏、4 条常见错误、每周一词、读者来信（披露逐字）、8 条金句、VOL.5 预告均干净。
- P8：干净。Q113–150 题面、徽章、G 对话、H 写作题与范文（88 词）、Mané Garrincha 图注、150 条答案注均干净；D3 四处空格在版。
- 网页 P1/P8（`web-p1-1.png`、`web-p8-8.png`）与印刷版内容一致；P1 标题修复在网版同见。

## 7. 观察项（不计缺陷）

- **O1** — canonical creambox.py 的 `desc-clear`（0.30×字号保守估计）6 处 −0.9~−1.1，见 §2 creambox 行裁决：真墨底余 +4.8/+4.9，修前亦然，非溢出。
- **O2** — 初版 `check_s11-pt.py` 误植 en-core `(N)` 括号空白标记致 12 项误报（见 §3）；已按 pt 实际结构（core-pt 自身亦无该标记）更正并重跑全绿；误报未进入任何门禁结论。
- **O3** — `textmd.py` 按其既有行为把 `en-textmd-diff.json` 写进共享机制目录 `scratch-fanout-pt/`（覆盖了重建版的同名文件）；内容为确定性输出（与重建版同口径：50 行 vs 核心，CJK 0），副本已另存本目录 `en-textmd-diff-fix2.json`。
- **O4** — `scratch-refanout-pt/FANOUT-REPORT-pt.md` §2 表格亦称 pt-en boxtitle "clear"，与 KIT §9 同源失实；该报告覆盖 10 个 pt 版、属共享重建报告，本轮只更正了 KIT 并在此记录，供协调员决定是否同步修订报告。
- **O5** — 仓库工作树本轮开工前已有大量他线改动（W43/W45/W46、W47 其他家族、`tools/` 等，`git status` 约 123 个已改文件 + 372 个未追踪项）；本轮源码与交付件只改了 `production/2026-w47/2026-w47-pt-en/` 内 7 个文件（`content12.py`、`content7.py`、`svg/p1-capa.svg`、`svg/p7-lingua.svg`、`A-Lucerna-VOL4.pdf`、`A-Lucerna-VOL4-web.pdf`、`WEEKLY-KIT.md`；text.md 被重导工具重写但字节相同）；`cards/*.png` 为 `render.py` 每轮重写的渲染缓存（p1/p7 随 SVG 变，其余未逐字节比对）；未 commit、未 push，未碰 core-pt 与其他版。

## 8. 结论（报事实，不作定稿决定）

- D-B1/D-B2 已在源头修复（字号 23→21pt），修后 PIL 真墨 + 交付 PDF 像素双法复测余量分别为 **+15.5 / +21.5**，全版 31 个盒标题 **0 溢出**。
- 其余全部机械门、150 键、8 页文字层、8 页目视均通过；D1/D2/D3 全部存活。
- 按 SOP §8.4，定稿须经新一轮独立全量校对零问题；本轮为返修自查，不作定稿结论。第二轮复校由协调员另派。
