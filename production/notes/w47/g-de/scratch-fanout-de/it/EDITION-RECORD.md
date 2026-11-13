# EDITION-RECORD — 2026-w47-de-it (German for Italian readers)

Builder: de fan-out builder, 5th shift, 2026-11-11. Source: core-de build14
(sha `9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4`).
Transform: `transform.py it` (transform-it2.log for the final build; transform-it.log
was build 1, superseded). Measure: `measure.py it` — 24/24 PASS (it/measure2.log).
Build: `build_edition.py it` — rebuild 2, 2026-11-11 06:25–06:29 UTC
(it/rebuild2.log, it/build.log). Build 1 superseded (see §3).

## §1 Deliverables (rebuild 2, final)

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-it.pdf` (print) | 10,965,089 | `8c9c1d4fb3ce889530ef1e424a9eba9d7a4c5e758667607852ea8ac4b1e8482c` |
| `Die-Lucerna-VOL4-de-it-web.pdf` (web, < 7 MB) | 1,553,866 | `9c01c2f3123ed38f332882c68c1fc0c8a9e876cd2bf8b6d2fbf50c063bc1d571` |
| `2026-w47-de-it.text.md` | 49,713 (48,033 chars, 591 entries, 150 ex.) | `5f3332f13de35e9206c397eac37eacc1fbca8a973b00231bfa3b6029b0835da7` |
| `ABSTRACT.txt` | — | one line, Italian, no ASCII `"` |
| `WEEKLY-KIT.md` | 11,951 | this edition's KIT (rebuild-2 values) |

8 SVGs in `svg/`; build interpreter `tools/venv/bin/python` (PIL 13.0.0).

## §2 Gates (rebuild 2) — ALL PASS

- `run.py`: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 1023, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 /
  B1 1342 / B2 1306, P8-battery 1409, P8-keys 2442 (bottom 2560, spare 118px).
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
  df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7 (identical to en/fr/es).
- Print/web text layer: default word multiset identical (print 50,594B /
  web 50,598B); `-raw` normalised identical (49,393B both).
- Chips: per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0.
- P8 min font: 9.94pt (≥ 9.75pt floor).
- U+2019 scan over 8 SVGs: 0.
- 150-key check (`it/keycheck-150.json`): 149/150 exact; Q150 PREFIX (expected,
  see §4). RC 0.

## §3 Build history

- **Build 1** (06:18–06:23 UTC): 3 gate failures, ONE root cause on P1 —
  FLOW OVERFLOW [P1-headline] (flow ended 1921, bottom 1828) + occlusion
  LINEX ×2 (Q6 'B1' chip and '6.' crossing the row-B hline at y=1844).
  Diagnosis by SVG measurement: the ZAHLEN box is 362px tall (es: 334px) —
  item 2 wrapped to 3 lines ("(Bayern-Colonia, ore / 20.30)"), so the box
  jumped from col 1 to col 2 and pushed JETZT ÜBEN down into the image row
  (same class as fr build 1's ZAHLEN box jump). Visual check of the build-1
  P1 render confirmed: ZAHLEN at col 2 top, Q6 "Der erste Advent ist am"
  overlapping the "EINE WOCHE, ZWEI STIMMUNGEN" head.
- Fix in `vals_it.json` (regenerated `tr_it.py`, diff exactly 1 line):
  ZAHLEN item 2 "(Bayern-Colonia, ore 20.30)" → "(Bayern-Colonia 20.30)".
  Edition dir deleted, re-transform, measure 24/24.
- **Rebuild 2** (06:25–06:29 UTC): ALL GATES PASS; P1-headline ends 1554 =
  core. Visual proofread of the rebuild-2 print PDF (P1–P8 at 100 dpi, renders
  /tmp/it2-proof-*.png) + SVG-level scan of the 7 col3 box titles (8 instances):
  all end ≤ 1862.0 (max 1856.5, NOCH EIN WORT). **Zero findings.** it complete.

## §4 150-key table

Source: `it/keycheck-150.json` (P8-SVG-extracted keys vs REG from the edition's
own sources). 149/150 exact. The single non-exact item is Q150, the open writing
task — the extractor truncates the REG key to its first clause; expected, and
Q150 is already in the p8-compare keydiff set.

| # | Pg | Level | Type | REG key | P8-extracted | Match |
|---|---|---|---|---|---|---|
| 1 | 1 | A2 | completamento | Bundesliga | Bundesliga | OK |
| 2 | 1 | A2 | completamento | Niederlande | Niederlande | OK |
| 3 | 1 | A2 | completamento | Sachsen | Sachsen | OK |
| 4 | 1 | A2 | completamento | Totensonntag | Totensonntag | OK |
| 5 | 1 | B1 | completamento | fünf | fünf | OK |
| 6 | 1 | B1 | completamento | 29. November | 29. November | OK |
| 7 | 1 | A2 | scelta multipla | B | B | OK |
| 8 | 1 | A2 | scelta multipla | A | A | OK |
| 9 | 1 | A2 | scelta multipla | B | B | OK |
| 10 | 1 | A2 | scelta multipla | B | B | OK |
| 11 | 2 | A2 | completamento | 18. November | 18. November | OK |
| 12 | 2 | A2 | completamento | 22. November | 22. November | OK |
| 13 | 2 | A2 | completamento | 29. November | 29. November | OK |
| 14 | 2 | A2 | completamento | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | completamento | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | trasformazione | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | trasformazione | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | trasformazione | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | trasformazione | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | trasformazione | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | scelta multipla | B | B | OK |
| 22 | 2 | A2 | scelta multipla | B | B | OK |
| 23 | 2 | A2 | scelta multipla | A | A | OK |
| 24 | 2 | A2 | scelta multipla | B | B | OK |
| 25 | 2 | A2 | abbinamento | d | d | OK |
| 26 | 2 | A2 | abbinamento | c | c | OK |
| 27 | 2 | A2 | abbinamento | a | a | OK |
| 28 | 2 | A2 | abbinamento | b | b | OK |
| 29 | 3 | A2 | vero o falso | Richtig | Richtig | OK |
| 30 | 3 | A2 | vero o falso | Falsch | Falsch | OK |
| 31 | 3 | A2 | vero o falso | Richtig | Richtig | OK |
| 32 | 3 | B1 | vero o falso | Falsch | Falsch | OK |
| 33 | 3 | A2 | vero o falso | Richtig | Richtig | OK |
| 34 | 3 | A2 | completamento | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | completamento | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | completamento | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | completamento | Advent | Advent | OK |
| 38 | 3 | A2 | completamento | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | scelta multipla | B | B | OK |
| 40 | 3 | A2 | scelta multipla | B | B | OK |
| 41 | 3 | A2 | scelta multipla | A | A | OK |
| 42 | 3 | B1 | scelta multipla | A | A | OK |
| 43 | 3 | A2 | costruzione di frasi | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | costruzione di frasi | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | costruzione di frasi | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | costruzione di frasi | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | scelta multipla | B | B | OK |
| 48 | 4 | B1 | scelta multipla | B | B | OK |
| 49 | 4 | B1 | scelta multipla | C | C | OK |
| 50 | 4 | B1 | scelta multipla | A | A | OK |
| 51 | 4 | B1 | scelta multipla | B | B | OK |
| 52 | 4 | B1 | abbinamento | d | d | OK |
| 53 | 4 | B1 | abbinamento | b | b | OK |
| 54 | 4 | B1 | abbinamento | c | c | OK |
| 55 | 4 | B1 | abbinamento | a | a | OK |
| 56 | 4 | B1 | completamento | mehr | mehr | OK |
| 57 | 4 | B1 | completamento | später | später | OK |
| 58 | 4 | B1 | completamento | früher | früher | OK |
| 59 | 4 | B1 | completamento | mehr | mehr | OK |
| 60 | 4 | B1 | scelta multipla | A | A | OK |
| 61 | 4 | B1 | scelta multipla | B | B | OK |
| 62 | 4 | B1 | scelta multipla | C | C | OK |
| 63 | 4 | B1 | scelta multipla | A | A | OK |
| 64 | 4 | B1 | scelta multipla | B | B | OK |
| 65 | 5 | B1 | scelta multipla | A | A | OK |
| 66 | 5 | B1 | scelta multipla | B | B | OK |
| 67 | 5 | B1 | scelta multipla | B | B | OK |
| 68 | 5 | B1 | scelta multipla | B | B | OK |
| 69 | 5 | A2 | scelta multipla | A | A | OK |
| 70 | 5 | B1 | completamento | Türchen | Türchen | OK |
| 71 | 5 | B1 | completamento | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | completamento | Christkind | Christkind | OK |
| 73 | 5 | B1 | completamento | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | completamento | Kerze | Kerze | OK |
| 75 | 5 | A2 | completamento | Stern | Stern | OK |
| 76 | 5 | B1 | trasformazione | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | trasformazione | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | trasformazione | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | trasformazione | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | vero o falso | Richtig | Richtig | OK |
| 81 | 5 | B1 | vero o falso | Falsch | Falsch | OK |
| 82 | 5 | A2 | vero o falso | Richtig | Richtig | OK |
| 83 | 6 | B1 | scelta multipla | A | A | OK |
| 84 | 6 | B1 | scelta multipla | B | B | OK |
| 85 | 6 | B1 | scelta multipla | B | B | OK |
| 86 | 6 | B2 | scelta multipla | B | B | OK |
| 87 | 6 | B1 | scelta multipla | A | A | OK |
| 88 | 6 | B2 | scelta multipla | B | B | OK |
| 89 | 6 | B2 | scelta multipla | B | B | OK |
| 90 | 6 | B2 | scelta multipla | A | A | OK |
| 91 | 6 | B2 | scelta multipla | B | B | OK |
| 92 | 6 | B1 | scelta multipla | B | B | OK |
| 93 | 6 | B2 | completamento | wird | wird | OK |
| 94 | 6 | B2 | completamento | ob | ob | OK |
| 95 | 6 | B1 | completamento | geht | geht | OK |
| 96 | 6 | B2 | completamento | beginnt | beginnt | OK |
| 97 | 6 | B1 | completamento | Buße | Buße | OK |
| 98 | 6 | B2 | completamento | Kirchenjahr | Kirchenjahr | OK |
| 99 | 6 | B2 | completamento | Friedhof | Friedhof | OK |
| 100 | 6 | B1 | completamento | Einigung | Einigung | OK |
| 101 | 7 | A2 | completamento | wird | wird | OK |
| 102 | 7 | A2 | completamento | werden | werden | OK |
| 103 | 7 | A2 | completamento | wird | wird | OK |
| 104 | 7 | A2 | scelta multipla | A | A | OK |
| 105 | 7 | B1 | completamento | stiller | stiller | OK |
| 106 | 7 | B1 | completamento | weil | weil | OK |
| 107 | 7 | B1 | trasformazione | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | scelta multipla | A | A | OK |
| 109 | 7 | B2 | completamento | ob | ob | OK |
| 110 | 7 | B2 | completamento | fraglich | fraglich | OK |
| 111 | 7 | B2 | trasformazione | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | scelta multipla | B | B | OK |
| 113 | 8 | A2 | testo con buchi | A | A | OK |
| 114 | 8 | A2 | testo con buchi | B | B | OK |
| 115 | 8 | A2 | testo con buchi | A | A | OK |
| 116 | 8 | A2 | testo con buchi | B | B | OK |
| 117 | 8 | A2 | testo con buchi | A | A | OK |
| 118 | 8 | A2 | testo con buchi | A | A | OK |
| 119 | 8 | A2 | testo con buchi | B | B | OK |
| 120 | 8 | A2 | testo con buchi | A | A | OK |
| 121 | 8 | B1 | scelta multipla | A | A | OK |
| 122 | 8 | A2 | scelta multipla | B | B | OK |
| 123 | 8 | B1 | scelta multipla | B | B | OK |
| 124 | 8 | B1 | scelta multipla | B | B | OK |
| 125 | 8 | A2 | scelta multipla | B | B | OK |
| 126 | 8 | A2 | scelta multipla | A | A | OK |
| 127 | 8 | B1 | scelta multipla | B | B | OK |
| 128 | 8 | A2 | scelta multipla | B | B | OK |
| 129 | 8 | B1 | scelta multipla | A | A | OK |
| 130 | 8 | A2 | scelta multipla | B | B | OK |
| 131 | 8 | A2 | scelta multipla | B | B | OK |
| 132 | 8 | B1 | scelta multipla | B | B | OK |
| 133 | 8 | A2 | costruzione di frasi | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | costruzione di frasi | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | costruzione di frasi | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | costruzione di frasi | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | traduzione | La Bundesliga torna venerdì. | La Bundesliga torna venerdì. | OK |
| 138 | 8 | A2 | traduzione | I mercatini chiudono la domenica. | I mercatini chiudono la domenica. | OK |
| 139 | 8 | B1 | traduzione | Sto facendo un calendario dell'Avvento. | Sto facendo un calendario dell'Avvento. | OK |
| 140 | 8 | B1 | traduzione | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | abbinamento | c | c | OK |
| 142 | 8 | B1 | abbinamento | a | a | OK |
| 143 | 8 | B1 | abbinamento | d | d | OK |
| 144 | 8 | B1 | abbinamento | b | b | OK |
| 145 | 8 | A2 | completamento del dialogo | A | A | OK |
| 146 | 8 | A2 | completamento del dialogo | B | B | OK |
| 147 | 8 | A2 | completamento del dialogo | A | A | OK |
| 148 | 8 | B1 | completamento del dialogo | A | A | OK |
| 149 | 8 | A2 | completamento del dialogo | A | A | OK |
| 150 | 8 | B1 | scrittura | Esercizio libero — segui i punti del riquadro di scrittura | Esercizio libero | PREFIX |
