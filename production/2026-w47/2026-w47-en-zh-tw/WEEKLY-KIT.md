# WEEKLY-KIT — 2026-W47 en-zh-tw (English target, Traditional Chinese reader)

## 1. Identity
- Slug: `2026-w47-en-zh-tw`
- Target language: English (en). Reader language: Traditional Chinese (zh-tw).
- Issue week: Monday 16 – Sunday 22 November 2026. VOL.4.
- Core: `production/2026-w47/core-en/` (en-zh-cn), copied whole, explanation layer rewritten in
  Traditional Chinese. Simplified and Traditional Chinese are independent editions — never converted
  between them; every Chinese string here is Traditional.
- Exercises: 150 (registry 150; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- MODEL words: 82.

## 2. Files delivered
- 8 SVG (`svg/p1-front.svg` … `svg/p8-test.svg`) + 8 card PNGs (`cards/`).
- Print PDF: `The-Lucerna-VOL4-en-zh-tw.pdf` — 38,152,350 bytes,
  SHA-256 `7641031186c77653ac1263056a968ba7ce2ffb9383716c5a35cfad798e0fc334`
  (CJK-font-embedding scale, like ja/ko/core-en).
- Web PDF: `The-Lucerna-VOL4-en-zh-tw.web.pdf` — 2,965,191 bytes,
  SHA-256 `e07e5dd048dad9ab1ed42daa6d33c2e9f0dea129538b957c06afe25627e0d177`
  (built only with `tools/webpdf.py`; text layer 42,852 chars, identical to the print extraction — token-multiset diff 0/0; per-page byte-identical 8/8; < 7 MB).
- `2026-w47-en-zh-tw.text.md` — 51,147 bytes, SHA-256 `57cb886738e8e23d79abe531e1f03ee7372560c5020ff02d4d6997ea117651b3`, exported from the build source (never from the PDF);
  stub registry 150 = real registry 150.
- `ABSTRACT.txt` — one line, Traditional Chinese, no ASCII double quotes.
- `registry.json` — fresh dump (150 keys), copied over the stale core copy from apply.py.
- `svglib.py` is the W46 en-zh-tw file wholesale (apply.py does this for ja/zh-tw only) — verified
  byte-identical to `2026-w46-en-zh-tw/svglib.py`.

## 3. Gates (all green, re-run fresh 2026-11-11 after the two fixes)
- run.py exit 0; 0 FLOW OVERFLOW / HEAD TOO WIDE after the P2 fix; every Flow end y ≤ its bottom
  (P8-keys 2137/2560; P2-feature 1528/1540 — tight, 12pt spare, visually clean;
  P2-ex 2532/2560).
- occlusion audit: 0 flags (selftest OK).
- p8 extract: 60/150 noted (same set as core); compare CLEAN; keydiff [137, 138, 139, 150]
  (expected: key 140 "打破沉默。" is script-identical in Simplified and Traditional, so it does
  not differ from the core — the only edition whose keydiff omits 140, by identity, not by error).
- freeze baseline tool: 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs: 8/8 MATCH.
  Freeze diff: added CJK = 775 characters (the Traditional layer; most Traditional strings share
  characters with the Simplified core, so the added count is lower than ja/ko); removed = core
  Simplified Chinese layer.
- print/web text token-multiset diff: 0/0 (42,852 chars each; token-multiset diff 0/0; per-page byte-identical 8/8).
- `check_s11.py zh-tw`: ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19;
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min font 13.5 pt ≥ 9.75;
  chip-rect counts = core per page; Q113–120 options line with [A2] tag present;
  "Levels: 145–149 [A2]" present; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　寫作 [B1]" present).
- **Script gate (OpenCC s2t, this edition only):** registry.json + text.md + all 8 SVGs convert
  to themselves with 0 differences (re-run in this rebuild — see §5 item 4 for the first-build
  宣佈 fix that closed it) — zero Simplified characters anywhere in the edition's deliverables.

## 4. Translation decisions (Traditional Chinese)
- Follows W46 zh-tw (TM): instructions （填空/改寫/糾錯）; gloss format "term = translation",
  "·" separators, "譯注｜" box prefix (bslib4 gloss() prepends it; gloss translations are bare —
  only the P1 bridge carries its own label, "譯注｜", via f.bridge at the default 20.5pt, the
  W46 zh-tw convention — the W46 bridge uses f.expl, which is the same para call).
  No bridge-size patch for zh-tw (p1_bridge_size None).
- "runoff" = "第二輪投票"; "call a race" = "宣佈結果"; "to certify" = "正式確認";
  "midterm" = "期中選舉"; "seat" = "席位"; theme "Break the Silence" = "打破沉默".
- Numbers box keeps the English term with a Traditional gloss in parentheses (W46 zh-tw precedent:
  "Nov 11, 11:00 — the silence（默哀） · 1918 — the armistice（停戰）").
- P2 calendar lines follow the same W46 precedent (English + Traditional gloss), NOT full-Chinese
  dates: "Nov 10 — House Republicans choose their leader（眾議院共和黨選領袖） ·
  Nov 18–19 — House Democrats vote（眾議院民主黨投票）" /
  "Nov 20 — World Children's Day（世界兒童日） · Nov 26 — Thanksgiving（感恩節） ·
  Nov 27 — Black Friday（黑色星期五）".
- SAY IT title = "這樣說日期" (date, not clock time — the de D-de1 lesson).
- P1 word-of-week bridge pre-shortened to 2 lines: "期中選舉：眾議院全部席位，參議院約三分之一席位。"
  (fr/es lesson).
- TM types (used as-is, 7): 翻译→"翻譯", 写作→"寫作", 阅读理解→"閱讀理解", 单选→"單選",
  词汇配对→"詞彙配對", 句型转换→"句型轉換", 对话补全→"對話補全". TM instr (3): 把词和释义配对→
  "把詞和釋義配對", 改写→"改寫", 配对→"配對".
- **Identity mappings (zh-tw only — the TM stores differing pairs only, so script-identical
  literals must be mapped to themselves or apply.py flags them unmapped):** instr 填空→"填空";
  types 完形填空→"完形填空", 完成句子→"完成句子"; lit identity entries: '11 月 = November',
  'A　CLOZE　完形填空', 'CULTURE　文化', 'LIFE　生活', 'YOUTH　青年', 'official = 正式的',
  'whether = 是否', '八位 = eight'.
- Fresh sets: instr 纠错→"糾錯"; types 从句→"從句", 将来时→"將來時", 时态→"時態",
  比较填空→"比較填空", 过去时→"過去時", 金句填空→"金句填空", 纠错→"糾錯",
  图表读数→"圖表讀數" (overrides the poisoned TM value "sans").
- ekeys: 137 "民主黨贏下了眾議院和參議院。", 138 "計票仍在繼續。",
  139 "新國會將於 2027 年 1 月開會。", 140 "打破沉默。" (identity — script-identical),
  150 "開放題 — 要點見寫作框，範文在第 8 版寫作框內" (dash form, from the TM —
  no override needed).
- Box titles (single-line): "ERROR CLINIC　糾錯門診", "READERS' CORNER　讀者來信",
  "AN EXAMPLE LETTER　示例信", "THE TOOLBOX　句型工具箱", "NEXT WEEK　VOL.5預告",
  "SENATE IN NUMBERS　參議院數字" (core fix1 dropped "THE"), "HOW LONG?　任期多長？",
  "ODD SOCKS, IN NUMBERS　奇襪日", "SATURDAY, NOV 21　週六賽程" (core fix1 title),
  "HAYMITCH'S GAMES　海米奇的比賽",
  "THE CALENDAR　本週日曆" — all fit, no collision (occlusion 0 flags; P2 card checked: the
  SENATE title ends well clear of "Second story").
- P8 section heads use TM short labels ("完成句子與轉換", "範文") that differ from the registry
  type names ("完成句子", "句型轉換", "寫作") — same pattern as fr/es/it/pt/nl/ru/ja/ko.

## 5. Fixes in this round (→ rebuild + re-render + full re-gate each)
1. **P2-ex FLOW OVERFLOW on the first run** (y=2946/2560 — the same number as ko's first run).
   Root cause (ko lesson): the W46 TM B bridge wraps to 2 lines; the early extra line cascades
   through the 4-column flow packing. Fix: `lit_overrides` → "用 will + 動詞原形改寫（承諾）。"
   (1 line). Re-run: P2-ex ends 2532/2560.
2. **Simplified character 布 in the Q2/Q95 registry notes** ("call a race = 宣布競選結果").
   The W46 zh-tw TM itself carries it (W46 content56.py:107/148) — a conversion gap shipped in
   W46. The notes only appear in registry.json + text.md (Q2/Q95 are not in the noted set, so
   they never render in the SVGs/PDFs — verified by grep). Fix: `lit_overrides` →
   "call a race = 宣佈競選結果". OpenCC s2t re-check on the fresh registry + text.md: 0
   differences — the only simplified residue in the whole edition, now closed.
   **Process slip (mine):** the first override edit REPLACED the lit_overrides dict instead of
   merging, silently dropping the B-bridge fix — the re-run overflowed again (2946) and caught
   it. Lesson: when adding a second lit_override, merge into the existing dict, never assign a
   fresh one; verify both overrides are present in map-<lang>.json before applying.
3. P8 key size 13.5/1.26 is the W46 zh-tw extracted value already (P8-keys ends 2137/2560).
4. **Rebuild + fix1 (11 Nov 2026, core-en fix1 sync — this round).** Core-en was fixed and
   re-proofed (Q39→a, Q40→d, Ashes rewritten as a 2025–26 retrospective, 已宣布 wording,
   SEARCHES/DID YOU KNOW box heights, SENATE/SATURDAY titles, SAY IT middle panel widened)
   and this edition was rebuilt from the fixed core via `scratch-fanout-en2/fanout/apply.py` +
   patched `map-zh-tw.json` (14 new literals: Q39/Q40 keys + notes, Q46/Q52/Q55/Q125 notes,
   SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge). All 9 proof1 defects
   were core-level (zero edition-level) and are resolved by the rebuild (verified per edition:
   registry keys 39=a/40=d, notes `mentor = 導師 a` / `arena = 競技場 d`; Q46 note dated
   Fri 21 Nov 2025; Q52 `hosted`, Q55 `won`, Q125 `A (4–1)`; text.md answers 39→a, 40→d,
   125→A; `Arsenal are winning!`; no `Perth is winning!` / `second week in Perth` /
   `Ashes begin`). The old ABSTRACT was short-form (§9-class, like ja D4) and was rewritten
   to the full form (announced results; certification 10 Nov–18 Dec; 16 Nov Anti-Bullying/Odd
   Socks; 20 Nov Children's Day + Hunger Games; 21 Nov Premier League back + Turin ATP final +
   Ashes 4–1 look-back; reader language; A2–B2; 150). The §5 item 1 P2-ex bridge fix
   ("用 will + 動詞原形改寫（承諾）。") and item 2 宣佈 fix both survive the rebuild (they live
   in the map, re-applied) — P2-ex ends 2532/2560 as before.
   **New script issue found by this round's OpenCC s2t self-check (first build):** the 6 new
   已宣布 literals came through the map as 已宣布 with 布 — OpenCC s2t flagged 4 diffs in
   registry.json, 6 in text.md, 5 in the SVGs, every one 布→佈 in 已宣布. 布 is not a
   Simplified leak in the strict sense (宣布 is standard Traditional too), but this edition's
   own precedent (§5 item 2) writes 宣佈 with 佈, and the §3 script gate requires 0 s2t
   differences — so the 6 map values were patched 宣布→宣佈 (P1 strip, Q7/Q82/Q83/Q84 notes,
   P6 bridge), full rebuild + re-gate. Re-check after the rebuild: registry.json, text.md and
   all 8 SVGs convert to themselves with **0 differences**; 宣佈 13× in text.md, 9× in
   registry.json; 宣布 0× anywhere. (The `opencc` binary is not installed on this VM; the
   check used the Python `opencc` package in the repo venv, `OpenCC('s2t')`.)
   **Correction (2026-11-11, proof1 D1):** the "0× anywhere" claim above missed one place —
   ABSTRACT.txt was outside that self-check's scope (§3 script gate lists registry.json +
   text.md + 8 SVGs only) and still carried one 已宣布結果. It has since been changed to
   已宣佈結果 (one character, 布→佈) and re-checked with the same OpenCC s2t method:
   ABSTRACT.txt now converts to itself with 0 differences. The §5 item 4 history above is
   unchanged; this note is the only addition.
5. **Rebuild gates (11 Nov 2026, second build of this round; logs in
   `hidden_files/w47/scratch-fanout-en2/fanout/zh-tw/build-gates.log`)**: `run.py` exit 0, zero
   OVERFLOW / TOO WIDE, all flows within bottom, TOTAL 150, MODEL 82; `occlusion_audit.py`
   0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as core); `p8.py compare`
   CLEAN, keydiff=[137, 138, 139, 150] (expected — key 140 "打破沉默。" is script-identical
   in Simplified and Traditional, so it does not differ from the core); registry vs P8
   extract 149/150 exact + n=150 short-label exception; registry keys vs core 145/150 (diff
   only the 5 reader-language keys 137–140, 150); `freeze.py baseline` 8/8 SVGs byte-identical;
   `freeze.py diff` TOTAL added CJK 775; print/web text layers 42,852 chars each,
   token-multiset diff 0/0, per-page byte-identical 8/8; `check_s11.py` ALL PASS; source
   boxtitle sweep 12/12 fit; SVG boxtitle sweep 18/18 fit; canonical `creambox.py` scan: all
   inside-only clearances positive; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK
   (Traditional layer — OpenCC s2t 0 differences, see above).

## 6. Self-check (2026-11-11)
- Full read of `2026-w47-en-zh-tw.text.md` (all ~1,306 lines): zero issues (after the two fixes).
  Notes kept: Q2/Q95 note "call a race = 宣佈競選結果" (fixed — see §5); Q13 "(決勝輪 12 月 1 日)"
  is Traditional throughout （決勝輪）; Q6/Q10/Q12 "新國會2027年1月開會" terse as in core (no
  spaces around the year — the TM value); Q11 "11 月 = November" is the identity-mapped literal;
  Q34 "(open = 上映（第三人稱單數加 s）)" correct; Q54 "eight (八位 = eight)" follows the core's
  tautological note pattern; Q89 "正式結果來自各州認證" correct; Q97 "take time = 花時間" correct;
  Q110 "more than結構" terse as in core; Q136 "whether = 是否" vs Q105
  "whether = 是否（不知道的事）" — two source literals, both correct; "五句影評｜who、where、
  發生了什麼、轉折、結局——五句就夠。" is the W46 zh-tw TM value for the FIVE SENTENCES bridge
  (kept); "看球英語｜比數、誰得分、誰領先——短句就是直播英語。" and "一張地圖｜五十個州、五十套
  規則——所以選舉夜看的是地圖，不是一個數字。" are W46 zh-tw TM values (kept, Taiwanese 比數);
  "DEEP READ · 時事深讀" and "YOUTH · 青年" are the W46 zh-tw heads (kept).
- All 8 cards visually checked after the final render — clean. P1: bridge 2 lines clear of
  IN BRIEF, numbers box English+gloss, "TRY IT NOW · 即學即練", footer "第1版／共8版".
  P2: calendar English+gloss, "THE SENATE, IN NUMBERS · 參議院數字", SAY IT "這樣說日期",
  gloss single "譯注｜to certify = …", B bridge 1 line. P3: "COMING SOON · 即將上映",
  "HAYMITCH'S GAMES · 海米奇的比賽", gloss single "譯注｜a tribute = …", Rousseau tiger.
  P4: "SATURDAY, NOV 21 · 週六賽程" (core fix1 title), gloss single "譯注｜a Test = …", W. G. Grace photo; P4 lead is the Ashes 2025–26 retrospective "Perth, One Year On: How Australia Kept the Ashes".
  P5: "ODD SOCKS, IN NUMBERS · 奇襪日", gloss single "譯注｜bullying = …",
  "SPEAK UP · 大聲說出來", Lawrence children photo. P6: "HOW LONG? · 任期多長？",
  gloss single "譯注｜to call a race = 宣佈結果 · …", "A PRACTICE BALLOT · 模擬選票",
  voting booth photo. P7: all gloss boxes single "譯注｜", "THE TOOLBOX · 句型工具箱",
  "READERS' CORNER · 讀者來信", "AN EXAMPLE LETTER · 示例信", "ERROR CLINIC · 糾錯門診",
  "NEXT WEEK · VOL.5預告", Johnson portrait. P8: cloze + [A2] option tags,
  "B MULTIPLE CHOICE · 單選", "C READING · 閱讀理解", "D SENTENCES · 完成句子與轉換",
  "E TRANSLATION · 翻譯" with "翻譯：", "F WORDS · 詞彙配對", "G DIALOGUE · 對話補全" +
  "Levels: 145–149 [A2]", "H WRITING · 寫作 [B1]" + Traditional instruction, MODEL + Reading
  Room photo, ANSWERS block all 150 keys ending well above the footer with "150. 開放題 —
  要點見寫作框，範文在第 8 版寫作框內 (按要點給分)"; footer "第8版／共8版".

## 7. Furniture
- foot_left "The Lucerna　英語週報 VOL.4　正文英語　講解繁體中文";
  foot_right "第{n}版／共{total}版"; gloss_prefix "譯注｜"; p8_sep "— 第{pg}版 —";
  translate prefix "翻譯："; badge "英語正文　繁體中文講解 — 給繁體中文讀者的版本";
  topstrip "WEEKLY IN ENGLISH　每週一期　讀英語世界正在談的事";
  edition line "英語週報　VOL.4　選舉　叢林　電影"; edition spacing 11.5;
  p1_bridge_size None (default 20.5, W46 zh-tw convention); p8_mode "notes".

## 8. Provenance
- TM: W46 `2026-w46-en-zh-tw` positional alignment (228 pairs — fewer than the 260 of the other
  languages because it stores differing pairs only). Poisoned values caught:
  'note' → 'P8 saved, TOTAL exercises:' (harmless, rejected by build_map's POISON regex);
  '图表读数' → 'sans' (overridden by fresh type "圖表讀數").
  'THE ERROR CLINIC　易错诊所' → 'THE ERROR CLINIC　易錯診所' is a legitimate conversion, not poison.
- Map: `scratch-fanout-en2/fanout/map-zh-tw.json` (lit 245, instr 5, type 17, ekey 4).
  Misses: 216 total, 193 with real CJK = 179 lit + 10 types/instr + 4 ekeys (11 more than the
  other languages — the 8 script-identical lit + 3 script-identical type/instr entries).
  build_map normalizes U+2019 → ASCII apostrophe in all map values (fr lesson).
- F-MAIL: no real letters arrived; P7 prints the labelled editor's example + the VOL.3
  disclosure promising real letters from VOL.5. No invented letters, no email checked.

## 9. Build record
- `scratch-fanout-en2/fanout/zh-tw/` — build-gates.log, make_textmd_w47.py, occlusion.log/json,
  p8-extract/compare.json, freeze.log/diff.json, webpdf.log, textmd.log, registry.json, dump_reg.log,
  freeze-final/.

## 10. Tool note (NOT fixed — p8.py is off-limits to the builder)
- `tools/p8.py` FOOTER_RE does not match the mixed-case footer "The Lucerna …" + "第 8 版／共 8 版":
  the merged footer line leaks into the last answer segment (key 150) for every edition.
  Masked when key 150 is dash-style (zh-tw, ko, ja, ru, nl, pt, it, fr, de), bites when
  paren-style without a dash (es, before its fix). A case-insensitive match on the masthead, or
  dropping the merged footer line by its y=2624 baseline, would close it.
- Occlusion audit gap (found in the nl round): the audit does not flag a box title running into live
  text in the neighbouring column. A title-vs-neighbour text proximity check would close it.
- Flow gap (found in the ko round): `match_set`'s keep-together `_fit` clamps a block to the page
  bottom when it doesn't fit in the last column. The run-gate's flow-end check catches it.
- TM conversion gap (found in this round): the W46 zh-tw TM carries an unconverted Simplified
  character (布 in "宣布"). A script gate (OpenCC s2t, 0 differences) belongs in the builder's
  checklist for zh-tw — and the same check would catch a Traditional character leaking into a
  Simplified edition.
