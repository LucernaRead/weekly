import re, sys, os, html
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
sys.path.insert(0, os.path.join(BASE, "tools"))
import importlib.util
spec = importlib.util.spec_from_file_location("oa", os.path.join(BASE, "tools/occlusion_audit.py"))
oa = importlib.util.module_from_spec(spec); spec.loader.exec_module(oa)
path = os.path.join(BASE, "files/weekly-report-w45-zh-tw-nl/svg/p7-lang.svg")
s = open(path, encoding="utf-8").read()
# letter box: rect at x=1451 (col3) - list all rects there
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', s):
    x, y, w, h = map(float, m.groups())
    if abs(x - 1451) < 1:
        print(f"RECT x={x} y={y} w={w} h={h} bottom={y+h:.2f} expanded={y+h+0.7:.2f}")
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')
for m in TEXT_RE.finditer(s):
    t = html.unescape(m.group(4))
    if "Stuur je brief in" in t:
        x, y, attrs = float(m.group(1)), float(m.group(2)), m.group(3)
        fm = re.search(r'font-family="([^"]+)"', attrs); sm = re.search(r'font-size="([\d.]+)"', attrs)
        bold = 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs
        anchor = "middle" if 'text-anchor="middle"' in attrs else ("end" if 'text-anchor="end"' in attrs else "start")
        box = oa.ink_box(t, fm.group(1) if fm else "", float(sm.group(1)) if sm else 20.0, bold, x, y, anchor, 0.0)
        print(f"LAST LINE node x={x} y={y} text={t!r}")
        print(f"  ink box={box} ink_bottom={box[3]:.2f} ink_center_y={(box[1]+box[3])/2:.2f}")
