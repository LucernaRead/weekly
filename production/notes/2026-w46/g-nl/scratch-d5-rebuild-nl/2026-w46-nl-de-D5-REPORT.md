# D5 报告 — 2026-w46-nl-de（W46 荷兰语目标 · 读者 de）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 6,194,387 字节，SHA-256 `4ba753d022db16927c76f907dcaccc6defe47949fea5c3880cb95be77630c241`；网 PDF 730,817 字节，SHA-256 `6f9ce924f4c761fd22d8f0751fdbbc0b9e05e3eea2339f09176f28784085e056`。
- 基线 D5 census：D5 Latin 496（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：latin；`_D5_READER` 位于 `svglib.py:100` = `latin`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：15/19

- P1 `IN ZAHLEN` +17.2px（core −7.8）
- P1 `KURZ GEMELDET` +24.7px（core −22.0）
- P2 `MERK ES DIR` +47.0px（core −18.0）
- P6 `PRO UND KONTRA` +26.1px BODY（core −22.0）
- P7 `WORT DER WOCHE` +17.1px（core −22.0）
- HEAD TOO WIDE ×1：P2 head `DRIE DINGEN VOOR 11 NOVEMBER`（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:177, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P1 numbers box title `DE WEEK IN CIJFERS　IN ZAHLEN` — content12.py:50, f.box tsize 23→21.5 (ink 421.6→394.0px, slack 10.5)
- P1 `IN HET KORT　KURZ GEMELDET` — content12.py:134, p.text 24→22.5pt (ink 424.6→398.0px, slack 2.5); ### line lost, see blocker
- P2 box title `ZO ONTHOUD JE HET　MERK ES DIR` — content12.py:181, f.box tsize 23→20 (ink 452.0→393.0px, slack 11.5)
- P6 `VOOR OF TEGEN?　PRO UND KONTRA` — content56.py:162, p.text 21→19.5pt (ink 426.9→396.4px, slack 4.1)
- P7 `HET WOORD　WORT DER WOCHE` — content7.py:84, p.text 23→21.5pt (ink 416.9→389.7px, slack 10.8)

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 56.3px PASS；D37 run2 26.3。
- P8 run2：行数 227/227，最大墨底 2560.0，距页脚线 2596 余 36.0px，距页底 2700 余 140.0px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-de tag=run2 14:03:26
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=213 news=190 cjk_sans=18 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=221 news=204 cjk_sans=17 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=207 news=192 cjk_sans=15 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=190 news=178 cjk_sans=12 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 5604980 B
PASS  G5 — web 651370 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 232, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-de: 26 boxes, 41 candidates, 0 SPILL, 41 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-de: 19 titles, 238 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-de: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=44400 web chars=44400 stripped-multiset-diff=0 G15a text.md DIFF 11 lines stripped-multiset-diff=24 -> FAIL 
REC   G15b — rc=1 CARRYOVER: FAIL
FAIL  G15c — UNEXPECTED: 2 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000JEDE WOCHE A' end_x=1341.6 date_start_x=1397.9 gap=56.3px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 badge y=614 'NIEDERLÄNDISCHER TEXT\u3000DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR' end_x=1413.2 cream_left=1439.5 margin=26.3px (PASS)
=== 2026-w46-nl-de run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-DE.pdf` 5,604,980 字节，SHA-256 `c85eb233c7782e69858d38c20f0d396ecc062cb23bbb50fa56b6d8d50d752887`。
- 网 PDF `2026-w46-nl-de.web.pdf` 651,370 字节，SHA-256 `b9627c7dbc29236b3244e043a76e7128eca81956dcf8989cc4b3e595d8a830cc`（文字 44,400 字符）。
- text.md 40,835 字节，SHA-256 `67857267c3afbee3923b67c4f040975cb9fe7b0462ab0df88276107ff27f130e` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-de/2026-w46-nl-de.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、content7、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。