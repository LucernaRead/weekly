# D5 rebuild report — 2026-w45-zh-tw-ja (W45 zh-tw × ja)

- Week: 2026-W45 (VOL.2). Target: Traditional Chinese (zh-tw). Reader: Japanese.
- Core: `production/2026-w45/core-zh-tw/` (en edition doubles as core).
- Builder: scratch `hidden_files/d5-redo/scratch-2026-w45-zh-tw/` (`baseline/` + `patched/`).
- Date: 2026-11-14. Method: D5-METHOD §3 (16 gates + D18 + D37).

## 1. Baseline (pre-D5 rebuild, venv)

- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2.pdf`: 17,608,680 B, SHA-256 `8884c8d2740d6066357f0562657aeee323558f554c702d63e7764ef3a053d8f5` — matches MANIFEST-W45 §zh-tw-ja print pin byte-for-byte.
- Web PDF: 2,633,089 B (< 7 MB). pdfdiff vs issued web PDF: IDENTICAL (weekly word trim `「金融科技」—|「金融科技」`).
- print-vs-web text multiset: rc 0.
- Naive textexp: BYTE-IDENTICAL to the fanout `.text.md.new` (53,365 B).
- Joiner regression (textexp_zh_tw_d5.py v2 on baseline SVG): BYTE-IDENTICAL to fanout.
- Pre-D5 census: `d5_latin_in_cjk` 281 (> 0 — the defect D5 fixes).
- p8 extract 150/150; p8 compare vs baseline core: CLEAN.

## 2. Install

- `_D5_READER = "cjk"` (mode cjk); routing test FAILURES: 0.
- fix2 retained: `_QUOTE_CLS` ×4, fix2 block ×1, D5 block ×1.
- svglib diff vs baseline: 142 lines (W43 precedent: 100 latin/ru, 142 ja/ko).

## 3. Rebuild (patched)

- run → render → webpdf, `tools/venv/bin/python`; fontconfig warmed (`fc-cache -f`) before the first render.
- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2.pdf`: 16,784,370 B, SHA-256 `995310a7b8000db0d41d4caa90b7d2e8a78b09ec4f269a6597d384cde8ea920f`.
- Web PDF `2026-w45-zh-tw-ja.web.pdf`: 2,511,546 B (< 7 MB), SHA-256 `c4e62ee226bb776d65c92010b58c396d009ce1f682c117960665407781b90c4c`.
- Text `2026-w45-zh-tw-ja.text.md.new`: 53,419 B, SHA-256 `8b35a4732f3671e6e6fe2d522351ed678d1446c29fc0630143c751c18ceecb26` (joiner export).

## 4. Gates (all green)

| Gate | Result | Detail |
|---|---|---|
| GATE 1 | PASS | run TOTAL 150, 0 FLOW, 0 HEAD |
| GATE 2 | PASS | head_check 0 defects |
| GATE 3 | PASS | d5 census PASS (latin 0, cyrillic 0, curly-in-CJK 0) |
| GATE 4 | PASS | render RC=0, print PDF written |
| GATE 5 | PASS | webpdf RC=0, web 2511546 B <7MB |
| GATE 6 | PASS | occlusion selftest OK, 0 flags |
| GATE 7 | PASS | p8 extract 150/150 |
| GATE 8 | PASS | p8 compare CLEAN (CLEAN [] [] []) |
| GATE 9 | PASS | freeze baseline 8/8 |
| GATE 10 | PASS | freeze diff vs BASE: added CJK 0 (strict-cjk) |
| GATE 11 | PASS | spill 0 (0 SPILL) |
| GATE 12 | PASS | boxtitle 0 DEFECT (BOXTITLE 2026-w45-zh-tw-ja: 20 titles, 628 body lines, 0 DEFECT) |
| GATE 13 | PASS | edge 0 TOUCH 0 NEAR (EDGE_SCAN 2026-w45-zh-tw-ja: 8 pages, 0 TOUCH, 0 NEAR) |
| GATE 14 | PASS | creambox PASS 0 defects (selftest OK) |
| GATE 15c | PASS | native verifier ADOPT (all pages) |
| GATE 15a | REFLOW | (accepted, D30) difflines=128 multiset=0 native=ADOPT |
| GATE 15 | PASS | print=web multiset 0 + 15a REFLOW (D30) + 15c native ADOPT |
| GATE 16 | PASS | census_quotes 0 defective |
| GATE D18 | PASS | masthead gaps >0 (see measure-p1.log) |
| GATE D37 | PASS | no P1 line crosses right-box edge (see measure-p1.log) |

- D18 masthead gaps (y=316): min inter-element gap 8.0px (all 10 editions identical) — PASS (> 0).
- D37 P1 lines vs right cream box (left 1439.5): no line starting left of the box crosses its edge; y=612 line absent in this family — PASS.
- P8: 146 lines (baseline 146); footer slack 37.9 px (footer rule y=2596, page bottom 2700).
- Gate 15a: REFLOW (accepted, D30) — whitespace-stripped char multiset diff 0, native verifier ADOPT, difflines 128. Gate 15b shared verifier: baseline rc=1, patched rc=1 (D27 diagnostic, not a gate verdict).

## 5. Fixes

- Round 1 gates (2026-11-14): gate 12 boxtitle 2 DEFECT + gate 14 creambox 2 defects — both true D5 regressions, same two gloss boxes:
  - P4 [BODY] +3.5px right: `content34.py:117` gloss “4つの言葉：完封（シャットアウト）、封王（優勝決定）、全壘打（ホームラン）、MVP（最優秀選手）。”, 20.5pt, box (538.5, 858.25, 422.5, 145.675). Root cause: `wrap()` SEAM_SLACK=28 lets a line reach max_w+28 = 414.5px, but the box text area is 404.5px; the TC face fit, the JP face is wider for this string.
  - P5 [BODY] +8.5px right: `content56.py:22` gloss (旅展攻略…マスコットパレード…), 20.5pt, box (88, 1866.665, 422.5, 264.575).
- Fix (patched/ only): `bslib4.py` `gloss()` gains a `size=20.5` parameter; the two call sites pass `size=19.5`. No other gloss box touched (10 others byte-identical).
- Round 2 gates: P5 fixed, P4 line 1 still +2.2px right at 19.5pt (measured 406.7px vs 405.3px simulated — simulation under-reads by ~1.4px).
- Round 2 fix: P4 gloss `size=19.5` → `19.0` (simulated max line 394.9px, ~8px clearance).
- Round 3 gates: 19/19 green — boxtitle 0 DEFECT, creambox 0 defects. P8 lines 146→146, footer slack 37.9px unchanged.

## 6. Residuals

None.

## 7. Re-proof points

- re-check the two fixed gloss boxes (P4 baseball-words gloss at 19.0pt, P5 travel-fair gloss at 19.5pt) for clean reflow and no box-bottom crowding; confirm no wording changed anywhere (whitespace-stripped char multiset diff 0); P8 quiz content unchanged (150/150, compare CLEAN).

## 8. Files (builder originals)

- Print: `patched/2026-w45-zh-tw-ja/Lucerna-VOL2.pdf` (16,784,370 B, `995310a7b8000db0d41d4caa90b7d2e8a78b09ec4f269a6597d384cde8ea920f`)
- Web: `patched/2026-w45-zh-tw-ja/2026-w45-zh-tw-ja.web.pdf` (2,511,546 B, `c4e62ee226bb776d65c92010b58c396d009ce1f682c117960665407781b90c4c`) — closer copies the original, never re-runs webpdf.
- Text: `logs/2026-w45-zh-tw-ja/2026-w45-zh-tw-ja.text.md.new` (53,419 B, `8b35a4732f3671e6e6fe2d522351ed678d1446c29fc0630143c751c18ceecb26`)
- Gates: `logs/2026-w45-zh-tw-ja/GATES-SUMMARY.txt` (copy in `production/notes/2026-w45/g-zh-tw/scratch-d5-rebuild-zh-tw/`, `cmp`-verified).
