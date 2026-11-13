# PROOF NOTE — 2026-w47-ru-ja (independent re-proof, round 2)

- Edition: `2026-w47-ru-ja` (Russian target, Japanese reader), VOL.4
- Production dir: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-ja/`
- Proofreader: independent (did not build this edition)
- Date: 2026-11-11
- Method: read all 8 pages of the print PDF visually (80 dpi full-page renders +
  3× zoom crops of suspect lines), read `2026-w47-ru-ja.text.md` in full (838 lines),
  read the web PDF (text layer + P8 render). Mechanical checks with the repo tools
  (`tools/p8.py extract`, `tools/venv/bin/python` + PyMuPDF span/word audits).
  Read-only; no production file modified, no render, no lint, no commit.

## VERDICT: (b) — FINDINGS (one systematic defect class, ~90 sites)

One defect class, present on all 8 pages: **the space character is missing between
words** — at SVG span boundaries (neither adjacent span carries a space) and, in
several cases, baked into a single span's string. What is left is only a 0–2.7 pt
layout gap. Where the gap is ≤ ~1.5 pt the words visibly run together
(verified at 3× zoom); where it is 1.6–2.7 pt it reads as a markedly tight space.
Normal inter-word space in this edition is ~3–3.5 pt at body size (calibrated on
P4 body text, where spans abut at gap 0.0 and the space lives inside the span
text, e.g. `'й тур сыграли'`, `' 6–8'`). This is NOT the KIT's ruled-normal
"narrow (4–6 px) Cyrillic–Latin gloss space": the gaps here are ~1–2 pt
(≈1–3 px at any render scale), and most joins are Cyrillic–Cyrillic
(`КонстантинЮон`, `Профессиональныепраздники`, `современногорусского`,
`настоящаястатистика`, `Главныетемынеделив`), which that ruling does not cover.
The pattern (same fault in bylines, captions, glosses, stems, body text, answers
on all 8 pages) points to a renderer/template root cause, not per-page typos —
fix belongs to the build/template wave, but the defect is in this delivered print
PDF and in the web PDF (same SVGs; web text layer is literally identical).

Everything else verified clean (see §3–§5). No overflow/overlap/clipping/tofu
found on any page; no content/factual/key error found. The L836 fix that
triggered this re-proof is itself correct (§2).

## §1 SHAs (start = end; nothing changed during the read)

| file | SHA-256 | bytes |
|---|---|---|
| `2026-w47-ru-ja.text.md` | `07824474bb88439bea67fb4d1dc3ede956f33b006a32e8203e5b52081c1090da` | 64,477 |
| `Lucerna-VOL4-ru-ja.pdf` (print) | `150f970828142d50cc10ba157182dd282c22dd74d82de5f7c932141d86cda0a3` | 27,409,704 |
| `Lucerna-VOL4-ru-ja-web.pdf` (web) | `ea1a9d7381f02e18ab24c3d20c36efec1b9b58cf3494b3e2478a27a1851a6743` | 3,721,620 |

- text.md SHA matches the required `07824474…` exactly; size 64,477 B. ✓
- Print SHA matches KIT §5 exactly; print was NOT rebuilt by the fix. ✓
- Web SHA differs from KIT §5 (`57cf6b07…`, 3,721,635 B) — KNOWN drift, not a
  defect: per the KIT Fix-1 note, concurrent webpdf rebuild jobs rewrote all 9 ru
  web PDFs during the apply (22:19 UTC). On-disk web SHA was stable across this
  whole read (start = end), web PDF is 8 pages, text layer literally identical to
  print (80,927 chars, byte-identical `pdftotext` output), P8 render matches
  print P8. Web check is COMPLETE, not deferred. Coordinator to reconcile the
  KIT web SHA in the KIT-sync wave.

## §2 The L836 fix — VERIFIED CORRECT

- text.md L836 reads exactly: `150. ✓ 模範文はこのページの H 欄（97 語）`
- Print P8 appendix line 150 reads exactly the same string (pdftotext P8,
  line 823; `tools/p8.py extract` gives printed key `✓` with that note).
  L836 == printed P8 Q150 line. ✓
- The note text is unchanged vs the old long form; only the redundant
  parenthesised prefix was dropped. The body Q150 stem still carries the
  full note (`key: （自由記述、模範文は下） (模範文はこのページの H 欄（97 語）)`),
  which is the same note text — not a mismatch.
- Model text counted independently: exactly **97 words** (matches the
  "97 語" claim in the H brief, the appendix line and the P8 header). ✓

## §3 Key / exercise verification — ALL CLEAN

- `tools/p8.py extract --p8 svg/p8-test.svg --total 150`: noted set **150/150**.
- Appendix keys in text.md: 1–150 contiguous, each key value matches the
  printed P8 key (149/150 exact string match; 150 differs only in that the
  extractor splits key `✓` from its note — the full printed line equals the
  appendix line, see §2). The KIT's keydiff [137, 138, 139, 140] is vs the
  core's Russian keys — expected, since these four are RU→Japanese translation
  items re-aimed at the reader language; their Japanese keys are correct.
- Body key cross-check (all 150 stems vs appendix): 0 mismatches apart from
  the Q150 key/note split described in §2.
- No tofu (0 U+FFFD in text.md); no `解説 — 解説` double gloss anywhere.
- Spot-checked fixes from the re-fanout: Q20 key `желании` ✓, Q25 option
  `День студента` ✓, Q54 `2:0` ✓, Q57–60 matchings ✓.

## §4 Content verification — ALL CLEAN

- Weekdays: 12 Nov Thu, 16 Nov Mon, 17 Nov Tue, 18 Nov Wed, 19 Nov Thu,
  20 Nov Fri, 21–22 Sat–Sun, 27 Nov Fri, 30 Nov Mon — all correct for 2026.
- P4 results table: all 8 round-14 matches present
  (Локомотив–Рубин 0:1, Факел–Динамо 1:2, Ахмат–Родина 1:0, Краснодар–ЦСКА 4:2,
  Крылья Советов–Оренбург 2:0, Спартак–Акрон 2:1, Зенит–Ростов 2:2,
  Балтика–Динамо Мх 0:1); goals sum to **21**, matching the P1 claim.
  Round-15 fixtures: 8 matches, 20–22 Nov, weekdays correct.
- P6 chart: 38/26/18/18 = 100%, bars proportional, labelled practice data with
  the full disclaimer; calendar strip 16–22 correct (21–22 highlighted).
- "В ноябре 20 рабочих дней и 10 выходных" correct for Russia (4 Nov holiday).
- P7 "ФРАЗЫ НЕДЕЛИ": all 8 quotes verified verbatim against their cited pages
  (P1 ×2, P2, P3, P4, P5, P6 ×2). Letters box + F-MAIL disclosure present in
  Russian and Japanese; Pushkin caption, weekly word (`чёрная пятница`,
  P1 + P7) and all 5 photo credits present.
- P1 index ("В ЭТОМ НОМЕРЕ") pages/levels match P2–P8; P1 "О ЧЁМ ПИШУТ" list
  matches text.md.
- No overflow, overlap, clipping or tofu on any of the 8 pages (full-page
  visual read). P2/P3 mid-column whitespace is layout air, not a defect.

## §5 FINDINGS — missing space characters (one class, all pages)

Notation: `A|B` = words run together as printed (space character absent;
layout gap shown in pt where measured). "Joined" = gap ≤ ~1.5 pt or baked
into one span (visually run together, 3×-zoom verified for a representative
sample on every page). "Narrow" = same missing space, gap 1.6–2.7 pt
(tight but discernible gap). Both lists are the same root cause.

### P1 — joined
- Byline: `От редакции|Lucerna` (1.1)
- Right rail, grey line under О ЧЁМ ПИШУТ: `Главные|темы|недели|в|российских|СМИ`
  (whole line unspaced)
- Right rail, source line: `По российским|СМИ, ноябрь 2026 г.`
- Photo credit: `—|лицензия` (1.3), `лицензия|CC0` (1.1)
- СНЕГ БУДЕТ box: `Устойчивый|снег`, `метеорологическая|зима`, `в двадцатые|числа`,
  `Не забудьте|тёплую`
- Body: `на момент|сдачи`, `результат|этого`, `с Узбекистаном|в`,
  `большая распродажа|в`, `скидки в магазинах|и`, `как завершился|14-й` (deck)
- Index: `Студенты|и` ("Стр. 2 Студенты и Дед Мороз")
- Q7 `Сколько|очков`, Q9 `Когда|сборная`, Q10 `Когда|начинается|«чёрная`
### P1 — narrow
- Gloss: `зона вылета|降格圏内` (1.9), `в истории|史上初めて。` (1.6)
- Word box: `чёрная пятница|= ブラックフライデー` (no space before `=`)

### P2 — joined
- Byline: `От редакции|Lucerna` (1.1)
- Band title: `день рождения|Деда Мороза`
- Body: `Международный|день` (body + Q11), `В России главный|студенческий|день`,
  `Татьянин|день`, `Праздник отмечают|в`, `Профессиональные|праздники` (body + Q15),
  `Успехов|в учёбе`, `самое главное|желание`, `лучшие мы напечатаем|в`,
  `Что вы пожелаете|студенту`, `День работника налоговых|органов`,
  `День преподавателя|высшей школы`, `Четыре слова о ноябрьской|погоде`
- Credit: `Картина: Константин|Юон`
- Gloss 1: `поздравить|祝う` (1.3); gloss 2: `желание|願い` (1.4)
- Exercises: Q12 `Главный|студенческий|день`; Q15 stem `Профессиональные|праздники`;
  `Напишите два предложения|по-русски` (body + А ВЫ? box, ×2)
### P2 — narrow
- Gloss 2: `успехов|成功` (2.0)

### P3 — joined
- Byline: `От редакции|Lucerna` (1.1)
- Gloss 1: `криминальная|犯罪もの` (0.6); gloss 2: `экранизация|映画化` (1.0),
  `кинозрителя|観客` (0.7)
- Body: `в прокат выходят|сразу`, `«Голодные|игры»` (×3),
  `документальный|фильм`, `об Элизабет|Холмс`, `основательнице|стартапа`,
  `сказочное|фэнтези`, `сначала|один фильм`, `Владимира|Маяковского`
- Q29 `Сколько|премьер`
### P3 — narrow
- Gloss 1: `биография|伝記映画` (1.6)
- Q31 option: `A.|в Москве` (2.3)
- Section head: `ГЛАГОЛЫ|И ФОРМЫ`

### P4 — joined
- Byline: `От спортивной|редакции|Lucerna` (two joins, 1.1)
- Band title: `все восемь результатов|+ сборная` (gap −0.2, `+` touching)
- Body: `мы напечатали|только`, `Спасибо внимательным|читателям`,
  `гости сравняли|счёт`, `играла с Узбекистаном|в`, `Результат|на момент сдачи`
- Credit: `общественное достояние|(Wikimedia Commons)` (1.1)
- Q47 `Сколько|матчей`, Q56 `Матч … начался|в`
### P4 — narrow
- Body: `чемпионат возвращается|20 ноября` (2.1)
- Gloss: `поправка|訂正` (2.0), `в зоне вылета|降格圏` (2.0)
- Q49 option: `A.|на 15-й минуте` (1.6)
- Q50 option: `A. 20|ноября` (mechanically detected, no space char)

### P5 — joined
- Byline: `От редакции|Lucerna` (1.1)
- Band title: `«Чёрная пятница»: скидки|с 16 ноября`
- Body: `Когда|и где?`, `скидки … начинаются|уже`, `главная распродажа|года`,
  `многие заказывают|несколько`, `на маркетплейсах|скидки`,
  `промокоды на электронику действуют|обычно`, `промокоды|на электронику`,
  `предварительно|с 25 по 27 ноября`, `«скидка 90%» не всегда|значит` (×2),
  `Распродажа|11.11`
- Gloss 1: `календарная|дата` (baked into one span), `примерки|試着` (1.5);
  gloss 2: `в прошлом|году`, `бытовую|технику|家電` (1.5)
- Credit: `Фото: Престон|Керес`, `общественное достояние|(Wikimedia Commons)` (1.1)
- B1 example: `Проверьте|срок`
- C76: `товар возвращают|в магазин`
### P5 — narrow
- Gloss 1: `подошёл|ぴったり合った` (2.1)

### P6 — joined
- Byline: `От редакции|Lucerna` (1.1)
- Body: `Проверьте|посылку`, `примерьте|покупку`, `не забудьте|вернуть`,
  `заказы|с 11.11`, `заказы … приходят|именно`, `Это учебный|опрос`,
  `опрос редакции|для упражнений` (baked: span text `редакциидля упражнений`)
- Gloss: `задают|ритм` (baked: `задаютритм`)
- Disclaimer: `для упражнений|— не настоящая|статистика`
  (`упражнений—` 1.2; `настоящаястатистика` baked into one span)
- Q83 `Сколько|выходных|дней`, Q88 `Профессиональные|праздники`,
  Q100 stem `Люди … возвращают|покупки`
### P6 — narrow
- Band title: `Неделя|16–22 ноября` (2.0)
- Gloss: `честные|本物` (2.1), `середина|真ん中` (1.9)
- Calendar legend: `выходные|(21–22 ноября)` (1.8), `выходные|+ 15-й тур` (2.0),
  `Светлое|— рабочие дни` (2.1)

### P7 — joined
- A2 body: `Гололедица|опасна:`, `будьте|осторожны!`
- A2 gloss: `мокрый|снег`, `ледяной|дождь` (both baked into gloss spans)
- B1 body: `Проверьте|срок` (example + Q108), `промокод|действует`,
  `товар возвращают|в магазин`, `сначала|список`
- B1 gloss: `распродажа|大セール` (1.4)
- B2 body: `Когда|факт`, `признак хорошего|уровня`
- B2 gloss: `синоптики|обещают` (baked), `может|быть` (baked: `можетбыть`)
- Error clinic: `Проверьте|срок` (see B1 body above)
- Caption: `современного|русского`, `литературного|языка` (both baked),
  `Кипренский|—` (0.8), `общественное|достояние` (baked),
  `достояние|(Wikimedia Commons)` (1.1)
- Phrase: `«Профессиональные|праздники не дают выходных»`
- Letters box: `Настоящих|писем`
- Next-week band: `Результат|матча` (baked)
- Band subtitle: `Фокус|на язык`, `Три|уровня, три темы`
### P7 — narrow
- B1 gloss: `скидка|割引` (1.6), `промокод|割引コード` (1.6), `возврат|返品` (2.0)
- A2 gloss: `оттепель|雪解け` (1.6)
- B2 gloss: `по данным|により` (1.9)
- Error clinic: `«забили 21 гол»` gloss reads `забили|21` (1.7, no space char)
- Phrases: `«После паузы чемпионат возвращается|20 ноября»` (1.9);
  `(Страница|1)` ×8 in phrase notes (1.8 each — tight space before the digit)

### P8 — joined
- Band subtitle: `Большой|тест недели` (baked: `Большойтест недели`)
- C text: `Маша поздравляет|друга-студента` (×2: C text + D133),
  `Кого Маша поздравляет|во вторник?` (Q130),
  `в пункте выдачи|и проверяет подарок`
- D135: `Маша заказывает|подарок`; D136: `Сначала|составьте|список`;
  F143: `результат|матча, например 2:2`
- H model text: `начинается|в понедельник`, `начинается|16 ноября`,
  `я поздравляю|друга-студента`, `я заказываю|подарок`,
  `проверяю|покупку`, `готовлюсь|к новой неделе`,
  `начинается|15-й тур!`
- Q121 `Когда|День`, Q122 `Сколько|рабочих`, Q123 `Сколько|очков`,
  Q125 `Когда|«чёрная`, Q125 option `A. 13|ноября`, Q140 `Поздравляю|с`
- Answers: 43 `Пять премьер выходят|19 ноября`, 79 `Сначала|список,`,
  81 `Промокод|действует 4–7 дней` (baked: `Промокоддействует4–7`),
  100 `… или возвращают|покупки`, 126 `Устойчивый|снег`,
  35 `рассказывает|— рассказывать` (0.9)
### P8 — narrow / glue (same root cause)
- Answers: `=` glued in `распродажа|= 大セール` (70, 105), `промокод|= プロモコード`
  (72, 108), `выспаться|= たっぷり寝る` (95); `→` junctions with ~1–2 pt gaps
  and no space char (e.g. 35 `рассказывать→рассказывает`, 34 `выходить→выходят`,
  61 `сыграть→сыграли`); `В … начинается|15-` (Q118 stem, 1.3),
  `начинается|16` (answers, 1.9).
- Not counted as defects: Japanese-note-internal CJK↔digit spacing
  (`11月17日` etc.) and the `✓ … H 欄` note — normal Japanese mixed-text
  setting, verified visually fine.

### Mechanism evidence (for the fix wave)
- Calibration: in correctly spaced body text, spans abut at gap 0.0 and the
  space lives INSIDE span text (`'й тур сыграли'`, `' 6–8'`, `' ноября'`).
  At every finding above, NEITHER adjacent span carries a space character —
  the space is absent from the text stream, not merely narrow.
- Audit method: `tools/venv/bin/python` + PyMuPDF `get_text('dict')` span
  audit (no-space-char boundaries, gap reported) + `get_text('words')`
  token-membership scan vs text.md + 3× zoom crops of ~25 sites.
  Full mechanical lists kept with this note's working files in `/tmp/rujaproof/`
  (`spanaudit3.txt`; renders `pg-*.png`, crops `c-*`/`v-*`/`w-*`/`g-*`).
  Note: `/tmp` is ephemeral — the lists above are the durable record.

## §6 Non-defect observations (not findings)

- Q140 appendix key `みなさん、学生の日おめでとう！` adds `みなさん` ("everyone"),
  which has no counterpart in the Russian `Поздравляю с Днём студента!`.
  Mild translation liberty, meaning preserved; not flagged as a defect.
- `— СТРАНИЦА ? —` separator and the trailing «Морозко» credit in text.md
  match the core exporter's format (per KIT, not a defect).
- text.md omits the F-MAIL disclosure and the P1 word gloss by the exporter's
  established exclusion of variable-assembled content (per KIT, not a defect).
- P1 photo credit `лицензия CC0`: first read as fine, then char-level
  measurement showed NO space character (1.1 pt gap) — it IS a finding,
  listed in §5 P1. (Recorded here so the change of call is traceable.)
- P4 body `возвращается 20 ноября` and P8 `рассказывать → рассказывает`
  looked spaced at 80 dpi but have no space character and only a ~2 pt gap;
  listed under narrow in §5 (same root cause).

## §7 Scope / what was NOT checked

- Web PDF: text layer + P8 render checked; full 8-page web visual read not
  done (web is built from the same SVGs and its text layer is byte-identical
  to print, so a separate full read would duplicate the print read).
- No lint run, no commit, no push, no render, no file modification (per brief).
- Disk: no large intermediates kept outside /tmp; this note is the only file
  written (in the scratch dir named in the brief).
