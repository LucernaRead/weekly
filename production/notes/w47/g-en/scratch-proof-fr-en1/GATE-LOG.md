# GATE-LOG — W47 fr-en proof1（独立复校门禁日志）

版：`production/2026-w47/2026-w47-fr-en/`。全部由复校员独立重跑；构建者的 gates-run4.json 仅作对照，未作证据。
解释器一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。

## 0. 身份核对（2026-11-11，磁盘实测）

```
La-Lucerna-VOL4-fr-en.pdf       17,418,994 B  e97e9f7b845d42be75ca085f33c61e8ee7518bc57d79c75b586c695b1c42b7cd  ✓
La-Lucerna-VOL4-fr-en-web.pdf    1,663,511 B  2ef460c16cee6c844d0cb4be4a627399c596e0eefe469b014d7ff92dfb8592da  ✓
2026-w47-fr-en.text.md              46,190 B  349e20c97cd8632a0f3ea7e198b0974ab03edb535340f3d2606615a69f7f6db9  ✓
```

## 1. freeze diff

```
tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg \
  --edition-svg production/2026-w47/2026-w47-fr-en/svg --json <proof>/freeze-diff.json
runtime: .../tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3
p1: +25 strings / -23 strings; CJK core 224 -> edition 35; added CJK chars: 0
p2: +38 strings / -33 strings; CJK core 283 -> edition 30; added CJK chars: 0
p3: +35 strings / -44 strings; CJK core 194 -> edition 19; added CJK chars: 0
p4: +44 strings / -50 strings; CJK core 238 -> edition 29; added CJK chars: 0
p5: +39 strings / -42 strings; CJK core 244 -> edition 23; added CJK chars: 0
p6: +30 strings / -30 strings; CJK core 226 -> edition 25; added CJK chars: 1 {'\u3000': 1}
p7: +42 strings / -34 strings; CJK core 411 -> edition 16; added CJK chars: 1 {'\u3000': 1}
p8: +125 strings / -123 strings; CJK core 1220 -> edition 189; added CJK chars: 7 {'\u3000': 7}
TOTAL added CJK characters: 9   (全部为 U+3000 全角空格，无新增汉字)
```

## 2. freeze baseline（scratch 副本内复现构建，生产文件未动）

```
tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-fr-en \
  --core-svg production/2026-w47/2026-w47-fr-en/svg --out <proof>/freeze-baseline \
  --json <proof>/freeze-baseline.json
baseline: 8/8 SVGs byte-identical (repointed files: render.py)
  OK  p1-une.svg core d832422ed8b816a5 produced d832422ed8b816a5
  OK  p2-vie.svg core f200006f762fc65b produced f200006f762fc65b
  OK  p3-culture.svg core 4867f16985720f43 produced 4867f16985720f43
  OK  p4-sport.svg core 14690fdab725be4e produced 14690fdab725be4e
  OK  p5-jeunesse.svg core 8d7d907ba973b98f produced 8d7d907ba973b98f
  OK  p6-politique.svg core 087ab1a571c7f790 produced 087ab1a571c7f790
  OK  p7-langue.svg core 5476d2d0dc244fcd produced 5476d2d0dc244fcd
  OK  p8-exercices.svg core f310354ad24114a0 produced f310354ad24114a0
core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
```

## 3. occlusion / p8（独立重跑）

```
occlusion_audit.py svg/  ->  selftest OK: planted classes fired
  {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
  .../2026-w47-fr-en/svg/: 0 flags
p8.py extract --p8 svg/p8-exercices.svg --total 150 -> noted set = 121 of 150 (parse: joined); keys 150
p8.py compare --core-p8 core-fr/svg/p8-exercices.svg --edition-p8 svg/p8-exercices.svg --total 150
  core 121 noted / edition 121 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[150]
```

## 4. proof_gates.py（复校员自写，逐门重跑；见 proof-gates.json）

```
PASS source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
PASS string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
PASS text_layer: print/web pdftotext byte-equal (105574 B); web 1663511 B < 7MB; print 17418994 B
PASS p8_font: P8 min font 11.625pt >= 9.75pt
PASS scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
PASS chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
PASS keycheck: 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
PASS mcq: bodies: 45  rendered lines: 1481
PASS widths: 31 single-line strings all within budget
PASS band_spans: FR title ends 1236.9, band_r1 starts 1252.1, FR sub ends 837.2, band_r2 starts 1467.1
INFO fonts_audit: {'Noto Sans CJK SC': 692, 'UnifrakturMaguntia': 1, 'Newsreader': 945, 'Noto Serif CJK SC': 74, 'DejaVu Sans': 4}
PROOF GATES 10/10 PASS (plus 2 info-only)
```

## 5. creambox.py 全版扫描（canonical 版，见 creambox-all.log）

```
33 盒；inside-only clearance 全为正，最小 +5.0（P2 ET VOUS 盒，末行 'in.'，desc-clear -1.0 已裁图核实为启发式假阳性）
BELOW-WINDOW 8 处：+24.0 ×1（LE MOT DE LA SEMAINE）、+37.0 ×7（下一栏目标题），均为已知假阳性类
P7-TOOLBOX summary: 4 boxes, min inside clearance +24.7, min desc-clear +18.8
```

## 6. 字体审计（记录用）

```
SVG font-family 计数：Noto Sans CJK SC 692 / Newsreader 945 / Noto Serif CJK SC 74 / DejaVu Sans 4 / UnifrakturMaguntia 1
印刷版 PDF 嵌入字体含多份 NotoSansCJKsc-Regular/Bold (cid) + Newsreader16pt + NotoSerifCJKsc-Regular + UnifrakturMaguntia + DejaVuSans
P2 英文译注实例：font-family="Noto Sans CJK SC" font-size="20" fill="#6f675d"（"Tell us about your 19 November..."）
```

## 7. 150 键交叉核对（独立脚本）

```
p8-proof1.json keys 150  vs  text.md P8 答案区解析 150：仅 Q150 键后多注记后缀，键本身一致；其余 149 键逐字一致
p8-proof1.json keys 150  vs  core final-fr-p8.json：仅 Q150 不同
逐题对照正文/题干：Q1–Q149 无错键；Q48=A 与 P4 正文一致；2026-11-16（一）至 11-22（日）经 date -d 核实
```

## 8. 目视日志

```
印刷版 PDF 150 dpi 全 8 页（png-print/p-1..p-8.png）：逐页目视，零版式缺陷
网页版 PDF 100 dpi P1/P8（png-web/p-1.png、p-8.png）：与印刷版同版式同内容
裁图 300 dpi：crop-p2-etvous.png（ET VOUS 盒底，末行在盒内）；p1-photo-xref7.png（Atget 源图，白方块为源图内容）
```

## 9. 发现的问题汇总

```
D1（缺陷）：P8 Q64 注记 "Les Braves by Dont" → 应为 "Dhont"（expl.py:264 n_photo3；SVG p8 x=538.5 y=2102.96；
  印刷版 P8 span bbox (557.79,1563.73)-(697.02,1580.57)pt 11.625pt；text.md 同文）
O-D5（观察，不判）：讲解层拉丁字符用 Noto Sans CJK SC（692 处），见 PROOF-NOTE.md
```

## 附：文件清单（本复校 scratch 目录）

```
PROBE.txt  PROOF-NOTE.md  GATE-LOG.md  proof_gates.py  proof-gates.json
freeze-diff.json  freeze-baseline.json  freeze-baseline/（复现构建副本）
occlusion-proof1.json  p8-proof1.json  p8compare-proof1.json  mcq-proof1.log
print-proof1.txt  web-proof1.txt  creambox-all.log
png-print/p-1..p-8.png  png-web/p-1..p-8.png
crop-p1-photo.png  crop-p1-photo2.png  crop-p2-etvous.png  p1-photo-xref7.png
```
