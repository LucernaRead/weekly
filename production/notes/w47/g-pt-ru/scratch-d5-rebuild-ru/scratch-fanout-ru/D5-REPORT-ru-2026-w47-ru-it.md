# D5-REPORT — ru-it (2026-w47)

- Edition: `2026-w47-ru-it` (target ru, reader it, mode latin, `_D5_READER = "latin"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader it`
  (per PILOT-REPORT install method; CJK-DECISION.md §1–§3 + brief-d5-rebuild.md read).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-it/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-it/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-checked against the production
  files themselves (not a scratch copy).

## Install

- Pre-fix `svglib.py` md5 `27f11789af7c828e47ca14eb00c1dded` (no fix2;
  unkerned run-measurement fix present) → post-install
  `2e87fef862607133a962c0ee981bd0a6` (fix2 added by the installer + D5).
- `assert_routing.py` (latin→news): all assertions pass, fix2 routing preserved.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK); pre-fix run.log 0 HEAD TOO WIDE,
  0 FLOW OVERFLOW, TOTAL 150.

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 430 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (2 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0, first pass already normal (20,877,046 B — no font-subset
  explosion of the ru-es kind); `webpdf.py` RC=0, 57,852 text bytes.
- text.md byte-identical: SHA-256
  `0bb5739a9e2a1215074b8d5cba566736e88cd84d45f3bc28eb0fe5a8966f5989` (63,972 B).

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-it.pdf`: `12f897b2…` 21,263,401 B →
  **`6b79403a69c526e1fe71057322b02298a68ef876a7903f3ecf1c2e0ba05b04d5` 20,877,054 B**
- Web `Lucerna-VOL4-ru-it-web.pdf`: `6fce91e4…` 3,381,661 B →
  **`7c2ecb0479b1ce8ad7a7f192b7355aaa58f90ce7994efbf71a5c304b8365181f` 3,330,486 B**
  (< 7 MB; print/web text layers byte-identical, 38,608 chars each)
- Production `svglib.py` contains `_D5_READER` (verified); KIT §5 synced to
  the SHAs above.

## Defects found by D5 (2, both fixed; text unchanged, font size only; both cream-box titles)

1. P1 `СМИ　COSA DICONO I MEDIA` over right +23.4px (creambox + boxtitle agree;
   flagged as BODY because the box holds the P1 "in this issue" media line).
   Fix: `content12.py:73` size 27→25pt (advance 424.2→392.8 vs box inner width
   400.5, ~7.7px margin; 26pt still over by 8.0px).
2. P7 `ОШИБКИ　CLINICA DEGLI ERRORI` over right +24.6px (creambox + boxtitle agree).
   Fix: `content7.py:77` size 23→21pt (advance 425.5→388.5, ~12.0px margin;
   22pt still over by 6.5px).
   Full rebuild + full gates re-run after the fixes. Card crops of both fixed
   titles were read visually and confirmed inside their boxes with margin.

NOT fixed (voided false positive): PILOT-REPORT §5.4 en-ru P8 key-row
"collisions" — voided by CJK-DECISION.md §2 (occlusion_audit.py measured
bare `Noto Sans` runs on the CJK SC face; U+00B7 full-width). No P8 key
row was touched. This edition's P8 ran 0 occlusion flags with the fixed tool.

## Gates (post-fix rebuild, GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs core-ru
  CLEAN (keydiff=[137, 138, 139, 140], expected reader-language keys).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0 (added Latin strings 147 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (55 titles, 684 body lines — down from 57/682 pre-fix because the two
  shrunk heads fell below the tool's title-size threshold; classification
  only, 0 defects); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 229→229, slack_footer 44.5→44.5px; ratios n=399, median 1.040,
  bold median 1.049).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (38,608 chars).
- P8 Morozko SKIPPED by the build's own condition — as before,
  by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §7 appended with the D5 record; §5 PDF SHAs/sizes updated
  to the new values above. History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
