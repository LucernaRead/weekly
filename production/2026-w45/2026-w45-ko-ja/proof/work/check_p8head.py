import xml.etree.ElementTree as ET
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
for label,path in [("W43 ko-ja",f"{BASE}/files/weekly-report-ko-ja/svg/p8-siheom.svg"),("W45 ed",f"{BASE}/files/weekly-report-w45-ko-ja/svg/p8-siheom.svg"),("W45 core",f"{BASE}/files/weekly-report-w45-ko-core/svg/p8-siheom.svg")]:
    print(f"--- {label} ---")
    for t in texts(path):
        if '解答' in t or '参考答案' in t: print(repr(t))
