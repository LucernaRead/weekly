# -*- coding: utf-8 -*-
"""Render the ZH-CN weekly VOL.3: svg/ -> cards/ PNG (1950px) -> print PDF (cairosvg+pypdf).
Web PDF is built separately with tools/webpdf.py (text layer required)."""
import os, io, glob
import cairosvg
from pypdf import PdfWriter, PdfReader

BASE = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/zh-cn-fix-keys/gates/freeze-baseline")
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

writer = PdfWriter()
for s in SVGS:
    data = cairosvg.svg2pdf(url=s)
    reader = PdfReader(io.BytesIO(data))
    for pg in reader.pages:
        writer.add_page(pg)
print_pdf = os.path.join(BASE, "Lucerna-VOL3.pdf")
with open(print_pdf, "wb") as fh:
    writer.write(fh)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))
