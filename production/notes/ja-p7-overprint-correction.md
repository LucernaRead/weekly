# JA core P7 overprint — correction cycle record

Opened 2026-10-21 (evening) by the main line, from the JA×PT independent proofread escalation (KIT §13 of files/weekly-report-ja-pt/).

## Defect
In the JA core's P7 vocabulary deck, two level-column seams have REAL glyph overprints (not audit artifacts): frozen Japanese lines wrap past the 434-unit column pitch and overprint the neighbour column's first glyph, producing illegible merged glyphs.
- Seam (a): y=336.86 — B1 column (x=527) line ending …スタジアムで大き vs B2 column (x=989) という意味です…; ink overlap ≈30 units （き/と superimposed).
- Seam (b): y=369.54 — A2 column (x=65) line ending …季節で vs B1 column (x=527) な声…; overlap ≈9 units.
Pixel proof of inheritance: rendered-card strips hash-identical between core and JA×PT (55ab31e7…, fc5a4895…, wider crop 4b71a2ea…). Present in the JA core and every shipped JA fan-out (ja-en, ja-de, ja-fr, ja-es, ja-it, ja-pt). Earlier builders adjudicated these flags as "clean columns" — that adjudication is WRONG and superseded by the JA×PT proofread.

## Fix plan (geometry only, content byte-identical)
1. Patch the JA core build's P7 wrap metrics so no vocab line crosses a column seam; re-render the core; geometric audit must show the two TEXTX flags gone and no other page changes.
2. Apply the identical code patch to the 6 shipped fan-out build dirs; re-render each; geometry-focused verification per edition (P7 seams clean; diff vs shipped = P7 seam lines only).
3. Main line re-pins all 7 editions in LucernaRead/weekly with dated correction notes in each md body (repo rule: corrections via new PDF + pin update + note).
4. JA fan-outs not yet built (ja-nl, ja-ru, ja-ko, ja-zh-cn, ja-zh-tw) MUST be built from the patched core build.

## Status — CLOSED 2026-10-21 (evening)
- Diagnosis: the kinsoku oidashi loop in `svglib.py wrap()` pulled glyphs without re-measuring (B1 line +57.92 units over the 434 limit; A2 +37.28). Census: 16 overfull lines in the core, only these 2 cross the 28-unit gutter.
- Patch: `SEAM_SLACK = 28` seam-repair pass in wrap(); identical patched svglib.py (md5 d73e23b3…) in the core + all 6 fan-out build dirs — future JA builds copying the core build inherit it.
- Verification (all 7 editions): pages 1–6/8 byte-identical; P7 differs only in the 4 seam text elements; the 2 TEXTX flags gone, 0 new; seams now have 31 / 25 clear columns.
- Repo: all 7 editions re-pinned 2026-10-21 with dated correction notes in each md body (commits 08db975…f7a4eed; remote main = f7a4eed, lint --require-pdf green at 75).
- **PATCH COMPLETE (2026-10-21, patch agent).** Diagnosis: the wrap metric was correct; the kinsoku oidashi loop in `svglib.py wrap()` never re-measures the receiving line, and NO_START chains (』!。) cascaded 3 pulls into the B1 line (491.92 vs limit 434) and 2 pulls into the A2 line (471.28). Fix: `SEAM_SLACK = 28` constant + a seam-repair pass in `wrap()` that sheds trailing glyphs forward ONLY for lines oidashi grew past max_w + SEAM_SLACK, until they fit max_w. Identical patched `svglib.py` (md5 d73e23b365676c3618d7e060b835eb4d) in the core build and all 6 fan-out builds; all 7 editions re-rendered.
- Verification (all 7 editions, uniform): pages 1–6/8 SVGs byte-identical; P7 differs in exactly the 4 seam-line text elements at unchanged coordinates; concatenated text identical on all pages; registry 150 unchanged; ink-extent audit (positive control passed): exactly the 2 P7 TEXTX flags removed, 0 new flags (core 19→17 · en 20→18 · de 22→20 · fr 28→26 · es 23→21 · it 24→22 · pt 24→22); pixel check on every P7 card: seam (a) 31 clear columns (ink 962 | 994), seam (b) 25 clear columns (ink 502 | 528).
- Dated patch note with old → new pins appended to all 7 WEEKLY-KIT.md files. Verification workspace: hidden_files/ja-p7-fix/ (pre-patch snapshots, census, audit.py).
- Note for re-pin: the JA×PT proofreader was still running in parallel and re-rendered ja-pt in place twice (content verified identical each time); web-PDF sha256 embeds a render timestamp, so if ja-pt is rendered again before re-pinning, re-measure its pin at re-pin time. SVG state is stable and verified.
- Repo re-pins pending (main line).
