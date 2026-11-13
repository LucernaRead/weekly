# GATE-LOG — Lucerna Weekly 2026-W47 en-es · proof1

All measurements on disk in this scratch dir unless noted. Tools run with `~/workspace/weekly-git/tools/venv/bin/python`. Probe first: `git -C ~/workspace/weekly-git hash-object -w --stdin` OK + probe file written here. TMPDIR pointed at this scratch dir; /tmp never written.

## Identity / SHA (PASS)
- Print `The-Lucerna-VOL4-en-es.pdf`: 29,330,745 B, sha256 `e668bc5f40f8c6e3ddc7a1d705cc39bcd004a615a2d9f2f62a0cad68304bc719` (prefix e668bc5f40f8c6e3 ✓)
- Web `The-Lucerna-VOL4-en-es.web.pdf`: 2,377,727 B, sha256 `a0a2f9d6d3035e4df1e05f5cf8c73c3a7fea1e35f1440b4b18e52ca85e68bcd8` (prefix a0a2f9d6d3035e4d ✓)
- `2026-w47-en-es.text.md`: 53,837 B, sha256 `850fee7a0f45942896d5f2fbe91a58f4878626d2b2636266c2a7faa0288ab9db` (prefix 850fee7a0f459428 ✓)
- Both PDFs 8 pages, 1462.5×2025 pts.

## Text proofread (150 answers; 149/150 correct)
- Full text.md read. Registry: numbers 1–150 continuous; per-page 10/17/18/18/18/18/12/39; levels A2 62 / B1 66 / B2 22 — all match KIT.
- Answer lines 150/150 match `registry.json` exactly (key + level, 0 mismatches).
- Semantic check of every key against its stem: 148/150 correct. FAIL: Q39 (mentor, key d, correct a), Q40 (arena, key a, correct d) — see PROOF-NOTE D1. All other matching sets verified against SVG letter labels: P2 D 24–27, P4 C 56–59, P5 C 74–77, P8 F 141–144.
- Cross-references: IN THIS ISSUE p.2–p.8 matches sections; "Read page 6" / "Ver página 6" → P6 map; P2 "Page 3 has the story / page 4 the sport" correct. P7 golden sentences: all 8 verbatim in the issue body, page attributions correct. Model text "My Monday, November 16" = 82 alphanumeric-token words (matches KIT).
- ABSTRACT.txt: one line, Spanish, no ASCII double quotes, real topics + A2–B2 + 150 ejercicios.
- Curly double quotes balanced: text.md 81/81, SVG visible text 82/82. ASCII apostrophe 43 (es) vs 45 (core); curly apostrophe ’ = 0 in both — straight-apostrophe usage is the frozen core convention.
- Banned/internal strings in visible SVG text: 0 for 桥接, SOP, proofread, TODO, PLACEHOLDER, Lorem, XXX, cover/Cover. VOL.4 ×12; VOL.5 ×8 (next-issue teasers); VOL.3 ×3 (legitimate: "VOL.3 promised…", P6 Q93 option); no VOL.1/VOL.2. Middle dot · = 282, identical in core and es. Furniture uses U+3000 (141 occurrences). Real CJK in visible es text = 0; only 3 CJK chars in the non-visible moth `<title>Lucerna 三色蛾</title>` shared with core (KIT-disclosed).
- Weekdays (America/Toronto `date`): every date/weekday in the paper correct — Nov 3 Tue, Nov 8 Sun, Nov 9 Mon, Nov 10 Tue, Nov 15 Sun, Nov 16 Mon, Nov 18 Wed, Nov 19 Thu, Nov 20 Fri, Nov 21 Sat, Nov 22 Sun, Nov 26 Thu, Nov 27 Fri, Dec 1 Tue, Dec 18 Fri, Jan 3 2027 Sun.

## Mechanical gates
- occlusion_audit.py: 0 flags, selftest OK (all 6 planted classes fired incl. BOXTITLE). Caveat: BOXTITLE only covers bordered boxes (stroke or fill #2c2822); cream boxes are NOT covered — D2/D3 were found by the explicit boxtitle measurement below, not by the audit.
- p8.py extract: 150 keys extracted; noted set 60/150, identical to core set. p8.py compare: CLEAN, missing=[], extra_count=0, keydiff=[137, 138, 139, 140, 150] (expected: Spanish translation keys 137–140 + open writing task 150).
- keycheck (p8 extract vs registry): 149/150 exact; only Q150 truncated to "Pregunta abierta" (known extractor short-label pattern, same as core).
- freeze.py baseline: 8/8 SVGs byte-identical by direct sha256 comparison of reproduced vs shipped SVGs (repro in `freeze-final/build-copy/svg/`). freeze.py diff vs core-en: added CJK = 9 chars, all U+3000 (furniture separators). All added/removed English strings are furniture/bridges, gloss lines, instruction words (Completa/Empareja/Reescribe), "Translate:"→"Traduce:", or re-chunked P8 key lines with identical keys — no English article text changed. P8 added/removed both contain "38. b · 39. d · 40. a · 41. c" (same keys, different wrapping/notes), confirming Q39/Q40 are core-identical.
- creambox (raw): many −35..−37 "clearances" — all +45px-window false positives (next-section text).
- creambox_check.py (refined, authoritative): NO OVERFLOW on any page, 32 cream boxes, inside clearance +5.0 to +92.4 px; tightest P2 box y=1184 (+5.0, still positive); P7 toolbox box y=651, bottom 1008.2, clearance +48.5.
- boxtitle width (explicit, edition's own `svglib.text_w`, Noto Sans CJK SC 700): 17 cream-box titles measured. Fits: P1 THE WEEK IN NUMBERS +20.4, SEARCHES +259.7, IN THIS ISSUE +36.4, IN BRIEF +173.0; P2 THE CALENDAR +85.4, DID YOU KNOW? +210.3, AND YOU? +192.0; P3 COMING SOON +49.0, HAYMITCH'S GAMES +33.5; P4 WHY PERTH? +57.8, SATURDAY, NOVEMBER 21 +7.5; P5 ODD SOCKS, IN NUMBERS +27.7, SPEAK UP +152.2; P6 A PRACTICE BALLOT +58.3; P7 THE TOOLBOX +65.8; P8 MODEL +663.0. FAILS: P2 THE SENATE, IN NUMBERS −25.0 (D2); P6 HOW LONG? −5.7 (D3). Core comparison: core P2 title ends 989.1 vs rect 961.0 (−28.1, core-rooted); core P6 ends 1732.5 (+129.5, fits); core P1 fits by 1.5 px; core P4 fits by 0.7 px. Visual confirmation: crops `crop-p2-senate.png`, `crop-p6-howlong.png`, `crop-core-p2-senate.png`, `crop-p1-numbers.png`, `crop-p4-saturday.png` in this dir; P2/P6 spills visible on the full cards too.
- P8 minimum font size: 13.5 pt (≥ SOP §1.1 floor 9.75 pt, matches KIT); other pages' min font-size 15.5 pt.
- Print vs web PDF text layers: both 8 pages, 1462.5×2025 pts, pdftotext 48,972 bytes each, token-multiset diff 0/0.

## Visual inspection (8 print cards + web P1/P8 renders)
- Viewed: `cards/p1-front.png` … `p8-test.png` (all 8), `web-p1-1.png`, `web-p8-8.png` (72 dpi pdftoppm renders in this dir).
- Clean: masthead, VOL.4, date line, banners, headlines, article flow, all images + captions (Capitol; Audubon turkey; Rousseau tiger; W. G. Grace; Lawrence 1912 children; Hartford voting booth; Samuel Johnson 1772; Library of Congress Main Reading Room), footers ("Página N de 8"), IN THIS ISSUE, model text, ANSWERS block. No footer intrusion, no text overlap, no other overflow.
- Defects seen: D2 (P2 "El Senado" past the cream edge), D3 (P6 "mandato" final "o" straddling the cream edge), D1 (P8 ANSWERS prints "38. b · 39. d · 40. a · 41. c").
- P2 SAY IT boxes: "¡Feliz Día de Acción de Gracias!" fits inside its box (crop `crop-p2-sayit.png`).

## External facts (web-verified 2026-11-11, multiple sources each)
- US midterms: AP calls as of Sun Nov 8 — House D 254 / R 162, 19 uncalled; Senate 20 of 33 called to D, 13 R, 2 uncalled (Alaska, Mississippi); 7 flips (Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina, Texas); 5 governors (Georgia, Iowa, Nevada, Ohio, Texas); 35 Senate seats (33 regular + 2 specials FL/OH); 36 governor races; pre-vote House 218R–214D, Senate 53–47; new Congress convenes Jan 3, 2027; Georgia runoff Dec 1 if no majority (conditional statement in the paper is correct as a rule); certification window Nov 10–Dec 18 consistent; House Republicans voted Tue Nov 10 (Jim Jordan elected, Mike Johnson did not run); House Democrats vote Nov 18–19.
- I'm a Celebrity series 26: Mon Nov 16, 9 p.m., ITV1/ITVX, Ant & Dec, Murwillumbah NSW, one-day delay because England play Spain in the Nations League Sun Nov 15, Unpacked on ITV2, "How to Survive the Jungle" special Sun Nov 15, campmates unconfirmed at press time.
- Hunger Games: Sunrise on the Reaping opens Fri Nov 20, 2026; Collins novel 2025 (Mar 18, 2025); Joseph Zada = Haymitch (16), McKenna Grace = Maysilee Donner, Ralph Fiennes = young President Snow, Francis Lawrence directs, 50th Games / Second Quarter Quell, twice as many tributes, Woody Harrelson played older Haymitch; soundtrack album arrives Nov 13.
- Ashes: 1st Test Sat Nov 21 Perth (Optus/Perth Stadium), Cummins out (back), Hazlewood out (hamstring), Smith captains, Boland in, Doggett debut; England last won a series in Australia 2010–11 (3–1), lost 4–0 in 2017–18 and 2021–22, 2023 drawn 2–2; Australia lost their first Test at Perth Stadium Nov 2024 by 295 runs to India.
- Premier League Matchweek 11: Sat Nov 21 Man City–Fulham 12:30, Newcastle–Arsenal 17:30; Sun Nov 22 Liverpool–Man Utd 16:30. ATP Finals Turin Nov 15–22, field exactly Zverev, Alcaraz, Shelton, Medvedev, Cobolli, Fils, Tiafoe, Jodar (Jodar qualified Nov 6, debut); Sinner two-time defending champion out with knee injury; two groups of four. NFL Week 11: Colts at Texans Thu Nov 19, Vikings–49ers in Mexico City Sun Nov 22 8:20 p.m. ET, Patriots on bye, Patriots–Lions in Munich Sun Nov 15.
- Anti-Bullying Week Nov 16–20, theme "Break the Silence", Odd Socks Day Mon Nov 16, 10th anniversary, organised by the Anti-Bullying Alliance (England/Wales/NI), theme shaped by 200+ children, ~8 million children reached, >80% of schools.
- World Children's Day Fri Nov 20, theme "My day. My rights. My future.", CRC adopted Nov 20, 1989, UNICEF-led. Thanksgiving Thu Nov 26 (4th Thursday), Black Friday Fri Nov 27.
- NOT source-verified (flagged, not asserted false): P4 "Day one is already sold out"; Ashes first ball "10:20 a.m. local — 2:20 a.m. in London" (timezone arithmetic consistent; start time itself not source-checked); ATP singles final "not before 6 p.m. local time".

## Core溯源 (defects whose root is core-en)
- D1 (Q39/Q40 keys): core-en `content34.py` line 61 keys `["b", "d", "a", "c"]` identical; core registry identical; core P3 SVG letter order identical. → core-level candidate for the coordinator.
- D2 (P2 title overflow): core title also overflows the same box by 28.1 px (visually confirmed on the core card). → core-level candidate.
- D3 (P6 title overflow): core fits by 129.5 px. → es-only, fixable in the es layer.
- O1 (P5 bridge triple) and O2 (NEXT WEEK "second week in Perth"): both are core text, frozen; recorded as observations only.
