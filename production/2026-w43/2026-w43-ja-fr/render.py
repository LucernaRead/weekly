# -*- coding: utf-8 -*-
"""Render the JA weekly: svg/ -> cards/ PNG (1950px) -> print PDF (cairosvg+pypdf)
-> web PDF (JPEG q85 @1400px, < 10 MB for Discord)."""
import os, io, glob
import cairosvg
from PIL import Image
from pypdf import PdfWriter, PdfReader

BASE = os.path.dirname(os.path.abspath(__file__))
SVGS = sorted(glob.glob(os.path.join(BASE, "svg", "*.svg")))
assert len(SVGS) == 8, SVGS

os.makedirs(os.path.join(BASE, "cards"), exist_ok=True)
png_paths = []
for s in SVGS:
    name = os.path.splitext(os.path.basename(s))[0] + ".png"
    out = os.path.join(BASE, "cards", name)
    cairosvg.svg2png(url=s, write_to=out, output_width=1950, output_height=2700)
    png_paths.append(out)
    print("card:", name)

# print PDF from per-page PDFs
writer = PdfWriter()
for s in SVGS:
    data = cairosvg.svg2pdf(url=s)
    reader = PdfReader(io.BytesIO(data))
    for pg in reader.pages:
        writer.add_page(pg)
print_pdf = os.path.join(BASE, "Lucerna-VOL1-FR.pdf")
with open(print_pdf, "wb") as fh:
    writer.write(fh)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))

# web PDF via tools/webpdf.py (vector text layer, SOP appendix 4)
import subprocess, sys
web_pdf = os.path.join(BASE, "Lucerna-VOL1-FR-web.pdf")
tools = os.path.expanduser("~/workspace/weekly-git/tools")
r = subprocess.run([sys.executable, os.path.join(tools, "webpdf.py"), os.path.join(BASE, "svg"), web_pdf],
                   capture_output=True, text=True)
print(r.stdout)
print(r.stderr, file=sys.stderr)
if r.returncode != 0:
    raise SystemExit(f"webpdf.py failed: {r.returncode}")
print("web PDF:", web_pdf, os.path.getsize(web_pdf))
