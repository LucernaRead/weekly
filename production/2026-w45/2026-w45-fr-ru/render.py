# -*- coding: utf-8 -*-
"""FR x RU W45 render: single-process SVG driver is separate (import
content12, content34, content56, content7, content8 in one process);
this script renders cards + print PDF + web PDF from the edition SVGs.
Run with tools/venv/bin/python (cairosvg + Pillow + pypdf).
Web PDF: each card -> JPEG quality=75, optimize=True, then packed as
PDF (Pillow default quality is 75; see KIT for the q72/q75 byte test).
"""
import glob, os, sys
import cairosvg
from pypdf import PdfWriter
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru")
QUALITY = int(os.environ.get("WEB_QUALITY", "75"))

svgs = sorted(glob.glob(os.path.join(ED, "svg", "*.svg")))
assert len(svgs) == 8, svgs
w = PdfWriter()
for f in svgs:
    png = f.replace("/svg/", "/cards/").replace(".svg", ".png")
    cairosvg.svg2png(url=f, write_to=png, output_width=1950)
    im = Image.open(png)
    assert im.size == (1950, 2700), (png, im.size)
    cairosvg.svg2pdf(url=f, write_to="/tmp/fr-ru-page.pdf")
    w.append("/tmp/fr-ru-page.pdf")
with open(os.path.join(ED, "Le-Lucerna-VOL3-RU.pdf"), "wb") as fh:
    w.write(fh)
imgs = []
# FIX 2026-10-28 (web-PDF noise root cause): NEVER reuse one temp JPEG
# path across pages. Image.open() is lazy: all 8 handles pointed at the
# same path while each iteration overwrote it, so Pillow's PDF writer
# embedded byte-salad for pages 1-7 (only page 8, written last and never
# overwritten, stayed valid). Per-page temp files reproduce cleanly.
for i, f in enumerate(svgs):
    png = f.replace("/svg/", "/cards/").replace(".svg", ".png")
    im = Image.open(png).convert("RGB")
    tmp = f"/tmp/fr-ru-webpage-{i}.jpg"
    im.save(tmp, "JPEG", quality=QUALITY, optimize=True)
    imgs.append(Image.open(tmp))
imgs[0].save(os.path.join(ED, "Le-Lucerna-VOL3-RU-web.pdf"), save_all=True,
             append_images=imgs[1:], resolution=150.0)
print("render done, web quality", QUALITY)
