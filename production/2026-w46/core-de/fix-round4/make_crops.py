from PIL import Image
import os
R4 = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/de-fix-round4")
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-zh-cn/cards/p8-uebungen.png")
final = Image.open(ED)
before = Image.open(os.path.join(R4, "crops/p8-round3-state.png"))
print("final card:", final.size, "before:", before.size)
def crop(img, box, name, scale=2):
    c = img.crop(box)
    if scale != 1:
        c = c.resize((c.width*scale, c.height*scale), Image.NEAREST)
    c.save(os.path.join(R4, "crops", name))
    print(name, c.size)
# D-R3-2 seam (flag 1): x 400-1010, y 2140-2245
crop(final, (400, 2140, 1010, 2245), "flag1-fixed-2x.png")
crop(before, (400, 2140, 1010, 2245), "flag1-round3-2x.png")
# D-R3-1 seam (flag 2): x 480-1450, y 2470-2575
crop(final, (480, 2470, 1450, 2575), "flag2-fixed-2x.png")
crop(before, (480, 2470, 1450, 2575), "flag2-round3-2x.png")
# key140 block: x 1400-1950, y 2030-2165
crop(final, (1400, 2030, 1950, 2165), "key140-fixed-2x.png")
# full frame half-scale
half = final.resize((975, 1350), Image.LANCZOS)
half.save(os.path.join(R4, "crops/p8-full-fixed-half.png"))
print("p8-full-fixed-half.png", half.size)
