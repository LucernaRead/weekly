# GATE LOG — Lucerna Weekly 2026-W47 · en-it · proof2 (post-delta)

**Date:** 2026-11-11 · **Proofreader:** independent proof2 · **Conclusion: (a) zero defects (see PROOF-NOTE.md)**
**Scratch:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-it2/`
**Edition:** `~/workspace/weekly-git/production/2026-w47/2026-w47-en-it/`
**Core:** `~/workspace/weekly-git/production/2026-w47/core-en/`
**Delta reference:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-en-it/DELTA-NOTE.md`
**Proof1 reference:** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-it1/` (conclusion (a) PROVISIONAL, pending this round)

## 0. Probes (before work)
- `ls /dev/null` → present. `touch /dev/null` fallback not needed.
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` ✓
- Write probe in goals-side scratch (`probe.txt`) ✓. TMPDIR=`<scratch>/tmp` throughout; `/tmp` avoided (except one tool-output spill file created by the runtime, not by me).
- Disk at start: 62G available.
- Repo AGENTS.md (`~/workspace/weekly-git/AGENTS.md`) read before further work in the clone: no conflict — this round is read-only proof, no commits, tools run from `tools/venv/bin/python`.

## 1. SHA verification — all MATCH (before and after)
Print PDF `The-Lucerna-VOL4-en-it.pdf`: 29,327,187 B, SHA-256 `2db4dad1496e474fbd01315bf3b7f8393358a60155ce103f6a8bae476a5502a0` ✓
Web PDF `The-Lucerna-VOL4-en-it.web.pdf`: 2,408,879 B, SHA-256 `570eef4fb1174edb33e3e46c324d96231dac086140a34e1e7376929a41525239` ✓
text.md `2026-w47-en-it.text.md`: 53,944 B, SHA-256 `a833062570765ad5fea4e1f2a4ac4396afd28f2376bb86dbeb9991eae9e2f464` ✓
Both PDFs 8 pages, 1462.5 × 2025 pts. Re-measured after all proof work: identical.
Core-en before/after (unchanged, matches delta note §7.3): print `08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213`, 41,407,287 B; text.md 51,402 B. `git status` on both production dirs: only `??` (untracked) — no production file written by this round.

## 2. Delta independently re-verified (delta scratch `pre/` vs production)
- Registry pre vs production: exactly **1** diff — n=73 key `'speak'` → `'up'`, note identical.
- text.md pre vs production: exactly **1** differing line (1151): `73. [A2] Completare le frasi — speak (…)` → `— up (…)`. `wc -l` 1305 both.
- SVG SHA pre vs production: p1–p7 byte-identical; only `p8-test.svg` changed (`2060db36…` → `ba31ef73…`). P5 unchanged = correct expected (§7 correction in DELTA-NOTE).
- `content56.py:49` key `"up"`; P5 SVG: `Speak ___` ×1, `to speak up` ×2; P8 SVG contains `73. up` (byte offset 1228433).
- Registry Q73: `{'n': 73, 'page': 5, 'level': 'A2', 'type': 'Completare le frasi', 'key': 'up', 'note': 'speak up = parlare senza paura'}`; core-en Q73 key `'up'`, note `'speak up = 大声说出来'`.

## 3. Reproducibility — print PDF byte-identical from scratch copy
Copied the edition dir to `proof-copy/` and re-ran `run.py` + `render.py` there (repo venv python).
- `run.py` RC=0; 0 OVERFLOW / TOO WIDE; flows all within bottoms (P8-keys 2443/2560); TOTAL 150; MODEL 82. Log: `gates/run.log`.
- `render.py` RC=0; print PDF 29,327,187 B. Log: `gates/render.log`.
- Re-rendered print PDF SHA-256 = `2db4dad1496e474fbd01315bf3b7f8393358a60155ce103f6a8bae476a5502a0` — **byte-identical to production**. All 8 SVGs MATCH production byte-for-byte (`gates/svg-sha256-recopy.txt` vs `gates/svg-sha256-prod.txt`, `diff` clean).

## 4. Registry re-dump — identical
Repointed copy of `dump_reg.py` (`gates/dump_reg_proof.py`: `os.chdir` → proof-copy, output → `gates/registry-redump.json`; the edition's own script hardcodes its output to the shared fanout scratch, so running it unmodified would have overwritten that archive) RC=0; re-dumped registry == production `registry.json` (`cmp` clean; 150 entries; per page 10/17/18/18/18/18/12/39; A2 62 / B1 66 / B2 22). Files: `gates/dump_reg.log`, `gates/registry-redump.json`, `gates/dump_reg_proof.py`.

## 5. Occlusion audit — 0 flags
`tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --json gates/occlusion.json` (real command, NO `--selftest`): selftest OK (all 6 planted classes fired, clean controls silent), **0 flags**, RC=0. Files: `gates/occlusion.log`, `gates/occlusion.json`.

## 6. p8 extract + compare — CLEAN
`tools/p8.py extract` (core): 60 noted. `extract` (edition, production SVG): 60 noted, Q73=`up` (core also `up`), noted set == core. `compare`: **CLEAN**, missing=[] extra_count=0 uncertain=[], keydiff=[137, 138, 139, 140, 150]. Files: `gates/p8-extract-core.json/.log`, `gates/p8-extract.json/.log`, `gates/p8-compare.json/.log`.

## 7. Keycheck — canonical run hit a stale archive; independent re-run 149/150
- Canonical `keycheck_ed.py it` RC=0 (`gates/keycheck.log`): registry-vs-p8extract **148/150** exc=[150] mismatch=[(73, 'up', 'speak')]; registry-keys-vs-core 145/150, same 5 expected diffs; Q38-41 [b, a, d, c]; Q125 A; Q46 A; Q52 hosted; Q55 won; Q82/83/84 B/C/A; noted set == core; extract keys 150, missing none.
- Root cause (verified, NOT an edition defect): `keycheck_ed.py:16` reads its extract from the archived `scratch-fanout-en2/fanout/it/p8-extract.json` (mtime 2026-11-11 11:57, pre-delta, Q73=`'speak'`), while the registry it reads is current production (Q73=`'up'`). The mismatch is the archive predating the delta.
- Independent re-run against MY fresh extract + production registry (`gates/keycheck-mine.log`): registry-vs-p8extract **149/150 exc=[150] mismatch=[]**; registry-keys-vs-core 145/150 (same 5 diffs); Q38-41 [b,a,d,c]; Q125 A; Q46 A; Q52 hosted; Q55 won; Q82/83/84 B/C/A; noted set == core; extract keys 150, missing none; Q73 registry=up extract=up core=up. This is the figure that counts for the gate.
- Coordinator follow-up (not a defect): refresh `scratch-fanout-en2/fanout/it/p8-extract.json` after a delta, or repoint the canonical script, or every post-delta canonical keycheck will repeat this phantom 148/150.

## 8. Freeze — core baseline 8/8, edition supplement 8/8, diff +9 U+3000
- Standard invocation (`--build` = core-en, `--core-svg` = core-en/svg): RC=0, **8/8 SVGs byte-identical**, repointed files: none; core integrity re-hash OK. File: `gates/freeze.log`, build copy in `gates/freeze-final/`.
- Supplementary edition-internal baseline (`--build` = proof-copy, `--core-svg` = edition svg): RC=0, **8/8 byte-identical** (produced p8 `ba31ef73…` == shipped post-delta p8). Recorded as supplement only, per task §5 — it does not stand in for the core baseline. File: `gates/freeze-edition.log`, build copy in `gates/freeze-edition/`.
- `freeze.py diff` RC=0: per-page +34/-34, +43/-54, +25/-23, +24/-22, +24/-22, +25/-21, +66/-55, +105/-99 strings; **TOTAL added CJK characters: 9, all U+3000** (p1: 2, p2–p8: 1 each). Files: `gates/freeze-diff.log`, `gates/freeze-diff.json`.

## 9. Web PDF — scratch-only re-render; production print/web text layers identical
- `webpdf.py` on proof-copy SVGs → `gates/web-proof.pdf` RC=0: 2,408,885 B, 49,133 text bytes, SHA `3d3b72fa…`. Its text layer is **byte-identical** to the production web PDF (47,988 chars, token diff 0). Production web PDF was never written.
- Print/web (production PDFs) via pdftotext: print chars 47,988, web chars 47,988, token-multiset diff **0**, only-in-print [] only-in-web []; per-page byte-identical **8/8** (p1 4974B, p2 5898B, p3 5371B, p4 5858B, p5 4764B, p6 5701B, p7 6324B, p8 10243B — p8 is 10,246 − 3 = the one key). File: `gates/printweb.log`.
- Print-vs-web render pixel diff (PIL, 110dpi): P1 0.657% / P8 0.157% of pixels differ >30 grey levels — font-rasterisation from the web PDF's Lucerna-renamed subsets, not content; text layers are byte-identical per page and web P8 is visually identical to print P8.

## 10. text.md re-export — byte-identical
`make_textmd_w47.py` repointed copy (`gates/make_textmd_proof.py`: CORE→proof-copy, SCRATCH→gates with registry-redump.json, OUT→`gates/textmd-reexport.md`) RC=0: recorded blocks 498, stub registry 150 = real registry 150, wrote 53,944 B. `cmp` vs production text.md: **byte-identical**, SHA `a8330625…`. Files: `gates/make_textmd_proof.py`, `gates/textmd-reexport.md`, `gates/textmd.log`.

## 11. check_s11 — ALL PASS
`check_s11.py it` RC=0: colour set core 19 = edition 19, no extra/missing; badges A2 #5c6e30 / B1 #46581f / B2 #37402f present; P8 min SVG font-size 13.5; Q113–120 [A2] tag line; "Levels: 145–149 [A2]"; Q120 [A2] chip OK; WRITING head "H　WRITING　Scrittura [B1]". File: `gates/check_s11.log`.

## 12. Boxtitle sweeps — 12/12 source, 18/18 SVG, 0 overflows
- Source (`sweep_titles.py it`) RC=0: 12 measured, 0 over budget; tightest HOW LONG? 384.3px margin +20.2. File: `gates/boxtitle.log`.
- SVG (`sweep_svg_titles.py it`) RC=0: 18 checked, 0 overflows. File: `gates/boxtitle-svg.log`.

## 13. Creambox (canonical tool) — log byte-identical to proof1
`hidden_files/w47/tools/creambox.py` on production `svg/*.svg` (8 files) RC=0: 32 boxes. File: `gates/creambox-all.log`; `diff` vs proof1 `gates2/creambox-all.log` RC=0 (byte-identical).
- Inside-only lines: min inside clearance **+5.0px**; zero inside-only negatives. The only negative inside-only figure is the desc-clear −1.0px on the P2 AND YOU? box — same adjudicated false alarm as proof1 (last line "redazione." has no descender; baseline clearance +5.0px inside the cream; rendered P2 confirms).
- The raw negative "clearance" lines are below-window titles of the next box (tool's known false-positive class), each with a positive inside-only line, unchanged from proof1.

## 14. Spill sweep (baselines outside cream boxes)
For every #f0eee5 cream box, text lines horizontally overlapping the box whose baseline falls below its bottom: 23 lines total across p1–p7, 0 on p8; gaps below the bottom are **24.0px minimum** (p1 'THE WORD OF THE WEEK' title), all others ≥35.5px. Every one is a next-section title or a following paragraph — no line straddles a box edge, no pure-fill unbordered box overflow. No spill. (Method note: a first naive sweep counting all text outside any box is meaningless — body text legitimately sits outside boxes; the straddle-zone check above is the operative one.)

## 15. verify_ed — ALL PASS (23/23)
`verify_ed.py it` RC=0: Q39 key a; Q40 key d; Q39 note mentor=a; Q40 note arena=d ("arena = l'arena d"); Q40 note not estadio/stadio; Q46 key A; Q46 note 2025; Q52 hosted; Q55 won; Q125 key A; Q125 note 4-1; registry notes no stale Ashes phrasing; text.md has 150 answers; text.md Q39 a / Q40 d / Q125 A; text.md "Arsenal are winning"; no 'Perth is winning' / 'second week in Perth' / 'Ashes begin'; Ashes retrospective present; P8 min PDF font 10.12pt ≥ 9.75pt; SVG zero real CJK. File: `gates/verify.log`.

## 16. 150-question three-source hand verification
Full read of production `text.md` (1305 lines) + registry + P8 extract + SVG definitions. All 150 answers checked against stems — **150/150 correct**. Spot-checked in detail: Q73 `up` → "Speak up: tell a teacher."; Q79 "Children are speaking up this week."; Q81 "She is sitting with a new friend."; Q100 `won` vs Q107 `win` (drills vs headline) both correct in place; Q108 "won" / Q109 "continued" / Q110 "more than" / Q111 "whether" corrections; Q112 Tuesday (Nov 3 2026 = Tuesday, verified); Q137–140 translations; Q145–149 dialogue (row/film/popcorn/show/Friday, confirmed by the dialogue's own answers "The front row", "Yes, Friday"). All 5 matching sets verified against printed definitions in source AND SVG (P2 Q24–27 b/c/a/d; P3 Q38–41 b/a/d/c; P4 Q56–59 b/c/d/a; P5 Q74–77 d/a/b/c; P8 Q141–144 b/c/d/a).
Weekday spot-checks via `date -d` (America/Toronto) all match: Tue 2026-11-03, Sun 2026-11-08, Mon 2026-11-09, Tue 2026-11-10, Mon 2026-11-16, Wed 2026-11-18, Fri 2026-11-20, Sat 2026-11-21, Sun 2026-11-22, Thu 2026-11-26, Fri 2026-11-27, Tue 2026-12-01, Fri 2025-11-21.

## 17. Visual — 8 print pages + web P1/P8
Rendered from the production print PDF with pdftoppm @110dpi: `render/p--1.png`…`p--8.png`; web: `render/w1--1.png`, `w8--8.png`. All 8 pages read: no overlap, no spill, no missing content; footers "Pagina n di 8" all present. P5 shows "73. Speak ___: tell a teacher." with the "to speak up = parlare senza paura" gloss; P8 ANSWERS block shows "73. up". Web P1/P8 match print P1/P8 (text layer 8/8 identical; web P8 visually identical).

## 18. Sweeps
- Orphan punctuation: 0 orphan-led lines in text.md.
- U+2019: 0 hits in text.md, all 8 SVGs (61 ASCII straight apostrophes in text.md).
- D5 fonts (record only): print PDF 41 objects / 7 families (DejaVuSans ×1, Newsreader16pt-Italic ×1, Newsreader16pt-Regular ×16, NotoSansCJKsc-Bold ×8, NotoSansCJKsc-Regular ×8, NotoSerifCJKsc-Regular ×6, UnifrakturMaguntia ×1); web PDF 41 objects / 8 Lucerna-renamed families. P8 min PDF font 10.12pt ≥ 9.75pt.
- Internal labels in text.md: only the W46 header boilerplate (lines 5, 1003), byte-identical in core-en — core-inherited convention, not flagged (same as proof1).

## 19. Defects
**None.** No commit, no push.
