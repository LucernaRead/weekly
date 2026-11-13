# WEEKLY-KIT — 2026-W47 es-ru (Испанский × Русский)

- Издание: `2026-w47-es-ru` — La Lucerna Spanish Weekly VOL.4, 16–22 ноября 2026.
- Язык читателя: русский (ru). Язык цели: испанский (es), текст заморожен из `core-es/`.
- Статус: **самопроверка готова, известных дефектов нет; ждёт независимой вычитки.**
- Строитель: fan-out builder (испанская семья), build 2 финальный, 2026-11-11.

## §1 Спецификация (из core-es, без изменений)

- 8 страниц, 150 упражнений (A2 50 / B1 72 / B2 28; по страницам 10/18/18/18/18/18/12/38).
- Шрифт ответов P8 13,5 ед. = 10,125 pt (мин. Tm d 106,5, как в core).
- Бумага #fbfaf6; мастхед 196 ед.; VOL.4 ×9 в SVG-тексте, VOL.5 ×3 (только
  законные отсылки к следующему выпуску).
- Чипы P8: A2 11 / B1 21 / B2 3 = 35 chip-rects + 1 #37402f rect шапки
  (в core те же 4 #37402f rects).
- Q113–150 все с бейджами; пропущенных чипов нет.
- Шрифты: Noto Serif/Sans с кириллицей (у Newsreader нет кириллицы);
  печать PDF больше латинских изданий (3,59 МБ против ~3,50 МБ) из-за
  кириллических подмножеств шрифтов.

## §2 Содержание по страницам (русский слой)

- P1 Portada: глосс ««Дебаты»: люди обсуждают публично.» (1 строка, §6.10);
  шапка «CADA SEMANA EN ESPAÑOL　ИСПАНСКИЙ ГЛАЗАМИ ИСПАНИИ»;
  pairing line «ТЕКСТЫ НА ИСПАНСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ
  РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ»; lead-глосс «ПЕРВАЯ НЕДЕЛЯ КАМПАНИИ　ДО ВЫБОРОВ
  13 ДНЕЙ».
- P2 Vida: полоса «Жизнь»; календарь «EL CALENDARIO　Календарь» (короткий,
  риска pt-§6.13 нет); Note «Пояснение — el debate = дебаты · el mitin =
  предвыборный митинг · el cartel = плакат · el escaño = место в
  парламенте.»; C-intro «Прочитайте статью и выберите ответ.» (1 строка).
- P3 Cultura: полоса «Культура»; Note со словами фламенко; your-turn
  3 строки @19 («Вы слушали фламенко? Какая музыка вашей страны — с
  дуэнде? Напишите два предложения и пришлите их.»).
- P4 Deporte: полоса «Спорт»; Note «Пояснение — la jornada = тур · el
  derbi = дерби · el liderato = первое место · el parón = перерыв · la
  fase liga = этап лиги.»; your-turn 6 строк @20.
- P5 Juventud: полоса «Молодёжь»; your-turn 4 строки @19 (§6.11);
  B-bridge «Вставьте слова из рамки. Внимание: некоторые слова нужно
  проспрягать.» 2 строки, как в harvest.
- P6 A fondo: полоса «Разбор»; подзаголовок «Читать кампанию: дебаты,
  программы и опросы» (полный sub в sans 18, 952,2 ед., лимит 1684).
- P7 Lengua: полоса «Язык»; глосс слова недели «debate = дебаты:
  публичное обсуждение; выборы — 29-го.» (2 строки); ERRORES все 4 по
  1 строке (§6.12); письмо с половинными скобками «(ejemplo, escrito por
  la redacción)»; примечание редакции 4 строки @19 (§6.8).
- P8 Ejercicios y respuestas: заголовок «Упражнения и ответы»; шапка
  RESPUESTAS на y=1337, поток ключей с 1363; правая пометка «К каждому
  ответу — короткое пояснение　✓ = задание с образцом» (635,6 ед. @19,5).

## §3 Замеренные итоги (build 2, финал)

- `run.py` rc=0, 0 OVERFLOW / 0 TOO WIDE, TOTAL 150.
- Концы колонок: P2 1080,0; P3 1594,75 (13 px над разделителем y=1608);
  P4 1022,5; P5 1601,55 (6,45 px над разделителем, §6.11); P6 1241,55;
  P7 1865,51 (точно как de/fr/it/pt/nl); P8-keys y=2537 (23 px запаса);
  P8-ex flow y=943.
- Render rc=0: печать `La-Lucerna-VOL4-es-ru.pdf` 3.593.674 B,
  SHA-256 `1e727ff1d28dfcbaa04bf6835d873475c9080960edaae0650825b8be15925938`;
  web `La-Lucerna-VOL4-es-ru-web.pdf` 904.435 B,
  SHA-256 `b88bfd2ce822603c0711e66ae61107e5c88975c7a9fb4b78246353f041e44877`.
- Occlusion-аудит: **0 flags**. Bridge-sweep: 0 сирот (20 bridges).
  Box-vs-hline-sweep: 0.
- p8 extract 150/150, compare CLEAN, keydiff=[137, 138] (§6.1).
- Freeze: tool 8 OK + прямая sha256 8/8 (build-copy/svg vs отправленный svg/).
- pdftotext print = web, 53.128 B, байт-в-байт.
- Мин. шрифт P8: Tm min d 106,5 (150 записей) = 10,125 pt, как в core.
- Полноширинная пунктуация: 0 в .py и в SVG-тексте (118 × U+3000 —
  разделитель заголовков, как в core).
- CJK: только наследованный заголовок мотылька «三色蛾» (P1, невидимые
  метаданные).
- Токены слов-глосс (§8.1-метод, по страницам, требуется ≥2): P1
  reflexión 2; P2 mitin 2 / cartel 2 / escaño 2; P3 cante 5 / toque 6 /
  baile 9 / compás 4 / duende 5; P4 parón 2 / liderato 3; P5 papeleta 2 /
  censo 2 / plazo 3.
- `.text.md`: 1.875 строк, прочитан полностью; номера 1–150 все на месте;
  0 CJK; нет «12 de noviembre».
- 150 ключей: полный REG-dump прочитан (`scratch-fanout-es/es-ru-keys.txt`);
  matching-наборы сверены побуквенно: 25–28 (debate=дебаты c,
  mitin=митинг b, cartel=плакат d, escaño=место в парламенте a),
  52–55 (jornada=тур c, derbi=дерби b, liderato=первое место a,
  fase liga=этап лиги d), 141–144 (sondeo=опрос c, muestra=выборка d,
  margen de error=погрешность b, junta electoral=избирательная
  комиссия a).

## §4 Источники (из core-es)

- Полный исходник core (bslib4.py, content*.py, render.py, run.py,
  svglib.py + assets/) через `apply_fanout.py ru`; переписан только слой
  объяснений. Испанский текст заморожен; ни новой trend-разведки, ни
  изменений фактов, ни изменений ключей.
- W46 es-ru как референс для имён типов («Письмо», «Перевод»,
  «Составьте предложение», «В/НВ») и harvest-конвенций.
- ru.json harvest (263 ключей), таблицы MANUAL/instr в `manual_table.py`.

## §5 Команды сборки

```
cd ~/workspace/weekly-git
# apply (один раз):
tools/venv/bin/python <scratch>/apply_fanout.py ru
# build:
tools/venv/bin/python run.py                     # в папке издания
tools/venv/bin/python render.py
tools/venv/bin/python tools/occlusion_audit.py svg
tools/venv/bin/python tools/p8.py extract --p8 svg/p8-ejercicios.svg --total 150 --json <scratch>/es-ru-p8-extract.json
tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-es/svg/p8-ejercicios.svg --edition-p8 svg/p8-ejercicios.svg --total 150
tools/venv/bin/python tools/freeze.py baseline --build . --core-svg ./svg --out <scratch>/freeze-es-ru-2
python3 <scratch>/sweep_de.py .
python3 <scratch>/extract_text_es_ru.py svg 2026-w47-es-ru.text.md
```

## §6 Адьюдикации

- §6.1 keydiff [137, 138]: переводные задания переориентированы
  (правило W45/W46). Ключи — русские предложения «Понедельник —
  Международный день фламенко.» / «В субботу мы смотрим севильское
  дерби.»; пометка «См. оригинал.» (обе). Не дефект.
- §6.2 #1 остаётся в 2 строки: замороженный ключ «13» + помета полным
  предложением («Кампания начинается в пятницу, 13 ноября, в полночь»);
  сокращать нечего (как de/pt/nl).
- §6.3 #44 и #139 остаются в 2 строки: wraps как в core
  («Время впереди, глагол вторым» / «pedir antes del jueves 19»).
- §6.4 #137 и #138 остаются в 2 строки: ключи сами по себе занимают
  строку; даже минимальная помета «См. оригинал.» даёт 2 строки.
  (Во fr/it/nl #138 стал 1 строкой; в ru оба ключа длиннее.)
- §6.5 P8-keys заканчиваются y=2537 — внутри потока (низ 2560).
- §6.6 Мотылёк `<title>Lucerna 三色蛾</title>` (P1): наследован из core,
  невидимые метаданные, оставлен без изменений (как во всех изданиях).
- §6.7 CW-44 и eh-формула (§6.8–§6.9 из es-nl): тексты боксов P7
  измерены на CW−44; wrap-размер в eh-формулах тоже менян с 20 на 19
  (content56.py:50, content34.py:45). P4-eh намеренно оставлен 20/*29:
  первая правка по ошибке поменяла и P4 (2 вхождения паттерна в
  content34.py), исправлено обратно — P4-параграф рисуется на 20,
  формула должна совпадать, иначе бокс станет короче текста.
- §6.8 Примечание редакции (P7): 4 строки @19 на CW−44, текст
  «Примечание редакции: к сдаче номера настоящих писем и лучших
  текстов не поступило; в этом выпуске — письмо-образец. Обещание — на
  VOL.5.» — с исправлением грамматики harvest: «к сдачи номера» →
  «к сдаче номера» (к + дательный падеж). P7 col3 = 1865,51, как у
  латинских изданий.
- §6.9 ERRORES: ВСЕ 4 пометы в harvest были по 2 строки на CW−44
  (fr: 2, nl: 2, ru: 4 — максимум; каждая лишняя строка +26,5 px):
  err1 «Час — единственное число: es.»; err2 «mejor уже
  сравнительная степень.» (без «: без más» — «Sin más» уже есть в
  испанской строке «→ «Es mejor.» Sin más.» выше); err3 «gente —
  единственное: глагол — тоже.» («глагол в единственном числе»
  не влезало; «gente — единственное число: глагол тоже.» тоже 2 строки);
  err4 «creo que утверждает: изъявительное.» (без « es.»).
- §6.10 P1-gloss (урок es-nl, применён сразу): измерен в sans 19 на
  gw: ««Дебаты»: люди обсуждают публично.» (356,6 ед., 1 строка).
  ««Дебаты»: два человека или больше обсуждают публично, по очереди и
  с вопросами.» — 2 строки.
- §6.11 P5 your-turn 4 строки @19 (BOX 1601,55; 6,45 px над
  разделителем): русский текст не укладывается в 3 строки без
  потрошения инструкции «Напишите два предложения и пришлите их.»
  (испробованы варианты с «Голосовать по почте или лично?» — 4 строки;
  единственный 3-строчный вариант срезал «и пришлите их»). 6,45 px —
  легальный зазор, как 7 px у de-P3. P3 your-turn — 3 строки @19
  («Вы слушали фламенко? Какая музыка вашей страны — с дуэнде?
  Напишите два предложения и пришлите их.»): «когда-нибудь» (ever) и
  «обладает дуэнде» → «— с дуэнде?» сокращены, «два» и «пришлите их»
  сохранены (вариант с «когда-нибудь» — 4 строки, пересёк бы
  разделитель).
- §6.12 P2 C-intro 1 строка («Прочитайте статью и выберите ответ.»);
  P5 B-bridge 2 строки, как в harvest (как it/nl — 2-строчный B-bridge
  не сиротит; сокращать только при 3 строках).
- §6.13 P8-диагностика: 33 многострочных пункта в build 1 — максимум
  среди изданий (pt: 26). Сокращены 27 помет до 1 строки; остались
  только §6.2–§6.4. Ошибка измерения #73: я сперва решил, что оригинал
  «documento de identidad = документ, удостоверяющий личность» — 1
  строка, потому что измерял только СОКРАЩЁННЫЕ варианты; диагностика
  показала 2 строки. Итог: «identidad = удостоверение личности»
  (1 строка).
- §6.14 Массовые замены помет P8: повторяющиеся пометы заменены везде
  («Голосование по почте нужно запросить до 19-го числа» — 5×, включая
  #9; «Международный день фламенко, понедельник, 16 ноября» — 3×,
  у #10 другая помета). Два отката после проверки: (а) перевод
  FRASES-цитаты на P7 («Опрос — это фото с погрешностью, сделанное в
  конкретный день.») НЕ сокращается — это золотое предложение, не
  P8-помета; (б) помета #44 возвращена к оригиналу
  («Время впереди, глагол вторым»), сокращена только #133 — core-
  consistent wrap #44 должен остаться побайтово тем же.
- §6.15 P2 your-turn 7 строк @20 (col3 1080,0 — как de 1080,0);
  P4 your-turn 6 строк @20 (бокс ~1022,5, таблица 1140) — без правок.
- §6.16 Тип письменного задания для P8-диагностики: «Письмо»
  (content8.py:134 — ✓-форма).

## §7 Раунды самопроверки

- Раунд 1 (build 1): P8-keys 13 overflows, конец y=2605; P7 col3
  1865,51; P5 col3 1601,55; P3 col3 1594,75. Диагностика: 33
  многострочных P8-пункта.
- Раунд 2 (build 2): 27 помет сокращены (+#73); run 0 overflow;
  P8-keys y=2537; render ok; occlusion **0 flags**; sweeps 0/0;
  p8 CLEAN; freeze 8/8; pdftotext идентичен.
- Раунд 3 (финал): 8 PNG прочитаны визуально; 150 ключей прочитаны;
  .text.md 1.875 строк прочитан полностью; §1.1 замерен; токены
  глосс; **ноль находок**.

## §8 Поставки (все в `production/2026-w47/2026-w47-es-ru/`)

- `La-Lucerna-VOL4-es-ru.pdf` — 3.100.959 B,
  SHA-256 `c4732fd0f2ab07d8d4ed834ab5b2356f58ab0f9f592220bf032b960035cc9bf3`
  (fix-esru-f1, 2026-11-13; pre-fix 3.100.944 B `d383753b4862…`, see below)
- `La-Lucerna-VOL4-es-ru-web.pdf` — 950.846 B,
  SHA-256 `cc549a5a212afc4960038720aae88468041562f031b96ea81292c70033fb5551`
  (fix-esru-f1, 2026-11-13; pre-fix 950.823 B `b6246122f94d…`, see below)
- `2026-w47-es-ru.text.md` (1.875 строк)
- `ABSTRACT.txt` (русский, одна строка, без ASCII-двойных кавычек)
- `WEEKLY-KIT.md` (этот файл)
- 8 SVG в `svg/`, 8 PNG в `cards/`

## §9. 重建（re-fanout，2026-11-11 — core build 10）

Core baseline: core-es fix build 10 (independent re-proof (a), zero findings) — print 17,212,955 B SHA `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`, web 1,410,471 B SHA `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`, text.md 1,822 lines SHA `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`.
Method: old edition backed up to `scratch-refanout-es/backup-old/` (verified identical), deleted, re-applied via `scratch-fanout-es/apply_fanout.py`; `classify.py` diffed fresh sources against the backup line by line — KEEP = core build-10 change, REVERT = edition hand fix restored, MERGE = derbi letter line (fresh sábado + backup ASCII parens), INSERT = RTVE debate-a-ocho timeline row. No commit, no push.
Common core changes kept: C1 (P1 CINCO CLAVES box 700→720), C2 (`antes del jueves`→`hasta el jueves`), es-ja D1 (consejo completed) + D4 (derbi sábado 21st), es-nl D1/D2, es-pt C2 (PCTE kept, 195 kept). C3 (P5 vocab `content56.py:79`) left as-is per adjudication.
Gates (all green unless noted): run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; render rc=0; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated — translation items keyed by target-language sentence); freeze 8/8 SVGs byte-identical; freeze-diff CJK accounting clean; canonical creambox.py full scan 0 own-ink overflow (the 6 raw negative lines per edition are the known below-box headings, identical to core); creambox_diag 0 own-ink negatives; boxtitle 0 overflow; keycheck 149/150 (only the #150 open-question `✓` exception); sweep 0 orphans / 0 box-vs-hline; pdftotext print = web bytes; P8 min effective font 10.125pt (≥ 9.75pt floor).
Classify: KEEP 17 / REVERT 45 / MERGE 1 / INSERT 1 / DELETE 0. Build: run1 rc=0, TOTAL 150, P8-keys y=2537. New print 3,593,735 B SHA `68a761681e7d760174eed1554672b7c3664cfbbef16bc89538543202bc3414b5`; web 941,922 B SHA `e6281174237fe2bd31fb749fe7bc9bd76055933a632ec8b20d3081556171aaab`; text.md 1,893 lines SHA `05e7d6c91fa331618985a9d9bfae6564c1d596321227d002e4ff92e26a25c6aa`; print/web text 117,979 bytes, identical.
Hand fixes re-applied: D1 — P3 ¿Y TÚ? box eh +20→+25 (true-ink clearance +2.7px; crop verified, ink inside). D2 — P5 same box eh +20→+25 (true-ink +2.7px; capped by the y=1608 divider, 1.5px gap — cannot extend further; crop verified). D3 — P7 box title `ERRORES TÍPICOS　Типичные ошибки` → `…　Ошибки` (was +44.7px; boxtitle 0 overflow; crop verified).
Keycheck: 148/150 — #150 is the expected open-question `✓` exception; #137 is an extractor false positive, adjudicated (same item as p8-compare keydiff [137, 138], old KIT §6.1): the Russian translation sentence `Понедельник — Международный день фламенко.` uses the em-dash as a copula, which `p8.py` splits as key—note; the rendered P8 crop shows the full sentence printed followed by `См. оригинал.` — not a defect.

## D5 重建记录（2026-11-12，B档）

- 安装：`mechanism/apply_variant.py --svglib <本版>/svglib.py --target es --reader ru`（mode ru）；`svglib.py` md5 `6a46ee51…` → `74f3fb03…`（安装器同时补 port 了 fix2）；路由断言说明：`route_assert.py` 的 3 个 FAIL 是脚本局限（其前三项检查无条件要求拉丁/数字 sans → `news`，与其自身的 ru 模式检查矛盾），非真实缺陷——实际路由已核实：`_D5_READER='ru'`，拉丁/西里尔/数字 sans → `sans_noto`，U+201C/U+2019 → `news`，CJK → `sans`，serif → `news`；机制 `test_d5_routing.py` FAILURES: 0；普查 Noto Sans 元素 768 个（ru 路径确实触发）。
- 预修 3 项共用版式（与 core-es 相同西班牙语串、同栏宽）：P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt、P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt、P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。
- 逐项修 3 项（均为 D5 新缺陷，修前基线 0）：① P1 正文行 `Пять главных тем　Para entender la semana` 右超 +16.1px（boxtitle BODY DEFECT 与 creambox DEFECT 一致确认）——19→18pt；② P7 页脚：俄语编者注 `ldcn` 在 Noto Sans 下由 4 行变 5 行（+27px），把底部 `LA PRÓXIMA SEMANA` 通栏顶进页脚（occlusion FOOTER+LINEX 同源）——`ldcn` 19→18pt（高度公式与绘制两处同改），通栏回到基线位置；③ P8 TEXTX：图注 credit `Pluma de cisne — dominio público (Wikimedia Commons)` 在 Noto Sans 下 416.2→426.0px，超栏宽 422.5 折成两行，第二行 `Commons)` 与 y=1337 的 RESPUESTAS 标题行相撞——`bslib4.caption()` 增加可选参数 `csize`（默认 15.5），P8 此处调用传 `csize=14.5`（398.5px，恢复一行）。以上文字均未动。
- 门禁全绿：run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0（`head_check.py` PASS 0 defects）；render rc=0；D5 普查 0（D5 0/0，curly_in_cjk 0，curly_total=0）；U+201C 普查（`census_quotes.py`）0；occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，仅读者语译注差异）；boxtitle 0 DEFECT；creambox（仓内 `tools/d5_creambox_audit.py`）PASS 0 defects（P8 250 行、页脚余量 36.4px 不变）；spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es：新增 CJK 字符 0；印/网文字层 44,167 字符、8,076 词一致。
- 新 PDF：印刷版 3,213,677 B SHA `707b82670349ab43cc2923388335063001864320ee7b34b002114c12fa273619`；网页版 1,062,147 B SHA `a0889431bde27466d78a63ba7ec67bc6c0ac299063de3f5ff03d22f246f692c8`。`text.md` 字节不变（SHA `05e7d6c9…`）。日志：`hidden_files/w47/scratch-d5-rebuild-es/2026-w47-es-ru/`。

## es 家庭修复 F2/F3/F4（2026-11-12，独立重校 PROOF-NOTE (b) 返修）

- 改动：F2（P6 时间轴措辞：`(sin el PSOE)` → `(sin el PSOE confirmado)`）＋ F4（P2 日历框俄语注释缩短 5 行：30→25 行，DECIR LA HORA 标题上移 107pt，尾行 `nunca «en las 21:00».` 回到同栏 (403.9, 1052.9)，目视确认；本版事后由跨家 *-ru 工人重渲染一次字体路由）。F1（缺首字下沉）按协调员裁定不修：全刊引擎级缺口，进模板 backlog，见 FIX-LOG。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0 → text.md 更新（core-es 为 D5 工具重导出；其余 10 版手术替换，diff 只含意改行；ru F4 另做词级手术，见 FIX-LOG 陷阱核查节）。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 B，SHA-256 `0ca1beca6d7498103b7d36fc27c4946cfdc0276606935ad8b80c0ae9c796e32c`；网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 B（< 7 MB），SHA-256 `2febbe24084bff7e022d937e506df8b1866d211a752936a268194623b09997ae`；text.md `2026-w47-es-ru.text.md` 52,347 B，SHA-256 `dadb3e8478e5d06d970e60f62dbd9d958944e28b9b1bc64c541b77cca9571b5a`。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs 新 core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 30 titles, 372 body lines，0 DEFECT；spill 0 SPILL（27 盒，72 candidates）；edge 0 TOUCH / 0 NEAR；D5 census PASS（弯引号全在 Newsreader）；freeze baseline 8/8；印/网 pdftotext 53,420 字节逐字节一致。
- 日志：`hidden_files/w47/scratch-fix-es/`（FIX-LOG.md、build-all.log、build-resume.log、gates-all.log、text-pre/）。

## 第二轮独立重校修复 G3（2026-11-12，PROOF-NOTE-2 (b) 返修）

- 改动：G3（仅 text.md 两处碎片错位，印/网 PDF 均正确、无需重渲）：`2026-w47-es-ru.text.md` L208 孤立行 `nunca «en las 21:00».` 移回 DECIR 段尾（L327，DECIR 标题 L321 起 6 行内，与其余 10 版一致）；L327 错置的 `пришлите их в редакцию.` 移回 P2 ¿Y TÚ? 框俄语说明尾（L300，`предложения по-испански и` 之后）。行数不变（1888 行）。重生成路径已试行并否决：D5 导出器干跑重分段 299 行、首行误标为 core-es slug，且两处碎片仍错位（干跑中两行相邻于 DECIR 段后），故改用行号锚定手术换回两行，见 FIX-LOG-2 机制节。
- 未重渲：印 PDF 与网 PDF 未动，SHA 不变（印 `0ca1beca6d74…`、网 `2febbe24084b…`，见下）；text.md 与印 PDF 文字层已核对一致（印 PDF 文本层：DECIR 尾行 `nunca «en las 21:00».` 在 DECIR 段内、¿Y TÚ? 尾句 `пришлите их в редакцию.` 在框内）。
- 文件：印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 B，SHA-256 `0ca1beca6d7498103b7d36fc27c4946cfdc0276606935ad8b80c0ae9c796e32c`（未变）；网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 B（< 7 MB），SHA-256 `2febbe24084bff7e022d937e506df8b1866d211a752936a268194623b09997ae`（未变）；text.md `2026-w47-es-ru.text.md` 52,347 B（字节数未变，仅两行换位），SHA-256 `8a57918fc0f9baf0de43b0f920f7ff25272b74e90b94a0c60aeea435673db701`（改前 `dadb3e8478e5…`）。
- 门禁全绿（PDF 未动，门禁重跑确认无回归）：occlusion 0 flags；p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 30 titles, 372 body lines，0 DEFECT，0 OBSERVE，0 marginal；spill 0 SPILL（27 盒，72 candidates，72 OBSERVE）；edge 8 页 0 TOUCH / 0 NEAR；D5 census PASS（弯引号 U+201C/U+201D 全版 0）；freeze baseline 8/8；印/网 pdftotext 53,420 字节逐字节一致；P8 答案 1–150 全有。
- 日志：`hidden_files/w47/scratch-fix2-w47-es/`（FIX-LOG-2.md、gates2.log、text-pre/）。

## 第三轮独立重校修复 H1（2026-11-12，PROOF-NOTE-3 (b) 返修）

- 改动：H1（es-ru 称呼混用，低）：P1 栏目头 `AHORA TÚ　Теперь ты` 用 ты 体，与全版其余称呼（`А вы?` ×4、框内 37 处 вы 词形）不一致；改动最小的一致化——栏目头 `Теперь ты` → `Теперь вы`（1 处；正文 вы 体不动）。源头：`2026-w47-es-ru/content12.py:51`，`f.head("AHORA TÚ　Теперь ты", 25)` → `f.head("AHORA TÚ　Теперь вы", 25)`。其余 10 版未动。
- 重建：`run.py` rc=0（TOTAL 150）→ `render.py` rc=0（一次通过，无中断）→ text.md 手术替换 L147 一行（先断言原文再替换；未整版重导出——D5 导出器干跑 1866 行 vs 已装 1888 行、diff 200 行重分段，见 FIX-LOG-3；意改在干跑 L138 在场）。SVG 内 `Теперь вы` ×1、`Теперь ты` 0。
- 文件：印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,213,297 B，SHA-256 `538ca756749a2bd57760b6bf9c5cc370aefeef11f4ba1e9f409073ba60a33d2d`（改前 `0ca1beca6d7498103b7d36fc27c4946cfdc0276606935ad8b80c0ae9c796e32c`，+1 B）；网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,847 B（< 7 MB），SHA-256 `8d440e9b52cf9a157755ec223b5cd160b86d8a7a62a5ff3eca1ac9f8aac61a3d`（改前 `2febbe24084bff7e022d937e506df8b1866d211a752936a268194623b09997ae`，+30 B）；text.md `2026-w47-es-ru.text.md` 52,367 B（I1 +18 B，J1 +2 B）、1888 行，SHA-256 `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b`（改前 `6f89a108c8fdb314083cb44f7e8b34b409b4d9dab50b1e2af1f5b0b18bc240a6`）。印/网各 8 页；印/网 pdftotext 53,420 字节逐字节一致。
- 核对：text.md 词边界 `\bты\b` 0 处（Python re；grep -P 的 `\p{L}` 计数 15 为工具假象，命中均为 дебаты 等词内子串——已用 Python 逐行核对，唯一独立词即 L147 改前处）；`А вы?` 仍 ×4；`Теперь вы` text.md 1 处、印/网 PDF 文字层各 1 处（pdftotext；PyMuPDF 抽取将全角空格省去、呈 `Теперьвы`，`Теперьты` 0）；U+201C/U+201D 全版 0。
- 门禁全绿：occlusion 0 flags；p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；boxtitle 30 titles, 372 body lines，0 DEFECT，0 OBSERVE，0 marginal；spill 0 SPILL（27 盒，72 candidates，72 OBSERVE）；edge 8 页 0 TOUCH / 0 NEAR（日志行 "1 touch/near-lines" 为汇总行本身含关键词的计数假象，edge JSON 实为 0/0）；D5 census PASS（弯引号 U+201C/U+201D 全版 0）；freeze baseline 8/8；P8 答案 1–150 全有。
- 日志：`hidden_files/w47/scratch-fix3-w47-es/`（FIX-LOG-3.md、gates3.sh、gates-all.log、run-es-ru.log、render-es-ru.log、text-pre.md、text-dryrun.md）。

## 第四轮独立重校修复 I1（2026-11-12，PROOF-NOTE-4 §2 返修）

- 改动：I1（text.md 专属，低）：两栏/两块拼接处丢空格致文字粘连；本版共 18 处（PROOF-NOTE-4 表列 7+7=14 处；机械穷举+印层逐一核验另得多 4 处同类粘连，见 FIX-LOG-4 §3）：分版粘连 11 处（驼峰粘连3 处、数字→大写粘连2 处、句号→大写粘连2 处、逗号粘连1 处、中点粘连1 处、句号→小写粘连1 处、右括号粘连1 处）；目录粘连 7 处（`Pág. 2La semana` … `Pág. 8Ejercicios y respuestas` → 各补空格）。
- 重建：未重建（PDF 未动）；text.md 手术替换 18 处（逐处先断言原文存在再替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 17 行，行数不变（1889 行）。
- 文件：text.md `2026-w47-es-ru.text.md` 52,365 B（I1 前 52,347 B，+18 B）、1889 行，SHA-256 `6f89a108c8fdb314083cb44f7e8b34b409b4d9dab50b1e2af1f5b0b18bc240a6`（改前 `ee9b53f788c85e8b28dd87ae99066552c04807bf8a6f04aa5124e582f1faa5b4`）；印/网 PDF 未动，SHA 不变（印 `538ca756749a`、网 `8d440e9b52cf`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）；D5 普查 PASS（弯引号 0/0 在 Newsreader）。
- 日志：`hidden_files/w47/scratch-fix4-w47-es/`（FIX-LOG-4.md、fix.py、fix2.py、fix-report.json、text-pre-*.md、gates4.sh、gates4.log、p8-extract/compare、census）。

## 第五轮独立重校修复 J1（2026-11-12，PROOF-NOTE-5 §3 返修）

- 改动：J1（text.md 专属，低）：小写词与小写词拼接粘连（I1 同类残留，第四轮 9 类模式与修复轮重扫均漏检）；本版共 2 处：`confinal` → `con final`（L1201，P6 Q88 C 尾 `con` + Q92 A 尾 `final`）；`unamuestra` → `una muestra`（L1201，Q92 C 首词 `una` + D 框次词 `muestra`）。
- 重建：未重建（PDF 未动）；text.md 手术替换 2 处（逐处先与同版印 PDF 文字层核对断句、再断言原文存在后替换，替换后断言旧串为 0；未整版重导出）；diff 只含意改行 1 行，行数不变（1889 行）。
- 文件：text.md `2026-w47-es-ru.text.md` 52,367 B（J1 前 52,365 B，+2 B）、1889 行，SHA-256 `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b`（改前 `6f89a108c8fdb314083cb44f7e8b34b409b4d9dab50b1e2af1f5b0b18bc240a6`）；印/网 PDF 未动，SHA 不变（印 `538ca756749a`、网 `8d440e9b52cf`）。
- 门禁：p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异）。
- 日志：`hidden_files/w47/scratch-fix5-w47-es/`（FIX-LOG-5.md、fix5.py、fix-report.json、text-pre-*.md、gates5.sh、gates5.log、p8-extract/compare、rescan.py、rescan.json）。

## fix-xru（2026-11-12，SOP §1.1）

- 改动：`svglib.py` 的 `_D5_READER == "ru"` 分支把拉丁文路由到 Noto Sans CJK，违反 SOP §1.1；分支已删（标记 `[removed 2026-11-12 fix-xru]`），恒走 else 逻辑——拉丁文 → Newsreader，西里尔文 → Noto Sans。
- 重建：`driver.sh es`（run.py rc=0，TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE；render.py rc=0；文字层字符多重集 pre/post 一致，35,160 非空格字符；webpdf.py rc=0，8 页）。
- 探针（SVG runs）：修前 LAT@NotoSans=3301 LAT@Newsreader=18633 CYR@NotoSans=4300；修后 LAT@NotoSans=0 LAT@Newsreader=21934 CYR@NotoSans=4300（不变）。8 个 SVG 全部已变。
- 文件：印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,100,942 B，SHA-256 `277b2d2695f8fb23354a1143828b391944916dab5550e83e56d4e8ca16441806`（改前 3,213,297 B `538ca756749a…`）；网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 950,829 B，SHA-256 `985368280784e08e1fd37e306c6ff4cba40fb0c356083dd5a91b0cd48de958df`（改前 1,061,847 B `8d440e9b52cf…`）；text.md 未变，52,367 B，SHA-256 `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b`。无重试。

## fix-es-ru2（2026-11-12，*-ru 扫查 boxtitle 回归 1 处）

- 缺陷：扫查（`hidden_files/w47/scratch-sweep-xru-occl-2/SWEEP-LOG.md`）发现 P1 框标题 `LA SEMANA EN CIFRAS　В цифрах` 右溢 +22.3px（core −18.0，回归；ink_r 983.3，框右界 961.0）。根因：fix-xru 把拉丁文改走较宽的 Newsreader，标题变宽。
- 改动：仅降字号、不改措辞——`content12.py:46`，`f.box("LA SEMANA EN CIFRAS　В цифрах", …)` 加 `tsize=21`（默认 23pt）。实测（工具自带 ink 数学）：23pt +25.1px、22pt 仍 +5.6px、21pt 余 11.9px，循 de-fr 的 D5 先例（同类标题 23→21pt）。措辞、字号其余处均未动。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0（印 + 网一次生成）。SVG diff：仅 p1-portada.svg 变，p2–p8 字节一致。
- 文件：印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,100,944 B，SHA-256 `d383753b48628ce402c7c91d082e8596f7d8472c93eb21acbe84f6c2938fe5f5`（改前 3,100,942 B `277b2d2695f8…`，+2 B）；网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 950,823 B，SHA-256 `b6246122f94d949c61cd67aec16ee17194355981d486a8fd8b3b020db56bb544`（改前 950,829 B `985368280784…`，−6 B）；text.md 未变（措辞未改，无需重导出），52,367 B，SHA-256 `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b`。印/网各 8 页。
- 门禁全绿：boxtitle 0 DEFECT（rc=0；注：标题 21pt 低于工具 22pt 检测下限，38 titles 计为 BODY——同 de-fr 情况，改用直接测量核实：重建后 SVG 标题三段 ink_r 最大 946.3px，框右界 961.0，余 14.7px）；occlusion 0 flags（自检通过）；spill 0 SPILL（27 盒，149 candidates）；edge 8 页 0 TOUCH / 0 NEAR；p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异，同前）；D5 census 探针与修前一致（LAT@Newsreader=21934，CYR@NotoSans=4300，CJK+CYR=555，路由未动）；文字层字符多重集修前/修后一致（35,160 非空格字符），印/网 pdftotext 各 53,413 B、多重集一致；freeze baseline 8/8 SVGs byte-identical；creambox 差分（修前基线 vs 修后）PASS 0 defects（仅 P1 有 diff/moved，系标题降字号 + 框矮 2px 所致；p2–p8 diff 0）。
- 日志：`hidden_files/w47/scratch-fix-es-ru2/`（FIX-LOG.md、measure_title.py、title-direct-measure.log、build-run/render.log、boxtitle/occlusion/spill/edge/p8/creambox/freeze 日志、pre/post SHA 与文字层）。

## fix-esru-f1（2026-11-13，第七轮独立重校 PROOF-NOTE-7 F1 返修）

- 缺陷：P5 EJERCICIOS 分隔线（y=1608，全宽）横穿 ¿Y TÚ? 奶油框，框底 1633.55，超出分隔线 25.55px；框内俄文末行 `пришлите их.`（基线 1626.59）被绿线隔在框外一侧。字形未被线划过，文字全可读。8 页横扫仅此一处。溯源：框高随字体改道逐次变高（303.0 → 329.0 → 356.0），分隔线 y=1608 未动。
- 改动：纯几何修，不改文字、不动分隔线、不动其他页——`content56.py` ¿Y TÚ? 框：标题→正文间距 52→46、西语行距 1.42→1.38、西→俄块间距 10→2、俄文首行偏移 20→12、俄文行距 1.42→1.30；字号不变（西语 21.5pt、俄文 19pt），折行不变（西语 4 行、俄文 5 行）。框高公式改按实际绘制偏移推导（`eh = ru_last + 7`），不再用旧启发式（62 + … + 25），防公式与绘制再漂移。
- 实测（修前印 PDF 直接测量）：框底 1633.55、分隔线 1608、超出 25.55px；修后 SVG/PDF 双重实测：框高 356.0→321.48（省 34.52px）、框底 1599.03、距分隔线 8.97px；末行俄文基线 1592.03（距线 15.97px），框内文字完整可读。P5 放大裁图前后对照已目视确认：分隔线与框无交叉。
- 重建：`run.py` rc=0（TOTAL 150，0 FLOW OVERFLOW / HEAD TOO WIDE）→ `render.py` rc=0（印 + 网一次生成）。SVG diff：仅 p5-juventud.svg 变，p1–p4、p6–p8 字节一致。
- 文件：印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,100,959 B，SHA-256 `c4732fd0f2ab07d8d4ed834ab5b2356f58ab0f9f592220bf032b960035cc9bf3`（改前 3,100,944 B `d383753b4862…`，+15 B）；网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 950,846 B，SHA-256 `cc549a5a212afc4960038720aae88468041562f031b96ea81292c70033fb5551`（改前 950,823 B `b6246122f94d…`，+23 B）；text.md 未变（措辞未改，无需重导出），52,367 B，SHA-256 `ac246f8709d3535958ccebb3b6913800bd3866001de5322358d3ba026f69c42b`。印/网各 8 页。
- 门禁全绿：D5 census PASS；occlusion 真实审计 0 flags（自检另行通过，仅作 sanity check）；boxtitle 0 DEFECT（38 titles / 584 body lines）；spill 0 SPILL（27 盒，149 candidates）；edge 8 页 0 TOUCH / 0 NEAR；p8 extract 150/150，compare vs core-es CLEAN（keydiff=[137, 138]，读者语翻译题应有差异，同前）；freeze baseline 8/8 SVGs byte-identical；印/网文字层逐字节一致（pdftotext 53,414 B；`-layout` 113,438 B；修前 53,413 B 的 +1 B 为 pdftotext 行分组随行距重排所致，文字未变，text.md SHA 不变）。
- 日志：`hidden_files/w47/scratch-fix-esru-f1/`（FIX-REPORT.md、gates-fix.sh / gates-fix.log、各门禁日志与 JSON、p5-before/after PNG 与 zoom 前后对照图、svg-before.sha256、印/网文字层）。
