# GATE-LOG — W47 fr-es proof1 独立门禁重跑日志

复校：2026-11-11，proof1。解释器一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
`gates-proof.py` 为 builder `gates.py` 的副本，仅改输出目录到本 scratch，第 7 门在 scratch 副本 `rerun/` 中重跑（生产目录零写入）。

## 0. 探针与身份核对

```
$ ls /dev/null -> No such file or directory
$ touch /dev/null; echo test | git -C ~/workspace/weekly-git hash-object -w --stdin
9daeafb9864cf43055ae93beb0afd6c7d144bfa4
$ echo probe-ok > .../hidden_files/w47/probe-fr-es1.txt   (成功后已删除)
$ sha256sum La-Lucerna-VOL4-fr-es.pdf La-Lucerna-VOL4-fr-es-web.pdf 2026-w47-fr-es.text.md
eb2a01432212e59f5b56cba88e437b4ac2c80b16a54d36b0a85d265b0496d806  La-Lucerna-VOL4-fr-es.pdf
1756ddfe5f1927122610661dfd50ed874e3fd4672a2d8e4549285d13482f323f  La-Lucerna-VOL4-fr-es-web.pdf
87bc611d595420d535418ceb0ef7118924e9876fed28e9732af584aaa4bb2635  2026-w47-fr-es.text.md
17,418,404 B / 1,699,232 B / 46,721 B —— 与任务书逐值一致，先核对再开工。
```

## 1. freeze diff（首检）

```
$ tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg \
    --edition-svg production/2026-w47/2026-w47-fr-es/svg --json .../freeze-diff.json
runtime: .../tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3
p1: +25 strings / -23 strings; CJK core 224 -> edition 35; added CJK chars: 0
p2: +38 strings / -33 strings; CJK core 283 -> edition 28; added CJK chars: 0
p3: +35 strings / -44 strings; CJK core 194 -> edition 20; added CJK chars: 1 {'\u3000': 1}
p4: +45 strings / -50 strings; CJK core 238 -> edition 27; added CJK chars: 0
p5: +37 strings / -42 strings; CJK core 244 -> edition 22; added CJK chars: 0
p6: +29 strings / -30 strings; CJK core 226 -> edition 25; added CJK chars: 1 {'\u3000': 1}
p7: +43 strings / -34 strings; CJK core 411 -> edition 15; added CJK chars: 0
p8: +124 strings / -122 strings; CJK core 1220 -> edition 190; added CJK chars: 8 {'\u3000': 8}
TOTAL added CJK characters: 10
```

新增 CJK 全部为 U+3000 全角空格（两段式导读条分隔符，本家庭通用结构）；无新增汉字/假名/韩文。
逐页 U+3000 计数（edition vs core，SVG 全文）：p1 35/35、p2 28/33、p3 20/19、p4 27/29、p5 22/23、p6 25/24、p7 15/15、p8 190/182——净增 10，与 freeze diff 一致。

## 2. gates 15/15（独立重跑，exit 0）

```
$ tools/venv/bin/python gates-proof.py es proof1
PASS run: exit 0, zero overflow/wide; TOTAL 150
by level {'A2': 53, 'B1': 75, 'B2': 22}
by page {1: 10, 2: 15, 3: 18, 4: 18, 5: 17, 6: 18, 7: 12, 8: 42}
PASS occlusion: 0 flags, selftest OK
PASS p8_extract: keys 150/150, printed notes 121/150
PASS p8_compare: CLEAN, keydiff [150] (writing key only)
PASS source_freeze: content/bslib/svglib/run byte-identical to core; render.py differs only in BASE+PDF name
PASS string_freeze: all non-CJK core strings survive per page; 0 core-E survivors; 0 unaccounted CJK chars; 1 strings excused as translated E values
PASS freeze_direct: two builds sha256 8/8 identical: ['bd6a40f0', '220dd45e', '1b39fa5b', 'dd5ec45e', '51b18d6f', 'c3f18dcd', 'c7fc6d9e', '20df945f']
PASS text_layer: print/web pdftotext byte-equal (105094 B); web 1699232 B < 7MB; print 17418404 B
PASS p8_font: P8 min font 11.625pt >= 9.75pt
PASS scans: U+2019=0, U+00B7=0, gold=0, old paper=0, #fbfaf6 x8
PASS chips: 134 total [10, 12, 18, 15, 14, 15, 12, 38]
PASS keycheck: 150 keys vs core: only Q150 differs (writing key) — 150 core keys, 150 extracted
PASS mcq: bodies: 45  rendered lines: 1480
PASS widths: 31 single-line strings all within budget
PASS band_spans: FR title ends 1236.9, band_r1 starts 1299.7, FR sub ends 837.2, band_r2 starts 1450.1
GATES 15/15 PASS
```

注：门 1 读的是 builder 的 `build-run2.log` 副本（`build-proof1.log`，证据链）；门 7 的两次构建一次在生产 SVG（哈希取样，只读），一次在 scratch 副本 `rerun/` 中完整重跑，8/8 SHA 与 builder run2 逐位相同，生产目录未写入。完整 JSON：`gates-proof1.json`。

## 3. creambox（规范版，8 页）

```
$ tools/venv/bin/python .../hidden_files/w47/tools/creambox.py .../2026-w47-fr-es/svg/*.svg > creambox.log
```

8 条 BELOW-WINDOW（详见 PROOF-NOTE §4）：7 条为下一栏目标题假阳性；1 条真溢出——P7 邮箱盒 `envíos reales.`（盒底 2258.0，末行基线 2260.6，+2.6）。
核心版同盒对照（`creambox-core.log`）：P7 盒末基线 2233.3，盒内余 +24.7，干净；P2 ET VOUS 盒核心版 desc-clear −2.2（比本版 −1.6 更紧），属核心继承。

P7 溢出 PIL 真墨测量（印刷版 PDF，250 dpi，`png/crop3-p7-mailbox.png`；y_pt = 0.75 × y_svg，3 个盒子验明）：

```
奶油矩形底 pt 1693.5；'envíos reales.' span bbox [759.8, 1678.5, 852.6, 1699.7]，基线 pt 1695.45（盒底下 1.95pt）
奶油末行（该行 x 范围）：svg 2257.5（= 盒底 2258.0）
'envíos reales.' 深色墨行：svg 2254–2260；盒底之下满色墨行 svg 2258/2259/2260（(110,103,93)）
深绿带起于 svg 2270.0，墨行 2261–2269 为零（白间隔），故 2258–2260 的墨确为该行字脚，非页脚带
P2 ET VOUS 盒对照：奶油矩形底 pt 981.4；末行 span bbox 底 pt 982.5（+1.1pt）；核心版同盒 +1.5pt
P1 agenda 盒对照：与核心版逐值相同（desc-clear +2.3）
```

## 4. 字体实测（D5，网页版 PDF span）

```
web p1 fonts: LucernaUnifrakturMaguntia, LucernaNotoSansCJKSC-Reg/Bold,
              LucernaNewsreader-Reg/Bold
'Votación del Senado: el miércoles.' -> LucernaNotoSansCJKSC-Reg 14.25pt
'Cuenta tu 19 de noviembre: escribe dos' -> LucernaNotoSansCJKSC-Reg 15.0pt
'envíos reales.' -> LucernaNotoSansCJKSC-Reg 14.62pt
'EXPLICACIONES EN ESPAÑOL' -> LucernaNotoSansCJKSC-Reg 12.75pt
'ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI' -> LucernaNotoSansCJKSC-Bold 34.5pt
'Dimanche 8 novembre, Carlos Alcaraz' -> LucernaNewsreader-Regular 18.0pt
'Le Lucerna' masthead -> LucernaUnifrakturMaguntia-Regular 147.0pt
```

讲解层拉丁字符全部落在 Noto Sans CJK SC（SOP §1.1 违规，全周级待定项，记录在案，不据此判 (b)，不擅自修）。

## 5. 150 键独立抽取与文本扫描

```
p8.py extract --total 150 -> keys 150/150, notes 121/150 (p8-proof1.json)
keycheck: 150 键对 core-fr/final-fr-p8.json，仅 Q150 不同（开放题 -> Pregunta abierta）
Q83 三重核对：core final-fr-p8.json = 'C'；本版抽取 = 'C'；
  P8 SVG 印出 '83. C (Votación solemne el 9 de dic.)'；核心 text.md '83. C（正式投票 12 月 9 日）'——一致
text.md 扫描：CJK 字符 0；U+2019=0；U+00B7=0；U+3000=387（版内分隔符）
MODÈLE 96 词（80–100 要求内）；P7 八句金句 8/8 逐字出自 P1–P6 正文
```

## 6. 目视记录

- 印刷版 PDF 100 dpi 全页：`png/p1.png`–`png/p8.png`（P1–P6、P8 干净；P7 除 D-1 外干净）
- 250 dpi 裁图：`png/crop3-p7-mailbox.png`（D-1 证据）、`png/crop3-p2-box.png`、`png/crop3-p1-agenda.png`
- 早期废裁图（y 比例错误，已不用作证据）：`png/crop-p7-mailbox.png`、`png/crop-p2-box.png`、`png/crop-p1-agenda.png`、`png/crop-p1-band.png`、`png/crop2-*.png`
