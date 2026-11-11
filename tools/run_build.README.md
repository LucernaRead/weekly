# run_build.py — scratch-build wrapper

**One rule, enforced by code instead of by briefs: a rebuild never writes
into `production/` unless you say so out loud.**

## The problem it fixes

W47 had fifteen run.py in-place rewrite incidents (run-log.md + ledger.md,
2026-11-11). Same shape every time: a worker rebuilt an edition in
scratch, but the copy's `OUT` / `BASE` still pointed at the real
`production/<week>/<slug>/` tree, so `run.py` / `render.py` rewrote the
shipped `svg/*.svg` — in the worst case (#11) also `cards/*.png` and the
print PDF — in place. All fifteen rewrites were byte-identical (zero
content damage), but the guard was a sentence in a brief, and hand-sed
kept missing it:

| Trigger | Incidents |
|---|---|
| `sed` pattern only matched absolute paths; `OUT` used `~/...` | #1, #6 |
| `run.py` run before the absolute `OUT` was rewritten at all | #2, #5, #7, #8, #10, #12, #13, #14, #15 |
| sync copied production sources over the already-patched `OUT` line | #3 |
| `content*.py:6` / `:10` hardcoded a literal production absolute path | #4, #11, #14, #15 |
| `runpy` executed inside the edition dir itself (registry read) | #9 |
| `render.py` `BASE` also hardcoded, so cards + print PDF were rewritten | #11 |
| freeze baseline given an already-patched copy as its `--build` | freeze-baseline trap #4 (related; `freeze.py` repoints, but only paths matching its regex) |

## What the wrapper does

1. **Never runs in place.** It copies `--build` to `<out>/build-copy`
   and runs the copy. `__file__`-relative `OUT`/`BASE` (535 content
   files) then resolve inside the copy by construction.
2. **Repoints by resolution, not by spelling.** Every quoted path
   literal in the copy's `.py` files is `expanduser` + `realpath`
   resolved; anything landing inside `production/` is rewritten to the
   scratch tree (edition dir → `build-copy`, `.../svg` →
   `build-copy/svg`, anything else under `production/` →
   `<out>/external/...`). This catches the `~` form sed missed.
3. **Verifies before running.** If any `.py` in the copy still names
   the real production tree, it aborts (exit 2) without executing
   anything. A missed redirect is a hard failure.
4. **Refuses `--out` inside `production/`** unless `--allow-production`
   is passed explicitly — checked before creating anything.
5. **Snapshots production before/after** (SHA-256 of the whole edition
   dir) and aborts if anything changed — defence in depth for write
   paths the repoint cannot see.
6. **Logs the resolved real paths** of every step to
   `<out>/run-build.log`, so an audit can see exactly where the build
   wrote. It also picks the interpreter the way `tools/freeze.py` does
   (ko family → system python3 / Pillow 10, else `tools/venv` /
   Pillow 13) and aborts on a mismatch.

## Usage

```sh
# rebuild an edition's SVGs + cards + PDFs into scratch
python tools/run_build.py --build production/2026-w47/core-zh-cn \
    --out tools/scratch/run-build/zh-cn-1

# SVG rebuild only (freeze-style), explicit out, dry run first
python tools/run_build.py --build production/2026-w47/2026-w47-it-en \
    --out ~/scratch/it-en-rebuild --steps run --dry-run

# deliberate --out inside production/ (a fixer who wants the build copy
# next to the edition): the build still runs in <out>/build-copy, never
# in the edition dir itself
python tools/run_build.py --build production/2026-w47/2026-w47-it-en \
    --out production/2026-w47/2026-w47-it-en --allow-production --steps run
```

Exit codes: `0` built; `1` the build/render step itself failed;
`2` wrapper refusal (production target, unrepointed reference left in
the copy, production files changed, wrong interpreter).

## Notes

- The wrapper does not modify any production `run.py` / `render.py` /
  `content*.py`. It works with the existing call shapes: `run.py` when
  present, else `import content12, content34, content56, content7,
  content8` in order (same as `tools/freeze.py` baseline); then
  `render.py` when present.
- Default `--out` is `tools/scratch/run-build/<slug>-<timestamp>/`
  (`tools/scratch/` is gitignored). `--production-root` overrides the
  production tree (used by the tests, which build against a fake tree).
- Importable helpers: `repoint_tree`, `verify_no_production_refs`,
  `snapshot_dir`, `is_within`, `resolve`.
- Tests: `hidden_files/w47/scratch-run-build/` on the goals side
  (refusal case + scratch-redirect case, incl. the `~` form).
- Adoption is a W47+ rollout item: briefs should tell builders and
  proofreaders to run rebuilds through this wrapper instead of
  hand-copying + hand-sed. `freeze.py` keeps its own repoint for the
  baseline subcommand; this wrapper is the general rebuild path.
