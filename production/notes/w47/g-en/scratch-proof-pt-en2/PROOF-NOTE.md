# 独立校对笔记 — 2026-W47 pt-en（重建版，proof1）

- 校对员：proof1（重建版独立复校；与 pt 核心 builder、pt-en 重建者、第一轮复校员均不同人）
- 校对时间：2026-11-11 15:33–约 16:00 EST
- 复校对象：`production/2026-w47/2026-w47-pt-en/`（重建版，core-pt fix2 `d2b0e182` 重建）
- 依据：任务书 + `FANOUT-REPORT-pt.md` §1/§2/§6 + 本版 `WEEKLY-KIT.md` §9 附录（Re-fanout 说明）+ SOP §8
- 方式：只检查、不改任何源码/成品。`run.py` 重跑、`render.py`、`webpdf.py`、keycheck 均在 scratch 内 `build-copy` 进行；版目录 47 个文件开工前后 SHA 全量复核**零改动**（`prod-snapshot.sha256`）。全部解释器为 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3，各工具 runtime 行自证）。
- 工作笔记目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-en2/`（本目录内 `prev-first-round-proof2/` 为第一轮 proof2 的旧笔记，已原样归档，未动）

## 0. 开工探针与身份核对

- 探针 1：`ls /dev/null` 存在（crw-rw-rw-，1, 3）；`git hash-object -w /dev/null` 成功（`e69de29b…`，rc=0）。
- 探针 2：在本 scratch 目录真实写文件成功。
- 印刷 PDF `A-Lucerna-VOL4.pdf`：**12,932,439 字节，sha256 `782e7cb9d9109f4282667fd6dde71ab981933fa5290a9cd4882aaa49322cca6d`**——与任务书逐字一致。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：**1,139,921 字节，sha256 `e02cf58cbee4cf5daac47fccc9319faf8158b6b31523ba220794f415a5e9bb61`**——与任务书逐字一致。
- 文字 `2026-w47-pt-en.text.md`：**37,333 字节，sha256 `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`**——与任务书逐字一致，且与第一轮版字节相同（`backup-sha.txt` en/text.md 同 SHA）。
- 身份相符，继续复校。

## 1. 缺陷（2 项）——结论 (b) 的依据

两处均为盒标题（cream-box title）真墨溢出盒右缘，任务书明文门禁「creambox/box-title PIL 真墨 0 溢出」要求为 0，实测为 2。两处均经三重证据确认：(i) `boxtitle_core.py`（PIL advance）标记 `<<<< OVERFLOW`；(ii) 自写真墨探针（与 `gates.py` 同款 `svglib._pil` + `getbbox anchor='ls'`）测得真墨右缘出盒；(iii) 交付印刷 PDF 渲染目视——标题末字落在奶油盒外的纸面上。两处在第一轮版（`backup-old/`）中已存在、数值逐字相同（重建未引入、也未修复）；核心版（core-pt）同类标题 0 溢出（`boxtitle-core.log`，OVERFLOW 0 处），故不是核心继承。

### D-B1 — P1「A SEMANA EM NÚMEROS In numbers」标题出盒 −22.5px

- 位置：`svg/p1-capa.svg`，标题元素 `x=1007.0 y=823.18 fs=23 bold Noto Sans CJK SC`，文本 `A SEMANA EM NÚMEROS　In numbers`（单 `<text>` 元素）。
- 盒：`x=989.0 y=786.18 w=422.5 h=434.0`，盒右缘 `1411.5`。
- 实测：advance 右缘 `1433.5`（clear −22.0，`boxtitle.log`）；**真墨右缘 `1434.0`（clear −22.5，`boxtitle-trueink.log`）**。源头：`content12.py:43`：`f.box("A SEMANA EM NÚMEROS　In numbers", [`。
- 目视证据：`render/crop-p1-title.png`（放大裁切：`In numbers` 的末尾 `s` 落在盒外白纸上）；`render/print-p1-1.png` 整页同见。
- 排除误报：不是 advance 口径假象（真墨比 advance 更宽 0.5px）；不是标题换行（单行单元素）；盒右缘 1411.5 为该盒唯一右边界。

### D-B2 — P7「ERROS COMUNS Common mistakes」标题出盒 −14.5px

- 位置：`svg/p7-lingua.svg`，标题元素 `x=1461.5 y=242 fs=23 bold Noto Sans CJK SC`，文本 `ERROS COMUNS　Common mistakes`。
- 盒：`x=1439.5 y=200.0 w=422.5 h=935.5`，盒右缘 `1862.0`。
- 实测：advance 右缘 `1876.5`（clear −14.5，`boxtitle.log`）；**真墨右缘 `1876.5`（clear −14.5，`boxtitle-trueink.log`）**。源头：`content7.py:82`：`p.text(bx + 22, yy3 + 26, "ERROS COMUNS　Common mistakes", 23, "sans", True,`。
- 目视证据：`render/crop-p7-title.png`（放大裁切：`mistakes` 的末尾 `s` 落在盒外）；`render/print-p7-7.png` 整页同见。

### 为什么 occlusion 0 flags 不覆盖这两处（工具盲区，非裁决）

- `occlusion_audit.py` 的 BOXTITLE 类只考察带描边（`stroke` 非空）或 `#2c2822` 填充的矩形（`occlusion_audit.py` 约 L471–500：`e.attrs.get("stroke") not in (None, "none") or fill == "#2c2822"`）；奶油盒 `#f0eee5` 为纯填充无描边，**从不进入候选**，故 0 flags 不能为盒标题背书。盒标题的专用门是 `boxtitle_core.py`，它对两处均亮 `OVERFLOW`。
- `boxtitle_core.py` 的 rc 恒为 0（脚本无非零退出路径），`gates.json` 的 `boxtitle_rc: 0` 是空洞信号，以 `OVERFLOW` 标记为准。
- KIT §9「boxtitle true-ink clear on all boxes」与事实不符——重建者自己的 `en-boxtitle.log` 就有这两行 `OVERFLOW`，我的独立重跑日志与之**逐字节相同**（`diff` 无差异）。
- 其余 29 个盒标题全部为正余量，最小正余量 +22.2px（P2 `Palmeiras × Flamengo, às`），无边缘待裁决项。
- 同类横向情况（仅作背景，不属本版）：de −1.6、es −3.6、it −59.6 亦有 OVERFLOW；fr/ja/ko/nl/ru/zh-tw 为 0。

## 2. 机械门（全部独立重跑，见 GATE-LOG.md）

| 门 | 结果 | 证据 |
|---|---|---|
| 身份（字节+SHA-256） | 三 SHA 与任务书逐字一致 | 本笔记 §0 |
| run.py 重跑（build-copy 内） | **rc=0，TOTAL 150**；A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38；FLOW OVERFLOW 0，HEAD TOO WIDE 0 | `run-rebuild.log` |
| gates.py（版内自检，只读） | **16/16 PASS，FAILURES: none**（rc=0） | `gates-edition.log` |
| freeze baseline（版重建 vs 发货 SVG） | **8/8 byte-identical**，repointed files: none；8 个哈希与重建日志逐字相同 | `freeze-baseline-ed.log` |
| freeze baseline（核心重建 vs 发货核心 SVG） | **8/8 byte-identical**（rc=0） | `freeze-baseline-core.log` |
| freeze baseline 字面读法 | `--build` 指核心 svg 目录本身不可行：`ModuleNotFoundError: No module named 'content12'`（rc=1）。该参数按工具 docstring 须为含 run.py 的构建目录；上两行 8/8 已覆盖两种合理解读 | `freeze-baseline-literal.log` |
| freeze diff（核心对照） | 与重建日志逐字相同；新增 CJK 共 9 个，全部为 U+3000（P1 2、其余每页 1）；新增汉字 0 | `freeze-diff.log`、`freeze-diff.json` |
| occlusion 真实审计 | **0 flags**（rc=0）；内置自检 6 类全触发、干净对照静默 | `occlusion.log`、`occlusion.json` |
| p8 extract | **150/150**（rc=0） | `p8-extract.log`、`p8-extract.json` |
| p8 compare vs 核心 | **CLEAN**，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138]（预期，翻译题答案） | `p8-compare.log`、`p8-compare.json`（本体已全文核对） |
| keycheck | **149/150**（rc=0）；唯一不符 #150（开放作文，提取为 `✓`，预期） | `keycheck.log`、`keycheck-150.json` |
| print/web 文字层 | `pdftotext -layout` **逐字节相同 110,367 B**；逐页 8/8 相同；`check_final` 词多重集 diff 0（各 8,507 词），页数 8/8 | `print.txt`、`web.txt`、`print-p[1-8].txt`、`web-p[1-8].txt`、`check-final.log`、`en-textdiff.json` |
| P8 最小字号 | **9.75pt**，低于 9.75pt 0 处；答案区 187 spans、1,543 词 | `minfont.log`、`en-p8size.json` |
| creambox 真墨 | 31 个 OWN 末行全部正余量，**最小真墨底余 +2.1px**，0 溢出；日志与重建逐字节相同 | `creambox.log`、`creambox-diag.log`（与重建 `diff` 无差异） |
| boxtitle | **2 处 OVERFLOW**（见 §1）；日志与重建逐字节相同 | `boxtitle.log`、`boxtitle-trueink.log` |
| sweep | box-vs-hline 0；bridges 20，orphans 0，widows 0 | `sweep.log` |
| 重渲对比（仅 scratch 副本） | 印 PDF 重渲 **SHA 与交付逐字相同**（`782e7cb9…`）；网 PDF 重渲 SHA 浮动（`dc152e57…`，1,139,916 B，预期浮动），**文字层与交付网 PDF 逐字节相同** 110,367 B；重渲印 PDF 文字层亦逐字节相同 | `render-copy.log`、`webpdf-copy.log`、`web-rerender.pdf` |
| D5 gloss（§3） | 4 行、末行右余 +190.5、底余 +42.7、无溢出；与重建宣称逐字相同 | `gloss-probe.log` |

## 3. D5 P4 gloss 核验（只记录数量，不判 (b)，不修）

- en 的 `冠军` 本就映射为 `title`（`tables_en.py:36`：`"冠军": "title"`），无歧义可消；重建只加新 SEG 键 `冠军头衔 → title`（`:37`）与 `墨底 → ink bottom`（`:38`），渲染与 text.md 均不变。
- text.md 与首轮版字节相同：SHA `513326ff…`（§0），`text.md` 第 215 行仍为 `*Note｜o agregado aggregate score · os pênaltis penalty shoot-out · a decisão the final · o título title · a pausa the break · a taça trophy.*`。
- PIL 实测（`gloss_probe.py` 独立重跑）：P4 gloss 盒 `x=989.0 y=270.48 w=422.5 h=175.4`，**4 行、末行右余 +190.5、底余 +42.7、无溢出**——与重建宣称逐字相同。
- SEG 键总数：222（与报告 §8.2 一致）；`冠军 → title`、`冠军头衔 → title`、`墨底 → ink bottom` 均已核实。

## 4. KIT 附录之外的 proof1 旧修复存活复验

| # | 修复 | 核实位置 | 结果 |
|---|---|---|---|
| D1 | P1 刊头标语 | `tables_en.py:199`（首轮笔记称 :197，行号 +2 系新增两行 SEG 键所致，值不变）：`"读巴西人正在读的葡萄牙语": "The Portuguese that Brazil is reading"`；旧形 `The Portuguese Brazil is reading` 全版 0 处；渲染 P1 文字层同值 | 存活 |
| D2 | P4 词表注 | `tables_en.py:36`：`"冠军": "title"`；旧值 `champion` 全版 0 处；渲染 P4 Note 行 `o título title`；P1–P6 词表注 29 项逐项重核全部正确（同首轮 proof2 结论；抽查 feriadão / quilombo / agregado / pênaltis / gabarito / prazo / chute 等无误） | 存活 |
| D3-56/57/58/102 | P8 注冒号 | 发货 `svg/p8-avaliacao.svg` 内 `3 &gt; 1: mais`、`5 &gt; 4: mais`、`16:30 &lt; 17:00: mais cedo`、`cair numa sexta-feira: falls on a Friday` 各 1 处；旧形 0 处 | 存活 |
| 全版冒号复扫 | `:` 后直接接字母 | 8 个 SVG + text.md 均为 **0 处**（时刻 `13:30` 等属数字，已排除；base64 数据已排除） | 存活 |
| hand patch 盘点 | classify 重跑 | **23 KEEP、0 REVERT、0 MERGE/INSERT/DELETE**（bslib4 9、content12 11、content34 1、content56 1、content8 1；与重建宣称一致）——抽查：P1 flash box 436→474、P3 +26、P6 640→654、P8 `max_w=395`、bslib4 `max_w` 管线均在位 | 存活 |

## 5. 150 题逐题手验（题干 + 键 + 题干适配）

- 三源：`text.md` 练习全文（已通读 534 行）+ 渲染 8 页文字层（`print-p[1-8].txt` 已通读）+ REG 键/`p8-extract.json`（`q-table.txt` 150 行已逐条核对）。
- 键：149/150 与提取逐字一致，唯一 #150 为预期 `✓`；keydiff [137, 138] 的译文已验正确（137 `Friday 20 November is a national holiday.`、138 `Palmeiras won 5–4 in the shoot-out.`；139/140 为英→葡，答案为葡语原文，正确）。
- 题干适配（Q73/en-ko 教训）：逐题核对题干是否贴合英文读者——Q73 `Depois da prova, começa a ___.`（espera）题干为通用葡语、无错位；其余如 Q56–59 比较级、Q76–79 将来时、Q93–100 过去时/词框、Q101–112 介词/过去完成/将来虚拟式、Q113–120 完形、Q121–132 阅读理解（Rafael：Salvador / capoeira / Palmeiras × Flamengo / extraoficial）、Q133–136 组句、Q137–140 翻译、Q141–144 配对、Q145–149 对话（Q148 `na internet`，em+a=na 正确）、Q150 开放作文均正确。
- 事实抽查（独立验算）：P6 图表 16–30 日共 15 天（工作日 10 天：16/17/18/19/23/24/25/26/27/30；周末+假日 5 天：20/21/22/28/29），第 10 个工作日 11 月 30 日，27–30 窗口与版内「entre 27 e 30 de novembro, conforme a contagem」一致；星期经 `date -d`（America/Sao_Paulo）核实：11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日——与版内全部星期表述一致；Q150 范文独立数词 **88 词**（含 `×` 计一词），与 REG `model words: 88` 一致。
- 徽章/版式：8 页徽章与核心逐页同数同级（gates.py 16/16 覆盖 P7 引文 2×、披露逐字、图片+来源 5/5、页脚 8/8）；VOL.4 全期正确；P8 答案区 187 spans 最小 9.75pt，恰为下限。
- 孤儿标点扫（`orphan_sweep.py`）：A（`:` 后接字母）0、B（行首孤儿标点）0、D（双空格）0；C（行末 `:`）6 处全为合法引导冒号（如 `No futebol, a final está decidida:`）；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行**逐字相同**，为空格占位符的固有格式，非缺陷；text.md 冒号后接字母 0 处、CJK 仅 U+FF5C ×6（冻结 `Note｜` 标签格式）、U+2019 0。

## 6. 8 页逐页目视（交付印刷 PDF 渲染，110dpi）

- P1：干净；惟 D-B1 标题出盒（见 §1 与 `crop-p1-title.png`）。头条、数字盒、日程、目录、每周一词、快讯、Q1–10、Q7–10 均干净；D1 标语单行完整。
- P2：干净。Q11–28、PARA NÃO ERRAR、Note 框、日程四格均干净；中部大空白为核心版式。
- P3：干净。Q29–46、6 词 Note 框、Zumbi 图注（Parreiras 1927）均干净。
- P4：干净。D2 `o título title` 在版；OS FINALISTAS 数据盒、足球周表、截稿注（10 November）、Q47–64 均干净；P4 gloss 盒 4 行、底余充足（§3）。
- P5：干净。Q65–82、Gary Todd 图注 CC0、五步计划均干净。
- P6：干净。图表算术已独立验算（§5）；Q83–100、时间线盒均干净；Note 框 `o chute a lucky guess` 在盒内。
- P7：干净；惟 D-B2 标题出盒（见 §1 与 `crop-p7-title.png`）。三级语法栏、4 条常见错误、每周一词、读者来信（示例 + 葡/英双语披露，VOL.3→VOL.5 承诺顺延）、8 条金句、VOL.5 预告均干净。
- P8：干净。Q113–150 题面、徽章、G 对话、H 写作题与范文（88 词）、Mané Garrincha 图注、150 条答案注均干净。
- 网页 P1/P8（`web-p1-1.png`、`web-p8-8.png`）与印刷版内容一致；P1 标题出盒在网版同样可见。

## 7. 观察项（不计缺陷）

- **O1** — KIT 第 94 行与 §9 称 `.text.md` 为「535 lines」，实测为 **534 行**（`wc -l` 与 gates.json `text_lines: 534` 一致；与第一轮 proof2 O1 同一问题，KIT 行数口径差 1，非版面内容问题）。
- **O2** — `.text.md` 内实有 6 处 U+FF5C 全角竖线（冻结 `Note｜`/`Key words｜` 标签格式，与核心同格式，非中文文字；与第一轮 proof2 O2 同一口径差异）。
- **O3** — P8 注 55 `taça=the champions' trophy` 与 P4 注 `a taça trophy` 对同一词释义宽严不一（与第一轮 proof2 O6 同一观察）；含义未错，仅释义不一致。
- **O4** — P2/P3/P5/P6 中部大空白与 P2/P4 栏尾孤行（与第一轮 proof2 O4 同一观察，核心版式，与核心一致，非 fan-out 引入）。
- **O5** — P6 Note 框 `o chute a lucky guess`：`chute` 未出现在 P6 文章正文，但出现在当页 D 组词框与 Q100 题面，且核心中文注同样释 `chute`（与第一轮 proof2 O5 同一观察，核心版式、忠实转译）。
- **O6** — D5 字体只记录数量：P4 gloss 盒 4 行、末行右余 +190.5、底余 +42.7（§3）；不判 (b)，不修。
- **O7** — `classify_pt.py` 的输出文件写在其自身目录（重建 scratch）内；本次运行重写了重建的 `en-classify.json`（确定性内容，计数未变：23 KEEP；已复制一份至本 scratch 备查）。
- **O8** — §1 缺陷的第一轮来源：两处标题溢出在第一轮版中已存在（`boxtitle-backup.log` 数值逐字相同），第一轮 proof2 仅以 O3「标题贴盒右缘」记录、未量测；本次为首次以真墨量测 + 目视确认。

## 8. 结论（报事实，不作定稿决定）

- 本轮独立全量复校发现 **缺陷 2 项**（§1：D-B1、D-B2，均为盒标题真墨溢出盒右缘），其余全部机械门、150 题、8 页文字层、事实抽查均通过。
- 结论 **(b)**：有缺陷待修。按 SOP §8.4，一整轮全量校对须零问题方可定稿；是否定稿由协调员决定。
- 本轮未修改任何成品；版目录 47 个文件开工前后 SHA 全量复核零改动；全部校对证据在 `scratch-proof-pt-en2/`（本笔记 + `GATE-LOG.md` + 各门日志/JSON + `render/` 12 张渲染图 + `build-copy/` 重跑副本 + `freeze-pt-en/`、`freeze-pt-core/`）。

## 附：三 SHA（完整串）

- 印刷 PDF `A-Lucerna-VOL4.pdf`：12,932,439 字节；sha256 `782e7cb9d9109f4282667fd6dde71ab981933fa5290a9cd4882aaa49322cca6d`；8 页。
- 网页 PDF `A-Lucerna-VOL4-web.pdf`：1,139,921 字节；sha256 `e02cf58cbee4cf5daac47fccc9319faf8158b6b31523ba220794f415a5e9bb61`；8 页；文字层 110,367 字节（pdftotext -layout）。
- 文字 `2026-w47-pt-en.text.md`：37,333 字节；sha256 `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed`；534 行。
