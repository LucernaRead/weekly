# EDITION-RECORD — 2026-w47-de-pt (German for Portuguese readers)

Builder: de fan-out builder, 5th shift, 2026-11-11. Source: core-de build14
(sha `9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4`).
Transform: `transform.py pt` (transform-pt2.log for the final build; transform-pt.log
was build 1, superseded). Measure: `measure.py pt` — 24/24 PASS (pt/measure2.log).
Build: `build_edition.py pt` — rebuild 2, 2026-11-11 06:36–06:40 UTC
(pt/rebuild2.log, pt/build.log). Build 1 superseded (see §3).

## §1 Deliverables (rebuild 2, final)

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-pt.pdf` (print) | 10,968,902 | `d946e0184638857c6e7800faa54570815245496e0c48316af75bd4d4582c0c5a` |
| `Die-Lucerna-VOL4-de-pt-web.pdf` (web, < 7 MB) | 1,559,382 | `a86ce50df519bee26a5fa4858ac17079306b9f15929fc5e88f5c6c1a7d1c081d` |
| `2026-w47-de-pt.text.md` | 49,813 (47,948 chars, 591 entries, 150 ex.) | `496e931a201ea78df436ef5a25a9404d773e898cbd66e0da4e5abe719cca6462` |
| `ABSTRACT.txt` | — | one line, Portuguese, no ASCII `"` |
| `WEEKLY-KIT.md` | 11,676 | this edition's KIT (rebuild-2 values) |

8 SVGs in `svg/`; build interpreter `tools/venv/bin/python` (PIL 13.0.0).

## §2 Gates (rebuild 2) — ALL PASS

- `run.py`: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 /
  B1 1342 / B2 1306, P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103px).
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
  frozen 147/163/195/166/173/175/150/186, sha8 083e2a2a / 689045ad / 093cf378 /
  df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7 (identical to en/fr/es/it).
- Print/web text layer: default word multiset identical (print 50,685B /
  web 50,688B); `-raw` normalised identical (49,501B both).
- Chips: per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0.
- P8 min font: 9.94pt (≥ 9.75pt floor).
- U+2019 scan over 8 SVGs: 0.
- 150-key check (`pt/keycheck-150.json`): 149/150 exact; Q150 PREFIX (expected,
  see §4). RC 0.

## §3 Build history

- **Build 1** (06:32–06:35 UTC): exactly 1 gate failure — 'no HEAD TOO WIDE':
  P8-battery head A "A　LÜCKENTEXT　Texto com lacunas" (434.6px > CW 422.5).
  All other gates passed (occlusion 0 flags, chips 141, p8 CLEAN, freeze exit 0,
  P8 min font 9.94pt, P8-battery ends 1409, P8-keys 2457). New defect class for
  this family: a P8 battery head over the column-width limit (es build 1's F head
  was the same class — 525.6px; pt's is only 12.1px over).
- Process note: the first build 1 launch was killed 10 seconds in because I had
  launched it before running `measure.py` — the measure command had a missing
  `$S/` path prefix (ran `measure.py` from /home/hatch, file not found, RC 2).
  Relaunched after a proper measure (24/24). Lesson recorded in the fanout
  report: measure first, then build — never invert.
- Fix in `vals_pt.json` (regenerated `tr_pt.py`, diff exactly 1 line):
  "A　LÜCKENTEXT　Texto com lacunas" → "A　LÜCKENTEXT　Preenchimento"
  (400.4px, PASS, 22px margin — the standard Portuguese term for a cloze
  exercise). Edition dir deleted, re-transform, measure 24/24.
- **Rebuild 2** (06:36–06:40 UTC): ALL GATES PASS. Visual proofread of the
  rebuild-2 print PDF (P1–P8 at 100 dpi, renders /tmp/pt2-proof-*.png) +
  SVG-level scan of the 7 col3 box titles (8 instances): all end ≤ 1862.0
  (max 1849.6, NOCH EIN WORT). **Zero findings.** pt complete.

## §4 150-key table

Source: `pt/keycheck-150.json` (P8-SVG-extracted keys vs REG from the edition's
own sources). 149/150 exact. The single non-exact item is Q150, the open writing
task — the extractor truncates the REG key to its first clause; expected, and
Q150 is already in the p8-compare keydiff set.

| # | Pg | Level | Type | REG key | P8-extracted | Match |
|---|---|---|---|---|---|---|
| 1 | 1 | A2 | completar | Bundesliga | Bundesliga | OK |
| 2 | 1 | A2 | completar | Niederlande | Niederlande | OK |
| 3 | 1 | A2 | completar | Sachsen | Sachsen | OK |
| 4 | 1 | A2 | completar | Totensonntag | Totensonntag | OK |
| 5 | 1 | B1 | completar | fünf | fünf | OK |
| 6 | 1 | B1 | completar | 29. November | 29. November | OK |
| 7 | 1 | A2 | escolha múltipla | B | B | OK |
| 8 | 1 | A2 | escolha múltipla | A | A | OK |
| 9 | 1 | A2 | escolha múltipla | B | B | OK |
| 10 | 1 | A2 | escolha múltipla | B | B | OK |
| 11 | 2 | A2 | completar | 18. November | 18. November | OK |
| 12 | 2 | A2 | completar | 22. November | 22. November | OK |
| 13 | 2 | A2 | completar | 29. November | 29. November | OK |
| 14 | 2 | A2 | completar | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | completar | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | transformação | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | transformação | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | transformação | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | transformação | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | transformação | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | escolha múltipla | B | B | OK |
| 22 | 2 | A2 | escolha múltipla | B | B | OK |
| 23 | 2 | A2 | escolha múltipla | A | A | OK |
| 24 | 2 | A2 | escolha múltipla | B | B | OK |
| 25 | 2 | A2 | associar palavras | d | d | OK |
| 26 | 2 | A2 | associar palavras | c | c | OK |
| 27 | 2 | A2 | associar palavras | a | a | OK |
| 28 | 2 | A2 | associar palavras | b | b | OK |
| 29 | 3 | A2 | verdadeiro ou falso | Richtig | Richtig | OK |
| 30 | 3 | A2 | verdadeiro ou falso | Falsch | Falsch | OK |
| 31 | 3 | A2 | verdadeiro ou falso | Richtig | Richtig | OK |
| 32 | 3 | B1 | verdadeiro ou falso | Falsch | Falsch | OK |
| 33 | 3 | A2 | verdadeiro ou falso | Richtig | Richtig | OK |
| 34 | 3 | A2 | completar | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | completar | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | completar | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | completar | Advent | Advent | OK |
| 38 | 3 | A2 | completar | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | escolha múltipla | B | B | OK |
| 40 | 3 | A2 | escolha múltipla | B | B | OK |
| 41 | 3 | A2 | escolha múltipla | A | A | OK |
| 42 | 3 | B1 | escolha múltipla | A | A | OK |
| 43 | 3 | A2 | construir frases | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | construir frases | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | construir frases | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | construir frases | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | escolha múltipla | B | B | OK |
| 48 | 4 | B1 | escolha múltipla | B | B | OK |
| 49 | 4 | B1 | escolha múltipla | C | C | OK |
| 50 | 4 | B1 | escolha múltipla | A | A | OK |
| 51 | 4 | B1 | escolha múltipla | B | B | OK |
| 52 | 4 | B1 | associar palavras | d | d | OK |
| 53 | 4 | B1 | associar palavras | b | b | OK |
| 54 | 4 | B1 | associar palavras | c | c | OK |
| 55 | 4 | B1 | associar palavras | a | a | OK |
| 56 | 4 | B1 | completar | mehr | mehr | OK |
| 57 | 4 | B1 | completar | später | später | OK |
| 58 | 4 | B1 | completar | früher | früher | OK |
| 59 | 4 | B1 | completar | mehr | mehr | OK |
| 60 | 4 | B1 | escolha múltipla | A | A | OK |
| 61 | 4 | B1 | escolha múltipla | B | B | OK |
| 62 | 4 | B1 | escolha múltipla | C | C | OK |
| 63 | 4 | B1 | escolha múltipla | A | A | OK |
| 64 | 4 | B1 | escolha múltipla | B | B | OK |
| 65 | 5 | B1 | escolha múltipla | A | A | OK |
| 66 | 5 | B1 | escolha múltipla | B | B | OK |
| 67 | 5 | B1 | escolha múltipla | B | B | OK |
| 68 | 5 | B1 | escolha múltipla | B | B | OK |
| 69 | 5 | A2 | escolha múltipla | A | A | OK |
| 70 | 5 | B1 | completar | Türchen | Türchen | OK |
| 71 | 5 | B1 | completar | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | completar | Christkind | Christkind | OK |
| 73 | 5 | B1 | completar | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | completar | Kerze | Kerze | OK |
| 75 | 5 | A2 | completar | Stern | Stern | OK |
| 76 | 5 | B1 | transformação | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | transformação | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | transformação | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | transformação | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | verdadeiro ou falso | Richtig | Richtig | OK |
| 81 | 5 | B1 | verdadeiro ou falso | Falsch | Falsch | OK |
| 82 | 5 | A2 | verdadeiro ou falso | Richtig | Richtig | OK |
| 83 | 6 | B1 | escolha múltipla | A | A | OK |
| 84 | 6 | B1 | escolha múltipla | B | B | OK |
| 85 | 6 | B1 | escolha múltipla | B | B | OK |
| 86 | 6 | B2 | escolha múltipla | B | B | OK |
| 87 | 6 | B1 | escolha múltipla | A | A | OK |
| 88 | 6 | B2 | escolha múltipla | B | B | OK |
| 89 | 6 | B2 | escolha múltipla | B | B | OK |
| 90 | 6 | B2 | escolha múltipla | A | A | OK |
| 91 | 6 | B2 | escolha múltipla | B | B | OK |
| 92 | 6 | B1 | escolha múltipla | B | B | OK |
| 93 | 6 | B2 | completar | wird | wird | OK |
| 94 | 6 | B2 | completar | ob | ob | OK |
| 95 | 6 | B1 | completar | geht | geht | OK |
| 96 | 6 | B2 | completar | beginnt | beginnt | OK |
| 97 | 6 | B1 | completar | Buße | Buße | OK |
| 98 | 6 | B2 | completar | Kirchenjahr | Kirchenjahr | OK |
| 99 | 6 | B2 | completar | Friedhof | Friedhof | OK |
| 100 | 6 | B1 | completar | Einigung | Einigung | OK |
| 101 | 7 | A2 | completar | wird | wird | OK |
| 102 | 7 | A2 | completar | werden | werden | OK |
| 103 | 7 | A2 | completar | wird | wird | OK |
| 104 | 7 | A2 | escolha múltipla | A | A | OK |
| 105 | 7 | B1 | completar | stiller | stiller | OK |
| 106 | 7 | B1 | completar | weil | weil | OK |
| 107 | 7 | B1 | transformação | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | escolha múltipla | A | A | OK |
| 109 | 7 | B2 | completar | ob | ob | OK |
| 110 | 7 | B2 | completar | fraglich | fraglich | OK |
| 111 | 7 | B2 | transformação | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | escolha múltipla | B | B | OK |
| 113 | 8 | A2 | texto com lacunas | A | A | OK |
| 114 | 8 | A2 | texto com lacunas | B | B | OK |
| 115 | 8 | A2 | texto com lacunas | A | A | OK |
| 116 | 8 | A2 | texto com lacunas | B | B | OK |
| 117 | 8 | A2 | texto com lacunas | A | A | OK |
| 118 | 8 | A2 | texto com lacunas | A | A | OK |
| 119 | 8 | A2 | texto com lacunas | B | B | OK |
| 120 | 8 | A2 | texto com lacunas | A | A | OK |
| 121 | 8 | B1 | escolha múltipla | A | A | OK |
| 122 | 8 | A2 | escolha múltipla | B | B | OK |
| 123 | 8 | B1 | escolha múltipla | B | B | OK |
| 124 | 8 | B1 | escolha múltipla | B | B | OK |
| 125 | 8 | A2 | escolha múltipla | B | B | OK |
| 126 | 8 | A2 | escolha múltipla | A | A | OK |
| 127 | 8 | B1 | escolha múltipla | B | B | OK |
| 128 | 8 | A2 | escolha múltipla | B | B | OK |
| 129 | 8 | B1 | escolha múltipla | A | A | OK |
| 130 | 8 | A2 | escolha múltipla | B | B | OK |
| 131 | 8 | A2 | escolha múltipla | B | B | OK |
| 132 | 8 | B1 | escolha múltipla | B | B | OK |
| 133 | 8 | A2 | construir frases | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | construir frases | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | construir frases | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | construir frases | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | tradução | A Bundesliga volta na sexta. | A Bundesliga volta na sexta. | OK |
| 138 | 8 | A2 | tradução | Os mercados fecham no domingo. | Os mercados fecham no domingo. | OK |
| 139 | 8 | B1 | tradução | Estou a fazer um calendário do Advento. | Estou a fazer um calendário do Advento. | OK |
| 140 | 8 | B1 | tradução | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | associar palavras | c | c | OK |
| 142 | 8 | B1 | associar palavras | a | a | OK |
| 143 | 8 | B1 | associar palavras | d | d | OK |
| 144 | 8 | B1 | associar palavras | b | b | OK |
| 145 | 8 | A2 | completar o diálogo | A | A | OK |
| 146 | 8 | A2 | completar o diálogo | B | B | OK |
| 147 | 8 | A2 | completar o diálogo | A | A | OK |
| 148 | 8 | B1 | completar o diálogo | A | A | OK |
| 149 | 8 | A2 | completar o diálogo | A | A | OK |
| 150 | 8 | B1 | escrita | Tarefa livre — segue os pontos do quadro de escrita | Tarefa livre | PREFIX |
