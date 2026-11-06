# Own orphan scan: group text nodes by (page, x, size) with dy in [10,45] as
# consecutive lines; report last line of each group (final-line token).
# Defect classes flagged separately: mid-word split (line ends mid-word is
# not detectable from nodes alone -- wrap() splits on spaces by construction,
# so instead flag: final line is a lone punctuation fragment, starts with
# punctuation, or is a single short token following a longer line).
import re, sys, os, html, glob
def attr(a,k):
    m=re.search(k+r'="([^"]*)"',a); return m.group(1) if m else None
def nodes(path):
    out=[]
    for m in re.finditer(r'<text\b([^>]*)>([^<]*)</text>', open(path,encoding="utf-8").read()):
        a,t=m.group(1),html.unescape(m.group(2))
        if t.strip(): out.append((float(attr(a,"x")),float(attr(a,"y")),float(attr(a,"font-size")),t))
    return out
def scan(d,label):
    total=0; hits=[]
    for path in sorted(glob.glob(os.path.join(d,"*.svg"))):
        ns=nodes(path)
        # group by (x,size) sorted by y; consecutive if dy in [10,45]
        groups={}
        for x,y,s,t in ns: groups.setdefault((round(x,1),s),[]).append((y,t))
        for (x,s),lst in groups.items():
            lst.sort()
            cur=[lst[0]]
            seqs=[]
            for item in lst[1:]:
                if 10 <= item[0]-cur[-1][0] <= 45: cur.append(item)
                else: seqs.append(cur); cur=[item]
            seqs.append(cur)
            for seq in seqs:
                if len(seq)>=2:
                    y,t=seq[-1]
                    hits.append((os.path.basename(path),x,s,y,t))
    print(f"{label}: total orphan-scan hits (last line of >=2-line groups) = {len(hits)}")
    return hits
ed=scan(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru/svg"),"ED")
co=scan(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg"),"CORE")
import json
json.dump({"ed":ed,"core":co}, open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-ru-proof/work/orphans.json"),"w"), ensure_ascii=False, indent=1)
# print ED hits compactly
for h in ed: print("ED ", h)
