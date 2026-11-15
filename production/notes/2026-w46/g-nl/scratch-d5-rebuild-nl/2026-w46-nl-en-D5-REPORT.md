# D5 报告 — 2026-w46-nl-en（W46 荷兰语目标 · 读者 en）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 6,178,707 字节，SHA-256 `f3d678675ed7e09baf831c9bc1a000f34d4e223142c02779e8355131677dd481`；网 PDF 725,007 字节，SHA-256 `5e7f0b504b8e51152af6d4ee52ee42ce9ade44090a5aa26e4fcc53f95b9559cb`。
- 基线 D5 census：D5 Latin 495（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：latin；`_D5_READER` 位于 `svglib.py:100` = `latin`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：15/19

- P1 `IN NUMBERS` +39.2px
- P1 `THIS WEEK'S EVENTS` +9.2px BODY
- P1 `IN THIS ISSUE` +8.5px
- P2 `REMEMBER` +34.0px
- P6 `FOR OR AGAINST?` +24.1px BODY
- P7 `WORD OF THE WEEK` +38.1px
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:175, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P1 numbers box title `DE WEEK IN CIJFERS　IN NUMBERS` — content12.py:48, f.box tsize 23→20.5 (ink →395.6px, slack 8.9)
- P1 agenda line `Agenda van de week　THIS WEEK'S EVENTS` — content12.py:70, p.text 19→18pt (ink →388.4px, slack 12.1)
- P1 contents title `IN DEZE EDITIE　IN THIS ISSUE` — content12.py:90, p.text 24→23pt (ink →391.7px, slack 8.8); ### line lost, see blocker
- P2 box title `ZO ONTHOUD JE HET　REMEMBER` — content12.py:179, f.box tsize 23→21 (ink →400.4px, slack 4.1)
- P6 `VOOR OF TEGEN?　FOR OR AGAINST?` — content56.py:162, p.text 21→19.5pt (ink →393.9px, slack 6.6)
- P7 `HET WOORD　WORD OF THE WEEK` — content7.py:84, p.text 23→20.5pt (ink →390.8px, slack 9.7)

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 100.1px PASS；D37 run2 N/A（无徽章行，y=372 配对行在奶油框顶 588.0 之上）。
- P8 run2：行数 237/237，最大墨底 2555.5，距页脚线 2596 余 40.5px，距页底 2700 余 144.5px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-en tag=run2 14:04:52
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=215 news=190 cjk_sans=20 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=222 news=204 cjk_sans=18 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=208 news=192 cjk_sans=16 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=193 news=180 cjk_sans=13 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 5602917 B
PASS  G5 — web 649294 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 249, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-en: 26 boxes, 42 candidates, 0 SPILL, 42 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-en: 19 titles, 234 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-en: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=43478 web chars=43478 stripped-multiset-diff=0 G15a text.md DIFF 11 lines stripped-multiset-diff=26 -> FAIL 
REC   G15b — rc=1 CARRYOVER: FAIL
FAIL  G15c — UNEXPECTED: 2 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000EVERY WEEK\u3000R' end_x=1297.8 date_start_x=1397.9 gap=100.1px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 (PASS - N/A) no P1 pairing/badge line (y>500); pairing line is at y=372, above cream box top 588.0
=== 2026-w46-nl-en run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-EN.pdf` 5,602,917 字节，SHA-256 `390c68ff1185abd6b43ff2757ddcfa98b23abae15fdf03d51bd4f33bc56e2640`。
- 网 PDF `2026-w46-nl-en.web.pdf` 649,294 字节，SHA-256 `c70283142eb278d893d57f1b0a25362fa7d7290ae69f47b691b75bc89a634c66`（文字 43,478 字符）。
- text.md 40,134 字节，SHA-256 `98493cef669acc0a34945e7b2186995aaf7ddba8d8befa3c8a59331860163d8d` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-en/2026-w46-nl-en.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、content7、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。