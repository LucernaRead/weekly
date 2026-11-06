# -*- coding: utf-8 -*-
"""W45 FR x JA edition renderer. SINGLE-PROCESS driver + cards + dual PDFs.

Run with tools/venv/bin/python only (cairosvg lives in the venv).
Step 1 imports the content modules in order in THIS process, so the
exercise registry (REG) accumulates 1..150 exactly once.
Step 2 renders cards (1950 wide) and the print PDF (cairosvg svg2pdf +
pypdf merge) from the freshly written SVGs.
Step 3 builds the web PDF FRESH from the delivered cards (Pillow save
PDF, default JPEG quality -- the q72/q75 conclusion is measured, not
assumed, by the web-pdf check script).
No content fixes live here; all content edits live in transform.py.
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import cairosvg  # noqa: E402
from pypdf import PdfWriter  # noqa: E402
from PIL import Image  # noqa: E402

BASE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-fr-ja")


def main():
    import content12, content34, content56, content7, content8  # noqa: F401
    os.makedirs(f"{BASE}/svg", exist_ok=True)
    os.makedirs(f"{BASE}/cards", exist_ok=True)
    svgs = sorted(glob.glob(f"{BASE}/svg/*.svg"))
    assert len(svgs) == 8, svgs
    for f in svgs:
        card = f.replace("/svg/", "/cards/").replace(".svg", ".png")
        cairosvg.svg2png(url=f, write_to=card, output_width=1950)
        print("card", card)
    w = PdfWriter()
    for f in svgs:
        tmp = os.path.join(HERE, "scratch", "page.pdf")
        cairosvg.svg2pdf(url=f, write_to=tmp)
        w.append(tmp)
    with open(f"{BASE}/Le-Lucerna-VOL3-JA.pdf", "wb") as fh:
        w.write(fh)
    print("print pdf", f"{BASE}/Le-Lucerna-VOL3-JA.pdf")
    imgs = []
    for f in svgs:
        card = f.replace("/svg/", "/cards/").replace(".svg", ".png")
        imgs.append(Image.open(card).convert("RGB"))
    imgs[0].save(f"{BASE}/Le-Lucerna-VOL3-JA-web.pdf", save_all=True,
                 append_images=imgs[1:], resolution=150.0,
                 title="Le-Lucerna-VOL3-JA-web")
    print("web pdf", f"{BASE}/Le-Lucerna-VOL3-JA-web.pdf")


if __name__ == "__main__":
    main()
