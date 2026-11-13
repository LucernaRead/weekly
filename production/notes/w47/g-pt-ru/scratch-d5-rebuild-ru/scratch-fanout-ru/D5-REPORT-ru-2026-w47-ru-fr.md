# D5-REPORT — ru-fr (2026-w47)

- Edition: `2026-w47-ru-fr` (target ru, reader fr, mode latin, `_D5_READER = "latin"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader fr`
  (per PILOT-REPORT install method; CJK-DECISION.md §1–§3 + brief-d5-rebuild.md read).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-fr/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-fr/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-checked against the production
  files themselves (not a scratch copy).

## Install

- Pre-fix `svglib.py` md5 `b0928993747a13e94573a5dcced00961` (fix2 already present,
  unkerned run-measurement fix present) → post-install `662f031c1bdcab4e01137c425cc761d9`.
- `assert_routing.py` (latin→news): all assertions pass, fix2 routing preserved.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK); pre-fix run.log 0 HEAD TOO WIDE,
  0 FLOW OVERFLOW, TOTAL 150.

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 434 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (4 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0; `webpdf.py` RC=0, 58,025 text bytes.
- text.md byte-identical: SHA-256
  `e4cc50fd4195ed1adb7051c684c894c5a3b3091aa643cf3bab96690178e22a46` (63,361 B).

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-fr.pdf`: `79e75523…` 21,264,368 B →
  **`7dbe1f0d67160eb6e33d563e7b36b142e93d00b4b4d7ee616636f2f1ff79b736` 20,880,952 B**
- Web `Lucerna-VOL4-ru-fr-web.pdf`: `671dbbca…` 3,383,213 B →
  **`6841ac9686540a6467b741abe0e8fdcf5c9ed9c69414e76ae5c8f6aec6ef9a76` 3,334,434 B**
  (< 7 MB; print/web text layers byte-identical, 38,524 chars each)
- Production `svglib.py` contains `_D5_READER` (verified); KIT §5 synced to
  the SHAs above.

## Defects found by D5 (3, all fixed; text unchanged, font size only; all cream-box titles)

1. P1 `В ЭТОМ НОМЕРЕ　AU SOMMAIRE` over right +19.4px (creambox + boxtitle agree).
   Fix: `content12.py:91` size 24→22pt (advance 418.7→383.8 vs box inner width
   400.5, ~16.7px margin).
2. P6 `ЗА И ПРОТИВ　POUR ET CONTRE` over right +19.4px (creambox + boxtitle agree).
   Fix: `content56.py:136` size 24→22pt (same numbers).
3. P7 `СЛОВО　LE MOT DE LA SEMAINE` over right +8.4px (creambox + boxtitle agree).
   Fix: `content7.py:88` size 23→22pt (advance 408.8→391.0, ~9.5px margin).
   The P1 full-width word head `СЛОВО НЕДЕЛИ　LE MOT DE LA SEMAINE`
   (`content12.py:109`, 22pt) had no defect and was left alone.
   Full rebuild + full gates re-run after the fixes. (A runtime restart
   interrupted the first post-fix gates run after boxtitle had already passed
   0 DEFECT; the gates were re-run in full — GATES_OVERALL_FAIL=0.)

NOT fixed (voided false positive): PILOT-REPORT §5.4 en-ru P8 key-row
"collisions" — voided by CJK-DECISION.md §2 (occlusion_audit.py measured
bare `Noto Sans` runs on the CJK SC face; U+00B7 full-width). No P8 key
row was touched. This edition's P8 ran 0 occlusion flags with the fixed tool.

## Gates (post-fix rebuild, GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs core-ru
  CLEAN (keydiff=[137, 138, 139, 140], expected reader-language keys).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0 (added Latin strings 144 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (57 titles, 682 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 229→229, slack_footer 44.5→44.5px; ratios n=401, median 1.040,
  bold median 1.049).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (38,524 chars).
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
