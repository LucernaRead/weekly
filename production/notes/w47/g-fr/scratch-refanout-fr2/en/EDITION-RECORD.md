# EDITION-RECORD — 2026-w47-fr-en（重建 #2）

读者母语：en。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['d832422e', 'f200006f', '4867f169', '14690fda', '8d7d907b', '087ab1a5', '5476d2d0', 'e027cc89']
- text_layer: PASS — print/web pdftotext byte-equal (105574 B); web 1700436 B < 7MB; print 17418996 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1481
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1252.1, FR sub ends 837.2, band_r2 starts 1467.1

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 0，记录残留 0，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1924.1, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2056.8, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-en.pdf`：17,418,996 B，SHA-256 `7210b3e23c97ef4f683bf695ecc7484bc97fda5cf522abb94fb16ce17f675414`
- 网页 PDF `La-Lucerna-VOL4-fr-en-web.pdf`：1,700,436 B，SHA-256 `ca7f8ae3a76fdbb70f8af1724f92bdb6269f8bbc48b41348457e3d6ddbf551a2`
- `.text.md`：46,191 B，SHA-256 `7b658ae24f265d145455798c39f158d504b39e8034022a06b1c809c8bd7a5c4c`，44136 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `d832422e`, p2 `f200006f`, p3 `4867f169`, p4 `14690fda`, p5 `8d7d907b`, p6 `087ab1a5`, p7 `5476d2d0`, p8 `e027cc89`
- 改动页（vs #1）：P8（f310354a→e027cc89）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
