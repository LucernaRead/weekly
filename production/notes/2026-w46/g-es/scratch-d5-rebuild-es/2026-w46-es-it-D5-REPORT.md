# D5 rebuild report — 2026-w46-es-it (W46 es, reader it)

- Mode: latin; `_D5_READER = "it"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 446,706 B / SHA256 `c3bfe0351698f65bc53e3437f644f535ac16d76a78f6f661fa3ef80eeab84e40` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 499,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader).
  Baseline print 4,061,333 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader it --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 16/19

- G6: TEXTX 185.5x25.5px. G12: 26/270/2/1/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 3 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 266 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 7.9px, D37 margin=106.4px).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:27` — band headline 46 -> 37 (gap +8.2px)
- `content12.py:50` — P1 numbers f.box tsize added 21.5 (was default 23) (margin 10.0px)
- `content12.py:93` — P1 sommaire 24 -> 23.5 (margin 4.7px)
- `content12.py:186` — P2 calendar f.box tsize added 21.5 (was default 23) (margin 4.5px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 0 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 266. G11 0 SPILL.
  G12 22/274/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 231 rows, slack 58.5px. G15a text-layer diff 0;
  text.md DIFF 128 lines, native verifier ADOPT (REWRAP 34, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5569 md=7139. G16 0 defective.
- D18 gap 7.9px (baseline 96.5px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 margin margin=106.4px (baseline 147.0px).
  D39(4) P7 band bottom vs footer 2596: -25.9px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta +0;
  only whitespace reflow (10 \n<->space swaps) — no words lost.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-it.pdf` 3,477,440 B
  SHA256 `543439c04489e9b6d01fb64bd61dd9da4ed6f23bdc243d93a143bb0cc17142a2`
- Web `2026-w46-es-it.web.pdf` 407,145 B
  SHA256 `25f1f7b2b58f85b955abe44745422bfe090840b0ab1395b57d0d55d9283729dd`
- text.md 46,715 B SHA256 `11c2fc4dcfb1ae65cf85bdcb2b454836e00f569c057695868a258567feceb0c9`
  (textexp output, `logs/2026-w46-es-it/2026-w46-es-it.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-it/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-it/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-it/g*-run2.log`,
  `logs/2026-w46-es-it/census-run2.json`, `logs/2026-w46-es-it/freeze-diff-run2.json`.
