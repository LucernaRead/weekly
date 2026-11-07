# W45 English core VOL.2 — INDEPENDENT PROOFREAD, ROUND 2 (after fix round 1)

- Edition: `files/weekly-report-w45-en-core/` (8 SVGs, 8 PNGs, `The-Lucerna-VOL2.pdf` + `The-Lucerna-VOL2-web.pdf` at 8 pages each, `WEEKLY-KIT.md`, `ABSTRACT.txt`)
- Proofreader: independent (not the builder, not the fix agent). Round-1 report (`hidden_files/w45/en-core-independent-proof.md`) and fix log (`hidden_files/w45/en-core-fix1.md`) were read but NOT trusted; every check below was re-run or re-read from the re-rendered edition itself.
- Method: SOP §§1–8 + occlusion appendix. SVG text extracted independently per page and read end to end; all 8 PNGs viewed as images; all dates re-checked with `date -d`; exercise numbering, all P8 keys, chart sums, model-essay word count, gloss anchoring, golden sentences, trend-pool + W43-promise compliance re-verified; `tools/occlusion_audit.py` run with `--selftest` first, then on the edition dir.
- Builder files were NOT edited. No git push, no Discord, no messages sent.

## VERDICT: 2 PROBLEMS — NOT ZERO-PROBLEM, DO NOT FINALIZE YET

All 11 round-1 fixes verify (see §"Round-1 fix verification" below), and the fix round's flagged P8-battery risk passes visual inspection. But a complete fresh round found 2 NEW problems, both of the same class as round-1 problems 1 and 3 (false statements about dates / about the issue's own pages). Per SOP §8.4, only a full round finding zero problems finalizes this core, so this core is NOT finalized.

Per-area verdicts:

- Text (spelling/grammar/punctuation): PROBLEM (no. 1 is a false page attribution in teaching text; no spelling/grammar errors found).
- Numbers (numbering, keys, chart, word count): CLEAN.
- Facts (dates, trend pool, red lines): PROBLEM (no. 2 is a temporal contradiction).
- Layout (overflow/overlap/footer/images/credits): CLEAN.
- Geometry (occlusion audit): CLEAN — tool selftest OK (all 6 planted classes fired, clean controls silent), edition run **0 flags**, and visual inspection of all 8 pages found no overflow, overlap, or footer intrusion.

## Numbered problem list

### 1. P7 B2 column — "whether" is claimed to be the word of the page-6 deep read, but "whether" never occurs on page 6
- Location: P7, LEVEL B2 · WHETHER = IF ?: "Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word of the deep read (page 6)."
- Evidence: case-insensitive grep of the rendered P6 SVG finds **zero** occurrences of "whether" anywhere on page 6 (article, ballot box, chart, exercises, boxes — none). The word occurs in this issue only on P7 itself (the column, the toolbox B2 sentence) and on P8 (Q125, Q136, answers). A learner who follows the printed pointer to page 6 will not find the word there. The attribution is therefore false as printed, in the same class as round-1 problem 3 (a false claim about the issue's own pages).
- Note on the alternative reading: "whether" does suit the deep read's *theme* (election-night uncertainty), and the column's example sentence is a teaching example, not a claimed verbatim quote. The defect is the page attribution itself, not the grammar teaching. Fix (minimal): drop the page-6 attribution (e.g. "It is the word for election-night uncertainty") or reword so it no longer states the word belongs to page 6.

### 2. P5 SATURDAY SPORT box — Saturday, November 7 is framed as coming BEFORE the Tuesday vote, but November 7 is AFTER Tuesday, November 3
- Location: P5, SATURDAY SPORT box: "Before Tuesday, there is Saturday : MLS fixtures on November 7, including Charlotte against Inter Miami and Atlanta against the New York Red Bulls. The weekend warms up before the vote."
- Evidence: `date -d` confirms November 3, 2026 is a Tuesday and November 7, 2026 is a Saturday — four days AFTER the vote, not before it. Both framing clauses say the same wrong thing ("Before Tuesday…" and "…warms up before the vote"), and the box contradicts P4, which correctly frames the same November 7 Saturday as the warm-up for Sunday, November 8 ("On Saturday, November 7, the warm-up is already on… The weekend starts on Saturday"). The MLS fixtures themselves are correct (they match P4 and the trend pool); only the box's temporal framing is wrong.
- Fix: reframe the box to match P4, e.g. "After Tuesday, the weekend keeps going: MLS fixtures on Saturday, November 7…" / "The weekend warms up for Sunday's games." Do NOT move the fixtures to a pre-election Saturday — the November 7 date is pool-sourced.

## Round-1 fix verification (all 11 verify on the rendered pages)

1. **P2 weekend wording — VERIFIED.** P2 article now reads: "Two autumn rituals, one weekend — and both are now just passed, not coming." (PNG + SVG text both confirm; "one weekend apart" is gone.)
2. **Bernabéu wording — VERIFIED.** P7 B1 comparatives: "« The Bernabéu is bigger than most stadiums. »" P8 Q123 stem: "The Bernabéu is ___ than most stadiums." Key stays B (bigger). No "Madrid is bigger" remains.
3. **Past Simple column truthful — VERIFIED.** P7 B1 now reads: "Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet." Consistent with P4's D-section hypothetical framing, which is unchanged.
4. **P8 keys 76/77 — VERIFIED.** P8 answers read "76. b · 77. a" (a result = the final numbers of a vote; to call = to announce the winner). All other matching groups re-checked and still correct (P2 24–27, P3 38–41, P4 56–59, P8 141–144).
5. **Q72/Q73 keys — VERIFIED.** P8 answers read "72. map · 73. phone", matching the P5 article's singulars ("Every channel has its own map", "hands free for the phone").
6. **Q53 key — VERIFIED.** P8 answer reads "53. begin", matching the P4 article's twice-printed "the WTA Finals begin".
7. **P3 Q36 uniquely answerable — VERIFIED.** Stem now reads "Godzilla is bigger, darker, and ___ than ever this time." Only "louder" completes the article's triple; key "louder" is now uniquely correct.
8. **Q122 note — VERIFIED.** P8 answer reads "122. B（已发生的事用 fell）". Raw-SVG grep finds zero occurrences of "比赛用 fell" anywhere in the issue; the copy-paste error is gone.
9. **Q126 future-honest — VERIFIED.** Stem now reads "The film ___ on Friday, November 6. A. will open · B. will opened · C. will opens", key A, note "将来时 will + 动词原形". Only A is grammatical (will + base form), and the November 6 opening is correctly future at the November 2 issue date.
10. **P2 gloss anchoring — VERIFIED.** P2 gloss now reads: "讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。" All three words occur in the P2 article; "daylight saving" occurs zero times in the P2 SVG (its P1 search-chart occurrence is a search term, not a gloss, and is untouched).
11. **14 P8 items now badged — VERIFIED, including the dialogue range notation.** Cloze 112–119 each carry a per-item badge (112 A2, 113 A2, 114 B1, 115 A2, 116 A2, 117 A2, 118 B1, 119 B1 = A2 5 / B1 3); writing heading reads "H · WRITING · 写作 [B1]" (B1 1); dialogue carries "Levels : 145–148 [A2] · 149 [B1]" (A2 4 / B1 1). **Judgment on the range notation: it PASSES.** The line names every dialogue item exactly once, assigns each exactly one level, and leaves no item unassigned or ambiguous (145, 146, 147, 148 → A2; 149 → B1). Newly badged total A2 9 / B1 5. Recomputed printed split: previously labeled items A2 51 / B1 64 / B2 21 (recounted item-by-item from the printed badges in this round, not taken from round 1) + newly badged A2 9 / B1 5 = **A2 60 / B1 69 / B2 21**, total 150 — exactly the KIT split.

## Fix-round risk re-check: P8 battery flow (2px slack) — PASSES visually
- The P8 PNG was viewed closely at the dialogue/Writing junction. The "Levels : 145–148 [A2] · 149 [B1]" line sits fully clear above the writing-strip rule, with normal breathing room; nothing is struck through, crowded, or touching the MODEL box. In SVG coordinates the Levels baseline is y=1455.24, the strip rule is y=1486, the Writing heading is y=1526 and the MODEL box top is y=1500 — the line is clear of both. The fix log's tight flow end (y=1483 vs bottom 1485) does not produce any visible crowding. No problem here.

## Verified clean (re-checked independently in this round, no problem found)

- Dates/weekdays: Nov 2 Mon, Nov 3 Tue, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Oct 31 Sat, Nov 1 Sun, Nov 11 Wed, Nov 15 Sun — all correct per `date -d` (the two new problems are wording/attribution errors, not calendar errors).
- Exercise numbering: 1–150 continuous — all 150 keys present in the P8 answers section, none missing, none repeated; per-page counts P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39, matching the KIT.
- P8 keys otherwise: all remaining keys re-derived against stems, articles, and sources — correct, including chart Q82–Q87 (38+29+21+12 = 100; 38−21 = 17), error clinic Q108–Q111, golden-sentence items Q100–Q107, cloze Q112–Q119, reading Q129–Q132, dialogue Q145–Q149, translation Q137–Q139, and the Q35 "taller" / Q55 "faster" comparatives.
- Model essay: 81 words by standard word count (85 counting standalone punctuation tokens ":" / "!" as the builder does) — within the required 80–100 under either count. Writing prompts on P8 match the task; the model sentence "On Sunday night, the clocks had fallen back" is past-perfect-correct (by Sunday night the 2 a.m. change had already happened).
- Golden sentences: all 8 verified verbatim against this issue's own articles (P1, P2 ×2, P3, P4 ×2, P5, P6) — none imported from outside.
- Gloss anchoring otherwise: P1 (midterm/ballot/race/call a race), P3 (open/monster/catchphrase/series), P4 (fixture/title/defend/fan), P5 (map/too close to call/second screen), P6 (register/governor/shape laws/patience) — every word verified present in its page's article.
- Trend-pool compliance (spot-checked against `hidden_files/w45/trend-batch-A.md`, EN section): Election Day Nov 3 lead; Oct 31/Nov 1 as just-passed reports; NFL Week 9 Madrid Bengals–Falcons at the Bernabéu + Dolphins–Lions Miami Nov 8; F1 São Paulo Nov 8 as the second race after the Austin US GP; NASCAR Homestead-Miami, WTA Finals Indian Wells, Baumgardner–Turhan Arlington Nov 8; MLS Nov 7 Charlotte–Inter Miami / Atlanta–New York Red Bulls; films Nov 6 (Cat in the Hat, Godzilla Minus Zero); Netflix Nov 4/5/6/8 slate — all pool-sourced. VOL.1's question ("what do Americans read, watch and eat while they wait") answered on P5. VOL.3 preview dates correct (Nov 11 Veterans Day, Nov 15 NFL Munich, midterm-results report).
- Red lines: no international politics; no UK-ecosystem nodes (no Guy Fawkes / Remembrance); no Senate seats-up count printed (only "about a third" + chamber size 100); no governor count printed ("in many states"); no poll figures, predictions, or real-person quotes printed; practice ballot uses candidate codes A–D only; practice chart is labeled teaching data on the page ("The chart is teaching data, not a real poll") and in Q87; illustrative dialogue ("Did you see Ohio?", "Florida is close!") is unattributed generic speech, not a real-person quote.
- Readers'-corner honesty: P7's corner is explicitly labeled on the page ("editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled") with the matching Chinese editor's note; "M. L., a reader in Chicago" sits inside that labeled example, not presented as a real reader. The open debt (real letters + VOL.1 writing review, carried to VOL.3) is disclosed, not fabricated — same standing as round 1, not a new problem.
- Layout: all 8 PNGs viewed — no overflow, overlap, footer intrusion, or edge breach; P8 answers end above the footer; P2 clocks read 1:00 / 1:30 / 7:45 correctly.
- Images/captions/credits: all 5 match the KIT — P1 voting booth (Kenneth C. Zirkel, CC0), P2 1912 Halloween postcard (public domain), P3 Manet "Cat and Flowers" with an explicit "Not film art" note (CC0), P4 1910 football (Frank R. Snyder, public domain), P6 Capitol (public domain).
- Masthead/pairing: "The Lucerna" masthead, "英语周报 VOL.2" pairing footer and "第 N 版 / 共 8 版" page lines on all 8 pages; 8 pages (multiple of 4); ABSTRACT.txt present and fact-consistent (Nov 2–8, Nov 3 election, clock change, Nov 6 films, Nov 8 Madrid/São Paulo sport, A2–B2, 150 exercises).
- Geometry: see verdict above — selftest OK, edition run 0 flags, visual inspection clean.

## Observations (NOT counted as problems)

- House style uses a space before "?" and ":" throughout ("Tuesday night ?", "America Votes : …"). It is systematic across all 8 pages (presumably family style), so it is not counted as a punctuation error here; if the family style is ever normalized to English punctuation, it must change everywhere at once.
- British spellings "colour" (throughout) and "maths" (P6, once) appear in a paper about American English. They are internally consistent and standard English variants, not errors; not counted. (If the family ever adopts American spellings, change everywhere at once.)
- P8 Q140's Chinese rendering adds "拨回时钟" to "Not every place changes." This is a contextual free translation (the sentence's P2 context is the clock change) and is acceptable as printed.
- P3's "Tell us your choice on page 7" points at the readers'-corner page, which invites letters generally but does not mention the film vote specifically. Loose cross-reference, not false; consider adding one line on P7 acknowledging film votes (carried over from round 1, still not a problem).
- P7's toolbox line "every phrase of the week comes from an article of this issue" is read, as in round 1, as referring to the 8 golden sentences (all verified verbatim); the three toolbox sentences themselves are teaching examples, not claimed verbatim quotes. This reading is NOT extended to problem 1 above, because problem 1's wording is a specific page attribution ("the word of the deep read (page 6)"), not a general toolbox claim.
- P8 reading/dialogue vignettes (Sam, the voting-place dialogue) are undated fiction set before a Tuesday; with no date printed they are internally consistent and are not affected by problem 2, which concerns only the explicitly dated P5 box.

## What must happen before finalizing

Fix problems 1–2, re-render the affected pages (P5, P7; full-issue re-render preferred so flows re-verify), and submit for a fresh full independent proof round. This report does NOT pre-approve any fix — fixes must be re-checked, not assumed.
