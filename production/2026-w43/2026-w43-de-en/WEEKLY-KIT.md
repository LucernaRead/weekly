# Die Lucerna — 德语周报 VOL.1 · ENGLISH-EXPLANATIONS EDITION · WEEKLY KIT

**Edition:** German core VOL.1 × English explanations — **matrix cell DE × EN**. Same frozen German core as the first issued pair (German text + Chinese explanations, `files/weekly-report-de-vol1/`); only the explanation layer was rewritten, into English. Languages pair one-to-one; the English part is explanations （讲解）, written directly in English.
**Week:** Mon 2026-10-19 → Sun 2026-10-25. **Lead story:** „Eine Stunde geschenkt" — Zeitumstellung (Sun Oct 25, 03:00→02:00) + Herbstferien peak in 11 Länder (unchanged from the core).
**Status:** Built + full proofread complete (see record below). NOT posted to Discord (per assignment).

## Pairing badge (new in this edition, per current production standard)
- **Masthead badge, P1 (centered, bold olive, directly under the edition line):**
  `TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`
- **Footer on all 8 pages:** `Die Lucerna · GERMAN WEEKLY VOL.1 · German text · English explanations` / `Page n of 8`.
- Section headers are German + English throughout (e.g. `LEBEN · Life`, `ÜBUNGEN · Page 2 exercises`, `ANTWORTEN · All answers with notes (pages 1–8)`).

## What was changed vs. the core — and what was not
- **Changed (explanation layer + page furniture only):** every gloss/note box (now prefixed `Note —`), all exercise instructions (Fill in / Rewrite / True or false? / Build a sentence / Translate into English / Translate into German / Match the pairs), all section bridges and explainers, error-clinic notes, toolbox glosses, readers'-corner note, phrase-of-the-week translations (P7 — the German quotes themselves are untouched), the VOL.2 teaser heading, the writing-task instruction, and **all 150 P8 answer notes, now in English**. Exercise type labels in the registry are in English (fill-in, multiple choice, transformation, matching, true/false, cloze, sentence building, dialogue completion, translation, writing).
- **Unchanged (frozen core):** all German articles, headlines, exercise bodies and options, the fixture table, the practice chart data and its German labels, all facts and dates, the 4 public-domain images and their credit lines, the model text (87 words), page geometry (1950×2700, 4 columns), layout code (copied, not shared — originals untouched).

## Measured totals (visible-text extraction from the rendered SVGs, text elements summed, no separators — same method applied to both editions)
- **Exercises: 150** — identical registry: A2 67 · B1 69 · B2 14; by page P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38 (all match the core KIT).
- **Text volume: 46,740 characters** (after the independent-proofread fixes below; as first built: 46,698. Core by the same extraction: 39,985; the core KIT's own count is 40,036). The increase is the English apparatus: Latin-script explanations run longer than the Chinese ones they replace.

## Zero-diff verification (core is frozen)
1. **Registry diff** (both builds' exercise registries dumped and compared entry by entry): 150 = 150; numbers, pages and levels identical for all 150. **Keys identical for 147/150.** The 3 exceptions are inherent to the pairing, not content changes: #137/#138 are the two German→reader-language translation keys, re-expressed in English („The night has 25 hours." / „I change the clock on Saturday evening."); #150 is the writing item's registry line, an apparatus instruction (open-task note), now in English. #139/#140 (reader-language→German) keys are German and byte-identical.
2. **Rendered-text diff** (all visible text extracted from both editions' SVGs, CJK stripped from the core text): every German fragment of the core is present in this edition. The only unmatched core fragments are the known mixed strings — masthead lines, gloss/bridge lines, box lines with parenthetical glosses, section headers, footers — i.e. exactly the apparatus strings this edition exists to replace; their German components are unchanged.
3. **CJK scan of this edition's rendered pages: 0 CJK characters on all 8 pages** (build sources also scan 0).
4. **P7 phrases:** all 8 verbatim quotes occur exactly 2× in the rendered text (article + P7), same as the core.
5. **Images:** 4 embedded images (frost P1, atomuhr P2, luther P3, kuerbis P5) with the core's credit lines unchanged; `assets/CREDITS.md` copied with the build.

## Adjudications
1. **Translation exercises (P8 §E)** pair the target language with the reader's language by definition, so in this edition they are DE↔EN (core: DE↔ZH): the two German sentences and the two German answer keys are byte-identical; the two reader-language sides are English (prompts „On Sunday I sleep an hour longer." / „You can borrow books at the library.", keys for #137/#138 in English). Direction is carried by the instruction label (Translate into English / Translate into German) so each item stays on one printed line, as in the core.
2. **Layout accommodations for longer English apparatus** (no core content touched): P8 answer keys set at 13 pt (core: 14.5 pt) so all 150 English notes fit the page; three P8 section heads shortened (…· Quiz / · Sentences / · Matching) to stay inside the column; three P1 box glosses and the P6 practice-data footnote shortened to fit their fixed lines; the P6 health-box English summary is compressed (the full German STIKO text above it is unchanged); P7 readers'-box height allowance +22 for the 3-line English note. Final build log: **zero FLOW OVERFLOW / HEAD TOO WIDE warnings**; all flow end positions match or sit inside the core's (P1 headline flow ends at y=1585, exactly the core's value).

## Proofread record (builder's full pass on this edition)
- Explanation-language audit: 100% of the apparatus is English — verified by the CJK scan (0) plus a full read of all 8 rendered pages; every English gloss was checked against the German it annotates (the glossed words occur in the articles, as in the core).
- All 150 keys re-checked via the registry diff above; numbering 1–150 continuous; level/page distribution identical to the core KIT.
- English read-through: glosses, notes, instructions and key notes checked for grammar and sense (American spellings: tire, favorite, equalizer).
- Visual pass over all 8 cards: defects found and fixed during the pass — P1 „Die Woche in Zahlen" box title overflowing into the exercise column (shortened to „· Numbers", measured 391.7 ≤ 398 inner width), P7 toolbox title too wide (→ „· Toolbox"), P6 practice-data footnote running off the page edge (shortened, measured 1567 ≤ 1820), P7 readers'-box border crossing the last English line (height allowance +22), P1 headline flow overflow and P6 exercise flow overflow from longer English bridges/glosses (shortened until the final build was warning-free). The raised closing-quote glyph after the Fragen labels is identical in the core's own cards (font rendering of „…“), not a defect of this edition.
- Facts/dates: unchanged from the independently proofread core; nothing re-sourced, nothing added.

## Files
- `svg/` — 8 page SVGs (p1-front … p8-uebungen)
- `cards/` — 8 full-res PNGs (1950 px wide)
- `Die-Lucerna-VOL1-EN.pdf` — print PDF, 10.5 MB
- `Die-Lucerna-VOL1-EN-web.pdf` — Discord web PDF, **4.02 MB (< 10 MB limit)** (re-rendered after the proofread fixes below; re-rendered again 2026-10-21 for the P6 occlusion patch at the end of this kit — print PDF now 10,478,519 B)
- Build sources: `hidden_files/weekly-report-de-en-build/` (copy of the core build with the English apparatus; the core build in `hidden_files/weekly-report-de-build/` was not modified)

## Reproduction
```bash
python3 -m venv /tmp/wp-venv && /tmp/wp-venv/bin/pip install cairosvg pillow pypdf   # if venv missing
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-de-en-build
/tmp/wp-venv/bin/python run.py        # one process, all 5 content files — the registry must accumulate across pages
# then render: cairosvg svg2png @1950 → cards/; svg2pdf + pypdf merge → Die-Lucerna-VOL1-EN.pdf;
# JPEG pages q85 @1400 → Die-Lucerna-VOL1-EN-web.pdf
```

## Independent proofread record (fresh full pass, 2026-10-21)

Method: all visible text extracted from both editions' SVGs and diffed (line multisets + German-fragment check in both directions); both builds re-run in scratch copies and their exercise registries dumped and compared entry by entry; fresh rebuilds verified byte-identical to the shipped SVGs before and after fixes; 60+ exercises independently re-solved against the articles/chart/keys; all 8 cards viewed in both passes.

**Builder's claims — verified:** character totals (46,698 as built / core 39,985 by identical extraction); registry 150 = 150 with identical page (10/18/18/18/18/18/12/38) and level (A2 67 · B1 69 · B2 14) distributions; keys byte-identical for 147/150, the 3 diffs exactly the documented pairing items (#137/#138 English translation keys — both correct; #150 registry instruction line); #139/#140 German keys identical; CJK = 0 in all SVGs and build sources; P7's 8 phrases byte-identical between editions, each occurring exactly 2× in each edition; the 4 images byte-identical payloads with identical credit lines; masthead badge present on P1, pairing footer on all 8 pages; model text = 87 words; chart data 46/22/18/14 and bars proportional; P8 keys legible at 13 pt; the builder's documented fit fixes (P1 Zahlen title, P6 footnote inside the page edge, P7 readers'-box border) all confirmed in the render.

**Problems found and fixed (EN build sources only; whole issue re-rendered, second full pass = zero problems):**
1. **P7 toolbox entry invisible (layout, serious).** The 6th toolbox gloss, "Es ist fraglich, ob ... = it is doubtful whether ...", was drawn at y 833/862 — below the toolbox box (bottom 790.5) and underneath the readers' box rect painted after it, so it never appeared in the render. The `tbh` formula under-allows the drawn height by ~110 (each entry's draw advance carries a +20.5 first-baseline offset the formula omits). Fixed in `content7.py`: height allowance +96 net (per-entry gap 10→6 in formula and draw loop, trailing pad 14→96), rail gaps 26→10, readers' box pad 42→38, "Noch ein Wort" box 150→140 with its text offset 78→74, phrases section py 1520→1524. Verified geometrically in the final SVG: entry 6 baselines 813/842 inside the box (bottom 848.5); readers' last line slack 12.7; word-box slack 7.8; column ends 1505 vs. the phrases rule at 1512. **Note: the frozen core has the identical latent overflow** (its 6th entry sits at y 833 vs. box bottom 761, likewise covered) — flagged here; the core was not touched, per the freeze.
2. **P6 health-box English summary dropped facts.** "…for over-60s, pregnant women and risk groups." omitted two facts the German STIKO text (and the core's Chinese summary) carry: pregnancy **from the second trimester** and **protection builds up in 10–14 days**. Replaced with: "Flu season is coming: STIKO recommends the flu jab for over-60s, pregnant women from the 2nd trimester and risk groups — protection in 10–14 days." (4 lines; box ends y 1400, 8 units above the chart rule; "risk groups" kept as the cover term for the chronically ill and care/medical staff, matching the summary's compression level.)
3. **P7 phrase translation unidiomatic.** "In this night, the hour from 2.00 to 3.00 comes twice." (a calque of "in dieser Nacht") → "That night, the hour from 2.00 to 3.00 comes twice." The German quote itself is untouched and still occurs exactly 2×.

**Kept items (with reasons):** (a) P3 "ZWEI FESTE, EIN TAG" box: its last line "(Kappel-Grafenhausen)." prints ~13 units below the box border into the inter-box gap — geometry byte-identical in the frozen core (same rects, same baselines), fully legible; German core furniture, not introduced by this edition. (b) P8 matching definition "a. ein Tag, an dem man nicht arbeiten" ends flush at the inner frame — pixel-identical to the core render; the word is complete. (c) P2 "Wussten Sie das?" last line sits tight to its box border — identical in the core. (d) 15 registry notes are identical between editions because they are language-neutral (German grammar annotations / arithmetic), not Chinese residue. (e) P1 header fragment "Die Fragen der deutschen Ratgeber" and P8's "Alle Antworten unten auf dieser Seite" exist in the core as bilingual section furniture and are carried by the English section heads in this edition — apparatus, not article/exercise content; every German article sentence, exercise stem, option and key outside the documented pairing items is unchanged.

**Final verdict: one complete independent pass over the fixed, re-rendered edition found ZERO problems. The edition is final.** (Not posted to Discord.)

## PATCH 2026-10-21 — P6 PRO-&-CONTRA box occluded 4 article lines (occlusion audit defect #2)

**Defect.** On P6, the PRO-&-CONTRA box (fill #f1ead6, rect (65,1000)–(961,1252)) was painted after the article flow and covered the last two lines of article columns 1 and 2 (93–100% glyph coverage, per the programme-wide geometric audit `hidden_files/occlusion-audit-2026-10-21.md`, defect #2): col 1 „Sommerzeit wieder ein; seitdem" / „gilt sie ohne Unterbrechung." and col 2 „einig — und so blieb alles, wie es" / „ist. Die Länder konnten sich nicht". In the render both columns simply stopped mid-sentence at the box top („…führten beide deutsche Staaten die" / „…Mitgliedstaaten wurden sich nicht"); the continuation existed only in the SVG text stream. The defect was inherited verbatim from the German core (the core is patched separately; this entry covers only the DE × EN edition).

**Root cause.** The P6 article flow (`content56.py`, `Flow` over cols 0–2, start y=200) has a bottom limit of 1080, so columns 1–2 legitimately run to baselines 1065/1058. The box was hard-placed at y=1000 — inside the flow's region — on the assumption the article had ended; only column 3 (gloss box) actually ends above 1000. Paint order did the rest: the box rect is emitted after the article text and is opaque.

**Why the independent proofread missed it.** The proofread above viewed all 8 cards in both passes and re-derived the keys — but visually the columns end mid-sentence in a way that reads as a column break, and the hidden strings are present in the extracted text, so text-stream checks (registry diff, fragment diff, phrase counts) all passed. Only a paint-order geometry check (glyph boxes vs. later opaque rects) exposes this class; it is now part of the programme's audit.

**Fix (geometry only, `hidden_files/weekly-report-de-en-build/content56.py`).** The whole PRO-&-CONTRA block was shifted down +85: rect y 1000→1085 (box now 1085–1337), title baseline 1042→1127, column heads 1090→1175, item flows start 1112→1197. Clearances: deepest article glyph bottom 1072.6 → 12.4 units above the box top; box bottom 1337 → 71 units above the practice-chart rule (y=1408). The box keeps its size, content, and role; nothing else on the page moved. **No text content changed** (German or English).

**Diff scope.** Only `svg/p6-vertiefung.svg` differs from the previously shipped files (the other 7 SVGs are byte-identical — a pre-patch rebuild from unmodified sources first reproduced all 8 shipped SVGs byte-identically). Within P6, only the box rect and its 13 text nodes changed y-coordinates.

**Verification.**
- Exercise registry dumped before and after the patch: **150 entries, byte-identical** (numbers, pages, levels, keys, notes).
- Visible-text extraction of all 8 pages before/after: identical string sequences on every page.
- Rebuild log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings.
- Full occlusion/footer/edge sweep re-run on the re-rendered SVGs (audit method: production-font glyph boxes, paint-order coverage ≥30%, footer band y>2580, page edges 1950×2700): **zero flags on all 8 pages**. The sweep was instrument-validated against the pre-fix geometry, where it reproduces the audit's exact 4 flags (100/100/93/100%).
- All 8 re-rendered cards viewed; P6 checked closely (both article sentences now complete above the box; chart and exercises untouched).
- Re-rendered artifacts: print PDF `Die-Lucerna-VOL1-EN.pdf` 10,478,519 B; web PDF `Die-Lucerna-VOL1-EN-web.pdf` 4,023,605 B (< 10 MB).
