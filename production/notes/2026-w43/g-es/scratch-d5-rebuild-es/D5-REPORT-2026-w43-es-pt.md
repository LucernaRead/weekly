# D5 rebuild report — 2026-w43-es-pt (Portuguese reader edition)

W43 es family, D5-only rebuild (SOP §1.1 font fix: explanation-layer Latin/Cyrillic moved from Noto Sans CJK to Newsreader / Noto Sans). Built 2026-11-13; **no commit, no push** (landing by the independent re-proof closer).
Work logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-pt/` (`GATES-SUMMARY.txt` is the master table; `run1/` holds the pre-fix log archive).

## 1. Install

- Core landing (once for the whole family): `apply_variant.py --patch-core es --week 2026-w43 --i-understand-this-writes-production` → `production/2026-w43/core-es/svglib.py` (`_D5_READER = "latin"` on landing; installed into scratch as the zh-cn reader, final value `"cjk"`).
- This edition: `apply_variant.py --svglib <edition>/svglib.py --target es --reader pt --week 2026-w43` (after a clean `--check` dry-run). After install `_D5_READER = "latin"`. fix2 (U+201C/U+201D/U+2019 → serif) kept: this edition has 0 curly quotes.
- Routing unit test `test_d5_routing.py`: **FAILURES: 0**.
- Rebuild: `run.py` → `render.py` → `webpdf.py`; text.md re-exported for verification with `hidden_files/style-port-es/textexp_es.py` (SVG-route exporter); the deliverable is the shipped `.text.md` carried over unchanged (see §5).

## 2. Baseline (pre-repair production edition, proven clean before install)

- `run.py` RC=0, **TOTAL 150**, 0 warnings; `render.py` + `webpdf.py` output text-identical to the shipped edition (character-multiset diff 0); rebuilt SVGs 8/8 byte-identical to shipped.
- Pre-repair census `d5_census.py`: D5 Latin **488**, Cyrillic **0**, curly-in-CJK **0** (>0, install precondition met).
- Baseline measured (shipped recipe): print PDF `769c6cb4e2efcd5c57992bd5146b9a2537a7ab2037be2c3de2b9b8f8d50d9a25` (5163376 B), render web PDF `c27dea0e89da69c5e427bc17908da12a5e8506840fe8fda5de6446c4e20c83d7` (3515085 B), issues web PDF `aa900030469181db06661b8a9652b81a4f4405a2e0582cbcc906358e11bbe04f` (1144654 B). Older KIT values (older recipe) are stale; the values above govern.

## 3. Defects and fixes (run 1 → second-round fixes)

- Run-1 gates: head_check defects **3**; occlusion **1 TEXTX (P7)**; boxtitle/creambox defects **1 (P2 Para guardar +5.4)**; P8 lines **197**, footer slack **56.4px**; verify **HOLD — masthead tagline×date collision (see fix 1–2)**.
- Second-round fixes (font sizes only, no text change; measured advances with the patched svglib `text_w`, sans bold; column width CW=422.5, box-title inner width 404.5, P7 p.text title inner width 400.5):
  1. `content12.py:15` masthead tagline `SEMANAL EN ESPAÑOL　UM NÚMERO POR SEMANA　O ESPANHOL QUE A ESPANHA LÊ` 17→16 — D5 widened Latin (Newsreader wider than CJK SC at 17pt + letter-spacing 1.7), so the centered tagline's right end moved right and the right-aligned date's left end moved left; their gap collapsed 80.4px → −4.4px and the glyphs touched (`LÊ` + `SEMANA` rendered as `LÊSEMANA`). 16pt restores a +41.0px gap.
  2. `content12.py:16` masthead date `SEMANA DEL 19 AL 25 DE OCTUBRE DE 2026` 17→16 (paired with the tagline; same collision).
  3. `content12.py:125` P1 head `EL OTOÑO EMPIEZA DE VERDAD` 25→24 (439.1→421.5).
  4. `content7.py:16` P7 head `A2　DECIR LA HORA Y EL PRESENTE` 24→21 (471.1→412.2; also clears the P7 TEXTX collision — that head overlapped `B1` by 20.5×16.8px).
  5. `content7.py:48` P7 head `B2　CREO QUE… / NO CREO QUE…` 24→23 (428.8→411.0).
  6. `content12.py:176` P2 box `FRASE PARA RECORDAR　Para guardar` tsize 20→19 (409.2→388.8; was already 20 pre-D5; note: no `LA` prefix in this edition's title).
  - P3 head `RECORDAR JUNTOS　Lembrar` fits at 25pt, no fix needed.
- P8: lines 197→197, footer slack 56.4px unchanged; p8 compare CLEAN (keydiff [137, 138]).

## 4. Gates (run 2, ALL-GREEN)

- run TOTAL 150, warnings 0; head_check PASS 0 defects; d5 census Latin 0 / Cyrillic 0 / curly-in-CJK 0; render RC=0; webpdf RC=0 (1065509 B <7MB); occlusion 0 (incl. selftest); p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8; freeze diff vs base added CJK chars TOTAL 1 (U+3000, run split); spill 0; boxtitle 0; edge 0/0; creambox PASS 0 defects (ratios n=395, median 1.040); text-layer print=web multiset diff 0; census_quotes 0 defective; family gates.py N/A. Run 1 had returned HOLD on the masthead merge (`LÊ`+`SEMANA` → `LÊSEMANA` in the re-export); the masthead 17→16pt fix resolves it — run 2 verifies ADOPT.
- Logs: `hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-pt/GATES-SUMMARY.txt`.

## 5. New deliverables and KIT

- New print PDF `1f3225f9527af54b52e53383fcaebfdf0d64a82119c70e84d72925bba27d102b` (4554264 B); new render web PDF `68411a88e07a1f1c455f1beea51c4761245e6357b0ad001ea16c44b6dd415711` (3522457 B); issues web PDF (`tools/webpdf.py`) `0de196c49f8f78000925496f6618de10ed37c2e7fd579f6d5b0fc3f64e3d0e4c` (1065509 B) — to be swapped into `issues/2026-w43/2026-w43-es-pt/2026-w43-es-pt.pdf` by the closer with a pin update (shipped `806cfdecd075a6114dd2309776cda812fb18153c7d6b572173a3091054cb8a0b`, 1108388 B). Print PDF shrank from font-subset changes (Latin moved out of the CJK font); text content unchanged (print=web text-layer multiset diff 0).
- text.md: D5 changes no text content; re-export after rebuild reflows line breaks (29 REWRAP), so the deliverable is the shipped `.text.md` carried over unchanged (BYTE-IDENTICAL); acceptance `verify_textexp_es.py --edition` verdict **ADOPT** (0 UNEXPECTED; exercise numbers 313/313 in sequence; all 8 pages token-identical).
- KIT: `production/2026-w43/2026-w43-es-pt/WEEKLY-KIT.md` (deliverables rows updated to D5 values + trailing D5 record (§13)).
