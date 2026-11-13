# D5-REPORT — 2026-w47-nl-es (Dutch core, Spanish readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green** (independent re-proof is the coordinator's separate step).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `0388d59c…b771` 12,669,541 B; web `5b4f8162…d7a21` 1,616,172 B, 46,814 text bytes; text.md `44fc3d5c…d00eb` 47,649 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill **1 SPILL** (P4 D11, pre-existing), boxtitle **1 DEFECT** (P6 `DE GRAFIEK　DATOS DE PRÁCTICA` +1.5px, pre-existing — see KIT note), edge 0; census FAIL 497 Latin-in-CJK-sans.

## Install
- `apply_variant.py --target nl --reader es` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported before rebuild: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11).
- 5 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　EN CIFRAS` +10.2px → f.box tsize 23 → 22
  2. P1 `IN DEZE EDITIE　ESTE NÚMERO` +20.5px → 24 → 22pt
  3. P2 `ZO ONTHOUD JE HET　RECUERDA` +24.0px → f.box tsize 23 → 21
  4. P6 `DE GRAFIEK　DATOS DE PRÁCTICA` +58.6px → 24 → 20pt (verified visually on card crop)
  5. P7 `HET WOORD　PALABRA SEMANAL` +32.1px → 23 → 21pt
  6. P2 TEXTX: `PAKJESAVOND IN VIER WOORDEN　PAKJESAVOND EN CUATRO PALABRAS` overlapped right-anchored subtitle by 6.8×15.5px → head 28 → 27pt

## Gates (final rebuild-2, after fixes)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,540,063 B < 7 MB, 46,705 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 449 |
| occlusion | 0 flags |
| spill | 0 SPILL (39 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit (tools version) | PASS 0 defects (P8 lines 237→237) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,705 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final)
- print `De-Lucerna-VOL4-nl-es.pdf` `a6f787524e60c724d9b254676a075704bddd51d3d9a8a84adfc3a551bb24d62f` — 12,107,935 B
- web `De-Lucerna-VOL4-nl-es-web.pdf` `51cf30c34120149c05055c2345d4aef56534429a2d4cceb650f46b27c42c6b0e` — 1,540,063 B
- text.md `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` — 47,649 B, **byte-identical to pre-D5**

## Notes
- KIT updated (Files delivered + new D5 section). Build-copy `post/freeze/build-copy` deleted after verification.
- No commit, no push, no `lint.mjs --write`.
