# COVER-KIT — W43 Weekly Cover, French readers (fr)

## Spec
- SOP 附则五 (weekly cover): 12 editions per week, one per reader language;
  this edition is for FRENCH readers. All cover-original writing (title,
  intro, explanations, headings) is in French. Headlines and excerpts stay
  in their ORIGINAL languages, verbatim.
- Masthead: "Le Lucerna" (French article convention). The cover itself
  carries NO vol number; it is marked COVER (dark-olive COVER badge on P1
  + "Le Lucerna · COVER · 19-25 octobre 2026" footer on every page).
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif (Noto Serif/Sans CJK SC, as in the FR core build).
- Week: W43, 19–25 October 2026.

## Sources (no re-extraction; no discrepancy found)
- Shared source: `hidden_files/cover-backfill/headlines-w43.json` (+ `.md`),
  12 items in FIXED order: en, de, fr, es, it, pt, nl, ru, ja, ko, zh-cn,
  zh-tw. Each item's headline + excerpt were loaded programmatically from
  the JSON into the build, so they are verbatim by construction; a
  spaceless-match check against the built SVGs confirmed 12/12 headlines
  and 12/12 excerpts (see Verification). No discrepancy vs. the JSON was
  found, so nothing was "fixed" in the source material.
- Language/masthead reference: `tools/tables.json` (fr column T_BADGE forms
  used for the source-language tags; fr gloss prefix "Note — ").
- Build patterns: FR core build dir `hidden_files/weekly-report-vol4-build/`
  — `svglib.py` COPIED into the cover build dir (never imported from the
  core dir, per the task rule). Page/frame/footer code rewritten for the
  cover (no core content modules used).
- Core mastheads + VOLs on P8, from the same JSON: The Lucerna VOL.1 (en),
  Die Lucerna VOL.1 (de), Le Lucerna VOL.2 (fr), La Lucerna VOL.1 (es),
  La Lucerna VOL.1 (it), A Lucerna VOL.1 (pt), De Lucerna VOL.1 (nl),
  Lucerna VOL.1 (ru, ja, ko, zh-cn, zh-tw).

## Layout (binding, 8 pages)
- P1: COVER badge + masthead "Le Lucerna" + week label
  "Semaine du 19-25 octobre 2026" + French cover title
  "Douze langues, une semaine d'actualités" + 2-sentence generic framing
  intro (no new facts) + 12 headline teasers in fixed order, numbered
  1–12, two columns (1–6 left, 7–12 right), source-language label +
  verbatim headline.
- P2–P7: the 12 items in full, 2 per page, fixed order — P2: EN, DE;
  P3: FR, ES; P4: IT, PT; P5: NL, RU; P6: JA, KO; P7: zh-cn, zh-tw.
  Each item: source-language tag (French name + core masthead), verbatim
  headline, verbatim excerpt, then a "Note — " explanation box IN FRENCH
  (1–2 sentences: what happened + why it matters). Every explanation
  claim is traceable to that item's headline + excerpt only; keywords are
  glossed without new facts (e.g. NL note covers only the vacation facts
  in its excerpt, not the design/dance words in its headline, which the
  excerpt does not detail).
- P8: the week's 12 core papers at a glance, fixed order: per core,
  masthead + VOL + verbatim headline, nothing invented.

## Files
- Build dir: `hidden_files/cover-w43-fr-build/` — `build.py`, copied
  `svglib.py`, `svg/` (8 SVGs), `png/` (CairoSVG render proofs).
- Edition dir (this dir): `svg/` (same 8 SVGs) + `cover-w43-fr.pdf` +
  this COVER-KIT.md.
- No git operations performed (per task).

## Verification (all gates passed)
- Visual eyeball: all 8 pages rendered with CairoSVG and inspected —
  no overflow, no cut-off text, no tofu/missing glyphs (Latin, Cyrillic,
  Japanese, Korean, Simplified + Traditional Chinese all render), no
  overlapping elements. Page content bottoms: P1 2078, P2 1920, P3–P6
  1862, P7 1952, P8 2052 (limit 2540; footer rule 2580).
- Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py svg/`
  → selftest OK (all 6 planted classes fired, clean controls silent),
  **0 flags — CLEAN**.
- Verbatim check (SVG text, spaceless match): 12/12 headlines +
  12/12 excerpts present. No VOL string on P1–P7; exactly 12 VOL lines
  on P8.
- Final PDF built ONLY with
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`:
  `cover-w43-fr.pdf`, 354,586 bytes (< 7 MB target), 8 pages,
  9,611 text bytes (non-empty text layer).
- PDF headline check: `pdftotext` + spaceless match → **all 12 headlines
  extract from the PDF**.

## Issues found + fixed
1. **U+2019 right single quote renders fullwidth in Noto CJK** — the first
   render showed a visible gap after every French apostrophe
   ("l' élection", "qu' en"). Measured: U+2019 is ~22 px wider than
   ASCII `'` at 29 pt in Noto Sans CJK SC. The shipped FR core uses ASCII
   `'` exclusively (0 × U+2019 in its P1 SVG), so all cover-original
   French text (title, intro, explanations) was switched to ASCII `'`.
   Verbatim headlines/excerpts were NOT touched — the JSON contains no
   U+2019 at all (only ASCII apostrophes), so verbatimness is unaffected.
   Re-rendered and re-checked: apostrophes now tight.
2. **P2–P7 first draft bunched at the top** (content ended ~y=1200, half
   the page empty). Fixed by starting the second item at a fixed y=1400
   with a gold separator rule, spreading both items down the page
   (final bottoms 1862–1952). No size changes needed.
3. Minor: zh-cn excerpt's final "。" wraps alone onto a second line on P7
   — verbatim wrapping, not a cut-off; left as is.
4. **P7 zh-tw French explanation: wrong typhoon name (fix, 2026-10-28)** —
   OLD: "Le typhon puissant Changpi s'approche des eaux à l'est de
   Taïwan" — NEW: "Le typhon puissant Jangmi s'approche des eaux à
   l'est de Taïwan". Authority: the zh-tw core's own P1 SVG
   (`weekly-report-zhtw-vol1/svg/p1-front.svg`) names the storm
   "Jangmi" (強烈颱風「薔琵」); "Changpi" was a blend of Champi (the
   DIFFERENT ko-item storm, correctly kept on P6) and Jangmi. Only this
   one word changed, in the build source
   (`hidden_files/cover-w43-fr-build/build.py`, zh-tw EXPL entry); the
   rest of the explanation is unchanged, and the verbatim zh-tw headline
   and excerpt (Traditional characters) were NOT touched. SVGs
   regenerated via `build.py` and copied to the edition dir; page
   bottoms unchanged (P1 2078, P2 1920, P3–P6 1862, P7 1952, P8 2052).
   Re-verification after the fix: occlusion audit 0 flags (selftest
   OK); PDF rebuilt ONLY with `webpdf.py` → `cover-w43-fr.pdf`,
   354,589 bytes (< 7 MB), 8 pages, 9,610 text bytes (non-empty text
   layer); `pdftotext` check → 12/12 headlines extract, "Jangmi"
   present, "Changpi" absent. No git operations performed (per task);
   the coordinator makes the fix commit.
