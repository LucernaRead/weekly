# Lucerna Weekly — W46 Korean × English edition (KO×EN, VOL.3) — WEEKLY KIT

- Issue week: Mon Nov 9 – Sun Nov 15, 2026. Issue dated Mon Nov 9, 2026. VOL.3.
- Pairing: target Korean × reader-native English. Masthead takes NO article (Korean). Pairing badge on P1 masthead (W43/W45 ko-en measured instance: subtitle 372→366, badge inserted y=394, 17pt bold olive) + every page footer (full names: "Lucerna · KOREAN WEEKLY VOL.3 · Korean text · English explanations" / "Page N of 8"). Gloss prefix "Note — ".
- Target-language text frozen from the W46 core; explanation layer entirely in English. Korean text (articles, exercises, P7 phrases, teaser, example letter) is byte-identical to the core except the P8 E-zone re-aiming below. No Chinese explanation strings remain in the build sources (verified by CJK-literal scan: only the adjudicated Hanja paragraph on P3, which is Korean article text explaining the character 土).
- Build dir: `hidden_files/weekly-report-w46-ko-en-build/` (W45 ko-en build copied: bslib4.py/svglib.py/run.py/render.py + assets; content files overwritten with the frozen W46 core; `transform-w45.py` reference; `supp_en.py` = GEOM + letters rebuild + SUPP map). Edition dir: `files/weekly-report-w46-ko-en/` (svg/, cards/, Lucerna-VOL3-EN.pdf, Lucerna-VOL3-EN-web.pdf, this KIT, ABSTRACT.txt, 2026-w46-ko-en.text.md).
- Transform method (tools README #17/#18): whole-line / exact-literal replacements only, each asserted present (or already-applied, idempotent); no AST byte offsets; no repr literals. Filtered W45 ko-en REPS (137 applied, 142 skipped as W45-only) + SUPP map for W46-new strings + fresh GEOM with W46 headline/deck lines + letters rebuild per the W45 en precedent (single English disclosure; Korean disclosure lines dropped; lh formula rebuilt for 2 blocks).
- P8 E-zone re-aimed KO↔EN per the W45 ko-en precedent: items 137/138 keys become English ("Nov 12 is D-7.", "Kimchi season is in full swing."); items 139/140 stems become English, keys stay Korean. Hence p8.py compare keydiff=[137, 138] (expected, adjudicated).
- P7 readers' corner: editor's example letter frozen verbatim (Korean); single English disclosure stating the example is not a real letter, no real reader letters or best P8 writing had arrived by press time, the example stands, last issue's promise carries to VOL.4, plus an explicit solicitation for letters and P8 writing. No fabricated readers/letters/names/quotes.
- P7 phrases of the week: the 8 Korean phrases are verbatim from this issue's articles (verified 8/8 whitespace-insensitive); English translations are new for W46 topics.

## Measured exercise counts (final build)

- TOTAL 150. By page: 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38. By level: A2 51 / B1 72 / B2 27. By type: fill-in 48, multiple choice 52, matching 16, cloze 13, sentence building 8, transformation 4, true/false 4, translation 4, writing 1 (type labels in English, per the W45 ko-en precedent).
- P7 teaser ends y=2483.7 (inside the 2540 content limit). Zero FLOW OVERFLOW / HEAD TOO WIDE warnings.

## Gates

- Self-proofread: all 8 cards read visually (P1 spot-checked; P7 letters box re-checked after rebuild); gloss occurrence inherited from the core (same Korean prose; gloss headwords unchanged); P7 phrases 8/8 verbatim; dates/arithmetic inherited from the core (frozen).
- Occlusion audit: selftest OK (6 planted classes fire, clean controls silent); final **0 flags** (incl. LINEX + same-baseline furniture scan + chart GRAZE element-check).
- p8.py compare vs core: **CLEAN**, missing=[] extra_count=0, keydiff=[137, 138] (E-zone re-aiming, expected).
- p8.py extract: noted set 150/150.
- freeze.py diff vs core: 0 added CJK characters on every page (P1–P8); Korean text frozen (added/removed string counts reflect explanation-layer translation only).
- ×KO orphan scan (window 10–45, ≥3-syllable tail, parenthesised fragments, line-start orphan punctuation): 1 hit — the P4 parenthesised clause tail 「신문에 나온 일이에요.)」, adjudicated non-defect (complete clause, same as the core). Kinsoku line-starts: 0.
- Web PDF via tools/webpdf.py: Lucerna-VOL3-EN-web.pdf, 2,292,768 bytes (< 7 MB), pdftotext 52,461 bytes, 8 pages, consistent with the print PDF. Exactly one `*web*.pdf` in the edition dir.

## Output files + sizes (final render)

- `svg/` — 8 SVGs. `cards/` — 8 page PNGs.
- `Lucerna-VOL3-EN.pdf` — print PDF, 32,290,739 bytes. SHA-256: `9fa379f4d052ca0f6268f0d0808d8858c6b6e717e87cd9bed8647d269b86be02`.
- `Lucerna-VOL3-EN-web.pdf` — web PDF, 2,292,768 bytes. SHA-256: `da208304f40724f6f0beb8db7576287020ab092e9dea71cbf5c2362463b08773`.
- `ABSTRACT.txt` — one line, English, no ASCII double quotes.
- `2026-w46-ko-en.text.md` — 338 items, 8 pages, exported from the source manuscript via `textmd.py` (answer keys/notes excluded; no PDF/SVG extraction).

## Fixes log (this edition)

- W45-op partial translations found by the full CJK scan and normalised: D-zone note "Use 「에서」 for the place of an action" → "Use 에서 for the place of an action"; G-zone note already "Kimjang = making kimchi for winter" (kept); match note "설악산 = actual observation Oct 16 c" (kept); clinic note "준플레이오프 = KIA won three straight b" (kept). No Korean text touched.
- GEOM: fresh W46 lines (headline/deck/right-side texts); right-side gold line "Kimchi season in full swing · One week to the CSAT" (W45 en precedent length class).

## Open verification debts

- Inherited from the core KIT (Korean Series G1–G5 unknown at Nov 2 press time; no observed Naejangsan/Wolchulsan peak; HanNeungGeom secondaries caveat; image shortfall). No independent reproof round has been run on this edition.

## Fix record — Round 1 proofreader verdict (fix worker, 2026-11-03)

Source-only fixes for the independent proofreader's Round 1 defects (verdict: `hidden_files/w46/ko-proofread-gates/proofreader-verdict-round1.md`); full re-render from source, no hand-edited SVG/PDF. Observations O1–O8 untouched. A Round 2 independent proofread follows; re-gating does not replace it.

- D2 (BLOCKING, frozen core, all 11 editions): P3 gloss line under the "당신은?" prompt. The `가늘다` entry was DELETED from the gloss line in `content34.py` (and mirrored in the `supp_*.py` record pair; core `check_core.py` hand list updated the same way). Before: `겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share` After: `겹치다 = to overlap · 감사하다 = to thank · 나누다 = to tell apart, to share` Post-fix verification: `가늘` occurs 0 times in all 8 SVGs and in `2026-w46-ko-en.text.md` of every edition; remaining gloss entries intact and correctly punctuated; P3 visually checked at full frame in all 11 editions (shortened gloss inside its box, no overflow/overlap). SVG hash comparison vs the pre-fix inventory: only `p3-munhwa.svg` changed in this edition (zh-tw: P3 + P6).
- ⚠️ DISCREPANCY FLAG for the coordinator / Round 2 proofreader (do not treat the D2 deletion as proof the stem never occurs): pre-fix verification found the attributive inflection `가늰` (가 U+AC00 + 늰 U+B2B0; `'가늘' in '가늰'` is False at codepoint level) 3× per edition — P3 body `길고 가늰 과자를 친구와 나누는` and P5 ×2 (body + exercise stem) — which the verdict's stem list (가는, 가늘게, 가느다란, 얇) did not cover. The prescribed deletion was applied exactly as ordered; post-fix `가늰` remains 3× per edition. Adjudication of keep-vs-restore belongs to Round 2.

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 0 (ja 2,662 vs Round 1's 2,664 — the −2 is the deleted gloss entry leaving the core multiset: 3 Hangul syllables + 细; pt +8 Hangul = the adjudicated quoted sentence; zh-tw 903 unchanged: P6 `規` +1, P3 `細` −1).
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 (identical to Round 1). Kinsoku: 0. Koscan reconstruction: CANDIDATES=307 TRUE_SPLITS=0 S3=0 (reconstruction script preserved at `hidden_files/w46/ko-fix/koscan_reconstruct.py`; the Round 1 koscan script itself was not preserved, only its logs).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-EN-web.pdf` 2292678 bytes (< 7 MB), 8 pages, pdftotext 52460 bytes. `Lucerna-VOL3-EN.pdf` 32290628 bytes, 8 pages. `2026-w46-ko-en.text.md` regenerated from the source manuscript via `textmd.py` (headers byte-identical to pre-fix, 338 items, 27939 bytes; diff vs pre-fix export is only the fixed gloss line(s)).

## Fix record — Round 3 (2026-11-03; Round 2 verdict FAIL — three frozen-core defects)

Round 2 proofreader verdict (2026-11-03): all 11 editions FAIL on three blocking frozen-core defects; D1 confirmed; keys 150/150 confirmed; gates clean. Round 3 fixed ONLY the three defects below, at the build sources (no SVG/PDF patches), full re-render of all 11 editions. D1 was NOT disturbed. No other family touched. Nothing pushed/inserted/posted. Full report: `hidden_files/w46/ko-fix-round3/FIX-REPORT.md`.

- R-GLOSS — RESTORE the `가늘다` gloss entry in the P3 gloss line, exactly as pre-fix (reverses the Round 1 D2 deletion, whose "occurs nowhere" premise Round 2 refuted: `가늰` occurs 3× per edition — P3 body, P5 body, P5 exercise 69 option A, key 69 = A — and `가늘다 → 가늰` is a ㄹ-irregular attributive). Restored in `content34.py`, both sides of the `supp_*.py` record pair, and the core `check_core.py` hand list.
  - Before (Round 1 form): `Note — 겹치다 = to overlap · 감사하다 = to thank · 나누다 = to tell apart, to share`
  - After (restored, verified verbatim from the rendered P3 SVG gloss band): `Note — 겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share`
  - This resolves the Round 1 discrepancy flag in this KIT: the stem DOES occur (as inflected `가늰`); the entry is restored, not deleted.
- D3 — item 54 (P4), stem fix at the core source, key UNCHANGED (`밀렸어요`).
  - Before: `한국시리즈 시작이 하루 ___어요.` → reconstructed `하루 밀렸어요어요` (doubled ending).
  - After: `한국시리즈 시작이 하루 ___.` → reconstructed `한국시리즈 시작이 하루 밀렸어요.` (verified in all 11 renderings).
- D4 — item 103 (P7), stem fix at the core source, key UNCHANGED (`절임배추`).
  - Before: `미리 소금에 절인 배추를 ___이라고 해요.` (ungrammatical: `배추` is vowel-final, quotative must be `라고`).
  - After: `미리 소금에 절인 배추를 ___라고 해요.` → reconstructed `미리 소금에 절인 배추를 절임배추라고 해요.` (verified in all 11 renderings; contrast item 101 `김장이라고`, batchim-final, unchanged).
- Same-class sweep (AST text-read of the build sources, `sweep.py`): all 77 fill-in stems scanned for stem+key doubling — exactly 1 candidate (item 54); all quotative `이라고/라고` usages scanned for final-syllable mismatch — exactly 1 mismatch (item 103) among 3 quotative stems, plus 4 correct prose usages and 1 non-applicable (`'D-7'이라고`, non-Hangul token) reported unscanned-as-defect for Round 3 adjudication. No further candidates; nothing else fixed.
- Keys UNCHANGED: p8.py compare CLEAN 150/150, keydiff [137, 138]; per-edition key-extraction JSONs byte-identical pre-fix vs post-fix (all 150 keys, noted sets identical; keys 54 `밀렸어요` and 103 `절임배추` unchanged everywhere).

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix-round3/gates/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 0. No U+FFFD.
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags in all 88 pages, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38. Kinsoku: 0. Koscan reconstruction: CANDIDATES=358 TRUE_SPLITS=0 S3=0 (script preserved at `hidden_files/w46/ko-fix-round3/koscan-round3.py`).
- P3 gloss-box geometry: gloss lines inside their box (top margin 38.5, bottom margin 47.725); occlusion 0. Visual: P3 full frame checked (restored gloss inside its box, no overflow); P4 item 54 / P7 item 103 checked at full frame in the core + spot checks (de P4, ja P7).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-EN-web.pdf` 2292773 bytes (< 7 MB), 8 pages, pdftotext 52452 bytes. `Lucerna-VOL3-EN.pdf` 32290743 bytes, 8 pages, pdftotext 52452 bytes. `2026-w46-ko-en.text.md` regenerated via `textmd.py` (headers byte-identical to pre-fix, 338 items, 27959 bytes; diff vs pre-fix export is only the restored P3 gloss line).
- Change isolation: hash diff vs the pre-fix snapshot — exactly 9 files changed in this edition (svg/p3, svg/p4, svg/p7, cards p3/p4/p7, print PDF, web PDF, `.text.md`); SVG-text multiset diff — the ONLY string changes are the three fixes (P3 gloss wrap lines, P4 item-54 stem, P7 item-103 stem). No other string changed anywhere.
