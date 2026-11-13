# D5-REPORT — 2026-w47-nl-fr (Dutch core, French readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green** (independent re-proof is the coordinator's separate step).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `50d9182b…a544` 12,656,012 B; web `9e90d0ab…84e4` 1,612,638 B, 46,862 text bytes; text.md `21888192…e7c9` 47,739 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill **1 SPILL** (P4 D11, pre-existing), boxtitle 0, edge 0; census FAIL 500 Latin-in-CJK-sans.

## Install
- `apply_variant.py --target nl --reader fr` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported before rebuild: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11).
- 6 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　EN CHIFFRES` +44.2px → f.box tsize 23 → 20 (also fixed the P1 TEXTX overlap with `'wedstrijden.'` 16.5×4.8px; verified visually on card crop)
  2. P2 `ZO ONTHOUD JE HET　À RETENIR` +20.0px → f.box tsize 23 → 21
  3. P6 `DE GRAFIEK　DONNÉES FICTIVES` +42.6px → 24 → 21pt
  4. P6 `VOOR OF TEGEN?　POUR OU CONTRE` +24.1px → 21 → 19pt
  5. P7 `PAS OP!　CLINIQUE DES ERREURS` +21.1px → 23 → 21pt
  6. P7 `HET WOORD　MOT DE LA SEMAINE` +44.1px → 23 → 20pt

## Gates (final rebuild-2, after fixes)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,538,529 B < 7 MB, 46,764 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138, 140] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 452 |
| occlusion | 0 flags |
| spill | 0 SPILL (38 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit (tools version) | PASS 0 defects (P8 lines 215→215) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,764 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final)
- print `De-Lucerna-VOL4-nl-fr.pdf` `06838646466863580a8ee2cc95129152cd719f9063b9f445152da8a4ec8c2357` — 12,106,426 B
- web `De-Lucerna-VOL4-nl-fr-web.pdf` `50bee8b9a1e55c4f835318f95f9e9d4ae34efe1e36cd598c1ec166e0e25437cc` — 1,538,529 B
- text.md `21888192450ff4f8350ed5c0fd091e4de44e4425fd593103b35358cdef43e7c9` — 47,739 B, **byte-identical to pre-D5**

## Notes
- KIT updated (Files delivered + new D5 section). Build-copy `post/freeze/build-copy` deleted after verification.
- No commit, no push, no `lint.mjs --write`.
