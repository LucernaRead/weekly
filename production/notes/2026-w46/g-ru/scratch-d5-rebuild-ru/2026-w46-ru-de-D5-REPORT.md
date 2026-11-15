# D5 report — 2026-w46-ru-de（W46 ru，读者 de · German）

- 构建目录：`patched/2026-w46-ru-de/`；目标语 ru；模式 latin；`_D5_READER` 在 `svglib.py:107` = `latin`；fix2 `_QUOTE_CLS` ×4；ru 内容走旧 `_D5_READER == "ru"` 分支（D26；fix-xru 未引入）；`test_d5_routing.py` FAILURES: 0。
- 基线：run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；text.md 与 `issues/` BYTE-IDENTICAL；印/网 PDF 文字层与已发 PDF 去空白多重集差 0；`issues/` pin（pdfBytes/pdfSha256）与文件一致；p8 extract 150/150。修前普查：D5 Latin in CJK 441、Cyrillic in CJK 0、curly in CJK 0。基线 D18 间隙 152.2px、D37 余量 104.5px。

## run1 门禁（19 verdict）

| 门 | run1 | run2 |
|---|---|---|
| G1 run | PASS | PASS |
| G2 head_check | PASS | PASS |
| G3 d5_census | PASS | PASS |
| G4 render | PASS | PASS |
| G5 webpdf | PASS | PASS |
| G6 occlusion | FAIL | FAIL |
| G7 p8_extract | PASS | PASS |
| G8 p8_compare | PASS | PASS |
| G9 freeze_baseline | PASS | PASS |
| G10 freeze_diff | PASS | PASS |
| G11 spill | PASS | PASS |
| G12 boxtitle | FAIL | PASS |
| G13 edge | PASS | PASS |
| G14 creambox | FAIL | PASS |
| G15a textlayer+text.md | PASS | FAIL |
| G15b carryover (record only) | RECORD | RECORD |
| G15c native_verify | PASS | FAIL |
| G16 quotes | PASS | PASS |
| D18 masthead | PASS | PASS |
| D37 badge | PASS | PASS |

run1：16/19 scored gates PASS；run2：16/19 scored gates PASS。

## 修复（2 处，只降字号）

- `content56.py:135` P6 标题 `ЗА И ПРОТИВ　PRO UND CONTRA`：24→22pt（run1 越界 +25.7px；探针余量 8.1px；D47（已发版第 347 行））。
- `content8.py:115` P8 刊头 `ОТВЕТЫ　LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN`：25→23pt（run1 越界 G6 +82.4px；探针余量 0.6px；D47（已发版第 514 行））。

## 终轮门禁详情（run2）

- G1：TOTAL=150 OVF=0 HDW=0。G2：head_check 0 defects。G3：D5 Latin in CJK 0、Cyrillic 0、curly in CJK 0、curly_total 0、noto_sans 354。
- G6：flags=1，仅剩 P1 斜体 `предзимье` TEXTX 旗标（`ink overlaps '»' by 4.8x9.8px`）——D41 量测 artifact：该行 runs 与基线逐字同位（`«` x=1439.5、`предзимье` x=1450.7、`»` x=1563.7，21.5pt italic，全 11 版同值）；300 dpi 像素实测 `ь` 墨尾 SVG 1554.5、`»` 墨首 1556.4，实隙 1.9 SVG 单位（~5.9px），无真实碰撞；审计器以正体字宽量斜体字致误报。基线同态，D5 零改动此行。由重校复核接受。
- G7：p8 extract 150/150。G8：p8 compare CLEAN，keydiff=[137, 138, 139, 140]（E 节翻译，by design）。G9：freeze baseline 8/8。G10：CJK added 0；Latin added 145（断 run 拆分，仅记录）。G11：SPILL=0。G12：defects=0（titles=56，body_lines=655）。G13：edge 0/0。G14：creambox 0 defects。
- G15a：print=35641 web=35641 issued=35851，print-web raw multiset diff 0；pdfdiff vs 已发：IDENTICAL。 text.md 与已发版差 D47 丢失的 `###` 行（见下），其余逐行相同。
- G15b（仅记录）：SVG-only 534 / MD-only 1998。
- G15c：原生校验器 HOLD（UNEXPECTED 4 块）。 HOLD 原因即 D47 丢失的 `###` 行（每行计 2 块）；除丢失行外 0 差异。
- G16：GRAND TOTAL defective: 0。D18：间隙 119.7px（centre=975.0、date_end=1862.0）。D37：60.9px（y=372.0）。

## D47（builder 只记录，closer 补行）

- ЗА И ПРОТИВ　PRO UND CONTRA（24→22pt，content56.py:135）：导出器 `textexp_ru.py:169` 的 24pt 阈值丢掉其 `###` 行；D47（已发版第 347 行）。标题文字仍在终轮印 PDF 文字层内（fitz 去空白匹配在位）；PDF 文字层与已发版去空白多重集差 0。
- ОТВЕТЫ　LÖSUNGEN — NACH SEITEN GEORDNET; AUFGABENNUMMER SUCHEN（25→23pt，content8.py:115）：导出器 `textexp_ru.py:169` 的 24pt 阈值丢掉其 `###` 行；D47（已发版第 514 行）。标题文字仍在终轮印 PDF 文字层内（fitz 去空白匹配在位）；PDF 文字层与已发版去空白多重集差 0。
closer 补行后 text.md 即已发版值（字节 + SHA 见下已发版行）；补行后针对性重验 G15a/G15c。

## 交付物 pin（run2，builder 原件）

- 印 PDF `Lucerna-VOL3-ru-de.pdf`：14204989 字节，SHA-256 `bb108ea0a3c1299f764e4914eb13c5c36512e3191c8c2518c0a34420d0831731`
- 网 PDF `2026-w46-ru-de.web.pdf`：2324509 字节，SHA-256 `053e4399d047a3af863973d83850c0c77c19367ac97be29b38deb7173e4d4dc1`
- text.md（导出器输出）：54804 字节，SHA-256 `aba0c199d58a216b30817d9c4cb132bf044b1ddc622e03395ae81327974c0548`
- text.md（已发版值，D47 closer 补行后即此值）：54925 字节，SHA-256 `94d20967435353ab83f50917b1d43d097562514c31559e713854500b249e3948`

## 残留项（仅记录）

- G6 P1 斜体旗标：D41 量测 artifact，见上（重校复核）。
- G15a/G15c HOLD：D47，见上（closer 补行 + 针对性重验）。
- G15b 仅记录（D27）。G10 Latin 新增为断 run 拆分，仅记录。
