# Web PDF backfill — text-layer replacement for all 260 weekly web PDFs

One-time backfill (user 2026-10-28): old web PDFs are 8 full-page JPEGs
with no text layer (pdftotext = 0 bytes, invisible to search engines).
New builder `tools/webpdf.py` produces 2-3 MB PDFs with text
byte-identical to the print PDF.

## Pre-flight (2026-10-28 ~19:05 EDT)
- weekly-git `git status` clean; HEAD == `git ls-remote origin main` ==
  fac0f2eb9e116e53fee38e928fbd8769b7b829ec (last commit 2026-10-28
  09:59 UTC, ~13h before start — no other process pushing).

## Mapping (260/260, 0 unmatched, 0 problems)
- Method: index.json `pdfSha256` matched against sha256 of every PDF
  under `files/` (543 files hashed).
- 248 matched uniquely on first pass.
- 12 W43 editions matched 2 files each: the real edition dir (svg/ =
  8 SVGs) + a staging copy under `files/weekly-pdf-bundle/issues/`
  (no SVGs). Resolved exactly: svg-dir candidate agrees with the
  fallback naming pattern in all 12 cases (cores vol1/vol4, fan-outs
  weekly-report-<target>-<native>, zh cores unhyphenated zhcn/zhtw).
  Bundle copies are NOT render sources and are NOT touched by this
  backfill (out of scope; flagged in the final report as stale).
- Full mapping: `mapping.json` in this dir.

## Pilots (coordinator, verified before fan-out)
- 2026-w45-en-de: 2,143,836 bytes, 46,498 text bytes, BYTE-IDENTICAL
  to print PDF text. PASS.
- 2026-w43-en-zh-cn: 1,962,329 bytes, 49,288 text bytes,
  BYTE-IDENTICAL to print PDF text. PASS.
- Both already rendered in `out/`; excluded from worker slices.

## Render workers (5 slices, 258 editions)
- slice-1: 52 (2026-w43-de-en … 2026-w43-it-ru)
- slice-2: 52 (2026-w43-it-zh-cn … 2026-w43-ru-ja)
- slice-3: 52 (2026-w43-ru-ko … 2026-w45-es-ko)
- slice-4: 51 (2026-w45-es-nl … 2026-w45-nl-en)
- slice-5: 51 (2026-w45-nl-es … 2026-w45-zh-tw-ru)
- Workers render + verify ONLY (no git, no files-dir writes).
- Workers write results incrementally (results-N.json).

## Worker incident 2026-10-28 ~19:18 EDT (runtime restart drain)
- Slice-1 + slice-3 workers errored at submission ("restart drain in
  progress; rejecting new submission") — runtime issue, not a task
  failure. Disk check showed slice-1: 8 verified PASS entries kept,
  slice-3: 6 PDFs on disk but 0 verified entries (untrusted).
- Recovery: slice-1b worker re-dispatched for the remaining 44
  editions (results-1b.json); slice-3 worker re-dispatched for the
  full 52 (results-3.json). Slices 2/4/5 kept running (5/8/8 PASS at
  last check).

## Slice-1b result (2026-10-28 ~20:21 EDT): 43 PASS, 1 FAIL
- FAIL: 2026-w43-fr-nl — byte-identity gate failed. Investigation
  (coordinator): NOT a builder bug. The new PDF faithfully renders
  the current SVGs (p3-culture.svg numbers items 1./2./3./4./5./
  14./15.…). The shipped print PDF numbers the same page-3 items
  exactly +26 higher (30./31./40./41./42.…). Pre-existing
  source/print divergence in this edition; pushing the new PDF
  would visibly change shipped exercise numbers, which is a
  content change beyond this format-only backfill. Decision: fr-nl
  is NOT pushed; logged as failed with this reason for the parent
  to adjudicate (fix SVGs vs rebuild print vs accept new
  numbering). All other fr-* editions in slice-1b passed
  byte-identical, so the divergence is specific to fr-nl, not
  systematic.
- Slice-1 total: 51 PASS, 1 FAIL (fr-nl).

## Push status (serialized by coordinator only)
- RENDERS COMPLETE: 259/260 verified + queued (2 pilots + 257 worker
  PASS). All 7 workers finished; no worker still running.
- Failed: 1 (2026-w43-fr-nl byte-identity, see below)
- Still rendering: 0
- Slice status: slice-1 51/52 (1 FAIL), slice-1b 43/44, slice-2 52/52
  COMPLETE (ja-zh-tw via coordinator retry PASS), slice-3 52/52
  COMPLETE, slice-4 51/51 COMPLETE, slice-5 51/51 COMPLETE
- Copied to files dirs: 1 (2026-w45-en-de, pilot test copy only)
- Committed + pushed to weekly-git: 0/260
- Note: slice-4/slice-5 workers report the VM restarted mid-run
  (uptime 1 min after restart, /tmp wiped); both recovered via
  incremental results. Workspace out/ + results files survived.

## PAUSED — repo work suspended 2026-10-28 ~20:30 EDT
- A concurrent process is committing W45/W43 COVER additions in this
  same clone (reflog: 00:04–00:27 UTC at pause time, STILL ACTIVE at
  last check 00:47 UTC — latest local commit 4d60730 "Add
  2026-w45-cover-ko" 00:45:47 UTC, author Beacon, LOCAL-ONLY —
  ls-remote still fac0f2e). Per the backfill's pre-flight rule the
  coordinator does NOT touch the repo until it finishes.
- The coordinator's one test change (2026-w45-en-de PDF, working
  tree only, never committed) was REVERTED; `git status` is clean.
  The new PDF survives in scratch/out/ + the files-dir copy.
- BLOCKER 2 (independent): lint cannot pass while covers/ sits at
  repo root — lint.mjs ROOT_ALLOW has no 'covers' entry, and
  report() exits 1 BEFORE --write writes index.json. So even after
  the covers process finishes, `lint --write` / `--require-pdf`
  cannot go green in weekly-git unless the parent decides: add
  'covers' to ROOT_ALLOW, move covers out of root, or otherwise
  resolve. The coordinator will NOT change lint.mjs or delete
  covers/ unilaterally (both out of scope; covers is another
  process's fresh work).
- ALSO FOUND: lint --write does NOT rewrite .md frontmatter — it
  only regenerates index.json FROM frontmatter (pdfBytes/pdfSha256
  come from the .md). Each backfill edition therefore needs its
  .md frontmatter updated to the new size/sha BEFORE lint --write,
  and the commit must include PDF + .md + index.json (not PDF +
  index.json as the brief assumed). AGENTS.md confirms: "pdfBytes
  与 pdfSha256 从最终定稿的网页版 PDF 实测" and "把生成的 index.json
  和 md 一起提交".
- Renders continue (workers never touch git); the queue is held
  until the parent serializes repo access.

## Failed / stuck list
- 2026-w43-fr-nl: byte-identity gate failed. New PDF faithfully
  renders current SVGs (p3 numbers 1./2./3./4./5./14./15.…); shipped
  print PDF numbers the same page-3 items exactly +26 higher
  (30./31./40./41./42.…). Pre-existing source/print divergence;
  pushing would visibly change shipped exercise numbers — content
  change beyond this format-only backfill. NOT pushed; needs
  parent adjudication (fix SVGs vs rebuild print vs accept).
- 2026-w43-ja-zh-tw: RESOLVED by coordinator retry (results-retry.json).
  Worker render timed out (>300s) under 5-worker contention (load
  ~11); the killed render left a partial 3,288,794-byte PDF (sha
  4aa9de4a…) in out/, which the coordinator DELETED (hazard: must
  never be pushed). Retry took ~145s (heavy CJK-TC font subset),
  output 3,288,794 bytes (same size, different sha 62cb786c…),
  45,647 text bytes, BYTE-IDENTICAL to print. Now queued as PASS.
  (Note: build_queue.py still lists the old worker FAIL in its
  EXCLUDED echo, but the retry PASS supersedes it — queue.json
  contains ja-zh-tw.)

## fr-nl FIX (2026-10-29, user decision: fix SVGs to shipped numbering)
- Full-text diff proved the ONLY divergence was numbering, uniform +26:
  p3-culture.svg labels 1.–18. → 27.–44.; p4-sport.svg labels 19.–36. →
  45.–62. (incl. range 24–27. → 50–53. and inline 24./25./26./27. vocab
  labels → 50./51./52./53.). Pages 1,2,5,6,7,8 already matched print
  exactly; p8 answer keys already used shipped numbering (no p8 change).
- Backups: original p3/p4 SVGs + failed web PDF in fr-nl-fix/.
- Gap analysis before edit: min label-to-content gap 70px; widening
  1-char labels to 2-char adds ~1 digit width — no overlap risk.
- Edit: exact-element replacement only (37 labels total), asserted
  once-each + old labels gone + new labels present.
- Occlusion audit (selftest OK): edited edition = 1 flag BOXTITLE on
  p2-vie.svg ONLY (0 flags on p3/p4). Proven PRE-EXISTING: audit of
  original SVGs shows the identical p2 flag (p2 untouched, mtime Oct
  22; 0.7px ink/border crossing). Not a new overlap; p2 NOT touched
  (format-only backfill scope).
- Rebuild: webpdf.py → out/2026-w43-fr-nl.pdf, 1,873,296 bytes, 8 pp,
  sha 8b0f896f…, pdftotext 50,491 bytes BYTE-IDENTICAL to print text.
- Visual: p3 + p4 rendered (fr-nl-fix/page-3.png, page-4.png) and
  eyeballed — labels 27–44 / 45–62 clean, no overlaps.
- queue.json: fr-nl appended (260 entries); manifest.json: all 260
  out/ PDFs sha+size re-verified, all < 7 MB.

## PUSH COMPLETE (2026-10-29)
- Worktree ~/workspace/weekly-backfill (branch backfill-webpdf, from
  origin/main fac0f2e). Per-edition commits: PDF + .md (pdfBytes/
  pdfSha256 only) + index.json (lint --write), 1 edition/commit,
  batches of 3, each batch proven by ls-remote == HEAD.
- 260/260 pushed to main. Final HEAD e33bc3790c7b1c2e87fd0c5e17394b078fb07334
  (260 backfill commits on top of fac0f2e). Driver killed once
  mid-run (~02:32, runtime restart) at 96 committed / 93 pushed;
  resumed cleanly from push-state.json (backlog pushed first).
  Tunnel bad phases (push rc=128 / broken pipe) hit many batches;
  all landed via retry loop + same-HEAD manual assists.
- Final verification on main: lint --require-pdf green (OK:260,
  index.json latest); ls-remote == HEAD e33bc37; 130 PDFs W43 +
  130 PDFs W45; all 260 repo PDFs sha+size == manifest, all 260 .md
  frontmatter + index.json entries match; 5 spot-checks (incl.
  fr-nl) text byte-identical to print, all < 7 MB. Tree clean.
- Scope note: backfill commits touch ONLY pdfBytes/pdfSha256
  frontmatter + PDF + index.json. The .md body fixes (boilerplate,
  excerpt lines, titles, excerpt language, abstract framing) are a
  separate follow-up scheduled AFTER this push; nothing in this
  push blocks or pre-empts them.
