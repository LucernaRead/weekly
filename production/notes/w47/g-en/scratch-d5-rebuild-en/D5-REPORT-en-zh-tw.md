# D5 rebuild report — 2026-w47-en-zh-tw (Traditional Chinese reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-zh-tw/`.

## Install
- `apply_variant.py --target en --reader zh-tw` (mode cjk) on the edition's own
  `svglib.py`; post-install md5 `c2e7af2d9b3a4d43b78ed92124e37fff`,
  `_D5_READER = "cjk"` (script-based routing, no `_READER_LANG` gate).
- Routing unit check: `check_routing.py` has no cjk mode, so the latin case set
  was run inline with `_D5_READER == "cjk"` expected — FAILURES: 0; fix2 preserved.

## Pre-fix baseline (snapshotted from production immediately before the install)
- Print PDF `854d0943264c0821842da52d75585a5eeaaf537b371e0148d22bfab7a1853468`
  (38,152,349 B); web PDF `09121c22b92825030144b14409802681dedd96491eac3cf02b8b00770bee8085`
  (2,965,195 B); text.md `cf12ebfe…` (51,144 B).
  (The KIT web line read 2,965,206 B / `e6e9f859…` — stale; the disk-measured value
  taken minutes before the install is authoritative.)
- Census pre: D5 Latin-in-CJK 374, Cyrillic 0, curly in CJK 0.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P1 cream-box title `THE WEEK IN NUMBERS　數字看本週` +36.5 px right.
   Fix: `content12.py:43`, `tsize` 23 → 20.
2. P2 cream-box title `SENATE IN NUMBERS　參議院數字` +1.2 px right.
   Fix: `content12.py:175`, `tsize` 23 → 22.
3. P3 cream-box title `HAYMITCH'S GAMES　海米奇的比賽` +17.8 px right.
   Fix: `content34.py:82`, `tsize` 23 → 21.
4. P5 cream-box title `ODD SOCKS, IN NUMBERS　奇襪日` +6.3 px right.
   Fix: `content56.py:22`, `tsize` 23 → 22.

## Gates (final run, `logs/2026-w47-en-zh-tw/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,150] (omits 140 — expected for this edition, script-identical key)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 775 (the Traditional layer itself); added Latin strings 132 (D5 run-splitting)
- spill 0 SPILL (135 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=425, median 1.015, bold 1.057)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- U+201C census (`census_quotes.py`): 0 defective
- textcheck PASS: print/web 47,680 chars (pre-fix 47,829; −149 whitespace-only,
  non-space multiset 33,932 identical pre/post); text.md BYTE-IDENTICAL
- P8: lines 184 → 182, footer slack 34.6 → 35.6 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-zh-tw.pdf`: 30,215,246 B,
  sha256 `44dcb76d240a890d1e603e31fc835bd209f70d144fe491703bb860d9189e5a67`
- Web PDF `The-Lucerna-VOL4-en-zh-tw.web.pdf`: 2,701,246 B (< 7 MB),
  sha256 `6353e45069479048b87647895eb330c22d9afa6d369c024e0f5c6475f0abc061`
- text.md unchanged: `cf12ebfe…`, 51,144 B

## KIT
- `WEEKLY-KIT.md` §2 print/web lines updated; §3 D5 rebuild + gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-zh-tw/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
