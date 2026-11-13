# it-nl RECORD — COMPLETE (build2, 2026-11-11)

## Deliverables
- Print PDF `La-Lucerna-VOL4-NL.pdf` — 14,034,647 bytes, sha256 `9322290029fa8175400a21cf2539346ba767fa8299812c6b7cb1c039d36ea242`
- Web PDF `La-Lucerna-VOL4-NL-web.pdf` — 1,259,635 bytes, sha256 `6c546925c847f034bd1381b435a8cdbb863920f3597f9ae3e994356298655d56`
- `2026-w47-it-nl.text.md` — 55,590 bytes, 1317 lines, 150 exercises (exported from production sources)
- `ABSTRACT.txt` (Dutch, one line, no ASCII double quotes — full text in `build_edition.py` ABSTRACTS and in the edition WEEKLY-KIT.md §7)
- `WEEKLY-KIT.md` written (mirror of the en/de/fr/es/pt KIT structure; nl numbers §7/§8)
- 8 SVG in `svg/` + 8 cards in `cards/`

## Gates — ALL PASS (`nl/gates2.log`, build2)
- run.py rc 0, 150 exercises, zero FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE; flow ends P7 col3 1673.0, P8-ex col 3 y=941.1, P8-keys col 3 y=2529 (bottom 2552, 23 px spare)
- occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff [137,138,139]); freeze fragments 0 unexplained; freeze baseline direct sha256 8/8
- strict-CJK added = 8 × U+3000 only; print/web multiset identical (7,905 words); web < 7 MB; P8 min font 13.0 px = 9.75 pt
- §1.1 scans pass; VOL.5 = 3 legitimate nodes (same as core); textmd validate 0/0; keys match (except 137–139 + writing); notes match translations.py (table_gaps empty)
- P8 chip check: Q113–120, Q145–149, Q150 all B1, = core 1:1

## Build history — 2 builds
- Pre-build shortenings (13 nl values in `translations.py`, each count-asserted 1×, applied BEFORE building — the de/fr/es/pt lesson): match_set instr "Koppel elk woord aan de betekenis" (317.1px) → "Koppel de woorden" (177.7px, budget 254.5px); P4 E TU 3 lines → 2 ("Welke wedstrijd kijk je zondagavond? Schrijf twee zinnen in het Italiaans.", send-clause dropped); P7 disclosure 5 lines → 3 ("Voorbeeld van de redactie, geen echte brief. Geen echte brieven of beste opstellen; de belofte geldt voor VOL.5."); P7 error notes → 1 line each, colon forms ("La Lazio: enkelvoud, het werkwoord ook." / "Na è probabile che: aanvoegende wijs." / "Torrone: enkelvoud, het werkwoord ook." — the "… , het werkwoord ook." forms still measured 2 lines); P1 cifre → 2 lines each (29 → "(Lazio leidt)"; 24 → "(24 doelpunten in 10 wedstrijden)" with ", in tien wedstrijden" dropped from the head; 20.45 → "(20.45 uur)"; meer dan 150 → "(meer dan 150 figuranten)"); P8 notes 44/134 → "Onderwerp + werkwoord", 136 → "Onderwerp + werkwoord", 87 → "Het zijn oefengegevens, geen voorspellingen".
- P8 estimate (es method): 6 two-liners (44, 87, 134, 136, 137, 138), total 4592.6 px vs 4576 px capacity (−16.6 px); 87 + 136 conversions save 29.6 px (est. ~4563 px); 44/134 measured 2 lines even after shortening. Build1 confirmed P8-keys ends 2529/2552 — the same as es/pt (estimator conservative by ~10 px, as in pt).
- Build1 (~270 s): run.py rc 0, 150 exercises, writing_type "Schrijven". Gates1 19/20 — one failure, a REAL defect: [EDGE] p1-prima.svg "ITALIAANS WEEKBLAD" ink box (-2.7, 303.75, 452.3, 331.5) outside the page. Root cause: the P1 masthead band is drawn centered at x=975 with letter-spacing 11.5 (`content12.py:18`); the Dutch name is the longest Latin masthead, so the band is ~5.4 px wider than the page. Fix at source (edition file only): `content12.py:18` spacing 11.5 → 11.0. Build1 SHAs superseded: print 14,034,681 bytes, web 1,259,644 bytes.
- Build2 interruption (environmental, not a build defect): the first `rebuild3.py nl build2` was SIGTERM'd by a service restart mid-render (run.py ALL DONE; render.py wrote cards but no print PDF — session proc_c519339088fd, exitSignal 15); the second attempt's tool call timed out at dispatch (180 s) and its session vanished after the last card, again before the print PDF. Recovery: ran the remaining steps individually as backgrounded commands — render.py (RC=0, print PDF 14,034,647 bytes at 03:39), webpdf.py (RC=0, 1,259,635 bytes at 03:41), `.text.md` export (55,590 bytes, 150 exercises at 03:42) — each verified separately. The build2.log in nl/ is from the run.py step of the interrupted attempts (ALL DONE, no overflow); render2.log/webpdf2.log are from the step-wise recovery runs. Lesson for ru/ja/ko/zh-tw: prefer backgrounded step-wise runs over one long foreground rebuild when the runtime is busy; a killed render leaves valid SVGs + cards but stale PDFs, so always re-verify PDF mtimes/SHAs after any interruption before running gates.
- Re-aimed nl keys (from build_edition.py tr() of the Chinese sources): 137 "Voor de Madonna della Salute steken mensen de geloftebrug over." / note "Vergelijk met het origineel"; 138 "Zondagavond speelt Atalanta tegen Inter." / "si gioca = wordt gespeeld"; 139 "Zaterdag speelt Lazio thuis tegen Lecce." / "in casa = thuis"; 140 "Elk getal moet duidelijk zijn. → ___" / "dovere = moeten".

## Visual — 8/8 cards viewed (build2), zero defects
- P1: masthead band FIXED — first node now x=10.5, spacing 11.0, "ITALIAANS WEEKBLAD VOL.4 LA SERIE A IL TORRONE VENEZIA" fully visible with margins both sides; cifre box 2-line items clean; bridge 3 lines OK; footer "Pagina 1 van 8".
- P2: "Koppel de woorden" instr fits; E TU box reader question fits ("Ben je weleens over een geloftebrug gelopen of heb je een boom geplant? Schrijf twee zinnen in het Italiaans naar de redactie.").
- P3: E TU box clean ("Houd je meer van torrone of van chocolade? Schrijf twee zinnen en stuur ze op.").
- P4: E TU box ends flush with the table header at 1140.45 = core; match_set instr fits; results table clean.
- P5: clean (structural mid-page whitespace is the core pattern).
- P6: clean — practice bar chart + "VOORBEELDMINIMA" box + Q83–100.
- P7: error notes 1 line each; disclosure 3 lines ends 1673.0, clear of the FRASI hline; LA PAROLA gloss 2 lines.
- P8: Q113–120 B1 badges; 141–144 "Koppel de woorden" fits, no graze; RISPOSTE 1–150 all present; Q137/138/139 wrap to 2 lines each (fit, flow ends 2529/2552); Q44/134 wrap to 2 lines each (fit); Q136 1 line; Q87 1 line; Q149/Q150 separate lines; "150. ✓ Modeltekst in sectie H hieronder (99 woorden)".

## Self-read — full .text.md (1317 lines), all 150 keys re-verified
- Dutch explanation layer throughout; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK).
- Spot checks: Q22 A gelofte uit 1630; Q29 B; Q32 A «Fate dolci» (note uses “Fate dolci” curly quotes — the translations.py nl value verbatim, see below); Q44/134 note "Onderwerp + werkwoord"; Q51 B; Q58 "più + bella: zondagavond is het mooist (een oordeel)" (kept, 1-liner); Q59 meglio; Q66 B 23 Nov; Q81 Vero; Q82 Falso; Q85 B (13−11=2); Q86 A (6+7=13); Q87 note "Het zijn oefengegevens, geen voorspellingen"; Q92 +0.8% (note "Groei Prognose voor 2027: +0,8 %" — see below); Q104 B; Q108 A; Q112 B; Q120 B 24 Nov; Q136 note "Onderwerp + werkwoord" (converted); Q137–140 re-aimed.
- Model text 99 words frozen. Disclosure 3-line version in P7 LETTERE (nl): "Voorbeeld van de redactie, geen echte brief. Geen echte brieven of beste opstellen; de belofte geldt voor VOL.5."
- Table-value observations (pre-existing, NOT introduced by this build; left as-is for the independent proofreader): Q92 note "Groei Prognose" (Dutch compounds are one word: "Groeiprognose"); Q32 note “Fate dolci” (curly double quotes vs « » elsewhere).

## Quota stops on this shift: NONE. Core-it untouched.

---

## Re-fan-out (2026-11-11)
- Rebuilt from core-it fix3 (36bdec2e) by build_edition.py, RC=0 first attempt; text.md 55,509 bytes, 1317 lines, 150 exercises.
- Gates: 20/20 PASS, 0 FAIL (`scratch-refanout-it/gates-nl.log`); P8-keys flow ends y=2529 (bottom 2552); freeze baseline re-taken 8/8 (this dir's baseline is the re-fan-out one; first-fan-out baseline preserved in `scratch-refanout-it/prev-fanout/nl/`).
- fix3 9 lines + E labels + table values verified by `scratch-refanout-it/check_refanout.py` (ALL PASS); sim cross-check 0 unexpected changes.
- KIT updated with the new SHAs + §11 (see the edition dir). Full report: `scratch-refanout-it/FANOUT-REPORT-it.md`.
