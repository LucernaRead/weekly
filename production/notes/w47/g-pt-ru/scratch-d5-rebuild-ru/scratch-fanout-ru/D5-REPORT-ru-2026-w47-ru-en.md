# D5-REPORT — ru-en (2026-w47)

- Edition: `2026-w47-ru-en` (target ru, reader en, mode latin, `_D5_READER = "latin"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader en`
  (per PILOT-REPORT install method; CJK-DECISION.md §1–§3 + brief-d5-rebuild.md read).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-en/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).

## Install

- Pre-fix `svglib.py` md5 `27f11789af7c828e47ca14eb00c1dded` (no fix2 block yet,
  unkerned run-measurement fix present) → post-install
  `2e87fef862607133a962c0ee981bd0a6` (fix2 block added by the installer + D5 block).
- `assert_routing.py` (latin→news): all assertions pass, fix2 routing preserved.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK); pre-fix run.log 0 HEAD TOO WIDE,
  0 FLOW OVERFLOW, TOTAL 150.

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 433 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (2 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0; `webpdf.py` RC=0, 57,370 text bytes.
- text.md byte-identical: SHA-256
  `5dba645578989ed58673b060b6c67e6df844335f82a1ba351012f66e5c9404df` (62,786 B).

## New PDFs

- Print `Lucerna-VOL4-ru-en.pdf`: `e29ba5fa…` 21,248,719 B →
  **`f20b04c8244c911d10409f2303a35fb1d541e2790c15c98b0f6107c44164c75c` 20,875,448 B**
- Web `Lucerna-VOL4-ru-en-web.pdf`: `7a3f6351…` 3,378,370 B →
  **`21781f8396d9d936b23595eff234d3f712adb822dd95be049dd428dd2043ad95` 3,328,931 B**
  (< 7 MB; print/web text layers byte-identical, 38,166 chars each)

## Defects found by D5 (2, both fixed; text unchanged, font size only; both P1 cream-box titles)

1. `СМИ　WHAT THE MEDIA SAY` over right +24.4px (creambox + boxtitle agree).
   Fix: `content12.py:77` size 27→25pt (advance 424.4→393.0 vs box inner width
   400.5, ~7.5px margin).
2. `В ЭТОМ НОМЕРЕ　IN THIS ISSUE` over right +6.4px (creambox + boxtitle agree).
   Fix: `content12.py:95` size 24→23pt (advance 405.3→388.5, ~12px margin).
   Sibling title `О ЧЁМ ПИШУТ` (27pt) had no defect and was left alone.
   Full rebuild + full gates re-run after the fixes; P1 card crops visually
   confirmed both titles inside their boxes.

NOT fixed (voided false positive): PILOT-REPORT §5.4 en-ru P8 key-row
"collisions" — voided by CJK-DECISION.md §2 (occlusion_audit.py measured
bare `Noto Sans` runs on the CJK SC face; U+00B7 full-width). No P8 key
row was touched. This edition's P8 ran 0 occlusion flags with the fixed tool.

## Gates (post-fix rebuild, GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs core-ru
  CLEAN (keydiff=[137, 138, 139, 140], expected reader-language keys).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0 (added Latin strings 146 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (57 titles, 685 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 244→244, slack_footer 47.5→47.5px; ratios n=402, median 1.040,
  bold median 1.049).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (38,166 chars).
- P8 «Морозко» image SKIPPED by the build's own condition — as before,
  by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §7 appended with the D5 record; §5 PDF SHAs/sizes updated
  to the new values above. History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
