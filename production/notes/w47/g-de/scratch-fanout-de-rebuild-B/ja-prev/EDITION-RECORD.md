# EDITION RECORD — 2026-W47 de-ja (German target, Japanese reader)

Rebuild 3, 2026-11-11 07:14–07:15 UTC. **ALL GATES PASS.**

## Deliverables

- Print PDF: `Die-Lucerna-VOL4-de-ja.pdf` — 23,901,730 B, sha256 `19d5a14a2966e6865a8bfb28bd74fd0c05b10594a37670fe7db4d84596e5605a`
- Web PDF: `Die-Lucerna-VOL4-de-ja-web.pdf` — 2,113,005 B, sha256 `8dc87c2363a02cb2b098f55614e3866b31f5796c91ea6e8d3d393fbfbb66236d` (52,874 text bytes; < 7 MB)
- Text export: `2026-w47-de-ja.text.md` — 51,914 B (42,951 chars, 591 entries, 150 exercises), sha256 `c780542f0835bdaef6cfd52939346ecec6daa06d6b0edb4e348201942b2a3951`
- ABSTRACT.txt: 426 B (Japanese)

## Gates (rebuild 3)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- measure 24/24 PASS (`ja/measure4.log`)
- verify TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags
- p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150]
- freeze (tools/freeze.py, venv interpreter): exit 0, TOTAL added CJK 2,994 (Japanese layer)
- freeze_direct rendered 8/8 (frozen 144/164/200/166/179/173/163/183; sha8 b01ba1b1 / 2db0dd83 / 5c2bc909 / df1bebf7 / e7b235f9 / 89156519 / b854370f / 1c855c30); source level at build time: only 4 unaccounted strings, all the documented JP font switch (transform.py lines 198–202). NOTE: the json was re-run at ~07:30 as a diagnostic after the core-side change (zh-tw KIT §6) and now additionally lists that German sentence pair (unaccounted removed 2 / added 4); rendered counts/sha8 unchanged.
- print/web text layer identical (default multiset 52,873 B / 52,874 B; -raw normalised 51,710 B both)
- P8 min font 9.94pt (≥ 9.75pt); chips 141 (10/15/18/15/18/18/12/35), P8 A2 22 / B1 13 / B2 0
- U+2019 full scan over 8 SVGs = 0; box titles 8/8 inside (max end 1849.1)
- CJK residual audit: 4,005 CJK chars in 8 SVGs, 0 not in tr_ja.py values (zero leftover Simplified Chinese)
- Visual proofread: 8/8 pages at 100 dpi, zero findings (renders /tmp/ja3-proof-*.png)

## Build history

- Build 1: FAILED 5 gates — occlusion 2 flags (P1 ZAHLEN column jump) + p8 compare SHORT missing [150].
- Build 2: occlusion FIXED (ZAHLEN head → 数字 337.9px; word-of-week → 5ページ。 410.5px, 1 line; Q150 key shortened), p8 compare STILL failed missing [150] — wrap simulation proved the kinsoku cascade breaks the line after the Q150 dash regardless of key tail length.
- Build 3: ALL GATES PASS. Fix: Q150 note removed (EN key 'Marked against the points listed' → ''; gen_tr diff exactly 1 line). 14 wrap-simulation variants tested; only removing a whole note (Q147/Q148/Q149 dialogue note or Q150 note) moves the break; all shorten-only variants fail. Q150's procedural grading note was removed rather than a dialogue verb-form note. REG key unchanged; keycheck still 149/150 with Q150 PREFIX, as the Latin editions.

## Flow ends (rebuild 3)

P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315, P5-main 996, P5-ex 2441 (= core), P6-main 747, P6-ex 2496, P7-A2 1278 / B1 1342 / B2 1306, P8-battery 1409, P8-keys 2473 (bottom 2560, spare 87px).

## 150-key check (keycheck.py, rebuild 3)

149/150 exact. Only Q150 differs, and only as PREFIX (expected): extracted `自由課題` is a prefix of the REG key `自由課題 — 枠のポイントに従おう`. p8 compare status CLEAN with keydiff [137, 138, 139, 150] (137–139 are the expected translate-to-Japanese items; 150 is the Q150 PREFIX).

| n | page | level | type | REG key | extracted |
|---:|---:|---|---|---|---|
| 1 | 1 | A2 | 穴埋め | Bundesliga | Bundesliga | OK |
| 2 | 1 | A2 | 穴埋め | Niederlande | Niederlande | OK |
| 3 | 1 | A2 | 穴埋め | Sachsen | Sachsen | OK |
| 4 | 1 | A2 | 穴埋め | Totensonntag | Totensonntag | OK |
| 5 | 1 | B1 | 穴埋め | fünf | fünf | OK |
| 6 | 1 | B1 | 穴埋め | 29. November | 29. November | OK |
| 7 | 1 | A2 | 選択問題 | B | B | OK |
| 8 | 1 | A2 | 選択問題 | A | A | OK |
| 9 | 1 | A2 | 選択問題 | B | B | OK |
| 10 | 1 | A2 | 選択問題 | B | B | OK |
| 11 | 2 | A2 | 穴埋め | 18. November | 18. November | OK |
| 12 | 2 | A2 | 穴埋め | 22. November | 22. November | OK |
| 13 | 2 | A2 | 穴埋め | 29. November | 29. November | OK |
| 14 | 2 | A2 | 穴埋め | Mittwoch | Mittwoch | OK |
| 15 | 2 | A2 | 穴埋め | Sachsen | Sachsen | OK |
| 16 | 2 | A2 | 書き換え | Der Buß- und Bettag ist fast überall abgeschafft worden. | Der Buß- und Bettag ist fast überall abgeschafft worden. | OK |
| 17 | 2 | A2 | 書き換え | Die Schulen in Bayern sind geschlossen geblieben. | Die Schulen in Bayern sind geschlossen geblieben. | OK |
| 18 | 2 | A2 | 書き換え | Viele Menschen sind in die Kirche gegangen. | Viele Menschen sind in die Kirche gegangen. | OK |
| 19 | 2 | B1 | 書き換え | Sachsen hat den Feiertag behalten. | Sachsen hat den Feiertag behalten. | OK |
| 20 | 2 | B1 | 書き換え | Die Märkte sind am Totensonntag geschlossen geblieben. | Die Märkte sind am Totensonntag geschlossen geblieben. | OK |
| 21 | 2 | A2 | 選択問題 | B | B | OK |
| 22 | 2 | A2 | 選択問題 | B | B | OK |
| 23 | 2 | A2 | 選択問題 | A | A | OK |
| 24 | 2 | A2 | 選択問題 | B | B | OK |
| 25 | 2 | A2 | 組み合わせ | d | d | OK |
| 26 | 2 | A2 | 組み合わせ | c | c | OK |
| 27 | 2 | A2 | 組み合わせ | a | a | OK |
| 28 | 2 | A2 | 組み合わせ | b | b | OK |
| 29 | 3 | A2 | 正誤問題 | Richtig | Richtig | OK |
| 30 | 3 | A2 | 正誤問題 | Falsch | Falsch | OK |
| 31 | 3 | A2 | 正誤問題 | Richtig | Richtig | OK |
| 32 | 3 | B1 | 正誤問題 | Falsch | Falsch | OK |
| 33 | 3 | A2 | 正誤問題 | Richtig | Richtig | OK |
| 34 | 3 | A2 | 穴埋め | Weihnachtsmarkt | Weihnachtsmarkt | OK |
| 35 | 3 | A2 | 穴埋め | Glühwein | Glühwein | OK |
| 36 | 3 | A2 | 穴埋め | Lebkuchen | Lebkuchen | OK |
| 37 | 3 | A2 | 穴埋め | Advent | Advent | OK |
| 38 | 3 | A2 | 穴埋め | Weihnachtsbaum | Weihnachtsbaum | OK |
| 39 | 3 | A2 | 選択問題 | B | B | OK |
| 40 | 3 | A2 | 選択問題 | B | B | OK |
| 41 | 3 | A2 | 選択問題 | A | A | OK |
| 42 | 3 | B1 | 選択問題 | A | A | OK |
| 43 | 3 | A2 | 文作り | Am 16. November öffnen die Weihnachtsmärkte in Köln. | Am 16. November öffnen die Weihnachtsmärkte in Köln. | OK |
| 44 | 3 | B1 | 文作り | Am Totensonntag bleiben die Märkte geschlossen. | Am Totensonntag bleiben die Märkte geschlossen. | OK |
| 45 | 3 | A2 | 文作り | Vor dem Dom steht ein großer Weihnachtsbaum. | Vor dem Dom steht ein großer Weihnachtsbaum. | OK |
| 46 | 3 | B1 | 文作り | Die Lichter leuchten schon vor dem ersten Advent. | Die Lichter leuchten schon vor dem ersten Advent. | OK |
| 47 | 4 | B1 | 選択問題 | B | B | OK |
| 48 | 4 | B1 | 選択問題 | B | B | OK |
| 49 | 4 | B1 | 選択問題 | C | C | OK |
| 50 | 4 | B1 | 選択問題 | A | A | OK |
| 51 | 4 | B1 | 選択問題 | B | B | OK |
| 52 | 4 | B1 | 組み合わせ | d | d | OK |
| 53 | 4 | B1 | 組み合わせ | b | b | OK |
| 54 | 4 | B1 | 組み合わせ | c | c | OK |
| 55 | 4 | B1 | 組み合わせ | a | a | OK |
| 56 | 4 | B1 | 穴埋め | mehr | mehr | OK |
| 57 | 4 | B1 | 穴埋め | später | später | OK |
| 58 | 4 | B1 | 穴埋め | früher | früher | OK |
| 59 | 4 | B1 | 穴埋め | mehr | mehr | OK |
| 60 | 4 | B1 | 選択問題 | A | A | OK |
| 61 | 4 | B1 | 選択問題 | B | B | OK |
| 62 | 4 | B1 | 選択問題 | C | C | OK |
| 63 | 4 | B1 | 選択問題 | A | A | OK |
| 64 | 4 | B1 | 選択問題 | B | B | OK |
| 65 | 5 | B1 | 選択問題 | A | A | OK |
| 66 | 5 | B1 | 選択問題 | B | B | OK |
| 67 | 5 | B1 | 選択問題 | B | B | OK |
| 68 | 5 | B1 | 選択問題 | B | B | OK |
| 69 | 5 | A2 | 選択問題 | A | A | OK |
| 70 | 5 | B1 | 穴埋め | Türchen | Türchen | OK |
| 71 | 5 | B1 | 穴埋め | Wunschzettel | Wunschzettel | OK |
| 72 | 5 | B1 | 穴埋め | Christkind | Christkind | OK |
| 73 | 5 | B1 | 穴埋め | Schokolade | Schokolade | OK |
| 74 | 5 | A2 | 穴埋め | Kerze | Kerze | OK |
| 75 | 5 | A2 | 穴埋め | Stern | Stern | OK |
| 76 | 5 | B1 | 書き換え | Die Kinder freuen sich, weil der Advent beginnt. | Die Kinder freuen sich, weil der Advent beginnt. | OK |
| 77 | 5 | B1 | 書き換え | Er bleibt zu Hause, weil es dunkel ist. | Er bleibt zu Hause, weil es dunkel ist. | OK |
| 78 | 5 | B1 | 書き換え | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | Sie geht in die Bibliothek, weil sie ein Buch lesen will. | OK |
| 79 | 5 | B1 | 書き換え | Köln feiert, weil die Weihnachtsmärkte öffnen. | Köln feiert, weil die Weihnachtsmärkte öffnen. | OK |
| 80 | 5 | A2 | 正誤問題 | Richtig | Richtig | OK |
| 81 | 5 | B1 | 正誤問題 | Falsch | Falsch | OK |
| 82 | 5 | A2 | 正誤問題 | Richtig | Richtig | OK |
| 83 | 6 | B1 | 選択問題 | A | A | OK |
| 84 | 6 | B1 | 選択問題 | B | B | OK |
| 85 | 6 | B1 | 選択問題 | B | B | OK |
| 86 | 6 | B2 | 選択問題 | B | B | OK |
| 87 | 6 | B1 | 選択問題 | A | A | OK |
| 88 | 6 | B2 | 選択問題 | B | B | OK |
| 89 | 6 | B2 | 選択問題 | B | B | OK |
| 90 | 6 | B2 | 選択問題 | A | A | OK |
| 91 | 6 | B2 | 選択問題 | B | B | OK |
| 92 | 6 | B1 | 選択問題 | B | B | OK |
| 93 | 6 | B2 | 穴埋め | wird | wird | OK |
| 94 | 6 | B2 | 穴埋め | ob | ob | OK |
| 95 | 6 | B1 | 穴埋め | geht | geht | OK |
| 96 | 6 | B2 | 穴埋め | beginnt | beginnt | OK |
| 97 | 6 | B1 | 穴埋め | Buße | Buße | OK |
| 98 | 6 | B2 | 穴埋め | Kirchenjahr | Kirchenjahr | OK |
| 99 | 6 | B2 | 穴埋め | Friedhof | Friedhof | OK |
| 100 | 6 | B1 | 穴埋め | Einigung | Einigung | OK |
| 101 | 7 | A2 | 穴埋め | wird | wird | OK |
| 102 | 7 | A2 | 穴埋め | werden | werden | OK |
| 103 | 7 | A2 | 穴埋め | wird | wird | OK |
| 104 | 7 | A2 | 選択問題 | A | A | OK |
| 105 | 7 | B1 | 穴埋め | stiller | stiller | OK |
| 106 | 7 | B1 | 穴埋め | weil | weil | OK |
| 107 | 7 | B1 | 書き換え | Viele bleiben zu Hause, weil es dunkel ist. | Viele bleiben zu Hause, weil es dunkel ist. | OK |
| 108 | 7 | B1 | 選択問題 | A | A | OK |
| 109 | 7 | B2 | 穴埋め | ob | ob | OK |
| 110 | 7 | B2 | 穴埋め | fraglich | fraglich | OK |
| 111 | 7 | B2 | 書き換え | Ich finde, dass das Gedenken Stille braucht. | Ich finde, dass das Gedenken Stille braucht. | OK |
| 112 | 7 | B2 | 選択問題 | B | B | OK |
| 113 | 8 | A2 | 穴埋め文 | A | A | OK |
| 114 | 8 | A2 | 穴埋め文 | B | B | OK |
| 115 | 8 | A2 | 穴埋め文 | A | A | OK |
| 116 | 8 | A2 | 穴埋め文 | B | B | OK |
| 117 | 8 | A2 | 穴埋め文 | A | A | OK |
| 118 | 8 | A2 | 穴埋め文 | A | A | OK |
| 119 | 8 | A2 | 穴埋め文 | B | B | OK |
| 120 | 8 | A2 | 穴埋め文 | A | A | OK |
| 121 | 8 | B1 | 選択問題 | A | A | OK |
| 122 | 8 | A2 | 選択問題 | B | B | OK |
| 123 | 8 | B1 | 選択問題 | B | B | OK |
| 124 | 8 | B1 | 選択問題 | B | B | OK |
| 125 | 8 | A2 | 選択問題 | B | B | OK |
| 126 | 8 | A2 | 選択問題 | A | A | OK |
| 127 | 8 | B1 | 選択問題 | B | B | OK |
| 128 | 8 | A2 | 選択問題 | B | B | OK |
| 129 | 8 | B1 | 選択問題 | A | A | OK |
| 130 | 8 | A2 | 選択問題 | B | B | OK |
| 131 | 8 | A2 | 選択問題 | B | B | OK |
| 132 | 8 | B1 | 選択問題 | B | B | OK |
| 133 | 8 | A2 | 文作り | Die Bundesliga kehrt am Freitag zurück. | Die Bundesliga kehrt am Freitag zurück. | OK |
| 134 | 8 | A2 | 文作り | Wir basteln im November einen Adventskalender. | Wir basteln im November einen Adventskalender. | OK |
| 135 | 8 | B1 | 文作り | Am Sonntag sind die Weihnachtsmärkte geschlossen. | Am Sonntag sind die Weihnachtsmärkte geschlossen. | OK |
| 136 | 8 | B1 | 文作り | Die Familie geht am Sonntag auf den Friedhof. | Die Familie geht am Sonntag auf den Friedhof. | OK |
| 137 | 8 | A2 | 翻訳 | ブンデスリーガは金曜日に復帰する。 | ブンデスリーガは金曜日に復帰する。 | OK |
| 138 | 8 | A2 | 翻訳 | 日曜日は市場が休み。 | 日曜日は市場が休み。 | OK |
| 139 | 8 | B1 | 翻訳 | アドベントカレンダーを作っている。 | アドベントカレンダーを作っている。 | OK |
| 140 | 8 | B1 | 翻訳 | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | Am Montag schaue ich zu Hause Deutschland gegen die Niederlande. | OK |
| 141 | 8 | B1 | 組み合わせ | c | c | OK |
| 142 | 8 | B1 | 組み合わせ | a | a | OK |
| 143 | 8 | B1 | 組み合わせ | d | d | OK |
| 144 | 8 | B1 | 組み合わせ | b | b | OK |
| 145 | 8 | A2 | 会話補完 | A | A | OK |
| 146 | 8 | A2 | 会話補完 | B | B | OK |
| 147 | 8 | A2 | 会話補完 | A | A | OK |
| 148 | 8 | B1 | 会話補完 | A | A | OK |
| 149 | 8 | A2 | 会話補完 | A | A | OK |
| 150 | 8 | B1 | 作文 | 自由課題 — 枠のポイントに従おう | 自由課題 | PREFIX |

Logs: `ja/rebuild3.log`, `ja/build.log`, `ja/measure4.log`, `transform-ja4.log`, `ja/keycheck-150.json`, `ja/freeze-direct.json`.
