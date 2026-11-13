# D5-REPORT (REDO) — 2026-w47-nl-ru (Dutch core, Russian readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step).

## Why a redo
The first D5 worker rebuilt the `fanout-nl/` COPY, not top-level production, and
deleted its build-copy — production still held pre-D5 PDFs (print `b9847bb2…`,
web `cbaac2df…`). This redo rebuilt from the current top-level build-6 sources
in place. The copy's D5 SHAs are superseded and do NOT describe production.

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `9b2531b76693…` (carries the unkerned-run patch, build 6); print `b9847bb26eac3011660c767b4ae17857ddeb39014fe8b9ffa7b9ec90b0404933` 12,718,074 B; web `cbaac2df7c7acd38f35c9cd9eaba04b3416c290b72e676057f68dccb47b6c7ca` 1,661,043 B; text.md `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` 57,870 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT, edge 0; census FAIL 612 (Latin 346 + Cyrillic 266 in CJK sans). `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader ru` (mode ru). svglib md5 → `dbf4aa780f7ebc9043b29c7025d84032`. Added Noto Sans faces/cmaps, sans_noto `_PATH` rows, fix2 block, D5 sans block, `_D5_READER = 'ru'`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported: P2 head `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt; P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 6).
- No other defects: the first worker's copy build also found zero D5-caused defects on this edition — Cyrillic tails route to Noto Sans unchanged, no box title overflowed. No en-ru-style P8 key-row collisions appeared (those were a proven measurement false positive in `occlusion_audit.py`, since fixed in the tool).

## Gates (final rebuild, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,779,860 B < 7 MB, 54,983 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 7 (all U+3000); added Latin strings 149 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 165 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (36 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 248→248, slack 39.0px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 54,983 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-ru.pdf` `8fa079cbd094b7b0863fcc526cd5a4f6d719cdadc7a41cdc97a261adbb3d1227` — 12,367,658 B
- web `De-Lucerna-VOL4-nl-ru-web.pdf` `69678fdcdd00e05fe188555d7aa5d6fc2235473a3b2a03cb027e009747d6dbff` — 1,779,868 B (larger than pre-D5: Cyrillic Noto Sans faces now embedded)
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `69678fdcdd00e05fe188555d7aa5d6fc2235473a3b2a03cb027e009747d6dbff` (1,779,868 B; rebuild output was `e025daa39ff503cb06938cd05877a0e98951daaf8bcb3523e6535de1a942221f`, 1,779,860 B — kept here as history). Content-equivalent: pdftotext 54,983 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `f23da475ff54bcfe86bbe6794473eafc65b42dbd5f015766924ce3e83cefb984` — 57,870 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-ru/`.
