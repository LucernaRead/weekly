# INDEPENDENT RE-PROOFREAD — W45 zh-cn × pt (Simplified Chinese target · Portuguese reader)

## Verdict: PASS — ZERO PROBLEMS

**All 14 gates independently re-verified, including the previously failing
Gate 10.** The fixed standalone transform alone reproduces the delivered
edition 8/8 byte-identical with exit code 0, zero warnings, registry 150
and TOTAL replacements 538. No blocking item remains. This report is the
finalization evidence for the coordinator to insert; this proofreader
declares nothing shipped, and took no Discord, repo, `weekly-git`,
`insert.py`, cron, or main-chat action.

First proof (hidden_files/w45/zh-cn-pt-proof/REPORT.md) was NOT PASS on
Gate 10 only; fix log (hidden_files/weekly-report-w45-zh-cn-pt-build/
FIX-LOG.md) folded 19 changes into the transform. Every other gate was
re-verified from scratch, not copied from either document.

---

## Pre-flight (coordinator ruling: no concurrent writer) — PASS

- (a) No live writer to the PT dirs or the transform: at task start the
  only live Python worker was a sibling zh-cn-ja proof's `run.py` in its
  own `w45/zh-cn-ja-proof/work/repro-core` dir, plus sibling de/it
  snapshot sleeps — all in their own dirs, none writing to the PT
  delivery dir, PT build dir, or the transform file (verified by `ps`
  + per-process cwd/cmdline inspection). At close: no PT process.
- (b) Two mtime snapshots ~3.5 min apart (snap1/snap2, all of delivery
  + PT build + transform file): **SNAP2-IDENTICAL, zero changes.**
- (c) Fix session completed: transform mtime 2026-10-28 08:06, FIX-LOG
  filed, KIT §10 (fix record) written 08:10, before this proof started.
- Gate 1 close check: delivery hashes at close identical to start, and
  snap3 identical to snap1 — **nothing changed during this round.**

## Per-gate evidence (tools: `tools/venv/bin/python`)

### Gate 1 — Delivery hash verification (start AND close): PASS

Start hashes = fix-log pre-fix hashes = close hashes, all 20 files
(8 SVGs, 8 cards, 2 PDFs, ABSTRACT.txt, WEEKLY-KIT.md). Print PDF
47,047,752 B sha `41906847…329872`; web PDF 3,252,004 B sha
`0bc2e290…0500aa` (full pins at end). Transform sha at start and close:
`2e9e5d482636ab3b8f9ee8613aee1fdd74c270ed8153b0f5850bb43acea8982e`
= fix-log post-fix pin (pre-fix was `3e5e0f34…`).

### Gate 10 — Documentation chain (the fixed item): PASS

- Procedure: fresh copy of the W45 zh-cn core build → `work/repro-build`;
  transform copy with **only** its `BUILD` path repointed (diff vs the
  original transform = that one line); transform run; OUT repointed in
  all 5 content files (expanduser spelling) to `work/repro-out` with
  zero core/delivery refs remaining; single one-process driver `run.py`
  (content12 → 34 → 56 → 7 → 8).
- Transform: **exit 0, "TOTAL replacements: 538"** (536 + 2 added pairs).
- Driver: **exit 0, registry TOTAL 150** (A2 56 / B1 69 / B2 25; pages
  10/18/18/18/18/18/12/38; types Complete a frase 68 / Escolha múltipla
  50 / Associação 20 / Escolha no contexto 11 / Escrita 1),
  **HEAD TOO WIDE 0, FLOW OVERFLOW 0** (grep count 0).
- SVGs vs delivered: **8/8 byte-identical** (P1–P8 all MATCH).
- Fold verified against the fix log, all 19: the 12 shortened notes,
  the 3 comma restructurings (keys 14/84/142), the P4 feature gloss,
  the P5 head, the P5 credit, the P6 head — every NEW string present
  in the transform. Two nuances, both legitimate, not defects:
  (i) the P5/P6 head pairs map from the English core forms
  ("Times & numbers" → "Datas e horas"; "Basket maths" →
  "Cálculos") — the intermediate PT forms ("Horários e números",
  "Contas das cestas") never existed in core sources, so they
  correctly do not appear in the transform; (ii) old English strings
  appear in the transform only as pair old-sides, and are absent from
  the PT build sources (grep: none) and from the delivered SVGs
  ("Public domain" 0 occurrences).
- Post-transform sources vs the PT build copy: identical except the
  OUT lines in the 5 content files and render.py's BASE/filename lines
  (core render names vs PT render names — the transform does not
  touch render.py, as expected). The fold is complete and exact.
- The 15 shortened/comma notes were also spot-verified verbatim in the
  delivered P8 SVG, old forms absent.

### Gate 3 — Freeze baseline + strict-CJK diff: PASS

- `freeze.py baseline` on the pristine core build: **8/8 byte-identical**
  (p1 `e057bbfc…`, p2 `c87aa67e…`, p3 `d50f09e1…`, p4 `dd3b1b0f…`,
  p5 `c71ef315…`, p6 `b06a85d2…`, p7 `f2319cb8…`, p8 `eaf368f8…`),
  "core integrity: shipped core SVGs unchanged". Core SVGs re-hashed
  after the repro run: unchanged.
- `freeze.py diff --strict-cjk` core vs edition: p1 +51/−46, p2 +63/−60,
  p3 +38/−38, p4 +40/−41, p5 +42/−41, p6 +39/−38, p7 +91/−88,
  p8 +191/−191 — **added CJK = 0 on every page, TOTAL 0** (exactly the
  first proof's churn).

### Gate 4 — p8.py + style: PASS

- `p8.py compare`: **CLEAN, core 150 noted, edition 150 noted,
  missing=[] extra_count=0 uncertain=[] keydiff=[]**.
- Core `content8.py:119` and PT `content8.py:119` byte-identical
  (`txt = f"{e_['n']}. {e_['key']} — {e_['note']}"`); writing branch
  identical except the required type-name test (`"写作"` → `"Escrita"`).
  Dash style is the W45 core's style and governs (see Gate 10 furniture).

### Gate 5 — Occlusion + rowcheck + chart labels: PASS

- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire,
  clean controls silent).
- Edition audit: **edition 0 flags; core 0 flags; NEW vs core 0.**
- Same-baseline ink-collision scan (own PIL implementation, tables.json
  fonts, SC face index 2, middle/start anchors honoured): **0 collisions
  across all 8 pages**, including the P1 top band.
- P6 chart-label element check (text ink vs later-drawn rects): **0
  overlaps.** Chart bars identical to core: x=325, y/width 1282/810.0,
  1340/537.0, 1398/480.0.

### Gate 6 — Gloss counts (split on `·`): PASS

- Source extraction (text read, no module import): **10 calls in both**,
  per-call **[4, 4, 4, 3, 3, 3, 3, 3, 3, 3], total 33 in both**,
  headwords identical item by item (including the folded P4 gloss).
- Rendered: "Nota — " 10× in edition SVGs, "Notes" 0×.

### Gate 7 — P7 golden sentences: PASS

- All 8 Chinese phrases byte-identical between core and PT `content7.py`
  quote tables; page tags Página 1/2/2/3/4/4/5/5 (counts in joined P7
  text: 1/2/1/2/2).
- Source-level: each phrase occurs **exactly 2×** (once in its article
  source content12/34/56, once in content7). Rendered joined-text:
  **exactly 2× each** across the edition (article page + P7, comma
  phrases in full-width ， form) — per-node counting misses the
  split-line renders, which is why the joined-text count is the valid
  one (same caveat as the first proof).
- All 8 PT translations present in P7 (space-joined check) with correct
  page tags, visible on the P7 card.

### Gate 8 — Images: PASS

- All 6 asset files byte-identical (md5) core build vs PT build; all 6
  embedded SVG payloads byte-identical core SVG vs edition SVG
  (P1 locker, P2 valley, P3 frost + dumplings, P4 lanparty, P5 popcorn;
  P6/P7/P8 none).
- Credits in PT column form, all present: P1 "Foto: Map hobby — CC0
  (Wikimedia Commons)", P2 "Foto: Paul Gilmore — CC0 (Wikimedia
  Commons)", P3 "Foto: Gerda Arendt — CC0 (Wikimedia Commons)" +
  "Foto: Syced — CC0 (Wikimedia Commons)", P4 "Foto: Syced — CC0
  (Wikimedia Commons)", P5 "Foto: Based5290 — Domínio público
  (Wikimedia Commons)". "Public domain" 0 occurrences in edition SVGs.
- Artist names match the core `assets/CREDITS.md` Commons API Artist
  column verbatim (see Limitations: no live Commons re-query; no new
  images, so no new authorization question arises).

### Gate 9 — Readers' corner: PASS (both prongs)

- Disclosure: labelled editor's example ("Exemplo da redação — não é
  uma carta de verdade.") + full Portuguese deferral disclosure,
  self-contained.
- Explicit open invitation, verbatim (space-joined across wrapped
  lines) in the delivered P7 SVG and visible on the P7 card:
  "Escreva-nos! Envie a sua carta em chinês — duas frases já bastam —
  e ela pode sair no próximo número."
- Disclosure measures **exactly 10 wrapped lines** (x=1473,
  y=1437.19 … 1692.79, 28.4 spacing). Teaser rect byte-identical to
  core (x=65, y=2436.1, width 1820, height 118 → ends 2554.1); col3
  last disclosure baseline 1692.79 consistent with the KIT's col3 end
  1708.1. (P7 rect lists differ elsewhere only in column badge
  positions shifted by legitimate Portuguese wrap growth — the teaser
  rect itself is identical.)

### Gate 10 (furniture) — three-way: PASS

- Badge **measured** in all three P1 SVGs: (x=975 centre, y=434.0),
  **19.5pt, weight 700, Noto Sans CJK SC** — core (EN badge), W43 PT
  badge, and this edition (verbatim W43 PT badge string) all in the
  same slot. The zh-cn in-place case applies (NOT EN×ZH-TW
  subtitle-slot, NOT FR/IT y=574 insert); no masthead element moved.
- Subtitle y=330 40pt bold, strapline y=372 19pt, top strip y=92:
  edition verbatim W43 PT forms with VOL.2 + W45 topic words
  (SEMANÁRIO CHINÊS SIMPLIFICADO · VOL.2 · 双11 · 立冬 · S16;
  "Leia a China de verdade, em chinês"; "Leia chinês de verdade,
  toda semana").
- Footers y=2624 all 8 pages verbatim W43 template with VOL.2;
  page lines "Página N de 8" all 8 pages; P8 separators
  "— Página N —" (N=1–8) identical to W43; P8 keys head and right line
  verbatim W43; gloss prefix "Nota — ". Shipped W43 wins where it
  differs from tables.json; tables.json was NOT edited. P8 dash style
  adjudicated against the W45 core, not VOL.1's paren (Gate 4).

### Gate 11 — Web regen: PASS (timestamp bytes excepted, stated explicitly)

- Repointed render.py copy (BASE → scratch only) run against the
  repro SVGs: **cards 8/8 byte-identical**, **print PDF byte-identical**
  (47,047,752 B, sha `41906847…329872`).
- Web PDF: same byte size (3,252,004 B), 8 pages, and a whole-file
  byte comparison shows differences in **exactly 8 byte positions, all
  inside the two PIL timestamp fields** (delivered CreationDate/
  ModDate 20261028073114Z vs regen 20261028082417Z; the fix round's
  "6 bytes" was the same artifact for its regen time — the count of
  differing digit positions depends on the two timestamps compared).
  **Web PDF is content-identical; no web-PDF regen can reproduce the
  delivered sha.** The delivered web PDF itself was verified directly
  (8 pages, 3,252,004 B, sha `0bc2e290…0500aa`).

### Gate 12 — Eyeball all 8 cards: PASS

- P1–P8 each viewed in full at 1950×2700, plus a 2× crop of the P5
  popcorn caption. No overflow, overlap, footer intrusion, clipped
  box, or missing content on any page. Specifics: P1 badge/masthead/
  photo/quiz clean; P2 grouped chip "25–28."; P3 two photos + credits
  clean; P4 PT gloss box clean; P5 "Datas e horas" head fits, caption
  + corrected credit legible at 2×; P6 chart bars/labels unclipped,
  "Cálculos" head fits, chart note on one line; P7 columns/clinic/
  frame/readers' corner (disclosure + invitation visible)/golden
  sentences/teaser all clean; P8 test sections + all 150 keys end well
  above the footer band, dash style throughout.

### Gate 13 — ABSTRACT.txt: PASS

- Single line (586 chars + trailing newline), **0 ASCII double quotes**,
  Portuguese. Names real topic keywords (Double 11 to 13 Nov, Início
  do Inverno 7 Nov, S16 Swiss phase, Dia dos Jornalistas 8 Nov,
  Sanxingdui AI film, We Only Have One Life), the paper name
  (Lucerna), the target language (chinês simplificado), the reader
  language (português), A2–B2, 150 exercises, and a learner search
  phrase ("aprender chinês lendo notícias de verdade").

### Gate 14 — First-proof non-blocking notes re-checked: PASS (all confirmed)

- "Associação"/"Escrita" print only as W43-identical section furniture:
  literal counts edition = W43 = "Associação" 5, "Escrita" 2;
  "Complete a frase" / "Escolha múltipla" / "Escolha no contexto" 0 in
  both. No registry leakage.
- P6 key-points box taller in PT (height 175.4 vs core 145.675 at
  (527, 723.0, width 434)) — legitimate wrap growth; occlusion 0.
- Chip pattern: P2–P6 each carry 14 standalone single-number chips +
  1 grouped range chip (e.g. "25–28."), identical in core and W43 —
  grouped items share a chip, not a numbering gap; registry + P8 CLEAN
  prove numbering.

---

## Non-blocking observations (NOT blocking items — do not mix into the verdict)

1. **KIT §7 still says "536 replacements"** while the post-fix transform
   is 538; KIT §10 (the fix record) states 538 correctly. A wording
   tidy for the coordinator; the artifact, the transform, and Gate 10
   are unaffected.
2. **Web-PDF timestamp byte count is 8 positions in this regen vs the
   fix round's 6** — both are the same timestamp-only artifact (see
   Gate 11); the differing-digit count varies with the regen time.
   Content-identical in both cases.
3. **Rowcheck implementation note:** the same-baseline scan is this
   proofreader's own PIL-ink approximation (tables.json fonts), not a
   canonical tool — it supplements the canonical occlusion audit (0
   flags), which is the gating measurement.
4. **First-proof note 4 (hash-file exit 1 from path prefixes)** does not
   recur: this round's hash comparisons used identical path lists and
   diffed clean at start vs close.

## Limitations (stated plainly)

- Fan-out proof against the frozen core + W43 furniture, by design: the
  core's facts/dates were NOT re-verified against external sources
  (inherited from the core KIT's `date -d` Asia/Shanghai verification).
  A core fact error, if one existed, would pass through.
- Commons credits were verified against the core `assets/CREDITS.md`
  (which records Commons API Artist-field verification on 2026-10-27),
  not by a fresh live Commons API re-query in this round; no new images
  were introduced, so no new authorization question arises.
- Visual inspection was at full-card resolution (1950×2700) plus one 2×
  crop (P5 caption). Sub-pixel defects below card resolution were
  covered by the geometric audits, not by eye.
- The transform repro repointed only the transform's `BUILD` path and
  the repro copy's `OUT` paths; no other transform content was altered.
- No Discord, repo, `weekly-git`, `insert.py`, or main-chat action was
  taken (forbidden by the task).

## Files produced by this proof (read-only elsewhere)

- This report:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-pt-reproof/REPORT.md`
- Scratch (all under the report's `work/` dir):
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-pt-reproof/work/`
  (snap1/snap2/snap3, hash_start/hash_close, freeze-baseline/diff,
  p8-compare, occlusion + selftest, checks.py + checks-out.txt,
  rowcheck.py + rowcheck.txt, transform-repro.py, transform-run.log,
  repro-build/, repro-out/, driver-run.log, render-regen/ +
  render-regen.log, p5-caption-crop.png)
- Note: `freeze.py baseline` also wrote its scratch output to
  `tools/scratch/baseline-zhcn-proof-pt-reproof/` (the tool's default
  output location, as in the first proof); it was not cleaned, per the
  task's ban on cleaning shared scratch dirs.

## Delivered-file pins (re-verified at close, identical to start)

- Print PDF `Lucerna-VOL2-PT.pdf`: 47,047,752 B, 8 pages, sha256
  `4190684793377b7ac853df3f190e048637323162f9dada01d74d23c613329872`
- Web PDF `Lucerna-VOL2-PT-web.pdf`: 3,252,004 B, 8 pages, sha256
  `0bc2e29083679ec6ce1acaeb27371174b6e4b95e97a560488a3968aba50500aa`
- SVGs: p1 `f1dedefa…`, p2 `c45889e4…`, p3 `d8ac8e61…`, p4 `9cd1c553…`,
  p5 `1aa87a54…`, p6 `3a8e2d85…`, p7 `601d531d…`, p8 `fe519c7b…`
  (full hashes in `work/hash_close.txt`)
- Cards: p1 `d5e9a091…`, p2 `563d1e0f…`, p3 `32b22c31…`, p4 `03b5a0fd…`,
  p5 `bf24d347…`, p6 `0304a9a6…`, p7 `2b9daf4c…`, p8 `603b3a43…`
  (full hashes in `work/hash_close.txt`)
- Transform (post-fix): `2e9e5d482636ab3b8f9ee8613aee1fdd74c270ed8153b0f5850bb43acea8982e`
