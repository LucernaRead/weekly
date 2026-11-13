# PROOF NOTE — 2026-W47 ru-en, re-fanout re-proofread (proof1 of the rebuilt edition)

- Edition: `2026-w47-ru-en` (Russian target × English readers), Lucerna Weekly VOL.4,
  issue 16–22 November 2026. Rebuilt whole from finalized core-ru fix1 (`f11854bf`).
- Proofer: independent re-proofread (complete re-check, not a delta review — the old
  proof1 was voided by the core D2 fix). Check only; no production file modified
  (see §7), no commit, no push.
- Date: 2026-11-11. Scratch:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-en2/`
- Read first: repo `SOP.md` (§8 + §1.1), `AGENTS.md`,
  `scratch-refanout-ru/FANOUT-REPORT-ru.md`,
  `scratch-refanout-ru/records/en/RECORD.md`,
  `scratch-proof-ru-en1/PROOF-NOTE.md` (old proof1),
  `scratch-proof-ru-en3/PROOF-NOTE.md` (proof3, zero-defect on the voided build).

## Verdict: (b) — 1 DEFECT FOUND, CANNOT FINALIZE

One minor defect, on the front page, found by the spill sweep the brief requires
(occlusion BOXTITLE does not cover unbordered cream boxes). Everything else in
this round is clean, including all previously known defects (old-proof1 D1/D2,
proof2 D3) — all verified fixed by independent re-measurement below. Severity is
minor (text fully legible, no collision, no content error), but it is a visible
front-page layout fault of exactly the class proof1 treated as blocking
(two minor spacing defects → "NOT zero-issue"), so the verdict is (b).

## Defect S1 — minor: P1 "ТУР В ЦИФРАХ" box title overhangs its cream box by 37.9 px

- Location: P1, middle column, stats box. Source: `content12.py:48`
  `f.box("ТУР В ЦИФРАХ　The round in numbers", [...])`; box drawn by
  `Flow.box()` (`bslib4.py:183` rect at column width, `:186` title drawn with
  no width/fit check).
- Original (rendered): the header line reads `ТУР В ЦИФРАХ　The round in numbers`
  and the English subtitle sticks out past the right edge of its own cream
  background into the white gutter, toward the right column.
- Should be: the whole header line fits inside its box, as the same header does
  in core-ru and as all 31 other cream-box titles in this edition do.
- Evidence (all three legs):
  (a) Source + measurement (PIL true ink, `occlusion_audit.ink_box`, same fonts
      as the canonical audit — `gates/spill.log`, `gates/spill-p1.log`):
      cream rect `p1-pervaya.svg` x=538.5 y=1203.735 w=422.5 h=380.0, no stroke;
      title run `　The round in numbers` (Noto Sans CJK SC, 23 px, baseline
      y=1240.735) ink right = **998.9** vs box right = 538.5 + 422.5 = **961.0**,
      overhang **37.9 px = 28.4 pt**; title ink starts x=556.5 (box x + pad 18),
      ink width 442.4 px > box inner width 386.5 px. My sweep measured all 32
      cream boxes: this is the ONLY ink-escape among all contained runs, and
      0 of 32 box titles have negative clearance — every other title fits.
  (b) Render evidence: `crops/p1-roundnumbers.png` (3× crop from the shipped
      print PDF) — the word "numbers" ends visibly outside the cream panel on
      white background; same crop from the web PDF is pixel-identical
      (`crops/p1-roundnumbers-web.png`, same SHA-256
      `ab4490ed…9add`). Both PDFs affected.
  (c) Provenance: the geometry is identical in `backup-old/` (same rect, same
      ink right 998.9) — it predates the re-fanout and was missed because no
      earlier round ran this sweep; in core-ru the same box carries
      `ТУР В ЦИФРАХ　数字看本轮`, ink right 864.6, inside the box. So this is a
      fan-out-introduced overhang (English subtitle longer than the Chinese
      one), not a core defect. No text–text collision: the nearest right-column
      text (`В 14-м туре…`, x=989–1052) sits at y≈1183–1197, above the title
      band y≈1222–1241; the overhang lands in empty gutter.
- Severity: minor — legible, no overlap, front-page cosmetic fault. Fix is a
  builder decision (shorten the English subtitle, e.g. `Round in numbers`, or
  widen the box); not mine to make.

## What was verified fixed (regression vs old proof1/proof2/proof3)

- Old proof1 D1 (P5 band subtitle curly quotes in CJK font): FIXED. SVG
  `p5-molodezh.svg` now carries `　"Black Friday": sales from 16 November`
  (straight quotes, Noto Sans CJK SC 18 px). Measured on the print PDF
  (PyMuPDF rawdict): closing `"` advance 6.399 pt, gap `"`→`:` **0.0 pt**
  (was 13.50 pt advance + 9.8 pt gap); identical in web. 3× crops
  `crops/p5-band-print.png` / `p5-band-web.png` pixel-identical, read by eye:
  closing quote tight on `:`. Proof: `gates/narrow-gaps.log`.
- Old proof1 D2 (web-only `14-й` gaps, 7 spots): FIXED, all 7 re-pinned by
  direct lookup (`verify_mine2.py`, `gates/verify-mine2.log`): web x1 == print
  x1, diff **0.000 pt** at P1 headline (133.018), P4 heading (106.464),
  P1 contents `1. 14-` (1138.695), P4 band-sub (1008.743), P1 contents `3. «`
  (1122.225), P5 title `«` (80.112); P7 `«` ×2 covered by the full scans
  (max diff 0.00 pt over all pairs).
- Proof2 D3 (web P1 WORD OF THE WEEK `«чёрная пятница»`): FIXED, all three
  facets re-measured: space char bbox byte-identical print/web
  `[1145.576, 1266.762, 1148.108, 1288.725]`, width 2.532 pt, gap 0.00 pt;
  `а`→`»` gap −2.193 pt in both; web embeds `LucernaNotoSerif-Italic` +
  `LucernaNewsreader-Italic`, P1 italic chars 16 = print. 3× crops
  `crops/p1-wordweek-print.png` / `-web.png` pixel-identical, read by eye:
  clear space, `»` tight. (Note: my first verify script had a finder bug —
  it looked for consecutive `я`,`п` chars and missed the space char between
  them; corrected measurement above supersedes it, values identical to
  proof3's pinned numbers.)
- D1 (core fix1, 4 KEEP strings): all landed. Text.md L459 `УЧЕБНЫЕ ДАННЫЕ`,
  L504 `Три уровня, три темы`, L596 `Большой тест недели + все ответы`;
  disclaimer (string 2) absent from text.md by design, present in P6 SVG;
  all 4 KEEP values present in SVG (concatenated-`<text>` check,
  `gates/d1-svg.log`). Full phrase `Международный день студента` ×2 in
  text.md = core ×2; Q25 option is `День студента` (text.md L187).
- D2 (Q25): option shortened, key b unchanged; P2 matching set now reads
  `b. День студента` on one line (visual P2 read).
- D6 (Q20): key `желании` — text.md ×2 (L173 stem + L694 key list), P8
  extract key 20 = core `ru-p8.json:177` = `желании`.
- Kicker: 9 double spaces landed (`content12.py:18`); PIL ink gaps
  `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`, min **5.9 px ≥ 4**;
  P1 kicker row element-identical to core. (`gates/kicker.log`)

## Observations (not defects)

- O1: Narrow run-boundary gaps (space-only SVG run skipped by CairoSVG):
  P2 Q15 `Профессиональныепраздники` ink gap 1.548 pt, P5
  `маркетплейсахскидки` 1.818 pt — positive gaps, readable as two words,
  byte-identical print/web (same values both PDFs). Same class proof2/proof3
  adjudicated not-a-defect with the same evidence; not re-flagged.
  Counter-cases with a real space char present in both PDFs: P7 header
  `СЛОВА ПОКУПОК`, P1 Q3 `Сборная играет`, P6 Q99 `остаются дома`, P7 gloss
  `синоптики обещают`. (`gates/narrow-gaps.log`)
- O2: `check_core` orphan (P7 y553 `”».`) and P1 same-baseline collision
  (y1712 `чёрная`) — both known-benign, same as core per KIT; P7 line visually
  complete in the render.
- O3: `___` literal blanks ×87 in text.md = ×87 in core text.md — core-inherited
  template matter, per brief not an edition defect; no per-edition fix.
- O4: Q51/Q139 British plural ("The national team play", "Russia play
  Venezuela") — internally consistent with the edition's British date format;
  proof1 O4, not flagged.
- O5: Q140 "Happy Students' Day to everyone!" adds "to everyone" — standard
  English greeting equivalent; proof1 O5, not flagged.
- O6: P8 Morozko image skipped by design (keys end col 3 y≈2288.84, condition
  `img_y+250+90=2652 > 2560` in `content8.py`, identical in core); text.md
  keeps the Morozko credit line. Freeze adjudication confirms the 14 removed
  caption words are exactly the core P8 y≥2450 caption block.
- O7: KIT documentation nits (NOT edition defects, for the coordinator):
  (i) KIT §5 records print/web SHAs + bytes (verified correct) but no
  `.text.md` SHA-256 (bytes 62,829 listed; SHA `1e06ec55…` lives only in
  `scratch-refanout-ru/records/en/RECORD.md`); (ii) KIT §5/§7 still quote
  `pdftotext` 57,149 bytes for the current build — re-measured plain pdftotext
  is **57,329 bytes both PDFs, byte-identical** (the 57,149 figure is from the
  pre-refanout print PDF; the refanout added D1 Russian strings).

## What was verified clean (summary; detail in GATE-LOG.md)

- Visual: all 8 pages re-rendered from SVG by me (CairoSVG, 975×1350,
  `fresh/`) and read in full; web P1/P5/P8 crops read. No overflow, overlap,
  clipping, or missing content except S1. No text crossing the footer line;
  P8 key complete to Q150.
- 150 questions: text.md (838 lines) read in full; every stem/option/key
  hand-checked against the article text; registry-vs-P8-extract 149/150
  (only Q150 differs: registry key is the open-task note, P8 prints ✓ —
  expected); stem keys vs text.md answer-list keys 0 mismatches (1–149);
  model text 97 words (80–100 required); p8 extract 150/150, compare CLEAN,
  keydiff vs core exactly [137, 138, 139, 140].
- Content spot-checks: dates/weekdays match the calendar (16 Mon–22 Sun Nov
  2026; 6–8 Nov Fri–Sun; 27 Nov Fri Black Friday; 30 Nov Mon Cyber Monday);
  21 goals, 31/29/26 points, 38+26+18+18=100 chart, 20 working days;
  golden sentences 8/8 verbatim with correct page refs; error clinic 4/4.
- Rerun reproducibility: edition rebuilt from a scratch copy (`rerun/`,
  `run.py` exit 0, TOTAL 150, 0 FLOW OVERFLOW / HEAD TOO WIDE) — all 8 SVGs
  byte-identical to shipped.
- Freeze: standard core baseline 8/8 + edition-internal baseline 8/8;
  freeze diff removed distinct 484 / count-sum 850, Cyrillic-bearing removed
  exactly 15 (Q46 `можно` + 14 Morozko caption words), unexplained 0, added
  Cyrillic 0, added CJK only U+3000 ×8.
- Occlusion: 42 TEXTX, 0 LINEX, adjudicated 42/42 CLEAR; flag set identical
  to proof1/proof3 except the one P6 D1 run re-segmentation
  (`?　PRACTICE DATA` → `?　`, same line, D1 change).
- Creambox: no negative inside-only clearance; 95 BELOW-WINDOW lines, all
  classified (offsets +28/+32/+34/+37 — next-block titles, weather-word
  boxes, day-strip legend, quick-quiz header); scan byte-identical to the
  backup-old scan (0 diff lines).
- Spill sweep (new): 32 cream boxes, 32 titles true-ink measured (0 bad);
  43 spill-below candidates all in the already-classified by-design set;
  exactly 1 ink-escape = S1 above.
- Print/web: pdftotext -layout byte-identical (111,886 B each); plain
  pdftotext byte-identical (57,329 B each); fitz multiset identical overall
  (30,363 chars) and per page; span-text multisets identical; abutting-pair
  and intra-char gap diffs max 0.00 pt; D1/D2/D3 pinned checks all pass.
- §1.1: s11_check rc=0, FAILURES: none; P8 min font 9.75 pt; paper
  #fbfaf6, badges A2/B1/B2 colours, foot VOL.4 + full-width space, VOL.3 ×1
  (P4 correction), masthead 196 px, band 46 px, left margin 88.0.
- SVG zero real CJK (only U+3000: 21/16/13/16/13/16/13/15 per page).
- D5 fonts (recorded only, not judged): print embeds NotoSerif/NotoSans/
  Newsreader/UnifrakturMaguntia (+ CJK variants), all embedded/subset/
  Unicode; web embeds Lucerna*-renamed subsets incl. both italic faces.
- Regression vs backup-old: text.md diff exactly 6 line pairs
  (L173 D6 key, L187 D2, L459/504/596 D1, L694 D6 key list), nothing else;
  source diffs only in content12.py (kicker + D6 + D2 + fix comments),
  content56.py (D1 title + disclaimer), content7.py (D1 P7 subtitle),
  content8.py (D1 P8 subtitle); SVG diffs only p1 (kicker), p2 (D2),
  p6/p7/p8 (D1 + D6 key). KEEP: proof1 D1 straight-quote fix survives
  (p5 SVG unchanged vs backup); proof2 D3 italic fix survives (verified
  above). No hand patch lost; no unexplained change.
- ABSTRACT.txt: 355 bytes, one English line, no ASCII double quotes,
  VOL.4 + A2–B2 + 150 exercises + real topics.

## Evidence files (scratch-proof-ru-en2/)

`PROOF-NOTE.md` (this file), `GATE-LOG.md`, `gates/` (check-core.log,
p8-extract/​compare.json+log, s11.log, freeze-std/int/diff logs +
freeze-diff.json, freeze-adjudicate.log, occlusion.json/log,
occlusion-compare.log, adjudication.log, creambox.log,
creambox-backup.log, creambox-analysis.log, d1d2d6-kicker.log, d1-svg.log,
kicker.log, keycheck.log, rerun.log, dump-reg.log, narrow-gaps.log,
final-checks.log, final-checks2.log, spill.log, spill-p1.log,
verify-mine.log (v1, killed as too slow), verify-mine2.log +
verify-mine2.py),
`fresh/` (8 self-rendered PNGs), `text/` (print.txt, web.txt),
`crops/` (p5-band, p1-headline, p1-wordweek, p1-roundnumbers print+web),
`rerun/` (rebuilt copy + registry.json), `spill.py`, `verify_mine.py`.
