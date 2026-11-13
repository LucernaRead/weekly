# D5-REPORT — ru-ja (2026-w47)

- Edition: `2026-w47-ru-ja` (target ru, reader ja, mode **cjk**, `_D5_READER = "cjk"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader ja`
  (per CJK-DECISION.md §1: script-based routing, NO `_READER_LANG` gate;
  same gates as Latin editions; brief-d5-rebuild.md §4 for fixes).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-ja/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-ja/`).
  The only build-copy was the gates' `freeze/` rebuild output, deleted after
  verification. Production SHAs below were re-checked against the production
  files themselves (not a scratch copy).
- **CJK set:** ru-ja is the 1st of 3 CJK reader editions (ja, ko, zh-tw).
  Latin set (de, en, fr, es, it, pt, nl) is complete.

## Install

- Pre-fix `svglib.py` md5 `27f11789af7c828e47ca14eb00c1dded` (no fix2;
  unkerned run-measurement fix present) → post-install
  `55830cada181d404325569fb24426b08` (fix2 added by the installer + D5;
  CJK index SC → JP; kinsoku block ported from core-zh-tw).
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

(KR/JP quotes NOT extended — CJK-DECISION.md §3; JP U+201C/U+201D advance
474/574, narrow like Newsreader. `census_quotes.py` counts only SC/TC/HK
as defective — correct, unchanged.)

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0 (second run; see incident below);
  `webpdf.py` RC=0, 58,604 text bytes.
- text.md byte-identical: SHA-256
  `07824474bb88439bea67fb4d1dc3ede956f33b006a32e8203e5b52081c1090da` (64,477 B).

## Incidents (both handled, neither entered any gate)

1. **SIGTERM kill mid-build:** the first build session was killed by SIGTERM
   (runtime restart) during `run.py`, after install + routing had completed.
   State check: run.py had written p1–p7 with D5 content (census D5_lat=0),
   but p8 was still pre-fix (md5 identical to the baseline snapshot).
   Recovery: install was complete (svglib `55830cad`), so NO re-install —
   `run.py` was simply re-run in full (deterministic, regenerates all 8 SVGs).
2. **Font-subset explosion (first render):** the first `render.py` produced a
   **73,026,666 B** print PDF (SHA `f0ac7a1a…`) holding **6,730 font objects**
   (thousands of NotoSerif-Medium / Newsreader / NotoSerifCJKjp subsets;
   siblings: ~72). A fresh single-page re-render of p1 was clean
   (7,061,374 B, 11 font refs). Same transient class as the ru-es incident
   (parallel-render/fontconfig contention). Re-running `render.py` produced
   a normal print PDF (27,365,531 B, 72 font refs) and regenerated the cards.
   The anomalous PDF never entered any gate; all gates below ran on the
   clean re-render.

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-ja.pdf`: `38a6efb0…` 27,407,117 B →
  **`f65820348befa4fff7103b816fe4195dd9951f54ae04cb9730916957a3f7e40d` 27,365,531 B**
- Web `Lucerna-VOL4-ru-ja-web.pdf`: `89973dd7…` 3,719,047 B →
  **`b6fed518a3c1ad5ec845ae5dbb8c61b3599e55a9c6a106478136670a4f1ea801` 3,692,485 B**
  (< 7 MB; print/web text layers byte-identical, 33,280 chars each)
- Production `svglib.py` contains `_D5_READER` (verified, value `cjk`);
  KIT §5 synced to the SHAs above.

## Defects found by D5 (0)

- First gates run was fully green — no fixes needed, no rebuild after the
  clean re-render. (The en-ja pilot had 5 defects; this edition's Japanese
  glosses all fit their boxes.)
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
  (57 titles, 716 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 224→224, slack_footer 46.7→46.7px; ratios n=394, median 1.028,
  bold median 1.040).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (33,280 chars).
- P8 Morozko SKIPPED by the build's own condition — as before,
  by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §7 appended with the D5 record (including both incidents);
  §5 PDF SHAs/sizes updated to the new values above. History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
