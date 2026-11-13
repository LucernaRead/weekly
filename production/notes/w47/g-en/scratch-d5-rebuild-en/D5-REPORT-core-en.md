# D5 rebuild report — core-en (Chinese reader, target English)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/core-en/`.

## Install
- `apply_variant.py --target en --reader zh-cn` (mode latin; core-en is the
  zh-cn reader edition) on the edition's own `svglib.py`;
  `_D5_READER = "latin"`; routing unit-checked: `check_routing.py` FAILURES: 0;
  fix2 preserved.
- Installed svglib md5 `957a49e191e2ed49c987baba3eb95af6`.

## Pre-fix baseline (previous worker's snapshot, `logs/`)
- Print PDF `ba7986e6…` (41,407,232 B); web PDF `7341c01e…` (2,804,232 B);
  text.md `23855d4b…` (51,402 B).
- Census pre: D5 Latin-in-CJK 389, Cyrillic 0, curly in CJK 0.

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P1 cream-box title `THE WEEK IN NUMBERS　数字看本周` +36.5 px right.
   Fix: `content12.py`, `tsize` 23 → 20.5.
2. P2 cream-box title `SENATE IN NUMBERS　参议院数字` +1.2 px right.
   Fix: `content12.py`, `tsize` 23 → 22.
3. P3 cream-box title `HAYMITCH'S GAMES　海米奇的比赛` +17.8 px right.
   Fix: `content34.py`, `tsize` 23 → 21.
4. P5 cream-box title `ODD SOCKS, IN NUMBERS　奇袜日` +6.3 px right.
   Fix: `content56.py`, `tsize` 23 → 22.

## Gates (final run, `logs/core-en/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract 150/150, noted 60/150 (same set); p8 compare CLEAN, keydiff=[]
- freeze baseline 8/8; freeze diff N/A (core vs itself)
- spill 0 SPILL (137 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=438, median 1.015, bold 1.057)
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 166 curly in Newsreader, Noto Sans elements 0
- textcheck PASS: print/web 34,112 chars, unchanged vs pre-fix; text.md BYTE-IDENTICAL
- P8: lines 192 → 191, footer slack 40.1 → 41.1 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-zh-cn.pdf`: 30,110,194 B,
  sha256 `99dad9f2ed3775282aefeffc4e1a1d6fdf0f49c8d65b92b6621c4efd12f69e96`
- Web PDF `The-Lucerna-VOL4-en-zh-cn.web.pdf`: 2,605,120 B (< 7 MB),
  sha256 `801597efe2c8b2422ff6419a02dcd2267ed2f04e59bf53f441cf5a0d5354b796`
- text.md unchanged: `23855d4b…`, 51,402 B

## KIT
- `WEEKLY-KIT.md` §7 print/web lines updated (full SHAs incl. web SHA added
  12 Nov 2026 — the web line previously carried no SHA); §9 D5 rebuild + gates bullets added.
- Verified 2026-11-12 (post-completion sweep): production print/web SHAs match
  this report, both SHAs present in the KIT, `svglib.py` contains `_D5_READER`.
