import sys, json, re
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
import p8
CORE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-core/svg/p8-ejercicios.svg"
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-es-fr/svg/p8-ejercicios.svg"
def segs(path):
    texts=p8.load_texts(path)
    els=p8.answers_elements(texts)
    entries=p8.split_lines(els,150)
    full,_=p8.extract(path,150)
    return entries, full
cs, cf = segs(CORE)
es, ef = segs(ED)
def dashkey(seg):
    seg=seg.strip()
    if seg.startswith("✓"):
        return "✓", seg[1:].strip()
    if " — " in seg:
        k,t=seg.split(" — ",1)
        return k.strip(), t.strip()
    return seg, ""
keydiff=[17,18,20,25,26,27,28,52,53,54,55,60,61,62,63,83,85,93,94,95,96,98,107,109,110,111,117,137,138,141,142,143,144,148]
rows=[]
for n in keydiff:
    ck,ct=dashkey(cs[n]); ek,et=dashkey(es[n])
    rows.append({"n":n,"core_seg":cs[n],"ed_seg":es[n],"core_dashkey":ck,"ed_dashkey":ek,
                 "dash_equal":ck==ek,"core_toolkey":cf[n]["key"],"ed_toolkey":ef[n]["key"],
                 "ed_method":ef[n]["method"],
                 "ed_note_tail_paren": bool(re.search(r"\(([^()]*)\)\s*$", et))})
    print(f"--- #{n} dash_equal={ck==ek} ed_method={ef[n]['method']} tailparen={rows[-1]['ed_note_tail_paren']}")
    print(f"  CORE seg: {cs[n]}")
    print(f"  ED   seg: {es[n]}")
    print(f"  CORE dashkey: {ck!r} | ED dashkey: {ek!r}")
    print(f"  toolkeys core={cf[n]['key']!r} ed={ef[n]['key']!r}")
diffs=[]
for n in range(1,151):
    ck,_=dashkey(cs[n]); ek,_=dashkey(es[n])
    if ck!=ek: diffs.append(n)
print("ALL-150 dashkey diffs:", diffs)
for n in [139,140,150]:
    print(f"#{n} CORE seg: {cs[n]}")
    print(f"#{n} ED   seg: {es[n]}")
    print(f"#{n} dashkeys core={dashkey(cs[n])[0]!r} ed={dashkey(es[n])[0]!r} methods core={cf[n]['method']} ed={ef[n]['method']}")
json.dump({"rows":rows,"all_dash_diffs":diffs}, open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-fr-proof/dashparse.json","w"), ensure_ascii=False, indent=1)
