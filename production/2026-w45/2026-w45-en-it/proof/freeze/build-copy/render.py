# -*- coding: utf-8 -*-
"""Render W45 EN x DE: cards (PNG @1950), print PDF, web PDF (JPEG q85 @1400).
Same recipe as the W45 EN core render, pointed at this edition only.
Run with tools/venv/bin/python (system python3 has no cairosvg)."""
import os, glob
from PIL import Image
import cairosvg
from pypdf import PdfWriter

ED = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-it-proof/freeze")
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
print_pdf = os.path.join(ED, "The-Lucerna-VOL2-IT.pdf")
with open(print_pdf, "wb") as f:
    writer.write(f)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))

imgs = []
for p in pages:
    png = os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))
    im = Image.open(png).convert("RGB").resize((1400, 1938), Image.LANCZOS)
    imgs.append(im)
web_pdf = os.path.join(ED, "The-Lucerna-VOL2-IT-web.pdf")
imgs[0].save(web_pdf, "PDF", save_all=True, append_images=imgs[1:], quality=85)
print("web PDF:", web_pdf, os.path.getsize(web_pdf))
