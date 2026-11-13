# GATE-LOG — de-es fix1 (rebuild 5, 2026-11-11)

Fix: D1 only — `content7.py:76` pad 90 → 110 (see FIX-LOG.md §2–§3). Nothing else changed in source.
Build: `tools/venv/bin/python build_edition.py es` (from `scratch-fanout-de/`, 2026-11-11 09:27–09:30 UTC), interpreter `tools/venv/bin/python` (PIL 13.0.0). Driver does NOT re-run transform, so the fix survives. All logs copied into this dir (build/render/webpdf/verify/occlusion/p8extract/p8compare/freeze/export/print.txt/web.txt + fresh freeze-direct/keycheck/boxtitle/d2scan/creambox runs).
Probe: `git hash-object -w` RC=0 before the build and before every write. Disk 77G avail.
Tool versions: `tools/webpdf.py` carries uncommitted changes (90 ins / 17 del, mtime 2026-11-11 09:10:13 UTC, another agent's in-flight D2 patch — UNCHANGED before/after this build, verified by mtime); `freeze.py`/`p8.py`/`occlusion_audit.py` mtimes predate the rebuild wave. Web PDF therefore built with the current working-tree webpdf.py (see note under web PDF).

## New deliverables

| File | Bytes | SHA-256 | vs rebuild 4 |
|---|---|---|---|
| `Die-Lucerna-VOL4-de-es.pdf` | 10,968,798 | `6e8bde3f30a6dcb415321051d0a9f1a19f3a5c033d0167b80215a969aa69077e` | −5 B (P7 geometry only) |
| `Die-Lucerna-VOL4-de-es-web.pdf` | 1,601,888 | `f43d561a2e54de16ffd194ea5f05b1ad9c6c44ef6d60809324cc73e2dfd28d7e` | +43,067 B (Bold subset, see below) |
| `2026-w47-de-es.text.md` | 50,124 | `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` | IDENTICAL (zero content change) |

## Gates (all green)

- `run.py` (build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150. Flow ends identical to rebuild 4 except P7 col3: P1-headline 1554, P1-fussball 2264, P1-quiz 2523, P2-feature 1023, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315, P5-main 1026, P5-ex 2441, P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1374 / B2 1306, **P7 col3 ends 1538.0** (was 1518.0, +20 as designed), P8-battery 1409, P8-keys 2457.
- `render.py` (render.log): exit 0, print PDF 8 pages.
- `webpdf.py` (webpdf.log): exit 0, 1,601,888 B < 7 MB. +43,067 B vs rebuild 4 is the working-tree webpdf.py now embedding `LucernaNewsreader-Bold` (24,224 B; log line `font LucernaNewsreader-Bold: 24224 bytes`) — the same effect the FANOUT-REPORT recorded for pt (+40,050 B), ko (+39,055 B), zh-tw (+39,047 B) when built with the patched tool. Web PDF valid: 8 pages, real text layer, multiset-identical to print (below). Two fontTools cosmetic warnings (fsSelection/macStyle bold bits) only, exit 0.
- `verify.py` (verify.log): exit 0, TOTAL 150 (10/18/18/18/18/18/12/38; A2 69 / B1 67 / B2 14), numbering continuous 1..150 True, SVGs byte-identical after verify run True, SOP 1.1 style audit True (old-style hexes []), verbatim OK (8 phrases 2× each), all 17 forbidden terms [] , P8 answers floor True (min SVG font 13.25 → 9.9375pt), MUSTER 84 words, chart 44+33+23=100, date arithmetic True.
- `tools/occlusion_audit.py` (occlusion.log / occlusion.json): **real run, NO --selftest** — selftest OK (all 6 planted classes fired, clean controls silent), **0 flags**, RC=0, `flag_count: 0`.
- `tools/p8.py extract` (p8extract.log/json): exit 0, **150/150 noted**.
- `tools/p8.py compare` vs core (p8compare.log/json): exit 0, **status CLEAN**, keydiff=[137, 138, 139, 150] (expected translation items only).
- `tools/freeze.py diff` (freeze.log/json): exit 0, TOTAL added CJK **7, all U+3000**, 1 per page P2–P8, 0 on P1.
- `freeze_direct.py es` (freeze-direct.log/json, fresh run into this dir): RC=0, source PASS (0 unaccounted removed/added; 520 removed / 528 added), rendered **8/8** — frozen 147/163/195/166/173/175/150/186, sha `083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7` — **identical to rebuild 4 on all 8 pages**, incl. P3 fc88f676 (Q34 new stem) and P7 b7aa0771 (frozen text unchanged; only box geometry moved). This proves the rebuild changed no text anywhere.
- `keycheck.py es` (keycheck.log / keycheck-150.json, fresh): RC=0, **149/150 exact**; only Q150 extractor truncation (`Tarea libre` vs full key) — expected.
- `boxtitle.py es` (boxtitle.log, fresh): **7/7 fit** (Tranquila 356.5, Palabras 387.6, Consejo 227.0, Adviento 341.4, Útiles 358.8, Cartas 248.2, Una palabra más 380.7; budget 400.5).
- Chips (driver): per page 10/15/18/15/18/18/12/35 = **141**; P8 A2 22 / B1 13 / B2 0.
- Print/web text layer (driver + print.txt/web.txt): pdftotext default — print 51,011 B / web 51,011 B, **word multiset identical** (8,088 words); `-raw` normalised — **exactly identical**, 49,812 B each. (Print bytes 51,012 → 51,011 vs rebuild 4: ±1 B of pdftotext whitespace grouping from the P7 geometry shift; multiset identical.) Web text layer non-empty.
- `d2scan-fix1.py` (d2scan.log / d2-scan.json, fresh): 58 print-abutting span pairs, **0 with web gap > 0.5 pt** (same as proof1).
- P8 minimum span size (PyMuPDF, driver): **9.94 pt** ≥ 9.75 pt floor.

## D1 fix verification (creambox + visual)

- `creambox.py` (this dir), post-fix `svg/p7-sprache.svg`:
  - toolbox: y=330 bottom **803.5**, last baseline 783.9, clearance **+19.6** (was −0.4) ✓
  - LESERBRIEFE: y=820 bottom 1372.0, last baseline 1361.6, clearance +10.4 (unchanged) ✓
  - NOCH EIN WORT: y=1388 bottom **1538.0**, last baseline 1495.1, clearance +42.9 (unchanged) ✓ — 10px before the Sätze rule at y=1548.
- `creambox.py` full edition (`svg/*.svg`): no other negative clearance except the matcher's known false positives (P1 col-3 word-box heading `DAS WORT DER WOCHE` at y=1676, 24px BELOW its box bottom 1652 — a following section head in the same column, inside the matcher's +45 window; P7 BEISPIELE boxes matched against exercise numbers below them). Same rows pre-fix (P1/P7 frozen shas unchanged); occlusion 0 flags + visual proofread confirm they are not defects.
- Visual (renders in this dir: `p7-print.png`, `p7-toolbox-print.png`): P7 viewed at 100 dpi full page + 300 dpi toolbox zoom (print). Last entry `Es ist fraglich, ob ... = aún dudoso` fully inside the cream box (clear cream below the `g` descender); 16px white gap to LESERBRIEFE; NOCH EIN WORT ends with cream below its text and a clear gap to the Sätze rule; no collision, no excess whitespace. Web toolbox zoom is **pixel-identical** to print (sha256 `a73b0ce9…`, same file) — web P7 carries the same fix.
- Q34 (no regression): new singular stem `Am Montag öffnet in Köln der erste ___.` 1× / old plural 0× in content34.py, .text.md, svg/p3-kultur.svg, print text layer, web text layer (all five places).
- Bent quotes: U+201C 66 / U+201D 0 / U+2019 0 / U+201E 66 over SVGs+text.md (33 per set, every 201C paired with 201E in German strings) — same as proof1.
- ABSTRACT.txt: 426 B, one line, Spanish, 0 ASCII double quotes (unchanged).

## Files changed by this rebuild (find -newermt 09:26 UTC)

- `content7.py` (the fix, 1 line), `svg/*.svg` (all 8 re-rendered; freeze_direct shas prove only P7 geometry differs — text identical on all 8 pages), `cards/*.png` (8 re-rendered), both PDFs, `2026-w47-de-es.text.md` (rewritten, byte-identical sha), `__pycache__/content7.*.pyc`.
- NOT touched: any other edition, `core-de/`, `tools/`, `issues/`, `covers/`. No commit, no push, no insert.py, no lint --write.
