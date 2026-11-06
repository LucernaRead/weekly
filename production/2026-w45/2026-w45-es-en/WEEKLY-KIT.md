# La Lucerna · Spanish Weekly VOL.2 — English-explanations edition (ES × EN) WEEKLY-KIT

> This file is the VOL.2 Spanish core's **English-native-reader edition**: the same
> core (Spanish text frozen), with the explanation layer entirely in English.
> The core first-pairing edition is the Chinese-explanations core
> (`files/weekly-report-w45-es-core/`). Parent SOP: `files/weekly-report-SOP.md`.

## 0. Edition identity

- **Pairing: target language = Spanish · reader native language = English**
  (one-to-one, no intermediary language).
- **Masthead badge (P1, subtitle slot y=372, 19.5pt BRICK)** — ES-core family
  precedent (EN/DE/ES cores carry a native subtitle slot; the badge replaces it
  in place, README #20):
  `TEXT IN SPANISH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`
- **Footer (all 8 pages)**: `La Lucerna · Spanish Weekly VOL.2 · Text in Spanish · Explanations in English` / `Page n of 8`.
- **Gloss prefix**: `Note | ` (P1 bridge: `Notes | `). **P8 separator**: `— PÁGINA n —`
  (Spanish, frozen from the core).
- Issue and week identical to the core: VOL.2 · Monday 2 – Sunday 8 November 2026;
  themes unchanged: the 29-N election countdown with housing as the deciding issue,
  the Monday 2 puente in nine communities, the European week, Sunday 8 November
  with the NFL at the Bernabéu (15:30) and Atlético–Barça (21:00).

## 1. What changed vs the core (explanation layer only)

- All explanations in English: Notes vocabulary glosses, section-title English
  glosses (e.g. `LA NOTICIA · Top story`, `VIDA · Life`, `CULTURA · Culture`,
  `DEPORTE · Sport`, `JUVENTUD · Youth`, `A FONDO · In depth`,
  `LENGUA · Language focus`), exercise bridges, exercise-type names
  (`Sentence completion`, `Multiple choice`, `True or false`,
  `Sentence building`, `Sentence transformation`, `Vocabulary matching`,
  `Translation`, `Cloze choice`, `Writing`), instruction labels
  (`Fill in`, `True or false`, `Build the sentence`, `Rewrite`, `Translate`,
  `Write`, `Match word to definition`), chart-reading notes, error-clinic notes,
  readers'-letters disclosure, next-issue preview gloss, and **all 150 P8 answer
  notes**.
- Furniture strings copied verbatim from the shipped W43 ES×EN edition
  (`files/weekly-report-es-en/` SVG + KIT §0), with VOL.1→VOL.2 only. The EN×DE
  English-form footer is a different edition's exception and was NOT used here.
- **Ruling 1 (P8 section E translation items, W43 ES×EN KIT ruling 1 applied)**:
  the core's E section is Spanish↔Chinese; this edition re-aims it Spanish↔English.
  Item 137 key: `Monday is a public holiday in nine communities.`
  Item 138 key: `On Sunday we watch the NFL and Atlético–Barça.`
  Items 139/140 prompts become English source sentences
  (`The Bernabéu hosts an NFL game.` / `Every chart must show its source.`),
  keys stay Spanish. All other 147 answer keys are byte-identical to the core
  (verified over all 150 rendered answer lines; see §4).
- **Ruling 2 (P7 example letter punctuation, W43 ES×EN KIT ruling 2 applied)**:
  the full-width parens around the letter's attribution change to ASCII parens
  (`(ejemplo, escrito por la redacción)`); letter body, name Ana and place
  Shanghái are frozen Spanish text. No new readers or letters invented: the
  letter remains the labelled editors' example, and the FIX1 disclosure
  (Spanish frozen; English note translated) still states that no real letters
  or best page-8 texts had arrived and the promise carries to VOL.3.
- Images, captions, credits and signatures are byte-identical to the core
  (same asset files, same hrefs and coordinates — the build copy's `assets/`
  and `svglib.py`, including `illus_houses()`, are untouched).

## 2. Scale (same counting method as the core: all text elements of the 8 SVGs)

- **Exercises: 150**, isomorphic to the core: pages 10 / 18 / 18 / 18 / 18 / 18 /
  12 / 38; levels A2 50 · B1 72 · B2 28.
- Registry types: Sentence completion 48 · Multiple choice 47 · Cloze choice 13 ·
  Vocabulary matching 12 · Sentence transformation 10 · True or false 8 ·
  Sentence building 7 · Translation 4 · Writing 1.
- Build warnings: **0 FLOW OVERFLOW / 0 HEAD TOO WIDE** (final build).
- 8 pages, 1950×2700; 8 full-page PNGs at 1950×2700.

## 3. Layout changes (only in this edition's build copy, core build untouched)

1. P6 exercises 19pt/gap 3 → **18.5pt/gap 2** (W43 ES×EN §3.1 precedent): the
   longer English notes overflowed the P6 exercise flow at 19pt.
2. P8 answer lines 13.5pt/1.16 → **13.2pt/1.12**, section separators 1.16 → 1.12
   (W43 ES×EN §8.1 precedent): English notes overflowed the 2552 answer bottom
   at 13.5pt. Answer-generation code otherwise byte-identical — dash style
   `N. key — note` and the `N. ✓ note` writing form are unchanged; the only
   code-token change is the type check `== "写作"` → `== "Writing"`, paired
   with the type-name translation (same as W43 ES×EN).
3. P1 five-keys note shortened to the W43 verbatim `Five keys — no invented
   numbers.` (the longer English line ran past the page edge, ink to x=2002).
4. P1 word-of-week note shortened to `The pre-campaign: weeks before the
   campaign.` (single line; the two-line version crossed the y=1844 rule).
5. P5 plan-box title shortened to `EL PLAN DEL PUENTE · The plan` (the longer
   title crossed its box border, ink to x=1082.8 vs border 961).
6. P7 errors-box title shortened to `ERRORES TÍPICOS · Mistakes` (the longer
   title crossed its box border, ink to x=1919.2 vs border 1885).
7. P7 column-3 notes trimmed to restore the core's preview geometry exactly
   (preview title baseline 2484.08, identical to the core): error notes
   (`gente is singular, like one group.` / `creo que states a fact: indicative.`),
   word note (`precampaña = the pre-campaign, the weeks before the campaign.
   The campaign starts Friday the 13th.`), disclosure note (drops only the
   trailing `Write in!`; all three disclosure facts kept). Without these trims
   the preview block sat on the footer rule (title baseline 2595.12).

## 4. Verification (all machine checks, builder-run; independent proofread pending)

- **Baseline**: `tools/freeze.py baseline` on the build copy before editing:
  **8/8 SVGs byte-identical** to the shipped core SVGs; core SVGs re-hashed
  afterwards, unchanged. Core hashes after the final build still match the
  baseline exactly (p1 `a1b30102…`, p2 `10e78c2e…`, p3 `5986ba9e…`,
  p4 `1894836e…`, p5 `cd15c68b…`, p6 `fcfccf82…`, p7 `b1774024…`,
  p8 `d1c46fa4…` — full hashes in the build log).
- **Frozen-text diff** (`tools/freeze.py diff`, core vs edition): added CJK = 0
  on all 8 pages; edition CJK = 0. Source-level diff of the two build trees
  shows every changed line is explanation-layer, furniture, OUT repointing, or
  the §3 layout parameters; the only Spanish-body line touched is the P7
  letter attribution (2 parenthesis characters, §1 ruling 2) plus the P1
  headline-note slot (a Spanish note translated to English, documented in §1).
  Remaining SVG string differences are explanation text or re-wrapping of
  frozen Spanish lines caused by longer English neighbours (verified line by
  line for the non-CJK removed strings).
- **P8** (`tools/p8.py compare`): **CLEAN, 150 = 150**, missing = [], extra = 0.
  Keydiff list [17, 18, 19, 20, 60, 61, 62, 63, 64, 72, 83, 85, 95, 96, 98, 107,
  117, 137, 138, 148]: 18 are note-only changes with byte-identical keys;
  137/138 are the §1 ruling-1 redirections; 150 (✓ form) renders
  `150. ✓ Model text in section H on this page (84 words)`. Full 150-key
  comparison over rendered answer lines: only 137, 138, 150 differ.
- **Occlusion** (`tools/occlusion_audit.py`, selftest passed): first run
  7 flags, all real defects from longer English text, all fixed (§3.3–3.7)
  and crop-verified on the rendered cards; final run **0 flags**.
- **Same-baseline ink scan** (FR×RU `rowcheck.py` method): 7 reports, all the
  P1 contents list (`Pág. n` + title, 4.0px gaps, no overlap) — byte-identical
  to the core's own scan (same 7, same gaps); no new same-row collision.
  Furniture bands (P1 top band, masthead, footer) show no flags in either.
- **Chart-page element check** (P6, README #12 graze class): text ink vs
  later-drawn rects = **0 overlaps**; bar labels, bars and values all clear
  on the rendered card.
  - COORDINATOR ADJUDICATION 2026-10-27 (frozen-core known defect, non-blocking):
    independent proof found 1 graze the builder's check missed — P6 second chart
    label `Inmigración` (x=1011, y=1717, 21pt bold) ink right edge 1144.2 vs
    following bar rect left edge 1139 (5.2px overlap; final `n` tail half-covered
    on the card, word unambiguous in context). Geometry verified pixel-identical
    to the already-shipped ES core (same text/rect indices, coordinates, fill;
    core card crop same sha256). Canonical occlusion audit = 0 flags; fixing
    would require re-shipping the core + rebuilding all ES fan-outs, which is
    disproportionate for a 5px tail graze. ACCEPTED as a registered known defect:
    this edition is finalized WITH this graze, and future ES fan-out proofs must
    NOT re-flag this same frozen geometry (report presence only, to confirm
    identity).
- **Gloss counts** (split on `·` itself, README #21): P2 5 = 5, P3 5 = 5,
  P4 5 = 5, P5 4 = 4 vs the core, item by item; every headword present in the
  rendered SVG text.
- **No CJK in the edition**: 0 CJK characters in all 8 delivered SVGs; the
  build copy's remaining CJK is two non-rendered source comments only.

## 5. Reproduction

- Build copy (core build copied, never edited in place):
  `hidden_files/weekly-report-w45-es-en-build/`
- Transform record (literal replacements with asserted counts):
  `hidden_files/w45-es-en-transform.py` (+ §3 fix-ups logged in the build dir)
- Single-process full build (never run content modules standalone — the
  shared exercise registry requires one process):
  `cd hidden_files/weekly-report-w45-es-en-build && ../../tools/venv/bin/python run.py`
- Render PNG + PDFs:
  `../../tools/venv/bin/python render.py` (render.py points at the new edition
  dir and the `VOL2-EN` PDF names)
- Geometry audit records: `hidden_files/w45-es-en-occlusion.json` (first run,
  7 flags) → `hidden_files/w45-es-en-occlusion2.json` (final, 0 flags);
  diff: `hidden_files/w45-es-en-diff.json`; crops:
  `hidden_files/w45-es-en-crops/`.

## 6. Deliverables (files/weekly-report-w45-es-en/)

- `svg/` 8 pages · `cards/` 8 PNGs (1950×2700)
- `La-Lucerna-VOL2-EN.pdf` (print) · `La-Lucerna-VOL2-EN-web.pdf` (web)
- This KIT · `ABSTRACT.txt`

Not delivered to Discord, not posted to the main chat, not pushed to any repo
— delivery is the parent line's job; this edition awaits independent proofread.
