# WEEKLY-KIT — Lucerna Weekly RU×JA（俄语正文 + 日语讲解）, W45 VOL.2

- **Edition**: 2026-W45 · VOL.2 · ロシア語テキスト · 日本語の解説 — 日本語読者のための版
- **Pairing**: target = Русский (ru) · reader native = 日本語 (ja)
- **Dates**: 2026-11-02 – 2026-11-08 (W45), issue date Monday 2 November 2026
- **Status**: BUILDER-COMPLETE — all self-check gates pass (below). NOT finalized:
  finalization requires a separate independent proofread. No repo insert, no
  Discord post, no chat card/PDF dump, no cron, no subagent was used or created.
- **Source core**: files/weekly-report-w45-ru-core/ (Russian body text frozen;
  only the explanation layer rewritten into Japanese, directly from the Russian
  originals — no intermediary language is used anywhere, and the banned
  intermediary term appears nowhere in the edition, this KIT, or the build code;
  the W43 method name was renamed `bridge()` → `expl()` as in the W43 RU×JA build)
- **Build dir**: hidden_files/weekly-report-w45-ru-ja-build/ (copy of the W45 RU
  core build, OUT repointed to files/weekly-report-w45-ru-ja/)
- **Totals**: 150 exercises = A2 51 · B1 75 · B2 24; per page 10/18/18/18/18/18/12/38
  — identical to the core registry. Model writing text = 84 words (brief: 80–100).

## §1 Method

1. Pre-flight duplicate check: neither files/weekly-report-w45-ru-ja/ nor
   hidden_files/weekly-report-w45-ru-ja-build/ existed; no ru-ja build process
   was running — proceeded (coordinator rule: no in-flight writes + quiet
   re-check = safe start; here there was nothing at all).
2. `tools/freeze.py baseline` on the W45 RU core build: **8/8 SVGs byte-identical**
   (p1 8bfcb7e2, p2 5b35f1d7, p3 8be9ba7f, p4 9d699050, p5 f49d0ed8,
   p6 8559d61d, p7 961119d6, p8 2738ae04); shipped core SVGs re-hashed unchanged
   after this build (same 8 prefixes — core untouched throughout).
3. Copy of the core build repointed (all 6 OUT/BASE occurrences of
   `weekly-report-w45-ru-core` → `weekly-report-w45-ru-ja`; zero residual core
   references in any .py). Pre-translation run reproduced the core's CJK totals
   per page exactly (117/189/124/119/105/136/245/806) and P7 col3 ends 1727.58.
4. svglib.py replaced wholesale with the canonical JA version (§7); the copy was
   never edited. No module was ever imported or run inside the core build
   directory (README #11); all runs went through the build's single one-process
   driver run.py (README #7).
5. Explanation layer rewritten by a whole-line / exact-unique-literal transform
   (scratch/map_ja.py + scratch/transform_ja.py): **234 pairs, 465 replacements**,
   applied longest-old-first with a per-pair count assertion (every pair found
   ≥1 time) and a totality pre-check (every CJK literal in the six sources was
   either a deliberate keep or contained a pair-old — 0 unmapped). Bare-text
   substitution only, never repr literals (README #18); no AST byte-offset
   splicing (README #17). Two transform-script defects were caught by its own
   assertions and fixed before any write (a missing pair, a duplicate pair).
6. Render: render.py produced cards + print/web PDFs (filenames carry the -JA
   suffix per the W45 sibling convention: Lucerna-VOL2-JA.pdf / -web.pdf).

## §2 JA column svglib standard

- svglib.py = canonical JA version, md5 **d73e23b365676c3618d7e060b835eb4d**,
  byte-identical to the W43 RU×JA build's svglib (diff empty) — JP faces +
  kinsoku oidashi + SEAM_SLACK seam repair, unedited (README #19: no NO_START
  extension was needed — the Russian body uses no ASCII closers that strand at
  line starts; the line-start scan in §6 confirms 0).
- The single CJK line inside the svglib SOURCE is an illustration docstring
  (`for 重阳`) — a code comment, never rendered. Rendered SVGs contain no svglib
  text of any kind; all rendered CJK comes from the Japanese explanation layer.

## §3 Furniture (JA column, verbatim from the shipped W43 RU×JA edition)

- P1 badge (see §3a for the slot record): «ロシア語テキスト · 日本語の解説 — 日本語読者のための版»
- P1 top band centre: «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 毎週一号 · ロシア人が読んでいるロシア語を読む»
  (first segment is the core's frozen Russian; left VOL line and right date line
  stay Russian, as in W43)
- Masthead: **Lucerna** (no article for Russian); strap y=330 kept Russian:
  «РУССКАЯ ГАЗЕТА · VOL.2 · ПРАЗДНИК · СКИДКИ · ФУТБОЛ»
- Footer left (every page): «Lucerna · ロシア語週刊 VOL.2 · 本文はロシア語 · 解説は日本語»
- Footer right (page line): «N ページ（全 8 ページ）»
- gloss() prefix: «解説 — »; the first expl() after the P1 headline carries the
  «解説 — » prefix inside its value (shipped ×JA convention)
- Section heads: Russian original · Japanese short title (e.g. «ЖИЗНЬ · 生活»,
  «КУЛЬТУРА · 文化», «СПОРТ · スポーツ», «МОЛОДЁЖЬ · 若者», «БОЛЬШОЙ РАЗБОР · 深掘り»,
  «ЯЗЫК · 言語», «ТЕСТ И ОТВЕТЫ · テストと答え»)
- P8 header: «ОТВЕТЫ · 全解答と解説（1–8ページ）»; right note
  «各問に日本語の解説つき · ✓ は模範文のある問題»
- P8 page separators: «— N ページ —» (×8); dash-style answer lines «N. key — note»,
  writing item «N. ✓ note» (RU family dash style, answer-generation code
  byte-identical to the core's apart from the separator string and the
  type-name check `== "作文"`)
- Exercise-type names (registry, 1:1 with the core): 空所補充 54 · 選択 42 ·
  語と意味を結ぶ 20 · 組み合わせ 12 · 書きかえ 4 · 空所補充・選択 13 · 翻訳 4 ·
  作文 1. Printed instr forms: 空所補充 / 組み合わせ / 書きかえ / 翻訳 / 作文 /
  語と意味を結ぶ / 日付と出来事を結ぶ / チームと相手を結ぶ
- Japanese Russian-grammar terminology used throughout: 生格 (genitive), 造格
  (instrumental), 与格 (dative), 不定形, 男性, 命令形

### §3a Badge slot — three-way measurement (for the coordinator)

- **This edition**: badge string verbatim from W43, at **(975, 372), 19.5pt bold,
  BRICK #a4553a, centred** — true ink span 717.82–1232.07 (width 514.25),
  ink top 355.0, ink bottom 374.0. Clearances: strap ink bottom 338.75 → badge
  top = 16.25 clear; badge bottom → rules at 392/401 (top edge 390.5) = 16.5
  clear; dark band top 424 = 50 clear. Same-baseline scan 0, occlusion audit 0,
  P1 card visually confirmed clean.
- **W43 shipped RU×JA**: identical string, identical slot (975, 372), identical
  size/weight/color — measured ink span 717.82–1232.07, byte-identical geometry.
- **README #20**: the (975, 574), 22pt BRICK insert describes FR/IT-as-target
  cores (whose y=372 is a frozen body strapline) and the W45 ru-de/ru-es inserts
  that followed it. It does NOT describe the RU-target ×JA column, whose own
  shipped precedent (W43 RU×JA, verified in both its shipped SVG and its build
  source) replaces the y=372 subtitle in place at 19.5pt BRICK. This edition
  follows the W43 same-pair shipped practice, not the §20 generalization —
  the same adjudication already accepted for the W45 372 family
  (ru-en/ru-fr/ru-it/ru-pt). No frozen Russian BODY text was deleted: the
  replaced y=372 line is the masthead furniture strapline, itemized in §4.

## §4 Freeze adjudication (Cyrillic token multiset, rendered SVGs)

- P2–P7: **zero delta** (counts 443/338/306/316/354/397 — P7 is 397 = 397 after
  the §8 fix; the pre-fix 397 → 396 delta was the word-box headword, restored).
- P1: differs by exactly the badge-slot strapline, itemized in full — the
  replaced y=372 line «ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК —
  НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ» contributes one occurrence each of ЕЖЕНЕДЕЛЬНАЯ,
  ДЛЯ, ИЗУЧАЮЩИХ, РУССКИЙ, ЯЗЫК, НАСТОЯЩАЯ, РОССИЯ (1→0) and one each of ГАЗЕТА
  (2→1), ПО (3→2), РУССКИ (2→1); core total 400 → edition 390. No other
  Cyrillic token differs anywhere on P1. This is the documented W43 RU×JA
  accommodation (§3a), not a content loss.
- P8: differs by exactly the separators — СТРАНИЦА 8→0 («— СТРАНИЦА N —» →
  «— N ページ —»); core total 641 → edition 633. No other Cyrillic token
  differs on P8.
- Russian body text multiset equals the core's apart from the two filed
  furniture items above. `tools/freeze.py diff`: string churn is explanation
  layer only (+22/−22, +35/−33, +23/−22, +23/−22, +23/−22, +32/−30, +38/−38,
  +174/−168 per page); total added CJK characters 2343, all Japanese
  explanation layer (top added chars per page are kana/kanji of the new notes).
  (Coordinator KIT-only correction 2026-10-27: builder draft wrote 2342;
  independent proof and coordinator re-measurement both give per-page
  185/243/171/159/167/209/285/924 = 2343, and freeze.py itself prints
  TOTAL 2343. Paper unchanged; see §11 adjudication note.)
- Level chips per page, core = edition: 10/15/16/15/15/18/12/35 (match_set prints
  one chip per set, hence P2 15 not 18 and P8 35 not 38 — same in both builds).

## §5 Answer-key gate (tools/p8.py compare)

- `p8.py compare`: **CLEAN** — core 150 noted, edition 150 noted, missing=[],
  extra=0, uncertain=[].
- Tool-reported keydiff [83, 137, 138, 148]. Registry-level truth by dash-parse
  (key = text before the FIRST « — », per the brief): **real keydiff = [137, 138]**.
  - #137 翻訳 key: «11 月 4 日星期三放假。» → «11月4日水曜日は休み。» (the key IS
    the reader-language translation — legal class, as W43 RU×JA #137/#138)
  - #138 翻訳 key: «促销码就是折扣码。» → «プロモコードとは割引コードのことだ。»
    (same class)
  - #83 and #148 are p8.py extraction artifacts (README #13 class): the tool's
    paren branch attributes trailing «（…）» note text to the key whenever the
    note ends in full-width parens. Dash-parse of the printed lines gives true
    keys #83 B = B («83. B — 週の休みは3日（水・土・日）») and #148 A = A
    («148. A — его = プロモコード（男性）»), identical to the core's keys;
    only the notes changed language, as they must.
  - #150 作文: tool key «✓» identical in both; note changed language
    («模範文はこのページの H 欄（84 語）») — same class as W43's #150, not flagged.
- Reverse-direction translation items #139/#140: Japanese source sentences printed
  («土曜日、クラスノダールはCSKAと対戦する。→ ___»,
  «みなさん、民族団結の日おめでとう！→ ___»), Russian keys byte-identical to the
  core. The #139 stem uses katakana transliteration (クラスノダール/CSKA) exactly
  as the core's stem used Chinese transliteration — the core's design gives
  transliterations, not Cyrillic spellings, so the student must still produce
  ««Краснодар» … с ЦСКА» from the transliteration.

## §6 Geometric + content gates

- `tools/occlusion_audit.py` (selftest OK: all 6 planted classes fire, clean
  controls silent): **edition 0 flags, core control 0 flags, NEW vs core 0**
  (final run scratch/occl-ed2.json; earlier run scratch/occl-ed.json also 0).
- Same-baseline ink scan (README #10, true PIL ink boxes): **0 flags** on all
  8 pages at <5-unit gaps, including the P1 top band and the badge row.
- P6 chart, element level (README #12): labels, values and bars at
  core-identical positions (labels x=65 at y 1634/1680/1726/1772; values
  34% x=1299, 28% x=1193, 22% x=1087, 16% x=981 — each 14 units past its bar
  end; bars 600/494/388/282 = round(v·600/34) for 34/28/22/16%). Text-ink vs
  later-drawn rect overlap check: **0 overlaps**. The RU P6 chart has no
  ES-style frozen overprint — 0 overlaps is the correct, expected result.
  The bilingual honesty caption is preserved (Russian frozen + Japanese
  «これは編集部の練習用データで、実際の統計ではありません。」).
- P7 readers' corner (no fabrication, core example + disclosure preserved):
  box geometry **identical to the core, value for value** — col3 rect bottoms
  1008.08 / 1242.58 / **1727.58** in both SVGs; phrases rule y=1756 in both
  (28.42 clear of the box bottom); P7 rect multiset diff = 0. The Japanese
  disclosure states all three facts in-page: no real letters arrived, no best
  P8 essays arrived, the letter is the editor's example, and the promise
  carries to VOL.3 («本物の投書も優秀作文も未着のため、編集部の例文です。約束は
  VOL.3 へ。」, 2 lines like the core's disclosure). The ru-en-style
  box-bottom-contact adjudication does not arise here as a new issue: geometry
  is core-identical and all text is readable (P7 card visually confirmed).
- Gloss counts (split on · itself, README #21): source gloss() items core = edition
  = **26** (content12 9, content34 9, content56 8, content7 0); rendered gloss
  boxes per page core = edition (P2 3, P3 2, P4 1, P5 2, P6 1); P1's single
  rendered «解説 — » line is the first-expl prefix per the shipped ×JA
  convention (§3), not a gloss box.
- Image payloads: **byte-identical to the core on all 8 pages** (base64-decoded
  SHA-256 per image element, same geometry).
- P7 golden sentences: all 8 Russian quotes byte-identical to the core,
  **each occurring exactly 2×** (article page + P7), with page tags matching
  their article pages: {1:2, 2:1, 3:1, 4:1, 5:1, 6:2} (distribution verified
  per page, not just in total). The 4 error-clinic wrong sentences occur 1×
  each, as in the core — they are clinic examples, not golden sentences.
- Residue scans: Chinese explanation residue = **0** (core Chinese marker strings
  «缩短的工作日 / 中文讲解 / 参考答案 / 练习与答案 / 本周金句 / 据俄罗斯媒体»
  all 0 in the rendered edition); simplified-only diagnostic characters = 0;
  rendered CJK = 237 distinct characters, all Japanese explanation layer. The
  only CJK strings that survive verbatim from the core are the Japanese-inherent
  band titles 生活 / 文化 and the identity-mapped match note 旅行 c (W43 precedent:
  these are Japanese words, adjudicated keeps).
- Content red line: Russian body untouched (domestic-life topics only); the
  Japanese layer adds no international-politics content.
- Fonts: JP faces throughout («Noto Serif/Sans CJK JP» via the JA svglib);
  visual pass over the P1 and P7 cards found no missing glyphs / tofu.
  Other pages are covered by the audits + Cyrillic diff (same coverage basis
  as the W45 siblings' builder passes).
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run.
  Rect-multiset diffs on P2–P6/P8 are explanation-layer reflows only (gloss
  boxes growing by one line where Japanese wraps longer, exercise chips shifting
  with their exercises) — counts unchanged, occlusion 0, no overflow.

## §7 Japanese typography (README #19)

- Canonical JA svglib, unedited (§2). JA kinsoku line-break reflows are the
  only post-swap differences vs the core's text (verified pre-translation:
  CJK totals per page identical).
- Line-start orphan-punctuation scan on the finished edition: **0 violations**
  (every rendered line is its own text element, so the scan is exhaustive;
  the set covers full-width closers 、，。）〕］｝」』》 and ASCII closers).
- Post-kinsoku line-end widths re-checked via the same scan pass: no line
  ends with lone closing punctuation.
- Adjudicated non-defect (ordinary CJK wrapping, same class as the W43 core's
  own character-split lines): the P7 B2 bridge wraps «書いている» across lines
  （書いて / いる). Japanese breaks between kana characters as a matter of
  course; no line begins or ends with lone punctuation, which is the actual
  defect class.

## §8 Self-proof defects found & fixed (2)

1. **P7 word-box headword dropped (mine)** — first audit run showed a P7
   Cyrillic delta промокод 4→3: my Japanese word-box line had replaced the
   Russian headword with katakana. Fixed per the ×JA convention (W43 ru-ja
   keeps the Russian headword: «единоличный лидер = …»): the line now reads
   «промокод = 割引コード。レジで入力。」 (verified 1 line at JA metrics, so
   the word-box height and P7 col3 ends 1727.58 are unchanged). Re-run:
   P7 Cyrillic delta = 0.
2. **P8 #139 stem gave away Cyrillic spellings (mine)** — first version cited
   ««Краснодар» … ЦСКА» inside the Japanese stem, adding 2 Cyrillic tokens vs
   the core. Fixed per the core's stem design (transliterations, not
   spellings): «土曜日、クラスノダールはCSKAと対戦する。→ ___». Re-run:
   P8 Cyrillic delta = separators only (СТРАНИЦА ×8).
- After each fix the full gate suite was re-run from a single-process build
  (freeze token diff, p8 compare CLEAN, occlusion audit, kinsoku/split/
  collision scans, golden-sentence counts).

## §9 Deliverables & measured pins

- files/weekly-report-w45-ru-ja/svg/ — 8 SVGs (p1-pervaya … p8-test)
- files/weekly-report-w45-ru-ja/cards/ — 8 card PNGs (1950×2700)
- Print PDF: Lucerna-VOL2-JA.pdf — 18,194,817 B, 8 pages,
  sha256 044da00c592d0aa988f71506d464541c949d8b2b46946155c5461debe9bf20f2
- Web PDF: Lucerna-VOL2-JA-web.pdf — 3,104,219 B (< 10 MB), 8 pages,
  sha256 da5124c824411a68ed695bf3fdda6118dc47ccf27e69612541b480e09544c8e0
- ABSTRACT.txt — one Japanese line, no ASCII double quotes, naming the real
  W45 topics (4 Nov Wednesday holiday, 3 Nov short day, 11.11 smart shopping,
  6–8 Nov RPL round 14) + a learner search phrase （ロシア語ニュースでロシア語を
  学ぶ) + masthead (Lucerna VOL.2), levels (A2–B2) and exercise count (150)
- Scratch evidence: hidden_files/weekly-report-w45-ru-ja-build/scratch/
  (map_ja.py, transform_ja.py, scan_all.py, scan_all.out, scan_all2.out,
  occl-ed.json, occl-ed2.json, occl-core.json, p8-core.txt, p8-ed.txt)
- Core integrity at close: freeze baseline hashes unchanged (see §1 step 2).

**Status: BUILDER-COMPLETE** — ready for the independent proofread; no repo
insert, no Discord post, no user message was made from this build.

## §11 Coordinator adjudication (2026-10-27, documentation only, no render change, FINALIZED)

- Independent proof (hidden_files/w45/ru-ja-proof/REPORT.md): paper ZERO defects (freeze exact, p8 CLEAN true diffs only [137,138], occlusion 0 + NEW 0, gloss 26, images byte-identical, P7 golden 2×, 150, 8 cards visual, PDFs match §9 pins, badge three-way = W43 shipped, P7 B2 「書いている」 wrap judged CJK-normal, not a problem); sole item was KIT §4 total added CJK 2342 vs measured 2343. Coordinator independently re-ran freeze.py diff and confirmed per-page 185/243/171/159/167/209/285/924 = 2343 (freeze.py prints TOTAL 2343). KIT text only (§4 corrected above); paper verified untouched (PDF sizes/SHAs = §9 pins, SVGs retain build mtimes, only KIT edited). Per the JA KIT-only precedent, no new proof round needed. FINALIZED.
- Process note (not a paper issue): the proofreader's registry rerun landed its OUT redirect in the shared scratch dir `goals/lucernaread-social-media-operations/tmp/` and its cleanup deleted other groups' regenerable scratch dumps there (`regdump-core`, `regdump-ko`, `w45ko-debug`). Delivered files were verified unaffected (mtime/SHA rechecked). No action: those dumps are regenerable if any running builder needs them; proofreaders must not clean shared scratch dirs.
