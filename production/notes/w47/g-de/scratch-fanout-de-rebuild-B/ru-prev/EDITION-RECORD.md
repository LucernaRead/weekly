# EDITION-RECORD — 2026-w47-de-ru (German for Russian readers)

Builder: de fan-out builder, 5th shift, 2026-11-11. Source: core-de build14
(sha `9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4`).
Transform: `transform.py ru` (transform-ru2.log for the final build).
Measure: `measure.py ru` — 24/24 PASS (ru/measure2.log).
Build: `build_edition.py ru` — rebuild 2, 2026-11-11 06:52–06:57 UTC
(ru/rebuild2.log, ru/build.log). Build 1 superseded (see §3).

## §1 Deliverables (rebuild 2, final)

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-ru.pdf` (print) | 10,954,755 | `74fac6aa22cf181614ff3fb40f267547f54859bcd072bc3dc17f78cc0ca9144e` |
| `Die-Lucerna-VOL4-de-ru-web.pdf` (web, < 7 MB) | 1,605,334 | `8f9b83e799ed2afafb96e94e862e434f487803203143f7cc7f1fafd3b1a664cf` |
| `2026-w47-de-ru.text.md` | 56,232 (47,595 chars, 591 entries, 150 ex.) | `e5d6bd0ba28ec910f83155c2cda4b38423a2000419c142ddd36d42e2bafcde16` |
| `ABSTRACT.txt` | 688 | one line, Russian, no ASCII `"` |
| `WEEKLY-KIT.md` | 15,097 | this edition's KIT (rebuild-2 values) |

8 SVGs in `svg/`; build interpreter `tools/venv/bin/python` (PIL 13.0.0).

## §2 Gates (rebuild 2) — ALL PASS

- `run.py`: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 1023, P2-ex 2332, P3-main 946, P3-ex 2363, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 /
  B1 1342 / B2 1306, P8-battery 1409, P8-keys 2545 (bottom 2560, spare 15px).
- `measure.py`: 24/24 PASS, 0 FAIL.
- `verify.py`: TOTAL 150; numbering continuous; SVGs byte-identical after
  re-run; SOP §1.1 audit True; verbatim OK; P8 floor True; 17 forbidden terms absent.
- `occlusion_audit.py`: 0 flags.
- `p8.py`: extract 150/150; compare `status: CLEAN missing=[] extra_count=0
  keydiff=[137, 138, 139, 150]` — expected (137–139 forward translations,
  150 open writing task; Q140 reverse item correctly does NOT diff).
- `freeze.py` diff: exit 0; added CJK 7, all U+3000 (1/page P2–P8, 0 on P1).
- `freeze_direct.py`: RC 0; source PASS (0 unaccounted removed/added;
  core 2556 / edition 2564 literals, removed 520 / added 528); rendered 8/8,
  frozen 149/163/198/166/179/175/160/187, sha8 73347f49 / 689045ad / 973ce090 /
  df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / 7016818d — P2/P4/P6 sha8 identical
  to the Latin editions; P1/P3/P5/P7/P8 differ with HIGHER frozen counts
  (more rendered text elements in ru, P1 207 vs 178 — extra pure-German lines
  coincide with core lines; segmentation, not content).
- Print/web text layer: default word multiset identical (print 57,611B /
  web 57,614B); `-raw` normalised identical (56,408B both).
- Chips: per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0.
- P8 min font: 9.94pt (≥ 9.75pt floor).
- U+2019 scan over 8 SVGs: 0.
- 150-key check (`ru/keycheck-150.json`): 149/150 exact; Q150 PREFIX (expected,
  see §4). RC 0.
- Box titles (SVG scan, 8 instances): all end ≤ 1862.0 (max 1853.4 LESERBRIEFE
  "Письма читателей", 8.6px margin).
- Visual proofread: P1–P8 re-rendered from the print PDF at 100 dpi and viewed
  (/tmp/ru2-proof-*.png). **Zero findings.** P5 re-checked in detail after the
  build-1 fix: 1903 calendar image + caption clear of the ÜBUNGEN header,
  Q68 back in column 1, Q82 clear of the footer.

## §3 Build history

- **Build 1** (~06:48–06:52 UTC): 3 gate failures — FLOW OVERFLOW [P5-ex]
  (flow ended y=2682, 122px over) + occlusion 3 flags on p5-jugend.svg
  (caption 2nd line on the ÜBUNGEN header rule — TEXTX; Q82 line crossing
  the footer hline — LINEX). Causes measured in the SVGs: (1) the P5
  section-A instruction wrapped to 2 lines (+30px per A question, Q68 pushed
  out of column 1); (2) two P5 vocab-box entries wrapped to 2 lines at the
  377.5px box width in serif 21.5pt ("der Wunschzettel — список желаний"
  380.6px, "das Christkind — Младенец Христос" 382.3px), adding ~61px to the
  col3 stack and driving the image into the header.
- **Fixes** (vals_ru.json, 3 values, tr_ru.py diff exactly 3 lines):
  instruction → "Прочитайте стр. 5 и выберите ответ." (1 line);
  "das Christkind — Младенец Христос" → "das Christkind — Младенец";
  "der Wunschzettel — список желаний" → "der Wunschzettel — желания".
  Box titles shortened in the same round (Тишина / Слова / Адвент / Справка).
- **Rebuild 2** (06:52–06:57 UTC): ALL GATES PASS. Vocab ends 979.36 (= it),
  image ends 1732.93 (= it), P5-ex ends 2441 (= core). ru complete.

## §4 150-key table

Source: `ru/keycheck-150.json` (P8-SVG-extracted keys vs REG from the edition's
own sources). 149/150 exact. The single non-exact item is Q150, the open writing
task — the extractor truncates the REG key to its first clause; expected, and
Q150 is already in the p8-compare keydiff set.

| # | Pg | Level | Type | REG key | P8-extracted | Match |
|---|---|---|---|---|---|---|
| 1 | 1 | A2 | дополнение | Bundesliga | Bundesliga | OK |
| 2 | 1 | A2 | дополнение | Niederlande | Niederlande | OK |
| 3 | 1 | A2 | дополнение | Sachsen | Sachsen | OK |
| 4 | 1 | A2 | дополнение | Totensonntag | Totensonntag | OK |
| 5 | 1 | B1 | дополнение | fünf | fünf | OK |
| 6 | 1 | B1 | дополнение | 29. November | 29. November | OK |
| 7 | 1 | A2 | выбор ответа | B | B | OK |
| 8 | 1 | A2 | выбор ответа | A | A | OK |
| 9 | 1 | A2 | выбор ответа | B | B | OK |
| 10 | 1 | A2 | выбор ответа | B | B | OK |
| 11 | 2 | A2 | дополнение | 18. November | 18. November | OK |
| 12 | 2 | A2 | дополнение | 22. November | 22. November | OK |
| 13 | 2 | A2 | дополнение | 29. November | 29. November | OK |
| 14 | 2 | A2 | дополнение | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | дополнение | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | преобразование | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | преобразование | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | преобразование | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | преобразование | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | преобразование | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | выбор ответа | B | B | OK |
| 22 | 2 | A2 | выбор ответа | B | B | OK |
| 23 | 2 | A2 | выбор ответа | A | A | OK |
| 24 | 2 | A2 | выбор ответа | B | B | OK |
| 25 | 2 | A2 | подбор слов | d | d | OK |
| 26 | 2 | A2 | подбор слов | c | c | OK |
| 27 | 2 | A2 | подбор слов | a | a | OK |
| 28 | 2 | A2 | подбор слов | b | b | OK |
| 29 | 3 | A2 | верно или нет | Richtig | Richtig | OK |
| 30 | 3 | A2 | верно или нет | Falsch | Falsch | OK |
| 31 | 3 | A2 | верно или нет | Richtig | Richtig | OK |
| 32 | 3 | B1 | верно или нет | Falsch | Falsch | OK |
| 33 | 3 | A2 | верно или нет | Richtig | Richtig | OK |
| 34 | 3 | A2 | дополнение | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | дополнение | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | дополнение | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | дополнение | Advent | Advent | OK |
| 38 | 3 | A2 | дополнение | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | выбор ответа | B | B | OK |
| 40 | 3 | A2 | выбор ответа | B | B | OK |
| 41 | 3 | A2 | выбор ответа | A | A | OK |
| 42 | 3 | B1 | выбор ответа | A | A | OK |
| 43 | 3 | A2 | составление предложений | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | составление предложений | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | составление предложений | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | составление предложений | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | выбор ответа | B | B | OK |
| 48 | 4 | B1 | выбор ответа | B | B | OK |
| 49 | 4 | B1 | выбор ответа | C | C | OK |
| 50 | 4 | B1 | выбор ответа | A | A | OK |
| 51 | 4 | B1 | выбор ответа | B | B | OK |
| 52 | 4 | B1 | подбор слов | d | d | OK |
| 53 | 4 | B1 | подбор слов | b | b | OK |
| 54 | 4 | B1 | подбор слов | c | c | OK |
| 55 | 4 | B1 | подбор слов | a | a | OK |
| 56 | 4 | B1 | дополнение | mehr | mehr | OK |
| 57 | 4 | B1 | дополнение | später | später | OK |
| 58 | 4 | B1 | дополнение | früher | früher | OK |
| 59 | 4 | B1 | дополнение | mehr | mehr | OK |
| 60 | 4 | B1 | выбор ответа | A | A | OK |
| 61 | 4 | B1 | выбор ответа | B | B | OK |
| 62 | 4 | B1 | выбор ответа | C | C | OK |
| 63 | 4 | B1 | выбор ответа | A | A | OK |
| 64 | 4 | B1 | выбор ответа | B | B | OK |
| 65 | 5 | B1 | выбор ответа | A | A | OK |
| 66 | 5 | B1 | выбор ответа | B | B | OK |
| 67 | 5 | B1 | выбор ответа | B | B | OK |
| 68 | 5 | B1 | выбор ответа | B | B | OK |
| 69 | 5 | A2 | выбор ответа | A | A | OK |
| 70 | 5 | B1 | дополнение | Türchen | Türchen | OK |
| 71 | 5 | B1 | дополнение | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | дополнение | Christkind | Christkind | OK |
| 73 | 5 | B1 | дополнение | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | дополнение | Kerze | Kerze | OK |
| 75 | 5 | A2 | дополнение | Stern | Stern | OK |
| 76 | 5 | B1 | преобразование | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | преобразование | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | преобразование | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | преобразование | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | верно или нет | Richtig | Richtig | OK |
| 81 | 5 | B1 | верно или нет | Falsch | Falsch | OK |
| 82 | 5 | A2 | верно или нет | Richtig | Richtig | OK |
| 83 | 6 | B1 | выбор ответа | A | A | OK |
| 84 | 6 | B1 | выбор ответа | B | B | OK |
| 85 | 6 | B1 | выбор ответа | B | B | OK |
| 86 | 6 | B2 | выбор ответа | B | B | OK |
| 87 | 6 | B1 | выбор ответа | A | A | OK |
| 88 | 6 | B2 | выбор ответа | B | B | OK |
| 89 | 6 | B2 | выбор ответа | B | B | OK |
| 90 | 6 | B2 | выбор ответа | A | A | OK |
| 91 | 6 | B2 | выбор ответа | B | B | OK |
| 92 | 6 | B1 | выбор ответа | B | B | OK |
| 93 | 6 | B2 | дополнение | wird | wird | OK |
| 94 | 6 | B2 | дополнение | ob | ob | OK |
| 95 | 6 | B1 | дополнение | geht | geht | OK |
| 96 | 6 | B2 | дополнение | beginnt | beginnt | OK |
| 97 | 6 | B1 | дополнение | Buße | Buße | OK |
| 98 | 6 | B2 | дополнение | Kirchenjahr | Kirchenjahr | OK |
| 99 | 6 | B2 | дополнение | Friedhof | Friedhof | OK |
| 100 | 6 | B1 | дополнение | Einigung | Einigung | OK |
| 101 | 7 | A2 | дополнение | wird | wird | OK |
| 102 | 7 | A2 | дополнение | werden | werden | OK |
| 103 | 7 | A2 | дополнение | wird | wird | OK |
| 104 | 7 | A2 | выбор ответа | A | A | OK |
| 105 | 7 | B1 | дополнение | stiller | stiller | OK |
| 106 | 7 | B1 | дополнение | weil | weil | OK |
| 107 | 7 | B1 | преобразование | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | выбор ответа | A | A | OK |
| 109 | 7 | B2 | дополнение | ob | ob | OK |
| 110 | 7 | B2 | дополнение | fraglich | fraglich | OK |
| 111 | 7 | B2 | преобразование | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | выбор ответа | B | B | OK |
| 113 | 8 | A2 | текст с пропусками | A | A | OK |
| 114 | 8 | A2 | текст с пропусками | B | B | OK |
| 115 | 8 | A2 | текст с пропусками | A | A | OK |
| 116 | 8 | A2 | текст с пропусками | B | B | OK |
| 117 | 8 | A2 | текст с пропусками | A | A | OK |
| 118 | 8 | A2 | текст с пропусками | A | A | OK |
| 119 | 8 | A2 | текст с пропусками | B | B | OK |
| 120 | 8 | A2 | текст с пропусками | A | A | OK |
| 121 | 8 | B1 | выбор ответа | A | A | OK |
| 122 | 8 | A2 | выбор ответа | B | B | OK |
| 123 | 8 | B1 | выбор ответа | B | B | OK |
| 124 | 8 | B1 | выбор ответа | B | B | OK |
| 125 | 8 | A2 | выбор ответа | B | B | OK |
| 126 | 8 | A2 | выбор ответа | A | A | OK |
| 127 | 8 | B1 | выбор ответа | B | B | OK |
| 128 | 8 | A2 | выбор ответа | B | B | OK |
| 129 | 8 | B1 | выбор ответа | A | A | OK |
| 130 | 8 | A2 | выбор ответа | B | B | OK |
| 131 | 8 | A2 | выбор ответа | B | B | OK |
| 132 | 8 | B1 | выбор ответа | B | B | OK |
| 133 | 8 | A2 | составление предложений | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | составление предложений | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | составление предложений | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | составление предложений | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | перевод | Бундеслига возвращается в пятницу. | Бундеслига возвращается в пятницу. | OK |
| 138 | 8 | A2 | перевод | Рынки закрыты в воскресенье. | Рынки закрыты в воскресенье. | OK |
| 139 | 8 | B1 | перевод | Я делаю адвент-календарь. | Я делаю адвент-календарь. | OK |
| 140 | 8 | B1 | перевод | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | подбор слов | c | c | OK |
| 142 | 8 | B1 | подбор слов | a | a | OK |
| 143 | 8 | B1 | подбор слов | d | d | OK |
| 144 | 8 | B1 | подбор слов | b | b | OK |
| 145 | 8 | A2 | дополнение диалога | A | A | OK |
| 146 | 8 | A2 | дополнение диалога | B | B | OK |
| 147 | 8 | A2 | дополнение диалога | A | A | OK |
| 148 | 8 | B1 | дополнение диалога | A | A | OK |
| 149 | 8 | A2 | дополнение диалога | A | A | OK |
| 150 | 8 | B1 | письмо | Свободное задание — следуйте пунктам из рамки письма | Свободное задание | PREFIX |
