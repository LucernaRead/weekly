# WEEKLY-KIT — Lucerna Japanese × Traditional Chinese (JA×ZH-TW), VOL.3, W46, 9–15 Nov 2026

Slug: `2026-w46-ja-zh-tw`. Target language: Japanese (articles frozen
byte-identical from the W46 JA core). Reader language: 繁體中文 (the
entire explanation layer). Source: the pristine W46 core build
`hidden_files/weekly-report-w46-ja-build/` (never modified); this
edition was produced by the dedicated generator
`hidden_files/w46/gen_ja_zhtw.py` (run with plain python3; it writes
the build dir `hidden_files/weekly-report-w46-ja-zh-tw-build/` directly,
no transform.py) from the pristine core build (exact-literal
replacements only; re-runnable).

## §1 Pairing badge and footers

- Masthead geometry (task + tools/README lesson 20): wordmark baseline
  y=262 (core position, kept), subtitle y=316, badge inserted at
  (975,356) 19pt BRICK `#a4553a`, strapline y=390, double rules 406/413,
  dark band y=424.
- Badge: `日語正文 · 繁體中文講解 — 給繁體中文讀者的版本`.
- Footer every page: `Lucerna · 日語週報 VOL.3 · 正文日語 · 講解繁體中文`; page line `第 N 版 / 共 8 版`.
- Top strip middle segment: `每週一期` (replacing the core's Chinese).
- Gloss prefix: `譯注｜`. P8 separators: `— 第N版 —`.
- Registry type names: 完成句子 / 單選 / 詞彙配對 / 造句 / 判斷對錯 / 完形單選 / 翻譯 / 寫作.
- P1 dark-band right lines (繁體中文, short form): `週日是七五三` /
  `紅葉最佳觀賞期向南移動 · 詳見第 6 版`.

## §2 What changed vs the core

Only the explanation layer: glosses, notes, answer notes, furniture
halves, band subtitles, the P2 season-word glosses, the P7 error-clinic
notes, frame breakdown, readers'-corner disclosure (ONE 繁體中文
disclosure replacing both the Japanese and Chinese lines, per the W45
coordinator ruling: "編輯部示例信，非真實來信。截稿前未收到真實來信與最佳作文；兩者將刊登於VOL.4。請把你的來信寄來。"), phrase
translations + page tags, teaser head, and the P8 E-zone re-aiming:
items 137–138 keep their Japanese stems with 繁體中文 keys;
items 139–140 have 繁體中文 stems with the Japanese keys byte-identical
to the core. All Japanese article/stem/option/letter/figure strings are
frozen; all facts and sources are the core's (§3 of the core KIT).

## §3 Content and counts

Same 8 pages and 150 exercises as the core (A2 46 · B1 75 · B2 29;
by page 10/18/18/18/18/18/12/38). P8 model text 154 characters.
Images: same 3 reused PD/CC0 images as the core (maple P1, Hiroshige
III print P3, stadium P4); credits in the core build's
`assets/CREDITS.md`.

## §4 Gates (recorded in hidden_files/w46/ja-gates.log)

- Builder self-check: no FLOW OVERFLOW / HEAD TOO WIDE warnings.
  P7 teaser ends y=2442.0 (< 2540); P8 keys-flow last baseline
  y=2514.92 (< 2540).
- Occlusion audit: 0 flags (`hidden_files/w46/ja-zh-tw-occlusion.json`;
  selftest OK).
- P8 compare: CLEAN, 150/150 noted, keydiff=[138] — exactly the re-aimed E-zone keys (expected;
  see §2). (`hidden_files/w46/ja-zh-tw-p8compare.json`).
- Freeze diff --strict-cjk: FAIL, 839 added characters — see adjudication below
  (`hidden_files/w46/ja-zh-tw-freeze.json`).
- Strict-CJK adjudication: `freeze.py --strict-cjk` reports FAIL with
  839 added characters — ADJUDICATED: every added CJK character was
  checked against the MAP values + TC furniture strings + the core
  repertoire; 0 unexplained characters, and 0 Simplified-only
  characters remain in the edition SVGs
  (`hidden_files/w46/ja-zh-tw-freeze.json`, analysed 2026-11-02).
  Strict-CJK = 0 is not achievable for a Traditional Chinese
  explanation layer and is not claimed.
- Kinsoku: TC NO_START extras (］｝〉》％) added by the plumbing edit;
  line-start scan clean. TC face verified rendering on P1/P7/P8 cards
  (font-family "Noto Sans CJK TC").
- Web PDF: `Lucerna-VOL3-ZHTW-web.pdf`, 2,875,035 bytes (< 7 MB),
  44,817 pdftotext bytes, identical to the print PDF text. Print PDF
  kept: `Lucerna-VOL3-ZHTW.pdf` (27,063,356 bytes).
- Visual pass: P1 card checked (badge geometry, gloss, numbers box);
  P7/P8 cards checked for this edition's risk areas (disclosure,
  keys fit). Kinsoku: the Japanese body text is the core's (0 line-start
  hits).
- `.text.md` exported from the builder SVG manuscript with
  `hidden_files/w46/make_textmd.py` (never from PDF).
- Proofread status: builder-complete; finalisation requires the
  independent proofread per SOP §8.4. This KIT does not declare the
  edition final. Nothing posted to Discord, nothing sent to chat,
  weekly repo untouched.

## §5 Reproduction

```
cd hidden_files/w46
python3 gen_ja_zhtw.py      # dedicated generator; writes the build dir directly (no transform.py)
cd ../weekly-report-w46-ja-zh-tw-build
tools/venv/bin/python run.py         # one process, shared registry
tools/venv/bin/python render.py      # cards + print PDF
tools/venv/bin/python webpdf.py <svg dir> <web pdf>   # from tools/
```

## §6 Fix history

Build method: this edition was NOT produced by the shared
  transform.py pattern. A dedicated generator
  `hidden_files/w46/gen_ja_zhtw.py` copies the pristine W46 core build
  and applies (a) TC face plumbing adapted from the W45 zh-tw
  transform §§2–3 (svglib gains _tc_index/_IDX_TC and a face="TC"
  parameter; bslib4 threads face through band/shead/para; footer with
  face="TC"; TC extras in NO_START), (b) a 179-entry Traditional
  Chinese MAP (`hidden_files/w46/maps/zh-tw.json`, built with OpenCC
  s2t over AST-extracted literals, with a Japanese-word guard,
  JP-shinjitai-only guard, and post-pass 爲→為; W45 precedents
  honoured: 第3号 stays, 數字看本週, 写真 captions stay Japanese,
  為 not 爲), (c) face="TC" call-site edits for explanation calls
  only (Japanese body stays JP face), and (d) the standard masthead
  geometry + badge. Two mixed kana+Chinese notes missed by the
  converter ("地点＋へ＋动词", "动词名词化时要加「こと」。") were
  found by an SC-only-character scan and added to the MAP. The 12.9pt
  keys-font patch was NOT needed (keys end 2514.92 at 13.3pt).
  Keydiff=[138] only: item 137's key has no Simplified-only
  characters, so its Traditional form is byte-identical to the core.

Fix record — Round 1 proofread defects (fix worker, 2026-11-02/03).
Round 1 verdict: FAIL on inherited D-CORE-01 + D-CORE-02 and on
zh-tw-only D-ZHTW-01 + D-ZHTW-02. Both fixed
at the source in the core build / this edition's ABSTRACT.txt; this
edition was fully re-rendered through the generator pipeline in §5 and re-gated
on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix/`). Round 2 independent proofread still
required.

- D-CORE-01: core `svglib.py` `wrap()` gained a NO_END kinsoku block
  (opening brackets `（「『〔【《〈([` never end a line); md5
  d73e23b365676c3618d7e060b835eb4d →
  74177544422fe677639d769cd80499fb, and `CANON_SVGLIB_MD5` in `gen_ja_zhtw.py` was updated to the new value. The §5
  "pristine core build" wording now refers to the pre-fix state; the
  current build carries the NO_END fix. P1 item 8 and P3 item 32 now
  keep `（月）` / `（土）` intact on one line (see core KIT §11 for the
  line-split quotes); no other text moved.
- D-CORE-02: `ABSTRACT.txt` closing rewritten to practice framing,
  rest verbatim. Before tail: `共150道練習題，透過真實日本新聞學日語。` After tail:
  `共150道以本週話題為素材的練習題。` (Full before/after in
  `hidden_files/w46/ja-fix/abstracts-before-after.txt`.)

- D-ZHTW-01/02 + same-class residue: the MAP
  (`hidden_files/w46/maps/zh-tw.json`) was missing the two listed
  strings. Fixed in the MAP (179 → 187 entries): `得到东西的场所用「で」。`
  → `得到東西的場所用「で」。` (P7 clinic); `在酉の市买熊手` →
  `在酉の市買熊手` (P8 key 42). The mandated full Simplified-only
  scan of the pre-fix zh-tw SVGs found 6 FURTHER same-class residue
  strings, also fixed via the MAP: `看的场所用「で」。` →
  `看的場所用「で」。` (P7 clinic); `场所用「で」` → `場所用「で」`
  (P8 key 135 note); `2026年没有三の酉` → `2026年沒有三の酉` (P8 key
  33 note); `新小结是美ノ海` → `新小結是美ノ海` (P8 key 59 note);
  `「千歳飴」受欢迎` → `「千歳飴」受歡迎` (P8 key 148 note);
  `口号是「静かだけど、冒険中。」` → `口號是「静かだけど、冒険中。」`
  (keys 103 and 128). The verdict's claim that its full scan found
  exactly 2 strings is therefore REFUTED on the pre-fix evidence
  (see `hidden_files/w46/ja-fix/sc-occurrences-BEFORE.txt`). Post-fix
  adjudicated scan (`sc_scan.py`, `sc-scan-AFTER.json`): 0 residue
  characters, 0 residue strings, all 8 Traditional forms present;
  the 21 remaining s2t-differing characters are legitimate Japanese
  shinjitai / deliberate keeps.
- P7 and P8 cards visually checked at full frame: clinic notes and
  P8 keys 33/42/59/103/128/135/148 render in Traditional with no
  overflow, overlap, or tofu.

- Re-gate (final artifacts): freeze diff exit 1 adjudicated: added-char set identical to Round 1 (158 distinct, all Traditional/Japanese repertoire); +10 instances vs Round 1, exactly the 8 conversion sites below; p8 compare CLEAN
  150/150, keydiff [138]; occlusion 0 flags; kinsoku scan
  (proofreader's definitions) start 0 / end 0 / orphan 0; counts 150
  (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38), stems
  and keys 1–150 complete, P6 bars 1020/780/720/480 with all labels
  + practice-data label, P7 phrases 2× verbatim, keys-flow end-y
  2514.9; web PDF 2,872,565 bytes (< 7 MB), 44,817 pdftotext bytes,
  byte-identical to the print PDF (27,062,370 bytes); text.md 44,192 bytes.
  P1 and P3 cards visually checked at full frame: both rewraps
  correct, no overflow/overlap.

Fix record — Round 3 proofread defect D-KEY-42 (fix worker, 2026-11-03).
Round 2 verdict: FAIL on D-KEY-42 only (all Round 1 defects confirmed
fixed). Fix applied at the source in the core build and propagated by
regeneration; this edition was fully re-rendered through the pipeline
in §5 and re-gated on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix-round3/`). Round 3 independent proofread
still required.

- D-KEY-42 (P8 key 42 omits a stem piece, BLOCKING, all 11 editions):
  P3 stem item 42 is `酉の市で / 熊手を / 買います → ___` (造句).
  The printed P8 key omitted the location piece `酉の市で`, while
  all 7 sibling 造句 keys (39, 40, 41, 133, 134, 135, 136) include
  every stem piece. Source: regenerated by `hidden_files/w46/gen_ja_zhtw.py` from the fixed core (MAP untouched, 187 entries); this build's `content34.py:95` carries the new key with the Traditional note.
  Before (P8 key 42): `42. 熊手を買います。 — 在酉の市買熊手`
  After (P8 key 42): `42. 酉の市で熊手を買います。 — 在酉の市買熊手`
  The reader-language note is UNCHANGED. The P3 stem is unchanged.
  No SVG/PDF was hand-edited; no other string was reworded.
  Fit: single line, width 292.8 of 434 (slack 141.2), y unchanged 1428.984.
- Change isolation: SVG text-multiset diff vs the pre-fix snapshot
  shows exactly one changed text in this edition (the key-42 line
  );
  hash check over the 132 edition files shows only the P8 SVG, both
  PDFs, and the .text.md changed in this edition (P1–P7 SVGs and
  ABSTRACT.txt byte-identical). Round 1 fixes survive (kinsoku 0/0/0,
  abstracts unchanged, zh-tw conversions intact where applicable).
- Re-gate (final artifacts): freeze diff exit 1 adjudicated legitimate: added-char set and total (158 distinct, 849 instances) byte-identical to Round 2; p8 compare CLEAN 150/150, keydiff [138] (adjudicated redirect, as Round 2); occlusion audit 0 flags
  (synthetic selftest passed); kinsoku scan start 0 / end 0 / orphan 0;
  counts 150 (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38),
  stems and keys 1–150 complete, sibling 造句 keys unchanged and
  complete, P6 bars 480/720/780/1020 with all labels + practice-data
  label, P7 phrases 2× verbatim, keys-flow end-y 2514.9;
  web PDF 2,872,569 bytes (< 7 MB), 44,829 pdftotext bytes, byte-identical to the print PDF (27,062,375 bytes); text.md 44,204 bytes. P8 card visually checked at full frame: key 42
  correct, no overflow, overlap, or tofu.
