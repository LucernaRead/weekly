# D5 rebuild report — 2026-w46-es-ko (W46 es, reader ko)

- Mode: cjk; `_D5_READER = "ko"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 765,554 B / SHA256 `9b1070f08457bf3008b631ec83b13ef387cd6de2d2a6d86cbad990207e108329` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 341,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 1, curly total 1 (all Newsreader).
  Baseline print 8,514,627 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader ko --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 18/19

- G6: 0 flags. G12: 38/570/0/1/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 1 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 216 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 131.8px, D37 margin=282.8px).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:50` — P1 numbers f.box tsize added 21.5 (was default 23) (margin 4.2px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 1 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 216. G11 0 SPILL.
  G12 34/574/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 223 rows, slack 41.7px. G15a text-layer diff 0;
  text.md DIFF 132 lines, native verifier ADOPT (REWRAP 34, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=6225 md=9044. G16 0 defective.
- D18 gap 131.8px (baseline 193.0px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 margin margin=282.8px (baseline 280.0px).
  D39(4) P7 band bottom vs footer 2596: -83.9px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta -3;
  only whitespace reflow (6 \n<->space swaps) — no words lost.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-ko.pdf` 5,299,605 B
  SHA256 `c164f504706130c0e1d4c02d220f8b264697df62217ce8fc737080ea9aeedeb0`
- Web `2026-w46-es-ko.web.pdf` 680,397 B
  SHA256 `73b9e0ae129bbfc7fc36e94ba79260966fc650eb7f724bd205a8068f4c1b7500`
- text.md 48,248 B SHA256 `84325a4d67aba838e20aff4a0e27b2dc8ad82eaaa9f18cc04dbe1aa807001a07`
  (textexp output, `logs/2026-w46-es-ko/2026-w46-es-ko.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-ko/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-ko/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-ko/g*-run2.log`,
  `logs/2026-w46-es-ko/census-run2.json`, `logs/2026-w46-es-ko/freeze-diff-run2.json`.
