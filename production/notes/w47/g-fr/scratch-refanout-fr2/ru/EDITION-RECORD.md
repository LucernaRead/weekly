# EDITION-RECORD — 2026-w47-fr-ru（重建 #2）

读者母语：ru。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['45d7ade2', 'e805be98', '8bc49b18', 'c9dc8270', 'b7577f84', '69a1f37e', '04f6feb7', 'a92673d4']
- text_layer: PASS — print/web pdftotext byte-equal (107298 B); web 1760007 B < 7MB; print 17477429 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1477
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1284.4, FR sub ends 837.2, band_r2 starts 1479.3

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 1，记录残留 0，字体分拆同基线 14。
- 孤行填空线：[{'page': 'p3', 'y': 1894.4, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2027.1, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-ru.pdf`：17,477,429 B，SHA-256 `c2976921db3531b69adc9d0a37ab8c5fb59dde8678d6892d6d2a9d72de040229`
- 网页 PDF `La-Lucerna-VOL4-fr-ru-web.pdf`：1,760,007 B，SHA-256 `a6d94e5f0d54f78d5cd822040b17bff37c04a7a6852ad25fce5388dcdca9a15a`
- `.text.md`：50,453 B，SHA-256 `a3449fa7e9d90576241371a33fd8f1c25d17a7c723ceee019de9e29d11ccd8f9`，43121 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `45d7ade2`, p2 `e805be98`, p3 `8bc49b18`, p4 `c9dc8270`, p5 `b7577f84`, p6 `69a1f37e`, p7 `04f6feb7`, p8 `a92673d4`
- 改动页（vs #1）：P7（e825ca39→04f6feb7）、P8（3cdf7e52→a92673d4）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
