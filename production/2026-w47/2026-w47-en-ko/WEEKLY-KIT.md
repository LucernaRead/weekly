# WEEKLY-KIT — 2026-W47 en-ko (English target, Korean reader)

## 1. Identity
- Slug: `2026-w47-en-ko`
- Target language: English (en). Reader language: Korean (ko).
- Issue week: Monday 16 – Sunday 22 November 2026. VOL.4.
- Core: `production/2026-w47/core-en/` (en-zh-cn), copied whole, explanation layer rewritten in Korean.
- Exercises: 150 (registry 150; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22).
- MODEL words: 82.

## 2. Files delivered
- 8 SVG (`svg/p1-front.svg` … `svg/p8-test.svg`) + 8 card PNGs (`cards/`).
- Print PDF: `The-Lucerna-VOL4-en-ko.pdf` — 30,159,302 bytes,
  SHA-256 `dacad9cca89b724500adf7c4eb1990ea3aadaf6f22bd65f4c315ea580e7233a0`
  [D5 rebuild, 12 Nov 2026 — see §3; pre-D5 values were print `c892247f…` 32,386,301 B,
  web `e8f6f94a…` 2,629,430 B.]
  [F1 fix, 12 Nov 2026 — see F1 bullet below; pre-fix values were print `aef89be3…` 30,158,892 B,
  web `e5ca7843…` 2,534,848 B.]
- Web PDF: `The-Lucerna-VOL4-en-ko.web.pdf` — 2,535,257 bytes,
  SHA-256 `7c486f7d60aac42e310f7d9ad7120e1a6385d65aaceca1757ce9b4151d462e4a`
  (built only with `tools/webpdf.py`; text layer 49,760 chars incl. whitespace, identical to the print extraction — token-multiset diff 0/0; per-page byte-identical 8/8; < 7 MB).
- `2026-w47-en-ko.text.md` — 53,758 bytes, SHA-256 `b5592fecb7afb30f1e22f865fe0a416dfd7dd9cc8b70319a7f6ad89cce6638bc`, exported from the build source (never from the PDF);
  stub registry 150 = real registry 150. Re-exported in the F1 fix (12 Nov 2026, see F1 bullet below; pre-fix 53,587 B `08d87476…`).
- `registry.json` — fresh dump (150 keys), SHA-256 `56f6620b5741bce7b6c8474e4f691ccb3bd909d3809f6bdc5b0848ac54cf732a`.
- **F1 fix (12 Nov 2026, proof-round defect F1 — Georgia runoff written as pending; work log in `hidden_files/w47/scratch-fix-en/FIX-LOG.md`, gates in `hidden_files/w47/scratch-fix-en/logs/2026-w47-en-ko/`):** P2 :185 + P6 :651 rewritten as settled law + result (Georgia law calls for a Dec 1 runoff only if no one wins a majority — AP called Jon Ossoff reelected 3 Nov, ~59%, so no runoff). Q13/Q142 untouched (rule questions, answers still 1 December). Source `content12.py:171` + `content56.py:103`; text.md re-exported with `scratch-fix-en/make_textmd_fix.py` (diff exactly the 2 lines, no title lost — all 7 D5-shrunk box titles present). Full rebuild + gates ALL-GREEN: run rc=0 TOTAL 150 MODEL 82, 0 overflow; head_check PASS; occlusion 0 flags (selftest OK); p8 extract 60/150, compare CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); freeze baseline 8/8; spill 0; boxtitle 0; edge 0; creambox PASS; census PASS; print/web text layers byte-identical. New deliverables: print 30,159,302 B SHA-256 `dacad9cca89b…` (was 30,158,892 B `aef89be3…`), web 2,535,257 B `7c486f7d…` (was 2,534,848 B `e5ca7843…`), text 53,758 B `b5592fec…` (was 53,587 B `08d87476…`); text layer 49,760 chars incl. whitespace (was 49,556).
- `ABSTRACT.txt` — one line, Korean, no ASCII double quotes.
- `ABSTRACT.txt` — one line, Korean, no ASCII double quotes.
- `registry.json` — fresh dump (150 keys), copied over the stale core copy from apply.py.

## 3. Gates (all green; verified 2026-11-11 after a VM restart cut the gates run — see §5)
- run.py exit 0; 0 FLOW OVERFLOW / HEAD TOO WIDE after the P2 fix; every Flow end y ≤ its bottom
  (P8-keys 2205/2560; P2-feature 1438/1540; P2-ex 2532/2560).
- occlusion audit: 0 flags (selftest OK).
- p8 extract: 60/150 noted (same set as core); compare CLEAN; keydiff [137, 138, 139, 140, 150]
  (reader-language translation keys + writing key — expected).
- freeze baseline tool: 8/8 byte-identical; direct sha256 re-render vs shipped core SVGs: 8/8 MATCH
  (re-run by hand after the restart wiped the gates stdout log).
  Freeze diff: added CJK = 2,323 characters — the Korean layer itself (Hangul 2,309/2,323 = 99.4%,
  U+3000 9); removed = core Chinese layer. No leftover Simplified Chinese verified: 0 hits for
  中期选举/众议院/民主党赢下/参议院/星期五/金句/范文 etc. in the SVGs.
- print/web text token-multiset diff: 0/0 (43,897 chars each; token-multiset diff 0/0; per-page byte-identical 8/8).
- `check_s11.py ko`: ALL §1.1/P8 CHECKS PASS (colour set core 19 = edition 19;
  badge colours A2 #5c6e30 / B1 #46581f / B2 #37402f; P8 min font 13.5 pt ≥ 9.75;
  chip-rect counts = core per page; Q113–120 options line with [A2] tag present;
  "Levels: 145–149 [A2]" present; Q120 [A2] chip OK;
  P8 WRITING head "H　WRITING　쓰기 [B1]" present).
- **D5 rebuild + gates (12 Nov 2026; full log `hidden_files/w47/scratch-d5-rebuild-en/logs/2026-w47-en-ko/GATES-SUMMARY.txt`)**: SOP §1.1 font fix — installed via `scratch-d5-plan/mechanism/apply_variant.py --target en --reader ko` (mode cjk, D5 block in this edition's `svglib.py`, `_D5_READER = "cjk"`; script-based routing, no `_READER_LANG` gate; routing unit-checked with the latin case set + `_D5_READER == "cjk"`: FAILURES: 0; U+201C fix2 routing preserved — `census_quotes.py`: 0 defective, all 164 curly quotes in Newsreader; KR quotes not extended per CJK-DECISION §3). Pre-fix census: 378 Latin-in-CJK-sans elements. Post-fix defect, D5-caused: P3 cream-box title `HAYMITCH'S GAMES　헤이미치의 경기` +32.9 px right → `tsize` 23 → 20 (`content34.py:82`). Layout only, text unchanged. Pre-fix baseline reconstructed (no pre-D5 snapshot existed for CJK editions): pre-fix print PDF `c892247f…` (32,386,301 B) + web PDF `e8f6f94a…` (2,629,430 B) + SVGs + text.md from `scratch-delta-en-ko/freeze-baseline-edition/build-copy/` (SHA-verified against the KIT-recorded values; the Nov-11 `scratch-fanout-en2/backup/` copy is stale — editorial fixes landed after it). Freeze gate ran under the venv (no Pillow-10 ABORT; system python3 carries Pillow 10.2.0 as the fallback, unused). Gates: run rc=0 TOTAL 150, MODEL 82, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; `head_check.py` PASS 0 defects; `render.py` + `webpdf.py` rc=0; `occlusion_audit.py` 0 flags (selftest OK); `p8.py extract` 60/150 (same set), `compare` **CLEAN**, keydiff=[137, 138, 139, 140, 150] (expected); `freeze.py baseline` **8/8**; `freeze.py diff` vs core-en TOTAL added CJK 2,323 (the Korean layer itself — Hangul 2,309/2,323 = 99.4%, U+3000 9; same count as the pre-D5 KIT note), added Latin strings 139 (D5 run-splitting); `spill_sweep.py` 0 SPILL (175 OBSERVE); `boxtitle_check.py` 0 DEFECT / 0 OBSERVE / 0 marginal (45 titles, 379 body lines); `pdf_edge_scan.py` 0 TOUCH, 0 NEAR; `d5_creambox_audit.py` **PASS 0 defects** (ratios n=430 median 1.025, bold 1.053; rerun after adding the baseline `svglib.py` + `assets/` to the backup dir — the first run failed to load the baseline module, not a defect); `d5_census.py` **PASS** — D5 Latin 0, Cyrillic 0, curly in CJK 0, 164 curly in Newsreader, `Noto Sans` elements 0; print/web `pdftotext` byte-identical, 49,556 chars incl. whitespace (pre-fix 49,708; −152 whitespace-only, non-space multiset 34,372 identical pre/post); text.md byte-identical (`08d87476…`, 53,587 B). P8: 185 → 184 lines, footer slack 44.0 → 37.6 px. **OVERALL: ALL-GREEN.** Pre-D5 baselines: print `c892247f…` (32,386,301 B), web `e8f6f94a…` (2,629,430 B); new SHAs in §2 (print `aef89be3…`, web `e5ca7843…`).

## 4. Translation decisions (Korean)
- Follows W46 ko (TM): instruction noun-phrases (빈칸 채우기, 바꿔 쓰기, 단어와 뜻 짝짓기,
  오류 고치기); gloss format "term = translation", "·" separators, "해설 — " box prefix
  (bslib4 gloss() prepends it; gloss translations are bare — only the P1 bridge carries its own
  label, "해설 — "). No bridge-size patch for ko (p1_bridge_size None — the W46 ko bridge renders
  at the default 20.5pt, verified in content12.py:42).
- "runoff" = "결선 투표"; "call a race" = "선거 결과를 발표하다" (TM);
  "to certify" = "공식 확인하다" (TM); "midterm" = "중간 선거"; "seat" = "의석";
  theme "Break the Silence" = "침묵을 깨라".
- Numbers box keeps the English term with a Korean gloss in parentheses (W46 ko precedent).
- P2 calendar lines in full-Korean short form (es precedent — avoids the fr P2 overflow):
  "11월 10일 — 공화당이 대표를 뽑다 · 11월 18–19일 — 민주당이 투표하다" /
  "11월 20일 — 세계 아동의 날 · 11월 26일 — 추수감사절 · 11월 27일 — 블랙프라이데이".
- SAY IT title = "날짜를 말하는 법" (date, not clock time — the de D-de1 lesson).
- P1 word-of-week bridge pre-shortened to 2 lines: "중간 선거: 하원은 전 의석, 상원은 3분의 1。"
  (fr/es lesson).
- TM types (used as-is): 完成句子→"문장 완성", 翻译→"번역", 写作→"쓰기", 阅读理解→"읽기 이해",
  单选→"객관식", 完形填空→"빈칸 채우기", 词汇配对→"단어 짝짓기", 句型转换→"문장 바꾸기",
  对话补全→"대화 완성". TM instr: 填空→"빈칸 채우기", 把词和释义配对→"단어와 뜻 짝짓기",
  改写→"바꿔 쓰기", 配对→"짝짓기".
- Fresh sets: instr 纠错→"오류 고치기"; types 从句→"종속절", 将来时→"미래형", 时态→"시제",
  比较填空→"비교", 过去时→"과거형", 金句填空→"명문장 빈칸 채우기", 纠错→"오류 고치기",
  图表读数→"그래프 읽기" (overrides the poisoned TM value "sans").
- ekeys: 137 "민주당은 하원과 상원에서 승리했다.", 138 "개표가 계속되고 있다.",
  139 "새 의회는 2027년 1월에 개회한다.", 140 "침묵을 깨라.",
  150 "열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에" (dash form, from the TM —
  no override needed).
- Box titles (single-line, short forms): "ERROR CLINIC　오류", "READERS' CORNER　독자의 편지",
  "AN EXAMPLE LETTER　보기", "THE TOOLBOX　도구 상자", "NEXT WEEK　VOL.5 예고",
  "SENATE IN NUMBERS　상원" (short gloss, nl lesson applied pre-emptively; core fix1 dropped
  "THE"), "HOW LONG?　임기의 길이", "ODD SOCKS, IN NUMBERS　숫자로",
  "SATURDAY, NOV 21　토요일" (core fix1 title), "HAYMITCH'S GAMES　헤이미치의 경기",
  "THE CALENDAR　이번 주 달력" — all short forms, no collision (occlusion 0 flags).
- P8 section heads use TM short labels ("문장 완성과 바꾸기", "모범 답안") that differ from the
  registry type names ("문장 완성", "문장 바꾸기", "쓰기") — same pattern as fr/es/it/pt/nl/ru/ja.

## 5. Fixes and incidents in this round
1. **P2-ex FLOW OVERFLOW on the first run** (y=2946/2560, need 362) — the only overflow in the
   whole fan-out. Root cause (diagnosed from the SVG + bslib4 Flow code): the W46 TM B bridge
   "will + 동사원형으로 바꿔 쓰세요(약속과 앞으로 일어날 일)." wraps to 2 lines; that one early
   extra line shifts the 4-column flow packing so a question spills columns, and `match_set`'s
   keep-together `_fit(362)` then clamps the D block to the page bottom (the 333pt dead gap) —
   a 29pt excess cascading into a 386pt overflow. Fix: `lit_overrides` in fresh-ko.json →
   "will + 동사로 바꿔 쓰세요(약속)。" (1 line). Re-run: P2-ex ends 2532/2560 — exactly ja's
   number. Lesson for zh-tw: **verify every reused TM bridge fits on ONE line** (same trap as
   de's SAY IT, fr's bridges, ja's separator) — a 1-line excess early in a 4-column flow
   cascades; check the P2-ex flow end on the first run, and shorten the bridge, not the questions.
2. **VM restart SIGTERM'd the gates run** (2026-11-11 ~05:25, same as the es incident): /tmp log
   wiped, text.md step never ran. Recovered the es way: completed steps verified fresh from
   their artifacts (dump_reg, occlusion, p8, freeze, webpdf all timestamped 05:21–05:25);
   re-ran only the direct-sha check (8/8), the print/web diff (0/0), print SHA/size, and the
   text.md export (RC=0, 150/150). No re-render needed (SVGs untouched).
3. P8 key size 13.5/1.26 is the W46 ko extracted value already (P8-keys ends 2205/2560).
4. **Rebuild + fix1 (11 Nov 2026, core-en fix1 sync — this round).** Core-en was fixed and
   re-proofed (Q39→a, Q40→d, Ashes rewritten as a 2025–26 retrospective, 已宣布 wording,
   SEARCHES/DID YOU KNOW box heights, SENATE/SATURDAY titles, SAY IT middle panel widened)
   and this edition was rebuilt from the fixed core via `scratch-fanout-en2/fanout/apply.py` +
   patched `map-ko.json` (14 new literals: Q39/Q40 keys + notes, Q46/Q52/Q55/Q125 notes,
   SATURDAY/SENATE titles, P1 strip, Q7/Q82/Q83/Q84 notes, P6 bridge). Proof1 defects D1–D2
   were core-level and are resolved by the rebuild (verified per edition: registry keys
   39=a/40=d, notes `mentor = 멘토 a` / `arena = 경기장 d`; Q46 note dated Fri 21 Nov 2025;
   Q52 `hosted`, Q55 `won`, Q125 `A (4–1)`; text.md answers 39→a, 40→d, 125→A;
   `Arsenal are winning!`; no `Perth is winning!` / `second week in Perth` / `Ashes begin`).
   **D3 (edition-level) fixed in the map**: P5 ODD SOCKS title `ODD SOCKS, IN NUMBERS　숫자로 보기`
   (424.1 px, −19.6) → `ODD SOCKS, IN NUMBERS　숫자로` (375.4 px, +29.1). The old ABSTRACT
   was short-form (§9-class, like ja D4) and was rewritten to the full form (announced results;
   certification 10 Nov–18 Dec; 16 Nov Anti-Bullying/Odd Socks; 20 Nov Children's Day + Hunger
   Games; 21 Nov Premier League back + Turin ATP final + Ashes 4–1 look-back; reader language;
   A2–B2; 150). Tight but passing, recorded: P3 HAYMITCH title `HAYMITCH'S GAMES　헤이미치의 경기`
   measures 401.9 px (+2.6 advance, +2.5 true ink) — genuinely tight but inside, no fix.
   The §5 item 1 P2-ex bridge fix ("will + 동사로 바꿔 쓰세요(약속)。") survives the rebuild
   (it lives in the map, re-applied) — P2-ex ends 2532/2560 as before.
5. **Rebuild gates (11 Nov 2026; logs in `hidden_files/w47/scratch-fanout-en2/fanout/ko/build-gates.log`)**:
   `run.py` exit 0, zero OVERFLOW / TOO WIDE, all flows within bottom, TOTAL 150, MODEL 82;
   `occlusion_audit.py` 0 flags, selftest OK; `p8.py extract` noted set 60/150 (same set as
   core); `p8.py compare` CLEAN, keydiff=[137, 138, 139, 140, 150] (expected); registry vs P8
   extract 149/150 exact + n=150 short-label exception; registry keys vs core 145/150 (diff
   only the 5 reader-language keys 137–140, 150); `freeze.py baseline` 8/8 SVGs byte-identical;
   `freeze.py diff` TOTAL added CJK 2,323; print/web text layers 43,897 chars each,
   token-multiset diff 0/0, per-page byte-identical 8/8; `check_s11.py` ALL PASS; source
   boxtitle sweep 12/12 fit; SVG boxtitle sweep 18/18 fit; canonical `creambox.py` scan: all
   inside-only clearances positive; P8 min PDF font 10.12 pt ≥ 9.75 pt; SVG zero real CJK
   (Korean Hangul, not Chinese — 0 hits for the Simplified-only check strings).
6. **Delta Q73 (11 Nov 2026, proof1 D4 — the ONLY change in this round; gates in
   `hidden_files/w47/scratch-delta-en-ko/DELTA-NOTE.md`).** core-en fix2 changed the Q73 key
   `"speak"` → `"up"` (stem `Speak ___: tell a teacher.`, note `speak up = …` untouched);
   this edition synced the same single key in `content56.py:49` and rebuilt
   (`run.py` / `render.py` / `tools/webpdf.py`, registry + text.md re-derived). Registry diff
   exactly 1 entry (n=73 speak→up); text.md diff exactly 1 line (answer 73); Q73 four-source
   consistent `up` (registry, text.md, P8 printed key, P5 stem + `to speak up` gloss). SVG
   scope: ONLY `p8-test.svg` changed — P5 is byte-identical, as expected (the key only ever
   prints on the P8 answers page; P5 prints only the `Speak ___` blank + the `speak up` note,
   verified by grep, not assumed). D1/D2/D3 verified unregressed (P4 retrospective
   title intact, 39=a/40=d, ODD SOCKS short title intact). Full gates re-run green
   (run rc=0 / TOTAL 150 / 0 overflow; freeze baseline 8/8 (edition build dir) + core
   read-only对照 8/8;
   freeze diff 2323; occlusion 0 flags; p8 extract 60/150 + compare CLEAN keydiff
   [137–140, 150]; keycheck 149/150 + #150; print/web text 107,720 bytes each, cmp
   identical, spans identical; P8 min font 10.125 pt; creambox/boxtitle/ink identical to
   proof1; 8 pages + web P1/P8 visually clean). Stem-fit audit: all 57 blank stems + cloze
   (112–119) + dialogue (145–149) re-checked with keys substituted, 0 flags; Q73 now reads
   "Speak up: tell a teacher." Observation only (not changed, core-inherited, same class as
   proof1 O7): rewrite keys Q18/Q63 drop a trailing adverbial ("Families will travel home.",
   "India beat Australia by 295 runs.") — grammatical standalone answers.

## 6. Self-check (2026-11-11)
- Full read of `2026-w47-en-ko.text.md` (all ~1,306 lines): zero issues.
  Notes kept: "YOUTH · 청년" and "DEEP READ · 시사 심층" are the shipped W46 ko heads
  (content56.py:12/93, TM values — kept as-is); "한 장의 지도｜쉰 개 주, 쉰 가지 규칙 — …" is a
  W46 ko TM value (kept, "쉰" is colloquial fifty); the ko edition mixes 해요체 and plain forms
  exactly as W46 ko does (TM values + my fresh translations follow the same mix); Q11
  "11월 = November" terse as in core; Q34 "(open = 개봉하다(3인칭 단수는 s 추가))" correct;
  Q54 "eight (여덟 명 = eight)" follows the core's tautological note pattern; Q89
  "공식 결과는 각 주 인증에서 나와요" is the TM value (해요체); Q97 "take time = 시간이 걸리다"
  correct; Q110 "more than 구문" terse as in core; Q136 "whether = ~인지" vs Q105
  "whether = ~인지（모르는 일）" — two source literals, both correct; "다섯 문장 평｜who, where,
  무슨 일, 반전, 결말 — 다섯 문장이면 돼요." is the W46 ko TM value for the FIVE SENTENCES
  bridge (kept); "경기 영어｜점수, 누가 득점했는지, 누가 앞서는지 — 짧은 문장이 생중계 영어예요."
  is a W46 ko TM value (kept).
- All 8 cards visually checked after the final render — clean. P1: bridge 2 lines clear of
  IN BRIEF, numbers box English+gloss, "TRY IT NOW · 바로 연습", footer "제 1 면／총 8 면".
  P2: calendar short form, "THE SENATE, IN NUMBERS · 상원", SAY IT "날짜를 말하는 법",
  gloss single "해설 — to certify = …", B bridge 1 line ("will + 동사로 바꿔 쓰세요(약속)。").
  P3: "COMING SOON · 곧 개봉", "HAYMITCH'S GAMES · 헤이미치의 경기",
  gloss single "해설 — a tribute = …", Rousseau tiger. P4: "SATURDAY, NOV 21 · 토요일" (core fix1 title),
  gloss single "해설 — a Test = …", W. G. Grace photo; P4 lead is the Ashes 2025–26 retrospective "Perth, One Year On: How Australia Kept the Ashes". P5: "ODD SOCKS, IN NUMBERS · 숫자로",
  gloss single "해설 — bullying = …", "SPEAK UP · 목소리를 높이자", Lawrence children photo.
  P6: "HOW LONG? · 임기의 길이", gloss single "해설 — to call a race = …",
  "A PRACTICE BALLOT · 연습용 투표", voting booth photo. P7: all gloss boxes single "해설 —",
  "THE TOOLBOX · 도구 상자", "READERS' CORNER · 독자의 편지", "AN EXAMPLE LETTER · 보기",
  "ERROR CLINIC · 오류", "NEXT WEEK · VOL.5 예고", Johnson portrait. P8: cloze + [A2] option
  tags, "B MULTIPLE CHOICE · 객관식", "C READING · 읽기 이해", "D SENTENCES · 문장 완성과 바꾸기",
  "E TRANSLATION · 번역" with "번역：", "F WORDS · 단어 짝짓기", "G DIALOGUE · 대화 완성" +
  "Levels: 145–149 [A2]", "H WRITING · 쓰기 [B1]" + Korean instruction, MODEL + Reading Room
  photo, ANSWERS block all 150 keys ending well above the footer with "150. 열린 문제 — 기준은
  쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에 (기준 항목대로 채점해요)"; footer "제 8 면／총 8 면".

## 7. Furniture
- foot_left "The Lucerna　영어 주간지 VOL.4　텍스트는 영어　해설은 한국어";
  foot_right "제 {n} 면／총 {total} 면"; gloss_prefix "해설 — "; p8_sep "— 제 {pg} 면 —";
  translate prefix "번역："; badge "영어 텍스트　한국어 해설 — 한국어 독자를 위한 판";
  topstrip "WEEKLY IN ENGLISH　매주 한 번　영어권에서 지금 화제가 되는 일 읽기";
  edition line "영어 주간지　VOL.4　선거　정글　영화"; edition spacing 11.5;
  p1_bridge_size None (default 20.5, W46 ko convention); p8_mode "notes".

## 8. Provenance
- TM: W46 `2026-w46-en-ko` positional alignment (260 pairs). Poisoned values caught:
  'note' → 'P8 saved, TOTAL exercises:' (harmless, rejected by build_map's POISON regex);
  '图表读数' → 'sans' (overridden by fresh type "그래프 읽기").
  'THE ERROR CLINIC　易错诊所' → 'THE ERROR CLINIC　오류 클리닉' is a legitimate W46 head, not poison.
- Map: `scratch-fanout-en2/fanout/map-ko.json` (lit 248, instr 5, type 17, ekey 4).
  Misses: 205 total, 182 with real CJK = 171 lit + 7 types + 4 ekeys.
  build_map normalizes U+2019 → ASCII apostrophe in all map values (fr lesson).
- F-MAIL: no real letters arrived; P7 prints the labelled editor's example + the VOL.3
  disclosure promising real letters from VOL.5. No invented letters, no email checked.

## 9. Build record
- `scratch-fanout-en2/fanout/ko/` — build-gates.log, make_textmd_w47.py, occlusion.log/json,
  p8-extract/compare.json, freeze.log/diff.json, webpdf.log, textmd.log, registry.json, dump_reg.log,
  freeze-final/.

## 10. Tool note (NOT fixed — p8.py is off-limits to the builder)
- `tools/p8.py` FOOTER_RE does not match the mixed-case footer "The Lucerna …" + "제 8 면／총 8 면":
  the merged footer line leaks into the last answer segment (key 150) for every edition.
  Masked when key 150 is dash-style (ko, ja, ru, nl, pt, it, fr, de), bites when paren-style
  without a dash (es, before its fix). A case-insensitive match on the masthead, or dropping the
  merged footer line by its y=2624 baseline, would close it.
- Occlusion audit gap (found in the nl round): the audit does not flag a box title running into live
  text in the neighbouring column. A title-vs-neighbour text proximity check would close it.
- Flow gap (found in this round): `match_set`'s keep-together `_fit` clamps a block to the page
  bottom when it doesn't fit in the last column, leaving a dead gap and an overflow that hides
  the real cause. The run-gate's flow-end check catches it, but the diagnostic ("need 362") only
  appears in the build log.
