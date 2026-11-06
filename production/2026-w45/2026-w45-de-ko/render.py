# -*- coding: utf-8 -*-
"""Render W45 DE x KO: cards (PNG @1950), print PDF, web PDF (JPEG q85 @1400).
Mirrors the W43 reproduction recipe (WEEKLY-KIT.md §Reproduction)."""
import os, glob
from PIL import Image
import cairosvg
from pypdf import PdfWriter

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-ko")
SVG = os.path.join(ED, "svg")
CARDS = os.path.join(ED, "cards")
os.makedirs(CARDS, exist_ok=True)
pages = sorted(glob.glob(os.path.join(SVG, "*.svg")))
assert len(pages) == 8, pages
names = [os.path.basename(p) for p in pages]
print("pages:", names)

# cards
for p in pages:
    out = os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))
    cairosvg.svg2png(url=p, write_to=out, output_width=1950)
    print("card:", out, os.path.getsize(out))

# print PDF via svg2pdf + merge
writer = PdfWriter()
for p in pages:
    pdf_bytes = cairosvg.svg2pdf(url=p)
    tmp = p.replace(".svg", ".tmp.pdf")
    with open(tmp, "wb") as f:
        f.write(pdf_bytes)
    writer.append(tmp)
    os.remove(tmp)
print_pdf = os.path.join(ED, "Die-Lucerna-VOL2-KO.pdf")
with open(print_pdf, "wb") as f:
    writer.write(f)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))

# web PDF: JPEG q85 @1400px, PIL multi-page PDF (JPEG encoding preserved)
imgs = []
for p in pages:
    png = os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))
    im = Image.open(png).convert("RGB").resize((1400, 1938), Image.LANCZOS)
    imgs.append(im)
web_pdf = os.path.join(ED, "Die-Lucerna-VOL2-KO-web.pdf")
imgs[0].save(web_pdf, "PDF", save_all=True, append_images=imgs[1:], quality=85)
print("web PDF:", web_pdf, os.path.getsize(web_pdf))
