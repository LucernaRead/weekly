from xml.etree import ElementTree as ET
import re
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-pt/svg"
CORE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg"
def alltext(base):
    out=""
    for pg in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
        t=ET.parse(f"{base}/{pg}.svg")
        out+="\n"+" ".join(''.join(el.itertext()) for el in t.iter() if el.tag.split('}')[-1]=='text')
    return out
def p7list(base):
    t=ET.parse(f"{base}/p7-yazyk.svg")
    return [(float(el.get('y')), ''.join(el.itertext()).strip()) for el in t.iter() if el.tag.split('}')[-1]=='text' and ''.join(el.itertext()).strip()]
ed=alltext(ED)
print("=== P7 golden list lines (y>=1794) ===")
for y,s in sorted(p7list(ED)):
    if y>=1794: print(f"  y={y} :: {s}")
