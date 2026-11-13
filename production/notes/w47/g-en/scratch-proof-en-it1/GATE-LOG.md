# GATE LOG — Lucerna Weekly 2026-W47 · en-it · proof1 (round 2, re-fanout #2 rebuild)

**Date:** 2026-11-11 · **Proofreader:** independent proof1 (round 2) · **Conclusion: (a) zero defects (see PROOF-NOTE.md)**
**Scratch:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-it1/`
**Edition:** `~/workspace/weekly-git/production/2026-w47/2026-w47-en-it/`
**Core:** `~/workspace/weekly-git/production/2026-w47/core-en/`
**Round-1 artifacts:** preserved in `round1/` (proof1 round 1, conclusion (b) D1+D2, pre-rebuild). This log is round 2 only; round-2 gate outputs live in `gates2/`, renders in `render2/`, scratch re-render copy in `proof-copy/`.

## 0. Probes (before work)
- `ls /dev/null` → present (`crw-rw-rw- 1 root root 1, 3 Nov 11 13:26 /dev/null`).
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` ✓
- Write probe in goals-side scratch (`PROBE.txt`, "probe-ok 2026-11-11T13:53:58Z") ✓. TMPDIR=`<scratch>/tmp` throughout; `/tmp` (512M) avoided.
- Disk at start: 66G available.

## 1. SHA verification — all MATCH (before and after)
Print PDF `The-Lucerna-VOL4-en-it.pdf`: 29,327,190 B, SHA-256 `bdfe23784024bb85635eb2984dd3c530c2db63aff1b7c102bc08b78b40d7b61c` ✓
Web PDF `The-Lucerna-VOL4-en-it.web.pdf`: 2,408,886 B, SHA-256 `d5e9c1af0880237350b4364d8a4be478673d87d249cd614f334849c969618e58` ✓
text.md `2026-w47-en-it.text.md`: 53,947 B, SHA-256 `433c2aec5b303a5968e535c83b38e6b30128c1b5a2318fb0fa44466f00dbb15e` ✓
Both PDFs 8 pages, 1462.5 × 2025 pts. Re-measured after all proof work: identical.
Core-en before/after (unchanged): print `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`, web `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`, text.md `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`. `git status` on both production dirs: only `??` (untracked) — no production file written by this round.

## 2. Reproducibility — print PDF byte-identical from scratch copy
Copied the edition dir to `proof-copy/` (50M) and re-ran `run.py` + `render.py` there (repo venv python).
- `run.py` RC=0; 0 OVERFLOW / TOO WIDE; flows all within bottoms (P8-keys 2443/2560; P1-headline 1779/1828; P1-countries 2298/2300; P2-feature 1497/1540; P2-ex 2532/2560); TOTAL 150; MODEL 82. Log: `gates2/run.log`.
- `render.py` RC=0; print PDF 29,327,190 B. Log: `gates2/render.log`.
- Re-rendered print PDF SHA-256 = `bdfe23784024bb85635eb2984dd3c530c2db63aff1b7c102bc08b78b40d7b61c` — **byte-identical to production**. All 8 SVGs MATCH production byte-for-byte.

## 3. Registry re-dump — identical
`dump_reg.py` in proof-copy RC=0; re-dumped registry == production `registry.json` (150 entries; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22). Files: `gates2/dump_reg.log`, `gates2/registry-redump.json`.

## 4. Occlusion audit — 0 flags
`tools/venv/bin/python tools/occlusion_audit.py` on proof-copy `svg/`: selftest OK (all 6 planted classes fired, clean controls silent), **0 flags**, RC=0. Files: `gates2/occlusion.log`, `gates2/occlusion.json`.

## 5. p8 extract + compare — CLEAN
`tools/p8.py extract` (core): 60 noted. `extract` (edition, proof-copy SVG): 60 noted. `compare`: **CLEAN**, missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139, 140, 150]. Files: `gates2/p8-extract-core.json/.log`, `gates2/p8-extract.json/.log`, `gates2/p8-compare.json/.log`.

## 6. Keycheck — 149/150 + exception (canonical + independent re-run)
- Canonical `keycheck_ed.py it` RC=0 (`gates2/keycheck.log`): registry-vs-p8extract exact **149/150** exc=[150] mismatch=[]; registry-keys-vs-core 145/150, diff only the 5 expected reader-language keys (137–140, 150); Q38-41 [b,a,d,c]; Q125 A; Q46 A; Q52 hosted; Q55 won; Q82/83/84 B/C/A; noted set == core noted: True; extract keys 150, missing none.
- Independent re-run against MY re-dumped registry + MY p8 extract (`gates2/keycheck-mine.log`): identical figures (149/150 exc=[150]; 145/150 vs core, same 5 diffs; same Q38-41/Q125/Q46/Q52/Q55/Q82-84; noted set == core).

## 7. Freeze — baseline 8/8, diff +9 U+3000
- `freeze.py baseline` (core re-rendered from source) RC=0: **8/8 SVGs byte-identical**, repointed files: none; core integrity re-hash OK. File: `gates2/freeze.log`, build copy in `gates2/freeze-final/`.
- `freeze.py diff` RC=0: per-page +34/-34, +43/-54, +25/-23, +24/-22, +24/-22, +25/-21, +66/-55, +105/-99 strings; **TOTAL added CJK characters: 9, all U+3000** (p1: 2, p2–p8: 1 each). Files: `gates2/freeze-diff.log`, `gates2/freeze-diff.json`.

## 8. Web PDF — scratch-only re-render; production print/web text layers identical
- `webpdf.py` on proof-copy SVGs → `gates2/web-proof.pdf` RC=0: 2,408,870 B, 49,136 text bytes. Its SHA (`610b2c4268e2769024ba9270faaad8aec9ad48f360c72ab036c416d73b7689d1`) differs from production web SHA as the iron rule predicts (fontTools `head.modified` wall-clock); its **text layer is byte-identical** to the production web PDF (47,991 chars). Production web PDF was never written.
- Print/web (production PDFs) via pdftotext: print chars 47,991, web chars 47,991, token-multiset diff **0**, only-in-print [] only-in-web []; per-page byte-identical **8/8** (p1 4974B, p2 5898B, p3 5371B, p4 5858B, p5 4764B, p6 5701B, p7 6324B, p8 10246B). File: `gates2/printweb.log`. (Absolute per-page byte counts differ from the fanout build log's because that log used a different pdftotext invocation; the per-page identical=True + token diff 0 results agree.)

## 9. text.md re-export — byte-identical
`make_textmd_w47.py` repointed (CORE→proof-copy, SCRATCH→gates2 with registry-redump.json, OUT→`gates2/textmd-reexport.md`) RC=0: recorded blocks 498, stub registry 150 = real registry 150, wrote 53,947 B. `cmp` vs production text.md: **byte-identical**, SHA `433c2aec…`. Files: `gates2/make_textmd_w47.py` (original copy), `gates2/make_textmd_proof.py` (repointed copy), `gates2/textmd-reexport.md`, `gates2/textmd.log`.

## 10. check_s11 — ALL PASS
`check_s11.py it` RC=0: colour set core 19 = edition 19, no extra/missing; badges A2 #5c6e30 / B1 #46581f / B2 #37402f present; P8 min SVG font-size 13.5; Q113–120 [A2] tag line; "Levels: 145–149 [A2]"; Q120 [A2] chip OK; WRITING head "H　WRITING　Scrittura [B1]". File: `gates2/check_s11.log`.

## 11. Boxtitle sweeps — 12/12 source, 18/18 SVG, 0 overflows
- Source (`sweep_titles.py it`) RC=0: 12 measured, 0 over budget; tightest HOW LONG? 384.3px margin +20.2; SENATE IN NUMBERS 358.4 +46.1; HAYMITCH'S GAMES 331.9 +72.6; A PRACTICE BALLOT 329.9 +74.6; WHY PERTH? 325.7 +78.8. File: `gates2/boxtitle.log`.
- SVG (`sweep_svg_titles.py it`) RC=0: 18 checked, 0 overflows (incl. SEARCHES 140.8 +259.7; IN THIS ISSUE 310.2 +90.2; MODEL 263.4 +587.6). File: `gates2/boxtitle-svg.log`.

## 12. Creambox (canonical tool) — all inside-only clearances positive
`hidden_files/w47/tools/creambox.py` on production `svg/*.svg` RC=0: 32 boxes. File: `gates2/creambox-all.log`.
- Inside-only lines: 25 boxes; min inside clearance **+5.0px**; min desc-clear −1.0px (one box, adjudicated below); zero inside-only negatives.
- The 21 raw negative "clearance" lines are below-window titles of the next box (tool's known false-positive class); each verified against its inside-only line, which is positive:
  - p1 numbers box −37.0 ('TRY IT NOW') → inside-only +45.7 ('del Senato che cambiano schieramento)')
  - p1 word-of-week box −24.0 → inside-only +48.0 ('p.8')
  - p2/p3/p4/p5/p6/p7/p8 boxes −35.5/−36.0/−37.0 (next section heads or following paragraphs, e.g. 'WHAT IS ON THIS WEEK?', 'FIVE SENTENCES', 'ONE SCREEN, TWO SCREENS', 'READ THE CHART', 'FIFTY ELECTIONS') → all inside-only clearances positive (min across the file +5.0).
- **P2 AND YOU? box (y=1211, bottom=1544.9):** inside-only last baseline 1539.8 clearance +5.0, desc-clear −1.0. Adjudication: the descender allowance is 0.30 × 20pt = 6.0px (1539.85+6.0=1545.85 vs bottom 1544.9 → −0.95 ≈ −1.0). The last line is "redazione." (SVG y=1539.85, x=1461.5, size 20) — letters r,e,d,a,z,i,o,n,e,. contain NO descender (g/j/p/q/y), so the allowance cannot apply. Rendered crop `render2/p2-andyou.png` shows the line fully inside the cream. **Heuristic false alarm, not a defect** (same class as the de edition's recorded AND YOU? false alarm in the fanout report).

## 13. verify_ed — ALL PASS (23/23)
`verify_ed.py it` RC=0: Q39 key a; Q40 key d; Q39 note mentor=a ('mentor = un mentore a'); Q40 note arena=d ("arena = l'arena d"); Q40 note not estadio/stadio; Q46 key A; Q46 note 2025; Q52 hosted; Q55 won; Q125 key A; Q125 note 4-1; registry notes no stale Ashes phrasing; text.md has 150 answers; text.md Q39 a / Q40 d / Q125 A; text.md "Arsenal are winning"; no 'Perth is winning' / 'second week in Perth' / 'Ashes begin'; Ashes retrospective present; P8 min PDF font 10.12pt ≥ 9.75pt; SVG zero real CJK. File: `gates2/verify.log`.

## 14. SAY IT box3 geometry (carry-forward, re-measured)
Source `content12.py:224-232`: `phrase_panel(1200, "Happy Thanksgiving!", "Buon Ringraziamento!")`, default w=280 → rect 1060..1340; glossary `lx = 1370` → **gutter 30px** (was 0px). `svglib.text_w`: "Buon Ringraziamento!" advance 208.2px, span 1095.9..1304.1, margins 35.9px/side; "Happy Thanksgiving!" 210.2px, margins 34.9px/side. SVG ground truth: panels 159–439 / 560–940 / 1060–1340; glossary words x=1370.0; sub x=1095.9. Box2 (w=380): EN 352.1px (margins 14.0), IT 363.6px (margins 8.2) — old D2 spills gone. Visual: `render2/p2-sayit.png`.

## 15. 150-question three-source hand verification
Full read of production `text.md` (1,306 lines) + registry + P8 extract + SVG definitions. All 150 answers checked against stems — **150/150 correct**. All 5 matching sets verified against printed definitions in source AND SVG (P2 Q24–27 b/c/a/d; P3 Q38–41 b/a/d/c; P4 Q56–59 b/c/d/a; P5 Q74–77 d/a/b/c; P8 Q141–144 b/c/d/a). Details in PROOF-NOTE.md. Weekday spot-checks via `date -d` (America/Toronto) all match (Fri 2025-11-21 … Tue 2026-12-01).

## 16. Visual — 8 print pages + web P1/P8 + crops
Rendered from the production print PDF with pdftoppm @110dpi: `render2/p-1.png`…`p-8.png`; web: `render2/w1-1.png`, `w8-8.png` (visually identical to print P1/P8); crops from the proof-copy card: `render2/p2-sayit.png`, `render2/p2-andyou.png`. All 8 pages read: no overlap, no spill, no missing content. Web P1/P8 match print.

## 17. Old-vs-new diff (backup → current)
- Registry: exactly 8 entries differ (Q39, Q40, Q46 note, Q52, Q55, Q82 note, Q84 note, Q125) — all expected core-fix1/edition-fix changes.
- text.md: 66 changed lines, all in expected areas (P1 strip "Risultati annunciati", SEARCHES order, SENATE/SATURDAY titles, Ashes retrospective, SAY IT sub, Q39/40/46/52/55/82/84/125, P7 win/won example, NEXT WEEK).
- SVGs: changed p1, p2, p4, p5, p6, p7, p8 (each with a reason); p3-culture unchanged (definitions identical; key change lives in registry + P8 answers).
- ABSTRACT: old short-form → new full-form (737 B, Lucerna + VOL.4 + 150 + A2–B2).

## 18. Sweeps
- "next Sunday": 0 hits in core-en + en-it + `tools/tables.py` — freeze rule has no applicable object; nothing hard-applied.
- Orphan punctuation: 0 orphan-led lines, 0 lone-opener line-ends; quotes balanced (“ 81/” 81, « 4/» 4, ASCII " 0).
- U+2019: 0 hits in text.md, all 8 SVGs, content*.py, registry.json (61 ASCII straight apostrophes in text.md).
- Internal labels in text.md: only the W46 header boilerplate (lines 5, 1003), byte-identical in core-en — core-inherited convention, not flagged.
- D5 fonts (record only): print PDF 41 objects / 7 families (DejaVuSans ×1, Newsreader16pt-Italic ×1, Newsreader16pt-Regular ×16, NotoSansCJKsc-Bold ×8, NotoSansCJKsc-Regular ×8, NotoSerifCJKsc-Regular ×6, UnifrakturMaguntia ×1); web PDF 41 objects / 8 Lucerna-renamed families. P8 min PDF font 10.12pt ≥ 9.75pt.

## 19. Defects
**None.** No commit, no push.
