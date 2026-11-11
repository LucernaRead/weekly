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
      Fallback (2026-11-10): builds whose OUT is __file__-relative write
      into the copy's own svg/ dir; files the run rewrote there (by mtime)
      are collected too, so a stale copy can never fake a match.

  diff --core-svg <dir> --edition-svg <dir> [--json out.json]
      Per-page text-multiset diff (every added/removed string listed with
      counts) + CJK accounting per page: edition CJK multiset vs core CJK
      multiset. For zh/ja editions the added-CJK list must be empty — any
      added CJK character means new target-language text appeared, which
      a fan-out must never do.
      + Latin accounting (2026-11-11): per-page added Latin strings and
      the unexpected subset (added Latin strings that are not a bare
      furniture language name, see FURNITURE_LANG_NAMES). --strict-latin
      fails when any unexpected Latin string was added. It is a
      same-slug before/after gate ONLY: a core-vs-edition diff always
      adds Latin wholesale (translation; measured 330 added / 211 removed
      core-de -> de-en), so --strict-latin must never be used there.

Exit: baseline 0 iff 8/8 identical; diff 0 normally, 1 with --strict-cjk
when CJK was added. Run with tools/venv/bin/python.

Runtime guard (2026-11-11): the stack is per family, not one global
mandate — build == freeze == core within a family. The canonical stack
is tools/venv (Pillow 13.0.0, pinned in tools/requirements.txt), and
main() asserts Pillow major version 13 for every path — EXCEPT the ko
family (core-ko and the 2026-w47-ko-* editions under production/),
which was built on system python3 (Pillow 10.2.0 / FreeType 2.13.2):
the venv measures the same Korean strings ~1.1% wider (~+1.11px per
Korean-space boundary), moving every line break, so a venv freeze of a
ko edition is 0/8 by construction — a recorded control, not a gate
failure (core-ko WEEKLY-KIT.md fix #15, Round 10). For ko paths main()
therefore asserts Pillow major version 10. pt-ko was realigned to the
venv core; ko stays on the system stack. The guard prints executable /
Pillow / FreeType versions in every run, so a wrong interpreter fails
loudly instead of silently producing numbers.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, time
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# ---------------- runtime guard (2026-11-11), per family ----------------
# Stack consistency is per family (build == freeze == core), not a single
# global venv mandate. The canonical stack is tools/venv (SOP; Pillow
# pinned 13.0.0 in tools/requirements.txt) — EXCEPT the ko family, whose
# shipped SVGs were built on system python3 (Pillow 10.2.0 /
# FreeType 2.13.2): the venv stack measures Korean ~1.1% wider
# (~+1.11px per space boundary; 40px: 991.3 vs 1002.2) and re-wraps
# every line, so a venv freeze of a ko edition is 0/8 by construction
# (core-ko WEEKLY-KIT.md fix #15, Round 10) — a recorded control, not
# a gate failure. The W47 pt-ko 0/8 freeze was the same mismatch in the
# other direction (freeze ran venv against system-built SVGs); pt-ko
# was realigned to the venv core, while ko stays on the system stack.
# A wrong interpreter must therefore fail loudly, against the family's
# own required major: ko family paths REQUIRE Pillow 10, all other
# paths REQUIRE Pillow 13.
REQUIRED_PILLOW_MAJOR = 13
KO_REQUIRED_PILLOW_MAJOR = 10


def runtime_env():
    """(executable, Pillow version, FreeType version) of this process."""
    try:
        import PIL
        from PIL import features
        pillow = PIL.__version__
        try:
            freetype = features.version("freetype2")
        except Exception:
            freetype = "unknown"
    except ImportError:
        pillow, freetype = "MISSING", "unknown"
    return sys.executable, pillow, freetype


def runtime_env_dict():
    exe, pillow, freetype = runtime_env()
    return {"executable": exe, "pillow": pillow, "freetype": freetype}


def is_ko_family_path(path):
    """True if path is inside the ko family: the core-ko build dir or a
    <week>-ko-* edition dir under production/ (any path component
    == 'core-ko' or matching '<week>-ko-')."""
    if not path:
        return False
    parts = os.path.abspath(path).split(os.sep)
    return any(p == "core-ko" or re.match(r"^\d{4}-w\d+-ko-", p) for p in parts)


def required_pillow_major(args):
    """Pillow major this run must see, from the paths it touches:
    10 for the ko family, 13 everywhere else."""
    paths = ([args.build, args.core_svg] if args.cmd == "baseline"
             else [args.core_svg, args.edition_svg])
    return (KO_REQUIRED_PILLOW_MAJOR
            if any(is_ko_family_path(p) for p in paths)
            else REQUIRED_PILLOW_MAJOR)


def check_runtime_env(required_major=REQUIRED_PILLOW_MAJOR):
    """Print the runtime line; abort (exit 2) unless the Pillow major
    matches the family's required stack (10 = ko family, 13 = default).
    A ko abort cites core-ko WEEKLY-KIT.md fix #15."""
    exe, pillow, freetype = runtime_env()
    print(f"runtime: {exe} | Pillow {pillow} | FreeType {freetype}")
    major = pillow.split(".")[0] if pillow not in ("MISSING", "unknown") else None
    if major != str(required_major):
        if required_major == KO_REQUIRED_PILLOW_MAJOR:
            print(f"ABORT: ko family builds on system python3 (Pillow 10.x) — "
                  f"core-ko WEEKLY-KIT.md fix #15: the venv (Pillow 13) measures "
                  f"Korean ~1.1% wider and re-wraps every line, so a venv freeze "
                  f"of a ko edition is 0/8 by construction. Got Pillow {pillow} "
                  f"at {exe}; re-run with /usr/bin/python3.", file=sys.stderr)
        else:
            print(f"ABORT: canonical stack is tools/venv Pillow {required_major}.x "
                  f"(got Pillow {pillow} at {exe}); re-run with tools/venv/bin/python. "
                  f"A wrong interpreter silently re-measures text "
                  f"(W47 pt-ko freeze 0/8).", file=sys.stderr)
        return 2
    return 0

TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
CJK_RE = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
LATIN_RE = re.compile(r"[A-Za-z]")
# Furniture language names (2026-11-11): the only added Latin strings a
# same-slug before/after diff may legitimately contain — a deliberate
# correction of a bare language name in the furniture (masthead pairing
# band / kicker). Membership is the 12 language names in the spellings
# attested in W47 furniture; as whole <text> strings only 2 are attested
# in W47 ('РУССКИЙ' x11, the ru kicker; '中文' x1) — the rest are the
# same-class prospective forms, so a future bare-name kicker is exempt
# rather than tripping the gate. Composite band strings (e.g. 'TEXTO
# CHINO / EXPLICACIONES EN ESPAÑOL', ~200 distinct forms across the
# grid) are deliberately NOT whitelisted: a change there is a real
# change and must trip --strict-latin for human review. A core-vs-edition
# diff can never be whitelisted this way — the whole body is translated.
FURNITURE_LANG_NAMES = frozenset({
    "Deutsch", "DEUTSCH", "German", "GERMAN",
    "English", "ENGLISH",
    "Français", "FRANÇAIS", "French", "FRENCH",
    "Español", "ESPAÑOL", "Spanish", "SPANISH",
    "Italiano", "ITALIANO", "Italian", "ITALIAN",
    "Português", "PORTUGUÊS", "Portuguese", "PORTUGUESE",
    "Nederlands", "NEDERLANDS", "Dutch", "DUTCH",
    "Русский", "РУССКИЙ", "Russian", "RUSSIAN",
    "日本語", "Japanese", "JAPANESE",
    "한국어", "Korean", "KOREAN",
    "中文", "简体中文", "繁體中文", "Chinese", "CHINESE",
})
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
    # 2026-11-11: the alternation must also cover hidden_files/ under
    # both trees — all scratch work now lives there (goals-side
    # hidden_files/w47/scratch-*/ and the in-repo hidden_files/w47/
    # scratch dirs fixers actually build in). The old alternation
    # (files|production only) missed them, so a build whose OUT pointed
    # at a scratch dir wrote outside --out and baseline self-reported
    # 0/8 while the files were fine elsewhere (repro in
    # hidden_files/w47/scratch-tools-bugfix-B/freeze-repro-old.log).
    pat = re.compile(r"([\"'])(?:~|/home/hatch)?/?workspace/(?:goals/"
                     r"lucernaread-social-media-operations/(?:files|hidden_files)"
                     r"|weekly-git/(?:production|hidden_files))/[^\"']*\1")
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
                # The repointed --out destination legitimately contains
                # real_core as a substring when --out sits under the same
                # tree (e.g. both under hidden_files/); strip the --out
                # prefix first so only genuine leftovers can trip this.
                s_wo_out = s.replace(out, "")
                if real_core in s_wo_out and ("files/weekly-report" in s_wo_out
                                              or "weekly-git/production" in s_wo_out
                                              or "hidden_files" in s_wo_out):
                    print(f"ABORT: {fn} still references the real edition dir {real_core}; "
                          "refusing to run (it could write into files/ or production/)", file=sys.stderr)
                    return 2
    runner = os.path.join(copy_dir, "run.py")
    if os.path.exists(runner):
        cmd = [sys.executable, "run.py"]
    else:
        cmd = [sys.executable, "-c",
               "import content12, content34, content56, content7, content8"]
    run_start = time.time()
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
    # Fallback (2026-11-10): builds whose OUT is __file__-relative
    # (content*.py: OUT = <this dir>/svg) ignore the literal-path repoint
    # above and write into the copy's own svg/ dir. Collect those too —
    # but ONLY files the run actually rewrote (mtime >= run start),
    # so a stale copied SVG can never pass as a reproduction.
    # The repointed <out>/svg wins when a file exists in both places.
    copy_svg = os.path.join(copy_dir, "svg")
    if os.path.isdir(copy_svg):
        for fn in sorted(os.listdir(copy_svg)):
            if not fn.endswith(".svg") or fn in produced:
                continue
            p = os.path.join(copy_svg, fn)
            if os.path.getmtime(p) >= run_start - 1:
                produced[fn] = sha256(p)
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
        json.dump({"ok": ok, "rows": rows, "runtime": runtime_env_dict()},
                  open(args.json_out, "w"), indent=1)
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
    report = {"core_svg": args.core_svg, "edition_svg": args.edition_svg,
              "runtime": runtime_env_dict(), "pages": {}}
    total_added_cjk = Counter()
    total_added_latin = 0
    total_unexpected_latin = Counter()
    for pg in sorted(set(core) | set(ed)):
        c, e = core.get(pg, Counter()), ed.get(pg, Counter())
        added, removed = e - c, c - e
        cjk_c = Counter(ch for s, n in c.items() for ch in s if CJK_RE.match(ch) for _ in range(n))
        cjk_e = Counter(ch for s, n in e.items() for ch in s if CJK_RE.match(ch) for _ in range(n))
        added_cjk = cjk_e - cjk_c
        total_added_cjk.update(added_cjk)
        # Latin accounting (2026-11-11): mirror the CJK accounting, so a
        # pure-Latin change is visible to the gate, not just listed in
        # added_strings. "Unexpected" = added Latin string that is not a
        # bare furniture language name (see FURNITURE_LANG_NAMES).
        latin_added = {s: n for s, n in added.items() if LATIN_RE.search(s)}
        latin_unexpected = {s: n for s, n in latin_added.items()
                            if s.strip() not in FURNITURE_LANG_NAMES}
        total_added_latin += sum(latin_added.values())
        total_unexpected_latin.update(latin_unexpected)
        report["pages"][pg] = {
            "added_strings": [{"text": s, "count": n} for s, n in sorted(added.items())],
            "removed_strings": [{"text": s, "count": n} for s, n in sorted(removed.items())],
            "cjk_core_total": sum(cjk_c.values()), "cjk_edition_total": sum(cjk_e.values()),
            "cjk_added": dict(added_cjk),
            "latin_added": sum(latin_added.values()),
            "latin_added_unexpected": [{"text": s, "count": n} for s, n in sorted(latin_unexpected.items())],
        }
        print(f"p{pg}: +{sum(added.values())} strings / -{sum(removed.values())} strings; "
              f"CJK core {sum(cjk_c.values())} -> edition {sum(cjk_e.values())}; "
              f"added CJK chars: {sum(added_cjk.values())} {dict(list(added_cjk.items())[:10]) if added_cjk else ''}; "
              f"added Latin strings: {sum(latin_added.values())} "
              f"(unexpected {sum(latin_unexpected.values())})")
    report["cjk_added_total"] = dict(total_added_cjk)
    report["latin_added_total"] = total_added_latin
    report["latin_added_unexpected_total"] = dict(total_unexpected_latin)
    print(f"TOTAL added CJK characters: {sum(total_added_cjk.values())}")
    print(f"TOTAL added Latin strings: {total_added_latin} "
          f"(unexpected {sum(total_unexpected_latin.values())})")
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    if args.strict_cjk and total_added_cjk:
        print("STRICT-CJK FAIL: edition adds CJK characters the core does not have", file=sys.stderr)
        return 1
    if args.strict_latin and total_unexpected_latin:
        print("STRICT-LATIN FAIL: edition adds Latin strings the core does not have "
              f"(unexpected {sum(total_unexpected_latin.values())}; same-slug before/after gate only — "
              "never use --strict-latin on a core-vs-edition diff)", file=sys.stderr)
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
    p.add_argument("--strict-latin", action="store_true",
                   help="fail when an unexpected Latin string was added "
                        "(same-slug before/after diffs only; never on core-vs-edition)")
    args = ap.parse_args(argv)
    rc = check_runtime_env(required_pillow_major(args))
    if rc:
        return rc
    return cmd_baseline(args) if args.cmd == "baseline" else cmd_diff(args)


if __name__ == "__main__":
    sys.exit(main())
