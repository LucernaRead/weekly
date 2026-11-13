# GATE LOG — 2026-W47 ru-en, Fix 3 (coordinator label "fix2"; re-proof R1+R2)

All gates self-run by the fixer on the fix2 rebuild. Interpreter:
`~/workspace/weekly-git/tools/venv/bin/python`. Edition dir:
`~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`.
Rebuild + all rendering ran in the scratch copy
(`hidden_files/w47/scratch-fix-ru-en2/rebuild/`); the outputs below are the
scratch outputs, promoted to production only after verification (FIX-LOG §6).

## 0. Startup probes — PASSED (2026-11-11)

- `echo test | git hash-object -w --stdin` in the repo → RC=0
  (`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`)
- Wrote probe file `scratch-fix-ru-en2/probe.txt` — OK

## 1. Identity — NEW (fix2) PDFs

- Print `Lucerna-VOL4-ru-en.pdf`: **21,251,270 bytes** (was 21,251,086),
  SHA-256 `d12fa6a6bb62dd7af36743c7d2f33d96d27def054e5dcd6fdb288ef3577c06a1`,
  8 pages (PyMuPDF)
- Web `Lucerna-VOL4-ru-en-web.pdf`: **3,380,903 bytes** (was 3,380,694, < 7 MB),
  SHA-256 `3cd934e01db298f13cd0c492ea14904ce2d5df3860d543818a91b1a4416c1dfe`,
  8 pages
- `.text.md`: 62,816 bytes (was 62,818), 150 exercises, 277 blocks; exactly 1 line
  changed (line 449, P6 box title)

## 2. Build rerun (`run.py` + `render.py` + `webpdf.py` + `ru_textmd.py`)

- `run.py`: exit 0, **0 FLOW OVERFLOW / HEAD TOO WIDE warnings**, TOTAL 150,
  levels A2 50 / B1 76 / B2 24, by page 10/18/18/18/18/18/12/38, by type
  fill-in 54 / multiple choice 42 / matching 20 / sentence building 12 / rewrite 4 /
  cloze 13 / translation 4 / writing 1, model words 97. Log: `gates/run.log`.
- SVG SHA-256 diff vs pre-fix: **only `p6-razbor.svg` changed**
  (`8a7199a6…` → `7ac43e6cbbea02d9e98add07554e17ce415424563be16bcfd610ff92605a2c63`).
  The p6 diff is exactly one run (`　FOR AND AGAINST` → `　FOR &amp; AGAINST`).
- `render.py`: 8 cards + print PDF written in the scratch copy (log: `gates/render.log`).
  Other 7 cards byte-identical to the shipped cards; only `p6-razbor.png` changed.
- `tools/webpdf.py` (shared tool, unmodified): 156 distinct chars; 8 pages;
  WROTE 3,380,903 bytes, **57,316 text bytes**. Log: `gates/webpdf.log`.
- `ru_textmd.py`: 62,816 bytes, 150 exercises, 277 blocks. Log: `gates/textmd.log`.

## 3. R1 verification (triple method, pre vs post)

Pre-fix (shipped PDFs/SVG):
- PIL true ink: 1862.4 svg px, box right 1862.0 → **−0.4 px**
  (`ink-pre.log`; brief: 1862.2 / −0.2 — reproduced within 0.2 px)
- Delivered print-PDF vector char boxes: 1863.5 svg px → **−1.5 px**
  (last char `T` bbox x1=1397.64 pt; `pdf-title-pre.log` — exact match with brief)
- Delivered print-PDF 600 dpi render: rightmost dark pixel 1862.6 svg px →
  **−0.6 px** (ink +3.7 render px past the box edge; `pre-clip.png`)

Post-fix (rebuilt PDFs; production print PDF re-measured after promotion,
`pdf-title-prod.log`, identical numbers):
- PIL true ink: **1829.4 svg px → +32.6 px** (`ink-post.log`)
- Delivered print-PDF vector char boxes: **1830.8 svg px → +31.2 px**
  (last char `T` bbox x1=1373.09 pt)
- Delivered print-PDF 600 dpi render: **1829.9 svg px → +32.1 px**
  (ink ends 200.3 render px inside the box edge; `post-clip.png`)
- Visual: 300 dpi P6-box crops print vs web **byte-identical**
  (SHA prefix `728a0457…`); title read by eye well inside the cream box.
- 32-box-title sweep (`titles-sweep-post.log`): 32 titles, **0 negative
  clearances**; tightest right clearance **+14.1 px** (P1 `В ЭТОМ НОМЕРЕ
  IN THIS ISSUE`); R1 title +32.6 px; S1 title +95.4 px (865.6, reproduced
  exactly); tightest bottom clearance +47.2 px.
- Spill sweep (`spill-post.log`): 32 cream boxes, **0 ink escapes, 0 bad
  titles**, 43 spill-below candidates (same by-design set as fix1).

## 4. R2 verification

- `build_map.py` read: miss-tr overrides tm2 (miss-tr wins, OVERRIDE logged
  on conflict); `tm2-en.json` has no `ТУР В ЦИФРАХ` key (checked directly).
- Pre-fix: `miss-tr-en.json:33` value `ТУР В ЦИФРАХ　The round in numbers`
  (SHA `54afc4c7…`); `map-en.json` lit value already short
  (SHA `400fcdd2…`).
- Post-fix: `miss-tr-en.json:33` value `ТУР В ЦИФРАХ　The round`
  (SHA `9c301611…`, still line 33, valid JSON, 123 lit keys, 0 occurrences
  of the long form).
- `python3 build_map.py en` in the fan-out scratch → rc=0, "map OK", no
  PROBLEMS; regenerated `map-en.json` **byte-identical** (SHA still
  `400fcdd2…`), lit value still short.
  (`snapshot-r2-pre.txt` / `snapshot-r2-post.txt`)

## 5. `check_core.py` (rebuild dir) — GOLDEN 8, BAD 0

- golden BAD 0, gloss fails 0, P8 SVG text 10,561 chars, 1 orphan line-start
  (P7 y553 `”».`, known benign), 1 same-baseline collision (P1 y1712 `чёрная`,
  known). Identical to fix1's record. Log: `gates/check-core.log`.

## 6. p8 extract + compare — 150/150, CLEAN

- `p8.py extract` on new P8 SVG: **150/150** noted (`gates/p8-extract.json`).
- `p8.py compare` vs core-ru P8 SVG: **CLEAN**, missing=[], extra=0,
  keydiff=[137, 138, 139, 140] only (the four E translation keys, as expected)
  (`gates/p8-compare.json`).

## 7. Keycheck — only Q150 differs

- Registry dumped from the scratch rebuild copy (`rebuild/registry.json`,
  150 entries; the dump re-ran the sources — rebuilt SVGs byte-identical
  after, `gates/svg-after-keycheck.txt`). Registry vs P8 extract
  (`gates/keycheck.log`): **149/150 match**; only mismatch is **Q150** —
  registry key `(Open task; model text below)` vs P8 printed `✓` (expected
  for the open writing task).

## 8. freeze — 8/8 byte-identical, RC=0

- `freeze.py baseline --build <core-ru> --core-svg <core-ru>/svg --out gates/freeze-std`:
  RC=0; **8/8 SVGs byte-identical**; "core integrity: shipped core SVGs
  unchanged by the run (8 files re-hashed)" (`gates/freeze-std.log`).
- `freeze.py diff --core-svg core-ru/svg --edition-svg rebuild/svg`
  (`gates/freeze-diff.json/.log`): per-page +/− strings p1 +20/−21, p2 +39/−36,
  p3 +26/−28, p4 +28/−28, p5 +29/−27, p6 +34/−32, p7 +49/−51, p8 +173/−627 —
  identical to fix1; added CJK total 8, all U+3000 (1 per page).
- Adjudication (`gates/freeze-adjudicate.log`): removed distinct **484**
  (per-page sums, fix1's counting; 451 globally deduplicated), count-sum 850,
  added distinct **324** (298 globally); **Cyrillic-bearing removed exactly
  15** = Q46 `можно` ×1 + 14 Morozko-caption words (all P8, image skipped by
  design), unexplained 0; **added Cyrillic-bearing strings 0**;
  P6 added string `　FOR & AGAINST` present, removed long-title string absent.

## 9. Print/web text layer — identical character multiset

- `pdftotext` bytes: print **57,316** / web **57,316**, both > 0, **byte-identical**
  (`cmp` clean, `text/print.txt`, `text/web.txt`). Layout `pdftotext -layout`:
  **111,873 bytes each, byte-identical**.
- `verify_mine2.py` (fix1's script, ED repointed to the rebuild;
  `gates/verify-mine2.log`): page counts 8/8; text multiset identical overall
  (**30,352** non-whitespace chars) and per page; span-text multisets identical
  all 8 pages; abutting span-pair gap diff max **0.00 pt**; intra-span char-pair
  gap diff max **0.00 pt**; D2 6 pinned spots diff **0.000 pt** each; D3
  `а`→`»` gap −2.193 pt both; web embeds both italic faces; P1 italic chars
  16 = print; D1 straight quotes, no curly quotes, both PDFs.
- verify_mine2 reports **1 FAIL: `D3 space 'я'->'п' identical print/web — print
  None web None`**. This is the script's **known finder bug** (documented in
  fix1's FIX-LOG §4.5: it looks for consecutive `я`,`п` and misses the space
  char between them). Corrected direct measurement (`d3_space.py`,
  `gates/d3-space.log`): space bbox **[1145.576, 1266.762, 1148.108,
  1288.725]**, **byte-identical print/web** — exactly fix1's pinned values.
  D3 still fixed; the FAIL is the checker, not the PDFs.

## 10. Occlusion audit — 42 TEXTX, 0 real flags

- `--selftest` OK (planted classes fired, clean controls silent).
- Real run on the rebuild SVGs: **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER,
  0 EDGE, 0 BOXTITLE** (`gates/occlusion.json/.log`).
- Flag set compared with fix1's `gates/occlusion.json`: **identical** (42/42
  flag dicts; only the `svgdir` path differs — rebuild vs production).
- Adjudication (`adjudicate_ru.py`, edition-pointed, `gates/adjudication-ed.log`):
  **42/42 CLEAR, 0 UNRESOLVED** — including the two P8 `ОТВЕТЫ` flags
  (gaps 19 px / 20 px).
- `creambox.py` full 8-page scan (`gates/creambox.log`): 1,156 lines;
  normalized diff vs fix1's scan: exactly **1 line** differs — the P6 title
  line (`FOR AND AGAINST` → `FOR &amp; AGAINST`).

## 11. s11 — FAILURES: none

- `s11_check.py` on the rebuild (via a `2026-w47-ru-en` symlink, removed
  after the run): rc=0, **FAILURES: none**; 8 SVG; paper #fbfaf6;
  no #f7f1e2/#c9a227/#8b4513/#000000; badges A2/B1/B2; foot VOL.4 +
  full-width space; VOL.3 only in P4 correction (×1); masthead 196 px;
  band 46 px; left margin 88.0; no CJK in visible SVG; both PDFs 8 pages;
  web 3,380,903 B < 7 MB; web text > 0; **P8 min font ≥ 9.75 pt: 9.75**.
  Log: `gates/s11.log`.
- P8 min font, direct PyMuPDF on the new print PDF (`gates/p8-minfont.log`):
  **9.75 pt** (411 spans < 10 pt) — identical to fix1.

## 12. Regression — S1 / D1 / D2 / D6 / kicker / Q20 / Q73 survive

- **S1:** P1 title ink right 865.6, clearance +95.4 px (titles sweep);
  p1 SVG byte-identical to pre-fix.
- **D1:** text.md L459 `УЧЕБНЫЕ ДАННЫЕ`, L504 `Три уровня, три темы`,
  L596 `Большой тест недели + все ответы` present; P5 straight quotes in
  both PDFs (verify_mine2 PASS).
- **D2 (Q25):** full phrase `Международный день студента` ×2 in text.md;
  Q25 option L187 intact; 7 D2 spots re-pinned, diff 0.000 pt.
- **D6 (Q20):** `желании` ×2 in text.md; P8 extract key 20 = registry.
- **Q20 / Q73:** Q20 key `желании`; Q73 stem L405 + key list L753 intact,
  P8 extract key 73 = `заказов`.
- **Kicker** (`kicker-post.log`): 9 double-space PIL true-ink gaps
  **[5.0, 5.4, 6.3, 11.8, 8.4, 5.4, 7.2, 9.5, 7.1] px, min 5.0 ≥ 4 — PASS**,
  reproducing fix1's list exactly (kicker SVG byte-identical to fix1's).
- **D3:** space bbox byte-identical (§9); `а`→`»` gap −2.193 pt both.

## 13. VOL + fonts (recorded only)

- `pdffonts` (`gates/fonts-print.log`, `gates/fonts-web.log`): 72 entries each,
  all emb/sub/uni; web embeds Lucerna*-renamed subsets including
  `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`.
- `tools/tables.py vol 2026-W47` → vol 4 (per fix1; KIT §5 foot VOL.4
  re-verified by s11).

## 14. Production zero-write check + KIT updated

- Edition-dir snapshot diff, same filter, pre vs post
  (`snapshot-edition-pre.txt` vs `snapshot-edition-post.txt`): exactly 7 files
  differ — `content56.py`, `svg/p6-razbor.svg`, `cards/p6-razbor.png`,
  print PDF, web PDF, `.text.md`, `WEEKLY-KIT.md`. Everything else
  byte-identical.
- `core-ru` snapshot diff: **identical** (untouched).
- Post-promotion re-measurement on the **production** print PDF
  (`pdf-title-prod.log`): char boxes +31.2 px, rendered pixels +32.1 px —
  identical to the scratch-rebuild measurements.
- `WEEKLY-KIT.md`: §5 outputs (new SHAs/bytes), §5 pdftotext 57,318 → 57,316
  + multiset 30,354 → 30,352, §5 text.md 62,818 → 62,816, §7 print/web
  text-layer line updated, §7 Fix 3 entry added (this round is Fix 3 in the
  KIT; Fix 2 already denotes the S1 fix — coordinator label "fix2" cited).
- No git add/commit/push/stash/reset, no `insert.py`/`lint --write`.
