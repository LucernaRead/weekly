# D5-REPORT — 2026-w47-nl-it (Dutch core, Italian readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green** (independent re-proof is the coordinator's separate step).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `2520e5ad…826` 12,667,197 B; web `609dc9a5…f97f0c` 1,610,232 B, 46,500 text bytes; text.md `62142f93…29e8` 47,049 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill **1 SPILL** (P4 D11, pre-existing), boxtitle 0, edge 0; census FAIL 495 Latin-in-CJK-sans.

## Install
- `apply_variant.py --target nl --reader it` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported before rebuild: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` (core fix5 D11).
- 2 D5-caused box-title defects (boxtitle + creambox agreed), both fixed by size only:
  1. P6 `VOOR OF TEGEN?　PRO O CONTRO?` +3.1px → 21 → 20pt
  2. P7 `PAS OP!　CLINICA DEGLI ERRORI` +8.1px → 23 → 22pt (verified visually on card crop)

## Incident: transient webpdf ENOSPC in rebuild-1
- `webpdf.py` died with `OSError: [Errno 28] No space left on device`; disk 92G used / 58G avail before and after, `/tmp` 4.8M used — a transient spike, not this edition. Rebuild-2 ran webpdf clean. The rebuild-1 text-layer diff (45 words) was the stale pre-D5 web PDF vs the new print PDF.

## Gates (final rebuild-2, after fixes)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,534,487 B < 7 MB, 46,362 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138, 140] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 447 |
| occlusion | 0 flags |
| spill | 0 SPILL (39 OBSERVE) |
| boxtitle | 0 DEFECT, 1 marginal (P2 `RICORDA` 0.8px margin, ink inside) |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit (tools version) | PASS 0 defects (P8 lines 228→228) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,362 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final)
- print `De-Lucerna-VOL4-nl-it.pdf` `5a90aa6d2e77d10ecdfa0ef5c6e48228173c302ff7df471c91fb7fc4c34e97f6` — 12,102,400 B
- web `De-Lucerna-VOL4-nl-it-web.pdf` `68a23245cc5276327390ef4478ea69a8eaf6de414ec7c3d403422d84eb7ae947` — 1,534,487 B
- text.md `62142f938c6a814297b5b4602a5a95ea0d7df38b1c4f86df5402a9a8dad629e8` — 47,049 B, **byte-identical to pre-D5**

## Notes
- KIT updated (Files delivered + new D5 section). Build-copy `post/freeze/build-copy` deleted after verification.
- No commit, no push, no `lint.mjs --write`.
