# Independent proofread — W45 ZH-TW × JA (Traditional Chinese target · Japanese reader)

**Verdict: NOT PASS** — 2 blocking items (one defect class, two sites).
All other gates pass, including Gate 10 reproduction and Traditional independence.
The edition must NOT be inserted until the builder fixes the blocking items,
re-renders the full issue, and a fresh full proofread round returns zero problems
(SOP §8.4). Nothing here declares anything shipped.

**Slug:** `2026-w45-zh-tw-ja` · **Issue week:** Nov 2–8, 2026 · **Pages:** 8 ·
**Exercises:** 150 · **Proof dir:** `hidden_files/w45/zh-tw-ja-proof/`
(work files under `work/`; this report is the finalization evidence — negative).

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- (a) No live worker writing to the delivery/build dirs: the only Python process
  observed during the round was a sibling `zh-tw-pt` render (different dirs).
  No process touched `weekly-report-w45-zh-tw-ja/` or its build dir.
- (b) Two hash snapshots of both dirs (`work/snap2.txt`, `work/snap3.txt`):
  ZERO changes; every file mtime ≤ 09:31 UTC Oct 28 (builder finished 09:31).
- (c) Builder session completed: delivered run/render logs + Gate 10 logs all
  closed with exit 0 and registry 150.
- Pre-flight PASSED; the proof proceeded. No subagent was spawned, `weekly-git`
  was not touched, `insert.py` was not run, nothing was posted to Discord or
  main chat, no cron was created, no shared scratch dir was cleaned. No content
  module was ever imported inside the core build dir — all re-runs used fresh
  copies under `work/` only.

## Blocking items (2)

Both are the same defect class: a Japanese line starting with a small kana
(sutegana), which JIS kinsoku prohibits at a line head. The builder's claim
"kinsoku line-start 0/1425" holds only for punctuation closers; the column's
own W43 zh-tw-ja precedent scanned NO_START + small kana, found 2, and fixed
them before shipping (W43 KIT §8.1; W43 shipped SVGs re-scanned here: 0
small-kana starts on all 8 pages). This edition's renderer NO_START set does
not contain small kana, so these are not auto-prevented — they must be caught
by scan and fixed by rewording, exactly as W43 did. The builder's scan missed
them (no kinsoku section exists in its `verify.py` or `scans.py`).

### B1. P5 gloss line starts with small ィ

- File: `files/weekly-report-w45-zh-tw-ja/svg/p5-youth.svg`,
  node `<text x="83" y="1992.17" font-size="20.5">ィショー、毎日14時のマスコットパレー…</text>`.
- Previous line ends `…韓国のJUMPテコンドー・コメデ` — the loanword
  コメディショー is split with small ィ stranded at the line head.
  Visible on the P5 card in the travel-fair gloss box.
- Remedy: adjust the gloss sentence in `transform.py` (the fan-out source) so
  the wrap point moves — e.g. reword the `テコンドー・コメディショー` segment
  or shift the break — then full re-render and re-scan to 0 small-kana starts.

### B2. P8 key-2 note line starts with small ョ

- File: `files/weekly-report-w45-zh-tw-ja/svg/p8-test.svg`,
  node `<text x="65" y="1411.408" font-size="12.8">ョン・センターで開催。</text>`.
- Previous key line ends `…香港コンベンション・アンド・エキシビシ` — the
  loanword コンベンション is split with small ョ stranded at the line head.
  Visible on the P8 card in the keys column (key 2).
- Remedy: adjust the key-2 note in `transform.py` so the wrap point moves —
  e.g. shorten to a form such as `香港コンベンションセンターで開催。` — then
  full re-render and re-scan to 0 small-kana starts.

After either fix, the whole issue must be re-rendered and this proof round
repeated in full (including a fresh Gate 10 replay, since the transform changes).

## Per-gate evidence (all independently re-run, not taken from the builder KIT)

1. **Freeze baseline + target-text attribution — PASS (with the Japanese caveat).**
   `freeze.py baseline` on a fresh core-build copy: **8/8 byte-identical**,
   core prefixes match the core KIT exactly; shipped core SVGs re-hashed
   unchanged at the end of this round. `freeze.py diff --strict-cjk` displays
   STRICT-CJK FAIL with TOTAL added CJK **5993** (per page 395/342/414/353/
   415/431/1140/2503; counted strings +22/−22, +33/−35, +38/−38, +33/−33,
   +37/−40, +37/−37, +88/−90, +192/−191) — identical to the builder's numbers,
   and structurally inevitable for a Japanese explanation layer, NOT a failure.
   The correct close, re-derived with fresh code (`work/proof2.py`):
   **B1 = 0, B2 = 0** unattributed added/removed strings, and **0 suspicious
   pure-Hanzi added strings**. Zero FLOW OVERFLOW / HEAD TOO WIDE warnings in
   the delivered run and in my Gate 10 replay. Transform audit (AST over all
   280 `rep()` pairs + 6 repoints = 286 log lines, matching the gate log):
   no OpenCC, no mapping table, no conversion logic; every non-furniture
   Traditional run in an `old` string survives verbatim in its `new` string,
   except one adjudicated explanation-layer citation (P3 note
   `Lidong is a solar term (節氣).` → `立冬は節気の一つ。` — the Japanese note
   uses the Japanese form 節気; the target text itself is untouched, and the
   rendered attribution stays 0/0). The 3 furniture pairs (footer, page line,
   badge) replace Traditional furniture text with Japanese furniture per the
   W43 precedent, as intended.
2. **Traditional independence — PASS (hard gate).** Re-extracted: edition CJK
   set **1029**, union of (W43 zh-tw-ja + zh-tw core) **1288**, outside **57**
   — the exact list in the builder KIT §3. Every outside character was
   adjudicated individually: all 57 occur in Japanese explanation-layer nodes
   (kana, Japanese kanji usage, Japanese punctuation). Apparent exceptions
   resolved as wrapped-line artifacts of Japanese sentences, not target text:
   彫/国 in the P3 gloss line `解説 — 高雄国際鉄彫刻祭（10月23日～11…`
   (continuation line has kana); ／ in P7 `（立冬／進補）。` (continuation of
   a Japanese grouping sentence); ～ in P8 key notes 41/42 (Japanese
   day-count notes); 点 in P8 key 60 `1 + 5 = 合計6点。` (Japanese note).
   Simplified-only spot list over frozen shared strings: **0 hits**. Over ALL
   edition strings the hits are only 国/学/点, every occurrence in
   Japanese-layer nodes (badge/footer/gloss/notes; the single non-kana-line
   occurrences are the wrapped-line cases above). Shinjitai inside the
   Japanese layer (e.g. 国, 学) is not a violation; no Simplified-form
   character occurs in Traditional target text. No conversion/OpenCC/mapping
   logic in the transform (verified by source read + grep).
3. **Target text zero difference — PASS.** Rendered-string attribution B1/B2
   = 0 (gate 1); registry keys identical 150/150 (gate 5); all 8 golden
   sentences verbatim from the core (gate 9); image payloads byte-identical
   (gate 10); readers'-corner Traditional letter + disclosure line-for-line
   identical (gate 11).
4. **Gate 10 reproduction — PASS (mandatory, blocking-class gate).** Fresh copy
   of the core build dir + the builder's `transform.py` ALONE, one-process
   driver (`run.py` → `render.py`) in `work/gate10/`: transform exit 0
   (286 replacements, OUT/BASE wholly repointed to the proof edition dir, no
   reference to the real delivery dir left in the copy), run exit 0 with zero
   warnings and registry 150 (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/
   12/38; types 67/54/16/12/1), render exit 0. Result: **SVGs 8/8
   byte-identical** to delivered, **cards 8/8 byte-identical**, print PDF
   byte-identical. No stray nested tree: the delivery dir contains only
   `svg/` + `cards/` + PDFs + ABSTRACT.txt + WEEKLY-KIT.md; the build dir's
   `gate10/` subtree is the builder's own documented Gate 10 run
   (build-copy + edition), not an inherited es template; no es-template
   reference exists in the transform or driver.
5. **P8 — PASS.** Default-form invocation (tables.json zh-tw `p8_file` is
   `p8-test.svg`, so no explicit-path form was needed):
   `p8.py compare --core-dir …/weekly-report-w45-zhtw-core --edition-dir
   …/weekly-report-w45-zh-tw-ja --target zh-tw` → **CLEAN, 150=150,
   missing=[], extra_count=0, keydiff=[]**. `p8.py extract` on the delivered
   P8: noted set **150/150**, parse lines (dash style). Registry dumps from
   fresh one-process runs of core copy vs transformed copy (`work/reg_core.json`,
   `work/reg_ed.json`): keys **0 diffs**, level/page/type **0 diffs**; notes
   differ on all 150 by English→Japanese translation (the fan-out's purpose);
   writing item 150 key `(開放題,範文如下)` identical, note translated like
   all others. (Note on the task's "writing-item change only" phrasing: the
   observed registry diff is keys-identical + all-notes-translated; the
   writing item differs from the other 149 only in its printed ✓ form on P8,
   which `p8.py compare` already adjudicates CLEAN. The substantive gate —
   keys identical, noted set 150/150 — passes.)
6. **P8 dash style + AI-variant trap — PASS.** Dash verified from the W43
   zh-tw-ja build code itself (`content8.py`: `f"{n}. {key} — {note}"`,
   writing `f"{n}. ✓ {note}"`) and from shipped W43 P8 key lines
   (`148. A — …`, `150. ✓ 開放課題 — …`); this edition's code and shipped
   key lines match (dash; separators `— N ページ —` at the W45 core metrics
   12.8pt/lh 1.12/gap 1, vs W43's 13.3/1.16/2 — a deliberate no-reflow choice,
   not a defect). Kinsoku punctuation line-starts 0, stray ASCII apostrophes
   **0** (core: 26, all in replaced English notes). AI forms, all verified in
   the final render: P6 gloss `AI＋（銀行・投資・保険の中のAI）` (avoids
   coining 人工知能); P6 note `AIはデータを見て、リスクを見つけ、顧客の質問に
   答える手伝いをする。` (fully Japanese); P8-key note `金融の中のAIは人工智慧＋。`
   (verbatim target term kept). Adjudication against THIS column: W43
   zh-tw-ja has no AI precedent (grep over its build sources: no AI string),
   so no column rule exists to import; keeping the verbatim term in the
   P8-key note is correct because the term IS the key (a Japanese rendering
   would break key–note correspondence), and it introduces no new target CJK
   (the term already occurs in the core's key and P6 article). The zh-tw-it
   pinyin-only rule and zh-tw-es/pt verbatim rules were NOT imported.
   Target-text attribution stays clean (gate 1).
7. **Occlusion + geometry — PASS except the kinsoku items in §Blocking.**
   `occlusion_audit.py --selftest` OK; edition **0 flags**, core **0 flags**,
   NEW vs core **0**. Same-baseline ink-collision scan (builder `scans.py`,
   re-run from a proof copy): edition **0**, core **0**. P4/P6 chart-label
   graze: **0/0**. Border-strike: **0/0**. The two first-render BOXTITLE
   fixes hold in the transform AND the final render (P2 you-line shortened;
   P7 disclosure shortened + box pad 26→42). **P7 letter-box direct
   measurement (mandatory):** SVG — box (1450.3, 1184.16)–(1885.7, 1762.06),
   last disclosure ink bottom 1753.63 → **8.43px clearance, fully inside**;
   card pixels — bottom border row 1761, last ink row 1752 → **9px
   clearance, fully inside**. (Core context only: core's own last line
   1756.38 vs its box bottom 1746.06 = 10.32px overflow while auditing clean
   — the known audit blind spot; the EDITION clears its border, as required.)
   P7 teaser: rect bottom **2559.36**, **20.64px** clear of the 2580 rule,
   last ink **2528.11** (SVG; card dark-rect rows through 2558 confirm).
   P8 keys end ink bottom **2538.1** (last nodes keys 40/81/121), clear of the
   footer rule.
8. **Gloss/match/registry — PASS.** Gloss calls in core sources = edition
   sources = 12 (content12 4, content34 5, content56 3, content7/8 0);
   rendered gloss boxes per page core = edition = 2/2/3/2/2/1/0/0; no core
   gloss string contains `·`, so items = calls = 12 (NOT zh-cn's 33). Match
   instr occurrences core = edition = 4 sets; registry 配對 = 16 (4×4).
   Registry 150 (A2 44 / B1 74 / B2 32; pages 10/18/18/18/18/18/12/38; types
   67/54/16/12/1; writing model verbatim — MODELO text identical in core and
   edition sources, label only changed).
9. **P7 golden sentences — PASS; KIT tag-list typo (non-blocking).** The 8
   sentences in the edition's `content7.py` quotes list are IDENTICAL to the
   core's list, sentence by sentence, with identical tags: p. 1, p. 1, p. 2,
   p. 3, p. 3, p. 4, p. 5, p. 6 (distribution (p. 1)×2, (p. 2)×1, (p. 3)×2,
   (p. 4)×1, (p. 5)×1, (p. 6)×1 — matching every other zh-tw sibling and the
   rendered tags on both the core and edition P7). Each sentence counts
   exactly **2× issue-wide** in both the core and the edition after
   punctuation normalisation (article + P7; the P7 quote uses full-width ，
   where the article uses half-width ,). The builder KIT §6's trailing phrase
   "matching the core's p. 1/2/3/3/4/5/6/6" contradicts its own preceding
   distribution and the shipped tags; it is a KIT typo, NOT an edition
   deviation — the edition preserves the core's P7 sentences exactly, so
   neither the verbatim-from-this-issue's-articles gate nor the core-fidelity
   gate is broken. The 3 error-clinic 「…」 lines count 1× each, as expected.
10. **Images — PASS.** Per-page payload hashes byte-identical core vs edition:
    p1 `ac4dfe2ad3a43cd3` (harbour.jpg, Wilfredor, CC0), p2 `a40e7a2b265beba6`
    (rain.jpg, CorraleH, CC0), p3 none, p4 `18ad8ae06fac2860` (baseball.jpg,
    Bain News Service, Public domain), p5 `bcbada13a5ae19d6` (pumpkin.jpg,
    Benjamin Balazs, CC0), p6/p7/p8 none. Credit lines verbatim identical on
    all pages. P4 provenance NOT re-litigated: placed bytes and credit line
    are unchanged from the core, and the core KIT's 2026-10-27 binding
    adjudication (CLOSED) is respected.
11. **Readers' corner — PASS.** Traditional letter (4 wrapped nodes) and
    Traditional disclosure (5 wrapped nodes) line-for-line identical to the
    core. Japanese disclosure (6 nodes) states no genuine letters exist
    (`本物の投書ではない`, `掲載できる投書がなく`) and ends with the verbatim
    open invitation `あなたの手紙を次号でお待ちしています。`, mirroring the
    core lt2 closing `你的來信，下一期見`. The W43 precedent's forward-promise
    form (`VOL.2では…掲載する！`) correctly does NOT apply here because the
    W45 core's disclosure is a deferral, not a promise; the W45 Japanese form
    adapts to the deferral.
12. **Furniture three-way — PASS; brief error (non-blocking).** Badge measured
    on all three P1s: core, W43 zh-tw-ja, and this edition are ALL
    x=975, y=378, 21pt, weight 700, fill **#3e4c2a (OLIVE)**, with this
    edition's badge text identical to W43's
    (`中国語（繁体字）テキスト · 日本語の解説 — 日本語読者のための版`).
    The task brief's BRICK #a4553a claim is wrong against BOTH shipped
    references; the edition's OLIVE follows shipped precedent and is correct
    — recorded as a non-blocking brief error, NOT an edition defect.
    (tables.json was not edited.) Footer: VOL.2-adapted Japanese form
    (`Lucerna · 中国語（繁体字）週刊 VOL.2 · 本文は中国語（繁体字） · 解説は日本語`)
    on all 8 pages; page lines `N ページ（全 8 ページ）` identical to W43;
    gloss prefix `解説 — ` identical to W43; P8 header, right header, band,
    band sub, and separators identical to W43 (separator metrics per gate 6).
    svglib byte-identical across core, edition, and W43
    (md5 `a269e147529bcb0a1f2dd3aa22fa5658`).
13. **Residual Latin rendered sweep — PASS.** Full sweep of all edition text
    nodes re-run independently. Every Latin-containing node is adjudicated:
    masthead/band/footer `Lucerna`; frozen edition line (VOL.2, dates);
    Japanese bylines retaining `FAQ`, `TSNA`; frozen article proper names
    (`StartmeupHK`, `Fintech Nexus: Bridging the World, Building the Future`,
    `ITF`, `SUPER STAGE`, `SOLID TIDES`, `Trick or Treat`, `JUMP`, `MVP`);
    Japanese gloss citations (`StartmeupHK`, `ITF`, `JUMP`, `MVP（最優秀選手）`);
    photo credits (`Photo: … — CC0 / Public domain (Wikimedia Commons)`);
    P7 `VOL.1` (frozen + Japanese disclosure) and teaser `次号予告（VOL.3）`;
    P8-note abbreviations `AI`, `MVP`, `SNS`; P7 tags `(p. N)`; P8 key
    letters. No English explanation prose remains. `算一算 · 計算してみよう`
    present on P2, P3, and P5 (1 node each); `Work it out` = 0 and every other
    English head (`Did you get it`, `Over to you`, `Quick quiz`, `Headline
    words`, `This week`, `Word of the week`, `Practice example`, `Read the
    chart`, `Deep-read quiz`, `True or false`, `The big quiz`, `Read and
    answer`, `Say it in context`, `Test & keys`, `Language focus`, `Fill in`)
    = 0. The P3 head was additionally confirmed visually on the P3 card.
14. **Web regen — PASS.** Gate 10 replay: cards **8/8 byte-identical**, print
    PDF **byte-identical** (sha matches delivered), web PDF
    **content-identical**: same size 3,308,957, 8 pages, all 8 page-image
    hashes identical, only **6 bytes differ**, all inside the
    CreationDate/ModDate timestamps (replay 09:39 vs delivered 09:22) — the
    timestamp exception, stated explicitly as required.
15. **Eyeball all 8 cards — PASS except the blocking kinsoku items.** Layout
    clean on all pages: no overflow, no overlap, no missing content, no footer
    collision, images/credits placed correctly, Japanese typesets correctly on
    the TC face, no missing-glyph boxes. Punctuation kinsoku line-starts 0,
    line-end openers 0, ー-starts 0, stray ASCII apostrophes 0. The two
    small-kana line starts (B1, B2) are visible in the render and are the
    only eyeball defects.
16. **ABSTRACT.txt — PASS.** Single line (one trailing newline, no ASCII double
    quotes), in Japanese, naming: Lucerna, 中国語（繁体字）, VOL.2, 11月2日～8日,
    A2～B2, 全150問, plus a learner search phrase
    (日本語の解説付きで中国語を学びたい人におすすめ). Every named topic
    cross-checked against the zh-tw core's actual content — all present:
    香港フィンテックウィーク (P1), 台北国際旅展 (P1), 味全龍の台湾シリーズ制覇
    (P4), 立冬と温泉・ハイキング (P2), 福隆サンドアート (P3), 高雄鉄彫刻祭 (P3),
    天母ハロウィーンと旅展攻略 (P5), ダブルイレブンの賢い買い方 (P2/P5).
    No topic outside the core.

## PDF pins re-verified (delivered files, this round)

- Print `Lucerna-VOL2.pdf`: **17,606,181 bytes**, 8 pages,
  SHA-256 `01b6a875f1fef45b173ec4543e515b9b40f5ca420765b6417e7f64aed635d9b7`.
- Web `Lucerna-VOL2-web.pdf`: **3,308,957 bytes** (< 10 MB), 8 pages,
  SHA-256 `b155a15cc7b16bf48213decce35e0890f21b5b84631a796b0dbc1fcfb96d3ad6`.
- Card PNGs: all 1950×2700, bytes match the builder KIT §16
  (1,131,378 / 1,270,402 / 1,072,967 / 1,044,850 / 1,335,675 / 945,176 /
  1,088,820 / 1,292,509).
- SVG SHA-256: 7 of 8 match the builder KIT §16 exactly; see the p3 note below.

## Non-blocking observations (do NOT affect the verdict)

1. **KIT §16 p3 pin is truncated (documentation typo).** The KIT prints a
   63-character hash for `p3-culture.svg`; a SHA-256 is 64 characters. The
   delivered file (and the Gate 10 replay file, byte-identical to it) hashes
   to `aa58b266ec10b54a19197f2ba8903a2dd742d920a1c3eb4d9661f4c3a0634ce4`
   — i.e. the KIT string plus a trailing `4`. The file is consistent; only
   the KIT string needs the missing character. The coordinator inserts from
   measured pins, so this does not block.
2. **KIT §6 tag-list typo** (see gate 9): the trailing `p. 1/2/3/3/4/5/6/6`
   contradicts the KIT's own distribution and the shipped tags; the edition
   itself is correct.
3. **Delivery PDF filename without -JA suffix: judged NON-BLOCKING.** The
   print PDF is named `Lucerna-VOL2.pdf` (the zh-tw core's own filename,
   kept as-is) while siblings renamed to `-XX`. Verified from `insert.py`
   (`find_web_pdf` aborts unless exactly 1 `*web*.pdf` exists — this dir has
   exactly 1 — and copies the web PDF as `<slug>.pdf`), so the repo artifact
   is slug-named regardless of the delivery-dir filename. Nothing was renamed
   by this proofread.
4. **Brief BRICK-vs-OLIVE error** (see gate 12): the edition is correct per
   shipped precedent; the brief was wrong.
5. **Core's own P7 readers'-corner overflow** (see gate 7): context only for
   the core; the edition clears its border.
6. **My first attribution run showed 3 unattributed added strings; resolved
   as a norm artifact** (missing `{NCHARS}`→138 substitution and MODELO-label
   stripping in my first script). The corrected run gives B1/B2 = 0, matching
   the builder. Recorded here so the intermediate number is not mistaken for
   a finding.

## Limitations (stated honestly)

- Japanese was checked by full reading of every rendered string and by
  mechanical scans, not by a native speaker; no native-speaker review was
  available in this round.
- Commons credits were verified against the core KIT's binding adjudication
  and byte-identity of placed images, not by a fresh live Commons API query
  (the P4 provenance question is closed by the coordinator's 2026-10-27
  ruling unless bytes or credit change — neither changed).
- The builder's kinsoku scan methodology is undocumented in the build dir
  (no kinsoku section in `verify.py`/`scans.py`); the 0/1425 punctuation claim
  was reproduced, and the small-kana finding comes from this proofread's own
  scan (same 1425 nodes, W43 precedent set), confirmed visually on the cards.
