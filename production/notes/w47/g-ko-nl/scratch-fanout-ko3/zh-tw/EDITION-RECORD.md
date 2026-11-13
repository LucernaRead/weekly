# EDITION RECORD — 2026-W47 ko-zh-tw (run 1; 2026-11-11)

- Slug: `2026-w47-ko-zh-tw` (target ko, reader Traditional Chinese). Core: `core-ko` run 11 (fix1) + textmd fix2.
- Build interpreter: **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py and webpdf.py on `tools/venv/bin/python` (cairosvg/fontTools, no PIL metrics). svglib.py byte-identical to core (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Map: 216 keys + 8 instr (`map-zh-tw.json`, `gen-map-zh-tw.py` via `mk-lang.py` + `zh-tw-replace.json` / `zh-tw-meta.json`); apply log `apply-zh-tw.log`.

## Files

- Print PDF: `Lucerna-VOL4-KO-ZH-TW.pdf` — **46,280,042 bytes**, SHA-256 `180d3ce0ef35f88aef9842e30835b29c77f0b7d5082e6529f9255f019610a949`
- Web PDF: `Lucerna-VOL4-KO-ZH-TW-web.pdf` — **4,348,626 bytes** (< 7 MB), SHA-256 `cfe20ece5a19f03e9ec7e3593c8fced61eae3f78d7eb19fdd09ba9d0729a78ab`
- Text export: `2026-w47-ko-zh-tw.text.md` — 34,637 bytes, 450 items, SHA-256 `af183ae64f665c405f86a54edf1a76315f80901e9fac615f7ba9b7cd70c453e2`
- `ABSTRACT.txt` — 268 bytes, SHA-256 `88f967a1267da0e6b6b352582fea454de11a31ce171b5a46c0d67311b34d7767`
- 8 SVGs in `svg/` (hashes in `zh-tw/sha-zh-tw-run1.txt`).

## Gates (freeze baseline blocked — see Adjudicated; all other gates pass)

| Gate | Result | Log |
|---|---|---|
| run.py (run 1) | exit 0, 0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150; A2 51 / B1 72 / B2 27; per page 10/18/18/18/18/18/12/38; P2-feature ends 1531, P8-keys ends 2351, P7 teaser 2425.7 | `zh-tw/build-zh-tw-run1.log` |
| boxtitle width | 8/8 within 386.5px | `zh-tw/boxtitle-zh-tw.log` |
| U+2019 scan (8 SVGs) | 0 | measured inline |
| occlusion audit | **0 flags** (0 flags) | `zh-tw/occlusion-zh-tw.json` / `zh-tw/occlusion-zh-tw.log` |
| p8.py extract | 150/150 noted | `zh-tw/p8-extract-zh-tw.log`, `zh-tw/p8-zh-tw.json` |
| p8.py compare vs core | [138] | `zh-tw/p8-compare-zh-tw.log` |
| freeze diff vs core | added CJK 822 (adjudicated — all 267 added / 268 removed strings traced) | `zh-tw/freeze-diff-zh-tw.log` |
| freeze baseline (/usr/bin/python3) | BLOCKED — runtime guard (see Adjudicated); venv run 0/8 | `zh-tw/freeze-zh-tw.log` |
| check_core (scratch copy) | gloss fails 0, orphan issues 0 | `zh-tw/check-zh-tw.log` |
| check_gloss (scratch copy) | gloss fails 0 | `zh-tw/check-zh-tw.log` |
| print/web text layers | byte-identical, 49,645 bytes each | `zh-tw/textlayer-diff-zh-tw.txt` (diff rc 0) |
| P8 min font (PyMuPDF, print PDF) | **9.975pt (region spans 163, at-min 158)** ≥ 9.75pt (P8 stem 10.35pt is the recorded core adjudication) | measured inline |
| keycheck (150 keys vs P8 SVG) | 149 exact + #150 `✓` (expected, core identical) = **150/150** | `zh-tw/keycheck-zh-tw.log` |
| §1.1 grep audit | paper/VOL.4/VOL.5/`·` counts identical to core page-by-page; `·` only in gloss/option/credit contexts; P7 VOL.5 3→2 by design (removed `lko`/`lcn2` lines) | `zh-tw/style11-zh-tw.log` |
| visual read | 8/8 print pages at 100dpi, zero issues | `zh-tw/pages/p-1.png` … `p-8.png` |
| text.md self-read | full read, zero issues (see notes) | — |
| hanzi residual scan | 1162 | measured inline |

## Fixes in this edition

['No post-apply fixes needed. Frame clean at map level: content7.py:81 `句式拆解：「在〜之後」。提問：「〜 후에 뭐 해요?」` (renders across two text elements in the P7 Pattern box, complete). boxtitle 8/8 on the first run; run.py run 1 clean (0 FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150). The nl P2-feature overflow defect class and the ja P8 #81 wrapped-note defect class were both checked and did not occur (P2-feature ends 1531; p8.py compare CLEAN on the first run).']

## Adjudicated (not defects — inherited from core or by design)

["FREEZE BASELINE BLOCKED (not an edition defect — a tooling conflict for the coordinator): tools/freeze.py gained a runtime guard at 2026-11-11 12:00 (uncommitted working-tree change) that aborts unless Pillow major == 13 (tools/venv). It contradicts the family's interpreter lock (core KIT fix #15 + task brief: build + freeze under /usr/bin/python3, PIL 10.2.0). Evidence: freeze.py baseline under the venv on this sys-built edition gives 0/8 (all 8 SVGs differ — dual-stack drift, PIL 13 re-measures Korean spacing ~1.11px wider per space boundary); the 8 editions built before 12:00 (en/de/es/fr/it/pt/nl/ru) froze 8/8 under /usr/bin/python3. The guard was NOT bypassed and the edition was NOT rebuilt under the venv (both would hide the conflict / break family consistency). The guard's own rationale cites the pt-ko 0/8, which was freeze(venv) vs build(sys) — the same mismatch. Coordinator decision needed: revert the guard, or move the family build stack to the venv. Log `zh-tw/freeze-zh-tw.log` (ABORT rc=2) and `zh-tw/freeze-zh-tw-venv.log` (0/8, rc=1).", "Freeze diff added CJK 822 (p1 47, p2 66, p3 49, p4 60, p5 56, p6 42, p7 97, p8 405) — lower than ja's 2901 because core is already Simplified Chinese: most CJK is shared, and the diff is the Simplified→Traditional script change plus the new Traditional-only strings. Adjudicated by machine check (zh-tw/verify-freeze-diff-zh-tw.py): all 267 added strings and all 268 removed strings traced to zh-tw map values / instr / structural strings (footer, page-line f-string, gloss prefix 譯注｜, H writing-note f-string, answer-line composites `N. KEY — NOTE`, notes + (N면) citations, E-stem blanks rendered as nbsp) or, for removed strings, to core map keys / core source literals. 0 unexplained on either side. The H notes on both sides are f-strings (JoinedStr in the AST, never plain literals), so both rendered forms were hardcoded in the verifier: zh-tw `本版H區範文（169字）`, core `范文见本版 H 区（169字）`.", 'p8.py compare keydiff [138] (not [137, 138] like the other fan-outs) — correct by construction: the E-group re-aiming translates keys 137/138 to Traditional Chinese, but the #137 key `11月22日是泡菜日。` is script-identical between Simplified and Traditional Chinese, so the extracted keys match; only the NOTE differs (對照第2版 vs 对照第2版) and notes are not keys. The #138 key differs (時隔12年奪冠 vs 时隔12年夺冠). Verified in the P8 SVG: `137. 11月22日是泡菜日。 — 對照第2版` / `138. 三星時隔12年奪冠。 — 對照第4版`.', 'text.md 450 items vs core 452: two accounted drops, no content gap — (1) `lcn2` removed by design; (2) `lko` removed by design. The Traditional Chinese P1 contents 8版 level `全部` IS in text.md — CJK passes is_prose, so zh-tw drops one fewer item than the Latin editions (449).', '#43/#123/#124 notes "內藏山：山林廳預測紅葉高峰在11月4日" / "內藏山：Weatheri預測高峰在11月11日" / "內藏山：山林廳預測高峰在11月11日": core\'s own renderings of the Weatheri (private weather company) and Forestry Service (山林廳) forecasts — not typos.', 'P8 #150 key renders as `✓` in both core and edition', 'Repeated page citations (1面/2面/4面/6面) appear once in text.md: textmd.py dedupes repeated citation strings — the rendered P7 phrases carry the full per-phrase citations (check_core phrases 8/8 verbatim).']

## 150-key table (REG from edition sources vs keys extracted from P8 SVG)

| # | Page | Type | Key | Note (Traditional Chinese) | SVG |
|---|---|---|---|---|---|
| 1 | 1 | 填空 | 1 | 11月18日是D-1 | OK |
| 2 | 1 | 填空 | 김장 | 泡菜季正忙 | OK |
| 3 | 1 | 填空 | 19 | 韓國高考在11月19日星期四 | OK |
| 4 | 1 | 填空 | 3 | 11月16日是D-3 | OK |
| 5 | 1 | 填空 | 4승 1패 | 三星4勝1負勝kt | OK |
| 6 | 1 | 填空 | 11 | 取消名額報名11月11日起 | OK |
| 7 | 1 | 單選 | A | 11月18日是D-1 | OK |
| 8 | 1 | 單選 | A | 泡菜成本比去年降9.0% | OK |
| 9 | 1 | 單選 | A | 泡菜日是11月22日星期日 | OK |
| 10 | 1 | 單選 | A | 韓國大賽三星奪冠 | OK |
| 11 | 2 | 單選 | A | 白菜20棵54,980韓元 | OK |
| 12 | 2 | 單選 | A | 泡菜成本降了9.0% | OK |
| 13 | 2 | 單選 | A | 泡菜日是11月22日星期日 | OK |
| 14 | 2 | 單選 | A | 韓史檢定在11月28日星期六 | OK |
| 15 | 2 | 單選 | A | 泡菜節在11月20日星期五 | OK |
| 16 | 2 | 填空 | 한창 | 泡菜季正忙 | OK |
| 17 | 2 | 填空 | 22 | 泡菜日是11月22日 | OK |
| 18 | 2 | 填空 | 54,980 | 白菜20棵54,980韓元 | OK |
| 19 | 2 | 填空 | 토 | 韓史檢定在星期六 | OK |
| 20 | 2 | 填空 | 배추 | 泡菜成本下降因白菜降價 | OK |
| 21 | 2 | 填空 | 199,456 | 四口之家泡菜成本199,456韓元 | OK |
| 22 | 2 | 填空 | 54,980 | 白菜20棵54,980韓元 | OK |
| 23 | 2 | 填空 | 26.5 | 白菜20棵比去年降26.5% | OK |
| 24 | 2 | 填空 | 13 | 取消名額報名11月11日至13日 | OK |
| 25 | 2 | 配對 | d | 김장비용 = 四口之家199,456韓元 d | OK |
| 26 | 2 | 配對 | a | 김치의 날 = 11月22日 a | OK |
| 27 | 2 | 配對 | c | 위킴 페스티벌 = 11月20日首爾 c | OK |
| 28 | 2 | 配對 | b | 한능검 = 韓國史考試簡稱 b | OK |
| 29 | 3 | 單選 | A | 泡菜日是11月22日 | OK |
| 30 | 3 | 單選 | B | 22代表泡菜的22種功效 | OK |
| 31 | 3 | 單選 | A | 泡菜節在11月20日星期五 | OK |
| 32 | 3 | 單選 | B | 內藏山林業廳預報峰值11月4日 | OK |
| 33 | 3 | 單選 | A | 林業廳標準是葉子50% | OK |
| 34 | 3 | 填空 | 절정 | 紅葉最美的時候叫절정 | OK |
| 35 | 3 | 填空 | 예보 | 預報日期和實際觀測日期不同 | OK |
| 36 | 3 | 填空 | 관측 | 實際觀測10月16日 | OK |
| 37 | 3 | 填空 | 김치의 날 | 11月22日是泡菜日 | OK |
| 38 | 3 | 填空 | 발효 | 泡菜是發酵食品 | OK |
| 39 | 3 | 填空 | 22 | 泡菜有22種功效 | OK |
| 40 | 3 | 填空 | 11 | 內藏山Weatheri預報11日 | OK |
| 41 | 3 | 填空 | 4 | 內藏山林業廳預報4日 | OK |
| 42 | 3 | 填空 | 20 | 泡菜節11月20日 | OK |
| 43 | 3 | 配對 | b | 내장산 = Weatheri預報11日 b | OK |
| 44 | 3 | 配對 | a | 월출산 = 林業廳預報9日 a | OK |
| 45 | 3 | 配對 | d | 두륜산 = 林業廳預報11日 d | OK |
| 46 | 3 | 配對 | c | 설악산 = 實際觀測10月16日 c | OK |
| 47 | 4 | 單選 | A | 韓國大賽三星奪冠 | OK |
| 48 | 4 | 單選 | C | 系列賽比分4勝1負 | OK |
| 49 | 4 | 單選 | B | 第5場11月8日大邱三星12比1 | OK |
| 50 | 4 | 單選 | A | 第1場kt以8比7獲勝 | OK |
| 51 | 4 | 單選 | B | 三星時隔12年奪冠 | OK |
| 52 | 4 | 填空 | 4승 1패 | 三星4勝1負勝kt | OK |
| 53 | 4 | 填空 | 수원 | 韓國大賽1、2場在水原 | OK |
| 54 | 4 | 填空 | 12대 1 | 第5場三星12比1獲勝 | OK |
| 55 | 4 | 填空 | 12 | 三星12年後再次奪冠 | OK |
| 56 | 4 | 填空 | 4연승 | 三星1負後4連勝 | OK |
| 57 | 4 | 句型轉換 | 삼성이 kt wiz를 이겼어요. | 이기다的過去式이겼어요 | OK |
| 58 | 4 | 句型轉換 | 1차전이 수원에서 열렸어요. | 열리다的過去式열렸어요 | OK |
| 59 | 4 | 句型轉換 | 한국시리즈가 끝났어요. | 끝나다的過去式끝났어요 | OK |
| 60 | 4 | 句型轉換 | 삼성이 5차전에서 이겼어요. | 이기다的過去式이겼어요 | OK |
| 61 | 4 | 配對 | c | 준플레이오프 = KIA三連勝 c | OK |
| 62 | 4 | 配對 | d | 플레이오프 = 三星3勝2負 d | OK |
| 63 | 4 | 配對 | a | 한국시리즈 = 三星4勝1負 a | OK |
| 64 | 4 | 配對 | b | K리그1 = 首爾提前奪冠 b | OK |
| 65 | 5 | 單選 | A | 預備召集在11月18日星期三 | OK |
| 66 | 5 | 單選 | B | 韓國高考8點40分開始 | OK |
| 67 | 5 | 單選 | A | 今年考生551,864人 | OK |
| 68 | 5 | 單選 | B | 成績12月11日星期五公布 | OK |
| 69 | 5 | 單選 | A | 考試日8點10分前入場完畢 | OK |
| 70 | 5 | 填空 | 예비소집 | 預備召集領取准考證 | OK |
| 71 | 5 | 填空 | 수험표 | 領取准考證、確認考場 | OK |
| 72 | 5 | 填空 | 2,310 | 考生比去年少2,310人 | OK |
| 73 | 5 | 填空 | 성적 | 成績12月11日公布 | OK |
| 74 | 5 | 填空 | 김치의 날 | 11月22日是泡菜日 | OK |
| 75 | 5 | 填空 | 551,864 | 今年考生551,864人 | OK |
| 76 | 5 | 填空 | 1,312 | 考場全國1,312處 | OK |
| 77 | 5 | 填空 | 85 | 全國有85個考區 | OK |
| 78 | 5 | 填空 | 10 | 考試日機關10點上班 | OK |
| 79 | 5 | 造句 | 수험생은 열심히 공부해요. | 語序：主語+副詞+動詞 | OK |
| 80 | 5 | 造句 | 우리는 수험생을 응원해요. | 主語+受詞+動詞的語序 | OK |
| 81 | 5 | 造句 | 비행기는 듣기 시간에 뜨지 않아요. | 聽力時段飛機不起降 | OK |
| 82 | 5 | 造句 | 친구는 김치를 나눠 줘요. | 朋友分享泡菜 | OK |
| 83 | 6 | 單選 | B | 本週韓國大賽已有結果 | OK |
| 84 | 6 | 單選 | A | 11月9日調查泡菜成本199,456韓元 | OK |
| 85 | 6 | 單選 | B | 紅葉預報日期已過 | OK |
| 86 | 6 | 單選 | C | 韓國高考成績12月11日公布 | OK |
| 87 | 6 | 單選 | A | 上週韓國大賽只是公布的日程 | OK |
| 88 | 6 | 單選 | A | 第1場kt以8比7獲勝 | OK |
| 89 | 6 | 單選 | B | 氣象廳觀測標準約80% | OK |
| 90 | 6 | 單選 | A | 10月16日白菜一棵5,557韓元 | OK |
| 91 | 6 | 單選 | A | 泡菜成本調查基準日11月9日 | OK |
| 92 | 6 | 單選 | A | 今年考生551,864人 | OK |
| 93 | 6 | 填空 | 발표 | 公布的日程可能改變 | OK |
| 94 | 6 | 填空 | 결과 | 結果要等比賽結束 | OK |
| 95 | 6 | 填空 | 기준 | 日期不同因標準不同 | OK |
| 96 | 6 | 填空 | 날짜 | 讀新聞先看日期 | OK |
| 97 | 6 | 是非 | 틀리다 | 特別措施只適用於11月19日 | OK |
| 98 | 6 | 是非 | 맞다 | 三星4勝1負奪冠 | OK |
| 99 | 6 | 是非 | 틀리다 | 預報日期不等於觀測日期 | OK |
| 100 | 6 | 是非 | 맞다 | 成績12月11日公布 | OK |
| 101 | 7 | 填空 | 김장 | 醃泡菜＝김장 | OK |
| 102 | 7 | 單選 | A | 泡菜日是11月22日 | OK |
| 103 | 7 | 填空 | 절임배추 | 提前鹽醃好的白菜 | OK |
| 104 | 7 | 單選 | A | 調料裡有蝦醬 | OK |
| 105 | 7 | 填空 | D-1 | 11月18日是D-1 | OK |
| 106 | 7 | 單選 | B | D-3＝11月16日 | OK |
| 107 | 7 | 填空 | 데이 | 11月19日是D-day | OK |
| 108 | 7 | 單選 | A | D-1就是明天考試 | OK |
| 109 | 7 | 填空 | 기준 | 日期不同因標準不同（3版） | OK |
| 110 | 7 | 單選 | A | 氣象廳觀測標準約80% | OK |
| 111 | 7 | 填空 | 결과 | 結果要等比賽結束 | OK |
| 112 | 7 | 單選 | B | 發布和結果要區分 | OK |
| 113 | 8 | 克漏字 | A | 泡菜日是11月22日星期日 | OK |
| 114 | 8 | 克漏字 | A | 韓國高考在11月19日星期四 | OK |
| 115 | 8 | 克漏字 | A | 韓史檢定在11月28日星期六 | OK |
| 116 | 8 | 克漏字 | A | 泡菜節在11月20日星期五 | OK |
| 117 | 8 | 克漏字 | A | 三星4勝1負奪冠 | OK |
| 118 | 8 | 克漏字 | A | 四口之家泡菜成本199,456韓元 | OK |
| 119 | 8 | 克漏字 | A | 白菜20棵54,980韓元 | OK |
| 120 | 8 | 克漏字 | A | 今年考生551,864人 | OK |
| 121 | 8 | 單選 | A | 今年考生551,864人 | OK |
| 122 | 8 | 單選 | B | 考場全國1,312處 | OK |
| 123 | 8 | 單選 | A | 內藏山林業廳預報峰值11月4日 | OK |
| 124 | 8 | 單選 | B | 內藏山Weatheri預報峰值11月11日 | OK |
| 125 | 8 | 單選 | B | 頭輪山林業廳預報峰值11月11日 | OK |
| 126 | 8 | 單選 | A | 第1場kt以8比7獲勝 | OK |
| 127 | 8 | 單選 | A | 取消名額報名11月11日至13日 | OK |
| 128 | 8 | 單選 | B | 山火注意期到12月15日 | OK |
| 129 | 8 | 單選 | B | 民俊星期三去預備召集 | OK |
| 130 | 8 | 單選 | A | 星期四參加韓國高考 | OK |
| 131 | 8 | 單選 | B | 星期日和家人分享泡菜 | OK |
| 132 | 8 | 單選 | C | 下週準備韓史檢定 | OK |
| 133 | 8 | 造句 | 저는 수요일에 예비소집에 가요. | 語序：主語+時間+地點+動詞 | OK |
| 134 | 8 | 造句 | 우리는 김치를 나눠 먹어요. | 主語+受詞+動詞的語序 | OK |
| 135 | 8 | 造句 | 민준이는 한국사를 좋아해요. | 좋아하다 = 喜歡 | OK |
| 136 | 8 | 造句 | 수험생은 도서관에서 공부해요. | 動作場所用「에서」 | OK |
| 137 | 8 | 翻譯 | 11月22日是泡菜日。 | 對照第2版 | OK |
| 138 | 8 | 翻譯 | 三星時隔12年奪冠。 | 對照第4版 | OK |
| 139 | 8 | 翻譯 | 11월 18일은 예비소집이에요. | 對照第5版 | OK |
| 140 | 8 | 翻譯 | 일요일에는 가족과 김치를 나눠 먹어요. | 對照第8版C區 | OK |
| 141 | 8 | 配對 | b | 예비소집 = 預備召集 b | OK |
| 142 | 8 | 配對 | c | 김치의 날 = 11月22日 c | OK |
| 143 | 8 | 配對 | a | 발효 = 發酵過程 a | OK |
| 144 | 8 | 配對 | d | 우승 = 奪冠 d | OK |
| 145 | 8 | 克漏字 | A | 星期三去預備召集 | OK |
| 146 | 8 | 克漏字 | A | 泡菜日是11月22日 | OK |
| 147 | 8 | 克漏字 | A | 韓史檢定在11月28日 | OK |
| 148 | 8 | 克漏字 | A | 四口之家泡菜成本199,456韓元 | OK |
| 149 | 8 | 克漏字 | A | 成績12月11日公布 | OK |
| 150 | 8 | 寫作 | （開放題，範文如下） | 本版H區範文（169字） | OK ✓ |
