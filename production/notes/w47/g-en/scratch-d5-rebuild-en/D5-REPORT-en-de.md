# D5 rebuild report — 2026-w47-en-de (German reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-de/`.

## Install
- `apply_variant.py --target en --reader de` (mode latin) on the edition's own
  `svglib.py`; pre-D5 md5 `05e25a0212a43d2c2298f85791e3c25d`, post-install
  `957a49e191e2ed49c987baba3eb95af6` (identical to core-en's installed svglib).
- Routing unit check (`check_routing.py`, latin): FAILURES: 0; fix2 preserved.

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `d0d14724442fbcf9d89c5e91a175f263b5aabe5a0f742c5aae013a67a4a8acc2`
  (29,331,210 B); web PDF `2c3ea4ca482d4617caeb93521904cd65feda4c967c1819291a635d929218aa08`
  (2,414,461 B); text.md `c16f0e47…` (52,565 B).
- Census pre: D5 Latin-in-CJK 534, Cyrillic 0, curly in CJK 0.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P7-col3 head `AN EXAMPLE LETTER　Musterbrief` — HEAD TOO WIDE +51.7 px advance
   at size 25 (run.py warning; all other gates miss this class).
   Fix: `content7.py:104`, head size 25 → 22.
2. P5 cream-box title `ODD SOCKS, IN NUMBERS　Zahlen` +15.3 px right
   (boxtitle + creambox agree). Fix: `content56.py:22`, `tsize` 23 → 21.
3. P6 cream-box title `A PRACTICE BALLOT　Stimmzettel` +16.4 px right
   (boxtitle + creambox agree). Fix: `content56.py:106`, `tsize` 23 → 21.

## Gates (final run, `logs/2026-w47-en-de/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 9, all U+3000; added Latin strings 351 (D5 run-splitting)
- spill 0 SPILL (145 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=459, median 1.015, bold 1.049)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 37,789 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 188 → 189, footer slack 35.9 → 35.9 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-de.pdf`: 28,845,194 B,
  sha256 `c7b8f20d9b5a828d963008447c3dfb205b4550b4d4a271a78eb2fc55112ea9dd`
- Web PDF `The-Lucerna-VOL4-en-de.web.pdf`: 2,334,418 B (< 7 MB),
  sha256 `e18adeb766be96acf12e34c38aeef9d4e0db5d1aff57f5a6f0ef8be7e0dc2c5a`
- text.md unchanged: `c16f0e47…`, 52,565 B

## KIT
- `WEEKLY-KIT.md` §7 print/web lines updated + D5 rebuild bullet; §9 D5 gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-de/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
