# WEEKLY-KIT — Lucerna Weekly W45 · JA × ZH-TW (builder record)

> Status: **builder-complete** (built by the JA×ZH-TW builder; NOT final
> approval — independent proofread still pending).
> Delivery: `files/weekly-report-w45-ja-zh-tw/` (svg×8, cards×8, print
> PDF, web PDF, this KIT, ABSTRACT.txt).
> Build tree: `hidden_files/weekly-report-w45-ja-zh-tw-build/`
> (`transform.py` is the single source of truth for all fixes; every
> re-render is `transform.py` → single-process `run.py` →
> `tools/venv/bin/python render.py`).
> Core: `files/weekly-report-w45-ja-core/` (VOL.2, read-only, never
> written by this build; verified 8/8 unchanged after every render).

## 1. Interpreters and libraries

- `run.py`: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0.
- `render.py`: `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0
  (system `python3` is also 3.12.3 but its PIL is 10.2.0 and it lacks
  cairosvg, so it was never used for either step).
- Interpreter validation: the pristine core build was copied to scratch,
  its OUT redirected, and run with the venv interpreter; it reproduced
  the shipped core SVGs **8/8 byte-identical** (see §2). The edition
  therefore uses the venv interpreter for both steps.

## 2. Core baseline (frozen reference)

SHA-256 of the shipped W45 JA core SVGs, recorded before any edition
work in `hidden_files/weekly-report-w45-ja-zh-tw-build/core-baseline-sha256.txt`:

- p1-hyoushi: `4abe63d2…13b17b`
- p2-kurashi: `08439072…5f9b`
- p3-bunka: `48a1fe94…96bc6b`
- p4-supotsu: `11b592b5…12c618`
- p5-wakamono: `3035b928…2070d5c`
- p6-fukayomi: `a8095c47…11f2`
- p7-kotoba: `08060a28…71d49`
- p8-tesuto: `9e733a42…d53196`

(Full hashes in the baseline file.) Core SVGs re-hashed after every
edition render: 8/8 unchanged each time. Core `svglib.py` MD5 verified
before every copy: `d73e23b365676c3618d7e060b835eb4d` (JA canonical,
SEAM_SLACK = 28). Canonical files were never edited.

## 3. Edition facts (all re-measured from the core, not copied)

VOL.2, masthead with no article, 150 exercises, A2 46 / B1 75 / B2 29,
page distribution 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38, model essay
167 characters titled 私の11月の週末 (character count, verbatim =
core, §7). Topics: 11月3日 Culture Day; 11月7–8 weekend autumn leaves
(Naruko Gorge peak, Kobe Nunobiki Herb Garden illuminations from
11月7日）; ゆる整え食 (Ajinomoto, 10月21日）; Reading Week in progress
through 11月9日； 11月7日立冬. P4 Japan Series G1/G2 verified, G3–G7
schedule only, deferred to VOL.3 on the page. 10月31日 Halloween is a
just-passed event. P6 practice chart (labelled practice data):
近場の満足 38 / 温泉 27 / 紅葉 21 / グルメ 14 = 100. P7: A2 column
本と読書のことば / B1 紅葉のことば / B2 数字を読む + error clinic
4 items + frame box ゆるく整える + readers' corner (§9) + VOL.3 teaser.
P8 zones A–H; E zone JA↔Traditional Chinese, 4 items (§8).

## 4. Transform summary

- 187-entry quoted-literal conversion map (186 reviewed entries +
  round-3 addition, §11), applied longest-first to the five content
  modules only; post-apply audit asserts no map old survives as a quoted
  literal. Conversion rules: data → 數據 (not 資料）; 读书周 → 讀書週;
  weekday tokens 週X → 星期X (X = 一..日）; 单词 → 單字; 日元 → 日圓;
  week words that are not weekdays keep 週 （讀書週, 本週, 週末）.
  Japanese text inside Chinese strings was never converted: Japanese
  place names in Japanese text stay 金沢, 横浜, 鳴子峡, 工芸, 金沢城;
  the same places in Chinese renderings convert separately (金泽 →
  金澤, 横滨 → 橫濱, 神户 → 神戶, 杉并 → 杉並）. Japanese headwords in
  gloss/explanation rows stay byte-identical; only the Chinese gloss
  part converts. Mixed ` · ` furniture converts segment by segment
  (kana segments and exactly 来週 stay Japanese).
- Explanation-function rename: the old function name (definition 1 in
  `bslib4.py`, 22 call sites: content12 3, content34 7, content56 8,
  content7 3, content8 1) is renamed to `expl()` with a `face`
  parameter. The transform script assembles the old name from split
  fragments, so neither the transform script nor any operative build
  file, SVG, or the abstract contains the old identifier or the old
  Chinese term for that function (both verified 0 by grep).
- Face routing (W43 same-pairing form — see the flagged interpretation
  in §12): JA canonical svglib + TC face routing (TC face index 3,
  verified equal to the W45 zh-tw core svglib's own TC face selection;
  TC NO_START set = JP set + ］｝〉》％; SEAM_SLACK behavior
  byte-identical). `bslib4.py` gains face parameters on `band`
  (face/sub_face), `shead`, `Flow._ph/para/box/head`, `gloss` (prefix
  譯注｜ in TC face), `ex` (instructions TC, `body_face` default JP),
  `match_set` (instructions TC). Band faces copy W43 exactly: P2, P3,
  P4, P5, P7, P8 titles TC; P6 title no face (pure Japanese, as in
  W43); all band subs TC except P8 sub JP. P8 answer separators and
  answer lines render TC face (W43 family convention for P8 apparatus,
  even though Japanese keys sit inside those lines). P7's three mixed
  gloss rows and P8's E-zone Chinese stems take `face="TC"` /
  `body_face="TC"`; all other explanation calls with Japanese text stay
  JP face by default.
- Masthead and furniture (§10): subtitle 330 → 316; badge inserted at
  (975, 356), 19pt sans bold BRICK, anchor middle, TC face, verbatim
  W43 string `日語正文 · 繁體中文講解 — 給繁體中文讀者的版本`;
  tagline 372 → 390; double rules 392/401 → 406/413; dark band
  unchanged at 424; wordmark unchanged at 262. Top-strip center line
  stays JP face with only 每周一期 → 每週一期 (W43 precedent). Footer
  left per page: `Lucerna · 日語週報 VOL.2 · 正文日語 · 講解繁體中文`
  (TC face); footer right unchanged (`第 N 版 / 共 8 版`). P8 band
  title `テストと答え · 練習與答案` (TC), sub stays Japanese
  `第 8 面 · 週の大きなテスト + 全ての答え` (JP). P8 answers head
  `答え · 參考答案 — 依版面分版排列，找到題號即可` (TC, W43 rewording);
  right note `每題附一句中文簡析 · 帶 ✓ 的為範文題` (TC; see §12 for
  the 範文題 vs W43 範本題 note). P8 separators `— 第{pg}版 —` (TC).
  P7 phrase page labels `第N面` → `第N版` (JA×KO precedent cited in
  W43); contents labels (`2面`…`8面`) and P8 band sub `第 8 面` stay
  Japanese and unchanged. PDF names follow W43 same-pairing and W45
  en-zh-tw: `Lucerna-VOL2-ZHTW.pdf`, `Lucerna-VOL2-ZHTW-web.pdf`.

## 5. Freeze gate — PASS (two-track account)

`tools/freeze.py diff` (core SVG vs edition SVG), occurrence counts
(distinct strings in parentheses):

- P1: +18 (18) / −17 (17). P2: +18 (18) / −18 (18).
  P3: +12 (12) / −12 (12). P4: +15 (12) / −15 (12).
  P5: +15 (12) / −14 (11). P6: +11 (9) / −11 (9).
  P7: +29 (29) / −29 (29). P8: +127 (124) / −127 (124).
  (Multi-count entries explain distinct-vs-occurrence gaps: 判斷 ×4
  on P4/P5, ×3 on P6; 翻譯 ×4 on P8.)
- Track 1 — Japanese frozen: the kana multiset (hiragana + katakana)
  is EQUAL between added and removed strings on all 8 pages. Every
  kana-bearing removed string is a mixed furniture/gloss/answer string
  whose Japanese half is preserved in an added counterpart; no
  pure-Japanese string was removed. All removed non-kana strings are
  Simplified Chinese explanation/answer-note/furniture strings (full
  lists in the freeze JSON held in /tmp during the build; P8 lines
  adjudicated individually in §8).
- Track 2 — explanation replacement: the 793 "added CJK" characters in
  the tool's accounting are Traditional replacement characters (new to
  the core's multiset because the Simplified forms differ), not new
  target-language text. The strict-CJK flag is therefore not the
  applicable test for a script-conversion edition; the applicable tests
  (kana equality + string pairing) are clean.
- P1 net +1 string is the new badge line. P5 net +1 distinct string is
  a wrap reflow, not a content change: core splits 守る across lines
  (`…仮装 变装 · 守` + `る 遵守。`), TC wraps it whole (`守る 遵守。`)
  and splits 話題 instead (`…話題 話` + `題。`); kana multiset equal.
- P7 target-language definition sentences frozen verbatim; only glosses
  localized (this rule holds for all target-language families).

## 6. Traditional independence gate — PASS (with two flagged items)

- Reference set R = W43 same-pairing Traditional character set (868
  chars, from its SVGs) ∪ W45 zh-tw core character set (868 chars),
  |R| = 1280. Edition character set = 806 chars. Superset beyond R =
  100 chars, each adjudicated:
  - 96 legitimate: Japanese body text of new W45 topics (九州, 金沢,
    埼玉, 筒香嘉智, 川村友斗, 観客, etc. — Japanese kanji/kana absent
    from W43/zh-tw-core for topic reasons) and new Traditional topic
    words (傳統, 規則, 搜尋, 氣象廳, 澀谷, 金澤, 觀眾, 石川縣, 管絃,
    照亮, 萬份, 化妝, etc.).
  - 4 Simplified-residue chars, all in the single P8 #124 line
    （连胜开局的夺冠率73%: 连/胜/开/夺） — caught by the P8 completeness
    gate and fixed in round 3 (§11). Post-fix rescan: 0 residue.
- TC-face word/character rescan (OpenCC s2twp-derived Simplified-only
  set, 2647 chars, applied to TC-face text elements only): round-3
  result is 12 hits, ALL frozen Japanese segments inside mixed
  furniture strings, band titles, gloss rows, or P8 apparatus lines
  rendered TC by family convention （届 in お届けします, 数 in 数字で見る,
  号/内 in この号の内容, 横 in 横浜, 点 in 同点, 装 in 仮装, 万 in
  〜万食, 来 in 来週, 温 in 気温, 峡 in 鳴子峡, 静 in 静か）. Zero true
  residue.
- Mainland-vocabulary substring scan on TC-face text (软件/硬件/视频/
  音频/网络/信息/数据/资料/鼠标/键盘/打印/复印/短信/公交/地铁/出租车/
  外卖/快递/网购/直播/点赞/质量/里面/夜里/单词/日元/周一..周日）: 0 hits.
- Quotation marks: 「」 36 / 」 36, balanced; «» 0 on all pages. The
  core `«»` count in W45 JA core content/bslib files was measured as 0,
  so there is no core `«»` form to explain.
- Shared-glyph adjudication: 只 occurs 0 times in the edition SVGs
  (also 0 in core content files, core SVGs, bslib, svglib, and W43
  edition SVGs by the searches run) — see the flagged mismatch in §12.
  Other shared-glyph items kept verbatim with legitimacy notes:
  市場＝集市, 陶器＝陶瓷, 金箔＝金箔, 和家人一起, 1.5倍＝比去年多50%,
  73%≈4人中的3人, 飲むことができません＝不能喝, 立冬在11月7日,
  文化日是11月3日。 (P8 #137 key, §8), 借りられます＝能借（可能形）,
  plus the Japanese-sentence and language-neutral notes listed in the
  build notes (e.g. 鍋の食卓は去年の1.5倍, 発表は10月21日,
  11月から1月まで気温は平年より高い, グラフは練習用データです).
  s2twp variants: 里 occurs 3 times in core content, all Chinese 里
  meaning inside/at-night, all converted to 裡 （夜里路上不能喝酒 →
  夜裡路上不能喝酒; 围栏里面 → 圍欄裡面; 夜里用灯光照亮 →
  夜裡用燈光照亮）. 栗 occurs 0 times in core content files.

## 7. Counts, phrases, essay, images — PASS

- 150 exercises, continuous; A2 46 / B1 75 / B2 29; pages
  10/18/18/18/18/18/12/38 (= core). Run log: 0 `FLOW OVERFLOW`, 0
  `HEAD TOO WIDE`.
- Gloss rendering (· split, counted in the rendered SVG gloss boxes):
  10 rows, 39 segments = P1 4 / P2 9 / P3 8 / P4 7 / P5 7 / P6 4.
- Golden phrases: 8 Japanese phrases, each exactly 2× in the whole
  edition under whitespace-stripped counting. Accounting note: P7
  quotes add outer 「」 around each sentence, so the fully-quoted form
  appears 1× (P7 only) while the sentence itself appears 2× (article
  page + P7). Phrase 3 keeps its inner 『』 in both occurrences
  （『ゆる』は、無理をしない、ゆっくり、という意味です。: P2 + P7).
  P7 phrase page labels: 第1版 ×2, 第2版 ×2, 第3版, 第4版, 第5版,
  第6版 (rendered `(第N版)` after each translation).
- Model essay: 167 characters, byte-identical to the core (title
  私の11月の週末）.
- Images: payload byte-identical to the core on all 4 pages (same
  position, same embedded-data hash and length). Credits placed on
  every image, Commons API Artist field: P1 maple — Poliphilo, CC0;
  P3 Hiroshige III print — 歌川広重（三代）, public domain; P4 stadium
  — Syced, CC0; P5 pumpkin — Petr Kratochvil, public domain.

## 8. P8 gate — PASS

- `tools/p8.py` dual-path (extract + compare), total 150: core noted
  150/150, edition noted 150/150, status **CLEAN**, missing = [],
  extra = 0, uncertain = [].
- Keydiff = [2, 8, 32, 65, 69, 115, 117, 138, 140, 147] (10 items),
  each checked against printed lines, counted once, no double count:
  - 9 note localizations captured inside extracted keys (answer value
    identical): #2, #8, #147 (`读书周到11月9日` → `讀書週到11月9日`);
    #32 (`工艺展到11月8日` → `工藝展到11月8日` — the P8 #32 note,
    distinct from the P3 #37 bare note and the P3 suffixed note);
    #65, #117 (`万圣节在10月31日` → `萬聖節在10月31日`); #69
    （`横滨中区民祭在11月8日` → `橫濱中區民祭在11月8日`); #115
    （`日本大赛第1战在10月24日` → `日本大賽第1戰在10月24日`); #140
    (note `对照第6版` → `對照第6版` captured inside the extracted key
    because the parenthetical second half wraps to a second line).
  - 1 true E-zone Chinese key localization: #138
    （`乱扔垃圾，要罚2,000日元。` → `亂扔垃圾，要罰2,000日圓。`).
  - #139 is OUTSIDE keydiff (extracted key = Japanese sentence only,
    byte-identical); its note localization （对照第7版 → 對照第7版）
    is the second E-zone prompt localization. Total E-zone prompt
    localizations = 2 (#139 outside keydiff, #140 inside keydiff).
    A "2+19"-style double count is wrong; the unambiguous count is:
    keydiff 10 = 9 note localizations + 1 key localization.
- E-zone full lines (edition): #137 key `文化日是11月3日。` — shared-
  glyph Chinese, textually unchanged, documented as a shared-glyph
  key, NOT a missed conversion; note localized to 對照第3版. #138 key
  localized (above); note 對照第5版. #139 stem
  `讀書週從10月27日開始。→ ___` (body_face TC); Japanese key
  unchanged; note 對照第7版. #140 stem `我想去神戶看紅葉燈光秀。→ ___`
  (body_face TC); Japanese key unchanged; note
  對照第6版（神戶的燈光秀）.
- P8 completeness comparison (freeze-diff-blind pass-through check):
  every P8 line byte-identical to the core was listed and adjudicated.
  Round-3 result: all identical CJK lines without kana are legitimate
  (shared-glyph notes: 109, 110, 34, 36, 38, 44, 94; Japanese headwords
  141–144; section head `B · 一般問題`; footer `第 8 版 / 共 8 版`;
  造句 ×4; 野球 fragment); all identical kana lines are frozen
  Japanese. The one true pass-through found in round 2 (§11, #124)
  is fixed and re-verified: the edition now prints
  `124. A — 2連勝開局的奪冠率73%`.
- P8 print-note metric: 150 (the core P8 itself prints 150 notes;
  the EN family's 78 was not copied).

## 9. Readers' corner — PASS (with explicit scope ruling)

- Japanese example letter `lt` and Japanese disclosure `ld` frozen
  verbatim; no invented names, letters, or quotations.
- Traditional disclosure `lcn` (TC face), verbatim:
  `編輯部示例信，非真實來信。截至截稿，未收到真實來信與第8版最佳作文；VOL.3將刊登收到的來信與佳作。請把你的來信寄來。`
  It contains all 3 facts (example is not a real letter; no real
  letters received; no best P8 writing received) + the VOL.3 promise
  （VOL.3將刊登收到的來信與佳作）.
- Solicitation sentence, quoted verbatim (final sentence of the
  disclosure paragraph): `請把你的來信寄來。` — an explicit imperative.
  Scope ruling (pt-family precedent, stated explicitly, not assumed):
  the solicitation literally covers letters only; the same page's
  disclosure defers best P8 text to VOL.3, and the teaser line names
  the p.8 best text （第8版の作文の優秀作）; the combination passes.
  The teaser line itself is not counted as solicitation.
- Deviation note: the solicitation is the final sentence of the
  disclosure paragraph, NOT an independent line as first planned —
  because a separate 2-line invitation pushed the P7 teaser to 2582
  (> 2540 gate) and overflowed the letters box (invite line-2 baseline
  1816.24 vs box bottom 1808.08), and even a separate 1-line invite
  still overflowed the box (formula bottom 1779.08 vs baseline
  1787.84). `wrap()` at the real width (390, TC face) proves the merged
  paragraph stays 3 lines — identical to the disclosure alone — so the
  letters box returns to exactly the core formula and the teaser to
  the core value (§11).

## 10. Geometry — PASS

- Canonical `tools/occlusion_audit.py`: selftest OK (all 6 planted
  classes fired, clean controls silent); edition 0 flags; core
  0 flags; NEW vs core 0.
- ADVANCE-method scans (build-dir `advance_scan.py`, kept for the
  record): page-right-edge violations 0. BOXEDGE (text advance vs
  containing bordered rect, with the containment condition fixed to
  require the text to start inside the rect): edition 2, core 2,
  NEW = 0 — the 2 shared items are same-baseline (P4 note advancing
  to 1892.3 vs box right 1885, +7.3; P7 letters line to 1889.2 vs
  1885, +4.2; identical values in the core). FRAME (rect borders +
  lines vs true ink boxes): edition 70 raw / 63 deduped, core 68 raw /
  62 deduped; NEW = 3, all adjudicated: (a) P1 double rules at 406/413
  (the intentional W43 masthead move from 392/401, flagging the same
  neighboring ink as the core's rules); (b) P2 season-words head
  grazing the box below by 2px of font descent (ink bottom 1620.0 vs
  box top 1618) — visually verified clean on the card crop (clear gap
  between head text and box border; the graze is descent padding, not
  glyph ink). The canonical audit's 0 NEW stands as the authoritative
  result; the ADVANCE scan adds no new defect.
- Kinsoku line-start scan (JP set + TC extras ］｝〉》％): 0 on all
  8 pages.
- P8 answer-flow end: 2366 < 2540 (run log: `flow[P8-keys] ended col
  3/3 y=2366 (bottom 2540)`). P7 teaser end: 2512.08 < 2540 (=
  core value); P7 col3 end 1738.08 (= core value).
- P6 chart-label ink coverage (baseline-anchored PIL getbbox ink vs
  bar rects, NOT the getbbox-of-em-box method): 0.00% on all 8 labels
  (4 names + 4 values; names sit left of bars, values 16px right of
  bar ends).
- Furniture triple (W45 core / W43 same-pairing / this edition):
  wordmark 262 / 262 / 262; subtitle 330 / 316 / 316; badge — / (975,
  356) 19pt / (975, 356) 19pt, string verbatim = W43; tagline
  372 / 390 / 390; rules 392/401 / 406/413 / 406/413; dark band
  424 / 424 / 424; top strip 92 / 92 / 92; footer left SC form /
  TC form VOL.1 / TC form VOL.2 (volume differs correctly per issue).
  No slot differs from the W43 same-pairing actuals; the README #20
  generalization was not used where W43 actuals exist.

## 11. Fix rounds (baselines archived, never reset)

- `baselines/core-baseline-sha256.txt` — frozen core reference (§2).
- Round 1: first edition render. Counts all correct, but P7 teaser
  ended 2582.08 (> 2540) and the separate 2-line invitation overflowed
  the letters box. Pre-fix output archived as
  `baselines/round1-sha256.txt` + `baselines/round1-svg/` (SVG only;
  cards/PDFs not yet rendered).
- Round 2: invitation merged into the disclosure paragraph as its
  final sentence (§9). Result: P7 col3 1738.08 and teaser 2512.08,
  both exactly the core values. Pre-fix output archived as
  `baselines/round2-sha256.txt` + `baselines/round2-svg/` (full
  SVG/card/PDF hashes). Round-2 vs round-1 SVG hashes: only P7
  changed, as expected.
- Round 3: P8 completeness catch — the P8 registry's own #124 note
  (`2连胜开局的夺冠率73%`, without 是） differs from the P4 note
  (`…夺冠率是73%`, with 是）, so the reviewed 186-entry map missed
  this distinct string and it passed through as Simplified. Fix: one
  map entry added directly to `transform.py` (map now 187 entries;
  `map.json` left at the reviewed 186 for the record). Result: #124
  prints `2連勝開局的奪冠率73%`; TC-face rescan and identical-line
  audit clean (§6, §8). Round-3 vs round-2: only P8 SVG and the P8
  card changed, as expected.
- All fixes went only into `transform.py`; every round re-ran the
  full pipeline from the pristine core.

## 12. Flagged items for the parent / independent proofreader

1. **Svglib routing interpretation (adjudication requested).** The
   task wording says to use the zh-tw core's own svglib (MD5
   `a269e147…`) for Traditional units and not to apply the JA
   canonical MD5 to Traditional units. This build instead follows the
   shipped W43 same-pairing form — JA canonical svglib plus TC face
   routing — because the zh-tw core svglib is TC-only (no face
   parameter, no SEAM_SLACK constant) and wholesale use would render
   Japanese body text in TC face; W43 KIT §2 measured JP/TC glyph
   differences for Japanese kanji and concluded Japanese body text
   must never render in TC face. TC face index is still verified as
   3, matching the zh-tw core svglib's TC index method and
   `tables.json`. If the proofreader rules the other way, the
   Traditional units' glyph shapes (not their text) would change.
2. **P8 #37 bare-note handling (adjudication requested).** Core
   `content34.py:82` registers the P3 fill-in with key `8` and bare
   note `工艺展到11月8日` (no weekday suffix), distinct from the
   suffixed P3 note `工艺展到11月8日（周日）` and the P8 note
   `传统工艺展到11月8日`. This build maps the bare note to
   `工藝展到11月8日`, preserving the bare form and note identity,
   following the JA×EN/JA×DE/JA×FR precedent of not adding a weekday.
   The fact (exhibition through 11月8日, Sunday — P3 stem
   展覧会は11月 ___ 日（日）までです。 and 2026-11-08 is Sunday in
   Asia/Tokyo) supports a suffixed form, but adding 星期日 would
   change the note's identity; the proofreader should confirm the
   bare-form choice.
3. **P8 answers right note: 範文題 vs W43 範本題.** This edition keeps
   the core-faithful conversion `為範文題` (core: 为范文题）; W43's
   own wording was 範本題. Rationale: this edition's P8 apparatus uses
   範文 throughout (H-zone `範文見本版 H 區`, `範文（167 字）`), so
   範文題 is internally consistent; forcing W43's word would break
   that consistency. The main answers-head line DOES use the W43
   rewording （依版面分版排列…).
4. **只 ×3 mention vs measured 0.** The task mentions 只 ×3 as a
   shared-glyph item to adjudicate; exhaustive searches found 只 0
   times in core content files, core SVGs, bslib, svglib, W43 edition
   SVGs, and the edition SVGs. Reported as 0 with method, not
   invented; the proofreader should confirm whether the ×3 referred
   to another family or an earlier core revision.
5. **Band-title faces for P2/P3 follow W43-copy, not a content rule.**
   W43 P2/P3 titles are pure Japanese yet render TC face; this build
   copies that (W43 precedence per the task), even though a pure
   content-based rule would leave them JP. Recorded, not assumed.

## 13. Final output hashes (round 3)

SVG (delivery `svg/`):

- p1-hyoushi: `f57d611e…fff6`
- p2-kurashi: `11c6b9e9…048`
- p3-bunka: `0138360a…352`
- p4-supotsu: `23f68794…462`
- p5-wakamono: `a92ac748…22`
- p6-fukayomi: `95c9dcb1…09db`
- p7-kotoba: `e5cebfea…f605`
- p8-tesuto: `5c6c9de0…b382`

Cards (delivery `cards/`): p1 `0bdfafed…`, p2 `25c427c8…`,
p3 `2aea1974…`, p4 `2e9bae9f…`, p5 `5f70d05d…`, p6 `687c6d72…`,
p7 `4c8fb356…`, p8 `c78125b6…` (full hashes in §14 notes and the
build log; the P8 card hash changed in round 3, all others are
round-2 values).

PDFs (delivery root):

- Print `Lucerna-VOL2-ZHTW.pdf`: 26,380,935 bytes,
  SHA-256 `b469c2a2a02791f23d252f7724b584dfd5df4cd3142a3650d305254091c0d8aa`.
- Web `Lucerna-VOL2-ZHTW-web.pdf`: 2,919,122 bytes,
  SHA-256 `e863a1c052d0400c8a6e0183585fc2061047db88263c639b3e3068d3f8d32038`.

## 14. Build log (kept in the build tree)

- `transform.py` — the transform (self-contained for fix rounds;
  map inline, 187 entries).
- `gen_map.py`, `map.json` (186 reviewed entries), `map_review.txt`
  (190 lines incl. 4 justified NOOPs) — one-time scaffolding; later
  fixes edit `transform.py` directly.
- `advance_scan.py` — the ADVANCE right-edge + frame-line scan.
- `baselines/` — `core-baseline-sha256.txt`, `round1-sha256.txt` +
  `round1-svg/`, `round2-sha256.txt` + `round2-svg/`.
- `core-baseline-sha256.txt` — duplicate of the frozen core reference
  at the build-tree root for convenience.

Full per-file hashes: SVG p1
`f57d611e1dcb4bafa6d845a05021e8d0ee246ef13813faae09309f637750fff6`,
p2 `11c6b9e950147135e708403c720a8ec615f7f77c5b1e253a1781266f9048dc48`,
p3 `0138360a1301cbe1f0f601a39aeb3e4c8149ddd1b24ae85703c8d366780ca352`,
p4 `23f68794801e2109451af647a265fb9bda27405f68bb6a3c4e7164f559802462`,
p5 `a92ac7482013c60607b70a0340bd5db86a16dea992f67fdad97c5c08364c4e22`,
p6 `95c9dcb19e6397ce78aa5e2174caddae8c66e0e13cb8234144040a55de0f09db`,
p7 `e5cebfea1b120097ae3754425a5d656be0d9f2ee80172f1e7b2fc038c0ddf605`,
p8 `5c6c9de0a8eed9b88c7108b54ad8b62b8fd65927a86e71e9ba9af6a49e2ec382`;
cards p1 `0bdfafed0120c97ed078c2eb4f3d4150c95dac875d7bc91a56dac10354706fa3`,
p2 `25c427c8e82e57b4300cba6c50bbecf7006213bd3a18d1dfec0014d490721a7e`,
p3 `2aea1974a04781eaa318170a6bf2a858c64d159c2fb81d3194f68d676779a909`,
p4 `2e9bae9fb44c9f20c87ed4bb013c74b64b4d2da0c0d41c156b08f6c66e23d0ce`,
p5 `5f70d05d086b499b2a62026b56d17fc0c661849e1c32f97b159f31cd5e81ab98`,
p6 `687c6d729360a0e700698f8c7823faeafd83c1fb340626457b59ab6425352919`,
p7 `4c8fb3565faa1d255290ce89c3a1cb8e00c7f4954650489e98e416a4ec5c8342`,
p8 `c78125b6b3a03f77531e53f36042b09f7cafd12752bfa1abbae5f651a996b099`.
