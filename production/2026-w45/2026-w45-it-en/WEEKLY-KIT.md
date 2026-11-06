# La Lucerna — Italian Weekly, VOL.2, week of 2–8 November 2026
## Italian × English edition (IT×EN) — BUILDER KIT (not a finalization notice)

**Pairing:** text in Italian · explanations in English — the edition for English-speaking readers.
**Base:** W45 IT core (`files/weekly-report-w45-it-core/`, VOL.2), frozen byte-for-byte for all Italian body text; only the explanation layer is translated into English.
**Counts (measured from the core, not copied from another language family):** 150 exercises; levels A2 47 / B1 70 / B2 33; page distribution P1 10, P2 18, P3 18, P4 18, P5 18, P6 18, P7 12, P8 38; model text 81 words.
**Topics:** the first cold snap of November; 2 November Commemoration of the Dead; Panettone World Cup final in Milan, 7–8 November 2026; Festa del Torrone in Cremona; Serie A matchday 11.
**Deliverables in this directory:** `svg/` ×8, `cards/` ×8, `La-Lucerna-VOL2-EN.pdf` (print), `La-Lucerna-VOL2-EN-web.pdf` (web), this KIT, `ABSTRACT.txt`.
**Build tree:** `hidden_files/weekly-report-w45-it-en-build/` — `transform.py` (single source of truth, including all fix rounds), per-round sha256 baselines, gate outputs, and the scripts `chartcheck.py`, `rightedge.py`, `rowcheck.py`, `dump_reg.py`.
**Status:** builder-complete. Independent proofread is still required before finalization; this KIT does not declare the edition finalized. The edition has not been posted to Discord, sent into the main chat, or pushed to any repo by this build.

## Per-page contents

- **P1 Prima (10):** top story "Arriva il primo freddo", pairing badge, settimana day-by-day, cifre box, parola box, IN BREVE, QUIZ LAMPO 7–10.
- **P2 Vita (18):** first cold / dressing / 2 November, NOTE box, LO SAPEVI, E TU, FRASE box, exercises 11–28 (Fill in, True/False-style comprehension, Match the pairs).
- **P3 Cultura (18):** Panettone final Milan, Torrone Cremona, Alba white truffle, NOTE box, IL WEEKEND DOLCE, E TU, exercises 29–46 (Fill in, Reorder, passato prossimo).
- **P4 Sport (18):** Serie A matchday 11 + European cups, fixture table, NOTE box, E TU, exercises 47–64 (comprehension, Match the pairs, comparatives, passato prossimo).
- **P5 Giovani (18):** after Lucca Comics, Forum Cultura Milan, Festival dei Popoli Florence, piano box, NOTE box, E TU, exercises 65–82 (comprehension, word box, futuro, True or false).
- **P6 Approfondimento (18):** how to read a forecast (probability, not certainty), practice chart (invented data, labelled), NOTE box, exercises 83–100 (chart reading, comprehension, congiuntivo, weather words).
- **P7 Lingua (12):** three level columns (A2 weather verbs, B1 passato prossimo, B2 congiuntivo), ERRORI TIPICI, LA PAROLA «l'assaggio», LETTERE DEI LETTORI, FRASI DELLA SETTIMANA (8 golden sentences), LA PROSSIMA SETTIMANA (VOL.3).
- **P8 Valutazione (38):** test sections A–H (113–150) + full answer key grouped by page, Italian separators "— PAGINA n —", model text in section H (81 words).

## Furniture (measured from the shipped W43 IT×EN SVGs, which govern over README #20 generalizations)

- Pairing badge, P1, centered x=975 y=574, sans 22 bold, BRICK #a4553a: "Text in Italian · Explanations in English — the edition for English-speaking readers".
- Footer: "La Lucerna · ITALIAN WEEKLY VOL.2 · TEXT IN ITALIAN · EXPLANATIONS IN ENGLISH"; page line "Page N of 8"; gloss prefix "NOTE · "; P8 separators stay Italian.
- P1 top strip: "OGNI SETTIMANA IN ITALIANO · THE ITALIAN ITALIANS ARE READING"; P1 subtitle: "THE ITALIAN WEEKLY · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A" (44 pt in this edition — see fix round 3).
- Section headers keep Italian first + English tail ("LA NOTIZIA · THE TOP STORY", "IN QUESTO NUMERO · CONTENTS", "E TU? · Over to you", "ESERCIZI · Page N exercises", "LA PAROLA · Word of the week", "ERRORI TIPICI · Common mistakes").
- P7 band sub: "Language focus · Tre livelli, tre strumenti · Three levels, three tools"; FRASI header: "FRASI DELLA SETTIMANA · PHRASES OF THE WEEK (verbatim from this issue)"; next-week band: "LA PROSSIMA SETTIMANA · NEXT WEEK (VOL.3)".
- P8 titles: "RISPOSTE · ANSWER KEY — grouped by page: find your exercise number"; right note "Each answer has a one-line note in English · ✓ = model-text task".
- P8 band sub: "Page 8 · La grande prova della settimana + tutte le risposte".
- Instruction words: Fill in / Reorder / True or false / Match the pairs / Translate into English / Translate into Italian / Write.
- Registry type names (never printed) stay in Chinese, exactly as in the W43 IT×EN precedent, keeping the registry byte-comparable with the core; the P8 writing type check therefore also stays.

## Method

- `transform.py` applies literal `rep()` replacements only; each `rep()` fails loudly if its old string is absent, so a typo can never silently skip a translation. Italian target text is never a replacement target. Every fix-round edit went into `transform.py`; content files were restored pristine from the core build before each re-render.
- Repointing: all five content files plus `render.py` change `weekly-report-w45-it-core` to `weekly-report-w45-it-en`; PDF names become `La-Lucerna-VOL2-EN.pdf` / `La-Lucerna-VOL2-EN-web.pdf`.
- Re-renders run through the single driver process: `run.py` then `render.py` under `tools/venv/bin/python` (system python3 has no cairosvg).
- Interpreters / libraries (both measured from the same venv, recorded separately as required): run.py — `tools/venv/bin/python`, Python 3.12.3, Pillow 13.0.0; render.py — `tools/venv/bin/python`, Python 3.12.3, Pillow 13.0.0.
- Registry dumps were made in scratch copies (`reg-core/`, `reg-en/`) because content modules carry absolute OUT paths and must never be executed inside a shipped build dir; both dumps printed "dumped 150".

## Measured gates (final round, round 4)

- **Core freeze:** `tools/freeze.py baseline` reproduced 8/8 core SVGs byte-identical before any editing; core SVGs re-hashed after the build and confirmed unchanged (baseline in `core-svg-baseline.txt`).
- **Explanation-layer purity:** edition SVG CJK count 0 on all 8 pages; `tools/freeze.py diff` added CJK 0 on every page; the banned term for the explanation layer appears in no deliverable (SVG, card, PDF, KIT, ABSTRACT all scanned).
- **P8:** `tools/p8.py compare` reads CLEAN 150=150, missing=[], extra_count=0, uncertain=[] (outputs `p8-core.txt`, `p8-ed.txt`). Keydiff list [6, 13, 14, 15, 16, 20, 38, 58, 71, 74, 77, 137, 138, 139] adjudicated item by item below. P8 notes are pure English; the printed-note set is equal (EXTRA_ONLY acceptable — no extra noted beyond the translated set).
- **Occlusion:** `tools/occlusion_audit.py` edition 0 flags (self-test OK), core 0 flags, NEW vs core 0 (outputs `occlusion4.json`, `occlusion-new4.json`).
- **Chart labels (P6):** baseline-anchored ink method (PIL getmetrics, anchor `ls`), worst chart-label coverage 0.0%, gate <30% — pass (`chartcheck.py`).
- **Right edge (all 8 pages):** ADVANCE method, 0 violations past the inner frame line (1910). Four margin-zone entries (1885, 1910] are byte-identical frozen Italian lines also present in the core (P1 parola lines, P2 match right line, P8 H body line) — inherited, not new (`rightedge.py`, output `rightedge-en.txt`).
- **Same-baseline collisions (all 8 pages):** 7 flags, byte-identical to the core's 7 — the sommario label/title pairs with a designed 4.0 px gap, no overlap — inherited, not new (`rowcheck.py`).
- **Gloss:** rendered `gloss()` strings split on `·` and counted item by item: core [6, 5, 4, 4, 5] total 24, EN identical [6, 5, 4, 4, 5] total 24 (rendered NOTE lines carry the "NOTE · " prefix; counting strips the prefix first).
- **P7 golden sentences:** all 8 occur exactly 2× in both core and EN when node texts are joined with spaces (a naive separator-free join falsely gives 1× because wrapped article lines split mid-phrase); all 8 quote nodes present verbatim on P7.
- **P7 word box (blocking gate):** Italian definition sentence kept verbatim — "« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone." — only the gloss localized: "assaggio = tasting. See page 3: free tasting at the Panettone final." Parola gloss verified verbatim in both core and EN. Errori notes compressed to one wrapped line each at 19.5 pt, holding the core's column-3 geometry exactly (P7 column 3 ends y=1673.0, exactly the core value, 13 px clear of the FRASI rule at y=1686).
- **Column-3 ends (final):** P2 1025.0, P3 1310.25, P4 904.0, P5 1343.75, P6 1096.5, P7 1673.0 — all within their limits.
- **Independent recount (from rendered SVGs, chips + printed numbers, not the registry):** 150 items, continuous 1–150, levels A2 47 / B1 70 / B2 33; per-page 10/18/18/18/18/18/12/38. Registry comparison agrees: meta diffs (page/level/type) NONE; key diffs only #137, #138, #139, #150; note diffs all 150 (translated).
- **Model text:** 81 words, matching the core.
- **Visual inspection:** all 8 cards viewed page by page (P1 badge/subtitle/gloss/rule, P2, P3 photo + credit, P4 fixture table, P5 photo + credit, P6 chart + caption, P7 column stack + FRASI, P8 key block ending y=2484 with footer clearance). No defects observed in the final round.
- **Overflow:** zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final render (`build-round4.log`).

## P8 keydiff adjudication (14 items)

- **11 paren-branch extraction artifacts, not real key changes** (the canonical tool was NOT modified; adjudication only): for #6 previsioni, #13 guanti, #14 crisantemi, #15 termosifoni, #16 fa, #20 resta, #38 mandorle, #58 più bella, #71 gratuiti, #74 castagne, #77 ci sarà, the printed key (text before " — ") is byte-identical on both sides. Cause: when a note contains parentheses (core full-width or English half-width), `p8.py`'s paren branch truncates the dash-style line — the same family as the tools README #13 dash-truncation lesson. Possible tool fix is a TODO for the main line.
- **3 genuine keydiffs, all legal E-section re-aims** (same item numbers as the W43 IT×EN ruling): #137 "On Monday the first cold arrives." / #138 "The public can taste for free." / #139 "Sunday evening: Fiorentina play Juventus." — each with instruction "Translate into English".
- **Not in keydiff, confirmed separately:** #140's printed key is identical Italian ("Ogni previsione deve essere chiara.") with the body re-aimed to "Every forecast must be clear. → ___" (instruction "Translate into Italian"); #150's key is "(open task — model text below)" with note "Model text in section H below (81 words)"; P8 writing bridge: "Writing task (no single right answer); the model text (81 words) follows."

## Readers' corner — interpretation flagged for the proofreader (not settled)

The Italian letter stays frozen verbatim including "(esempio della redazione)". The English note states all three disclosure facts plus an imperative invitation: "Editor's sample, not a real letter: no real letters yet, no best page-8 essay yet — both promised for VOL.3. Write to us!" This mirrors the W45 ES×EN precedent (frozen target-language disclosure + English note). No additional Italian disclosure sentence was added, because adding one would push column 3 past the FRASI rule at y=1686; the "Italian original + English equivalent" requirement is met by the frozen Italian label plus the Italian VOL.3 promise in the next-week band together with this English note. The proofreader is asked to adjudicate this interpretation explicitly.

## Fix-round record

- **Round 1 (initial):** 150 exercises, correct levels/pages, P7 column 3 ends 1673.0. Defect: P8 key flow FLOW OVERFLOW (2 items), pushing items 149–150 onto the footer rule. Pre-fix baselines: `baseline-round1.txt`.
- **Fix round 1 (wording only, no layout-parameter change):** 8 wrapped P8 key lines eliminated, each replacement verified to wrap to exactly 1 line at 13 pt serif in width 434 with the build's own wrap(): #3 note → "Forum Cultura and Panettone final: both in Milan"; #41 note → "assaggiare takes avere"; #44 and #134 note (same string, 2 occurrences) → "Subject + essere + place"; #56 note → "Sunday matches are later than Friday's: più tardi"; #58 note → "più + bella: Sunday evening is the finest" (parenthetical dropped); #138 note → "assaggiare gratis = taste free"; #139 key → "Sunday evening: Fiorentina play Juventus." (the longer "On Sunday evening, Fiorentina play Juventus." still wrapped to 2 lines). Round 2: zero overflow/wide warnings; P8 key flow ends y=2484 (bottom 2552); only P8 SVG/card/PDFs changed. Pre-fix baselines: `baseline-round2.txt`.
- **Fix round 2 (wording only):** occlusion edition 2 flags, both P1 and both NEW vs core: (a) LINEX — the row-B rule at y=1864 struck the second line ("mild autumn.") of the P1 parola gloss; (b) BOXTITLE — the settimana subtitle "This week's diary · Cosa succede, giorno per giorno" ran to ink right 1934.8, past the box border 1885.0. Fixes: subtitle → "This week · Cosa succede, giorno per giorno" (398.3 px, inside the 412 px slot); parola gloss → "'Il primo freddo': cold after a mild autumn." (402.1 px, verified 1 line; the quoted Italian phrase itself carries "first cold"). Round 3: zero overflow/wide warnings; only P1 SVG/card/PDFs changed. Pre-fix baselines: `baseline-round2-pre.txt` (copy of round-2 baselines) and `baseline-round3.txt`.
- **Fix round 3 (wording + one furniture size):** the right-edge scan (ADVANCE method) was first run with a relative path that globbed nothing — caught on review and re-run with absolute paths; the scan scripts were also fixed mid-build (anchor parsing: a lazy regex + optional group never captured text-anchor, so end/middle-anchored text was misjudged as start-anchored; frame rects excluded). True findings: (a) P1 masthead subtitle at 46 pt overprinted both inner frame lines (advance edges 57.1..1917.9; core subtitle fits) — fixed by reducing the subtitle to 44 pt in the EN build only, full text kept, edges now 73.1..1876.9; (b) match-set instruction "Match words to definitions" ran past the content edge in column 3 (P2 D: edge 1894.0) — fixed by adopting the W43 IT×EN string "Match the pairs" for all 3 match sets (P2 D, P4 B, P8 F). Round 4: zero overflow/wide warnings; only P1, P2, P4, P8 SVGs/cards and the PDFs changed. Pre-fix baselines: `baseline-round3-pre.txt`; final baselines: `baseline-round4.txt`.

## W43 deviation list (furniture matches W43 IT×EN except where noted)

1. VOL.1 → VOL.2 in the footer (required by the issue).
2. P1 masthead subtitle at 44 pt instead of 46 pt (fix round 3; full text kept; W43's shorter subtitle fit at 46 pt).
3. P1 subtitle topics, band-right text, and all article-driven furniture strings follow the W45 core content (same patterns, new week).
4. Readers'-corner English note states the three disclosure facts explicitly + "Write to us!" (see the flagged interpretation above); W43's note was a shorter sample-letter sentence.
5. P8 E-section re-aims #137–#140 and #150 note follow the W43 IT×EN ruling exactly (same item numbers).
6. FRASE box title ("LA FRASE PER RICORDARE · Remember", 450.7 px at 23 pt) uses tsize=19 (372.2 px) — the same W43 IT×EN precedent for an over-wide box title.
7. P8 key-note trims (fix round 1) and P1 settimana subtitle / parola gloss shortenings (fix round 2) are EN-build-only wording fits; no layout parameter was changed in rounds 1–2.
8. Everything else — badge, footer pattern, page line, gloss prefix, P8 separators, RISPOSTE titles, band-sub patterns, instruction words, image assets and credit lines, registry type names — matches W43 IT×EN.

## Reproduce

```
cd hidden_files/weekly-report-w45-it-en-build
cp ../weekly-report-w45-it-build/content{12,34,56,7,8}.py ../weekly-report-w45-it-build/bslib4.py ../weekly-report-w45-it-build/svglib.py ../weekly-report-w45-it-build/render.py .
rm -rf __pycache__
tools/venv/bin/python transform.py
tools/venv/bin/python run.py
tools/venv/bin/python render.py
```

## Final files (round 4)

- Print PDF `La-Lucerna-VOL2-EN.pdf`: 7,173,236 bytes, sha256 6103191a82e2de6b703d909ebe0f2c578fe7b98fa09fffc9c4ef08a3aa774eb3
- Web PDF `La-Lucerna-VOL2-EN-web.pdf`: 3,570,974 bytes, sha256 6f038cbd364fd44a66bcdb9de0181885bd7c180e73bc83dec00c2fe057432f37
