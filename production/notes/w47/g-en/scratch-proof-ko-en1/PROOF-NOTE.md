# PROOF NOTE — W47 ko-en, independent proof round 1 (proof1)

- Edition: `2026-w47-ko-en` (target ko, reader English), VOL.4
- Print PDF: `Lucerna-VOL4-KO-EN.pdf` 45,262,664 B, SHA-256 `571699d675bd31f2cc656698df05908e6843517b8cc28b5e0b849a0f6f48cc18` — verified, matches brief
- Web PDF: `Lucerna-VOL4-KO-EN-web.pdf` 4,013,441 B, SHA-256 `02203d2490905b9d863c935ede7b378eb87bd00ce9bf5069ab8bbc2f109d4323` — verified, matches brief
- text.md: 26,389 B, 332 items — verified (683 lines)
- Builder record: `hidden_files/w47/scratch-fanout-ko/en/EDITION-RECORD.md` (run 2); KIT in edition dir. Both read; all builder conclusions re-verified independently below, none taken on trust.
- Probe: `git hash-object -w` OK (739131467b5da8adfaadbc527d26e0d777b5ad96); note dir writable. EDQUOT (Errno 122) hit once while writing this note; deleted only my own reproducible intermediates (freeze build copy 68M + web page renders 11M) and retried once — write succeeded.
- Scope: read SOP.md §8 + §1.1 (full), AGENTS.md, coordinator brief, fan-out report, builder record. Full re-read of text.md (332 items) + extracted SVG text of all 8 pages (1,512 lines) + visual read of all 8 print pages + pixel-diff print-vs-web. 150 keys re-derived stem-by-stem against P1–P7 exercises and the P8 answer key. Mechanical gates re-run independently (see GATE-LOG.md).
- No source/finished file was modified. No insert.py, no lint --write, no git writes.

## VERDICT: (b) 缺陷清单 — 2 defects, one of them fails a hard zero-scan gate

This round is NOT zero-issue. Both defects are in P7, both in the English explanation layer added by the fan-out (core has neither).

### D1 — [中] P7 frame gloss uses curly double quotes U+201C/U+201D, rendered full-width in Noto Sans CJK KR

- Location: `svg/p7-mal.svg`, `<text x="1461.5" y="1233.32" font-family="Noto Sans CJK KR" font-size="20">`, source `content7.py:81` (`wcn = "Frame: “after ~”. Ask: “〜 후에 뭐 해요?”"`).
- Evidence: independent scan of all 8 SVGs + text.md + ABSTRACT.txt: U+2019 = 0 everywhere (pass); U+201C = 2, U+201D = 2, all in p7-mal.svg (FAIL — task/known-defect class (2) requires 0). Core-ko scans 0/0/0 on all 8 pages. Zoom render `work/p7-frame-zoom.png` (300 dpi crop of the print PDF) shows the quotes visibly full-width with wide gaps: `Frame: “after ~”. Ask: “〜 후에 뭐 해요?”` — opening quote detached from `after`, closing quote detached before the period. The rest of the edition uses straight quotes (U+0027 ×65 across the 8 SVGs, incl. the Korean frame example directly above this line: `'수능 후에 김치의 날이 와요.'`), so this line is also internally inconsistent.
- Severity: 中. One line, but a visible typographic defect on the printed page and an explicit zero-scan gate failure. Fix: replace with straight double quotes `"` (or single quotes), as everywhere else in the edition; rebuild + full re-proof per SOP §8.4.

### D2 — [低] P7 "Phrases of the week" item 7 is not verbatim from any article; its citation is circular

- Location: P7 phrases list, 7th phrase `「수능 후에 김치의 날이 와요」 / After the CSAT comes Kimchi Day. (7면)`.
- Evidence: the exact sentence occurs nowhere in P1–P6. `grep -o` over all 8 SVGs finds it only in `p7-mal.svg` (frame example line, split across two `<text>` elements at y=1081.2/1142.26, plus the phrases-list line at y=2091.7). The heading claims "(verbatim from this issue)" and SOP §4 requires the 金句 to be 摘自本期自己的文章; the other 7 phrases were each verified verbatim (substrings) in P1–P6 articles — #1 P2 strip, #2 P1 lead, #3 P4 headline, #4 P2, #5 P3, #6 P6, #8 P6. The "(7면)" citation points at the "Pattern of the week" frame example that itself coined the sentence. Genuine article sentences with the same meaning exist and could replace it: P1 `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`, or P5/P7-B1 `수능이 끝나고 사흘 뒤에 김치의 날이 와요`.
- Severity: 低. The sentence is factually correct and uses only issue facts; the defect is sourcing/citation, not content. Fix: swap in a genuine article sentence (with its real page citation) or drop the item; rebuild + full re-proof.

## VERIFIED CLEAN (independent re-check, not taken from builder)

### Text / content — full read
- All 8 pages re-read in full (SVG text + text.md + rendered pages). Korean spelling, particles, spacing, verb forms checked; P7 error-clinic corrections all correct (김치의날→김치의 날; 삼성는→삼성은; 담궈요→담가요; 날예요→날이에요).
- All "Note —" glosses checked: every glossed Korean word occurs in its adjacent article; all English glosses correct (incl. neighbour, pre-salted cabbage, test-site office, to tell apart).
- Dates/weekdays verified by calendar: Nov 16 Mon, 17 Tue, 18 Wed, 19 Thu, 20 Fri, 21 Sat, 22 Sun, 28 Sat, Dec 11 Fri, Dec 15 Tue — every weekday claimed in the edition is correct.
- Percentages re-computed: 199,456 vs 219,071 = −8.95% ≈ 9.0% ✓; 54,980 vs 74,800 = −26.5% ✓; 199,456 vs 평년 230,442 = −13.4% ✓; 2014→2026 = 12 years ✓; 551,864 + 2,310 = 554,174 last year ✓.
- External facts spot-checked live (web, Korean sources): 2027 CSAT Nov 19 (Thu), 85 districts, 1,312 sites, 551,864 candidates (−2,310), 08:10 entry / 08:40–17:45, listening 13:10–13:35, offices from 10:00, scores Dec 11 (Edu. Ministry 2026-10-20) — all match. HanNeungGeom 81st Nov 28 (Sat) 10:00, 심화 only, fee 27,000원, photo registration from Nov 11 10:00, cancelled-seat sign-up Nov 11–13, results Dec 11 (국사편찬위원회 notice) — all match. Kimjang cost aT Nov 10 announcement (Nov 9 basis): 199,456원, −9.0% vs 219,071, −13.4% vs 평년, cabbage 20 = 54,980 (−26.5%), chili powder −1.8%, radish −5.6%, peeled garlic & salted shrimp up — all match. Korean Series 2026: Samsung 4–1 over kt, G5 Nov 8 Daegu 12–1, 1 loss then 4 straight, first title since 2014, 9th overall, playoff Samsung 3–2 KIA, G1 kt 8–7, G4 10–5 (Nov 8–9 press) — all match.
- P7 phrases 1–6, 8 verified verbatim from articles (see D2 for #7). P7 B1 "사흘 뒤" arithmetic: Nov 19 + 3 days = Nov 22 ✓. D-3/D-1/D-데이 mapping ✓.
- VOL.4 correct on all pages; VOL.5 appears twice on P7 by design (next-week bar + readers'-corner promise, core had 3). `·` counts identical to core page-by-page (13/21/20/14/20/31/17/38). No hanzi in any `<text>` (0). No U+2019 anywhere (0).
- H model text: 169 characters excluding spaces (221 incl. spaces) — same count and convention as core (core KIT: 169), within the stated 150–200 range under that convention. Not a defect.
- P8 answer-note prose spot-checked against keys (incl. #25–28/#43–46/#61–64 matching notes, #57–60 past forms, #79–82 word order, #133–140 translations, #137 "See page 2" / #138 "See page 4" / #139 "See page 5" / #140 "See section C on page 8" — all point at the right pages; #140's source sentence is section C verbatim). Repeated option letter at the end of matching notes (`… won d`) is core's own convention — adjudicated, not a defect. "Weatheri" is core's rendering — adjudicated.
- P4 ladder "LG가 두산에 4대 1로 승리": identical in core; `대` marks a game score (as in 12대 1), not a series record — not a defect.

### 150 keys — re-derived, 150/150
- Numbering 1–150 continuous, no gaps/dups; per-page 10/18/18/18/18/18/12/38; levels A2 51 / B1 72 / B2 27 (recounted from SVG badges — matches builder). Every key checked against its stem + the cited article/table: all correct, including #32 B (Forestry Nov 4), #89 B (~80%), #97 틀리다 (measures Nov 19 only), #106 B (D-3 = Nov 16), #122 B (1,312), #124 B (Weatheri Nov 11), #125 B (Duryunsan Nov 11), #137/#138 English keys (re-aimed, expected keydiff), #150 `✓` model item.
- P8 extract (independent): 150/150 noted; compare vs core: CLEAN, keydiff [137, 138] only (expected).

### Layout / visual — 8/8 print pages + print-vs-web pixel diff
- P1–P8 each visually clean: no overflow, overlap, footer intrusion, or clipped text; all 8 photos present with honest captions (incl. Hokkoda file photo on P1 and early-20th-century US team photo on P4, both captioned as file photos); "In numbers", "Shopping list", "To know", "Youth numbers" boxes fit.
- P2 notes checked with the `Note —` reader-language prefix included (de-family lesson): all 4 P2 notes wrap inside their boxes; the "Counting the days" strip sits at its normal position; exercises 11–28 fit with white space to spare. No defect.
- P1 drop cap reads correctly as "11월 16일…" (the extracted "1" + "1월" is the drop-cap split, not a typo).
- Print-vs-web pixel diff at 72 dpi: mean abs diff ≤ 0.47/page (P6 = 0.00); layout identical, differences are image downsampling only.

### Deliverables
- ABSTRACT.txt: one line, English, 0 ASCII double quotes, contains刊名/目标语名/A2–B2/150 exercises + real topics (CSAT D-3, Nov 19, Kimchi Day Nov 22, 199,456 won, Samsung 12-year title, History exam, leaves) ✓.
- text.md 332 items: the F-block 2nd term (김치의 날), D-section stems, P8 answer-key lines and the "All" badge are absent — but byte-for-byte the same export behaviour as core-ko's text.md (333 items). Shared textmd.py quirk, identical in core, print unaffected — observation, not a defect in this edition.
- P1 calendar omits Nov 21 (LA kimchi event): identical in core — editorial selection, not a defect.

## Observations (not defects, for the parent line)
- O1: textmd.py drops the F-section 2nd term, the D-section stems and the P8 answer-key lines from text.md in BOTH core and this edition (core 333 items, en 332 — the 1-item delta is the "All" badge only). If the site body should carry them, the fix belongs in the shared exporter, not in this edition.
- O2: P1 calendar lists 5 dates and omits Nov 21 (LA kimchi-making, P3) — same in core; the calendar's stated criterion ("날짜가 정해진 일만 모았어요") is about inclusion, so this is editorial selection.
- O3: P1 autumn photo is a Hokkoda (Hokkaido) file photo, honestly captioned as such — same in core.

## What must happen before delivery
1. Fix D1 (content7.py:81, straight quotes) and D2 (swap phrase 7 for a genuine article sentence).
2. Rebuild the edition, re-render both PDFs.
3. A fresh full proof round from scratch (SOP §8.4) — this round's clean findings do not carry over to a rebuilt edition.
