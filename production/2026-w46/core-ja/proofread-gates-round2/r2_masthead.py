# Masthead pixel clearance on rendered P1 cards: find ink-row bands in the
# masthead region and report gaps between bands (wordmark / subtitle / badge /
# strapline). Cards are 1950x2700 renders of the SVGs.
from PIL import Image
import os
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
DIRS = {"zh-cn": "weekly-report-w46-ja-core", "de": "weekly-report-w46-ja-de",
        "en": "weekly-report-w46-ja-en", "es": "weekly-report-w46-ja-es",
        "fr": "weekly-report-w46-ja-fr", "it": "weekly-report-w46-ja-it",
        "ko": "weekly-report-w46-ja-ko", "nl": "weekly-report-w46-ja-nl",
        "pt": "weekly-report-w46-ja-pt", "ru": "weekly-report-w46-ja-ru",
        "zh-tw": "weekly-report-w46-ja-zh-tw"}
for code, d in DIRS.items():
    im = Image.open(os.path.join(BASE, d, "cards", "p1-hyoushi.png")).convert("L")
    W, H = im.size
    px = im.load()
    # ink = dark pixel in masthead x-range; scan rows y=100..450
    bands = []
    in_band = False
    for y in range(100, 450):
        ink = any(px[x, y] < 120 for x in range(60, 1890, 3))
        if ink and not in_band:
            start = y; in_band = True
        elif not ink and in_band:
            bands.append((start, y - 1)); in_band = False
    if in_band: bands.append((start, 449))
    gaps = [bands[i+1][0] - bands[i][1] - 1 for i in range(len(bands) - 1)]
    print(code, "size", (W, H), "bands", bands, "gaps", gaps)
