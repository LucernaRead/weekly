import json, pathlib, re, xml.etree.ElementTree as ET
G=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/w46/es-proofread-gates-round3/freeze-de.json"
data=json.loads(G.read_text())
NS="{http://www.w3.org/2000/svg}"
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
def page_texts(d,nm):
    t=ET.parse(d/"svg"/nm); return [(el.get("x"),el.get("y"),el.text or "") for el in t.iter(NS+"text")]
# Gloss: find HINWEIS block lines by column: P2 x=527? gloss boxes at bottom? Print all texts containing gloss headwords per page and join consecutive lines in same column.
# Simpler: use added strings containing gloss fragments + SVG order join per page.
for pg,nm in [(2,"p2-vida.svg"),(3,"p3-cultura.svg"),(4,"p4-deporte.svg"),(5,"p5-juventud.svg")]:
    print(f"=== P{pg} added strings mentioning gloss terms ===")
    for s in data["pages"][str(pg)]["added_strings"]:
        print("  +", s["text"])
    print(f"--- P{pg} removed strings (first 8) ---")
    for s in data["pages"][str(pg)]["removed_strings"][:8]:
        print("  -", s["text"])
