# D5-REPORT (REDO) — 2026-w47-nl-en (Dutch core, English readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step).

## Why a redo
The first D5 worker rebuilt the `fanout-nl/` COPY, not top-level production, and
deleted its build-copy — production still held pre-D5 PDFs (print `79fa049b…`,
web `4a7ca8c4…`). This redo rebuilt from the current top-level build-11 sources
in place. The copy's D5 SHAs (print `ff89c908…` / 12,102,278 B) are superseded
and do NOT describe production.

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `79fa049b318d94f15f28fe23daefd2513221a77fde6511c694aee109bacf3239` 12,665,893 B; web `4a7ca8c48ef188a04cbeba67c6a2cbb984e64589a269dec6d4ccef79c246a8c4` 1,610,561 B; text.md `9596c4acbb27c20c0f1581dff99ac8871ad0937ec5839397f0fa9d3087a87978` 45,115 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by build-10 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 498 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader en` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged; conclusions reused from the first worker's copy build, re-verified here)
- Ported: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 10).
- 6 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX from defect 1, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　IN NUMBERS` +39.2px → f.box tsize 23 → 20 (also fixes TEXTX overlap with `'wedstrijden.'` 11.5×4.8px)
  2. P1 `Agenda van de week　THIS WEEK'S EVENTS` +9.2px → 19 → 18pt
  3. P1 `IN DEZE EDITIE　IN THIS ISSUE` +8.5px → 24 → 23pt
  4. P2 `ZO ONTHOUD JE HET　REMEMBER` +34.0px → f.box tsize 23 → 20
  5. P6 `VOOR OF TEGEN?　FOR OR AGAINST?` +24.1px → 21 → 19pt
  6. P7 `HET WOORD　WORD OF THE WEEK` +38.1px → 23 → 20pt

## Gates (final rebuild, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,534,345 B < 7 MB, 45,350 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys; 140 now matches core after build-11 Q140 fix) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 15 (all U+3000); added Latin strings 444 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 247 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (37 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 236→236, slack 38.4px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 45,350 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-en.pdf` `d87a5242afec8f603c1182afc7f90e6ee94c580a8b217a708883cf231533e55b` — 12,102,271 B
- web `De-Lucerna-VOL4-nl-en-web.pdf` `db7a9ace064a17a36230332b5d46fa51ff4c96f432cae676174eecff632722e1` — 1,534,348 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `db7a9ace064a17a36230332b5d46fa51ff4c96f432cae676174eecff632722e1` (1,534,348 B; rebuild output was `c43bccdd7899e2ee5c41615d74c75fd76120043b29fac67d04ebb600a0acfa0d`, 1,534,345 B — kept here as history). Content-equivalent: pdftotext 45,350 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `9596c4acbb27c20c0f1581dff99ac8871ad0937ec5839397f0fa9d3087a87978` — 45,115 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (§6 sizes + new §12; history preserved, §10/§11 untouched). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-en/`.
