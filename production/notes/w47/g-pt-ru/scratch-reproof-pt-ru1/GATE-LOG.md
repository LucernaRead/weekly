# GATE-LOG — 2026-W47 pt-ru re-proof 机械门实跑证据

复校：re-proof 独立复校，2026-11-11。全部命令以 `~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3）
实跑，`TMPDIR=<scratch>/tmp`，日志与 JSON 均存于本 scratch 目录。生产目录零写入（47 文件开工快照，
完工复核 0 非 OK；run.py 三次重跑后字节不变）。正典 creambox：`hidden_files/w47/tools/creambox.py`，
md5 `ee7a55d8b2057cf4ad42a97bb1197383`（已验，与 proof1 同一正典）。

## §0 身份与探针

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；
  goals 侧 `hidden_files/w47/scratch-reproof-pt-ru1/` 写入成功。
- SHA（`sha256sum` 实测，开工与完工两次一致，与任务给定新版值一致）：
  - 印 `A-Lucerna-VOL4.pdf` `86447421b5a5abff48690ed8ab8e4cd51ce9808e5adcaf24f0d8e30004a0d2f2`，12,916,388 字节
  - 网 `A-Lucerna-VOL4-web.pdf` `acd86e86bc20562c2080952bec2c89071c85c1733d2cb5183f4dc6d90253b779`，1,188,615 字节
  - `2026-w47-pt-ru.text.md` `87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8`，39,736 字节，535 行

## 1. run.py — rc=0，TOTAL 150

`run.log`：`TOTAL 150`，by level A2 48 / B1 71 / B2 31，by page 1:10 2:18 3:18 4:18 5:18 6:18 7:12 8:38，
model words 88。P8-keys flow 末 y=2556（bottom 2560），P8 exercises 末 y=976.15。
重跑三次（run.py / keycheck 内嵌 / REG 导出）后 47 个生产文件与开工快照逐字节一致。

## 2. gates.py（builder 自查，复跑）— 16/16 PASS，rc=0

`gates.log` 全文 16 行 PASS，FAILURES: none。要点与 proof1 一致：`P1 VOL.4 + week dates` /
`P1 subtitle topics` / `footer+page line 8/8` / `no VOL.3 residue` / `press-time note + final named` /
`P1 masthead lines fit 1820` / `same-baseline ink collisions = 0` / `page-frame ink crossings = 0` /
`P6 chart-label coverage <30%` / `gloss items enumerated`（29）/ `gloss headwords survive`（0 missing）/
`P7 quotes 2x + page tag + RU`（8/8）/ `readers corner disclosure`（5/5）/ `images + credits 5/5` /
`P7 quotes clear of preview box`（max baseline 2351.17）/ `P1 headline <= 56`（41 字符）。

## 3. occlusion_audit.py — 0 flags（本版与 core-pt 均 0；KIT §6 的 1 flag 已过期）

- `occlusion.log`：selftest OK（planted `BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX` 各 1，clean controls silent）；
  `svg: 0 flags`，`ru-occlusion.json`：`{"flag_count": 0, "flags": []}`，rc=0。
- `occlusion-core.log`：core-pt/svg 同跑亦 **0 flags**。
- 几何核实：KIT 所称 P1 LINEX graze（quiz 规则线擦 `em Brasília.` 行墨顶 0.2px）在新版几何中不存在——
  规则线现处 y=2350.0，D3 行墨顶 2313.1（PDF 渲染），相距 36.9px；框底 2348.0，规则线在其下 2.0px。
  该说法来自 core fix1 之前的旧几何（proof1 当时实跑亦为 0 flags）。工具与几何一致：无 flag。

## 4. 正典 creambox.py 全版扫描 — 0 真溢出（`creambox-all.log`，438 行）

| 位置 | creambox 读数 | 像素核实（交付 PDF 渲染） | 裁决 |
|---|---|---|---|
| P7 ERROS COMUNS 标题 | （横向，见 §7）墨右 1764.5，clear +97.5 | 墨右 1762.8，clear +99.2 | **D1 修净** |
| P1 数字框标题 | （横向，见 §7）墨右 1391.0，clear +20.5 | 墨右 1388.0，clear +23.5 | **D2 修净** |
| P1 EM POUCAS 框末行 `em Brasília.` | inside 末行 +20.4；框底 2348.0 | 奶油底 2347.7，墨 2313.1–2331.8，clear +16.2 | **D3 修净** |
| P3 周框末行 `16h30.` | inside 末行 +10.4；框底 551.0 | 奶油底 550.6，墨底 540.5，clear +10.5 | **D4 修净** |
| P6 时间线框末行 `Página do Participante.` | inside 末行 +13.2；框底 854.0 | 奶油底 853.4，墨底 845.3，clear +8.7 | **D5 修净** |
| P2 SÁB 21 格末行 `Палмейрас–Фламенго` | inside 末行 +6.8；框底 1768.0 | 奶油底 1767.4，墨底 1765.0，clear +3.0 | **SÁB 21 正确，在框内** |
| P7 A PALAVRA 框末行 | inside 末行 +4.5，desc-clear −1.5 | 墨底 1430.9 < 框底 1431.5（+0.6 内） | 非缺陷（O3，PDF 渲染裁决） |
| P2 E VOCÊ 框 | inside +5.0，desc-clear −1.0 | 墨底 907.7 < 框底 909.0 | 非缺陷 |
| P3 E VOCÊ 框 | inside +5.1，desc-clear −0.9 | 墨底 878.4 < 框底 880.0 | 非缺陷 |
| P4 E VOCÊ 框 | inside +5.1，desc-clear −0.9 | 墨底 903.4 < 框底 905.0 | 非缺陷 |
| P5 E VOCÊ 框 | inside +5.7，desc-clear −0.3 | 墨底 838.6 < 框底 840.5 | 非缺陷 |
| P5 数字框 `2027.` | inside +5.4，desc-clear −1.1 | 墨底 507.4 < 框底 513.0（无降部字母） | 非缺陷 |
| P7-TOOLBOX 汇总 | 3 框，min inside +4.5，min desc-clear −1.5 | — | 通过 |
| 其余全部框 | inside clearance ≥ +4.5 | — | 通过 |

core-pt 对照扫描（`creambox-core.log`）：P1 同窗末行 2327.6/框底 2348.0、P3 `16h30.` 540.6/551.0、
P6 `Página do Participante.` 840.8/854.0——与本版几何完全一致，D3/D4/D5 系 core fix1 盒高修净；
core P7 标题 `ERROS COMUNS　常见错误`、P1 数字框标题 `A SEMANA EM NÚMEROS　数字`（中文 gloss，对照无溢出）。

## 5. p8 compare — CLEAN，keydiff=[137, 138]（`p8-compare.log` / `ru-p8-compare.json` 本体已读）

`core 150 noted / edition 150 noted / status: CLEAN / missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`，rc=0。
- **137**：SVG 答案区 y=2118.4 直读全文 `137. Пятница, 20 ноября, — национальный праздник. — Смотри заголовок на странице 1`
  （续行 y=2133.0），正确俄译；提取器在首个 ` — ` 处截断为工具 artifact，非缺陷。
- **138**：`Палмейрас выиграл 5–4 по пенальти.` = `O Palmeiras venceu nos pênaltis por 5 a 4.`，正确俄译，非缺陷。
其余 148 键与 core 完全一致。

## 6. freeze — baseline 8/8，diff 仅 U+3000

- `freeze.py baseline`：`baseline: 8/8 SVGs byte-identical (repointed files: none)`，8 个 OK，rc=0（`freeze-baseline.log`）。
- `freeze.py diff` vs core-pt：各页增减字符串均为讲解层替换；added CJK 仅 U+3000，共 **9** 个（P1 2，余每页 1），rc=0
  （`freeze-diff.log` / `ru-freeze-diff.json`）。

## 7. boxtitle 逐个实测（PIL 真墨迹，`inkprobe.log` / `boxtitles.json`）

全版横向扫描：无一墨迹超页右边界 1884。全部 33 个奶油框首行标题墨右缘 vs 框右缘：

| 页 | 框标题（首行） | 框右 | 墨右 | clear |
|---|---|---|---|---|
| P1 | A SEMANA EM NÚMEROS　Цифры | 1411.5 | 1391.0 | **+20.5**（D2，PDF 渲染 +23.5） |
| P1 | A SEMANA, DIA A DIA | 1862.0 | 1732.5 | +129.5 |
| P1 | NESTA EDIÇÃO　В этом номере | 1862.0 | 1833.5 | +28.5 |
| P1 | EM POUCAS PALAVRAS　Коротко | 1862.0 | 1853.5 | +8.5（全版最紧） |
| P2 | PARA NÃO ERRAR　Правило | 961.0 | 877.5 | +83.5 |
| P2 | Пояснение — o feriadão… | 961.0 | 928.5 | +32.5 |
| P2 | VOCÊ SABIA? | 1862.0 | 1611.5 | +250.5 |
| P2 | E VOCÊ?　Расскажи о себе | 1862.0 | 1780.5 | +81.5 |
| P2 | o feriado começa | 510.5 | 409.0 | +101.5 |
| P2 | Palmeiras × Flamengo, às | 961.0 | 938.5 | +22.5 |
| P2 | o fim do feriadão | 1411.5 | 1309.0 | +102.5 |
| P2 | tudo volta ao normal | 1862.0 | 1797.5 | +64.5 |
| P3 | Пояснение — o quilombo… | 961.0 | 916.5 | +44.5 |
| P3 | A SEMANA, DIA A DIA | 1862.0 | 1702.5 | +159.5 |
| P3 | E VOCÊ?　Расскажи о себе | 1862.0 | 1780.5 | +81.5 |
| P3 | PALAVRAS DA MEMÓRIA | 1862.0 | 1716.5 | +145.5 |
| P4 | Пояснение — o agregado… | 1411.5 | 1373.0 | +38.5 |
| P4 | OS FINALISTAS | 1862.0 | 1628.5 | +233.5 |
| P4 | E VOCÊ?　Расскажи о себе | 1862.0 | 1780.5 | +81.5 |
| P5 | O PLANO DA ESPERA | 961.0 | 787.5 | +173.5 |
| P5 | Пояснение — o gabarito… | 961.0 | 861.5 | +99.5 |
| P5 | OS JOVENS EM NÚMEROS | 1862.0 | 1761.5 | +100.5 |
| P5 | E VOCÊ?　Расскажи о себе | 1862.0 | 1780.5 | +81.5 |
| P6 | Пояснение — o prazo… | 961.0 | 933.5 | +27.5 |
| P6 | O CAMINHO ATÉ O GABARITO | 1862.0 | 1770.5 | +91.5 |
| P6 | LER OS NÚMEROS | 1862.0 | 1671.5 | +190.5 |
| P6 | A CONTAGEM　do dia 16 ao dia 30 | 961.0 | 456.0 | +505.0 |
| P6 | DOIS GABARITOS　um exame | 1862.0 | 1314.0 | +548.0 |
| P7 | ERROS COMUNS　Ошибки | 1862.0 | 1764.5 | **+97.5**（D1，PDF 渲染 +99.2） |
| P7 | A PALAVRA　Слово недели | 1862.0 | 1769.5 | +92.5 |
| P7 | CARTAS DOS LEITORES | 1862.0 | 1718.5 | +143.5 |

最小余量 +8.5，无负值。P1 头条墨 x=88–1351，无溢出。

## 8. keycheck — 148/150（按设计 rc=1；两项均已裁决非缺陷）

独立重跑改编版 `keycheck_ptru.py`（REG key vs p8-extract）：`REG entries: 150; exact match: 148/150`，
mismatch 仅：
- n=137（Перевод）：REG `Пятница, 20 ноября, — национальный праздник.` vs 提取 `Пятница, 20 ноября,`——提取截断 artifact；
- n=150（Письмо）：REG `(открытое задание — образец ниже)` vs 提取 `✓`——开放题既定标记。
另逐题手验 150/150（`keycheck-150-table.txt`：题干×SVG key×core key 逐行读完，含 Q73 配对）。

## 9. 印/网文字层比对（两种方法）

- `pdfinfo`：两 PDF 均为 8 页，1462.5×2025pt。
- fitz（`check_final_ptru.py` / `ru-textdiff-fitz.json`）：印/网各 **8,093** 词，词多重集差 **0**；
  P8 答案区 span 最小 9.75pt（625 spans，印/网一致）；P8 答案区词数 1,352。
- `pdftotext -layout`（`print.txt` / `web.txt`）：印/网各 8,170 词，多重集差 0；行 diff 仅 40 行，
  全部在 P8，单空格列移（已知非缺陷，与 KIT 所述一致）。
- 自 scratch 重渲染网 PDF（`webpdf.py` → `web-rerender.pdf`，rc=0，8 页，未覆盖生产网 PDF）：
  文字层与生产网 PDF 多重集差 0（8,170/8,170）；italic spans 1=1；字节 1,188,613 vs 生产 1,188,615
  （差 2 字节为已知 fontTools wall-clock 不可复现，永不以字节论证）。
- italic spans 全文档：印 1 = 网 1（P1 `« consciência »`，Newsreader-Italic 16.12pt；`italic-check.log`）。

## 10. check_s11（en 版改编，`check_s11_ptru.py`）— ALL PASS，rc=0

对 core-pt 逐页比对：纸色 `#fbfaf6` 8/8；VOL.4/VOL.5/VOL.3 计数逐页相等（总量 VOL.4=9、VOL.5=3、VOL.3=2；
VOL.5 仅 P7 预告/披露内，VOL.3 仅 P7 披露内）；chip rect 数逐页相等（P1 10、P2 15、P3 18、P4 15、P5 18、P6 18、P7 12、P8 35），
颜色多重集相等；颜色集 core 21 = edition 21，无增减；徽章三色齐全；禁色 `#f7f1e2/#c9a227/#8b4513/#000000` 全无；
masthead 196px、band 46px 在；左缘最小 x=88.0；可见 SVG 无 CJK（U+3000 除外，moth `<title>` 已剥离）；
页脚 8 页均 `A Lucerna　ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4　…`（U+3000 分隔）。
P8：最小字号 13.0 单位 = 9.75pt；答案区最小 13.0 单位（1339 spans）；Q113–120、Q145–150 chip 逐题核对，
级别色与 REG 一致（全 B1，`#46581f`）；`H ESCREVA VOCÊ` 在；bridge 2 行
（`Письменное задание; образец текста (88 слов) — ниже.`，y=578.1/607.8，x=1440）。

## 11. sweep（box-vs-hline / bridge orphans / bridge widows）— 0/0/0

重跑改编版 `sweep_ptru.py`（`sweep.log`）：box-vs-hline flags 0；bridges 20，orphans 0；widows 0。

## 12. P8 最小字号实测

SVG 答案区（y>1250）：最小 **13.0 单位 ×0.75 = 9.75pt**，共 1327 个 span，恰为 SOP §1.1 下限；
P8 答案流末行基线 2546.7（页脚 2624 除外），墨底约 2551 < 2560，余量约 9px。

## 13. 弯引号 + CJK 全版扫描（`inkprobe.log` §D/E）

- U+201C/U+201D/U+2019：P1–P7 全部为 0；P8 为 201C×2、201D×2、2019×0——位于 E139/E140 俄语句源，正确用法；
  正文内容中直引号 `"` 为 0（标签剥离后统计）；直单引号仅 P7 ×2（`'выпадать на день'`，与 pt-en 同型释义引用，非缺陷）。
- CJK：P1 仅 moth logo `<title>` 内 `三色蛾`（非读者面）；其余 7 页无 CJK（U+3000 除外）；text.md CJK 字符 0。

## 14. 标语主客 + 事实

- P1 顶栏标语：`Португальский, который читает Бразилия`——`который` 为无生命阳性宾格（=主格形），
  `Бразилия` 为主格主语，解析为“巴西读的葡语”，与中文「读巴西人正在读的葡萄牙语」一致，正确。
- 星期/日期（`date -d`，America/Toronto）：2026-11-15 周日、11-16 周一、11-17 周二、11-20 周五、
  11-21 周六、11-22 周日、11-27 周五、12-06 周日、11-07 周六、11-08 周日、11-30 周一——与版内全部一致。
- 样文 88 词（程序计数）；Enem 次日 13h30–18h30 = 5 小时；工作日 10+5=15。

## 15. 判为非缺陷的项（汇总）

1. E VOCÊ 各框 desc-clear −0.3…−1.0（P2/P3/P4/P5）——PDF 渲染墨底均在框底内 1.3–1.9px。
2. P5 数字框 `2027.` desc-clear −1.1——无降部字母，渲染墨底 507.4 < 框底 513。
3. P7 A PALAVRA 框 desc-clear −1.5——渲染墨底 1430.9 < 框底 1431.5（+0.6px 内，O3；PIL 亚像素读数 1432.0 以 PDF 渲染裁决）。
4. 四处 BELOW-WINDOW 负值——框下另起标题/正文，假阳性。
5. Occlusion KIT 称 1 flag vs 实跑 0 flags（本版与 core 均 0）——旧几何说法已过期；新几何中规则线与墨顶相距 36.9px，无擦过。
6. keydiff [137, 138]——正确俄译；137 提取器截断为工具 artifact（SVG 全文已直读）。
7. keycheck 148/150——仅 Q137（截断）与 Q150（✓）两项既定例外。
8. print/web `-layout` 40 行 P8 单空格列移——词多重集差 0，已知非缺陷。
9. P7 直单引号 ×2——与 pt-en 同型释义引用惯例。
10. KIT 词数 8,095 vs 实测 8,093——KIT 笔误（其自家 JSON 亦为 8,093）；diff=0 结论正确。
11. D2 clear KIT 称 +20.2 vs 实测 PIL +20.5 / 渲染 +23.5——量测口径差，均在框内。

## 文件清单（本 scratch）

`PROOF-NOTE.md` / `GATE-LOG.md` / `keycheck-150.json` / `keycheck-150-table.txt` / `stems.json` / `registry.json` /
`run.log` / `gates.log` / `occlusion.log` / `ru-occlusion.json` / `occlusion-core.log` / `core-occlusion.json` /
`p8-extract.log` / `ru-p8-extract.json` / `p8-compare.log` / `ru-p8-compare.json` / `core-p8-extract.json` / `core-p8-extract.log` /
`freeze-baseline.log` / `freeze-diff.log` / `ru-freeze-diff.json` /
`creambox-all.log` / `creambox-core.log` / `inkprobe.py` / `inkprobe.log` / `boxtitles.json` /
`pixelprobe.py` / `pixelprobe.log` / `print.txt` / `web.txt` / `web-rerender.pdf` / `web-rerender.txt` / `webpdf-rerender.log` /
`check_s11_ptru.py` / `check_s11.log` / `check_final_ptru.py` / `check_final.log` / `ru-textdiff-fitz.json` / `italic-check.log` /
`keycheck_ptru.py` / `keycheck.log` / `sweep_ptru.py` / `sweep.log` / `presnap.sha256` /
`pdfrender/print-{1..8}.png` / `crops/crop-p*.png`（7 张）/ `backup-edition/`（开工前全版备份，仅作可逆保障）
