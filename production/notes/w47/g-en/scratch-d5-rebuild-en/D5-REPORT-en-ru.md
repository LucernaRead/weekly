# D5 rebuild report — 2026-w47-en-ru (Russian reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-ru/`.

## Install
- `apply_variant.py --target en --reader ru` (mode ru) on the edition's own
  `svglib.py`; post-install md5 `bf16a297b92c275cff1388fff24f73f6`.
- Routing unit check (`check_routing.py`, ru): FAILURES: 0; fix2 preserved.

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `a42edc0e0bd0b7bbcac0163ad70639a1b400cb2cf6df4584db4f544f76c5d594`
  (29,241,520 B); web PDF `588002ff286f0648db8951e08f31a8b0fc4eca56fc20190bf7a32d71ad0b389a`
  (2,452,552 B); text.md `78c1b137…` (62,381 B).
- Census pre: D5 Latin-in-CJK 395, Cyrillic-in-CJK 303, curly in CJK 0.

## Defects found
- **None.** run.py clean on the first run (0 FLOW OVERFLOW, 0 HEAD TOO WIDE);
  no source fix was needed.
- NOTE: PILOT-REPORT §5.4's en-ru P8 "answer key-row collisions ×3" is VOID
  (mechanism-confirmed measurement false positive, occlusion_audit.py
  resolve_font fixed) — no P8 key-row change was made; the (fixed) occlusion
  audit reports 0 flags on the rebuilt edition.

## Gates (final run, `logs/2026-w47-en-ru/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 9, all U+3000; added Latin strings 135 (D5 run-splitting)
- spill 0 SPILL (150 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=472, median 1.008, bold 0.956)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 37,997 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 192 → 203, footer slack 47.8 → 36.3 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-ru.pdf`: 29,097,398 B,
  sha256 `e8c2cc4ef2388d0fbc2b13afb401822935b9e1f792352d6cf7c51b92e482dca3`
- Web PDF `The-Lucerna-VOL4-en-ru.web.pdf`: 2,572,948 B (< 7 MB),
  sha256 `f50ae8fc638cc35a39aea65f352e2d436e667ac3aae703df9bd64f9533e2596d`
- text.md unchanged: `78c1b137…`, 62,381 B

## KIT
- `WEEKLY-KIT.md` §2 print/web lines updated; §3 D5 rebuild + gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-ru/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
