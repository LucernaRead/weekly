# -*- coding: utf-8 -*-
"""Export <slug>.text.md for a W46 EN-family edition from its own build-dir
source manuscript (AST walk of content*.py, never executed, never from a
PDF/SVG). Format mirrors the finished EN x DE / core .text.md files:
plain reading-order lines, EXERCISE:/MATCH: lines, and a single Answers
section reconstructed from the exercise registry (ex + match_set + reg_ex
calls, including the P8 battery `for` loops over literal data lists).

Usage: en_textmd.py <build-dir> <out.md> <slug> "<reader label>"
"""
import ast, os, re, sys

PAGE_LINE_RE = re.compile(
    r"^(Page \d+ of \d+|Seite \d+ von \d+|Page \d+ sur \d+|Página \d+ de \d+"
    r"|Pagina \d+ (di|van) \d+|\d+ ページ（全 \d+ ページ）|제 \d+ 면 / 총 \d+ 면"
    r"|第 \d+ 版 / 共 \d+ 版|Страница \d+ из \d+)$")


def is_furniture(s):
    s2 = s.strip()
    if not s2 or s2 in ("·", "sans", "serif"):
        return True
    if s2.startswith("The Lucerna ·"):
        return True
    if PAGE_LINE_RE.match(s2):
        return True
    if re.fullmatch(r"[().·\s—\-–]*", s2):
        return True
    return False


class Exporter:
    def __init__(self):
        self.lines = []
        self.exn = 0
        self.page = 0
        self.strings = {}   # module-level NAME -> long str
        self.lists = {}     # module-level NAME -> list of evaluated items
        self.env = {}       # loop-bound NAME -> value
        self.stop = False

    # ---- evaluation ----
    def eval_str(self, node):
        if isinstance(node, ast.Constant):
            return node.value if isinstance(node.value, str) else None
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            a, b = self.eval_str(node.left), self.eval_str(node.right)
            if a is None and b is None:
                return None
            return (a or "") + (b or "")
        if isinstance(node, ast.Name):
            if node.id in self.env:
                v = self.env[node.id]
                return v if isinstance(v, str) else (str(v) if v is not None else None)
            return self.strings.get(node.id)
        if isinstance(node, ast.JoinedStr):
            out = []
            for v in node.values:
                if isinstance(v, ast.Constant):
                    out.append(str(v.value))
                elif isinstance(v, ast.FormattedValue):
                    s = self.eval_str(v.value)
                    out.append(s if s is not None else "{...}")
                else:
                    out.append("{...}")
            return "".join(out)
        if isinstance(node, ast.Subscript):
            base = self.eval_value(node.value)
            idx = node.slice.value if isinstance(node.slice, ast.Constant) else None
            if isinstance(base, (list, tuple)) and isinstance(idx, int):
                v = base[idx]
                return v if isinstance(v, str) else str(v)
            return "{...}"
        if isinstance(node, ast.Call):
            fn = getattr(node.func, "id", "") or getattr(node.func, "attr", "")
            if fn == "join":
                parts = self.eval_value(node.args[0]) if node.args else None
                if isinstance(parts, list):
                    return " · ".join(str(p) for p in parts)
            return None
        return None

    def eval_value(self, node):
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, (ast.List, ast.Tuple)):
            return [self.eval_value(e) for e in node.elts]
        if isinstance(node, ast.Name):
            if node.id in self.env:
                return self.env[node.id]
            if node.id in self.lists:
                return self.lists[node.id]
            return self.strings.get(node.id)
        s = self.eval_str(node)
        return s

    def eval_iter(self, node):
        """Return a list of items for a for-loop / comprehension iter, or None."""
        if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "zip":
            parts = [self.eval_iter(a) for a in node.args]
            if all(isinstance(p, list) for p in parts):
                return list(zip(*parts))
            return None
        v = self.eval_value(node)
        if isinstance(v, list):
            return v
        return None

    def bind(self, target, value):
        if isinstance(target, ast.Name):
            self.env[target.id] = value
        elif isinstance(target, ast.Tuple):
            for t, v in zip(target.elts, value if isinstance(value, (list, tuple)) else []):
                self.bind(t, v)

    def collect(self, tree):
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                    and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                if isinstance(node.value, (ast.List, ast.Tuple)):
                    self.lists[name] = [self.eval_value(e) for e in node.value.elts]
                s = self.eval_str(node.value)
                if s is not None and len(s) > 20:
                    self.strings[name] = s

    # ---- emission ----
    def emit(self, s):
        if s and not is_furniture(s):
            t = s.strip()
            if t == "{...}":
                return  # unresolved f-string fragment, not display text
            self.lines.append(t)
            self.lines.append("")

    def register(self, level, typ, key, note):
        self.exn += 1
        self.reg.append((self.exn, level, typ, key, note))
        return self.exn

    def walk(self, path):
        src = open(path, encoding="utf-8").read()
        tree = ast.parse(src)
        self.collect(tree)
        self.reg = getattr(self, "reg", [])

        def rec(n):
            if self.stop:
                return
            # reg_ex list comprehension assigned to a name (cnums/gnums):
            # register each item AND bind the name to the numbers list.
            if isinstance(n, ast.Assign) and len(n.targets) == 1 \
                    and isinstance(n.targets[0], ast.Name) \
                    and isinstance(n.value, ast.ListComp):
                lc = n.value
                if isinstance(lc.elt, ast.Call) and getattr(lc.elt.func, "id", "") == "reg_ex":
                    gen = lc.generators[0]
                    items = self.eval_iter(gen.iter)
                    if items is not None:
                        nums = []
                        saved = dict(self.env)
                        for it in items:
                            self.bind(gen.target, it)
                            a = [self.eval_str(x) for x in lc.elt.args[:4]]
                            nums.append(self.register(a[0], a[1], a[2], a[3]))
                        self.env = saved
                        self.env[n.targets[0].id] = nums
                        return
            # page break: a fresh BSPage4 assignment
            if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) \
                    and getattr(n.value.func, "id", "") == "BSPage4":
                self.page += 1
                self.lines.extend(["", f"## Page P{self.page}", ""])
                for ch in ast.iter_child_nodes(n):
                    rec(ch)
                return
            # P8-keys flow: stop the manuscript here (answers are appended
            # separately from the registry)
            if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) \
                    and getattr(n.value.func, "id", "") == "Flow":
                for kw in n.value.keywords:
                    if kw.arg == "tag" and isinstance(kw.value, ast.Constant) \
                            and kw.value.value == "P8-keys":
                        self.stop = True
                        return
            if isinstance(n, ast.For):
                # Evaluate a loop only when its body registers exercises
                # (the P8 battery); display-only loops (directory, charts)
                # are walked once with unresolved names, like the shipped
                # exporter, so their loop-bound text is skipped.
                has_ex = any(
                    isinstance(x, ast.Call) and (
                        getattr(x.func, "attr", None) or getattr(x.func, "id", "")
                    ) in ("ex", "match_set", "reg_ex")
                    for x in ast.walk(n))
                if has_ex:
                    items = self.eval_iter(n.iter)
                    if items is not None:
                        saved = dict(self.env)
                        for it in items:
                            self.bind(n.target, it)
                            for st in n.body:
                                rec(st)
                        self.env = saved
                        return
            if isinstance(n, ast.ListComp):
                # only reg_ex comprehensions (cnums/gnums) matter here
                if isinstance(n.elt, ast.Call) and getattr(n.elt.func, "id", "") == "reg_ex":
                    gen = n.generators[0]
                    items = self.eval_iter(gen.iter)
                    if items is not None:
                        nums = []
                        saved = dict(self.env)
                        for it in items:
                            self.bind(gen.target, it)
                            a = [self.eval_str(x) for x in n.elt.args[:4]]
                            nums.append(self.register(a[0], a[1], a[2], a[3]))
                        self.env = saved
                        return nums
            if isinstance(n, ast.Call):
                name = getattr(n.func, "attr", None) or getattr(n.func, "id", "")
                if name == "foot":
                    return
                if name in ("para", "head", "gloss", "bridge", "instrline", "expl"):
                    # f.para("text") vs p.para(x, y, "text", ...): fall back
                    # to args[2] when args[0] is not display text.
                    s = self.eval_str(n.args[0]) if n.args else None
                    if s is None and len(n.args) > 2:
                        s = self.eval_str(n.args[2])
                    self.emit(s)
                elif name == "band":
                    self.emit(self.eval_str(n.args[0]) if n.args else None)
                    if len(n.args) > 2:
                        self.emit(self.eval_str(n.args[2]))
                elif name == "box":
                    # shipped format emits the box title only, not its rows
                    self.emit(self.eval_str(n.args[0]) if n.args else None)
                elif name == "text":
                    s = self.eval_str(n.args[2]) if len(n.args) > 2 else None
                    size = n.args[3].value if len(n.args) > 3 \
                        and isinstance(n.args[3], ast.Constant) else 0
                    if s and size and size >= 18:
                        self.emit(s)
                elif name == "reg_ex":
                    a = [self.eval_str(x) for x in n.args[:4]]
                    self.register(a[0], a[1], a[2], a[3])
                elif name == "ex":
                    a = [self.eval_str(x) for x in n.args[:5]]
                    opts = self.eval_value(n.args[5]) if len(n.args) > 5 else None
                    level, typ, key, note, body = a
                    self.register(level, typ, key, note)
                    s = f"EXERCISE: {body or ''}"
                    if isinstance(opts, list) and opts:
                        s += " " + " · ".join(
                            f"{chr(65 + i)}. {o}" for i, o in enumerate(opts) if o)
                    self.lines.append(s)
                    self.lines.append("")
                elif name == "match_set":
                    a = [self.eval_str(x) for x in n.args[:2]]
                    lefts = self.eval_value(n.args[2]) if len(n.args) > 2 else []
                    rights = self.eval_value(n.args[3]) if len(n.args) > 3 else []
                    keys = self.eval_value(n.args[4]) if len(n.args) > 4 else []
                    notes = self.eval_value(n.args[5]) if len(n.args) > 5 else []
                    for i, lf in enumerate(lefts or []):
                        self.register(a[0], a[1],
                                      keys[i] if i < len(keys) else "",
                                      notes[i] if i < len(notes) else "")
                        self.lines.append(f"MATCH: {lf}")
                    for rt in rights or []:
                        self.lines.append(f"MATCH: {rt}")
                    self.lines.append("")
            for ch in ast.iter_child_nodes(n):
                rec(ch)
        rec(tree)


def main():
    build, out, slug, label = sys.argv[1:5]
    ex = Exporter()
    ex.reg = []
    ex.lines = [
        "# The Lucerna — English Weekly VOL.3 (2026-W46, 9–15 November 2026)",
        "",
        f"Target: English. Reader language: {label}. Levels A2–B2. 150 exercises.",
        "",
        "Source manuscript export: headings, paragraphs and exercises in original order, "
        "exported from the build source files (content12.py, content34.py, content56.py, "
        "content7.py, content8.py). Answers appended from the exercise registry.",
        "",
    ]
    for fname in ["content12.py", "content34.py", "content56.py",
                  "content7.py", "content8.py"]:
        path = os.path.join(build, fname)
        if os.path.exists(path):
            ex.walk(path)
            ex.lines.append("")
    ex.lines.extend(["", "## Answers (Page 8, from the exercise registry)", ""])
    for n, level, typ, key, note in ex.reg:
        s = f"{n}. [{level}] {typ} — {key}"
        if note:
            s += f" ({note})"
        ex.lines.append("")
        ex.lines.append(s)
    text = "\n".join(ex.lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    open(out, "w", encoding="utf-8").write(text)
    print(f"wrote {out}: {ex.exn} exercises, {len(text)} bytes")


if __name__ == "__main__":
    main()
