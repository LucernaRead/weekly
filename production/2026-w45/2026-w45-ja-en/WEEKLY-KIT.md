# WEEKLY-KIT — Japanese Weekly VOL.2 · JA × EN edition (Japanese text · English explanations)

The English-explanations edition of the W45 Japanese Weekly VOL.2: the same
issue as the finalized core edition (Japanese text + Chinese explanations),
with the whole explanation apparatus rewritten in English for
English-speaking readers. Japanese content — articles, exercise stems and
options, quoted sentences, the text being taught — is unchanged, element
for element, except for the single coordinator-ruled readers'-corner change
documented in §6.

- Week: Mon 2 – Sun 8 Nov 2026 (W45, VOL.2) · 8 pages · page size 1950×2700
- Files: `svg/` (8 SVG), `cards/` (8 PNG 1950×2700),
  `Lucerna-VOL2-EN.pdf` (print, 27,138,307 B),
  `Lucerna-VOL2-EN-web.pdf` (web, 3,038,903 B — under the ~10 MB server limit)
- Core edition (frozen, untouched): `files/weekly-report-w45-ja-core/`; core build:
  `hidden_files/weekly-report-w45-ja-build/`. This edition's build:
  `hidden_files/weekly-report-w45-ja-en-build/` (transform.py + run.py +
  render.py + per-round sha256 baselines + gate outputs). The core was never
  modified — final check: all 8 core SVGs still byte-identical to the
  baseline reproduction (hash-list md5 8950594a4b0116c2addbfe1c07118b4a,
  identical before and after this build).
- Status: FIX ROUND 5 COMPLETE (blocking item B-1 fixed, §8). This is NOT
  a finalization: the fix changed rendered output, so per SOP §8.4 a
  fresh full independent proofread is still required before any
  delivery. No Discord post, no chat card/PDF dump, no cron, no
  weekly-repo touch was made by this build.

## 1. Pairing badge and footers (W43 JA × EN shipped precedent, measured)

- P1 masthead carries the pairing line, bold olive, centered, 19 pt, at
  y=356, exactly as in the shipped W43 JA × EN SVG:
  **TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS**
  Masthead name stays "Lucerna", no article — Japanese is an article-less
  language. Masthead geometry copied whole from W43 JA × EN: wordmark
  baseline 262→248, edition line 330→316, badge inserted at 356, tagline
  372→390, rules 392/401→406/413, dark band stays at y=424.
- Top strip: "VOL. 2 · 第2号" (core, frozen); middle line "毎週、日本語で ·
  Weekly · 日本人が読んでいる日本語を読む" (the core's Chinese middle
  segment replaced by "Weekly", per W43).
- P1 dark band, right side (English, short form per W43 pattern):
  "Tuesday is Culture Day" / "After the holiday, the autumn-leaf weekend
  arrives · See page 3".
- Every page footer: left
  `Lucerna · JAPANESE WEEKLY VOL.2 · Japanese text · English explanations`,
  right `Page n of 8`.
- In-text gloss lines use the prefix `Note — ` (was the core's Chinese
  prefix). Band subtitles follow the W43 pattern "レベル … · <Japanese
  theme> · <English theme>".
- Section furniture (English halves, W43 wording): "Top story", "Week in
  numbers", "Practice now", "In this issue", "Word of the week",
  "News in brief", "Quick quiz", "Your turn", "Words of the season",
  "Page N exercises", "Answers on page 8 · Levels are mixed — find your
  number", "Reading the chart", "Practice data", "Test and answers",
  "Frame of the week", "Readers' corner", "Phrases of the week (verbatim
  from this issue)", "Next issue (VOL.3)", "Answers — grouped by page; just
  find your number", "A short English note with every answer · ✓ = the
  model-text item", separators "— Page N —".
- Registry type names (W43 set): fill-in, multiple choice, sentence
  building, true/false, matching, cloze, translation, writing.
  Instructions: "Fill in", "Build a sentence", "True or false?", "Match
  words to meanings", "Match events to places and dates", "Translate",
  "Writing".

## 2. Counts (measured three ways: registry, freeze diff, independent SVG count)

- Exercises: **150** — A2 46 · B1 75 · B2 29; per page
  10/18/18/18/18/18/12/38. Independent SVG count (level chips + number
  labels in document order, match ranges expanded): P1–P7 = 112
  (A2 37 / B1 53 / B2 22, numbers continuous 1–112); P8 = 38
  (A2 9 / B1 22 / B2 7, numbers 113–150). Totals agree: 150, A2 46, B1 75,
  B2 29. No FLOW OVERFLOW, no HEAD TOO WIDE in any build round.
- Page 8 writing model 『私の11月の週末』 = **167 characters** (counted
  programmatically by the build, inside the printed 150–200 range),
  identical to the core.
- Gloss items (rendered gloss() strings split on ·, counted item by item):
  feature pages core 39 = edition 39 — P1 4, P2 9, P3 8, P4 7, P5 7, P6 4.
  P7 column bridges core 9 = edition 9 (A2 3 / B1 3 / B2 3), Japanese
  headwords byte-identical, glosses English.
- P7 phrases of the week: all 8 verbatim quotes occur exactly 2× in the
  full-issue blank-stripped text concatenation (quote in its article +
  quote in the P7 list). Source-page tags match the core's mapping
  (core 第N面 → edition p.N): p.1, p.1, p.2, p.2, p.3, p.4, p.5, p.6.

## 3. What changed vs the core — and what did not

Changed (apparatus only): every gloss/note, exercise instruction,
section-header and band-subtitle English half, the three "Your turn"
reader lines, the P2 season-word card glosses, the P7 error-clinic notes,
frame note, the P7 phrase translations, the answers header, the keys'
group headers, the registry type names, and **all 150 answer notes** —
rewritten as full, natural English. CORRECTION (fix round 5, §8): this
claim was false as written at round 4 — independent proofread found
P8 #37's note still Chinese (`37. 8 — 工艺展到11月8日`); it was
Englished only in fix round 5, after which all 150 notes are English
(verified: post-fix P8-vs-core full-line comparison finds 0 identical
lines). P1 trend-box English lines were
shortened in fix round 3 to fit their fixed slots (see §8).

Re-aimed translation items (E zone, the only key changes; W43 JA × EN
pattern — bodies re-aimed at English, Japanese keys byte-identical):
- #137 key (JA→EN): `Culture Day is November 3.`
- #138 key (JA→EN): `If you drop litter, the fine is 2,000 yen.`
- #139 body now an English prompt (`Reading Week starts on October 27.`);
  its Japanese key is byte-identical to the core.
- #140 body now an English prompt
  (`I want to go to Kobe to see the autumn-leaf illuminations.`); its
  Japanese key is byte-identical to the core.
- #150's registry line reads `(open task — model text below)` (its note
  is `Model text in section H on this page (167 characters)`); the item
  itself, an open writing task, is unchanged.

Not changed: every Japanese article, stem, option, letter and figure; all
other keys; the P4 G3–G7 schedule-only treatment with the VOL.3 deferral
note on the page; the P6 practice chart (38/27/21/14 = 100, labelled
practice data); the P8 38-item structure; です・ます style; full-form
weekday spellings (土よう日, 日よう日).

## 4. Images (payload-verified per page vs the core)

- P1 maple (Poliphilo — CC0, Wikimedia Commons), P3 Hiroshige III print
  (歌川広重（三代）, 1876, public domain, Wikimedia Commons), P4 stadium
  (Syced — CC0, Wikimedia Commons), P5 pumpkin (Petr Kratochvil — public
  domain, Wikimedia Commons). Base64 payload hashes per page are identical
  to the core's (P1 92f3f41c7cec, P3 76f4abb34efc, P4 ab8d113ff083,
  P5 f954d75303c8 — first 12 hex chars of sha256). Credits on the pages
  match the core's, character for character.

## 5. Topics and sources (inherited from the core, unchanged)

Culture Day Tue Nov 3 + the Nov 7–8 autumn-leaf peak weekend (Naruko
Gorge peak; Kobe Nunobiki Herb Garden illuminations from Sat Nov 7) +
yuru eating trend (Ajinomoto, Oct 21) + Reading Week in progress (ends
Nov 9) + Ritto Sat Nov 7; Japan Series G1/G2 verified reports (G3–G7
schedule only, results deferred to VOL.3 on the page); Halloween Oct 31
as a just-passed report; JMA Oct 20 three-month forecast; note.com
Oct 22 roundup explicitly marked as not a survey; practice chart data
explicitly marked as practice data.

## 6. P7 structure (measured from the core) and the readers'-corner ruling

Core P7, verified by reading the core build: A2 column 本と読書のことば
(Reading Week) / B1 column 紅葉のことば (autumn leaves) / B2 column
数字を読む (reading numbers) + error clinic (4 items: past tense after
昨日, こと nominalization, か所 for places, で for place of action) +
frame box 『ゆるく整える』 breakdown + readers' corner + VOL.3 teaser.
Column definitions and quote originals are verbatim; only glosses and
explanations are localized to English. Definition-sentence localization
would be a blocking failure — none occurred: P7 Japanese definition
sentences are byte-identical to the core's.

Readers' corner (coordinator ruling, executed as ordered): no reader,
letter, name or quotation was invented. The core's sample letter is kept
verbatim. The core's Chinese disclosure is the core reader-native layer
and was replaced by an English disclosure stating the 3 facts (no real
letters received; no best P8 compositions received; sample stands and
both will appear in VOL.3) plus an explicit imperative invitation with a
VOL.3 publication promise ("Send us your letter in Japanese — selected
letters will be printed in VOL.3!"). The core's Japanese disclosure line
was NOT kept as the operative disclosure (English readers cannot read
it, which would violate the all-explanations-in-the-reader's-language
rule). The VOL.3 teaser line is a contents preview, not an invitation,
and is not counted as one.

## 7. Mechanical gates (all measured on the FINAL files, round 4)

- Core baseline (tools/freeze.py baseline, scratch repointed copy):
  **8/8 SVGs byte-identical**; shipped core SVGs re-hashed unchanged.
- Frozen-core diff (tools/freeze.py diff --strict-cjk, final):
  added CJK characters **0 on all 8 pages** (P1 1406→1275, P2 1312→1161,
  P3 1172→1051, P4 1263→1169, P5 1247→1132, P6 1186→1101, P7 1676→1308,
  P8 2721→1448 — reductions are the removed Chinese explanation layer).
  (Round-4 figure for P8 was 1454; fix round 5 removed 6 more CJK chars,
  exactly the Chinese note of #37.)
  Added/removed string lists were read in full: removed = Chinese
  explanation strings + the ruled readers'-corner disclosure + page-tag
  furniture; added = English apparatus + Japanese headwords already in
  the core. No frozen Japanese sentence is removed or altered.
- Forbidden bridge word: **0 occurrences** in all SVGs, ABSTRACT.txt and
  this KIT.
- Chinese residue, word-level review: every CJK run in the edition's
  added strings was adjudicated — all are frozen Japanese words or
  Japanese headwords of English glosses. A simplified-only codepoint
  scan flagged only shared kanji in frozen Japanese (全国, 会社, 来週
  forms); zero simplified-only residue.
- Japanese line-start rule (kinsoku NO_START set, all 8 pages): core 0 =
  edition 0 on every page; no inherited line-start flags exist at all.
- P8 (tools/p8.py compare, explicit dual-path form):
  **CLEAN, 150 = 150, missing [] extra []**; P8 notes all English as of
  fix round 5 (§8) — the round-4 wording of this claim was false for
  #37 (see §3 correction); the fix-round-5 re-run is CLEAN with the
  same 21-item keydiff list below.
  Keydiff list [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117,
  118, 137, 138, 140, 146, 147] adjudicated item by item:
  17 are note-only translations (key byte-identical); #5 and #101 are
  parenthesis-branch extraction artifacts — printed keys verified
  byte-for-byte (key 7 and key 27 identical in core and edition, only
  the notes differ); #137 and #138 are the legal E-zone re-aims (§3).
  #139 and #140 keep byte-identical Japanese keys (bodies re-aimed).
  P8 comment set equality holds with no extras.
- Geometry (tools/occlusion_audit.py, selftest green, all 6 classes fire):
  edition **0 flags**, core **0 flags**, NEW vs core **0**.
  Same-baseline ink collisions on furniture bands: 0.
  Right-edge ADVANCE scan (all text elements, advance width, limit
  x=1885.5): 0 violations in edition and core.
  P6 chart-label coverage, baseline-anchored ink method (PIL getbbox,
  anchor ls, bars as later-drawn rects): max coverage **0.000** (gate
  <30%). Chart labels sit fully clear of the bars.
- Frame/box check: box-title ink vs own borders is covered by the audit
  (0 BOXTITLE); the P7 teaser band ends at y=2524.12, inside the 2540
  content limit and 56 px clear of the 2580 footer line.
- Essay: 167 characters, core-identical.
- All 8 cards viewed individually (P1–P8): no overflow, overlap, clipped
  label, or misplaced box found on visual pass.

## 8. Fix rounds (each round's edits went into transform.py first, then a
## single-process re-render; pre-fix sha256 baselines recorded each round)

- Round 1 (baseline): first full build. Counts exact; P7 teaser band
  ended at 2582.12 (past the 2540 content limit, into the footer line)
  because the English readers'-corner disclosure ran longer than the
  core's two disclosure lines.
- Round 2: shortened the English disclosure (all 3 facts + invitation
  kept); teaser band now ends at 2524.12. Only P7 SVG/card and the PDFs
  changed (sha256 diff verified).
- Round 3 (critical): word-level diff review caught substring
  replacement corrupting frozen Japanese — several note strings are
  prefixes of frozen stems/articles (e.g. a note vs its stem minus 。,
  a note inside the P6 chart note). The transform was rewritten to
  argument-scoped note replacement (exact 4th argument of .ex() calls
  and exact match_set notes-list items only; bare substring replacement
  for notes is forbidden and documented in transform.py). Also fixed:
  a P8 note that had kept a leftover weekday suffix, and a proper-name
  note reworded to keep added CJK at 0. Changed files were exactly
  P1/P4/P5/P6/P8 (the corrupted pages) + PDFs; frozen sentences
  re-verified line-identical to the core.
- Round 4 (final): P1 trend box — two English lines overflowed their
  fixed slots (audit: 3 NEW flags). Both lines were shortened with
  PIL-measured widths ("Dates in articles; not exact statistics",
  312.4 px; "These four topics shape this issue.", 293.2 px; box inner
  width 390 px). Only P1 SVG/card and the PDFs changed. Final audit:
  occlusion 0/0/0, strict-CJK 0, P8 CLEAN.
- Round 5 (B-1 fix, independent-proofread blocking item): P8 #37's note
  was still Chinese (`37. 8 — 工艺展到11月8日`, byte-identical to the
  core) while the same fact's #32 was already English. Root cause: the
  bare note string was missing from transform.py NOTES — NOTES held
  only the two near-neighbours, the 传统… note and #32's （周日） note.
  Fix (transform.py only, then single-process re-render): added
  `("工艺展到11月8日", "The exhibition runs to November 8")` to NOTES;
  key `8`, question number and all other notes untouched. Fact check:
  the P3 stem is `展覧会は11月 ___ 日（日）までです。` and 2026-11-08
  is a Sunday, so the English note matches the stem fact.
  Pre-fix baseline: `sha256-fix5-prefix.txt` in the build tree (18
  deliverables + KIT + ABSTRACT + 10 build files; pre-fix print PDF
  a213dcf6357b…c8b, web PDF 394b93996688…a3, P8 SVG 65b63e637613…,
  P8 card 8b28f8e7d8d6…). Changed build files: transform.py
  (005c6a0b… → c858f930…) and regenerated content34.py
  (0570cb3c… → 935c4fe4…) only; all other build files byte-identical.
  Changed deliverables (sha256 diff vs baseline): exactly P8 SVG
  (→ a7433832d190…), P8 card (→ 641e290f07c7…) and the dual PDFs;
  the other 7 pages' SVG + cards are byte-identical. Freeze diff vs
  the round-4 final json confirms the same scope: pages 1–7
  added/removed strings identical; P8 differs by exactly one added
  string (`37. 8 — The exhibition runs to November 8`) and one removed
  string (`37. 8 — 工艺展到11月8日`).
  Re-run gates (full outputs in `build-fix5.log`, `gates-fix5.log`,
  `freeze-diff-fix5.json`, `p8-compare-fix5.json`,
  `occlusion-fix5.json`, `scope-fix5.txt`, `residue-p8-fix5.txt`):
  freeze baseline 8/8; freeze diff --strict-cjk added CJK 0 on all 8
  pages (P8 CJK total 2721→1448); p8.py compare explicit dual-path
  CLEAN 150 = 150, keydiff unchanged
  [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117, 118, 137,
  138, 140, 146, 147]; occlusion selftest green (6/6 classes), edition
  0 flags, core 0 flags, NEW vs core 0; P8 card viewed — #37 line fits
  its column, no overflow/overlap; simplified-only scan true positives
  0 (「艺」 eliminated, 0 occurrences in all 8 SVGs; the only raw
  proof-set hit, P4 「点」, is core-shared frozen Japanese); P8 150
  answer lines vs core: numbers complete, 0 fully identical lines, so
  no remaining line that should have been Englished. Counts unchanged
  (150, A2 46 / B1 75 / B2 29; model text 167 chars).
  KIT-only text edits in this round touched no deliverable other than
  the dual PDFs' own record (§11). NOTE: this KIT correction does NOT
  replace re-proofread — per SOP §8.4 this rendered change requires a
  fresh full independent proofread round before any delivery.

## 9. Reproduction

Build directory: `hidden_files/weekly-report-w45-ja-en-build/`
(transform.py = the single source of the edition build; run.py = the
one-process driver; render.py = cards + PDFs; svglib.py = canonical JA
build, md5 d73e23b365676c3618d7e060b835eb4d, copied verbatim and never
edited).

```bash
cd hidden_files/weekly-report-w45-ja-en-build
../../tools/venv/bin/python transform.py   # core build -> edition build
../../tools/venv/bin/python run.py         # ONE process: content12->34->56->7->8
../../tools/venv/bin/python render.py      # cards + print PDF + web PDF
```

Interpreters (both run.py and render.py): `tools/venv/bin/python`
(Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1, pypdf 6.21.2). System
python3 (PIL 10.2.0, no cairosvg) was NOT used for any render step.
Shared-registry rule honored: content modules run only through the
single driver process, never standalone, never imported inside the core
build directory.

## 10. W43 JA × EN deviations (same pairing, W43 shipped SVG as yardstick)

Furniture deviations: NONE except those forced by the issue itself —
VOL.2 (vs VOL.1), PDF names `Lucerna-VOL2-EN(.pdf/-web.pdf)` (W45
fan-out naming; W43 used `Lucerna-VOL1-EN`), counts (W43: A2 48 / B1 75 /
B2 27, essay 150 chars; W45 core: A2 46 / B1 75 / B2 29, essay 167
chars), and the readers'-corner disclosure, which follows the W45
coordinator ruling (§6) rather than W43's shorter two-line form.
Masthead geometry, badge text, footer pattern, gloss prefix, P8
separators/headers, instruction and type-name sets, quote page-tag style
(p.N), band-subtitle pattern, and "Your turn" wording are all identical
to the W43 JA × EN precedent. The README §20 JA-target geometry case
(JA × ZH-TW: wordmark stays at 262) was NOT followed, per the brief:
the same-pairing W43 JA × EN geometry (wordmark 248) governs.

## 11. Delivery record (builder scope only)

- Delivered to: `files/weekly-report-w45-ja-en/` — svg ×8, cards ×8,
  print PDF, web PDF, WEEKLY-KIT.md (this file), ABSTRACT.txt.
- Print PDF: 27,138,307 B,
  sha256 abb86daf0ff11308bec4f104eb6ce7dae869847a7dacaab198339003ef39919f
- Web PDF: 3,038,903 B,
  sha256 5a4893e50047c5dbde3cce1da8c56149d1b227c24a646755609714b678036cd3
- NOT done (out of builder scope, awaiting a fresh full independent
  proofread per SOP §8.4 and the main line): finalization announcement,
  Discord delivery (still paused by the user's standing order), repo
  insert, any cron change.
