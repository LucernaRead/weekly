# GATE-LOG — 2026-W47 pt-es（重建版，proof1）

校对时间：2026-11-11。解释器（全部）：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3，各工具 runtime 行自证；pt 家族规范）。`PYTHONDONTWRITEBYTECODE=1` 全程开启，`TMPDIR=<scratch>/tmp`（未用系统 /tmp）。
生产目录只读；`run.py` / `render.py` / `webpdf.py` / keycheck 只在 scratch 内 `build-copy/` 运行。版目录 47 个文件开工前后 SHA 全量复核零改动（`prod-snapshot.sha256`）；core-pt 41 个文件零改动（`core-snapshot.sha256`）。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-es2/`

## §0 身份核对（磁盘为准）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0；`/dev/null` 存在（crw-rw-rw-）。
- 印 PDF `A-Lucerna-VOL4.pdf`：SHA256 `f1b4fc207a3575391868aeb9c8f7d0f34659c434ecf3a13c85c8cba19362a0d4` / **12,933,062 B**——与任务书逐字一致。
- 网 PDF `A-Lucerna-VOL4-web.pdf`：SHA256 `d00e8f5420750496b7cb7551eab51e7207a123b1c3f0a55896aead83dac4ae7c` / **1,140,276 B**——与任务书逐字一致。
- text.md `2026-w47-pt-es.text.md`：SHA256 `96d6f11a5616ab97291115bb9da0577bce8049031f14988576f6cced77b29e27` / **37,467 B**——与任务书逐字一致。

| # | 门 | 命令 / 位置 | 日志 | rc | 实测值 |
|---|---|---|---|---|---|
| 1 | run.py 重跑 | `build-copy/` 内 `python run.py` | `run-rebuild.log` | 0 | `TOTAL 150`；`by level {'A2': 48, 'B1': 71, 'B2': 31}`；`by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；`model words: 88`；`OVERFLOW`/`TOO WIDE` 0 处（grep 0 命中）；末行 `ALL DONE` |
| 2 | SVG 重建一致 | `build-copy/svg` vs 发货 `svg/`，8 文件逐一 sha256 | （本文件 §1） | — | **8/8 字节一致** |
| 3 | gates.py 16/16 | 版目录内 `python gates.py`（只读，仅 open 读） | `gates-edition.log` | 0 | `[PASS]` 16 行；`FAILURES: none`（最小页框边距 L/R/T/B = 47.0/44.5/35.0/32.0；P1 头条 41 字符 ≤56；gloss 29 项；P7 金句 8 条 2×+页签+西语；图片+credits 5/5；P7 金句区 clears 预告框，最大基线 2380.67 < 2404） |
| 4 | freeze baseline（核心） | `tools/freeze.py baseline --build <core-pt> --core-svg <core-pt>/svg --out freeze-core` | `freeze-baseline-core.log` | 0 | **8/8 byte-identical**，repointed files: none；p1 `bd87a867…`、p2 `0a8300c3…`、p3 `e3c97081…`、p4 `f539bdb8…`、p5 `51629e93…`、p6 `a3c3cf38…`、p7 `43b845fc…`、p8 `a7b7a661…`；core integrity：发货核心 SVG 前后重哈希一致 |
| 5 | freeze baseline（版） | `tools/freeze.py baseline --build <版目录> --core-svg <版目录>/svg --out freeze-ed` | `freeze-baseline-ed.log` | 0 | **8/8 byte-identical**，repointed files: none；p1 `d30c2ee6…`、p2 `0be39d1c…`、p3 `f6095d0a…`、p4 `3148d4b9…`、p5 `31241efb…`、p6 `61863d5c…`、p7 `22ce3ac7…`、p8 `0febf48d…`；core integrity 一致 |
| 6 | freeze diff | `tools/freeze.py diff --core-svg <core-pt>/svg --edition-svg <版>/svg --json freeze-diff.json` | `freeze-diff.log`、`freeze-diff.json` | 0 | p1 +26/−39、p2 +41/−33、p3 +34/−29、p4 +30/−26、p5 +41/−48、p6 +25/−22、p7 +52/−46、p8 +189/−753；**新增 CJK 共 9 个，全部 U+3000**（P1 2、其余每页 1）；新增汉字 0 |
| 7 | occlusion 真实审计 | `tools/occlusion_audit.py <版>/svg --json occlusion.json`（非 `--selftest`） | `occlusion.log`、`occlusion.json` | 0 | 内置自检 `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；审计 `<版>/svg: 0 flags`；`flag_count: 0` |
| 8 | p8 extract | `tools/p8.py extract --p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-extract.json` | `p8-extract.log`、`p8-extract.json` | 0 | `noted set = 150 of 150 (parse: lines)` |
| 9 | p8 compare | `tools/p8.py compare --core-p8 <core-pt>/svg/p8-avaliacao.svg --edition-p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-compare.json` | `p8-compare.log`、`p8-compare.json`（本体已全文核对） | 0 | `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`（预期：翻译题答案） |
| 10 | keycheck | 本 scratch 副本 `keycheck_core.py <build-copy> p8-extract.json` | `keycheck.log`、`keycheck-150.json` | 0 | `REG entries: 150; p8extract keys: 150`；**exact match 149/150**；唯一 `MISMATCH n=150 type=Escritura: key='(ejercicio abierto — texto modelo abajo)' extracted='✓'`（预期：开放作文） |
| 11 | Respostas 三方一致 | `resp_compare2.py`（text.md Respostas vs REG 键） | `resp-compare.log` | 0 | 150/150 解析；**不符 0**（Q150 除外：Respostas 为 `✓ Ver el texto modelo…(88 palabras)`，与 REG 开放题注述同义） |
| 12 | 印/网文字层 | `pdftotext -layout` 印/网全文 + 逐页 8/8 `cmp` | `print.txt`、`web.txt`、`print-p[1-8].txt`、`web-p[1-8].txt` | 0 | 全文 `cmp` 相同，**109,231 B**；逐页相同：P1 14,131 B、P2 11,247 B、P3 9,512 B、P4 9,333 B、P5 9,467 B、P6 12,379 B、P7 12,301 B、P8 30,861 B |
| 13 | check_final | 本 scratch 副本 `check_final.py <版目录>` | `check-final.log`、`es-textdiff.json`、`es-p8size.json` | 0 | `pages print=8 web=8`；`words print=8576 web=8576 multiset-diff=0`；`diff sample: []`；`P8 answer-region span count: 185 min size: 9.75`；`word count: 1607` |
| 14 | P8 最小字号 | 本 scratch 副本 `minfont.py <印 PDF>` | `minfont.log` | 0 | `P8 min effective font size = 9.75 pt (n=372)`；`below 9.75pt: 0` |
| 15 | creambox | 本 scratch 副本 `creambox.py <版>/svg/*.svg` | `creambox.log` | 0 | 全 8 页 31 框；负余量 4 处均为盒外后继标题行（见门 16 裁决）；D1 框底 2348.0、末行基线 2327.6、余量 **+20.4**；D2 框底 551.0、`16h30.` 余量 **+10.4**；D3 框底 854.0、`Página do Participante.` 余量 **+13.2** |
| 16 | creambox 真墨裁决 | 本 scratch 副本 `creambox_diag.py <版>/svg/*.svg` | `creambox-diag.log` | 0 | 31 个 OWN 末行；真墨底余最小 **−0.3px**（2 处：P4 E VOCÊ 框、P7 词框）；其余 ≥ +0.3px；D1 真墨底余 **+15.4**、D2 **+10.1**、D3 **+8.0**；3 处 below-window 行均为 owner-rect=NONE 的后继标题/分隔线，非溢出 |
| 17 | −0.3px 两处卡片裁决 | `card_probe.py`（重渲卡片 PIL，亮度<190） | `card-probe.log` | 0 | P4 E VOCÊ 框底 876 以下是 **0 个深色像素**（30px 窗口）；P7 词框底 1461 以下是 **0 个深色像素**；P2 E VOCÊ 框底 909 以下 0 个；P5 框底 811 以下首现为 837 行的 396px 通栏分隔线（后继内容，非本框末行）。−0.3px 为字体度量 artifact，非缺陷 |
| 18 | boxtitle（advance） | 本 scratch 副本 `boxtitle_core.py <版>/svg` | `boxtitle.log` | 0（注：脚本无非零退出路径，rc 为空洞信号） | 30 盒；**1 处 `<<<< OVERFLOW`**：P1 `EM POUCAS PALAVRAS　EN BREVE` title_w=404.1 right=1865.6 clear=−3.6；其余最小正余量 +10.5（P1 `A SEMANA EM NÚMEROS　En cifras`） |
| 19 | boxtitle 真墨（PIL，逐元素本字号） | 本 scratch 自写 `boxtitle_trueink.py`（版内 svglib `_pil` + getbbox anchor='ls'，与 gates.py 同款；标题用各自实际字号，不强制 23pt） | `boxtitle-trueink.log` | 0 | 30 盒；**1 处 `<<<< TRUE-INK OVERFLOW`**：P1 EN BREVE 真墨右缘 1865.5、框右 1862.0、clear **−3.5**；D4 P2 `PARA NÃO ERRAR　La regla` 真墨 863.5、clear **+97.5**；D5 P7 `ERROS COMUNS　Errores` 真墨 1750.5、clear **+111.5**；D6 P7 `A PALAVRA　La palabra` 真墨 1724.5、clear **+137.5**；其余最小 +10.5 |
| 20 | boxtitle PDF 渲染交叉验证 | 本 scratch 自写 `pdf_render_titles.py`（交付印 PDF 经 pdftoppm 96dpi 渲染，1:1 SVG 单位；逐盒量标题行最右深色像素） | `pdf-render-titles.log` | 0 | 30 盒；**1 处 `<<<< PDF-RENDER OVERFLOW`**：P1 EN BREVE 渲染墨右 1865、clear **−3**（列计数：x=1863 有 9px、1864 有 6px、1865 有 2px 深色像素）；其余最小 +12（P1 `A SEMANA EM NÚMEROS` +12、P2 `Palmeiras × Flamengo, às` +22、P1 `NESTA EDIÇÃO` +22）；D4 +98、D5 +112、D6 +138 |
| 21 | D1/D2/D3 PDF 渲染复核 | 同上（逐行深色像素计数） | `pdf-render-titles.log` 末尾 | 0 | D1：末行墨止于 2331，框底 2348（**+17**）；2349–2350 行为 422px 通栏分隔线（盒外 quiz 分隔线，非文本溢出）；D2：末行墨止于 539，框底 551，框下无深色行；D3：降部墨止于 844，框底 854，框下无深色行。**三处均已修复** |
| 22 | D7 P8 范文 PDF 渲染复核 | `card_probe3` 方法重跑于交付印 PDF 渲染（逐行精确带） | `card-probe2.log`（卡片）+ §21 同方法 | 0 | 10 行范文：PDF 渲染最右墨 1829、最小余量 **+33**；卡片最右墨 1840、最小余量 +22。首轮 D7（+2/+14）**已消失**；范文已重排（第 2–3 行现为 `despertador…leio sobre` / `Zumbi e Palmares…`） |
| 23 | sweep | 本 scratch 副本 `sweep_de.py <版目录>` | `sweep.log` | 0 | `box-vs-hline flags: 0`；`bridges found: 20`；`bridge orphans: 0`；`bridge widows: 0` |
| 24 | 孤儿标点扫 | 本 scratch 副本 `orphan_sweep.py`（8 SVG + text.md） | `orphan-sweep.log` | 0 | A（`:` 后接字母）4 处：均为 P8 答案行 `56. mais — 3 > 1:mais` / `57. …:mais` / `58. …:mais cedo` / `102. …:cae en viernes`——键值分隔符，与核心版同格式，p8 compare CLEAN；B（行首孤儿）0；C（行末 `:`）6 处全为合法引导冒号；D（双空格）0；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，空白占位符固有格式；text.md 冒号后接字母 0 |
| 25 | 弯引号 / CJK / 禁词 | 计数扫描（8 SVG + text.md） | （本文件 §2） | 0 | text.md：`“` 2、`”` 2、`’` 0（仅 P8 E139/E140 西班牙语句）；直引号 `"` 0；CJK 表意字 0；U+FF5C `｜` ×6（gloss 分隔符，与 en 版同数）；U+3000 text.md 0；SVG：p8 `“`/`”` 各 2、其余页 0；p1 另有 3 个表意字，皆属 moth logo 内部 `<title>Lucerna 三色蛾</title>`（不可见元数据）；禁词扫描（翻译/翻譯/简体/SOP/TODO/placeholder/lorem/XXX）text.md 0 命中 |
| 26 | 150 题手验 | 全文通读 text.md 534 行 + 渲染文字层 8 页 + `keycheck-150.json` + Respostas 三方比对 | `keycheck-150.json`、`resp-compare.log`、`print-p[1-8].txt` | — | **150/150 题干与键逐项适配**（见 PROOF-NOTE §4）；含 Q73 `espera`、Q137/138 译文、Q139/140 反向翻译、Q148 `na internet`、Q125 36 轮、Q83–86 图表算术 10+5=15、范文 88 词手数 |
| 27 | 星期核实 | `date -d`（America/Sao_Paulo） | （本文件 §2） | 0 | 11-07 周六、11-08 周日、11-15 周日、11-16 周一、11-17 周二、11-18 周三、11-19 周四、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日——全部与版面一致 |
| 28 | 8 页目视 | 交付印 PDF `pdftoppm -r 96` 全 8 页 | `render/print-p-[1-8].png` | — | 8/8 页已目视；除门 20 的 P1 标题出盒（3px，需放大可见）外无可见缺陷；网 P1/P8 抽查与印版内容一致（P1 出盒在网版同见） |
| 29 | 重渲对比（仅 scratch） | `build-copy/` 内 `render.py` + `tools/webpdf.py <build-copy>/svg web-rerender.pdf` | `render-copy.log`、`webpdf-copy.log`、`web-rerender.pdf`、`web-rerender.txt` | 0 / 0 | 重渲印 PDF **SHA 与交付逐字相同** `f1b4fc20…`（12,933,062 B）；重渲网 PDF SHA 浮动（`c792a22b…`，1,140,275 B，预期浮动——fontTools 嵌时间戳），**文字层与交付网 PDF 逐字节相同** 109,231 B；重渲印 PDF 文字层亦逐字节相同 |
| 30 | 补充检查 S1（P2 PARA 标题） | `supp_checks.py`（PIL 23pt 粗体真墨 + PDF 渲染像素 + 3× 裁图） | `supp-checks.log`、`p2-para-title-pdf.png` | 0 | SVG 标题元素 x=556.5 y=642.02 fs=23 bold；PIL 真墨右 863.5、clear **+97.5**；advance 右 863.7；PDF 渲染最右深色像素 863、clear **+98**。**通过**；pt-it 版 −59.5 在本版不复现（西语 gloss `La regla` 仅 9 字符，意语 `La regola da ricordare` 21 字符） |
| 31 | 补充检查 S2（P1 顶栏标语） | `supp_checks.py`（tables_es.py:201 核对 + SVG 顶栏几何 + 改后行宽量测）+ 西班牙语语法独立判定 | `supp-checks.log`、PROOF-NOTE §5 | 0 | 见 PROOF-NOTE §5：原句语法成立，**不记缺陷**（观察项 O-S1，附完整语法依据）；改后句 `El portugués que leen los brasileños` 量测：17pt + letter-spacing 1.7，居中于 x=975 时跨度 [577.6, 1372.4]，在版心 [88, 1862] 内，左栏（止于 327.2）余量 +250、右栏（起于 1459.5）余量 +87，**放得下** |
| 32 | 生产目录未改动 | 开工 `sha256sum` 快照 vs 收工复核 | `prod-snapshot.sha256`、`core-snapshot.sha256` | — | 版目录 47 个文件 `sha256sum -c` 全 OK；core-pt 41 个文件全 OK；**零改动** |

## §1 run.py 重建 SVG 一致性（门 2 明细）

```
p1-capa.svg IDENTICAL
p2-vida.svg IDENTICAL
p3-cultura.svg IDENTICAL
p4-esporte.svg IDENTICAL
p5-jovens.svg IDENTICAL
p6-aprofundamento.svg IDENTICAL
p7-lingua.svg IDENTICAL
p8-avaliacao.svg IDENTICAL
```

## §2 其余机械事实

- 8 页，1950×2700，4 栏；页数 8（4 的倍数）；VOL.4。
- 150 题分布与 KIT 一致（每页 10/18/18/18/18/18/12/38）；题号连续无缺重（p8 extract 150/150）。
- 5 图与核心字节相同（KIT §3；gates 5/5 PASS）。
- P7 金句 8 条，每条正文出现 2× + 页签 + 西语译文（gates PASS）。
- 读者来信栏：葡语示例 + 葡语披露原文 + 西语披露译文 + 示例标签 5/5（gates PASS）；无真实来信（F-MAIL 规则，仅用户直发计入）。
- **check_s11**：仓库与 pt 家族内不存在名为 `check_s11` 的脚本或检查（`grep -rn s11 --include='*.py' --include='*.md'` 于 SOP.md、版目录、tools/ 均无命中）；本版的等效检查为 gates.py 16 项（门 3）+ check_final.py（门 13），均已跑过并全 PASS。特此记录，不作假数。
- **D5 字体问题**：只记录，不判。P7 A2 gloss 用 ASCII 单引号 `'caer en un día'`（text.md 直引号撇号 2 处，即此一对）；拉丁解释层在 Noto Sans CJK SC 的字体事为已知待用户裁定的事，不作缺陷。

## 未通过的门

- **门 18/19/20（boxtitle 真墨 0 溢出）：1 处溢出**——P1 `EM POUCAS PALAVRAS　EN BREVE`：advance −3.6、PIL 真墨 −3.5、交付 PDF 渲染 −3px。详见 PROOF-NOTE.md §1。结论 **(b)**。
