#!/usr/bin/env python3
"""W43 story images: resize raw generations to 1200x800 WebP <=400KB.
Adapted from the W46 convert_images.py approach. Prints per-file sizes."""
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
REPO = "/home/hatch/workspace/weekly-git"
OUT = os.path.join(REPO, "covers/2026-w43/images")
os.makedirs(OUT, exist_ok=True)

SRC = {
    "de": "media-generation-w43-de-0-d7e5ee35-1fea-47de-a760-7817d7a94525.webp",
    "fr": "media-generation-w43-fr-0-e2a847ad-26f0-4bdf-8c66-7cc92d6a13df.webp",
    "es": "media-generation-w43-es-0-b7bfabf3-1dcc-43ec-8102-a77b8d487293.webp",
    "en": "media-generation-w43-en-0-32f5cdd0-5058-4ece-b05e-d08c1d4d8b28.webp",
    "it": "media-generation-w43-it-0-59e39230-5274-4525-ad37-b1f1b10d1928.webp",
    "pt": "media-generation-w43-pt-0-3845f249-aa53-4129-9b1c-860111a7ee07.webp",
    "nl": "media-generation-w43-nl-0-943af77e-ea58-4999-9ff6-87377c1c2581.webp",
    "ru": "media-generation-w43-ru-0-24052e62-4c6d-4ee2-9143-e3dd543073da.webp",
    "ja": "media-generation-w43-ja-0-e9224fdb-c9a8-49d2-a9e2-f6bbae1d5f19.webp",
    "ko": "media-generation-w43-ko-0-2aa4582b-26f7-4077-bb0d-f1ef8173ec8b.webp",
    "zh-cn": "media-generation-w43-zh-cn-0-e985ae27-f557-456a-8ff7-d569f2dfad9a.webp",
    "zh-tw": "media-generation-w43-zh-tw-0-522166b8-2dc9-4d77-832f-343e627e2398.webp",
}

def convert(src_path, dst_path, start_q):
    im = Image.open(src_path).convert("RGB").resize((1200, 800), Image.LANCZOS)
    q = start_q
    while q >= 55:
        im.save(dst_path, "WEBP", quality=q, method=6)
        if os.path.getsize(dst_path) <= 400 * 1024:
            return q
        q -= 5
    raise SystemExit(f"UNDERFLOW {dst_path} still >400KB at q=55")

for lang, fn in SRC.items():
    q = convert(os.path.join(RAW, fn), os.path.join(OUT, f"{lang}.webp"), 82)
    print(f"{lang}: q={q} {os.path.getsize(os.path.join(OUT, lang + '.webp'))} bytes")
# High-quality en embed version for the feature slot (base64 in all 12 covers).
q = convert(os.path.join(RAW, SRC["en"]), os.path.join(HERE, "en_hq.webp"), 92)
print(f"en_hq: q={q} {os.path.getsize(os.path.join(HERE, 'en_hq.webp'))} bytes")
print("OK")
