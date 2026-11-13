# EDITION RECORD — 2026-W47 de-ko (German target, Korean reader)

Rebuild 2, 2026-11-11 07:22–07:23 UTC. **ALL GATES PASS.**

## Deliverables

- Print PDF: `Die-Lucerna-VOL4-de-ko.pdf` — 15,906,995 B, sha256 `2232d232f6b156e4c0242e5883a4f31821ded5faaa72dbcdc15a43bacc48aec1`
- Web PDF: `Die-Lucerna-VOL4-de-ko-web.pdf` — 1,867,491 B, sha256 `3070faf0c58e07ef056b7deed582036f09143d031417457da84ba84655b7563d` (52,320 text bytes; < 7 MB)
- Text export: `2026-w47-de-ko.text.md` — 51,499 B (43,395 chars, 591 entries, 150 exercises), sha256 `7de85c889534ea93d96d47fea65ed869dcba578d538bb242a70761c4b334057f`
- ABSTRACT.txt: 388 B (Korean)

## Gates (rebuild 2)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- measure 24/24 PASS (`ko/measure3.log`)
- verify TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags
- p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150]
- freeze (tools/freeze.py, venv interpreter): exit 0, TOTAL added CJK 3,096 (Korean layer)
- freeze_direct source level PASS (0 unaccounted); rendered 8/8 (frozen 149/163/201/166/179/175/160/185; sha8 73347f49 / 689045ad / 14aaccaf / df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / f6dd4a15)
- print/web text layer identical (default multiset 52,317 B / 52,320 B; -raw normalised 51,152 B both)
- P8 min font 9.94pt (≥ 9.75pt); chips 141 (10/15/18/15/18/18/12/35), P8 A2 22 / B1 13 / B2 0
- U+2019 full scan over 8 SVGs = 0; box titles 8/8 inside (max end 1857.3)
- Visual proofread: 8/8 pages at 100 dpi, zero findings (renders /tmp/ko2-proof-*.png)

## Build history

- Build 1: FAILED 2 gates — occlusion only, 1 real flag: [TEXTX] P1 Q6 overlapped ZAHLEN head (464.6px); fix → `DIE WOCHE IN ZAHLEN　숫자` (334.1px). p8 compare was already CLEAN in build 1.
- Build 2: ALL GATES PASS (one-value fix; gen_tr diff exactly 1 line; transform-ko3.log RC 0; measure3 24/24).

## Flow ends (rebuild 2)

P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 993, P2-ex 2332, P3-main 886, P3-ex 2333, P4-main 647, P4-ex 2315, P5-main 996, P5-ex 2441 (= core), P6-main 747, P6-ex 2523, P7-A2 1278 / B1 1310 / B2 1306, P8-battery 1409, P8-keys 2395 (bottom 2560, spare 165px).

## 150-key check (keycheck.py, rebuild 2)

148/150 exact. Both mismatches are extractor join artifacts, verified in the P8 SVG as correct rendering:

- Q139: extracted `대림절 달력을만들고 있습니다.` vs REG `대림절 달력을 만들고 있습니다.` — SVG line 1 ends `대림절 달력을` (y=2250.14), line 2 starts `만들고 있습니다.` (y=2265.775); join2() glues Hangul across the break without a space.
- Q150: extracted `자유과제` vs REG `자유 과제 — 쓰기 상자의 항목을 따르세요` — same space-join artifact (`자유` ends line 1 y=2359.585, `과제 — …` starts line 2 y=2375.22) plus the expected PREFIX truncation. Q150 note `（나열된 항목으로 채점）` is retained and renders.

p8 compare is CLEAN with keydiff [137, 138, 139, 150] (137–139 translate-to-Korean, 150 Q150 PREFIX).

| n | page | level | type | REG key | extracted |
|---:|---:|---|---|---|---|
| 1 | 1 | A2 | 빈칸 채우기 | Bundesliga | Bundesliga | OK |
| 2 | 1 | A2 | 빈칸 채우기 | Niederlande | Niederlande | OK |
| 3 | 1 | A2 | 빈칸 채우기 | Sachsen | Sachsen | OK |
| 4 | 1 | A2 | 빈칸 채우기 | Totensonntag | Totensonntag | OK |
| 5 | 1 | B1 | 빈칸 채우기 | fünf | fünf | OK |
| 6 | 1 | B1 | 빈칸 채우기 | 29. November | 29. November | OK |
| 7 | 1 | A2 | 선택 문제 | B | B | OK |
| 8 | 1 | A2 | 선택 문제 | A | A | OK |
| 9 | 1 | A2 | 선택 문제 | B | B | OK |
| 10 | 1 | A2 | 선택 문제 | B | B | OK |
| 11 | 2 | A2 | 빈칸 채우기 | 18. November | 18. November | OK |
| 12 | 2 | A2 | 빈칸 채우기 | 22. November | 22. November | OK |
| 13 | 2 | A2 | 빈칸 채우기 | 29. November | 29. November | OK |
| 14 | 2 | A2 | 빈칸 채우기 | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | 빈칸 채우기 | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | 바꾸어 쓰기 | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | 바꾸어 쓰기 | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | 바꾸어 쓰기 | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | 바꾸어 쓰기 | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | 바꾸어 쓰기 | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | 선택 문제 | B | B | OK |
| 22 | 2 | A2 | 선택 문제 | B | B | OK |
| 23 | 2 | A2 | 선택 문제 | A | A | OK |
| 24 | 2 | A2 | 선택 문제 | B | B | OK |
| 25 | 2 | A2 | 짝 맞추기 | d | d | OK |
| 26 | 2 | A2 | 짝 맞추기 | c | c | OK |
| 27 | 2 | A2 | 짝 맞추기 | a | a | OK |
| 28 | 2 | A2 | 짝 맞추기 | b | b | OK |
| 29 | 3 | A2 | 맞다/틀리다 | Richtig | Richtig | OK |
| 30 | 3 | A2 | 맞다/틀리다 | Falsch | Falsch | OK |
| 31 | 3 | A2 | 맞다/틀리다 | Richtig | Richtig | OK |
| 32 | 3 | B1 | 맞다/틀리다 | Falsch | Falsch | OK |
| 33 | 3 | A2 | 맞다/틀리다 | Richtig | Richtig | OK |
| 34 | 3 | A2 | 빈칸 채우기 | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | 빈칸 채우기 | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | 빈칸 채우기 | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | 빈칸 채우기 | Advent | Advent | OK |
| 38 | 3 | A2 | 빈칸 채우기 | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | 선택 문제 | B | B | OK |
| 40 | 3 | A2 | 선택 문제 | B | B | OK |
| 41 | 3 | A2 | 선택 문제 | A | A | OK |
| 42 | 3 | B1 | 선택 문제 | A | A | OK |
| 43 | 3 | A2 | 문장 만들기 | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | 문장 만들기 | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | 문장 만들기 | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | 문장 만들기 | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | 선택 문제 | B | B | OK |
| 48 | 4 | B1 | 선택 문제 | B | B | OK |
| 49 | 4 | B1 | 선택 문제 | C | C | OK |
| 50 | 4 | B1 | 선택 문제 | A | A | OK |
| 51 | 4 | B1 | 선택 문제 | B | B | OK |
| 52 | 4 | B1 | 짝 맞추기 | d | d | OK |
| 53 | 4 | B1 | 짝 맞추기 | b | b | OK |
| 54 | 4 | B1 | 짝 맞추기 | c | c | OK |
| 55 | 4 | B1 | 짝 맞추기 | a | a | OK |
| 56 | 4 | B1 | 빈칸 채우기 | mehr | mehr | OK |
| 57 | 4 | B1 | 빈칸 채우기 | später | später | OK |
| 58 | 4 | B1 | 빈칸 채우기 | früher | früher | OK |
| 59 | 4 | B1 | 빈칸 채우기 | mehr | mehr | OK |
| 60 | 4 | B1 | 선택 문제 | A | A | OK |
| 61 | 4 | B1 | 선택 문제 | B | B | OK |
| 62 | 4 | B1 | 선택 문제 | C | C | OK |
| 63 | 4 | B1 | 선택 문제 | A | A | OK |
| 64 | 4 | B1 | 선택 문제 | B | B | OK |
| 65 | 5 | B1 | 선택 문제 | A | A | OK |
| 66 | 5 | B1 | 선택 문제 | B | B | OK |
| 67 | 5 | B1 | 선택 문제 | B | B | OK |
| 68 | 5 | B1 | 선택 문제 | B | B | OK |
| 69 | 5 | A2 | 선택 문제 | A | A | OK |
| 70 | 5 | B1 | 빈칸 채우기 | Türchen | Türchen | OK |
| 71 | 5 | B1 | 빈칸 채우기 | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | 빈칸 채우기 | Christkind | Christkind | OK |
| 73 | 5 | B1 | 빈칸 채우기 | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | 빈칸 채우기 | Kerze | Kerze | OK |
| 75 | 5 | A2 | 빈칸 채우기 | Stern | Stern | OK |
| 76 | 5 | B1 | 바꾸어 쓰기 | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | 바꾸어 쓰기 | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | 바꾸어 쓰기 | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | 바꾸어 쓰기 | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | 맞다/틀리다 | Richtig | Richtig | OK |
| 81 | 5 | B1 | 맞다/틀리다 | Falsch | Falsch | OK |
| 82 | 5 | A2 | 맞다/틀리다 | Richtig | Richtig | OK |
| 83 | 6 | B1 | 선택 문제 | A | A | OK |
| 84 | 6 | B1 | 선택 문제 | B | B | OK |
| 85 | 6 | B1 | 선택 문제 | B | B | OK |
| 86 | 6 | B2 | 선택 문제 | B | B | OK |
| 87 | 6 | B1 | 선택 문제 | A | A | OK |
| 88 | 6 | B2 | 선택 문제 | B | B | OK |
| 89 | 6 | B2 | 선택 문제 | B | B | OK |
| 90 | 6 | B2 | 선택 문제 | A | A | OK |
| 91 | 6 | B2 | 선택 문제 | B | B | OK |
| 92 | 6 | B1 | 선택 문제 | B | B | OK |
| 93 | 6 | B2 | 빈칸 채우기 | wird | wird | OK |
| 94 | 6 | B2 | 빈칸 채우기 | ob | ob | OK |
| 95 | 6 | B1 | 빈칸 채우기 | geht | geht | OK |
| 96 | 6 | B2 | 빈칸 채우기 | beginnt | beginnt | OK |
| 97 | 6 | B1 | 빈칸 채우기 | Buße | Buße | OK |
| 98 | 6 | B2 | 빈칸 채우기 | Kirchenjahr | Kirchenjahr | OK |
| 99 | 6 | B2 | 빈칸 채우기 | Friedhof | Friedhof | OK |
| 100 | 6 | B1 | 빈칸 채우기 | Einigung | Einigung | OK |
| 101 | 7 | A2 | 빈칸 채우기 | wird | wird | OK |
| 102 | 7 | A2 | 빈칸 채우기 | werden | werden | OK |
| 103 | 7 | A2 | 빈칸 채우기 | wird | wird | OK |
| 104 | 7 | A2 | 선택 문제 | A | A | OK |
| 105 | 7 | B1 | 빈칸 채우기 | stiller | stiller | OK |
| 106 | 7 | B1 | 빈칸 채우기 | weil | weil | OK |
| 107 | 7 | B1 | 바꾸어 쓰기 | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | 선택 문제 | A | A | OK |
| 109 | 7 | B2 | 빈칸 채우기 | ob | ob | OK |
| 110 | 7 | B2 | 빈칸 채우기 | fraglich | fraglich | OK |
| 111 | 7 | B2 | 바꾸어 쓰기 | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | 선택 문제 | B | B | OK |
| 113 | 8 | A2 | 빈칸 글 | A | A | OK |
| 114 | 8 | A2 | 빈칸 글 | B | B | OK |
| 115 | 8 | A2 | 빈칸 글 | A | A | OK |
| 116 | 8 | A2 | 빈칸 글 | B | B | OK |
| 117 | 8 | A2 | 빈칸 글 | A | A | OK |
| 118 | 8 | A2 | 빈칸 글 | A | A | OK |
| 119 | 8 | A2 | 빈칸 글 | B | B | OK |
| 120 | 8 | A2 | 빈칸 글 | A | A | OK |
| 121 | 8 | B1 | 선택 문제 | A | A | OK |
| 122 | 8 | A2 | 선택 문제 | B | B | OK |
| 123 | 8 | B1 | 선택 문제 | B | B | OK |
| 124 | 8 | B1 | 선택 문제 | B | B | OK |
| 125 | 8 | A2 | 선택 문제 | B | B | OK |
| 126 | 8 | A2 | 선택 문제 | A | A | OK |
| 127 | 8 | B1 | 선택 문제 | B | B | OK |
| 128 | 8 | A2 | 선택 문제 | B | B | OK |
| 129 | 8 | B1 | 선택 문제 | A | A | OK |
| 130 | 8 | A2 | 선택 문제 | B | B | OK |
| 131 | 8 | A2 | 선택 문제 | B | B | OK |
| 132 | 8 | B1 | 선택 문제 | B | B | OK |
| 133 | 8 | A2 | 문장 만들기 | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | 문장 만들기 | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | 문장 만들기 | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | 문장 만들기 | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | 번역 | 분데스리가는 금요일에 복귀합니다. | 분데스리가는 금요일에 복귀합니다. | OK |
| 138 | 8 | A2 | 번역 | 일요일에는 시장이 닫습니다. | 일요일에는 시장이 닫습니다. | OK |
| 139 | 8 | B1 | 번역 | 대림절 달력을 만들고 있습니다. | 대림절 달력을만들고 있습니다. | JOIN-ARTIFACT |
| 140 | 8 | B1 | 번역 | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | 짝 맞추기 | c | c | OK |
| 142 | 8 | B1 | 짝 맞추기 | a | a | OK |
| 143 | 8 | B1 | 짝 맞추기 | d | d | OK |
| 144 | 8 | B1 | 짝 맞추기 | b | b | OK |
| 145 | 8 | A2 | 대화 완성 | A | A | OK |
| 146 | 8 | A2 | 대화 완성 | B | B | OK |
| 147 | 8 | A2 | 대화 완성 | A | A | OK |
| 148 | 8 | B1 | 대화 완성 | A | A | OK |
| 149 | 8 | A2 | 대화 완성 | A | A | OK |
| 150 | 8 | B1 | 쓰기 | 자유 과제 — 쓰기 상자의 항목을 따르세요 | 자유과제 | PREFIX |

Logs: `ko/rebuild2.log`, `ko/build.log`, `ko/measure3.log`, `transform-ko3.log`, `ko/keycheck-150.json`, `ko/freeze-direct.json`.
