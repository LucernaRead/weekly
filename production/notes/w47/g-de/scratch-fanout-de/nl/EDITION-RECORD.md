# EDITION-RECORD — 2026-w47-de-nl (German for Dutch readers)

Builder: de fan-out builder B (rebuild wave), 2026-11-11. Source: core-de build15
(print 22,965,197 B sha `49beffc4…`, web 2,044,855 B sha `9b63b413…`,
text.md 49,798 B sha `0952bc51…`, proof5 (a) zero findings, 2026-11-11 08:02 UTC).
Transform: `transform.py nl` (transform-nl.log, RC 0). Measure: `measure.py nl` —
24/24 PASS (nl-measure-rblog.log in rebuild-B notes). Build: `build_edition.py nl` —
rebuild-B build 1, 2026-11-11, ALL GATES PASS by ~08:13 UTC (nl-rebuild-B.log).
**Sole content change vs build 1 (2026-11-11 06:46 UTC): core Q34 stem corrected**
(singular, matching key `Weihnachtsmarkt`); no tr/vals change, no other content touched.
Build-1 record preserved in rebuild-B notes (`nl-prev/EDITION-RECORD.md`).

## §1 Deliverables (rebuild-B build 1, final)

| File | Bytes | SHA-256 |
|---|---|---|
| `Die-Lucerna-VOL4-de-nl.pdf` (print) | 10,964,699 | `8f47eea85f54067532cad3e21ba74d3ed98133a3eabc5605dcb34ca3cca8d6d6` |
| `Die-Lucerna-VOL4-de-nl-web.pdf` (web, < 7 MB) | 1,553,854 | `be22a1b5beda4dcaaeccbcffcb7a122e01bb3f92a488d896fd261808ffc34551` |
| `2026-w47-de-nl.text.md` | 49,403 (47,761 chars, 591 entries, 150 ex.) | `e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e` |
| `ABSTRACT.txt` | — | one line, Dutch, no ASCII `"` |
| `WEEKLY-KIT.md` | — | this edition's KIT (rebuild-B values) |

8 SVGs in `svg/`; build interpreter `tools/venv/bin/python` (PIL 13.0.0).

**Q34 stem check (rebuild-B):** new stem `Am Montag öffnet in Köln der erste ___.`
1× each in `content34.py`, `.text.md`, P3 SVG (`p3-kultur.svg`), print-PDF text layer,
web-PDF text layer; old stem 0× in all of those (also 0× in both PDF text layers).
Key `Weihnachtsmarkt` unchanged. Freeze-direct P3 sha8 changed (093cf378 → fc88f676);
all other pages' frozen sha8 identical to build 1 — the single-string delta.

## §2 Gates (rebuild-B build 1) — ALL PASS

- `run.py`: exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150.
  Flow ends: P1-headline 1554 (= core), P1-fussball 2264, P1-quiz 2523,
  P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 706, P4-ex 2315,
  P5-main 1026, P5-ex 2441 (= core), P6-main 777, P6-ex 2523, P7-A2 1278 /
  B1 1342 / B2 1306, P8-battery 1409, P8-keys 2457 (bottom 2560, spare 103px).
  Identical to build 1.
- `measure.py`: 24/24 PASS, 0 FAIL.
- `precheck.py`: RC 0, 0 FAIL; `boxtitle.py`: 7/7 fit (max 395.5px, budget 400.5).
- `verify.py`: TOTAL 150; numbering continuous; SVGs byte-identical after
  re-run; SOP §1.1 audit True; verbatim OK; P8 floor True; 17 forbidden terms absent.
- `occlusion_audit.py`: 0 flags.
- `p8.py`: extract 150/150; compare `status: CLEAN missing=[] extra_count=0
  keydiff=[137, 138, 139, 150]` — expected (137–139 forward translations,
  150 open writing task; Q140 reverse item correctly does NOT diff).
- `freeze.py` diff: exit 0; added CJK 7, all U+3000 (1/page P2–P8, 0 on P1).
- `freeze_direct.py`: RC 0; source PASS (0 unaccounted removed/added;
  removed 521 / added 529, identical to build 1); rendered 8/8,
  frozen 147/163/195/166/173/175/150/186, sha8 083e2a2a / 689045ad / fc88f676 /
  df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7 (only P3 sha8 changed vs
  build 1).
- Print/web text layer: default word multiset identical (print 50,192B /
  web 50,194B); `-raw` normalised identical (49,003B both).
- Chips: per page {1:10, 2:15, 3:18, 4:15, 5:18, 6:18, 7:12, 8:35} TOTAL 141;
  P8 A2 22 / B1 13 / B2 0.
- P8 min font: 9.94pt (≥ 9.75pt floor).
- U+2019 scan over 8 SVGs: 0.
- 150-key check (`nl/keycheck-150.json`): 149/150 exact; Q150 PREFIX (expected,
  see §4). RC 0.

## §3 Build history

- **Build 1 (2026-11-11 06:46 UTC, 5th shift)**: ALL GATES PASS on the first run.
  Visual proofread of the print PDF (P1–P8 at 100 dpi, renders /tmp/nl-proof-*.png)
  + SVG-level scan of the 7 col3 box titles (8 instances): all end ≤ 1862.0
  (max 1857.0, DER WERKZEUGKASTEN "Werktuig", 5.0px margin, deterministic).
  **Zero findings.** Print 10,964,692 B sha `bb54120a…`; web 1,553,848 B sha
  `74a0ecddea…`; text.md 49,404 B sha `d02aa27e…`.
- **Rebuild-B build 1 (2026-11-11 ~08:13 UTC)**: edition dir deleted, re-transformed
  from core-de build15 with unchanged `tr_nl.py` / `vals_nl.json` (transform RC 0,
  measure 24/24), rebuilt — ALL GATES PASS first run, no fixes needed.
  Visual proofread: print PDF re-rendered P1–P8 at 100 dpi
  (renders /tmp/nl-rb-proof-*.png), zero findings; P3 Q34 visually confirmed as
  the new stem. Only delta vs build 1 is the Q34 stem (1 string, P3).
- Note the P8 battery heads as actually built (short, no fix needed):
  F "WÖRTER PAAREN　Combineren", C "LESEVERSTEHEN　Lezen" — the longer
  hypothetical strings "Woorden koppelen" / "Begrijpend lezen" were never in the file.

## §4 150-key table

Source: `nl/keycheck-150.json` (P8-SVG-extracted keys vs REG from the edition's
own sources). 149/150 exact. The single non-exact item is Q150, the open writing
task — the extractor truncates the REG key to its first clause; expected, and
Q150 is already in the p8-compare keydiff set.

| # | Pg | Level | Type | REG key | P8-extracted | Match |
|---|---|---|---|---|---|---|
| 1 | 1 | A2 | invullen | Bundesliga | Bundesliga | OK |
| 2 | 1 | A2 | invullen | Niederlande | Niederlande | OK |
| 3 | 1 | A2 | invullen | Sachsen | Sachsen | OK |
| 4 | 1 | A2 | invullen | Totensonntag | Totensonntag | OK |
| 5 | 1 | B1 | invullen | fünf | fünf | OK |
| 6 | 1 | B1 | invullen | 29. November | 29. November | OK |
| 7 | 1 | A2 | meerkeuze | B | B | OK |
| 8 | 1 | A2 | meerkeuze | A | A | OK |
| 9 | 1 | A2 | meerkeuze | B | B | OK |
| 10 | 1 | A2 | meerkeuze | B | B | OK |
| 11 | 2 | A2 | invullen | 18. November | 18. November | OK |
| 12 | 2 | A2 | invullen | 22. November | 22. November | OK |
| 13 | 2 | A2 | invullen | 29. November | 29. November | OK |
| 14 | 2 | A2 | invullen | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | invullen | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | omzetten | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | omzetten | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | omzetten | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | omzetten | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | omzetten | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | meerkeuze | B | B | OK |
| 22 | 2 | A2 | meerkeuze | B | B | OK |
| 23 | 2 | A2 | meerkeuze | A | A | OK |
| 24 | 2 | A2 | meerkeuze | B | B | OK |
| 25 | 2 | A2 | combineren | d | d | OK |
| 26 | 2 | A2 | combineren | c | c | OK |
| 27 | 2 | A2 | combineren | a | a | OK |
| 28 | 2 | A2 | combineren | b | b | OK |
| 29 | 3 | A2 | juist of onjuist | Richtig | Richtig | OK |
| 30 | 3 | A2 | juist of onjuist | Falsch | Falsch | OK |
| 31 | 3 | A2 | juist of onjuist | Richtig | Richtig | OK |
| 32 | 3 | B1 | juist of onjuist | Falsch | Falsch | OK |
| 33 | 3 | A2 | juist of onjuist | Richtig | Richtig | OK |
| 34 | 3 | A2 | invullen | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | invullen | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | invullen | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | invullen | Advent | Advent | OK |
| 38 | 3 | A2 | invullen | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | meerkeuze | B | B | OK |
| 40 | 3 | A2 | meerkeuze | B | B | OK |
| 41 | 3 | A2 | meerkeuze | A | A | OK |
| 42 | 3 | B1 | meerkeuze | A | A | OK |
| 43 | 3 | A2 | zinnen bouwen | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | zinnen bouwen | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | zinnen bouwen | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | zinnen bouwen | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | meerkeuze | B | B | OK |
| 48 | 4 | B1 | meerkeuze | B | B | OK |
| 49 | 4 | B1 | meerkeuze | C | C | OK |
| 50 | 4 | B1 | meerkeuze | A | A | OK |
| 51 | 4 | B1 | meerkeuze | B | B | OK |
| 52 | 4 | B1 | combineren | d | d | OK |
| 53 | 4 | B1 | combineren | b | b | OK |
| 54 | 4 | B1 | combineren | c | c | OK |
| 55 | 4 | B1 | combineren | a | a | OK |
| 56 | 4 | B1 | invullen | mehr | mehr | OK |
| 57 | 4 | B1 | invullen | später | später | OK |
| 58 | 4 | B1 | invullen | früher | früher | OK |
| 59 | 4 | B1 | invullen | mehr | mehr | OK |
| 60 | 4 | B1 | meerkeuze | A | A | OK |
| 61 | 4 | B1 | meerkeuze | B | B | OK |
| 62 | 4 | B1 | meerkeuze | C | C | OK |
| 63 | 4 | B1 | meerkeuze | A | A | OK |
| 64 | 4 | B1 | meerkeuze | B | B | OK |
| 65 | 5 | B1 | meerkeuze | A | A | OK |
| 66 | 5 | B1 | meerkeuze | B | B | OK |
| 67 | 5 | B1 | meerkeuze | B | B | OK |
| 68 | 5 | B1 | meerkeuze | B | B | OK |
| 69 | 5 | A2 | meerkeuze | A | A | OK |
| 70 | 5 | B1 | invullen | Türchen | Türchen | OK |
| 71 | 5 | B1 | invullen | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | invullen | Christkind | Christkind | OK |
| 73 | 5 | B1 | invullen | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | invullen | Kerze | Kerze | OK |
| 75 | 5 | A2 | invullen | Stern | Stern | OK |
| 76 | 5 | B1 | omzetten | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | omzetten | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | omzetten | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | omzetten | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | juist of onjuist | Richtig | Richtig | OK |
| 81 | 5 | B1 | juist of onjuist | Falsch | Falsch | OK |
| 82 | 5 | A2 | juist of onjuist | Richtig | Richtig | OK |
| 83 | 6 | B1 | meerkeuze | A | A | OK |
| 84 | 6 | B1 | meerkeuze | B | B | OK |
| 85 | 6 | B1 | meerkeuze | B | B | OK |
| 86 | 6 | B2 | meerkeuze | B | B | OK |
| 87 | 6 | B1 | meerkeuze | A | A | OK |
| 88 | 6 | B2 | meerkeuze | B | B | OK |
| 89 | 6 | B2 | meerkeuze | B | B | OK |
| 90 | 6 | B2 | meerkeuze | A | A | OK |
| 91 | 6 | B2 | meerkeuze | B | B | OK |
| 92 | 6 | B1 | meerkeuze | B | B | OK |
| 93 | 6 | B2 | invullen | wird | wird | OK |
| 94 | 6 | B2 | invullen | ob | ob | OK |
| 95 | 6 | B1 | invullen | geht | geht | OK |
| 96 | 6 | B2 | invullen | beginnt | beginnt | OK |
| 97 | 6 | B1 | invullen | Buße | Buße | OK |
| 98 | 6 | B2 | invullen | Kirchenjahr | Kirchenjahr | OK |
| 99 | 6 | B2 | invullen | Friedhof | Friedhof | OK |
| 100 | 6 | B1 | invullen | Einigung | Einigung | OK |
| 101 | 7 | A2 | invullen | wird | wird | OK |
| 102 | 7 | A2 | invullen | werden | werden | OK |
| 103 | 7 | A2 | invullen | wird | wird | OK |
| 104 | 7 | A2 | meerkeuze | A | A | OK |
| 105 | 7 | B1 | invullen | stiller | stiller | OK |
| 106 | 7 | B1 | invullen | weil | weil | OK |
| 107 | 7 | B1 | omzetten | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | meerkeuze | A | A | OK |
| 109 | 7 | B2 | invullen | ob | ob | OK |
| 110 | 7 | B2 | invullen | fraglich | fraglich | OK |
| 111 | 7 | B2 | omzetten | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | meerkeuze | B | B | OK |
| 113 | 8 | A2 | gatentekst | A | A | OK |
| 114 | 8 | A2 | gatentekst | B | B | OK |
| 115 | 8 | A2 | gatentekst | A | A | OK |
| 116 | 8 | A2 | gatentekst | B | B | OK |
| 117 | 8 | A2 | gatentekst | A | A | OK |
| 118 | 8 | A2 | gatentekst | A | A | OK |
| 119 | 8 | A2 | gatentekst | B | B | OK |
| 120 | 8 | A2 | gatentekst | A | A | OK |
| 121 | 8 | B1 | meerkeuze | A | A | OK |
| 122 | 8 | A2 | meerkeuze | B | B | OK |
| 123 | 8 | B1 | meerkeuze | B | B | OK |
| 124 | 8 | B1 | meerkeuze | B | B | OK |
| 125 | 8 | A2 | meerkeuze | B | B | OK |
| 126 | 8 | A2 | meerkeuze | A | A | OK |
| 127 | 8 | B1 | meerkeuze | B | B | OK |
| 128 | 8 | A2 | meerkeuze | B | B | OK |
| 129 | 8 | B1 | meerkeuze | A | A | OK |
| 130 | 8 | A2 | meerkeuze | B | B | OK |
| 131 | 8 | A2 | meerkeuze | B | B | OK |
| 132 | 8 | B1 | meerkeuze | B | B | OK |
| 133 | 8 | A2 | zinnen bouwen | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | zinnen bouwen | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | zinnen bouwen | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | zinnen bouwen | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | vertaling | De Bundesliga keert vrijdag terug. | De Bundesliga keert vrijdag terug. | OK |
| 138 | 8 | A2 | vertaling | De markten zijn zondag dicht. | De markten zijn zondag dicht. | OK |
| 139 | 8 | B1 | vertaling | Ik maak een adventskalender. | Ik maak een adventskalender. | OK |
| 140 | 8 | B1 | vertaling | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | combineren | c | c | OK |
| 142 | 8 | B1 | combineren | a | a | OK |
| 143 | 8 | B1 | combineren | d | d | OK |
| 144 | 8 | B1 | combineren | b | b | OK |
| 145 | 8 | A2 | dialoog aanvullen | A | A | OK |
| 146 | 8 | A2 | dialoog aanvullen | B | B | OK |
| 147 | 8 | A2 | dialoog aanvullen | A | A | OK |
| 148 | 8 | B1 | dialoog aanvullen | A | A | OK |
| 149 | 8 | A2 | dialoog aanvullen | A | A | OK |
| 150 | 8 | B1 | schrijven | Open opdracht — volg de punten in het schrijfblok | Open opdracht | PREFIX |
