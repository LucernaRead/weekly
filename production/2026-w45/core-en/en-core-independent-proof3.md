# W45 English core VOL.2 — INDEPENDENT PROOFREAD, ROUND 3 (after fix round 2)

- Edition: `files/weekly-report-w45-en-core/` (8 SVGs, 8 PNGs, `The-Lucerna-VOL2.pdf` + `The-Lucerna-VOL2-web.pdf` at 8 pages each, `WEEKLY-KIT.md`, `ABSTRACT.txt`)
- Proofreader: independent (not the builder, not any fix agent). Round-1 report (`hidden_files/w45/en-core-independent-proof.md`), fix log 1 (`hidden_files/w45/en-core-fix1.md`), round-2 report (`hidden_files/w45/en-core-independent-proof2.md`), and fix log 2 (`hidden_files/w45/en-core-fix2.md`) were read but NOT trusted; every check below was re-run or re-read from the re-rendered edition itself.
- Method: SOP §§1–8 + occlusion appendix. SVG text extracted independently per page and read end to end; all 8 PNGs viewed as images; all dates re-checked with `date -d`; exercise numbering, all P8 keys, chart sums, model-essay word count, gloss anchoring, golden sentences, trend-pool + W43-promise compliance re-verified; `tools/occlusion_audit.py` run with `--selftest` first, then on the edition dir.
- Builder files were NOT edited. No git push, no Discord, no messages sent.

## VERDICT: ZERO PROBLEMS — FINALIZES THIS CORE

Per-area verdicts:

- Text (spelling/grammar/punctuation): CLEAN.
- Numbers (numbering, keys, chart, word count): CLEAN.
- Facts (dates, trend pool, red lines): CLEAN.
- Layout (overflow/overlap/footer/images/credits): CLEAN.
- Geometry (occlusion audit): CLEAN — tool selftest OK (all 6 planted classes fired, clean controls silent), edition run **0 flags**, and visual inspection of all 8 pages found no overflow, overlap, footer intrusion, or line-through-text.

## Round-2 fix verification (both verify on the rendered pages)

### Fix (a): P7 B2 "whether" no longer carries the false page-6 attribution — VERIFIED
- P7 LEVEL B2 column now reads: "Whether introduces an open question inside a sentence — more elegant than if, and safe everywhere. It is the word for election-night uncertainty."
- Old wording absent: case-insensitive grep of all 8 SVGs finds **zero** occurrences of "word of the deep read".
- "whether" occurs zero times on page 6 (P6 SVG grep = 0), and no page-6 claim for "whether" remains anywhere in the issue. Full "whether" census: P7 ×4 (column heading "WHETHER = IF ?", "Nobody knows whether…", "Whether introduces…", toolbox B2 sentence) and P8 ×5 (Q125 option, Q136 label, answer 125 note, answer 136 + its note) — all teaching uses with no page claim.
- The separate true attribution is untouched: the P7 B2 EXAMPLE box still reads "« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6)", and that sentence is verbatim from page 6. The P7 golden-sentence "(page 6)" for the same sentence is likewise intact and true.

### Fix (b): P5 SATURDAY SPORT box reframed to match P4 — VERIFIED
- P5 box now reads: "After Tuesday, the weekend keeps going : MLS fixtures on Saturday, November 7, including Charlotte against Inter Miami and Atlanta against the New York Red Bulls. The weekend warms up for Sunday's games."
- Old wording absent: all 8 SVGs contain **zero** occurrences of "Before Tuesday" and **zero** of "warms up before the vote".
- Fixtures and dates unchanged (Charlotte–Inter Miami, Atlanta–New York Red Bulls, Saturday November 7) and consistent with P4, which frames the same Saturday as the warm-up ("On Saturday, November 7, the warm-up is already on… The weekend starts on Saturday — and it does not stop."). `date -d` confirms November 7, 2026 is a Saturday, after Tuesday November 3.
- Visually clean on the P5 PNG: the box prints fully with clear space below, no crowding.

## Round-1 fix verification (all 11 still hold on the current render)

1. **P2 weekend wording — HOLDS.** "Two autumn rituals, one weekend — and both are now just passed, not coming." "one weekend apart" is gone.
2. **Bernabéu wording — HOLDS.** P7 B1: "« The Bernabéu is bigger than most stadiums. »" P8 Q123: "The Bernabéu is ___ than most stadiums." Key B (bigger). No "Madrid is bigger" remains.
3. **Past Simple column truthful — HOLDS.** P7 B1: "Use it for what is already finished — the clocks that fell back on November 1, and the « as-if-finished » retellings on page 4. The November 3 election and the November 8 games are still to come at press time, so their results are not past yet."
4. **P8 keys 76/77 — HOLD.** Answers read "76. b · 77. a" (a result = the final numbers of a vote; to call = to announce the winner).
5. **Q72/Q73 keys — HOLD.** Answers read "72. map · 73. phone", matching the P5 article's singulars.
6. **Q53 key — HOLDS.** Answer reads "53. begin", matching the P4 article's twice-printed "the WTA Finals begin".
7. **P3 Q36 uniquely answerable — HOLDS.** Stem: "Godzilla is bigger, darker, and ___ than ever this time." Key "louder" is now the only completion of the article's triple.
8. **Q122 note — HOLDS.** Answer reads "122. B（已发生的事用 fell）". Raw-SVG grep finds zero occurrences of "比赛用 fell" anywhere in the issue.
9. **Q126 future-honest — HOLDS.** Stem: "The film ___ on Friday, November 6. A. will open · B. will opened · C. will opens", key A, note "将来时 will + 动词原形". Only A is grammatical, and November 6 is future at the November 2 issue date.
10. **P2 gloss anchoring — HOLDS.** Gloss reads: "讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。" All three words occur in the P2 article; "daylight saving" occurs zero times in the P2 SVG (its P1 occurrence is a search term, not a gloss).
11. **14 P8 items badged — HOLDS.** Cloze 112–119 each carry a per-item badge (112 A2, 113 A2, 114 B1, 115 A2, 116 A2, 117 A2, 118 B1, 119 B1); writing heading reads "H · WRITING · 写作 [B1]"; dialogue carries "Levels : 145–148 [A2] · 149 [B1]". The range notation still passes: every dialogue item is named exactly once with exactly one level (145–148 → A2; 149 → B1). Recomputed printed split from the badges in this round: P1 A2 8 / B1 2; P2 A2 16 / B1 1; P3 A2 11 / B1 7; P4 A2 2 / B1 16; P5 A2 2 / B1 16; P6 B1 3 / B2 15; P7 A2 5 / B1 5 / B2 2; P8 A2 16 / B1 19 / B2 4 — total **A2 60 / B1 69 / B2 21 = 150**, exactly the KIT split.

## Fix-round risk re-check: P8 battery flow — PASSES
- The P8 PNG was viewed closely at the dialogue/Writing junction. The "Levels : 145–148 [A2] · 149 [B1]" line sits fully clear above the writing-strip rule with normal breathing room; nothing is struck through, crowded, or touching the MODEL box. In SVG coordinates the Levels baseline is y=1455.24 and the strip rule is y=1486 — over 30 px clear. The tight flow end (y=1483 vs bottom 1485) produces no visible crowding.

## Verified clean (re-checked independently in this round)

- Dates/weekdays: Nov 2 Mon, Nov 3 Tue, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Oct 31 Sat, Nov 1 Sun, Nov 11 Wed, Nov 15 Sun — all correct per `date -d` (America/Toronto).
- Exercise numbering: 1–150 continuous — all 150 keys present in the P8 answers section (the 8 section-lead items 1, 11, 28, 46, 64, 82, 100, 112 confirmed in place by direct reading); none missing, none repeated; per-page counts P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39, matching the KIT.
- P8 keys otherwise: all remaining keys re-derived against stems, articles, and sources — correct, including chart Q82–Q87 (38+29+21+12 = 100; 38−21 = 17), error clinic Q108–Q111, golden-sentence items Q100–Q107, cloze Q112–Q119, reading Q129–Q132, dialogue Q145–Q149, translation Q137–Q139, matching groups P2 24–27, P3 38–41, P4 56–59, P5 74–77, P8 141–144, and the Q35 "taller" / Q54–Q55 comparatives.
- Model essay: 81 words by standard word count (85 counting standalone punctuation tokens ":" / "«" / "!" / "»") — within the required 80–100 under either count. Writing prompts on P8 match the task; the model sentence "On Sunday night, the clocks had fallen back" is past-perfect-correct (by Sunday night the 2 a.m. change had already happened). All four writing prompts are covered (watched results, ate pizza, map showed, clocks sentence).
- Golden sentences: all 8 verified verbatim against this issue's own articles (P1, P2 ×2, P3, P4 ×2, P5, P6) — none imported from outside.
- Gloss anchoring otherwise: P1 (midterm/ballot/race/call a race), P3 (open/monster/catchphrase/series), P4 (fixture/title/defend/fan), P5 (map/too close to call/second screen), P6 (register/governor/shape laws/patience) — every word verified present in its page's article.
- All page cross-references checked: P1 → p.7 (readers' corner) and p.2 (clocks); P3 → p.7; P7 → pp.1, 2, 4, 5, 6 (all true: election story, clock sentences, comparatives, results sentence, patience sentence); P8 → p.7 (VOL.3 readers' corner). No false pointer remains.
- Explanation layer: every gloss, note, and answer explanation is in Chinese (the EN-core convention for Chinese-native readers); the English teaching text contains no Chinese except the intended glosses, and no English explanation text is left untranslated. No occurrence of 「桥接」 anywhere in the issue.
- Trend-pool compliance (checked against `hidden_files/w45/trend-batch-A.md`, EN section): Election Day Nov 3 lead; Oct 31/Nov 1 as just-passed reports; NFL Week 9 Madrid Bengals–Falcons at the Bernabéu + Dolphins–Lions Miami Nov 8; F1 São Paulo Nov 8 as the second race after the Austin US GP; NASCAR Homestead-Miami, WTA Finals Indian Wells, Baumgardner–Turhan Arlington Nov 8; MLS Nov 7 Charlotte–Inter Miami / Atlanta–New York Red Bulls; films Nov 6 (Cat in the Hat, Godzilla Minus Zero); Netflix Nov 4/5/6/8 slate — all pool-sourced.
- W43-promise compliance (checked against `hidden_files/w45/w43-promises.md`, EN section): Election Day Nov 3 honored as lead; Halloween Oct 31 and the Nov 1 clock change covered as just-passed reports; VOL.1's question ("what do Americans read, watch and eat while they wait") answered on P5; VOL.3 preview dates correct (Nov 11 Veterans Day, Nov 15 NFL Munich, midterm-results report). The real-letters + VOL.1-writing-review promise is NOT yet delivered — but it is honestly disclosed on P7 (see Observations), not fabricated, so it is not a new problem in this round.
- Red lines: no international politics (grep: zero occurrences of Ukraine/Putin/Kremlin/invasion/sanctions); no UK-ecosystem nodes (no Guy Fawkes / Remembrance); no Senate seats-up count printed (only "about a third" + chamber size 100); no governor count printed ("in many states"); no poll figures, predictions, or real-person quotes printed; practice ballot uses candidate codes A–D only; practice chart is labeled teaching data on the page ("The chart is teaching data, not a real poll") and in Q87; illustrative dialogue ("Did you see Ohio?", "Florida is close!") is unattributed generic speech, not a real-person quote.
- Readers'-corner honesty: P7's corner is explicitly labeled on the page ("editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled") with the matching Chinese editor's note; "M. L., a reader in Chicago" sits inside that labeled example, not presented as a real reader. The open debt (real letters + VOL.1 writing review, carried to VOL.3) is disclosed, not fabricated — same standing as rounds 1–2, not a new problem.
- Layout: all 8 PNGs viewed — no overflow, overlap, footer intrusion, or edge breach; P8 answers end above the footer; P2 clocks read 1:00 / 1:30 / 7:45 correctly; P6 practice-ballot checkboxes render as intended.
- Images/captions/credits: all 5 match the KIT — P1 voting booth (Kenneth C. Zirkel, CC0), P2 1912 Halloween postcard (public domain), P3 Manet "Cat and Flowers" with an explicit "Not film art" note (CC0), P4 1910 football (Frank R. Snyder, public domain), P6 Capitol (public domain).
- Masthead/pairing: "The Lucerna" masthead, "英语周报 VOL.2" pairing footer and "第 N 版 / 共 8 版" page lines on all 8 pages; 8 pages (multiple of 4); ABSTRACT.txt present and fact-consistent (Nov 2–8, Nov 3 election, clock change, Nov 6 films, Nov 8 Madrid/São Paulo sport, A2–B2, 150 exercises).
- PDFs: `The-Lucerna-VOL2.pdf` 8 pages, 31,114,501 bytes; `The-Lucerna-VOL2-web.pdf` 8 pages, 3,712,305 bytes — matching the fix-2 log.
- Geometry: selftest OK, edition run 0 flags, visual inspection clean (see verdict above). No thin line crosses any text on any page.

## Observations (NOT counted as problems)

- House style uses a space before "?" and ":" throughout ("Tuesday night ?", "America Votes : …"). It is systematic across all 8 pages (presumably family style), so it is not counted as a punctuation error here; if the family style is ever normalized to English punctuation, it must change everywhere at once.
- British spellings "colour" (throughout) and "maths" (P6, once) appear in a paper about American English. They are internally consistent and standard English variants, not errors; not counted.
- P8 Q140's Chinese rendering adds "拨回时钟" to "Not every place changes." This is a contextual free translation (the sentence's P2 context is the clock change) and is acceptable as printed.
- P3's "Tell us your choice on page 7" points at the readers'-corner page, which invites letters generally but does not mention the film vote specifically. Loose cross-reference, not false; carried over from rounds 1–2, still not a problem.
- P7's toolbox line "every phrase of the week comes from an article of this issue" is read, as in rounds 1–2, as referring to the 8 golden sentences (all verified verbatim); the three toolbox sentences themselves are teaching examples, not claimed verbatim quotes.
- P8 reading/dialogue vignettes (Sam, the voting-place dialogue) are undated fiction; with no date printed they are internally consistent.
- P2 Q18/Q19 "going to" drills are undated generic grammar transformations, not dated claims about this week; not affected by the tense-honesty fixes.
- KIT bookkeeping note (not an edition defect): KIT §1 still lists the pre-fix-2 PDF byte sizes (31,113,553 / 3,695,227) while the current files are 31,114,501 / 3,712,305 per the fix-2 log. Recommend a one-line KIT refresh; the printed edition and the PDFs themselves are unaffected.
- W43 promise debt remains open (real reader letters + VOL.1 writing review, carried to VOL.3 with honest on-page disclosure). It stays open until VOL.3 delivers it, but it is disclosed, not hidden, and does not block this core's finalization.

## Finalization statement

This is a complete fresh round, not a spot-check: all 8 pages were read end to end, all numbers re-derived, all dates re-checked, all 8 PNGs viewed, and the geometric audit re-run with a passing selftest. It finds **zero problems**. Both round-2 fixes verify, all 11 round-1 fixes still hold, and no new problem of any class was found. Per SOP §8.4, this core is finalized: **The Lucerna English core VOL.2 (W45) is approved for repo insert.** This report does not approve any other edition.
