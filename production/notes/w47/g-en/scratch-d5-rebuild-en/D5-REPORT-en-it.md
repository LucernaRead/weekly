# D5 rebuild report — 2026-w47-en-it (Italian reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-it/`.

## Install
- `apply_variant.py --target en --reader it` (mode latin) on the edition's own
  `svglib.py`; pre-D5 md5 `05e25a0212a43d2c2298f85791e3c25d`, post-install
  `957a49e191e2ed49c987baba3eb95af6` (identical to core-en's installed svglib).
- Routing unit check (`check_routing.py`, latin): FAILURES: 0; fix2 preserved.

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `2db4dad1496e474fbd01315bf3b7f8393358a60155ce103f6a8bae476a5502a0`
  (29,327,187 B); web PDF `510a03ad52c246a4e4f9b0535197ee96b3c9ab447a79587c1d147793457f78e5`
  (2,408,878 B); text.md `a8330625…` (53,944 B).
- Census pre: D5 Latin-in-CJK 542, Cyrillic 0, curly in CJK 0.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P6 head `READ THE CHART　Leggi il grafico` — HEAD TOO WIDE +26.4 px advance at 25.
   Fix: `content56.py:112`, head size 25 → 23.
2. P7-col3 head `AN EXAMPLE LETTER　Esempio` — HEAD TOO WIDE +8.0 px advance at 25.
   Fix: `content7.py:104`, head size 25 → 24.
3. P1 cream-box title `THE WEEK IN NUMBERS　In cifre` +3.5 px right.
   Fix: `content12.py:43`, `tsize` 23 → 22.

## Gates (final run, `logs/2026-w47-en-it/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 9, all U+3000; added Latin strings 357 (D5 run-splitting)
- spill 0 SPILL (146 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=467, median 1.008, bold 1.050)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 38,207 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 192 → 192, footer slack 47.8 → 37.8 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-it.pdf`: 28,841,334 B,
  sha256 `7efa726326acac745e8140a88791727bc20fb843236d56f3188f938c8be9658f`
- Web PDF `The-Lucerna-VOL4-en-it.web.pdf`: 2,330,533 B (< 7 MB),
  sha256 `681f6184d35e5b107d612fe0f3c6e17f47c30388d6de303eb5237e0f0435dfdc`
- text.md unchanged: `a8330625…`, 53,944 B

## KIT
- `WEEKLY-KIT.md` §2 print/web lines updated; §3 D5 rebuild + gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-it/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
