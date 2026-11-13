# D5-REPORT — 2026-w47-nl-pt (Dutch core, Portuguese readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green** (independent re-proof is the coordinator's separate step).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `e85aa1a0…a834` 12,672,018 B; web `a0c8c87b…46d85` 1,618,472 B, 46,693 text bytes; text.md `865e659f…7efc` 47,204 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill **0** (phaseA-2 re-run after the two ported fixes; D11 already fixed in the regenerated SVGs), boxtitle 0, edge 0; census FAIL 497 Latin-in-CJK-sans.

## Install
- `apply_variant.py --target nl --reader pt` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported before rebuild: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11).
- 6 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　NÚMEROS` +7.2px → f.box tsize 23 → 22
  2. P1 `IN DEZE EDITIE　NESTA EDIÇÃO` +21.5px → 24 → 22pt
  3. P2 `ZO ONTHOUD JE HET　LEMBRA-TE` +33.0px → f.box tsize 23 → 21
  4. P2 TEXTX: `PAKJESAVOND IN VIER WOORDEN　PAKJESAVOND EM QUATRO PALAVRAS` overlapped right-anchored subtitle by 11.8×19.5px → head 28 → 27pt
  5. P6 `DE GRAFIEK　DADOS DE TREINO` +28.6px → 24 → 22pt
  6. P6 `VOOR OF TEGEN?　A FAVOR / CONTRA` +32.1px → 21 → 19pt
  7. P7 `HET WOORD　PALAVRA DA SEMANA` +57.1px → 23 → 19pt (verified visually on card crop)

## Gates (final rebuild-2, after fixes)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,542,934 B < 7 MB, 46,593 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138, 140] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 450 |
| occlusion | 0 flags |
| spill | 0 SPILL (39 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit (tools version) | PASS 0 defects (P8 lines 240→240) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,593 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final)
- print `De-Lucerna-VOL4-nl-pt.pdf` `773eb8bb3a47a6c457530183c043f42431baadcf4cea28b7cc18c1750edd48a6` — 12,110,804 B
- web `De-Lucerna-VOL4-nl-pt-web.pdf` `cc34b7b36257adb895c2276e5f868b701c09d71b6d2c3eb7ddd1d1e881c7e6cc` — 1,542,934 B
- text.md `865e659fc2d4a9b1639c3513cd8e3326536feac8ae5fed14dca411d0cc137efc` — 47,204 B, **byte-identical to pre-D5**

## Notes
- KIT updated (Files delivered + new D5 section). Build-copy `post/freeze/build-copy` deleted after verification.
- No commit, no push, no `lint.mjs --write`.
