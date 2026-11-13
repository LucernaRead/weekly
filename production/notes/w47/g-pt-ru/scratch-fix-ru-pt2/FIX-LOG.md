# FIX-LOG — W47 ru-pt fix2 (KIT-only doc repair, 2026-11-11)

Scope: only `production/2026-w47/2026-w47-ru-pt/WEEKLY-KIT.md` in
`~/workspace/weekly-git`. No source, SVG, PDF, or text.md touched; no
rebuild, no re-proofread, no commit, no push. Fixes re-proof (b) defect
(b)-1 only: the KIT recorded the pre-fix1 re-fanout build's identity
numbers; the on-disk fix1 deliverables are a different set.

## Probes (before work)

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → rc=0
  (`e69de29b…5391`).
- Real file written to goals-side scratch
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-pt2/probe.txt`.
- Scratch dir (sole, dedicated):
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-pt2/`.
  TMPDIR pointed at it for all pdftotext runs. Python:
  `~/workspace/weekly-git/tools/venv/bin/python`.

## On-disk re-measurement (before any edit)

Method: `sha256sum` + `stat -c %s` on the production files;
`pdftotext` (plain, NO `-layout`) on both PDFs, byte count + non-whitespace
char count via repo venv Python, multiset compared with `collections.Counter`.
(`-layout` gives 110,945 bytes — NOT the re-proof figure; plain pdftotext
reproduces it exactly.)

| file | SHA-256 | bytes |
|---|---|---|
| `Lucerna-VOL4-ru-pt.pdf` (print) | `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed` | 21,205,591 |
| `Lucerna-VOL4-ru-pt-web.pdf` (web) | `f21ed9285a7fcca0a3515e2daa2af2518b0e11fb83752280ea448cf80b7864df` | 3,383,546 |
| `2026-w47-ru-pt.text.md` | `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` | 65,155 |

- pdftotext (plain): print 58,327 bytes, web 58,327 bytes; chars 38,844
  total / 31,105 non-whitespace each; character multiset print == web
  (Counter identical). Matches re-proof exactly.
- All six values agree with the re-proof measurements before editing.

## Changes (file: `WEEKLY-KIT.md`, 7 edit sites, 6 lines)

1. **L53 (§5) print PDF identity**
   - Before: `21,205,597 bytes`, SHA `59f01012f5c64fdddb73e1b73a50b448e21b8d2c68f59b740b4927a6f1444cdd`
   - After: `21,205,591 bytes`, SHA `4d726d922b33b6c38ab93e7ed1c47c8913817a5fa4e3bbc59988ff232bec61ed`
2. **L54 (§5) web PDF identity**
   - Before: `3,383,529 bytes`, SHA `485a27b6be196e7f7d95c3b2d2e218ba3969ebe8fe084668ec20eea4f7bcff70`
   - After: `3,383,546 bytes`, SHA `f21ed9285a7fcca0a3515e2daa2af2518b0e11fb83752280ea448cf80b7864df`
3. **L56 (§5) text layer**
   - Before: pdftotext bytes `58,200`; `31,041 chars each`
   - After: pdftotext bytes `58,327`; `31,105 chars each`
4. **L77 (§7) print/web text layer**
   - Before: `31,041 chars each` → After: `31,105 chars each`
5. **L79 (§7 §1.1 spot-checks) web PDF size**
   - Before: `web 3,344,677 bytes < 7 MB` (proof1 size) → After: `web 3,383,546 bytes < 7 MB`
6. **L83 (§7 re-fanout para) RECORD.md reference**
   - Before: `` full record in `hidden_files/w47/scratch-refanout-ru/records/pt/RECORD.md` ``
   - After: `` full record in `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-refanout-ru/records/pt/RECORD.md` — goals-side scratch, not inside the repo clone ``
   - Verification: the file exists at that goals-side path; head reads
     `# ru-pt — re-fanout self-check record (2026-11-11)` / `Rebuilt from
     finalized core-ru (fix1 f11854bf) with the D1 map fix.`
7. **L83 kicker ink gaps**
   - Before: `PIL ink gaps [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6] px, min 5.9 ≥ 4`
   - After: `re-proof (round 2, 2026-11-11) measured ink gaps 1x [9, 4, 10, 7, 7, 8, 9, 9, 10] px, 2x min 4.0 px ≥ 4 (the earlier self-check values [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6] px, min 5.9 did not reproduce under either re-proof measurement set)`
   - Old kicker numbers kept only inside the explicit "did not reproduce"
     parenthetical, as a superseded-value note (not as a live claim).

**Extra correction in the same defect class (same line, L83):** the
re-fanout self-check's `31,107 chars` also did not match the delivered
PDFs (re-proof + my own re-measurement: 31,105). Corrected in place with
an explicit note: `print/web text multiset identical overall and per page
(31,105 chars; the re-fanout self-check's 31,107 did not reproduce —
re-proof measured 31,105 on the delivered PDFs)`. Not in the task's grep
list, flagged here so the parent sees it.

## Item 5 (D5) — NOT changed

KIT has no D5 section: grep for `D5` / `1863` / `1864` / `P8 副标题` =
0 hits. Per task instruction, no section was added. The re-proof P8
subtitle raster value 1864 is therefore recorded here only, not in the KIT.

## Post-edit verification

- Old-number grep `59f01012|485a27b6|3,344,677|58,200|31,041` on KIT: **0 hits**.
  (No history section holds old SHAs, so no exception was needed.)
- New values present: print SHA ×1, web SHA ×1, `58,327` ×1, `31,105` ×3
  (L56, L77, L83), `21,205,591` ×1, `3,383,546` ×2 (L54, L79).
- Snapshot comparison: `find . -type f -exec sha256sum` before vs after
  (44 files) — diff shows **only `./WEEKLY-KIT.md` changed**
  (`94cf3a57…` → `184cdc8c…`); the other 43 files byte-identical.
  Snapshots: `snapshot-before.txt`, `snapshot-after.txt` in this scratch dir.
- `git status --porcelain` for the edition dir shows the whole dir as
  untracked (`?? production/2026-w47/2026-w47-ru-pt/`) — pre-existing state
  of the clone; nothing committed or pushed by this task.
- KIT's unchanged claim `.text.md` 65,155 bytes agrees with on-disk stat.
- D5 and P1 MEDIA (±1px observation items) not defects — no content touched.

## Observations (not changed, for parent)

- KIT §5 line 42 also cites `hidden_files/w47/scratch-fanout-ru/` for the
  transform scripts (same goals-side-scratch-vs-clone path shape as the
  RECORD.md citation fixed above). Left as-is: out of this task's item
  list; flagging only.
- Working files in this scratch dir: `probe.txt`, `pt.txt` (pdftotext
  -layout output, 110,945 B — evidence that -layout is the wrong
  method), `p.txt` / `w.txt` (plain pdftotext outputs, 58,327 B each),
  `snapshot-before.txt`, `snapshot-after.txt`, this `FIX-LOG.md`.
