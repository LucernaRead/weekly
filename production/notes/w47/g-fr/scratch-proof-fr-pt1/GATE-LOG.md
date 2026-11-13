# GATE-LOG — W47 fr-pt 独立复校 proof1

复校员：独立复校（与构建者不同人）。日期：2026-11-11。
目标：`production/2026-w47/2026-w47-fr-pt/`（run2）。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-pt1/`。
只读生产文件：未改任何生产文件，未 commit、未 push。确定性重建在 scratch 副本 `rerun/` 中进行，生产目录零写入；全部 venv python 运行均加 `PYTHONDONTWRITEBYTECODE=1`。

## 0. 探针与身份核对

- `ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通（`9daeafb9…`）；goals 侧写文件成功（`probe.txt`）后开工。TMPDIR 用 goals 侧 scratch 下 `tmp/`。
- 磁盘 SHA（实测，与任务书一致）：
  - 印刷 PDF `La-Lucerna-VOL4-fr-pt.pdf`：17,420,079 B，`dc64cb43fcf8a87cc6234a10e0912daf5afc4b77e1299cea6a17424989e3f6c3`
  - 网页 PDF `La-Lucerna-VOL4-fr-pt-web.pdf`：1,702,412 B，`1b7eb1cfa8f9f7a94cc5575f937d73a08332a3750c5206f8ee5bb3ebbcd3644b`
  - `2026-w47-fr-pt.text.md`：46,601 B（1,088 行），`45aa52c54faa11ce0d0dfcffb8682aa1198850ce2f5ea62ae0d8efe74cb9c8a6`

## 1. freeze 首检

`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-fr/svg --edition-svg production/2026-w47/2026-w47-fr-pt/svg --json freeze-diff.json`（Pillow 13.0.0 / FreeType 2.14.3）：

- p1: +25 / −23；CJK core 224 → edition 35；新增 CJK 0
- p2: +38 / −33；CJK core 283 → edition 34；新增 CJK 1 {U+3000: 1}
- p3: +36 / −44；CJK core 194 → edition 19；新增 CJK 0
- p4: +45 / −50；CJK core 238 → edition 29；新增 CJK 0
- p5: +41 / −42；CJK core 244 → edition 22；新增 CJK 0
- p6: +30 / −30；CJK core 226 → edition 22；新增 CJK 0
- p7: +42 / −34；CJK core 411 → edition 15；新增 CJK 0
- p8: +123 / −123；CJK core 1220 → edition 192；新增 CJK 10 {U+3000: 10}
- TOTAL 新增 CJK 11，全部为 U+3000（结构分隔符，无 CJK 汉字/假名/韩文）。8/8 页。

## 2. 机械门禁（独立重跑，15/15 PASS）

`gates-proof.py`（`gates.py` 的副本；输出改到本 scratch；第 7 门确定性重跑改在 scratch 副本 `rerun/` 中做）`pt proof1`，exit 0，`GATES 15/15 PASS`（`gates-proof1.json`）：

| 门 | 结果 |
|---|---|
| run | PASS — exit 0，零 overflow/wide；TOTAL 150；by level A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| occlusion | PASS — 0 flags，selftest OK（`occlusion-proof1.json`） |
| p8_extract | PASS — keys 150/150，printed notes 121/150（`p8-proof1.json`） |
| p8_compare | PASS — CLEAN，keydiff [150]（仅写作题键）（`p8compare-proof1.json`） |
| source_freeze | PASS — content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | PASS — 核心非 CJK 串逐页存活；0 核心 E 残留；0 未入账 CJK；1 条翻译豁免（核心 `stem_e1` 前缀 `Traduisez : `） |
| freeze_direct | PASS — scratch 副本重跑，8/8 SVG SHA 全同：`a8ca67ea, 1c7f056e, 13a8fe0a, d9b6af38, 2a66a9f0, 5ef9766c, ea3d710b, 7d582103`（与 builder run2 哈希逐位相同；另一次独立重建亦 8/8，见 `build-proof1.log`） |
| text_layer | PASS — 印/网 pdftotext 逐字节一致（104,850 B）；网 1,702,412 B < 7MB；印 17,420,079 B（`print-proof1.txt`、`web-proof1.txt` 逐字节等长同内容） |
| p8_font | PASS — P8 最小字号 11.625pt ≥ 9.75pt |
| scans | PASS — U+2019=0，U+00B7=0，gold=0，旧纸色=0，#fbfaf6 ×8 |
| chips | PASS — 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck | PASS — 150 键对核心 `final-fr-p8.json`，仅 Q150 不同（`keytable-proof1.txt` 逐题列表） |
| mcq | PASS — bodies: 45，rendered lines: 1483，0 缺陷（`mcq-proof1.log`） |
| widths | PASS — 31 条单行串全部在预算内 |
| band_spans | PASS — 法文标题止 1236.9，band_r1 起 1270.9，法文副标题止 837.2，band_r2 起 1489.2 |

## 3. creambox（规范版，8 页）

`hidden_files/w47/tools/creambox.py` 扫 8 个 SVG（`creambox.log`），核心版对照扫 `creambox-core.log`。

- 8 条 BELOW-WINDOW：7 条假阳性（下一栏目/框标题，盒内末行 clearance +47.7 ~ +48.5；与核心版同值 −24.0 / −37.0）；1 条真溢出：P7 y=1878 盒 `envios reais.` +2.6 = 缺陷 D-1（见 PROOF-NOTE）。
- P7 盒对照：pt 盒内末行 2233.3（+24.7 / desc +18.8）；核心版同盒亦 2233.3（+24.7 / desc +18.8），干净。
- P2 `ET VOUS ?` 盒：pt 末行 1304.2（+4.4 / desc −1.6）；核心版同盒 1275.8（+3.8 / desc −2.2，更紧）——核心继承，不列缺陷。
- P1 agenda 盒：pt 末行 1248.0（+8.0 / desc +2.3），与核心版逐值相同。

## 4. D-1 PIL 真墨测量（250 dpi，`png/crop-p7-mailbox.png`）

- 裁切：印刷版 PDF P7，clip (740, 1390, 1430, 1750) pt，250 dpi。
- 校准：垂直扫描 x=1000pt：svg 2258 仍奶油色 (239,237,228)，svg 2259 起纸白 (251,249,246)；奶油末行 svg 2257.7 ≈ 盒底 2258.0。
- 墨行：`envios reais.` 注记灰字 (110,103,93) 墨行 svg 2258–2260.8，盒底之下满色墨行 svg 2259.2 / 2259.6 / 2260.0；末行字脚约 2.5–2.8 svg 单位（≈1.9pt ≈ 0.67mm）落于盒外白底。
- PDF span 佐证：奶油矩形底 pt 1693.5；`envios reais.` span bbox 底 pt 1699.66（+6.16pt，含字体下行量）；基线 pt 1695.45，比盒底低 1.95pt。核心版同盒末 span bbox 底 pt 1679.2，盒内余 14.3pt。
- 目视：`png/crop-p7-mailbox.png` 可见奶油边线横切 `envios reais.` 字脚下部；网页版 `png/web-p7.png` 同盒同位。

## 5. 目视

- 印刷版 PDF 100 dpi 全页 `png/p1.png`–`png/p8.png`：除 D-1 外零问题（见 PROOF-NOTE §5）。
- 裁图：`png/crop-p7-mailbox.png`（D-1）、`png/crop-p2-box.png`（P2 盒，无漫出感）、`png/crop-p1-agenda.png`（P1 agenda 盒，干净）。
- 网页版抽查：`png/web-p1.png`、`png/web-p7.png`，与印刷版同版式，D-1 同位。

## 6. 150 题手验与文本核查（摘要；详见 PROOF-NOTE §6）

- 独立抽取 p8 键 150/150，与核心逐键比对仅 Q150 不同（`Pergunta aberta`）；`keytable-proof1.txt` 逐题列表。
- `.text.md` 全文 1,088 行通读：CJK 0、U+2019=0、U+00B7=0、"Dont" 0、"Dhont" 4；人名逐一核对法文正文无误。
- Q83=C 三重核对（核心键 C、P8 印出、日历 9 déc.）；Q148 见 R1（核心继承）；MODÈLE 96 词（80–100）；P7 八句金句 8/8 逐字出自 P1–P6 正文。
- ABSTRACT.txt：一行葡萄牙语，233 B，内容准确。
- D5 字体普查：SVG 8 页 Newsreader 947 / Noto Sans CJK SC 692 / Noto Serif CJK SC 74 / DejaVu Sans 4 / UnifrakturMaguntia 1；CJK 字体段中纯拉丁文 498 段；网页版 PDF span：葡语讲解层 LucernaNotoSansCJKSC-Reg/Bol，法文正文 Newsreader（见 PROOF-NOTE R2，仅记录）。

## 7. 结论

**(b) 有缺陷，不定稿**——缺陷 1 项：D-1（P7 读者园地奶油盒，葡语注记末行漫出盒底 2.6 svg 单位）。另记录 R1（Q148 核心继承错法语，需 core 轨道修）、R2（D5 字体，全周级待定项），均不计入本版 (b) 判定。
