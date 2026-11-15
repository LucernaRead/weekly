# D5 报告 — 2026-w46-nl-it（W46 荷兰语目标 · 读者 it）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 6,191,732 字节，SHA-256 `a735a42a9df48721d797787bf9c46a87afbc98d824ae80ca5e2666edd6989ba7`；网 PDF 725,275 字节，SHA-256 `07380a482dc36cdaab510f676e5744917cfce8329b17a8b525b8283957350d4f`。
- 基线 D5 census：D5 Latin 495（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：latin；`_D5_READER` 位于 `svglib.py:100` = `latin`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：14/19

- P6 `PRO O CONTRO?` +3.1px BODY
- P7 `CLINICA DEGLI ERRORI` +8.1px
- G6 TEXTX（D5 回归，基线 0 flags）：P8 标题与右侧灰注重叠 42.1×19.0px
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:177, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P8 TEXTX (D5 regression; baseline 0 flags) — content8.py:119, title p.text 25→23.5pt (title ink 1135.1→1066.9px vs 1090.8px available, slack 23.9; right-anchored note 681.2px)
- P6 `VOOR OF TEGEN?　PRO O CONTRO?` — content56.py:162, p.text 21→20.5pt (ink →393.6px, slack 6.9)
- P7 `PAS OP!　CLINICA DEGLI ERRORI` — content7.py:73, p.text 23→22pt (ink →391.2px, slack 9.3)

## 5. run2 门禁：19/19

- D18 run2 间隙 77.9px PASS；D37 run2 106.3。
- P8 run2：行数 234/234，最大墨底 2545.2，距页脚线 2596 余 50.8px，距页底 2700 余 154.8px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-it tag=run2 14:09:01
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=213 news=190 cjk_sans=18 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=222 news=205 cjk_sans=17 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=206 news=191 cjk_sans=15 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=191 news=179 cjk_sans=12 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 5602970 B
PASS  G5 — web 649327 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 237, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-it: 26 boxes, 41 candidates, 0 SPILL, 41 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-it: 25 titles, 231 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-it: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
PASS  G15a — G15a print chars=44259 web chars=44259 stripped-multiset-diff=0 G15a text.md BYTE-IDENTICAL (41537 bytes) 
REC   G15b — rc=1 CARRYOVER: FAIL
PASS  G15c — verdict: ADOPT (0 UNEXPECTED) rc=0
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000OGNI SETTIMA' end_x=1320.0 date_start_x=1397.9 gap=77.9px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 badge y=614 "TESTI IN OLANDESE\u3000SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I" end_x=1333.2 cream_left=1439.5 margin=106.3px (PASS)
=== 2026-w46-nl-it run2: 19/19 PASS, 0 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-IT.pdf` 5,602,970 字节，SHA-256 `02ca0720444bc86d1df569973580c5b925545e34d531a1672b8fe9e66763d323`。
- 网 PDF `2026-w46-nl-it.web.pdf` 649,327 字节，SHA-256 `29f1e524a472c77b8a8a2d9d74e396a7e39ecb8790892b9321dd3eb68f0687a5`（文字 44,259 字符）。
- text.md 41,537 字节，SHA-256 `fb1116cfe7b91d2705f9923381aa5c7eb1163a66365603653b75b2e17b8ed551` — BYTE-IDENTICAL vs `issues/` (41,537 bytes)。
- text.md 取件口径：`logs/2026-w46-nl-it/2026-w46-nl-it.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- 无阻塞。text.md BYTE-IDENTICAL。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。
- G12 另有 1 marginal（工具计数、不点名，非缺陷，rc=0）。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、content7、content8、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。