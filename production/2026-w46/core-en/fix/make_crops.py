from PIL import Image, ImageDraw
from pathlib import Path
BASE = Path.home() / "workspace/goals/lucernaread-social-media-operations/files"
OUT = Path.home() / "workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-fix/crops"
OUT.mkdir(exist_ok=True)
def crop(ed, card, box, name, scale=2):
    im = Image.open(BASE / f"weekly-report-w46-en-{ed}/cards/{card}").convert("RGB").crop(box)
    im = im.resize((im.width*scale, im.height*scale), Image.LANCZOS)
    im.save(OUT / name)
    print(name, im.size)
def sheet(items, name, label_h=40, gap=12, scale=2):
    crops = []
    for ed, card, box, label in items:
        im = Image.open(BASE / f"weekly-report-w46-en-{ed}/cards/{card}").convert("RGB").crop(box)
        im = im.resize((im.width*scale, im.height*scale), Image.LANCZOS)
        crops.append((label, im))
    w = max(im.width for _, im in crops)
    h = sum(label_h + im.height + gap for _, im in crops)
    sh = Image.new("RGB", (w, h), "white")
    d = ImageDraw.Draw(sh); y = 0
    for label, im in crops:
        d.text((8, y+10), label, fill="black")
        sh.paste(im, (0, y+label_h)); y += label_h + im.height + gap
    sh.save(OUT / name); print(name, sh.size)
# B4 toolbox sheets (box x 1440..1890, y 400..570)
sheet([(ed,"p7-langue.png",(1440,400,1890,570),f"P7 toolbox {ed}") for ed in ["core","de","es","fr","it","ja"]], "b4-sheet1.png")
sheet([(ed,"p7-langue.png",(1440,400,1890,570),f"P7 toolbox {ed}") for ed in ["ko","nl","pt","ru","zh-tw"]], "b4-sheet2.png")
# B5 editor note
sheet([(ed,"p7-langue.png",(980,2040,1890,2170),f"P7 editor note {ed}") for ed in ["core","zh-tw"]], "b5-sheet.png")
# B6 bridge
crop("zh-tw","p2-life.png",(515,1995,975,2115),"b6-bridge.png")
# B1 titles
sheet([(ed,"p6-politique.png",(1440,655,1890,745),f"P6 HOW LONG {ed}") for ed in ["es","pt","ru"]], "b1-sheet.png")
# ko orphans + B3
crop("ko","p3-culture.png",(530,565,975,685),"ko-p3-gloss.png")
crop("ko","p4-sport.png",(530,1090,975,1210),"ko-p4-gloss.png")
crop("ko","p8-exercices.png",(60,1935,1890,2210),"ko-p8-b3.png")
# M1 bands
sheet([(ed,"p8-exercices.png",(60,105,1890,175),f"P8 FINAL TEST band {ed}") for ed in ["de","fr"]], "m1-sheet.png")
# M4 titles
sheet([(ed,"p3-culture.png",(1440,825,1890,915),f"P3 title {ed}") for ed in ["nl","pt"]], "m4-sheet.png")
# M2 P2 gloss boxes
sheet([(ed,"p2-life.png",(990,1285,1890,1430),f"P2 gloss {ed}") for ed in ["fr","ko","zh-tw"]], "m2-sheet.png")
# M3 de P6 gloss (find box: crop col3 gloss area y 800-900)
crop("de","p6-politique.png",(1440,795,1890,905),"m3-de-gloss.png")
