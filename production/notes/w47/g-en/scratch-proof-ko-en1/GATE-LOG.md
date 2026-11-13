# GATE LOG — W47 ko-en proof1 (independent re-runs, 2026-11-11)

Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-en/`
Core dir: `~/workspace/weekly-git/production/2026-w47/core-ko/`
All tools run from `~/workspace/weekly-git/tools/` with `tools/venv/bin/python` unless noted. No writes to the edition dir; outputs in this scratch dir (`work/`).

| Gate | Command / method | Result |
|---|---|---|
| Hashes | `sha256sum` both PDFs | print 571699d6…cc18 (45,262,664 B) ✓; web 02203d24…4323 (4,013,441 B) ✓ — match brief |
| U+2019 scan | count U+2019 in 8 SVGs + text.md + ABSTRACT.txt | **0 everywhere ✓** |
| U+201C/U+201D scan | count in same files | **FAIL: U+201C ×2, U+201D ×2, all in p7-mal.svg** (frame gloss line, Noto Sans CJK KR); core 0/0 on all pages — see PROOF-NOTE D1 |
| Hanzi residual | CJK Unified chars inside `<text>` per SVG | 0 total ✓ |
| Occlusion audit | `occlusion_audit.py <svg>` | selftest OK (6 classes fired, clean controls silent); **0 flags** ✓ — `work/occlusion-proof1.json`, `.log` |
| p8 extract | `p8.py extract --p8 …/p8-siheom.svg --total 150` | **150/150 noted** ✓ — `work/p8-extract-proof1.log`, `p8-proof1.json` |
| p8 compare | `p8.py compare --core-p8 … --edition-p8 … --total 150` | **CLEAN**, missing=[] extra=0, keydiff=[137, 138] (expected re-aiming) ✓ — `work/p8-compare-proof1.log` |
| Freeze baseline | `/usr/bin/python3 freeze.py baseline --build <ed> --core-svg <ed>/svg --out work/freeze-proof1` | **8/8 byte-identical**; hashes match KIT exactly (p1 b7143ff1…, p8 4ee95a38…) ✓ — log `work/freeze-baseline-proof1.log` (build-copy dir deleted after EDQUOT cleanup; log retained) |
| Freeze diff | `freeze.py diff --core-svg core/svg --edition-svg ed/svg` | added CJK **7, all U+3000** (1/page on P2–P8) ✓ — `work/freeze-diff-proof1.log/.json` |
| Text layers | `pdftotext` print vs web + `cmp` | **50,698 bytes each, byte-identical** ✓; all 8 pages non-empty in both PDFs — `work/print.txt`, `work/web.txt` |
| P8 min font | PyMuPDF min span size on P8, print + web | **9.975pt both** ≥ 9.75pt ✓ |
| Boxtitles | `/usr/bin/python3 boxtitle-ko.py <ed>` | **8/8 ≤ 386.5px** (336.5 / 373.1 / 330.1 / 329.0 / 358.4 / 236.6 / 359.9 / 312.1) ✓ |
| 150-key re-derivation | manual, stem-by-stem vs P1–P7 + P8 key (see PROOF-NOTE) | **150/150**; numbering continuous; levels A2 51 / B1 72 / B2 27 recounted from SVG badges ✓ |
| Visual | 8 print pages @110dpi (pages-print/p1–p8.png) + 300dpi crops (work/p7-frame-zoom.png, work/p1-dropcap-zoom.png) | 8/8 clean layout; D1 visible in P7 zoom (full-width quotes) |
| Print vs web | 72dpi pixel diff, all 8 pages | mean abs diff ≤ 0.47/page (P6 0.00); layout identical ✓ |
| Text.md | read in full; diffed structurally vs core text.md | 332 items; gaps (F 2nd term, D stems, P8 key lines, "All") identical in core — exporter quirk, not a defect |
| ABSTRACT.txt | read; ASCII `"` count | 1 line, 0 ASCII double quotes, all required elements ✓ |

## Disk incident
- While writing PROOF-NOTE.md: `Disk quota exceeded (os error 122)` (EDQUOT; `df` showed 7.4G free — quota, not disk-full).
- Action per task: stopped, deleted ONLY my own reproducible intermediates in this note dir — `work/freeze-proof1/` (68M, regenerable via freeze baseline) and `pages-web/` (11M, regenerable from the web PDF). Retried the write once — succeeded. Note dir now 11M. No other files touched.
