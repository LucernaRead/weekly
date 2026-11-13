# W47 disk cleanup log — ROUND 2 — scratch-cleanup-disk99

Date: 2026-11-12 ~02:30–02:56 UTC (run 2026-11-11 21:30–21:56 EST). Operator: cleanup subagent.
Scope: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/` and
`~/workspace/weekly-git/hidden_files/w47/`. Read-only SHA audit first, SHA-verified deletions only.
No build, render, commit, push, or production change of any kind. `rm` only (no trash — same
filesystem, moves bytes without freeing quota, per round 1). Round 1's log is `CLEANUP-LOG.md`
in this same dir; round-1 rules stand, plus the coordinator's clarified rules (1)–(3) for this round.

## df before / after

| moment | df -k Used | df -h Used |
|---|---|---|
| task start | 103,215,896 | 99G |
| delete-phase start (inside delete2.py) | 102,943,976 | 99G |
| after delete2.py | 97,264,064 | 94G |
| after (b) fix-up | 97,280,192 | 94G |
| log writing (~02:56 UTC) | 97,350,164 | 94G |

**Note on df:** the volume is 150G; the binding line is the ~100–105G quota. Gross freed by
verified deletions: **6,618,867,218 B (6,312.2 MB ≈ 6.16 GiB)**. Net df change over the run is
smaller (−5,865,732 KB ≈ −5.59 GiB from task start to log writing) because concurrent workers
kept writing throughout (~0.5 GiB during the run; df was still climbing ~70 MB in the 4 minutes
after the last deletion). The ≥2G target is met more than 3× over.

## Result summary

- **Deleted: 4,521 files, 6,618,867,218 B (6,312.2 MB)**, all re-verified by SHA+size immediately
  before `rm`, with at least one listed survivor re-verified (SHA) immediately before each `rm`.
- **Skipped at delete time: 41 files** (kept; see §6) — production rebuilt under them between audit
  and delete. The other 32 apparent skips were my own prefix bug, recovered in the fix-up (§7).
- **Target ≥2G REACHED.** No directory was removed. No file under `production/` was modified
  (spot-check: ru-it print still `12f897b2…`, ru-it web still `6fce91e4…`, exactly round 1's values).
- `scratch-refanout-it2/backup/` verified intact before AND after: 430 files, 326,077,331 B, unchanged.
  Its files were used as byte-survivors only (read-only hashing); nothing inside `backup/` was deleted.
  Deletions from `scratch-refanout-it2/` came only from `prev-logs/` (outside `backup/`), as permitted.

| verdict | files | bytes | meaning |
|---|---|---|---|
| DELETE-DUP-PROD | 2,357 | 2,137,508,043 (2,038.5 MB) | byte-identical (SHA-256) to the same file in production NOW |
| DELETE-DUP-KEPT | 1,806 | 3,966,448,763 (3,782.7 MB) | byte-identical to a kept file in R-scratch / rebuild dirs / it2 backup |
| DELETE-DUP-GROUP | 315 | 464,853,010 (443.3 MB) | ≥2 identical candidate copies; one designated keeper remains |
| DELETE-SVG-R-KEPT (b) | 32 | 17,659,458 (16.8 MB) | freeze-baseline SVGs, byte-identical to kept R1 files (direct comparison) |
| DELETE-C-DUP-TWIN (c) | 9 | 25,655,264 (24.5 MB) | patch1 twin copies; italic-fix1 twin remains |
| DELETE-C-SUPERSEDED (c) | 2 | 6,742,680 (6.4 MB) | italic-fix1 + patch1 web PDFs, superseded (see §4) |

Audit scale: production map 2,538 build files (131 edition dirs); kept map 20,243 build files
(all `.pdf/.svg/.png` outside the candidate dirs, both roots, excluding `assets/`); candidates
5,555 files. Zero hardlinked candidates (nlink>1: 0), so file bytes = freed bytes.

## Deleted by family dir

| dir | files | bytes |
|---|---|---|
| scratch-refanout-zh-tw | 550 | 770,780,603 (735.1 MB) |
| scratch-refanout-ru | 335 | 708,501,799 (675.7 MB) |
| scratch-refanout-it2 (prev-logs/ only) | 513 | 631,706,247 (602.4 MB) |
| scratch-fanout-zh-tw | 355 | 584,574,646 (557.5 MB) |
| scratch-fanout-en | 177 | 549,818,585 (524.3 MB) |
| scratch-refanout-pt | 342 | 517,164,429 (493.2 MB) |
| scratch-fanout-en2 | 245 | 516,324,280 (492.4 MB) |
| scratch-refanout-it | 362 | 433,840,918 (413.7 MB) |
| scratch-fanout-pt | 196 | 404,995,061 (386.2 MB) |
| scratch-fanout-it | 255 | 321,682,576 (306.8 MB) |
| scratch-refanout-es | 355 | 303,069,135 (289.0 MB) |
| scratch-fanout-ru | 194 | 293,140,495 (279.6 MB) |
| scratch-refanout-fr2 | 135 | 134,477,475 (128.2 MB) |
| scratch-fanout-es | 193 | 122,258,895 (116.6 MB) |
| scratch-fanout-zh-cn | 84 | 114,587,300 (109.3 MB) |
| scratch-refanout-nl | 116 | 82,934,094 (79.1 MB) |
| scratch-fanout-ko3 | 47 | 55,993,547 (53.4 MB) |
| scratch-webpdf-patch1 (c) | 10 | 29,022,884 (27.7 MB) |
| scratch-fanout-fr | 24 | 22,959,731 (21.9 MB) |
| scratch-ru-rebuild-ru-fr (b) | 16 | 8,830,132 (8.4 MB) |
| scratch-ru-rebuild-ru-de (b) | 8 | 4,414,824 (4.2 MB) |
| scratch-ru-rebuild-ru-en (b) | 8 | 4,414,502 (4.2 MB) |
| scratch-webpdf-italic-fix1 (c) | 1 | 3,375,060 (3.2 MB) |
| scratch-fanout-de / de-rebuild-A / de-rebuild-B / ja / ko / nl, W fanout-ja | 0 | evidence only, nothing deletable |

Full per-file list: `deleted-manifest-2.tsv` in this dir (path, size, SHA-256, verdict, survivor used).

## (a) Fanout / refanout — method

- Candidates: every `.pdf` / `.svg` (non-`assets/`) plus `.png` on render-output paths
  (`cards/`, `qa/`, `pages/`, `png/`, `visual/`, `sheets/`, `*-review/`, `*-crop*`/`crop-*`/
  `vis-*`/`*-contact.png`/page-render names, production-tree copies under `tmp/`/`sandbox/`/`backup*/…/cards/`).
  `.jpg` never candidates (all under `assets/` = source inputs). No non-`pN-*` SVG exists in the
  candidate dirs (all SVGs are page outputs).
- Verdicts by SHA against three maps: production NOW, kept scratch (incl. it2 `backup/` as a
  read-only survivor source), and within-candidate duplicate groups (keep-one: the first sorted
  path remains; 231 keepers, 404.1 MB).
- PNG rule (1) applied: a DELETE-DUP-GROUP PNG additionally required its edition mapped AND its
  production source intact (edition dir with `.md` in production). Two derivation bugs in the first
  audit pass left 24 PNGs unmapped (family target regex failed for `zh-cn`/`zh-tw` targets;
  `<lang>-review` tokens unrecognised); both fixed, all 24 re-derived and deleted as group
  duplicates (18 + 6, 6.7 MB total). Spurious-regex-match hazard found while fixing: a lazy
  `[a-z-]*?` match can return wrong language groups (`freeze-es-ja-3` first matched `ze/es`);
  the fix splits tokens on `-` and scans language codes directly.
- Race handling: the audit took ~20 min (cold, contended disk); workers kept rebuilding. Every
  delete re-verified the file (size+SHA) and at least one survivor (SHA) immediately before `rm`;
  a survivor already verified this run was re-checked by stat (size+mtime_ns) with a fresh hash on
  any change. 41 files failed that check at delete time and were kept (see §6) — the check worked
  as designed. No file was deleted whose survivor had vanished: the resolver pre-excluded every
  file in the final deletion set from the survivor lists (that caught exactly one case, §5).

## (b) Freeze-baseline SVGs — 32 files, all deleted

Direct byte comparison, fresh-hashed this round: every one of the 32 SVGs in
`scratch-ru-rebuild-ru-{de,en,fr}/freeze-baseline{,2}/build-copy/svg/` is byte-identical to kept
files in `scratch-ru-rerun-R1/` (two R1 copies each, `ru-{de,en,fr}-1` and `-2`), re-verified in
the fix-up run immediately before each `rm`. Rule (2) satisfied: byte-identical to a KEPT file.
See also §7 for the fix-up this required.

## (c) italic-fix1 / patch1 freeze builds — provenance established, 11 of 20 files deleted

**Provenance (from the dirs' own logs):** both are ru-en (`2026-w47-ru-en`) freeze snapshots.
- `scratch-webpdf-patch1` — D2 weight patch, 2026-11-11 08:33–08:50 UTC (`PATCH-LOG.md`, `GATE-LOG.md`).
  Print untouched: 21,245,374 B, SHA `7b73070c2c11…`. Web rebuilt: 3,367,620 B, SHA `82dfb6eaeff6…`.
- `scratch-webpdf-italic-fix1` — D3 italic patch, 2026-11-11 ~09:05–09:25 UTC (`PATCH-LOG.md`,
  `GATE-LOG.md`). Print untouched, same bytes/SHA `7b73070c2c11…`. Web rebuilt: 3,375,060 B,
  SHA `6419f7ad188d…` (D2 + D3 fixes, all gates green).
**Supersession:** production ru-en NOW is print `e29ba5fae4a3…`, web `7a3f635116c9…` (rebuilt again
after round 1, which saw `1fcc6aa4…`) — neither freeze print nor either freeze web matches
production. The D2+D3 `webpdf.py` patch is committed (`40963281 "tools: webpdf weight + italic
face resolution (ru-en D3)"`), so the web builds are reproducible from the repo tool.
**Source identity:** the freeze `2026-w47-ru-en.text.md` is NOT byte-identical to production's
text.md, and the freeze SVGs match neither production ru-en SVGs nor R1/R2 ru-en builds — the
freeze build used an older source version. Therefore:
- print PDF `7b73070c…`: identical twin in both dirs → DELETE one (patch1), KEEP one (italic-fix1).
- 8 SVGs per dir: byte-identical across the two dirs → DELETE one copy of each (patch1), KEEP one
  (italic-fix1). They are the only surviving copies of that source version, so one copy stays.
- web PDFs: single copies each, superseded, reproducible from the kept freeze sources
  (SVGs + text.md stay in place) + the committed tool patch → DELETE both.
- Deleted (c): 9 DUP-TWIN + 2 SUPERSEDED = 11 files, 32,397,944 B. Kept (c): 9 twin copies in
  italic-fix1 (print + 8 SVGs).
- The 16 freeze `cards/*.png` (8 per dir) are OUT of this round's (c) 20-file scope and were kept;
  checked: 0 of 16 are byte-identical to production ru-en cards (production cards have moved on).

## Kept, with reasons

| class | files | bytes | reason |
|---|---|---|---|
| KEEP-SINGLE (candidates) | 804 | 1,879,435,062 (1,792.4 MB) | unique SHA, no survivor in production / kept scratch / other candidates; deleting would destroy the only copy of that build |
| KEEP-GROUP-KEEPER (candidates) | 231 | 423,745,483 (404.1 MB) | designated survivor of a duplicate group; the other group members were deleted |
| KEEP-SURVIVOR-LOST | 1 | 3,375,060 (3.2 MB) | `scratch-refanout-ru/backup-old/2026-w47-ru-en/Lucerna-VOL4-ru-en-web.pdf` (SHA `6419f7ad…`): its only survivor was the italic-fix1 (c) web PDF being deleted this round; kept so the bytes survive somewhere |
| DELETE-DUP-PROD skipped at delete time (§6) | 41 | 41,561,930 (39.6 MB) | production rebuilt under them after the audit; survivor no longer verifies; now unique older versions |
| png-other | 7 | 731,983 | 3× `scratch-refanout-it2/pages-crop-*.png` (render-output naming, but no SHA match to any candidate — no survivor established) + 4× `scratch-refanout-nl/it-d1-d3-before-after/*.png` (before/after comparison renders, render-output status not established by the path rules). Kept per "cannot verify → keep". |
| KEEP-C-TWIN (c) | 9 | 25,655,264 | italic-fix1 print + 8 SVGs: sole surviving copies of that source version (see §4) |
| all evidence / sources / KITs / assets / text.md / scripts | — | — | never in scope, untouched everywhere |
| all off-limits dirs | — | — | untouched (verified by manifest grep: no deleted path is under any off-limits dir or `backup/`) |

## §6 — the 41 delete-time skips (kept, correct outcome)

All `DELETE-DUP-PROD`, all "no survivor verifies now": between the audit's production hash and
the delete, workers rebuilt these editions' production files, so the recorded production survivor
no longer matches the candidate's SHA. The candidates are now the only copies of the older
builds, so keeping them is right. Clusters (all SVGs except one print PDF):
- pt-ru: 9 (refanout-pt freeze-pt-ru p1–p8 + backup-old p5)
- ru-ko: 16 (refanout-ru records/ko freeze print + p1–p8; backup-old p3–p5; fanout-ru ko freeze p3 + freeze2 p3–p5)
- ru-zh-tw: 13 (refanout-ru records/zh-tw freeze p1–p7 — p8 deleted fine; backup-old p3–p5; fanout-ru zh-tw freeze p3–p5)
- en p1-front: 2 (fanout-en2 fanout/de, /nl freeze-final)
- pt ru-freeze1 p5: 1 (fanout-pt)
(The 41 are listed in full in `delete-summary-2.json` under `skipped`.)

## §7 — bug found and fixed in-run: (b) survivor-prefix bug

The first delete run skipped all 32 (b) SVGs as "no survivor verifies now". Cause: my bug, not a
missing survivor — `resolve2.py` carried the (b) survivor paths straight from round-1's
`/tmp/verify2.json` (`scratch-ru-rerun-R1/...`, no root prefix), and `delete2.py`'s survivor check
only recognises `G:`/`W:`/`PROD:`-prefixed paths, so it treated them as notes and skipped every
file. Fixed with `/tmp/fixup_b.py` (correct `G:` prefix, same per-file re-verification): all 32
deleted, 0 skipped, survivors re-verified fresh (R1 files still present with matching SHAs).
Lesson: survivor-path normalisation belongs in the resolver, not the deleter; round 1's raw
relative paths must be absolutised before use. The fix-up results are appended to
`deleted-manifest-2.tsv` and folded into `delete-summary-2.json` (`fixup_b_*` fields).

## What was NOT done

- No file under `production/` read for writing, modified, or deleted. No commit / push / lint.
  No build / render. No off-limits dir touched. No directory removed.
- The `scratch-ru-rebuild-C/` wave-C ru-ko Medium build ("before" reference) untouched.
- Kept files were hashed read-only; two kept files vanished mid-audit (workers deleted
  `scratch-gatefix-ja-koit/builds/ko-it-fix1/build-copy/*` and
  `scratch-svg-refresh/freeze-ru-it/build-copy/*` during the kept-map hash — recorded as
  `KEPT HASH FAIL` lines in the audit output; they simply never entered the kept map, so no
  deletion ever depended on them).

## Files produced by this run

- `deleted-manifest-2.tsv` — full deletion manifest (path, size, SHA-256, verdict, survivor used), 4,521 rows.
- `delete-summary-2.json` — counts/bytes per verdict, df before/after, backup-it2 check, skipped list (73: 41 genuine + 32 recovered in the fix-up), fix-up fields.
- This file (`CLEANUP-LOG-2.md`).
- Working scripts (not deliverables, in /tmp): `audit2.py`, `resolve2.py`, `fix_png.py`,
  `delete2.py`, `fixup_b.py`, plus `/tmp/audit2.json` (per-file verdicts) and `/tmp/resolve2.json`
  (final delete list with survivor lists).
