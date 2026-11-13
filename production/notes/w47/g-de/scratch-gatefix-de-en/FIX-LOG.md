# FIX-LOG — W47 boxtitle gate fix (de/en families)

Scope: the 8 boxtitle DEFECTs assigned to this worker in the 130-wide
pre-insert run (`Reports-preinsert/new-gates-130.md`, 2026-11-12 01:54 UTC,
`tools/boxtitle_check.py`, commit 45ca73fc). All 8 are P1 regressions vs the
core edition (core fits, fan-out does not). No it-ru, no ru family, no
`*-ru` outside the assigned de-ru, no other edition touched. No commit /
push / lint. No text content changed in any edition — every fix is a
layout-only font-size reduction.

## §0 Method (shared)

1. **Reproduce**: re-ran `tools/boxtitle_check.py` on each edition in
   `production/2026-w47/` — all 8 reproduced exactly as the report
   (de-es +8.5, de-fr +5.5, de-ko +6.5, de-nl +26.5, de-pt +15.5,
   de-ru +12.5, en-de +15.5, en-nl +7.5). Visual crops from the production
   print PDFs confirm the ink running past the cream box onto white paper
   (de-nl sommaire title, de-es Fragen subtitle; en-de was already visually
   confirmed in the gate run).
2. **Fix choice**: the grid is 1950 wide with RIGHT=1862 (88px margins) and
   CW=422.5 — the boxes cannot be widened without breaking the grid, and the
   P1 boxes have no vertical room for a line break. So: font size down to
   the smallest half-point step that leaves a ≥5px margin, measured with the
   gate's own PIL true-ink math (`tools/boxtitle_check.py:ink_bbox`, via the
   edition's own `svglib.py`). NOTE: first measurement pass was wrong — the
   script passed family `"sans"`, and the gate's `kind_of()` is
   case-sensitive (`"Sans" in family`), so `"sans"` measured as **serif**.
   Passing the real SVG family `"Noto Sans CJK SC"` reproduces the gate
   values exactly (validated: all 8 current-fs numbers match the report to
   0.5px). Lesson: always measure with the family string the SVG carries.
3. **Rebuild**: `tools/run_build.py --steps run,render` (scratch build-copy;
   production integrity re-hashed unchanged) + `tools/webpdf.py` for the web
   PDF. Serial, one edition at a time.
4. **Gates on the rebuilt edition**: boxtitle 0 DEFECT (also 0 OBSERVE / 0
   marginal — no line overflows anywhere); `verify.py` TOTAL 150 + SVGs
   byte-identical after re-run; `p8.py` extract + compare CLEAN;
   `tools/occlusion_audit.py` 0 flags; `tools/freeze.py diff` exit 0;
   rendered frozen intersection 8/8 identical to the pre-fix production
   SVGs (`frozen_check.py`, same math as `freeze_direct.py` part B);
   `freeze_direct.py` rendered 8/8 for the de family (source level: see
   §3 pre-existing note).
5. **Sync**: copy rebuilt `svg/*.svg` + print PDF + web PDF into production,
   SHA-256-verify every file after copy, update KIT §5 (deliverables) +
   §6 (Rebuild note) + §7 (Round entry). `cards/*.png` deliberately NOT
   re-synced (regenerable render intermediates; no gate reads them).
   `*.text.md` byte-identical in every case (no text changed) — verified by
   SHA before/after.

## §1 de-es — DONE (2026-11-12)

- **Defect**: P1 BODY, `Las grandes preguntas　Die Fragen der Woche`,
  fs 19, ink 1461.5→1870.5, box right 1862.0, **+8.5px** (core −22.0).
  Reproduced by gate re-run; crop `crop-de-es-p1-fragen.png` shows the
  final "e" of "Woche" on white paper past the cream edge.
- **Fix**: `content12.py:69`, font size **19 → 18** (layout only, no text
  change). Predicted margin +12.5px.
- **Rebuild** (`de-es/`, `run-build.log`): run.py exit 0, zero FLOW OVERFLOW
  / HEAD TOO WIDE, P8 TOTAL 150. Print PDF 10,968,799 B (+1 B).
  Web PDF rebuilt: 1,601,884 B, 51,011 text bytes (identical to print).
- **Gates on build-copy**:
  - boxtitle: **0 DEFECT, 0 OBSERVE, 0 marginal** (27 titles, 239 body lines)
  - verify.py: exit 0, TOTAL 150, numbering continuous 1–150, SVGs
    byte-identical after re-run, SOP 1.1 style audit True, verbatim OK,
    P8 answers floor 9.94pt ≥ 9.75pt, 0 forbidden terms
  - p8: extract 150/150; compare CLEAN, missing=[] extra_count=0,
    keydiff=[137, 138, 139, 150] (the 4 expected items)
  - occlusion: 0 flags, selftest OK (6 planted classes fired)
  - freeze.py diff: exit 0, added CJK 7 (all U+3000, 1/page P2–P8, 0 on P1)
  - freeze_direct.py: rendered **8/8**, frozen 147/163/195/166/173/175/150/186,
    sha8 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 /
    b7aa0771 / 57e118e7 — **identical to the KIT rebuild-5 record**;
    source level FAIL (see §3, pre-existing)
  - frozen_check (core vs production-before vs build-copy): **PASS 8/8**
  - Visual: `crop-de-es-p1-fragen-FIXED.png` — subtitle ends inside the
    cream box; pixel-measured ink edge moved from 21px past the box edge to
    ~24px inside it.
- **Sync** (2026-11-12 ~02:14 UTC): `svg/*.svg` (8) + print PDF + web PDF
  copied; SHA-256 verified 10/10 OK.
  - Print: 10,968,799 B, sha256
    `a255aa6b268d54ac861759a2c459ca4f673aeb9a72f37f7af1153ebfc5e06deb`
  - Web: 1,601,884 B, sha256
    `682fd0d0ef1eaeea704cbc56e2159b4ca23d58cf42cbcb59bcff12ac0ad0558d`
  - text.md: 50,124 B, sha256 `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` (unchanged)
  - KIT updated: §5 deliverables (rebuild 6), Status line, §6 Rebuild 6
    subsection, §7 Round 3 entry.
- **Final confirmation on production files**: boxtitle
  **0 DEFECT, 0 OBSERVE, 0 marginal**, exit 0.

## §2 Remaining 7 — DONE (2026-11-12)

Driver: `driver7.py` (serial: run_build run,render → webpdf → boxtitle →
verify → p8 extract/compare → occlusion → freeze diff → frozen_check →
freeze_direct for de family). Per-edition logs under `2026-w47-<slug>/`.
All 7 rebuilt, gated green, synced to production (SHA-verified 10/10 each),
production boxtitle re-confirmed 0/0/0 on all 7 together (single final run,
exit 0). KITs updated for all 7 (see each entry). No text changed anywhere;
all `text.md` SHAs identical to the KIT record.

### de-fr — DONE

- **Defect**: P1 BODY, `Les grandes questions　Die Fragen der Woche`, fs 19,
  ink 1867.5, box right 1862.0, **+5.5px** (core −22.0).
- **Fix**: `content12.py:69`, font size **19 → 18** (layout only). Ink end
  1867.5 → **1846.5**, margin **+15.5px**.
- **Gates on build-copy**: boxtitle **0 DEFECT / 0 OBSERVE / 0 marginal**;
  verify.py exit 0, TOTAL 150, SVGs byte-identical after re-run, SOP 1.1
  style True, P8 floor True; p8 extract 150/150, compare CLEAN keydiff
  [137,138,139,150]; occlusion 0 flags; freeze.py diff exit 0, added CJK 7
  (all U+3000); freeze_direct rendered **8/8**, sha8 083e2a2a / 689045ad /
  fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7 — identical
  to the KIT rebuild-5 record; source FAIL = 4 unaccounted ADDED literals
  (see §3, pre-existing, KIT-documented); frozen_check **PASS 8/8**.
- **Sync**: print 10,932,566 B (+1) sha
  `f5e68b46039f4bdb77a8ffb8e80fd47c0e0b24ebff746e74a6da6804c127bf67`; web
  1,600,196 B (−1) sha
  `ae89ba2c23645fe720f812d0a2902feecdddc1f2326ef0c026d8c111b33933f7`;
  text.md 50,042 B sha
  `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6`
  (unchanged). KIT: §5 deliverables (rebuild 6), status line, §6 Rebuild 6
  subsection, §7 Round 3 entry.

### de-ko — DONE

- **Defect**: P1 BODY, `이번 주의 다섯 가지 질문　Die Fragen der Woche`,
  fs 19, ink 1868.5, box right 1862.0, **+6.5px** (core −22.0).
- **Fix**: `content12.py:69`, font size **19 → 18** (layout only). Ink end
  1868.5 → **1846.5**, margin **+15.5px**.
- **Gates on build-copy**: boxtitle **0 / 0 / 0**; verify.py exit 0, TOTAL
  150, SVGs byte-identical after re-run; p8 extract 150/150, compare CLEAN
  keydiff [137,138,139,150]; occlusion 0 flags; freeze.py diff exit 0,
  added CJK 3,096 (the Korean explanation layer itself, expected);
  freeze_direct rendered **8/8**, sha8 73347f49 / 689045ad / 8b2e9eba /
  df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / f6dd4a15 — identical to the KIT
  fix1 record; source FAIL `'sans'` ×2 (see §3, pre-existing);
  frozen_check **PASS 8/8**.
- **Sync**: print 15,907,007 B (+1) sha
  `5e34f31a4922a35902ffd3decebb9ba92d81387c4e1042244799630de1707114`; web
  1,909,583 B (−4) sha
  `d77adb822d976cceab204f45fe8e8e66dc98ada4783de4f21820646518a1c704`;
  text.md 51,498 B sha
  `fd2dbd047e23bcd0fffc5245ee8d529b9e848adc11133ff46f490b304b8a66a2`
  (unchanged). KIT: §2 Deliverables (fix2 rebuild), status line, §6 fix2
  bullet. NOTE: its §3 still claims freeze_direct source PASS — that claim
  was true at fix1 time; the source level FAIL is recorded honestly in the
  §6 fix2 bullet (see §3).

### de-nl — DONE

- **Defect**: P1 TITLE, `IN DIESER AUSGABE　In dit nummer`, fs 24, ink
  1888.5, box right 1862.0, **+26.5px** (core −22.0). Visually confirmed
  pre-fix: the whole gloss `In dit nummer` ends on white paper past the
  cream box edge (`crop-de-nl-p1-sommaire.png`).
- **Fix**: `content12.py:89`, font size **24 → 22** (layout only). Ink end
  1888.5 → **1852.5**, margin **+9.5px**.
- **Gates on build-copy**: boxtitle **0 / 0 / 0**; verify.py exit 0, TOTAL
  150, SVGs byte-identical after re-run; p8 extract 150/150, compare CLEAN
  keydiff [137,138,139,150]; occlusion 0 flags; freeze.py diff exit 0,
  added CJK 7 (all U+3000); freeze_direct rendered **8/8**, sha8 083e2a2a /
  689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7
  — identical to the KIT rebuild-fix1 record; source FAIL `'sans'` ×2
  (see §3, pre-existing); frozen_check **PASS 8/8**. Visual:
  `crop-de-nl-p1-sommaire-FIXED.png` — title fully inside the cream box.
- **Sync**: print 10,964,699 B (+2) sha
  `55489de172f5743e6480b939ba485a6c8be34029d37f53de0e0acaf2d59e4b72`; web
  1,596,814 B (−16) sha
  `56aeb8cd7bedd98fc8a96a7175a583b8183333ab1aa457e4fac3992f857c5734`;
  text.md 49,403 B sha
  `e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e`
  (unchanged). KIT: §5 deliverables (rebuild fix2), status line,
  §6 Rebuild fix2 subsection, §7 fix2 bullet.

### de-pt — DONE

- **Defect**: P1 TITLE, `DIE WOCHE IN ZAHLEN　Em números`, tsize 23, ink
  976.5, box right 961.0 (P1 ZAHLEN box), **+15.5px** (core −11.5).
- **Fix**: `content12.py:43`, `f.box(..., tsize=23)` → **tsize 21.5**
  (layout only). Ink end 976.5 → **948.5**, margin **+12.5px**. Box height
  334.2 → 332.725 (title baseline y 1507.1 → 1505.565); P1-headline flow end
  stays **1554 (= core)** — verified identical with the fix reverted in a
  scratch copy (the 1.5px slack is absorbed at the column break), so the
  KIT flow-ends line is unchanged.
- **Gates on build-copy**: boxtitle **0 / 0 / 0**; verify.py exit 0, TOTAL
  150, SVGs byte-identical after re-run; p8 extract 150/150, compare CLEAN
  keydiff [137,138,139,150]; occlusion 0 flags; freeze.py diff exit 0,
  added CJK 7 (all U+3000); freeze_direct rendered **8/8**, sha8 083e2a2a /
  689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7
  — identical to the KIT rebuild-4 record; source FAIL `'sans'` ×2
  (see §3, pre-existing); frozen_check **PASS 8/8**. Visual:
  `crop-de-pt-p1-zahlen-FIXED.png` — title fully inside the cream box.
- **Sync**: print 10,968,901 B (−1) sha
  `bfdc6e8fda242f11dfaee0658b016dc6cf7c622c71b7287d1dfa018809fab9e9`; web
  1,602,460 B (−12) sha
  `e723f2cbc267d6d0fbe35be45d243ae5c3dcfe3130d8a38a012d6f018ad1a010`;
  text.md 49,812 B sha
  `e2ee96ebd9dca775598431f87c511f53ed04dec2547896586d46a2c57a800928`
  (unchanged). KIT: §5 deliverables (rebuild 5), status line, §7 Rebuild 5
  subsection (pt keeps rebuild notes in §7).

### de-ru — DONE

- **Defect**: P1 TITLE, `IN DIESER AUSGABE　Содержание`, fs 24, ink 1874.5,
  box right 1862.0, **+12.5px** (core −22.0).
- **Fix**: `content12.py:89`, font size **24 → 22.5** (layout only). Ink end
  1874.5 → **1848.5**, margin **+13.5px**.
- **Gates on build-copy**: boxtitle **0 / 0 / 0**; verify.py exit 0, TOTAL
  150, SVGs byte-identical after re-run; p8 extract 150/150, compare CLEAN
  keydiff [137,138,139,150]; occlusion 0 flags; freeze.py diff exit 0,
  added CJK 7 (all U+3000); freeze_direct rendered **8/8**, sha8 73347f49 /
  689045ad / f356adcf / df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / 7016818d
  — identical to the KIT rebuild-fix1 record; source FAIL `'sans'` ×2
  (see §3, pre-existing); frozen_check **PASS 8/8**.
- **Sync**: print 10,954,763 B (+4) sha
  `237d36ae2d04b84808b017752307d6742155f5f84762fc4e3e581a6c7b430c29`; web
  1,647,542 B (+15) sha
  `1a708f26903d2b4fbc2aa82b1130fb7f8843528742568cc8cbdef7ebd8b61554`;
  text.md 56,231 B sha
  `dee6697b0ec3ff279ad4508dcc7d7402952d40fcc8670b1208a2de9158074958`
  (unchanged). KIT: §5 deliverables (rebuild fix2), status line,
  §6 Rebuild fix2 subsection, §7 fix2 bullet.

### en-de — DONE

- **Defect**: P1 BODY (SEARCHES footnote), `Relative Beliebtheit, keine
  exakten Suchzahlen.`, fs 19, ink 1877.5, box right 1862.0, **+15.5px**
  (core −22.0). Visually confirmed in the gate run: line end on white paper
  outside the cream box.
- **Fix**: `content12.py:85`, font size **19 → 18** (layout only). Ink end
  1877.5 → **1855.5**, margin **+6.5px**.
- **Gates on build-copy**: boxtitle **0 / 0 / 0**; `run.py` exit 0, zero
  FLOW OVERFLOW / HEAD TOO WIDE, TOTAL 150, MODEL 82; determinism re-run
  (`run.py` again in the build copy): SVGs byte-identical, TOTAL 150 again;
  occlusion 0 flags, selftest OK; p8 extract noted set 60/150 (same set as
  core), compare CLEAN keydiff [137,138,139,140,150] (expected);
  `freeze.py diff` vs core-en exit 0, TOTAL added CJK 9, all U+3000;
  frozen_check (core vs pre-fix vs rebuilt SVGs) **PASS 8/8 identical**;
  print/web text layers 48,638 bytes each, identical content. Visual:
  `crop-en-de-p1-searches-FIXED.png` — footnote fully inside the cream box.
- **Driver remediation (NOT edition defects — driver assumptions, fixed in
  the driver)**: (1) en editions have NO `verify.py` (de-family script);
  TOTAL/MODEL come from `run.py` + a determinism re-run. (2) The en P8
  file is `p8-test.svg`, not `p8-uebungen.svg` (en SVG names: p1-front,
  p2-life, p3-culture, p4-sport, p5-youth, p6-deep, p7-lang, p8-test). (3)
  `p8.py compare --target en` resolves the P8 path via `p8_path()` which
  looks for `p8-exercices.svg` — use explicit `--core-p8/--edition-p8`
  paths instead. (4) `frozen_check.py` hardcoded the de SVG names; it now
  discovers `pN-*.svg` via glob (page number from filename) and reproduces
  freeze_direct's exact math (raw inner text, NOT stripped — stripping
  drops the spaced variants; hash over sorted multiset elements). It
  reproduces the KIT reference numbers exactly on de-es (147/163/195/166/
  173/175/150/186, sha8 083e2a2a/…/57e118e7).
- **Sync**: print 29,331,210 B (+1) sha
  `d0d14724442fbcf9d89c5e91a175f263b5aabe5a0f742c5aae013a67a4a8acc2`; web
  2,414,461 B (−10) sha
  `2c3ea4ca482d4617caeb93521904cd65feda4c967c1819291a635d929218aa08`;
  text.md 52,565 B sha
  `c16f0e473f8017605fe8822a6d711134ad55b1708a0f22346ef2b4dd1f01d589`
  (unchanged). KIT: §7 deliverable lines (new bytes/SHAs; text layer
  47,403 chars / 48,638 bytes unchanged) + §9 boxtitle-fix bullet.

### en-nl — DONE

- **Defect**: P1 BODY (SEARCHES footnote), `Relatieve populariteit, geen
  exacte zoekcijfers.`, fs 19, ink 1869.5, box right 1862.0, **+7.5px**
  (core −22.0).
- **Fix**: `content12.py:85`, font size **19 → 18** (layout only). Ink end
  1869.5 → **1848.5**, margin **+13.5px**.
- **Gates on build-copy**: boxtitle **0 / 0 / 0**; `run.py` exit 0, zero
  overflow, TOTAL 150, MODEL 82; determinism re-run SVGs byte-identical;
  occlusion 0 flags; p8 extract noted set 60/150 (same set as core),
  compare CLEAN keydiff [137,138,139,140,150]; `freeze.py diff` exit 0,
  TOTAL added CJK 9, all U+3000; frozen_check **PASS 8/8**; text layers
  identical content (web 49,155 text bytes).
- **Sync**: print 29,341,266 B (−1) sha
  `626e4c1bbf2c77cb579ac9f6e7511ce7036d6af1bebdb5b7700a729615dc7fee`; web
  2,411,532 B (−14) sha
  `dd4cee4884e6f3d3af68788b469ac33d4b452c75d4bad91fd68e01dc8e70cf38`;
  text.md 53,565 B sha
  `30bfb6f93860fae5ae58707c28c4f2e3a18ebcc07e272681e67688451d12c0be`
  (unchanged). KIT: §2 Files delivered (new bytes/SHAs; text layer
  48,041 chars unchanged) + §3 boxtitle-fix bullet + §9 Build record
  bullet.

## §3 Pre-existing finding (NOT this fix, flagged for the coordinator)

`freeze_direct.py` **source level FAILs on de-es** (and may on the other de
editions — checked per edition in §2): 1 unaccounted removed literal,
`'sans'` ×2 in `svglib.py`. Root cause, measured: `core-de/svglib.py`
(mtime 2026-11-11 22:35) carries a fix2 patch (U+201C routing, proof2
D1/D2) that the fan-out copies of `svglib.py` (mtime 2026-11-11 08:20) do
not have — the core was patched after the fan-out was copied from it, so
the edition's `svglib.py` is stale vs core (17 vs 15 `'sans'` literals).
This predates the boxtitle fix: the fix changed one int + one comment, no
string literal, in a file (`content12.py`) that is not `svglib.py`. The
rendered freeze level is unaffected (8/8, SHAs identical to the KIT).
Deliberately NOT fixed here: syncing core's `svglib.py` into the editions
would change glyph rendering (U+201C routing) — a separate fix with its
own proof, for the coordinator to decide.

Confirmed per-edition (2026-11-12, same root cause): de-es, de-ko, de-nl,
de-pt, de-ru all report the same 1 unaccounted removed literal
(`'sans'` ×2 in `svglib.py`); in every case the KIT's earlier "source
PASS" claim was true at that edition's rebuild time and went stale when
core moved on — nothing was rewritten in history, the new rebuild note
records it honestly. **de-fr is different**: it reports 4 unaccounted
ADDED literals — the rebuild-4 box-title shortenings
(`'WEIHNACHTSWÖRTER　Noël'`, `'DER TIPP　Conseil'`, `'ADVENTSWÖRTER　Avent'`,
`'DER WERKZEUGKASTEN　Outils'` in content34.py:58/78, content56.py:46,
content7.py:79) were shortened in the content files without updating
`tr_fr.py`, so freeze_direct's source accounting (which keys on
`tr_fr.py`) cannot account for them. This is KIT-documented in the de-fr
KIT Rebuild 5 "Tool-note" (running freeze_direct from
`scratch-fanout-de-rebuild-A/` with the current `tr_fr.py` passes; this
run used the stale `tr_fr.py` in `scratch-fanout-de/`). Same conclusion:
not fixed here, for the coordinator.
