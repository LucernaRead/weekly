# D5 rebuild report — 2026-w46-es-pt (W46 es, reader pt)

- Mode: latin; `_D5_READER = "pt"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 453,443 B / SHA256 `d93c906decf7512c82fda4d2105999bc2f68cfb9d724e191be6d47a57f729011` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 495,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader).
  Baseline print 4,067,542 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader pt --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 16/19

- G6: TEXTX 127.3x26.8px. G12: 22/272/1/0/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 1 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 266 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 129.4px, D37 N/A).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:26` — band headline 46 -> 39.5 (gap +12.7px)
- `content12.py:177` — P2 calendar tsize 19 -> 18.5 (margin 6.2px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 0 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 266. G11 0 SPILL.
  G12 22/272/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 241 rows, slack 43.7px. G15a text-layer diff 0;
  text.md DIFF 140 lines, native verifier ADOPT (REWRAP 36, 0 UNEXPECTED).
  G15b (record-only): checker has no pt table (see §6); native verifier ADOPT covers text.md. G16 0 defective.
- D18 gap 129.4px (baseline 203.5px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: -83.9px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta +0;
  only whitespace reflow (7 \n<->space swaps) — no words lost.
- G15b: the shared carryover checker `verify_textmd.py` has no READER_TABLES entry for pt (record-only, D27) — no carryover number exists for this edition. Text.md acceptance rests on G15c (native verifier ADOPT). Shared-tool gap, reported to the coordinator; no edition action.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-pt.pdf` 3,482,901 B
  SHA256 `9a34021a83f146c225d11222780e143a11ed46eaf24297aa425c18c3cf09807b`
- Web `2026-w46-es-pt.web.pdf` 412,608 B
  SHA256 `4542a936df21b2c6d5482d2573be35b6c24b5c27639e430a2071661a6a3d695c`
- text.md 46,614 B SHA256 `7f7ebaee53638be9b2e8a37d12ad48570f1bdf4353e4eb2bdf2e40c68d3f2f45`
  (textexp output, `logs/2026-w46-es-pt/2026-w46-es-pt.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-pt/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-pt/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-pt/g*-run2.log`,
  `logs/2026-w46-es-pt/census-run2.json`, `logs/2026-w46-es-pt/freeze-diff-run2.json`.
