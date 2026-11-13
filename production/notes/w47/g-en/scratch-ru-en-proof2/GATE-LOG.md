# GATE LOG — 2026-W47 ru-en, Proof 2 (independent re-verification)

All gates self-run by the proofer on the SHIPPED PDFs (print SHA `7b73070c…`, web SHA `82dfb6ea…`).
Interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PyMuPDF 2.1).
Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`.
Core dir: `~/workspace/weekly-git/production/2026-w47/core-ru/` (the brief's `2026-w47-ru/` does not exist).
Outputs that would normally go to the intended scratch dir went to `/tmp/scratch-ru-en-proof2/`
because `/home` hit EDQUOT at ~08:58 UTC (see PROOF-NOTE.md header). `PYTHONDONTWRITEBYTECODE=1`
was set for all tool runs so no `__pycache__` writes were attempted on `/home`.

## 0. Startup probes — PASSED, then EDQUOT at ~08:58 UTC

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, RC=0 (08:46 UTC)
- Real write probe: `scratch-ru-en-proof2/probe.txt` written OK (08:46 UTC)
- 08:58 UTC: append to `probe.txt` failed: `echo: write error: Disk quota exceeded` (RC=1);
  one re-probe also failed the same way → all `/home` writes stopped immediately per the brief.
- `/tmp` probe: `echo test > /tmp/probe-ru-en-proof2.txt` → OK (tmpfs, 195M free). All subsequent
  scratch writes went to `/tmp/scratch-ru-en-proof2/`.

## 1. Identity — SHA-256 verified (both MATCH)

- `sha256sum Lucerna-VOL4-ru-en.pdf Lucerna-VOL4-ru-en-web.pdf` in the edition dir:
  - print 21,245,374 B, `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e`, 8 pages
  - web 3,367,620 B, `82dfb6eaeff6eaa7d9851c723404dc27536fd41225804921d2071e522bae65ec`, 8 pages
- `pdfinfo` both: 8 pages, 1462.5 x 2025 pts, PDF 1.7, producer pypdf.

## 2. Text layers

- `pdftotext Lucerna-VOL4-ru-en.pdf /tmp/p.txt` → 57,149 B, RC=0
- `pdftotext Lucerna-VOL4-ru-en-web.pdf /tmp/w.txt` → 57,148 B, RC=0
- `diff /tmp/p.txt /tmp/w.txt` → exactly ONE differing line (P1 line 207):
  `«чёрная пятница»` (print) vs `«чёрнаяпятница»` (web). This is D3(a).
- `-layout` extractions to the intended `txt/` dir: print 111,805 B / web 111,804 B (before EDQUOT).

## 3. D2 — 7 original spots re-measured by direct span lookup (PyMuPDF rawdict)

Command: ad-hoc script, spans matched by (page, text) in both PDFs.
Result: print x1 == web x1 at ALL 7 spots → gaps 0.00 pt.
P1 headline `14-` 133.02/133.02; P4 heading `14-` 106.46/106.46; P1 contents `1. 14-`
1138.69/1138.69; P4 band-sub ` все восемь результатов` 1008.74/1008.74 (`+` x0 1008.61 both);
P1 contents `3. «` 1122.22/1122.22; P5 title `«` 80.11/80.11; P7 `«` ×2 1105.61/1105.61.

## 4. Full independent web-vs-print scan (`fullscan.py`, run before EDQUOT)

- `~/workspace/weekly-git/tools/venv/bin/python -W ignore <scratch>/fullscan.py` → RC=0
- Output: `scan.json`, `scan-out.txt` (intended scratch dir).
- Span-text diffs: 1 (D3(a), P1 «чёрная пятница»). Abutting pairs (web−print gap) > 0.5 pt: 1
  (D3(b), +3.354 pt). Intra-span char-pair gap diffs > 0.5 pt: 1 (D3(a) 'я|п', 2.532→1.177).
  Per-page char multiset: P1 spaces 496→495 only; P2–P8 identical. Total chars 35,198→35,197.
- Font census (ad-hoc script): print italic 16 chars (NotoSerif-MediumItalic 14 +
  Newsreader16pt-Italic 2); web italic 0. Web embeds `LucernaNewsreader-Bold` (patch works).

## 5. D3 visual confirmation (3× crops, read by eye)

- `p1-teaser-print.png` vs `p1-teaser-web.png` (clip x1040–1420, y1240–1330, P1):
  print «чёрная пятница» italic + spaced + » tight; web «чёрнаяпятница » upright + joined + » detached.
- `p5-band-print.png` vs `p5-band-web.png` (clip x830–1400, y95–155, P5): band subtitle identical
  in both, straight quotes — D1 confirmed visually in both PDFs.
- `p5-market-print.png`: 'на маркетплейсах скидки' reads with a normal space in print
  (the missing-space-glyph extraction merge is a rendering non-issue there).
- `p1-headline-*.png`: rendered (not needed for the verdict; span numbers already exact).

## 6. D1 + curly-quote sweep

- `grep -n "Black Friday" txt/print.txt txt/web.txt` → line 390 both, straight quotes.
- Visible-`<text>` sweep (ElementTree over `svg/*.svg`): U+201C ×1, U+201D ×1 (P7 y=552.64,
  the intended pair); U+2019 ×0, U+2018 ×0. Same counts in both PDFs' text layers.
- `content*.py` grep: U+201C/U+201D only `content56.py:12` (Russian «Чёрная пятница» guillemets)
  and `content7.py:70` (P7 pair); U+2019 ×0.

## 7. `check_core.py` — GOLDEN 8, BAD 0, RC=0

- `PYTHONDONTWRITEBYTECODE=1 …/venv/bin/python check_core.py .`
- golden BAD: 0; gloss fails: 0; P8 svg text chars: 10,571.
- 1 orphan line-start (P7 y553 `”».`, known benign); 1 same-baseline collision
  (P1 y1712 'чёрная' + ' ', the D3 line).

## 8. p8 extract + compare — 150/150, CLEAN, RC=0

- `tools/p8.py extract --p8 svg/p8-test.svg --total 150 --json /tmp/scratch-ru-en-proof2/p8-extract.json`
  → noted set = 150 of 150, RC=0.
- `tools/p8.py compare --core-p8 <core-ru>/svg/p8-test.svg --edition-p8 svg/p8-test.svg
  --total 150 --json /tmp/scratch-ru-en-proof2/p8-compare.json`
  → `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`, RC=0.
  (First attempt used the brief's `2026-w47-ru/svg/p8-test.svg`, which does not exist — the
  core P8 SVG is at `core-ru/svg/p8-test.svg`. FileNotFoundError, RC=1, corrected path, re-run OK.)

## 9. freeze — baseline 8/8, diff −0 removed, RC=0

- `tools/freeze.py baseline --build . --core-svg svg --out /tmp/scratch-ru-en-proof2/freeze`
  → `baseline: 8/8 SVGs byte-identical`, RC=0; core integrity OK (8 shipped core SVGs unchanged).
  (p5 hash `ae19aec96bc1d5ba…` matches fix1; all 8 hashes listed in the run output.)
- `tools/freeze.py diff --core-svg <core-ru> --edition-svg svg --json /tmp/scratch-ru-en-proof2/freeze-diff.json`
  → per page −0 strings removed (P1–P8); added CJK only U+3000 (121 total). RC=0.

## 10. Occlusion audit — 42 TEXTX, flag set IDENTICAL to fix1, RC=0

- `tools/occlusion_audit.py --selftest` → OK (planted classes fired, clean controls silent), RC=0.
- `tools/occlusion_audit.py --json /tmp/scratch-ru-en-proof2/occlusion.json svg` → RC=0:
  42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE.
- Flag-set comparison vs fix1's `occlusion.json`: IDENTICAL (same 42 flags).
  Round-1 pixel adjudication (42/42 CLEAR, systematic false-positive class) still applies; no new flag.

## 11. Content proofread (manual, print PDF vs core-ru)

- Read `txt/print.txt` P1–P8 end to end (858 lines). All headlines, dates, numbers, exercises
  and keys verified against core-ru (see PROOF-NOTE.md §"Content proofread").
- `.text.md` mechanical comparison (130 exercises both, 0 STEM diffs; key diffs only 137–140 +
  Q150 parser artifact, hand-verified). Model text Q150 = 97 words (98 tokens incl. "Пример:").
- VOL counts (visible SVG text): VOL.4 ×9, VOL.3 ×1, VOL.5 ×6.
  `tools/tables.py vol 2026-W47` → `{"week": "2026-W47", "vol": 4}`.
- P8 min font (PyMuPDF, print PDF P8): 9.75 pt (387 spans), next 9.98 pt — meets ≥ 9.75 pt.
- KIT read-only check: §5/§7 record the patched web PDF (3,367,620 B, SHA `82dfb6ea…`) correctly;
  §7's "character multiset identical" and "1,704 pairs → 0 gaps" claims are contradicted by
  the measurements in §3–§4 above (off by one space; the P1 pair fell out of their matcher).

## 12. NOT done (per the brief / blocked)

- No source edits, no rebuilds, no commit, no push. No changes to core-ru, other editions, `tools/`.
- KIT not edited (read-only check above).
- PROOF-NOTE.md + GATE-LOG.md written to `/tmp/scratch-ru-en-proof2/` (EDQUOT fallback), NOT to
  the intended `hidden_files/w47/scratch-ru-en-proof2/` — that directory is unwritable until the
  home quota is cleared. Files written there before EDQUOT (probe/fullscan/scan/txt/PNGs) remain.
