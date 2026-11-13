# de-en per-edition record (rebuild-A, rebuild 3, 2026-11-11)

## Conclusion
de-en COMPLETE. ALL GATES PASS (rebuild 3, 2026-11-11 ~08:15 UTC). 8-page visual
proofread zero findings. 150-question key check 149/150 exact (Q150 = extractor
truncation, expected). P8 chips 35, whole-issue chips 141.
Independent proofread pending (coordinator to assign) — note: the previous
proof1 (a) is void because it was done against the old Q34 stem; a fresh full
proofread round must be assigned.

## Why this rebuild
core-de was re-finalised as build15 (proof5 (a) zero findings, 2026-11-11 08:02 UTC)
with exactly one content change: Q34 stem in `content34.py:105`
`"Am Montag öffnen in Köln die ersten ___."` →
`"Am Montag öffnet in Köln der erste ___."` (key `Weihnachtsmarkt` unchanged).
The previous de-en (rebuild 2) carried the old plural stem, so the edition was
deleted and re-transformed from the new core. No other content was intentionally
changed, except the one box-title fix below (a real defect the previous rounds
missed — see §"Box-title fix").

## Deliverables (in production/2026-w47/2026-w47-de-en/)
- 8 SVG: p1-front, p2-leben, p3-kultur, p4-sport, p5-jugend, p6-vertiefung,
  p7-sprache, p8-uebungen
- Print PDF: Die-Lucerna-VOL4-de-en.pdf — 10,966,409 bytes,
  sha256 47aae035c9531818bce832e25b2aed6ed2557c18229c514bf32443fb6becd429
- Web PDF: Die-Lucerna-VOL4-de-en-web.pdf — 1,555,605 bytes,
  sha256 37ba00d4fcf83f7dd78fe6427d5b0c1ae70c9035fbe8dd345dfde8de13d12875
  (file name is `-web.pdf`, same as the previous round; see note at the end)
- Text: 2026-w47-de-en.text.md — 49,665 bytes, 48,034 chars, 591 entries, 150 ex.,
  sha256 2eb0363202b8c9eacc8aaaf5008eedab614b8ddb0301082e92eb80cd25d6b7f5
- ABSTRACT.txt: one line, English, 356 bytes, 0 ASCII double quotes
- WEEKLY-KIT.md: restored from the rebuild-2 KIT and updated to rebuild-3 values
  (source build15, new gate numbers, Q34 + box-title notes).

## Q34 stem verification (old stem must be 0, new stem 1x, everywhere)
- `content34.py` source: new 1, old 0
- `2026-w47-de-en.text.md`: new 1, old 0
- `svg/p3-kultur.svg`: new 1, old 0
- print PDF text layer (pdftotext, whitespace-normalised): new 1, old 0
- web PDF text layer (same): new 1, old 0
- P3 visual: Q34 renders as "Am Montag öffnet in Köln der erste ___." (see目视 P3).

## Gates (rebuild3.log; full gate logs in this dir)
- run.py exit 0; 0 FLOW OVERFLOW; 0 HEAD TOO WIDE; TOTAL 150
- measure.py 24/24 PASS, 0 FAIL (measure1.log)
- precheck.py 24/24 PASS, 0 FAIL; boxtitle.py 7/7 after the fix below
- verify.py: TOTAL 150, numbering continuous, SVGs byte-identical after re-run,
  SOP 1.1 style audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags (selftest OK)
- p8 extract 150/150; compare CLEAN; keydiff [137, 138, 139, 150] (expected)
- freeze diff exit 0; added CJK 7 (all U+3000, 1 per page P2–P8)
- print/web text: default word multiset identical (50,434B / 50,435B);
  raw normalised identical (49,277B each)
- chips per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0
- P8 min font 9.94pt >= 9.75pt
- export exit 0
- U+2019 scan: 0 across all 8 SVGs

## Freeze direct sha256 (8/8)
- Source-level PASS: removed 520 / added 528 literals, 0 unaccounted either way.
- Rendered-level frozen intersection per page: P1 147 / P2 163 / P3 195 / P4 166 /
  P5 173 / P6 175 / P7 150 / P8 186 strings;
  sha 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7.
  Only P3 sha differs from the rebuild-2 reference (093cf378 → fc88f676): the
  frozen set still has 195 strings, but the Q34 stem string itself changed
  (plural → singular), so its hash changed. All other pages byte-identical to
  the reference. This is the expected Q34 fingerprint.

## 150-question key check (keycheck-150.json)
P8-SVG-extracted keys vs REG from the edition's own sources: 149/150 exact.
Only Q150 differs: extractor truncates REG key "Open task — follow the points in
the writing box" to "Open task" (expected; Q150 is the open writing task, already
in the keydiff set). REG by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38};
levels A2 69 / B1 67 / B2 14.

## Flow ends (identical to rebuild 2 — only Q34 + the box title moved)
P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523, P2-feature 964,
P2-ex 2332, P3-main 886, P3-ex 2363, P4-main 677, P4-ex 2315, P5-main 1026,
P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 / B1 1342 / B2 1306,
P8-battery 1409, P8-keys 2481 (bottom 2560, spare 79), P8 image height 140;
P3 col3 1643.19 (hline 1668, 25px clear), P4 col3 1156.02 (edge-touch, like core),
P5 col3 image 1732.93 (hline 1744, 11px), P7 col3 1518.0 (30px clear of 1548 rule).

## Box-title fix (real defect, found by boxtitle.py precheck — NOT part of Q34)
- Precheck: `boxtitle.py en` failed 1/7 — `WEIHNACHTSWÖRTER　Christmas words`
  measures 483.5px at 24pt bold against the 400.5px box budget (box x 1439.5,
  right edge 1862.0). The title ink ran 83px past the cream box onto the
  newsprint. Confirmed visually on the rebuild-2 P3 render (crop
  /tmp/bt-proof/en-p3-weihn.png): "words" sits outside the cream box.
  The previous rounds claimed en/fr "clean" but never actually ran boxtitle.py
  on en/fr (the sweep covered only the 8 languages of the 5th shift); the
  visual proofreads missed the spill. Same defect class as de-es build 2
  (5 titles over, fixed by shortening).
- Fix (only in this rebuild's `tr_en.py`, diff in `../tr-fixes.diff`):
  `WEIHNACHTSWÖRTER　Christmas words` → `WEIHNACHTSWÖRTER　Words` (359.9px).
  Bare-noun pattern, same as it `Parole` / pt `Palavras` / es `Palabras`.
  German head untouched; the key occurs once in core (`content34.py:58`,
  the P3 box head), so nothing else changed. boxtitle.py re-run: 7/7.
- Rebuilt P3 crop confirms "WEIHNACHTSWÖRTER　Words" sits fully inside the
  cream box (see 目视 P3).

## Visual proofread (8 pages, print PDF @100dpi, renders /tmp/en3-proof/p-*.png)
Zero findings.
- P1: masthead, headline, ZAHLEN box in column, JETZT ÜBEN, FRAGEN sidebar,
  IN DIESER AUSGABE, word of the week, football photo + caption, KURZ & GUT,
  BLITZQUIZ, footer clean. "Germany's five hot questions" apostrophe tight.
- P2: article, Note gloss box, four side boxes, RECHNEN table, exercises A–D
  clean. "Let's calculate" / "This week's dates" tight (straight apostrophes).
- P3: article, Note box, 1930 market painting + caption, WEIHNACHTSWÖRTER box
  (title now inside the cream box), UND SIE?, DER TIPP ("Editor's tip" tight),
  exercises A–D clean. Q34 new singular stem visible.
- P4: article, Note box, header photo + caption, UND SIE? box touching the
  results table edge without overlap, 9-row results table, exercises A–D clean.
  O1 preserved as ruled (not a defect): prose "VfB Stuttgart verlor in Istanbul
  bei Galatasaray mit 0:2" is in the article; the results table lists Bundesliga
  only. Nothing was "fixed" there.
- P5: article, Note box, ADVENTSKALENDER/ADVENTSWÖRTER (title inside box),
  UND SIE?, 1903 calendar image + caption (caption clear of the rule),
  editors' week table ("The editors' week" tight), exercises A–D clean.
- P6: article, Note box, DIE ZAHLEN, DIE STILLE WOCHE, DIE DEBATTE, poll bars
  (44/33/23, labels clear), ÜBUNGSDATEN single line, exercises A–D clean.
  Chart note "editors' practice" tight.
- P7: three lessons (A2/B1/B2), toolbox (6 entries, last inside the box),
  LESERBRIEFE (with 3-line disclosure), NOCH EIN WORT, reading-room photo +
  caption, Sätze der Woche 8 items, FEHLERKLINIK 4 groups, VOL.5 band clean.
  "Readers' / Editor's / Learners'" tight.
- P8: A cloze (113–120, 8 badges) / B Quiz (121–123) / C reading (124–132) /
  D sentence building (133–136) / E translation (137–140) / F matching (141–144)
  / G dialogue (145–149, 5 badges) / H writing (MUSTER 84 words) / ANTWORTEN
  8 groups all complete, image in place, keys end above the footer.
  Key "133. Die Bundesliga kehrt…" shows no glued words.

## Core source check
- core-de build15 verified at rebuild start: print 22,965,197 B
  sha256 49beffc4223ede29674a3c70c341ec9fc04d2103eb632d1194e8ffcb31250607;
  web 2,044,855 B sha256 9b63b413424caa99ed255c7b84dc8368df3ad39f1de956768bbe2353037c01a8;
  text 49,798 B sha256 0952bc517e96351e505d4790237aa00d4ca36032763ec256d005d6eeec3c8b48.
- New Q34 stem present 1x in core `content34.py:105`; old stem 0x.
- Starter probe (2026-11-11 08:05 UTC): `git hash-object -w` OK, real file write
  to this scratch dir OK; disk 150G total, 104G used, 46G free.

## Files in this dir
- build.log, render.log, webpdf.log, verify.log, occlusion.log, occlusion.json,
  p8extract.log, p8extract.json, p8compare.log, p8compare.json, freeze.log,
  freeze.json, export.log, print.txt, web.txt, rebuild3.log (full gate driver
  output), transform-en.log, measure1.log, precheck-en.log, boxtitle-en.log,
  keycheck-150.json, keycheck.log, freeze-direct.json, freeze-direct.log

## Note on the web PDF name
The assignment brief said the en web PDF is `.web.pdf` (with a dot). On-disk
evidence says otherwise: the previous round's file is
`Die-Lucerna-VOL4-de-en-web.pdf` (hyphen), the FANOUT-REPORT-de.md records the
same name, and `build_edition.py` writes `-web.pdf` for every language. This
rebuild therefore kept `-web.pdf`, per the brief's own "follow the previous
round's file name" rule. Flagged to the coordinator, not silently "fixed".
