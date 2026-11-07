#!/usr/bin/env python3
"""Convert raw W46 story images to repo spec: 1200x800 WebP, <=400 KB.
Also builds a high-quality en embed version for the feature slot.
Run from anywhere; paths are absolute."""
import os
from PIL import Image

RAW = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/cover-build/raw"
OUT = "/home/hatch/workspace/weekly-git/covers/2026-w46/images"
BUILD = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/cover-build"

SRC = {
    "de": "media-generation-w46-de-0-c9ea9a0e-96fb-4652-beae-f865dff5cad4.webp",
    "fr": "media-generation-w46-fr-0-fdbfb32f-dd0b-4403-a769-115c020e157f.webp",
    "es": "media-generation-w46-es-0-e6a6c5f4-ace1-4907-a081-6039141f4059.webp",
    "en": "media-generation-w46-en-0-af5e8024-b29e-47a6-b508-7d8c77c5fd52.webp",
    "it": "media-generation-w46-it-0-4a56a199-48fb-4798-99ed-bf8e0efcc95f.webp",
    "pt": "media-generation-w46-pt-0-723cd4c2-a7d4-496b-97e6-6484f7dea12f.webp",
    "nl": "media-generation-w46-nl-0-487eddb2-8da4-4a05-a30d-29f7c04f7cd0.webp",
    "ru": "media-generation-w46-ru-0-6e323274-ac62-4010-894f-e039d3292a8e.webp",
    "ja": "media-generation-w46-ja-0-7edfe294-e516-4464-9508-807d52e1533b.webp",
    "ko": "media-generation-w46-ko-0-bdff7ed6-e9d3-4eeb-9106-70458d569983.webp",
    "zh-cn": "media-generation-w46-zh-cn-0-c1d59251-1213-4a53-8ce6-568252f072bb.webp",
    "zh-tw": "media-generation-w46-zh-tw-0-2b305061-50b4-49fa-89e2-1ca66da1442c.webp",
}

os.makedirs(OUT, exist_ok=True)
for lang, fn in SRC.items():
    im = Image.open(os.path.join(RAW, fn)).convert("RGB")
    im = im.resize((1200, 800), Image.LANCZOS)
    q = 82
    while True:
        p = os.path.join(OUT, lang + ".webp")
        im.save(p, "WEBP", quality=q, method=6)
        size = os.path.getsize(p)
        if size <= 400 * 1024 or q <= 55:
            print(f"{lang}: {size} bytes @q{q}")
            break
        q -= 5
    assert open(p, "rb").read(12)[0:4] == b"RIFF" and open(p, "rb").read(12)[8:12] == b"WEBP"

# high-quality en embed version (feature slot, same image, less compression)
im = Image.open(os.path.join(RAW, SRC["en"])).convert("RGB").resize((1200, 800), Image.LANCZOS)
hq = os.path.join(BUILD, "en_hq.webp")
im.save(hq, "WEBP", quality=92, method=6)
print("en_hq:", os.path.getsize(hq), "bytes")
print("OK")
