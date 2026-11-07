# WEEKLY-KIT — Lucerna 简体中文周报 VOL.3 (W46), zh-cn × ko

## Identity and spec

- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. VOL.3.
- **Pairing:** zh-cn × ko — Simplified Chinese body text with a Korean
  explanation layer, the edition for Korean-speaking readers. P1 badge:
  “중국어 간체 텍스트 · 한국어 해설 — 한국어 독자를 위한 판”.
- **Masthead:** bare `Lucerna` (no article). Every page footer reads
  “Lucerna · 중국어 간체 주간지 VOL.3 · 텍스트는 중국어 간체 · 해설은
  한국어”; page line “제 {n} 면 / 총 8 면”. Gloss prefix “해설 — ”. P8
  separator “— 제 {n} 면 —”. P7 phrase tags “p. N” (kept, W45 KO
  precedent). Model answer “모델 답안: ”.
- **Format:** 8 pages, 1950×2700 px, 4 columns, same geometry as the core.
  150 exercises, unified numbering 1–150, P8 keys generated from the
  registry. Core text frozen (see below); only the explanation layer was
  rewritten, natively in Korean.
- **Status:** builder self-check complete (see gates below). Builder
  handoff, NOT a finalisation claim — independent proofreading is still
  owed by the parent line. No Discord, no chat dumps, no repo push.

## Contents

Identical to the core edition (`files/weekly-report-w46-zh-cn-core/
WEEKLY-KIT.md` — contents table, trend sources, W45-promise handling,
image authorisations). This KIT records only what differs: the Korean
explanation layer, the transform, and the gates.

## Frozen-core proof — strict-CJK adjudication (read this first)

- `tools/freeze.py diff --strict-cjk` is MEANINGLESS as a pass/fail gate
  for this edition: the explanation layer itself is written in Korean
  (Hangul), so added CJK is expected and large. Final run: **TOTAL added
  CJK characters: 4300** (all Hangul in the explanation layer).
- The W45 KO adjudication was applied instead: **Hanzi-added accounting.**
  Counting only Hanzi (U+4E00–U+9FFF) per page, core vs edition:
  **added Hanzi = 0 on ALL 8 pages** (P1–P8). This matches — and on P8
  betters — the W45 KO precedent (Hanzi added 0 on P1–P7, only cited 候
  on P8). No new Hanzi was introduced by any Korean explanation string.
- Built by copying the finished W46 core build dir and applying exact-
  string replacements (282 keys, `hidden_files/w46/maps/ko.json`,
  `hidden_files/w46/transform.py` — every key asserted found; coverage
  checked with `hidden_files/w46/coverage.py`: all English display strings
  covered or explicitly frozen).
- Phrases of the week: all 8 exactly 2× (article + P7) in the final SVGs
  (joined-text counting).
- Photo credits kept in English (W45 precedent). Pinyin kept; English
  glosses translated.

## Adjudications (for the independent proofreader)

- **Hanzi hygiene fixes in build 2:** the first build added 4 Hanzi
  (双 ×3, 付 ×1). Three came from writing “双11” in Korean explanations
  where the source said “Double 11” — replaced with Hangul “더블 11”
  (the W45 KO precedent writes no Hanzi in explanations). The fourth was
  a typo: a Japanese “付き” had slipped into a Korean P8 header string —
  replaced with pure Korean (“답마다 설명이 있어요”). A full kana scan
  of the final map found no other Japanese strays. (An earlier map draft
  also contained a stray “届” kanji in one Korean sentence; fixed before
  the first build.)
- **Comma-after-CJK:** two Korean notes were written with “—” instead of
  a comma directly after a CJK character (e.g. “소포는 个 를 써요 — 只
  나 条 가 아니에요.”), because the typesetter converts such commas to
  full-width “，” — same trap as the Latin-script editions.
- **P7 B1 example:** the Korean explanation keeps the English example
  sentence (“영어 «Monday, Nov 9»는 … 가 돼요”), as in W45.
- **KO orphan scan (W45 lesson 16):** line-start closing punctuation and
  dangling opening-paren line-ends scanned across all 8 final SVGs:
  **0 flags**.

## Gates (final render)

- Driver: TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 164 characters, **zero** FLOW
  OVERFLOW / HEAD TOO WIDE warnings (terse notes from the start: the P8
  keys simulation ends at y = 2263, bottom 2540, 151 wrapped lines).
- Occlusion audit (`tools/occlusion_audit.py`, selftest first): **0 flags**.
- Same-baseline ink-collision scan (`hidden_files/w46/rowcheck.py` §1):
  all 8 pages CLEAN (§2 hardcodes the NL P6 filename and does not run for
  this family; P6 chart rects verified directly: 220/330/550/770 px from
  x=325).
- `tools/p8.py extract --total 150`: noted set = 150 of 150.
- `tools/p8.py compare` core vs edition P8: status CLEAN (missing = [],
  extra = 0, keydiff = []).
- `tools/freeze.py diff --strict-cjk`: TOTAL added CJK 4300 — EXPECTED
  FAIL, adjudicated by Hanzi-added accounting above (added Hanzi = 0 on
  all pages; do NOT record this edition as “strict-cjk clean”).
- Web PDF (`tools/webpdf.py`): `Lucerna-VOL3-KO-web.pdf`, 2,526,535
  bytes (< 7 MB), 46,858 text bytes; `pdftotext` output byte-identical to
  the print PDF (`Lucerna-VOL3-KO.pdf`, 32,301,882 bytes). Print PDF kept
  in the edition dir.
- Visual check: P8 card read in full after the final render (keys end
  cleanly above the footer rule); P1/P2 cards spot-checked.
- Files: 8 SVGs in `svg/`, 8 cards PNG, print + web PDFs, `ABSTRACT.txt`
  (Korean), `2026-w46-zh-cn-ko.text.md` (exported from the source
  manuscript with the fixed `hidden_files/w46/textmd.py`, never from
  PDF), this KIT.

## Reproduction

```bash
cd hidden_files/weekly-report-w46-zh-cn-ko-build
../../tools/venv/bin/python run.py
../../tools/venv/bin/python render.py
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-zh-cn-ko
./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-zh-cn-ko/svg/p8-ceyan.svg --total 150
./venv/bin/python p8.py compare --core-p8 ../files/weekly-report-w46-zh-cn-core/svg/p8-ceyan.svg --edition-p8 ../files/weekly-report-w46-zh-cn-ko/svg/p8-ceyan.svg --total 150
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w46-zh-cn-core/svg --edition-svg ../files/weekly-report-w46-zh-cn-ko/svg --strict-cjk
./venv/bin/python webpdf.py ../files/weekly-report-w46-zh-cn-ko/svg ../files/weekly-report-w46-zh-cn-ko/Lucerna-VOL3-KO-web.pdf
python3 ../w46/textmd.py 2026-w46-zh-cn-ko ../files/weekly-report-w46-zh-cn-ko/2026-w46-zh-cn-ko.text.md
```

To rebuild from the core: copy the core build dir, repoint OUT paths to
`files/weekly-report-w46-zh-cn-ko/svg`, apply `hidden_files/w46/maps/
ko.json` with `hidden_files/w46/transform.py`, then run as above.

## Post-proof fix record

### Fix — Round 2 verdict D3 + D4 (blocking, frozen-core answer-key registry errors; 2026-11-03 fix worker; full Round 3 independent proofread still owed)

- **Trigger:** Round 2 proofreader verdict D3 + D4 (`hidden_files/w46/zh-cn-proofread-gates-round2/proofreader-verdict-round2.md`). Both defects lived in the shared frozen-core registry and were carried faithfully into every fan-out edition. No other change was made.
- **D3 (P2 matching, ex. 25-28):** printed P8 keys were `25. c / 26. b / 27. d` (28. a correct). Rendered right column: a. "北方冬天家里暖和，靠它" (= 供暖), b. "打开快递柜要用的号码" (= 取件码), c. "买的东西，装在里面送来" (= 包裹), d. "双11最忙的卖货时间" (= 高潮场). Correct keys: **25. d / 26. c / 27. b / 28. a**. Source: core build `content12.py:282`, keys `["c","b","d","a"]` -> `["d","c","b","a"]`, and the four P8 note trailing letters re-lettered to match (c/b/d/a -> d/c/b/a). List order 25-28 verified from source before editing.
- **D4 (P6 matching, ex. 99-100):** printed P8 keys were `99. b / 100. a` (97. c, 98. d correct). Rendered right column: a. "还没发生的事，先猜一猜" (= 预报), b. "提前放到离买家近的地方" (= 前置), c. "别人说的话，不一定是真的" (= 说法), d. "量出来的数字" (= 数据). Correct keys: **97. c / 98. d / 99. a / 100. b**. Source: core build `content56.py:226`, keys `["c","d","b","a"]` -> `["c","d","a","b"]`, and the two P8 note trailing letters re-lettered (b/a -> a/b). List order 97-100 verified from source before editing. (P8 prints `"{n}. {key} — {note}"`, so keys and note letters had to change together or the line would contradict itself.)
- **Applied in:** all 10 build dirs (`content12.py` + `content56.py` in each) and all 9 transform maps (`hidden_files/w46/maps/{de,es,fr,it,ja,ko,nl,pt,ru}.json`, 5 note entries re-lettered per map; rebuild-from-core reproducibility re-tested for ES: transform OK, 282 keys, match_set blocks byte-identical). Post-fix grep: no old key list remains in any build dir.
- **Full 150-key re-verification (core registry, static dump of all 130 `ex` + 5 `match_set`):** 145 keys confirmed correct, only 25/26/27/99/100 wrong — now corrected. All 5 matching sets checked option-by-option (P3 43-46 b/c/a/d, P4 61-64 d/c/b/a, P5 79-82 d/c/b/a confirmed correct). Arithmetic recomputed (260+90=350; 350-60=290); writing model 164 characters. Log: `hidden_files/w46/zh-cn-fix-keys/key-verification-log.md`. Flagged, NOT changed (pre-existing stem awkwardness, passed by the Round 2 proofreader; for Round 3/coordinator): ex. 101 stem reads "我拿了一个___包裹。" with key 个 — the stem already contains 一个 before the blank.
- **Re-render:** full re-render of all 10 editions from source; 0 FLOW OVERFLOW / HEAD TOO WIDE in every driver log; `.text.md` regenerated from the source manuscript (diff vs pre-fix copy = exactly the 5 corrected note lines per edition; headers preserved verbatim). Change footprint vs the pre-fix snapshot: exactly 5 files per edition changed (`.text.md`, print PDF, web PDF, `svg/p8-ceyan.svg`, `cards/p8-ceyan.png`) — P2/P6 SVGs are byte-identical because matching keys print only on P8.
- **Re-gates on final artifacts (all 10):** occlusion audit 0 flags (selftest OK); freeze `--strict-cjk` added CJK 0 every page for the 8 Latin/RU editions, JA total added 4908 and KO total added 4304 with KO Hanzi-added 0 (identical to Round 1 adjudicated figures); p8.py extract 150/150 + compare CLEAN, keydiff [] per edition; rowcheck section 1 CLEAN all 8 pages (section 2 crash on hardcoded `p6-verdieping.svg` is the known N/A); counts 150 (A2 56/B1 69/B2 25), per-page 10/18/18/18/18/18/12/38; P7 phrases 2x each; P6 chart rects exact; kinsoku 0; web PDFs 8 pages, <= 7 MB, pdftotext bytes > 0 and byte-identical web vs print; freeze baseline for the core 8/8 SHA-identical. The 5 corrected keys were verified printing correctly in this edition's native P8 rendering (25.d / 26.c / 27.b / 99.a / 100.b, key and note letter consistent). Visual: P1/P2/P6/P8 at full frame, zero defects. Gate evidence: `hidden_files/w46/zh-cn-fix-keys/gates/`.
- **Status after this fix:** re-gated clean by the fix worker; full Round 3 independent proofread of all 10 editions is still owed before shipping. No push, no insert, no Discord post, no chat dump.
