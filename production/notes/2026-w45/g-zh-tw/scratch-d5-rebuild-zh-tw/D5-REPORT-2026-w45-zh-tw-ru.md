# D5 rebuild report — 2026-w45-zh-tw-ru (W45 zh-tw × ru)

- Week: 2026-W45 (VOL.2). Target: Traditional Chinese (zh-tw). Reader: Russian.
- Core: `production/2026-w45/core-zh-tw/` (en edition doubles as core).
- Builder: scratch `hidden_files/d5-redo/scratch-2026-w45-zh-tw/` (`baseline/` + `patched/`).
- Date: 2026-11-14. Method: D5-METHOD §3 (16 gates + D18 + D37).

## 1. Baseline (pre-D5 rebuild, venv)

- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-RU.pdf`: 13,573,143 B, SHA-256 `621c481031774e64db62957be91635b86f3872179ffc21bfe3445b7d669d80ad` — matches MANIFEST-W45 §zh-tw-ru print pin byte-for-byte.
- Web PDF: 2,097,395 B (< 7 MB). pdfdiff vs issued web PDF: IDENTICAL (weekly word trim `「金融科技」—|「金融科技」`).
- print-vs-web text multiset: rc 0.
- Naive textexp: BYTE-IDENTICAL to the fanout `.text.md.new` (62,582 B).
- Joiner regression (textexp_zh_tw_d5.py v2 on baseline SVG): BYTE-IDENTICAL to fanout.
- Pre-D5 census: `d5_latin_in_cjk` 275 (> 0 — the defect D5 fixes).
- p8 extract 150/150; p8 compare vs baseline core: CLEAN.

## 2. Install

- `_D5_READER = "ru"` (mode ru); routing test FAILURES: 0.
- fix2 retained: `_QUOTE_CLS` ×4, fix2 block ×1, D5 block ×1.
- svglib diff vs baseline: 100 lines (W43 precedent: 100 latin/ru, 142 ja/ko).

## 3. Rebuild (patched)

- run → render → webpdf, `tools/venv/bin/python`; fontconfig warmed (`fc-cache -f`) before the first render.
- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-RU.pdf`: 11,229,253 B, SHA-256 `170e0e97019a066286b71c9d8993e0f9ca834b6be5a037761eb562cc2739d5b4`.
- Web PDF `2026-w45-zh-tw-ru.web.pdf`: 2,105,259 B (< 7 MB), SHA-256 `6b2f0dfcc103f256ccc720713cd252f124554743d944f727ba5ddc55aaa35569`.
- Text `2026-w45-zh-tw-ru.text.md.new`: 62,687 B, SHA-256 `c12530049243657274dba53e44ca0f1265b4124723056dc5cd27a307c9351f60` (joiner export).

## 4. Gates (18/19 — gate 11 residual, pre-existing; see §6)

| Gate | Result | Detail |
|---|---|---|
| GATE 1 | PASS | run TOTAL 150, 0 FLOW, 0 HEAD |
| GATE 2 | PASS | head_check 0 defects |
| GATE 3 | PASS | d5 census PASS (latin 0, cyrillic 0, curly-in-CJK 0) |
| GATE 4 | PASS | render RC=0, print PDF written |
| GATE 5 | PASS | webpdf RC=0, web 2105259 B <7MB |
| GATE 6 | PASS | occlusion selftest OK, 0 flags |
| GATE 7 | PASS | p8 extract 150/150 |
| GATE 8 | PASS | p8 compare CLEAN (CLEAN [] [] []) |
| GATE 9 | PASS | freeze baseline 8/8 |
| GATE 10 | PASS | freeze diff vs BASE: added CJK 0 (strict-cjk) |
| GATE 11 | FAIL | spill rc=1 |
| GATE 12 | PASS | boxtitle 0 DEFECT (BOXTITLE 2026-w45-zh-tw-ru: 40 titles, 481 body lines, 0 DEFECT) |
| GATE 13 | PASS | edge 0 TOUCH 0 NEAR (EDGE_SCAN 2026-w45-zh-tw-ru: 8 pages, 0 TOUCH, 0 NEAR) |
| GATE 14 | PASS | creambox PASS 0 defects (selftest OK) |
| GATE 15c | PASS | native verifier ADOPT (all pages) |
| GATE 15a | REFLOW | (accepted, D30) difflines=384 multiset=0 native=ADOPT |
| GATE 15 | PASS | print=web multiset 0 + 15a REFLOW (D30) + 15c native ADOPT |
| GATE 16 | PASS | census_quotes 0 defective |
| GATE D18 | PASS | masthead gaps >0 (see measure-p1.log) |
| GATE D37 | PASS | no P1 line crosses right-box edge (see measure-p1.log) |

- D18 masthead gaps (y=316): min inter-element gap 8.0px (all 10 editions identical) — PASS (> 0).
- D37 P1 lines vs right cream box (left 1439.5): no line starting left of the box crosses its edge; y=612 line absent in this family — PASS.
- P8: 164 lines (baseline 156); footer slack 51.4 px (footer rule y=2596, page bottom 2700).
- Gate 15a: REFLOW (accepted, D30) — whitespace-stripped char multiset diff 0, native verifier ADOPT, difflines 384. Gate 15b shared verifier: baseline rc=1, patched rc=1 (D27 diagnostic, not a gate verdict).

## 5. Fixes

- Round 1 gates (2026-11-14): gate 6 occlusion 9 flags + gate 12 boxtitle 2 DEFECT + gate 14 creambox 2 defects (gate 11 spill is a pre-existing residual, §6).
  - P2 [TITLE] +8.5px right: `content12.py:178` “封王優惠　Чемпионские скидки”, 25pt bold, box (1439.5, 1092, 422.5, 250). P5 [TITLE] +7.5px right: `content56.py:78` “天母時間表　Расписание Тяньму”, 25pt bold, box (1439.5, 604, 422.5, 470). Noto Sans is wider than the old CJK face for Cyrillic. Fix: 25→24pt in both `p.text` calls (D5-METHOD §4 head 25→24 pattern; simulated ink_r 1854.5/1852.7 vs box right 1862).
  - P7 occlusion (9 LINEX, teaser vs footer rule): P7 col3 ends 1755.36 → 1839.88 (+84.52px); teaser ends 2553.36 → 2637.88. Three Russian sans texts each wrapped +1 line under Noto Sans: clinic note r[2] 19.5pt, frame `wcn` 20pt, letters `lcn` 20pt. Fix (`patched/2026-w45-zh-tw-ru/content7.py` only, measure + draw sizes together, line-height factors unchanged): clinic r[2] 19.5→19.0 (factor 26.52), wcn 20→19.5 (factor 29), lcn 20→19.5 (factor 29). Simulated wrap counts return to baseline (2/2/6).
- Round 2 gates: 18/19 green — occlusion 0 flags, boxtitle 0 DEFECT, creambox 0 defects. P7 col3 ends back to baseline, teaser ends 2553.36 (footer slack 51.4px). P8 lines 156→164 (D5 run-splitting only), footer slack 36.2→51.4px.

## 6. Residuals

- Gate 11 spill (1 SPILL, rc=1) — ACCEPTED RESIDUAL, pre-existing, not a D5 defect: P3 box (1439.5, 696.0, 422.5, 260.0) bottom=956.0, `BELOW +0.20px x=1461.5 y=956.2 [SPILL] 'песке?'` (sub-pixel). Baseline run: identical box, line and offset (rc=1). Precedent: PLAN.md L223.

## 7. Re-proof points

- re-check the two fixed titles (P2 “Чемпионские скидки”, P5 “Расписание Тяньму” at 24pt) and the P7 teaser band clearance vs the footer rule; confirm no wording changed anywhere (multiset diff 0); P8 quiz content unchanged (150/150, compare CLEAN).

## 8. Files (builder originals)

- Print: `patched/2026-w45-zh-tw-ru/Lucerna-VOL2-RU.pdf` (11,229,253 B, `170e0e97019a066286b71c9d8993e0f9ca834b6be5a037761eb562cc2739d5b4`)
- Web: `patched/2026-w45-zh-tw-ru/2026-w45-zh-tw-ru.web.pdf` (2,105,259 B, `6b2f0dfcc103f256ccc720713cd252f124554743d944f727ba5ddc55aaa35569`) — closer copies the original, never re-runs webpdf.
- Text: `logs/2026-w45-zh-tw-ru/2026-w45-zh-tw-ru.text.md.new` (62,687 B, `c12530049243657274dba53e44ca0f1265b4124723056dc5cd27a307c9351f60`)
- Gates: `logs/2026-w45-zh-tw-ru/GATES-SUMMARY.txt` (copy in `production/notes/2026-w45/g-zh-tw/scratch-d5-rebuild-zh-tw/`, `cmp`-verified).
