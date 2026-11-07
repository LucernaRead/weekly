# -*- coding: utf-8 -*-
"""Render cards + print PDF + web PDF for the EN x FR edition.
Run ONLY with tools/venv/bin/python (system python3 has no cairosvg)."""
import glob, os
import cairosvg
from pypdf import PdfWriter
from PIL import Image

base = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-fr")
w = PdfWriter()
for f in sorted(glob.glob(base + "/svg/*.svg")):
    cairosvg.svg2png(url=f, write_to=f.replace("/svg/", "/cards/").replace(".svg", ".png"), output_width=1950)
    cairosvg.svg2pdf(url=f, write_to="/tmp/en45frpage.pdf")
    w.append("/tmp/en45frpage.pdf")
w.write(open(base + "/The-Lucerna-VOL2-FR-print.pdf", "wb"))
imgs = [Image.open(f).convert("RGB") for f in sorted(glob.glob(base + "/cards/*.png"))]
for im in imgs:
    im.thumbnail((1400, 1938))
imgs[0].save(base + "/The-Lucerna-VOL2-FR-web.pdf", save_all=True, append_images=imgs[1:], quality=85)
print("render done")
