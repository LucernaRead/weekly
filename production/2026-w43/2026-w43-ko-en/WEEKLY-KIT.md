# Lucerna 한국어판 VOL.1 — ENGLISH edition (Korean text · English explanations)

Week: Mon 2026-10-19 – Sun 2026-10-25 · Issue date on the masthead: Tue 2026-10-21
Deliverables in this folder: `svg/` (8 pages), `cards/` (8 PNGs, 1950×2700),
`Lucerna-VOL1-EN.pdf` (print), `Lucerna-VOL1-EN-web.pdf` (web, < 10 MB),
this KIT.
Build sources: `hidden_files/weekly-report-ko-en-build/` (a copy of the core
build; the core build and the core edition were never modified).

## 1. What this edition is

The second edition of the Korean VOL.1: the same issue as the finalized core
(`files/weekly-report-ko-vol1/`, Korean text + Chinese explanations), with the
explanation apparatus rewritten in **English** for English-speaking readers.
Everything else — Korean articles, exercises, images, facts, levels, page
architecture — is the core's, unchanged. Production-matrix cell: target Korean
× reader native language English.

Pairing badge (P1 masthead, bold olive, centred under the tagline):
**TEXT IN KOREAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING
READERS**. Masthead name "Lucerna" with no article (Korean convention, as the
core). Every page footer labels the pairing:
"Lucerna · KOREAN WEEKLY VOL.1 · Korean text · English explanations" and
"Page n of 8".

## 2. What changed vs the core (apparatus only)

- Every Chinese gloss (all "Note — " boxes; prefix 译注｜ → "Note — "), grammar
  note, instruction, explainer sentence, clinic rule, pattern note, readers'
  note, chart note, section glossline, dual-language title second half, band
  subtitle second half, contents gloss, and **every P8 answer note** is now
  full English. Korean wording is kept inside glosses where the Korean itself
  is the content (headwords, quoted forms).
- Registry type labels and on-page instruction labels are English
  (fill-in / multiple choice / matching / cloze / sentence building /
  transformation / true/false / translation / writing; Fill in / Rewrite /
  Build a sentence / Translate / O or X? / Write / Match the pairs /
  Match word to meaning).
- Translation exercises re-aimed at the reader's language, exactly as in the
  sibling fan-out editions — 4 items:
  - #137, #138: Korean stems kept; keys are now the English translations
    ("The typhoon's path can still change." / "There are 29 days left until
    the exam."), notes "From page 1" / "From page 2".
  - #139, #140: stems are now English sentences ("Please check the latest
    weather this weekend." / "On Friday I go to Haneul Park to see the silver
    grass."); keys are the Korean translations, notes "From page 1" /
    "From page 3".
  - #150 (writing): the registry key carries the apparatus label
    "(open task — model text below)"; the on-page task and the model text are
    unchanged Korean.
  All other 147 keys are byte-identical to the core registry.
- Two furniture micro-changes inherited from the sibling fan-out pattern: the
  P8 H-section glossline is English only; the readers'-corner honesty line is
  English only (the DE × EN sibling does the same).

## 3. Layout adjustments (measured, apparatus-driven)

- P1 masthead: the badge line was inserted; tagline, double rules and the
  dark band shifted down to make room (band contents unchanged). The band's
  right-hand English lines are unchanged core text.
- P8 key flow bottom extended 2400 → 2540 (English notes run longer); flow
  ends at y = 2470, lowest printed key baseline 2516.5 — **63.5 px clear of
  the footer rule (2580)**, measured in the rendered SVG.
- P7: the readers'-corner box grew slightly (English note); the phrases block
  starts at y = 1747.76; the VOL.2 teaser box ends ≈ 2550, above the footer.
- Four over-long single-line strings were shortened to fit their containers
  (widths measured with the production fonts): the P1 search-box source line
  ("KoreaTrendBoard (10월 21일) · Volumes approx.", 17pt), and three box
  titles ("· Numbers", "· Using D-day", "· Youth numbers").
- One inherited geometry defect found and fixed in this edition only: on P2
  the D-day strip's memorise-sentence sat with its baseline 4 px above the
  exercises rule, which grazed the glyph bottoms; the sentence moved up 6 px.
  **The core carries the identical geometry** (its audit predates the
  line-crossing check); flagged here for the parent — the core was not
  touched.

## 4. Verification (all measured on the final render)

- Baseline: the unmodified copy of the core build, rebuilt in a scratch
  directory, reproduces all 8 shipped core SVGs **byte-identically**.
- Registry: 150 exercises; levels A2 57 · B1 66 · B2 27; per page
  10/18/18/18/18/18/12/38 — identical to the core. Types: fill-in 49 ·
  multiple choice 51 · matching 16 · cloze 13 · sentence building 8 ·
  transformation 4 · true/false 4 · translation 4 · writing 1. Writing model
  162 characters (unchanged).
- Registry diff vs core: pages and levels identical for all 150 items; keys
  differ only at #137, #138, #150 (documented in §2).
- **Han characters in the rendered text: 0.** The only non-Korean, non-Latin
  glyphs anywhere are typographic (「」·—→✓ etc.), as in the core.
- Re-solve: keys are byte-identical to the core for 147/150 items (the core's
  own proofread re-derived all 150 by hand); the 4 re-aimed translation items
  and a 36-note sample across all pages were re-verified in the English layer;
  all 16 matching notes' letters agree with their keys; no note parenthesis is
  glued to the preceding word (typography standard).
- P7 phrases: all 8 printed phrases' occurrence counts across the issue are
  identical to the core (4/2/2/4/2/2/2/2), each appearing exactly once on P7
  with its page tag — the core's verbatim verification carries over, and the
  English translations under them are new apparatus.
- Facts identical to the core: Champi stays an OPEN forecast (no landfall
  asserted — KMA/JMA/JTWC divergence stated on P1); foliage two-peaks
  presented with both criteria; CSAT Nov 19, D-29, 551,864 candidates, 1,312
  sites, 13:10–13:35 flight pause; NMIXX Melon #34 → #5 (chart bars
  unchanged, 143px : 21px = 34 : 5); 해요체 throughout. Images and credit
  lines byte-identical per page (embedded payloads compared 1/1/2/1/2/1/0/0).
- Character totals (same extraction method as the core KIT): visible text
  21,363 without spaces / 26,518 with spaces (core: 15,927 / 19,645 — the
  increase is the longer English apparatus; the method reproduces the core's
  published totals exactly on the core).
- Geometric occlusion audit (SOP addendum, all four checks: paint-order
  coverage ≥30%, footer band, page edges, later-line ink-band crossing, plus
  text–text overlap): 3 initial flags — (1) P1 source line overflowing the
  page edge: REAL, fixed (§3); (2) P2 rule grazing the sentence: REAL, fixed
  (§3); (3) masthead wordmark vs edition line: **false positive** —
  crop-adjudicated at native resolution (clear air between glyphs),
  geometry identical to the shipped core, and real-font metrics
  (UnifrakturMaguntia: "Lucerna" @168 = 524 px wide) contradict the audit
  script's generic estimate. Final audit: zero unresolved flags.
- Build warnings on the final build: none (no flow overflow, no wide heads).

## 5. Kept items (adjudicated)

- The P8 "— 제8면 —" group heading lands at the foot of key column 3 with its
  items in column 4 — a flow artifact of the longer English notes; numbering
  is continuous and the header tells readers to find items by number. Same
  class the core accepted for exercise section heads.
- Dual-language lines whose second half is English combine Korean + English
  (e.g. band subtitles, section titles) — the fan-out standard (the core
  combined Korean + Chinese the same way).
- The P1 numbers box is titled "· Numbers" (shortened to fit, §3); the DE ×
  EN sibling uses the same shortening.

## 6. Files

| File | Bytes |
|---|---|
| Lucerna-VOL1-EN.pdf (print) | 33,831,694 |
| Lucerna-VOL1-EN-web.pdf | 3,048,383 |
| svg/ (8) · cards/ (8 PNG, 1950×2700) | — |

Reproduce: in `hidden_files/weekly-report-ko-en-build/`, run `run.py` then
`render.py` with the project venv (CairoSVG + Pillow + PyPDF). Fonts: Noto
Serif/Sans CJK (KR index), UnifrakturMaguntia for the wordmark — as the core.

## 7. Status

Built and self-proofread to the standard above (the fan-out gate: builder's
full pass + the checks in §4). **Not posted to Discord** — the parent posts
the web PDF to the 한국어 thread of #lucerna-weekly. The VOL.2 promises
printed in this issue are the core's and are registered in the core KIT §11.

## 8. Independent proofread record (fresh pass, independent of the builder)

Method: node-level text diff of all 8 pages against the frozen core; rendered-text
Han scan; programmatic comparison of all 150 P8 key strings and of both builds'
registries (rebuilt from source); the writing model recounted directly; all 8 P7
phrases re-located issue-wide; 40+ exercises re-solved from stems/articles; the SOP
geometric audit (production-font glyph boxes: paint-order coverage, footer band,
page edges, thin-line crossings, text–text overlap) plus native-resolution crops
of every flagged or adjudicated region; all 8 cards viewed.

**One problem found — fixed, re-rendered, and a complete re-pass run:**

1. **P8 "— 제8면 —" key-group heading orphaned (the §5 "kept" adjudication was NOT
   accepted).** In the shipped render the heading sat alone at the foot of key
   column 3 (baseline 2515.0) while its items 113–150 begin at the top of column
   4; in the core the same heading heads items 113–115 in-column, and the other
   seven headings in this edition each head their group. Numbering stayed
   continuous, but a group heading detached from its group is a reader-facing
   defect, so the gate was not passed as shipped. Fix (ko-en build only,
   `content8.py`): keep-with-next in the key flow — a group heading advances to
   the next column unless the heading plus its first key line both fit the
   current column. Re-rendered: only `p8-siheom.svg` changed (pages 1–7
   byte-identical); the heading now tops column 4's group at baseline 1341.3,
   column 3 ends cleanly at #112, and the per-column lowest key baselines are
   2516.5 / 2515.0 / 2485.8 / 2484.3 (63.5 px clear of the 2580 footer rule —
   the builder's figure, verified exactly). The §6 table was updated to the
   re-rendered PDF sizes.

**Everything else in the builder's account verified true:**

- Core integrity: every Korean article/stem/option unchanged; all node
  differences classify as apparatus, the documented #137/#138/#139/#140/#150
  items, the P1 badge, or pairing footers. Rendered Han = 0. The three shortened
  box titles confirmed as shipped; the 17 Korean instruction sentences (P2–P6)
  are all rendered as faithful English imperatives and no lowercase type-name
  label survives anywhere (the per-item labels are imperative forms throughout,
  as §2 records). 해요체 is preserved by construction (Korean content
  byte-identical to the core).
- Keys/registry: key strings differ from the core at exactly #137/#138/#150;
  registry 150 with pages 10/18/18/18/18/18/12/38, levels A2 57 · B1 66 · B2 27
  and the §3 type distribution — re-derived independently from both builds.
  Writing model recounted at exactly 162 characters; its string is byte-identical
  in both builds. All 16 matching notes agree with their keys; note parentheses
  are space-separated (the only glued parentheses are Korean-content conventions
  identical in the core: "19일(월)", "다음(Daum)", "엔믹스(NMIXX)").
- Facts: Champi stays an open forecast (the P1 article states the landfall is
  undecided; the only "landfall" string anywhere is the dictionary gloss
  "상륙하다 = to make landfall"); the foliage two-criteria dispute is intact;
  CSAT/NMIXX/foliage figures all re-checked against the article texts.
- Geometry: my own audit of the final render flags exactly one item — the P1
  wordmark/edition-line box overlap (0.24) — crop-adjudicated at native
  resolution: clear air between the blackletter ink and the edition line; false
  positive, same as the core. The builder's two fixes re-adjudicated in the final
  render: the P1 search-box source line ends at x≈1850 inside the frame, and the
  P2 D-day sentence clears the rule below it (glyph bottom 1800.2 vs rule 1804;
  no crossing). P7's readers'-corner/phrases boundary and teaser box (ends
  y≈2550, above the footer band) are clean. Image payloads and credit lines are
  byte-identical to the core on every page (counts 1/1/2/1/2/1/0/0). Pairing
  badge legible on P1; pairing footers on all 8 pages.

**Verdict: this independent pass, run in full on the final (post-fix) render,
finds ZERO problems. The KO × EN edition is FINAL.** (Not posted — posting is
the parent agent's step. Note for the parent: the P2 D-day rule graze recorded
in §3 exists in the frozen core as well, per the builder's flag; the core was
not touched in this proofread.)
