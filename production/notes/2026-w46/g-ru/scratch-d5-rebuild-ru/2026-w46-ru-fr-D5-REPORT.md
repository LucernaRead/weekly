# D5 report — 2026-w46-ru-fr（W46 ru，读者 fr · French）

- 构建目录：`patched/2026-w46-ru-fr/`；目标语 ru；模式 latin；`_D5_READER` 在 `svglib.py:107` = `latin`；fix2 `_QUOTE_CLS` ×4；ru 内容走旧 `_D5_READER == "ru"` 分支（D26；fix-xru 未引入）；`test_d5_routing.py` FAILURES: 0。
- 基线：run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；text.md 与 `issues/` BYTE-IDENTICAL；印/网 PDF 文字层与已发 PDF 去空白多重集差 0；`issues/` pin（pdfBytes/pdfSha256）与文件一致；p8 extract 150/150。修前普查：D5 Latin in CJK 434、Cyrillic in CJK 0、curly in CJK 24。基线 D18 间隙 149.8px、D37 余量 84.7px。

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

## 修复（4 处，只降字号）

- `content12.py:47` P1 数字盒标题 `НЕДЕЛЯ В ЦИФРАХ　EN CHIFFRES`（f.box `], tsize=`）：23（默认）→22.5pt（run1 越界 +6.2px；探针余量 0.5px；—）。
- `content12.py:85` P1 目录盒 `В ЭТОМ НОМЕРЕ　AU SOMMAIRE`：24→22.5pt（run1 越界 +18.2px；探针余量 6.0px；D47（已发版第 48 行））。
- `content56.py:135` P6 标题 `ЗА И ПРОТИВ　POUR ET CONTRE`：24→22.5pt（run1 越界 +18.7px；探针余量 6.0px；D47（已发版第 347 行））。
- `content7.py:80` P7 标题 `СЛОВО　LE MOT DE LA SEMAINE`：23→22pt（run1 越界 +8.4px；探针余量 7.5px；—）。

## 终轮门禁详情（run2）

- G1：TOTAL=150 OVF=0 HDW=0。G2：head_check 0 defects。G3：D5 Latin in CJK 0、Cyrillic 0、curly in CJK 0、curly_total 39、noto_sans 354。
- G6：flags=1，仅剩 P1 斜体 `предзимье` TEXTX 旗标（`ink overlaps '»' by 4.8x9.8px`）——D41 量测 artifact：该行 runs 与基线逐字同位（`«` x=1439.5、`предзимье` x=1450.7、`»` x=1563.7，21.5pt italic，全 11 版同值）；300 dpi 像素实测 `ь` 墨尾 SVG 1554.5、`»` 墨首 1556.4，实隙 1.9 SVG 单位（~5.9px），无真实碰撞；审计器以正体字宽量斜体字致误报。基线同态，D5 零改动此行。由重校复核接受。
- G7：p8 extract 150/150。G8：p8 compare CLEAN，keydiff=[137, 138, 139, 140]（E 节翻译，by design）。G9：freeze baseline 8/8。G10：CJK added 0；Latin added 155（断 run 拆分，仅记录）。G11：SPILL=0。G12：defects=0（titles=56，body_lines=654）。G13：edge 0/0。G14：creambox 0 defects。
- G15a：print=35577 web=35577 issued=35787，print-web raw multiset diff 0；pdfdiff vs 已发：IDENTICAL。 text.md 与已发版差 D47 丢失的 `###` 行（见下），其余逐行相同。
- G15b（仅记录）：SVG-only 555 / MD-only 2210。
- G15c：原生校验器 HOLD（UNEXPECTED 4 块）。 HOLD 原因即 D47 丢失的 `###` 行（每行计 2 块）；除丢失行外 0 差异。
- G16：GRAND TOTAL defective: 0。D18：间隙 116.4px（centre=975.0、date_end=1862.0）。D37：47.0px（y=372.0）。

## D47（builder 只记录，closer 补行）

- В ЭТОМ НОМЕРЕ　AU SOMMAIRE（24→22.5pt，content12.py:85）：导出器 `textexp_ru.py:169` 的 24pt 阈值丢掉其 `###` 行；D47（已发版第 48 行）。标题文字仍在终轮印 PDF 文字层内（fitz 去空白匹配在位）；PDF 文字层与已发版去空白多重集差 0。
- ЗА И ПРОТИВ　POUR ET CONTRE（24→22.5pt，content56.py:135）：导出器 `textexp_ru.py:169` 的 24pt 阈值丢掉其 `###` 行；D47（已发版第 347 行）。标题文字仍在终轮印 PDF 文字层内（fitz 去空白匹配在位）；PDF 文字层与已发版去空白多重集差 0。
closer 补行后 text.md 即已发版值（字节 + SHA 见下已发版行）；补行后针对性重验 G15a/G15c。

## 交付物 pin（run2，builder 原件）

- 印 PDF `Lucerna-VOL3-ru-fr.pdf`：14204483 字节，SHA-256 `b022a7d76f75ebcd47d2879719e0050cd5b734fdf0fb1610b71a8de0db9f8574`
- 网 PDF `2026-w46-ru-fr.web.pdf`：2323995 字节，SHA-256 `7bf46bbf38fdb35489e25660ce0048cecb45fa15ba88f2315741476006ca9a1c`
- text.md（导出器输出）：54851 字节，SHA-256 `7ce2934c373579d210e996f7dab3bd3ecba950c017f4dda4488a987f94b69d25`
- text.md（已发版值，D47 closer 补行后即此值）：54938 字节，SHA-256 `fa89a406d2bf3f1e414bc4ce320e8b572797aeb2d64759e8a885f9c4128eea56`

## 残留项（仅记录）

- G6 P1 斜体旗标：D41 量测 artifact，见上（重校复核）。
- G15a/G15c HOLD：D47，见上（closer 补行 + 针对性重验）。
- G15b 仅记录（D27）。G10 Latin 新增为断 run 拆分，仅记录。
