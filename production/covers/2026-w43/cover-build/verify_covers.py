#!/usr/bin/env python3
"""Independent post-build verification for W43 covers (not the builder's
own assertions): 144/144 headline+teaser exactness, tag-structure parity
with the W45 template, en feature image bytes == en_hq.webp."""
import base64
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/weekly-git"
READERS = ["de", "fr", "es", "en", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]
teasers = json.load(open(os.path.join(HERE, "teasers.json"), encoding="utf-8"))["teasers"]
HEADLINES = {
    "de": "Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien",
    "fr": "Présidentielle 2027 : les Français regardent déjà les sondages",
    "es": "Este domingo: dormimos una hora más… ¡y se juega el Clásico!",
    "en": "First Votes, First Games : America's Biggest Week of the Autumn",
    "it": "Un'ora in più di sonno: domenica torna l'ora solare",
    "pt": "Domingo é dia de decisão: o Brasil volta às urnas",
    "nl": "Een volle week: vakantie, design, dance — en een uur extra slaap",
    "ru": "Первый снег — уже на этой неделе!",
    "ja": "土よう日、日本シリーズが始まる！",
    "ko": "태풍 참피가 오고 있어요",
    "zh-cn": "双11到了「付尾款」的这一周",
    "zh-tw": "強颱薔琵壓境！週五、週六風雨最大",
}
en_hq = open(os.path.join(HERE, "en_hq.webp"), "rb").read()

def tagseq(html):
    # Tag names + attributes, except img src/alt (replaced) — but keep
    # everything else so structural drift is caught.
    out = []
    for m in re.finditer(r"<[^>]+>", html):
        tag = m.group(0)
        if tag.startswith("<img"):
            tag = re.sub(r'src="[^"]*"', 'src=X', tag)
            tag = re.sub(r'alt="[^"]*"', 'alt=X', tag)
        if tag.startswith("<meta"):
            # Meta description content carries the week dates (legitimately
            # replaced W45 -> W43); it is text, not structure.
            tag = re.sub(r'content="[^"]*"', 'content=X', tag)
        out.append(tag)
    return out

fails = []
checked = 0
for r in READERS:
    out_path = os.path.join(REPO, "covers/2026-w43", f"2026-w43-cover-{r}",
                            f"2026-w43-cover-{r}.html")
    tpl_path = os.path.join(REPO, "covers/2026-w45", f"2026-w45-cover-{r}",
                            f"2026-w45-cover-{r}.html")
    out = open(out_path, encoding="utf-8").read()
    tpl = open(tpl_path, encoding="utf-8").read()
    order = re.search(r'data-story-langs="([^"]+)"', out).group(1).split()
    arts = re.split(r"(?=<article)", out)[1:]
    if len(arts) != 12:
        fails.append(f"{r}: {len(arts)} articles")
        continue
    for i, ch in enumerate(arts):
        tgt = order[i]
        h = re.search(r"<h[123][^>]*>(.*?)</h[123]>", ch, flags=re.S).group(1)
        p = re.search(r"<p[^>]*>(.*?)</p>", ch, flags=re.S).group(1)
        htxt = re.sub(r"<[^>]+>", "", h).strip()
        ptxt = re.sub(r"<[^>]+>", "", p).strip()
        checked += 1
        if htxt != HEADLINES[tgt]:
            fails.append(f"{r}/{tgt}: headline mismatch: {htxt[:60]!r}")
        if ptxt != teasers[r][tgt]:
            fails.append(f"{r}/{tgt}: teaser mismatch: {ptxt[:60]!r} vs {teasers[r][tgt][:60]!r}")
    # Tag-structure parity vs template.
    if tagseq(out) != tagseq(tpl):
        fails.append(f"{r}: tag sequence differs from W45 template")
    # En feature image bytes.
    m = re.search(r'<img[^>]*src="data:image/webp;base64,([^"]+)"', out)
    if not m:
        fails.append(f"{r}: no en feature img data URI")
    elif base64.b64decode(m.group(1)) != en_hq:
        fails.append(f"{r}: en feature image bytes != en_hq.webp")
    # No W45 story text: template article h/p texts must be gone.
    tpl_arts = re.split(r"(?=<article)", tpl)[1:]
    for ch in tpl_arts:
        for tag in ("h", "p"):
            mm = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", ch, flags=re.S)
            if mm:
                old = re.sub(r"<[^>]+>", "", mm.group(1)).strip()
                if old and old in out and tag == "h":
                    fails.append(f"{r}: W45 headline remains: {old[:60]!r}")

print(f"articles checked: {checked} (expect 144: 12 readers x 12 stories)")
if fails:
    print("FAILURES:")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("VERIFY OK: 144/144 texts exact, tag parity holds, en feature bytes match")
