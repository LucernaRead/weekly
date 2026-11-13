# EDITION RECORD — 2026-W47 de-zh-tw (German target, Traditional-Chinese reader)

Build 1, 2026-11-11 07:27–07:28 UTC. **ALL GATES PASS on the first run.**

## Deliverables

- Print PDF: `Die-Lucerna-VOL4-de-zh-tw.pdf` — 23,048,415 B, sha256 `71693e9c011ffc4b589a3fdaba8d339cad7e9f3ebaac35ea33ea34e1d2fa8537`
- Web PDF: `Die-Lucerna-VOL4-de-zh-tw-web.pdf` — 2,301,044 B, sha256 `11f58493f60fe6dce06b8f3c47095e7b5fbec5a2cb300a8d4a9074b478189cc1` (49,907 text bytes; < 7 MB)
- Text export: `2026-w47-de-zh-tw.text.md` — 49,093 B (42,126 chars, 591 entries, 150 exercises), sha256 `f82141d6224f6870f1218b1f0aa58e2f4dd7b6baa81515fc1d4239b6b3261b5f`
- ABSTRACT.txt: 294 B (Traditional Chinese)

## Gates (build 1)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- measure 24/24 PASS (`zh-tw/measure1.log`)
- verify TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags
- p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150]
- freeze (tools/freeze.py, venv interpreter): exit 0, TOTAL added CJK 1,328 (Traditional layer)
- freeze_direct rendered 8/8 (frozen 151/164/206/166/182/176/170/191; sha8 54c9b51e / 2db0dd83 / 56a81b7d / df1bebf7 / b42a8c3d / babfe417 / 9dc31873 / 961dd98a); source level: exactly 4 unaccounted strings — 3 from the documented TC font switch + 1 from a core-side change made at 07:28:39 UTC, after this build (see below)
- print/web text layer identical (default multiset 49,906 B / 49,907 B; -raw normalised 48,778 B both)
- P8 min font 9.94pt (≥ 9.75pt); chips 141 (10/15/18/15/18/18/12/35), P8 A2 22 / B1 13 / B2 0
- U+2019 full scan over 8 SVGs = 0; box titles 8/8 inside (max end 1825.1)
- CJK residual audit: 2,978 CJK chars in 8 SVGs; the only char not in tr_zh-tw.py values is ／ U+FF0F, the pageline separator from PAGELINE_ZH_TW — legitimate furniture; zero leftover Simplified-Chinese strings
- Visual proofread: 8/8 pages at 100 dpi, zero findings (renders /tmp/zhtw-proof-*.png)

## Core-side change AFTER this build (coordinator decision — not this edition's defect)

At 2026-11-11 07:28:39 UTC, core-de/content34.py line 105 was changed: the German exercise stem went from plural `Am Montag öffnen in Köln die ersten ___.` to singular `Am Montag öffnet in Köln der erste ___.`. All 10 editions carry the plural (built from the core as it stood at their transform times). Proof it is core-side: ja's freeze_direct re-run at ~07:30 shows the same unaccounted pair (it passed at build time, 07:15); ja's rendered frozen counts/sha8 are unchanged. The coordinator must decide whether the singular is a correction all 10 editions must re-transform for, or the editions stand as built.

## Flow ends (build 1)

P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 964, P2-ex 2332, P3-main 886, P3-ex 2333, P4-main 647, P4-ex 2315, P5-main 996, P5-ex 2441 (= core), P6-main 747, P6-ex 2523, P7-A2 1278 / B1 1310 / B2 1306, P8-battery 1409, P8-keys 2379 (bottom 2560, spare 181px).

## 150-key check (keycheck.py, build 1)

149/150 exact. Only Q150 differs, and only as PREFIX (expected): extracted `開放任務` is a prefix of the REG key `開放任務 — 依寫作框中的要點進行`. p8 compare status CLEAN with keydiff [137, 138, 139, 150] (137–139 are the expected translate-to-Traditional-Chinese items; 150 is the Q150 PREFIX). Q150's note `（依列出的要點評分）` is retained and renders.

| n | page | level | type | REG key | extracted |
|---:|---:|---|---|---|---|
| 1 | 1 | A2 | 填空 | Bundesliga | Bundesliga | OK |
| 2 | 1 | A2 | 填空 | Niederlande | Niederlande | OK |
| 3 | 1 | A2 | 填空 | Sachsen | Sachsen | OK |
| 4 | 1 | A2 | 填空 | Totensonntag | Totensonntag | OK |
| 5 | 1 | B1 | 填空 | fünf | fünf | OK |
| 6 | 1 | B1 | 填空 | 29. November | 29. November | OK |
| 7 | 1 | A2 | 選擇題 | B | B | OK |
| 8 | 1 | A2 | 選擇題 | A | A | OK |
| 9 | 1 | A2 | 選擇題 | B | B | OK |
| 10 | 1 | A2 | 選擇題 | B | B | OK |
| 11 | 2 | A2 | 填空 | 18. November | 18. November | OK |
| 12 | 2 | A2 | 填空 | 22. November | 22. November | OK |
| 13 | 2 | A2 | 填空 | 29. November | 29. November | OK |
| 14 | 2 | A2 | 填空 | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | 填空 | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | 改寫 | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | 改寫 | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | 改寫 | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | 改寫 | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | 改寫 | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | 選擇題 | B | B | OK |
| 22 | 2 | A2 | 選擇題 | B | B | OK |
| 23 | 2 | A2 | 選擇題 | A | A | OK |
| 24 | 2 | A2 | 選擇題 | B | B | OK |
| 25 | 2 | A2 | 配對 | d | d | OK |
| 26 | 2 | A2 | 配對 | c | c | OK |
| 27 | 2 | A2 | 配對 | a | a | OK |
| 28 | 2 | A2 | 配對 | b | b | OK |
| 29 | 3 | A2 | 是非題 | Richtig | Richtig | OK |
| 30 | 3 | A2 | 是非題 | Falsch | Falsch | OK |
| 31 | 3 | A2 | 是非題 | Richtig | Richtig | OK |
| 32 | 3 | B1 | 是非題 | Falsch | Falsch | OK |
| 33 | 3 | A2 | 是非題 | Richtig | Richtig | OK |
| 34 | 3 | A2 | 填空 | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | 填空 | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | 填空 | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | 填空 | Advent | Advent | OK |
| 38 | 3 | A2 | 填空 | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | 選擇題 | B | B | OK |
| 40 | 3 | A2 | 選擇題 | B | B | OK |
| 41 | 3 | A2 | 選擇題 | A | A | OK |
| 42 | 3 | B1 | 選擇題 | A | A | OK |
| 43 | 3 | A2 | 造句 | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | 造句 | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | 造句 | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | 造句 | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | 選擇題 | B | B | OK |
| 48 | 4 | B1 | 選擇題 | B | B | OK |
| 49 | 4 | B1 | 選擇題 | C | C | OK |
| 50 | 4 | B1 | 選擇題 | A | A | OK |
| 51 | 4 | B1 | 選擇題 | B | B | OK |
| 52 | 4 | B1 | 配對 | d | d | OK |
| 53 | 4 | B1 | 配對 | b | b | OK |
| 54 | 4 | B1 | 配對 | c | c | OK |
| 55 | 4 | B1 | 配對 | a | a | OK |
| 56 | 4 | B1 | 填空 | mehr | mehr | OK |
| 57 | 4 | B1 | 填空 | später | später | OK |
| 58 | 4 | B1 | 填空 | früher | früher | OK |
| 59 | 4 | B1 | 填空 | mehr | mehr | OK |
| 60 | 4 | B1 | 選擇題 | A | A | OK |
| 61 | 4 | B1 | 選擇題 | B | B | OK |
| 62 | 4 | B1 | 選擇題 | C | C | OK |
| 63 | 4 | B1 | 選擇題 | A | A | OK |
| 64 | 4 | B1 | 選擇題 | B | B | OK |
| 65 | 5 | B1 | 選擇題 | A | A | OK |
| 66 | 5 | B1 | 選擇題 | B | B | OK |
| 67 | 5 | B1 | 選擇題 | B | B | OK |
| 68 | 5 | B1 | 選擇題 | B | B | OK |
| 69 | 5 | A2 | 選擇題 | A | A | OK |
| 70 | 5 | B1 | 填空 | Türchen | Türchen | OK |
| 71 | 5 | B1 | 填空 | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | 填空 | Christkind | Christkind | OK |
| 73 | 5 | B1 | 填空 | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | 填空 | Kerze | Kerze | OK |
| 75 | 5 | A2 | 填空 | Stern | Stern | OK |
| 76 | 5 | B1 | 改寫 | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | 改寫 | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | 改寫 | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | 改寫 | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | 是非題 | Richtig | Richtig | OK |
| 81 | 5 | B1 | 是非題 | Falsch | Falsch | OK |
| 82 | 5 | A2 | 是非題 | Richtig | Richtig | OK |
| 83 | 6 | B1 | 選擇題 | A | A | OK |
| 84 | 6 | B1 | 選擇題 | B | B | OK |
| 85 | 6 | B1 | 選擇題 | B | B | OK |
| 86 | 6 | B2 | 選擇題 | B | B | OK |
| 87 | 6 | B1 | 選擇題 | A | A | OK |
| 88 | 6 | B2 | 選擇題 | B | B | OK |
| 89 | 6 | B2 | 選擇題 | B | B | OK |
| 90 | 6 | B2 | 選擇題 | A | A | OK |
| 91 | 6 | B2 | 選擇題 | B | B | OK |
| 92 | 6 | B1 | 選擇題 | B | B | OK |
| 93 | 6 | B2 | 填空 | wird | wird | OK |
| 94 | 6 | B2 | 填空 | ob | ob | OK |
| 95 | 6 | B1 | 填空 | geht | geht | OK |
| 96 | 6 | B2 | 填空 | beginnt | beginnt | OK |
| 97 | 6 | B1 | 填空 | Buße | Buße | OK |
| 98 | 6 | B2 | 填空 | Kirchenjahr | Kirchenjahr | OK |
| 99 | 6 | B2 | 填空 | Friedhof | Friedhof | OK |
| 100 | 6 | B1 | 填空 | Einigung | Einigung | OK |
| 101 | 7 | A2 | 填空 | wird | wird | OK |
| 102 | 7 | A2 | 填空 | werden | werden | OK |
| 103 | 7 | A2 | 填空 | wird | wird | OK |
| 104 | 7 | A2 | 選擇題 | A | A | OK |
| 105 | 7 | B1 | 填空 | stiller | stiller | OK |
| 106 | 7 | B1 | 填空 | weil | weil | OK |
| 107 | 7 | B1 | 改寫 | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | 選擇題 | A | A | OK |
| 109 | 7 | B2 | 填空 | ob | ob | OK |
| 110 | 7 | B2 | 填空 | fraglich | fraglich | OK |
| 111 | 7 | B2 | 改寫 | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | 選擇題 | B | B | OK |
| 113 | 8 | A2 | 完形填空 | A | A | OK |
| 114 | 8 | A2 | 完形填空 | B | B | OK |
| 115 | 8 | A2 | 完形填空 | A | A | OK |
| 116 | 8 | A2 | 完形填空 | B | B | OK |
| 117 | 8 | A2 | 完形填空 | A | A | OK |
| 118 | 8 | A2 | 完形填空 | A | A | OK |
| 119 | 8 | A2 | 完形填空 | B | B | OK |
| 120 | 8 | A2 | 完形填空 | A | A | OK |
| 121 | 8 | B1 | 選擇題 | A | A | OK |
| 122 | 8 | A2 | 選擇題 | B | B | OK |
| 123 | 8 | B1 | 選擇題 | B | B | OK |
| 124 | 8 | B1 | 選擇題 | B | B | OK |
| 125 | 8 | A2 | 選擇題 | B | B | OK |
| 126 | 8 | A2 | 選擇題 | A | A | OK |
| 127 | 8 | B1 | 選擇題 | B | B | OK |
| 128 | 8 | A2 | 選擇題 | B | B | OK |
| 129 | 8 | B1 | 選擇題 | A | A | OK |
| 130 | 8 | A2 | 選擇題 | B | B | OK |
| 131 | 8 | A2 | 選擇題 | B | B | OK |
| 132 | 8 | B1 | 選擇題 | B | B | OK |
| 133 | 8 | A2 | 造句 | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | 造句 | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | 造句 | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | 造句 | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | 翻譯 | 德甲週五回歸。 | 德甲週五回歸。 | OK |
| 138 | 8 | A2 | 翻譯 | 週日市集休息。 | 週日市集休息。 | OK |
| 139 | 8 | B1 | 翻譯 | 我正在做將臨期日曆。 | 我正在做將臨期日曆。 | OK |
| 140 | 8 | B1 | 翻譯 | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | 配對 | c | c | OK |
| 142 | 8 | B1 | 配對 | a | a | OK |
| 143 | 8 | B1 | 配對 | d | d | OK |
| 144 | 8 | B1 | 配對 | b | b | OK |
| 145 | 8 | A2 | 對話補全 | A | A | OK |
| 146 | 8 | A2 | 對話補全 | B | B | OK |
| 147 | 8 | A2 | 對話補全 | A | A | OK |
| 148 | 8 | B1 | 對話補全 | A | A | OK |
| 149 | 8 | A2 | 對話補全 | A | A | OK |
| 150 | 8 | B1 | 寫作 | 開放任務 — 依寫作框中的要點進行 | 開放任務 | PREFIX |

Logs: `zh-tw/rebuild1.log`, `zh-tw/build.log`, `zh-tw/measure1.log`, `transform-zh-tw.log`, `zh-tw/keycheck-150.json`, `zh-tw/freeze-direct.json`.
