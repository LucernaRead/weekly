# -*- coding: utf-8 -*-
"""Export <slug>.text.md for every W46 DE edition from the edition's own
build-dir sources (AST string literals, in source order) — never from PDF/SVG.

Covers: Flow page tags, p.text/para/head/bridge/title/byline, box titles +
bodies, ex/match_set exercises, reg_ex registry keys (P8 answers), captions,
band/strip/shead furniture. f-strings with interpolated values are skipped
(their static furniture is covered by the literal lines); P8 answer lines
come from the reg_ex calls.
"""
import ast, os, re

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HID = os.path.join(GOAL, "hidden_files")
EDITIONS = [
    ("zh-cn", "weekly-report-w46-de-zh-cn-build", "2026-w46-de-zh-cn"),
]


def strval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                parts.append(str(v.value))
            elif isinstance(v, ast.FormattedValue):
                parts.append("N")
        joined = "".join(parts)
        # Only gap paragraphs (cloze/dialog "___") survive as text;
        # furniture f-strings (page numbers, separators) are skipped.
        return joined if "___" in joined else None
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        a, b = strval(node.left), strval(node.right)
        if a is not None and b is not None:
            return a + b
    return None


def listvals(node):
    out = []
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        for e in node.elts:
            v = strval(e)
            if v is not None:
                out.append(v)
            else:
                out.extend(listvals(e))
    return out


def walk_file(path, out, init):
    page = init
    tree = ast.parse(open(path, encoding="utf-8").read())

    def emit(txt):
        t = txt.strip()
        if len(t) > 1:
            out.append((page, t))

    def visit(node):
        nonlocal page
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            names = [t.id for t in targets if isinstance(t, ast.Name)]
            if any("def" in n for n in names):
                for v in listvals(node.value):
                    if keep(v):
                        emit(v)
            for ch in ast.iter_child_nodes(node):
                visit(ch)
            return
        if isinstance(node, ast.For):
            for sub in ast.walk(node.iter):
                if isinstance(sub, (ast.List, ast.Tuple)):
                    for v in listvals(sub):
                        if keep(v):
                            emit(v)
            for ch in ast.iter_child_nodes(node):
                visit(ch)
            return
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else "")
            args = node.args
            if name == "Flow":
                for kw in node.keywords:
                    if kw.arg == "tag":
                        v = strval(kw.value)
                        if v:
                            m = re.search(r"P([1-8])\b", v)
                            if m:
                                page = "P" + m.group(1)
            elif name == "text":
                if len(args) >= 3:
                    v = strval(args[2])
                    if v:
                        emit(v)
            elif name == "para":
                # Flow.para(s, ...) vs Page.para(x, y, s, ...)
                recv = fn.value.id if isinstance(fn, ast.Attribute) and isinstance(fn.value, ast.Name) else ""
                idx = 2 if recv == "p" else 0
                if len(args) > idx:
                    v = strval(args[idx])
                    if v:
                        emit(v)
            elif name in ("head", "bridge", "title", "byline", "gloss"):
                if args:
                    v = strval(args[0])
                    if v:
                        emit(v)
            elif name == "box":
                if args:
                    v = strval(args[0])
                    if v:
                        emit(v)
                if len(args) >= 2:
                    # paras: list of strings, or (text, size, kind, ...) rows:
                    # emit only the text (first element) of each row.
                    if isinstance(args[1], (ast.List, ast.Tuple)):
                        for el in args[1].elts:
                            if isinstance(el, (ast.List, ast.Tuple)) and el.elts:
                                v = strval(el.elts[0])
                            else:
                                v = strval(el)
                            if v:
                                emit(v)
            elif name == "band":
                for a in args:
                    v = strval(a)
                    if v:
                        emit(v)
            elif name == "strip":
                # strip(y, h, text, ...) -> text is args[2]
                if len(args) >= 3:
                    v = strval(args[2])
                    if v:
                        emit(v)
            elif name == "shead":
                if len(args) >= 3:
                    v = strval(args[2])
                    if v:
                        emit(v)
            elif name == "caption":
                # caption(p, x, y, w, fr, credit="") -> fr is args[4]
                if len(args) >= 5:
                    v = strval(args[4])
                    if v:
                        emit(v)
                for kw in node.keywords:
                    if kw.arg == "credit":
                        v = strval(kw.value)
                        if v:
                            emit("Bildnachweis: " + v)
            elif name == "ex":
                # ex(level, typ, key, note, body, opts=None, instr=None)
                for i in (2, 3, 4):
                    if len(args) > i:
                        v = strval(args[i])
                        if v:
                            emit(v)
                if len(args) > 5:
                    for v in listvals(args[5]):
                        emit(v)
                for kw in node.keywords:
                    if kw.arg == "instr":
                        v = strval(kw.value)
                        if v:
                            emit(v)
            elif name == "match_set":
                for a in args[2:6]:
                    for v in listvals(a):
                        emit(v)
                for kw in node.keywords:
                    if kw.arg == "instr":
                        v = strval(kw.value)
                        if v:
                            emit(v)
            elif name == "reg_ex":
                # reg_ex(level, typ, key, note="") -> P8 answer key line
                vals = [strval(a) for a in args[:4]]
                vals = [v for v in vals if v]
                if len(vals) >= 3:
                    key, note = vals[2], vals[3] if len(vals) > 3 else ""
                    emit(f"{key} ({note})" if note else key)
        for ch in ast.iter_child_nodes(node):
            visit(ch)

    visit(tree)


def keep(s):
    s2 = s.strip()
    if not s2 or len(s2) < 2:
        return False
    if s2 in DROP_EXACT:
        return False
    if DROP_RE.match(s2):
        return False
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", s2):
        return False
    if re.fullmatch(r"[0-9][0-9.,:;/% -]*", s2):
        return False
    return True


DROP_EXACT = {"sans", "serif", "middle", "start", "end", "left", "right",
              "C12", "C34", "C56", "C7", "C8", "L1", "L2", "L3",
              "A", "B", "C", "D", "E", "F", "G", "H", "A2", "B1", "B2"}
DROP_RE = re.compile(r"^(~/|/|\.|[A-Za-z0-9_./-]+\.(py|svg|pdf|png|jpg|ttf|otf|woff2?))$")


def is_head(s):
    t = s.strip()
    if "·" in t and len(t) <= 64 and t.split("·")[0].strip().isupper():
        return True
    if re.fullmatch(r"[A-ZÄÖÜ0-9 .\-–—&/()]+", t) and len(t) <= 48 and any(c.isalpha() for c in t):
        return True
    return False


GOLDEN = [
    "Die Bundesliga pausiert — aber die Nationalmannschaft spielt.",
    "Um 11.11 Uhr beginnt in Köln die neue Karnevalssession.",
    "Sein Gedenktag ist der 11. November.",
    "Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut.",
    "Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.",
    "Das Spiel ist ausverkauft, RTL überträgt live.",
    "Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.",
    "Am Sonntag ist es still im Land.",
]

for ed, build, slug in EDITIONS:
    bdir = os.path.join(HID, build)
    items = []
    for f, pg in [("content12.py", "P1"), ("content34.py", "P3"),
                  ("content56.py", "P5"), ("content7.py", "P7"),
                  ("content8.py", "P8")]:
        walk_file(os.path.join(bdir, f), items, pg)
    lines = [f"# Die Lucerna · VOL.3 — 9. bis 15. November 2026",
             "",
             f"Edition `{slug}` — German text with reader-language explanations. "
             "Exported from the production source manuscript (build-dir sources), "
             "in reading order: headlines, article paragraphs, boxes, exercises, answers.",
             ""]
    cur = None
    prev = None
    for page, txt in items:
        if page != cur:
            lines.append(f"## Seite {page[1]}")
            lines.append("")
            cur = page
        if txt == prev:
            continue
        prev = txt
        lines.append(f"### {txt}" if is_head(txt) else txt)
        lines.append("")
    eddir = os.path.join(GOAL, "files", f"weekly-report-w46-de-{ed}")
    out = os.path.join(eddir, f"{slug}.text.md")
    open(out, "w", encoding="utf-8").write("\n".join(lines))
    body = "\n".join(lines)
    gold = sum(1 for g in GOLDEN if g in body) if ed in ("core", "zh-cn") else "-"
    print(slug, "items:", len(items), "bytes:", os.path.getsize(out), "golden:", gold)
