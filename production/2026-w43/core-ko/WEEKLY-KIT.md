# Lucerna 한국어판 VOL.1 — WEEKLY KIT

**Edition:** Korean core, first pair — Korean target text + explanations in the reader's native language (Chinese). Languages pair one-to-one; the Chinese in this issue is small gray glosses, notes and answer explanations only.
**Week:** Mon 2026-10-19 – Sun 2026-10-25 · **VOL.1 / 제1호**
**Masthead:** **Lucerna**, no article. Korean is an article-less language, so per the SOP masthead rule the blackletter Latin wordmark stands alone (same treatment as the Russian, Chinese and Japanese editions).
**Speech level:** 해요체 held throughout all learner text.

## Spec

- 8 pages, 1950×2700 px, 4 columns, warm ivory #f7f1e2, deep-olive accents — same grid as all editions.
- Ramp: P1 front A2 · P2 life A2 · P3 culture A2→B1 · P4 sport B1 · P5 youth B1 · P6 deep read B2 · P7 language focus (A2/B1/B2 columns) · P8 assessment + writing + all keys.
- Pipeline: Python → SVG → CairoSVG → PNG/PDF → pypdf. Build code: `hidden_files/weekly-report-ko-build/` (run.py, content12/34/56/7/8.py, bslib4.py, svglib.py, render.py). Fonts: Noto Serif/Sans CJK KR (index 1), UnifrakturMaguntia for the masthead.
- Build produced **zero** FLOW OVERFLOW / HEAD TOO WIDE warnings.

## Measured totals (visible-text extraction from the final SVGs, one consistent method)

| Page | Chars (no spaces) | Chars (with spaces) | Exercises |
|---|---|---|---|
| P1 표지 | 1,877 | 2,343 | 10 |
| P2 생활 | 1,751 | 2,160 | 18 |
| P3 문화 | 1,560 | 1,900 | 18 |
| P4 스포츠 | 1,451 | 1,761 | 18 |
| P5 청년 | 1,501 | 1,866 | 18 |
| P6 깊이 읽기 | 1,613 | 2,043 | 18 |
| P7 말 공부 | 1,731 | 2,123 | 12 |
| P8 시험과 답 | 4,443 | 5,449 | 38 |
| **Total** | **15,927** | **19,645** | **150** |

- Exercises by level: **A2 57 · B1 66 · B2 27 = 150**. Every item level-badged; keys registry-generated.
- Exercises by type: 完成句子 49 · 单选 51 · 词汇配对 16 · 完形单选 13 · 造句 8 · 句型转换 4 · 判断 4 · 翻译 4 · 写作 1.
- P8 writing model: 162 chars, programmatically counted, inside its printed 150–200자 range.

## Benchmark comparison (honest)

- Exercise benchmark 《英语周报》 = 154 counted items. This issue: **150 (97%)** — at the level of DE/ES/IT/PT/NL/RU/JA VOL.1 (all 150), above FR VOL.2 (145) and EN VOL.1 (149). No padding was added to chase 154.
- Text volume: 15,927 no-space chars vs the Japanese core's 16,815 — slightly leaner. Korean 띄어쓰기 makes the with-space figure (19,645) the fairer cross-edition comparator for Korean; both figures are stated so nothing hides behind the counting method. (Updated after the independent-proofread fix below: the P8 key notes were rewritten as Chinese one-liners, which shortened P8 by 363 no-space chars.)
- B2 share is the thinnest slice (27/150, 18%): the pool's B2 material is essentially the P6 deep read plus its exercise set and the P7 B2 column. Disclosed, not padded.

## Per-page contents

- **P1 표지 (A2)** — Lead: Typhoon Champi (see editorial notes). Numbers box (30호 / 초속 59미터 / 25~26일 / 검색 1위), this week's search terms box (two date-labeled datasets, volumes flagged approximate on-page), contents, word of the week 북상하다, weekend briefs (억새·단풍·수능), NASA typhoon photo, 6 instant drills + 4 lightning-quiz items.
- **P2 생활 (A2)** — Typhoon home-safety checklist (windows, balcony items, check the latest forecast) + CSAT D-29 feature: 551,864 candidates, 1,312 test sites, offices from 10:00, extra subway services, aircraft held during English listening 13:10–13:35; D-day 4-box strip; library photo; 18 exercises.
- **P3 문화 (A2→B1)** — 25th Seoul Silver Grass Festival, Haneul Park, Oct 17–23 (Friday = last day), theme 「억새, 자연이 건네는 위로」, former-landfill park; Cheongsong Apple Festival: online edition running now (Sep 24–Nov 8), on-site Nov 4–8, free '청이와 송이' emoticons for the first 75,000; Keibun painting + Cézanne still life; 18 exercises.
- **P4 스포츠 (B1)** — KBO semi-playoff KIA vs LG as schedule and stakes only (G3 Oct 20, G4 Oct 21, G5 if needed Oct 23; winner opens the playoff vs Samsung on Sun Oct 25; kt wiz waits in the Korean Series from Mon Nov 2; LG's 4–1 wild-card win over Doosan). Drawn 4-step road-to-the-Korean-Series ladder; archival team photo; 18 exercises.
- **P5 청년 (B1)** — NMIXX 6th mini-album 'Strange Muse', title '긴 소원 (Birthday Wish)', released Mon Oct 19 18:00, first unit songs, Melon Top 100 #34 on release evening → #5 by midnight (career high); Chiikawa film back to #1, 1.5M cumulative admissions. Drawn Melon chart, bars exactly proportional (143 px : 21 px = 34 : 5 at 4.2 px per rank unit, noted on-page); concert-crowd and cinema photos; 18 exercises.
- **P6 깊이 읽기 (B2)** — The two foliage peaks: Forest Service/National Arboretum map (dated Sep 22) puts Seoraksan's maple peak on **Oct 20** (criterion: 50%+ of leaves turned, by species); Weatheri + Korea National Park Service say **Oct 25** (criterion: whole mountain ~80% turned); Jirisan ~Oct 25 on the Forest Service timeline. Both dates printed **with their criteria**; comparison table with source line; media-literacy angle ("check the criterion, not just the date"); Hakkoda valley photo, honestly captioned as a file photo; 18 exercises.
- **P7 말 공부** — A2 날씨의 말 (북상하다·진로·영향권), B1 날짜 세는 말 (D-day counting), B2 예보 읽는 법 (기준) — 12 exercises; error clinic ×4 (학교에서 갔어요→학교에; 할수→할 수 띄어쓰기; 책를→책을; mixed speech levels→unify); frame 「〜까지 ○일 남았어요」; readers' corner = editor's example letter, explicitly labeled as an example; 8 phrases of the week, verbatim from this issue's articles with page tags; VOL.2 teaser.
- **P8 시험과 답** — 38 assessment items (timeline cloze, general MC, mini-reading, sentence building, translation both directions, matching, dialogue cloze, writing 『나의 가을 주말』 with counted model) + all 150 answer keys with one-line Chinese explanations, grouped by page.

## Sources (only source pool: trend research 2026-W43, batch C, 한국어 section)

| Item | Used on | Notes honored |
|---|---|---|
| KO-1 Typhoon Champi (#30) | P1 lead, P2 checklist, P7, P8 | See editorial notes — open forecast only |
| KO-2 KBO postseason | P1, P4, P7 teaser, P8 | Schedule/stakes only; no results existed in the pool, none invented |
| KO-3 NMIXX 'Strange Muse' | P5, P8 | Chart positions as pooled (#34 → #5) |
| KO-4 Chiikawa film | P1 heat box, P5, P8 | 1.5M cumulative as pooled |
| KO-5 Silver Grass Festival | P1 briefs, P3, P8 | 25th edition, Oct 17–23, free entry |
| KO-6 Foliage two peaks | P1 briefs, P6, P7, P8 | Both dates printed with both criteria |
| KO-7 CSAT Nov 19 | P1 briefs, P2, P7, P8 | 551,864 candidates · 1,312 sites · D-29 (arithmetic verified: Oct 21 → Nov 19 = 29 days) |
| KO-8 Cheongsong Apple Festival | P1 heat box, P3, P8 | Online now; on-site Nov 4–8; emoticons 75,000 |

- The two search datasets are never merged: Google Trends Korea snapshot dated **Oct 17** and KoreaTrendBoard dated **Oct 21** are labeled with their own dates everywhere they appear, and volumes are printed as approximate (대략적인 숫자) on P1.
- All weekdays verified against the real 2026 calendar (Oct 19 Mon, 20 Tue, 21 Wed, 23 Fri, 25 Sun, Nov 2 Mon, Nov 19 Thu).
- No politics of any kind appears in this issue; the pool contained none.

## Editorial calls (adjudications)

- **Typhoon = open forecast, never a landed fact.** KMA changed its forecast on Oct 21; KMA/JMA/JTWC tracks diverge; the paper prints "경로는 아직 바뀔 수 있어요" (the path can still change), attributes the numbers to KMA's Oct 21 morning announcement, and promises to check the actual track in VOL.2. No landfall is asserted anywhere.
- **Baseball results:** the pool held no G3/G4 results at press time, so P4 prints the fixture list and stakes only and says so ("경기 결과는 다음 주 신문에서 알려 드릴게요"). The only completed result printed is the wild-card game (LG 4–1 Doosan), which the pool states as completed.
- **P4 past-tense conversion exercises (57–60)** are anchored only to events the paper itself states as completed (wild-card result, festival start, KMA's forecast change, album release).
- File photos are captioned as file photos with their real subjects (see image list) — never presented as the event itself.

## Images (8, all public domain / CC0, license verified per image via Wikimedia Commons metadata on 2026-10-21; all verified actually placed in the final SVGs — image elements per page: 1/1/2/1/2/1/0/0)

| Page | Image | Author / license | Caption honesty |
|---|---|---|---|
| P1 | Super Typhoon Maysak eye from ISS-43 | NASA / Public domain | Captioned as a 2015 Maysak file photo, NOT Champi |
| P2 | Students studying, Sias Library 2017 | Gary Todd / CC0 | Generic study scene, labeled 자료 사진 |
| P3 | Quail Feeding Amidst Susuki and Kikyo | Matsumura Keibun / Public domain | Painting; susuki is the festival's plant |
| P3 | Still Life with Apples | Paul Cézanne / Public domain | Painting |
| P4 | Washington baseball team group photo | Bain News Service / Public domain | Captioned as an early-1900s US team |
| P5 | Crowd at Fort Knox concert | US Army / Public domain | Captioned as a file photo, NOT NMIXX |
| P5 | Movie theater seats | Elijah Flores / CC0 | Generic cinema interior |
| P6 | Hakkoda Mountains, Jogakura Valley in autumn | lumoplank / CC0 | Captioned as a file photo, NOT Seoraksan |

Full per-image records: `hidden_files/weekly-report-ko-build/assets/CREDITS.md`.

## Proofread record (full self-pass, all items re-checked after the final render)

- Korean: 띄어쓰기 scan, particle use (은/는/이/가/을/를/에/에서), endings and honorific consistency (해요체 held; the only deviations are the error clinic's four deliberately wrong examples, each printed in 「」as the mistake to fix), 이에요/예요 distribution checked.
- Every one of the 150 answer keys re-derived against its stem on the rendered P8 (registry-generated list read against the exercise pages).
- P7 phrases of the week byte-verified (whitespace-insensitive match): each of the 8 phrases occurs verbatim in its tagged article page and once in P7.
- Line-start audit on the final SVGs: **no line begins with closing punctuation** (Korean or Chinese). 14 automated flags were all adjudicated as opening quotes or the '·' option separator used across all editions.
- Every glossed word confirmed present on its own page (see fix 3 below).
- Data re-checks: D-29 = 29 days (computed); Melon bars measured in SVG coordinates (143 : 21 = 34 : 5); pool figures re-read against the pool file; the two search datasets kept separate with their dates.
- Fixes made during production, each verified in the final render:
  1. P1 search-terms box: bottom text lines collided — stack spacing tightened and re-measured in SVG coordinates.
  2. P5 Melon chart: the "34위" label was clipped at the box edge — bars rescaled to 4.2 px/unit (proportion preserved), labels fully inside.
  3. P5 gloss word 관객 did not occur on the page — the article sentence now reads "지금까지 본 관객은 150만 명이 넘어요".
  4. P8 writing model was 107 chars against its printed 150–200자 instruction — lengthened to a counted 162 chars.
  5. Feature columns on P2–P6 ran short — filled with pool-based paragraphs and a P5 numbers box (no new facts introduced).
  6. One build crash (wrong tuple format in a box call) was caught because the P5 card's hash had not changed after an edit — the stale render was discarded and rebuilt.
- Adjudicated residuals (accepted, consistent with earlier editions): the third feature column is not fully filled on P3–P6; exercise section heads can split from their matching sets across a column break (P2/P4 D sections); P7 has a quiet band between the columns and the phrases section.

## VOL.2 promises printed in this issue (must be honored next week)

1. 준플레이오프 결과와 플레이오프 소식 — semi-playoff result and playoff news.
2. 태풍 참피의 실제 진로 확인 — what Champi actually did.
3. 단풍 절정 확인 — which foliage peak date proved right.
4. 10월 31일 할로윈 — Halloween.
5. 독자 편지와 8면 쓰기 우수작 — real readers' letters and the best P8 writing (the VOL.1 letter is labeled an editor's example).

## Deliverables in this folder

- `svg/` — p1-pyoji, p2-saenghwal, p3-munhwa, p4-seupocheu, p5-cheongnyeon, p6-gipi, p7-mal, p8-siheom
- `cards/` — the same 8 pages as 1950×2700 PNGs
- `Lucerna-VOL1.pdf` — print PDF, 34.80 MB
- `Lucerna-VOL1-web.pdf` — web PDF, 2.90 MB (under the ~10 MB Discord limit)

## Reproduction

```bash
python3 -m venv /tmp/wp-venv && /tmp/wp-venv/bin/pip install cairosvg pillow pypdf
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-ko-build
/tmp/wp-venv/bin/python run.py      # builds svg/ + prints registry stats (TOTAL 150)
/tmp/wp-venv/bin/python render.py  # builds cards/, print PDF, web PDF
```

Not posted to Discord (per instructions for this build).

## Independent proofread (separate pass, 2026-10-21)

Method: all visible text extracted from the 8 rendered SVGs with coordinates and read page by page; **all 150 answers re-derived by hand** against stems, articles, the P6 table and the P5 chart; every builder claim in this KIT re-verified against the render (SVG coordinates/rects), the trend pool, and the real 2026 calendar — not against the build sources' intentions.

### Fixed (1 defect class, 139 strings)

- **P8 answer-key notes were Korean, not the promised Chinese.** The printed P8 header says "每题附一句中文简析" and this KIT claimed "all 150 answer keys with one-line Chinese explanations", but ~130 of the 150 notes were Korean restatements of the article (e.g. key 1: "참피는 올해 제30호 태풍"; key 90: "두 날짜는 모두 맞을 수 있어요"). SOP §3 puts 答案简析 in the reader's-native-language layer, and the Japanese core's keys are Chinese — so the Korean notes broke both the printed promise and the edition architecture. **Fix:** 139 note strings rewritten as Chinese one-liners in the build sources (`content12/34/56/7/8.py`, notes only — every old string asserted before replacement; the 11 notes already in Chinese were kept: 16, 135, 137–140, 141–144, 150). Two notes were tautologies repeating their own answer sentence (82, 134) and got real explanations. Whole issue re-rendered; verified programmatically that **all 150 answer tokens are byte-identical before/after** and that no Korean-only note remains. New totals: **15,927 no-space / 19,645 with-space** (P8 4,443 / 5,449, same visible-text extraction method as the other pages; pages 1–7 reproduce the table above exactly). Print PDF 34.80 MB, web PDF 2.90 MB.

### Verified clean (builder's claims independently confirmed)

- **All 150 keys re-derived correct**, incl. the four matching sets (25–28 → b/d/c/a; 43–46 → b/c/d/a; 61–64 → b/c/a/d; 141–144 → b/c/d/a — the last read as left-item→option pairs matching the registry, consistent with the KIT's "a/c/b/d" phrasing). Numbering 1–150 continuous; per-page counts 10/18/18/18/18/18/12/38; levels A2 57 · B1 66 · B2 27.
- **Typhoon framing audit clean everywhere** — articles, the P1 numbers box (25~26일 marked 예상), exercises and keys: KMA's Oct 21 change is the news, KMA/JMA/JTWC disagreement printed, path stated as changeable, no landfall or damage asserted, no key depends on a track outcome (ex. 9's key needs only "올 수 있는 곳").
- Foliage P6 prints **both** dates with **both** criteria attributed (table + text + footnote), 지리산 under the Forest Service timeline only; no single "official" date anywhere. Baseball = schedule/stakes only; the one printed result (LG 4–1 Doosan, wild card) is completed and sourced.
- Melon chart bars measured in the SVG: **143 px and 21 px exactly (34:5)**, "34위" label fully inside the panel; proportionality note printed on the chart.
- Writing model counted programmatically: **162 chars** (공백 제외, the convention the page itself states: "162자"), inside the printed 150–200자 range.
- All 8 images placed in the render (1/1/2/1/2/1/0/0); the three file-photo captions read and honest (2015 Maysak ≠ Champi; US Army crowd labeled 자료 사진; Hakkoda photo — listed in CREDITS as Jōdōgahama, actually the Hakkoda mountains file — captioned generically as a mountain valley in autumn colors and marked 자료 사진, claims nothing about Seoraksan).
- Every gloss on P1–P7 glosses a word on its own page; the builder's P5 관객 fix confirmed in the rendered article body ("지금까지 본 관객은 150만 명이 넘어요"), and 누적 likewise present.
- P7's 8 phrases are verbatim contiguous excerpts of the tagged articles with correct page tags (programmatic, whitespace-insensitive). Occurrence counts exceed 2 for three phrases only through legitimate apparatus reuse — phrase 1 also in P1's standfirst deck and quoted in P8 ex. 137's stem; phrase 4 also as P2 matching option a and P8 ex. 138's stem; phrase 8 quoted in a P8 key note in the first render (that note is now Chinese). The SOP requirement (verbatim + correct tag) holds; recorded here rather than rebuilt.
- All printed date/weekday pairs checked against the real 2026 calendar (Oct 19 Mon, 20 Tue, 21 Wed, 23 Fri, 24 Sat, 25 Sun, 31 Sat; Nov 2 Mon, Nov 4 Wed, Nov 19 Thu; Sep 22 Tue) — all correct; D-29 (Oct 21 → Nov 19) arithmetically exact; sums 982+514+431+312=2,239 not printed anywhere (pool discipline kept).
- Speech level: 해요체 held throughout learner text; the only 합쇼체 token is the error clinic's deliberate mistake example (입니다), framed as an error. 띄어쓰기 read-through: no errors found. Line-start audit on the render: no line begins with closing punctuation; 4 lines begin with the "·" separator (house style, same adjudication as the builder's 14-flag count under a wider definition).
- Masthead "Lucerna" with no article on all 8 pages; VOL.2 teaser in the paper matches the registered promises above item for item; the readers'-corner letter is labeled an editor's example in Korean and Chinese; P1 search box measured collision-free in the final SVG (items end y≈1244, contents block starts y=1336) and viewed clean; no overflow/overlap/footer collisions on any of the 8 PNGs; P8 keys end at y=2351, above the 2540 content limit.
- Banned-word scan (bridge / 桥接） over pages, this KIT and all build code including comments: **absent**.
- Builder's pre-fix P8 total (4,806) differed from this pass's extraction by 3 chars; immaterial, superseded by the post-fix recount above.

Final state after this pass: a complete second pass over the re-rendered issue found **zero problems**. The issue is final.

## PATCH (2026-10-21): P2 D-day sentence grazed by the exercises rule — fixed

**Provenance.** The KO × EN builder's geometric audit flagged the defect on its
own P2 and fixed it there (sentence up 6 px), reporting the geometry as
inherited from this core. This core's own audits predate the line-crossing
check (thin lines sit under the 30 % coverage threshold), so the graze was
never flagged here. Verified independently in the core before touching
anything:

- SVG: the D-day strip's memorise-sentence («문장으로 외워요: 「수능까지 29일
  남았어요. 오늘이 D-29예요.」», Noto Serif CJK KR 20.5) sat at baseline
  **y=1800**; the exercises rule (`<line>` y=1804, stroke-width 2, rendered
  rows 1803–1804) is painted after it. Baseline only 4 px above the rule.
- Pixel measurement of the shipped card: sentence dark ink reaches y=1801,
  its anti-aliasing fringe y=1802 — exactly one faint row above the rule;
  the 4× crop shows the periods and glyph bottoms kissing the rule. Under
  the audit ink-band convention (baseline −0.88em…+0.30em → band
  1782.0–1806.2) the rule crosses the band. A graze, same class as the
  PT-core P7 and IT-core P1 thin-line defects. Confirmed REAL.

**Fix (geometry only).** `content12.py`: the sentence's `p.para` y moved
`dy + 234` → `dy + 228` (−6 px, mirroring the EN edition's fix exactly).
Knock-ons checked: above it the D-day word boxes end at y=1768 (sentence ink
top now ≈1776, ~8 px clear); the rule and everything below are unmoved.
No text changed.

**Verification.**
- Baseline first proven: the unmodified build reproduces all 8 shipped SVGs
  and cards byte-identically (registry TOTAL 150; A2 57 · B1 66 · B2 27;
  pages 10/18/18/18/18/18/12/38).
- Diff old vs new P2 SVG: exactly one attribute — the sentence element's
  `y="1800"` → `y="1794"`. Every text string identical; all 150 keys
  byte-identical (nothing textual touched anywhere).
- Diff scope: only `svg/p2-saenghwal.svg`, `cards/p2-saenghwal.png` and the
  two PDFs changed; P1, P3–P8 SVGs and PNGs byte-identical (MD5 vs pre-patch).
- Post-fix card pixels: sentence ink ends y=1795, fringe y=1796, rows
  1797–1802 empty, rule at 1803–1804 — 6+ px of clear air; crop viewed.
- Full sweep of all 8 pages (paint-order coverage ≥30 %, footer band,
  page edge, line-crossing; production-font glyph boxes): **zero flags**.
  The sweep was instrument-validated against the pre-patch files, where it
  raises exactly this one flag.
- Final sizes: print PDF 34,800,245 B; web PDF 2,896,878 B (< 10 MB).
  The copy already posted to Discord predates this patch; the parent line
  should replace it with this build.
