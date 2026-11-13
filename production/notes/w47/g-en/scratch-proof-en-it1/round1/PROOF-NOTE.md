# PROOF NOTE — Lucerna Weekly 2026-W47 · en-it · proof1

**Edition:** English target × Italian readers (`2026-w47-en-it`), VOL.4, issue week 2026-11-16..22
**Proofreader:** independent proof1 (SOP §8.4), not the builder
**Date:** 2026-11-11
**Conclusion: (b) 缺陷清单 — NOT zero-defect. 2 defects (D1 SEVERE, D2 MODERATE).**

## Objects verified (SHA-256, all MATCH KIT §2 / on-disk)

| File | Size | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-it.pdf` (print) | 29,326,709 B | `195e155228e63515d3133a32cebbbee71c3dccf973387d4c1c2f614670e3da26` |
| `The-Lucerna-VOL4-en-it.web.pdf` (web) | 2,372,517 B | `995339d48612cc9344a5213e38026a9cda9a1de910efb268308fa9e877064a46` |
| `2026-w47-en-it.text.md` | 53,373 B | `a9cbd2f18c6ecfeebf86dfe68558ab9d1145ce7fc4476b8004b610bb7e4805ec` |

Both PDFs 8 pages (pdfinfo). Probe passed before work (`hash-object` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; `probe.txt` written in scratch).

## What was checked

- Full read of `text.md` (~1,306 lines): all 150 answers checked against their stems — 148 correct, 2 wrong (D1). Per-page counts 10/17/18/18/18/18/12/39 = 150 (A2 62 / B1 66 / B2 22, matches KIT §1).
- All 8 print pages rendered and read visually (`render/p-1.png`…`p-8.png`); web P1 and P8 rendered and read (`render/w-1.png`, `w-8.png`).
- External facts verified by web search (details in GATE-LOG §5): US midterms (House 254D/162R/19 uncalled, Senate 20D/13R of 33, 7 flips, 5 governors flipped, pre-vote 218R–214D / 53R–47D, new Congress Jan 2027), Mike Johnson not running for House GOP leader (vote Tue Nov 10), Hunger Games: Sunrise on the Reaping (Fri Nov 20, Zada/Grace/Fiennes, Lawrence directing, 50th Games, soundtrack Nov 13), I'm a Celebrity s26 (Mon Nov 16, 9 p.m., Ant & Dec, Murwillumbah; launch one day late because England–Spain Sun Nov 15), Ashes 1st Test Perth Sat Nov 21 (first ball 10:20 local = 02:20 London; Cummins out, Smith captains, Boland in; Hazlewood out; England last series win in Australia 2010–11; Australia lost first Perth-Stadium Test Nov 2024 by 295 runs to India), ATP Finals Turin Nov 15–22 (field Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Jódar; Sinner defending champion out with knee injury; semis Sat Nov 21, finals Sun Nov 22), Premier League Nov 21–22 fixtures, NFL Week 11 (Colts–Texans Thu Nov 19; Vikings–49ers Mexico City Sun Nov 22; Patriots bye after Munich), Anti-Bullying Week Nov 16–20 theme "Break the Silence", Odd Socks Day Mon Nov 16, 10th anniversary, ~8 million children / 80%+ schools, World Children's Day Fri Nov 20, CRC adopted 1989; all dates/weekdays re-checked with `date -d` (America/Toronto). No contradictions found.
- Mechanical gates: see GATE-LOG.md (occlusion 0, p8 compare CLEAN, freeze 8/8, print/web text identical, P8 min font 10.12 pt ≥ 9.75 floor, creambox all positive, boxtitle 31/31 fit, keycheck-equivalent 149/150 with only the expected Q150 dash-split, quotes balanced, forbidden terms 0, CJK = U+3000 separators only).

---

## D1 — P3 matching keys Q39/Q40 swapped (SEVERE: wrong answer key; CORE-ROOTED)

**Location:** P3 exercise C · THE WORDS (`svg/p3-culture.svg`, also printed in P8 answers block, `registry.json`, `text.md`).

**Printed definitions (SVG-verified, both this edition and core-en):**
- a = "a person who teaches and guides you"
- b = "a person chosen to take part in the Games"
- c = "a person who lives with you in the jungle camp"
- d = "the place where the Games are fought"

**Keys as printed (all three sources agree with each other):** Q38=b tribute ✓, **Q39=d, Q40=a**, Q41=c campmate ✓.

**Correct keys:** 39. a mentor = a person who teaches and guides you → **a**; 40. the arena = the place where the Games are fought → **d**. As printed, Q39=d and Q40=a are both wrong.

**Why no gate caught it:** registry, `text.md`, and P8 print all agree, so p8 compare (CLEAN) and the registry-vs-print consistency check are blind to it; the error is only visible against the printed exercise definitions.

**Root:** core-en. Core registry has identical Q39=d ("mentor=导师 d"), Q40=a ("arena=竞技场 a"), and core-en `svg/p3-culture.svg` has the same definition order. **Core-level candidate — report to coordinator; do not touch core.** The fix (Q39→a, Q40→d) must land in core-en and propagate to all fan-out editions; every other edition inherits the same wrong keys.

**Scope check:** all other matching sets verified correct against their printed definitions: P2 Q24–27, P4 Q56–59, P5 Q74–77, P8 Q141–144. All other 148 answers manually checked against stems and found correct (including MCQs, cloze Q112–119, P6 chart arithmetic 254+162+19=435, Q84 "33 of 35", P7 drills/error clinic Q100–111, dialogue Q145–149, translations Q137–140).

---

## D2 — P2 SAY IT cream boxes: centred lines wider than their boxes (MODERATE: visible layout defect; MIXED root)

**Location:** P2, SAY IT strip, three cream boxes (all 280 px wide, y=1636, h=132).

**Measurements** (PIL true-ink, Newsreader SemiBold 20 for English; Noto Sans CJK SC Regular 20, face index 2, for Italian; confirmed visually on the rendered P2 — the lines plainly stick out past the cream panels on both sides):

| Box | Line | Ink span | Spill |
|---|---|---|---|
| box2 x=610–890 | EN "The new Congress meets in January." | 574.0–926.0 | **36.0 px left + 36.0 px right** |
| box2 x=610–890 | IT "Il nuovo Congresso si riunirà a gennaio." | 568.2–932.2 | **41.8 px left + 42.2 px right** |
| box3 x=1060–1340 | IT "Buon Giorno del Ringraziamento!" | 1045.1–1355.1 | **14.9 px left + 15.1 px right** |

Box1 (x=159–439) is clean: EN margins 22/22, IT margins ~11.5. Box3 EN "Happy Thanksgiving!" margins ~35 ✓.

**Root attribution:**
- Box2 **English** line x=574.0 is identical in core-en (core SVG same coordinates) → **core-rooted**.
- Core's Chinese lines fit inside their boxes (box2 "新国会在一月开会。" x=660; box3 "感恩节快乐！" x=1140), so the two **Italian** overflows are **edition-local** (Italian translations longer than the core Chinese and longer than the 280 px boxes).

**Why no gate caught it:** text is drawn after its box and nothing covers it, so the occlusion audit (0 flags) is blind to this class — same blindness as the de toolbox case. A full-edition horizontal-overflow scan was run with an overlap-≥0.5 membership filter: exactly these 3 lines are real hits; an earlier broad scan (`gates/h-overflow.log`, loose filter) is full of neighbouring-column false positives and must NOT be cited as evidence.

**Fix direction (for coordinator/fix agent):** shorten or wrap the three lines, reduce the SAY IT font, or widen the boxes. Box2 English line requires a core fix (or a per-edition override); the two Italian lines are fixable edition-locally.

---

## Observations (not defects)

1. **P8 min font 10.12 pt vs KIT §3 claim 13.5 pt.** Measured minimum span (PyMuPDF, both PDFs) is 10.12 pt on P8 and all pages (smallest spans are answer-note lines, e.g. "(Al Senato, 33 seggi su 35 sono già stati decisi)…"). 13.5 pt is the configured answers-block font size, not the measured minimum. 10.12 pt still passes the SOP §1.1 floor of 9.75 pt. Observation only.
2. **P2 AND YOU box tight but inside.** Corrected creambox: last baseline 1512.8, box bottom 1517.9, clearance +5.0. Last line is "redazione." — no descender letters — so ink ends at the baseline, ~5 px inside the box edge. Tight, not a spill. No PIL ink measurement was done on it; not needed given the glyph shapes.
3. **P7 column-break continuation.** The irregular-verbs list "win → won, lose → lost, beat → beat, choose" ends at the bottom of column 1; "→ chose, run → ran." continues at the top of column 2. Readable, in order, no content loss. Not a defect.
4. **Unverified (not contradicted) claims:** "Day one [Ashes] is already sold out" (P4); "ATP singles final not before 6 p.m. local" (P4); World Children's Day 2026 theme "My day. My rights. My future." (P5); "House Democrats vote November 18 and 19" (P2). No independent source confirmed or contradicted them.
5. **Known accepted/quirky items (KIT §6) — NOT re-flagged:** Q2/Q95 "proclamare il risultato" (TM) vs P6 gloss "annunciare il risultato" (both correct); Q105 vs Q136 "whether = se" variants; Q54 note "eight (otto = eight)" tautological like core; Q34 "(open = uscire (terza persona singolare con -s))"; Q110 "more than, la struttura" terse as in core; "Cinque frasi | who, where, cosa è successo, la svolta, la fine" is the W46 it TM value (kept); Q40 gloss "arena = lo stadio" is loose but not flagged.
6. One aggregator (political.org) showed House 252/161/22 vs the paper's 254/162/19 — minority figure; the paper matches the majority of sources (AP-based guides).

## Files

- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-it1/`
- Gates: `gates/` (occlusion, p8, freeze, creambox, boxtitle, keycheck-150, h-overflow, print/web text)
- Renders: `render/p-1.png`…`p-8.png` (print), `render/w-1.png`, `render/w-8.png` (web), `render/p2-sayit.png`, `render/p7-toolbox.png` (crops)

## Recommendation

Fix D1 in core-en (Q39→a, Q40→d) and propagate; fix D2 (shorten/wrap/shrink the three SAY IT lines, or widen the boxes — box2 English in core, Italian lines edition-local). Re-proof after fix. Do NOT ship as-is: D1 prints two wrong answer keys.
