# EDITION RECORD — 2026-W47 ko-de (run 2, rebuild; 2026-11-11)

- Slug: `2026-w47-ko-de` (target ko, reader English). Core: `core-ko` run 10.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-de.json`, `gen-map-de.py` via `mk-de.py` + `de-replace.json`); apply log `apply-de.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-EN.pdf` — **45,262,664 bytes**, SHA-256 `571699d675bd31f2cc656698df05908e6843517b8cc28b5e0b849a0f6f48cc18`
- Web PDF: `Lucerna-VOL4-KO-EN-web.pdf` — **4,013,441 bytes** (< 7 MB), SHA-256 `02203d2490905b9d863c935ede7b378eb87bd00ce9bf5069ab8bbc2f109d4323`
- Text export: `2026-w47-ko-de.text.md` — 26,389 bytes, 332 items, SHA-256 `7a8f6cef233eb3fe0ef19d1dc7cafed339d2dad740373d8e58e858632ced845d`
- `ABSTRACT.txt` — 305 bytes, SHA-256 `1187194316bea8381ec48d359fd41698d6e18e8e4dfa090889df92724fabc812`
- 8 SVGs in `svg/` (run 2 hashes in `de/sha-de-run2.txt`).

## Gates (all pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 2) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2457, P7 teaser 2539.22 | `de/build-de-run2.log` |
| boxtitle width | 8/8 titles ≤ 386.5px (run 2: P3 `Wichtig` 319.6px, P5 `Jugendzahlen` 345.7px) | `de/boxtitle-de-run2` (inline) |
| U+2019 scan (8 SVGs, run 2) | 0 | re-run on run-2 SVGs (measured inline) |
| occlusion audit | **0 flags** (selftest OK, 6 classes fired, clean controls silent) | `de/occlusion-de2.json` / `de/occlusion-de2.log` |
| p8.py extract | 150/150 noted | `de/p8-extract-de.log`, `de/p8-de.json` |
| p8.py compare vs core | CLEAN, keydiff `[137, 138]` (E-group re-aimed, W46 precedent) | `de/p8-compare-de.log` |
| freeze diff vs core | added CJK 7, all U+3000 (footer 3 vs 2 full-width spaces; P1 offset by band sub) | `de/freeze-diff-de.log` |
| freeze baseline (/usr/bin/python3) | **8/8 byte-identical** | `de/freeze-de.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `de/check-de.log` |
| check_gloss (scratch copy) | gloss fails 0 | `de/check-de.log` |
| print/web text layers | byte-identical, 52,009 bytes each | `de/textlayer-diff-de.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `de/keycheck-de.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `de/style11-de.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `de/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 0 Chinese characters in `<text>` | measured inline |

## Fixes in this edition

1. **P2-feature FLOW OVERFLOW in German (run 1)**: `!! FLOW OVERFLOW [P2-feature] col 2 y=1171 need 390 bottom 1540` — the shopping-list box (390px) did not fit in the remaining column, was clamped to the feature bottom and painted OVER the D-day strip (occlusion audit: 7 flags — 3 COVER on shopping-list lines, 4 TEXTX vs the strip/exercise header). Root cause: the 봉사활동 gloss wrapped to 3 lines in German (`Hinweis — … = ehrenamtliche Arbeit …`, +1 line = +29.7px vs en), pushing the box past the bottom (en ended at 1531 with only 9px spare). Fix: gloss shortened to `봉사활동 = Ehrenamt · 이웃 = Nachbar · 따뜻하다 = warm` (2 lines, verified with core `svglib.wrap`, prefix included). All other P2 glosses measured: 효능 2, 아삭하다 2, 조사하다 3 in both en and de (identical y-coords, no fix). Rebuilt as run 2: P2-feature ends 1531 (same as en), 0 warnings, occlusion 0 flags. Lesson added to the ko family: always measure gloss wraps WITH the reader-language gloss prefix — the prefix alone can cost a line.
2. **Box titles wider than the 386.5px inner width** (run 1, same defect class as en): P3 `김치의 날에 알아 둘 것　Gut zu wissen` 389.4px, P5 `이번 주 청년 숫자　Zahlen der Jugend` 396.8px. Shortened: P3 → `Wichtig` (319.6px), P5 → `Jugendzahlen` (345.7px); others kept (P1 `In Zahlen` 312.9, P2 hanneung `Anmeldung` 264.2, P2 shopping `Einkaufsliste` 326.7, P7 clinic `Fehlerklinik` 248.3, P7 frame `Muster der Woche` 341.3, P7 letters `Leserecke` 246.9). `boxtitle-ko.py` 8/8 after re-apply.
3. **Map generation pitfall (recorded)**: `de-replace.json` had a stray `{` at the start of the second block (JSON error, fixed) and the Frame-entry value in the en source is a literal backslash escape `“` (not a real “ char), so the replace table needed a separate backslash-form key to match. `gen-map-de.py` initially wrote `map-en.json` / printed `GEN-MAP-EN`; fixed in `mk-de.py` and the current file.

## Adjudicated (not defects — inherited from core or by design)

- P8 match-item notes end with the option letter repeated (`25. d — … 199.456 Won d`, `26. a — … 22. Nov. a`): the letter is in the SOURCE note literal itself, core's own convention (`김장비용=四口之家199,456韩元 d` in core-ko); the de map translated the note text and kept the letter.
- #40/#123/#124 note "Weatheri-Prognose": core's own rendering of 웨더아이 (private weather company, corrected in core run 4) — not a typo.
- P8 #150 key renders as `✓` in both core and edition (verified: core extract #150 == `'✓'`); the "(offene Aufgabe — Mustertext unten)" text is the exercise stem, not the printed key.
- P7 VOL.5 count 3 (core) → 2 (de): core's `lko` Korean disclosure line was removed by design (single reader-language disclosure replaces `lcn`; `lko`/`lcn2` lines + render lines removed, W46 ko-de precedent).
- text.md 332 items vs core 333: `textmd.py`'s `is_prose` drops the bare 3-letter Latin word "Alle" (P1 contents 8면 row level); the SVG/PDF render "Alle" correctly (visible on the P1 render). Export quirk, not a content gap.
- Freeze diff added CJK 7, all U+3000 (ideographic space, footer): same pattern as de-family Latin editions.
- KEYS_HALF / NOTE_WRAP: not present in ko core or shared tools; ko P8 keys already use dash style `n. key — note`, satisfied by construction.
- P8 answer-note person names: only personal name is 민준 (Minjun, #129 "Minjun geht am Mittwoch zur Vorversammlung", #135 note) — standard Revised Romanization, consistent within the edition; no sumo-style romaji issue (ja-family class does not apply here). Team/company names (Samsung, kt wiz, KIA, LG, FC Seoul, Weatheri, KBO) match core's own renderings.
- P7 teaser headroom is 40.8px (footer 2580 − teaser 2539.2) — tighter than core (32.3px) but inside limits; do not lengthen the P7 disclosure.
- De-specific renderings (W46 ko-de precedent where noted): CSAT kept; Kimchi-Tag; Kimjang-Kosten; Vorversammlung (예비소집); Geschichtsprüfung (한능검); Forstbehörde (Forestry Service); Weatheri kept; German date `18. Nov.`; German numbers `199.456 Won` / `9,0 %`; score `4:1`; gloss prefix `Hinweis — `; footer `Lucerna　KOREANISCHE WOCHENZEITUNG VOL.4　Koreanischer Text　Erklärungen auf Deutsch`; page line `Seite {n} von {total}`; writing note `Mustertext in Abschnitt H auf dieser Seite ({NCHARS} Zeichen)`; writing key `(offene Aufgabe — Mustertext unten)`.

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (English) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | Satz ergänzen | 1 | 18. Nov. ist D-1 | OK |
| 2 | 1 | Satz ergänzen | 김장 | Die Kimchi-Saison läuft auf Hochtouren | OK |
| 3 | 1 | Satz ergänzen | 19 | Die CSAT ist am Donnerstag, 19. Nov. | OK |
| 4 | 1 | Satz ergänzen | 3 | 16. Nov. ist D-3 | OK |
| 5 | 1 | Satz ergänzen | 4승 1패 | Samsung schlug kt 4:1 | OK |
| 6 | 1 | Satz ergänzen | 11 | Anmeldung für freie Plätze ab 11. Nov. | OK |
| 7 | 1 | Auswahl | A | 18. Nov. ist D-1 | OK |
| 8 | 1 | Auswahl | A | Die Kimjang-Kosten sanken um 9,0 % gegenüber dem Vorjahr | OK |
| 9 | 1 | Auswahl | A | Der Kimchi-Tag ist Sonntag, 22. Nov. | OK |
| 10 | 1 | Auswahl | A | Samsung gewann die Korean Series | OK |
| 11 | 2 | Auswahl | A | 20 Kohlköpfe: 54.980 Won | OK |
| 12 | 2 | Auswahl | A | Die Kimjang-Kosten sanken um 9,0 % | OK |
| 13 | 2 | Auswahl | A | Der Kimchi-Tag ist Sonntag, 22. Nov. | OK |
| 14 | 2 | Auswahl | A | Die Geschichtsprüfung ist Samstag, 28. Nov. | OK |
| 15 | 2 | Auswahl | A | Das WiKim-Festival ist Freitag, 20. Nov. | OK |
| 16 | 2 | Satz ergänzen | 한창 | Die Kimchi-Saison läuft auf Hochtouren | OK |
| 17 | 2 | Satz ergänzen | 22 | Der Kimchi-Tag ist der 22. Nov. | OK |
| 18 | 2 | Satz ergänzen | 54,980 | 20 Kohlköpfe: 54.980 Won | OK |
| 19 | 2 | Satz ergänzen | 토 | Die Geschichtsprüfung ist am Samstag | OK |
| 20 | 2 | Satz ergänzen | 배추 | Die Kosten sanken, weil Kohl billiger ist | OK |
| 21 | 2 | Satz ergänzen | 199,456 | Kimjang für vier: 199.456 Won | OK |
| 22 | 2 | Satz ergänzen | 54,980 | 20 Kohlköpfe: 54.980 Won | OK |
| 23 | 2 | Satz ergänzen | 26.5 | 20 Kohlköpfe, 26,5 % weniger als im Vorjahr | OK |
| 24 | 2 | Satz ergänzen | 13 | Anmeldung für freie Plätze: 11.–13. Nov. | OK |
| 25 | 2 | Paare zuordnen | d | 김장비용 = Kimjang für vier, 199.456 Won d | OK |
| 26 | 2 | Paare zuordnen | a | 김치의 날 = 22. Nov. a | OK |
| 27 | 2 | Paare zuordnen | c | 위킴 페스티벌 = 20. Nov. in Seoul c | OK |
| 28 | 2 | Paare zuordnen | b | 한능검 = kurz für die Geschichtsprüfung b | OK |
| 29 | 3 | Auswahl | A | Der Kimchi-Tag ist der 22. Nov. | OK |
| 30 | 3 | Auswahl | B | 22 steht für Kimchis 22 Wirkungen | OK |
| 31 | 3 | Auswahl | A | Das WiKim-Festival ist Freitag, 20. Nov. | OK |
| 32 | 3 | Auswahl | B | Naejangsan: Forstbehörde-Prognose, Höhepunkt 4. Nov. | OK |
| 33 | 3 | Auswahl | A | Die Forstbehörde zählt 50 % der Blätter | OK |
| 34 | 3 | Satz ergänzen | 절정 | Das schönste Laub heißt 절정 | OK |
| 35 | 3 | Satz ergänzen | 예보 | Prognosedaten weichen von beobachteten Daten ab | OK |
| 36 | 3 | Satz ergänzen | 관측 | Tatsächlich beobachtet am 16. Okt. | OK |
| 37 | 3 | Satz ergänzen | 김치의 날 | Der 22. Nov. ist der Kimchi-Tag | OK |
| 38 | 3 | Satz ergänzen | 발효 | Kimchi ist ein fermentiertes Lebensmittel | OK |
| 39 | 3 | Satz ergänzen | 22 | Kimchi hat 22 Wirkungen | OK |
| 40 | 3 | Satz ergänzen | 11 | Naejangsan: Weatheri-Prognose 11. Nov. | OK |
| 41 | 3 | Satz ergänzen | 4 | Naejangsan: Forstbehörde-Prognose 4. Nov. | OK |
| 42 | 3 | Satz ergänzen | 20 | Das WiKim-Festival ist der 20. Nov. | OK |
| 43 | 3 | Paare zuordnen | b | 내장산 = Weatheri-Prognose 11. Nov. b | OK |
| 44 | 3 | Paare zuordnen | a | 월출산 = Forstbehörde-Prognose 9. Nov. a | OK |
| 45 | 3 | Paare zuordnen | d | 두륜산 = Forstbehörde-Prognose 11. Nov. d | OK |
| 46 | 3 | Paare zuordnen | c | 설악산 = tatsächlich beobachtet am 16. Okt. c | OK |
| 47 | 4 | Auswahl | A | Samsung gewann die Korean Series | OK |
| 48 | 4 | Auswahl | C | Die Serie endete 4:1 | OK |
| 49 | 4 | Auswahl | B | Spiel 5, 8. Nov. in Daegu: Samsung 12:1 | OK |
| 50 | 4 | Auswahl | A | Spiel 1: kt gewann 8:7 | OK |
| 51 | 4 | Auswahl | B | Samsungs erster Titel seit 12 Jahren | OK |
| 52 | 4 | Satz ergänzen | 4승 1패 | Samsung schlug kt 4:1 | OK |
| 53 | 4 | Satz ergänzen | 수원 | Die Spiele 1 und 2 waren in Suwon | OK |
| 54 | 4 | Satz ergänzen | 12대 1 | Spiel 5: Samsung gewann 12:1 | OK |
| 55 | 4 | Satz ergänzen | 12 | Samsung gewann nach 12 Jahren wieder | OK |
| 56 | 4 | Satz ergänzen | 4연승 | Samsung gewann viermal in Folge nach einer Niederlage | OK |
| 57 | 4 | Umformen | 삼성이 kt wiz를 이겼어요. | 이기다: Vergangenheit 이겼어요 | OK |
| 58 | 4 | Umformen | 1차전이 수원에서 열렸어요. | 열리다: Vergangenheit 열렸어요 | OK |
| 59 | 4 | Umformen | 한국시리즈가 끝났어요. | 끝나다: Vergangenheit 끝났어요 | OK |
| 60 | 4 | Umformen | 삼성이 5차전에서 이겼어요. | 이기다: Vergangenheit 이겼어요 | OK |
| 61 | 4 | Paare zuordnen | c | 준플레이오프 = KIA gewann dreimal in Folge c | OK |
| 62 | 4 | Paare zuordnen | d | 플레이오프 = Samsung gewann 3:2 d | OK |
| 63 | 4 | Paare zuordnen | a | 한국시리즈 = Samsung gewann 4:1 a | OK |
| 64 | 4 | Paare zuordnen | b | K리그1 = Seoul gewann vorzeitig b | OK |
| 65 | 5 | Auswahl | A | Die Vorversammlung ist Mittwoch, 18. Nov. | OK |
| 66 | 5 | Auswahl | B | Die CSAT beginnt um 8:40 Uhr | OK |
| 67 | 5 | Auswahl | A | Prüflinge dieses Jahr: 551.864 | OK |
| 68 | 5 | Auswahl | B | Die Ergebnisse kommen Freitag, 11. Dez. | OK |
| 69 | 5 | Auswahl | A | Sei am Prüfungstag bis 8:10 Uhr im Raum | OK |
| 70 | 5 | Satz ergänzen | 예비소집 | Hol deine Zulassung bei der Vorversammlung ab | OK |
| 71 | 5 | Satz ergänzen | 수험표 | Hol deine Zulassung ab und prüfe den Prüfungsort | OK |
| 72 | 5 | Satz ergänzen | 2,310 | 2.310 Prüflinge weniger als im Vorjahr | OK |
| 73 | 5 | Satz ergänzen | 성적 | Die Ergebnisse kommen am 11. Dez. | OK |
| 74 | 5 | Satz ergänzen | 김치의 날 | Der 22. Nov. ist der Kimchi-Tag | OK |
| 75 | 5 | Satz ergänzen | 551,864 | Prüflinge dieses Jahr: 551.864 | OK |
| 76 | 5 | Satz ergänzen | 1,312 | Prüfungsorte im ganzen Land: 1.312 | OK |
| 77 | 5 | Satz ergänzen | 85 | 85 Prüfungsbezirke im ganzen Land | OK |
| 78 | 5 | Satz ergänzen | 10 | Am Prüfungstag beginnen die Ämter um 10:00 Uhr | OK |
| 79 | 5 | Sätze bilden | 수험생은 열심히 공부해요. | Wortstellung: Subjekt + Adverb + Verb | OK |
| 80 | 5 | Sätze bilden | 우리는 수험생을 응원해요. | Subjekt + Objekt + Verb | OK |
| 81 | 5 | Sätze bilden | 비행기는 듣기 시간에 뜨지 않아요. | Keine Flüge während des Hörtests | OK |
| 82 | 5 | Sätze bilden | 친구는 김치를 나눠 줘요. | Ein Freund teilt Kimchi | OK |
| 83 | 6 | Auswahl | B | Diese Woche hat die Korean Series ein Ergebnis | OK |
| 84 | 6 | Auswahl | A | Umfrage vom 9. Nov.: Kimjang-Kosten 199.456 Won | OK |
| 85 | 6 | Auswahl | B | Die prognostizierten Laubtermine sind vorbei | OK |
| 86 | 6 | Auswahl | C | Die CSAT-Ergebnisse kommen am 11. Dez. | OK |
| 87 | 6 | Auswahl | A | Letzte Woche war die Serie nur ein Terminplan | OK |
| 88 | 6 | Auswahl | A | Spiel 1: kt gewann 8:7 | OK |
| 89 | 6 | Auswahl | B | Der Wetterdienst beobachtet etwa 80 % | OK |
| 90 | 6 | Auswahl | A | Ein Kohlkopf, 16. Okt.: 5.557 Won | OK |
| 91 | 6 | Auswahl | A | Bezugsdatum der Kimjang-Umfrage ist der 9. Nov. | OK |
| 92 | 6 | Auswahl | A | Prüflinge dieses Jahr: 551.864 | OK |
| 93 | 6 | Satz ergänzen | 발표 | Ein veröffentlichter Terminplan kann sich ändern | OK |
| 94 | 6 | Satz ergänzen | 결과 | Ergebnisse gibt es erst nach den Spielen | OK |
| 95 | 6 | Satz ergänzen | 기준 | Daten weichen ab, weil die Kriterien abweichen | OK |
| 96 | 6 | Satz ergänzen | 날짜 | Wenn du Nachrichten liest, prüfe zuerst das Datum | OK |
| 97 | 6 | Richtig oder falsch | 틀리다 | Die Sondermaßnahmen gelten nur am 19. Nov. | OK |
| 98 | 6 | Richtig oder falsch | 맞다 | Samsung gewann den Titel 4:1 | OK |
| 99 | 6 | Richtig oder falsch | 틀리다 | Prognosedaten sind keine beobachteten Daten | OK |
| 100 | 6 | Richtig oder falsch | 맞다 | Die Ergebnisse kommen am 11. Dez. | OK |
| 101 | 7 | Satz ergänzen | 김장 | Kimchi für den Winter einlegen = 김장 | OK |
| 102 | 7 | Auswahl | A | Der Kimchi-Tag ist der 22. Nov. | OK |
| 103 | 7 | Satz ergänzen | 절임배추 | Im Voraus gesalzener Kohl | OK |
| 104 | 7 | Auswahl | A | Das Gewürz enthält gesalzene Garnelen | OK |
| 105 | 7 | Satz ergänzen | D-1 | 18. Nov. ist D-1 | OK |
| 106 | 7 | Auswahl | B | D-3 = 16. Nov. | OK |
| 107 | 7 | Satz ergänzen | 데이 | Der 19. Nov. ist D-Day | OK |
| 108 | 7 | Auswahl | A | D-1 heißt: Die Prüfung ist morgen | OK |
| 109 | 7 | Satz ergänzen | 기준 | Die Daten weichen ab, weil die Kriterien abweichen (Seite 3) | OK |
| 110 | 7 | Auswahl | A | Der Wetterdienst beobachtet etwa 80 % | OK |
| 111 | 7 | Satz ergänzen | 결과 | Ergebnisse gibt es erst nach den Spielen | OK |
| 112 | 7 | Auswahl | B | Ankündigungen und Ergebnisse unterscheiden | OK |
| 113 | 8 | Lückentext | A | Der Kimchi-Tag ist Sonntag, 22. Nov. | OK |
| 114 | 8 | Lückentext | A | Die CSAT ist am Donnerstag, 19. Nov. | OK |
| 115 | 8 | Lückentext | A | Die Geschichtsprüfung ist Samstag, 28. Nov. | OK |
| 116 | 8 | Lückentext | A | Das WiKim-Festival ist Freitag, 20. Nov. | OK |
| 117 | 8 | Lückentext | A | Samsung gewann den Titel 4:1 | OK |
| 118 | 8 | Lückentext | A | Kimjang für vier: 199.456 Won | OK |
| 119 | 8 | Lückentext | A | 20 Kohlköpfe: 54.980 Won | OK |
| 120 | 8 | Lückentext | A | Prüflinge dieses Jahr: 551.864 | OK |
| 121 | 8 | Auswahl | A | Prüflinge dieses Jahr: 551.864 | OK |
| 122 | 8 | Auswahl | B | Prüfungsorte im ganzen Land: 1.312 | OK |
| 123 | 8 | Auswahl | A | Naejangsan: Forstbehörde-Prognose, Höhepunkt 4. Nov. | OK |
| 124 | 8 | Auswahl | B | Naejangsan: Weatheri-Prognose, Höhepunkt 11. Nov. | OK |
| 125 | 8 | Auswahl | B | Duryunsan: Forstbehörde-Prognose, Höhepunkt 11. Nov. | OK |
| 126 | 8 | Auswahl | A | Spiel 1: kt gewann 8:7 | OK |
| 127 | 8 | Auswahl | A | Anmeldung für freie Plätze: 11.–13. Nov. | OK |
| 128 | 8 | Auswahl | B | Die Waldbrand-Warnzeit endet am 15. Dez. | OK |
| 129 | 8 | Auswahl | B | Minjun geht am Mittwoch zur Vorversammlung | OK |
| 130 | 8 | Auswahl | A | Er nimmt am Donnerstag an der CSAT teil | OK |
| 131 | 8 | Auswahl | B | Er teilt am Sonntag Kimchi mit der Familie | OK |
| 132 | 8 | Auswahl | C | Nächste Woche bereitet er sich auf die Geschichtsprüfung vor | OK |
| 133 | 8 | Sätze bilden | 저는 수요일에 예비소집에 가요. | Wortstellung: Subjekt + Zeit + Ort + Verb | OK |
| 134 | 8 | Sätze bilden | 우리는 김치를 나눠 먹어요. | Subjekt + Objekt + Verb | OK |
| 135 | 8 | Sätze bilden | 민준이는 한국사를 좋아해요. | 좋아하다 = mögen | OK |
| 136 | 8 | Sätze bilden | 수험생은 도서관에서 공부해요. | Für den Handlungsort nimm 「에서」. | OK |
| 137 | 8 | Übersetzen | Der 22. Nov. ist der Kimchi-Tag. | Siehe Seite 2 | OK |
| 138 | 8 | Übersetzen | Samsung gewann den Titel nach 12 Jahren. | Siehe Seite 4 | OK |
| 139 | 8 | Übersetzen | 11월 18일은 예비소집이에요. | Siehe Seite 5 | OK |
| 140 | 8 | Übersetzen | 일요일에는 가족과 김치를 나눠 먹어요. | Siehe Abschnitt C auf Seite 8 | OK |
| 141 | 8 | Paare zuordnen | b | 예비소집 = Vorversammlung b | OK |
| 142 | 8 | Paare zuordnen | c | 김치의 날 = 22. Nov. c | OK |
| 143 | 8 | Paare zuordnen | a | 발효 = der Gärungsprozess a | OK |
| 144 | 8 | Paare zuordnen | d | 우승 = Meisterschaft d | OK |
| 145 | 8 | Lückentext | A | Er geht am Mittwoch zur Vorversammlung | OK |
| 146 | 8 | Lückentext | A | Der Kimchi-Tag ist der 22. Nov. | OK |
| 147 | 8 | Lückentext | A | Die Geschichtsprüfung ist am 28. Nov. | OK |
| 148 | 8 | Lückentext | A | Kimjang für vier: 199.456 Won | OK |
| 149 | 8 | Lückentext | A | Die Ergebnisse kommen am 11. Dez. | OK |
| 150 | 8 | Schreiben | (offene Aufgabe — Mustertext unten) | Mustertext in Abschnitt H auf dieser Seite (169 Zeichen) | OK ✓ |
