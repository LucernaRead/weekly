# EDITION-RECORD — 2026-w47-fr-zh-tw（重建 #2）

读者母语：zh-tw。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['bc9050c8', 'b46154cf', '22af3699', '5af79c73', 'a1981b77', '81a3f8ff', '087855db', '7b8c6116']
- text_layer: PASS — print/web pdftotext byte-equal (101463 B); web 2552871 B < 7MB; print 30551086 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1442
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1405.0, FR sub ends 837.2, band_r2 starts 1571.4

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 2，记录残留 1，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1864.7, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 1997.4, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-zh-tw.pdf`：30,551,086 B，SHA-256 `ccdfc35fb49f41f6ee966f296a0016ccdff6b1d4a865cb79238997c3b42af95b`
- 网页 PDF `La-Lucerna-VOL4-fr-zh-tw-web.pdf`：2,552,871 B，SHA-256 `ac9f148038dcdb103230d78a319a1d206d3f394a3746dabd819d683852603324`
- `.text.md`：45,998 B，SHA-256 `6e348b8c9309d1822a3d6cf4482dee9781ea07157002f0239990b5c61ed73ba9`，39013 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `bc9050c8`, p2 `b46154cf`, p3 `22af3699`, p4 `5af79c73`, p5 `a1981b77`, p6 `81a3f8ff`, p7 `087855db`, p8 `7b8c6116`
- 改动页（vs #1）：P2（7e372c72→b46154cf）、P3（f3280832→22af3699）、P8（86da3308→7b8c6116）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
