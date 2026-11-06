import re, glob, os
from collections import defaultdict
HANGUL = re.compile(r'[\uac00-\ud7a3]')
d = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-ko/svg")
tot_adj = 0; tot_ge3 = 0; examples = []
for path in sorted(glob.glob(d+"/*.svg")):
    src = open(path, encoding="utf-8").read()
    nodes = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"[^>]*>([^<]*)</text>', src):
        if m.group(5).strip():
            nodes.append((float(m.group(1)), float(m.group(2)), float(m.group(4)), m.group(5)))
    groups = defaultdict(list)
    for x,y,s,t in nodes: groups[(round(x),s)].append((y,t))
    for (x,s), lines in groups.items():
        lines.sort()
        for (y1,prev),(y2,nxt) in zip(lines, lines[1:]):
            p, n = prev.strip(), nxt.strip()
            if p and HANGUL.search(p[-1]) and n and HANGUL.search(n[0]):
                tot_adj += 1
                first = n.split()[0] if n.split() else ""
                if len(HANGUL.findall(first)) >= 3:
                    tot_ge3 += 1
                    if len(examples) < 25:
                        examples.append((os.path.basename(path), p[-18:], n[:22:], p.endswith(('요','다','요.','다.','요?','요!'))))
print("Hangul-Hangul adjacencies:", tot_adj, "of which next-first-token>=3 syll:", tot_ge3)
for e in examples: print(e)
