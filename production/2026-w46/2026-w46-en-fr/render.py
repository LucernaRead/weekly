# -*- coding: utf-8 -*-
"""Render W46 EN core: cards (PNG @1950), print PDF. Web PDF via tools/webpdf.py."""
import os, glob
from PIL import Image
import cairosvg
from pypdf import PdfWriter
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-en-fr")
SVG = os.path.join(ED, "svg"); CARDS = os.path.join(ED, "cards")
os.makedirs(CARDS, exist_ok=True)
pages = sorted(glob.glob(os.path.join(SVG, "*.svg")))
assert len(pages) == 8, pages
for p in pages:
    out = os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))
    cairosvg.svg2png(url=p, write_to=out, output_width=1950)
    print("card:", out, os.path.getsize(out))
writer = PdfWriter()
for p in pages:
    pdf_bytes = cairosvg.svg2pdf(url=p)
    tmp = p.replace(".svg", ".tmp.pdf")
    with open(tmp, "wb") as f: f.write(pdf_bytes)
    writer.append(tmp); os.remove(tmp)
pp = os.path.join(ED, "The-Lucerna-VOL3.pdf")
with open(pp, "wb") as f: writer.write(f)
print("print PDF:", pp, os.path.getsize(pp))
