# de-pt per-edition record (rebuild-A, rebuild 3, 2026-11-11)

## Conclusion
de-pt COMPLETE. ALL GATES PASS (rebuild 3, second attempt, 2026-11-11 08:41 UTC).
8-page visual proofread zero findings. 150-question key check 149/150 exact
(Q150 = extractor truncation, expected). P8 chips 35, whole-issue chips 141.
Independent proofread pending (coordinator to assign).

## Why this rebuild
core-de was re-finalised as build15 (proof5 (a) zero findings, 2026-11-11 08:02 UTC)
with exactly one content change: Q34 stem in `content34.py:105`
`"Am Montag öffnen in Köln die ersten ___."` →
`"Am Montag öffnet in Köln der erste ___."` (key `Weihnachtsmarkt` unchanged).
The previous de-pt (rebuild 2) carried the old plural stem, so the edition was
deleted and re-transformed from the new core. No other content was intentionally
changed: pt needed no box-title fix this round (boxtitle.py 7/7 as-is), and the
rebuild-2 P8 battery-A head fix ("Preenchimento") is preserved in the copied
tr_pt.py.

## First build attempt failed (RC 120, render killed mid-run) — retried clean
- First `build_edition.py pt` run (08:31–08:32 UTC): run.py completed
  (P8 saved, TOTAL 150) but the driver died during render.py — only cards
  p1–p3 were written (p4–p8 cards in the dir were stale rebuild-2 files),
  no print PDF, driver log 0 bytes, exit code 120. The machine was under heavy
  parallel load at the time (other agents' run.py/render.py/webpdf work in
  other families, ~184 MB free RAM). No gate output was produced, so nothing
  was half-verified; the failure was a killed process, not a content defect.
- Retry (08:37–08:41 UTC, `python -u` so the log streams): ALL GATES PASS.
  The retry re-ran the whole driver from scratch (run.py → render.py → …);
  nothing from the failed attempt was reused except the already-transformed
  sources (identical — transform RC was 0, measure 24/24).
- Both logs kept: `rebuild3.log` is the retry's full gate output (copied from
  `rebuild3-retry.log`); the failed attempt's empty log was overwritten by the
  copy — its evidence (0-byte log, RC 120, cards p1–p3 only at 08:31–08:32)
  is recorded here and in this session's report, not in a file.

## Deliverables (in production/2026-w47/2026-w47-de-pt/)
- 8 SVG: p1-front, p2-leben, p3-kultur, p4-sport, p5-jugend, p6-vertiefung,
  p7-sprache, p8-uebungen
- Print PDF: Die-Lucerna-VOL4-de-pt.pdf — 10,968,908 bytes,
  sha256 33e2dc7d5fe62549c605a622d61d59ade0dd5fa4e54aa3a7901dbbc486d260aa
- Web PDF: Die-Lucerna-VOL4-de-pt-web.pdf — 1,599,432 bytes,
  sha256 a251196e6d411c09f3b4ccef54876da6fcacd96fd899198154b9836118b877bb
- Text: 2026-w47-de-pt.text.md — 49,812 bytes, 47,947 chars, 591 entries, 150 ex.,
  sha256 4257920750577d5ad5f0e58ca8959dcb8ef4779cafd1a932a170405c24790dbf
- ABSTRACT.txt: one line, Portuguese, 400 bytes, 0 ASCII double quotes
- WEEKLY-KIT.md: restored from the rebuild-2 KIT and updated to rebuild-3 values
  (source build15, new gate numbers, Q34 + webpdf notes).

## Q34 stem verification (old stem must be 0, new stem 1x, everywhere)
- `content34.py` source: new 1, old 0
- `2026-w47-de-pt.text.md`: new 1, old 0
- `svg/p3-kultur.svg`: new 1, old 0
- print PDF text layer (pdftotext, whitespace-normalised): new 1, old 0
- web PDF text layer (same): new 1, old 0
- P3 visual: Q34 renders as "Am Montag öffnet in Köln der erste ___." (see目视 P3).

## Gates (rebuild3.log = retry; full gate logs in this dir)
- run.py exit 0; 0 FLOW OVERFLOW; 0 HEAD TOO WIDE; TOTAL 150
- measure.py 24/24 PASS, 0 FAIL (measure1.log)
- precheck.py 24/24 PASS, 0 FAIL; boxtitle.py 7/7 (no change needed)
- verify.py: TOTAL 150, numbering continuous, SVGs byte-identical after re-run,
  SOP 1.1 style audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags (selftest OK)
- p8 extract 150/150; compare CLEAN; keydiff [137, 138, 139, 150] (expected)
- freeze diff exit 0; added CJK 7 (all U+3000, 1 per page P2–P8)
- print/web text: default word multiset identical (50,684B / 50,684B);
  raw normalised identical (49,500B each)
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
  Only P3 sha differs from the rebuild-2 reference (093cf378 → fc88f676): the
  frozen set still has 195 strings, but the Q34 stem string itself changed
  (plural → singular), so its hash changed. All other pages byte-identical to
  the reference. This is the expected Q34 fingerprint, identical to de-en/de-fr/de-es/de-it.

## 150-question key check (keycheck-150.json)
P8-SVG-extracted keys vs REG from the edition's own sources: 149/150 exact.
Only Q150 differs: extractor truncates REG key "Tarefa livre — segue os pontos
do quadro de escrita" to "Tarefa livre" (expected; Q150 is the open writing
task, already in the keydiff set). REG by page {1:10, 2:18, 3:18, 4:18, 5:18,
6:18, 7:12, 8:38}; levels A2 69 / B1 67 / B2 14.

## Flow ends (identical to rebuild 2)
P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523, P2-feature 993,
P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315, P5-main 996,
P5-ex 2441 (= core), P6-main 747, P6-ex 2523, P7-A2 1278 / B1 1342 / B2 1306,
P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103), P8 image height 140;
P3 col3 1643.19 (hline 1668, 25px clear), P4 col3 1156.02 (edge-touch, like core),
P5 col3 image 1732.93 (hline 1744, 11px), P7 col3 1547.5 (0.5px clear of the
1548 rule — edge-touch, same as rebuild 2: the P7 col3 content is unchanged,
freeze counts identical, and the visual shows the last toolbox entry inside
its box with LESERBRIEFE below, no overlap; occlusion 0 flags).

## Web PDF +40 KB vs rebuild 2 — explained (tool change mid-session, NOT content)
- Rebuild-2 web PDF: 1,559,382 B. Rebuild-3 web PDF: 1,599,432 B (+40,050 B).
  The print PDF moved only +6 B and text.md −1 B, so the jump is not content.
- Cause: `tools/webpdf.py` has an UNCOMMITTED working-tree change (made by the
  scratch-webpdf-patch1 agent between my de-it build 08:29 and the pt build
  08:31): `fc_match` now queries `:weight=200` / `:weight=100` instead of
  `:style=Bold`. With the new query, `fc-match 'Newsreader:weight=200'`
  resolves to `Newsreader-SemiBold.ttf` (a different file from Regular), so
  `build_subsets` no longer skips the Bold subset — the pt web PDF embeds a
  Newsreader-Bold subset on all 8 pages (log: `font LucernaNewsreader-Bold:
  24868 bytes`). The en/fr/es/it web PDFs, built 08:15–08:29 with the
  pre-patch code, embed NO Newsreader-Bold at all (verified with pdffonts on
  all five web PDFs). The SVGs are identical in font usage across languages
  (1 Newsreader-700 element per page, 432 Noto Sans 700 each), so this is
  purely the tool version at build time.
- The pt web PDF is valid: 8 pages, real text layer, print/web text multiset
  identical (50,684B each), raw normalised identical (49,500B each), < 7 MB.
  The Bold subset arguably renders headlines more correctly than the
  Bold-less siblings. NOT rebuilt with the old code and the four siblings
  NOT rebuilt with the new code: the patch is still uncommitted work by
  another agent and may change again — rebuilding now would churn. Flagged
  to the coordinator: once the webpdf patch settles, the four sibling web
  PDFs can be rebuilt with the settled tool for family consistency.
- Note the same `webpdf.py` diff also explains nothing else in this rebuild:
  all other gate numbers are in line with the siblings.

## Visual proofread (8 pages, print PDF @100dpi, renders /tmp/pt3-proof/p-*.png)
Zero findings.
- P1: masthead, headline, ZAHLEN box in column, JETZT ÜBEN, FRAGEN sidebar,
  IN DIESER AUSGABE, word of the week, football photo + caption, KURZ & GUT,
  BLITZQUIZ, footer clean.
- P2: article, Note box, four side boxes, RECHNEN table, exercises A–D clean.
  "DIE STILLE WOCHE Tranquila" inside its box.
- P3: article, Note box, 1930 market painting + caption, WEIHNACHTSWÖRTER box
  ("Palavras" inside), UND SIE?, DER TIPP ("Conselho da redação" inside),
  exercises A–D clean. Q34 new singular stem visible.
- P4: article, Note box, header photo + caption, UND SIE? box inside, 9-row
  results table, exercises A–D clean. O1 preserved as ruled.
- P5: article, Note box, ADVENTSKALENDER/ADVENTSWÖRTER ("Advento" inside),
  UND SIE?, 1903 calendar image + caption, week-plan table, exercises A–D clean.
- P6: article, Note box, DIE ZAHLEN, DIE STILLE WOCHE, DIE DEBATTE, poll bars
  (44/33/23, labels clear), ÜBUNGSDATEN single line, exercises A–D clean.
- P7: three lessons (A2/B1/B2), toolbox (6 entries, last inside the box),
  LESERBRIEFE ("Cartas dos leitores" inside, with Portuguese disclosure),
  NOCH EIN WORT, reading-room photo + caption, Sätze der Woche 8,
  FEHLERKLINIK 4 groups, VOL.5 band clean.
- P8: A cloze ("Preenchimento" — rebuild-2 fix preserved) / B Quiz / C reading /
  D sentence building / E translation (137–140) / F matching / G dialogue
  (5 badges) / H writing (MUSTER 84 words) / ANTWORTEN 8 groups all complete,
  image in place, keys end 2457 (103px above the bottom).

## Core source check
- core-de build15 verified at rebuild start (see de-en record): print
  22,965,197 B sha 49beffc4…; web 2,044,855 B sha 9b63b413…; text 49,798 B
  sha 0952bc51…. New Q34 stem 1x in core `content34.py:105`; old stem 0x.

## Files in this dir
- build.log, render.log, webpdf.log, verify.log, occlusion.log, occlusion.json,
  p8extract.log, p8extract.json, p8compare.log, p8compare.json, freeze.log,
  freeze.json, export.log, print.txt, web.txt, rebuild3.log (retry's full gate
  driver output), rebuild3-retry.log (same, original name), transform-pt.log,
  measure1.log, precheck-pt.log, boxtitle-pt.log, keycheck-150.json,
  keycheck.log, freeze-direct.json, freeze-direct.log
