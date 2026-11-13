# GATE LOG — 2026-W47 ru-en, Round-1 Independent Proofread

All gates self-run by the proofer. Interpreter: `~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0 — same as the build; system `python3` has Pillow 10.2.0, hence the interpreter matters per the ko-family lesson). KIT records the build used `tools/venv/bin/python`.

## 0. Startup probes — PASSED (2026-11-11 02:28 EST / 07:28 UTC)

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`, RC=0
- Wrote probe file `scratch-proof-ru-en1/PROBE.txt` ("probe-ok ru-en1 2026-11-11T07:28:00Z") — OK

## 1. Identity — MATCHES KIT exactly

- `sha256sum Lucerna-VOL4-ru-en.pdf` → `023d9fd12bdca276751400fb13f7f399d645c267a09ba1897eb0e598d52f2e3a`, 21,245,420 bytes, 8 pages (PyMuPDF)
- `sha256sum Lucerna-VOL4-ru-en-web.pdf` → `fab0fc44736ecb169a1cc3932a8e85db2504f694f02e84d45f3063435327493d`, 3,341,934 bytes, 8 pages, < 7 MB
- `2026-w47-ru-en.text.md`: 56,604 bytes per KIT; 690 lines read in full

## 2. Fresh visual renders — 8/8 pages read, web P1/P8 read

- Re-rendered all 8 SVGs with CairoSVG via `tools/venv/bin/python` into `fresh/` (975×1350 PNGs; builder's `cards/` not trusted). All pages read in full: no overflow, overlap, clipping, or missing content.
- Web P1/P8 rendered from the web PDF at 150 dpi (`fresh/web-p1.png`, `fresh/web-p8.png`, 3047×4219) and read in full; layout identical to print except D2 (P1 headline gap, visible in the small render as "14- й").
- Zoom crops in `crops/` (4× from print PDF unless noted): P1 'субботу,' comma; P8 'ОТВЕТЫ' band; P7 'ЯЗЫК' band; P3 'биография:'; P5 'смартфоны,'; P2 'студента.'; P6 'PRACTICE DATA' header; P5 band subtitle; P7 orphan line; P1 footer; P8 H model text; `crop-headline-print.png` / `crop-headline-web.png` (D2); `crop-p4head-print.png` / `crop-p4head-web.png` (D2). All clean except D1/D2.

## 3. run.py rerun (scratch copy, original untouched) — exit 0, zero overflow

- Command: copied edition dir to `scratch-proof-ru-en1/rerun/`, ran `run.py` there. Log: `rerun-log.txt`.
- Result: exit 0, **0 FLOW OVERFLOW / HEAD TOO WIDE warnings**, TOTAL 150, levels A2 50 / B1 76 / B2 24, by-page distribution matches KIT, by-type matches, model words 97.
- Rerun SVGs byte-identical 8/8 to shipped SVGs.

## 4. check_core.py self-run — GOLDEN 8, golden BAD 0, gloss fails 0

- Result: GOLDEN 8, golden BAD 0, gloss fails 0, P8 SVG text 10,571 chars, 1 orphan line-start (P7 y553 `”».` — O1, false positive, verified complete line), 1 same-baseline collision (P1 y1712 italic «чёрная пятница» — O2, same as core).
- Each golden sentence occurs exactly twice (source page + P7 list); page refs on P7 correct (P1×2, P2×1, P3×1, P4×1, P5×1, P6×2). (My first naive coordinate-sorted join falsely showed misses — columns interleaved; document-order join + check_core confirmed all 8.)

## 5. p8 extract + compare — 150/150, CLEAN

- `p8.py extract` on rendered P8: **150/150** noted. All 150 printed key VALUES equal `.text.md` key values; all 150 full key lines (value + note) verified present in rendered P8 via whitespace-insensitive substring check; all 8 "— СТРАНИЦА N —" separators present. Key 150 prints "✓ See the model text…" by design.
- `p8.py compare` vs core-ru P8 SVG: CLEAN, missing=[], extra=0, keydiff=[137, 138, 139, 140] only — the four E translation keys, each verified as the intended English translation:
  - 137 "Tuesday 17 November, Students' Day."
  - 138 "A parcel must be tracked, collected and checked."
  - 139 "On Tuesday Russia play Venezuela."
  - 140 "Happy Students' Day to everyone!"

## 6. freeze — 8/8 byte-identical

- `freeze` baseline run: RC=0, **8/8 SVGs byte-identical** (repointed files: none; shipped core SVGs unchanged).
- Direct SHA-256 comparison (own run.py rerun in scratch copy): 8/8 MATCH.

## 7. Print/web text layer — identical character multiset

- `pdftotext` bytes: print 57,153 / web 57,200, both > 0.
- Non-whitespace chars: 30,293 each; character multiset identical; per-page identical (5354 / 5784 / 4644 / 5593 / 4930 / 4609 / 6044 / 12442).
- The 43-space + 4-newline raw difference is pdftotext segmentation whitespace only. (`print.txt`, `web.txt`)

## 8. Occlusion audit — 42 TEXTX, 0 real flags

- `--selftest` OK (planted classes fired, clean controls silent).
- Real run RC=0: **42 TEXTX, 0 LINEX, 0 COVER, 0 FOOTER, 0 EDGE, 0 BOXTITLE** (per-page: P1 10, P7 8, P4 7, P2 6, P6 4, P3 3, P5 2, P8 2). (`occlusion.json`)
- Adjudicated all 42 independently (`adjudicate-mine.txt`): pixel-gap measurement on print-PDF renders gave 33 CLEAR (gap ≥ 2 px); the remaining 9 verified visually clear at 4× zoom (the 2 band-title "TOUCH?" cases — P8 'ОТВЕТЫ' 8.0×35.5 px, P7 'ЯЗЫК' 3.8×35.5 px — were artifacts of the pixel test counting the dark-green band background as ink; the punctuation cases P1 'субботу,' P2 'студента.' P3 'биография:' P5 'смартфоны,' P6 'сбивается.' P7 'прессы,' show clear gaps).
- All 42 are the known systematic false-positive class (audit overestimates the right edge of a Cyrillic run by a few px). **0 real flags.**

## 9. P8 min font — 9.75 pt (meets ≥ 9.75 pt)

- PyMuPDF on print PDF P8: 387 spans at 9.75 pt; next size 9.98 pt.

## 10. U+2019 regression — 0; curly double quotes — P5 only (D1)

- U+2019 total across all 8 SVGs: **0**. U+2018: 0. Straight apostrophes: 21 (all fine; P2-band apostrophe advance measured 3.75 pt in Noto Sans CJK SC — normal, not full-width).
- U+201C/201D: P5 ×1 pair, P7 ×1 pair only. P7 pair is in Newsreader (proportional, fine). P5 pair is D1: `“`/`”` advance 13.50 pt = 1 em at 13.5 pt (full-width); ink gap ≈ 9.8 pt before `:`; normal word space in the same line 3.02 pt; widest Latin letter `m` 12.50 pt.

## 11. CJK / ban-word / VOL scans

- CJK scan of visible SVG text: **0 CJK chars** on all 8 pages (only CJK is `三色蛾` inside the moth `<title>` metadata, same as core, per KIT).
- Ban-word scan of visible SVG text (43,371 chars): **0 hits** for TODO/FIXME/XXX/lorem/placeholder/TBD/占位/SOP/proofread/Kaggle/cover/???/@@@. (`banwords.txt`)
- VOL inventory: VOL.4 ×9 (masthead + 8 footers), VOL.3 ×1 (P4 correction sentence — expected), VOL.5 ×6 (teasers/disclosure — expected). No misprint.
- Footer (zoom-verified): `Lucerna　RUSSIAN WEEKLY VOL.4　Russian text　English explanations` with full-width-space (U+3000) separators, "Page N of 8" on all pages. §1.1 compliant.
- ABSTRACT.txt: one English line, 355 bytes, no ASCII double quotes.

## 12. Badges — 0 mismatches

- 130 individual exercise chips paired (badge rect fill → level text → number) against the registry: all levels match. Per-page: P1 A2 9/B1 1; P2 A2 10/B1 4 (+group); P3 A2 7/B1 7 (+group); P4 A2 2/B1 12 (+group); P5 A2 6/B1 8 (+group); P6 B2 14/B1 4; P7 A2 4/B1 4/B2 4; P8 A2 8/B1 24/B2 2 (+group). (`badges-check.txt`, `fonts-badges.txt`)
- The 20 "missing" chip numbers are the 5 matching sections, each covered by ONE correct group chip: P2 "25–28." A2, P3 "39–42." B1, P4 "57–60." B1, P5 "75–78." B1, P8 "141–144." B2. Total badges 135, 0 level mismatches. Fills: A2 `#5c6e30`, B1 `#46581f`, B2 `#37402f`.

## 13. Registry distribution — matches KIT

- TOTAL 150; by page P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38; by level A2 50, B1 76, B2 24; by type fill-in 54, multiple choice 42, matching 20, sentence building 12, rewrite 4, cloze 13, translation 4, writing 1.
- Model text ("Моя неделя 16–22 ноября") = 97 words by whitespace split (hyphen-split would be 99); rendered P8 H text verified word-for-word against `.text.md`.

## 14. Web-vs-print geometry drift scan (D2)

- Method: PyMuPDF `get_text('dict')`; matched lines by (rounded y0, joined text); compared consecutive abutting span pairs (print A.x1 == B.x0) in the web PDF.
- Result: 1,349 abutting pairs; web gaps > 0.5 pt at only 7 spots: P4 24 pt `14-`|`й тур` 2.6 pt; P1 15 pt `1. 14-`|`й тур` 2.2 pt; P4 13.5 pt ` все восемь результа`|`+` 1.9 pt; P1 15 pt `3. «`|`Чёрная пятница` 1.1 pt; P5 24 pt `«`|`Чёрная пятница` 0.9 pt; P7 16.12 pt `«`|… 0.6 pt ×2. All other pairs ≤ 0.5 pt (mostly 0.0–0.1 pt).
- P1 headline 39.8 pt pair measured directly (spans have different bbox y0, so the line scan did not pair them): `14-` box x1 128.6 (web) vs 133.0 (print); next span x0 133.0 both → 4.4 pt box gap, 2.75 pt ink gap at 4×. P4 heading 24 pt: `14-` x1 103.8 (web) vs 106.5 (print) → 2.6 pt gap. Both confirmed visually (crops).
- Masthead wordmark control: masthead ink width print 1330.7 pt vs web 1330.0 pt — identical; no wordmark defect.

## 15. Fact spot-checks (public sources, 2026-11-11)

- Weekdays: 6 Nov 2026 Fri, 7 Sat, 8 Sun, 12 Thu, 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 27 Fri (Black Friday), 29 Sun (Mother's Day), 30 Mon (Cyber Monday) — all consistent. (2026-11-11 is Wednesday.)
- "В ноябре 20 рабочих дней и 10 выходных": correct for Russia — Nov 2026 has 21 weekdays minus 4 Nov Unity Day (public holiday) = 20 working, 10 non-working.
- RPL round 14 (Forbes 9 Nov 2026; Sports.ru; Sport-Express 8 Nov 2026; 86.ru 11 Nov 2026): Краснодар–ЦСКА 4:2 (Кордоба 16', Кисляк 35', Батчи 40', Уткин 74', Кордоба 82', Глебов 90+1'), Зенит–Ростов 2:2 (Комаров 83'), Динамо–Факел 2:1 (winner 90+1'), Спартак–Акрон 2:1, Локомотив–Рубин 0:1, Ахмат–Родина 1:0, Балтика–Динамо Мх 0:1 (8 Nov), Крылья–Оренбург 2:0; 8 matches, 21 goals total (1+3+1+6+2+3+4+1); Zenit & Dynamo 31 pts joint first, Spartak 29, Krasnodar & CSKA 26 each (7W 5D 2L); round 15 starts 20 Nov (Ростов–Крылья Советов). All match the edition.
- Film slate: "Бумажный тигр" = James Gray's Paper Tiger, crime drama, world premiere in competition at 2026 Cannes (16 May 2026), US release 13 Nov 2026 (Wikipedia/press); "Увидеть всё" = A24's You Can See Everything, documentary about Elizabeth Holmes (Theranos founder), dirs. Nathan Fielder & Lance Oppenheim, Telluride premiere 6 Sep 2026, US theatrical 16 Oct 2026; "Рокки — это я" = I Play Rocky, dir. Peter Farrelly, Stallone biopic, US release 6 Nov 2026 (limited) / 20 Nov wide; "Дедмобиль" = real family comedy starring Yuri Stoyanov, dir. Vladimir Kott — release-date sources conflict (Karo Premier/Mosfilm 23 Oct 2026 announcement: 19 Nov; August festival piece: wide release 26 Nov; piracy-listing sites: 20 Nov); edition follows the latest distributor announcement (19 Nov); "Колотун и Волшебное Королевство" = real, Russian release 19 Nov 2026 (6+); "Лес" = real, adaptation of Svetlana Tyulbasheva's bestselling novel, dir. Gamlet Dulyan, wide Russian release 12 Nov 2026; "Лиля" = real biopic of Lili Brik (Mayakovsky's muse), dir. Vera Storozheva, Russian release 12 Nov 2026.
- 1946 Prague decision for International Students' Day; Kiprensky Pushkin portrait 1827; Simonyan centenary; 1912 Olympics photo — consistent with general knowledge.
- Ozon "14.4m orders on 11 Nov 2025" not independently verified; left as core fact, not flagged.
