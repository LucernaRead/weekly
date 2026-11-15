# D5 rebuild report — 2026-w46-es-zh-cn (W46 es, reader zh-cn)

- Mode: cjk; `_D5_READER = "zh-cn"`. D5-only family (§1.1 already in the style-port baseline).
- Baseline (shipped): issues pin print 939,647 B / SHA256 `fd4c89ff9041eb445d13749e543c7a489f534ddf6a953146e39032291d525363` — verified against the
  issues PDF file (bytes + SHA match). Baseline build: TOTAL 150, OVF 0, HDW 0;
  print/web text-layer stripped-diff 0; text.md BYTE-IDENTICAL to issues
  (textexp_es.py, native verifier ADOPT). Baseline census: D5 Latin-in-CJK 339,
  D5 Cyrillic-in-CJK 0, curly-in-CJK 3, curly total 6 (all Newsreader).
  Baseline print 16,098,719 B.
- Install: `apply_variant.py --svglib <patched> --target es --reader zh-cn --week 2026-w46`
  (`--check` dry-run clean first). Routing test `test_d5_routing.py` FAILURES: 0.
  fix2 retained (`_QUOTE_CLS` x4).

## run1 gates — 18/19

- G6: 0 flags. G12: 30/352/0/2/0 (titles/body/DEFECT/OBSERVE/marginal). G14: 2 defects.
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
  curly total 6 all Newsreader; Noto Sans 0. G4 print 8 pp. G5 web <7 MB.
  G6 0 flags. G7 extract 150/150. G8 CLEAN (keydiff [137, 138]; zh-cn [] — core-es is the zh-cn template).
  G9 baseline 8/8. G10 CJK added 1, Latin added 221. G11 0 SPILL.
  G12 28/354/0/0/0 (titles/body/DEFECT/OBSERVE/marginal). G13 0 TOUCH, 0 NEAR.
  G14 0 defects; P8 200 rows, slack 58.4px. G15a text-layer diff 0;
  text.md DIFF 86 lines, native verifier ADOPT (REWRAP 23, 0 UNEXPECTED).
  G15b (record-only): CARRYOVER FAIL svg=5905 md=7977. G16 0 defective.
- D18 gap 103.0px (baseline 165.1px — narrowed by the wider Newsreader slogan + date, still PASS).
  D37 N/A — no badge line in the box zone (only de/it/ko have the y=614 badge); strapline y=372 above box top 588 (baseline N/A).
  D39(4) P7 band bottom vs footer 2596: +4.6px (pre-existing).
- Content preservation (fitz, baseline-vs-run2 print text layer): char delta -5;
  only whitespace reflow (7 \n<->space swaps) — no words lost.
- D39(4): P7 band bottom 2600.6 vs footer 2596 (+4.6px crossing) is PRE-EXISTING — baseline identical (+4.6px); accepted per D39(4).
- core-es cross-check: this edition is the reader-dir build; core-es differs only in the 4 furniture lines (see family report §0).

## Deliverables (run2)

- Print `La-Lucerna-VOL3-es-zh-cn.pdf` 4,874,811 B
  SHA256 `75783010e42b644b7a191b92a539bcc3d225372f4e2316cfc47170c9bd4015b5`
- Web `2026-w46-es-zh-cn.web.pdf` 756,631 B
  SHA256 `d33dae9eabbeeb01e78e7336b3ad918962126f36e22a4b012538260a5515cc60`
- text.md 44,710 B SHA256 `bb704230b486d73d976168f9d11588b9e60d424fe2770a81d11a2acbabc6d35a`
  (textexp output, `logs/2026-w46-es-zh-cn/2026-w46-es-zh-cn.text.md.run2`; the `<slug>.text.md` inside the
  edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it)
- KIT: `patched/2026-w46-es-zh-cn/WEEKLY-KIT.md` (pin updated + D5 section).
- Logs: `logs/2026-w46-es-zh-cn/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-zh-cn/g*-run2.log`,
  `logs/2026-w46-es-zh-cn/census-run2.json`, `logs/2026-w46-es-zh-cn/freeze-diff-run2.json`.
