# D5 rebuild report — 2026-w46-es-de (W46 es, reader de)

- Mode: latin; `_D5_READER = "de"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 458,350 B / SHA256 `178fbaf9171057f45f11ddaa7f1d6fd40d44d1a627609118503e548e1f1ae693` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 502,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 2, curly total 2 (all Newsreader).
  Baseline print 4,069,616 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader de --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 16/19

- G6: TEXTX 103.8x25.0px. G12: 26/275/2/2/1 (titles/body/DEFECT/OBSERVE/marginal). G14: 4 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 249 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 21.1px, D37 margin=60.3px).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:27` — band headline 46 -> 40 (gap +25.4px)
- `content12.py:50` — P1 numbers f.box tsize added 22 (was default 23) (margin 4.7px)
- `content56.py:22` — P5 plan tsize 20 -> 19.5 (margin 8.1px)
- `content7.py:79` — P7 errors 20 -> 18.5 (margin 11.3px)
- `content7.py:90` — P7 word 23 -> 21.5 (margin 7.9px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 2 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 249. G11 0 SPILL.
  G12 24/277/0/0/1 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 239 rows, slack 43.7px. G15a text-layer diff 0;
  text.md DIFF 76 lines, native verifier ADOPT (REWRAP 20, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5703 md=7064. G16 0 defective.
- D18 gap 21.1px (baseline 105.0px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 margin margin=60.3px (baseline 104.6px).
  D39(4) P7 band bottom vs footer 2596: -25.9px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta +0;
  only whitespace reflow (16 \n<->space swaps) — no words lost.
- G12 marginal (run2): P1 `KURZNACHRICHTEN` +0.7px, within the 1.0px tolerance; D5-introduced (baseline boxtitle: 0 marginal) but below the 2.0px defect threshold, left as is.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-de.pdf` 3,484,405 B
  SHA256 `b69ef08674d8f8c42b8d73ab8bfc4037025c52d023f6da6c92b7d2321ea5113c`
- Web `2026-w46-es-de.web.pdf` 414,135 B
  SHA256 `2ffab127a3b85cbd4ca68e64f30a96901514a98678efff01649a7e1f517d42ec`
- text.md 46,929 B SHA256 `3887e34ee0aadc057daf5f9273159cfb10ace8c808a9e5a64c0347d568647b20`
  (textexp output, `logs/2026-w46-es-de/2026-w46-es-de.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-de/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-de/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-de/g*-run2.log`,
  `logs/2026-w46-es-de/census-run2.json`, `logs/2026-w46-es-de/freeze-diff-run2.json`.
