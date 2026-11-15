# D5 rebuild report — 2026-w45-zh-tw-es (W45 zh-tw × es)

- Week: 2026-W45 (VOL.2). Target: Traditional Chinese (zh-tw). Reader: Spanish.
- Core: `production/2026-w45/core-zh-tw/` (en edition doubles as core).
- Builder: scratch `hidden_files/d5-redo/scratch-2026-w45-zh-tw/` (`baseline/` + `patched/`).
- Date: 2026-11-14. Method: D5-METHOD §3 (16 gates + D18 + D37).

## 1. Baseline (pre-D5 rebuild, venv)

- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-ES.pdf`: 20,370,347 B, SHA-256 `0bc020f257608dd1289e303ad9328d224bd50aa05de41fe3f8d69ecc4de8c636` — matches MANIFEST-W45 §zh-tw-es print pin byte-for-byte.
- Web PDF: 2,447,411 B (< 7 MB). pdfdiff vs issued web PDF: IDENTICAL (weekly word trim `「金融科技」—|「金融科技」`).
- print-vs-web text multiset: rc 0.
- Naive textexp: BYTE-IDENTICAL to the fanout `.text.md.new` (52,237 B).
- Joiner regression (textexp_zh_tw_d5.py v2 on baseline SVG): BYTE-IDENTICAL to fanout.
- Pre-D5 census: `d5_latin_in_cjk` 626 (> 0 — the defect D5 fixes).
- p8 extract 150/150; p8 compare vs baseline core: CLEAN.

## 2. Install

- `_D5_READER = "latin"` (mode latin); routing test FAILURES: 0.
- fix2 retained: `_QUOTE_CLS` ×4, fix2 block ×1, D5 block ×1.
- svglib diff vs baseline: 100 lines (W43 precedent: 100 latin/ru, 142 ja/ko).

## 3. Rebuild (patched)

- run → render → webpdf, `tools/venv/bin/python`; fontconfig warmed (`fc-cache -f`) before the first render.
- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-ES.pdf`: 10,665,886 B, SHA-256 `eae66cad7c0cccf9f6d24498ddabe6f55ad4e370c69473851a481e6fb5c8bd70`.
- Web PDF `2026-w45-zh-tw-es.web.pdf`: 1,888,333 B (< 7 MB), SHA-256 `2d86c67fee3b7fef0e0256fd3d3a749d020e402ba5f9564de95b3cf5913f6f71`.
- Text `2026-w45-zh-tw-es.text.md.new`: 52,327 B, SHA-256 `001a0392e6050d1004798fd3f503ed4ee5a80927c6a60a34a2ef52d1c1a6cceb` (joiner export).

## 4. Gates (all green)

| Gate | Result | Detail |
|---|---|---|
| GATE 1 | PASS | run TOTAL 150, 0 FLOW, 0 HEAD |
| GATE 2 | PASS | head_check 0 defects |
| GATE 3 | PASS | d5 census PASS (latin 0, cyrillic 0, curly-in-CJK 0) |
| GATE 4 | PASS | render RC=0, print PDF written |
| GATE 5 | PASS | webpdf RC=0, web 1888333 B <7MB |
| GATE 6 | PASS | occlusion selftest OK, 0 flags |
| GATE 7 | PASS | p8 extract 150/150 |
| GATE 8 | PASS | p8 compare CLEAN (CLEAN [] [] []) |
| GATE 9 | PASS | freeze baseline 8/8 |
| GATE 10 | PASS | freeze diff vs BASE: added CJK 0 (strict-cjk) |
| GATE 11 | PASS | spill 0 (0 SPILL) |
| GATE 12 | PASS | boxtitle 0 DEFECT (BOXTITLE 2026-w45-zh-tw-es: 40 titles, 461 body lines, 0 DEFECT) |
| GATE 13 | PASS | edge 0 TOUCH 0 NEAR (EDGE_SCAN 2026-w45-zh-tw-es: 8 pages, 0 TOUCH, 0 NEAR) |
| GATE 14 | PASS | creambox PASS 0 defects (selftest OK) |
| GATE 15c | PASS | native verifier ADOPT (all pages) |
| GATE 15a | REFLOW | (accepted, D30) difflines=274 multiset=0 native=ADOPT |
| GATE 15 | PASS | print=web multiset 0 + 15a REFLOW (D30) + 15c native ADOPT |
| GATE 16 | PASS | census_quotes 0 defective |
| GATE D18 | PASS | masthead gaps >0 (see measure-p1.log) |
| GATE D37 | PASS | no P1 line crosses right-box edge (see measure-p1.log) |

- D18 masthead gaps (y=316): min inter-element gap 8.0px (all 10 editions identical) — PASS (> 0).
- D37 P1 lines vs right cream box (left 1439.5): no line starting left of the box crosses its edge; y=612 line absent in this family — PASS.
- P8: 165 lines (baseline 174); footer slack 35.2 px (footer rule y=2596, page bottom 2700).
- Gate 15a: REFLOW (accepted, D30) — whitespace-stripped char multiset diff 0, native verifier ADOPT, difflines 274. Gate 15b shared verifier: baseline rc=1, patched rc=1 (D27 diagnostic, not a gate verdict).

## 5. Fixes

None — first patched rebuild passed all gates; no fix needed.

## 6. Residuals

None.

## 7. Re-proof points

- confirm no wording changed anywhere (whitespace-stripped char multiset diff 0); P8 quiz content unchanged (150/150, compare CLEAN); spot-check P1 masthead and P7 teaser clearance.

## 8. Files (builder originals)

- Print: `patched/2026-w45-zh-tw-es/Lucerna-VOL2-ES.pdf` (10,665,886 B, `eae66cad7c0cccf9f6d24498ddabe6f55ad4e370c69473851a481e6fb5c8bd70`)
- Web: `patched/2026-w45-zh-tw-es/2026-w45-zh-tw-es.web.pdf` (1,888,333 B, `2d86c67fee3b7fef0e0256fd3d3a749d020e402ba5f9564de95b3cf5913f6f71`) — closer copies the original, never re-runs webpdf.
- Text: `logs/2026-w45-zh-tw-es/2026-w45-zh-tw-es.text.md.new` (52,327 B, `001a0392e6050d1004798fd3f503ed4ee5a80927c6a60a34a2ef52d1c1a6cceb`)
- Gates: `logs/2026-w45-zh-tw-es/GATES-SUMMARY.txt` (copy in `production/notes/2026-w45/g-zh-tw/scratch-d5-rebuild-zh-tw/`, `cmp`-verified).
