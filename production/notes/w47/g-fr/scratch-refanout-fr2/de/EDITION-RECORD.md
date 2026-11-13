# EDITION-RECORD — 2026-w47-fr-de（重建 #2）

读者母语：de。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['35c72f4e', '38a1a6fc', '93a010c3', 'cd216538', '32c60e8a', '083360a7', '700bee74', '660522e4']
- text_layer: PASS — print/web pdftotext byte-equal (104632 B); web 1706936 B < 7MB; print 17424223 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1485
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1337.5, FR sub ends 837.2, band_r2 starts 1417.5

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 0，记录残留 0，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1894.4, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2027.1, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-de.pdf`：17,424,223 B，SHA-256 `77842fe4dc5d162adc7f2b8694ad92e985fe83a1fcd9a49c2c3e3ae2886d8e7b`
- 网页 PDF `La-Lucerna-VOL4-fr-de-web.pdf`：1,706,936 B，SHA-256 `df62f6ee61ae8cc6cd57c837a4a2da74187f855b0d71d2c5a07751ebfb9fdf37`
- `.text.md`：46,632 B，SHA-256 `d3735ef592bc02fcbe9712c3a184c2c2c963fd3fcfaf3311363ccf2baf95bc18`，44478 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `35c72f4e`, p2 `38a1a6fc`, p3 `93a010c3`, p4 `cd216538`, p5 `32c60e8a`, p6 `083360a7`, p7 `700bee74`, p8 `660522e4`
- 改动页（vs #1）：P7（4bc0ef75→700bee74）、P8（7e3269a2→660522e4）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
