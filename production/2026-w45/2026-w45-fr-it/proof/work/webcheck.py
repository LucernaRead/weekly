# -*- coding: utf-8 -*-
"""Web-PDF vs cards check (own code, scratch outputs only).
1. Extract JPEG streams from delivered web PDF (pypdf), hash each.
2. Rebuild web PDF from delivered cards with the builder recipe
   (JPEG q72 optimize, Pillow save resolution=150), extract its streams, compare.
3. Per page: decode delivered JPEG, compare pixels vs delivered card PNG
   resized to JPEG size: full-res mean abs diff + 4x-downsampled mean abs diff.
4. Cards vs SVG re-render (cairosvg @1950) byte compare.
5. Print PDF page count/size via pypdf.
"""
import os, sys, io, json, hashlib
from PIL import Image
import cairosvg
from pypdf import PdfReader, PdfWriter

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-it")
WORK = sys.argv[1]
os.makedirs(WORK, exist_ok=True)

def page_images(pdf_path):
    r = PdfReader(pdf_path)
    out = []
    for i, page in enumerate(r.pages):
        imgs = []
        for img in page.images:
            imgs.append((img.name, img.data))
        out.append({"mediabox": [float(v) for v in page.mediabox], "images": [(n, hashlib.sha256(b).hexdigest(), len(b)) for n, b in imgs]})
    return r, out

web = os.path.join(ROOT, "Le-Lucerna-VOL3-IT-web.pdf")
r, web_info = page_images(web)
print("web pages:", len(r.pages), "page sizes pts:", web_info[0]["mediabox"])

cards = [os.path.join(ROOT, "cards", f"p{n}-{s}.png") for n, s in
         [(1, "une"), (2, "vie"), (3, "culture"), (4, "sport"), (5, "jeunesse"), (6, "politique"), (7, "langue"), (8, "exercices")]]
# rebuild
imgs = []
for c in cards:
    im = Image.open(c).convert("RGB")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=72, optimize=True)
    imgs.append(Image.open(io.BytesIO(buf.getvalue())).copy())
    print("card", os.path.basename(c), Image.open(c).size, "jpeg bytes", len(buf.getvalue()))
rebuilt = os.path.join(WORK, "rebuilt-web.pdf")
imgs[0].save(rebuilt, save_all=True, append_images=imgs[1:], resolution=150.0)
r2, rebuilt_info = page_images(rebuilt)
print("rebuilt pages:", len(r2.pages))
stream_match = []
for i in range(8):
    a = web_info[i]["images"]; b = rebuilt_info[i]["images"]
    stream_match.append({"page": i + 1, "delivered": a, "rebuilt": b,
                         "same_stream": [x[1] for x in a] == [x[1] for x in b]})
    print(f"page {i+1} delivered streams {a} rebuilt {b} same={stream_match[-1]['same_stream']}")

# pixel compare delivered JPEG vs card (PIL only)
from PIL import ImageChops, ImageStat
def mad(a, b):
    d = ImageChops.difference(a, b)
    s = ImageStat.Stat(d)
    return sum(s.mean) / len(s.mean)
pix = []
for i, c in enumerate(cards):
    rr = PdfReader(web)
    data = rr.pages[i].images[0].data
    j = Image.open(io.BytesIO(data)).convert("RGB")
    card = Image.open(c).convert("RGB")
    card_r = card.resize(j.size, Image.LANCZOS)
    m = mad(j, card_r)
    js = j.resize((j.size[0] // 4, j.size[1] // 4), Image.LANCZOS)
    cs = card_r.resize((j.size[0] // 4, j.size[1] // 4), Image.LANCZOS)
    m_ds = mad(js, cs)
    pix.append({"page": i + 1, "jpeg_size": j.size, "card_size": card.size,
                "mean_abs_diff": round(m, 3), "downsampled_mean_abs_diff": round(m_ds, 3)})
    print(f"page {i+1} jpeg {j.size} MAD {m:.3f} DS-MAD {m_ds:.3f}")

# cards vs SVG re-render
svg_names = ["p1-une", "p2-vie", "p3-culture", "p4-sport", "p5-jeunesse", "p6-politique", "p7-langue", "p8-exercices"]
card_match = []
for s, c in zip(svg_names, cards):
    out = os.path.join(WORK, s + "-rerender.png")
    cairosvg.svg2png(url=os.path.join(ROOT, "svg", s + ".svg"), write_to=out, output_width=1950)
    h1 = hashlib.sha256(open(out, "rb").read()).hexdigest()
    h2 = hashlib.sha256(open(c, "rb").read()).hexdigest()
    card_match.append({"page": s, "rerender_sha": h1, "card_sha": h2, "identical": h1 == h2})
    print(s, "rerender==card:", h1 == h2, Image.open(out).size)

# print PDF
pr = PdfReader(os.path.join(ROOT, "Le-Lucerna-VOL3-IT.pdf"))
print("print pages:", len(pr.pages), "size pts:", [float(v) for v in pr.pages[0].mediabox], "bytes:", os.path.getsize(os.path.join(ROOT, "Le-Lucerna-VOL3-IT.pdf")))
print("web bytes:", os.path.getsize(web), "rebuilt bytes:", os.path.getsize(rebuilt))
json.dump({"web_info": web_info, "rebuilt_info": rebuilt_info, "stream_match": stream_match,
           "pix": pix, "card_match": card_match,
           "print_pages": len(pr.pages), "print_bytes": os.path.getsize(os.path.join(ROOT, "Le-Lucerna-VOL3-IT.pdf")),
           "web_bytes": os.path.getsize(web), "rebuilt_bytes": os.path.getsize(rebuilt)},
          open(os.path.join(WORK, "webcheck.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
