# WEEKLY-KIT — 2026-W47 en-ja (English target, Japanese reader)

## 1. Identity
- Slug: `2026-w47-en-ja`
- Target language: English (en). Reader language: Japanese (ja).
- Issue week: Monday 16 – Sunday 22 November 2026. VOL.4.
- Core: `production/2026-w47/core-en/` (en-zh-cn), copied whole, explanation layer rewritten in Japanese.
- Exercises: 150 (registry 150; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- MODEL words: 82.

## 2. Files delivered
- 8 SVG (`svg/p1-front.svg` … `svg/p8-test.svg`) + 8 card PNGs (`cards/`).
- Print PDF: `The-Lucerna-VOL4-en-ja.pdf` — 35,187,926 bytes,
  SHA-256 `068e2d9da3e50d70dde8f3525faa73e4d703d29adcdad4d18c80cbfe13e698b1`
  [D5 rebuild, 12 Nov 2026 — see §3; pre-D5 values were print `e91ed980…` 41,509,391 B,
  web `fb903b2b…` 2,883,888 B.]
  [F1 fix, 12 Nov 2026 — see F1 bullet below; pre-fix values were print `2da13855…` 35,187,539 B,
  web `e880d0c9…` 2,712,817 B.]
  (41 MB is the CJK-font-embedding scale — the core-en print PDF is 41,407,278 bytes).
  Delta 2026-11-11 (Q73 speak→up, §5): same byte size as the proof1 build; SHA changed.
- Web PDF: `The-Lucerna-VOL4-en-ja.web.pdf` — 2,713,215 bytes,
  SHA-256 `e0ead68adf7a5be76c2b26c8fb6b2662732ac5b19b27f788c9f377795186b911`
  (built only with `tools/webpdf.py`; text layer 49,871 chars incl. whitespace, identical to the print extraction — token-multiset diff 0/0; per-page byte-identical 8/8; < 7 MB).
- `2026-w47-en-ja.text.md` — 53,756 bytes, SHA-256 `2ccd31bee63d5abc4b50f35a4a77923922bfd4bb63e0b2f168211f46f04c3f4e`, exported from the build source (never from the PDF);
  stub registry 150 = real registry 150. Re-exported in the F1 fix (12 Nov 2026, see F1 bullet below; pre-fix 53,585 B `2d498e4e…`).
- **F1 fix (12 Nov 2026, proof-round defect F1 — Georgia runoff written as pending; work log in `hidden_files/w47/scratch-fix-en/FIX-LOG.md`, gates in `hidden_files/w47/scratch-fix-en/logs/2026-w47-en-ja/`):** P2 :185 + P6 :651 rewritten as settled law + result (Georgia law calls for a Dec 1 runoff only if no one wins a majority — AP called Jon Ossoff reelected 3 Nov, ~59%, so no runoff). Q13/Q142 untouched (rule questions, answers still 1 December). Source `content12.py:171` + `content56.py:103`; text.md re-exported with `scratch-fix-en/make_textmd_fix.py` (diff exactly the 2 lines, no title lost — all 7 D5-shrunk box titles present). Full rebuild + gates ALL-GREEN: run rc=0 TOTAL 150 MODEL 82, 0 overflow; head_check PASS; occlusion 0 flags (selftest OK); p8 extract 60/150, compare CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); freeze baseline 8/8; spill 0; boxtitle 0; edge 0; creambox PASS; census PASS; print/web text layers byte-identical. New deliverables: print 35,187,926 B SHA-256 `068e2d9da3e5…` (was 35,187,539 B `2da13855…`), web 2,713,215 B `e0ead68a…` (was 2,712,817 B `e880d0c9…`), text 53,756 B `2ccd31be…` (was 53,585 B `2d498e4e…`); text layer 49,871 chars incl. whitespace (was 49,689).
- `ABSTRACT.txt` — one line, Japanese, no ASCII double quotes.
- `registry.json` — fresh dump (150 keys), copied over the stale core copy from apply.py.
- `svglib.py` is the W46 en-ja file wholesale (apply.py does this for ja/zh-tw only) — verified
  byte-identical to `2026-w46-en-ja/svglib.py`.

- **Delta Q73 (2026-11-11, core-en fix2 sync — this round, only change in the edition).**
  Core-en fix2 changed the Q73 key `"speak"` → `"up"` (stem "Speak ___: tell a teacher.",
  note "speak up = …" unchanged). This edition synced the single key only:
  `content56.py:49` `"speak"` → `"up"` (note + stem untouched, one source line);
  registry diff exactly 1 line (583: `"key": "speak"` → `"up"`); text.md diff exactly
  1 line (1151: `73. [A2] 文の完成 — speak (…)` → `— up (…)`); P8 SVG differs from the
  proof1 build in exactly 3 bytes (`73. speak` → `73. up`); P1–P7 SVGs byte-identical
  to the proof1 build (P5 stem unchanged, so P5 is identical too). Rebuilt via run.py /
  render.py / webpdf.py + registry + text.md re-export; full re-gate green (see §3 note
  below and `hidden_files/w47/scratch-delta-en-ja/DELTA-NOTE.md`). Q73 four-source
  agreement: registry `up`, text.md:1151 `up`, P8 printed key `73.up`, P5 stem
  "Speak ___: tell a teacher." + note "speak up = 声を上げる" — "Speak up" fits.
  P5 SVG byte-identical to the proof1 build is correct and expected (the key itself
  never appears on P5, only the blank `Speak ___` + the `speak up` note; only P8 changes —
  confirmed by the en-es delta and by this edition's own baseline rebuild). The edition
  baseline (`freeze.py baseline --build 2026-w47-en-ja --core-svg 2026-w47-en-ja/svg`)
  re-run after delivery: 8/8, with the core read-only control (`--build core-en`) also 8/8.
  All 53 fill-in/rewrite items re-checked for key-fills-blank sense (53/53 sensible,
  each mapped 1:1 to its registry entry). No other source line touched; core-en untouched
  (its content56.py:49 already `up`); no commit/push (coordinator's job).

## 3. Gates (all green, re-run fresh 2026-11-11 after the P4 fix; re-run again the same day for the Q73 delta — see §5)
- run.py exit 0; 0 FLOW OVERFLOW / HEAD TOO WIDE; every Flow end y ≤ its bottom
  (P8-keys 2205/2560; P2-feature 1438/1540; P2-ex 2532/2560).
- occlusion audit: 0 flags (selftest OK).
- p8 extract: 60/150 noted (same set as core); compare CLEAN; keydiff [137, 138, 139, 140, 150]
  (reader-language translation keys + writing key — expected).
- freeze baseline tool: 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs: 8/8 MATCH.
  Freeze diff: added CJK = 2,084 characters — the Japanese explanation layer itself (hiragana-heavy
  histogram: の 81, は 74, い 59, を 55, で 52…; re-measured in this rebuild — the old KIT's
  2,096 was the pre-rebuild count, the 2,092 found during the rebuild check was the first build
  of this round before the A PRACTICE BALLOT title fix); removed = core Chinese layer. No leftover
  Simplified Chinese re-verified on the rebuilt text.md: 0 hits for 中期选举/众议院/民主党赢下/
  参议院/星期五/金句/范文 etc.; the only shared kanji (国/与/来) all occur in Japanese context
  (あなたの国では, 与えられた語で, 前に来る, 民主党は下院で).
- print/web text token-multiset diff: 0/0 (43,475 chars each; token-multiset diff 0/0; per-page byte-identical 8/8).
- `check_s11.py ja`: ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19;
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min font 13.5 pt ≥ 9.75;
  chip-rect counts = core per page; Q113–120 options line with [A2] tag present;
  "Levels: 145–149 [A2]" present; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　作文 [B1]" present).
- **D5 rebuild + gates (12 Nov 2026; full log `hidden_files/w47/scratch-d5-rebuild-en/logs/2026-w47-en-ja/GATES-SUMMARY.txt`)**: SOP §1.1 font fix — installed via `scratch-d5-plan/mechanism/apply_variant.py --target en --reader ja` (mode cjk, D5 block in this edition's `svglib.py`, `_D5_READER = "cjk"`; script-based routing, no `_READER_LANG` gate; latin/cjk share routing — Latin/digits/punct → Newsreader, Cyrillic → Noto Sans, CJK → Noto Sans CJK JP; routing unit-checked with the latin case set + `_D5_READER == "cjk"`: FAILURES: 0; U+201C fix2 routing preserved — `census_quotes.py`: 0 defective, all 164 curly quotes in Newsreader). Pre-fix census: 380 Latin-in-CJK-sans elements. Post-fix defects, all D5-caused (same classes as the Latin editions, cf. CJK-DECISION §1 pilot): (1) P8-battery head `D　SENTENCES　文の完成と書きかえ` HEAD TOO WIDE +19.0 px advance at 24 → head size 24 → 22 (`content8.py:72`); (2) P1 cream-box title `THE WEEK IN NUMBERS　今週の数字` +36.5 px right → `tsize` 23 → 20 (`content12.py:43`); (3) P2 cream-box title `THE CALENDAR　今週のカレンダー` +2.8 px right → `tsize` 23 → 22 (`content12.py:180`); (4) P3 cream-box title `HAYMITCH'S GAMES　ヘイミッチ戦` +17.8 px right → `tsize` 23 → 21 (`content34.py:82`); (5) P5 cream-box title `ODD SOCKS, IN NUMBERS　数字で` +6.3 px right → `tsize` 23 → 22 (`content56.py:22`). Layout only, text unchanged. Pre-fix baseline reconstructed (no pre-D5 snapshot existed for CJK editions): pre-fix print PDF `e91ed980…` (41,509,391 B) + SVGs from the mechanism pilot's `scratch-d5-mech-close/cjk-en-ja/base/` (verified 8/8 SVG = delivered, print SHA = KIT-recorded value); pre-fix web SHA `fb903b2b…` from the KIT (the pilot's base web render differs by 8 B — render-level, not content); pre-fix text extraction from that print PDF; pre-fix census 380 from the pilot's `census-base.log`. Gates: run rc=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; `head_check.py` PASS 0 defects; `render.py` + `webpdf.py` rc=0; `occlusion_audit.py` 0 flags (selftest OK); `p8.py extract` 60/150 (same set), `compare` **CLEAN**, keydiff=[137, 138, 139, 140, 150] (expected); `freeze.py baseline` **8/8**; `freeze.py diff` vs core-en TOTAL added CJK 2,084 (the Japanese layer itself, cf. §3 pre-D5 note), added Latin strings 138 (D5 run-splitting); `spill_sweep.py` 0 SPILL (147 OBSERVE); `boxtitle_check.py` 0 DEFECT / 0 OBSERVE / 0 marginal (30 titles, 269 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` **PASS 0 defects** (ratios n=435 median 1.012, bold 1.057; rerun after adding the baseline `svglib.py` + `assets/` to the backup dir — the first run failed to load the baseline module, not a defect); `d5_census.py` **PASS** — D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, `Noto Sans` elements 0; print/web `pdftotext` byte-identical, 49,689 chars incl. whitespace (pre-fix 49,784; −95 whitespace-only, non-space multiset 34,522 identical pre/post); text.md byte-identical (`2d498e4e…`, 53,585 B). P8: 185 → 185 lines, footer slack 34.6 → 34.6 px. **OVERALL: ALL-GREEN.** Pre-D5 baselines: print `e91ed980…` (41,509,391 B), web `fb903b2b…` (2,883,888 B); new SHAs in §2 (print `2da13855…`, web `e880d0c9…`).

## 4. Translation decisions (Japanese)
- Follows W46 ja (TM): instructions in plain imperative form (空所補充, 書きかえ, 直しなさい);
  gloss format "term = translation", "·" separators, "解説 — " box prefix (bslib4 gloss() prepends
  it; gloss translations are bare — only the P1 bridge carries its own label, "解説 — ").
  No bridge-size patch for ja (p1_bridge_size None — the W46 ja bridge renders at the default
  20.5pt, verified in content12.py:42).
- "runoff" = "決選投票"; "call a race" = "当確を出す" (bridge/glosses; registry notes keep the TM
  "選挙結果を発表すること" — two different source literals, both correct);
  "to certify" = "正式に認証する" (TM); "midterm" = "中間選挙"; "seat" = "議席";
  theme "Break the Silence" = "沈黙を破れ".
- Numbers box keeps the English term with a Japanese gloss in parentheses (W46 ja precedent).
- P2 calendar lines in full-Japanese short form (es precedent — avoids the fr P2 overflow):
  "11月10日 — 共和党が党首を選ぶ · 11月18–19日 — 民主党が投票" /
  "11月20日 — 世界子どもの日 · 11月26日 — 感謝祭 · 11月27日 — ブラックフライデー".
- SAY IT title = "日付の言い方" (date, not clock time — the de D-de1 lesson).
- P1 word-of-week bridge pre-shortened to 2 lines: "中間選挙：下院は全議席、上院は約3分の1。"
  (fr/es lesson).
- TM types (used as-is): 完成句子→"文の完成", 翻译→"翻訳", 写作→"作文", 阅读理解→"読解",
  单选→"選択", 完形填空→"空所補充", 词汇配对→"語彙マッチング", 句型转换→"文型変換",
  对话补全→"会話補完". TM instr: 填空→"空所補充", 把词和释义配对→"語と意味を結ぶ",
  改写→"書きかえ", 配对→"語と意味を結ぶ".
- Fresh sets: instr 纠错→"直しなさい"; types 从句→"従属節", 将来时→"未来形", 时态→"時制",
  比较填空→"比較", 过去时→"過去形", 金句填空→"名文の空所補充", 纠错→"誤り直し",
  图表读数→"グラフの読み取り" (overrides the poisoned TM value "sans").
- ekeys: 137 "民主党は下院と上院で勝利した。", 138 "開票はまだ続いている。",
  139 "新議会は2027年1月に開会する。", 140 "沈黙を破れ。",
  150 "自由記述 — 要点は作文の枠内、模範文は8ページの作文枠の中" (dash form, from the TM —
  no override needed).
- Box titles (single-line, short forms): "ERROR CLINIC　誤り", "READERS' CORNER　読者の手紙",
  "AN EXAMPLE LETTER　見本", "THE TOOLBOX　道具箱", "NEXT WEEK　VOL.5予告",
  "SENATE IN NUMBERS　上院" (short gloss, nl lesson applied pre-emptively; core fix1 dropped
  "THE"), "HOW LONG?　任期の長さ", "ODD SOCKS, IN NUMBERS　数字で",
  "SATURDAY, NOV 21　土曜日" (core fix1 title), "HAYMITCH'S GAMES　ヘイミッチ戦",
  "THE CALENDAR　今週のカレンダー", "A PRACTICE BALLOT　投票用紙" — all short forms, no
  collision (occlusion 0 flags; SVG boxtitle sweep 18/18).
- P8 section heads use TM short labels ("文の完成と書きかえ", "語彙の組み合わせ", "会話補完",
  "模範文") that differ from the registry type names ("文の完成", "語彙マッチング", "会話補完",
  "作文") — same pattern as fr/es/it/pt/nl/ru.

## 5. Fix in this round (→ rebuild + re-render + full re-gate)
- **P4 gloss separator inconsistency.** My #188 used full-width colons ("a Test：5日間のクリケットの
  試合 · a tour：ツアー …") while every other gloss in the edition uses "=" — fixed to
  "a Test = 5日間のクリケットの試合 · a tour = ツアー · an injury = けが · a break = 休憩期間。"
  Verified 0× "a Test：" in the re-exported text.md and visually on the P4 card. Lesson for
  ko/zh-tw: check the separator character in every fresh gloss translation, not just the words.
- **Anchor typo (build_map caught it).** My first miss-tr-ja.json #7 anchor used the Japanese kanji
  勝/輪 ("决勝輪") instead of the source's Simplified 胜/轮 ("决胜轮") — build_map's anchor
  resolution failed with 0 candidates. Fixed the anchor to the exact source characters.
  Lesson: anchors must be copied character-for-character from the source literal, never typed from
  memory in a CJK language (kanji look-alikes are the trap).
- P8 key size 13.5/1.26 is the W46 ja extracted value already (no es-style change needed at the
  meta level — the first run already used 13.5; P8-keys ends 2205/2560).
- **Rebuild + fix1 (11 Nov 2026, core-en fix1 sync — this round).** Core-en was fixed and
  re-proofed (Q39→a, Q40→d, Ashes rewritten as a 2025–26 retrospective, 已宣布 wording,
  SEARCHES/DID YOU KNOW box heights, SENATE/SATURDAY titles, SAY IT middle panel widened)
  and this edition was rebuilt from the fixed core via `scratch-fanout-en2/fanout/apply.py` +
  patched `map-ja.json` (14 new literals: Q39/Q40 keys + notes, Q46/Q52/Q55/Q125 notes,
  SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge). Proof1 defects D1–D3
  were core-level and are resolved by the rebuild (verified per edition: registry keys
  39=a/40=d, notes `mentor = 師匠 a` / `arena = 競技場 d`; Q46 note dated Fri 21 Nov 2025;
  Q52 `hosted`, Q55 `won`, Q125 `A (4–1)`; text.md answers 39→a, 40→d, 125→A;
  `Arsenal are winning!`; no `Perth is winning!` / `second week in Perth` / `Ashes begin`).
  **D4 (edition-level) fixed**: the old ABSTRACT violated SOP §9 (no Lucerna/A2–B2/150) and
  was short-form — rewritten to the full form (announced results; certification 10 Nov–18 Dec;
  16 Nov Anti-Bullying/Odd Socks; 20 Nov Children's Day + Hunger Games; 21 Nov Premier League
  back + Turin ATP final + Ashes 4–1 look-back; reader language; A2–B2; 150).
  **D5 (edition-level) fixed in the map**: P3 HAYMITCH title `HAYMITCH'S GAMES　ヘイミッチの大会`
  (431.4 px, −26.9) → `HAYMITCH'S GAMES　ヘイミッチ戦` (385.4 px, +19.1).
  **D6 (edition-level) fixed in the map**: P5 D-section instruction `現在進行形で書きかえよう
  （今起きていること）。` wrapped and orphaned "と）。" in column 3 → `現在進行形で書きかえよう。`
  (single line on the rebuilt P5 SVG, baseline y=2543.95, above the footer rule).
  **New defect found by this round's own boxtitle sweep (pre-existing, missed by ja proof1,
  same class as ko D3):** P5 ODD SOCKS title `ODD SOCKS, IN NUMBERS　数字で見る` (426.9 px,
  −22.4; identical in the pre-rebuild SVG) → `ODD SOCKS, IN NUMBERS　数字で` (≈357.9 px).
  **Second new defect found by the same sweep:** P6 `A PRACTICE BALLOT　練習用投票用紙`
  (407.9 px advance, −3.4; true ink −3.5 px — a real overflow, not a rounding artifact) →
  `A PRACTICE BALLOT　投票用紙` (338.9 px, +65.6). Both fixed in `map-ja.json`, full rebuild +
  re-gate. All 18 SVG box titles now fit (tightest THE WEEK IN NUMBERS +1.5 advance, +1.5
  true ink — genuinely tight but inside, recorded, no fix). KIT §3 freeze number corrected to
  the re-measured 2,084 (see §3).
- **Rebuild gates (11 Nov 2026, second build of this round; logs in
  `hidden_files/w47/scratch-fanout-en2/fanout/ja/build-gates.log`)**: `run.py` exit 0, zero
  OVERFLOW / TOO WIDE, all flows within bottom, TOTAL 150, MODEL 82; `occlusion_audit.py`
  0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as core); `p8.py compare`
  CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); registry vs P8 extract 149/150 exact
  + n=150 short-label exception; registry keys vs core 145/150 (diff only the 5
  reader-language keys 137–140, 150); `freeze.py baseline` 8/8 SVGs byte-identical;
  `freeze.py diff` TOTAL added CJK 2,084; print/web text layers 43,475 chars each,
  token-multiset diff 0/0, per-page byte-identical 8/8; `check_s11.py` ALL PASS; source
  boxtitle sweep 12/12 fit; SVG boxtitle sweep 18/18 fit; canonical `creambox.py` scan: all
  inside-only clearances positive; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK
  (Japanese, not Chinese — the sweep counts only non-Japanese CJK; 0 hits for the
  Simplified-only check strings above). (First build of this round passed everything except
  the two boxtitle sweeps, which caught the A PRACTICE BALLOT title; the second build is
  the shipped one.)

## 6. Self-check (2026-11-11)
- Full read of `2026-w47-en-ja.text.md` (all ~1,306 lines): zero issues (after the P4 fix;
  the fix touches one gloss literal only, and the P8 tail was re-read in the re-export — same
  content apart from that literal).
  Notes kept: Q2/Q95 note "call a race = 選挙結果を発表すること" (TM) vs P6 gloss "当確を出す" —
  two source literals, both correct; Q11 "11月 = November" terse as in core; Q34
  "(open = 公開される（三人称単数 + s）)" correct; Q54 "eight (8人 = eight)" follows the core's
  tautological note pattern; Q97 "take time = 時間がかかる" correct; Q110 "more thanの構文" terse
  as in core; Q136 "whether = 〜かどうか" vs Q105 "whether = かどうか（わからないこと）" — two
  source literals, both correct; "5文レビュー｜who、where、何が起きたか、転換、結末——5文で十分。"
  is the W46 ja TM value for the FIVE SENTENCES bridge (kept); "観戦英語｜スコア、誰が得点したか、
  誰がリードしているか——短い文こそ実況英語。" and "一枚の地図｜50の州、50通りのルール——…" are
  W46 ja TM values (kept); "LIGHTNING QUIZ · 稲妻クイズ" is the W46 ja TM head (kept).
- All 8 cards visually checked after the final render — clean. P1: bridge 2 lines clear of
  IN BRIEF, numbers box English+gloss, "TRY IT NOW · すぐ練習", footer "1ページ（全8ページ）".
  P2: calendar short form, "THE SENATE, IN NUMBERS · 上院", SAY IT "日付の言い方",
  gloss single "解説 — to certify = …". P3: "COMING SOON · 近日公開",
  "HAYMITCH'S GAMES · ヘイミッチ戦", gloss single "解説 — a tribute = …", Rousseau tiger.
  P4: "SATURDAY, NOV 21 · 土曜日" (core fix1 title), gloss single "解説 — a Test = …" (fix verified),
  W. G. Grace photo; P4 lead is the Ashes 2025–26 retrospective "Perth, One Year On: How Australia Kept the Ashes". P5: "ODD SOCKS, IN NUMBERS · 数字で", gloss single
  "解説 — bullying = …", "SPEAK UP · 声を上げよう", Lawrence children photo.
  P6: "HOW LONG? · 任期の長さ", gloss single "解説 — to call a race = …",
  "A PRACTICE BALLOT · 投票用紙" (see §5), voting booth photo. P7: all gloss boxes single "解説 —",
  "THE TOOLBOX · 道具箱", "READERS' CORNER · 読者の手紙", "AN EXAMPLE LETTER · 見本",
  "ERROR CLINIC · 誤り", "NEXT WEEK · VOL.5予告", Johnson portrait. P8: cloze + [A2] option
  tags, "B MULTIPLE CHOICE · 選択", "C READING · 読解", "D SENTENCES · 文の完成と書きかえ",
  "E TRANSLATION · 翻訳" with "訳しなさい：", "F WORDS · 語彙の組み合わせ",
  "G DIALOGUE · 会話補完" + "Levels: 145–149 [A2]", "H WRITING · 作文 [B1]" + Japanese
  instruction, MODEL + Reading Room photo, ANSWERS block all 150 keys ending well above the
  footer with "150. 自由記述 — 要点は作文の枠内、模範文は8ページの作文枠の中 (要点ごとに採点)";
  footer "8ページ（全8ページ）".

## 7. Furniture
- foot_left "The Lucerna　英語週刊 VOL.4　本文は英語　解説は日本語";
  foot_right "{n} ページ（全{total} ページ）"; gloss_prefix "解説 — "; p8_sep "— {pg} ページ —";
  translate prefix "訳しなさい："; badge "英語テキスト　日本語の解説 — 日本語読者のための版";
  topstrip "WEEKLY IN ENGLISH　毎週1回　英語圏で話題のこと";
  edition line "英語週刊　VOL.4　選挙　ジャングル　映画"; edition spacing 11.5;
  p1_bridge_size None (default 20.5, W46 ja convention); p8_mode "notes".

## 8. Provenance
- TM: W46 `2026-w46-en-ja` positional alignment (260 pairs). Poisoned values caught:
  'note' → 'P8 saved, TOTAL exercises:' (harmless, rejected by build_map's POISON regex);
  '图表读数' → 'sans' (overridden by fresh type "グラフの読み取り").
  'THE ERROR CLINIC　易错诊所' → 'THE ERROR CLINIC　誤り' is a legitimate translation, not poison.
- Map: `scratch-fanout-en2/fanout/map-ja.json` (lit 248, instr 5, type 17, ekey 4).
  Misses: 205 total, 182 with real CJK = 171 lit + 7 types + 4 ekeys.
  build_map normalizes U+2019 → ASCII apostrophe in all map values (fr lesson).
- F-MAIL: no real letters arrived; P7 prints the labelled editor's example + the VOL.3
  disclosure promising real letters from VOL.5. No invented letters, no email checked.

## 9. Build record
- `scratch-fanout-en2/fanout/ja/` — build-gates.log, make_textmd_w47.py, occlusion.log/json,
  p8-extract/compare.json, freeze.log/diff.json, webpdf.log, textmd.log, registry.json, dump_reg.log,
  freeze-final/.
- Q73 delta (2026-11-11): `hidden_files/w47/scratch-delta-en-ja/` — DELTA-NOTE.md,
  pre/ (pre-build registry.json + text.md), pre-svg/ (pre-build SVG bytes), build/render/dump_reg/
  textmd/webpdf logs, occlusion/p8-extract/p8-compare/freeze logs + json, printweb/check_s11/
  keycheck/answers-150/p8font/boxtitle/creambox logs, fill-rewrite(.map).log, svg-*-diff logs.

## 10. Tool note (NOT fixed — p8.py is off-limits to the builder)
- `tools/p8.py` FOOTER_RE does not match the mixed-case footer "The Lucerna …" + "1 ページ（全8 ページ）":
  the merged footer line leaks into the last answer segment (key 150) for every edition.
  Masked when key 150 is dash-style (ja, ru, nl, pt, it, fr, de), bites when paren-style without a
  dash (es, before its fix). A case-insensitive match on the masthead, or dropping the merged
  footer line by its y=2624 baseline, would close it.
- Occlusion audit gap (found in the nl round): the audit does not flag a box title running into live
  text in the neighbouring column. A title-vs-neighbour text proximity check would close it.
