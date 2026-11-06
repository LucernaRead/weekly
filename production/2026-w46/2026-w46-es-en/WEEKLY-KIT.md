# La Lucerna — SPANISH WEEKLY VOL.3 · ES × EN (W46)

**Pairing:** Spanish target text (frozen W46 core, `files/weekly-report-w46-es-core/`, VOL.3, week Mon 9 – Sun 15 Nov 2026) + explanation layer written natively in **English**, for English-speaking readers. **Status:** builder-complete. **Independent proofread: PENDING** (parent runs it; repo insert happens only after it passes — no final-edition claim is made here). No Discord post, no main-chat card/PDF dump, no cron was created; the core build dir and the W43/W45 edition dirs were never written.

## 1. Method & baseline proof

- Build dir: `hidden_files/weekly-report-w46-es-en-build/` — a copy of the W46 core build (`hidden_files/weekly-report-w46-es-build/`), made AFTER the core's post-build fix (P2 note "罢工前两天" → "罢工后两天", matching its key "dos días después de la huelga"; core re-rendered and re-gated before this copy).
- All OUT paths in the copy were repointed to `files/weekly-report-w46-es-en/`; the single-process driver `run.py` renders all 8 pages in one process (shared bslib4 registry).
- Only the explanation layer was rewritten, via the asserted-replacement tables `hidden_files/w46/t_en.py` + `t_en2.py` (engine `hidden_files/w46/engine.py`: longest-first literal replacement, every pair hit-counted, abort-on-miss). The one CJK line left in build code, `svglib.py` (a dead-code illustration comment), is never rendered; the rendered SVGs contain zero CJK characters (freeze diff: edition CJK = 0 on all 8 pages).
- Exercise type names translate 1:1 (W43 ES×EN precedent): Sentence completion 48 · Multiple choice 47 · Cloze choice 13 · Vocabulary matching 12 · Sentence transformation 10 · True or false 8 · Sentence building 7 · Translation 4 · Writing 1. Instr labels: Fill in / True or false / Build the sentence / Rewrite / Translate / Write / Match word to definition. The P8 type check is `== "Writing"`, paired with the type-name translation.
- P8 translation items re-aimed per the W45 ES×EN ruling: keys 137/138 are the English sentences (Spanish bodies frozen); bodies 139/140 are the English source sentences (Spanish keys frozen); notes translated. This is the ONLY key difference in `p8.py compare` (keydiff [137, 138], adjudicated).

## 2. Furniture (verbatim from the shipped W43 ES×EN edition, VOL.1→VOL.3 only; W46 topics substituted)

- Masthead: **La Lucerna**
- P1 badge (brick #a4553a, 19.5pt bold, subtitle slot y=372, replaces the core tagline line): `TEXT IN SPANISH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`
- P1 edition line (46pt): `SPANISH WEEKLY · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`
- P1 top strip: `CADA SEMANA EN ESPAÑOL · REAL SPANISH, EVERY WEEK`
- P1 band right lines: `THE CAMPAIGN STARTS FRI 13 · STRIKE WED 11` / `TOP STORY · SEE PAGES 2 AND 6`
- Section heads: `VIDA · Life`, `CULTURA · Culture`, `DEPORTE · Sport`, `JUVENTUD · Youth`, `A FONDO · In depth`, `LENGUA · Language focus`, `EJERCICIOS Y RESPUESTAS · Exercises and answers`
- Footers, all 8 pages: `La Lucerna · Spanish Weekly VOL.3 · Text in Spanish · Explanations in English` and `Page N of 8`.
- Gloss prefix: `Note | ` (bslib `gloss()`); the P1 headline explanation line uses the same `Note | ` prefix.
- P8 header: `RESPUESTAS · Answer key — arranged by page; just find the number` / right note `One short English note per item · ✓ marks the writing task`; separator stays Spanish, frozen from the core: `— PÁGINA N —`. Exercise-page right note: `Answers on page 8 · Levels are mixed — find your number`.

## 3. Layout fixups (wording/size only — frozen geometry untouched; all W43/W45 ES×EN precedents)

1. P6 exercises 19pt/gap 3 → **18.5pt/gap 2** (×18): the longer English notes overflowed the P6 exercise flow at 19pt.
2. P8 answer lines 13.5pt/1.16 → **13.2pt/1.12**, section separators 1.16 → 1.12: English notes overflowed the 2552 answer bottom at 13.5pt. Answer-generation code otherwise byte-identical — dash style `N. key — note` and the `N. ✓ note` writing form are unchanged.
3. P1 five-keys note shortened to the W43 verbatim `Five keys — no invented numbers.` (the longer English line ran past the page edge, ink to x=1996.75).
4. P1 word-of-week note: `“la huelga general”: all workers stop work for 24 hours.` (single line; clear of the y=1844 rule).
5. P5 plan-box title shortened to `EL PLAN DE LA SEMANA · The plan` (the longer title crossed its box border, ink to x=1085 vs border 961).
6. P7 errors-box title shortened to `ERRORES TÍPICOS · Mistakes` (the longer title crossed its box border, ink to x=1919.2 vs border 1885).
7. P7 column-3 notes trimmed to restore the core's preview geometry exactly (P7 col-3 ends 1789.58, identical to the core): error notes (`gente is singular: use a singular verb.` / `creo que states a fact: indicative, es.`), word note (`huelga general = general strike: everyone stops work for a day. Strike week; campaign starts Friday 13.`), disclosure note (3 facts kept, no `Write in!` tail: `Editor's note: no real letters, no best page-8 texts; an editor's example is printed and the promise carries to VOL.4.`). Without these trims the letters box spilled one line onto the quotes rule and the preview block sat on the footer rule (col-3 end 1900.62). Verified visually on the final P7 card.

## 4. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38. Build warnings: **0 FLOW OVERFLOW / 0 HEAD TOO WIDE** (final build). 8 pages, 1950×2700; 8 full-page PNGs at 1950×2700. Print PDF 4,602,057 B; web PDF 520,992 B (< 7 MB).

## 5. Verification (all machine checks, builder-run; independent proofread pending)

- `tools/freeze.py diff` (core vs edition): added CJK characters **0** on all 8 pages; edition CJK total 0 on all pages. Removed/added string sets are explanation-layer/furniture only; no Spanish token lost or added (see `hidden_files/w46/es-en-diff.json`).
- `tools/p8.py compare` (target es): **CLEAN**, 150 = 150, missing=[], extra=0, keydiff=[137, 138] (re-aimed translation items, §1).
- `tools/occlusion_audit.py`: **0 flags** (selftest passed; `hidden_files/w46/es-en-occlusion3.json`, final render).
- Same-baseline scan (`hidden_files/w46/checks.py`): 7 reports, all P1 contents-list `Pág. N + title` 4.0px gaps, no overlap — byte-identical pattern to the core's own scan.
- P6 chart element-check (`checks.py`, later-rect graze): **0 overlaps**; chart geometry frozen from the core (W46 bar layout; the W45 "Inmigración graze" defect does not exist in W46 geometry).
- Web PDF: `pdftotext` 46,063 B, byte-identical to the print PDF's text; < 7 MB.
- Golden sentences: 8, verbatim from this issue's own articles, each appearing exactly 2× across the 8 SVGs (article + P7), with English translations 8/8. Page tags `(Página N)` frozen Spanish, counts equal to the core's.
- Reader letters: no real letters fabricated. The P7 letter is the core's labelled editor's example (Spanish body frozen, incl. Ana/Shanghái; attribution parens changed to half-width per W45 EN precedent); Spanish disclosure frozen; English disclosure carries all facts (no real letters, no best page-8 texts, example printed, promise carries to VOL.4).
- The 12 Nov decree-vote date is NOT reintroduced anywhere (0 occurrences of "12 de noviembre" as a vote date; the 12 Nov Nations League fixture is a football date, not a decree vote). 8 Nov results are not invented: the core's "results unavailable at press time" statement is frozen.
- Images: byte-identical to the core (P3 chestnuts CC0, P1 line-art ballot-box illustration, P5 typographic INFAMIA plate; see build-dir `assets/CREDITS-VOL3.md`).
- `.text.md` exported from this edition's own SVG text layer via `hidden_files/w46/es_textmd.py` (never from PDF).

## 6. Deliverables (this dir)

| File | Spec |
| --- | --- |
| `La-Lucerna-VOL3-EN.pdf` | Print, 8 pages, 4,602,057 B |
| `La-Lucerna-VOL3-EN-web.pdf` | Web, 8 pages, 520,992 B, text layer verified |
| `cards/p1…p8-*.png` | 1950×2700 PNG cards ×8 |
| `svg/p1…p8-*.svg` | Source SVGs ×8 |
| `ABSTRACT.txt` | English one-line abstract |
| `2026-w46-es-en.text.md` | Full text export from SVG layer |
| `WEEKLY-KIT.md` | This file |

Rebuild note (2026-11-02): this edition was rebuilt from the fixed core build after the core letters-box height fix (core KIT §6.8: disclosure's last line previously escaped the box; box bottom now 1834, last line 1824, preview bottom 2572). All gates re-run clean on the final render.

Build/transform record: `hidden_files/w46/es-en-build.log`, `hidden_files/w46/t_en.py`, `hidden_files/w46/t_en2.py`, `hidden_files/w46/engine.py`, `hidden_files/w46/checks.py`.
