# de-fr per-edition record (4th shift, rebuild 3, 2026-11-11)

## Conclusion
de-fr COMPLETE. ALL GATES PASS (rebuild 3, 2026-11-11 04:38 UTC). 8-page visual
proofread zero findings. 150-question key check 149/150 exact (Q150 = extractor
truncation, expected). P8 chips 35, whole-issue chips 141.
Independent proofread pending (coordinator to assign).

## Deliverables (in production/2026-w47/2026-w47-de-fr/)
- 8 SVG: p1-front, p2-leben, p3-kultur, p4-sport, p5-jugend, p6-vertiefung,
  p7-sprache, p8-uebungen
- Print PDF: Die-Lucerna-VOL4-de-fr.pdf — 10,932,758 bytes,
  sha256 acfdfb0d914b097d7a6cabb34f19c32068273a52242ec19155b5a697ac3a05f8
- Web PDF: Die-Lucerna-VOL4-de-fr-web.pdf — 1,557,331 bytes,
  sha256 2b13edd197ecd80559ef65329e7e4e2aef5bc5051cc8d04dca030235fb8791e4
- Text: 2026-w47-de-fr.text.md — 50,116 bytes, 48,235 chars, 591 entries, 150 ex.,
  sha256 effbd257252256566ba2af9caee79bbeecc54d01f39813e51ac0c617553b2a8b
- ABSTRACT.txt: one line, French, 414 bytes, 0 ASCII double quotes
- WEEKLY-KIT.md: written (fr edition record)

## Gates (rebuild3.log; full gate logs in this dir)
- run.py exit 0; 0 FLOW OVERFLOW; 0 HEAD TOO WIDE; TOTAL 150
- measure.py 24/24 PASS, 0 FAIL
- verify.py: TOTAL 150, numbering continuous, SVGs byte-identical after re-run,
  SOP 1.1 style audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags (selftest OK)
- p8 extract 150/150; compare CLEAN; keydiff [137, 138, 139, 150] (expected)
- freeze diff exit 0; added CJK 7 (all U+3000)
- print/web text: default word multiset identical (50,955B / 50,957B);
  raw normalised identical (49,772B each)
- chips per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0
- P8 min font 9.94pt >= 9.75pt
- flow ends: P1-headline 1554 (= core), P3-main 916, P3-ex 2041, P5-ex 2441 (= core),
  P8-keys 2426 (spare 134), P8-battery 1409, P8 image height 140,
  P3 col3 1612.66 (hline 1668, 55px clear), P4 col3 1156.02 (edge-touch, like core),
  P5 col3 image 1732.93 (hline 1744, 11px), P7 col3 1518.0 (30px clear of 1548 Sätze rule)

## Freeze direct sha256 (8/8, freeze-direct.json)
- Source-level: AST string-literal multiset core vs edition — 0 unaccounted
  removed, 0 unaccounted added (520 removed / 528 added, every one accounted for
  by tr_fr.py, the CJK inventory, or a documented transform artifact).
- Rendered-level frozen intersection per page: P1 147 / P2 163 / P3 195 / P4 166 /
  P5 173 / P6 175 / P7 150 / P8 186 strings;
  sha 083e2a2a / 689045ad / 093cf378 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7
  — identical to de-en (the frozen content is the shared German text).

## 150-question key check (keycheck-150.json)
P8-SVG-extracted keys vs REG from the edition's own sources: 149/150 exact.
Only Q150 differs: extractor truncates REG key "Exercice libre — suivez les points
de l'encadré d'écriture" to "Exercice libre" (expected; Q150 is the open writing
task, already in the keydiff set). REG by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18,
7:12, 8:38}; levels A2 69 / B1 67 / B2 14; types choix multiple 52 / à compléter 41 /
transformation 11 / vrai ou faux 8 / texte à trous 8 / phrases à construire 8 /
associations 12 / traduction 4 / dialogue à compléter 5 / rédaction 1.

## Visual proofread (8 pages, print PDF @100dpi + magnified crops)
Zero findings. All 8 pages viewed one by one; magnified crops of the P1
word-of-week line (1 line, clears the 1844 hline) and the P4 Und-Sie box
(2-line German + 2-line French prompt, clear of the results table). Fixed spots
re-checked: P1 ZAHLEN box + Fragen line, P5 col3 image/hline + 1-line bridges,
P6 ÜBUNGSDATEN single line, P7 toolbox/NOCH EIN WORT, P8 battery head
"C LESEVERSTEHEN Lecture" + keys end 2426. U+2019 across the 8 SVGs is 0
(straight U+0027 used from the start in tr_fr.py).

## Builds (this edition)
- Build 1 (2026-11-11 ~03:20 UTC): failed 4 gates — P1-headline FLOW OVERFLOW
  (ZAHLEN box column jump), P5-ex overflow, P8-battery HEAD TOO WIDE, occlusion
  28 flags. Diagnosed, fixed in tr_fr.py (fix_tr_fr.py, 88 value fixes + LAYOUT
  pad fix). Logs archived in fr-build1/; edition dir deleted and rebuilt.
- Build 2 (2026-11-11 ~04:19 UTC): failed 3 gates — occlusion 1 LINEX flag
  (P1 word-of-week para 2nd line crossed the 1844 hline) and print/web default
  word multiset (artifact of a 69.6 MB print PDF with 335 embedded font subsets
  from a render run under heavy parallel-family CPU contention; a clean re-render
  of the same SVGs is ~10.9 MB / 35 fonts and extracts identically). Fixed in
  tr_fr.py (fix_tr_fr2.py, 1 fix: para shortened to 1 line). Edition dir deleted
  and rebuilt; topband wording left unchanged (isolated print-vs-web test with
  subset fonts proved it extracts identically — topband_test.py).
- Rebuild 3 (2026-11-11 04:38 UTC): ALL GATES PASS. Print PDF 10,932,758 bytes.

## Core source check
core-de/content8.py sha256 9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4
— unchanged since this shift started; no re-copy needed.

## Files in this dir
- build.log, render.log, webpdf.log, verify.log, occlusion.log, occlusion.json,
  p8extract.log, p8extract.json, p8compare.log, p8compare.json, freeze.log,
  freeze.json, export.log, print.txt, web.txt, rebuild3.log (full gate driver output),
  measure3.log, transform-fr3.log, keycheck-150.json (150-question key table),
  freeze-direct.json (direct freeze proof)
- fr-build1/ (failed build-1 gate logs, archived), transform-fr.log (build-2 transform)
