# D5-REPORT — ru-ko (2026-w47)

- Edition: `2026-w47-ru-ko` (target ru, reader ko, mode **cjk**, `_D5_READER = "cjk"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader ko`
  (per CJK-DECISION.md §1: script-based routing, NO `_READER_LANG` gate;
  same gates as Latin editions; brief-d5-rebuild.md §4 for fixes).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-ko/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-ko/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-checked against the production
  files themselves (not a scratch copy).
- **CJK set:** ru-ko is the 2nd of 3 CJK reader editions (ja done, ko done,
  zh-tw remains). Latin set (de, en, fr, es, it, pt, nl) is complete.

## Install

- Pre-fix `svglib.py` md5 `27f11789af7c828e47ca14eb00c1dded` (no fix2;
  unkerned run-measurement fix present) → post-install
  `33cb3a37bca478bbf4952ae6c6d974fd` (fix2 added by the installer + D5;
  CJK index SC → KR).
- `assert_routing.py` (latin-class arg `news`, same for cjk mode):
  all assertions pass, fix2 routing preserved, CJK stays in CJK sans.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK); pre-fix run.log 0 HEAD TOO WIDE,
  0 FLOW OVERFLOW, TOTAL 150.

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 206 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (2 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

(KR/JP quotes NOT extended — CJK-DECISION.md §3; KR U+201C/U+201D advance
474/574, narrow like Newsreader. `census_quotes.py` counts only SC/TC/HK
as defective — correct, unchanged.)

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0, first pass already normal (21,975,314 B — no font-subset
  explosion of the ru-es/ru-ja kind); `webpdf.py` RC=0, 58,749 text bytes.
- text.md byte-identical: SHA-256
  `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe` (65,012 B).

## ko freeze exception — NOT triggered

- The brief warned `freeze.py` demands Pillow 10 for ko paths, so the venv
  (Pillow 13) freeze might ABORT, with a one-time system-python3 run as the
  only permitted fallback. In this edition the venv freeze baseline ran
  **8/8 byte-identical with no abort** — the exception was never needed.
  System python3 was confirmed beforehand to carry Pillow 10.2.0 (available
  as a standby, never used). No path was renamed, no gate was bypassed.

## Hangul `_run_w` fix still in place

- The pre-D5 `_run_w` Hangul fix (whole-string `getlength` for Hangul runs;
  see KIT §7 "Rebuild") survives D5 unchanged: no regression — P7
  `Страница` page references show no overlap (occlusion 0 flags), and the
  P7 junctions were already verified on the synced print PDF.

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-ko.pdf`: `62538d21…` 22,005,230 B →
  **`2f6ecdcc2abf2277e7994602416e873187b944c23c70d1606086d577dac12085` 21,975,314 B**
- Web `Lucerna-VOL4-ru-ko-web.pdf`: `e996c1f3…` 3,510,669 B →
  **`a2ea1b41922aaf66feefe9165e96cdf4eba69fcfcbc799f1340a34322e9d070f` 3,494,622 B**
  (< 7 MB; print/web text layers byte-identical, 33,867 chars each)
- Production `svglib.py` contains `_D5_READER` (verified, value `cjk`);
  KIT §5 synced to the SHAs above.

## Defects found by D5 (0)

- First gates run was fully green — no fixes needed.
- No P8 key-row work: PILOT-REPORT §5.4 en-ru P8 key-row "collisions" —
  voided by CJK-DECISION.md §2 (occlusion_audit.py measured bare `Noto Sans`
  runs on the CJK SC face; U+00B7 full-width). No P8 key row was touched.
  This edition's P8 ran 0 occlusion flags with the fixed tool.

## Gates (GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs core-ru
  CLEAN (keydiff=[137, 138, 139, 140], expected reader-language keys).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0 (added Latin strings 67 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (67 titles, 759 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 242→242, slack_footer 45.7→45.7px; ratios n=393, median 1.028,
  bold median 1.040).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (33,867 chars).
- P8 Morozko SKIPPED by the build's own condition — as before,
  by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §7 appended with the D5 record (including the untriggered
  ko freeze exception); §5 PDF SHAs/sizes updated to the new values above.
  History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
