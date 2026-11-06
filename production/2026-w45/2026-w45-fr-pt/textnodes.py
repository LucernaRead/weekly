import sys, re, xml.etree.ElementTree as ET
# dump text nodes: page, y, size, text
for path in sys.argv[1:]:
    print("==", path)
    tree = ET.parse(path)
    for el in tree.getroot().iter():
        if el.tag.endswith('text') and (el.text or '').strip():
            print(f"y={el.get('y')} x={el.get('x')} fs={el.get('font-size')} | {(el.text or '').strip()}")
