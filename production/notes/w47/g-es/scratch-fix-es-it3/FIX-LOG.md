# FIX-LOG — es-it fix2: whole-batch revert of fix1 (28 curly → straight Italian apostrophes)

**Defect (independent re-proof (b), sole finding):** fix1's 28 curly U+2019 apostrophes render with a full-em gap in Noto Sans CJK SC — the sans font of all Italian explanation text. fontTools (re-proof, system `NotoSansCJK-Regular.ttc`, SC face): U+2019 advance **1000/1000 em** vs straight `'` 278/1000 em and space 224/1000 em. 150 dpi renders: 12/12 sans spots visibly gapped (`L’ EDIZIONE`, `l’ anima`, …), pixel-measured word-internal max white gap P1 **24 px** (old straight 6 px), P3 **28 px** (old straight 10 px); web PDF the same 24/28 px. The 16 curly apostrophes in Newsreader (P8 answer keys) render tight (0.256 em). All other gates were green; C1/C2 already fixed.

**Method:** whole-batch revert of fix1 at the same 28 lines in the 5 content sources — every listed line re-verified before the edit (exact U+2019 count, inside a double-quoted string literal, no code quotes on the line; `content8.py:133/135` code quotes `e_['n']` etc. explicitly excluded and untouched). Whole-batch, not just the 12 sans spots: the rest of W47 is all-straight (es-fr 56 straight / 0 curly, es-en 8 straight / 0 curly), so reverting only 12 would leave es-it the only edition mixing both forms. `python -m py_compile` on all 8 edition sources after the edit: OK. Rebuild: `run.py` rc=0, `render.py` rc=0, text.md re-exported from the new SVGs. No commit, no push.

**Result:** text.md straight 28 / curly 0; SVG straight 28 / curly 0; print text layer straight 28 / curly 0; web text layer straight 28 / curly 0. New three-piece: print `12e7e0817b13bdd21576b820bd567b821fb69c679508189b1ef9ba973b442724` / 3,498,553 B — **byte-identical to the refanout print** (fix1's SHA-BEFORE); web `626e7588389b3c835eec0c8eebde974332ab27a90bca7a0dd2c5ffbdce19f6bd` / 882,084 B; text.md `434e8df8f0d64924b89efe561adcc9406e7b1442e801eee66c16ceeca7f06abe` / 45,176 B, 1,806 lines — **byte-identical to the refanout text.md**. SVGs 8/8 byte-identical to the refanout SVGs (freeze baseline + direct sha256 vs fix1's `svg-BEFORE.sha256`). Gates: run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; occlusion 0; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated); freeze 8/8; freeze-diff CJK +6 (same as refanout); creambox 0 own-ink overflow (6 known below-box negatives, identical to refanout); creambox_diag 0 negative ink-clearances, C1 retested +3.8 px; boxtitle 0 overflow (min clear +14.4); keycheck 149/150 (only #150 ✓ exception); pdftotext print = web bytes (108,723 B, same as refanout); P8 min font 10.125pt (≥ 9.75pt floor); sweep 0 orphans / 0 box-vs-hline / 0 bridge widows; SVG-wide orphan-punctuation sweep 0; text.md punctuation-only lines 0; C2 not recurring (`antes del jueves` 0, `hasta el jueves 19` 5); 150 exercises hand-verified (text.md byte-identical to the proofread refanout text; the only diff vs the fix1 text is the 28 apostrophes + one re-wrap; keys re-proven by keycheck + p8 compare; the two key-bearing changes, 146 `carta d'identità` and 147 `Dov'è l'urna?`, visually confirmed in the P8 control crop); 8 pages viewed.

**Web PDF SHA is not reproducible run-to-run (measured, not assumed):** two consecutive `webpdf.py` runs on the identical SVGs give different SHAs (882,086 vs 882,083 B; first byte difference inside a compressed font stream, `/Length 1976` vs `1975`; no CreationDate/ID in the file). The shipped web PDF is `render.py`'s output; do not re-render it afterwards — the SHA will change again with identical content.

**Layout changes from the narrower glyph (both expected, no overflow):** (1) P1 masthead pairing line is middle-anchored: start x 650.9 → 657.5 (back to the refanout value), still centred, same y. (2) P3 Nota gloss re-wrap reversed within the same 2 lines at the same coordinates: line 1 ends `l'anima`, line 2 `del flamenco.` — the exact reverse of fix1's re-wrap. All other SVG elements byte-identical after apostrophe normalisation (element-wise diff vs the fix1 SVGs).

**Rendering spot-check (150 dpi, re-proof coordinates where verifiable):** 13 print spots + 2 web spots. Word-internal max white gap (ink = luminance < 128, measured inside the apostrophe word's own span — the re-proof's `词内` number, boxes recovered by template-matching the re-proof crops against its own 150 dpi renders, then re-centred from PIL word measurement where the match was wrong). Results: all 12 sans spots curly 24–29 px → straight 6–7 px, every crop visually tight with no visible gap; Newsreader control (P8 `Dov'è l'urna?`) 3 px → 3 px, tight in both versions. P1 reproduces the re-proof numbers exactly (24 → 6); P3 28 → 6. Full table (`crop-check.json`):

- P1 L'EDIZIONE: gap curly 24 px → fix2 6 px — `crops/fix2-p1-LEDIZIONE.png`
- WEB P1 L'EDIZIONE: gap curly 24 px → fix2 6 px — `crops/fix2-web-p1-LEDIZIONE.png`
- P2 l'articolo bridge: gap curly 28 px → fix2 6 px — `crops/fix2-p2-larticolo.png`
- P3 l'anima: gap curly 28 px → fix2 6 px — `crops/fix2-p3-lanima.png`
- WEB P3 l'anima: gap curly 28 px → fix2 6 px — `crops/fix2-web-p3-lanima.png`
- P3 l'articolo bridge: gap curly 28 px → fix2 6 px — `crops/fix2-p3-larticolo-bridge.png`
- P4 l'articolo bridge: gap curly 28 px → fix2 6 px — `crops/fix2-p4-larticolo-bridge.png`
- P5 l'urna: gap curly 29 px → fix2 6 px — `crops/fix2-p5-lurna.png`
- P5 l'articolo bridge: gap curly 28 px → fix2 6 px — `crops/fix2-p5-larticolo-bridge.png`
- P7 L'ora: gap curly 28 px → fix2 6 px — `crops/fix2-p7-Lora.png`
- P7 L'una: gap curly 27 px → fix2 7 px — `crops/fix2-p7-Luna.png`
- P7 d'errore: gap curly 26 px → fix2 6 px — `crops/fix2-p7-derroire.png`
- P7 l'indicativo: gap curly 29 px → fix2 6 px — `crops/fix2-p7-lindicativo.png`
- P8 un'unica: gap curly 29 px → fix2 6 px — `crops/fix2-p8-ununica.png`
- P8 control Dove l'urna: gap curly 3 px → fix2 3 px — `crops/fix2-p8-Dove-lurna-newsreader.png`

Method notes (for the re-proof): the first template match (full-image NCC on 3x-LANCZOS-downscaled crops) gave low scores (0.2–0.8) and 4 wrong boxes (P7-Lora, P7-derroire, P8-control off-frame/wrong region, P3 straight word off-frame after the re-wrap). Those 4 were rebuilt deterministically from PIL word measurement using the same fonts svglib measures with (`NotoSansCJK-Regular.ttc` SC face idx 2, `Newsreader-Regular.ttf`), which also reproduces the re-proof P1 box exactly (word x0 1605.0 vs NCC box x 1551). The P1 band-max gap is 38 px in BOTH versions (a structural gap around the em dash in the masthead line, not the apostrophe) — hence the word-span metric above. Everything else (template boxes for the 9 verified spots) was kept. The earlier band-max numbers (P1 38/38, P7-derroire 21/21) were measurement artefacts of the wrong boxes/bands, superseded by the word-span numbers here.

**D5 (record only, not fixed):** font distribution unchanged — Newsreader 973, Noto Sans CJK SC 632, Noto Serif CJK SC 43, UnifrakturMaguntia 1. The gap was D5's Latin layer falling back to the CJK sans; D5 scope awaits the user's decision.

## The 28 changes (one per line; content8.py:93 carries two)

### 1. `content12.py:21` — L’EDIZIONE

- BEFORE: `p.text(975, 614, "TESTI IN SPAGNOLO　SPIEGAZIONI IN ITALIANO — L’EDIZIONE PER I LETTORI ITALIANI", 16, "sans", False, GREY, anchor="middle")`
- AFTER: `p.text(975, 614, "TESTI IN SPAGNOLO　SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", 16, "sans", False, GREY, anchor="middle")`

### 2. `content12.py:275` — l’articolo

- BEFORE: `e.bridge("Leggi l’articolo e scegli la risposta giusta.")`
- AFTER: `e.bridge("Leggi l'articolo e scegli la risposta giusta.")`

### 3. `content34.py:22` — l’anima

- BEFORE: `f.gloss("el cante = il canto · el toque = la chitarra · el baile = la danza · el compás = il ritmo · el duende = l’anima del flamenco.")`
- AFTER: `f.gloss("el cante = il canto · el toque = la chitarra · el baile = la danza · el compás = il ritmo · el duende = l'anima del flamenco.")`

### 4. `content34.py:61` — l’articolo

- BEFORE: `e.bridge("Leggi l’articolo di pagina 3: vero o falso?")`
- AFTER: `e.bridge("Leggi l'articolo di pagina 3: vero o falso?")`

### 5. `content34.py:87` — L’UNESCO

- BEFORE: `e.ex("A2", "Scelta multipla", "B", "L’UNESCO lo annunciò a Nairobi nel 2010",`
- AFTER: `e.ex("A2", "Scelta multipla", "B", "L'UNESCO lo annunciò a Nairobi nel 2010",`

### 6. `content34.py:93` — l’elezione

- BEFORE: `e.ex("B1", "Scelta multipla", "B", "Dopo il flamenco: l’elezione del 29 novembre",`
- AFTER: `e.ex("B1", "Scelta multipla", "B", "Dopo il flamenco: l'elezione del 29 novembre",`

### 7. `content34.py:168` — l’articolo

- BEFORE: `e.bridge("Leggi l’articolo di pagina 4 e scegli la risposta giusta.")`
- AFTER: `e.bridge("Leggi l'articolo di pagina 4 e scegli la risposta giusta.")`

### 8. `content56.py:29` — l’urna.

- BEFORE: `f.gloss("el sobre = la busta · la papeleta = la scheda · el censo = il registro elettorale · el plazo = la scadenza · la urna = l’urna.")`
- AFTER: `f.gloss("el sobre = la busta · la papeleta = la scheda · el censo = il registro elettorale · el plazo = la scadenza · la urna = l'urna.")`

### 9. `content56.py:66` — l’articolo

- BEFORE: `e.bridge("Leggi l’articolo di pagina 5 e scegli la risposta giusta.")`
- AFTER: `e.bridge("Leggi l'articolo di pagina 5 e scegli la risposta giusta.")`

### 10. `content56.py:86` — d’identità

- BEFORE: `e.ex("B1", "Completare frasi", "identidad", "documento de identidad = documento d’identità",`
- AFTER: `e.ex("B1", "Completare frasi", "identidad", "documento de identidad = documento d'identità",`

### 11. `content56.py:107` — Quest’anno

- BEFORE: `e.ex("B1", "Vero o falso", "Verdadero", "Quest’anno si può votare con MiDNI",`
- AFTER: `e.ex("B1", "Vero o falso", "Verdadero", "Quest'anno si può votare con MiDNI",`

### 12. `content56.py:218` — d’errore,

- BEFORE: `e.ex("B2", "Scelta multipla", "B", "Sondaggio: foto con margine d’errore, un giorno preciso",`
- AFTER: `e.ex("B2", "Scelta multipla", "B", "Sondaggio: foto con margine d'errore, un giorno preciso",`

### 13. `content56.py:237` — d’errore

- BEFORE: `e.ex("B2", "Completare frasi", "margen de error", "margen de error = margine d’errore",`
- AFTER: `e.ex("B2", "Completare frasi", "margen de error", "margen de error = margine d'errore",`

### 14. `content7.py:20` — L’ora

- BEFORE: `a.bridge("L’ora: es la una (singolare), son las dos (plurale); una partita inizia a las 21:00.")`
- AFTER: `a.bridge("L'ora: es la una (singolare), son las dos (plurale); una partita inizia a las 21:00.")`

### 15. `content7.py:21` — l’una

- BEFORE: `a.ex("A2", "Completare frasi", "Es", "Per l’una si usa il singolare Es",`
- AFTER: `a.ex("A2", "Completare frasi", "Es", "Per l'una si usa il singolare Es",`

### 16. `content7.py:27` — L’una

- BEFORE: `a.ex("A2", "Scelta multipla", "B", "L’una si dice Es la una",`
- AFTER: `a.ex("A2", "Scelta multipla", "B", "L'una si dice Es la una",`

### 17. `content7.py:52` — l’indicativo.

- BEFORE: `c.bridge("es necesario que, para que, ojalá con il congiuntivo; creo que con l’indicativo.")`
- AFTER: `c.bridge("es necesario que, para que, ojalá con il congiuntivo; creo que con l'indicativo.")`

### 18. `content7.py:69` — L’una

- BEFORE: `    ("«Son la una en punto.»", "→ «Es la una.» Es singular.", "L’una è singolare: si usa es."),`
- AFTER: `    ("«Son la una en punto.»", "→ «Es la una.» Es singular.", "L'una è singolare: si usa es."),`

### 19. `content7.py:124` — d’errore,

- BEFORE: `    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Un sondaggio è una foto con margine d’errore, scattata un giorno preciso.", "Página 6"),`
- AFTER: `    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Un sondaggio è una foto con margine d'errore, scattata un giorno preciso.", "Página 6"),`

### 20. `content8.py:44` — l’app

- BEFORE: `f.ex("B1", "Scelta multipla", "C", "MiDNI è l’app ufficiale di identificazione",`
- AFTER: `f.ex("B1", "Scelta multipla", "C", "MiDNI è l'app ufficiale di identificazione",`

### 21. `content8.py:67` — all’inizio

- BEFORE: `f.ex("B1", "Formare frasi", "¿A qué hora empieza el debate?", "Parola interrogativa all’inizio",`
- AFTER: `f.ex("B1", "Formare frasi", "¿A qué hora empieza el debate?", "Parola interrogativa all'inizio",`

### 22. `content8.py:70` — l’originale.

- BEFORE: `f.ex("A2", "Traduci", "Lunedì è la Giornata internazionale del flamenco.", "Cfr. l’originale.",`
- AFTER: `f.ex("A2", "Traduci", "Lunedì è la Giornata internazionale del flamenco.", "Cfr. l'originale.",`

### 23. `content8.py:72` — l’originale.

- BEFORE: `f.ex("A2", "Traduci", "Sabato guardiamo il derby di Siviglia.", "Cfr. l’originale.",`
- AFTER: `f.ex("A2", "Traduci", "Sabato guardiamo il derby di Siviglia.", "Cfr. l'originale.",`

### 24. `content8.py:86` — d’errore

- BEFORE: `            ["sondeo=sondaggio c", "muestra=campione d", "margen de error=margine d’errore b", "junta electoral=commissione elettorale a"],`
- AFTER: `            ["sondeo=sondaggio c", "muestra=campione d", "margen de error=margine d'errore b", "junta electoral=commissione elettorale a"],`

### 25. `content8.py:91` — d’identità

- BEFORE: `f.ex("B1", "Cloze (scelta)", "A", "documento de identidad = carta d’identità",`
- AFTER: `f.ex("B1", "Cloze (scelta)", "A", "documento de identidad = carta d'identità",`

### 26. `content8.py:93` — Dov’è (×2)

- BEFORE: `f.ex("B1", "Cloze (scelta)", "A", "¿dónde está la urna? Dov’è l’urna?",`
- AFTER: `f.ex("B1", "Cloze (scelta)", "A", "¿dónde está la urna? Dov'è l'urna?",`

### 27. `content8.py:100` — un’unica

- BEFORE: `f.bridge("Prova di scrittura (senza un’unica risposta giusta); testo modello (97 parole) qui sotto.")`
- AFTER: `f.bridge("Prova di scrittura (senza un'unica risposta giusta); testo modello (97 parole) qui sotto.")`

## Files changed

- `production/2026-w47/2026-w47-es-it/content12.py`, `content34.py`, `content56.py`, `content7.py`, `content8.py` (the 28 apostrophes only; `content8.py:133/135` untouched)
- Regenerated in place: `svg/*.svg` (8), `cards/*.png` (8), `La-Lucerna-VOL4-es-it.pdf`, `La-Lucerna-VOL4-es-it-web.pdf`, `2026-w47-es-it.text.md`, `WEEKLY-KIT.md` (§10 fix2 record)
- Core es (`production/2026-w47/core-es/`) unchanged: print `2723a283…` / 17,212,955 B, web `c2473211…` / 1,410,471 B, text `509c95fa…` — identical before and after.
- No other edition touched; nothing committed, nothing pushed.

## Scratch record

Workdir: `hidden_files/w47/scratch-fix-es-it3/` — `apply_fix2.py`, `fix2-records.txt`, `SHA-BEFORE.txt`, `SHA-AFTER.txt`, `before/` (pre-fix2 content/text.md/SVGs), `curly-before.txt`, `gates.py` + `it-*.log/json`, `crop_check2.py`/`crop-check.log` (superseded NCC run), `recrop.py`/`recrop.log` + `crop-check.json` (final numbers), `word-boxes.json`, `measure_words.py`, `orphan_svgdiff.py` + `svg-diff-report.txt`, `renders-fix2/` (150 dpi print + web P1/P3), `crops/` (`fix2-*.png` + `ref-*.png` curly references), `run-fix2.log`, `render-fix2.log`, `text-extract-fix2.log`, `FIX-LOG.md` (this file).
