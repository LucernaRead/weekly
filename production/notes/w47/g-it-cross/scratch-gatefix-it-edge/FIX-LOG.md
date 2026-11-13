# FIX-LOG — W47 it edge defects (P1 strap clipped by page edge)

Worker: gatefix-it-edge (02421b4e). Date: 2026-11-12, ~02:00–02:30 UTC.
Scope: 2026-w47-it-es + 2026-w47-it-pt ONLY (it-en/it-nl verification only, untouched).
Defect source: standing pre-insert gate `tools/pdf_edge_scan.py` (commit 45ca73fc),
130-wide report `hidden_files/w47/Reports-preinsert/new-gates-130.md`
(evidence `hidden_files/w47/scratch-new-gates/per-edition/edge/`,
crops `…/edge/crops/2026-w47-it-es-p1-right.png` + `…-it-pt-p1-right.png`, byte-identical).
No commit, no push, no lint. Work in `~/workspace/weekly-git` (main).
it-ru untouched (its boxtitle fix waits for the R2R3 sync).

## Root cause (measured, both editions identical)

P1 masthead strap, `content12.py:18`, 36pt serif bold, `anchor="middle"` at x=975,
`spacing=11.5`:

- it-es: `SEMANARIO ITALIANO　VOL.4　LA SERIE A　IL TORRONE　VENEZIA`
- it-pt: `SEMANÁRIO ITALIANO　VOL.4　LA SERIE A　IL TORRONE　VENEZIA`

Measured with the edition's own `svglib.text_w` (PIL, same font stack as the build):
glyph advance 1340.5u + spacing 11.5 × 53 gaps = **total 1950.0 units = exactly the page
width** (PW = 1950). Centered at 975, the strap runs from x=0 to x=1950 by construction,
so the side-bearing/overhang of the bold `S` (left) and final `A` (right) has nowhere to
go — the final `A` of VENEZIA clips the right sheet edge. The crop shows the `A` sliced
at the edge. This is a layout defect, not a content defect: no word may be deleted
(the strap lists the issue's stories).

For reference, the sibling straps measure: it-en total 1935.2u (nominal ±15.4px),
it-nl total 1928.9u at spacing 11.0 (nominal ±22.0px) — both clear the edge.

## Fix (minimal layout change, shared value, no text change)

`content12.py:18` in BOTH editions, one token each: `spacing=11.5` → `spacing=11.0`.
Font stays 36pt, strap text byte-identical, no other line touched. (There is no shared
strap builder — each it-* edition carries its own `content12.py:18`; the "shared fix"
is the same parameter value in both files. it-en/it-nl were NOT edited, so they needed
no rebuild.)

Predicted effect (same probe): total 1923.5u → nominal margins 27.6px each side
(9.9pt), comfortably beyond the gate's TOUCH band (3px) and NEAR band (10px).
Alternatives measured and NOT taken: 35pt/11.5 (38.9px margins — bigger visual change),
34pt/11.5 (77.6px — far bigger change). 11.0 is the smallest change that clears the
edge with a real margin (~1.4% narrower overall).

## Per-edition record

### 2026-w47-it-es

- Defect (REPRODUCED on production PDF before fix, `verify-before/2026-w47-it-es.json`;
  edge scan RC=1): P1 right TOUCH 11px, min_dist right 0.0pt, left 1.4pt (near left+right).
  P2–P8 clean (min_dist ≥ 50.8pt).
- Fix: `production/2026-w47/2026-w47-it-es/content12.py:18`, spacing 11.5 → 11.0.
- Scratch build: `scratch-gatefix-it-edge/it-es-1`
  (`tools/run_build.py --build production/2026-w47/2026-w47-it-es --out …/it-es-1
  --steps run,render`, RC=0, integrity "production unchanged (41 files)"; then
  `tools/webpdf.py svg/ La-Lucerna-VOL4-ES-web.pdf`, RC=0).
  Build log: `it-es-1-build.log`; webpdf log: `it-es-1-webpdf.log`.
- After fix, scratch edge scan (`verify-after-es/build-copy.json`, RC=0):
  **8 pages, 0 TOUCH, 0 NEAR**; P1 min_dist left **11.5pt** / right **10.1pt**
  (top 59.4, bottom 53.6). Visual check: `it-es-p1-strap.png` — full strap visible,
  final `A` complete with white space to its right.
- Gates on scratch build-1:
  - run.py TOTAL **150**, ALL DONE, no OVERFLOW/TOO WIDE/NOSPACE.
  - p8 extract **150/150** (`it-es-1-p8-extract.json`).
  - p8 compare vs core-it: **CLEAN**, missing [] extra 0, keydiff **[137,138,139]**
    (expected re-aimed; `it-es-1-p8-compare.json`).
  - occlusion_audit: **0 flags** (selftest OK).
  - spill_sweep: **0 SPILL / 59 OBSERVE**, 29 boxes — identical to baseline.
  - boxtitle_check (proper baseline: recheck-week + `--backup-root hidden_files/w47`,
    `boxtitle-after3/2026-w47-it-es.json`): **0 DEFECT / 4 OBSERVE** — the same 4
    same-as-backup values as the pre-fix baseline (cifre +134.5, BODY +12.5,
    frase +99.5, PAROLA +17.5). No new defects. (First attempt without a resolvable
    core/backup context flagged those 4 as DEFECT "no baseline" — an invocation
    artifact, not a real change; see `boxtitle-after/` vs `boxtitle-after3/`.)
  - freeze repro build 2 (`it-es-2`, RC=0, TOTAL 150): **8/8 SVG SHA match**,
    print PDF **byte-identical** to build 1.
  - print/web text layers: identical all 8 pages, 43,606 chars
    (`it-es-1-textlayer.json`).
  - `.text.md` **byte-identical** to production (sha256 verified; see SHAs below).
- BEFORE (production, pre-sync): print `La-Lucerna-VOL4-ES.pdf` 14,033,619 B,
  sha256 `6c299214601b4936dc5329cc72627919fe3b27b90f742298a2eae8cb03554769`;
  web `La-Lucerna-VOL4-ES-web.pdf` 1,291,397 B,
  sha256 `bb6342c8bee3085defcb02ebd75f725c624393d60438314e542f9f27db9ac792`;
  text.md 56,193 B, sha256 `4fd5647e2b7a13812b384963607bd67eda2c2c4fe6bd197b9b08bc08eee21643`.
- AFTER (synced to production, SHAs re-verified after copy):
  print `La-Lucerna-VOL4-ES.pdf` **14,033,594 B**,
  sha256 `551f5fbd039a6d7e322c200ac044048c8beb1cc09af0a04a87df26de4c7951ea`;
  web `La-Lucerna-VOL4-ES-web.pdf` **1,291,381 B**, 46,032 text bytes,
  sha256 `d5deb6efbbef4a1f997168a8edd6bc9be95ae9c92e5528de9a1ffbae029a3667`;
  text.md unchanged (same size + sha as BEFORE).
- KIT: §7 deliverables updated to the new SHAs/sizes (label now "edge-fix build,
  2026-11-12"); §9 edge-fix entry added with the pre-fix SHAs. NOTE (pre-existing,
  found during sync, NOT caused by this fix): KIT §7 had recorded the web sha as
  `c194c3421415c75ed089ced802aae069d6bbd6c3de10c9a4e694cac58c447862`, but the actual
  pre-sync production web PDF was `bb6342c8…` (same size 1,291,397) — the web PDF
  had been rebuilt by the webpdf-rebuild round without a KIT update. The §9 entry
  records both the KIT-stale value and the actual pre-sync value.
- Final confirmation on production files (`verify-after-prod/2026-w47-it-es.json`,
  RC=0): 8 pages, **0 TOUCH, 0 NEAR**; P1 left 11.5pt / right 10.1pt.

### 2026-w47-it-pt

- Defect (REPRODUCED on production PDF before fix, `verify-before/2026-w47-it-pt.json`;
  edge scan RC=1): P1 right TOUCH 11px, min_dist right 0.0pt, left 1.4pt (near left+right).
  P2–P8 clean (min_dist ≥ 63.0pt). Crop byte-identical to it-es.
- Fix: `production/2026-w47/2026-w47-it-pt/content12.py:18`, spacing 11.5 → 11.0.
- Scratch build: `scratch-gatefix-it-edge/it-pt-1` (same commands as it-es, RC=0,
  integrity "production unchanged (41 files)"; webpdf RC=0).
  Build log: `it-pt-1-build.log`; webpdf log: `it-pt-1-webpdf.log`.
- After fix, scratch edge scan (`verify-after-pt/build-copy.json`, RC=0):
  **8 pages, 0 TOUCH, 0 NEAR**; P1 min_dist left **11.5pt** / right **10.1pt**.
  Visual check: `it-pt-p1-strap.png` — full strap visible, final `A` complete.
- Gates on scratch build-1:
  - run.py TOTAL **150**, ALL DONE, no overflow.
  - p8 extract **150/150** (`it-pt-1-p8-extract.json`).
  - p8 compare vs core-it: **CLEAN**, keydiff **[137,138,139]** (expected;
    `it-pt-1-p8-compare.json`).
  - occlusion_audit: **0 flags** (selftest OK).
  - spill_sweep: **0 SPILL / 59 OBSERVE**, 29 boxes — identical to baseline.
  - boxtitle_check (`boxtitle-after3/2026-w47-it-pt.json`): **0 DEFECT / 0 OBSERVE** —
    identical to baseline. No new defects.
  - freeze repro build 2 (`it-pt-2`, RC=0, TOTAL 150): **8/8 SVG SHA match**,
    print PDF **byte-identical** to build 1.
  - print/web text layers: identical all 8 pages, 43,243 chars
    (`it-pt-1-textlayer.json`).
  - `.text.md` **byte-identical** to production (sha256 verified; see SHAs below).
- BEFORE (production, pre-sync): print `La-Lucerna-VOL4-PT.pdf` 14,036,607 B,
  sha256 `9910d536048ae4975c6e1657827f299abab0d274819f881b648a56d513b65135`;
  web `La-Lucerna-VOL4-PT-web.pdf` 1,294,380 B,
  sha256 `d7ccdc15d31f7e472ba58f64198dd07ed044b0b1a7fbc72e12d133a09ef17cca`;
  text.md 55,718 B, sha256 `e01360ae9c401d014a9e0a51779646845a112aac4e8afe912090269c6ffa7302`.
- AFTER (synced to production, SHAs re-verified after copy):
  print `La-Lucerna-VOL4-PT.pdf` **14,036,579 B**,
  sha256 `724aa399bc3f8119fdbdcc13dc2f8ce851aeb8c59a1c5ce64992dc7d62dca4a5`;
  web `La-Lucerna-VOL4-PT-web.pdf` **1,294,361 B**, 45,787 text bytes,
  sha256 `bb4c77c904ba04df7e79da57b65b737134d23c7ae4619473b657f17ed520f68c`;
  text.md unchanged (same size + sha as BEFORE).
- KIT: §7 deliverables updated to the new SHAs/sizes; §9 edge-fix entry added.
  NOTE (pre-existing, found during sync): KIT §7 had recorded the web sha as
  `f2e390f31fc30d14ff08803244cc66749abafd2acdeb41763ba3800fc5f0d85e` / 1,294,373 B,
  but the actual pre-sync production web PDF was `d7ccdc15…` / 1,294,380 B — again
  the webpdf-rebuild round without a KIT update. Recorded in the §9 entry.
- Final confirmation on production files (`verify-after-prod/2026-w47-it-pt.json`,
  RC=0): 8 pages, **0 TOUCH, 0 NEAR**; P1 left 11.5pt / right 10.1pt.

## Near-misses protected (untouched, re-verified on production after the fix)

- it-en: P1 left **6.1pt** / right **5.4pt**, 0 TOUCH, 0 NEAR — values identical to
  the pre-fix baseline (`verify-after-en-nl/2026-w47-it-en.json`, RC=0).
- it-nl: P1 left **9.0pt** / right **7.9pt**, 0 TOUCH, 0 NEAR — values identical to
  the pre-fix baseline (`verify-after-en-nl/2026-w47-it-nl.json`, RC=0).
- Neither was edited or rebuilt; their production PDFs are untouched.

## Files changed (production, uncommitted — no commit/push per task)

- `production/2026-w47/2026-w47-it-es/content12.py` (line 18, spacing only)
- `production/2026-w47/2026-w47-it-es/La-Lucerna-VOL4-ES.pdf` (synced)
- `production/2026-w47/2026-w47-it-es/La-Lucerna-VOL4-ES-web.pdf` (synced)
- `production/2026-w47/2026-w47-it-es/WEEKLY-KIT.md` (§7 + §9)
- `production/2026-w47/2026-w47-it-pt/content12.py` (line 18, spacing only)
- `production/2026-w47/2026-w47-it-pt/La-Lucerna-VOL4-PT.pdf` (synced)
- `production/2026-w47/2026-w47-it-pt/La-Lucerna-VOL4-PT-web.pdf` (synced)
- `production/2026-w47/2026-w47-it-pt/WEEKLY-KIT.md` (§7 + §9)

NOT changed: `*.text.md` (byte-identical, verified by sha256 on rebuild);
core-it; it-ru; ru family; any other edition. The `text.md` "M" in git status vs HEAD
is pre-existing (re-fan-out-2 proofread corrections, e.g. "Domenica 22 novembre torna"
→ "Sabato 21 novembre torna"), not from this fix — the scratch rebuild from the fixed
sources reproduces the production text.md byte-for-byte.

## Environment notes

- Disk at start 98G used / 150G; 99G after the builds (scratch dir 221M total);
  under the 100G stop line throughout. Memory gate respected: renders started only
  with MemAvailable ≥ 1500MB (1584–2284MB observed); other agents' builds (ru-es R1,
  de-es, core-ru, ru-ko, ko-it) were running concurrently — all renders serial, one
  at a time for this worker.
- `~/workspace/weekly-git/AGENTS.md` read before proceeding (repo house rules).
- Scratch kept: `it-es-1/`, `it-pt-1/` (build-1, the sync source of truth),
  all logs + gate JSONs + strap PNGs in this directory. Repro builds (`it-es-2`,
  `it-pt-2`) and boxtitle recheck copies (`boxtitle-recheck/`, `recheck-week/`)
  deleted after verification per the local-storage rule; their values are recorded
  above (freeze 8/8 + print byte-identical; boxtitle-after3 JSONs kept).
