# WEEKLY-KIT — The Lucerna English Weekly VOL.3 (2026-W46) · EN × KO

- Slug week: `2026-w46` · frontmatter week `2026-W46` · issue week Mon 9 Nov – Sun 15 Nov 2026.
- Target: English (en). Reader language: Korean (ko). Edition slug: `2026-w46-en-ko`. VOL.3.
- Core text frozen from `files/weekly-report-w46-en-core/` (see its WEEKLY-KIT.md for contents, trend/fact sources, images, promises). Only the explanation layer was rewritten in Korean; English body text is byte-identical (freeze diff: 2,381 added CJK characters).
- Build dir: `hidden_files/weekly-report-w46-en-ko-build/` (built from scratch in this cycle: `gen_fanout.py ko` first failed with 148 leftover core strings (MAP 104 from `kept-ko.json`, 0 fragment pairs). `hidden_files/w46/authored-ko.json` (151 keys: 147 leftovers + 4 mixed-string fixes) translates every remaining explanation string into Korean in the kept-KO style (polite 해요체, concise glosses; e.g. poppy = 양귀비꽃, veteran = 참전 용사, armistice = 휴전 협정, Remembrance Day = 전몰자 추모일). `kept-ko.json` verified free of U+FFFD corruption (an earlier garbled display was a rendering artifact).
- LESSON: `gen_fanout.py`'s leftover check compares whole AST strings only, so partial translations slip through. A separate Han-character scan found 4 mixed strings (e.g. `用 will + 动词바꿔 쓰기…`, the VOL.2 editor's note, `语法点｜fall…`), fixed with whole-string authored entries. After re-run: leftover scan 0, Han-string count 0 in content/bslib sources (the `；`/`：` in content8 key strings are frozen core conventions, verified in the core source).)
- Furniture (W45 EN×KO shipped precedents, VOL.3): footer "The Lucerna · 영어 주간지 VOL.3 · 텍스트는 영어 · 해설은 한국어"; page line "제 {n} 면 / 총 {total} 면"; gloss prefix "해설 — "; P1 badge in the y=372 slot, 19.5pt bold BRICK: "영어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판"; masthead line "영어 주간지 · VOL.3 · 기념 · 축구 · 영화" at 46pt.
- P8 keys convention (W45 EN×KO): explicit (PRINT_SET, 70 notes). p8.py verdict: CLEAN, 70→70.

## Exercises

- Total 150 (P1 10, P2 17, P3 18, P4 18, P5 18, P6 18, P7 12, P8 39); A2 60, B1 69, B2 21 — identical numbering/levels to the core (re-measured from `hidden_files/w46/en-core/registry.json`, 150 entries, 1–150 unique); only type labels, notes and keys were translated. P8 starts at 112; dialogue 145–149; writing 150 (open). Model text "My Wednesday, November 11" = 84 words.

## Layout adjustments vs core (English text unchanged)

- Occlusion fixes (first audit 2 P1 flags, both pixel-adjudicated real): orphan "." from the caption wrapping ("추모예요. Remembrance Day는 전몰자 추모일이에요." → "Remembrance Day는 전몰자 추모일이에요.") and the searches title 13px over ("이번 주 영어권 인기 검색어 · Google Trends 스냅샷" → "… · Google Trends"). Re-audit: 0 flags.
- Visual-pass fix: missing spaces before weekday parentheses in the P1 Week-in-Numbers box ("Ebenezer(금요일)" / "Finals(일요일)" → "Ebenezer (금요일)" / "Finals (일요일)"), fixed in source + full re-render + re-gate.

## Gates

- Builder self-check: PASS — final build log zero FLOW OVERFLOW / HEAD TOO WIDE warnings, 150 exercises.
- `occlusion_audit.py`: 0 flags — PASS (JSON: `hidden_files/w46/final-ko-occlusion.json`; re-gated after the final re-render: `hidden_files/w46/final2-ko-occlusion.json`).
- Supplementary scans (`hidden_files/w46/rowcheck46.py`, adapted family rowcheck: same-baseline text-ink collisions on all 8 pages, P6 chart-label GRAZE coverage, gloss-count comparison): CLEAN on all 8 pages, P6 chart-label coverage 0.0%, 0 gloss-count mismatches.
- `p8.py compare` (explicit P8 SVG paths, total 150): CLEAN, 70→70 — PASS (JSON: `hidden_files/w46/final-ko-p8.json`; re-gated after the final re-render: `hidden_files/w46/final2-ko-p8.json`).
- `freeze.py diff` vs core: exit 0 (plain diff, no --strict-cjk), TOTAL added CJK characters 2,381 — the Hangul explanation layer, expected (--strict-cjk fails by design on a CJK layer) — PASS (JSON: `hidden_files/w46/final-ko-freeze.json`; re-gated after the final re-render: `hidden_files/w46/final2-ko-freeze.json`).
- Visual card pass: P1 + P8 inspected at full frame (all other pages covered by the geometric gates + same-baseline scan); no overflow/overlap, no missing glyphs/tofu, footer intact, images present with credits.
- Web PDF: `The-Lucerna-VOL3-web.pdf`, 1,785,374 bytes (< 7 MB), text layer 47,098 bytes via pdftotext. Print PDF kept: `The-Lucerna-VOL3.pdf` (18,551,621 bytes).
- `2026-w46-en-ko.text.md` (45,987 bytes): exported from the fan-out source manuscript via AST (`hidden_files/w46/en_textmd.py`, never from PDF/SVG) + registry answers appended; verified byte-identical to a fresh deterministic re-export; 8 pages, 150 numbered answers.
- `ABSTRACT.txt` (479 bytes): single line + trailing newline, no ASCII double quotes, reader-native.

## Proofread record (builder self-check, 3 Nov 2026)

- Round 1: full read of the line-by-line proof diff against a same-exporter en-de reference (258 lines; lines identical to en-de, i.e. the shared English body, hidden). Round 2: regeneration of the proof diff from the final text.md export and exact diff against round 1 — the ONLY differences were the intended fix lines below (re-read and verified); all other lines byte-identical to the round-1 proofread text. Zero new issues in round 2.
- FLAG FOR THE COORDINATOR (core-source defect, inherited unchanged): the P7/P8 gloss of "HOW LONG?" as a term of office ("El mandato" / "O mandato" / "Срок полномочий" / "임기는 얼마나?" / "任期多長？" / "任期はどれくらい？") comes from the frozen core source and is shared by all 11 natives including shipped en-de and en-zh-cn. It was NOT diverged in these 9 editions — fixing it means fixing the core. An independent proofreader follows; this self-proofread does not replace it.

### Fixes applied in this edition

- Matching notes "word=gloss" → "word = gloss" (20 notes, regex `"([a-z-]+)=([가-힣])`).
- #103: "is 여전히 ~이다" → "is = 여전히 ~이다"; #107: "there were 과거형" → "there were = 과거형".
- Verified correct and left as-is: #36 "split = 의견이 갈린" (core sentence "the vote is split again") and #55 "여덟 명" (eight players).

## Repro

```bash
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-ko-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-en-ko
./venv/bin/python webpdf.py ../files/weekly-report-w46-en-ko/svg ../files/weekly-report-w46-en-ko/The-Lucerna-VOL3-web.pdf
```

## Fix record — independent proofread Round 1 fixes (fix worker, 2026-11-03)

Source-only fixes per `hidden_files/w46/en-proofread-gates/proofreader-verdict-round1.md`; full re-render from the build sources (run.py + render.py + tools/webpdf.py + en_textmd.py). No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; this record is not a proofread verdict.
- B4 (all 11 editions, frozen core): P7 toolbox B1 sentence wrapped with a lone closing guillemet `»` alone on a line. Source `hidden_files/weekly-report-w46-en-build/content7.py:51` (and the same line in every fan-out `content7.py`): before `B1 — « Dickens wrote the story in 1843. »` → after `B1 — « Dickens wrote the story in 1843.»` (space before `»` removed in the toolbox para only; the P7 B1 box example on line 32 keeps the spaced form). Rendered in all 11 as two lines `B1 — « Dickens wrote the story in` / `1843.»`; no lone `»` line remains in any edition (verified by SVG text extraction and visually on the P7 cards of all 11 editions).
- B2 (ko): `ABSTRACT.txt` typo `NFL 댦헨 경기` — one character `댦` U+B326 → `뮌` U+BB8C (`뮌헨` = Munich). Abstract re-verified: single line + trailing newline, no ASCII double-quote, 479 bytes (unchanged).
- B3 (ko): P8 mid-word syllable splits with tail ≥3, ×2. (1) Entry 68 note (`content56.py:37`): before `갈라쇼는 솔퍼드에서 생방송돼요` → after `모금 갈라쇼는 솔퍼드에서 생방송돼요` — `솔퍼드` now unsplit on one P8 line. (2) Entry 130 note (`content8.py:63`): before `전교생이 2분간 묵념해요` → after `전교생이 2분 동안 묵념해요` — break now at the word boundary, `묵념해요` unsplit. Canonical `koscan.py` (10–45 window, source-adjudicated): CANDIDATES 28, TRUE_SPLITS 13, S3 = 0 (was 1), orphan final lines 0, line-start orphan punct 1 (the frozen P8 `! See you…` convention, adjudicated). The other 13 true splits (1–2-syllable tails) are below the S3 standard and were left alone. Verified visually on the P8 card.
- M2 (fr/ko/zh-tw): doubled gloss prefix `해설 — 해설 —` on the 5 P2–P6 gloss boxes; the leading `해설 — ` was stripped from each of the 5 `f.gloss(...)` call strings (`content12.py:180`, `content34.py:28,111`, `content56.py:26,107`), rendering a single `해설 — …` per the KIT furniture claim. P1 single-prefix line untouched.
- REGRESSION FIX (introduced by the M2 reflow, same defect class as B5/B6): removing the prefix re-wrapped two gloss boxes onto orphan final lines — P3 box ended `은.` alone, P4 box ended `.` alone. Re-broken in source: P3 gloss (`content34.py:28`) `아직 오지 않은.` → `아직 오지 않은 것.` (final line `은 것.`); P4 gloss (`content34.py:111`) `스타 선수.` → `스타선수.` (box now 2 lines, period attached). Wrap-simulated with the real fonts before applying; koscan re-run after the re-render confirms 0 orphans. The fr/zh-tw gloss boxes were wrap-simulated too — no orphans there.
- `<slug>.text.md` regenerated with the canonical `hidden_files/w46/en_textmd.py` (uniform family format; headers verbatim). Old text.md preserved under `hidden_files/w46/en-fix/old-textmd/`. For this edition the diff vs the old file is exactly the fix lines listed above.
- Re-gates on the final artifacts: build log zero `FLOW OVERFLOW` / `HEAD TOO WIDE`, TOTAL 150; canonical `occlusion_audit.py` 0 flags, selftest OK; `rowcheck46.py` 0 same-baseline collisions, 0 gloss-count mismatches, P6 chart-label GRAZE 0.0%; registry re-measured (core): 150 unique exercises 1–150, per-page 10/17/18/18/18/18/12/39, A2 60 / B1 69 / B2 21.
- `freeze.py diff` vs core: exit 0, TOTAL added CJK characters 2,375 (was 2,381; delta is pure Hangul explanation layer: M2 de-duplication −10, B5 core −2, B3 +3, regression fix +1, multiset sharing; script scan: Hangul only, 0 Han). `p8.py compare --total 150`: CLEAN, 70→70, missing [], uncertain [], keydiff [137, 138, 139, 140, 150] legitimate. Web PDF 1,785,457 bytes (< 7 MB), pdftotext 47,052 bytes (equal to print extraction, 8 pages); print PDF 18,551,689 bytes; text.md 45,945 bytes.
