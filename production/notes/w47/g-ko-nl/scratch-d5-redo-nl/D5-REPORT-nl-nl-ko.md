# D5-REPORT — 2026-w47-nl-ko (Dutch core, Korean readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step). First D5 build of this edition (the first D5 worker never started the CJK reader editions).

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `51f469d99e12dd041ed171fc401ea648`; print `c4f446b9adc06c29be6a047abf30c83a445062bc26335a578a9609afb42d537d` 17,281,343 B; web `f0c2cc079a5c8330ca6153206e7202ea424e25d295d7ae8333a3935265e8b7bc` 1,919,763 B; text.md `75fbaa3004d0da29ce096953bd584b891afc2daee6a2bffa8d7cd7fe31105dd9` 47,585 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT, edge 0; census FAIL 333 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader ko` (mode cjk — character-script routing, no `_READER_LANG` gate, per CJK-DECISION §1; CJK index already KR). svglib md5 → `956ddfde0e783827b69304f80ddb98af`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported: P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 3).
- Exactly 1 D5-caused defect found in rebuild-1: HEAD TOO WIDE [P2-feature]: `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt. No box-title defect (all 39 titles fit).

## Freeze gate note
- `freeze.py baseline` ran under `tools/venv/bin/python` with RC=0 (8/8 byte-identical). The task's system-python3 fallback for a ko freeze ABORT was NOT needed.

## Gates (final rebuild-2, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,791,909 B < 7 MB, 47,521 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 3447 (KR text in Noto Sans CJK KR); added Latin strings 110 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 215 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (123 OBSERVE) |
| boxtitle | 0 DEFECT (39 titles, 492 body lines) |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 229→229, slack 54.0px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective (KR quotes not a defect) |
| text layer | print = web = 47,521 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-ko.pdf` `fd8daad8ba7eeee962fdd0479c389a36d8c435b2fc78d2262f87c23ceeeee039` — 13,871,308 B
- web `De-Lucerna-VOL4-nl-ko-web.pdf` `694720afc0ccf6ebfb7f3800b22aaa114c097d4b85c79c369a58d8fb457db974` — 1,791,910 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `694720afc0ccf6ebfb7f3800b22aaa114c097d4b85c79c369a58d8fb457db974` (1,791,910 B; rebuild output was `7dd70f00993ae30759fc1e9d3ecd9f8f05c5e0075ab255dbb185c83943953fe0`, 1,791,909 B — kept here as history). Content-equivalent: pdftotext 47,521 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `75fbaa3004d0da29ce096953bd584b891afc2daee6a2bffa8d7cd7fe31105dd9` — 47,585 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-ko/` (`rebuild-1.log` = defect discovery, `rebuild-2.log` = final green).
