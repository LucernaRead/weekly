# INDEPENDENT RE-PROOFREAD — W45 ZH-CN × IT (Simplified Chinese target · Italian reader)

## VERDICT: PASS — ZERO PROBLEMS

Full round re-verified from scratch against the post-fix delivery. Both
blocking items from the first proof (REPORT.md in
`hidden_files/w45/zh-cn-it-proof/`) are fixed and independently confirmed;
every other gate re-verified, not copied. This report is the finalization
evidence for the coordinator's insert step. (This proofreader fixed nothing,
touched no delivery/build file, ran no insert, posted nothing anywhere.)

## Pre-flight (duplicate check — PASSED, proof proceeded)

- (a) No live worker/process writing to the delivery dir
  (`files/weekly-report-w45-zh-cn-it/`) or the it-build dir at proof start
  (only unrelated workers, e.g. a zh-cn-es reproof webregen, none touching
  the it dirs).
- (b) mtime snapshots of both dirs: snapshot 1 → snapshot 2 (3 minutes
  apart) = ZERO changes; snapshot 1 → snapshot 3 (end of round) = ZERO
  changes (`work/mtime1.txt`, `work/mtime2.txt`, `work/mtime3.txt`).
- (c) Fix session completed before proof start (FIXLOG.md filed; last
  delivery write 08:08–08:10 UTC, proof began after).
- Delivery SHA-256s unchanged throughout the round
  (`work/delivery-hashes1.txt` == `work/delivery-hashes-final.txt`).

## Per-gate evidence

All commands run with `tools/venv/bin/python`. Work dir:
`hidden_files/w45/zh-cn-it-reproof/work/` (nothing outside it was written;
`~/workspace/weekly-git`, insert.py, Discord, main-chat delivery, crons,
shared scratch dirs, the core build, the W43 edition, tools/, and the
delivery dir were not touched; no subagent spawned; no content module was
ever imported inside the core build dir).

### Gate 1 — Pre-flight + delivery hash verification: PASS

Start and close hashes identical (see PDF pins below). Sizes: print PDF
46,262,363 B; web PDF 3,262,810 B; P8 SVG hash
`70e28a68cd1266ddbb3786f2a0520bad20edfb17c4f66334762b2ede8e774d58`;
P8 card hash
`54c826e360a687eba8ea1bf30a0749c1cbb918cd659374a766686fa8e76f95dd`.

### Gate 2 — Change-set verification: PASS

Programmatic comparison of the live delivery against the fix log's
pre-fix (`fixlog/prefix-hashes.txt`) and post-fix
(`fixlog/postfix-hashes.txt`) tables: P1–P7 SVGs and P1–P7 cards are
byte-identical to PRE-fix; exactly three other files differ from pre-fix
and match POST-fix — P8 SVG, P8 card, both PDFs. Nothing else changed.
The P8-only claim was further proven by reconstruction (see Gate 4 note):
a fresh core + fixed transform minus the single B1 mapping reproduces
ALL 8 pre-fix hashes exactly, including pre-fix P8
`d4f4cb95ca3f33b1b5f5b13cc8cc578467747de8755facf3210685ab6297e3d3`.

### Gate 3 — B1 (P8 key 135 Italian note): PASS

- Delivered P8 SVG node, verbatim:
  `135. 数字 (shùzì — i personaggi del film AI sono immagini digitali.)`
  at x=1451, y=2059.70 — also visibly on the P8 card, right column,
  between Italian notes 134 and 136.
- Mirror verified: it-build `content56.py:81` (the P5 exercise 70
  definition) reads
  `shùzì — i personaggi del film sono immagini digitali.`; the same
  Italian form is the delivered P8 key 70 node
  (`70. 数字 (shùzì — i personaggi del film sono immagini digitali.)`).
  The B1 form inserts `AI` after `film` for the AI-film variant — the
  meaning (the AI film's characters are digital images) is preserved,
  and the paren style `数字 (shùzì — [Italian clause])` is preserved.
- Fix location verified in code: `scratch/transform.py` line 310, phase 1,
  immediately after the ex-70 mapping, with the comment
  "B1 fix (2026-10-28): P8-key AI variant, missed by the ex-70 mapping
  above" — a mapping inside the transform, not a post-hoc edit.
- Zero reflow (genuine pre→post node diff, reconstructed pre-fix P8 vs
  delivered P8 — see Gate 4 note): 330 nodes both, EXACTLY ONE changed
  node (node 310, key 135), identical x/y; neighbours 134 (y=2030.47)
  and 136 (y=2088.93) byte-identical; last key continuation ends
  y=2528.98; footer rule 2580.

### Gate 4 — B2 Gate 10 (documentation chain): PASS

Fresh copy of the zh-cn core build
(`hidden_files/weekly-report-w45-zhcn-build/`) + the fixed
`scratch/transform.py` ALONE (placed at `<copy>/scratch/transform.py`),
content-file OUT paths repointed in the copy only (expanduser form;
`render.py` was not executed — its core BASE reference remains in the
copy but was never run), then one-process `run.py`
(content12 → 34 → 56 → 7 → 8):
- transform count-only exit 0; transform apply exit 0; `run.py` exit 0.
- Phase counts verified from my own run logs (`work/gate10-*.log`):
  phase 1 = 276 mappings / 423 replacements; phase 2a = 11 entries /
  11 replacements; phase 2b = 34 entries / 39 replacements;
  TOTAL = 473.
- Result: gate10-out SVGs **8/8 byte-identical** to the NEW delivered
  SVGs (hashes in `work/gate10-hashes.txt`).
- Warnings: **zero** `FLOW OVERFLOW` / `HEAD TOO WIDE` in the run log.
- Registry from the run: TOTAL 150, A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, types 完成句子 68 / 单选 50 / 词汇配对 20 /
  完形单选 11 / 写作 1; writing model 172 characters.
- Core integrity: core SVGs re-hashed before/after the Gate 10 run —
  unchanged (`work/core-hashes-before.txt` ==
  `work/core-hashes-after.txt`).
- Note (reconstruction, not a waiver): removing ONLY the B1 mapping
  line from the fixed transform and re-running the same pipeline
  reproduces the fix log's pre-fix hashes 8/8 (phase 1 = 275 mappings /
  422 replacements, total 472, run exit 0, zero warnings), which is what
  made the genuine pre→post P8 node diff in Gate 3 possible. The
  pre-fix P8 SVG file itself was not archived in the fix log (only its
  hash); the reconstruction is validated by that hash match, not assumed.

### Gate 5 — Header-claim truth: PASS

- P8 header claim `Tutte le note in italiano` is now true. Scope check
  redone: comparing P8 note CONTENT (format-stripped) core-vs-edition,
  the only note identical to the core is #94, pure maths
  (`199 − 20 = 179 yuan.` — delivered `94. 179 (199 − 20 = 179 yuan.)`,
  core `94. 179 — 199 − 20 = 179 yuan.`), language-neutral. The former
  second identical note, #135, is now Italian.
- Distinctive-English-word scan over the joined text of all 8 NEW SVGs:
  NONE on any page (the word `film` occurs — it is the Italian noun
  `film`, e.g. `Il film AI`, `Film AI e un film d'inverno` — not an
  English leftover; it was excluded on that ground, as in the first
  proof's loanword classification).
- Old English #135 string
  (`the AI film's characters are digital images`) absent from all 8 SVGs.

### Gate 6 — Freeze baseline + strict-CJK diff: PASS

- `freeze.py baseline` on the core build: **8/8 SVGs byte-identical**
  (p1 e057bbfcdfcd6fca, p2 c87aa67eb6785a58, p3 d50f09e1a72b6fd3,
  p4 dd3b1b0fdc80627a, p5 c71ef3153d70701c, p6 b06a85d276db8a53,
  p7 f2319cb8997f8d36, p8 eaf368f8dca48dff — matching the first
  proof's hashes exactly); core SVGs re-hashed unchanged afterwards.
- `freeze.py diff --strict-cjk` core-vs-edition (`work/diff.json`):
  per-page CJK 851→815 / 1053→1031 / 812→790 / 810→789 / 944→922 /
  1005→983 / 760→652 / 1102→985; **added CJK = 0 on all 8 pages,
  TOTAL 0** (exit 0). The 34 pinyin conversions hold: P8 full-width
  parens are back to the core's 11, all inside frozen Chinese stems
  (see Gate 7 note). Any added CJK would have been blocking; there is none.

### Gate 7 — p8.py + paren style: PASS

- `p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-it
  --target zh-cn`: core 150 noted, edition 150 noted, **status CLEAN,
  missing=[] extra_count=0 uncertain=[] keydiff=[]** (`work/p8.json`,
  `work/p8.log`).
- Paren style verified as the correct family style: W43 zh-cn-it build
  `content8.py` lines 119/121 specify
  `f"{e_['n']}. {e_['key']} ({e_['note']})"` and
  `f"{e_['n']}. ✓ ({e_['note']})"`; W43 shipped P8 prints paren for
  all 150 keys (188 keyed nodes incl. wrapped continuations, 150
  paren-form); this edition likewise 150 paren-form keys, and its 11
  full-width-paren nodes are exactly the core's 11 frozen stems
  (also 11 on W43 shipped P8). The W45 core's dash and sibling
  editions' dash are NOT a defect here.

### Gate 8 — Occlusion audit + same-baseline + P6 chart: PASS

- `occlusion_audit.py --selftest`: OK (all 6 planted classes fire,
  clean controls silent).
- Canonical audit on the edition: **0 flags**; with `--core`: core
  0 flags, **NEW vs core: 0** (`work/occlusion.json`).
- Same-baseline scan (it-build `scratch/rowcheck.py`, copied to my work
  dir): **same-baseline OVERLAP = 0**; the script's 13 CHART-GRAZE
  lines are the known false-positive class (baselines ~33–39 px above
  the rect tops, ink well clear — same adjudication as the first proof).
- P6 chart-label element check (true ink boxes via PIL + real TTC
  faces): chart rects x=325, widths 810 / 537 / 480 px at y=1282 /
  1340 / 1398, h=34 (KIT values exact); value labels clear by exactly
  16 px each — "270 元" ink x[1151.0, 1223.5] vs bar end 1135;
  "179 元" ink x[878.0, 947.5] vs bar end 862;
  "160 元" ink x[821.0, 890.8] vs bar end 805.

### Gate 9 — Gloss counts (split on `·`): PASS

- 10 `f.gloss()` calls in both the core build and the it-build code;
  items split on `·` itself: **core 33 = edition 33**, distribution
  identical (content12: 4,4,4; content34: 3,3,3; content56: 3,3,3,3),
  headwords equal item-by-item in order.
- Rendered `Nota — ` prefix counts match: P1 1, P2 2, P3 2, P4 1,
  P5 2, P6 2; P7/P8 0.

### Gate 10 — P7 golden sentences: PASS

- All 8 phrases verbatim, each **exactly 2×** by node-concatenated page
  text (the first proof's corrected method — a naive space-joined count
  undercounts wrapped phrases): 「不用等11月11日」 pp.1+7,
  「下单就能发货」 pp.2+7, 「先看结算页，再付款」 pp.2+7,
  「水开始结冰」 pp.3+7, 「三场都输了」 pp.4+7,
  「小局一场没赢」 pp.4+7, 「故事够不够好」 pp.5+7,
  「别以后，就现在」 pp.5+7.
- P7 tags read Pagina 1, 2, 2, 3, 4, 4, 5, 5 — matching the article
  pages and the core's counts exactly (visible on the P7 card).

### Gate 11 — Images: PASS

- 6 photos placed (P1 1, P2 1, P3 2, P4 1, P5 1, P6/P7/P8 0), every
  embedded payload **byte-identical (MD5) to the core's** in order,
  and all 6 asset files MD5-identical between the core and it builds
  (locker/valley/frost/dumplings/lanparty/popcorn).
- Credit lines match the core with only the label translated
  (`Photo:` → `Foto:`): Map hobby, Paul Gilmore, Gerda Arendt,
  Syced ×2, Based5290 — verbatim from the core build
  `assets/CREDITS.md`, which records them as the Commons API Artist
  field (see Limitations: the API itself was not re-queried in this
  proof).

### Gate 12 — Readers' corner: PASS

- Core's Chinese example letter byte-identical to the core (visible on
  the P7 card): 「你好！我住在上海。立冬那天，我吃了饺子，也给妈妈打了电话。双11，我买了一件毛衣，现货第二天就到了。」
- Italian disclosure on P7 (space-joined node text, verbatim):
  "Una lettera di esempio della redazione — non è una lettera vera.
  Il VOL.1 aveva promesso per questo numero le lettere vere dei
  lettori e il miglior tema del VOL.1: non è arrivato nulla, quindi
  l'invito resta aperto. Rimandato, non cancellato — mandateci le
  vostre lettere in cinese, le pubblicheremo!" — labels the editor's
  example, states no genuine letters exist, states the VOL.1 promise,
  and carries the explicit open invitation **verbatim**. Corner head:
  "读者园地 · L'angolo dei lettori".
- P7 teaser band rect bottom measured **2553.12**, footer rule 2580 →
  26.88 px clear; teaser text fits on one line inside the band
  (visually confirmed on the P7 card).

### Gate 13 — Furniture three-way (core EN · W43 it · this edition): PASS

- Badge MEASURED on all three P1s: core's own badge at **y=434,
  19.5pt**; W43 shipped zh-cn-it replaces it **in place, same y/size**;
  this edition identical string, same slot/size:
  `TESTI IN CINESE SEMPLIFICATO · SPIEGAZIONI IN ITALIANO —
  L'EDIZIONE PER I LETTORI ITALIANI` at (975, 434), 19.5pt. The
  zh-cn family in-place case is CONFIRMED on measurement — not the
  FR/IT inserted-at-y=574 case, not a masthead-shift case. Masthead
  geometry untouched (wordmark 262, strap 330, strapline 372, badge 434
  all at core positions; only strap topics + strapline translation
  changed). P1 card visually confirms the badge in place.
- Footer (all 8 pages):
  `Lucerna · SETTIMANALE CINESE SEMPLIFICATO VOL.2 · TESTI IN CINESE
  SEMPLIFICATO · SPIEGAZIONI IN ITALIANO` (VOL follows the target core;
  otherwise identical to W43's VOL.1 footer). Page line:
  `Pagina N di 8` all pages. Gloss prefix: `Nota — `.
  P8 separators: `— Pagina N —` ×8, identical to W43 shipped.
  P8 header identical to W43
  (`答案 · Soluzioni — per pagina, con una nota per ogni risposta` /
  `Tutte le note in italiano · ✓ = il compito di scrittura`).
  P1 strap/strip/strapline: strip + strapline identical to W43; strap
  = weekly name + VOL.2 + this issue's topics (双11 · 立冬 · S16).
  Band titles identical to W43: 生活 · Vita, 文化 · Cultura,
  体育 · Sport, 青年 · Giovani, 深读 · Lettura approfondita,
  词语 · Focus sulla lingua, 测验与答案 · Test e soluzioni; the five
  re-titled bands carry no English title (Life/Culture/Youth/Deep
  read/Language focus all ABSENT from the delivered text).
- P8 key-flow end (first proof's pending item, RESOLVED): the nominal
  flow bottom 2540 vs the flagged 2545 is a flow-parameter number, not
  ink. Measured ink: last key baseline y=2530.48 (item 111), key-150
  continuation y=2528.98, footer rule 2580 → ~49–51 px clear; the
  occlusion audit reports no FOOTER flag; the P8 card shows clear blank
  space between the last key line and the footer rule. Not a defect.
- Writing entry: rendered key
  `150. ✓ (Domanda aperta — il modello è nella sezione F di questa
  pagina, 172 caratteri)`; model answer 172 characters, identical text
  to the core model (Gate 4 registry + P8 CLEAN).

### Gate 14 — Web regen: PASS (with timestamp caveat)

- Build `render.py` copied to my scratch with BASE redirected
  (`work/webregen/`), run over copies of the delivered SVGs:
  cards **8/8 byte-identical** to delivered; print PDF **byte-identical**
  (SHA-256 `612959385fedcfd660f0892efe6964007b2aa8a14a5dffafa137b743f05a4efa`,
  matching the KIT pin exactly); web PDF **8 pages, 3,262,810 bytes**
  (same length as delivered).
- Regenerated web PDF differs from delivered by exactly **8 bytes, all
  inside `/CreationDate` / `/ModDate` timestamps** (delivered
  `20261028080842Z` vs regeneration `20261028082535Z` — the
  regeneration time); same length, same pages, otherwise byte-identical.
  This is PIL PDF timestamp metadata, not a content difference, and it
  is why a regenerated web PDF can never match the KIT SHA unless
  timestamps are pinned. Recorded here as a caveat, not a defect: the
  delivered file's size + SHA match the KIT pins exactly
  (`work/webregen-compare.txt`, `work/webregen.log`).

### Gate 15 — All 8 cards visual: PASS

All 8 cards read in full (P1, P2, P3, P4, P5, P6, P7, P8). Furniture,
boxes, flows, answer blocks all clean: no overflow, no overlap, no
missing content, no footer intrusion on any page. Specific visual
adjudications:
- P8 keys flow: last key lines sit visibly clear above the footer rule
  with blank space; key 135's note is now Italian among Italian notes.
- P8 top rule: test flow ends, gold rule, then keys header — clean.
- P7 teaser band: single line, fully inside the dark band, clear gap
  to the footer rule; readers'-corner disclosure fully legible with
  the invitation verbatim.
- P6 chart: bars, row labels, and value labels all clear of each
  other; no clipped label; head `Calcoli` fits.
- P1 masthead/badge: badge in place under the strapline, no overprint.

### Gate 16 — ABSTRACT.txt: PASS

Single Italian line (453 bytes, trailing newline, no ASCII double
quotes) naming the real topics (Doppio 11 shopping race with vendite
in stock and sconti diretti, Lidong / Inizio dell'inverno sabato
7 novembre, quarti di finale dei Mondiali S16 di League of Legends,
il film fatto con l'AI Sanxingdui, il nuovo film invernale), the
learner search phrase "impara il cinese leggendo notizie vere in
cinese", the paper name Lucerna, the target language (cinese
semplificato, per lettori italiani), levels A2–B2, and 150 esercizi.
Conforms to SOP §9. (Same minor note as the first proof, not a defect:
the abstract writes "Lidong" without tone marks while the paper uses
"lìdōng" — a toneless romanization in the abstract alone.)

## Builder claims — verification summary

| Claim | Verdict |
|---|---|
| B1 fixed as a phase-1 mapping in transform.py, mirror ex 70 + `AI` | CONFIRMED (line 310, right after ex-70 mapping; delivered node verbatim) |
| B1 fit: zero FLOW OVERFLOW, 330 nodes both, exactly one changed node, key 135 y = 2059.70 both, neighbours unchanged, zero reflow, last key line ends y = 2528.98 vs footer rule 2580 | CONFIRMED (genuine reconstructed pre→post node diff) |
| B2 fixed by folding the fix layer into transform.py in two phases (2a 11 literals, 2b 34 pinyin literals) | CONFIRMED (phase counts from my own run: 11/11, 34/39) |
| Gate 10 fresh core + fixed transform alone = 8/8 byte-identical, exits 0/0/0, zero warnings, phase 1 = 276/423, total 473, registry 150 | CONFIRMED exactly |
| Change set: P1–P7 SVGs + cards byte-identical to pre-fix; only P8 SVG + P8 card + both PDFs differ, solely via key 135 | CONFIRMED programmatically against prefix/postfix tables |
| New pins: print 46,262,363 B sha 61295938…, web 3,262,810 B sha 742c01ca…, P8 SVG sha 70e28a68…, P8 card sha 54c826e3… | CONFIRMED (full hashes in PDF pins below) |
| Mechanical gates green (occlusion 0 + NEW 0, p8 CLEAN, gloss 33, registry 150, 0 warnings) | CONFIRMED |
| Header claim "Tutte le note in italiano" now true; distinctive-English-word scan NONE on all 8 new SVGs; old English #135 absent | CONFIRMED (with the `film` = Italian noun note in Gate 5) |
| Everything else from the first proof's pass list | RE-VERIFIED above (freeze, p8, occlusion, gloss, golden, images, corner, furniture, abstract, cards) |

## Non-blocking observations (NOT defects; do not mix into the verdict)

1. **Rowcheck raw output (13 CHART-GRAZE flags):** all are false
   positives of that script's crude baseline-proximity heuristic
   (baselines ~33–39 px above rect tops, ink well clear). The true-ink
   test (occlusion audit 0 flags + the P6 element check in Gate 8)
   and same-baseline OVERLAP = 0 confirm no real graze. Not a defect.
2. **"in stock" / "merce in stock" phrasing:** Italian commercial
   loanword usage, consistent across gloss and notes; classified as
   Italian, not an English leftover. Not a defect.
3. **Abstract "Lidong" without tone marks:** see Gate 16. Not a defect.
4. **P7 disclosure replacement (not alongside):** the core's Chinese
   disclosure sentences do not appear in the edition; the disclosure is
   Italian-only per the W43 shipped precedent, with all facts preserved
   in Italian. Not a defect.
5. **Web PDF regeneration SHA:** differs from the delivered file only in
   CreationDate/ModDate timestamps (see Gate 14). Not a defect.
6. **Gate 10 copy's `render.py`:** the fresh-core copy still contains
   the core BASE reference in `render.py`, which was never executed in
   this proof (only `run.py` was run, with OUT repointed in the content
   files). No write to any real dir occurred (core hashes unchanged).
   Not a defect, recorded for method transparency.

## Limitations (stated plainly)

- The Commons API Artist field was NOT re-queried live in this proof
  (no live-browser/API route is available to this subagent). Credit
  lines were verified as verbatim matches to the core build's
  `assets/CREDITS.md`, which records the 2026-10-27 API check
  (`extmetadata` Artist + LicenseShortName), and to the core's rendered
  credit lines with only the `Photo:` → `Foto:` label changed.
- The pre-fix P8 SVG file itself was not archived in the fix log (only
  its SHA-256). The genuine pre→post node diff in Gates 2–3 rests on a
  reconstruction (fixed transform minus the single B1 line) that
  reproduces the recorded pre-fix hash 8/8 — strong evidence, stated
  here rather than presented as a direct archived-file diff.
- Italian copy was checked by full SVG-text extraction, targeted
  English-word scans, and card reading; this is not a line-by-line
  Italian grammar copy-edit of every sentence beyond the gates' scope.
  (That scope is sufficient to catch B1-class defects: the scans cover
  every explanation string.)
- Registry level/page/type counts were verified via the Gate 10 driver
  run, the core KIT, and the P8 CLEAN 150=150 gate — not via an
  independent registry dump taken from the delivered SVGs alone.

## Files

- This report:
  `hidden_files/w45/zh-cn-it-reproof/REPORT.md`
- Evidence under `hidden_files/w45/zh-cn-it-reproof/work/`:
  `mtime1/2/3.txt`, `delivery-hashes1/final.txt`,
  `core-hashes-before/after.txt`, `analyze.py` + `analyze-out.txt`,
  `analyze2.py` + `analyze2-out.txt`, `analyze3.py` +
  `analyze3-out.txt`, `diff.json`, `occlusion.json`,
  `occlusion-selftest.log`, `p8.json`, `p8.log`, `rowcheck.py`,
  `rowcheck-out.txt`, `freeze-baseline.log`, `freeze-diff.log`,
  `gate10-build/` + `gate10-out/` + `gate10-count/apply/run.log`,
  `gate10-hashes.txt`, `recon-prefixed-build/` +
  `recon-prefixed-out/` + `recon-count/apply/run.log`,
  `p8-nodediff.txt`, `webregen/` + `webregen.log` +
  `webregen-compare.txt`.

## PDF pins (delivered files, re-verified)

- Print: `Lucerna-VOL2.pdf`, 46,262,363 bytes, 8 pages, SHA-256
  `612959385fedcfd660f0892efe6964007b2aa8a14a5dffafa137b743f05a4efa`
- Web: `Lucerna-VOL2-web.pdf`, 3,262,810 bytes, 8 pages, SHA-256
  `742c01caaa149105addc903dd08739b3c143a6314c973471a0c934c4bed4b621`
