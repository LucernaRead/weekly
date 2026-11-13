# -*- coding: utf-8 -*-
"""Export the CORE (zh-cn) .text.md from build sources via the same AST
exporter used for the 10 fan-outs (hidden_files/w46/it-finish/export_it_textmd.py).
Never from PDF/SVG. Run from it-fix/ with the tools venv python."""
import os, sys
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/it-finish"))
import export_it_textmd as E

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HID = os.path.join(GOAL, "hidden_files")
PAGES = E.PAGES
FILES = E.FILES

bdir = os.path.join(HID, "weekly-report-w46-it-build")
ex = E.Exporter()
ex.gloss_prefix_from(bdir)
for f in FILES:
    ex.walk_file(os.path.join(bdir, f))
assert ex.exn == 150, ex.exn
lines = ex.lines
ded = []
for item in lines:
    if not ded or ded[-1][1] != item[1]:
        ded.append(item)
slug = "2026-w46-it-zh-cn"
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
eddir = os.path.join(GOAL, "files", "weekly-report-w46-it-core")
out = os.path.join(eddir, f"{slug}.text.md")
text = "\n".join(out_lines).strip() + "\n"
open(out, "w", encoding="utf-8").write(text)
print(slug, "exercises:", ex.exn, "bytes:", len(text.encode("utf-8")), "lines:", len(out_lines))
