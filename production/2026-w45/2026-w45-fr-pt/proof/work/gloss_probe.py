# -*- coding: utf-8 -*-
"""Proofreader-owned gloss recount (README #21口径, independent code):
parse content*.py with ast, track CURPAGE[0] assignments in file order,
count gloss() first-arg strings split on '·' itself (non-empty after strip,
trailing 。 stripped for emptiness test only), Nota/HINWEIS/译注 bridge
strings with the prefix stripped BEFORE splitting, and mots/mots4/mots5
list literal lengths. Read-only: never imports or executes build modules.
Also verifies every gloss item's French headword (text before first space
or '=') appears in the corresponding rendered SVG page text.
"""
import ast, os, re, sys, json
import xml.etree.ElementTree as ET

HOME = os.path.expanduser("~")
ROOT = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations")
CORE_BUILD = os.path.join(ROOT, "hidden_files/weekly-report-w45-fr-build")
ED_BUILD = os.path.join(ROOT, "hidden_files/weekly-report-w45-fr-pt-build")
ED_SVG = os.path.join(ROOT, "files/weekly-report-w45-fr-pt/svg")
CORE_SVG = os.path.join(ROOT, "files/weekly-report-w45-fr-core/svg")
PAGE_FILES = {1: "p1-une.svg", 2: "p2-vie.svg", 3: "p3-culture.svg", 4: "p4-sport.svg",
              5: "p5-jeunesse.svg", 6: "p6-politique.svg", 7: "p7-langue.svg", 8: "p8-exercices.svg"}

def count_file(path):
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    page = None
    res = {}
    items = {}
    for node in tree.body:
        seg = ast.get_source_segment(src, node) or ""
        m = re.search(r"CURPAGE\[0\] = (\d)", seg)
        if m:
            page = int(m.group(1))
        if page is None:
            continue
        res.setdefault(page, [0, 0, 0])
        items.setdefault(page, {"gloss": [], "nota": [], "mots": []})
        for sub in ast.walk(node):
            if not isinstance(sub, ast.Call):
                continue
            func = sub.func
            name = func.attr if isinstance(func, ast.Attribute) else ""
            if name == "gloss" and sub.args and isinstance(sub.args[0], ast.Constant):
                s = sub.args[0].value
                parts = [t.strip() for t in s.split("·") if t.strip().strip("。")]
                res[page][0] += len(parts)
                items[page]["gloss"].extend(parts)
            if name == "bridge" and sub.args and isinstance(sub.args[0], ast.Constant):
                s = sub.args[0].value
                if s.startswith(("译注", "HINWEIS", "Nota")):
                    s2 = re.sub(r"^(译注｜|HINWEIS · |Nota — )", "", s)
                    parts = [t for t in s2.split("·") if t.strip()]
                    res[page][1] += len(parts)
                    items[page]["nota"].extend(parts)
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in ("mots", "mots4", "mots5"):
                    if isinstance(node.value, ast.List):
                        res[page][2] += len(node.value.elts)
                        items[page]["mots"].extend(
                            [e.value for e in node.value.elts if isinstance(e, ast.Constant)])
    return res, items

def svg_text(path):
    tree = ET.parse(path)
    return re.sub(r"\s+", " ", " ".join(
        (el.text or "") for el in tree.getroot().iter() if el.tag.endswith("text")))

out = {}
for label, base, svgdir in [("core", CORE_BUILD, CORE_SVG), ("edition", ED_BUILD, ED_SVG)]:
    total = [0, 0, 0]
    per = {}
    all_items = {}
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        r, it = count_file(os.path.join(base, f))
        for pg, v in r.items():
            if pg not in per:
                per[pg] = [0, 0, 0]
                all_items[pg] = {"gloss": [], "nota": [], "mots": []}
            for i in range(3):
                per[pg][i] += v[i]
                total[i] += v[i]
            for k in all_items[pg]:
                all_items[pg][k].extend(it[pg][k])
    # survival check: gloss headwords in rendered page
    missing = {}
    for pg in sorted(per):
        jt = svg_text(os.path.join(svgdir, PAGE_FILES[pg]))
        miss = []
        for item in all_items[pg]["gloss"]:
            head = item.split("=")[0].strip().split(" ")[0] if "=" in item else item.split(" ")[0]
            # head may be a multi-word French phrase start; check first token
            tok = head.strip("«")
            if tok and tok not in jt:
                miss.append((item, tok))
        missing[pg] = miss
    out[label] = {"per_page": per, "total": total, "gloss_missing_in_render": missing}
    print(label, "per_page:", per)
    print(label, "TOTAL gloss/nota/mots:", total)
    print(label, "gloss items missing from render:", {k: v for k, v in missing.items() if v})
json.dump(out, open(os.path.join(ROOT, "hidden_files/w45/fr-pt-proof/work/gloss_probe.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
