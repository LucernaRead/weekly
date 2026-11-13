# EDITION RECORD — 2026-W47 ko-ja (run 2; 2026-11-11)

- Slug: `2026-w47-ko-ja` (target ko, reader Japanese). Core: `core-ko` run 11 (fix1) + textmd fix2.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-ja.json`, `gen-map-ja.py` via `mk-lang.py` + `ja-replace.json` / `ja-meta.json`); apply log `apply-ja.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-JA.pdf` — **51,357,740 bytes**, SHA-256 `7bc95f9748e2d07ec16bd3d19e678e3525f1959dc653a9a4a18059ee2cae2d4c`
- Web PDF: `Lucerna-VOL4-KO-JA-web.pdf` — **4,388,239 bytes** (< 7 MB), SHA-256 `9f0567aa3357528ae0e89e682beef7481d02e679965416c5c82bac5316a8a9c0`
- Text export: `2026-w47-ko-ja.text.md` — 35,425 bytes, 450 items, SHA-256 `635ec8afac75dc7859cb362dcf9f3470dfb083a67858790a15006cfa3afd9e97`
- `ABSTRACT.txt` — 342 bytes, SHA-256 `4a9445de3848203250f4d4992a79fb08992dada8cd0f747e2b745746f453157a`
- 8 SVGs in `svg/` (hashes in `ja/sha-ja-run2.txt`).

## Gates (freeze baseline blocked — see Adjudicated; all other gates pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 2) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2454.7 | `ja/build-ja-run2.log` |
| boxtitle width | 8/8 within 386.5px | `ja/boxtitle-ja.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (0 flags) | `ja/occlusion-ja.json` / `ja/occlusion-ja.log` |
| p8.py extract | 150/150 noted | `ja/p8-extract-ja.log`, `ja/p8-ja.json` |
| p8.py compare vs core | [137, 138] | `ja/p8-compare-ja.log` |
| freeze diff vs core | added CJK 2901 (adjudicated — all 307 added / 303 removed strings traced) | `ja/freeze-diff-ja.log` |
| freeze baseline (/usr/bin/python3) | BLOCKED — runtime guard (see Adjudicated); venv run 0/8 | `ja/freeze-ja.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `ja/check-ja.log` |
| check_gloss (scratch copy) | gloss fails 0 | `ja/check-ja.log` |
| print/web text layers | byte-identical, 53,212 bytes each | `ja/textlayer-diff-ja.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt (region spans 163, at-min 158)** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `ja/keycheck-ja.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `ja/style11-ja.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `ja/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 825 | measured inline |

## Fixes in this edition

['P3 box-title OVER (run 1 boxtitle 7/8): `김치의 날에 알아 둘 것\u3000知っておくこと` 393.4px. Shortened in the map source (ja-replace.json: `知っておくこと` → `知っておく`) via mk-lang.py ja + gen-map-ja.py + re-apply; then boxtitle 8/8. The shortened title renders on one line in the P3 box (P3 render).', 'P8 #81 answer note wrapped to a second line (run 1): the note `リスニングの時間は飛行機が飛ばない` (15 chars) was too long for the 13.3px answer line (463.5px vs a ~420–464px wrap threshold), so the P8 key printed as `81. … —` with the note on the next line, and p8.py compare failed SHORT missing=[81]. Shortened in the map source (ja-replace.json: `リスニングの時間は飛行機が飛ばない` → `聴解中は飛行機が飛ばない`, 12 chars, 397.6px — comfortably below the widest fitting answer line, 420.1px) via mk-lang.py ja + gen-map-ja.py + re-apply (run 2). Now a single line: `81. 비행기는 듣기 시간에 뜨지 않아요. — 聴解中は飛行機が飛ばない`; p8.py compare CLEAN. Only P8 SVG changed between run 1 and run 2; text.md byte-identical (note not in export set).', 'Frame clean at map level: content7.py:81 `枠組み：「〜のあと」。たずね方：「〜 후에 뭐 해요?」` — no post-apply fix needed']

## Adjudicated (not defects — inherited from core or by design)

["FREEZE BASELINE BLOCKED (not an edition defect — a tooling conflict for the coordinator): tools/freeze.py gained a runtime guard at 2026-11-11 12:00 (uncommitted working-tree change) that aborts unless Pillow major == 13 (tools/venv). It contradicts the family's interpreter lock (core KIT fix #15 + task brief: build + freeze under /usr/bin/python3, PIL 10.2.0). Evidence: freeze.py baseline under the venv on this sys-built edition gives 0/8 (all 8 SVGs differ — dual-stack drift, PIL 13 re-measures Korean spacing ~1.11px wider per space boundary); the 8 editions built before 12:00 (en/de/es/fr/it/pt/nl/ru) froze 8/8 under /usr/bin/python3. The guard was NOT bypassed and the edition was NOT rebuilt under the venv (both would hide the conflict / break family consistency). The guard's own rationale cites the pt-ko 0/8, which was freeze(venv) vs build(sys) — the same mismatch. Coordinator decision needed: revert the guard, or move the family build stack to the venv. Log `ja/freeze-ja.log` (ABORT rc=2) and `ja/freeze-ja-venv.log` (0/8).", 'Freeze diff added CJK 2901 (p1 122, p2 257, p3 204, p4 154, p5 211, p6 121, p7 345, p8 1487) — expected: Japanese explanations are CJK vs core. Adjudicated by machine check (verify-freeze-diff4.py): all 307 added strings and all 303 removed strings traced to ja map values / instr / structural strings (footer, page-line f-string, gloss prefix 解説 —, H writing-note f-string, answer-line composites `N. KEY — NOTE`, notes + (N면) citations, E-stem blanks rendered as nbsp). 0 unexplained on either side. The last removed string needed the core H f-string (`范文见本版 H 区（{NCHARS}字）`, a JoinedStr, not a plain literal).', 'text.md 450 items vs core 452: two accounted drops, no content gap — (1) `lcn2` removed by design; (2) `lko` removed by design. The Japanese P1 contents 8면 level `すべて` IS in text.md (line 119) — CJK passes is_prose, so ja drops one fewer item than the Latin editions (449). Run-2 text.md is byte-identical to run-1 text.md (SHA 635ec8af…) because the #81 note string is not in the text.md export set (P8 answer notes are not collected by textmd.py — same for en).', '#43/#123/#124 notes "内蔵山：山林庁の予想では紅葉のピークは11月4日" / "内蔵山：ウェザーアイの予想では11月11日" / "内蔵山：山林庁の予想ではピークは11月11日": core\'s own renderings of the Weatheri (private weather company) and Forestry Service (산림청) forecasts — not typos.', 'P8 #150 key renders as `✓` in both core and edition', 'Repeated page citations (1면/2면/4면/6면) appear once in text.md: textmd.py dedupes repeated citation strings — the rendered P7 phrases carry the full per-phrase citations (check_core phrases 8/8 verbatim).']

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (Japanese) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | 穴埋め | 1 | 11月18日はD-1 | OK |
| 2 | 1 | 穴埋め | 김장 | キムチの季節も真っ盛り | OK |
| 3 | 1 | 穴埋め | 19 | 修学能力試験は11月19日（木）です | OK |
| 4 | 1 | 穴埋め | 3 | 11月16日はD-3 | OK |
| 5 | 1 | 穴埋め | 4승 1패 | サムスンがKTウィズに4-1で勝利 | OK |
| 6 | 1 | 穴埋め | 11 | 欠員募集の申込みは11月11日から | OK |
| 7 | 1 | 選択問題 | A | 11月18日はD-1 | OK |
| 8 | 1 | 選択問題 | A | キムジャンの費用は去年より9.0%下がった | OK |
| 9 | 1 | 選択問題 | A | キムチの日は11月22日（日）です | OK |
| 10 | 1 | 選択問題 | A | サムスンが韓国シリーズで優勝 | OK |
| 11 | 2 | 選択問題 | A | 白菜20玉：54,980ウォン | OK |
| 12 | 2 | 選択問題 | A | キムジャンの費用が9.0%下がった | OK |
| 13 | 2 | 選択問題 | A | キムチの日は11月22日（日）です | OK |
| 14 | 2 | 選択問題 | A | 韓国史検定は11月28日（土）です | OK |
| 15 | 2 | 選択問題 | A | ウィキム・フェスティバルは11月20日（金）です | OK |
| 16 | 2 | 穴埋め | 한창 | キムチの季節も真っ盛り | OK |
| 17 | 2 | 穴埋め | 22 | キムチの日は11月22日です | OK |
| 18 | 2 | 穴埋め | 54,980 | 白菜20玉：54,980ウォン | OK |
| 19 | 2 | 穴埋め | 토 | 韓国史検定は土曜日です | OK |
| 20 | 2 | 穴埋め | 배추 | 白菜が安くなったから費用が下がった | OK |
| 21 | 2 | 穴埋め | 199,456 | 4人家族のキムジャン：199,456ウォン | OK |
| 22 | 2 | 穴埋め | 54,980 | 白菜20玉：54,980ウォン | OK |
| 23 | 2 | 穴埋め | 26.5 | 白菜20玉、去年より26.5%安い | OK |
| 24 | 2 | 穴埋め | 13 | 欠員募集の申込み：11月11日〜13日 | OK |
| 25 | 2 | 組み合わせ | d | 김장비용 = 4人家族のキムジャン、199,456ウォン d | OK |
| 26 | 2 | 組み合わせ | a | 김치의 날 = 11月22日 a | OK |
| 27 | 2 | 組み合わせ | c | 위킴 페스티벌 = 11月20日、ソウル c | OK |
| 28 | 2 | 組み合わせ | b | 한능검 = 韓国史検定の略 b | OK |
| 29 | 3 | 選択問題 | A | キムチの日は11月22日です | OK |
| 30 | 3 | 選択問題 | B | 22はキムチの22の効能を表す | OK |
| 31 | 3 | 選択問題 | A | ウィキム・フェスティバルは11月20日（金）です | OK |
| 32 | 3 | 選択問題 | B | 内蔵山：山林庁の予想では紅葉のピークは11月4日 | OK |
| 33 | 3 | 選択問題 | A | 山林庁の基準は葉の50% | OK |
| 34 | 3 | 穴埋め | 절정 | いちばん美しい紅葉を절정という | OK |
| 35 | 3 | 穴埋め | 예보 | 予想の日付と実際の観測日はちがう | OK |
| 36 | 3 | 穴埋め | 관측 | 実際に観測されたのは10月16日 | OK |
| 37 | 3 | 穴埋め | 김치의 날 | 11月22日はキムチの日です | OK |
| 38 | 3 | 穴埋め | 발효 | キムチは発酵食品です | OK |
| 39 | 3 | 穴埋め | 22 | キムチには22の効能がある | OK |
| 40 | 3 | 穴埋め | 11 | 内蔵山：ウェザーアイの予想では11月11日 | OK |
| 41 | 3 | 穴埋め | 4 | 内蔵山：山林庁の予想では11月4日 | OK |
| 42 | 3 | 穴埋め | 20 | ウィキム・フェスティバルは11月20日です | OK |
| 43 | 3 | 組み合わせ | b | 내장산 = ウェザーアイの予想11月11日 b | OK |
| 44 | 3 | 組み合わせ | a | 월출산 = 山林庁の予想11月9日 a | OK |
| 45 | 3 | 組み合わせ | d | 두륜산 = 山林庁の予想11月11日 d | OK |
| 46 | 3 | 組み合わせ | c | 설악산 = 実際の観測10月16日 c | OK |
| 47 | 4 | 選択問題 | A | サムスンが韓国シリーズで優勝 | OK |
| 48 | 4 | 選択問題 | C | シリーズは4-1で終了 | OK |
| 49 | 4 | 選択問題 | B | 第5戦、11月8日大邱：サムスン12-1 | OK |
| 50 | 4 | 選択問題 | A | 第1戦：KTウィズが8-7で勝利 | OK |
| 51 | 4 | 選択問題 | B | サムスン12年ぶりの優勝 | OK |
| 52 | 4 | 穴埋め | 4승 1패 | サムスンがKTウィズに4-1で勝利 | OK |
| 53 | 4 | 穴埋め | 수원 | 第1・2戦は水原で行われた | OK |
| 54 | 4 | 穴埋め | 12대 1 | 第5戦：サムスンが12-1で勝利 | OK |
| 55 | 4 | 穴埋め | 12 | サムスンが12年ぶりに再び優勝 | OK |
| 56 | 4 | 穴埋め | 4연승 | サムスンは1敗のあと4連勝 | OK |
| 57 | 4 | 書き換え | 삼성이 kt wiz를 이겼어요. | 이기다：過去形이겼어요 | OK |
| 58 | 4 | 書き換え | 1차전이 수원에서 열렸어요. | 열리다：過去形열렸어요 | OK |
| 59 | 4 | 書き換え | 한국시리즈가 끝났어요. | 끝나다：過去形끝났어요 | OK |
| 60 | 4 | 書き換え | 삼성이 5차전에서 이겼어요. | 이기다：過去形이겼어요 | OK |
| 61 | 4 | 組み合わせ | c | 준플레이오프 = KIAが3連勝 c | OK |
| 62 | 4 | 組み合わせ | d | 플레이오프 = サムスンが3-2で勝利 d | OK |
| 63 | 4 | 組み合わせ | a | 한국시리즈 = サムスンが4-1で勝利 a | OK |
| 64 | 4 | 組み合わせ | b | K리그1 = ソウルが早期優勝 b | OK |
| 65 | 5 | 選択問題 | A | 予備招集は11月18日（水）です | OK |
| 66 | 5 | 選択問題 | B | 試験は8時40分に始まります | OK |
| 67 | 5 | 選択問題 | A | 今年の受験者は551,864人です | OK |
| 68 | 5 | 選択問題 | B | 成績は12月11日（金）に発表されます | OK |
| 69 | 5 | 選択問題 | A | 試験当日は8時10分までに教室に入る | OK |
| 70 | 5 | 穴埋め | 예비소집 | 予備招集で受験票を受け取る | OK |
| 71 | 5 | 穴埋め | 수험표 | 受験票を受け取り、試験場を確認する | OK |
| 72 | 5 | 穴埋め | 2,310 | 受験者は去年より2,310人少ない | OK |
| 73 | 5 | 穴埋め | 성적 | 成績は12月11日に発表される | OK |
| 74 | 5 | 穴埋め | 김치의 날 | 11月22日はキムチの日です | OK |
| 75 | 5 | 穴埋め | 551,864 | 今年の受験者は551,864人です | OK |
| 76 | 5 | 穴埋め | 1,312 | 試験場は全国に1,312か所 | OK |
| 77 | 5 | 穴埋め | 85 | 全国に85の試験地区がある | OK |
| 78 | 5 | 穴埋め | 10 | 試験当日は役所が10時に始まる | OK |
| 79 | 5 | 文を作る | 수험생은 열심히 공부해요. | 語順：主語＋副詞＋動詞 | OK |
| 80 | 5 | 文を作る | 우리는 수험생을 응원해요. | 主語＋目的語＋動詞 | OK |
| 81 | 5 | 文を作る | 비행기는 듣기 시간에 뜨지 않아요. | 聴解中は飛行機が飛ばない | OK |
| 82 | 5 | 文を作る | 친구는 김치를 나눠 줘요. | 友だちがキムチを分け合う | OK |
| 83 | 6 | 選択問題 | B | 今週は韓国シリーズの結果が出ている | OK |
| 84 | 6 | 選択問題 | A | 11月9日の調査：キムジャンの費用は199,456ウォン | OK |
| 85 | 6 | 選択問題 | B | 紅葉の予想日は過ぎた | OK |
| 86 | 6 | 選択問題 | C | 試験の成績は12月11日に発表される | OK |
| 87 | 6 | 選択問題 | A | 先週のシリーズは日程だけだった | OK |
| 88 | 6 | 選択問題 | A | 第1戦：KTウィズが8-7で勝利 | OK |
| 89 | 6 | 選択問題 | B | 気象庁は約80%で観測する | OK |
| 90 | 6 | 選択問題 | A | 白菜1玉、10月16日：5,557ウォン | OK |
| 91 | 6 | 選択問題 | A | キムジャン調査の基準日は11月9日 | OK |
| 92 | 6 | 選択問題 | A | 今年の受験者は551,864人です | OK |
| 93 | 6 | 穴埋め | 발표 | 発表された日程は変わることがある | OK |
| 94 | 6 | 穴埋め | 결과 | 結果は試合が終わってから | OK |
| 95 | 6 | 穴埋め | 기준 | 基準がちがうから日付もちがう | OK |
| 96 | 6 | 穴埋め | 날짜 | ニュースを読むときはまず日付を確認する | OK |
| 97 | 6 | 正誤 | 틀리다 | 特別な措置は11月19日だけ | OK |
| 98 | 6 | 正誤 | 맞다 | サムスンが4-1で優勝 | OK |
| 99 | 6 | 正誤 | 틀리다 | 予想日は観測日とちがう | OK |
| 100 | 6 | 正誤 | 맞다 | 成績は12月11日に発表される | OK |
| 101 | 7 | 穴埋め | 김장 | 冬のキムチ作り = 김장 | OK |
| 102 | 7 | 選択問題 | A | キムチの日は11月22日です | OK |
| 103 | 7 | 穴埋め | 절임배추 | あらかじめ塩漬けした白菜 | OK |
| 104 | 7 | 選択問題 | A | 味つけにアミの塩辛が入っている | OK |
| 105 | 7 | 穴埋め | D-1 | 11月18日はD-1 | OK |
| 106 | 7 | 選択問題 | B | D-3 = 11月16日 | OK |
| 107 | 7 | 穴埋め | 데이 | 11月19日はDデー | OK |
| 108 | 7 | 選択問題 | A | D-1は試験が明日ということ | OK |
| 109 | 7 | 穴埋め | 기준 | 基準がちがうから日付もちがう（3ページ） | OK |
| 110 | 7 | 選択問題 | A | 気象庁は約80%で観測する | OK |
| 111 | 7 | 穴埋め | 결과 | 結果は試合が終わってから | OK |
| 112 | 7 | 選択問題 | B | 発表と結果を区別する | OK |
| 113 | 8 | 空所補充 | A | キムチの日は11月22日（日）です | OK |
| 114 | 8 | 空所補充 | A | 修学能力試験は11月19日（木）です | OK |
| 115 | 8 | 空所補充 | A | 韓国史検定は11月28日（土）です | OK |
| 116 | 8 | 空所補充 | A | ウィキム・フェスティバルは11月20日（金）です | OK |
| 117 | 8 | 空所補充 | A | サムスンが4-1で優勝 | OK |
| 118 | 8 | 空所補充 | A | 4人家族のキムジャン：199,456ウォン | OK |
| 119 | 8 | 空所補充 | A | 白菜20玉：54,980ウォン | OK |
| 120 | 8 | 空所補充 | A | 今年の受験者は551,864人です | OK |
| 121 | 8 | 選択問題 | A | 今年の受験者は551,864人です | OK |
| 122 | 8 | 選択問題 | B | 試験場は全国に1,312か所 | OK |
| 123 | 8 | 選択問題 | A | 内蔵山：山林庁の予想では紅葉のピークは11月4日 | OK |
| 124 | 8 | 選択問題 | B | 内蔵山：ウェザーアイの予想ではピークは11月11日 | OK |
| 125 | 8 | 選択問題 | B | 頭輪山：山林庁の予想ではピークは11月11日 | OK |
| 126 | 8 | 選択問題 | A | 第1戦：KTウィズが8-7で勝利 | OK |
| 127 | 8 | 選択問題 | A | 欠員募集の申込み：11月11日〜13日 | OK |
| 128 | 8 | 選択問題 | B | 山火事注意期間は12月15日まで | OK |
| 129 | 8 | 選択問題 | B | ミンジュンは水曜日に予備招集に行きます | OK |
| 130 | 8 | 選択問題 | A | 木曜日に試験を受けます | OK |
| 131 | 8 | 選択問題 | B | 日曜日は家族とキムチを分け合います | OK |
| 132 | 8 | 選択問題 | C | 来週は韓国史検定の準備をします | OK |
| 133 | 8 | 文を作る | 저는 수요일에 예비소집에 가요. | 語順：主語＋時間＋場所＋動詞 | OK |
| 134 | 8 | 文を作る | 우리는 김치를 나눠 먹어요. | 主語＋目的語＋動詞 | OK |
| 135 | 8 | 文を作る | 민준이는 한국사를 좋아해요. | 좋아하다 = 好き | OK |
| 136 | 8 | 文を作る | 수험생은 도서관에서 공부해요. | 動作の場所には「에서」を使う | OK |
| 137 | 8 | 翻訳 | 11月22日はキムチの日。 | 2ページ参照 | OK |
| 138 | 8 | 翻訳 | サムスン12年ぶりの優勝。 | 4ページ参照 | OK |
| 139 | 8 | 翻訳 | 11월 18일은 예비소집이에요. | 5ページ参照 | OK |
| 140 | 8 | 翻訳 | 일요일에는 가족과 김치를 나눠 먹어요. | 8ページCセクション参照 | OK |
| 141 | 8 | 組み合わせ | b | 예비소집 = 予備招集 b | OK |
| 142 | 8 | 組み合わせ | c | 김치의 날 = 11月22日 c | OK |
| 143 | 8 | 組み合わせ | a | 발효 = 発酵の過程 a | OK |
| 144 | 8 | 組み合わせ | d | 우승 = 優勝 d | OK |
| 145 | 8 | 空所補充 | A | 水曜日に予備招集に行きます | OK |
| 146 | 8 | 空所補充 | A | キムチの日は11月22日です | OK |
| 147 | 8 | 空所補充 | A | 韓国史検定は11月28日です | OK |
| 148 | 8 | 空所補充 | A | 4人家族のキムジャン：199,456ウォン | OK |
| 149 | 8 | 空所補充 | A | 成績は12月11日に発表される | OK |
| 150 | 8 | 作文 | （自由課題 — 模範解答は下） | このページのHセクションの模範解答（169字） | OK ✓ |
