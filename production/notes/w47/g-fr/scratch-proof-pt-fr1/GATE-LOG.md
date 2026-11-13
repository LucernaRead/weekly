# GATE-LOG — 2026-W47 pt–fr proof1 (independent)

Proofreader: pt-fr1, 2026-11-11. All gates run by the proofreader; KIT numbers are not trusted, only re-run results below. All commands run with `TMPDIR=<scratch>/tmp` (system /tmp never used). Edition dir untouched (`git status` clean apart from the untracked edition dir itself).

## §0 Identity (disk is authoritative)

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`, rc=0 (probe OK)
- Scratch write probe: `hidden_files/w47/scratch-proof-pt-fr1/probe.txt` written and read back OK
- creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383` — matches task
- Print PDF `A-Lucerna-VOL4.pdf`: sha256 `fe02b4fbb3a5869c53657e1ef8abae2e2b6a6b6b9314f4f633c88483884cd7cd`, 12,934,799 bytes — matches task
- Web PDF `A-Lucerna-VOL4-web.pdf`: sha256 `96190bcacb57c5304d4356ab4c91aac75a270913abde2c6cc06624bfc024717e`, 1,104,302 bytes — matches task
- text.md `2026-w47-pt-fr.text.md`: sha256 `f3cb6a085b203dc421186ef64d77f5b51ebc9f70a4652d6f7b7b130b54ef0018`, 37,687 bytes — matches task

## §1 Mechanical gates (all re-run)

| Gate | Command / method | Result |
|---|---|---|
| Builder gates | `tools/venv/bin/python production/2026-w47/2026-w47-pt-fr/gates.py` | **16/16 PASS**, `FAILURES: none` (`gates.log`) |
| Occlusion audit | `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-pt-fr --json occlusion.json` | **0 flags**; self-test OK, all 6 planted classes fired (`occlusion.log`, `occlusion.json`) |
| creambox canonical | `tools/venv/bin/python <goals>/hidden_files/w47/tools/creambox.py production/2026-w47/2026-w47-pt-fr/svg/*.svg` | full scan done (`creambox.log`); see §2 |
| p8 extract | `tools/p8.py extract --p8 .../svg/p8-avaliacao.svg --total 150` | **150/150 noted** (`p8-extract.log`) |
| p8 compare | `tools/p8.py compare --core-p8 production/2026-w47/core-pt/svg/p8-avaliacao.svg --edition-p8 .../svg/p8-avaliacao.svg --total 150` | **CLEAN**, missing=[] extra_count=0 uncertain=[] **keydiff=[137, 138]** (`p8-compare.log`) |
| freeze baseline | `tools/freeze.py baseline --build production/2026-w47/2026-w47-pt-fr --core-svg .../svg --out freeze1 --json freeze1.json` | **8/8 SVGs byte-identical**, repointed: none (`freeze1.log`, `freeze1.json`) |
| freeze diff | `tools/freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg .../svg` | added CJK only **U+3000 ×9** (P1: 2, others: 1 each); per-page +26..+52 / −22..−48 strings, P8 +191/−753 (`freeze-diff.log`, `freeze-diff.json`) |
| Print/web text layers | PyMuPDF `get_text` on both PDFs, 8 pages each | both **46,525 bytes**, word-multiset diff **0** (0 only-print, 0 only-web) |
| P8 min font (real) | PyMuPDF spans, print PDF p.8 (and web p.8) | **min 9.75pt** (174 spans at 9.75pt; distinct sizes 9.75–34.5pt); web identical 9.75pt. = SOP §1.1 floor. KIT's "9.75pt" confirmed by measurement, not trusted |
| Curly quotes | scan of visible text in all 8 SVGs + text.md + ABSTRACT.txt | straight `"` **0**; `“”` balanced (P8 2 open / 2 close; text.md same); `'` straight apostrophes 52 in SVGs (all French elisions: `l'`, `d'`, `s'`, `n'`, `qu'`) + 22 in text.md; U+2019: 1 (P1 `L'ÉDITION`) — see §4 non-defects |
| P1 headline length | gates.py | 41 non-space chars ≤ 56 |
| Model text | programmatic word count on text.md | **88 words** (range 80–100) |
| Phrases of the week | count in text.md | each of the 8 phrases exactly **2×** |
| CJK | scan of text.md + all 8 SVG visible texts | non-U+3000 CJK **0** everywhere; U+3000 furniture separators only (13–20 per SVG) |

## §2 Creambox adjudication (`creambox.log`, `ink.log`, `ink.json`)

Canonical scan output, per box (inside-only last baseline + desc-clear with 0.30em allowance):

- Negative "last baseline in +45 window" entries (7×: P1 −37.0/−17.6, P2 −32.0, P3 −37.0/−15.6, P6 −0.8/−42.0) are all **below-window headings** (+15.6…+42.0px below the box bottom), i.e. false positives — inside-only clearances for those boxes are all positive.
- Tight inside-only lines (desc-clear < 0) — all adjudicated by true-ink PIL measurement (`measure_ink.py`, reuses `occlusion_audit.ink_box`, 4× supersampled real fonts) + pixel strip scans on the rendered cards:
  - P2 E VOCÊ box (1439.5, 545, 364): last line `Écrivez deux phrases et envoyez-les.`, baseline 904.0, desc-clear −1.0 → true ink bottom **908**, box bottom 909 (1px clear); strip y 909–915: 0 dark px.
  - P3 E VOCÊ box (1439.5, 551, 303): same line, desc-clear −0.9 → strip below 854: 0 dark px.
  - P4 E VOCÊ box (1439.5, 602, 303): last line `envoyez-les.`, desc-clear −0.9 → strip below 905: 0 dark px.
  - P5 numbers box (1439.5, 200, 313): last line `2027.`, desc-clear −1.1 (no descenders in `2027.` — allowance artefact) → strip below 513: 0 dark px.
  - P5 E VOCÊ box (1439.5, 539, 272.5): same line, desc-clear −0.9 → strip below 811.5: 0 dark px.
  - P7 word box (1439.5, 1157.5, 274): last line `mémoire de la lutte et de la culture.`, baseline 1427.0, clearance +4.5, desc-clear −1.5 → true ink bottom **1426**, box bottom 1431.5 (5.5px clear); strip below 1431.5: 0 dark px; crop `crops/p7-wordbox-bottom.png` visually clean.
  - **P7-TOOLBOX summary: 3 boxes, min inside clearance +4.5, min desc-clear −1.5** (allowance artefact only; true ink clear everywhere).
- **`box_bottom: 0`** across all 8 pages (no text ink crosses any cream-box bottom by true ink).
- CORRECTION NOTE: an early pixel scan of "ink below box bottom" used wrong x-ranges (assumed all P2/P5 boxes share x≈538.5; the E VOCÊ boxes are in fact at x=1439.5). Its hits (P2 294px, P4 689px, P5 819px) were the neighbouring gloss box's own next lines, not spill. Redone with correct per-box rects (listed in the scan): all strips 0 dark px. The ink-box result was authoritative throughout.
- `box_right: 3` — all three are defects D1/D2/D3 (PROOF-NOTE). `box_left: 0`. `right_edge` (past 1950): 0. `left_margin` hits (11×) are 0.2px glyph-bearing noise, except the P1 kicker left overshoot (D4, 4.3px, confirmed by pixels).

## §3 Keycheck

- `keycheck-150.json`: **150/150 OK**, each with key + verification basis (question stem + source passage + printed P8 answer + text.md Respostas).
- Mechanical cross-check printed P8 answers (SVG) vs text.md Respostas: 150/150 match. Two parse artefacts resolved by inspection, not defects:
  - Q140: printed line ends `…gabarito oficial. —` (em-dash note separator; splitter only knew en-dash) — key identical.
  - Q150: printed as split nodes `150.` + `✓` + `Voir le texte modèle dans la section H de cette page (88 mots)` on one baseline — key identical to text.md.
- p8 keydiff [137, 138] adjudicated: 137 `Le vendredi 20 novembre est un jour férié national.` and 138 `Palmeiras a gagné 5–4 aux tirs au but.` are correct French renderings of the Portuguese answers; core's duplicate bare `138.` token is absent in fr (single `138.` — not a defect).

## §4 Judged non-defects (checked, not defects)

- Straight apostrophes `'` in French glosses (52×): systematic across W47 (pt-en 8×, pt-de 2×, pt-es 2× straight apostrophes in their glosses); no SOP rule mandates U+2019 in body text. Recorded as O1, not a defect.
- `L' ÉDITION` visible gap in P1 subtitle: KIT-noted Newsreader rendering quirk; source is `L'ÉDITION` (U+2019, no space). Mechanism-level, pre-existing.
- P3/P5 `Complétez avec les mots de l'encadré.` intro at bottom of col. 1 with word list at top of col. 2; P4 `B AS PALAVRAS` header orphan at bottom of col. 1: core flow behaviour, identical in core-pt. Not defects.
- Large mid-page white gaps (P2 cols 2–4, P3 col 3, P5 cols 2–3, P6 col 2): articles end above the fixed exercise band; core layout.
- `Mots-clés｜` and `·` separators in gloss lists: established house style, core-identical; SOP §1.1's full-width-space rule covers masthead/kicker/footer separators.
- P7 phrase-1 French `Jour de la Conscience noire : jour férié national un vendredi.` — telegraphic gloss word order, meaning clear (O2).
- P7 A2 `cair signifie « tomber un jour »`; P7 B1 `attention à l'accent au passé d'abrir, garantir et sair` — compressed glosses, meaning clear (O2).
- P6 `27–30 novembre` range for the 10th working day: correct per Edital §15.1 (27 if the 20 Nov holiday counts as a working day, 30 if not); external sources agree.
- Q125 round 36: round 35 = midweek 18/19 Nov fixtures; Sat 21 Palmeiras × Flamengo is round 36; external fixture note (Cruzeiro × Palmeiras 18 Nov, 20h30, 35ª rodada) corroborates.
- P8 header `Une courte note par réponse ✓ marque le texte modèle`: ink right edge exactly 1862.0 = margin (0.0 over) — not a defect.
- Core duplicate bare `138.` token: fr has one — not a defect.

## §5 External fact sources (checked live 2026-11-11)

- Weekdays: `date -d` for 2026-11-07/08/14/15/16/17/18/19/20/21/22/23/27/30, 2026-12-06, 2027-01-01 — Sat/Sun/Sun/Mon/Tue/Wed/Thu/Fri/Sat/Sun/Mon/Fri/Mon/Sun/Fri. All match the issue.
- Copa do Brasil semi-finals (7–8 Nov 2026): Atlético-MG 1–1 Grêmio (Sat 7, Arena MRV; Renan Lodi, Carlos Vinícius; agg 3–1) and Vasco 2–1 Palmeiras (Sun 8, São Januário; pens 5–4; agg 2–2), final single match 6 Dec, Mané Garrincha, Brasília — estacaolivremt.com.br, infobotucatu.com, sportradar.com, sportbuzz.com.br, edmaisesporte.com.br.
- São Paulo GP (Sun 8 Nov): Norris win, Verstappen 2nd, Hadjar 3rd, Mercedes constructors' champions — relargada.com.br, race-trace.news, lance.com.br, gazetaesportiva.com.
- Enem 2026: 8 + 15 Nov (Sundays), day 1 redação/Linguagens/Humanas 13h30–19h, day 2 Natureza/Matemática 13h30–18h30, 90 questions each; Edital nº 64/2026 §15.1 "até o 10º dia útil após o 2º dia"; deadline 27–30 Nov depending on the 20 Nov holiday count; result mid-January 2027, Página do Participante; 5,051,345 inscrições — centerdrop.com, focaedu.com, aprovatotal.com.br, sisu.pro.br, vestibulares.estrategia.com, blogdovestibular.com.
- Consciência Negra / Zumbi: died 20 Nov 1695; Lei nº 12.519/2011 created the day (no holiday); Lei nº 14.759/2023 (21 Dec 2023) made it a national holiday; 20 Nov 2026 is a Friday — ocalendario.com.br, afrocultura.com.br, pt.wikipedia.org, cep.pr.gov.br, trf2.jus.br.
- Brasileirão round 35: Cruzeiro × Palmeiras Wed 18 Nov 20h30, Mineirão, 35ª rodada — sportsja.com.br (Gazeta Esportiva).
- Working-day arithmetic (own): 16–30 Nov = 15 days; weekends 21–22 + 28–29 (4) + holiday 20 (1) = 5 non-working; 10 working days; 10th working day = 30 Nov (27 Nov if the holiday counted).

## §6 Files produced (scratch)

- `PROOF-NOTE.md`, `GATE-LOG.md` (this file), `keycheck-150.json`
- Evidence: `gates.log`, `occlusion.log`, `occlusion.json`, `creambox.log`, `p8-extract.log`, `p8-compare.log`, `freeze1.log`, `freeze1.json`, `freeze-diff.log`, `freeze-diff.json`, `ink.log`, `ink.json`, `measure_ink.py`, `probe.txt`
- Visual crops: `crops/p1-numbers-title.png`, `crops/p2-paranao-title.png`, `crops/p7-erros-title.png`, `crops/p1-kicker.png`, `crops/p2-evoce-bottom.png`, `crops/p4-evoce-bottom.png`, `crops/p5-numbers-bottom.png`, `crops/p7-wordbox-bottom.png`
- No source files modified; no commit; no push.
