# EDITION-RECORD — 2026-w47-de-es (German for Spanish readers)

Builder: de fan-out builder, 5th shift, 2026-11-11. Source: core-de build14
(sha `9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4`).
Transform: `transform.py es` (transform-es3.log for the final build).
Measure: `measure.py es` — 24/24 PASS (es/measure3.log).
Build: `build_edition.py es` — rebuild 3, 2026-11-11 06:08–06:14 UTC
(es/rebuild3.log, es/build.log). Builds 1–2 superseded (see §3).

## §1 Deliverables (rebuild 3, final)

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-es.pdf` (print) | 10,968,797 | `2c535a10f81516a749c56fa43290bc54c5bd268ba36469caa10367bc944395ed` |
| `Die-Lucerna-VOL4-de-es-web.pdf` (web, < 7 MB) | 1,558,812 | `b20ceebfeba6c5e7ad2be9d2123b8406755bceff0174f34c6ca4158e03716228` |
| `2026-w47-de-es.text.md` | 50,125 (48,287 chars, 591 entries, 150 ex.) | `b36e21f45810821a28855186fe67739927e18f2aff30ef56672e3fda44753d48` |
| `ABSTRACT.txt` | 426 | one line, Spanish, no ASCII `"` |
| `WEEKLY-KIT.md` | 12,503 | this edition's KIT (rebuild-3 values) |

8 SVGs in `svg/`; build interpreter `tools/venv/bin/python` (PIL 13.0.0).

## §2 Gates (rebuild 3) — ALL PASS

- `run.py`: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 1023, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 /
  B1 1374 / B2 1306, P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103px).
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
  df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7 (identical to en/fr).
- Print/web text layer: default word multiset identical (print 51,013B /
  web 51,014B); `-raw` normalised identical (49,813B both).
- Chips: per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0.
- P8 min font: 9.94pt (≥ 9.75pt floor).
- U+2019 scan over 8 SVGs: 0.
- 150-key check (`es/keycheck-150.json`): 149/150 exact; Q150 PREFIX (expected,
  see §4). RC 0.

## §3 Build history

- **Build 1** (~05:42–05:47 UTC): 3 gate failures — P8-battery F head too wide
  (525.6px > CW 422.5) + occlusion 4 flags (P3 title ink 1987.75; P7 toolbox
  title 1994.75; P8 F head 1965.0; P3 LINEX tip line 1623.66 vs rule 1608).
  Fixed: P3 title → "Palabras", toolbox → "Herramientas", F head → "Parejas",
  LAYOUT ey 1620 → 1680.
- **Build 2** (~05:55 UTC): ALL GATES PASS (print 10,968,933 B sha
  `6b1cc8b89f8933b426c309b2d2934b08d4f970be5d7362e09bb2bea87ccaeedd`; web
  1,558,952 B sha `fd87f12f6c30b8bb20a0e036576e8e334ddcfd333e8c2c21c9b13706d541c2ff`;
  text.md 50,195 B sha `46b2936c234038b6f785a6fea212e867b06cdc08b7aa843a1536ff207c78bf9e`).
  Visual proofread (P1–P8 at 100 dpi) found the NEW defect class
  **col3 box-title overflow** (5 titles spilling off their cream boxes; box right
  edge 1862.0, budget 400.5px): STILLE OVER 84.0, TIPP OVER 10.1, ADVENTSWÖRTER
  OVER 83.4, WERKZEUGKASTEN OVER 47.5, LESERBRIEFE OVER 15.0. No other findings.
- **Rebuild 3** (06:08–06:14 UTC): 5 titles shortened (Tranquila / Consejo /
  Adviento / Útiles / Cartas); new script `boxtitle.py` (7/7). ALL GATES PASS.
  Visual proofread of the rebuild-3 print PDF (P1–P8 at 100 dpi, renders
  /tmp/es3-proof-*.png) + SVG-level scan of the 7 col3 box titles (8 instances):
  all end ≤ 1862.0 (max 1849.1). **Zero findings.** es complete.

## §4 150-key table

Source: `es/keycheck-150.json` (P8-SVG-extracted keys vs REG from the edition's
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
| 7 | 1 | A2 | opción múltiple | B | B | OK |
| 8 | 1 | A2 | opción múltiple | A | A | OK |
| 9 | 1 | A2 | opción múltiple | B | B | OK |
| 10 | 1 | A2 | opción múltiple | B | B | OK |
| 11 | 2 | A2 | completar | 18. November | 18. November | OK |
| 12 | 2 | A2 | completar | 22. November | 22. November | OK |
| 13 | 2 | A2 | completar | 29. November | 29. November | OK |
| 14 | 2 | A2 | completar | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | completar | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | transformación | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | transformación | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | transformación | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | transformación | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | transformación | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | opción múltiple | B | B | OK |
| 22 | 2 | A2 | opción múltiple | B | B | OK |
| 23 | 2 | A2 | opción múltiple | A | A | OK |
| 24 | 2 | A2 | opción múltiple | B | B | OK |
| 25 | 2 | A2 | emparejar palabras | d | d | OK |
| 26 | 2 | A2 | emparejar palabras | c | c | OK |
| 27 | 2 | A2 | emparejar palabras | a | a | OK |
| 28 | 2 | A2 | emparejar palabras | b | b | OK |
| 29 | 3 | A2 | verdadero o falso | Richtig | Richtig | OK |
| 30 | 3 | A2 | verdadero o falso | Falsch | Falsch | OK |
| 31 | 3 | A2 | verdadero o falso | Richtig | Richtig | OK |
| 32 | 3 | B1 | verdadero o falso | Falsch | Falsch | OK |
| 33 | 3 | A2 | verdadero o falso | Richtig | Richtig | OK |
| 34 | 3 | A2 | completar | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | completar | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | completar | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | completar | Advent | Advent | OK |
| 38 | 3 | A2 | completar | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | opción múltiple | B | B | OK |
| 40 | 3 | A2 | opción múltiple | B | B | OK |
| 41 | 3 | A2 | opción múltiple | A | A | OK |
| 42 | 3 | B1 | opción múltiple | A | A | OK |
| 43 | 3 | A2 | construir frases | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | construir frases | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | construir frases | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | construir frases | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | opción múltiple | B | B | OK |
| 48 | 4 | B1 | opción múltiple | B | B | OK |
| 49 | 4 | B1 | opción múltiple | C | C | OK |
| 50 | 4 | B1 | opción múltiple | A | A | OK |
| 51 | 4 | B1 | opción múltiple | B | B | OK |
| 52 | 4 | B1 | emparejar palabras | d | d | OK |
| 53 | 4 | B1 | emparejar palabras | b | b | OK |
| 54 | 4 | B1 | emparejar palabras | c | c | OK |
| 55 | 4 | B1 | emparejar palabras | a | a | OK |
| 56 | 4 | B1 | completar | mehr | mehr | OK |
| 57 | 4 | B1 | completar | später | später | OK |
| 58 | 4 | B1 | completar | früher | früher | OK |
| 59 | 4 | B1 | completar | mehr | mehr | OK |
| 60 | 4 | B1 | opción múltiple | A | A | OK |
| 61 | 4 | B1 | opción múltiple | B | B | OK |
| 62 | 4 | B1 | opción múltiple | C | C | OK |
| 63 | 4 | B1 | opción múltiple | A | A | OK |
| 64 | 4 | B1 | opción múltiple | B | B | OK |
| 65 | 5 | B1 | opción múltiple | A | A | OK |
| 66 | 5 | B1 | opción múltiple | B | B | OK |
| 67 | 5 | B1 | opción múltiple | B | B | OK |
| 68 | 5 | B1 | opción múltiple | B | B | OK |
| 69 | 5 | A2 | opción múltiple | A | A | OK |
| 70 | 5 | B1 | completar | Türchen | Türchen | OK |
| 71 | 5 | B1 | completar | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | completar | Christkind | Christkind | OK |
| 73 | 5 | B1 | completar | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | completar | Kerze | Kerze | OK |
| 75 | 5 | A2 | completar | Stern | Stern | OK |
| 76 | 5 | B1 | transformación | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | transformación | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | transformación | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | transformación | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | verdadero o falso | Richtig | Richtig | OK |
| 81 | 5 | B1 | verdadero o falso | Falsch | Falsch | OK |
| 82 | 5 | A2 | verdadero o falso | Richtig | Richtig | OK |
| 83 | 6 | B1 | opción múltiple | A | A | OK |
| 84 | 6 | B1 | opción múltiple | B | B | OK |
| 85 | 6 | B1 | opción múltiple | B | B | OK |
| 86 | 6 | B2 | opción múltiple | B | B | OK |
| 87 | 6 | B1 | opción múltiple | A | A | OK |
| 88 | 6 | B2 | opción múltiple | B | B | OK |
| 89 | 6 | B2 | opción múltiple | B | B | OK |
| 90 | 6 | B2 | opción múltiple | A | A | OK |
| 91 | 6 | B2 | opción múltiple | B | B | OK |
| 92 | 6 | B1 | opción múltiple | B | B | OK |
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
| 104 | 7 | A2 | opción múltiple | A | A | OK |
| 105 | 7 | B1 | completar | stiller | stiller | OK |
| 106 | 7 | B1 | completar | weil | weil | OK |
| 107 | 7 | B1 | transformación | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | opción múltiple | A | A | OK |
| 109 | 7 | B2 | completar | ob | ob | OK |
| 110 | 7 | B2 | completar | fraglich | fraglich | OK |
| 111 | 7 | B2 | transformación | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | opción múltiple | B | B | OK |
| 113 | 8 | A2 | texto con huecos | A | A | OK |
| 114 | 8 | A2 | texto con huecos | B | B | OK |
| 115 | 8 | A2 | texto con huecos | A | A | OK |
| 116 | 8 | A2 | texto con huecos | B | B | OK |
| 117 | 8 | A2 | texto con huecos | A | A | OK |
| 118 | 8 | A2 | texto con huecos | A | A | OK |
| 119 | 8 | A2 | texto con huecos | B | B | OK |
| 120 | 8 | A2 | texto con huecos | A | A | OK |
| 121 | 8 | B1 | opción múltiple | A | A | OK |
| 122 | 8 | A2 | opción múltiple | B | B | OK |
| 123 | 8 | B1 | opción múltiple | B | B | OK |
| 124 | 8 | B1 | opción múltiple | B | B | OK |
| 125 | 8 | A2 | opción múltiple | B | B | OK |
| 126 | 8 | A2 | opción múltiple | A | A | OK |
| 127 | 8 | B1 | opción múltiple | B | B | OK |
| 128 | 8 | A2 | opción múltiple | B | B | OK |
| 129 | 8 | B1 | opción múltiple | A | A | OK |
| 130 | 8 | A2 | opción múltiple | B | B | OK |
| 131 | 8 | A2 | opción múltiple | B | B | OK |
| 132 | 8 | B1 | opción múltiple | B | B | OK |
| 133 | 8 | A2 | construir frases | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | construir frases | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | construir frases | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | construir frases | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | traducción | La Bundesliga vuelve el viernes. | La Bundesliga vuelve el viernes. | OK |
| 138 | 8 | A2 | traducción | Los mercados cierran el domingo. | Los mercados cierran el domingo. | OK |
| 139 | 8 | B1 | traducción | Estoy haciendo un calendario de Adviento. | Estoy haciendo un calendario de Adviento. | OK |
| 140 | 8 | B1 | traducción | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | emparejar palabras | c | c | OK |
| 142 | 8 | B1 | emparejar palabras | a | a | OK |
| 143 | 8 | B1 | emparejar palabras | d | d | OK |
| 144 | 8 | B1 | emparejar palabras | b | b | OK |
| 145 | 8 | A2 | completar el diálogo | A | A | OK |
| 146 | 8 | A2 | completar el diálogo | B | B | OK |
| 147 | 8 | A2 | completar el diálogo | A | A | OK |
| 148 | 8 | B1 | completar el diálogo | A | A | OK |
| 149 | 8 | A2 | completar el diálogo | A | A | OK |
| 150 | 8 | B1 | redacción | Tarea libre — sigue los puntos del recuadro de escritura | Tarea libre | PREFIX |
