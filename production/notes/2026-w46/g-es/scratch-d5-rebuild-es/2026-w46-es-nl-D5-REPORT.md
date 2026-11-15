# D5 rebuild report — 2026-w46-es-nl (W46 es, reader nl)

- Mode: latin; `_D5_READER = "nl"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 454,982 B / SHA256 `f9a10f0f5fc9ab8b518e97b5e0b82591e42d7f31802576104e631710f4d4eeb3` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 503,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader).
  Baseline print 4,068,620 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader nl --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 16/19

- G6: TEXTX 175.0x20.8px. G12: 24/276/1/1/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 2 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 258 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 72.4px, D37 N/A).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:26` — band headline 46 -> 37 (gap +18.7px)
- `content12.py:92` — P1 sommaire 24 -> 22.5 (margin 4.7px)
- `content56.py:22` — P5 plan tsize 20 -> 19 (margin 7.8px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 0 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 258. G11 0 SPILL.
  G12 24/276/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 239 rows, slack 46.8px. G15a text-layer diff 0;
  text.md DIFF 108 lines, native verifier ADOPT (REWRAP 28, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5596 md=7196. G16 0 defective.
- D18 gap 72.4px (baseline 153.1px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: -30.9px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta +0;
  only whitespace reflow (7 \n<->space swaps) — no words lost.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-nl.pdf` 3,482,208 B
  SHA256 `69855a88e5a360a87cfdb86061c66f712825eaa8758d5512f061eb90e0d4ab72`
- Web `2026-w46-es-nl.web.pdf` 411,903 B
  SHA256 `b2bae05871d1216f12c5d1ef4c53d0fbe5844e8dcc37346beda4cfdf4ea890a5`
- text.md 46,632 B SHA256 `d1068dc7b89c7066217201410a93ccc9cb5440eb0c8df503a239a6bbf7d575c5`
  (textexp output, `logs/2026-w46-es-nl/2026-w46-es-nl.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-nl/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-nl/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-nl/g*-run2.log`,
  `logs/2026-w46-es-nl/census-run2.json`, `logs/2026-w46-es-nl/freeze-diff-run2.json`.
