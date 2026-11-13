# GATE LOG — 2026-W47 ru-en, Fix 1 (post-fix re-verification)

All gates self-run by the fixer on the fix1 rebuild. Interpreter:
`~/workspace/weekly-git/tools/venv/bin/python`. Edition dir:
`~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`.

## 0. Startup probes — PASSED (2026-11-11 07:59 UTC)

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → RC=0
- Wrote probe file `scratch-fix-ru-en1/PROBE.txt` — OK

## 1. Identity — NEW (fix1) PDFs

- Print `Lucerna-VOL4-ru-en.pdf`: **21,245,374 bytes** (was 21,245,420),
  SHA-256 `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e`,
  8 pages (PyMuPDF)
- Web `Lucerna-VOL4-ru-en-web.pdf`: **3,341,905 bytes** (was 3,341,934, < 7 MB),
  SHA-256 `0c7ebd6ad6f808623228a39b56508d46df2e74fbe16eb89392e325c5aaced46e`,
  8 pages
- `.text.md`: 56,600 bytes (was 56,604), 150 exercises, 203 blocks; exactly 1 line
  changed (line 264, P5 band subtitle)

## 2. Build rerun (`run.py` + `render.py` + `webpdf.py`)

- `run.py`: exit 0, **0 FLOW OVERFLOW / HEAD TOO WIDE warnings**, TOTAL 150,
  levels A2 50 / B1 76 / B2 24, by page 10/18/18/18/18/18/12/38, by type
  fill-in 54 / MCQ 42 / matching 20 / sentence building 12 / rewrite 4 / cloze 13 /
  translation 4 / writing 1, model words 97. Log: `exp/run-fix1.log`.
- SVG SHA-256 diff vs pre-fix: **only `p5-molodezh.svg` changed**
  (`5b66992d…` → `ae19aec96bc1d5ba0caf1cb083ce6ca8bafbe6dca1198ceb8107f4e2c83adb1f`).
  Saved: `exp/svg-before.sha256`, `exp/svg-after.sha256`.
- `render.py`: 8 cards + print PDF written (log: `exp/render-fix1.log`).
- `tools/webpdf.py` (UNPATCHED shared tool): 155 distinct chars; 8 pages;
  WROTE 3,341,905 bytes, **57,196 text bytes**. Log: `exp/webpdf-fix1.log`.

## 3. D1 verification

- P5 band subtitle in BOTH new PDFs: `"Black Friday": sales from 16 November`,
  13.5 pt, identical span boxes (x0=1126.0, x1=1374.5). 4× zoom crop from the new
  print PDF (`exp/p5-band-crop.png`) read: closing straight quote sits tight on
  `:`. PIL: straight `"` advance 6.40 pt vs curly 13.50 pt (1 em).
- U+201C/U+201D rescan over visible `<text>` in all 8 SVGs: **0 on P1–P6, P8;
  2 on P7 only** (the intended Newsreader pair `“` / `”».`, untouched).
  U+2019: **0** on all 8 SVGs. U+2018: 0.
- CJK in visible SVG text: only U+3000 separators (121), no CJK ideographs
  (only CJK elsewhere is `三色蛾` in the moth `<title>` metadata, same as core).

## 4. `check_core.py` (edition dir) — GOLDEN 8, BAD 0

- golden BAD 0, gloss fails 0, P8 SVG text 10,571 chars, 1 orphan line-start
  (P7 y553 `”».`, known benign O1), 1 same-baseline collision (P1 y1712 italic
  «чёрная пятница», known O2). Identical to round-1 record.

## 5. p8 extract + compare — 150/150, CLEAN

- `p8.py extract` on new P8 SVG: **150/150** noted (`p8-extract.json`).
- `p8.py compare` vs core-ru P8 SVG: **CLEAN**, missing=[], extra=0,
  keydiff=[137, 138, 139, 140] only (the four E translation keys, as expected)
  (`p8-compare.json`).

## 6. freeze — 8/8 byte-identical, RC=0

- `freeze.py baseline --build . --core-svg svg --out scratch-fix-ru-en1/freeze`:
  RC=0; tool reports OK per file incl. new p5 hash `ae19aec9…`; core integrity
  check: shipped SVGs unchanged by the run.
- Direct SHA-256 comparison shipped `svg/` vs `freeze/build-copy/svg/`: **8/8 MATCH**.

## 7. Print/web text layer — identical character multiset

- `pdftotext` bytes: print 57,149 / web 57,196, both > 0 (`print.txt`, `web.txt`).
- Non-whitespace chars: **30,293 each; character multiset identical overall AND
  per page** (PyMuPDF per-page counts: P1 3078, P2 3396, P3 2707, P4 3357,
  P5 2939, P6 2752, P7 3580, P8 8484 — equal print vs web on every page).

## 8. Occlusion audit — 42 TEXTX, 0 real flags

- `--selftest` OK (planted classes fired, clean controls silent).
- Real run RC=0: **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE**
  (per-page: P1 10, P2 6, P3 3, P4 7, P5 2, P6 4, P7 8, P8 2) (`occlusion.json`).
- Flag set compared with round-1 `occlusion.json`: **identical** — same 42 flags
  (same page/text/overlap). Both P5 flags are in the article body
  (y=214 `пятница`/`»:`, y=812 `смартфоны`/`,`) — none touches the changed band
  subtitle (y=168). Round-1 pixel adjudication (42/42 CLEAR, known systematic
  false-positive class) therefore still applies unchanged; no new flag appeared.

## 9. P8 min font — 9.75 pt (meets ≥ 9.75 pt)

- PyMuPDF on new print PDF P8: **387 spans at 9.75 pt**; next size 9.98 pt.
  Identical to round-1 measurement.

## 10. VOL + footer

- Visible SVG text: VOL.4 ×9 (masthead + 8 footers), VOL.3 ×1 (P4 correction
  sentence — expected), VOL.5 ×6 (teasers/disclosure — expected).
- `tools/tables.py vol 2026-W47` → vol 4.

## 11. D2 — re-measured on the NEW (fix1) web PDF: STILL PRESENT, unchanged

- Direct span measurements (new web vs new print): P1 headline 39.8 pt gap
  **4.33 pt**; P4 heading 24 pt **2.62 pt**; P1 contents-1 15 pt **2.20 pt**;
  P4 band-sub 13.5 pt **1.94 pt**; P1 contents-3 15 pt **1.17 pt**; P5 title
  24 pt **0.91 pt**; P7 16.12 pt **0.58 pt** ×2. (Scan file: `exp/d2-scan.json`.)
- Root-cause proof and the verified tool-patch proposal are in FIX-LOG.md §2–§3.
  Experiment outputs: `exp/webpdf-weight.py` (v1 copy), `exp/webpdf-weight2.py`
  (v2 copy), `exp/web-weight.pdf`, `exp/web-weight2.pdf`, `exp/core-ru-web-v2.pdf`,
  `exp/probe.svg`, `exp/probe-print.pdf`, `exp/probe-web.pdf`, `exp/probe2.svg`,
  `exp/probe2.pdf`, `exp/p5-band-print.png`, `exp/p5-band-crop.png`.
- Patched-copy (v2) measurements on the new SVGs: **all 7 spots → 0.00 / −0.31 /
  −0.14 / −0.29 pt**; full abutting scan (1,704 pairs) **0 gaps > 0.5 pt**
  (worst 0.05 pt); text multiset == print. Cross-check on core-ru: shipped web
  4 gaps > 0.5 pt (worst 2.62) → patched **0** (worst 0.05), text unchanged.
- `tools/` was NOT modified. The shipped web PDF still carries D2 until the
  coordinator approves the patch and the web PDF is rebuilt with it.

## 12. KIT updated

- `WEEKLY-KIT.md` §5 (new PDF bytes/SHAs, fix1 rebuild note, `.text.md` 56,600 B)
  and §7 (fix1 record: D1 fixed, D2 patch proposal, gates). No
  `EDITION-RECORD.md` exists in the edition dir or nearby (searched); the KIT is
  the edition record.
