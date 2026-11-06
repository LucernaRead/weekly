# Independent proofread — W45 zh-CN × ES (Simplified Chinese target · Spanish reader)

**Verdict: NOT PASS — one blocking item (Gate 10, transform-solo reproduction).
The delivered edition itself passes every content, geometry, furniture,
registry, image, readers'-corner, PDF and visual gate below; it is NOT
finalized because Gate 10 fails as specified, and the task states
reproduction failure is BLOCKING. Do NOT declare this edition shipped —
the coordinator inserts it only after the blocking item is closed.**

- Edition: `files/weekly-report-w45-zh-cn-es/` — svg ×8, cards ×8,
  print `Lucerna-VOL2-ES.pdf`, web `Lucerna-VOL2-ES-web.pdf`,
  `WEEKLY-KIT.md`, `ABSTRACT.txt` (Spanish, single line).
- Core: `files/weekly-report-w45-zhcn-core/` (zh-cn × en, VOL.2).
  W43 same-pairing reference: `files/weekly-report-zh-cn-es/`.
- Proofreader scratch (all work here, nothing else written):
  `hidden_files/w45/zh-cn-es-proof/work/`.
- Toolchain: `tools/venv/bin/python` throughout (Python 3.12.3).
- Delivery dir and core SVGs re-hashed at the end of this proof:
  identical to the pre-proof snapshot — this proof wrote nothing to the
  delivery dir, the core, the build dirs, `tools/`, or `weekly-git`.
  No subagent was spawned; no Discord/main-chat delivery; no insert.py;
  no cron; no shared scratch cleaned.

## Pre-flight (duplicate / moving-target check)

- At task start (2026-10-28 07:30 UTC) the delivery dir showed writes
  07:12–07:24 UTC (builder finalization: SVGs, cards, PDFs, ABSTRACT,
  WEEKLY-KIT). No process was writing to any ES dir — the only live
  workers found were rendering a *different* pairing
  (`weekly-report-w45-zh-cn-pt-build`), which touches no ES path.
- Stability check: SHA-256 snapshot of all delivered SVGs/cards/PDFs,
  then a 3-minute wait and re-hash — all hashes unchanged. The recent
  mtimes were builder completion immediately before handoff, not a live
  worker, so proof proceeded (standing down on any sub-30-minute mtime
  would have meant never proofing a just-finished build). This reasoning
  is recorded here rather than hidden.

## Blocking list (1 item)

### B1 — Gate 10: transform.py alone does NOT reproduce the delivered SVGs (5/8, not 8/8)

Procedure (all inside proof scratch): fresh copy of the zh-cn core build
→ copy of the ES build's `transform.py` into it → run `transform.py`
alone → repoint the copy's `OUT` paths (expanduser form) to proof
scratch → run the single-process driver (`run.py`, sections in order:
content12 → 34 → 56 → 7 → 8) → SHA-256-compare the 8 produced SVGs
against the delivered SVGs.

Results:

- `transform.py` exits 1: **315/319 replacements, 4 MISSES**.
  Three misses are benign (see below); one is a real translation gap.
- SVG comparison: **P1–P5 byte-identical; P6, P7, P8 DIFFER.**
  - P6: `f91f656d5727…` (repro) vs `d26244db1229…` (delivered).
    Text diff +1/−1 string: the repro head is
    `C · 练习篮子算一算 · Cuentas de cestas` (transform.py line 50);
    delivered is `C · 练习篮子算一算 · Cuentas`.
    Repro driver prints `!! HEAD TOO WIDE [P6-ex]` — the exact
    build-es-1 pre-fix defect.
  - P7: `f582fddf048b…` vs `1fd7c5999928…`. Text diff +4/−4 strings.
    The repro P7 still contains English frame text (see B1-c).
  - P8: `20fb7b2b24e…` vs `d6c9bb95b56…`. Text diff +19/−36 strings
    (re-wrapped key lines from shortened notes). Repro driver prints
    4× `!! FLOW OVERFLOW [P8-keys]` with keys flow ending y=2585
    (past the 2540 bottom) — the exact build-es-1 pre-fix defect.
    Delivered build-es-3 ends y=2411.
- B1-a — The 21 post-transform manual edits (full diff saved at
  `work/manual-edits-diff.txt`; counts exclude the `OUT` line):
  content12 ×6, content34 ×3, content56 ×5, content7 ×3, content8 ×4.
  By kind: 1× P6 head shortening (content56:217); 1× P7 frame-text
  translation (content7:80, see B1-c); 18× P8-note shortenings /
  rewordings (including the 2 pinyin rewordings, content56:75 and :89);
  1× P8-note translation completion (content8:62, see B1-c).
  The builder's KIT §9 documents the head shortening, the 18 P8-note
  tightenings and the pinyin rewordings as fix rounds, but those edits
  were never folded back into `transform.py`.
- B1-b — The 4 transform MISSES, adjudicated individually:
  - `content12.py: "Lucerna editors · Reading level B1"` — benign:
    the core has no B1 byline on P1/P2 (only A2).
  - `content56.py: "Lucerna editors · Reading level A2"` — benign:
    the core has no A2 byline on P5/P6 (only B1/B2).
  - `content34.py: "Lucerna editors · Reading level A2→B1"` — benign:
    already translated by the earlier loop replacement, whose old
    string is a substring of this one
    (`…Reading level A2` inside `…Reading level A2→B1`); the delivered
    byline `Redacción Lucerna · Nivel de lectura A2→B1` is correct.
  - `content8.py: "shùzì — the film's characters are digital images."`
    — REAL GAP (see B1-c). The core's content8 note is
    `shùzì — the AI film's characters are digital images.` (with
    "AI"); the transform old string (without "AI") matches only the
    content56 note, so the content8 note was never translated by
    transform.py and was fixed by hand in the ES build.
- B1-c — English residue in the transform-alone output (absent from
  the delivered edition):
  - Repro P7 contains the untranslated frame sentence
    `(First check the reviews, then order.) The frame 先…再… gives the
    order of actions. More: …` — delivered P7 correctly prints the
    Spanish version
    `(Primero mira las reseñas y luego pide.) El marco 先…再… da el
    orden de las acciones. Más: …` (verified on the P7 card).
  - Repro P8 key 135 note is
    `shùzì — the AI film's characters are digital images.` — delivered
    P8 key 135 correctly prints
    `shùzì — personajes digitales en la película con IA.`
- B1-d — What this does and does not mean. The delivered edition is
  reproducible from the *final* ES build files: a repointed copy of
  `hidden_files/weekly-report-w45-zh-cn-es-build/` reproduces all 8
  delivered SVGs byte-for-byte (verified, see Gate 10 note). The failure
  is specifically that `transform.py` — the script presented as the
  explanation-layer transform — is a pre-fix script (it reproduces
  build-es-1, warnings included), so a future rebuild from core +
  transform.py alone would ship the P6 overflow, the P8 overflow, and
  English on P7/P8. That is why Gate 10 is blocking even though the
  delivered files are clean.
- Required closure (for the coordinator/builder; NOT done by this
  proofreader): fold all 21 edits into `transform.py` (fix the
  content8 shùzì old string to include "AI", add the content7 wt
  translation, the head shortening, and the 18 P8-note shortenings /
  rewordings), then re-run Gate 10 to 8/8 and confirm the regenerated
  SVGs equal the delivered SVGs. If that regeneration is byte-identical
  to the delivered files, this report's content gates stand as-is and
  only Gate 10 needs re-running; any content change requires a fresh
  full proofread round per SOP §8.4.

## Per-gate evidence (all other gates PASS)

### Gate 1 — freeze baseline 8/8 + freeze diff (PASS)

- `tools/freeze.py baseline --build ../hidden_files/weekly-report-w45-zhcn-build
  --core-svg ../files/weekly-report-w45-zhcn-core/svg
  --out work/baseline-zhcn` → **8/8 SVGs byte-identical**; core
  integrity: shipped core SVGs unchanged by the run. Hashes match the
  builder's KIT §4 exactly:
  p1 `e057bbfcdfcd6fca`, p2 `c87aa67eb6785a58`, p3 `d50f09e1a72b6fd3`,
  p4 `dd3b1b0fdc80627a`, p5 `c71ef3153d70701c`, p6 `b06a85d276db8a53`,
  p7 `f2319cb8997f8d36`, p8 `eaf368f8dca48dff` (12-hex prefixes;
  full hashes in `work/freeze-baseline.log`).
- `tools/freeze.py diff --strict-cjk` (core vs edition, saved
  `work/freeze-diff.json`) → per page +/− strings and CJK, identical
  to the builder's KIT §5: P1 +50/−46 (851→815), P2 +64/−60 (1053→1031),
  P3 +38/−38 (812→790), P4 +41/−41 (810→789), P5 +42/−41 (944→922),
  P6 +40/−38 (1005→983), P7 +91/−88 (760→652), P8 +198/−198 (1102→1082);
  **added CJK = 0 on all 8 pages, TOTAL 0, exit 0.** No added CJK
  remains to adjudicate; removals are explanation-layer only
  (furniture, the P7 disclosure rewrite, Chinese words inside core
  English notes replaced by pinyin/Spanish). Simplified Chinese target
  text is unchanged.

### Gate 2 — p8.py compare + P8 style (PASS)

- `tools/p8.py compare --core-dir ../files/weekly-report-w45-zhcn-core
  --edition-dir ../files/weekly-report-w45-zh-cn-es --target zh-cn` →
  **CLEAN: core 150 noted, edition 150 noted, missing=[] extra_count=0,
  uncertain=[], keydiff=[]** (saved `work/p8-compare.json`). SHORT
  does not occur.
- Style verified from the core's shipped build code, never from memory:
  core `content8.py` lines 119/121 are
  `txt = f"{e_['n']}. {e_['key']} — {e_['note']}"` and
  `txt = f"{e_['n']}. ✓ {e_['note']}"` (dash style); the edition's
  `content8.py` lines 119/121 are byte-identical. The W43 same-pairing
  paren style belongs to the VOL.1 core family and was correctly NOT
  carried over (dash-family rule, tools README #8). Delivered P8 card
  confirms dash rendering (`1. 10 — …`, `150. ✓ Pregunta abierta — …`).
- `keylines.py` rerun (core vs edition P8): keys 150=150, **0 keys with
  more lines in the edition, 0 total extra lines** — the 18 tightened
  notes wrap no worse than the core. Spot-check: keys 68 and 74
  (pinyin notes) each wrap to exactly 1 line:
  `68. B — La nueva película se estrena en lìdōng, 7 de noviembre.`
  and `74. 立冬 — lìdōng — estreno de la nueva película.`

### Gate 3 — occlusion audit + ink-collision + P6 chart-label (PASS)

- `tools/occlusion_audit.py --selftest` → OK (all 6 planted classes
  fire exactly once; clean controls silent).
- `tools/occlusion_audit.py ../files/weekly-report-w45-zh-cn-es` →
  **0 flags, exit 0** (saved `work/occlusion.json`).
- With `--core ../files/weekly-report-w45-zhcn-core/svg` →
  **core 0 flags; NEW vs core: 0** (saved `work/occlusion-core.json`).
- Independent same-baseline ink-collision scan (own script
  `work/myproof.py`, PIL true-ink boxes, SC face, all pages, all text
  nodes, gap < 2 flagged; builder's `checks.py` rerun as cross-check):
  **0 flags** on both runs, including the P1 top band (3 nodes at
  y=92: VOL. 2 · 第 2 号 / top strip / date; masthead `Lucerna` at
  y=262) and the P1 badge line.
- P6 element-level chart-label coverage (text ink vs every later-drawn
  rect, any overlap reported, not just ≥30%): **0 texts with any
  later-rect ink overlap.** Bars verified in SVG rects: widths
  810/537/480 px at x=325, y=1282/1340/1398 (3.0 px/yuan for
  270/179/160 yuan); row-label ink ends x ≤ 206; value labels at
  x=1151/878/821 (= bar end + 16). P6 card confirms all three value
  labels fully visible and unclipped.
- P8 top-rule proximity (inherited from the core, unchanged): rule
  line y=1264 (x 65→1885) in both core and edition; last test-flow
  baseline y=1232.7 in both (builder's "flow ends y=1262" is the cursor
  after the last line, i.e. baseline + line step, identical in both);
  keys-area max baseline y=2531.98 in both; all 8 P8 separator y
  positions identical to the core. Canonical audit silent; P8 card
  eyeballed clean (no text struck by the rule).

### Gate 4 — gloss counts (PASS)

Split on `·` itself (never on ` · `), verified two independent ways
(source `gloss()` strings in both builds, and rendered SVG gloss boxes
reconstructed from wrapped lines):

- Source: content12 [4,4,4], content34 [3,3,3], content56 [3,3,3,3],
  total 33, equal item by item core vs edition.
- Rendered (prefix `Nota — ` vs core `Notes｜`): P1 [4], P2 [4,4],
  P3 [3,3], P4 [3], P5 [3,3], P6 [3,3] — exactly the builder's claim,
  equal per page core vs edition.
- Gloss prefix in all rendered boxes is `Nota — ` (W43 same-pairing
  form), never the core's `Notes｜`.

### Gate 5 — P7 golden sentences (PASS, with a measurement note)

All 8 phrases are verbatim contiguous excerpts from this issue's own
articles with correct Spanish page tags. Counting method matters and is
stated here: raw-substring counting over SVG files undercounts, because
4 phrases wrap across text nodes in the article. Counting over
concatenated per-page text nodes (document order), each phrase occurs
exactly 1× on its claimed article page + 1× on P7 = 2× total, in both
core and edition:

| Phrase | Article page | P7 tag |
|---|---|---|
| 不用等11月11日 | P1 | (Página 1) |
| 下单就能发货 | P2 | (Página 2) |
| 先看结算页，再付款 | P2 | (Página 2) |
| 水开始结冰 | P3 | (Página 3) |
| 三场都输了 | P4 | (Página 4) |
| 小局一场没赢 | P4 | (Página 4) |
| 故事够不够好 | P5 | (Página 5) |
| 别以后，就现在 | P5 | (Página 5) |

P7 header states the phrases are textual, from this issue's articles
(`Frases de la semana (textuales, de los artículos de este número)`).
No adjudication inheritance was needed: the edition's frozen text was
verified against the edition's own SVGs, not assumed from the core.

### Gate 6 — images (PASS, with a corrected measurement)

- Image elements per page, edition = core: P1 1, P2 1, P3 2, P4 1,
  P5 1, P6 0, P7 0, P8 0 — **6 photos total**, placement geometry
  (x/y/w/h) identical to the core.
- Payload MD5 (embedded data URIs; note: the SVGs use plain `href=`,
  not `xlink:href=` — an early proof-script regex using `xlink:href`
  found zero payloads and was corrected; the figures below use the
  corrected `href` extraction): edition payloads byte-identical to the
  core per page AND to the asset files — locker `420c6150a831…`,
  valley `550e463b4ad93…`, frost `d0b015bc9da8…`, dumplings
  `e8d752779a4a…`, lanparty `6b8e90374bf6…`, popcorn `a903e35f1eb2…`.
- Credit lines (all 6, from the SVG text nodes): P1
  `Foto: Map hobby — CC0 (Wikimedia Commons)`; P2
  `Foto: Paul Gilmore — CC0 (Wikimedia Commons)`; P3
  `Foto: Gerda Arendt — CC0 (Wikimedia Commons)` and
  `Foto: Syced — CC0 (Wikimedia Commons)`; P4
  `Foto: Syced — CC0 (Wikimedia Commons)`; P5
  `Foto: Based5290 — Dominio público (Wikimedia Commons)`.
  Only the `Photo:` label became `Foto:` (popcorn: `Dominio público`);
  artist names identical to the core's. `assets/CREDITS.md` is
  byte-identical between the core build and the ES build
  (SHA-256 prefix `a03a3d26e5e8b624`, 1779 bytes). Live re-query of the
  Commons API was not possible in this subagent (no live browser);
  see Limitations.

### Gate 7 — readers' corner (PASS)

P7 corner, verified from the edition SVG nodes and the P7 card:

- Letter itself byte-identical to the core (3 nodes, y=1315.6/1346.1/
  1376.7): `「你好！我住在上海。立冬那天，我吃了饺子，也给妈妈打了电话。
  双11，我买了一件毛衣，现货第二天就到了。」`
- Disclosure in Spanish, labelled editor's example, stating no genuine
  letters exist and deferring the VOL.1 promise (`Aplazado, no
  cancelado`): `Ejemplo de la redacción, no una carta real. VOL.1
  prometió cartas reales y la mejor redacción de VOL.1 en VOL.2; no ha
  llegado ninguna carta real ni hay ningún texto publicable, así que
  este rincón sigue publicando un ejemplo de la redacción.`
- **Explicit open invitation, inside the corner itself** (not a teaser
  line, not another page's exercise prompt — the P2/P3/P5/P6 `¿Y tú?`
  prompts are separate and were not counted):
  `¡Envíanos tu carta en chino! Escribe dos frases sobre tu semana y la
  publicaremos aquí.` (joined across nodes y=1607.6/1636.0/1664.4;
  visible verbatim on the P7 card).
  A facts-only disclosure would have failed; this one passes both
  requirements.

### Gate 8 — furniture three-way + two adjudications (PASS)

Measured from shipped SVGs (core EN / W43 shipped zh-cn×es / this
edition), all pages where applicable:

| Furniture | Core (EN) | W43 shipped ES | This edition |
|---|---|---|---|
| P1 badge | (975, 434), 19.5pt, Chinese+English text | (975, 434), 19.5pt, `TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES` | W43 string verbatim, (975, 434), 19.5pt |
| Footer (all 8 pp) | `Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations` | `Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.1 · TEXTO EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL` | `Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.2 · TEXTO EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL` (VOL.2 follows the target core — justified pair-varying change) |
| Page line (all 8 pp) | `第 N 版 / 共 8 版` | `Página N de 8` | `Página N de 8` (all 8 verified) |
| Gloss prefix | `Notes｜` | `Nota — ` | `Nota — ` |
| P8 separators | `— Page N —` | `— Página N —` | `— Página N —` (all 8, sentence case) |
| P8 key style | dash | paren (VOL.1 family) | dash (own core's style; see Gate 2) |
| P8 header | `答案 · Answer keys — by page, with a note on every answer` / `All notes in English · ✓ = the writing task` | `答案 · Claves — por página, con una nota para cada respuesta` / `Todas las notas en español · ✓ = la tarea de escritura` | W43 strings verbatim (verified in SVG) |
| P1 strap | `简体中文版 · VOL.2 · 双11 · 立冬 · S16` | `SEMANARIO CHINO SIMPLIFICADO · VOL.1 · 双11 · 大闸蟹 · 霜降` | `SEMANARIO CHINO SIMPLIFICADO · VOL.2 · 双11 · 立冬 · S16` (VOL.2 + this issue's topics; Chinese topic words kept) |
| P1 strapline | `给学中文的人的周报 — Read the real China, in Chinese` | `给学中文的人的周报 — Lee la China real, en chino` | W43 second half verbatim |
| Top strip | `每周读中文 · Read real Chinese, every week` | `每周读中文 · Lee chino de verdad, cada semana` | W43 string verbatim |
| Photo credits | `Photo: … — CC0 / Public domain` | `Foto: … — CC0` | `Foto: … — CC0` (popcorn: `Dominio público`) |

- **Adjudication (a) — badge slot: RULED for the builder.** All three
  P1 badge nodes measure (975, 434), 19.5pt, centered: the core's own
  slot, the W43 shipped same-pairing slot, and this edition's slot are
  identical. The in-place replacement case applies (zh-cn core family);
  this is not the FR/IT insertion case (y=574, 22pt) nor the KO shift
  case. No masthead displacement; body strapline at y=372 untouched.
- **Adjudication (b) — P8 separator: RULED for the builder; shipped
  wins.** The W43 shipped same-pairing SVG prints `— Página N —`
  (verified on all 8 separators in `weekly-report-zh-cn-es/svg/
  p8-ceyan.svg`); this edition follows the shipped form.
  `tools/tables.json` lists the es p8_separator as all-caps
  `— PÁGINA {n} —`, which contradicts the shipped artifact.
  **tables.json was NOT edited** (per the brief: shipped wins; do not
  force the wrong form by editing the table). Discrepancy recorded
  here for the parent line to fold in. This edition contains zero
  occurrences of all-caps `PÁGINA`.
- Masthead: bare `Lucerna` (blackletter, y=262); `The Lucerna` 0,
  `Le Lucerna` 0 in the delivered SVGs (Chinese is article-less per
  the SOP).

### Gate 9 — web PDF regeneration (PASS, with documented timestamp variance)

Procedure: copy of the delivered SVGs + the ES build's `render.py`
(BASE repointed to proof scratch `work/webregen`) run with the venv
Python.

- Cards regenerated 8/8 **byte-identical** to the delivered cards.
- Print PDF regenerated **byte-identical**: 50,133,157 bytes,
  SHA-256 `e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46`
  = KIT pin, 8 pages.
- Web PDF regenerated: 8 pages, **3,242,033 bytes (< 10 MB)** = KIT
  size; SHA-256 `abc0cb99cb9445fe1231597747021cac556723cb0b4c3263daa712ecfb8c2e1c`
  vs delivered/KIT pin `0ee7547e5d24a835cb349a4037fa94adf279c3350b73a26dacb414609baa573c`.
  Byte-diff of the two web PDFs: **exactly 8 differing bytes, all in
  the two timestamps** — `/CreationDate (D:20261028071904Z)` /
  `/ModDate (D:20261028071904Z)` (delivered) vs `…074323Z` (regen).
  Page count, page images, title metadata, and every other byte are
  identical. The delivered file's own size + SHA match the KIT pins
  exactly (verified in the pre-proof snapshot); the regen variance is
  a Pillow wall-clock timestamp, not a content difference. Adjudicated
  PASS on that basis, with the variance stated here rather than hidden.
- Delivered cards are all 1950×2700 RGB PNGs.

### Gate 10 — transform solo reproduction (FAIL — see Blocking list B1)

For completeness, the rest of Gate 10's evidence:

- Final ES build files DO reproduce the delivered SVGs: a repointed
  copy of `hidden_files/weekly-report-w45-zh-cn-es-build/` (OUT →
  proof scratch) run through the single-process driver produces all 8
  delivered SVGs byte-for-byte, with build-es-3 flow values
  (P7 teaser 2525.1, P8 keys 2411, zero warnings). So the edition is
  reproducible from its final build dir; only the transform-alone path
  fails.
- Registry (dumped by running the content modules in one process in
  each build copy; `work/reg-ed.json` vs `work/reg-core.json`):
  TOTAL 150, A2 56 / B1 69 / B2 25, pages 10/18/18/18/18/18/12/38,
  types 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1,
  writing model 172 characters — identical to the core registry.
  Key diffs: exactly one — #150, core `(开放题，范文如下)` →
  edition `(pregunta abierta — modelo a continuación)`.
  All other 149 keys byte-identical; level/page/type identical for
  all 150; all 150 notes differ (translation, expected).
  Key #150 is registry-only and invisible on paper: the delivered P8
  prints `150. ✓ Pregunta abierta — el modelo está en la sección F de
  esta página, 172 caracteres` (no apparatus text as a key), matching
  the W43 precedent.
- Builder claims re-measured and confirmed (delivered edition):
  P7 teaser ends 2525.1 (core 2554.1), above the 2580 footer line
  (last teaser baseline 2491.1 vs core 2520.1); P7 col3 ends 1679.1
  (core 1708.1); P8 test flow ends y=1262 / keys flow ends y=2411
  (build-es-3 log; SVG geometry identical to core — see Gate 3);
  final render zero `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings
  (build-es-3 log; the transform-alone repro is the run that still
  shows warnings, see B1).
- P7 B1 glossline re-aim verified: edition P7 prints
  `Así, «el sábado por la tarde, 7 de noviembre» se convierte en
  11月7日星期六晚上.`; core prints
  `So English «Saturday evening, Nov 7» becomes 11月7日星期六晚上.`
  The Chinese result string `11月7日星期六晚上` is unchanged.
- P8 top-rule proximity inherited identically from the core (Gate 3).
- 18 tightened P8 notes kept facts/keys unchanged: p8.py keydiff=[]
  and keylines 0-worse (Gate 2); 立冬 pinyin citations verified
  (keys 68/74, 1 line each; strict-CJK added = 0).
- Number localization spot-check: P8 key 126 prints
  `1,192 millones de yuanes` (Spanish comma decimal for 1.192
  million); other figures unchanged (dates, times, scores, basket
  maths verified against the core registry and the P6 chart).

### Gate 11 — all 8 cards visual (PASS)

Every delivered card read in full (furniture, boxes, flows, answer
blocks, photos, credits, footers):

- P1: masthead, strap, strapline, badge, headline band, calendar,
  contents, word of the week, locker photo + credit, briefs, quick
  quiz — no overflow/overlap; footer clear.
- P2: gloss boxes, valley photo + credit, word cards, exercises
  11–28 — clean; footer clear.
- P3: frost + dumpling photos + credits, gloss boxes, exercises
  29–46 — clean; footer clear.
- P4: LAN-party photo + credit, schedule box, `Sina Sports` source
  line (proper noun, also present in the core), exercises 47–64 —
  clean; footer clear.
- P5: popcorn photo + `Dominio público` credit, gloss boxes,
  exercises 65–82 — clean; footer clear.
- P6: practice-data bar chart with all labels fully visible and
  unclipped, `Cuentas` head fitting its box, exercises 83–100 —
  clean; footer clear.
- P7: A2/B1/B2 columns, error clinic, frame (Spanish), readers'
  corner (disclosure + invitation, both visible), 8 phrases with
  correct `Página N` tags, VOL.3 teaser, footer clear.
- P8: test sections A–F, writing model, all 150 keys grouped by
  `— Página N —`, dash style, top rule clear of text, keys ending
  well above the footer — clean.
- Targeted English-residue scan over delivered SVG text: the only
  `Sport` hit is the proper-noun source name `Sina Sports` (1×, also
  in the core); `The Lucerna`/`Le Lucerna`/`— Page `/`Notes｜`/
  `Answer keys` and the other core English strings: 0.
- Weekday spot-check (Asia/Shanghai, `date -d`): 2026-11-02 Monday,
  2026-11-07 Saturday, 2026-11-08 Sunday, 2026-11-10 Tuesday,
  2026-11-11 Wednesday, 2026-11-15 Sunday — matching every Spanish
  weekday rendering in the edition.
- ABSTRACT.txt: single line (+ trailing newline), no ASCII double
  quotes, Spanish, names Lucerna, Simplified Chinese, the real topics
  (Doble 11 stock sales, Comienzo del Invierno Saturday 7 November,
  S16 quarter-finals, Sanxingdui Future Past AI film, We Only Have One
  Life), A2–B2, 150 preguntas, and a learner search phrase
  (`aprende chino leyendo noticias reales en chino`).

## Non-blocking observations (NOT blocking items — do not mix into B1)

1. Web PDF regen SHA differs from the KIT pin in exactly 8 timestamp
   bytes (Gate 9). Content-identical; no action needed unless the
   pipeline wants deterministic timestamps.
2. The ES build's `run.py` docstring says "Run the IT weekly build
   files…" — a copy artefact from another pairing's driver. It has no
   functional effect (it runs content12 → 34 → 56 → 7 → 8 in one
   process, as required) but is worth fixing on the next touch for
   hygiene.
3. Builder KIT §8's "English-residue 0" is correct under the targeted
   scan (only `Sina Sports`, a proper noun also in the core). A naive
   ASCII-word scan is not evidence here: Spanish words fragment under
   `[A-Za-z]+` tokenization (accents stripped), so it was discarded in
   favour of the targeted core-English-string scan.
4. The P8 "flow ends y=1262 / keys ends y=2411" figures are driver
   cursor values (last baseline + line step), not last baselines
   (1232.7 / column-dependent). Both match the core exactly; no
   discrepancy, just a measurement-definition note for future proofs.

## Limitations (stated plainly)

1. Image Commons Artist-field verification was NOT re-queried live:
   this subagent has no live browser, and the task's image gate is
   satisfied by payload identity + credit identity against the core
   (whose KIT records the 2026-10-27 Commons verification) + the
   identical `CREDITS.md`. If the coordinator wants a fresh Commons
   API check, that is a separate live-source task.
2. Trend/fact re-sourcing was NOT redone: the edition is a translation
   fan-out; freeze diff (added CJK 0) + registry identity prove no
   target fact, date, or figure changed from the core, so the core
   KIT's sourcing and honesty limits (17:52 source chain, S16
   2026-10-27 cutoff) are inherited, not independently re-verified.
3. Spanish was checked by full reading of extracted text and all 8
   cards, not by a native speaker; no Spanish grammar/spelling defect
   was found, but this proof cannot claim native-speaker authority.
4. The transform-repro copy's `render.py` still points at the core
   edition dir (it was never executed in this proof; only the content
   modules were run). It has no effect on any result above.
5. The builder's completion report beyond the KIT was not available to
   this proofreader as a separate document; builder claims were taken
   from the task brief + the edition KIT and verified independently
   item by item above — nothing was accepted on trust.

## Files produced by this proof

- `hidden_files/w45/zh-cn-es-proof/REPORT.md` (this report)
- `hidden_files/w45/zh-cn-es-proof/work/freeze-baseline.log`
- `hidden_files/w45/zh-cn-es-proof/work/freeze-diff.json`
- `hidden_files/w45/zh-cn-es-proof/work/freeze-diff.log`
- `hidden_files/w45/zh-cn-es-proof/work/p8-compare.json`
- `hidden_files/w45/zh-cn-es-proof/work/p8-compare.log`
- `hidden_files/w45/zh-cn-es-proof/work/occlusion-selftest.log`
- `hidden_files/w45/zh-cn-es-proof/work/occlusion.json`
- `hidden_files/w45/zh-cn-es-proof/work/occlusion-core.json`
- `hidden_files/w45/zh-cn-es-proof/work/occlusion.log`
- `hidden_files/w45/zh-cn-es-proof/work/occlusion-core.log`
- `hidden_files/w45/zh-cn-es-proof/work/myproof.py`
- `hidden_files/w45/zh-cn-es-proof/work/myproof-report.txt`
- `hidden_files/w45/zh-cn-es-proof/work/myproof-console.log`
- `hidden_files/w45/zh-cn-es-proof/work/builder-checks-rerun.log`
- `hidden_files/w45/zh-cn-es-proof/work/transform-repro/` (fresh core
  copy + transform.py alone + repointed driver run; repro SVGs)
- `hidden_files/w45/zh-cn-es-proof/work/transform-repro-run.log`
- `hidden_files/w45/zh-cn-es-proof/work/manual-edits-diff.txt`
- `hidden_files/w45/zh-cn-es-proof/work/repro-vs-delivered-diff.json`
- `hidden_files/w45/zh-cn-es-proof/work/webregen/` (regenerated cards
  + print/web PDFs from delivered SVGs)
- `hidden_files/w45/zh-cn-es-proof/work/webregen-run.log`
- `hidden_files/w45/zh-cn-es-proof/work/esbuild-copy/` (final ES build
  copy reproducing delivered SVGs 8/8)
- `hidden_files/w45/zh-cn-es-proof/work/reg-ed.json`
- `hidden_files/w45/zh-cn-es-proof/work/reg-core.json`
- `hidden_files/w45/zh-cn-es-proof/work/dump_reg.py`
- `hidden_files/w45/zh-cn-es-proof/work/baseline-zhcn/` (freeze
  baseline copy)

## PDF pins (delivered files, verified against the KIT)

- Print `Lucerna-VOL2-ES.pdf`: 50,133,157 bytes, 8 pages,
  SHA-256 `e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46`.
- Web `Lucerna-VOL2-ES-web.pdf`: 3,242,033 bytes (< 10 MB), 8 pages,
  SHA-256 `0ee7547e5d24a835cb349a4037fa94adf279c3350b73a26dacb414609baa573c`.
