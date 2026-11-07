# WEEKLY-KIT — Lucerna Japanese × English (JA×EN), VOL.3, W46, 9–15 Nov 2026

Slug: `2026-w46-ja-en`. Target language: Japanese (articles frozen
byte-identical from the W46 JA core). Reader language: English (the
entire explanation layer). Source: the pristine W46 core build
`hidden_files/weekly-report-w46-ja-build/` (never modified); this
edition was produced by `transform.py` in
`hidden_files/weekly-report-w46-ja-en-build/` (exact-literal
replacements only; re-runnable: transform → run.py → render.py).

## §1 Pairing badge and footers

- Masthead geometry (task + tools/README lesson 20): wordmark baseline
  y=262 (core position, kept), subtitle y=316, badge inserted at
  (975,356) 19pt BRICK `#a4553a`, strapline y=390, double rules 406/413,
  dark band y=424.
- Badge: `TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`.
- Footer every page: `Lucerna · JAPANESE WEEKLY VOL.3 · Japanese text · English explanations`; page line `Page N of 8`.
- Top strip middle segment: `Weekly` (replacing the core's Chinese).
- Gloss prefix: `Note — `. P8 separators: `— Page N —`.
- Registry type names: fill-in / multiple choice / cloze / matching /
  sentence building / true/false / translation / writing. Instructions:
  Fill in / Build a sentence / Translate / Writing / True or false? /
  Match words to meanings.
- P1 dark-band right lines (English, short form): `Sunday is
  Shichi-Go-San` / `The leaf season moves south · See page 6`.

## §2 What changed vs the core

Only the explanation layer: glosses, notes, answer notes, furniture
halves, band subtitles, the P2 season-word glosses, the P7 error-clinic
notes, frame breakdown, readers'-corner disclosure (ONE English
disclosure replacing both the Japanese and Chinese lines, per the W45
coordinator ruling: it states the letter is an editor's sample, no real
letters or best Page 8 compositions had arrived by the deadline, both
will appear in VOL.4, and invites letters in Japanese), phrase
translations + page tags (`p. N`), teaser head, and the P8 E-zone
re-aiming: items 137–138 keep their Japanese stems with English keys;
items 139–140 have English stems with the Japanese keys byte-identical
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
  P7 teaser ends y=2497.6 (< 2540); P8 keys flow ends y=2473 (< 2540).
- Occlusion audit: 0 flags (`hidden_files/w46/ja-en-occlusion.json`;
  selftest OK). One LINEX flag found in round 1 (P1 word-of-week gloss
  wrapped across the row-B rule); fixed by shortening the gloss in
  `transform.py`, re-rendered, 0 flags.
- P8 compare: CLEAN, 150/150 noted, keydiff=[137, 138] — exactly the
  two re-aimed E-zone keys (expected; see §2).
  (`hidden_files/w46/ja-en-p8compare.json`).
- Freeze diff --strict-cjk: 0 added CJK characters
  (`hidden_files/w46/ja-en-freeze.json`). Round 1 showed 12 surplus CJK
  characters, all Japanese headwords echoed inside English notes
  (ポッキー, 千歳飴, 4連勝) where the core notes used the Simplified
  headword forms; the three note renderings were changed to drop the
  echo (the headword already stands as the item key), re-rendered, 0.
- Web PDF: `Lucerna-VOL3-EN-web.pdf`, 2,318,038 bytes (< 7 MB),
  46,148 pdftotext bytes, identical to the print PDF text. Print PDF
  kept: `Lucerna-VOL3-EN.pdf` (27,837,882 bytes).
- Visual pass: P1, P7, P8 cards checked (badge geometry, disclosure,
  keys fit); P2–P6 follow the core layout with the English layer and
  passed the occlusion audit. Kinsoku: the Japanese body text is the
  core's (0 line-start hits); English text has no kinsoku application.
- `.text.md` exported from the builder SVG manuscript with
  `hidden_files/w46/make_textmd.py` (never from PDF).
- Proofread status: builder-complete; finalisation requires the
  independent proofread per SOP §8.4. This KIT does not declare the
  edition final. Nothing posted to Discord, nothing sent to chat,
  weekly repo untouched.

## §5 Reproduction

```
cd hidden_files/weekly-report-w46-ja-en-build
tools/venv/bin/python transform.py   # from the pristine W46 core build
tools/venv/bin/python run.py         # one process, shared registry
tools/venv/bin/python render.py      # cards + print PDF
tools/venv/bin/python webpdf.py <svg dir> <web pdf>   # from tools/
```

## §6 Fix history

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
  rest verbatim. Before tail: `150 exercises for readers learning Japanese through real Japanese news.` After tail:
  `150 exercises built from this week's topics.` (Full before/after in
  `hidden_files/w46/ja-fix/abstracts-before-after.txt`.)
- Re-gate (final artifacts): freeze diff exit 0, 0 added CJK; p8 compare CLEAN
  150/150, keydiff [137, 138]; occlusion 0 flags; kinsoku scan
  (proofreader's definitions) start 0 / end 0 / orphan 0; counts 150
  (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38), stems
  and keys 1–150 complete, P6 bars 1020/780/720/480 with all labels
  + practice-data label, P7 phrases 2× verbatim, keys-flow end-y
  2532.0; web PDF 2,318,036 bytes (< 7 MB), 46,148 pdftotext bytes,
  byte-identical to the print PDF (27,837,879 bytes); text.md 45,541 bytes.
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
  every stem piece. Source: regenerated by this edition's `transform.py` from the fixed core (no transform-table edit); this build's `content34.py:95` carries the new key with the unchanged EN note.
  Before (P8 key 42): `42. 熊手を買います。 — Buying a kumade at Tori-no-ichi`
  After (P8 key 42): `42. 酉の市で熊手を買います。 — Buying a kumade at Tori-no-ichi`
  The reader-language note is UNCHANGED. The P3 stem is unchanged.
  No SVG/PDF was hand-edited; no other string was reworded.
  Fit: single line, width 407.9 of 434 (slack 26.1), y unchanged 1428.984.
- Change isolation: SVG text-multiset diff vs the pre-fix snapshot
  shows exactly one changed text in this edition (the key-42 line
  );
  hash check over the 132 edition files shows only the P8 SVG, both
  PDFs, and the .text.md changed in this edition (P1–P7 SVGs and
  ABSTRACT.txt byte-identical). Round 1 fixes survive (kinsoku 0/0/0,
  abstracts unchanged, zh-tw conversions intact where applicable).
- Re-gate (final artifacts): freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2); occlusion audit 0 flags
  (synthetic selftest passed); kinsoku scan start 0 / end 0 / orphan 0;
  counts 150 (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38),
  stems and keys 1–150 complete, sibling 造句 keys unchanged and
  complete, P6 bars 480/720/780/1020 with all labels + practice-data
  label, P7 phrases 2× verbatim, keys-flow end-y 2532.0;
  web PDF 2,318,038 bytes (< 7 MB), 46,160 pdftotext bytes, byte-identical to the print PDF (27,837,881 bytes); text.md 45,553 bytes. P8 card visually checked at full frame: key 42
  correct, no overflow, overlap, or tofu.
