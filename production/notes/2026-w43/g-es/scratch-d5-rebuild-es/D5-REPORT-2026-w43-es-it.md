# D5 rebuild report — 2026-w43-es-it (Italian reader edition)

W43 es family, D5-only rebuild (SOP §1.1 font fix: explanation-layer Latin/Cyrillic moved from Noto Sans CJK to Newsreader / Noto Sans). Built 2026-11-13; **no commit, no push** (landing by the independent re-proof closer).
Work logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-it/` (`GATES-SUMMARY.txt` is the master table; `run1/` holds the pre-fix log archive).

## 1. Install

- Core landing (once for the whole family): `apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py` (`_D5_READER = "latin"` on landing; installed into scratch as the zh-cn reader, final value `"cjk"`).
- This edition: `apply_variant.py --svglib <edition>/svglib.py --target es --reader it --week 2026-w43` (after a clean `--check` dry-run). After install `_D5_READER = "latin"`. fix2 (U+201C/U+201D/U+2019 → serif) kept: this edition has 0 curly quotes.
- Routing unit test `test_d5_routing.py`: **FAILURES: 0**.
- Rebuild: `run.py` → `render.py` → `webpdf.py`; text.md re-exported for verification with `hidden_files/style-port-es/textexp_es.py` (SVG-route exporter); the deliverable is the shipped `.text.md` carried over unchanged (see §5).

## 2. Baseline (pre-repair production edition, proven clean before install)

- `run.py` RC=0, **TOTAL 150**, 0 warnings; `render.py` + `webpdf.py` output text-identical to the shipped edition (character-multiset diff 0); rebuilt SVGs 8/8 byte-identical to shipped.
- Pre-repair census `d5_census.py`: D5 Latin **494**, Cyrillic **0**, curly-in-CJK **0** (>0, install precondition met).
- Baseline measured (shipped recipe): print PDF `659a5794b07575bf5a68beaf04d88838d6173daa62b17df5eff466fd77f6d333` (5157454 B), render web PDF `502b2ff438a8dc81f0683f274bb0947a0346329955b56e8ae14adaf169d930a7` (3499571 B), issues web PDF `e1af268503dbd2d87029d9faa546bee984f8c9cd196c8179e70bfd87cf57dea4` (1137657 B). Older KIT values (older recipe) are stale; the values above govern.

## 3. Defects and fixes (run 1 → second-round fixes)

- Run-1 gates: head_check defects **4**; occlusion **1 TEXTX (P7)**; boxtitle/creambox defects **3 (P1 IN CIFRE +17.5; P1 IL NUMERO +3.7; P7 ERRORI TIPICI +26.7)**; P8 lines **210**, footer slack **56.6px**; verify **ADOPT (31 REWRAP)**.
- Second-round fixes (font sizes only, no text change; measured advances with the patched svglib `text_w`, sans bold; column width CW=422.5, box-title inner width 404.5, P7 p.text title inner width 400.5):
  1. `content12.py:128` P1 head `EL OTOÑO EMPIEZA DE VERDAD` 25→24 (439.1→421.5).
  2. `content34.py:23` P3 head `RECORDAR　RICORDARE INSIEME` 25→22 (467.5→411.4; 23pt still +7.6 over).
  3. `content7.py:16` P7 head `A2　DECIR LA HORA Y EL PRESENTE` 24→21 (471.1→412.2; also clears the P7 TEXTX collision — that head overlapped `B1` by 20.5×16.8px).
  4. `content7.py:48` P7 head `B2　CREO QUE… / NO CREO QUE…` 24→23 (428.8→411.0).
  5. `content12.py:50` P1 box `LA SEMANA EN CIFRAS　IN CIFRE` tsize 23→21 (421.8→385.0; 22pt margin only 1.1).
  6. `content12.py:93` P1 `EN ESTA EDICIÓN　IL NUMERO` p.text 24→23 (403.9→387.1).
  7. `content7.py:79` P7 `ERRORES TÍPICOS　ERRORI TIPICI` p.text 23→21 (427.5→390.3; 22pt still +8.3 over).
- P8: lines 210→210, footer slack 56.6px unchanged; p8 compare CLEAN (keydiff [137, 138]).

## 4. Gates (run 2, ALL-GREEN)

- run TOTAL 150, warnings 0; head_check PASS 0 defects; d5 census Latin 0 / Cyrillic 0 / curly-in-CJK 0; render RC=0; webpdf RC=0 (1060240 B <7MB); occlusion 0 (incl. selftest); p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8; freeze diff vs base added CJK chars TOTAL 1 (U+3000, run split); spill 0; boxtitle 0; edge 0/0; creambox PASS 0 defects (ratios n=401, median 1.040); text-layer print=web multiset diff 0; census_quotes 0 defective; family gates.py N/A. 
- Logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-it/GATES-SUMMARY.txt`.

## 5. New deliverables and KIT

- New print PDF `93435546576e4270e119f57dde820eea9892b9ebce87b54ffce8251e86c7fc78` (4548994 B); new render web PDF `579ecf54de6c9f8914f398068d4322f35e8e94c3f644fead95b78a5f939b4ca2` (3514713 B); issues web PDF (`tools/webpdf.py`) `17c097d15ca2e8cfccc3c8df60a739c54073e5476bbee93dbc43f6fceba025ff` (1060240 B) — to be swapped into `issues/2026-w43/2026-w43-es-it/2026-w43-es-it.pdf` by the closer with a pin update (shipped `aa1c9f0b1c487c5cd6f19067c220530ae1af064588b09deb739c8f880a606414`, 1101162 B). Print PDF shrank from font-subset changes (Latin moved out of the CJK font); text content unchanged (print=web text-layer multiset diff 0).
- text.md: D5 changes no text content; re-export after rebuild reflows line breaks (31 REWRAP), so the deliverable is the shipped `.text.md` carried over unchanged (BYTE-IDENTICAL); acceptance `verify_textexp_es.py --edition` verdict **ADOPT** (0 UNEXPECTED; exercise numbers 313/313 in sequence; all 8 pages token-identical).
- KIT: `production/2026-w43/2026-w43-es-it/WEEKLY-KIT.md` (deliverables rows updated to D5 values + trailing D5 record (§12)).
