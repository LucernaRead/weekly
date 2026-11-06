# La Lucerna — HEBDOMADAIRE ITALIEN VOL.1 · IT × FR

**Pairing:** Italian target text (frozen W43 core, `files/weekly-report-it-vol1/`) + explanation layer written natively in **French**, for francophone readers.
**Status:** builder-complete. **Independent proofread: PENDING** (parent runs it; repo insert + Discord posting happen only after it passes — not done here).

## 1. Method & baseline proof

- Build dir: `hidden_files/weekly-report-it-fr-build/` — a copy of the core build (`weekly-report-it-build/`), taken from the CURRENT shipped core (incl. its post-audit geometry patches).
- **Baseline proven before any edit:** the unmodified copy reproduced all 8 shipped core SVGs byte-identically (sha256 matched all 8).
- Only the explanation layer was rewritten (asserted-replacement scripts, abort-on-mismatch, per content file). Italian target text is byte-identical to the core, with the documented exceptions in §3.
- Full SVG text-node diff vs core reviewed node by node: every removed string is a Chinese explanation/furniture string; every added string is its French counterpart (or a wrap-shifted line of one). All pure-Italian article/exercise text is present unchanged in both.
- CJK scan of all 8 final SVGs: **zero**.
- Banned intermediary term: absent from paper, this KIT, and all build code (the inherited code method was renamed `expl()`).
- Images: the 4 embedded payloads (P1 NIST-F1 atomic clock, P3 white truffles, P3 Artemisia *Giuditta*, P5 Chaplin) are byte-identical to the core; credit lines unchanged (Italian apparatus of the frozen core, verified string-identical per page).

## 2. Furniture (as rendered)

- Masthead: **La Lucerna**
- P1 badge (brick #a4553a, 20px bold, replaces the tagline line): `TEXTES EN ITALIEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES` (ink 996.8px ≤ 1820)
- P1 edition line (46px): the HEBDOMADAIRE variant measured 1853.3px > 1820 limit, so the measured JOURNAL variant is used (DE×FR precedent): `JOURNAL ITALIEN · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL CINEMA` (ink 1671.1px)
- P1 band right lines: `CE DIMANCHE, UNE HEURE DE SOMMEIL EN PLUS` / `La nuit du changement d'heure · voir page 2`
- Band subs: P2 `VITA · VIE QUOTIDIENNE`, P3 `CULTURA · CULTURE`, P4 `SPORT · SPORT`, P5 `GIOVANI · JEUNESSE`, P6 `APPROFONDIMENTO · EN PROFONDEUR`, P7 `LINGUA · LANGUE`, P8 `VALUTAZIONE E RISPOSTE · EXERCICES ET RÉPONSES` / `Page 8 · …`
- Footers, all 8 pages: `La Lucerna · HEBDOMADAIRE ITALIEN VOL.1 · TEXTE EN ITALIEN · EXPLICATIONS EN FRANÇAIS` and `Page N sur 8`
- Gloss prefix: `Note — `; keys header `RISPOSTE · CORRIGÉS — classés par page, cherchez le numéro`; answer-key typography: space before each note parenthesis, half-width parens only.
- Instruction labels: Compléter / Associer / Former une phrase / Vrai ou faux / Traduire / Écrire.

## 3. Registry verification & key-diff registry

- **150 exercises — A2 46 · B1 71 · B2 33; per page 10/18/18/18/18/18/12/38; page/level/type identical to core for all 150 (programmatic registry diff).**
- **Key changes — exactly 3, all documented fan-out exceptions:**
  - **#137** (Traduire, IT→reader language): key → **`Le dimanche, nous dormons une heure de plus.`** (note `traduction`)
  - **#138** (Traduire): key → **`L'exposition reste ouverte jusqu'en avril.`** (note `= reste ouverte`)
  - **#150** (Écrire, apparatus line): key → **`Question ouverte — texte modèle ci-dessous sur cette page`** (note `Texte modèle dans la section H de cette page (90 mots)`)
- Exercises #139/#140 are translation items in the reverse direction (reader language → Italian): their **stems** were re-aimed at French (`Samedi, 18:00 : Napoli–Roma. → ___`, `Chaque chiffre doit avoir une source. → ___`); their **Italian keys are byte-identical to the core**.
- All other 145 keys byte-identical to the core. Answer notes: all translated into French except #86 (`5 − 3,4 = 1,6`), which is language-neutral arithmetic and unchanged.
- Sample re-solve across all pages against the French keys: consistent with the articles (clock change 03:00→02:00; Napoli–Roma Sat 18:00; Inter–Fiorentina Sun 12:30 first match with ora solare; Manovra components 5,0 + 5,0 + 3,4 = 13,4 ≠ total ≈23,5 — the on-page honesty note is Italian core text, untouched; Lucca Oct 28–Nov 1; Ognissanti Sun Nov 1).

## 4. Weekday / date verification (real 2026 calendar, programmatic)

Every weekday claim in the Italian text checked with Python `datetime` — **all correct, no inherited weekday error**: Sat Oct 24 / Sun Oct 25 (clock change), Tue Oct 20, Wed Oct 21 (Artemisia opens), Thu Oct 22, Fri Oct 23, Wed Oct 28 (vote + Lucca opens), Sat Oct 10 (fiera opened), Sun Dec 6 (fiera closes), Sun Nov 1 (Ognissanti — also the P8 #128 key claim), Mon Oct 19, and Sun Mar 28 2027 = last Sunday of March 2027 (ora legale return). Nothing in the target text was changed.

## 5. P7 phrases

All 8 Italian quotes verified **verbatim** (normalized text join) in their tagged article page (1× each) and once in the P7 list — exactly 2 occurrences per quote across the issue, page tags correct: Pagina 1, 1, 2, 2, 3, 4, 5, 6. Glosses are the French translations.

## 6. Fit defects found in-build and fixed (French apparatus only; core geometry and Italian text untouched)

French-layer shortenings to restore the core's flow ends (all documented, wording stays natural French):

1. P1 box line 2 parenthetical `(dans la nuit de dimanche)` → `(nuit de dimanche)`.
2. P4 vocab gloss shortened to end `in trasferta = à l'extérieur.` (3 lines, as core).
3. P6 §A explanation → `Regardez les deux graphiques : choisissez.` (1 line).
4. P7 clinic French notes ×4 shortened (`Seule 1:00 prend è, les autres sono.` / `andare prend essere, pas avere.` / `a + il = al ; cf. del, nel, sul, dal.` / `gente est singulier (féminin).`).
5. P7 parola gloss → `anteprima = avant-première : la première projection d'un film. Page 5, au festival.`
6. P7 letter note → `Lettre d'exemple, écrite par la rédaction. Le VOL.2 publiera vos lettres et le meilleur texte page 8.`
7. 13 P8 key notes trimmed (#3, #7, #23, #40, #46, #51, #83, #90, #135, #136, #137, #139 + the #138 note) so the key flow ends at y=2502 ≤ 2552, all columns clear of the y=2580 footer rule.
8. **P1 word-of-week gloss — line strike (main audit catch, pixel-confirmed):** the 2-line French gloss's second line (baseline 1872) was struck by the full-width rule at y=1864 (the core's post-audit patch position, safe only for the core's 1-line gloss). Gloss shortened to one line: `« Mauvais temps » : pluie, vent, tempête : Adam.` Final audit: 0 flags; pixel re-check shows clear air above the IN BREVE box.
9. **Box titles (titles audit catch, all pixel-confirmed crossings):**
   - P1 `LA SETTIMANA IN CIFRE · LA SEMAINE EN CHIFFRES` crossed its box border → title `LA SETTIMANA IN CIFRE · EN CHIFFRES` at `tsize=20` (ES×FR short-form precedent). Pixel margin after fix: 24px.
   - P2 `LA FRASE PER RICORDARE · À RETENIR` crossed by ~28px at tsize 23 → `tsize=20`, string unchanged (ES×FR precedent). Pixel margin after fix: 26px.
   - P7 `ERRORI TIPICI · ERREURS FRÉQUENTES` crossed by ~45px → `ERRORI TIPICI · ERREURS TYPES` at 23 (ES×FR wording precedent). Pixel check after fix: ends well inside the box.

Final full build: **zero flow-overflow / head-too-wide warnings** on all 8 pages; all flow ends at or inside the core's ends except P8 keys (2502 vs core 2366, still ≤ 2552 region bottom).

## 7. Geometric occlusion audit (SOP gate)

Tooling: `audit_it_fr.py` (paint-order scan, production font metrics via svglib/PIL, ink band baseline −0.88em…+0.30em, **line boxes expanded by half the stroke width**), validated first on synthetic controls (COVER, LINEX and FOOTER positive controls all fired; a clean control passed). Companion scans: `audit_titles.py` (title ink vs its own box border), `audit_texttext.py`. The same main audit run on the shipped core SVGs as a control: 0 flags.

- Coverage/footer/edge/line scan: 1 flag found (the P1 gloss line strike, §6.8) → fixed → **final run 0 flags on all 8 pages**.
- Box-title scan: 3 crossings found (§6.9) → fixed → **final run 0 crossings**; tightest remaining title margin 7.1px (`IN QUESTO NUMERO · SOMMAIRE`, pixel-verified inside its box).
- Text–text scan: 1 flag — masthead wordmark `La Lucerna` vs the P1 edition line, the known display-size ink-band model artifact; visually confirmed on the card: clear separation. NON-DEFECT (core geometry, unchanged).
- All 8 final cards viewed visually: no occlusion, no overflow, no clipped text.

## 8. Deliverables (`files/weekly-report-it-fr/`)

- `svg/` ×8, `cards/` ×8 (1950×2700 PNG)
- Print PDF: `La-Lucerna-VOL1-FR.pdf` — **9,077,841 bytes**, sha256 `16021e33b1353a5d068ebcf03fc334ff4072450d4b351e16752d11d923edc91f`, 8 pages
- Web PDF: `La-Lucerna-VOL1-FR-web.pdf` — **3,635,776 bytes** (< 10 MB), sha256 `677c225c59179889ffba02a1bfb150f9f7e97ec82c189adbed272081128ce763`, 8 pages

## 9. Open gate

**Independent proofread has NOT run — marked PENDING.** No GitHub repo insert and no Discord post were made (parent handles both after the proofread passes).
