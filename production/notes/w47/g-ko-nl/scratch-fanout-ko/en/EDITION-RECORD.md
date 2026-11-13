# EDITION RECORD — 2026-W47 ko-en (run 2, rebuild; 2026-11-11)

- Slug: `2026-w47-ko-en` (target ko, reader English). Core: `core-ko` run 10.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-en.json`, `gen-map-en.py`); apply log `apply-en2.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-EN.pdf` — **45,262,664 bytes**, SHA-256 `571699d675bd31f2cc656698df05908e6843517b8cc28b5e0b849a0f6f48cc18`
- Web PDF: `Lucerna-VOL4-KO-EN-web.pdf` — **4,013,441 bytes** (< 7 MB), SHA-256 `02203d2490905b9d863c935ede7b378eb87bd00ce9bf5069ab8bbc2f109d4323`
- Text export: `2026-w47-ko-en.text.md` — 26,389 bytes, 332 items, SHA-256 `7a8f6cef233eb3fe0ef19d1dc7cafed339d2dad740373d8e58e858632ced845d`
- `ABSTRACT.txt` — 305 bytes, SHA-256 `1187194316bea8381ec48d359fd41698d6e18e8e4dfa090889df92724fabc812`
- 8 SVGs in `svg/` (run 2 hashes in `en/sha-en-run2.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 2) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38 | `en/build-en-run2.log` |
| boxtitle width | 8/8 titles ≤ 386.5px | `apply-en2.log` (inline) |
| U+2019 scan (8 SVGs, run 2) | 0 | re-run on run-2 SVGs (measured inline) |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `en/occlusion-en2.json` / `en/occlusion-en2.log` |
| p8.py extract | 150/150 noted | `en/p8-extract-en.log`, `en/p8-en.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `en/p8-compare-en.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer 3 vs 2 full-width spaces; P1 offset by band sub) | `en/freeze-diff-en.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `en/freeze-en.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `en/check-en.log` |
| check_gloss (scratch copy) | gloss fails 0 | `en/check-en.log` |
| print/web text layers | byte-identical, 50,698 bytes each | `en/textlayer-diff-en.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `en/keycheck-en.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `en/style11-en.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `en/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **Box titles wider than the 386.5px inner width** (found by occlusion audit, run 1: 2 TEXTX flags — P1 calendar item 2 vs numbers-box title, P5 youth-numbers title vs feature prose; P2/P3 titles spilled onto empty space, same defect class). Shortened, measured with `text_w` (23px bold sans): P1 numbers box → `In numbers` (336.5px); P2 shopping box → `Shopping list` (330.1px); P3 kimchi-day box → `To know` (329.0px); P5 youth numbers box → `Youth numbers` (358.4px). Rebuilt as run 2; occlusion re-run 0 flags. New tool: `boxtitle-ko.py` (asserts all box titles ≤ 386.5px; run after every apply).
2. **Discarded render (run 1)**: the first `render.py` run was started before the box-title fix and died mid-run when re-apply deleted the svg dir (`URLError: No such file ... p4-seupocheu.svg`); its output was discarded, never used. Lesson: never re-apply while a render is running. Re-rendered cleanly after run 2 (rc 0).

## Adjudicated (not defects — inherited from core or by design)

- P8 match-item notes end with the option letter repeated (`25. d — … won d`, `26. a — … Nov 22 a`): the letter is in the SOURCE note literal itself, core's own convention (`김장비용=四口之家199,456韩元 d` in core-ko); the en map translated the note text and kept the letter.
- #43/#123/#124 note "Weatheri forecast": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(open task — model text below)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (en): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure replaces `lcn`; `lko`/`lcn2` lines + render lines removed, W46 ko-en precedent).
- text.md 332 items vs core 333: `textmd.py`'s `is_prose` drops the bare 3-letter Latin word "All" (P1 contents 8면 row level); the SVG/PDF render "All" correctly (visible on the P1 render). Export quirk, not a content gap.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- P8 answer-note person names: only personal name is 민준 (Minjun, section C protagonist + P8 #129 note) — standard Revised Romanization, consistent within the edition; no sumo-style romaji issue (ja-family class does not apply here). Team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings.

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (English) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | fill-in | 1 | Nov 18 is D-1 | OK |
| 2 | 1 | fill-in | 김장 | Kimchi season is in full swing | OK |
| 3 | 1 | fill-in | 19 | The CSAT is on Thursday, Nov 19 | OK |
| 4 | 1 | fill-in | 3 | Nov 16 is D-3 | OK |
| 5 | 1 | fill-in | 4승 1패 | Samsung beat kt 4–1 | OK |
| 6 | 1 | fill-in | 11 | Cancelled-seat sign-up starts Nov 11 | OK |
| 7 | 1 | multiple choice | A | Nov 18 is D-1 | OK |
| 8 | 1 | multiple choice | A | Kimjang costs fell 9.0% from last year | OK |
| 9 | 1 | multiple choice | A | Kimchi Day is Sunday, Nov 22 | OK |
| 10 | 1 | multiple choice | A | Samsung won the Korean Series | OK |
| 11 | 2 | multiple choice | A | 20 cabbages: 54,980 won | OK |
| 12 | 2 | multiple choice | A | Kimjang costs fell 9.0% | OK |
| 13 | 2 | multiple choice | A | Kimchi Day is Sunday, Nov 22 | OK |
| 14 | 2 | multiple choice | A | The History exam is Saturday, Nov 28 | OK |
| 15 | 2 | multiple choice | A | The WiKim Festival is Friday, Nov 20 | OK |
| 16 | 2 | fill-in | 한창 | Kimchi season is in full swing | OK |
| 17 | 2 | fill-in | 22 | Kimchi Day is Nov 22 | OK |
| 18 | 2 | fill-in | 54,980 | 20 cabbages: 54,980 won | OK |
| 19 | 2 | fill-in | 토 | The History exam is on Saturday | OK |
| 20 | 2 | fill-in | 배추 | Costs fell because cabbage is cheaper | OK |
| 21 | 2 | fill-in | 199,456 | Kimjang for four: 199,456 won | OK |
| 22 | 2 | fill-in | 54,980 | 20 cabbages: 54,980 won | OK |
| 23 | 2 | fill-in | 26.5 | 20 cabbages, down 26.5% from last year | OK |
| 24 | 2 | fill-in | 13 | Cancelled-seat sign-up: Nov 11–13 | OK |
| 25 | 2 | matching | d | 김장비용 = kimjang for four, 199,456 won d | OK |
| 26 | 2 | matching | a | 김치의 날 = Nov 22 a | OK |
| 27 | 2 | matching | c | 위킴 페스티벌 = Nov 20 in Seoul c | OK |
| 28 | 2 | matching | b | 한능검 = short for the History exam b | OK |
| 29 | 3 | multiple choice | A | Kimchi Day is Nov 22 | OK |
| 30 | 3 | multiple choice | B | 22 means kimchi's 22 benefits | OK |
| 31 | 3 | multiple choice | A | The WiKim Festival is Friday, Nov 20 | OK |
| 32 | 3 | multiple choice | B | Naejangsan: Forestry Service forecast peak Nov 4 | OK |
| 33 | 3 | multiple choice | A | The Forestry Service counts 50% of leaves | OK |
| 34 | 3 | fill-in | 절정 | The loveliest leaves are called 절정 | OK |
| 35 | 3 | fill-in | 예보 | Forecast dates differ from observed dates | OK |
| 36 | 3 | fill-in | 관측 | Actually observed Oct 16 | OK |
| 37 | 3 | fill-in | 김치의 날 | Nov 22 is Kimchi Day | OK |
| 38 | 3 | fill-in | 발효 | Kimchi is fermented food | OK |
| 39 | 3 | fill-in | 22 | Kimchi has 22 benefits | OK |
| 40 | 3 | fill-in | 11 | Naejangsan: Weatheri forecast Nov 11 | OK |
| 41 | 3 | fill-in | 4 | Naejangsan: Forestry Service forecast Nov 4 | OK |
| 42 | 3 | fill-in | 20 | The WiKim Festival is Nov 20 | OK |
| 43 | 3 | matching | b | 내장산 = Weatheri forecast Nov 11 b | OK |
| 44 | 3 | matching | a | 월출산 = Forestry Service forecast Nov 9 a | OK |
| 45 | 3 | matching | d | 두륜산 = Forestry Service forecast Nov 11 d | OK |
| 46 | 3 | matching | c | 설악산 = actually observed Oct 16 c | OK |
| 47 | 4 | multiple choice | A | Samsung won the Korean Series | OK |
| 48 | 4 | multiple choice | C | The series ended 4–1 | OK |
| 49 | 4 | multiple choice | B | Game 5, Nov 8 in Daegu: Samsung 12–1 | OK |
| 50 | 4 | multiple choice | A | Game 1: kt won 8–7 | OK |
| 51 | 4 | multiple choice | B | Samsung's first title in 12 years | OK |
| 52 | 4 | fill-in | 4승 1패 | Samsung beat kt 4–1 | OK |
| 53 | 4 | fill-in | 수원 | Games 1 and 2 were in Suwon | OK |
| 54 | 4 | fill-in | 12대 1 | Game 5: Samsung won 12–1 | OK |
| 55 | 4 | fill-in | 12 | Samsung won again after 12 years | OK |
| 56 | 4 | fill-in | 4연승 | Samsung won four straight after one loss | OK |
| 57 | 4 | transformation | 삼성이 kt wiz를 이겼어요. | 이기다: past 이겼어요 | OK |
| 58 | 4 | transformation | 1차전이 수원에서 열렸어요. | 열리다: past 열렸어요 | OK |
| 59 | 4 | transformation | 한국시리즈가 끝났어요. | 끝나다: past 끝났어요 | OK |
| 60 | 4 | transformation | 삼성이 5차전에서 이겼어요. | 이기다: past 이겼어요 | OK |
| 61 | 4 | matching | c | 준플레이오프 = KIA won three straight c | OK |
| 62 | 4 | matching | d | 플레이오프 = Samsung won 3–2 d | OK |
| 63 | 4 | matching | a | 한국시리즈 = Samsung won 4–1 a | OK |
| 64 | 4 | matching | b | K리그1 = Seoul won early b | OK |
| 65 | 5 | multiple choice | A | The advance assembly is Wednesday, Nov 18 | OK |
| 66 | 5 | multiple choice | B | The CSAT starts at 8:40 | OK |
| 67 | 5 | multiple choice | A | This year's candidates: 551,864 | OK |
| 68 | 5 | multiple choice | B | Scores come out Friday, Dec 11 | OK |
| 69 | 5 | multiple choice | A | Be in your room by 8:10 on exam day | OK |
| 70 | 5 | fill-in | 예비소집 | Pick up your ticket at the advance assembly | OK |
| 71 | 5 | fill-in | 수험표 | Pick up your ticket and check your test site | OK |
| 72 | 5 | fill-in | 2,310 | 2,310 fewer candidates than last year | OK |
| 73 | 5 | fill-in | 성적 | Scores come out Dec 11 | OK |
| 74 | 5 | fill-in | 김치의 날 | Nov 22 is Kimchi Day | OK |
| 75 | 5 | fill-in | 551,864 | This year's candidates: 551,864 | OK |
| 76 | 5 | fill-in | 1,312 | Test sites nationwide: 1,312 | OK |
| 77 | 5 | fill-in | 85 | 85 test districts nationwide | OK |
| 78 | 5 | fill-in | 10 | On exam day, offices start at 10:00 | OK |
| 79 | 5 | sentence building | 수험생은 열심히 공부해요. | Word order: subject + adverb + verb | OK |
| 80 | 5 | sentence building | 우리는 수험생을 응원해요. | Subject + object + verb | OK |
| 81 | 5 | sentence building | 비행기는 듣기 시간에 뜨지 않아요. | No flights during the listening test | OK |
| 82 | 5 | sentence building | 친구는 김치를 나눠 줘요. | A friend shares kimchi | OK |
| 83 | 6 | multiple choice | B | This week the Korean Series has a result | OK |
| 84 | 6 | multiple choice | A | Nov 9 survey: kimjang costs 199,456 won | OK |
| 85 | 6 | multiple choice | B | The forecast leaf dates have passed | OK |
| 86 | 6 | multiple choice | C | CSAT scores come out Dec 11 | OK |
| 87 | 6 | multiple choice | A | Last week the Series was only a schedule | OK |
| 88 | 6 | multiple choice | A | Game 1: kt won 8–7 | OK |
| 89 | 6 | multiple choice | B | The weather service observes about 80% | OK |
| 90 | 6 | multiple choice | A | One cabbage, Oct 16: 5,557 won | OK |
| 91 | 6 | multiple choice | A | The kimjang survey's reference date is Nov 9 | OK |
| 92 | 6 | multiple choice | A | This year's candidates: 551,864 | OK |
| 93 | 6 | fill-in | 발표 | A published schedule can change | OK |
| 94 | 6 | fill-in | 결과 | Results come only after the games | OK |
| 95 | 6 | fill-in | 기준 | Dates differ because the criteria differ | OK |
| 96 | 6 | fill-in | 날짜 | When you read the news, check the date first | OK |
| 97 | 6 | true/false | 틀리다 | The special measures apply only on Nov 19 | OK |
| 98 | 6 | true/false | 맞다 | Samsung won the title 4–1 | OK |
| 99 | 6 | true/false | 틀리다 | Forecast dates are not observed dates | OK |
| 100 | 6 | true/false | 맞다 | Scores come out Dec 11 | OK |
| 101 | 7 | fill-in | 김장 | Making kimchi for winter = 김장 | OK |
| 102 | 7 | multiple choice | A | Kimchi Day is Nov 22 | OK |
| 103 | 7 | fill-in | 절임배추 | Cabbage salted in advance | OK |
| 104 | 7 | multiple choice | A | The seasoning has salted shrimp | OK |
| 105 | 7 | fill-in | D-1 | Nov 18 is D-1 | OK |
| 106 | 7 | multiple choice | B | D-3 = Nov 16 | OK |
| 107 | 7 | fill-in | 데이 | Nov 19 is D-day | OK |
| 108 | 7 | multiple choice | A | D-1 means the exam is tomorrow | OK |
| 109 | 7 | fill-in | 기준 | The dates differ because the criteria differ (page 3) | OK |
| 110 | 7 | multiple choice | A | The weather service observes about 80% | OK |
| 111 | 7 | fill-in | 결과 | Results come only after the games | OK |
| 112 | 7 | multiple choice | B | Tell announcements and results apart | OK |
| 113 | 8 | cloze | A | Kimchi Day is Sunday, Nov 22 | OK |
| 114 | 8 | cloze | A | The CSAT is on Thursday, Nov 19 | OK |
| 115 | 8 | cloze | A | The History exam is Saturday, Nov 28 | OK |
| 116 | 8 | cloze | A | The WiKim Festival is Friday, Nov 20 | OK |
| 117 | 8 | cloze | A | Samsung won the title 4–1 | OK |
| 118 | 8 | cloze | A | Kimjang for four: 199,456 won | OK |
| 119 | 8 | cloze | A | 20 cabbages: 54,980 won | OK |
| 120 | 8 | cloze | A | This year's candidates: 551,864 | OK |
| 121 | 8 | multiple choice | A | This year's candidates: 551,864 | OK |
| 122 | 8 | multiple choice | B | Test sites nationwide: 1,312 | OK |
| 123 | 8 | multiple choice | A | Naejangsan: Forestry Service forecast peak Nov 4 | OK |
| 124 | 8 | multiple choice | B | Naejangsan: Weatheri forecast peak Nov 11 | OK |
| 125 | 8 | multiple choice | B | Duryunsan: Forestry Service forecast peak Nov 11 | OK |
| 126 | 8 | multiple choice | A | Game 1: kt won 8–7 | OK |
| 127 | 8 | multiple choice | A | Cancelled-seat sign-up: Nov 11–13 | OK |
| 128 | 8 | multiple choice | B | The fire-precaution period ends Dec 15 | OK |
| 129 | 8 | multiple choice | B | Minjun goes to the advance assembly on Wednesday | OK |
| 130 | 8 | multiple choice | A | He takes the CSAT on Thursday | OK |
| 131 | 8 | multiple choice | B | He shares kimchi with family on Sunday | OK |
| 132 | 8 | multiple choice | C | Next week he prepares for the History exam | OK |
| 133 | 8 | sentence building | 저는 수요일에 예비소집에 가요. | Word order: subject + time + place + verb | OK |
| 134 | 8 | sentence building | 우리는 김치를 나눠 먹어요. | Subject + object + verb | OK |
| 135 | 8 | sentence building | 민준이는 한국사를 좋아해요. | 좋아하다 = to like | OK |
| 136 | 8 | sentence building | 수험생은 도서관에서 공부해요. | Use 「에서」 for the place of an action | OK |
| 137 | 8 | translation | Nov 22 is Kimchi Day. | See page 2 | OK |
| 138 | 8 | translation | Samsung won the title after 12 years. | See page 4 | OK |
| 139 | 8 | translation | 11월 18일은 예비소집이에요. | See page 5 | OK |
| 140 | 8 | translation | 일요일에는 가족과 김치를 나눠 먹어요. | See section C on page 8 | OK |
| 141 | 8 | matching | b | 예비소집 = advance assembly b | OK |
| 142 | 8 | matching | c | 김치의 날 = Nov 22 c | OK |
| 143 | 8 | matching | a | 발효 = the fermentation process a | OK |
| 144 | 8 | matching | d | 우승 = championship d | OK |
| 145 | 8 | cloze | A | He goes to the advance assembly on Wednesday | OK |
| 146 | 8 | cloze | A | Kimchi Day is Nov 22 | OK |
| 147 | 8 | cloze | A | The History exam is Nov 28 | OK |
| 148 | 8 | cloze | A | Kimjang for four: 199,456 won | OK |
| 149 | 8 | cloze | A | Scores come out Dec 11 | OK |
| 150 | 8 | writing | (open task — model text below) | Model text in section H of this page (169 characters) | OK ✓ |
