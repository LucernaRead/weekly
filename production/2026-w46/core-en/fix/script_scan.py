# Read-only Unicode-range scan of rendered SVG <text> contents.
import re, sys
from pathlib import Path
BASE = Path.home() / "workspace/goals/lucernaread-social-media-operations/files"
def rng(ch):
    o = ord(ch)
    if 0x4E00 <= o <= 0x9FFF or 0x3400 <= o <= 0x4DBF: return "Han"
    if 0x3040 <= o <= 0x309F: return "Hiragana"
    if 0x30A0 <= o <= 0x30FF: return "Katakana"
    if 0xAC00 <= o <= 0xD7A3: return "Hangul"
    if 0x0400 <= o <= 0x04FF: return "Cyrillic"
    return None
TEXT_RE = re.compile(r"<text\b[^>]*>(.*?)</text>", re.S)
for d in sorted(BASE.glob("weekly-report-w46-en-*")):
    txt = ""
    for svg in sorted((d / "svg").glob("*.svg")):
        raw = svg.read_text(encoding="utf-8", errors="replace")
        for m in TEXT_RE.finditer(raw):
            txt += re.sub(r"<[^>]+>", "", m.group(1))
    from collections import Counter
    c = Counter(rng(ch) for ch in txt)
    c.pop(None, None)
    print(d.name.replace("weekly-report-w46-en-", ""), dict(c))
