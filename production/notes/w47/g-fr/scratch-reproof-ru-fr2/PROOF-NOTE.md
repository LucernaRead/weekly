# PROOF NOTE — 2026-w47-ru-fr (independent re-proof, Round 2 of the Fix-2 files)

- **Edition:** 2026-w47-ru-fr (Russian text, French explanations, VOL.4)
- **Proofer:** independent (did not build or fix this edition)
- **Date:** 2026-11-11
- **Verdict: (a) — ZERO FINDINGS.** Both round-1 findings are verified fixed; the full
  re-read found no new content, factual, or key error. (Word-spacing observations
  are recorded factually in §5 per the brief — out of scope, not findings, and they
  do not change this verdict.)

## SHAs (start = end; nothing changed mid-read)

| File | SHA-256 | Bytes |
|---|---|---|
| `2026-w47-ru-fr.text.md` | `e4cc50fd4195ed1adb7051c684c894c5a3b3091aa643cf3bab96690178e22a46` | 63,361 |
| `Lucerna-VOL4-ru-fr.pdf` (print) | `cdde6a829ba09283d7f815c960570cd1aec0771a41b3f03bead08cb47d530f79` | 21,291,969 |
| `Lucerna-VOL4-ru-fr-web.pdf` (web) | `7a3af1e2de8b57517e9c2e7b4933e35495107f5e2c4a9b72dfcefdb5fc0e79c5` | 3,385,807 |

- All three SHAs match the expected values in the brief exactly, at start AND end
  of the read. text.md is 836 lines.
- KIT §5 now carries these same three SHAs — the round-1 web-SHA drift
  (`45f6401d…` vs on-disk `0c708aa1…`) is resolved by the Fix-2 rebuild + KIT update.

## 1. F-1 — "Selon la météo" — VERIFIED FIXED

- text.md L616 (exercise key) and L812 (appendix), both exactly:
  `126. B — Selon la météo : pluie et neige mouillée`
- Print P8 answer key (pdftotext raw + layout, and the 100-dpi render): the same
  line, key 126, in the "— СТРАНИЦА 8 —" group. Web PDF: identical (text layer
  byte-identical to print, §4; web P8 render pixel-identical to print P8).
- `content8.py:43` carries the fixed note; P8 SVG (`svg/p8-test.svg`) contains
  "Selon la météo" ×1.
- "Selon les météo" = 0 and "les météo :" = 0 in text.md, print text, web text.
  The only "les météo" substring hits (3, all in text.md L538/L540/L793) are
  "les météorologues" — correct plural, not flagged.
- Answer letter B and the Russian stem are unchanged and correct.

## 2. F-2 — dangling Morozko caption — VERIFIED FIXED

- "Морозко" = 0 in text.md, 0 in print text, 0 in web text, 0 in all 8 SVGs
  (`grep -r` over `svg/`).
- text.md is now 836 lines / 276 paragraph blocks (was 838 / 277): exactly the
  L837–838 blank + caption lines removed, nothing else. The diff discipline in
  KIT §7 Fix 2 (L616 + L812 wording change, caption lines removed, L836
  unchanged) is consistent with what is on disk.
- P8 render: no Morozko image, no caption; keys end col 3 with clean empty space
  below — image still skipped by design (keys end col 3), same as W46 ru-fr.
- `content8.py:136` is now module-qualified `bslib4.caption(...)` inside the
  never-taken Morozko branch; `ru_textmd.py` untouched.

## 3. L836 (earlier fix) — STILL INTACT

- text.md L836, byte-exact: `150. ✓ Voir le texte modèle dans la section H de cette page (97 mots)`
- Printed P8 key 150 (raw text + render) is byte-identical. The long form
  (`150. (Question ouverte, texte modèle ci-dessous) — …`) survives only as the
  exercise statement's key on the section-H exercise line L663 — that is the
  exercise line, not the appendix, and it is correct there.
- Section-H model text ("Моя неделя 16–22 ноября…", L664) counts **exactly
  97 whitespace tokens**, within the stated 80–100 range; its Russian is correct.

## 4. Keys / appendix / web PDF

- Appendix keys 1–150 contiguous, none missing; inline exercise numbers 1–150
  contiguous in the body (matching groups as ranges 25–28 / 39–42 / 57–60 /
  75–78 / 141–144). All 150 inline keys agree with the appendix (the 20 matching
  items differ only in separator `·` vs `—`; Q150 differs only in the ✓ form vs
  the exercise-line long form — both by design).
- Printed P8 answer key: 150 entries, none missing, in both layout and raw
  extraction. Normalised comparison vs the appendix: every apparent mismatch is
  a pdftotext artefact — (a) "— СТРАНИЦА N —" group headers bleeding into
  entries in raw mode, (b) word-split threshold merging around `→` / `:` / `—`
  (e.g. "выходят19", "распродажа—"), (c) my own regex splitting on "20." inside
  Q45's "16:20" (Q20/Q45 re-verified directly in the raw text: `20. желании —
  желание = un vœu` and `45. В ноябре солнце садится около 16:20. — Le soleil
  se couche vers 16 h 20` — both correct). Keys themselves match in every case.
- Web PDF: 8 pages, same page size as print (1462.5 × 2025 pts), 3,385,807 bytes
  (< 7 MB); text layer byte-identical to print (112,048 bytes each, `-layout`
  dumps, `cmp` clean); web P8 render pixel-identical to print P8
  (identical PNG SHA). No deferred web verdict needed.

## 5. Page-by-page read (print PDF, all 8 pages, 100-dpi renders + full text.md)

- **P1** — Masthead, kicker, lead (14-й тур, «Зенит»/«Динамо» 31 pt), gloss,
  "ТУР В ЦИФРАХ", exercises 1–6 + quiz 7–10, park photo + caption, weather box,
  "В ЭТОМ НОМЕРЕ" Стр. 2–8 all match actual pages, word of the week
  («чёрная пятница»). Dates: тур 6–8 Nov (Fri–Sun), 12 Nov Thursday,
  17 Nov Tuesday, 15-й тур 20 Nov — all verified against the calendar.
  No overflow/overlap/clipping/tofu.
- **P2** — Student Day / Ded Moroz / weather; holidays list 16–22 Nov; words of
  the week with correct French glosses; Yuon «Зима. Ростов» + caption;
  exercises 11–28. Keys correct (Q20 `желании`, Q22 16:20, Q25–28 matching).
- **P3** — Cinema 19 Nov, five premieres; exercises 29–46. Keys correct
  (Q33 26 Nov Hunger Games — see fact check below; Q38 `ноября`; Q43–46
  sentence building). No photo on P3 (layout as designed).
- **P4** — 14-й тур results table, all 8 matches: Локомотив–Рубин 0:1,
  Факел–Динамо 1:2, Ахмат–Родина 1:0, Краснодар–ЦСКА 4:2,
  Крылья Советов–Оренбург 2:0, Спартак–Акрон 2:1, Зенит–Ростов 2:2,
  Балтика–Динамо Мх 0:1. Goals sum to 21 (1+3+1+6+2+3+4+1) = the "21 гол"
  claim on P1. Correction note re VOL.3 (Балтика–Динамо Мх 0:1, 8 Nov, 20:45)
  consistent with the table. 15-й тур fixtures: 8 matches, 20–22 Nov, weekdays
  correct (Пт 20.11 / Сб 21.11 / Вс 22.11). National-team box (12 Nov Thu 18:00
  Tashkent; 17 Nov Tue 19:00 Krasnodar) + 1912 photo + caption; exercises
  47–64, all keys agree with table and article (Q52 0:1, Q53 2:2, Q54 2:0,
  Q55 0:1, Q56 20:45, Q57–60 matching, Q61–64 verb forms).
- **P5** — «Чёрная пятница» dates (Ozon 13 Nov–2 Dec, WB 16–30 Nov, М.Видео
  from 12 Nov, Яндекс Маркет 25–27 Nov, Lamoda 27–30 Nov, Cyber Monday 30 Nov)
  agree across article, dates box and keys (Q65–69); 11.11 box (14.4M orders)
  and Q73 `заказов` agree; market photo + caption; exercises 65–82.
- **P6** — Week 16–22 Nov; calendar strip 16 пн–22 вс, 21–22 highlighted as
  weekend; chart 38/26/18/18 = 100 with correct keys (Q83 B=2, Q84 5, Q85 B,
  Q86 26, Q87 18); disclaimer "Это учебный опрос редакции… — не настоящая
  статистика / Ceci est un sondage d'exercice…" present in both languages.
  "В ноябре 20 рабочих дней и 10 выходных" re-verified: Nov 2026 has 21
  weekdays − 4 Nov (Unity Day, Wednesday) = 20 working days; 9 weekend days
  + 4 Nov = 10 days off. Exercises 83–100.
- **P7** — Three levels (A2 weather / B1 shopping / B2 attribution); 4 errors
  with correct corrections (с + instrumental, на + prepositional, 21 + гол,
  с + genitive); Pushkin/Kiprensky portrait + caption; letters box (no real
  letters, editorial example, promise moved to VOL.5 — consistent with P2
  "А ВЫ?" box); 8 "ФРАЗЫ НЕДЕЛИ" quotes all verbatim from pages 1–6 with
  correct French translations and page numbers; "СЛЕДУЮЩАЯ НЕДЕЛЯ" band.
  Exercises 101–112.
- **P8** — Big test 113–150 (A chronicle 8, B general 8, C Masha reading 4,
  D sentences 4, E translation 4, F matching 4, G shop dialogue 5, H writing 1
  + 97-word model text) + complete answer key 1–150 ending with the ✓ Q150
  line. Footer "Page 8 sur 8", no overflow. No Morozko image, by design.

## 6. Fact checks done this round (external, beyond round 1)

- **Students' Day "решение… приняли в Праге в 1946 году" (P2, Q21 key 1946):**
  supported — the day was proclaimed in London in 1941, and its celebration was
  confirmed at the World Congress of Students held in Prague in 1946 (Bolashaq /
  Wikipedia accounts). The edition's phrasing matches the Prague-1946
  confirmation; not an error.
- **«Голодные игры: Рассвет жатвы» 26 ноября (P3, Q33 key A = 26 Nov):**
  correct for the Russian release — world premiere 20 Nov (Lionsgate/Scholastic),
  but the Russian distributor moved the Russian release a week to 26 Nov
  (tvmag.ru, sobaka.ru, cyber.sports.ru, mk.ru, lifehacker.ru, metaratings).
- **«Увидеть всё» (P3):** confirmed — A24 documentary about Elizabeth Holmes,
  directed by Nathan Fielder and Lance Oppenheim, Russian release 19 Nov 2026
  (t-j.ru, tbank-online.com).
- **Black Friday 27 Nov 2026 = Friday; Cyber Monday 30 Nov = Monday** — verified
  against the calendar. "В России «чёрную пятницу» проводят с 2013 года" —
  consistent with the known first Russian Black Friday (2013).
- Weekdays for every date in the issue (4/6/7/8/12/16/17/18/19/20/21/22/27/30
  Nov 2026) verified with `date` — all match the edition.

## 7. Word-spacing observations — FACTUAL RECORD ONLY (out of scope, no verdict impact)

Per the brief, the systematic ru-family word-spacing question is under separate
investigation; the strings below are recorded as observed in the 100-dpi renders
of the print PDF, without adjudication. (Round 1 pixel-measured two of these:
P1 "метеорологическая | зима" gap 2.56 SVG units — tight but present; P1 byline
"От редакции | Lucerna" gap 4.8 units — a full normal space — so a joined look at
100 dpi does not by itself mean a missing space. I did not re-measure.)

- P1: "От редакцииLucerna" (byline); "метеорологическаязима" (СНЕГ БУДЕТ? box);
  gloss line "зона вылетаla zone de relégation · на момент сдачиà la date de
  bouclage · в историиpour la première fois de l'histoire".
- P2: "От редакцииLucerna"; "Татьяниндень"; "Профессиональныепраздники";
  "поздравитьféliciter"; "успеховréussite"; "желаниеun vœu";
  "Картина: КонстантинЮон — общественноедостояние" (Yuon credit);
  header "день рожденияДеда Мороза".
- P3: "От редакцииLucerna"; "биографияbiopic"; "криминальнаяpolicier";
  "экранизацияadaptation à l'écran"; "кинозрителяspectateur";
  "Вечеромможно" (Q37); "посмотреть фильмв кино" (Q46).
- P4: "От спортивнойредакцииLucerna"; "возвращается20 ноября";
  header "все восемь результатов+ сборная".
- P5: "От редакцииLucerna"; "начинаютсяуже"; "заказываютнесколько";
  "календарнаядата"; "подошёлva bien"; "примеркиessayage";
  "в прошлом годуl'an dernier"; "бытовую техникуappareils ménagers".
- P6: "От редакцииLucerna"; "выспатьсяи"; "Проверьтепосылку";
  "примерьтепокупку"; "задаютритм"; "честныеde vrais"; "серединаle milieu";
  "Профессиональныепраздники"; "выходныхдней"; "покупкамии";
  "займутсяспортом". (The P6 French disclaimer looked like "d' exercice" at
  100 dpi; pdftotext of the PDF gives "Ceci est un sondage d'exercice de la
  rédaction" — correct, no space — so that was a low-resolution illusion.)
- P7: "синоптикиобещаютles météorologues promettent"; "оттепельredoux";
  "мокрый снег neige mouillée"; "ледяной дождь pluie verglaçante";
  "распродажаgrande vente"; "скидкаremise"; "промокодcode promo";
  "возвратretour"; "Картина: Орест Кипренский— общественноедостояние";
  "Результатматча" (СЛЕДУЮЩАЯ НЕДЕЛЯ band); "промокоддействует" (B1 text);
  "возвращаютв магазин".
- P8: "поздравляетдруга-студента" (Q133 / Masha text); "проверяютпосылки"
  (key 100); "Сначаласоставьтесписок покупок" (key 136);
  "результатматча" (141a). All other P8 strings read normally.

## 8. Observation only (not a finding) — `— СТРАНИЦА ? —` in text.md

- Present at text.md L671, immediately after the
  `### ОТВЕТЫ · CORRIGÉ — CLASSÉ PAR PAGE …` header (L670 is `## Answers`,
  L671 is `— СТРАНИЦА ? —`). Known exporter artifact in all ru-target
  text.md files, per the brief; left as is.

## 9. What was checked in full

- Read all 8 print-PDF pages visually (100 dpi) + web P8 render + full text.md
  (836 lines) + web PDF (page count, size, text layer).
- French: every gloss, instruction, exercise label and answer note read; Russian:
  every article, caption, exercise stem and key read. No French or Russian error
  found this round.
- Keys: appendix 1–150 vs inline keys vs printed P8 keys — all agree
  (artefacts explained in §4).
- Facts spot-verified externally: Nov 2026 calendar (20/10, incl. 4 Nov Unity
  Day); 14-й тур results (8 matches, 21 goals) vs table vs keys; Black Friday /
  11.11 dates; chart sums to 100; model text = 97 words; P7 phrases verbatim vs
  source pages; Students' Day 1946; Hunger Games RU 26 Nov; "Увидеть всё" A24.
- No overflow, overlap, clipping or tofu on any page; footers/masthead correct
  on all pages ("Page N sur 8"); P8 answer key complete to Q150.

## Files / scratch

- Proof note (this file):
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-fr2/PROOF-NOTE.md`
- Scratch renders (ephemeral, /tmp, deleted after the read): `/tmp/rufr2/p-*.png`
  (100 dpi, P1–P8), `/tmp/rufr2/w8-8.png` (web P8), `/tmp/rufr2/print.txt`,
  `web.txt`, `p8.txt`, `p8raw.txt`, `p4.txt`.
- No production file was modified; no commit/push/lint run; nothing copied out
  of the production directory except the /tmp text extractions above.
