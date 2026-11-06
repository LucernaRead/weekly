# -*- coding: utf-8 -*-
"""Render W46 DE core: cards (PNG @1950), print PDF (CairoSVG + pypdf),
web PDF via tools/webpdf.py (vector text layer, NOT PIL JPEG拼合)."""
import os, glob, subprocess, sys
import cairosvg
from pypdf import PdfWriter

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w46-de-core")
SVG = os.path.join(ED, "svg")
CARDS = os.path.join(ED, "cards")
os.makedirs(CARDS, exist_ok=True)
pages = sorted(glob.glob(os.path.join(SVG, "*.svg")))
assert len(pages) == 8, pages
print("pages:", [os.path.basename(p) for p in pages])

for p in pages:
    out = os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))
    cairosvg.svg2png(url=p, write_to=out, output_width=1950)
    print("card:", out, os.path.getsize(out))

writer = PdfWriter()
for p in pages:
    pdf_bytes = cairosvg.svg2pdf(url=p)
    tmp = p.replace(".svg", ".tmp.pdf")
    with open(tmp, "wb") as f:
        f.write(pdf_bytes)
    writer.append(tmp)
    os.remove(tmp)
print_pdf = os.path.join(ED, "Die-Lucerna-VOL3.pdf")
with open(print_pdf, "wb") as f:
    writer.write(f)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))

web_pdf = os.path.join(ED, "Die-Lucerna-VOL3-web.pdf")
r = subprocess.run([os.path.join(GOAL, "tools/venv/bin/python"),
                    os.path.join(GOAL, "tools/webpdf.py"), SVG, web_pdf],
                   capture_output=True, text=True)
print(r.stdout)
print(r.stderr, file=sys.stderr)
print("webpdf exit:", r.returncode)
assert r.returncode == 0, "webpdf.py failed"
print("web PDF:", web_pdf, os.path.getsize(web_pdf))
assert os.path.getsize(web_pdf) < 7 * 1024 * 1024, "web PDF >= 7MB"
