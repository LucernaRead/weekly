# Proofreader Verdict — Round 3 (FULL round, all 11 editions)

**Issue:** Lucerna Weekly W46, dated Mon 2026-11-09 – Sun 2026-11-15. KO target.
**Editions (11; NO ko-ko edition):** `2026-w46-ko-de`, `-en`, `-es`, `-fr`, `-it`, `-ja`, `-nl`, `-pt`, `-ru`, `-zh-cn`, `-zh-tw`. Canonical core dir `files/weekly-report-w46-ko-core/` is the zh-cn edition content, not a 12th edition.
**Proofreader role:** independent; did not build or fix these editions. Proofreader only — nothing was fixed, re-rendered, or edited in any edition file. `~/workspace/weekly-git` and `index.json` were never touched; nothing was pushed, inserted, or posted to Discord.
**Gate dir (fresh):** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-proofread-gates-round3/`
**Round 3 fix record adjudicated:** `.../hidden_files/w46/ko-fix-round3/FIX-REPORT.md` + Round 3 records appended to each edition's `WEEKLY-KIT.md`.
**Prior verdict:** Round 2 FAIL, all 11 editions, on three frozen-core defects (R-GLOSS, D3, D4). Round 1 Observations O1–O8 stay as adjudicated and were not re-raised.
**Date of this verdict:** 2026-11-03 (EST).

## Final verdict line

**ROUND 3 PASS (all 11 shippable)**

No new defects and no residual defects were found in any check. All three Round 2 blocking defects are CONFIRMED fixed in all 11 editions. All re-gates are clean. The `'D-7'이라고` usage is adjudicated ACCEPTABLE (see §3).

## Per-edition PASS/FAIL

| Edition | Verdict |
|---|---|
| 2026-w46-ko-de | PASS |
| 2026-w46-ko-en | PASS |
| 2026-w46-ko-es | PASS |
| 2026-w46-ko-fr | PASS |
| 2026-w46-ko-it | PASS |
| 2026-w46-ko-ja | PASS |
| 2026-w46-ko-nl | PASS |
| 2026-w46-ko-pt | PASS |
| 2026-w46-ko-ru | PASS |
| 2026-w46-ko-zh-cn (core) | PASS |
| 2026-w46-ko-zh-tw | PASS |

## 1. Fix verification

All fix claims were verified independently in the fresh Round 3 gate dir (own ET-based extraction `r3_fixverify.py`, own exercise extraction, own sweeps; the fix worker's gate JSONs were not trusted). Adjudication: CONFIRMED / PARTIAL / REFUTED per claim.

### 1.1 R-GLOSS — `가늘다` gloss entry restored — CONFIRMED, 11/11

Expected strings are Round 2 verdict §2.4 / FIX-REPORT §1 (identical in both). Every edition's P3 gloss line is byte-equal to its expected string (MATCH 11/11, `fix-verification.json`):

- zh-cn: `译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。`
- de: `HINWEIS · 겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen`
- en: `Note — 겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share`
- es: `Nota — 겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir`
- fr: `Note — 겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager`
- it: `Nota — 겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere`
- ja: `解説 — 겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う`
- nl: `Uitleg — 겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen`
- pt: `Nota — 겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar`
- ru: `Пояснение — 겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться`
- zh-tw: `譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。`

Counts in every edition's joined SVG text: `가늘` = 1 (gloss only), `가늰` = 3 (P3 body `길고 가늰 과자를 친구와 나누는`, P5 body `길고 가늰 과자 한 상자를 건네며`, P5 exercise 69 option A, key 69 = A). P3 gloss-box geometry clean in all 11 (top margin 38.5, bottom margin 47.725 in every edition; core/zh-tw 2 gloss lines, other 9 editions 3 lines; gloss lines inside their boxes). All 11 P3 cards viewed at full frame: restored gloss inside its box, no overflow/overlap/tofu; image credits present (Udonhan1992 CC0; Paul Cézanne Public domain).

KIT discrepancy-flag resolution: the Round 1 discrepancy flag is resolved in ALL 11 `WEEKLY-KIT.md` files — each carries exactly one `resolves the Round 1 discrepancy flag` line stating the stem DOES occur (as inflected `가늰`) and the entry is restored, not deleted; the original discrepancy-flag text is preserved above it.

### 1.2 D3 — item 54 doubled verb ending — CONFIRMED, 11/11

Item 54 stem in all 11 P4 renderings: `한국시리즈 시작이 하루 ___.` P8 key `밀렸어요` in all 11 (codepoint-verified; the `밀렸어��` seen in one tool-output rendering is a display/transport artefact — U+FFFD = 0 in all joined SVG text). Reconstruction `한국시리즈 시작이 하루 밀렸어요.` is grammatical. `___어요` is absent everywhere. Same-class sweep: 77 fill stems/edition, 0 doubling flags post-fix (own `r3_sweeps.py`, blank-sentence identity byte-identical across all 11 editions).

### 1.3 D4 — item 103 wrong quotative particle — CONFIRMED, 11/11

Item 103 stem in all 11 P7 renderings: `미리 소금에 절인 배추를 ___라고 해요.` Key `절임배추` in all 11; reconstruction grammatical. Items 34 (`절정이라고`, 정 batchim ✓) and 101 (`김장이라고`, 장 batchim ✓) unchanged and correct. Same-class quotative sweep: exactly 3 quotative stems (34, 101, 103), all correct post-fix; item 112's hit is an extraction artefact (whole P7 column concatenated) whose `라고` follows vowel-final 요 ✓. All rendered prose quotatives in the core are correct: `'D-7'이라고` (adjudicated §3), `예보 날짜라고` (짜 vowel-final ✓), `김장이라고` (장 ✓), `'...?'라고` (요 ✓).

### 1.4 D1 survives (zh-tw only) — CONFIRMED

zh-tw `规` = 0, `規` = 2; core zh-cn retains `规` = 2 (expected). Own OpenCC s2t scan of the final zh-tw SVGs: exactly 2 distinct candidates — `峰` U+5CF0 ×8 (e.g. P1 `高峰`, standard Traditional form) and `准` U+51C6 ×1 (P8 `准考證`, standard Traditional term) — both adjudicated non-defects, same as Round 2. Zh-tw P6 gloss `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` intact.

## 2. Full key-letter verification — 150/150, no wrong key letter

Method: own extraction (`extract_exercises.py` → `exercises-all.json` + per-edition text dumps): 138 blocks/edition = 150 items (4 range blocks ×4: 25–28, 43–46, 61–64, 141–144); P8 answers 150/edition in all 11. Every key was verified semantically against the article text (core `.text.md`), the stem/grammar, and recomputed arithmetic/dates — not by p8.py set-equality alone. All 150 items in the core were read; P8 key-heads were cross-checked in all 11 editions' P8 renderings (byte-identical except the 137/138 translation re-aims and the item-150 pointer, as in Round 2).

### 2.1 Matching blocks (stem + options + key, quoted from P8 renderings)

**25–28 (P2, keyed 25=a, 26=c, 27=d, 28=b):**
- 25. 김장 — a. 겨울 김치를 담그는 일 ✓ (article: 겨울 김치를 담그는 일)
- 26. 새우젓 — c. 값이 오른 새우젓 (article: 1년 전보다 32.5% 올랐어요)
- 27. 소방의 날 — d. 11월 9일 (article: 11월 9일은 소방의 날, from 119)
- 28. 한능검 — b. 한국사 시험의 줄임말 (article: 한국사능력검정시험, 정기 접수 11월 10일 17시 마감)

**43–46 (P3, keyed 43=b, 44=a, 45=d, 46=c):**
- 43. 내장산 — b. 공단 예보 11월 11일 (국립공원공단 예보 11월 11일)
- 44. 월출산 — a. 산림청 예보 11월 9일 (산림청 예보 11월 9일)
- 45. 두륜산 — d. 산림청 예보 11월 11일 (산림청 예보 11월 11일)
- 46. 설악산 — c. 실제 관측 10월 16일 (실제 관측 절정 10월 16일)

**61–64 (P4, keyed 61=b, 62=d, 63=a, 64=c):**
- 61. 준플레이오프 — b. KIA가 LG를 3연승으로 이겼어요 (article: 3연승, 5-1/6-3/13-1)
- 62. 플레이오프 — d. 삼성이 KIA를 3승 2패로 이겼어요
- 63. 한국시리즈 — a. kt wiz와 삼성이 싸워요
- 64. 이동일 — c. 시리즈 사이에 하루가 필요해요

**141–144 (P8, keyed 141=b, 142=a, 143=d, 144=c):**
- 141. 절정 — b. 단풍이 가장 아름다운 때
- 142. 김장 — a. 겨울 김치를 담그는 일
- 143. 예보 — d. 미리 알린 날짜나 날씨
- 144. 관측 — c. 실제로 본 날짜나 날씨

Options in each block are unique and non-overlapping; no option fits two stems, no stem fits two options.

### 2.2 Cloze / fill / choice keys (spot-checked classes, all verified)

- **D-counts/dates (recomputed, Asia/Seoul):** Nov 9 = Mon = D-10, Nov 12 = Thu = D-7, Nov 15 = Sun = D-4, Nov 19 = Thu = D-day; 예비소집 Nov 18 Wed; 한능검 Nov 28 Sat; 정기 접수 마감 Nov 10 17시; 취소 좌석 11–13일. Items 1, 3, 4, 6, 7, 65–68, 83, 86, 97–99, 105–108, 113–115, 127, 128, 149 all consistent.
- **Numbers:** 배추 5,557원 (−10.3%), 새우젓 20,269원/kg (+32.5%) — items 11, 12, 21, 22, 118, 119; 수험생 551,864명 / 시험장 1,312곳 — items 75, 76, 91, 92, 121, 122; scores 3승 2패, 5-1/8-3/6-4/4-2/6-1, 5-1/6-3/13-1 — items 5, 10, 47–50, 52, 117, 126; 50% (산림청 잎) vs ~80% (기상청 산 전체) — items 88, 89, 110; 응시료 27,000원 / 50% 환불 기준 — item 23/24 context.
- **Grammar transforms:** items 57–60 past forms (이겼어요/열렸어요/밀렸어요/이겼어요) all correct; item 58's `1차전이 대구에서 열렸어요` is the playoff Game 1 (10월 26일 대구, KIA 5-1), so the section header's "all changed sentences are events in this paper" holds. Sentence-order 79–82, 133–136 correct (subject+time+object+verb; `에서` for place of action). Item 54/103 reconstructions grammatical (§1.2–1.3). Item 37 uniqueness (`농업인` only) holds.
- **Translations 137–140:** 137 `11월 12일은 D-7예요.` / 138 `김장이 한창이에요.` / 139 (native→Korean) / 140 (native→Korean) all correct; per-edition re-aims verified for 137/138 in all 11 P8 key lists (e.g. de `Der 12. November ist D-7.` / `Kimjang ist in vollem Gange.`; ru 137 full SVG text `137. 12 ноября — D-7. — См. стр. 1`).
- **Item 150 writing model:** 158 characters excluding the `예:` label (160 including the label, as measured on the joined model text) — matches the P8 pointer in all 11 editions.

### 2.3 Key-unchanged proof (independent)

Own script `r3_keyunchanged.py` ran `tools/p8.py extract --total 150` FRESH via the tools venv for every edition on the current P8 SVGs, then compared each full key dict + noted set against the pre-fix snapshot JSONs in `ko-fix-round3/pre-fix/p8keys/` by reading the JSON contents directly. Result: **keys identical in 11/11 editions, diff numbers [], extra [], noted sets identical**; key 54 = `밀렸어요`, key 103 = `절임배추` in all 11, before and after. The fix worker's disclosed truncated-print issue was resolved by direct inspection: each pre-fix JSON carries its own edition-specific `p8` path; the current extractions carry the corresponding absolute paths (relative-vs-absolute form only).

## 3. Adjudication: `'D-7'이라고` — ACCEPTABLE (not a defect; no fix required)

**Full context** (rendered core P1 text nodes, x=65, y=1068.8–1296.8; build source `content12.py:40`, read as text only): `수능 카운트다운도 계속돼요. 수능은 11월 19일 목요일이에요. 월요일 11월 9일에는 10일이 남아요. 목요일 11월 12일에는 7일이 남아요. 그래서 12일을 'D-7'이라고 해요. 시험 날의 특별한 조치는 11월 19일에만 적용돼요. 이번 주의 조치가 아니에요.` The usage occurs identically in all 11 editions (25 `D-7` text nodes per edition).

**Ruling:** ACCEPTABLE. The quotative particle follows the final pronounced sound of the quoted token. `D-7` is read with final element `7` — as Korean `칠` (batchim ㄹ), English `seven` (final /n/), or Korean `세븐` (batchim ㄴ). All plausible readings are consonant-final, so `이라고` is the correct form; no plausible reading ends vowel-finally (that would require stopping at `D`/디 and ignoring `-7`). The batchim rule therefore yields `이라고`, not `라고`. The fix worker's "rule not applicable" framing is imprecise, but the form itself is correct. Web searches for `"D-7이라고" 수능` and for the 이라고/라고 rule for foreign/alphanumeric tokens surfaced common `D-7` countdown usage and National Institute of Korean Language orthography principles, but no counter-example or authority stating `D-7라고`; the ruling rests on the phonological analysis above. If the coordinator disagrees, the only alternative form would be `'D-7'라고`, which this proofread rules incorrect.

## 4. Full re-gates on the final artifacts (run independently this round)

- **Freeze:** `tools/freeze.py baseline` — 8/8 SVGs byte-identical, exit 0; core integrity re-hash confirms shipped core unchanged. Freeze diffs: Latin/Cyrillic editions added CJK/Hangul = 0; ja total 2,664 (Round 2: 2,662; Hangul added 0); zh-tw total 904 (Round 2: 903; Hangul added 0); pt total 8 Hangul (어/울/요/에/났/서/만, 서×2 — the adjudicated quoted `서울에서 만났어요`, unchanged). Delta arithmetic verified char-by-char: ja delta vs Round 2 = `細` 1→2 AND `い` 37→38 — both from the restored gloss `細い` (the fix report's shorthand "+2 = restored 細" is imprecise; the exact delta is 細+1, い+1). zh-tw delta = `細` 1→2 only (+1, restored gloss `細`; the pre-existing 細 is the P8 key-69 note in both ja and zh-tw). No U+FFFD anywhere.
- **p8.py compare** (`--target ko`): CLEAN 150/150 in all 11; keydiff `[137, 138]` in all fan-outs except zh-tw `[]`; core extract 150/150. (Set equality only — semantic verification is §2.)
- **Canonical occlusion audit** (`tools/occlusion_audit.py`, selftest OK — all 6 planted classes fired exactly once, clean controls silent): **0 flags in all 11 editions, all 88 pages.**
- **Counts:** TOTAL 150, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 — identical in all 11 editions.
- **Kinsoku:** 0 in all 11. **P7 phrases:** all 8 KIT phrases verified verbatim contiguous excerpts in articles AND on P7, all editions (also visually confirmed on the core P7 card).
- **Reader-facing sweep:** hits only adjudicated false-positive substrings (`core` inside `coreano`/`Score`, French `encore`) — 0 genuine internal-production terms.
- **P6 table:** 12/12 cells per edition, table only (no bar chart). Cells: 구분 / 이번 주 (11월 9~15일) / 시험 날 (11월 19일) / 날짜 세기 / D-10 ~ D-4 / D-데이 / 분위기 / 카운트다운 / 시험 당일 / 특별 조치 / 없어요 (평상시) / 있어요 (10시 출근 등).
- **Masthead/badge/footer:** masthead y=262 in all 11; badge at y=394, 20pt, in all fan-outs except ja (badge in the subtitle slot, y=372) and the core (subtitle-slot form, per the O6 precedent); footers native-language with correct page numbering in all 11 (verified in `checks.json` badge_footer data and visually on P1/P8 cards).
- **PDFs:** all web PDFs are real PDF documents, 8 pages, ≤7 MB (2,243,389–2,661,599 bytes); `pdftotext` bytes 50,756–61,377 (>0), measured in Round 3 on the final web PDFs. **Caveat (non-blocking observation, see §7A):** the fix report's "web==print" equality could not be independently re-verified, because no print PDF ships in the edition folders — the non-web `Lucerna-VOL3*.pdf` file in each folder is a UTF-8 text dump byte-identical to that edition's web-PDF text layer (verified byte-identical for the core; byte sizes match exactly in all 11), not a PDF. The shipped web PDF fully satisfies the gate; the print-PDF figures in FIX-REPORT §7 (30.8–36.2 MB) refer to files not present in the edition folders.
- **ABSTRACT.txt:** all 11 single logical line, no ASCII double quote, reader-native, practice framing (e.g. zh-cn ends with the A2–B2 / 150-exercise framing; no news framing).
- **Native-language correctness / script residue:** gloss prefixes native per edition (译注/HINWEIS/Note/Nota/Uitleg/解説/Пояснение/譯注); Han distinct in Latin editions = only 一/十/土 (from Korean text: 十 in dates, 土 in 흙토); ja kana = 1,494 (native), ru Cyrillic = 8,370 (native), all others 0; FFFD = 0 everywhere.
- **Own koscan/orphan scan** (`koscan-round3.py`, tools/README standards: window 10–45px, same-column x within 30px, pure-Hangul fragments, source-word attestation via AST literal read of build sources, never imported/executed): TRUE_SPLITS=0, S3≥3=0, S3≤3=0, LINESTART=0 in all 11 editions. Candidates 357–362/edition. ORPHANshort 10–11/edition, same adjudicated set as Round 2 (complete words/labels); in en/fr/ja/pt the two P3 items `물`/`간식` sit 89px lower (y 1173.9/1225.9 → 1262.9/1314.9) — same words, same adjudication, consistent with restored-gloss reflow. No mid-word split anywhere.

## 5. Change isolation — CONFIRMED

Own script `r3_isolation.py` (hash + multiset diff vs the pre-fix snapshot `ko-fix-round3/pre-fix/`): **exactly 9 files changed per edition** — `svg/p3-munhwa.svg`, `svg/p4-seupocheu.svg`, `svg/p7-mal.svg`, `cards/p3-munhwa.png`, `cards/p4-seupocheu.png`, `cards/p7-mal.png`, print PDF, web PDF, `.text.md`. All other SVGs/cards byte-identical. SVG-text multiset diff: +51/−47 total across 11 editions; P1/P2/P5/P6/P8 identical in every edition; only P3 gloss wrap lines (restored entry + wrap reflow), the P4 item-54 stem line, and the P7 item-103 stem line changed. The non-`가늘` REMOVED/ADDED fragments are all wrap-reflow pieces of the gloss line. `.text.md` diffs: exactly 1 line per edition — the P3 gloss line. (An own-script parser bug in the first isolation run — single-space split of `sha256sum` output and the core section named `core` — was fixed before the rerun that produced this result.)

## 6. Cards viewed at full frame

- P1 ×11, P8 ×11, P3 ×11, P4 (core), P7 (core): all viewed at full frame. No overflow, overlap, missing glyphs/tofu, or missing image credits. P4 card shows item 54 stem `한국시리즈 시작이 하루 ___.`; P7 card shows item 103 stem `미리 소금에 절인 배추를 ___라고 해요.`; P3 cards show the restored gloss inside its box in all 11 editions; P1 cards show the badge visibly in the masthead (ja: subtitle slot) and the `'D-7'이라고` paragraph clean; P8 cards show all 150 answers legible with the item-150 model text present.

## 7. New / residual defects

**None.** No new defects and no residual defects were found in any completed check. Round 1 Observations O1–O8 were not re-raised.

## 7A. Non-blocking observation: print-PDF packaging (NOT a defect against the shipped editions)

In every edition folder the file named `Lucerna-VOL3*.pdf` (the non-web PDF) is not a PDF document: `file` reports "Unicode text, UTF-8 text", `pdftotext`/`pdfinfo` fail on it ("Couldn't find trailer dictionary"), and its bytes are identical to the `pdftotext` output of that edition's web PDF (byte-identical comparison for the core; sizes match the web pdftotext byte counts in all 11 editions: 50,756 / 53,316 / 52,452 / 54,064 / 54,155 / 53,507 / 53,821 / 53,178 / 53,675 / 61,396 / 50,903). No ~30 MB print PDF exists in any W46 edition folder (searched the whole goals tree; only VOL1/VOL2-era print PDFs were found). The file already existed pre-fix (pre-fix inventory hash differs, as expected: its text content changed with the three fixes), so this is a pre-existing pipeline packaging quirk, not a Round 3 regression, and it affects no reader-facing artifact — the shipped web PDF is a real, text-layered PDF in every edition. The fix report's FIX-REPORT §7 print-PDF sizes and its "web==print" claim therefore rest on files outside the edition folders and could not be re-verified here. Recommended follow-up for the coordinator (not a shipping blocker): either ship the real print PDFs in the edition folders or rename the text dump (e.g. `.txt`) so the `.pdf` extension does not mislead downstream checks. This observation does not change the PASS verdict: the edition scope in the task (8 SVGs + `*-web.pdf` + `.text.md` + `ABSTRACT.txt` + `WEEKLY-KIT.md`) is fully satisfied and verified.

## 8. Gate evidence saved

All under `hidden_files/w46/ko-proofread-gates-round3/`: `extract_exercises.py`, `round3-checks.py`, `koscan-round3.py`, `r3_fixverify.py`, `r3_keyunchanged.py`, `r3_isolation.py`, `r3_sweeps.py`, `zh_tw_simp_scan.py`; `counts/` + `exercises-all.json` + `exercises-<code>.txt` (+ `extract.log`, `extract2.log`); `checks.json`/`checks.log`; `fix-verification.json`/`fixverify.log`; `p8keys-now/*.json`, `key-unchanged.json`, `keyunchanged.log`; `gates/` (freeze baseline + 10 freeze diffs, occlusion selftest + 11 occlusion runs, p8 core + 10 p8 compares); `isolation.log`, `change-isolation.json`, `textmd-diffs.txt`; `koscan/koscan-round3.json`, `koscan.log`; `zh-tw-simp-scan.log`; `sweeps.log`; `pre-gate-hashes.txt`.
