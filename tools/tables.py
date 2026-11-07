#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tables.py — loader + CLI for the hard-coded Lucerna Weekly reference tables.

Every other tool in this directory imports from here; agents should too,
instead of copying language names, thread IDs or furniture strings by hand.

Usage:
    tables.py lang <code>                 language record (JSON)
    tables.py thread <target-code>       Discord thread id for a target language
    tables.py vol <week> [--allocate]     issue number of a week from production/volumes.json;
                                          --allocate appends max+1 for a new week later than all others
    tables.py furniture <native> --target <code> --week <week>
                                          rendered badge / footer / page line / gloss prefix
    tables.py slug <week> <target> <native>     e.g. 2026-W43 fr zh-cn -> 2026-w43-fr-zh-cn
    tables.py edition-dir <target> <native>     files/ directory name for a pairing
    tables.py frontmatter                 frontmatter conventions from lint.mjs
    tables.py check-repo [--repo PATH]    cross-check threads/names/mastheads vs repo frontmatter
All commands print JSON with --json, human-readable otherwise. Exit 1 on error.
Run with tools/venv/bin/python (any python3 works for this module).
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES_PATH = os.path.join(HERE, "tables.json")


def load():
    with open(TABLES_PATH, encoding="utf-8") as f:
        return json.load(f)


T = load()
LANGS = T["languages"]
ORDER = T["language_order"]


def lang(code):
    if code not in LANGS:
        raise KeyError(f"unknown language code {code!r} (known: {', '.join(ORDER)})")
    return LANGS[code]


VOLUMES_PATH = os.path.join(HERE, "..", "production", "volumes.json")


def _norm_week(week):
    m = re.match(r"^(\d{4})-w(\d{2})$", week, re.I)
    if not m:
        raise ValueError(f"week must look like 2026-W46, got {week!r}")
    return f"{m.group(1)}-W{m.group(2)}"


def vol(week, allocate=False):
    """Issue number of a week. The tracker production/volumes.json is the only source:
    one entry per published week, numbered 1, 2, 3 … in week order (all 12 targets share it).
    Never type a vol by hand; allocate the next one when a new week's production starts."""
    week = _norm_week(week)
    with open(VOLUMES_PATH, encoding="utf-8") as f:
        vols = json.load(f)
    if week in vols:
        return vols[week]
    if not allocate:
        raise KeyError(f"{week} has no issue number in production/volumes.json "
                       f"(run `tables.py vol {week} --allocate` when the week's production starts)")
    if vols and week < max(vols):
        raise ValueError(f"{week} is earlier than the latest tracked week {max(vols)}; numbers only grow")
    vols[week] = max(vols.values(), default=0) + 1
    with open(VOLUMES_PATH, "w", encoding="utf-8") as f:
        json.dump(vols, f, indent=2)
        f.write("\n")
    return vols[week]


def masthead(code):
    return lang(code)["masthead"]


def thread(target):
    return lang(target)["discord_thread"]


def slug(week, target, native):
    lang(target); lang(native)
    if target == native:
        raise ValueError("target == native is not a legal pairing")
    if {target, native} == {"zh-cn", "zh-tw"}:
        raise ValueError("zh-cn x zh-tw pairings do not exist")
    return f"{week.lower()}-{target}-{native}"


def edition_dir(target, native):
    """files/ directory name for a pairing (target == native -> the core dir)."""
    lang(target); lang(native)
    if target == native:
        return lang(target)["core_dir"]
    exc = T["edition_dir_rule"]["exceptions"].get(f"{target}-{native}")
    if exc:
        return exc
    return f"weekly-report-{target}-{native}"


def core_dir(target):
    return lang(target)["core_dir"]


def core_build_dir(target):
    return lang(target)["core_build_dir"]


def p8_file(target):
    return lang(target)["p8_file"]


def furniture(native, target, week):
    """Render the column furniture for (target text x native explanations) in a given week."""
    col = T["columns"].get(native)
    if col is None:
        raise KeyError(f"no established furniture column for native {native!r} "
                       f"(established: {', '.join(T['columns'])})")
    names = col["target_names"].get(target)
    if names is None:
        raise KeyError(f"no target-name row for {target!r} in the {native} column")
    number = vol(week)
    ctx = {"MASTHEAD": masthead(target), "VOL": number, "N": "{n}",
           "T_BADGE": names["T_BADGE"], "T_FADJ": names["T_FADJ"], "T_FNOUN": names["T_FNOUN"]}
    def render(tpl):
        return tpl.format(**ctx) if tpl else None
    return {
        "native": native, "target": target, "vol": number,
        "status": col["status"],
        "derived_target_row": bool(names.get("derived")),
        "badge": render(col["badge_template"]),
        "footer": render(col["footer_template"]),
        "page_line": render(col["page_line_template"]),
        "gloss_prefix": col["gloss_prefix"],
        "p8_separator": render(col["p8_separator_template"]),
        "variants": col.get("variants", []),
    }


def check_repo(repo):
    """Cross-check tables.json against every repo edition's frontmatter."""
    issues = os.path.join(repo, "issues")
    problems, checked = [], 0
    for week in sorted(os.listdir(issues)):
        wdir = os.path.join(issues, week)
        if not os.path.isdir(wdir):
            continue
        for s in sorted(os.listdir(wdir)):
            md = os.path.join(wdir, s, f"{s}.md")
            if not os.path.exists(md):
                continue
            raw = open(md, encoding="utf-8").read()
            fm = {}
            for line in raw.splitlines():
                m = re.match(r"^([A-Za-z][A-Za-z0-9]*):\s*\"?([^\"\n]*)\"?\s*$", line)
                if m:
                    fm[m.group(1)] = m.group(2).strip()
            checked += 1
            for role in ("target", "native"):
                code = fm.get(role)
                rec = LANGS.get(code)
                if rec is None:
                    problems.append(f"{s}: unknown {role} code {code}")
                    continue
                if fm.get(f"{role}Name") != rec["name_en"]:
                    problems.append(f"{s}: {role}Name {fm.get(f'{role}Name')} != table {rec['name_en']}")
                if fm.get(f"{role}Label") != rec["label"]:
                    problems.append(f"{s}: {role}Label {fm.get(f'{role}Label')} != table {rec['label']}")
            t = fm.get("target")
            if t in LANGS:
                if fm.get("discordThread") != LANGS[t]["discord_thread"]:
                    problems.append(f"{s}: discordThread {fm.get('discordThread')} != table {LANGS[t]['discord_thread']}")
                if fm.get("masthead") != LANGS[t]["masthead"]:
                    problems.append(f"{s}: masthead {fm.get('masthead')} != table {LANGS[t]['masthead']}")
    return {"repo": repo, "editions_checked": checked, "mismatches": problems}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", action="store_true", help="JSON output")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lang"); p.add_argument("code")
    p = sub.add_parser("thread"); p.add_argument("target")
    p = sub.add_parser("furniture"); p.add_argument("native")
    p.add_argument("--target", required=True); p.add_argument("--week", required=True)
    p = sub.add_parser("vol"); p.add_argument("week"); p.add_argument("--allocate", action="store_true")
    p = sub.add_parser("slug"); p.add_argument("week"); p.add_argument("target"); p.add_argument("native")
    p = sub.add_parser("edition-dir"); p.add_argument("target"); p.add_argument("native")
    sub.add_parser("frontmatter")
    p = sub.add_parser("check-repo")
    p.add_argument("--repo", default=os.path.expanduser("~/workspace/weekly-git"))
    args = ap.parse_args(argv)
    try:
        if args.cmd == "lang":
            out = lang(args.code)
        elif args.cmd == "thread":
            out = {"target": args.target, "discord_thread": thread(args.target)}
        elif args.cmd == "furniture":
            out = furniture(args.native, args.target, args.week)
        elif args.cmd == "vol":
            out = {"week": _norm_week(args.week), "vol": vol(args.week, args.allocate)}
        elif args.cmd == "slug":
            out = {"slug": slug(args.week, args.target, args.native)}
        elif args.cmd == "edition-dir":
            out = {"dir": edition_dir(args.target, args.native)}
        elif args.cmd == "frontmatter":
            out = T["frontmatter"]
        elif args.cmd == "check-repo":
            out = check_repo(args.repo)
            if out["mismatches"]:
                print(json.dumps(out, ensure_ascii=False, indent=2) if args.json else
                      f"MISMATCHES ({len(out['mismatches'])}):\n" + "\n".join(out["mismatches"]))
                return 1
        else:
            raise AssertionError(args.cmd)
    except (KeyError, ValueError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2
    if args.json or not isinstance(out, str):
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(out)
    if args.cmd == "check-repo":
        print(f"OK: {out['editions_checked']} editions checked, 0 mismatches" if not args.json else "")
    return 0


if __name__ == "__main__":
    sys.exit(main())
