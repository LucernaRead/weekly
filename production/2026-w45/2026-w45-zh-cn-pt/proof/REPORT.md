# INDEPENDENT PROOFREAD — W45 zh-cn × pt (Simplified Chinese target · Portuguese reader)

## Verdict: NOT PASS

**One blocking item only (Gate 10).** Every content, geometry, furniture,
P8, gloss, image, readers'-corner, PDF and visual gate PASSES. The single
failure is reproducibility: the standalone transform script does NOT
reproduce the delivered edition. Per the tasking, reproduction failure is
BLOCKING, so this edition cannot be declared finalized on this round —
even though the delivered artifact itself passed every other check.

**Do NOT ship on this report. The coordinator inserts nothing yet.**
Remedy (for the builder/coordinator, NOT performed by this proofreader):
consolidate the five fix-round edits listed under Blocking item B-1 into
`hidden_files/w45-zh-cn-pt-transform.py`, re-run transform-alone to 8/8,
then commission a fresh full proof round.

---

## Blocking item

### B-1 — Gate 10, transform solo reproduction: 5/8, not 8/8

- **Procedure (exactly as tasked):** fresh copy of the W45 zh-cn core build
  → `work/repro-build`, OUT repointed (all 5 content files, expanduser
  spelling) to `work/repro-out`, transform copy with only its `BUILD`
  path repointed to the fresh copy, transform run (exit 0, "TOTAL
  replacements: 536"), then the single one-process driver `run.py`
  (content12 → 34 → 56 → 7 → 8, in order), output compared to the
  delivered SVGs.
- **Result:** P1, P2, P3, P7 byte-identical; **P4, P5, P6, P8 differ.**
  Repro hashes (first 12 hex) vs delivered:
  - P4: repro `6c052ef7b968` vs delivered `9cd1c55337cf`
  - P5: repro `8e09efaecef2` vs delivered `1aa87a544f29`
  - P6: repro `e2cb98ebcea4` vs delivered `3a8e2d85faa1`
  - P8: repro `d3304bcfb777` vs delivered `fe519c7b61b3`
- **String-level diff (repro → delivered, freeze.py diff):**
  - P4 +4/−5: the P4 feature gloss one-off fix is missing from the
    transform. Repro renders the English gloss ("Nota — tǎotài 淘汰 —
    to knock out, to eliminate · nèizhàn 内战 — a match between two
    teams … · zhǐbù 止步 — to stop here, to go no further."); the
    delivered edition renders the Portuguese gloss ("eliminar, tirar
    do torneio · um jogo entre dois times da mesma região · parar
    aqui, não ir adiante."). This is the one-off the builder's KIT §7
    itself discloses as fixed "afterwards" and never folded back.
  - P5 +2/−2: head "C · 时间与数字 · Horários e números" (repro) vs
    "C · 时间与数字 · Datas e horas" (delivered); credit "Foto:
    Based5290 — Public domain (Wikimedia Commons)" (repro) vs
    "Foto: Based5290 — Domínio público (Wikimedia Commons)"
    (delivered). Fix rounds 2 and 4, not in the transform.
  - P6 +1/−1: head "C · 练习篮子算一算 · Contas das cestas" (repro)
    vs "C · 练习篮子算一算 · Cálculos" (delivered). Fix round 2.
  - P8 +18/−33: the 12 shortened P8 notes (fix round 1) and the 3
    comma restructurings (fix round 3, keys 14/84/142) are missing
    from the transform; the rest of the ± counts is line reflow from
    those changes. Repro P8 notes still read e.g. "14. A — Depois do
    立冬， o tempo fica mais frio dia a dia." (with the
    renderer-converted ， after 立冬) vs delivered "14. A — O tempo
    fica mais frio dia a dia depois do 立冬."
- **The repro run reproduces the builder's build1 defects:** 2×
  `HEAD TOO WIDE` (P5 "Horários e números", P6 "Contas das cestas")
  and `FLOW OVERFLOW [P8-keys]` to y=2585 (bottom 2540). The delivered
  edition fixed all three; the transform alone does not.
- **Root cause (evidence, not speculation):** the transform file's
  mtime is 2026-10-28 07:09, predating the fix rounds (build logs
  07:11–07:28, delivered SVGs 07:28). Its text contains the pre-fix
  strings ("Horários e números", "Contas das cestas", "Depois do 立冬,",
  "No 立冬, ela fez…") and zero occurrences of "Cálculos",
  "Datas e horas" or "Domínio público". The fixes live only in the PT
  build copy (`hidden_files/weekly-report-w45-zh-cn-pt-build/`).
- **Contrast evidence (why this is a stale-record failure, not an
  undocumented artifact):** a repointed copy of the PT BUILD directory
  itself, run through the same one-process driver, reproduces the
  delivered SVGs **8/8 byte-identical** with **zero** FLOW OVERFLOW /
  HEAD TOO WIDE warnings and identical registry stats (see Gate 10b).
  The delivered artifact is fully deterministic from its build
  directory; only the standalone transform record is stale.
- **What was NOT done:** this proofreader did not edit the transform,
  the build copy, or the delivery dir (task forbids fixing). No
  conclusion about the edition's content rests on this item.

---

## Pre-flight (coordinator ruling: no concurrent writer)

- **(a) No live writer to the PT dirs:** at task start the only live
  Python processes were a sibling FR proofreader's freeze-baseline run
  (its own `tools/scratch/baseline-zhcn-proof-fr` output) and later a
  sibling IT proofreader — both read-only against the core/FR/IT dirs,
  neither writing to the PT delivery dir, the PT build dir, or the
  core build dir. Verified by `ps` + per-process cmdline inspection.
- **(b) Two mtime snapshots, ~3.5 min apart, of all three dirs**
  (delivery `files/weekly-report-w45-zh-cn-pt/`, PT build
  `hidden_files/weekly-report-w45-zh-cn-pt-build/`, core build
  `hidden_files/weekly-report-w45-zhcn-build/`): **SNAP2-IDENTICAL**,
  zero changes.
- **(c) Builder session completed:** PT build6 log ends "ALL DONE"
  (registry TOTAL 150), KIT written 07:34 UTC, all delivered files
  timestamped 07:28–07:34 UTC, before this proof started (~07:36 UTC).
- **Pre-flight: PASS.** Full proof proceeded.

---

## Per-gate evidence (all tools: `tools/venv/bin/python`)

### Gate 1 — freeze baseline 8/8 + strict-CJK diff: PASS

- `freeze.py baseline --build ../hidden_files/weekly-report-w45-zhcn-build
  --core-svg ../files/weekly-report-w45-zhcn-core/svg
  --out scratch/baseline-zhcn-proof-pt` →
  **"baseline: 8/8 SVGs byte-identical"** (p1 `e057bbfc…`, p2 `c87aa67e…`,
  p3 `d50f09e1…`, p4 `dd3b1b0f…`, p5 `c71ef315…`, p6 `b06a85d2…`,
  p7 `f2319cb8…`, p8 `eaf368f8…` — exactly the builder's claimed hashes),
  freeze.py itself: "core integrity: shipped core SVGs unchanged".
- Core SVGs re-hashed before / after baseline / at end of proof:
  hash-only lists **identical all three times**.
- `freeze.py diff --strict-cjk` core vs edition →
  p1 +51/−46, p2 +63/−60, p3 +38/−38, p4 +40/−41, p5 +42/−41,
  p6 +39/−38, p7 +91/−88, p8 +191/−191 — **exactly the builder's
  claimed churn; added CJK = 0 on every page, TOTAL 0.**
- Removed-CJK audit (every removed CJK run checked against its edition
  page): all vanished runs are (a) EN-column furniture replaced by PT
  furniture (footer "简体中文周报 / 简体中文正文 / 英语讲解", badge,
  page line "第 N 版 / 共 8 版"), or (b) the core's Chinese disclosure
  sentence on P7 replaced by the Portuguese disclosure. **No article
  body, stem, option, or caption text was removed.** The frozen
  editor's-example letter itself remains in Chinese.

### Gate 2 — p8.py compare: PASS

- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-pt
  --target zh-cn` → **"core 150 noted, edition 150 noted, status:
  CLEAN, missing=[] extra_count=0 uncertain=[] keydiff=[]"**.
- P8 style verified from code, never memory: core `content8.py:119`
  and PT `content8.py:119` are byte-identical —
  `txt = f"{e_['n']}. {e_['key']} — {e_['note']}"` — and the writing
  branch `txt = f"{e_['n']}. ✓ {e_['note']}"` is likewise identical;
  only the type-name test differs (`"写作"` → `"Escrita"`, the required
  localization). Core prints dash, edition prints dash, VOL.1 prints
  paren — the W45 core's style governs, so dash is deliberate and
  correct. Separators "— Página N —" (N=1–8) byte-identical to W43.
- 12 shortened P8 notes spot-checked in the delivered P8 (keys
  1, 2, 9/11, 12, 51/130, 77, 109, 111, 115, 120, 135, 147, 149):
  all single-line, keys and facts unchanged (e.g. 51/130 "A final:
  15 de novembro, 03:00, hora de Pequim." — matches the core fact).
- 3 comma restructurings verified verbatim in delivered P8:
  14 "O tempo fica mais frio dia a dia depois do 立冬.",
  84 "Com o 直降 o preço do checkout é o que você paga.",
  142 "No 立冬 ela fez bolinhos com a mãe." — no comma-after-CJK in
  any of them; final strict-CJK diff is 0 (Gate 1).

### Gate 3 — occlusion + same-baseline + chart labels: PASS

- `occlusion_audit.py --selftest` → OK (all 6 planted classes fire,
  clean controls silent). Refusal condition not triggered.
- `occlusion_audit.py …/weekly-report-w45-zh-cn-pt
  --core …/weekly-report-w45-zhcn-core` → **edition 0 flags; core 0
  flags; NEW vs core 0.**
- Same-baseline ink-collision scan (builder's rowcheck logic, run from
  a copy in my own work dir against a copied svglib): **0 collisions
  across all 8 pages**, including the P1 top band (Portuguese centre
  strap longer than the English one).
- P6 chart-label element check (true-ink boxes vs later-drawn rects,
  core and edition): **0 overlaps in both.** Chart bars verified
  identical to core in the SVG rects: x=325, y/width 1282/810.0,
  1340/537.0, 1398/480.0 in both. (One rect differs between core and
  edition P6 — a key-points box background at (527, 723.0, 434) that is
  taller in PT, 175.4 vs 145.675 — legitimate Portuguese wrap growth,
  covered by the 0-flag audit; see Non-blocking.)

### Gate 4 — gloss counts (split on `·`): PASS

- Extracted from build sources (not renders): **10 calls in both**,
  per-call **[4, 4, 4, 3, 3, 3, 3, 3, 3, 3], total 33 in both**,
  headwords (Chinese token before " — ") identical item by item.
- Rendered prefix: "Nota — " occurs 10× in edition SVGs, "Notes" 0×.

### Gate 5 — P7 golden sentences: PASS

- All 8 Chinese phrases byte-identical between core and PT `content7.py`
  quote tables; page tags match (Página 1/2/2/3/4/4/5/5 = core
  p. 1/2/2/3/4/4/5/5).
- Each phrase verified as a contiguous substring of this issue's own
  article sources (before the P7 block): 「不用等11月11日」 P1,
  「下单就能发货」 P2, 「先看结算页,再付款」 P2, 「水开始结冰」 P3,
  「三场都输了」 P4, 「小局一场没赢」 P4, 「故事够不够好」 P5,
  「别以后,就现在」 P5. Three of them (下单就能发货 / 水开始结冰 /
  三场都输了) render split across wrapped SVG lines, which is why a
  naive single-node search misses them; the source contiguity and the
  P7 render (same coordinates as core) confirm them.
- Rendered comma forms: the two comma phrases render with full-width
  ， ("先看结算页，再付款", "别以后，就现在") at the same coordinates
  (y=2139.1, 2289.1) in BOTH core and edition — the svglib
  ASCII-comma-adjacent-to-CJK conversion, inherited, not a change.
- All 8 phrases + PT translations + "(Página N)" tags present in the
  delivered P7 SVG and visible on the P7 card.

### Gate 6 — images: PASS

- All 6 payloads byte-identical (md5) between core assets, core SVGs
  and edition SVGs: P1 locker.jpg, P2 valley.jpg, P3 frost.jpg +
  dumplings.jpg, P4 lanparty.jpg, P5 popcorn.jpg; P6/P7/P8 none —
  same files and placements as the core.
- Credits in PT column form, all present: P1 "Foto: Map hobby — CC0
  (Wikimedia Commons)", P2 "Foto: Paul Gilmore — CC0 (Wikimedia
  Commons)", P3 "Foto: Gerda Arendt — CC0 (Wikimedia Commons)" +
  "Foto: Syced — CC0 (Wikimedia Commons)", P4 "Foto: Syced — CC0
  (Wikimedia Commons)", P5 "Foto: Based5290 — Domínio público
  (Wikimedia Commons)". No leftover "Public domain" anywhere
  (0 occurrences in edition SVGs). Credit names match the Commons
  Artist-field forms carried by the core KIT/assets CREDITS (no new
  images introduced, so no new authorization question arises).

### Gate 7 — readers' corner: PASS (mandatory gate, both prongs)

- Disclosure: labelled editor's example ("Exemplo da redação — não é
  uma carta de verdade.") + full deferral disclosure in Portuguese,
  self-contained (core's Chinese disclosure sentence replaced, not
  silently dropped).
- Explicit open invitation, verbatim in the delivered P7 SVG (joined
  across wrapped lines) and on the P7 card:
  "Escreva-nos! Envie a sua carta em chinês — duas frases já bastam —
  e ela pode sair no próximo número."
  (The VOL.3 teaser line and the P2/P3/P5/P6 "E você?" prompts were
  NOT relied on, per the task.)
- Disclosure measures **exactly 10 wrapped lines**, same baselines as
  the core (x=1473, y=1437.19 … 1692.79, 28.4 spacing, both editions).
  P7 col3 ends 1708.1 and teaser ends 2554.1 in BOTH the core KIT
  (§"ends at y = 1708.1, teaser ends at y = 2554.1") and the PT build6
  log, and the delivered P7 teaser rect is byte-identical to the
  core's (x=65, y=2436.1, height 118 → ends 2554.1). Footer line 2580
  untouched.

### Gate 8 — furniture three-way + two adjudications: PASS

- Measured (not copied) from core / W43 shipped / edition P1 SVGs:
  - Masthead `Lucerna` (no article) in all three.
  - Subtitle y=330, 40pt bold: core "简体中文版 · VOL.2 · 双11 ·
    立冬 · S16" / W43 "SEMANÁRIO CHINÊS SIMPLIFICADO · VOL.1 · 双11 ·
    大闸蟹 · 霜降" / edition "SEMANÁRIO CHINÊS SIMPLIFICADO · VOL.2 ·
    双11 · 立冬 · S16" (VOL + topic words updated, justified).
  - Strapline y=372, 19pt: core "给学中文的人的周报 — Read the real
    China, in Chinese" / W43 and edition verbatim "给学中文的人的周报
    — Leia a China de verdade, em chinês".
  - Top strip y=92: core "每周读中文 · Read real Chinese, every
    week" / W43 and edition verbatim "每周读中文 · Leia chinês de
    verdade, toda semana".
  - Footer y=2624, all 8 pages, edition verbatim W43 template with
    VOL.2: "Lucerna · SEMANÁRIO CHINÊS SIMPLIFICADO VOL.2 · TEXTOS EM
    CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS"; page line
    "Página N de 8" all 8 pages.
  - Gloss prefix "Nota — " (Gate 4); P8 keys head "答案 · Gabarito —
    por página, com uma nota em cada resposta" and right line "Todas
    as notas em português · ✓ = a tarefa de escrita" verbatim W43.
- **Adjudication (a) — badge slot: builder's claim CONFIRMED.**
  Badge node measured in all three: (x=975 centre, y=434.0),
  19.5pt, bold, Noto Sans CJK SC. Core badge is itself printed there,
  and W43 uses exactly that slot and size, so the zh-cn family
  in-place case applies (NOT the EN×ZH-TW subtitle-slot case, NOT the
  FR/IT inserted-at-y=574 case). Edition badge string is verbatim the
  W43 PT badge. No masthead element moved; body below y=606 untouched
  (frozen elements' coordinates match the core).
- **Adjudication (b) — P8 style: builder's claim CONFIRMED.**
  W45 core prints dash (verified in core SVG: "1. 10 — …" and in
  core code, Gate 2); edition prints dash; VOL.1 printed paren
  because the VOL.1 core did. The W45 core's style governs this
  edition, NOT VOL.1's paren. Answer-generation code byte-identical
  to the W45 core's except the required type-name string (Gate 2).

### Gate 9 — web PDF regeneration: PASS (with timestamp note)

- Repointed copy of the build's `render.py` (BASE → my scratch only),
  run against the delivered SVGs: **cards 8/8 byte-identical** (full
  sha256 match per card), **print PDF byte-identical**:
  47,047,752 B, sha256
  `4190684793377b7ac853df3f190e048637323162f9dada01d74d23c613329872`
  = KIT pin.
- Delivered web PDF verified directly: 8 pages, 3,252,004 B (< 10 MB),
  sha256
  `0bc2e29083679ec6ce1acaeb27371174b6e4b95e97a560488a3968aba50500aa`
  = KIT pin.
- Regenerated web PDF: same byte size (3,252,004), 8 pages, same
  mediaboxes (1400×1938), **identical per-page image-stream hashes**
  on all 8 pages. Its file sha differs ONLY because PIL writes
  CreationDate/ModDate timestamps (delivered 20261028073114Z vs regen
  20261028075244Z). This is a timestamp artifact, not a content
  difference; no web-PDF regen can ever reproduce the delivered sha.
  Recorded here so the timestamp delta is not misread as a mismatch.
- ABSTRACT.txt: single line, 0 ASCII double quotes, Portuguese,
  names real topics (Double 11 to 13 Nov, Início do Inverno 7 Nov,
  S16 Swiss phase, Dia dos Jornalistas 8 Nov, Sanxingdui AI film,
  We Only Have One Life), masthead, target language, A2–B2, 150
  exercises, and a learner search phrase ("aprender chinês lendo
  notícias de verdade").

### Gate 10 — transform solo reproduction: FAIL (blocking, B-1)

- Transform-alone: **5/8** (P1, P2, P3, P7 identical; P4, P5, P6, P8
  differ) — full evidence under Blocking item B-1. Registry from the
  transform-alone run itself still matches the core exactly (TOTAL
  150; A2 56 / B1 69 / B2 25; pages 10/18/18/18/18/18/12/38; types
  Complete a frase 68 / Escolha múltipla 50 / Associação 20 /
  Escolha no contexto 11 / Escrita 1; writing model 172 chars),
  confirming the failure is confined to the five unconsolidated fix
  edits, not to numbering or content structure.
- **Gate 10b (supplementary, not tasked): PT-build-copy rerun 8/8.**
  Repointed copy of `hidden_files/weekly-report-w45-zh-cn-pt-build/`
  through the one-process driver reproduces the delivered SVGs 8/8
  byte-identical, zero warnings, identical registry. The delivered
  artifact is deterministic from its build directory.

### Gate 11 — all 8 cards visual: PASS

- P1–P8 each eyeballed in full at 1950×2700, plus a 2× crop of the P5
  popcorn caption. No overflow, overlap, footer intrusion, clipped
  box, or missing content found on any page. Specifics: P1 badge/
  masthead/photo/quiz clean; P2 grouped matching chip "25–28." (this
  is why P2–P6 show 14 standalone chips — grouped items share a chip;
  the same pattern appears in the core and W43, so it is not a
  numbering gap); P3 two photos + credits clean; P4 PT gloss box
  clean; P5 "Datas e horas" head fits, caption legible at 2× with the
  corrected credit; P6 chart bars/labels unclipped, "Cálculos" head
  fits, chart note on one line; P7 columns/clinic/frame/readers'-
  corner (disclosure + invitation visible)/golden sentences/teaser
  all clean; P8 test sections + all 150 keys end well above the
  footer band, dash style throughout.
- Final-render warnings: builder build6 log **0** FLOW OVERFLOW /
  HEAD TOO WIDE; my PT-build-copy rerun likewise **0**.

### Builder claims cross-check (summary)

- All builder claims verified true EXCEPT the implicit claim that the
  transform record reproduces the final edition (it does not — B-1).
  Verified true: 150 / levels / pages / types / writing 172; gloss
  10/33 per-call; P7 col3 1708.1 / teaser 2554.1; 12 shortened notes;
  3 comma restructurings; P5 caption; P7 B1 glossline adaptation
  ("Assim, «sábado à noite, 7 de novembro» vira 11月7日星期六晚上."
  — explanation-layer only, Chinese result string unchanged);
  zero final-render warnings; PDF sizes + pins.

---

## Non-blocking observations (NOT blocking items — do not mix into B-1)

1. **Registry type words "Associação" / "Escrita" do print — as
   section furniture, not registry leakage.** Literal count: "Complete
   a frase" 0, "Escolha múltipla" 0, "Escolha no contexto" 0,
   "Associação" 5, "Escrita" 2 in edition SVGs. Every one of the 7 is
   a section head or glossline ("D · 词语配对 · Associação" P2–P6,
   "F · 写一写 · Escrita", "Escrita — não há uma única resposta
   certa.") that appears **identically in the shipped W43
   same-pairing edition** (same 5+2, same positions) and is documented
   in the edition KIT §4 as the PT column's own forms. No exercise
   carries a registry type label; the 150-render check holds. The
   builder's "NONE print" wording is imprecise for these two single
   words; the substantive gate (no registry dump on pages) passes.
   Flagged only so the coordinator can tighten the wording next
   cycle.
2. **P6 key-points box is taller in PT** (height 175.4 vs core 145.675
   at (527, 723.0)) — Portuguese wrap growth, not a defect; occlusion
   0 flags, card clean.
3. **Web-PDF regen timestamp delta** — see Gate 9. Content-identical;
   only PIL CreationDate/ModDate differ.
4. **Freeze-baseline trailing diff exit code** — my own hash-file
   comparison exited 1 solely because the two hash files used
   different path prefixes (absolute vs relative); the hash values
   are identical. Re-verified with hash-only lists: identical
   before/after/now. Not a core-integrity issue.
5. **Golden-sentence rendered commas** — full-width ， forms in both
   core and edition (renderer conversion), not an edition change.
6. **Chip-count pattern** — P2–P6 show 14 standalone chips for 18
   exercises because grouped items share one chip (e.g. "25–28.");
   identical in core and W43; registry + P8 CLEAN prove numbering.
7. **Sibling agents observed** — FR and IT proofreaders ran concurrently
   in their own dirs during this proof; none wrote to the PT dirs
   (pre-flight snapshots confirm).

---

## Limitations (stated plainly)

- This proof verifies the fan-out against its core (frozen-target
  rule) and the W43 same-pairing furniture; it does **not** re-verify
  the core's facts/dates against external sources — those are
  inherited from the core, whose own KIT records `date -d`
  Asia/Shanghai verification (2026-11-02 Mon … 2026-11-08 Sun, etc.).
  A core fact error, if one existed, would pass through this fan-out
  proof by design.
- Visual inspection was at full-card resolution (1950×2700) plus one
  2× crop (P5 caption). Sub-pixel defects below card resolution were
  covered by the geometric audits, not by eye.
- No Discord, repo, `weekly-git`, `insert.py`, or main-chat action was
  taken (forbidden by the task); delivery readiness beyond this report
  (repo insert, pins) is the coordinator's step after a passing round.
- The transform repro repointed only the transform's `BUILD` path and
  the repro copy's `OUT` paths; no other transform content was altered.
  If the builder consolidates the fixes differently (e.g. different
  wording), the fresh proof round must re-run Gate 10 from the new
  transform, not assume it passes.

---

## Files produced by this proof (read-only elsewhere)

- This report:
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-pt-proof/REPORT.md`
- Scratch (all under the report's `work/` dir — snapshots, tool
  outputs, scripts, repro outputs, render regen):
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-pt-proof/work/`
  (snap1/snap2, diff.json, p8-compare.txt, occlusion.json,
  rowcheck.txt, checks1/2/3 outputs, furniture.txt,
  repro-vs-delivered.json, repro-run.log, ptbuild-run.log,
  render-regen.log, p5-caption-crop.png, core hash lists)

## Delivered-file pins (verified on the delivered files themselves)

- Print PDF `Lucerna-VOL2-PT.pdf`: 47,047,752 B, 8 pages, sha256
  `4190684793377b7ac853df3f190e048637323162f9dada01d74d23c613329872`
- Web PDF `Lucerna-VOL2-PT-web.pdf`: 3,252,004 B, 8 pages, sha256
  `0bc2e29083679ec6ce1acaeb27371174b6e4b95e97a560488a3968aba50500aa`
