# de-en per-edition record (3rd shift, rebuild 2, 2026-11-11)

## Conclusion
de-en COMPLETE. ALL GATES PASS (rebuild 2, 2026-11-11 02:53 UTC). 8-page visual
proofread zero findings after the apostrophe fix. 150-question key check 149/150
exact (Q150 = extractor truncation, expected). P8 chips 35, whole-issue chips 141.
Independent proofread pending (coordinator to assign).

## Deliverables (in production/2026-w47/2026-w47-de-en/)
- 8 SVG: p1-front, p2-leben, p3-kultur, p4-sport, p5-jugend, p6-vertiefung,
  p7-sprache, p8-uebungen
- Print PDF: Die-Lucerna-VOL4-de-en.pdf — 10,966,416 bytes,
  sha256 a997c6cefe8467bdd37a71158e0f61ceff16d653039f50159b1608305b3a4b87
- Web PDF: Die-Lucerna-VOL4-de-en-web.pdf — 1,555,614 bytes,
  sha256 62623cb5996644004ba48a6ed7246cdd0584bec3a2549123174db318384a3a90
- Text: 2026-w47-de-en.text.md — 49,676 bytes, 48,045 chars, 591 entries, 150 ex.,
  sha256 0749ad78f536883f8f3a484d7c93f026d0f7d7f433891861333f7a9a8fbf3830
- ABSTRACT.txt: one line, English, 356 bytes, 0 ASCII double quotes
- WEEKLY-KIT.md: written (en edition record)

## Gates (rebuild2.log; full gate logs in this dir)
- run.py exit 0; 0 FLOW OVERFLOW; 0 HEAD TOO WIDE; TOTAL 150
- measure.py 24/24 PASS, 0 FAIL
- verify.py: TOTAL 150, numbering continuous, SVGs byte-identical after re-run,
  SOP 1.1 style audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags (selftest OK)
- p8 extract 150/150; compare CLEAN; keydiff [137, 138, 139, 150] (expected)
- freeze diff exit 0; added CJK 7 (all U+3000)
- print/web text: default word multiset identical (50,445B / 50,446B);
  raw normalised identical (49,288B each)
- chips per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0
- P8 min font 9.94pt >= 9.75pt
- flow ends: P1-headline 1554 (= core), P5-ex 2441 (= core), P8-keys 2481 (spare 79),
  P8-battery 1409, P8 image height 140, P3 col3 1643.19 (hline 1668, 25px clear),
  P4 col3 1156.02 (edge-touch, like core), P5 col3 image 1732.93 (hline 1744, 11px),
  P7 col3 1518.0 (30px clear of 1548 Sätze rule)

## Freeze direct sha256 (8/8)
- Source-level: all core no-CJK string literals (2033) present in the edition with
  the same count; only 8 absent, all expected transform artifacts (subtitle,
  full-width parens, spaced separator, PDF name, verify docstring/path).
  All added no-CJK strings are English.
- Rendered-level frozen intersection per page: P1 147 / P2 163 / P3 195 / P4 166 /
  P5 173 / P6 175 / P7 150 / P8 186 strings;
  sha 083e2a2a / 689045ad / 093cf378 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7.

## 150-question key check (keycheck-150.json)
P8-SVG-extracted keys vs REG from the edition's own sources: 149/150 exact.
Only Q150 differs: extractor truncates REG key "Open task — follow the points in
the writing box" to "Open task" (expected; Q150 is the open writing task, already
in the keydiff set). REG by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38};
levels A2 69 / B1 67 / B2 14; types MC 52 / fill-in 41 / transformation 11 /
true-false 8 / cloze 8 / sentence building 8 / matching 12 / translation 4 /
dialogue 5 / writing 1.

## Visual proofread (8 pages, print PDF @100dpi + magnified crops)
Zero findings after the apostrophe fix. Per-page notes in FANOUT-REPORT-de.md
("de-en 目视"). The only defect found: 9 English strings used curly apostrophe
U+2019, which renders as a wide full-width glyph in Noto Sans CJK SC
("Let' s calculate", "Editor' s tip", …). Fixed by replacing with straight
apostrophe U+0027 (as \u0027 escapes in tr_en.py single-quoted strings — a raw '
would terminate the literal; the first attempt broke compilation and was fixed
the same way). Rebuild 2 re-ran all gates; 5 magnified crops confirm tight
rendering; total U+2019 across the 8 SVGs is 0. Rule added to tr_en.py docstring
and to the en KIT §7. Lesson for the remaining 9 languages: use straight
apostrophes from the start; scan for U+2019 in every edition's self-check.

## Core source check
core-de/content8.py sha256 9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4
— unchanged since this shift started; no re-copy needed.

## Files in this dir
- build.log, render.log, webpdf.log, verify.log, occlusion.log, occlusion.json,
  p8extract.log, p8extract.json, p8compare.log, p8compare.json, freeze.log,
  freeze.json, export.log, print.txt, web.txt, rebuild2.log (full gate driver output),
  transform-en.log, keycheck-150.json (150-question key table)
