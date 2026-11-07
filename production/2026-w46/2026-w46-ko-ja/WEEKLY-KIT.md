# WEEKLY-KIT — Lucerna Korean Weekly VOL.3 · Korean × Japanese (2026-W46)

Pairing: Korean text, Japanese explanations. Edition slug: `2026-w46-ko-ja`.
Week: Mon 9 Nov – Sun 15 Nov 2026 (weekStart 2026-11-09, weekEnd 2026-11-15).
VOL: VOL.3. Lead: 「김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날」.

## Build method

- Core text frozen from the W46 Korean core build
  (`hidden_files/weekly-report-w46-ko-build/`); only the explanation layer rewritten.
- Build dir: `hidden_files/weekly-report-w46-ko-ja-build/` — copied from the W45
  ko-ja build (`.py` + `assets/` only), content files overwritten with the frozen
  W46 core content, ja `bslib4.py`/`svglib.py` kept (furniture, `解説 — ` gloss
  prefix, ja NO_START extension in the fan-out's own svglib — canonical svglib
  never edited).
- Transform: filtered W45 operations (harvested REPL flat dict + LINE_EDITS)
  applied first, then `supp_ja.py` (GEOM subtitle-slot form + SUPP map incl. the
  fr set plus 4 shared-kanji band titles `생활 · 生活`, `문화 · 文化`,
  `스포츠 · 体育`, `청년 · 青年` left as-is — the characters read identically in
  Japanese, longest-first).
- P1 geometry: SUBTITLE-SLOT form (distinct from the other 10 editions) — the
  badge REPLACES the subtitle at y=372, 19.5pt BRICK, rules/band/deck unmoved.
  Badge: `韓国語テキスト · 日本語の解説 — 日本語読者のための版`.
  Footer: `Lucerna · 韓国語週刊 VOL.3 · 本文は韓国語 · 解説は日本語` /
  `N ページ（全 8 ページ）`. Strapline second segment: `毎週一号`.
- Right-band line 1 `キムジャン`; line 2: `キムジャン最盛期 · 修能まであと一週間`.
- Phrases pitch 124→112 (patched directly in `content7.py`; GEOM scope is P1 only).
- P8 separator edited in W45 to `— {pg}ページ —` (kept via W45 ops).
- Letters: Korean `lko` kept; `lcn` = `編集部の例文です。`; `lcn2` =
  `本物の手紙も優秀作も届かず、例文を掲載。約束はVOL.4へ。ぜひご投稿ください！` —
  editor's example + disclosure + solicitation, promise carried to VOL.4.
  No real letters arrived; nothing fabricated.
- E-zone (P8): W45 precedent — items 137/138 keys become Japanese, 139/140 stems
  become Japanese, keys stay Korean (p8 keydiff [137, 138], expected).
- CSAT term: 修能 (W45 precedent). Korean `D-` notation kept (D-7 etc., never J-).

## Contents / counts

8 pages, 150 exercises (registry count): A2 51 / B1 72 / B2 27;
pages 10/18/18/18/18/18/12/38. P8 writing model 158 chars (spaces removed),
inside the printed 150–200자 instruction. P7 golden sentences 8/8 verbatim
from this issue's own articles (whitespace-insensitive, checked against SVGs).

## Gates (2026-11-02)

- `run.py`: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE; P7 teaser ends 2470.7 (<2540).
- `occlusion_audit.py`: selftest OK; final 0 flags (after the P2 box-title fix below).
- `p8.py compare` (core vs ja): CLEAN, missing=[] extra_count=0,
  keydiff=[137, 138] (expected E-zone re-aiming). Extract 150/150 — after the
  P8-note fixes below (first compare was SHORT, missing=[81, 133]).
- `freeze.py diff`: 2,664 added CJK chars, ALL kana/kanji, ZERO Hangul —
  adjudicated legitimate Japanese reader notes (strict-CJK-scope lesson: judge
  by the per-char Hangul list, not the raw count).
- `check_edition.py`: phrases 8/8; orphan scan 1 hit, adjudicated — P4 PAREN-FRAG
  `신문에 나온 일이에요.)` at y=2098.2, byte-identical to the core's adjudicated
  hit (complete clause). Kinsoku line-starts 0.
- Letters-box audit (manual): disclosure inside its box, margin +8px.
- Visual: P1 + P7 cards read — subtitle-slot badge form, footer, Japanese notes
  clean; letters box, phrases pitch, teaser clean.
- Full CJK scan after SUPP: all remaining CJK is legitimate Japanese kanji/kana
  (glosses, type labels 単択/文完成/空所補充/語彙対応/組み合わせ/正誤/翻訳/作文,
  band titles). One line that displayed as mojibake (`���紙締め切り`) in tool
  output was verified a display artifact only: the bytes are 本 (U+672C) in
  `content34.py` line 210.

## Fixes during this build

1. P2 box-title BOXTITLE: `김장 장보기 목록 · キムジャンの買い物リスト` right ink
   1467.0 > border 1423.0 → shortened to `김장 장보기 목록 · 買い物リスト` in
   `content12.py` + `supp_ja.py`; re-audit 0 flags.
2. P8 SHORT missing=[81, 133]: both keys' notes wrapped to 2 lines in the 434px
   P8 column, breaking `p8.py` extraction.
   - Item 81 note `リスニングの時間は飛行機が離着陸しない` →
     `リスニング時間は離着陸しない` — the W45 ja transform's own shortening
     (`transform-w45.py` lines 34–35), which the W46 harvest had missed.
   - Item 133 note `語順：主語＋時間＋目的語＋動詞` → `主語・時間・目的語・動詞`
     (new shortening; all four elements kept). Both recorded in `supp_ja.py`.
   Re-extract 150/150, compare CLEAN.

## Outputs

- `svg/` (8), `cards/` (8)
- Print: `Lucerna-VOL3.pdf` — 36,156,859 bytes,
  SHA-256 `7e74eeb2a5413503b97d7e5832246393f5d8c62377c60b6dded36edee0540c35`
  (larger than sibling editions: Japanese kana/kanji glyph subsets).
- Web: `Lucerna-VOL3-web.pdf` (via `tools/webpdf.py`) — 2,661,595 bytes (<7 MB),
  pdftotext 53,830 bytes, phrase 「김장이 한창이에요」 found 7 times, consistent
  with print text. SHA-256 `d049da0475229039206670d58c13462cc576fe4a1c35044ba8723f5ad71671f1`
- `ABSTRACT.txt` (Japanese, single line, no ASCII double quotes)
- `2026-w46-ko-ja.text.md` — 339 items, 8 pages, exported from the source
  manuscript via `textmd.py` (never from PDF); answer keys/notes excluded. (339 vs
  the core's 338: P1 furniture — the subtitle-slot badge replaces the Korean
  subtitle line; all other pages match 1:1.)

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

- D2 (BLOCKING, frozen core, all 11 editions): P3 gloss line under the "당신은?" prompt. The `가늘다` entry was DELETED from the gloss line in `content34.py` (and mirrored in the `supp_*.py` record pair; core `check_core.py` hand list updated the same way). Before: `겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` After: `겹치다 = 重なる · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う` Post-fix verification: `가늘` occurs 0 times in all 8 SVGs and in `2026-w46-ko-ja.text.md` of every edition; remaining gloss entries intact and correctly punctuated; P3 visually checked at full frame in all 11 editions (shortened gloss inside its box, no overflow/overlap). SVG hash comparison vs the pre-fix inventory: only `p3-munhwa.svg` changed in this edition (zh-tw: P3 + P6).
- ⚠️ DISCREPANCY FLAG for the coordinator / Round 2 proofreader (do not treat the D2 deletion as proof the stem never occurs): pre-fix verification found the attributive inflection `가늰` (가 U+AC00 + 늰 U+B2B0; `'가늘' in '가늰'` is False at codepoint level) 3× per edition — P3 body `길고 가늰 과자를 친구와 나누는` and P5 ×2 (body + exercise stem) — which the verdict's stem list (가는, 가늘게, 가느다란, 얇) did not cover. The prescribed deletion was applied exactly as ordered; post-fix `가늰` remains 3× per edition. Adjudication of keep-vs-restore belongs to Round 2.

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 2662 (ja 2,662 vs Round 1's 2,664 — the −2 is the deleted gloss entry leaving the core multiset: 3 Hangul syllables + 细; pt +8 Hangul = the adjudicated quoted sentence; zh-tw 903 unchanged: P6 `規` +1, P3 `細` −1).
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 (identical to Round 1). Kinsoku: 0. Koscan reconstruction: CANDIDATES=310 TRUE_SPLITS=0 S3=0 (reconstruction script preserved at `hidden_files/w46/ko-fix/koscan_reconstruct.py`; the Round 1 koscan script itself was not preserved, only its logs).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-web.pdf` 2661269 bytes (< 7 MB), 8 pages, pdftotext 53820 bytes. `Lucerna-VOL3.pdf` 36156571 bytes, 8 pages. `2026-w46-ko-ja.text.md` regenerated from the source manuscript via `textmd.py` (headers byte-identical to pre-fix, 339 items, 28230 bytes; diff vs pre-fix export is only the fixed gloss line(s)).

## Fix record — Round 3 (2026-11-03; Round 2 verdict FAIL — three frozen-core defects)

Round 2 proofreader verdict (2026-11-03): all 11 editions FAIL on three blocking frozen-core defects; D1 confirmed; keys 150/150 confirmed; gates clean. Round 3 fixed ONLY the three defects below, at the build sources (no SVG/PDF patches), full re-render of all 11 editions. D1 was NOT disturbed. No other family touched. Nothing pushed/inserted/posted. Full report: `hidden_files/w46/ko-fix-round3/FIX-REPORT.md`.

- R-GLOSS — RESTORE the `가늘다` gloss entry in the P3 gloss line, exactly as pre-fix (reverses the Round 1 D2 deletion, whose "occurs nowhere" premise Round 2 refuted: `가늰` occurs 3× per edition — P3 body, P5 body, P5 exercise 69 option A, key 69 = A — and `가늘다 → 가늰` is a ㄹ-irregular attributive). Restored in `content34.py`, both sides of the `supp_*.py` record pair, and the core `check_core.py` hand list.
  - Before (Round 1 form): `解説 — 겹치다 = 重なる · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う`
  - After (restored, verified verbatim from the rendered P3 SVG gloss band): `解説 — 겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う`
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
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 2,664 (Round 2: 2,662; +2 = restored 細, Hangul added 0). No U+FFFD.
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags in all 88 pages, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38. Kinsoku: 0. Koscan reconstruction: CANDIDATES=360 TRUE_SPLITS=0 S3=0 (script preserved at `hidden_files/w46/ko-fix-round3/koscan-round3.py`).
- P3 gloss-box geometry: gloss lines inside their box (top margin 38.5, bottom margin 47.725); occlusion 0. Visual: P3 full frame checked (restored gloss inside its box, no overflow); P4 item 54 / P7 item 103 checked at full frame in the core + spot checks (de P4, ja P7).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-web.pdf` 2661599 bytes (< 7 MB), 8 pages, pdftotext 53821 bytes. `Lucerna-VOL3.pdf` 36156863 bytes, 8 pages, pdftotext 53821 bytes. `2026-w46-ko-ja.text.md` regenerated via `textmd.py` (headers byte-identical to pre-fix, 339 items, 28252 bytes; diff vs pre-fix export is only the restored P3 gloss line).
- Change isolation: hash diff vs the pre-fix snapshot — exactly 9 files changed in this edition (svg/p3, svg/p4, svg/p7, cards p3/p4/p7, print PDF, web PDF, `.text.md`); SVG-text multiset diff — the ONLY string changes are the three fixes (P3 gloss wrap lines, P4 item-54 stem, P7 item-103 stem). No other string changed anywhere.
