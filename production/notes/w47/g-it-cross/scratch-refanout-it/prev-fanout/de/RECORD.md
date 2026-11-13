# it-de — edition record (build5, 2026-11-11)

## Deliverables
- `production/2026-w47/2026-w47-it-de/La-Lucerna-VOL4-DE.pdf` — 14,037,296 bytes, sha256 `6903d98b3adb07c1fea0ff1e9b844cc8d8950fc8cfd34adb82394582bbf304cf`
- `La-Lucerna-VOL4-DE-web.pdf` — 1,265,110 bytes, sha256 `a62a094705fabd79cd70efec5083835e5cc2ff2d943f36c19d851f0f36cee6e1`
- `2026-w47-it-de.text.md` — 56,734 bytes, 1317 lines, 150 exercises
- `ABSTRACT.txt`, `WEEKLY-KIT.md` (both in the edition dir)
- 8 SVG + 8 cards in `svg/` / `cards/`

## Builds
- build1 (prev. runner, ~269 s): run.py rc 0, 150 ex., but 3 FLOW OVERFLOWs — P1-headline ended 1916 (bottom 1828); P8-keys over 28px (last two answers merged on one baseline, breaking p8 extract); P7 col3 ended 1848.5 (FRASI hline at 1686). Gates failed on occlusion (1 TEXTX on P8), p8 extract/compare PARSE_FAIL.
- build2 (this runner): 13 strings shortened, measured with the build's own `wrap()` first, applied identically to translations.py + the edition sources — P1 cifre items to 2 lines each; P7 error notes to 1 line each; disclosure 6 → 3 lines; six P8 answer notes shortened to convert 2-line answers to 1 line (22/128, 58, 87, 138, 139). Result: zero overflow, P7 col3 ends 1673.0, p8 extract 150/150, compare CLEAN. Gates left 1 flag: [TEXTX] P8 match_set instr "Ordne die Wörter den Bedeutungen zu" (347.1px at 19.5px sans, start-anchored at x+196) crossed into the next column, grazing the model text by 92.8×4.2px.
- build3: instr shortened to "Wörter zuordnen" (153.0px) in translations.py + content8.py only. Gates failed: the same instr is used by three match_set calls (P2 content12.py, P4 content34.py, P8 content8.py) — the P4 occurrence overlapped a B2 chip 24.3×14.0px, and freeze flagged the old string unexplained on P2/P4.
- build4: remaining two occurrences fixed in content12.py + content34.py. Gates left 1 flag: [COVER] P4 E TU text 52% covered by the results-table row rect — the German E TU question wrapped to 3 lines, its third line inside the fixed table (title y=1140, first row rect 1156–1218); box bottom 1169 vs core/en 1140.
- build5 (this runner): P4 E TU question shortened to 2 lines — "Welches Spiel siehst du Sonntagabend? Schreib zwei Sätze auf Italienisch." ("send them to us" clause dropped, as in the shipped en edition). Result: P4 col3 ends 1140.45 (= core), occlusion 0, gates ALL PASS (gates5.log).

## Gates (gates5.log, ALL PASS)
occlusion 0; p8 extract 150/150, compare CLEAN (keydiff 137–139 only); freeze fragments 0 unexplained; freeze baseline sha256 8/8; strict-cjk 13 × U+3000 only; print/web multiset identical 7,798 words; web 1,265,110 < 7MB; P8 min 13.0px = 9.75pt; §1.1 scans pass; VOL.5 = 3 legitimate nodes; textmd 0/0; keys match (except 137–139 + writing); notes match translations.py (9 frozen notes exempted).

## Self-checks
- P8 chips: Q113–120, Q145–149, Q150 all B1, = core 1:1.
- Visual 8/8 cards: zero defects (P4 E TU box flush with the table header; P7 disclosure 3 lines, clear of the FRASI rule; P8 match instr short, no graze on the model text; P3/P5 structural whitespace is the core pattern).
- Full self-read of .text.md (1317 lines): only CJK is the deliberate 「翻译」 type label (Q137–140) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); German explanation layer throughout; all 150 keys re-verified (spot checks: Q51 B, Q58 più bella, Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q92 +0.8%, Q120 B 24 Nov, Q137–140 re-aimed).
- ABSTRACT: DE one line, no ASCII double quotes.

## Lessons carried forward (de/fr/nl length risk)
- Any reader-language string drawn start-anchored across a column boundary must be measured with the build's own `text_w`/`wrap`: match_set `instr` at x+196 has only 254.5px before the next column (de "Ordne die Wörter den Bedeutungen zu" = 347.1px); the P4 E TU box has a fixed table at y=1140 (2-line budget for the question); the P8 RISPOSTE flow has only ~61px of spare capacity over 4 columns (each 2-line answer costs 14.82px extra).
- The three match_set instructions (P2/P4/P8) share one translations.py entry — fix all three call sites, not one.
- P8 answer-note shortenings must keep the gloss link where possible; where a note had to become terse (138 "wird gespielt", 139 "zu Hause"), the full gloss stays in the P8 exercise stem and in the .text.md exercise entry.

## Tool fixes made this shift
None (gates.py was fixed in the en shift; shared tools untouched).
