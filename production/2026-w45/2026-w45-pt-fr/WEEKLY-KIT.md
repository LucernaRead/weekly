# WEEKLY-KIT — W45 PT × FR (Portuguese text × French explanations)

**Pairing:** target language Portuguese (Brazilian) × reader native language French.
**Issue week:** 2026-11-02 (Mon) – 2026-11-08 (Sun). **Volume:** VOL.2 (2nd edition).
**Topics (from the W45 PT core):** Enem week — Finados holiday pont (Nov 2) + Enem day 1 (Nov 8);
football — Copa do Brasil semifinal return legs (Nov 7 Atlético-MG × Grêmio,
Nov 8 Vasco × Palmeiras).
**Build status:** builder-complete. NOT finalized — independent proofread (SOP gate)
is still outstanding and is the main line's job. No Discord post, no main-chat
card/PDF dump, no cron, no repo push was made by this build.

## 1. Source and method

- **Core (frozen verbatim):**
  `files/weekly-report-w45-pt-core/` (W45 PT core, VOL.2) and its build tree
  `hidden_files/weekly-report-w45-pt-build/`.
- **Furniture reference (read-only comparison):** W43 same-pairing edition
  `files/weekly-report-pt-fr/` + `hidden_files/weekly-report-pt-fr-build/`.
  Furniture follows the W43 measured SVGs wherever they exist; they win over the
  tools README generic text. Every deviation from W43 is listed in §4 with a reason.
- **Build tree (this edition):**
  `hidden_files/weekly-report-w45-pt-fr-build/` — build logs, `transform.py`,
  all gate raw outputs, per-round sha256 baselines.
- **Method:** fresh copy of the core build dir, transformed by `transform.py`
  (modeled on the W45 PT×DE sibling's transform). Every fix round went into
  `transform.py`; content files were never edited alone, so a from-scratch rerun
  reproduces the shipped files. Transform rules: idempotency guard (aborts if
  already transformed), OUT/BASE/PDF repointing, exact-literal replacements sorted
  longest-first (several short literals are prefixes of longer ones, e.g.
  `13 点关门` inside the P7 clinic sentence, `feriadão = 连休` inside longer notes),
  residual-CJK scan excluding `typ` registry strings (e.g. `单选`, never rendered —
  `bslib4.ex()` prints only level/number/instr/body; P8 prints key/note and checks
  `type == "写作"` for the writing item).
- **Interpreters (measured):** `run.py` and `render.py` both ran under
  `tools/venv/bin/python` — Python 3.12.3, PIL 13.0.0. System python3 has no
  cairosvg and was never used for rendering. `transform.py` itself ran under
  system python3 (3.12.3, text-only edits).

## 2. Measured specs (core WEEKLY-KIT, verified on this edition's render)

- 8 pages, 1950 × 2700, 4 columns, 8 = multiple of 4.
- **150 exercises, numbered 1–150.** Levels: A2 49 · B1 70 · B2 31.
  Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
  Types: 完成句子 61 · 单选 49 · 词汇配对 12 · 造句 7 · 判断对错 3 ·
  完形单选 13 · 翻译 4 · 写作 1. Model essay 93 words (80–100 range).
- Render: FLOW OVERFLOW 0, HEAD TOO WIDE 0 (all rounds except round 1, fixed).
  Flow ends (round 3): P1-headline 1367/1828, P1-tv 2264/2290, P1-quiz 2491/2540,
  P2-feature 1321/1540, P2 col3 932.0, P2-ex 2440/2580, P3-main 1075/1560,
  P3 col3 1110.5, P3-ex 2438/2580, P4-main 989/1080, P4 col3 905.0,
  P4-ex 2396/2580, P5-main 1038/1560, P5 col3 1098.5, P5-ex 2466/2580,
  P6-main 718/1520, P6 col3 1066.0, P6-ex 2281/2580, P7-a2 1092/1560,
  P7-b1 1089/1560, P7-b2 1214/1560, P7 col3 1826.5, P8-ex 1037/1252,
  P8-keys 2444/2552 (108 px margin).

## 3. Freeze gates (all measured on final round-3 outputs)

- **Core freeze:** `freeze.py baseline` reproduced the shipped core 8/8 SVGs
  byte-identical before transformation (e.g. p1 `0dc8089df727dfe4`); the core
  was untouched afterwards.
- **Added CJK:** `freeze.py diff` round 3 — **0 on all 8 pages**
  (core CJK per page 156/177/153/148/223/118/357/1123 → edition 0 on every page).
- **全文 桥接 0; word `bridge` 0; German test tokens absent on all pages**
  (`Feiertagswochenende`, `Eingangstore`, `Prüfung`, `Sonntag`, `HINWEIS`,
  `Wochenzeitung`, `Tag 2 ist` — a German slip `Tag 2 ist am 15. November` was
  caught in `transform.py` before any run and corrected to
  `Le jour 2, c'est le 15 novembre`).
- **P7 word-box freeze (BLOCKING gate):** the Portuguese definition sentence is
  verbatim across its two wrapped lines —
  `« feriadão »: sábado, domingo e segunda — três dias de descanso.` —
  and ONLY the gloss line is localized: `feriadão = pont de trois jours.`
  Definition localization was ruled a freeze violation for the DE/NL family and
  the same rule was applied here.
- **Cross-family residue re-scan (gate 10):** per-page CJK 0 on all 8 pages
  (see freeze diff above); no other-family language residue in the explanation
  layer or P8 notes. P8 notes are pure French (verified by the round-3 note
  listing; the only non-French tokens are frozen Portuguese headwords/keys).

## 4. Furniture registry (W43 PT×FR measured precedent + deviations)

- **P1 badge** (y=372, 19 pt bold BRICK, replaces the strapline in place):
  `TEXTES EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`
  (rendered-SVG-measured 999.5 px).
- **Footer (8/8):** `A Lucerna · HEBDOMADAIRE PORTUGAIS VOL.2 · TEXTE EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS`;
  page line `Page N sur 8` (8/8). VOL.2 substituted for W43's VOL.1 (this issue
  is the core's VOL.2).
- **Gloss prefix:** `Note — ` (gloss boxes, 5 boxes); P1 bridge uses `Notes — `.
- **P8 separator — DEVIATION from tools README, kept from W43:** `— PÁGINA {pg} —`
  (W43 PT×FR shipped SVG precedent, NOT the README's `— Page {n} —` form;
  same call as the PT×DE sibling).
- **Edition line — DEVIATION from W43 FR's 36 pt, kept at core 40 pt:**
  French line `JOURNAL PORTUGAIS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE`
  measures 1732.1 px at 40 pt ≤ 1820 px, so no shrink was needed.
- **Top strip (W43 FR exact):**
  `TODA SEMANA EM PORTUGUÊS · CHAQUE SEMAINE · LE PORTUGAIS QUE LIT LE BRÉSIL`.
- **Band titles:** VIDA · LA VIE, CULTURA · CULTURE, ESPORTE · SPORT,
  JOVENS · JEUNES, APROFUNDAMENTO · APPROFONDISSEMENT, LÍNGUA · LANGUE;
  band subtitles append a French half after `·` (W43 pattern).
- **`E VOCÊ? · ET VOUS?`** (with the French space before `?`).
- **Instruction labels:** 填空→`Compléter`, 造句→`Former une phrase`,
  翻译→`Traduire`, 写作→`Écrire`, 判断→`Vrai ou faux?`,
  把词和释义配对→`Associer`.
- **ERROS COMUNS title — DEVIATION, shortened per W43 FR precedent:**
  `ERROS COMUNS · ERREURS` (the full `ERREURS FRÉQUENTES` form measures
  480.8 px at 23 pt > the 390 px box inner width).
- **French typography:** space before `?!:` in the French layer; French-layer
  times written `13 h`, frozen Portuguese keeps `13h`.
- **P8 notes carry NO parentheses** (avoids the `p8.py` paren-branch extraction
  artifact; W43's `(titre page 1)`-style note reworded with `cf.`).

## 5. Fit fixes across rounds (all in transform.py)

- **Round 1 defects:** P8-keys FLOW OVERFLOW ×4 (French notes longer than Chinese;
  keys ran past bottom 2552 to y=2582); occlusion 14 flags (P1 LINEX palavra
  gloss 2 lines crossing hline y=1844; P1 BOXTITLE numbers-box title ink 964.5 >
  border 961.0; P7 COVER×4 + TEXTX×2 — quotes covered by the preview band
  y=2404–2522; P8 TEXTX×6 — items 147–150 clamped/overprinted).
- **Round 2 fixes (line counts verified via `svglib.wrap()` before applying):**
  P1 palavra gloss → `« Feriadão »: trois jours de pont.` (1 line);
  P1 numbers-box title → 21 pt via transform post-pass (step 2.5, scoped to the
  `A SEMANA EM NÚMEROS · CHIFFRES` box call; at 21 pt ink 383.1 px clears
  border 961.0);
  P7 error-clinic notes → 1 line each (`Stylo noir à l'Enem, pas de bleu.` /
  `Fermeture à 13 h: trop tard à 13 h 30.` / `Dormez bien, ne bachotez pas.` /
  `Pont du 31 octobre au 2 novembre.`, saves 4×29.5 px);
  P7 palavra gloss → `feriadão = pont de trois jours.` (1 line, saves 29 px);
  P7 example note → `Exemple de la rédaction. Écrivez-nous! Les meilleures paraîtront au VOL.3.`
  (2 lines, saves 58 px; imperative + VOL.3 publication promise = the explicit
  invitation gate 6 requires);
  P7 disclosure → `Note de la rédaction: ni lettres ni meilleurs textes du VOL.1 avant le bouclage — l'exemple reste, promesse au VOL.3.`
  (3 lines, saves 58 px; keeps all three facts);
  P8 shortenings, each verified 1 line: item 15 `Pas de changement d'heure au Brésil`;
  30 `Fleurs aux cimetières, surtout des chrysanthèmes`;
  31 `Messes toute la journée, églises et cimetières`;
  48 `Retour Vasco × Palmeiras, dimanche 8`;
  69 `Mardi 3: reprise des assemblées des États`;
  shared card note (items 13/80/92) → `La carte indique le lieu de l'examen`;
  81 `Faux: mieux vaut réviser un peu chaque jour`; 88 `Chiffres officiels de l'Inep`;
  98 `segunda chamada = rattrapage, 2e entrée`;
  131 `La veille: document, stylo noir, il se couche tôt`;
  144 `segunda chamada = réentrée impossible à l'Enem` (printed key line
  `144. c — segunda chamada = réentrée impossible à l'Enem : c`, the trailing
  `: c` being the match-item note pattern shared by 141–144, verified 1 line).
- **Round 3 fix (the last flag):** P7 palavra box height +4 px via a second
  transform post-pass (trailing `+ 20` → `+ 24` on the `wh = 62 + …` line in
  `content7.py`). Cause: the French gloss line's Latin descenders (`p`) put true
  ink bottom 1283.3 vs border 1282.5 (+0.8 px); the core passes only because CJK
  glyphs have no descenders. Family precedent: the core KIT's own round-1 fix
  for a 1 px box-bottom press was the same box-height compensation.
  Predicted knock-ons confirmed: P7 col3 1822.5 → 1826.5, last quote-row ink
  bottom 2396.2 < preview-band top 2404 (clearance 7.8 px). The fy gap constant
  and the 128 px quote-row spacing were NOT touched (core geometry).

## 6. Geometric gates (final round-3 outputs)

- **Occlusion audit (selftest OK): edition 0 flags, core 0 flags, NEW 0.**
  Raw output: `hidden_files/weekly-report-w45-pt-fr-build/occlusion-round3.json`.
- **Same-baseline ink-collision scan** (`extra_scans.py`, true ink, decoded text):
  **0 collisions on all 8 pages** (furniture bands, strapline rows, exercise
  heads, footers included).
- **P6 chart-label coverage, baseline-anchored ink method** (PIL `getmetrics`
  ascent/descent, anchor `ls`; `getbbox` readings do not count):
  **max 0.0%** (gate <30%); no P6 text has >0.5% later-rect coverage.
- **Frame / right-edge scan (all 8 pages):** 0 frame-strip hits (outer 28/3.4,
  inner 40/1.2, all four sides); max ink-right per page 1885.1 (p1, p3–p8) and
  1897.2 (p2); max text-ink-bottom 2629.0 (footer baseline 2624, audit-exempt).
  The p2 1897.2 line is the frozen Portuguese match option
  `d. o objeto que dá luz e se acende em memória` — the CORE p2 SVG has the
  byte-identical ink-right 1897.2 on the identical line, so it is inherited
  geometry, not a new defect; it stays 12.8 px inside the inner frame (1910).
- **Decoded-entity note:** same-baseline "hits" were measured on
  `html.unescape`d text; a raw `&amp;` reading is a known measurement artifact
  and was not counted.

## 7. Text gates (final round-3 outputs unless noted)

- **Gloss count:** 5 gloss boxes, 26 items = core 26, headwords identical
  item-by-item (split on `·` per README #21, never on ` · `). Gloss prefix
  `Note — ` count 5 = the 5 gloss boxes.
- **P7 quotes:** all 8 appear exactly 2× in the whole edition (source article +
  P7), each on its labeled page and inside the P7 block. Labels/pages:
  `Do feriadão à prova`→P1, `Muita gente viaja…`→P1, `Finados é o dia da memória`→P2,
  `lembrar é um jeito de continuar perto`→P3, `cada ponto vale uma posição…`→P4,
  `quem dorme bem lembra melhor`→P5, `primeiro as fáceis…`→P6,
  `Confira o cartão, durma bem, chegue cedo`→P2. P7 phrases verified verbatim
  from this issue's articles.
- **Readers' corner (P7, all present, zero fabrication):**
  `— EXEMPLO DA REDAÇÃO` label; Portuguese disclosure verbatim
  (`Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.`);
  French example note with explicit invitation (imperative + VOL.3 promise);
  French disclosure with all three facts (no real letters, no best P8 texts,
  example stays + VOL.3 promise); example explicitly labeled as an editorial
  example; no invented reader, letter, name, or quote. Content-preview lines and
  other-page exercise hints were NOT counted as invitations.
- **Furniture verified:** footer + `Page N sur 8` on 8/8 pages; P1 badge;
  P1 edition line; P1 top strip; band titles/subtitles on all banded pages.
- **Image / credit:** only PD/CC0 image `estudo.jpg`; base64 payload
  byte-identical to the core (length 342,316); credit line
  `Foto: Gary Todd / Wikimedia Commons — CC0` present on P1 (credit taken from
  the Commons API Artist field per core KIT, W43-verified); the image is
  verifiably typeset on P1 (photo + caption + credit visible on the P1 card).
- **Visual check:** ALL 8 cards (1950×2700 PNG) viewed page by page — no overlap,
  no truncation, no frame-press; footers show VOL.2; pairing badge and
  headers/footers complete. (The NL×PT lesson — viewing only 4 pages missed a
  P2 overflow — was honored: all 8 were viewed.)

## 8. P8 (tools/p8.py compare, round 3)

- **Status: CLEAN, 150 = 150, missing = [], extra = 0, uncertain = [].**
- **keydiff = [2, 4, 101, 137, 138, 146], adjudicated item by item against the
  printed P8 rows:**
  - **2, 4, 101, 146 — core-side paren-branch artifacts, NOT real differences.**
    The core notes contain trailing full-width `（...）` groups, so `p8.py`
    takes the core key as everything before the paren group (e.g. core item 2
    key `portões — portões = 大门`), while the French note has no parens so
    dash extraction gives the true key `portões`. Verified by extracting the
    key maps from both P8 SVGs: the printed French key token is byte-identical
    to the core's.
  - **137, 138 — legal re-aims (W43 KIT pattern).** 137 key PT→FR
    `Dimanche 8 novembre, c'est le premier jour de l'Enem.`
    (note `cf. le titre de la page 6`); 138 key
    `Vérifiez la carte avant dimanche.` (note `confira = vérifiez`).
  - **139, 140 — stems re-aimed FR→PT, keys byte-identical Portuguese:**
    139 stem `« Le feriadão va du 31 octobre au 2 novembre. » → ___`;
    140 stem `« Quand vous arriverez, présentez la pièce d'identité avec photo. » → ___`.
  - **150 — writing apparatus in French** (key `Question ouverte — texte modèle ci-dessous sur cette page`,
    note `Texte modèle dans la section H de cette page (93 mots)`); model text
    untouched; the writing prompt stem stays Portuguese (W43 FR + DE precedent).
- **P8 notes are pure French** (no parentheses, per §4).

## 9. Files and hashes (final round-3 deliverables)

- `svg/` × 8 (p1-capa, p2-vida, p3-cultura, p4-esporte, p5-jovens,
  p6-aprofundamento, p7-lingua, p8-avaliacao).
- `cards/` × 8, all 1950 × 2700 PNG.
- Print PDF `A-Lucerna-VOL2-FR.pdf` — 8 pages, 3,470,958 bytes,
  sha256 `545d6849cd6df0d5788f927eda2f3e6a79024c1f73f7b2beea8e888666702f4d`.
- Web PDF `A-Lucerna-VOL2-FR-web.pdf` — 8 pages, 3,471,235 bytes (<10 MB),
  sha256 `28965e764e220d6fe4d03aec7f95c7c7eb4dfdf12c1bbfb64cf4afe9af041c22`.
- `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (French, one line, no ASCII
  double quotes).
- Card SHA-256 (round 3): p1 `657bcd1f…`, p2 `da067a72…`, p3 `1bb0b6a6…`,
  p4 `43ab45b7…`, p5 `29720e4d…`, p6 `2f8e6b10…`, p7 `2e10bd71…`,
  p8 `3c0dba52…` (full hashes in the build-round3 baseline log).

## 10. Build history

- Round 1: rendered OK; defects = P8-keys FLOW OVERFLOW ×4, occlusion 14 flags.
- Round 2: all §5 round-2 fixes applied; FLOW OVERFLOW 0; occlusion 1 flag
  (P7 palavra box +0.8 px); p8 CLEAN; freeze diff added CJK 0.
- Round 3: palavra box +4 px post-pass; occlusion 0/0/0; all supplementary
  scans 0; all text gates re-verified; all 8 cards visually checked.
- Transform debugging notes (do not repeat): duplicate old literals cause MISS
  failures — `13:30 开考` listed twice with different translations (kept single
  entry `Début à 13 h 30`), `começar：ela → começa` identical in P2 and P7
  (deduped), `巴西没有夏令时，钟表不动` duplicated after inserting the short form
  (deleted the original long-translation entry; kept
  `Pas de changement d'heure au Brésil`). A standalone `13 点关门` entry
  (`Fermeture à 13 h`) was initially missing and added.
- Gate raw outputs in the build tree: `build-round1.log`, `build-round2.log`,
  `build-round3.log`, `occlusion-round1.json`, `occlusion-round2.json`,
  `occlusion-round3.json`, `diff-round2.json`, `diff-round3.json`,
  `extra_scans.py` (+ its round-3 output in the build log).
