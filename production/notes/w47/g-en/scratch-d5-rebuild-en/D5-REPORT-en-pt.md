# D5 rebuild report — 2026-w47-en-pt (Portuguese reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-pt/`.

## Install
- `apply_variant.py --target en --reader pt` (mode latin) on the edition's own
  `svglib.py`; pre-D5 md5 `05e25a0212a43d2c2298f85791e3c25d`, post-install
  `957a49e191e2ed49c987baba3eb95af6` (identical to core-en's installed svglib).
- Routing unit check (`check_routing.py`, latin): FAILURES: 0; fix2 preserved.

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `52452731bc5988209215cb8f83548b14a7d1a933953dac09688e7f8d82a3b700`
  (29,345,708 B); web PDF `b787bd7dcf88dcb148e7e6469b77f76c5206191115f28d7e4ec470ae5db6ade8`
  (2,418,221 B); text.md `f85c55ce…` (54,120 B).
- Census pre: D5 Latin-in-CJK 545, Cyrillic 0, curly in CJK 0.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P6 head `READ THE CHART　Leia o gráfico` — HEAD TOO WIDE +10.1 px advance at 25.
   Fix: `content56.py:112`, head size 25 → 24.
2. P7-col3 head `AN EXAMPLE LETTER　Exemplo` — HEAD TOO WIDE +10.1 px advance at 25.
   Fix: `content7.py:104`, head size 25 → 24.
3. P1 cream-box title `THE WEEK IN NUMBERS　Números` +23.5 px right.
   Fix: `content12.py:43`, `tsize` 23 → 21.
4. P6 cream-box title `HOW LONG?　Duração do mandato` +4.0 px right.
   Fix: `content56.py:171`, `tsize` 23 → 22.

## Gates (final run, `logs/2026-w47-en-pt/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 9, all U+3000; added Latin strings 363 (D5 run-splitting)
- spill 0 SPILL (148 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=467, median 1.003, bold 1.049)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 38,095 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 192 → 192, footer slack 47.8 → 37.8 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-pt.pdf`: 28,850,005 B,
  sha256 `4ecc163c3c669b90c32ec36c5465e5abc93bef8d4071f500b94cb03e1d85da3f`
- Web PDF `The-Lucerna-VOL4-en-pt.web.pdf`: 2,339,191 B (< 7 MB),
  sha256 `dbc0fefb64ab7a9373705e6ed4654dbf7fe77b5f8e1b19a2d290259805e15843`
- text.md unchanged: `f85c55ce…`, 54,120 B

## KIT
- `WEEKLY-KIT.md` §2 print/web lines updated; §3 D5 rebuild + gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-pt/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
