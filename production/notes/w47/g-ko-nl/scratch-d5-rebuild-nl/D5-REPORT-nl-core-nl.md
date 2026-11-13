# D5-REPORT — core-nl (2026-W47, Dutch core, reader zh-cn)

Date: 2026-11-12 (UTC). Worker: D5 rebuild, nl family. Status: **DONE, all gates green** (independent re-proof is the coordinator's separate step, not done here).

## Pre-D5 baseline (phase A, verified on disk)
- svglib md5 `152dd0feb7c221d59e778542c890f07b`; print `4f66c793…5b154` 25,955,680 B; web `34273bb8…c90a` 2,104,068 B, 44,197 text bytes; text.md `0b97a48d…7050c` 44,093 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0 flags, spill 0, boxtitle 0 DEFECT, edge 0; census FAIL 335 Latin-in-CJK-sans (the D5 defect itself).

## Install
- `apply_variant.py --target nl --reader zh-cn` (mode cjk). svglib md5 → `44a000db7b2e4fe344770e7cbac182ba`. Routing assert: FAILURES 0 (fix2 U+201C/U+201D/U+2019 → news preserved).

## Defect found + fixed (D5-caused, 1 item)
- `HEAD TOO WIDE [P2-feature]: DRIE DINGEN VOOR 5 DECEMBER` — 25pt advance 451.8px > col 422.5px. Fix: `content12.py:175` head 25 → 23pt (415.6px). Text unchanged. P2 card crop verified by eye: head inside column 1, no collision.
- Same 25 → 23pt fix ported to all 7 Latin/Russian-reader fan-outs' `content12.py`; D11 fix5 (content34.py 62 → 89) ported to all 7 fan-outs (pre-existing P4 spill there). CJK-reader fan-outs untouched (no CJK decision yet).

## Gates (final rebuild-2, after fix)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| render.py / webpdf.py | RC 0; web 1,874,709 B < 7 MB, 44,127 text bytes |
| p8 extract | 150/150 |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs pre-D5 | added CJK 0, added Latin strings 222 (run-splitting, expected) |
| occlusion | 0 flags |
| spill | 0 SPILL (58 OBSERVE) |
| boxtitle | 0 DEFECT (25 titles) |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (n=381, median 1.04; P8 lines 220→220, slack 54.0px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| text layer | print = web = 44,127 bytes, word multiset diff 0 |
| orphan sweep | (a) 0; (b) 1 candidate `）集。` P5 — pre-existing in pre-D5 baseline, not D5-caused |

## New SHAs (final)
- print `De-Lucerna-VOL4.pdf` `0c5d63b942d2a024694e87ba27b85b3eff0b3d411e78f9956094b5f2a4383be4` — 13,830,540 B
- web `De-Lucerna-VOL4-web.pdf` `2b6f223eaff9afa7445c54b385213e8131eeddf11b9ae9a139388b32da7f940d` — 1,874,709 B
- text.md `0b97a48dc248c9cf3dc28f21b55e06a1e0dc7dea7db5f6e46e55f2f2fed7050c` — 44,093 B, **byte-identical to pre-D5**
- Only `p2-leven.svg` differs between D5 rebuild 1 and 2 (head fix); other 7 SVGs identical.

## Notes
- Print-PDF size 25,955,680 → 13,830,540 B: stale-baseline artifact, not content loss. Evidence: same render.py/venv; all 7 fan-out pre-D5 print PDFs ≈12.66 MB with byte-identical embedded-image tables; this rebuild's PDF has 8 pages, 7 images, all fonts embedded+subsetted, text layer = web. Recorded in KIT §18.
- Creambox audit initially failed (phase-A snapshot lacked `baseline-ed/svglib.py` + `assets/lucerna-moth.svg`); both restored, `phaseA.sh` patched.
- First D5 rebuild passed all gates except the P2 HEAD TOO WIDE; a re-run was cut by a service restart at 07:31 UTC (SVGs regenerated, run.log lost at 0 bytes); rebuild-2 re-ran everything from install onward.
- KIT: §7 sizes + new §18 (dated rebuild record, history preserved). Build-copy `post/freeze/build-copy` deleted after verification; scratch now 3.6 MB.
- No commit, no push, no `lint.mjs --write`.
