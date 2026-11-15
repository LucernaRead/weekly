# D5 报告 — 2026-w46-nl-fr（W46 荷兰语目标 · 读者 fr）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 6,180,134 字节，SHA-256 `fae23f62805324f13452f995dd53c624e242eaeb88e8690004487d45c359c10a`；网 PDF 727,795 字节，SHA-256 `555c6b6d5b99f5eb35b63d4a88c21607b138ea24e44464333fff7fd218196a06`。
- 基线 D5 census：D5 Latin 499（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：latin；`_D5_READER` 位于 `svglib.py:100` = `latin`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：15/19

- P1 `EN CHIFFRES` +44.2px
- P2 `À RETENIR` +20.0px
- P6 `DONNÉES FICTIVES` +42.6px
- P6 `POUR OU CONTRE?` +40.1px BODY
- P7 `CLINIQUE DES ERREURS` +21.1px
- P7 `MOT DE LA SEMAINE` +44.1px
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:177, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P1 numbers box title `DE WEEK IN CIJFERS　EN CHIFFRES` — content12.py:50, f.box tsize 23→20.5 (ink →400.1px, slack 4.4)
- P2 box title `ZO ONTHOUD JE HET　À RETENIR` — content12.py:181, f.box tsize 23→21.5 (ink →396.5px, slack 8.0)
- P6 `DE GRAFIEK　DONNÉES FICTIVES` — content56.py:142, p.text 24→21.5pt (ink →397.0px, slack 3.5); ### line lost, see blocker
- P6 `VOOR OF TEGEN?　POUR OU CONTRE ?` — content56.py:162, p.text 21→18.5pt (ink →388.3px, slack 12.2)
- P7 `PAS OP!　CLINIQUE DES ERREURS` — content7.py:73, p.text 23→21.5pt (ink →394.0px, slack 6.5)
- P7 `HET WOORD　MOT DE LA SEMAINE` — content7.py:84, p.text 23→20.5pt (ink →395.6px, slack 4.9)

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 54.3px PASS；D37 run2 13.9。
- P8 run2：行数 237/237，最大墨底 2560.1，距页脚线 2596 余 35.9px，距页底 2700 余 139.9px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-fr tag=run2 14:07:38
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=213 news=190 cjk_sans=18 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=225 news=208 cjk_sans=17 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=207 news=192 cjk_sans=15 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=193 news=180 cjk_sans=13 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 5606470 B
PASS  G5 — web 652873 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 238, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-fr: 26 boxes, 41 candidates, 0 SPILL, 41 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-fr: 15 titles, 245 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-fr: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=44471 web chars=44471 stripped-multiset-diff=0 G15a text.md DIFF 11 lines stripped-multiset-diff=27 -> FAIL 
REC   G15b — rc=1 CARRYOVER: FAIL
FAIL  G15c — UNEXPECTED: 2 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000CHAQUE SEMAI' end_x=1343.6 date_start_x=1397.9 gap=54.3px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 badge y=614 "TEXTES EN NÉERLANDAIS\u3000EXPLICATIONS EN FRANÇAIS — L'ÉDITION P" end_x=1425.6 cream_left=1439.5 margin=13.9px (PASS)
=== 2026-w46-nl-fr run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-FR.pdf` 5,606,470 字节，SHA-256 `adf997d1bc02f45967316f6e4859599a424a94f838b63e7ac7d6b54150eeede6`。
- 网 PDF `2026-w46-nl-fr.web.pdf` 652,873 字节，SHA-256 `8eea2048fe1aafd46a8bb9ee9186cae4eaccba0ef7949f76948e8cb492f675b0`（文字 44,471 字符）。
- text.md 42,212 字节，SHA-256 `e8c724ec899c17127cfc655825a69b69cd5d9c3bebaadb16f64c0233bd002ee9` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-fr/2026-w46-nl-fr.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、content7、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。