# -*- coding: utf-8 -*-
"""Render W45 FR x ES: cards (PNG @1950), print PDF, web PDF.
Same recipe as the W45 FR core render (cards full-size, web PDF from
JPEG quality 72), pointed at this edition only.
Run with tools/venv/bin/python (system python3 has no cairosvg)."""
import os, glob
from PIL import Image
import cairosvg
from pypdf import PdfWriter

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-es")
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
print_pdf = os.path.join(ED, "Le-Lucerna-VOL3-ES.pdf")
with open(print_pdf, "wb") as f:
    writer.write(f)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))

imgs = []
tmp_jpg = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".webpage.jpg")
for p in pages:
    im = Image.open(os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))).convert("RGB")
    im.save(tmp_jpg, "JPEG", optimize=True)
    imgs.append(Image.open(tmp_jpg).copy())
os.remove(tmp_jpg)
web_pdf = os.path.join(ED, "Le-Lucerna-VOL3-ES-web.pdf")
imgs[0].save(web_pdf, save_all=True, append_images=imgs[1:], resolution=150.0)
print("web PDF:", web_pdf, os.path.getsize(web_pdf))
