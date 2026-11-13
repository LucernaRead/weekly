# PROOF NOTE — 2026-W47 ru-en, re-proofread of the fix1 (S1) build

- Edition: `2026-w47-ru-en` (Russian target × English readers), Lucerna Weekly VOL.4,
  issue 16–22 November 2026.
- Proofer: independent re-proofread (all gates re-run by me, all defects re-measured
  on disk; nothing taken from FIX-LOG or proof1 on trust).
- Date: 2026-11-11. Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-en1/`
- Read first: repo `SOP.md` (§1.1, §8.4), `AGENTS.md`, coordinator brief,
  fix1 `FIX-LOG.md` (both Fix 1 and Fix 2 sections), proof1
  `scratch-proof-ru-en2/PROOF-NOTE.md` + `GATE-LOG.md` (reference only).
- Scope: this edition only. No production file modified, no commit, no push.

## Verdict: (b) — 2 DEFECTS FOUND, CANNOT FINALIZE

S1 itself is fixed and verified (see §1). But the full-line box-title sweep — the
check the brief orders for all 32 titles — finds one more title overhanging its box
(R1, same class as S1, much smaller), and the four-way sync check finds the fan-out
record still carrying the old long form (R2, latent revival risk). Both are minor;
neither touches the delivered text content. The fix for both is small and the
builder's to make; this note is not a sign-off.

## Defect R1 — minor: P6 box title "ЗА И ПРОТИВ FOR AND AGAINST" overhangs its cream box by ~0.7 px

- Location: P6, right column, "ЗА И ПРОТИВ" box. Source: the box title line in
  `svg/p6-razbor.svg` (runs on baseline y=705.5: `ЗА` x=1461.5, `И`, `ПРОТИВ`,
  `　FOR AND AGAINST` x=1625.4, Noto Sans CJK SC 24pt bold). Cream rect x=1439.5
  w=422.5 → right edge **1862.0**.
- Evidence (three independent measurements, all the same sign):
  (a) PIL true ink (`occlusion_audit.ink_box`, same fonts as the canonical audit;
  `gates/s1.log`): last run ink right **1862.2** (advance right 1862.21, confirmed
  at PIL scale 16 and 32 — not a quantisation artifact) → clearance **−0.2 px**.
  (b) Delivered PDF vector data (`gates/pdf-title.log`): rightmost char bbox
  1397.64 pt = 1863.5 px → clearance **−1.5 px**, identical in print and web.
  (c) Delivered PDF rendered pixels, the arbiter (task rule 3;
  `gates/raster_title_check.py`, 4× crops `crops/p6-title-crop-print.png` /
  `-web.png`, byte-identical): cream right column 1295, title ink right column
  1297 → clearance **−2 render px = −0.7 SVG px**. Read by eye: the top bar of
  the final `T` in `AGAINST` crosses the cream edge by 2 pixels at 4× zoom.
- Provenance: fan-out-introduced, same class as S1. The core-ru title is
  `ЗА И ПРОТИВ　正反两方`, ink right 1745.4, clearance **+116.6 px**; the English
  subtitle `FOR AND AGAINST` is what pushes the line out.
- Why proof1 missed it: proof1's spill sweep measures only the FIRST run of each
  title (`top = min(inside, key=y)` — `spill.py`), so for this box it measured
  `ЗА` (clearance ≈ +350) and never the full line. Its "0 bad titles" claim is
  true for that method and says nothing about full-line fit. My sweep measures
  the full title line (`s1_measure.py`): 32 titles, tightest is this one at −0.2,
  second-tightest +14.1 (P1 right-column box), all others ≥ +14.1.
- Correction on the brief: its "(tightest in proof1 +6.8px)" misattributes a
  kicker-gap value — 6.8 appears in proof1 only in the kicker list
  [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]; proof1 published no
  tightest-title figure. The re-measured tightest is −0.2 px (PIL) / −0.7 px
  (render), reported here as R1.
- Severity: minor — 0.7 SVG px ≈ 0.5 pt ≈ 0.18 mm, invisible at 100% view,
  readable, no collision. But it is a real overhang of the exact class S1 was
  (a visible front-page fault at 37.9 px blocked proof1), and the standing gate
  is proofread-until-zero with no tolerance rule for sub-pixel title overhang
  on the books. Fix is a builder decision (shorten the English subtitle).

## Defect R2 — minor, latent: fan-out record `miss-tr-en.json` still carries the old long title

- Location: `hidden_files/w47/scratch-fanout-ru/miss-tr-en.json:33`
  (`lit` bucket): `"ТУР В ЦИФРАХ　数字看本轮": "ТУР В ЦИФРАХ　The round in numbers"`.
- The other three sync points are correct and mutually consistent (all re-checked
  by me): `content12.py:52` → `f.box("ТУР В ЦИФРАХ　The round", …)`; text.md L25
  `### ТУР В ЦИФРАХ · The round`; `map-en.json` `lit` value
  `ТУР В ЦИФРАХ　The round`; `svg/p1-pervaya.svg` carries `　The round` only;
  `The round in numbers` occurs 0 times in all four live places (grep-verified).
- Why R2 matters: `scratch-fanout-ru/build_map.py:13,28–33` merges
  `miss-tr-<lang>.json` OVER `tm2-<lang>.json` into `map-<lang>.json` (`m[bucket][k]
  = v`, miss-tr wins). `tm2-en.json` does NOT contain this key at all (verified),
  so `miss-tr-en.json` is the SOLE upstream source of the literal. Re-running
  `build_map.py en` + the fan-out would regenerate `map-en.json` with the long
  form and revive the S1 overhang in `content12.py`. FIX-LOG §1's claim ("a
  re-fanout cannot revive the long form") holds for the current `map-en.json`
  file but not for the pipeline that regenerates it.
- Residue audit (complete): `The round in numbers` survives only in
  (i) `miss-tr-en.json:33` [R2, live input]; (ii) `scratch-fanout-ru/en/freeze/
  build-copy/content12.py` + `svg/p1-pervaya.svg` [frozen snapshot copy, not a
  live input — noted, not a defect]; (iii) `content12.py:48–51` comment and
  `WEEKLY-KIT.md:94` [fix history quoted in prose — intentional documentation,
  not live values, not defects].
- Severity: minor, latent — the delivered PDFs are unaffected; the risk fires
  only on a re-fanout. Fix is one value in `miss-tr-en.json` (then `build_map.py`
  regenerates the map identically short — verifiable by re-running it).

## §1. S1 verified fixed (the fix1 defect)

- Identity first (before any other work): print 21,251,086 B
  `9a159cd59f32443eb8d612eb05959ff7af3273d4c3796da0b2b2f6a7f1800b0a`; web
  3,380,694 B `7e465d67a96c3e47aa415cc530160de2df9f9b2d9f923e85366da28b8e263ed5`;
  text.md 62,818 B `5960b7a649a8b50036fefa0b16580a2209bc694ea45fb5377a9ee39d9c1296ee`
  — all three match the FIX-LOG final table (lines 319–321) exactly. The
  intermediate print SHA `023d9fd1…` (FIX-LOG line 19) is an early rebuild
  product, not a deliverable — not used.
- PIL true ink (`gates/s1.log`, per-run, 23pt bold): `ТУР` 556.5–600.5,
  `В` 604.7–620.5, `ЦИФРАХ` 625.4–722.9, `　The round` 726.6–**865.6**. Full title
  ink right **865.6**, box right 961.0, clearance **95.4 px** (was 998.9, −133.3).
  Requirement ink right ≤ 957: PASS with 91.4 px to spare.
- Rendered-pixel arbiter (4× crops from the DELIVERED PDFs): clearance
  **291 render px = 97.0 SVG px**, print and web byte-identical crops
  (`crops/p1-round-crop-print.png` = `crops/p1-round-crop-web.png`, SHA
  `099ba2c6…`), requirement ≥ +5 render px: PASS by a wide margin. Read by eye:
  `ТУР В ЦИФРАХ　The round` ends well inside the cream box (crop in §Evidence).
- Spill sweep (`gates/spill.log`, the shared script): 32 cream boxes, 32 titles
  measured (first-run method), **0 ink escapes, 0 bad titles**, 43 spill-below
  candidates (same count/classified set as proof1/fix1), RESULT: PASS.

## What was verified clean (detail in GATE-LOG.md)

- Mechanical gates, all re-run by me: `run.py` rc=0 TOTAL **150** (A2 50 / B1 76 /
  B2 24; by page 10/18/18/18/18/18/12/38; model words 97), 0 FLOW OVERFLOW /
  HEAD TOO WIDE; scratch-copy rebuild reproduces all 8 shipped SVGs
  byte-identical; occlusion 42 TEXTX / 0 of every other class, adjudicated
  **42/42 CLEAR** on edition assets (core-pointed: 38 CLEAR + 4 UNRESOLVED —
  adjudicator artifact, see Observations); p8 extract **150/150**, compare
  **CLEAN** rc=0, keydiff **[137, 138, 139, 140]**, missing/extra/uncertain empty;
  registry-vs-P8 **149/150** (only Q150, expected ✓); freeze baseline core
  **8/8** rc=0 and edition **8/8** rc=0; freeze diff removed count-sum 850,
  Cyrillic-bearing removed exactly 15 (Q46 `можно` + 14 Morozko words),
  added Cyrillic 0, added CJK 8 all U+3000; `check_core` rc=0, golden BAD 0,
  gloss fails 0; `s11_check` rc=0, FAILURES: none, **P8 min font 9.75 pt**
  (direct PyMuPDF confirms 9.75 on both PDFs, 411 spans <10pt); creambox
  detailed scan 1156 lines, diff vs proof1 log exactly 1 line (the P1 title).
- Print/web text layer: plain pdftotext **57,318 bytes each, byte-identical**;
  layout 111,875 each, byte-identical; character multiset identical overall
  (**30,354** non-whitespace chars) and per page; span multisets identical;
  abutting/intra-char gap diffs max 0.00 pt; D2 6 pins 0.000 pt; D3 `а`→`»`
  −2.193 pt both, italics 16 = 16, D1 straight quotes in both PDFs.
  `verify_mine2` reports 1 FAIL (D3 space) — the script's known finder bug
  (supplement note 2, proof1's own record); corrected direct measurement:
  space char bbox **[1145.576, 1266.762, 1148.108, 1288.725]**, width 2.532 pt,
  byte-identical print/web — exactly proof2's pinned values. D3 fixed.
- Kicker: independent re-measurement (my own method, run-level ink gaps)
  reproduces fix1's list exactly: **[5.0, 5.4, 6.3, 11.8, 8.4, 5.4, 7.2, 9.5, 7.1]**,
  min **5.0 px ≥ 4 — PASS**. Proof1's list could not be reproduced by either
  fix1's or my method (same finding as fix1); the kicker SVG is byte-identical
  to the version proof1 measured.
- 150 questions: text.md (838 lines) read in full by me, every stem/option/key
  hand-checked against the article text; stems (Cyrillic) vs core: **0 Russian
  differences** (the single diff is gloss language, Q46); key parts vs core:
  exactly 5 diffs = Q137–140 (English translation keys, by design) + Q150
  (open task); stem keys vs answer-list keys 0 mismatches; matching inline
  keys 20/20 agree with the answer list; model text **97 words** ✓;
  `___` ×87 = core ×87; dates/weekdays verified against the calendar
  (16 Mon–22 Sun, 6–8 Fri–Sun, 27 Fri Black Friday, 30 Mon Cyber Monday);
  21 goals in round 14 (summed from the P4 results table in the SVG),
  31/29/26 points,
  38+26+18+18=100 chart, 20 working days; golden sentences 8/8 verbatim with
  correct page refs; error clinic 4/4; P4 results table (SVG) confirms all 8
  scores and the 21-goal total.
- D2 (Q25): full phrase `Международный день студента` ×2 in text.md = core ×2;
  Q25 option L187 `25. 17 ноября — День студента (key b · Students' Day b)` ✓.
- D6 (Q20): `желании` ×2 in text.md = core ×2 (L173 stem + L694 key list);
  P8 extract key 20 = registry = `желании` ✓.
- Q73: stem L405 `73. [B1 · fill-in] В прошлом году сделали 14,4 млн ___. —
  key: заказов` and key list L753 `73. заказов — заказ = an order` intact;
  P8 extract key 73 = `заказов` ✓.
- SVG regression vs proof1 backup (`scratch-proof-ru-en2/rerun/svg/`): **only
  p1 differs** (exactly 1 line: the title run `　The round in numbers` →
  `　The round`); p2–p8 byte-identical.
- KIT doc fixes verified: §5 carries the text.md SHA
  `5960b7a6…` (was missing per proof1) and pdftotext **57,318** with a dated
  correction note (57,329 pre-fix, −11 for the shortened title) — the
  supplement's note (57,329 = pre-fix) is consistent with my measurement.
- Fonts (recorded only, not judged): **72 entries print, 72 web**, all emb/sub/
  uni; print embeds NotoSerif/NotoSans/Newsreader/UnifrakturMaguntia (+ CJK
  variants); web embeds Lucerna*-renamed subsets incl. both italic faces.
- Visual: all 8 pages rendered from the DELIVERED print PDF (`fresh/`) and read
  in full; no overflow, overlap, clipping, or missing content except R1
  (invisible at 100%); P8 key complete to Q150; no text crossing the footer line.

## Observations (not defects)

- O1: Narrow run-boundary gaps (space-only SVG run skipped by CairoSVG): same
  class as proof1 O1, now also visible in gloss notes (P3 `биографияbiopic`,
  P5 `календарнаядатаcalendar`, P7 `Профессиональныепраздники` in the golden
  sentences) — positive gaps, readable as two words, byte-identical print/web;
  not re-flagged, same adjudication as proof1/proof2/proof3.
- O2: `check_core` orphan (P7 y553 `”».`) and P1 same-baseline collision (y1712
  `чёрная`) — both known-benign, same as core per KIT; P7 line visually
  complete in the render.
- O3: `___` literal blanks ×87 in text.md = ×87 in core text.md — core-inherited
  template matter, per brief not an edition defect.
- O4: Q51/Q139 British plural ("The national team play", "Russia play
  Venezuela") — internally consistent with the edition's British date format;
  proof1 O4, not flagged.
- O5: Q140 "Happy Students' Day to everyone!" adds "to everyone" — standard
  English greeting equivalent; proof1 O5, not flagged.
- O6: P8 Morozko image skipped by design (keys end col 3 y≈2288.84, condition
  `img_y+250+90=2652 > 2560` in `content8.py`, identical in core); text.md
  keeps the Morozko credit line. Freeze adjudication confirms the 14 removed
  caption words are exactly the core P8 caption block.
- O7: Adjudicator core-pointed run gives **38 CLEAR + 4 UNRESOLVED**, not the
  supplement's "2 UNRESOLVED": the extra two are P5 `смартфоны` and P7 `ЯЗЫК`
  (neighbour English runs exist only in the edition). Same artifact class;
  the edition-pointed run (42/42 CLEAR) is the correct one.
- O8: Freeze "removed distinct 484" is the per-page-summed figure; the global
  distinct count is 451 (same strings removed on several pages). Definition
  note, not a discrepancy — count-sum 850 matches on both definitions.

## Evidence files (scratch-reproof-ru-en1/)

`PROOF-NOTE.md` (this file), `GATE-LOG.md`, `s1_measure.py`,
`kicker_measure.py`, `pdf_title_check.py`, `raster_title_check.py`,
`spill.py`, `verify_mine2.py`, `dump_reg.py`, `adjudicate_ru.py`,
`s11_check.py`, `creambox.py` (simple version, superseded by `creambox2.py`
— detailed version), `gates/` (run.log, render-equivalent SVG SHAs,
occlusion.json/log, adjudication-ed.log, adjudication-core.log,
p8-extract.json/log, p8-compare.json/log, keycheck.log, freeze-std.log,
freeze-ed.log, freeze-diff.json/log, freeze-adjudicate.log, check-core.log,
s11.log, spill.log, s1.log, kicker.log, creambox.log, verify-mine2.log,
d3-space.log, stem-key-compare.log, final-checks.log, pdf-title.log,
fonts-print.log, fonts-web.log, registry.json, svg-prod.sha256,
svg-rebuild.sha256), `crops/` (p1-round-crop-print.png, -web.png,
p6-title-crop-print.png, -web.png — print/web pairs byte-identical),
`text/` (print.txt, web.txt, print-layout.txt, web-layout.txt),
`fresh/` (8 page renders from the delivered print PDF),
`rebuild-copy/` (scratch rebuild sources + registry).


---

# PROOF NOTE — 2026-W47 ru-en, re-proof of the Fix 4 build (text.md L836 only)

- Edition: `2026-w47-ru-en` (Russian target × English readers), Lucerna Weekly VOL.4,
  issue 16–22 November 2026.
- Proofer: independent re-proofread (I did not build this edition). Date: 2026-11-11.
- Scope: full independent proofread of the edition as delivered — all 8 print-PDF
  pages (visual, 110 dpi renders), the full text.md (838 lines), and the web PDF.
  Read-only; no production file modified, no commit/push/lint, no re-render.
  /tmp render intermediates deleted after the read.
- Note: this note is appended to the earlier Fix 2 re-proof note in the same file
  (same scratch dir, reused by the coordinator); the earlier note above is untouched.

## Verdict: (a) ZERO FINDINGS

## SHAs (start = end; nothing changed mid-read)

| file | SHA-256 | size |
|---|---|---|
| 2026-w47-ru-en.text.md | `5dba645578989ed58673b060b6c67e6df844335f82a1ba351012f66e5c9404df` | 62,786 B |
| Lucerna-VOL4-ru-en.pdf (print) | `d12fa6a6bb62dd7af36743c7d2f33d96d27def054e5dcd6fdb288ef3577c06a1` | 21,251,270 B |
| Lucerna-VOL4-ru-en-web.pdf (web) | `0778f40076d6579b6699c9508e886186a2c86500e0216c38c6168d4e270127f4` | 3,380,920 B |

- text.md SHA **matches the required `5dba6455…` exactly** (62,786 B). Gate passed.
- Print SHA **matches KIT §5** (`d12fa6a6…`). Print was not rebuilt by Fix 4, as briefed.
- Web SHA **differs from KIT §5** (`3cd934e0…`, 3,380,903 B) vs on-disk `0778f400…`
  (3,380,920 B, +17 B). Known drift per the Fix 4 record: concurrent webpdf rebuild
  jobs rewrote all 9 ru web PDFs during the apply. KIT-vs-disk mismatch alone is not
  a defect — content verified below; flagged here for the coordinator's KIT-sync wave.
- Web PDF was **stable** across the read (same SHA at start and end) — no DEFERRED
  verdict needed; web check is complete.

## The Fix 4 change (verified)

- text.md L836 reads exactly: `150. ✓ See the model text in section H of this page (97 words)`
- Print P8 answer key Q150 reads byte-identically (text layer + visual): same line.
- Model text word count re-measured independently: **97 words** in text.md
  (`Пример: … Мне нравится такая неделя!`) and the same 97 words on printed P8
  (pdftotext slice = 106 tokens only because column interleaving adds
  `Пример:` + `F СЛОВА НЕДЕЛИ` + `B2` + `Match words and meanings` = 9 extra tokens;
  97 + 9 = 106, reconciled).

## Appendix keys 1–150 vs printed P8 (programmatic + visual)

- text.md appendix contains all keys 1–150, none missing.
- Every appendix key line matches the printed P8 answer key **verbatim**
  (space-tolerant check: 0 diffs), including Q150 ✓ form and the four E-translation
  keys 137–140.
- All 150 inline exercise keys in the body were parsed; all 150 stems were checked
  against their page SVG (first-24-chars test): 134 direct hits; the 16 matching-group
  items (Q39–42, 57–60, 75–78, 141–144) are split across two printed lists, so
  term and meaning were checked separately — all 16 terms and all 16 meanings present
  on the correct page with correct pairings.
- Exercise answers spot-verified against the articles for correctness (not just
  presence): Q20 `желании` (prepositional after о), Q25–28 b/d/c/a, Q41–42 c/a,
  Q57–60 b/a/c/d, Q75–78 d/b/a/c, Q65/66/67/68/69 (27 Nov / 16–30 Nov / 13 Nov–2 Dec /
  30 Nov / since 2013), Q83–87 (2 / 5 / B / 26 / 18), Q97–100 (поэтому / а / а / или),
  Q113–120, Q121–128, Q129–136 (Masha passage), Q137–140, Q141–149 — all correct.

## Page-by-page notes (print PDF, visual read)

- **P1** — Clean. Lead `14-Й ТУР СЫГРАН!`, stats box `ТУР В ЦИФРАХ The round` inside
  its cream box (Fix 2 holds), word of the week `«чёрная пятница»` italic with the
  space intact (D3 holds), quiz 7–10 correct, photo + caption + CC0 credit fine.
  No overflow/overlap/clipping.
- **P2** — Clean. Students' Day / Ded Moroz dates and weather words consistent;
  exercises 11–28 all present and correct.
- **P3** — Clean. Five premieres, 19 Nov; exercises 29–46 present; `«Бумажный тигр»`
  Cannes-2026, `«Увидеть всё»` = Elizabeth Holmes — as written, consistent.
- **P4** — Clean. All 8 round-14 results in the table match P1 (Krasnodar–CSKA 4:2,
  Zenit–Rostov 2:2, Dynamo–Fakel 2:1, Lokomotiv–Rubin 0:1, Baltika–Dynamo Mx 0:1);
  VOL.3 correction box present; exercises 47–64 correct.
- **P5** — Clean. Band subtitle `"Black Friday": sales from 16 November` with
  straight quotes (D1 holds); sale dates box consistent with the article;
  exercises 65–82 correct.
- **P6** — Clean. Day strip weekdays correct (16 пн … 22 вс); practice chart
  38+26+18+18 = 100% and labelled practice data; `ЗА И ПРОТИВ FOR & AGAINST`
  inside its box (Fix 3 holds); `В ноябре 20 рабочих дней и 10 выходных` verified
  correct for November 2026 (9 weekend days + 4 Nov holiday); exercises 83–100.
- **P7** — Clean. Three level columns, error clinic all four corrections correct
  (с + instrumental, на + prepositional, 21 гол, с 19 ноября genitive), word box
  `распродажа`, readers' corner honestly labelled editorial example with the VOL.5
  carry-over, 8 golden sentences all quoted verbatim from their cited pages
  (P1×2, P2, P3, P4, P5, P6×2), Pushkin/Kiprensky 1827 caption correct,
  VOL.5 teaser (Mother's Day 29 Nov = last Sunday of Nov 2026 ✓).
- **P8** — Clean. All sections A–H present; model text 97 words as counted;
  answer key complete 1–150, arranged by page; no Morozko image (skipped by the
  build's own condition, per KIT — not a defect).

## Content / fact checks

- Calendar: 16 Nov 2026 = Monday, 27 Nov = Friday (Black Friday), 30 Nov = Monday
  (Cyber Monday) — all as printed. 17 Nov Students' Day, 18 Nov Ded Moroz birthday,
  25 Jan Татьянин день, 22 Nov Psychologists' Day — consistent throughout.
- English explanations read correctly throughout; Russian source text correct;
  no tofu, no clipped text, no overlap observed on any page.

## Web PDF check

- pdftotext print vs web: **byte-identical, 57,316 bytes, `diff` 0**; per-page byte
  counts identical on all 8 pages.
- Web P1 and P8 rendered and read visually: identical layout/content to print.
  Pixel diff print-vs-web: P8 only 67 px; P1 ~247k px, localised to the photo band
  (y2000–2800, JPEG recompression in the web build) and masthead blackletter
  antialiasing (y200–400) — rasterisation-level only, no content difference.
  D2 (7 spots) and D3 (italic space) show no regression: text layer identical.

## Observations (not findings)

- Narrow word spaces where a Cyrillic run meets the next run render tight enough
  that pdftotext merges them (e.g. P1 `метеорологическаязима`, P2
  `Профессиональныепраздники`, Note boxes `поздравитьto`, `успеховsuccess`). The
  space element is present in the SVG source; measured on P2 at 300 dpi the ink gap
  is ~21 px (~5 pt) — a real space, same class as the KIT-known narrow-space ruling
  (cf. earlier note O1 in this file). Not flagged as a defect.
- text.md exercise line 150 (body, not appendix) still carries the old
  `(Open task; model text below)` parenthetical in its key field — that is the
  exercise-body line, outside the Fix 4 scope (appendix L836 only); not a defect.
- text.md `— СТРАНИЦА ? —` separator and the trailing «Морозко» credit line are
  the core exporter's format (per KIT known rulings); not defects.

## Findings

None. **(a) ZERO FINDINGS.**
