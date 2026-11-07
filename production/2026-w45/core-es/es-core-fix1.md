# W45 ES core (VOL.2) — FIX1 log: independent-proof 5 problems fixed

**Fix agent:** 2026-10-26. Source of problems: `hidden_files/w45/es-core-independent-proof.md`
(independent proofread, verdict: 5 problems, NOT finalized).
**Scope:** only the 5 fixes below. No new articles, no new facts, no image/credit/ABSTRACT
changes (ABSTRACT untouched — it contains no Nov 12 date and no letters promise).
Nothing pushed to git, nothing posted to Discord, nobody messaged.
**Fresh full independent proof round still required after this fix** (per SOP §8.4 and the
proof report) — this log is NOT a finalization certificate.

## Build files edited (all under `hidden_files/weekly-report-w45-es-build/`)

- `content56.py` — P5 wording + P6 timeline
- `content7.py` — P7 readers' corner disclosure + preview + P7 reflow
- `content12.py` — P1 gloss
- `content8.py` — P8 answer note 123

## Fix 1 — BLOCKING: unconfirmed Nov 12 Diputación Permanente vote date, DELETED both places

- P6 timeline (`EL CAMINO AL 29N`): entry `12 NOV. — La Diputación Permanente vota
  los decretos.` removed. Timeline now runs 2 OCT → 29 NOV in 9 entries
  (3 NOV → 13 NOV directly). Box height is formula-computed, so it shrank cleanly
  (865.35 → 785.05); `LEER UNA ENCUESTA` box and the CIS chart below reflowed with
  no gap or orphan; P6 col3 now ends 1272.05, well clear of the chart at 1566.
- P7 preview (`LA PRÓXIMA SEMANA · VOL.3`): sentence `El jueves 12: la Diputación
  Permanente vota los decretos de vivienda.` removed. Preview now reads, in full:
  "El viernes 13: empieza la campaña electoral. El domingo 29: España vota. Además:
  tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!"
  (one line, no orphan; the VOL.3 letters/best-texts promise is kept because the
  parent decision for Fix 2 carries that promise to VOL.3).
- No replacement date invented. Verified in final SVGs: zero occurrences of
  `12 NOV`, `jueves 12`, `Diputación Permanente` across all 8 pages.
- KIT §6.1 debt note is SUPERSEDED by this fix: the date is no longer printed
  anywhere, so there is no VOL.3 correction to print; VOL.3 must not reintroduce
  the date unless/until a second independent source confirms it.

## Fix 2 — PROMISE GAP: W43 promise honored by ON-PAGE disclosure (parent decision, binding)

No letters or P8 texts fabricated. Inside the P7 `CARTAS DE LOS LECTORES` box itself
(not only in the KIT), after the unchanged labeled example letter, two new notes:

- Spanish: "Nota de la redacción: al cierre no había cartas reales ni los mejores
  textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.3."
- Chinese: "编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！"

The existing labeling is untouched: "— Ana (ejemplo, escrito por la redacción)" and
the example-letter text are unchanged; the old solicitation line was replaced by the
disclosure above, which keeps the call for letters (欢迎来信！).
Reflow forced by the disclosure (box grew 365.5 → 520.5 high, col3 end 1665.08 →
1820.08): the frases block is now positioned from the box end (hline 21px below it,
as before), quote row spacing tightened 158 → 128 (longest quote block is ~105px, so
23px clearance remains), and the preview box is positioned from the frases block end
(2440.08, 30px below the last quote line, 22px above the footer line at 2580).
Rendered P7 PNG viewed: disclosure fully inside the box, no overlap, no overflow,
preview box intact, footer intact.

## Fix 3 — MINOR: P5 "dos noches seguidas" corrected

P5 article closing: "…el puente, para los jóvenes, tiene dos noches seguidas." →
"…tiene dos noches grandes." (Sat Oct 31 and Sun Nov 8 are 8 days apart, not
consecutive.) No dependent exercise or note used "seguidas" for P5 (Q82 only states
"Halloween llenó las calles el sábado 31"), so no other change was needed.
P3's "tres noches seguidas de otoño" was an observation, not a counted problem, and
was deliberately left untouched per the change-nothing-else constraint.

## Fix 4 — MINOR: P8 answer note 123 corrected, key unchanged

`123. C — 国家德比与 NFL 都在周日` → `123. C — 马竞–巴萨与 NFL 都在周日`.
El Clásico is Madrid–Barça; the question is about Atlético–Barça. Key stays C.
Rendered P8 PNG viewed: note correct, answers 1–150 complete, no layout breakage.

## Fix 5 — MINOR: P1 gloss "el BOE" removed (no P1 anchor)

P1 gloss line now reads: "讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 ·
el decreto 法令 · la candidatura 候选人名单。" Removal (not re-anchoring) was chosen
because the P1 article never mentions the BOE. Verified in final P1 SVG: 0 occurrences
of "BOE"; every remaining gloss word occurs in the P1 article (la cuenta atrás in the
headline, disolvió las Cortes, decretos, candidaturas).

## Re-render + gates (all after the fixes)

- Full rebuild: `run.py` (all 5 content modules, single process) — 0 FLOW OVERFLOW /
  0 HEAD TOO WIDE warnings; exercises TOTAL 150, per-page 10/18/18/18/18/18/12/38
  (unchanged counts).
- Full re-render: `render.py` (tools/venv python) — 8 SVGs → 8 cards PNG (1950×2700) →
  `La-Lucerna-VOL2.pdf` (8 pages) + `La-Lucerna-VOL2-web.pdf` (8 pages).
- Builder re-read: every changed page/answer re-read on the rendered PNGs — P1 gloss,
  P5 closing, P6 timeline, P7 readers' corner + preview, P8 answer 123 — all correct
  as described above; no other page content changed.
- Occlusion audit: `tools/occlusion_audit.py --selftest` passed (all six planted
  classes fired, clean controls silent); full audit on the final render:
  **0 flags** (`hidden_files/w45/es-core/occlusion5.json`, `flag_count: 0`).
  No flags to adjudicate.

## Counts (final)

- Pages: 8. Exercises: 150 (unchanged). Build warnings: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE.
- Occlusion audit flags: 0. Problems fixed: 5/5. Problems that could not be made
  cleanly: none.
- Remaining step (not mine): a FRESH full independent proof round per SOP §8.4.

## What was NOT changed

Images, credits, ABSTRACT, exercise numbering/keys (except the note wording in Fix 4),
all other articles, notes, and pages. W43 files and build directory untouched.
