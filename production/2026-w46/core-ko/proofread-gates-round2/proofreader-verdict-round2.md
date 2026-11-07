# Round 2 Proofreader Verdict — Lucerna Weekly VOL.3, W46, KO target

- **Issue:** VOL.3, dated Mon 2026-11-09 to Sun 2026-11-15 (Asia/Seoul).
- **Proofreader:** independent, Round 2. Did not build or fix these editions. No edition file was edited, no re-render, no push, no insert, no Discord post, no contact with `~/workspace/weekly-git`.
- **Scope:** 11 editions, one per reader-native language: de, en, es, fr, it, ja, nl, pt, ru, zh-cn, zh-tw. There is NO ko-ko edition. The canonical core dir `files/weekly-report-w46-ko-core/` is the zh-cn edition content and is NOT a 12th edition.
- **Gate dir (this round):** `hidden_files/w46/ko-proofread-gates-round2/` — all gate JSONs/logs/scripts below live there. The Round 1 gate dir was not reused.
- **Documents read first:** SOP (`files/weekly-report-SOP.md`, full), Round 1 verdict (`hidden_files/w46/ko-proofread-gates/proofreader-verdict-round1.md`), fix record (`hidden_files/w46/ko-fix/FIX-REPORT.md` + fix records appended to each edition's `WEEKLY-KIT.md`), tools README (`tools/README.md`). Round 1 Observations O1–O8 stand as adjudicated and are not re-raised.
- **Caveat (carried from Round 1, unchanged):** external article facts were NOT checked against live sources; verification is internal consistency against the KIT/article text only. No live-browser work is available to this subagent.

## Per-edition verdicts

| Edition | Verdict | Blocking defects |
|---|---|---|
| 2026-w46-ko-de | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 — all frozen core, all 11 editions |
| 2026-w46-ko-en | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-es | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-fr | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-it | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-ja | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-nl | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-pt | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-ru | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-zh-cn (core) | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |
| 2026-w46-ko-zh-tw | **FAIL** | R-GLOSS (restore), D3 item 54, D4 item 103 |

No edition-specific defects were found. All three blocking defects are frozen-core defects present identically in all 11 editions. All three are minor severity (single-word / single-entry / single-suffix), same class as Round 1's D1/D2, and all three block under proofread-until-zero as written.

## 1. Fix verification — D1 and D2 as applied

### D1 (zh-tw only): P6 gloss Simplified `规` → Traditional `規`

**CONFIRMED.** Evidence, independently re-measured this round:

- zh-tw P6 gloss line (`svg/p6-gipi.svg`): `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` — `規` U+898F present, `规` U+89C4 absent.
- `规` = 0 across all zh-tw SVG text; `規` = 2 in zh-tw (P6 gloss + P8 key 96 `규모`). Core zh-cn retains `规` = 2, as expected for the Simplified edition.
- Expanded Simplified-only scan (OpenCC `s2t` over ALL zh-tw SVG `<text>`, `zh-tw-simp-scan.log`): exactly 2 distinct candidates — `峰` U+5CF0 ×8 (e.g. P1 `高峰`; the standard Traditional form in this usage — `s2t`→`峯` is a variant preference, not a Simplified-only character) and `准` U+51C6 ×1 (P8 `准考證`, the standard Traditional term). Both adjudications re-verified independently: **non-defects**. No other Simplified-only character remains in zh-tw.
- P6 zh-tw card viewed at full frame: gloss inside its box, table clean, no overflow/overlap.

### D2 (all 11): P3 gloss headword `가늘다` deleted

**CONFIRMED as applied — but see §2: the deletion itself is ruled a blocking defect requiring restoration.** The fix worker executed exactly what Round 1 ordered; the order rested on a false premise.

Evidence, independently re-measured this round:

- `가늘` = 0 in the joined SVG text of all 11 editions.
- P3 gloss lines in all 11 editions show the shortened gloss with the `가늘다` entry removed and every other entry intact (full wrapped text verified, including continuations):

| Edition | P3 gloss as shipped (post-fix) |
|---|---|
| zh-cn (core) | `译注｜겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。` |
| de | `HINWEIS · 겹치다 = sich überschneiden · 감사하다 = danken · 나누다 = unterscheiden, teilen` |
| en | `Note — 겹치다 = to overlap · 감사하다 = to thank · 나누다 = to tell apart, to share` |
| es | `Nota — 겹치다 = coincidir, solaparse · 감사하다 = agradecer · 나누다 = distinguir, compartir` |
| fr | `Note — 겹치다 = se chevaucher · 감사하다 = remercier · 나누다 = distinguer, partager` |
| it | `Nota — 겹치다 = sovrapporsi · 감사하다 = ringraziare · 나누다 = distinguere, condividere` |
| ja | `解説 — 겹치다 = 重なる · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` |
| nl | `Uitleg — 겹치다 = samenvallen · 감사하다 = bedanken · 나누다 = onderscheiden, delen` |
| pt | `Nota — 겹치다 = sobrepor-se · 감사하다 = agradecer · 나누다 = distinguir, partilhar` |
| ru | `Пояснение — 겹치다 = совпадать · 감사하다 = благодарить · 나누다 = различать, делиться` |
| zh-tw | `譯注｜겹치다 重疊 · 감사하다 感謝 · 나누다 區分、分享。` |

- `.text.md` exports agree: each edition's export carries the same shortened gloss line (grep-verified, all 11).
- P3 gloss-box geometry: gloss text sits inside its box in all 11 editions (box rects checked: e.g. core box x=527 w=434, y=1316.95 h=115.95, gloss lines y=1355.45/1385.175; de box y=1346.675 h=145.675, gloss lines 1385.175/1414.9/1444.625). All 11 P3 cards viewed at full frame: shortened gloss inside its box with margins, no overflow, no overlap, no other gloss entry disturbed. Canonical occlusion audit: 0 flags on every page of every edition.
- Fix records appended to all 11 `WEEKLY-KIT.md` files (grep: `가늘` 2–3 hits per KIT, `가늰` 1–2 hits per KIT — the fix record text itself).

**Adjudication of the fix claims:** D1 **CONFIRMED**. D2-as-applied **CONFIRMED** (deletion executed exactly as ordered, geometry clean, no collateral damage). The Round 1 "occurs nowhere" premise behind D2 is **REFUTED** — see §2, which converts the applied deletion into blocking defect R-GLOSS.

## 2. The `가늰` adjudication — GLOSS MUST BE RESTORED (blocking, minor, frozen core, all 11)

### 2.1 Round 1's claim is REFUTED as stated

Round 1 (D2) claimed the gloss headword `가늘다` "occurs nowhere in the issue", on evidence that a full-text search for `가늘` returned exactly 1 hit (the gloss itself) and that the stems `가는, 가늘게, 가느다란, 얇` returned 0. That evidence was incomplete: it did not cover the attributive inflection `가늰`.

Codepoint fact (independently re-verified this round): `가늘` = 가 U+AC00 + 늘 U+B298; `가늰` = 가 U+AC00 + 늰 U+B2B0. `'가늘' in '가늰'` is `False` — a substring search for `가늘` cannot see `가늰`. The deletion was therefore ordered on a false premise. **The deletion must NOT be presented as proof the word never occurred in inflected form.** The word occurs 3× per edition in inflected form.

### 2.2 The 3 occurrences, independently verified (core AND fan-outs)

`가늘` = 0 in all 11 editions; `가늰` = exactly 3 per edition, identical Korean contexts in all 11 (stems are frozen Korean; only type labels are translated). Quoted with page/item context:

1. **P3 body**, `p3-munhwa.svg`, x=527, y=666.95 (core; y=696.675 in de/en/es/fr/it/ja/nl/pt, y=726.4 in ru):
   > `길고 가늰 과자를 친구와 나누는` — line of the Pepero Day paragraph ("the day you share long, thin snacks with friends").
2. **P5 body**, `p5-cheongnyeon.svg`, x=527, y=1251.45 (core/de/en/es/fr/ja/pt/zh-tw; y=1340.45 it, y=1281.175 nl, y=1370.175 ru):
   > `줘요. 길고 가늰 과자 한 상자를 건네며` — followed by `'날씬해지자'고 말하기도 해요` ("…handing over a box of long, thin snacks, saying 'let's get slim'").
3. **P5 exercise 69, option A**, `p5-cheongnyeon.svg`, x=65, y=2306.225 (core/de/en/fr/ja/zh-tw; y=2335.95 es/it/nl/pt/ru):
   > Stem: `빼빼로데이에는 무엇을 나눠 줘요? A. 길고 가늰` (option continues `과자`; B. `가래떡만`, C. `김치`). P8 key 69 = A in all 11 editions.

No edition glosses `가늘/가늰` anywhere post-fix: the P5 gloss boxes (checked in zh-cn/de/en/ja/zh-tw) gloss `날씬해지다` ("become slim") and `건네다`, not `가늘다`. The deleted P3 gloss was the issue's only definition. The builder's own KIT had already adjudicated `가늘다 → 가늰` a legitimate dictionary/inflected pair among 14 pairs ("no true gloss orphans remain") before Round 1.

### 2.3 Recoverability judgment — not reliably recoverable

Arguments for recoverability were weighed and found insufficient:

- **For:** the parallel adjective `길고` (long) + `과자` (snack/stick) + the Pepero Day "four 1s like sticks" explanation + the exact collocation `길고 가늰 과자` repeated at all 3 occurrences + the P5 `날씬해지자` ("let's get slim") association all point in the right direction. An advanced reader could guess "thin/slim".
- **Against (decisive):** (a) `가늰` is an irregular attributive inflection of `가늘다` (ㄹ-irregular: stem-final ㄹ drops before the attributive ending, and the remaining syllable changes at codepoint level) — an A2–B1 reader cannot derive it from the dictionary form by rule, and the dictionary form is precisely what a gloss supplies; (b) it is the correct answer to a **tested item** (69) — the reader must select it as the answer, so guessing is not good enough; the item tests a word the issue no longer defines; (c) SOP §8.1 ("注释的词必须真实出现在正文里" — glossed words must genuinely occur in the text) is satisfied by the inflected occurrence: the gloss was legitimate under the SOP's own rule, and the KIT adjudication said so; (d) restoration costs one gloss entry with no reflow risk — it fit pre-fix, in the same box, in all 11 editions.

The deletion is therefore **not** acceptable. A reader at the issue's own A2–B1 level cannot be relied on to recover `가늰` without the gloss, and the tested item makes the gap consequential rather than cosmetic.

### 2.4 RULING: GLOSS MUST BE RESTORED (blocking defect R-GLOSS)

**R-GLOSS — blocking, minor severity, frozen core, all 11 editions.** Restore the `가늘다` entry exactly as it stood pre-fix, re-inserted after the `겹치다` entry, keeping each edition's native prefix and all other entries byte-identical. Exact restoration text per edition (from the fix report's Before column, verified against the shipped After lines — the restoration is the Before column verbatim):

| Edition | Restore to (full gloss entry; prefix unchanged) |
|---|---|
| zh-cn (core) | `译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。` |
| de | `HINWEIS · 겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen` |
| en | `Note — 겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share` |
| es | `Nota — 겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir` |
| fr | `Note — 겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager` |
| it | `Nota — 겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere` |
| ja | `解説 — 겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` |
| nl | `Uitleg — 겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen` |
| pt | `Nota — 겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar` |
| ru | `Пояснение — 겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться` |
| zh-tw | `譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。` |

An alternative reworded entry covering the inflected form directly (e.g. glossing `가늰` itself) was considered and is NOT required: restoring the dictionary-form entry as-is matches the issue's gloss convention for every other inflected word (e.g. `겹치다`, `감사하다` glossed in dictionary form while occurring inflected), and the KIT already adjudicated this pair legitimate. Restore as-is; do not reword.

## 3. Full key verification — 150/150 verified semantically

Method: own extraction (`extract_exercises.py`, file-order SVG `<text>` parse; badge+number starts; P8 answers parsed separately after the `답 ·` header) → `exercises-all.json` + `exercises-<code>.txt` per edition. 138 blocks per edition = 150 items (4 range blocks ×4 items: 25–28, 43–46, 61–64, 141–144). P8 answers: 150 per edition. Every key was verified semantically in the core against article/stem/grammar, and cross-checked in all 11 editions: P8 key-heads are byte-identical across all 11 editions except the expected translation re-aims of keys 137/138 and the item-150 model pointer (see below); `p8.py compare` is CLEAN 150/150 in all 11 (see §5). Matching-block stems/options are byte-identical Korean in all 11 editions (only type labels translated), so the core matching verification transfers to every edition.

**Result: 148 of 150 keys correct. 2 keys are correct as letters but their stems are ungrammatical (D3, D4 below) — the defect is in the stem, not the key letter.** No wrong key letter was found in any edition. Count: **150/150 key letters verified; 148/150 stem+key pairs fully sound; 2 stem defects (D3, D4).**

### 3.1 Matching blocks — option-by-option (core P8 keys; identical in all 11)

| Block | Stems → options (verbatim) | P8 keys | Verdict |
|---|---|---|---|
| 25–28 (P2, A2) | 25. 김장 26. 새우젓 27. 소방의 날 28. 한능검 — a. 겨울 김치를 담그는 일 b. 한국사 시험의 줄임말 c. 값이 크게 오른 젓갈 d. 119에서 온 11월 9일의 날 | 25=a, 26=c, 27=d, 28=b | Correct. 김장 = winter-kimchi making (a); 새우젓 = the risen-price salted shrimp (c); 소방의 날 = Nov 9 from 119 (d); 한능검 = Korean History exam abbreviation (b). |
| 43–46 (P3, A2) | 43. 내장산 44. 월출산 45. 두륜산 46. 설악산 — a. 산림청 예보 11월 9일 b. 공단 예보 11월 11일 c. 실제 관측 10월 16일 d. 산림청 예보 11월 11일 | 43=b, 44=a, 45=d, 46=c | Correct. 내장산 = parks-agency forecast Nov 11 (b); 월출산 = Forestry Service forecast Nov 9 (a); 두륜산 = Forestry Service forecast Nov 11 (d); 설악산 = actual observation Oct 16 (c). Note options a/d differ only by date — keys match the article's agency/date pairings exactly. |
| 61–64 (P4, B1) | 61. 준플레이오프 62. 플레이오프 63. 한국시리즈 64. 이동일 — a. kt wiz와 삼성이 싸워요 b. KIA가 LG를 3연승으로 이겼어요 c. 시리즈 사이에 하루가 필요해요 d. 삼성이 KIA를 3승 2패로 이겼어요 | 61=b, 62=d, 63=a, 64=c | Correct. 준플레이오프 = KIA's 3 straight wins over LG (b); 플레이오프 = Samsung beat KIA 3–2 (d); 한국시리즈 = kt wiz vs Samsung (a); 이동일 = a rest day between series (c). |
| 141–144 (P8, B2) | 141. 절정 142. 김장 143. 예보 144. 관측 — a. 겨울 김치를 담그는 일 b. 단풍이 가장 아름다운 때 c. 실제로 본 날짜나 날씨 d. 미리 알린 날짜나 날씨 | 141=b, 142=a, 143=d, 144=c | Correct. 절정 = the most beautiful foliage moment (b); 김장 = winter-kimchi making (a); 예보 = announced-in-advance date/weather (d); 관측 = actually-observed date/weather (c). |

### 3.2 All other keys

- **Choice keys (1–150, non-matching):** every key verified against the article text, the P6 comparison table, or the P5/P7 source sentences. All correct as letters. Spot principles applied: uniqueness checked where a distractor could plausibly also be right (item 37: only `농업인` yields the correct compound `농업인의 날`; `빼빼로/가래떡 + 의 날` are wrong forms — cleared). Item 72 checked against the P5 article and cleared (article confirms the exact phrasing `선물하기도 해요`).
- **Cloze/fill keys:** every key reconstructs grammatically with its stem **except D3 and D4** (see §4). Systematic check: item 54 is the SOLE fill item whose key ends with the stem's own suffix; item 103 is the sole quotative-particle mismatch.
- **Arithmetic/numerical keys, recomputed:** D-counts Nov 9 = D-10, Nov 12 = D-7, Nov 15 = D-4, Nov 19 = D-day (date arithmetic re-verified with `date -d`, Asia/Seoul: Nov 9 Mon, 12 Thu, 15 Sun, 18 Wed, 19 Thu, 22 Sun, 28 Sat — all correct); prices 5,557 / 20,269; −10.3% / +32.5%; playoff scores 3–2 / 6–1 / 5–1; 551,864 candidates; 1,312 sites; 27,000-won fee; 50% / ~80% criteria — all consistent with KIT/article text. External facts not live-checked (see caveat).
- **Sentence-order items 79–82, 133–136:** verified correct as printed.
- **Translation items 137–140 (core):** 137 `11月12日是D-7。`, 138 `泡菜季正忙。`, 139 `11월 11일은 이름이 세 개예요。`, 140 `저는 수요일에 친구에게 가래떡을 나눠 줘요。` — all correct. Fan-out re-aims of 137/138 verified per edition and all correct (de `Der 12. November ist D-7.` / `Kimjang ist in vollem Gange.`; en `Nov 12 is D-7.` / `Kimchi season is in full swing.`; es/fr/it/nl/pt/ru/ja equivalents likewise correct, including ja 138 `キムジャンの季節は最盛期だ。` and ru 137 `12 ноября — D-7.`; zh-tw shares the core keys, keydiff []). Item-150 model pointers are translations of the same pointer in every edition (e.g. en `Model text in section H of this page (158 characters)`).
- **Item 150 writing model:** no-space count 160 including the `예:` label; excluding the label, body = 158 chars — reproduces the printed `158자` claim exactly; in any counting the model sits inside the printed 150–200자 instruction. No defect.
- Extraction artefact (not an edition defect): file-order interleaving appends following-column/section-header text to a few extracted items (6, 15, 20, 24, 33, 38, 42, 51, 56, 60, 104, 112, 120, 128, 136, 149); stems/keys themselves were verified against raw SVG dumps. Display artefacts: `��` glyphs seen in tool output for strings such as `김장비는` are transport/display artefacts; codepoint dumps verified clean, and U+FFFD = 0 in all joined SVG text.

## 4. New / residual defects (blocking)

All three are frozen-core defects, present identically in all 11 editions (Korean stems frozen; only type labels translated). All are minor severity, same class as D1/D2.

### D3 — NEW, BLOCKING, minor: item 54, P4 — doubled verb ending

- **Stem (all editions, `p4-seupocheu.svg`):** `한국시리즈 시작이 하루 ___어요.`
- **P8 key (all editions):** `밀렸어요` (e.g. zh-cn: `54. 밀렸어요 — 开幕因雨和第五场推迟一天`).
- **Defect:** literal substitution gives `하루 밀렸어요어요` — the key already ends in `어요`, doubling the stem's own suffix. Systematic check of all fill items: 54 is the SOLE item where the key ends with the stem's own suffix (contrast item 19 `조심` + `하세요`, item 20 `좌우` + `한다고` — all others reconstruct grammatically).
- **Fix (coordinator's choice):** change the stem to `한국시리즈 시작이 하루 ___.` (key `밀렸어요` unchanged) OR change the key to `밀렸`. Either restores a grammatical sentence; the stem change is cleaner (keeps the full polite form as the answer).

### D4 — NEW, BLOCKING, minor: item 103, P7 — wrong quotative particle

- **Stem (all editions, `p7-mal.svg`):** `미리 소금에 절인 배추를 ___이라고 해요.`
- **P8 key (all editions):** `절임배추` (e.g. zh-cn: `103. 절임배추 — 提前用盐腌好的白菜`).
- **Defect:** `배추` ends in the vowel-final syllable 추 (no batchim), so the correct quotative is `라고`, not `이라고`: the correct form is `절임배추라고 해요`. Contrast item 101 `김장이라고` (김장 is batchim-final — correct) and item 34 `절정이라고` (correct). The stem as printed is ungrammatical with the key.
- **Fix (coordinator's choice):** change the stem to `미리 소금에 절인 배추를 ___라고 해요.` (cleanest; key unchanged) OR reword the stem. Either restores grammaticality.

### R-GLOSS — residual from the D2 fix: gloss deletion must be restored

See §2 in full. Blocking, minor, frozen core, all 11 editions. Exact restoration text per edition in §2.4.

**Complete residual defect list: R-GLOSS (all 11) + D3 item 54 (all 11) + D4 item 103 (all 11).** No other defects found. No edition-specific defects found.

## 5. Gate outputs summary (all re-run independently this round; fix worker's gate JSONs were not trusted)

| Gate | Result | Artefacts |
|---|---|---|
| Freeze baseline | 8/8 SVGs byte-identical (core); shipped core SVGs unchanged by the run. Exit 0. | `freeze-baseline/`, `freeze-baseline.log` |
| Freeze diffs per edition (`tools/freeze.py diff`) | Latin/Cyrillic editions: `cjk_added_total = {}` (0 added CJK/Hangul). ja: added total 2,662 CJK-range, Hangul added 0 (Round 1: 2,664; −2 = the deleted gloss entry — consistent with the D2 fix). zh-tw: added total 903, Hangul added 0. pt: added total 8 Hangul, P7 only, distinct chars 어/울/요/에/났/서/만 (서×2) = the quoted `서울에서 만났어요` (adjudicated quote, Round 1 O2 pattern). Removed-string review: long-Hangul removed strings are furniture/instructions/headers/disclosure only; no article-body sentence removed. | `freeze-<code>.json/.log` (10 files) |
| Article preservation | 153 article sentences from the core `.text.md` (≥15 Hangul chars, pure-Korean lines) found whitespace-insensitively in every edition's joined SVG text: 0 missing in 10 editions; ja missing 1 only — the P1 subtitle furniture line `한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로` (replaced by the badge in the subtitle slot — adjudicated ja precedent, O6 family variant). | `checks.json`, `checks.log` |
| p8.py compare (`--target ko`) | CLEAN 150/150 in all 11 editions; keydiff [137, 138] in all fan-outs except zh-tw []; core-vs-itself CLEAN, keydiff []. Exit 0 all. (Set equality only — semantic verification is §3 above.) | `p8-<code>.json/.log` (11 + core) |
| Canonical occlusion audit (`tools/occlusion_audit.py`; selftest OK — all 6 planted classes fired, clean controls silent) | **0 flags in all 11 editions, all 88 pages.** | `occlusion-<code>.json/.log`, `occlusion-selftest.log` |
| Counts re-measured (extraction, ranges expanded) | TOTAL 150, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 — identical in all 11 editions. | `exercises-all.json`, `exercises-<code>.txt` |
| Kinsoku scan | 0 in all 11 (lines starting with closing punctuation `).,;:!?…»」』》’”`). | `checks.json` |
| Own koscan/orphan scan (`koscan-round2.py`; window 10–45px, same-column x within 30px, pure-Hangul fragments; TRUE_SPLIT iff joined fragments form a word attested in that edition's build `.py` string literals read via `ast`, never imported/executed; orphan short lines ≤2 chars incl. parenthesised fragments; line-start orphan punctuation) | **TRUE_SPLITS=0, S3=0 (both ≥3 and ≤3 senses), LINESTART=0 in all 11 editions.** 10–11 ORPHANshort hits per edition, all adjudicated non-defects: complete words/labels, not fragments — P1 brief heads `예보/김장/단풍/야구`, P2 list tail `필수`, P3 checklist items `물/간식` (+ zh-tw credit-wrap `사진`), P4 ladder label `삼성`, P6 table header `구분`, P7 option-wrap tail `해요` (2 syllables, complete word, wrap of `안 해요`). No mid-word split anywhere. The fix worker's reconstructed script was read and NOT reused unexamined (its documented first-version false-flag — fusing `두산에` + `4대` into `두산에대` — was corrected to require pure-Hangul fragments; this round's independent implementation agrees: 0 true splits). | `koscan-round2.py`, `koscan-round2.json`, `koscan-round2.log` |
| P7 phrases | All 8 KIT phrases verified as verbatim contiguous excerpts in the articles AND present on P7, all editions (whitespace-insensitive). | `checks.json` |
| P6 comparison table | 12/12 cells present, identical Korean cells in all editions. **No bar chart exists on P6** — rect inventory (39 rects, core): background, double border, header band, gloss boxes, table cells (3 cols × 4 rows at y=1268–1476), level badges. There are no data bars to measure; the table is the P6 visual. Table-cell geometry identical across editions. | `checks.json` |
| Script residue | Han chars in Latin/Cyrillic editions = only `一十土` (P3 Hanja paragraph); kana = 0 outside ja; Cyrillic = 0 outside ru; U+FFFD = 0 everywhere. zh-cn: 0 Traditional-only chars (OpenCC t2s diff empty). zh-tw: t2s diffs are expected Traditional forms only. Latin tokens in zh-cn/zh-tw/ja = brands/proper names/credits only (KIA, kt wiz, KBO, Lucerna, VOL, Wikimedia Commons, D- markers). | `checks.json`, `zh-tw-simp-scan.log` |
| Reader-facing sweep | Hits only false-positive substrings — `core` inside `coreano/coreana`, `encore` (French word), `Score` — 0 genuine internal-production terms. | `checks.json` |
| Badge / footer | Masthead `Lucerna` y=262 all editions; badge line y=394, 20pt form in de/en/es/fr/it/nl/pt/ru/zh-tw (subtitle shifted 372→366); ja badge in subtitle slot y=372 (19.5pt form); core has no discrete badge line (O6 precedent, matches W45 core). Footers present on all pages with correct native pairing labels and page numbers (P1 footers verified in `checks.json`). | `checks.json` |
| ABSTRACT.txt | All 11: single logical line, no ASCII double quote, reader-native, practice framing, masthead + VOL.3 + target + A2–B2 + 150 present (e.g. zh-cn ends `A2 到 B2 分级，150 道练习题。`; zh-tw `A2 到 B2 分級，150 道練習題。`). | `checks.json` |
| Dates / weekdays | Re-verified with `date -d`, Asia/Seoul: Nov 9 Mon, 10 Tue, 11 Wed, 12 Thu, 13 Fri, 14 Sat, 15 Sun, 18 Wed, 19 Thu, 22 Sun, 28 Sat. D-counts: Nov 9 D-10, Nov 12 D-7, Nov 15 D-4, Nov 19 D-day — all correct. | this verdict (§3.2) |
| Web PDFs | All 8 pages, ≤7 MB (2,243,230–2,661,269 bytes), `pdftotext` bytes 50,748–61,377, matching the fix report's inventory. | `checks.json`, `inventories.json` |
| Print PDFs | All 8 pages; `pdftotext` bytes 50,748–61,377 (text layer present); sizes 30,826,972–36,156,571 bytes. | `print-pdf-inventory.log` |
| Writing model (P8 item 150) | 158-char claim reproduced exactly (body 158 chars excl. `예:` label; 160 incl. label). | §3.2 |
| Cards viewed at full frame | P1 + P8 all 11 editions, P3 ×11, P6 zh-tw — 34 cards, all clean: no overflow, overlap, missing glyphs/tofu, or missing image credits. P3 gloss boxes contain the shortened gloss with margins in all 11. P6 zh-tw gloss shows `規模` correctly. | §1, §5 (this table) |
| Native-language correctness | Every explanation, gloss, note, abstract and footer in the reader's native language; no untranslated strings; no wrong-script residue; register consistent. Translated P8 notes for keys 137/138 verified per edition (all correct); matching-block option translations verified (Korean stems identical; type labels correctly translated). | §3, `checks.json` |

## 6. Notes for the coordinator

- The three blocking defects are all one-line fixes in the frozen core + fan-out rebuild; the R-GLOSS restoration re-uses text that already fit pre-fix, and D3/D4 each have a clean single-line fix option that leaves the key unchanged. After fixing, a re-gate (freeze/p8/occlusion + P3/P4/P5/P7 card spot-check) is required before shipping — this verdict does not pre-approve the fixed artifacts.
- Round 1's D2 deletion order should be recorded as issued on a false premise so the same stem-search error is not repeated: a gloss headword's inflected forms must be searched by stem/inflection family (including ㄹ-irregular attributive `가늘다 → 가늰`), not by a single substring.
- The background inventory job from the previous session never delivered; its figures were independently re-measured this round (web + print PDF inventories above) and are not relied on.

## Final verdict

**ROUND 2 FAIL — blocking defects: R-GLOSS (gloss `가늘다` must be restored, all 11 editions), D3 (item 54 stem doubled ending, all 11 editions), D4 (item 103 stem wrong quotative particle, all 11 editions).**
