# WEEKLY-KIT — 2026-W47 · German target, Japanese reader

- Edition: `2026-w47-de-ja` — German target text, Japanese explanations
- Week: Mon 2026-11-16 – Sun 2026-11-22 · VOL.4 · Press time: Mon 2026-11-09
- Lead story: **Die Bundesliga kehrt zurück — Bayern gegen Köln**
- Status: complete (rebuild-B), all gates green on the FIRST rebuild run, visual
  proofread 8/8 pages zero findings (rebuild-B build 1, 2026-11-11). Rebuild 3
  (2026-11-11 07:15 UTC) also passed all gates; this rebuild only carries the
  core build15 Q34 stem correction (see §6). Fix1 rebuild (2026-11-11, D1
  toolbox-pad fix only, all gates green again; independent proof2 pending —
  coordinator to assign).
- **D5 font rebuild applied 2026-11-12 (all gates green — see §3b/§6)**

## §1 Contents

8 pages, 1950×2700, 4 columns. **150 exercises**, continuous numbering 1–150, all in the registry.
Chips: 141 total (P1 10, P2 15, P3 18, P4 15, P5 18, P6 18, P7 12, P8 35; P8 A2 22 / B1 13 / B2 0).

## §2 Deliverables (fix-de-round3 rebuild, 2026-11-13; F3 Haushalt fix rebuild superseded)

- Print PDF: `Die-Lucerna-VOL4-de-ja.pdf` — 16798018 B, sha256 `60942dc9dd9ff8da645b761bde07c4031db866dc5dde5537c01a4be780620a8b`
- Web PDF: `Die-Lucerna-VOL4-de-ja-web.pdf` — 1949457 B, sha256 `579e4a2ac75ac8e57ea25f0db72ba805eb0af43ef74ba65fdda89edf5ba73d90` (53,015 text bytes; < 7 MB)
- Text export: `2026-w47-de-ja.text.md` — 52154 B (43,159 chars, 591 entries, 150 exercises), sha256 `e32d3cb404865284c94bef09f44bbaf9fa32ae5f883ac8b92bc3dcc2f9aaee23` (changed — see the fix-de-minor1 and fix-de-round3 entries below)
- ABSTRACT.txt: 426 B, Japanese, one line, no ASCII double quotes
- 8 SVGs in `svg/`; all gates green (D5 round, see §3b)

Print PDF is 16.0 MB (was 23.9 MB): D5 moved the Latin explanation layer out of the CJK faces, so far fewer CJK glyph subsets are embedded. No gate checks print size; web PDF is the size-checked one.

## §3 Gates (rebuild-B build 1)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150
- measure 24/24 PASS (ja/measure4.log)
- verify TOTAL 150, numbering continuous, SVGs byte-identical after re-run, §1.1 audit True, verbatim OK, P8 floor True, 17 forbidden terms absent
- occlusion 0 flags
- p8 extract 150/150, compare CLEAN, keydiff [137, 138, 139, 150] (expected: the three translate-to-Japanese items + Q150 — see §6)
- freeze (tools/freeze.py, venv interpreter): exit 0, TOTAL added CJK 2,994 — the Japanese explanation layer itself (see §5)
- freeze_direct 8/8 rendered (frozen 144/164/200/166/179/173/163/183); source level shows exactly 4 unaccounted strings, all the documented JP font switch (see §5)
- print/web text layer identical (default word multiset: print 52,873 B / web 52,873 B; -raw normalised: 51,709 B both)
- P8 min font 9.94pt (≥ 9.75pt floor)
- U+2019 full scan over 8 SVGs = 0
- Box titles: 8 instances, all end ≤ 1862.0 (max 1849.1)
- keycheck 149/150: Q150 PREFIX only (extracted '自由課題' vs REG key '自由課題 — 枠のポイントに従おう') — same as all Latin editions
- Visual proofread: all 8 pages rendered at 100 dpi and viewed, zero findings

## §3b Gates (D5 font rebuild round, 2026-11-12 — full re-run on the rebuilt edition; scratch `hidden_files/w47/scratch-d5-de/de-ja/`)

- D5 mechanism: `apply_variant.py --svglib … --target de --reader ja` (mode cjk) on the edition's `svglib.py`; fix2 curly-quote routing installed with it (routing assert `ROUTING FAILURES: 0`, adapted for cjk: `_D5_READER == "cjk"`, Latin sans → news — latin/cjk share routing per CJK-DECISION §1). Install note: `CJK index already JP` (production had already done the SC→JP rewrite; no kinsoku action). Pre-D5 `svglib.py` backed up as `svglib.py.pre-d5`. Pre-D5 baseline verified CLEAN before install: the production dir was copied to scratch and rebuilt with the venv interpreter — freeze baseline **8/8 SVGs byte-identical** to the delivered SVGs (`freeze-pre-baseline.log`). Pre-D5 production snapshot in `scratch-d5-de/de-ja/baseline/` (SVGs + sources, fix1 state). KIT wave 2 check: pre-D5 print SHA matches the KIT (`2638a6e6…`), but the pre-D5 web PDF on disk was sha `a4bbff2b…`, NOT the KIT's fix1 record `161f2dd0…` — the fix1 web PDF had been rebuilt without a KIT sync (same class as de-en/de-fr/de-it/de-nl/de-pt/de-ru). The D5 values above are measured from the actual files on disk.
- Pre-D5 D5 census: **474 Latin-in-CJK-Sans elements** (matches D5-CENSUS-130); quotes defective 0; p8 extract 150/150.
- `run.py` (run3 — see the stale-run2 note in §6): TOTAL **150**, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (`tools/head_check.py`: PASS 0 defects).
- `mechanism/d5_census.py`: **PASS — D5 Latin 0, D5 Cyrillic 0, curly-in-CJK 0**.
- `tools/occlusion_audit.py`: **0 flags** (selftest OK; fixed tool — bare `Noto Sans` runs measured on the non-CJK face, brief §10).
- `tools/p8.py`: extract 150/150; compare vs rebuilt core-de P8: `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 150]` — the same 4 expected reader-language items as rebuild-B.
- `tools/freeze.py`: baseline **8/8 SVGs byte-identical** (venv Pillow 13.0.0 / FreeType 2.14.3); diff pre-D5 baseline vs rebuilt: **added CJK characters 0** (added Latin strings 467 = D5 run-splitting, higher than the Latin readers because CJK titles split per script run).
- `tools/spill_sweep.py`: 32 boxes, 100 candidates, **0 SPILL**, 100 OBSERVE.
- `tools/boxtitle_check.py`: 52 titles, 339 body lines, **0 DEFECT**, 0 OBSERVE, 1 marginal (P7 `　道具箱` +1.0px, within tolerance — the core has the same +1.0 marginal, pre-existing, not a D5 regression; real backup comparison: `scratch-d5-de/scratch-fanout-de/backup/2026-w47-de-ja`).
- `tools/pdf_edge_scan.py`: 8 pages, **0 TOUCH, 0 NEAR**.
- `tools/d5_creambox_audit.py` (pre-D5 baseline vs rebuilt): **PASS 0 defects**; ratios n=532, median 1.009, bold 1.049 / regular 1.000; P8 lines 234→232, footer slack 33.6→33.6px.
- Web/print text layer: `pdftotext` default mode — both **52,775 bytes**, word multiset identical, normalised text exactly identical; `-raw` mode — both 51,704 bytes, identical.

## §4 Language

- Reader: Japanese (日本語). ED_SPACING 7.0, NOTE_WRAP "full", KEYS_HALF=false.
- TYPEMAP: 完成句子→穴埋め / 单选→選択問題 / 句型转换→書き換え / 词汇配对→組み合わせ / 判断对错→正誤問題 / 完形填空→穴埋め文 / 造句→文作り / 对话补全→会話補完 / 翻译→翻訳 / 写作→作文
- Gloss prefix: `注 — ` · Page line: `{n} / {total} ページ` · P8SEP: `— {pg} ページ —`
- Edition line: `ドイツ語週刊　VOL.4　ブンデスリーガ復帰　静かな一週間`
- Footer: `Die Lucerna　ドイツ語週刊 VOL.4　ドイツ語テキスト　日本語解説`
- Chart labels: ['サッカー', '市場', '静かな日']
- Place names: ケルン, マインツ, ニュルンベルク, フライブルク, ライプツィヒ, ハンブルク, グラートバッハ, ブレーメン, シャルケ, シュツットガルト, ザクセン, バイエルン, オランダ
- ABSTRACT.txt (Japanese): "Die Lucerna ドイツ語週刊 VOL.4：ブンデスリーガ復帰（バイエルンはケルンをホームに迎える）、オランダとのネーションズリーグ決戦、悔い改めと祈りの日と死者の日曜日、ケルンのクリスマス市の開場、11月3～8日の欧州戦とブンデスリーガの結果。ドイツ語テキスト、日本語解説、A2～B2レベル、今週の話題の150問。"

## §5 Freeze / CJK handling (read before claiming --strict-cjk)

- `freeze.py diff --strict-cjk` does NOT pass for this edition, by design: the reader-language explanation layer itself adds CJK (2,994 chars: hiragana/katakana/kanji). The en-family precedent (en-ja: 2,092) is to record the total and audit the added characters instead.
- Residual audit run on rebuild-B: kanji-only scan (U+4E00–U+9FFF): 1,358 chars in the 8 SVGs; only 2 outside tr_ja.py values — 色/蛾, both from the core's own `<title>Lucerna 三色蛾</title>` in p1-front.svg, byte-identical in core-de — zero leftover Simplified Chinese in translated text. (Rebuild 3's full CJK audit: all 4,005 CJK characters in the 8 SVGs appear in tr_ja.py's values.)
- freeze_direct.py source level: removed 516 / added 524 literals; the ONLY unaccounted strings at build time were the documented svglib JP font switch from transform.py steps 198–202 (`def _sc_index` → `_jp_index`, `endswith("SC")` → `endswith("JP")`, `"Noto Serif CJK SC"` → `"Noto Serif CJK JP"`, `"Noto Sans CJK SC"` → `"Noto Sans CJK JP"`) — removed 'Noto Serif CJK SC', added 'JP', 'Noto Sans CJK JP', 'Noto Serif CJK JP'. NOTE (rebuild-B, 2026-11-11): ja/freeze-direct.json re-run on rebuild-B lists ONLY the JP switch (removed 1 / added 3) — the 07:30 diagnostic's extra German stem pair is gone, because core-de build15 and this edition now carry the same corrected Q34 stem. Rendered P3 sha8 moved 5c2bc909 → 2dd3b3f2 (the stem); all other frozen counts/sha8 identical: 144/164/200/166/179/173/163/183.
- Interpreter: `tools/venv/bin/python` (PIL 13.0.0) for build and freeze, as required (system python3 PIL 10.2.0 measures 1.1% differently).

## §6 Build history (3 rounds)

- **Build 1** (2026-11-11 ~06:58–07:01 UTC): FAILED 5 gates — occlusion 2 flags (P1 ZAHLEN box column jump: word-of-week wrapped to 2 lines and crossed the hline; ZAHLEN head 457.9px overlapped Q6) + p8 compare SHORT missing [150] (Q150 extractor failure). Print 23,902,660 B.
- **Build 2** (2026-11-11 ~07:06–07:08 UTC): occlusion FIXED (ZAHLEN head → 'DIE WOCHE IN ZAHLEN　数字' 337.9px; word-of-week → 'アドベントカレンダー（24の小窓）。5ページ。' 410.5px, 1 line; Q150 key shortened to '自由課題 — 枠のポイントに従おう'), p8 compare STILL failed missing [150]. Root cause proved by wrap simulation: the page-8 keys paragraph's kinsoku cascade breaks the line right after the Q150 dash ('—') regardless of the key's tail length; the dash loses its trailing space at a CJK line break and join2() glues it to the next character, so the extractor's `" — " in seg` check fails. Shortening the key alone cannot move the break.
- **Build 3** (2026-11-11 ~07:11–07:15 UTC): ALL GATES PASS. Fix: Q150's note removed — EN key 'Marked against the points listed' → '' (vals_ja.json, nested v['values'] addressing; gen_tr diff exactly 1 line). Simulation had tested 14 variants: only removing a whole note (Q147/Q148/Q149's dialogue note, or Q150's note) moves the break; every shorten-only variant failed. Removing Q150's grading note was chosen over a dialogue note because the note is procedural (the H section + MUSTER already carry the instruction) while Q145–149's notes are the answer content of the conjugation exercise. All other editions keep their Q150 note (es/ru/it/pt/nl) — ja is the only edition without it; the REG key is unchanged so keycheck is still 149/150 with Q150 PREFIX, exactly as the Latin editions.
- Flow ends (rebuild 3): P1-headline 1503, P1-fussball 2264, P1-quiz 2523, P2-feature 993, P2-ex 2332, P3-main 916, P3-ex 2333, P4-main 677, P4-ex 2315, P5-main 996, P5-ex 2441 (= core), P6-main 747, P6-ex 2496, P7-A2 1278 / B1 1342 / B2 1306, P8-battery 1409, P8-keys 2473 (bottom 2560, spare 87px).
- **Rebuild-B build 1** (2026-11-11 ~08:43 UTC): ALL GATES PASS first run. Core-de build15 corrected the P3 Q34 stem to the singular form matching key `Weihnachtsmarkt` (D-01, resolved at the core). Edition deleted and re-transformed from the new core with unchanged `tr_ja.py` / `vals_ja.json`; no fixes needed, visual proofread 8/8 zero findings (renders /tmp/ja-rb-proof-*.png). Flow ends identical to rebuild 3 (spare 87px); only delta is that one stem string (P3 sha8 5c2bc909 → 2dd3b3f2; print 23,901,730 → 23,901,736 B, web 2,113,005 → 2,113,024 B, text 51,914 → 51,913 B).
- **Fix1 rebuild (2026-11-11 — D1 only):** P7 DER WERKZEUGKASTEN cream box too short
  (family defect from de-es proof1, reproduced on ja pre-fix): box bottom 754.0, last
  entry `Es ist fraglich, ob ... = まだ不明` baseline 754.8 (clearance −0.8), `fraglich`
  descender ink ~4.7 below the box. Root cause (measured per-edition): the `tbh`
  formula in `content7.py:76` counts `n*29.5+6` per entry but the real advance is
  `20.5 + n*29.11 + 6` (`Page.para` first-baseline offset, 6 entries = +123 missed); ja
  wraps Σlines=8, so clearance = pad − 90.8 and pad 90 gave −0.8. Fix (edition-local,
  `content7.py:76` only): pad 90 → 110 (core-de value), comment rewritten with the
  arithmetic. Verified: toolbox bottom 754.0 → **774.0**, clearance **+19.2**;
  LESERBRIEFE y 770 → 790 (+10.4 unchanged); NOCH EIN WORT ends 1488.5 → **1508.5**
  (+42.9 unchanged, far before the 1548 Sätze rule). 300 dpi toolbox zoom confirms the
  last entry fully inside the cream box; print/web toolbox zooms pixel-identical. No
  text changed: text.md byte-identical (sha a59f7847…); freeze_direct 8/8 rendered with
  frozen counts identical to rebuild-B (144/164/200/166/179/173/163/183); its source
  level still shows the same 4 documented JP-font-switch strings as rebuild-B (§3/§5
  — pre-existing tool-accounting gap in `svglib.py`, identical before/after this fix,
  verified by a pad-90 revert re-run). New deliverables: print 23,901,741 B (+5 B) sha
  `2638a6e62c00da39933a3e921bb74d0d81d6cc00ddf2eff50000c182554f98e1`; web 2,155,095 B
  (+42,071 B — working-tree webpdf.py now embeds the `LucernaNewsreader-Bold` subset,
  21,596 B; same effect as es/fr/it/pt/ko/zh-tw; < 7 MB, text layer identical to print)
  sha `161f2dd0bdfefecffe06944ded2d22f22410daeb321e7bc387c745da9cbcce16`; text.md 51,913 B
  sha a59f7847… (unchanged). All gates green (occlusion 0 flags real run, p8 CLEAN
  keydiff [137,138,139,150], freeze diff +2,994 CJK — the Japanese explanation layer
  itself, keycheck 149/150 — Q150 extractor truncation only, boxtitle 7/7, d2scan 67
  pairs 0 web gaps >0.5pt, P8 min 9.94pt, chips 141, verify TOTAL 150, bent quotes
  U+201C 33 / U+201D 0, Q34 new stem 1x in all five places). Gate logs in
  `hidden_files/w47/scratch-fix-de-toolbox-family/gates-ja/`; build logs in
  `hidden_files/w47/scratch-fanout-de/ja/`.
- **D5 font rebuild (2026-11-12)** — **Cause**: explanation-layer Latin rendered in Noto Sans CJK JP instead of Newsreader (SOP §1.1 font table; CJK-DECISION §1: script-based routing, Latin → Newsreader, no `_READER_LANG` gate). Pre-D5 census: 474 Latin-in-CJK-Sans elements. **Fix (mechanism)**: `apply_variant.py` installed the D5 `_char_font` sans routing on the edition's `svglib.py` with `_D5_READER = "cjk"` (fix2 included). No German text, fact, or key changed; no wording changed at all. **Four D5-caused defects, all fixed in source and rebuilt**: (1) P1-fussball head `EINE WOCHE, ZWEI STIMMUNGEN` — HEAD TOO WIDE at 25pt; `content12.py:124` 25→22pt (411.8px fits the 422.5px column). (2) P1 sommaire title `IN DIESER AUSGABE　今号の内容` — +7.5px; `content12.py:89` 24→22pt (374.0px fits 400.5). (3) P2 box title `DIE STILLE WOCHE　静かな一週間` — +19.1px; `content12.py:221` 24→22pt (384.7px fits 400.5). (4) P5 box title `ADVENTSWÖRTER　待降節の言葉` — +11.4px; `content56.py:46` 24→22pt (377.6px fits 400.5). **Stale-run2 note (process, not content)**: the first post-fix rebuild (run2) was dispatched in the same tool batch as the source edits and ran against the pre-edit sources — its P2 title was still 24pt, so boxtitle/creambox still failed that one item. A clean re-run (run3, after the edits were on disk) shows the P2 title at 22pt and all gates green; the run2 log is kept as `run2-stale.log`. Lesson: never dispatch edits and the rebuild in the same batch. **Verification**: full gate re-run (§3b) — census 0, occlusion 0, p8 CLEAN, freeze 8/8, added CJK 0, spill 0, boxtitle 0 (real backup), edge 0, creambox PASS, print/web text layers identical in both modes. The P1 masthead subtitle never collided with the headline in this edition; no P8 battery head overflowed.
- **Reproof fix rebuild (2026-11-12)** — **Cause**: independent reproof of the D5 rebuild found 9 items (F7 major, rest minor) — see `hidden_files/w47/scratch-reproof-w47-de/PROOF-NOTE.md`. **Fix (in source, then rebuilt)**: F1 — P5 UND SIE prompt gained the advent-calendar question; F5 — P1 DIE WOCHE IN ZAHLEN box regained the three German sentences (+ reader gloss). Knock-on: the 9-line box (402px) broke the P1-headline flow (ended 1921 > 1828, occlusion 11 flags); box items 20.5→18pt, flow ends 1554 (= core/es). Gates: build ALL GATES PASS; boxtitle 0 DEFECT; spill 0 SPILL; edge 0/0; census-patched PASS (P5 cjk_sans +2 = the longer F1 prompt's run split, verified); head_check PASS; text.md dry-run diff 4 lines, 0 dropped. **Verification**: full gate re-run (logs in `hidden_files/w47/scratch-fix-de/logs/`); per-edition entry in `scratch-fix-de/FIX-LOG.md`. New deliverables: print 15,960,325 B sha `1b91ff1f9ca0…`; web 1,935,367 B sha `dfb0c403f2f4…`; text.md 52,118 B sha `15aa6bc8921b…`.

- **F3 Haushalt fix rebuild (2026-11-13)** — **Cause**: de-family independent reproof (worker 4c143a3c, F3 medium) — P6 `der Haushalt` mistranslated as household budget (`家計`): the article is about the federal budget Bundeshaushalt 2027 ("11 月 27 日表决"); the other 8 editions all say budget, and this edition's own Q92 answer already says `2027年度予算`. **Fix (in source, `content56.py` only, 3 visible places)**: band head `静かな一週間と家計` → `静かな一週間と予算`; gloss `der Haushalt = 家計` → `der Haushalt = 予算`; debate sentence `家計：電気税がどれだけ下がるかは未定` → `予算：電気税がどれだけ下がるかは未定` (same string in the height-calc line and the render line — both changed). Plain `予算` chosen over the proofreader's `予算（国家予算）`: same 2-character length as `家計` (zero layout shift — P6 col3 ends 1206.02, identical to the D5 build) and consistent with Q92's `2027年度予算`. No other content touched. **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); only `p6-vertiefung.svg` changed (other 7 SVGs byte-identical; p6 text diff exactly the 3 changes, 262 texts both sides, 0 `家計` left); web PDF rebuilt from the new SVGs. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-ja-ko1/de-ja/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137,138,139,150]; occlusion 0 flags; boxtitle 0 DEFECT / 0 OBSERVE / 1 marginal (P7 `道具箱` +1.0px, core same +1.0, pre-existing since D5); spill 0 SPILL / 100 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 3,006 (reader layer; unchanged vs pre-fix by the multiset proof below); print/web text layers multiset-identical (35,665 non-space chars each); pre/post print multiset differs ONLY by 家×3/計×3 → 予×3/算×3; text.md re-exported from source, diff exactly 3 lines (L703/L721/L753), 591 entries / 150 exercises, byte size unchanged (52,118 B). New deliverables: print 15,960,377 B sha `0d44f823eca9…`; web 1,935,434 B sha `d7df759a75f5…`; text.md 52,118 B sha `1e156f8bf8ca…`. Not committed / not pushed (coordinator inserts).

- **fix-de-minor1 rebuild (2026-11-13)** — **Cause**: de-family round-2 independent reproof (worker 7877e6e8, §8.4 round 2) — C-1/C-2 (core German text, all 11 editions). **Fix (in source, then rebuilt)**: C-1 — P3 lead `die ersten Weihnachtsmärkte` contradicted the Hafenmarkt (open since 13 Nov, same article §2): P3 lead → `zwei große Weihnachtsmärkte` (same length, zero layout shift); the P5 lead carried the identical false claim and was fixed with the same wording; Q34 `Am Montag öffnet in Köln der erste ___.` → `Am Montag öffnen in Köln der Markt am Dom und der Markt der Engel, zwei große ___.` (word-box word and answer key `Weihnachtsmarkt` → `Weihnachtsmärkte`); Q80 `Am 16. November öffnen in Köln die ersten Weihnachtsmärkte.` → `Am 16. November öffnen der Markt am Dom und der Markt der Engel.` (answer stays `Richtig`). Q29 left unchanged (A2-acceptable per the brief; changing it would change the answer key). C-2 — P5 1903 calendar `Die Kinder konnten die Fenster mit Bildern überkleben.` → `Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben.` (the 1903 Lang/Kepler edition was windowless cut-and-paste). The `überkleben` gloss entry is left in place (the brief's fix is the sentence only; flagged to the coordinator). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p3, p5, p8 (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-fix-de-minor1/2026-w47-de-ja/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 52 titles, 343 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal (P7 `　道具箱` +1.0px, core same +1.0, pre-existing since D5); spill 0 SPILL / 100 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 2,978 (reader layer; the shift vs the previous round's count is P3/P5/P8 re-wrap from the longer Q34/Q80 sentences, not content — the multiset proof below is authoritative), added Latin strings 154; print/web text layers multiset-identical (35,716 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: `die ersten`→`zwei große` ×3, `erste`→`Markt am Dom und der Markt der Engel` ×2, `Fenster mit Bildern überkleben`→`Bilder ausschneiden und auf den Kalender kleben`, footer/Q34-key changes where applicable); text.md re-exported from the fixed sources, diff exactly 7 lines (L309 P3 lead, L387 box, L389 Q34, L573 P5 lead, L577 C-2, L693 Q80, L1165 P8 answers Q34 key), 591 entries / 150 exercises. New deliverables: print 15,960,412 B sha `ec7c841964f7…`; web 1,935,469 B sha `766cc50e4cce…`; text.md 52,187 B sha `e85704db941c…`. Not committed / not pushed (coordinator inserts).

- **fix-de-round3 rebuild (2026-11-13)** — **Cause**: de-family round-3 independent reproof (§8.4 round 3) — R3-F1/R3-F2 (see below). **Fix (in source, then rebuilt)**: R3-F1 — the C-2 fix (fix-de-minor1) removed `überkleben` from the P5 1903 sentence but left the orphan gloss entry in the P5 gloss (`content56.py:23`); SOP §8.1 requires every glossed word to occur in the text, so the ` · überkleben …` segment was deleted from the P5 gloss (gloss shortens by one entry, layout-safe). **Verification**: rebuild via `tools/run_build.py` (RC 0, TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE); changed SVGs: p5 only (all other SVGs byte-identical vs pre-fix); web PDF rebuilt from the new SVGs via `tools/webpdf.py`. Full gates re-run (logs in `hidden_files/w47/scratch-reproof-de-round3/2026-w47-de-ja/fix-round3/`): verify TOTAL 150 + SVGs byte-identical after re-run + §1.1 audit True; p8 extract 150/150, compare CLEAN keydiff [137, 138, 139, 150]; occlusion 0 flags (selftest OK); boxtitle 52 titles, 341 body lines, 0 DEFECT, 0 OBSERVE, 1 marginal; spill 0 SPILL / 100 OBSERVE; edge 8 pages 0 TOUCH / 0 NEAR; head_check PASS 0 defects; D5 census PASS (Latin 0, Cyrillic 0, curly-in-CJK 0); freeze diff exit 0, added CJK 2974, added Latin strings 153; print/web text layers multiset-identical (35,699 non-space chars each); pre/post print multiset differs ONLY by the intended character swaps (word-level diff checked: gloss `überkleben …` entry removed); text.md re-exported from the fixed sources, diff exactly L585 P5 gloss, 591 entries / 150 exercises. New deliverables: print 16,798,018 B sha `60942dc9dd9f…`; web 1,949,457 B sha `579e4a2ac75a…`; text.md 52,154 B sha `e32d3cb40486…`. Not committed / not pushed (coordinator inserts).
