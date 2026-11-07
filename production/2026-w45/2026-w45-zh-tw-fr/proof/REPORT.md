# INDEPENDENT PROOFREAD — W45 zh-TW × FR (Traditional Chinese target · French reader)

**Verdict: PASS with ZERO PROBLEMS.** All 16 gates pass, including Gate 10
reproduction and Traditional independence. This report is the finalization
evidence for the coordinator's insert step. Nothing in this proof declares
anything shipped, and no insert, Discord post, chat delivery, cron, or
`weekly-git` action was taken by the proofreader.

- Edition dir: `files/weekly-report-w45-zh-tw-fr/` (svg ×8, cards ×8, print +
  web PDFs, WEEKLY-KIT.md, ABSTRACT.txt)
- Core: `files/weekly-report-w45-zhtw-core/` (KIT read first; 150 exercises,
  A2 44 / B1 74 / B2 32, pages 10/18/18/18/18/18/12/38)
- W43 same-pairing reference: `files/weekly-report-zh-tw-fr/`
- Builder dir (read-only for this proof): `hidden_files/weekly-report-w45-zh-tw-fr-build/`
- This proof's work: `hidden_files/w45/zh-tw-fr-proof/` (this REPORT.md + `work/`)

## Pre-flight (coordinator ruling: NO CONCURRENT WRITER)

- No live worker/process writing to the delivery or build dirs (`ps` clean).
- Two mtime snapshots of both dirs ~2 minutes apart: **IDENTICAL**
  (`work/snap1.txt`, `work/snap2.txt`).
- Builder session complete (KIT status BUILT, delivery mtimes 2026-10-28
  08:53–08:57 UTC, before this proof began). Pre-flight CLEAR; proof proceeded.

## Per-gate evidence

### 0. Delivery pins re-verified (start and end of proof)

- Print `Lucerna-VOL2-FR.pdf`: 20,075,140 B,
  sha256 `6323329f91ee49644957a6736d54e8e604009a184fe5d17dbf85273d5876dc27` ✓
- Web `Lucerna-VOL2-FR-web.pdf`: 3,478,378 B,
  sha256 `d50c68bbfbca315a9b05504e6261b5c734a292d5441e8defc733678800b12645` ✓
- Both 8 pages. Pins unchanged after the Gate 10 run (see Gate 10 note).
- Delivered SVG sha256 (all 8) match the builder KIT Gate 10 list exactly:
  p1 `446aa933f1f94d8…`, p2 `9c69461636c3fb…`, p3 `4696d0415d094…`,
  p4 `fe832a7eff464e…`, p5 `335e7c4560c7ed…`, p6 `e12de61199e8a…`,
  p7 `3318776e25130…`, p8 `3e7908dfab9dfa…` (full hashes in §Gate 10 output).

### 1. Freeze baseline + strict-CJK diff

- `tools/freeze.py baseline` on the unmodified zh-tw core build: **8/8
  byte-identical**; core hashes `4672c972763b0eaf`, `889fb533ef3ff62e`,
  `508703c2b3c313c6`, `e04b62ea6211c9ff`, `4dfce72d88000fbc`,
  `06ba4c6627cb8165`, `00ac7f57125fcc09`, `e6e97d02595aef3b` — matching the
  builder's baseline list; shipped core SVGs re-hashed unchanged afterwards.
- `tools/freeze.py diff --strict-cjk` core vs edition: **strict-CJK added = 0
  on all 8 pages** (p1–p8: 0, 0, 0, 0, 0, 0, 0, 0).
  Full-width ， counts identical core vs edition on every page
  (26/40/40/33/40/19/30/31), so the intermediate +6 ， on P7 is gone.
- The 6 FIX4 comma restructurings were read in the transform and lose no
  meaning: 集章, c'est → 集章 veut dire; 封王, puis → 封王 puis; the B2
  paragraph rebuilt as « Autrefois 打卡 voulait dire… », « 討糖 désigne… »,
  « 踩街 est… », « 泡湯 est… » (same glosses, same facts).
  (`work/freeze-diff.json`)

### 2. Traditional independence — HARD GATE, re-extracted from shipped SVGs

- CJK sets extracted from the shipped SVG `<text>` nodes themselves
  (ranges U+3400–U+4DBF, U+4E00–U+9FFF, U+F900–U+FAFF, U+20000–U+2A6DF):
  edition 766, core 767, W43 784; **characters in the edition outside
  (core ∪ W43) = 0**.
- Simplified-only spot scan over all edition SVG text (邮 说 国 龙 马 发
  让 对 为 会 东 车 门 问 间 见 长 湾 网 风 飞 头 汉 义 习 贝 产 严 刘 广 厂 疗):
  **ZERO hits**.
- Transform grep: opencc/OpenCC/s2t/t2s/zhconv/convert/mapping/Simplified/简体
  all **0 occurrences**; the transform is whole-literal English→French
  replacements only, no conversion logic, no mapping table.
- The 1-char shortfall vs the core is the designed furniture change (Chinese
  badge/footer strings replaced by French furniture, per W43 precedent).

### 3. Target text ZERO difference (run level)

- Every removed CJK string in the freeze diff was listed and classified:
  all are explanation-layer or furniture — bilingual section heads, gloss
  lines with English notes, P8 key lines with English notes, the Chinese
  badge/footer/page lines. No article, exercise-face, or target sentence
  string was removed or altered.
- Added CJK strings are the same Chinese heads/terms with the English second
  part replaced by French; no new CJK character anywhere (Gate 1).
- Corroborated by Gate 10 (transform-only derivation from the core with
  exact-count asserted replacements) and by p8.py keydiff[] (Gate 5).

### 4. Gate 10 — REPRODUCTION (mandatory, blocking) — PASS

- Fresh copy of the core build into `work/gate10/` + `transform_fr.py`
  ALONE, then the single one-process driver `run.py`:
  **exit 0, 8/8 byte-identical** to the delivered SVGs
  (`sha256sum -c` against the pre-run snapshot: all 8 OK),
  **ZERO FLOW OVERFLOW / HEAD TOO WIDE warnings** (`grep -c` = 0),
  registry identical: TOTAL 150, by level A2 44 / B1 74 / B2 32,
  by page 10/18/18/18/18/18/12/38,
  by type 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1.
  (`work/gate10-run.log`)
- Transform-only proof (separate from the run): text-applying the transform's
  replacement lists (repoint + bslib + R12/R34/R56/R7/R8 + FIX2–FIX5 +
  render_names) to fresh core copies yields files **byte-identical** to the
  FR build's bslib4.py, content12/34/56/7/8.py and render.py. **No direct
  build-copy edit remains.** Every fix lives in the transform:
  FIX2 band titles + P6 head + P7 compression, FIX3/FIX4 disclosure trims,
  FIX5 letters-box constant +26 → +56 (+30).
- Transparency note: the Gate 10 run writes its SVGs into the edition dir
  (that is the transform's repointed OUT). The delivered SVGs were backed up
  first (`work/delivered-svg-backup/`); after the run every hash was
  verified unchanged, so the delivery is intact. Cards and PDFs were NOT
  regenerated into the delivery dir (see Gate 14 for the proof-local regen).

### 5. p8.py — CLEAN

- `tools/p8.py compare --core-p8 … --edition-p8 … --total 150`:
  **CLEAN, core 150 noted, edition 150 noted, missing=[], extra_count=0,
  uncertain=[], keydiff=[]**.
- `extract` on the edition P8: noted set 150/150.
- Writing-model body (138 characters) verified byte-identical core vs
  edition; only its French label changed (« Texte modèle : »).

### 6. Occlusion audit + ink collisions + chart labels

- `tools/occlusion_audit.py --selftest`: OK (all 6 planted classes fired,
  clean controls silent).
- Edition run: **0 flags**; `--core` run: core 0 flags, **NEW vs core 0**.
  (`work/occlusion.json`)
- Same-baseline ink-collision scan (own implementation, PIL/TC-font widths
  via a fresh copy of svglib's `text_w`, gap < 2px criterion): **0 flags**
  on all 8 pages.
- P4/P6 chart-label element check (text ink vs later-drawn bar rects):
  **0 overlaps**. Bar widths match the core exactly: P4 120.0 and 600.0 px
  (at y=1204, 1404); P6 600.0, 800.0, 800.0, 800.0 px (at y=962, 1014, 1066,
  1118). P6's other 60×30 chip rects are also identical.
- The 4 first-pass flags were fixed in the transform, not adjudicated away:
  P2 你呢 box (FIX4 French 3→2 lines), P5 box title (FIX4 « Le programme de
  Tianmu » → « Le programme »), P6 box title (FIX4 « Comparez
  attentivement » → « Comparez »), P7 letters box (FIX3/FIX4 disclosure
  trims + FIX5 height constant +30). Final render: 0 flags.

### 7. Gloss counts + registry (zh-tw core's true counts)

- Source-text grep, core build vs FR build (no module imports):
  gloss() core = edition = **12** (content12 4, content34 5, content56 3);
  glossline() core = edition = **4** (content7 3, content8 1).
  Per-page split consistent with the builder's claim (P1 2, P2 2, P3 3,
  P4 2, P5 2, P6 1; P7 3, P8 1).
- No gloss string in either build contains a `·` item separator, so
  tools/README #21's split-counting case does not arise.
- Registry from the Gate 10 run (above): 150, A2 44 / B1 74 / B2 32,
  types 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1 — identical
  to the zh-tw core KIT, NOT the zh-cn 56/69/25 split. Verified from the
  run output, not copied from the builder's numbers.

### 8. P7 golden sentences

- All 8 verbatim from this issue's own articles (bracket-stripped inner
  text; articles carry no 「」): **exactly 2 occurrences each** in the
  edition full text AND in the core full text, present on the tagged
  article page and on P7 in both.
- Tags in the zh-tw core's form, in strip order: **p. 1, 1, 2, 3, 3, 4, 5, 6**
  (read off the shipped P7 French tag lines, which match the core's
  English tag lines item for item). Not zh-tw-de's S. form, not zh-cn's form.
- Sentences: 用手機轉帳…金融科技 (p. 1), 123個國家及城市…攤位 (p. 1),
  需要才買… (p. 2), 在高雄，鋼鐵也能變成舞台 (p. 3),
  福隆的夏天，在10月26日畫下句點 (p. 3), 6比0完封兄弟… (p. 4),
  250家店家一起討糖 (p. 5), 旅展首日中午12點才開門 (p. 6).

### 9. Images

- Per-page payload counts core = edition, byte-identical payloads:
  **1/1/0/1/1/0/0/0** (P3 0, unlike zh-cn's P3 2 — verified against the
  zh-tw core, not zh-cn). P4 payload hash `18ad8ae06fac2860…` = the core's
  verified Washington baseball-team photo.
- Credits verbatim in the shipped SVGs: « Photo: Wilfredor — CC0
  (Wikimedia Commons) » (P1), « Photo: CorraleH — CC0 (Wikimedia Commons) »
  (P2), « Photo: Bain News Service — Public domain (Wikimedia Commons) »
  (P4), « Photo: Benjamin Balazs — CC0 (Wikimedia Commons) » (P5).
  P4 provenance is covered by the coordinator's 2026-10-27 adjudication
  (CLOSED, byte-identical to the W43 Korean build record) and was not
  re-flagged; placed bytes and credit line are unchanged.

### 10. Readers' corner

- Frozen Traditional disclosure **byte-identical** in the edition P7 and in
  the core P7: « 延期披露：VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文；
  截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，
  並繼續公開徵集。你的來信，下一期見。 »
- French disclosure states no genuine letters exist (« Lettre d'exemple —
  pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies
  lettres et les meilleurs textes de page 8 ; aucun texte publiable
  n'était arrivé — l'exemple reste, et l'invitation reste ouverte :
  écrivez-nous ! »).
- Verbatim open invitation confirmed on the card: **« écrivez-nous ! »**
  (with French spacing before the exclamation mark).

### 11. Furniture three-way (core · W43 zh-tw-fr · this edition)

- P1 pairing badge MEASURED on all three P1s at **y=378, 21pt**:
  core = Chinese+English line, OLIVE #3e4c2a (subtitle slot exists);
  W43 = French line, BRICK #a4553a, replaced in place;
  edition = **identical French text to W43**, BRICK #a4553a, in place:
  « TEXTES EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS —
  L'ÉDITION POUR LES LECTEURS FRANCOPHONES ».
  This matches the zh-tw-de family slot behaviour cited by the builder and
  is confirmed by measurement, not assumed.
- Footer (all 8 pages, edition): « Lucerna · HEBDOMADAIRE CHINOIS VOL.2 ·
  TEXTE EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS » with page
  lines « Page N sur 8 » — the W43 French form with VOL.2. ✓
- Gloss prefix: edition « Note — » ×12, « Notes｜ » ×0 — the W43 zh-tw-fr
  family precedent (W43 itself: « Note — » ×11). ✓
- P8 separator: « — Page N — » on all 8 separators in core, W43 and
  edition (unchanged). ✓
- P8 dash style: W43 P8 sample key lines use dash style
  (« 1. B — Jangmi est un typhon fort (sévère). »); core and edition P8
  lines are dash style too (« 1. B — La Semaine FinTech ouvre le lundi
  2 nov. »). **NO paren interaction in this family** — the dash claim is
  confirmed against the shipped W43 SVG, so no paren-style conversion
  issue arises. (Unlike zh-cn-fr's paren style; family precedent checked,
  not assumed.)
- Edition line y=316 and strapline y=410: byte-identical core vs edition.
- `tools/tables.json` was NOT edited by this proof (discrepancies were
  adjudicated against shipped W43, which wins per the task).

### 12. Residual Latin

- Full inventory of all 657 unique Latin-bearing strings in the edition
  SVGs was listed and classified (`work/proof_checks.log` §K).
- Allowed residues only: the French explanation layer; frozen citations
  (Fintech Nexus theme « Fintech Nexus: Bridging the World, Building the
  Future », StartmeupHK, ITF, SUPER STAGE, SOLID TIDES, Trick or Treat,
  JUMP, MVP, TSNA, C.C. Mercedes, Pier-2, Cathay Pacific Taipei-Tokyo,
  trail transliterations, NT$, VOL.2, level chips, option letters);
  photo credits (above); W43-precedent « — Page N — » separators and
  « p. N » tags.
- English-marker scan (Fill in, Answer keys, Word of the week, Over to you,
  Did you get it, in English, Traditional Chinese text, English
  explanations, Notes｜, Staff report, Test & keys, True or false, The big
  quiz, Read and answer, Say it in context, This week, Life, Deep read,
  Language focus, Youth): **none present**. English function-word scan
  over Latin strings found only the frozen Fintech Nexus theme (plus
  false hits on the French words « quiz »/« notes »).
- **Zero English explanation prose. No other Latin residue found.**

### 13. Non-blocking adjudications — verified, not rubber-stamped

- P4 title « 棒球詞卡 · Les mots du baseball » wraps to two lines
  (y=765.025 « 棒球詞卡 · Les mots du », y=806.505 « baseball », size 34):
  clean wrap inside the flow, no overlap with any neighbour (occlusion 0,
  same-baseline 0, card eyeball clean). **Clean, not blocking.**
- P7-A2 flow-end 1594 vs 1560 bottom is trailing gap only: measured A2
  column (x 60–500, y < 1700) max baseline **1551.35**, max ink bottom
  ≈1557.80 ≤ 1560 design bottom. **Trailing gap only, not blocking.**
  P7 overall non-footer max ink bottom ≈2515.16 (core ≈2515.66); footer
  rule at 2580 is clear.

### 14. Web regen (proof-local, delivery PDFs untouched)

- Regen from the reproduced SVGs with the edition's own render.py
  (BASE repointed to `work/render-out/` only):
  cards **8/8 byte-identical**; print PDF **byte-identical**
  (20,075,140 B, sha256 `6323329f…5876dc27` = delivered pin);
  web PDF **content-identical with timestamp bytes excepted, stated
  explicitly**: same size 3,478,378 B, 8 pages, identical embedded JPEG
  page images (same byte sizes on all 8 pages); the two files differ in
  exactly **8 bytes, all inside /CreationDate and /ModDate**
  (D:20261028085408Z → D:20261028090703Z). The delivered web PDF's own
  sha (`d50c68bb…b12645`) is therefore unchanged and still valid.

### 15. Eyeball — all 8 cards

- Viewed page by page (1950×2700 PNGs): layout clean on every page, no
  overflow, no overlap, no footer collision, no missing content.
- P1: badge in brick, harbour photo + Wilfredor credit fully visible.
  P2: rain photo + CorraleH credit; 你呢 box fits. P3: no photo (correct),
  all boxes fit. P4: two-line title wrap clean; chart bars + labels clear;
  team photo, caption and Bain credit fully visible. P5: shortened
  « Le programme » schedule box fits; pumpkin photo + Balazs credit
  visible. P6: chart + « Comparez » box fit; exercises clear. P7: A2/B1/B2
  columns, clinic, frame, readers' corner (frozen disclosure + French
  disclosure + « écrivez-nous ! »), phrase strip with tags, VOL.3 teaser
  all fit above the footer. P8: test sections A–F, writing model,
  dash-style keys, « — Page N — » separators, footer all clean.

### 16. ABSTRACT.txt

- French, single line (366 bytes, 1 trailing newline, **no ASCII double
  quotes**): « Lucerna, hebdomadaire en chinois traditionnel du 2 au
  8 novembre 2026 : Semaine FinTech de Hong Kong, Salon international du
  voyage de Taipei, titre des Dragons de Wei Chuan en Série de Taïwan,
  Lidong, Halloween à Tianmu et festival de sculpture sur acier de
  Kaohsiung — 150 exercices du niveau A2 au niveau B2 pour apprendre le
  chinois traditionnel en lisant. »
- Contains: paper name (Lucerna), target language (chinois traditionnel),
  A2–B2, exercise count (150), a learner search phrase (« apprendre le
  chinois traditionnel en lisant »).
- Every named topic cross-checked against the zh-tw core's actual content:
  FinTech Week (P1/P6) ✓, ITF Taipei (P1) ✓, Dragons title (P4) ✓,
  Lidong (P2/P3) ✓, Tianmu Halloween (P5) ✓, Kaohsiung steel festival
  (P3) ✓. **No topic outside the core. Nothing blocking.**

## Non-blocking observations (separate from the verdict)

1. FIX4's French disclosure shortens the main-phase draft (« Lettre
   d'exemple de la rédaction » → « Lettre d'exemple »; « à la mise sous
   presse » dropped). All material facts survive (example letter, no
   publishable text arrived, example stays, invitation open +
   « écrivez-nous ! »). No change required.
2. P5 « 4 500 seaux citrouilles » uses « citrouilles » as a noun adjunct
   in the plural; acceptable in this register. No change required.
3. P4 two-line title wrap and P7-A2 trailing gap: verified clean in
   Gate 13 above; recorded here only so they are not re-raised as
   findings.
4. Method note (not an edition issue): an early extraction of the P8
   writing model compared unequal regex spans and briefly read
   "not identical"; the corrected comparison (same 138-character body,
   different end anchors) shows the model body byte-identical. No
   edition text is affected.

## Limitations (stated honestly)

- French was checked by full reading of the entire explanation layer
  (every transform replacement + every added string in the freeze diff +
  the rendered cards), not by a native speaker.
- No live Commons API re-query was performed in this proof. Image credits
  were verified verbatim against the shipped core SVGs and the core KIT's
  Commons-Artist-field table, with payload byte-identity to the core
  (including the coordinator-closed P4 record). A fresh Commons fetch
  would add nothing unless the placed bytes or credit lines change.
- `tools/tables.json` furniture strings were not re-derived from the repo;
  furniture was adjudicated against the shipped W43 zh-tw-fr SVGs, which
  are the binding family precedent for this pair.
- The proofreader did not re-verify the core's own facts (dates, scores,
  arithmetic) beyond what the fan-out gates require; the core was already
  independently proofread and finalized, and this proof's remit is the
  fan-out's fidelity to that core.

## Files

- [REPORT.md](sandbox://workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-fr-proof/REPORT.md)
- Work evidence under `hidden_files/w45/zh-tw-fr-proof/work/`:
  `snap1.txt`, `snap2.txt`, `freeze-diff.json`, `occlusion.json`,
  `proof_checks.py`, `proof_checks.log`, `gate10-run.log`,
  `textapply/` (transform-only proof), `gate10/` (Gate 10 reproduction),
  `render-out/` (proof-local regen), `delivered-*-backup.*` (pre-proof
  backups of the delivery, unused for restoration — nothing needed it).
