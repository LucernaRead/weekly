# W45 ZH-CN×FR — Independent Proofread: FULL ROUND (re-dispatch)

## Verdict: NOT PASS — 3 blocking items (itemized below)

This is a complete independent proofread (11 gates + all builder-claim
verifications + both adjudications). The edition is **not finalized** by
this report. The coordinator must not insert it until the 3 blocking
items are fixed, the edition is fully re-rendered, and a fresh full
proof round returns zero problems. No fix was made by this proofreader:
everything below is read-only except this report dir and its `work/`
scratch. No weekly-git touch, no insert.py run, no Discord delivery,
no main-chat card/PDF delivery, no cron, no shared-scratch cleanup.

## Pre-flight (coordinator ruling applied, NOT the literal 30-min window)

- (a) No live worker writing to the FR delivery/build dirs: the only
  live weekly worker at check time was a `render.py` in
  `weekly-report-w45-zh-cn-de-build` (PID 6902, a different edition);
  `ps` greps for `zh-cn-fr|zhcn-fr` returned nothing. PASS.
- (b) Two mtime+hash snapshots of the delivery dir, the zh-cn core
  build dir, and the fr build dir, ~3.5 min apart (07:32 → 07:35 UTC):
  `SNAP STABLE`, `HASH STABLE`. PASS.
- (c) Builder session completed (KIT 07:27 UTC, render5.log 07:23 UTC;
  completion handoff 07:28 UTC). PASS.
- Pre-flight therefore PASSED and the full proof ran. (The prior
  attempt's stand-down note in this dir is superseded by this report.)

## BLOCKING ITEMS (each must be fixed + re-proofed)

### B1 — P1 badge COLOR deviates from the W43 shipped same-pairing edition (KIT claim false)

- Delivered ED P1 badge node: `x=975 y=434 font-size=19.5
  font-weight=700 fill=#3e4c2a` (olive), text
  « TEXTES EN CHINOIS SIMPLIFIÉ · EXPLICATIONS EN FRANÇAIS —
  L'ÉDITION POUR LES LECTEURS FRANCOPHONES ».
- W43 shipped same-pairing P1 badge node: same x/y/size/weight/text,
  but `fill=#a4553a` (brick red).
- W43 FR build code (`hidden_files/weekly-report-zhcn-fr-build/
  content12.py:23`): `p.text(975, 434, "TEXTES …", 19.5, "sans", True,
  BRICK, anchor="middle")`. W45 core code (line 23): same call with
  `OLIVE`. The ED transform replaced only the badge TEXT and kept the
  core's OLIVE constant (`fr-build/content12.py:23`).
- The ED KIT §IDENTITY claims the badge is "brick red #a4553a bold".
  That claim is FALSE for the delivered SVG. No KIT justification for
  olive exists — the KIT asserts brick — so this is an unnoticed
  carryover, not a deliberate pair-varying change.
- Fix: change the P1 badge colour constant OLIVE → BRICK on that one
  line, re-render, re-proof. (Slot/size/text adjudication (a) itself
  PASSES — see Gate 8.)

### B2 — P8 answer-key style deviates from the W43 shipped same-pairing edition (builder's justification false)

- Delivered ED P8: dash style, 150/150 key lines
  (`1. 10 — Ventes de stock JD.com dès le 12 octobre.`, …,
  `150. ✓ Tâche ouverte — modèle section F, 172 caractères`).
- Shipped W43 zh-cn×fr P8 SVG: PAREN style, 150/150 key lines
  (`1. 12 (JD.com a ouvert ses ventes en stock le 12 oct.)`, …,
  `150. ✓ (Question ouverte — le modèle est dans la section F …)`).
  Measured directly from the shipped SVG: dash-count 1 (a wrapped
  continuation fragment), paren-count 150.
- W43 FR build code (`content8.py:119,121`): paren
  (`f"{e_['n']}. {e_['key']} ({e_['note']})"`,
  `f"{e_['n']}. ✓ ({e_['note']})"`). W43 FR KIT §IDENTITY's
  paren-style sentence is therefore CONFIRMED by shipped SVG + code.
- The ED KIT §3 claim that "the shipped W43 vol1 core and W43 fr P8
  SVGs both print dash style" is FALSE for the W43 FR SVG. (The W43
  vol1 CORE is indeed dash — 149/149 — which is exactly why the W43 FR
  fan-out's deliberate dash→paren change is the same-pairing precedent
  that matters here, per tools README #14: bracket form follows the
  family's shipped fan-out code.)
- The ED kept the W45 core's dash code byte-identical. That is the
  core-following argument, but the KIT's stated justification for
  keeping dash rests on the false W43-SVG claim, so no valid
  pair-varying justification stands. Under Gate 8's rule (furniture
  verbatim from W43 shipped same-pairing unless justified), dash is
  an unjustified deviation.
- Fix: change the key format to paren in fr-build `content8.py:119,121`
  (mirroring W43 FR), re-render, re-proof. Helpful facts for the fix:
  ED's 150 printed notes currently contain ZERO internal parentheses,
  so the W43 FR no-internal-paren constraint is already satisfied;
  BUT ED notes (unlike W43 FR's) contain cited CJK words, so the
  re-proof must check the paren render for any widening/oddity around
  CJK-adjacent parentheses.

### B3 — Gate 10 literal transform-solo reproduction FAILS (3/8)

- Procedure: fresh copy of the pristine zh-cn core build +
  fr-build `transform.py` alone (exit 0) + OUT redirected to proof
  scratch + single-process `run.py` (exit 0).
- Result: only 3/8 SVGs reproduce (p3-wenhua, p4-tiyu match).
  p1, p2, p5, p6, p7, p8 DIFFER. Solo-run geometry: P7 col3 ends
  1881.12, teaser ends 2727.12 — i.e. the known build-1 state with the
  teaser past the footer band, not the delivered 1706.6 / 2552.6.
- Cause (proven by source diff): `transform.py` (mtime 07:04) predates
  all fixups. The final sources differ from transform-only sources in
  ~40 lines = documented fixup1 (band titles, 3 missed English notes,
  4 comma rewordings, head shortenings, P8 shortenings) + fixup2 (20
  note shortenings, P7 col3 cuts) + fixup3 (5 occlusion strings, no
  script) + the final P7 corner-note cut (no script). Additionally,
  saved `fixup1.py` exits 1 on a stale entry: it expects
  `L'opération de la boutique WeChat dure 35 jours au total.` in
  `content56.py`, but that string never exists there (content56's note
  has no "in total"; the "au total" entry belongs to content12 and is
  correctly present in fixup2). The script applies its other
  replacements before reporting FAILED, so the builder's own run hit
  the same benign failure.
- Qualification (important, does not waive the gate): the FULL build
  record DOES reproduce the edition — transform + fixup1 + fixup2 +
  the 6 documented final strings (5 fixup3 strings + corner cut),
  run through the single-process driver, reproduces the delivered 8
  SVGs BYTE-FOR-BYTE (8/8 MATCH, zero FLOW OVERFLOW / HEAD TOO WIDE,
  P7 col3 1706.6 / teaser 2552.6, registry TOTAL 150 / A2 56 / B1 69 /
  B2 25 / pages 10/18/18/18/18/18/12/38 / types 68/50/20/11/1 /
  writing 172). The delivered artifact is therefore genuine, not
  hand-tweaked — but no single script regenerates it from pristine
  core, which is what Gate 10 requires.
- Fix: fold every fixup into `transform.py` (or ship a `reproduce.sh`
  that runs transform + fixups in order) so a fresh core copy + one
  script reproduces the delivered SVGs; re-proof must re-run Gate 10
  literally.

## PER-GATE EVIDENCE

### Gate 1 — Freeze baseline + diff: PASS (with the B3 qualification)

- `tools/freeze.py baseline` on the zh-cn core build: **8/8 SVGs
  byte-identical** to the shipped core; core SVGs re-hashed
  afterwards, unchanged (hashes match pre-run snapshot).
- `tools/freeze.py diff --strict-cjk` core-vs-edition: **added CJK = 0
  on every page, TOTAL 0, exit 0** (p1 +51/−46, p2 +65/−60, p3 +39/−37,
  p4 +41/−40, p5 +45/−41, p6 +43/−38, p7 +88/−82, p8 +184/−190
  strings). Every removed-CJK string was inspected: all are
  apparatus (bilingual section heads, gloss strings, P8 notes,
  footers/page markers, band titles, clinic/frame notes, model-answer
  wrap fragments) — no article-body target text removed or altered.
  No adjudication needed (added CJK = 0, not merely cited words).

### Gate 2 — p8.py compare: PASS

- `tools/p8.py compare --core-dir …zhcn-core --edition-dir …zh-cn-fr
  --target zh-cn`: **CLEAN, 150 = 150, missing = [], extra = 0,
  keydiff = []**.
- Style verified from code, never memory: core `content8.py:119`
  `f"{e_['n']}. {e_['key']} — {e_['note']}"` (dash),
  `121` writing `f"{e_['n']}. ✓ {e_['note']}"`; ED code identical at
  both lines, only notes translated. Registry-only #150 change
  verified: ED key `(question ouverte — modèle ci-dessous)` vs core
  `(开放题，范文如下)`; printed form is `150. ✓ Tâche ouverte —
  modèle section F, 172 caractères` in both the SVG text nodes and
  the P8 card — the key itself never prints, so the change is truly
  registry-only and invisible on paper (mirrors W43 FR's #150 change).
  Every keydiff item was verified from SVG nodes (there are none).

### Gate 3 — Occlusion audit + supplements: PASS

- `tools/occlusion_audit.py --selftest`: OK — all 6 planted classes
  fired exactly once, clean controls silent.
- `occlusion_audit.py <edition> --core <core>`: **0 flags; core 0
  flags; NEW vs core 0** (exit 0). Builder's occlusion5/occlusion5-core
  JSON (0/0) independently reproduced.
- Same-baseline ink-collision scan (builder's `rowcheck.py`, copied to
  proof scratch, ED path repointed): **0 same-baseline flags**
  (furniture bands incl. P1 top band covered).
- P6 chart-label element check (sub-30% COVER blind spot, README #12):
  bars x=325, widths 810/537/480 px (3.0 px/yuan), value labels at
  x=1151/878/821 (= bar end + 16 px) — identical to core; NO other
  rect exists in the chart band (y 900–1500) that could cover any
  label ink. PASS by element inspection, not just audit-clean.
- Builder-claim re-measurements: P7 col3 ends 1706.6, teaser ends
  2552.6 (27.4 px clear of the 2580 footer line) — reproduced exactly
  in my independent run; P7 teaser last text baseline 2518.6 + line
  pitch = 2552.6, consistent. P8 keys end baseline 2514.9 (65.1 px
  clear of the 2580 footer rule) — reproduced exactly; see
  non-blocking observation N1 for the core-comparison correction.
- 5 French-length overflows (fixup3) confirmed fixed: occlusion 0
  flags now; P1 numbers-box title, P1 calendar line, P2 dates-box
  title, P2 word-card 0 spill, P5 words-box title all render inside
  their boxes on the cards.

### Gate 4 — Gloss counts (split on `·` itself): PASS

- Rendered `gloss()` call strings split on `·` (never on ` · `),
  counted from build sources and cross-checked against rendered
  gloss boxes (`Note — ` lines): core 33 = ED 33, box by box —
  content12 4+4+4, content34 3+3+3, content56 3+3+3+3 (P1 4, P2 4+4,
  P3 3+3, P4 3, P5 3+3, P6 3+3 as KIT states). All ED gloss boxes use
  the `Note — ` prefix (10 rendered gloss-box lines, 0 exceptions).

### Gate 5 — P7 golden sentences: PASS

- All 8 phrases occur exactly 2× in reading-order-joined SVG text
  (article + P7), verbatim and contiguous, with correct page tags,
  identical to the core: 「不用等11月11日」 p.1; 「下单就能发货」
  p.2; 「先看结算页，再付款」 p.2; 「水开始结冰」 p.3;
  「三场都输了」 p.4; 「小局一场没赢」 p.4; 「故事够不够好」 p.5;
  「别以后，就现在」 p.5. Each phrase's article occurrence sits on
  its tagged page (verified per page, not just issue-wide).

### Gate 6 — Images: PASS

- Placement in rendered SVGs: P1 1, P2 1, P3 2, P4 1, P5 1, P6 0,
  P7 0, P8 0 = 6 photos, every credited image placed, no uncredited
  image embedded.
- Credit lines match the Commons API Artist field from the core's
  `assets/CREDITS.md` verbatim (only the label is French, `Photo : `
  per W43 shipped same-pairing): P1 Map hobby CC0; P2 Paul Gilmore
  CC0; P3 Gerda Arendt CC0 + Syced CC0; P4 Syced CC0; P5 Based5290
  public domain.
- Embedded payloads decoded from the ED SVGs and MD5-matched to core
  assets: locker 420c6150…, valley 550e463b…, frost d0b015bc…,
  dumplings e8d75277…, lanparty 6b8e9037…, popcorn a903e35f…
  (fr-build asset files MD5-identical to core assets). File photos
  captioned 资料图; P4 LAN-party caption states 2003/France.

### Gate 7 — Readers' corner: PASS (mandatory gate fully met)

- Core disclosure frozen: Chinese part byte-identical in substance
  (VOL.1 promise, none arrived, no publishable submission, editor's
  example still printed, 延期不是取消）.
- French disclosure present in the reader's own language:
  « le VOL.1 avait promis de vraies lettres et la meilleure
  rédaction du VOL.1. Aucune n'est arrivée : voici encore un exemple
  de la rédaction. Reporté, pas annulé. »
- Letter labelled editor's example: « 编辑部示例信，不是真实来信 ».
  No reader, name, or quotation invented.
- Explicit open invitation INSIDE the corner, verbatim:
  « Écrivez-nous ! Envoyez votre lettre en chinois. »
  (Not a teaser line, not another page's exercise prompt — the
  VOL.3 teaser is a separate band and was not counted.)

### Gate 8 — Furniture three-way: STRINGS PASS, COLOUR + P8 STYLE FAIL (B1, B2)

- Badge slot adjudication (a): RULED IN-PLACE SLOT. Measured:
  core badge y=434, 19.5 pt, OLIVE; W43 shipped badge y=434,
  19.5 pt, BRICK; ED badge y=434, 19.5 pt, OLIVE. Text identical in
  ED and W43. Subtitle untouched at y=372 (19 pt, French half
  « Lire la vraie Chine, en chinois » matching W43). This is neither
  the EN/DE/ES y≈372 subtitle-slot case nor the FR/IT y=574 inserted
  case — the zh-cn family in-place slot at y=434 is the correct
  precedent, and the ED uses it. Slot/size/text PASS; colour FAILS
  (B1).
- P8 style adjudication (b): RULED PAREN (see B2). Shipped W43 SVGs
  are paren, confirming W43 KIT prose; builder's dash claim refuted.
- All other furniture strings verbatim from W43 shipped same-pairing
  (VOL.1→VOL.2 only): footers on all 8 pages
  « Lucerna · HEBDOMADAIRE CHINOIS VOL.2 · TEXTE EN CHINOIS SIMPLIFIÉ
  · EXPLICATIONS EN FRANÇAIS »; page lines « Page N sur 8 » ×8;
  gloss prefix « Note — »; P8 separators « — Page N — » ×8; P1
  edition line « HEBDOMADAIRE CHINOIS · VOL.2 · 双11 · 立冬 · S16 »
  40 pt y=330; P8 header
  « 答案 · Réponses — par page, avec une note pour chaque réponse »
  + right line « Toutes les notes en français · ✓ = l'exercice
  d'écriture » (both identical to W43). Masthead « Lucerna » with no
  article (0 occurrences of « Le Lucerna » / « The Lucerna »).
  Banned intermediary term 0 occurrences.

### Gate 9 — Web PDF regeneration: PASS (with timestamp caveat)

- Build's `render.py` copied to proof scratch with ED redirected to a
  scratch dir holding copies of the delivered SVGs (delivery dir
  never written): cards 8/8 byte-identical to delivered cards;
  print PDF regenerated byte-identical
  (46,662,483 B, sha256
  `d5f8fe4fe8983fdd4b0105061b918a56ecc5709be960e90728bb2c589f9e3331`
  = KIT pin, 8 pages).
- Web PDF: 8 pages, 3,259,655 B (< 10 MB). Delivered file matches its
  KIT pin (`dc3f70448d3d894d0342bcddb263d4681621c2ec89d13ac4d00789c5c390535f`).
  My regenerated web PDF differs in exactly 8 bytes — the Pillow
  `/CreationDate` + `/ModDate` timestamps (builder 20261028072300Z
  vs my run 20261028074724Z). All page/image content is
  byte-identical. Byte-identity across runs is therefore impossible
  for the web PDF by construction (Pillow embeds the current time);
  the regeneration is substantively exact and the delivered pin is
  self-consistent. This is NOT counted as a defect.

### Gate 10 — Transform solo reproduction: FAIL (B3); full-record reproduction: 8/8

- See B3. Literal solo: 3/8. Full record
  (transform + fixup1 + fixup2 + 6 documented strings, single-process
  driver, OUT redirected): 8/8 byte-identical, zero warnings,
  registry stats reproduced exactly. Delivered + core SVGs re-hashed
  after all proof runs: unchanged from the pre-flight snapshot.

### Gate 11 — Cards visual (all 8 eyeballed): PASS

- P1: badge/footer/boxes/photo+credit/quiz flow clean; no overflow.
- P2: word cards, « Retenez la phrase » line clear of card 0;
  « Les dates » box fits; exercises 11–28 flow clean.
- P3: frost + dumpling photos + credits; gloss boxes; exercises
  29–46 clean.
- P4: LAN-party photo + 2003/France caption; S16 schedule box;
  exercises 47–64 clean.
- P5: « Mots de la semaine » title reads cleanly — measured ink end
  954.0 vs border 961 = 7.0 px margin (builder's 7.1 px confirmed
  within rounding); popcorn photo + credit; exercises 65–82 clean.
- P6: chart bars/labels fully visible, no clipping (see Gate 3);
  « Les paniers » head fits; exercises 83–100 clean.
- P7: A2/B1/B2 columns, error clinic, frame, readers' corner,
  phrases, VOL.3 teaser all fit with footer clearance; clinic item 3
  judged complete in context (see N3); teaser band clear of footer.
- P8: test flow (113–150) + all 150 keys in 4 columns with
  « — Page N — » headers; keys end well clear of the footer rule on
  the card (measured 65.1 px); the lower placement vs the builder's
  claimed core figure is addressed in N1 — visually acceptable,
  readable, no footer contact. One wrapped key (149, 2 lines) sits
  inside its column.
- No overflow, overlap, covered/clipped/struck-through text, or
  missing content observed on any page.

## BUILDER CLAIMS — VERIFICATION TABLE

| Claim | Verdict |
|---|---|
| P7 col3 1706.6, teaser 2552.6 (27.4 px clear) | CONFIRMED exactly (independent run) |
| P8 keys end 2514.9, 65.1 px clear | CONFIRMED for ED; core comparison corrected (see N1). Placement judged ACCEPTABLE on the card (clear + readable) |
| P5 title margin 7.1 px | CONFIRMED (7.0 px by my PIL measure, rounding); reads cleanly |
| P7 clinic item 3 terse note complete enough | JUDGED COMPLETE (see N3) |
| "Shopping" = standard French borrowing, not English remnant | CONFIRMED in substance; count corrected (see N2) |
| Registry-only #150 key change, invisible on paper | CONFIRMED (printed `150. ✓ …` carries no key) |
| 4 full-width commas reworded, strict-CJK diff clean 0 | CONFIRMED (final diff TOTAL added CJK 0; comma rewordings found in fixup1) |
| 5 French-length overflows fixed, 0 flags now | CONFIRMED (occlusion 0, NEW 0, rowcheck 0) |
| Registry TOTAL 150, A2 56/B1 69/B2 25, pages 10/18/18/18/18/18/12/38, writing model 172 | CONFIRMED (independent driver run + model char count = 172 exactly) |
| Zero FLOW OVERFLOW / HEAD TOO WIDE on final render | CONFIRMED (0 in independent full-record run log) |
| Print 46,662,483 B sha d5f8fe4f…; web 3,259,655 B sha dc3f7044… | CONFIRMED (delivered files match KIT pins; print regen byte-identical; web regen content-identical, timestamps only) |
| Badge "brick red #a4553a" | REFUTED — delivered badge is olive #3e4c2a (B1) |
| "Shipped W43 SVGs are dash" (P8) | REFUTED — shipped W43 P8 is paren 150/150 (B2) |
| Transform-solo reproduction (implied by KIT reproduction section) | REFUTED as a solo claim — 3/8 only (B3); full-record 8/8 |

## NON-BLOCKING OBSERVATIONS (separate from blocking items — do not ship-block on these alone)

- N1 — Builder's core P8 figure is wrong, artifact is fine: the KIT
  says ED keys sit "LOWER than the core's 2395". Measured from the
  shipped SVGs, the CORE's keys end at baseline 2530.35 — i.e. the ED
  (2514.9) actually ends HIGHER than the core with MORE footer
  clearance (65.1 px vs core 49.7 px). The KIT sentence should be
  corrected on rebuild, but the ED's P8 placement needs no change.
- N2 — "Shopping" count: the KIT says 4 apparatus strings; the
  delivered SVGs contain 6 text nodes with "shopping" (P1 band sub
  ×1, P2 band sub + word-strip head + « Quatre mots… appli de
  shopping » ×3, P7 A2 head + « Les mots du shopping… » ×2). All
  are standard French usage (faire du shopping / appli de shopping /
  mots du shopping), and the English-function-word scan finds no
  English apparatus. Substance passes; only the KIT count is off.
- N3 — P7 clinic item 3 (« Nombre + classificateur + nom. Le 个 est
  en trop. ») is terse but complete: the corrected sentence
  「我买了三件毛衣」 sits directly above it and carries the 件 point;
  the note states the order rule + the extra-个 diagnosis. Kept as
  is; no change required.
- N4 — ED gloss-box rendered line count (10) vs W43 (11) is a content
  difference (different gloss boxes in a different issue), not a
  furniture deviation; the prefix form is identical.
- N5 — Core KIT visible-text totals quoted in the ED KIT
  (22,990/26,717) differ slightly from the core KIT's own figures
  (23,038/26,765) — a counting-method note, not edition content;
  the freeze diff is authoritative and clean.
- N6 — Web-PDF timestamp non-determinism (Gate 9): Pillow embeds
  CreationDate/ModDate, so no two web-PDF runs are byte-identical.
  Documented, not a defect.

## LIMITATIONS (stated plainly)

- French prose was inspected (full read of extracted SVG text + all 8
  cards) but not by a native-speaker reviewer; idiom/grammar judgment
  is inspection-level only.
- Dates, weekdays, facts, and figures were NOT re-sourced: they are
  inherited frozen target text from the already-finalized W45 zh-cn
  core (freeze diff proves zero target change). Re-verifying the
  core's trend/fact sources was out of scope for this fan-out proof.
- insert.py was not run (forbidden to this proofreader) and repo
  lint/frontmatter conformance is for the coordinator's insert step;
  ABSTRACT.txt was checked for form (single French line, 431 chars,
  no ASCII double quotes, real topics + learner phrase + masthead +
  target language + A2–B2 + 150 questions) but not linted against
  the repo.
- The P8 paren-style fix (B2) will need its own re-proof attention:
  ED notes contain cited CJK words (unlike W43 FR's CJK-free notes),
  so the re-proof must confirm half-width parens render correctly
  around CJK-adjacent text.

## DELIVERY PINS (delivered files, verified)

- Print PDF `Lucerna-VOL2-FR.pdf`: 46,662,483 B, 8 pages, sha256
  `d5f8fe4fe8983fdd4b0105061b918a56ecc5709be960e90728bb2c589f9e3331`
- Web PDF `Lucerna-VOL2-FR-web.pdf`: 3,259,655 B, 8 pages, sha256
  `dc3f70448d3d894d0342bcddb263d4681621c2ec89d13ac4d00789c5c390535f`
- SVGs (8): p1 39160a7f…, p2 d8f6bbdd…, p3 2cef9fea…, p4 cebc50b6…,
  p5 3823652c…, p6 948434f2…, p7 c54b6010…, p8 e2b48684… (full hashes
  in `work/snap1.sha`)
- Work evidence: `hidden_files/w45/zh-cn-fr-proof/work/` (snapshots,
  diff.json, occlusion.json, rowcheck, gloss/chart/badge/P8-style
  scripts, repro + repro-solo + webregen dirs and logs)

## WHAT THE REBUILD ROUND MUST DO (for the coordinator's dispatch)

1. Fix B1 (badge OLIVE → BRICK, one line) + B2 (P8 keys dash → paren,
   two lines) in the fr-build sources.
2. Fold all fixups into `transform.py` (or add a reproduce script)
   so Gate 10 passes literally from a fresh core copy.
3. Full one-process re-render + render.py, then a FRESH full proof
   round (all 11 gates, not a delta check) — with special attention
   to paren rendering around CJK-cited notes and to the corrected
   KIT sentences (badge colour, W43 P8 style, core P8 2395 figure,
   shopping count).
4. Only then insert. This edition is NOT shipped by this report.
