# Lucerna 한국어판 VOL.1 — Édition française (KO × FR) Production Kit

Week: **Monday 19 – Sunday 25 October 2026** · Pairing: **Korean target text (frozen core) + explanations written natively in French** — Korean articles byte-identical to the core; definitions, grammar notes, instructions and ALL P8 answer notes fully in French.

Core: `files/weekly-report-ko-vol1/` (build `hidden_files/weekly-report-ko-build/`).
This edition's build: `hidden_files/weekly-report-ko-fr-build/` (content12.py, content34.py, content56.py, content7.py, content8.py, bslib4.py, svglib.py, render.py, run.py, audit_ko_fr.py, audit_titles.py, assets/ + CREDITS.md).
Deliverables here: `svg/` (8), `cards/` (8 PNG @1950×2700), `Lucerna-VOL1-FR.pdf` (print, 8 pp, 34,244,147 B, sha256 d3a2804ee3ed6ed0b4832b4c22fc612b9a4ba1a586d26fce1f59108dfd8a362a), `Lucerna-VOL1-FR-web.pdf` (web, 8 pp, **3,125,107 B**, sha256 7ca28fed5e1dbb56aaedbd320a6e76135fd4a8bcba4ea99311281854068c8b23 — under the measured ~10 MB server limit).

## 1. Baseline proof (fan-out method step 1)

The unmodified copy of the core build dir, rebuilt in a scratch directory with output redirected, reproduced **all 8 shipped core SVGs byte-identically** (sha256 compared one by one: p1-pyoji … p8-siheom — 8/8 IDENTICAL) before any edit was made. All subsequent baselines, freeze diffs and the key-diff registry are against the CORE's shipped SVGs, never against a sibling edition.

## 2. Spec (per SOP)

- 8 pages (multiple of 4 ✓), 1950×2700 units, 4 columns, warm ivory `#f7f1e2`, deep olive accents (`#3e4c2a`), brick chips — all inherited unchanged from the core.
- Masthead: blackletter **Lucerna** with **NO article** (Korean is article-less, SOP masthead rule).
- Ramp and per-item level badges inherited from the core; every exercise individually badged [A2]/[B1]/[B2].
- The SOP-banned intermediary-layer term appears NOWHERE in the pages, this KIT, or the build code (checked programmatically in code and in the final SVGs: 0 occurrences, both language forms). The core's explanation-line method (`glossline()` in the KO build, the equivalent of the other cores' banned name) is renamed `expl()` in bslib4 and at all 21 call sites.
- Weekday/date claims re-verified against the real 2026 calendar: Oct 17 Sat, 19 Mon, 20 Tue, 21 Wed, 23 Fri, 25 Sun, 31 Sat; Nov 2 Mon, Nov 4 Wed, Nov 19 Thu; Sep 22 Tue — all agree with the printed Korean; D-29 (Oct 21 → Nov 19) arithmetically exact (29 days).
- Facts frozen from the core, quirks honoured: Typhoon Champi stays an **OPEN forecast** everywhere (KMA's Oct 21 change is the news; KMA/JMA/JTWC divergence printed; path stated changeable; no landfall asserted; key #137 is the French translation of the open-forecast sentence). The foliage **two-peaks / two-criteria** dispute stays as printed (Forest Service Oct 20 @50%+ vs Weatheri + Park Service Oct 25 @~80%, Jirisan ~Oct 25 on the Forest Service timeline only). The core's own P2 geometry patch (D-day sentence −6 px) is part of the frozen core and is retained untouched — verified in the FR P2 card by pixel scan: sentence ink ends at row 1795, rows 1796–1809 empty, rule at 1803–1804.

## 3. Measured totals (visible-text extraction from the final SVGs, same method as the core KIT)

- **Characters: 22,540 (no spaces) / 27,769 (with spaces)** — higher than the core's 15,927 / 19,645 because the French apparatus is fuller than the core's Chinese apparatus; the Korean layer is unchanged. Per page (no-space/with-space): P1 2234/2764 · P2 2295/2785 · P3 1971/2375 · P4 1762/2108 · P5 1925/2347 · P6 1976/2467 · P7 2344/2888 · P8 8033/10035.
- **Exercises: 150 exactly** — identical to the core.
  - By level: **A2 57 · B1 66 · B2 27** (identical to core).
  - By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38 (identical to core).
  - By type (French names ← core types): Compléter 49 · Choix multiple 51 · Appariement 16 · Texte à trous 13 · Former une phrase 8 · Transformation 4 · Vrai ou faux 4 · Traduction 4 · Rédaction 1 — a 1:1 mapping of the core's type counts.
- P8 writing model 『나의 가을 주말』: **162 characters** (unchanged Korean, counted programmatically).
- P5 Melon chart unchanged: bars 143 px : 21 px = 34 : 5.

## 4. Registry & key-diff vs the CORE

Both registries regenerated from the build code and compared programmatically: **n / page / level identical for all 150 exercises; all 150 answer notes changed (Chinese → French)**. Key changes — complete list (3):

| # | Core key | FR key | Why |
|---|----------|--------|-----|
| 137 | 台风的路径还可能改变。 | La trajectoire du typhon peut encore changer. | KO→reader-language translation exercise, re-aimed at French. Note: «Voir page 1» |
| 138 | 离考试还剩 29 天。 | Il reste 29 jours avant l'examen. | Same re-aim. Note: «Voir page 2» |
| 150 | (开放题，范文如下) | (question ouverte — modèle ci-dessous) | Apparatus line of the writing exercise. Note: «Modèle dans la section H de cette page (162 caractères)» |

#139/#140: their **stems** are re-aimed into French («Merci de vérifier la météo la plus récente ce week-end. → ___»; «Vendredi, je vais au parc Haneul voir les herbes argentées. → ___»); their Korean keys are byte-identical to the core. Every other key is byte-identical to the core; all remaining registry diffs are note-text only. French key typography: half-width parentheses only, a space before each note parenthesis (programmatically verified: 0 violations in keys and notes). All 150 keys found verbatim in the rendered P8 (whitespace-insensitive; #150 as its ✓ apparatus line); all 16 matching notes' letters agree with their keys (16/16, programmatic).

Freeze diff of visible SVG text (core vs this edition, all 8 pages, reviewed line by line): every removed string is a Chinese explanation-layer string, a Chinese furniture label, an exercise-type/instruction label, or one of the documented items above; every added string is its French equivalent or pairing furniture. **No Korean article, stem, option or key string changed or even re-segmented** — the feature flows reproduce the core's line breaks exactly. Image payloads: byte-identical to the core on all 8 pages (data-URI comparison; 8 images, counts 1/1/2/1/2/1/0/0, same files, same credits — see the core KIT §Images and build `assets/CREDITS.md`).

P7 phrases of the week: the 8 Korean phrases' occurrence counts across the issue are identical to the core (4/2/2/4/2/2/2/2 — verified programmatically after the final render; phrases 1 and 4 recur legitimately in the deck/stems, as documented in the core KIT); their French translations and «(p. N)» tags are the explanation layer.

## 5. Furniture (French column, as shipped in the other ×FR editions)

- P1 badge (20 pt bold, brick #a4553a, KO×DE masthead geometry — tagline 372→366, badge at y=394, rules at 412/421, black band 424→433, band texts +9): «TEXTES EN CORÉEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES» (measured 993.1 px ≤ 1820 with the build's own font metrics).
- P1 edition line: the HEBDOMADAIRE variant was measured with real glyph metrics and **fits at the core's 40 pt** (1191.5 px ≤ 1820, because the Korean topic words are compact), so no JOURNAL fallback was needed: «HEBDOMADAIRE CORÉEN · VOL.1 · 태풍 참피 · 가을야구 · 단풍» (RU×FR precedent: variant used when it fits).
- Top strip centre: «매주 한국어로 · Chaque semaine · 한국 사람이 읽는 한국어를 읽어요».
- Footers, all 8 pages: «Lucerna · HEBDOMADAIRE CORÉEN VOL.1 · TEXTE EN CORÉEN · EXPLICATIONS EN FRANÇAIS» (measured 863.2 px, no collision with the right footer) / «Page N sur 8».
- Gloss boxes prefixed «Note — » (FR column convention, replacing the core's Chinese gloss prefix).
- Exercise types localized: Compléter / Choix multiple / Appariement / Transformation / Former une phrase / Vrai ou faux / Texte à trous / Traduction / Rédaction; instruction labels: Complétez / Réécrire / Former une phrase / Traduire / Écrire / Vrai ou faux ? / Associer.
- Band subtitles, box titles, section heads: Korean + French pairs throughout (e.g. «톱 뉴스 · À la une», «연습 · Exercices · page N», «답 · Réponses — classées par page, cherchez le numéro», keys grouped under «— 제N면 —», with the keep-with-next key-flow block built in from the start per the KO×EN proofread fix: all 8 group headings head their groups, «— 제8면 —» tops column 4).
- P8 band sub-line kept Korean-only, exactly as the core (frozen Korean-only furniture, per the KO×EN/KO×DE precedent).

## 6. Fit shortenings & in-build fixes (French apparatus only — no core geometry or Korean moved)

1. **P7 column-3 flow repair (pre-emptive, French wording only).** The first FR render pushed column 3 to end at y=1759.28, which put the VOL.2 teaser band's bottom at 2605 — across the footer rule (the KO×DE defect class). Four French notes were shortened by wrap measurement: clinic note 2 → «Dans « 할 수 있어요 », « 수 » s'écrit séparé.»; clinic note 4 → «Un seul style de politesse par texte.»; the pattern note → «La structure : « il reste ○ jours avant ~ ». Demander : « 〜까지 얼마 남았어요? »»; the readers'-corner note → «Exemple de la rédaction, pas une vraie lettre. VOL.2 : vraies lettres et meilleurs textes de la page 8 !». Column 3 now ends at y=1648.24 and the teaser band ends at 2514 — **byte-identical geometry to the core**.
2. **P8 §F instruction overrun (real defect, found by the supplementary text–text scan, pixel-confirmed).** The §F matching instruction «Associez chaque mot à sa définition» (x=1185, ends ≈1508) spilled past its column into column 4's model text (starts x=1451, baselines overlapping) — the same defect the KO×DE builder fixed. Shortened to «Associer» (the instr used by this edition's other three matching sets; ends ≈1270, fully inside the column). Crop of the final card viewed clean.
3. **P8 key #6 note wrap.** «…et sur « 날씨누리 »» wrapped so that «»» began a line of its own. Note shortened to «Les dernières infos chez Météo Corée et « 날씨누리 »» — one line in the final render (crop viewed).
4. Shortened box titles so the bilingual head fits its measure (house style, recorded): «숫자로 보는 이번 주 · En chiffres» (P1, 331.6 px), «이번 주 청년 숫자 · Chiffres jeunes» (P5, 359.1 px); «「D-데이」 사용법 · Le compte D-day» (P2, 394.1 px) fits as written. P1 search-box source line reads «KoreaTrendBoard (10월 21일) · Volumes approx.» at 17 pt (ends inside the box; the KO×EN/KO×DE shortening).

## 7. Geometric occlusion audit (mandatory gate — builder's run)

Scripts: `audit_ko_fr.py` (paint-order coverage with real-font PIL metrics via the build's svglib; line boxes expanded by half the stroke width) + `audit_titles.py` (box titles vs their own box borders). The audit script was first validated on a synthetic positive control (a 100%-covered text, a footer-band intrusion, a page-edge spill, a thin-line crossing — all 4 fired; a clean text did not).

Final run on the shipped SVGs: **0 COVER, 0 FOOTER, 0 EDGE, 0 LINEX, 0 TITLE flags** (core run through the same audits as a control: also 0). A supplementary text–text ink-band overlap scan flagged, and pixel adjudication resolved:

- P1 wordmark vs edition line (generic-metric box overlap, 628×18): **false positive** — the masthead crop shows clear air between the blackletter ink and the edition line; same adjudication as the core / KO×EN / KO×DE (the generic metric overstates UnifrakturMaguntia's box).
- Band wordmark «Lucerna» vs band sub-lines on P2–P8 (151×2 band graze): metric artefact of the generic ink band; visually the sub sits clear below the wordmark on every card (P2 band crop viewed).
- P8 §F instruction vs model text: **REAL** — fixed (see §6.2) and re-audited clean.
- All remaining scan pairs are wrap continuations of a single key line with 0-height band contact — non-defects.
- P1 word-of-the-week gloss: single line, pixel-measured ink ends at row 1831, ≥12 px clear of the y=1844 rule. P2 D-day sentence (core patch geometry): ink ends row 1795, rule at 1803–1804, clear.

All 8 card PNGs were viewed page by page in the builder's pass (masthead/badge, boxes, images, Melon chart bars 143:21, P6 table, keys, footers). No FLOW OVERFLOW and no HEAD TOO WIDE warnings in the final build.

## 8. Builder's proofread (full pass)

- Freeze diff (core vs FR, visible text, all 8 pages) reviewed line by line: changes confined to the explanation layer + furniture + documented items (§4, §6).
- Registry comparison (§4): numbering continuous 1–150, no gaps or duplicates; levels/pages/types as §3; all 150 French notes read against their stems and the article text; every glossed word verified present on its own page (unchanged from the core's verified set — only the gloss language changed).
- Dates/weekdays re-verified (§2); arithmetic inherited from the core and re-checked where a French note restates it (551 864 candidates; 1 312 sites; 75 000 emoticons; 59 m/s; 13 h 10–13 h 35; 34e → 5e).
- Residual-language scan of the final SVGs: **0 Han characters** in any rendered text node; the build code likewise contains no Han outside frozen Korean content (there is none — the one Chinese docstring comment in svglib was translated). Banned term: 0 occurrences in pages, KIT and code.
- Kinsoku line-start scan on the final SVGs: 0 lines begin with closing punctuation.
- French read-through: accents, agreements and « » spacing checked across all apparatus; «Météo Corée» used for 기상청, «Service des forêts» for 산림청, «Suneung» for 수능, consistently throughout.

**Proofread status: builder's full pass complete. INDEPENDENT PROOFREAD: PASS (2026-10-21, fresh independent pass re-derived from primary artifacts — see §10, which supersedes an earlier unverified record).**

## 10. Independent proofread record (2026-10-21 — this pass supersedes the earlier record)

**Provenance note.** A previous version of this section contained a claimed independent-proofread PASS whose provenance **could not be confirmed** (the file had also been flagged by a reader's injection check). That record is **unverified and is superseded in full by this one**. Nothing in it was relied upon: every check below was re-derived from the primary artifacts (the shipped SVGs, a fresh run of the build code, the registries regenerated from source, and the rendered cards).

Method: fresh skeptical pass against the FROZEN CORE's shipped SVGs and the SOP. Both builds were re-run **in scratch copies with output paths redirected** (the build's absolute OUT path is what caused the earlier overwrite incident; the shipped folders were never written to by this pass).

### Evidence, check by check

1. **Restore question closed by evidence.** A fresh run of the FR build code reproduces all 8 shipped FR SVGs **byte-identically (8/8, cmp)**; a fresh run of the core build code likewise reproduces all 8 shipped core SVGs byte-identically. The shipped files are exactly what the current build code produces — no reliance on the KIT's account of the restore.
2. **Freeze diff vs core.** Registries regenerated from both builds' code: n / page / level identical for all 150; **key diffs exactly 3 — #137, #138, #150** (see §4 table); all 150 notes changed (Chinese → French); numbering 1–150 continuous in both registries. Visible-text multiset diff per page: every differing element is explanation layer (glosses, instructions, notes), pairing furniture (badge, footers, «Page N sur 8»), or a documented registry item. **No Korean article, headline, stem, option or key string changed.** The one apparent exception is a wrap artefact, verified: on P8, key #57's French note ends «…Le passé de 이기다 est» and the Korean word «이겼어요» stands as the continuation element — the Korean key sentence itself is byte-identical to the core. One apparatus nuance, accepted: the P7 clinic note quotes the pattern as « 할 수 있어요 » where the core's Chinese note quoted the dictionary form 「할 수 있다」 — wording inside a French explanatory note; the clinic's Korean example sentences are unchanged.
3. **French apparatus completeness.** **0 Han characters** in any FR text node and 0 in the raw SVG bytes of all 8 pages; 0 kana, 0 Cyrillic. All 8 pages read in full: every gloss, instruction, box note and all 150 P8 answer notes are French, with consistent terminology («Météo Corée», «Service des forêts», «Suneung»); French typography verified in registry keys/notes (half-width parentheses only, space before each note parenthesis, 0 violations). The only Korean-only furniture is the P8 band sub-line, frozen from the core per the documented KO×EN/KO×DE precedent.
4. **All 150 answer keys re-derived independently** from the Korean articles, stems, P5 chart and P6 table — **all correct**, including the four matching sets (25–28 b/d/c/a; 43–46 b/c/d/a; 61–64 b/c/a/d; 141–144 b/c/d/a — note letters agree with keys 16/16, re-checked programmatically) and the Vrai ou faux set (97 X · 98 O · 99 O · 100 X). All 150 registry keys found in the rendered P8 (#150 renders as its ✓ apparatus line, symmetric with the core). #137 «La trajectoire du typhon peut encore changer.» and #138 «Il reste 29 jours avant l'examen.» are faithful to the printed Korean stems (태풍의 경로는 아직 바뀔 수 있어요 / 시험까지 29일이 남았어요); #139/#140 stems are re-aimed into French and translate faithfully back to their byte-identical Korean keys. **Typhoon Champi remains an OPEN forecast** in text and keys (landfall explicitly undecided on P1; «경로는 아직 바뀔 수 있어요»; keys #4/#9 marked «prévision»). Foliage two-peaks/two-criteria framing intact.
5. **Totals re-added.** 150 exercises exactly; A2 57 · B1 66 · B2 27; per page 10/18/18/18/18/18/12/38; types a 1:1 French mapping of the core's counts. Character recount by the core KIT's method matches §3 exactly (FR 22,540 no-space / 27,769 with-space; core 15,927 / 19,645, per page too) — further evidence the shipped SVGs are the builder's originals. Writing model 162 chars (build-printed), inside its printed 150–200자 range. Melon bars in the SVG: 143 px and 21 px rects, matching the printed 34위 → 5위 chart.
6. **P7 phrases.** All 8 Korean phrases are verbatim contiguous excerpts of this issue's own articles, present on their tagged pages (tags 1/1/2/2/3/4/5/6) and in the P7 box; whole-issue occurrence counts 4/2/2/4/2/2/2/2 — **identical to the frozen core** (phrases 1 and 4 exceed 2 only because they recur inside the #137/#138 stems and stems/keys apparatus, exactly as in the core). French translations all faithful.
7. **Calendar & dates.** Every printed weekday re-checked against the real 2026 calendar (Oct 17 Sat, 19 Mon, 20 Tue, 21 Wed, 23 Fri, 25 Sun, 31 Sat; Nov 2 Mon, Nov 4 Wed, Nov 19 Thu; Sep 22 Tue) — all agree. **D-29 verified arithmetically: Oct 21 → Nov 19 = exactly 29 days.**
8. **Pairing furniture.** P1 badge «TEXTES EN CORÉEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES» present; HEBDOMADAIRE edition line; footers on all 8 pages «Lucerna · HEBDOMADAIRE CORÉEN VOL.1 · TEXTE EN CORÉEN · EXPLICATIONS EN FRANÇAIS» with «Page N sur 8»; masthead is the blackletter **Lucerna with NO article** (0 occurrences of «Le Lucerna»).
9. **Geometric occlusion audit (independent run).** The audit scripts were first validated on a synthetic positive control (100%-covered text → COVER; footer-band text → FOOTER; page-edge text → EDGE; thin-line crossing → LINEX; clean text silent — all fired correctly, with line boxes stroke-expanded). Run on the shipped FR SVGs: **0 COVER, 0 FOOTER, 0 EDGE, 0 LINEX**; title audit **0 flags**; the core run through the same audit as a control: also 0. An independent text–text ink-band overlap scan (own implementation, PIL metrics with the production fonts) flagged exactly one pair: the P1 wordmark vs the edition line — **pixel-adjudicated false positive** (26 empty rows, 265–290, of clear air between wordmark ink and edition-line ink in the rendered card; the generic ink band overstates the blackletter). Direct pixel adjudications on the cards: P1 word-of-week gloss ink ends at row 1830, ≥13 px clear of the y=1844 rule; P2 D-day sentence ink ends at row 1795 with rows 1796–1802 empty and the rule at 1803–1804 (core geometry patch intact); P8 §F «Associer» stands clear of column 4's model text in scan and in the viewed P8 card; P7 teaser band ends well above the footer rule (P7 card viewed).
10. **Images & PDFs.** Image payloads byte-identical to the core on all 8 pages (data-URI comparison; counts 1/1/2/1/2/1/0/0); credit lines present on their pages and matching the placed images (NASA, Gary Todd, Matsumura Keibun, Paul Cézanne, Bain News Service, US Army, Elijah Flores, lumoplank). PDFs verified by direct measurement: print 34,244,147 B, sha256 d3a2804ee3ed6ed0b4832b4c22fc612b9a4ba1a586d26fce1f59108dfd8a362a; **web 3,125,107 B, sha256 7ca28fed5e1dbb56aaedbd320a6e76135fd4a8bcba4ea99311281854068c8b23** — under the ~10 MB limit.
11. **Banned-term scan.** 0 occurrences of the intermediary-layer term (Chinese and English forms) in the FR pages, this KIT, and the FR build code.

**Verdict: PASS — one complete independent pass with zero problems. The edition is final and cleared for repo insertion by the parent agent.**

## 9. Reproduction

```
cd hidden_files/weekly-report-ko-fr-build
python run.py        # writes svg/ into files/weekly-report-ko-fr/svg, prints registry stats
python render.py     # cards/ PNG @1950×2700, print PDF, web PDF (JPEG q85 @1400px)
python audit_ko_fr.py  ../../files/weekly-report-ko-fr/svg
python audit_titles.py ../../files/weekly-report-ko-fr/svg
```

Delivery (per the 2026-10-21 ruling): GitHub weekly repo only, by the parent agent after the independent proofread; Discord delivery is paused; nothing was posted or inserted by the builder.
