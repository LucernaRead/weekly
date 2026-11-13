# EDITION-RECORD — 2026-w47-fr-nl（重建 #2）

读者母语：nl。核心：`2026-w47-fr-zh-cn` fix4。重建 run1（r2run1，2026-11-11）。

## 门禁（r2run1，15/15 PASS）
- run: PASS — exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
- occlusion: PASS — 0 flags, selftest OK
- p8_extract: PASS — keys 150/150, printed notes 121/150
- p8_compare: PASS — CLEAN, keydiff [150] (writing key only)
- source_freeze: PASS — content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
- string_freeze: PASS — all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
- freeze_direct: PASS — two builds sha256 8/8 identical: ['984a2867', '1f619509', '4ef160c4', 'c9b59871', 'f2342e2a', 'ce2141d5', '4eb69452', '467885cd']
- text_layer: PASS — print/web pdftotext byte-equal (105229 B); web 1699714 B < 7MB; print 17418792 B
- p8_font: PASS — P8 min font 11.625pt >= 9.75pt
- scans: PASS — U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
- chips: PASS — 134 total [10, 12, 18, 15, 14, 15, 12, 38]
- keycheck: PASS — 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
- mcq: PASS — bodies: 45  rendered lines: 1480
- widths: PASS — 31 single-line strings all within budget
- band_spans: PASS — FR title ends 1236.9, band_r1 starts 1329.4, FR sub ends 837.2, band_r2 starts 1457.5

## 额外核查（check_extra.py）
- 孤儿标点：新增 0，核心继承 0，记录残留 0，字体分拆同基线 0。
- 孤行填空线：[{'page': 'p3', 'y': 1924.1, 'x': 538.5, 'text': '___'}, {'page': 'p3', 'y': 2056.8, 'x': 538.5, 'text': '___'}, {'page': 'p8', 'y': 843.0, 'x': 989.0, 'text': '___'}]（与核心同位关系见 FANOUT-REPORT-fr2.md）。
- Q148：stem_ok=True，key_in_content8=True，extracted='devant le'。

## 产物
- 印刷 PDF `La-Lucerna-VOL4-fr-nl.pdf`：17,418,792 B，SHA-256 `3b0073cc94bcfb42d9a0ecdd5cd9bbc2b3d7b5846d2f62e82db5be4c9b6957ee`
- 网页 PDF `La-Lucerna-VOL4-fr-nl-web.pdf`：1,699,714 B，SHA-256 `5217c87ac893a6b0bd89a7066d1c28acf0ff1aa780c4522114fa5360309b18b7`
- `.text.md`：46,265 B，SHA-256 `d83b5831b235a7b8a9efad5343d996fc85c70d16400eed7250beb4eb4bb5ee28`，44186 字符，542 条目，150 题
- 8 SVG（SHA 前 8 位）：p1 `984a2867`, p2 `1f619509`, p3 `4ef160c4`, p4 `c9b59871`, p5 `f2342e2a`, p6 `ce2141d5`, p7 `4eb69452`, p8 `467885cd`
- 改动页（vs #1）：P7（037b5c49→4eb69452）、P8（6a9750ef→467885cd）
- `ABSTRACT.txt`：自 #1 版原样恢复（内容不受 fix4 影响）。
