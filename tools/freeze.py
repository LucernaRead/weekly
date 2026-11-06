#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""freeze.py — baseline reproduction proof + frozen-core text diff.

Subcommands:
  baseline --build <core build dir> --core-svg <dir> --out <scratchdir>
      Copy the build dir into <out>/build-copy, repoint every output path
      that aimed at the real files/ tree (legacy goal layout) or the real
      production/ tree (repo layout) into <out>/svg, run the copy
      (run.py if present, else import content12/34/56/7/8 in order), and
      sha256-compare the produced SVGs against the shipped core SVGs.
      Guards: aborts if any copied content file still references the real
      core svg dir; hashes the real core SVGs before AND after and aborts
      if they changed. Expect 8/8.

  diff --core-svg <dir> --edition-svg <dir> [--json out.json]
      Per-page text-multiset diff (every added/removed string listed with
      counts) + CJK accounting per page: edition CJK multiset vs core CJK
      multiset. For zh/ja editions the added-CJK list must be empty — any
      added CJK character means new target-language text appeared, which
      a fan-out must never do.

Exit: baseline 0 iff 8/8 identical; diff 0 normally, 1 with --strict-cjk
when CJK was added. Run with tools/venv/bin/python.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
CJK_RE = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
CONTENT_ORDER = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def dir_hashes(d):
    return {fn: sha256(os.path.join(d, fn))
            for fn in sorted(os.listdir(d)) if fn.endswith(".svg")}


def load_texts(path):
    import html
    s = open(path, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in TEXT_RE.findall(s)]


def page_num(fn):
    m = re.match(r"p(\d+)", fn)
    return int(m.group(1)) if m else 99


# ---------------- baseline ----------------------------------------------
def cmd_baseline(args):
    build = os.path.abspath(args.build)
    core_svg = os.path.abspath(args.core_svg)
    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)
    before = dir_hashes(core_svg)
    if len(before) != 8:
        print(f"ABORT: core svg dir has {len(before)} SVGs, expected 8", file=sys.stderr)
        return 2
    copy_dir = os.path.join(out, "build-copy")
    if os.path.exists(copy_dir):
        shutil.rmtree(copy_dir)
    shutil.copytree(build, copy_dir, ignore=shutil.ignore_patterns("__pycache__"))
    svg_out = os.path.join(out, "svg")
    os.makedirs(svg_out, exist_ok=True)

    # Repoint outputs: rewrite any quoted path string that points into the
    # real files/ tree (legacy goal layout) or the real production/ tree
    # (repo layout, production/<week>/<slug>/) to the scratch tree, so
    # the copy can only write under --out.
    pat = re.compile(r"([\"'])(?:~|/home/hatch)?/?workspace/(?:goals/"
                     r"lucernaread-social-media-operations/files|weekly-git/production)/[^\"']*\1")
    touched = []
    for root, _, files in os.walk(copy_dir):
        for fn in files:
            if not fn.endswith(".py"):
                continue
            p = os.path.join(root, fn)
            s = open(p, encoding="utf-8").read()
            def repl(m):
                q = m.group(1)
                inner = m.group(0)[1:-1]
                dest = svg_out if inner.rstrip("/").endswith("/svg") else out
                return f"{q}{dest}{q}"
            s2 = pat.sub(repl, s)
            if s2 != s:
                open(p, "w", encoding="utf-8").write(s2)
                touched.append(os.path.relpath(p, copy_dir))
    # Guard: no copied file may still point at the real core svg dir.
    real_core = os.path.dirname(core_svg)  # the edition dir (files/ or production/)
    for root, _, files in os.walk(copy_dir):
        for fn in files:
            if fn.endswith(".py"):
                s = open(os.path.join(root, fn), encoding="utf-8").read()
                if real_core in s and ("files/weekly-report" in s or "weekly-git/production" in s):
                    print(f"ABORT: {fn} still references the real edition dir {real_core}; "
                          "refusing to run (it could write into files/ or production/)", file=sys.stderr)
                    return 2
    runner = os.path.join(copy_dir, "run.py")
    if os.path.exists(runner):
        cmd = [sys.executable, "run.py"]
    else:
        cmd = [sys.executable, "-c",
               "import content12, content34, content56, content7, content8"]
    proc = subprocess.run(cmd, cwd=copy_dir, capture_output=True, text=True)
    if proc.returncode != 0:
        print("BUILD FAILED:\n" + proc.stdout[-3000:] + proc.stderr[-3000:], file=sys.stderr)
        return 1
    after = dir_hashes(core_svg)
    if after != before:
        print("ABORT: THE REAL CORE SVGs CHANGED during the run — investigate before trusting anything",
              file=sys.stderr)
        return 2
    produced = {}
    for root, _, files in os.walk(out):
        for fn in files:
            if fn.endswith(".svg") and "build-copy" not in root:
                produced[fn] = sha256(os.path.join(root, fn))
    rows, ok = [], 0
    for fn in sorted(before):
        match = produced.get(fn) == before[fn]
        ok += match
        rows.append({"file": fn, "match": match,
                     "core_sha256": before[fn][:16], "produced_sha256": (produced.get(fn) or "")[:16]})
    print(f"baseline: {ok}/8 SVGs byte-identical (repointed files: {', '.join(touched) or 'none'})")
    for r in rows:
        print(f"  {'OK ' if r['match'] else 'DIFF'} {r['file']} core {r['core_sha256']} produced {r['produced_sha256']}")
    print(f"core integrity: shipped core SVGs unchanged by the run ({len(after)} files re-hashed)")
    if args.json_out:
        json.dump({"ok": ok, "rows": rows}, open(args.json_out, "w"), indent=1)
    return 0 if ok == 8 else 1


# ---------------- diff ----------------------------------------------------
def cmd_diff(args):
    def pages(d):
        out = {}
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".svg"):
                out.setdefault(page_num(fn), Counter()).update(load_texts(os.path.join(d, fn)))
        return out
    core, ed = pages(args.core_svg), pages(args.edition_svg)
    report = {"core_svg": args.core_svg, "edition_svg": args.edition_svg, "pages": {}}
    total_added_cjk = Counter()
    for pg in sorted(set(core) | set(ed)):
        c, e = core.get(pg, Counter()), ed.get(pg, Counter())
        added, removed = e - c, c - e
        cjk_c = Counter(ch for s, n in c.items() for ch in s if CJK_RE.match(ch) for _ in range(n))
        cjk_e = Counter(ch for s, n in e.items() for ch in s if CJK_RE.match(ch) for _ in range(n))
        added_cjk = cjk_e - cjk_c
        total_added_cjk.update(added_cjk)
        report["pages"][pg] = {
            "added_strings": [{"text": s, "count": n} for s, n in sorted(added.items())],
            "removed_strings": [{"text": s, "count": n} for s, n in sorted(removed.items())],
            "cjk_core_total": sum(cjk_c.values()), "cjk_edition_total": sum(cjk_e.values()),
            "cjk_added": dict(added_cjk),
        }
        print(f"p{pg}: +{sum(added.values())} strings / -{sum(removed.values())} strings; "
              f"CJK core {sum(cjk_c.values())} -> edition {sum(cjk_e.values())}; "
              f"added CJK chars: {sum(added_cjk.values())} {dict(list(added_cjk.items())[:10]) if added_cjk else ''}")
    report["cjk_added_total"] = dict(total_added_cjk)
    print(f"TOTAL added CJK characters: {sum(total_added_cjk.values())}")
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    if args.strict_cjk and total_added_cjk:
        print("STRICT-CJK FAIL: edition adds CJK characters the core does not have", file=sys.stderr)
        return 1
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("baseline")
    p.add_argument("--build", required=True); p.add_argument("--core-svg", required=True)
    p.add_argument("--out", required=True); p.add_argument("--json", dest="json_out")
    p = sub.add_parser("diff")
    p.add_argument("--core-svg", required=True); p.add_argument("--edition-svg", required=True)
    p.add_argument("--json", dest="json_out"); p.add_argument("--strict-cjk", action="store_true")
    args = ap.parse_args(argv)
    return cmd_baseline(args) if args.cmd == "baseline" else cmd_diff(args)


if __name__ == "__main__":
    sys.exit(main())
