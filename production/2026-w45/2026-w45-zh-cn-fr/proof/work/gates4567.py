import re, glob, os
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg"
CO="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg"
FB="/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-cn-fr-build"
CB="/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zhcn-build"
def gloss_calls(builddir):
    # find gloss(...) call strings in content*.py + bslib? gloss() defined in bslib, called in content modules
    out={}
    for f in sorted(glob.glob(builddir+"/content*.py")):
        s=open(f,encoding="utf-8").read()
        for m in re.finditer(r"gloss\((.*?)\)\s*$", s, re.M):
            out.setdefault(os.path.basename(f),[]).append(m.group(1))
    return out
for label,bd in [("CORE",CB),("ED",FB)]:
    tot=0; print("=====",label)
    for f, calls in gloss_calls(bd).items():
        # each call: count items by splitting the rendered string arg on · itself.
        # The call arg is usually a single quoted string; extract string literals joined.
        n=0; details=[]
        for c in calls:
            lits=re.findall(r'"([^"]*)"', c)
            joined="".join(lits)
            items=[x for x in joined.split("·")]
            n+=len(items); details.append(len(items))
        print("  ",f,"calls:",len(calls),"items:",n,details)
        tot+=n
    print("  TOTAL gloss items:",tot)
