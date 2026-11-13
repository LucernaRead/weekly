# FIX-LOG — es-it fix1: E1 (28 straight → curly Italian apostrophes)

**Defect (proof2 (b), sole item):** all 28 Italian elision apostrophes were straight U+0027; curly U+2019 was 0 — in text.md (28/0), in the 8 SVGs (28/0), and in the print/web text layers (28/0). Core es untouched.

**Method:** line-targeted replacement in the 5 content sources only (each listed line verified before the edit: exact straight count, inside a double-quoted string literal, no code quotes on the line; `content8.py:133/135` code quotes `e_['n']` etc. explicitly excluded and untouched). `python -m py_compile` on all 8 edition sources after the edit: OK. Rebuild: `run.py` rc=0, `render.py` rc=0, text.md re-exported from the new SVGs. No commit, no push.

**Result:** text.md straight 0 / curly 28; SVG straight 0 / curly 28; print text layer straight 0 / curly 28; web text layer straight 0 / curly 28. New three-piece: print `5af794cbd0454944099ba311597bade7d8eff0b2ede08ee0ba1c14bccd8bcb53` / 3,522,764 B; web `eb0b2635dfdd46d8d6bc6a392365c59f2582f906958bd2c6b3dbf12ba7694da1` / 883,013 B; text.md `81f41695cf1aef7e93152aed8c81f958fa43e57c7faada7bfe76284eb9f4f444` / 45,232 B, 1,806 lines. Gates: run rc=0 TOTAL 150, 0 OVERFLOW/TOO WIDE; occlusion 0; p8 extract 150/150; p8 compare CLEAN (keydiff [137, 138] adjudicated); freeze 8/8; freeze-diff CJK +6 (same as refanout); creambox 0 own-ink overflow (6 known below-box negatives, identical to refanout); creambox_diag 0 negative ink-clearances; boxtitle 0 overflow (min clear +14.4); keycheck 149/150 (only #150 ✓ exception); pdftotext print = web bytes (108,653 B); P8 min font 10.125pt (≥ 9.75pt floor); sweep 0 orphans / 0 box-vs-hline / 0 bridge widows; SVG-wide orphan-punctuation sweep 0; text.md punctuation-only lines 0. 150 exercises hand-verified via text.md (word sequence identical to the proofread pre-fix text except the 28 apostrophes + one re-wrap, see below); 8 pages viewed.

**Layout changes from the wider glyph (both expected, no overflow):** (1) P1 masthead pairing line is middle-anchored: start x 657.5 → 650.9, still centred, same y. (2) P3 Nota gloss re-wrapped within the same 2 lines at the same coordinates: old line 1 ended `l'anima`, line 2 `del flamenco.`; new line 1 ends `=`, line 2 `l’anima del flamenco.` — same words, same order, same box. All other SVG elements byte-identical after apostrophe normalisation (element-wise diff vs the refanout freeze build-copy, verified 8/8 byte-identical to the pre-fix SVGs).

**Rendering observation (from the 8-page visual check, new in fix1 — not a gate failure):** U+2019 in Noto Sans CJK SC (the sans font of all Italian explanation text) has a FULL-WIDTH advance: 1000/1000 em, vs straight ' 278/1000 em and space 224/1000 em (measured with fontTools on the system NotoSansCJK-Regular.ttc, SC face). So the 12 curly apostrophes in sans text render with a full-em gap after them — `l’ anima`, `Leggi l’ articolo`, `L’ EDIZIONE` — as if a space followed the apostrophe. The 15 curly apostrophes in Newsreader (P8 answer keys) render proportionally (’ 0.256 em vs ' 0.216 em) and look tight/normal. No shipped W47 edition renders a curly apostrophe in this sans font today (es-fr 56 straight / 0 curly; es-en 8 straight / 0 curly), so es-it is the first. A font-level fix (e.g. a proportional Latin sans for the explanation layer) is out of scope for this E1 fix and needs a coordinator decision; the character change itself is complete and all gates are green.

## The 28 changes (one per line; content8.py:93 carries two)

### 1. `content12.py:21` — L’EDIZIONE

- BEFORE: `p.text(975, 614, "TESTI IN SPAGNOLO　SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI", 16, "sans", False, GREY, anchor="middle")`
- AFTER: `p.text(975, 614, "TESTI IN SPAGNOLO　SPIEGAZIONI IN ITALIANO — L’EDIZIONE PER I LETTORI ITALIANI", 16, "sans", False, GREY, anchor="middle")`

### 2. `content12.py:275` — l’articolo

- BEFORE: `e.bridge("Leggi l'articolo e scegli la risposta giusta.")`
- AFTER: `e.bridge("Leggi l’articolo e scegli la risposta giusta.")`

### 3. `content34.py:22` — l’anima

- BEFORE: `f.gloss("el cante = il canto · el toque = la chitarra · el baile = la danza · el compás = il ritmo · el duende = l'anima del flamenco.")`
- AFTER: `f.gloss("el cante = il canto · el toque = la chitarra · el baile = la danza · el compás = il ritmo · el duende = l’anima del flamenco.")`

### 4. `content34.py:61` — l’articolo

- BEFORE: `e.bridge("Leggi l'articolo di pagina 3: vero o falso?")`
- AFTER: `e.bridge("Leggi l’articolo di pagina 3: vero o falso?")`

### 5. `content34.py:87` — L’UNESCO

- BEFORE: `e.ex("A2", "Scelta multipla", "B", "L'UNESCO lo annunciò a Nairobi nel 2010",`
- AFTER: `e.ex("A2", "Scelta multipla", "B", "L’UNESCO lo annunciò a Nairobi nel 2010",`

### 6. `content34.py:93` — l’elezione

- BEFORE: `e.ex("B1", "Scelta multipla", "B", "Dopo il flamenco: l'elezione del 29 novembre",`
- AFTER: `e.ex("B1", "Scelta multipla", "B", "Dopo il flamenco: l’elezione del 29 novembre",`

### 7. `content34.py:168` — l’articolo

- BEFORE: `e.bridge("Leggi l'articolo di pagina 4 e scegli la risposta giusta.")`
- AFTER: `e.bridge("Leggi l’articolo di pagina 4 e scegli la risposta giusta.")`

### 8. `content56.py:29` — l’urna

- BEFORE: `f.gloss("el sobre = la busta · la papeleta = la scheda · el censo = il registro elettorale · el plazo = la scadenza · la urna = l'urna.")`
- AFTER: `f.gloss("el sobre = la busta · la papeleta = la scheda · el censo = il registro elettorale · el plazo = la scadenza · la urna = l’urna.")`

### 9. `content56.py:66` — l’articolo

- BEFORE: `e.bridge("Leggi l'articolo di pagina 5 e scegli la risposta giusta.")`
- AFTER: `e.bridge("Leggi l’articolo di pagina 5 e scegli la risposta giusta.")`

### 10. `content56.py:86` — d’identità

- BEFORE: `e.ex("B1", "Completare frasi", "identidad", "documento de identidad = documento d'identità",`
- AFTER: `e.ex("B1", "Completare frasi", "identidad", "documento de identidad = documento d’identità",`

### 11. `content56.py:107` — Quest’anno

- BEFORE: `e.ex("B1", "Vero o falso", "Verdadero", "Quest'anno si può votare con MiDNI",`
- AFTER: `e.ex("B1", "Vero o falso", "Verdadero", "Quest’anno si può votare con MiDNI",`

### 12. `content56.py:218` — d’errore

- BEFORE: `e.ex("B2", "Scelta multipla", "B", "Sondaggio: foto con margine d'errore, un giorno preciso",`
- AFTER: `e.ex("B2", "Scelta multipla", "B", "Sondaggio: foto con margine d’errore, un giorno preciso",`

### 13. `content56.py:237` — d’errore

- BEFORE: `e.ex("B2", "Completare frasi", "margen de error", "margen de error = margine d'errore",`
- AFTER: `e.ex("B2", "Completare frasi", "margen de error", "margen de error = margine d’errore",`

### 14. `content7.py:20` — L’ora

- BEFORE: `a.bridge("L'ora: es la una (singolare), son las dos (plurale); una partita inizia a las 21:00.")`
- AFTER: `a.bridge("L’ora: es la una (singolare), son las dos (plurale); una partita inizia a las 21:00.")`

### 15. `content7.py:21` — l’una

- BEFORE: `a.ex("A2", "Completare frasi", "Es", "Per l'una si usa il singolare Es",`
- AFTER: `a.ex("A2", "Completare frasi", "Es", "Per l’una si usa il singolare Es",`

### 16. `content7.py:27` — L’una

- BEFORE: `a.ex("A2", "Scelta multipla", "B", "L'una si dice Es la una",`
- AFTER: `a.ex("A2", "Scelta multipla", "B", "L’una si dice Es la una",`

### 17. `content7.py:52` — l’indicativo

- BEFORE: `c.bridge("es necesario que, para que, ojalá con il congiuntivo; creo que con l'indicativo.")`
- AFTER: `c.bridge("es necesario que, para que, ojalá con il congiuntivo; creo que con l’indicativo.")`

### 18. `content7.py:69` — L’una

- BEFORE: `    ("«Son la una en punto.»", "→ «Es la una.» Es singular.", "L'una è singolare: si usa es."),`
- AFTER: `    ("«Son la una en punto.»", "→ «Es la una.» Es singular.", "L’una è singolare: si usa es."),`

### 19. `content7.py:124` — d’errore

- BEFORE: `    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Un sondaggio è una foto con margine d'errore, scattata un giorno preciso.", "Página 6"),`
- AFTER: `    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "Un sondaggio è una foto con margine d’errore, scattata un giorno preciso.", "Página 6"),`

### 20. `content8.py:44` — l’app

- BEFORE: `f.ex("B1", "Scelta multipla", "C", "MiDNI è l'app ufficiale di identificazione",`
- AFTER: `f.ex("B1", "Scelta multipla", "C", "MiDNI è l’app ufficiale di identificazione",`

### 21. `content8.py:67` — all’inizio

- BEFORE: `f.ex("B1", "Formare frasi", "¿A qué hora empieza el debate?", "Parola interrogativa all'inizio",`
- AFTER: `f.ex("B1", "Formare frasi", "¿A qué hora empieza el debate?", "Parola interrogativa all’inizio",`

### 22. `content8.py:70` — l’originale

- BEFORE: `f.ex("A2", "Traduci", "Lunedì è la Giornata internazionale del flamenco.", "Cfr. l'originale.",`
- AFTER: `f.ex("A2", "Traduci", "Lunedì è la Giornata internazionale del flamenco.", "Cfr. l’originale.",`

### 23. `content8.py:72` — l’originale

- BEFORE: `f.ex("A2", "Traduci", "Sabato guardiamo il derby di Siviglia.", "Cfr. l'originale.",`
- AFTER: `f.ex("A2", "Traduci", "Sabato guardiamo il derby di Siviglia.", "Cfr. l’originale.",`

### 24. `content8.py:86` — d’errore

- BEFORE: `            ["sondeo=sondaggio c", "muestra=campione d", "margen de error=margine d'errore b", "junta electoral=commissione elettorale a"],`
- AFTER: `            ["sondeo=sondaggio c", "muestra=campione d", "margen de error=margine d’errore b", "junta electoral=commissione elettorale a"],`

### 25. `content8.py:91` — d’identità

- BEFORE: `f.ex("B1", "Cloze (scelta)", "A", "documento de identidad = carta d'identità",`
- AFTER: `f.ex("B1", "Cloze (scelta)", "A", "documento de identidad = carta d’identità",`

### 26. `content8.py:93` — Dov’è, l’urna

- BEFORE: `f.ex("B1", "Cloze (scelta)", "A", "¿dónde está la urna? Dov'è l'urna?",`
- AFTER: `f.ex("B1", "Cloze (scelta)", "A", "¿dónde está la urna? Dov’è l’urna?",`

### 27. `content8.py:100` — un’unica

- BEFORE: `f.bridge("Prova di scrittura (senza un'unica risposta giusta); testo modello (97 parole) qui sotto.")`
- AFTER: `f.bridge("Prova di scrittura (senza un’unica risposta giusta); testo modello (97 parole) qui sotto.")`

## Files changed

- `production/2026-w47/2026-w47-es-it/content12.py`, `content34.py`, `content56.py`, `content7.py`, `content8.py` (the 28 apostrophes only; `content8.py:133/135` untouched)
- Regenerated in place: `svg/*.svg` (8), `cards/*.png` (8), `La-Lucerna-VOL4-es-it.pdf`, `La-Lucerna-VOL4-es-it-web.pdf`, `2026-w47-es-it.text.md`, `WEEKLY-KIT.md` (§9 correction + §10 fix1 record)
- Core es (`production/2026-w47/core-es/`) unchanged: print `2723a283…` / 17,212,955 B, web `c2473211…` / 1,410,471 B, text `509c95fa…` — identical before and after.
- No other edition touched; nothing committed, nothing pushed.
