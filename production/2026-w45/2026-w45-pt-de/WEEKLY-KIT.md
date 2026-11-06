# A Lucerna — VOL.2 · Portugiesische Ausgabe für deutschsprachige Leser (PT × DE, W45)

**Pairing:** Brazilian Portuguese text + German explanations (Zielsprache Portugiesisch, Erklärsprache Deutsch)
**Week:** Monday 2026-11-02 to Sunday 2026-11-08 (W45) · **Volume:** VOL.2 · **Masthead:** A Lucerna
**Theme (frozen from the core):** A SEMANA DO ENEM — Finados feriadão (Mon 2 Nov) + Enem day 1 (Sun 8 Nov) + Copa do Brasil semifinal second legs (7/8 Nov).

This edition is the German-reader issue of the finalized Portuguese W45 core
(`files/weekly-report-w45-pt-core/`, Brazilian Portuguese text + Chinese
explanation layer, incl. its FIX1 P7 readers'-corner disclosure patch). It was
produced by copying the core build to
`hidden_files/weekly-report-w45-pt-de-build/` and rewriting ONLY the
explanation layer into full German, via the checked-in `transform.py`
(exact-literal replacements + file-specific post-pass). The Portuguese layer
is frozen (proof below). **Builder status: builder-complete only — this KIT
does NOT declare the edition finalized; an independent proofread is still
required (SOP §8.4). Nothing was posted to Discord, nothing was sent to the
main chat, no cron was created, weekly-git was not touched.**

## 1. Method & freeze proof

1. **Baseline first.** `tools/freeze.py baseline` on the unmodified core
   build: all 8 SVGs came out **byte-identical** to the shipped core SVGs
   (p1-capa 0dc8089df727dfe4, p2-vida 56db3aa80e1318db, p3-cultura
   82f6fc3a94fbc11e, p4-esporte c5647cf6e9c080ec, p5-jovens 92e86020ce81f3c8,
   p6-aprofundamento e6097473ded2f016, p7-lingua a72cb75a519319f4,
   p8-avaliacao 82630480322959ad — first 16 hex of sha256).
2. **Core untouched.** The shipped core SVGs were re-hashed after the full
   build: all 8 hashes identical to the baseline record above. W43
   directories were read only, never modified.
3. **Explanation layer rewritten in full German:** every gloss (prefix
   `HINWEIS · `), every section instruction, the P1 numbers-box glosses,
   the P2 time-box glosses, the P5 study-plan parentheticals, the P6 chart
   head, all three P7 teaching-column bridges, the common-errors notes, the
   word-of-the-week note, the readers'-corner notes, all 8 phrases-of-the-
   week translations, **and all 150 P8 answer notes**. Nothing explanatory
   remains in Chinese.
4. **Freeze audit (tools/freeze.py diff, --strict-cjk):** per page, edition
   CJK total **0** (core 156/177/153/148/223/118/357/1123) and **added CJK
   characters: 0** on all 8 pages. Every added/removed string is
   explanation-layer churn or a documented furniture/re-aim item below.
   **No Portuguese sentence, stem, option or key was removed or altered**
   except the three documented P8 re-aims in §4.
5. **Registry diff (150 vs 150, parsed from both builds' content files in
   order):** zero differences in number / page / level / type. Key
   differences: exactly #137, #138, #150 (§4). All other 147 keys are
   byte-identical to the core registry.
6. **Reproducibility (gate §8).** After the final build, a fresh copy of
   the core build + `transform.py` alone was run in a scratch directory
   and re-rendered: **8/8 SVGs byte-identical** to the delivered edition,
   transform exit 0, zero build warnings. `transform.py` is therefore the
   single source of the fan-out; no hand edit lives only in a content file.
   Per-round full sha256 baselines of svg/cards/PDFs are in the build dir
   (`run1-baseline.sha256` before round 2, `run2-baseline.sha256` before
   round 3).

## 2. Pairing badge & furniture (as printed; W43 PT × DE measured SVG wins over generic tables)

- **P1 badge** (brick red, bold, in place of the strapline, x=975, y=372,
  19 pt — W43 shipped geometry, verified in the W43 SVG):
  `PORTUGIESISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`
  (measured width 962.3 px, centred).
- **Footers (all 8 pages):** left `A Lucerna · PORTUGIESISCHE WOCHENZEITUNG
  VOL.2 · TEXT AUF PORTUGIESISCH · ERKLÄRUNGEN AUF DEUTSCH` (tables.json DE
  column, VOL.2) · right `Seite N von 8`.
- **Masthead:** `A Lucerna` (Portuguese article, unchanged). Edition line
  under it at **34 pt** (reduced from the core's 40 pt — the German line
  measures **1742.9 px** at 34 pt, limit 1820):
  `PORTUGIESISCHE WOCHENZEITUNG · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE`.
- **Top strip:** `TODA SEMANA EM PORTUGUÊS · DAS PORTUGIESISCH, DAS BRASILIEN LIEST`
  (W43 verbatim).
- **Band subtitles (Portuguese first, German half):** VIDA · LEBEN /
  CULTURA · KULTUR / ESPORTE · SPORT / JOVENS · JUGEND / APROFUNDAMENTO ·
  VERTIEFUNG / LÍNGUA · SPRACHE / AVALIAÇÃO E RESPOSTAS · TEST UND LÖSUNGEN;
  P2 sub keeps the Portuguese sub and appends the German half
  (`… · Finados und Wiederholung: das lange Wochenende in Brasilien`);
  P7 sub `Im Fokus: Sprache · Três níveis, três ferramentas · Drei Stufen, drei Werkzeuge`
  (W43 pattern); P8 sub `SEITE 8 · A grande prova da semana + todas as respostas`
  (W43 verbatim).
- **Bilingual section heads:** A NOTÍCIA · SCHLAGZEILE · AGORA VOCÊ · SIE
  SIND DRAN · EM POUCAS PALAVRAS · IN KÜRZE · QUIZ RELÂMPAGO · BLITZQUIZ ·
  PARA NÃO ERRAR · MERKSATZ · E VOCÊ? · UND SIE? · OS HORÁRIOS DO DOMINGO 8 ·
  DIE ZEITEN AM SONNTAG · A SEMANA DO FUTEBOL · DIE FUSSBALLWOCHE · FRASES
  DA SEMANA · SÄTZE DER WOCHE (wörtlich aus dieser Ausgabe) · RESPOSTAS ·
  LÖSUNGEN — nach Seiten geordnet, nach Nummer suchen · exercise heads
  `EXERCÍCIOS · ÜBUNGEN · SEITE n`, right note `Lösungen auf Seite 8 ·
  gemischte Stufen — nach Nummern suchen`.
- **Instruction labels:** Ausfüllen / Zuordnen / Sätze bilden /
  Wahr oder falsch? / Übersetzen / Schreiben.
- **Gloss prefix:** `HINWEIS · ` (tables.json DE column, W43 SVG-verified).
- **P8 separator — DEVIATION (documented, W43 precedent wins):** the
  shipped W43 PT × DE P8 keeps `— PÁGINA {n} —`, NOT the tables.json DE
  form `— SEITE {n} —`. This edition keeps `— PÁGINA {n} —` for the same
  reason: the family's shipped fan-out is the furniture authority.
- **Exercise `typ` registry strings** (e.g. "单选", "完成句子") are left
  untouched in the build code exactly as in the W43 PT × DE build: they
  are never rendered (bslib4 `ex()` prints level/number/instr/body only;
  P8 prints key/note and checks `type == "写作"` for the writing item).
  They appear nowhere in the SVGs (CJK total 0, §1.4).
- **Measured shortenings (house style, widths re-measured with production
  font metrics):** numbers box `A SEMANA EM NÚMEROS · ZAHLEN`; P1 palavra
  gloss one line `„Feriadão“ = langes Wochenende, drei Tage.`; P2 time-box
  labels shortened to single lines (`Sonntag 12 Uhr: öffnen`,
  `Die Tore schließen um 13 Uhr`, `13:30 Uhr: Beginn`, `19 Uhr: Ende`);
  P6 chart head `O DOMINGO 8 EM NÚMEROS · DIE ZAHLEN DES 8. NOVEMBER
  (horários oficiais do Inep)`; P5 plan parentheticals use half-width
  parentheses with a space before `(` (W43 rule).

## 3. Totals (core figures first, then this edition)

| | Core (W45 PT) | This edition (PT × DE) |
|---|---|---|
| Pages | 8 (1950×2700) | 8 (1950×2700) |
| Exercises | 150 — A2 49 · B1 70 · B2 31; per page 10/18/18/18/18/18/12/38 | **150 — identical** (same split) |
| Types | 完成句子 61 · 单选 49 · 词汇配对 12 · 造句 7 · 判断对错 3 · 完形单选 13 · 翻译 4 · 写作 1 | identical (registry types unchanged) |
| Writing model (§H) | 93 words, Portuguese, unchanged | 93 words, unchanged |
| Visible characters (SVG text nodes, no spaces) | 27,066 | 34,474 (P1 3605 / P2 3544 / P3 3109 / P4 3229 / P5 3273 / P6 3219 / P7 3716 / P8 9279 — German apparatus is longer) |
| CJK characters in final SVGs | — (Chinese layer) | **0** (all 8 pages) |
| Full-width punctuation in final SVGs | — | **0** |
| Print PDF | `A-Lucerna-VOL2.pdf` 15.96 MB (core name) | `A-Lucerna-VOL2-DE.pdf` — 3,475,407 B, 8 pages |
| Web PDF | `A-Lucerna-VOL2-web.pdf` 3.27 MB | `A-Lucerna-VOL2-DE-web.pdf` — 3,490,440 B, 8 pages (< 10 MB) |

PDF sha256: print `a952fcefde109f84ca0fcfc3e7c1981b47184d45432e7b04460b694822a03242`,
web `beea22b7ea91b02e5c0b8304b2710c1154efeae2a808633f921df5e562a59f29`.

## 4. Re-aimed items (the ONLY content changes vs the core)

Translation exercises legitimately re-aim at the reader's language (W43 KIT §4 pattern):

| # | Change |
|---|---|
| 137 | PT→DE. Stem frozen. Key now German: `Sonntag, 8. November ist Tag 1 des Enem.` (shortened from the first draft's longer key so the P8 line stays one line — see §6.3). Note: `vgl. Seite 6`. |
| 138 | PT→DE. Stem frozen. Key now German: `Prüfen Sie die Karte vor dem Sonntag.` Note: `confira = prüfen Sie`. |
| 139 | DE→PT. Stem now German: `„Der Feriadão geht vom 31. Oktober bis zum 2. November.“ → ___` Note: `feriadão = langes Feiertagswochenende`. **Portuguese key byte-identical.** |
| 140 | DE→PT. Stem now German: `„Wenn Sie ankommen, zeigen Sie bitte Ihren Ausweis mit Foto vor.“ → ___` Note: `Futuro do Subjuntivo chegar + Imperativ apresente`. **Portuguese key byte-identical.** |
| 150 | Writing (open). Registry key now German apparatus: `(offene Aufgabe — Mustertext unten)`; note `Mustertext in Bereich H auf dieser Seite (93 Wörter)`; §H line on the page: `Schreibaufgabe (offen); Mustertext (93 Wörter) unten.` Portuguese prompt and model text unchanged. |

All other 145 keys are byte-identical to the core registry (§1.5).

## 5. P8 gate (tools/p8.py compare, plus manual adjudication)

- `p8.py compare`: core **150 noted**, edition **150 noted**,
  status **CLEAN**, missing=[] extra_count=0 uncertain=[],
  keydiff=**[2, 4, 101, 137, 138, 146]**.
- **Real re-aims:** 137, 138 (§4). 150 shows no keydiff because both
  sides extract the writing key token `✓` (check branch) — the note
  change itself is real and printed (§4).
- **Adjudicated artifacts (NOT edition defects):** 2, 4, 101, 146.
  On the CORE side, those printed segments end in full-width paren
  groups (`portões — portões = 大门（考场大门）`,
  `13h30 — 13h30 开考（巴西利亚时间）`,
  `confiro — conferir：eu → confiro（不规则）`,
  `A — seção = 考场分区（房间）`), so p8.py's paren branch takes the
  whole pre-paren string as the key, while the edition (dash branch,
  no parens) extracts the true key. Proof the edition keys are correct:
  the registry diff (§1.5) shows edition keys for 2 (`portões`), 4
  (`13h30`), 101 (`confiro`), 146 (`A`) byte-identical to the core
  registry. The artifact is on the core side of the comparison, not a
  change in this edition.
- **P8 answer notes are pure German.** Printed P8 lines containing `(`:
  exactly one — #150's `Mustertext in Bereich H auf dieser Seite
  (93 Wörter)`, which is the W43-precedent writing-item form and is
  extracted via the check branch regardless. This is the handling of
  the NL × DE paren-group problem: no other P8 note carries parentheses
  at all, so no p8.py paren-branch pseudo-key can arise from this
  edition's notes. (Body-text parentheticals on P1/P5 are not P8 notes
  and are invisible to p8.py.)
- **P8 key flow ends clean:** lowest key baselines per column 2523.30 /
  2536.38 / 2534.72 / 2532.14 → clearances to the y=2580 rule 56.7 /
  43.6 / 45.3 / 47.9 px (every column ≥ 40 px).

## 6. Layout decisions forced by German length (three fix rounds)

1. **Round 1 (13 NEW occlusion flags, all real):** P1 palavra gloss
   wrapped to 2 lines and crossed the y=1844 rule → shortened to one
   line (final clearance **23.1 px**, cf. W43's 22 px). P7 column 3 grew
   (German notes) to col3-ends 2056.5, pushing the quotes block into
   the next-issue box and the footer → trimmed (see below). P8 keys
   overflowed by 3 clamped lines (148/149/150 drawn on one baseline) →
   shortened 5 col-3 keys to one line each (see round-2 note).
2. **Round 2 (P7 trims, content preserved):** error-clinic notes to one
   line each (`Nur schwarzer Stift — blau gilt nicht.`,
   `13 Uhr Schluss — 13:30 Uhr ist zu spät.`,
   `Kein Pauken nachts — Schlaf hilft mehr.`,
   `Feriadão: 31. Oktober bis 2. November.`); word note to one line
   (`feriadão = langes Feiertagswochenende.`); letters note to two
   lines (`Beispiel der Redaktion. Schreiben Sie uns! Beste Briefe
   erscheinen in VOL.3.`); disclosure to three lines (`Anmerkung: Echte
   Briefe und beste Texte kamen bis Redaktionsschluss nicht an —
   Beispiel bleibt, Versprechen gilt für VOL.3.`). Col3 ends 2056.5 →
   **1822.5**; quotes last translation ink bottom ≈ 2393 vs next-issue
   box top 2404 → **≈10.8 px clearance** (visually confirmed on the
   card). P8 keys: #130 (`Im Feriadão ruht er aus, wiederholt täglich
   etwas`), #131 (`Am Vorabend: Ausweis und Stift bereit, früh
   schlafen`), #134 (note abbreviated to `S + V + O + Ort` — P8 only;
   the P3 body note keeps its full form), #137 key (see §4), #144
   (`segunda chamada = kein Einlass nach Schluss: c`) — 5 lines saved
   vs 4 needed (61 px overflow), leaving ≈17 px margin. Round 2 build
   warnings: **zero**; occlusion flags: 1 (round-3 item).
3. **Round 3 (P7 word-box descender):** the Latin note's descenders
   crossed the word-box border by 1.1 px (audit BOXTITLE; the core's
   Chinese note has no descenders, so the core formula is 1.1 px too
   tight for Latin). Fix: word-box bottom pad +8 (formula constant
   20→28) compensated by −8 in the gap to the letters box (22→14), so
   col3 ends stay 1822.5 and the quotes block does not move. Both
   constants live in `transform.py`'s file-specific post-pass, so the
   fresh-copy reproduction (§1.6) includes them.
4. **Final build warnings:** FLOW OVERFLOW **0** · HEAD TOO WIDE **0**
   (round-3 log).

## 7. Geometric occlusion audit (mandatory SOP gate)

`tools/occlusion_audit.py` (selftest OK, all 6 classes fire, clean
controls silent), final run: **edition 0 flags · core 0 flags · NEW 0**.
Additional scans (same-baseline ink spacing, decoded entities):
- Same-baseline collisions: **0** on P2–P8; P1 has one 1.7 px gap
  (contents line `Finados, o dia da memória` + level label `A2→B1`) —
  gap is positive (no overlap) and the geometry is **byte-identical to
  the core** (same coordinates in the core SVG); it is the core KIT's
  retained tight-spacing item, not a new defect.
- P1 top band (y=92): left/middle/right ink gaps 224 px / 94 px — no
  collision (the FR × RU same-baseline failure mode, checked explicitly).
- Page-frame check (ink vs inner frame 40..1910 × 40..2660, PIL
  anchor-ls measurement, entities decoded): **0 violations on all 8
  pages** (this is the check whose EDGE class missed the NL × RU
  subtitle frame press; here it is run explicitly per page).
- P6 chart labels (`portões abertos`, `espera`, `prova`) vs later-drawn
  bars, baseline-anchored PIL measurement (getbbox anchor `ls`, 4×):
  **0.0% coverage each** (< 30% pass; bars start after the label
  advance by construction, and the card shows all three labels + values
  fully readable).

## 8. Gloss, phrases, readers' corner

- **Gloss counts** (rendered `gloss()` strings split on `·`, README
  §21 method): P2 6 = 6 · P3 6 = 6 · P4 5 = 5 · P5 5 = 5 · P6 4 = 4 —
  **total 26 = 26**, item by item vs the core.
- **Phrases of the week:** all 8 Portuguese quotes occur **exactly 2×**
  in the edition (source article + P7) and 2× in the core; each stands
  on its tagged page (P1 ×2, P2 ×2, P3, P4, P5, P6 — tags `Página N`
  unchanged from the core); P7 phrases are verbatim from this issue's
  articles (checked against the core's quote list, which is frozen).
- **Readers' corner (zero fabrication):** no reader, letter, name or
  quotation invented. The page simultaneously carries all three facts:
  (a) no real letters had arrived by press time — PT disclosure verbatim
  (`Nota da redação: as cartas reais e os melhores textos prometidos
  no VOL.1 não chegaram até o fechamento — fica o exemplo, e a
  promessa passa para o VOL.3.`) and its German same-meaning version
  (`Anmerkung: Echte Briefe und beste Texte kamen bis
  Redaktionsschluss nicht an — Beispiel bleibt, Versprechen gilt für
  VOL.3.`); (b) no best P8 text — same two disclosure sentences name
  the best texts; (c) labeled editor's example + VOL.3 promise
  (`«…» — EXEMPLO DA REDAÇÃO`, `Beispiel der Redaktion.`). The explicit
  German invitation is present and is not a preview line or an
  exercise prompt: imperative + publication promise —
  `Schreiben Sie uns! Beste Briefe erscheinen in VOL.3.`

## 9. Images & credits (public domain / CC0 only)

- Only photograph in the issue: P1 library-study photo (`estudo.jpg`) —
  **CC0, Gary Todd / Wikimedia Commons** (reused from the W43 PT core
  with the same credit line, printed on P1:
  `Foto: Gary Todd / Wikimedia Commons — CC0`, verified on the card).
  Embedded payload md5-identical to the core's P1 image
  (`7e6fa99b846ad620c84eb989452c52d4`).
- All other visuals are original charts/tables built from verified
  facts (P1 time table, P2 time boxes, P4 fixture table, P6 minute bars
  + two-Sundays table). No other photo is used; no new photo was
  introduced by this fan-out.

## 10. Cross-family residue scan

- Chinese residue: **0 per page** (CJK 0 on all 8 pages, §1.4).
- Full-width punctuation: **0** on all 8 pages.
- English residue (the DE × PT precedent): standalone English function
  words (`the/and/with/from/your/this/that/have/has/will/would/can/
  should`) scanned per page: **0 hits on all 8 pages**.
- No other target/native language's furniture strings appear (badge,
  footers, page lines, gloss prefix, section heads all DE-column forms
  from §2).

## 11. Build environment & reproduction

- `run.py` and `render.py` both ran under `tools/venv/bin/python`:
  **Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1** (system python3 has no
  cairosvg and was not used).
- Single-process renders only (run.py drives content12→34→56→7→8 in one
  process, per README §7 — the shared exercise registry rule).
- Build dir `hidden_files/weekly-report-w45-pt-de-build/` holds:
  `transform.py` (the fan-out), content/bslib/svglib sources, assets,
  `baseline.json` (freeze baseline 8/8), `diff-run2.json`,
  `occlusion-run1/2/3.json`, `p8-core.txt` / `p8-ed.txt`,
  `build-run1/2/3.log`, `build-render1/2/3.log`,
  `run1-baseline.sha256`, `run2-baseline.sha256`,
  `repro-check2/` (fresh-copy reproduction proof: transform exit 0,
  zero warnings, 8/8 SVGs byte-identical).
- Known transform incident, fixed in the tool: an early second run of
  `transform.py` on the already-transformed tree duplicated the P2 band
  subtitle (its new string contains its old string as a prefix);
  `transform.py` now refuses to run on an already-transformed tree
  (idempotency guard), and the delivered files were verified free of
  the duplication.

## 12. Retained items (with reasons)

- P1 contents tight gap (1.7 px, §7): core-identical geometry, core KIT
  retained item; no overlap, readable.
- P3/P5 column-bottom whitespace: same breathing whitespace as the core
  (flow bottoms unchanged by the fan-out).
- P1 numbers-box and P5 plan-box German parentheticals: body-text
  glosses, not P8 notes; half-width parentheses with a preceding space
  (W43 rule).
- Core facts untouched: Enem times (12h/13h/13h30/19h), "mais de 5
  milhões" (no precise count), no scores, no league positions, no
  election/market numbers — all inherited verbatim from the core.

## 13. Files

- `svg/` — 8 page SVGs (p1-capa … p8-avaliacao)
- `cards/` — 8 page PNGs (1950×2700, all 8 visually inspected: no
  overlap, no truncation, no footer press)
- `A-Lucerna-VOL2-DE.pdf` (print) · `A-Lucerna-VOL2-DE-web.pdf` (web)
- `ABSTRACT.txt` — German one-liner (no ASCII double quotes)
- Build code: `hidden_files/weekly-report-w45-pt-de-build/` (copy of the
  W45 PT core build + `transform.py`; core dirs untouched)

## 14. Open items (for the independent proofread, not the builder)

- Independent second-eyes proofread (SOP gate) has not been performed
  by this build; this KIT's conclusions are the builder's own checks.
- Repo insert (insert.py + lint) and any Discord delivery are for the
  main line to arrange; per the standing delivery pause, nothing was
  pushed or posted by this build.
