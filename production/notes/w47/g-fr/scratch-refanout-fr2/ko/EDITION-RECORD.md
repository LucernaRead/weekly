# EDITION-RECORD — 2026-w47-fr-ko（重建 #2）

读者母语：ko。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['4e1d1ac2', 'c172ea06', '591b514a', '5cf88f14', '946a7778', '77321a37', 'b1769f84', 'fc7999be']
- text_layer: PASS — print/web pdftotext byte-equal (102735 B); web 2048869 B < 7MB; print 23103425 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1449
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1436.9, FR sub ends 837.2, band_r2 starts 1563.3

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 2，记录残留 0，字体分拆同基线 13。
- 孤行填空线：[{'page': 'p3', 'y': 1864.7, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 1997.4, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-ko.pdf`：23,103,425 B，SHA-256 `a315cced01b3725d57e17ca5b57015372b4bf2555392033cae618dd38faf3c82`
- 网页 PDF `La-Lucerna-VOL4-fr-ko-web.pdf`：2,048,869 B，SHA-256 `0862b544eb337d4061cf762a9f40932ae40fc5d0107cfd9bac2bb31e4349ebd5`
- `.text.md`：47,323 B，SHA-256 `f5474d61eeadf9fdb2fe6a5fb3e2e15ff9088201aa8989e986ed064f46ba5c37`，40026 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `4e1d1ac2`, p2 `c172ea06`, p3 `591b514a`, p4 `5cf88f14`, p5 `946a7778`, p6 `77321a37`, p7 `b1769f84`, p8 `fc7999be`
- 改动页（vs #1）：P8（b533645f→fc7999be）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
