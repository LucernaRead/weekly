# D5 报告 — 2026-w46-nl-zh-cn（W46 荷兰语目标 · 读者 zh-cn）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 17,797,581 字节，SHA-256 `5655379045484e0e7cf12f3b918527d92ac0e42e56acb4513849c13ff3134149`；网 PDF 1,237,283 字节，SHA-256 `d65cea86066c7b9d5d1d23eaac9bf1a0c51dcbac5c9d590baf21d0b6277911a5`。
- 基线 D5 census：D5 Latin 331 + curly-in-CJK 2 (curly total 4)（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。 core-nl 以 `--reader zh-cn` 装机。
- 模式：cjk；`_D5_READER` 位于 `svglib.py:100` = `cjk`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：17/19

- HEAD TOO WIDE ×1：P2 head `DRIE DINGEN VOOR 11 NOVEMBER`（25pt），其余 18 门全绿

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:175, head 25→22pt (ink 471.1→414.5px, slack 8.0)

## 5. run2 门禁：19/19

- D18 run2 间隙 93.2px PASS；D37 run2 N/A（无徽章行，y=372 配对行在奶油框顶 588.0 之上）。
- P8 run2：行数 213/213，最大墨底 2541.0，距页脚线 2596 余 55.0px，距页底 2700 余 159.0px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-zh-cn tag=run2 14:19:24
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=244 news=192 cjk_sans=33 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=2 p2-leven.svg: els=241 news=188 cjk_sans=53 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=228 news=181 cjk_sans=47 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=209 news=168 cjk_sans=41 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 7347872 B
PASS  G5 — web 1011482 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 218, run-split)
PASS  G11 — SPILL_SWEEP core-nl: 26 boxes, 70 candidates, 0 SPILL, 70 OBSERVE rc=0
PASS  G12 — BOXTITLE core-nl: 25 titles, 325 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN core-nl: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
PASS  G15a — G15a print chars=36860 web chars=36860 stripped-multiset-diff=0 G15a text.md BYTE-IDENTICAL (39208 bytes) 
REC   G15b — rc=1 CARRYOVER: FAIL
PASS  G15c — verdict: ADOPT (0 UNEXPECTED) rc=0
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000每周一期\u3000读荷兰人正在读' end_x=1304.7 date_start_x=1397.9 gap=93.2px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 (PASS - N/A) no P1 pairing/badge line (y>500); pairing line is at y=372, above cream box top 588.0
=== 2026-w46-nl-zh-cn run2: 19/19 PASS, 0 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3.pdf` 7,347,872 字节，SHA-256 `ab840bcd5e6b28fdbe89f18b0176ac268109c9d41c285d7fec47910a4c9a67b1`。
- 网 PDF `2026-w46-nl-zh-cn.web.pdf` 1,011,482 字节，SHA-256 `2c0a602c6f654e86da102c4b94e1f64231ed8d8f36045a2de12709dcccf88134`（文字 36,860 字符）。
- text.md 39,208 字节，SHA-256 `056619a357e6d4323e1c13d51a84f52ff5b470a6409978483f63f70a8b0726c6` — BYTE-IDENTICAL vs `issues/` (39,208 bytes)。
- text.md 取件口径：`logs/2026-w46-nl-zh-cn/2026-w46-nl-zh-cn.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- 无阻塞。text.md BYTE-IDENTICAL。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、svglib（core-nl，随 zh-cn bundle 同步） + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。