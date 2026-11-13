# GATE LOG — W47 webpdf.py weight patch, ru-en web-PDF rebuild (post-patch verification)

All gates self-run by the patch executor on the rebuilt web PDF.
Interpreter: `~/workspace/weekly-git/tools/venv/bin/python`.
Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`.
Notes dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-webpdf-patch1/`.

## 0. Startup probes — PASSED (2026-11-11 08:33 UTC)

- `echo probe-test | git -C ~/workspace/weekly-git hash-object -w --stdin` → RC=0
- Wrote probe file `scratch-webpdf-patch1/PROBE.txt` — OK
- `df -h`: 45 GB free; no EDQUOT at any point.

## 1. Identity — NEW web PDF, print PDF untouched

- Print `Lucerna-VOL4-ru-en.pdf`: **21,245,374 bytes**, SHA-256
  `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e`, 8 pages —
  identical bytes and SHA before and after the rebuild (verified by `sha256sum`
  immediately before and after the `webpdf.py` run).
- Web `Lucerna-VOL4-ru-en-web.pdf`: **3,367,620 bytes** (was 3,341,905, +0.77%),
  SHA-256 `82dfb6eaeff6eaa7d9851c723404dc27536fd41225804921d2071e522bae65ec`,
  8 pages, < 7 MB ✓.
- No `run.py` / `render.py` re-run was performed in this task, so no print
  output or SVG could have changed.

## 2. Patch verification (fc_match)

- Pre-patch `fc-match`: `Newsreader:style=Bold` → Regular;
  bare `Noto Sans` → Regular; bare `Noto Serif` → Regular.
  Numeric controls: `:weight=200` → SemiBold/Bold, `:weight=100` → Medium.
- Post-patch `webpdf.fc_match`: Newsreader bold → SemiBold, regular → Regular;
  Noto Sans regular → Medium, bold → Bold; Noto Serif regular → Medium,
  bold → Bold. Full table in PATCH-LOG.md §2.
- `git diff -- tools/webpdf.py`: one line changed + 4-line comment, nothing else.

## 3. D2 gaps — 7 spots, all ≤ 0.5 pt (PATCH-LOG.md §4 for the full table)

- P1 headline 4.33 → **0.00**; P4 heading 2.62 → **0.00**;
  P1 contents-1 2.20 → **−0.31**; P4 band-sub 1.94 → **−0.14**;
  P1 contents-3 1.17 → **−0.29**; P5 title 0.91 → **0.00**;
  P7 0.58 → **0.00** (×2). Web gap == print gap at every spot.
- Full abutting-span scan: **1,704 pairs, 0 gaps > 0.5 pt, worst 0.05 pt**
  (P7 16.12 pt). No new gaps.

## 4. Text layer — identical multiset, per page

- `pdftotext` bytes: print 57,149 / web 57,148, both > 0 (`print.txt`, `web.txt`).
- Non-whitespace chars: **30,293 each**; per-page counts identical
  (3078 / 3396 / 2707 / 3357 / 2939 / 2752 / 3580 / 8484);
  character multiset identical overall AND per page (PyMuPDF Counter, 8/8 True).

## 5. Occlusion audit — 42 TEXTX, 0 real flags, flag set identical to fix1

- `--selftest` OK (planted classes fired, clean controls silent).
- Real run (exit code 1 = flags found, per tool semantics):
  **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE**
  (`occlusion.json`, `occlusion.log`).
- Flag set compared with fix1's `occlusion.json`: **identical** — same 42 flags
  (same page/text/overlap). Round-1 pixel adjudication (42/42 CLEAR, known
  systematic false-positive class — audit overestimates the right edge of a
  Cyrillic run by a few px) therefore still applies unchanged; **no new flag
  appeared**. Nothing in this task touches SVGs, so no new occlusion could arise.

## 6. p8 extract + compare — 150/150, CLEAN

- `p8.py extract --p8 svg/p8-test.svg --total 150`: **150/150 noted**
  (`p8-extract.json`).
- `p8.py compare --core-p8 …/core-ru/svg/p8-test.svg --edition-p8 svg/p8-test.svg
  --total 150`: **CLEAN, missing=[], extra_count=0**,
  keydiff=[137, 138, 139, 140] only (the four E translation keys, as expected)
  (`p8-compare.json`, `p8-compare.log`, RC=0).

## 7. Freeze — baseline RC=0, 8/8 byte-identical

- `freeze.py baseline --build . --core-svg svg --out scratch-webpdf-patch1/freeze`:
  RC=0; tool reports OK per file incl. new p5 hash `ae19aec9…`;
  core integrity check: shipped SVGs unchanged by the run.
  (`freeze.log`, `freeze/`).
- Direct SHA-256 comparison shipped `svg/` vs `freeze/build-copy/svg/`:
  **8/8 MATCH** (p1 `1b0e209bab5e`, p2 `c129b99d76d6`, p3 `f0f5733ec71c`,
  p4 `88ddba098a02`, p5 `ae19aec96bc1`, p6 `11482bf79f6e`, p7 `a3462e1d8a62`,
  p8 `acb211760637`).

## 8. KIT updated

- `WEEKLY-KIT.md` §5 (new web-PDF bytes/SHA, pdftotext bytes, patched-rebuild
  record line) + §7 spot-check line and D2 bullet (patch-applied sub-bullet).
  No other edition's KIT touched.

## 9. Git — no writes

- No `git add` / commit / push / stash / reset; no `insert.py`; no `lint --write`.
- Uncommitted by design: ` M tools/webpdf.py` + the two changed files inside the
  untracked edition dir (`Lucerna-VOL4-ru-en-web.pdf`, `WEEKLY-KIT.md`).
  The patch commit is left for the coordinator to arrange as a standalone commit.
