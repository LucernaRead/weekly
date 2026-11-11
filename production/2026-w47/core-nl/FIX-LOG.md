# FIX-LOG — core-nl fix round 2 (2026-11-11)

Core-nl reopened after nl-de proof1 (b) found D3 + D4; nl-es proof1 D5 was
verified as a true core defect and merged into this round. Scope: D3 + D4 +
D5 only. nl-de D1/D2 (German box overflow) are edition-level, pending
re-fan-out + per-edition fix1 — not in this round. D5 (web PDF italic loss)
is handled by rebuilding all web PDFs with the patched webpdf.py before
insert — not in this round.

## D3 — P2 section-D option c past the right content edge (+8.6px)

- **Evidence (pre-fix, verified on disk):** `svg/p2-leven.svg` contained
  `<text x="1473.5" y="2233" font-family="Newsreader" font-size="23">c. eten
  voor het paard van Sinterklaas</text>`. PIL measurement (Newsreader 23px):
  advance 397.1px, right edge 1870.6, content right edge 1862 → **+8.6px
  over** (matches proof1's three methods +8.5/+13.1/+11.5).
- **Root cause:** `match_set` wraps the right-side string first, then
  prepends the "c. " letter — wrap fits the bare string inside its 388.5px
  budget, but the ~23px prefix pushes the rendered line over the edge.
  Same class as fix round 1 D2 (advance estimate below true ink).
- **Fix (only `content12.py`):** `"eten voor het paard van Sinterklaas"`
  → `"eten voor Sinterklaas' paard"` (same meaning, possessive shortening;
  key c, item count, semantics unchanged). An in-content line break is not
  possible: `wrap()` only breaks at spaces and takes no manual-break token.
- **Re-measurement (rebuilt SVG, real rendered lines, PIL):**
  c "c. eten voor Sinterklaas' paard" right edge 1790.1, clearance **+71.9px**
  (gate ≥ +5px). Same-page D options re-measured: a two lines +97.8 /
  +269.4, b +45.5, d +55.5; left column 25–28 all ≥ +199. No new overflow.
  P2 card visually checked.

## D4 — text.md answer marker not localized (mechanism-level)

- **Evidence (pre-fix, verified on disk):** each of the 9 nl fan-out
  text.md files contained 150 occurrences of 「答案」 (142 single-exercise
  `— 答案：` + 8 match-item `(答案 key · …)`); core text.md has 162 lines
  containing 「答案」.
- **Root cause:** `hidden_files/w47/scratch-fanout-nl/export_fanout.py`
  hardcoded `— 答案：` in `fmt_ex` and `(答案 …)` in `fmt_match`.
- **Corrections to proof1:** (1) 「— Antwort:」 is German — it applies to
  the de reader edition only, not to the whole family; (2) core-nl (zh-cn
  reader) and nl-zh-tw (zh-tw reader) correctly use Chinese 「答案：」 and
  were NOT touched.
- **Fix:** added an `ANSWER_MARK` table to `export_fanout.py` and routed
  `fmt_ex` / `fmt_match` / the self-check regex through it:
  de `— Antwort:` / `Antwort`; en `— Correct:` / `Correct`;
  es `— Respuesta:` / `Respuesta`; fr `— Réponse:` / `Réponse`;
  it `— Risposta:` / `Risposta`; ja `— 答え：` / `答え`;
  ko `— 정답：` / `정답`; pt `— Resposta:` / `Resposta`;
  ru `— Ответ：` / `Ответ`. Match items use the bare word
  (e.g. `(Antwort c · …)`). The en form follows the existing precedent in
  the en family (`— Correct:` in en-fr / en-es / en-it / en-pt / en-nl /
  en-ru / en-ja text.md); other families carry no inline-marker precedent
  (their exporters hardcode English or have no inline marker), so the
  prescribed forms were used as given. Only the 9 text.md files were
  re-exported; no PDF was rebuilt.
- **Verification (per edition):** 「答案」 residual **0** in all 9;
  142 new exercise markers + 8 new match words each; line count 430 = 430
  unchanged; diff vs pre-re-export snapshot: exactly 300 changed lines per
  edition (150 old + 150 new), every changed line containing an old or new
  marker — no other content changed. zh-tw untouched (162 「答案」 lines,
  control). The exporter change lives in goals-side scratch (same as prior
  rounds' exporters, not committed to the repo).

## D5 — Q63 / Q126 "PSV 26 points lead the Eredivisie" has no source in this issue

- **Evidence (pre-fix, verified on disk):** core text.md line 215 (Q63
  note) and line 397 (Q126 stem + note) state PSV lead with 26 points, but
  no article, box or chart in the issue prints "PSV 26 points / leading the
  Eredivisie" (no `26 punten` anywhere in the SVGs; P4 only has Nations
  League group points; the body only gives round-12 scores Cambuur–PSV 2–5
  and Heerenveen–Feyenoord 5–3 plus the round-13 fixtures). The fact is
  externally true, but a reader cannot derive or verify the exact number
  26 from this issue — Q126's precise number could only be guessed from
  outside knowledge.
- **Fix chosen: (1) add the fact to the body** — not (2) rewrite Q126.
  Before writing, every number was verified against public sources:
  VAVEL, PitchLab, Sports Mole, Sports Oracle, TuringStats and 4 more all
  agree — after round 12 (8 Nov 2026): PSV 26 pts (1st), Feyenoord 25 (2nd),
  Ajax 25 (3rd).
- **Change (only `content34.py`):** P4 HET PROGRAMMA box gained a 5th fact:
  `"Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten."`
  (parallels the existing "Stand na 4 wedstrijden: …" fact; 2 lines, box
  +73px, P4 col3 ends 1129.6 → 1202.6, ~400px clear of the exercises rule
  at 1608). Q63's note and Q126's stem/note are unchanged — with this line
  both are now directly verifiable from the text (26 readable; 25 is
  Feyenoord's points, a live distractor; 8 is the Nations League points).
- **Re-measurement:** the line is present in the P4 SVG, in both PDFs'
  text layers and in the re-exported text.md (line 188); P4 card visually
  checked (line inside the box, clear margins). The 9 fan-out PDFs still
  lack the line — they inherit it at re-fan-out from the fixed core; not
  rebuilt in this round.

## Gates (final build, 2026-11-11)

- `run.py` exit 0: TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0; zero FLOW OVERFLOW /
  HEAD TOO WIDE warnings.
- `occlusion_audit.py svg/`: selftest OK, **0 flags**.
- Creambox check (`scratch-fix-core-nl1/check_creambox.py`, PIL true-ink
  measurement of every text inside every cream `#f0eee5` box + page-edge
  scan): **0 real overflows**. The v2 geometric scan flagged 3
  CREAM-BOTTOM lines (P2/P5/P6, ≤1.6px); a pixel probe on the rendered
  cards found 0 ink pixels in the 7px strip below each box — the flags are
  artifacts of a Latin 0.3×size descent allowance applied to CJK-only last
  lines (no descenders), identical in the pre-fix build.
- `p8.py extract --total 150`: noted set **150/150**.
- Freeze (direct sha256, clean-dir re-run of `run.py`): **8/8 MATCH**.
- P8 answer font size (PyMuPDF): min = median = **10.12pt** ≥ 9.75pt floor.
- Web vs print text layer (PyMuPDF position-sorted): all 8 pages positional
  diff 0, multiset diff 0 (tokens 751/706/665/659/686/649/736/1668 = 6,520).
  pdftotext: print 44,198 bytes, web 44,198 bytes.
- Full re-proofread of rebuilt print PDF text vs fix-round text: diff only
  14 lines — the D3 string (1 place) + the D5 line (2 lines) + pdftotext
  reading-order shifts of the same P4 sentences. P2/P4 cards viewed.
- Core text.md re-export (`export47.py`, exit 0): 44,088 bytes;
  142 + 2 + 8 = 150 exercises; 8 golden lines; 6 gloss lines. Diff vs
  pre-rebuild: only the D3 match line (line 124) and the D5 box line
  (+line 188).

## New SHAs (lowercase) + bytes

- Print PDF `De-Lucerna-VOL4.pdf`:
  `5308f4a321e6176acfe58b69b858413183093097559b6fe3bd9a50eb5bd361f8`
  (25,955,593 bytes)
- Web PDF `De-Lucerna-VOL4-web.pdf`:
  `a5f7ecba7d8436fb9173f2f468b6074e98514e316964b6e50c8cd966d6a1cfd3`
  (2,104,002 bytes)
- Core text.md `2026-w47-nl-zh-cn.text.md`:
  `2f2a650b54989e7b4b656f21cc2ae613e9dc42425a56106f03e00dff6b25d92e`
  (44,088 bytes)
- Fan-out text.md (9, marker-only re-export, 430 lines each):
  - nl-de `8e7a9935d9488306798f1eb32729ff53616c362b13b8396900b1301b44444e68`
  - nl-en `eea7dff83ae166d32e84494105132f8cda2eef7de4525749e63db8292bb62738`
  - nl-es `982d3fb694ee820fd27954cc004517b487eaf4294b567f9a05ba198afdbaee8b`
  - nl-fr `5a2275c2d535b410bf207d8a7df956b3724d9f9cc1fb0bbcb5c1d192c8784f41`
  - nl-it `4e4b505acfe00a97d36f6b0bf8e32650c4130118171011241104adf1411df3af`
  - nl-ja `a5c66d8e50746750d2ebe955dab4a793060e08251dd01be3e9b7208da10c404f`
  - nl-ko `702e12429b09648655760352f966574f4483c5b63413d2d22a9ebd861f26683a`
  - nl-pt `5686b0b8cecdf16f3df92bcad915ae8ca85a7eeedee34b45e35b9e31f2ccc033`
  - nl-ru `bb43662b68f56e072b19ba5544ae70208786775fcdfa03f3d47776c55b7d6ee1`

## Files changed (this commit)

Per the repo rule (AGENTS.md: rendered SVGs/PNGs/PDFs are reproducible
render cache, not kept in `production/`), only sources + text.md + docs are
committed. The rebuilt SVGs/cards/PDFs stay on disk for the coordinator's
insert flow; their SHAs are recorded above and in WEEKLY-KIT.md §13.

- `production/2026-w47/core-nl/content12.py` (D3)
- `production/2026-w47/core-nl/content34.py` (D5)
- `production/2026-w47/core-nl/2026-w47-nl-zh-cn.text.md`
- `production/2026-w47/core-nl/WEEKLY-KIT.md` (§13)
- `production/2026-w47/core-nl/FIX-LOG.md` (this file)
- `production/2026-w47/fanout-nl/2026-w47-nl-{de,en,es,fr,it,ja,ko,pt,ru}/2026-w47-nl-<r>.text.md`
  (D4 marker-only re-export)

Rebuilt on disk, NOT committed (render cache): `svg/p2-leven.svg`,
`svg/p4-sport.svg` (other 6 SVGs byte-identical to the fix-round build),
`cards/*.png`, `De-Lucerna-VOL4.pdf`, `De-Lucerna-VOL4-web.pdf`.

Not committed (goals-side scratch, same as prior rounds):
`hidden_files/w47/scratch-fix-core-nl1/` (logs, measurements, snapshots,
repro), `hidden_files/w47/scratch-fanout-nl/export_fanout.py` (ANSWER_MARK
change — the exporter itself lives outside the repo).
