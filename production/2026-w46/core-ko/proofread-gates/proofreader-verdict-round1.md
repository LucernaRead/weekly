# Independent Proofread Verdict — Round 1
# Lucerna Weekly W46 · KO target · VOL.3 · 2026-11-09 – 2026-11-15

Proofreader: independent subagent (did not build these editions). Proofread run 2026-11-03 (Asia/Toronto dates per task clock; all re-runs independent of builder gates).
Gate artefacts: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-proofread-gates/`
(see "Gate outputs" below). No edition file was edited, re-rendered, pushed, or inserted. No live-browser work was available to this proofreader; external fact claims are adjudicated as UNVERIFIABLE where noted.

## Verdict summary

| Edition (slug) | Dir | Verdict |
|---|---|---|
| 2026-w46-ko-zh-cn | `weekly-report-w46-ko-core` (core IS the zh-cn edition) | **FAIL** — D2 |
| 2026-w46-ko-de | `weekly-report-w46-ko-de` | **FAIL** — D2 |
| 2026-w46-ko-en | `weekly-report-w46-ko-en` | **FAIL** — D2 |
| 2026-w46-ko-es | `weekly-report-w46-ko-es` | **FAIL** — D2 |
| 2026-w46-ko-fr | `weekly-report-w46-ko-fr` | **FAIL** — D2 |
| 2026-w46-ko-it | `weekly-report-w46-ko-it` | **FAIL** — D2 |
| 2026-w46-ko-ja | `weekly-report-w46-ko-ja` | **FAIL** — D2 |
| 2026-w46-ko-nl | `weekly-report-w46-ko-nl` | **FAIL** — D2 |
| 2026-w46-ko-pt | `weekly-report-w46-ko-pt` | **FAIL** — D2 |
| 2026-w46-ko-ru | `weekly-report-w46-ko-ru` | **FAIL** — D2 |
| 2026-w46-ko-zh-tw | `weekly-report-w46-ko-zh-tw` | **FAIL** — D1 + D2 |

## Defect list

### Frozen-core defects (present in all 11 editions via the frozen core)

**D2 — BLOCKING (minor severity). P3 gloss headword with no occurrence in the issue: 가늘다.**
- Location: P3 (`p3-munhwa.svg`), gloss box under the "당신은?" prompt, all 11 editions.
- Wrong text (core, verbatim): `译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。`
  (zh-tw form: `譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。`; de form verified: `가늘다 = dünn · 감사하다 = danken · 나누다 …`.)
- Evidence: full-text search of all 8 core SVGs for `가늘` returns exactly one hit — the gloss line itself. All inflected/related stems return 0 in every page: `가는`, `가늘게`, `가느다란`, `얇`. The body text describes garaetteok as `길고 하얘요` (P5), never 가늘다. Neighbouring headwords in the same gloss line DO occur on P3 (겹치다 via `겹쳐/겹치는`, 감사하다 via `감사`, 나누다 via `나누/나눠`; 막히다 in the adjacent gloss line via `막힐 수 있어요`), so this is a single orphan, not a systemic gloss failure.
- Correct text / fix (coordinator's choice): either delete `가늘다 细 · ` (and equivalents) from the P3 gloss line in all 11 editions, or add the word to P3 body text. Recommended: delete — one-line change, no reflow risk.
- This refutes the completeness of the KIT gloss-occurrence adjudication (the "14 dictionary/inflected pairs" note) insofar as it implied every glossed headword occurs in the issue.

### Edition-specific defects

**D1 — BLOCKING (minor severity; single character). `2026-w46-ko-zh-tw`, P6 gloss line: Simplified-form character 规.**
- Location: `weekly-report-w46-ko-zh-tw/svg/p6-gipi.svg`, gloss line.
- Wrong text (verbatim): `譯注｜재다 衡量 · 규모 规模 · 섞다 混淆。`
- Correct text: `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` (规 U+89C4 → 規 U+898F in `規模`).
- Evidence: expanded Simplified-only character scan over the zh-tw SVGs returned this as the sole genuine hit (all other hits — 正/找/把/所/止/模/峰 — are identical in both scripts). The same word WAS correctly converted elsewhere in the same edition: core P8 key 96 appears in zh-tw as `96. 규모 — 大數字顯示全國規模`, proving the P6 gloss was missed. The freeze diff (903 added CJK, 0 Hangul) cannot catch it because the character is already present in the core's Simplified gloss.
- This REFUTES the zh-tw KIT claim "Simplified-character heuristic scan after SUPP: 0 hits".
- Fix: replace 规 with 規 in that one gloss line.

No other defects were found. In particular: no occlusion flags, no P8 set/key errors, no count errors, no mid-word Hangul splits, no kinsoku violations, no reader-facing internal language, no badge/footer errors, no PDF/text-layer failures, no image-credit omissions, no W45-promise misses.

## Observations (non-blocking; recorded for the coordinator)

- **O1 — Exercise-instruction language divergence.** en/fr/ja/zh-tw retain Korean exercise-instruction sentences (frozen core; e.g. en P2 `빈칸에 알맞은 말을 넣으세요.` under Korean section titles, with a native-language type label beside every item); de/es/it/nl/pt/ru translated them (documented in KITs as a deliberate W46 deviation from W45). This matches the shipped W45 ko-en precedent (verified in W45 ko-en P2), so it is NOT a defect. Consequence: en/fr KIT claims that the "explanation layer [is] entirely in English/French" are overstated in this respect. ru P8 writing header lines (`쓰기 문제예요 (정답은 하나가 아니에요). 아래에 / 158자의 예가 있어요.`, ru P8 y=239.5/269.225) remain Korean while ru translated all other instructions — within-edition inconsistency, observation only; stem + Russian label `Письмо` convey the task. All editions uniformly keep the frozen P1 subtitle and P8 running head in Korean (furniture, not defects).
- **O2 — pt quoted Hangul legitimate.** pt adds exactly 8 Hangul chars, P7 only: `서울에서 만났어요`, quoted in the error-clinic note (W45 precedent cited in KIT). Confirmed by canonical freeze diff.
- **O3 — ja P8 key 62 spacing.** `62. d — 플레이오프 = サムスン3–2 d` prints spaces around `=`; cosmetic only; P8 extract still 150/150.
- **O4 — fr/en "Jimin"/"Korean"/"encore"/"score" tokens cleared.** fr `encore` is the French word; `Korean Series`/`Jimin` are proper-name/transliteration usage in French/English explanations and keys. No untranslated-English residue. Ru P8 keys use Latin `Samsung` (brand name; `KIA` is Latin everywhere) — acceptable; no `Самсунг` transliteration anywhere, not treated as a defect.
- **O5 — zh-tw KIT coordinate inaccuracy (not an edition defect).** The zh-tw KIT describes the P3 orphan tail `주세요.` as "same coordinates as core y=1396.6"; measured zh-tw y=1416.79 (+20.15px, same frozen wrap, shifted box flow). The KIT's non-defect adjudication of the tail itself stands.
- **O6 — Core/zh-cn has no discrete badge LINE** (only the Korean subtitle at y=372 + footer `韩语周报` pairing label). This matches the shipped W45 core exactly (verified: W45 ko-core P1 has the same masthead form, no badge line) — established core convention, not a regression. All 10 fan-outs carry an explicit badge line.
- **O7 — "���" glyphs seen in tool output are transport/display artefacts, not file defects.** Byte/codepoint dumps verified correct codepoints; zero U+FFFD bytes in all 88 SVGs.
- **O8 — Image-credit English** (`Bain News Service — Public domain (Wikimedia Commons)`, artist names) inside Korean `사진:`/`그림:` captions is uniform across all editions including core — source attribution by design, not wrong-language residue.

## KIT-claim adjudication (summary)

CONFIRMED (re-run independently): freeze baseline 8/8 SVGs byte-identical; canonical per-char freeze diffs (de/en/es/fr/it/nl/ru 0 added CJK, 0 Hangul; ja 2,664 added CJK / 0 Hangul; zh-tw 903 added CJK / 0 Hangul; pt 8 added Hangul, P7 only); removed-Hangul strings all explanation-layer, no article-body sentence removed; Hanja residue only 土/十/一 (P3 Hanja paragraph) in Latin/Cyrillic editions; 0 kana outside ja; 0 Cyrillic outside ru; P8 CLEAN 150/150 all editions with keydiff [137,138] except zh-tw []; occlusion 0 flags all 88 pages (selftest: all 6 classes fire, clean controls silent); counts TOTAL 150, A2 51 / B1 72 / B2 27, pages 10/18/18/18/18/18/12/38 in all editions (matching-range headers 25–28/43–46/61–64/141–144 resolved); all 8 P7 Korean phrases verbatim contiguous excerpts on their tagged pages and on P7, all editions; kinsoku 0; koscan TRUE_SPLITS=0, S3=0 all editions; reader-facing sweep 0 genuine internal-production terms; badge forms/colours measured (majority #a4553a 20pt BRICK y=394; en #3e4c2a 17pt olive; ja #a4553a 19.5pt subtitle-slot y=372); footer labels on all 8 pages, correct page numbers, all editions; letters-box disclosures inside boxes (baseline margins 13.7–101.2px, measured per edition); P7 teaser ends <2540 in all editions (2470.7–2528.7); masthead rendered-pixel check — `Lucerna` ink x 716–1230 (orig), centred, clear of frame, all editions; P6 comparison table identical 12 Korean cells in all editions (no bar chart on P6 — table only); P1 numbers strip 10/7/3/17/5,557 present; image credits complete (lumoplank, wizdata, Udonhan1992, Cézanne, Bain, Gary Todd — all PD/CC0 with honest file-photo labelling; zh-tw P3 credit wraps `자료`/`사진` across two lines, text complete); web PDFs — all 8 pages, <7 MB, text layer 50,765–61,405 bytes, sizes/SHAs match KIT claims exactly; ABSTRACT.txt all single-line, no ASCII double-quote, reader-native, practice framing, masthead + target + A2–B2 + 150 present; text.md exports — slugs correct in all 11, 8 page heads, line counts match KIT (695/697/699 via wc -l; non-empty lines 348/349/350 = KIT "items" 338/339/340 + 10 header lines); W45 promises honoured — all five teaser items (kimjang incl. 5,557/20,269 prices + Seoul discount Nov 5–11; CSAT D-10/D-7/D-4 with Thu Nov 12; HanNeungGeom registration closes Nov 10 17:00 + cancelled-seat registration Nov 11–13 + 27,000-won fee + Nov 28 exam; verified playoff result Samsung 3–2 over KIA + announced/shifted Korean Series schedule with press-time distinction taught on P6; readers'-corner carry with disclosure + VOL.4 promise) and the VOL.4 teaser (CSAT day Nov 18–19, HanNeungGeom prep, Nov 22 Kimchi Day, letters + best P8 writing); P8 answer-key spot-check (16 keys incl. E-zone 137–140 and matching 141–144) all correct vs articles/stems/tables; P8 writing model 158 chars within the printed 150–200자 instruction; date/weekday arithmetic verified (`date -d`, Asia/Seoul: Nov 9 Mon, 12 Thu, 15 Sun, 18 Wed, 19 Thu, 22 Sun, 28 Sat; D-10/D-7/D-4 correct); gloss occurrence spot-check passed except D2; P4 parenthesised-clause orphan tail adjudicated non-defect (complete clause; absent in de/es/it/nl/pt/ru where the instruction was translated); P3 `주세요.` tail adjudicated non-defect.

REFUTED: zh-tw KIT "Simplified-character heuristic scan: 0 hits" (D1); zh-tw KIT P3 tail coordinate claim (O5); en/fr KIT "explanation layer entirely in [native language]" as an absolute (O1); KIT gloss-occurrence adjudication completeness (D2).

UNVERIFIABLE (no live-browser access available to this proofreader; internally consistent, no contradiction found): external factual claims behind the articles — KAMIS prices and the −10.3%/+32.5% changes (prior-year values not printed, arithmetic not re-derivable), playoff game scores/dates, 551,864 candidates / 1,312 sites, 27,000-won fee. Print-PDF SHAs not re-verified beyond KIT claims (web PDFs verified exactly).

## Gate outputs (all under `hidden_files/w46/ko-proofread-gates/`)

`inventories.json`, `freeze-rederive.json` (superseded by canonical per-char `freeze-*.json` + `.log` — string-level re-derivation was wrap-churn and is discarded), `freeze-baseline` + `.log`, `exercise-counts.json` + `exercise-counts-v2.json`, `badge-footer.json`, `p8-*.json` + `.log` (+ `p8-core.json`), `occlusion-*.json` + `.log` + `occlusion-selftest.log`, `koscan-*.log`, `p7-phrases.json`, `kinsoku.json`, `reader-facing-sweep.json`, `p6-table.json`, `letters-box-dump.json`, `letters-box-measured.json`, `masthead-pixels.json`, `masthead-renders/` (11 inspection-only P1 PNG renders, gates dir only), `defect-evidence.json`, `proof-gates-part1.py`, `proof-gates-part2.py`, this verdict file.

Cards viewed at full frame: P1 + P8 of all 11 editions (22 cards) + spot checks P3, P6 (core). No overflow, overlap, missing glyphs/tofu, or missing image credits found on any viewed card.

## Seed record (for the coordinator's insert step)

- Target VOL number: **VOL.3** (all 11 editions; masthead/footer furniture confirms).
- Re-measured exercise total + level split (2026-11-03, identical in all editions): **TOTAL 150; A2 51 / B1 72 / B2 27**; per-page **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**.
- Core P1 article opening 2–3 sentences verbatim (target language Korean; P1 lead article, deck line `목요일 11월 12일은 수능까지 딱 일주일 남는 날이에요` precedes it; lead headline: `김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날`):
  > 11월 9일 월요일부터 15일 일요일까지, 이번 주는 김장이 한창인 주간이에요. 배추 값은 내렸는데 새우젓 값은 올랐어요. 장을 볼 때는 가격을 하나하나 확인하는 것이 좋아요。

## Required fixes before shipping (Round 2 re-verification scope)

1. D2: remove `가늘다` (and its gloss) from the P3 gloss line in all 11 editions, or add the word to P3 body text. Re-verify by re-running the gloss-occurrence check.
2. D1: replace 规 with 規 in the zh-tw P6 gloss line (`규모` → `規模`). Re-verify by re-running the Simplified-only scan (expect 0 genuine hits).

If the coordinator rules D2 cosmetic/non-blocking, only `2026-w46-ko-zh-tw` remains blocked (D1). Under the proofread-until-zero gate as written, both defects block.

ROUND 1 FAIL
