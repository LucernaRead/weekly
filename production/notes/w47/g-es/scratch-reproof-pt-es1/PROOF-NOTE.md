# PROOF-NOTE — 2026-W47 pt-es（葡萄牙语目标 · 西班牙语读者版）· reproof 独立复校（fix1 后）

- 版目录：`production/2026-w47/2026-w47-pt-es/`
- 复校员：独立复校（reproof），2026-11-11
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-es1/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3，各工具 runtime 行自证）；`PYTHONDONTWRITEBYTECODE=1`；`TMPDIR=<scratch>/tmp`
- 前置：proof1 = `scratch-proof-pt-es2`（重建版，D-NEW1 报告）；首轮 7 缺陷 = `scratch-proof-pt-es1`

## 结论：(a) 零缺陷，可定稿

**D-NEW1 已修复并三法验证通过；proof1 的 D1–D6、D7 全部存活；150 题逐题手验 150/150；全部机械门通过。无新缺陷。**

**生产目录零改动、未重建生产文件、未 commit、未 push。**开工/收工快照复核：版目录 43 文件（不含 `__pycache__`）、core-pt 38 文件全部 SHA 不变。

## §0 三 SHA 实测（开工核对，与任务书逐字一致；收工复核不变）

| 件 | SHA-256 | 字节数 |
|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | `75e870cf38a85a5c84ed4d02b19923736dcd4756c3e9d12a52cc1778b982f3d3` | 12,933,061 |
| 网 PDF `A-Lucerna-VOL4-web.pdf` | `4e7b30eaa0a1938c28f12fdac1df494b54d94bfccd14261d2de868ff0e36e94d` | 1,140,280 |
| 文 `2026-w47-pt-es.text.md` | `96d6f11a5616ab97291115bb9da0577bce8049031f14988576f6cced77b29e27` | 37,467 |

## §1 D-NEW1 复测：已修复（三法一致，交付 PDF 为准）

- **位置**：P1 右栏 EM POUCAS PALAVRAS 奶油框标题 `EM POUCAS PALAVRAS　EN BREVE`。
- **源码行**：`content12.py:139`：`p.text(bx + 22, 1914, "EM POUCAS PALAVRAS　EN BREVE", 23, "sans", True, OLIVE)`——字号确为 **23pt**（改前 24pt）；文字一字未改。框 rect（SVG）：`x=1439.5 y=1874 w=422.5 h=474` → 框右缘 **1862.0**。
- **实测**（`boxtitle-advance.log` / `boxtitle-trueink.log` / `pdf-render-titles.log` / `card-probe.log`）：

| 方法 | 实测右缘 | clear | 门限 |
|---|---|---|---|
| advance（boxtitle_core.py） | 1848.7 | **+13.3** | > 0 |
| PIL 真墨（boxtitle_trueink.py，本字号 23pt 粗体） | 1848.5 | **+13.5** | > 0 |
| **交付印 PDF 渲染**（pdftoppm 96dpi，1:1 单位） | 1848 | **+14** | **≥ +5** |
| **交付网 PDF 渲染**（同法，P1） | 1848 | **+14** | ≥ +5 |
| CairoSVG 卡片（同 SVG） | 1848 | +14 | 交叉验证 |

- **逐列计数**（印/网 P1 标题带 y 1892–1918，亮度<190）：x=1846: 9px、1847: 8px、1848: 6px、**x≥1849 全部 0px**。改前对照（proof1）：x=1863: 9、1864: 6、1865: 2。
- **渲染证据**：`p1-enbreve-title-pdf.png`（交付印 PDF 渲染 4× 裁切，x 1700–1900 / y 1870–1945）：末字母 `E` 止于奶油盒内，盒右缘外为空白；P1 整页目视（`render/print-p-1.png`）：标题在盒内，顶栏标语、头条、quiz 均正常，无其他可见变化。
- **改动范围独立复核**：其余 7 页 SVG 与 proof1 build-copy SVG **逐字节相同**（`cmp`）；P1 仅差 1 个 token——`font-size="24"` → `"23"`（x=1461.5 y=1914，文案不变）。build-copy 内 `run.py` 重建 8/8 与生产 SVG 字节相同；重渲染印 PDF SHA 与交付件逐字相同（`75e870cf…` / 12,933,061 B）；8 张卡片与生产卡片逐字节相同。

## §2 首轮缺陷存活复验（D1–D7，全部独立重测）

| # | 首轮缺陷 | 本次复测 | 结果 |
|---|---|---|---|
| D1（核心） | P1 EM-BREVE 框末行在框外 +33px | 框底 2348.0、末行基线 2327.6、真墨底 2332.6、余量 **+15.4**（creambox-diag）；交付 PDF 渲染：墨止于 2331，2349–2350 行为 422px 通栏 quiz 分隔线（盒外，与文本分离），其后为 quiz 内容；奶油底边实测 2347 | **存活** |
| D2（核心） | P3 日程框末行 `16h30.` 在框外 +16px | 框底 551.0、末行基线 540.6、真墨底 540.9、余量 **+10.1**；PDF 渲染：墨止于 539，框下无深色行 | **存活** |
| D3（核心） | P6 时间线框末行降部越边 6px | 框底 854.0、末行基线 840.8、真墨底 846.0、余量 **+8.0**；PDF 渲染：墨止于 844，框下无深色行 | **存活** |
| D4（本版） | P2 `PARA NÃO ERRAR　La regla para recordar` +67px | 源 `tables_es.py:58`「口诀」→`La regla` 已落地；旧长 gloss 全版 0 处；PIL 真墨 863.5、clear **+97.5**；PDF 渲染 863、clear **+98**；卡片 865、clear +96 | **存活** |
| D5（本版） | P7 `ERROS COMUNS　Errores frecuentes` +13px | 源 `tables_es.py:107`「常见错误」→`Errores` 已落地；PIL 真墨 1750.5、clear **+111.5**；PDF 渲染 1750、clear **+112**；卡片 1749、clear +113 | **存活** |
| D6（本版） | P7 `A PALAVRA　La palabra de la semana` +17px | 源 `tables_es.py:136`「本周生词」→`La palabra` 已落地；PIL 真墨 1724.5、clear **+137.5**；PDF 渲染 1724、clear **+138**；卡片 1726、clear +136 | **存活** |
| D7（核心） | P8 范文第 2–3 行超出版心 +2/+14px | 范文 10 行（`Texto modelo`，y=703.6–879.1）交付印 PDF 渲染逐行与 proof1 旧值完全相同，最右墨 1829、最小余量 **+33**；重建印 PDF 逐行相同（+33）；卡片最右墨 1840、最小余量 +22 | **存活** |

## §3 盒标题计数裁定：31 行（fix1 正确，proof1 的 30 行有误）

advance / PIL 真墨 / 交付 PDF 渲染三法各自独立计数均为 **31 行**，0 溢出；三法最小余量分别为 +10.5（P1 `A SEMANA EM NÚMEROS　En cifras`）/ +10.5 / +12（同条）。其余 24 行 advance ≥ +23.6、真墨 ≥ +23.5、PDF ≥ +24。D-NEW1 为最紧项（+13.3 / +13.5 / +14）。

## §4 150 题手验（全文通读 text.md 534 行，逐题核对题干、键与正文）

**150/150 通过。**要点（与 fix1 §3 逐项一致，本次独立复核）：

- Q1–10：consciência/feriado/sexta/três/6/decidem；quiz B/B/C/B。
- Q11–28：Q11–15 全 B；Q16–20 cai/dura/descansamos/abrem/aproveita；Q21–24 数字 3/1695/2023/27；Q25–28 配对 a/b/c/d。
- Q29–46：Q29 C（1695-11-20）、Q30 A（Alagoas）、Q31 B（14.759 使成国定假日，12.519 仅设纪念日）、Q33 A；Q34–39 quilombo/resistência/escravizados/líder/memória/combate；Q40–43 morreu/nasceu/defendeu/formaram；Q44–46 组句逐字一致。
- Q47–64：Q47 A、Q48 B、Q49 B、Q50 B、Q51 A（Norris）；Q52–55 b/a/d/c；Q56–59 mais/mais/mais/menos；Q60–64 empatou/venceu/abriu/garantiu/foram。
- Q65–82：Q65–69 B/B/A/B/B；Q70–75 gabarito/oficial/extraoficiais/**espera**/nota/pesa——Q73 重点复核：正文「Depois da prova, começa…a espera pelo gabarito」原文贴合；Q76–79 sairá/publicarão/decidirá/chegará；Q80–82 V/F/V。
- Q83–100：图表算术独立验算——11 月 16–30 日共 15 天，工作日 10 天（16–19、23–27、30），周末 + 假日 5 天（21、22、28、29、20），10+5=15；Q83 B、Q84 A、Q85 B、Q86 B、Q87 B；Q88 A、Q89 B、Q90 B、Q91 B、Q92 B；Q93–96 serão/contam/fixa/pesa；Q97–100 prazo/dia útil/coerência/chute。
- Q101–112：em/numa/é/B（aproveitamos）/empatou/venceu/abriu/B（saíram）/sair/for/tiver/B（sair）。
- Q113–132：A/A/B/A/B（Q116 6 日、Q117 Palmeiras、Q119 15 日、Q120 五小时 13h30–18h30）/A/B/A（Q121 B、Q122 A、Q123 B、Q124 B、**Q125 A（36 轮：35 轮止于周四 19，21 日一战属 36 轮）**、Q126 B、Q127 A、Q128 A）；Q129–132 B/B/A/B（Rafael：Salvador/周五 capoeira/周六 Palmeiras×Flamengo/周一查 extraoficial）。
- Q133–136 组句逐字正确；**Q137/138 译文正确**（p8 compare keydiff 预期项）；**Q139/140 反向翻译正确**。
- Q141–144 配对 c/d/b/a；Q145–149 全 A（Mané/sexto/quinto/**na internet**/obrigado）。
- Q150：开放作文；范文手数 **88 词**（× 计为一词，与构建器 `model words: 88` 一致），内容覆盖周五/周六/周日三日与 20 日纪念意义。
- 机械背书：keycheck 149/150（唯一不符 Q150 开放题，预期）；p8 compare CLEAN，keydiff=[137, 138]；Respostas 修正版三方比对 150/150 解析、0 不符（Q150 除外，见 §5）。

## §5 工具链勘误再确认（两则均已独立复现，不沿用旧版）

1. **Respostas 解析器 v1/v2 只能解析 143 条**：本轮重跑 `resp_compare.py`（v1）与 `resp_compare2.py`（v2）均只解析出 **143 条**，漏 [11, 29, 47, 65, 83, 101, 113]（7 个页首题），mismatches 各 14 条——页眉分隔所致，非内容问题。本轮用修正版 `resp_compare_fix.py`（页眉归一化为 ` · ` 后再解析）：8 处页眉归一化，**150/150 解析，0 不符**（Q150 除外：Respostas 为 `✓ Ver el texto modelo…(88 palabras)`，与 REG 开放题注述同义）。
2. **proof 的 `card-probe3.log` 为失败日志**：未引用其数值；D7 本轮用 `d7_essay_measure.py` 在真正的范文 10 行上独立重测（交付印 PDF +33 / 重建印 PDF +33 / 卡片 +22，与 proof1/fix1 逐行一致）。

## §6 标语核实（不列为缺陷）

P1 顶栏标语「El portugués que lee Brasil」**仍为原句，未动**：源 `tables_es.py:201`「读巴西人正在读的葡萄牙语」→「El portugués que lee Brasil」；`content12.py:15` 顶栏整行原文保留；SVG 元素 `<text x="622.6" y="92" font-size="17" …>TODA SEMANA EM PORTUGUÊS　Cada semana　El portugués que lee Brasil</text>`（跨度 [622.6, 1327.4]）；SVG 内 1 处，印 P1 文字层 1 处，网 P1 文字层 1 处。已裁定语法正确（西语 que 作宾语、主语后置，与法语/意语同类结构一致），**绝不列为缺陷**。

## §7 其余裁定

- **−0.3px 两处为字体度量 artifact，非缺陷**（与 fix1 裁决一致，本轮卡片独立重测）：P4 E VOCÊ 框底 876 以下 **0 个**深色像素；P7 词框底 1461 以下 **0 个**深色像素；P2 E VOCÊ 框底 909 以下 0 个；P5 框底 811 以下首现为 841 行的分隔线（后继内容，非本框末行）。
- 孤儿标点扫：A 类 4 处均为 P8 答案行键值分隔符（`56. mais — 3 > 1:mais` 等，与核心版同格式，p8 compare CLEAN）；B 类 0；C 类 6 处全为合法引导冒号；D 类 0；E 类 1 处 Q38 `Sem ___ , não há futuro.`——与核心版同行逐字相同，空白占位符固有格式。
- 宽带扫描说明：`card_probe.py` 的 P8 Respostas 列表扫描（band 内 x 延至 1949）在 y=1472 行读到 1856（卡片）——与 fix1 的数值一致，**非回归**；该读数是同 y 带内其他栏的墨迹，非本行自身墨迹。权威的 D7 判定是 §2/D7 的范文 10 行列内限宽测量（PDF +33 / 卡片 +22）。

## 缺陷清单

**无。零缺陷。**
