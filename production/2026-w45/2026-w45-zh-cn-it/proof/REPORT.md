# INDEPENDENT PROOFREAD — W45 ZH-CN × IT (Simplified Chinese target · Italian reader)

## VERDICT: NOT PASS

Two blocking items (below). The edition is **not finalized** and must not be
declared shipped. Per the task, the coordinator inserts only on a
ZERO-PROBLEMS round; this round found problems. Do NOT fix-and-ship on this
report alone — fix, re-render, and re-proof a full round from scratch.

## Blocking list

### B1. P8 key 135 note is in English, not Italian (explanation-layer defect)

- **Location:** `files/weekly-report-w45-zh-cn-it/svg/p8-ceyan.svg`, P8 keys,
  "— Pagina 8 —" group, and visibly on `cards/p8-ceyan.png` (right column,
  between Italian notes 134 and 136).
- **Delivered text (verbatim from the SVG node):**
  `135. 数字 (shùzì — the AI film's characters are digital images.)`
- **Why it blocks:** the explanation layer must be fully in the reader's
  native language. The P8 header itself asserts "Tutte le note in italiano"
  (all notes in Italian), and the edition KIT claims "every explanation
  element is Italian" — both false for this item. It is not a loanword or a
  proper name: it is a full English clause.
- **Root cause (verified in code):** the build's `scratch/transform.py`
  maps only the P5 exercise form
  `shùzì — the film's characters are digital images.` → Italian (ex 70,
  correctly Italian in the edition), but has NO mapping for the P8-key
  variant with "AI" (`content8.py:62`:
  `shùzì — the AI film's characters are digital images.`). The miss
  survived because `p8.py compare` compares keys, not note language
  (keydiff [] is still correct), and strict-CJK cannot see it (the note
  contains no CJK).
- **Scope check (this is the ONLY such item):** all-edition English-word
  scan over every added (explanation-layer) string found no other English
  prose; P8 core-vs-edition note comparison found only two identical
  notes — #94 (pure maths `199 − 20 = 179 yuan.`, language-neutral) and
  #135; every unchanged Latin-script string is frozen Chinese target text
  (AI, team codes, Lucerna, VOL). The neighbouring key 70 IS Italian
  (`i personaggi del film sono immagini digitali`), proving the intended
  translation.
- **Fix required:** translate the note to Italian (mirroring ex 70, e.g.
  `shùzì — i personaggi del film AI sono immagini digitali.`), re-render
  through the single-process driver, then run a FULL fresh proof round.

### B2. Gate 10 — transform-solo reproduction 0/8 (reproducibility failure)

- **What was run:** fresh copy of the zh-cn core build
  (`hidden_files/weekly-report-w45-zhcn-build/`) → copy of the build's
  `scratch/transform.py` placed at `<copy>/scratch/transform.py` →
  count-only (275 mappings, 434 replacements, zero zero-match aborts) →
  `apply` (422 replacements) → single-process `run.py`
  (content12 → 34 → 56 → 7 → 8) with OUT repointed to
  `hidden_files/w45/zh-cn-it-proof/work/repro-out/svg` (verified zero
  references to any real edition/core dir before running; core build dir
  never imported or executed in place).
- **Result:** all 8 reproduced SVGs DIFFER from the delivered SVGs
  (0/8 byte-identical). Registry from the repro run is IDENTICAL to the
  delivered edition (TOTAL 150, A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, types 68/50/20/11/1, writing model 172 chars) —
  so the divergence is purely the post-transform fix layer, itemized by
  freeze diff repro-vs-delivered (`work/repro-vs-delivered.json`):
  - P1/P2/P4/P5 box-title shortenings (Numeri della settimana;
    Date settimanali; Parole per la gara; Parole settimanali);
  - all five re-titled bands (Vita / Cultura / Giovani /
    Lettura approfondita / Focus sulla lingua — repro still prints
    Life / Culture / Youth / Deep read / Language focus);
  - P6 head shortening (`Calcoli` vs `Calcoli con i cesti`) — the repro
    run fires `HEAD TOO WIDE [P6-ex]` exactly as the builder's first
    render did;
  - P7 disclosure rewrite (repro keeps the core's Chinese disclosure
    sentences + transform.py's short Italian note; delivered has the full
    Italian disclosure with the invitation);
  - all 34 P8 pinyin notes (repro prints full-width parens with Han
    citations; delivered prints half-width parens with pinyin-only
    citations — the `pinyin_fix.py` layer).
- **Why it blocks:** the task's gate 10 requires transform.py ALONE to
  reproduce the delivered SVGs byte-for-byte, and states reproduction
  failure is BLOCKING. transform.py as shipped is stale: the builder's six
  self-fixed defect rounds were applied to the build copy but never folded
  back into it.
- **Nuance (recorded, not a waiver):** the BUILD directory itself DOES
  reproduce: a repointed copy of `hidden_files/weekly-report-w45-zh-cn-it-build/`
  run through `run.py` reproduces all 8 delivered SVGs byte-for-byte with
  ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings (`work/buildrepro-run.log`).
  So the KIT's claimed reproduction path (build `run.py`) is valid; what
  fails is the stricter gate-10 path (transform.py alone from a fresh
  core). Fix = fold the fix layer into transform.py (or ship
  pinyin_fix.py + the band/box/head/disclosure fix list as part of the
  reproduction record) and re-run gate 10 to 8/8, then re-proof fully.

## Pre-flight (duplicate check — PASSED, proof proceeded)

- No live process writing to the delivery dir
  (`files/weekly-report-w45-zh-cn-it/`), the it-build dir, or the core
  build dir at proof start (only an unrelated zh-cn-ru `render.py` was
  running; it touches neither target dir).
- mtime snapshots of all three dirs: snapshot 1 → snapshot 2 (a few
  minutes apart) = ZERO changes; final snapshot at end of proof
  (07:56 UTC) vs snapshot 1 = ZERO changes; delivery SHA-256s unchanged
  throughout (`work/mtime1.txt`, `work/mtime2.txt`, `work/mtime3.txt`,
  `work/delivery-hashes1.txt`, `work/delivery-hashes-final.txt`).
- Builder session completed before proof start (last delivery write
  07:37 UTC; proof began 07:38 UTC). Pre-flight conditions (a), (b), (c)
  all hold.

## Per-gate evidence

All commands run with `tools/venv/bin/python`. Work dir:
`hidden_files/w45/zh-cn-it-proof/work/` (report + logs + scratch copies;
nothing outside this dir was written; `~/workspace/weekly-git`,
insert.py, Discord, main-chat delivery, crons, shared scratch dirs, the
core build, the W43 edition, tools/, and the delivery dir were not
touched).

### Gate 1 — freeze baseline + diff: PASS (baseline 8/8, strict-CJK 0)

- `freeze.py baseline` on the core build: **8/8 SVGs byte-identical**
  (p1 e057bbfcdfcd6fca, p2 c87aa67eb6785a58, p3 d50f09e1a72b6fd3,
  p4 dd3b1b0fdc80627a, p5 c71ef3153d70701c, p6 b06a85d276db8a53,
  p7 f2319cb8997f8d36, p8 eaf368f8dca48dff — matching the builder's
  claimed hashes exactly); core SVGs re-hashed unchanged afterwards.
- `freeze.py diff --strict-cjk` core-vs-edition: per-page CJK
  851→815 / 1053→1031 / 812→790 / 810→789 / 944→922 / 1005→983 / 760→652 /
  1102→985; **added CJK = 0 on all 8 pages, TOTAL 0** (`work/diff.json`).
- Target-text zero-change adjudication: every added string containing CJK
  was inspected. All CJK runs in added strings occur in the core, except
  P8 model-answer wrap fragments (`我和妈妈一起`, `我去买了一件毛`, `巾`,
  `直降以后便宜了不少`, `的比赛`, `我又买了一条围`, `衣`) — verified as
  substrings of the core's frozen 172-character model answer, split at
  different wrap points because the "Risposta modello:" prefix shifts
  wrapping. No new target text. Removed CJK strings are exactly the
  explanation layer (English notes/furniture replaced by Italian, plus the
  P7 Chinese disclosure sentences replaced per the W43 Italian-only
  precedent — see gate 7).

### Gate 2 — p8.py compare vs core: PASS

- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-it
  --target zh-cn`: core 150 noted, edition 150 noted,
  **status CLEAN, missing=[] extra_count=0 uncertain=[] keydiff=[]**.
  P8 key numbers 1–150 complete, no gaps (independent SVG-node check).

### Gate 3 — occlusion audit + same-baseline + P6 chart: PASS

- `occlusion_audit.py --selftest` first: OK (all 6 planted classes fire,
  clean controls silent) — selftest would have refused conclusion on
  failure; it passed.
- Canonical audit on the edition: **0 flags**; with `--core`: core
  0 flags, **NEW vs core: 0** (`work/occlusion.json`).
- Same-baseline scan (builder's `scratch/rowcheck.py`, copied to my work
  dir and run from `tools/`): **same-baseline OVERLAP = 0**. The script's
  crude chart heuristic emits 13 CHART-GRAZE flags; see non-blocking
  observations — all adjudicated false positives by true-ink measurement.
- P6 element check (true ink boxes via PIL + real TTC faces, every
  earlier-drawn text vs every later-drawn rect on P6):
  **0 intersections**. Chart bars verified in the SVG rects: x=325,
  widths 810 / 537 / 480 px at y=1282 / 1340 / 1398, h=34 (KIT values
  exact). Labels clear: value "270 元" x[1151,1223.5] vs bar end 1135
  (16 px); "179 元" vs bar end 862 (16 px); "160 元" vs bar end 805
  (16 px); chart title ink ends y=1271.8 vs bar A top 1282 (10 px).

### Gate 4 — gloss counts (split on `·`): PASS

- 10 gloss() calls in both core and edition build code; items split on
  `·` itself: **core 33 = edition 33**, distribution identical
  (4,4,4 / 3,3,3 / 3,3,3,3 per content12/34/56). Rendered `Nota — `
  prefix counts match the call distribution (P1 1, P2 2, P3 2, P4 1,
  P5 2, P6 2; P7/P8 0).

### Gate 5 — P7 golden sentences: PASS

- All 8 phrases verbatim, each **exactly 2×** (article + P7) by
  node-concatenated page text (a naive space-joined count undercounts
  wrapped phrases — corrected method documented here): 「不用等11月11日」
  pp.1+7, 「下单就能发货」 pp.2+7, 「先看结算页，再付款」 pp.2+7,
  「水开始结冰」 pp.3+7, 「三场都输了」 pp.4+7, 「小局一场没赢」
  pp.4+7, 「故事够不够好」 pp.5+7, 「别以后，就现在」 pp.5+7.
  P7 tags read Pagina 1, 2, 2, 3, 4, 4, 5, 5 — matching the article
  pages and the core's counts exactly.

### Gate 6 — images: PASS

- 6 photos placed (P1 1, P2 1, P3 2, P4 1, P5 1, P6/P7/P8 0), every
  embedded payload **byte-identical (MD5) to the core's** in order and to
  the build asset files (locker/valley/frost/dumplings/lanparty/popcorn).
  Asset files themselves are MD5-identical between the core and it
  builds.
- Credit lines match the core with only the label translated
  (`Photo:` → `Foto:`): Map hobby, Paul Gilmore, Gerda Arendt, Syced ×2,
  Based5290 — verbatim from the core build `assets/CREDITS.md`, which
  records them as the Commons API Artist field (see Limitations: the API
  itself was not re-queried in this proof).

### Gate 7 — readers' corner: PASS

- Core's Chinese example letter byte-identical to the core:
  「你好！我住在上海。立冬那天，我吃了饺子，也给妈妈打了电话。双11，我买了一件毛衣，现货第二天就到了。」
- Italian disclosure on P7 (verbatim, node-joined): "Una lettera di
  esempio della redazione — non è una lettera vera. Il VOL.1 aveva
  promesso per questo numero le lettere vere dei lettori e il miglior
  tema del VOL.1: non è arrivato nulla, quindi l'invito resta aperto.
  Rimandato, non cancellato — mandateci le vostre lettere in cinese, le
  pubblicheremo!" — labels the editor's example, states no genuine
  letters exist, states the VOL.1 promise, and carries the EXPLICIT open
  invitation **verbatim** as required. (Per the W43 shipped precedent,
  the disclosure is Italian-only; the core's Chinese disclosure sentences
  were replaced, not kept alongside — the facts are fully preserved in
  Italian. The corner head reads "读者园地 · L'angolo dei lettori".)
- P7 teaser band rect bottom measured **2553.12**, footer rule 2580 →
  26.88 px clear; teaser text fits on one line inside the band (visually
  confirmed on the P7 card crop).

### Gate 8 — furniture three-way (core / W43 shipped / this edition): PASS, with two adjudications

- Badge: core's own badge at **y=434, 19.5pt** (olive, centred);
  W43 shipped zh-cn-it replaces it **in place, same y/size**; this
  edition identical string, same slot/size. **Adjudication (a): the
  zh-cn family in-place case is CONFIRMED on measurement** — not the
  FR/IT inserted-at-y=574 case, not a masthead-shift case. Masthead
  geometry untouched (wordmark 262, strap 330, strapline 372, badge 434
  all at core positions; only strap topics + strapline translation
  changed).
- Footer (all 8 pages): `Lucerna · SETTIMANALE CINESE SEMPLIFICATO VOL.2 ·
  TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO` (VOL follows
  the target core; otherwise identical to W43's VOL.1 footer).
  Page line: `Pagina N di 8` all pages. Gloss prefix: `Nota — `.
  P8 separators: `— Pagina N —` ×8, identical to W43 shipped.
  P8 header identical to W43
  (`答案 · Soluzioni — per pagina, con una nota per ogni risposta` /
  `Tutte le note in italiano · ✓ = il compito di scrittura`).
  P1 strap/strip/strapline: strip + strapline identical to W43; strap
  = weekly name + VOL.2 + this issue's topics (双11 · 立冬 · S16).
  Band titles identical to W43: 生活 · Vita, 文化 · Cultura,
  体育 · Sport, 青年 · Giovani, 深读 · Lettura approfondita,
  词语 · Focus sulla lingua, 测验与答案 · Test e soluzioni.
- **Adjudication (b) — P8 STYLE: PAREN is the correct family style.**
  (i) W43 zh-cn-it build code `content8.py:119`
  (`f"{e_['n']}. {e_['key']} ({e_['note']})"`) and `:121`
  (`f"{e_['n']}. ✓ ({e_['note']})"`) specify paren — builder's citation
  VERIFIED, line numbers exact. (ii) W43 shipped P8 SVG prints paren
  throughout (150 half-width-paren notes). (iii) This edition prints
  paren consistently (150 half-width-paren notes; full-width parens back
  to the core's 11, all inside frozen Chinese stems with contexts
  byte-identical to the core's). The W45 core's dash and the sibling
  W45 zh-cn editions' dash are therefore NOT a defect here: different
  natives may carry different shipped precedents (tools README #14 —
  verified from the family's shipped fan-out build code, not from the
  core's rendered SVG alone, and not merely on the builder's citation).
- Writing entry: key `(domanda aperta — modello qui sotto)` in the
  edition build `content8.py:103`, byte-identical to the W43 IT form;
  rendered key `150. ✓ (Domanda aperta — il modello è nella sezione F
  di questa pagina, 172 caratteri)`; model answer 172 characters
  verified from the rendered SVG, identical text to the core model.

### Gate 9 — web PDF regeneration: PASS (with timestamp caveat)

- Build `render.py` copied to my scratch with BASE redirected
  (`work/webregen/`), run over copies of the delivered SVGs:
  cards **8/8 byte-identical** to delivered; print PDF **byte-identical**
  (SHA-256 `799d95f49840fe69fa7d89f6eef8bde0313d7aaeab91111c2ab4a43e3c1777cc`,
  matching the KIT pin exactly); web PDF **8 pages, 3,262,614 bytes
  (< 10 MB)**, delivered file SHA-256
  `93e8056d1a6ce7d839fcf8915cf84c1127ee980e45dcad475e982bd269527d66`
  matching the KIT pin exactly.
- Regenerated web PDF differs from delivered by exactly 8 bytes, all
  inside `/CreationDate` / `/ModDate` timestamps (07:34:40Z vs 07:51:37Z
  — the regeneration time); same length, same pages, otherwise
  byte-identical. This is PIL PDF timestamp metadata, not a content
  difference, and it is why a regenerated web PDF can never match the
  KIT SHA unless timestamps are pinned. Recorded here as a caveat, not a
  defect: the delivered file's size + SHA match the KIT pins exactly.

### Gate 10 — transform solo reproduction: FAIL (blocking, see B2)

- 0/8 byte-identical; divergence itemized under B2. (Build-dir
  reproduction separately verified 8/8 — see B2 nuance.)

### Gate 11 — all 8 cards visual: PASS on layout (B1 visible on P8 card)

- All 8 cards read in full, plus crops (P1 top band, P7 bottom, P8
  bottom, P8 keys-rule area). Furniture, boxes, flows, answer blocks all
  clean: no overflow, no overlap, no missing content, no footer
  intrusion on any page. Specific visual adjudications:
  - P8 keys flow: last key lines (150, 111) sit visibly clear above the
    footer rule with blank space (see non-blocking observations). The
    builder's "visibly above the footer rule" claim is CONFIRMED on the
    card, not just on the number.
  - P8 top rule: test flow ends, gold rule, then keys header — clean,
    no line struck through (same adjudication class as the core's
    top-rule note).
  - P7 teaser band: single line, fully inside the dark band, clear gap
    to the footer rule.
  - P6 chart: bars, row labels, and value labels all clear of each
    other; no clipped label.
  - P8 card visibly shows B1: key 135's English note stands out among
    Italian notes — this is how the defect presents on the page.

## Builder claims — verification summary

| Claim | Verdict |
|---|---|
| Freeze baseline 8/8, core unchanged | CONFIRMED (hashes match exactly) |
| Freeze diff strict-CJK 0, per-page CJK counts | CONFIRMED exactly |
| P8 CLEAN 150=150, keydiff [] | CONFIRMED |
| Occlusion 0 / NEW 0 | CONFIRMED |
| Gloss 10 calls, 33=33 | CONFIRMED |
| P7 phrases 8× exactly 2× | CONFIRMED (with corrected counting method) |
| Images byte-identical per page | CONFIRMED |
| P7 teaser ends 2553.12 (footer rule 2580) | CONFIRMED (rect bottom measured) |
| P8 keys end y=2545 vs bottom 2540, last line visibly above footer rule | CONFIRMED on the card (see observations) |
| Pinyin discipline: 34 notes, full-width parens back to core's 11, strict-CJK 0 | CONFIRMED (spot-checked citations: zhíjiàng, ruìshì lún, zǒngjuésài, táotài sài, zuìdījià, máoyī/jiàn/gè/tiáo, língchén, zǎoshang, zhōuliù) |
| Italian/English-coinciding words + proper names classification | CONFIRMED, except B1 (a genuine English note, not a loanword) |
| Five re-titled bands, no English band title remains | CONFIRMED (Life/Culture/Youth/Deep read/Language focus/Test & keys/Quick quiz/Top story/Briefs/Contents/Word of the week/This week in numbers all ABSENT) |
| P7 disclosure rewritten concise, still states example + invitation, teaser clears footer | CONFIRMED |
| Registry TOTAL 150, A2 56/B1 69/B2 25, pages 10/18/18/18/18/18/12/38, writing 172 | CONFIRMED (via both repro driver runs + core KIT + P8 150=150) |
| Writing key mirrors W43 IT | CONFIRMED |
| Zero FLOW OVERFLOW / HEAD TOO WIDE on final render | CONFIRMED for the build-dir reproduction (zero warnings); the transform-solo repro DOES fire HEAD TOO WIDE (expected — it lacks the P6 head fix) |
| "Every explanation element is Italian" | REFUTED by B1 (key 135) |
| Transform.py as reproduction record | REFUTED by B2 (stale — missing the fix layer) |

## Non-blocking observations (NOT defects; do not mix into the blocking list)

1. **P8 keys-flow end (y=2545 vs nominal bottom 2540):** judged on the
   card, not the number. Last key ink baseline is y=2530.48 (item 111),
   ink bottom ≈2534.5, footer rule at 2580 → ~45 px clear; the
   occlusion audit reports no FOOTER flag; the P8 bottom crop shows
   clear blank space between the last key line and the footer rule.
   Same adjudication as the core's P8 top-rule proximity note. Not a
   defect.
2. **Rowcheck raw output (13 CHART-GRAZE flags):** all are false
   positives of that script's crude baseline-proximity heuristic
   (baselines ~33 px above rect tops, ink well clear). The true-ink
   test over all P6 text-vs-later-rect pairs returns 0, and
   same-baseline OVERLAP = 0. The builder's "0 grazes" claim is
   understood as adjudicated true grazes = 0, which this proof
   confirms. Not a defect.
3. **"in stock" / "merce in stock" phrasing:** Italian commercial
   loanword usage ("vendite in stock", "merce in stock"), used
   consistently across the gloss and notes; classified as Italian, not
   an English leftover. Not a defect.
4. **Web PDF regeneration SHA:** differs from the delivered file only in
   CreationDate/ModDate timestamps (see gate 9). Not a defect.
5. **ABSTRACT.txt:** single Italian line naming the real topics
   (Doppio 11, Lidong/Inizio dell'inverno 7 novembre, S16, Sanxingdui AI
   film, film invernale), the learner phrase "impara il cinese leggendo
   notizie vere in cinese", masthead, target language, A2–B2 levels and
   150 exercises. Conforms to SOP §9. Minor note only: the abstract
   writes "Lidong" without tone marks, while the paper uses "lìdōng" —
   a toneless romanization in the abstract alone, not a defect.
6. **P7 disclosure replacement (not alongside):** the core's Chinese
   disclosure sentences do not appear in the edition; the disclosure is
   Italian-only per the W43 shipped precedent, with all facts preserved
   in Italian. This matches the task's gate-7 substance (labeled
   example + no-genuine-letters statement + explicit invitation, all
   present). Not a defect.

## Limitations (stated plainly)

- The Commons API Artist field was NOT re-queried live in this proof
  (no live-browser/API route is available to this subagent). Credit
  lines were verified as verbatim matches to the core build's
  `assets/CREDITS.md`, which records the 2026-10-27 API check
  (`extmetadata` Artist + LicenseShortName), and to the core's rendered
  credit lines with only the `Photo:` → `Foto:` label changed.
- Registry level/page/type counts were verified via the two repro
  driver runs (both produced identical stats), the core KIT, and the
  P8 CLEAN 150=150 gate — not via an independent registry dump taken
  from the delivered SVGs alone.
- Italian copy was checked by full SVG-text extraction, targeted
  English-word scans, and card reading; this is not a line-by-line
  Italian grammar copy-edit of every sentence beyond the gates' scope.
  (That scope is sufficient to catch B1-class defects: the scans cover
  every explanation string.)
- Pre-flight snapshots 1→2 were a few minutes apart; the longer
  snapshot 1→3 window (~18 minutes, zero changes) is what most strongly
  supports "builder session completed, no concurrent writer".

## Files

- This report:
  `hidden_files/w45/zh-cn-it-proof/REPORT.md`
- Evidence under `hidden_files/w45/zh-cn-it-proof/work/`:
  `mtime1/2/3.txt`, `delivery-hashes1/final.txt`,
  `core-hashes-before/after.txt`, `diff.json`, `occlusion.json`,
  `rowcheck.py`, `rowcheck-out.txt`, `repro-vs-delivered.json`,
  `transform-count.log`, `transform-apply.log`, `repro-run.log`,
  `buildrepro-run.log`, `webregen/` (regen cards + PDFs),
  `repro-build/` + `repro-out/` (transform-solo repro),
  `buildrepro/` + `buildrepro-out/` (build-dir repro),
  `crops/` (p7-bottom, p8-bottom, p1-top, p8-keysrule).

## PDF pins (delivered files, verified)

- Print: `Lucerna-VOL2.pdf`, 46,262,380 bytes, 8 pages, SHA-256
  `799d95f49840fe69fa7d89f6eef8bde0313d7aaeab91111c2ab4a43e3c1777cc`
- Web: `Lucerna-VOL2-web.pdf`, 3,262,614 bytes, 8 pages, SHA-256
  `93e8056d1a6ce7d839fcf8915cf84c1127ee980e45dcad475e982bd269527d66`
