# D5-REPORT — ru-es (2026-w47)

- Edition: `2026-w47-ru-es` (target ru, reader es, mode latin, `_D5_READER = "latin"`)
- Date: 2026-11-12 (UTC). Builder: W47 D5 ru-family worker.
- Mechanism: `scratch-d5-plan/mechanism/apply_variant.py --target ru --reader es`
  (per PILOT-REPORT install method; CJK-DECISION.md §1–§3 + brief-d5-rebuild.md read).
- Build interpreter: `tools/venv/bin/python` throughout (Pillow 13.0.0). No system python3.
- Scratch: `hidden_files/w47/scratch-d5-rebuild-ru/scratch-fanout-ru/2026-w47-ru-es/`
  (baseline/ = pre-fix svg + svglib.py + assets; backup/ = same copy for boxtitle).
- **Build location: IN PLACE in production** (`production/2026-w47/2026-w47-ru-es/`).
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
| D5 Latin in CJK Sans | 429 | **0** |
| D5 Cyrillic in CJK Sans | 0 | 0 (417 Noto Sans elements, unchanged) |
| curly quotes in CJK Sans | 0 | 0 (2 total, all Newsreader) |
| `census_quotes.py` defective | 0 | **0** |

## Builds

- `run.py` RC=0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE;
  `head_check.py` (run.log vs base-run.log) PASS 0 defects.
- `render.py` RC=0; `webpdf.py` RC=0, 57,962 text bytes.
- text.md byte-identical: SHA-256
  `332c8e4f5478181d21281fe059483f0da4ee2bf5e39fec4464f836049e2bad60` (64,176 B).

## Render incident (first render discarded, never gated)

- The first `render.py` run produced a **47,719,959 B** print PDF (SHA
  `0bd972dd…`). Diagnosis: font-subset explosion — the PDF held **10,164 font
  objects** (siblings: ~59) with random subset prefixes, while image bytes
  were **identical** to ru-fr (20,383,251). A fresh single-page re-render of
  p1 was normal (6,099,711 B, 10 font refs, same as ru-fr p1). Root cause:
  transient failure under heavy parallel-render contention (several families'
  workers rendering at the same time; fontconfig-cache interference suspected).
  Re-running `render.py` produced a normal print PDF (20,880,148 B) and
  regenerated the cards. The anomalous PDF never entered any gate; all gates
  below ran on the clean re-render. (Same class of transient may hit other
  editions — if a print PDF comes out ~2× the sibling size, re-run render.py
  and check the font-object count before gating.)

## New PDFs (verified in production)

- Print `Lucerna-VOL4-ru-es.pdf`: `deb7b08e…` 21,276,149 B →
  **`047ef0fbf75a7e47cdbe1267e28084b1c4953d48e18d9d6cbabe924ad3a1af1a` 20,880,148 B**
- Web `Lucerna-VOL4-ru-es-web.pdf`: `8c1bb27e…` 3,385,029 B →
  **`662998dc1e54f435f8fa08df31af846ddd8cf88990eeb3b97758dd1d5426ab05` 3,333,651 B**
  (< 7 MB; print/web text layers byte-identical, 38,581 chars each)
- Production `svglib.py` contains `_D5_READER` (verified); KIT §5 synced to
  the SHAs above.

## Defects found by D5 (2, both fixed; text unchanged, font size only; both cream-box titles)

1. P6 `ЗА И ПРОТИВ　PROS Y CONTRAS` over right +13.4px (creambox + boxtitle agree).
   Fix: `content56.py:136` size 24→22pt (advance 413.5→379.0 vs box inner width
   400.5, ~21.5px margin; 23pt would leave only 4.3px, so 22pt).
2. P7 `ОШИБКИ　CLÍNICA DE ERRORES` over right +3.6px (creambox + boxtitle agree).
   Fix: `content7.py:77` size 23→22pt (advance 403.6→386.1, ~14.4px margin).
   The other P7 word head `СЛОВО　LA PALABRA` (`content7.py:88`, 23pt) had no
   defect and was left alone.
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
  added CJK chars 0 (added Latin strings 145 = D5 run-splitting).
- `occlusion_audit.py` (fixed version) 0 flags; `boxtitle_check.py` 0 DEFECT
  (57 titles, 680 body lines); `d5_creambox_audit.py` PASS 0 defects
  (P8 lines 230→230, slack_footer 46.5→46.5px; ratios n=397, median 1.040,
  bold median 1.049).
- `spill_sweep.py` 0 SPILL; `pdf_edge_scan.py` 0 TOUCH, 0 NEAR.
- Print/web text layers byte-identical (38,581 chars).
- P8 Morozko SKIPPED by the build's own condition — as before,
  by design, not a defect.

## KIT

- `WEEKLY-KIT.md` §7 appended with the D5 record (including the render
  incident); §5 PDF SHAs/sizes updated to the new values above. History preserved.
- Independent re-proof is the coordinator's job; this report records
  self-check gates only.

## Cleanup

- `freeze/` build-copy deleted after verification. Baseline + logs + JSONs kept.
- No commit, no push, no `lint --write`. No other family touched.
