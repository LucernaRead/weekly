import re, glob
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg"
CO="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg"
def alltext(d):
    out={}
    for f in sorted(glob.glob(d+"/*.svg")):
        s=open(f,encoding="utf-8").read()
        ts=[re.sub(r"<[^>]+>","",m) for m in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
        out[f.split("/")[-1]]=ts
    return out
ed=alltext(ED); co=alltext(CO)
phrases=[("不用等11月11日","1"),("下单就能发货","2"),("先看结算页，再付款","2"),("水开始结冰","3"),("三场都输了","4"),("小局一场没赢","4"),("故事够不够好","5"),("别以后，就现在","5")]
def joined(ts): return "".join(ts)
for ph,pg in phrases:
    ce=joined(ed["p7-ciyu.svg"]).count(ph)  # P7 occurrence? joined per page not whole; do whole-issue below
    print(ph, "page tag", pg)
for label,dd in [("ED",ed),("CORE",co)]:
    whole="".join("".join(v) for v in dd.values())
    # reading-order joined count: text nodes in file order concatenated
    print("=====",label)
    for ph,pg in phrases:
        # count occurrences in whole issue text (per-page joined would split wraps; use whole joined with no separator - wraps split phrases across nodes!)
        c=whole.count(ph)
        # also count with whitespace-insensitive: strip all spaces? phrases have no spaces; node splits may break them
        print(f"  {ph}: raw-joined count={c}")
    # per-page: find which pages contain each phrase (allowing split across adjacent nodes: join nodes of that page)
    for ph,pg in phrases:
        pages=[k for k,v in dd.items() if ph in "".join(v)]
        print(f"  {ph} on pages: {pages} (tag says p.{pg})")
