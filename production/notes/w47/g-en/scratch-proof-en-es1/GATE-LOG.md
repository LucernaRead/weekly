# GATE-LOG — Lucerna Weekly 2026-W47 en-es · proof1 (re-fanout #2 rebuild)

All measurements on disk in this scratch dir unless noted. Tools run with `~/workspace/weekly-git/tools/venv/bin/python` (Pillow 13.0.0 / FreeType 2.14.3). Probe first: `git -C ~/workspace/weekly-git hash-object -w --stdin` OK (`bf0a0bbf…`) + probe file `probe2.txt`. TMPDIR = this scratch dir's `tmp/`; `/tmp` never written; `/dev/null` present throughout. Production files read-only; every rebuild ran in a scratch copy.

## Identity / SHA (PASS)
- Print `The-Lucerna-VOL4-en-es.pdf`: 29,331,231 B, sha256 `6341e239942338c547cfff31d96b4d6b0ad5b4ad811164380995959ea210b4a5`
- Web `The-Lucerna-VOL4-en-es.web.pdf`: 2,414,448 B, sha256 `73356781d8c02970f18e592ef60189891db128eb38cabb04442e1919ee725b97`
- `2026-w47-en-es.text.md`: 54,388 B, sha256 `2539179917d985e6da78c36be288946865af6b8aa8599c3e532e44e262921e2d`
- `registry.json`: 22,306 B, sha256 `58a61af5a5bde13b5c54e825efa2d877937313b91bef4a98165a27383d216e1b`
- Both PDFs 8 pages, 1462.5×2025 pts. Re-hashed identical at end of round (see `gates-run1.log` head and final check).

## run.py (copy rebuild — `run.log`, `runcopy/`)
- `cp -r` edition to `runcopy/`, removed PDFs, ran venv `run.py`: **RC=0**, OVERFLOW 0, TOO WIDE 0, MODEL words: 82, `P8 saved, TOTAL exercises: 150`, ALL DONE. All flows within bottom (P1-headline 1806/1828, P1-countries 2298/2300, P1-quiz 2491/2560, P2 1497/1540 & 2532/2560, P3 2014/2560 & 1619/2560, P4 2235/2560 & 1655/2560, P5 657/2560 & 1832/2560, P6 2045/2560 & 1226/2560, P7 1786/2560 & 2419/2560, P8-battery 1418/1555, P8-keys 2443/2560).

## freeze.py baseline (`freeze.log`, `freeze-final/`)
- `freeze.py baseline --build <edition> --core-svg <edition>/svg --out freeze-final`: **RC=0, 8/8 SVGs byte-identical** (reproduced in copy vs shipped). Core integrity: shipped SVGs unchanged by the run (8 files re-hashed).

## freeze.py diff vs core-en (`freeze-diff.log`, `freeze-diff.json`, `freeze-diff-strings.txt`)
- **RC=0.** p1 +34/−33, p2 +43/−54, p3 +26/−23, p4 +26/−22, p5 +25/−22, p6 +25/−21, p7 +64/−55, p8 +104/−98 strings; **TOTAL added CJK 9, all U+3000** (p1: 2, p2–p8: 1 each).
- Added/removed strings reviewed line by line (613-line dump): all are furniture (masthead strips, section heads + Spanish glosses, footers "Página N de 8", page separators "— Página N —"), instruction words (Completa/Empareja/Reescribe/Corrige), glosses/notes, or re-chunked P8 key lines with identical keys. **No English article text changed.** Core P8 removed strings contain the same fixed key line `38. b · 39. a · 40. d · 41. c`.

## occlusion audit (`occlusion.log`, `occlusion.json`, `occlusion-selftest.log`)
- Selftest RC=0: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent.
- Edition `--core <core-en>/svg`: **0 flags; core 0 flags; NEW vs core 0. RC=0.**

## p8.py (`p8-extract-core.json/log`, `p8-extract.json/log`, `p8-compare.json/log`)
- Extract core: noted set = 60 of 150. Extract edition: noted set = 60 of 150 — **identical set** [3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108–150].
- Compare: **status CLEAN**, missing=[], extra_count=0, uncertain=[], keydiff=[137, 138, 139, 140, 150] (expected: Spanish translation keys 137–140 + open writing task 150). RC=0.

## keycheck (`keycheck.log`, `keycheck.py`)
- p8 extract vs shipped registry: **150/150 keys present**; missing none; only mismatch Q150 truncated to "Pregunta abierta" (known extractor short-label pattern, same as core).
- text.md answers vs registry: **150 answer lines, numbers 1–150 continuous; 0 mismatches** (key + level).

## check_s11 (`check_s11.log`)
- RC=0. Badge colours B1 #46581f / B2 #37402f present; P8 min font-size 13.5; P8 Q113-120 options line with [A2] tag present; 'Levels: 145-149 [A2]' present; Q120 [A2] chip OK; P8 WRITING head present; **ALL §1.1/P8 CHECKS PASS**.

## boxtitle sweeps (`boxtitle.log`, `boxtitle-svg.log`)
- Source titles (12): **over budget 0**. Tightest: THE WEEK IN NUMBERS +20.4, ODD SOCKS +27.7, HAYMITCH'S GAMES +33.5, SENATE IN NUMBERS +33.6, COMING SOON +49.0, WHY PERTH? +57.8, A PRACTICE BALLOT +58.3, THE TOOLBOX +65.8.
- Rendered SVG titles (18): **overflows 0**. P1 +20.4/+259.7/+36.4/+173.0; P2 SENATE +33.6, CALENDAR +85.4, DID YOU KNOW? +210.3, AND YOU? +192.0; P3 +49.0/+33.5; P4 +57.8, SATURDAY, NOV 21 +86.7; P5 +27.7/+152.2; P6 A PRACTICE BALLOT +58.3, **HOW LONG? Duración +142.3**; P7 +65.8; P8 MODEL +663.0.

## creambox canonical scan (`creambox-check.log`)
- `creambox_check.py` on all 8 shipped SVGs: **RC=0, NO OVERFLOW**. 32 cream boxes, inside clearance +5.0 to +92.4 px. Per page: P1 +45.7/+12.0/+48.0/+44.0; P2 +48.1/+48.1/+47.7/+14.3/+5.0/+30.0/+30.0/+72.0; P3 +48.1/+47.7/+48.5; P4 +48.1/+47.7/+48.5; P5 +48.1/+47.7/+48.5; P6 +48.1/+47.7/+48.5; P7 7 boxes +47.7/+48.5 (toolbox box y=651, bottom 1008.2, clearance +48.5); P8 +92.4.

## SAY IT phrase boxes (`sayit-check.log`, `crop-sayit-feliz.png`)
- Edition `svglib.text_w` (sans/serif, 20 pt), box by box: box1 (159–439): 'The counting continues.' ends 404.6 (+34.4), 'El recuento sigue en curso.' ends 423.2 (+15.8); box2 (560–940): 'The new Congress meets in January.' ends 908.7 (+31.3), 'El nuevo Congreso se reunirá en enero.' ends 930.5 (+9.5); box3 (1060–1340): 'Happy Thanksgiving!' ends 1294.1 (+45.9), '¡Feliz Día de Acción de Gracias!' advance 285.8, x=1057.1 → ends 1342.9 (advance ±2.9 px over each edge).
- Pixel check on the print card (band y=1710–1745): **ink x-range 1060–1338, inside box edges 1060/1340** — the advance overhang is glyph side-bearing only; no ink leaves the cream. Crop `crop-sayit-feliz.png` visually confirms. Not a defect (see PROOF-NOTE O4).

## verify_ed (`verify.log`)
- **RC=0, VERIFY ALL PASS.** PASS Q39 key a; Q40 key d; Q39 note mentor=a; Q40 note arena=d; Q40 note not estadio/stadio; Q46 key A; Q46 note 2025; Q52 key hosted; Q55 key won; Q125 key A; Q125 note 4-1; registry notes: no stale Ashes phrasing; text.md has 150 answers; text.md Q39 a / Q40 d / Q125 A; text.md: "Arsenal are winning"; no 'Perth is winning' / 'second week in Perth' / 'Ashes begin'; Ashes retrospective present; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK.

## Print vs web text layers (`printweb.log`)
- pdftotext token-multiset: print 48,258 chars / 2,507 distinct tokens; web 48,258 chars / 2,507 distinct; **diff total 0**; only-in-print [] / only-in-web []. Per-page byte-identical 8/8 (p1 4956B, p2 5890B, p3 5309B, p4 5786B, p5 4694B, p6 5653B, p7 6051B, p8 9919B).
- Web PDF P8 text layer contains `38. b · 39. a · 40. d · 41. c`.

## Orphan punctuation (`orphan.log`)
- All SVG `<text>` elements + all text.md lines scanned. Single-char orphan lines: 。0, ”0, ：0, –0, —0, .0, ,0, ’0, »0, «0. Lines starting with a closing orphan or ending with an opening orphan: none.

## Text proofread (150 answers; 150/150 semantically correct)
- Full text.md read (P1–P8 + all answer lines). Registry: numbers 1–150 continuous; per-page 10/17/18/18/18/18/12/39; levels A2 62 / B1 66 / B2 22 — all match KIT.
- Answer lines 150/150 match registry exactly (key + level, 0 mismatches).
- Semantic check of every key against its stem: **150/150 correct**. Matching sets verified against printed SVG letter order: P2 D 24–27, P3 C 38–41 (39→a mentor, 40→d arena), P4 C 56–59, P5 C 74–77, P8 F 141–144. Chart arithmetic 254+162+19=435 (Q87→C); 254−218=36. Cloze 112–119, dialogue 145–149, translations 137–140 all verified.
- Cross-references: IN THIS ISSUE p.2–p.8 matches sections; "Read page 6" → P6 map; P2 "Page 3 has the story / page 4 the sport" correct. P7 golden sentences: all 8 verbatim in the issue body, page attributions correct. Model text "My Monday, November 16" = 82 alphanumeric-token words (matches KIT and run.py).
- ABSTRACT.txt: one line, Spanish, 807 B, no ASCII double quotes, real topics + A2–B2 + 150 ejercicios.
- Curly double quotes balanced: SVG visible text 82/82. ASCII apostrophe 43 (es) vs 45 (core); curly apostrophe ’ = 0 in both — straight-apostrophe usage is the frozen core convention.
- Banned/internal strings in visible SVG text: 0 for SOP, proofread, TODO, PLACEHOLDER, Lorem, XXX, cover/Cover, estadio, stadio. VOL.4 ×12; VOL.5 ×8 (next-issue teasers); VOL.3 ×3 (legitimate). Middle dot · = 282. Furniture uses U+3000 (141 occurrences). Real CJK in visible es text = 0 (only U+3000).
- Weekdays (America/Toronto `date`): every date/weekday in the paper correct — Nov 3 Tue, Nov 8 Sun, Nov 9 Mon, Nov 10 Tue, Nov 15 Sun, Nov 16 Mon, Nov 18 Wed, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun, Nov 26 Thu, Nov 27 Fri, Dec 1 Tue, Dec 18 Fri, Jan 3 2027 Sun, Nov 21 2025 Fri, Jan 8 2026 Thu.
- Q109 clinic correction审定接受： "The count continue after the vote." → "The count continued after the vote." (past-tense correction, consistent with the clinic label and the issue's past frame).

## External facts (web-verified 2026-11-11, multiple sources each)
- US midterms (carried from previous build, unchanged in this rebuild): AP calls as of Sun Nov 8 — House D 254 / R 162, 19 uncalled; Senate 20 of 33 called to D, 13 R, 2 uncalled (Alaska, Mississippi); 7 flips (Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina, Texas); 5 governors (Georgia, Iowa, Nevada, Ohio, Texas); 35 Senate seats; 36 governor races; pre-vote House 218R–214D, Senate 53–47; new Congress convenes Jan 3, 2027; Georgia runoff Dec 1 if no majority (conditional statement correct as a rule); certification window Nov 10–Dec 18 consistent.
- 2025–26 Ashes retrospective (this rebuild's changed content — verified this round): series 4–1 to Australia (ECB statement, cricketcountry, ICC); Perth 1st Test won by Australia by 8 wickets inside two days (cricket.com.au, AP via Technorati, NetBet); shortest Ashes Test by balls bowled since 1888; Melbourne 4th Test England won by 4 wickets inside two days, first Test win in Australia in ~15 years (ICC, AP, Cricbuzz, CricketArchive); Sydney 5th Test Australia won by 5 wickets, series 4–1; series Nov 21, 2025–Jan 8, 2026.
- Hunger Games / I'm a Celebrity / Premier League / ATP / NFL / Anti-Bullying Week / World Children's Day / Thanksgiving (carried from previous build, unchanged): Sunrise on the Reaping opens Fri Nov 20, 2026; Collins novel 2025; Joseph Zada = Haymitch (16), McKenna Grace = Maysilee Donner, Ralph Fiennes = young President Snow, Francis Lawrence directs, 50th Games / Second Quarter Quell, twice as many tributes, Woody Harrelson played older Haymitch; I'm a Celebrity series 26 Mon Nov 16, 9 p.m., ITV1/ITVX, Ant & Dec, Murwillumbah NSW, one-day delay (England–Spain Nations League Sun Nov 15), Unpacked on ITV2, "How to Survive the Jungle" Sun Nov 15; Premier League Matchweek 11 Sat Nov 21 Man City–Fulham 12:30, Newcastle–Arsenal 17:30, Sun Nov 22 Liverpool–Man Utd 16:30; ATP Finals Turin Nov 15–22; NFL Week 11 Colts at Texans Thu Nov 19, Vikings–49ers in Mexico City Sun Nov 22 8:20 p.m. ET, Patriots on bye; Anti-Bullying Week Nov 16–20, theme "Break the Silence", Odd Socks Day Mon Nov 16, 10th anniversary, Anti-Bullying Alliance, ~8 million children, >80% of schools; World Children's Day Fri Nov 20, theme "My day. My rights. My future.", CRC adopted Nov 20, 1989; Thanksgiving Thu Nov 26 (4th Thursday), Black Friday Fri Nov 27.
- NOT source-verified (flagged, not asserted false): ATP singles final "not before 6 p.m. local time". (The two flags from the previous build — P4 "Day one is already sold out" and the Ashes first-ball time — are gone with the Ashes rewrite.)

## Visual inspection (8 print cards + web P1/P8 renders)
- Viewed: `cards/p1-front.png` … `p8-test.png` (all 8), `web-p1-1.png`, `web-p8-8.png` (72 dpi pdftoppm renders in this dir). Clean: masthead, VOL.4, date line, banners, headlines, article flow, all images + captions (Capitol; Audubon turkey; Rousseau tiger; W. G. Grace; Lawrence 1912 children; Hartford voting booth; Samuel Johnson 1772; Library of Congress Main Reading Room), footers ("Página N de 8"), IN THIS ISSUE, model text, ANSWERS block. No footer intrusion, no text overlap, no other overflow.
- Fixed-title crops: `crop-new-p2-life-title.png` (SENATE IN NUMBERS El Senado inside cream, +33.6 px), `crop-new-p6-deep-title.png` (HOW LONG? Duración inside cream, +142.3 px).
- Old-vs-new: old web P1/P8 renders in `prev-proof1-old-sha/` compared directly (P1: 4 intended diffs; P8: Ashes/Q39/Q40/Q52/Q46-note diffs only); P2/P6 title before/after crops; P2–P7 otherwise covered by freeze-diff vs core + KIT fix list + full text re-read (old full-page renders for P2–P7 did not survive).

## Core cross-check
- core-en `content34.py:61` keys `["b", "a", "d", "c"]`; core registry Q39=a / Q40=d. Core-vs-es key diffs: only 137–140, 150 (reader-language keys).
- Core-en source SHAs recorded in PROOF-NOTE (registry + content12/34/56/7/8) for the coordinator's before/after comparison. core-en and en-es both remain untracked new directories; no file in either was modified by this round (git status shows no M items for either path; other M items under production/2026-w47 belong to parallel editions).
