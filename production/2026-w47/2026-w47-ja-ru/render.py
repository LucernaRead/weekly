# -*- coding: utf-8 -*-
"""Render the JA weekly W46: svg/ -> cards/ PNG (1950px) -> print PDF
(cairosvg+pypdf). Web PDF is built separately with tools/webpdf.py
(text-layer web PDF per SOP appendix 4); this script never makes an
image-only web PDF."""
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
print_pdf = os.path.join(BASE, "Lucerna-VOL4-JA-RU.pdf")
with open(print_pdf, "wb") as fh:
    writer.write(fh)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))
