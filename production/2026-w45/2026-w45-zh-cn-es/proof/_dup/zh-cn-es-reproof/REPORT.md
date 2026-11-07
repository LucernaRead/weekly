# Independent RE-proofread — W45 zh-CN × ES (Simplified Chinese target · Spanish reader)

**Verdict: PASS with ZERO PROBLEMS across all 14 gates, including Gate 10
with exit codes. This report is the finalization evidence for the
coordinator to insert; this proofreader does NOT declare the edition
shipped and performed no insert, Discord, main-chat, cron, or weekly-git
action.**

- Edition: `files/weekly-report-w45-zh-cn-es/` — svg ×8, cards ×8,
  print `Lucerna-VOL2-ES.pdf`, web `Lucerna-VOL2-ES-web.pdf`,
  `WEEKLY-KIT.md`, `ABSTRACT.txt` (Spanish, single line).
- Core: `files/weekly-report-w45-zhcn-core/` (zh-cn × en, VOL.2).
  W43 same-pairing reference: `files/weekly-report-zh-cn-es/`.
- Prior round: first proof (`hidden_files/w45/zh-cn-es-proof/REPORT.md`)
  was NOT PASS on Gate 10 only (transform-solo 5/8; 21 hand edits
  un-folded). Fix round 1 folded all 21 edits
  (`hidden_files/weekly-report-w45-zh-cn-es-build/FIX-LOG-GATE10.md`);
  micro-fix rounds 1+2 deleted the 3 remaining benign byline misses
  (`MICROFIX-LOG.md`, round 2 under explicit coordinator authorization).
- Reproof scratch (all work here, nothing else written):
  `hidden_files/w45/zh-cn-es-reproof/work/`.
- Toolchain: `tools/venv/bin/python` throughout (Python 3.12.3).
- No subagent was spawned. No content module was ever imported inside
  the CORE build dir — all executions used fresh copies with OUT
  repointed to reproof scratch (verified: core and edition OUT lines
  untouched afterwards; core SVGs re-hashed identical at close).

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER — intent, not the literal window)

- (a) No live worker writing to the ES delivery/build dirs: at
  snapshot time the only live workers were on other pairings
  (zh-cn-JA render, zh-cn-FR/PT/IT reproofs); `ps | grep zh-cn-es`
  = NONE at both snapshots.
- (b) Two mtime snapshots of both dirs ~3 minutes apart: `diff` =
  ZERO changes (`work/mtime1.txt` vs `work/mtime2.txt`).
- (c) Fix sessions completed: FIX-LOG-GATE10 filed ("FIX DONE, NOT
  finalized") and MICROFIX-LOG filed through round 2 ("MICRO-FIX
  ROUND 2 DONE, NOT finalized"). Proceeded.
- Delivery hashes at start matched every claimed pin exactly (see
  PDF pins below); closing re-hash identical — the delivery did not
  move during this round.

## Per-gate evidence (all independently re-verified, nothing copied from the first proof)

### Gate 1 — Pre-flight + delivery hash verification at start AND close (PASS)

- Start hashes (`work/delivery-hash-start.txt`) = close hashes
  (`work/delivery-hash-close.txt`): `diff` clean. 8 SVGs, 8 cards,
  both PDFs, ABSTRACT.txt — sizes + SHA-256 recorded in both files.
- Print: 50,133,157 B, SHA-256
  `e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46`.
- Web: 3,242,033 B (< 10 MB), SHA-256
  `0ee7547e5d24a835cb349a4037fa94adf279c3350b73a26dacb414609baa573c`.
- ABSTRACT.txt: SHA-256
  `e408c4825931773811c674e93e3b0474170f3ddca2c9ebae327afd74ee5c0b47`.

### Gate 2 (task Gate 10) — DOCUMENTATION CHAIN, the fixed item (PASS, rigorously)

Procedure (all inside reproof scratch): fresh copy of the zh-cn core
build → copy of the ES build's fixed `transform.py` + `run.py` into
it → OUT (expanduser form) repointed in the COPY's content files to
`work/gate10-out` → run `transform.py` alone → run the single-process
driver (`run.py`, content12 → 34 → 56 → 7 → 8) → SHA-256/cmp-compare
the 8 produced SVGs against the delivered SVGs.

- **Transform: 317/317 replacements, EXIT 0, zero MISS / FAILED**
  (`work/gate10-transform.log`: 317 `ok` lines, 0 `MISS` lines).
  The 318 denominator in the round-2 brief was arithmetic, not a
  gate: round 1 had 318 entries (317 hits + 1 miss); deleting exactly
  one entry leaves 317 entries, all hitting. 317/317 + exit 0 is the
  correct measured result and the gating condition is exit 0 — NOT
  failed on the denominator wording, per the brief.
- **Driver: exit 0, ZERO `HEAD TOO WIDE` / `FLOW OVERFLOW` warnings**,
  registry TOTAL 150 (A2 56 / B1 69 / B2 25; pages
  10/18/18/18/18/18/12/38; types 完成句子 68 / 单选 50 / 词汇配对 20 /
  完形单选 11 / 写作 1), P7 teaser ends **2525.1**, P7 col3 ends
  **1679.1**, P8 keys flow ends **y=2411** (bottom 2540) — all
  delivered values (`work/gate10-driver.log`).
- **SVG comparison: 8/8 byte-identical to the delivered SVGs**
  (cmp, all 8 pages).
- **Output-identity proof verified independently:** gate10
  `content34.py` line 16 reads exactly
  `f.byline("Redacción Lucerna · Nivel de lectura A2→B1")` — the
  loop A2 replacement produced exactly the deleted line's target
  string, as predicted. No `A2→B1` byline replacement line remains in
  transform.py (only the stale comment mention at lines 28–32, see
  Non-blocking observations).
- Transform-output content files are byte-identical to the delivered
  ES build content files except the repointed OUT line (line 6 only,
  verified per file by diff); `bslib4.py` identical modulo OUT.
- The 21 folded edits are present in transform.py and hit: P6 head
  `Cuentas`, P7 Spanish frame, 18 P8-note shortenings/rewordings
  incl. the 2 pinyin rewordings, and the content8 shùzì old string
  with "AI" (P8 key 135 on the delivered card reads
  `135. shùzì — personajes digitales en la película con IA.`).

### Gate 3 — Freeze baseline 8/8 + freeze diff strict-CJK added = 0 (PASS)

- `tools/freeze.py baseline` (`work/freeze-baseline.log`): **8/8 SVGs
  byte-identical**; core integrity: shipped core SVGs unchanged.
  Hashes match the builder's KIT §4 exactly: p1 `e057bbfcdfcd6fca`,
  p2 `c87aa67eb6785a58`, p3 `d50f09e1a72b6fd3`, p4 `dd3b1b0fdc80627a`,
  p5 `c71ef3153d70701c`, p6 `b06a85d276db8a53`, p7 `f2319cb8997f8d36`,
  p8 `eaf368f8dca48dff` (12-hex prefixes; full hashes re-verified
  at close).
- `tools/freeze.py diff --strict-cjk` (`work/freeze-diff.json`):
  P1 +50/−46 (851→815), P2 +64/−60 (1053→1031), P3 +38/−38 (812→790),
  P4 +41/−41 (810→789), P5 +42/−41 (944→922), P6 +40/−38 (1005→983),
  P7 +91/−88 (760→652), P8 +198/−198 (1102→1082); **added CJK = 0
  on all 8 pages, TOTAL 0, exit 0** — identical to the first proof
  and the KIT.

### Gate 4 — p8.py CLEAN + P8 dash style (PASS)

- `tools/p8.py compare --target zh-cn` (`work/p8.log`): **CLEAN:
  core 150 noted, edition 150 noted, missing=[] extra_count=0,
  uncertain=[], keydiff=[]**, exit 0.
- Dash style verified from the core's shipped build code: core
  `content8.py` lines 119/121 are
  `txt = f"{e_['n']}. {e_['key']} — {e_['note']}"` and
  `txt = f"{e_['n']}. ✓ {e_['note']}"`; the edition's lines 119/121
  are byte-identical. Delivered P8 card confirms dash rendering
  (`1. 10 — …`, `150. ✓ Pregunta abierta — …`).

### Gate 5 — Occlusion audit + same-baseline rowcheck + P6 chart-label (PASS)

- `tools/occlusion_audit.py --selftest` → OK (all 6 planted classes
  fire exactly once; clean controls silent).
- Edition audit → **0 flags, exit 0**; with
  `--core …/weekly-report-w45-zhcn-core/svg` → **core 0 flags; NEW
  vs core: 0** (`work/occlusion.log`, `work/occlusion.json`).
- Independent same-baseline ink scan (own script `work/rowcheck.py`,
  PIL true-ink boxes, SC face, all pages, all text nodes, gap < 2
  flagged): **0 flags** on all 8 pages, including the P1 top band
  (3 nodes at y=92; masthead `Lucerna` at y=262).
- P6 element-level chart-label coverage (text ink vs bar rects, 2D):
  **0 overlaps.** Bars verified in SVG rects: widths 810/537/480 px
  at x=325, y=1282/1340/1398; value labels at x=1151/878/821
  (= bar end + 16: `270 元` y=1310, `179 元` y=1368, `160 元`
  y=1426). P6 card confirms all three value labels fully visible
  and unclipped. (An early crude band-only check flagged 9
  x-overlaps; the proper 2D check shows all 9 are vertical misses —
  title/footnote rows above/below the bars — not coverage. The 2D
  result is the adjudicated one.)

### Gate 6 — Gloss counts split on `·` (PASS)

- Source `gloss()` strings, split on `·` itself: content12
  [4,4,4], content34 [3,3,3], content56 [3,3,3,3], **total 33**,
  equal item by item core vs edition (`work/gates6_11.log`).
- Rendered gloss boxes (`Nota — ` prefix vs core `Notes｜`): P1
  [1], P2 [2,1], P3 [1,1], P4 [1], P5 [1,2], P6 [1,1] — equal per
  page core vs edition. (Note: the first proof's rendered listing
  grouped P2/P3 differently by page in prose; the per-box lists
  above are the measured values and they match core exactly.)

### Gate 7 — P7 golden sentences (PASS)

All 8 phrases are verbatim contiguous excerpts from this issue's own
articles, counted over concatenated per-page text nodes (document
order): each occurs exactly 1× on its claimed article page + 1× on
P7 = 2× total, in both core and edition:

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

P7 header states the phrases are textual, from this issue's
articles (`Frases de la semana (textuales, de los artículos de este
número)`).

### Gate 8 — Images (PASS)

- Image elements per page, edition = core: P1 1, P2 1, P3 2, P4 1,
  P5 1, P6 0, P7 0, P8 0 — **6 photos total**, placement geometry
  (x/y/w/h) identical to the core.
- Payload MD5 (embedded data URIs, plain `href=`): edition payloads
  byte-identical to the core per page AND to the asset files —
  locker `420c6150a831…`, valley `550e463b4ad93…`, frost
  `d0b015bc9da8…`, dumplings `e8d752779a4a…`, lanparty
  `6b8e90374bf6…`, popcorn `a903e35f1eb2…`.
- Credit lines (all 6, from SVG text nodes): P1
  `Foto: Map hobby — CC0 (Wikimedia Commons)`; P2
  `Foto: Paul Gilmore — CC0 (Wikimedia Commons)`; P3
  `Foto: Gerda Arendt — CC0 (Wikimedia Commons)` and
  `Foto: Syced — CC0 (Wikimedia Commons)`; P4
  `Foto: Syced — CC0 (Wikimedia Commons)`; P5
  `Foto: Based5290 — Dominio público (Wikimedia Commons)`.
  Artist names identical to the core's. `assets/CREDITS.md` is
  byte-identical between the core build and the ES build
  (SHA-256 prefix `a03a3d26e5e8b624`, 1805 bytes). Live re-query of
  the Commons API was not possible in this subagent (no live
  browser); see Limitations.

### Gate 9 — Readers' corner (PASS)

P7 corner, verified from edition SVG nodes (column x=1473, in
reading order) and the P7 card:

- Letter byte-identical to the core (3 nodes, y=1315.6/1346.1/
  1376.7): `「你好！我住在上海。立冬那天，我吃了饺子，也给妈妈打了电话。
  双11，我买了一件毛衣，现货第二天就到了。」`
- Disclosure in Spanish, labelled editor's example, stating no
  genuine letters exist and deferring the VOL.1 promise
  (`Aplazado, no cancelado`): `Ejemplo de la redacción, no una carta
  real. VOL.1 prometió cartas reales y la mejor redacción de VOL.1 en
  VOL.2; no ha llegado ninguna carta real ni hay ningún texto
  publicable, así que este rincón sigue publicando un ejemplo de la
  redacción.` (nodes y=1437.2–1579.2).
- **Explicit open invitation, inside the corner itself** (nodes
  y=1607.6/1636.0/1664.4, visible verbatim on the P7 card):
  `¡Envíanos tu carta en chino! Escribe dos frases sobre tu semana y
  la publicaremos aquí.`
- Measurement note: a naive whole-page concatenation check initially
  returned False for the disclosure/invitation because P7's
  document order interleaves columns; restricting to the corner
  column in reading order gives the verbatim strings above. This is
  a measurement artifact, not a content gap.

### Gate 10 — Furniture three-way (core EN · W43 ES · this edition) (PASS)

Measured from shipped SVGs (badge node = (x, y, size, text)):

- **P1 badge — re-measured and confirmed:** core EN (975, 434),
  19.5pt; W43 shipped ES (975, 434), 19.5pt,
  `TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL — LA
  EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`; this edition the W43
  string verbatim at (975, 434), 19.5pt. The first proof's
  adjudication (975, 434), 19.5pt stands; body strapline at y=372
  untouched.
- **P8 separators — re-verified on all three, shipped wins:**
  core `— Page N —` (all 8); W43 `— Página N —` (all 8); this
  edition `— Página N —` (all 8, sentence case, zero occurrences
  of all-caps `PÁGINA`). `tools/tables.json` still lists the es
  separator as all-caps `— PÁGINA {N} —` and was **NOT edited**,
  per the adjudication.
- Footer (all 8 pp, P1/P2/P8 verified + card eyeball on all 8):
  `Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.2 · TEXTO EN CHINO
  SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL`.
- Page line (all 8): `Página N de 8`. Gloss prefix: `Nota — `.
  P8 header: W43 strings verbatim. P1 strap:
  `SEMANARIO CHINO SIMPLIFICADO · VOL.2 · 双11 · 立冬 · S16`. P1
  strapline: `给学中文的人的周报 — Lee la China real, en chino`.
  Top strip: `每周读中文 · Lee chino de verdad, cada semana`.
  Masthead: bare `Lucerna`; `The Lucerna` 0, `Le Lucerna` 0.

### Gate 11 — P1 glossline / P7 glossline near-miss check (PASS)

Both deliberately preserved strings are intact on the delivered
cards:

- P1 glossline keeps `solar`: P1 nodes (x=1451) read
  `「立冬」 lìdōng — Comienzo del Invierno: el primer término solar
  del invierno. 立冬到了，冬天要来了。Ejemplo: 「立冬那天，我们吃饺子。」`
  — the phrase `primer término solar del invierno` is intact
  across the wrap (nodes y=1712.0/1742.1/1772.2). The shortened
  P8 note (`el primer término del invierno`, no `solar`) is a
  different replacement and did not touch this line.
- `Dos palabras más` glossline keeps the old wording: P7 nodes
  (x=527, y=1170.9/1203.6/1236.3/1269.0) read
  `Dos palabras más: 凌晨 (língchén) son las horas pequeñas después
  de medianoche, antes del alba; 傍晚 (bàngwǎn) es el rato corto
  justo antes de que oscurezca.` The shortened P8 key 105 note
  (`las primeras horas tras medianoche`) is a different replacement.
- A naive whole-page concatenation check initially missed both
  (wrap + column interleave); the node-level readings above are the
  adjudicated evidence.

### Gate 12 — Web regen (PASS, with documented timestamp variance)

Procedure: copy of the delivered SVGs + the ES build's `render.py`
(BASE repointed to reproof scratch `work/webregen`) run with the
venv Python (`work/webregen.log`).

- Cards regenerated 8/8 **byte-identical** to the delivered cards.
- Print PDF regenerated **byte-identical**: 50,133,157 bytes,
  SHA-256 `e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46`
  = KIT pin, 8 pages.
- Web PDF regenerated: 8 pages, **3,242,033 bytes** = KIT size;
  SHA differs from the delivered pin in exactly **10 bytes across 2
  ranges, all in the two timestamps** — `/CreationDate
  (D:20261028071904Z)` / `/ModDate (D:20261028071904Z)` (delivered)
  vs `…082615Z` (regen). Page count, page images, and every other
  byte are identical. Stated explicitly: content-identical,
  timestamp bytes excepted.
- Delivered cards are all 1950×2700 RGB PNGs.

### Gate 13 — Eyeball all 8 cards (PASS)

Every delivered card read in full:

- P1: masthead, strap, strapline, badge, headline band, calendar,
  contents, word of the week, locker photo + credit, briefs, quick
  quiz — no overflow/overlap; footer clear.
- P2: gloss boxes, valley photo + credit, word cards, exercises
  11–28 — clean; footer clear.
- P3: frost + dumpling photos + credits, gloss boxes, exercises
  29–46 — clean; footer clear.
- P4: LAN-party photo + credit, schedule box, `Sina Sports` source
  line (proper noun, also present in the core, 1× in each), exercises
  47–64 — clean; footer clear.
- P5: popcorn photo + `Dominio público` credit, gloss boxes,
  exercises 65–82 — clean; footer clear.
- P6: practice-data bar chart with all labels fully visible and
  unclipped, `Cuentas` head fitting its box, exercises 83–100 —
  clean; footer clear.
- P7: A2/B1/B2 columns, error clinic, Spanish frame
  (`(Primero mira las reseñas y luego pide.) El marco 先…再… da el
  orden de las acciones. Más: …`), readers' corner (disclosure +
  invitation, both visible), 8 phrases with correct `Página N`
  tags, VOL.3 teaser, footer clear.
- P8: test sections A–F, writing model, all 150 keys grouped by
  `— Página N —`, dash style, top rule clear of text, keys ending
  well above the footer — clean.
- Targeted English-residue scan over delivered SVG text:
  `The Lucerna`/`Le Lucerna`/`— Page `/`Notes｜`/`Answer keys`/
  `First check the reviews`/`the AI film`/`PÁGINA`: all 0. The only
  `Sport` hit is the proper-noun source name `Sina Sports` (1×,
  also in the core).
- Weekday spot-check (Asia/Shanghai, `date -d`): 2026-11-02 Monday,
  2026-11-07 Saturday, 2026-11-08 Sunday, 2026-11-11 Wednesday —
  matching every Spanish weekday rendering in the edition.

### Gate 14 — ABSTRACT.txt (PASS)

- Single line (+ trailing newline), 468 bytes, **no ASCII double
  quotes**, Spanish, in the edition dir.
- Names: Lucerna, `chino simplificado`, `lectores hispanohablantes`;
  real topic keywords: Doble 11 stock sales with direct discounts,
  Comienzo del Invierno Saturday 7 November, S16 World Championship
  quarter-finals, AI film Sanxingdui Future Past, winter film We
  Only Have One Life; levels A2–B2; `150 preguntas`; learner search
  phrase `aprende chino leyendo noticias reales en chino`.

## Non-blocking observations (NOT blocking items — do not mix into the verdict)

1. **Stale comment block, build-dir transform.py lines 28–32:** still
   says the content34 A2→B1 line is "HELD, not deleted … it stays".
   That comment is stale — the line WAS deleted in micro-fix round
   2 under explicit coordinator authorization — but it is
   comment-only, does not execute, and was deliberately left
   untouched under the one-line-only authorization. Recorded here
   only; it fails no gate. (Transform SHA-256 post-round-2:
   `b2dda203bfcbee83363079557ee4cff770b3a13b071e97d0ae612ea70892d5d3`,
   unchanged by this reproof.)
2. **318-vs-317 denominator wording:** the round-2 brief asked for
   "318/318", but that denominator cannot survive the deletion (318
   entries = 317 hits + 1 miss; deleting one entry leaves 317
   entries, all hitting). 317/317 + exit 0 is the correct measured
   result; the gating condition is exit 0. Not a defect.
3. Web PDF regen SHA differs from the KIT pin in exactly the two
   timestamp fields (Gate 12). Content-identical; no action needed
   unless the pipeline wants deterministic timestamps.
4. The ES build's `run.py` docstring says "Run the IT weekly build
   files…" — a copy artefact from another pairing's driver, carried
   over from the first proof's observation. No functional effect.
5. `tools/tables.json` still lists the es P8 separator as all-caps
   `— PÁGINA {N} —`, contradicting the shipped `— Página N —`
   form. Per adjudication, shipped wins and the table was NOT
   edited; the discrepancy stays recorded for the parent line.

## Limitations (stated plainly)

1. Image Commons Artist-field verification was NOT re-queried live:
   this subagent has no live browser. The gate is satisfied by
   payload identity + credit identity against the core (whose KIT
   records the 2026-10-27 Commons verification) + the identical
   `CREDITS.md`. A fresh Commons API check is a separate live-source
   task if the coordinator wants one.
2. Trend/fact re-sourcing was NOT redone: the edition is a
   translation fan-out; freeze diff (added CJK 0) + registry
   identity prove no target fact, date, or figure changed from the
   core, so the core KIT's sourcing and honesty limits are
   inherited, not independently re-verified.
3. Spanish was checked by full reading of extracted text and all 8
   cards, not by a native speaker; no Spanish grammar/spelling
   defect was found, but this proof cannot claim native-speaker
   authority.
4. This reproof wrote nothing to the delivery dir, the core, the
   build dirs, `tools/`, or `weekly-git`. All proof work is under
   `hidden_files/w45/zh-cn-es-reproof/work/`.

## Files produced by this reproof

- `hidden_files/w45/zh-cn-es-reproof/REPORT.md` (this report)
- `hidden_files/w45/zh-cn-es-reproof/work/mtime1.txt`,
  `mtime2.txt` (pre-flight snapshots)
- `hidden_files/w45/zh-cn-es-reproof/work/delivery-hash-start.txt`,
  `delivery-hash-close.txt`
- `hidden_files/w45/zh-cn-es-reproof/work/gate10/` (fresh core copy
  + fixed transform.py alone + repointed driver run; repro SVGs in
  `gate10-out/`)
- `hidden_files/w45/zh-cn-es-reproof/work/gate10-transform.log`,
  `gate10-driver.log`
- `hidden_files/w45/zh-cn-es-reproof/work/baseline-zhcn/` (freeze
  baseline copy), `freeze-baseline.log`, `freeze-diff.json`,
  `freeze-diff.log`
- `hidden_files/w45/zh-cn-es-reproof/work/p8.json`, `p8.log`
- `hidden_files/w45/zh-cn-es-reproof/work/occlusion-selftest.log`,
  `occlusion.json`, `occlusion.log`
- `hidden_files/w45/zh-cn-es-reproof/work/rowcheck.py`,
  `rowcheck.log`
- `hidden_files/w45/zh-cn-es-reproof/work/gates6_11.py`,
  `gates6_11.log`
- `hidden_files/w45/zh-cn-es-reproof/work/svgtxt.py`
- `hidden_files/w45/zh-cn-es-reproof/work/webregen/` (regenerated
  cards + print/web PDFs from delivered SVGs), `webregen.log`,
  `webregen-cards.sha`, `delivered-cards.sha`

## PDF pins (delivered files, re-verified at close)

- Print `Lucerna-VOL2-ES.pdf`: 50,133,157 bytes, 8 pages,
  SHA-256 `e53d52040d1990edbb3c89aa6a3e0fc29d83c9325de75e3f1f65aed911543c46`.
- Web `Lucerna-VOL2-ES-web.pdf`: 3,242,033 bytes (< 10 MB), 8 pages,
  SHA-256 `0ee7547e5d24a835cb349a4037fa94adf279c3350b73a26dacb414609baa573c`.
