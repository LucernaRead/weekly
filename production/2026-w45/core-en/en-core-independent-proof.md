# W45 English core VOL.2 — INDEPENDENT PROOFREAD (fresh eyes)

- Edition: `files/weekly-report-w45-en-core/` (8 SVGs, 8 PNGs, `The-Lucerna-VOL2-web.pdf`, `WEEKLY-KIT.md`, `ABSTRACT.txt`)
- Proofreader: independent (not the builder). Builder's record (`hidden_files/w45/en-core/PROOF-NOTE.md`, `occlusion2.json`) was read but NOT trusted; every check below was re-run or re-read from the rendered edition itself.
- Method: SOP §§1–8 + occlusion appendix. SVG text extracted independently per page and read end to end; all 8 PNGs viewed; all dates re-checked with `date -d`; exercise numbering, P8 keys, chart sums, model-essay word count, gloss anchoring, golden sentences, trend-pool compliance, and W43 promises re-verified; `tools/occlusion_audit.py` run with `--selftest` first, then on the edition dir.
- Builder files were NOT edited. No git push, no Discord, no messages sent.

## VERDICT: 11 PROBLEMS — NOT ZERO-PROBLEM, DO NOT FINALIZE YET

Per-area verdicts:

- Text (spelling/grammar/punctuation): PROBLEMS (nos. 1–3, 9, 10 below).
- Numbers (numbering, keys, chart, word count): PROBLEMS (nos. 4–7).
- Facts (dates, trend pool, red lines): CLEAN except no. 1 (a date-proximity wording error); all other facts verified clean (see "Verified clean").
- Layout (overflow/overlap/footer/images/credits): CLEAN.
- Geometry (occlusion audit): CLEAN — tool selftest OK (all 6 planted classes fired, clean controls silent), edition run **0 flags**, and visual inspection of all 8 pages found no overflow, overlap, or footer intrusion.

## Numbered problem list

### 1. P2 article — "one weekend apart" is factually wrong
- Location: P2, main article, paragraph beginning "Halloween and the clock change belong together in America".
- Printed: "Two autumn rituals, one weekend apart — and both are now just passed, not coming."
- Evidence: Halloween was Saturday, October 31, and the clocks went back at 2 a.m. Sunday, November 1 — hours apart, on the SAME weekend (the article itself states both dates two paragraphs earlier). "One weekend apart" implies separation by a week. Fix: e.g. "one weekend, two rituals" / "two autumn rituals, one weekend".

### 2. P7 B1 column + P8 Q123 — "Madrid" compared with stadiums (city vs. stadium)
- Locations: (a) P7, LEVEL B1 · COMPARATIVES: "Short adjective + -er + than : « Madrid is bigger than most stadiums. »"; (b) P8, Q123: "Madrid is ___ than most stadiums. A. big · B. bigger · C. biggest" (key: bigger).
- Evidence: Madrid is a city, not a stadium; the comparison subject should be the Bernabéu, as P4 Q54 correctly does ("The Bernabéu is ___ than most NFL stadiums."). As printed, both the teaching example and the test item state a category error. Fix both to the Bernabéu (or another stadium subject).

### 3. P7 B1 THE PAST SIMPLE — false claim about the issue's own pages
- Location: P7, LEVEL B1 · THE PAST SIMPLE: "Sports and election pages are written in this tense — every result is past."
- Evidence: False twice over. (a) The P4/P5 articles are written in present/future tense ("Sunday, November 8, is the biggest sports day…", "On Tuesday night, November 3, here is the answer…"), not past simple. (b) At this issue's date (Monday, November 2), the election (November 3) and the games (November 8) have NOT happened, so their results are not past. Note the builder already knew the distinction: P4's D-section is explicitly framed as hypothetical ("比赛已结束的说法"). Fix: rewrite the column's claim (e.g. past simple is the tense of the exercises' "as-if-finished" retellings, not of the articles or of results at press time).

### 4. P8 answers — P5 matching keys 76/77 are SWAPPED
- Location: P8 ANSWERS, "— 第 5 版 —": "76. a · 77. b".
- Evidence: P5 matching items are 76. a result / 77. to call, with options a. "to announce the winner of an election" / b. "the final numbers of a vote". A result is the final numbers (b); to call is to announce the winner (a). The printed keys are exactly reversed. Correct: 76 → b, 77 → a. (All other matching groups — P2 24–27, P3 38–41, P4 56–59, P8 141–144 — were checked and are correct.)

### 5. P8 answers — Q72/Q73 keys pluralize the article's own singular phrases
- Location: P8 ANSWERS: "72. maps · 73. phones".
- Evidence: P5 article (the source of both stems) says "Every channel has its own map" (singular) and "hands free for the phone" (singular). Stems: Q72 "Every channel has its own ___." / Q73 "Hands free for the ___." The expected completions from the article are "map" and "phone"; the keys "maps"/"phones" contradict the article's own wording. Fix keys to map / phone.

### 6. P8 answers — Q53 key "begins" contradicts the issue's own article
- Location: P8 ANSWERS: "53. begins".
- Evidence: The P4 article twice uses the plural verb for this subject: "the WTA Finals begin at Indian Wells" (article body) and "WTA Finals begin, Indian Wells." (Sunday schedule box). Stem Q53: "The WTA Finals ___ on Sunday." The key should match the issue's own usage: "begin". (External usage debates aside, an answer key must not contradict the issue's own article.)

### 7. P3 Q36 — underdetermined item: three correct completions, key accepts one
- Location: P3, B · SENTENCES, Q36: "Godzilla is ___ than ever this time." Key (P8): "36. louder".
- Evidence: The P3 article sentence is "bigger, darker, and louder than ever" — bigger, darker, and louder are ALL grammatically and factually valid completions of the stem. A single-answer key marking only "louder" correct is indefensible as printed. Fix: accept all three, or reword the stem to pin one adjective (e.g. quote the full triple, or specify "loudest-sounding").

### 8. P8 answers — Q122 note is a copy-paste error ("比赛")
- Location: P8 ANSWERS: "122. B（已发生的比赛用 fell）".
- Evidence: Q122 is "The clocks ___ back on Sunday." — about clocks falling back, not a match/game ("比赛"). The note's rationale names the wrong topic entirely (apparently copied from a sports item). Fix the note to clocks, e.g. "已发生的事用 fell".

### 9. P8 Q126 — past tense used for a future event, with no hypothetical framing
- Location: P8, B · MULTIPLE CHOICE, Q126: "The film ___ on Friday, November 6. A. opened · B. open · C. opens" (key: opened; note: "过去的事用过去式 opened").
- Evidence: This issue is dated Monday, November 2; the November 6 opening is still in the future at press time, so "opened" + "过去的事" (a past event) is temporally wrong as printed. Contrast P4's D-section, which explicitly frames its past-simple items as hypothetical ("比赛已结束的说法"); Q126 carries no such framing. Fix: reframe the stem (e.g. set it after Friday) or change the item to a future/going-to form.

### 10. P2 gloss — "daylight saving" does not occur in the article it annotates
- Location: P2, gloss line: "译注｜讲解｜to fall back（时钟）拨回 · daylight saving 夏令时 · a costume…".
- Evidence: The P2 article never uses "daylight saving" (it says "spring forward, fall back" and "change the clocks"); the phrase occurs elsewhere only in P1's search list and in this gloss itself. SOP §8 requires each glossed word to actually appear in the core text it annotates. Fix: either introduce the term in the P2 article or drop it from the P2 gloss (the other three P2 gloss words — fall back, costume, trick or treat — all check out; all other pages' glosses were verified anchored).

### 11. P8 — 14 items carry no printed level badge (SOP §4)
- Location: P8, section A cloze (112–119), section G dialogue (145–149), section H writing (150).
- Evidence: SOP §4 requires every question to be individually labeled [A2]/[B1]/[B2]. P8 sections B–F do label each item, but A, G, and H print no level badge at all. Consequence: the KIT's level split (A2 60 / B1 69 / B2 21) cannot be verified from the printed page for these 14 items — labeled items sum to A2 51 / B1 64 / B2 21, leaving A2 9 / B1 5 to be taken on trust. Fix: print a level badge on each of these 14 items (and confirm the KIT split then matches).

## Verified clean (re-checked independently, no problem found)

- Dates/weekdays: Nov 2 Mon, Nov 3 Tue, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Oct 31 Sat, Nov 1 Sun, Nov 11 Wed, Nov 15 Sun — all correct per `date -d`.
- Exercise numbering: 1–150 continuous, no gap or repeat; per-page counts P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39, matching the KIT.
- P8 keys otherwise: all remaining keys re-derived against stems, articles, and sources — correct, including chart Q82–Q87 (38+29+21+12 = 100; 38−21 = 17), error clinic Q108–Q111, golden-sentence items Q100–Q107, cloze Q112–Q119, reading Q129–Q132, dialogue Q145–Q149, and translation Q137–Q139.
- Model essay: 81 words by standard word count (builder's "85" counts standalone punctuation tokens); within the required 80–100 under either count. Topic prompts on P8 match the writing task.
- Golden sentences: all 8 verified verbatim against this issue's own articles (P1, P2 ×2, P3, P4 ×2, P5, P6) — none imported from outside.
- Trend-pool compliance: Election Day Nov 3 leads; Oct 31/Nov 1 treated as just-passed reports (P2: "both are now just passed, not coming"); VOL.1's question ("what do Americans read, watch and eat while they wait") answered on P5; VOL.3 preview dates correct (Nov 11 Veterans Day, Nov 15 NFL Munich, midterm-results report). No Senate seats-up count printed (only "about a third" + chamber size 100); no governor count printed ("in many states"); no poll figures, predictions, or real-person quotes printed; practice ballot uses candidate codes A–D only; practice chart is labeled teaching data on the page ("The chart is teaching data, not a real poll") and in Q87.
- Red lines: no international politics; no UK-ecosystem nodes (no Guy Fawkes / Remembrance); no invented polls/quotes/predictions; illustrative dialogue ("Did you see Ohio?", "Florida is close!") is unattributed generic speech, not a real-person quote.
- Gloss anchoring otherwise: P1 (midterm/ballot/race/call a race), P3 (open/monster/catchphrase/series), P4 (fixture/title/defend/fan), P5 (map/too close to call/second screen), P6 (register/governor/shape laws/patience) — every word verified present in its page's article.
- Layout: all 8 PNGs viewed — no overflow, overlap, footer intrusion, or edge breach; P8 answers end above the footer; clocks on P2 read 1:00 / 1:30 / 7:45 correctly.
- Images/captions/credits: all 5 match the KIT — P1 voting booth (Kenneth C. Zirkel, CC0), P2 1912 Halloween postcard (public domain), P3 Manet "Cat and Flowers" with an explicit "Not film art" note (CC0), P4 1910 football (Frank R. Snyder, public domain), P6 Capitol (public domain).
- Masthead/pairing: "The Lucerna" masthead, "英语周报 VOL.2" pairing footer and "第 N 版 / 共 8 版" page lines on all 8 pages; 8 pages (multiple of 4); ABSTRACT.txt present and fact-consistent.
- Geometry: see verdict above — 0 flags, selftest passed.

## Observations (NOT counted as problems)

- House style uses a space before "?" and ":" throughout ("Tuesday night ?", "America Votes : …"). It is systematic across all 8 pages (presumably family style), so it is not counted as a punctuation error here; if the family style is ever normalized to English punctuation, it must change everywhere at once.
- P8 Q140's Chinese rendering adds "拨回时钟" to "Not every place changes." This is a contextual free translation (the sentence's P2 context is the clock change) and is acceptable as printed.
- P3's "Tell us your choice on page 7" points at the readers'-corner page, which invites letters generally but does not mention the film vote specifically. Loose cross-reference, not false; consider adding one line on P7 acknowledging film votes.
- P7's toolbox line "every phrase of the week comes from an article of this issue" was read as referring to the 8 golden sentences (all verified verbatim); the three toolbox sentences themselves are teaching examples, not claimed verbatim quotes.

## Open promise debt (disclosed by the builder, NOT a hidden defect)

- W43 promised VOL.2 would print REAL reader letters and review VOL.1's P8 writing. Neither is delivered in VOL.2: no real letters/submissions had arrived. This is NOT a fabrication — P7's readers'-corner is explicitly labeled on the page ("editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled") with a matching Chinese editor's note, and the KIT §8 records it the same way. The "M. L., a reader in Chicago" name sits inside that labeled example, not presented as a real reader. The debt (real letters + VOL.1 writing review) is carried to VOL.3, which P7's corner promises ("VOL.3 起刊登收到的真实来信"). This debt does not add to the problem count, but it stays open until VOL.3 delivers it.

## What must happen before finalizing

Fix problems 1–11, re-render the whole issue, and submit it for a fresh full independent proof round. This report does NOT pre-approve any fix — fixes must be re-checked, not assumed.
