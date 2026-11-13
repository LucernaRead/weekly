# GATE-LOG — 2026-W47 de-pt toolbox fix1 (rebuild 4, 2026-11-11)

Build driver: `tools/venv/bin/python build_edition.py pt` (from `scratch-fanout-de/`;
runs run.py → render.py → webpdf → verify → occlusion → p8 → freeze → pdftotext →
chips → export; does NOT re-run transform, so the `content7.py` fix survives).
Driver stdout: **ALL GATES PASS 2026-w47-de-pt**. Per-gate detail below.
Extra gates re-run afterwards by `run-gates.sh` in this scratch dir (log `gates-fix1.log`).

Tool versions at build time: `tools/webpdf.py` UNMODIFIED in the working tree
(mtime 2026-11-11 09:10, no `M` in git status — unlike the es fix1 build, which
carried uncommitted webpdf changes). `tools/freeze.py` (mtime 2026-11-10 22:59),
`tools/occlusion_audit.py` (2026-11-11 05:01), `tools/p8.py` (2026-11-10 21:37)
show `M` in git status — other agents' in-flight changes, used as-is, untouched
by this fix. `tools/venv/bin/python` (PIL 13.0.0).

## Driver gates (build.log / scratch-fanout-de/pt/)

- run.py exit 0; **zero FLOW OVERFLOW / HEAD TOO WIDE**; TOTAL 150.
  Flow ends identical to KIT §6 except P7 image: P7-A2 1278 / B1 1342 / B2 1306;
  P7 image ends 1541.83; P7 col3 ends **1547.5** (unchanged); P8 battery 1409.445;
  P8 keys 2457 (bottom 2560, spare 103px).
- render.py exit 0; print PDF exists.
- verify.py: TOTAL 150; numbering continuous 1–150; SVGs byte-identical after
  verify run; SOP 1.1 style audit True; verbatim OK; P8 answers floor True;
  all 17 forbidden terms absent; MUSTER 84 words; chart 44+33+23=100; dates True.
- occlusion_audit.py (real run): **0 flags** (selftest OK: all 6 planted classes
  fired, clean controls silent).
- p8.py extract 150/150; compare vs core: `status: CLEAN missing=[] extra_count=0
  keydiff=[137, 138, 139, 150]` — the 4 expected items only.
- freeze.py diff: exit 0; TOTAL added CJK 7, all U+3000 (1 per page P2–P8, 0 on P1).
- Print/web text layer: `pdftotext` default — print 50,684B / web 50,684B,
  **word multiset identical**; `-raw` — both 49,500B, normalised text
  **exactly identical**. Web PDF has a real text layer.
- Level chips per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35},
  **TOTAL 141**; P8 by level A2 22 / B1 13 / B2 0.
- Export: text.md 49,812 bytes, **sha e2ee96ebd9dca775598431f87c511f53ed04dec25
  47896586d46a2c57a800928 — byte-identical to pre-fix** (zero content change).
- P8 min span size (PyMuPDF): **9.94pt** (≥ 9.75pt floor).

## Extra gates (run-gates.sh, this scratch dir)

- freeze_direct (fresh re-run, `freeze-direct.json` + `freeze-direct.log`):
  source PASS (520 removed / 528 added, 0 unaccounted); rendered **8/8** —
  P1 147 sha 083e2a2a, P2 163 sha 689045ad, P3 195 sha **fc88f676** (post-Q34
  value; the `scratch-fanout-de/pt/freeze-direct.json` on disk was stale from
  rebuild 2, P3 093cf378 — the driver does not run freeze_direct), P4 166
  sha df1bebf7, P5 173 sha 86fa4421, P6 175 sha 2bbe05f9, P7 150 sha b7aa0771
  (unchanged — frozen German strings untouched), P8 186 sha 57e118e7.
- keycheck 150 (`keycheck-150.json` + `keycheck.log`): **149/150 exact**; the
  single non-exact item is Q150 (open writing task, extractor truncates the REG
  key — expected, same as rebuild 3). (Needed the driver's `p8extract.json`
  copied into this scratch dir; keycheck.py reads it from OUT.)
- boxtitle (`boxtitle.log`): **7/7 fit** — DER WERKZEUGKASTEN Material 386.1/400.5.
- measure (`measure.log`): **24/24 PASS, 0 FAIL**.
- pdftotext print vs web (own outputs `print.txt`/`web.txt`/`print-raw.txt`/
  `web-raw.txt`): default 50,684B each, word multiset identical; raw normalised
  identical, 49,500B each.
- Quotes over the 8 SVGs: German „ (U+201E) 33 = “ (U+201C) 33, **paired**;
  U+201D 0, U+2019 0, straight U+0027 0. (The first scan miscounted „ as 201C;
  corrected count above.)
- Q34 stem: new stem "Am Montag öffnet in Köln der erste ___." 1× / old stem 0×
  in source, text.md, P3 SVG, print text layer, web text layer. **No regression.**
- D1 (`pess.`) five-fold re-verification: `pess.` 13 / `pers.` 0 in content8.py,
  text.md, P8 SVG, print P8 text layer, web P8 text layer. (The 5th fold —
  200 dpi visual — is proof2's, on the untouched P8; P8 freeze sha unchanged.)
- d2scan (`d2scan.json` + `d2scan.log`): 60 abutting pairs checked,
  **0 web gaps >0.5pt**.
- creambox full edition (`creambox-after.log`): toolbox **+20.0** (y=310,
  bottom=813.0, last baseline 793.0); LESERBRIEFE +10.4 (unchanged); NOCH EIN
  WORT +42.9, ends 1547.5 (unchanged). All other creambox rows positive except
  the matcher's known false positives (see below).
- Print vs web P7 rail pixel diff (150 dpi, toolbox+LESERBRIEFE+NOCH EIN WORT
  region): **0 pixels differ >60 gray** of 1,312,085 — pixel-identical rail.

## creambox negative rows — false positives (pre-existing, unchanged)

- P7 −35.0 ×3 (BEISPIELE boxes vs exercise numbers below them in the same
  column, inside the matcher's +45 window): identical values pre- and post-fix;
  documented as false positives in de-es fix1 §1, same pattern in all editions.
- P1 −24.0 ('DAS WORT DER WOCHE' at y=1676, x=1439.5): the next col-3 section
  head 24px BELOW the 'IN DIESER AUSGABE' box (bottom 1652); the box's real
  last content is 'Übungen & Lösungen' at 1636 (clearance +16.0). Not box
  content; no overlap.
- P2 −44.9 ('Die Daten der Woche' at y=1594): the next col-3 head 44.9px BELOW
  the 'DIE STILLE WOCHE' box (bottom 1549.1); the box's real last content is
  'Gedenken an die Verstorbenen.' at 1529.6 (clearance +19.5). Not box content.
- Both rows concern pages whose sources were NOT touched (only content7.py
  changed, which emits only p7); freeze_direct P1/P2 shas are identical to
  proof2's, and occlusion is 0 flags. Not defects, not regressions.

## Visual check (print PDF renders in this scratch dir)

- `p7-print-100dpi.png` (full P7, 100 dpi): toolbox starts slightly above the
  A2/B1/B2 heads, clear gap to the intro lines; last entry fully inside the box
  with cream below it; 16px gap to LESERBRIEFE; NOCH EIN WORT ends at the
  Sätze rule as before; no overlaps or collisions anywhere on the page.
- `p7-toolbox-zoom.png` (toolbox region, 300 dpi): all 6 entries legible,
  last line "Es ist fraglich, ob ... = ainda duvidoso" fully inside the cream
  with clear cream below the 'g' descender; box bottom edge clean.
