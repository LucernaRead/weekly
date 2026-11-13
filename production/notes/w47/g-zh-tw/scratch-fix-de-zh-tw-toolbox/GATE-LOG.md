# GATE-LOG — de-zh-tw fix1 (rebuild, 2026-11-11)

Fix: D1 only — `content7.py:76` pad 90 → 110 (see FIX-LOG.md §2–§3). Nothing else changed in source.
Build: `tools/venv/bin/python build_edition.py zh-tw` (from a copy of the fan-out driver in this dir, 2026-11-11 09:41–09:46 UTC), interpreter `tools/venv/bin/python` (PIL 13.0.0). Driver does NOT re-run transform, so the fix survives. All logs in this dir (`zh-tw/` = driver output: build/render/webpdf/verify/occlusion/p8extract/p8compare/freeze/export/print.txt/web.txt + fresh freeze-direct/keycheck/boxtitle/d2scan/creambox runs).
Probe: `git hash-object -w` RC=0 before the build and before every write. /tmp was 100% full — all intermediates in this scratch dir (`TMPDIR=<scratch>/tmp`); nothing written to /tmp, no one else's files touched.
Tool versions: `tools/webpdf.py` clean in git (commit 40963281 "webpdf weight + italic face resolution", mtime 2026-11-11 09:10:13 UTC) — this web PDF embeds the `LucernaNewsreader-Italic` subset (23,908 B; +3,050 B vs rebuild-B, text layer identical). `freeze.py`/`p8.py`/`occlusion_audit.py` carry working-tree modifications predating the rebuild wave (mtimes Nov 10 22:59 / 21:37 / Nov 11 05:01 — same versions as rebuild-B).

## New deliverables

| File | Bytes | SHA-256 | vs rebuild-B |
|---|---|---|---|
| `Die-Lucerna-VOL4-de-zh-tw.pdf` | 23,048,426 | `74faeb9d898e254cd3f27a675063739701a9e40e387bde4b3622be5b7f240545` | +3 B (P7 geometry only) |
| `Die-Lucerna-VOL4-de-zh-tw-web.pdf` | 2,343,141 | `352ead22cee3fc77c56aa5d036015ba3e309679848cbf722a5e11d22ceb296b9` | +3,050 B (Italic subset) |
| `2026-w47-de-zh-tw.text.md` | 49,092 | `fe62ddb59ac6ee2b2c474c7d11019295652e95e3c6bbd22b138fb4c7e798b0f9` | IDENTICAL (zero content change) |

## Gates (all green)

- `run.py` (zh-tw/build.log): exit 0, **zero FLOW OVERFLOW / HEAD TOO WIDE**, TOTAL 150. Flow ends identical to rebuild-B except P7 col3: P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 964, P2-ex 2332, P3-main 886, P3-ex 2333, P4-main 647, P4-ex 2315, P5-main 996, P5-ex 2441, P6-main 747, P6-ex 2523, P7-A2 1278 / B1 1310 / B2 1306, P7 image ends 1541.83, **P7 col3 ends 1480.5** (was 1460.5, +20 as designed), P8-battery 1409, P8-keys 2379.
- `render.py` (zh-tw/render.log): exit 0, print PDF 8 pages.
- `webpdf.py` (zh-tw/webpdf.log): exit 0, 2,343,141 B < 7 MB, 49,905 text bytes. Fonts: Newsreader Regular 21,560 B / Bold 21,596 B / Italic 23,908 B (Italic is new vs rebuild-B, from the committed 40963281 tool change), Noto Sans/Serif CJK TC Regular+Bold, UnifrakturMaguntia 32,852 B. Two fontTools cosmetic warnings (fsSelection/macStyle bold bits) only, exit 0.
- `verify.py` (zh-tw/verify.log): exit 0, TOTAL 150, numbering continuous 1..150 True, SVGs byte-identical after verify run True, SOP 1.1 style audit True (old-style hexes []), verbatim OK (8 phrases 2× each), all forbidden terms [] (17 driver-checked + 桥接), P8 answers floor True (min SVG font 13.25 → 9.9375pt).
- `tools/occlusion_audit.py` (zh-tw/occlusion.log / occlusion.json): **real run, NO --selftest** — selftest OK (all 6 planted classes fired, clean controls silent), **0 flags**, RC=0.
- `tools/p8.py extract` (zh-tw/p8extract.log/json): exit 0, **150/150 noted**.
- `tools/p8.py compare` vs core (zh-tw/p8compare.log/json): exit 0, **status CLEAN**, keydiff=[137, 138, 139, 150] (expected translation items only).
- `tools/freeze.py diff` (zh-tw/freeze.log/json): exit 0, TOTAL added CJK **1,328** (the Traditional-Chinese explanation layer, by design — see KIT §5).
- `freeze_direct.py zh-tw` (freeze-direct.log/json, fresh run into this dir): source level FAIL (same as rebuild-B: exactly the documented TC font-switch unaccounted strings — removed 'Noto Serif CJK SC', added 'Noto Sans CJK TC' / 'Noto Serif CJK TC' / 'TC'), rendered **8/8** — frozen 151/164/206/166/182/176/170/191, sha8 `54c9b51e / 2db0dd83 / ad74f280 / df1bebf7 / b42a8c3d / babfe417 / 9dc31873 / 961dd98a` — **identical to rebuild-B on all 8 pages**, incl. P3 ad74f280 (Q34 new stem) and P7 9dc31873 (frozen text unchanged; only box geometry moved). This proves the rebuild changed no text anywhere.
- `keycheck.py zh-tw` (keycheck.log / keycheck-150.json, fresh): RC=0, **149/150 exact**; only Q150 extractor truncation (`開放任務 — 依寫作框中的要點進行` vs extracted `開放任務`) — expected.
- `boxtitle.py zh-tw` (boxtitle.log, fresh): **7/7 fit** (寧靜的一週 363.6, 聖誕 333.4, 編輯小提示 252.7, 將臨期詞彙 355.4, 工具箱 361.9, 讀者來信 267.3, 再說一句 287.1; budget 400.5).
- Chips (driver): per page 10/15/18/15/18/18/12/35 = **141**; P8 A2 22 / B1 13 / B2 0.
- Print/web text layer (driver + print.txt/web.txt): pdftotext default — print 49,905 B / web 49,905 B, **word multiset identical**; `-raw` normalised — **exactly identical**, 48,777 B each. Web text layer non-empty.
- `d2scan-zh-tw.py` (d2scan.log / d2-scan.json, fresh; adapted from the de-es d2scan with zh-tw paths): 67 print-abutting span pairs, **0 with web gap > 0.5 pt**.
- P8 minimum span size (PyMuPDF, driver): **9.94 pt** ≥ 9.75 pt floor.
- Driver gate summary: all [PASS] except one [FAIL] `export exit 0` on the first run — cause: the scratch copy of `export_text_lang.py` was missing its `stub_svg`/`stub_bslib` modules (copy omission, fixed by copying the stubs from `scratch-fanout-de/`). The export was then re-run twice: first with an empty gloss prefix (shell-quoting failure on the Traditional-Chinese dict key — wrote a wrong 49,052 B file, discarded), then with the correct prefix `註 — ` + NOTE_WRAP `full` → exit 0, text.md byte-identical to rebuild-B (sha `fe62ddb5…`, see export-fix1c.log). The [FAIL] line in `build-fix1.log` is therefore superseded; the export gate is green on the corrected re-run.

## D1 fix verification (creambox + visual)

- `creambox.py` (this dir), post-fix `svg/p7-sprache.svg`:
  - toolbox: y=330 bottom **774.0**, last baseline 754.8, clearance **+19.2** (was −0.8) ✓
  - LESERBRIEFE: y=790 bottom 1314.5, last baseline 1304.4, clearance **+10.1** (unchanged) ✓
  - NOCH EIN WORT: y=1330 bottom **1480.5**, last baseline 1437.6, clearance +42.9 (unchanged) ✓ — 67.5px before the Sätze rule at y=1548.
- `creambox.py` full edition (`svg/*.svg`): diff of pre/post logs = exactly the three col-3 rail rows above; no other negative clearance except the matcher's known false positives (P1 −37.0/−24.0, P7 BEISPIELE −35.0×3 — same rows pre-fix, occlusion 0 flags + visual proofread confirm they are not defects).
- Visual (renders in this dir: `render/p7-print-7.png`, `render/p7-toolbox-print-7.png`, `render/p7-web-7.png`, `render/p7-toolbox-web-7.png`): P7 viewed at 100 dpi full page + 300 dpi toolbox zoom (print). Last entry `Es ist fraglich, ob ... = 是否……尚未確定` fully inside the cream box (clear cream below the text); 16px white gap to LESERBRIEFE; NOCH EIN WORT ends with a clear gap to the Sätze rule; no collision, no excess whitespace. Web toolbox zoom is **pixel-identical** to print (sha256 `f7960a4d228595a8ffe831dd72d3a1f0399b19a27178c9e406f8d57a26850fe7`, same file) — web P7 carries the same fix.
- Q34 (no regression): new singular stem `Am Montag öffnet in Köln der erste ___.` 1× / old plural stem `Am Montag öffnen in Köln die ersten ___.` 0× in content34.py, .text.md, svg/p3-kultur.svg, print text layer, web text layer (all five places). (The string `öffnen in Köln die ersten` still occurs in the P3 article sentence "Am Montag, dem 16. November, öffnen in Köln die ersten Weihnachtsmärkte…" — legitimate article text, not the Q34 stem.)
- Bent quotes: U+201C 66 / U+201D 0 / U+2019 0 / U+201E 66 over SVGs+text.md (33 per set, every 201C paired with 201E in German strings) — same as rebuild-B.
- ABSTRACT.txt: 294 B, one line, Traditional Chinese, 0 ASCII double quotes (unchanged).

## Files changed by this rebuild (find -newermt 09:30 UTC)

- `content7.py` (the fix, 1 line), `svg/*.svg` (all 8 re-rendered; freeze_direct shas prove only P7 geometry differs — text identical on all 8 pages), `cards/*.png` (8 re-rendered), both PDFs, `2026-w47-de-zh-tw.text.md` (rewritten, byte-identical sha), `__pycache__/content7.*.pyc`.
- `WEEKLY-KIT.md` (§2 fix1 deliverables + Status + §7 fix1 entry + new §8).
- NOT touched: any other edition, `core-de/`, `tools/`, `issues/`, `covers/`. No commit, no push, no insert.py, no lint --write.
