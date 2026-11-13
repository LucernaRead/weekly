# GATE LOG — 2026-W47 ru-en, independent re-proof of fix2

All gates self-run by the re-proofer on the delivered edition. Interpreter:
`~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13). Edition dir:
`~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`. All builds ran in
the scratch copy (`hidden_files/w47/scratch-reproof-ru-en2/rebuild/`); production
was never written (snapshot diff identical, §14). TMPDIR = own scratch throughout.

## 0. Startup probes — PASSED (2026-11-11)

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → rc=0
  (`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`)
- Real write probe `scratch-reproof-ru-en2/probe.txt` — OK

## 1. Identity — start = close (no change during re-proof)

- Print `Lucerna-VOL4-ru-en.pdf`: **21,251,270 bytes**,
  SHA-256 `d12fa6a6bb62dd7af36743c7d2f33d96d27def054e5dcd6fdb288ef3577c06a1`, 8 pages
- Web `Lucerna-VOL4-ru-en-web.pdf`: **3,380,903 bytes** (< 7 MB),
  SHA-256 `3cd934e01db298f13cd0c492ea14904ce2d5df3860d543818a91b1a4416c1dfe`, 8 pages
- `.text.md`: 62,816 bytes,
  SHA-256 `5ec76132a069d0c1cef7e9abe54d2556ace7419daf308805491b77bb22bfd97d`
- All three match the brief's expected values, measured at start and again at close.

## 2. Build rerun (`run.py` + `render.py` + `webpdf.py` + `ru_textmd.py`, in scratch)

- `run.py`: exit 0, **0 FLOW OVERFLOW / HEAD TOO WIDE warnings**, TOTAL 150,
  levels A2 50 / B1 76 / B2 24, by page 10/18/18/18/18/18/12/38, by type
  fill-in 54 / multiple choice 42 / matching 20 / sentence building 12 / rewrite 4 /
  cloze 13 / translation 4 / writing 1, model words 97. Log: `gates/run.log`.
- SVG SHA-256 diff rebuild vs production: **8/8 byte-identical** (p1–p8, all SAME).
- `render.py`: rc=0, 8 cards (byte-identical to production cards, all 8) + print PDF
  21,251,270 bytes, SHA **identical to production** (`d12fa6a6…`).
- `tools/webpdf.py`: rc=0, 156 distinct chars; WROTE 3,380,888 bytes
  (15 B short of production's 3,380,903 — font-subset randomness, expected),
  **57,316 text bytes** (same as production). Log: `gates/webpdf.log`.
- `ru_textmd.py`: rc=0, 62,816 bytes, 150 exercises, 277 blocks; SHA **identical to
  production** (`5ec76132…`). Log: `gates/textmd.log`.

## 3. R1 verification (triple method, on the DELIVERED print + web PDFs)

- PIL true ink: 1829.4 svg px, box right 1862.0 → **+32.6 px** (`ink-post.log`)
- Delivered print-PDF vector char boxes: 1830.8 svg px → **+31.2 px**
  (last char `T` bbox x1=1373.09 pt; `pdf-title-print.log`)
- Delivered print-PDF 600 dpi render: 1829.9 svg px → **+32.1 px**
  (ink ends 200.3 render px inside the box edge)
- Delivered web PDF, same two measures: **+31.2 px / +32.1 px** (`pdf-title-web.log`)
- Visual: 300 dpi P6-box crops print vs web **byte-identical**
  (SHA `f0957d07…`); title read by eye well inside the cream box.
- 32-box-title sweep (`titles-sweep.log`): 32 titles, **0 negative
  clearances**; tightest right clearance **+14.1 px** (P1 `В ЭТОМ НОМЕРЕ
  IN THIS ISSUE`); R1 title +32.6 px; S1 title +95.4 px (865.6); tightest bottom
  clearance +47.2 px.
- Spill sweep (`spill.log`): 32 cream boxes, **0 ink escapes, 0 bad titles**,
  43 spill-below candidates (same by-design set as fix1/fix2).

## 4. R2 verification

- `build_map.py` read in full: miss-tr overrides tm2 (miss-tr wins, OVERRIDE logged
  on conflict); `tm2-en.json` has 4 buckets and **no** `ТУР В ЦИФРАХ` key.
- `miss-tr-en.json:33` value `ТУР В ЦИФРАХ　The round`
  (SHA `9c301611…`, 123 lit keys, 0 occurrences of the long form);
  `map-en.json` lit value short (SHA `400fcdd2…`).
- `python3 build_map.py en` in my own scratch copy (`r2/`) → rc=0, "map OK", no
  PROBLEMS, `map lit 335 type 8 instr 9 key 8`; regenerated `map-en.json`
  **byte-identical** (SHA still `400fcdd2…`).

## 5. `check_core.py` (production edition dir) — GOLDEN 8, BAD 0

- golden BAD 0, gloss fails 0, P8 SVG text 10,561 chars, 1 orphan line-start
  (P7 y553 `”».`, known benign), 1 same-baseline collision (P1 y1712 `чёрная`,
  known). Log: `gates/check-core.log`.

## 6. p8 extract + compare — 150/150, CLEAN

- `p8.py extract` on rebuild P8 SVG: **150/150** noted (`gates/p8-extract.json`).
- `p8.py compare` vs core-ru P8 SVG: **CLEAN**, missing=[], extra=0,
  keydiff=[137, 138, 139, 140] only (`gates/p8-compare.json`).

## 7. Keycheck — only Q150 differs

- Registry dumped from the scratch rebuild copy (`rebuild/registry.json`,
  150 entries; dump re-ran the sources — rebuilt SVGs re-verified byte-identical
  after, 8/8 SAME). Registry vs P8 extract (`gates/keycheck.log`): **149/150
  match**; only mismatch is **Q150** — registry key `(Open task; model text below)`
  vs P8 printed `✓` (expected for the open writing task).

## 8. Freeze — 8/8 byte-identical, RC=0

- `freeze.py baseline --build <core-ru> --core-svg <core-ru>/svg`:
  RC=0; **8/8 SVGs byte-identical**; "core integrity: shipped core SVGs unchanged
  by the run (8 files re-hashed)" (`gates/freeze-std.log`).
  NOTE: my first baseline attempt returned 0/8 because I passed `--build` the
  rebuild dir instead of core-ru — an invocation error of mine, not a finding;
  the corrected re-run is 8/8 and is the recorded result.
- `freeze.py diff --core-svg core-ru/svg --edition-svg rebuild/svg`
  (`gates/freeze-diff.json/.log`): per-page +/− strings p1 +20/−21, p2 +39/−36,
  p3 +26/−28, p4 +28/−28, p5 +29/−27, p6 +34/−32, p7 +49/−51, p8 +173/−627;
  added CJK total 8, all U+3000 (1 per page).
- Adjudication (`gates/freeze-adjudicate.log`): removed distinct **451**
  (per-page sum 484), count-sum 850, added distinct **298** (per-page sum 324);
  **Cyrillic-bearing removed exactly 15** = Q46 `можно` ×1 + 14 Morozko-caption
  words (all P8, image skipped by design), unexplained 0; **added Cyrillic-bearing
  strings 0**; P6 added string `　FOR & AGAINST` present, removed long-title
  string absent.
- Independent Cyrillic multiset diff (`gates/cyrillic-stems.log`, my own script):
  added Cyrillic strings **0**, removed exactly the same 15; edition visible-SVG
  CJK only U+3000 (123 occurrences).

## 9. Print/web text layer — identical character multiset

- `pdftotext` bytes: print **57,316** / web **57,316**, **byte-identical**
  (`cmp` clean, `text/print.txt`, `text/web.txt`). Layout `pdftotext -layout`:
  **111,873 bytes each, byte-identical**.
- `verify_mine2.py` (rebuild PDFs AND delivered production PDFs;
  `gates/verify-mine2.log`, `gates/verify-mine2-prod.log` — identical verdicts):
  page counts 8/8; text multiset identical overall (**30,352** non-whitespace
  chars) and per page; span-text multisets identical all 8 pages; abutting
  span-pair gap diff max **0.00 pt**; intra-span char-pair gap diff max **0.00 pt**;
  D2 7 pinned spots diff **0.000 pt**; D3 `а`→`»` gap −2.193 pt both; web embeds
  both italic faces; P1 italic chars 16 = print; D1 straight quotes, no curly
  quotes, both PDFs.
- verify_mine2 reports **1 FAIL: `D3 space 'я'->'п' identical print/web — print
  None web None`**. This is the script's **known finder bug** (it looks for
  consecutive `я`,`п` and misses the space char between them). Corrected direct
  measurement (`d3_space.py`, `gates/d3-space.log`): space bbox
  **[1145.576, 1266.762, 1148.108, 1288.725]**, **byte-identical print/web**.
  D3 still fixed; the FAIL is the checker, not the PDFs.

## 10. Occlusion audit — 42 TEXTX; corrected adjudication (SX=1.0)

- `--selftest` OK (planted classes fired, clean controls silent).
- Real run on the production SVGs: **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER,
  0 EDGE, 0 BOXTITLE** (`gates/occlusion.json/.log`; rc=1 = flags found).
- CORRECTED adjudication (`adjudicate_sx10.py`, SX=1.0, same junction-gap logic,
  vs production cards AND delivered print-PDF raster at 96 dpi):
  **37 CLEAR, 5 OVERLAP** (`gates/adjudication-sx10.log`). The old script with
  hardcoded SX=1950/1800 re-run edition-pointed still says 42/42 CLEAR
  (`gates/adjudication-old-sx.log`) — the wrong scale shifts J by up to ~150 px.
  **The old 42/42 must not be cited.**
- The 5 flags, resolved as audit false positives (evidence in
  `gates/occ5-measure.log`, `gates/occ5-pdfchar.log`, `crops/occ-*.png`):
  P1/P4 `Краснодар` » ×4 — PIL true-ink gap **+2.4 px**, delivered-PDF raster
  clear column 1 px, 300 dpi crop visibly separate; P7 `Кипренского` `, 1827` ×1 —
  PIL true-ink gap **+2.3 px**, caption over dark portrait image (pdf raster
  confounded by image highlights), 300 dpi crop visibly separate. All five
  junctions are position-identical in frozen core-ru (inherited, not introduced).
  The two P8 `ОТВЕТЫ` flags are CLEAR on both rasters (card 11/12 px, pdf 13/12 px).
- `creambox.py` full 8-page scan (`gates/creambox.log`): 1,156 lines; P6 title
  line `FOR &amp; AGAINST`.

## 11. s11 — FAILURES: none

- `s11_check.py` on the production edition dir: rc=0, **FAILURES: none**; 8 SVG;
  paper #fbfaf6; no #f7f1e2/#c9a227/#8b4513/#000000; badges A2/B1/B2; foot VOL.4 +
  full-width space; VOL.3 only in P4 correction (×1); masthead 196 px; band 46 px;
  left margin 88.0; no CJK in visible SVG; both PDFs 8 pages; web 3,380,903 B < 7 MB;
  web text > 0; **P8 min font ≥ 9.75 pt: 9.75**. Log: `gates/s11.log`.
- P8 min font, direct PyMuPDF on the delivered print PDF (`gates/p8-minfont.log`):
  **9.75 pt** (411 spans < 10 pt).
- `tables.py vol 2026-W47` → vol 4.

## 12. Regression — S1 / D1 / D2 / D6 / kicker / Q20 / Q73 survive

- **S1:** P1 title ink right 865.6, clearance +95.4 px (titles sweep); p1 SVG
  byte-identical to the fix1-measured version.
- **D1:** text.md L459 `УЧЕБНЫЕ ДАННЫЕ`, L504 `Три уровня, три темы`,
  L596 `Большой тест недели + все ответы` present; P5 straight quotes in both
  PDFs (verify_mine2 PASS).
- **D2 (Q25):** full phrase `Международный день студента` ×2 in text.md = core
  ×2; Q25 option L187 intact; 7 D2 spots re-pinned, diff 0.000 pt.
- **D6 (Q20):** `желании` ×2 in text.md = core ×2; Q20 stem L173 + key list
  L694 intact; P8 extract key 20 = registry.
- **Q73:** stem L405 `73. [B1 · fill-in] В прошлом году сделали 14,4 млн ___. —
  key: заказов` and key list L753 `73. заказов — заказ = an order` intact,
  P8 extract key 73 = `заказов`.
- **Kicker** (`kicker.log`): 9 double-space PIL true-ink gaps
  **[5.0, 5.4, 6.3, 11.8, 8.4, 5.4, 7.2, 9.5, 7.1] px, min 5.0 ≥ 4 — PASS**.
- **D3:** space bbox byte-identical (§9); `а`→`»` gap −2.193 pt both.
- **150 exercises:** registry 150 = P8 extract 150 = text.md 150 exercises
  (277 blocks), same by-page/by-level distribution as fix1.

## 13. VOL + fonts (recorded only; D5 not a gate)

- `pdffonts` (`gates/fonts-print.log`, `gates/fonts-web.log`): 72 entries each,
  all emb/sub/uni; web embeds Lucerna*-renamed subsets including
  `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`. No non-embedded font.

## 14. Production zero-write check

- Edition-dir snapshot diff, same filter and path form, start vs close
  (`snapshot-start.txt` vs `snapshot-end.txt`, 44 files): **identical**.
- `core-ru` snapshot diff: **identical** (untouched).
- Closing triple SHAs identical to opening triple (§1).
- No git add/commit/push/stash/reset, no `insert.py`/`lint --write`.
