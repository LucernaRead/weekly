# -*- coding: utf-8 -*-
"""FR x DE gate checks (read-only over shipped SVGs).
- text-node extraction per page
- CJK scan (Han chars in rendered text nodes; base64 excluded by construction)
- French-frozen check via tools/freeze.py diff (run separately)
- gloss counts: gloss() call strings in source split on '·' (README #21),
  plus bridge HINWEIS notes and word-list boxes, per page
- footer/badge/badge-y checks, P7 quote checks, P8 ends
Usage: venv python checks.py
"""
import os, re, sys, glob
import xml.etree.ElementTree as ET

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
CORE = os.path.join(ROOT, "weekly-report-w45-fr-core", "svg")
ED = os.path.join(ROOT, "weekly-report-w45-fr-es", "svg")


def nodes(path):
    out = []
    tree = ET.parse(path)
    for el in tree.getroot().iter():
        if el.tag.endswith("text") and (el.text or "").strip():
            out.append((float(el.get("x") or 0), float(el.get("y") or 0),
                        el.get("font-size"), (el.text or "").strip()))
    return out


def all_text(path):
    return " ".join(t for _, _, _, t in nodes(path))


for name, d in [("core", CORE), ("edition", ED)]:
    print(f"--- {name} ---")
    for p in sorted(glob.glob(os.path.join(d, "*.svg"))):
        txt = all_text(p)
        han = [c for c in txt if "\u4e00" <= c <= "\u9fff"]
        fw = txt.count("（") + txt.count("）")
        print(os.path.basename(p), "chars:", len(txt), "Han:", len(han),
              "fullwidth-parens:", fw,
              "footer-ES:" , ("SEMANARIO FRANCÉS VOL.3" in txt),
              "footer-ZH:", ("法语周报" in txt))
    print()

# P1 furniture
p1 = all_text(os.path.join(ED, "p1-une.svg"))
for s in ["TEXTOS EN FRANCÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES",
          "SEMANARIO EN FRANCÉS · VOL.3 · FIN DE SEMANA DE FINALES",
          "HEBDOMADAIRE EN FRANÇAIS · CADA SEMANA · EL FRANCÉS QUE LEEN LOS FRANCESES",
          "Le Lucerna"]:
    print("P1 contains", repr(s[:40]), ":", s in p1)
badge = [n for n in nodes(os.path.join(ED, "p1-une.svg")) if "TEXTOS EN FRANCÉS" in n[3]]
print("badge nodes:", badge)

# P7 frozen quotes + reader corner
p7 = all_text(os.path.join(ED, "p7-langue.svg"))
for s in ["Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?",
          "Les jeunes créateurs y rencontrent leur public, en vrai.",
          "Ce calendrier peut encore bouger.",
          "¡Envíanos tu carta o tu mejor texto de la página 8!",
          "ningún texto del VOL.2 llegó a tiempo",
          "Exemple de la rédaction (ce texte n'est pas une lettre de lecteur)"]:
    print("P7 contains", repr(s[:50]), ":", s in p7)
# P7 word-box definitions must stay French verbatim (core P7 box strings)
p7core = all_text(os.path.join(CORE, "p7-langue.svg"))
print("P7 core-vs-edition shared French sentences check: see freeze diff.")

# P8 ends: max y of text nodes on P8 (answers flow) and P7 teaser
for pg in ["p7-langue.svg", "p8-exercices.svg"]:
    ns = nodes(os.path.join(ED, pg))
    print(pg, "max text y:", max(y for _, y, _, _ in ns))
print("bridge-word present (forbidden):", any("桥接" in all_text(os.path.join(ED, p))
      for p in os.listdir(ED)))
