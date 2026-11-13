# GATE-LOG — 2026-W47 pt-en（重建版，proof1）

校对时间：2026-11-11 15:33–约 16:00 EST。解释器（全部）：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3；各工具 runtime 行自证）。`PYTHONDONTWRITEBYTECODE=1` 全程开启。生产目录只读；`run.py` / `render.py` / `webpdf.py` / keycheck 只在 `build-copy/` 内运行。版目录 47 个文件开工前后 SHA 全量复核零改动（`prod-snapshot.sha256`）。

| # | 门 | 命令 / 位置 | 日志 | rc | 实测值（源行） |
|---|---|---|---|---|---|
| 0 | 身份 | `sha256sum` + `stat` 三文件 | 本文件 | — | 印 `782e7cb9d9109f4282667fd6dde71ab981933fa5290a9cd4882aaa49322cca6d` / 12,932,439 B；网 `e02cf58cbee4cf5daac47fccc9319faf8158b6b31523ba220794f415a5e9bb61` / 1,139,921 B；文 `513326ffa497ca2b6714c1016eadbfaa2ac3447269b782749c968022e0e118ed` / 37,333 B——与任务书逐字一致 |
| 1 | run.py 重跑 | `build-copy/` 内 `python run.py` | `run-rebuild.log` | 0 | `TOTAL 150`；`by level {'A2': 48, 'B1': 71, 'B2': 31}`；`by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；`model words: 88`；`FLOW OVERFLOW` 0 处；`TOO WIDE` 0 处；末行 `ALL DONE` |
| 2 | gates.py 16/16 | 版目录内 `python gates.py`（只读） | `gates-edition.log` | 0 | `[PASS]` 16 行；`FAILURES: none` |
| 3 | freeze baseline（版） | `tools/freeze.py baseline --build <版目录> --core-svg <版目录>/svg --out freeze-pt-en` | `freeze-baseline-ed.log` | 0 | `baseline: 8/8 SVGs byte-identical (repointed files: none)`；8 哈希与重建 `en-freeze.log` 逐字相同（p1 `164d2c52…`、p2 `3473dabd…`、p3 `a9bb5c13…`、p4 `93559314…`、p5 `3ca31fbe…`、p6 `1005050c…`、p7 `3760e251…`、p8 `4829faec…`）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)` |
| 4 | freeze baseline（核心） | `tools/freeze.py baseline --build <core-pt> --core-svg <core-pt>/svg --out freeze-pt-core` | `freeze-baseline-core.log` | 0 | `baseline: 8/8 SVGs byte-identical (repointed files: none)`（p1 `bd87a867…`、p2 `0a8300c3…`、p3 `e3c97081…`、p4 `f539bdb8…`、p5 `51629e93…`、p6 `a3c3cf38…`、p7 `43b845fc…`、p8 `a7b7a661…`） |
| 5 | freeze baseline（字面读法） | `tools/freeze.py baseline --build <core-pt>/svg --core-svg <core-pt>/svg --out freeze-literal` | `freeze-baseline-literal.log` | 1 | `ModuleNotFoundError: No module named 'content12'`——`--build` 按工具 docstring 须为含 run.py 的构建目录，核心 svg 目录本身不可行；门 3/4 已覆盖两种合理解读 |
| 6 | freeze diff | `tools/freeze.py diff --core-svg <core-pt>/svg --edition-svg <版>/svg --json freeze-diff.json` | `freeze-diff.log`、`freeze-diff.json` | 0 | p1 +27/−39、p2 +39/−33、p3 +32/−29、p4 +30/−26、p5 +41/−48、p6 +25/−22、p7 +52/−46、p8 +191/−753；`TOTAL added CJK characters: 9`，全部 U+3000（P1 2、其余每页 1）；新增汉字 0；与重建 `en-freeze-diff.log` 逐字相同 |
| 7 | occlusion 真实审计 | `tools/occlusion_audit.py <版>/svg --json occlusion.json`（非 `--selftest`） | `occlusion.log`、`occlusion.json` | 0 | 内置自检行 `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；审计行 `<版>/svg: 0 flags` |
| 8 | p8 extract | `tools/p8.py extract --p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-extract.json` | `p8-extract.log`、`p8-extract.json` | 0 | `noted set = 150 of 150 (parse: lines)` |
| 9 | p8 compare | `tools/p8.py compare --core-p8 <core-pt>/svg/p8-avaliacao.svg --edition-p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-compare.json` | `p8-compare.log`、`p8-compare.json`（本体已全文核对） | 0 | `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]` |
| 10 | keycheck | 本 scratch 副本 `keycheck_core.py <build-copy> p8-extract.json` | `keycheck.log`、`keycheck-150.json` | 0 | `REG entries: 150; p8extract keys: 150`；`exact match: 149/150`；唯一 `MISMATCH n=150 page=8 type=Writing: key='(open task — model text below)' extracted='✓'`（预期） |
| 11 | 印/网文字层 | `pdftotext -layout` 印/网 + 逐页 8/8 `cmp` | `print.txt`、`web.txt`、`print-p[1-8].txt`、`web-p[1-8].txt` | 0 | 全文 `cmp` 相同，110,367 B；逐页相同：P1 14,269 B、P2 11,124 B、P3 9,547 B、P4 9,310 B、P5 9,428 B、P6 12,168 B、P7 12,333 B、P8 32,188 B |
| 12 | check_final | 本 scratch 副本 `check_final.py <版目录>` | `check-final.log`、`en-textdiff.json`、`en-p8size.json` | 0 | `pages print=8 web=8`；`words print=8507 web=8507 multiset-diff=0`；`diff sample: []`；`P8 answer-region span count: 187 min size: 9.75`；`word count: 1543` |
| 13 | P8 最小字号 | 本 scratch 副本 `minfont.py <印 PDF>` | `minfont.log` | 0 | `P8 min effective font size = 9.75 pt (n=375)`；`below 9.75pt: 0` |
| 14 | creambox | 本 scratch 副本 `creambox.py <版>/svg/*.svg` | `creambox.log` | 0 | 全量盒行与重建 `en-creambox.log` `diff` 无差异；负余量行 4 处均为盒外标题行（见门 15 裁决） |
| 15 | creambox 真墨裁决 | 本 scratch 副本 `creambox_diag.py <版>/svg/*.svg` | `creambox-diag.log` | 0 | 31 个 OWN 末行；真墨底余最小 **+2.1px**（P2 `Palmeiras–Flamengo clash`），其余 +4.8 及以上；**0 溢出**；与重建 `en-creambox-diag.log` `diff` 无差异 |
| 16 | boxtitle | 本 scratch 副本 `boxtitle_core.py <版>/svg` | `boxtitle.log` | 0（注：脚本无非零退出路径，rc 为空洞信号） | **2 处 `<<<< OVERFLOW`**：P1 `box x=989..1412 y=786 title y=823.2 … title_w=426.5 right=1433.5 clear=-22.0`（`A SEMANA EM NÚMEROS　In numbers`）；P7 `box x=1440..1862 y=200 title y=242.0 … title_w=415.0 right=1876.5 clear=-14.5`（`ERROS COMUNS　Common mistakes`）；其余 29 盒最小正余量 +22.2px；与重建 `en-boxtitle.log` `diff` 无差异 |
| 17 | boxtitle 真墨复核 | `boxtitle_trueink.py`（`svglib._pil` + `getbbox anchor='ls'`，与 gates.py 同款） | `boxtitle-trueink.log` | 0 | P1 真墨右缘 1434.0，盒右缘 1411.5，**clear −22.5，出盒 YES**；P7 真墨右缘 1876.5，盒右缘 1862.0，**clear −14.5，出盒 YES** |
| 18 | boxtitle 对照 | 同工具跑核心版 + 第一轮备份版 | `boxtitle-core.log`、`boxtitle-backup.log` | — | 核心版 OVERFLOW **0 处**；第一轮备份版 OVERFLOW 2 处，与本版数值逐字相同（P1 −22.0、P7 −14.5） |
| 19 | sweep | 本 scratch 副本 `sweep_de.py <版目录>` | `sweep.log` | 0 | `box-vs-hline flags: 0`；`bridges found: 20`；`bridge orphans: 0`；`bridge widows: 0` |
| 20 | D5 gloss PIL 实测 | 本 scratch 副本 `gloss_probe.py <版目录>` | `gloss-probe.log` | 0 | `GLOSS VERDICT: lines=4 last-line right clear +190.5 last-line bottom clear +42.7 overflow=no`（盒 x=989.0 y=270.48 w=422.5 h=175.4）；与重建宣称逐字相同 |
| 21 | classify（hand patch） | 本 scratch 副本 `classify_pt.py en` | `classify.log`、`en-classify.json` | 0 | `en COUNTS: {'KEEP': 23}`；分文件 bslib4 9、content12 11、content34 1、content56 1、content8 1，其余 0；REVERT/MERGE/INSERT/DELETE 0 |
| 22 | D1/D2/D3 存活 | `grep` 表 + SVG + 渲染文字层 | PROOF-NOTE §4 | — | D1 `tables_en.py:199` 新标语在位、旧形 0；D2 `tables_en.py:36` `"冠军": "title"`、旧值 `champion` 0、渲染 `o título title`；D3 四处各 1 处、旧形 0；全版 `:` 后接字母 0 处（8 SVG + text.md） |
| 23 | SEG 键 | `tables_en.py` 导入计数 | — | — | SEG 222 键；`冠军 → title`（:36）、`冠军头衔 → title`（:37）、`墨底 → ink bottom`（:38） |
| 24 | text.md | `wc` + 行抽查 | — | — | 534 行、37,333 B；L215 gloss 行含 `o título title`；L433 `### Frases da semana (verbatim from this issue)`；`(verbatim from this issue)` ×1；CJK 仅 U+FF5C ×6；U+2019 0 |
| 25 | ABSTRACT.txt | `wc` + 全文 | — | — | 561 字节，英文单段，含刊头 `A Lucerna Portuguese Weekly VOL.4:` |
| 26 | 150 题手验 | 通读 `text.md` 534 行 + 渲染文字层 8 页 + `q-table.txt` 150 行 | `q-table.txt`、`print-p[1-8].txt` | — | 键 149/150 一致（唯一 #150 预期）；题干逐题核对无误（含 Q73 `espera` 适配、Q137/138 译文、Q148 `na internet`、Q150 范文手数 88 词）；P6 图表算术独立验算 10+5=15；星期 `date -d`（America/Sao_Paulo）8 个日期全部一致 |
| 27 | 孤儿标点扫 | `orphan_sweep.py`（8 SVG + text.md） | `orphan-sweep.log` | 0 | A（`:` 后接字母）0；B（行首孤儿标点）0；C（行末 `:`）6 处全为合法引导冒号；D（双空格）0；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，空白占位符固有格式 |
| 28 | 8 页目视 | 交付印 PDF `pdftoppm -r 110`；网 P1/P8 抽查 | `render/print-p[1-8]-*.png`、`render/web-p1-1.png`、`render/web-p8-8.png`、`render/crop-p1-title.png`、`render/crop-p7-title.png` | — | 8/8 页已目视；除门 16/17 的两处标题出盒外无可见缺陷；网 P1/P8 与印刷版内容一致（P1 出盒在网版同见） |
| 29 | 重渲对比（仅 scratch） | `build-copy/` 内 `render.py` + `tools/webpdf.py <build-copy>/svg web-rerender.pdf` | `render-copy.log`、`webpdf-copy.log`、`web-rerender.pdf`、`web-rerender.txt`、`print-rerender.txt` | 0 / 0 | 重渲印 PDF **SHA 与交付逐字相同** `782e7cb9…`（12,932,439 B）；重渲网 PDF SHA 浮动（`dc152e57…`，1,139,916 B，预期浮动），**文字层与交付网 PDF 逐字节相同** 110,367 B；重渲印 PDF 文字层亦逐字节相同 |
| 30 | 生产目录未改动 | 开工 `sha256sum` 快照 vs 收工复核 | `prod-snapshot.sha256` | — | 47 个文件 `sha256sum -c` 全 OK，零改动 |

## 未通过的门

- **门 16/17（boxtitle 真墨 0 溢出）：2 处溢出**——D-B1（P1，−22.5px）、D-B2（P7，−14.5px）。详见 PROOF-NOTE.md §1。结论 **(b)**。
