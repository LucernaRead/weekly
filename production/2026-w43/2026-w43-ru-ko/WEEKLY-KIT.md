# WEEKLY-KIT — RU×KO (Russian text · Korean explanations)

- **Edition**: Lucerna Weekly W43 (2026-10-19 – 2026-10-25), VOL.1 — Russian target text with the full explanation layer in Korean (해요체), for Korean-speaking readers.
- **Status**: PASS — independent proofread complete (2026-10-22): one explanation-layer defect found and fixed (P4 §D instruction orphan, see §9), full gate suite re-run clean on the final build. Not inserted into the repo, not posted anywhere.
- **Pairing badge (P1)**: 러시아어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판
- **Source core**: files/weekly-report-ru-vol1/ (finalized RU VOL.1 core, 150 exercises = A2 54 · B1 72 · B2 24). Russian target text is frozen byte-for-byte; only the Chinese explanation layer of the core was re-rendered in Korean.
- **Content line**: Russian domestic life only (첫눈 «Первый снег», 12-day school holidays Oct 24 – Nov 4, Moscow derby, Halloween, family days). The Korean layer adds no international politics or geopolitics.

## 1. Deliverables (measured on disk)

| File | Bytes | SHA-256 |
|---|---|---|
| Lucerna-VOL1-KO.pdf (print) | 24,343,479 | 59a3c344e5bf84a665a59ce72768fc052af534c6523d37c8f39ea47e9f55e69b |
| Lucerna-VOL1-KO-web.pdf (web, < 10 MB) | 3,532,952 | 4e6a1a340b6b654c8d464979fcebf778bd7ebb1ebed3118e51530592ff962e98 |
| svg/ × 8 | p1 1,018,497 · p2 320,502 · p3 1,157,971 · p4 302,454 · p5 489,193 · p6 983,933 · p7 28,668 · p8 61,634 | — |
| cards/ × 8 (1950×2700 PNG) | p1 1,347,148 · p2 1,016,811 · p3 1,364,928 · p4 839,111 · p5 960,661 · p6 905,252 · p7 685,115 · p8 1,012,143 | — |

Build dir: hidden_files/weekly-report-ru-ko-build/ (copy of the RU core build, OUT repointed to files/weekly-report-ru-ko/). One-process driver run.py (README #7); rendering via the copy's render.py.

## 2. Method

1. Copied hidden_files/weekly-report-ru-build/ → hidden_files/weekly-report-ru-ko-build/; repointed every OUT (expanduser form, all 5 content modules) and render.py BASE + PDF names (Lucerna-VOL1-KO.pdf / -web.pdf); printed OUT before the first run — zero references to the core files dir remain in the copy.
2. tools/freeze.py baseline on the untouched copy: **8/8 SVGs byte-identical** to the shipped core; core integrity re-hashed after every later run (final check: shipped core SVGs unchanged, hashes match the first baseline).
3. Explanation-layer transform: an exact-literal replacement table (468 quoted/raw replacements applied, every pattern consumed, asserted) + bridge() → expl() rename (1 def + 20 call sites). The transform script lives in the build's scratch/ subdir and necessarily quotes the core's original Chinese strings as search patterns (scratch-confined, disclosed here per toolkit rules). End-state assertion: **zero Han characters in all six operative modules**.
4. Registry comparison (core build registry vs edition registry, both dumped from one-process runs): structure (n/page/level) identical for all 150; type labels mapped per the KO column set (문장 완성 54 · 객관식 42 · 단어 짝짓기 20 · 문장 만들기 12 · 빈칸 객관식 13 · 문장 바꾸기 4 · 번역 4 · 쓰기 1); totals 150 = A2 54 · B1 72 · B2 24.

## 3. Furniture registry (KO column forms, target = 러시아어)

Applied verbatim from files/weekly-report-en-ko/WEEKLY-KIT.md §3 with the target name set to 러시아어; masthead is article-less "Lucerna".

- **Top band (P1)**: left `VOL. 1 · ПЕРВЫЙ ВЫПУСК` (frozen), centre `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 매주 발행 · 러시아가 읽는 러시아어` (Russian segment frozen; the core's Chinese segments replaced per the column formula), right `НЕДЕЛЯ С 19 ПО 25 ОКТЯБРЯ 2026 ГОДА` (frozen).
- **P1 serif line (y=330) / subtitle (y=372)**: both are Russian target text in this core (`РУССКАЯ ГАЗЕТА · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ` / `ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — …`) — kept frozen byte-for-byte (unlike the EN/DE cores, whose y=330 lines were explanation-layer text).
- **Pairing badge — INSERTED form**: because y=372 is frozen target text here, the badge is inserted at **y=574**, 22pt sans bold BRICK, centred — the FR×KO / ES×KO inserted-form precedent: `러시아어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`. It sits between the dark band (ends y=542) and the headline kicker (baseline 606); no occlusion or same-line flag.
- **Dark band right lines**: `이번 주 첫눈` / `예보가 엇갈려요 · 2면 참조` (해요체, gold).
- **Footer (all 8 pages)**: left `Lucerna · 러시아어 주간지 VOL.1 · 텍스트는 러시아어 · 해설은 한국어`; right `제 N 면 / 총 8 면`.
- **Gloss prefix**: `해설 — ` (bslib4 gloss()). P1 headline explanation line runs through expl() with no prefix, as in the family's other ×KO editions.
- **Bilingual heads**: target original · short Korean form — ГЛАВНАЯ ТЕМА · 헤드라인 / НЕДЕЛЯ В ЦИФРАХ · 이번 주 숫자 / СЕЙЧАС ВЫ · 지금 연습해요 / СМИ · 미디어 화제 / В ЭТОМ НОМЕРЕ · 이번 호 차례 / СЛОВО НЕДЕЛИ · 이번 주 단어 / КОРОТКО · 단신 / БЛИЦ-ВИКТОРИНА · 번개 퀴즈 / СЛОВА О ПОГОДЕ · 날씨 단어 / ЗА И ПРОТИВ · 찬반 / ОШИБКИ · 실수 클리닉 / СЛОВО · 이번 주 새 단어 / СЛЕДУЮЩАЯ НЕДЕЛЯ · 다음 호 예고 (VOL.2); band titles ЖИЗНЬ · 생활, КУЛЬТУРА · 문화, СПОРТ · 스포츠, МОЛОДЁЖЬ · 청소년, БОЛЬШОЙ РАЗБОР · 심층, ЯЗЫК · 언어, ТЕСТ И ОТВЕТЫ · 연습과 답; band subs carry a short Korean segment after the frozen Russian one.
- **Exercise header right note (P2–P6)**: `답은 8면에 · 문제는 급이 섞여 있어요, 번호로 찾으세요`; P1 quiz right note: `1면을 읽고 정답을 고르세요 · 답은 8면에`.
- **Instr labels**: 빈칸 채우기 / 문장 만들기 / 번역 / 쓰기 / 바꿔 쓰기 / 단어와 뜻 짝짓기 (family set).
- **P8**: header `ОТВЕТЫ · 정답 — 면별로 나누어 실었어요, 번호로 찾으세요`; right note `문제마다 한국어 해설 한 줄 · ✓ 표시는 모범 답안 문제예요`; separators `— 제 N 면 —`; answer typography is the RU family's dash style (`N. key — note`, writing items `N. ✓ note`) at the core's own sizes (13.3/13.0, lh 1.13), verified from the core build code (README #8/#14).

## 4. Freeze evidence

- freeze.py diff (core svg/ vs edition svg/): **Han characters added = 0**. Added CJK = 2,565 chars, all Hangul (explanation layer; 2,570 in the builder's build, −5 after the §9 proofread fix shortened one instruction).
- **Removed strings without Han**: only the eight P8 separators `— СТРАНИЦА N —` (furniture, replaced by `— 제 N 면 —`). Every other removed string is a Chinese explanation string.
- **Cyrillic word multiset**: removed net = {СТРАНИЦА ×8} only. Added net = citations inside Korean notes/keys where the core note was pure Chinese — team names (ЦСКА ×2, Спартак ×5, Зенит ×3, Динамо ×3, Родина ×2, Оренбург ×2), the four film titles («Морозко», «Сказка о потерянном времени», «Чудо-Юдо», «Королевство кривых зеркал»), and «19 октября» inside the Pushkin phrase gloss. Every added Cyrillic word already appears in the core's own Russian text; **no new Russian target text**.
- P7 phrases: all 8 Russian quotes byte-identical to the core (absent from the diff), page tags `(Страница N)` kept in Russian; occurrence counts equal (freeze multiset diff). Only the Chinese translations became Korean.
- **Gloss item counts (per call site, AST-counted against the core)**: all 28 gloss/expl call sites preserve their item counts exactly (3·3·3·3 on P1/P2 glosses, P3 3+3, P4 4, P5 3+2, P6 3, P7 bridges 4+2+3 segments; every instruction bridge 1→1). Match-set notes: 20/20 translated, none dropped.

## 5. P8 printed-note gate

- p8.py extract on the shipped core P8: printed set = **150/150** (RU core prints every note, dash style). The edition is built from the same code path (no note filtering), so it prints the same set by construction.
- p8.py compare (core P8 vs edition P8, total 150): **CLEAN** — missing=[], extra=0, uncertain=[]; printed keydiffs reported by the tool: [54, 137, 138].
- **Key-diff table (registry-authoritative)**:

| # | Kind | Core key | Edition key |
|---|---|---|---|
| 137 | translation item re-aimed at reader language | 星期日中央陆军将对阵斯巴达克。 | 일요일에 ЦСКА가 «Спартак»과 경기해요. |
| 138 | translation item re-aimed at reader language | 预报员预报十月末有雨夹雪。 | 예보원이 10월 말 진눈깨비를 예보해요. |
| 150 | writing device item | （开放题，范文如下） | (열린 문제 — 모범 답안은 아래에 있어요) |

- **Stem changes (bodies, keys stay Russian)**: #139 prompt body 星期六开始放假，一共十二天。→ `토요일부터 방학이 시작되고 모두 12일이에요. → ___`; #140 prompt body 我祝爸爸父亲节快乐！→ `아빠께 아버지의 날 축하 인사를 드려요! → ___`.
- **#54 is a tool extraction artifact (README #13), not a key change**: the printed line is identical in structure — core `54. третий — 第三名：третий（阳性主格）`, edition `54. третий — 3위: третий (남성 주격)`; the registry key is `третий` in both. The extractor trips on the half-width parentheses in the Korean note; the registry diff is authoritative.
- #150 is not surfaced by p8.py's ✓-branch comparison; the registry diff records both its key (device form above) and its note: core `范文见本版 H 区（82 词）` → edition `모범 답안은 이 면 H 구역에 있어요 (82단어)` — model length preserved (NWORDS = 82 in both builds).
- **Language-neutral notes (byte-identical, 8)**: #17 выпасть → выпадет · #35 учиться → учился · #36 написать → написал · #63 закончиться → закончился · #73 День бабушек и дедушек · #90 слушать → слушают · #104 выпасть → выпадет · #110 обещать → обещают. The other 142 notes are translated into Korean.

## 6. Mechanical gates (final build)

- **occlusion_audit.py** (selftest OK): edition 2 flags, core 2 flags, **NEW vs core = 0**. Both flags sit on frozen Russian text and reproduce identically on the core: BOXTITLE p1 'странице.' (КОРОТКО box, ink 2305.6 vs border 2304.0) and LINEX p2 'Запомните пару…' (section rule crossing) — inherited core items, not explanation-layer defects.
- **Same-line ink-collision scan** (PIL ink boxes, occlusion_audit measurement): edition **0** / core 0.
- **P6 chart, element level** (README #12): bars measured 600/494/388/282 px = 34/28/22/16 × 600/34 exactly; the four % labels sit 14 px right of their bar ends with zero ink overlap; the practice-data disclaimer keeps the core's Russian sentence plus its Korean equivalent.
- **Korean orphan scan** (full edition, tightened rule: last wrapped line ≤ 3 glyphs or a single syllable flagged): after fixes, **0 true orphans**. Two remaining candidates adjudicated non-defects: P8 #46 tail `Пушкина` (a Russian citation word wrapping inside a mixed note — the core wraps the same citation) and P8 #133 tail `시간` (a complete two-syllable word).
- **Residual scans**: Han characters in the 8 edition SVGs = 0 per page; footer pairing line present on all 8 pages; gloss prefix `해설 — ` counts per page = core `译注｜` counts (P1 shows 1 vs core 0 — that hit is the pairing badge itself, which contains `해설 — `; P1 has no gloss() box in either build); banned/other-column terms in pages and operative code: `bridge` 0, `paper` 0, Seite/Página/Pagina/페이지/译注 0.
- **Calendar (Europe/Moscow, verified against the real 2026 calendar)**: Oct 19 Mon · Oct 21 Wed · Oct 22 Thu · Oct 23 Fri · Oct 24 Sat · Oct 25 Sun · Oct 28 Wed · Oct 31 Sat · Nov 4 Wed — all core weekday claims hold; holidays Oct 24 – Nov 4 = 12 days; ministry window Oct 26 – Nov 3 = 9 days.
- **Flow discipline**: one-process runs print no OVERFLOW / HEAD TOO WIDE warnings. Height-critical boxes match the core exactly (P2 col3 ends 1467.75 = core; P7 col3 ends 1682.96 = core — the Korean lines inside the wrap()-measured А ВЫ / clinic / word / letters boxes were pre-measured to the core's line counts). P8 answers flow ends y=2261 vs core 2231 (bottom 2540).

## 7. Builder self-proof — defects found and fixed

Full visual pass over all 8 cards (Korean glyphs render throughout, no missing-glyph boxes; fonts per tables.json / the shared svglib). Seven explanation-layer wrap defects were found and fixed, each fix in the Korean wording only, each followed by a one-process re-render and a full gate re-run:

1. P1 numbers box, fact 3: Korean parenthetical pushed the closing `)` onto its own third line → shortened to `(러시아 12라운드)`; the line now wraps in 2 lines with the parenthesis attached.
2. P2 §B instruction bridge: tail `세요.` (word-split of 완성하세요) → shortened to `네모 속 단어나 알맞은 동사 형태로 완성하세요.` — now one line.
3. P3 §B instruction bridge: tail `요.` single-syllable orphan → `알맞은 동사 형태나 격으로 빈칸을 채우세요.` — now one line.
4. P7 phrase 2: the frozen page tag `(Страница 2)` split across lines (`2)` dangling) → translation shortened; the whole translation + tag now sits on one line.
5. P7 B2 bridge: tail `예요.` (copula dangling on a third line) → `…불확실함의 표현이에요.` — now 2 lines with a full tail.
6. P8 notes #45/#135 (the same core note, kept consistent): tail `째` (word-split of 두 번째) → `시간이 먼저, 동사는 둘째`.
7. P8 key #138: tail `비` (word-split of 진눈깨비) → key shortened to `예보원이 10월 말 진눈깨비를 예보해요.` (still a translation-item key diff, §5).

## 8. Notes for the independent proofreader

- Re-derive the P8 keys from the registry (hidden_files/ru-ko-reg-core.json and ru-ko-reg-edition.json are the builder's dumps; regenerate rather than trust). Expected key diffs: {137, 138, 150}; stems {139, 140}; identical notes {17, 35, 36, 63, 73, 90, 104, 110}.
- The two inherited occlusion flags (P1 BOXTITLE, P2 LINEX) exist identically in the shipped core — adjudicate against the core, not as new defects.
- The P8 answer block uses the RU core's own sizes (13.3 separators / 13.0 answers, lh 1.13), not the ES×KO sizes — the family rule is "the core's typography, the column's language".
- Height-critical Korean lines were pre-measured with the build's own wrap() to the core's line counts before the transform; the col3 end coordinates on P2/P7 match the core to 0.01 px.
- Scratch (transform script with the core's Chinese strings as search patterns, pristine pre-transform module copies, line-scan script, registry dumps) is confined to hidden_files/weekly-report-ru-ko-build/scratch/ and hidden_files/ru-ko-*.json; nothing operative references it.

## 9. Independent proofread record (2026-10-22) — PASS

All builder claims re-derived independently; scratch in hidden_files/proof-ru-ko/.

- **freeze baseline 8/8** byte-identical (run at start and again on the final build); shipped core untouched throughout.
- **Registry re-dumped independently** (one-process runs in repointed copies; the edition copy re-render reproduced the shipped SVGs 8/8 before the fix): structure identical, levels A2 54 · B1 72 · B2 24; **key diffs exactly {137, 138, 150}**, stems {139, 140} verified in the shipped P8 SVG; identical notes exactly {17, 35, 36, 63, 73, 90, 104, 110}; 142 notes translated (the 8 without Hangul are the match/score notes whose Chinese transliterations were replaced by the original Russian names — the Cyrillic citations in the freeze accounting); NWORDS = 82 in both builds. The proofreader's dumps are byte-equal to the builder's registry dumps.
- **All 150 keys re-derived by hand** from the Russian bodies/options/article facts (AST extraction aligned to the registry): zero discrepancies. P6 chart bars measured in the SVG: 600/494/388/282 px at x=685 = 34/28/22/16 % (ratio-exact), % labels at bar-end +14 px, zero overlap; the whole P6 rect multiset is identical to the core.
- **p8.py**: core extract = 150/150; compare **CLEAN**, keydiff [54, 137, 138]; #54 disproven as an extraction artifact by direct printed-line inspection (`54. третий — 3위: третий (남성 주격)`, key identical). P8 sizes/lh in code identical to the core (13.3/13.0, lh 1.13).
- **Defect found and fixed (1)**: P4 §D instruction bridge wrapped as «…빈칸을 채» / «우세요.» — the word 채우세요 split mid-word, leaving a fragment tail (README #16 class; the builder's orphan scan missed it because the tail is 3 syllables). Fixed in the explanation layer only: «괄호 속 동사를 알맞은 시제 형태로 바꾸세요.» — now renders as a single line; only the P4 SVG changed (other 7 pages byte-identical), one-process re-render + full gate re-run. The builder's other 7 fixes were verified in place individually.
- **Orphan re-scan (README #16口径, block-final elements incl. parenthesised fragments)**: after the fix, remaining candidates are all complete text — P1's two lines ending in an attached parenthetical, P5 gloss tail «집에 놀러 가요» (complete phrase), P8 #133 tail «시간» (complete word, token-boundary break; builder's adjudication upheld), P2 weather-word table entries.
- **Geometry**: occlusion_audit (selftest OK) 2 flags = core's 2 frozen-Russian flags, NEW = 0; same-baseline ink-collision scan (README #10, PIL ink boxes) 0 in edition and core; per-column max baseline / max rect bottom on P2 and P7 identical to the core in every column (incl. the 1682.96 box bottom).
- **Furniture (EN×KO §3)**: footers ×8 verbatim with «제 N 면 / 총 8 면»; badge INSERTED at y=574, 22pt/700/#a4553a, centred — adjudicated compliant: this core's y=330/372 are frozen Russian target text (absent from the freeze removed set), so the FR×KO/ES×KO inserted form is the correct precedent; gloss prefix «해설 — » single (9 boxes, no doubles); P8 separators ×8; gloss/expl item counts equal at all 29 call sites.
- **P7**: all 8 quotes verbatim from this issue's articles (whitespace-normalised check incl. the long quote 2), page-tag distribution identical to the core.
- **Calendar** (real 2026, Europe/Moscow): Oct 19 Mon · 21 Wed · 22 Thu · 23 Fri · 24 Sat · 25 Sun · 28 Wed · 31 Sat · Nov 4 Wed · Nov 5 Thu; holidays Oct 24–Nov 4 = 12 days; ministry Oct 26–Nov 3 = 9 days. Red line: no geopolitics lexicon anywhere in the Korean layer ( sole «핵» hit is «핵심» in a section sub-line).
- **Final pins (measured on disk after the fix)**: web PDF 3,532,952 B / sha256 4e6a1a34…; print PDF 24,343,479 B / sha256 59a3c344… (§1 updated).
