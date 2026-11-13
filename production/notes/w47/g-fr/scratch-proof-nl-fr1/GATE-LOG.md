# GATE-LOG — 2026-W47 nl → fr（proof1，build-6）

校对员 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-fr1/`
除注明外，全部命令均以 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）运行；重建只在 scratch 副本里做；生产目录零写入、未 commit、未 push。证据文件均在 scratch 内，文件名见各节。

## §0 身份核对（开工与收尾两次实测一致）

- 印 PDF `De-Lucerna-VOL4-nl-fr.pdf`：SHA `6aedb91fdc857b2ae545795b490c10b95400925ab1f430c658ca34922fd92d47`，12,656,006 B。
- 网 PDF `De-Lucerna-VOL4-nl-fr-web.pdf`：SHA `4f78d3a7c804ceb6d57fbde3e94cc91da21cf12c37360d4203238abf21a02f06`，1,612,639 B。
- text.md `2026-w47-nl-fr.text.md`：SHA `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a`，47,744 B。
- 核心对照（只读）：印 `b7d4a9cddbc38dd56ddd22cd2ae15a2e04ba1988670b6cf384eafbc66bd7ce47` / 25,955,578 B；网 `5a47449cdff7d5847aee81c1c5b0f1af54cfeda873c5b55058a6d18f0e10404c` / 2,104,000 B；文 `0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c` / 44,093 B。
- pre-delta 参照（`fanout-nl/2026-w47-nl-fr/`）：SVG 逐字节比对——仅 p4、p8 不同，其余 6 页相同；text.md diff 恰 415 行（`kort `，+5 B）。
- 生产文件收尾复核：三 SHA 与开工一致；8 个生产 SVG SHA 与开工一致。

## §1 构建重建（`run.log`）

- 命令：scratch 副本 `rebuild/` 内 `run.py`（输出重定向绝对路径 `$S/run.log`，目标在 scratch 内，开工前已核对）。
- 结果：rc=0；TOTAL **150**；by page 10/18/18/18/18/18/12/38；by level A2 46 / B1 73 / B2 31；`grep -ci "overflow\|too wide"` = **0**；`P4 col3 ends 1229.6`；`P6 chart ends 717`、`P6 col3 ends 1052.0`、`P7 col3 ends 1927.0` 与修前一致。
- 重建 SVG vs 生产 SVG：**8/8 字节一致**（逐页 sha256 比对）。

## §2 freeze（`freeze-core.log` / `freeze-ed.log` / `freeze-diff.log`）

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out $S/freeze-core`：rc=0，**8/8 字节一致**；核心完整性复核通过（运行前后 8 文件重哈希无变）。
- 本版自身 8/8：`freeze.py baseline --build <本版> --core-svg <本版>/svg --out $S/freeze-ed`：rc=0，**8/8 字节一致**。
- `freeze.py diff --core-svg core-nl/svg --edition-svg <本版>/svg --json freeze-diff.json`：rc=0；逐页增减 +27/+44/+30/+29/+41/+36/+47/+181；**新增 CJK 仅 7 个 U+3000**（P2–P8 各一，P1 为零），无任何汉字新增。

## §3 occlusion 真实审计（`occlusion.log`）

- 命令：`tools/occlusion_audit.py <本版>/svg/`。
- 结果：rc=0；自检 `selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}; clean controls silent`；**0 flags**。
- 保留意见：occlusion 对横向越框、盒标题溢出、盒底溢出、D11 类整行出盒有盲区——盒标题与 D11 已另用 PIL 真墨 + 交付 PDF 渲染像素双法重测（§7、§8），occlusion 0 不单独作证。

## §4 p8 extract / compare（`p8-extract.log` / `p8-compare.log` / `p8-compare.json`）

- `p8.py extract --p8 <本版>/svg/p8-toets.svg --total 150`：rc=0，noted set **150/150**。
- `p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 <本版>/svg/p8-toets.svg --total 150`：rc=0，**status: CLEAN**，missing=[]，extra_count=0，uncertain=[]；**keydiff=[137, 138]**。
- keydiff 裁决（合法重定向，非缺陷）：
  - #137：core `圣诞老人新闻每天 18:00 播出。` → 版 `Le journal de Sinterklaas passe chaque jour à 18 h 00.`——荷→法翻译题，译文正确（正文 P3）。
  - #138：core `前两名晋级四分之一决赛。` → 版 `Les deux premiers passent en quart de finale.`——荷→法翻译题，译文正确（正文 P4）。

## §5 150 题三方逐题手验（`stem-key-compare.log` / `keycheck-3way.log` / `p8-compare-3way.json`）

- registry 来源：本轮自己导出——`dump_reg.py` 在 scratch 副本内重跑 5 个 content 文件，分别导出核心 `registry-core.json`（150 条）与本版 `registry-ed.json`（150 条），级别分布两版皆 A2 46 / B1 73 / B2 31。
- 三方（registry vs text.md vs P8 印键，`keycheck_3way.py`）：**149/149 MATCH**，DIFF=[]，MISSING=[]；Q150 开放写作例外（P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为读者语占位）。
- 题干 vs 核心（text.md，`stem_key_compare.py`）：148/150 逐字一致；仅 139/140 不同——按设计为读者语题干（核心中文 `阿姆斯特丹的入城式是第 88 届。` / `我做一个带小诗的伪装礼物。` vs 本版法文 `L'arrivée à Amsterdam est la 88e édition.` / `Je fais une surprise avec un petit poème.`），已对 `content8.py` 的 `ex()` 原文与两版 P8 SVG 核实；其余题干（含配对项 25–28、141–144）逐字一致。
- 键 vs 键（registry）：147/150 一致；仅 137/138（翻译键即读者语）与 150（开放题占位）按设计不同；级别/页码 0 差异。
- text.md 答案 vs 自身 registry 键：两版皆 0 差异（Q150 除外）。
- Q140：registry = text.md:415 = P8 印键 = `Ik maak een surprise met een kort gedicht.`；题干含 petit（法文）/ 小（核心中文），键含 kort，对应关系成立；text.md diff 恰 415 行。
- 配对键：25–28 = d/c/a/b；141–144 = b/c/d/a。
- 范文：81 词（核心同数同口径；题求 80–100 词）。

## §6 印/网文字层（`print-web-text.log`）

- 方法：PyMuPDF 位置排序逐词比对（`print_web_text.py`）。
- 印 vs 网：8 页 posdiff 0、msdiff 0（词数 826/834/730/736/811/758/950/2461）；pdftotext 印 46,867 B = 网 46,867 B。
- 印文字层 vs build-5（fanout staging）：unified diff 恰好 Q140 一行（`Ik maak een surprise met een gedicht.` → `Ik maak een surprise met een kort gedicht.`），D11 不改文字，零其他差异。
- P8 最小字号（交付印 PDF，PyMuPDF spans）：**min 10.12pt**（174 spans；中位 10.35）≥ 9.75pt（SOP §1.1 下限）。
- 补充（P1 HET WOORD 法语两行 vs y=1853 横线，交付 PDF 1:1 渲染像素探查）：上行末墨行 1850（线顶 1852.4，余量 +2.4px），下行首墨行 1857（线底 1853.6，余量 +3.4px），紧但不触线；p1 SVG 与 pre-delta 逐字节一致，非 delta 引入。

## §7 盒标题横扫 + creambox + spill（`titles-pdf.log` / `creambox.log` / `spill-sweep.log`）

- 盒标题（`titles_pdf.py`，56 个，**以交付印 PDF 的 1:1 fitz 渲染像素裁决**，探针为文本自身 advance 跨度）：**0 越边**。最紧：P6 `DE GRAFIEK　DONNÉES FICTIVES` +13.0px、P7 `HET WOORD　MOT DE LA SEMAINE` +13.0px、P6 `VOOR OF TEGEN?　POUR OU CONTRE` 与 P7 `PAS OP!　CLINIQUE DES ERREURS` +16.0px。
- creambox（`creambox.py`，几何警告带：右界 rect−8px、底界 baseline+0.3×size vs rect−2px）：警告带 3 处——P1 CREAM-RIGHT（`DE WEEK IN CIJFERS　EN CHIFFRES`，几何右 956.5 vs 盒右 961.0）、P2/P5 CREAM-BOTTOM（`rédaction.` / `envoie-les.`）。交付 PDF 像素裁决：**全部假阳性**（真墨余量 P1 右 +6.0 / P2 +6.8 / P5 +7.5px；盒底下 7px 条带 0 非纸像素）；**真溢出 0**；P4（D11 盒）0 flags。
- spill 横扫（`spill_sweep.py`，60px 窗口）：候选 BELOW 6 / ABOVE 22 / SIDE 3，逐项裁决均为独立相邻版块（下一节标题、提示语、gloss、图注、邻盒标题）；P4 HET PROGRAMMA 盒 BELOW 命中 0。P6 的 ABOVE 命中（683.86/708.28 两行）为上方图表盒内的 D8 图注原文，归属已对 `content56.py:143–158` 核实，非溢出。

## §8 Delta 六处复核（`width-scan.log` / `d11-measure.log` / `orphan-sweep.log`）

- 宽度带（`width_scan.py`，本版文字 + 本版 `svglib.wrap()`，0.1px 步进重算，机制与调用点源码实测在）：
  - D6：带 **410.8–512.4**，w=430.4 在带内；wrap 复现 2 行；SVG 行与基线 2303.5 / 2333.22 逐字一致。（delta 称上界 450.0，本轮重算 512.4；选中值在双方带内，无影响。）
  - D7：带 **419.2–447.7**，w=433.45 在带内；3 行，基线 725.66 / 755.39 / 785.11。
  - D8：带 **359.7–404.8**，capcn_w=382.25 在带内；4 行，基线 635.02 / 659.44 / 683.86 / 708.28；`P6 chart ends 717` 不变。
  - D10：带 **367.5–451.2**，dt_zh_w=408.75 在带内；2 行，基线 1783.27 / 1811.67；`P7 col3 ends 1927.0` 不变。
  - 机制：`bslib4.py:119` `para(..., w=None)` 与 `bridge(..., w=None)` 在位；`capcn_w` / `dt_zh_w` 各在盒高与渲染两处同用。
- D11（`d11_measure.py`，双法）：源码 `content34.py:130` `sh = 89 + ...`（37 行 P3 盒仍 `sh = 62 + ...` 未动）；5 句断行 [3, 3, 3, 2, 3] = 14 行，重算 sh = 638.0 = SVG 盒高；盒 (1439.5, 591.6, 422.5, 638.0) 底 1229.6，末行 `18:45 uur.` 基线 1209.49 → **几何余量 +20.11px**；交付 PDF 渲染像素最低墨行 1209 → **真墨余量 +21px**，盒底下 7px 条带 0 非纸像素。
- 孤儿标点横扫（`orphan_sweep.py`，1458 行，PIL + svglib 双 advance，CJK + 拉丁标点）：独行标点 **0**，行首标点 **0**，8 页全 0；brute-force 以标点开头的 `<text>` 元素 **0** 个。
- D6/D7/D8/D10 目标行内容搜索（orphan-sweep.log 末尾）：各行原文与基线与 §8 带扫描一致。

## §9 §1.1 检查（`check-s11-nl.log`，`check_s11_nl.py` 为 nl 适配版）

- 纸色 `#fbfaf6` rect 8 页齐；颜色集合核心=本版（19=19，无增减）；徽章色 A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` 均在版。
- VOL.4 / VOL.5 计数逐页与核心相等（P1 VOL.4 3=3；P2 VOL.5 1=1；P7 VOL.5 4=4；其余 VOL.5 0=0）。
- 徽章 rect 逐页计数与颜色多重集与核心相等：P1–P8 = 10/15/18/18/18/18/12/35。
- P8：SVG 最小 font-size 属性 13.5；徽章 35=35；24pt 题头徽章颜色 0 不符；配对头 `25–28.`（P2）与 `141–144.`（P8）齐全。
- 方法备注：初版检查曾报 Q150 题头徽章不符与 `25–28.` 缺失——复核为检查器假设错误（P8 答案区 `150. ` 13.5pt 键行本无徽章，与核心同构；`25–28.` 头在 P2 不在 P8），已修正检查器并重跑通过；不作缺陷。

## §10 前轮 proof1 四项缺陷的本版复核（D1–D4 alpha，build-5）

- D1 P7 标题：现为 `HET WOORD　MOT DE LA SEMAINE`；交付 PDF 真墨右 1849 vs 盒右 1862.0，**余量 +13.0px**（`titles-pdf.log` p7 行）。已修复。
- D2 P6 标题：现为 `VOOR OF TEGEN?　POUR OU CONTRE`；真墨右 1846，**余量 +16.0px**。已修复。
- D3 网 PDF 斜体：网 PDF 含 `LucernaNewsreader-Italic`；P1 `«de groepswinst»` 在网 PDF 中为 `LucernaNewsreader-Italic` 16.12pt（印 PDF `Newsreader16pt-Italic` 16.12pt）；**斜体 span 数印 == 网 == 1**。已修复（仅凭印/网词层一致不能作证斜体，故另查字体）。
- D4 撇号：8 页 SVG 中 U+2019 = **0**；text.md 与印/网 PDF 文字层中 U+2019 / U+2018 均为 0。已修复。
- D5 字体（只记录，不修，不作门）：纯拉丁文段落在 CJK 字体上 **500 段**，逐页 [59, 67, 58, 58, 62, 62, 64, 70]，全在 Noto Sans CJK SC；字体总段数 Sans CJK SC 500 / Newsreader 929 / UnifrakturMaguntia 1。

## §11 目视（`render/p1–p8.png`，交付印 PDF 150dpi 渲染）

- P1–P8 逐页目视干净：无溢出、无遮挡、无截断、无错字；页脚 `Page N sur 8`、刊头 VOL.4、双语栏标全齐。P3/P6/P7 栏中留白为 build-5 既有版式（三页 SVG 与 pre-delta 逐字节一致），非 delta 回归。

## 结论

**全部 11 节门禁通过，缺陷 0 项。(a) 零缺陷，可定稿。**
