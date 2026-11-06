import re, json
from xml.etree import ElementTree as ET
def parse(path):
    t=ET.parse(path)
    nodes=[]
    for e in t.iter():
        if e.tag.endswith('text') and e.text:
            nodes.append(e.text)
    # answers region: after node starting with RESPUESTAS
    start=None
    for i,tx in enumerate(nodes):
        if tx.startswith('RESPUESTAS'):
            start=i; break
    assert start is not None
    ans={}
    cur=None; buf=[]
    def flush():
        nonlocal cur, buf
        if cur is not None:
            s=' '.join(buf)
            s=re.sub(r'\s+',' ',s).strip()
            ans[cur]=s
        buf=[]
    for tx in nodes[start+1:]:
        tx=tx.strip()
        if re.match(r'^— PÁGINA \d+ —$', tx) or tx.startswith('Una nota'):
            continue
        m=re.match(r'^(\d+)\.\s*(.*)$', tx)
        if m and 1<=int(m.group(1))<=150 and cur != int(m.group(1)):
            flush(); cur=int(m.group(1)); buf=[m.group(2)] if m.group(2) else []
        elif cur is not None:
            buf.append(tx)
    flush()
    # key = first-dash split: 'key — note'; writing form '✓ note'
    keys={}
    for n,s in ans.items():
        if ' — ' in s:
            keys[n]=s.split(' — ',1)[0].strip()
        else:
            keys[n]=s
    return ans, keys
core_ans, core_keys = parse('/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-core/svg/p8-ejercicios.svg')
ed_ans, ed_keys = parse('/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-it/svg/p8-ejercicios.svg')
print(f"core answers parsed: {len(core_ans)} numbers {min(core_ans)}..{max(core_ans)} missing={sorted(set(range(1,151))-set(core_ans))}")
print(f"ed   answers parsed: {len(ed_ans)} numbers {min(ed_ans)}..{max(ed_ans)} missing={sorted(set(range(1,151))-set(ed_ans))}")
diffs=[]
for n in range(1,151):
    if core_keys.get(n)!=ed_keys.get(n):
        diffs.append(n)
        print(f"--- KEY DIFF #{n} ---")
        print(f"  CORE printed: {core_ans.get(n)!r}")
        print(f"  CORE key     : {core_keys.get(n)!r}")
        print(f"  ED   printed: {ed_ans.get(n)!r}")
        print(f"  ED   key     : {ed_keys.get(n)!r}")
        # note tail check: does ED note end with ASCII paren group?
        ednote = ed_ans.get(n,'').split(' — ',1)[1] if ' — ' in ed_ans.get(n,'') else ''
        print(f"  ED note tail : {ednote[-60:]!r}  ends-paren-group={bool(re.search(r'\([^()]*\)\s*$', ednote))}")
print(f"TOTAL key diffs by independent dash-parse: {diffs}")
# specific checks
for n in [139,140,150]:
    print(f"#{n} CORE key={core_keys.get(n)!r}  ED key={ed_keys.get(n)!r}  identical={core_keys.get(n)==ed_keys.get(n)}")
    print(f"   ED printed: {ed_ans.get(n)!r}")
json.dump({'core_keys':core_keys,'ed_keys':ed_keys,'diffs':diffs}, open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-it-proof/p8-dashparse.json','w'), ensure_ascii=False, indent=1)
