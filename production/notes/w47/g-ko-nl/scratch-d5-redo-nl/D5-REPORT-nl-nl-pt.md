# D5-REPORT (REDO) — 2026-w47-nl-pt (Dutch core, Portuguese readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step).

## Why a redo
The first D5 worker rebuilt the `fanout-nl/` COPY, not top-level production, and
deleted its build-copy — production still held pre-D5 PDFs (print `dd74de0a…`,
web `1c8b8a6c…`). This redo rebuilt from the current top-level build-4 sources
in place. The copy's D5 SHAs (print `773eb8bb…` / 12,110,804 B) are superseded
and do NOT describe production.

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `dd74de0a45556e96fdfcc216a9d249bbae577ace249bfbc256dd564ef6e5113e` 12,672,019 B; web `1c8b8a6c3ecccdb8a95268077cfc8b97b6c0750f80b112bdfb29d4180c2d59d3` 1,618,464 B; text.md `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f` 47,209 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT, edge 0; census FAIL 497 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader pt` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged; conclusions reused from the first worker's copy build, re-verified here)
- Ported: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 4).
- 6 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　NÚMEROS` +7.2px → f.box tsize 23 → 22
  2. P1 `IN DEZE EDITIE　NESTA EDIÇÃO` +21.5px → 24 → 22pt
  3. P2 `ZO ONTHOUD JE HET　LEMBRA-TE` +33.0px → f.box tsize 23 → 21
  4. P2 TEXTX: `PAKJESAVOND IN VIER WOORDEN　PAKJESAVOND EM QUATRO PALAVRAS` overlapped right-anchored subtitle by 11.8×19.5px → head 28 → 27pt
  5. P6 `DE GRAFIEK　DADOS DE TREINO` +28.6px → 24 → 22pt
  6. P6 `VOOR OF TEGEN?　A FAVOR / CONTRA` +32.1px → 21 → 19pt
  7. P7 `HET WOORD　PALAVRA DA SEMANA` +57.1px → 23 → 19pt

## Gates (final rebuild, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,542,942 B < 7 MB, 46,598 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 450 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 239 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (39 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 240→240, slack 38.3px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,598 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-pt.pdf` `dc43c521becb6e20ddc578dd544e8bd717bd07903aef4e5d4cb48939947bb326` — 12,110,806 B
- web `De-Lucerna-VOL4-nl-pt-web.pdf` `b9e2c0d5b7f2bbfedc3a97fd1817d614c93b30e0480b8c2749d96d8769bcf07c` — 1,542,946 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `b9e2c0d5b7f2bbfedc3a97fd1817d614c93b30e0480b8c2749d96d8769bcf07c` (1,542,946 B; rebuild output was `a5c9fd90831465afe86d9629d2e1cbe07d4875c0d9bdc983cdff4cd47bfc1f17`, 1,542,942 B — kept here as history). Content-equivalent: pdftotext 46,598 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f` — 47,209 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-pt/`.
