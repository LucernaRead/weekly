# REBUILD-LOG — W47 CONSOLIDATED re-rebuild R1: ru-de / ru-en / ru-fr / ru-es / core-ru

Date: 2026-11-12 ~00:15 UTC–. Worker: R1 consolidated re-rebuild.
Scratch dir (this log's home):
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ru-rerun-R1/`
Production dir: `~/workspace/weekly-git/production/2026-w47/` (main only, no branch).
Fixes in the source svglib.py copies (verified §0): Medium faces (first fix) + `_run_w`
(second fix), md5 `ee3211298f274e02ade2d4ca318ce354` in all 5 editions.
core-ru additionally: `content8.py:133` `img_h = 250` → `img_h = 200` (Morozko layout fix,
the ONLY production file touched; see §0b). DO NOT SYNC — scratch builds only.

## 0. Preconditions (verified before any build)

- Disk used 97G (< 100G stop line) at start; re-checked per build.
- svglib.py md5 in all 5 editions: `ee3211298f274e02ade2d4ca318ce354` (verified 00:15 UTC).
- Memory gate: `free -m` available was ~1030–1230 MB at start (edge-scan worker
  `pdf_edge_scan.py` ~1.26 GB RSS active, 43/130 editions at 00:13 UTC). The ru-de
  `_run_w` probe (00:01–00:03 UTC) built cleanly under the same edge-scan load, so
  after a short wait with no recovery, builds proceed serially with exit-code +
  OOM monitoring; any OOM failure would stop the run and wait the scan out.
  (Per-build available-MB recorded below.)

## 0b. core-ru production fix (ONE line, applied 00:15 UTC)

`production/2026-w47/core-ru/content8.py:133`: `img_h = 250` → `img_h = 200`.
`git diff` on that file shows exactly this one line. Nothing else in core-ru
touched (the `ru_textmd.py` / `svglib.py` diffs in `git status` predate this task:
the `_run_w` port worker's writes at 00:00:33 UTC).

## 1. BEFORE state (current production PDFs — mixed build states, verified)

Production is MIXED (confirmed against wave-A logs, census reproduced row-for-row):
- ru-de / ru-en / ru-fr production = wave-A Medium rebuilds (census matches wave-A
  AFTER exactly: ru-de 27/30, ru-en 29/32, ru-fr 28/31).
- ru-es production = PRE-Medium (wave A stopped per precondition — second fix had
  landed mid-wave; nothing wrong with the edition). Census 170/212, matches wave-A
  BEFORE exactly. Byline fused at 1.1 pt ("От редакцииLucerna").
- core-ru production = PRE-Medium (Medium build exists only as the Morozko-probe
  scratch build `probe-a1-run`). Census 188/262. Byline fused at 1.1 pt.
  P8 Morozko PLACED in production (keys end 2188.39, ends 2579.99).

Per-edition BEFORE SHAs/sizes: `before.sha256` in this dir.

(Tables to fill below per edition.)

## 2. ru-de — GREEN (all gates pass)

Builds: `ru-de-1/` (00:15–00:21 UTC, mem avail 1061 MB at start) + `ru-de-2/`
(00:24–00:26 UTC, mem avail 1384 MB). Both RC=0, TOTAL 150, P8 keys end
2331.72 (Morozko SKIPPED — as in production; only core-ru/ru-zh-tw have it),
integrity "production unchanged (42 files re-hashed)" both times.
Disk 98G at build 2.

- BEFORE (production, Medium): print `80024034…` 21,230,193 B; web `05b0a7ab…`
  3,384,428 B; text.md `d0f9b48c…` 63,471 B. Census 27 tokens / 30 boundaries.
- AFTER build 1: print SHA `1920da86eb76624b300a6c76f6acc3a0bfbb2921aab37ad111cd434e238e396c`
  21,229,165 B — **EXACT MATCH with the `_run_w` probe's print SHA** (reproducibility
  signal confirmed); web SHA `8366d304e95ba1a906b762f884dbcb636b1b321d47f1cdfe9c833f8b94ca9197`
  3,383,411 B vs probe web `254eb45f…` 3,383,424 B — 13-byte difference, webpdf
  font-subsetting nondeterminism across processes only (same class as the probe
  log §6 5-byte note); text layer identical to print per page (see below).
- Census AFTER (build 1): print = web = **12 tokens / 15 boundaries**, exactly the
  probe's FP set: `→После` ×3 (3.75), `A2→B1`/`A2→B2` (0.0, diagram connectors),
  `→Родительный` (3.75), P8 `→выходят/рассказывает/снял/сыграли/играет/победило/
  работаем` (2.40–2.41, normal median), `✓Mustertext` (2.41). **0 real joins.**
  All 15 fixed joins at normal gaps: 13ноября 2.47, Imperativ:не 2.35,
  20ноября 3.52, 19ноября 3.48, 16ноября 3.68, A.на 3.48, A.биография 3.63,
  A.снег 3.71, A.цена 3.72, A.точно 3.71, Tauwetter; 3.43, Rabattcode; 3.47,
  результатов+ 3.01, —скидка 2.41, —поздравляю 2.41. Text layer: spaced
  "13/19/20/16 ноября" present, fused forms absent, all 4. Byline unchanged
  2.89 / 2.82 (P4).
- Gates build 1: run.py TOTAL 150 (zero overflow); p8 extract 150/150;
  p8 compare vs production core-ru: CLEAN, keydiff [137, 138, 139, 140]
  (EXPECTED — German model answers); occlusion audit 0 flags (selftest OK);
  print/web text layers identical per page 8/8 (37,532 chars each).
- Freeze: **8/8 SVG SHA match** build 1 vs build 2; print PDFs byte-identical
  (same SHA `1920da86…`). (Build 2's build-copy web PDF is the stale copied
  production file — not a fresh build, same caveat as the probe.)
- KIT §5+§7 values (sync step applies): print
  `1920da86eb76624b300a6c76f6acc3a0bfbb2921aab37ad111cd434e238e396c`,
  21,229,165 B; web `8366d304e95ba1a906b762f884dbcb636b1b321d47f1cdfe9c833f8b94ca9197`,
  3,383,411 B. text.md unchanged (`d0f9b48c…`, verified via run-build integrity +
  build-copy hash — see §7).

## 3. ru-en — GREEN (all gates pass)

Builds: `ru-en-1/` (00:27–00:28 UTC) + `ru-en-2/` (00:30–00:32 UTC, mem avail
938 MB at start). Both RC=0, TOTAL 150, P8 keys end 2288.84 (identical to the
Morozko-probe production value — no reflow from `_run_w`), Morozko SKIPPED as
in production, integrity "production unchanged (42 files re-hashed)" both times.

- BEFORE (production, Medium): print `1fcc6aa4…` 21,249,828 B;
  web `7e67d006…` 3,379,458 B; text.md `5dba6455…`. Census 29 tokens / 32 boundaries.
- AFTER build 1: print SHA `e29ba5fae4a3886d19867a6c995786deec7afe307f48d79d301d6be5ae0fc81b`
  21,248,719 B; web SHA `7a3f635116c948b2c9605be4111859f212a117b5cc4240c20fadbd3321174f5b`
  3,378,370 B.
- Census AFTER (build 1): print = web = **12 tokens / 15 boundaries**, exactly
  the ru-de probe's FP set (with `✓See` for the native-language check token):
  `→После` ×3, `A2→B1`/`A2→B2`, `→Родительный`, P8 `→выходят/рассказывает/снял/
  сыграли/играет/победило/работаем` (2.40–2.41), `✓See` (2.41). **0 real joins.**
  All 15 shared fixed joins at normal gaps (13ноября 2.47, 20ноября 3.52,
  19ноября 3.48, 16ноября 3.68, A.на 3.48, A.биография 3.63, A.снег 3.71,
  A.цена 3.72, A.точно 3.71, результатов+ 3.01, —скидка 2.41, —поздравляю 2.41;
  P8 `Imperativ:` pair n/a — ru-en line reads "Negative imperative: не").
  Edition-specific BEFORE joins all cleared at normal gaps, fused forms absent
  from the text layer: `·середина` → "· середина" 3.47; `to;может` → "to; может"
  3.46; `imperative:не` → "imperative: не" 2.34; `row:пять` → "row: пять" 2.41;
  `Note:играть` → "Note: играть" 2.39. DATE text layer: spaced forms present,
  fused absent, all 4. Byline unchanged 2.89 / 2.82.
- Gates build 1: run.py TOTAL 150; p8 extract 150/150; p8 compare vs production
  core-ru: CLEAN, keydiff [137, 138, 139, 140] (EXPECTED — English model
  answers); occlusion 0 flags (selftest OK); print/web text layers identical
  per page 8/8 (37,122 chars each).
- Freeze: **8/8 SVG SHA match** build 1 vs build 2; print PDFs byte-identical
  (see SHAs above). (Build 2's build-copy web PDF is the stale copied
  production file, same caveat as the probe.)
- KIT §5+§7 values (sync step applies): print
  `e29ba5fae4a3886d19867a6c995786deec7afe307f48d79d301d6be5ae0fc81b`,
  21,248,719 B; web `7a3f635116c948b2c9605be4111859f212a117b5cc4240c20fadbd3321174f5b`,
  3,378,370 B. text.md unchanged.

## 4. ru-fr — GREEN (all gates pass)

Builds: `ru-fr-1/` (00:32–00:34 UTC, mem avail 1512 MB at start) + `ru-fr-2/`
(00:35–00:37 UTC, mem avail 1077 MB). Both RC=0, TOTAL 150, P8 keys end
2317.03 (identical to the Morozko-probe production value — no reflow),
Morozko SKIPPED as in production, integrity "production unchanged
(42 files re-hashed)" both times.

- BEFORE (production, Medium): print `32f2e168…` 21,290,501 B; web `2eb8062c…`
  3,384,329 B; text.md `e4cc50fd…`. Census 28 tokens / 31 boundaries.
- AFTER build 1: print SHA `c29251ebecb6125edbf7e9d4f66c6ff3371f164651563412a3db142d876ff6b5`
  21,289,489 B; web SHA `d17fc2255b1b6c7b15286ce6b111c8d8f9c3079b210dd372e144e6ca9918c4d6`
  3,383,322 B.
- Census AFTER (build 1): print = web = **14 tokens / 17 boundaries** = the ru-de
  probe's 12/15 FP set (with `✓Voir`) + 2 extra: `Ozon:` / `Wildberries:` (P5,
  gap None). **Both are FALSE POSITIVES, verified in source:** the P5 schedule
  lines are genuinely written without a space — `content56.py:33`
  `"Ozon: 13 ноября – 2 декабря."` and likewise `"Wildberries: 16–30 ноября."`
  (ink gap to ':' is 0.00, line word gaps 3.9–3.95 — the colon is part of the
  written form, as in the Russian core). The census flags them only because its
  text.md check is global: French key translations elsewhere write
  "Ozon : 13 novembre" (text.md lines 394/615/747/811). **0 real joins.**
  All 15 shared fixed joins at normal gaps (13ноября 2.47, 20ноября 3.52,
  19ноября 3.48, 16ноября 3.68, A.на 3.48, A.биография 3.63, A.снег 3.71,
  A.цена 3.72, A.точно 3.71, результатов+ 3.01, —скидка 2.41, —поздравляю 2.38;
  P8 `Imperativ:` pair n/a — ru-fr line is French). Edition-specific BEFORE
  joins cleared, fused forms absent, spaced present: `:пять` → ": пять",
  `:играть` → ": играть" ("— Attention : играть +"), `—поздравляю` →
  "— поздравляю". DATE text layer: spaced forms present, fused absent, all 4.
  Byline unchanged 2.89 / 2.82.
- Gates build 1: run.py TOTAL 150; p8 extract 150/150; p8 compare vs production
  core-ru: CLEAN, keydiff [137, 138, 139, 140] (EXPECTED — French model
  answers); occlusion 0 flags (selftest OK); print/web text layers identical
  per page 8/8 (37,505 chars each).
- Freeze: **8/8 SVG SHA match** build 1 vs build 2; print PDFs byte-identical
  (same SHA `c29251eb…`). (Build 2's build-copy web PDF is the stale copied
  production file, same caveat as the probe.)
- KIT §5+§7 values (sync step applies): print
  `c29251ebecb6125edbf7e9d4f66c6ff3371f164651563412a3db142d876ff6b5`,
  21,289,489 B; web `d17fc2255b1b6c7b15286ce6b111c8d8f9c3079b210dd372e144e6ca9918c4d6`,
  3,383,322 B. text.md unchanged.

## 5. ru-es — GREEN (all gates pass)

Builds: `ru-es-1/` (00:38–00:39 UTC) + `ru-es-2/` (02:03–02:04 UTC, mem avail
1109 MB at start). Both RC=0, TOTAL 150, P8 keys end 2331.72 (identical to
the Morozko-probe production value — no reflow from `_run_w`), Morozko
SKIPPED as in production, integrity "production unchanged (42 files
re-hashed)" both times.
NOTE — the first `ru-es-2` attempt was killed mid-render by the session abort
(00:41 UTC: run.py had finished TOTAL 150, render.py was running; the
build-copy still held the stale production PDF, 0 integrity lines). The
partial dir was removed and build 2 re-run clean from scratch; the freeze
below is build 1 vs the clean re-run.

- BEFORE (production, PRE-Medium — wave A stopped per precondition, second fix
  had landed mid-wave; nothing wrong with the edition): print `64cb48f9…`
  21,278,615 B; web `526873a8…` 3,387,494 B; text.md `332c8e4f…`. Census
  **170 tokens / 212 boundaries** (matches wave-A BEFORE exactly). Byline
  fused at 1.1 pt ("От редакцииLucerna"); body-text fusions throughout
  (редакцииLucerna 1.1, Устойчивыйснег 1.26, Сколькоочков 1.44, …).
- AFTER build 1: print SHA `deb7b08e1697793a0412cf5c06c85fbc737393e50a6407fa83864b5ccb2ad31e`
  21,276,149 B; web SHA `8c1bb27e7bf3bc3bb79a5cc1fe534b7499719158f7532dd90b18b10719f401d4`
  3,385,029 B. (This rebuild carries BOTH fixes for ru-es: the Medium faces
  from its svglib source + `_run_w`.)
- Census AFTER (build 1): print = web = **12 tokens / 15 boundaries**, exactly
  the ru-de probe's FP set (with `✓Véase` for the native-language check token):
  `→После` ×3, `A2→B1`/`A2→B2`, `→Родительный`, P8 `→выходят/рассказывает/снял/
  сыграли/играет/победило/работаем` (2.40–2.41), `✓Véase` (2.41). **0 real joins**
  — down from 170/212. All 15 shared fixed joins at normal gaps (13ноября
  2.47, 20ноября 3.52, 19ноября 3.48, 16ноября 3.68, A.на 3.48, A.биография
  3.63, A.снег 3.71, A.цена 3.72, A.точно 3.71, результатов+ 3.01, —скидка
  2.41, —поздравляю 2.37; P8 `Imperativ:` pair n/a — ru-es line is Spanish).
  Pre-Medium body fusions all cleared: byline restored to 2.89 / 2.82 (P4);
  "От редакции Lucerna", "Устойчивый снег", "Сколько очков", "17 ноября"
  spaced in the text layer, fused forms absent. Edition-specific BEFORE join
  `Atención:играть` (−0.12) → "Atención: играть", ink gap 2.36 pt = the line
  normal (2.36–2.41; same as ru-en's "Note: играть" 2.39). DATE text layer:
  spaced forms present, fused absent, all 4.
- Gates build 1: run.py TOTAL 150; p8 extract 150/150; p8 compare vs production
  core-ru: CLEAN, keydiff [137, 138, 139, 140] (EXPECTED — Spanish model
  answers); occlusion 0 flags (selftest OK); print/web text layers identical
  per page 8/8 (37,577 chars each).
- Freeze: **8/8 SVG SHA match** build 1 vs build 2 (clean re-run); print PDFs
  byte-identical (same SHA `deb7b08e…`). (Build 2's build-copy web PDF is the
  stale copied production file, same caveat as the probe.)
- KIT §5+§7 values (sync step applies): print
  `deb7b08e1697793a0412cf5c06c85fbc737393e50a6407fa83864b5ccb2ad31e`,
  21,276,149 B; web `8c1bb27e7bf3bc3bb79a5cc1fe534b7499719158f7532dd90b18b10719f401d4`,
  3,385,029 B. text.md byte-identical (`332c8e4f…`, build-copy hash verified).

## 6. core-ru — GREEN (all gates pass, Morozko restored)

Builds: `core-ru-1/` (02:05–02:07 UTC) + `core-ru-2/` (02:13–02:16 UTC, mem
avail 1596 MB at start). Both RC=0, TOTAL 150, integrity "production
unchanged (45 files re-hashed)" both times.

- Production fix (verified, NOT re-applied): `content8.py:133` reads
  `img_h = 200` (applied 00:15 UTC, §0b). `git diff` on that file shows exactly
  this one line. The `ru_textmd.py` / `svglib.py` diffs in `git status` predate
  this task (the `_run_w` port worker, 00:00:33 UTC).
- Geometry (re-verified under `_run_w`, as the Morozko probe §6 required):
  P8 keys end col 3 y **2216.58 — EXACTLY the probe value** (`_run_w` causes no
  reflow, as its comment claims). Morozko ends **2558.18 — EXACTLY the
  predicted value**. Margins vs the probe §2: guard 2240.58+200+90 = 2530.58 <
  2560, **skip trips at +29.42** further keys growth; true caption end 2558.18
  is 1.82 inside the soft CONTENT_BOTTOM 2560 (same standing as the OLD shipped
  build, which ended 2579.99 — passing 2560 is not a failure by that standard);
  **footer-rule (2596) crossing at +37.82**.
- Morozko image + caption PRESENT on P8: SVG
  `<image x="1439.5" y="2240.58" width="422.5" height="200"
  preserveAspectRatio="xMidYMid slice">`; caption baselines 2464.58 /
  2490.23 (19pt, "«Морозко»: иллюстрация Ивана Билибина, 1932 год. Зимняя
  сказка — к ноябрю."), credit 2517.88 / 2538.03 (15.5pt, "Иллюстрация: Иван
  Билибин — общественное достояние (Wikimedia Commons)") — all exactly the
  probe's predicted values; all caption/credit words present.
- Images: print PDF per-page [1,1,0,1,1,0,1,1] total **6 (P8=1)**; web PDF
  identical; production identical.
- BEFORE (production, PRE-Medium — Medium build exists only as the
  Morozko-probe scratch build): print `d60fbd6c…` 31,429,147 B; web
  `b5d67aeb…` 4,025,900 B; text.md `348511e0…` (both .text.md files
  byte-identical). Census **188 tokens / 262 boundaries**. Byline fused at
  1.1 pt. P8 Morozko PLACED in production (keys end 2188.39, ends 2579.99).
- AFTER build 1: print SHA `c2fd743e16fec66c13cf1f610445c5b1c35f209279d6e5cdfdc0d2deec7202a2`
  31,426,561 B; web SHA `a4f4bbd61deb3574a9e66acaf4d7d0e2cd613cfadf6f235bf007555555c81c7f`
  4,023,304 B. (Print is 1,042 B smaller than the Medium probe's 31,427,603 B:
  `_run_w` moved x positions; expected.)
- Census AFTER (build 1): print = web = **42 tokens / 58 boundaries**, down
  from 188/262. Adjudication (arithmetic closes: 42 = 11 + 28 + 3 tokens;
  58 = 14 + 36 + 8 boundaries):
  - **11 tokens / 14 boundaries — the probe's FP set** (no ✓ token in core):
    `→После` ×3, `A2→B1`/`A2→B2`, `→Родительный`, P8 `→выходят/рассказывает/
    снял/сыграли/играет/победило/работаем` (2.40–2.41, normal median).
  - **28 tokens / 36 boundaries — CJK extraction artifacts** (P8 zh-cn
    model-answer lines; Chinese has no inter-word spaces by design):
    '泽尼特与迪纳摩各31分', '黑五11月16日开始', '第15轮11月20日',
    '黑五11月13日–12月2日', '网络星期一11月30日', '一周5个工作日',
    '14轮11月8日结束', '14轮共进21球', '国际大学生节11月17日',
    '俄罗斯主要大学生节是1月25日', '太阳约16:20', '第14轮共8场比赛',
    '罗斯托夫83分钟扳平', '国家队周二19:00', '日历黑五是11月27日星期五',
    '黑五11月16–30日', '俄罗斯自2013年办黑五', '五部首映11月19日' (gaps
    2.32–2.40, at the P8 normal) + the '·'-suffixed glosses (截至交稿时·,
    祝取得成绩·, 改编成电影·, 扳平比分·, 奠定节奏·, 名副其实的·, gap 3.44)
    + '“黑色星期五”：11月16日开始打折' (full-width colon, CJK no-space
    form) + '后面用гол：забили' + '参考答案—' (gap 4.26, wide) +
    '约16:20' (time form). Every one of these appears in the Morozko probe's
    adjudicating census of the Medium build as CLEAR-EXTRACTION (except
    '后面用гол：забили' = CLEAR-REALSPACE). CJK totals unchanged vs Medium
    (980 → 980) and vs production.
  - **3 tokens / 8 boundaries — '8.11.' (4x), '7.11.' (3x), '6.11.' (1x)**,
    gap 0.0. NOT joins: the source writes them genuinely without a space —
    `content34.py:150–152` `("Вс 8.11.", "«Крылья Советов» — ...")`; the
    fixture lines are not in text.md at all (verified: no '8.11' in
    `2026-w47-ru-core.text.md`), so the census flag comes only from its
    global ". 11" check matching elsewhere — the same global-check
    over-flagging as the ru-fr `Ozon:` case. Same class as the census doc's
    own "11.11" genuine-no-space example.
  - **ГЛАГОЛЫИ: GONE** — not in the AFTER census at all. Fused form absent
    from the text layer, spaced 'ГЛАГОЛЫ И' present. `_run_w` resolved the
    bold-caps bbox artifact the Medium build still showed (2.62 pt).
  **0 real joins.** All 15 shared fixed joins at normal gaps (13ноября 2.47,
  20ноября 3.52, 19ноября 3.48, 16ноября 3.68, A.на 3.48, A.биография 3.63,
  A.снег 3.71, A.цена 3.72, A.точно 3.71, результатов+ 3.01, —скидка 2.41,
  —поздравляю 2.34; P8 `Imperativ:` pair n/a — core P8 carries the Chinese
  gloss, no "Imperativ:" token; no imperative join appears in the census).
  Byline restored to 2.89 / 2.82 (from fused 1.1). DATE text layer: spaced
  forms present, fused absent, all 4.
- Gates build 1: run.py TOTAL 150; p8 extract 150/150; p8 compare vs the
  Medium-probe build (`probe-a1-run`): CLEAN, keydiff []; p8 compare vs
  production core-ru: CLEAN, keydiff []; occlusion 0 flags (selftest OK);
  print/web text layers identical per page 8/8 (31,504 chars each).
  Text-layer cross-checks (fitz get_text): mine vs production print — only
  +263 spaces +14 newlines, **0 non-space character differences**; mine vs
  Medium probe build — only +30 spaces +1 newline, 0 non-space differences.
  (The Morozko probe's "25,934 chars" was a whitespace-excluding count;
  by the same get_text method production is 31,227 and the Medium build
  31,473.)
- Freeze diff vs the Medium NO-Morozko scratch build
  (`scratch-ru-rebuild-C/core-ru/build/build-copy/svg`, via `tools/freeze.py
  diff`): **P1–P7 +0/−0 strings**, CJK totals unchanged, 0 added Latin;
  **P8 +32/−0** — every added string is a Morozko caption/credit word or
  punctuation; the 1 "unexpected" added Latin string is '(Wikimedia
  Commons)' (restored credit line, present in the old production build) —
  exactly the probe's freeze result. Freeze diff vs the Medium+Morozko
  probe build: **+0/−0 on all 8 pages** (text content identical). Freeze
  diff vs OLD production SVGs: **0 Cyrillic-bearing strings added or removed
  on any page**, CJK totals unchanged on all pages (only space/punct
  re-segmentation).
- Freeze: **8/8 SVG SHA match** build 1 vs build 2; print PDFs byte-identical
  (same SHA `c2fd743e…`). (Build 2's build-copy web PDF is the stale copied
  production file, same caveat as the probe.)
- KIT §5+§7 values (sync step applies): print
  `c2fd743e16fec66c13cf1f610445c5b1c35f209279d6e5cdfdc0d2deec7202a2`,
  31,426,561 B; web `a4f4bbd61deb3574a9e66acaf4d7d0e2cd613cfadf6f235bf007555555c81c7f`,
  4,023,304 B. text.md byte-identical (`348511e0…`, both files verified).

## 7. Wrap-up — all 5 editions GREEN

### text.md byte-identity (build-copy vs production, all verified by SHA-256)
| Edition | text.md SHA (both sides) | Identical |
|---|---|---|
| ru-de | `d0f9b48c…` | yes |
| ru-en | `5dba6455…` | yes |
| ru-fr | `e4cc50fd…` | yes |
| ru-es | `332c8e4f…` | yes |
| core-ru (ru-core + ru-zh-cn) | `348511e0…` | yes (both files) |

### KIT §5+§7 values for the sync step (build-1 outputs; do NOT edit KIT files here)
| Edition | Print SHA-256 | Print bytes | Web SHA-256 | Web bytes |
|---|---|---|---|---|
| ru-de | `1920da86eb76624b300a6c76f6acc3a0bfbb2921aab37ad111cd434e238e396c` | 21,229,165 | `8366d304e95ba1a906b762f884dbcb636b1b321d47f1cdfe9c833f8b94ca9197` | 3,383,411 |
| ru-en | `e29ba5fae4a3886d19867a6c995786deec7afe307f48d79d301d6be5ae0fc81b` | 21,248,719 | `7a3f635116c948b2c9605be4111859f212a117b5cc4240c20fadbd3321174f5b` | 3,378,370 |
| ru-fr | `c29251ebecb6125edbf7e9d4f66c6ff3371f164651563412a3db142d876ff6b5` | 21,289,489 | `d17fc2255b1b6c7b15286ce6b111c8d8f9c3079b210dd372e144e6ca9918c4d6` | 3,383,322 |
| ru-es | `deb7b08e1697793a0412cf5c06c85fbc737393e50a6407fa83864b5ccb2ad31e` | 21,276,149 | `8c1bb27e7bf3bc3bb79a5cc1fe534b7499719158f7532dd90b18b10719f401d4` | 3,385,029 |
| core-ru | `c2fd743e16fec66c13cf1f610445c5b1c35f209279d6e5cdfdc0d2deec7202a2` | 31,426,561 | `a4f4bbd61deb3574a9e66acaf4d7d0e2cd613cfadf6f235bf007555555c81c7f` | 4,023,304 |

Census summary (print = web in every case): ru-de 27/30 → 12/15; ru-en 29/32
→ 12/15; ru-fr 28/31 → 14/17 (the +2 are the verified `Ozon:`/`Wildberries:`
false positives); ru-es 170/212 → 12/15; core-ru 188/262 → 42/58 (11 FP +
28 CJK-extraction + 3 date-form tokens; 0 real joins). All 5: 0 real joins,
DATE cases gone, print/web text layers identical per page, run.py TOTAL 150,
p8 extract 150/150, p8 compare CLEAN (keydiff [137,138,139,140] for the four
ru-* editions, [] for core-ru), occlusion 0 flags, freeze 8/8 + print PDFs
byte-identical between the two independent builds.

### Final production integrity
- `sha256sum -c before.sha256`: all production PDFs + text.md files for the 5
  editions byte-identical to the BEFORE state (no production PDF/text.md was
  written by this task).
- `git diff` in production: exactly one file changed — `core-ru/content8.py`,
  the single authorized line (`img_h = 250` → `img_h = 200`). The
  `ru_textmd.py` / `svglib.py` diffs predate this task.
- NO sync performed: no built PDF copied into production, no KIT file edited,
  no commit/push/lint. All builds live in scratch under this dir only.
- Disk: 97G at start → 99G at end (stop line 100G; my 10 builds are ~0.5G,
  the rest was written by concurrent workers — R3 wave, edge scan, secondary
  motion). Flag for the parent: the disk is 1G from the stop line.

### Files in this scratch dir
- `REBUILD-LOG.md` (this file), `before.sha256`, `census.py`, `line_gaps.py`,
  `gap_rude.py`, `textlayer.py` (tools), `census-before-*.json/.log`,
  `census-after-*-1-print/web.json/.log`, `gap-before-*.log`,
  `gap-after-*-1.log`, `textlayer-*-1.json`, `*-1-p8-extract/compare.json/.log`,
  `*-1-occlusion.json/.log`, `core-ru-1-freeze-vs-medium*.json/.log`,
  `core-ru-1-freeze-vs-production.json/.log`, `*-1-build.log`, `*-2-build.log`,
  `ru-de-1/`, `ru-de-2/`, `ru-en-1/`, `ru-en-2/`, `ru-fr-1/`, `ru-fr-2/`,
  `ru-es-1/`, `ru-es-2/`, `core-ru-1/`, `core-ru-2/` (run_build scratch dirs:
  `build-copy` + `run-build.log` each).
