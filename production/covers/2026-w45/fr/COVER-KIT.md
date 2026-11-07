# COVER-KIT — W45 Weekly Cover, French readers (fr)

## Spec
- SOP 附则五 (weekly cover): 12 editions per week, one per reader language;
  this edition is for FRENCH readers. All cover-original writing (title,
  intro, explanations, headings) is in French. Headlines and excerpts stay
  in their ORIGINAL languages, verbatim.
- Masthead: "Le Lucerna" (French article convention). The cover itself
  carries NO vol number; it is marked COVER (dark-olive COVER badge on P1
  + "Le Lucerna · COVER · 2-8 novembre 2026" footer on every page).
- 8 pages, 1950×2700, weekly visual system: warm ivory #f7f1e2, deep olive
  accents, serif (Noto Serif/Sans CJK SC, as in the FR core build).
- Week: W45, 2–8 November 2026.

## Sources (no re-extraction; no discrepancy found)
- Shared source: `hidden_files/cover-backfill/headlines-w45.json` (+ `.md`),
  12 items in FIXED order: en, de, fr, es, it, pt, nl, ru, ja, ko, zh-cn,
  zh-tw. Each item's headline + excerpt were loaded programmatically from
  the JSON into the build, so they are verbatim by construction; a
  tag-stripped spaceless-match check against the built SVGs confirmed
  12/12 headlines and 12/12 excerpts (see Verification). JSON vs `.md`
  cross-check also confirmed all 12 headlines and all 12 excerpts present
  in both. No discrepancy vs. the JSON was found, so nothing was "fixed"
  in the source material.
- W45 VOLs (verified against the JSON, matching the task spec): FR VOL.3,
  all other 11 cores VOL.2.
- Language/masthead reference: `tools/tables.json` (fr column T_BADGE forms
  used for the source-language tags; fr gloss prefix "Note — ").
- Build patterns: FR core build dir `hidden_files/weekly-report-vol4-build/`
  — `svglib.py` COPIED into the cover build dir (identical to the W43 FR
  cover's copy; never imported from the core dir, per the task rule).
  Page/frame/footer code adapted from the W43 FR cover build (same layout,
  W45 week/title dates). No core content modules used.
- No git operations performed (per task).

## Layout (binding, 8 pages)
- P1: COVER badge + masthead "Le Lucerna" + week label
  "Semaine du 2-8 novembre 2026" + French cover title
  "Douze langues, une semaine d'actualités" + 2-sentence generic framing
  intro (no new facts) + 12 headline teasers in fixed order, numbered
  1–12, two columns (1–6 left, 7–12 right), source-language label +
  verbatim headline.
- P2–P7: the 12 items in full, 2 per page, fixed order — P2: EN, DE;
  P3: FR, ES; P4: IT, PT; P5: NL, RU; P6: JA, KO; P7: zh-cn, zh-tw.
  Each item: source-language tag (French name + core masthead), verbatim
  headline, verbatim excerpt, then a "Note — " explanation box IN FRENCH
  (1–2 sentences: what happened + why it matters). Every explanation
  claim is traceable to that item's headline + excerpt only; keyword
  glosses add no article facts (e.g. KO note glosses kimjang as the
  kimchi preparation for winter; the NL note covers only the excerpt's
  climate-week actions, not the headline's museum/football words, which
  the excerpt does not detail).
- P8: the week's 12 core papers at a glance, fixed order: per core,
  masthead + VOL + verbatim headline, nothing invented (FR VOL.3, all
  others VOL.2).

## Files
- Build dir: `hidden_files/cover-w45-fr-build/` — `build.py`, copied
  `svglib.py`, `svg/` (8 SVGs), `png/` (CairoSVG render proofs).
- Edition dir (this dir): `svg/` (same 8 SVGs) + `cover-w45-fr.pdf` +
  this COVER-KIT.md.

## Verification (all gates passed)
- Visual eyeball: all 8 pages rendered with CairoSVG and inspected —
  no overflow, no cut-off text, no tofu/missing glyphs (Latin, Cyrillic,
  Japanese, Korean, Simplified + Traditional Chinese all render), no
  overlapping elements. Page content bottoms: P1 2122, P2 2056, P3 1906,
  P4 1999, P5 1862, P6 1906, P7 1952, P8 2052 (limit 2540; footer rule 2580).
- Occlusion audit: `tools/venv/bin/python tools/occlusion_audit.py svg/`
  → selftest OK (all 6 planted classes fired, clean controls silent),
  **0 flags — CLEAN**.
- Verbatim check (SVG text elements, tag-stripped spaceless match):
  12/12 headlines + 12/12 excerpts present. No VOL string on P1–P7;
  exactly 12 VOL lines on P8.
- Final PDF built ONLY with
  `tools/venv/bin/python tools/webpdf.py <svg-dir> <out.pdf>`:
  `cover-w45-fr.pdf`, 344,301 bytes (< 7 MB target), 8 pages,
  10,672 text bytes (non-empty text layer).
- PDF headline check: `pdftotext` + spaceless match → **all 12 headlines
  extract from the PDF**.

## Issues found + fixed
1. **CairoSVG renders Latin serif text wider than the PIL measure** —
   the first render showed full-width excerpt lines overflowing the right
   frame edge on P2–P5 (EN, FR, ES, IT, NL excerpts clipped at the frame;
   e.g. P2 EN "Senate and governorships in many states." ran past the
   border). Fix: item headline/excerpt wrap width reduced from W to
   W-120 (1820 → 1700) and note-box wrap from W-60 to W-120, in
   `item_block` only (P1 teasers and P8 were already inside the frame and
   are unchanged). Re-rendered and re-inspected: all lines now end
   inside the frame with margin; content bottoms still ≤ 2056.
2. **French accents vs. apostrophes** — the first draft of the
   explanations dropped accents entirely; corrected to full accented
   French, keeping ASCII `'` apostrophes only (0 × U+2019 in the build
   source, verified by count; the W45 JSON itself contains no U+2019, so
   verbatim headlines/excerpts are unaffected). Re-rendered: apostrophes
   tight, no fullwidth gaps.
3. Preflight: `hidden_files/cover-w45-fr-build/` did not exist at task
   start (no active work in the last ~30 minutes), so the build proceeded
   rather than standing down. Sibling W45 EN/DE cover builds were active
   concurrently but in their own dirs; this build touched only the FR
   build dir and the FR edition dir.
