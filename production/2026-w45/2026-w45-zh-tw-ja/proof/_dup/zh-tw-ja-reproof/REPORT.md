# Independent RE-PROOFREAD — W45 ZH-TW × JA (Traditional Chinese target · Japanese reader)

**Verdict: PASS — ZERO PROBLEMS.** Full round from scratch per SOP §8.4
(§8 loop rule: any problem → fix in source → full re-render → full re-proof
until a whole round returns zero problems). This round returns zero problems
across all 18 gates below, including Gate 10 reproduction, Traditional
independence, and the kinsoku fix verification with my own scan at 0.
This report is the finalization evidence for the coordinator to insert.
Nothing here was posted to Discord or main chat; `weekly-git` was not
touched, `insert.py` was not run, no cron was created, no shared scratch
dir was cleaned, no subagent was spawned.

**Slug:** `2026-w45-zh-tw-ja` · **Issue week:** Nov 2–8, 2026 · **Pages:** 8 ·
**Exercises:** 150 · **Proof dir:** `hidden_files/w45/zh-tw-ja-reproof/`
(work files under `work/`; scripts `reproof.py`, `attrib.py`,
`letterbox.py`, `scans_copy.py`, `dump_driver.py`; Gate 10 replay under
`work/gate10/`; regenerated freeze diff `work/freeze-diff-fix.json`).

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker writing to the delivery/build dirs: `ps` at round start
  showed only system processes; no Python/render/transform process touched
  either dir.
- (b) Two mtime snapshots of both dirs (`work/snap1.txt` 09:51 UTC,
  `work/snap2.txt` 09:54 UTC): ZERO changes; every delivery/build file
  mtime ≤ 09:50 UTC (fix session finished 09:50).
- (c) Fix session completed: delivered run-fix/render-fix/verify-fix logs
  all closed, Gate 10-fix logs closed with exit 0 and registry 150.
- Pre-flight PASSED; the proof proceeded. No content module was ever
  imported inside the core build dir — all re-runs used fresh copies under
  `work/` only. No SVG was ever grepped directly; all SVG reads used
  XML parsing or targeted extraction scripts.

## The two blocking items from the first proof — both FIXED and verified

- **B1 (P5 gloss, small ィ):** old stranded form GONE. Delivered P5 nodes:
  `花笠舞、韓国のJUMPによるテコンドー・` (y=1962.445) +
  `コメディショー、毎日14時のマスコットパ…` (y=1992.17) — the loanword
  sits whole on one line; gloss line count unchanged at 7 lines. Old
  fragment `韓国のJUMPテコンドー・コメディショー` absent; new fragment
  `韓国のJUMPによるテコンドー・コメディショー` present. Meaning preserved
  (added による is purely grammatical); target text untouched.
- **B2 (P8 key-2 note, small ョ):** old stranded form GONE. Delivered P8
  key 2: `2. A — メインカンファレンスは香港コンベンション・エキシビション・セ`
  (y=1397.072) + `ンターで開催。` (y=1411.408) — clean line head ン, not a
  small kana. Old `アンド・エキシビション` absent; new
  `コンベンション・エキシビション・センターで開催` present; subject
  (`メインカンファレンスは香港…`) and venue preserved, key–note
  correspondence intact. Editorial concurrence: I do NOT prefer the first
  proof's shorter suggestion (`香港コンベンションセンターで開催。`) — it
  drops the main-conference subject, while the fixer's アンド-drop form
  passes the scan and preserves the note's full meaning. No editorial
  objection raised, and nothing is blocked on this choice.
- No other text changed by the rewordings: change-scope check (gate 18)
  confirms only P5/P8 differ from the first build.

## Per-gate evidence (all independently re-run, not taken from the builder KIT)

1. **Freeze baseline + target-text attribution — PASS.** `freeze.py
   baseline` on a fresh core-build copy: **8/8 byte-identical**, core
   prefixes match the core KIT exactly; shipped core SVGs re-hashed
   unchanged. Regenerated `freeze.py diff --strict-cjk` (my own JSON,
   NOT the pre-fix JSON): STRICT-CJK FAIL display with TOTAL added CJK
   **5992** (per page 395/342/414/353/418/431/1140/2499; string counts
   +22/−22, +33/−35, +38/−38, +33/−33, +37/−40, +37/−37, +88/−90,
   +192/−191) — structurally inevitable for a Japanese explanation layer,
   NOT a failure. The delta vs the first build is exactly the two
   rewordings (P5 415→418 for による, P8 2503→2499 for dropped アンド).
   Correct close, re-derived with fresh code (`work/attrib.py`) on the
   regenerated JSON: **A1 = 0, A2 = 0, B1 = 0, B2 = 0**. Two pure-Hanzi
   added fragments initially flagged by a prefix-naive check were resolved
   as wrapping artifacts of Japanese transform strings (P3 gloss
   `高雄国際鉄彫刻祭…` after the `解説 — ` prefix; P8 key 97
   `合計開場時間：30時間。` after the `97. 30 — ` prefix) — both verified
   present verbatim in transform new strings. Zero FLOW OVERFLOW / HEAD
   TOO WIDE warnings in the delivered run and in my Gate 10 replay.
2. **Traditional independence — PASS (hard gate).** Re-extracted myself
   (XML parse, CJK-filtered sets): edition CJK **1029**, union of (W43
   zh-tw-ja + zh-tw core) **1288**, outside **57** — the exact list in
   the builder KIT §3. Every outside character adjudicated node by node:
   all 57 occur in Japanese explanation-layer nodes (kana-bearing lines);
   the only no-kana-line occurrences are the same wrapped-line artifacts
   as the first proof (彫 in the P3 gloss first line, ／ in P7
   `（立冬／進補）。`, ～ in P3 gloss and P8 key notes 41/42, 点 in P8 key
   60 `1 + 5 = 合計6点。`) — continuations of Japanese sentences, not
   target text. Simplified-only spot list over frozen shared strings:
   **0 hits**; over ALL edition strings the only hits are 国/学/点, every
   occurrence in Japanese-layer nodes. Shinjitai inside the Japanese layer
   is not a violation; no Simplified-form character occurs in Traditional
   target text. No OpenCC/conversion/mapping logic in the transform
   (source read + token grep: OpenCC, opencc, s2t, t2s, mapping, convert(
   all absent; 280 rep pairs counted by AST, matching the first proof's
   280 rep + 6 repoints = 286 log lines).
3. **Target text zero difference — PASS.** Attribution B1/B2 = 0 (gate 1);
   registry keys identical 150/150 (gate 5); all 8 golden sentences
   verbatim from the core (gate 10); image payloads byte-identical
   (gate 11); readers'-corner Traditional letter + disclosure line-for-line
   identical (gate 12).
4. **Gate 10 reproduction — PASS (mandatory, blocking-class gate).** Fresh
   copy of the core build dir + the builder's `transform.py` ALONE,
   one-process driver (`run.py` → `render.py`) in `work/gate10/`:
   transform exit 0 (no delivery-dir reference left in the copy), run
   exit 0 with zero `!!` warnings and registry 150 (A2 44 / B1 74 /
   B2 32; pages 10/18/18/18/18/18/12/38; types 67/54/16/12/1), render
   exit 0. Result: **SVGs 8/8 byte-identical** to delivered, **cards 8/8
   byte-identical**, print PDF byte-identical. No stray nested tree: the
   delivery dir contains only `svg/` + `cards/` + PDFs + ABSTRACT.txt +
   WEEKLY-KIT.md; the build dir's `gate10/` and `gate10-fix/` subtrees are
   the builder's own documented Gate 10 runs, not inherited templates.
5. **P8 — PASS.** Default-form invocation (tables.json zh-tw `p8_file`
   is `p8-test.svg`, so no explicit-path form was needed):
   `p8.py compare --core-dir …/weekly-report-w45-zhtw-core --edition-dir
   …/weekly-report-w45-zh-tw-ja --target zh-tw` → **CLEAN, 150=150,
   missing=[], extra_count=0, keydiff=[]**. `p8.py extract` on the
   delivered P8: noted set **150/150**, parse lines (dash style).
   Registry dumps from fresh one-process runs of core copy vs transformed
   copy (`work/reg_core.json`, `work/reg_ed.json`): keys **0 diffs**,
   level/page/type **0 diffs**; notes differ on all 150 by
   English→Japanese translation (the fan-out's purpose); writing item 150
   key `(開放題,範文如下)` identical, note translated like all others.
   (On the task's "writing-item change only" phrasing: as the first proof
   recorded, the substantive gate — keys identical, noted set 150/150 —
   passes; the writing item differs from the other 149 only in its
   printed ✓ form on P8, which `p8.py compare` already adjudicates CLEAN.)
6. **Kinsoku fix verification — PASS (critical gate, my own scan).**
   Method (W43 zh-tw-ja precedent, re-implemented independently with XML
   parsing in `work/reproof.py`): every `<text>` node's first character
   against renderer NO_START punctuation
   (`。、，．！？：；）」』】％ー…‥・)]}〉》.,!?%:;"`) PLUS small kana
   `ぁぃぅぇぉっゃゅょゎゕゖァィゥェォッャュョヮヵヶ`, last character
   against NO_END (`「『（【〈《([{"`), over ALL 8 delivered SVGs.
   **Result: nodes 1425, NO_START 0, small-kana line starts 0, NO_END 0.**
   The builder's `verify.py` section H and `scans.py` KINSOKU section
   (re-run from a proof copy) agree at the same 1425/0/0/0. A rewording
   that merely moved a stranded kana to another line head would have
   failed this scan; both fixes place the loanwords whole on one line.
   W43 shipped SVGs re-scanned with the same method: 0/0/0, confirming
   the method reproduces the precedent.
7. **P8 dash style + AI-variant trap — PASS.** Dash verified from the
   W43 zh-tw-ja build code itself (`content8.py` lines 118/120:
   `f"{n}. {key} — {note}"`, writing `f"{n}. ✓ {note}"`) and from shipped
   W43 P8 key lines (`1. B — …`, `150. ✓ 開放課題 — …`); this edition's
   code and shipped key lines match (dash; separators `— N ページ —`
   at W45 core metrics 12.8pt/lh 1.12/gap 1). AI forms, all verified in the
   final render: P6 gloss `AI＋（銀行・投資・保険の中のAI）`, P6 note
   `AIはデータを見て、リスクを見つけ、顧客の質問に答える手伝いをする。`
   (key 88), P8-key note `金融の中のAIは人工智慧＋。` (key 138, verbatim
   target term kept). Adjudication against THIS column: W43 zh-tw-ja
   content sources contain no AI string (grep over its build sources:
   no AI string), so no column rule exists to import; keeping the verbatim
   term in the P8-key note is correct because the term IS the key, and it
   introduces no new target CJK (the term already occurs in the core's key
   and P6 article). Target-text attribution stays clean (gate 1). Stray
   ASCII apostrophes **0** (core: 28, all in replaced English notes).
8. **Occlusion + geometry — PASS.** `occlusion_audit.py --selftest` OK;
   edition **0 flags**, core **0 flags**, NEW vs core **0**. Same-baseline
   ink-collision scan (builder `scans.py`, re-run from a proof copy):
   edition **0**, core **0**. P4/P6 chart-label graze: **0/0**.
   Border-strike: **0/0**. **P7 letter-box DIRECT measurement
   (mandatory, re-measured myself):** SVG — rect (1451, 1184.86,
   434×576.5), stroke edge bottom 1762.06; last disclosure ink bottom
   **1753.63** (audit's own `ink_box`, Noto Sans CJK TC 20pt) →
   **8.43px clearance, fully inside**; card pixels — last ink row 1752,
   border-tan stroke row 1761 (430 pixels) → **9px clearance, fully
   inside**. P7 teaser rect bottom **2559.36** (20.64px clear of the 2580
   rule), last teaser ink **2528.11**. P8 keys end ink **2538.10** (keys
   40/81/121, baseline 2536.848, 12.8pt), clear of the footer rule.
9. **Gloss/match/registry — PASS.** Gloss boxes core = edition =
   2/2/3/2/2/1/0/0 (total 12); no core gloss string contains `·`, so
   items = calls = 12 (NOT zh-cn's 33). Match sets: 4 (content12 1,
   content34 2, content56 1) × 4 items = **16** 配對, matching the
   registry. Registry 150 (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/
   12/38; types 67/54/16/12/1; writing MODELO text verbatim identical in
   core and edition sources, label only changed: `Model answer: ` →
   `モデル解答：`).
10. **P7 golden sentences — PASS.** All 8 verbatim from this issue's own
    articles, each exactly **2× issue-wide** in BOTH core and edition
    after punctuation normalisation (concatenated-issue counts, not
    per-node counts). Tags (p. 1)×2, (p. 2)×1, (p. 3)×2, (p. 4)×1,
    (p. 5)×1, (p. 6)×1 — identical in core and edition. The 3 error-clinic
    「…」 lines count 1× each, as expected. KIT §6 correction verified:
    it now reads p. 1×2, p. 2, p. 3×2, p. 4, p. 5, p. 6, and the EDITION
    matches the core (the first proof's KIT-typo note is closed).
11. **Images — PASS.** Per-page payload hashes byte-identical core vs
    edition: p1 `ac4dfe2ad3a43cd3` (harbour.jpg, Wilfredor, CC0), p2
    `a40e7a2b265beba6` (rain.jpg, CorraleH, CC0), p3 none, p4
    `18ad8ae06fac2860` (baseball.jpg, Bain News Service, Public domain),
    p5 `bcbada13a5ae19d6` (pumpkin.jpg, Benjamin Balazs, CC0), p6/p7/p8
    none. Credit lines verbatim identical on all pages. P4 provenance
    NOT re-litigated: placed bytes and credit line are unchanged from the
    core, and the core KIT's 2026-10-27 binding adjudication (CLOSED) is
    respected.
12. **Readers' corner — PASS.** Traditional letter (4 wrapped nodes) and
    Traditional disclosure (5 wrapped nodes) line-for-line identical to
    the core (verified node by node). The 4 apparent "missing" Traditional
    nodes in a naive no-Latin filter are English-layer tails (fair-words
    list tail, group-words tail, local-words tail) and the furniture page
    line — all legitimately replaced by Japanese, not letter/disclosure
    text. Japanese disclosure (6 nodes) states no genuine letters exist
    (`本物の投書ではない`, `掲載できる投書がなく`) and ends with the
    verbatim open invitation `あなたの手紙を次号でお待ちしています。`,
    matching the W45 core's deferral form (not W43's forward-promise form).
13. **Furniture three-way — PASS.** Badge measured on all three P1s: core,
    W43 zh-tw-ja, and this edition are ALL x=975, y=378, 21pt, weight 700,
    fill **#3e4c2a (OLIVE)**, with this edition's badge text identical to
    W43's (`中国語（繁体字）テキスト · 日本語の解説 — 日本語読者のための版`).
    The task brief's BRICK claim was wrong against both shipped references
    (non-blocking brief error, NOT an edition defect — unchanged from the
    first proof). Footer VOL.2-adapted Japanese form on all 8 pages; page
    lines `N ページ（全 8 ページ）` identical to W43; gloss prefix
    `解説 — ` identical to W43; P8 header, right header, band
    (`測驗與答案 · テストと答え`), band sub
    (`第 8 版 · 本週大測驗 + 全部答案 · 今週のテストと全解答`), and
    separators identical to W43 (separator metrics per gate 7). svglib
    byte-identical across core, edition, and W43
    (md5 `a269e147529bcb0a1f2dd3aa22fa5658`). tables.json NOT edited by
    this proof (default-form p8 invocation resolved correctly).
14. **Residual Latin rendered sweep — PASS.** Full sweep of all edition
    text nodes re-run independently. Every Latin-containing node is
    adjudicated: masthead/band/footer `Lucerna`; frozen edition line
    (VOL.2, dates); Japanese bylines retaining `FAQ`, `TSNA`; frozen
    article proper names (`StartmeupHK`,
    `Fintech Nexus: Bridging the World, Building the Future`, `ITF`,
    `SUPER STAGE`, `SOLID TIDES`, `Trick or Treat`, `JUMP`, `MVP`);
    Japanese gloss citations (`StartmeupHK`, `ITF`, `JUMP`,
    `MVP（最優秀選手）`); photo credits
    (`Photo: … — CC0 / Public domain (Wikimedia Commons)`); P7 `VOL.1`
    (frozen + Japanese disclosure) and teaser `次号予告（VOL.3）`; P8-note
    abbreviations `AI`, `MVP`, `SNS`; P7 tags `(p. N)`; P8 key letters.
    No English explanation prose remains. `算一算 · 計算してみよう`
    present on P2, P3, and P5 (1 node each, P3 confirmed visually on the
    card); `Work it out` = 0 and every other English head = 0.
15. **Web regen — PASS.** Gate 10 replay: cards **8/8 byte-identical**,
    print PDF **byte-identical**; web PDF **content-identical**: same
    size 3,309,173, 8 pages, only **8 bytes differ, all inside the
    CreationDate/ModDate timestamps** (delivered 20261028094729Z vs replay
    20261028095548Z) — the timestamp exception, stated explicitly as
    required.
16. **Eyeball all 8 cards — PASS.** Layout clean on all pages: no overflow,
    no overlap, no missing content, no footer collision, images/credits
    placed correctly, Japanese typesets correctly on the TC face, no
    missing-glyph boxes. P5 gloss area visually clean (コメディショー whole
    on one line, no stranded kana); P8 key-2 area visually clean
    (…エキシビション・セ / ンターで開催。); P7 teaser/footer clearance
    confirmed visually; P7 readers'-corner last line fully inside its box
    with clear space below.
17. **ABSTRACT.txt — PASS.** Single line (one trailing newline, 174
    characters), no ASCII double quotes, in Japanese, naming: Lucerna,
    中国語（繁体字）, VOL.2, 11月2日～8日, A2～B2, 全150問, plus a learner
    search phrase (日本語の解説付きで中国語を学びたい人におすすめ).
    Every named topic cross-checked against the zh-tw core's actual
    content — all present: 香港金融科技週, 台灣國際旅展, 味全龍, 立冬,
    福隆, 鋼鐵 (高雄鉄彫刻祭), 天母, 雙11. No topic outside the core.
18. **Change-scope check — PASS.** Against the builder's pre-fix Gate 10
    render (`build/gate10/edition/`): only P5/P8 SVGs and cards differ;
    the other 6 SVGs and cards are byte-identical. New pins match the KIT
    §16 exactly: SVG p5 `326b641e72cc71c816345ab891457aa6cd3ba1edb97924461727307939fbb9e9`,
    SVG p8 `d0f58c06a5f7cb6b45f9a070932d06031e16d9449ae4192a6c647c0ddccedc1e`;
    cards p5 1,337,283 B, p8 1,291,502 B (pre-fix: 1,335,675 / 1,292,509);
    all other card bytes unchanged (1,131,378 / 1,270,402 / 1,072,967 /
    1,044,850 / 945,176 / 1,088,820). KIT doc corrections verified: §6 tag
    list corrected (gate 10); §16 p3 pin completed to its true 64-char hash
    `aa58b266ec10b54a19197f2ba8903a2dd742d920a1c3eb4d9661f4c3a0634ce4`
    (delivered file and Gate 10 replay agree); §2/§7/§16 numbers and pins
    updated to the fixed render (5992, P5 418 / P8 2499, print/web pins
    below); new §18 fix-round section present and accurate (its §18.1–18.2
    rewordings match the delivered SVGs node for node).

## PDF pins re-verified (delivered files, this round)

- Print `Lucerna-VOL2.pdf`: **17,606,366 bytes**, 8 pages,
  SHA-256 `2a65419a5a206153b2ca8926a6a81c03b3fa8e3a9a72afdf7617d0b62630e945`.
- Web `Lucerna-VOL2-web.pdf`: **3,309,173 bytes** (< 10 MB), 8 pages,
  SHA-256 `eebf0102e4ad37c39a90d50fce831842b4fcae9b2e22a02bcd7d44c5394b189f`.
- SVG SHA-256 (all 8 match builder KIT §16 exactly):
  p1 `dc36d99206915d076365d95826e664e73a5065b64bed90177d18a51b815eaac5`,
  p2 `45872bce8345bbaf8863e4ff3bd16df40ab069686bd51808826eff1bcc1437bd`,
  p3 `aa58b266ec10b54a19197f2ba8903a2dd742d920a1c3eb4d9661f4c3a0634ce4`,
  p4 `701bd92da8f101e3a8d8296bc468c90422d30a56027a35edd2e2275a13b749d1`,
  p5 `326b641e72cc71c816345ab891457aa6cd3ba1edb97924461727307939fbb9e9`,
  p6 `9970560b86c78ba1550985495910d203767ba8a77821099a27f590f7c91d2b29`,
  p7 `e07438a80eccc83423562bbd9155744e2533bdb7d6d077f24d8c78c687ffd9c3`,
  p8 `d0f58c06a5f7cb6b45f9a070932d06031e16d9449ae4192a6c647c0ddccedc1e`.
- Card PNGs: all 1950×2700, bytes per gate 18.

## Non-blocking observations (do NOT affect the verdict)

1. **Delivery PDF filename without -JA suffix: judged NON-BLOCKING**
   (unchanged from the first proof). `insert.py`'s `find_web_pdf` requires
   exactly 1 `*web*.pdf` (this dir has exactly 1) and copies it as
   `<slug>.pdf`, so the repo artifact is slug-named regardless.
2. **Brief BRICK-vs-OLIVE error** (gate 13): the edition is correct per
   shipped precedent; the brief was wrong.
3. **P1 gloss keeps the full formal venue name** (`香港コンベンション・
   アンド・エキシビション・センター`): this is a DIFFERENT string from the
   P8 key-2 note and was deliberately untouched by the fix — not an
   inconsistency, and it does not strand any kana (verified in the
   rendered P1 gloss nodes).
4. **Core's own P7 readers'-corner overflow** (core last line past its box
   border while auditing clean): context only for the core; the EDITION
   clears its border (gate 8).

## Limitations (stated honestly)

- Japanese was checked by full reading of every rendered string and by
  mechanical scans, not by a native speaker; no native-speaker review was
  available in this round.
- Commons credits were verified against the core KIT's binding
  adjudication and byte-identity of placed images, not by a fresh live
  Commons API query (the P4 provenance question is closed by the
  coordinator's 2026-10-27 ruling unless bytes or credit change — neither
  changed).
- One intermediate counting slip in this round (an unfiltered all-character
  set briefly reported as CJK counts) was caught and corrected before any
  conclusion: the corrected CJK-filtered counts are 1029/1288 with the
  identical 57-character outside list, and all adjudications above use the
  corrected extraction.
