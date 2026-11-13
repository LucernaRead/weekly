# FIX-LOG — W47 core-en fix 1 (2026-11-11)

Fixer: core-en subagent (fix1). Scope: `production/2026-w47/core-en/` ONLY.
No fan-out edits, no `tools/` edits, no commit, no push.
Work log + scripts: `hidden_files/w47/scratch-fix-core-en1/`
(`sweep_ink.py`, `sweep_sayit.py`, `dump_reg_fix1.py`, `make_textmd_fix1.py`,
`keycheck_fix1.py`, `dump_keyverify_fix1.py`, `audit_110_fix1.py`, `tmp/`).

## 0. Input gaps (verified, not assumed)

- The 9 cited PROOF-NOTEs
  (`hidden_files/w47/scratch-proof-en-{fr,ko,ja,es,it,ru,nl,pt,zh-tw}1/PROOF-NOTE.md`)
  **do not exist in this clone** — the "9/9 confirmed" claim could not be
  verified from files. Only 7 unrelated PROOF-NOTEs exist (de-fr, ja-de,
  ja-en, ja-es, ja-fr, ja-it, ja-pt), none about core-en. Every defect below
  was verified independently: source inspection + rendered-ink measurement
  (cairosvg PNGs at 1950 px) + online fact checks.
- `hidden_files/w47/scratch-en/` and `scratch-en-fix2/` (incl. the cited
  `make_textmd_w47.py` exporter) also do not exist in this clone. The
  text.md exporter was re-derived from scratch (`make_textmd_fix1.py`,
  same recording contract); its output diffed against the pre-fix text.md
  shows ONLY the intended changes (see §3).
- `production/covers/2026-w47/cover.json` does not exist in this clone
  either (covers/ holds only w43/w45/w46). The cover flag in §6 is therefore
  a handoff to the coordinator, not a verified finding.

## 1. Baselines (pre-fix, disk-measured; KIT §7 cross-checked)

| artifact | sha256 | bytes |
|---|---|---|
| print PDF `The-Lucerna-VOL4-en-zh-cn.pdf` | `ca1ab6c02906a39f00442154b25ac18678753cb2da2624bc9be559a4c20233e1` | 41,407,278 |
| web PDF `The-Lucerna-VOL4-en-zh-cn.web.pdf` | `2ee5391f00d1b5324c193548508c614b2c5a3f51da958257e2cd4cabfc483337` | 2,765,419 |
| `2026-w47-en-zh-cn.text.md` | `4f0c74311ed7e5ad0ce1962a2204b0713002126909f4c3a4df6b7baff0081308` | 50,768 |

core-en was (and is) untracked in git (`?? production/2026-w47/core-en/`).

## 2. The 9 items — what was changed

### Item 1 — Q39/Q40 keys swapped (severe)
- `content34.py` match_set keys `["b","d","a","c"]` → `["b","a","d","c"]`;
  notes: mentor→a, arena→d. Registry n=39→`a`, n=40→`d`.
- Hand-verified against the stems: a tribute = "a person chosen to take
  part in the Games" (b); a mentor = "a person who teaches and guides
  you" (a); the arena = "the place where the Games are fought" (d);
  a campmate = "a person who lives with you in the jungle camp" (c).
- Registry re-dumped (`dump_reg_fix1.py`); diff vs pre-fix registry:
  exactly 10 entries changed (n=7, 39, 40, 46, 52, 55, 82, 83, 84, 125).
- **Registry derivation (conclusion): hand-maintained, NOT
  transform-derived.** Each en-* edition dir is a full copy of the core
  build with its own `content*.py` + `dump_reg.py` + `registry.json`; keys
  are hard-coded per edition (e.g. `en-fr/content34.py:61` carries the
  same wrong `["b","d","a","c"]`). No `apply.py`/`map*.json` exists for
  en fan-outs. All 10 en-* fan-outs (de, es, fr, it, ja, ko, nl, pt, ru,
  zh-tw) carry the same wrong keys (n=39 `'d'`, n=40 `'a'`). The core fix
  does NOT auto-propagate — each en-* fix1 must sync Q39/Q40 (and the
  Ashes rewrite, 已宣布 wording, etc.) in its own files + re-dump.
- en-ja KIT §3 records "added CJK = 2,096"; fresh `freeze.py diff`
  core-en→en-ja measured **2,092** (TOTAL added CJK characters). The
  2,096 lives in the en-ja KIT (out of scope to edit) — correction belongs
  to the en-ja fix pass. The number shifts again after this core fix
  (core CJK changed).

### Item 2 — P1 SEARCHES box overflow 18.0 px
- Baseline (rendered ink): box bottom 1256.0, last footnote baseline
  1274.0 → overflow 18.0 px baseline / 19.0 px ink.
- **Caught late:** the first rebuild did NOT change this box (the bar
  labels/footnotes are hand-placed, so `run.py` reports no overflow);
  the post-rebuild ink sweep found the overflow unchanged and it was
  fixed in a second pass: bar step 92→86 px in `content12.py` (the
  searches chart), footnotes now at baselines
  1184 / 1210 / 1244, last ink 1245, clearance **+11.0 px** inside the
  box. Sommaire box (y=1280) untouched.
- Rebuilt + re-rendered + re-gated after the fix (freeze 8/8 again,
  only p1 SVG changed).

### Item 3 — P2 DID YOU KNOW box overflow 12.7 px
- Baseline: box y=832.9 h=325.5 bottom 1158.4, last line "November 3."
  baseline 1171.1 → overflow 12.7 px baseline / 11.6 px ink.
- Fix: box height formula first-baseline offset 62→89 (the true offset
  is 16+52+21). Box now h=352.5, bottom 1185.4, last ink 1170,
  clearance **+15.4 px**.

### Item 4 — "confirmé" wording (call ≠ certified)
- `已确认` → `已宣布` everywhere in core-en: P1 strip
  ("中期选举 · 已宣布结果 · 详见第6版"), Q7 note, Q83 note, P6 bridge
  ("读上面的已宣布数图表…"), Q82/Q83/Q84 notes, registry notes
  (n=7, 82, 83, 84). French layer untouched (faithful translation).
- Deliberately unchanged: P6 "When the certified results are in, VOL.5
  will report them" (model wording); Q93 note; `certify` definitions;
  the certified-results certification-window facts.

### Item 5 — Ashes P4: whole page a year late (major rewrite)
Facts re-verified online 2026-11-11 (Wikipedia 2025–26 Ashes series,
ECB, Premier League, ATP/Tennis sources, NFL schedules) and by
`date -d` (America/Toronto): 2025–26 series 21 Nov 2025–8 Jan 2026,
**Australia won 4–1**. 1st Test Perth Fri–Sat 21–22 Nov 2025, Aus won
by 8 wickets in 2 days (shortest Ashes Test by balls bowled since
1888; Starc 7/58, Head 123 off 83, 69-ball century; Doggett &
Weatherald debuted). 2nd Brisbane 4–7 Dec, Aus by 8 wickets. 3rd
Adelaide 17–21 Dec, Aus by 82 runs, retained Ashes. 4th Melbourne
26–27 Dec, **England won by 4 wickets** (first England Test win in
Australia in ~15 years). 5th Sydney 4–8 Jan, Aus by 5 wickets.
Cummins out (back) Tests 1, 2, 4, 5, Smith captained; Cummins
captained the 3rd. Hazlewood out of 1st Test (hamstring, replaced by
Neser). Perth Stadium's first Ashes Test; city not in the 2021–22
schedule. **India beat Aus by 295 runs Nov 2024 at Perth Stadium —
true, kept.** Next Ashes: England, **18 June–2 Aug 2027** (1st Test
Trent Bridge, Fri 18 June 2027).
Changes:
- P4 rewritten as a retrospective: title "Perth, One Year On: How
  Australia Kept the Ashes" (wraps 2 lines like the old title);
  5 article paras; golden sentence "The Ashes are not a sport for
  early nights." kept verbatim.
- WHY PERTH box rewritten (keeps the India 295-runs Nov 2024 fact).
- Fixtures box title "SATURDAY, NOV 21　周六赛程", Ashes line dropped
  (3 lines remain).
- Q46 new stem/note (began Fri 21 Nov 2025 Perth, key A, distractor
  Sat 21 Nov 2026); Q52 key `hosts`→`hosted` ("Perth Stadium ___ its
  first Ashes Test in November 2025."); Q55 key `sold`→`won`
  ("Australia ___ the first Test by eight wickets."); ONE SCREEN
  "Perth is winning!"→"Arsenal are winning!".
- P1: headline para "…a look back at last year's Ashes…"; searches
  `"ashes"`→`"thanksgiving"`; IN BRIEF ASHES→"A year ago: Australia
  beat England 4–1 in the 2025–26 Ashes. (p. 4)".
- P2 feature para: "On Saturday, November 21, the Premier League is
  back — and page 4 looks back at the Ashes. Page 3 has the film
  guide, page 4 the sport."
- P5 para: "…and the football is back on Saturday".
- P7 Try-it (win/won): next Ashes June 2027 England; "Australia won
  the first Test."
- P8 Q125→"Australia won the 2025–26 Ashes by... A. 4–1 · B. 1–4 ·
  C. 2–2", key **A**.
- Unchanged: Q47/Q48/Q49/Q50/Q51/Q53/Q54; all matching sets C;
  P8 Q132 distractor "the Ashes"; P7 "whether … rain in Perth"
  (generic example); P1 sommaire "Perth, Turin & football".
- 150-question structure and 8 pages preserved (still 150; per-page
  10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).

### Item 6 — Box titles, rendered-ink sweep (whole issue)
- Baseline ink sweep (shipped SVGs): only 2 overflows — P2 SENATE
  −26.0 px (ink 556..987 vs boxR 961.0), P4 SATURDAY −2.0 px (ink
  1458..1864 vs boxR 1862.0). KIT §4 box-title table was not trusted
  (kind/weight/size unrecorded, not reproducible).
- Fixes: SENATE title → "SENATE IN NUMBERS　参议院数字" (ink now
  557..930, **+31.0 px**); SATURDAY title → "SATURDAY, NOV 21　周六赛程"
  (ink now 1458..1785, **+77.0 px**).
- **D7/D8 precision (en-zh-tw proof1 follow-up):** the old title's
  advance looked inside (+0.7 px) but its TRUE INK overran the box
  (tw proof: 1458..1865 vs 1862, −3.0 px; my baseline measured
  1458..1864, −2.0 px — same defect within measurement rounding; the
  box edge cut through the middle of "程"). The fix was sized by true
  ink, not advance. Note: the tw PROOF-NOTE itself does not exist in
  this clone (see §0); the defect was confirmed by my own baseline
  ink measurement.
- Sweep-tool fix found during verification: the title scanner
  concatenated same-baseline runs from a neighbouring column into the
  title (P4 "WHY PERTH" + col-2 "52.填空" → false −208.0 px
  "overflow"). `sweep_ink.py` now clips title runs to the box x-range;
  real WHY PERTH title ink is 556..872, **+89.0 px** inside.
- Post-fix sweep: **0 OVERFLOW** on all 8 pages. Tightest fitting
  titles: WEEK IN NUMBERS +5.5 px, HAYMITCH +21.0 px, ODD SOCKS
  +28.5 px. Tightest box bottom: P2 AND YOU? +2.9 px (passing,
  unchanged, recorded).

### Item 7 — P2 SAY IT box
- Baseline: only the middle label overflowed — "The new Congress meets
  in January." advance 352.1 (+36.0/side), ink 358 (+39.0/side) vs the
  280 px panel. Others fit ("The counting continues." −22.0/side;
  "Happy Thanksgiving!" −34.9/side). Vocab list fits (tightest "a
  turkey" −25.0 to RIGHT=1862); note para tightest line −1.0 px (fits).
- Fix: `phrase_panel` gained a `w` param; middle panel w=380 (spans
  560–940). Post-fix sweep (script geometry updated to the 380 px
  panel): label ink 574..931, **−11.0 px/side inside**. All other
  SAY IT lines unchanged and inside.

### Item 8 — P4 col-3 box title (307.0 vs 303.4 budget)
- Covered by the item-6 sweep: the SATURDAY fixtures title was the
  overflowing one; fixed as above (+77.0 px by true ink).

### Item 9 — P7 NEXT WEEK "the certified results" promise
- Certification window 10 Nov–18 Dec (Ballotpedia; Arkansas 18 Dec
  latest fixed date, Mississippi 31 Dec, 5 states no fixed date);
  VOL.5 (23–29 Nov) cannot have them all. P6's conditional wording
  ("When the certified results are in, VOL.5 will report them") is
  the model and was kept.
- P7 NEXT WEEK rewritten: "Thanksgiving in America. The Ashes:
  England's rematch waits until June 2027. More certified results of
  the midterm election. And your letters — the first real ones."
- **D9 second half (en-zh-tw proof1 follow-up):** the old line also
  said "The Ashes, second week in Perth" — wrong on its own terms
  (the issue's own schedule had the 1st Test 21–25 Nov; Perth has no
  "second week"; the 2nd Test was in Brisbane). The rewrite drops
  that phrase entirely.

### Attached checks
- ABSTRACT.txt rewritten (已核实→已宣布; Perth first-Test→"11 月 21 日
  周六英超回归与都灵 ATP 总决赛、一年前珀斯灰烬杯 4–1 回顾"). SOP §9:
  Lucerna ✓, A2–B2 ✓, 150 ✓, one line, no ASCII double quotes, reader
  language Chinese ✓.
- KIT updated: §1 P4 row, §3 Ashes bullet, §6 W46 Ashes teaser
  (overtaken), §7 build/repro (new SHAs/sizes, fix-1 notes), §8
  proofread record (fix-1 entry), §9 gates (new results).
- The en-zh-tw follow-up states en proof1 is now 9/9 with no new core
  defects; en-zh-tw has zero edition-unique defects — all 9 items are
  core-level; en-zh-tw rebuilds with the core + proof2 (coordinator's
  call, not this fix).

## 3. Rebuild + text.md re-export

- `run.py`: zero FLOW OVERFLOW / HEAD TOO WIDE (both runs). Flow ends:
  P1-headline 1751/1828, P1-countries 2298/2300, P1-quiz 2491/2560,
  P2-feature 1528/1540, P2-ex 2532/2560, P3-main 1984/2560, P3-col3
  1619, P4-main 2045/2560, P4-col3 1625, P5-main 597, P5-col3 1832,
  P6-main 2016, P6-col3 1196, P7-main 1613, P7-col3 2307, P8-battery
  1418/1555, P8-keys 2548/2560. TOTAL exercises 150, MODEL words 82.
- text.md re-exported by the re-derived stub exporter
  (`make_textmd_fix1.py`, 501 paras, 150 answers, 51,405 B). Diff vs
  pre-fix text.md shows **ONLY the intended changes** (strip, headline,
  searches, IN BRIEF, SENATE title, P2 para, P4 title + 5 paras +
  WHY PERTH + Q46/Q52/Q55 + fixtures title/Ashes line +
  "Arsenal are winning!", P5 para, P6 bridge, P7 Try-it + NEXT WEEK,
  P8 Q125, answers n=7/39/40/46/52/55/82/83/84/125). No unintended
  change anywhere.
- `render.py` (cards + print PDF) + `tools/webpdf.py` re-run after each
  source change (fix-1a and fix-1b after the SEARCHES step fix).

## 4. New SHAs (final, fix-1b)

| artifact | sha256 | bytes |
|---|---|---|
| print PDF | `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566` | 41,407,278 |
| web PDF | `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8` | 2,804,271 |
| text.md | `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b` | 51,405 |

SVGs (`freeze.py baseline`, 8/8 byte-identical reproduction):
p1 `a9a8deaf76e61cb2`, p2 `979747160de01d67`, p3 `efb83ce76688554b`
(unchanged from the pre-fix baseline), p4 `aa6f395e4932ef8b`,
p5 `a6a515cd5f734d0d`, p6 `7692256484f26289`, p7 `da908af644651793`,
p8 `2f9a0334d70e07ba`. (Fix-1a intermediate: p1 was `a84e80c342b6238f`;
only p1 changed in fix-1b.)

## 5. Gate results (all on the final artifacts)

| gate | result |
|---|---|
| `run.py` build | 0 FLOW OVERFLOW / HEAD TOO WIDE; 150 exercises; MODEL 82 words |
| `freeze.py baseline` | **8/8 SVGs byte-identical**, RC 0 (twice; core integrity re-hashed 8/8) |
| `occlusion_audit.py` (formal, no --selftest) | **0 flags**, RC 0 |
| `p8.py extract --total 150` | noted set = 60 of 150 (parse: joined) — same set as pre-fix baseline |
| keycheck (registry vs P8-extracted) | **149/150 exact**; n=150 the known full-text writing exception; 0 mismatches — PASS |
| rendered-ink sweep (all boxes + titles) | **0 OVERFLOW** (see §2 items 2/3/6/7 for clearances) |
| SAY IT sweep | middle label −11.0 px/side inside the 380 px panel; all other lines inside |
| print/web text layer per page | **8/8 pages byte-identical** (P1 4,868 B; P2 5,983 B; P3 5,352 B; P4 5,807 B; P5 4,709 B; P6 5,615 B; P7 6,073 B; P8 9,731 B) |
| 150 keys semantic check (stem-by-stem) | **150/150 PASS** incl. all 5 matching sets vs stems |
| 54 fill-in keys re-verified | 完成句子 34 + 完形填空 8 + 金句/比较/过去时×2/将来时/时态/从句 7 + 对话补全 5 = **54/54 PASS** |
| §1.1 grep audit | paper `#fbfaf6` 1/page, no `#f7f1e2`; no gold/red-brown/near-black colours in markup; fonts Newsreader / Noto Sans CJK SC / Noto Serif CJK SC / UnifrakturMaguntia (+ DejaVu Sans only for the 4 ☐ ballot checkboxes on P6 — pre-existing fallback, Newsreader has no ☐ glyph); badges A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f`, white text; VOL.4 in all 12 occurrences (VOL.3/VOL.5 only as deliberate historical/future references); `·` only as an in-body separator — no box title/head/band/masthead carries one |
| date/weekday `date -d` (America/Toronto) | all dates verified: Fri 21 Nov 2025 (1st Test), Tue 3 Nov 2026, Sun 8 Nov 2026, Mon 9 Nov 2026, Sun 15 Nov 2026, Mon 16 Nov 2026, Thu 19 Nov 2026, Fri 20 Nov 2026, Sat 21 Nov 2026, Sun 22 Nov 2026, Thu 26 Nov 2026, Fri 27 Nov 2026, Tue 1 Dec 2026, Fri 18 Dec 2026, Thu 8 Jan 2026, Fri 18 Jun 2027 |
| external facts | Ashes / PL Matchweek 11 / ATP Finals / NFL Week 11 re-verified online 2026-11-11 (see item 5) |
| ABSTRACT.txt SOP §9 | Lucerna ✓, A2–B2 ✓, 150 ✓, one line, no ASCII double quotes |

Pre-existing notes (not introduced by fix 1): P2 AND YOU? box bottom
+2.9 px (tight, passing); P1 masthead `#cac8ba` caption line ("Tuesday, November 3: America voted…", 1 text run,
pre-existing muted caption tone); P6 ☐ DejaVu fallback (above).

## 6. Flags for the coordinator (out of core-en scope, NOT done here)

1. **W47 cover.json does not exist yet in this clone.** When it is
   written, its `en` entry must NOT repeat the old framing ("Ashes
   begin Sat 21 Nov in Perth"). It must use the retrospective:
   lead "Perth, One Year On: How Australia Kept the Ashes" (Australia
   4–1, 2025–26), next series England June 2027. Same applies to any
   other cover/teaser text that mentions the Ashes date.
2. **en fan-outs need their own fix1** (see §2 item 1): all 10 en-*
   editions carry the same wrong Q39/Q40 keys and the same year-late
   Ashes page; the core fix does not propagate. Each must sync Q39/Q40,
   the Ashes rewrite, 已宣布 wording, and the box-title/SAY IT fixes
   in its own files + re-dump its registry. The en-ja KIT §3 freeze
   number 2,096 should be corrected to 2,092 in that pass (measured
   `freeze.py diff` core-en→en-ja; it will shift again after the core
   fix, so re-measure then).
3. No commit / no push made by this fix (per task). Repair re-check of
   the fixed core is separately assigned.
