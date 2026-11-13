# W47 IT fan-out — STATUS (updated 2026-11-11 ~05:40 UTC / 2026-11-11 00:40 EST)

## ✅ it-zh-tw COMPLETE (build1, 2026-11-11 ~05:40 UTC) — 10 of 10 done — FAN-OUT COMPLETE
- Print PDF `La-Lucerna-VOL4-ZH-TW.pdf` 27,779,760 bytes, sha256 `6171fea645bd67e0c06d77934229c727b71465aec3fc3f42a82a41ab1933e9f0`; web PDF `La-Lucerna-VOL4-ZH-TW-web.pdf` 2,042,022 bytes, sha256 `57e29e6ff725a3c093e4d1a51f9d2c0113aeff8c8481e62c27752da0e43fce16`; `.text.md` 52,568 bytes / 1317 lines; ABSTRACT.txt (ZH-TW, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`zh-tw/gates1.log`, build1 — first attempt): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; print/web multiset identical (6,843 words each, chars equal); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK). No strict-CJK check for zh-tw (reader values are themselves CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1 — coordinates BYTE-IDENTICAL to the core, including Q150 (y=586), unlike ja/ko which flow 30 px lower.
- Visual: 8/8 cards viewed (build1), zero defects (P1 masthead band starts x=185.8, exactly the core's start; P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 2 lines ends 1644.0, clear of the FRASI hline; P8 match instr "把詞和釋義配對" fits; P8-keys flow ends 2484/2552 — 68 px spare; P3/P5 structural whitespace is the core pattern, left as-is). P5 word list wraps after 'sede ·' (same as core, unlike ja/ko). P8 separators keep the Italian "— PAGINA {pg} —" by design (P8_SEP["zh-tw"], same as en/de/fr/es).
- Self-read: full .text.md 1317 lines read; only Simplified Chinese residue is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); Traditional Chinese explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A 1630 年誓願, Q29 B, Q32 A "Fate dolci" (curly quotes — table value verbatim, same as nl/ko), Q51 B, Q58 "più + bella 週日晚上最好看（主觀評價）", Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q87 "圖表數據是練習用的、不是真實預報", Q92 B +0.8%, Q120 B 24 Nov, Q135 note "疑問詞組在句首", Q136 note "主語 + 動詞 + 地點", Q137–140 re-aimed).
- Build history (1 build + step-wise recovery; full record in `zh-tw/RECORD.md`): 5 zh-tw values PRE-shortened before building — the 4 cifre lines rewritten whole-line into Traditional Chinese (the table's zh-tw values still carried the full Italian descriptive head: 11 lines vs the 8-line budget; rewrites total 6 lines) and the 44/134 note PRE-EMPTIVELY shortened to "主語 + 動詞" (ja/ko lesson). Everything else already fit as measured (instr 136.5 px; error notes all 1 line; disclosure 2 lines; gloss 2 lines; bridge 2 lines; FRASI all 1+1). **Build driver SIGTERM'd by a service restart at ~284 s** (after run.py ALL DONE + render.py had written the print PDF + 8 cards, during webpdf) — recovered step-wise per the nl lesson: print PDF verified first (8 pages, pdftotext 102,884 bytes), then webpdf.py alone (~298 s), then the `.text.md` export alone via `zh-tw/export_textmd.py` (52,568 bytes, 150 exercises) — each verified (fresh mtimes + SHAs) before gates. No tool fixes in this shift — the ja-shift fixes carried over and the zh-tw build passed first attempt.
- Table-value observations (pre-existing, NOT introduced by this build; left as-is for the independent proofreader): P4 results title reads "第 11 輪賽果（6–8 novembre）" — the month name stays Italian inside the Traditional Chinese title (translations.py zh-tw value verbatim); Q32 note uses "Fate dolci" (curly quotes vs « » elsewhere, same as nl/ko).
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: none — all 10 fan-out editions complete. Coordinator assigns independent proofreaders per edition.

## ✅ it-ko COMPLETE (build1, 2026-11-11 ~05:20 UTC) — 9 of 10 done
- Print PDF `La-Lucerna-VOL4-KO.pdf` 19,296,953 bytes, sha256 `522008ebdfed52952fc51ebdabae6ab69af7a30ae92a70610b1cd99409c5a517`; web PDF `La-Lucerna-VOL4-KO-web.pdf` 1,575,451 bytes, sha256 `a9bdc956ca19be6fd5acc37df5ee6e54f3fd2afdc43b456ba7f131d131652763`; `.text.md` 57,376 bytes / 1317 lines; ABSTRACT.txt (KO, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`ko/gates1.log`, build1 — first attempt): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; print/web multiset identical (7,425 words each, chars equal); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK). No strict-CJK check for ko (reader values are themselves CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1 (same coordinates except Q150, y=616 vs core y=586, same as ja).
- Visual: 8/8 cards viewed (build1), zero defects (P1 masthead band starts x=133.2, both margins clean; P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr "단어와 뜻을 연결하세요" fits; P8-keys flow ends 2499/2552 — 53 px spare; P3/P5 structural whitespace is the core pattern, left as-is). OBSERVATION (not a defect): P5 word list wraps after 'incontro' (core: after 'sede ·'), so its second line starts with '·' — same words, different break, as in ja. P3 word box wraps after 'corteo ·' (same as core).
- Self-read: full .text.md 1317 lines read; only non-Korean CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); Korean explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A 1630년의 서원, Q29 B, Q32 A "Fate dolci" (curly quotes — table value verbatim, same as nl), Q51 B, Q58 "più + bella: 일요일 저녁이 가장 좋다（주관적 평가）", Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q87 "차트 수치는 연습용 자료이며 실제 예보가 아닙니다", Q92 B +0.8%, Q120 B 24 Nov, Q135 note "의문어구는 문장 맨 앞에", Q136 note "주어 + 동사 + 장소", Q137–140 re-aimed).
- Build history (1 build; full record in `ko/RECORD.md`): 3 ko values PRE-shortened before building — disclosure 4→3 lines (C3; the minimal C1 form still measured 4 lines at 1142.0 px, 6.5 px over), cifre 20.45 3→2 lines (D2; the unedited value wrapped to 3 because the closing fullwidth paren spilled onto a third line), and the 44/134 note PRE-EMPTIVELY shortened to "주어 + 동사" (ja lesson — the ja build1 P8-keys ended 2561, 9 px over, from column-break waste; doing it before building saved ko a rebuild). Everything else already fit as measured (instr 190.3 px; error notes all 1 line; gloss 2 lines; cifre total 8; bridge 2 lines; FRASI all 1+1). Build1 ~191 s (KR svglib wraps much faster than JP with kinsoku). No tool fixes in this shift — the ja-shift fixes carried over and the ko build passed first attempt.
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-zh-tw (build_edition.py zh-tw) — the LAST edition.

## ✅ it-ja COMPLETE (build2, 2026-11-11 ~05:08 UTC) — 8 of 10 done
- Print PDF `La-Lucerna-VOL4-JA.pdf` 28,221,078 bytes, sha256 `f0fb8a83671a4d7bfee852436c907b6372a7631be92a7ef4725f2154d0e97220`; web PDF `La-Lucerna-VOL4-JA-web.pdf` 1,869,651 bytes, sha256 `b6660f12a4d57833139ba6a80a7d4fc2cd033f308ed3cf35fa36bfacdaf72cf3`; `.text.md` 58,239 bytes / 1317 lines; ABSTRACT.txt (JA, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`ja/gates2.log`, build2): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; print/web multiset identical (6,760 words each, chars equal); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK). No strict-CJK check for ja (reader values are themselves CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1 (same coordinates except Q150, y=616 vs core y=586).
- Visual: 8/8 cards viewed (build2), zero defects (P1 masthead band starts x=102.3, リ visibly present; P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr "単語と意味を合わせなさい" fits; P8-keys flow ends 2546/2552 — only 6 px spare, deterministic, accepted; P3/P5 structural whitespace is the core pattern, left as-is). OBSERVATION (not a defect): P5 word list wraps after 'incontro' (core: after 'sede ·'), so its second line starts with '·' — same words, different break.
- Self-read: full .text.md 1317 lines read; only non-Japanese CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); Japanese explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A 1630年の誓い, Q29 B, Q51 B, Q58 "più + bella：日曜の夜が一番すばらしい（主観的な評価）", Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q87 "グラフの数字は練習用のデータで、本物の予報ではありません", Q92 B +0.8%, Q120 B 24 Nov, Q135 note "疑問句は文頭に", Q136 note "主語 + 動詞 + 場所", Q137–140 re-aimed).
- Build history (2 builds; full record in `ja/RECORD.md`): 5 ja values PRE-shortened before building (instr 273.0→234.0 px; disclosure 4→3 lines; Torrone error note 2→1; cifre 20.45 + 150 each 3→2 lines; total cifre 8 lines). **First build attempt DIED at 2.7 s on a tool bug: build_edition.py's residual-CJK check flagged legitimate Japanese as "residual Chinese" — fixed in the scratch tool (CJK readers get a key-residue check instead of the generic regex); the half-built dir was removed before re-running. This fix is REQUIRED for ko and zh-tw too.** Build1: P8-keys flow ended 2561 (9 px over) with NO "FLOW OVERFLOW" in the log — root causes: column-break waste (~52 px; the sum-of-advances estimate 4533.3 px ignores it) + run.py's `_fit` omits the 13 px first-baseline offset, so the last para can cross the bottom by up to 13 px silently. Fix: shared 44/134 note "主語 + 動詞 + 場所 + 日付" → "主語 + 動詞" (applied to translations.py + content34.py:98 + content8.py:62 — rebuild trap). Build2: P8-keys 2546/2552. Gates1 FAILED 2 items, both tool bugs: occlusion [COVER] 'リ' 89% (the audit read the P1 moth's LOCAL coords as page coords — fixed in the SHARED `tools/occlusion_audit.py` with a transform stack + a selftest regression case; verified no regression: core/ru/en audits still 0 flags) and freeze P5 fragments (same text, different wrap — fixed in scratch `gates.py` with the adjacent-pair rule). Gates2 ALL PASS. **P8 estimator lesson for ko/zh-tw: "total ≤ 4576 px" is NOT sufficient — allow ~50–130 px for break waste; always read the build log's `flow[P8-keys] ended` line. Probe scripts in `ja/` are reusable for ko (KR index, drop the kinsoku port).**
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-ko (build_edition.py ko), then zh-tw.

## ✅ it-ru COMPLETE (build3, 2026-11-11 ~04:35 UTC) — 7 of 10 done
- Print PDF `La-Lucerna-VOL4-RU.pdf` 14,181,162 bytes, sha256 `b70e7b62da565b7fdb4aa18a56995bb7c366af395fca7c31847ebf857254b2b4`; web PDF `La-Lucerna-VOL4-RU-web.pdf` 1,407,790 bytes, sha256 `1c93b80d57de5e76b036bd60a2f2af05fde2d65c1ceb05e469344b657debd964`; `.text.md` 67,722 bytes / 1317 lines; ABSTRACT.txt (RU, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`ru/gates4.log`, build3): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; strict-cjk added = 8 × U+3000 only; print/web CHARACTER multiset identical (print 7,601 / web 7,708 words — word-count difference is a pdftotext splitting artifact on letter-spaced Cyrillic; char multiset equal, print-only/web-only both empty); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1.
- Visual: 8/8 cards viewed (build3), zero defects (P1 masthead band starts x=119.6, both margins clean; P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr "Соедините слова" fits; P8-keys flow ends 2529/2552; P3/P5 structural whitespace is the core pattern, left as-is). OBSERVATION (rendering characteristic, NOT a defect — pixel-verified, recorded in `ru/RECORD.md` + KIT §10 for the proofreader): word gaps at svglib run boundaries measure ~3–5 px vs ~7–9 px inside a run (P7 FRASI translations, P2/P3 NOTE glosses); layout advances are correct, no overlap/tofu; changing it would mean modifying the shared svglib measurement and risk pushing the P8 flow (only 23 px spare) over capacity — engine left untouched.
- Self-read: full .text.md 1317 lines read; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); Russian explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A 1630, Q29 B note "Торроне закрывается в воскресенье 22 ноября", Q51 B, Q58 più bella, Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q92 B +0.8%, Q120 B 24 Nov, Q135 note "Вопрос — в начале", Q137–140 re-aimed).
- Build history (3 builds; full record in `ru/RECORD.md`): 18 ru values PRE-shortened before building. Build1 gates FAILED 4 items — [LINEX] P7 col3 1702.0 (extra line was the LA PAROLA gloss, not the disclosure); freeze fragments (footer/NOTE words split by the ru svglib) + print/web word-multiset diff (pdftotext Cyrillic splitting) + textmd REV 'Страница' — the last three are one root cause (svglib fragment-splitting), fixed in the scratch tools, not the edition. **Rebuild trap: `rebuild3.py` does NOT re-run the table pass** — translations.py-only edits after build1 never reach the edition (build2 changed nothing); after build1, shortenings must be applied identically to BOTH translations.py AND the edition's `content*.py`. Build2 fixes applied directly to edition sources: `content7.py` gloss (2 occurrences) 3→2 lines, `content34.py:61` Q29 note (2-line RISPOSTE answer → 1 line). Build3 gates3 failed only textmd REV 'ИТАЛЬЯНСКОМ' (footer-left words split) — validator fixed with FOOT_FULL; gates4 ALL PASS. **P8 estimator correction: `Flow.para` defaults to `kind="serif"` — RISPOSTE answers are SERIF 13 in 422.5 px, not sans** (serif re-estimate 5 two-liners / 4577.8 px exactly matched the built flow end 2561). P1 band lesson: isolated BSPage4 measurement predicted x=−119.6, real built band x=119.6 — do NOT pre-fix the band; trust the built SVG. Ru `wrap()` is slow (~20–25 s per call, Noto fonts load per call) — background measurement commands.
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-ja (build_edition.py ja), then ko → zh-tw.

## ✅ it-nl COMPLETE (build2, 2026-11-11 ~04:05 UTC) — 6 of 10 done
- Print PDF `La-Lucerna-VOL4-NL.pdf` 14,034,647 bytes, sha256 `9322290029fa8175400a21cf2539346ba767fa8299812c6b7cb1c039d36ea242`; web PDF `La-Lucerna-VOL4-NL-web.pdf` 1,259,635 bytes, sha256 `6c546925c847f034bd1381b435a8cdbb863920f3597f9ae3e994356298655d56`; `.text.md` 55,590 bytes / 1317 lines; ABSTRACT.txt (NL, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`nl/gates2.log`, build2): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; strict-cjk added = 8 × U+3000 only; print/web multiset identical (7,905 words); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1.
- Visual: 8/8 cards viewed (build2), zero defects (P1 masthead band FIXED — first node x=10.5, spacing 11.0, both margins clean; P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr "Koppel de woorden" fits; P8-keys flow ends 2529/2552; P3/P5 structural whitespace is the core pattern, left as-is).
- Self-read: full .text.md 1317 lines read; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); Dutch explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A gelofte uit 1630, Q51 B, Q58 "zondagavond is het mooist (een oordeel)" kept as a 1-liner, Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q87 "Het zijn oefengegevens, geen voorspellingen", Q92 +0.8%, Q120 B 24 Nov, Q136 note "Onderwerp + werkwoord" converted, Q137–140 re-aimed).
- Build history (2 builds; full record in `nl/RECORD.md`): 13 nl values PRE-shortened before building. Build1 gates 19/20 — one REAL defect: [EDGE] P1 masthead band "ITALIAANS WEEKBLAD" ink box x=-2.7 outside the page (Dutch name is the longest Latin masthead; band centered at 975 with letter-spacing 11.5, ~5.4 px wider than the page). Fix (edition file only): `content12.py:18` spacing 11.5 → 11.0 — band now starts x=10.5, occlusion 0. Build2 was interrupted TWICE by the environment (service-restart SIGTERM mid-render, then a dispatch-timeout kill after the last card, both before the print PDF) — recovered by running render.py / webpdf.py / .text.md export individually as backgrounded commands, each verified (RC=0, fresh PDF mtimes/SHAs) before gates. LESSON for ru/ja/ko/zh-tw: prefer backgrounded step-wise runs over one long foreground rebuild when the runtime is busy; after any interruption, re-verify PDF mtimes/SHAs before running gates (a killed render leaves valid SVGs + cards but stale PDFs). Table-value observations (pre-existing, left as-is for the proofreader): Q92 note "Groei Prognose" (should be one word "Groeiprognose"); Q32 note “Fate dolci” (curly quotes vs « » elsewhere).
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-ru (build_edition.py ru), then ja → ko → zh-tw.

## ✅ it-pt COMPLETE (build1, 2026-11-11 ~04:00 UTC) — 5 of 10 done
- Print PDF `La-Lucerna-VOL4-PT.pdf` 14,036,807 bytes, sha256 `4492665b04a7a631c9e8ace2cd15cfe077dbd3607f78b6aab228e05470629882`; web PDF `La-Lucerna-VOL4-PT-web.pdf` 1,262,226 bytes, sha256 `164492f8ab7b69f166b47778f856ae9d16cb29ed43dc2458208cc804f41e93c1`; `.text.md` 55,820 bytes / 1317 lines; ABSTRACT.txt (PT, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`pt/gates1.log`, first run): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; strict-cjk added = 8 × U+3000 only; print/web multiset identical (7,981 words); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1.
- Visual: 8/8 cards viewed, zero defects (P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr "Relaciona as palavras" fits; P8-keys flow ends 2529/2552; P3/P5 structural whitespace is the core pattern, left as-is). OBSERVATION (not a defect): P1 masthead band starts at x=0.0, flush with the left page edge (same as es); initial "S" and final "A" fully rendered, no glyph clipped, right edge ≈1881 < 1950.
- Self-read: full .text.md 1317 lines read; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); Portuguese explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A voto de 1630, Q51 B, Q58 "o domingo à noite é o melhor (uma opinião)", Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q87 "São dados de prática, não previsões", Q92 +0.8%, Q120 B 24 Nov, Q136 note "Sujeito + verbo + lugar" kept as a 1-liner, Q137–140 re-aimed).
- Build history (1 build; full record in `pt/RECORD.md`): 13 pt values PRE-shortened before building. Disclosure needed "passa ao VOL.5" (not "passa para o") to reach 3 lines — both "passa para o" candidates measured 4. P8 estimate (es method): 7 two-liners, 4607.4 px vs 4576 px capacity; expected only 3 conversions (134 measured 2 lines by wrap() — "Sujeito" one letter longer than es "Sujeto") — but build1 P8-keys ended 2529/2552, same as es, and the shipped P8 card shows 134 on ONE line. LESSON: the estimator is conservative by ~10 px (Flow.para wraps slightly tighter than a direct wrap() call at the same width); trust the build log's flow end when estimate and build disagree by < 15 px. Edit-script slip: the Torrone error-note pt value has no leading "O " ("Torrone é singular, …") — caught by the count assertion before any write, corrected, re-ran cleanly.
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-nl (build_edition.py nl), then ru → ja → ko → zh-tw.

## ✅ it-es COMPLETE (build1, 2026-11-11 ~03:30 UTC) — 4 of 10 done
- Print PDF `La-Lucerna-VOL4-ES.pdf` 14,033,685 bytes, sha256 `9c7ee019b041a7484aed75d92c5d9f21f7e899fde8e8fa05813cc3c60b0b8d31`; web PDF `La-Lucerna-VOL4-ES-web.pdf` 1,259,244 bytes, sha256 `d05e956d056c76f8bf3f6ce560073d1c341a7e1ea71ce0fa17f1e19ee3d93408`; `.text.md` 56,259 bytes / 1317 lines; ABSTRACT.txt (ES, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`es/gates1.log`, first run): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; strict-cjk added = 8 × U+3000 only; print/web multiset identical (8,012 words); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1.
- Visual: 8/8 cards viewed, zero defects (P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr "Relaciona las palabras" fits; P8-keys flow ends 2529/2552; P3/P5 structural whitespace is the core pattern, left as-is). OBSERVATION (not a defect): P1 masthead band starts at x=0.0, flush with the left page edge (en 7.4, fr 63.2, core 185.8); zoom-verified the initial "S" and final "A" are fully rendered, no glyph clipped, right edge ≈1881 < 1950. Same pattern as the accepted en edition, at the boundary. pt ("SEMANÁRIO ITALIANO") and nl ("ITALIAANS WEEKBLAD") will likely show the same; watch, do not pre-fix.
- Self-read: full .text.md 1317 lines read; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); Spanish explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A voto de 1630, Q51 B, Q58 "el domingo por la noche es el mejor (una valoración)", Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q87 "Son datos de práctica, no previsiones", Q92 +0.8%, Q120 B 24 Nov, Q136 note "Sujeto + verbo + lugar" kept as a 1-liner, Q137–140 re-aimed).
- Build history (1 build; full record in `es/RECORD.md`): 12 es values PRE-shortened before building (de/fr lesson). NEW P8 estimation method (use for pt/nl/ru/ja/ko/zh-tw): map the fr `.text.md` RISPOSTE lines through translations.py (fr→reader, longest-first) and wrap each at sans 13 in 422.5 px — es estimate was 7 two-liners, 4607.4 px vs 4576 px capacity (−31.4 px); 4 P8 note shortenings (44/134, 58, 87) saved 59.3 px; build1 confirmed P8-keys ends 2529/2552. Caution: 44/134 share the "主语 + 动词 + 地点 + 日期" entry while 136 uses "主语 + 动词 + 地点" — different entries, verify against the previous edition's content8.py before shortening.
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-pt (build_edition.py pt), then nl → ru → ja → ko → zh-tw.

## ✅ it-fr COMPLETE (build1, 2026-11-11 ~03:05 UTC) — 3 of 10 done
- Print PDF `La-Lucerna-VOL4-FR.pdf` 14,034,268 bytes, sha256 `5445d1a62f631bb75cafcb20df40c376d44b608254824444166714670f2dc0c7`; web PDF `La-Lucerna-VOL4-FR-web.pdf` 1,258,939 bytes, sha256 `416b11053b82475ad84bcb1badc10d992357a3e0fbde1786c55bee693bb3c0a8`; `.text.md` 56,616 bytes / 1317 lines; ABSTRACT.txt (FR, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`fr/gates2.log`): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; strict-cjk added = 8 × U+3000 only; print/web multiset identical (8,028 words); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1.
- Visual: 8/8 cards viewed, zero defects (P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr "Associe mots et définitions" fits, no graze; P3/P5 structural whitespace is the core pattern, left as-is).
- Self-read: full .text.md 1317 lines read; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent); French explanation layer throughout; all 150 keys re-verified (spot checks: Q22 A vœu de 1630, Q51 B, Q58 "le plus beau dimanche soir (un jugement)", Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q87 "Ce sont des données d'exercice, pas des prévisions", Q92 +0.8%, Q120 B 24 Nov, Q137–140 re-aimed).
- Build history (1 build; full record in `fr/RECORD.md`): 13 fr values PRE-shortened before building (de lesson). Build1 zero overflow on first attempt (P4 col3 1140.45 = core, P7 col3 1673.0). Gates1 19/20 — textmd validate reverse-miss 8 (REV 'Page N sur 8'): a VALIDATOR bug, not an edition defect — the reverse skip regex in scratch `validate_edition_textmd.py` only covered footers with prepositions of/di/de/von/из//, never fr "sur" (nor nl "van", ja/ko/zh-tw forms). Fix (scratch tool only): per-language FOOT_RE dict added covering all 10 languages (es/pt `Página N de N`, nl `Pagina N van N`, ru `Страница N из N`, ja `N ページ（全 N ページ）`, ko `제 N 면 / 총 N 면`, zh-tw `第N版／共N版`). Gates2 re-run: GATES ALL PASS.
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-es (build_edition.py es), then pt → nl → ru → ja → ko → zh-tw.

## ✅ it-de COMPLETE (build5, 2026-11-11 ~02:34 UTC) — 2 of 10 done
- Print PDF `La-Lucerna-VOL4-DE.pdf` 14,037,296 bytes, sha256 `6903d98b3adb07c1fea0ff1e9b844cc8d8950fc8cfd34adb82394582bbf304cf`; web PDF `La-Lucerna-VOL4-DE-web.pdf` 1,265,110 bytes, sha256 `a62a094705fabd79cd70efec5083835e5cc2ff2d943f36c19d851f0f36cee6e1`; `.text.md` 56,734 bytes / 1317 lines; ABSTRACT.txt (DE, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`de/gates5.log`): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained; freeze baseline direct sha256 8/8; strict-cjk added = 13 × U+3000 only; print/web multiset identical (7,798 words); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1.
- Visual: 8/8 cards viewed, zero defects (P4 E TU box flush with the table header at 1140.45 = core; P7 disclosure 3 lines ends 1673.0, clear of the FRASI hline; P8 match instr short, no graze on the model text; P3/P5 structural whitespace is the core pattern, left as-is).
- Self-read: full .text.md 1317 lines read; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK); German explanation layer throughout; all 150 keys re-verified (spot checks: Q51 B, Q58 più bella, Q59 meglio, Q66 B 23 Nov, Q81 Vero, Q82 Falso, Q85 B 2, Q86 A 13, Q92 +0.8%, Q120 B 24 Nov, Q137–140 re-aimed).
- Build history (5 builds; full record in `de/RECORD.md`): build1 3 FLOW OVERFLOWs (P1-headline 1916, P8-keys +28px, P7 col3 1848.5) — German strings run longer. build2 shortened 13 strings (P1 cifre → 2 lines each; P7 error notes → 1 line each; disclosure 6 → 3 lines; six P8 notes → 1-line answers) — zero overflow, but 1 occlusion flag: P8 match_set instr "Ordne die Wörter den Bedeutungen zu" (347.1px) grazed the model text 92.8×4.2px. build3 shortened the instr to "Wörter zuordnen" (153.0px) in content8.py only — but the same instr is used by THREE match_set calls (P2/P4/P8), so P4 still flagged (B2 chip 24.3×14.0px) + freeze unexplained on P2/P4. build4 fixed the other two call sites — then 1 flag: P4 E TU question 3 lines, third line inside the fixed results table (box bottom 1169 vs core/en 1140). build5 shortened the P4 E TU question to 2 lines ("Welches Spiel siehst du Sonntagabend? Schreib zwei Sätze auf Italienisch.", send-clause dropped as in en) — P4 col3 ends 1140.45, ALL PASS.
- Lessons for fr/es/pt/nl (long-word risk): measure any start-anchored cross-column string with the build's own `text_w`/`wrap` (match_set instr budget 254.5px at x+196; P4 E TU 2-line budget vs fixed table at y=1140; P8 RISPOSTE spare capacity only ~61px/4 columns); fix ALL call sites of a shared translations.py entry, not one. The fr/es/pt/nl match_set instr values in translations.py are long (fr "Associez les mots à leurs définitions" etc.) — measure before building, shorten pre-emptively if > 254.5px.
- Quota stops on this shift: NONE. Core-it untouched.
- NEXT: it-fr (build_edition.py fr), then es → pt → nl → ru → ja → ko → zh-tw.

## ✅ it-en COMPLETE (build4, 2026-11-11 ~01:50 UTC) — 1 of 10 done
- Print PDF `La-Lucerna-VOL4-EN.pdf` 14,032,990 bytes, sha256 `d41e7255d7da8ea63cf07560911a518b2e55a4a7d8a9eb8b0f3c1ae6d3129e2f`; web PDF `La-Lucerna-VOL4-EN-web.pdf` 1,259,104 bytes, sha256 `32a6727966cfa130618c64356cd9db9812f04cbc96e961ff1534b143580e5903`; `.text.md` 55,286 bytes / 1317 lines; ABSTRACT.txt (EN, one line, no ASCII quotes); WEEKLY-KIT.md written.
- Gates ALL PASS (`en/gates5.log`): occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff only 137–139 re-aimed); freeze diff fragments 0 unexplained (P1–7, real check — see below); freeze baseline direct sha256 8/8; strict-cjk added = 13 × U+3000 only; print/web multiset identical (7,945 words); web < 7 MB; P8 min font 13.0px = 9.75pt; §1.1 scans pass; VOL.5 only in the 3 legitimate nodes (same as core); textmd validate 0/0; keys 1–150 match core (except 137–139 + writing); notes match translations.py (except 137–140 + writing; 9 frozen notes — Italian verb paradigms 16–20/60–61 + arithmetic 85–86 — carried byte-identical, no CJK).
- P8 chip check: Q113–120, Q145–149, Q150 all carry B1 badges, matching core 1:1 (the earlier detector "MISSING" for Q150 was a bug — the RISPOSTE answer line overwrote the stem result; the stem badge is present in both core and en).
- Visual: 8/8 cards viewed, zero defects (P4 E TU 2 lines clear of the table; P7 disclosure ends 1673.0, clear of the FRASI hline; P3/P5 structural whitespace is the core pattern, left as-is).
- Self-read: full .text.md 1317 lines read; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent); no other-language residue; all 150 keys re-verified.
- Build4 fix (the last LINEX): the P7 LETTERE disclosure was shortened 4 wrapped lines → 3 ("Editor's sample, not a real letter. No real letters or best page-8 writing had arrived; the promise carries to VOL.5.", wrap-measured) after build3's error-note shortenings left col3 ending 1702.0 (one line more than estimated). Same wording synced to translations.py:986 + content7.py:100/106.
- gates.py fixes by this runner (scratch tool, NOT shared tools): p8 extract reads `noted_set`; p8 compare reads `status` + allows keydiff ⊆ {137,138,139}; "no VOL.5" is now furniture-scoped (preview header / disclosure / P2 cross-ref allowed — the core has the same 3 nodes); textmd-validate duplicate kwarg removed; freeze check now reads the real per-page `added_strings`/`removed_strings` (the old top-level `added` key does not exist in freeze.py's schema — the old check was VACUOUS) and explains every fragment against translations.py + generated furniture (NOTE/gloss composites, gloss + " (Pagina N)", page-line furniture; P8 skipped, covered by p8 compare + key audit); keys check skips the writing item; notes check compares against translations.py values with the frozen-paradigm/arithmetic exemption. Also fixed gates.py foot_re for ja (`\d+ ページ（全 8 ページ）`) and ko (`제 \d+ 면 / 총 8 면`) to match build_edition.py's PAGE_LINE.
- Quota stops on this shift: NONE after the 01:00 UTC stop — build3 (01:31) and build4 (01:38) both wrote fine. Probes at 01:30 UTC passed (hash-object + real file write); df 53G free.
- Core-it untouched (read-only source; git status shows core-it only as an untracked new directory, no modifications).

## ⛔ STOPPED AGAIN — Disk quota exceeded on write (2026-11-11 ~01:00 UTC)
Per the brief: on EPERM / Disk quota exceeded / ffmpeg failure, stop immediately,
write it at the top of the record, do not hammer retries.

- Failed operation: `run.py` (build3 rebuild of it-en) -> `content12.py` line 158,
  `svglib.py save()` -> `OSError: [Errno 122] Disk quota exceeded:
  '.../2026-w47-it-en/svg/p1-prima.svg'` (first SVG write of the rebuild).
- `df`: /home/hatch 150G total, 105G used, **45G free** (70%) — disk NOT full;
  Errno 122 is a quota limit, not free space. Same signature as the 00:42 UTC stop.
- No retry attempted. No further writes after this record entry except the
  single STATUS.md update itself.
- Damage check (read-only): all build2 outputs INTACT — svg/p1-prima.svg still
  130,726 bytes, mtime 00:34 UTC (the failed open("w") did not truncate it);
  all 8 SVGs + 8 cards + both PDFs + .text.md unchanged from build2.
- Fixes applied BEFORE the stop (all writes succeeded and grep-verified):
  1. translations.py (151,997 bytes, mtime 00:59:32 UTC): 4 en strings shortened —
     P4 E TU line -> "Which match will you watch on Sunday evening? Write two
     sentences in Italian."; P7 notes -> "La Lazio is singular, so is the verb." /
     "Use the subjunctive after è probabile che." / "Torrone is singular, so is
     the verb." (other "send them in" strings on other pages untouched).
  2. Edition content34.py (2 occurrences of the P4 line) + content7.py (3 P7 notes)
     patched identically; grep-verified.
  3. gates.py fixed: p8 paths now p8-valutazione.svg (edition + core); §1.1 scan
     loop now uses real SVG names p1-prima.svg ... p8-valutazione.svg; strict-cjk
     now passes when the only added CJK chars are U+3000 (furniture spaces).
- Write probes at start of this shift BOTH passed (git hash-object -w + real file
  write in the edition dir), so the quota hit mid-rebuild, not at open.
- State: en sources are patched but NOT rebuilt — on-disk PDFs/SVGs/.text.md are
  still build2 (pre-patch, with the 2 occlusion flags). Next runner: re-run
  `en/rebuild3.py en build3` (run/render/webpdf/.text.md export) once the quota
  clears, then gates + visual + self-read + 150-key audit + KIT. Nothing else
  half-written. de/fr/es/pt/nl/ru/ja/ko/zh-tw: NOT started.

## Progress — edition it-en (first of 10), NOT yet complete
- build_edition.py works end-to-end. en built (run.py rc 0, 150 exercises,
  by level A2 47 / B1 70 / B2 33; render rc 0; webpdf rc 0; .text.md exported,
  55,322 bytes after re-export).
- Print PDF: `La-Lucerna-VOL4-EN.pdf` 14,033,017 bytes (pre-patch build).
  Web PDF: `La-Lucerna-VOL4-EN-web.pdf` 1,259,129 bytes (< 7 MB).
- Build issue fixed: P1-headline FLOW OVERFLOW (ended 1916 vs bottom 1828).
  Cause: English bridge 3 lines + cifre box 3-line items. Fix applied at source:
  cifre items shortened (Lazio top with 29 points / 24 goals in 10 matches /
  over 150 performers in the parade) — box back to 470.42px = core height.
  Rebuild: P1-headline ends 1362 (same as core), zero overflow. Synced into
  translations.py (that write succeeded, 00:34).
- Gates run (gates.py, en/gates1.log): PASS freeze diff (0 added strings),
  PASS print/web text multiset identical (7,957 words each), PASS web < 7 MB,
  PASS print size. FAILs:
  1. occlusion_audit: 2 flags — [COVER] p4-sport "and send them in."
     (E TU box text covered 52% by results-table row rect at y1156);
     [LINEX] p7-lingua "letter. No real letters or best page-8"
     (disclosure line ink crossed by FRASI hline at y1686).
  2. p8 extract/compare: FAILED only because gates.py used wrong filenames
     (p8.svg vs actual p8-valutazione.svg) — gates.py bug, not an edition defect.
  3. freeze strict-cjk: 13 "added CJK" — all 13 are U+3000 ideographic space
     (the §1.1 full-width-space furniture separators), NOT real CJK text.
     Adjudicated: expected; gates.py must exempt U+3000.
- Fixes designed, measured, NOT yet applied (blocked by the quota stop):
  - P4: shorten en E TU line to "Which match will you watch on Sunday evening?
    Write two sentences in Italian." (measured 2 lines vs 3; col3 ends 1169.45
    -> ~1140.45, clearing the table rect at 1156).
  - P7: shorten three error notes to 1 line each — "La Lazio is singular, so
    is the verb." / "Use the subjunctive after è probabile che." /
    "Torrone is singular, so is the verb." (measured 1 line each; saves
    3 x 29.5 = 88.5px; col3 ends 1761 -> ~1672.5, clearing the 1686 hline).
  - gates.py fixes: use real SVG names (p1-prima.svg ... p8-valutazione.svg);
    strict-cjk must exempt U+3000.
- Still to do for en after the quota clears: apply the 4 string fixes
  (translations.py + content34.py + content7.py), rebuild run/render/webpdf,
  re-export .text.md, re-run gates, visual-check all 8 cards, full self-read,
  150-key verification, write en record + WEEKLY-KIT.md.
- Editions de/fr/es/pt/nl/ru/ja/ko/zh-tw: NOT started. Nothing built yet.
  Build tooling ready: scratch-fanout-it/build_edition.py, gates.py,
  validate_edition_textmd.py, translations.py (239 entries, 10 languages),
  cjk-inventory.json.

## Files
- Work record / scripts: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-it/`
- Edition dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-it-en/`
- Core (untouched): `~/workspace/weekly-git/production/2026-w47/core-it/`

## Mechanism fix — type '翻译' localized (2026-11-11, fix-export-it1)

- Precedent overturned: the header comment in translations.py ("Type '翻译'
  deliberately NOT in this table, W46 precedent: kept as-is") is dead.
  W47 it-en proof1 + it-es fix1 (commit 8f2bba56) established the label must
  read in the reader's language; a re-fan-out with the old table would have
  wiped the it-es hand-fix (and it-en's) back to 「翻译」.
- Fix (option i — table mapping, smallest change, covers all 10 editions):
  1. translations.py: added "翻译" -> en Translate / de Übersetzen /
     fr Traduire / es Traducir / pt Traduzir / nl Vertalen / ru Переведите /
     ja 翻訳 / ko 번역하기 / zh-tw 翻譯 (new entry after "写作"; header
     comment corrected). Table now 240 keys.
  2. build_edition.py: consumed["翻译"] = 4 (the E re-aim consumes the 4
     instr="翻译" occurrences; the 4 type args go through the table pass);
     residual-CJK gate for non-CJK readers tightened to zero-tolerance
     (the old "翻译" exemption removed — a surviving 「翻译」 now fails
     the build instead of passing silently).
  3. W46 exporter (production/2026-w46/core-it/finish/export_it_textmd.py)
     NOT changed: it prints typ verbatim, which is correct once the
     source carries the localized label. flow.ex never renders typ in
     the PDF (only in REG + run.py's by-type log), so the fix changes
     .text.md only; P8-keys loop (e_["type"] == writing type) untouched.
- Verification (harness in
  hidden_files/w47/scratch-fix-export-it1/harness.py, log harness.log):
  Phase 1 — real table pass from core-it, all 10 langs: "翻译" replaced
  exactly 4x, labels correct 4/4 per lang, count assertions green, zero
  residual CJK / zero residual table keys.
  Phase 2 — real W46 exporter over committed edition sources (control vs
  fixed): it-es fixed re-export is BYTE-IDENTICAL to fix1's hand-fixed
  text.md (56,267 B, SHA ebd13d45…5cabf); it-de / it-ru fixed re-exports
  differ from committed text.md by exactly the 4 E-label lines
  (969/971/973/975), controls byte-identical.
- Re-fan-out precondition: SATISFIED. Re-running build_edition.py now
  produces localized E labels in all 10 it editions.
- Known pre-existing drift (not this fix): all 10 committed edition
  content8.py files carry a post-fan-out proof patch at lines 80-82
  (deficit/copertura/scaglione notes) that core-it does NOT have, plus
  further proof patches in individual edition sources. A re-fan-out from
  core-it will NOT reproduce those patches — the coordinator must
  re-apply (or port to core-it) the post-fan-out proof patches before /
  alongside any re-fan-out. This fix does not touch that question.
- Files changed by this fix: translations.py, build_edition.py (this dir
  only). No commit, no push, no production file touched.

---

## Re-fan-out (2026-11-11, scratch-refanout-it/FANOUT-REPORT-it.md)
- Source: core-it fix3 commit 36bdec2e (re-proof (a) zero issues) + table fix (17 values, TABLE-FIX-LOG.md) + exporter 「翻譯」 fix (240-entry map) + the 1 real hand patch (it-nl masthead spacing 11.5 → 11.0, re-applied + re-rendered + measured: band left 10.5 / right 1873.7 on a 1950-wide page).
- Result: 10/10 editions rebuilt first attempt (build_edition.py RC=0 each), gates 10/10 ALL PASS (Latin/Cyrillic 20/20, CJK 19/19), freeze baselines re-taken 8/8, sim cross-check 0 unexpected changes, visual 8/8 per edition (10 contact sheets + 9 full-size key pages), 0 defects.
- The earlier coordination note ("re-fan-out will LOSE the content8.py:80–82 proof patch") is superseded: PATCH-INVENTORY.md §4 B-7–B-9 adjudicated those long glosses as PRE-fix3 wording; fix3 shortened them on purpose (P8 F matching options protruding into the column gap). The rebuild correctly carries the fix3 short forms.
- Backup: first-fan-out editions preserved SHA-verified at scratch-refanout-it/backup/ (430 files) until the new bundle is in the repo. First-fan-out baselines/logs preserved at scratch-refanout-it/prev-fanout/.
- No commit, no push. Only production/2026-w47/2026-w47-it-*/ and hidden_files/w47/ touched.

---

## Re-fan-out 2 (core D-2 fix) (2026-11-11, scratch-refanout-it2/FANOUT-REPORT-it2.md)
- Source: core-it D-2 fix (content7.py:17/:18 only; core re-proof (a) zero issues; core SHAs verified on disk before building: print e1f89922…, web 09f2ef66…, text 9eb9ee06…). Mechanism unchanged (build_edition.py, gates.py, translations.py 240×10); it-nl masthead spacing 11.5 → 11.0 re-applied + re-rendered + measured (band left 10.5 / right 1873.7, same as last round).
- Result: 10/10 rebuilt (batch 1 interrupted once by a runtime restart mid-de-webpdf; the partial de dir was deleted and rebuilt clean from the same mechanism), gates 10/10 ALL PASS (Latin/Cyrillic 20/20, CJK 19/19), D-2 checks 10/10 ALL PASS (incl. explicit PDF text-layer proof — the pure-Latin change is invisible to freeze/p8), freeze baselines re-taken 8/8, visual 80/80 pages on 10 contact sheets + 3 full-size crops, 0 defects. text.md −21 bytes on all 10 editions.
- Tracking item closed for this round: it-zh-tw P1 cifre title spare re-measured +1.0 px (PIL, identical to pre-refanout) / ink max x=959 at 96 dpi (same as before); still the tightest margin, still passing per the accepted precedent — re-measure again on the next re-fan-out.
- Corrections found this round: (1) check_refanout2.py — PDF text layer glues `→` to its neighbour word; D-2 L17 now counted arrow-normalised; difflib merges the two adjacent changed lines into one opcode; empty SVG text nodes no longer fail the node-diff guard. (2) update_kits2.py — "240 entries" occurs twice per KIT; strict-cjk regex had a double backslash (would have mislabelled all 7 Latin editions "n/a" — the same error the re-fan-out KITs carry in §8, now corrected in this round's §8: de/en ×13, es/fr/nl/pt/ru ×8); §7 text-line regex must consume to end-of-line + count=1 (es trailing old text SHA; de/en/ru §12 second deliverables block).
- Backup: pre-refanout editions preserved SHA-verified at scratch-refanout-it2/backup/ (430 files) until the new bundle is in the repo. Re-fan-out logs/baselines preserved at scratch-refanout-it2/prev-logs/.
- No commit, no push. Only production/2026-w47/2026-w47-it-*/ and hidden_files/w47/ touched.
