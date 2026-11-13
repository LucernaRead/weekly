# D5-REPORT (REDO) — 2026-w47-nl-es (Dutch core, Spanish readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step).

## Why a redo
The first D5 worker rebuilt the `fanout-nl/` COPY, not top-level production, and
deleted its build-copy — production still held pre-D5 PDFs (print `e6c28566…`,
web `b483f73d…`). This redo rebuilt from the current top-level build-5 sources
in place. The copy's D5 SHAs (print `a6f78752…` / 12,107,935 B) are superseded
and do NOT describe production.

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5` 12,669,546 B; web `b483f73d80199a96b4a390c165ce7fb94c3d01c7104975e1a749cf5156687a4f` 1,616,179 B; text.md `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` 47,649 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT (copy-era pre-existing +1.5px P6 defect already fixed in production by fix1 D1), edge 0; census FAIL 497 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader es` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged; conclusions reused from the first worker's copy build, re-verified here)
- Ported: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` and P6 `DE GRAFIEK` 24 → 23pt were already in production.
- 5 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　EN CIFRAS` +10.2px → f.box tsize 23 → 22
  2. P1 `IN DEZE EDITIE　ESTE NÚMERO` +20.5px → 24 → 22pt
  3. P2 `ZO ONTHOUD JE HET　RECUERDA` +24.0px → f.box tsize 23 → 21
  4. P6 `DE GRAFIEK　DATOS DE PRÁCTICA` +58.6px → 23 → 20pt
  5. P7 `HET WOORD　PALABRA SEMANAL` +32.1px → 23 → 21pt
  6. P2 TEXTX: `PAKJESAVOND IN VIER WOORDEN　PAKJESAVOND EN CUATRO PALABRAS` overlapped right-anchored subtitle by 6.8×15.5px → head 28 → 27pt

## Gates (final rebuild, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,540,064 B < 7 MB, 46,704 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 449 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 231 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (39 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 237→237, slack 41.7px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,704 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-es.pdf` `2da02d5b30814f011adc75399fd5c4b1b90e41e8877bf3eb16c0610d4408f776` — 12,107,937 B
- web `De-Lucerna-VOL4-nl-es-web.pdf` `249fda66604bdda210ee57701c27931bc8beb17ba978c99fb85e9cb40b482684` — 1,540,062 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `249fda66604bdda210ee57701c27931bc8beb17ba978c99fb85e9cb40b482684` (1,540,062 B; rebuild output was `ac5498117a56a0d7125e4b59ab39d6db8371297ca1671feb269bc46f13ef14b5`, 1,540,064 B — kept here as history). Content-equivalent: pdftotext 46,704 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` — 47,649 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-es/`.
