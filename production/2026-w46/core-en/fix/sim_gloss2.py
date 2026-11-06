import sys, os, re
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-build"))
from svglib import wrap, text_w
def gloss_calls(path):
    t = open(path, encoding="utf-8").read()
    return re.findall(r'\.gloss\("([^"]*)"\)', t)
def show(ed, prefix, path):
    for s in gloss_calls(path):
        rendered = prefix + s
        lines = wrap(rendered, "sans", False, 20.5, 398)
        last = lines[-1]
        flag = " <-- CHECK" if len(last.strip()) <= 2 else ""
        print(f"{ed} {os.path.basename(path)} ({len(lines)}L) last={last!r} w={text_w(last,'sans',False,20.5):.1f}{flag}")
        for ln in lines: print(f"    [{text_w(ln,'sans',False,20.5):6.1f}] {ln!r}")
B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files")
for f in ["content12.py","content34.py","content56.py"]:
    show("FR", "Note | ", f"{B}/weekly-report-w46-en-fr-build/{f}")
for f in ["content12.py","content34.py","content56.py"]:
    show("ZH-TW", "譯注｜講解｜", f"{B}/weekly-report-w46-en-zh-tw-build/{f}")
for f in ["content12.py","content34.py","content56.py"]:
    show("KO", "해설 — ", f"{B}/weekly-report-w46-en-ko-build/{f}")
