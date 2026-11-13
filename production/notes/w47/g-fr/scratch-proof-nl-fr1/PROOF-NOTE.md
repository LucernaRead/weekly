# PROOF-NOTE — 2026-W47 nl → fr（proof1，独立复校，build-6）

- 版：`production/2026-w47/2026-w47-nl-fr/`（荷兰语目标 × 法语读者版，VOL.4，8 版，150 题）
- 任务：delta build-6（core-nl fix3 + fix4 + fix5 同步，D6–D11）独立校对
- 校对员 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-fr1/`
- 日期：2026-11-11
- 方法：全部数字自己重跑、自己重测，不信任任何前人数字。Python 一律 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。重建只在 scratch 副本（`rebuild/`、`core_copy/`）里做，生产目录零写入（开工与收尾两次 SHA 复核一致）。nl 族无现成 check_s11.py / verify_ed.py——本次在自己 scratch 里写了 nl 适配版（`check_s11_nl.py`、`stem_key_compare.py`、`keycheck_3way.py`、`width_scan.py`、`d11_measure.py`、`creambox.py`、`orphan_sweep.py`、`spill_sweep.py`、`titles_pdf.py`、`print_web_text.py`）；en 族原版未动。
- SOP：已读 repo 根 `SOP.md` 全文（§1.1、§8.4）与 `hidden_files/w47/briefs/brief-coordinator.md`。

## 结论：(a) 零缺陷，可定稿

全部门禁一次通过；delta 六处逐项复核通过；前轮 proof1（build-5，见下）四项缺陷已在本版修复并经本轮独立重测证实；150 题三方逐题手验 149/149 + Q150 开放题例外；8 页目视干净。**缺陷 0 项。**

## 身份核对（三 SHA 实测，开工与收尾两次一致）

| 文件 | 字节 | SHA-256（实测） | 与任务一致 |
|---|---|---|---|
| 印 `De-Lucerna-VOL4-nl-fr.pdf` | 12,656,006 | `6aedb91fdc857b2ae545795b490c10b95400925ab1f430c658ca34922fd92d47` | ✓ |
| 网 `De-Lucerna-VOL4-nl-fr-web.pdf` | 1,612,639 | `4f78d3a7c804ceb6d57fbde3e94cc91da21cf12c37360d4203238abf21a02f06` | ✓ |
| 文 `2026-w47-nl-fr.text.md` | 47,744 | `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a` | ✓ |

核心对照（只读，未动）：印 `b7d4a9cd…` / 25,955,578 B，网 `5a47449c…` / 2,104,000 B，文 `0b97a48d…` / 44,093 B，三件与任务一致；freeze-core 另验核心 SVG 运行前后哈希无变。

pre-delta 参照（`fanout-nl/2026-w47-nl-fr/`，staging，未动）：8 个 SVG 比对——**仅 p4、p8 不同，其余 6 页逐字节相同**，与 delta 声称一致；text.md diff 恰为 415 行一行（`kort `，+5 B），47,739 → 47,744 B。

## 缺陷清单

**无。0 项缺陷。**

## Delta 六处逐项独立复核（全部通过）

### D6 结构同步（P3 桥接 w=430.4）——通过
- 机制在位：`bslib4.py:119` `para(..., w=None)`（`w = self.w if w is None else w`），`bridge(..., w=None)` 转发；调用点 `content34.py:78` `e.bridge("Complète au passé composé. Attention aux auxiliaires hebben/zijn.", w=430.4)`（实测源码在）。
- 本版文字 + 本版 `svglib.wrap()`、0.1px 步进重算：**带 410.8–512.4**，w=430.4 在带内；`wrap(..., 430.4)` 精确复现当前 2 行。
- 交付 SVG 实测（`p3-cultuur.svg`）：`Complète au passé composé. Attention aux` (y=2303.5) / `auxiliaires hebben/zijn.` (y=2333.22)，句末 `.` 在行末，无孤儿；p3 SVG 与 pre-delta 字节一致，下游零位移。
- 注：delta 称带上界 450.0，本轮重算上界为 512.4（下界 410.8 一致）。差异在带外侧，选中值 430.4 在双方带内，无影响；以本轮实测带为准。

### D7 结构同步（P7 gloss 桥接 w=433.45）——通过
- 调用点 `content7.py:19` `w=433.45`（实测在）；重算带 **419.2–447.7**（与 delta 声称逐值一致），w 在带内。
- 交付 SVG 实测（`p7-taal.svg`）：3 行逐字相同，基线 725.66 / 755.39 / 785.11，末行 `scoren marquer.`；p7 SVG 与 pre-delta 字节一致，无孤儿。

### D8 结构同步（P6 图注 capcn_w=382.25）——通过
- `content56.py:143–144, 158`：`capcn_w = 382.25`，盒高 `ch` 与渲染 `p.para(..., capcn_w, ...)` 两处同用（实测在）；重算带 **359.7–404.8**（与 delta 声称逐值一致），w 在带内。
- 交付 SVG 实测（`p6-verdieping.svg`）：4 行逐字相同，基线 635.02 / 659.44 / 683.86 / 708.28；`P6 chart ends 717`、`P6 col3 ends 1052.0` 与修前一致，零 y 位移；无行首标点。

### D9 真修（键补 kort）——通过
- 三源一致（逐字相同）：registry 键 = text.md:415 答案 = P8 印键，均为 `Ik maak een surprise met een kort gedicht.`（`content8.py:75`，实测在）。
- 手验题干–键契合：法语题干 `Je fais une surprise avec un petit poème.` 含 petit，键 `Ik maak een surprise met een kort gedicht.` 含 kort，petit ↔ kort 对应（nl-de D12 的教训：题干丢“小”而 key 有 kort 即为缺陷；本版题干有 petit，确认无此缺陷）。核心侧印证：核心 text.md:416 题干中文 `我做一个带小诗的伪装礼物。` 含“小”，键亦为 `Ik maak een surprise met een kort gedicht.`，三方一致。
- text.md diff 恰 415 行一行；keydiff 由 [137, 138, 140] → [137, 138]，140 移出（见下）。

### D10 结构同步（P7 来信 dt_zh_w=408.75）——通过
- `content7.py:91–92, 102`：`dt_zh_w = 408.75`，盒高 `lh` 与渲染两处同用（实测在）；重算带 **367.5–451.2**（delta 称 367.5–450.0，上界差 1.2px 为 0.1px 网格取整口径，无影响），w 在带内。
- 交付 SVG 实测（`p7-taal.svg`）：2 行逐字相同，基线 1783.27 / 1811.67；`P7 col3 ends 1927.0` 与修前一致；无行首标点。

### D11 真修（P4 HET PROGRAMMA 盒顶 62→89）——通过，双法独立重测
- 源码：`content34.py:130` `sh = 89 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30`；第 37 行 P3 SINTERKLAAS 盒仍为 `sh = 62 + ...`，未动。
- 事实句断行重算（serif 21.5，CW−44）：[3, 3, 3, 2, 3] = 14 行；重算 `sh = 638.0`，与 SVG 盒高一致。
- 方法 1（SVG 几何）：盒 `<rect x=1439.5 y=591.6 w=422.5 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基线 y=1209.49 → **盒内余量 +20.11px（≥ +20px 标准）**。
- 方法 2（交付印 PDF 渲染像素，1:1 1950×2700 fitz 渲染）：盒 x 范围内最低墨行 y=1209 → **真墨余量 +21px**；盒底下 7px 条带 **0 非纸像素**；末行墨 x 跨度 1463–1562（文起 x=1461.5）。`P4 col3 ends 1229.6`（run.log）。
- 目视：P4 渲染图上末行在盒内，下有明显留白。

## 前轮 proof1 四项缺陷（build-5）的本版复核——全部已修复

开工时发现 scratch 内留有前轮 proof1（build-5，2026-11-11 11:20–11:37 UTC）的笔记（已保全为 `PROOF-NOTE-build5-alpha.md` / `GATE-LOG-build5-alpha.md`，未改动）。该轮结论为 (b)，四项缺陷针对的是旧 build-5（印 12,704,394 B）。本轮在 build-6 上逐项独立重测（非采信前轮数字）：

| 前轮缺陷 | build-6 本轮实测 | 结论 |
|---|---|---|
| D1 P7 标题 `HET WOORD　LE MOT DE LA SEMAINE` 墨超盒右 +21.6px | 标题已改为 `HET WOORD　MOT DE LA SEMAINE`（`p7-taal.svg` 实测）；交付 PDF 渲染像素：真墨右 1849，盒右 1862.0，**余量 +13.0px** | 已修复 |
| D2 P6 标题 `VOOR OF TEGEN?　POUR OU CONTRE?` 墨超 +0.8px | 标题已改为 `VOOR OF TEGEN?　POUR OU CONTRE`（去尾 `?`）；真墨右 1846，**余量 +16.0px** | 已修复 |
| D3 网 PDF 斜体丢失 | 网 PDF 含 `LucernaNewsreader-Italic`；P1 `«de groepswinst»` 在网 PDF 中为 `LucernaNewsreader-Italic` 16.12pt（印 PDF 为 `Newsreader16pt-Italic` 16.12pt）；**斜体 span 数印 == 网 == 1** | 已修复 |
| D4 撇号混用（U+2019 8 处） | 8 页 SVG 中 U+2019 = **0**；text.md 与印/网 PDF 文字层中 U+2019 / U+2018 均为 0；U+0027 全版统一 | 已修复 |

## 观察类（不列为缺陷，不修版）

- **D5 字体问题（只记录，不修，待用户定范围）**：纯拉丁文段落在 CJK 字体上的分布（fix4 口径：`<text>` 内容含拉丁字母且无 CJK 字、字体为 Noto Sans/Serif CJK SC）。本版实测：**500 段**，逐页 [59, 67, 58, 58, 62, 62, 64, 70]，全部在 Noto Sans CJK SC；字体总段数 Noto Sans CJK SC 500 / Newsreader 929 / UnifrakturMaguntia 1。核心 FIX-LOG 同口径为 206 段（方法未完全一致，不可直接比）。此为全周级已知待定项，不作门禁、不修版。
- **核心继承项**：孤儿横扫 1458 行全 0（见下），本版无核心继承的孤儿填空行可列；前轮 O4（#63/#126“PSV 榜首 26 分”）本轮核实：该事实见于 P4 正文 HET PROGRAMMA 盒（`Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.`），#126 题干“PSV staat bovenaan … met ___ punten”答案 B（26）有据，#63“PSV staat onderaan”键 Niet waar 有据；键与核心一致，不作缺陷。
- **栏中空白**：P3、P6、P7 栏中下部有大面积留白——该三页 SVG 与 pre-delta 逐字节一致，为 build-5 既有版式，非 delta 回归，不列缺陷。

## 核实摘要（已核实无问题）

- 构建：`run.py` rc=0、TOTAL 150、页分布 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31、0 FLOW OVERFLOW / HEAD TOO WIDE（grep 0 命中）；`P4 col3 ends 1229.6`；重建 SVG 8/8 字节一致。
- 冻结：核心 baseline 8/8（rc=0，核心 SVG 运行前后哈希无变）；本版自身 8/8；freeze diff 新增 CJK 仅 7 个 U+3000（P2–P8 各一，P1 为零），无任何汉字新增。
- occlusion 真实审计 0 flags（自检 6 类全触发，干净对照静默）；但 occlusion 对盒标题/横向越框/D11 类整行出盒有盲区——盒标题与 D11 已另用 PIL 真墨 + 交付 PDF 渲染像素双法重测（见上），occlusion 0 不单独作证。
- creambox：警告带 3 处（P1/P2/P5），交付 PDF 像素裁决全部为假阳性（真墨余量 +6.0 / +6.8 / +7.5px）；真溢出 0；P4（D11 盒）0 flags。
- spill 横扫：候选 BELOW 6 / ABOVE 22 / SIDE 3，逐项裁决均为独立相邻版块（下一节标题、提示语、gloss、图注），非溢出；P4 HET PROGRAMMA 盒 BELOW 命中 0。
- 孤儿标点横扫（1458 行，PIL + svglib 双 advance）：独行标点 0，行首标点 0；brute-force 以标点开头的 `<text>` 元素 0 个。
- p8 extract 150/150；p8 compare CLEAN，keydiff [137, 138]（翻译题，键即读者语，按设计不同，译文经核正确）。
- 150 题逐题手验：registry vs text.md vs P8 印键三方 **149/149 MATCH** + Q150 开放写作例外（P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为读者语占位）；配对键 25–28 = d/c/a/b，141–144 = b/c/d/a。
- 题干 vs 核心：148/150 逐字一致；仅 139/140 不同——按设计为读者语题干（核心中文 / 本版法文），已对 `content8.py` 的 `ex()` 原文与 P8 SVG 核实；键 vs 键：147/150 一致，仅 137/138（翻译键即读者语）与 150（开放题占位）按设计不同；级别/页码 0 差异；text.md 答案 vs 自身 registry 键 0 差异（两版皆然）。
- 印/网文字层：8 页逐词位置排序 posdiff 0、msdiff 0（印/网词数 826/834/730/736/811/758/950/2461）；pdftotext 印 46,867 B = 网 46,867 B；印文字层 vs build-5 diff 恰好 Q140 一行（`kort`）。
- P8 最小字号：交付印 PDF 实测 **10.12pt**（174 spans；中位 10.35）≥ 9.75pt（SOP §1.1 下限）；P8 SVG 最小 font-size 属性 13.5。
- §1.1：纸色 `#fbfaf6` 8 页齐；颜色集合核心=本版（19=19，无增减）；VOL.4/VOL.5 计数逐页与核心相等；徽章 rect 逐页计数与颜色多重集与核心相等（P1–P8：10/15/18/18/18/18/12/35）；P8 徽章 35=35，题头徽章颜色 0 不符；配对头 `25–28.`（P2）与 `141–144.`（P8）齐全。
- 盒标题横扫（56 个，交付 PDF 渲染像素裁决）：**0 越边**；最紧三处：P6 `DE GRAFIEK　DONNÉES FICTIVES` +13.0px、P7 `HET WOORD　MOT DE LA SEMAINE` +13.0px、P6/P7 `VOOR OF TEGEN?　POUR OU CONTRE` / `PAS OP!　CLINIQUE DES ERREURS` +16.0px。
- 8 页目视（交付印 PDF 150dpi 渲染，`render/p1–p8.png`）：P1–P8 干净，无溢出、无遮挡、无截断、无错字；页脚 `Page N sur 8`、刊头 VOL.4、双语栏标全齐。

## 附记：scratch 目录既有内容说明

开工时 scratch 目录内已有前轮 proof1（build-5）的中间文件与两份笔记。两份笔记已原样保全为 `PROOF-NOTE-build5-alpha.md` / `GATE-LOG-build5-alpha.md`；本轮同名中间脚本/日志为本轮自己重写的重跑结果，未引用前轮数字；`rebuild/` 副本经核为全新 build-6 复制（8/8 重建 SVG 与生产一致，尺寸与 SHA 相符），无陈旧内容污染。生产目录零写入；未 commit、未 push。
