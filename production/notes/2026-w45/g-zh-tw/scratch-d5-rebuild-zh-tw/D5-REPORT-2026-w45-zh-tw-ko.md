# D5 rebuild report — 2026-w45-zh-tw-ko (W45 zh-tw × ko)

- Week: 2026-W45 (VOL.2). Target: Traditional Chinese (zh-tw). Reader: Korean.
- Core: `production/2026-w45/core-zh-tw/` (en edition doubles as core).
- Builder: scratch `hidden_files/d5-redo/scratch-2026-w45-zh-tw/` (`baseline/` + `patched/`).
- Date: 2026-11-14. Method: D5-METHOD §3 (16 gates + D18 + D37).

## 1. Baseline (pre-D5 rebuild, venv)

- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-KO.pdf`: 15,270,228 B, SHA-256 `27c0fba39dfb422c2b2506b2d4087e0278769f8161fe8920a736b29732605fa0` — matches MANIFEST-W45 §zh-tw-ko print pin byte-for-byte.
- Web PDF: 2,309,670 B (< 7 MB). pdfdiff vs issued web PDF: IDENTICAL (weekly word trim `「金融科技」—|「金融科技」`).
- print-vs-web text multiset: rc 0.
- Naive textexp: BYTE-IDENTICAL to the fanout `.text.md.new` (53,907 B).
- Joiner regression (textexp_zh_tw_d5.py v2 on baseline SVG): BYTE-IDENTICAL to fanout.
- Pre-D5 census: `d5_latin_in_cjk` 286 (> 0 — the defect D5 fixes).
- p8 extract 150/150; p8 compare vs baseline core: CLEAN.

## 2. Install

- `_D5_READER = "cjk"` (mode cjk); routing test FAILURES: 0.
- fix2 retained: `_QUOTE_CLS` ×4, fix2 block ×1, D5 block ×1.
- svglib diff vs baseline: 142 lines (W43 precedent: 100 latin/ru, 142 ja/ko).

## 3. Rebuild (patched)

- run → render → webpdf, `tools/venv/bin/python`; fontconfig warmed (`fc-cache -f`) before the first render.
- run.py: TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE.
- Print PDF `Lucerna-VOL2-KO.pdf`: 12,454,880 B, SHA-256 `21a2ecb8d4e7a3dede08dcfe8e8559e9ba38ff77c74590f56f5445053c7c4f39` (F1 fix rebuild 2026-11-15; builder value was 12,454,544 B, `a443f9fea58c…`).
- Web PDF `2026-w45-zh-tw-ko.web.pdf`: 2,121,041 B (< 7 MB), SHA-256 `416a0f4fb178aba63b324c466c4abb7577192c17d675e396c0edfb8639b5708a` (builder value was 2,120,710 B, `95040ed5d895…`).
- Text `2026-w45-zh-tw-ko.text.md.new`: 53,965 B, SHA-256 `ff9c86522fc81a24931ff5595b6d074ca73b66350abd873d661414927b7574a6` (joiner export; builder value was 53,957 B, `b79c3a7a53f3…`).

## 4. Gates (all green)

| Gate | Result | Detail |
|---|---|---|
| GATE 1 | PASS | run TOTAL 150, 0 FLOW, 0 HEAD |
| GATE 2 | PASS | head_check 0 defects |
| GATE 3 | PASS | d5 census PASS (latin 0, cyrillic 0, curly-in-CJK 0) |
| GATE 4 | PASS | render RC=0, print PDF written |
| GATE 5 | PASS | webpdf RC=0, web 2121041 B <7MB |
| GATE 6 | PASS | occlusion selftest OK, 0 flags |
| GATE 7 | PASS | p8 extract 150/150 |
| GATE 8 | PASS | p8 compare CLEAN (CLEAN [] [] []) |
| GATE 9 | PASS | freeze baseline 8/8 |
| GATE 10 | PASS | freeze diff vs BASE: added CJK 0 (strict-cjk) |
| GATE 11 | PASS | spill 0 (0 SPILL) |
| GATE 12 | PASS | boxtitle 0 DEFECT (BOXTITLE 2026-w45-zh-tw-ko: 47 titles, 1108 body lines, 0 DEFECT) |
| GATE 13 | PASS | edge 0 TOUCH 0 NEAR (EDGE_SCAN 2026-w45-zh-tw-ko: 8 pages, 0 TOUCH, 0 NEAR) |
| GATE 14 | PASS | creambox PASS 0 defects (selftest OK) |
| GATE 15c | FAIL (expected F1 delta) | native verifier rc=1: P1–P7 ADOPT, title ADOPT; P8 MISMATCH, first diff at char 5309, exactly at answer 141 (`4,100원이에요(정가 8,200원)` → `NT$4,100이에요(정가 NT$8,200)`) |
| GATE 15a | REFLOW + F1 delta | (accepted, D30 + F1 fix) difflines=98 (builder 86 + 12 F1 run-split lines) multiset=8 (`N`+2, `T`+2, `$`+2, `원`−2) |
| GATE 15 | FAIL (expected F1 delta) | print=web multiset 0 + 15a REFLOW (D30) + 15c native MISMATCH confined to answer 141 (see §9) |
| GATE 16 | PASS | census_quotes 0 defective |
| GATE D18 | PASS | masthead gaps >0 (see measure-p1.log) |
| GATE D37 | PASS | no P1 line crosses right-box edge (see measure-p1.log) |

- Fix re-run gates total: **PASS=17 FAIL=2** (the two non-PASS lines are GATE 15 and GATE 15c, both the F1 content delta itself measured against the pre-fix baseline对照 — the same "fix verdict 天生带 15a 红" pattern as the es/pt/it fix precedents). All other 17 gates PASS, identical to the builder run.
- D18 masthead gaps (y=316): min inter-element gap 8.0px (all 10 editions identical) — PASS (> 0).
- D37 P1 lines vs right cream box (left 1439.5): no line starting left of the box crosses its edge; y=612 line absent in this family — PASS.
- P8: 167 lines (baseline 167); footer slack 38.9 px (footer rule y=2596, page bottom 2700).
- Gate 15a: REFLOW + F1 delta (accepted, D30 + F1 fix, see §9) — whitespace-stripped char multiset diff 8 vs the pre-fix baseline, exactly the F1 change (`N`+2, `T`+2, `$`+2, `원`−2); native verifier P8 MISMATCH confined to answer 141; difflines 98 (builder 86 + 12 F1 run-split lines); print=web multiset still 0. Gate 15b shared verifier: baseline rc=1, patched rc=1 (D27 diagnostic, not a gate verdict).

## 5. Fixes

**F1 (2026-11-15, reproof finding F1 — the only fix):** ko P8 answer 141 currency unit `4,100원` → `NT$4,100` (and `8,200원` → `NT$8,200` in the list-price parenthesis). `content8.py:77`, applied identically to scratch `patched/` and production; one line only, no other wording changed. Re-export + re-render + full gates re-run, ko only (see §9).

## 6. Residuals

None.

## 7. Re-proof points

- confirm the only wording change is the F1 fix at answer 141 (`content8.py:77`; whitespace-stripped char multiset diff 8, exactly the F1 change); P8 quiz content otherwise unchanged (150/150, compare CLEAN); spot-check P1 masthead and P7 teaser clearance.

## 8. Files (builder originals)

- Print: `patched/2026-w45-zh-tw-ko/Lucerna-VOL2-KO.pdf` (12,454,880 B, `21a2ecb8d4e7a3dede08dcfe8e8559e9ba38ff77c74590f56f5445053c7c4f39`) — F1 fix rebuild; builder value was 12,454,544 B, `a443f9fea58c…`
- Web: `patched/2026-w45-zh-tw-ko/2026-w45-zh-tw-ko.web.pdf` (2,121,041 B, `416a0f4fb178aba63b324c466c4abb7577192c17d675e396c0edfb8639b5708a`) — closer copies the original, never re-runs webpdf; builder value was 2,120,710 B, `95040ed5d895…`
- Text: `logs/2026-w45-zh-tw-ko/2026-w45-zh-tw-ko.text.md.new` (53,965 B, `ff9c86522fc81a24931ff5595b6d074ca73b66350abd873d661414927b7574a6`) — builder value was 53,957 B, `b79c3a7a53f3…`
- Gates: `logs/2026-w45-zh-tw-ko/GATES-SUMMARY.txt` (copy in `production/notes/2026-w45/g-zh-tw/scratch-d5-rebuild-zh-tw/`, `cmp`-verified; fix re-run summary, PASS=17 FAIL=2 with the two non-PASS lines being the expected F1 delta — see §9).

## 9. F1 fix (2026-11-15, reproof F1 — full record)

- **Source verified pre-fix:** `content8.py:77` identical in scratch `patched/` and production (`cmp` clean); baseline `content8.py:77` and the baseline naive export (line 5808) carry the identical wrong line — pre-existing, not D5-introduced. Story text L72 (`4張一共4,100元`), the other 9 editions' answer 141 (no unit), and this edition's own `NT$` usage (arithmetic `NT$2,400 + NT$1,600 = NT$4,000`, `NT$6,200 − NT$1,200 = NT$5,000`, Cathay `NT$13,433`) all confirm `NT$4,100 (정가 NT$8,200)` as the correct value.
- **Change:** `f.ex("B1", "單選", "A", "4장 세트 쿠폰은 4,100원이에요(정가 8,200원).",` → `f.ex("B1", "單選", "A", "4장 세트 쿠폰은 NT$4,100이에요(정가 NT$8,200).",` — one line, currency units + the corresponding Korean particle only; stem, answer letter A, and every other character untouched. `diff` vs baseline `content8.py` is exactly this one line.
- **Rebuild:** run → render → webpdf → joiner textexp from patched, `tools/venv/bin/python`, `fc-cache -f` warmed first; TOTAL 150; new deliverables in §3/§8 above.
- **text.md:** diff vs the builder delivery is exactly one hunk (answer 141): the single line re-exports as 11 run-split lines because `NT$` is a Latin run under D5 routing; whitespace-stripped char multiset diff vs builder text.md is exactly 8 (`N`+2, `T`+2, `$`+2, `원`−2).
- **Gates (full re-run, ko only):** PASS=17 FAIL=2. GATE 15 and GATE 15c are the F1 delta itself against the pre-fix baseline (15a multiset 8, difflines 98 = builder 86 + 12 F1 run-split lines; 15c P8 MISMATCH first diff at char 5309, answer 141 only; print=web multiset 0; 15b rc=1/1 as builder, D27 diagnostic). All other 17 gates PASS. P8 lines 167→167, footer slack 38.9px unchanged; P8 page eyeballed clean, answer 141 in full and in-box.
- **Unmoved proof:** p1–p7 SVG SHA-256 identical to builder `deliverables.json` pins; only `p8-test.svg` changed (`2d3abfb19b0f3817` → `4ea737e0538feff4`, first 16). No other edition touched; no commit/push; scratch not cleared.
- **Fix report:** `hidden_files/d5-redo/FAMILY-W45-ZH-TW-FIX.md`. **Status: fixed, pending independent reproof v2.**
