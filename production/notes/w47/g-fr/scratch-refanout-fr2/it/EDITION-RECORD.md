# EDITION-RECORD — 2026-w47-fr-it（重建 #2）

读者母语：it。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['aa3ae078', 'f541b51c', '52b4baf0', '249b0d98', 'a91995f1', '76cc6f87', '12eb2907', '64d1ba48']
- text_layer: PASS — print/web pdftotext byte-equal (106161 B); web 1696726 B < 7MB; print 17415873 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1478
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1307.6, FR sub ends 837.2, band_r2 starts 1481.2

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 0，记录残留 0，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1894.4, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2027.1, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-it.pdf`：17,415,873 B，SHA-256 `2a47495b00bda39a108420b1986bf214946220952b6f9c8b4bd47e842e5632f6`
- 网页 PDF `La-Lucerna-VOL4-fr-it-web.pdf`：1,696,726 B，SHA-256 `8957acb69bb9342957c0c20a2f61412f0386beb721cdb076fbfa493bcd58b3ab`
- `.text.md`：46,617 B，SHA-256 `fac32b0bbf28a1b1a7a7365620de5348501fa49b7295816414522bd85ca25919`，44488 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `aa3ae078`, p2 `f541b51c`, p3 `52b4baf0`, p4 `249b0d98`, p5 `a91995f1`, p6 `76cc6f87`, p7 `12eb2907`, p8 `64d1ba48`
- 改动页（vs #1）：P5（7a7f178e→a91995f1）、P7（d486ba6a→12eb2907）、P8（e95c7ef1→64d1ba48）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
