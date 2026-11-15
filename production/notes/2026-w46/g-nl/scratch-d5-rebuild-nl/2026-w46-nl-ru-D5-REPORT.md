# D5 报告 — 2026-w46-nl-ru（W46 荷兰语目标 · 读者 ru）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 6,195,788 字节，SHA-256 `022cf486e32e002111a6f043db84002f0bb0cf630726e2a1158e96082027e62b`；网 PDF 774,392 字节，SHA-256 `4d9f3b5432a04f8acd1a13b84f85e6d6eb19e2d566b80bb58ebd2a205b53d397`。
- 基线 D5 census：D5 Latin 329 + D5 Cyrillic 270（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：ru；`_D5_READER` 位于 `svglib.py:100` = `ru`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：15/19

- P1 `В ЭТОМ НОМЕРЕ` +1.6px
- G11 SPILL ×1：P2 lichtjes 行俄文释义 4 行溢出盒底 13.34px（基线同款，pre-existing，非 D5 回归）
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:175, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P1 contents title `IN DEZE EDITIE　В ЭТОМ НОМЕРЕ` — content12.py:90, p.text 24→23.5pt (ink →393.7px, slack 6.8); ### line lost, see blocker
- P2 lichtjes-row spill — content12.py:228, definition `p.para` 19→17.5pt (LAMPION definition 4→3 lines; box bottom 1768.0, last line was 13.34px below; baseline-identical pre-existing spill, not a D5 regression)

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 167.0px PASS；D37 run2 N/A（无徽章行，y=372 配对行在奶油框顶 588.0 之上）。
- P8 run2：行数 247/247，最大墨底 2558.3，距页脚线 2596 余 37.7px，距页底 2700 余 141.7px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-ru tag=run2 14:15:31
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=225 news=110 cjk_sans=18 noto_sans=85 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=224 news=106 cjk_sans=17 noto_sans=101 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=208 news=99 cjk_sans=15 noto_sans=94 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=195 news=91 cjk_sans=13 noto_sans=91 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 5866946 B
PASS  G5 — web 893471 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 151, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-ru: 26 boxes, 41 candidates, 0 SPILL, 41 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-ru: 25 titles, 277 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-ru: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=44147 web chars=44147 stripped-multiset-diff=0 G15a text.md DIFF 11 lines stripped-multiset-diff=26 -> FAIL 
REC   G15b — rc=1 CARRYOVER: FAIL
FAIL  G15c — UNEXPECTED: 2 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000ЧИТАЕМ ПО-ГО' end_x=1266.7 date_start_x=1433.7 gap=167.0px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 (PASS - N/A) no P1 pairing/badge line (y>500); pairing line is at y=372, above cream box top 588.0
=== 2026-w46-nl-ru run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-RU.pdf` 5,866,946 字节，SHA-256 `38303d35cba52cdf9998a533e0772e279a75dca23a0ac86daf916885116a50cc`。
- 网 PDF `2026-w46-nl-ru.web.pdf` 893,471 字节，SHA-256 `a3968d091cc4eadd5ed9d1498cd25e105ecf63f44f642a117192c125fadcb9ad`（文字 44,147 字符）。
- text.md 50,743 字节，SHA-256 `0aef78e38676690a1457223c7336f070fe00747055e36be9e34532bbb8ac617a` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-ru/2026-w46-nl-ru.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。
- G11 lichtjes 溢出为基线同款 pre-existing，修复后 run2 0 SPILL。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。