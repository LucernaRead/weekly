# La Lucerna — HEBDOMADAIRE ESPAGNOL VOL.1 · ES × FR

**Pairing:** Spanish target text (frozen W43 core, `files/weekly-report-es-vol1/`) + explanation layer written natively in **French**, for francophone readers.
**Status:** builder-complete. **Independent proofread: PENDING** (parent runs it; repo insert + Discord posting happen only after it passes — not done here).

## 1. Method & baseline proof

- Build dir: `hidden_files/weekly-report-es-fr-build/` — a copy of the core build (`weekly-report-es-build/`).
- **Baseline proven before any edit:** the unmodified copy reproduced all 8 shipped core SVGs byte-identically (sha256 set recorded during the build).
- Only the explanation layer was rewritten (asserted-replacement scripts, abort-on-mismatch, per content file). Spanish target text is byte-identical to the core, with the documented exceptions in §3.
- Visible-text multiset diff vs core: every removed non-Chinese string adjudicated — (a) the Spanish tagline line on P1, replaced by the pairing badge per spec; (b) two re-wrap segmentation artifacts (same words, different line-break segment); (c) two segments of removed Chinese explanation lines whose Spanish words survive inside the French replacement.
- CJK scan of all 8 final SVGs (ideographs, U+3000–303F punctuation, fullwidth FF00–FFEF, U+FFFD): **zero**.
- Banned intermediary term: absent from paper, this KIT, and all build code (the inherited code method was renamed `expl()`).
- Images: the 3 embedded payloads (P1 NIST clock, P3 chestnuts, P5 Halloween postcard) are byte-identical to the core; credit lines unchanged (Spanish apparatus of the frozen core).

## 2. Furniture (as rendered)

- Masthead: **La Lucerna**
- P1 badge (brick #a4553a, 20px bold, replaces the tagline line): `TEXTES EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES` (ink 1026px ≤ 1820)
- P1 edition line (46px, ink 1600px ≤ 1820 — the HEBDOMADAIRE variant fits for ES): `HEBDOMADAIRE ESPAGNOL · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1`
- P1 top strip: `CADA SEMANA EN ESPAÑOL · CHAQUE SEMAINE · L'ESPAGNOL DES ESPAGNOLS`
- P1 band right lines: `UNE HEURE DE SOMMEIL EN PLUS · ET LE CLÁSICO` / `TROIS RENDEZ-VOUS EN UNE NUIT · PAGES 2 ET 4`
- Footers, all 8 pages: `La Lucerna · HEBDOMADAIRE ESPAGNOL VOL.1 · TEXTE EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS` and `Page N sur 8`
- Gloss prefix: `Note — ` (vocab boxes use `terme = gloss` entries); answer-key typography: space before each note parenthesis, half-width parens only.
- Instruction labels: Compléter / Vrai ou faux / Former une phrase / Reformuler / Traduire / Écrire / Associer.

## 3. Registry verification & key-diff registry

- **150 exercises — A2 52 · B1 70 · B2 28; per page 10/18/18/18/18/18/12/38; page/level/type identical to core for all 150 (programmatic diff: zero diffs).**
- **Key changes — exactly 3, all documented fan-out exceptions:**
  - **#137** (Traduire, ES→reader language): key core `周日我们多睡一个小时。` → **`Le dimanche, nous dormons une heure de plus.`** (note `Traduction (texte page 1)`)
  - **#138** (Traduire): key core `周一在九个自治区是假日。` → **`Le lundi est férié dans neuf régions.`** (note `Traduction (texte page 3)`)
  - **#150** (Écrire, apparatus line): key core `（开放题，范文如下）` → **`Question ouverte — texte modèle ci-dessous sur cette page`**
- Exercises #139/#140 are translation items in the reverse direction (reader language → Spanish): their **stems** were re-aimed at French (`Le Clásico se joue le dimanche soir à neuf heures. → ___`, `Chaque graphique doit indiquer sa source. → ___`); their **Spanish keys are byte-identical to the core**.
- Answer notes: 144 of 150 translated into French; 6 notes identical to core because they are language-neutral (#60–63 conjugation arrows, #87 arithmetic, #103 pronoun note).
- Sample re-solve across all pages against the French keys: consistent with the articles (clock change 03:00→02:00 peninsula / 02:00→01:00 Canaries; El Clásico Sun Oct 25, 21:00, Camp Nou; F1 Austin same hour; European goals total **40**; CIS PSOE 34.0 %; Demócrata sum 77.2 %; Halloween Sat Oct 31; elections Nov 29).

## 4. P7 phrases

All 8 Spanish quotes verified verbatim (normalized text join) in **both** their article page and P7, with correct page tags: Página 1, 2, 2, 4, 3, 3, 5, 6. Glosses are the French translations.

## 5. Fit defects found in-build and fixed (French apparatus only; core geometry and Spanish text untouched)

1. **P1 box title overflow (box-title audit catch):** `LA SEMANA EN CIFRAS · EN CHIFFRES` struck **15.8px past its box border** → set that box's title size 23→21 (`tsize=21`, FRASE-box precedent). Final audit: 0 crossings; tightest remaining title margin 15.8px (P7 palabra).
2. **P2 FRASE box title:** `FRASE PARA RECORDAR · À RETENIR` at `tsize=20` (dropped "LA", ES×DE precedent); ink 363.5px ≤ 395px inner width.
3. **P3 §D explanation** shortened to `Formez une phrase avec ces mots.` — exercise flow end back to the core's y=2552.
4. **P6 exercises overflow:** §A explanation shortened to `Regardez les graphiques et choisissez.` (1 line) and the P6 exercise gap reduced 3→1 on all 18 size-19 items (ES×DE precedent). Flow ends y=2561 < 2580.
5. **P7 column-3 parity** (must end at the core's exact y=1663.96): clinic notes shortened — `Seule la una prend es; le reste, son.` / `État du jour: estar. Ser = ennuyeux.` / `gente: collectif, verbe au singulier.`; letter note `Lettre d'exemple. VOL.2: vraies lettres et meilleurs textes — écris-nous!` — all matched to the core's wrap-line counts. Clinic title `ERRORES TÍPICOS · ERREURS TYPES` at size 20 (ink 365.3px); palabra title `LA PALABRA · MOT DE LA SEMAINE` at 23 (396.2px).
6. **P8 answer flow:** 11 answer notes shortened to restore one-line answers (#30 `9 régions seulement en congé le lundi`, #32, #33, #43 `verbe en 2e position`, #44 `le lieu, à la fin`, #45 `lieu 1er, verbe 2e`, #64 `ir → fueron, comme ser`, #80, #81, #128 `la DANA Adam, première tempête nommée`). Net answer-line delta vs core = **+1** (only #137, a full-sentence key, wraps to 2 lines — ES×DE precedent). Key flow ends y=2518 ≤ 2552; all four columns clear the y=2580 footer rule.

Final full build: **zero flow-overflow warnings** on all 8 pages.

## 6. Geometric occlusion audit (SOP gate)

Tooling: `audit_es_fr.py` (paint-order scan, PIL/svglib production font metrics, ink band baseline −0.88em…+0.30em, **line boxes expanded by half stroke width**), validated first on synthetic positive controls (COVER, LINEX and FOOTER controls all fired; a clean text passed). Companion scans: `audit_titles.py` (ink vs its own box border), `audit_texttext.py`.

- Coverage/footer/edge/line scan: **1 flag, inherited from the core control run (identical flag)** — P1 palabra gloss line 2 (baseline 1842) vs the full-width rule at y=1844. **Pixel-adjudicated on the rendered card: gloss ink occupies rows ≤1842, rows 1843–1844 contain zero dark pixels in the box range, rule top ≈1843.4 → ≥1px clear air, no glyph contact. NON-DEFECT** (same geometry and standard as the ES×EN core adjudication: ink 1830–1842 vs rule 1843–1844, overlap 0).
- Text–text scan: 1 flag — wordmark `La Lucerna` vs P1 edition line, the known 168pt ink-band model artifact. Pixel measurement: wordmark ink bottom row 264, edition-line ink top row 286 → **22px clear gap. NON-DEFECT.**
- Box-title scan: 1 crossing found and fixed (§5.1); final run **0 crossings**.
- All 8 final cards viewed visually: no occlusion, no overflow, no clipped text.

## 7. Deliverables (`files/weekly-report-es-fr/`)

- `svg/` ×8, `cards/` ×8 (1950×2700 PNG)
- Print PDF: `La-Lucerna-VOL1-FR.pdf` — **5,796,417 bytes**, sha256 `5538322b587f86399bdaecf6232d61798e721ce9e07e6c39c85b171510fe8dac`, 8 pages
- Web PDF: `La-Lucerna-VOL1-FR-web.pdf` — **3,921,553 bytes** (< 10 MB), sha256 `f3c80268bc2b16a731a0b7cf130c2faa113dae3f209ac34030ba60f2bb0dae42`, 8 pages

## 8. Open gate

**Independent proofread has NOT run — marked PENDING.** No GitHub repo insert and no Discord post were made (parent handles both after the proofread passes).

## 9. Factual correction (2026-10-21): P5 "jueves 23" → "viernes 23"

- **Error:** the P5 article (Spanish text, byte-identical to the core) said the eFootball jersey is playable "desde el jueves 23" — 23 October 2026 is a **Friday**. Found by this edition's independent proofreader; fixed the same day in the core and in all three ES fan-outs (EN/DE/FR). This edition's change is one word in `content56.py` line 19.
- **Verification:** baseline proven first (unmodified build reproduced all 8 shipped SVGs byte-identically). Rendered diff = exactly one text element in `p5-juventud.svg` (same line, y=1504.82); the other 7 SVGs and 7 cards are byte-identical, only the P5 card re-rendered. Registry sweep: no exercise stem/key/note cites the weekday; #80 (key Verdadero, stem says only "desde el 23 de octubre") re-solved — still holds; P7's phrase quotes only "sábado 24" (correct). All other weekday claims in the text check out against the 2026 calendar. Geometry: changed-line ink 433→446px, 53px clear of the column edge; occlusion audit = 0 flags on P5 (the single P1 model flag is pre-existing and pixel-adjudicated a non-defect — gloss ink ≤ row 1842, rule rows 1843–1844 clear).
- **Deliverables (corrected; supersede §7):** Print PDF `La-Lucerna-VOL1-FR.pdf` — **5,796,412 bytes**, sha256 `beb37696fed50384172f6c35a1135cfba2b30ca74a0717aba4dae82ff49ef158`, 8 pages. Web PDF `La-Lucerna-VOL1-FR-web.pdf` — **3,921,696 bytes** (< 10 MB), sha256 `fb1ca823a03f8f42a4264eb4806ffd2b4285d028d471471dc4f365103aaf9de8`, 8 pages. The GitHub repo entry `2026-w43-es-fr` was re-pinned to the corrected PDF with a correction note.
