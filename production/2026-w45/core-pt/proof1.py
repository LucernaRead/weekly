# -*- coding: utf-8 -*-
"""W45 PT core self-proofread checks: text dump, golden-quote counts,
exercise-number continuity, P8 key coverage, banned words, footer/badge."""
import re, glob, html

ED = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-core/svg"
svgs = sorted(glob.glob(ED + "/*.svg"))
assert len(svgs) == 8, svgs
alltext = []
for s in svgs:
    raw = open(s, encoding="utf-8").read()
    texts = re.findall(r"<text[^>]*>(.*?)</text>", raw)
    texts = [html.unescape(t) for t in texts]
    alltext.append("\n".join(texts))
    with open(f"/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/pt-core/text-{s.split('/')[-1].replace('.svg', '.txt')}", "w", encoding="utf-8") as fh:
        fh.write("\n".join(texts))
joined = re.sub(r"\s+", " ", "\n".join(alltext).replace("«", "").replace("»", ""))

quotes = [
    "Do feriadão à prova: a semana do Enem",
    "Muita gente viaja, visita a família e vai ao cemitério levar flores",
    "Finados é o dia da memória",
    "lembrar é um jeito de continuar perto",
    "cada ponto vale uma posição, cada gol vale uma história",
    "quem dorme bem lembra melhor",
    "primeiro as fáceis, depois as difíceis",
    "Confira o cartão, durma bem, chegue cedo",
]
print("== golden quotes (want exactly 2 each) ==")
for q in quotes:
    print(joined.count(q), "|", q)

print("== banned words ==")
for w in ["bridge", "桥接", "ponte", "VOL.1", "VOL1"]:
    print(w, joined.count(w))
print("== masthead/foot ==")
print("A Lucerna count:", joined.count("A Lucerna"))
print("VOL.2 count:", joined.count("VOL.2"))
print("== P8 keys: numbered answer lines ==")
p8 = alltext[7]
keys = re.findall(r"^(\d+)\. ", p8, flags=re.M)
print("answer-line numbers found:", len(keys), "first:", keys[0] if keys else None, "last:", keys[-1] if keys else None)
nums = [int(k) for k in keys]
print("continuous 1..150:", nums == list(range(1, 151)))
print("== char counts ==")
tot = 0
for i, t in enumerate(alltext, 1):
    c = len(re.sub(r"\s", "", t))
    tot += c
    print(f"P{i}: {c}")
print("TOTAL non-space chars:", tot)
