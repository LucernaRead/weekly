import xml.etree.ElementTree as ET, re, json
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
for label,path in [("ED",f"{BASE}/files/weekly-report-w45-ko-ja/svg/p8-siheom.svg"),("CORE",f"{BASE}/files/weekly-report-w45-ko-core/svg/p8-siheom.svg")]:
    print(f"===== {label} =====")
    for t in texts(path):
        if re.match(r'^(81|137|138|139|140|150|109)\.', t.strip()):
            print(repr(t))
    # P8 header lines
    for t in texts(path):
        if '全解答' in t or '参考答案' in t or 'テストと答え' in t or '测验与答案' in t:
            print("HEADER:", repr(t))
