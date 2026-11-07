#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export <slug>.text.md from the source manuscript (content*.py string
literals, in source order) — NEVER from a PDF/SVG. Shared W46 tool.
Usage: export_text.py <build-dir> <out.md> "<H1 title>"
Furniture (footers, masthead, page numbers) is excluded by pattern."""
import ast, sys, os, re

SKIP_SUBSTR = ("De Lucerna", "LUCERNA", "VOL.", "共 8 版", "Page ", "Pagina ",
               "Seite ", "Página ", "版 /", "面 /", "ELKE WEEK",
               "NIVEAU", "Leesniveau", "Van de redactie", "NIVEAU ")
FOOTER_RE = re.compile(r"第\s*\d+\s*[版面]|Page \d+ of 8|Pagina \d+ van 8|Seite \d+ von 8")
SKIP_EXACT = {"", "·"}

def is_furniture(s):
    s2 = s.strip()
    if s2 in SKIP_EXACT:
        return True
    if FOOTER_RE.search(s2):
        return True
    if re.fullmatch(r"[().·\s—\-–]*", s2):
        return True
    return any(k in s2 for k in SKIP_SUBSTR)

class Exporter:
    def __init__(self, build):
        self.build = build
        self.lines = []
        self.exn = 0
        self.strings = {}  # module-level NAME -> str
        self.quotes = []
        self.page = 0
        self.stop = False

    def eval_str(self, node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            a, b = self.eval_str(node.left), self.eval_str(node.right)
            return (a or "") + (b or "") if (a is not None or b is not None) else None
        if isinstance(node, ast.Name):
            return self.strings.get(node.id)
        return None

    def eval_list(self, node):
        if isinstance(node, ast.List):
            out = []
            for el in node.elts:
                s = self.eval_str(el)
                out.append(s if s is not None else "?")
            return out
        return None

    def collect_strings(self, tree):
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                    and isinstance(node.targets[0], ast.Name):
                s = self.eval_str(node.value)
                if s is not None and len(s) > 20:
                    self.strings[node.targets[0].id] = s

    def emit_ex(self, level, typ, key, note, body, opts, instr):
        self.exn += 1
        s = f"{self.exn}. [{level} · {typ}] {body or ''}"
        if opts:
            s += " " + " · ".join(opts)
        if key:
            s += f" — 答案：{key}"
        if note:
            s += f"（{note}）"
        if instr:
            s += f" [{instr}]"
        self.lines.append(s)

    def walk(self, path):
        self.stop = False
        src = open(path, encoding="utf-8").read()
        tree = ast.parse(src)
        self.collect_strings(tree)
        # golden sentences: module-level `quotes` list of (q, gloss, page)
        for node in tree.body:
            if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "quotes" \
                    and isinstance(node.value, ast.List):
                for el in node.value.elts:
                    if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                        q, cn, pg = (self.eval_str(x) for x in el.elts[:3])
                        self.quotes.append(f"> {q} — {cn} ({pg})")
        def rec(n):
            if self.stop:
                return
            if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) \
                    and getattr(n.value.func, "id", "") == "BSPage4":
                if self.page > 0:
                    self.page += 1
                    self.lines.extend(["", f"## Pagina {self.page}", ""])
                else:
                    self.page = 1
                for ch in ast.iter_child_nodes(n):
                    rec(ch)
                return
            if isinstance(n, ast.Call):
                if getattr(n.func, "id", "") == "Flow":
                    for k in n.keywords:
                        if k.arg == "tag" and isinstance(k.value, ast.Constant) and k.value.value == "P8-keys":
                            self.stop = True
                            return
                if getattr(n.func, "attr", None) == "end_report":
                    for ch in ast.iter_child_nodes(n):
                        rec(ch)
                    return
                name = getattr(n.func, "attr", None)
                if name == "para":
                    s = self.eval_str(n.args[0]) if n.args else None
                    if s is None and len(n.args) > 2:
                        s = self.eval_str(n.args[2])
                    if s and not is_furniture(s):
                        self.lines.append(s)
                        self.lines.append("")
                elif name == "head":
                    s = self.eval_str(n.args[0]) if n.args else None
                    if s and not is_furniture(s):
                        self.lines.extend(["", "## " + s, ""])
                elif name == "gloss":
                    s = self.eval_str(n.args[0]) if n.args else None
                    if s:
                        self.lines.append("> " + s)
                        self.lines.append("")
                elif name == "box":
                    t = self.eval_str(n.args[0]) if n.args else None
                    if t and not is_furniture(t):
                        self.lines.extend(["", "### " + t, ""])
                    if len(n.args) > 1 and isinstance(n.args[1], ast.List):
                        for el in n.args[1].elts:
                            if isinstance(el, ast.Tuple) and el.elts:
                                s = self.eval_str(el.elts[0])
                                if s and not is_furniture(s):
                                    self.lines.append(s)
                                    self.lines.append("")
                elif name == "ex":
                    a = [self.eval_str(x) for x in n.args[:5]]
                    opts = self.eval_list(n.args[5]) if len(n.args) > 5 else None
                    kw = {k.arg: self.eval_str(k.value) for k in n.keywords}
                    instr = kw.get("instr")
                    self.emit_ex(a[0], a[1], a[2], a[3], a[4], opts, instr)
                elif name == "match_set":
                    a = [self.eval_str(x) for x in n.args[:2]]
                    lefts = self.eval_list(n.args[2]) if len(n.args) > 2 else []
                    rights = self.eval_list(n.args[3]) if len(n.args) > 3 else []
                    keys = self.eval_list(n.args[4]) if len(n.args) > 4 else []
                    notes = self.eval_list(n.args[5]) if len(n.args) > 5 else []
                    kw = {k.arg: self.eval_str(k.value) for k in n.keywords}
                    start = self.exn + 1
                    self.lines.append(f"{start}–{start + len(lefts) - 1}. [{a[0]} · {a[1]}] {kw.get('instr') or ''}".rstrip())
                    for i, lf in enumerate(lefts):
                        self.exn += 1
                        ky = keys[i] if i < len(keys) else ""
                        ridx = ord(ky.strip().lower()) - 97 if ky and len(ky.strip()) == 1 else i
                        rt = rights[ridx] if 0 <= ridx < len(rights) else "?"
                        nt = notes[i] if i < len(notes) else ""
                        self.lines.append(f"{self.exn}. {lf} — {rt} (答案 {ky} · {nt})")
                    self.lines.append("")
                elif name == "text":
                    s = self.eval_str(n.args[2]) if len(n.args) > 2 else None
                    size = n.args[3].value if len(n.args) > 3 and isinstance(n.args[3], ast.Constant) else 0
                    if s and "ANTWOORDEN" in s:
                        self.stop = True
                        return
                    if s and size and size >= 24 and not is_furniture(s) and not s.strip().startswith("·"):
                        self.lines.extend(["", "### " + s, ""])
                        if "ZINNEN" in s and self.quotes:
                            self.lines.extend(self.quotes)
                            self.lines.append("")
                elif name == "end_report":
                    pass
            for ch in ast.iter_child_nodes(n):
                rec(ch)
        rec(tree)

def main():
    build, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
    ex = Exporter(build)
    ex.lines = ["# " + title, "", "## Pagina 1", ""]
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(build, fname)
        if os.path.exists(path):
            ex.walk(path)
            ex.lines.append("")
    # drop trailing page header left by the final end_report()
    while ex.lines and ex.lines[-1] == "":
        ex.lines.pop()
    if ex.lines and ex.lines[-1].startswith("## Pagina"):
        ex.lines.pop()
    text = "\n".join(ex.lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    open(out, "w", encoding="utf-8").write(text)
    print(f"wrote {out}: {ex.exn} exercises, {len(text)} bytes")

if __name__ == "__main__":
    main()
