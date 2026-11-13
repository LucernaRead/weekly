# FIX-LOG — W47 ru-nl fix2 (KIT-only doc repair)

- Task: re-issue `WEEKLY-KIT.md` identity numbers to the fix2 (re-proof-verified) deliverables. KIT only.
- File changed: `~/workspace/weekly-git/production/2026-w47/2026-w47-ru-nl/WEEKLY-KIT.md` (17,754 → 18,290 bytes, +536 B = one added bullet).
- Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ru-nl2/` (probe.txt, snapshot-before/after.txt, sha-before/after.txt, grep-old-before.txt, grep-new-before.txt).
- No commit, no push. No source, SVG, PDF, text.md, or any other file touched. No rebuild, no re-proof.

## 0. Probe (before work)

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` (OK).
- Real scratch write: `scratch-fix-ru-nl2/probe.txt` (`probe-ru-nl2 2026-11-11T19:29:34Z disk-writable`) OK.
- `TMPDIR` = scratch dir throughout. Python (page-count check only) = repo venv `tools/venv/bin/python`.
- Repo house rules read: `~/workspace/weekly-git/AGENTS.md` (content-only repo; KIT edit is production-source doc work, no lint/insert step required for a KIT-only change; no commit made per task).

## 1. Disk verification (before any edit) — all match the task's re-proof values

`sha256sum` + `wc -c` on the production dir, 2026-11-11 ~19:29 UTC; file mtimes 18:03–18:07 UTC same day:

| Artifact | SHA-256 (disk) | Bytes (disk) |
|---|---|---|
| `Lucerna-VOL4-ru-nl.pdf` (print) | `5843ae6b80ac7e38298ec33d565b19e49d73dc165e6d18ffeec5bdddd4982fa2` | 21,291,643 |
| `Lucerna-VOL4-ru-nl-web.pdf` (web) | `d3f016d58cb7b37a35cbf5b05e9a012c49bff6a116baf716db39aca56500b3eb` | 3,387,332 |
| `2026-w47-ru-nl.text.md` | `8ac1336dbc521f510747d2a838a52e763d6452a81f8ea75ee6fc7c7687942423` | 64,051 |

Cross-check: identical to the independent re-proof record `hidden_files/w47/scratch-reproof-ru-nl1/GATE-LOG.md` G0 and `PROOF-NOTE.md` §1 (all three "MATCHES coordinator"). Page counts re-verified with repo-venv PyMuPDF: print 8 pages, web 8 pages.

## 2. Changes (line numbers = post-edit KIT)

| # | Location | Before | After |
|---|---|---|---|
| 1 | §5 L53 print PDF | `21,315,805` bytes, SHA `8982ce29eaf2bc57661a089b9bf0bd8021444130e2e0c9aa505f9176de4a1e17` | `21,291,643` bytes, SHA `5843ae6b80ac7e38298ec33d565b19e49d73dc165e6d18ffeec5bdddd4982fa2` |
| 2 | §5 L54 web PDF | `3,387,072` bytes, SHA `abc3ec69f695129c9e248dae36880da1754f6af5ef32b62f5438435458512593` | `3,387,332` bytes, SHA `d3f016d58cb7b37a35cbf5b05e9a012c49bff6a116baf716db39aca56500b3eb` |
| 3 | §5 L57 `.text.md` | `64,053` bytes | `64,051` bytes (SHA `8ac1336dbc521f510747d2a838a52e763d6452a81f8ea75ee6fc7c7687942423`, recorded here, not added to the KIT line — that line carries no SHA by format) |
| 4 | §7 L80 §1.1 spot-checks (sweep find) | `web 3,348,435 bytes < 7 MB` | `web 3,387,332 bytes < 7 MB` |
| 5 | §7 new L85 bullet (re-proof note) | — (D7 fix1 section had no re-proof note) | Added: "Re-proof (a) independent verification (2026-11-11, `hidden_files/w47/scratch-reproof-ru-nl1/`): verdict ZERO DEFECTS — content cleared as final. D7 verified fixed: PIL true-ink U+2019 advance 18.00 px → U+0027 advance 5.00 px (subtitle advance 229.77 → 216.38 px); band raster thema → 's gap 3 SVG px on card/print/web, exactly the same-band median (neighbourhood gaps 1–5 px). text.md −2 B (64,053 → 64,051 B) is exactly the UTF-8 ’ (3 B) → ' (1 B) delta; the §5 SHAs above are the re-proof-verified values." |

Notes on #4: `3,348,435` was NOT in the task's grep list, but the full-KIT sweep found it as a current-state claim in L80 that matched neither the old L54 value (3,387,072) nor disk (3,387,332) — a stale build-2-era figure never updated at the re-fanout, while L53/L54/L57 were. Fixed to the disk-verified value; no `issues/` copy of ru-nl exists that it could have referred to (checked — `issues/2026-w47/` has no ru-nl dir).

Notes on #5: values corroborated verbatim from the re-proof record, not just the task brief — `PROOF-NOTE.md` L25 (PIL 18.00 / 5.00 px, subtitle 229.77 → 216.38), L27 (band raster 3 SVG px, neighbourhood gaps 1–5 px, median 3), L23 (−2 B = ’→' delta), and `PROOF-NOTE.md` header "Verdict: (a) ZERO DEFECTS". KIT L81 "Visual check" line ("No overflow, no overlap, no clipped text") was confirmed consistent with re-proof (a) (GATE-LOG: all 8 cards read, no overflow/overlap/clipping; 42/42 CLEAR; key cross-check 0 mismatches) and left un-reworded, per task.

## 3. Retained history (deliberately NOT changed)

- L84 re-fanout paragraph: "`(63,984 → 64,053 bytes)`" — historical record of the fix1 re-fanout diff. Retained.
- L85 new bullet: "`(64,053 → 64,051 B)`" — explicitly framed as the pre-fix value in the fix2 delta. Retained as history annotation.
- L56/L78 per-build character counts (31,014 chars, build 2) vs L84 (31,087 chars, re-fanout): per-build historical records, not current-state identity claims — left untouched, out of fix2 scope.

## 4. Post-edit verification

- Old-number grep on the edited KIT: `8982ce29` 0, `abc3ec69` 0, `21,315,805` 0, `3,387,072` 0, `3,348,435` 0.
- `64,053` remaining hits: 2 — L84 (history, see §3) and L85 (history annotation, see §3). The task's zero-hit list does not include `64,053`.
- New values present: L53, L54, L57, L80, L85 (grep-verified).
- Snapshot comparison (`find . -type f -printf '%s %p'`, before vs after, whole production dir): exactly one line differs — `./WEEKLY-KIT.md` 17754 → 18290. Every other file byte-identical.
- Deliverable SHA re-check after edit: `sha-before.txt` vs `sha-after.txt` identical — print/web/text.md untouched.
- `git status` on the repo shows the production dir untracked (`?? production/2026-w47/2026-w47-ru-nl/` — never committed), so the snapshot diff above is the change evidence, not a git diff. No commit/push made, per task.

## 5. Not done / open

- None. All five task items (1–5) completed; verification criteria met.
