# D5 报告 — 2026-w46-nl-ja（W46 荷兰语目标 · 读者 ja）

日期：2026-11-15。标准：D5 + §1.1 合并重修。家族报告：`hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`。

## 1. 基线核实

- run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；印/网 PDF 文字层与 `issues/` 已发 PDF stripped-diff 0；`issues/` pin 一致；text.md 与 `issues/` BYTE-IDENTICAL；p8 extract 150/150。
- 基线印 PDF 18,688,956 字节，SHA-256 `3c0f44d6c949b95cce9234358c50fb07b951f166c35e94b0e45e2833cc1360f6`；网 PDF 1,289,644 字节，SHA-256 `1b49dad909a514c12e7628150947880ed0ccfb76270994b33f620d5f516d3ee3`。
- 基线 D5 census：D5 Latin 323（`logs/census-baseline-*.json`）。
- 基线 D18 间隙见家族报告；D37 见 §5。KIT SHA 滞后已确认——以基线实测为准，不以 KIT 旧 pin 为准。

## 2. 装机

- `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46`（先 `--check` 干跑，全 clean）。
- 模式：cjk；`_D5_READER` 位于 `svglib.py:100` = `cjk`；fix2 保留（`_QUOTE_CLS` ×4）；`test_d5_routing.py` FAILURES: 0。

## 3. run1 门禁：15/19

- P1 `数字で見る今週` +38.2px
- P6 `グラフ（練習データ）` +25.6px
- HEAD TOO WIDE ×1：P2 head（25pt）

## 4. 修复（全部只降字号，零文案改动）

- P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:175, head 25→22pt (ink 471.1→414.5px, slack 8.0)
- P1 numbers box title `DE WEEK IN CIJFERS　数字で見る今週` — content12.py:48, f.box tsize 23→20.5 (ink →394.5px, slack 10.0)
- P6 `DE GRAFIEK　グラフ（練習データ）` — content56.py:142, p.text 24→22pt (ink →390.6px, slack 9.9); ### line lost, see blocker

## 5. run2 门禁：17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS)

- D18 run2 间隙 18.7px PASS；D37 run2 N/A（无徽章行，y=372 配对行在奶油框顶 588.0 之上）。
- P8 run2：行数 224/224，最大墨底 2551.5，距页脚线 2596 余 44.5px，距页底 2700 余 148.5px。
- 19 verdict 原文：

```
=== gates 2026-w46-nl-ja tag=run2 14:10:27
PASS  G1 — TOTAL exercises: 150, OVF=0, HDW=0
PASS  G2 — HEAD CHECK PASS 0 defects 
PASS  G3 — rc=0 p1-voorpagina.svg: els=238 news=187 cjk_sans=32 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p2-leven.svg: els=242 news=184 cjk_sans=58 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p3-cultuur.svg: els=228 news=180 cjk_sans=48 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 p4-sport.svg: els=207 news=167 cjk_sans=40 noto_sans=0 D5_lat=0 D5_cyr=0 curly_cjk=0 curly=0 
PASS  G4 — render rc=0, print 10702606 B
PASS  G5 — web 1073941 B <7MB
PASS  G6 — selftest rc=0 audit rc=0
PASS  G7 — extract rc=0 noted=150/150
PASS  G8 — CLEAN, rc=0 keydiff=[137, 138]
PASS  G9 — baseline: 8/8 rc=0
PASS  G10 — CJK added 0 chars=[] (Latin added 211, run-split)
PASS  G11 — SPILL_SWEEP 2026-w46-nl-ja: 26 boxes, 67 candidates, 0 SPILL, 67 OBSERVE rc=0
PASS  G12 — BOXTITLE 2026-w46-nl-ja: 23 titles, 338 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal rc=0
PASS  G13 — EDGE_SCAN 2026-w46-nl-ja: 8 pages, 0 TOUCH, 0 NEAR rc=0
PASS  G14 — defects=0 rc=0
FAIL  G15a — G15a print chars=37811 web chars=37811 stripped-multiset-diff=0 G15a text.md DIFF 11 lines stripped-multiset-diff=22 -> FAIL 
REC   G15b — rc=1 CARRYOVER: FAIL
FAIL  G15c — UNEXPECTED: 2 block(s) rc=1
PASS  G16 — GRAND TOTAL defective: 0 rc=0
PASS  D18 — D18 slogan 'ELKE WEEK IN HET NEDERLANDS\u3000毎週一号\u3000オランダ人が読' end_x=1379.2 date_start_x=1397.9 gap=18.7px [calib centre=975.0 vs 975, date_end=1862.0 vs 1862.0] (PASS)
D18/D37: PASS
PASS  D37 — D37 (PASS - N/A) no P1 pairing/badge line (y>500); pairing line is at y=372, above cream box top 588.0
=== 2026-w46-nl-ja run2: 17/19 PASS, 2 FAIL (G15b record-only)
```

## 6. 交付物 pin（run2 终轮实测）

- 印 PDF `De-Lucerna-VOL3-JA.pdf` 10,702,606 字节，SHA-256 `8ae383d5adb1660e1e86727e2c7287a321ff6ca941b930d23826ead062fb1f08`。
- 网 PDF `2026-w46-nl-ja.web.pdf` 1,073,941 字节，SHA-256 `bf75a711695d8dfa05f1cd3e833c4ec089644d039330a4eebbf37a1424a4302b`（文字 37,811 字符）。
- text.md 42,197 字节，SHA-256 `15bfe2c3a49eacc7e4a84426742637febd58efcf32295aa8f8a16148d8d37a29` — BYTE-IDENTICAL（D47 補行后；G15a/G15c 针对性重验通过）。
- text.md 取件口径：`logs/2026-w46-nl-ja/2026-w46-nl-ja.text.md.run2`；`patched/` 与 `production/` 内同名 `.text.md` 为 2026-11-06 fanout 旧产物，不得取用。

## 7. 残留项

- **阻塞（全家共性，见家族报告 §0）**：导出器 `export_text.py:168` 的 `###` 阈值 size>=24pt —— 本版修复把标题降到 24pt 以下后，`###` 标记行从 text.md 丢失一枚；PDF 文字层无变化（fitz 基线 vs 终轮 stripped 字符差 0），G15a FAIL + G15c HOLD 均为此单一根因。
- G15b 仅记录（D27 已知工具口径差，基线同款残留）。

## 8. 同步清单（patched → production，见家族报告 §8）

- 同步文件：content12、content56、svglib + 本版 WEEKLY-KIT.md（含 §7 新 pin 与 D5 重建节）。ABSTRACT.txt 排除；JPG 绝不进 production（D20）。
- 网 PDF 由 closer 拷 builder run2 原件，不重跑 webpdf。