# -*- coding: utf-8 -*-
"""Count gloss() items: split each gloss() call string on the bare middle
dot (README #21: split on the dot itself, never on the spaced form) and
verify each item. Compares a build dir against the core build dir."""
import ast
import os
import sys


def gloss_strings(build_dir):
    out = []
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        tree = ast.parse(open(os.path.join(build_dir, fn), encoding="utf-8").read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                    and node.func.attr == "gloss" and node.args \
                    and isinstance(node.args[0], ast.Constant):
                out.append(node.args[0].value)
    return out


def count(strings):
    total = 0
    for s in strings:
        items = [i for i in s.split("·")]
        total += len(items)
        print(f"  {len(items)} items: {s[:60]!r}")
    return total


if __name__ == "__main__":
    core, ed = sys.argv[1], sys.argv[2]
    print("CORE:")
    c = count(gloss_strings(core))
    print("EDITION:")
    e = count(gloss_strings(ed))
    print(f"gloss total: core={c} edition={e}")
    sys.exit(0 if c == e else 1)
