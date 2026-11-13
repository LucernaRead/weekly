# PROOF NOTE — Lucerna Weekly 2026-W47 · en-it · proof1 (round 2, re-fanout #2 rebuild)

**Edition:** English target × Italian readers (`2026-w47-en-it`), VOL.4, issue week 2026-11-16..22
**Proofreader:** independent proof1 (SOP §8.4), not the builder / not the fan-out agent
**Date:** 2026-11-11
**Conclusion: (a) 定稿零缺陷 — zero defects. Ready to ship.**
**Round-1 record preserved:** this round's predecessor (proof1 round 1, 2026-11-11 09:56, conclusion (b) D1+D2) is archived untouched in `round1/` (PROOF-NOTE.md, GATE-LOG.md, gates/, render/, creambox.py, probe.txt). This note covers ONLY the re-fanout #2 rebuild.

## Objects verified (SHA-256)

| File | Size | SHA-256 | Check |
|---|---|---|---|
| `The-Lucerna-VOL4-en-it.pdf` (print) | 29,327,190 B | `bdfe23784024bb85635eb2984dd3c530c2db63aff1b7c102bc08b78b40d7b61c` | MATCH task + KIT §2 |
| `The-Lucerna-VOL4-en-it.web.pdf` (web) | 2,408,886 B | `d5e9c1af0880237350b4364d8a4be478673d87d249cd614f334849c969618e58` | MATCH task + KIT §2 |
| `2026-w47-en-it.text.md` | 53,947 B | `433c2aec5b303a5968e535c83b38e6b30128c1b5a2318fb0fa44466f00dbb15e` | MATCH task + KIT §2 |

Both PDFs 8 pages, 1462.5 × 2025 pts (pdfinfo). Probes passed before work (`ls /dev/null` present; `echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`; write probe in goals-side scratch OK; TMPDIR pointed at scratch `tmp/`, `/tmp` avoided throughout).

**Core-en unchanged by this round (measured before AND after):** print `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`, web `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`, text.md `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b` — identical at both ends. No production file was written: all re-renders ran in the scratch copy `proof-copy/`; `git status` shows the edition dir only as untracked (`??`), same as before this round.

## What was checked

- **Reproducibility (scratch copy only):** `run.py` RC=0, 0 OVERFLOW / TOO WIDE, TOTAL 150, MODEL 82; `render.py` RC=0. Re-rendered print PDF is **byte-identical** to production (`bdfe2378…`, 29,327,190 B) and all 8 SVGs MATCH production byte-for-byte.
- **Registry:** `dump_reg.py` re-dump identical to production `registry.json` (150 entries; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22 — matches KIT §1).
- **Occlusion audit:** 0 flags (selftest OK, all 6 planted classes fired, clean controls silent).
- **p8 extract + compare:** 60/150 noted, same set as core; **CLEAN**, missing=[] extra=0, keydiff=[137, 138, 139, 140, 150] (reader-language translation keys + open writing key — expected).
- **Keycheck (canonical + independent re-run on my own re-dump/extract):** registry-vs-p8extract **149/150 exact + n=150 short-label exception**, mismatch=[]; registry-keys-vs-core 145/150 (diff only the 5 expected reader-language keys 137–140, 150); Q38–41 = [b, a, d, c]; Q125=A, Q46=A, Q52=hosted, Q55=won; Q82/83/84 = B/C/A; noted set == core; extract keys 150, none missing.
- **Freeze:** baseline 8/8 byte-identical (core re-rendered from source matches shipped core SVGs; core integrity re-hash OK); diff TOTAL added CJK = **9, all U+3000 separators**.
- **Print/web text layers:** 47,991 chars each, token-multiset diff **0**, per-page byte-identical **8/8**. Scratch-only webpdf re-render (2,408,870 B, SHA `610b2c42…`, differs from production web SHA as the iron rule predicts — wall-clock `head.modified`) has a **byte-identical text layer** to the production web PDF. Production web PDF never overwritten.
- **text.md:** re-export from proof-copy source + re-dumped registry is **byte-identical** to production text.md (SHA `433c2aec…`, 53,947 B, 498 recorded blocks, stub registry 150 = real registry 150).
- **check_s11:** ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19; badges A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min SVG font 13.5pt; Q113–120 [A2] tag line; "Levels: 145–149 [A2]"; Q120 [A2] chip; WRITING head "H　WRITING　Scrittura [B1]").
- **Boxtitle sweeps:** source 12/12 fit (tightest HOW LONG? 384.3px, margin +20.2); rendered SVG 18/18 fit, 0 overflows.
- **Creambox (canonical `hidden_files/w47/tools/creambox.py`, all 8 SVGs):** 32 boxes; min inside-only clearance **+5.0px**, no inside-only negative. The 21 raw negative "clearance" lines are all below-window titles of the following box (known false-positive class, e.g. 'TRY IT NOW' at −37.0 under the numbers box) — each adjudicated in GATE-LOG §9. The single desc-clear flag (−1.0px, P2 AND YOU? box) is a heuristic false alarm: last line "redazione." contains no descender letter (g/j/p/q/y); baseline clearance is +5.0px inside the cream, confirmed on the rendered crop (`render2/p2-andyou.png`).
- **verify_ed.py:** ALL PASS (23/23).
- **150 questions, three-source hand verification:** full read of `2026-w47-en-it.text.md` (1,306 lines) + registry + P8 extract + SVG definitions. Every answer checked against its stem; all 5 matching sets verified against their printed definitions in source AND SVG (see §"Matching sets" below). **150/150 correct.**
- **8 pages rendered and read visually** from the production print PDF (`render2/p-1.png`…`p-8.png`) + web P1/P8 (`render2/w1-1.png`, `w8-8.png`) + P2 SAY IT / AND YOU? crops. No overlap, no spill, no missing content.
- **Old-vs-new diff** (vs `scratch-fanout-en2/backup/2026-w47-en-it/`): registry differs in exactly 8 entries (Q39, Q40, Q46 note, Q52, Q55, Q82 note, Q84 note, Q125); text.md 66 changed lines, all in the expected fix areas; SVGs changed on 7 pages with a reason each, p3-culture unchanged (Q39/40 key change lives in registry + P8 answers, definitions unchanged). ABSTRACT old short-form → new full-form. No unexpected change anywhere.
- **Weekday spot-check** (`date -d`, America/Toronto): Fri 2025-11-21, Tue 2026-11-03, Sun 2026-11-08, Mon 2026-11-09, Tue 2026-11-10, Mon 2026-11-16, Wed 2026-11-18, Thu 2026-11-19, Fri 2026-11-20, Sat 2026-11-21, Sun 2026-11-22, Thu 2026-11-26, Fri 2026-11-27, Tue 2026-12-01 — all match the text.
- **"next Sunday" freeze rule:** grep over core-en + en-it + `tools/tables.py` returns **0 hits** — the rule has no applicable object in this edition; nothing was hard-applied from old line numbers.
- **Orphan punctuation sweep:** 0 orphan-led lines, 0 lone-opener line-ends in text.md; quotes balanced (“ 81/” 81, « 4/» 4, ASCII " 0).
- **U+2019 sweep:** 0 hits in text.md, all 8 SVGs, content*.py, registry.json. All 61 apostrophes in text.md are ASCII straight (I'm, Australia's, L'Australia, HAYMITCH'S, …) — consistent with build_map's U+2019→ASCII normalisation.
- **D5 fonts (recorded only, not judged):** print PDF 41 font objects, 7 families — DejaVuSans ×1, Newsreader16pt-Italic ×1, Newsreader16pt-Regular ×16, NotoSansCJKsc-Bold ×8, NotoSansCJKsc-Regular ×8, NotoSerifCJKsc-Regular ×6, UnifrakturMaguntia ×1. Web PDF 41 objects, 8 Lucerna-renamed families. P8 min PDF font **10.12pt ≥ 9.75pt** floor.
- **Internal-label sweep of text.md:** only hits are the W46 header boilerplate (line 5 "exported from the build source files (content12.py…)" and line 1003 "from the exercise registry") — byte-identical in core-en's text.md, a core-inherited convention, not an edition defect.

## Carry-forward items (round-1 D1/D2 + fanout #2 build record) — all verified closed

1. **it SAY IT box3 layout collision (fanout #2 defect 5) — CLOSED, re-measured from source + SVG.**
   - Source `content12.py:224-232`: `phrase_panel(1200, "Happy Thanksgiving!", "Buon Ringraziamento!")` with default `w=280` → rect x=1060..1340; glossary `lx = 1370`. **Gutter = 30px** (was 0px with the reverted w=340 panel).
   - Measured (`svglib.text_w`): "Buon Ringraziamento!" advance **208.2px**, span 1095.9..1304.1, margins **35.9px/side** — matches the KIT claim exactly. EN label "Happy Thanksgiving!" 210.2px, margins 34.9px/side.
   - SVG ground truth (`p2-life.svg`): panels at 159–439, 560–940, 1060–1340; glossary words start x=1370.0; sub starts x=1095.9. Rendered crop `render2/p2-sayit.png` shows all three subs inside their cream with clear margins and a clear gap to the glossary column.
   - Round-1 D2 also covered box2 (w=380): EN "The new Congress meets in January." 352.1px (margins 14.0), IT "Il nuovo Congresso si riunirà a gennaio." 363.6px (margins 8.2) — both inside panel 560–940. Old spills (36.0px/side EN, 41.8/42.2px IT in the 280 panel) are gone. SVG confirms: box2 sub starts x=568.2, ends 931.8.
2. **ABSTRACT full form — VERIFIED.** 737 bytes, one line, no ASCII double quotes. Contains "The Lucerna", "VOL.4", "150 esercizi", "livelli A2–B2", plus the announced results (254–162, certification 10 Nov–18 Dec), 16 Nov Anti-Bullying/Odd Socks, 20 Nov Children's Day + Hunger Games, 21 Nov Premier League + Turin ATP final, Ashes 4–1 look-back. Old short-form ("Il settimanale in inglese per chi legge in italiano: …") is gone.
3. **Q40 arena note error class — VERIFIED FIXED.** Registry Q40 note = `arena = l'arena d` (old: `arena = lo stadio a` — stadium, wrong). `estadio`/`stadio` 0 hits in the note (verify_ed PASS). Same fix confirmed in text.md answer 40 and P8 extract key d.
4. **Q39→a / Q40→d Ashes wording — FOUR-WAY CONSISTENT.** Registry (39=a, 40=d), text.md answers (39→a, 40→d), P8 extract keys (39=a, 40=d, part of the 149/150 exact), SVG definitions (`p3-culture.svg`: a = "a person who teaches and guides you", b = "a person chosen to take part in the Games", c = "a person who lives with you in the jungle camp", d = "the place where the Games are fought") — mentor→a, arena→d. Q46=A (Fri 21 Nov 2025 Perth), Q52=hosted, Q55=won, Q125=A (4–1) in all sources; "Arsenal are winning!" present; "Perth is winning!", "second week in Perth", "Ashes begin" 0 hits.
5. **Round-1 D1 (core-rooted Q39/Q40 swap) — resolved by the core fix1 + rebuild, not by an edition hack:** the new keys come from the fixed core via apply.py + patched `map-it.json`; the old backup's keys (39=d, 40=a) are gone.

## Matching sets (all 5 verified against printed definitions)

| Set | Lefts → keys (registry) | Rights a–d (source order = SVG letter order) | Verdict |
|---|---|---|---|
| P2 Q24–27 | runoff→b, certify→c, turkey→a, Thanksgiving→d | a=bird of the Thanksgiving dinner, b=second vote, c=confirm a count officially, d=American family holiday | ✓ (SVG rights confirm a=bird, b=second vote, c=confirm, d=holiday) |
| P3 Q38–41 | tribute→b, mentor→a, arena→d, campmate→c | a=teaches and guides you, b=chosen to take part in the Games, c=lives with you in the jungle camp, d=place where the Games are fought | ✓ |
| P4 Q56–59 | Test→b, tour→c, injury→d, break→a | a=pause between parts of a season, b=five-day cricket match, c=series of games away from home, d=damage to the body that stops you playing | ✓ |
| P5 Q74–77 | bullying→d, speak up→a, right→b, silence→c | a=saying what you think loudly and clearly, b=something every child has by law, c=saying nothing at all, d=hurting or frightening someone again and again | ✓ |
| P8 Q141–144 | call→b, runoff→c, certify→d, midterm→a | a=election in the middle of a President's term, b=news organisation's judgement on a race, c=second vote when nobody wins, d=confirm a count officially | ✓ |

## Tight-but-passing (genuinely tight, inside, recorded no-fix)

- **HOW LONG? box title:** source 384.3px, margin **+20.2px** (tightest of the 12); SVG advance margin +20.2 — inside, visually confirmed on P6.
- **P2 AND YOU? box:** last baseline clearance **+5.0px**; desc-clear heuristic −1.0px is a false alarm (last line "redazione." has no descender; see §9 of GATE-LOG). Same class as the de edition's recorded false alarm in the fanout report.
- **Q2 note vs P6 gloss:** "call a race = proclamare il risultato" (registry note, TM) vs "annunciare il risultato" (P6 gloss) — two source literals, both correct (KIT §6).
- **Q54 note** "eight (otto = eight)" — tautological, same pattern as the core's note style; not a defect.
- **Q34 note** "(open = uscire (terza persona singolare con -s))" — correct in context (film opening = uscire).

## Defects

**None. Zero defects found in this round.**

No commit, no push made. All work in `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-it1/` (gates in `gates2/`, renders in `render2/`, scratch re-render copy in `proof-copy/`).
