# D5-REPORT — core-ru (2026-w47)

- Edition: `core-ru` (target ru, reader zh-cn, mode **cjk**,
  `_D5_READER = "cjk"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader zh-cn`
  (per CJK-DECISION.md §1: script-based routing, NO `_READER_LANG` gate;
  same gates as Latin editions; brief-d5-rebuild.md §4 for fixes).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/core-ru/`
  (baseline/ = pre-fix svg + svglib.py + assets; the creambox-audit baseline
  copy initially missed `assets/lucerna-moth.svg` — copied in 06:56, then
  creambox passed and the full gates re-run passed).
- **Build location: IN PLACE in production** (`production/2026-w47/core-ru/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-verified against the production
  files themselves on 2026-11-12 (see "Final production verification").
- **Core:** the 11th of 11 ru-family editions (core + 10 fan-out).
  This edition's Cyrillic was already correctly routed pre-D5 (422 elements in
  Noto Sans, 0 Cyrillic in CJK Sans); D5 fixed only its 207 Latin runs.

## Install

- Pre-fix `svglib.py` md5 (fix2 present) → post-install
  `d6e0a93d27c8366de20a16fa4a38cc20` (`_D5_READER = "cjk"`; CJK index SC).
- `assert_routing.py` (latin-class arg `news`, same for cjk mode):
  all assertions pass, fix2 routing preserved, CJK stays in CJK sans.
- Baseline verified clean BEFORE install: pre-fix `run.py` rebuild reproduced the
  delivered 8 SVGs byte-identically (8/8 sha256 OK).

## Census (pre → post)

| check | pre | post |
|---|---|---|
| D5 Latin in CJK Sans | 207 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (422 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (4 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` PASS 0 defects.
- `render.py` RC=0; `webpdf.py` RC=0, 3,898,257 B (< 7 MB), 56,087 text bytes.
- text.md byte-identical: SHA-256
  `348511e061c28019b56d81b84f90013e086b6369cb6f2a9483c2fb0cb0bf717`
  (60,953 B; both `2026-w47-ru-core.text.md` and
  `2026-w47-ru-zh-cn.text.md` carry this SHA).

## New PDFs (verified in production)

- Print `Lucerna-VOL4.pdf`: `09680fb5…` 31,426,216 B →
  **`e3c4c0ee155a96a96a56a70326e4df0e0572705e2fff3457599f361b929b60bf` 24,713,345 B**
- Web `Lucerna-VOL4-web.pdf`: `03d1b6f4…` 4,023,396 B →
  **`0bdc87e621d75bb35d4a507463237fa05748dfaf1e67090926e68afb58ba45af` 3,898,257 B**
  (< 7 MB; print/web text layers byte-identical, 32,613 chars each)
- Production `svglib.py` contains `_D5_READER` (verified, value `cjk`);
  KIT §9 synced to the SHAs above.

## Defects found by D5 (0)

- Zero content defects, zero fixes. The only gates hiccup was the creambox
  audit crashing on a missing baseline asset (`assets/lucerna-moth.svg`),
  a scratch-copy issue, not an edition defect — fixed by copying the asset
  into the baseline, then full gates re-run green.
- No P8 key-row work: PILOT-REPORT §5.4 en-ru P8 key-row "collisions" —
  voided by CJK-DECISION.md §2 (occlusion_audit.py measured bare `Noto Sans`
  runs on the CJK SC face; U+00B7 full-width). No P8 key row was touched.

## Gates (GATES_OVERALL_FAIL=0)

- D5 census PASS (0/0/0); quotes census 0; `head_check.py` PASS 0 defects.
- `run.py` TOTAL 150; `p8.py extract` 150/150; `p8.py compare` vs baseline
  CLEAN (keydiff=[] — core is its own baseline).
- `freeze.py baseline` 8/8 byte-identical; freeze-diff vs pre-fix baseline:
  added CJK chars 0.
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (57 titles, 704 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 237→237, slack_footer 55.0→55.0px; ratios n=395, median 1.026,
  bold median 1.040).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (32,613 chars).

## KIT

- `WEEKLY-KIT.md` §7.7 D5 record appended; §9 print/web SHA + sizes updated.
  History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
