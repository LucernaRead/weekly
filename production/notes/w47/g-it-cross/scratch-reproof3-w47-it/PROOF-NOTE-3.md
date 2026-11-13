# PROOF-NOTE-3 — W47 Italian family, third-round independent reproof

- **Proofreader:** third-round independent (distinct from builder, round-1 proofreader/fixer, round-2 proofreader/fixer)
- **Date:** 2026-11-12
- **Scope:** `production/2026-w47/` Italian family only — 11 editions: `core-it` (= it-zh-cn) + `2026-w47-it-{en,de,fr,es,pt,nl,ru,ja,ko,zh-tw}`
- **Disk gate:** `df` 95G used / 150G total at start and at end (64%) — under the 100G gate, work proceeded.
- **Method:** read-only on production files; `run.py` re-run in scratch copies; gates via `gates3.sh` (copied from round-2 `gates2.sh`, only the scratch path changed); tools interpreter `tools/venv/bin/python` throughout.
- **Sources read in full:** `SOP.md` (§8/§8.4), `scratch-reproof2-w47-it/PROOF-NOTE-2.md`, `scratch-fix2-w47-it/FIX-LOG-2.md`, `scratch-fix-it/FIX-LOG.md`.

## Overall conclusion — (a) CLEAN

**Zero findings. MAJOR 0, MEDIUM 0, low 0. This is a zero-problem round.**

- R2-1 and R2-2 both verified in place (§2).
- Full re-read of it-en text.md (1317 lines) + `>`-line-by-`>`-line diffs of the other 10 editions + programmatic cross-edition checks: no content error (§3).
- Mechanical gates: **11/11 ALL-GREEN** — run.py TOTAL 150 / 0 FLOW OVERFLOW / 0 HEAD TOO WIDE, occlusion 0 flags, p8 extract 150/150, p8 compare CLEAN, D5 census clean, boxtitle 0 DEFECT, spill 0 SPILL, edge 0 TOUCH / 0 NEAR, print/web text layers identical (nonws diff 0) (§4).
- Round-1 fixes F-1–F-5, core-1, Q136, R-1 all still in place (§5).
- Four external facts re-checked against live sources 2026-11-12, all consistent with the paper (§6).
- Visual spot check of the two re-rendered print PDFs (core-it, it-zh-tw: P1, P4, P8): clean, no overflow/overlap/clipping (§7).

No finding table — there is nothing to record. Checked-and-excluded items are listed in §8 (not findings).

## Per-edition conclusions

| Edition | Conclusion |
|---|---|
| core-it (it-zh-cn) | Clean. R2-1/R2-2 in place; gates ALL-GREEN. |
| it-en | Clean. Full re-read, 150/150 exercises + answers verified; gates ALL-GREEN. |
| it-de | Clean. Diff read in full; gates ALL-GREEN. |
| it-fr | Clean. `6–8 novembre` untouched (correct French); diff read in full; gates ALL-GREEN. |
| it-es | Clean. Diff read in full; gates ALL-GREEN. |
| it-pt | Clean. Diff read in full; gates ALL-GREEN. |
| it-nl | Clean. Diff read in full; gates ALL-GREEN. |
| it-ru | Clean. Content proofread normally; gates ALL-GREEN (D5 census `noto_sans_elements=777` is the known cross-family systemic issue, not re-reported). |
| it-ja | Clean. Targeted gloss/quote checks correct; gates ALL-GREEN (P8-keys 2561 is the known flow-cursor artifact, see §4). |
| it-ko | Clean. Targeted gloss/quote checks correct; gates ALL-GREEN (text-layer diff 1 = whitespace only, nonws 0 — adjudicated item, not re-reported). |
| it-zh-tw | Clean. R2-1/R2-2 in place; diff read in full; gates ALL-GREEN. |

## 1. File fingerprints (verified 33/33)

All 11 editions match FIX-LOG-2 (core-it, it-zh-tw) / PROOF-NOTE-2 (other 9). Print PDFs are `La-Lucerna-VOL4.pdf` (core-it) / `La-Lucerna-VOL4-<LANG>.pdf`; web PDFs add `-web` before `.pdf`.

| Edition | Print PDF bytes / SHA-256 (first 12) | Web PDF bytes / SHA-256 (first 12) | text.md bytes / SHA-256 (first 12) |
|---|---|---|---|
| core-it | 14,839,776 / `7b3034a08180` | 1,546,116 / `393e65473a1c` | 52,677 / `24b37ae72af3` |
| it-en | 13,496,925 / `aeae0796361c` | 1,215,698 / `e071a54f8f30` | 55,126 / `a4d863d96180` |
| it-de | 13,499,265 / `8cf7241a5d60` | 1,218,051 / `13414d0fbe1b` | 56,634 / `27f58fca0f39` |
| it-fr | 13,497,005 / `ffb20e7b9620` | 1,215,747 / `d08db2eb54b2` | 56,524 / `b4d1ec47ff3a` |
| it-es | 13,497,563 / `4393ba30bd49` | 1,216,301 / `c40c7a0067bd` | 56,214 / `e19cf39d5ef6` |
| it-pt | 13,500,238 / `c4d4fe0f005e` | 1,218,997 / `a6e7e8365466` | 55,736 / `03cc7389d3ed` |
| it-nl | 13,495,268 / `b5a24a8f4234` | 1,213,994 / `8fc2d76c044a` | 55,535 / `92ddd5838d6f` |
| it-ru | 13,752,697 / `af296c0525ea` | 1,465,756 / `597e400ffcec` | 67,681 / `298c2cd79bb8` |
| it-ja | 21,050,187 / `38a236a3d0ca` | 1,697,338 / `e035db45098e` | 58,209 / `3dafa38c8b40` |
| it-ko | 15,803,899 / `66dffb4ebd5c` | 1,484,256 / `7419a5a624e5` | 57,349 / `c37668224de7` |
| it-zh-tw | 14,907,346 / `3cf43a808c2a` | 1,640,999 / `133b04d123f1` | 52,588 / `1ae5edf7b167` |

## 2. R2-1 / R2-2 verification — both IN PLACE

### R2-1 — P4 results title localised (core-it, it-zh-tw)

- core-it + it-zh-tw text.md L445 now read `I RISULTATI DELL'11ª GIORNATA　第 11 轮赛果（11月6–8日）` / `第 11 輪賽果（11月6–8日）`.
- `novembre）` count = 0 in both text.md files.
- Print-PDF text layer contains `11月6–8日` (core-it line 965, zh-tw line 960).
- it-fr text.md still has `6–8 novembre` in exactly 1 place — correct French, untouched as required.

### R2-2 — matching-exercise notes use spaced ` = ` (core-it, it-zh-tw)

- Spaceless `=` pairs (regex `[a-zà-ÿ]+=[^]`) = 0 in both editions.
- The 24 match-set lines (L285/287/289/291, L499/501/503/505, L981/983/985/987 + answers L1067/1069/1071/1073, L1121/1123/1125/1127, L1299/1301/1303/1305) all contain ` = ` in both editions — 24/24 each.
- Per-word spaced counts: 12 words ×2, plus pre-existing extras also in spaced form (vetta ×3 incl. vocab line L855 `vetta = 榜首。`; manovra/deficit/copertura/scaglione ×4 each incl. fill-in Q97–100) — consistent with FIX-LOG-2 §4. `votivo=还愿桥` does not exist as a standalone string (`votivo` occurs only inside `ponte votivo=`); 12 groups is correct.

## 3. Full re-read (content)

- **it-en text.md read in full, 1317 lines.** Italian body, all 150 exercises and 150 answers checked one by one against stems/article/charts; all consistent. Verified: dates/weekdays (Nov 16 Mon, Nov 21 Sat, Nov 22 Sun, Nov 12 Thu, Nov 15 Sun, Nov 6 Fri, Nov 7 Sat, Nov 8 Sun, Nov 23 Mon — all consistent with the week of Mon 2026-11-09); P4 results table sums to 24 goals in 10 matches (3+1+2+3+3+2+3+1+2+4); Q85 13−11=2, Q86 6+7=13; P7 eight quotes verbatim vs P1–P6; Q44/Q134/Q136 notes complete (subject+verb+place+date); model text 99 words (round-2 script check); contents page numbers match sections.
- **Diffs vs it-en read `>`-line by `>`-line in full** (`diffs/diff-<edition>.txt`; changed-line counts: core-it 802, de 796, fr 794, es 796, pt 800, nl 794, ru 802, ja 802, ko 802, zh-tw 802): core-it (401 `>` lines), it-de (398), it-fr (397), it-es (398), it-pt (400), it-nl (397), it-zh-tw (401) — all correct native-language glosses, numbers, dates, names. it-ja / it-ko / it-ru: targeted checks (match glosses Q25–28/52–55/141–144, Q133–140, NOTE lines, P7 quote translations, answer notes) — all correct (e.g. ja salute=健康, ponte votivo=奉納の橋; ko 서원의 다리, 건강; ru обетный мост, здоровье).
- **Programmatic cross-edition checks** (all 11 text.md): 150/150 exercises and 150/150 answers each; exercise key-token diffs vs it-en only [137,138,139] (translation answers in reader language — expected design) + [150] (model-text pointer wording; nl lacks [150] because its Q150 key matches en); answer-key diffs identical set [137,138,139,150]. Italian stems byte-identical after stripping bracket type labels; residual stem diffs explained (weekly-plan list items 1–5 parenthetical translations, match-word glosses, Q140 prompt given in reader language). Number mismatches across diffs all explained by locale conventions (CJK `11月21日` adds month 11; `17:00`→`17 Uhr`/`17h`/`17点`; `1,360`→`1.360`/`1 360`/`1360`; `+0.8%`→`+0,8%`; spelled-out numbers in fr/es/pt/nl/ru quote translations; `Read page 1` → `Lis la une` etc.).
- **Quote census:** ASCII `"` = 0 in all 11 text.md (earlier 68–150 counts were apostrophes in Italian elisions); curly quotes balanced everywhere (en/de/ja/ko/core/zh-tw “ ” 3/3; de also „ 3; fr/es/pt «» 55/55; ru «» 126/126; nl “ ” 1/1, «» 54/54); U+FFFD = 0 in all 11.
- **ABSTRACT.txt:** all 11 read — reader-native, VOL.4, A2–B2, 150 exercises, real topics (Lazio 29 pts, Torrone/Eurochocolate Sunday close, Salute/Tree Day, BookCity/TFF, budget bill); no "learn X by reading news" phrasing. core-it abstract contains `意大利语正文与简体中文讲解，A2–B2` (core-1 verified).

## 4. Mechanical gates — 11/11 ALL-GREEN

run.py re-run in scratch copies (`runs/<slug>/`, logs `logs/run-<slug>.log`); gates via `gates3.sh` (logs `logs/gates-<slug>-*.log`, JSON `gates/<slug>/`).

| Edition | run.py TOTAL / FLOW OVERFLOW / HEAD TOO WIDE | P8-keys end (bottom 2552) | occlusion | p8 extract / compare | D5 census | boxtitle | spill | edge | textlayer print/web |
|---|---|---|---|---|---|---|---|---|---|
| core-it | 150 / 0 / 0 | 2499 | 0 flags | 150/150, self (skip) | latin 0, cyr 0, curly 4/4 Newsreader, noto 0 | 24 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 38091/38091, diff 0, nonws 0 |
| it-en | 150 / 0 / 0 | 2514 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 4/4, noto 0 | 18 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 43831/43831, diff 0, nonws 0 |
| it-de | 150 / 0 / 0 | 2514 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 2/2, noto 0 | 22 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 44743/44743, diff 0, nonws 0 |
| it-fr | 150 / 0 / 0 | 2529 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 0, noto 0 | 20 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 44641/44641, diff 0, nonws 0 |
| it-es | 150 / 0 / 0 | 2543 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 0, noto 0 | 20 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 44590/44590, diff 0, nonws 0 |
| it-pt | 150 / 0 / 0 | 2543 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 0, noto 0 | 22 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 44217/44217, diff 0, nonws 0 |
| it-nl | 150 / 0 / 0 | 2543 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 2/2, noto 0 | 22 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 44674/44674, diff 0, nonws 0 |
| it-ru | 150 / 0 / 0 | 2543 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 0, noto 777* | 26 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 44243/44243, diff 0, nonws 0 |
| it-ja | 150 / 0 / 0 | 2561† | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 0, noto 0 | 24 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 38957/38957, diff 0, nonws 0 |
| it-ko | 150 / 0 / 0 | 2546 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 4/4, noto 0 | 36 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 39407/39406, diff 1, nonws 0‡ |
| it-zh-tw | 150 / 0 / 0 | 2499 | 0 flags | 150 noted, CLEAN, keydiff [137,138,139] | latin 0, cyr 0, curly 4/4, noto 0 | 24 titles, 0 DEFECT | 0 SPILL | 0 TOUCH / 0 NEAR | 37930/37930, diff 0, nonws 0 |

\* it-ru `noto_sans_elements=777` is the known cross-family D5 systemic issue (Latin titles rendered in Noto Sans); separate worker is fixing svglib.py. Per task instruction, not re-reported as a finding. Content proofread normally.
† it-ja P8-keys 2561 is the known flow-cursor artifact from round 2 (no FLOW OVERFLOW warning; round 2 physically verified the PDF: last answer baseline y=1908.9pt vs footer 1968pt, 59pt gap, complete). it-ja was not re-rendered; the value is unchanged. No action.
‡ it-ko text-layer diff 1 is whitespace-only (nonws_diff=0) — the FIX-LOG adjudicated 1-whitespace-char print/web difference. Not re-reported.

All p8 compares: `missing=[] extra_count=0 uncertain=[]`; keydiff `[137,138,139]` is the expected translation-answer keys (Q137–139 model translations in reader language). All boxtitle checks 0 DEFECT / 0 OBSERVE / 0 marginal. All edge scans: 8 pages, P8 min distance ≥53.6pt from every edge.

## 5. Round-1 fixes re-verified still in place

- **F-1** (5 shortened reader subtitles): en `EVERY WEEK IN ITALIAN`, fr `CHAQUE SEMAINE EN ITALIEN`, pt `TODA SEMANA EM ITALIANO`, nl `ELKE WEEK IN HET ITALIAANS`, ru `КАЖДУЮ НЕДЕЛЮ ПО-ИТАЛЬЯНСКИ` — all present.
- **F-2** (P6 timeline MAR row): `NOV. Scade` present in print-PDF text layer of core-it, it-en, it-ru (1 each).
- **F-3** (7 full-width colons → half-width): template-string scan = 0 in all 11 editions.
- **F-4** (P2 box title back to "remember" class): `LA FRASE PER RICORDARE` + reader gloss present in all 11 (es `RECORDAR` is the D5-shortened form, accepted).
- **F-5** (Q44/Q134 notes completed): all 11 editions carry subject+verb+place+date notes on Q44 and Q134.
- **core-1** (footer + abstract): print-PDF footer `La Lucerna 意大利语周报 VOL.4 正文意大利语 讲解简体中文`; abstract carries `意大利语正文与简体中文讲解，A2–B2`.
- **Q136 completion:** nl and ru Q136 carry the place note (`Onderwerp + werkwoord + plaats` / `Подлежащее + глагол + место`).
- **R-1** (ru P8-keys overflow compensation): ru P8-keys end 2543 ≤ 2552.

## 6. External facts — re-checked 2026-11-12, all consistent

- **BookCity Milano 2026:** 15th edition, 23–29 Nov, theme `Il senno sulla Luna` (Ariosto-inspired) — IULM/Hostelworld confirm dates and theme.
- **Festa del Torrone, Cremona:** 29th edition, 7–22 Nov (16 days, three weekends), theme `Il Confine – Dove gli opposti si incontrano`; 1441 Sforza–Visconti wedding re-enactment, Sun 22 Nov; Torrone d'Oro to Davide Simonetta on 22 Nov; 150+ figuranti — multiple sources confirm.
- **Eurochocolate, Perugia:** 32nd edition, 13–22 Nov, theme `Fate Dolci`; Calabria guest region; `I tesori della Calabria Straordinaria` Fri 20 Nov 18:15; Iginio Massari closing Sun 22 Nov — eurochocolate.net / tagumbria confirm.
- **Torino Film Festival:** 44th edition, 24 Nov–2 Dec (9 days), 120 titles, opening `November 1963` (Roland Joffé) — FilmFreeway / Cineuropa / FRED confirm.

## 7. Visual spot check (two re-rendered print PDFs)

Rendered P1, P4, P8 of core-it and it-zh-tw print PDFs at 60 dpi (`pages/`):

- core-it P1: masthead `VOL.4 LA SERIE A · IL TORRONE · VENEZIA`, `SETTIMANA DAL 16 AL 22 NOVEMBRE 2026`, contents, QUIZ LAMPO — clean.
- core-it P4: R2-1 title `I RISULTATI DELL'11ª GIORNATA 第 11 轮赛果（11月6–8日）` in place; results table complete; footer `La Lucerna 意大利语周报 VOL.4 正文意大利语 讲解简体中文` — clean.
- core-it P8: exercises 113–150 + RISPOSTE key 1–150 complete, no clipping; footer intact — clean.
- it-zh-tw P4: title `第 11 輪賽果（11月6–8日）` in place; footer `La Lucerna 意大利語週報 VOL.4 正文意大利語 講解繁體中文` — clean.

No overflow, overlap, or clipping observed in any of the six pages.

## 8. Items checked and excluded (NOT findings)

- `���` appearing in my own awk-pipeline output at core-it `>` line 215 and zh-tw line 297: verified by direct `grep`/`cat -A` to be a display artifact — files contain correct `政府批准不等于已经是法律。` / `複數 sono andati`; source `content7.py:121` and PDF text layer agree. U+FFFD = 0 everywhere.
- Letters note drops "page-8" (e.g. de `Keine echten Briefe oder besten Aufsätze`, fr `ni de meilleure rédaction`) in all non-en editions — paraphrase of an editorial meta-note, same class passed by rounds 1–2.
- es/pt P8 section-A type label `[B1 · Cloze]`, nl `[B1 · Cloze-keuze]` — shared template loanword, not an error.
- fr `Cette sem.`, pt `Esta sem.` abbreviations; P8 header `La grande prova della settimana + tutte le risposte` untranslated in all 11 (template style, round-2 excluded).
- Q146 answer note drops "(plural)"/"（复数）" in fr/es/pt (Q37 keeps it) — gloss itself correct.
- NOTE gloss `il protagonista` = 主角 (core-it/zh-tw) vs Q70 note 嘉宾 — both valid senses; en NOTE gives "protagonist / guest".
- Simplified/traditional leakage scan: zh-tw has no simplified-only chars, core-it no traditional-only chars (the character 文 appears in both scripts legitimately).
- es Q55 absent from diff because `debutto = debut, a` is byte-identical to en (round-2 noted: `debut` is an accepted Spanish loanword).

## 9. Not re-reported (per task)

FIX-LOG adjudicated items (it-de P1 gap 5.0pt, it-zh-tw cifre title margin +0.5px, it-ko print/web 1 whitespace-char diff), round-1/round-2 accepted residuals, and the it-ru Latin-title font issue (known cross-family D5 systemic issue, separate worker fixing svglib.py).

## Work products

- This note: `scratch-reproof3-w47-it/PROOF-NOTE-3.md`
- Diffs: `scratch-reproof3-w47-it/diffs/diff-<edition>.txt` (10 files)
- run.py logs: `scratch-reproof3-w47-it/logs/run-<slug>.log` (11)
- Gate logs: `scratch-reproof3-w47-it/logs/gates-<slug>-*.log`; gate JSON: `scratch-reproof3-w47-it/gates/<slug>/`
- Gate script: `scratch-reproof3-w47-it/gates3.sh`
- Visual spot-check renders: `scratch-reproof3-w47-it/pages/` (core-p1/p4/p8, tw-p1/p4/p8)
- Scratch run copies: `scratch-reproof3-w47-it/runs/<slug>/`

## Round verdict

**(a) CLEAN — zero-problem round. MAJOR 0, MEDIUM 0, low 0.** R2-1 and R2-2 verified in place; all 11 editions gate ALL-GREEN. Per SOP §8.4 proofread-until-zero, the it family has completed a zero-finding round.
