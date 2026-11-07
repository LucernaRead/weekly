# WEEKLY KIT — De Lucerna VOL.2, NL × DE (W45)

## 1. Spec

- **Issue week:** Monday 2 November – Sunday 8 November 2026 (same as the W45 NL core).
- **Pairing:** Dutch target text (frozen) × German explanation layer (fully localised).
- **Masthead:** De Lucerna (Dutch article De, per the core).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Lead topic (from the core, unchanged):** «Nederland in de Klimaatweek» — Klimaatweek (2–8 Nov), Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov).
- **Build tree:** `hidden_files/weekly-report-w45-nl-de-build/` (copy of the W45 NL core build, OUT repointed to this edition before any run; the core build directory was never imported or run in place, per tools/README #11).
- **Delivery:** this directory — `svg/` (8 SVGs), `cards/` (8 PNGs, 1950×2700), print PDF, web PDF, this KIT, `ABSTRACT.txt` (German, single line, no ASCII double quotes).
- **Status: builder-complete only.** NOT finalised — an independent proofread round is still required. Nothing was posted to Discord, nothing was sent to the main chat, no cron was created, weekly-git was not touched.

## 2. Core measured values (from the W45 NL core WEEKLY-KIT, re-verified in this build)

- **Exercises: 150 total.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- **By level: A2 47, B1 72, B2 31** (build registry output, identical to the core).
- **By type (German labels, counts identical to the core):** ergänzen 65, wählen 44, zuordnen 8, richtig/falsch 7, Sätze bilden 8, Lückentext 13, übersetzen 4, schreiben 1.
- **Model essay (P8 H, ex. 150): 87 words** (registry assertion, unchanged; Dutch text frozen).
- **Numbering continuous 1–150.**

## 3. Furniture — W43 NL × DE measured values (shipped SVG wins over generic tables)

Measured from `files/weekly-report-nl-de/svg/` (W43) and applied verbatim, with VOL.1 → VOL.2:

- **P1 pairing badge (INSERTED, not replacing the strapline):** x=975, y=568, 20pt, weight 700, fill #a4553a (BRICK), centred, text «NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER» (measured width 1025.4px, centred span 462–1487; band bottom 542, headline label baseline 606 — no contact). The Dutch strapline at y=372 («DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS», 19pt) is kept verbatim — unlike the W45 NL × EN build, which replaced it.
- **Footer (all 8 pages):** «De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.2 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH» (measured width 1140.8px at 20pt).
- **Page line (all 8 pages):** «Seite N von 8».
- **Gloss prefix (shipped W43 form):** «Hinweis · » — NOT the tables.json generic «HINWEIS · »; the shipped W43 NL × DE SVG reads «Hinweis · het ezelsbruggetje = …». Recorded here as a W43-measured override.
- **Bridge prefix (shipped W43 form):** «Erklärung · » (W43 P1: «Erklärung · de herfstvakantie = Herbstferien …»).
- **P1 top strip (W43 form):** «ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH» (measured 705.1px, centred span 622.5–1327.5; right-hand week line starts at 1419.8 — 92px clear).
- **P1 subtitle (label localised, topics frozen):** «NIEDERLÄNDISCH · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12» (measured 1644.0px < 1820px inner width — MUSEUMNACHT is kept; the W45 NL × EN build dropped it only because its longer WEEKBLAD label overflowed, which does not apply here).
- **P8 answer separators:** «— PAGINA N —» kept as in both shipped fan-outs (W43 NL × DE and W45 NL × EN); the tables.json DE separator «— SEITE N —» was NOT applied, because both shipped precedents keep the Dutch page reference in the answer apparatus.
- **P8 answer style:** dash style, as the NL core (keys «N. key — note»).

## 4. Gates — measured values (all builder-side; independent proofread still required)

### 4.1 Freeze (tools/freeze.py diff, core vs edition)

- **Baseline before transform: 8/8 byte-identical** — the unmodified copy of the core build re-rendered into this edition dir produced SHA-256-identical SVGs to the shipped core (recorded in `core-sha256-before.txt`); the core SVGs re-hash unchanged afterwards (8/8 OK at the end of the build).
- **Final diff:** per page added/removed strings — P1 +29/−28, P2 +43/−33, P3 +30/−27, P4 +29/−25, P5 +42/−34, P6 +37/−32, P7 +47/−45, P8 +181/−167. **Added CJK characters: 0 on every page; edition CJK total: 0.**
- **Removed-string audit:** every removed string contains Chinese except 8 wrapped-line fragments, each verified as a re-wrap of an intact sentence, not a loss: P5 «1. Kijk zondag om 20:00 uur op RTL» + «4 (am Sonntag …» (same Dutch sentence, break moved by the longer German parenthetical); P6 lone «）» (caption re-wrap); P7 «bomen。/thuis。/zij zette vast。/。» (bridge line tails; full bridges present, e.g. «opruimen = aufräumen: wij hebben / opgeruimd; vastzetten = befestigen: zij zette / vast.»); P8 «6. planten — veel mensen → planten» (note localised to «Plural, also planten», key «planten» unchanged) and «voorgelezen» (wrap fragment of «41. hebben voorgelezen — voorlezen Perfekt: hebben voorgelezen», present verbatim).

### 4.2 P8 printed-note set (tools/p8.py compare, BY NUMBER)

- **Core noted: 150/150. Edition noted: 150/150. Status: CLEAN, missing=[], extra_count=0, uncertain=[].**
- **keydiff=[7, 17, 70, 71, 76, 96, 137, 138, 148]**, adjudicated item by item:
  - **137, 138 — genuine re-aims (NL→reader direction, the only true key changes).** 137 key: «气候周持续七天。» → «Die Klimaatweek dauert sieben Tage.»; 138 key: «橙色预警意味着：做好准备。» → «Code Orange bedeutet: Bereite dich vor.» Notes likewise German. 139 and 140 are NOT in keydiff: their Dutch keys («Museumnacht duurt van 19:00 uur tot 02:00 uur.» / «Ik doe mee aan de Klimaatweek.») are byte-identical to the core; only their prompts were re-aimed to German (reader→NL direction).
  - **7, 17, 70, 71, 76, 96, 148 — p8.py paren-branch extraction artifacts, NOT key changes.** In each case the true printed key before « — » is byte-identical to the core (7: B; 17: wortelen; 70: eiland; 71: proef; 76: gaat winnen; 96: advies; 148: B); only the note was translated to German. The tool inflates its «key» candidate with the note text because the German note ends with an ASCII paren group — «(2.–8. November)», «(Plural)», «(het)», «(de)», «(nur eine Vermutung)», «(het)», «(Boden)» — while the Chinese note used full-width «（）», flipping the tool from its dash branch to its paren branch. Per the standing rule, a key candidate that is not a bare key (here: key + translated note) is not a real key difference; the bare keys match.

### 4.3 Geometric occlusion (tools/occlusion_audit.py, selftest OK each run)

- **Edition: 0 flags. Core: 0 flags. NEW vs core: 0.**
- **Same-baseline ink-collision scan (rowcheck.py, README #10): all 8 pages CLEAN.**
- **P6 chart-label coverage (README #12 GRAZE watch): worst bbox coverage 0.0%** — no chart label is covered by any later-drawn rect at all.
- **P1 word-of-week graze (adjudicated, audit-clean):** the German word para is 2 lines ending at baseline 1871.9, the same geometry as the shipped W45 NL × EN edition; the IN HET KORT box top (1874) sits below the glyph baseline with no struck glyph (visually verified on the P1 card crop: both lines fully legible, box edge below the text). The P1 row-B separator line (y=1853) likewise sits below the first line's descenders, as in the core.

### 4.4 Gloss counts (rendered gloss() strings split on ·, README #21)

- P2 box (content12): core 6 vs edition 6 — OK. P3 box: 5 vs 5 — OK. P4 box: 5 vs 5 — OK. P5 box: 5 vs 5 — OK. P6 box: 5 vs 5 — OK. No gloss string introduces an extra «·».

### 4.5 P7 golden sentences and phrases

- All 8 Dutch golden sentences appear **exactly 2×** in the edition (once in the source article, once on P7), verbatim, with the correct «(Pagina N)» label: P1 ×2, P2 ×1, P3 ×1, P4 ×1, P5 ×1, P6 ×2. Each was also verified present in its source page.
- **P7 word-box freeze (standing ruling):** the Dutch definition sentence ««meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.» is preserved verbatim; only the German gloss line below it was localised («meedoen = teilnehmen, dabei sein.»). All four PAS OP Dutch wrong/correction lines are verbatim. No definition sentence was translated into German. (No unfinalised edition was used as a precedent for any of this; the only precedents cited are shipped editions: W43 NL × DE and W45 NL × EN.)

### 4.6 Readers' corner (P7 BRIEVEN VAN LEZERS — no fabrication)

- The Dutch example letter is frozen verbatim («Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)); no reader, letter, name or quote was invented.
- **All three facts are on the page, in Dutch (frozen) and in German:** no real letters arrived; no best page-8 texts arrived; the printed item is an example with the promise carried to VOL.3. German disclosure verbatim: «Redaktionsschluss: keine echten Briefe, keine besten Seite-8-Texte — darum ein Beispiel; Versprechen für VOL.3.»
- **Explicit German invitation (imperative + print promise), verbatim:** «Beispiel der Redaktion, kein echter Brief. Schicke uns echte Briefe und beste Seite-8-Texte — wir drucken sie in VOL.3!» (Content-preview lines and other pages' exercise prompts are not counted as this invitation; this sentence is inside the BRIEVEN box itself.)
- **P7 column-3 bottom: 1896.5** (core: 1897.0); ZINNEN section headline rule at 1937 — 40.5px clear.

### 4.7 Other gates

- **Flow warnings in the final build: zero FLOW OVERFLOW, zero HEAD TOO WIDE** (final log `build-log-fix2.txt`; flow ends: P1-headline 1401/1828, P2-ex 2402/2580, P3-ex 2465/2580, P4-ex 2406/2580, P5-ex 2406/2580, P6-ex 1895/2580, P7 columns ≤1249/1560, P8-keys 2389/2540).
- **Images (all reused W43/W45-core assets, no new downloads):** P1 herfstbos — Foto: Vovogov90 — CC0; P2 kinderdijk — Foto: Nationaal Archief — CC0; P3 gracht — Foto: W. Punt / Anefo, Nationaal Archief — CC0; P4 elftal1912 — Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein. All four credit lines are present in the rendered SVGs (checks_de.py). Image payloads are byte-identical to the core build (same assets dir).
- **Banned strings in rendered SVG text:** «桥接» 0, «讲解» 0, «译注» 0, CJK characters 0 on all 8 pages, ASCII double quotes in SVG texts 0.
- **P6 chart:** values 45/25/20/10 (total 100) unchanged; chart labelled ÜBUNGSDATEN in the title and in the German caption («ÜBUNGSDATEN: erfundene Zahlen, nur zum Üben, keine echte Umfrage. …»); the Dutch OEFENDATA caption line is kept verbatim.
- **Footers:** 8/8 carry VOL.2 (see §3); no page footer reads VOL.1.

## 5. Toolchain

- **run.py and render.py both ran under `tools/venv/bin/python`: Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1.** (System python3 is also 3.12.3 but ships Pillow 10.2.0 and no cairosvg, so it was not used; render.py requires the venv per the task.)
- **Baseline reproduction:** the unmodified core build copy rendered 8/8 byte-identical SVGs under this toolchain (see §4.1), so the toolchain reproduces the family baseline.
- **Single-process rule (README #7):** every render went through the build's single driver `run.py` (content12 → 34 → 56 → 7 → 8 in one process); no content module was ever imported or run standalone, and nothing was imported inside the core build directory (README #11).
- **Line-based splicing only (README #17):** the fan-out transform (`transform_de.py`, plus the fix1/fix2 edit scripts logged in the build dir) replaces whole lines or exact unique literals with an assertion per replacement; no AST byte-offset splicing was used.

## 6. Fix records

### Fix 1 (first-build overflows: P1-headline +490px cascade, P2-ex match_set 39px over, P7 col3 2101, P8-keys clamped)

Pre-fix SVG hashes recorded in `fix1-baseline-sha256.txt` before editing.

- **P1:** bridge shortened to 3 lines («Erklärung · Klimaatweek = Klimawoche · boom planten = Baum pflanzen · besparen = sparen · waarschuwing = Warnung.») and cijfers parentheticals shortened («(Tage der Klimaatweek)», «(Bäume und Sträucher, Samstag)», «(Museen, über 70)», «(12. Spieltag)») — box total 424 → 343px, restoring the core's column-break geometry; headline flow now ends 1401 (core 1452).
- **P2-ex:** exercise-section heads gap 13 → 8 (4 heads) and P2 exercise gaps 8 → 4 (14 items), mirroring the W45 NL × EN fix1 recipe; P2-ex now ends 2402 (was clamped at 3032).
- **P7 col3:** clinic notes made telegraphic following the NL × EN fix1 precedent (Dutch correction lines carry the full meaning): «Langzeitwetter, nicht Wetter heute.», «Klimaatweek ist ein Name, also groß.», «Hauptsatz-Verb an zweiter Stelle: blijf ik.»; word gloss shortened to «meedoen = teilnehmen, dabei sein.»; disclosure and invitation shortened to their final forms in §4.6. Col3 ends 2101 → 1896.5.
- **P8-keys:** font tightening following the NL × EN fix1 / W43 DE family precedent: keys 13.5pt/lh 1.16/gap 0.5 → 13.0pt/lh 1.14/gap 0.3; separators 14pt/lh 1.16/gap 2 → 13.5pt/lh 1.17/gap 1.5; flow bottom 2552 → 2540. Keys now end 2389 (was clamped at 2582). Key/note texts unchanged.

### Fix 2 (first audit: 4 NEW flags)

Pre-fix SVG/card/PDF hashes recorded in `fix2-baseline-sha256.txt` before editing.

- **P1 COVER** (word-of-week 3rd line «von unserem Klima.» fully covered by the IN HET KORT box): German para shortened to 2 lines (««Klima»: Wetter und Natur über lange Zeit. Die Klimaatweek handelt davon.») — same baselines as the shipped NL × EN geometry; audit now 0, crop verified.
- **P2 EDGE** (match_set instruction «Wörter und Bedeutungen zuordnen», 320.4px from x=1647 → ink to 1967.5, past the 1950 page edge): shortened in both content12 and content8 to «Wort und Bedeutung zuordnen» (279.9px → ends 1926.9, 23px inside the page).
- **P6 BOXTITLE** («VOOR OF TEGEN? · DAFÜR ODER DAGEGEN?», ink right 1930.2 > box border 1885): retitled «VOOR OF TEGEN? · PRO UND KONTRA» (395.4px → ink right 1868.4, inside the border; crop verified).
- **P7 TEXTX** (golden row 0 German + «(Pagina 1)» wrapped, leaving a dangling «1)» 14px above the next quote): row-0 German shortened to «Vom 2. bis 8. November ist in den Niederlanden Klimaatweek.» (650.2px < 896px column width, single line); all 8 golden rows now single-line, crop verified.

## 7. Delivery values

| File | Bytes | SHA-256 |
|---|---|---|
| De-Lucerna-VOL2-DE.pdf (print, 8 pages) | 7,918,211 | 4708ee95814b843a163ef6d3433783276068e8a824584a1e1155b5e0ff71c870 |
| De-Lucerna-VOL2-DE-web.pdf (web, 8 pages, < 10 MB) | 3,691,075 | c2fed9ab18fdaf2f279231818f103329c295a9cccb87e5a7f40af457d7c5433d |
| svg/p1-voorpagina.svg | — | 05be7af291a930221571e4d4f1ea42ea5644e6ea16c51fa86e38524951ec392b |
| svg/p2-leven.svg | — | fff90fb788a35d348f673726654517f4498964629dc125ab3e92a200f8d32422 |
| svg/p3-cultuur.svg | — | 6ceae6143952e665d4b266e726a36092dd51c1d73c24cb381599cb5ed29cbebd |
| svg/p4-sport.svg | — | 16d9c61f37960b0c5fed9881116421fed28dba7b045ba936523dbf3301bfccb0 |
| svg/p5-jongeren.svg | — | 3437359ae01fc36aed803fcdf4b025fd4211350700724a5d87b79d8f34f9edac |
| svg/p6-verdieping.svg | — | 4a2ec65546e6c31ae800649d1d5e955f78040f3106ed7146f88c26d873226bdc |
| svg/p7-taal.svg | — | 5a7dd7cbfda6604ff8c6eea80d98e7e43b44c60ab81835bd348cb57d093d5378 |
| svg/p8-toets.svg | — | 0e60f996f0271defb5a995ed31a10af5712d283632e1256f1100e45e66a69118 |

Cards: 8 PNGs, each 1950×2700 (SHA-256 in the build log / delivery listing; p1 79c5caf0…, p2 0150f99a…, p3 98923033…, p4 0ac33e42…, p5 73f3d82d…, p6 9ed3e208…, p7 18718f42…, p8 163ca877… — full values in the final build listing).

## 8. Reproduce

```
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-nl-de-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py    # SVGs -> edition svg/ dir
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py  # cards + PDFs
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-nl-de --core ../files/weekly-report-w45-nl-core
./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-nl-core --edition-dir ../files/weekly-report-w45-nl-de --target nl
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-nl-core/svg --edition-svg ../files/weekly-report-w45-nl-de/svg
```

Note for a from-scratch rerun: `transform_de.py` records the first transform; the fix1/fix2 edits listed in §6 are applied afterwards (they are also visible as the diff between the transform output and the final content files). The transform script itself is not idempotent on already-transformed sources (its specific replacements assert on the Chinese originals), which is the expected one-off behaviour.
