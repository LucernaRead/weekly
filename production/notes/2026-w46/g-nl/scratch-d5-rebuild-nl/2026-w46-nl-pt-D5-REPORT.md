# D5 报告 — 2026-w46-nl-pt（W46 荷兰语目标 · 读者 pt）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 6,196,922 字节，SHA-256 `e6d6843aa3311d23ea0688cc49cd1dcfa8765616622cb06f448efd22060f074e`；网 PDF 734,121 字节，SHA-256 `36ac9f8820c036f6631677c36df373a460ab262b903f3185f483ae4202eaed4f`。
- 基线 D5 census：D5 Latin 494（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：latin；`_D5_READER` 位于 `svglib.py:100` = `latin`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：15/19

- P1 `NÚMEROS` +7.2px
- P1 `NESTE NÚMERO` +40.5px
- P2 `LEMBRA-TE` +33.0px
- P6 `DADOS DE TREINO` +28.6px
- P6 `PRÓS E CONTRAS` +15.1px BODY
- P7 `PALAVRA DA SEMANA` +57.1px（全家最大单项）
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:175, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P1 numbers box title `DE WEEK IN CIJFERS　NÚMEROS` — content12.py:48, f.box tsize 23→22 (ink →393.9px, slack 10.6)
- P1 contents title `IN DEZE EDITIE　NESTE NÚMERO` — content12.py:90, p.text 24→21.5pt (ink →394.9px, slack 5.6); ### line lost, see blocker
- P2 box title `ZO ONTHOUD JE HET　LEMBRA-TE` — content12.py:179, f.box tsize 23→21 (ink →399.2px, slack 5.3)
- P6 `DE GRAFIEK　DADOS DE TREINO` — content56.py:142, p.text 24→22pt (ink →392.9px, slack 7.6); ### line lost, see blocker
- P6 `VOOR OF TEGEN?　PRÓS E CONTRAS` — content56.py:162, p.text 21→20pt (ink →396.2px, slack 4.3)
- P7 `HET WOORD　PALAVRA DA SEMANA` — content7.py:84, p.text 23→20pt (ink →397.2px, slack 3.3)

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 5.0px PASS；D37 run2 N/A（无徽章行，y=372 配对行在奶油框顶 588.0 之上）。
- P8 run2：行数 233/233，最大墨底 2547.9，距页脚线 2596 余 48.1px，距页底 2700 余 152.1px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-pt tag=run2 14:13:39
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=212 news=189 cjk_sans=18 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=224 news=207 cjk_sans=17 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=206 news=191 cjk_sans=15 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=191 news=179 cjk_sans=12 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 5611198 B
PASS  G5 — web 657625 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 239, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-pt: 26 boxes, 41 candidates, 0 SPILL, 41 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-pt: 19 titles, 239 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-pt: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=44209 web chars=44209 stripped-multiset-diff=0 G15a text.md DIFF 20 lines stripped-multiset-diff=51 -> FAIL 
REC   G15b — rc=2 ERROR: no verify_textmd table for reader 'pt' yet — calibrate it from that edition's own SVG/.text.md until its residual is 0, then add it to READER_TABLES in /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/tools/verify_textmd.py
FAIL  G15c — UNEXPECTED: 4 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000O NEERLANDÊS' end_x=1392.9 date_start_x=1397.9 gap=5.0px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 (PASS - N/A) no P1 pairing/badge line (y>500); pairing line is at y=372, above cream box top 588.0
=== 2026-w46-nl-pt run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-PT.pdf` 5,611,198 字节，SHA-256 `609470f61602a13a7d43b30e9f6757ae2a980f294262b863e09577c1de9ad499`。
- 网 PDF `2026-w46-nl-pt.web.pdf` 657,625 字节，SHA-256 `28290b8240c19060be41fa3bd8c8d0b458a963d3794e590efd1ef5464e372ef0`（文字 44,209 字符）。
- text.md 40,888 字节，SHA-256 `d27f670e4eb30eaa9241c0e2e16dce8df1dac0b0b72078ba044cc7a15c8993f3` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-pt/2026-w46-nl-pt.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。
- D18 run2 5.0px 为全家最紧。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、content7、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。