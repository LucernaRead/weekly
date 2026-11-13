# D5 rebuild report — 2026-w47-en-nl (Dutch reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-nl/`.

## Install
- `apply_variant.py --target en --reader nl` (mode latin) on the edition's own
  `svglib.py`; pre-D5 md5 `b4cb4b20d49cf461461e26faee001da0` (differs from the other
  en editions: this svglib already carried the fix2 port), post-install
  `a691786512a06974721a0734866162c9`.
- Routing unit check (`check_routing.py`, latin): FAILURES: 0; fix2 preserved
  (installer reported "fix2 already present").

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `21e13a74e9d938684fcc941e2caca6a8b22ab3e5aa7deb30f2db044405eea4bd`
  (29,341,219 B); web PDF `c769e979ee69e4d424e34c32bfcc01f1d7b37d64b2c4f8dd4529b29718bbcf1e`
  (2,411,506 B); text.md `30bfb6f9…` (53,565 B).
- Census pre: D5 Latin-in-CJK 545, Cyrillic 0, curly in CJK 0, curly total 168.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P7-col3 head `AN EXAMPLE LETTER　Voorbeeld` — HEAD TOO WIDE +27.1 px advance at 25.
   Fix: `content7.py:104`, head size 25 → 23.
2. P8-battery head `B　MULTIPLE CHOICE　Meerkeuze` — HEAD TOO WIDE +18.6 px advance at 24.
   Fix: `content8.py:44`, head size 24 → 22.
3. P5 cream-box title `ODD SOCKS, IN NUMBERS　Cijfers` +12.3 px right.
   Fix: `content56.py:22`, `tsize` 23 → 21.

## Gates (final run, `logs/2026-w47-en-nl/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 9, all U+3000; added Latin strings 361 (D5 run-splitting)
- spill 0 SPILL (149 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=468, median 1.009, bold 1.049)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 168 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 38,188 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 199 → 178, footer slack 35.9 → 35.9 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-nl.pdf`: 28,841,767 B,
  sha256 `ac22842fe93817981d9402773ada2941447c6ec5983cd6ba5a892ac87b744404`
- Web PDF `The-Lucerna-VOL4-en-nl.web.pdf`: 2,330,974 B (< 7 MB),
  sha256 `ec2c820e7326fd84f02e9afa7cf497dec120b93fb77974b9755de431d80ef6f0`
- text.md unchanged: `30bfb6f9…`, 53,565 B

## KIT
- `WEEKLY-KIT.md` §2 print/web lines updated; §3 D5 rebuild + gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-nl/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
