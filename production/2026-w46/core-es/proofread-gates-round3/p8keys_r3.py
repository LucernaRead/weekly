import xml.etree.ElementTree as ET, pathlib, re, json
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
NS="{http://www.w3.org/2000/svg}"
def answers(d):
    t=ET.parse(d/"svg"/"p8-ejercicios.svg")
    els=[(el.text or "") for el in t.iter(NS+"text")]
    # find RESPUESTAS header index
    start=None
    for i,s in enumerate(els):
        if s.startswith("RESPUESTAS"):
            start=i; break
    assert start is not None
    rest=els[start+1:]
    # join: new item when text starts with "N. " (number dot space) at line start; but wrapped lines may also... answer lines begin with number.
    items={}; cur=None
    for s in rest:
        m=re.match(r"^(\d+)\.\s+(.*)$", s.strip())
        if m:
            cur=int(m.group(1)); items[cur]=m.group(2).strip()
        elif cur is not None:
            items[cur]+=" "+s.strip()
    return items
core=answers(BASE/"weekly-report-w46-es-core")
de=answers(BASE/"weekly-report-w46-es-de")
print("core items:", len(core), "de items:", len(de))
print("missing in DE:", sorted(set(core)-set(de)), "extra in DE:", sorted(set(de)-set(core)))
diffs=[]
for n in sorted(core):
    if core[n]!=de[n]:
        diffs.append(n)
        print(f"--- {n} ---\n  CORE: {core[n]}\n  DE:   {de[n]}")
print("differing items:", diffs)
# key token = text up to ' — ' or ' - ' or end; for sentence keys whole sentence is key
def keypart(s):
    return s.split(" — ")[0].strip()
print("\n=== key parts differing ===")
for n in diffs:
    print(n, "CORE key:", repr(keypart(core[n])), "| DE key:", repr(keypart(de[n])))
# model word count from DE joined answers region: find model text in P8 pre-RESPUESTAS region
t=ET.parse(BASE/"weekly-report-w46-es-de"/"svg"/"p8-ejercicios.svg")
joined=" ".join((el.text or "") for el in t.iter(NS+"text"))
j=joined.find("Vivo en Madrid")
k=joined.find("RESPUESTAS", j)
model=joined[j:k].strip()
print("\nmodel words (DE SVG):", len(model.split()))
print(model)
# core model too
t2=ET.parse(BASE/"weekly-report-w46-es-core"/"svg"/"p8-ejercicios.svg")
joined2=" ".join((el.text or "") for el in t2.iter(NS+"text"))
j2=joined2.find("Vivo en Madrid"); k2=joined2.find("RESPUESTAS", j2)
model2=joined2[j2:k2].strip()
print("model words (CORE SVG):", len(model2.split()), "| identical:", model==model2)
json.dump({"core":core,"de":de}, open(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/w46/es-proofread-gates-round3/p8keys-r3.json","w"), ensure_ascii=False, indent=1)
