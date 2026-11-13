# D5-REPORT — 2026-w47-nl-de (Dutch core, German readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green** (independent re-proof is the coordinator's separate step).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `f87d3f4d…ab59` 12,669,890 B; web `44d15508…ab6` 1,617,821 B, 46,734 text bytes; text.md `7d6eee03…d873` 46,214 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill **1 SPILL** (P4 D11, pre-existing — see below), boxtitle 0 DEFECT, edge 0; census FAIL 501 Latin-in-CJK-sans.

## Install
- `apply_variant.py --target nl --reader de` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported before rebuild: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt (core-nl D5 defect); P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11; pre-D5 spill +6.89px `'18:45 uur.'`).
- 6 D5-caused box-title defects (boxtitle + creambox agreed), all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　IN ZAHLEN` +17.2px → f.box tsize 23 → 21
  2. P1 `Agenda van de week　TERMINE DER WOCHE` +19.2px → 19 → 17pt
  3. P1 `IN HET KORT　KURZ GEMELDET` +24.7px → 24 → 22pt
  4. P2 `ZO ONTHOUD JE HET　MERK DIR` +11.0px → f.box tsize 23 → 22
  5. P6 `VOOR OF TEGEN?　DAFÜR / DAGEGEN` +31.1px → 21 → 19pt (verified visually on card crop)
  6. P7 `HET WOORD　WORT DER WOCHE` +17.1px → 23 → 21pt

## Gates (final rebuild-2, after fixes)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| render.py / webpdf.py | RC 0; web 1,536,341 B < 7 MB, 46,645 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138, 140] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000, 1/page p2–p8); added Latin strings 457 |
| occlusion | 0 flags |
| spill | 0 SPILL (38 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 228→228, slack 43.5px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| text layer | print = web = 46,645 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final)
- print `De-Lucerna-VOL4-nl-de.pdf` `dc567b1a5a7afb338a6dba411ad5d8b0708d9d89a29c2c40e62a323aaf56cfff` — 12,104,226 B
- web `De-Lucerna-VOL4-nl-de-web.pdf` `1259cb64766b694bf7444d1f916e50bbb6baedc9ec2b3a48aff2cbf3bc6f2416` — 1,536,341 B
- text.md `7d6eee03b87a09d9319a999a1842e6252c7bb1959d6f57f6d40b431e967fd873` — 46,214 B, **byte-identical to pre-D5**

## Notes
- KIT updated (Files delivered + new D5 section). Build-copy `post/freeze/build-copy` deleted after verification.
- No commit, no push, no `lint.mjs --write`.
