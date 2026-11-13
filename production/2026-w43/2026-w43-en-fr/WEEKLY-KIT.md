# WEEKLY KIT — The Lucerna · ENGLISH WEEKLY VOL.1 · EN × FR edition

**Pairing:** English text + French explanations, for French-speaking readers.
**Badge (P1, brick red #a4553a, in place of the core tagline):** TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES
**Masthead:** The Lucerna (unchanged). P1 title line: HEBDOMADAIRE EN ANGLAIS · VOL.1 · SPORT · ÉLECTIONS · CITROUILLES.
**Footers (all 8 pages):** left “The Lucerna · HEBDOMADAIRE ANGLAIS VOL.1 · TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS”, right “Page N sur 8”.
**Week:** Mon 2026-10-19 → Sun 2026-10-25 (W43) · VOL.1 · 8 pages (1950×2700) · **149 exercises** (A2 58 · B1 72 · B2 19; per page 10/17/18/18/18/18/12/38 — identical to the core).

## Deliverables (this directory)
- `svg/` — 8 page SVGs (p1-front … p8-exercices)
- `cards/` — 8 PNG cards, 1950 px wide (p1-front, p2-life, p3-culture, p4-sport, p5-youth, p6-midterms, p7-language, p8-test-answers)
- `The-LUCERNA-English-Weekly-VOL1-FR-print.pdf` — 8,623,199 bytes · sha256 a6f003c1abf6d18b71b962869f51f413d3df507c898ee246c161a04e89da01f6
- `The-LUCERNA-English-Weekly-VOL1-FR-web.pdf` — **4,421,142 bytes (< 10 MB)** · sha256 65a52868566f289cddf42013e6fd82f71e0c22280aa60c52ef92522880a6fdd9
- D5 rebuild (2026-11-13, see D5 rebuild section below): print `The-Lucerna-VOL1-en-fr.pdf` **7,502,963 bytes** · sha256 `44b551420d6b91b17f5e19b16986e3f1a1ed65758b9c8f71f39c0d7e987351b7`; web `2026-w43-en-fr.web.pdf` **1,072,352 bytes** · sha256 `cb02ed902f319f610fdf1e206cc48a5501940ce55cb51f9985c3534e24a70275` (< 7 MB); text.md byte-identical to the shipped version (sha256 `2b25e2aa…`). Pre-D5 values: print 8,623,199 B, web 1,113,337 B (`b2dfb4f5…`, shipped in issues/). (The KIT pins above are the D1-era pre-D5 values, already expired before this rebuild.)
- Build code: `hidden_files/weekly-report-en-fr-build/` (copy of the frozen core build; core dirs never edited)

## Method (fan-out, same as the EN×DE sibling)
1. Copied the finalized, P1-patched core build; rebuilt it unmodified first — all 8 SVGs byte-identical to the shipped core, registry identical (149).
2. Rewrote ONLY the explanation layer into full French: every gloss, grammar point, instruction, section-head French half, chart note, clinic note, readers'-corner reply, teaser, and all P8 answer notes. No third language anywhere; explanations are written directly in French (the layout library's instruction-line method was renamed so the banned intermediary term appears nowhere in this edition's paper, kit, or code — 0 occurrences, grep-verified).
3. House bilingual heads kept (English half frozen + French half); over-wide French halves shortened (recorded below). Gloss prefix: “Note | ”. French typography: ’ apostrophes, decimal commas, space before %, guillemets « ».

## Freeze record (verified programmatically)
- Registry diff vs core: n / page / level / body identical for all 149.
- **Key diffs: exactly 3 — #136, #139, #149** (the documented reader-language items):
  - #136 (EN→FR): key → “Le vote n’est plus l’affaire d’une journée ; c’est une saison.”
  - #139 (EN→FR): key → “Aucun des deux clubs n’a jamais gagné les World Series.”
  - #137 / #138 (FR→EN): prompts became French (“Traduisez : Les 76ers ont gagné le match 106 à 100.” / “Traduisez : Cette année, le vote anticipé a commencé lundi.”); English keys byte-identical.
  - #149: registry line is a French apparatus line (“Tâche ouverte — points dans le cadre d’écriture ; texte modèle dans le cadre de cette page”, note “Noté sur les points”).
- Full text-set diff vs core SVGs: on P2–P7 every core-only line contains CJK (pure-English lines all byte-identical); P1 differs only in the tagline→badge line and one sommaire line whose English segment is byte-identical with a French gloss (wrap point shifted); P8 key lines re-wrap because all notes now print (French, in parentheses).
- P7's 8 phrases: page-level occurrence counts identical to the core on every page (verbatim property inherited from the frozen English layer; correct page tags 2/2/4/4/2/6/6/2).
- Images: 4 embedded images, MD5-identical to the core; credits identical (English).
- Facts identical (NBA opening Tue Oct 20; World Series Game 1 Fri Oct 23; F1 Austin).
- CJK characters in final SVGs: **0**.
- Re-solve: 36 exercises re-derived against the French notes across all 8 pages (incl. chart arithmetic #82–87: 34/27/61/43/18/100; COLA 3,6 %; 106–100 = 6 points; Texas Oct 19 < Florida Oct 24; House 218–214 = 4 < 10) — all agree.

## P8 answer keys (house format, as EN×DE)
All 149 notes printed, format “key (note)” — plain space before a half-width parenthesis. Keys set at 13.5 pt / lh 1.26, flow bottom 2530, group headers “— Page N —” at 16 pt. **Lowest key baseline measured: 2529.3 → ink bottom 2533.3, 46.7 px clear of the 2580 footer rule.** Battery heads/exercises carry gap=8 (sibling pattern).

## Geometry (mandatory audit — builder run)
Paint-order audit with real-font metrics and stroke-expanded line boxes (`hidden_files/weekly-report-en-fr-build/audit_en_fr.py`), validated on a synthetic positive control (line-crossing, ≥30 % cover, and footer-band defects all detected; clean page silent):
- **Final result: 0 flags on all 8 pages** (cover ≥30 %, footer band, page edges, thin-line crossings).
- Supplementary scans, also clean: text–text overlap vs core (only the masthead/title-line pair remains — same geometry as the shipped core, clear air verified in the render) and a box-title spill scan (0).
- Defects found by the scans and fixed in this build (explanation-layer geometry/text only):
  1. P1 clock band: French band-right lines overlapped the English headline by 60 px (line 1) and 32 px (line 2) → compressed to “L’EUROPE RECULE · L’AMÉRIQUE ATTEND” / “Amérique : le 1er novembre · page 7” (gaps 74 / 44 px; sibling pattern).
  2. P1 word-of-week gloss wrapped to 3 lines; line 2 crossed the y=1844 separator rule and line 3 hit row B → gloss shortened (“(Reculer d’une heure.) …”, 2 lines), start raised (my+168 → my+160), rule moved 1844 → 1852. Crop-verified.
  3. P2 AND-YOU box: the French rendering (5 lines) overran the box formula (col-3 end 1621.6) and crossed the TELLING THE TIME rule at y=1558 → compact French echo (2 lines, sibling pattern): “Un hot-dog dans votre frigo ? Vos revenus du mois ? Deux phrases en anglais !” Box now ends 1534.6. Crop-verified. P2 exercise gaps set to the sibling values (heads gap=8, exercises gap=9, matching gap=8); several notes trimmed to one line.
  4. Box titles spilling past their boxes → shortened: P4 fixtures “· Le programme” → “· Agenda” (35 px spill, reached the next column); P3 “SAY IT ON THE NIGHT · À dire ce soir-là” → “· Ce soir-là”, “DATES TO REMEMBER · Dates à retenir” → “· À retenir”; P6 “HOW TO FOLLOW IT · Comment suivre” → “· À suivre”, “ELECTION WORDS · Mots des élections” → “· Vocabulaire”; P5 “WORDS OF THE SCREEN · Mots de l’écran” → “· L’écran” and P6 “HEADLINE LANGUAGE · La langue des titres” → “· Les titres” (both had crossed the page edge: 1957 / 1967 > 1950); P1 numbers box “· En chiffres” → “· Chiffres” (1 px spill).
  5. Section heads too wide → French halves shortened: P3 A “· Vrai / faux”, B “· Fête”, D “· Transformer”; P4 B “· Sport”; P5 B “· À l’écran”, C “· En direct”, D “· Vrai / faux”; P6 chart head “· Graphique”, r6 head “· À compléter”; P8 B head “· QCM” (the long variant measured too wide).
  6. P6 article gloss box overflowed its column (bottom 1420) → trimmed to “midterm (elections) = … · the House = la Chambre des représentants · margin = l’écart.” (turnout/incumbent are glossed in the same page's ELECTION WORDS box and in P8 §F — sibling precedent). Article flow now ends at y=1408, exactly the core's end.
  7. P6 chart: honesty line set as a two-line paragraph (English byte-identical + “Données d’exercice, simplifiées et inventées ; ce n’est pas un vrai sondage.”) with the chart rect moved chy+76/h356 → chy+96/h336 (box bottom unchanged), per the sibling pattern.
- Build log: zero FLOW OVERFLOW and zero HEAD TOO WIDE warnings; all flows end inside their bounds. All 8 cards viewed; the two repaired zones (P1 gloss, P2 AND-YOU) additionally crop-checked.

## VOL.2 promises carried over in French (must be honoured next issue)
Halloween night Sat Oct 31; clocks fall back Sun Nov 1; Election Day Tue Nov 3 and its results (P7 teaser, French); real readers' letters from VOL.2 and comments on VOL.1's page-8 writing (readers'-corner note, French); the best AND-YOU sentences printed in VOL.2 page 7 (P2 box promise, English line frozen + French echo).

## Reproduction
```
cd hidden_files/weekly-report-en-fr-build
/tmp/wp-venv/bin/python -c "import content12, content34, content56, content7, content8"   # fixed import order; writes svg/ in files/weekly-report-en-fr/
/tmp/wp-venv/bin/python audit_en_fr.py ../../files/weekly-report-en-fr/svg               # must print TOTAL FLAGS: 0
# cards: cairosvg svg2png output_width=1950 · print PDF: svg2pdf + pypdf merge · web PDF: PIL thumbnails 1400×1938, quality=85
```
Not posted to Discord (per assignment).

## Independent proofread record (2026-10-21, fresh reviewer, full pass — ZERO problems)

Complete independent pass over the shipped artifacts; no defect found, nothing to fix, no re-render needed. Verdict: **PASS — final**.

- **Reproducibility**: scratch rebuilds of the FR build and the frozen core build each reproduce all 8 shipped SVGs byte-identically → core untouched by this edition; deliverables match their sources.
- **Core-integrity diff** (full visible-text multiset diff, both editions): every English sentence/stem/option/key unchanged except the documented items. Registry key diff = exactly **#136, #139, #149** (French values as documented above; #137/#138 prompts French, keys byte-identical English) — the same differing-key pattern as the EN×DE precedent. P1–P7 core-only lines all carry the core's Chinese apparatus; P8 battery-only lines likewise (28 core-only, all CJK/full-width; 30 FR-only, none).
- **Explanation-language audit**: CJK characters in the FR SVG markup = **0**. All **149 French notes read against their core counterparts — faithful in full** (numbers, names, dates, grammar points all preserved; decimal commas correctly localized: 3,6 % / 22,54 / 13,5 milliards / 3,8 milliards / 0,45 kg). French apparatus natural and grammatical throughout (glosses, instructions, sidebars, readers'-corner and VOL.2 teaser included). Exercises re-solved from the FR paper's own stems/articles — all 149 keys agree (spot anchors: chart #82–87 = 34/27/61/43/18/100; COLA 3,6 %; 106–100 = 6; matching maps P2 b/d/c/a · P4 d/b/a/c · P8 b/c/d/a; clocks 8:00/2:30/7:45 match their drawings). Writing model byte-identical to the core's (word count therefore identical). P8 typography: space before every note parenthesis, half-width only (full-width parens = 0, glued parens = 0).
- **P8 printed keys**: all 149 entries parsed from the shipped P8 SVG and compared to the registry — keys AND French notes match exactly, 0 mismatches; 8 group headers present; **lowest key baseline re-measured 2529.27** (builder: 2529.3) → 46.7 px clear of the 2580 rule.
- **Geometry (independent audit)**: own paint-order audit (real-font PIL metrics; coverage ≥30 %, footer band, page edges, stroke-expanded thin-line crossings, text–text overlaps), validated on a synthetic positive control (all five defect classes fire; clean page silent). Result on the shipped FR SVGs: **zero defects on all 8 pages**; the only text–text band pairs are the masthead wordmark/title and the inner-page band title/sub-line — visually adjudicated on the cards as clear air, same geometry as the core. Builder's audit re-run on shipped SVGs: 0 flags. Every builder fix re-verified in the shipped renders: clock-band gaps measured 68.3 / 38.5 px of clear air (builder claimed 74 / 44 — metric difference only, no contact either way); word-of-week gloss 2 lines, baselines 1812.0/1837.7, rule at 1852, crop-clean; AND-YOU box bottom measured **1534.6 exactly**, crop shows the « phrases » descender clears the box border with visible air and the TELLING THE TIME rule (1558) is 21.8 px below the band bottom; all eight shortened box titles measured inside their boxes (margins 15–73 px); P6 honesty paragraph (2 lines, ends x=913 / 538) clear of the READING rule (y=1507, x 989–1423) and the chart rect (top 1552, ink clearance 8.4 px); chart rect bottom 1888 = core's.
- **Badge/footers/masthead**: brick-red pairing badge on P1 (« TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES »); French pairing footers on all 8 pages (« Page N sur 8 »); masthead “The Lucerna”.
- **Facts**: weekdays verified against the 2026 calendar (NBA opening Tue Oct 20; World Series Game 1 Fri Oct 23, Game 2 Sat Oct 24; Europe DST Sun Oct 25 vs US Sun Nov 1; Halloween Sat Oct 31; Election Day Tue Nov 3) — all as printed. P7's 8 phrases byte-verbatim; per-page occurrence counts identical to the core. 4 images MD5-identical to the core; credits identical (English).
- **Deliverables**: print PDF 8,623,199 B / sha256 a6f003c1…f6d18b; web PDF 4,421,142 B / sha256 65a52868…f9dd9 — both match the KIT, both 8 pages.
- **Out-of-scope observation** (frozen core, for the record — NOT an EN×FR defect): the same audit run on the core flags the core P1 word-of-week Chinese gloss line (baseline 1846) crossed by the y=1844 rule; the FR and DE editions do not inherit it (gloss rewritten, rule at 1852).

## D5 rebuild (2026-11-13, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-fr/`; per-edition report: `production/notes/2026-w43/g-en/scratch-d5-rebuild-en/D5-REPORT-2026-w43-en-fr.md`.

**Install**: core landed with `apply_variant.py --patch-core en --week 2026-w43` (core-en `svglib.py` +95/−3, `_D5_READER = "latin"`); this edition installed with `--svglib patched/…/svglib.py --target en --reader fr --week 2026-w43`, `_D5_READER = "latin"` (installed svglib md5 identical to the production core-en install); routing unit test FAILURES: 0 (66 PASS); fix2 block kept.

**Baseline** (pre-fix production build): run TOTAL 149, 0 warnings; print PDF byte-identical to `MANIFEST-W43-D1.md`; print/web text layers differ by 0 chars; self-built web vs shipped web differ by 0 non-space chars (spaces only); pre-fix census D5 Latin 598, Cyrillic 0, curly in CJK 59 (the family's highest — French « » quotes); baseline P8 noted 149/149.

**Defects and fixes** (run1: 12 items, all D5 widening except the pre-existing P2 spill, which the baseline shares; sizes only, no wording changed):

- heads ×6: P3 `A　TRUE OR FALSE ?　Vrai / faux` 25→24; P4 `C　COMPARATIVES　Comparatifs` 25→23 (24 still 2.5 px over); P5 `EARNINGS, IN PLAIN ENGLISH` 26→25; P5 `D　TRUE OR FALSE ?　Vrai / faux` 25→24; P6 `READING THE CHART　Graphique` 24→23; P8 `D　SENTENCES　Phrases à former` 24→23 (column width 422.5).
- occlusion ×1 (P1): band headline vs subtitle `L'EUROPE RECULE` overlapped 121.2×20.8 px → headline 46→**42** (44 still overlapped).
- creambox/boxtitle ×4: P1 `THE WEEK IN NUMBERS　Chiffres` +12.5 px → `tsize=22`; P2 `DO THE MATHS　À vous de calculer` +14.7 px → `tsize=22`; P3 `FESTIVAL WORDS　Mots de la fête` +5.1 px → `tsize=22`; P6 `HEADLINE LANGUAGE　Les titres` +6.2 px → `tsize=22`.
- spill ×1: P2 `Check your number !` below the DID YOU KNOW box by 12.71 px → box-height formula tail +14→+34 (box bottom +20 px; same pre-existing defect as core-en).

P8: 221→221 lines, footer slack 34.9→34.9 px.

**Gates run2 (all 17 ALL-GREEN)**: run TOTAL 149, 0 warnings; head_check 0; d5 census 0/0/0; render RC=0; webpdf RC=0 (1,072,352 B < 7 MB); occlusion 0 flags; p8 extract noted 149/149; p8 compare **EXTRA_ONLY** (extra_count=87, adjudicated accepted; keydiff=[136, 139, 149], the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0; spill 0; boxtitle 0 DEFECT (57 titles); edge 0/0; creambox PASS 0 defects; text layer print=web diff 0; census_quotes 0 defective; no family gates.py for en.

**New deliverables**: print `The-Lucerna-VOL1-en-fr.pdf` 7,502,963 B (`44b55142…`); web `2026-w43-en-fr.web.pdf` 1,072,352 B (`cb02ed90…`); text.md byte-identical (`2b25e2aa…`). Still 149 exercises; answer keys differ from the core only at #136/#139/#149, as registered.
