# D5-REPORT (REDO) — 2026-w47-nl-fr (Dutch core, French readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step).

## Why a redo
The first D5 worker rebuilt the `fanout-nl/` COPY, not top-level production, and
deleted its build-copy — production still held pre-D5 PDFs (print `6aedb91f…`,
web `81d4fc19…`). This redo rebuilt from the current top-level build-6 sources
in place. The copy's D5 SHAs (print `06838646…` / 12,106,426 B) are superseded
and do NOT describe production.

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `78fdfbb037538b1f8a738434ea90a782`; print `6aedb91fdc857b2ae545795b490c10b95400925ab1f430c658ca34922fd92d47` 12,656,006 B; web `81d4fc195b008be1ec35d7fe5ec31e4c591fd796d54730c410857843f0c1793b` 1,612,631 B; text.md `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a` 47,744 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT, edge 0; census FAIL 500 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader fr` (mode latin). svglib md5 → `9e44d3e443063634d5dd8570d4af10b7`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged; conclusions reused from the first worker's copy build, re-verified here)
- Ported: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 6).
- 6 D5-caused box-title defects (boxtitle + creambox agreed) + 1 occlusion TEXTX from defect 1, all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　EN CHIFFRES` +44.2px → f.box tsize 23 → 20 (also fixes TEXTX overlap with `'wedstrijden.'` 16.5×4.8px)
  2. P2 `ZO ONTHOUD JE HET　À RETENIR` +20.0px → f.box tsize 23 → 21
  3. P6 `DE GRAFIEK　DONNÉES FICTIVES` +42.6px → 24 → 21pt
  4. P6 `VOOR OF TEGEN?　POUR OU CONTRE` +24.1px → 21 → 19pt
  5. P7 `PAS OP!　CLINIQUE DES ERREURS` +21.1px → 23 → 21pt
  6. P7 `HET WOORD　MOT DE LA SEMAINE` +44.1px → 23 → 20pt

## Gates (final rebuild, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,538,515 B < 7 MB, 46,769 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 452 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 242 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (38 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 215→215, slack 37.6px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,769 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-fr.pdf` `08f57ec27d8698c54be0ef79024048fec737ed4aabbfa8be68c1bb04b26c5fad` — 12,106,421 B
- web `De-Lucerna-VOL4-nl-fr-web.pdf` `1b429a3ff61edb99348c4d29a790204565b07a173e966f340268af79b9c585bc` — 1,538,511 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `1b429a3ff61edb99348c4d29a790204565b07a173e966f340268af79b9c585bc` (1,538,511 B; rebuild output was `7e2f0989d641c4f6daa83f9f4698747810ab7f7e9ee9a588a38d9208eb362126`, 1,538,515 B — kept here as history). Content-equivalent: pdftotext 46,769 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `f1d1154442c4ea26fcc71dcf605704ab76a3555a2568bff521f158d974b5bc1a` — 47,744 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-fr/`.
