# D5-REPORT — ru-de (2026-w47)

- Edition: `2026-w47-ru-de` (target ru, reader de, mode latin, `_D5_READER = "latin"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader de`
  (per PILOT-REPORT install method; CJK-DECISION.md §1–§3 + brief-d5-rebuild.md read).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-de/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).

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
| D5 Latin in CJK Sans | 433 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (3 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0; `webpdf.py` RC=0, 57,833 text bytes.
- text.md byte-identical: SHA-256
  `d0f9b48c8fab4df8bb39acfdfebfbc6ad6cf0f09e75891449d13a0f1ce2dcc0f` (63,471 B).

## New PDFs

- Print `Lucerna-VOL4-ru-de.pdf`: `e78581ab…` 21,229,209 B →
  **`0aa0287b13ea7169176754e0eb9ead35b9b4698ce2351575eb8d1b13c69f12cd` 20,880,795 B**
- Web `Lucerna-VOL4-ru-de-web.pdf`: `956a6b62…` 3,383,497 B →
  **`98f015bd027be573661b3a88bfd79a0d46a584b479ccb2ab0ad4d9f053df9200` 3,334,227 B**
  (< 7 MB; print/web text layers byte-identical, 38,463 chars each)

## Defects found by D5 (2, both fixed; text unchanged, font size only)

1. P6 cream-box title `ЗА И ПРОТИВ　PRO UND CONTRA` over right +26.4px
   (creambox + boxtitle agree; pre-fix +1.1px OBSERVE). Cause: bold Latin head
   widened in Newsreader SemiBold. Fix: `content56.py:136` size 24→22pt
   (advance 425.9→390.4 vs box inner width 400.5, ~10px margin).
2. P8 head/subtitle same-baseline collision: `ОТВЕТЫ　LÖSUNGEN — NACH SEITEN
   GEORDNET; AUFGABENNUMMER SUCHEN` (25pt bold) ink overlapped right-anchored
   subtitle `Jede Lösung mit einer kurzen deutschen Erläuterung …` by
   86.5×19.0px (occlusion TEXTX; same class as en-fr P1). Fix:
   `content8.py:116` head size 25→22pt (advance 1077.3→948.0, ~43px gap;
   subtitle untouched). Full rebuild + full gates re-run after the fixes;
   P8/P6 card crops visually confirmed clean (head clear of subtitle,
   title inside its box).

NOT fixed (voided false positive): PILOT-REPORT §5.4 en-ru P8 key-row
"collisions" — voided by CJK-DECISION.md §2 (occlusion_audit.py measured
bare `Noto Sans` runs on the CJK SC face; U+00B7 full-width). No P8 key
row was touched. This edition's P8 ran 0 occlusion flags with the fixed tool.

## Gates (post-fix rebuild, GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs core-ru
  CLEAN (keydiff=[137, 138, 139, 140], expected reader-language keys).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0 (added Latin strings 143 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (57 titles, 682 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 254→254, slack_footer 46.5→46.5px; ratios n=400, median 1.040,
  bold median 1.049).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (38,463 chars).
- P8 Morozko SKIPPED by the build's own condition (keys end 2331.72) — as
  before, by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §6 appended with the D5 record; §4 PDF SHAs/sizes updated
  to the new values above. History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
