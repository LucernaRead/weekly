#!/usr/bin/env python3
"""Coverage check: every English-bearing display string in the CORE content
modules must be covered by a fan-out mapping (as a full key or via a
fragment key contained in it), or be on the FROZEN list. F-string parts
are checked from raw source text instead (they never appear as constants).
"""
import ast, json, re, sys, os

CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-zhcn-build")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py",
         "content8.py", "bslib4.py"]
EN_RE = re.compile(r"[A-Za-z][a-z]{2,}")  # English word; pinyin never matches
FROZEN = {
    "Photo: Map hobby — CC0 (Wikimedia Commons)",
    "Photo: Paul Gilmore — CC0 (Wikimedia Commons)",
    "Photo: Gerda Arendt — CC0 (Wikimedia Commons)",
    "Photo: Syced — CC0 (Wikimedia Commons)",
    "Photo: Based5290 — Public domain (Wikimedia Commons)",
    "VOL. 3 · 第 3 号",
    "简体中文版 · VOL.3 · 双11 · 消防日 · S16",
    "双11×S16",
    "S16",
    "A2→B1",
    "A2→B2",
    "Lucerna",
    "这是《Lucerna》简体中文版第3号。每周,我们用简单的中文,带你读真正的中国新闻。欢迎你!",
}
SKIP = {"sans", "serif", "middle", "end", "UnifrakturMaguntia",
        "locker.jpg", "valley.jpg", "frost.jpg", "lanparty.jpg",
        "popcorn.jpg", "P1-headline", "P1-week", "P1-quiz", "P2-feature",
        "P2-ex", "P3-feature", "P3-ex", "P4-feature", "P4-ex",
        "P5-feature", "P5-ex", "P6-feature", "P6-ex", "P7-a2", "P7-b1",
        "P7-b2", "P8-ex", "P8-keys", "P1 saved, exercises so far:",
        "P2 saved, exercises so far:", "P3 saved, exercises so far:",
        "P4 saved, exercises so far:", "P5 saved, exercises so far:",
        "P6 saved, exercises so far:", "P7 saved, exercises so far:",
        "P8 saved, exercises total:", "levels:", "level",
        "writing model chars:", "P2 col3 ends", "P3 col3 ends",
        "P4 col3 ends", "P5 col3 ends", "P6 col3 ends",
        "P7 col3 ends", "P7 teaser ends",
        "V4 broadsheet library: 1950x2700, 4 columns, exercise registry + flow layout.",
        "assets", "page", "type", "key", "note", ".png", "png", "jpeg",
        "xMidYMid slice", "none",
        "Flows text blocks down a column, then to the next. Heights pre-measured via wrap().",
        "paras: list of (text, kind, bold, fill, size, lh). Height pre-measured.",
        "lefts numbered (each registered), rights lettered a/b/c... printed once."}

def strings_in_order(path):
    tree = ast.parse(open(path, encoding="utf-8").read())
    out = []
    def visit(node, inf):
        if isinstance(node, ast.JoinedStr):
            inf = True
        if isinstance(node, ast.Constant) and isinstance(node.value, str) \
                and not inf:
            out.append((node.lineno, node.value))
        for c in ast.iter_child_nodes(node):
            visit(c, inf)
    visit(tree, False)
    out.sort(key=lambda t: t[0])
    return [v for _, v in out]

def main():
    mapping = json.load(open(sys.argv[1], encoding="utf-8"))
    keys = list(mapping.keys())
    stripped_keys = {k.strip() for k in keys}
    uncovered = []
    all_raw = ""
    for fname in FILES:
        all_raw += open(os.path.join(CORE, fname), encoding="utf-8").read()
    for k in keys:
        if "{" in k:
            for seg in re.split(r"\{[^}]+\}", k):
                if seg and seg not in all_raw:
                    uncovered.append(("ALL", f"TEMPLATE SEGMENT MISSING: {seg!r}"))
    for fname in FILES:
        raw = open(os.path.join(CORE, fname), encoding="utf-8").read()
        for s in strings_in_order(os.path.join(CORE, fname)):
            s = s.strip()
            if not s or s in SKIP or s in FROZEN:
                continue
            if s.startswith("~/workspace") or s.startswith("#") or \
                    s.startswith("{OUT}"):
                continue
            if not EN_RE.search(s):
                continue
            if s in mapping or s.strip() in stripped_keys:
                continue
            if any(k in s for k in keys if len(k) >= 4):
                continue
            uncovered.append((fname, s))
    if uncovered:
        print(f"UNCOVERED: {len(uncovered)}")
        for f, s in uncovered:
            print(f, repr(s))
        sys.exit(1)
    print("coverage OK:", len(keys), "keys cover all English display strings")

if __name__ == "__main__":
    main()
