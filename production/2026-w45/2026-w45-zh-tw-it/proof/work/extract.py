# Proof extraction: parse shipped SVGs -> per-page text-node JSON.
# Read-only wrt shipped dirs. No content-module imports.
import json, re, sys, os, hashlib, base64
import xml.etree.ElementTree as ET

def texts(svg_path):
    tree = ET.parse(svg_path)
    out = []
    for el in tree.iter():
        tag = el.tag.split('}')[-1]
        if tag == 'text':
            t = ''.join(el.itertext())
            out.append({'x': el.get('x'), 'y': el.get('y'),
                        'size': el.get('font-size'), 'fill': el.get('fill'),
                        'anchor': el.get('text-anchor'), 'weight': el.get('font-weight'),
                        'text': t})
    return out

def images(svg_path):
    tree = ET.parse(svg_path)
    out = []
    for el in tree.iter():
        tag = el.tag.split('}')[-1]
        if tag == 'image':
            href = el.get('{http://www.w3.org/1999/xlink}href') or el.get('href') or ''
            raw = ''
            if href.startswith('data:'):
                raw = href.split(',', 1)[1] if ',' in href else ''
                try:
                    blob = base64.b64decode(raw)
                    h = hashlib.sha256(blob).hexdigest()
                except Exception:
                    h = 'DECODE-FAIL'
            else:
                h = 'EXTERNAL:' + href[:80]
            out.append({'x': el.get('x'), 'y': el.get('y'), 'w': el.get('width'),
                        'h': el.get('height'), 'sha': h})
    return out

def main(d, outpath):
    res = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith('.svg'):
            p = os.path.join(d, fn)
            res[fn] = {'texts': texts(p), 'images': images(p)}
    with open(outpath, 'w', encoding='utf-8') as fh:
        json.dump(res, fh, ensure_ascii=False, indent=1)
    print(outpath, 'pages:', len(res))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
