# Die Lucerna — DE × IT · WEEKLY-KIT

**Edition:** German target text (VOL.1 core, frozen) · explanations in Italian for Italian-speaking readers
**Week:** W43 · Mon 19 – Sun 25 October 2026 · **Pages:** 8 (1950×2700) · **Exercises:** 150 (A2 67 · B1 69 · B2 14)
**Build:** `hidden_files/weekly-report-de-it-build/` (transform_it.py = the exact-count replacement record; registry_core.json / registry_it.json = registry dumps)
**Proofread:** builder's own full pass complete (see §9) · **independent proofread: DONE — PASS (see §11; one real defect found and fixed, §10 pins for p7 + both PDFs superseded by §11)**

---

## 1 · Baseline proof (fan-out method step 1)

The core build dir was copied to `weekly-report-de-it-build/` and run UNMODIFIED with its
output redirected to `baseline-out/`. All 8 SVGs reproduced the shipped core SVGs byte-identically:

| page | sha256 (baseline reproduction = shipped core) |
|---|---|
| p1-front | be1b0f7b7f2c… |
| p2-leben | cac83eb5d228… |
| p3-kultur | d862d862b123… |
| p4-sport | 591eaa94747d… |
| p5-jugend | b48ed8104190… |
| p6-vertiefung | a69b6fee767d… |
| p7-sprache | b4f74e0844fb… |
| p8-uebungen | 8fb288ff2ee0… |

**Baseline: 8/8 byte-identical.** Only after this proof was the copy edited. The frozen core
(`files/weekly-report-de-vol1/`, `hidden_files/weekly-report-de-build/`) was never modified.

## 2 · What changed (and only this)

- Every Chinese explanation string → Italian: glosses (prefix «Nota — »), grammar notes,
  section instructions, exercise apparatus, all P8 answer notes — fully in Italian.
- Pairing furniture (§4). Registry type names → Italian (completare, scelta multipla,
  trasformazione, abbinamento, vero/falso, costruire frasi, testo a buchi, traduzione,
  completare il dialogo, scrittura); instruction labels → Completa / Riscrivi / Vero o falso? /
  Costruisci la frase / Abbina le coppie / Traduci in italiano / Traduci in tedesco.
- Answer-key format: space + half-width parenthesis `key (note)` (core used full-width parens).
- The explanation-layer method in bslib4 is named `expl()`; the intermediary-layer term occurs
  0 times in paper, KIT and code. Zero CJK and zero full-width punctuation in the final SVGs
  (verified by scan of all build code and by the text diff, §6).
- P8 answer-key typography: 14.5px/1.3 → **13px/1.26** so the longer Italian notes fit the page
  (keys flow ends y=2328 of 2560). Same documented adjustment as the DE×FR and DE×ES editions.
- German target text, images, layout geometry: frozen. Flow end positions match the core
  (P1 headline flow ends y=1585, P6 exercises y=2402 — identical to core and to DE×ES).

## 3 · Key-diff registry (complete)

Registry diffed item-by-item against the core registry (levels, pages, types after mapping:
all identical; notes: 135 translated, 15 German-only notes correctly unchanged).
**Keys differing from the core: exactly 3.**

| # | section | core key | DE×IT key | why |
|---|---|---|---|---|
| 137 | E · ÜBERSETZEN | 这一夜有 25 个小时。 | **La notte ha 25 ore.** | translation item re-aimed at Italian; note: «Stunden = ore» |
| 138 | E · ÜBERSETZEN | 我周六晚上拨钟。 | **Sabato sera sposto l'orologio.** | translation item re-aimed at Italian; note: «umstellen = spostare (un orologio)» |
| 150 | H · SCHREIBEN | 开放题 — 要点见写作框，范文在第 8 版写作框内 (note 按要点给分） | **Domanda aperta — segui i punti del riquadro di scrittura; il testo modello è nel riquadro di questa pagina** (note: «Si valuta secondo i punti indicati») | writing apparatus in Italian |

**Stem-only re-aims (keys byte-identical to core):**

| # | core stem | DE×IT stem | key (unchanged) |
|---|---|---|---|
| 139 | 我周日多睡一小时。（译成德语） | **Domenica dormo un'ora in più.** (instr: Traduci in tedesco) | Am Sonntag schlafe ich eine Stunde länger. |
| 140 | 在图书馆可以借书。（译成德语） | **In biblioteca si possono prendere in prestito i libri.** (instr: Traduci in tedesco) | In der Bibliothek kann man Bücher leihen. |

Items 137/138 also drop the core's in-body direction suffix; the direction is carried by the
instruction label («Traduci in italiano»), as in DE×ES. No other key differs.

## 4 · Italian furniture (verbatim, as shipped)

- P1 badge (brick, y=372 strap slot): «TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI»
- P1 strap: «SETTIMANALE TEDESCO · VOL.1 · OROLOGI · VACANZE · BRINA» · top strip: «WÖCHENTLICH AUF DEUTSCH · OGNI SETTIMANA · IL TEDESCO CHE LEGGONO I TEDESCHI»
- Footer (all pages): «Die Lucerna · SETTIMANALE TEDESCO VOL.1 · TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»
- Gloss prefix: «Nota — » · masthead: «Die Lucerna» (as the core ships)
- All furniture strings were measured with the production font metrics before building;
  every string fits its slot (widths on file in measure_it.py).

**Width-driven wording shortenings (wording shortened, never geometry):**
1. P1 clock-band right line: «Domenica, orologio indietro» — the fuller «Domenica si riporta
   l'orologio indietro» (450.7px) would start at x=1404 and collide with the German band line
   (ends x=1502); the shipped wording starts at x=1524, mirroring DE×ES's clearance (23px).
   Found by the text-text audit, fixed, re-audited clean.
2. P7 toolbox title: «DER WERKZEUGKASTEN · Gli utili» («· Gli strumenti» measured 451px > the
   412px box inner width).
3. P8 section head: «F · WÖRTER PAAREN · Le coppie» («· Abbina le parole» measured 478px > 434px column).
4. P1 expl line and the three «In cifre» parentheticals shortened to DE×ES brevity so the P1
   headline flow keeps the core's exact column distribution (verified by simulation).
5. P6 instruction lines A/B shortened to one line each («Guarda il grafico e scegli la risposta
   giusta.» / «Leggi il testo di pagina 6 e scegli la risposta.») — two-line versions cascade
   the exercise flow past the page bottom (simulated +266px).

## 5 · Printed-note set verification

The core prints ALL 150 P8 notes (print-all rule). This edition's registry has 150/150
non-empty notes and the keys are generated by the identical code path. Verified in the
RENDERED p8 SVG: the printed key numbers run 1→150 in order (complete sequence), every one of
the 150 items was observed with its parenthetical note (142 by segment scan + the 8 page-group
leaders 1/11/29/47/65/83/101/113 verified individually), 0 items without a note.
**Printed-note set = the core's set of 150. PASS.**

## 6 · Freeze check

Full text-element diff, core SVGs vs this edition's SVGs, all 8 pages, reviewed line by line:
every removed line contains Chinese or is a bilingual furniture/mixed element; every added line
is its Italian counterpart. No German article text, exercise body, option list, fixture row,
timeline entry, model text or credit line differs. P7 phrase quotes: occurrence count of each
of the 8 German quotes in the build sources is exactly 2 — identical to the core (verbatim
contiguous excerpts, page tags Seite 1/2/3/4/5/6/2/6 unchanged).
Calendar re-verified for 2026: Sat 24 Oct (Tag der Bibliotheken), Sun 25 Oct 03:00→02:00
(Zeitumstellung), Sat 31 Oct (Halloween + Klassiker), Sun 1 Nov (Allerheiligen), Sun 28 Mar 2027
(Winterzeit end), Fri 23 Oct (fixture row) — all correct.

## 7 · Geometric occlusion audit (mandatory gate)

Scripts: audit_de_it.py (paint-order coverage/line/footer/edge; line boxes expanded by half
stroke width), audit_titles.py (box-border crossings), audit_texttext.py — validated first on a
synthetic positive control (all 4 defect classes fire: COVER, LINEX, FOOTER, EDGE).

**Core (baseline SVGs):** main audit 0 flags · titles audit 1 crossing (the core's own P1
Fragen subtitle strikes 19.2px past its box border) · text-text 1 (masthead model artifact).
**This edition (final SVGs):** main audit 1 flag · titles audit **0 crossings** (the Italian
subtitle «Le domande delle guide tedesche», 297px, fits the box — the core's crossing is gone) ·
text-text 2. **No NEW defects; flag-by-flag adjudication:**

1. Main-audit LINEX, P7: phrases hline (y=1508) vs word-box line 2 ink band. PIXEL adjudication
   on the 1950×2700 render: text ink (descenders of «gegen») ends at pixel row 1506; the gold
   rule occupies rows 1507–1508. Zero shared rows → **graze, non-defect**.
2. Text-text, P1 masthead vs strap: model-band artifact of the 168px wordmark; also fires on
   the core. PIXEL check: wordmark ink ends row 264, strap ink starts row 295 → **non-defect**.
3. Text-text, P7: word-box line 3 (baseline 1531) vs phrases header right (baseline 1548).
   PIXEL check: word ink bottom row 1530, header ink top row 1537 → **graze, non-defect**.

**Defect found by eye in the builder's proofread and FIXED:** P6 chart label «leggere un
libro» (145.0px) ran 5px under its bar (bar starts x=535; label ended x=540) — below the
audit's 30% coverage threshold, visible in the render. Shortened to «leggere libri»
(109.8px, ends x=505) and re-rendered; only p6 SVG changed, all other pages byte-identical.
Bar values/lengths re-measured: 46/22/18/14 % at 24px per point — correct.

## 8 · Images (all public domain; credit lines as printed, frozen from the core)

| file | page | credit line (printed) |
|---|---|---|
| frost.jpg | P1 | Foto: Courtney Celley, U.S. Fish and Wildlife Service — public domain |
| atomuhr.jpg | P2 | Foto: NIST — public domain |
| luther.jpg | P3 | Gemälde: Lucas Cranach d. Ä., 1528 (Veste Coburg) — public domain |
| kuerbis.jpg | P5 | Foto: U.S. Department of Agriculture — public domain |

All four images verified as actually placed in the renders (P1 frost branches, P2 NIST-F1,
P3 Luther portrait, P5 pumpkin market).

## 9 · Builder's proofread record

All 8 pages read end-to-end in the rendered cards. All 150 keys re-derived via the registry
diff (§3) plus spot re-derivation from the German text on every page; totals/levels equal the
core (150 · A2 67 · B1 69 · B2 14); every weekday/date claim re-checked (§6); P7 verbatim +
2×-occurrence parity (§6); printed-note set (§5); audits (§7). Defects found in this pass:
P1 clock-band collision (fixed, §4.1) and the P6 bar label (§7) — both fixed and re-verified.
**Independent proofread: DONE — PASS, see §11.**

## 10 · Deliverables & pins

| file | bytes | sha256 |
|---|---|---|
| Lucerna-VOL1-IT-web.pdf | 4,263,206 | 36fa2dae69dff67821e3530e15b1b0a579393c8a7bb1d88b9e5f33a0cb485f6f |
| Lucerna-VOL1-IT.pdf (print) | 10,478,579 | 0aaba2e1d222c2ac7543368eac0d7cc643aae6f986c97dd27d635178213cc220 |

Web PDF < 10 MB ✓ (JPEG pages q85 @1400px, the finalized core recipe).
Final SVG sha256: p1 278b8a87ae00… · p2 03b912940f18… · p3 9c7c75678949… · p4 983f6b34656d… ·
p5 15adee729d87… · p6 79fbe9eb09f2… · p7 99f0ff91453a… · p8 398ee71e49b9…
Cards: cards/p1-front.png … p8-uebungen.png (1950×2700).

---

## 11 · Independent proofread record — PASS (after one proofreader fix)

Independent pass by a fresh proofreader (own extraction, own registry dumps from fresh
build runs in scratch copies, own occlusion-audit implementation), 2026-10-21/22.
Scratch + scripts: `hidden_files/proof-deit-independent/`.

**Baseline & build integrity.** The unmodified core build, copied to scratch with only its
output path redirected, reproduced all 8 shipped core SVGs byte-identically (8/8, hashes =
§1). A scratch copy of this edition's build likewise reproduced the shipped edition SVGs
8/8. Core shipped SVG hashes re-measured at the end of the pass: unchanged.

**Freeze.** Full text-element diff, core vs edition, all 8 pages, every line classified:
each removed line contains Chinese, is the P1 pairing-badge slot line (replaced by the
Italian pairing badge, §4), or is an answer-flow / punctuation wrap fragment whose German
key text is intact in both editions; zero added lines contain CJK. No German article text,
exercise body, option, fixture row, timeline entry, model text or credit line differs.
Italian completeness confirmed by reading all 8 rendered pages end-to-end; CJK count in
the final SVGs and in both PDFs' text layers = 0.

**Registry (own dumps from both builds).** 150 = 150; levels A2 67 · B1 69 · B2 14 and
per-page counts 10/18/18/18/18/18/12/38 identical; type names map 1:1 with identical
counts. **Key diffs = exactly {137, 138, 150}**, with exactly the §3 values (137 «La notte
ha 25 ore.», 138 «Sabato sera sposto l'orologio.», 150 Italian apparatus); both are faithful
renderings of the German stems («Die Nacht hat 25 Stunden.», «Ich stelle die Uhr am
Samstagabend um.») sighted in the printed P8. Stems 139/140 are re-aimed in Italian
(«Traduci in tedesco») with German keys byte-identical to the core (registry-proven).
Notes: 135 translated, 15 unchanged — all 15 verified German-only (grammar forms,
arithmetic) with no Chinese inside; no empty notes on either side. All 150 printed keys
were sighted in the P8 answer block and checked against the German text page by page.

**PRINTED-NOTE SET EQUALITY — PASS.** Sets extracted from the shipped P8 SVGs by full
key+note string match (whitespace-normalized): core printed set = {1..150}, this edition
= {1..150}. EQUAL by number; every note present with its exact registry text.

**P7 phrases.** All 8 German quotes occur exactly 2× issue-wide in BOTH editions (article
page + P7), page tags identical (Seite 1/2/3/4/5/6/2/6) and matching the article page each
quote was found on. **Calendar** re-verified with `date` (Europe/Berlin): Sat 24 Oct, Sun 25
Oct (03:00→02:00), Fri 23 Oct fixture, Sat 31 Oct, Sun 1 Nov, Sun 28 Mar 2027 — all correct.

**Geometric occlusion audit (own implementation).** Paint-order parse, PIL real-font glyph
boxes, line boxes expanded by half stroke width; validated on a synthetic positive control
first (5/5 planted classes fired: COVER, LINEX, EDGE, FOOTER, box-border TITLE; clean text
and a clean box title unflagged). Core: 5 flags. Edition as shipped: 7 flags, of which the
4 shared with the core were pixel-adjudicated non-defects (identical renders in both
editions): P2/P3/P5 facts-box last line spills under its box border — border row sits
between text lines and touches no glyph ink (P2 measured: upper line ink ends row 1157,
border row 1158, spilled-line ink starts 1159; core and edition pixel counts identical
row-for-row); P8 match line ink ends x=1905 vs inner frame x=1910 in both editions.

**ONE REAL DEFECT FOUND (new in this edition) — FIXED by the proofreader.** On P7 the
Italian toolbox glosses wrapped one line longer than the core's Chinese for two entries
(«Von O bis O …» and «Es ist fraglich, ob …»), cascading the whole col-4 stack +59px: the
NOCH EIN WORT box (bottom at y=1544.5 vs the core's 1485.5) was cut by the phrases hline
(y=1508) and its bottom border struck through the phrases subtitle «Citazioni letterali
dagli articoli…» (border row 1544 inside the subtitle's ink rows 1537–1552; the two text
lines visually collided). The builder's audits did not test this pair, so their "0 new
defects" claim was false for P7. Fix (explanation layer only, wording only; measured with
the production wrap at the 390px box width): toolbox entry → «Von O bis O = gomme,
ottobre-Pasqua» (375.5px, 1 line) and «Es ist fraglich, ob ... = non è chiaro se» (371.6px,
1 line; only the Italian gloss's trailing ellipsis dropped). Rebuilt via the edition's own
pipeline: build log «P7 col3 ends 1485.5» = the core's value; NOCH box back at y=1335.5 /
bottom 1485.5; only p7-sprache.svg changed (other 7 pages byte-identical); registry
post-fix == pre-fix. Pixel-verified on the shipped card: hline rows 1507–1508 carry no text
ink, subtitle ink rows 1531–1552 contain no rule row. The ENTIRE pass was then re-run from
the top on the final artifacts: freeze diff, registry, printed-note sets, phrases, scans,
images, and the audit (final edition flags = the 4 inherited, pixel-cleared ones only).

**Builder's other claims verified at pixel level.** P1 clock band: German headline ink
ends x=1506, Italian «Domenica, orologio indietro» ink starts x=1510 — clear (tighter than
the advance-metric figures in §4.1, but no contact). P1 Fragen subtitle «Le domande delle
guide tedesche» ink x1473–1770, fits its box (the core's own title overflow at this box —
ink to x≈1905 past the x=1885 border — is a core defect this edition does not inherit).
P6 chart label «leggere libri» ink ends x=505, bar starts x=535 — clear. Shortened titles
fit: toolbox title ink ends x=1858, P8 «F · WÖRTER PAAREN · Le coppie» ends x=1849 (edge
1885). P8 keys flow ends y=2328 (§2) confirmed from the build log; P1/P6 flow ends match
the core (1585 / 2402). Images: payloads and placements byte-identical to the core on all
pages; printed credits match §8 and the core KIT.

**Documentation correction (§2 scope).** The intermediary-layer term occurs 0 times in the
paper, in this KIT, in both PDFs, and in every runnable build module (bslib4.py,
content*.py, run.py, render.py, registry JSONs). It survives only as the 5 source patterns
inside transform_it.py — the rename tool's search strings that removed the inherited core
method name (the same pattern as the sibling RU×IT build's transform tool). §2's "0 times
in paper, KIT and code" should be read with that scope; the edition itself is clean.

**Final pins (supersede §10 for p7 and both PDFs; all other §10 values unchanged):**
- p7-sprache.svg sha256 `e00cd11ee21e068d3927c6bbb1ae74a95ce266579a0db1af04e42c254761a4b2`
- Web PDF: **4,262,595 B** (< 10 MB ✓), sha256 `9449bb0c00124e24da7d165c1e655b3af6c2b5ef9d7c47d737593e389087791b`
- Print PDF: 10,478,562 B, sha256 `266267f4d0a61254500e30b8e1a9d72701c073ca94e17db8a75f69b7b216c00f`

**Verdict: PASS — one complete independent pass with zero problems on the final
artifacts. Cleared for repo insertion.** No repo insert, no posts made (per scope).
