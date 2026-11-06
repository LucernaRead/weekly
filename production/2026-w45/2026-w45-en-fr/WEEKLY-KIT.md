# WEEKLY KIT — The Lucerna · ENGLISH WEEKLY VOL.2 · EN × FR edition

**Masthead:** The Lucerna (unchanged). P1 edition line: HEBDOMADAIRE EN ANGLAIS · VOL.2 · ÉLECTIONS · FOOTBALL · CINÉMA.
**Badge (P1, y=372 slot, 19.5pt BRICK):** TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES.
**Footers (all 8 pages):** left "The Lucerna · HEBDOMADAIRE ANGLAIS VOL.2 · TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS", right "Page N sur 8".
**Week:** Mon 2026-11-02 → Sun 2026-11-08 (W45) · VOL.2 · 8 pages (1950×2700) · **150 exercises** (A2 60 · B1 69 · B2 21; per page 10/17/18/18/18/18/12/39 — identical to the core, independently re-counted from the registry).
**Status: builder-complete, NOT final.** This report does not claim independent proofread (SOP still requires a full zero-problem independent round before final). No Discord delivery, no main-chat cards/PDFs, no repo insert, no cron — those belong to the parent line.

## 1. Deliverables

`files/weekly-report-w45-en-fr/`:

- `svg/` — 8 pages of SVG sources (p1-front … p8-exercices)
- `cards/` — 8 full-page PNGs, 1950×2700 (all 8 viewed by the builder)
- `The-Lucerna-VOL2-FR-print.pdf` — merged 8-page PDF, 17,295,418 bytes · sha256 408a67f7b25d2fb509ed6c6f6252fa1ffc7f0d8e9ca7c2f43e1ff923c04d0c74
- `The-Lucerna-VOL2-FR-web.pdf` — compressed PDF, 3,884,123 bytes (< 10 MB) · sha256 5e32b328302815cec138f9b352a62f23d70152124d04f4f1385efd67dddb4706
- This file + `ABSTRACT.txt`

SVG sha256 (final): p1 03aedc904164f05f8ffb8b3e66e146e1d153ce062e16ebac536f1d84c9960595 · p2 d8cb1ea3eb36a5795eb9659be97a9504583a1c187bbc3385f38f788185ca1409 · p3 123b64f5e019c9905246dfa2aef05a1d6df6da33dbd6175f14d829c53b2406d8 · p4 146ad42712719644f0d459a7f1a7357c55b2a4b3c4d0239ec7b86de70a7591ba · p5 eb749740b4e7efe3869db2d5eb3f5d0594425e27daabb8627eefacfe72f76286 · p6 dff0138924e5aa0880a5b210da82481b941f3737f2a0646d7953276ee4ac08bd · p7 4ca6df6eee69a27ef5f5eff844f9d41dcc169326e67575f84a11e0571d323b24 · p8 5aeadb180e5c921f74f088a3bdc3d064acc384f36c2d7a8e7ce8544390d6817e.

Build tree: `hidden_files/weekly-report-w45-en-fr-build/` — `transform.py` (the single source of the transformation; every fix round edited it, never the generated files directly), `run.py` (single-process driver), `render.py` (cards + PDFs), `scans.py` (extra scans), `check_reg.py`, `gloss_count.py`, per-round sha256 baselines (`round1-baseline-core.txt`, `round2-baseline-svg.txt`, `round3-baseline.txt`, `final-hashes.txt`), and raw gate outputs (`freeze-diff.json`, `freeze-diff-final.json`, `p8-compare.txt`, `p8-compare150.txt`, `p8-compare150.json`, `occlusion.json`, `occlusion3.json`, `occlusion-final.json`, `scans.txt`, `reg-check.txt`, `gloss-count.txt`, `cjk-lines.txt` — the core's Chinese-line inventory the transform was built from).

## 2. What this edition is

The W45 EN core (`files/weekly-report-w45-en-core/`, VOL.2) with ONLY its explanation layer replaced by French, exactly as the W43 EN×FR edition did for the W43 core: every gloss, grammar point, instruction, section-head French half, chart note, clinic note, readers'-corner disclosure, teaser echo, and all P8 answer notes are French; the English body text is frozen. No third language anywhere: edition SVG CJK = 0, and the banned intermediary term occurs 0 times in every deliverable (checked in SVG, KIT, ABSTRACT, and build code).

Per-page content (core's, verified against the core KIT and the rendered pages):

- P1 (A2, 10): head story "America Votes : Election Day Comes on Tuesday, November 3" (midterms: all 435 House seats, about a third of the Senate, governorships; early voting; counting takes time); searches chart (late-October snapshot, labelled relative interest, not exact volumes); sommaire; word of the week "midterm"; voting-booth photo + "FALL, THE SEASON OF VOTES"; IN BRIEF; LIGHTNING QUIZ (4).
- P2 (A2, 17): clocks fall back Sun Nov 1 (2 a.m. → 1 a.m., 25-hour night; Arizona and Hawaii do not change); Halloween Sat Oct 31 as a past event; Nov 6 films; telling-the-time column (1:00 / 1:30 / 7:45 clocks); 1912 Halloween postcard.
- P3 (A2→B1, 18): Fri Nov 6 films "The Cat in the Hat" (Dr. Seuss, Bill Hader) and "Godzilla Minus Zero" (Takashi Yamazaki); at-home week (Netflix Nov 4/5/6/8); five-sentence reviews; Manet cat illustration (caption states it is not film art).
- P4 (B1, 18): Sun Nov 8 — NFL Week 9 Madrid game (Bengals–Falcons, Bernabéu) + Dolphins–Lions (Miami); F1 São Paulo Grand Prix; NASCAR Homestead-Miami; WTA Finals Indian Wells; boxing Baumgardner–Turhan (Arlington); Sat Nov 7 MLS fixtures; 1910 football photo.
- P5 (B1, 18): election night at home (maps, second screen, pizza) — answers the VOL.1 question; "Too close to call" taught; Sat Nov 7 MLS warm-up.
- P6 (B2, 18): how America votes (one country, fifty elections; House 2-year terms, Senate 6-year terms, about a third per election); practice ballot (candidates only as codes A–D); teaching chart "WHY DO VOTERS VOTE EARLY ?" (38/29/21/12, total 100, labelled on the page as teaching data, not a real poll); Capitol photo.
- P7 (A2/B1/B2, 12): three level columns (A2 falling back + going to; B1 comparatives + past simple; B2 headline present + whether); toolbox (one sentence per level); phrases of the week (8, all from this issue's own articles); error clinic (4); readers' corner; VOL.3 teaser (Wed Nov 11 Veterans Day, Sun Nov 15 NFL in Munich, midterm results reported).
- P8 (39): cloze 8 (Leo's Nov 3) + multiple choice 9 + reading 4 (Sam, Ohio teacher, early voting) + sentences 4 + translation 4 + matching 4 + dialogue 5 (voting place) + writing 1 ("My Tuesday, November 3", 80–100 words; model 85 words by raw-whitespace count, model text byte-identical to the core's).

## 3. Furniture registry (same-pairing precedent)

All furniture strings follow the SHIPPED W43 EN×FR SVGs (`files/weekly-report-en-fr/svg`), which outrank the tables.json generalisations for this pairing:

- Badge, footer, page line: as in the header above (VOL.1 → VOL.2 updated; footer keeps singular "TEXTE EN").
- Gloss prefix: "Note | " — the shipped W43 EN×FR gloss boxes read "Note | ", not the tables.json "Note — " generalisation (which the table itself flags as the cross-column pattern with EN×FR as the early variant). This edition uses the shipped same-pairing form.
- P1 geometry: edition line at y=330 (46pt serif bold); badge replaces the y=372 strapline slot in place at 19.5pt BRICK (W43 EN×FR geometry; the core's English strapline line is the slot, per README #20's EN-core case). Top strip centre: "WEEKLY IN ENGLISH · Chaque semaine · L'anglais que lit l'Amérique" (W43 shipped line, core's centre text is identical).
- Instruction-line method renamed `bridge()` → `instrline()` (W43 EN×FR build precedent); gloss boxes auto-prefix "Note | "; instruction lines carry "Note | " explicitly where the core had its Chinese instruction prefix.
- Exercise types (registry strings, W43 EN×FR forms): Compléter / Choix multiple / Transformation / Compréhension écrite / Texte à trous / Dialogue à compléter / Traduction / Appariement / Lecture de graphique / À vous (phrases) / Correction (clinic) / Écriture (writing). Instructions: Complétez / Réécrivez / Corrigez / Associez.
- P8 heads (W43 EN×FR forms): "A · CLOZE · Texte à trous", "B · MULTIPLE CHOICE · QCM", "C · READING · Compréhension", "D · SENTENCES · Phrases à former", "E · TRANSLATION · Traduction", "F · WORDS · Mots à associer", "G · DIALOGUE · À compléter", "H · WRITING · Écriture [B1]"; band "EXERCISES & ANSWERS · Exercices et réponses", sub "FINAL TEST · Test final · Answers at the bottom of this page"; ANSWERS head "ANSWERS · Toutes les réponses commentées (pages 1 à 8)"; separators "— Page N —"; keys at 13.5pt/1.26, keys flow bottom 2530, ALL notes printed in half-width parens (full-width parens = 0 in P8).
- P7 heads (W43 EN×FR forms): "LEVEL A2 · Les bases", "LEVEL B1 · Plus loin", "LEVEL B2 · Le défi", "THE TOOLBOX · Boîte à outils", "THE EXAMPLE · L'exemple", "PHRASES OF THE WEEK · Phrases de la semaine (de ce numéro)", "THE ERROR CLINIC · Les erreurs", "READERS' CORNER · Courrier des lecteurs", "NEXT WEEK · VOL.3 La semaine prochaine"; band "LANGUAGE IN HAND · La langue en main".

## 4. Measured gates (all re-run on the final files)

- **Core baseline:** `tools/freeze.py baseline` on the W45 core build: **8/8 SVGs byte-identical**, shipped core SVGs re-hashed unchanged.
- **Freeze diff** (core vs edition, final run): added CJK = 0 on every page; edition CJK = 0. Removed strings with no CJK: P1 — the y=372 strapline (the badge slot, §3) plus one key-box line re-wrap fragment (same English words, "·" moved by re-wrapping); P7 — two re-wrap fragments ("6)." from the B2 example box, one lone Chinese full stop); P8 — 20 key-line re-wrap fragments (French notes lengthen key lines, so the " · "-joined sequences split at different points; keys themselves adjudicated by `p8.py`, below). No English body sentence is lost: every pure-English removed string is a wrap fragment of text present in the edition, or the documented badge slot.
- **P7 frozen-word gate:** all 8 golden sentences verified verbatim in the P7 SVG; all four column definition sentences verified verbatim ("The clocks fell back.", "She is going to vote on Tuesday.", "The Bernabéu is bigger than most stadiums.", "Nobody knows whether the race is called yet."); only glosses/notes localised. P7 structure measured from the core (3 level columns + toolbox + 8 phrases + 4-item clinic + readers' corner + teaser), not copied from any other family.
- **P8:** `tools/p8.py compare --total 150`: core 78 noted → edition **150 noted**, status **EXTRA_ONLY, missing=[]**, extra_count=72 (the 72 numbers whose notes the core suppresses by its length/type rule but the FR edition prints in full, W43 EN×FR pattern). keydiff = **[137, 138, 139, 140, 150]**, adjudicated item by item (printed keys extracted from both P8 SVGs):
  - 137: core Chinese key (EN→ZH in the core) → FR "La patience fait partie du système, et non un échec de celui-ci." — EN→FR redirection, legal.
  - 138: core Chinese key (EN→ZH in the core) → FR "Le mardi 3 novembre est le jour des élections aux États-Unis." — EN→FR redirection, legal.
  - 139: core Chinese key (EN→ZH in the core) → FR "Dimanche, la NFL joue à Madrid." — EN→FR redirection, legal.
  - 140: core Chinese key (EN→ZH in the core) → FR "Tous les endroits ne changent pas." — EN→FR redirection, legal.
  - 150: writing open-task key description, core Chinese → FR "Tâche ouverte — points dans le cadre d'écriture ; texte modèle dans le cadre de cette page" — same meaning, translated (W43 EN×FR precedent used the identical French wording).
  - 145 (dialogue "ID"): keys identical ("ID" = "ID") — the earlier parse artifact (the note's inner "(ID)" parenthesis) was removed at source in round 3 by shortening the note to "Au vote, on montre sa pièce d'identité"; it no longer appears in keydiff.
  - **Measurement note on translation direction:** the core's four P8 translation prompts are ALL English sentences (137 "Translate :", 138/139 (core instruction word = Chinese for "translate") + an English sentence, 140 "Translate :") with Chinese keys — i.e. this core's battery is EN→ZH throughout; only the instruction word (English "Translate :" vs the Chinese word for "translate") differs between items. The FR edition therefore renders all four as EN→FR (English prompt, French key). There is no ZH→EN item in this core to mirror as FR→EN.
  - P8 notes are pure French (P8 SVG CJK = 0, full-width parens = 0); lowest key baseline re-measured from the final SVG (see §5).
- **Gloss counts** (rendered `gloss()` strings split on "·" itself, README #21): P1+P2 core 3 = FR 3; P3+P4 core 8 = FR 8; P5+P6 core 7 = FR 7; total **18 = 18**. P1 bridge line (not a `gloss()` call): 4 items = 4 items. P7 phrases: 8 grammar points = 8, plus 8 exercise notes = 8 (each golden sentence counts 2×, labels/levels identical to the core: 100 A2, 101 A2, 102 B1, 103 B1, 104 B2, 105 B2, 106 A2, 107 B1).
- **Geometry:**
  - `tools/occlusion_audit.py` (selftest passed first): edition **1 flag** (TEXTX, P1 wordmark vs edition line, 834.2×6.2px), core **0 flags**, NEW = 1 — adjudicated below; no COVER/LINEX/FOOTER/EDGE/BOXTITLE flags on any page.
  - **Occlusion adjudication (measurement artifact, not a defect):** rendered pixels of the final P1 card show wordmark ink rows 150–292 (150–293 at threshold 240), a paper gap, then edition-line ink from row 295 — a 2px clear gap, MORE than the core's own 1px gap (core: wordmark ends 289, edition line starts 291) in the identical geometry. The tool's font-metric boxes overestimate the edition line's top by ~11px (tool box top 283.75 vs rendered ink top 295, verified at thresholds 128/200/240). The IDENTICAL flag (834.2×6.2) fires on the shipped W43 EN×FR edition under the same tool, i.e. this is the known artifact of the W43 furniture pair, not a new defect; moving the edition line would break the W43 shipped geometry for a non-defect, so the geometry is kept. The literal "NEW = 0" tool-output reading is therefore NOT met; the true-defect count is 0. The independent proofreader is asked to confirm this adjudication (pixel evidence above + W43 precedent).
  - Builder's extra scans (`scans.py`, decoded measurement): same-baseline furniture bands (top strip y=92, band heads 116/142, dark band 478/522, footers 2624) — no pair gap under 40px anywhere. Right-edge ADVANCE scan: no text advance past the inner frame (1910) or the page edge; the only advances past the content edge (1885) are two frozen P8 matching lines (1899.4, 1903.8) that are byte-identical in position and text in the core (same x, same strings; their y shifted only by the battery's one extra wrapped line, §5). P6 chart labels, baseline-anchored ink (PIL getmetrics, anchor ls) vs later-drawn rects: all four labels 0.0% coverage, gate <30% passed. (P6's chart is text lines, not bars, as in the core; there is no bar rect to cover a label.)
  - P8 lowest key baseline: Levels line at 1470.965 (ink bottom ≈1476.8), 9px clear of the writing-strip rule at 1486 — see §5.
- **Visual:** all 8 cards viewed in full (not just P1/P6/P7/P8). No overflow, overlap, or footer strike found. Two inherited core renderings are kept unchanged per the freeze rule and are NOT FR defects: the practice-ballot ☐ glyphs render as crossed boxes (identical in the core card crop) and the clinic ✗ marks render the same way (identical in the core).
- **Counts (independent registry run, one process):** total 150; per page 10/17/18/18/18/18/12/39; levels A2 60 / B1 69 / B2 21; numbering continuous 1–150, no gaps or duplicates. Essay model 85 words (raw-whitespace count, the core's own convention), model text byte-identical to the core's.

## 5. Fix rounds (all edits in transform.py; pre-fix sha256 baselines recorded each round)

- **Round 1:** first render, 150 exercises, but FLOW OVERFLOW on P1-headline and P2-exercises, and the P8 battery ran one line long (Levels line ink crossed the writing-strip rule). Causes measured, not guessed: (a) P1 bridge + two box lines each wrapped to 4 lines in French vs 3 in Chinese (+~90px); (b) P2 bridges A and C each gained a line, cascading the column packing so the final match block (362px) no longer fit its column; (c) P8 E139's English prompt wraps to 2 lines under "Translate : " (core: 1 line under the Chinese instruction word), shifting the battery by one ex-body line (29.725px), proven by y-sequence diff of the two P8 SVGs.
- **Round 2:** shortened the P1 bridge ("Note | a midterm = mi-mandat · a ballot = bulletin de vote · a race = course électorale · to call a race = annoncer le résultat.", 3 lines) and box lines ("(tous les sièges en jeu)", "(deux rendez-vous dimanche)", each 3 lines); shortened P2 bridges to one line each ("D'après l'heure, complétez en anglais.", "Lisez la page 2 et choisissez." — the latter mirrors the W43 EN×FR "Relisez la page 2 et choisissez."); recovered the P8 battery with two gap tweaks (dialogue paragraph gap 10→2; F match_set gap 14→8, the W43 EN×FR match gap). Result: zero FLOW OVERFLOW / HEAD TOO WIDE warnings; P1-headline ends 1502 (bottom 1828), P2-ex ends 2532 (bottom 2562), P8 battery ends 1499 with the Levels baseline at 1470.965.
- **Round 3:** P8 compare (total 149 default) showed keydiff 145 as a bracket artifact from the note's inner "(ID)"; shortened that note (see §4). Re-ran with `--total 150`: EXTRA_ONLY, keydiff [137, 138, 139, 140, 150] as adjudicated above. No other content changed in round 3.

## 6. Readers' corner (coordinator ruling, applied verbatim)

No reader, letter, name, or quotation is invented. The core's English example quote ("On Sunday, I slept one hour more — and I still woke up late !" — M. L., a reader in Chicago, with its "(editor's example : …)" label) is kept byte-identical, as are the English teaser promise and the P8 writing promise ("The best texts will appear in VOL.3"). The core's Chinese disclosure paragraph becomes the French disclosure (3 lines, inside the box): it states all three facts — no real letters arrived for VOL.2, no best page-8 writing from VOL.1 arrived, the labelled example stays and the promise moves to VOL.3 — plus an explicit imperative invitation with a VOL.3 publication promise ("Envoyez vos lettres : les meilleures paraîtront dans le VOL.3 !"). No new English disclosure sentence was written (the core has none; the analogous IT×EN item was already ruled non-blocking for the same reason). The teaser line itself is not counted as the invitation.

## 7. W45 deviations from the core, deliberate and measured

Beyond the furniture registry (§3) and the round-2/3 repairs (§5): (1) P1 word gloss is a one-liner ("midterm election = une élection de mi-mandat.") so the core's geometry (gloss baseline my+168, row-B rule 1844) is untouched — a two-line French gloss would have struck the rule; (2) dark-band right lines shortened to "ÉLECTIONS MARDI · HORLOGES RECULÉES" / "Mardi 3 novembre, jour des élections · page 6" so the advance-measured gap to the English left lines stays ≥100px; (3) box-title French halves shortened where PIL measurement exceeded the box (AT HOME THIS WEEK · À la maison; THE CAT'S HAT · Le chapeau; SUNDAY, NOVEMBER 8 · Agenda; TOO CLOSE TO CALL · Trop serré; A PRACTICE BALLOT · Bulletin test; FIVE SENTENCES · Cinq phrases; HOW LONG ? · Quelle durée ?; THE WEEK IN NUMBERS · Chiffres; DO THE MATHS · À vous de calculer; WHY MADRID ? · Pourquoi Madrid ?); (4) P6 chart head "READ THE CHART · Graphique" (W43 EN×FR chart-head form); (5) P8 battery gap tweaks (§5). Nothing else moved: every other French string keeps the core's coordinates, sizes, and line heights.

## 8. Reproduction

```bash
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-en-fr-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python transform.py  # core -> FR build files (asserts every replacement + post-conditions)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py         # single-process driver, generates 8 SVGs in order (never import a content module standalone)
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py      # cards + print PDF + web PDF
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-en-core/svg --edition-svg ../files/weekly-report-w45-en-fr/svg
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-en-core --edition-dir ../files/weekly-report-w45-en-fr --target fr --total 150
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-en-fr --core ../files/weekly-report-w45-en-core
```

Interpreters (both recorded, as required): `run.py` runs under `tools/venv/bin/python` (Python 3.12.3, Pillow 13.0.0); `render.py` runs under the same `tools/venv/bin/python` (Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1). System python3 has no cairosvg and must not be used for render.py. Font note: the build library's font table resolves the split NotoSerifCJK/NotoSansCJK TTCs (SC face index 2 for the French Latin text path, same as the core build).

## 9. Open items for the independent proofreader (not builder defects)

1. Confirm the §4 occlusion adjudication (1 tool TEXTX flag = measurement artifact; rendered 2px paper gap, core 1px, identical flag on shipped W43 EN×FR).
2. Full proofread to zero problems (SOP gate) — this build report is builder self-check + mechanical gates only.
3. Repo insert (insert.py) and any delivery are the parent line's serialized work; this task deliberately did not touch weekly-git.
4. VOL.3 must honour the carried promises: real readers' letters + best VOL.1 page-8 writing deferred (readers' corner disclosure), Nov 11 Veterans Day, Nov 15 NFL Munich, midterm results (teaser).
