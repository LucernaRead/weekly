# PROOF NOTE — W47 ru-es re-proof (independent)

- **Edition:** 2026-w47-ru-es (VOL.4, issue 2026-11-16–22)
- **Proofer:** independent re-proof agent (did not build this edition)
- **Date:** 2026-11-11
- **Verdict: (b) — 17 FINDINGS** (all one defect class: collapsed word spaces in the delivered print PDF; the same class also appears in the web PDF where checked)

## SHA-256 record (start and end)

| File | Start (2026-11-11 ~22:46 UTC) | End | Bytes |
|---|---|---|---|
| `2026-w47-ru-es.text.md` | `332c8e4f5478181d21281fe059483f0da4ee2bf5e39fec4464f836049e2bad60` | identical | 64,176 |
| `Lucerna-VOL4-ru-es.pdf` (print) | `64cb48f90dea70553a76e70c8cb9bc75ffa571c1ceaa8318c8655b47b80cf7c3` | identical | 21,278,615 |
| `Lucerna-VOL4-ru-es-web.pdf` (web) | `526873a863981b82d6d56892508ef635204baf1569746ba4b2d0b70cd96c8123` | identical | 3,387,494 |

- Print SHA **matches KIT §5**. Print SHA did not change during the read (as expected — print was not rebuilt by this fix).
- Web SHA **differs from KIT §5** (`7af50086c326e1d5bcd78afa746663e3a0d1c5b5b35735a719a17006b694b051`, 3,387,465 B). Known drift: the concurrent pre-insert web-PDF rebuild rewrote all 9 ru web PDFs; the KIT already records this. Not a defect on its own — web content was verified (below). Web SHA was **stable across the whole read** (start = end), so the web check is complete, not deferred.
- text.md SHA matches the required value exactly (`332c8e4f…`, 64,176 B).

## Trigger fix verified (the reason for this re-proof)

- text.md L836 exactly: `150. ✓ Véase el texto modelo en la sección H de esta página (97 palabras)` — matches the print P8 Q150 line exactly.
- Model text ("Пример: Моя неделя 16–22 ноября…") counted **97 words** — matches "(97 palabras)".
- Appendix keys 1–150 all match the printed P8 keys: 128/150 regex-matched with ZERO diffs vs the text.md appendix; the remaining 22 (35, 43–46, 79–82, 97–100, 133–140, 150) confirmed by eye in the text-layer tail — all match.
- **The L836 fix itself is correct and complete. The 17 findings below are pre-existing delivery defects, unrelated to the L836 change (print/web PDFs were not rebuilt by this fix).**

## Defect class

**Collapsed word space in the delivered print PDF.** The builder splits text into per-word `<text>` elements with explicit x positions plus separate space elements (usually in "Noto Sans CJK SC"). For some words the rendered ink overruns the builder's width estimate and swallows the following space, so two words render as one glued token (e.g. "метеорологическаязима"). The space element exists in the SVG with a normal advance (3.8–5.8 SVG units ≈ 2.9–4.4 pt) — the defect is in the rendered PDF, not the source text. The KIT's self-check ("no overflow, no overlap, no clipped text") and the occlusion audit (42 TEXTX, 0 LINEX, adjudicated 42/42 CLEAR) do **not** catch this class: there is no overlap, just a missing gap.

**Adjudication standard:** 200 dpi zoom; the junction reads as one word (glyphs touch/interlock, gap no wider than inter-letter gaps in the same words) while other word spaces on the same line are clearly wider. Pixel-measured gaps are supporting evidence only; visual reading at 200 dpi is decisive. 60 dpi impressions are unreliable (several junctions that look glued at 60 dpi are fine at 200 dpi). pdftotext word-merging alone is NOT proof (false positives exist — see "Checked and NOT defects").

## Findings (17)

### P1
1. **"СНЕГ БУДЕТ?" box** — `метеорологическаязима` — "Устойчивый снег ляжет позже, чем обычно: метеорологическая зима придёт…" renders as one word. Measured ink gap 1.8 pt vs 5.4–6.1 pt normal word spaces on the same line.

### P2
2. **"ПРАЗДНИКИ НЕДЕЛИ" box** — `рожденияДеда` — "18 ноября — день рожденияДеда Мороза". Ink continuous (0 pt gap); neighbours "день рождения" and "Деда Мороза" have normal spaces.
3. **Body text** — `Профессиональныепраздники` — "Профессиональные праздники не дают выходных: это рабочие дни…" Measured 2.9 pt vs 4.3–14.0 pt on the same line; visibly glued.
4. **Nota box** — `поздравитьfelicitar` — "Nota — поздравить felicitar · родина tierra natal · повод motivo." Measured 2.9 pt vs 5.0–10.4 pt on the same line; "ь" and "f" touch.

### P3
5. **Nota box** — `криминальнаяpolicíaca` — "биография biopic · криминальная policíaca · сказочное de cuento." Measured 3.2 pt; "я" and "p" touch.
6. **Nota box** — `экранизацияadaptación` — "экранизация adaptación al cine · кинозрителя espectador." Measured 3.2 pt; "я" and "a" touch.

### P4
7. **Masthead kicker (dark band)** — `результатов+` — "14-й тур: все восемь результатов+ сборная" (text.md: "результатов + сборная"). Space before "+" collapsed (ink gap ≤1.8 pt, i.e. letter-spacing size) while the space after "+" is normal 4.3 pt. SVG: 'результатов' x=1234.5, space x=1341.8, '+' x=1345.8 — rendered "результатов" ink overruns ~4+ units.

### P5
8. **Nota box** — `календарнаядата` — "календарная дата fecha del calendario". Measured 2.5 pt; "я" and "д" touch.
9. **Body text** — `маркетплейсахскидки` — "на маркетплейсах скидки начинаются уже в середине месяца." Measured 2.5 pt vs 5.4 pt for the other space on the same line (на→маркетплейсах).
10. **Body text** — `начинаютсяуже` — same sentence, next line. Measured 2.2 pt vs 4.7 pt (уже→в) on the same line.

### P6
11. **Chart disclaimer** — `упражнений—` — "Это учебный опрос редакции для упражнений— не настоящая статистика." Pre-dash space collapsed, post-dash space normal (asymmetric, same class as #7).

### P7
12. **Pushkin caption** — `Кипренский—` — "Картина: Орест Кипренский— общественное достояние (Wikimedia Commons)". Pre-dash space collapsed, post-dash space normal.

### P8
13. **Q135** — `заказываетподарок` — "В пятницу Маша заказывает подарок → ___". Measured 1.1–1.2 pt; "т" and "п" touch.
14. **Answers 82** — `negativo:не` — "82. Не спешите с покупкой. — Imperativo negativo:не спешите". Colon junction; ":" touches "н".
15. **Answers 100** — `возвращаютпокупки` — "100. Люди проверяют посылки или возвращаютпокупки. — …". Measured 1.3 pt; "т" and "п" touch.
16. **Answers 135** — `заказываетподарок` — "135. В пятницу Маша заказываетподарок. — El tiempo primero, el lugar en segundo lugar". Measured 1.1 pt; same word pair as #13.
17. **Answers 139** — `Atención:играть` — "139. El martes Rusia juega contra Venezuela. — Atención:играть + с + instrumental". Colon junction; ":" touches "и". Present identically in the web PDF text layer (checked in both PDFs).

## Page-by-page notes

- **P1:** Lead, kickers, byline, quiz Q7–Q10, word of the week, "СНЕГ БУДЕТ?" box, "КОРОТКО" box, park photo caption — all read correctly except finding #1. Byline "От редакции Lucerna" verified fine (ink gap 3.6–4.0 pt, identical to the other space in the same line — pdftotext merge is an artifact). Nota gloss "в истории por primera vez en la historia" fine; Q5 "Чемпионат возвращается ___ ноября" fine; Q8 "Как сыграли" fine; Q6 "В 14-м туре забили ___ гол." fine; caption "лицензия CC0" fine (narrow but visible gap); "играет с Венесуэлой в" fine; "Главные темы недели" fine.
- **P2:** Holidays box, body, Nota box, Yuon caption — findings #2–#4. Caption "Константин Юон — общественное достояние" fine; "желание un" fine (3.6 pt, clear gap). Large white gaps in the middle columns are layout whitespace, not defects.
- **P3:** Cinema lead, Nota box — findings #5–#6. "биография biopic" fine (4.3 pt). Large white gaps in the middle column are layout whitespace, not defects.
- **P4:** Football results, kicker — finding #7. "Результат на", "возвращается 20", "Узбекистаном в" fine; caption "автор неизвестен, 1912 — общественное достояние" fine.
- **P5:** Black Friday lead, Nota box, body — findings #8–#10. Kicker "скидки с 16 ноября" fine.
- **P6:** Chart + disclaimer + "Фразы недели" quotes — finding #11. Chart sums 38+26+18+18=100. Scores/dates cross-checked consistent (Krasnodar–CSKA 4:2, Zenit–Rostov 2:2, Baltika–Dinamo Mh 0:1 20:45, Krylia–Orenburg 2:0, Spartak–Akron 2:1). "редакции для" checked and fine (borderline: 2.9 pt vs ~5.0–5.4 pt normal, but the 200 dpi crop shows an even, clearly visible gap the same as the next word space in the line); "настоящая статистика" fine.
- **P7:** Pushkin lead, "Фразы недели" quotes, gloss lines A2/B1/B2 — finding #12. Quotes verified verbatim against P1–P6 text. "синоптики обещают" (4.7 pt), "может быть" (3.6 pt, both body and gloss occurrences), "распродажа gran" (3.2 pt, clear gap), "распродажа = gran venta", "Профессиональные праздники", "возвращается 20" all fine.
- **P8:** Test Q113–Q150 + answers 1–150 + model text H — findings #13–#17. Q150 ✓ line matches text.md L836 exactly; model text 97 words; appendix keys 1–150 all match (see above). Weekdays verified with `date -d`: 12 Nov Thu, 16 Nov Mon, 17 Nov Tue, 18 Nov Wed, 19 Nov Thu, 20 Nov Fri, 21 Nov Sat, 22 Nov Sun, 27 Nov Fri — all as printed. Morozko image skipped by the build's own condition (known, by design, same as W46 ru-es). Checked and fine: Q113 "начинается ___", Q117 "выходят ___", Q118 "начнётся ___", Q121 "Когда День", Q122 "Сколько рабочих дней", Q125 "Когда «чёрная", Q126 "Устойчивый снег", Q129 "Студентка ·", Q130 "поздравляет во вторник", Q133 "поздравляет друга-студента", Q140 "Поздравляю с", Q147 "Проверьте ___", Q148 "— Всё в порядке, спасибо!", Q149 "Хороших ___!", A43 "выходят 19", A79 "Сначала список", A80 "начинается 16", A133 "поздравляет друга-студента", A136 "Сначала составьте список покупок", answers line 35 "рассказывает — рассказывать → рассказывает", P8 "—" / "=" / "→" / "+" separator junctions (line-35 precedent: 1.4 pt gaps around separators read fine).
- **General:** No overflow, overlap, clipping, or tofu seen anywhere in the print PDF. All 8 pages read in Spanish (reader language) with correct Russian source text; weekly word, exercises, and captions correct apart from the findings above.

## Web PDF check

- Text layer identical to print (whitespace-stripped sorted-char multiset diff empty, 30,838 chars).
- Web P1 and P8 rendered at 60 dpi and visually spot-checked — layout identical to print.
- Finding #17 ("Atención:играть") confirmed present in the web PDF text layer as well (same defect class in web). The other print findings were not individually re-rendered in web, but the web text layer is identical to print, so the same collapsed spaces are expected throughout the web PDF (the defect is in the shared rendering, not the file).
- Web SHA stable across the whole read — check complete, not deferred.

## Checked and NOT defects (do not re-report)

- P1/P4 bylines "От редакции Lucerna" / "От спортивной редакции Lucerna" (3.6–4.0 pt, identical to the other space in the same line — pdftotext merge is an artifact); P2 "желание un" (3.6 pt, clear gap); P3 "биография biopic" (4.3 pt); P6 "редакции для" (2.9 pt, clear gap in 200 dpi crop — borderline, kept fine); P7 "синоптики обещают" (4.7 pt), "может быть" (3.6 pt), "распродажа gran" (3.2 pt, clear gap); P5 kicker "скидки с 16 ноября"; P7 gloss lines A2/B1/B2 (all junctions clear at 200 dpi); P7 "Фразы недели" quotes; P7 "распродажа = gran venta"; P8 Q116 "играет с", Q122 "рабочих дней", Q130 "поздравляет во вторник", Q133 "поздравляет друга-студента", Q141 "результат матча", A43 "выходят 19", A79 "Сначала список", A80 "начинается 16", A133 "поздравляет друга-студента", A136 "Сначала составьте список покупок", answers line 35, P8 "—"/"="/"→"/"+" separator junctions; P4 "Результат на", "возвращается 20", "Узбекистаном в", caption "автор неизвестен, 1912"; P2 caption "Константин Юон"; P1 "играет с Венесуэлой в", "Главные темы недели", Q8 "Как сыграли", Q6 "В 14-м туре забили ___ гол.", caption "лицензия CC0"; P1 Nota gloss "в истории por…"; P1 Q5 "Чемпионат возвращается ___ ноября"; Q113, Q117, Q118, Q121, Q125, Q126, Q129, Q140, Q147, Q148, Q149; P6 "настоящая статистика"; H model text "проверяю промокоды и заказываю подарок" (clear space — same word pair as Q135/A135, but fine here: different line, different justification).
- **A81 "Промокод действует"** (answers 81): narrow but visible gap — 2.5 pt at x-height, within the line's normal 2.2–4.0 pt word-space range (confirmed by 4× tight zoom); the 1.3 pt bbox reading is descender-level narrowing of the two "д" tails only. NOT a defect.

## Method

- Print PDF text layer read for all 8 pages; all 8 pages rendered to PNG at 60 dpi and read; P1, P4, P5 rendered at 200 dpi with many zoom crops and pixel measurements.
- Candidates found via (i) pdftotext-merged-word detection vs text.md vocabulary (33 candidates incl. false positives like 'восемь', 'задают'), (ii) full-SVG space-element sweep (3,159 junctions measured by pixel gaps — largely unreliable: many 0.0 readings are band/transform artifacts; p1 SVG has 1 `transform`, others 0; not trusted without visual confirmation), (iii) bbox adjacent-word gap sweep (5,772 pairs; line grouping by y only, so line medians inflated by inter-column gaps — flags need visual confirmation).
- Every flagged junction adjudicated visually at 200 dpi. PDF→SVG scale: PDF pt = SVG units × 0.75; 200 dpi px = SVG units × 2.0833.
- P8 small type (13–13.8 pt): ~1.4 pt gaps there render as acceptable word spaces (verified on answers line 35); only junctions where the glyphs touch/interlock at 200 dpi are listed as defects.
- Working renders/crops live in `/tmp/ru-es-proof/` (ephemeral; ~20 MB).

## KIT drift note (for coordinator's KIT-sync wave)

- Web PDF SHA on disk (`526873a8…`, 3,387,494 B) differs from KIT §5 (`7af50086…`, 3,387,465 B) — the pre-insert web-PDF rebuild. Content verified identical to print.
- Print SHA matches KIT §5.
