# Lucerna Weekly W45 — Korean target × French native (KO×FR)

## Status

**builder-complete — NOT finalized.** Finalization is decided by independent
proofread, not by the builder. This edition was NOT posted to Discord, NOT
inserted into any repository, NOT sent into the main chat, and no cron was
created for it. Builder: subagent build only.

## Delivery

Directory: `files/weekly-report-w45-ko-fr/`

- `svg/` — 8 pages: p1-pyoji, p2-saenghwal, p3-munhwa, p4-seupocheu,
  p5-cheongnyeon, p6-gipi, p7-mal, p8-siheom
- `cards/` — 8 PNG cards, same basenames
- `Lucerna-VOL2-FR.pdf` — print PDF, 32,587,981 bytes,
  sha256 `2fc4e410d120eba3563e9a7809343a87e0610da5b9d9774a44d9754976ccacaa`
- `Lucerna-VOL2-FR-web.pdf` — web PDF, 3,565,743 bytes,
  sha256 `4773a934add411954d54dfe0e48cad54a5dba88cd984d1037d9982611594687a`
- `ABSTRACT.txt` — French single line, no ASCII double quotes
- `WEEKLY-KIT.md` — this file

Build tree (single source of edits): `hidden_files/weekly-report-w45-ko-fr-build/`
(`transform.py` is the only edit source; every fix round re-copied the core
files, re-applied `transform.py`, and re-rendered in a single process.)

## Spec (verified from the W45 KO core KIT + rendered core SVGs)

- VOL.2, masthead `Lucerna` with NO article (Korean takes no article).
- Issue week 2026-11-02 – 2026-11-08. Theme: Ipdong week / last foliage
  weekend / kimjang season opening / CSAT countdown. CSAT-day measures are
  dated 2026-11-19 ONLY throughout, never presented as applying to the issue
  week. No international politics; Korean domestic politics only.
- 150 exercises. Pages 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
  Levels A2 51 / B1 72 / B2 27. Types: complete-sentence 48, single-choice 52,
  vocabulary matching 16, cloze 13, sentence-making 8, transformation 4,
  true/false 4, translation 4, writing 1.
- P8: 38 items (A 8, B 8, C 4, D 4, E 4, F 4, G 5, H 1), printed-note set
  150/150, dash style (`N. key — note`), Korean group titles.
- Writing model 157 characters excluding spaces, verbatim = core.
- P7 phrase whole-issue frequencies 5 / 2 / 4 / 2 / 2 / 2 / 2 / 2 (= core).
- Gloss 84 items (split on `·`), per-page distribution = core (see below).
- Images per page 1 / 1 / 2 / 1 / 1 / 0 / 0 / 0.

## Furniture — three-way comparison (W45 core / W43 ko-fr / this edition)

Measured values, not copied across pairings. W43 ko-fr is the authority for
pairing furniture; the tools README generalization was NOT followed where
W43 ko-fr differs (notably badge geometry).

| Item | W45 core | W43 ko-fr (measured) | This edition |
|---|---|---|---|
| Masthead article | none | none | none (`Lucerna` bare) |
| Pairing badge | n/a (core has no pairing badge) | `TEXTES EN CORÉEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`, 20pt bold BRICK `#a4553a`, y=394 | same string, 20pt bold BRICK, y=394 (advance 993.1px) |
| Subtitle y | 372 | 366 | 366 |
| Rule lines y | 392 / 401 | 412 / 421 | 412 / 421 |
| Dark band y | 424 | 433 | 433 |
| Band texts y | 478 / 522 | 487 / 531 | 487 / 531 |
| Edition line | core-native form | `HEBDOMADAIRE CORÉEN · VOL.1 · 태풍 참피 · 가을야구 · 단풍`, 40pt | `HEBDOMADAIRE CORÉEN · VOL.2 · 입동 · 단풍 · 김장`, 40pt (advance 1024.6px, fits) |
| Footer (every page) | core-native form | `Lucerna · HEBDOMADAIRE CORÉEN VOL.1 · TEXTE EN CORÉEN · EXPLICATIONS EN FRANÇAIS`, 20pt, y=2624 | same form with VOL.2, 20pt, y=2624 (advance 863.2px) |
| Page line | core-native form | `Page {n} sur 8` | `Page {n} sur 8` (all 8 pages verified) |
| Gloss prefix | core-native form | `Note — ` | `Note — ` |
| P8 group separators | Korean `— 제N면 —` | Korean `— 제N면 —` | Korean `— 제N면 —` (frozen; NOT the generic tables form) |
| P8 band sub-line | Korean-only | Korean-only (`제8면 · 이번 주의 큰 시험 + 모든 답`) | Korean-only |
| Top strip centre | core-native form | core-native form | `매주 한국어로 · Chaque semaine · 한국 사람이 읽는 한국어를 읽어요` |
| Band right (P1) | core-native form | n/a (W43 theme differs) | `IPDONG` / `L'Ipdong, le samedi 7 novembre · Début du kimjang` |

Band titles: 생활 · Vie quotidienne; 문화 · Culture; 스포츠 · Sports;
청년 · Jeunesse; 깊이 읽기 · Lecture approfondie; 말 공부 · Langue;
시험과 답 · Test et réponses (P8 band sub-line kept Korean-only).
Exercise heads: `연습 · Exercices page N`. Type names: Compléter / Choix
multiple / Appariement / Texte à trous / Former une phrase / Transformation /
Vrai ou faux / Traduction / Rédaction. Instruction labels: Complétez /
Réécrire / Former une phrase / Traduire / Écrire / Associer.
Contents P8 row level reads `Tous` (P8 mixes A2/B1/B2).

## Language layer

- Target-language (Korean) text frozen verbatim; explanation layer entirely
  in French. Korean glossline instructions and P8 Korean group separators
  frozen, following the W43 ko-fr precedent.
- Text-node scans on the final SVGs: Han characters 0 on every page,
  ASCII double-quote characters 0 in text nodes, the banned
  intermediary-layer term 0 in SVGs + ABSTRACT + build code + this KIT
  (the term is referred to only obliquely here, never spelled out).
  No occurrence of `Le Lucerna` anywhere (masthead is article-free).
- Type/instruction collision handled in `transform.py` before the global
  map: the translation and writing instruction labels were localized first,
  then the global type names, so no instruction label was overwritten by a
  type name. Replacements are longest-source-first with assertions
  (source occurs ≥1 time and is absent afterwards); the transform is atomic.

## P7 gates

- Definition sentences frozen verbatim; only glosses localized.
- Golden sentences are verbatim contiguous excerpts of this issue's own
  text with correct page tags; whole-issue counts edition = core =
  5 / 2 / 4 / 2 / 2 / 2 / 2 / 2, each phrase also present on its tagged page.
- Readers' corner: zero invented letters. It shows the labeled editor's
  example (`Exemple de la rédaction, pas une vraie lettre.`), the frozen
  Korean disclosure verbatim, the French disclosure covering BOTH letters
  and P8 writing, and the explicit imperative public solicitation
  (`Envoyez-nous votre lettre et votre texte de page 8!`). Teaser lines,
  content-preview lines, and other-page exercise hints were NOT counted as
  solicitation.
- VOL.3 preview keeps the promise of letters + best P8 writing.
- P7 phrases pitch: core 132 → edition 102 (documented geometry deviation,
  forced by the longer French readers' corner; phrase rows need ~76px, so
  pitch 102 still leaves ~26px inter-row air). P7 col3 ends 1865.94;
  P7 teaser band rect (65, 2401.94, 1820×118) → teaser end 2519.94
  (gate <2540).

## P8 gates

- Dual-path compare, `--total 150`: core 150 noted = edition 150 noted,
  status CLEAN, missing [] extra_count 0 uncertain [].
- Tool versions: at task start, `tools/p8.py` was the verified old version,
  sha256 `67df05f1bc7234eeb48d25fff2cb85a406e8bfcd6b211b9fdc76231b6296c132`.
  During this build (2026-10-28 03:35:43 UTC) ANOTHER process replaced
  `tools/p8.py` with a file byte-identical to
  `hidden_files/w45/p8-dash-fix-verify/p8.py.new` (sha256
  `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`).
  This builder did NOT write to `tools/`. Both versions were run on this
  edition and agree: CLEAN, keydiff `[137, 138]`. The new version was used
  read-only for cross-check only and was NOT adopted by this builder.
- Keydiff adjudication (from printed lines, never from tool output alone):
  - 137: stem Korean `11월 7일은 입동이에요.` → key
    `Le 7 novembre, c'est l'Ipdong.`, note `Voir page 1`. Genuine E re-aim.
  - 138: stem Korean `수능까지 12일이 남았어요.` → key
    `Il reste 12 jours avant le Suneung.`, note `Voir page 5`. Genuine E re-aim.
  - 139: stem French `Les mesures spéciales ne s'appliquent que le
    19 novembre. → ___`, key Korean byte-identical to core, note
    `Voir page 6`. 140: stem French `Samedi, je vais à Naejangsan voir les
    feuillages. → ___`, key Korean byte-identical to core, note
    `Voir page 3`. E-zone item numbers were verified from the core render,
    not copied from other families.
  - 150: H apparatus line, key `(question ouverte — modèle ci-dessous)`,
    note `Modèle dans la section H de cette page (157 caractères)`.
    The registry comparison keydiff is `[137, 138, 150]`; the p8 tool
    correctly excludes the apparatus line, giving `[137, 138]`.
  - No 109-style parenthesis/dash artifact in either tool's output for
    this edition. Printed line 109 checked directly:
    `109. 기준 — Les dates diffèrent car les critères diffèrent (page 3)`
    (key byte-identical to core; note localized).
- P8 numbered key lines 1–150 present exactly once in the keys flow.
- P8 keys flow: 165 keys-region lines, max baseline 2528.85, ink bottom
  2532.60 (gate <2540).
- P8 header: `답 · Réponses — classées par page, cherchez le numéro` /
  right line `Chaque réponse avec une courte note en français · ✓ = exercice
  à texte modèle`.
- P8 notes are pure French. Freeze diff: added CJK characters = 2 on P8
  only (`절` +1, `기` +1), all other pages 0. Adjudication: a Korean-headword
  citation in the French note for item 104 (`절기 = les 24 divisions de
  l'année`), quoting the P7 exercise's own Korean word — same citation
  class as the ko-pt precedent, not new target text and not explanation
  residue.

## Gloss (render-time `·`-split counts)

Core = edition per file: content12 24, content34 26, content56 28,
content7 6, content8 0, TOTAL 84.

## Geometry gates (final render, venv PIL)

- Canonical `tools/occlusion_audit.py` self-test OK (all planted classes
  fired, clean controls silent). Edition flags 0, core flags 0, NEW
  (edition-minus-core) 0.
- ADVANCE full-page right-edge scan (inner frame x=1910): worst advance
  end 1885.0, flags 0.
- Full-page frame-line scan (ink vs stroked rect borders): flags 0.
- Same-baseline ink overlap scan (0.6px tolerance): flags 0.
- P6 chart-label coverage (getmetrics baseline-anchored ink boxes):
  12 labels, worst coverage 0.0% (gate <30%).
- Rendered-line window scan (dy 10–45): line-start flags 0.
- Korean orphan scan (window 10–45, ≥3-syllable-tail standard): post-kinsoku
  line-start NO_START flags 0; mid-word splits with tail ≥3 syllables 0.
  Lone final-line fragments (≤3 chars) 5, all adjudicated as legitimate
  short finals of frozen Korean text, not orphan defects: title fragment
  `소식`, option word `대구`, true/false option `틀리다` (×3).
- Below-box spill candidate scan (baseline within 45px under a stroked
  rect bottom, x inside rect): 31 candidates, ALL adjudicated as following
  elements (section heads, image captions, table next-row texts, following
  paras), none a box's own content below its box. The frame scan's zero
  straddles plus this scan close the fully-below-spill class that the
  core's own P7 readers box exhibited (see Observations).
- P8 answer-flow end 2532.60 < 2540; P7 teaser end 2519.94 < 2540.
- Gate output was not truncated. All 8 cards viewed visually, page by
  page (p1–p8), clean: badge, band, footers, boxes, images, keys flow,
  readers box fully containing its last line with air before the phrases
  rule.

## Images

Only explicitly public-domain/CC0. Credit lines taken verbatim from the
Commons API Artist field; every credited image verified as actually placed.
Payload hashes identical core vs edition on every page under BOTH calibers
(base64-text sha256 prefix / decoded-JPEG sha256 prefix):

| Page | Images | Credits |
|---|---|---|
| P1 | 1 | lumoplank — CC0 |
| P2 | 1 | wizdata — CC0 |
| P3 | 2 | Udonhan1992 — CC0; Paul Cézanne — Public domain |
| P4 | 1 | Bain News Service — Public domain |
| P5 | 1 | Gary Todd — CC0 |
| P6 / P7 / P8 | 0 | — |

Payload prefixes (base64-text / decoded-JPEG): P1 `535fff46b7ce` /
`6f7f33ed8f40`; P2 `e66d2b455ec6` / `96a6a19b612a`; P3 `e266b6ee1a87` /
`158ea3a0e81f` and `5bea45d1f81e` / `214cc390ac7c`; P4 `1a7e7d6d5ffc` /
`18ad8ae06fac`; P5 `6a1bab177d54` / `35e7dc69d417`.

## Registry

Expanded to 150 continuous; number/page/level identical to core for all
150; notes changed 150/150. Baseline proof: the unmodified core copy,
repointed to the new edition directory, reproduced all 8 core SVGs
byte-identically (8/8) before localization. Core SVGs unchanged after this
build (sha256 check against the recorded baseline passes).

## Rounds log

- Round 1: canonical occlusion audit 3 flags, all real — P2 box title
  `한능검 접수 · Inscriptions à l'examen d'histoire` crossed its box border
  (right ink 1057.2 > border 961.0) and caused a TEXTX overlap with a gloss
  line; P3 box title `단풍 구경 준비물 · Pour voir les feuillages` crossed
  its border (1447.5 > 1423.0). No FLOW OVERFLOW / HEAD TOO WIDE warnings.
  Round 1 baselines saved in `round1-svg-sha256.txt`.
- Round 2 fix (via `transform.py` only, then fresh core re-copy +
  re-transform): P2 box title shortened to `한능검 접수 · Inscriptions`,
  P3 box title to `단풍 구경 준비물 · À emporter`. Round 1→round 2 diff
  exactly scoped: only p2/p3 SVG + card + both PDFs changed; all other
  files byte-identical. Canonical audit then 0 / 0 / 0.
  Round 2 baselines saved in `round2-svg-sha256.txt`.
- Round 3 fix (via `transform.py` only, then fresh core re-copy +
  re-transform): P7 readers-box `lh` formula +40 slack (see Observations)
  and P7 phrases pitch 112 → 102. Round 2→round 3 diff exactly scoped:
  only p7 SVG + card + both PDFs changed; all other files byte-identical.
  Round 3 baselines saved in `round3-svg-sha256.txt`. This KIT's PDF
  byte counts and hashes are the round-3 values.

## Deviations from W43 ko-fr (deliberate, recorded)

- VOL.2 (W43 was VOL.1); issue week and theme are W45 (Ipdong week
  2026-11-02–08), not W43's theme.
- P7 phrases pitch 132 → 102 (W43 shipped 132; the longer French
  readers' corner forced the change; row content ~76px, pitch 102 keeps
  ~26px inter-row air).
- P7 readers-box `lh` formula +40 slack (W43 formula undercounts drawn
  height; see Observations).
- P2/P3 box-title shortenings (`Inscriptions`, `À emporter`) — round-2
  geometry fixes, not W43 strings.
- P8 short-variant note strings distinct from longer P3 forms
  (e.g. the Naejangsan forecast-peak and Seoul registration-window notes)
  — the round-1 transform trap class, fixed before first render.
- Band sub-lines, contents, and exercise furniture follow the W45 core
  where the theme differs (e.g. P1 band right Ipdong lines, contents level
  `Tous` for the mixed-level P8 row).
- PDF names follow the W43 ko-fr pattern: `Lucerna-VOL2-FR.pdf` and
  `Lucerna-VOL2-FR-web.pdf`.

## Toolchain

- `run.py` and `render.py` both run with `tools/venv/bin/python`:
  Python 3.12.3, PIL 13.0.0, cairosvg 2.9.1. System python3 (3.12.3,
  PIL 10.2.0) was NOT used for rendering. Audit measurements use venv PIL;
  `render.py` always uses the venv.
- Supplementary scans were implemented fresh in this build tree
  (`audit_fr.py`, `orphan_log.py`, `gloss_compare.py`, `reg_compare.py`).
  The sibling ko-de `audit_extra.py` / `spy_wrap.py` files were NOT copied
  or run.
- `transform.py` is the single source of edits; pre-fix full sha256
  baselines were saved before each fix round; the build tree was never
  reset in a way that loses a baseline.

## Observations (for independent proofread; none blocks builder-complete)

1. Inherited core readers-box formula undercount: the core's `lh` formula
   undercounts drawn height by ~25–29px. In the core, the last disclosure
   line sits fully below its box (box bottom 1738.94, last ink bottom
   1766.73) but above the phrases rule (1768.94) — a fully-below spill the
   border-straddle scan cannot see. In this edition the longer French
   disclosure made it a straddle (ink 1805.53–1826.28 across the 1825.94
   border, final line 1.01px above the phrases rule). Fixed here with +40
   slack: new box bottom 1865.94, last ink bottom 1854.93 inside by ~11px,
   and the pitch change keeps the teaser end at 2519.94. The CORE itself
   still carries the undercount; a core-side fix is a separate decision.
2. `audit_fr.py` section 4 (P6 label coverage) initially returned 0 labels
   after a parser fix, because the section's element regex used greedy
   attribute matching that swallowed each text element following a
   self-closing rect. Fixed to non-greedy attributes; clean re-run reports
   all 12 labels at 0.0%. The same greedy pattern does not affect the
   canonical occlusion audit or the other sections (verified by the
   independent parse counts: 169 texts on P6).
3. `tools/p8.py` was replaced mid-build by another process (see P8 gates).
   This builder neither made nor adopted the replacement; both tool
   versions agree on this edition.
4. The 5 lone final-line fragments and the 31 below-box spill candidates
   are adjudicated above; the proofreader may re-check them against the
   cards, which were all viewed clean.
5. ABSTRACT.txt (French, single line, no ASCII double quotes):
   `Lucerna coréen VOL.2 : la semaine de l'Ipdong du 2 au 8 novembre 2026 —
   derniers feuillages d'automne, ouverture de la saison du kimjang, compte
   à rebours du Suneung et inscriptions à l'examen d'histoire de Corée ;
   150 exercices de coréen du niveau A2 au niveau B2 pour apprendre le
   coréen en lisant de vrais articles.`
