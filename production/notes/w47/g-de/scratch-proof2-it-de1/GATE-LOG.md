# GATE-LOG — 2026-W47 it-de proof2（独立复校）

- 对象：`production/2026-w47/2026-w47-it-de/`（重扩散新版，core fix3 `36bdec2e`）
- 日期：2026-11-11；复校员：proof2（只读生产）
- 探针：`git hash-object -w /dev/null` → rc=0，`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`；goals-side scratch 真实写盘通过（`probe.txt`）。`PYTHONDONTWRITEBYTECODE=1` 全程，TMPDIR=`$SCRATCH/tmp/`。
- 结论：20/20 门禁通过，但存在 2 项版式缺陷（见 PROOF-NOTE.md §5 D1/D2）。门禁通过 ≠ 定稿。

## 逐门结果

### G1 探针与 SHA 核对 — PASS
- 探针通过（上）。
- 印 PDF `La-Lucerna-VOL4-DE.pdf`：14,037,260 B，SHA `ee5a962f1f3b59a8a225acbf949ee542b7d81f99451cc1dc591babb0a3c3234f` ✓ 与简报一致；8 页，1462.5×2025 pt。
- 网 PDF `La-Lucerna-VOL4-DE-web.pdf`：1,297,292 B，SHA `e6d3df844c9fa4fd3ef5e39dcf6cd80d740dfbd7cc5208384763efc6ee89eb84` ✓ 与简报一致；8 页，1462.5×2025 pt；< 7 MB。
- 文本 `2026-w47-it-de.text.md`：56,699 B，SHA `8660fc02b2510cce831e5c3e57b0020949dc4c05e5d4b1bd30db4e667b4cc222` ✓ 与简报一致；1317 行（+结尾换行）。
- KIT §7 L45–46 所载印/网 SHA 与盘上一致；文本以 56,699 B / 1317 行对上（KIT 未印文本 SHA）。
- 复校结束时三件 SHA 复核不变，mtime 未变（12:17–12:19），生产只读成立。

### G2 run.py（scratch 副本 `$SCRATCH/rebuild/`）— PASS
- RC=0；TOTAL 150；级别 A2 47 / B1 70 / B2 33；页数 10/18/18/18/18/18/12/38；范文 99 词。
- FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE = **0**（`out/run.log`）。
- 流末端与 KIT 一致：P1-headline 1362、P2-ex 2356、P3-main col1 1278、P4-main 650、P4 col3 1140.45、P7 col3 1673.0、P8-ex col3 y=870、P8-keys col3 y=2514（底 2552）。

### G3 SVG 重建 8/8 字节一致 — PASS
- 重建 8 个 SVG 的 SHA 与交付 `svg/` 逐个比对，`sha256sum -c` 全 OK（`shipped-svg.sha256`、`out/rebuilt-svg.sha256`）。

### G4 重渲印 PDF 与交付逐字节相同 — PASS
- `render-scratch.py`（BASE 重定向到 `$SCRATCH/rebuild`）：RC=0；重渲件 14,037,260 B，SHA = `ee5a962f…`，与交付 `La-Lucerna-VOL4-DE.pdf` 逐字节相同（`out/render.log`）。
- web PDF 未重渲染（字节不可复现，只比文字层，见 G8）。

### G5 freeze 核心 baseline 8/8 — PASS
- `tools/freeze.py baseline --build $SCRATCH/rebuild --core-svg <edition>/svg`：**8/8 字节一致**，core 完整性复核通过（`out/freeze-baseline.log`、`out/freeze-baseline.json`）。

### G6 freeze diff vs core — PASS
- 0 unexplained fragments（P1–P7）；新增 CJK 仅 U+3000 ×13（家具分隔符，豁免）；新增全为德语讲解层/家具，删除全为 core 中文讲解层；意大利目标语零改动（`out/gates.log`，gates.py freeze-diff 段）。

### G7 occlusion audit — PASS（但附盲区声明）
- `tools/occlusion_audit.py` 自测：6 类阳性对照全触发、干净对照静默；交付 svg 扫出 **0 flags**（`out/occlusion.log`）。
- 盲区：occlusion 对无边框奶油盒横向溢出是盲的——本轮 D1（+138.5 px）、D2（+30.5 px）均在 occlusion 0 flags 下存在。不得以 0 flags 为盒标题背书。

### G8 印/网文字层一致 — PASS
- pdftotext 多重集相同：各 7,787 词，字符集相等；网 PDF 文字层 46,127 B（与印版逐字节等长）；网 PDF 1,297,292 B < 7 MB。

### G9 P8 最小字号 — PASS
- SVG 最小字号 13.0 px = **9.75 pt**（SOP §1.1 下限）。

### G10 §1.1 视觉规格 — PASS
- 纸色 #fbfaf6 在；无金/砖/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点（预告栏、LETTERE 说明、P2 交叉引用）；徽章色 A2/B1/B2 在；无双层外框（0 全页 rect）。

### G11 奶油盒 PIL 真墨扫 — 2 处溢出（缺陷，见 PROOF-NOTE §5）
- 自写 `creambox-proof2.py`：29 个 #f0eee5 盒全扫。
- **D1**：P1 cifre 盒标题墨迹右缘 1099.5 px，超盒右缘 961 达 **+138.5 px**（源码 `content12.py:44`）。
- **D2**：P2 frase 盒标题墨迹右缘 991.5 px，超盒右缘 961 达 **+30.5 px**（源码 `content12.py:177`）。
- 根因：`bslib4.py:174` `box()`，标题以单行 `self.p.text(x + pad, …)` 绘制（`bslib4.py:186`），无宽度核对。
- 纵向：9 盒 0.30 em 余量为负（−0.4…−1.5 px）；像素复核（`out/creambox-pixel.log`）全部真墨清除量为正 +4.8…+5.8 px，最紧 P7 LETTERE +0.7 px，裁图目视在盒内——非缺陷（`out/creambox.log`）。
- D1 副标题（proof1 D1 项）：PIL 真墨右缘 1856.5 px，清除量 **+5.5 px**，已修（`out/measure-de.log`）。

### G12 横向 spill 扫 — 0 实溢出（页边）
- 自写 `h-overflow-proof2.py`：1617 文本节点 vs 页边 0/1862。
- PIL 标记 15 处（+0.2…+0.4 px），交付 PDF 200 dpi 像素裁定（`out/pixel-edge.log`、`out/overmargin-gray.log`）：页脚 `Seite N von 8` 各行最右墨迹 SVG 1861.0，在边距内，PIL 标记为度量舍入；P2 `verde` 行末 +0.4 px、P5 Corot 图注 +0.4 px 为亚像素噪声。
- 仅两处实墨越线，见 G13（非缺陷，数值在案）。

### G13 P8 家具行与范文行越线 — 记录，非缺陷
- 家具行 `Jede Antwort hat eine einzeilige Notiz auf Deutsch　✓ = Modelltext-Aufgabe`：PIL 1862.3（+0.3 px），像素最右实墨 1864.3（**+2.4 px**，灰度 104 实墨）。未列缺陷：幅度 1.8 pt、无裁切/重叠、it-en 同型行亦超 +1.8 px（跨版系统性贴边渲染效应）。标注裁图 `out/ann-p8-furniture.png`。
- 范文行 `Testo modello: Domenica 22 novembre metto la sciarpa e`：PIL 1861.5（盒内），像素最右实墨 1863.4（**+1.4 px**）。未列缺陷：冻结意大利文，与 core 逐字节相同，core 同行像素亦 +1.4 px（core 复校 (a) 时即在，core 级固有特征）。标注裁图 `out/ann-p8-modeltext.png`。

### G14 孤儿扫 — PASS（0 孤儿）
- `out/orphan.log`：**0 孤儿**。P3-main 末行 `costruzioni.` 为文章最后一行（core 同文同断行，core y=1202.94，本版 y=1232.67；续栏无正文），非栏断孤儿；余下单字节点为徽章/题号/节标/练习短词等结构项。

### G15 p8 extract — PASS
- 150/150 noted，RC=0（`out/p8-extract.json`、`out/p8-extract.log`）。

### G16 p8 compare vs core — PASS
- 状态 **CLEAN**，missing=[]，extra=0，keydiff = **[137, 138, 139]**（预期：重定向的读者句键；Q140 意语句键，core 与本版相同、无 diff，正确）（`out/p8-compare.json`、`out/p8-compare.log`）。

### G17 text.md validate — PASS
- forward-miss 0 / reverse-miss 0（gates.py textmd 段）。

### G18 150 键复核 — PASS
- 键 1–150 与 core 一致（除 137–139 重定向与写作项）；notes 与 translations.py 一致（除 137–140 + 写作项）；table_gaps=[]。

### G19 日期/星期全验 — PASS
- `TZ=Europe/Rome date -d` 核对文中全部星期表述：11 月 6 日周五、7 日周六、8 日周日、9 日周一、12 日周四、13 日周五、14 日周六、15 日周日、16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二、12 月 2 日周三（TFF 9 天）、12 月 6 日周日、12 月 31 日周四、10 月 15 日周四、10 月 28 日周三——与文中 VEN 6.11 / SAB 7.11 / DOM 8.11 / giovedì 12 / martedì 17 / lunedì 23 / martedì 24 / LUN 16 / MAR 17 / GIO 19 / VEN 20 / SAB 21 / DOM 22 全部一致。LA SETTIMANA 无周三 18 日条目（fix3 已接受 D12）。

### G20 8 页逐版目视 — 2 处可见缺陷（即 D1/D2）
- 交付印 PDF 200 dpi 渲染（`out/pages/p-1.png` … `p-8.png`）逐页目视：除 D1/D2 盒标题溢出外，无溢出、重叠、压页脚、图片与出处问题，无豆腐块。P3/P5 中部结构性留白为 core 固有模式。D1 在 P1 全页图上亦可见；D2 在裁图可见。

## 附加机械核对（非门禁，但已实测）

| 项 | 结果 |
|---|---|
| Q150 范文词数 | 实数 **99 词**（与 KIT/题面一致） |
| 文本 CJK 扫描 | 汉字 **0 个**（无「翻譯」/任何中文残留）；全角冒号 ×14（冻结动词范式注 16–20、60–61）；U+3000 ×106（家具分隔符） |
| ABSTRACT.txt | 一行、德语、无 ASCII 双引号、含 Lucerna / 意大利目标名 / A2–B2 / 150 Übungen |
| 标题数实测 | 「56 titles」是幻数：机械规则（`## `+全大写行）计 **104** 个标题行；清洗后 61 个具名标题（54 全大写 + 7 句首大写头条） |
| fix3 九行核对 | D1（`domenica sera`）、P2 b/d 改写、D11、P4 b/c、P8 F 短式均在位，旧措辞无残留 |
| proof1 D1/D2 | 均已修（见 G11 与 G12） |
| P7 FRASI 8 引文 | 逐字核对原文及页码（P1 ×2、P2、P3、P4、P5、P6 ×2）无误 |
| 数学题 | Q83 Torino 5° 最冷、Q84 Napoli 13° 最热、Q85 13−11=2、Q86 6+7=13 全对 |
| 匹配键 | P2 25–28（c/b/d/a）、P4 52–55（d/b/c/a）、P8 F 141–144（d/c/b/a）全对 |
| 非盒 fill 复核 | #f4efe1（15 处）与 #f6e08e（9 处）皆为深底文字 fill，非盒；奶油盒只有 #f0eee5（29 个），已全扫 |

## 证据文件索引（均在 scratch 内）

- `out/run.log`、`out/rebuilt-svg.sha256`、`out/render.log`、`out/freeze-baseline.log`、`out/freeze-baseline.json`、`out/occlusion.log`、`out/p8-extract.json`、`out/p8-compare.json`、`out/gates.log`、`out/measure-de.log`、`out/h-overflow.log`、`out/pixel-edge.log`、`out/creambox.log`、`out/creambox-pixel.log`、`out/orphan.log`、`out/overmargin-gray.log`
- `out/pages/p-1.png` … `p-8.png`
- `out/ann-p1-cifre-title.png`、`out/ann-p2-frase-title.png`、`out/ann-p8-furniture.png`、`out/ann-p8-modeltext.png`、`out/ann-p2-line.png`、`out/ann-p5-credit.png`、`out/crop-p7-lettere-bottom.png`、`out/crop-p1-cifre.png`、`out/crop-p2-frase.png`
- `h-overflow-proof2.py`、`creambox-proof2.py`、`pixel-edge.py`、`pixel-p8.py`、`gates-proof2.py`、`render-scratch.py`
