# PROOF-NOTE — Lucerna Weekly 2026-W47 en-ru, proof1 (rebuilt edition, en re-fanout #2)

- **Edition:** English target, Russian reader (en-ru), VOL.4
- **Proofreader:** independent proof1 (SOP §8.4), not the builder/fan-out agent
- **Date:** 2026-11-11
- **Object (verified on disk before AND after the round; SHAs re-checked 2026-11-11 14:1x UTC):**
  - Print PDF `The-Lucerna-VOL4-en-ru.pdf` — 29,241,701 B — `daf81d35cdf44e66dffaed2f2ab68da66251742a1be02cb1af95f8daeed9cdaf`
  - Web PDF `The-Lucerna-VOL4-en-ru.web.pdf` — 2,452,739 B — `3fb58ae2e80f16460e7da5f5973cc5eb9ffc2687579b6fd88fb2d9eef41674fe`
  - Text `2026-w47-en-ru.text.md` — 62,395 B — `d59c98c0676f74352ce81557598641b91d4d17a4d033dbdd22e775199f0bbcf7`
  - All three match the brief exactly. Both PDFs 8 pages, 1462.5×2025 pt.
  - Core-en (control) SHAs measured before AND after this round, unchanged:
    print `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`
    (41,407,278 B), web `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`
    (2,804,271 B), text `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`
    (51,405 B) — identical to the FANOUT-REPORT values.
- **Scope:** full text.md read (~1,306 lines); 150 exercise keys verified stem-by-stem
  against stems (hand) + registry + P8-extracted keys (mechanical); all 8 print pages
  viewed; web P1 + P8 rendered and viewed; new/changed facts checked against live
  sources; all mechanical gates re-run independently (see GATE-LOG.md).
- **Prior round:** the pre-refanout proof1 (09:56 today, verdict (b), 5 defects) is
  archived untouched at `old-proof1-pre-refanout/` (its PROOF-NOTE.md, GATE-LOG.md,
  `gates/`, `render/`). This round re-proves the rebuilt edition from scratch.
- **No source files modified, no rebuild, no commit/push.** Web PDF never re-rendered
  into the production dir; re-renders ran only in scratch (`freeze-final/`).

## Verdict: (b) DEFECT LIST — not final

One defect. All five proof1 defects (D1–D5) are resolved (see "Carry-forward"
below); the one defect below is pre-existing in the old build and was missed by
proof1 — it is not a regression of the refanout. Per SOP §8.4 the edition is not
final until a full proof round finds zero issues.

---

## Defect 1 — P1 SEARCHES gloss overflows the cream-box right edge — LOW (cosmetic)

- **Location:** P1, SEARCHES OF THE WEEK col-3 cream box, last line (the Russian gloss
  under "Snapshots, early November: search interest changes during the day.").
- **Rendered text:** "Относительный интерес, не точные цифры." (41 chars, 19 px sans).
- **Source:** `content12.py:85`
  `p.text(gx + 22, byy + 76, "Относительный интерес, не точные цифры.", 19, "sans", False, GREY)`;
  map value `map-ru.json:228` (`"相对热度示意，非精确搜索量。"` → this Russian gloss).
  Box: cream rect x=1439.5, w=422.5 → right edge 1862.0 (SVG px).
- **Three independent measurements, all over:**
  1. **SVG advance** (`svglib.text_w`, same function the sweeps use): text starts
     x=1461.5, width 409.0 px → ends 1870.5 → **over +8.5 px**.
  2. **Print-PDF ink** (PyMuPDF spans): span x[1096.1, 1403.5] pt vs rect
     x[1079.6, 1396.5] pt → **right +7.0 pt (+9.3 SVG px)**; left margin +16.5 pt.
     This is the ONLY H-SPILL in the whole issue (h-containment scan, 8 pages).
  3. **Rendered pixels** (150 dpi print render, `render/print-p-1.png`): cream→white
     transition at 1396.5–1397 pt confirmed on the gloss baseline row; rightmost ink
     pixel 1401.6 pt → **ink over +5.1 pt (+6.8 SVG px)**. Zoom crop
     `render/p1-searches-gloss.png` shows the tail "цифры." sitting on white past the
     cream edge.
- **Attribution: en-ru-specific, PRE-EXISTING, missed by proof1.**
  - Core-en control: the Chinese gloss `相对热度示意，非精确搜索量。` same x/size,
    width 266.0 px → ends 1727.5, margin −134.5 px — fits. The spill is the Russian
    translation's width, not the core layout.
  - Pre-refanout backup (`scratch-fanout-en2/backup/2026-w47-en-ru/svg/p1-front.svg`):
    byte-identical line, same x=1461.5, same width 409.0, same over +8.5 px
    (only y differs: 1274 → 1244, from the core SEARCHES-box content shift). The
    refanout did not introduce it.
  - Proof1's h-containment listed only 5 H-SPILLs (P2 SAY IT ×3, P3, P4) and reported
    "no other overflow … on P1" — this line was missed there.
- **Impact:** cosmetic; the line stays within the column and page and remains legible,
  but its last ~2 characters sit on white past the cream edge — the same defect class
  old proof1 D5 flagged for the P3/P4 titles (P4 was +8.1 pt there; this is +5.1–7.0 pt).
- **Fix route:** shorten the Russian gloss literal (map-ru.json:228 → content12.py:85
  via the fanout map + rebuild, same mechanism as fanout-en2; rebuild + full re-gate,
  then a fresh proof round). Constraint: at 19 px the line must end ≤ 1862.0, i.e.
  width ≤ ~400 px with a small safety margin (current 409.0 px; cut ≥ ~10 px, e.g.
  drop one short word while keeping the "relative interest, not exact figures"
  meaning). The English line above it (line 84) is unchanged. A rebuild changes the
  print/web PDF and text.md SHAs; the new SHAs must be re-verified by the next proof.

---

## Carry-forward — all verified (en #2 build record)

- **ABSTRACT — full form ✓.** One line, 659 chars, Russian, no ASCII double quotes.
  Contains Lucerna, VOL.4, 150, A2–B2, plus announced results, certification
  10 Nov–18 Dec, 16 Nov Anti-Bullying/Odd Socks, 20 Nov Children's Day + Hunger
  Games, 21 Nov Premier League back + Turin ATP final + Ashes 4–1 look-back.
  The old short form is gone.
- **Q39→a / Q40→d — four-way consistent ✓.**
  SVG stems (P3, `svg/p3-culture.svg` + P3 render): 38. a tribute, 39. a mentor,
  40. the arena, 41. a campmate; definitions a="a person who teaches and guides you"
  (mentor), b="a person chosen to take part in the Games" (tribute),
  c="a person who lives with you in the jungle camp" (campmate),
  d="the place where the Games are fought" (arena).
  Registry keys: 38=b, 39=a, 40=d, 41=c. P8-extracted keys: same. text.md answers:
  39→a (`mentor = наставник a`), 40→d (`arena = арена d`). P8 render shows
  "38. b · 39. a · 40. d · 41. c". Notes `mentor = наставник a` / `arena = арена d`.
- **Ashes rewrite ✓.** P4 is the 2025–26 retrospective ("Perth, One Year On: How
  Australia Kept the Ashes"); no stale phrasing anywhere: 0 hits for
  "Ashes begin" / "Perth is winning" / "second week in Perth" / "never hosted" /
  "England's last tour skipped" in text.md, all 8 SVGs, registry.json and
  content*.py (the only hit for the phrase is KIT §5's own description of the fix).
  Q46 key A (Fri 21 Nov 2025, Perth), Q52 `hosted`, Q55 `won`, Q125 key A (4–1);
  text.md has "Arsenal are winning!" and no "Perth is winning!".
- **Old D1 (Q39/40) — resolved.** Old D2 (Ashes stale) — resolved.
  Old D3 (P2 DID YOU KNOW cut) — resolved: last line "November 3." baseline
  1171.1, baseline clearance +14.3 px, true-ink-bottom clearance +14.3 px (no
  descenders); P2 render shows it fully inside the cream with padding below.
  Old D4 (P2 SAY IT overflow) — resolved: `content12.py:229`
  `phrase_panel(299, …, w=420)` (panel 89–509; 51 px gap to the middle panel at
  560); RU line 1 "Подсчёт голосов всё ещё продолжается." 394.5 px fits; RU line 2
  360.6 px fits the core-widened w=380 middle panel; P2 SAY IT crop shows all three
  Russian subs inside their panels with margins, glossary gutter intact (panel 3
  still ends at 1340, glossary at lx=1370).
  Old D5 (P3/P4 titles) — resolved: P3 "HAYMITCH'S GAMES　Игры" 309.6 px (+94.9);
  P4 "SATURDAY, NOV 21　Суббота" 328.9 px (+75.6); all 18 SVG box titles fit.
- **"next Sunday" freeze rule — NO APPLICABLE OBJECT.** 0 hits for "next Sunday" in
  core-en content*.py, en-ru content*.py, `tools/tables.py`, and 0 hits
  (case-insensitive) in both text.md files. Nothing to freeze; not applied, not
  forced onto any line.

## Verified clean (summary — see GATE-LOG.md for per-gate evidence)

- **150 exercise keys: 150/150 correct** (hand-verified stem-by-stem against the
  text.md body; mechanical cross-check registry vs P8-extract 149/150 + the known
  n=150 short-label exception, registry vs core 145/150 differing only in the 5
  reader-language keys 137–140, 150). All matching blocks verified in definition
  order: Q24–27 (b/c/a/d), Q38–41 (b/a/d/c), Q56–59 (b/c/d/a), Q74–77 (d/a/b/c),
  Q141–144 (b/c/d/a). MCQ options, cloze, transforms, translations 137–140,
  dialogue 145–149 (row/film/popcorn/show/Friday), Q150 dash form all correct.
  Arithmetic re-checked: 254+162+19=435 ✓; 20+13+2=35 ✓; Q87 key C (435) ✓.
- **External facts — new/changed items checked live 2026-11-11 (Sky, Cricbuzz, ICC,
  Sportradar, Flashscore):** 2025–26 Ashes first Test Fri 21 Nov 2025 Perth,
  Australia won by 8 wickets in 2 days, 847 balls — "shortest Ashes Test, by balls
  bowled, since 1888" (only 788 Old Trafford 1888 and 792 Lord's 1888 shorter) ✓;
  series Nov 21, 2025–Jan 8, 2026, Australia won first three (Perth, Brisbane,
  Adelaide), England won 4th in Melbourne by 4 wickets (first England Test win in
  Australia since Sydney 2011, ~15 years), Australia won 5th in Sydney by 5
  wickets, final 4–1 ✓; "two Tests lasted only two [days]" — Perth and Melbourne ✓;
  India beat Australia by 295 runs at Perth, Nov 2024 ✓; next Ashes in England,
  June 2027 (P7 "in England, in June 2027"; core gives 18 Jun–2 Aug 2027) ✓.
  Unchanged facts (midterms 254/162/19, Senate 20–13 + Alaska/Mississippi, 7 flips,
  5 governors, 218–214/53–47 going-in, new Congress Jan 2027, Johnson will not run,
  House GOP Nov 10 / Dems Nov 18–19, Georgia runoff Dec 1 conditional, Anti-Bullying
  Week Nov 16–20 theme "Break the Silence", Odd Socks Day Mon Nov 16 10th year,
  I'm a Celebrity Mon Nov 16 9 p.m. ITV1/ITVX Murwillumbah, Hunger Games film
  Fri Nov 20 2026 + soundtrack Nov 13, ATP Finals Nov 15–22 Turin with the exact
  8-man field, Sinner out with knee injury, NFL Week 11, Premier League fixtures)
  are byte-identical to the text proof1 verified against live sources the same day
  (freeze diff shows only re-segmentation of identical English strings + Russian
  additions + Chinese removals — no new English content); weekday/date arithmetic
  re-verified (Nov 3 Tue, Nov 8 Sun, Nov 9 Mon, Nov 15 Sun, Nov 16 Mon, Nov 18 Wed,
  Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun, Nov 26 Thu Thanksgiving, Dec 1 Tue).
  Not separately re-verified (minor/hedged, no contradiction found): certification
  window Nov 10–Dec 18; "Patriots, after Munich"; W.G. Grace photo credit (Herbert
  Rose Barraud); Rousseau "Surprised!" 1891; Lawrence children photo Feb 19, 1912;
  Samuel Johnson portrait (Reynolds, 1772); LOC Reading Room photo (Highsmith).
- **Mechanical gates (all re-run independently — see GATE-LOG.md):** occlusion audit
  0 flags (selftest OK); p8 extract 60/150 both, compare CLEAN, keydiff
  [137, 138, 139, 140, 150] (expected); keycheck 149/150 + n=150 exception;
  freeze baseline 8/8 byte-identical re-render of the edition in scratch (hashes
  match the builder's exactly); freeze diff TOTAL added CJK 9, all U+3000;
  print/web text identity 47,655 chars each, token-multiset diff 0, per-page
  byte-identical 8/8; check_s11 ALL PASS; source boxtitle sweep 12/12 fit; SVG
  boxtitle sweep 18/18 fit; canonical creambox scan 0 OVERFLOW, all inside-only
  clearances positive (min baseline +5.0 px); true-ink bottom scan: every box's
  last line ink-bottom clearance ≥ 0 (see tight items below);
  h-containment: exactly 1 H-SPILL (Defect 1 above); V-SPILLs are only the known
  +6.0/+13.7 next-block headings below boxes (design spacing, same as proof1);
  P8 min font 10.12 pt ≥ 9.75 pt floor (PyMuPDF, independently measured; P1 min
  11.62 pt); quotes balanced (U+201C 81 / U+201D 81 in text.md; 82/82 across SVGs;
  U+2019 = 0; U+2018 = 0; ASCII apostrophe 40 in text.md); 0 Cyrillic-adjacent
  curly quotes in all 8 SVGs; banned-word scan 0 hits (SOP/proofread/cover/TODO/
  FIXME/XXX/lorem/占位/桥接); SVG zero real CJK (only U+3000); F-MAIL: no invented
  letters (P7 keeps the labelled editor's example + VOL.3 disclosure, as KIT §8).
- **Visual:** print P1–P8 all viewed; web P1 + P8 rendered and viewed, identical to
  print. No other overflow/overlap/truncation/footer-intrusion on any page. Footers
  "Страница N из 8" on all pages; masthead/edition line/badge correct.
  P7 toolbox contents fully inside cream (creambox P7 summary: 7 boxes, min inside
  clearance +47.7, min desc-clear +41.6).

## Tight-but-passing (genuinely tight, inside, recorded no-fix)

- **P5 ODD SOCKS, IN NUMBERS　Цифры** — advance margin +6.2 px, true-ink margin
  +6.5 px (source + SVG sweeps agree). Inside; tightest title in the issue.
- **P2 AND YOU? box, last line "по-английски для редакции."** — baseline clearance
  +5.0 px; PIL true-ink-bottom clearance +0.0 px; rendered-pixel measurement
  (150 dpi, text-ink only, olive divider excluded) +0.9 pt (+1.3 SVG px) — inside,
  not crossing. The olive full-width divider at pt 1168.5 is a design rule below the
  box (spans 66.2–1395.8 pt), not a spill. Same geometry as the de edition's
  identical box, adjudicated the same way (card crop verifies).
- **P1 SEARCHES gloss vertical** — ink-bottom clearance +7.0 px (only its horizontal
  spill is Defect 1); the English line above it is short.
- **P2 DID YOU KNOW?** — after the fix, last-line ink-bottom +14.3 px; not tight.

## Minor nits (not defects)

- KIT §3 "P8 min font 13.5 pt" conflates SVG px with pt (same wording nit as
  proof1): the real rendered size is 10.12 pt, still above the ≥9.75 pt floor.
  `check_s11.py` prints "P8 min font-size: 13.5" (SVG px). Wording only.
- P5 line "У каждого ребёнка есть права | Every child has rights = У каждого
  ребёнка есть права." — the Russian is repeated redundantly. Stylistic nit,
  core-rooted (same as proof1).
- Q108 correction drops "in 2026" from the error sentence — grammatical, not flagged
  (same as proof1).

## D5 font inventory (recorded only, not judged — per brief)

1,798 `<text>` elements across the 8 SVGs; 26 distinct `font-size` values (px):
13.5×75, 15.5×13, 16×1, 17×34, 18×15, 18.5×2, 19×162, 19.5×71, 20×53, 20.5×166,
21×21, 21.5×183, 22×167, 22.5×9, 23×147, 23.5×131, 24×465, 25×34, 26×2, 27×3,
28×11, 32×11, 36×5, 46×15, 53×1, 196×1 (masthead). No judgement made.

## Evidence paths (scratch dir)

`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-ru1/`
- `PROOF-NOTE.md` (this file), `GATE-LOG.md`
- `gates/` — occlusion.json/.log, p8-extract*.json/.log, p8-compare.json/.log,
  keycheck.py/.log, freeze.log, freeze-diff.json/.log, printweb-diff.log,
  check_s11.log, boxtitle.log, boxtitle-svg.log, creambox.log, ink-bottom.log,
  ink-bottom2.log, h-containment.py/.log, verify.log
- `render/` — print-p-*.png (8 pages, 150 dpi), web-p1-1.png, web-p8-8.png,
  p1-searches-gloss.png, p1-searches-box.png, p2-andyou-bottom.png, p2-sayit.png,
  p2-didyouknow.png, p2-senate-title.png, p3-haymitch-title.png,
  p4-saturday-title.png, p5-oddsocks-title.png
- `freeze-final/` — scratch re-render of the edition (8/8 byte-identical SVGs)
- `old-proof1-pre-refanout/` — the pre-refanout proof1 round, archived untouched
- `.probe`, `creambox.py` (early copy; the canonical scan used
  `hidden_files/w47/tools/creambox.py`)
