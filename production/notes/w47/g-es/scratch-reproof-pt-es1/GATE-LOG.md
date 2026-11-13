# GATE-LOG — 2026-W47 pt-es（reproof，fix1 后独立复校）

复校时间：2026-11-11。解释器（全部）：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3，各工具 runtime 行自证；pt 家族规范）。`PYTHONDONTWRITEBYTECODE=1` 全程开启，`TMPDIR=<scratch>/tmp`（未用系统 /tmp）。
生产目录改动：**零**（开工/收工 `sha256sum -c` 复核：版目录 43 文件、core-pt 38 文件全 OK；`__pycache__` 除外计数，fix1 的 47/41 含 pycache）。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-es1/`
前置：开工三 SHA 与任务书逐字一致（印 `75e870cf…` / 12,933,061 B；网 `4e7b30ea…` / 1,140,280 B；文 `96d6f11a…` / 37,467 B）；收工复核不变。

## §0 门总表（全部在 build-copy 内先跑，再对生产交付态复验）

| # | 门 | 命令 / 位置 | 日志 | rc | 实测值 |
|---|---|---|---|---|---|
| 1 | run.py 重跑 | `build-copy/` 内 `python run.py` | `run-rebuild.log` | 0 | `TOTAL 150`；`by level {'A2': 48, 'B1': 71, 'B2': 31}`；`by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；`model words: 88`；`OVERFLOW`/`TOO WIDE` 0 处；末行 `ALL DONE` |
| 2 | SVG 重建一致 | `build-copy/svg` vs 发货 `svg/`，8 文件逐一 `cmp` | （本文件 §1） | — | **8/8 字节相同** |
| 3 | render.py（印 PDF） | `build-copy/` 内 `python render.py` | `render-copy.log` | 0 | 8 卡片 + 印 PDF 12,933,061 B；SHA `75e870cf…`（与交付件逐字相同） |
| 4 | webpdf.py（网 PDF） | `tools/webpdf.py build-copy/svg web-rerender.pdf`（只在 scratch 内） | `webpdf-copy.log` | 0 | 8 页，116 字符，8 字体子集；1,140,276 B（交付件 1,140,280 B，差 4 B 为已知 wall-clock 不可复现）；文字层与交付网 PDF 逐字节相同（109,229 B） |
| 5 | gates.py 16/16 | 生产目录内 `python gates.py`（只读）+ build-copy 内同跑 | `gates-production.log` / `gates-copy.log` | 0 / 0 | `[PASS]` 16 行；`FAILURES: none`（最小页框边距 L/R/T/B = 47.0/47.5/35.0/32.0；P1 头条 41 字符 ≤56；gloss 29 项；P7 金句 8 条 2×+页签+西语；图片+credits 5/5；P7 金句区 clears 预告框，最大基线 2380.67 < 2404） |
| 6 | freeze baseline（核心） | `tools/freeze.py baseline --build <core-pt> --core-svg <core-pt>/svg --out freeze-core` | `freeze-baseline-core.log` | 0 | **8/8 byte-identical**，repointed files: none；p1 `bd87a867…`、p2 `0a8300c3…`、p3 `e3c97081…`、p4 `f539bdb8…`、p5 `51629e93…`、p6 `a3c3cf38…`、p7 `43b845fc…`、p8 `a7b7a661…`（与 proof1/fix1 逐字一致） |
| 7 | freeze baseline（版） | `tools/freeze.py baseline --build <版目录> --core-svg <版目录>/svg --out freeze-ed` | `freeze-baseline-ed.log` | 0 | **8/8 byte-identical**，repointed files: none；p1 `092e2d3d…`（新 hash——仅此页变）、p2 `0be39d1c…`、p3 `f6095d0a…`、p4 `3148d4b9…`、p5 `31241efb…`、p6 `61863d5c…`、p7 `22ce3ac7…`、p8 `0febf48d…`（p2–p8 与 proof1/fix1 逐字一致）；core integrity 一致 |
| 8 | freeze diff | `tools/freeze.py diff --core-svg <core-pt>/svg --edition-svg <版>/svg --json freeze-diff.json` | `freeze-diff.log`、`freeze-diff.json` | 0 | p1 +26/−39、p2 +41/−33、p3 +34/−29、p4 +30/−26、p5 +41/−48、p6 +25/−22、p7 +52/−46、p8 +189/−753；**新增 CJK 共 9 个，全部 U+3000**（P1 2、其余每页 1）；新增汉字 0（与 proof1/fix1 一致） |
| 9 | occlusion 真实审计 | `tools/occlusion_audit.py <版>/svg --json occlusion.json`（非 `--selftest`） | `occlusion.json`、`occlusion.log` | 0 | 内置自检 `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；审计 `0 flags`；`flag_count: 0` |
| 10 | p8 extract | `tools/p8.py extract --p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-extract.json` | `p8-extract.log` | 0 | `noted set = 150 of 150 (parse: lines)` |
| 11 | p8 compare | `tools/p8.py compare --core-p8 <core-pt>/svg/p8-avaliacao.svg --edition-p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-compare.json` | `p8-compare.log`、`p8-compare.json` | 0 | `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`（预期：翻译题答案） |
| 12 | keycheck | 本 scratch 副本 `keycheck_core.py <build-copy> p8-extract.json`（内含 run.py 重跑） | `keycheck.log`、`keycheck-150.json` | 0 | `REG entries: 150; p8extract keys: 150`；**exact match 149/150**；唯一 `MISMATCH n=150 type=Escritura: key='(ejercicio abierto — texto modelo abajo)' extracted='✓'`（预期：开放作文） |
| 13 | Respostas 三方一致 | 本 scratch 自写 `resp_compare_fix.py`（修正版，见 §6） | `resp-compare.log` | 0 | 页眉归一化 8 处；150/150 解析，missing []；**不符 0**（Q150 除外：Respostas 为 `✓ Ver el texto modelo…(88 palabras)`，与 REG 开放题注述同义） |
| 14 | 印/网文字层 | `pdftotext -layout` 印/网全文 + 逐页 8/8 `cmp` | `print.txt`、`web.txt`、`print-p[1-8].txt`、`web-p[1-8].txt` | 0 | 全文 `cmp` 相同，**109,229 B**；逐页相同：P1 14,129 B、P2 11,247 B、P3 9,512 B、P4 9,333 B、P5 9,467 B、P6 12,379 B、P7 12,301 B、P8 30,861 B（与 fix1 逐字一致） |
| 15 | check_final | 本 scratch 副本 `check_final.py <build-copy>` | `check-final.log` | 0 | `pages print=8 web=8`；`words print=8576 web=8576 multiset-diff=0`；`diff sample: []`；`P8 answer-region span count: 185 min size: 9.75`；`word count: 1607` |
| 16 | P8 最小字号 | 本 scratch 副本 `minfont.py <交付印 PDF>` | `minfont.log` | 0 | `P8 min effective font size = 9.75 pt (n=372)`；`below 9.75pt: 0` |
| 17 | creambox | 本 scratch 副本 `creambox.py <版>/svg/*.svg` | `creambox.log` | 0 | 全 8 页 31 框；D1 框底 2348.0、末行基线 2327.6、余量 **+20.4**；D2 框底 551.0、`16h30.` 余量 **+10.4**；D3 框底 854.0、`Página do Participante.` 余量 **+13.2** |
| 18 | creambox 真墨裁决 | 本 scratch 副本 `creambox_diag.py <版>/svg/*.svg` | `creambox-diag.log` | 0 | 31 个 OWN 末行；真墨底余最小 **−0.3px**（2 处：P4 E VOCÊ 框、P7 词框——与 proof1/fix1 相同，见门 19 卡片裁决）；其余 ≥ +0.3px；D1 真墨底余 **+15.4**、D2 **+10.1**、D3 **+8.0**；3 处 below-window 行均为 owner-rect=NONE 的后继标题/分隔线，非溢出 |
| 19 | −0.3px 两处卡片裁决 | `card_probe.py`（build-copy 卡片，亮度<190；卡片与生产卡片 8/8 字节相同） | `card-probe.log` | 0 | P4 E VOCÊ 框底 876 以下是 **0 个深色像素**；P7 词框底 1461 以下是 **0 个深色像素**；P2 E VOCÊ 框底 909 以下 0 个；P5 框底 811 以下首现为 841 行的分隔线（后继内容，非本框末行）。−0.3px 为字体度量 artifact，非缺陷（与 proof1/fix1 裁决一致） |
| 20 | boxtitle（advance） | 本 scratch 副本 `boxtitle_core.py <版>/svg` | `boxtitle-advance.log` | 0 | **31 行**（独立计数，见 §4）；**OVERFLOWS: 0**（无负余量）；D-NEW1 标题 fs=23、title_w=387.2、right=1848.7、clear **+13.3**；其余最小正余量 +10.5（P1 `A SEMANA EM NÚMEROS　En cifras`） |
| 21 | boxtitle 真墨（PIL，逐元素本字号） | 本 scratch 自写 `boxtitle_trueink.py`（生产目录） | `boxtitle-trueink.log` | 0 | **31 行**；**TRUE-INK OVERFLOWS: 0**；D-NEW1 真墨右缘 1848.5、框右 1862.0、clear **+13.5**；D4 P2 `PARA NÃO ERRAR　La regla` 真墨 863.5、clear **+97.5**；D5 P7 `ERROS COMUNS　Errores` 真墨 1750.5、clear **+111.5**；D6 P7 `A PALAVRA　La palabra` 真墨 1724.5、clear **+137.5**；其余最小 +10.5 |
| 22 | boxtitle PDF 渲染交叉验证 | 本 scratch 自写 `pdf_render_titles.py`（交付印 PDF 渲染 `render/print-p-*.png`） | `pdf-render-titles.log` | 0 | **31 行标题**；**PDF-RENDER TITLE OVERFLOWS: 0**；D-NEW1 渲染墨右 1848、clear **+14**；其余最小 +12（P1 `A SEMANA EM NÚMEROS` +12、P2 `Palmeiras × Flamengo, às` +22、P1 `NESTA EDIÇÃO` +22）；D4 +98、D5 +112、D6 +138；网 PDF P1 同法重测：墨右 1848、clear **+14**（逐列计数：1846:9 / 1847:8 / 1848:6 / ≥1849:0） |
| 23 | D1/D2/D3 PDF 渲染复核 | 同上（逐行深色像素计数） | `pdf-render-titles.log` | 0 | D1：末行墨止于 2331，框底 2348；2349–2350 行为 422px 通栏分隔线（盒外 quiz 分隔线，非文本溢出），其后为 quiz 内容；D2：末行墨止于 539，框下无深色行；D3：降部墨止于 844，框下无深色行。**三处均已修复且存活** |
| 24 | D7 范文 PDF 渲染复核 | 本 scratch 自写 `d7_essay_measure.py`（范文 10 行，逐行精确带，列内限宽；交付印 PDF / 重建印 PDF / 卡片三路） | `d7-essay.log` | 0 | 10 行范文：交付印 PDF 最右墨 1829、最小余量 **+33**；**重建印 PDF 逐行与交付值完全相同，最小余量 +33**；卡片最右墨 1840、最小余量 +22（与 proof1/fix1 的 +33/+22 逐项一致） |
| 25 | sweep | 本 scratch 副本 `sweep_de.py <版目录>` | `sweep.log` | 0 | `box-vs-hline flags: 0`；`bridges found: 20`；`bridge orphans: 0`；`bridge widows: 0` |
| 26 | 孤儿标点扫 | 本 scratch 改编 `orphan_sweep_fix.py <build-copy>` | `orphan-sweep.log` | 0 | A（`:` 后接字母）4 处：均为 P8 答案行 `56. mais — 3 > 1:mais` / `57. …:mais` / `58. …:mais cedo` / `102. …:cae en viernes`——键值分隔符，与核心版同格式，p8 compare CLEAN；B（行首孤儿）0；C（行末 `:`）6 处全为合法引导冒号；D（双空格）0；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，空白占位符固有格式；text.md 冒号后接字母 0；text.md `｜` ×6（U+FF5C gloss 分隔符）、U+2019 0 |
| 27 | check_s11（pt 改编） | 本 scratch 自写 `check_s11_pt.py`（改编自 en `check_s11.py`，见 §7） | `check-s11.log` | 0 | 生产目录运行 **ALL §1.1/P8 CHECKS PASS**：colour set core 21 = edition 21，extra/missing 均为 none；badge A2/B1/B2 均 present；P8 min font 13.0（core 13.5）；P8 练习号 113–150 全 present；P8 Q120 chip (88.0, 734.7, `#46581f`) 与 core 完全一致；P8 Escritura head 行（`150.` + `Escritura` + `B1`）present |
| 28 | 150 题手验 | 全文通读 text.md 534 行 + keycheck-150.json + Respostas 三方比对 | `keycheck-150.json`、`resp-compare.log` | — | **150/150 题干与键逐项适配**（见 PROOF-NOTE §4；含 Q73 `espera`、Q137/138 译文、Q139/140 反向翻译、Q148 `na internet`、Q125 36 轮、Q83–86 图表算术 10+5=15、范文 88 词手数） |
| 29 | 8 页目视 | 交付印 PDF `pdftoppm -r 96` 全 8 页 | `render/print-p-[1-8].png`、`render/web-p-[1-8].png` | — | P1 已目视：标题在盒内，顶栏标语、头条、quiz 均正常；其余 7 页 SVG 与 proof1 字节相同，只抽查渲染一致性（重建卡片 8/8 与生产卡片字节相同） |
| 30 | 生产目录改动范围 | 开工 `sha256sum` 快照 vs 收工复核 | `prod-snapshot-before.sha256`、`core-snapshot-before.sha256` | — | 版目录 43 文件、core-pt 38 文件**零改动**；text.md SHA 不变；无 commit、无 push |

## §1 run.py 重建 SVG 一致性（门 2 明细）

```
p1-capa IDENTICAL（重建 vs 生产）
p2-vida IDENTICAL
p3-cultura IDENTICAL
p4-esporte IDENTICAL
p5-jovens IDENTICAL
p6-aprofundamento IDENTICAL
p7-lingua IDENTICAL
p8-avaliacao IDENTICAL
```

## §2 与 proof1 备份的 SVG 比对（门外追加，任务书②）

proof1 备份 = `scratch-proof-pt-es2/build-copy/svg/`：

```
p1-capa DIFFERS — 仅 1 个 token：font-size="24" → "23"（x=1461.5 y=1914，文案 EM POUCAS PALAVRAS　EN BREVE 不变）
p2-vida / p3-cultura / p4-esporte / p5-jovens / p6-aprofundamento / p7-lingua / p8-avaliacao IDENTICAL
```

生产 SVG 哈希：p1 `092e2d3d…`、p2 `0be39d1c…`、p3 `f6095d0a…`、p4 `3148d4b9…`、p5 `31241efb…`、p6 `61863d5c…`、p7 `22ce3ac7…`、p8 `0febf48d…`（p2–p8 与 fix1 逐字一致）。

## §3 首轮 7 项缺陷存活复验（proof1 实测值 → 本次复测）

| # | 首轮缺陷 | 本次复测 | 结果 |
|---|---|---|---|
| D1（核心） | P1 EM-BREVE 框末行在框外 +33px | 框底 2348.0、末行基线 2327.6、真墨底 2332.6、余量 **+15.4**（creambox-diag）；PDF 渲染：墨止于 2331，框下 2349–2350 为 422px quiz 分隔线（盒外，与文本分离） | **存活** |
| D2（核心） | P3 日程框末行 `16h30.` 在框外 +16px | 框底 551.0、末行基线 540.6、真墨底 540.9、余量 **+10.1**；PDF 渲染：墨止于 539，框下无深色行；卡片：墨止于 540 | **存活** |
| D3（核心） | P6 时间线框末行降部越边 6px | 框底 854.0、末行基线 840.8、真墨底 846.0、余量 **+8.0**；PDF 渲染：墨止于 844，框下无深色行；卡片：降部墨 841–845 在框内 | **存活** |
| D4（本版） | P2 `PARA NÃO ERRAR　La regla para recordar` +67px | 源 `tables_es.py:58`「口诀」→`La regla` 已落地；旧长 gloss 全版 0 处；PIL 真墨 863.5、clear **+97.5**；PDF 渲染 863、clear **+98**；卡片 865、clear +96 | **存活** |
| D5（本版） | P7 `ERROS COMUNS　Errores frecuentes` +13px | 源 `tables_es.py:107`「常见错误」→`Errores` 已落地；PIL 真墨 1750.5、clear **+111.5**；PDF 渲染 1750、clear **+112**；卡片 1749、clear +113 | **存活** |
| D6（本版） | P7 `A PALAVRA　La palabra de la semana` +17px | 源 `tables_es.py:136`「本周生词」→`La palabra` 已落地；PIL 真墨 1724.5、clear **+137.5**；PDF 渲染 1724、clear **+138**；卡片 1726、clear +136 | **存活** |
| D7（核心） | P8 范文第 2–3 行超出版心 +2/+14px | 范文 10 行（`Texto modelo`，y=703.6–879.1）PDF 渲染逐行与旧值完全相同，最右墨 1829、最小余量 **+33**；卡片最右墨 1840、最小余量 +22；第 2–3 行现为 `despertador…leio sobre` / `Zumbi e Palmares…` | **存活** |
| D-NEW1 | — | 见 PROOF-NOTE §1：PDF 渲染 **+14**（印/网一致） | **已修复** |

注：D4/D5/D6 的卡片值（+96/+113/+136）为本轮 `card_probe.py` 在 build-copy 卡片上的独立重测（卡片与生产卡片 8/8 字节相同），与 proof1/fix1 的卡片值在 ±2px 内一致（渲染取整）；判定以 PDF 渲染为准。

## §4 框标题全表（三法）

全部 31 行框标题逐一 PIL 真墨量测；最紧几处 PDF 渲染像素交叉验证。最小三项列于表首（其余行 advance ≥ +22.6、真墨 ≥ +22.5、PDF ≥ +22）：

| 标题 | advance | PIL 真墨 | PDF 渲染 | 卡片 |
|---|---|---|---|---|
| P1 `EM POUCAS PALAVRAS　EN BREVE`（**D-NEW1，改后**） | +13.3 | +13.5 | **+14** | +14 |
| P1 `A SEMANA EM NÚMEROS　En cifras` | +10.5 | +10.5 | +12 | — |
| P1 `NESTA EDIÇÃO　En este número` | +22.6 | +22.5 | +22 | — |
| P2 `Palmeiras × Flamengo, às` | +22.2 | +22.5 | +22 | — |
| P2 `PARA NÃO ERRAR　La regla`（D4） | +97.3 | +97.5 | +98 | +96 |
| P7 `ERROS COMUNS　Errores`（D5） | +111.6 | +111.5 | +112 | +113 |
| P7 `A PALAVRA　La palabra`（D6） | +138.0 | +137.5 | +138 | +136 |
| 其余 24 行 | ≥ +23.6 | ≥ +23.5 | ≥ +24 | — |

完整 31 行见 `boxtitle-advance.log`（advance）、`boxtitle-trueink.log`（真墨）与 `pdf-render-titles.log`（PDF 渲染 31 行，0 溢出）。**计数裁定：31 行**——三法各自独立计数均为 31，fix1 正确，proof1 的 30 行有误。

**宽带扫描说明**：`card_probe.py` 的 P8 Respostas 列表扫描（band 内 x 延至 1949）在 y=1472 行读到 1856（卡片）——与 fix1 的数值一致，**非回归**；该读数是同 y 带内其他栏（col 2/3）的墨迹，非本行自身墨迹。权威的 D7 判定是 §3/D7 的范文 10 行列内限宽测量（PDF +33 / 卡片 +22，新旧逐行相同）；另 gates.py 页框检查 0 穿越、最小右边距 47.5px，佐证全版无墨近页边。

## §5 文字层 2 字节差说明（fix1 改动所致，预期内）

- 交付印 PDF vs proof1 旧印 PDF 的 `pdftotext -layout` 全文仅 1 行不同（第 72 行）：`EM POUCAS PALAVRAS` 与 `EN BREVE` 之间的 `-layout` 空格由 22 格变为 20 格——标题字号 24→23pt 后分隔符 U+3000 渲染变窄所致。**文字内容逐字相同**，其余 7 页逐页字节相同。
- 交付印 vs 交付网：全文与逐页 8/8 逐字节相同（109,229 B）。
- 网 PDF SHA 只作记录，不作论证（fontTools 写 wall-clock 到 head.modified；本轮 scratch 内重建网 PDF 1,140,276 B，文字层与交付网 PDF 逐字节相同）。

## §6 复校工具链勘误（本轮独立复现，如实记录）

1. **Respostas 解析器 bug（proof 沿用脚本）**：`resp_compare.py`（v1 lookahead）与 `resp_compare2.py`（v2 strip）在当前 text.md 上均只解析出 **143 条**，漏掉 7 个页首题（11、29、47、65、83、101、113），mismatches 各 14 条——Respostas 列表以 `\n\n**Página N** — `（U+2014）分页，旧解析器跨不过该分隔；v2 的 strip 更把边界项粘连（`10. B\n\n11. B` 成一项）。7 题的键在原文中均存在且正确（`11. B`、`29. C`、`47. A`、`65. B`、`83. B`、`101. em`、`113. A`），故为解析器 artifact，非内容问题。本轮改写 `resp_compare_fix.py`（页眉归一化为 ` · ` 分隔符后再解析）：8 处页眉归一化，**150/150 解析，0 不符**。
2. **proof 的 `card-probe3.log` 为失败日志**：108 字节，内容为 Python Traceback（`NameError: name 'S' is not defined`）；其 GATE-LOG §22 的 D7 数值（PDF +33 / 卡片 +22）并非出自该脚本，但本轮已用 `d7_essay_measure.py` 在范文 10 行上独立重测证实（交付印 PDF +33 / 重建印 PDF +33 / 卡片 +22，新旧逐行相同），与该失败日志无关。
3. **proof `card-probe2.log` 与其 GATE-LOG §22 的数值口径不同**：前者是 Respostas 列表宽带扫描（最紧 +6 卡片），后者是范文 10 行列内限宽测量（+22 卡片 / +33 PDF）。两者本轮均重测并与 proof1/fix1 的原始日志值逐行一致，无回归；GATE-LOG 以 §3/D7 的范文测量为准。

## §7 check_s11 改编说明（pt 无专用脚本）

- en 原件：`scratch-fanout-en2/fanout/check_s11.py`（§1.1 + P8 字体 + badge 检查，对 core-en）。
- 改编件：本 scratch `check_s11_pt.py`（只写进本 scratch，未动 en 原件与仓库任何文件）。改编点与 fix1 相同：core-en → core-pt；版目录 `2026-w47-pt-es`；页文件名 en `p1-front…p8-test` → pt `p1-capa…p8-avaliacao`；pt-es 版目录无 `registry.json`，Q120 chip 的级别改与 core-pt 直接比对（同坐标同色 `#46581f` = B1）；pt-es P8 无 cloze passage，改查 P8 练习号 113–150 全 present；H WRITING 头改查同行 `150.` + `Escritura` + `B1`。
- 结果：生产目录运行 **ALL PASS**，rc=0。

## 未通过的门

**无。**全部机械门通过；D-NEW1 已修复；首轮 7 项全部存活；150 题手验 150/150。
