# D5-REPORT — 2026-w47-nl-ru (Dutch core, Russian readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green on first rebuild** (independent re-proof is the coordinator's separate step).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `f945029d…89c2` 12,718,382 B; web `e5e3d5d3…2724` 1,661,354 B, 54,978 text bytes; text.md `558786fc…9273` 57,848 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill **1 SPILL** (P4 D11, pre-existing), boxtitle 0, edge 0; census FAIL 612 Latin-in-CJK-sans.

## Install
- `apply_variant.py --target nl --reader ru` (mode ru). svglib md5 → `37af27e93cadf56a0ea711105024e232`. Routing assert: FAILURES 0 (Cyrillic → sans_noto; 780 Noto Sans elements post-D5).

## Fixes (layout only, text unchanged)
- Ported before rebuild: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11).
- **No D5-caused defects.** No size changes needed: Cyrillic tails route to Noto Sans (unchanged advance), and the Dutch heads' Newsreader widening stayed inside every box.

## Gates (rebuild-1 = final)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,780,189 B < 7 MB, 54,941 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138, 140] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 149 |
| occlusion | 0 flags (the en-ru pilot P8 "collisions" were the fixed measurement false positive — no key rows touched) |
| spill | 0 SPILL (36 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit (tools version) | PASS 0 defects (P8 lines 248→248, slack 39.0px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 54,941 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final)
- print `De-Lucerna-VOL4-nl-ru.pdf` `85e2aa0910c7f6d04df93561b4468caeffc04d0e9f493047fb1726a964e8d169` — 12,368,014 B
- web `De-Lucerna-VOL4-nl-ru-web.pdf` `566ee0197d9d42711a9bda1d7d6ee35ba40fbacd1b39a3f1c041a02be1d9a266` — 1,780,189 B
- text.md `558786fc6247329c319fd1cf965e458ec32cea1daf3d7ae534f02c9804829273` — 57,848 B, **byte-identical to pre-D5**

## Notes
- KIT updated (Files delivered + new D5 section). Build-copy `post/freeze/build-copy` deleted after verification.
- No commit, no push, no `lint.mjs --write`.
