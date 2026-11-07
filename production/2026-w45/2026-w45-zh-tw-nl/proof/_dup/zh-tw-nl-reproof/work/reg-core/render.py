# -*- coding: utf-8 -*-
"""Render the ZH-TW weekly: svg/ -> cards/ PNG (1950px) -> print PDF (cairosvg+pypdf)
-> web PDF (JPEG q85 @1400px, < 10 MB for Discord)."""
import os, io, glob
import cairosvg
from PIL import Image
from pypdf import PdfWriter, PdfReader

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-nl-reproof/work/reg-core-out")
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
print_pdf = os.path.join(BASE, "Lucerna-VOL2.pdf")
with open(print_pdf, "wb") as fh:
    writer.write(fh)
print("print PDF:", print_pdf, os.path.getsize(print_pdf))

# web PDF: JPEG pages at 1400px wide, q85
imgs = []
for pp in png_paths:
    im = Image.open(pp).convert("RGB")
    w, h = im.size
    im = im.resize((1400, int(h * 1400 / w)), Image.LANCZOS)
    imgs.append(im)
web_pdf = os.path.join(BASE, "Lucerna-VOL2-web.pdf")
imgs[0].save(web_pdf, save_all=True, append_images=imgs[1:], quality=85)
print("web PDF:", web_pdf, os.path.getsize(web_pdf))
