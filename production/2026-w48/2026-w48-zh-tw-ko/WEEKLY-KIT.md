# WEEKLY-KIT — 2026-W48 zh-tw-ko (Korean explanations)

## 1. Identity

- Slug: `2026-w48-zh-tw-ko` — Traditional Chinese target text, Korean explanation layer.
- Issue: 2026-11-23..2026-11-29, VOL.5, 8 pages, 150 exercises.
- Levels: A2 44 / B1 74 / B2 32. Pages: 10/18/18/18/18/18/12/38.
- Types: 單選 67 · 完成句子 54 · 配對 16 · 完形單選 12 · 寫作 1. Model text 136 characters.
- Source: `production/2026-w48/core-zh-tw/` (fourth-round independent proofread,
  zero findings). Target-language text frozen; only the explanation layer is
  in Korean. Fonts for the Korean reader layer: Noto Serif CJK KR / Noto Sans
  CJK KR (webpdf subset families confirm both KR faces embedded; no tofu).

## 2. Build

- Mechanism: `scratch-fanout-zh-tw/apply_zhtw.py ko` (copy core, AST-span
  literal replacement from `map-ko.json` + KR branch in the applier) +
  `run.py`. Translation table: `map-ko.json` (36,529 B) built from the W47
  zh-tw-ko harvest + hand-written `miss-ko-a.json` / `miss-ko-b.json` + ko
  meta (page line `제{n}면／전체 {total}면`, gloss `참고｜`, export title
  `VOL.5 · 중국어 번체 텍스트 · 한국어 해설`).
- `run.py` exit 0, TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE
  (ko-run2.log, 2026-11-19 06:58 UTC).
- Render under the W48 render lock (acquired 2026-11-19T10:02:35Z, released
  10:05:45Z; available memory 3,543 MB at acquire, 3,158 MB at render,
  2,854 MB at webpdf — all above the 500 MB gate). All 8 cards re-rendered
  from the final SVGs: p1–p4 were already current (06:59 UTC), p5–p8 were
  stale 2026-11-17 09:04 cards predating the P6 fix and were regenerated.
- **Fix1 (2026-11-19 ~10:36–10:37 UTC, proof round 1 D1 + D2 — see §7):**
  8 source-only edits (content12.py ×3, content34.py ×1, content56.py ×3,
  content7.py ×1; full FIX record in `scratch-fanout-zh-tw/ko-fix-log.md`),
  run.py RC=0 TOTAL 150, occlusion 0 flags, render under the lock
  (acquired 10:36:03Z, owner.txt agent=zh-tw-ko-fix1, released 10:37Z after
  export; available memory 1,779 MB at acquire, 1,826 MB at render,
  1,732 MB at webpdf, 1,669 MB at export — all above the 500 MB gate).
  Print PDF 10,656,453 B, web PDF 2,060,406 B, text.md 58,940 B (see §6).
- Reproduction: copy `core-zh-tw` whole, run `apply_zhtw.py ko`, run
  `run.py`, render under the lock, export with title
  `VOL.5 · 중국어 번체 텍스트 · 한국어 해설`.
- NOTE: re-running `apply_zhtw.py` re-copies core-zh-tw over the edition dir
  and deletes `WEEKLY-KIT.md` — rewrite the KIT after the final apply.
  (Not re-run in this session; the edition was continued from the on-disk
  SVGs after the P6 fix.)

## 3. Contents (same as core-zh-tw)

- P1 lead: 63rd Golden Horse Awards winners preview (ceremony Sun Nov 22,
  18:30, Taipei Music Center; no winner named — full report in VOL.6) +
  Wei Chuan Dragons championship parade (Sun Nov 22, 14:00, Tianmu → Taipei Dome).
  P2 Xiaoxue + Black Friday + New Taipei Christmas market × esports finals.
  P3 winning films in cinemas + deTour 2026 + Charlie musical + steel festival
  closing recap. P4 parade deep report + U-Sport points. P5 Hong Kong Christmas
  (WinterFest, Disneyland, Jazz Festival, esports). P6 deep read Nov 23–29,
  five big dates (timeline chart). P7 language focus + error clinic + frame
  一…就… + readers' corner (editor's example + deferral disclosure, bilingual
  Traditional Chinese + Korean) + phrases of the week + VOL.6 teaser. P8 test
  + answers + writing 《我的一天：11月29日》.
- Trend sources, images, captions: unchanged from core-zh-tw (see core KIT).

## 4. Findings fixed during this build (self-check)

1. P6 occlusion (only defect found in this edition's audit): the timeline
   Korean note ran into the right-column 「看活動三問」 box
   (ko-occlusion1.log, 3 TEXTX flags on p6-deep.svg). Fix: shortened the
   single line in `content56.py:154` to
   `타임라인: MegaBox 11월 23일, 재즈 11월 24일, 블랙프라이데이 11월 27일,
   e스포츠 결승전 11월 28일, 디자인 페스티벌 11월 29일.`
   — all five dates kept, no fact changed. Re-ran run.py + occlusion audit:
   0 flags (ko-occlusion2.log, selftest OK, rc=0); the shortened line is
   confirmed on the rendered P6 card, ending well clear of the right box.
2. Stale cards: p5–p8 cards predated the P6 fix (2026-11-17 09:04); all 8
   cards re-rendered from the final SVGs in this session (ko-render1.log).
3. P8 keys were claimed 150/150 + CLEAN by the previous builder with no log
   on disk; re-ran p8.py extract + compare in this session and logged it
   (ko-p8.log): extract 150/150, compare CLEAN, keydiff=[].

## 5. Gates (final run, ko-gates-final.log — superseded by fix1, ko-fix-gates.log) — ALL PASS (11/11)

- checks.py PASS (phrases 2×, Simplified-only scan empty, P4 bars + P6 dots exact).
- occlusion 0 flags, selftest rc=0.
- p8 extract 150/150; p8 compare CLEAN, keydiff=[].
- freeze repro 8/8 (direct sha256; repro OUT rewritten to repro dir).
- print/web text layers 8/8 pages, posdiff=0 msdiff=0 (P1 168, P2 238, P3 288,
  P4 225, P5 275, P6 235, P7 269, P8 926 words each — P2/P5/P7 each −1 token
  vs the pre-fix build, matching the one-word shortenings in fix1).
- pdftotext_nonempty: print 51,388 B / web 51,389 B (1-byte difference is the
  single extra '\n' in the web PDF, same pattern as the core).
- P8 full-page min font 9.75pt (print and web).
- P8 chips core = edition {A2 8, B1 20, B2 10}.
- §1.1 SVG audit: off-palette none, no old gold, stroked_rects 0, VOL.5 10 = core 10, paper fills 8.
- leftover_simplified: 0 hits (OpenCC s2t set 2,606 chars; 6 core-allowlisted).
- leftover_english: 0 map keys remaining, 0 shared-ASCII-long strings.
- boxtitle: 56 titles, 1,537 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal.
- Line-start punctuation scan (proofer's method, PyMuPDF on the print PDF):
  0 places (ko-fix-linestarts.log); pre-fix count was 7.

## 6. Artifacts

- Print PDF `Lucerna-VOL5-ZH-TW-KO.pdf`: 10,656,453 bytes,
  SHA-256 `a8f92a1566d9d506ce63b9e391297819a7c5c3326a2ca8520b42b0c5546543aa`,
  8 pages, 1462.5 × 2025 pt.
- Web PDF `Lucerna-VOL5-ZH-TW-KO-web.pdf`: 2,060,406 bytes,
  SHA-256 `3f2b28ddee829252d848d05a09d947193475421cb4731f2eec4bd977c9fb8346`,
  8 pages, 51,389 text bytes, < 7 MB.
- Text `2026-w48-zh-tw-ko.text.md`: 58,940 bytes,
  SHA-256 `fcfe293fc24a138549211a408e55980c039419e537aa8c36bd481d51a5536910`
  (exported from SVG source, never from PDF).
- ABSTRACT.txt (Korean, one line, no ASCII double quotes): 398 bytes.

## 7. Proofread record

- Core-zh-tw: fourth-round independent proofread, zero findings.
- This edition: builder self-check zero findings —
  8/8 cards visually verified from the print PDF (P1–P8, no overflow /
  overlap / footer collision / tofu; P6 timeline fix confirmed on the card);
  150 keys re-verified item by item (p8.py extract 150/150 + compare CLEAN
  vs core, plus a text.md answer-head cross-check: 95 letter keys and 54
  fill-in/writing answers, zero diffs vs core, incl. 113–150);
  full text.md + SVG text self-read (11,799 lines scanned: 0 kana,
  0 Cyrillic, 0 long Latin sentences, 0 U+FFFD; 1,998 Hangul lines;
  the only ASCII double quotes are the frozen deTour theme
  `"BETTER, NOT PERFECT"`, identical in the core).
- Observations, not defects: P5 「耶誕城電競時間表」 box ends
  `每次5分鐘；看完比賽去看燈` — identical in the core text.md (frozen
  target text). P7 item 109 reuses the P6 item 83 stem — identical in the
  core (frozen). The P1 note renders the host as `Will Or(Ko Wai-lam)` —
  same name as the core's `Will Or (Ko Wai-lam)` (frozen proper noun).
- Independent proofread round 1 (2026-11-19, `scratch-proof-fanout-zh-tw-ko/PROOF-REPORT.md`):
  2 light defects, no medium/major; gates 11/11, 150 keys CLEAN, 8/8 cards clean.
  D1 — P1 Notes gloss `Will Or(Ko Wai-lam)` / `「再見江湖」(Farewell, Jianghu)` missing the
  space before the parenthesis (core and all sibling editions have it).
  D2 — 7 line-initial punctuation spots in the Korean explanation layer (PyMuPDF scan).
- Fix1 (this build, 2026-11-19): D1 — two spaces added in content12.py:44, nothing else
  on that line (rendered gap measured 4.4 px = exactly one 18 px space; `Will Or (Ko Wai-lam)`
  one node with the space inside). D2 — one word shortened per spot, meaning/facts/dates/
  numbers/keys untouched: P1 word box `수상자 명단이 발표되는 것을…` → `수상자 명단 발표를…`;
  P6 three-questions `골라서` → `골라`; P2 gloss `5분씩` → `5분`; P4 byline `타이베이시 정부,`
  → `타이베이시,`; P5 gloss `49일 동안` → `49일간`; P6 gloss `재즈 페스티벌은` → `재즈 축제는`;
  P7 clinic `10일 동안` → `10일간`. Root cause noted in ko-fix-log.md: `svglib.wrap`'s
  kinsoku table covers only full-width punctuation, not ASCII `.`/`,`, so the ASCII
  closers could land line-initial; the wrap table itself was NOT changed (out of scope).
  Untouched by design: `영화(入圍/頒獎)`-style attached brackets, and the P5 ex-66 note
  `Christmas Town은 49일 동안 열려요.` (a different sentence from the D2-5 gloss).
- Fix1 self-check (zero findings): run.py RC=0 TOTAL 150, checks PASS, occlusion 0 flags
  (selftest OK), gates 11/11 ALL PASS (ko-fix-gates.log), p8 extract 150/150 + compare
  CLEAN + per-key JSON diff 0 (ko-fix-p8.log, ko-fix-p8keys.log), freeze 8/8, print/web
  text multiset diff 0, P8 min font 9.75pt both PDFs, line-start scan 0 places
  (ko-fix-linestarts.log). 8/8 cards visually verified from the print PDF + 200 DPI
  crops of all 8 fixed spots (ko-fix-qc/): no overflow/overlap/footer collision/tofu;
  P6 timeline fix and P3 D6 state unchanged. Full text.md self-read (ko-fix-selfread.log):
  11,795 lines, 0 kana, 0 Cyrillic, 0 U+FFFD, 1,996 Hangul lines, only ASCII quotes
  the frozen deTour theme `"BETTER, NOT PERFECT"`, 0 TODO/FIXME/待補/佔位.
- Independent proofread round 2: pending coordinator assignment.
