# EDITION-RECORD — 2026-w47-fr-pt（重建 #2）

读者母语：pt。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['a8ca67ea', '1c7f056e', '13a8fe0a', 'd9b6af38', '2a66a9f0', '5ef9766c', 'c3419d55', '34bf3311']
- text_layer: PASS — print/web pdftotext byte-equal (104688 B); web 1702371 B < 7MB; print 17420030 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1482
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1270.9, FR sub ends 837.2, band_r2 starts 1489.2

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 0，记录残留 0，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1924.1, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2056.8, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-pt.pdf`：17,420,030 B，SHA-256 `420d79e71cc02859a5d9c8fa94c1b09ea7ae4f786c22911a4d8d2a3e7ed95521`
- 网页 PDF `La-Lucerna-VOL4-fr-pt-web.pdf`：1,702,371 B，SHA-256 `fb88ae09d19a9b66906df2865ec15529c9f09429de22e690fbcc252ac5eff6b1`
- `.text.md`：46,536 B，SHA-256 `172f28dc192ea023b64bffb3e84f8a7106b4ff46f9db11a6a5d08d0f6b9efbdd`，44240 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `a8ca67ea`, p2 `1c7f056e`, p3 `13a8fe0a`, p4 `d9b6af38`, p5 `2a66a9f0`, p6 `5ef9766c`, p7 `c3419d55`, p8 `34bf3311`
- 改动页（vs #1）：P7（ea3d710b→c3419d55）、P8（7d582103→34bf3311）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
