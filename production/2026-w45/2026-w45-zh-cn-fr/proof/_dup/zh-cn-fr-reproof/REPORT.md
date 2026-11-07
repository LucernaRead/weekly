# W45 ZH-CN×FR — Independent RE-PROOFREAD: FULL ROUND

## Verdict: PASS — ZERO PROBLEMS

This is a complete independent re-proofread from scratch (all 16 gates in
the dispatch, not a delta check). All three blocking items from the first
proof (REPORT.md in `hidden_files/w45/zh-cn-fr-proof/`) are fixed and
re-verified; every other gate re-verified independently. The edition is
**finalized by this report as the coordinator's evidence for insert**.
No fix was made by this proofreader: everything below is read-only
except this report dir and its `work/` scratch. No weekly-git touch, no
insert.py run, no Discord delivery, no main-chat card/PDF delivery, no
cron, no shared-scratch cleanup, no subagent spawned. No content module
was ever imported inside the core build dir; all reproduction runs used
fresh copies with OUT repointed to proof scratch.

## Pre-flight (coordinator ruling applied: intent = NO CONCURRENT WRITER)

- (a) No live worker writing to the FR delivery/build dirs: at check
  time the only live weekly workers were a `zh-cn-pt` fix render and a
  `zh-cn-it` occlusion audit (different editions); `ps` greps for
  `zh-cn-fr|zhcn-fr` returned nothing throughout. PASS.
- (b) Mtime+hash snapshots of delivery + build dirs: snap1 08:09 UTC,
  snap2 08:10 UTC, close snap3 08:19 UTC — `HASH STABLE` and `MTIME
  STABLE` across the whole round (~10 min window snap1→snap3; snap1→
  snap2 alone was ~1 min, so the close snapshot is the load-bearing
  one). All delivery mtimes predate this session by 5+ min (last write
  08:03:57 UTC). PASS.
- (c) Fix session completed: fix-round.log, render-fix.log
  (08:03–08:07 UTC), KIT 08:07 UTC, all before this session. PASS.
- Pre-flight therefore PASSED and the full reproof ran.

## BLOCKING ITEMS — ALL RESOLVED (with evidence)

### B1 — P1 badge colour: FIXED ✓

- Delivered ED P1 badge node, measured: `x=975 y=434 font-size=19.5
  font-weight=700 fill=#a4553a` (brick), text
  « TEXTES EN CHINOIS SIMPLIFIÉ · EXPLICATIONS EN FRANÇAIS —
  L'ÉDITION POUR LES LECTEURS FRANCOPHONES » (unchanged).
- Three-way: W43 shipped same-pairing badge = same x/y/size/weight/
  text, `fill=#a4553a`; W45 core badge = same slot/size, `fill=#3e4c2a`
  (olive) with the core's own English text. Slot, size, colour all
  measured, not assumed. The ED KIT §IDENTITY "brick red #a4553a" claim
  is now TRUE. Source proof: pre-fix→post-fix source diff shows exactly
  one P1-rendering change, `content12.py:23` OLIVE→BRICK (see Gate 2).

### B2 — P8 answer-key style: FIXED ✓

- Delivered ED P8: paren style, 150/150 key-start lines each carrying
  exactly one `(`; 150 half-width `(` and 150 half-width `)` in the
  keys area; keys-area full-width parens = 0. The 11 full-width pairs
  in the whole P8 file are all in test stems (y<900, same 11 as the
  core), none in keys. W43 shipped same-pairing P8 measured the same
  way: 150/150 paren, full-width 11 (stems), half-width 150 — the ED
  now matches the W43 precedent exactly.
- Keys end baseline 2514.92, i.e. 65.08 px clear of the 2580 footer
  rule (unchanged from pre-fix 2514.9 modulo rounding).
- The 2 keys not ending in `)` on their first line (147, 149) are
  wrapped keys whose continuation lines close the paren
  (`attendre la prévente.)`, `dernier.)`) — same class as the first
  proof's wrapped 149, not a style deviation.
- 34 pinyin-only citations (39 keys) each adjudicated below (Gate 4);
  all preserve meaning, characters remain in stems.
- `tools/p8.py compare`: CLEAN, 150 = 150, missing = [], extra = 0,
  keydiff = [].

### B3 — Gate 10 literal reproduction: FIXED ✓

- Procedure (this round, fresh): pristine zh-cn core build copied to
  proof scratch + fr-build `transform.py` alone (exit 0, all counts
  asserted, "transform applied OK") + OUT/BASE repointed to proof
  scratch (expanduser form matched — see README #11 pitfall) + the
  build's own single-process `run.py` (exit 0; identical to fr-build's
  run.py by diff).
- Result: **8/8 SVGs byte-identical to the delivered post-fix SVGs**,
  zero `HEAD TOO WIDE` / `FLOW OVERFLOW` warnings, registry TOTAL 150
  (A2 56 / B1 69 / B2 25; pages 10/18/18/18/18/18/12/38; types 完成句子
  68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1), P7 col3 1706.6 /
  teaser 2552.6.
- Repaired `fixup1.py` exits 0 on solo sources: fresh core copy +
  REPL-only transform variant (exit 0) + repaired fixup1 → `fixup1 OK`,
  all entries found including the repaired `content12.py`
  "L'opération de la boutique WeChat dure 35 jours au total." entry
  (1×); the two identical band entries correctly skipped as no-ops.
- Discrepancy note (task-flagged, now moot): the first proof's B3
  header said solo 3/8 while its own differing-page list (p1, p2, p5,
  p6, p7, p8 differ) implies 2/8. The fix log's pre-fix solo baseline
  is 2/8, consistent with the differing-page list. The current Gate 10
  result (8/8) does not depend on which pre-fix figure was right, so
  this is recorded, not treated as a finding.

## PER-GATE EVIDENCE

### Gate 1 — Pre-flight + delivery hash verification at start AND close: PASS

- Start hashes (snap1) match the fix log's fix-post.sha on all 18
  files (8 SVGs, 8 cards, both PDFs); close hashes (snap3) identical
  to snap1 — zero changes during the round. Core SVGs unchanged at
  close (re-hash matches post-baseline hash).
- Pins (re-verified): print PDF 46,662,604 B, sha256
  `2f1dbc24cf5265564a0adee556c542cf0ca4cea24270daf6b1d0e9f7ed2c1969`;
  web PDF 3,265,050 B, sha256
  `107dbffeb82e97e9d4fe9f2fe78e51f871481f6e067ea5d188b2456eac29778d`;
  ABSTRACT.txt 436 B, sha256
  `6ed587554b3702e4006d546813993078af3274987da34c1f70841c8c2ddeef56`
  (untouched, mtime 07:23:22).

### Gate 2 — Scope verification: PASS

- Pre-fix (fix-prefixed.sha) vs post-fix (snap1) hashes: P2–P7 SVGs +
  P2–P7 cards byte-identical (12/12); only P1 SVG, P8 SVG, P1 card, P8
  card, and the two PDFs changed — exactly the fix round's claimed
  scope.
- P1: delivered badge node measured exactly as specified in B1 above.
  Stronger than the fix log's node-diff claim: a source diff of the
  first proof's pre-fix delivered-source copy (`zh-cn-fr-proof/work/
  repro/`) against the post-fix fr-build sources shows the ONLY
  P1-rendering change is `content12.py:23` OLIVE→BRICK. Every other
  content change is a registry-note string (rendered only in P8 keys)
  or the two `content8.py` key-format lines; `bslib4.py`, `svglib.py`,
  `run.py` byte-identical; `fixup1.py` differs only by its header note
  + the repaired entry. (OUT/BASE path lines differ only because the
  pre-fix copy lived in proof scratch.) Saved as
  `work/source-diff-pre-post.txt`.
- P8: changes fully accounted for — paren format (content8:119,121)
  + the 34-entry FIX_CJK conversion list. Source-diff hunk accounting:
  5 matching-list hunks × 4 keys + 19 single-note hunks = 39 keys,
  exactly the fix log's 39. P8 text-node count unchanged at 317.

### Gate 3 — B1 three-way: PASS (see B1; slot y=434, size 19.5 pt, colour #a4553a, all measured)

### Gate 4 — B2 P8 paren style + pinyin citations: PASS

- Paren metrics: key starts 150/150, half-width parens 150, keys-area
  full-width parens 0, keys end 2514.92 (65.08 px clear); `p8.py`
  CLEAN (150=150, keydiff[]). See B2.
- Each of the 34 pinyin-only citations adjudicated for meaning
  preservation (FIX_CJK list cross-checked: all 34 new fragments
  present in delivered P8, all 34 old CJK-citing fragments absent;
  rebuilt 150 keys: 0 with CJK inside the note parens):
  早上→zǎoshang, 立冬→lìdōng, 直降→zhíjiàng, 周六→zhōuliù,
  件→jiàn / 个→gè / 条→tiáo, 补冬→bǔdōng, 立减→lìjiǎn,
  现货→xiànhuò, 「最低价」→« zuìdījià » (French guillemets, the
  correct French quotation form), 内战→nèizhàn, 凌晨→língchén,
  地始冻→dì shǐ dòng, 总决赛→zǒngjuésài, 救赎→jiùshú,
  数字形象→shùzì xíngxiàng, 数据→shùjù, 毛衣→máoyī,
  水始冰→shuǐ shǐ bīng, 淘汰赛→táotàisài, 火化师→huǒhuàshī,
  瑞士轮→ruìshìlún, 票房→piàofáng, 结算页→jiésuàn yè,
  说法→shuōfǎ, 运费→yùnfèi, 雉入大水为蜃→zhì rù dà shuǐ wéi shèn.
  Every pinyin is the standard reading with correct tones; every
  cited word occurs in exercise stems outside the keys area
  (counts 2–79 per word; e.g. 立冬 79, 现货 38, 直降 20, 雉入大水为蜃
  4), so no citation loses its referent. The 5 dropped-character
  cases (e.g. `凌晨 língchén` → `língchén`, `bǔdōng 补冬` → `bǔdōng`)
  drop only a redundant duplicate where the pinyin was already
  present. NO citation loses meaning; nothing blocking.
- Freeze diff `--strict-cjk`: added CJK = 0 on every page, TOTAL 0,
  exit 0 (per-page +/− strings identical to the first proof:
  p1 +51/−46, p2 +65/−60, p3 +39/−37, p4 +41/−40, p5 +45/−41,
  p6 +43/−38, p7 +88/−82, p8 +184/−190). This independently confirms
  the paren conversion introduced no full-width paren CJK.

### Gate 5 — B3 Gate 10 documentation chain: PASS (see B3; transform exit 0, driver exit 0, fixup1 exit 0)

### Gate 6 — Freeze baseline: PASS

- `tools/freeze.py baseline` on the zh-cn core build: **8/8 SVGs
  byte-identical** to the shipped core (core hashes e057bbfc…,
  c87aa67e…, d50f09e1…, dd3b1b0f…, c71ef315…, b06a85d2…, f2319cb8…,
  eaf368f8…); core SVGs re-hashed afterwards, unchanged.

### Gate 7 — Occlusion audit + supplements: PASS

- `tools/occlusion_audit.py --selftest`: OK — all 6 planted classes
  fired exactly once, clean controls silent.
- Edition: **0 flags; core 0 flags; NEW vs core 0** (exit 0).
- Same-baseline ink-collision scan (builder's `rowcheck.py` copied to
  proof scratch, ED repointed): **0 same-baseline flags**.
- P6 chart-label element check: bars x=325, widths 810/537/480 px
  (3.0 px/yuan), value labels at x=1151/878/821 (= bar end + 16 px),
  identical to core; NO other rect exists in the chart band
  (y 900–1500) that could cover any label ink. PASS by element
  inspection, not just audit-clean.
- P7 geometry re-confirmed: col3 ends 1706.6, teaser baseline 2518.6
  → ends 2552.6 (27.4 px clear of 2580); core teaser-adjacent max text
  y 2520.1, comparable.

### Gate 8 — Gloss counts (split on `·`): PASS

- Rendered `gloss()` call strings split on `·` itself: core 33 = ED
  33, file by file (content12 12, content34 9, content56 12; content7
  0, content8 0). Rendered gloss boxes all use the `Note — ` prefix
  (10 lines, 0 exceptions).

### Gate 9 — P7 golden sentences: PASS

- All 8 phrases occur exactly 2× issue-wide (article page 1 + P7 1),
  verbatim, with correct page tags: 「不用等11月11日」 p.1;
  「下单就能发货」 p.2; 「先看结算页，再付款」 p.2;
  「水开始结冰」 p.3; 「三场都输了」 p.4; 「小局一场没赢」 p.4;
  「故事够不够好」 p.5; 「别以后，就现在」 p.5.

### Gate 10 — Images: PASS

- Placement: P1 1, P2 1, P3 2, P4 1, P5 1, P6 0, P7 0, P8 0 = 6
  photos, every credited image placed, no uncredited image embedded.
- Embedded payloads MD5-matched to core assets AND to both build asset
  dirs: locker 420c6150…, valley 550e463b…, frost d0b015bc…,
  dumplings e8d75277…, lanparty 6b8e9037…, popcorn a903e35f…
  (identical to the first proof's list).
- Credit lines match the core's `assets/CREDITS.md` Artist field
  verbatim (only the label is French, `Photo : `): P1 Map hobby CC0;
  P2 Paul Gilmore CC0; P3 Gerda Arendt CC0 + Syced CC0; P4 Syced CC0;
  P5 Based5290 public domain. File photos captioned 资料图; P4
  LAN-party caption states 2003/France.

### Gate 11 — Readers' corner: PASS

- Chinese disclosure span byte-identical in substance to the core
  (from 编辑部示例信 through 延期不是取消。, verified by span
  extraction, not line eyeballing).
- French disclosure present: « le VOL.1 avait promis de vraies
  lettres et la meilleure rédaction du VOL.1. Aucune n'est arrivée :
  voici encore un exemple de la rédaction. Reporté, pas annulé. »
- Letter labelled editor's example: « 编辑部示例信，不是真实来信 ».
  No reader, name, or quotation invented.
- Explicit open invitation INSIDE the corner, verbatim (French
  typographic space before `!`): « Écrivez-nous ! Envoyez votre
  lettre en chinois. » (confirmed in space-joined SVG text and in
  `content7.py` source; the dispatch's `Écrivez-nous!` spelling is
  the same string modulo that French space).

### Gate 12 — Furniture three-way: PASS

- Footers on all 8 pages verbatim from W43 modulo VOL.1→VOL.2:
  « Lucerna · HEBDOMADAIRE CHINOIS VOL.2 · TEXTE EN CHINOIS
  SIMPLIFIÉ · EXPLICATIONS EN FRANÇAIS ».
- Page lines « Page N sur 8 » ×8; P8 separators « — Page N — » ×8
  (identical to W43); P8 header + right line identical to W43;
  gloss prefix « Note — » everywhere; P1 edition line
  « HEBDOMADAIRE CHINOIS · VOL.2 · 双11 · 立冬 · S16 » at 40 pt
  y=330; subtitle at y=372 untouched
  (« 给学中文的人的周报 — Lire la vraie Chine, en chinois »);
  badge in the zh-cn family's in-place slot y=434 (neither the
  y≈372 subtitle-slot case nor the y=574 inserted case).
- Masthead « Lucerna » with no article (0 occurrences of
  « Le Lucerna » / « The Lucerna »). Banned intermediary term 0.
- Core-keys-end figure verified: core keys end baseline 2530.35
  (49.65 px clear) — confirming the first proof's correction of the
  builder's 2395 figure. ED keys end 2514.92 (65.08 px clear) — the
  ED ends HIGHER than the core with MORE clearance. The KIT now
  explicitly corrects the figure (KIT line 449: "not 2395").
- No discrepancies requiring adjudication; shipped W43 wins nowhere
  needed because nothing conflicts (tables.json NOT edited).

### Gate 13 — Web regen: PASS

- Build `render.py` copied to proof scratch with ED redirected to a
  scratch dir holding copies of the delivered SVGs (delivery dir
  never written): cards **8/8 byte-identical** to delivered cards;
  print PDF regenerated **byte-identical** (46,662,604 B, sha256
  `2f1dbc24…` = delivered pin, 8 pages).
- Web PDF: 8 pages, 3,265,050 B, same length as delivered; differs in
  exactly **8 bytes**, both inside the Pillow `/CreationDate` +
  `/ModDate` timestamps (builder 20261028080356Z vs my run
  20261028081741Z). All page/image content byte-identical. The web
  pin is therefore **run-specific by construction (content-identical,
  not byte-identical across runs)** — stated explicitly, not a
  defect (same conclusion as the first proof's N6).

### Gate 14 — Cards visual (all 8 eyeballed): PASS

- P1: brick badge, footer, boxes, photo+credit, quiz flow clean.
- P2: word cards, « Retenez la phrase » line clear of card 0,
  « Les dates » box fits, exercises 11–28 clean.
- P3: frost + dumpling photos + credits; gloss boxes; 29–46 clean.
- P4: LAN-party photo + 2003/France caption; S16 schedule box;
  47–64 clean.
- P5: « Mots de la semaine » title reads cleanly inside its box;
  popcorn photo + credit; 65–82 clean.
- P6: chart bars/labels fully visible, no clipping; « Les paniers »
  head fits; 83–100 clean.
- P7: A2/B1/B2 columns, error clinic (item 3 complete in context —
  see non-blocking N3), frame, readers' corner, phrases, VOL.3 teaser
  all fit with footer clearance.
- P8: test flow (113–150) + all 150 paren-form keys in 4 columns
  with « — Page N — » headers; pinyin citations render cleanly with
  half-width parens (e.g. key 14 « Après lìdōng… », key 106
  « 06 h 00 correspond à zǎoshang… », key 109 « « zuìdījià » »);
  keys end well clear of the footer; wrapped keys 147/149 sit inside
  their columns.
- No overflow, overlap, covered/clipped/struck-through text, or
  missing content on any page.

### Gate 15 — ABSTRACT.txt: PASS

- French single line (431 chars, 436 bytes, one trailing newline
  only), 0 ASCII double quotes, untouched since the build
  (sha 6ed58755…).
- Names the paper (Lucerna), the target language (chinois), the
  reader (lecteurs francophones), A2–B2, 150 questions, the real
  topic keywords (ventes de stock du Double 11 et remises directes,
  début de l'hiver le samedi 7 novembre, quarts de finale du Mondial
  S16 de League of Legends, film IA Sanxingdui Future Past, nouveau
  film We Only Have One Life) and a learner search phrase
  (« apprendre le chinois en lisant de vraies infos chinoises »).

### Gate 16 — First proof's non-blocking observations: CONFIRMED NON-BLOCKING

- N1 (core P8 figure): CLOSED by the fix round — the KIT now says
  "not 2395" and the corrected figures are verified above (core
  2530.35 / ED 2514.92). No edition change needed or made.
- N2 (shopping count): STILL OPEN in KIT prose only — the KIT still
  says "four apparatus strings" while the delivered SVGs contain 6
  "shopping" text nodes (P1 band sub ×1, P2 band sub + word-strip
  head + « appli de shopping » ×3, P7 A2 head + « mots du shopping »
  ×2). All are standard French usage (faire du shopping / appli de
  shopping / mots du shopping); the English-function-word scan over
  the final SVGs finds no English apparatus (only French « page »
  hits, e.g. « Réponses page 8 »). Substance passes; only the KIT
  count sentence is off. Genuinely non-blocking.
- N3 (P7 clinic item 3): confirmed complete in context on the P7 card
  (« Nombre + classificateur + nom. Le 个 est en trop. » directly
  under the corrected 「我买了三件毛衣」). No change required.
- N4 (gloss-box lines 10 vs W43 11): re-measured — W43 has 11
  (1+2+2+2+2+2), ED has 10. Content difference between issues, not a
  furniture deviation; prefix form identical. Non-blocking.
- N5 (core KIT visible-text totals): re-measured — core KIT's own
  figures are 23,038/26,765 vs the ED KIT's quoted core figures
  22,990/26,717. Counting-method prose note only; the freeze diff is
  authoritative and clean. Non-blocking.
- N6 (web-PDF timestamps): re-confirmed in this round's own regen
  (exactly 8 bytes, timestamps only). Documented, not a defect.
- None of N2/N4/N5/N6 is re-litigated as blocking: no genuine defect
  with evidence stands behind any of them.

## BUILDER (FIX-ROUND) CLAIMS — VERIFICATION TABLE

| Claim | Verdict |
|---|---|
| B1 one line OLIVE→BRICK, count 1; P1 node diff one fill attribute | CONFIRMED (source diff + node measurement; see Gate 2) |
| B2 paren-form key starts 150/150, half-width 150, full-width 0 (keys area), keys end 2514.92 / 65.08 px clear, p8 CLEAN | CONFIRMED exactly |
| B2 34 distinct notes / 39 keys converted, characters stay in stems, meaning preserved | CONFIRMED (item-by-item adjudication, Gate 4) |
| B3 fresh pristine core + new transform.py alone reproduces post-fix 8 SVGs 8/8, zero warnings | CONFIRMED (transform exit 0, driver exit 0) |
| B3 repaired fixup1 exits 0 on solo sources | CONFIRMED (`fixup1 OK` on REPL-only sources) |
| Scope: P2–P7 byte-identical pre/post; P1 changed, P8 changed | CONFIRMED (hash comparison, 12/12 identical) |
| New pins print 46,662,604 B sha 2f1dbc24…; web 3,265,050 B sha 107dbffb… (web run-specific) | CONFIRMED (print byte-identical on regen; web content-identical, timestamps only) |
| ABSTRACT.txt untouched sha 6ed58755… | CONFIRMED |

## NON-BLOCKING OBSERVATIONS (separate from the verdict — do not ship-block)

- NB1 — KIT "shopping appears in four apparatus strings" count is
  still wrong (true count 6 nodes; see Gate 16 N2). KIT prose only;
  the edition's French usage is correct. May be corrected in a later
  KIT touch-up; it does not block insert.
- NB2 — KIT visible-text core figures (22,990/26,717) vs core KIT's
  own (23,038/26,765) counting-method difference (see Gate 16 N5).
  KIT prose only; freeze diff is authoritative.
- NB3 — Web-PDF pin is run-specific by construction (Pillow
  timestamps; see Gate 13). The coordinator's insert step must pin
  the delivered file's bytes, not expect cross-run byte-identity for
  the web PDF (print PDF is deterministic).

## LIMITATIONS (stated plainly)

- French prose was inspected (full read of extracted SVG text + all 8
  cards) but not by a native-speaker reviewer; idiom/grammar judgment
  is inspection-level only.
- Dates, weekdays, facts, and figures were NOT re-sourced: they are
  inherited frozen target text from the already-finalized W45 zh-cn
  core (freeze diff proves zero target change). Re-verifying the
  core's trend/fact sources was out of scope for this fan-out reproof.
- Commons credits were verified against the core's `assets/CREDITS.md`
  Artist field (which records the Commons API verification of
  2026-10-27) and by payload MD5 identity — no fresh Commons API
  re-query was made in this round.
- insert.py was not run (forbidden to this proofreader) and repo
  lint/frontmatter conformance is for the coordinator's insert step;
  ABSTRACT.txt was checked for form (Gate 15) but not linted against
  the repo.
- No pre-fix P1 SVG file survives for a literal pre/post node diff;
  the P1 scope conclusion rests on the stronger combination of
  pre/post hash scope + the pre/post source diff + the byte-identical
  Gate 10 reproduction (see Gate 2).

## DELIVERY PINS (delivered files, re-verified at close)

- Print PDF `Lucerna-VOL2-FR.pdf`: 46,662,604 B, 8 pages, sha256
  `2f1dbc24cf5265564a0adee556c542cf0ca4cea24270daf6b1d0e9f7ed2c1969`
- Web PDF `Lucerna-VOL2-FR-web.pdf`: 3,265,050 B, 8 pages, sha256
  `107dbffeb82e97e9d4fe9f2fe78e51f871481f6e067ea5d188b2456eac29778d`
  (run-specific: content-identical across runs, timestamps differ)
- SVGs (8): p1 9dd64f21…, p2 d8f6bbdd…, p3 2cef9fea…, p4 cebc50b6…,
  p5 3823652c…, p6 948434f2…, p7 c54b6010…, p8 d72dac39…
  (full hashes in `work/snap1.sha` = `work/snap3.sha`)
- Cards (8): p1 31c28e46…, p2 23cb3fb1…, p3 258cce08…, p4 fd9b80d4…,
  p5 92c8cd6c…, p6 c46165da…, p7 da078cc2…, p8 550db561…
- Work evidence: `hidden_files/w45/zh-cn-fr-reproof/work/` (snapshots,
  diff.json, occlusion.json, rowcheck, gloss/chart/badge/P8-style
  measurements, Gate 10 repro + fixup1-solo dirs and logs, webregen
  dir and log, pre/post source diff)

## WHAT THE COORDINATOR MAY DO NOW

Insert the edition (repo insert step, with its own lint/frontmatter
checks). No further proof round is owed for B1/B2/B3: this report is
the fresh full-round zero-problem evidence. This report does not itself
insert, ship, or deliver anything.
