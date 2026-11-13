# -*- coding: utf-8 -*-
"""Export <slug>.text.md from the SOURCE MANUSCRIPT (content*.py literals),
never from PDF/SVG. Collects printed prose strings in source order, grouped
by page (CURPAGE tracking). Excludes answer keys, key-notes, furniture
(foot/top band), code strings and file paths. Usage:
  python textmd.py <build_dir> <slug> <out_path> <title_line>
"""
import ast, os, re, sys

HANGUL = re.compile(r"[\uac00-\ud7a3]")
CJK = re.compile(r"[\u4e00-\u9fff]")
CYR = re.compile(r"[\u0400-\u04ff]")
KANA = re.compile(r"[\u3040-\u30ff]")

def is_prose(s):
    if len(s) < 2:
        return False
    # D7 (2026-11-11): reject only path-like slashes (no spaces around "/",
    # e.g. "assets/x"); " / " is a word-block separator in exercise stems
    # (P5/P8 D group: "저는 / 수요일에 / ... → ___") and must be kept.
    if re.search(r"\S/\S", s) or s.endswith((".py", ".pdf", ".svg", ".png", ".jpg", ".md")):
        return False
    if "assets/" in s or s.startswith("~") or s.startswith("hidden_files"):
        return False
    if HANGUL.search(s) or CJK.search(s) or CYR.search(s) or KANA.search(s):
        return True
    # Latin-script explanation prose (fan-outs): multi-word sentence
    if " " in s.strip() and len(s.strip()) >= 8 and re.search(r"[a-zA-Z]{3}", s):
        return True
    return False

# (receiver, method) -> positional arg indexes to collect (str or list-of-str)
CALL_ARGS = {
    ("p", "text"): [2], ("p", "para"): [2], ("p", "paraq"): [2],
    ("p", "band"): [0, 1, 2], ("p", "strip"): [2],
    ("f", "para"): [0], ("f", "lead_para"): [0], ("f", "head"): [0], ("f", "title"): [0],
    ("f", "byline"): [0], ("f", "gloss"): [0], ("f", "glossline"): [0],
    ("f", "section"): [0], ("f", "box"): [0, 1], ("f", "boxq"): [0, 1],
    ("f", "ex"): [4, 5], ("f", "match_set"): [2, 3],
}

# D7 (2026-11-11): .ex / .match_set are collected by method name, whatever
# the Flow receiver is called. The (receiver, method) table above only
# whitelisted ("f", "ex") / ("f", "match_set"), so the P1 quiz (qf),
# P2-P6 (e) and P7 (a/b/c) exercises were silently dropped (99 items).
METHOD_ARGS = {"ex": [4, 5], "match_set": [2, 3]}

def strings_from(node):
    """Yield (lineno, str) for string constants inside node (incl. lists)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        yield (node.lineno, node.value)
    elif isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        for el in node.elts:
            yield from strings_from(el)
    elif isinstance(node, ast.Dict):
        for k in node.keys:
            if k is not None:
                yield from strings_from(k)
        for v in node.values:
            yield from strings_from(v)

def collect(build_dir):
    items = []  # (page, lineno, seq, text)
    seq = 0
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(build_dir, fname)
        src = open(path, encoding="utf-8").read()
        tree = ast.parse(src, filename=fname)
        cur = None
        for node in ast.walk(tree):
            # CURPAGE assignment tracking needs order: walk top-level stmts
            pass
        for stmt in tree.body:
            for node in ast.walk(stmt):
                if isinstance(node, ast.Assign):
                    for t in node.targets:
                        if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Name) and t.value.id == "CURPAGE":
                            if isinstance(node.value, ast.Constant):
                                cur = int(node.value.value)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                    recv = node.func.value.id if isinstance(node.func.value, ast.Name) else None
                    key = (recv, node.func.attr)
                    method = node.func.attr
                    idxs = CALL_ARGS.get(key)
                    if idxs is None:
                        idxs = METHOD_ARGS.get(method)
                    if idxs is not None:
                        # p.text top band: skip y < 200
                        if key == ("p", "text") and node.args and isinstance(node.args[1], ast.Constant) and isinstance(node.args[1].value, (int, float)) and node.args[1].value < 200:
                            continue
                        for idx in idxs:
                            if idx < len(node.args):
                                for ln, s in strings_from(node.args[idx]):
                                    if is_prose(s):
                                        # R2-1 (2026-11-12): strings from .ex /
                                        # .match_set are exercise items; tag them so
                                        # the dedup below keeps one copy per call
                                        # site (per exercise block), not one per book.
                                        items.append((cur, ln, seq, s, method in METHOD_ARGS)); seq += 1
                        # keyword body= for .ex (any receiver)
                        for kw in node.keywords:
                            if kw.arg in ("body", "opts") and method == "ex":
                                for ln, s in strings_from(kw.value):
                                    if is_prose(s):
                                        items.append((cur, ln, seq, s, True)); seq += 1
                # module-level prose constants (topics, briefs, nums, rows, quotes, letters...)
                if isinstance(node, ast.Assign) and isinstance(node.value, (ast.List, ast.Tuple, ast.Dict)):
                    skip_names = {"OUT"}
                    names = [t.id for t in node.targets if isinstance(t, ast.Name)]
                    if not any(n in skip_names for n in names):
                        for ln, s in strings_from(node.value):
                            if is_prose(s):
                                items.append((cur, ln, seq, s, False)); seq += 1
                # A1 (D6 fix 2026-11-11): module-level plain-string assignments
                # (wt/lt/lcn/etvous/MODELO...). A top-level `x = "..."` is prose
                # used twice (wrap() for box height + p.para/f.para print); the
                # List/Tuple/Dict branch above never sees it and strings_from()
                # drops ast.Name args, so these were silently missing from text.md.
                if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                    if is_prose(node.value.value):
                        items.append((cur, node.value.lineno, seq, node.value.value, False)); seq += 1
    # sort by (page, file order approx via seq) — seq already reflects file
    # order; keep seq order, group by page preserving first-seen page order
    # R2-1 (2026-11-12): the old global `seen` dedup (one copy of each
    # normalized string per book) silently dropped exercise items that share
    # a string with an earlier page/block: P2 D Q26, P4 D Q61-63, P8 B
    # Q121/Q126 stems and P8 F Q142. Exercise items (.ex stems/opts and
    # .match_set terms/glosses) are therefore deduped by call site, not by
    # string: each call site is one exercise block, so the same stem/term
    # legitimately re-appears in its own block (re-test questions, match
    # words that also occur in a date box or route map). Plain prose keeps
    # the old global string dedup; exercise items are never added to `seen`
    # either, so a prose line that happens to share an exercise string is
    # still kept in its own place.
    seen = set()
    pages = {}
    for pg, ln, sq, s, is_ex in sorted(items, key=lambda t: t[2]):
        norm = re.sub(r"\s+", " ", s).strip()
        if is_ex:
            pages.setdefault(pg, []).append(norm)
            continue
        if norm in seen:
            continue
        seen.add(norm)
        pages.setdefault(pg, []).append(norm)
    return pages

def main():
    build_dir, slug, out_path, title = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    pages = collect(build_dir)
    lines = [f"# {title}", "",
             f"Slug: `{slug}` — text exported from the source manuscript (content*.py); not extracted from PDF.",
             ""]
    for pg in sorted(pages, key=lambda p: (p is None, p)):
        label = f"Page {pg}" if pg else "Front matter"
        lines.append(f"## {label}")
        lines.append("")
        for s in pages[pg]:
            lines.append(s)
            lines.append("")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("wrote", out_path, "pages:", sorted([p for p in pages if p]), "items:", sum(len(v) for v in pages.values()))

if __name__ == "__main__":
    main()
