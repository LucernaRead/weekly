# D5-REPORT — ru-zh-tw (2026-w47)

- Edition: `2026-w47-ru-zh-tw` (target ru, reader zh-tw, mode **cjk**,
  `_D5_READER = "cjk"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader zh-tw`
  (per CJK-DECISION.md §1: script-based routing, NO `_READER_LANG` gate;
  same gates as Latin editions; brief-d5-rebuild.md §4 for fixes).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-zh-tw/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-zh-tw/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-checked against the production
  files themselves (not a scratch copy).
- **CJK set complete:** ru-zh-tw is the 3rd of 3 CJK reader editions (ja, ko,
  zh-tw all done). This is the LAST of the 11 ru-family editions
  (core-ru + 10 fan-out; 11/11 done).

## Install

- Pre-fix `svglib.py` md5 `b0928993747a13e94573a5dcced00961` (fix2 already present,
  ported 2026-11-12 per KIT §9; unkerned run-measurement fix present)
  → post-install `d6e0a93d27c8366de20a16fa4a38cc20` — the SAME md5 as core-ru's
  D5 svglib (both are zh-tw-based CJK; reader zh-tw uses the core-zh-tw base).
  The installer did NOT re-add fix2 (already present) and added the D5 sans
  block + `_D5_READER = 'cjk'`; CJK index SC → TC.
- `assert_routing.py` (latin-class arg `news`, same for cjk mode):
  all assertions pass, fix2 routing preserved, CJK stays in CJK sans.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK); pre-fix run.log 0 HEAD TOO WIDE,
  0 FLOW OVERFLOW, TOTAL 150.

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 207 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (422 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (4 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

(TC/JP/KR quotes NOT extended — CJK-DECISION.md §3; only SC/TC/HK defective
U+201C/U+201D are 1000/1000em. `census_quotes.py` counts only SC/TC/HK as
defective — correct, unchanged.)

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0, first pass already normal (24,763,703 B — no font-subset
  explosion of the ru-es/ru-ja kind); `webpdf.py` RC=0, 56,175 text bytes.
- text.md byte-identical: SHA-256
  `277a24f8a1674c970a367bf4fc8cccdd85d3f88941f85d633713a0e525ee6c83` (60,850 B).

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-zh-tw.pdf`: `810514b2…` 24,784,623 B →
  **`a6c1b4cffbefec3a600eedd5a7cc7c03beed488041f988b4ba90ced2901f1a8c` 24,763,703 B**
- Web `Lucerna-VOL4-ru-zh-tw-web.pdf`: `0cef86ea…` 3,992,151 B →
  **`8eb6f61cef467f5a66c77b66133809df7a1488fd857332d49baadb7e6a7e15c8` 3,976,325 B**
  (< 7 MB; print/web text layers byte-identical, 32,556 chars each)
- Production `svglib.py` contains `_D5_READER` (verified, value `cjk`);
  KIT §1 table synced to the SHAs above.

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
  (57 titles, 703 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 225→225, slack_footer 33.2→33.2px; ratios n=393, median 1.026,
  bold median 1.040).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (32,556 chars).
- Morozko SURVIVES as before (P8 keys end 2188.39, image 422.5×250 at
  y=2212.39 — same as the pre-D5 record in KIT §9).

## KIT

- `WEEKLY-KIT.md` §1 deliverables table updated to the new SHAs/sizes;
  header status line updated (D5 = Build 3, current); new §10 D5 record
  appended. History preserved (pre-fix SHAs remain in §9).
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
