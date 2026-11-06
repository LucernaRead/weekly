# La Lucerna — HEBDOMADAIRE ESPAGNOL VOL.2 · ES × FR (W45)

**Pairing:** Spanish target text (frozen W45 core,
`files/weekly-report-w45-es-core/`, VOL.2, semaine du lundi 2 au dimanche
8 novembre 2026) + explanation layer written natively in **French**, for
francophone readers. **Status:** builder-complete. **Independent
proofread: PENDING** (parent runs it; repo insert + any posting happen
only after it passes — not done here, and no final-edition claim is made
here). No Discord post, no main-chat card/PDF dump, no cron was created;
the core build dir and the W43 edition dir were never written.

## 1. Method & baseline proof

- Build dir: `hidden_files/weekly-report-w45-es-fr-build/` — a copy of the
  W45 core build (`hidden_files/weekly-report-w45-es-build/`).
- **Baseline proven before any edit:** `tools/freeze.py baseline` on the
  copy reproduced all 8 shipped core SVGs byte-identically:
  p1 `a1b30102…`, p2 `10e78c2e…`, p3 `5986ba9e…`, p4 `1894836e…`,
  p5 `cd15c68b…`, p6 `fcfccf82…`, p7 `b1774024…`, p8 `d1c46fa4…`
  (full hashes in §8); core SVGs re-hashed afterwards, unchanged.
- All OUT paths in the copy were repointed (all `os.path.expanduser`
  forms) to `files/weekly-report-w45-es-fr/`; the single-process driver
  `run.py` renders all 8 pages in one process (shared bslib4 registry).
- Only the explanation layer was rewritten, via the asserted-replacement
  script `hidden_files/w45-es-fr-transform.py` (290 replacements, each
  asserting its hit count, abort-on-mismatch; longer strings before their
  substrings; full bridge sentences before bare `instr=` values).
  **Reproducibility verified:** a from-scratch copy + the same script +
  `run.py` reproduces all 8 delivered SVGs byte-for-byte (hashes in §8).
- Exercise type names (`完成句子`/`单选`/…) stay frozen per the W43 ES×FR
  precedent (only `instr=` labels translate: Compléter / Vrai ou faux /
  Former une phrase / Reformuler / Traduire / Écrire / Associer).
  The one CJK line left in build code, `svglib.py` line 120, is a dead-code
  illustration comment (never rendered); the rendered SVGs contain zero
  CJK characters (freeze diff: edition CJK = 0 on all 8 pages).

## 2. Furniture (verbatim from the shipped W43 ES×FR edition, VOL.1→VOL.2 only)

Source of every string: the shipped W43 SVGs in
`files/weekly-report-es-fr/svg/` (+ that edition's KIT §2); where a
W43 string and a generic column note conflicted, the shipped SVG won.

- Masthead: **La Lucerna**
- P1 badge (brick #a4553a, 20px bold, subtitle slot y=372, replaces the
  core tagline line): `TEXTES EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`
- P1 edition line (46px): `HEBDOMADAIRE ESPAGNOL · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL`
- P1 top strip: `CADA SEMANA EN ESPAÑOL · CHAQUE SEMAINE · L'ESPAGNOL DES ESPAGNOLS`
- P1 band right lines: `PLUS QUE 27 JOURS AVANT LE 29-N · LE LOGEMENT DÉCIDE` / `À LA UNE · VOIR PAGES 2 ET 6`
- Section heads: `VIDA · VIE QUOTIDIENNE`, `CULTURA · CULTURE`,
  `DEPORTE · SPORT`, `JUVENTUD · JEUNESSE`, `A FONDO · EN PROFONDEUR`,
  `LENGUA · LANGUE`, `EJERCICIOS Y RESPUESTAS · EXERCICES ET RÉPONSES`;
  band subtitles: French second half (e.g. P7 `Focus langue · Tres niveles, tres herramientas · Trois niveaux, trois outils`, P8 `Page 8 · La gran prueba de la semana + todas las respuestas`).
- Box/section second halves follow W43 verbatim: `LA SEMANA EN CIFRAS · EN CHIFFRES`, `EL CALENDARIO · LE CALENDRIER`, `EN ESTA EDICIÓN · SOMMAIRE`, `BREVES · EN BREF`, `QUIZ RELÁMPAGO · QUIZ ÉCLAIR`, `LA NOTICIA · À LA UNE`, `AHORA TÚ · À TOI DE JOUER`, `ERRORES TÍPICOS · ERREURS TYPES`, `LA PALABRA · MOT DE LA SEMAINE`, `FRASES DE LA SEMANA · PHRASES DE LA SEMAINE (MOT POUR MOT, TIRÉES DE CE NUMÉRO)`, `LA PRÓXIMA SEMANA · LA SEMAINE PROCHAINE (VOL.3)`, `EJERCICIOS · EXERCICES`, `RESPUESTAS · CORRIGÉS — classés par page, cherchez le numéro` (+ right note `Une courte explication en français pour chaque exercice · ✓ = exercice d'écriture`).
- Footers, all 8 pages: `La Lucerna · HEBDOMADAIRE ESPAGNOL VOL.2 · TEXTE EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS` and `Page N sur 8`.
- Gloss prefix: `Note — ` (vocab boxes use `terme = gloss` entries).
- P8 separator stays Spanish, frozen from the core (W43 precedent):
  `— PÁGINA N —`. Exercise-page right note (W43 verbatim):
  `Réponses page 8 · Exercices mélangés par niveau, cherchez par numéro`.

## 3. Registry verification & key-diff adjudication

- **150 exercises — A2 50 · B1 72 · B2 28; per page 10/18/18/18/18/18/12/38;
  page/level/type identical to core for all 150.**
- `tools/p8.py compare` (explicit `--core-p8/--edition-p8`, total 150):
  **CLEAN, 150 = 150, missing = [], extra = 0**, keydiff list of 34.
  Adjudication, item by item, against the *printed* `N. key — note`
  lines (first-dash split, byte comparison):
  - **148/150 keys byte-identical to the core.** The 32 non-137/138
    keydiff entries (17, 18, 20, 25, 26, 27, 28, 52, 53, 54, 55, 60, 61,
    62, 63, 83, 85, 93, 94, 95, 96, 98, 107, 109, 110, 111, 117, 141, 142,
    143, 144, 148) are a **tool extraction artifact**: every one of those
    French notes ends in an ASCII paren group (`(singulier)`,
    `(pluriel)`, `(passé)`, `(b)` …), and `p8.py`'s paren branch then
    mis-extracts the key (README #13 class: suspect the tool before the
    edition). Printed keys verified byte-identical.
  - **Exactly 2 real key changes, the W43 ES×FR KIT §3 precedent
    (translation items re-aimed ES→reader language):**
    - **#137** key core `周一在九个自治区是假日。` →
      **`Le lundi est férié dans neuf communautés.`**
      (note `d'après le texte`)
    - **#138** key core `周日我们看 NFL 和马竞–巴萨。` →
      **`Le dimanche, nous regardons la NFL et l'Atlético–Barça.`**
      (note `d'après le texte`)
  - **#139/#140** (reverse direction): stems re-aimed at French
    (`Le Bernabéu accueille un match de la NFL. → ___`,
    `Chaque graphique doit indiquer sa source. → ___`); **Spanish keys
    byte-identical to the core** — same pairing as W43 §3.
  - **#150** (Écrire, apparatus line): renders
    `150. ✓ Texte modèle dans la section H de cette page (84 mots)`
    (W43 wording with the W45 word count 84, not 82).
  - One language-neutral note kept identical to the core: P6 §A
    `34 + 22,2 + 17,1 = 73,3` (digits only).
- **Frozen-text diff** (`tools/freeze.py diff --strict-cjk`, core vs
  edition): **added CJK = 0 on all 8 pages** (core CJK 170/280/161/169/
  247/80/388/981 → edition 0). Every removed non-CJK string adjudicated:
  (a) the P1 tagline line, replaced by the badge per §2; (b) re-wrap
  segmentation fragments of frozen Spanish lines whose words survive
  verbatim in the French render (P2 calendar box, P5 plan box, P7 letter
  re-wrap after the paren change, P8 answer-line wraps) — each fragment
  verified present in the edition's joined text; (c) P8 answer segments
  whose keys are verified byte-identical above. No Spanish token was
  added or removed: source-tree diff core-build vs this build touches
  only `bslib4.py`, the five content files and `render.py` (OUT +
  filenames); every changed line is explanation text, furniture, the
  §5 layout parameters, or the two apparatus items below.
- **Apparatus-only Spanish-line changes (2, both documented):**
  (1) P7 letter attribution parens full-width → ASCII
  (`(ejemplo, escrito por la redacción)`) — W43 ES×FR shipped ASCII
  parens and W45 ES×EN ruling 2 did the same; letter body, name Ana and
  place Shanghái frozen. (2) Nothing else: no reader, letter or quote
  was invented; the P7 letter remains the labelled editors' example and
  the FIX1 disclosure (Spanish frozen, French note translated) still
  states that no real letters or best P8 texts had arrived, promise
  carried to VOL.3.

## 4. P7 phrases

All 8 Spanish quotes verified verbatim in **both** their article page and
P7, each appearing exactly **2 times** across the 8 SVGs (programmatic
count, normalized whitespace), with correct page tags: Página 1, 2, 3,
4, 5, 6, 6, 1. Glosses are the French translations.

## 5. Fit defects found in-build and fixed (French apparatus only; core geometry and Spanish text untouched)

1. **P8 answer flow overflow** (French notes longer): answer lines
   13.5pt/1.16 → **13.2pt/1.12**, separators 1.16 → 1.12 (W45 ES×EN §3.2
   precedent). Dash style `N. key — note` and `N. ✓ note` unchanged.
2. **P6 exercise flow overflow** (+82px): §A bridge shortened to the W43
   verbatim `Regardez les graphiques et choisissez.` (1 line); §D
   bridge shortened to `Complétez avec : sondeo · muestra · indecisos · margen de error`
   (2 lines, word list kept); exercise gap 3→1 on all 18 size-19 items
   (W43 ES×FR §5.4 precedent).
3. **P1 CIFRAS box-title crossing** (ink 976.8 > border 961.0): title
   size 23→21 (`tsize=21`, W43 §5.1 precedent); final margin 21.7px.
4. **P5 plan box-title crossing** (ink 1020.2 > border 961.0): title
   shortened to `EL PLAN DEL PUENTE · LE PLAN` (W45 ES×EN §3.5
   precedent); final margin 49.5px.
5. **P7 clinic box-title crossing** (ink 1893.0 > border 1885.0): title
   size 23→20 (W43 §5.5 precedent, ink 365.3px).
6. **P1 word-note LINEX** (2nd line crossed the y=1844 rule): note
   shortened to one line `La précampagne : avant la campagne officielle.`
   (413.6px ≤ 434px).
7. **P7 column-3 overflow** (French notes pushed the quotes block and
   the preview box over the footer rule; preview was at y=2609):
   trimmed exactly 169.04px so col-3 ends at the core's 1820.08 + 2px box
   slack (final 1822.08): palabra note 4→2 lines, clinic notes #3/#4
   2→1 lines each, disclosure note 6→4 lines (all three disclosure
   facts kept: no real letters, no best P8 texts, example printed +
   promise to VOL.3 + invitation). Preview now at y=2442.08, bottom
   2560.08 (19.9px clear of the 2580 footer rule).
8. **P7 palabra box-bottom graze** (ink 1255.1 > border 1254.6 by 0.5px,
   Latin descenders where the core's CJK ink has none): box height +2px.

Final full build: **zero FLOW OVERFLOW / zero HEAD TOO WIDE** on all
8 pages.

## 6. Geometric occlusion audit (SOP gate) + companion scans

- `tools/occlusion_audit.py` (selftest passed: all 6 planted classes
  fired, clean controls silent): first run 5 flags (all French apparatus,
  §5.3–5.7), all fixed; **final run 0 flags, --core comparison NEW
  flags = 0** (core control: 0 flags).
- Same-baseline ink scan (FR×RU rowcheck method, <6px threshold): 7
  hits, **identical to the core control run** — the P1 sommaire rows,
  where `Pág. N` and its title sit at a deliberate +4.0px ink gap
  (positive gap, no overlap). No furniture-band collision; no new
  same-baseline defect.
- P6 chart element check: chart-zone rects (10) and texts (23)
  **byte-identical to the core**; no chart geometry moved.
- **Known frozen-core defect, preserved not repaired (coordinator's
  ruling):** the P6 second chart's `Inmigración` label is pressed ~5px
  by its bar (label ink ends 1144.4, bar starts 1139 → 5.36px overlap).
  This is frozen core geometry, present identically in the shipped
  core; it was deliberately NOT repaired here.
- Gloss counting (split on `·` itself, README #21): core 19 = edition
  19, per box 5/5/5/4, item by item.
- Images: P3 chestnuts and P5 pumpkin payloads byte-identical to the
  core (same href hashes, same x/y/w/h); P1 houses illustration is the
  core's code-drawn `illus_houses()` (code untouched); credit lines
  unchanged (Spanish apparatus of the frozen core).

## 7. Deliverables (`files/weekly-report-w45-es-fr/`)

- `svg/` ×8, `cards/` ×8 (1950×2700 PNG, all verified)
- Print PDF: `La-Lucerna-VOL2-FR.pdf` — **7,157,921 bytes**,
  sha256 `30f599889883a7b1d22068a9b0de2240b8da329bdf36376f0c7f8fa9c1d76dd7`,
  8 pages
- Web PDF: `La-Lucerna-VOL2-FR-web.pdf` — **3,732,117 bytes** (< 10 MB),
  sha256 `4fe17f4c8054a368fc42657e2c185e5b0ab544e108d3c9f9168933fc08a4c722`,
  8 pages
- `WEEKLY-KIT.md` (this file), `ABSTRACT.txt` (French, one line, no
  ASCII double quotes)

## 8. SVG hashes (delivered edition + core baseline)

Delivered edition:
- p1 `e69c0ccebf4a6b723b8553d945ee79f54754156afcdb266ad0cb2f9464f248e5`
- p2 `7a0cba42b2095eb50aacba099aa8a103dd47f227c2f3688708b98e16dae5b7dd`
- p3 `9a762bb5c40f21ed507a17215a1d6bbc510e4a15ed7b54a19a67bad620fe1836`
- p4 `15d333c123d07513a712f782baea2b8ca9c2e2ee952166d3c80a65a4108e2e91`
- p5 `cde8920ba54a7d81d0bfcad8e71dc23aa8e8ab332889f3f728389ee06f159e74`
- p6 `9d9a981db5528254634f4f4450e83741d3da430bdc7e3bdd588623aeae5393e9`
- p7 `552938aee3a15cdd84292058c15ec553b6a5a92d16fd625da22f3ca532cab431`
- p8 `d9774e72e48853c1f30b221f8a68d1aa23d9a2b3ea85b5d1a241f5988cbf9d9f`

Core baseline (re-hashed after the final build, unchanged):
- p1 `a1b3010296ad129e45d2816637762cec4f25635ff43ea2197e08e0efd0daf34d`
- p2 `10e78c2e6cb295198cce99ed6182cf2472511da267ddeb9bf4379d464f0bb724`
- p3 `5986ba9e318c985e14d33abb6e9277f22bf7c0c6a961f94501cdfa46b655aa8b`
- p4 `1894836e06be824b1dc3a3ac46474ccced7495679f23aabc0f27808c63617a67`
- p5 `cd15c68b5f8db752b6bc62346dd22826d19513d41fab16f2a2f7c119a3893fd2`
- p6 `fcfccf8267e10cc7ddbf14d5aa9dd735cf1c73a110f4fe8ec38d8e9aef07b280`
- p7 `b1774024b6a17353d18a7b9b13f4be14ce8a6a4ca1b8f2565e06fafb0a90a8fe`
- p8 `d1c46fa439ac505db6e2708df8206f10d7046947064172dfcde22e74d7545147`

Audit records: `hidden_files/w45-es-fr-diff.json` (freeze diff),
`hidden_files/w45-es-fr-occlusion.json` (final 0-flag audit),
`hidden_files/w45-es-fr-transform.py` (asserted transform, from-scratch
verified), `hidden_files/w45-es-fr-rowcheck.py` (same-baseline scan).

## 9. Open gate

**Independent proofread has NOT run — marked PENDING.** No GitHub repo
insert and no Discord post were made (parent handles both after the
proofread passes). No final-edition claim is made here.

## Coordinator adjudication (2026-10-27, binding — documentation only, no render change)

**Badge size 20px: ACCEPTED as-is, no change. This edition is FINALIZED.** Independent proof three-way measurement: edition badge 20px, W43 shipped same-pairing badge 20px, README #20 says 19.5pt. The edition badge element is BYTE-IDENTICAL to the W43 shipped SVG (string, slot y=372, size, bold, color #a4553a all identical), and W43 same-pairing KIT §2 also records 20px. Furniture rule = copy the W43 shipped same-pairing SVG verbatim; README #20's 19.5pt describes the EN-core instance, not the FR column (same principle as the es-de badge-slot adjudication). Forcing 19.5pt would deviate from the shipped same-pairing precedent for no reader benefit. **Future ES×FR proofs must NOT re-flag badge size.** Two brief-record corrections (non-defects): the W43 translation-redirection precedent is in W43 KIT §3, not §5 (§5 is the layout-defects section) — the builder's §3 citation was correct; and the language-neutral identical notes are 2 (#19, #87), not 1 as the builder's main text states — an undercount with no effect on any conclusion.
