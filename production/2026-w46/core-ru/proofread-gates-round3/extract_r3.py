import re, glob, json, collections
def texts(p):
    t=open(p,encoding='utf-8').read()
    return re.findall(r'<text[^>]*>(.*?)</text>',t,re.S)
def attrs(p):
    t=open(p,encoding='utf-8').read()
    return re.findall(r'<text[^>]*>',t)
ed=f"{__import__('os').path.expanduser('~')}/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-it"
out={}
for f in sorted(glob.glob(ed+'/svg/*.svg')):
    ns=texts(f)
    out[f.split('/')[-1]]=ns
    print("==",f.split('/')[-1],"nodes:",len(ns))
json.dump(out,open(__import__('os').path.expanduser('~')+'/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ru-proofread-gates-round3/gates/svg-text-nodes.json','w'),ensure_ascii=False,indent=1)
