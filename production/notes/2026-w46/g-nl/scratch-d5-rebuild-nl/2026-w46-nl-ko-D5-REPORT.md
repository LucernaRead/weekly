# D5 报告 — 2026-w46-nl-ko（W46 荷兰语目标 · 读者 ko）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 10,378,999 字节，SHA-256 `f2aae8fede6d932937e2587c992a6207217699b42afb0b202fade58d3b54b3cb`；网 PDF 1,019,674 字节，SHA-256 `1432ea17c49fdaa8b23e5f7cbd192ba19313f3c2923f38b9cd9b1b56e54c3e06`。
- 基线 D5 census：D5 Latin 323（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：cjk；`_D5_READER` 位于 `svglib.py:100` = `cjk`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：14/19

- P6 `)` +5.7px（`DE GRAFIEK　그래프(연습용 데이터)` 末行）
- D18 run1 FAIL −294.6px 为量测器 bug（空格 run 误匹配日期），真值 77.3px PASS
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:175, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P6 `DE GRAFIEK　그래프(연습용 데이터)` — content56.py:142, p.text 24→23.5pt (ink →397.6px, slack 2.9); ### line lost, see blocker

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 77.3px PASS；D37 run2 N/A（无徽章行，y=372 配对行在奶油框顶 588.0 之上）。
- P8 run2：行数 211/211，最大墨底 2542.0，距页脚线 2596 余 54.0px，距页底 2700 余 158.0px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-ko tag=run2 14:11:56
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=326 news=240 cjk_sans=68 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=389 news=266 cjk_sans=123 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=321 news=233 cjk_sans=88 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=294 news=217 cjk_sans=77 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 7369851 B
PASS  G5 — web 905149 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 217, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-ko: 26 boxes, 118 candidates, 0 SPILL, 118 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-ko: 38 titles, 476 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-ko: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=37763 web chars=37763 stripped-multiset-diff=0 G15a text.md DIFF 11 lines stripped-multiset-diff=23 -> FAIL 
REC   G15b — rc=1 CARRYOVER: FAIL
FAIL  G15c — UNEXPECTED: 2 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000매주 발행\u3000네덜란드인이' end_x=1320.6 date_start_x=1397.9 gap=77.3px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 (PASS - N/A) no P1 pairing/badge line (y>500); pairing line is at y=372, above cream box top 588.0
=== 2026-w46-nl-ko run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-KO.pdf` 7,369,851 字节，SHA-256 `014bbd7c093eed07d351f7ca6af2891d2fb607d04e6b8dcef74ac43a9ff36339`。
- 网 PDF `2026-w46-nl-ko.web.pdf` 905,149 字节，SHA-256 `78f6847a11883cfcb1cf6659b7aa831a471221d6bac3f94cd9cca6f83d3a8b1f`（文字 37,763 字符）。
- text.md 42,430 字节，SHA-256 `0dc44dc1f15519e2623c0273dfaf83a0cee1305f491a8a410f3780140c70f9a5` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-ko/2026-w46-nl-ko.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。
- D18 run1 量测器 bug 已修（空格 run 误匹配日期），run2 真值 77.3px PASS。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。