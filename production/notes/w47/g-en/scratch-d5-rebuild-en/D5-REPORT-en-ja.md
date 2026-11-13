# D5 rebuild report — 2026-w47-en-ja (Japanese reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-ja/`.

## Install
- `apply_variant.py --target en --reader ja` (mode cjk) on the edition's own
  `svglib.py`; post-install md5 `794125b17e55a18a1bdeca24c9ef7c73`,
  `_D5_READER = "cjk"` (script-based routing, no `_READER_LANG` gate).
- Routing unit check: `check_routing.py` has no cjk mode, so the latin case set
  was run inline with `_D5_READER == "cjk"` expected — FAILURES: 0; fix2 preserved.

## Pre-fix baseline (reconstructed — no pre-D5 snapshot existed for CJK editions)
- Print PDF `e91ed980047959177588a26c72fff55bc2710c7ce476d631d87d1bcd20c19542`
  (41,509,391 B); web PDF `fb903b2b1da9be8abc04ad40e6387cb6050eaa41bc4c3c63b0eddb07150f48f0`
  (2,883,888 B); text.md `2d498e4e…` (53,585 B).
- Sources: mechanism pilot's `scratch-d5-mech-close/cjk-en-ja/base/` (8/8 SVG
  byte-identical to delivered; base print PDF SHA = KIT-recorded value).
  Pre-fix web SHA is the KIT value (the pilot's base web render differs by 8 B —
  render-level, not content). Pre-fix text extraction from that print PDF.
- Census pre: D5 Latin-in-CJK 380, Cyrillic 0, curly in CJK 0 (pilot `census-base.log`).

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P8-battery head `D　SENTENCES　文の完成と書きかえ` — HEAD TOO WIDE +19.0 px advance at 24.
   Fix: `content8.py:72`, head size 24 → 22.
2. P1 cream-box title `THE WEEK IN NUMBERS　今週の数字` +36.5 px right.
   Fix: `content12.py:43`, `tsize` 23 → 20.
3. P2 cream-box title `THE CALENDAR　今週のカレンダー` +2.8 px right.
   Fix: `content12.py:180`, `tsize` 23 → 22.
4. P3 cream-box title `HAYMITCH'S GAMES　ヘイミッチ戦` +17.8 px right.
   Fix: `content34.py:82`, `tsize` 23 → 21.
5. P5 cream-box title `ODD SOCKS, IN NUMBERS　数字で` +6.3 px right.
   Fix: `content56.py:22`, `tsize` 23 → 22.

## Gates (final run, `logs/2026-w47-en-ja/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 2,084 (the Japanese layer itself); added Latin strings 138 (D5 run-splitting)
- spill 0 SPILL (147 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=435, median 1.012, bold 1.057)
  — rerun after adding baseline `svglib.py` + `assets/` to the backup dir; the first
  run failed to load the baseline module (FileNotFoundError), not a defect.
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- U+201C census (`census_quotes.py`): 0 defective
- textcheck PASS: print/web 49,689 chars incl. whitespace (pre-fix 49,784; −95 whitespace-only,
  non-space multiset 34,522 identical pre/post); text.md BYTE-IDENTICAL
- P8: lines 185 → 185, footer slack 34.6 → 34.6 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-ja.pdf`: 35,187,539 B,
  sha256 `2da1385568476f99b1070fd50dc4878dfe05b38c5844d340524b6458a7dda937`
- Web PDF `The-Lucerna-VOL4-en-ja.web.pdf`: 2,712,817 B (< 7 MB),
  sha256 `e880d0c9370a195f0414e5868119bf9f1bec08916e5da65331b859017bfaf877`
- text.md unchanged: `2d498e4e…`, 53,585 B

## KIT
- `WEEKLY-KIT.md` §2 print/web lines updated; §3 D5 rebuild + gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-ja/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
