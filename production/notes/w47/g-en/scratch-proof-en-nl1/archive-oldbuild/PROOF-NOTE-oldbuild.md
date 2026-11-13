# PROOF-NOTE — Lucerna Weekly 2026-W47, edition en-nl (proof1)

- **Edition:** English target, Dutch reader (`production/2026-w47/2026-w47-en-nl/`)
- **Proofreader:** independent proof1 (SOP §8.4); not the builder.
- **Date:** 2026-11-11 (Toronto, America/Toronto)
- **Scope:** full text.md read; 150/150 answer keys checked against stems; 8 print pages + web P1/P8 visually inspected from fresh renders; external facts verified item by item; all mechanical gates run (see GATE-LOG.md).
- **Core:** `core-en` already finalized. Defects rooted there are reported as **core-level candidates**; core was not touched.

## Conclusion: (b) — defect list

Four defects. Three are core-level (root in `core-en`, shared by all 11 fanouts — the same wrong content will print in every edition); one is nl-level.

---

## Defect 1 — CORE-LEVEL, HIGH — P3 matching keys 39/40 swapped (wrong answers printed)

**Where:** P3 section C "THE WORDS" (38–41) + P8 ANSWERS "— Pagina 3 —" + appendix keys 39/40 in `2026-w47-en-nl.text.md` + `registry.json` (nl and core identical).

**Printed definitions (verified in the rendered P3 SVG, x≥1000, and visually):**
- a. "a person who teaches and guides you" (y=1079)
- b. "a person chosen to take part in the Games" (y=1150)
- c. "a person who lives with you in the jungle camp" (y=1221)
- d. "the place where the Games are fought" (y=1292)

**Terms:** 38. a tribute → b ✓; **39. a mentor → printed key d, correct key a**; **40. the arena → printed key a, correct key d**; 41. a campmate → c ✓.

**Effect:** two of four matching items in section C are marked wrong for every reader who answers correctly. The P8 answer block prints "39. d · 40. a", so the wrong keys are the ones a reader checks against.

**Root:** core registry (`core-en/registry.json` carries the same 39=d, 40=a). Fix must land in core and re-fanout, or be repaired in every edition the same way.

---

## Defect 2 — CORE-LEVEL, HIGH — The Ashes cluster is a year stale: the 2025–26 Ashes transposed to November 2026

**Where (all in core text, fanout repeats it):**
- P1 IN BRIEF — "ASHES — Sat Nov 21: Australia v England, first Test, Perth. (p. 4)"
- P2 "WHAT IS ON THIS WEEK?" — "On Saturday, November 21, the Ashes begin in Perth — at 2:20 a.m. London time."
- P4 feature "Saturday in Perth: The Ashes Are Back" (whole article) + Q46 (key A rests on the false premise)
- P5 "THE JUNGLE, TOO" — "the Ashes begin on Saturday morning in Perth"
- P7 NEXT WEEK — "The Ashes, second week in Perth"
- P8 Q125 — key C "Sat, Nov 21" (answer follows the false premise)

**What is false, verified against the 2025–26 record:**
- The 1st Test at Optus Stadium, Perth, was **Friday Nov 21, 2025**; Australia won by 8 wickets on Nov 22, 2025. The series was won by Australia **4–1** (Brisbane Dec 4, Adelaide, Melbourne — England won, Sydney Jan 4–8, 2026). There is no first Ashes Test in Perth in November 2026; the next Ashes series is not this winter.
- "Perth Stadium has never hosted an Ashes Test" — false; it hosted the 2025 opener.
- "England's last tour skipped Perth" — false for the last tour (2025–26 included Perth); true only of 2021–22.
- "lost 4–0 on their last two tours, in 2017–18 and 2021–22" — false as a two-tour record: 2025–26 was 4–1 and England won in Melbourne, their first Test win in Australia since 2010–11.
- "Brendan Doggett may play his first Test" — Doggett debuted in November 2025.
- "Day one is already sold out" / "Scott Boland takes Cummins's place" as a fresh event — 2025 facts.
- "First ball 10:20 local / 2:20 GMT", "Nov 21–25 window", "Dec 4 Brisbane 2nd Test", and the core KIT's England XII — all match the 2025 fixture exactly.

**Still true (checked, not defects):** England's last series win in Australia was 2010–11 (Q49 key A ✓); the 2023 home series was drawn; India beat Australia by 295 runs in Perth in November 2024 (Q63 ✓); Q60–63 keys are fine. Q46's key A is "correct" only inside the paper's own false premise.

**Effect:** the P4 feature — the edition's whole sport lead — reports a series that happened a year earlier as if it starts this Saturday. A reader who follows cricket will spot it immediately; a learner will learn false facts.

---

## Defect 3 — CORE-LEVEL, MODERATE — P7 NEXT WEEK promises "the certified results" for VOL.5

**Where:** P7 "NEXT WEEK · Vooruitblik VOL.5" — "…The certified results of the midterm election."

**Why it fails:** state certification runs **November 10 to December 18** (verified: Ballotpedia 2026 table; Arkansas certifies Dec 18, the latest fixed state date; Mississippi Dec 31; five states set no fixed date). VOL.5 covers Nov 23–29, so certified results cannot be complete by then. P6 words it correctly and conditionally ("When the certified results are in, VOL.5 will report them"); the P7 line is a flat promise.

**Fix direction:** reword to what VOL.5 can actually carry (e.g. "the count so far" / "more certified results"), in core.

---

## Defect 4 — NL-LEVEL, MINOR — French guillemets « » in Dutch text

**Where:** `2026-w47-en-nl.text.md`, 4 places:
- line 993 — P8 H instruction: «Mijn maandag 16 november»
- line 1135 — Q65 note: «Doorbreek de stilte»
- line 1181 — Q88 note: «De uitslag bekendmaken»
- line 1257 — Q126 note: «Doorbreek de stilte»

Dutch convention is “…” (curly double quotes); « » is French/Spanish/Italian usage. The guillemets print on P8 — visible in the render in the H instruction and in answer notes 65 and 126 (Q88's note is in the source text and its extracted P8 key matches the registry verbatim). The same « » is correct in the fr/es/it fanouts; in nl it is a style error carried over from the shared template.

---

## Observations (not defects)

1. **Widowed section heads (cosmetic):** P4 "B SENTENCES" and P5 "D PRESENT CONTINUOUS" heads sit at the bottom of a column with their items at the top of the next column. Readable, just untidy.
2. **P1 kicker tension:** "Bevestigde uitslag" ("confirmed result") sits next to an article that stresses "a call is not the official result". The paper consistently labels the figures as Nov 8 calls, so this is not a defect — noted only.
3. **House triple 254/162/19 (P1/P6) is a live-count snapshot, not a confirmed error.** AP's Nov 8 call as cited by the core KIT (4 sources, 9pm ET Nov 8) is 254/162/19; other trackers at nearby times showed 252/161/22 (political.org, Nov 8), 254/163 (poliwave, Nov 10), 252/162/21 (NBC, Nov 7). Live counts moved as races were called; the paper dates its figures to Nov 8 and the arithmetic (254+162+19=435) checks out.
4. **Georgia runoff (P2/P6):** phrased conditionally ("if needed"); the Georgia race was among the 33 called, so no live runoff exists — the conditional wording keeps it true.
5. **P5 "FRIDAY'S WORDS":** "Elk kind heeft rechten | Every child has rights = Elk kind heeft rechten." — the gloss repeats the Dutch (Dutch | English = Dutch). Harmless TM carryover.

---

## What was verified and is correct

**External facts (web-verified 2026-11-11):**
- **Midterms:** Democrats won both houses. Senate 20D/13R of 35 called, 2 uncalled (Alaska, Mississippi); 7 flips, all to D (IA, KS, ME, NC, OH, SC, TX); governors 5 flipped (GA, IA, NV, OH, TX). Before: House R 218–214, Senate R 53–47; majority 218.
- **Mississippi:** no runoff in a regular federal general election (plurality wins; the 2018 runoff was a special election). MS race uncalled, Colom leading Hyde-Smith by ~2,633 (Nov 10 count).
- **Mike Johnson** will not run for House GOP leader (NBC/AP, Nov 4); House GOP vote Nov 10; new Congress Jan 3, 2027; House Democrats' leadership votes Nov 18–19 (Axios/Politico).
- **I'm a Celebrity 2026:** Mon Nov 16, 9pm, ITV1/ITVX, Ant & Dec, Murwillumbah NSW, Unpacked on ITV2 (Sam Thompson & Kemi Rodgers); launch a day late because England v Spain, Nations League, Sun Nov 15. **The one-off special "How to Survive the Jungle": Sun Nov 15, 6pm, ITV1/ITVX** (Wikipedia series 26; tvzoneuk; memorabletv).
- **Anti-Bullying Week 2026:** Mon 16–Fri 20 Nov, theme "Break the Silence", Odd Socks Day Mon 16 Nov, 10th anniversary (started 2017), Anti-Bullying Alliance, theme shaped by 200+ children. **Figures check:** NCB (Feb 2026) — "reach 8 million children and young people through Anti-Bullying Week resources each year"; "Over 80% of schools mark the week" (Teachwire; ABA's own doc: "estimated 80% of schools in the UK taking part reaching over 7.5 million"). The paper's "about eight million children" and "more than 80% of schools" match the ABA's own headline figures.
- **Hunger Games:** film Fri Nov 20, 2026 (Lionsgate); soundtrack album Nov 13 (MCA, 29 tracks); Francis Lawrence directs; Joseph Zada as Haymitch, McKenna Grace, Ralph Fiennes as young Snow; novel 2025 (Collins); 50th Games / Second Quarter Quell, twice as many tributes.
- **ATP Finals 2026:** Nov 15–22, Turin; the 8 players named are exactly right (Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Jódar); Sinner, two-time defending champion, out with right-knee injury (announced Oct 6).
- **Premier League:** Sat Nov 21 Man City–Fulham 12:30, Newcastle–Arsenal 17:30; Sun Nov 22 Liverpool–Man Utd 16:30 — exact.
- **NFL Week 11:** Thu Nov 19 Colts at Texans 8:15pm ET (Prime Video); Sun Nov 22 Vikings vs 49ers, Mexico City, 8:20pm ET (NBC); Patriots bye Week 11 after the Munich game vs Lions Sun Nov 15, 9:30am ET.
- **World Children's Day 2026:** Fri Nov 20; UNICEF theme "My day. My rights. My future."; CRC adopted Nov 20, 1989.
- **Certification window:** Nov 10–Dec 18 (Ballotpedia; congresscountdown), Arkansas Dec 18 latest fixed date, Mississippi Dec 31, five states no fixed date.

**In-paper checks:** 150/150 answer keys verified against stems (except defects 1–2 above); all matching sets verified (P2 D, P4 C, P5 C, P8 F); P6 chart arithmetic 254+162+19=435 ✓; P7 golden sentences 8/8 verbatim against this issue's articles ✓; H MODEL text 82 words (80–100 required) ✓; weekdays for all 16 dates named in the paper verified against `date` (America/Toronto) — all match; per-page exercise counts 10/17/18/18/18/18/12/39 = 150; levels A2 62 / B1 66 / B2 22; numbering continuous 1–150.

**Visual check (fresh renders, all 8 print pages + web P1/P8):** no overflow, overlap, or clipped text; P2 SENATE title gap confirmed visually (the earlier tight-title fix holds); P7 TOOLBOX all three lines inside the cream box with clear space below; P8 answers block ends well above the footer; all 8 footers "Pagina N van 8"; all images with correct captions and PD/CC0 credits; CREDITS.md verified (note: the "johnson" portrait is **Samuel** Johnson, 1772, Reynolds — not Mike Johnson).

## Items explicitly NOT flagged
- House-count snapshot variance (see observation 3) — plausible live-count movement, core KIT cites its sources.
- Anti-Bullying Week reach figures — verified against ABA/NCB's own numbers.
- Georgia runoff — conditional wording, true as stated.
