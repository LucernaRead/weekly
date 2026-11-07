# WEEKLY-KIT — Lucerna 简体中文周报 VOL.3 (W46), zh-cn × ja

## Identity and spec

- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. VOL.3.
- **Pairing:** zh-cn × ja — Simplified Chinese body text with a Japanese
  explanation layer, the edition for Japanese-speaking readers. P1 badge:
  “中国語（簡体字）テキスト · 日本語の解説 — 日本語読者のための版”.
- **Masthead:** bare `Lucerna` (no article). Every page footer reads
  “Lucerna · 中国語（簡体字）週刊 VOL.3 · 本文は中国語（簡体字） ·
  解説は日本語”; page line “{n} ページ（全 8 ページ）”. Gloss prefix
  “解説 — ”. P8 separator “— {n} ページ —”. P7 phrase tags “p. N” (kept,
  W45 JA precedent). Model answer “モデル解答：”.
- **Format:** 8 pages, 1950×2700 px, 4 columns, same geometry as the core.
  150 exercises, unified numbering 1–150, P8 keys generated from the
  registry. Core text frozen (see below); only the explanation layer was
  rewritten, natively in Japanese.
- **Status:** builder self-check complete (see gates below). Builder
  handoff, NOT a finalisation claim — independent proofreading is still
  owed by the parent line. No Discord, no chat dumps, no repo push.

## Contents

Identical to the core edition (`files/weekly-report-w46-zh-cn-core/
WEEKLY-KIT.md` — contents table, trend sources, W45-promise handling,
image authorisations). This KIT records only what differs: the Japanese
explanation layer, the transform, and the gates.

## Frozen-core proof — strict-CJK adjudication (read this first)

- `tools/freeze.py diff --strict-cjk` is MEANINGLESS as a pass/fail gate
  for this edition: the explanation layer itself is written in Japanese
  (kana + kanji), so added CJK is expected and large. Final run: **TOTAL
  added CJK characters: 4908** (per page: p1 398, p2 479, p3 306, p4 342,
  p5 283, p6 397, p7 783, p8 1922 — the bulk is hiragana/katakana and
  Japanese kanji in the explanation layer).
- The W45 JA string-level gate was applied instead: **Chinese-run
  conservation.** Every maximal CJK run (≥2 chars) in the core SVGs was
  checked against the same page's joined text in this edition. The ONLY
  missing runs are 6, all adjudicated and identical to the other 7
  shipped fan-outs:
  - furniture, replaced wholesale per the badge/footer rule (W45
    precedent): “简体中文周报” (footer), “简体中文正文” + “英语讲解”
    (badge);
  - the 「包裹」 word-of-week gloss sentence, an explanation-layer string
    rewritten natively in every fan-out: “买的东西”, “都装在包裹里”,
    “送到你手里” (verified absent in the DE/FR/ES/IT/PT/NL/RU editions
    too — same treatment, not a JA-only loss).
- Built by copying the finished W46 core build dir and applying exact-
  string replacements (282 keys, `hidden_files/w46/maps/ja.json`,
  `hidden_files/w46/transform.py` — every key asserted found; coverage
  checked with `hidden_files/w46/coverage.py`: all English display strings
  covered or explicitly frozen).
- Phrases of the week: all 8 exactly 2× (article + P7) in the final SVGs
  (joined-text counting).
- Photo credits kept in English (W45 precedent). Pinyin kept; English
  glosses translated.
- The build copy's `svglib.py` extends `NO_START` with small kana
  “ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ” (W45 precedent: a line must
  not start with small kana). The canonical `svglib.py` was never edited.

## Adjudications (for the independent proofreader)

- **fanout.sh JA-branch bug, fixed:** the tool's kana-extension insertion
  assumed `NO_START` at module level, but in the W46 `svglib.py` it is
  function-local (indented); the first JA build failed with
  `IndentationError`. The insertion was fixed to preserve the line's
  indentation, `fanout.sh` itself was patched (indentation-preserving
  insert), and the shipped build was produced by the patched script —
  the fix reproduces on a fresh rebuild (verified: the shipped build
  copy's `svglib.py` lines 101–103 carry the indented `NO_START +=` line).
- **Box title shortened:** “本周生活小日历 · 今週のカレンダー”
  (BOXTITLE flag in build 1).
- **Comma-after-CJK:** two Japanese notes were written with “—” instead
  of a comma directly after a CJK character (e.g. “荷物は 個 を使う —
  只 や 条 ではない。”), because the typesetter converts such commas to
  full-width “，” — same trap as the Latin-script editions.
- **P7 B1 example:** the Japanese explanation keeps the English example
  sentence (“英語の «Monday, Nov 9» は … になる”), as in W45.
- **Kinsoku/orphan scan:** the small-kana `NO_START` extension is the W45
  precedent for the P7 “って...” line-start orphan class; no orphan
  line-start flags were raised by the occlusion audit on the final SVGs.

## Gates (final render)

- Driver: TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 164 characters, **zero** FLOW
  OVERFLOW / HEAD TOO WIDE warnings (terse notes from the start: the P8
  keys simulation ends at y = 2263, bottom 2540, 152 wrapped lines).
- Occlusion audit (`tools/occlusion_audit.py`, selftest first): **0 flags**.
- Same-baseline ink-collision scan (`hidden_files/w46/rowcheck.py` §1):
  all 8 pages CLEAN (§2 hardcodes the NL P6 filename and does not run for
  this family; P6 chart rects verified directly: 220/330/550/770 px from
  x=325).
- `tools/p8.py extract --total 150`: noted set = 150 of 150.
- `tools/p8.py compare` core vs edition P8: status CLEAN (missing = [],
  extra = 0, keydiff = []).
- `tools/freeze.py diff --strict-cjk`: TOTAL added CJK 4908 — EXPECTED
  FAIL, adjudicated by Chinese-run conservation above (do NOT record this
  edition as “strict-cjk clean”).
- Web PDF (`tools/webpdf.py`): `Lucerna-VOL3-JA-web.pdf`, 2,730,433
  bytes (< 7 MB), 47,271 text bytes; `pdftotext` output byte-identical to
  the print PDF (`Lucerna-VOL3-JA.pdf`, 33,921,301 bytes). Print PDF kept
  in the edition dir.
- Visual check: P8 card read in full after the final render (keys end
  cleanly above the footer rule); P1/P2 cards spot-checked for the fixed
  box-title area.
- Files: 8 SVGs in `svg/`, 8 cards PNG, print + web PDFs, `ABSTRACT.txt`
  (Japanese), `2026-w46-zh-cn-ja.text.md` (exported from the source
  manuscript with `hidden_files/w46/textmd.py`, never from PDF), this KIT.

## Reproduction

```bash
cd hidden_files/weekly-report-w46-zh-cn-ja-build
../../tools/venv/bin/python run.py
../../tools/venv/bin/python render.py
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-zh-cn-ja
./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-zh-cn-ja/svg/p8-ceyan.svg --total 150
./venv/bin/python p8.py compare --core-p8 ../files/weekly-report-w46-zh-cn-core/svg/p8-ceyan.svg --edition-p8 ../files/weekly-report-w46-zh-cn-ja/svg/p8-ceyan.svg --total 150
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w46-zh-cn-core/svg --edition-svg ../files/weekly-report-w46-zh-cn-ja/svg --strict-cjk
./venv/bin/python webpdf.py ../files/weekly-report-w46-zh-cn-ja/svg ../files/weekly-report-w46-zh-cn-ja/Lucerna-VOL3-JA-web.pdf
python3 ../w46/textmd.py 2026-w46-zh-cn-ja ../files/weekly-report-w46-zh-cn-ja/2026-w46-zh-cn-ja.text.md
```

To rebuild from the core: copy the core build dir, repoint OUT paths to
`files/weekly-report-w46-zh-cn-ja/svg`, apply `hidden_files/w46/maps/
ja.json` with `hidden_files/w46/transform.py` (the patched `fanout.sh`
does all of this, including the kana extension), then run as above.

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
