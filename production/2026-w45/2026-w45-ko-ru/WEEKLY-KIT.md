# WEEKLY-KIT — W45 KO×RU (Korean target × Russian native)

Edition: **Lucerna VOL.2, week 2026-11-02 – 2026-11-08** (magazine model: cycle started Mon 2026-10-26,
issue dated the following Monday). Target language Korean, reader native language Russian.
Delivery dir: `files/weekly-report-w45-ko-ru/` (svg ×8, cards ×8, print PDF, web PDF, this KIT, ABSTRACT.txt).
Build tree: `hidden_files/weekly-report-w45-ko-ru-build/` (transform.py, fix1.py, fix2.py, fix3.py,
orphan_scan.py, geom_extra.py, gloss_render.py, baselines, diff.json, occlusion.json, orphan-out.txt,
geom-extra-out.txt, gloss-render-out.txt). Core reference (read-only): `files/weekly-report-w45-ko-core/`
+ `hidden_files/weekly-report-w45-ko-build/`. W43 same-pairing furniture reference (read-only):
`files/weekly-report-ko-ru/`. Nothing under `tools/` was modified by this build.

## Toolchain (coordinator ruling: record run.py and render.py separately)

- run.py AND render.py both ran under the tools venv: `tools/venv/bin/python` — **python 3.12.3, PIL 13.0.0**.
  System python3 (3.12.3, PIL 10.2.0) was NOT used for render.py (it has no cairosvg) and was not used for run.py.
- Single-process re-render per README #7 (content modules share bslib4 REG; never run standalone).
- README #11 respected: no content module was ever imported inside the core build dir (all comparisons via
  copies / tools/freeze.py). Core files were never written by this build.
- Tools versions: `tools/p8.py` sha256 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`
  (the current new version; another process replaced p8.py mid-build on 2026-10-28 — this build did not write
  to tools/). `tools/occlusion_audit.py` selftest OK (all 6 planted classes fired, clean controls silent).

## Core measured values (verified in this build's output, not copied)

VOL.2, masthead Lucerna with NO article, 1950×2700, 4 columns. 150 exercises: by page 10/18/18/18/18/18/12/38;
by level A2 51 / B1 72 / B2 27; by type 完成句 48 / 单选 52 / 配对 16 / 完形 13 / 造句 8 / 变换 4 / 判断 4 /
翻译 4 / 写作 1 (this edition under Russian type names — see mapping below). P8 38 items
(A8/B8/C4/D4/E4/F4/G5/H1), printed notes 150/150, dash style `N. key — note`. Model essay 157 chars
(whitespace-stripped), starting `나의 겨울 준비는 김장부터 시작해요.` — frozen verbatim. P7: A2/B1/B2 4 exercises
each + clinic 4 + frame `〜부터 〜까지` + readers' corner + VOL.3 preview. Golden phrases 8, whole-issue
frequencies 5/2/4/2/2/2/2/2. Images per page 1/1/2/1/1/0/0/0 (P1 autumn, P2 ssam, P3 Bukhansan + apples,
P4 baseball Bain PD, P5 study photo). Theme: Ipdong week — last foliage weekend, kimjang/winter-prep season
opening, CSAT countdown D-17→D-12, CSAT-day measures dated Nov 19 ONLY.

## Method

Core build tree copied; transform.py-style literal mapping replaces ONLY the Chinese explanation layer with
Russian; Korean target text byte-frozen; only the explanation layer changes. transform.py is the single source
of truth: longest-first exact-literal replacements, each asserted present ≥1 and absent afterwards, atomic
write at end; NO AST byte-offset splicing (README #17), NO repr literals into f-strings (README #18).
Every fix-round change was also appended to transform.py (nl-en lesson: unsynced fixes = recurrence caveat).
CORRECTION (2026-10-28, B-1 sync): that sentence was FALSE for fix2/fix3 — see "Fix sync B-1"
below. fix1 was appended; fix2/fix3 were appended only by the 2026-10-28 sync, after independent
proof showed their short forms absent from transform.py.

Furniture: W43 ko-ru SVG measurements take priority over tools/README #20 generalities. Verified from shipped
W43 ko-ru P1 SVG: serif line y=330 `КОРЕЙСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.1 · …`; subtitle y=366; badge y=394, 20pt bold
BRICK `#a4553a`, `ТЕКСТЫ НА КОРЕЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`;
double rules y=412/421; dark band rect y=433, band texts y=487/531. Applied to W45: serif line
`КОРЕЙСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · 입동 · 단풍 · 김장`; subtitle 372→366 (Korean subtitle text unchanged);
badge inserted y=394 with the same W43 string; rules 392/401→412/421; band rect 424→433, band texts
478/522→487/531; headline at hy=580 unchanged.
Footer (bslib4 foot()): `Lucerna · КОРЕЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА КОРЕЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ`;
page line `Страница {n} из {total}`. Gloss prefix `Пояснение — ` (replaces `译注｜`). Top strip:
`매주 한국어로 · Каждую неделю · 한국 사람이 읽는 한국어를 읽어요`. Band right P1: `ИПДОН` /
`Ипдон в субботу, 7 ноября · Начало кимчжана`.
Type/instruction mapping (W43 RU precedent): 完成句子→Дополните предложение; 单选→Выбор ответа;
词汇配对→Пары слов; 句型转换→Преобразование предложения; 造句→Составьте предложение; 判断→Верно или неверно;
完形单选→Заполните пропуски; 填空→Вставьте; 改写→Перепишите; 翻译→Переведите; 写作→Письмо.
Match instructions: 把词和说明配对/把词和释义配对→Соедините пары слов; 把山和说明配对→Соедините пары.
content8.py writing check updated `== "写作"` → `== "Письмо"`.
P8 E items: #137/#138 keys re-aimed to Russian (W43 precedent); #139/#140 stems re-aimed to Russian, Korean keys
frozen; #150 key `(открытый вопрос — образец ниже)`, note `Образец — в разделе H этой страницы ({NCHARS} знаков)`
(157 → genitive plural `знаков` is correct).
P7 target-language definition sentences frozen verbatim; only gloss lines localized. P7 frame/letter Korean text frozen.
P8 band-right string `제8면 · 이번 주의 큰 시험 + 모든 답` is Korean-only in CORE too and identical in W43 ko-ru:
it is the family's frozen Korean band-right descriptor for P8, NOT an untranslated explanation string (the P8 band
TITLE was localized: `시험과 답 · Тест и ответы`). Not a defect.

## Fix log

- **transform.py**: full mapping. Transcription pitfalls found and fixed during this step: several glossline()
  source strings end with ASCII `.` not `。` (e.g. `문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.` and all
  `…고르세요.` / `…넣으세요.` / `…답하세요.` / `…만드세요.` glosslines) — corrected before the successful run.
- **fix1.py** (also appended to transform.py): P8 B variants `内藏山公团预报峰值11月11日`, `月出山林业厅预报峰值11月9日`,
  `首尔报名窗口10点至12点`, plus repair of a substring artifact — first-pass `措施只适用于11月19日` had matched
  INSIDE `特别措施只适用于11月19日` (P6 judgment note), leaving mixed `特别Меры…`; fix1 replaced it with
  `Особые меры действуют только 19 ноября`. After fix1, all 6 operative files scan CLEAN of Hanzi
  (`[\u4e00-\u9fff]` = 0).
- **fix2.py** (NOT appended to transform.py at the time — corrected by the B-1 sync below): (1) P5 glosses made terse to save 3 lines (~89px):
  `정리 = повторение · 끈끈하다 = липкий · 합격 = сдача.`;
  `중점 = главный · 배치하다 = разместить · 통제하다 = перекрывать.`;
  `챙기다 = приготовить · 졸리다 = сонливость · 평소 = обычно.`;
  `비다 = молиться · 피하다 = избегать · 미끄럽다 = скользкий.`
  (one typo caught before running: `졸리да` with Cyrillic д corrected to Korean `졸리다`).
  (2) Five P8 note shortenings, each verified 2→1 wrapped lines at 13.3pt/434px:
  `Пик по лесной службе, Нэчжансан — 4 ноября`; `Пик по парковой корпорации, Нэчжансан — 11 ноября`;
  `Прогноз парковой корпорации, Нэчжансан — 11-е`; `С 13 часов 6 ноября — запись на оставшиеся места`;
  `Пик по лесной службе, Вольчхульсан — 9 ноября`.
  (One fix2 run initially failed because content12.py was missing from its FILES list — #24's note lives in
  content12; fix2 is atomic so nothing was applied until the corrected rerun.)
  (3) P7 letter disclosure shortened 6→4 wrapped lines + phrases pitch 132→102 (all phrase rows measure exactly
  76.0px, leaving 26px air, same as ko-fr).
- **fix3.py** (NOT appended to transform.py at the time — corrected by the B-1 sync below): (1) P1 gloss → exactly 3 wrapped lines:
  `입동 = ипдон · 절정 = пик · 김장 = кимчжан · 상륙하다 = выйти на берег · 온대저기압 = циклон.`
  Documented gloss compromise: `циклон` underspecifies `внетропический` (extratropical); the full term is carried
  by the P1/P4 articles, and the 4-line full-term variant still misses the fit by ~0.4px.
  (2) Six more P8 note shortenings, each verified 2→1 lines: `Во время аудирования самолёты не летают` (#67/#81);
  `Безопасность в Сеуле на Хэллоуин — 3 271 человек` (#68/#119); `С пожеланием сдачи дарят тток и ёт` (#72);
  `В день экзамена учреждения работают с 10 часов` (#77); `Самолёты ограничены во время аудирования` (#99);
  `На следующей неделе — экзамен по истории Кореи` (#131). Deliberately NOT changed: past-tense group notes
  (#58/#59/#60) and #144 note.
- **Letter-box slack**: core formula undercounts ~26–29px (core P7 last line escapes its box — measured below).
  Applied ko-fr precedent +40 slack: letter-box formula trailing `+26` → `+66` in content7.py `lh` formula.

## Fix sync B-1 (2026-10-28, transform.py + this KIT only — paper unchanged)

CORRECTION to the Method claim above and to the fix2/fix3 headers below: the claim
that every fix-round change had been appended to transform.py was FALSE for fix2/fix3.
Independent proof (hidden_files/w45/ko-ru-proof/REPORT.md §11/B-1) ran the shipped
transform.py alone on a fresh core copy (257 replacements passed) and found 19 fix2/fix3
short forms absent from transform.py (count 0 each), the delivered build files still in
their long forms, and a re-render in the overflow state (P1-headline overflow, P5-feature
overflow, P8-keys 2569 > 2540, P7 teaser 2695.46, p1/p5/p7/p8 SVGs differing). fix1 WAS
appended (REPL.update in transform.py); fix2/fix3 were not, until this sync.

This sync appends all 19 fix2/fix3 mappings verbatim to transform.py as a separate
second phase (FIX2FIX3), AFTER the main REPL phase: their sources are the RU long forms
that the main phase itself produces, so merging them into REPL would sort some of them
before their producer and assert-fail. Main REPL entries: 257, unchanged. FIX2FIX3: 19.
Idempotency (ko-it precedent): an entry whose source is absent but whose destination —
or, for a chained entry, its final form after later entries in the same pass (e.g. a f.ex
line whose dst still carries type "翻译", later rewritten to "Переведите") — or, for a
superseded main-phase entry, its fix short form — is already present is SKIPPED, not
failed. An entry with neither source nor destination/final/superseding form still FAILS
(verified by two negative controls: a corrupted P1 short gloss and a corrupted chained
E-item final form each make transform.py exit non-zero). No paper file, no build content
file, and nothing under tools/ was changed by this sync; the delivered SVGs/cards/PDFs
were NOT re-rendered.

### Synced entries (long → short, verbatim from fix2.py / fix3.py)

fix2 (12):
- fix2-1: `정리 = приводить в порядок, повторять · 끈끈하다 = липкий · 합격 = успешная сдача.` → `정리 = повторение · 끈끈하다 = липкий · 합격 = сдача.`
- fix2-2: `중점 = приоритетный · 배치하다 = размещать · 통제하다 = перекрывать, контролировать.` → `중점 = главный · 배치하다 = разместить · 통제하다 = перекрывать.`
- fix2-3: `챙기다 = приготовить заранее · 졸리다 = хотеть спать · 평소 = обычно.` → `챙기다 = приготовить · 졸리다 = сонливость · 평소 = обычно.`
- fix2-4: `비다 = молиться, желать · 피하다 = избегать · 미끄럽다 = скользкий.` → `비다 = молиться · 피하다 = избегать · 미끄럽다 = скользкий.`
- fix2-5: `Пик по прогнозу лесной службы по Нэчжансану — 4 ноября` → `Пик по лесной службе, Нэчжансан — 4 ноября`
- fix2-6: `Пик по прогнозу парковой корпорации по Нэчжансану — 11 ноября` → `Пик по парковой корпорации, Нэчжансан — 11 ноября`
- fix2-7: `Прогноз парковой корпорации по Нэчжансану — 11-е число` → `Прогноз парковой корпорации, Нэчжансан — 11-е`
- fix2-8: `С 13 часов 6 ноября — запись по всей стране на оставшиеся места` → `С 13 часов 6 ноября — запись на оставшиеся места`
- fix2-9: `Пик по прогнозу лесной службы по Вольчхульсану — 9 ноября` → `Пик по лесной службе, Вольчхульсан — 9 ноября`
- fix2-10: `К моменту сдачи в печать настоящих писем читателей и лучшего сочинения со стр. 8 не поступило: пример остаётся, а обещание переносится в VOL.3. Присылайте нам свои письма и свои тексты со стр. 8!` → `Настоящих писем и лучшего сочинения со стр. 8 к сдаче номера не поступило: пример остаётся, обещание — в VOL.3. Присылайте письма и тексты со стр. 8!`
- fix2-11: `cyq = fy + 66 + (i % 4) * 132` → `cyq = fy + 66 + (i % 4) * 102`
- fix2-12: `py = fy + 66 + 4 * 132 + 18` → `py = fy + 66 + 4 * 102 + 18`

fix3 (7):
- fix3-1: `입동 = ипдон, начало зимы · 절정 = пик, апогей · 김장 = заготовка кимчи на зиму · 상륙하다 = выйти на берег · 온대저기압 = внетропический циклон.` → `입동 = ипдон · 절정 = пик · 김장 = кимчжан · 상륙하다 = выйти на берег · 온대저기압 = циклон.`
- fix3-2: `Во время аудирования самолёты не взлетают и не садятся` → `Во время аудирования самолёты не летают`
- fix3-3: `Сотрудников безопасности в Сеуле на Хэллоуин — 3 271 человек` → `Безопасность в Сеуле на Хэллоуин — 3 271 человек`
- fix3-4: `С пожеланием успешной сдачи дарят тток из клейкого риса и ёт` → `С пожеланием сдачи дарят тток и ёт`
- fix3-5: `В день экзамена учреждения начинают работу в 10 часов` → `В день экзамена учреждения работают с 10 часов`
- fix3-6: `Во время аудирования в день экзамена самолёты ограничены` → `Самолёты ограничены во время аудирования`
- fix3-7: `На следующей неделе готовится к экзамену по истории Кореи` → `На следующей неделе — экзамен по истории Кореи`

### Repro validation (scratch only, tools venv python, OUT repointed to scratch)

- Fresh core copy + new transform.py alone: 276 ok (257 REPL + 19 FIX2FIX3), 0 skip, 0 fail.
- 6 content files: OUT-normalized identical to the delivered build files, and byte-identical
  after restoring the delivered OUT line (bslib4 has no OUT line; strict identical).
- 8 SVGs: byte-identical to the delivered SVGs (p1 d188d1c7…, p2 c8ce33ac…, p3 de57bfbe…,
  p4 8ce74068…, p5 ebbea645…, p6 56eff22f…, p7 e57f374e…, p8 8fa66246…; full hashes in
  the fix scratch deliverables-snapshot files).
- Run log: ZERO FLOW OVERFLOW; P1-headline ends 1413, P5-feature ends 1268, P7 teaser ends
  2517.46 (< 2540), P8-keys ends 2456 (< 2540); TOTAL 150 — exactly the shipped round-3 values.
- Re-run on a delivered-build copy: 276 skip (258 already-applied + 18 superseded-by-fix),
  0 ok, files byte-unchanged — transform.py is now idempotent on the shipped tree.
- transform.py sha256 before this sync: 2895b6616ed4691864d06041edd9d185dd05767d030b6d519d7ef8aaf75475cd;
  after: cc72648708f7192a0aab53dc1a013e3f8afcaff5dcc003c060575e8e033b84b8 (final, with the
  chained-final-form skip logic; the intermediate sync hash was
  973d62f7268a7e1b890d48f39220d28ee716c67157667f14d3643f584cdaef76, superseded in the same
  session by the idempotency hardening — fresh repro was re-run against the final hash).
- Deliverable hash proof: svg×8 + cards×8 + both PDFs re-hashed after this KIT edit and found
  identical to the pre-fix snapshot (print PDF 30,916,571 B, sha256
  b4756358b2b821495d18ec66b6db56c3cedba7c964957df252941a52a5907070; web PDF 3,622,912 B,
  sha256 76e8b5032d0378b53f228e4d6a69d81f48d63987b63ab004bf9282dad81ffb01). KIT/ABSTRACT are
  not render inputs, so a KIT-only edit cannot change the PDFs; the re-hash confirms it.
- This sync does NOT finalize the edition: independent re-verification (repro re-check) and
  coordinator sign-off are still required before any listing.

## Build rounds (2026-10-28, all in this build tree)

- **Round 1** (tools venv run.py, single process): TOTAL 150, levels/pages/types exactly matching core (types under
  Russian names). Problems: P5-feature FLOW OVERFLOW, P8-keys FLOW OVERFLOW, P7 teaser end 2695.46 > 2540, plus a
  P1-headline overflow hidden in the truncated log tail. Baseline: `round1-svg-sha256.txt`.
- **Round 2** (after fix2): P5-feature ends 1268 ✓, P7 col3 1863.46, teaser 2517.46 ✓; but P1-headline overflow
  surfaced and P8-keys still ended 2569. Baseline: `round2-svg-sha256.txt` (p1–p4, p6 unchanged from round 1;
  p5 `ebbea645…`, p7 `e57f374e…`, p8 `966f8ace…`).
  - P1 root cause (from SVG column dump): RU P1 gloss ran 5 lines vs core 3, pushing the numbers box out of
    column 1 and the last drill past bottom 1828. A 4-line gloss would still miss by ~0.4px, so the gloss MUST be 3 lines.
  - P8 diagnosis: core P8 keys are all 150 single-line items; RU round 1 had 23 two-line items (173 lines). After
    fix2, 166 item lines + 8 separators = 174 lines; columns fill sequentially so the last column's remainder sets
    the flow cursor (2569). Saving 2+ lines anywhere drops the final cursor.
- **Round 3** (after fix3): ZERO FLOW OVERFLOW / HEAD TOO WIDE. Flow ends: P1-headline col 2 y=1413 (exactly core's
  value); P1-weekend 2094; P1-quiz 2521; P2-feature 1447; P2-ex 2258; P3-feature 1349; P3-ex 2146; P4-feature 1081;
  P4-ex 2002; P5-feature 1268; P5-ex 2256; P6-feature 1149; P6-ex 2253; P7-a2 1092 / b1 1029 / b2 1089; P7 col3 1863.46;
  P7 teaser 2517.46 (< 2540 ✓); P8-ex 463; P8-keys 2456 (< 2540 ✓, 84px margin on the flow cursor).
  Rendered (tools venv render.py, 2026-10-28 ~04:34): 8 cards + print PDF 30,916,571 bytes + web PDF 3,622,912 bytes
  (< 10 MB). Baselines: `round3-svg-sha256.txt` and `round3-full-sha256.txt` (svg+cards+both PDFs). No render change
  after round 3; ABSTRACT.txt and this KIT are not render inputs (PDF rehash after KIT/ABSTRACT confirms identical hashes).

## Gate 1 — Freeze (tools/freeze.py diff, core vs edition; full diff in diff.json)

p1–p7 added CJK = 0 on every page; p8 added CJK = 2 chars (`절` +1: core 11→RU 12; `기` +1: core 19→20).
Attribution (provable headword citation, same class as the brief's ko-fr/ko-es #104 example): P8 item #104 note
`절기 = 24 сезона года` — `절기` is the P7 exercise's own Korean headword; core's P8 note for #104 was
Chinese-only, so 절+기 are net-new on P8 only as this citation. All other P8 Korean citations (e.g. #34/#142 `절정`)
were already present in core P8 counts. Edition SVGs contain ZERO Hanzi on all 8 pages (direct scan).

## Gate 2 — P8 (tools/p8.py, current new version, explicit dual-path compare, --total 150)

`core 150 noted, edition 150 noted, status: CLEAN, missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`.
Adjudicated from printed lines: #137 core `11月7日是立冬。 — 对照第 1 版` → RU `7 ноября — это ипдон. — См. стр. 1`
(genuine E re-aim); #138 core `离高考还剩 12 天。 — 对照第 5 版` → RU `До экзамена осталось 12 дней. — См. стр. 5`
(genuine E re-aim); #139/#140 keys frozen Korean (`특별 조치는 11월 19일에만 적용돼요.`,
`저는 토요일에 내장산에 단풍을 보러 가요.`), notes localized; #150
`✓ Образец — в разделе H этой страницы (157 знаков)`. No #109 keydiff under the new tool (old-tool dash artifact
gone); no #137/#138-type Russian-dash paren-branch false positives outstanding. P8 notes are pure Russian
(no cross-family residue; the one mixed-language artifact found during transform was repaired by fix1).

## Gate 3 — Gloss (README #21: split on `·` itself, never on ` · `; method stated explicitly)

- Rendered-page method (gloss_render.py: prefix-anchored gloss() boxes in the rendered SVG, continuation lines joined,
  split on `·`): core boxes p1 [5], p2 [4,3,3,3,3], p3 [4,3,3,3], p4 [4,2,1], p5 [3,3,3,3], p6 [3,2,3], p7 [], p8 []
  = **61**; RU identical per page per box = **61**. ALL-BOXES-EQUAL.
- Call-string method: gloss() only core 61 = RU 61 (content12 21, content34 20, content56 20, content7 0, content8 0);
  gloss()+glossline() core 84 = RU 84 (content12 24, content34 26, content56 28, content7 6, content8 0).
- No other edition's KIT was "corrected" over counting-method differences (README #21: pending parent decision;
  the gate is equality with core, which holds on both counts).

## Gate 4 — Golden phrases

All 8 phrases verbatim + page tags + whole-issue frequencies equal core: **5/2/4/2/2/2/2/2**.
Each phrase is present on its tagged page (P7 phrases section tags: 1,1,1,2,3,4,5,6) and is a contiguous excerpt of
this issue's articles. (Phrase 1 occurs 3× on p1 itself — band + article + P7-section accounting is whole-issue;
the gate is whole-issue equality, which holds exactly.)

## Gate 5 — Geometry

- Canonical `tools/occlusion_audit.py`: edition **0 flags**, core **0 flags**, NEW vs core **0**. Output in occlusion.json.
- Supplementary scans (geom_extra.py, reusing the audit tool's parsing/font resolution; full output in
  geom-extra-out.txt, untruncated): (A) same-baseline ink collisions: **0 on all 8 pages**; (B) border-cut scan
  (text ink crossing a later-drawn border-only rect while starting inside it, page-frame rects excluded): **0 on all
  8 pages**; (C) P6-only max later-rect/image coverage of baseline-anchored true ink: **0.0%** (< 30% gate);
  (D) right-edge advance scan (PIL getlength advance right past 1885.5 or left before 64.5, footer text ending exactly
  at 1885 allowed): **0 on all 8 pages**.
- Visual review: **all 8 cards read** (p1–p8): no overflow, overlap, footer, image, or credit issues. P1 masthead/badge/
  band/gloss/numbers/drills all fit; P3 match section and apple caption wrap correctly; P4 ladder diagram labels
  ungrazed; P5 numbers box title inside its box; P6 comparison table all cells visible; P7 letter box inside with air
  (see gate 7); P8 keys fit in 3 columns above the footer. The P8 band-right Korean string is family precedent
  (see Method), not a defect.

## Gate 6 — Orphan scan (window [10,45], ≥3-syllable tail standard, all prose columns; script orphan_scan.py, output orphan-out.txt)

Edition: S1=0, S3=0, S3b=0, S4=0, S5=0, G=5, S2=10. Core对照: S1=0, S3=0, S3b=0, S4=0, S5=0, S2=9, G=4.
S2 adjudications (all non-defects — complete standalone strings/items, not stranded fragments): P1 word-of-week line
`입동 = ипдон, сезон начала зимы.`; gloss continuations containing complete headword+translation items
(`отопление · 식탁 = обеденный стол.`, `= штраф · 불씨 = искра.`, `예의 = вежливость, правила поведения.`,
`되다 = становиться единым.` — the last is a word-boundary wrap of `하나가 되다`, not a mid-word split, and S3
correctly silent); `= масштаб · 섞다 = смешивать, путать.`; P7 glossline `나다 = пережить, провести.` (complete item);
clinic note `К месту назначения — «э», а не «를».` (complete sentence); P8 key
`109. 기준 — Даты различаются из-за разных критериев (стр. 3)` (complete key line). The `1,620명)` line (P5 box,
x=545, y=1398.55) is inherited verbatim from core at identical coordinates (core scan shows the same line) — frozen
Korean box item, complete numeric token, not a word fragment. RU has one extra G vs core (P6 gloss continuation
`· 확정 = подтверждённый · 믿다 =` at y=1059.175) — same gloss-continuation format class, longer Russian gloss, not a
defect. Lines starting with `=` in RU glosses are the W43 RU `word = gloss` format's wrap behavior (also shipped in
W43), not line-start orphan punctuation (S1 set is `.!?…)]»」`).

## Gate 7 — P8 flow-end triple measure + P7 boxes (limit 2540)

- P8: flow cursor **2456** (run log, last-column end); max baseline across all keys columns **2531.98**
  (col2 last line #113 `113. A — Ипдон — в субботу, 7 ноября`; col2's next item did not fit, so the flow moved to
  col3, whose last item #150 sits at baseline 2439.79); max ink bottom **2535.73** — all three < 2540 ✓
  (ink-bottom margin 4.27px; the flow-fit guarantees no drawn line exceeds the limit).
- P7 teaser: rect (65, 2399.5, 1885, 2517.5), bottom **2517.5** < 2540 ✓ (run-log teaser end 2517.46, 0.04 rounding).
- P7 readers'-corner (letter) box: rect (1450.3, 1256.3, 1885.7, 1864.2); last ink bottom **1852.55**
  (`Присылайте письма и тексты со стр. 8!`) → **inside by 11.61px** ✓; gap letter-box-bottom → phrases rule
  (rule at 1892.46) = **28.3px** ✓; last ink → rule = 39.9px. Core对照: core letter box (1229.7–1739.6), last ink
  bottom 1766.73 → **escapes by 27.09px** (confirms the core formula undercount); this edition does NOT inherit it.
- P7 phrases: pitch 102, all phrase rows measure exactly 76.0px, 26px air above the phrases rule.

## Gate 8 — Readers' corner (no invented names/letters/quotes; all elements on-page)

- Labeled editor's example: `Пример от редакции, а не настоящее письмо.` (plus Korean `— 독자 편지의 예`).
- Three factual disclosures (Russian lcn2, repeated in Korean lko): no real letters
  (`Настоящих писем … не поступило`), no best P8 composition (`лучшего сочинения со стр. 8 … не поступило`),
  both deferred to VOL.3 (`обещание — в VOL.3`).
- Explicit imperative solicitation covering BOTH letters and best P8 texts: `Присылайте письма и тексты со стр. 8!`
  (teaser/preview/other-page hints do NOT count — this line is inside the readers'-corner box itself).

## Gate 9 — Image payload = core (two hash measures; credits verbatim from Commons API Artist field)

Payload byte-identical to core on every page (base64-text sha256 and decoded-JPEG sha256 both match; full hashes below).
Counts 1/1/2/1/1/0/0/0 = core. Every credited image is placed; credit lines identical to core:
P1 autumn `lumoplank — CC0`; P2 ssam `wizdata — CC0` (captioned honestly as ssam, NOT kimjang — see fact debts);
P3 Bukhansan `Udonhan1992 — CC0` + apples `Paul Cézanne — Public domain`; P4 baseball `Bain News Service — Public domain`;
P5 study `Gary Todd — CC0`; P6/P7/P8 no photos.
- p1 img0: b64sha `535fff46b7cef2237589a156495a8ef9e805b4fa683289d55da6448aff4cec23`, jpegsha `6f7f33ed8f40f3c07c3f30a914a369c5986ea62d0fa33286d3d20d46e88f0388` (722,393 bytes)
- p2 img0: b64sha `e66d2b455ec68fd10e8f7a7fa28e9323d3b4ee52c57b92336b9f9177fcd3614b`, jpegsha `96a6a19b612a4b284956e9b99a4aa65c8ede7e18b7d040f8fb645165f14173bc` (532,598 bytes)
- p3 img0: b64sha `e266b6ee1a87086487c142a8eded5565bbe2b112c53632c8a638db6f9c573c2d`, jpegsha `158ea3a0e81f041d71bb9a29614b14d9a0cd84451c98fda3a2b0302cbb3e791b` (477,930 bytes)
- p3 img1: b64sha `5bea45d1f81e0716ea1d0d08693d3fb6df61a69442db5e6334c7c28787b8a7d2`, jpegsha `214cc390ac7cbcb05b0ce3edbcc01ccb365ad8114ad9bb8dcb68fc03981ebf56` (654,163 bytes)
- p4 img0: b64sha `1a7e7d6d5ffcede7632a1905a69b8e4893d965000e5e371cbf467920b2c946e3`, jpegsha `18ad8ae06fac2860d2c03323efd7ad5736de8597e1540058e830ccd35bad1009` (145,898 bytes)
- p5 img0: b64sha `6a1bab177d540192c4ac194e8f0d5ec160331304649991c3d80e9fd743c229f3`, jpegsha `35e7dc69d41784917d91feaf830d8c5703fb650e0005ad531fbe68332687e6e5` (460,131 bytes)

## Gate 10 — ABSTRACT.txt

Single line, Russian, no ASCII double quotes, with real topic keywords + learner search phrase + masthead + target
language + A2–B2 + 150 exercises. Text: `Lucerna — корейский еженедельник VOL.2 для русскоязычных читателей:
учим корейский по текстам об ипдоне 7 ноября, последних выходных красной листвы, начале сезона кимчжана,
обратном отсчёте до экзамена сунын и осеннем бейсболе; уровни A2–B2, 150 упражнений с ответами и разборами.`
(insert.py aborts without it; present.)

## Gate 11 — Web PDF vs cards (fr-en noise lesson)

8 pages; each embedded JPEG (1400×1938) compared against its card resized to the same size: mean|diff| 2.079 /
2.036 / 2.007 / 1.726 / 1.874 / 1.715 / 1.587 / 2.196, px>20 0.41–0.66% — uniform pure JPEG roundtrip noise, no outlier
page, no substituted or corrupted page. No noisy page.

## Gate 12 — Baselines

Every fix round recorded its pre-fix full baseline before rendering (round1-svg-sha256.txt, round2-svg-sha256.txt,
round3-svg-sha256.txt, round3-full-sha256.txt in the build tree); the build dir was never reset. Round 3 is the
shipped render; no render change after it (KIT-only text + ABSTRACT.txt added afterwards, PDFs rehashed identical).

## Delivered files + hashes (round 3, re-verified after KIT/ABSTRACT)

- Print PDF `Lucerna-VOL2-RU.pdf`: **30,916,571 bytes**, sha256 `b4756358b2b821495d18ec66b6db56c3cedba7c964957df252941a52a5907070`
- Web PDF `Lucerna-VOL2-RU-web.pdf`: **3,622,912 bytes**, sha256 `76e8b5032d0378b53f228e4d6a69d81f48d63987b63ab004bf9282dad81ffb01`
- SVG sha256 (round3-full): p1 `d188d1c7355c16396f10f2ae10b089b5d5daeba2d855c99d84b12db0d87b1f1f`,
  p2 `c8ce33ac4786d01bcf92996c8a548e2e1af12929240f56076c6056ba782cd12c`,
  p3 `de57bfbe13f62d13526fa49a3dbabe5e7e5a72859aff60f7639973357ab50abc`,
  p4 `8ce740683a7d8d31cccbe1aa0d3b2c0e2e0818b2bcfe4d8cedec87bf8f1aa09e`,
  p5 `ebbea6456c94d6edf17f4668b9d1af7669783078c8e82ef621094f6853ecb92a`,
  p6 `56eff22fbd271d9d5f61ba14a4ba6c26cd1f6146a00dc206b6053bf73f72ea30`,
  p7 `e57f374e7cd6ffa35468c88e185c686cf24e06a0bbdc34c1de00335627ca9d7f`,
  p8 `8fa662464615ddad783a8730864af5f7d39c1de0370775d0bd487cc0edf7750c`
- Cards sha256 (round3-full): p1 `5159622e4260a6e66e9006e1afc1c12f8d34b4e631792a138aac1c38e9806020`,
  p2 `772576f686587dcdd4a8950a4d7e6bf1409a1afde54a79ec7300b6386d2b5523`,
  p3 `76e7b661406dfd801982971512af98dd4746df1735c66188c612131192defb26`,
  p4 `13d6362e5357b8c20e672a5358c14dda4d4bf680fdd1f2d59af3a1e0ac2e4ede`,
  p5 `937f1711aa84f6324101b49d0853e4558b2087bf03abed33052855ac31c1c59f`,
  p6 `8be542ec7949182f5b23d363fbb7c01be264c4952d6bec380a182d5bb77ec5ed`,
  p7 `a9ff68f5724ba8cdc6dd68df51494195f54439bd0baad8731e776803b6e2c981`,
  p8 `5b62f98bd1b575fe1c66971d7043511d83e1fd76b2437bd20da8d8bcfd7d0abd`

## Inherited-only fact debts (carried, NOT re-litigated as this edition's blockers, no new claims added)

Korean Series Nov 2 start may shift after playoff rain delay (issue uses `발표된` wording + press-time note); playoff
G1 (Oct 26) result unknown at cutoff — no score printed; Champi "latest warning record" claim deleted as unconfirmed;
Ipdong Nov 7 / Soseol Nov 22 from calendar blogs (KASI official page not retrieved); Korean-history-exam details are
second-hand reports; Commons photo shortfall (no verified PD/CC0 Korean foliage/kimjang/Korean-student-studying photo;
ssam photo captioned honestly as ssam, NOT kimjang). No international politics; target-country domestic politics rule
and China exception are standing SOP rules, not triggered here.

## Delivery status

COMPLETE and ready for coordinator insert (insertion is serialized by the coordinator; this builder did not insert,
did not post to Discord, did not send cards/PDFs to main chat, did not touch weekly-git, tools/, other editions,
or shared scratch, and created no crons). No open defects. Known thin margins (not defects): P8 max ink bottom
2535.73 vs limit 2540 (4.27px; flow-fit guarantees compliance); P7 letter-box inside margin 11.61px.
