# WEEKLY-KIT — Lucerna Korean Weekly VOL.3 · Korean × Italian (2026-W46)

Pairing: Korean text, Italian explanations. Edition slug: `2026-w46-ko-it`.
Week: Mon 9 Nov – Sun 15 Nov 2026 (weekStart 2026-11-09, weekEnd 2026-11-15).
VOL: VOL.3. Lead: 「김장 한창, 수능 D-7 — 11월 11일은 세 가지 이름의 날」.

## Build method

- Core text frozen from the W46 Korean core build
  (`hidden_files/weekly-report-w46-ko-build/`); only the explanation layer rewritten.
- Build dir: `hidden_files/weekly-report-w46-ko-it-build/` — copied from the W45
  ko-it build (`.py` + `assets/` only), content files overwritten with the frozen W46
  core content, it `bslib4.py`/`svglib.py` kept (furniture, `Nota — ` gloss prefix).
- Transform: filtered W45 operations (harvested from the W45 it build's
  `transform-w45.py`: `add()` calls + GEOMETRY/R/RENDER lists, idempotent) applied
  first, then `supp_it.py` (GEOM majority form + 120-string SUPP map, longest-first).
- P1 geometry: majority form — 20pt BRICK badge at y=394, subtitle shifted to 366,
  rules 412/421, dark band 433. Badge:
  `TESTI IN COREANO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`.
  Footer: `Lucerna · SETTIMANALE COREANO VOL.3 · TESTI IN COREANO · SPIEGAZIONI IN ITALIANO`
  / `Pagina N di 8`. Strapline second segment: `Ogni settimana`.
- Right-band line 1 `KIMJANG`; line 2:
  `La stagione del kimjang è in pieno fermento · Manca una settimana all'esame`.
- Phrases pitch 124→112 (patched directly in `content7.py`; GEOM scope is P1 only).
- Letters: Korean `lko` kept; `lcn` = `Esempio della redazione, non vera.`;
  `lcn2` = `Nessuna lettera vera né testo di pagina 8 arrivato: resta l'esempio,
  la promessa passa al VOL.4. Scrivici!` — editor's example + disclosure + solicitation,
  promise carried to VOL.4. No real letters arrived; nothing fabricated.
- E-zone (P8): W45 precedent — items 137/138 keys become Italian, 139/140 stems
  become Italian, keys stay Korean (p8 keydiff [137, 138], expected).
- Type labels in Italian (deliberate deviation from W45, where it kept Chinese
  labels; verified against the build sources): 完成句子→`Completa la frase`,
  单选→`Scelta multipla`, 词汇配对→`Abbinamento`, 完形单选→`Cloze`,
  造句→`Costruisci la frase`, 句型转换→`Trasforma la frase`,
  判断→`Vero o falso`, 翻译→`Traduzione`, 写作→`Scrittura`; exercise
  instructions use `Completa`, `Costruisci`, `Abbina`, `Riscrivi`, `Traduci`,
  `Scrivi` — the family's own W45 instruction vocabulary, carried by the W45
  transform (not by SUPP).

## Contents / counts

8 pages, 150 exercises (registry count): A2 51 / B1 72 / B2 27;
pages 10/18/18/18/18/18/12/38. P8 writing model 158 chars (spaces removed),
inside the printed 150–200자 instruction. P7 golden sentences 8/8 verbatim
from this issue's own articles (whitespace-insensitive, checked against SVGs).

## Gates (2026-11-02)

- `run.py`: TOTAL 150, zero FLOW OVERFLOW / HEAD TOO WIDE; P7 teaser ends 2526.2 (<2540).
- `occlusion_audit.py`: selftest OK; final 0 flags (after the P2 box-title fix below).
- `p8.py compare` (core vs it): CLEAN, missing=[] extra_count=0,
  keydiff=[137, 138] (expected E-zone re-aiming). Extract 150/150.
- `freeze.py diff`: 0 added CJK chars on every page (Latin script; no Hangul added).
- `check_edition.py`: phrases 8/8; orphan scan 1 hit, adjudicated — P4 SHORT-TAIL
  `않아요.` at y=1873, byte-identical wrap in the frozen core SVG (same coordinates);
  the 3-syllable verb-ending tail is the natural wrap point of the frozen stem.
  Kinsoku line-starts 0.
- Letters-box audit (manual, after the core/es/de/pt spill was found): disclosure
  inside its box, margin +8px on all editions; it trailing +60→+66.
- Visual: P1 + P7 cards read — badge/footer/Italian notes clean; letters box,
  phrases pitch, teaser clean.
- Full CJK-literal scan after SUPP: only the adjudicated Hanja paragraph remains
  (shared-kanji band titles etc. are legitimate Italian-edition text).

## Fixes during this build

1. P2 box-title TEXTX collision: `김장 장보기 목록 · Lista della spesa per il kimjang`
   overlapped the exercise below → shortened to `김장 장보기 목록 · Lista della spesa`
   in `content12.py` + `supp_it.py`; re-audit 0 flags.
2. Letters-box trailing +60→+66 (safety margin; the same under-counted-box defect
   found in the core, de, es, pt builds — box 1 line too short for its own text,
   missed by the occlusion audit, caught by visual check + rect measurement).
   Teaser 2520.2→2526.2, still <2540.

## Outputs

- `svg/` (8), `cards/` (8)
- Print: `Lucerna-VOL3-IT.pdf` — 32,463,406 bytes,
  SHA-256 `1321c365eb90db00a74c2c73ea4d60ac14c63668299e825a93dfb37151428ea6`
- Web: `Lucerna-VOL3-IT-web.pdf` (via `tools/webpdf.py`) — 2,288,546 bytes (<7 MB),
  pdftotext 53,516 bytes, phrase 「김장이 한창이에요」 found 7 times, consistent
  with print text. SHA-256 `1453514515557699e6123bb3e1dda4fe877164fa591d56803aa2849abf0eb792`
- `ABSTRACT.txt` (Italian, single line, no ASCII double quotes)
- `2026-w46-ko-it.text.md` — 338 items, 8 pages, exported from the source
  manuscript via `textmd.py` (never from PDF); answer keys/notes excluded.

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

- D2 (BLOCKING, frozen core, all 11 editions): P3 gloss line under the "당신은?" prompt. The `가늘다` entry was DELETED from the gloss line in `content34.py` (and mirrored in the `supp_*.py` record pair; core `check_core.py` hand list updated the same way). Before: `겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere` After: `겹치다 = sovrapporsi · 감사하다 = ringraziare · 나누다 = distinguere, condividere` Post-fix verification: `가늘` occurs 0 times in all 8 SVGs and in `2026-w46-ko-it.text.md` of every edition; remaining gloss entries intact and correctly punctuated; P3 visually checked at full frame in all 11 editions (shortened gloss inside its box, no overflow/overlap). SVG hash comparison vs the pre-fix inventory: only `p3-munhwa.svg` changed in this edition (zh-tw: P3 + P6).
- ⚠️ DISCREPANCY FLAG for the coordinator / Round 2 proofreader (do not treat the D2 deletion as proof the stem never occurs): pre-fix verification found the attributive inflection `가늰` (가 U+AC00 + 늰 U+B2B0; `'가늘' in '가늰'` is False at codepoint level) 3× per edition — P3 body `길고 가늰 과자를 친구와 나누는` and P5 ×2 (body + exercise stem) — which the verdict's stem list (가는, 가늘게, 가느다란, 얇) did not cover. The prescribed deletion was applied exactly as ordered; post-fix `가늰` remains 3× per edition. Adjudication of keep-vs-restore belongs to Round 2.

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: 0 (ja 2,662 vs Round 1's 2,664 — the −2 is the deleted gloss entry leaving the core multiset: 3 Hangul syllables + 细; pt +8 Hangul = the adjudicated quoted sentence; zh-tw 903 unchanged: P6 `規` +1, P3 `細` −1).
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38 (identical to Round 1). Kinsoku: 0. Koscan reconstruction: CANDIDATES=291 TRUE_SPLITS=0 S3=0 (reconstruction script preserved at `hidden_files/w46/ko-fix/koscan_reconstruct.py`; the Round 1 koscan script itself was not preserved, only its logs).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-IT-web.pdf` 2288426 bytes (< 7 MB), 8 pages, pdftotext 53493 bytes. `Lucerna-VOL3-IT.pdf` 32463283 bytes, 8 pages. `2026-w46-ko-it.text.md` regenerated from the source manuscript via `textmd.py` (headers byte-identical to pre-fix, 338 items, 28219 bytes; diff vs pre-fix export is only the fixed gloss line(s)).

## Fix record — Round 3 (2026-11-03; Round 2 verdict FAIL — three frozen-core defects)

Round 2 proofreader verdict (2026-11-03): all 11 editions FAIL on three blocking frozen-core defects; D1 confirmed; keys 150/150 confirmed; gates clean. Round 3 fixed ONLY the three defects below, at the build sources (no SVG/PDF patches), full re-render of all 11 editions. D1 was NOT disturbed. No other family touched. Nothing pushed/inserted/posted. Full report: `hidden_files/w46/ko-fix-round3/FIX-REPORT.md`.

- R-GLOSS — RESTORE the `가늘다` gloss entry in the P3 gloss line, exactly as pre-fix (reverses the Round 1 D2 deletion, whose "occurs nowhere" premise Round 2 refuted: `가늰` occurs 3× per edition — P3 body, P5 body, P5 exercise 69 option A, key 69 = A — and `가늘다 → 가늰` is a ㄹ-irregular attributive). Restored in `content34.py`, both sides of the `supp_*.py` record pair, and the core `check_core.py` hand list.
  - Before (Round 1 form): `Nota — 겹치다 = sovrapporsi · 감사하다 = ringraziare · 나누다 = distinguere, condividere`
  - After (restored, verified verbatim from the rendered P3 SVG gloss band): `Nota — 겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere`
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
- p8.py: CLEAN 150/150, keydiff [137, 138]. Occlusion audit: 0 flags in all 88 pages, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38. Kinsoku: 0. Koscan reconstruction: CANDIDATES=359 TRUE_SPLITS=0 S3=0 (script preserved at `hidden_files/w46/ko-fix-round3/koscan-round3.py`).
- P3 gloss-box geometry: gloss lines inside their box (top margin 38.5, bottom margin 47.725); occlusion 0. Visual: P3 full frame checked (restored gloss inside its box, no overflow); P4 item 54 / P7 item 103 checked at full frame in the core + spot checks (de P4, ja P7).
- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `Lucerna-VOL3-IT-web.pdf` 2288549 bytes (< 7 MB), 8 pages, pdftotext 53507 bytes. `Lucerna-VOL3-IT.pdf` 32463409 bytes, 8 pages, pdftotext 53507 bytes. `2026-w46-ko-it.text.md` regenerated via `textmd.py` (headers byte-identical to pre-fix, 338 items, 28242 bytes; diff vs pre-fix export is only the restored P3 gloss line).
- Change isolation: hash diff vs the pre-fix snapshot — exactly 9 files changed in this edition (svg/p3, svg/p4, svg/p7, cards p3/p4/p7, print PDF, web PDF, `.text.md`); SVG-text multiset diff — the ONLY string changes are the three fixes (P3 gloss wrap lines, P4 item-54 stem, P7 item-103 stem). No other string changed anywhere.
