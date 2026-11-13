# D5-REPORT — 2026-w47-nl-ja (Dutch core, Japanese readers)

Date: 2026-11-12 (UTC). Status: **DONE, all gates green in top-level production** (independent re-proof is the coordinator's separate step). First D5 build of this edition (the first D5 worker never started the CJK reader editions).

## Pre-D5 baseline (top-level, verified on disk)
- svglib md5 `ae9985696bf2f828e53eab9894d73cb4`; print `f78ffe324aaf24d39fa71cc815b96d6c163cf2747c27a10d7633e94cb41943b0` 26,049,309 B; web `591836f2de9ddf6609658c0fe101e6cfad60d4aa49aa4287989a3815be40248a` 2,155,393 B; text.md `060bfdea243483edb1a30691ff26291eac1a90bc69f2ea4c38fe97eac05bb93a` 47,801 B.
- Pre-D5 gates: TOTAL 150, 0 HEAD TOO WIDE, occlusion 0, spill 0 (P4 D11 already fixed in production), boxtitle 1 DEFECT (P6 +2.5px, pre-existing), edge 0; census FAIL 336 Latin-in-CJK-sans. `run.py` pre-run reproduced on-disk SVGs 8/8 byte-identical.

## Install
- `apply_variant.py --target nl --reader ja` (mode cjk — character-script routing, no `_READER_LANG` gate, per CJK-DECISION §1; CJK index SC → JP; kinsoku already present). svglib md5 → `910444d24366a0cc60c970e49847dcea`. Routing assert: FAILURES 0.

## Fixes (layout only, text unchanged)
- Ported: P4 HET PROGRAMMA box `sh = 62 + …` → `89 + …` was already in production (build 6).
- 3 D5-caused defects found in rebuild-1 (widened Latin head pushes the CJK tail out of the box — the en-ja pilot class), all fixed by size only:
  1. HEAD TOO WIDE [P2-feature]: `DRIE DINGEN VOOR 5 DECEMBER` 25 → 23pt
  2. P2 `ZO ONTHOUD JE HET　こう覚えよう` over +21.0px → f.box tsize 23 → 21
  3. P6 `DE GRAFIEK　グラフ（練習データ）` over +25.6px (was +2.5px pre-D5) → 24 → 21pt

## Gates (final rebuild-2, in top-level production)
| gate | result |
|---|---|
| run.py | TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE |
| head_check.py | PASS 0 defects |
| render.py / webpdf.py | RC 0; web 1,968,009 B < 7 MB, 47,834 text bytes |
| p8 extract | 150/150 |
| p8 compare vs core-nl | CLEAN, keydiff=[137, 138] (reader-language keys) |
| freeze baseline | 8/8 byte-identical |
| freeze diff vs core-nl | added CJK 3315 (JP text in Noto Sans CJK JP); added Latin strings 74 |
| freeze diff vs pre-D5 baseline | added CJK 0; added Latin strings 216 (run-splitting) |
| occlusion | 0 flags |
| spill | 0 SPILL (67 OBSERVE) |
| boxtitle | 0 DEFECT |
| edge | 0 TOUCH, 0 NEAR |
| creambox audit | PASS 0 defects (P8 lines 230→230, slack 39.4px) |
| d5 census | PASS: D5 Latin 0, Cyrillic 0, curly-in-CJK 0 |
| census_quotes.py | 0 defective |
| text layer | print = web = 47,834 bytes, word multiset diff 0 |
| orphan sweep | (a) 0, (b) 0 |

## New SHAs (final, verified on production files)
- print `De-Lucerna-VOL4-nl-ja.pdf` `67aeebb40b5820193277cfea8a05b075849612f4d2e7e75a4e021485953702bc` — 18,803,852 B
- web `De-Lucerna-VOL4-nl-ja-web.pdf` `9a4b3dbd5dad2ec271e699d39e49c2820af4d7c2770e172bb61b68fe9700af07` — 1,968,007 B
- **Repro check (2026-11-12, third worker):** `render.py` re-ran in place and reproduced the print PDF byte-identically; `webpdf.py` re-ran and produced a new web SHA `9a4b3dbd5dad2ec271e699d39e49c2820af4d7c2770e172bb61b68fe9700af07` (1,968,007 B; rebuild output was `6840df0c1e61710d944b539a10241e6b1ae480f4702eff0bbb2bbc9f51d1714d`, 1,968,009 B — kept here as history). Content-equivalent: pdftotext 47,834 B identical; `textlayer.py` re-run vs the new web PDF: RC 0, word multiset diff 0, char streams equal, orphan (a)/(b) 0. The KIT "Files delivered" is synced to the new production file.
- text.md `060bfdea243483edb1a30691ff26291eac1a90bc69f2ea4c38fe97eac05bb93a` — 47,801 B, **byte-identical to pre-D5**

## Notes
- KIT synced in production (Files delivered + new D5 rebuild section; history preserved). No commit, no push, no `lint.mjs --write`.
- Logs: `hidden_files/w47/scratch-d5-redo-nl/2026-w47-nl-ja/` (`rebuild-1.log` = defect discovery, `rebuild-2.log` = final green).
