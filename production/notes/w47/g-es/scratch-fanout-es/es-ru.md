# es-ru — Per-edition record (2026-11-11)

Status: **COMPLETE — self-check zero issues; awaiting independent proofreading.**

## Coverage pre-check

- ru-missing 129 items; ru-conflicts 0 lines; ru.json 263 keys.
- All covered by MANUAL + harvest/ru.json + special handling.
- apply_fanout.py CJK allow-list: Latin/ru = zero CJK in .py ✓.

## Apply

- `apply_fanout.py ru`: 487 total literal replacements; 1 manual-over-harvest
  override: «Después ___ (原形 enviar) el sobre.» harvest «Después ___
  (инфинитив enviar) el sobre.» → manual «Después ___ (инфинитив: enviar)
  el sobre.» (with colon).
- Leftover zh keys NONE; CJK in .py NONE.
- Band titles verified: VIDA　Жизнь, CULTURA　Культура, JUVENTUD　Молодёжь
  (capitalised, not all-caps). «EL CALENDARIO　Календарь» — short gloss,
  no pt-§6.13 overflow risk. P8 header already «Страница 8» (harvest
  de-capped). P8 writing type «Письмо» (content8.py:134 — the ✓ form).

## Pre-build fixes (all wrap-measured before build — in SANS at the real width)

- P1 gloss (content12.py:116, sans 19, gw): ««Дебаты»: два человека или
  больше обсуждают публично, по очереди и с вопросами.» (2 lines) →
  ««Дебаты»: люди обсуждают публично.» (356.6 units, 1 line at 378.5).
  The nl lesson was applied from the start: measured in sans at gw, not
  serif at CW.
- P7 word-box gloss: «debate = дебаты: публичное обсуждение по очереди.
  Эта неделя — неделя дебатов; выборы — 29-го.» (3 lines @20) →
  «debate = дебаты: публичное обсуждение; выборы — 29-го.» (2 lines @20).
- P7 F-MAIL editor's note: original 6 lines @20 / 5 @19 (CW) → first
  draft «Примечание редакции: er waren...» — no: the Russian draft was
  «Примечание редакции: к сдачи номера настоящих писем и лучших текстов
  не поступило, поэтому в этом выпуске — письмо-образец от редакции.
  Обещание переносится на VOL.5. Пишите нам!» — measured 5 lines @19
  at CW-44 → replaced with «Примечание редакции: к сдаче номера
  настоящих писем и лучших текстов не поступило; в этом выпуске —
  письмо-образец. Обещание — на VOL.5.» (4 lines @19 at CW−44 ✓).
  Includes a grammar fix of the harvest: «к сдачи номера» → «к сдаче
  номера» (к + dative). The ldcn wrap size was changed 20→19 and
  multiplier *29→*27 (content7.py:102) and the para 20→19 (:109),
  mirroring the Latin editions — otherwise col3 lands +29.
- P7 ERRORES notes (4): ALL FOUR were 2 lines at CW-44 in harvest
  (ERR1 438.9, ERR2 413.8, ERR3 570.2, ERR4 382.3) — the most of any
  edition (fr: 2, nl: 2). Each extra line adds ~26.5px to the errores
  box (+106px if left). Shortened to 1 line each: ERR1 «Час —
  единственное число: es.»; ERR2 «mejor уже сравнительная степень.»
  (drops «: без más» — «Sin más» is already in the Spanish right line
  above); ERR3 «gente — единственное: глагол — тоже.» («глагол в
  единственном числе» didn't fit; «gente — единственное число: глагол
  тоже.» was also 2 lines); ERR4 «creo que утверждает: изъявительное.»
  (drops « es.»).
- P5 your-turn: «Вы голосовали бы по почте или лично? Что бы вы купили
  в «чёрную пятницу»: что-то полезное или каприз? Напишите два
  предложения и пришлите их.» — 5 lines @20, 4 lines @19 (CW-44) →
  rendered at 19 with eh wrap size 20→19 + multiplier *29→*27, text
  UNCHANGED (see §6.11: 4 lines @19 → P5 col3 1601.55, 6.45px above the
  divider, adjudicated).
- P3 your-turn: «Вы когда-нибудь слушали фламенко? Какая музыка вашей
  страны обладает дуэнде? Напишите два предложения и пришлите их.»
  (4 lines @20 AND @19) → «Вы слушали фламенко? Какая музыка вашей
  страны — с дуэнде? Напишите два предложения и пришлите их.»
  (3 lines @19) — drops «когда-нибудь» (ever) and rephrases «обладает
  дуэнде» as «— с дуэнде?»; keeps «два» and «пришлите их». Rendered
  at 19 (eh + para).
- P2 your-turn: 7 lines @20 — no fix (P2 col3 1080.0, same as de).
  P4 your-turn: 6 lines @20 — no fix (box ~1022.5, fixture table 1140).
- P2 C-intro (content12.py:275): «Прочитайте статью на странице 2 и
  выберите правильный ответ.» (2 lines) → «Прочитайте статью и выберите
  ответ.» (1 line @20.5).
- P5 B-bridge (content56.py:78): «Вставьте слова из рамки. Внимание:
  некоторые слова нужно проспрягать.» — already 2 lines @20.5, kept as
  harvested (like it/nl).
- P6 band: «Читать кампанию» → «Читать кампанию: дебаты, программы и
  опросы» (full sub in sans 18: 952.2 units, limit 1684 — fits).
- P8 header note: «К каждому ответу — короткое пояснение　✓ = задание с
  образцом» 635.6 units wide @19.5 → header 1302→1337, keys flow
  1328→1363.
- Letter parens full-width → half-width «(ejemplo, escrito por la
  redacción)» (content7.py:99).

### eh-formula incident (ru)

My first pre-fix pass changed the `, "sans", False, 20, CW - 44)) * 29`
pattern in content34.py with expect=2 — it matched BOTH the P3 eh line
(:45) and the P4 eh line (:132). P4's para still draws at 20, so the
mismatch would have made the P4 box too short for its 6-line text.
Caught by re-reading the file; P4's eh reverted to 20/*29. **Lesson:
when a substitution pattern occurs more than once in a file, check
whether each occurrence is really the one you mean — the count
assertion alone doesn't catch a same-pattern second site.**

## Builds

- **Build 1:** run rc=0, TOTAL 150; P2 col3 1080.0, P3 col3 1594.75,
  P4 col3 1022.5, P5 col3 1601.55, P7 col3 1865.51 (exactly the Latin
  target); P8-keys 13 overflows, ended y=2605 (45 over).
- **P8 diagnostic (ru):** 33 multi-line items vs core's 2 — the most of
  any edition so far (pt: 26). Writing type «Письмо» (content8.py:134).
  Tightened 27 notes to 1 line each (wrap-verified at 13.5); kept #1
  (frozen key + full-sentence note), #44/#139 (core-consistent),
  #137/#138 (keys alone fill the line; «См. оригинал.» is already
  minimal). Details:
  - #3/#9/#22/#65/#123 «Голосование по почте нужно запросить до 19-го
    числа» → «Заявка на голосование по почте — до 19-го» (5× — the
    shared note also feeds #9).
  - #4/#21/#29 «Международный день фламенко, понедельник, 16 ноября»
    → «День фламенко: понедельник, 16 ноября» (3×; #10 has a different,
    already-1-line note).
  - #30 «ЮНЕСКО: фламенко в наследии с 2010 года», #31 «Фламенко:
    пение, гитара и танец вместе», #32 «День святой Цецилии — 22
    ноября», #33 «Оркестр Бильбао: воскресенье, 22-го, 12:00»,
    #41 «Фламенко родилось из многих культур Андалусии»,
    #43 «Подлежащее, глагол», #45 «Место — впереди»,
    #56 «más + importante (борьба за титул)»,
    #57 «muchísimos = очень много болельщиков»,
    #68 «MiDNI — новый способ подтвердить личность»,
    #73 «identidad = удостоверение личности» (see §6.13),
    #80 «Голосование по почте — через Correos»,
    #82 «В этом году можно голосовать с MiDNI»,
    #88 «Только бесплатный эфир, с источником»,
    #92 «Опрос: фото с погрешностью на один день»,
    #126 «MiDNI — официальное приложение»,
    #133 «Сначала время, потом глагол»,
    #135 «Подлежащее, глагол, время»,
    #136 «Вопрос — в начале»,
    #137/#138 «См. оригинал.»,
    #149 «Во сколько закрывается участок?»,
    #150 «См. образец в разделе H (97 слов)».
  - Two reverts after the mass replace (see KIT §6.14): P7 FRASES quote
    translation restored to full form; #44 note restored to original
    (only #133 keeps the short form).
  - #73 measurement error (KIT §6.13): I first concluded the original
    note was 1 line because I only measured SHORTENED candidates; the
    diagnostic showed 2 lines. Fixed in build 2.
- **Build 2 (final):** run rc=0, 0 OVERFLOW/TOO WIDE, TOTAL 150;
  P8-keys y=2537 (23px spare).

## Gates (build 2)

- Render rc=0 (print 3,593,674 B; web 904,435 B). Occlusion 0 flags;
  sweeps 0/0; p8 extract 150/150, compare CLEAN, keydiff=[137, 138]
  adjudicated (re-aimed: Russian-sentence keys «Понедельник —
  Международный день фламенко. — См. оригинал.» / «В субботу мы
  смотрим севильское дерби. — См. оригинал.»); freeze tool 8 OK +
  direct sha256 8/8; pdftotext print = web, 53,128 B byte-identical;
  P8 min font 10.125pt (Tm min d 106.5); §1.1: paper #fbfaf6 ×8,
  VOL.4 ×9, VOL.5 ×3, chips A2 11 / B1 21 / B2 3 = 35 + band,
  Q113–150 all badged; full-width 0 in .py and SVG text; CJK only moth
  title (P1); gloss tokens all ≥2 (P1 reflexión 2; P2 mitin 2 / cartel 2 /
  escaño 2; P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 5; P4 parón
  2 / liderato 3; P5 papeleta 2 / censo 2 / plazo 3).

## Visual (8 PNGs, all clean)

- P1 gloss 1 line, clear of divider; masthead, pairing line, numbers
  box, quiz.
- P2 title «EL CALENDARIO　Календарь» fits, Note box clear, C-intro
  1 line, ¿Y TÚ? box 7 lines inside. (The «nunca «en las 21:00».»
  at the top of column 3 is the DECIR LA HORA paragraph's legitimate
  cross-column flow continuation, not an orphan.)
- P3 ¿Y TÚ? box 3 lines above divider; A-bridge 2 lines together;
  D-bridge 2 lines together.
- P4 ¿Y TÚ? box 6 lines above fixture table; A-bridge 2 lines together.
- P5 ¿Y TÚ? box 4 lines, 6.45px above divider (§6.11); B-bridge 2 lines
  together; C-bridge 2 lines together.
- P6 band subtitle full; A-bridge 2 lines together; D-bridge 2 lines
  together.
- P7 word-box gloss 2 lines; letter half-width parens; ed note 4 lines
  inside box; ERRORES notes 1 line each; banner well above footer;
  FRASES quotes + Russian translations all present.
- P8 RESPUESTAS header + note clear of swan caption; keys end well above
  footer; all 150 keys visible; Q113–120, Q145–149 chips present;
  #1 2 lines, #44/#139 2 lines, #137/#138 2 lines (all adjudicated);
  #150 ✓ form 1 line.

## 150-key verification

Full REG dump read (`es-ru-keys.txt`, 150 lines); matching sets verified
letter-by-letter: 25–28 (debate=дебаты c, mitin=митинг b, cartel=плакат d,
escaño=место в парламенте a), 52–55 (jornada=тур c, derbi=дерби b,
liderato=первое место a, fase liga=этап лиги d), 141–144
(sondeo=опрос c, muestra=выборка d, margen de error=погрешность b,
junta electoral=избирательная комиссия a).

## `.text.md`

1,875 lines, read end-to-end (Russian layer line by line; Spanish frozen
as in core); numbers 1–150 all present; 0 CJK; no «12 de noviembre».
Exported with `extract_text_es_ru.py` (copied from
`extract_text_es_nl.py`, sed es-nl→es-ru, grep-verified no residue).

## es-ru deliverables (all in `~/workspace/weekly-git/production/2026-w47/2026-w47-es-ru/`)

- `La-Lucerna-VOL4-es-ru.pdf` — 3,593,674 B,
  SHA-256 `1e727ff1d28dfcbaa04bf6835d873475c9080960edaae0650825b8be15925938`
- `La-Lucerna-VOL4-es-ru-web.pdf` — 904,435 B,
  SHA-256 `b88bfd2ce822603c0711e66ae61107e5c88975c7a9fb4b78246353f041e44877`
- `2026-w47-es-ru.text.md` (1,875 lines)
- `ABSTRACT.txt` (Russian, one line, no ASCII double quotes, 668 bytes)
- `WEEKLY-KIT.md` (adjudications §6.1–§6.16; 3-round self-proofread
  record; final round zero findings)
- 8 SVG in `svg/`, 8 PNG in `cards/`

**Self-check conclusion: zero known defects; awaiting independent proofreading.**

## Records

`scratch-fanout-es/es-ru.md` (this file), `es-ru-build1/2.log`,
`es-ru-render2.log`, `es-ru-freeze.log`, `freeze-es-ru-2/`,
`es-ru-keys.txt`, `extract_text_es_ru.py`, `2026-w47-es-ru-apply.json`;
`FANOUT-REPORT-es.md` updated (es-ru line added, checklist checked).
