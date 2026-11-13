# GATE-LOG — 2026-W47 ru-ko proof1 (independent mechanical gates, all re-run)

Edition: `production/2026-w47/2026-w47-ru-ko/` · VOL.4 · 2026-11-11
Python: `~/workspace/weekly-git/tools/venv/bin/python`. Creambox: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py` (md5 ee7a55d8b2057cf4ad42a97bb1197383 — verified). All logs in this scratch dir. Nothing in the edition dir was modified.

## §0 Identity + probe

- Probe: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; scratch probe file written OK.
- Disk SHA: print PDF 22,002,774 B `4e450e65…055ca0`; web PDF 3,474,892 B `797af4e6…984f0`; text.md 65,002 B `a1cbef36…87f99`. **All three match the task.** Sizes are as on disk.
- KIT discrepancy (not a defect): KIT (`WEEKLY-KIT.md`) §5 says text.md is 58,811 bytes; disk says 65,002 (SHA still matches the task). KIT also says web PDF 58,554 pdftotext bytes / 26,441 chars each — my pdftotext counts differ (print 33,706 chars, web 33,753 chars). KIT's numbers are stale / different-method, not defects.
- Edition dir is untracked in git (`?? production/2026-w47/2026-w47-ru-ko/`).

## §1 Occlusion audit — 42/42 CLEAR

- Tool: `tools/occlusion_audit.py svg/`; selftest OK (all 6 planted classes fired, clean controls silent). Result **42 flags, all TEXTX, 0 COVER/LINEX/FOOTER/EDGE/BOXTITLE** — exactly matching KIT's count. Logs: `occlusion.log`, `occlusion.json`.
- Adjudication (a bounding-box-overlap flag is not ink contact; the audit measures boxes):
  - Row-wise light-gap test (`occ-gap.txt`): for each flag, per row in the overlap's y-range, the longest light run inside the overlap x-interval. 36 flags CLEAR (min light gap 1–4px; #42 P8 has 0 dark pixels in the intersection at all).
  - 6 flags the gap test called "TOUCH-ROWS" were adjudicated by 3× visual crops (`occ-flag6.png`): #12 P2 `студента`+`.` (normal punctuation, hair gap), #30 P6 `сбивается`+`.`, #31 P6 `Планируйте`+`:`, #33 P7 band `ЯЗЫК`+`언어` (clear gap between К and 언), #38 P7 `!»`+`студента`, #41 P8 band `ОТВЕТЫ`+`테스트와 답` (clear gap between Ы and 테). The "touch" readings are an artifact: the overlap interval cuts through a vertical glyph stem, so no light gap can exist inside the interval itself. All 6 CLEAR on pixels.
  - Band-title flags #32 P6 (`?　연습용 자료` vs `НЕДЕЛЕ`, 3.3×21.8px), #33 P7, #41 P8 are the Cyrillic-title + full-width-space + Korean-subtitle construction; PIL ink boxes for the CJK run start a few px left of where CairoSVG places the glyphs. Pixels show a clear gap in every case.
- Contact-sheet attempt (`occ-sheet1..11.png`) is superseded — broken layout (overflow, tofu labels). The gap test + targeted crops are the evidence.

## §2 Creambox full scan — clean (1 false positive, true-ink clear)

- Canonical `creambox.py`, all 8 SVGs (`creambox-all.log`, 1154 lines). P7 toolbox summary: **3 boxes, min inside clearance +11.9, min desc-clear +5.9** (positive).
- Only ONE inside-only negative desc-clear in the whole edition: P2 box y=795 bottom=1159.0, last baseline 1154.0, desc-clear −1.0, text `즈에게 한 문장.` — true-ink re-measurement (via `occlusion_audit.ink_box`, same PIL method as the audit) gave ink bottom 1156.0 vs box bottom 1159.0 → **clear +3.0px**; the −1.0 was the 0.30em heuristic overestimating Hangul (no descenders). Not a defect.
- No below-window whole-line spills (min below-window offset +28.0; the +12..+18 spill class is absent).

## §3 P8 compare — CLEAN; keydiff [137–140] adjudicated

- `tools/p8.py compare --core-p8 core-ru/svg/p8-test.svg --edition-p8 <edition>/svg/p8-test.svg --total 150`: rc=0, **CLEAN**, 150 noted both sides, missing=[], extra=0, **keydiff=[137,138,139,140]** (`p8compare.log/.json`). P8 extract: 150/150 (`p8extract-ed.log/.json`).
- Keydiff content (core keys are Chinese; edition keys are the correct Korean translations of the Russian stems):
  - 137: core `11月17日星期二，大学生节。` → edition `11월 17일 화요일, 대학생의 날.` ✓
  - 138: core `包裹要追踪、领取并检查。` → edition `소포는 추적하고, 찾아가고, 확인해야 합니다.` ✓
  - 139: core `星期二俄罗斯队对阵委内瑞拉队。` → edition `화요일 러시아는 베네수엘라와 맞붙습니다.` ✓
  - 140: core `祝大家大学生节快乐！` → edition `모두 대학생의 날 축하합니다!` ✓
  - Core keys verified independently via `p8.py extract` on `core-ru/svg/p8-test.svg` (`p8extract-core.json`, 150/150).

## §4 Freeze — diff + baseline 8/8

- `tools/freeze.py diff --core-svg core-ru/svg --edition-svg <edition>/svg`: rc=0. Per-page added/removed strings: P1 +21/−21, P2 +38/−37, P3 +28/−27, P4 +26/−28, P5 +26/−27, P6 +32/−54, P7 +48/−58, P8 +735/−315; total added CJK 2,861 (`freeze-diff.log/.json`, `worddiff.txt`, `freeze-analysis.txt`, `freeze-cyr.txt`).
- Word-level diff shows NO Cyrillic content removed except legitimate items: footer furniture (core `LUCERNA RUSSIAN WEEKLY` → Korean footer), P6 practice-data label (Russian → Korean disclosure, Korean text verified present at P6 y=1582), P7 band subtitle `Три уровня, три темы` → Korean `세 수준, 세 주제`, P2 `родина`→`роди`+`나` and P7 `синоптики`→`시`+`ноптики` (defects D1a/D1b), P8 band subtitle `Большой тест недели: все ответы` → Korean (verified present at P8 y=168).
- `tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out <scratch>/freeze-base`: rc=0, **8/8 SVGs byte-identical**, core integrity confirmed (`freeze-base.log`, `freeze-base/`).
- Method note (not a defect): `tools/freeze.py` has only `baseline`/`diff` subcommands; there is no `freeze_direct` subcommand, as the task anticipated.

## §5 Print/web text layer

- pdftotext both PDFs: 8 pages each, 1462.5×2025 pts. Print 58,507 B / 33,706 chars; web 58,554 B / 33,753 chars. Character multiset identical EXCEPT whitespace (web +41 spaces, +6 newlines — pdftotext segmentation noise) and the D5 line-206 difference. Both non-empty on all pages.
- Web PDF has **0 italic fonts** vs print's 2 (`Newsreader16pt-Italic`, `NotoSerif-MediumItalic`) — see PROOF-NOTE D5. All other text is identical.

## §6 P8 min font — 9.75pt (SOP floor, not a defect)

- PyMuPDF on the print PDF: P8 minimum font size **9.75pt** (`Newsreader16pt-Regular`) — exactly the SOP §1.1 floor. KIT's 9.75pt claim independently confirmed. At the allowed minimum, not a defect.

## §7 Curly quotes — only the intentional P7 pair

- U+201C/U+201D/U+2019 scan of all 8 SVGs: only P7 has 1 pair — `«на “чёрной пятнице”».` at y=552.64 — the task-noted intentional exception. Zero straight quotes anywhere. PASS.

## §8 Boxtitle / horizontal overflow — P1/P3/P5 clean; P2 D-option overflows (D2)

- P1 boxtitle horizontal check (three methods): (i) PIL true-ink right-edge scan of every P1 text node — max ink-right 1862.0 (exactly the designed right margin; footer page-number and one note line); (ii) PDF span check — P1's widest span `ГОДА` ends 1397.7pt (=1863.6px), but the pixel scan shows no P1 ink past x=1862, so that is span-bbox padding; (iii) 200dpi-equivalent pixel scan of all 8 cards for dark pixels past x=1862 (excluding footer band y>2596): **P1, P3–P8 clean; only P2 has ink past the margin** (D2).
- P1 cream-box titles: all first-line and max-inside ink-right clearances positive (min +18.2px, numbers box; right-column boxes +21.9 to +30.2px).
- P3/P5 right-column cream boxes: true-ink clearances huge — P3 +68.3/+68.1, P5 +68.4.
- Mixed-script sweep (joins same-baseline nodes, flags tokens mixing Cyrillic + Hangul): edition 15 hits, core 0. Triage: 13 join artifacts (masthead Korean + Russian, stem + `N.빈칸 채우기` tags, Cyrillic `а` cited inside Korean notes at P8 Q98/99 — legitimate bilingual citation); 2 real defects (D1a/D1b). Single-node token sweep found nothing because the corruption is split across two `<text>` nodes.

## §9 Wrap sweep — 6 mid-word Korean splits (D3); everything else is a word boundary

- Method: SVG line-boundary analysis, column-aware (`wrap-sweep3.txt` + variant `wrap-sweep4.txt`, `p3-gloss.txt`). For every pair of consecutive lines in the same column (y-gap 15–45px) where both contain Hangul, the boundary fragments were checked against the source strings in `content*.py`: a join that appears in the source as one word (no space) is a mid-word split.
- Found (all in-source-word=True): P1 원고, P2 편집부에, P2 모로즈에게, P3 동화, P3 채우세요, P7 편집부 — see PROOF-NOTE D3. All confirmed in SVG nodes and on the rendered cards.
- Legitimate boundaries (in-source-word=False): P1 `끝났다`/`제15라운드는`, P2 `роди나`/`고향`, P4 `поправка`/`정정`, P6 chart title/disclosure, P7 `약속한다`/`данным`, `진눈깨비`/`ледяной`, `프로모코드`/`할인`, P8 key-line boundaries (separate entries, not wraps) and the P8 H-instruction break after `(97` (space boundary inside a parenthetical — awkward but not a mid-word split).
- The variant sweep (either-side Hangul, digit/Latin-adjacent splits) found no further mid-word splits.

## §10 Keycheck — 150/150

- `keycheck-150.json`: 150 entries, per-question hand check. Inline keys (text.md exercises) = Answers section = P8 printed keys; **0 mismatches** (Q150's initial flag was a parsing artifact — open writing question, P8 prints the ✓ marker; see entry note).
- Counts verified by parsing text.md + P8 extract: pages 10/18/18/18/18/18/12/38; levels A2 50 / B1 76 / B2 24 (matching-group levels from range headers: 25–28 A2, 39–42/57–60/75–78 B1, 141–144 B2); types 문장 완성 54 / 객관식 55 / 단어 짝짓기 20 / 문장 만들기 12 / 문장 바꾸기 4 / 번역 4 / 쓰기 1. Model text verified 97 words.
- Q30 entry flagged with the 로키/록키 note (PROOF-NOTE D4). Q8/Q124 CSKA entries noted (see §11).

## §11 Items judged non-defects

- **P8 Morozko illustration + caption absent** from P8 SVG/card: core P8 has caption `«Морозко»: иллюстрация Ивана Билибина, 1932 год…` at y=2486–2560; edition P8 has neither image nor caption. KIT says skipped by the build's own condition, same as W46 ru-ko — accepted as conditional-by-design; text.md retains the trailing credit line `*«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя сказка — к ноябрю.*` (matches core exporter format). No dangling reference remains.
- **Latin `CSKA` in Korean answer notes** (Q8, Q124: `크라스노다르가 CSKA를 4:2로 이겼다`; text.md 4 occurrences) while other clubs use Hangul: NOT a defect — W46 ru-ko text.md uses the same Latin CSKA in a Korean note (`13라운드: CSKA 0-0 오렌부르크`, 2 occurrences); established practice.
- **P2 desc-clear −1.0** → true ink clear +3.0px (§2). Not a defect.
- **P7 y=693 `진눈깨비;распродажа`** — join artifact only: nodes `진눈깨비;` (x=364.9) and `распродажа` (x=538.5), ~60px gap. Clear.
- **P2 Yuon credit** `Картина: Константин Юон — общественное достояние` (y=1526) — nominative after colon, grammatically correct; caption `картина Константина Юона` (y=1473) correct. Same in core.
- **P7 Pushkin credit** `Картина: Орест Кипренский — общественное достояние (Wikimedia Commons)` (y=1557.3, verified in SVG) — colon present, correct.
- **P1 masthead subtitle spacing in pdftotext** — pdftotext drops spaces there in BOTH PDFs; evidence it is a span/segmentation artifact, not a rendering defect: the print PDF itself has spans like `Когданачинается` (y=1797) that pdftotext renders as `Когда начинается`. Same behavior in both artifacts; the rendered cards show normal spacing.
- **Q62 key `будет`** ("15-й тур будет 20–22 ноября") — slightly colloquial but acceptable Russian.
- **P8 H-instruction line break after `(97`** — at a space boundary, not mid-word (§9).
- 8 golden sentences verified present verbatim in their cited articles with correct page refs (P1×2, P2×1, P3×1, P4×1, P5×1, P6×2).

## §12 External facts checked

- Weekdays via `TZ='Asia/Seoul' date -d`: 2026-11-16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 27 Fri, 29 Sun, 30 Mon, 12 Thu, 8 Sun — all consistent with the issue's claims (round 14 Fri 6–Sun 8 Nov; Students' Day Tue 17; Ded Moroz Wed 18; five premieres Thu 19; round 15 Fri 20–Sun 22; Black Friday calendar date Fri 27; Cyber Monday Mon 30; national-team matches Thu 12 and Tue 17).
- P4 results table read off the card (8 matches, 6–8 Nov) matches Q52–60 keys exactly; round-15 fixtures (20–22 Nov) consistent; top-5 table consistent with the lead.
- W46 ru-ko comparison was not possible for SVG/cards (W46 ru-ko keeps no `svg/` or `cards/` — only sources + logs); the CSKA precedent was checked against W46 text.md instead.
- No web research was needed for the D4 (Rocky→록키) call: standard Korean rendering of the film *Rocky* is 록키; 로키 is "Loki".

## §13 Scratch files (evidence)

`probe.txt`, `occlusion.log`, `occlusion.json`, `occ-gap.txt`, `occ-flag6.png`, `occ-adjudicate.txt` (superseded naive test), `occ-sheet1..11.png` (superseded broken layout), `p8compare.log/.json`, `p8extract-ed.log/.json`, `p8extract-core.json`, `creambox-all.log`, `freeze-diff.log/.json`, `freeze-cyr.txt`, `freeze-analysis.txt`, `freeze-base.log`, `freeze-base/`, `worddiff.txt`, `context.txt`, `context2.txt`, `sinop.txt`, `d1-verify.txt`, `mixed-sweep.txt`, `ink-measure.txt`, `ink-measure2.txt`, `p2-student.txt`, `pixel-scan.txt`, `print.txt`, `web.txt`, `p2-d-row.png`, `p3-gloss.txt`, `wrap-sweep.txt`, `wrap-sweep2.txt`, `wrap-sweep3.txt`, `wrap-sweep4.txt`, `keycheck-build.txt`, `keycheck-report.txt`, `italic-print.png`, `italic-web.png`, `keycheck-150.json`, `PROOF-NOTE.md`, `GATE-LOG.md`, `tmp/`.
