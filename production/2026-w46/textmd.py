#!/usr/bin/env python3
"""Export <slug>.text.md from the source manuscript (.py content modules).

Reads the content*.py files with ast (no import — module-level code must
never execute) and emits display strings in source order, one paragraph per
string, under per-page headings. Code-only strings are skipped by rule.
Run from the build dir:  textmd.py <slug> <out-path>
"""
import ast, re, sys, os

SKIP_EXACT = {
    "sans", "serif", "middle", "end", "assets", "F", "type", "key", "note",
    "page", "VOL. 3 · 第 3 号", "P1-headline", "P1-week", "P1-quiz",
    "P2-feature", "P2-ex", "P3-feature", "P3-ex", "P4-feature", "P4-ex",
    "P5-feature", "P5-ex", "P6-feature", "P6-ex", "P7-a2", "P7-b1",
    "P7-b2", "P8-ex", "P8-keys", "P7 col3 ends", "P2 col3 ends",
    "P3 col3 ends", "P4 col3 ends", "P5 col3 ends", "P6 col3 ends",
    "P7 teaser ends", "P1 saved, exercises so far:",
    "P2 saved, exercises so far:", "P3 saved, exercises so far:",
    "P4 saved, exercises so far:", "P5 saved, exercises so far:",
    "P6 saved, exercises so far:", "P7 saved, exercises so far:",
    "P8 saved, exercises total:", "levels:", "level",
    "writing model chars:", "locker.jpg", "valley.jpg", "frost.jpg",
    "lanparty.jpg", "popcorn.jpg", "UnifrakturMaguntia",
}
SKIP_PREFIX = ("~/workspace", "#", "{OUT}", "P1 saved", "P7 saved")
CODE_RE = re.compile(r"[+\[\]]\s*[a-z_]+\[|d_,|m\[1\]|\{i\+1\}|\{e_\[|\{NCHARS\}|\{pg\}|\{n\}|\{num\}")

def is_display(s):
    s = s.strip()
    if not s or s in SKIP_EXACT:
        return False
    if s.startswith(SKIP_PREFIX):
        return False
    if CODE_RE.search(s):
        return False
    if "{" in s and "}" in s:  # format spec, not display text
        return False
    if re.fullmatch(r"[\d.,:;·—\-/ ]+", s):
        return False
    has_cjk = bool(re.search(r"[\u4e00-\u9fff]", s))
    # Cyrillic (RU), kana (JA), Hangul (KO) display strings carry no CJK/Latin run
    has_other_script = bool(re.search(r"[\u0400-\u04ff\u3040-\u30ff\uac00-\ud7a3]", s))
    has_latin_word = bool(re.search(r"[A-Za-z]{2,}", s))
    if has_cjk or has_other_script:
        return len(s) >= 2
    return has_latin_word and len(s) >= 4

def strings_in_order(path):
    tree = ast.parse(open(path, encoding="utf-8").read())
    out = []
    # collect constants NOT inside an f-string (JoinedStr parts are fragments)
    def visit(node, in_fstring):
        if isinstance(node, ast.JoinedStr):
            in_fstring = True
        if isinstance(node, ast.Constant) and isinstance(node.value, str) \
                and not in_fstring:
            out.append((node.lineno, node.value))
        for child in ast.iter_child_nodes(node):
            visit(child, in_fstring)
    visit(tree, False)
    out.sort(key=lambda t: t[0])
    return [v for _, v in out]

def main():
    slug, outpath = sys.argv[1], sys.argv[2]
    files = ["content12.py", "content34.py", "content56.py",
             "content7.py", "content8.py"]
    pages = [("content12.py", 1, "头版"), ("content12.py", 2, "生活"),
             ("content34.py", 3, "文化"), ("content34.py", 4, "体育"),
             ("content56.py", 5, "青年"), ("content56.py", 6, "深读"),
             ("content7.py", 7, "词语精讲"), ("content8.py", 8, "测验与答案")]
    # split each file's strings at its page boundary: content12/34/56 each
    # hold two pages; the boundary is the second OUT path literal.
    lines = [f"# {slug}", ""]
    for fname, pageno, title in pages:
        strs = strings_in_order(fname)
        # find boundary: index of the string that starts the page's svg path
        bounds = [i for i, s in enumerate(strs) if s.startswith("{OUT}/p")]
        if fname in ("content12.py", "content34.py", "content56.py"):
            if pageno % 2 == 1:
                chunk = strs[: bounds[0]] if bounds else strs
            else:
                chunk = strs[bounds[0]:] if bounds else []
        else:
            chunk = strs
        lines.append(f"## 第 {pageno} 版 · {title}")
        lines.append("")
        prev = None
        for s in chunk:
            s = s.strip()
            if not is_display(s):
                continue
            if s == prev:  # consecutive duplicate (box title + body)
                continue
            prev = s
            lines.append(s)
            lines.append("")
    open(outpath, "w", encoding="utf-8").write("\n".join(lines))
    print("wrote", outpath, len(lines), "lines")

if __name__ == "__main__":
    main()
