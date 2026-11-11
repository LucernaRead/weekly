# FIX-LOG — core-nl fix rounds 2–3 (2026-11-11)

## Fix round 3 — D6/D7 orphan 。 (2026-11-11)

Core-nl reopened after independent re-proof (proof2,
`hidden_files/w47/scratch-proof-core-nl2/PROOF-NOTE.md`, conclusion (b)):
fix2's D3/D4/D5 all regressed PASS, 150 exercises, 16 mechanical gates,
all external facts PASS — but 2 new defects of the same class (both
pre-existing fix-round leftovers missed by proof1, NOT introduced by
fix2). Scope: D6 + D7 only. No wording, key, or fact changed anywhere;
only the two line breaks moved. Fan-out editions NOT rebuilt in this
round (nl re-fan-out is rebuilding 10 editions from the fix2 core in
parallel — coordinator to schedule the fix3 incremental rebuild).

### D6 — P3 trailing 。 alone on its own line (section C, HET PERFECTUM bridge)

- **Evidence (pre-fix, verified on disk):** `svg/p3-cultuur.svg`:
  bridge `用现在完成时补全，注意助动词 hebben/zijn` (x=538.5, y=2250.5,
  20.5px), then `。` alone in its own `<text>` (x=538.5, y=2280.225) —
  the only character on the line. Print-PDF crop in proof2
  `render/crop-p3-orphan.png`. text.md carries the sentence on one line
  with its 。 (the wrapper ejected it at the SVG layer).
- **Root cause:** the greedy `wrap()` at the full column width (422.5px)
  happens to push the final `。` onto a second line by itself.
- **Fix:** `bslib4.py`: `Flow.para` / `Flow.bridge` take a new optional
  `w` parameter (wrap-width override; default = column width, so every
  existing call is unaffected). `content34.py`: that one bridge call
  passes `w=CW - 40` (382.5px). Width scan: every width in 300–405px
  wraps to the same two lines
  `用现在完成时补全，注意助动词 / hebben/zijn。`; 382.5px sits 22.5px
  below the 405px threshold. Still 2 lines — no downstream y shift.
- **Re-measurement (rebuilt SVG):** lines are
  `['用现在完成时补全，注意助动词', 'hebben/zijn。']`; the orphan is
  gone. Print-PDF crop `render/crop-p3-fixed.png` confirms visually.

### D7 — P7 trailing 。 alone on its own line (A2 VOETBALWOORDEN gloss bridge)

- **Evidence (pre-fix, verified on disk):** `svg/p7-taal.svg`:
  `；de kwartfinale 四分之一决赛；scoren 进球` (x=88.0, y=755.385,
  20.5px), then `。` alone in its own `<text>` (x=88.0, y=785.11).
  Print-PDF crop in proof2 `render/crop-p7-orphan.png`.
- **Root cause:** same as D6.
- **Fix:** `content7.py`: that one bridge call passes `w=CW - 35`
  (387.5px). Width scan: every width in 377.5–395px wraps to the same
  three lines `de wedstrijd 比赛；de groepswinst 小组 / 头名；de kwartfinale
  四分之一决赛； / scoren 进球。`; 387.5px is the middle of the band.
  Still 3 lines — no downstream y shift.
- **Re-measurement (rebuilt SVG):** last line is `scoren 进球。`; the
  orphan is gone. Print-PDF crop `render/crop-p7-fixed.png` confirms
  visually.

### Full-edition orphan-punctuation sweep (rebuilt SVGs, all 8 pages)

`<text>` elements grouped by baseline y (a lone character counts as an
orphan only if it owns its whole baseline):

- Lone `。`: **0** on all 8 pages.
- Lone closing quotes `» ” ’ ） 」 》`: **0** on all 8 pages.
- Lone `：` / `–`: **0** as well.
- P8's 7 lone `）` `<text>` elements each share their baseline with 4–6
  siblings — answer-zone inline locators, not orphans (excluded, same as
  proof2).

### Side note: exporter stub (goals-side tool, not committed)

`scratch-nl/stub_bslib47.py` (the recording stub `export47.py` runs the
content files against) overrode `Flow.para`/`Flow.bridge` without `w`,
so the first text.md re-export died with
`TypeError: Flow.para() got an unexpected keyword argument 'w'`. Added
`w=None` pass-through to both overrides (signature compatibility only;
exported text unaffected). Re-export then exited 0 and produced a
byte-identical text.md.

### Fix-round-3 gates (final build, 2026-11-11)

- Build: `run.py` exit 0, TOTAL 150, by page 10/18/18/18/18/18/12/38,
  A2 46 / B1 73 / B2 31; `render.py` exit 0, zero FLOW OVERFLOW / HEAD
  TOO WIDE warnings. SVG hashes: only `p3-cultuur.svg` and
  `p7-taal.svg` changed; the other 6 are byte-identical to fix2.
- `occlusion_audit.py svg/`: selftest OK, **0 flags**.
- Creambox check (same `check_creambox.py` as fix2): same 3 CREAM-BOTTOM
  flags (P2/P5/P6, ≤1.6px); 7px strip below each box bottom probed
  pixel by pixel on the card PNGs: **0 non-paper pixels** — all three
  are the known false positives (CJK last line measured with a Latin
  0.3×size descender allowance), same as proof2. **True overflow 0.**
  (Note: my full-width band scan for P6 bottomed at 664.44 because the
  cream fill itself trips the non-paper threshold; proof2's narrower
  glyph scan gave ink bottom 661.4, clearance +3.6px. The decisive
  below-box strip probe agrees in both rounds: 0 ink.)
- `p8.py extract --p8 svg/p8-toets.svg --total 150`: noted set **150/150**.
- P8 keys vs text.md (proof2's `step3b_p8compare.py`, rerun unmodified
  except the scratch path): output **byte-identical to proof2's own run**
  — the 8 "mismatches" are all match items 25–28/141–144 whose text.md
  answers live on range-header lines (parser yields None); the match
  keys themselves agree: 25–28 = d/c/a/b, 141–144 = b/c/d/a. text.md
  is byte-identical to fix2 and the P8 keys match the proof2-verified
  set, so the 150 keys needed no fresh hand-check (nothing changed).
- Freeze (direct sha256, clean-dir re-run of `run.py`): **8/8 MATCH**.
- P8 answer font size (PyMuPDF): min = **10.12pt** ≥ 9.75pt floor.
- Web vs print text layer (PyMuPDF position-sorted): all 8 pages
  positional diff 0, multiset diff 0 (tokens 760/715/673/671/700/659/
  738/1685 = 6,520). pdftotext: print 44,197 bytes, web 44,197 bytes.
  (1 byte less than fix2's 44,198: the D6 reflow drops the single space
  that separated 助动词 from hebben/zijn — fix2's line 1 ended with
  "…助动词 hebben/zijn" (55B incl. that space) and the orphan "。" (4B);
  fix3's lines are 43B + 15B. The D7 hunk is byte-neutral (107B = 107B).
  The print-text diff vs fix2 shows exactly the two reflowed passages
  and nothing else.)
- D3 regression re-measured (proof2's `step3_gates.py`): P2 D-option
  true-ink clearances identical to proof2 (c +71.5, a +97.5, b +44.5,
  d +55.5; left 25–28 +278.5/+285.5/+208.5/+265.5). Quote sweep:
  ASCII `"` 0, backtick 0, `« »` paired on P1/P2/P7/P8, `“ ”` only the
  P1 pair. Golden lines 8/8 verbatim in body; Q150 model 81 words
  (80 excluding the standalone `–`), within 80–100.
  (Two pre-existing quirks in proof2's `step3_gates.py`, same in its
  own run: it crashes after the quote section on `re.findall(..., md)`
  where `md` is a list — the golden-lines section was re-run separately
  (`golden-fix3.txt`, 8/8); and its embedded p8-extract subsection
  reports noted set 0 because it omits `--json` — the standalone
  `p8.py extract` (150/150) is authoritative.)
- Core text.md re-export (`export47.py`, exit 0): 44,088 bytes,
  **byte-identical to fix2** (SHA `2f2a650b…b25d92e` unchanged); 432
  lines; 142 + 2 + 8 = 150 exercises; 8 golden lines; 6 gloss lines.
- Print PDF viewed page by page (PyMuPDF self-render 1.5×,
  `render/p1–p8.png`): P1/P2/P4/P5/P6/P8 clean; P3/P7 fixed spots
  confirmed by crops. No new findings. (Pre-existing proof2 N3 — P7
  VOLGENDE WEEK dark band tight to its last line — unchanged, out of
  scope for this round.)

## New SHAs (lowercase) + bytes — fix round 3

- Print PDF `De-Lucerna-VOL4.pdf`:
  `82427d3f80af23588726311dd415ff9caefe0cc153dc3b3637444babd4bc9eb7`
  (25,955,581 bytes)
- Web PDF `De-Lucerna-VOL4-web.pdf`:
  `44553e5c77d3fbf796939fc35bc43721292e44f1669253cd23fc76c47bcd5a39`
  (2,103,999 bytes)
- Core text.md `2026-w47-nl-zh-cn.text.md`:
  `2f2a650b54989e7b4b656f21cc2ae613e9dc42425a56106f03e00dff6b25d92e`
  (44,088 bytes — **unchanged from fix2**)

## Files changed (this commit, fix round 3)

Per the repo rule (AGENTS.md: rendered SVGs/PNGs/PDFs are reproducible
render cache, not kept in `production/`), only sources + text.md + docs
are committed. The rebuilt SVGs/cards/PDFs stay on disk for the
coordinator's insert flow; their SHAs are recorded above and in
WEEKLY-KIT.md §14.

- `production/2026-w47/core-nl/bslib4.py` (`w` wrap-width override on
  `Flow.para`/`Flow.bridge` — mechanism for both fixes; **first added
  to the repo in this commit**, previously untracked on disk)
- `production/2026-w47/core-nl/content34.py` (D6 call site)
- `production/2026-w47/core-nl/content7.py` (D7 call site — **first added
  to the repo in this commit**, previously untracked on disk; same
  precedent as fix2 first adding `content12.py`/`content34.py`)
- `production/2026-w47/core-nl/WEEKLY-KIT.md` (§14)
- `production/2026-w47/core-nl/FIX-LOG.md` (this file)

Unchanged, not in this commit: `content12.py` (D3 fix2 intact),
`2026-w47-nl-zh-cn.text.md` (byte-identical). Rebuilt on disk, NOT
committed (render cache): `svg/p3-cultuur.svg`, `svg/p7-taal.svg`
(other 6 SVGs byte-identical to the fix2 build), `cards/*.png`,
`De-Lucerna-VOL4.pdf`, `De-Lucerna-VOL4-web.pdf`. Fan-out text.md/PDFs
NOT rebuilt in this round — coordinator's fix3 incremental rebuild.

Not committed (goals-side scratch, same as prior rounds):
`hidden_files/w47/scratch-fix-core-nl3/` (logs, measurements, renders,
gates), `hidden_files/w47/scratch-nl/stub_bslib47.py` (the `w`
pass-through — the exporter stub lives outside the repo).

---


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
