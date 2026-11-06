# WEEKLY-KIT — Lucerna Japanese × German (JA×DE), VOL.3, W46, 9–15 Nov 2026

Slug: `2026-w46-ja-de`. Target language: Japanese (articles frozen
byte-identical from the W46 JA core). Reader language: Deutsch (the
entire explanation layer). Source: the pristine W46 core build
`hidden_files/weekly-report-w46-ja-build/` (never modified); this
edition was produced by `transform.py   # from the pristine W46 core build` in
`hidden_files/weekly-report-w46-ja-de-build/` (exact-literal
replacements only; re-runnable).

## §1 Pairing badge and footers

- Masthead geometry (task + tools/README lesson 20): wordmark baseline
  y=262 (core position, kept), subtitle y=316, badge inserted at
  (975,356) 19pt BRICK `#a4553a`, strapline y=390, double rules 406/413,
  dark band y=424.
- Badge: `JAPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`.
- Footer every page: `Lucerna · JAPANISCHE WOCHENZEITUNG VOL.3 · TEXT AUF JAPANISCH · ERKLÄRUNGEN AUF DEUTSCH`; page line `Seite N von 8`.
- Top strip middle segment: `Jede Woche` (replacing the core's Chinese).
- Gloss prefix: `Anm. — `. P8 separators: `— Seite N —`.
- Registry type names: Satz bilden / Übersetzen / Schreiben / Richtig/Falsch / Ausfüllen / Wörter zuordnen; Lückentext / Multiple Choice / Ausfüllen / Zuordnen / Satzbau / Richtig/Falsch / Übersetzen / Schreiben.
- P1 dark-band right lines (Deutsch, short form): `Sonntag ist Shichi-Go-San` /
  `Die Laubzeit zieht nach Süden · Siehe Seite 6`.

## §2 What changed vs the core

Only the explanation layer: glosses, notes, answer notes, furniture
halves, band subtitles, the P2 season-word glosses, the P7 error-clinic
notes, frame breakdown, readers'-corner disclosure (ONE Deutsch
disclosure replacing both the Japanese and Chinese lines, per the W45
coordinator ruling: "Beispiel der Redaktion, kein echter Brief. Bis zum Redaktionsschluss trafen keine echten Briefe und keine besten Aufsätze ein; beides erscheint in VOL.4. Schickt uns euren Brief auf Japanisch — ausgewählte Briefe werden in VOL.4 abgedruckt!"), phrase
translations + page tags, teaser head, and the P8 E-zone re-aiming:
items 137–138 keep their Japanese stems with Deutsch keys;
items 139–140 have Deutsch stems with the Japanese keys byte-identical
to the core. All Japanese article/stem/option/letter/figure strings are
frozen; all facts and sources are the core's (§3 of the core KIT).

## §3 Content and counts

Same 8 pages and 150 exercises as the core (A2 46 · B1 75 · B2 29;
by page 10/18/18/18/18/18/12/38). P8 model text 154 characters.
Images: same 3 reused PD/CC0 images as the core (maple P1, Hiroshige
III print P3, stadium P4); credits in the core build's
`assets/CREDITS.md`.

## §4 Gates (recorded in hidden_files/w46/ja-gates.log)

- Builder self-check: no FLOW OVERFLOW / HEAD TOO WIDE warnings.
  P7 teaser ends y=2526.6 (< 2540); P8 keys-flow last baseline
  y=2535.01 (< 2540).
- Occlusion audit: 0 flags (`hidden_files/w46/ja-de-occlusion.json`;
  selftest OK).
- P8 compare: CLEAN, 150/150 noted, keydiff=[137, 138] — exactly the re-aimed E-zone keys (expected;
  see §2). (`hidden_files/w46/ja-de-p8compare.json`).
- Freeze diff --strict-cjk: 0 added CJK characters
  (`hidden_files/w46/ja-de-freeze.json`).
- Web PDF: `Lucerna-VOL3-DE-web.pdf`, 2,366,003 bytes (< 7 MB),
  46,990 pdftotext bytes, identical to the print PDF text. Print PDF
  kept: `Lucerna-VOL3-DE.pdf` (29,499,997 bytes).
- Visual pass: P1 card checked (badge geometry, gloss, numbers box);
  P7/P8 cards checked for this edition's risk areas (disclosure,
  keys fit). Kinsoku: the Japanese body text is the core's (0 line-start
  hits).
- `.text.md` exported from the builder SVG manuscript with
  `hidden_files/w46/make_textmd.py` (never from PDF).
- Proofread status: builder-complete; finalisation requires the
  independent proofread per SOP §8.4. This KIT does not declare the
  edition final. Nothing posted to Discord, nothing sent to chat,
  weekly repo untouched.

## §5 Reproduction

```
cd hidden_files/weekly-report-w46-ja-de-build
tools/venv/bin/python transform.py   # from the pristine W46 core build
tools/venv/bin/python run.py         # one process, shared registry
tools/venv/bin/python render.py      # cards + print PDF
tools/venv/bin/python webpdf.py <svg dir> <web pdf>   # from tools/
```

## §6 Fix history

Round history: the P8 keys flow overflowed at 13.3pt (German notes
  run long); fixed with the 12.9pt / lh 1.13 keys-font patch (map EXTRA,
  applied before the separator-text entry in content8.py), plus note
  shortenings, the P4 title "Bilanz", and the P1 footnote fix. A stale
  P7 SVG (standalone content7.py debug run at 14:23, registry numbers
  1–12 instead of 101–112) was found during web-PDF text verification
  this session; the edition was rebuilt cleanly through the full
  pipeline (gen → transform → run.py → render.py), re-gated on the
  final SVGs, and the web PDF + text.md were regenerated. The print PDF
  (29,499,997 bytes, identical size to the good 14:11 render) was
  never affected.

Fix record — Round 1 proofread defects (fix worker, 2026-11-02/03).
Round 1 verdict: FAIL on inherited D-CORE-01 + D-CORE-02. Both fixed
at the source in the core build / this edition's ABSTRACT.txt; this
edition was fully re-rendered through the pipeline in §5 and re-gated
on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix/`). Round 2 independent proofread still
required.

- D-CORE-01: core `svglib.py` `wrap()` gained a NO_END kinsoku block
  (opening brackets `（「『〔【《〈([` never end a line); md5
  d73e23b365676c3618d7e060b835eb4d →
  74177544422fe677639d769cd80499fb, and `CANON_SVGLIB_MD5` in this
  edition's `transform.py` was updated to the new value. The §5
  "pristine core build" wording now refers to the pre-fix state; the
  current build carries the NO_END fix. P1 item 8 and P3 item 32 now
  keep `（月）` / `（土）` intact on one line (see core KIT §11 for the
  line-split quotes); no other text moved.
- D-CORE-02: `ABSTRACT.txt` closing rewritten to practice framing,
  rest verbatim. Before tail: `150 Übungen für alle, die Japanisch durch echte japanische Nachrichten lernen.` After tail:
  `150 Übungen zu den Themen dieser Woche.` (Full before/after in
  `hidden_files/w46/ja-fix/abstracts-before-after.txt`.)
- Re-gate (final artifacts): freeze diff exit 0, 0 added CJK; p8 compare CLEAN
  150/150, keydiff [137, 138]; occlusion 0 flags; kinsoku scan
  (proofreader's definitions) start 0 / end 0 / orphan 0; counts 150
  (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38), stems
  and keys 1–150 complete, P6 bars 1020/780/720/480 with all labels
  + practice-data label, P7 phrases 2× verbatim, keys-flow end-y
  2535.0; web PDF 2,365,997 bytes (< 7 MB), 46,990 pdftotext bytes,
  byte-identical to the print PDF (29,499,992 bytes); text.md 46,348 bytes.
  P1 and P3 cards visually checked at full frame: both rewraps
  correct, no overflow/overlap.

Fix record — Round 3 proofread defect D-KEY-42 (fix worker, 2026-11-03).
Round 2 verdict: FAIL on D-KEY-42 only (all Round 1 defects confirmed
fixed). Fix applied at the source in the core build and propagated by
regeneration; this edition was fully re-rendered through the pipeline
in §5 and re-gated on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix-round3/`). Round 3 independent proofread
still required.

- D-KEY-42 (P8 key 42 omits a stem piece, BLOCKING, all 11 editions):
  P3 stem item 42 is `酉の市で / 熊手を / 買います → ___` (造句).
  The printed P8 key omitted the location piece `酉の市で`, while
  all 7 sibling 造句 keys (39, 40, 41, 133, 134, 135, 136) include
  every stem piece. Source: regenerated by this edition's `transform.py` from the fixed core (no transform-table edit); this build's `content34.py:95` carries the new key with the unchanged DE note.
  Before (P8 key 42): `42. 熊手を買います。 — Einen Kumade auf dem Tori-no-ichi kaufen`
  After (P8 key 42): `42. 酉の市で熊手を買います。 — Einen Kumade auf dem Tori-no-ichi kaufen`
  The reader-language note is UNCHANGED. The P3 stem is unchanged.
  No SVG/PDF was hand-edited; no other string was reworded.
  Fit: WRAPS to two lines: full width 466.1 exceeds the 434 column, so wrap() splits after `Tori-no-ichi` (line 1 width 419.0, line 2 `kaufen` at y=1383.5); line-1 y unchanged 1368.877, keys-flow end-y unchanged 2535.0, kinsoku/orphan scan 0. The wrap breaks at a space before `kaufen`, no bracket/punctuation split; the same edition's P8 already wraps keys 68 (`Schrein`) and 97 (`(Donnerstag)`) onto single-word second lines. Flagged for the Round 3 proofreader; no note or font was changed to avoid it, per the specified fix..
- Change isolation: SVG text-multiset diff vs the pre-fix snapshot
  shows exactly one changed text in this edition (the key-42 line
  plus its `kaufen` wrap continuation);
  hash check over the 132 edition files shows only the P8 SVG, both
  PDFs, and the .text.md changed in this edition (P1–P7 SVGs and
  ABSTRACT.txt byte-identical). Round 1 fixes survive (kinsoku 0/0/0,
  abstracts unchanged, zh-tw conversions intact where applicable).
- Re-gate (final artifacts): freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2); occlusion audit 0 flags
  (synthetic selftest passed); kinsoku scan start 0 / end 0 / orphan 0;
  counts 150 (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38),
  stems and keys 1–150 complete, sibling 造句 keys unchanged and
  complete, P6 bars 480/720/780/1020 with all labels + practice-data
  label, P7 phrases 2× verbatim, keys-flow end-y 2535.0;
  web PDF 2,366,010 bytes (< 7 MB), 47,006 pdftotext bytes, byte-identical to the print PDF (29,500,005 bytes); text.md 46,360 bytes. P8 card visually checked at full frame: key 42
  correct, no overflow, overlap, or tofu.
