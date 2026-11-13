# D5-REPORT (REDO) — 2026-w47-nl-de (Dutch core, German readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step).

## Why a redo
The first D5 worker rebuilt the `fanout-nl/` COPY, not top-level production, and
deleted its build-copy — production still held pre-D5 PDFs (print `8e3ba915…`,
web `0139ab96…`). This redo rebuilt from the current top-level build-8 sources
in place. The copy's D5 SHAs (print `dc567b1a…` / 12,104,226 B) are superseded
and do NOT describe production.

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `ff8bc1f4678cf646ce2cf20aa59355b6` (carries the build-8 fix2 port); print `8e3ba9155d155db85f2b0c03f1595d920ceb8b3220d7652929f67b489f8b1412` 12,669,946 B; web `0139ab963c4e61f534ef537ee17ff3899c029780577036696776055d35c3c360` 1,617,872 B; text.md `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb` 46,226 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production by build-7 sh=89 port), boxtitle 0 DEFECT, edge 0; census FAIL 501 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader de` (mode latin). svglib md5 → `968d05e480a512853d96d0eee9ec104c`. Installer reported "fix2 already present" (preserved). Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged; conclusions reused from the first worker's copy build, re-verified here)
- Ported: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 7).
- 6 D5-caused box-title defects (boxtitle + creambox agreed), all fixed by size only:
  1. P1 `DE WEEK IN CIJFERS　IN ZAHLEN` +17.2px → f.box tsize 23 → 21
  2. P1 `Agenda van de week　TERMINE DER WOCHE` +19.2px → 19 → 17pt
  3. P1 `IN HET KORT　KURZ GEMELDET` +24.7px → 24 → 22pt
  4. P2 `ZO ONTHOUD JE HET　MERK DIR` +11.0px → f.box tsize 23 → 22
  5. P6 `VOOR OF TEGEN?　DAFÜR / DAGEGEN` +31.1px → 21 → 19pt
  6. P7 `HET WOORD　WORT DER WOCHE` +17.1px → 23 → 21pt

## Gates (final rebuild, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,536,343 B < 7 MB, 46,657 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 457 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 236 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (38 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 228→228, slack 43.5px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 (curly_total 1, in Newsreader) |
| census_quotes.py | 0 defective |
| text layer | print = web = 46,657 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-de.pdf` `97420549c81ef63a0f77cfa985f84b89a79371f00ab15026e6d8f21ac2c4b4f5` — 12,104,230 B
- web `De-Lucerna-VOL4-nl-de-web.pdf` `2361bedfd4d5f869ec193877cb80189a9ff0078fcf7bde71d88b1fbfe5a40abb` — 1,536,341 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `2361bedfd4d5f869ec193877cb80189a9ff0078fcf7bde71d88b1fbfe5a40abb` (1,536,341 B; rebuild output was `15a65413c7f7d5635066ba69c4cdf39c23547366ca364b247fffecfbeba5126a`, 1,536,343 B — kept here as history). Content-equivalent: pdftotext 46,657 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb` — 46,226 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-de/`.
