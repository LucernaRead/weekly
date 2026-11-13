# de-es per-edition record (rebuild-A, rebuild 4, 2026-11-11)

## Conclusion
de-es COMPLETE. ALL GATES PASS (rebuild 4, 2026-11-11 08:24 UTC). 8-page visual
proofread zero findings. 150-question key check 149/150 exact (Q150 = extractor
truncation, expected). P8 chips 35, whole-issue chips 141.
Independent proofread pending (coordinator to assign).

## Why this rebuild
core-de was re-finalised as build15 (proof5 (a) zero findings, 2026-11-11 08:02 UTC)
with exactly one content change: Q34 stem in `content34.py:105`
`"Am Montag öffnen in Köln die ersten ___."` →
`"Am Montag öffnet in Köln der erste ___."` (key `Weihnachtsmarkt` unchanged).
The previous de-es (rebuild 3) carried the old plural stem, so the edition was
deleted and re-transformed from the new core. No other content was intentionally
changed: es needed no box-title fix this round (its five titles were already
shortened in rebuild 3 and re-verified 7/7).

## Deliverables (in production/2026-w47/2026-w47-de-es/)
- 8 SVG: p1-front, p2-leben, p3-kultur, p4-sport, p5-jugend, p6-vertiefung,
  p7-sprache, p8-uebungen
- Print PDF: Die-Lucerna-VOL4-de-es.pdf — 10,968,803 bytes,
  sha256 7bc39e1f58b9bb447caf4f69b397eb39723ab2fef1c2bc4cf99d1be4a6e580ed
- Web PDF: Die-Lucerna-VOL4-de-es-web.pdf — 1,558,821 bytes,
  sha256 cd453143111bfad4f7f8a6ada98190f1790d2feccdaf3fd7c762a3a683043b90
- Text: 2026-w47-de-es.text.md — 50,124 bytes, 48,286 chars, 591 entries, 150 ex.,
  sha256 5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3
- ABSTRACT.txt: one line, Spanish, 426 bytes, 0 ASCII double quotes
- WEEKLY-KIT.md: restored from the rebuild-3 KIT and updated to rebuild-4 values
  (source build15, new gate numbers, Q34 note).

## Q34 stem verification (old stem must be 0, new stem 1x, everywhere)
- `content34.py` source: new 1, old 0
- `2026-w47-de-es.text.md`: new 1, old 0
- `svg/p3-kultur.svg`: new 1, old 0
- print PDF text layer (pdftotext, whitespace-normalised): new 1, old 0
- web PDF text layer (same): new 1, old 0
- P3 visual: Q34 renders as "Am Montag öffnet in Köln der erste ___." (see目视 P3).

## Gates (rebuild4.log; full gate logs in this dir)
- run.py exit 0; 0 FLOW OVERFLOW; 0 HEAD TOO WIDE; TOTAL 150
- measure.py 24/24 PASS, 0 FAIL (measure1.log)
- precheck.py 24/24 PASS, 0 FAIL; boxtitle.py 7/7 (no change needed)
- verify.py: TOTAL 150, numbering continuous, SVGs byte-identical after re-run,
  SOP 1.1 style audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags (selftest OK)
- p8 extract 150/150; compare CLEAN; keydiff [137, 138, 139, 150] (expected)
- freeze diff exit 0; added CJK 7 (all U+3000, 1 per page P2–P8)
- print/web text: default word multiset identical (51,012B / 51,013B);
  raw normalised identical (49,812B each)
- chips per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0
- P8 min font 9.94pt >= 9.75pt
- export exit 0
- U+2019 scan: 0 across all 8 SVGs

## Freeze direct sha256 (8/8)
- Source-level PASS: removed / added literals all accounted for
  (0 unaccounted either way).
- Rendered-level frozen intersection per page: P1 147 / P2 163 / P3 195 / P4 166 /
  P5 173 / P6 175 / P7 150 / P8 186 strings;
  sha 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7.
  Only P3 sha differs from the rebuild-3 reference (093cf378 → fc88f676): the
  frozen set still has 195 strings, but the Q34 stem string itself changed
  (plural → singular), so its hash changed. All other pages byte-identical to
  the reference. This is the expected Q34 fingerprint, identical to de-en/de-fr.

## 150-question key check (keycheck-150.json)
P8-SVG-extracted keys vs REG from the edition's own sources: 149/150 exact.
Only Q150 differs: extractor truncates REG key "Tarea libre — sigue los puntos
del recuadro de escritura" to "Tarea libre" (expected; Q150 is the open writing
task, already in the keydiff set). REG by page {1:10, 2:18, 3:18, 4:18, 5:18,
6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.

## Flow ends (identical to rebuild 3)
P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523, P2-feature 993,
P2-ex 2332, P3-main 886, P3-ex 2333, P4-main 677, P4-ex 2315, P5-main 996,
P5-ex 2441 (= core), P6-main 747, P6-ex 2523, P7-A2 1278 / B1 1342 / B2 1306,
P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103), P8 image height 140;
P3 col3 1643.19 (hline 1668, 25px clear), P4 col3 1156.02 (edge-touch, like core),
P5 col3 image 1732.93 (hline 1744, 11px), P7 col3 1518.0 (30px clear of 1548 rule).

## Visual proofread (8 pages, print PDF @100dpi, renders /tmp/es4-proof/p-*.png)
Zero findings.
- P1: masthead, headline, ZAHLEN box in column, JETZT ÜBEN, FRAGEN sidebar,
  IN DIESER AUSGABE, word of the week, football photo + caption, KURZ & GUT,
  BLITZQUIZ, footer clean.
- P2: article, Note box, four side boxes, RECHNEN table, exercises A–D clean.
  "DIE STILLE WOCHE Tranquila" inside its box.
- P3: article, Note box, 1930 market painting + caption, WEIHNACHTSWÖRTER box
  ("Palabras" inside), UND SIE?, DER TIPP ("Consejo" inside), exercises A–D
  clean. Q34 new singular stem visible.
- P4: article, Note box, header photo + caption, UND SIE? box inside, 9-row
  results table, exercises A–D clean. O1 preserved as ruled.
- P5: article, Note box, ADVENTSKALENDER/ADVENTSWÖRTER ("Adviento" inside),
  UND SIE?, 1903 calendar image + caption, week-plan table, exercises A–D clean.
- P6: article, Note box, DIE ZAHLEN, DIE STILLE WOCHE, DIE DEBATTE, poll bars
  (44/33/23, labels clear), ÜBUNGSDATEN single line, exercises A–D clean.
- P7: three lessons (A2/B1/B2), toolbox (6 entries, last inside the box),
  LESERBRIEFE ("Cartas" inside, with Spanish disclosure), NOCH EIN WORT,
  reading-room photo + caption, Sätze der Woche 8, FEHLERKLINIK 4 groups,
  VOL.5 band clean.
- P8: A cloze / B Quiz / C reading / D sentence building / E translation
  (137–140) / F matching / G dialogue (5 badges) / H writing (MUSTER 84 words) /
  ANTWORTEN 8 groups all complete, image in place, keys end 2457 (103px above
  the bottom).

## Core source check
- core-de build15 verified at rebuild start (see de-en record): print
  22,965,197 B sha 49beffc4…; web 2,044,855 B sha 9b63b413…; text 49,798 B
  sha 0952bc51…. New Q34 stem 1x in core `content34.py:105`; old stem 0x.

## Files in this dir
- build.log, render.log, webpdf.log, verify.log, occlusion.log, occlusion.json,
  p8extract.log, p8extract.json, p8compare.log, p8compare.json, freeze.log,
  freeze.json, export.log, print.txt, web.txt, rebuild4.log (full gate driver
  output), transform-es.log, measure1.log, precheck-es.log, boxtitle-es.log,
  keycheck-150.json, keycheck.log, freeze-direct.json, freeze-direct.log
