# -*- coding: utf-8 -*-
"""Render W45 FR x ZH-TW: cards (PNG @1950), print PDF, web PDF.

Run with tools/venv/bin/python (Python 3.12.3, Pillow 13.0.0, cairosvg).
Web PDF recipe (FR-family W45 convention, cf. fr-nl KIT §10): open the
8 delivered cards as RGB and PIL-save as PDF directly (no explicit
quality -> Pillow default, empirically q75; verified by stream
byte-compare in verify_webpdf.py). The web PDF is generated fresh
from THIS edition's cards, never from the core's web PDF.
"""
import glob
import os

import cairosvg
from PIL import Image
from pypdf import PdfWriter

ED = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-zh-tw-proof/work/webregen"
SVG = os.path.join(ED, "svg")
CARDS = os.path.join(ED, "cards")
os.makedirs(CARDS, exist_ok=True)
pages = sorted(glob.glob(os.path.join(SVG, "*.svg")))
assert len(pages) == 8, pages
print("pages:", [os.path.basename(p) for p in pages])

for p in pages:
    out = os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))
    cairosvg.svg2png(url=p, write_to=out, output_width=1950)
    im = Image.open(out)
    assert im.size == (1950, 2700), (out, im.size)
    print("card:", out, os.path.getsize(out), im.size)

writer = PdfWriter()
for p in pages:
    pdf_bytes = cairosvg.svg2pdf(url=p)
    tmp = p.replace(".svg", ".tmp.pdf")
    with open(tmp, "wb") as f:
        f.write(pdf_bytes)
    writer.append(tmp)
    os.remove(tmp)
print_pdf = os.path.join(ED, "Le-Lucerna-VOL3-ZHTW.pdf")
with open(print_pdf, "wb") as f:
    writer.write(f)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))

imgs = []
for p in pages:
    png = os.path.join(CARDS, os.path.basename(p).replace(".svg", ".png"))
    imgs.append(Image.open(png).convert("RGB"))
web_pdf = os.path.join(ED, "Le-Lucerna-VOL3-ZHTW-web.pdf")
imgs[0].save(web_pdf, "PDF", save_all=True, append_images=imgs[1:],
             resolution=150.0, title="Le-Lucerna-VOL3-ZHTW-web")
print("web PDF:", web_pdf, os.path.getsize(web_pdf))
