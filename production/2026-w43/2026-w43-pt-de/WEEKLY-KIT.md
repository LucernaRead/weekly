# A Lucerna — VOL.1 · Portugiesische Ausgabe für deutschsprachige Leser (PT × DE)

**Pairing:** Brazilian Portuguese text + German explanations (Zielsprache Portugiesisch, Erklärsprache Deutsch)
**Week:** Monday 2026-10-19 to Sunday 2026-10-25 (W43) · **Volume:** VOL.1 · **Masthead:** A Lucerna
**Theme (frozen from the core):** O SEGUNDO TURNO — runoff Sunday 25 October, final TV debate, Enem ahead.

This edition is the German-reader issue of the finalized Portuguese VOL.1 core
(`files/weekly-report-pt-vol1/`, Chinese explanation layer, incl. its §14 P8 patch and
§15 P7 readers'-corner rule patch). It was produced by copying the core build to
`hidden_files/weekly-report-pt-de-build/` and rewriting ONLY the explanation layer into
full German. The Portuguese layer is frozen (proof below).

---

## 1. Method & freeze proof

1. **Baseline first.** The unmodified copy was rebuilt before any edit: all 8 SVGs came out
   **byte-identical** to the shipped patched core SVGs (cmp on p1-capa … p8-avaliacao), and the
   exercise registry was identical (150 items). Only then was anything changed.
2. **Explanation layer rewritten in full German:** every gloss (prefix `HINWEIS · `), every
   section instruction, the P5 study-plan parentheticals, the P1 numbers-box glosses, the P2
   time-box glosses, the P6 chart sub-labels, all three P7 teaching-column notes, the
   common-errors notes, the word-of-the-week note, the readers'-corner note, all 8
   phrases-of-the-week translations, **and all 150 P8 answer notes**. Nothing explanatory
   remains in Chinese; nothing explanatory is a one-line gloss over Portuguese — the apparatus
   is German throughout.
3. **Freeze audit (SVG text-node multiset diff, core vs this edition):** every removed core
   node is (a) Chinese apparatus, (b) a bilingual furniture line whose Portuguese half survives
   verbatim inside the new German line, or (c) one of the documented exceptions: the P1
   tagline line (replaced by the pairing badge — same accommodation as the other reader
   editions) and the P8 key lines whose Chinese notes contained full-width colons (note text
   only; the Portuguese keys inside them are unchanged). **No Portuguese sentence, stem,
   option or key was removed or altered.**
4. **Registry diff (150 vs 150):** zero differences in number / page / level / type.
   Key differences: exactly the three documented items in §4. 149 of 150 answer notes differ
   (apparatus language); the one unchanged note is the language-neutral arithmetic
   "900 − 250 = 650".

## 2. Pairing badge & furniture (as printed)

- **P1 badge** (brick red, bold, in place of the tagline, y=372):
  `PORTUGIESISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`
- **Footers (all pages):** left `A Lucerna · PORTUGIESISCHE WOCHENZEITUNG VOL.1 · TEXT AUF
  PORTUGIESISCH · ERKLÄRUNGEN AUF DEUTSCH` · right `Seite N von 8`
- **Masthead:** `A Lucerna` (Portuguese article, unchanged). Edition line under it at **34 pt**
  (reduced from the core's 40 pt Chinese line — the German line measures 1793 px at 34 pt,
  limit 1820): `PORTUGIESISCHE WOCHENZEITUNG · VOL.1 · O SEGUNDO TURNO · O DEBATE FINAL · O
  ENEM VEM AÍ`
- **Top strip:** `TODA SEMANA EM PORTUGUÊS · DAS PORTUGIESISCH, DAS BRASILIEN LIEST`
- **Bilingual section heads (Portuguese first, German half):** A NOTÍCIA · SCHLAGZEILE ·
  AGORA VOCÊ · SIE SIND DRAN · EM POUCAS PALAVRAS · IN KÜRZE · QUIZ RELÂMPAGO · BLITZQUIZ ·
  PARA NÃO ERRAR · MERKSATZ · E VOCÊ? · UND SIE? · OS HORÁRIOS DO DOMINGO · DIE ZEITEN AM
  SONNTAG · A SEMANA DO FUTEBOL · DIE FUSSBALLWOCHE · FRASES DA SEMANA · SÄTZE DER WOCHE
  (wörtlich aus dieser Ausgabe) · RESPOSTAS · LÖSUNGEN — nach Seiten geordnet, nach Nummer
  suchen · bands VIDA · LEBEN / CULTURA · KULTUR / ESPORTE · SPORT / JOVENS · JUGEND /
  APROFUNDAMENTO · VERTIEFUNG / LÍNGUA · SPRACHE / AVALIAÇÃO E RESPOSTAS · TEST UND LÖSUNGEN ·
  exercise heads `EXERCÍCIOS · ÜBUNGEN · SEITE n`, right note `Lösungen auf Seite 8 ·
  gemischte Stufen — nach Nummern suchen`.
- **Measured shortenings (house style kept, widths re-measured with production font
  metrics):** numbers box `A SEMANA EM NÚMEROS · ZAHLEN` (the longer "· IN ZAHLEN" variant
  measured 429 px > 390 box width); error clinic `ERROS COMUNS · HÄUFIGE FEHLER`; P6 chart
  head `AS BUSCAS DO 1º TURNO · DIE SUCHEN ZUM 1. WAHLGANG (dados do Google)`.
- **Instruction labels:** Ausfüllen / Zuordnen / Sätze bilden / Wahr oder falsch? /
  Übersetzen / Schreiben.
- **Gloss prefix:** `HINWEIS · ` (the library's configurable gloss label).

## 3. Totals

| | |
|---|---|
| Pages | 8 (1950×2700, 4 columns, warm ivory #f7f1e2) |
| Exercises | **150** — A2 44 · B1 75 · B2 31; per page 10/18/18/18/18/18/12/38 |
| Visible characters (SVG text nodes) | 34,965 without spaces · 41,502 with spaces (core: 30,100 / 35,889 — the German apparatus is longer) |
| Writing model (§H) | 92 words, Portuguese, unchanged |
| CJK characters in final SVGs | **0** (all 8 pages) |
| Full-width punctuation in final SVGs | **0** |
| Print PDF | `A-Lucerna-VOL1-DE.pdf` — 6,456,333 B |
| Web PDF | `A-Lucerna-VOL1-DE-web.pdf` — 3,667,040 B (< 10 MB Discord limit) |

## 4. Re-aimed items (the ONLY content changes vs the core)

Translation exercises legitimately re-aim at the reader's language (§E, P8):

| # | Change |
|---|---|
| 137 | PT→DE. Stem frozen. Key now German: `Am Sonntag kehrt Brasilien an die Wahlurnen zurück.` Note: `vgl. die Schlagzeile auf Seite 1` |
| 138 | PT→DE. Stem frozen. Key now German: `Prüfen Sie Ihren Wahlort, bevor Sie losgehen.` Note: `Confira = prüfen Sie` |
| 139 | DE→PT. Stem now German: `Die Suchen nach «guitarra» sind um 53 % gestiegen. → ___` Note: `cresceram = sind gestiegen`. **Portuguese key byte-identical.** |
| 140 | DE→PT. Stem now German: `Wenn Sie ankommen, prüfen Sie bitte Ihr Wahllokal. → ___` Note: `Futuro do Subjuntivo (chegar) + Imperativ confira`. **Portuguese key byte-identical.** |
| 150 | Writing (open). Registry key line now German apparatus: `(offene Aufgabe — Mustertext unten)`; note `Mustertext in Bereich H auf dieser Seite (92 Wörter)`; §H line on the page: `Schreibaufgabe (offen); Mustertext (92 Wörter) unten.` Portuguese prompt and model text unchanged. |

All other 145 keys are byte-identical to the core registry (verified by direct diff).

## 5. Layout decisions forced by German length

1. **P7 col-3 trims (one wrapped line each, content preserved):** the German notes initially
   grew each col-3 box by exactly one line (+29/+29/+29 px), which pushed the
   phrases-of-the-week start from fy=1766 to fy=1853.5 and drove the last quote row into the
   hardcoded next-issue box (top y=2404). Trimmed: error-clinic note 1 (`…steht mit a: ao
   debate.`), word-of-the-week note (`urna = die elektronische Wahlurne — auch die Wahl
   selbst: voltar às urnas, as urnas abrem.`), readers'-corner note (`Beispiel der Redaktion —
   in VOL.2 echte Briefe und der beste Seite-8-Text!`, 2 lines). Col-3 geometry is now
   **identical to the patched core**: boxes 856.5 / 303.0 / 318.5, stack bottom 1722.0,
   fy = 1766, gold rule at y=1752.
2. **P1 palavra gloss shortened to one line:** `„Wahllokal“: der genaue Ort Ihrer Stimme.`
   (381 px). The two-line first version left its last line's ink band crossing the row rule
   at y=1844 (crop-verified graze); the one-line version restores the core's ~22 px clearance.
3. **P5 study-plan spaces:** the five German parentheticals take a normal space before "("
   (the core's full-width Chinese parenthesis needed none); box height recomputes from the
   same strings, verified in the render.
4. **P8 key flow** ends at cursor y=2504 (flow bottom 2552) with the core's patched key
   typography (13.5 pt, lh 1.16) retained.

## 6. Geometry — measured clearances

- **P8 lowest key baselines per column** (measured in the final SVG, rule at y=2580):
  col 1 **2535.64** (44.4 px clear) · col 2 **2534.72** (45.3) · col 3 **2537.30** (42.7) ·
  col 4 **2487.56** (92.4). Every column clears by ≥ 40 px (the requirement; the PT×EN
  sibling shipped at ~5 px — this edition does not repeat that).
- **P7 readers'-corner rule:** fy = max(1712, ly+lh+44) = 1766 → rule at **y=1752**, German
  note ink bottom ≈ 1709 → **≈43 px clearance**; crop-checked in the rendered card.
- **Phrases row vs next-issue box:** last translation ink bottom 2382.5 vs box top 2404 —
  21.5 px, exactly the patched core's geometry.

## 7. Geometric occlusion audit (mandatory SOP gate)

Paint-order audit over all 8 final SVGs with production font metrics (ink band
baseline −0.88 em … +0.30 em): checks (a) ≥30 % coverage by a later opaque shape,
(b) footer-band intrusion / rule crossing, (c) page-edge spill, (d) any later-drawn line
crossing a text ink band. **Final result: 0 flags.**

Two flags during production, both real, both fixed and re-audited:
1. P7 phrases row 4 covered 67–100 % by the next-issue box → fixed by the §5.1 trims.
2. P1 palavra gloss line crossing the y=1844 rule (crop-verified graze) → fixed by §5.2.

## 8. Proofread record (builder pass)

- Registry re-diffed against the core: structure identical; key diffs = §4 only.
- Re-solved against the printed keys (sample of 40+): all of P1 (1–10) and P2 (11–28)
  from the text; arithmetic #23 (982+514+431+312=2.239), #57 (66.026 > 66.000), #86
  (350+350=700), #87 (900−250=650); subjunctive set #109–112 (tiver / chegar / for / for);
  translations #137–140; writing #150. All keys confirmed; every P8 note parenthesis is
  preceded by a space and uses half-width parentheses only.
- P7 phrases: the 8 Portuguese quotes are part of the frozen text layer (byte-identical
  node audit, §1.3); each stands in its source article and in the phrases section with the
  correct page tag (P1 ×2, P2 ×2, P3, P4, P5, P6 as printed).
- Facts identical to the core: runoff **Sunday 25 October**; Copa do Brasil semifinals in
  **November** (1 Nov Palmeiras×Vasco 16:00, Grêmio×Atlético-MG 18:30; returns 7/8 Nov);
  **no poll percentages anywhere** — every % figure in the paper, including inside German
  notes, is Google search data and is labelled as such (`Google-Suchdaten — keine
  Wahlabsicht.`).
- Images: all 4 embedded payloads byte-identical to the core (md5-verified: P1 urna,
  P3 violão + Django, P5 study hall); credit lines unchanged (Portuguese, as in the core).
- The banned intermediary term appears 0 times in the paper and in this KIT.

## 9. VOL.2 promises carried from this issue (must be honoured)

- P7 next-issue box (Portuguese, frozen): Halloween Sat 31 Oct; Copa do Brasil semifinals
  Sun 1 Nov; Finados Mon 2 Nov (three-day weekend); Enem Sun 8 & 15 Nov.
- Readers' corner (German note): VOL.2 prints **real readers' letters and the best writing
  text from page 8**.

## 10. Files

- `svg/` — 8 page SVGs (p1-capa … p8-avaliacao)
- `cards/` — 8 page PNGs (all viewed in proofread)
- `A-Lucerna-VOL1-DE.pdf` (print) · `A-Lucerna-VOL1-DE-web.pdf` (web, Discord-ready)
- Build code: `hidden_files/weekly-report-pt-de-build/` (copy of the core build; core dirs
  untouched)

## 11. Independent proofread record (SOP gate — second pair of eyes, 2026-10-21)

One complete independent pass, nothing taken on the builder's word. **Result: zero
problems found; no fixes, no re-render needed.**

- **Core integrity:** full SVG text-node multiset diff, all 8 pages (322 removed /
  354 added node instances). Every delta classified: Chinese apparatus → German
  apparatus, bilingual furniture (Portuguese half preserved verbatim), or a documented
  exception (§4 items; P1 tagline → badge; P1 edition line). No Portuguese sentence,
  stem, option or key altered.
- **Registry (dumped independently from both builds):** 150 vs 150; levels
  A2 44 · B1 75 · B2 31, pages 10/18/18/18/18/18/12/38, types identical. Only fields
  differing anywhere: `key`/`note`; key diffs = exactly #137, #138, #150 (§4);
  #139/#140 keys byte-identical Portuguese.
- **Re-solve:** all 150 exercises re-solved from the printed articles/charts — every
  key correct (incl. #23 = 982+514+431+312 = 2.239, #86 = 700, #87 = 650, subjunctive
  set #109–112, translations #137–140). German apparatus read in full: natural,
  grammatical; space before every parenthesis — programmatic scan of all pages:
  0 violations, incl. the five P5 study-plan parentheticals (also crop-verified).
- **Language scans:** CJK = 0 and full-width punctuation = 0 on all 8 pages.
  Visible characters recomputed: 34,965 / 41,502 — exactly as §3.
- **Red line:** every % figure in the edition is Google search data and labelled as
  such («Google-Suchdaten — keine Wahlabsicht.», article framing, P8 notes);
  no poll percentages anywhere.
- **Geometry (own paint-order audit, production font metrics):** 0 coverage, 0
  line-crossing, 0 page-edge, 0 text–text flags; the only hits are the 16 footer-self
  items (each page's own footer text below its rule, by design, as in the core).
  P8 lowest baselines per column measured: 2535.64 / 2534.72 / 2537.30 / 2487.56 →
  clearances 44.4 / 45.3 / 42.7 / 92.4 px — the builder's §6 figures exact.
  P7 gold rule at y=1752 confirmed in the SVG; readers'-corner note ink bottom
  1709.5 → 42.5 px clearance, crop-verified in the rendered card. P1 palavra gloss:
  one line, ink bottom 1821.9 vs the y=1844 rule → 22.1 px, crop-verified.
  Phrases row ends 2382.5 vs next-issue box 2404, as in the patched core.
- **Badge/furniture:** P1 badge centred (x=975, y=372, 19 pt bold, brick red),
  visible in the render; pairing footers on all 8 pages; masthead «A Lucerna»;
  edition line 34 pt, width measured 1793 px ≤ 1820.
- **P7 phrases:** each of the 8 quotes occurs exactly 2× in the build sources
  (source article + phrases section), byte-verbatim; German translations carry the
  correct page tags (P1 ×2, P2 ×2, P3, P4, P5, P6). Facts identical: runoff Sunday
  25 October; Copa do Brasil semifinals in **November**.
- **Images:** all 4 embedded payloads md5-identical to the core per page; credit
  lines unchanged (Portuguese). Both PDFs 8 pages; sizes as §3.
- **Adjudication:** the string `bridge` occurs in the build code only as the
  inherited layout-method name `bridge()` (the grey instruction-line renderer),
  byte-identical in the frozen core build; it appears nowhere in the paper or this
  KIT and is not the banned intermediary-language term. Not a defect.

**Verdict: PASS — final.**
