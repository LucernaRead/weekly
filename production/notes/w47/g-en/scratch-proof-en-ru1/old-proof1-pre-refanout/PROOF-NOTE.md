# PROOF-NOTE — Lucerna Weekly 2026-W47 en-ru, proof1

- **Edition:** English target, Russian reader (en-ru), VOL.4
- **Proofreader:** independent proof1 (SOP §8.4), not the builder
- **Date:** 2026-11-11
- **Object (verified on disk, SHA-256 re-checked 2026-11-11):**
  - Print PDF `The-Lucerna-VOL4-en-ru.pdf` — 29,241,566 B — `788cd0c08ec9b72fd52c8a65b4aadacb05e27980369295d7df0b726eb82efd70`
  - Web PDF `The-Lucerna-VOL4-en-ru.web.pdf` — 2,417,491 B — `da80486218d001cc6dc09e4107391cf81b15d1dde7f5c3b6d8e0aeb5f2ffe77a`
  - Text `2026-w47-en-ru.text.md` — 61,835 B — `5e8f7bf4f8e4b9d8c70c275f92e178fa03ee5b48b58da690f248415ab289dacb`
  - Both PDFs 8 pages, 1462.5×2025 pt.
- **Scope:** full text.md read (~1,306 lines); 150 exercise keys verified stem-by-stem; all 8 print pages viewed; web P1 + P8 rendered and viewed; every external fact checked against live sources; all mechanical gates run (see GATE-LOG.md).
- **No source files modified, no rebuild, no commit/push.**

## Verdict: (b) DEFECT LIST — not final

Five defects. Two are high severity (wrong answer key; factual error in the lead story). Per SOP §8.4 the edition is not final until a full proof round finds zero issues.

---

## Defect 1 — Q39/Q40 answer keys swapped (P3 matching) — HIGH

- **Location:** P3 matching exercise (definitions a–d) and P8 answers block ("38. b · 39. d · 40. a · 41. c"); also in the print-PDF text layer.
- **Rendered definition order** (confirmed in `svg/p3-culture.svg` lines 141–152 and in text.md):
  - a = "a person who teaches and guides you" → **mentor**
  - b = "a person chosen to take part in the Games" → tribute
  - c = "a person who lives with you in the jungle camp" → campmate
  - d = "the place where the Games are fought" → **arena**
- **Registry / text.md answers say:** 38 tribute→b ✓, **39 mentor→d ✗ (must be a)**, **40 arena→a ✗ (must be d)**, 41 campmate→c ✓.
- **Root: CORE-LEVEL.** Core-en registry is identical (`39 key 'd' note 'mentor=导师 d'`, `40 key 'a' note 'arena=竞技场 a'`). The swap lives in core; fixing it in en-ru alone would leave the other 11 native editions wrong. Report to coordinator; do not touch core.
- **Impact:** readers who answer correctly are marked wrong; the printed answer key is wrong.

## Defect 2 — Ashes story is one year stale (P4 lead + cross-references) — HIGH

- **Location:** P4 lead ("Saturday, November 21: Australia v England, first Test, Perth"); P1 IN BRIEF; P2 calendar; P5 golden sentence; P7 quote; P8 Q125.
- **What the paper says:** "Perth Stadium has never hosted an Ashes Test", "England's last tour skipped Perth", "The last series, in England in 2023, was drawn", "England lost 4–0 on their last two tours, in 2017–18 and 2021–22", Cummins out with a back injury / Smith captains / Boland replaces him / Doggett debuts.
- **Reality (verified 2026-11-11, Sky / CricTracker / Cricbuzz / BBC):** the 2025–26 Ashes first Test **was** Nov 21, 2025 at Perth Stadium — Australia won by 8 wickets in 2 days. By Nov 2026, Perth **has** hosted an Ashes Test, the last series was 2025–26 (not 2023), and England's last tour is 2025–26. The paper's details mirror Nov 2025 exactly (first ball 10:20 Perth = 02:20 London matches the paper's stated times). There is no Ashes series in Nov 2026.
- **Root: CORE-LEVEL.** The premise is in core-en; every native edition carries the same story. Report to coordinator; do not touch core.
- **Impact:** the P4 lead story — the edition's sport centrepiece — is factually false in its premise, and the error propagates to six other places in the issue.

## Defect 3 — P2 DID YOU KNOW? box bottom cuts through "November 3." — LOW–MEDIUM (cosmetic)

- **Location:** P2, DID YOU KNOW? cream box, last line.
- **Evidence:** box rect bottom 868.8 pt; the last line's span top 866.5 pt, baseline 882.6 pt — 663 ink px below the box bottom in the render. Zoom crop `render/p2-didyouknow.png` confirms the cream edge cuts through the line.
- **Root: CORE-LEVEL.** Identical in core-en (same 663 px) — the box is too short for its content in the core layout.
- **Impact:** cosmetic; the line is legible but visibly straddles the box edge.

## Defect 4 — P2 SAY IT mini-boxes 1–2: translation lines overflow the cream boxes horizontally — LOW (cosmetic)

- **Location:** P2, SAY IT boxes 1 and 2 (box 3 fits).
- **Evidence (PDF ink measurement):**
  - RU line 1 ink x 103–490 vs box [159,439] — 56 px left, 51 px right.
  - RU line 2 ink x 571–924 vs box [610,890] — 39 px left, 34 px right.
  - EN line 2 "The new Congress meets in January." ink x 574–931 vs box [610,890] — overflows both sides.
  - Visual crop `render/p2-sayit.png` confirms Russian text on white outside the cream.
- **Root: mixed.** EN line 2 overflow is **core-level** (identical in core-en). RU lines 1–2 overflow is **en-ru-specific**: the core Chinese lines fit (widths ~126–166 px vs Russian ~350 px); texts are centred on the box centres so the spill is symmetric.
- **Impact:** cosmetic; text is fully legible and does not overlap anything, but it sits on white outside the cream boxes.

## Defect 5 — P3/P4 column-3 box titles overflow the cream-box right edge — LOW (cosmetic)

- **Location:** P3 and P4, column-3 cream-box titles (PDF span measurement, budget 303.4 pt):
  - P3 "HAYMITCH'S GAMES　Игры Хеймитча" 323.8 pt → **over by 20.4 pt (~27 px)**.
  - P4 "SATURDAY, NOVEMBER 21　Суббота" 311.5 pt → **over by 8.1 pt (~11 px)**.
  - The other 8 col-3 titles pass (8 pass / 2 over; see `gates/boxtitle-ru.log`). Full-width crops of P3/P4 confirm the gloss tails sit on white past the cream edge.
- **Root: mixed.** P3 is **en-ru-specific** (core-en title 290.2 pt passes). P4 overflow exists in core too (core 307.0 pt, over by 3.6 pt) and is **worse in ru**.
- **Impact:** cosmetic; titles stay within the column and page and remain legible.

---

## Verified clean (summary — see GATE-LOG.md for per-gate evidence)

- **150 exercise keys:** 148/150 correct; only Q39/Q40 wrong (Defect 1). All other matching blocks verified (Q24–27, Q56–59, Q74–77, Q141–144). MCQ options, cloze, transforms, translations 137–140, dialogue 145–149, Q150 dash form all correct.
- **External facts (checked against live sources 2026-11-11):** US midterms exactly as printed — AP Nov 8 count Dem 254 / GOP 162 / 19 uncalled; Senate 20–13, 2 uncalled (Alaska, Mississippi); 7 flips incl. Texas/Kansas/Iowa/Ohio/Maine/NC/SC; 5 governors incl. Georgia/Iowa/Nevada/Ohio/Texas; going-in House 218–214, Senate 53–47; new Congress Jan 3, 2027; House GOP leadership elections Nov 10; Mike Johnson will not run as House GOP leader (NBC/AP Nov 4); House Democrats leadership elections Nov 18–19; Georgia majority rule, runoff would be Dec 1 (conditional phrasing in the paper is accurate; Ossoff in fact won outright Nov 3, so no runoff is needed — the paper never claims Georgia is uncalled). Anti-Bullying Week 2026 Nov 16–20, theme "Break the Silence", Odd Socks Day Mon Nov 16, 10th anniversary — exact. I'm a Celebrity 2026 Mon Nov 16, 9pm ITV1/ITVX, Ant & Dec, Murwillumbah NSW, Unpacked on ITV2 (Sam Thompson & Kemi Rodgers), launch a day late because Spain v England Nations League Sun Nov 15 — exact. Hunger Games: film Fri Nov 20, 2026; novel Mar 2025 (Mar 18); Joseph Zada = 16-yr-old Haymitch, McKenna Grace = Maysilee Donner, Ralph Fiennes = Snow, Francis Lawrence directs; 50th Games, Second Quarter Quell; soundtrack album Nov 13 (MCA, 29 tracks) — exact. ATP Finals Nov 15–22 Turin, field exactly Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Jodar; Sinner 2024+2025 champion, out with knee injury (Oct 6); semis Sat Nov 21, finals Sun Nov 22 — exact. NFL Week 11: Colts at Texans Thu Nov 19, 8:15pm ET; Vikings vs 49ers Mexico City Sun Nov 22, 8:20pm ET; Patriots on bye — exact. Premier League: Man City–Fulham Sat Nov 21 12:30; Newcastle–Arsenal 17:30; Liverpool–Man Utd Sun Nov 22 16:30 — exact. All weekday/date arithmetic in the paper verified (Nov 3 Tue, Nov 8 Sun, Nov 9 Mon, Nov 15 Sun, Nov 16 Mon, Nov 18 Wed, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun, Nov 26 Thu Thanksgiving, Dec 1 Tue). Arithmetic: 254+162+19=435 ✓; 20+13+2=35 ✓.
  - **Not separately verified** (minor/hedged in the paper, no contradiction found): certification window Nov 10–Dec 18; "Patriots, after Munich"; W.G. Grace photo credit (Herbert Rose Barraud); Rousseau "Surprised!" 1891; Lawrence children photo Feb 19, 1912; Samuel Johnson portrait (Reynolds, 1772); Library of Congress Reading Room photo (Carol M. Highsmith).
- **Mechanical gates:** occlusion audit 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–140, 150 — expected); freeze 8/8 byte-identical re-render; check_s11.ru all §1.1/P8 checks pass; print/web text identity (47,093 chars, token-multiset diff 0); P8 min font 10.12 pt ≥ 9.75 pt floor; quotes balanced (U+201C 81 / U+201D 81 in text.md; 82/82 across SVGs; U+2019 = 0); banned-word scan 0 hits; creambox P7 toolbox clean (all box contents inside, padding +4.5 to +92.4); no other overflow/overlap/truncation/footer-intrusion on P1, P3, P4, P5, P6, P8; footers "Страница N из 8" on all pages; masthead/edition line/badge correct; web P1/P8 match print.
- **Cyrillic quote note:** 0 Cyrillic-adjacent curly quotes in all 8 SVGs. The brief's P7 "чёрной пятнице" exception does not occur in this edition (lowercase "чёрной" appears nowhere; only capital "Чёрная пятница" unquoted in P2) — nothing to judge.

## Minor nits (not defects)

- KIT §3 "P8 min font 13.5 pt" conflates SVG px with pt — real rendered size is 10.12 pt, still above the ≥9.75 pt floor. Wording nit only.
- P5 line "У каждого ребёнка есть права | Every child has rights = У каждого ребёнка есть права." — the Russian is repeated redundantly. Stylistic nit, core-rooted.
- Q108 correction drops "in 2026" from the error sentence — grammatical, not flagged.

## Core-level candidates for the coordinator

1. Q39/Q40 swap (Defect 1) — core registry.
2. Ashes year-stale premise (Defect 2) — core story.
3. P2 DID YOU KNOW? box bottom cut (Defect 3) — core layout, identical in core.
4. P2 SAY IT EN line 2 overflow (part of Defect 4) — core layout, identical in core.
5. P4 box-title overflow, core portion (part of Defect 5) — core 307.0 pt vs 303.4 pt budget.

## En-ru-specific items (fixable in this edition alone)

- P2 SAY IT RU lines 1–2 overflow (Defect 4, Russian width).
- P3 box-title overflow by 20.4 pt (Defect 5) and the P4 aggravation (8.1 pt vs core 3.6 pt).

## Evidence paths (scratch dir)

`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-ru1/`
- `PROOF-NOTE.md` (this file), `GATE-LOG.md`
- `gates/` — occlusion.json/.log, p8-extract*.json/.log, p8-compare.json/.log, freeze.log, freeze-diff.json/.log, check_s11.log, printweb-diff.log, quote-diff.log, creambox.log, creambox-core.log, creambox-true.log, h-containment.log, boxtitle-ru.log, matching-check.log
- `render/` — web-p1-1.png, web-p8-8.png, p2-didyouknow.png, p2-sayit.png
