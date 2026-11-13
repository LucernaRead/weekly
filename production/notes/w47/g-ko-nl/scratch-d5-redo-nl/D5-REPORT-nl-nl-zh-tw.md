# D5-REPORT — 2026-w47-nl-zh-tw (Dutch core, Traditional Chinese readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step). First D5 build of this edition (the first D5 worker never started the CJK reader editions).

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `d82666126b61cb2ec30583e554b7c887`; print `6de893ca2811357c7be524b2b17e78af1c5362abc647e957d8665559466c704a` 25,993,186 B; web `9b364507f3c66ae67403fd2604185b5514f5143ea2d3f26887f0c1a62453f16d` 2,369,238 B; text.md `30af89dfbfe2dd31caf41a7e13a21dc615f77c0a1dde18ba9c93328e5d806c60` 44,320 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 0 DEFECT, edge 0; census FAIL 333 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.
- Note: KIT §Files delivered recorded a different pre-D5 web SHA (`172c1be8…` / 2,369,230 B) — pre-existing drift, web rebuilt after KIT written; the baseline.txt values above are the verified on-disk pre-D5 state.

## Install
- `apply_variant.py --target nl --reader zh-tw` (mode cjk — character-script routing, no `_READER_LANG` gate, per CJK-DECISION §1). svglib md5 → `83c4820e35a1e89c010ae57a230fb958`. Routing assert: FAILURES 0.
- History: install + rebuild-1 run by the second worker (2026-11-12 ~11:27–11:28 UTC), interrupted during `render.py` of rebuild-1 (0-byte `render.log`); the third worker applied the one fix below and ran rebuild-2.

## Fixes (layout only, text unchanged)
- Ported: P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production.
- 1 D5-caused defect found in rebuild-1, fixed by size only:
  1. HEAD TOO WIDE [P2-feature]: `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt (`content12.py:175`; core-nl D5 defect, same line)
- No box-title defect: all 25 titles fit after the install (boxtitle 0 DEFECT, creambox PASS 0 defects).

## Gates (final rebuild-2, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,976,962 B < 7 MB, 44,254 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 1051 (Traditional Chinese reader text); added Latin strings 22 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 214 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (55 OBSERVE) |
| boxtitle | 0 DEFECT (25 titles, 312 body lines) |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 221→221, slack 53.0px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 44,254 bytes, word multiset diff 0, de-whitespaced char streams equal |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-zh-tw.pdf` `90710eae78ae9ddd78f02a8a47041fbb09f322aa5adb351e214034384679e32b` — 13,888,370 B
- web `De-Lucerna-VOL4-nl-zh-tw-web.pdf` `42b892b5c065d18639cb61254286cf016be0a01d41a5320ca6b94aeb5f114b8a` — 1,976,958 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `42b892b5c065d18639cb61254286cf016be0a01d41a5320ca6b94aeb5f114b8a` (1,976,958 B; rebuild output was `1a923a7a42c6c7bdcff8805c3ae0faca314a59cb3f632a7378dd7d4c3e93c954`, 1,976,962 B — kept here as history). Content-equivalent: pdftotext 44,254 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `30af89dfbfe2dd31caf41a7e13a21dc615f77c0a1dde18ba9c93328e5d806c60` — 44,320 B, **byte-identical to pre-D5**

## Notes
- Print PDF 25,993,186 → 13,888,370 B (−12.1 MB): fewer CJK glyphs embedded now that the explanation-layer Latin routes to Newsreader (same direction as nl-ja 26.0M → 18.8M, nl-ko 17.3M → 13.9M). Not content loss: text layer verified equal print vs web.
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-zh-tw/` (`rebuild-1.log` = install + defect discovery, interrupted at render; `rebuild-2.log` = final green).
