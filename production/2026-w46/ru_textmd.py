# -*- coding: utf-8 -*-
"""Export <slug>.text.md from the source manuscript (content*.py literals, in
source order) — NEVER from a PDF or SVG. RU-family W46 tool.
Usage: ru_textmd.py <build-dir> <out.md> "<H1 title>"
Furniture (masthead, badge, footers, page lines) is excluded by pattern.
P8 answer key is reconstructed from the collected ex()/match_set() calls,
grouped by page, mirroring the printed key section."""
import ast, sys, os, re

SKIP_SUBSTR = ("КАЖДУЮ НЕДЕЛЮ", "ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА", "LUCERNA RUSSIAN WEEKLY",
               "VOL.", "Lucerna ·", "TEXT IN RUSSIAN", "RUSSISCHER TEXT",
               "TEXTES EN RUSSE", "TEXTO EN RUSO", "TESTI IN RUSSO",
               "TEXTOS EM RUSSO", "TEKSTEN IN HET RUSSISCH",
               "ロシア語テキスト", "러시아어 텍스트", "俄語正文",
               "ЕЖЕНЕДЕЛЬНАЯ", "THE EDITION FOR", "DIE AUSGABE FÜR",
               "L'ÉDITION POUR", "LA EDICIÓN PARA", "L'EDIZIONE PER",
               "A EDIÇÃO PARA", "DE EDITIE VOOR", "日本語読者のための版",
               "한국어 독자를 위한 판", "給繁體中文讀者的版本")
PAGE_LINE_RE = re.compile(r"^(Page \d+ of \d+|Seite \d+ von \d+|Page \d+ sur \d+|Página \d+ de \d+|Pagina \d+ (di|van) \d+|\d+ ページ（全 \d+ ページ）|제 \d+ 면 / 총 \d+ 면|第 \d+ 版 / 共 \d+ 版)$")

def is_furniture(s):
    s2 = s.strip()
    if not s2 or s2 == "·" or s2 == "Lucerna":
        return True
    if PAGE_LINE_RE.match(s2):
        return True
    return any(k in s2 for k in SKIP_SUBSTR)

class Exporter:
    def __init__(self):
        self.lines = []
        self.exn = 0
        self.page = 0
        self.strings = {}
        self.reg = []  # (page, n, key, note, type)
        self.quotes = []

    def eval_str(self, node):
        if isinstance(node, ast.Constant):
            return node.value if isinstance(node.value, str) else None
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            a, b = self.eval_str(node.left), self.eval_str(node.right)
            if a is None and b is None:
                return None
            return (a or "") + (b or "")
        if isinstance(node, ast.Name):
            return self.strings.get(node.id)
        if isinstance(node, ast.JoinedStr):
            out = []
            for v in node.values:
                if isinstance(v, ast.Constant):
                    out.append(v.value)
                elif isinstance(v, ast.FormattedValue):
                    inner = v.value
                    if isinstance(inner, ast.Name) and inner.id == "NWORDS":
                        modelo = self.strings.get("MODELO", "")
                        out.append(str(len(modelo.split())))
                    else:
                        s = self.eval_str(inner)
                        out.append(s if s is not None else "?")
                else:
                    out.append("?")
            return "".join(out)
        return None

    def eval_list(self, node):
        if isinstance(node, ast.List):
            return [self.eval_str(el) for el in node.elts]
        return None

    def collect_strings(self, tree):
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 \
                    and isinstance(node.targets[0], ast.Name):
                s = self.eval_str(node.value)
                if s is not None and len(s) > 20:
                    self.strings[node.targets[0].id] = s
            if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "quotes" \
                    and isinstance(node.value, ast.List):
                for el in node.value.elts:
                    if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                        q, cn, pg = (self.eval_str(x) for x in el.elts[:3])
                        self.quotes.append(f"> {q} — {cn} ({pg})")
            if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "chart" \
                    and isinstance(node.value, ast.List):
                rows = []
                for el in node.value.elts:
                    if isinstance(el, ast.Tuple) and len(el.elts) == 2:
                        lab = self.eval_str(el.elts[0])
                        val = el.elts[1].value if isinstance(el.elts[1], ast.Constant) else "?"
                        rows.append(f"- {lab}: {val}%")
                if rows:
                    self.lines.extend(["", "### Chart (practice data)"] + rows + [""])

    def emit_ex(self, level, typ, key, note, body, opts, instr):
        self.exn += 1
        self.reg.append((self.page, self.exn, key, note, typ))
        s = f"{self.exn}. [{level} · {typ}] {body or ''}"
        if opts:
            s += " " + " · ".join(o for o in opts if o)
        if key:
            s += f" — key: {key}"
        if note:
            s += f" ({note})"
        if instr:
            s += f" [{instr}]"
        self.lines.append(s)

    def walk(self, path):
        src = open(path, encoding="utf-8").read()
        tree = ast.parse(src)
        self.collect_strings(tree)

        def rec(n):
            if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) \
                    and getattr(n.value.func, "id", "") == "BSPage4":
                self.page += 1
                self.lines.extend(["", f"## Page {self.page}", ""])
                for ch in ast.iter_child_nodes(n):
                    rec(ch)
                return
            if isinstance(n, ast.Call):
                name = getattr(n.func, "attr", None) or getattr(n.func, "id", "")
                if name == "foot":
                    return
                if name == "para":
                    s = self.eval_str(n.args[0]) if n.args else None
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
                elif name == "bridge":
                    s = self.eval_str(n.args[0]) if n.args else None
                    if s and not is_furniture(s):
                        self.lines.append("*" + s + "*")
                        self.lines.append("")
                elif name == "band":
                    t = self.eval_str(n.args[0]) if n.args else None
                    sub = self.eval_str(n.args[2]) if len(n.args) > 2 else None
                    if t:
                        self.lines.extend(["", "### " + t + ((" — " + sub) if sub else ""), ""])
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
                elif name == "caption":
                    s = self.eval_str(n.args[4]) if len(n.args) > 4 else None
                    if s and not is_furniture(s):
                        self.lines.append("*" + s + "*")
                        self.lines.append("")
                elif name == "text":
                    s = self.eval_str(n.args[2]) if len(n.args) > 2 else None
                    size = n.args[3].value if len(n.args) > 3 and isinstance(n.args[3], ast.Constant) else 0
                    if s and size and size >= 24 and not is_furniture(s) and not s.strip().startswith("·"):
                        self.lines.extend(["", "### " + s, ""])
                        if self.quotes and ("ФРАЗЫ" in s or "Фразы" in s or "SENTENCES" in s.upper()):
                            self.lines.extend(self.quotes)
                            self.lines.append("")
                elif name == "ex":
                    a = [self.eval_str(x) for x in n.args[:5]]
                    opts = self.eval_list(n.args[5]) if len(n.args) > 5 else None
                    kw = {k.arg: self.eval_str(k.value) for k in n.keywords}
                    self.emit_ex(a[0], a[1], a[2], a[3], a[4], opts, kw.get("instr"))
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
                        ky = (keys[i] or "").strip()
                        ridx = ord(ky.lower()) - 97 if len(ky) == 1 and ky.isalpha() else i
                        rt = rights[ridx] if 0 <= ridx < len(rights) else "?"
                        nt = notes[i] if i < len(notes) else ""
                        self.reg.append((self.page, self.exn, ky, nt, a[1]))
                        self.lines.append(f"{self.exn}. {lf} — {rt} (key {ky} · {nt})")
                    self.lines.append("")
            for ch in ast.iter_child_nodes(n):
                rec(ch)
        rec(tree)

def main():
    build, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
    writing_type = sys.argv[4] if len(sys.argv) > 4 else "writing"
    ex = Exporter()
    ex.lines = ["# " + title, ""]
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(build, fname)
        if os.path.exists(path):
            ex.walk(path)
            ex.lines.append("")
    # reconstructed answer key, grouped by page
    ex.lines.extend(["", "## Answers", ""])
    by_page = {}
    for pg, n, key, note, typ in ex.reg:
        by_page.setdefault(pg, []).append((n, key, note, typ))
    for pg in sorted(by_page):
        ex.lines.append(f"### Page {pg}")
        for n, key, note, typ in by_page[pg]:
            if typ == writing_type:
                ex.lines.append(f"{n}. ✓ {note}")
            else:
                ex.lines.append(f"{n}. {key} — {note}")
        ex.lines.append("")
    text = "\n".join(ex.lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    open(out, "w", encoding="utf-8").write(text)
    print(f"wrote {out}: {ex.exn} exercises, {len(text)} bytes")

if __name__ == "__main__":
    main()
