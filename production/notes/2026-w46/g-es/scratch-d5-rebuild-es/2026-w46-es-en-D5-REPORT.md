# D5 rebuild report — 2026-w46-es-en (W46 es, reader en)

- Mode: latin; `_D5_READER = "en"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 452,916 B / SHA256 `cc5278785570eccb7c71c8f65b2f9357dd61f64b25d83a266a0c41c181f472ca` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 499,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 2, curly total 3 (all Newsreader).
  Baseline print 4,054,021 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader en --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 18/19

- G6: 0 flags. G12: 30/262/0/2/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 2 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 264 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 124.7px, D37 N/A).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:49` — P1 numbers f.box tsize added 22 (was default 23) (margin 7.5px)
- `content56.py:28` — P5 plan f.box tsize added 21.5 (was default 23) (margin 7.0px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 3 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 264. G11 0 SPILL.
  G12 28/264/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 231 rows, slack 44.8px. G15a text-layer diff 0;
  text.md DIFF 142 lines, native verifier ADOPT (REWRAP 37, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5572 md=7181. G16 0 defective.
- D18 gap 124.7px (baseline 202.0px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: -25.9px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta +0;
  only whitespace reflow (7 \n<->space swaps) — no words lost.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-en.pdf` 3,480,826 B
  SHA256 `9dff62a83be83561f83aed7d4e8343391e3af8497e6e6295ca270e2a04f9d212`
- Web `2026-w46-es-en.web.pdf` 410,550 B
  SHA256 `2d4c70f9b20c4f0d56f0ece039db84c17464e670a2fe95b4b863b8babfee1cf6`
- text.md 45,999 B SHA256 `762a1ebfb734f44b0adedfda058ca7c4293eaedcce3a5b5c0d4767e8ae7c2587`
  (textexp output, `logs/2026-w46-es-en/2026-w46-es-en.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-en/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-en/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-en/g*-run2.log`,
  `logs/2026-w46-es-en/census-run2.json`, `logs/2026-w46-es-en/freeze-diff-run2.json`.
