# D5 rebuild report — 2026-w46-es-ru (W46 es, reader ru)

- Mode: ru (old branch, D26); `_D5_READER = "ru"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 506,271 B / SHA256 `a8783ca4ee1971dd9ad8d9c4e53f4dac126b7a863ee994326749949a18f57b9f` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 345,
  D5 Cyrillic-in-CJK 253, curly-in-CJK 0, curly total 0 (all Newsreader).
  Baseline print 4,111,508 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader ru --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 17/19

- G6: 0 flags. G12: 26/376/1/0/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 1 defects.
  G10: CJK added 1 (P6 U+3000 run-split), Latin added 165 (run-split).
  All other scored gates PASS (G1 150/0/0, G2 0 defects, G3 0/0/0, G4 8 pp, G5 <7 MB,
  G7 150/150, G8 CLEAN, G9 8/8, G11 0 SPILL, G13 0 TOUCH/NEAR, G15a text-layer diff 0,
  G15c ADOPT, G16 0 defective, D18 150.0px, D37 N/A).

## run1 -> run2 fixes (font-size reduction only; no copy changes)

- `content12.py:71` — P1 guide 19 -> 18 (margin 5.8px)

- Probe method: SVG-measured ink widths, linear scaling to >= 2px margin
  (`bin/apply_fixes.py`, each edit asserted unique + `ast.parse` clean; all added
  `tsize=` kwargs grep-verified as real arguments). Band headline probed against the
  full translation line (text_w; de probe reproduces the run1 TEXTX 103.8px exactly).

## run2 gates — 19/19 ALL-GREEN

- G1 TOTAL 150, OVF 0, HDW 0. G2 0 defects. G3 Latin 0 / Cyrillic 0 / curly-in-CJK 0;
  curly total 0 all Newsreader; Noto Sans 789. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]).
  G9 baseline 8/8. G10 CJK added 1, Latin added 165. G11 0 SPILL.
  G12 26/376/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 234 rows, slack 42.7px. G15a text-layer diff 0;
  text.md DIFF 94 lines, native verifier ADOPT (REWRAP 22, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5491 md=6883. G16 0 defective.
- D18 gap 150.0px (baseline 175.8px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: -6.8px.
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta -1;
  only whitespace reflow (4 \n<->space swaps) — no words lost.
- P8 reflow: patched P8 has 234 lines vs baseline 237 (creambox P8 diff 189 elements, moved 15); the P8 note SET is byte-identical baseline-vs-patched (150/150, same set) — pure layout reflow from the D5 font change, no content loss. P8 slack unchanged 42.7px. D39(4): P7 band moved down 29px vs baseline (-35.8 -> -6.8px) but stays above the footer line.
- G3 Noto Sans 789: ru Cyrillic correctly in Noto Sans (D26 old branch); baseline Cyrillic sat in a CJK font (d5_cyrillic_in_cjk 253) — the D5 fix.

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-ru.pdf` 3,776,995 B
  SHA256 `90665b4d609dc9d478d22c10678053adce89d0b9e6837feb06e6b421b660f0e8`
- Web `2026-w46-es-ru.web.pdf` 664,679 B
  SHA256 `3c0e1155dbf7f93ff2f3ca2852c14e058776b7e79eee8caaaa3d3ccc48abcf57`
- text.md 54,065 B SHA256 `1659e089e12b78806eb28fad85b25259bf599d8099b1a25475a662d22b64f90c`
  (textexp output, `logs/2026-w46-es-ru/2026-w46-es-ru.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-ru/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-ru/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-ru/g*-run2.log`,
  `logs/2026-w46-es-ru/census-run2.json`, `logs/2026-w46-es-ru/freeze-diff-run2.json`.
