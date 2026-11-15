# D5 rebuild report — 2026-w46-es-ja (W46 es, reader ja)

- Mode: cjk; `_D5_READER = "ja"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 1,080,987 B / SHA256 `88fe829d22347fd0a35d21ce319d662496665da935f3946b29009dfa5a9b81f1` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 342,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader).
  Baseline print 16,572,923 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader ja --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 17/19

- G6: 0 flags. G12: 28/370/1/1/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 2 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 220 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 48.5px, D37 N/A).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:49` — P1 numbers f.box tsize added 21.5 (was default 23) (margin 5.3px)
- `content7.py:79` — P7 errors 23 -> 22 (margin 9.1px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 0 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 220. G11 0 SPILL.
  G12 26/372/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 228 rows, slack 55.7px. G15a text-layer diff 0;
  text.md DIFF 106 lines, native verifier ADOPT (REWRAP 28, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=6468 md=9008. G16 0 defective.
- D18 gap 48.5px (baseline 110.7px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: -24.4px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta +1;
  only whitespace reflow (7 \n<->space swaps) — no words lost.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-ja.pdf` 8,654,706 B
  SHA256 `f70d73fa1599b270cb8e48311887cc8f97f2bfb0a17d20e7807f42012f96ee3e`
- Web `2026-w46-es-ja.web.pdf` 883,760 B
  SHA256 `9b0977949f98e5969c36f6e42828e9a94f30d7b99a688eeb1affd817035f5962`
- text.md 47,835 B SHA256 `a17196282c620808dbbe1f9c32a417b741e7008568246f143238ac54263ec3f1`
  (textexp output, `logs/2026-w46-es-ja/2026-w46-es-ja.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-ja/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-ja/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-ja/g*-run2.log`,
  `logs/2026-w46-es-ja/census-run2.json`, `logs/2026-w46-es-ja/freeze-diff-run2.json`.
