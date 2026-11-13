# D5-REPORT (REDO) — 2026-w47-nl-it (Dutch core, Italian readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step).

## Why a redo
The first D5 worker rebuilt the `fanout-nl/` COPY, not top-level production, and
deleted its build-copy — production still held pre-D5 PDFs (print `4d297162…`,
web `e2f6d075…`). This redo rebuilt from the current top-level build-6 sources
in place. The copy's D5 SHAs (print `5a90aa6d…` / 12,102,400 B) are superseded
and do NOT describe production.

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `4d297162d9e9f2ac99896ab2cf41865af0588d0d060ad76b89b3a7dabe44da15` 12,667,201 B; web `e2f6d07544458961b59020b7b54bb4114b041ab03cc542c78feb64a563d3ae11` 1,610,244 B; text.md `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b` 47,060 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT, edge 0; census FAIL 495 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader it` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged; conclusions reused from the first worker's copy build, re-verified here)
- Ported: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 6).
- 2 D5-caused box-title defects (boxtitle + creambox agreed), both fixed by size only:
  1. P6 `VOOR OF TEGEN?　PRO O CONTRO?` +3.1px → 21 → 20pt
  2. P7 `PAS OP!　CLINICA DEGLI ERRORI` +8.1px → 23 → 22pt

## Incident: transient webpdf ENOSPC in the first worker's rebuild-1
- The first worker's rebuild-1 `webpdf.py` died with `OSError: [Errno 28] No space left on device`; disk 92G used / 58G avail before and after, `/tmp` 4.8M used — a transient spike, not this edition. No such incident in this redo (webpdf RC=0 first try).

## Gates (final rebuild, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,534,505 B < 7 MB, 46,372 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 447 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 234 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (39 OBSERVE) |
| boxtitle | 0 DEFECT, 1 marginal (P2 `RICORDA` 0.8px margin, ink inside) |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 228→228, slack 41.7px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,372 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-it.pdf` `675f2bf33c42a74ff6991e72e5e27564b4b6d3abf8e84b94ae22a8d6d94ae437` — 12,102,402 B
- web `De-Lucerna-VOL4-nl-it-web.pdf` `81a3ffaf8e8ea2d23b521e16c4a8f73db9d28d73c0ed17532711f22579b40833` — 1,534,500 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `81a3ffaf8e8ea2d23b521e16c4a8f73db9d28d73c0ed17532711f22579b40833` (1,534,500 B; rebuild output was `f042c93a0522a6c1d89c7747c12bcb4710d00c065ca38d318e182157b2cc01e7`, 1,534,505 B — kept here as history). Content-equivalent: pdftotext 46,372 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b` — 47,060 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-it/`.
