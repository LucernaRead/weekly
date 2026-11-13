# EDITION RECORD — 2026-W47 de-ja (German target, Japanese reader)

Rebuild-B build 1, 2026-11-11 ~08:43 UTC. **ALL GATES PASS on the first rebuild run.**

Rebuild of rebuild 3 from the new core-de build15. Only delta: the P3 Q34 stem
corrected to the singular form matching key `Weihnachtsmarkt` (core build15,
proof5 (a) zero findings). `tr_ja.py` / `vals_ja.json` unchanged (Q150 note
still deleted, as in rebuild 3).

## Deliverables

- Print PDF: `Die-Lucerna-VOL4-de-ja.pdf` — 23,901,736 B, sha256 `f412f930242d16c87a7fb783506f6e92e5020a40e323edfdb1243dfd82db459d`
- Web PDF: `Die-Lucerna-VOL4-de-ja-web.pdf` — 2,113,024 B, sha256 `29f65fec5681e46f5b927171163c5d66559e61ed275d998583653574d8e8294a` (52,873 text bytes; < 7 MB)
- Text export: `2026-w47-de-ja.text.md` — 51,913 B (42,950 chars, 591 entries, 150 exercises), sha256 `a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69`
- ABSTRACT.txt: 426 B (Japanese)

## Gates (rebuild-B build 1)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- measure 24/24 PASS (`ja-measure-rblog.log`); precheck 0 FAIL; boxtitle 7/7
- verify TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags
- p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150]
- freeze (tools/freeze.py, venv interpreter): exit 0, TOTAL added CJK 2,994 (Japanese layer)
- freeze_direct rendered 8/8 (frozen 144/164/200/166/179/173/163/183; sha8 b01ba1b1 / 2db0dd83 / 2dd3b3f2 / df1bebf7 / e7b235f9 / 89156519 / b854370f / 1c855c30 — only P3 sha8 moved vs rebuild 3's 5c2bc909); source level: only 4 unaccounted strings, all the documented JP font switch (removed 1 `Noto Serif CJK SC`, added 3 `JP` / `Noto Sans CJK JP` / `Noto Serif CJK JP`; transform.py lines 198–202). The 07:30-diagnostic stem pair (removed 2 / added 4) is GONE — core and edition stems now match. Removed 516 / added 524 (prev diagnostic 517/525).
- print/web text layer identical (default multiset 52,872 B / 52,873 B; -raw normalised 51,709 B both)
- P8 min font 9.94pt (≥ 9.75pt); chips 141 (10/15/18/15/18/18/12/35), P8 A2 22 / B1 13 / B2 0
- U+2019 full scan over 8 SVGs = 0; box titles 7/7 fit (max 395.5px per boxtitle)
- CJK residual audit: kanji-only scan (U+4E00–U+9FFF): 1,358 chars in 8 SVGs; only 2 outside tr_ja.py values — 色/蛾, both from the core's own `<title>Lucerna 三色蛾</title>` in p1-front.svg, byte-identical in core-de; zero leftover Simplified Chinese in translated text
- keycheck 149/150 (only Q150 PREFIX, as rebuild 3). One transient RC=1 on the first post-build invocation with identical 149/150 output; re-ran twice, RC=0 both.
- Q34: new stem 1× in content34.py, .text.md, P3 SVG, print-PDF text layer, web-PDF text layer; old stem 0× in all (and 0× across the edition dir after the KIT rewrite); P3 visually confirmed as the new stem
- Visual proofread: 8/8 pages at 100 dpi, zero findings (renders /tmp/ja-rb-proof-*.png)

## Build history

- Rebuild 3 (5th shift, 2026-11-11 07:15 UTC): ALL GATES PASS after the Q150-note fix (build 1 failed 5 gates — occlusion 2 flags + p8 compare SHORT missing [150]; build 2 fixed occlusion but p8 compare still failed missing [150]).
- Rebuild-B build 1: ALL GATES PASS first run. No fixes needed; only the core Q34 stem changed.

## Flow ends (rebuild-B build 1)

P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315, P5-main 996, P5-ex 2441 (= core), P6-main 747, P6-ex 2496, P7-A2 1278 / B1 1342 / B2 1306, P8-battery 1409, P8-keys 2473 (bottom 2560, spare 87px). Identical to rebuild 3.

## 150-key check (keycheck.py, rebuild-B build 1)

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

Logs: `ja-rebuild-B.log`, `ja/build.log`, `ja-measure-rblog.log`, `ja-transform-stdout.log`, `ja/keycheck-150.json`, `ja/freeze-direct.json`, `freeze-direct-ja-rb.log`.
