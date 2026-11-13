# 独立校对笔记 — 2026-W47 pt-en（fix1 重建版，re-proof）

- 校对员：re-proof（第二轮复校；与 pt 核心 builder、pt-en 重建者、proof1 校对员、fix1 返修员均不同人）
- 校对时间：2026-11-11 EST
- 复校对象：`production/2026-w47/2026-w47-pt-en/`（fix1 重建版，VOL.4）
- 依据：任务书 + `scratch-fix-pt-en1/FIX-LOG.md` + `GATE-LOG.md`（返修自查，不作结论）+ `scratch-proof-pt-en2/PROOF-NOTE.md`（proof1 结论 (b) 依据）+ SOP §8
- 方式：只检查、不改任何源码/成品。`run.py` 重跑、`render.py`、`webpdf.py`、keycheck 均在 scratch 内 `build-copy` 进行；版目录 47 个文件开工前后 SHA 全量复核零改动（`prod-snapshot.sha256`）。全部解释器为 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3，各工具 runtime 行自证）。`PYTHONDONTWRITEBYTECODE=1` 全程开启，`TMPDIR` 指向本 scratch。
- 工作笔记目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-en1/`

## 0. 开工探针与身份核对

- 探针 1：`ls /dev/null` 存在（crw-rw-rw-，1, 3）；仓库内 `git hash-object -w --stdin` 成功（`9daeafb9…`，rc=0）。注：首次在 `~` 下直接跑因不在 git 仓库内报 `fatal: not a git repository`（rc=128）；改在 `~/workspace/weekly-git` 内重探即通，未硬锤。
- 探针 2：在本 scratch 目录真实写文件成功。
- 印刷 PDF `A-Lucerna-VOL4.pdf`：**12,932,441 字节，sha256 `7e235e4591c034815ed90bcc21cef48a3b40bb1eb39bb0ebb1c8f027fbcb2e42`**——与任务书逐字一致。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：**1,139,917 字节，sha256 `aad718e1efccbbcf24f4a1d6ac05fbe1bc59bf3b431037384f5645896bd7fc6c`**——与任务书逐字一致。
- 文字 `2026-w47-pt-en.text.md`：**37,333 字节，sha256 `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`**，534 行——与任务书逐字一致，且与修前逐字节相同（fix1 重导 diff 0 行）。
- 身份相符，继续复校。

## 1. 缺陷

**无。本轮独立全量复校发现缺陷 0 项。**

原 proof1 的两项缺陷 D-B1/D-B2 均已在源头修复并经独立重测证实（见 §2）；其余全部机械门、150 题、8 页文字层、事实抽查均通过（见 GATE-LOG.md）。

## 2. D-B1/D-B2 修复独立复验（不照抄 fix1 数字）

两处均经三重证据确认：(i) 源码字号 21pt 在位、措辞未变；(ii) 自写 PIL 真墨探针（全新编写，与 fix1 的 `measure_candidates.py` / proof1 的 `boxtitle_trueink.py` 不同脚本）量得真墨右缘回盒内；(iii) lineage 工具 `boxtitle_trueink.py` 交叉验证数值一致；(iv) 交付印刷 PDF 渲染目视——标题末字落在奶油盒内（见 §6 与 `render/crop-p1-title.png` / `render/crop-p7-title.png`）。

### D-B1 — P1「A SEMANA EM NÚMEROS In numbers」已回盒内，余量 +15.5px

- 位置：`svg/p1-capa.svg`，标题元素 `x=1007.0 y=821.18 fs=21 bold Noto Sans CJK SC`，文本 `A SEMANA EM NÚMEROS　In numbers`（单 `<text>` 元素）。
- 盒：`x=989.0 y=786.2 w=422.5 h=432.0`，盒右缘 `1411.5`（盒高较修前 434.0 减 2，`Flow.box` 盒高含 `tsize+10` 所致）。
- 实测（自写探针）：**真墨右缘 1396.0，clear +15.5**（advance 右缘 1396.5，clear +15.0）。lineage 工具同值（1396.0 / +15.5）。合格要求 ≥+4，余量为其近 4 倍。
- 方法自检：同一探针以修前 23pt 重测，得墨右 1433.0 / −21.5——与 proof1 实测（1434.0 / −22.5）在 1px 舍入内一致，证实探针能检出原缺陷。
- 源头：`content12.py:43`–48：`f.box("A SEMANA EM NÚMEROS　In numbers", [...], tsize=21)`，措辞逐字未变。

### D-B2 — P7「ERROS COMUNS Common mistakes」已回盒内，余量 +21.5px

- 位置：`svg/p7-lingua.svg`，标题元素 `x=1461.5 y=242 fs=21 bold Noto Sans CJK SC`，文本 `ERROS COMUNS　Common mistakes`。
- 盒：`x=1439.5 y=200.0 w=422.5 h=935.5`，盒右缘 `1862.0`。
- 实测（自写探针）：**真墨右缘 1840.0，clear +22.0**（advance 右缘 1840.5，clear +21.5）；lineage 工具：墨右 1840.5 / **+21.5**。两法差 0.5px（渲染舍入），均远高于 +4 门槛；与 fix1 所称 +21.5 一致（取 lineage 值）。
- 方法自检：同一探针以修前 23pt 重测，得墨右 1876.0 / −14.0——与 proof1 实测（1876.5 / −14.5）在 1px 舍入内一致。
- 源头：`content7.py:82`：`p.text(bx + 22, yy3 + 26, "ERROS COMUNS　Common mistakes", 21, "sans", True, OLIVE)`，措辞逐字未变。

### 全版盒标题横扫

- 自写探针扫全版 277 个盒内文本元素：**0 溢出**，最小余量即 D-B1 的 +15.5——D-B1 现为全版最紧的盒标题，仍合格。
- `boxtitle_core.py`（advance 口径）：31/31 盒标题 0 溢出，最小余量 +15.1（D-B1）；其余 29 标题最小正余量 +22.2（与 proof1 相同）。
- occlusion 0 flags 不覆盖此类（工具盲区，proof1 已述：奶油盒 `#f0eee5` 纯填充无描边从不进入候选），故以上盒标题专用门为准。

## 3. 机械门（全部独立重跑，见 GATE-LOG.md）

| 门 | 结果 | 证据 |
|---|---|---|
| 身份（字节+SHA-256） | 三 SHA 与任务书逐字一致 | 本笔记 §0 |
| run.py 重跑（build-copy 内） | **rc=0，TOTAL 150**；A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；FLOW OVERFLOW 0，HEAD TOO WIDE 0 | `run-rebuild.log` |
| 重建 SVG vs 发货 SVG | **8/8 字节一致** | `rebuilt-svg-sha.txt`、`shipped-svg-sha.txt` |
| gates.py 16/16 | **16/16 PASS，FAILURES: none**（rc=0） | `gates-edition.log` |
| freeze baseline（版重建 vs 发货 SVG） | **8/8 byte-identical**，repointed files: none | `freeze-baseline-ed.log` |
| freeze baseline（核心重建 vs 发货核心 SVG） | **8/8 byte-identical**（rc=0；`--build` 指 core-pt 构建目录、`--core-svg` 指 core-pt 的 svg 目录） | `freeze-baseline-core.log` |
| freeze diff（核心对照） | 新增 CJK 共 9 个，全部为 U+3000（P1 2、其余每页 1）；新增汉字 0 | `freeze-diff.log`、`freeze-diff.json` |
| occlusion 真实审计 | **0 flags**（rc=0）；内置自检 6 类全触发、干净对照静默 | `occlusion.log`、`occlusion.json` |
| p8 extract | **150/150**（rc=0） | `p8-extract.log`、`p8-extract.json` |
| p8 compare vs 核心 | **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138]（预期，翻译题答案）；`p8-compare.json` 本体已全文核对 | `p8-compare.log`、`p8-compare.json` |
| keycheck | **149/150**（rc=0）；唯一不符 #150（开放作文，提取为 `✓`，预期） | `keycheck.log`、`keycheck-150.json` |
| print/web 文字层 | `pdftotext -layout` **逐字节相同 110,438 B**；逐页 8/8 相同；`check_final` 词多重集 diff 0（各 8,507 词），页数 8/8 | `print.txt`、`web.txt`、`print-p[1-8].txt`、`web-p[1-8].txt`、`check-final.log`、`en-textdiff.json` |
| P8 最小字号 | **9.75pt**，低于 9.75pt 0 处；答案区 187 spans、1,543 词 | `minfont.log`、`en-p8size.json` |
| creambox 真墨 | 31 个 OWN 末行全部正余量，**最小真墨底余 +2.1px**，0 溢出 | `creambox.log`、`creambox-diag.log` |
| boxtitle | **0 处 OVERFLOW**（见 §2）；日志与 fix1 逐值相符 | `boxtitle.log`、`boxtitle-trueink.log`、`my-trueink.log` |
| sweep | box-vs-hline 0；bridges 20，orphans 0，widows 0 | `sweep.log` |
| check_s11（pt-adapted §1.1） | **ALL PASS**（rc=0） | `check-s11.log` |
| verify_ed（pt-en fix verification） | **ALL PASS**（rc=0） | `verify-ed.log` |
| classify（hand patch） | **KEEP 25**（proof1 的 23 + 新增 2 处 fix 标记）；REVERT/MERGE/INSERT/DELETE 0 | `classify.log` |
| D5 gloss（§4） | 4 行、末行右余 +190.5、底余 +42.7、无溢出；与 fix1 宣称逐字相同 | `gloss-probe.log` |
| 重渲对比（仅 scratch） | 见 GATE-LOG §11 | `render-copy.log`、`webpdf-copy.log`、`web-rerender.pdf` |

## 4. D5 P4 gloss 核验（只记录数量，不判 (b)，不修）

- en 的 `冠军` 本就映射为 `title`（`tables_en.py:36`：`"冠军": "title"`），无歧义可消；`冠军头衔 → title`（:37）与 `墨底 → ink bottom`（:38）均已核实。
- text.md 与首轮版字节相同：SHA `513326ff…`（§0），`text.md` 第 215 行仍为 `*Note｜o agregado aggregate score · os pênaltis penalty shoot-out · a decisão the final · o título title · a pausa the break · a taça trophy.*`。
- PIL 实测（`gloss_probe.py` 独立重跑）：P4 gloss 盒 `x=989.0 y=270.48 w=422.5 h=175.4`，**4 行、末行右余 +190.5、底余 +42.7、无溢出**——与 fix1 宣称逐字相同。
- SEG 键总数：222；`冠军 → title`（:36）、`冠军头衔 → title`（:37）、`墨底 → ink bottom`（:38）。

## 5. D1/D2/D3 修复存活复验

| # | 修复 | 核实位置 | 结果 |
|---|---|---|---|
| D1 | P1 刊头标语 | `tables_en.py` 新标语 `The Portuguese that Brazil is reading` 在位；旧形 `The Portuguese Brazil is reading` 全版构建源 0 处；渲染 P1 文字层同值 | 存活 |
| D2 | P4 词表注 | `tables_en.py:36`：`"冠军": "title"`；`champion` 2 处均为 `the champions' trophy`（`tables_en.py:39` 冠军奖杯、`content34.py:200` P8 注 55），非旧值；渲染 P4 Note 行 `o título title` | 存活 |
| D3-56/57/58/102 | P8 注冒号 | 发货 `svg/p8-avaliacao.svg` 明文内 `3 > 1: mais`、`5 > 4: mais`、`16:30 < 17:00: mais cedo`、`cair numa sexta-feira: falls on a Friday` 各 1 处；旧形 0 处 | 存活 |
| 全版冒号复扫 | `:` 后直接接字母 | 8 个 SVG 明文 + text.md 均为 **0 处**（时刻 `13:30` 等属数字，已排除；base64 数据已排除） | 存活 |
| SVG 变化 | 仅 P1/P7 应变 | vs fix1 `pre-svg-sha.txt`（proof1 发货基线）：仅 p1、p7 变，其余 6 页逐字节一致；`backup-old/` 为第一轮版，其 p3/p6/p8 差异在 fix1 修前已存在，与本轮无关 | 存活 |
| p8 键 | 150 键 | P8 提取键与 proof1 逐字相同（diff=[]） | 存活 |
| KIT §9 | 附录更正 | `boxtitle true-ink` 一句已改为如实记录（修前 2 处溢出 −22.5/−14.5，修后 0 处，余量 +15.5/+21.5）；`535 lines` 已更正为 `534 lines`；“Fix round 2” 记录段在位 | 已核实 |

## 6. 150 题逐题手验（题干 + 键 + 题干适配）

- 三源：`text.md` 练习全文（已通读 534 行）+ 渲染 8 页文字层（P1/P7 全文通读，其余逐页核对）+ REG 键/`p8-extract.json`（`q-table.txt` 150 行已逐条核对）。
- 三方一致：text.md 行内键、REG 键、P8 提取键 149/150 一致，唯一 #150 为预期开放作文（P8 提取 `✓`）；text.md 末行答案总表与 REG 逐键核对 0 差异；P8 渲染文字层扁平化子串核对 150/150 在位。
- 题干适配（Q73/en-ko 教训）：逐题核对题干是否贴合英文读者——Q73 `Depois da prova, começa a ___.`（espera）题干为通用葡语、无错位；其余如 Q56–59 比较级、Q76–79 将来时、Q93–100 过去时/词框、Q101–112 介词/过去完成/将来虚拟式、Q113–120 完形、Q121–132 阅读理解（Rafael：Salvador / capoeira / Palmeiras × Flamengo / extraoficial）、Q133–136 组句、Q137–140 翻译、Q141–144 配对、Q145–149 对话（Q148 `na internet`，em+a=na 正确）、Q150 开放作文均正确。
- 事实抽查（独立验算/检索）：P6 图表 16–30 日共 15 天（工作日 10 天：16/17/18/19/23/24/25/26/27/30；周末+假日 5 天：20/21/22/28/29），第 10 个工作日 11 月 30 日，27–30 窗口与版内「entre 27 e 30 de novembro, conforme a contagem」一致；星期经 `date -d`（America/Sao_Paulo）核实：11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日——与版内全部星期表述一致；Q150 范文独立数词 **88 词**（含 `×` 计一词），与 REG `model words: 88` 一致；Q120 第 2 日 13h30–18h30 = 5 小时（B）与 P5/P6 一致；Q89 两周日 8/15、Q125 第 36 轮 Palmeiras × Flamengo 在周六 21 日与 P1 日程一致。
- 外部事实核对（公开检索）：2026 圣保罗大奖赛 11 月 8 日 Norris 夺冠、Verstappen 第二、Hadjar 第三、Mercedes 获车队冠军（McLaren / Formula 1 / AP 多源一致）——与版内 P4/Q51/Q124 逐字相符；巴西杯半决赛 Atlético-MG 1–1 Grêmio（11 月 7 日，总比分 3–1，首回合 Grêmio 2–0）、Vasco 2–1 Palmeiras（11 月 8 日，点球 5–4，首回合 Palmeiras 1–0），进球者 Renan Lodi / Carlos Vinícius，决赛 12 月 6 日单场于 Mané Garrincha——与版内 P4/Q47–49/Q122–123 全部相符。
- 徽章/版式：8 页徽章与核心逐页同数同级（gates.py 16/16 覆盖 P7 引文 2×、披露逐字、图片+来源 5/5、页脚 8/8）；VOL.4 全期正确；P8 答案区 187 spans 最小 9.75pt，恰为下限。
- 孤儿标点扫（`orphan_sweep.py`）：A（`:` 后接字母）0、B（行首孤儿标点）0、D（双空格）0；C（行末 `:`）6 处全为合法引导冒号（如 `No futebol, a final está decidida:`）；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，为空格占位符的固有格式，非缺陷；text.md 冒号后接字母 0 处、CJK 仅 U+FF5C ×6（冻结 `Note｜` 标签格式）、U+2019 0。
- 弯引号成对：text.md `“`/`”` 2/2、8 SVG 明文 `“`/`”` 2/2、渲染文字层 P8 `“`/`”` 2/2；禁词/简体残留：text.md CJK 汉字 0 处。

## 7. 8 页逐页目视（交付印刷 PDF 渲染，110dpi）

- P1：干净；D-B1 标题已回盒内（`render/crop-p1-title.png` 放大裁切：`In numbers` 的末尾 `s` 落在盒内，右侧留白清晰）。头条、数字盒、日程、目录、每周一词、快讯、Q1–10 均干净；D1 标语单行完整。
- P2：干净。Q11–28、PARA NÃO ERRAR、Note 框、日程四格均干净；中部大空白为核心版式。
- P3：干净。Q29–46、6 词 Note 框、Zumbi 图注（Parreiras 1927）均干净。
- P4：干净。D2 `o título title` 在版；OS FINALISTAS 数据盒、足球周表、截稿注（10 November）、Q47–64 均干净；P4 gloss 盒 4 行、底余充足（§4）。
- P5：干净。Q65–82、Gary Todd 图注 CC0、五步计划均干净。
- P6：干净。图表算术已独立验算（§6）；Q83–100、时间线盒均干净；Note 框 `o chute a lucky guess` 在盒内。
- P7：干净；D-B2 标题已回盒内（`render/crop-p7-title.png` 放大裁切：`mistakes` 的末尾 `s` 落在盒内）。三级语法栏、4 条常见错误、每周一词、读者来信（示例 + 葡/英双语披露，VOL.3→VOL.5 承诺顺延）、8 条金句、VOL.5 预告均干净。
- P8：干净。Q113–150 题面、徽章、G 对话、H 写作题与范文（88 词）、Mané Garrincha 图注、150 条答案注均干净；D3 四处空格在版。
- 网页 P1/P8（`render/web-p1-1.png`、`render/web-p8-8.png`）与印刷版内容一致；P1 标题修复在网版同见。

## 8. 观察项（不计缺陷）

- **O1** — canonical creambox.py 的 `desc-clear`（0.30×字号保守估计）6 处 −0.9~−1.1（与 fix1 GATE-LOG §2 相同裁决）：真墨底余 +4.8/+4.9，修前亦然，非溢出。
- **O2** — `scratch-refanout-pt/FANOUT-REPORT-pt.md` §2 表格亦称 pt-en boxtitle "clear"，与 KIT §9 同源失实表述；该报告覆盖 10 个 pt 版、属共享重建报告，fix1 已记录在案，本轮未改（供协调员决定是否同步修订）。
- **O3** — P8 注 55 `taça=the champions' trophy` 与 P4 注 `a taça trophy` 对同一词释义宽严不一（与 proof1 O3 同一观察）；含义未错，仅释义不一致。
- **O4** — Q44 组句 `o dia 20 / é / feriado nacional → O dia 20 de novembro é feriado nacional.`——键句含词库未列的 `de novembro`；但与核心版 `core-pt/2026-w47-pt-zh-cn.text.md:197` 逐字相同，属核心继承的习题设计（日期由题面语境补足），非本版 fan-out 引入；proof1 亦已通过。本轮记为观察，不判缺陷。
- **O5** — P2/P3/P5/P6 中部大空白与 P2/P4 栏尾孤行（与 proof1 O4 同一观察，核心版式，与核心一致，非 fan-out 引入）。
- **O6** — P6 Note 框 `o chute a lucky guess`：`chute` 未出现在 P6 文章正文，但出现在当页 D 组词框与 Q100 题面，且核心中文注同样释 `chute`（与 proof1 O5 同一观察，核心版式、忠实转译）。
- **O7** — `furniture.py` FURN[en] `badge372` 的 `EXPLICATIONS` 拼写 stale（fix1 已记，见 KIT §6，本轮未动）。
- **O8** — D5 字体只记录数量：P4 gloss 盒 4 行、末行右余 +190.5、底余 +42.7（§4）；不判，不修。

## 9. 结论（报事实，不作定稿决定）

- 本轮独立全量复校发现 **缺陷 0 项**。D-B1/D-B2 已在源头修复（字号 23→21pt，措辞零改动），修后 PIL 真墨余量 **+15.5 / +21.5**，交付 PDF 像素裁图目视确认，全版 31 个盒标题 **0 溢出**；其余全部机械门、150 键、8 页文字层、事实抽查均通过；D1/D2/D3 全部存活；text.md 字节不变。
- 结论 **(a)**：零缺陷可定稿。按 SOP §8.4，是否定稿由协调员决定。
- 本轮未修改任何成品；版目录 47 个文件开工前后 SHA 全量复核零改动；全部校对证据在 `scratch-reproof-pt-en1/`（本笔记 + `GATE-LOG.md` + 各门日志/JSON + `render/` 渲染图 + `build-copy/` 重跑副本 + `my_trueink.py` 自写探针）。

## 附：三 SHA（完整串）

- 印刷 PDF `A-Lucerna-VOL4.pdf`：12,932,441 字节；sha256 `7e235e4591c034815ed90bcc21cef48a3b40bb1eb39bb0ebb1c8f027fbcb2e42`；8 页。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：1,139,917 字节；sha256 `aad718e1efccbbcf24f4a1d6ac05fbe1bc59bf3b431037384f5645896bd7fc6c`；8 页；文字层 110,438 字节（pdftotext -layout）。
- 文字 `2026-w47-pt-en.text.md`：37,333 字节；sha256 `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`；534 行。
