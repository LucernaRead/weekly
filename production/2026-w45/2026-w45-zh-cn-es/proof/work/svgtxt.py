# Reproof helper: text-node extraction + targeted checks (read-only on delivered SVGs).
import re, sys, glob, os, json
from xml.etree import ElementTree as ET

def texts(svgpath):
    # SVG text nodes: collect <text> elements' full text (incl. tspans) in doc order
    tree = ET.parse(svgpath)
    ns = {'s': 'http://www.w3.org/2000/svg'}
    out = []
    for el in tree.iter():
        if el.tag.endswith('}text') or el.tag == 'text':
            t = ''.join(el.itertext())
            out.append(t)
    return out

def alltexts(d):
    res = {}
    for f in sorted(glob.glob(os.path.join(d, '*.svg'))):
        res[os.path.basename(f)] = texts(f)
    return res

if __name__ == '__main__':
    d = sys.argv[1]
    res = alltexts(d)
    for k, v in res.items():
        print(f"== {k}: {len(v)} text nodes")
    if len(sys.argv) > 2 and sys.argv[2] == 'dump':
        out = sys.argv[3]
        with open(out, 'w', encoding='utf-8') as fh:
            json.dump(res, fh, ensure_ascii=False, indent=1)
        print("dumped", out)
