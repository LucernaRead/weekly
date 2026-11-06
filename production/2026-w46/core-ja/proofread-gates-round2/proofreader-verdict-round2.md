# Round 2 Independent Proofread Verdict — Lucerna Weekly W46, JA family

- **Issue:** VOL.3, dated Mon 2026-11-09 to Sun 2026-11-15.
- **Scope:** All 11 JA-target editions (one per reader-native language):
  `2026-w46-ja-de, -en, -es, -fr, -it, -ko, -nl, -pt, -ru, -zh-cn, -zh-tw`.
  The canonical core dir `files/weekly-report-w46-ja-core/` is the zh-cn edition; it is not a 12th edition.
- **Proofreader:** Independent, Round 2. Did not build or fix these editions. No edition file was edited, re-rendered, pushed, inserted, or posted.
- **Gate dir (fresh, Round 2):** `hidden_files/w46/ja-proofread-gates-round2/` — all gate JSONs/logs referenced below live there.
- **Round 1 verdict:** FAIL all 11 (D-CORE-01, D-CORE-02, D-ZHTW-01/02).
- **Round 2 verdict: ROUND 2 FAIL — blocking defect D-KEY-42 in all 11 editions.** See §5.

## 1. Fix verification

### 1.1 D-CORE-01 (kinsoku LINE-END) — CONFIRMED FIXED, wrap-level fix ACCEPTABLE

| Check | Result |
|---|---|
| Own line-end kinsoku scan (NO_END `（「『〔【《〈([` at line ends), 8 pages × 11 editions | 0 hits |
| Own line-start kinsoku scan (NO_START set), 8 pages × 11 editions | 0 hits |
| Own orphan scan (window 10–45) | 0 hits |
| `svglib.py` md5 (`hidden_files/weekly-report-w46-ja-build/svglib.py`) | `74177544422fe677639d769cd80499fb` (new value; old `d73e23b3…` absent from all scoped guard files) |
| NO_END block present in `wrap()`, after the NO_START loop, before seam-repair | Yes; pure character move, no width measurement |
| `CANON_SVGLIB_MD5` = new value in all 9 fan-out `transform.py` + `gen_ja_zhtw.py` | Yes, 1 occurrence each, plus md5 assert lines |
| `gen_ja_zhtw.py` `edit()` anchors intact (all sit above/below the NO_END block, none spans it) | Yes |
| zh-tw build-copy `svglib.py` contains NO_END block + `_tc_index` TC-face plumbing | Yes |
| Pre/post text-multiset diff (Round 1 `baseline-ja/svg/` pre-fix core SVGs vs current) | 1302 texts both sides; exactly 4 lines changed, P1 + P3 only; all other pages 0 diffs; element order and (x, y) identical |
| Changed files vs `ja-fix/before-sha256.txt` (132 files) | Only P1+P3 SVGs in all 11 editions, P7+P8 SVGs in zh-tw only, all 22 PDFs, all 11 `.text.md`, all 11 `ABSTRACT.txt` — no other SVG changed |

The two re-split stems read correctly, bracket intact across the split:

- P1 item 8 (`p1-hyoushi.svg`, x=527, y=2419.0 → 2449.45): BEFORE `七五三の中心の日はいつですか。 A. 9日（` / `月） · B. 11日（水） · C. 15日（日）` → AFTER `七五三の中心の日はいつですか。 A. 9日` / `（月） · B. 11日（水） · C. 15日（日）`. `A. 9日（月）` intact on line 2.
- P3 item 32 (`p3-bunka.svg`, x=65, y=2163.25 → 2190.8): BEFORE `二の酉はいつですか。 A. 19日（木） · B. 7日（` / `土） · C. 15日（日）` → AFTER `… · B. 7日` / `（土） · C. 15日（日）`. `B. 7日（土）` intact on line 2.

**Ruling (flagged item a): WRAP-LEVEL FIX ACCEPTABLE — CONFIRMED.** No other re-wraps or text moves were introduced. Caveat: a recursive grep for the old md5 over all of `hidden_files/` was killed before completing, so global absence of the old md5 is unverified; all 10 scoped guard files (core `svglib.py`, 9 fan-out `transform.py`, `gen_ja_zhtw.py`) were verified directly and contain only the new value.

### 1.2 D-CORE-02 (abstracts news-framing) — CONFIRMED FIXED, all 11

Own script `r2_abstracts.py` compared each current `ABSTRACT.txt` byte-wise against `ja-fix/abstracts-before-after.txt`. **All 11 PASS:** exactly one line + trailing newline, 0 ASCII double-quotes, contains `150`, `A2`, `B2`, current text equals the recorded AFTER text exactly, no banned news-framing tail, long common prefix with BEFORE (divergence only at the tail clause).

AFTER tails (practice framing), verified verbatim:

| Edition | AFTER tail |
|---|---|
| zh-cn | `共150道以本周话题为素材的练习。` |
| zh-tw | `共150道以本週話題為素材的練習題。` |
| en | `150 exercises built from this week's topics.` |
| de | `150 Übungen zu den Themen dieser Woche.` |
| es | `150 ejercicios construidos a partir de los temas de esta semana.` |
| fr | `150 exercices construits à partir des sujets de cette semaine.` |
| it | `150 esercizi costruiti sui temi di questa settimana.` |
| ko | `A2부터 B2까지 이번 주 주제를 소재로 한 150개의 연습 문제가 수록되어 있습니다.` |
| nl | `150 oefeningen op basis van de thema's van deze week.` |
| pt | `150 exercícios construídos a partir dos temas desta semana.` |
| ru | `150 упражнений, составленных по темам этой недели.` |

(The ru space-before-comma slip noted in the fix report is corrected in the current file.)

**Ruling: CONFIRMED.**

### 1.3 D-ZHTW (Simplified residue) — CONFIRMED FIXED (8 strings); Round 1 "exactly 2" claim REFUTED

All 8 conversions verified present in the zh-tw renderings, residue strings absent:

| # | BEFORE → AFTER | Location |
|---|---|---|
| 1 (D-ZHTW-01) | `得到东西的场所用「で」。` → `得到東西的場所用「で」。` | P7 clinic note, `p7-kotoba.svg`, y=784.0 |
| 2 (D-ZHTW-02) | `在酉の市买熊手` → `在酉の市買熊手` | P8 key 42, `p8-tesuto.svg`, y=1429.0 |
| 3 | `看的场所用「で」。` → `看的場所用「で」。` | P7 clinic note, y=967.6 |
| 4 | `场所用「で」` → `場所用「で」` | P8 key 135 note, y=1912.1 |
| 5 | `2026年没有三の酉` → `2026年沒有三の酉` | P8 key 33 note, y=2368.8 |
| 6 | `新小结是美ノ海` → `新小結是美ノ海` | P8 key 59 note, y=1956.6 |
| 7 | `「千歳飴」受欢迎` → `「千歳飴」受歡迎` | P8 key 148 note, y=2307.5 |
| 8 | `口号是「静かだけど、冒険中。」` → `口號是「静かだけど、冒険中。」` | P8 keys 103 (y=2133.5) and 128 (y=1692.0) |

Own correct-method scan (`r2_sc.py`, OpenCC, enumerate ALL chars whose s2t form differs, then adjudicate each): 21 distinct s2t-differing chars, 126 instances, 0 residue chars (`东买场欢没结` all absent), 0 of 8 residue strings present. MAP `hidden_files/w46/maps/zh-tw.json` has 187 entries; all 8 residue keys present with correct Traditional values.

**Refutation evidence:** `ja-fix/sc-occurrences-BEFORE.txt` (pre-fix enumeration, read in full) lists all 6 extra strings (#3–#8) with file/y/string — e.g. 场: P7 `看的场所用「で」。` (y=967.6) and P8 key 135 `场所用「で」`; 欢: P8 key 148; 没: P8 key 33; 结: P8 key 59; 号 in `口号是…` keys 103/128. The Round 1 verdict's "full scan found exactly these 2" claim is therefore **REFUTED**. `sc-scan-BEFORE.json` was NOT cited (discarded unsound definition, per brief).

**Each of the 21 claimed-legitimate chars adjudicated from its occurrences** — all occur only inside Japanese words/segments: 会 (会社/株式会社), 内 (内容/以内), 写 (写真/写真館), 参 (お参り/七五三参り; glosses correctly use 參拜), 号 (第3号/前号/今号/次号 only — no Chinese-segment occurrence remains), 国 (国際センター), 学 (学ぶ/学校/中学生), 寝 (寝る), 届 (お届け), 峡 (鳴子峡), 当 (本当), 数 (数字/数; paired with Traditional 數字 on the Japanese side of one bilingual header), 来 (来る/来ます/来週), 横 (横浜/横綱), 浅 (浅草), 温 (気温, one wrapped-line continuation), 点 (点差), 画 (版画), 祷 (ご祈祷), 里 (大の里), 静 (静か / quoted slogan; keys 103/128 correctly keep 静 inside the quoted Japanese slogan while the Chinese verb is 口號). Full string: `会内写参号国学寝届峡当数来横浅温点画祷里静`. Post-fix zh-tw state: **CLEAN**.

**Record inaccuracy (NOT an edition defect):** the fix report's "190 occurrences" figure is wrong. `sc-occurrences-BEFORE.txt` contains 27 char sections and 135 occurrence bullet lines; per-section recount gives BEFORE total 136 instances, AFTER total 126, delta exactly −10 = 东−1, 买−1, 场−3, 欢−1, 没−1, 结−1, 号−2. "190" equals the dump file's total line count, not the occurrence count.

**Ruling (flagged item b): REFUTATION CONFIRMED; post-fix state CLEAN.**

### 1.4 Flagged item (c) — zh-tw web PDF standalone re-run — CONFIRMED

Independently verified (own `r2_pdf.py`, §3): zh-tw web PDF = **2,872,565 B**, 44,817 `pdftotext` bytes, 8 pages, web extraction byte-identical to print extraction, ≤ 7 MB. Matches the claimed standalone re-run (exit 0) exactly. **Ruling: CONFIRMED.**

### 1.5 Regression sweep — no new defect introduced

- Badge-less core subtitle = W45 JA precedent, NOT a defect (core subtitle y=330, fill `#28251d`, size 40, weight 700; strapline y=372, fill `#57523f`). Not re-raised.
- Cosmetics O-01–O-05: O-01 spacing variant on key 92 (`34+26=60` in core/zh-tw vs `34 + 26 = 60` elsewhere) confirmed present, cosmetic only, not re-raised. O-02–O-05 checked visually/attribute-wise in §4; no change.
- W45-promise wording unchanged: P7 reader's-letter disclosure + VOL.4 carry-over present in all 11 editions (zh-tw disclosure wraps `VOL.`/`4。` across two lines — verified by reading the lines; the wrapped form is not a missing promise).
- Fix records appended to all 11 `WEEKLY-KIT.md` files (core §11; fan-outs §6 Fix history), with accurate defect/fix quotes (spot-checked core D-CORE-02 quote against `ABSTRACT.txt`).
- No fix introduced a new defect in gates, counts, geometry, or visuals (§3–§4), except D-KEY-42 (§5), which is pre-existing (inherited from the core), not introduced by the fix.

## 2. Full key-letter verification — 149/150 confirmed; 1 blocking defect (D-KEY-42)

Every key 1–150 was verified semantically in the JA core (full `2026-w46-ja-zh-cn.text.md` read) and in all 11 editions' P8 renderings (via `p8.py` extract + direct SVG reads). `p8.py` set-equality alone was NOT relied on. Arithmetic recomputed; weekday/date claims calendar-checked (§3); choice/cloze/fill keys checked against articles and grammar.

### 2.1 Matching blocks (stem + options + key, quoted)

**Items 25–28 (P2).** Stems: 25.ポッキー / 26.プリッツ / 27.千歳飴 / 28.熊手. Options (all four blocks): a. チョコレートの細いビスケット / b. 商売繁盛の縁起物 / c. 塩味の細いビスケット / d. 赤と白の長い飴. Keys: **25→d** (ポッキー = chocolate-coated thin stick), **26→c** (プリッツ = salty thin biscuit), **27→a** (千歳飴 = red-and-white long candy), **28→b** (熊手 = lucky rake). All correct.

**Items 43–46 (P3).** Stems: 43.七五三 / 44.千歳飴 / 45.熊手 / 46.酉の市. Options: a. 11月の酉の日に開くお祭り / b. 3歳・5歳・7歳の子どものお祝い / c. 商売繁盛の縁起物 / d. 赤と白の長い飴. Keys: **43→b**, **44→d**, **45→c**, **46→a**. All correct.

**Items 141–144 (P8).** Stems: 141.七五三 / 142.千歳飴 / 143.落葉 / 144.見頃. Options: a. 木から落ちた葉 / b. 3歳・5歳・7歳の子どものお祝い / c. 紅葉がいちばん美しい時 / d. 赤と白の長い飴. Keys: **141→b**, **142→d**, **143→a**, **144→c**. All correct.

### 2.2 Other key classes — all confirmed

- **Arithmetic (recomputed):** Q91 34−26=8 ✓; Q92 34+26=60 ✓; Q93 34+26+26+14=100 ✓; Q13/Q22 six `1`s in 平成11年11月11日 ✓; Q23 four sticks in `1111` ✓; Q54 10 (延長10回, G3) ✓; Q55 13 (13th title) ✓; Q56 3 (3 games to extra innings) ✓.
- **Choice/cloze/fill keys:** all verified against articles — weekday/date facts (9 Nov Mon, 11 Nov Wed, 27 Oct Tue, 13 Nov Fri, 15 Nov Sun, 19 Nov Thu, 22 Nov Sun), Japan Series scores (G1 3-1 11 inn, G2 4-3 10 inn, G3 2-1 10 inn walk-off HR by 正木智也, G4 4-2, G5–G7 not played, MVP 正木, 13th title, 2 straight years), survey figures (26% early Nov, 3% on 15th, 74% photo studio, 71% shrine prayer, n=200), foliage forecasts (Takao ~13 Nov, Miyajima 21 Nov, Arashiyama 23 Nov, Tokyo 29 Nov, Osaka 4 Dec; Weathernews 29 Oct 3rd forecast; JMC 2 Sep forecast), grammar clinic (past tense, こと nominalization, で for place of receiving/viewing).
- **Option-order swaps handled correctly:** Q87 (P6, key B 目安) vs Q126 (P8, key A 目安); Q103 (P7, key B slogan) vs Q128 (P8, key A slogan). Keys follow the swapped orders — not errors.
- **Cross-edition redirects (137/138):** key maps identical to core except 137/138 only (zh-tw: only 138 differs — its 137 sentence has no SC/TC-differing chars). Redirects verified as correct translations, e.g. en 137 `Shichi-Go-San is November 15.`, 138 `Pocky Day started in 1999.`; de 137 `Shichi-Go-San ist der 15. November.`; ko 137 `시치고상은 11월 15일이다.`; ru 138 `День Pocky начался в 1999 году.`; zh-tw 138 `波奇日從1999年開始。`. Adjudicated LEGITIMATE REDIRECTS (Japanese stems kept, native-language keys). 139/140 carry native-language stems with byte-identical Japanese keys in core and fan-outs.
- **Extractor artifact (NOT a defect):** `p8.py` extract truncated ru key 137 to `Сити-Го-Сан` because it splits dash-style notes at ` — `. The full SVG line is `137. Сити-Го-Сан — 15 ноября. — См. страницу 3` — complete and correct.
- **Model text (item 150):** 154 non-space characters excluding the `例：` label, verified from both `.text.md` and SVG elements (core `p8-tesuto.svg`, x=1451, y=464.4–558.6).

**Key-verification count: 149/150 confirmed. The sole exception is D-KEY-42 (§5).**

## 3. Full re-gate on the final artifacts (independent; fix worker's gate JSONs not trusted)

All gates run by the proofreader with `tools/venv/bin/python` under the Round 2 dir; core SVGs verified byte-identical before/after the gate run.

| Gate | Result |
|---|---|
| Freeze baseline | Exit 0, 8/8 byte-identical; core integrity re-hash clean |
| Freeze diff `--strict-cjk` | Exit 0, 0 added CJK for zh-cn/de/en/es/fr/it/nl/pt/ru. Exit 1 for ko and zh-tw only, both adjudicated legitimate (below) |
| ko freeze diff | Distinct added set identical to Round 1 (308 chars), total instances 3464 in both rounds (delta 0, no count diffs), ALL Hangul, 0 Han, no other scripts. Legitimate (Korean reader-language notes) |
| zh-tw freeze diff | Distinct added set identical to Round 1 (158 chars), total 839 → 849 (+10 exactly). Count diffs: 場 +3 (6→9), 買 +1, 東 +1, 號 +2, 沒 +1, 結 +1, 歡 +1 = +10 — exactly the 8 MAP conversions. No other change. (Note: `cjk_added_total` in freeze JSONs is a dict char→count, not an int.) |
| `p8.py` compare | CLEAN 150/150 for all 11; missing/extra/uncertain empty. Keydiffs: zh-cn `[]`; zh-tw `[138]`; other 9 `[137, 138]` — adjudicated legitimate redirects (§2.2) |
| Canonical occlusion audit (`occlusion_audit.py`) | 0 flags in all 11 editions; synthetic selftest passed on every run (all 6 planted classes fired, clean controls silent) |
| Counts (own `r2_counts.py`) | Stems 1–150 complete; P8 keys 1–150 complete; raw level chips A2 44 / B1 74 / B2 27 (145; 5 group/range labels); nearest-badge-in-column pairing split **A2 46 / B1 75 / B2 29**, 0 unpaired; per-page stem distribution 10/18/18/18/18/18/12/38; 0 overflow |
| P6 chart bars | x=315, widths **480/720/780/1020** (= 30×16/24/26/34), labels 山 34%, 神社 26%, 公園 24%, 町 16%, practice-data label present |
| P7 golden phrases | 8 phrases, each exactly 2× (article + P7), on source page and P7 in every edition; verbatim contiguous excerpts |
| Keys-flow max y (excl. footer; footer baseline 2624) | zh-cn 2514.9, de 2535.0, en 2532.0, es 2536.2, fr 2535.0, it 2535.0, ko 2520.4, nl 2537.4, pt 2533.5, ru 2524.0, zh-tw 2514.9 — clear in all editions |
| Pairing badges | Present (x=975, y=356, fill `#a4553a`, 19pt, weight 700, middle-anchored) with correct native-language text in all 10 fan-outs; core badge-less by W45 precedent (§1.5) |
| Masthead pixel clearance (own scan of rendered P1 cards, rows 100–450) | Wordmark band ends 265; subtitle 282–319; badge ~338–359; strapline 374–390. Inter-band gaps ≥13 units (wordmark→subtitle 16, subtitle→badge ≥18, badge→strapline 13–18). No band overlap. Subtitle/strapline/wordmark/footer attributes verified from SVG text elements |
| Weekday/date claims | All 15 explicit month+day+weekday claims in core SVGs calendar-verified (10-24 Sat, 10-25 Sun, 10-27 Tue, 10-28 Wed, 11-07 Sat, 11-09 Mon, 11-11 Wed, 11-13 Fri, 11-15 Sun, 11-19 Thu, 11-21 Sat, 11-22 Sun, 11-23 Mon, 11-29 Sun, 12-04 Fri) — all correct; issue dates 11-09–11-15 correct |
| PDFs (own `r2_pdf.py`) | All 11: 8 pages, web ≤ 7 MB, `pdftotext` bytes > 0, **web extraction byte-identical to print extraction**. Sizes (web B / text B): zh-cn 2,496,759 / 44,838; de 2,365,997 / 46,990; en 2,318,036 / 46,148; es 2,346,157 / 47,774; fr 2,344,131 / 47,669; it 2,337,474 / 47,549; ko 2,395,644 / 48,521; nl 2,340,930 / 46,803; pt 2,348,975 / 47,570; ru 2,254,296 / 54,264; zh-tw 2,872,565 / 44,817 |
| ABSTRACT.txt | Valid in all 11 (§1.2) |

## 4. Native-language correctness, reader-facing sweep, credits, visuals

- **Residue scans (own `r2_sweeps.py`):** 0 Hangul outside ko, 0 Cyrillic outside ru; 0 Chinese-prose marker hits (`读书周/练习/答案见/中文/简析/对照第`) in the 9 non-Chinese editions; ASCII-word profiles in each edition are the reader's own language (plus furniture: Lucerna, VOL, credits, proper names). Every explanation/gloss/note/abstract/footer in the reader's native language; register consistent.
- **Reader-facing sweep:** no week/language codes, repo links, SOP/proofread/audit wording, or structure labels on rendered pages. One false positive only: substring `cover` matched `covered` in the legitimate EN P8 note `74. 200 — The survey covered 200 Shichi-Go-San families` — not a defect. Only `VOL.4` occurrence is the P7 teaser/disclosure carry-over (Round 1 finding, unchanged).
- **Image credits:** all 3 photos credited on-page in all 11 editions — P1 maple (Poliphilo, CC0, Wikimedia Commons), P3 Hiroshige III 1876 print (歌川広重（三代）, public domain, Wikimedia Commons), P4 stadium (Syced, CC0, Wikimedia Commons).
- **Visual review (full frame, post-fix cards rendered 2026-11-03):** P1 ×11, P3 ×11, P8 ×11, P7 zh-tw — **all clean**: no overflow, overlap, missing glyphs/tofu, or missing credits. Q8 rewrap (§1.1) and Q32 rewrap render correctly in all 11; zh-tw P7 clinic Traditional forms visible; IT P1 numbers-box title fits (O-03 tight-but-passing, confirmed visually).

## 5. Residual defects — complete list

### D-KEY-42 (BLOCKING) — P8 key 42 omits a stem piece; present in ALL 11 editions

- **Stem (P3, item 42, all editions):** `酉の市で / 熊手を / 買います → ___` (造句 — build a sentence from the pieces).
- **Printed key (P8 answers, all 11 editions):** `42. 熊手を買います。` — e.g. core `p8-tesuto.svg`: `42. 熊手を買います。 — 在酉の市买熊手`; en: `42. 熊手を買います。 — Buying a kumade at Tori-no-ichi`; zh-tw: `42. 熊手を買います。 — 在酉の市買熊手`.
- **Defect:** the Japanese key sentence omits the stem piece `酉の市で` (the location). The reader-language note in every edition supplies the location, but the Japanese key itself is incomplete relative to its own stem.
- **Convention evidence:** all 7 sibling 造句 items include EVERY stem piece in the key — 39 (`七五三は子どものお祝いです。`), 40 (`神社へお参りに行きます。`), 41 (`千歳飴をもらいます。`), 133, 134, 135 (`神社で千歳飴をもらいます。`, incl. the `で`-location piece), 136. Q42 is the sole exception.
- **Correct key:** `酉の市で熊手を買います。`
- **Severity:** BLOCKING. The key sentence is grammatical and true (not a wrong letter), but incomplete under the issue's own 造句 convention; a learner checking their answer against the printed key is told a sentence missing a required piece is the answer. The defect is inherited from the core and is present identically in all 11 editions' P8 renderings.
- **Fix required (by the builder, not the proofreader):** change the P8 key 42 sentence in the core (and fan-outs) to `酉の市で熊手を買います。`, keeping the reader-language notes; re-gate P8 only.

**No other residual defect was found.** In particular: no wrong key letter other than the Q42 omission; no kinsoku, abstract, SC-residue, freeze, p8, occlusion, count, chart, badge, PDF, credit, or visual defect remains.

### Non-defects / record notes (explicitly NOT defects)

1. Fix-report "190 occurrences" figure — wrong (true BEFORE total 136; see §1.3). Fix-record reporting error only; the editions are clean.
2. Old-md5 global grep incomplete (§1.1 caveat) — scoped verification complete; not an edition defect.
3. `p8.py` ru key-137 truncation — extractor artifact (§2.2); SVG line complete.
4. EN `covered` substring hit — false positive (§4).
5. Badge-less core subtitle; O-01–O-05 cosmetics — adjudicated non-defects (§1.5), not re-raised.

## 6. Per-edition verdict

| Edition | Verdict | Blocking defects |
|---|---|---|
| 2026-w46-ja-de | **FAIL** | D-KEY-42 |
| 2026-w46-ja-en | **FAIL** | D-KEY-42 |
| 2026-w46-ja-es | **FAIL** | D-KEY-42 |
| 2026-w46-ja-fr | **FAIL** | D-KEY-42 |
| 2026-w46-ja-it | **FAIL** | D-KEY-42 |
| 2026-w46-ja-ko | **FAIL** | D-KEY-42 |
| 2026-w46-ja-nl | **FAIL** | D-KEY-42 |
| 2026-w46-ja-pt | **FAIL** | D-KEY-42 |
| 2026-w46-ja-ru | **FAIL** | D-KEY-42 |
| 2026-w46-ja-zh-cn (core) | **FAIL** | D-KEY-42 |
| 2026-w46-ja-zh-tw | **FAIL** | D-KEY-42 |

All three Round 1 defects (D-CORE-01, D-CORE-02, D-ZHTW-01/02) are CONFIRMED FIXED in every edition. The only remaining blocker is the single inherited key omission D-KEY-42, identical in all 11.

## 7. Gate outputs summary

Saved under `hidden_files/w46/ja-proofread-gates-round2/`: `run_gates.sh`, `gates-run.log`, `core-svg-sha256-before.txt`, `core-svg-sha256-after.txt`, `baseline-ja/` (freeze baseline), `freeze-*.json` (11), `p8compare-*.json` (11), `occlusion-*.json` (11), `p8extract-core.json`, `p8extract-*.json` (10), `r2_kinsoku.py`, `kinsoku-orphan-round2.json`, `kinsoku-round2.log`, `r2_abstracts.py`, `abstracts-round2.json`, `abstracts-round2.log`, `r2_sc.py`, `sc-scan-round2.json`, `sc-scan-round2.log`, `r2_counts.py`, `counts-round2.json`, `counts-round2.log`, `r2_pdf.py`, `pdf-round2.json`, `pdf-round2.log`, `r2_masthead.py`, `masthead-round2.log`, `r2_sweeps.py`, `sweeps-round2.json`, `sweeps-round2.log`, and this verdict file. Headline: freeze 8/8 + strict-CJK adjudicated; p8 CLEAN 150/150 ×11; occlusion 0 ×11; kinsoku/orphan 0/0/0 ×11; counts 150 / 46-75-29 ×11; PDFs 8 pages, web==print ×11; visuals P1/P3/P8 ×11 + P7 zh-tw clean.

## 8. Final verdict

ROUND 2 FAIL (blocking defect D-KEY-42 in all 11 editions: P8 key 42 `熊手を買います。` omits the stem piece `酉の市で`; correct key `酉の市で熊手を買います。`). All Round 1 defects are confirmed fixed; no other defect remains.
