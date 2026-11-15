# D5 rebuild report — 2026-w46-es-zh-tw (W46 es, reader zh-tw)

- Mode: cjk; `_D5_READER = "zh-tw"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 1,193,051 B / SHA256 `7c36fd305210447a8c85c564fdfb41b4dd21904c05c4bb0dcb03cf073281a41e` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 339,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader).
  Baseline print 16,148,875 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader zh-tw --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 18/19

- G6: 0 flags. G12: 30/348/0/2/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 2 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 221 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 103.0px, D37 N/A).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:49` — P1 numbers f.box tsize added 21.5 (was default 23) (margin 5.3px)
- `content56.py:28` — P5 plan f.box tsize added 22 (was default 23) (margin 4.5px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 0 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 221. G11 0 SPILL.
  G12 28/350/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 200 rows, slack 57.4px. G15a text-layer diff 0;
  text.md DIFF 78 lines, native verifier ADOPT (REWRAP 21, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5918 md=7969. G16 0 defective.
- D18 gap 103.0px (baseline 165.1px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: +4.6px (pre-existing).
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta -5;
  only whitespace reflow (7 \n<->space swaps) — no words lost.
- D39(4): P7 band bottom 2600.6 vs footer 2596 (+4.6px crossing) is PRE-EXISTING — baseline identical (+4.6px); accepted per D39(4).

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-zh-tw.pdf` 4,935,582 B
  SHA256 `bbddea054c40fabeb16a98fc4954cabb1f20206c6fc9b4823639b0b5de225775`
- Web `2026-w46-es-zh-tw.web.pdf` 850,025 B
  SHA256 `49d5ca8c851cc44bbfd96d0fb716fbd5fedb272a41f30d7b8b3b0e0d0623a2ec`
- text.md 44,689 B SHA256 `08ddaf09ccda73c80be05db0e1327b8847cd13841bf63c7025f87d929577597e`
  (textexp output, `logs/2026-w46-es-zh-tw/2026-w46-es-zh-tw.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-zh-tw/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-zh-tw/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-zh-tw/g*-run2.log`,
  `logs/2026-w46-es-zh-tw/census-run2.json`, `logs/2026-w46-es-zh-tw/freeze-diff-run2.json`.
