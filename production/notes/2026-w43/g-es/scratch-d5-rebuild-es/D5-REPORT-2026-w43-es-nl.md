# D5 rebuild report — 2026-w43-es-nl (Dutch reader edition)

W43 es family, D5-only rebuild (SOP §1.1 font fix: explanation-layer Latin/Cyrillic moved from Noto Sans CJK to Newsreader / Noto Sans). Built 2026-11-13; **no commit, no push** (landing by the independent re-proof closer).
Work logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-nl/` (`GATES-SUMMARY.txt` is the master table; `run1/` holds the pre-fix log archive).

## 1. Install

- Core landing (once for the whole family): `apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py` (`_D5_READER = "latin"` on landing; installed into scratch as the zh-cn reader, final value `"cjk"`).
- This edition: `apply_variant.py --svglib <edition>/svglib.py --target es --reader nl --week 2026-w43` (after a clean `--check` dry-run). After install `_D5_READER = "latin"`. fix2 (U+201C/U+201D/U+2019 → serif) kept: this edition has 0 curly quotes.
- Routing unit test `test_d5_routing.py`: **FAILURES: 0**.
- Rebuild: `run.py` → `render.py` → `webpdf.py`; text.md re-exported for verification with `hidden_files/style-port-es/textexp_es.py` (SVG-route exporter); the deliverable is the shipped `.text.md` carried over unchanged (see §5).

## 2. Baseline (pre-repair production edition, proven clean before install)

- `run.py` RC=0, **TOTAL 150**, 0 warnings; `render.py` + `webpdf.py` output text-identical to the shipped edition (character-multiset diff 0); rebuilt SVGs 8/8 byte-identical to shipped.
- Pre-repair census `d5_census.py`: D5 Latin **494**, Cyrillic **0**, curly-in-CJK **0** (>0, install precondition met).
- Baseline measured (shipped recipe): print PDF `a751c5961c34eddab94fdd41982b9c62f3f48550d1195f243c08971cb0d5a68c` (5164153 B), render web PDF `6665bf7c423664a5e91048a7b737aed1e0692400f904f0f9d3a3d2fb4b8c0b6e` (3501232 B), issues web PDF `6ab5a9e267929f219f008bb14825ce0abebb5a2093e77b112108700819ae6bce` (1145593 B). Older KIT values (older recipe) are stale; the values above govern.

## 3. Defects and fixes (run 1 → second-round fixes)

- Run-1 gates: head_check defects **4**; occlusion **1 TEXTX (P7)**; boxtitle/creambox defects **3 (P1 In cijfers +6.5; P1 In dit nummer +21.7; P2 Spreuk +40.7)**; P8 lines **217**, footer slack **56.6px**; verify **HOLD — masthead tagline×date collision (see fix 1–2)**.
- Second-round fixes (font sizes only, no text change; measured advances with the patched svglib `text_w`, sans bold; column width CW=422.5, box-title inner width 404.5, P7 p.text title inner width 400.5):
  1. `content12.py:15` masthead tagline `CADA SEMANA EN ESPAÑOL　ELKE WEEK　HET SPAANS DAT DE SPANJAARDEN LEZEN` 17→16 — D5 widened Latin (Newsreader wider than CJK SC at 17pt + letter-spacing 1.7), so the centered tagline's right end moved right and the right-aligned date's left end moved left; their gap collapsed 81.9px → −4.1px and the glyphs touched (`LEZEN` + `SEMANA` rendered as `LEZENSEMANA`, visually confirmed on the rendered P1). 16pt restores a +41.3px gap (date x=1435.0 as rendered).
  2. `content12.py:16` masthead date `SEMANA DEL 19 AL 25 DE OCTUBRE DE 2026` 17→16 (paired with the tagline; same collision).
  3. `content12.py:125` P1 head `EL OTOÑO EMPIEZA DE VERDAD` 25→24 (439.1→421.5).
  4. `content34.py:23` P3 head `RECORDAR JUNTOS　Herdenken` 25→24 (429.3→412.1).
  5. `content7.py:16` P7 head `A2　DECIR LA HORA Y EL PRESENTE` 24→21 (471.1→412.2; also clears the P7 TEXTX collision — that head overlapped `B1` by 20.5×16.8px).
  6. `content7.py:48` P7 head `B2　CREO QUE… / NO CREO QUE…` 24→23 (428.8→411.0).
  7. `content12.py:47` P1 box `LA SEMANA EN CIFRAS　In cijfers` tsize 23→22 (411.3→393.4).
  8. `content12.py:90` P1 `EN ESTA EDICIÓN　In dit nummer` p.text 24→22 (422.6→387.4; 23pt still +4.5 over).
  9. `content12.py:176` P2 box `LA FRASE PARA RECORDAR　Spreuk` tsize 23→20 (445.0→386.9; 21pt still +1.8 over).
- P8: lines 217→217, footer slack 56.6px unchanged; p8 compare CLEAN (keydiff [137, 138]).

## 4. Gates (run 2, ALL-GREEN)

- run TOTAL 150, warnings 0; head_check PASS 0 defects; d5 census Latin 0 / Cyrillic 0 / curly-in-CJK 0; render RC=0; webpdf RC=0 (1065755 B <7MB); occlusion 0 (incl. selftest); p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8; freeze diff vs base added CJK chars TOTAL 1 (U+3000, run split); spill 0; boxtitle 0; edge 0/0; creambox PASS 0 defects (ratios n=402, median 1.040); text-layer print=web multiset diff 0; census_quotes 0 defective; family gates.py N/A. Run 1 had returned HOLD on the masthead merge (`LEZEN`+`SEMANA` → `LEZENSEMANA` in the re-export); the masthead 17→16pt fix resolves it — run 2 verifies ADOPT.
- Logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-nl/GATES-SUMMARY.txt`.

## 5. New deliverables and KIT

- New print PDF `f3d646bb9bf3d793f2d0d3ef13ca14fe133b3ab280cfa61ef21a5907dd554d91` (4554520 B); new render web PDF `effe9f9ca02abde9a25795631604b27ff392e293cedb0e5ffe4b8836706d7c0f` (3500714 B); issues web PDF (`tools/webpdf.py`) `f9d7d20d036af3c3095c533ddfce898bb25be5fbbaa690cef573ce691d547aab` (1065755 B) — to be swapped into `issues/2026-w43/2026-w43-es-nl/2026-w43-es-nl.pdf` by the closer with a pin update (shipped `4a3aea12272eda5aea478ca7a0e04d03743371dd2ab50e93c3a2d4b1f4ae963a`, 1109277 B). Print PDF shrank from font-subset changes (Latin moved out of the CJK font); text content unchanged (print=web text-layer multiset diff 0).
- text.md: D5 changes no text content; re-export after rebuild reflows line breaks (25 REWRAP), so the deliverable is the shipped `.text.md` carried over unchanged (BYTE-IDENTICAL); acceptance `verify_textexp_es.py --edition` verdict **ADOPT** (0 UNEXPECTED; exercise numbers 313/313 in sequence; all 8 pages token-identical).
- KIT: `production/2026-w43/2026-w43-es-nl/WEEKLY-KIT.md` (deliverables rows updated to D5 values + trailing D5 record (§14)).
