# EDITION-RECORD — 2026-w47-fr-es（重建 #2）

读者母语：es。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['bd6a40f0', '220dd45e', '1b39fa5b', 'dd5ec45e', '51b18d6f', 'c3f18dcd', '75d2252b', 'aa084df5']
- text_layer: PASS — print/web pdftotext byte-equal (104934 B); web 1701681 B < 7MB; print 17418347 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1479
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1299.7, FR sub ends 837.2, band_r2 starts 1450.1

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 0，记录残留 0，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1924.1, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2056.8, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-es.pdf`：17,418,347 B，SHA-256 `77488ab05a39b269b38f16ebb0da59e500d1c9b8739e77a3ca3a9387712104f4`
- 网页 PDF `La-Lucerna-VOL4-fr-es-web.pdf`：1,701,681 B，SHA-256 `2e56003e9353fb3de400b27d9e6700e5ad834007e6be07b0dbe758442efbf0b3`
- `.text.md`：46,660 B，SHA-256 `096402b410eccd1f3d0cbcdd5cc786ec82815c967eaa0312157cd7b9b49a1d7f`，44426 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `bd6a40f0`, p2 `220dd45e`, p3 `1b39fa5b`, p4 `dd5ec45e`, p5 `51b18d6f`, p6 `c3f18dcd`, p7 `75d2252b`, p8 `aa084df5`
- 改动页（vs #1）：P7（c7fc6d9e→75d2252b）、P8（20df945f→aa084df5）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
