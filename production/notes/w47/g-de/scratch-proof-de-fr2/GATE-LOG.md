# GATE-LOG — W47 de-fr, proof2 (independent re-proofread)
Date: 2026-11-11. All gates run live by proof2 in `~/workspace/weekly-git`.
TMPDIR = this scratch dir's `tmp/` throughout. Edition identity re-verified
unchanged at end (see bottom). Logs cited below live in this scratch dir.

## 0. Probes (before any work)
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` PASS
- Real scratch-file write → OK. Disk 150G total / 74G used / 75G free.
- Identity: print PDF SHA `0df35360ac599e8af590f990ae302dfe17f8daf23904bbc4e5aac6d641ecc413`
  (10,932,565 B); web PDF SHA `5262bfaea8f8947874171b558e704e36bc7f138e3c9419afce5809a76836b167`
  (1,600,197 B); text.md SHA `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6`
  (50,042 B). All match task prefixes. Both PDFs 8 pages, 1462.5×2025 pt.

## 1. occlusion audit (formal run; NO --selftest flag on the audit itself)
- Result: exit 0; selftest OK (6 planted classes fired); **0 flags**; core 0;
  NEW vs core 0.
- Log: `occlusion.log`, `occlusion.json`. PASS.

## 2. p8 extract + compare
- extract: **150/150**. Log: `p8extract.log/.json`.
- compare vs core: CLEAN, missing=[], extra_count=0,
  keydiff=[137, 138, 139, 150] — all 4 expected (137–139 forward DE→FR
  translation keys; 150 open writing task). Log: `p8compare.log/.json`. PASS.

## 3. freeze.py diff
- Result: exit 0; added CJK total **7, all U+3000** (P1 0, P2–P8 1 each).
- Log: `freeze.log`, `freeze.json`. PASS.

## 4. freeze_direct (rebuild-A copy; --core-svg = core-de/svg)
- Source PASS (removed 520 / added 528, unaccounted 0/0).
- Rendered **8/8**; frozen counts P1–P8: 147/163/195/166/173/175/150/186.
- sha8: `083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7`
  (P3 sha changed with Q34 stem, as in rebuild 4).
- Log: `freeze-direct.log/.json`. PASS.

## 5. keycheck-150 (rebuild-A copy)
- **149/150 exact**; only Q150 extractor truncation
  ("Exercice libre — suivez les points de l'encadré d'écriture" → "Exercice libre"),
  expected.
- Log: `keycheck.log`, `keycheck-150.json`. PASS.

## 6. boxtitle.py (rebuild-A copy)
- **7/7 fit**. Independent re-measure from shipped SVG strings via core
  `svglib.text_w(s, "sans", True, sz)` reproduced identical values:
  P2 `DIE STILLE WOCHE　La semaine` 376.9; P3 `WEIHNACHTSWÖRTER　Noël` 339.9;
  P3 `DER TIPP　Conseil` 219.5; P5 `ADVENTSWÖRTER　Avent` 303.5;
  P7 `DER WERKZEUGKASTEN　Outils` 360.5; P7 `LESERBRIEFE　Courrier` 269.9;
  P7 `NOCH EIN WORT　Un mot de plus` 361.3 (budget 400.5; max ink end 1838.4,
  min spare 23.6px).
- Log: `boxtitle.log`. PASS.

## 7. measure.py (rebuild-A copy)
- **24/24 PASS, 0 FAIL**. Log: `measure.log`. PASS.

## 8. creambox.py full scan (family-fix copy; canonical hidden_files/w47/tools/ does not exist)
- All 8 SVGs scanned. P7 toolbox: bottom 803.5, last baseline 783.9, clearance **+19.6**.
  LESERBRIEFE bottom 1372.0 clearance +10.4; NOCH EIN WORT bottom 1538.0 clearance +42.9.
  All other pages' boxes positive (min +14.0) except two known matcher false
  positives (P1 sommaire −24.0, P7 −35.0 rows — identical in core-de, see PROOF-NOTE §7).
- Log: `creambox-all.log`. PASS.

## 9. d2scan.py
- 58 abutting pairs, **0 web gaps >0.5pt**. Log: `d2scan.log/.json`. PASS.

## 10. verify.py rerun (in edition dir)
- Exit 0; TOTAL 150; numbering continuous; **SVGs byte-identical before/after**
  (`svg-sha-before.txt` vs `svg-sha-after.txt`, diff empty).
- §1.1 audit True, old-style hexes []; verbatim OK (8 sentences ×2);
  17 forbidden terms all 0; P8 floor True (13.25 SVG units = 9.9375pt);
  MUSTER 84 words; chart 44+33+23=100; date arithmetic 18.11+11 / 15.11+7 /
  16.11+6 all True; zero FLOW OVERFLOW / HEAD TOO WIDE; flow ends match KIT
  (P8-keys 2426, spare 134px).
- Log: `verify.log`. PASS.

## 11. Print/web text layer comparison
- `pdftotext -layout`: both 115,769 B, word multiset identical (8,121 words).
- `pdftotext -raw`: both 49,698 B, normalised text exactly identical.
- Web PDF has a real text layer. Files: `print.txt`, `web.txt`,
  `print-raw.txt`, `web-raw.txt`. PASS.

## 12. P8 min font (PyMuPDF, both PDFs)
- **9.94pt** ≥ 9.75pt floor; P1 min 11.62pt. PASS.

## 13. Level chips (rx="2.7" rects)
- Per page 10/15/18/15/18/18/12/35 = **141**; P8 A2 22 / B1 13 / B2 0. PASS.

## 14. Q34 five places (proof1 D-01 fix check)
- New stem "Am Montag öffnet in Köln der erste ___." 1× in content34.py,
  text.md, P3 SVG, print text layer, web text layer; old stem 0× in all five.
  PASS.

## 15. Bent-quote counts
- text.md: U+201C 33 / U+201D 0 / U+201E 33 / U+2019 0 (33 German „ " pairs);
  « » 7 pairs; U+0027 42.
- SVG rendered text (201C/201D/201E): P1 5/0/5, P5 6/0/6, P7 21/0/21, P8 1/0/1;
  2019 0 everywhere. No English curly quotes anywhere. PASS.

## 16. §1.1 palette / fonts
- SVG hexes all §1.1 values except inherited core-identical sets (P4 table zebra
  `#f4efe0/#efe8d2`; moth logo `#34483A/#F1E8D4/#7898CD/#4D72B4/#EDD17F/#D7B257/#84A283/#4F765D`;
  light text on dark bands `#cac8ba` — byte-identical counts in core-de).
- Fonts: Newsreader 958, Noto Sans CJK SC 787, Noto Serif CJK SC 25,
  UnifrakturMaguntia 1. PASS.

## 17. Dates (date -d, Europe/Berlin)
- Nov 3 Tue, 4 Wed, 5 Thu, 6 Fri, 7 Sat, 8 Sun, 13 Fri, 16 Mon, 17 Tue,
  18 Wed, 19 Thu, 20 Fri, 22 Sun, 24 Tue, 25 Wed, 26 Thu, 27 Fri, 29 Sun —
  all match the edition's weekday claims. PASS.

## 18. P7 toolbox — 200dpi pixel re-measurement
- Cream block rows 688..1673px = 330.2..803.0 SVG units (nominal box bottom 803.5).
- Last-entry lowest ink row 1643px = 788.6 SVG units (baseline 783.9, `fraglich`
  descender 4.7 SVG units).
- **INK clearance 30px = 14.4 SVG units; BASELINE clearance 19.1 SVG units**
  (nominal 19.6). Both ≥ +10. **PASS.**
- Scripts: `measure_pixels.py`, `measure_pixels2.py`, `measure_pixels3.py`;
  logs `measure-pixels.log`, `measure-pixels2.log`, `measure-pixels3.log`;
  renders `render/print7-200-7.png`, `render/crop-p7-toolbox-200.png` (viewed).

## 19. P8 quote-gap test — 200dpi pixel ink-column measurement (tight-band per-char method)
- Lines use « » (no U+201C/U+201D): H-DE `«Meine Novemberwoche»` (Newsreader
  16.12pt, tight); H-FR `« Ma semaine de novembre »` (Noto Sans CJK SC 15.00pt);
  Q67 `« Im Lande des Christkinds »` (Noto Sans CJK SC 9.94pt).
- H-FR (em=41.7px): word gaps median 14px = 0.34em; » ink 15px = 0.36em,
  gap before » 14px = 0.34em (= line median word gap), gap after 5px = 0.12em.
- Q67 (em=27.6px): word gaps median 9px = 0.33em; » ink 10px = 0.36em,
  gap before » 9px = 0.33em (= line median word gap), gap after 9px = 0.33em.
- H-DE control: « ink 20px = 0.45em, » ink 21px = 0.47em — Newsreader guillemets
  wider than Noto's; no 1.00em full-width glyph anywhere.
- Judgment: gap before closing » = line's own median word-space gap in both
  cases → literal French space in source, NOT a wide-glyph defect. De-en
  signature (wide gap, NO space in source) absent. **NO DEFECT.**
- Crops viewed: `render/crop-h-fr-quote.png`, `render/crop-q67-quote.png`.
  (Crude full-band run superseded: descender contamination at 9.94pt.)

## 20. Visual reads
- Print P1–P8 (100dpi, `render/print-{1..8}.png`): all viewed, clean — zero
  overflow/overlap/footer pressure; images + credits in place.
- Web P1 (`render/web-1-1.png`) and web P8 (`render/web-8-8.png`): both viewed,
  visually identical to print. PASS.

## 21. Full text read + 150-key semantic check
- text.md 1,185 lines fully read. All 150 keys checked semantically against
  stems/article/chart: all correct (details in PROOF-NOTE §5). PASS.

## 22. External facts (browser.search, 2026-11-11)
- Bundesliga MD9 (all 9 results + scorers + 30 goals + table on GD), UCL MD4
  (Atlético–Bayern 0:2 Karl 54'/Laimer 74'; Dortmund–Betis 2:1; Leipzig–Man
  City 2:3; Stuttgart–Galatasaray 0:2), UEL MD4 / Conference MD3
  (Leverkusen–Marseille 0:1; Palace–Hoffenheim 1:1; Trabzon–Freiburg 0:1),
  Serbia–Germany 13 Nov (UEFA ban + children/50-fan exemption, ~5,000),
  Germany–Netherlands 16 Nov (last group game, "Endspiel" usage in real press),
  Cologne markets (16 Nov–23 Dec, closed 22 Nov, opening Tue 17 Nov 19:00,
  Harbour from 13 Nov), Aachen market (20 Nov–23 Dec, 53rd ed.),
  Wilhelm Ritter (1860–1948, "Weihnachtsmarkt auf der vorderen Insel Schütt"
  1930), Buß- und Bettag (Saxony-only since 1995; SächsSFG §6 dance ban
  3:00–24:00), Kepler "Im Lande des Christkinds" 1903 (first printed Advent
  calendar), Bundeshaushalt 2027 (adoption Fri 27 Nov), Stromsteuer 2.05 ct/kWh
  + Merz cut plan, MD10 fixtures, UCL MD5, UEL MD5 — ALL CONFIRMED.
  Sources in PROOF-NOTE §6. PASS.

## 23. ABSTRACT.txt
- French single line, no ASCII double quotes, facts consistent. PASS.

## Final identity re-check (after all work)
- print PDF `0df35360ac599e8af590f990ae302dfe17f8daf23904bbc4e5aac6d641ecc413`
- web PDF `5262bfaea8f8947874171b558e704e36bc7f138e3c9419afce5809a76836b167`
- text.md `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6` (50,042 B)
- All three identical to the start-of-task values. Edition untouched during proofread.
  (The edition directory is untracked in git — `?? production/2026-w47/2026-w47-de-fr/`
  — production source not yet inserted into `issues/`; no modification.)

## Summary
- Gates run: 23. Pass: 23. Fail: 0. Defects: 0.
- Conclusion: **(a) zero defects → this edition is final.**
