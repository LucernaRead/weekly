#!/usr/bin/env python3
"""Simulate the P8 keys flow for a build dir: total height vs the 4-column
budget (1328 -> 2540). Uses the build's own svglib wrap(). AST only.
"""
import ast, sys, os, importlib.util

def load_svglib(build):
    spec = importlib.util.spec_from_file_location("svglib_sim", os.path.join(build, "svglib.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def const_str(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                parts.append(str(v.value))
            elif isinstance(v, ast.FormattedValue):
                parts.append("164")  # NCHARS
        return "".join(parts)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        a, b = const_str(node.left), const_str(node.right)
        return None if a is None or b is None else a + b
    return None

def main():
    build = sys.argv[1]
    svglib = load_svglib(build)
    wrap = svglib.wrap
    entries = []  # (page, key, note, type)
    # page assignment: track current page via OUT path literals / band calls is
    # fragile; instead use file order + count: entries are registered in file
    # order content12(p1,p2), content34(p3,p4), content56(p5,p6), content7(p7),
    # content8(p8). We only need TOTAL height + per-entry lines, so page
    # grouping for headers: count entries per file-half via the '{OUT}/pN'
    # literal positions.
    files = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
    all_entries = []
    for fname in files:
        src = open(os.path.join(build, fname), encoding="utf-8").read()
        tree = ast.parse(src)
        # find page boundaries: line numbers of '{OUT}/p' string constants
        bounds = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) \
                    and node.value.startswith("{OUT}/p"):
                bounds.append(node.lineno)
        calls = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                    and node.func.attr in ("ex", "match_set"):
                calls.append(node)
        calls.sort(key=lambda n: n.lineno)
        for node in calls:
            page = 1
            if bounds:
                page = 1 + sum(1 for b in bounds if node.lineno > b)
            # page within file: content12 -> p1/p2 etc. Map file+half:
            base = {"content12.py": 1, "content34.py": 3, "content56.py": 5,
                    "content7.py": 7, "content8.py": 8}[fname]
            pg = base + (page - 1)
            if node.func.attr == "ex":
                args = node.args
                key = const_str(args[2]); note = const_str(args[3])
                typ = const_str(args[1]) or ""
                all_entries.append((pg, key, note, typ))
            else:
                def list_strs(n):
                    if isinstance(n, (ast.List, ast.Tuple)):
                        return [const_str(e) for e in n.elts]
                    return []
                keys = list_strs(node.args[4]) if len(node.args) > 4 else []
                notes = list_strs(node.args[5]) if len(node.args) > 5 else []
                for k, nt in zip(keys, notes):
                    all_entries.append((pg, k, nt, "matching"))
    print("entries:", len(all_entries))
    # simulate flow: 4 cols, top 1328, bottom 2540, para lh 1.16 size 13.3
    SIZE, LH, GAP = 13.3, 1.16, 0.5
    col, y = 0, 1328
    total_lines = 0
    longest = []
    cur_page = None
    for idx, (pg, key, note, typ) in enumerate(all_entries, 1):
        if pg != cur_page:
            cur_page = pg
            # header para: size 13.3, lh 1.16, gap 2, split=False; _fit uses
            # h+gap, advance is size + h + gap (Flow.para exact math)
            h = 1 * SIZE * LH
            if y + h + 2 > 2540:
                col += 1; y = 1328
            y += SIZE + h + 2
        if typ == "写作":
            txt = f"{idx}. ✓ {note}"
        else:
            txt = f"{idx}. {key} — {note}"
        lines = wrap(txt, "serif", False, SIZE, 434)
        total_lines += len(lines)
        h = len(lines) * SIZE * LH
        if y + h + GAP > 2540:
            col += 1; y = 1328
            if col > 3:
                print("OVERFLOW beyond col 3 at entry", idx, pg, key)
                break
        y += SIZE + h + GAP
        longest.append((len(lines), len(txt), pg, key, note))
    longest.sort(reverse=True)
    print(f"columns used: {col+1}, final y in last col: {y:.1f} (bottom 2540)")
    print("total wrapped lines:", total_lines)
    print("longest 15:")
    for ln, ch, pg, k, nt in longest[:15]:
        print(f"  p{pg} {ln} lines {ch}ch key={k!r} note={nt[:70]!r}")

if __name__ == "__main__":
    main()
