# GATE-LOG — 2026-W47 pt-en 第二轮复校（re-proof，SOP §8.4）

- 校对员：re-proof（独立复校；与 pt-en 重建者、proof1 校对员、fix1 返修员均不同人）
- 时间：2026-11-11（EST）
- 对象：`production/2026-w47/2026-w47-pt-en/`（fix1 重建版，VOL.4）
- 解释器（全部）：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3；各工具 runtime 行自证）+ `pdftotext`/`pdftoppm`。`PYTHONDONTWRITEBYTECODE=1` 全程开启，`TMPDIR` 指向本 scratch。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-en1/`。`run.py` / `render.py` / `webpdf.py` / keycheck 只在 `build-copy/` 内运行；版目录只读（开工 47 文件 SHA 快照 `prod-snapshot.sha256`，收工复核见 §12）。
- 全部日志与 JSON 在本目录；渲染图在 `render/`。

## 0. 身份（与任务书先验逐字一致）

| 文件 | 字节 | sha256 |
|---|---|---|
| 印刷 PDF `A-Lucerna-VOL4.pdf` | 12,932,441 | `7e235e4591c034815ed90bcc21cef48a3b40bb1eb39bb0ebb1c8f027fbcb2e42` |
| 网页 PDF `A-Lucerna-VOL4-web.pdf` | 1,139,917 | `aad718e1efccbbcf24f4a1d6ac05fbe1bc59bf3b431037384f5645896bd7fc6c` |
| 文字 `2026-w47-pt-en.text.md` | 37,333（534 行） | `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed` |

- 探针：`/dev/null` 存在（crw-rw-rw-）；仓库内 `git hash-object -w --stdin` 成功（`9daeafb9…`，rc=0）。注：首次在 `~` 下直接跑因不在 git 仓库内报 `fatal: not a git repository`（rc=128）；改在 `~/workspace/weekly-git` 内重探即通，未硬锤。

## 1. 构建

| 步骤 | 结果 |
|---|---|
| `run.py`（`build-copy/` 内） | rc=0；TOTAL 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；范文 88 词）；`OVERFLOW`/`TOO WIDE` 出现 0 次；末行 `ALL DONE`（`run-rebuild.log`） |
| 重建 SVG vs 发货 SVG | **8/8 字节一致**（`rebuilt-svg-sha.txt` vs `shipped-svg-sha.txt`；p1 `8d3e2875…`、p7 `7cb27481…` 均为修后值） |
| `gates.py`（`build-copy/` 内） | **16/16 PASS，FAILURES: none**（rc=0，`gates-edition.log`） |

## 2. 机械门

| 门 | 结果 | 证据 |
|---|---|---|
| freeze baseline（版） | **8/8 byte-identical**（repointed files: none；核心 SVG 完整性通过） | `freeze-baseline-ed.log` |
| freeze baseline（核心对照） | **8/8 byte-identical**（`--build` = core-pt 构建目录、`--core-svg` = core-pt 的 svg 目录；核心 SVG 完整性通过，rc=0） | `freeze-baseline-core.log` |
| freeze diff（核心对照） | 新增 CJK 共 **9 个，全部 U+3000**（P1 2、其余每页 1）；新增汉字 0 | `freeze-diff.log`、`freeze-diff.json` |
| occlusion 真实审计（非 `--selftest`） | **0 flags**（rc=0）；内置自检 6 类全触发、干净对照静默 | `occlusion.log`、`occlusion.json`（`flag_count: 0`） |
| p8 extract | **150/150**（rc=0） | `p8-extract.log`、`p8-extract.json` |
| p8 compare vs 核心 | **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138]（预期，翻译题答案）；`p8-compare.json` 本体已全文核对 | `p8-compare.log`、`p8-compare.json` |
| keycheck | **149/150**（rc=0）；唯一不符 #150（开放作文，提取为 `✓`，预期） | `keycheck.log`、`keycheck-150.json` |
| creambox（canonical） | rc=0；0 溢出；31 个 OWN 末行真墨底余最小 **+2.1px**（`creambox-diag.log`） | `creambox.log`、`creambox-diag.log` |
| boxtitle 全版横向 PIL | **31/31 0 溢出**；advance 口径最小余量 **+15.1**（D-B1） | `boxtitle.log` |
| boxtitle 真墨复核（lineage 工具） | D-B1 真墨右缘 1396.0、余量 **+15.5**；D-B2 真墨右缘 1840.5、余量 **+21.5**（见 §4） | `boxtitle-trueink.log` |
| sweep（盒外行/纯填充盒） | box-vs-hline **0**；bridges 20，orphans 0，widows 0 | `sweep.log` |
| check_final（print/web 文字层） | 页数 8/8；词数 print=web=**8,507**；**词多重集 diff 0**；P8 答案区最小字号 **9.75pt**（187 spans，1,543 词） | `check-final.log`、`en-textdiff.json`、`en-p8size.json` |
| print/web `pdftotext -layout` 字节比对 | 全文逐字节相同 **110,438 B**；逐页 8/8 相同 | `print.txt`、`web.txt`、`print-p[1-8].txt`、`web-p[1-8].txt` |
| P8 最小字号（minfont.py，PDF 实测） | **9.75pt**，低于 9.75pt 0 处（n=375） | `minfont.log` |
| 孤儿标点全版重扫 | A（`:` 后接字母）**0**；B（行首孤儿标点）**0**；C（行末 `:`）6 处全为合法引导冒号；D（双空格）**0**；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，空白占位符固有格式；text.md 冒号后接字母 0 处；CJK 仅 U+FF5C ×6；U+2019 0 | `orphan-sweep.log` |
| 弯引号成对 | text.md `“`/`”` 2/2；8 SVG 明文 `“`/`”` 2/2；直引号 `"` 0 处；直撇号 5 处均为英文属格/引文（`'to fall on a day'`、`Editor's example`、`Editor's note`），非弯引号残缺 | 本文件 §5 |
| check_s11（pt-adapted §1.1） | **ALL §1.1/P8 CHECKS PASS**（rc=0；fix1 scratch 的 pt-adapted 脚本重跑） | `check-s11.log` |
| verify_ed（pt-en fix verification） | **ALL pt-en FIX VERIFICATIONS PASS**（rc=0；D1/D2/D3 存活 + D-B1/D-B2 修后值 + text.md 不变 + 150 键不变） | `verify-ed.log` |
| classify（hand patch） | **KEEP 25**（proof1 的 23 + 本轮新增的 2 处 fix 标记：`content12.py:48` tsize=21、`content7.py:82` size 21）；REVERT/MERGE/INSERT/DELETE 0 | `classify.log` |
| D5 gloss PIL 实测（只记录，不判） | P4 gloss 盒 4 行、末行右余 **+190.5**、底余 **+42.7**、无溢出 | `gloss-probe.log` |
| 重渲比对（仅 scratch 副本 `build-copy`） | 见 §11 | `render-copy.log`、`webpdf-copy.log`、`web-rerender.pdf`、`web-rerender.txt`、`print-rerender.txt` |

## 3. check_s11 / verify_ed 说明（无 pt 家族原版）

- `tools/` 下无 `check_s11.py` / `verify_ed.py`；en 家族版硬编码 core-en 与 en 专属串，无法在 pt-en 上运行。本轮重跑 fix1 scratch 内已写好的两份 pt-adapted 等效脚本（`check_s11-pt.py`、`verify_ed-pt.py`），rc 均为 0、全绿；脚本本身未改动。
- pt 系无 `registry.json` 成品（core-pt、pt-de 均无 `dump_reg.py`/`registry.json`）；run.py 的 REGISTRY STATS（TOTAL 150）+ p8 extract 重 dump 即等效重 dump，未新建 `registry.json` 成品。

## 4. D-B1/D-B2 修后独立实测（两法 + 23pt 方法自检）

| 缺陷 | 位置 | 源头 | 修后字号 | 真墨右缘（自写探针） | 余量（自写探针） | 真墨右缘（lineage 工具） | 余量（lineage 工具） | 合格（≥+4） |
|---|---|---|---|---|---|---|---|---|
| D-B1 | P1 `A SEMANA EM NÚMEROS　In numbers` | `content12.py:43`（`f.box(..., tsize=21)`，L48） | 21 | 1396.0 | **+15.5** | 1396.0 | **+15.5** | ✓ |
| D-B2 | P7 `ERROS COMUNS　Common mistakes` | `content7.py:82`（`p.text(..., 21, ...)`） | 21 | 1840.0 | **+22.0** | 1840.5 | **+21.5** | ✓ |

- 措辞未变：两处标题字符串与修前逐字相同（仅字号 23→21）；text.md 字节不变（SHA 同 §0）。
- 自写探针（`my_trueink.py`，全新编写；用版内 `svglib._pil`/`_runs` 取字体、逐 run 渲染、PIL `getbbox` 取墨右缘；口径为 lineage 一致的 exclusive 右缘）：全版 277 个盒内文本元素 **0 溢出**，最小余量即 D-B1 的 +15.5；其余 29 个盒标题最小余量 +22.2（与 proof1 相同）。D-B2 两法差 0.5px（渲染舍入），均远高于 +4 门槛。
- 方法自检：同一探针以修前 23pt 重测两处标题，得 D-B1 墨右 1433.0/余量 −21.5、D-B2 墨右 1876.0/余量 −14.0——与 proof1 实测（−22.5/−14.5）在 1px 舍入内一致，证实本探针能检出原缺陷，非空信号。
- P7 另有 4 个空白文本元素（`<text> </text>`，单空格占位，y=341.24/551.28/790.56/1000.6），无墨迹，已跳过并记录。
- SVG 元素核实：P1 标题 `x=1007.0 y=821.18 fs=21 bold`，盒 `x=989.0 y=786.2 w=422.5 h=432.0` 右缘 1411.5（盒高较修前 434.0 减 2，`tsize+10` 所致）；P7 标题 `x=1461.5 y=242 fs=21 bold`，盒 `x=1439.5 y=200.0 w=422.5 h=935.5` 右缘 1862.0。

## 5. D1/D2/D3 存活复验（修后逐项）

| # | 修复 | 核实 | 结果 |
|---|---|---|---|
| D1 | P1 刊头标语 | `tables_en.py` 新标语 `The Portuguese that Brazil is reading` 在位（1 处）；旧形 `The Portuguese Brazil is reading` 全版构建源 0 处；渲染 P1 文字层同值 1 处 | 存活 |
| D2 | P4 词表注 | `tables_en.py:36` `"冠军": "title"`；渲染 P4 Note 行 `o título title` 1 处；`*.py` 内 `champion` 2 处均为 `the champions' trophy`（`tables_en.py:39` 冠军奖杯、`content34.py:200` P8 注 55），非旧值 `champion` 单独释 `冠军` | 存活 |
| D3-56/57/58/102 | P8 注冒号 | P8 SVG 明文 `3 > 1: mais`、`5 > 4: mais`、`16:30 < 17:00: mais cedo`、`cair numa sexta-feira: falls on a Friday` 各 1 处；旧形（冒号后无空格）0 处 | 存活 |
| 全版冒号复扫 | `:` 后直接接字母 | 8 个 SVG 明文（除时钟 `16:30` 等数字外）+ text.md 均为 **0 处** | 存活 |
| p8 键 | 150 键 | P8 extract 与 proof1 提取逐字相同（`verify_ed` PASS，diff=[]） | 存活 |
| SVG 变化 | 仅 P1/P7 应变 | 发货 SVG vs fix1 `pre-svg-sha.txt`（proof1 发货基线）：仅 p1（`164d2c52…`→`8d3e2875…`）、p7（`3760e251…`→`7cb27481…`）变，其余 6 页逐字节一致。注：`scratch-refanout-pt/backup-old/` 为第一轮版（非紧邻修前版），其 p3/p6/p8 与 proof1 发货版亦不同——该差异在 fix1 修前已存在，与本轮修复无关；以紧邻修前基线（fix1 pre-svg）为准，仅 P1/P7 变 | 存活 |

## 6. KIT §9 核对

- `boxtitle true-ink` 一句已改为如实记录（WEEKLY-KIT.md L123）：“2 overflows before fix round 2 (D-B1 … −22.5, D-B2 … −14.5, both present since the first-round edition), 0 after fix round 2”。
- `535 lines` 已更正：全文 `534 lines`（L116 等，实测 `wc -l` 534 行）。
- 附录 “Fix round 2” 记录段（L129）在位：两处 21pt、措辞未变、text.md 字节不变、修后余量 +15.5/+21.5、31/31 clear、仅 p1/p7 SVG 变、D1/D2/D3 存活、印 PDF scratch 重渲 SHA 一致。

## 7. 150 题逐题手验（题干 + 键 + 题干适配）

- 三源：`text.md` 全文 534 行（已通读）+ 渲染 8 页文字层（已通读 P1/P7 全文，其余逐页核对）+ REG 键/`p8-extract.json`（`q-table.txt` 150 行已逐条核对）。
- 三方一致：text.md 行内键、REG 键、P8 提取键 149/150 一致，唯一 #150 为预期开放作文（P8 提取 `✓`）；text.md 末行答案总表与 REG 逐键核对 0 差异；P8 渲染文字层扁平化子串核对 150/150 在位（含 Q150 的 `150. ✓ See the model text … (88 words)` 形）。
- 题干适配（逐题核对题干是否贴合英文读者）：Q73 `Depois da prova, começa a ___.`（espera）题干为通用葡语、无错位；Q56–58 比较级（`3 > 1: mais` 等）、Q76–79 将来时、Q93–100 过去时/词框、Q101–112 介词/过去完成/将来虚拟式、Q113–120 完形、Q121–132 阅读理解（Rafael：Salvador / capoeira / Palmeiras × Flamengo / extraoficial）、Q133–136 组句、Q137–140 翻译（137 `Friday 20 November is a national holiday.`、138 `Palmeiras won 5–4 in the shoot-out.`；139/140 为英→葡，答案为葡语原文，正确）、Q141–144 配对、Q145–149 对话（Q148 `na internet`，em+a=na 正确）、Q150 开放作文均正确。
- 事实抽查（独立验算/检索）：P6 图表 16–30 日共 15 天（工作日 10 天：16/17/18/19/23/24/25/26/27/30；周末+假日 5 天：20/21/22/28/29），第 10 个工作日 11 月 30 日，27–30 窗口与版内「entre 27 e 30 de novembro, conforme a contagem」一致；星期经 `date -d`（America/Sao_Paulo）核实：11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日——与版内全部星期表述一致；Q150 范文独立数词 **88 词**（含 `×` 计一词），与 REG `model words: 88` 一致；Q120 第二日 13h30–18h30 = 5 小时（B）与 P5/P6 一致；Q89 两周日 8/15 与 P6 一致；Q125 第 36 轮 Palmeiras × Flamengo 在周六 21 日与 P1 日程一致。
- 外部事实核对（公开检索）：2026 圣保罗大奖赛 11 月 8 日 Norris 夺冠、Verstappen 第二、Hadjar 第三、Mercedes 获车队冠军（McLaren/Formula 1/AP 等多源一致）——与版内 P4/Q51/Q124 逐字相符；巴西杯半决赛：Atlético-MG 1–1 Grêmio（11 月 7 日，总比分 3–1，首回合 Grêmio 2–0）、Vasco 2–1 Palmeiras（11 月 8 日，点球 5–4，首回合 Palmeiras 1–0），进球者 Renan Lodi / Carlos Vinícius，决赛 12 月 6 日单场于 Mané Garrincha——与版内 P4/Q47–49/Q122–123 全部相符。
- 徽章/版式：8 页徽章与核心逐页同数同级（gates.py 16/16 覆盖）；VOL.4 全期正确；P8 答案区 187 spans 最小 9.75pt，恰为下限。
- ABSTRACT.txt：561 字节，英文单段，含刊头 `A Lucerna Portuguese Weekly VOL.4:`。
- 观察项（不计缺陷）：Q44 组句 `o dia 20 / é / feriado nacional → O dia 20 de novembro é feriado nacional.`——键句含词库未列的 `de novembro`；但与核心版 `core-pt/2026-w47-pt-zh-cn.text.md:197` 逐字相同，属核心继承的习题设计（日期由题面语境补足），非本版 fan-out 引入；proof1 亦已通过。记为观察 O4，不判缺陷。

## 8. 8 页逐页目视（交付印刷 PDF 渲染，110dpi；网版 P1/P8 抽查）

- P1：干净；D-B1 标题已回盒内（`crop-p1-title.png` 放大裁切：`In numbers` 末尾 `s` 在盒内，右侧留白清晰）。D1 标语单行完整；头条、数字盒（4 项全）、日程、目录、每周一词、快讯、Q1–10 均干净。
- P2：干净。Q11–28、PARA NÃO ERRAR、Note 框、日程四格均干净；中部大空白为核心版式。
- P3：干净。Q29–46、6 词 Note 框、Zumbi 图注（Parreiras 1927）均干净。
- P4：干净。D2 `o título title` 在版；OS FINALISTAS 数据盒、足球周表、截稿注（10 November）、Q47–64 均干净。
- P5：干净。Q65–82、Gary Todd 图注 CC0、五步计划均干净。
- P6：干净。Q83–100、时间线盒、图表（10+5=15，两条形图）均干净；Note 框 `o chute a lucky guess` 在盒内。
- P7：干净；D-B2 标题已回盒内（`crop-p7-title.png` 放大裁切：`mistakes` 末尾 `s` 在盒内）。三级语法栏、4 条常见错误、每周一词、读者来信（披露逐字）、8 条金句、VOL.5 预告均干净。
- P8：干净。Q113–150 题面、徽章、G 对话、H 写作题与范文（88 词）、Mané Garrincha 图注、150 条答案注均干净；D3 四处空格在版。
- 网页 P1/P8（`web-p1-1.png`、`web-p8-8.png`）与印刷版内容一致；P1 标题修复在网版同见。

## 9. 观察项（不计缺陷）

- **O1** — canonical creambox.py 的 `desc-clear`（0.30×字号保守估计）6 处 −0.9~−1.1（与 fix1 GATE-LOG §2 相同裁决）：真墨底余 +4.8/+4.9，修前亦然，非溢出。
- **O2** — `scratch-refanout-pt/FANOUT-REPORT-pt.md` §2 表格亦称 pt-en boxtitle "clear"，与 KIT §9 同源失实表述；该报告覆盖 10 个 pt 版、属共享重建报告，fix1 已记录在案，本轮未改（供协调员决定是否同步修订）。
- **O3** — P8 注 55 `taça=the champions' trophy` 与 P4 注 `a taça trophy` 对同一词释义宽严不一（与 proof1 O3 同一观察）；含义未错，仅释义不一致。
- **O4** — Q44 组句键句含词库未列的 `de novembro`（见 §7；核心逐字相同，继承设计）。
- **O5** — D5 字体只记录数量：P4 gloss 盒 4 行、末行右余 +190.5、底余 +42.7（§2）；不判，不修。
- **O6** — `furniture.py` FURN[en] `badge372` 的 `EXPLICATIONS` 拼写 stale（fix1 已记，见 KIT §6，本轮未动）。

## 10. 结论（报事实，不作定稿决定）

- D-B1/D-B2 已在源头修复（字号 23→21pt，措辞零改动），修后 PIL 真墨 + 交付 PDF 像素双法复测余量分别为 **+15.5 / +21.5**（自写探针 +22.0/+15.5），全版 31 个盒标题 **0 溢出**；其余全部机械门、150 键、8 页文字层、事实抽查均通过；D1/D2/D3 全部存活。
- 按 SOP §8.4，定稿须经新一轮独立全量校对零问题；本轮为复校，结论见 PROOF-NOTE.md。
- 本轮未修改任何成品（收工复核见 §12）；未改 core-pt、W43–W46、其他目标语家庭；未 commit、未 push。

## 11. 重渲比对（仅 scratch 副本 `build-copy`，生产 web PDF 未被覆盖）

| 步骤 | 结果 |
|---|---|
| `render.py`（`build-copy/` 内） | rc=0；重渲印 PDF 12,932,441 B，**SHA 与交付逐字相同** `7e235e4591c034815ed90bcc21cef48a3b40bb1eb39bb0ebb1c8f027fbcb2e42` |
| `tools/webpdf.py`（`build-copy/svg` → `web-rerender.pdf`） | rc=0；1,139,919 B（交付 1,139,917 B，+2 B，fontTools 嵌时间戳所致的预期浮动）；**文字层与交付网 PDF 逐字节相同** 110,438 B |
| 重渲印 PDF 文字层 | 与交付印 PDF 文字层逐字节相同 |

## 12. 生产目录未改动

开工 `sha256sum` 快照 vs 收工复核：47 个文件 `sha256sum -c` 全 OK，零改动（`prod-snapshot.sha256`）。
