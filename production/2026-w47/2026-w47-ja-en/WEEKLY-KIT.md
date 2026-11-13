# WEEKLY-KIT — Lucerna 日本語版 VOL.4, English-reader edition (W47, 16–22 Nov 2026)

Slug: `2026-w47-ja-en`. Target language: Japanese. Reader language:
English. Built by fan-out from the re-settled core `2026-w47-ja-zh-cn`
(core-ja, frozen; only the explanation layer was rewritten).

## §1 Specification — SOP §1.1 visual system

- 8 pages, 1950×2700, 4 columns. Paper `#fbfaf6`, ink `#302c28`,
  caption `#6f675d`, fine line `#d8d2c4`, book-green cloth `#37402f`,
  olive `#46581f`, goose-yellow `#f6e08e`, on-cloth `#f4efe1`.
  Level badges: A2 `#5c6e30`, B1 `#46581f`, B2 `#37402f`, white text.
  No gold, no brick-red, no near-black backgrounds; no double outer
  frame; no `·` separator anywhere (8/8 SVGs: `·` 0×, `#fbfaf6`
  1×/page, old `#f7f1e2` 0×).
- Masthead `Lucerna` (no article for Japanese; UnifrakturMaguntia
  196px = 147pt). P1 headline 56px = 42pt. Margins MX=88px = 66pt.
  Footer every page: `Lucerna　JAPANESE WEEKLY VOL.4　Japanese text
  English explanations`, page line `Page N of 8` (English, per
  reader language). VOL.4 everywhere it is an issue number; the
  only VOL.3/VOL.5 strings are frozen article text (P4 previous-issue
  note, P7 next-issue teaser — same as the core).
- Exercises: 150 total, continuous numbering 1–150, registry-generated
  P8 answers. Measured: A2 48 · B1 73 · B2 29. By page:
  10/18/18/18/18/18/12/38. By type: fill-in 50 · multiple choice 51 ·
  matching 12 · sentence building 8 · true/false 11 · cloze 13 ·
  translation 4 · writing 1. P8 model text 154 characters.
- Practice section heads stay in Japanese, frozen (A　理解,
  B　ことば, C　数字と日付, C　文を作りましょう,
  D　ペアにしましょう, D　正しい・正しくない, B　グラフ,
  C　数字と事実, D　文を完成しましょう, B　一般問題,
  スポーツ　体育); exercise-type labels are English (fill-in,
  multiple choice, cloze, matching, sentence building, true/false,
  translation, writing). `match_set` instruction is
  `Match words to meanings`.
- `りくりゅう`: romaji `rikuryuu` in the P7 gloss and P8 answers.
  `ちいかわ`: `Chiikawa` (never the Chinese name 吉伊卡哇).
- Trend-box source line (P1): `Sources and dates are in the articles`
  (fits the 400px box). P7 disclosure (readers' corner) is English:
  "Editor's sample, not a real letter. No real letters or best Page 8
  compositions had arrived by the deadline; both will appear in VOL.5.
  Send us your letter in Japanese — selected letters will be printed
  in VOL.5!" No real letters were fabricated; nothing was fetched
  from any mailbox.

## §2 Lead and page contents

Same as the core (frozen Japanese text, facts, dates, pictures).
P1 lead: Ni-no-tori + Beaujolais Nouveau release, Thu 19 Nov.
P2 life (Tori-no-ichi + kumade). P3 culture (Beaujolais + stalls).
P4 sport (sumo Kyushu basho days 1–3, champion undecided, final
result promised in VOL.5). P5 youth (30 buzzword nominees +
Arashiyama photo). P6 deep read (foliage moving to Kyoto + labelled
practice-data chart, 38/24/22/16 = 100%). P7 language focus
(A2/B1/B2 columns + error clinic ×4 + frame 「福をかき込む」 +
readers' corner + 8 golden phrases + VOL.5 teaser). P8 assessment
+ writing + all keys.

## §3 Trend sources

Unchanged from the core — see `core-ja/WEEKLY-KIT.md` §3 (sumo
day 1–3 results, Tori-no-ichi, Weathernews foliage forecast,
Beaujolais Nouveau 19 Nov, buzzword nominees 5 Nov, calendar).
No new research was done for the fan-out; no fact was changed.

## §4 Promises honoured

Same as the core (KIT §4): sumo final in VOL.5, buzzword top 10 +
grand prize 1 Dec, readers' letters + best P8 writing carried
forward (disclosure re-printed in English), foliage continuation.

## §5 Golden phrases

The core's 8 phrases, verbatim Japanese + English glosses on P7
(English glosses translated from the core's Chinese glosses; the
Japanese sentences are byte-identical to the core).

## §6 Images

Same five PD/CC0 images as the core (P1 maple, P3 beaujolais,
P5 Arashiyama pond, P7 tori 2025, P8 Arashiyama temple). Credits
in `assets/CREDITS.md` (copied from the core). English captions
are the translated map values (e.g. `Photo: Poliphilo — CC0
(Wikimedia Commons)`).

## §7 Proofread record (builder self-check, this edition)

- Full text read: `2026-w47-ja-en.text.md` (1348 text lines) +
  all 8 card PNGs visually checked. No overflow, overlap, footer
  strike or tofu found in the final artifacts.
- Simplified-Chinese residue scan over the text dump:
  1 hit at first pass — the P8 answers header was still the core's
  Chinese line (classifier miss, see §11 F3); fixed to
  `答え　Answers — grouped by page; just find your number`.
  Second pass: 0 hits. `吉伊卡哇` 0×; `ryuuryuu` / `Chiikawa`
  as specified.
- 150 keys re-verified key-by-key against the core extract:
  only [137, 138, 139, 140] differ — the E-group translation
  answers, translated JA→EN as ruled (core keys are the Chinese
  sentences; en keys are their English translations). All other
  146 keys byte-identical to the core.
- P7 teaser ends 2557.1 (footer 2580, 23px clear); P7 col3 ends
  1783.1. P8 exercise flow ends col 3 y=531 (bottom 1252); P8-keys
  flow ends y=2530.5 (col 2 key 76; col 3 key 114 y=2530.3; bottom
  2540, 9.5px slack; footer divider 2596, clear; occlusion audit
  0 flags — measured run11; the earlier "ends col 3 y=2426 /
  114px slack" figure was stale, corrected in fix round 1, F6).

## §8 Gates (all recorded in scratch-fanout-ja/)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE
  (`build-en-run12.log`; fix-round-1 builds are run11 content,
  run12 the identical re-run for the freeze check; registry
  unchanged: 150 total, A2 48 / B1 73 / B2 29, pages
  10/18/18/18/18/18/12/38, types as §1).
- Occlusion audit: `tools/occlusion_audit.py` — 0 flags
  (`en-occlusion-run11.json`; selftest OK, all 6 classes fired on
  planted controls, clean controls silent).
- P8 extract: `tools/p8.py extract --total 150` — noted set 150/150
  (`en-p8-run11.json`).
- P8 compare: `tools/p8.py compare` vs the core — status CLEAN,
  missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139, 140]
  (`en-p8compare-run11.json`).
- Freeze: direct sha256 of the 8 SVGs, two consecutive builds
  (run11 vs run12) — 8/8 byte-identical (`en-sha-run11.txt`,
  `en-sha-run12.txt`).
- Web PDF: `tools/webpdf.py` — `Lucerna-VOL4-JA-EN-web.pdf`,
  4,379,966 bytes (< 7 MB), 45,936 pdftotext bytes, text
  byte-identical to the print PDF (character multiset).
  Print PDF: `Lucerna-VOL4-JA-EN.pdf`, 25,806,211 bytes, 8 pages.
  Print sha256:
  `c6a15edb8a6c9e2954cb844b38b36a27f19d404ede7ad5084c3d3389db3410cf`.
  Web sha256:
  `0560f0e4ea8520899c0b7054ded812d2a16fba6cec0f9e55cfc3bec8b99c1d8d`.
- Text: `2026-w47-ja-en.text.md`, 45,706 bytes, 1348 text lines,
  exported from the final SVGs (`export-textmd-en.py`,
  reconstructed — see §11 F6; byte-identical reproduction of the
  pre-fix file from the pre-fix SVGs).
- P8 minimum font size: 9.975pt (answers, 13.3 SVG px; PyMuPDF
  measurement of print PDF p.8; next size 10.35pt = exercises).
  P8 stems stay at 13.8px / 10.35pt per the core (Round 6 rollback).
- §1.1 grep audit on the final SVGs: paper `#fbfaf6` 1×/page,
  old `#f7f1e2` 0×, banned colours 0×, `·` 0×, badges A2 `#5c6e30`
  / B1 `#46581f` / B2 `#37402f`, masthead 196px on P1, page line
  `Page N of 8` 1×/page, VOL.4 as the issue number.
- U+2019 sweep: 0 in all 8 SVGs and in both PDFs' text layers
  (U+2018 also 0). 150-key re-verification (fix round 1): answer
  block old-vs-new diff = exactly the 6 F6 note lines; all 150
  keys byte-identical to the previous round (extract JSON keys
  48=B, 49=A, 54=11, 63=○, 111=11, 116=A).

### D5 rebuild (2026-11-12, SOP §1.1; template `mechanism/svglib-ja-d5.py`
installed as the edition svglib, `_D5_READER = "latin"`, 0 lines diff vs template)

- Production census before: D5 Latin 406 in Noto Sans CJK, Cyrillic 0, curly in CJK 0; after: D5 census PASS (Latin 0 / Cyrillic 0 / curly in CJK 0); quotes census 0 defective.
- Full gates, all green: run.py TOTAL 150, 0 FLOW OVERFLOW / 0 HEAD TOO WIDE (head_check PASS); occlusion 0 flags (selftest 6/6); p8 extract 150/150, compare vs D5 core-ja CLEAN, keydiff exactly [137, 138, 139, 140] (expected reader-language keys); freeze baseline 8/8 byte-identical; freeze diff vs pre-D5 base: added CJK 2 (both U+3000, run-split whitespace artifact); spill 0 SPILL (35 boxes, 84 OBSERVE); boxtitle 0 DEFECT / 0 OBSERVE (38 titles, 500 body lines, real pre-D5 backup); edge 0 TOUCH / 0 NEAR; creambox PASS 0 defects (ratios n=377 median 1.012 boldT 1.040 boldF 1.000; P8 lines 238→226, slack 61.5→61.7 px); text layers character-multiset identical print vs web and vs delivered (26,470 chars; delivered 26,578 raw, difference whitespace only).
- Print PDF `Lucerna-VOL4-JA-EN.pdf`: 25,806,203 bytes, sha256 `a063fff2f05e07ba7957834b7513344bead7ee8c9042dd22b028797e803a972f`.
- Web PDF `Lucerna-VOL4-JA-EN-web.pdf`: 4,379,969 bytes (< 7 MB), sha256 `9c9e2fd0d832973a89dc378bc94db29922a126a2ef139387ac37879d86a105d2`, 45,936 text bytes.
- Text.md unchanged (45,706 bytes). Post-sync verification on the production dir: freeze baseline 8/8, D5 census PASS, quotes census 0. Evidence in `hidden_files/w47/scratch-d5-ja/ja-en/` (RUN-LOG.md, gate logs + JSONs).

### Fix round — D1/D2 romaji fix (2026-11-12; independent reproof PROOF-NOTE.md)

- D1 (all 11 ja editions): `りくりゅう` romaji `ryuuryuu` → `rikuryuu` (5× per edition: P7 gloss + P8 answers 66/77/80/105). Sources: `content7.py` (2×) + `content56.py` (3×). Japanese core text `りくりゅう` untouched; answer letters untouched.
- Changed SVGs vs pre-fix: p7-kotoba.svg, p8-tesuto.svg; unchanged: p1-hyoushi.svg, p2-kurashi.svg, p3-bunka.svg, p4-supotsu.svg, p5-wakamono.svg, p6-fukayomi.svg.
- Print PDF `Lucerna-VOL4-JA-EN.pdf`: 25,806,211 bytes, sha256 `c6a15edb8a6c9e2954cb844b38b36a27f19d404ede7ad5084c3d3389db3410cf`.
- Web PDF `Lucerna-VOL4-JA-EN-web.pdf`: 4,379,966 bytes, sha256 `0560f0e4ea8520899c0b7054ded812d2a16fba6cec0f9e55cfc3bec8b99c1d8d`.
- Text `2026-w47-ja-en.text.md`: 45,706 bytes, sha256 `fb5a4700d3c94cd17039d8b69d2626e35ed115812fdcb5ca34f17294f8860c3f` (surgical replacement, exactly 5 lines changed, each only by the fix substitution).
- Full re-gates (all green):
  - run.py: P8 saved, TOTAL exercises: 150
  - head_check: HEAD CHECK PASS 0 defects
  - D5 census: CENSUS PASS
  - quotes: GRAND TOTAL defective: 0
  - occlusion: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-en/2026-w47-ja-en/svg: 0 flags 
  - p8 extract:   set: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
  - p8 compare: status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140] {'status': 'CLEAN', 'total': 150, 'how': 'lines', 'ref_how': 'lines', 'core_count': 150, 'edition_count': 150, 'core_set': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 4
  - freeze baseline: core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
  - freeze diff vs pre-fix base: p8: +4 strings / -4 strings; CJK core 1422 -> edition 1422; added CJK chars: 0 ; added Latin strings: 4 (unexpected 4) | TOTAL added CJK characters: 0 | TOTAL added Latin strings: 5 (unexpected 5)
  - spill: SPILL_SWEEP 2026-w47-ja-en: 35 boxes, 84 candidates, 0 SPILL, 84 OBSERVE
  - boxtitle: BOXTITLE 2026-w47-ja-en: 38 titles, 500 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal
  - edge: EDGE_SCAN 2026-w47-ja-en: 8 pages, 0 TOUCH, 0 NEAR
  - creambox: CREAMBOX PASS 0 defects
  - text layer: print-vs-web multiset diff: +0 -0 IDENTICAL
  - PDF text: /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-en/2026-w47-ja-en/Lucerna-VOL4-JA-EN.pdf ryuuryuu: 0; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-en/2026-w47-ja-en/Lucerna-VOL4-JA-EN.pdf rikuryuu: 5; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-en/2026-w47-ja-en/Lucerna-VOL4-JA-EN-web.pdf ryuuryuu: 0; /home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ja/ja-en/2026-w47-ja-en/Lucerna-VOL4-JA-EN-web.pdf rikuryuu: 5; 
- Post-sync verification on the production dir: freeze baseline 8/8, D5 census PASS, quotes census 0; production svg/text.md `ryuuryuu` 0×, `rikuryuu` 5×.
  Evidence in `hidden_files/w47/scratch-fix-ja/ja-en/` (fix log + gate logs + JSONs).

## §9 Reproduction

Build dir:
`production/2026-w47/fanout-ja/2026-w47-ja-en/` (copied from
`core-ja/` by `scratch-fanout-ja/apply.py en`, map
`scratch-fanout-ja/map-en.json`, 221 map keys + 6 instr + meta;
total key set 224 incl. the 3 post-apply additions, see §11).
`tools/venv/bin/python run.py`, then `render.py` (cards PNG +
print PDF), then `tools/webpdf.py svg Lucerna-VOL4-JA-EN-web.pdf`,
then `export-textmd-en.py`. Never run a build module standalone;
never import a content module inside a build dir. Scratch (logs,
probes, gate JSONs, maps) lives in
`hidden_files/w47/scratch-fanout-ja/`.

## §10 VOL.5 promises registered

Same as the core (KIT §10).

## §11 Fix record — fan-out fixes (builder, 2026-11-11)

- F1 (P8-keys overflow, the blocker inherited from the 3rd baton):
  keys flow ended col 3 y=2569 (bottom 2540); the last 6 entries
  (145–150) were all drawn on top of each other at y=2553.3.
  Root cause found non-destructively: `Flow.para(split=False)`
  advances `size + lines*size*lh + gap` per entry (13.3px baseline
  overhead per entry) while `_fit` only counts `lines*size*lh +
  gap`, so the flow overfills silently until the last column
  clamps. Fix (SOP §1.1 step 2, notes only — keys untouched):
  shortened 12 distinct answer notes (19 entries: 1, 2, 3, 5, 8,
  10, 20, 31, 32, 55, 68, 81, 87, 112, 114, 117, 119, 120, 123,
  126) to one line each, each verified with `svglib.wrap()` before
  editing and by full-flow simulation after. Result: keys flow
  ends y=2426, zero overflow.
- F2 (P1 LINEX): the word-of-the-week English gloss wrapped to
  3 lines and its last line `fortune.` (baseline y=1891.6) was
  struck by the row-B divider at y=1884. Fix: shortened the gloss
  to 2 lines (`…a charm for thriving business.`, last baseline
  1865.9, ink clear by ~13px). Re-audit 0 flags.
- F3 (Chinese residue, classifier gap): the P8 answers header was
  still the core's Chinese line — the classifier's ZH-marker set
  has no marker in it (no char from its set occurs), so it never
  entered the map, and apply.py's leftover check exempts every
  core literal not in the map, so nothing caught the omission.
  Fixed to W46 style with a §1.1 full-width space:
  `答え　Answers — grouped by page; just find your number`
  (width-verified: ends x=785.3, right-side text starts x=1281.5).
  The key was added to `map-keys.json` / `map-en.json` (222nd key).
- F4 (same gap, P7 bridges): two bridge glosses were missed for
  the same reason (their Chinese glosses use only kanji that are
  also valid Japanese: 之/提/拍): A2 bridge
  `酉の市 酉之市　熊手 熊手　手締め 拍手` →
  `酉の市 Tori-no-ichi　熊手 kumade　手締め hand-clapping`;
  B1 bridge `ノミネート 提名` → `ノミネート nomination`
  (W46 precedent: bridges are word + reader-language gloss).
  Added as keys 223–224. A full audit of all 575 frozen core
  literals (bridge/gloss args, `=` literals, short CJK literals)
  found no further missed Chinese glosses; the remaining
  not-in-map literals are frozen Japanese (section rubrics,
  stems, captions, golden phrases, f-string fragments handled by
  apply.py's structural edits).
- F5 (`·` separators): 13 occurrences (12 match-note `· letter`
  suffixes + the P8 header `·`) — W46 style, but §1.1 bans `·`
  and the core is 0×. Changed to the core's pattern (bare space +
  letter, e.g. `…for thriving business c`; header uses a
  full-width space). SVG grep now 0× on all 8 pages.
- Map accounting: `map-keys.json` 224 keys; `map-en.json`
  221 map keys + 6 instr, incl. instr-only 3 keys = 224 total.
  (Was 221 at handoff; +1 P8 header, +2 P7 bridges.)

- F6 (fix round 1, 2026-11-11 — proof round 1 D1/D2, sumo
  wrestler romaji in P8 answer notes; keys themselves all correct):
  `Umi-no-umi` → `Churanōmi` (key 48, content34.py:188);
  `Fujiryūga` → `Fujiryōga` (keys 49/54/63 content34.py:190/202/224,
  key 111 content7.py:57, key 116 content8.py:22). Readings
  verified independently against public sources before editing:
  美ノ海 = ちゅらのうみ (sumo-guide 力士名鑑「美ノ海 義久
  （ちゅらのうみ よしひさ）」; スポーツ報知 2026-10-26
  「美ノ海義久（ちゅらのうみ・よしひさ）」); 藤凌駕 =
  ふじりょうが (ozumo.jp, citing Japan Sumo Association profile:
  「藤凌駕 雅治（ふじりょうが まさはる）」; Wikipedia 同).
  Full-edition grep after the fix: `Fujiryūga` / `Umi-no-umi`
  0× in .py sources, SVGs and .text.md (the only remaining
  hits are the quoted old forms inside this KIT §11 record
  itself). Stale `__pycache__/content7.cpython-312.pyc` still
  carried the old bytes and was deleted by hand; the build
  itself reads sources via runpy, so it was never loaded.
  The two wrong spellings came from upstream: core-ja
  `WEEKLY-KIT.md` §3 trend-source record (lines 80–90) writes
  "Hōshōryū beat Umi-no-umi", "Kotosakura lost to Fujiryūga",
  "Ōnosato beat Fujiryūga", "Hōshōryū lost to Fujiryūga —
  Fujiryūga's first kinboshi". No shared romaji table file
  exists in this clone (`map-en.json` / `apply.py` absent, see
  proof round 1 O3); each Latin-script fan-out carried the same
  6 strings. Other editions NOT touched, state report only:
  ja-es / ja-fr / ja-it / ja-nl / ja-pt .py sources still carry
  `Fujiryūga` ×5 + `Umi-no-umi` ×1 each; ja-de .py already
  reads `Fujiryōga` ×5 + `Churanoumi` ×1 (different spelling,
  no macron — fixed separately / by another hand, not verified
  here); ja-ko / ja-ru / ja-zh-tw .py carry no Latin forms
  (Japanese kanji in notes). Core-ja untouched (red line).
  `export-textmd-en.py` was also absent from this clone, so it
  was reconstructed and restored into the edition dir (validated
  by byte-identical reproduction of the pre-fix .text.md from
  the pre-fix SVGs, and of the post-fix .text.md from the
  post-fix SVGs). Present-round §7 correction:
  the P8-keys flow actually ends y=2530.5 (measured run11),
  not y=2426 as previously recorded — pre-existing (line counts
  unchanged by this fix; occlusion 0, no defect).
  Rebuilt run11 + freeze re-run run12 (see §8).

- Fix round (2026-11-12, D1 romaji fix; see §8 fix subsection for gates + SHAs): D1 `ryuuryuu` → `rikuryuu` in `content7.py` + `content56.py` (5×, P7 gloss + P8 answers 66/77/80/105). Full rebuild + re-gates; print/web/text.md re-synced with new SHAs recorded in §8.
