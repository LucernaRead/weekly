# GATE-LOG — W47 fr-it proof1

复校：2026-11-11。解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-it1/`。
生产文件只读；determinism 在 goals 侧副本重建。

## 身份核对（磁盘 SHA-256）

- 印 `La-Lucerna-VOL4-fr-it.pdf` 17,415,946 B `79839bafd07e439122c64533a891a4810fa9bc0dc75bf557255211a06ee30b56` ✓
- 网 `La-Lucerna-VOL4-fr-it-web.pdf` 1,696,801 B `223287fef53f2c557ab3a19e2b9e453bfe50bce98ab7363fad052fdc9e5d3eaf` ✓
- `2026-w47-fr-it.text.md` 46,690 B `c75ba7ef0a59fcfc4b17cde8f488e9effd7afb7c66f50b5baf6ff0084400a89d` ✓
- 核心印 30,446,982 B `db3f2a71206f256b9ee0136afd8a2af663e0b3a33df8924c251a064611f135e7` ✓
- 核心网 2,205,749 B `26593a39c258fd721e11548f0ea8f7e8eb3cd47195c3d87003481aaf5fe17823` ✓
- 核心 text.md 46,477 B `2b50c88d6af4c3a9907e61cb71d67d9c9e2bb8992d41fd10bec7d10ca660737e` ✓
- 复校后重验：印/网/text SHA 未变。

## freeze 首检（tools/freeze.py diff）

- 8 页全出；exit 0。见 `freeze-diff.log` / `freeze-diff.json`。
- p1 +25/-23，p2 +37/-33，p3 +35/-44，p4 +45/-50，p5 +39/-42，p6 +29/-30，p7 +42/-34，p8 +124/-123。
- 新增 CJK 仅 U+3000 ×10（p2 1 个、p8 9 个，均在意语分隔串内）；移除串全为中文。

## 15 门独立复跑（proof_gates.py it proof1，exit 0）

见 `gates-proof1.log` / `gates-proof1.json`；mcq 日志 `mcq-proof1.log`；重建日志 `build-proof1-rerun.log`。

```
PASS run: exit 0, zero overflow/wide; TOTAL 150; by level {'A2': 53, 'B1': 75, 'B2': 22}; by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
PASS occlusion: 0 flags, selftest OK
PASS p8_extract: keys 150/150, printed notes 121/150
PASS p8_compare: CLEAN, keydiff [150] (writing key only)
PASS source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
PASS string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 3 strings excused as translated E values
PASS freeze_direct: two builds sha256 8/8 identical: ['aa3ae078', 'f541b51c', '52b4baf0', '249b0d98', '7a7f178e', '76cc6f87', 'd486ba6a', 'e95c7ef1']
PASS text_layer: print/web pdftotext byte-equal (106326 B); web 1696801 B < 7MB; print 17415946 B
PASS p8_font: P8 min font 11.625pt >= 9.75pt
PASS scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
PASS chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
PASS keycheck: 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
PASS mcq: bodies: 45  rendered lines: 1479
PASS widths: 31 single-line strings all within budget
PASS band_spans: FR title ends 1236.9, band_r1 starts 1307.6, FR sub ends 837.2, band_r2 starts 1481.2
GATES 15/15 PASS
```

## creambox（规范版，exit 0）

见 `creambox.log`。33 盒；8 处负 clearance：7 处假阳性（下一栏目标题被 +45 px 窗口捡到，盒内 clearance +47.7/+48.0/+48.5）；1 处真漫出：P7 读者来信盒，末行基线 2260.6 vs 盒底 2258.0（-2.6），PIL 真墨墨底 2265.1，实墨超 7.1 px。

## 目视

- `pg-1.png` … `pg-8.png`（100 dpi，印刷 PDF）；`p1-band-300dpi.png`；`p7-courrier-bottom-300dpi.png`。
- P1–P6、P8 零问题；P7 仅 D1；P5 仅 D2/D3（词表错字）。

## 150 题手验

- text.md 1,088 行全文通读；150 键对核心逐项比对，仅 Q150 不同；注记逐条核对无误；CJK=0。
- 词表类 E 键法语侧系统比对：仅 `mots_photo` 2 处偏离（D2/D3）。

## 字体调查（D5，已知全周待定项，记录）

- 8 SVG：Noto Sans CJK SC 691 / Newsreader 944 / Noto Serif CJK SC 74（皆 U+3000 run）/ UnifrakturMaguntia 1 / DejaVu Sans 4（P7 ✗）。
- 讲解层 sans 拉丁/意语元素一律 Noto Sans CJK SC。

## 结论

(b) 不定稿。缺陷：D1 P7 奶油盒漫出（实墨超 7.1 px）；D2 `una attrice`；D3 `una séance`（后两者在 `expl.py:139` 的 `mots_photo`）。
