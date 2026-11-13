# FANOUT-REPORT-ru — W47 Russian core → 10 reader editions (2026-11-10/11)

Fan-out builder (leaf). Core verified: print `Lucerna-VOL4.pdf` 31,429,156 bytes SHA `4b56429722dbbf4573eb80bf24a7d4ae8daf6a7217fd01537c26801fc4411868`; web 3,992,881 bytes SHA `8a2649263171727ecfb2118e3f85bc1ddfc8a0c1f23730e66652ba78e358fca7`; text.md 54,801 bytes. Mechanism: `tm_ru2.py` (role-aware TM from W46, 0 conflicts all langs), `apply_ru.py`, `build_map.py`, `s11_check.py`, `adjudicate_en.py` (+unicode-escape fix, reusable pattern). Per-edition records in `scratch-fanout-ru/<lang>/RECORD.md`; KIT in each edition dir.

## en — DONE, zero issues
- Print `Lucerna-VOL4-ru-en.pdf` 21,245,420 bytes, SHA `023d9fd12bdca276751400fb13f7f399d645c267a09ba1897eb0e598d52f2e3a`
- Web `Lucerna-VOL4-ru-en-web.pdf` 3,341,934 bytes, SHA `fab0fc44736ecb169a1cc3932a8e85db2504f694f02e84d45f3063435327493d`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR; freeze direct sha256 8/8; print/web multiset identical (30,293 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 2 = final (build 1 fixed 3 defects: P1 LINEX, P7 LINEX, key-137 parse artifact).
- Verdict: **zero issues, ready for independent proofread.**

## de — DONE, zero issues
- Print `Lucerna-VOL4-ru-de.pdf` 21,226,139 bytes, SHA `31fab92b7b1b392f9bb3a80acf449af239e948c55584581f96428c15a1248521`
- Web `Lucerna-VOL4-ru-de-web.pdf` 3,347,223 bytes, SHA `1a67d6b46352c3ae7bc039832bca0302399254f4e410dd268c43e98065296da7`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (30,938 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Single build (pre-build width fixes: P1 gloss, P7 word gloss, A-bridges, key-137 em-dash).
- Verdict: **zero issues, ready for independent proofread.**

## fr — DONE, zero issues
- Print `Lucerna-VOL4-ru-fr.pdf` 21,260,891 bytes, SHA `b9476fc2d49584d134e61d59f587bd24e76f4da0caf66de03884ba86523f3629`
- Web `Lucerna-VOL4-ru-fr-web.pdf` 3,346,639 bytes, SHA `78a56be6b7094ce1e9dd2435f174e4e8bb563e6c7363b2a2f82815dfd17128fe`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (30,708 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 2 = final (build 1 fixed 2 real defects: P1 head/chip 0 px contact → `EN CHIFFRES`; curly ’ full-width rendering → straight ' in 52 map values; pre-build fixes: P1 gloss, err1/err2, word gloss, A-bridges, key-137 comma).
- Verdict: **zero issues, ready for independent proofread.**
- Lessons written to `LESSONS-fr.md` (straight apostrophes for all Latin langs; P1 head width ≤975 vs Q6 chip at x=989; map has no `note` bucket).
## es — DONE, zero issues
- Print `Lucerna-VOL4-ru-es.pdf` 21,272,810 bytes, SHA `acef924f8742bc78726e73ca84c30ff9097ca4e8b99d1a9715bb834e92a89293`
- Web `Lucerna-VOL4-ru-es-web.pdf` 3,348,591 bytes, SHA `788411a8c3aadd54e64088022d41680b90b8c15762773c594775f3c76d9bee90`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (30,774 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 2 = final (build 1 fixed 1 defect: P7 clinic note `на + preposicional…` 385.4 px wrapped to 2 lines → `на + prepos.:` 330.0 px, 1 line; pre-build fixes: P1 gloss, errs, word gloss, A-bridges, key-137 comma, head `EN CIFRAS` ends x=849.2).
- Verdict: **zero issues, ready for independent proofread.**
## it — DONE, zero issues
- Print `Lucerna-VOL4-ru-it.pdf` 21,260,017 bytes, SHA `a3e17e19cca04a961963feea38afd63e001b27b3cea5fa872ae6f74890e87575`
- Web `Lucerna-VOL4-ru-it-web.pdf` 3,345,188 bytes, SHA `04fa800929cbf87e65a7e16b658f296c4939ba18ebbfdd7b149296ed4e501912`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (30,862 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 2 = final (build 1 fixed 1 defect: P2 gloss `поздравить congratularsi` → `fare gli auguri`, matching P8 key 130; 14 TM curly apostrophes → straight ' at map level; Ded Moroz rendered `Nonno Gelo` (fr-parallel: Père Gel); pre-build fixes: P1 gloss, errs, `на + prepos.:` abbreviation, A-bridges 421.2 px, head `IN CIFRE` ends x=827.8).
- Verdict: **zero issues, ready for independent proofread.**
## pt — DONE, zero issues
- Print `Lucerna-VOL4-ru-pt.pdf` 21,199,772 bytes, SHA `e6171dabf8d871619b75a45c691ffbf41cd994bf1ef597ad6907294b6f26ff88`
- Web `Lucerna-VOL4-ru-pt-web.pdf` 3,344,677 bytes, SHA `cc8fea68fcf0c8292cae4f73ee0ed23c2facacae1d34e77f9fdd1b2d995323ce`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (31,041 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 2 = final (build 1 fixed 1 defect: P3 gloss `криминальная criminal policial` → `policial`, matching es `policíaca`; Ded Moroz rendered `Avô Gelo`; pre-build fixes: P1 gloss, errs, `на + prepos.:` abbreviation, A-bridges 398.4 px, head `EM NÚMEROS` ends x=886.8).
- Verdict: **zero issues, ready for independent proofread.**
## nl — DONE, zero issues
- Print `Lucerna-VOL4-ru-nl.pdf` 21,285,839 bytes, SHA `59d16202fb04c4b912c6cb65c69052d160fee0d7e7a228d5a53d015ed8fa4352`
- Web `Lucerna-VOL4-ru-nl-web.pdf` 3,348,435 bytes, SHA `1c860fc77a9a1b2ad313bf6fdd846170fbf0850942595bfe6aaf19196a504b4c`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (31,014 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 2 = final (build 1 fixed 1 defect: P3 gloss `криминальная misdaad- · сказочное sprookjes-` → `crimineel · sprookjesachtig`, full Dutch adjectives; 4 TM curly apostrophes replaced at map level; Ded Moroz rendered `Grootvader Vorst`; pre-build fixes: P1 gloss, errs, `на + voorz.:` abbreviation, A-bridges 395.7 px, head `IN CIJFERS` ends x=854.9).
- Verdict: **zero issues, ready for independent proofread.**
## ja — DONE, zero issues
- Print `Lucerna-VOL4-ru-ja.pdf` 27,404,856 bytes, SHA `929a5c4786f256cb194cdab9cd7aafd0db1b8331e73ed8b0d1c1dcaf44b2a06e`
- Web `Lucerna-VOL4-ru-ja-web.pdf` 3,683,942 bytes, SHA `fbfb35d3d34e7e196c43254db3995e78d84224f5da79fdeeb48fff7a0436d233`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (26,540 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 3 = final (build 1 fixed 4 defects: P6 double `解説 — 解説 —` prefix — W46 TM bug, strip the baked-in prefix from gloss values; P7 B2 bridge `解説 —` prefix inconsistent with A2/B1 — stripped, then re-shortened to `予報士が約束する；по данным により；может быть たぶん。` (L1 395.0 / L2 401.7 px vs 422.5 px) after the first shortening left a dangling `；` + lone `ん。`; P2 dangling 。 `成功を` → `成功`; P4 dangling 。 `空所を埋める` → `埋める`; Ded Moroz rendered `ジェド・マロース`; P1 gloss shortened to `ブラックフライデー。` 359.1 px, head `数字で見る今節` ends x=892.8).
- Build incident: build-2 render's pypdf merge duplicated CJK font subsets → 72.5 MB print PDF (6,485 font refs vs normal 71); per-page output was normal, isolated re-merge gave 27,405,262 bytes / 71 fonts, re-ran render.py → clean 27,404,856 bytes / 71 fonts; the 72 MB file was discarded, never gated or delivered. Lesson: check print-PDF bytes (~27 MB CJK / ~21 MB Latin) and font-xref count (~71) after every render before gating.
- Verdict: **zero issues, ready for independent proofread.**
## ko — DONE, zero issues
- Print `Lucerna-VOL4-ru-ko.pdf` 22,002,774 bytes, SHA `4e450e65c7c5dfb5b2574a5400ccd98be5f687c2e2341d44a95b312134055ca0`
- Web `Lucerna-VOL4-ru-ko-web.pdf` 3,474,892 bytes, SHA `797af4e6e622d16a04577ae25b4ddea8e21c7dc668a56e172d945c06350984f0`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (26,441 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; Morozko image skipped by design. Build 2 = final (build 1 fixed 4 defects: 3 mid-word Korean syllable splits from CJK character-greedy wrapping — P4 gloss `강등권` / `에.`, P5 gloss `입어` / `보기.`, P7 B2 bridge `약속한` / `다;` — fixed by shortening `동점을 만들다` → `동점`, `달력상의 날짜 · подошёл 잘 맞았다` → `달력 날짜 · подошёл 맞음`, `기상 예보관들이 … ～에 따르면` → `예보관들이 … 에 따르면` (space-preferring wrap simulator, validated against all three build-1 breaks, confirms clean word-boundary breaks); P2 band `2면 연습` → `2면 연습 문제` for consistency with P3–P6 TM values. Deliberate overrides: `목… = 진눈깨비` (not TM `젖은 눈`, one gloss per word per issue); TM accepted for `гололедица` → `노면 결빙` and `답은 8면…`. Ded Moroz rendered `데드 모로즈`; no double `해설 —` prefix risk (verified); head `숫자로 보는 라운드` ends x=913.9).
- Verdict: **zero issues, ready for independent proofread.**
## zh-tw — DONE, zero issues
- Print `Lucerna-VOL4-ru-zh-tw.pdf` 24,785,168 bytes, SHA `69239a09d74a478e975893b8ee7866facd8ed16fb8bcfe7b14f78307b03469d7`
- Web `Lucerna-VOL4-ru-zh-tw-web.pdf` 3,963,820 bytes, SHA `543ce70dd628ee47313da3ffe667f2ef40df44841b299095a40bb9774200bfbd`
- Gates: run exit 0 / 150 / 0 overflow; p8 150/150 CLEAN (keydiff 137–140 only); occlusion 42 TEXTX 0 LINEX, adjudicated 42/42 CLEAR (shared adjudicate_ru.py); freeze direct sha256 8/8; print/web multiset identical (25,752 chars); P8 min 9.75 pt; §1.1 all pass; 8/8 cards read; 150-question recheck 0 issues; chips A 113–120 / G 145–149 / H all present; **Morozko image PRESENT by design** (keys end col 3 y=2173.2, core condition fires — the only fan-out where it appears). Build 1 = final, 0 defects in the visual check. Pre-build: P7 word gloss `要計劃，不要著急。` → `要計劃，別急。` (was 1 line + lone `急。`, 0.6 px over; now 1 line); 4 deliberate overrides — strip W46-baked `講解｜` from P6 gloss + P7 B2 bridge (else `譯注｜講解｜…` double prefix), and correct W46 TM's Simplified `范文` → Traditional `範文` in 2 places; 7 dead W46-only overrides removed (only 2 of 9 `講解｜` TM values exist in W47). Simplified sweep of applied sources + .text.md: 0 hits except `干` in `塔什干` (transliteration). Ded Moroz = 嚴寒老人; `ледяной дождь` = 凍雨, `мокрый снег` = 濕雪; head `數字看本輪` ends ≈x865.
- Tool fix: `s11_check.py` lang parsing cut `zh-tw` to `tw`, misfiring the Latin-reader CJK check; fixed to detect the `-zh-tw` suffix.
- Verdict: **zero issues, ready for independent proofread.**

## Status: 10/10 DONE — all editions self-checked to zero issues, ready for the coordinator's independent proofread.
