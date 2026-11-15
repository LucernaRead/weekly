# D5 report — 2026-w46-ru-it（W46 ru，读者 it · Italian）

- 构建目录：`patched/2026-w46-ru-it/`；目标语 ru；模式 latin；`_D5_READER` 在 `svglib.py:107` = `latin`；fix2 `_QUOTE_CLS` ×4；ru 内容走旧 `_D5_READER == "ru"` 分支（D26；fix-xru 未引入）；`test_d5_routing.py` FAILURES: 0。
- 基线：run TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；text.md 与 `issues/` BYTE-IDENTICAL；印/网 PDF 文字层与已发 PDF 去空白多重集差 0；`issues/` pin（pdfBytes/pdfSha256）与文件一致；p8 extract 150/150。修前普查：D5 Latin in CJK 435、Cyrillic in CJK 0、curly in CJK 8。基线 D18 间隙 165.2px、D37 余量 155.8px。

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
| G15a textlayer+text.md | PASS | PASS |
| G15b carryover (record only) | RECORD | RECORD |
| G15c native_verify | PASS | PASS |
| G16 quotes | PASS | PASS |
| D18 masthead | PASS | PASS |
| D37 badge | PASS | PASS |

run1：16/19 scored gates PASS；run2：18/19 scored gates PASS。

## 修复（2 处，只降字号）

- `content12.py:67` P1 媒体盒 `СМИ　COSA DICONO I MEDIA`：27→25pt（run1 越界 +23.4px；探针余量 5.7px；—）。
- `content7.py:69` P7 标题 `ОШИБКИ　CLINICA DEGLI ERRORI`：23→21.5pt（run1 越界 +24.6px；探针余量 0.8px；—）。

## 终轮门禁详情（run2）

- G1：TOTAL=150 OVF=0 HDW=0。G2：head_check 0 defects。G3：D5 Latin in CJK 0、Cyrillic 0、curly in CJK 0、curly_total 16、noto_sans 354。
- G6：flags=1，仅剩 P1 斜体 `предзимье` TEXTX 旗标（`ink overlaps '»' by 4.8x9.8px`）——D41 量测 artifact：该行 runs 与基线逐字同位（`«` x=1439.5、`предзимье` x=1450.7、`»` x=1563.7，21.5pt italic，全 11 版同值）；300 dpi 像素实测 `ь` 墨尾 SVG 1554.5、`»` 墨首 1556.4，实隙 1.9 SVG 单位（~5.9px），无真实碰撞；审计器以正体字宽量斜体字致误报。基线同态，D5 零改动此行。由重校复核接受。
- G7：p8 extract 150/150。G8：p8 compare CLEAN，keydiff=[137, 138, 139, 140]（E 节翻译，by design）。G9：freeze baseline 8/8。G10：CJK added 0；Latin added 147（断 run 拆分，仅记录）。G11：SPILL=0。G12：defects=0（titles=54，body_lines=657）。G13：edge 0/0。G14：creambox 0 defects。
- G15a：print=35557 web=35557 issued=35763，print-web raw multiset diff 0；pdfdiff vs 已发：IDENTICAL。 text.md 与已发版 BYTE-IDENTICAL。
- G15b（仅记录）：SVG-only 554 / MD-only 2074。
- G15c：原生校验器 ADOPT（UNEXPECTED 0 块）。
- G16：GRAND TOTAL defective: 0。D18：间隙 135.5px（centre=975.0、date_end=1862.0）。D37：124.0px（y=372.0）。

## 交付物 pin（run2，builder 原件）

- 印 PDF `Lucerna-VOL3-ru-it.pdf`：14198729 字节，SHA-256 `e22d3618fa12eae242bd5867b64277782f21052b3ef911383678ede8ff10938e`
- 网 PDF `2026-w46-ru-it.web.pdf`：2318221 字节，SHA-256 `056f0714d4962bafb816573f7200fb75a48a21e0ed5b3140d707011868bd40f1`
- text.md（导出器输出）：55293 字节，SHA-256 `6cdb16b179959b984a21eef10e327ff243bfce24c57445ba89daa7e740343f54`

## 残留项（仅记录）

- G6 P1 斜体旗标：D41 量测 artifact，见上（重校复核）。
- G15b 仅记录（D27）。G10 Latin 新增为断 run 拆分，仅记录。
