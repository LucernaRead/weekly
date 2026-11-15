# D5 rebuild report — 2026-w46-es-fr (W46 es, reader fr)

- Mode: latin; `_D5_READER = "fr"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 450,384 B / SHA256 `636ac740422a3529983c57d79dd4b47aab8048236e8268887ecf16bdf401f879` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 504,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader).
  Baseline print 4,064,165 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader fr --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 16/19

- G6: TEXTX 225.0x20.8px. G12: 24/274/3/1/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 4 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 259 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 18.5px, D37 N/A).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:26` — band headline 46 -> 35 (gap +11.7px)
- `content12.py:45` — P1 numbers tsize 20 -> 19 (margin 9.1px)
- `content12.py:92` — P1 sommaire 24 -> 23.5 (margin 5.7px)
- `content12.py:185` — P2 calendar f.box tsize added 21 (was default 23) (margin 9.2px)
- `content7.py:90` — P7 word 23 -> 20.5 (margin 2.1px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 0 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 259. G11 0 SPILL.
  G12 20/278/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 236 rows, slack 45.8px. G15a text-layer diff 0;
  text.md DIFF 122 lines, native verifier ADOPT (REWRAP 33, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5742 md=7212. G16 0 defective.
- D18 gap 18.5px (baseline 103.2px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: -57.4px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta +0;
  only whitespace reflow (19 \n<->space swaps) — no words lost.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-fr.pdf` 3,480,500 B
  SHA256 `7145519505303d50e4bf06052496cb02915e99f259f03575b6b7c39e1c6b1441`
- Web `2026-w46-es-fr.web.pdf` 410,179 B
  SHA256 `f33bbae5cae4833bb2734620114c5f7cdb94980117dcc99d2879e8e4f94b1955`
- text.md 47,366 B SHA256 `9be9217d9f31ae2df15a7739398a83ed2fe4bb1ffa5f49647aa2544c437fb402`
  (textexp output, `logs/2026-w46-es-fr/2026-w46-es-fr.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-fr/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-fr/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-fr/g*-run2.log`,
  `logs/2026-w46-es-fr/census-run2.json`, `logs/2026-w46-es-fr/freeze-diff-run2.json`.
