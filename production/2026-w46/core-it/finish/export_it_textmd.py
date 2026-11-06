# -*- coding: utf-8 -*-
"""Export <slug>.text.md for W46 IT editions from the edition's own build-dir
sources (AST string literals, in source order) — never from PDF/SVG.

Pattern: hidden_files/w46/export_textmd.py (DE family). Page headings are the
core's Italian section names. P8 answer lines are reconstructed from the
ex()/match_set() registry calls in source order (numbers 1..150), matching
the P8-keys render loop over REG. f-strings resolve only via the per-file
env (MODELO/NWORDS); unresolved interpolations are skipped as furniture.
"""
import ast, os, re, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HID = os.path.join(GOAL, "hidden_files")
PAGES = ["Prima", "Vita", "Cultura", "Sport", "Giovani", "Approfondimento", "Lingua", "Valutazione e risposte"]
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

EDITIONS = [
    ("de", "2026-w46-it-de"), ("en", "2026-w46-it-en"), ("es", "2026-w46-it-es"),
    ("fr", "2026-w46-it-fr"), ("ja", "2026-w46-it-ja"), ("ko", "2026-w46-it-ko"),
    ("nl", "2026-w46-it-nl"), ("pt", "2026-w46-it-pt"), ("ru", "2026-w46-it-ru"),
    ("zh-tw", "2026-w46-it-zh-tw"),
]


class Exporter:
    def __init__(self):
        self.env = {}       # NAME -> str | int | list
        self.lines = []     # (page_no, text)
        self.page = 0
        self.exn = 0
        self.answers = []   # (n, key, note, type)
        self.saw_p8keys = False
        self.gloss_prefix = ""
        self.writing_type = None

    def detect_writing_type(self, tree):
        """The P8-keys loop tests e_['type'] == '<writing type>' (translated
        per edition); that literal is this edition's writing type."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Compare) and len(node.ops) == 1 \
                    and isinstance(node.ops[0], ast.Eq):
                left, comp = node.left, node.comparators[0]
                if isinstance(left, ast.Subscript) and isinstance(comp, ast.Constant) \
                        and isinstance(comp.value, str):
                    self.writing_type = comp.value
                    return

    def gloss_prefix_from(self, bdir):
        """bslib4.Flow.gloss renders prefix + s (e.g. 'NOTE · '); the prefix
        lives in bslib, not in the content string. Extract it so the export
        matches the rendered text."""
        try:
            tree = ast.parse(open(os.path.join(bdir, "bslib4.py"), encoding="utf-8").read())
        except Exception:
            return
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == "gloss":
                for sub in ast.walk(node):
                    if isinstance(sub, ast.BinOp) and isinstance(sub.op, ast.Add) \
                            and isinstance(sub.left, ast.Constant) and isinstance(sub.left.value, str) \
                            and isinstance(sub.right, ast.Name) and sub.right.id == "s":
                        self.gloss_prefix = sub.left.value
                        return

    # ---------- value evaluation ----------
    def strval(self, node):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            v = self.env.get(node.id)
            return v if isinstance(v, str) else None
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            a, b = self.strval(node.left), self.strval(node.right)
            if a is not None and b is not None:
                return a + b
            return None
        if isinstance(node, ast.JoinedStr):
            parts = []
            for v in node.values:
                if isinstance(v, ast.Constant):
                    parts.append(str(v.value))
                elif isinstance(v, ast.FormattedValue):
                    inner = v.value
                    if isinstance(inner, ast.Name) and inner.id in self.env:
                        val = self.env[inner.id]
                        if isinstance(val, (int, float)) and v.format_spec:
                            spec = "".join(c.value for c in v.format_spec.values if isinstance(c, ast.Constant))
                            try:
                                parts.append(format(val, spec))
                            except Exception:
                                return None
                        else:
                            parts.append(str(val))
                    else:
                        return None
                else:
                    return None
            joined = "".join(parts)
            # Keep only f-strings whose interpolations all resolved from the
            # env (NWORDS bridges/notes); furniture f-strings (page numbers,
            # separators) hit the unresolved branch above and return None.
            return joined
        return None

    def listvals(self, node):
        out = []
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            for e in node.elts:
                v = self.strval(e)
                if v is not None:
                    out.append(v)
                elif isinstance(e, (ast.List, ast.Tuple, ast.Set)):
                    out.extend(self.listvals(e))
                elif isinstance(e, ast.Constant) and isinstance(e.value, (int, float)):
                    out.append(e.value)
                else:
                    out.extend(self.listvals(e))
        elif isinstance(node, ast.Name):
            v = self.env.get(node.id)
            if isinstance(v, list):
                flat = []
                for r in v:
                    if isinstance(r, list):
                        flat.extend(r)
                    else:
                        flat.append(r)
                return flat
        return out

    def rowvals(self, node):
        """One row of a list literal: scalar -> [value], tuple/list -> its values."""
        if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
            return self.listvals(node)
        v = self.strval(node)
        if v is not None:
            return [v]
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return [node.value]
        return []

    def collect_env(self, tree):
        # Lists only (pre-collected: For-loop iters are always defined before
        # the loop). Strings are recorded IN ORDER during visit(), because
        # names like `etvous` are re-assigned per page and must resolve to
        # the value in force at the point of use.
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                if isinstance(node.value, (ast.List, ast.Tuple)):
                    rows = [self.rowvals(e) for e in node.value.elts]
                    if rows:
                        self.env[name] = rows

    def emit(self, txt):
        t = txt.strip()
        if len(t) > 1:
            self.lines.append((self.page, t))

    # ---------- walking ----------
    def walk_file(self, path):
        tree = ast.parse(open(path, encoding="utf-8").read())
        self.env = {}
        self.collect_env(tree)
        if path.endswith("content8.py"):
            self.detect_writing_type(tree)
        self.visit(tree)

    def visit(self, node):
        if isinstance(node, ast.Assign):
            # CURPAGE[0] = N  -> page change
            for tgt in node.targets:
                if isinstance(tgt, ast.Subscript) and isinstance(tgt.value, ast.Name) \
                        and tgt.value.id == "CURPAGE" and isinstance(node.value, ast.Constant):
                    self.page = int(node.value.value)
            # record string/int assignments in source order (etvous, lt, bb, ...)
            if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                s = self.strval(node.value)
                if s is not None:
                    self.env[name] = s
                elif isinstance(node.value, ast.Call) and getattr(node.value.func, "id", "") == "len":
                    arg = node.value.args[0] if node.value.args else None
                    if isinstance(arg, ast.Call) and isinstance(arg.func, ast.Attribute) \
                            and arg.func.attr == "split" and isinstance(arg.func.value, ast.Name):
                        base = self.env.get(arg.func.value.id)
                        if isinstance(base, str):
                            self.env[name] = len(base.split())
            for ch in ast.iter_child_nodes(node):
                self.visit(ch)
            return
        if isinstance(node, ast.For):
            # emit the iterated list's contents (sett/som/facts/steps/dpb/quotes),
            # preserving row structure: one line per string, "gloss (page)" for
            # quote rows, "Lab V°" for chart rows.
            rows = None
            it = node.iter
            if isinstance(it, ast.Call) and getattr(it.func, "id", "") in ("enumerate", "zip") and it.args:
                it = it.args[0]
            if isinstance(it, ast.Name) and isinstance(self.env.get(it.id), list):
                rows = self.env[it.id]
            elif isinstance(it, (ast.List, ast.Tuple)):
                rows = [self.rowvals(e) for e in it.elts]
            if rows:
                for row in rows:
                    if isinstance(row, str):
                        self.emit(row)
                    elif isinstance(row, list):
                        strs = [x for x in row if isinstance(x, str)]
                        nums = [x for x in row if isinstance(x, (int, float))]
                        if len(strs) == 1 and len(nums) == 1:
                            self.emit(f"{strs[0]} {nums[0]:g}°")
                        elif len(strs) == 3 and re.fullmatch(r"Pagina \d+", strs[2]):
                            self.emit(strs[0])
                            self.emit(f"{strs[1]} ({strs[2]})")
                        else:
                            for x in strs:
                                self.emit(x)
            for ch in ast.iter_child_nodes(node):
                self.visit(ch)
            return
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else "")
            args = node.args
            recv = fn.value.id if isinstance(fn, ast.Attribute) and isinstance(fn.value, ast.Name) else ""
            if name == "Flow":
                for kw in node.keywords:
                    if kw.arg == "tag" and isinstance(kw.value, ast.Constant) and kw.value.value == "P8-keys":
                        self.saw_p8keys = True
            elif name == "text":
                if len(args) >= 3:
                    v = self.strval(args[2])
                    if v:
                        self.emit(v)
            elif name == "para":
                idx = 2 if recv == "p" else 0
                if len(args) > idx:
                    v = self.strval(args[idx])
                    if v:
                        self.emit(v)
            elif name in ("head", "bridge", "title", "byline", "expl"):
                if args:
                    v = self.strval(args[0])
                    if v:
                        self.emit(v)
            elif name == "gloss":
                if args:
                    v = self.strval(args[0])
                    if v:
                        self.emit(self.gloss_prefix + v)
            elif name == "box":
                if args:
                    v = self.strval(args[0])
                    if v:
                        self.emit(v)
                if len(args) >= 2:
                    for el in self._box_rows(args[1]):
                        self.emit(el)
            elif name == "band":
                for a in args:
                    v = self.strval(a)
                    if v:
                        self.emit(v)
            elif name == "strip":
                if len(args) >= 3:
                    v = self.strval(args[2])
                    if v:
                        self.emit(v)
            elif name == "shead":
                if len(args) >= 3:
                    v = self.strval(args[2])
                    if v:
                        self.emit(v)
            elif name == "caption":
                if len(args) >= 5:
                    v = self.strval(args[4])
                    if v:
                        self.emit(v)
                if len(args) >= 6:
                    v = self.strval(args[5])
                    if v:
                        self.emit(v)
                for kw in node.keywords:
                    if kw.arg == "credit":
                        v = self.strval(kw.value)
                        if v:
                            self.emit(v)
            elif name == "ex":
                a = [self.strval(x) for x in args[:5]]
                level, typ, key, note, body = (a + [None] * 5)[:5]
                opts = self.listvals(args[5]) if len(args) > 5 else []
                kw = {k.arg: self.strval(k.value) for k in node.keywords}
                instr = kw.get("instr")
                self.exn += 1
                self.answers.append((self.exn, key or "", note or "", typ or ""))
                s = f"{self.exn}. [{level} · {typ}] {body or ''}"
                if opts:
                    s += " " + " · ".join(str(o) for o in opts)
                if key:
                    s += f" — key: {key}"
                if note:
                    s += f" ({note})"
                if instr:
                    s += f" [{instr}]"
                self.emit(s)
            elif name == "match_set":
                a = [self.strval(x) for x in args[:2]]
                lefts = self.listvals(args[2]) if len(args) > 2 else []
                rights = self.listvals(args[3]) if len(args) > 3 else []
                keys = self.listvals(args[4]) if len(args) > 4 else []
                notes = self.listvals(args[5]) if len(args) > 5 else []
                kw = {k.arg: self.strval(k.value) for k in node.keywords}
                start = self.exn + 1
                self.emit(f"{start}–{start + len(lefts) - 1}. [{a[0]} · {a[1]}] {kw.get('instr') or ''}".rstrip())
                for i, lf in enumerate(lefts):
                    self.exn += 1
                    ky = keys[i] if i < len(keys) else ""
                    ridx = ord(ky.strip().lower()) - 97 if ky and len(ky.strip()) == 1 else i
                    rt = rights[ridx] if 0 <= ridx < len(rights) else "?"
                    nt = notes[i] if i < len(notes) else ""
                    self.answers.append((self.exn, ky, nt, a[1] or ""))
                    self.emit(f"{self.exn}. {lf} — {rt} (key {ky} · {nt})")
        for ch in ast.iter_child_nodes(node):
            self.visit(ch)

    def _box_rows(self, node):
        rows = []
        if isinstance(node, (ast.List, ast.Tuple)):
            for el in node.elts:
                if isinstance(el, (ast.List, ast.Tuple)) and el.elts:
                    v = self.strval(el.elts[0])
                    if v:
                        rows.append(v)
                else:
                    v = self.strval(el)
                    if v:
                        rows.append(v)
        return rows


def fix_quotes_lines(lines):
    """Quotes rows were emitted as 3 separate lines (quote, gloss, page);
    rejoin gloss+page into 'gloss (page)' when a bare page token follows."""
    out = []
    i = 0
    while i < len(lines):
        pg, t = lines[i]
        if i + 2 < len(lines) and lines[i + 1][0] == pg and lines[i + 2][0] == pg \
                and lines[i + 2][1] in ("Pagina 1", "Pagina 2", "Pagina 3", "Pagina 4", "Pagina 5", "Pagina 6") \
                and t.startswith("«"):
            out.append((pg, t))
            out.append((pg, f"{lines[i+1][1]} ({lines[i+2][1]})"))
            i += 3
        else:
            out.append((pg, t))
            i += 1
    return out


def main():
    only = sys.argv[1:] or None
    for code, slug in EDITIONS:
        if only and code not in only:
            continue
        bdir = os.path.join(HID, f"weekly-report-w46-it-{code}-build")
        ex = Exporter()
        ex.gloss_prefix_from(bdir)
        for f in FILES:
            ex.walk_file(os.path.join(bdir, f))
        assert ex.exn == 150, (code, ex.exn)
        lines = ex.lines
        # consecutive dedupe
        ded = []
        for item in lines:
            if not ded or ded[-1][1] != item[1]:
                ded.append(item)
        out_lines = [f"# {slug}", ""]
        cur = 0
        for pg, t in ded:
            if pg != cur and 1 <= pg <= 8:
                out_lines.append(f"## {PAGES[pg-1]}")
                out_lines.append("")
                cur = pg
            out_lines.append(t)
            out_lines.append("")
        if ex.saw_p8keys:
            out_lines.append("### Risposte")
            out_lines.append("")
            for n, key, note, typ in ex.answers:
                if typ and typ == ex.writing_type:
                    out_lines.append(f"{n}. ✓ {note}")
                else:
                    out_lines.append(f"{n}. {key} — {note}")
                out_lines.append("")
        eddir = os.path.join(GOAL, "files", f"weekly-report-w46-it-{code}")
        out = os.path.join(eddir, f"{slug}.text.md")
        text = "\n".join(out_lines).strip() + "\n"
        open(out, "w", encoding="utf-8").write(text)
        print(slug, "exercises:", ex.exn, "bytes:", len(text.encode("utf-8")), "lines:", len(out_lines))


if __name__ == "__main__":
    main()
