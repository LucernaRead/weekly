# WEEKLY-KIT — Lucerna Korean Weekly VOL.3 · Korean × Traditional Chinese (2026-W46)

Pairing: Korean text, Traditional Chinese explanations. Edition slug: `2026-w46-ko-zh-tw`.
Week: Mon 9 Nov – Sun 15 Nov 2026 (weekStart 2026-11-09, weekEnd 2026-11-15).
VOL: VOL.3. Lead: 「김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날」.

Simplified and Traditional Chinese are INDEPENDENT editions, never converted from
one another. This edition was built natively in Traditional Chinese from the
frozen Korean core; 高考 and 泡菜 are kept unchanged per the W45 zh-tw precedent
(they are the established terms in this edition's usage).

## Build method

- Core text frozen from the W46 Korean core build
  (`hidden_files/weekly-report-w46-ko-build/`); only the explanation layer rewritten.
- Build dir: `hidden_files/weekly-report-w46-ko-zh-tw-build/` — copied from the
  W45 ko-zh-tw build (`.py` + `assets/` only), content files overwritten with the
  frozen W46 core content, zh-tw `bslib4.py`/`svglib.py` kept (furniture,
  `譯注｜` gloss prefix).
- Transform: filtered W45 operations (harvested MAP + STRUCT, longest-first,
  combined-text) applied first, then `supp_zh_tw.py` (GEOM majority form + SUPP
  map converting Simplified explanation strings to Traditional; entries whose
  Traditional form is identical to Simplified omitted).
- Factory note: `supp_apply.py` was fixed during this build so `zh-tw` loads
  `supp_zh_tw.py` (`lang.replace('-', '_')`); previously it raised
  `ModuleNotFoundError: No module named 'supp_zh-tw'` and applied nothing.
- P1 geometry: majority form — 20pt BRICK badge at y=394, subtitle shifted to 366,
  rules 412/421, dark band 433. Badge:
  `韓語正文 · 繁體中文講解 — 給繁體中文讀者的版本`.
  Footer: `Lucerna · 韓語週報 VOL.3 · 正文韓語 · 講解繁體中文` / `第 N 版 / 共 8 版`.
  Strapline second segment: `每週一期`.
- Right-band line 1 `醃泡菜`; line 2: `醃泡菜季正忙 · 高考剩一週`.
- No phrases-pitch change (124 kept; teaser fit after the `lcn2` fix below).
- Letters: Korean `lko` kept; `lcn` = `編輯部範例信，非真實來信。`;
  `lcn2` = `鄭重說明：截稿前未收到真實來信與 8 版優秀作文，仍刊示例，順延至 VOL.4。`
  (37 chars, 2 lines) — editor's example + disclosure, promise carried to VOL.4.
  No real letters arrived; nothing fabricated.
- E-zone (P8): answer keys 137/138 coincide with the core's (shared characters);
  only the 對照/对照 cross-reference notes differ, as expected — hence
  `p8.py` keydiff=[] (see Gates).
- CSAT term: 高考 (W45 zh-tw precedent, kept). Korean `D-` notation kept.

## Contents / counts

8 pages, 150 exercises (registry count): A2 51 / B1 72 / B2 27;
pages 10/18/18/18/18/18/12/38. P8 writing model 158 chars (spaces removed),
inside the printed 150–200자 instruction. P7 golden sentences 8/8 verbatim
from this issue's own articles (whitespace-insensitive, checked against SVGs).

## Gates (2026-11-02)

- `run.py`: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE; P7 teaser ends 2518.7 (<2540).
- `occlusion_audit.py`: selftest OK; final 0 flags.
- `p8.py compare` (core vs zh-tw): CLEAN, missing=[] extra_count=0, keydiff=[]
  (answer keys coincide; only the 對照/对照 notes differ — expected, see above).
  Extract 150/150.
- `freeze.py diff`: 903 added CJK chars, ALL Traditional forms, ZERO Hangul —
  adjudicated legitimate Traditional Chinese reader notes (strict-CJK-scope
  lesson: judge by the per-char Hangul list, not the raw count).
- `check_edition.py`: phrases 8/8; orphan scan 2 hits, both adjudicated —
  P4 PAREN-FRAG `신문에 나온 일이에요.)` (byte-identical to the core's hit) and
  P3 SHORT-TAIL `주세요.` at y=1416.8 (the same frozen Korean instruction
  `한국어로 두 문장 써서 보내주세요.` wraps the same way in the core P3 SVG at
  y=1396.6; the tail is the 3-syllable polite ending). Kinsoku line-starts 0.
- Letters-box audit (manual): disclosure inside its box, margin +8px.
- Visual: P1 + P7 cards read — majority badge form, Traditional text throughout,
  letters box, teaser clean. Simplified-character heuristic scan after SUPP: 0 hits.
- Full CJK scan after SUPP: only Traditional Chinese + Korean (adjudicated by
  the freeze diff above).

## Fixes during this build

1. P7 teaser overflow (2547.7, over by 7.7): shortened `lcn2` to the 37-char
   Traditional form above in `content7.py` + `supp_zh_tw.py` → teaser 2518.7.
   (The same wording was later used for the core's own `lcn2` fix.)

## Outputs

- `svg/` (8), `cards/` (8)
- Print: `Lucerna-VOL3-ZHTW.pdf` — 32,054,364 bytes,
  SHA-256 `0a3157ed58b14d12480ed6a37c25cf39ef587c96d85259cdc735dabed6b2b828`
- Web: `Lucerna-VOL3-ZHTW-web.pdf` (via `tools/webpdf.py`) — 2,654,715 bytes (<7 MB),
  pdftotext 50,912 bytes, phrase 「김장이 한창이에요」 found 7 times, consistent
  with print text. SHA-256 `55268140de26a51f42ddacf0203f183a5b57ece379607a035ea364f4128ce0ab`
- `ABSTRACT.txt` (Traditional Chinese, single line, no ASCII double quotes)
- `2026-w46-ko-zh-tw.text.md` — 340 items, 8 pages, exported from the source
  manuscript via `textmd.py` (never from PDF); answer keys/notes excluded. (340 vs
  the core's 338: the +2 are P1 furniture strings — badge + dark-band lines —
  replacing the core's single Chinese band line; all other pages match 1:1.)

## Debts / open items

- Korean Series G1–G5 results unknown at the 2 Nov 2026 press time; G6/G7
  (10–11 Nov) conditional. No observed foliage peak for Naejangsan/Wolchulsan at
  press time (forecasts only, attributed by agency). HanNeungGeom details from
  secondaries citing the 19 Oct 2026 notice; cancelled-seat start time conflicts
  across secondaries (dates only printed). No independent reproof round run.
- Image shortfall (carried from W45): no verified PD/CC0 kimjang-making or Korean
  foliage photo; only the verified W45 file set reused with honest captions.
- W45 teaser honoured in full (kimjang / CSAT D-7 / HanNeungGeom / playoffs +
  Korean Series / letters + best P8 writing). VOL.4 teaser printed on P7.

## Fix record — Round 1 proofreader verdict (fix worker, 2026-11-03)

Source-only fixes for the independent proofreader's Round 1 defects (verdict: `hidden_files/w46/ko-proofread-gates/proofreader-verdict-round1.md`); full re-render from source, no hand-edited SVG/PDF. Observations O1–O8 untouched. A Round 2 independent proofread follows; re-gating does not replace it.

- D2 (BLOCKING, frozen core, all 11 editions): P3 gloss line under the "당신은?" prompt. The `가늘다` entry was DELETED from the gloss line in `content34.py` (and mirrored in the `supp_*.py` record pair; core `check_core.py` hand list updated the same way). Before: `겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。` After: `겹치다 重疊 · 감사하다 感謝 · 나누다 區分、分享。` Post-fix verification: `가늘` occurs 0 times in all 8 SVGs and in `2026-w46-ko-zh-tw.text.md` of every edition; remaining gloss entries intact and correctly punctuated; P3 visually checked at full frame in all 11 editions (shortened gloss inside its box, no overflow/overlap). SVG hash comparison vs the pre-fix inventory: only `p3-munhwa.svg` changed in this edition (zh-tw: P3 + P6).
- D1 (zh-tw only, BLOCKING): P6 gloss line, single character. Before: `譯注｜재다 衡量 · 규모 规模 · 섞다 混淆。` After: `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` (`规` U+89C4 → `規` U+898F, in `weekly-report-w46-ko-zh-tw-build/content56.py:125`; record entry added to `supp_zh_tw.py`). Post-fix expanded Simplified-only scan (OpenCC s2t over all CJK chars in zh-tw SVG text): only 2 candidates remain — `准` U+51C6 ×1 (P8 `准考證`, standard Traditional term) and `峰` U+5CF0 ×8 (identical in both scripts); `规` = 0. Changed SVGs vs pre-fix inventory: P3 + P6 only.

- ⚠️ DISCREPANCY FLAG for the coordinator / Round 2 proofreader (do not treat the D2 deletion as proof the stem never occurs): pre-fix verification found the attributive inflection `가늰` (가 U+AC00 + 늰 U+B2B0; `'가늘' in '가늰'` is False at codepoint level) 3× per edition — P3 body `길고 가늰 과자를 친구와 나누는` and P5 ×2 (body + exercise stem) — which the verdict's stem list (가는, 가늘게, 가느다란, 얇) did not cover. The prescribed deletion was applied exactly as ordered; post-fix `가늰` remains 3× per edition. Adjudication of keep-vs-restore belongs to Round 2.

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 903 (ja 2,662 vs Round 1's 2,664 — the −2 is the deleted gloss entry leaving the core multiset: 3 Hangul syllables + 细; pt +8 Hangul = the adjudicated quoted sentence; zh-tw 903 unchanged: P6 `規` +1, P3 `細` −1).
- p8.py: CLEAN 150/150, keydiff []. Occlusion audit: 0 flags, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 (identical to Round 1). Kinsoku: 0. Koscan reconstruction: CANDIDATES=311 TRUE_SPLITS=0 S3=0 (reconstruction script preserved at `hidden_files/w46/ko-fix/koscan_reconstruct.py`; the Round 1 koscan script itself was not preserved, only its logs).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-ZHTW-web.pdf` 2654260 bytes (< 7 MB), 8 pages, pdftotext 50895 bytes. `Lucerna-VOL3-ZHTW.pdf` 32053910 bytes, 8 pages. `2026-w46-ko-zh-tw.text.md` regenerated from the source manuscript via `textmd.py` (headers byte-identical to pre-fix, 340 items, 27513 bytes; diff vs pre-fix export is only the fixed gloss line(s)).

## Fix record — Round 3 (2026-11-03; Round 2 verdict FAIL — three frozen-core defects)

Round 2 proofreader verdict (2026-11-03): all 11 editions FAIL on three blocking frozen-core defects; D1 confirmed; keys 150/150 confirmed; gates clean. Round 3 fixed ONLY the three defects below, at the build sources (no SVG/PDF patches), full re-render of all 11 editions. D1 was NOT disturbed. No other family touched. Nothing pushed/inserted/posted. Full report: `hidden_files/w46/ko-fix-round3/FIX-REPORT.md`.

- R-GLOSS — RESTORE the `가늘다` gloss entry in the P3 gloss line, exactly as pre-fix (reverses the Round 1 D2 deletion, whose "occurs nowhere" premise Round 2 refuted: `가늰` occurs 3× per edition — P3 body, P5 body, P5 exercise 69 option A, key 69 = A — and `가늘다 → 가늰` is a ㄹ-irregular attributive). Restored in `content34.py`, both sides of the `supp_*.py` record pair, and the core `check_core.py` hand list.
  - Before (Round 1 form): `譯注｜겹치다 重疊 · 감사하다 感謝 · 나누다 區分、分享。`
  - After (restored, verified verbatim from the rendered P3 SVG gloss band): `譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。`
  - This resolves the Round 1 discrepancy flag in this KIT: the stem DOES occur (as inflected `가늰`); the entry is restored, not deleted.
- D3 — item 54 (P4), stem fix at the core source, key UNCHANGED (`밀렸어요`).
  - Before: `한국시리즈 시작이 하루 ___어요.` → reconstructed `하루 밀렸어요어요` (doubled ending).
  - After: `한국시리즈 시작이 하루 ___.` → reconstructed `한국시리즈 시작이 하루 밀렸어요.` (verified in all 11 renderings).
- D4 — item 103 (P7), stem fix at the core source, key UNCHANGED (`절임배추`).
  - Before: `미리 소금에 절인 배추를 ___이라고 해요.` (ungrammatical: `배추` is vowel-final, quotative must be `라고`).
  - After: `미리 소금에 절인 배추를 ___라고 해요.` → reconstructed `미리 소금에 절인 배추를 절임배추라고 해요.` (verified in all 11 renderings; contrast item 101 `김장이라고`, batchim-final, unchanged).
- Same-class sweep (AST text-read of the build sources, `sweep.py`): all 77 fill-in stems scanned for stem+key doubling — exactly 1 candidate (item 54); all quotative `이라고/라고` usages scanned for final-syllable mismatch — exactly 1 mismatch (item 103) among 3 quotative stems, plus 4 correct prose usages and 1 non-applicable (`'D-7'이라고`, non-Hangul token) reported unscanned-as-defect for Round 3 adjudication. No further candidates; nothing else fixed.
- Keys UNCHANGED: p8.py compare CLEAN 150/150, keydiff []; per-edition key-extraction JSONs byte-identical pre-fix vs post-fix (all 150 keys, noted sets identical; keys 54 `밀렸어요` and 103 `절임배추` unchanged everywhere).

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix-round3/gates/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 904 (Round 2: 903; +1 = restored 細, Hangul added 0). No U+FFFD.
- p8.py: CLEAN 150/150, keydiff []. Occlusion audit: 0 flags in all 88 pages, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38. Kinsoku: 0. Koscan reconstruction: CANDIDATES=361 TRUE_SPLITS=0 S3=0 (script preserved at `hidden_files/w46/ko-fix-round3/koscan-round3.py`).
- P3 gloss-box geometry: gloss lines inside their box (top margin 38.5, bottom margin 47.725); occlusion 0. Visual: P3 full frame checked (restored gloss inside its box, no overflow); P4 item 54 / P7 item 103 checked at full frame in the core + spot checks (de P4, ja P7).
- D1 survives: `规` = 0 in this edition; expanded OpenCC s2t Simplified-only scan re-run on the final SVGs returns exactly the 2 adjudicated non-defects (`峰` U+5CF0 ×8, `准` U+51C6 ×1). P6 gloss `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` intact.
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-ZHTW-web.pdf` 2654630 bytes (< 7 MB), 8 pages, pdftotext 50903 bytes. `Lucerna-VOL3-ZHTW.pdf` 32054373 bytes, 8 pages, pdftotext 50903 bytes. `2026-w46-ko-zh-tw.text.md` regenerated via `textmd.py` (headers byte-identical to pre-fix, 340 items, 27530 bytes; diff vs pre-fix export is only the restored P3 gloss line).
- Change isolation: hash diff vs the pre-fix snapshot — exactly 9 files changed in this edition (svg/p3, svg/p4, svg/p7, cards p3/p4/p7, print PDF, web PDF, `.text.md`); SVG-text multiset diff — the ONLY string changes are the three fixes (P3 gloss wrap lines, P4 item-54 stem, P7 item-103 stem). No other string changed anywhere.
