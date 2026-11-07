# Lucerna Weekly — Russian VOL.1 · French edition (RU × FR)

The Russian core issue (VOL.1, «Первый снег») reissued for French-speaking readers:
**Russian target text (frozen core) + explanations written natively in French**
（目标语正文 = 俄语核心冻结；讲解 = 法语母语原生撰写）.

- Week: 19–25 October 2026 · VOL.1
- Pages: 8 (1950×2700), warm ivory — identical layout to the core
- Exercises: **150** — A2 54 · B1 72 · B2 24 (registry identical to the core)
- Print PDF: `Lucerna-VOL1-FR.pdf` (22,574,325 B, sha256 `bac9302fa89a2918ef31cca755bb8a10337ad528183bdc03a3632077ab22a54d`)
- Web PDF: `Lucerna-VOL1-FR-web.pdf` (3,674,650 B < 10 MB, sha256 `acb965f6be666ad5806b3ddd3552f2f9ccc853c92ddf292f4a2f997d086a10c9`)
- Build: `hidden_files/weekly-report-ru-fr-build/` (seeded from the RU × DE build; see §2 for the core-conformance audit of that seed)

## 1. Method

Fan-out of the frozen Russian core (`files/weekly-report-ru-vol1/`). The explanation
layer (glosses, grammar notes, instructions, all 150 answer notes) was rewritten
natively in French; the Russian target text is byte-identical to the core.
The build was first proven to reproduce all 8 shipped core SVGs byte-identically
from an unmodified copy of the core build before any change was made.

## 2. Seed-source audit (per parent instruction)

The build was seeded from the RU × DE build files (they isolate every
explanation-layer string position for this core). The baseline and the final
freeze diff for this edition are against the **core**, not the sibling:

- Registry diff vs core: computed programmatically (§3) — keys differ only at the
  documented re-aims #137, #138, #150.
- Numeric-parameter audit: the ordered numeric-literal sequences of all build
  files (`bslib4.py`, `content12/34/56/7/8.py`, `svglib.py`) were compared
  against the **core build**. Result: **identical everywhere except one value** —
  `content12.py`, the P1 badge line font size 19 → 20 (with bold + brick fill),
  which is the documented badge substitution (§4), not DE-specific geometry.
  **No DE-inherited geometry differs from the core.**
- Text-element multiset diff per page (FR SVGs vs core SVGs): every difference is
  explanation-layer or §4 furniture. The only pure-Cyrillic removal on any page is
  the P1 strap subtitle, replaced by the French badge (§4). Wrap-segmentation
  differences in flowing apparatus (P7 «(Страница 2)» tag element; P8 keys-flow
  fragments «стихи Пушкина» / «Пушкина», and key line #97) are line-break
  artefacts of the French notes' lengths; the registry verifies every key string
  is present verbatim in the render (149/150 directly; #150 prints as the ✓ note
  line by design, as in the core).
- Image payloads: byte-identical to the core on all 8 pages (data-URI comparison).

## 3. Registry & key-diff vs the CORE

150 exercises; levels A2 54 · B1 72 · B2 24; per page 10/18/18/18/18/18/12/38;
writing model 82 words — all identical to the core registry (n/page/level asserted
equal for all 150). **Key changes (complete list — re-aimed translation items):**

| # | Core key | FR key | Why |
|---|----------|--------|-----|
| 137 | 星期日中央陆军将对阵斯巴达克。| Le dimanche, le CSKA joue contre le Spartak. | RU→reader-language translation; now targets French. Note: «Comparez page 4» |
| 138 | 预报员预报十月末有雨夹雪。| Les services météo promettent de la neige fondante pour la fin octobre. | Same re-aim. Note: «мокрый снег = la neige fondante» |
| 150 | （开放题，范文如下）| (Question ouverte — texte modèle ci-dessous) | Apparatus line. Note: «Le texte modèle se trouve dans la section H de cette page (82 mots)» |

#139/#140: prompts re-aimed into French («Les vacances commencent samedi — douze
jours en tout. → ___»; «Je souhaite à mon papa une bonne fête des pères ! → ___»);
their Russian keys are byte-identical to the core. Every other key is
byte-identical to the core; all remaining registry diffs are note-text only
(Chinese → French). French typography: space before each note parenthesis,
half-width parentheses only.

## 4. Furniture (French column)

- Badge (20 pt bold, brick #a4553a, in place of the core's strap subtitle):
  «TEXTES EN RUSSE · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES»
  (measured 985.6 px ≤ 1820 at build time)
- Masthead: «Lucerna» — no article (Russian takes none, as in the core)
- P1 edition line: «HEBDOMADAIRE RUSSE · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ»
  (measured 1474.6 px ≤ 1820 — the HEBDOMADAIRE variant fits; no short variant needed)
- Top strip centre: «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · CHAQUE SEMAINE · LE RUSSE QUE LIT LA RUSSIE»
- Footers, all 8 pages: «Lucerna · HEBDOMADAIRE RUSSE VOL.1 · TEXTE EN RUSSE · EXPLICATIONS EN FRANÇAIS» / «Page N sur 8»
- Exercise types localized: Compléter / Choix / Appariement / Phrases / Transformation /
  Cloze (P8) / Traduction / Rédaction; instructions: Compléter / Associer / Former la phrase / Transformer / Traduire en français / Traduire en russe / Écrire
- P6 chart disclaimer appended in French: «Un sondage d'exercice de la rédaction, pour s'entraîner — pas de vraies statistiques.»

## 5. Fit shortenings (French apparatus only — no core geometry or Russian moved)

- **P7 column 3** initially ended at 1738.48 (core: 1682.96), crossing the phrases
  rule at y=1698. Two French strings were shortened:
  - error-clinic note #4: «Génitif après « с » (le début) : с первого октября.» (2 lines)
    → «Après « с », le génitif : с первого октября.» (1 line)
  - readers'-corner note: «Exemple de la rédaction, pas une vraie lettre. Dans VOL.2 : de
    vraies lettres et les meilleurs textes !» (3 lines) →
    «Exemple fictif de la rédaction. VOL.2 : vraies lettres et meilleurs textes !» (2 lines;
    both VOL.2 promises kept)
  After the fix P7 col 3 ends at exactly **1682.96** — core parity, 15 px clear of the rule.
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings. The `P6-ex ended y=2594
  (bottom 2580)` cursor reading is identical in the shipped RU × DE build and is a
  trailing-gap cursor artefact: the geometric audit and the viewed card show the last
  P6 items (##99–100) ending well above the footer rule — not a defect.
- P8 keys flow: zero overflows; French notes are compact by design.

## 6. Audits

- **Geometric occlusion audit** (`audit_ru_fr.py`, paint order, production-font
  metrics, **stroke-expanded line boxes** — half stroke width each side; validated
  on synthetic positive controls: a zero-height `<line>` crossing and a covering
  rect are both detected): **1 flag**, the known P2 designed adjacency — the weather
  reminder line (baseline 1800) vs the twin rules at rows 1803–1804.
  **Pixel-adjudicated on the rendered card: the line's ink ends at row 1802; the
  rules occupy 1803–1804; zero contact** — identical to the core / RU × EN / RU × DE
  measurement. Non-defect. Effective flags: **0**.
- **Box-title vs border check** (dedicated pass: every bordered box's four edges,
  stroke-expanded, against every text ink band): **0 crossings** on all 8 pages.
- **Page-edge spill**: covered by the main audit — **0**.
- **CJK scan**: 0 CJK characters in all 8 final SVGs (Cyrillic + Latin only).
  The banned intermediary term appears nowhere in the paper, this KIT, or the
  build code (the inherited gloss method was renamed `expl()`).
- **All 8 cards viewed** — layout, French apparatus and footers verified visually.

## 7. Content verification

- **Weekday claims re-checked against the real 2026 calendar — all correct, no
  inherited weekday error found**: forecast window opens Wednesday 21 Oct; films
  Thursday 22 Oct; last school day / matchday 12 opens Friday 23 Oct; holidays
  Saturday 24 Oct – Wednesday 4 Nov = 12 days (span verified arithmetically);
  derby Sunday 25 Oct 16:00; Lyceum Day Monday 19 Oct; Father's Day Sunday 18 Oct;
  Grandparents' Day Wednesday 28 Oct; Halloween Saturday 31 Oct; ministry window
  Mon 26 Oct – Tue 3 Nov; school resumes Thursday 5 Nov; P6 calendar strip letters
  all 12 correct.
- **P7 phrases**: all 8 Russian quotes occur exactly 2× in the issue (article +
  phrases section), byte-verbatim, with correct (Страница N) tags.
- **Re-solve sample** (against the French keys, spanning all pages): #8 B (24 Oct =
  Saturday), #48 B (derby 16:00), #66 C (31 Oct = Saturday), #85 B (chart: most
  visit grandparents, 34 %), #97–100 transformations, #124 A (matchday opens Fri
  23 Oct), #137/#138 (French keys are faithful translations of the Russian
  prompts), #146 A (22 Oct = Thursday), #150 (model text present, 82 words).
- Facts unchanged from the core: «Первый снег» first-snow lead, 21–23 Oct forecast,
  four fairy-tale films Thu 22 Oct, Lyceum Day 1811 (215 years), Dynamo 25 / Zenit
  24 / Spartak 23, 900 ₽ ticket, 34/28/22/16 chart labelled exercise data in both
  languages. Russian domestic life only; no politics.

## 8. Proofread status

**PASSED — independent proofread, one complete pass, ZERO problems (2026-10-21).**

Independent proofreader's record (fresh pass over the shipped artifacts, trusting
nothing in §§1–7; baseline = the frozen CORE `files/weekly-report-ru-vol1/`):

1. **Freeze diff vs core.** Both builds re-run in isolation: the core build
   reproduces the shipped core SVGs byte-identically and the FR build reproduces
   the shipped FR SVGs byte-identically (baseline method sound). Per-page
   text-element multiset diff: every difference is explanation layer, §4 pairing
   furniture, or a §3 registry item. Pure-Cyrillic diff analysis: FR-only
   Cyrillic elements are exactly 4 — the documented wrap artefacts (P7
   «(Страница 2)» tag; P8 «стихи Пушкина» fragment; key lines #97/#140 split
   points). **No Russian target-text change outside the registry.**
2. **French apparatus completeness.** 0 CJK characters in all 8 final SVGs
   (text layer and raw bytes); no German residuals (the only substring hits are
   French «leader» contexts); all 150 P8 notes in French — 142 rewritten from the
   core's Chinese, 8 identical notes are language-neutral Russian verb-form notes
   («выпасть → выпадет» etc.), correct as-is. Instructions, glosses, section
   furniture in French on every page; all 8 cards viewed.
3. **Keys re-derived.** Registry comparison (both registries regenerated from
   source): key-only diffs = **#137, #138, #150 exactly** — the documented
   re-aims; #139/#140 keys byte-identical with prompts re-aimed into French
   (verified in the render); #137/#138 French keys verified as faithful
   translations of the printed Russian prompts («В воскресенье ЦСКА играет со
   «Спартаком».» / «Синоптики обещают мокрый снег в конце октября.»).
   Independent re-solve from the FR render: all five matching sets (25–28,
   39–42, 57–60, 75–78, 141–144), dialogue cloze 145–149, and MC spots #8 (B,
   Sat 24 Oct), #48 (B, 16:00), #66 (C, Sat 31 Oct), #85 (B, chart 34 %),
   #124 (A, Fri 23 Oct) — all correct. Model text: 82 words, byte-identical
   to the core.
4. **Totals.** 150 exercises — A2 54 · B1 72 · B2 24; per page
   10/18/18/18/18/18/12/38; unified numbering 1–150 continuous, no gaps/dupes
   in both registries.
5. **P7 phrases.** All 8 Russian quotes occur exactly 2× in the rendered issue
   (article + phrases section), byte-verbatim contiguous excerpts, each present
   on its tagged page — tags (Страница 1, 2, 2, 3, 3, 4, 5, 6) all correct.
6. **Weekdays/dates vs the real 2026 calendar — all correct:** forecast opens
   Wed 21 Oct; films Thu 22 Oct; last school day / round 12 opens Fri 23 Oct;
   holidays Sat 24 Oct – Wed 4 Nov = 12 days (re-counted); ministry window
   Mon 26 Oct – Tue 3 Nov = 9 days; derby Sun 25 Oct; Lyceum Day Mon 19 Oct;
   Father's Day Sun 18 Oct; Grandparents' Day Wed 28 Oct; Halloween Sat 31 Oct;
   school resumes Thu 5 Nov; 2026 − 1811 = 215; chart 34+28+22+16 = 100; P6
   calendar strip's 12 weekday letters all correct.
7. **Pairing furniture.** P1 badge present («TEXTES EN RUSSE · EXPLICATIONS EN
   FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES»); pairing footers +
   «Page N sur 8» on all 8 pages; masthead «Lucerna» with **no article**
   («Le Lucerna» absent everywhere).
8. **Geometric occlusion audit (proofreader's own run).** The audit script was
   first validated on synthetic positive controls (a covering rect detected at
   100 %; a zero-height `<line>` crossing detected via stroke-expanded line
   boxes). FR result: **1 raw flag** — P2 reminder line (baseline 1800) vs the
   rule at y=1804. Pixel-adjudicated on the FR card: the text's dark ink ends
   by row 1799 (rows 1800–1802 carry only 16–20 sparse descender pixels across
   the full width); rule rows 1803–1805 carry background-level dark counts
   (8 px, identical to empty rows 1806–1815); maximum dark run in rows
   1800–1815 is 4 px — **no rendered contact; non-defect**, identical to the
   core's measurement (the core returns the same single flag). Dedicated
   box-title-vs-border scan: **0 crossings** on all 8 pages. Page-edge spill:
   0. Footer band (y>2580): 0.
9. **Images & PDFs.** Image payloads byte-identical to the core on all 8 pages;
   credits present on every image page and matching the placed images (Yuon P1,
   Bentley P2, Kiprensky + Bilibin P3, 1912 squad PD note P4, USDA P5,
   Toxer427 CC0 P6). Web PDF measured independently: **3,674,650 B (< 10 MB),
   sha256 `acb965f6be666ad5806b3ddd3552f2f9ccc853c92ddf292f4a2f997d086a10c9`** —
   matches the §0 pin exactly (print PDF 22,574,325 B, sha `bac9302f…`, also
   matches).
10. **Banned-term scan.** 0 occurrences of the intermediary-layer term (Chinese
    form and English form) in the paper SVGs, this KIT, and the build code.

**Verdict: PASS.** No defects found; nothing fixed, nothing re-rendered — the
shipped artifacts stand as built. Cleared for repo insert by the parent
(Discord delivery remains paused per the user's 2026-10-21 instruction).
