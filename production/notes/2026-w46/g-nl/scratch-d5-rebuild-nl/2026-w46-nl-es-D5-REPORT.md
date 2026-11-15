# D5 报告 — 2026-w46-nl-es（W46 荷兰语目标 · 读者 es）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 6,193,665 字节，SHA-256 `44e9ddd6b700d22377b6005f4777790be232f4c5298fbb91064312df25f58303`；网 PDF 730,929 字节，SHA-256 `48cc1c2b3b2212ba0d186f8c30d714bafc8fda10d31d88cd0152027d5070efee`。
- 基线 D5 census：D5 Latin 494（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：latin；`_D5_READER` 位于 `svglib.py:100` = `latin`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：14/19

- P1 `EN CIFRAS` +10.2px
- P2 `RECUERDA` +24.0px
- P6 `DATOS DE PRÁCTICA` +58.6px
- D37 徽章 FAIL：margin −11.4px
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:177, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P1 numbers box title `DE WEEK IN CIJFERS　EN CIFRAS` — content12.py:50, f.box tsize 23→22 (ink →396.9px, slack 7.6)
- P2 box title `ZO ONTHOUD JE HET　RECUERDA` — content12.py:181, f.box tsize 23→21.5 (ink →400.1px, slack 4.4)
- P6 `DE GRAFIEK　DATOS DE PRÁCTICA` — content56.py:142, p.text 24→20.5pt (ink →391.5px, slack 9.0); ### line lost, see blocker
- P1 pairing badge — content12.py:21, p.text 16→15.5pt, middle-anchored (end 1450.9→1436.3px, margin −11.4→+3.2px vs cream left 1439.5)

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 77.9px PASS；D37 run2 3.2。
- P8 run2：行数 241/241，最大墨底 2560.1，距页脚线 2596 余 35.9px，距页底 2700 余 139.9px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-es tag=run2 14:06:16
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=212 news=189 cjk_sans=18 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=222 news=205 cjk_sans=17 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=206 news=191 cjk_sans=15 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=193 news=180 cjk_sans=13 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 5608124 B
PASS  G5 — web 654522 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 237, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-es: 26 boxes, 42 candidates, 0 SPILL, 42 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-es: 21 titles, 235 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-es: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=44378 web chars=44378 stripped-multiset-diff=0 G15a text.md DIFF 11 lines stripped-multiset-diff=27 -> FAIL 
REC   G15b — rc=1 CARRYOVER: FAIL
FAIL  G15c — UNEXPECTED: 2 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000CADA SEMANA ' end_x=1320.0 date_start_x=1397.9 gap=77.9px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 badge y=614 'TEXTOS EN NEERLANDÉS\u3000EXPLICACIONES EN ESPAÑOL — LA EDICIÓN P' end_x=1436.3 cream_left=1439.5 margin=3.2px (PASS)
=== 2026-w46-nl-es run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-ES.pdf` 5,608,124 字节，SHA-256 `50b722208ebc18cf578336a57ac1a3e4fe27c0e79ab7dc8ddd6fed0911b0abae`。
- 网 PDF `2026-w46-nl-es.web.pdf` 654,522 字节，SHA-256 `bc1eb2d67fc29e3739689fac5074e99ab465f07a76b8b5d9998a4c8f94bc2560`（文字 44,378 字符）。
- text.md 41,868 字节，SHA-256 `3f6a4098e3f627a83bbfc50f2034965dd968747512dd930087e74163bb68f121` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-es/2026-w46-nl-es.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。
- D37 徽章 margin run2 3.2px（探针预测 3.3px，0.1px 为墨宽 vs advance 舍入）。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。