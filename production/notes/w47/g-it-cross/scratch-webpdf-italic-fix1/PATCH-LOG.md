# PATCH-LOG — webpdf italic fix (D3), 2026-W47 ru-en

- Date: 2026-11-11 (UTC ~09:05–09:25)
- Executor: webpdf italic-fix agent (subagent, depth 2)
- Scope: `tools/webpdf.py` ONLY (one file) + rebuild of `Lucerna-VOL4-ru-en-web.pdf` ONLY.
  No edition source, no print PDF, no other tool touched. No git write of any kind
  (no add/commit/push/stash/reset, no `insert.py`, no `lint --write`). Commit left to
  the coordinator.
- Pre-existing working-tree state (NOT mine, untouched): `tools/freeze.py`,
  `tools/occlusion_audit.py`, `tools/p8.py` modified by other agents (mtimes
  2026-11-10 21:37 – 2026-11-11 05:01 UTC, before this session); ~149 dirty entries
  in `issues/2026-w43/` etc. Only `tools/webpdf.py` (mtime 09:10 UTC) is mine.

## 0. Probes (before every write step)

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb…`,
  RC=0, before each write (start, patch edits, rebuild, KIT edit, logs). Real-write
  probe file in this scratch dir written OK each time. No EDQUOT encountered
  (disk quota did not fire during this task; `df` showed 78G free on `/home`).

## 1. Defect (D3 — proof 2, web PDF only; print PDF zero defects)

P1 WORD OF THE WEEK box, line «чёрная пятница» (SVG `p1-pervaya.svg`, y=1712;
the edition's ONLY italic text — 5 `font-style="italic"` `<text>` runs, all on P1):
- (a) space glyph missing in web text layer: `'чёрнаяпятница'` (print has the space;
  whole-edition char count 35,197 vs 35,198; pdftotext 57,148 vs 57,149).
- (b) closing » detached: x1 deficit 3.354 pt (> 0.5 pt).
- (c) italic lost: web LucernaNotoSerif-Regular (+ LucernaNewsreader-Regular),
  print NotoSerif-MediumItalic + Newsreader16pt-Italic.
- Root cause class: tool face-resolution defect, same class as D2 (weight) —
  `tools/webpdf.py` contained ZERO italic handling (`grep -i italic|slant|oblique`
  → 0 hits); `fc_match` varied only weight.

## 2. Mechanism — verified by measurement, and it CORRECTS the brief's (a) theory

The brief said (a) is fixed by making sure U+0020 is in the subset charset.
That is necessary but NOT sufficient, and NOT the actual mechanism. Measured:

1. `collect_chars_and_families` on the ru-en SVGs: U+0020 IS already in the union
   (155 distinct chars), and every subset built by the pre-patch tool contains
   U+0020 in its cmap (checked with fontTools: LucernaNewsreader-Regular 88 glyphs,
   U+0020 present). The subset was never the gap.
2. CairoSVG never draws a whitespace letter at all — `cairosvg/text.py`:
   `# Only draw characters with 'content' (workaround for bug in cairo)` /
   `if not letter.isspace(): show_text(letter)`. So NO space glyph exists in
   EITHER PDF (print is also rendered by CairoSVG, `render.py` `svg2pdf`).
   Minimal repro (own SVG, full system fonts AND subset fonts): a standalone
   `<text> </text>` run emits no span in either case; positioning of the next run
   is preserved (matches the D3 symptom exactly).
3. The print "space" is extractor gap-synthesis: PyMuPDF/pdftotext inserts a space
   when the gap between adjacent chars is space-like. Print's italic gap
   'я'→'п' = 2.532 pt (0.157 × 16.12 pt font) synthesizes; web's upright gap =
   1.177 pt (0.073 ×) does not. All other standalone spaces in the edition agree
   print-vs-web because their upright advances are identical in both pipelines.
4. Therefore the (a) fix is the italic face itself: correct italic advances restore
   the 2.532 pt gap, and the space reappears in extraction. Verified post-rebuild:
   web space bbox [1145.576, 1266.762, 1148.108, 1288.725] == print, byte for byte.
5. Oblique: `fc-match 'Noto Serif:weight=100:slant=oblique'` → NotoSerif-MediumItalic,
   `'Newsreader:…:slant=oblique'` → Newsreader-Italic. Oblique requests resolve to
   the italic faces, so no separate oblique face is needed. This edition has 0
   oblique runs (grep 0 hits).

## 3. Verification of face resolution (before patching the build)

- `fc-match 'Noto Serif:weight=100:slant=italic'` → `NotoSerif-MediumItalic.ttf`
  (the exact print face); `'Newsreader:weight=100:slant=italic'` →
  `Newsreader-Italic.ttf` (exact print face); weight=200 + slant=italic →
  NotoSerif-BoldItalic / Newsreader-Italic (Newsreader has no Bold Italic).
- Standalone `build_subsets` run with the patched code: 16 subsets — Newsreader 3
  (Regular/Bold/Italic; Bold Italic deduped), Noto Sans 4, Noto Serif 4,
  CJK families 2 each (italic deduped to Regular/Bold), UnifrakturMaguntia 1.
  All contain U+0020; italic faces advertise OS/2 italic bit + macStyle 2 +
  name ID 2 Italic/Bold Italic.
- Isolated-fontconfig check of the built subsets: `LucernaNotoSerif:weight=100:
  slant=italic` → LucernaNotoSerif-Italic.ttf; `LucernaNewsreader:…:slant=italic`
  → LucernaNewsreader-Italic.ttf; `:slant=oblique` → the Italic subset;
  upright/bold requests unchanged (Regular/Bold). D2 faces untouched.

## 4. The patch (`tools/webpdf.py`, diff vs HEAD — includes the uncommitted D2 weight patch already in the working tree; my lines are the italic ones)

- Module docstring step 2: bold AND italic variants get their own subsets; weight
  and slant are orthogonal axes (up to 4 faces per family, deduped).
- `collect_chars_and_families`: `chars.add(' ')` — guarantees U+0020 in every
  subset charset (D3(a) guard; no-op for this edition since the space is already
  in the union, so it changes no subset bytes here).
- `fc_match(family, bold=False, italic=False)`: appends `:slant=italic` when
  italic. Docstring records D3 evidence (faces resolved, oblique fallback).
- `subset_font(..., italic=False)`: file stem / PostScript name use spaceless tag
  (`BoldItalic`); name ID 2 set to the subfamily ONLY for italic faces
  (non-italic faces keep their inherited ID 2 — D2-proven behaviour, do not touch:
  e.g. Newsreader-SemiBold's ID 2 is "Regular"); sets OS/2 italic bit (0x01),
  clears REGULAR bit (0x40) when italic, sets head macStyle italic bit (0x02)
  (clears both when upright).
- `build_subsets`: iterates the 4 variants (Regular, Bold, Italic, Bold Italic);
  skips a variant whose `fc_match` equals an already-built face for the family
  (replaces the old bold-only skip, which called `fc_match` twice per family).
  Docstring records the D3(a) mechanism correction (CairoSVG `isspace` skip +
  gap-synthesis) so the next reader does not re-derive the wrong theory.
- No other line touched. `python -c "ast.parse(...)"` → SYNTAX OK.

## 5. Rebuild (web PDF only)

```
cd production/2026-w47/2026-w47-ru-en
tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-ru-en-web.pdf   # RC=0
WROTE Lucerna-VOL4-ru-en-web.pdf: 3375060 bytes, 57149 text bytes
```

| PDF | Before | After | SHA-256 after |
|---|---|---|---|
| print `Lucerna-VOL4-ru-en.pdf` | 21,245,374 B, `7b73070c2c11313a…` | UNTOUCHED, same bytes + SHA | `7b73070c2c11313a7b7cd6ec714174bffc105fe5f595d99ef32c434e76d2885e` |
| web `Lucerna-VOL4-ru-en-web.pdf` | 3,367,620 B, `82dfb6eaeff6eaa7…` | **3,375,060 B** (+7,440 B, +0.22%) | `6419f7ad188d0e6aca09ae76abc739e954d0d6e1d5249171c34376e6b61360b6` |

- Full build log: `webpdf-build.log` in this dir. New subsets in the build log:
  LucernaNewsreader-Italic, LucernaNotoSans-Italic, LucernaNotoSans-BoldItalic,
  LucernaNotoSerif-Italic, LucernaNotoSerif-BoldItalic (other faces byte-identical
  sizes to the weight-patch build).

## 6. KIT update (ru-en only)

`production/2026-w47/2026-w47-ru-en/WEEKLY-KIT.md`:
- §5: new web PDF size/SHA; pdftotext 57,149 = print, `diff` 0; new italic-patch
  paragraph; character-multiset line corrected (35,198 chars each).
- §7: "Print/web text layer" line corrected — the old "character multiset identical
  (30,293 chars each)" claim was WRONG pre-fix (off by exactly one U+0020, D3(a));
  the 1,704-pair abutting-scan claim corrected too (its line-key matcher dropped the
  D3 pair because of the italic overhang); new "Webpdf italic patch APPLIED" record
  with the D3 fix, the mechanism correction, and the re-run gates.
- No other KIT touched. No `lint --write`, no index.json touch.

## 7. What this patch does NOT do

- No edition source change, no SVG change, no print re-render.
- No change to the upright/bold faces' resolution (D2 behaviour preserved —
  verified: all 7 D2 spots still 0.00 pt, see GATE-LOG.md).
- No handling of `font-style` values other than italic/oblique (none occur in this
  edition; oblique is covered by fontconfig fallback, verified in §3).
