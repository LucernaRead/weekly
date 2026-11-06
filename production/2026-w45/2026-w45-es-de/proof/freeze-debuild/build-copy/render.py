# -*- coding: utf-8 -*-
"""Render the ES core edition: svg/ -> cards/ PNG (1950x2700) -> print PDF -> web PDF.
Web PDF: pages downscaled to 1400px wide, JPEG q85 (finalized core recipe)."""
import os, io, glob
import cairosvg
from PIL import Image
from pypdf import PdfWriter, PdfReader

BASE = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-de-proof/freeze-debuild")
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
print_path = os.path.join(BASE, "La-Lucerna-VOL2.pdf")
with open(print_path, "wb") as fh:
    w.write(fh)
print("print PDF:", print_path, os.path.getsize(print_path))

imgs = []
for s in svgs:
    name = os.path.splitext(os.path.basename(s))[0]
    im = Image.open(os.path.join(CARDS, name + ".png")).convert("RGB")
    im = im.resize((1400, int(1400 * im.height / im.width)), Image.LANCZOS)
    imgs.append(im)
web_path = os.path.join(BASE, "La-Lucerna-VOL2-web.pdf")
imgs[0].save(web_path, save_all=True, append_images=imgs[1:], quality=85)
print("web PDF:", web_path, os.path.getsize(web_path))
