# D5 rebuild report — 2026-w43-es-fr (French reader edition)

W43 es family, D5-only rebuild (SOP §1.1 font fix: explanation-layer Latin/Cyrillic moved from Noto Sans CJK to Newsreader / Noto Sans). Built 2026-11-13; **no commit, no push** (landing by the independent re-proof closer).
Work logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-fr/` (`GATES-SUMMARY.txt` is the master table; `run1/` holds the pre-fix log archive).

## 1. Install

- Core landing (once for the whole family): `apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py` (`_D5_READER = "latin"` on landing; installed into scratch as the zh-cn reader, final value `"cjk"`).
- This edition: `apply_variant.py --svglib <edition>/svglib.py --target es --reader fr --week 2026-w43` (after a clean `--check` dry-run). After install `_D5_READER = "latin"`. fix2 (U+201C/U+201D/U+2019 → serif) kept: this edition has 0 curly quotes.
- Routing unit test `test_d5_routing.py`: **FAILURES: 0**.
- Rebuild: `run.py` → `render.py` → `webpdf.py`; text.md re-exported for verification with `hidden_files/style-port-es/textexp_es.py` (SVG-route exporter); the deliverable is the shipped `.text.md` carried over unchanged (see §5).

## 2. Baseline (pre-repair production edition, proven clean before install)

- `run.py` RC=0, **TOTAL 150**, 0 warnings; `render.py` + `webpdf.py` output text-identical to the shipped edition (character-multiset diff 0); rebuilt SVGs 8/8 byte-identical to shipped.
- Pre-repair census `d5_census.py`: D5 Latin **491**, Cyrillic **0**, curly-in-CJK **0** (>0, install precondition met).
- Baseline measured (shipped recipe): print PDF `ffb4f0ee4cd0a58f18976b86dc060f228f7df4b255f883bdac1f427f1f6dabf1` (5159752 B), render web PDF `4bc9aa956b3770aa1242c12eb5d33e59733a47a97264b05ee97f43da8ae1cad2` (3520308 B), issues web PDF `450af19c4157cd41e47bd8dbbd64a91718e1338d4c857160ca83079c7f6b0440` (1141107 B). Older KIT values (older recipe) are stale; the values above govern.

## 3. Defects and fixes (run 1 → second-round fixes)

- Run-1 gates: head_check defects **4**; occlusion **2 TEXTX (P1 EN CHIFFRES 5.0×7.7; P7)**; boxtitle/creambox defects **3 (P1 EN CHIFFRES +33.3; P1 SOMMAIRE +2.7; P7 MOT DE LA SEMAINE +46.5)**; P8 lines **199**, footer slack **57.4px**; verify **ADOPT (37 REWRAP)**.
- Second-round fixes (font sizes only, no text change; measured advances with the patched svglib `text_w`, sans bold; column width CW=422.5, box-title inner width 404.5, P7 p.text title inner width 400.5):
  1. `content12.py:125` P1 head `EL OTOÑO EMPIEZA DE VERDAD` 25→24 (439.1→421.5).
  2. `content34.py:23` P3 head `RECORDAR JUNTOS　MÉMOIRE` 25→24 (432.2→414.8).
  3. `content7.py:16` P7 head `A2　DECIR LA HORA Y EL PRESENTE` 24→21 (471.1→412.2; also clears the P7 TEXTX collision — that head overlapped `B1` by 20.5×16.8px).
  4. `content7.py:48` P7 head `B2　CREO QUE… / NO CREO QUE…` 24→23 (428.8→411.0).
  5. `content12.py:47` P1 box `LA SEMANA EN CIFRAS　EN CHIFFRES` tsize 21→19 (437.5→395.8; was already 21 pre-D5; 20pt still +12.1 over).
  6. `content12.py:90` P1 `EN ESTA EDICIÓN　SOMMAIRE` p.text 24→23 (403.4→386.7).
  7. `content7.py:90` P7 `LA PALABRA　MOT DE LA SEMAINE` p.text 23→20 (446.4→388.1; 21pt still +7.1 over).
- P8: lines 199→199, footer slack 57.4px unchanged; p8 compare CLEAN (keydiff [137, 138]).

## 4. Gates (run 2, ALL-GREEN)

- run TOTAL 150, warnings 0; head_check PASS 0 defects; d5 census Latin 0 / Cyrillic 0 / curly-in-CJK 0; render RC=0; webpdf RC=0 (1062545 B <7MB); occlusion 0 (incl. selftest); p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8; freeze diff vs base added CJK chars TOTAL 1 (U+3000, run split); spill 0; boxtitle 0; edge 0/0; creambox PASS 0 defects (ratios n=394, median 1.040); text-layer print=web multiset diff 0; census_quotes 0 defective; family gates.py N/A. 
- Logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-fr/GATES-SUMMARY.txt`.

## 5. New deliverables and KIT

- New print PDF `e627768c9a47be6d0d33696374eea3226d82ea81a8ca5fa65322186833d85b97` (4551313 B); new render web PDF `835d138e2837acbb1c4dd91e586f7c156c59dd40dae1beecfa7b987f436d579d` (3528082 B); issues web PDF (`tools/webpdf.py`) `9dc1d831cbbcf8a88b9d00367722e0571559cb2058bbf8f8dec907310f136e74` (1062545 B) — to be swapped into `issues/2026-w43/2026-w43-es-fr/2026-w43-es-fr.pdf` by the closer with a pin update (shipped `7ce00e4302bcc776650d42c59f03edf7b00e3bca3af030eed92179bd4ca0e28f`, 1104577 B). Print PDF shrank from font-subset changes (Latin moved out of the CJK font); text content unchanged (print=web text-layer multiset diff 0).
- text.md: D5 changes no text content; re-export after rebuild reflows line breaks (37 REWRAP), so the deliverable is the shipped `.text.md` carried over unchanged (BYTE-IDENTICAL); acceptance `verify_textexp_es.py --edition` verdict **ADOPT** (0 UNEXPECTED; exercise numbers 313/313 in sequence; all 8 pages token-identical).
- KIT: `production/2026-w43/2026-w43-es-fr/WEEKLY-KIT.md` (deliverables rows updated to D5 values + trailing D5 record (§10)).
