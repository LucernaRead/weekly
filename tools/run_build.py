#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run_build.py — shared scratch-build wrapper for weekly editions.

Why this exists
---------------
W47 saw FIFTEEN run.py in-place rewrite incidents (run-log.md, ledger.md
2026-11-11: #1 zh-cn-de, #2 zh-cn-fr, #3 zh-cn-es fix1, #4 zh-cn-it fix1,
#5 zh-cn-ru proof1, #6 sed-miss, #7 zh-cn-ko proof1, #8 zh-cn-ko proof1,
#9 nl-pt proof1b, #10 it-en proof2, #11 it-ja proof2, #12 it-es proof2,
#13/#14/#15 proof2 re-runs). Every one has the same shape: a worker
copied / ran a build in scratch, but the copy's OUT/BASE still pointed
at the real production/ tree, so run.py / render.py rewrote the shipped
svg/*.svg (sometimes also cards/*.png and the print PDF) in place.
All fifteen were byte-identical rewrites (zero content damage), but the
rule "redirect before you run" was bypassed fifteen times by hand-sed,
and hand-sed keeps missing: a `~` in the path, a sed pattern that only
matches absolute paths, a forgotten --out, a sync that overwrote the
patched OUT line, a runpy executed inside the edition dir itself.

This wrapper makes the safe path the only path:

  1. It NEVER runs build code in place. It always copies the edition
     dir into <out>/build-copy and runs the copy.
  2. It repoints every literal production path in the copy (OUT, BASE,
     and any other quoted path resolving inside production/) to the
     scratch tree — including `~`-prefixed paths (incident #6) and
     paths reached through symlinks — by resolving each candidate
     string, not by pattern-matching the spelling.
  3. It VERIFIES the copy before running: if any .py in the copy still
     references the real production tree, it aborts (exit 2) without
     running anything. A missed redirect is a hard failure, not a
     silent in-place rewrite.
  4. It refuses --out inside production/ unless --allow-production is
     passed explicitly (exit 2, before creating anything).
  5. It snapshots the production edition dir before the run and
     re-hashes it after: if anything in production changed, it aborts
     with the list of changed files (exit 2). Defence in depth for
     write paths the repoint cannot see (e.g. a path built at runtime).
  6. It logs the resolved real paths of OUT/BASE at every step, so a
     later audit can see exactly where the build wrote.

Usage (run from the repo clone, tools/venv/bin/python):
  python tools/run_build.py --build production/2026-w47/core-zh-cn \
      --out tools/scratch/run-build/zh-cn-1
  python tools/run_build.py --build production/2026-w47/2026-w47-it-en \
      --out ~/scratch/it-en-rebuild --steps run,render
  python tools/run_build.py --build <edition> --out <scratch> --dry-run
  python tools/run_build.py --build <edition> --out <scratch> \
      --steps run          # SVG rebuild only, like freeze.py baseline

Steps: "run" executes run.py in the copy (or imports content12/34/56/7/8
in order when run.py is absent, same as tools/freeze.py); "render"
executes render.py in the copy (skipped with a note when absent).
Default: run,render.

Interpreter: --python overrides. Otherwise ko-family builds
(core-ko, <week>-ko-*) use /usr/bin/python3 (Pillow 10, per core-ko
WEEKLY-KIT.md fix #15) and everything else uses tools/venv/bin/python
(Pillow 13), mirroring the runtime guard in tools/freeze.py.

Exit codes: 0 = built, outputs under <out>/build-copy (+ <out>/svg when
a script redirects there); 1 = the build/render step itself failed;
2 = wrapper refusal (production target, unrepointed reference left in
the copy, production files changed, wrong interpreter).

This wrapper does NOT modify any production run.py / render.py /
content*.py. Adoption by builders/proofreaders is a W47+ rollout item;
see tools/run_build.README.md.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time

CONTENT_ORDER = ["content12.py", "content34.py", "content56.py",
                 "content7.py", "content8.py"]
# Literal markers that must never survive in a build copy.
FORBIDDEN_MARKERS = (
    "weekly-git/production",
    "lucernaread-social-media-operations/files",
    "files/weekly-report",
)
QUOTED_RE = re.compile(r"""(["'])([^"']*)\1""")
REQUIRED_PILLOW_MAJOR = 13
KO_REQUIRED_PILLOW_MAJOR = 10


# ---------------- small helpers -------------------------------------------
def log(msg, logf=None):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    if logf is not None:
        logf.write(line + "\n")
        logf.flush()


def resolve(path):
    """expanduser + abspath + realpath: the path the OS will actually use."""
    return os.path.realpath(os.path.abspath(os.path.expanduser(path)))


def is_within(path, root):
    path, root = resolve(path), resolve(root)
    return path == root or path.startswith(root + os.sep)


def repo_root():
    return resolve(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))


def is_ko_family_path(path):
    parts = resolve(path).split(os.sep)
    return any(p == "core-ko" or re.match(r"^\d{4}-w\d+-ko-", p) for p in parts)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot_dir(d, exclude=None):
    """{relpath: (sha256, mtime_ns)} for every file under d, minus caches
    and minus the exclude subtree (the scratch out dir, when it lives
    inside d — e.g. an --allow-production out — must not count as a
    production change)."""
    snap = {}
    excl = resolve(exclude) if exclude else None
    for root, dirs, files in os.walk(d):
        dirs[:] = [x for x in dirs if x != "__pycache__"
                   and not (excl and is_within(os.path.join(root, x), excl))]
        for fn in sorted(files):
            p = os.path.join(root, fn)
            if excl and is_within(p, excl):
                continue
            rel = os.path.relpath(p, d)
            try:
                snap[rel] = (sha256(p), os.stat(p).st_mtime_ns)
            except OSError:
                snap[rel] = ("<unreadable>", 0)
    return snap


def snapshot_diff(before, after):
    """[(relpath, kind)] where kind is added/removed/changed."""
    out = []
    for rel in sorted(set(before) | set(after)):
        if rel not in before:
            out.append((rel, "added"))
        elif rel not in after:
            out.append((rel, "removed"))
        elif before[rel][0] != after[rel][0]:
            out.append((rel, "changed"))
    return out


# ---------------- repoint ---------------------------------------------------
def map_production_path(resolved, edition_dir, production_root, out_dir, copy_dir):
    """Where a path that pointed inside production/ must point instead."""
    if resolved == resolve(edition_dir):
        return copy_dir
    if is_within(resolved, edition_dir):
        return os.path.join(copy_dir, os.path.relpath(resolved, edition_dir))
    if resolved == resolve(production_root):
        return out_dir
    rel = os.path.relpath(resolved, production_root)
    return os.path.join(out_dir, "external", rel)


def repoint_tree(copy_dir, edition_dir, production_root, out_dir, logf=None):
    """Rewrite every quoted path literal in the copy's .py files that
    resolves inside production/ to its scratch mapped path.

    Returns (touched, mapped): touched = [relpath of rewritten files],
    mapped = [(original literal, new path)] for the log.
    Resolution (expanduser + realpath) is what catches the spellings a
    sed misses: `~/workspace/...`, absolute paths, symlinked paths.
    `__file__`-relative OUT/BASE need no rewrite: they resolve inside
    the copy by construction, and are logged as such by the caller.
    """
    touched, mapped = [], []
    for root, dirs, files in os.walk(copy_dir):
        dirs[:] = [x for x in dirs if x != "__pycache__"]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            s = open(p, encoding="utf-8").read()

            def repl(m):
                q, inner = m.group(1), m.group(2)
                if "/" not in inner:
                    return m.group(0)
                if not (inner.startswith(("~", "/", "workspace/"))
                        or "production/" in inner or "files/" in inner):
                    return m.group(0)
                # Resolve relative literals against the copy dir, as the
                # running script would see them.
                cand = (os.path.join(copy_dir, inner) if not inner.startswith(("~", "/"))
                        else inner)
                resolved = resolve(cand)
                if not is_within(resolved, production_root):
                    return m.group(0)
                new = map_production_path(resolved, edition_dir,
                                          production_root, out_dir, copy_dir)
                mapped.append((inner, new))
                return f"{q}{new}{q}"

            s2 = QUOTED_RE.sub(repl, s)
            if s2 != s:
                open(p, "w", encoding="utf-8").write(s2)
                touched.append(os.path.relpath(p, copy_dir))
    return touched, mapped


def verify_no_production_refs(copy_dir, edition_dir, production_root, out_dir):
    """After repoint: no .py in the copy may still name a write target in
    the real production tree. Returns [offending "file:line: snippet"]
    (empty = clean).

    Each quoted path-like literal is RESOLVED (same as repoint) and
    flagged only when it lands inside production/ AND outside the
    scratch out dir — so a repointed path that merely contains the
    production root as a prefix (e.g. <out>/build-copy under an
    --allow-production out inside production/) is not a false alarm.
    A bare forbidden marker outside any out-dir path is also flagged
    (catches paths built by joining fragments).
    """
    bad = []
    out_r = resolve(out_dir)
    for root, dirs, files in os.walk(copy_dir):
        dirs[:] = [x for x in dirs if x != "__pycache__"]
        for fn in files:
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            for i, line in enumerate(open(p, encoding="utf-8"), 1):
                flagged = False
                for m in QUOTED_RE.finditer(line):
                    inner = m.group(2)
                    if "/" not in inner:
                        continue
                    if not (inner.startswith(("~", "/", "workspace/"))
                            or "production/" in inner or "files/" in inner):
                        continue
                    cand = (os.path.join(copy_dir, inner)
                            if not inner.startswith(("~", "/")) else inner)
                    resolved = resolve(cand)
                    if (is_within(resolved, production_root)
                            and not is_within(resolved, out_r)):
                        bad.append(f"{os.path.relpath(p, copy_dir)}:{i}: "
                                   f"{line.strip()[:160]}")
                        flagged = True
                        break
                if flagged:
                    continue
                for marker in FORBIDDEN_MARKERS:
                    if marker in line and out_r not in line:
                        bad.append(f"{os.path.relpath(p, copy_dir)}:{i}: "
                                   f"{line.strip()[:160]}")
                        break
    return bad


# ---------------- interpreter ----------------------------------------------
def pick_python(build_dir, explicit, logf=None):
    if explicit:
        return resolve(explicit)
    if is_ko_family_path(build_dir):
        cand = "/usr/bin/python3"
        log(f"interpreter: ko family -> {cand} (Pillow 10, core-ko fix #15)",
            logf)
        return cand
    venv_py = os.path.join(repo_root(), "tools", "venv", "bin", "python")
    if os.path.exists(venv_py):
        log(f"interpreter: default stack -> {venv_py} (Pillow 13)", logf)
        return venv_py
    log(f"interpreter: no tools/venv found, using {sys.executable}", logf)
    return sys.executable


def check_pillow(python, build_dir):
    """Mirror tools/freeze.py: ko family needs Pillow 10, else 13.
    Returns 0 or an error string."""
    required = (KO_REQUIRED_PILLOW_MAJOR if is_ko_family_path(build_dir)
                else REQUIRED_PILLOW_MAJOR)
    proc = subprocess.run(
        [python, "-c", "import PIL; print(PIL.__version__)"],
        capture_output=True, text=True)
    ver = proc.stdout.strip()
    major = ver.split(".")[0] if ver else None
    if major != str(required):
        return (f"wrong interpreter: {python} has Pillow {ver or 'MISSING'}, "
                f"family requires Pillow {required}.x "
                f"({'ko family -> /usr/bin/python3' if required == 10 else 'default -> tools/venv/bin/python'}; "
                f"see tools/freeze.py runtime guard)")
    return 0


# ---------------- run ---------------------------------------------------------
def run_step(python, copy_dir, argv, label, logf):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    log(f"run: {' '.join(argv)} (cwd={copy_dir})", logf)
    proc = subprocess.run(argv, cwd=copy_dir, env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True)
    if logf is not None:
        logf.write(proc.stdout)
        logf.flush()
    print(proc.stdout, end="", flush=True)
    log(f"{label}: exit {proc.returncode}", logf)
    return proc.returncode


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--build", required=True,
                    help="edition dir to rebuild (core-<t> or <week>-<t>-<n>)")
    ap.add_argument("--out", help="scratch dir (default: "
                    "tools/scratch/run-build/<slug>-<timestamp>)")
    ap.add_argument("--steps", default="run,render",
                    help="comma list: run,render (default run,render)")
    ap.add_argument("--python", help="interpreter override")
    ap.add_argument("--production-root",
                    help="production tree root (default: <repo>/production)")
    ap.add_argument("--allow-production", action="store_true",
                    help="allow --out inside production/ (the build still "
                    "runs in <out>/build-copy, never in the edition dir "
                    "itself; still snapshots before/after)")
    ap.add_argument("--keep-copy", action="store_true",
                    help="keep <out>/build-copy after a successful run "
                    "(default: it is the output, so always kept; flag is a "
                    "no-op kept for symmetry with freeze.py)")
    ap.add_argument("--dry-run", action="store_true",
                    help="copy + repoint + verify only, do not run anything")
    ap.add_argument("--log", help="extra log file (default: <out>/run-build.log)")
    args = ap.parse_args(argv)

    build = resolve(args.build)
    if not os.path.isdir(build):
        print(f"ABORT: --build is not a directory: {build}", file=sys.stderr)
        return 2
    production_root = resolve(args.production_root) if args.production_root \
        else os.path.join(repo_root(), "production")
    slug = os.path.basename(build.rstrip(os.sep))
    out = resolve(args.out) if args.out else os.path.join(
        repo_root(), "tools", "scratch", "run-build",
        f"{slug}-{time.strftime('%Y%m%d-%H%M%S')}")
    steps = [s.strip() for s in args.steps.split(",") if s.strip()]
    for s in steps:
        if s not in ("run", "render"):
            print(f"ABORT: unknown step {s!r} (want run/render)", file=sys.stderr)
            return 2

    # --- refusal gate: BEFORE creating anything under --out ---------------
    if is_within(out, production_root) and not args.allow_production:
        print(f"ABORT: --out resolves inside production/: {out}\n"
              f"  production root: {production_root}\n"
              f"  refusing to build into the shipped tree. Pick a scratch "
              f"--out, or pass --allow-production for a deliberate "
              f"in-place build.", file=sys.stderr)
        return 2

    os.makedirs(out, exist_ok=True)
    log_path = args.log or os.path.join(out, "run-build.log")
    logf = open(log_path, "a", encoding="utf-8")
    logf.write(f"\n=== run_build {time.strftime('%Y-%m-%d %H:%M:%S %Z')} ===\n")
    try:
        log(f"build source : {build}", logf)
        log(f"production   : {production_root}", logf)
        log(f"scratch out  : {out}", logf)
        log(f"steps        : {', '.join(steps)}", logf)
        in_production = is_within(build, production_root)
        log(f"build is {'inside' if in_production else 'outside'} production/",
            logf)

        # --- pre-run integrity snapshot (only when source is production) --
        # The scratch out dir is excluded: with --allow-production it can
        # legitimately live inside the edition dir.
        before = snapshot_dir(build, exclude=out) if in_production else {}
        if before:
            log(f"snapshot: {len(before)} production files hashed", logf)

        # --- copy + repoint ----------------------------------------------
        copy_dir = os.path.join(out, "build-copy")
        if os.path.exists(copy_dir):
            shutil.rmtree(copy_dir)
        shutil.copytree(build, copy_dir,
                        ignore=shutil.ignore_patterns("__pycache__"))
        log(f"copied to    : {copy_dir}", logf)
        touched, mapped = repoint_tree(copy_dir, build, production_root,
                                       out, logf)
        for orig, new in mapped:
            log(f"repoint: {orig} -> {new}", logf)
        log(f"repointed files: {', '.join(touched) or 'none'}", logf)
        if not mapped:
            log("repoint: no literal production paths found — OUT/BASE are "
                "__file__-relative and resolve inside the copy", logf)

        bad = verify_no_production_refs(copy_dir, build, production_root, out)
        if bad:
            log("ABORT: unrepointed production references left in the copy:",
                logf)
            for b in bad:
                log(f"  STILL POINTS AT PRODUCTION: {b}", logf)
            print("ABORT: build copy still references the real production "
                  "tree; refusing to run. Offending lines:", file=sys.stderr)
            for b in bad:
                print(f"  {b}", file=sys.stderr)
            return 2
        log("verify: copy is clean — no .py references the real production "
            "tree", logf)
        log(f"effective OUT/BASE resolve inside: {copy_dir} (run) and "
            f"{out}/svg (any literal /svg target)", logf)

        if args.dry_run:
            log("dry-run: stopping before execution", logf)
            return 0

        # --- interpreter --------------------------------------------------
        python = pick_python(build, args.python, logf)
        err = check_pillow(python, build)
        if err:
            log(f"ABORT: {err}", logf)
            print(f"ABORT: {err}", file=sys.stderr)
            return 2
        log(f"interpreter Pillow check OK: {python}", logf)

        # --- run steps in the copy ----------------------------------------
        rc = 0
        if "run" in steps:
            runner = os.path.join(copy_dir, "run.py")
            if os.path.exists(runner):
                rc = run_step(python, copy_dir,
                              [python, "run.py"], "run.py", logf)
            else:
                code = "import " + ", ".join(
                    f[:-3] for f in CONTENT_ORDER
                    if os.path.exists(os.path.join(copy_dir, f)))
                rc = run_step(python, copy_dir,
                              [python, "-c", code], "content import", logf)
            if rc:
                log(f"ABORT: run step failed (exit {rc})", logf)
                return 1
        if "render" in steps:
            renderer = os.path.join(copy_dir, "render.py")
            if os.path.exists(renderer):
                rc = run_step(python, copy_dir,
                              [python, "render.py"], "render.py", logf)
                if rc:
                    log(f"ABORT: render step failed (exit {rc})", logf)
                    return 1
            else:
                log("render: no render.py in copy, skipping", logf)

        # --- post-run integrity check --------------------------------------
        if before:
            after = snapshot_dir(build, exclude=out)
            diff = snapshot_diff(before, after)
            if diff:
                log("ABORT: PRODUCTION FILES CHANGED during the run:", logf)
                for rel, kind in diff:
                    log(f"  {kind}: {rel}", logf)
                print("ABORT: production files changed during the run:",
                      file=sys.stderr)
                for rel, kind in diff:
                    print(f"  {kind}: {rel}", file=sys.stderr)
                return 2
            log(f"integrity: production unchanged ({len(after)} files "
                f"re-hashed)", logf)

        produced = sorted(
            os.path.relpath(os.path.join(r, f), out)
            for r, _, fs in os.walk(out) for f in fs
            if f.endswith((".svg", ".png", ".pdf")))
        log(f"done: outputs under {out} "
            f"({len(produced)} svg/png/pdf files)", logf)
        for p in produced:
            log(f"  out: {p}", logf)
        return 0
    finally:
        logf.close()


if __name__ == "__main__":
    sys.exit(main())
