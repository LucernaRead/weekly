# GATE-LOG — 2026-W47 pt-es（fix1，D-NEW1）

修复时间：2026-11-11。解释器（全部）：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3，各工具 runtime 行自证；pt 家族规范）。`PYTHONDONTWRITEBYTECODE=1` 全程开启，`TMPDIR=<scratch>/tmp`（未用系统 /tmp）。
生产目录改动：仅 FIX-LOG.md §4 所列 5 文件；core-pt 零改动（收工 `sha256sum -c core-snapshot-before.sha256` 全 OK）。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-es1/`
前置：改前三 SHA 与 proof1 任务书逐字一致（印 `f1b4fc20…` / 12,933,062 B；网 `d00e8f54…` / 1,140,276 B；文 `96d6f11a…` / 37,467 B）；改后三 SHA 见 FIX-LOG.md §3。

## §0 门总表（全部在 build-copy 内先跑，再对生产交付态复验）

| # | 门 | 命令 / 位置 | 日志 | rc | 实测值 |
|---|---|---|---|---|---|
| 1 | run.py 重跑 | `build-copy/` 内 `python run.py` | `run-rebuild.log` | 0 | `TOTAL 150`；`by level {'A2': 48, 'B1': 71, 'B2': 31}`；`by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；`model words: 88`；`OVERFLOW`/`TOO WIDE` 0 处；末行 `ALL DONE` |
| 2 | SVG 重建一致 | `build-copy/svg` vs 发货 `svg/`，8 文件逐一 `cmp` | （本文件 §1） | — | **仅 p1 变化**（标题 `font-size 24→23`）；其余 7 页字节一致 |
| 3 | render.py（印 PDF） | `build-copy/` 内 `python render.py` | `render-copy.log` | 0 | 8 卡片 + 印 PDF 12,933,061 B；SHA `75e870cf…` |
| 4 | webpdf.py（网 PDF） | `tools/webpdf.py build-copy/svg A-Lucerna-VOL4-web.pdf` | `webpdf-copy.log` | 0 | 8 页，116 字符，8 字体子集；1,140,280 B；SHA `4e7b30ea…`（网 SHA 浮动为已知根因，只认文字层） |
| 5 | gates.py 16/16 | 生产目录内 `python gates.py`（只读）+ build-copy 内同跑 | `gates-production.log` / `gates-batch-a.log` | 0 / 0 | `[PASS]` 16 行；`FAILURES: none`（最小页框边距 L/R/T/B = 47.0/47.5/35.0/32.0——R 由 44.5 变 47.5，只因 P1 标题变窄；P1 头条 41 字符 ≤56；gloss 29 项；P7 金句 8 条 2×+页签+西语；图片+credits 5/5；P7 金句区 clears 预告框，最大基线 2380.67 < 2404） |
| 6 | freeze baseline（核心） | `tools/freeze.py baseline --build <core-pt> --core-svg <core-pt>/svg --out freeze-core` | `freeze-baseline-core.log` | 0 | **8/8 byte-identical**，repointed files: none；p1 `bd87a867…`、p2 `0a8300c3…`、p3 `e3c97081…`、p4 `f539bdb8…`、p5 `51629e93…`、p6 `a3c3cf38…`、p7 `43b845fc…`、p8 `a7b7a661…`（与 proof1 逐字一致） |
| 7 | freeze baseline（版） | `tools/freeze.py baseline --build <版目录> --core-svg <版目录>/svg --out freeze-ed(-final)`（build-copy 与生产目录各跑一次） | `freeze-baseline-ed.log` / `freeze-baseline-ed-final.log` | 0 / 0 | **两次均为 8/8 byte-identical**，repointed files: none；p1 `092e2d3d…`（新 hash——仅此页变）、p2 `0be39d1c…`、p3 `f6095d0a…`、p4 `3148d4b9…`、p5 `31241efb…`、p6 `61863d5c…`、p7 `22ce3ac7…`、p8 `0febf48d…`（p2–p8 与 proof1 逐字一致）；core integrity 一致 |
| 8 | freeze diff | `tools/freeze.py diff --core-svg <core-pt>/svg --edition-svg <版>/svg --json freeze-diff.json` | `freeze-diff.log`、`freeze-diff.json` | 0 | p1 +26/−39、p2 +41/−33、p3 +34/−29、p4 +30/−26、p5 +41/−48、p6 +25/−22、p7 +52/−46、p8 +189/−753；**新增 CJK 共 9 个，全部 U+3000**（P1 2、其余每页 1）；新增汉字 0（与 proof1 一致） |
| 9 | occlusion 真实审计 | `tools/occlusion_audit.py <版>/svg --json occlusion.json`（非 `--selftest`） | `occlusion.json`、`gates-batch-b.log` | 0 | 内置自检 `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；审计 `0 flags`；`flag_count: 0` |
| 10 | p8 extract | `tools/p8.py extract --p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-extract.json` | `gates-batch-b.log` | 0 | `noted set = 150 of 150 (parse: lines)` |
| 11 | p8 compare | `tools/p8.py compare --core-p8 <core-pt>/svg/p8-avaliacao.svg --edition-p8 <版>/svg/p8-avaliacao.svg --total 150 --json p8-compare.json`（build-copy 与生产目录各跑一次） | `gates-batch-b.log` / `gates-final.log`、`p8-compare.json`、`p8-compare-final.json` | 0 / 0 | 两次均为 `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`（预期：翻译题答案） |
| 12 | keycheck | 本 scratch 副本 `keycheck_core.py <build-copy> p8-extract.json`（内含 run.py 重跑） | `gates-batch-d.log`、`keycheck-150.json` | 0 | `REG entries: 150; p8extract keys: 150`；**exact match 149/150**；唯一 `MISMATCH n=150 type=Escritura: key='(ejercicio abierto — texto modelo abajo)' extracted='✓'`（预期：开放作文） |
| 13 | Respostas 三方一致 | 本 scratch 自写 `resp_compare_fix.py`（修正版，见 §6） | `resp-compare.log` | 0 | 页眉归一化 8 处；150/150 解析，missing []；**不符 0**（Q150 除外：Respostas 为 `✓ Ver el texto modelo…(88 palabras)`，与 REG 开放题注述同义） |
| 14 | 印/网文字层 | `pdftotext -layout` 印/网全文 + 逐页 8/8 `cmp` | `print-new.txt`、`web-new.txt`、`print-new-p[1-8].txt`、`web-new-p[1-8].txt` | 0 | 全文 `cmp` 相同，**109,229 B**；逐页相同：P1 14,129 B、P2 11,247 B、P3 9,512 B、P4 9,333 B、P5 9,467 B、P6 12,379 B、P7 12,301 B、P8 30,861 B（P2–P8 字节数与 proof1 的旧值逐字一致；P1 少 2 B，见 §5） |
| 15 | check_final | 本 scratch 副本 `check_final.py <build-copy>` | `gates-batch-b.log` | 0 | `pages print=8 web=8`；`words print=8576 web=8576 multiset-diff=0`；`diff sample: []`；`P8 answer-region span count: 185 min size: 9.75`；`word count: 1607` |
| 16 | P8 最小字号 | 本 scratch 副本 `minfont.py <新印 PDF>` | `gates-batch-b.log` | 0 | `P8 min effective font size = 9.75 pt (n=372)`；`below 9.75pt: 0` |
| 17 | creambox | 本 scratch 副本 `creambox.py <版>/svg/*.svg` | `gates-batch-b.log` | 0 | 全 8 页 31 框；D1 框底 2348.0、末行基线 2327.6、余量 **+20.4**；D2 框底 551.0、`16h30.` 余量 **+10.4**；D3 框底 854.0、`Página do Participante.` 余量 **+13.2** |
| 18 | creambox 真墨裁决 | 本 scratch 副本 `creambox_diag.py <版>/svg/*.svg` | `gates-batch-b.log` | 0 | 31 个 OWN 末行；真墨底余最小 **−0.3px**（2 处：P4 E VOCÊ 框、P7 词框——与 proof1 相同，见门 19 卡片裁决）；其余 ≥ +0.3px；D1 真墨底余 **+15.4**、D2 **+10.1**、D3 **+8.0**；3 处 below-window 行均为 owner-rect=NONE 的后继标题/分隔线，非溢出 |
| 19 | −0.3px 两处卡片裁决 | `card_probe.py`（新卡片 PIL，亮度<190） | `card-probe-final.log` | 0 | P4 E VOCÊ 框底 876 以下是 **0 个深色像素**；P7 词框底 1461 以下是 **0 个深色像素**；P2 E VOCÊ 框底 909 以下 0 个；P5 框底 811 以下首现为 837 行的分隔线（后继内容，非本框末行）。−0.3px 为字体度量 artifact，非缺陷（与 proof1 裁决一致） |
| 20 | boxtitle（advance） | 本 scratch 副本 `boxtitle_core.py <版>/svg` | `gates-batch-a.log` | 0 | 31 行；**OVERFLOWS: 0**；D-NEW1 标题 fs=23、title_w=387.2、right=1848.7、clear **+13.3**；其余最小正余量 +10.5（P1 `A SEMANA EM NÚMEROS　En cifras`） |
| 21 | boxtitle 真墨（PIL，逐元素本字号） | 本 scratch 自写 `boxtitle_trueink.py`（生产目录复验同值） | `gates-batch-a.log` / `gates-final.log` | 0 | 31 行；**TRUE-INK OVERFLOWS: 0**；D-NEW1 真墨右缘 1848.5、框右 1862.0、clear **+13.5**；D4 P2 `PARA NÃO ERRAR　La regla` 真墨 863.5、clear **+97.5**；D5 P7 `ERROS COMUNS　Errores` 真墨 1750.5、clear **+111.5**；D6 P7 `A PALAVRA　La palabra` 真墨 1724.5、clear **+137.5**；其余最小 +10.5 |
| 22 | boxtitle PDF 渲染交叉验证 | 本 scratch 自写 `pdf_render_titles.py`（生产印 PDF 渲染复验，`pdf-render-titles-final.log`） | `gates-batch-c.log` / `gates-final.log`、`pdf-render-titles-final.log` | 0 | 31 行标题；**PDF-RENDER TITLE OVERFLOWS: 0**；D-NEW1 渲染墨右 1848、clear **+14**；其余最小 +12（P1 `A SEMANA EM NÚMEROS` +12、P2 `Palmeiras × Flamengo, às` +22、P1 `NESTA EDIÇÃO` +22）；D4 +98、D5 +112、D6 +138；网 PDF P1 同法重测：墨右 1848、clear **+14**（`web-p1-title.log`） |
| 23 | D1/D2/D3 PDF 渲染复核 | 同上（逐行深色像素计数） | `gates-batch-c.log` / `pdf-render-titles-final.log` | 0 | D1：末行墨止于 2331，框底 2348；2349–2350 行为 422px 通栏分隔线（盒外 quiz 分隔线，非文本溢出）；D2：末行墨止于 539，框底 551，框下无深色行；D3：降部墨止于 844，框底 854，框下无深色行。**三处均已修复且存活** |
| 24 | D7 范文 PDF 渲染复核 | 本 scratch 自写 `d7_essay_measure.py`（范文 10 行，逐行精确带，列内限宽；另 `d7_pdf.py` 为 Respostas 列表宽带扫描，见 §4） | `d7-essay.log` | 0 | 10 行范文：旧印 PDF 渲染最右墨 1829、最小余量 **+33**；**新印 PDF 渲染逐行与旧值完全相同，最小余量 +33**；新卡片最右墨 1840、最小余量 +22（与 proof1 的 +33/+22 逐项一致） |
| 25 | sweep | 本 scratch 副本 `sweep_de.py <版目录>` | `gates-batch-b.log` | 0 | `box-vs-hline flags: 0`；`bridges found: 20`；`bridge orphans: 0`；`bridge widows: 0` |
| 26 | 孤儿标点扫 | 本 scratch 改编 `orphan_sweep_fix.py <build-copy>`（原脚本路径硬编码生产目录，改编为 argv 传入） | `orphan-sweep.log` | 0 | A（`:` 后接字母）4 处：均为 P8 答案行 `56. mais — 3 > 1:mais` / `57. …:mais` / `58. …:mais cedo` / `102. …:cae en viernes`——键值分隔符，与核心版同格式，p8 compare CLEAN；B（行首孤儿）0；C（行末 `:`）6 处全为合法引导冒号；D（双空格）0；E（空格+标点）1 处：Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，空白占位符固有格式；text.md 冒号后接字母 0；text.md `｜` ×6（U+FF5C gloss 分隔符）、U+2019 0 |
| 27 | check_s11（pt 改编） | 本 scratch 自写 `check_s11_pt.py`（改编自 en `check_s11.py`，见 §7） | `check-s11.log` / `gates-final.log` | 0 | build-copy 与生产目录两次均为 **ALL §1.1/P8 CHECKS PASS**：colour set core 21 = edition 21，extra/missing 均为 none；badge A2/B1/B2 均 present；P8 min font 13.0（core 13.5）；P8 练习号 113–150 全 present；P8 Q120 chip (88.0, 734.7, `#46581f`) 与 core 完全一致；P8 Escritura head 行（`150.` + `Escritura` + `B1`）present |
| 28 | 150 题手验 | 全文通读 text.md 534 行 + keycheck-150.json + Respostas 三方比对 | `keycheck-150.json`、`resp-compare.log` | — | **150/150 题干与键逐项适配**（见 §3；含 Q73 `espera`、Q137/138 译文、Q139/140 反向翻译、Q148 `na internet`、Q125 36 轮、Q83–86 图表算术 10+5=15、范文 88 词手数） |
| 29 | 8 页目视 | 生产印 PDF `pdftoppm -r 96` 全 8 页（P1 重点目视；其余 7 页 SVG 与改前字节相同，只抽查渲染一致性） | `render-final/print-p-[1-8].png` | — | P1 已目视：标题在盒内，顶栏标语、头条、quiz 均正常；生产 P1 渲染与 build-copy 渲染 `cmp` 字节相同；其余 7 页渲染由 SVG 字节相同背书（见门 2） |
| 30 | 生产目录改动范围 | 开工 `sha256sum` 快照 vs 收工复核 | `prod-snapshot-before.sha256` | — | 47 文件中**恰好 5 个变化**：`content12.py`、`svg/p1-capa.svg`、`A-Lucerna-VOL4.pdf`、`A-Lucerna-VOL4-web.pdf`、`cards/p1-capa.png`；其余 42 文件字节不变；text.md SHA 不变；core-pt 41 文件全 OK |

## §1 run.py 重建 SVG 一致性（门 2 明细）

```
p1-capa DIFFERS — 仅标题元素 font-size="24" → "23"
p2-vida IDENTICAL
p3-cultura IDENTICAL
p4-esporte IDENTICAL
p5-jovens IDENTICAL
p6-aprofundamento IDENTICAL
p7-lingua IDENTICAL
p8-avaliacao IDENTICAL
```

## §2 首轮 7 项缺陷存活复验（proof1 实测值 → 本次复测）

| # | 首轮缺陷 | 本次复测 | 结果 |
|---|---|---|---|
| D1（核心） | P1 EM-BREVE 框末行在框外 +33px | 框底 2348.0、末行基线 2327.6、真墨底 2332.6、余量 **+15.4**（creambox-diag）；PDF 渲染：墨止于 2331，框下 2349–2350 为 422px quiz 分隔线（盒外，与文本分离） | **存活** |
| D2（核心） | P3 日程框末行 `16h30.` 在框外 +16px | 框底 551.0、末行基线 540.6、真墨底 540.9、余量 **+10.1**；PDF 渲染：墨止于 539，框下无深色行；卡片：墨止于 540 | **存活** |
| D3（核心） | P6 时间线框末行降部越边 6px | 框底 854.0、末行基线 840.8、真墨底 846.0、余量 **+8.0**；PDF 渲染：墨止于 844，框下无深色行；卡片：降部墨 841–845 在框内 | **存活** |
| D4（本版） | P2 `PARA NÃO ERRAR　La regla para recordar` +67px | 源 `tables_es.py:58`「口诀」→`La regla` 已落地；旧长 gloss 全版 0 处；PIL 真墨 863.5、clear **+97.5**；PDF 渲染 863、clear **+98**；卡片 865、clear +96 | **存活** |
| D5（本版） | P7 `ERROS COMUNS　Errores frecuentes` +13px | 源 `tables_es.py:107`「常见错误」→`Errores` 已落地；PIL 真墨 1750.5、clear **+111.5**；PDF 渲染 1750、clear **+112**；卡片 1749、clear +113 | **存活** |
| D6（本版） | P7 `A PALAVRA　La palabra de la semana` +17px | 源 `tables_es.py:136`「本周生词」→`La palabra` 已落地；PIL 真墨 1724.5、clear **+137.5**；PDF 渲染 1724、clear **+138**；卡片 1726、clear +136 | **存活** |
| D7（核心） | P8 范文第 2–3 行超出版心 +2/+14px | 范文 10 行（`Texto modelo`，y=703.6–879.1）PDF 渲染逐行与旧值完全相同，最右墨 1829、最小余量 **+33**；卡片最右墨 1840、最小余量 +22；第 2–3 行现为 `despertador…leio sobre` / `Zumbi e Palmares…` | **存活** |
| D-NEW1 | — | 见 FIX-LOG.md §2：PDF 渲染 **+14** | **已修复** |

注：D4/D5/D6 的卡片值（+96/+113/+136）为本轮 `card_probe.py` 在新卡片上的独立重测，与 proof1 的卡片值在 ±2px 内一致（渲染取整）；判定以 PDF 渲染为准。

## §3 150 题手验（本次独立通读 text.md 534 行，逐题核对键与题干）

- **150/150 通过**。与 proof1 §5 逐项一致，本次独立复核要点：
  - Q1–10：consciência/feriado/sexta/três/6/decidem；quiz B/B/C/B。
  - Q11–28：Q11–15 全 B；Q16–20 cai/dura/descansamos/abrem/aproveita；Q21–24 数字 3/1695/2023/27；Q25–28 配对 a/b/c/d。
  - Q29–46：Q29 C（1695-11-20）、Q31 B（14.759 使成国定假日，12.519 仅设纪念日）、Q33 A；Q34–39 quilombo/resistência/escravizados/líder/memória/combate；Q40–43 morreu/nasceu/defendeu/formaram；Q44–46 组句逐字一致。
  - Q47–64：Q47 A、Q48 B、Q49 B、Q50 B、Q51 A（Norris）；Q52–55 b/a/d/c；Q56–59 mais/mais/mais/menos；Q60–64 empatou/venceu/abriu/garantiu/foram。
  - Q65–82：Q65–69 B/B/A/B/B；Q70–75 gabarito/oficial/extraoficiais/**espera**/nota/pesa——**Q73 重点复核**：「Depois da prova, começa a ___.」键 `espera` 与正文「Depois da prova, começa…a espera pelo gabarito」贴合，题干动词 `começa` 与 `espera` 搭配自然；Q76–79 sairá/publicarão/decidirá/chegará；Q80–82 V/F/V。
  - Q83–100：图表算术独立验算——11 月 16–30 日共 15 天，工作日 10 天（16–19、23–27、30），周末 + 假日 5 天（21、22、28、29、20），10+5=15；Q83 B、Q84 A、Q85 B、Q86 B、Q87 B；Q88 A、Q89 B、Q90 B、Q91 B、Q92 B；Q93–96 serão/contam/fixa/pesa；Q97–100 prazo/dia útil/coerência/chute。
  - Q101–112：em/numa/é/B（aproveitamos）/empatou/venceu/abriu/B（saíram）/sair/for/tiver/B（sair）。
  - Q113–132：A/A/B/A/B（Q116 6 日、Q117 Palmeiras、Q119 15 日、Q120 五小时 13h30–18h30）/A/B/A（Q121 B、Q122 A、Q123 B、Q124 B、**Q125 A（36 轮）**、Q126 B、Q127 A、Q128 A）；Q129–132 B/B/A/B（Rafael：Salvador/周五 capoeira/周六 Palmeiras×Flamengo/周一查 extraoficial）。
  - Q133–136 组句逐字正确；**Q137/138 译文正确**（keydiff 预期项）；**Q139/140 反向翻译正确**。
  - Q141–144 配对 c/d/b/a；Q145–149 全 A（Mané/sexto/quinto/**na internet**/obrigado）。
  - Q150：开放作文；范文手数 **88 词**（× 计为一词，与构建器 `model words: 88` 一致），内容覆盖周五/周六/周日三日与 20 日纪念意义。
- 机械背书：keycheck 149/150（唯一不符 Q150 开放题，预期）；p8 compare CLEAN，keydiff=[137, 138]；Respostas 三方比对 150/150 解析、0 不符（Q150 除外，见 §6）。

## §4 框标题全表（三法）

全部 31 行框标题逐一 PIL 真墨量测；最紧几处 PDF 渲染像素交叉验证。最小三项列于表首（其余行 advance ≥ +23.6、真墨 ≥ +23.5、PDF ≥ +24）：

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

完整 30 行见 `gates-batch-a.log`（advance + 真墨）与 `pdf-render-titles-final.log`（PDF 渲染 31 行，0 溢出）。

**宽带扫描说明**：`card_probe2.py` / `d7_pdf.py` 的 P8 Respostas 列表扫描（band 内 x 延至 1949）在 y=1472/1500 行读到 1855/1856（卡片）与 1853（PDF 渲染）——与 proof1 自身的 `card-probe2.log` 数值逐行相同，**非回归**；该读数是同 y 带内其他栏（col 2/3）的墨迹，非本行自身墨迹。权威的 D7 判定是 §2/D7 的范文 10 行列内限宽测量（PDF +33 / 卡片 +22，新旧逐行相同）；另 gates.py 页框检查 0 穿越、最小右边距 47.5px，佐证全版无墨近页边。

## §5 文字层 2 字节差说明

- 新印 PDF vs 旧印 PDF 的 `pdftotext -layout` 全文仅 1 行不同（第 72 行）：`EM POUCAS PALAVRAS` 与 `EN BREVE` 之间的 `-layout` 空格由 22 格变为 20 格——标题字号 24→23pt 后分隔符 U+3000 渲染变窄所致。**文字内容逐字相同**，其余 7 页逐页字节相同。
- 新印 vs 新网：全文与逐页 8/8 逐字节相同（109,229 B）。
- 网 PDF SHA 只作记录，不作论证（fontTools 写 wall-clock 到 head.modified）。

## §6 复校工具链勘误（本轮发现，如实记录）

1. **Respostas 解析器 bug（proof 沿用脚本）**：`resp_compare.py`（v1 lookahead）与 `resp_compare2.py`（v2 strip）在当前 text.md 上均只解析出 **143 条**，漏掉 7 个页首题（11、29、47、65、83、101、113）——Respostas 列表以 `\n\n**Página N** — `（U+2014）分页，旧解析器跨不过该分隔；v2 的 strip 更把边界项粘连（`10. B\n\n11. B` 成一项）。7 题的键在原文中均存在且正确（`11. B`、`29. C`、`47. A`、`65. B`、`83. B`、`101. em`、`113. A`），故为解析器 artifact，非内容问题。本轮改写 `resp_compare_fix.py`（页眉归一化为 ` · ` 分隔符后再解析）：8 处页眉归一化，**150/150 解析，0 不符**。proof 的 `resp-compare.log` 称 150/0，其打印格式与两版脚本均不一致，未深究——以本轮修正版实测为准。
2. **proof 的 `card-probe3.log` 为失败日志**：108 字节，内容为 Python Traceback（`NameError: name 'S' is not defined`）；其 GATE-LOG §22 的 D7 数值（PDF +33 / 卡片 +22）并非出自该脚本，但本轮已用 `d7_essay_measure.py` 在范文 10 行上独立重测证实（新旧逐行相同）。
3. **proof `card-probe2.log` 与其 GATE-LOG §22 的数值口径不同**：前者是 Respostas 列表宽带扫描（最紧 +6 卡片），后者是范文 10 行列内限宽测量（+22 卡片 / +33 PDF）。两者本轮均重测并与 proof 的原始日志值逐行一致，无回归；GATE-LOG 以 §2/D7 的范文测量为准。

## §7 check_s11 改编说明（pt 无专用脚本）

- en 原件：`scratch-fanout-en2/fanout/check_s11.py`（§1.1 + P8 字体 + badge 检查，对 core-en）。
- 改编件：本 scratch `check_s11_pt.py`（只写进本 scratch，未动 en 原件与仓库任何文件）。改编点：
  - core-en → core-pt；版目录 `2026-w47-pt-es`；页文件名 en `p1-front…p8-test` → pt `p1-capa…p8-avaliacao`。
  - pt-es 版目录无 `registry.json`，Q120 chip 的级别改与 core-pt 直接比对（同坐标同色 `#46581f` = B1）。
  - pt-es P8 无 clozen  passage：不存在 `113. [A2] A. vote` 选项行与 `Levels: 145-149 [A2]` 行（core-pt 与本版 P8 全文 0 命中），改查 P8 练习号 113–150 全 present；H WRITING 头改查同行 `150.` + `Escritura` + `B1`（`B1` 为独立元素）。
  - 初版误报：正检查 `re.fullmatch(r"\d+\.", …)` 把 `141. a consciência` 判为缺号（Q141–144 误报 missing）——已修正为行首 `(\d+)\.` 匹配，复跑 ALL PASS（`p8-nums-141.log` 为证）。
- 结果：build-copy 与生产目录两次运行均为 ALL PASS，rc=0。

## 未通过的门

**无。**全部机械门通过；D-NEW1 已修复；首轮 7 项全部存活；150 题手验 150/150。
