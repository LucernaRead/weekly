# -*- coding: utf-8 -*-
"""Render the ES W46 core edition: svg/ -> cards/ PNG (1950x2700) -> print PDF
-> web PDF via tools/webpdf.py (vector text layer, SOP appendix 4).
"""
import os, io, glob, subprocess, sys
import cairosvg
from pypdf import PdfWriter, PdfReader

BASE = os.path.dirname(os.path.abspath(__file__))
SVG_DIR = os.path.join(BASE, "svg")
CARDS = os.path.join(BASE, "cards")
os.makedirs(CARDS, exist_ok=True)

svgs = sorted(glob.glob(os.path.join(SVG_DIR, "*.svg")))
assert len(svgs) == 8, svgs

page_pdfs = []
for s in svgs:
    name = os.path.splitext(os.path.basename(s))[0]
    png_path = os.path.join(CARDS, name + ".png")
    cairosvg.svg2png(url=s, write_to=png_path, output_width=1950, output_height=2700)
    page_pdfs.append(cairosvg.svg2pdf(url=s))
    print("rendered", name)

w = PdfWriter()
for b in page_pdfs:
    r = PdfReader(io.BytesIO(b))
    for pg in r.pages:
        w.add_page(pg)
print_path = os.path.join(BASE, "La-Lucerna-VOL3-es-de.pdf")
with open(print_path, "wb") as fh:
    w.write(fh)
print("print PDF:", print_path, os.path.getsize(print_path))

web_path = os.path.join(BASE, "La-Lucerna-VOL3-es-de-web.pdf")
tools = os.path.expanduser("~/workspace/weekly-git/tools")
r = subprocess.run([sys.executable, os.path.join(tools, "webpdf.py"), SVG_DIR, web_path],
                   capture_output=True, text=True)
print(r.stdout)
print(r.stderr, file=sys.stderr)
if r.returncode != 0:
    raise SystemExit(f"webpdf.py failed: {r.returncode}")
print("web PDF:", web_path, os.path.getsize(web_path))
