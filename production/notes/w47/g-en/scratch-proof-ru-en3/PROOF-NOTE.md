# PROOF NOTE — 2026-W47 ru-en, Proof 3 (independent, from scratch)

- Edition: `2026-w47-ru-en` (Russian target × English reader), VOL.4, issue 16–22 November 2026
- Proofer: proof3 (independent of fix1, patch executor, and proof2); 2026-11-11
- Work dir (read-only use): `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-en/`
- Core对照: `~/workspace/weekly-git/production/2026-w47/core-ru/`
- Notes dir: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-en3/`
- No source was edited, nothing rebuilt, no commit, no push, no change to `tools/` (per the brief).
  All tool outputs were written to this scratch dir only. `freeze.py baseline` ran on a copy
  under `freeze/` in this scratch dir, never in the edition dir.

## 0. Identity — SHA checks (ALL PASS)

| File | Bytes | SHA-256 | Expected | Result |
|---|---|---|---|---|
| `Lucerna-VOL4-ru-en.pdf` (print) | 21,245,374 | `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e` | same | **MATCH, 8 pages, 1462.5 × 2025 pt** |
| `Lucerna-VOL4-ru-en-web.pdf` (web, italic-patch rebuild) | 3,375,060 | `6419f7ad188d0e6aca09ae76abc739e954d0d6e1d5249171c34376e6b61360b6` | same | **MATCH, 8 pages, 1462.5 × 2025 pt** |
| `2026-w47-ru-en.text.md` | 56,600 | `2bf57f6808763372a1022cfe7dcaecae766a4a10ba62263e845c63166f66cc6c` | KIT §5: 56,600 B, 150 exercises, 203 blocks | **MATCH on bytes/exercises; SHA measured on disk** |

Notes on identity:
- The brief said to check the text.md SHA against an `EDITION-RECORD.md` in the edition
  dir. **No such file exists** in the edition dir or in `core-ru/` (searched). The record of
  reference is KIT §5 (56,600 bytes, 150 exercises, 203 blocks); bytes and exercise count
  match my measurements, and the SHA above is my independent on-disk measurement.
- SHAs of both PDFs and text.md were re-verified at the END of the session as well
  (after all tool runs): unchanged.
- One mtime moved during my session: `ru_textmd.py` shows mtime 2026-11-11 09:31:16 UTC;
  I did not edit it and none of my commands write to the edition dir (all writes went to
  this scratch dir; freeze baseline operates on its copy under `freeze/`). The SVG files
  all still carry their 08:05–08:06 mtimes, and the three deliverable SHAs are unchanged,
  so nothing in the edition changed. Logged here for the coordinator; most likely another
  concurrent agent touched the file.

## Verdict: (a) — ZERO defects. Ready to finalise.

The print PDF passed every check with no finding (as proof2 found). The web PDF's single
defect cluster from proof2 (D3, P1 WORD OF THE WEEK «чёрная пятница») is **fixed on all
three facets, verified by independent re-measurement** (not by trusting PATCH-LOG/GATE-LOG).
D1 and all 7 D2 spots remain fixed. The full from-scratch re-read of the web PDF (all 8
pages), text.md (690 lines), and SVG found no further defect. Two documentation corrections
for the KIT (not edition defects) are listed in §6.

---

## D3 — VERIFIED FIXED, all three facets (independent re-measurement)

P1 WORD OF THE WEEK box, line «чёрная пятница» (PDF line y0=1266.76, span x 1088.042–1222.815).
My own fresh script (`verify3.py`, char-level PyMuPDF rawdict; `verify3b.py` for the pinned
line-126 numbers). Values below are measured by me on the shipped files.

### D3(a) — Space: PRESENT, byte-identical bbox
- Web span text is `'чёрная пятница'`; the space char exists with bbox
  `[1145.576, 1266.762, 1148.108, 1288.725]`, width 2.532 pt — **identical to print**.
- Gap 'я'→'п': print 2.532 pt = web 2.532 pt, diff **0.00 pt** (was print 2.532 vs web 1.177).
- `pdftotext`: print **57,149 B** / web **57,149 B**; `diff` RC=0, zero differing lines.
  `«чёрная пятница»` ×10 in both texts; `'чёрнаяпятница'` ×0 in both.
- Whole-edition char totals: 35,198 chars each; spaces 4,905 each; non-whitespace 30,293 each.
- 3× crop (`crops/p1-teaser-print.png` / `p1-teaser-web.png`, clip x1040–1420, y1240–1330):
  **pixel-identical** — same SHA-256, 0 / 307,800 pixels differing. Read by eye: italic,
  two words with a clear space, closing » tight.

### D3(b) — Closing »: gap identical to print
- Last 'а' of пятница x1: print 1222.815 = web 1222.815, deficit **0.00 pt** (was 3.354).
- '»' x0: 1220.622 in both. Advance-box gap 'а'→'»': **−2.193 pt in both** (italic overhang
  restored; was +1.161 in web).

### D3(c) — Italic: present in web, char count equals print
- Web embeds `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic` (`pdffonts`; both
  embedded, subset, Unicode).
- Italic chars: print 16 (NotoSerif-MediumItalic 14 + Newsreader16pt-Italic 2) =
  web 16 (LucernaNotoSerif-Italic 14 + LucernaNewsreader-Italic 2).
- D3 span fonts: print NotoSerif-MediumItalic / Newsreader16pt-Italic; web
  LucernaNotoSerif-Italic / LucernaNewsreader-Italic, same 16.12 pt, same bboxes.

---

## D2 — all 7 original spots still 0.00 pt (direct pinned lookup)

| Spot | Print x1 | Web x1 | Deficit (was) |
|---|---|---|---|
| P1 headline `14-` 39.75 pt | 133.018 | 133.018 | **0.00** (was 4.33) |
| P4 heading `14-` 24 pt | 106.464 | 106.464 | **0.00** (was 2.62) |
| P1 contents `1. 14-` 15 pt | 1138.695 | 1138.695 | **0.00** (was 2.20) |
| P4 band-sub ` все восемь результатов` 13.5 pt | 1008.743 | 1008.743 | **0.00** (was 1.94) |
| P1 contents `3. «` 15 pt | 1122.225 | 1122.225 | **0.00** (was 1.17) |
| P5 title `«` 24 pt | 80.112 | 80.112 | **0.00** (was 0.91) |
| P7 `«` 16.12 pt, x0=1096.12 (y0 201.01 & 338.65) | 1105.606 / 1105.606 | 1105.606 / 1105.606 | **0.00 / 0.00** (was 0.58) |

Note: my `verify3b.py` pins the two P7 spots by (y0, x0); the looser `verify3.py` scan found
all six `«` occurrences at x0=1096.12 on P7, every one 0.00. Print P1-headline font is
Newsreader16pt-Regular while web is LucernaNewsreader-Bold at the same x1 — the weight
patch's intended face mapping (SemiBold≈Bold advance), x1 identical, so no defect.

## Full independent print-vs-web scan (two implementations agree)

- **My fresh implementation** (`verify3.py`: line (y0,y1) + order pairing, advance-box gaps,
  intra-span char-pair gaps, per-page multisets): span-text diffs **0**; abutting pairs
  > 0.5 pt: **0** (max |diff| **0.00 pt** over all pairs); intra-char diffs > 0.5 pt: **0**
  (max |diff| **0.00 pt**); per-page multiset diffs: all 8 pages empty.
- **Proof2's own script re-run** (`fullscan-proof2-copy.py`: copy of proof2's file, only the
  two paths changed to absolute, output to this scratch dir): span-text diffs **0**;
  abutting > 0.5 pt: **0**; intra-char > 0.5 pt: **0**; multiset diffs all 8 pages `{}`.
- Full-page pixel check: P8 print-vs-web mean abs diff **0.0**, 0 px > 30 (P8 has no images);
  P1 mean 0.213, 2,504 px > 30 of 4,264,650 — broken down by region: masthead (y<300)
  2,084 px (the large UnifrakturMaguntia display face rasterises slightly differently from
  the subset font), photo zone (y1600–2100) 420 px (web images are downscaled by design),
  body text (y300–1600) **0**, quiz/footer (y>2100) **0**. Text geometry is identical
  (char-level scan max diff 0.00 pt); the masthead difference is rasterisation only.

## D1 — FIXED, both PDFs
- P5 band subtitle reads `"Black Friday": sales from 16 November`, straight quotes, in
  print.txt:1136 AND web.txt:1136 (identical files). 3× crop (`crops/p5-band-web.png`) read
  by eye: closing straight quote tight on `:`.
- Curly-quote sweep (visible `<text>` in all 8 SVGs, ElementTree): U+201C ×1, U+201D ×1 —
  both on P7, the intended Newsreader pair `“чёрной пятнице”`. U+2019 ×0, U+2018 ×0.
  Same counts in both PDFs' text layers (1 × “ and 1 × ” each); straight `"` ×2 in each.
- Italic runs in SVG: exactly 5 `font-style="italic"` `<text>` runs, all in
  `p1-pervaya.svg` — the edition's only italic text, as the patch log states.

## Known narrow-gap class — re-checked, NOT a defect (matches proof2 ruling, same evidence)
- P5 band `' скидкис'`: chars measured — inter-word gap 'и'→'с' = **1.201 pt** at 13.5 pt
  (a full space in this face is 2.983 pt), identical in print and web (byte-identical char
  boxes). 3× crop read by eye: `«Чёрная пятница»: скидки с 16 ноября` — the gap reads as
  a space. Same class as P5 `маркетплейсахскидки` and P1 `большая распродажав`: a
  space-only SVG run skipped by CairoSVG, positioning-only gap, present in BOTH pipelines
  identically. No print/web divergence → not a defect. Same for the 4–6 px run-boundary
  gaps (`От редакцииLucerna`, `синоптикиобещают`, `Профессиональныепраздники`) — narrow
  but readable, identical in both PDFs (full scan max diff 0.00).

---

## Content proofread — web PDF + print PDF, all 8 pages read fully vs core-ru

Read `txt/print.txt` end to end (2,527 layout lines, P1–P8; web.txt byte-identical) and
`2026-w47-ru-en.text.md` end to end (690 lines). No content defect found.

- **Dates/weekdays** verified with `date` (Europe/Moscow): 16 Mon / 17 Tue / 18 Wed /
  19 Thu / 20 Fri / 21 Sat / 22 Sun Nov 2026; 6–8 Nov Fri–Sun (round 14); 12 Nov Thu
  (Uzbekistan 18:00, Pakhtakor); 17 Nov Tue 19:00 (Venezuela, Krasnodar, Ozon Arena);
  15th round 20–22 Nov Fri–Sun; Black Friday 27 Nov 2026 is a Friday; Cyber Monday 30 Nov
  is a Monday; Mother's Day 29 Nov is a Sunday; November 2026 = 20 working days + 10 days
  off. All weekdays printed in the paper match the calendar.
- **Numbers**: 31 pts Zenit/Dynamo, 29 Spartak, 26 Krasnodar/CSKA, 15th Lokomotiv; 21 goals;
  4:2 Krasnodar–CSKA (7 Nov); 2:2 Zenit–Rostov (83rd-minute equaliser); 2:1 Dynamo–Fakel
  (90+1 winner); 0:1 Lokomotiv–Rubin; correction box (VOL.3 printed 7 matches; 8th:
  Baltika — Dynamo Makhachkala 0:1, 8 Nov 20:45) — all internally consistent and matching
  core. Practice chart 38+26+18+18 = 100, explicitly labelled as editor-made practice data.
- **Spot-checked a dated claim against live sources**: «Голодные игры: Рассвет жатвы»
  26 November — confirmed for Russia (TMDB Russia release 11/26/2026; kinoafisha.info
  26 November 2026 Russia; ixbt.games: Russian premiere 26 Nov, moved back a week from
  19 Nov). US date 20 Nov is a different market; the paper's Russian date is correct.
- **P7 golden sentences**: `check_core.py` GOLDEN 8, BAD 0; I re-verified each of the 8
  quotes verbatim against the body text I read, with correct English translations and page
  attributions (P1/P1/P2/P3/P4/P5/P6/P6). Error clinic 4 items all correct
  (с + instrumental; на + prepositional; 21 + гол; с 19 + genitive ноября).
- **P8**: `p8.py extract` 150/150 noted; `p8.py compare` vs core-ru **CLEAN**, missing=[],
  extra=0, keydiff=[137, 138, 139, 140] (the four E translation keys, as expected).
  Answer key 1–150 all present in the printed P8; every key I spot-checked matches the body
  (incl. 21→1946, 22→16:20, 56→20:45, 63→играет, 73→заказов, 109→Синоптики обещают,
  127→B Dynamo Mkh 1:0, 145–149 dialogue). Model text (Q150) = **97 words** (counted by
  hand from the printed text; 80–100 required). P8 min font **9.75 pt** (387 spans; next
  9.98) — meets ≥ 9.75 pt.
- **Visual pages**: all 8 print pages rendered from the PDF and read by eye (P1, P2, P3,
  P4, P5, P6, P7, P8); web P1 read by eye. No overflow, no overlap, no clipped text, no
  text crossing the footer line; P5 exercises end clear of the footer; P8 answer key
  complete to Q150. The mid-page white space on P2/P3 is the standard anchored-exercises
  layout, not a defect.
- **Photos/credits** (all public domain, as labelled): 1912 Russia football team (author
  unknown); Yuon «Зима. Ростов»; Preston Keres / USDA; Kiprensky Pushkin portrait 1827;
  Toxer427 CC0. No image issue beyond credits (occlusion audit covers geometry).
- **VOL**: VOL.4 ×9 (masthead + 8 footers), VOL.3 ×1 (P4 correction sentence, expected),
  VOL.5 ×6 (teasers/disclosure, expected); `tables.py vol 2026-W47` → vol 4.
- **ABSTRACT.txt**: one English line, no ASCII double quotes, names the real W47 topics +
  VOL.4 + A2–B2 + 150 exercises.

## text.md — read in full, compared vs core text.md
- 690 lines, 56,600 bytes; 150 numbered exercise groups, numbers 1–150 complete, no gap
  or duplicate.
- **0 Russian stem diffs** vs core: all 150 stems byte-identical after stripping the
  translated level tag; the 20 apparent diffs are only the parenthetical key glosses
  (English vs Chinese, e.g. `key b · Students' Day b` vs `大学生节`).
- **Key values identical except 137–140** (the E translation keys, English sentences by
  design) and the Q150 open-task note (translated; model text itself identical). All other
  key differences are the parenthetical English-vs-Chinese notes only.
- Trailing «Морозко» credit line identical to core; `— СТРАНИЦА ? —` separator present
  (same as core exporter format, known, not a defect).

## Freeze diff — CORRECTED invocation, fully adjudicated (see §6)
- `freeze.py baseline`: **8/8 SVGs byte-identical**, RC=0 (p5 hash `ae19aec9…` matches the
  KIT record); core integrity OK.
- `freeze.py diff --core-svg core-ru/svg --edition-svg <edition>/svg` (correct paths):
  removed strings are the Chinese explanation layer, replaced by English; added CJK is
  only U+3000 ×6 (furniture separators). **No Russian core string is lost**: every removed
  Cyrillic-bearing string was adjudicated individually (adjudicate-freeze.py):
  - P6 (11): `УЧЕБНЫЕ ДАННЫЕ` → `PRACTICE DATA` (same line, y=1552); chart-note words
    (`Это`, `учебный`, `опрос`, `редакции`, `для`, `упражнений`, `не`, `настоящая`,
    `статистика`) → English sentence at y=1582.
  - P7 (4): `Три уровня, три темы` → `Three levels, three topics` (same line, y=168).
  - P8 (20): 15 words are the Morozko caption + credit (see below); `тест/недели/все/
    ответы` are the P8 header subtitle → English subtitle `The big test of the week + all
    the answers`; one `можно` is key 46's note (`можно + 不定式` → `can + infinitive`).
  - Added Cyrillic-bearing strings: 0 on all pages. No new Russian invented.
- **P8 Morozko image**: core P8 renders it (422.5×250 at y=2212.39) + caption; en P8 has
  0 images. This is the shared build code's own condition (`content8.py:131-140`,
  identical in core-ru and the edition): `if af.ci == 3 and img_y + img_h + 90 < 2560`.
  In en, keys end col 3 y=2288.84 → img_y≈2312.84 → 2312.84+250+90=2652.84 > 2560, so the
  image is skipped deterministically. Same as W46 ru-en, documented in the KIT. By design,
  not a defect; the alternative (shrinking answers below 9.75 pt or overflowing the
  footer band) would be worse. text.md retains the Morozko credit line.

## Mechanical gates (all re-run by me on the shipped files; see GATE-LOG.md)
- `check_core.py`: GOLDEN 8, BAD 0, gloss fails 0, P8 SVG text 10,571 chars; 1 orphan
  line-start (P7 y553 `”».`, known benign) + 1 same-baseline collision (P1 y1712
  `чёрная` + ` `, the D3 line).
- `p8.py extract` 150/150; `compare` CLEAN, keydiff [137, 138, 139, 140]. RC=0.
- `freeze.py baseline`: **8/8 SVGs byte-identical**, RC=0; core integrity OK.
- `occlusion_audit.py`: `--selftest` OK; real run **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER,
  0 EDGE, 0 BOXTITLE**. Flag set identical (as a set) to proof2's `occlusion.json` AND to
  the italic-fix run's `occlusion.json` — no new flag. (The JSON files differ by one byte
  only in the `svgdir` path string: proof2 ran with relative `svg`, I ran with the absolute
  path.) The tool returns RC=1 whenever any flag exists — that is its by-design "flags
  present" signal, not a failure; the 42 flags are the round-1 pixel-adjudicated-CLEAR set.

## §6 — Documentation corrections for the coordinator (NOT edition defects)
1. **KIT §7 "freeze diff −0 removed on all 8 pages" is wrong as stated.** Proof2's and
   the italic-fix executor's diff runs passed `--core-svg <core-ru>` (the edition dir,
   which contains no `.svg` files directly), so the core side was empty and "−0 removed"
   was vacuous. My correctly-invoked run (`--core-svg core-ru/svg`) shows the real diff:
   P1 −21 / P2 −36 / P3 −28 / P4 −28 / P5 −27 / P6 −54 / P7 −59 / P8 −637 strings, all
   the Chinese explanation layer, fully adjudicated above with no Russian core loss.
   The KIT line should be corrected to the real diff + adjudication.
2. **KIT §7 "§1.1 spot-checks" still quotes the stale web size `3,367,620 bytes`** (the
   pre-italic-fix web PDF). §5 has the current 3,375,060 bytes / SHA `6419f7ad…`. One-line
   KIT fix.
3. `EDITION-RECORD.md` does not exist (see §0); if the coordinator wants text.md SHAs
   recorded per edition, that file needs creating — the KIT is currently the only record.

## What this proof did NOT do (per the brief)
- No source edits, no rebuilds, no commit, no push. No changes to core-ru, other editions,
  `tools/`, or the KIT. No files left behind in the repo (all outputs in this scratch dir;
  `git status` shows the two edition dirs as untracked (`??`, as before — they were never
  committed) and `tools/` with the four pre-existing modified files from other agents
  (`freeze.py`, `occlusion_audit.py`, `p8.py`, `webpdf.py`), none touched by me; no new
  file appeared in the edition dir during my session (only `ru_textmd.py`'s mtime moved,
  see §0).
- One service restart interrupted a combined p8/check_core exec midway; the p8 logs had
  already landed, and check_core was re-run cleanly afterwards (its log is in this dir).
