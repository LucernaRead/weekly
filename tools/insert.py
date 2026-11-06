#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert.py — the Lucerna Weekly repo-insert flow, hard-coded.

Replaces the ~15 hand-run commands per edition. Steps, each verified,
failing loudly and stopping on the first problem:
  (a) abort if the slug already exists in the repo
  (b) generate <slug>.md — frontmatter per lint.mjs; vol / exercises /
      weekStart / weekEnd / publishedAt / excerpt copied from the target's
      xEN sibling md in the repo; masthead / names / labels / discordThread
      from tables.json; pdfBytes / pdfSha256 MEASURED from the edition's
      actual web PDF file (never taken from arguments or the KIT);
      abstract read from the edition dir's ABSTRACT.txt (single line, the
      reader-native-language summary written for this edition — ABORT if
      missing, empty, multi-line or containing an ASCII double quote);
      the edition's <slug>.text.md (repo AGENTS.md rule 4, exported from the
      source manuscript) must exist and be non-empty — ABORT if missing —
      and is measured (bytes + SHA-256) for the index `text` field;
      the abstract heading word comes from tables.json per native language
  (c) node lint.mjs --write
  (d) commit metadata + <slug>.text.md; push that sha (retry loop — tunnel cuts are normal)
  (e) copy the web PDF as <slug>.pdf; lint --write again (index drifts);
      node lint.mjs --require-pdf must be green
  (f) commit PDF + index.json; push with retries
  (g) verify git ls-remote origin main == local HEAD; print edition count

Modes:
  (default)    full insert with commits + pushes
  --dry-run    steps (a)+(b) checks only: aborts on existing slug, verifies
               the web PDF exists and the sibling md is present; writes nothing
  --render-only  render the .md into a scratch repo copy and lint it there
               (with the PDF, --require-pdf) — no real repo writes, no pushes
  --bundle     one target's whole native set as ONE commit (user order
               2026-11-03: a bundle = one commit; never one commit per
               edition, never one commit for the whole week). Renders every
               remaining native first (fail-fast, nothing written), then
               writes all md + .text.md + PDFs, one lint --write, one
               --require-pdf gate, ONE commit, one verified push. Editions
               already in the repo are skipped; --vol/--exercises/
               --seed-excerpt are required only when the target has no
               in-week sibling yet (same seed rule as single mode).
               --native/--edition-dir must NOT be given; edition dirs are
               resolved from --files-root (default: goal files/).

Usage:
  insert.py --week 2026-W43 --target ko --native pt \
            [--edition-dir ../production/2026-w43/2026-w43-ko-pt] [--repo ~/workspace/weekly-git]
  insert.py --week 2026-W46 --target de --bundle \
            --vol 3 --exercises 150 --seed-excerpt "..." [--repo ~/workspace/weekly-git]
Exit 0 on success, non-zero on any failed step. System python3 is fine
(only stdlib is used); git + node must be on PATH.

Edition sources live in the repo under production/<week>/<slug>/
(e.g. production/2026-w43/2026-w43-ko-pt/); --files-root defaults to
<repo>/production and --edition-dir defaults to the slug dir under it.
"""
import argparse, copy, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tables as T

REPO = os.path.expanduser("~/workspace/weekly-git")


def run(cmd, cwd=None, check=True):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and p.returncode != 0:
        raise SystemExit(f"STEP FAILED: {' '.join(cmd)}\n{p.stdout[-1500:]}\n{p.stderr[-1500:]}")
    return p


def sha256_bytes(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return os.path.getsize(path), h.hexdigest()


def find_web_pdf(edition_dir):
    # Web PDF = filename containing "web" OR Chinese "网页版" (FR core ships
    # 法语周报VOL3-网页版.pdf; 2026-10-27 fix after its seed insert aborted on []).
    # Exactly-1 check still aborts if both namings are present.
    cands = [os.path.join(edition_dir, f) for f in os.listdir(edition_dir)
             if f.lower().endswith(".pdf") and ("web" in f.lower() or "网页版" in f)]
    if len(cands) != 1:
        raise SystemExit(f"ABORT: expected exactly 1 *web*.pdf in {edition_dir}, found {cands}")
    return cands[0]


def parse_frontmatter(md_path):
    raw = open(md_path, encoding="utf-8").read()
    fm = {}
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z][A-Za-z0-9]*):\s*\"?([^\"\n]*)\"?\s*$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm, raw


def sibling_md(repo, week_lower, target):
    """The target's xEN edition md in the same week (frontmatter donor)."""
    cand = os.path.join(repo, "issues", week_lower, f"{week_lower}-{target}-en",
                        f"{week_lower}-{target}-en.md")
    if os.path.exists(cand):
        return cand
    # core-as-native case: target x zh-cn siblings carry the same donor fields
    for nat in T.ORDER:
        c = os.path.join(repo, "issues", week_lower, f"{week_lower}-{target}-{nat}",
                         f"{week_lower}-{target}-{nat}.md")
        if os.path.exists(c):
            return c
    return None


def render_md(args, repo):
    week_lower = args.week.lower()
    week_upper = f"{week_lower[:4].upper()}-W{week_lower[-2:]}" if "-w" in week_lower else args.week
    slug = T.slug(args.week, args.target, args.native)
    sib = sibling_md(repo, week_lower, args.target)
    if sib:
        fm, _ = parse_frontmatter(sib)
    else:
        # First edition of this target in this week: no in-week donor exists.
        # Seed mode (added 2026-10-26 for W45): week fields are computed from
        # --week (ISO week), publishedAt = weekStart, and the caller must
        # supply --vol, --exercises and --seed-excerpt (the excerpt is shared
        # across the target's natives, exactly as a sibling's excerpt would be).
        if args.vol is None or args.exercises is None or not getattr(args, "seed_excerpt", None):
            raise SystemExit(f"ABORT: no sibling md for target {args.target} in {repo}/issues/{week_lower} — first-in-week insert requires --vol, --exercises and --seed-excerpt")
        import datetime as _dt
        m = re.match(r"^(\d{4})-W(\d{1,2})$", args.week, re.I)
        if not m:
            raise SystemExit(f"ABORT: --week must look like 2026-W45, got {args.week}")
        ws = _dt.date.fromisocalendar(int(m.group(1)), int(m.group(2)), 1)
        we = ws + _dt.timedelta(days=6)
        fm = {"vol": str(args.vol), "exercises": str(args.exercises),
              "excerpt": args.seed_excerpt, "publishedAt": ws.isoformat(),
              "week": f"{int(m.group(1))}-W{int(m.group(2)):02d}",
              "weekStart": ws.isoformat(), "weekEnd": we.isoformat()}
        sib = "(seed)"
    web_pdf = find_web_pdf(args.edition_dir)
    nbytes, sha = sha256_bytes(web_pdf)
    text_path = os.path.join(args.edition_dir, f"{slug}.text.md")
    if not os.path.exists(text_path) or os.path.getsize(text_path) == 0:
        raise SystemExit(f"ABORT: no non-empty {slug}.text.md in edition dir {args.edition_dir} "
                         "(repo AGENTS.md rule 4: export the edition text from the source manuscript, never extracted from the PDF)")
    tnbytes, tsha = sha256_bytes(text_path)
    tl, nl = T.lang(args.target), T.lang(args.native)
    vol = args.vol if args.vol is not None else int(fm["vol"])
    exercises = args.exercises if args.exercises is not None else int(fm["exercises"])
    ctx = {"MASTHEAD": tl["masthead"], "VOL": vol,
           "TARGET_NAME": tl["name_en"], "NATIVE_NAME": nl["name_en"]}
    title = T.load()["frontmatter"]["title_template"].format(**ctx)
    excerpt = fm["excerpt"]
    abs_path = os.path.join(args.edition_dir, "ABSTRACT.txt")
    if not os.path.exists(abs_path):
        raise SystemExit(f"ABORT: no ABSTRACT.txt in edition dir {args.edition_dir} "
                         "(the edition's reader-language abstract is a required deliverable)")
    abstract = open(abs_path, encoding="utf-8").read().strip()
    if not abstract or "\n" in abstract or '"' in abstract:
        raise SystemExit("ABORT: ABSTRACT.txt must be a single non-empty line "
                         "without ASCII double quotes")
    body = T.load()["frontmatter"]["body_template"].format(
        TITLE=title, EXCERPT=excerpt, TARGET_NAME=tl["name_en"],
        NATIVE_NAME=nl["name_en"], EXERCISES=exercises,
        ABSTRACT=abstract, ABSTRACT_HEADING=nl["abstract_heading"])
    md = f"""---
title: "{title}"
excerpt: "{excerpt}"
abstract: "{abstract}"
publishedAt: "{fm['publishedAt']}"
week: "{fm['week']}"
weekStart: "{fm['weekStart']}"
weekEnd: "{fm['weekEnd']}"
vol: {vol}
masthead: "{tl['masthead']}"
target: {args.target}
targetName: "{tl['name_en']}"
targetLabel: "{tl['label']}"
native: {args.native}
nativeName: "{nl['name_en']}"
nativeLabel: "{nl['label']}"
exercises: {exercises}
pages: 8
pdf: {slug}.pdf
pdfBytes: {nbytes}
pdfSha256: {sha}
discordThread: "{tl['discord_thread']}"
draft: false
---

{body}
"""
    return slug, md, web_pdf, {"bytes": nbytes, "sha256": sha, "sibling": sib,
                            "text_path": text_path, "text_bytes": tnbytes, "text_sha256": tsha}


def push_with_verify(repo, sha, tries=8):
    for i in range(1, tries + 1):
        p = run(["git", "push", "origin", f"{sha}:main"], cwd=repo, check=False)
        remote = run(["git", "ls-remote", "origin", "main"], cwd=repo).stdout.split()[0]
        if remote == sha:
            print(f"  push verified on attempt {i}: origin main == {sha[:8]}")
            return
        print(f"  push attempt {i} not verified (remote {remote[:8]}), retrying…")
        time.sleep(min(5 * i, 20))
    raise SystemExit(f"STEP FAILED: push of {sha} never landed after {tries} attempts")


def edition_count(repo):
    out = run(["node", "lint.mjs", "--require-pdf"], cwd=repo, check=False)
    m = re.search(r"OK:(\d+)", out.stdout)
    return int(m.group(1)) if m else None


def bundle_natives(target):
    """All legal natives for one target bundle (same-language + the two
    cross-script Chinese pairings excluded, per T.slug)."""
    out = []
    for nat in T.ORDER:
        if nat == target or {target, nat} == {"zh-cn", "zh-tw"}:
            continue
        out.append(nat)
    return out


def resolve_bundle_dir(files_root, week_lower, target, native, slug):
    """Edition dir for one pairing inside a week bundle. New production
    layout first (production/<week>/<slug>/); fall back to the legacy
    weekly-report-* names, and to the target's core dir ONLY when the
    core dir holds this slug's .text.md (verified W46: en-zh-cn lives
    in weekly-report-w46-en-core, zh-tw-en in weekly-report-w46-zhtw-core;
    a core dir without the slug's text file is not a fallback)."""
    new = os.path.join(files_root, week_lower, slug)
    if os.path.isdir(new):
        return new
    week_suffix = week_lower.split("-", 1)[1]  # 2026-w46 -> w46
    std = os.path.join(files_root, f"weekly-report-{week_suffix}-{target}-{native}")
    if os.path.isdir(std):
        return std
    for core in (os.path.join(files_root, week_lower, f"core-{target}"),
                 os.path.join(files_root, f"weekly-report-{week_suffix}-{target}-core"),
                 os.path.join(files_root, f"weekly-report-{week_suffix}-{target.replace('-', '')}-core")):
        p = core
        if os.path.isdir(p) and os.path.exists(os.path.join(p, f"{slug}.text.md")):
            return p
    raise SystemExit(f"ABORT: no edition dir for {target}x{native} under {files_root} "
                     f"(tried {new}, {std} and the {target} core dir — no {slug}.text.md there)")


def main_bundle(args, repo, week_lower):
    target = args.target
    files_root = os.path.abspath(args.files_root)
    # clean tree: a bundle commit must contain exactly the bundle
    dirty = run(["git", "status", "--porcelain"], cwd=repo).stdout.strip()
    if dirty:
        raise SystemExit(f"ABORT: repo working tree not clean:\n{dirty}")
    todo = []
    for nat in bundle_natives(target):
        slug = T.slug(args.week, target, nat)
        dest_dir = os.path.join(repo, "issues", week_lower, slug)
        if os.path.exists(dest_dir):
            print(f"  skip {slug}: already in repo")
            continue
        todo.append(nat)
    if not todo:
        print(f"bundle {target}: all {len(bundle_natives(target))} editions already in repo — nothing to do")
        return 0
    print(f"(a) bundle {target}: {len(todo)} edition(s) to insert ({', '.join(todo)})")
    # (b) render ALL first: any missing ABSTRACT/.text.md/PDF aborts before
    # anything is written
    rendered = []
    for nat in todo:
        slug = T.slug(args.week, target, nat)
        sub = copy.copy(args)
        sub.native = nat
        sub.edition_dir = resolve_bundle_dir(files_root, week_lower, target, nat, slug)
        slug, md, web_pdf, pins = render_md(sub, repo)
        rendered.append((slug, nat, md, web_pdf, pins, sub.edition_dir))
        print(f"(b) {slug}: rendered from sibling {os.path.basename(pins['sibling'])}; "
              f"web PDF {pins['bytes']} B sha256 {pins['sha256'][:16]}…")
    if args.dry_run:
        print("dry-run: all renders passed, nothing written")
        return 0
    # (c) write everything, one lint --write. On any failure before the
    # commit, remove exactly what this run wrote so the repo is left as
    # it was (the driver falls back to per-edition inserts on a clean tree).
    written_dirs = []
    try:
        for slug, nat, md, web_pdf, pins, _ in rendered:
            d = os.path.join(repo, "issues", week_lower, slug)
            os.makedirs(d)
            written_dirs.append(d)
            open(os.path.join(d, f"{slug}.md"), "w", encoding="utf-8").write(md)
            shutil.copy(pins["text_path"], os.path.join(d, f"{slug}.text.md"))
            shutil.copy(web_pdf, os.path.join(d, f"{slug}.pdf"))
        run(["node", "lint.mjs", "--write"], cwd=repo)
        print("(c) all bundle files written; lint --write OK")
        out = run(["node", "lint.mjs", "--require-pdf"], cwd=repo, check=False)
        if out.returncode != 0:
            raise SystemExit(f"STEP FAILED: lint --require-pdf not green after bundle write\n{out.stdout}\n{out.stderr}")
        print(f"(d) lint --require-pdf green: {out.stdout.strip()}")
    except BaseException:
        for d in written_dirs:
            shutil.rmtree(d, ignore_errors=True)
        run(["git", "checkout", "--", "index.json"], cwd=repo, check=False)
        raise
    # (e) ONE commit for the whole bundle
    add_paths = ["index.json"]
    for slug, _, _, _, _, _ in rendered:
        add_paths.append(f"issues/{week_lower}/{slug}/{slug}.md")
        add_paths.append(f"issues/{week_lower}/{slug}/{slug}.text.md")
        add_paths.append(f"issues/{week_lower}/{slug}/{slug}.pdf")
    run(["git", "add"] + add_paths, cwd=repo)
    run(["git", "commit", "-m",
         f"Add {args.week.lower()}-{target} bundle ({target.upper()} text · {len(rendered)} natives)"], cwd=repo)
    sha = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
    print(f"(e) bundle commit {sha[:8]} ({len(rendered)} editions)")
    push_with_verify(repo, sha, tries=12)
    remote = run(["git", "ls-remote", "origin", "main"], cwd=repo).stdout.split()[0]
    local = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
    assert remote == local, (remote, local)
    print(f"(f) verified: ls-remote origin main == local HEAD ({local[:8]}); editions in repo: {edition_count(repo)}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--week", required=True, help="e.g. 2026-W43")
    ap.add_argument("--target", required=True)
    ap.add_argument("--native", help="single-edition mode only; omit with --bundle")
    ap.add_argument("--edition-dir", help="single-edition mode only; omit with --bundle")
    ap.add_argument("--bundle", action="store_true", help="one target's whole native set as ONE commit")
    ap.add_argument("--files-root", default=os.path.join(REPO, "production"),
                    help="bundle mode: dir holding the production/<week>/<slug> edition dirs "
                         "(single-edition --edition-dir defaults to the slug dir under it)")
    ap.add_argument("--repo", default=os.path.expanduser("~/workspace/weekly-git"))
    ap.add_argument("--vol", type=int)
    ap.add_argument("--exercises", type=int)
    ap.add_argument("--seed-excerpt", help="required only for a target's first edition in a week (no in-week sibling): the excerpt shared across that target's natives")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--render-only", action="store_true", help="render + lint in a scratch repo copy")
    ap.add_argument("--scratch", help="scratch dir for --render-only (default: tools/scratch/insert-render)")
    args = ap.parse_args(argv)
    repo = os.path.abspath(args.repo)
    week_lower = args.week.lower()
    if args.bundle:
        if args.native or args.edition_dir:
            raise SystemExit("ABORT: --bundle takes no --native/--edition-dir (edition dirs resolve from --files-root)")
        if args.render_only:
            raise SystemExit("ABORT: --render-only is single-edition only; use --bundle --dry-run to validate a bundle")
        return main_bundle(args, repo, week_lower)
    if not args.native:
        raise SystemExit("ABORT: single-edition mode requires --native")
    slug = T.slug(args.week, args.target, args.native)
    if not args.edition_dir:
        # Default: the slug dir under --files-root (production/<week>/<slug>/).
        args.edition_dir = os.path.join(os.path.abspath(args.files_root), week_lower, slug)
    args.edition_dir = os.path.abspath(args.edition_dir)
    dest_dir = os.path.join(repo, "issues", week_lower, slug)

    # (a) abort if the slug already exists
    if os.path.exists(dest_dir):
        raise SystemExit(f"ABORT (step a): slug {slug} already exists in the repo — nothing written")
    print(f"(a) slug {slug} not in repo — OK")

    slug2, md, web_pdf, pins = render_md(args, repo)
    assert slug2 == slug
    print(f"(b) rendered md from sibling {os.path.basename(pins['sibling'])}; "
          f"web PDF measured: {pins['bytes']} B sha256 {pins['sha256'][:16]}…; "
          f".text.md measured: {pins['text_bytes']} B sha256 {pins['text_sha256'][:16]}…")
    if args.dry_run:
        print("dry-run: checks passed, nothing written")
        return 0

    if args.render_only:
        scratch = args.scratch or os.path.join(REPO, "tools", "scratch", "insert-render")
        if os.path.exists(scratch):
            shutil.rmtree(scratch)
        shutil.copytree(repo, scratch, ignore=shutil.ignore_patterns(".git"))
        d = os.path.join(scratch, "issues", week_lower, slug)
        os.makedirs(d)
        open(os.path.join(d, f"{slug}.md"), "w", encoding="utf-8").write(md)
        shutil.copy(web_pdf, os.path.join(d, f"{slug}.pdf"))
        shutil.copy(pins["text_path"], os.path.join(d, f"{slug}.text.md"))
        run(["node", "lint.mjs", "--write"], cwd=scratch)
        run(["node", "lint.mjs"], cwd=scratch)  # structural + index consistency
        # targeted pin check for the rendered edition itself
        nbytes, sha = sha256_bytes(os.path.join(d, f"{slug}.pdf"))
        fm, _ = parse_frontmatter(os.path.join(d, f"{slug}.md"))
        assert int(fm["pdfBytes"]) == nbytes and fm["pdfSha256"] == sha, "rendered pins do not match the copied PDF"
        idx = json.load(open(os.path.join(scratch, "index.json"), encoding="utf-8"))
        ent = [e for e in idx["editions"] if e["slug"] == slug]
        assert len(ent) == 1 and ent[0]["text"] is not None, "index has no text entry for the rendered edition"
        assert ent[0]["text"]["bytes"] == pins["text_bytes"] and ent[0]["text"]["sha256"] == pins["text_sha256"], "index text pins do not match the copied .text.md"
        out = run(["node", "lint.mjs", "--require-pdf"], cwd=scratch, check=False)
        print(f"render-only: scratch repo at {scratch}")
        print(f"  lint --write + lint: green; rendered edition's pins verified "
              f"({nbytes} B, sha256 {sha[:16]}…)")
        if out.returncode == 0:
            print(f"  lint --require-pdf: green ({out.stdout.strip()})")
        else:
            others = [ln for ln in (out.stdout + out.stderr).splitlines()
                      if slug not in ln and ("不在仓内" in ln or "不符" in ln)]
            mine = [ln for ln in (out.stdout + out.stderr).splitlines() if slug in ln]
            if mine:
                raise SystemExit(f"STEP FAILED: --require-pdf flags the rendered edition:\n" + "\n".join(mine))
            print(f"  lint --require-pdf: fails ONLY on pre-existing repo state "
                  f"({len(others)} line(s) about other slugs, e.g. {others[0].strip() if others else '?'}) "
                  f"— the rendered edition itself is clean")
        print(f"  rendered md: {os.path.join(d, slug + '.md')}")
        return 0

    # full insert
    os.makedirs(dest_dir)
    md_path = os.path.join(dest_dir, f"{slug}.md")
    open(md_path, "w", encoding="utf-8").write(md)
    shutil.copy(pins["text_path"], os.path.join(dest_dir, f"{slug}.text.md"))
    run(["node", "lint.mjs", "--write"], cwd=repo)
    print("(c) lint --write OK")
    run(["git", "add", f"issues/{week_lower}/{slug}/{slug}.md", f"issues/{week_lower}/{slug}/{slug}.text.md", "index.json"], cwd=repo)
    run(["git", "commit", "-m",
         f"Add {slug} metadata ({args.target.upper()} text · {args.native.upper()} explanations)"], cwd=repo)
    sha = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
    print(f"(d) metadata commit {sha[:8]}")
    push_with_verify(repo, sha)
    shutil.copy(web_pdf, os.path.join(dest_dir, f"{slug}.pdf"))
    run(["node", "lint.mjs", "--write"], cwd=repo)
    out = run(["node", "lint.mjs", "--require-pdf"], cwd=repo, check=False)
    if out.returncode != 0:
        raise SystemExit(f"STEP FAILED (e): lint --require-pdf not green\n{out.stdout}\n{out.stderr}")
    print(f"(e) PDF copied; lint --require-pdf green: {out.stdout.strip()}")
    run(["git", "add", f"issues/{week_lower}/{slug}/{slug}.pdf", "index.json"], cwd=repo)
    run(["git", "commit", "-m", f"Add {slug} web PDF"], cwd=repo)
    sha = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
    print(f"(f) PDF commit {sha[:8]}")
    push_with_verify(repo, sha)
    remote = run(["git", "ls-remote", "origin", "main"], cwd=repo).stdout.split()[0]
    local = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
    assert remote == local, (remote, local)
    print(f"(g) verified: ls-remote origin main == local HEAD ({local[:8]}); editions in repo: {edition_count(repo)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
