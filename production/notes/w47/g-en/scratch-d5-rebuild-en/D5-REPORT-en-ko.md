# D5 rebuild report — 2026-w47-en-ko (Korean reader)

Date: 2026-11-12. Worker: D5 rebuild (en family). Logs: `logs/2026-w47-en-ko/`.

## Install
- `apply_variant.py --target en --reader ko` (mode cjk) on the edition's own
  `svglib.py`; post-install md5 `94c5a45c7af4469a7132d62445507781`,
  `_D5_READER = "cjk"` (script-based routing, no `_READER_LANG` gate).
- Routing unit check: `check_routing.py` has no cjk mode, so the latin case set
  was run inline with `_D5_READER == "cjk"` expected — FAILURES: 0; fix2 preserved.
- System python3 carries Pillow 10.2.0 (verified pre-emptively for the ko-freeze
  exception); the freeze gate ran clean under the venv, so the exception was unused.

## Pre-fix baseline (reconstructed — no pre-D5 snapshot existed for CJK editions)
- Print PDF `c892247fe96290e8cc563ff72bdf2bfaa59ef9f73fd0ea0956391e4b4e696158`
  (32,386,301 B); web PDF `e8f6f94a8ed493cbd4d0016ae6cbf0294a392af17d1337749b0897e6d3544a31`
  (2,629,430 B); text.md `08d87476…` (53,587 B).
- Sources: `scratch-delta-en-ko/freeze-baseline-edition/build-copy/` (print/web SHAs
  verified against the KIT-recorded values; the Nov-11 `scratch-fanout-en2/backup/`
  copy is stale — editorial fixes landed after it).
- Census pre: D5 Latin-in-CJK 378, Cyrillic 0, curly in CJK 0 (measured on the delta SVGs).

## Defects found (all D5-caused) and fixes (layout only, text unchanged)
1. P3 cream-box title `HAYMITCH'S GAMES　헤이미치의 경기` +32.9 px right.
   Fix: `content34.py:82`, `tsize` 23 → 20.

## Gates (final run, `logs/2026-w47-en-ko/GATES-SUMMARY.txt`)
- run.py RC=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE
- head_check.py PASS 0 defects
- render.py RC=0; webpdf.py RC=0
- occlusion 0 flags (selftest OK)
- p8 extract noted 60/150 (same set); p8 compare CLEAN, keydiff=[137,138,139,140,150] (expected)
- freeze baseline 8/8; freeze diff vs core-en: added CJK 2,323 (the Korean layer itself —
  Hangul 2,309/2,323 = 99.4%, U+3000 9; same count as the pre-D5 KIT note); added Latin strings 139 (D5 run-splitting)
- spill 0 SPILL (175 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal
- edge 0 TOUCH, 0 NEAR; creambox PASS 0 defects (n=430, median 1.025, bold 1.053)
  — rerun after adding baseline `svglib.py` + `assets/` to the backup dir; the first
  run failed to load the baseline module (FileNotFoundError), not a defect.
- census PASS: D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, Noto Sans elements 0
- U+201C census (`census_quotes.py`): 0 defective (KR quotes not extended, CJK-DECISION §3)
- textcheck PASS: print/web 49,556 chars incl. whitespace (pre-fix 49,708; −152 whitespace-only,
  non-space multiset 34,372 identical pre/post); text.md BYTE-IDENTICAL
- P8: lines 185 → 184, footer slack 44.0 → 37.6 px
- **OVERALL: ALL-GREEN**

## New deliverables
- Print PDF `The-Lucerna-VOL4-en-ko.pdf`: 30,158,892 B,
  sha256 `aef89be3f6bb58b57b56056946fc518414748f72a24df5db76ce6de29b190d0c`
- Web PDF `The-Lucerna-VOL4-en-ko.web.pdf`: 2,534,848 B (< 7 MB),
  sha256 `e5ca78436649c57d7787bcd57721e84eec03406fe2d5821b42fd226e21cd3b2d`
- text.md unchanged: `08d87476…`, 53,587 B

## KIT
- `WEEKLY-KIT.md` §2 print/web lines updated; §3 D5 rebuild + gates bullet added.
- Build-copy cleaned: `logs/2026-w47-en-ko/freeze/build-copy/` removed after ALL-GREEN
  (freeze-baseline.log retains the 8/8 verdict).
