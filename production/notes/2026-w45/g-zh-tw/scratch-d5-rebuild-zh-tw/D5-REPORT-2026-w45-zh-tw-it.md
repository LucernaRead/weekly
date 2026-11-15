# D5 rebuild report — 2026-w45-zh-tw-it (W45 zh-tw × it)

- Week: 2026-W45 (VOL.2). Target: Traditional Chinese (zh-tw). Reader: Italian.
- Core: `production/2026-w45/core-zh-tw/` (en edition doubles as core).
- Builder: scratch `hidden_files/d5-redo/scratch-2026-w45-zh-tw/` (`baseline/` + `patched/`).
- Date: 2026-11-14. Method: D5-METHOD §3 (16 gates + D18 + D37).

## 1. Baseline (pre-D5 rebuild, venv)

- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-IT.pdf`: 19,570,472 B, SHA-256 `2160b702f55eb0d1253c1c491b60460619c65067a6e710b12d6ec0c7369864e1` — matches MANIFEST-W45 §zh-tw-it print pin byte-for-byte.
- Web PDF: 2,399,738 B (< 7 MB). pdfdiff vs issued web PDF: IDENTICAL (weekly word trim `「金融科技」—|「金融科技」`).
- print-vs-web text multiset: rc 0.
- Naive textexp: BYTE-IDENTICAL to the fanout `.text.md.new` (51,308 B).
- Joiner regression (textexp_zh_tw_d5.py v2 on baseline SVG): BYTE-IDENTICAL to fanout.
- Pre-D5 census: `d5_latin_in_cjk` 601 (> 0 — the defect D5 fixes).
- p8 extract 150/150; p8 compare vs baseline core: CLEAN.

## 2. Install

- `_D5_READER = "latin"` (mode latin); routing test FAILURES: 0.
- fix2 retained: `_QUOTE_CLS` ×4, fix2 block ×1, D5 block ×1.
- svglib diff vs baseline: 100 lines (W43 precedent: 100 latin/ru, 142 ja/ko).

## 3. Rebuild (patched)

- run → render → webpdf, `tools/venv/bin/python`; fontconfig warmed (`fc-cache -f`) before the first render.
- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-IT.pdf`: 10,661,736 B, SHA-256 `8311e6503b3fff5e73b6a23aacfdc99c1494c770c3c24fadac84d303d2707ef7`.
- Web PDF `2026-w45-zh-tw-it.web.pdf`: 1,886,583 B (< 7 MB), SHA-256 `e0299352a1e411c95f45985cbaa266fd03d30d7728d860e1cb51162b874ba6c5`.
- Text `2026-w45-zh-tw-it.text.md.new`: 51,314 B, SHA-256 `98077421248f8a99dbc615ac58b8fe91404612052dc941bc997db2a33d6bdae9` (joiner export).

## 4. Gates (18/19 — gate 11 residual, pre-existing; see §6)

| Gate | Result | Detail |
|---|---|---|
| GATE 1 | PASS | run TOTAL 150, 0 FLOW, 0 HEAD |
| GATE 2 | PASS | head_check 0 defects |
| GATE 3 | PASS | d5 census PASS (latin 0, cyrillic 0, curly-in-CJK 0) |
| GATE 4 | PASS | render RC=0, print PDF written |
| GATE 5 | PASS | webpdf RC=0, web 1886583 B <7MB |
| GATE 6 | PASS | occlusion selftest OK, 0 flags |
| GATE 7 | PASS | p8 extract 150/150 |
| GATE 8 | PASS | p8 compare CLEAN (CLEAN [] [] []) |
| GATE 9 | PASS | freeze baseline 8/8 |
| GATE 10 | PASS | freeze diff vs BASE: added CJK 0 (strict-cjk) |
| GATE 11 | FAIL | spill rc=1 |
| GATE 12 | PASS | boxtitle 0 DEFECT (BOXTITLE 2026-w45-zh-tw-it: 40 titles, 451 body lines, 0 DEFECT) |
| GATE 13 | PASS | edge 0 TOUCH 0 NEAR (EDGE_SCAN 2026-w45-zh-tw-it: 8 pages, 0 TOUCH, 0 NEAR) |
| GATE 14 | PASS | creambox PASS 0 defects (selftest OK) |
| GATE 15c | PASS | native verifier ADOPT (all pages) |
| GATE 15a | REFLOW | (accepted, D30) difflines=94 multiset=0 native=ADOPT |
| GATE 15 | PASS | print=web multiset 0 + 15a REFLOW (D30) + 15c native ADOPT |
| GATE 16 | PASS | census_quotes 0 defective |
| GATE D18 | PASS | masthead gaps >0 (see measure-p1.log) |
| GATE D37 | PASS | no P1 line crosses right-box edge (see measure-p1.log) |

- D18 masthead gaps (y=316): min inter-element gap 8.0px (all 10 editions identical) — PASS (> 0).
- D37 P1 lines vs right cream box (left 1439.5): no line starting left of the box crosses its edge; y=612 line absent in this family — PASS.
- P8: 164 lines (baseline 164); footer slack 36.8 px (footer rule y=2596, page bottom 2700).
- Gate 15a: REFLOW (accepted, D30) — whitespace-stripped char multiset diff 0, native verifier ADOPT, difflines 94. Gate 15b shared verifier: baseline rc=1, patched rc=1 (D27 diagnostic, not a gate verdict).

## 5. Fixes

None — first patched rebuild passed all gates; no fix needed.

## 6. Residuals

- Gate 11 spill (1 SPILL, rc=1) — ACCEPTED RESIDUAL, pre-existing, not a D5 defect: P2 box (1439.5, 1092.0, 422.5, 230.0) bottom=1322.0, `BELOW +4.20px x=1461.5 y=1326.2 [SPILL] 'Doppio 11?'`. Baseline run: identical box, line and offset (rc=1). Precedent: PLAN.md L223.

## 7. Re-proof points

- re-check the P2 “Doppio 11?” spill (accepted pre-existing, +4.20px); confirm no wording changed anywhere (multiset diff 0); P8 quiz content unchanged (150/150, compare CLEAN).

## 8. Files (builder originals)

- Print: `patched/2026-w45-zh-tw-it/Lucerna-VOL2-IT.pdf` (10,661,736 B, `8311e6503b3fff5e73b6a23aacfdc99c1494c770c3c24fadac84d303d2707ef7`)
- Web: `patched/2026-w45-zh-tw-it/2026-w45-zh-tw-it.web.pdf` (1,886,583 B, `e0299352a1e411c95f45985cbaa266fd03d30d7728d860e1cb51162b874ba6c5`) — closer copies the original, never re-runs webpdf.
- Text: `logs/2026-w45-zh-tw-it/2026-w45-zh-tw-it.text.md.new` (51,314 B, `98077421248f8a99dbc615ac58b8fe91404612052dc941bc997db2a33d6bdae9`)
- Gates: `logs/2026-w45-zh-tw-it/GATES-SUMMARY.txt` (copy in `production/notes/2026-w45/g-zh-tw/scratch-d5-rebuild-zh-tw/`, `cmp`-verified).
