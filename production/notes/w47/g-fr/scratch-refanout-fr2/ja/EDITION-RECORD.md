# EDITION-RECORD — 2026-w47-fr-ja（重建 #2）

读者母语：ja。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['0111ee1c', 'db490888', '83ad866a', '2b64f954', 'cae84c75', '11f2a3c3', '7a37897c', 'bf40c3c0']
- text_layer: PASS — print/web pdftotext byte-equal (102405 B); web 2309603 B < 7MB; print 30565630 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1451
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1380.0, FR sub ends 837.2, band_r2 starts 1430.1

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 1，记录残留 0，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1864.7, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 1997.4, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-ja.pdf`：30,565,630 B，SHA-256 `291a514f7980e4a30e0f736d22f3c89c720996f96d83770206d92343e6096f63`
- 网页 PDF `La-Lucerna-VOL4-fr-ja-web.pdf`：2,309,603 B，SHA-256 `031684fd076ba8e1b3c64ae4f3df17330e10d838650ca2577cd110bc04ab44d3`
- `.text.md`：47,532 B，SHA-256 `aca654257d25d33d331db2c201724d287e050bdcb288c84057b74c8ef8461498`，39581 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `0111ee1c`, p2 `db490888`, p3 `83ad866a`, p4 `2b64f954`, p5 `cae84c75`, p6 `11f2a3c3`, p7 `7a37897c`, p8 `bf40c3c0`
- 改动页（vs #1）：P1（8bf58ae5→0111ee1c）、P4（8252ca19→2b64f954）、P6（7fdd8932→11f2a3c3）、P8（66b5fa78→bf40c3c0）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
