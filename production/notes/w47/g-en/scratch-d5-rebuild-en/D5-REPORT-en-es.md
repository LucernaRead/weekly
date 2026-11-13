# D5 rebuild report — 2026-w47-en-es (Spanish reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-es/`.

## Install
- `apply_variant.py --target en --reader es` (mode latin) on the edition's own
  `svglib.py`; pre-D5 md5 `05e25a0212a43d2c2298f85791e3c25d`, post-install
  `957a49e191e2ed49c987baba3eb95af6` (identical to core-en's installed svglib).
- Routing unit check (`check_routing.py`, latin): FAILURES: 0; fix2 preserved.

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `6a249cc98f0dea9aa24d6b0af1db9480d9b030164f6ad083e4ff4f01249a70cb`
  (29,331,230 B); web PDF `062f197279be7d94998a93ee89ec107812a96c77733e4edc1b5dee325dd72c67`
  (2,414,451 B); text.md `314b32a3…` (54,385 B).
- Census pre: D5 Latin-in-CJK 544, Cyrillic 0, curly in CJK 0.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P1 dark-band headline `DEMOCRATS WIN BOTH HOUSES!` (46 pt) overlapped the
   Spanish subtitle `Votación del 3 de noviembre…` by 16.2×20.5 px (occlusion TEXTX).
   Fix: `content12.py`, headline size 46 → 44.
2. P1-col1 head `TRY IT NOW　Practica al momento` — HEAD TOO WIDE +16.6 px advance at 25.
   Fix: `content12.py:47`, head size 25 → 23.
3. P6 head `READ THE CHART　Lee el gráfico` — HEAD TOO WIDE +7.9 px advance at 25.
   Fix: `content56.py:112`, head size 25 → 24.
4. P7-col3 head `AN EXAMPLE LETTER　Ejemplo` — HEAD TOO WIDE +3.5 px advance at 25.
   Fix: `content7.py:104`, head size 25 → 24.
5. P1 cream-box title `THE WEEK IN NUMBERS　En cifras` +21.5 px right.
   Fix: `content12.py:43`, `tsize` 23 → 21.
6. P5 cream-box title `ODD SOCKS, IN NUMBERS　Cifras` +6.3 px right.
   Fix: `content56.py:22`, `tsize` 23 → 22.

## Gates (final run, `logs/2026-w47-en-es/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 9, all U+3000; added Latin strings 363 (D5 run-splitting)
- spill 0 SPILL (150 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=466, median 1.003, bold 1.050)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 38,370 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 192 → 202, footer slack 46.8 → 37.3 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-es.pdf`: 28,847,427 B,
  sha256 `78a9edee2ea3bae5d9065e413c436eae18a204d018f25619997a2e90a82f68b0`
- Web PDF `The-Lucerna-VOL4-en-es.web.pdf`: 2,336,646 B (< 7 MB),
  sha256 `0b1c2088a6be102da734a2650fe200fa9efc751e0dfb868314bcbae2143a8abb`
- text.md unchanged: `314b32a3…`, 54,385 B

## KIT
- `WEEKLY-KIT.md` §7 print/web lines updated + D5 rebuild bullet; §9 D5 gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-es/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).

## Process note
- The first stage2 run was killed mid-flight when I edited `stage2_gates.sh` while it
  was running (bash reads the script incrementally — do NOT edit a running script).
  Re-ran stage2 fresh from the clean run.py output; no production file was harmed.
