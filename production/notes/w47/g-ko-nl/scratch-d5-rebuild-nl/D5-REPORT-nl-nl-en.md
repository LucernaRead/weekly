# D5-REPORT — 2026-w47-nl-en (Dutch core, English readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green** (independent re-proof is the coordinator's separate step).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `3352492c…693c` 12,665,902 B; web `2589cac4…9a06` 1,610,568 B, 45,429 text bytes; text.md `05513522…23dd` 45,106 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill **1 SPILL** (P4 D11, pre-existing), boxtitle 0 DEFECT, edge 0; census FAIL 498 Latin-in-CJK-sans.

## Install
- `apply_variant.py --target nl --reader en` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported before rebuild: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11).
- 6 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX from defect 1, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　IN NUMBERS` +39.2px → f.box tsize 23 → 20 (also fixes TEXTX overlap with `'wedstrijden.'` 11.5×4.8px; verified visually on card crop)
  2. P1 `Agenda van de week　THIS WEEK'S EVENTS` +9.2px → 19 → 18pt
  3. P1 `IN DEZE EDITIE　IN THIS ISSUE` +8.5px → 24 → 23pt
  4. P2 `ZO ONTHOUD JE HET　REMEMBER` +34.0px → f.box tsize 23 → 20
  5. P6 `VOOR OF TEGEN?　FOR OR AGAINST?` +24.1px → 21 → 19pt
  6. P7 `HET WOORD　WORD OF THE WEEK` +38.1px → 23 → 20pt

## Gates (final rebuild-2, after fixes)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| render.py / webpdf.py | RC 0; web 1,534,341 B < 7 MB, 45,341 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138, 140] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 15 (all U+3000); added Latin strings 444 |
| occlusion | 0 flags |
| spill | 0 SPILL (37 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 236→236, slack 38.4px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| text layer | print = web = 45,341 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final)
- print `De-Lucerna-VOL4-nl-en.pdf` `ff89c908aa2f8637e45b42c5d7064dcdd47afc618335e52afb1cdb7327a6a323` — 12,102,278 B
- web `De-Lucerna-VOL4-nl-en-web.pdf` `a35d66b1b7c6870d18ba781b4880386077e0af5ff60f49118a7877fc3097613a` — 1,534,341 B
- text.md `05513522b585be936b4bd28654e911c278595afa9ec8a8713e1504ab364623dd` — 45,106 B, **byte-identical to pre-D5**

## Notes
- KIT updated (§6 sizes + new §10 D5 section). Build-copy `post/freeze/build-copy` deleted after verification.
- No commit, no push, no `lint.mjs --write`.
