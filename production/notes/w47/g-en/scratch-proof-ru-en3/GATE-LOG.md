# GATE LOG — proof 3 (independent), 2026-W47 ru-en

All gates self-run by proof3 on the SHIPPED files (no rebuild, no source edit).
Interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (PyMuPDF 2.1).
Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`.
Core dir: `~/workspace/weekly-git/production/2026-w47/core-ru/`.
Scratch dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-en3/`
(`PYTHONDONTWRITEBYTECODE=1` on all tool runs; `echo test | git -C ~/workspace/weekly-git
hash-object -w --stdin` → `9daeafb…`, RC=0, re-run before every write step).

## 0. Identity — SHA-256 verified (before AND after all gates)

- print `Lucerna-VOL4-ru-en.pdf`: 21,245,374 B,
  `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e`, 8 pages.
- web `Lucerna-VOL4-ru-en-web.pdf`: 3,375,060 B,
  `6419f7ad188d0e6aca09ae76abc739e954d0d6e1d5249171c34376e6b61360b6`, 8 pages.
- `2026-w47-ru-en.text.md`: 56,600 B,
  `2bf57f6808763372a1022cfe7dcaecae766a4a10ba62263e845c63166f66cc6c`.
- Page size both PDFs: 1462.5 × 2025 pts, PDF 1.7.

## 1. D3 — all three facets GREEN (fresh implementation, `verify3.py` + `verify3b.py`)

| Facet | Before (proof 2) | After (measured here) | Gate |
|---|---|---|---|
| (a) space | web `'чёрнаяпятница'`, 35,197 chars | web `'чёрная пятница'`, space bbox `[1145.576, 1266.762, 1148.108, 1288.725]` **identical to print**, width 2.532 pt; gap 'я'→'п' 2.532 = 2.532, diff 0.00; `'чёрнаяпятница'` ×0 in both pdftotext outputs | PASS |
| (b) closing » gap | x1 deficit 3.354 pt, gap +1.161 pt | last-`а` x1 1222.815 = 1222.815, deficit **0.00 pt**; » x0 1220.622 both; gap −2.193 pt in BOTH | PASS (≤ 0.5 pt) |
| (c) italic | web Regular, 0 italic chars | web embeds LucernaNotoSerif-Italic + LucernaNewsreader-Italic (`pdffonts`); italic census print 16 (NotoSerif-MediumItalic 14 + Newsreader16pt-Italic 2) = web 16 (LucernaNotoSerif-Italic 14 + LucernaNewsreader-Italic 2) | PASS |

- 3× teaser crops (`crops/p1-teaser-print.png` / `p1-teaser-web.png`): **pixel-identical**,
  same SHA-256, 0 / 307,800 pixels differing. Read by eye: «чёрная пятница» italic, two
  words with a clear space, closing » tight on `а`.

## 2. D2 — all 7 original spots still 0.00 pt (direct pinned lookup, `verify3.py`/`verify3b.py`)

| Spot | Print x1 | Web x1 | Deficit (was) |
|---|---|---|---|
| P1 headline `14-` 39.75 pt | 133.018 | 133.018 | **0.00** (was 4.33) |
| P4 heading `14-` 24 pt | 106.464 | 106.464 | **0.00** (was 2.62) |
| P1 contents `1. 14-` 15 pt | 1138.695 | 1138.695 | **0.00** (was 2.20) |
| P4 band-sub ` все восемь результатов` 13.5 pt | 1008.743 | 1008.743 | **0.00** (was 1.94) |
| P1 contents `3. «` 15 pt | 1122.225 | 1122.225 | **0.00** (was 1.17) |
| P5 title `«` 24 pt | 80.112 | 80.112 | **0.00** (was 0.91) |
| P7 `«` 16.12 pt ×2, x0=1096.12, y0 201.01 & 338.65 | 1105.606 / 1105.606 | 1105.606 / 1105.606 | **0.00 / 0.00** (was 0.58) |

No regression.

## 3. D1 — FIXED, both PDFs

- P5 band subtitle `"Black Friday": sales from 16 November`, straight quotes, in
  print.txt:1136 AND web.txt:1136 (the two texts are byte-identical). 3× crop
  (`crops/p5-band-web.png`) read by eye: closing straight quote tight on `:`.
- Curly-quote sweep (all 8 SVGs + both PDF text layers): U+201C ×1, U+201D ×1 (P7
  intended pair `“чёрной пятнице”`), U+2019 ×0, U+2018 ×0; straight `"` ×2 in each PDF.
- Italic runs in SVG: 5 × `font-style="italic"`, all in `p1-pervaya.svg`.

## 4. Full independent scan — two implementations, same result

- **Mine** (`verify3.py`, fresh code, line (y0,y1) + order pairing): span-text diffs **0**;
  abutting pairs > 0.5 pt: **0** (max |diff| **0.00 pt**); intra-span char-pair diffs
  > 0.5 pt: **0** (max |diff| **0.00 pt**); per-page char multiset diffs: all 8 pages empty.
  Char totals: 35,198 each; spaces 4,905 each; non-whitespace 30,293 each.
- **Proof2's script re-run** (`fullscan-proof2-copy.py`, proof2's file unchanged except the
  two PDF paths made absolute; output `scan-proof2-copy.json` in this dir): span-text
  diffs **0**; abutting > 0.5 pt: **0**; intra-char > 0.5 pt: **0**; multiset diffs all 8
  pages `{}`.
- Full-page pixel check: P8 print-vs-web mean abs diff **0.0**, 0 px > 30 (no images on
  P8); P1 mean 0.213, 2,504 px > 30 of 4,264,650 — by region: masthead (y<300) 2,084 px
  (UnifrakturMaguntia display face rasterises slightly differently from the subset font),
  photo zone (y1600–2100) 420 px (web images downscaled by design), body text (y300–1600)
  **0**, quiz/footer (y>2100) **0**. Max abs diff 202 (masthead). Text geometry identical
  per the char-level scan; the masthead difference is rasterisation only, not content.

## 5. Text layers — byte-identical

- `pdftotext Lucerna-VOL4-ru-en.pdf` → **57,149 B**; `pdftotext …-web.pdf` → **57,149 B**.
- `diff` of the two texts → **RC=0, zero differing lines**. Texts saved at `txt/print.txt`
  / `txt/web.txt` in this dir. `«чёрная пятница»` ×10 in both; `чёрнаяпятница` ×0 in both.

## 6. `check_core.py` — GOLDEN 8, BAD 0, RC=0

- Run as `…/venv/bin/python check_core.py .` with cwd = edition dir (the edition's own
  script, as proof2 ran it). Log: `check-core.log`.
- golden BAD: 0; gloss fails: 0; P8 svg text chars: 10,571.
- 1 orphan line-start (P7 y553 `”».`, known benign); 1 same-baseline collision
  (P1 y1712 `чёрная` + ` `, the D3 line — same as core/proof 2).
- NOTE: one combined exec (p8 + check_core) was interrupted by a service restart after the
  two p8 logs had landed; check_core was re-run cleanly afterwards.

## 7. p8 extract + compare — 150/150, CLEAN, RC=0

- `tools/p8.py extract --p8 <edition>/svg/p8-test.svg --total 150 --json p8-extract.json`
  → noted set = 150 of 150, RC=0.
- `tools/p8.py compare --core-p8 <core-ru>/svg/p8-test.svg --edition-p8 <edition>/svg/p8-test.svg
  --total 150 --json p8-compare.json`
  → `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`, RC=0
  (the four E translation keys, as expected).

## 8. freeze — baseline 8/8, diff adjudicated, RC=0

- `tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out freeze`
  → `baseline: 8/8 SVGs byte-identical (repointed files: none)`, RC=0
  (p5 hash `ae19aec96bc1d5ba…` matches the KIT record; full log: `freeze.log`).
  Core integrity OK (8 shipped core SVGs unchanged).
- `tools/freeze.py diff --core-svg <core-ru>/svg --edition-svg <edition>/svg
  --json freeze-diff.json` → per page +/− strings (P1 +20/−21, P2 +39/−36, P3 +26/−28,
  P4 +28/−28, P5 +29/−27, P6 +34/−54, P7 +49/−59, P8 +173/−637); added CJK only U+3000
  (6 total), RC=0. Full log: `freeze-diff.log`.
- **Correction to prior rounds**: proof2 and the italic-fix executor ran diff with
  `--core-svg <core-ru>` (the edition dir, no `.svg` files directly inside), so their
  "−0 strings removed" was vacuous (empty core side). This run uses the correct
  `core-ru/svg` path. Every removed Cyrillic-bearing string was adjudicated individually
  (`adjudicate-freeze.py`, `adjudicate-freeze-out.txt`): P6 label/note → English
  equivalents at the same positions; P7 subtitle → `Three levels, three topics`;
  P8 Morozko caption/credit (image skipped by the shared build condition, see
  PROOF-NOTE.md) + header subtitle → English subtitle + key-46 note `можно` → `can`.
  Added Cyrillic-bearing strings: 0 on all pages. **No Russian core content lost.**
- P8 Morozko mechanism verified in the shared build code (`content8.py:131-140`,
  identical in core-ru and the edition): `img_y = af.y + 24; if af.ci == 3 and
  img_y + img_h + 90 < 2560` — en keys end col 3 y=2288.84 → 2652.84 > 2560 → skipped.

## 9. Occlusion audit — 42 TEXTX, flag set IDENTICAL to proof2 and italic-fix runs

- `tools/occlusion_audit.py --selftest` → OK (planted classes fired, clean controls silent), RC=0.
- `tools/occlusion_audit.py --json occlusion.json <edition>/svg` → **42 TEXTX,
  0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE**. Log: `occlusion.log`.
- Flag-set comparison (as sets) vs proof2's `occlusion.json` AND the italic-fix run's
  `occlusion.json`: **IDENTICAL — no new flag**. (The JSON files differ by one byte only
  in the `svgdir` field: proof2 ran with relative `svg`, this run with the absolute path.)
  Round-1 pixel adjudication (42/42 CLEAR, systematic false-positive class) still applies.
- Exit-code note: the tool returns **RC=1 whenever any flag exists** — that is its by-design
  "flags present" signal, not a failure of this run.

## 10. P8 min font, VOL, ABSTRACT, text.md

- P8 min font (PyMuPDF on print PDF): **9.75 pt** (387 spans; next 9.98) — meets ≥ 9.75 pt.
- VOL in print text layer: VOL.4 ×9, VOL.3 ×1 (P4 correction), VOL.5 ×6 (teasers/
  disclosure); `tables.py vol 2026-W47` → vol 4.
- ABSTRACT.txt: one English line, 0 ASCII double quotes, real W47 topics + VOL.4 +
  A2–B2 + 150 exercises.
- text.md: 56,600 B, SHA-256 `2bf57f68…`; 150 numbered exercise groups, numbers 1–150
  complete; 0 Russian stem diffs vs core text.md; key values identical except 137–140
  (by-design translations); Morozko credit line identical to core.
- Weekdays verified with `date` (Europe/Moscow): 16 Mon–22 Sun; 6–8 Nov Fri–Sun;
  12 Nov Thu; 17 Nov Tue; 27 Nov Fri (Black Friday); 29 Nov Sun (Mother's Day); 30 Nov Mon
  (Cyber Monday). Hunger Games Russian premiere 26 Nov confirmed against live sources
  (TMDB, kinoafisha.info, ixbt.games).

## 11. Visual pages

- All 8 print pages rendered from the PDF (1.2×) and read by eye (`crops/p1–p8-print.png`);
  web P1 read by eye (`crops/p1-web.png`); P5 band 3× crop (`crops/p5-band-web.png`).
  No overflow, no overlap, no clipped text, no text crossing the footer line; P5 exercises
  end clear of the footer; P8 answer key complete to Q150.

## 12. NOT done (per the brief)

- No source edits, no rebuilds of any other edition, no print re-render.
- No git write operations of any kind (no add/commit/push/stash/reset, no `insert.py`,
  no `lint --write`). No files left behind in the repo: all outputs are in this scratch dir.
- `EDITION-RECORD.md` (named in the brief) does not exist in the edition dir or core-ru;
  text.md identity rests on the on-disk SHA + KIT §5 (see PROOF-NOTE.md §0).
