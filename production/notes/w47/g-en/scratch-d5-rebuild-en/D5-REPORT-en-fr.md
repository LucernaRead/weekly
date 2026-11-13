# D5 rebuild report — 2026-w47-en-fr (French reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-fr/`.
Pilot reference: `scratch-d5-plan/mechanism/PILOT-REPORT.md` §5 — all 4 predicted
defects reproduced exactly (same pages, same values) and fixed.

## Install
- `apply_variant.py --target en --reader fr` (mode latin) on the edition's own
  `svglib.py`; pre-D5 md5 `05e25a0212a43d2c2298f85791e3c25d`, post-install
  `957a49e191e2ed49c987baba3eb95af6` (identical to core-en's installed svglib).
- Routing unit check (`check_routing.py`, latin): FAILURES: 0; fix2 preserved.

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `0b4fded62123ee39ec97b8d4b7abd9c5c8e1f41184500a0aa76c25ee2678c693`
  (29,330,985 B); web PDF `bc56eabd68ee1e62739d60dfc15952ad154429c09de109f36d809ee8430beb1b`
  (2,413,669 B); text.md `ed8fd9ec…` (53,806 B).
- Census pre: D5 Latin-in-CJK 545, Cyrillic 0, curly in CJK 0.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P1 dark-band headline `DEMOCRATS WIN BOTH HOUSES!` (46 pt) overlapped the
   French subtitle `Vote du 3 novembre…` by 12.9×20.5 px (occlusion TEXTX).
   Fix: `content12.py`, headline size 46 → 44.
2. P7-col3 head `AN EXAMPLE LETTER　Exemple` — HEAD TOO WIDE +8.6 px advance at 25.
   Fix: `content7.py:104`, head size 25 → 24.
3. P8-battery head `D　SENTENCES　Phrases à former` — HEAD TOO WIDE +1.2 px advance at 24.
   Fix: `content8.py:72`, head size 24 → 23.
4. P1 cream-box title `THE WEEK IN NUMBERS　Chiffres` +12.5 px right.
   Fix: `content12.py:43`, `tsize` 23 → 21.
5. P5 cream-box title `ODD SOCKS, IN NUMBERS　Chiffres` +28.3 px right.
   Fix: `content56.py:22`, `tsize` 23 → 21.
6. P6 cream-box title `A PRACTICE BALLOT　Bulletin test` +16.4 px right.
   Fix: `content56.py:106`, `tsize` 23 → 21.

## Gates (final run, `logs/2026-w47-en-fr/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 9, all U+3000; added Latin strings 362 (D5 run-splitting)
- spill 0 SPILL (145 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=467, median 1.003, bold 1.049)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 38,213 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 197 → 191, footer slack 35.3 → 35.9 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-fr.pdf`: 28,846,712 B,
  sha256 `abb14dde411a781141733afeacdbe88327787dd50906dc2f0a128bdcc742ef52`
- Web PDF `The-Lucerna-VOL4-en-fr.web.pdf`: 2,335,922 B (< 7 MB),
  sha256 `bae85a6819662c47627561fde036b63c282cc491186871bd94e50dd9a09372bf`
- text.md unchanged: `ed8fd9ec…`, 53,806 B

## KIT
- `WEEKLY-KIT.md` §7 print/web lines updated + D5 rebuild bullet; §9 D5 gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-fr/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
