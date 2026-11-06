# -*- coding: utf-8 -*-
"""Web PDF vs cards, own implementation (pypdf image extraction + PIL)."""
import os, io, sys
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
from pypdf import PdfReader
from PIL import Image, ImageChops, ImageStat
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-nl")
for pdf, label in [(os.path.join(ED, "Lucerna-VOL2-NL-web.pdf"), "web"),
                   (os.path.join(ED, "Lucerna-VOL2-NL.pdf"), "print")]:
    r = PdfReader(pdf)
    print(f"{label} PDF: pages={len(r.pages)} bytes={os.path.getsize(pdf)}")
r = PdfReader(os.path.join(ED, "Lucerna-VOL2-NL-web.pdf"))
cards = sorted(os.path.join(ED, "cards", f) for f in os.listdir(os.path.join(ED, "cards")) if f.endswith(".png"))
print("cards order:", [os.path.basename(c) for c in cards])
for i, page in enumerate(r.pages):
    imgs = list(page.images)
    if not imgs:
        print(f"  web p{i+1}: NO embedded image"); continue
    im = Image.open(io.BytesIO(imgs[0].data)).convert("RGB")
    card = Image.open(cards[i]).convert("RGB").resize(im.size, Image.LANCZOS)
    diff = ImageStat.Stat(ImageChops.difference(im, card)).mean
    print(f"  web p{i+1}: raster={im.size} mean|diff|={[round(v, 2) for v in diff]} max_mean={max(diff):.2f}")
