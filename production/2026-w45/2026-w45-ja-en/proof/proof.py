#!/usr/bin/env python3
# Independent proof script for W45 JA x EN. Read-only vs files/ trees; writes only to proof dir.
import re, json, hashlib, os, sys
from pathlib import Path
from collections import Counter
B = Path(os.environ["HOME"])/"workspace/goals/lucernaread-social-media-operations"
CORE = B/"files/weekly-report-w45-ja-core/svg"
ED = B/"files/weekly-report-w45-ja-en/svg"
W43 = B/"files/weekly-report-ja-en/svg"
PROOF = B/"hidden_files/w45/ja-en-proof"
FILES = {"p1":"p1-hyoushi.svg","p2":"p2-kurashi.svg","p3":"p3-bunka.svg","p4":"p4-supotsu.svg",
         "p5":"p5-wakamono.svg","p6":"p6-fukayomi.svg","p7":"p7-kotoba.svg","p8":"p8-tesuto.svg"}
def texts_of(p):
    t = p.read_text()
    out=[]
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        attrs=m.group(1); s=m.group(2)
        def grab(a):
            mm=re.search(a+r'="([^"]*)"', attrs); return mm.group(1) if mm else ""
        out.append({"x":float(grab("x") or 0),"y":float(grab("y") or 0),
                    "size":grab("font-size"),"bold":"700" in attrs,"anchor":grab("text-anchor"),
                    "fill":grab("fill"),"fam":grab("font-family"),"text":s})
    return out
def raw(p): return p.read_text()
def is_cjk(ch): return '\u2e80'<=ch<='\u9fff' or '\u3040'<=ch<='\u30ff'
def cjk_runs(s): return re.findall(r'[\u2e80-\u9fff\u3040-\u30ff]+', s)
out={}
# ---- 1. forbidden word ----
for name,path in [("svg-ed",ED),("kit",B/"files/weekly-report-w45-ja-en/WEEKLY-KIT.md"),("abstract",B/"files/weekly-report-w45-ja-en/ABSTRACT.txt")]:
    if path.is_dir():
        cnt=sum((p.read_text().count("桥接")+p.read_text().count("橋接")) for p in path.glob("*.svg"))
    else:
        cnt=path.read_text().count("桥接")+path.read_text().count("橋接")
    out[f"forbidden_{name}"]=cnt
# ---- 2. kinsoku line-start ----
NOSTART=set("、。。。。。．，、」』）】〕ー゛゜ァィゥェォッャュョヮぁぃぅぇぉっゃゅょゎ・：；？！〜…")
NOSTART |= set("、。．，」』）】〕")
kin={}
for pg,fn in FILES.items():
    for label,d in [("core",CORE),("ed",ED)]:
        bad=[t["text"] for t in texts_of(d/fn) if t["text"] and t["text"][0] in NOSTART]
        kin[f"{label}_p{pg}"]=bad
out["kinsoku"]={k:(len(v),v) for k,v in kin.items()}
# ---- 3. multiset diff audit: removed/added per page ----
fd=json.load(open(PROOF/"freeze-diff-proof.json"))
out["freeze_pages"]={k:{"added_n":len(v["added_strings"]),"removed_n":len(v["removed_strings"]),
    "cjk_core":v["cjk_core_total"],"cjk_ed":v["cjk_edition_total"],"cjk_added":v["cjk_added"]} for k,v in fd["pages"].items()}
# removed strings containing kana (potential frozen Japanese) - list them
rem_kana={}
for pg,v in fd["pages"].items():
    lst=[s["text"] for s in v["removed_strings"] if re.search(r'[\u3040-\u30ff]', s["text"])]
    rem_kana[pg]=lst
out["removed_with_kana"]=rem_kana
# added strings containing CJK
add_cjk={}
for pg,v in fd["pages"].items():
    lst=[s["text"] for s in v["added_strings"] if cjk_runs(s["text"])]
    add_cjk[pg]=lst
out["added_with_cjk"]=add_cjk
# word-level: every CJK run in EDITION full text that is NOT a substring of core full text
core_full={pg:"".join(t["text"] for t in texts_of(CORE/fn)) for pg,fn in FILES.items()}
ed_full={pg:"".join(t["text"] for t in texts_of(ED/fn)) for pg,fn in FILES.items()}
word_new={}
for pg in FILES:
    cf=core_full[pg]
    runs=set()
    for t in texts_of(ED/FILES[pg]):
        for r in cjk_runs(t["text"]):
            if len(r)>=1 and r not in cf: runs.add(r)
    word_new[pg]=sorted(runs)
out["cjk_runs_not_in_core_page"]=word_new
# simplified-only codepoints in edition texts (chars whose JP form differs)
SIMP_ONLY=set("为说话语对发让见读这个们还电车马门问现实义头龙汉认识观点发际动劳务肃胁胆脑肠肤脚脸阴阳")
simp={}
for pg,fn in FILES.items():
    chars=sorted(set(ch for t in texts_of(ED/fn) for ch in t["text"] if ch in SIMP_ONLY))
    simp[pg]=chars
out["simplified_only_chars"]=simp
# sentence-final 。 integrity: core strings ending with 。 that are NOT in removed set must be in edition
# (use multiset comparison)
for pg,fn in FILES.items():
    cc=Counter(t["text"] for t in texts_of(CORE/fn)); ec=Counter(t["text"] for t in texts_of(ED/fn))
    missing=[]
    for s,c in cc.items():
        if s.endswith("。") and ec.get(s,0)<c: missing.append((s,c,ec.get(s,0)))
    out.setdefault("final_maru_missing",{})[pg]=missing
# ---- 4. P1 trend widths ----
sys.path.insert(0, str(B/"hidden_files/weekly-report-w45-ja-en-build"))
import svglib
trend={}
for t in texts_of(ED/"p1-hyoushi.svg"):
    if t["text"] in ("Dates in articles; not exact statistics","These four topics shape this issue."):
        kind="serif" if "Serif" in t["fam"] else "sans"
        w=svglib.text_w(t["text"], kind, t["bold"], float(t["size"]))
        trend[t["text"]]={"x":t["x"],"y":t["y"],"size":t["size"],"anchor":t["anchor"],"width_px":round(w,1)}
out["p1_trend_widths"]=trend
# trend box rects on P1: rects near those y
t1=raw(ED/"p1-hyoushi.svg")
rects=re.findall(r'<rect[^>]*>', t1)
out["p1_rects_near_trend"]=[r for r in rects if any(str(y) in r for y in ("122"))][:10]
# ---- 5. counts via SVG: standalone number labels + level chips ----
counts={}
for pg,fn in FILES.items():
    ts=texts_of(ED/fn)
    nums=[]; chips=[]
    for i,t in enumerate(ts):
        if re.fullmatch(r"\d+\.", t["text"]): nums.append(int(t["text"][:-1]))
        if t["text"] in ("A2","B1","B2") and t["bold"]:
            chips.append(t["text"])
    counts[pg]={"numbers":nums,"n_numbers":len(nums),"chips":dict(Counter(chips))}
out["svg_counts"]=counts
# ---- 6. P7 phrases + tags ----
def dump_page(d,pg):
    return texts_of(d/FILES[pg])
# find P7 phrases section: texts containing 'Phrases' in ed, and core equivalent region by y
p7ed=texts_of(ED/"p7-kotoba.svg"); p7co=texts_of(CORE/"p7-kotoba.svg")
out["p7_ed_phrase_region"]=[t for t in p7ed if "Phrases" in t["text"] or "phrase" in t["text"].lower()]
# dump all P7 ed texts y>=1700 and core y>=1700
out["p7_ed_y1700"]=[(t["x"],t["y"],t["text"]) for t in p7ed if t["y"]>=1700]
out["p7_co_y1700"]=[(t["x"],t["y"],t["text"]) for t in p7co if t["y"]>=1700]
# phrase counting: blank-stripped full issue concatenation, for each candidate quote
# candidate quotes = P7 phrase list entries: lines in phrase region that are Japanese quoted sentences.
# Instead: take core P7 phrase quotes from KIT-independent source: phrases are the 8 quoted sentences
# appearing in P7 list; identify by region: after header containing 'Phrases' until 'Readers' text.
def phrase_entries(ts):
    idx=[i for i,t in enumerate(ts) if "Phrases of the week" in t["text"]]
    if not idx: return []
    start=idx[0]
    entries=[]
    for t in ts[start+1:]:
        if "Readers" in t["text"] or "Next issue" in t["text"]: break
        entries.append(t)
    return entries
out["p7_ed_phrase_entries"]=[(t["x"],t["y"],t["text"]) for t in phrase_entries(p7ed)]
# full-issue blank-stripped text
def full_blank(d):
    s=""
    for pg,fn in FILES.items():
        s+="".join(t["text"] for t in texts_of(d/fn))
    return re.sub(r"\s+","",s)
ed_blank=full_blank(ED); co_blank=full_blank(CORE)
out["p7_ed_phrase_entries_text"]=[t["text"] for t in phrase_entries(p7ed)]
# quote counting needs the quote strings themselves (Japanese sentences inside entries).
# Entries are wrapped lines; join consecutive lines per entry is hard from SVG alone.
# Use build content7? No - use freeze: P7 phrases are verbatim quotes from articles; count via
# known quote fragments extracted from entries joined: join all phrase-entry texts, then split by 'p.' tags?
out["p7_phrase_joined"]= "".join(t["text"] for t in phrase_entries(p7ed))
# ---- 7. gloss ----
def gloss_blocks(ts, prefix):
    blocks=[]; cur=None
    for t in ts:
        if t["text"].startswith(prefix):
            if cur: blocks.append(cur)
            cur=[t]
        elif cur is not None and t["x"]==cur[0]["x"] and t["size"]==cur[0]["size"] and not t["bold"]:
            # continuation only if y close and next is not a header: heuristic - same x/size/fill
            if t["fill"]==cur[0]["fill"]:
                cur.append(t)
            else:
                blocks.append(cur); cur=None
        else:
            if cur: blocks.append(cur); cur=None
    if cur: blocks.append(cur)
    return [" ".join(x["text"] for x in b) for b in blocks]
gloss={}
for pg in ["p1","p2","p3","p4","p5","p6"]:
    co=gloss_blocks(texts_of(CORE/FILES[pg]),"译注｜")
    ed=gloss_blocks(texts_of(ED/FILES[pg]),"Note — ")
    def items(blocks):
        res=[]
        for b in blocks:
            body=b.split("｜",1)[-1].split("—",1)[-1] if "｜" in b or "—" in b else b
            # split on middle dot
            parts=[p.strip() for p in body.split("·")]
            res.append(parts)
        return res
    gloss[pg]={"core_blocks":co,"ed_blocks":ed,"core_items":items(co),"ed_items":items(ed)}
out["gloss_p1_p6"]=gloss
# P7 column vocab lines: font 20.5, fill #57523f, containing middle dot, y before first exercise chip in column
# Simpler: dump all P7 lines with '·' and size 20.5 for manual identification
out["p7_dot_lines_ed"]=[(t["x"],t["y"],t["text"]) for t in p7ed if "·" in t["text"] and t["size"]=="20.5"]
out["p7_dot_lines_co"]=[(t["x"],t["y"],t["text"]) for t in p7co if "·" in t["text"] and t["size"]=="20.5"]
# ---- 8. P8 keys raw lines ----
def p8_answer_lines(d):
    ts=texts_of(d/"p8-tesuto.svg")
    # answer section starts after a text containing 'Answers' header; keys are texts matching ^\d+\. 
    lines={}
    for t in ts:
        m=re.match(r"^(\d+)\.\s+(.*)$", t["text"])
        if m: lines.setdefault(int(m.group(1)),[]).append(m.group(2))
    return lines, ts
co_lines,co_ts=p8_answer_lines(CORE); ed_lines,ed_ts=p8_answer_lines(ED)
out["p8_answer_line_counts"]={"core":len(co_lines),"ed":len(ed_lines)}
keydiff_detail={}
for n in sorted(set(co_lines)|set(ed_lines)):
    c=" ".join(co_lines.get(n,[])); e=" ".join(ed_lines.get(n,[]))
    if c!=e: keydiff_detail[n]={"core":c,"ed":e}
out["p8_keydiff_printed"]=keydiff_detail
# P8 notes pure English: note part after ' — ' or ' (' in answer lines: check CJK in note part
def note_part(s):
    if " — " in s: return s.split(" — ",1)[1]
    m=re.search(r"\(([^)]*)\)\s*$", s)
    return m.group(1) if m else ""
note_cjk={}
for n,parts in ed_lines.items():
    s=" ".join(parts); np=note_part(s)
    if cjk_runs(np): note_cjk[n]=(s,np)
out["p8_ed_note_cjk"]=note_cjk
# P8 note set equality via p8.py extract already; also raw: numbers with notes
# ---- 9. essay ----
def find_essay(ts):
    # model text section H: find text '私の11月の週末' then following paragraph texts until footer-ish
    idx=[i for i,t in enumerate(ts) if "私の11月の週末" in t["text"]]
    return idx
out["essay_title_idx_ed"]=find_essay(p7ed)  # placeholder, real below
for label,d in [("core",CORE),("ed",ED)]:
    ts=texts_of(d/"p8-tesuto.svg")
    idx=find_essay(ts)
    seg=[]
    if idx:
        i=idx[0]
        for t in ts[i+1:i+30]:
            seg.append(t["text"])
            if "Lucerna ·" in t["text"] or "Page 8" in t["text"] or "第 8 版" in t["text"]: break
    out[f"essay_seg_{label}"]=seg
# ---- 10. abstract ----
ab=(B/"files/weekly-report-w45-ja-en/ABSTRACT.txt").read_text()
out["abstract"]={"raw":ab,"lines":ab.count("\n"),"has_ascii_quote":'"' in ab,"chars":len(ab)}
# ---- 11. images ----
def img_hashes(d):
    res={}
    for pg,fn in FILES.items():
        t=raw(d/fn)
        hs=[]
        for m in re.finditer(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', t):
            hs.append(hashlib.sha256(m.group(1).encode()).hexdigest()[:12])
        res[pg]=hs
    return res
out["images"]={"core":img_hashes(CORE),"ed":img_hashes(ED)}
# credits: texts containing 出典 or artist names
def credits(d):
    res={}
    for pg,fn in FILES.items():
        res[pg]=[t["text"] for t in texts_of(d/fn) if "出典" in t["text"] or "Poliphilo" in t["text"] or "Syced" in t["text"] or "Kratochvil" in t["text"] or "広重" in t["text"] or "Commons" in t["text"]]
    return res
out["credits"]={"core":credits(CORE),"ed":credits(ED)}
# ---- 12. furniture measurements P1 ----
def mast(d):
    ts=texts_of(d/"p1-hyoushi.svg")
    m={}
    for t in ts:
        if t["text"]=="Lucerna" and t["size"]=="168": m["wordmark_y"]=t["y"]
        if "VOL.2" in t["text"] and "日本語版" in t["text"]: m["subtitle"]=(t["y"],t["size"],t["text"])
        if "EXPLANATIONS IN ENGLISH" in t["text"] or "中文讲解" in t["text"] or "EXPLANATIONS" in t["text"]: m["badge"]=(t["y"],t["size"],t["text"])
        if "週刊新聞" in t["text"] or "周报" in t["text"] or "for readers" in t["text"].lower(): m["strapline_candidate"]=(t["y"],t["text"])
    # strapline: the text at y~390 in ed, y~372 core? take texts y in 360-400 excluding badge
    m["texts_350_400"]=[(t["y"],t["size"],t["text"]) for t in ts if 350<=t["y"]<=400]
    # rules: line elements y
    t_raw=raw(d/"p1-hyoushi.svg")
    m["lines_y"]=[mm.group(0)[:120] for mm in re.finditer(r'<line[^>]*>', t_raw)][:20]
    m["rects_top"]=[mm.group(0)[:160] for mm in re.finditer(r'<rect[^>]*>', t_raw)][:12]
    # footers all pages
    return m
out["mast"]={k:mast(d) for k,d in [("w43",W43),("core",CORE),("ed",ED)]}
def footers(d):
    res={}
    for pg,fn in FILES.items():
        ts=texts_of(d/fn)
        res[pg]=[t["text"] for t in ts if "Lucerna ·" in t["text"] or "Page " in t["text"] or "共 8 版" in t["text"] or "第 " in t["text"] and "版" in t["text"]]
    return res
out["footers"]={k:footers(d) for k,d in [("w43",W43),("core",CORE),("ed",ED)]}
# P8 separators + headers
def p8furn(d):
    ts=texts_of(d/"p8-tesuto.svg")
    return [t["text"] for t in ts if t["text"].startswith("— ") and t["text"].endswith(" —") or "Test and answers" in t["text"] or "练习与答案" in t["text"] or "Answers —" in t["text"] or "答案" in t["text"]]
out["p8_furn"]={k:p8furn(d) for k,d in [("w43",W43),("core",CORE),("ed",ED)]}
# instruction + type sets: exercise header instruction texts (texts after number labels, size 19.5, non-bold? ) - collect distinct short EN/ZH instruction strings from P1-P8
def instr(d):
    s=set()
    for pg,fn in FILES.items():
        for t in texts_of(d/fn):
            if t["size"]=="19.5" and len(t["text"])<=30: s.add(t["text"])
    return sorted(s)
out["instr_19p5"]={k:instr(d) for k,d in [("w43",W43),("core",CORE),("ed",ED)]}
# band subtitles: P2-P8 band texts (dark band header lines) - first texts per page
def bands(d):
    res={}
    for pg,fn in FILES.items():
        ts=texts_of(d/fn)
        res[pg]=[t["text"] for t in ts[:4]]
    return res
out["bands_first4"]={k:bands(d) for k,d in [("w43",W43),("core",CORE),("ed",ED)]}
# P7 teaser: bottom rects/lines
for label,d in [("ed",ED),("core",CORE)]:
    t_raw=raw(d/"p7-kotoba.svg")
    rects=[]
    for m in re.finditer(r'<rect[^>]*>', t_raw):
        mm=re.search(r'y="([\d.]+)"', m.group(0)); hh=re.search(r'height="([\d.]+)"', m.group(0))
        if mm and hh and float(mm.group(1))>2000: rects.append((m.group(0)[:180], float(mm.group(1)), float(hh.group(1)), float(mm.group(1))+float(hh.group(1))))
    out[f"p7_bottom_rects_{label}"]=rects
    lines=[m.group(0)[:140] for m in re.finditer(r'<line[^>]*>', t_raw) if '2580' in m.group(0) or '2540' in m.group(0)]
    out[f"p7_footer_lines_{label}"]=lines
    ts=texts_of(d/"p7-kotoba.svg")
    out[f"p7_max_text_y_{label}"]=max(t["y"] for t in ts if "Page 7" not in t["text"] and "Lucerna ·" not in t["text"])
    out[f"p7_texts_y2400_{label}"]=[(t["y"],t["text"]) for t in ts if t["y"]>=2400]
json.dump(out, open(PROOF/"proof.json","w"), ensure_ascii=False, indent=1)
print("written proof.json")
for k in ["forbidden_svg-ed","forbidden_kit","forbidden_abstract"]:
    print(k, out[k])
print("kinsoku counts", {k:v[0] for k,v in out["kinsoku"].items()})
print("freeze", out["freeze_pages"])
print("svg_counts", {k:(v["n_numbers"],v["chips"]) for k,v in out["svg_counts"].items()})
print("p1_trend", out["p1_trend_widths"])
print("p8_keydiff_n", sorted(out["p8_keydiff_printed"].keys()))
print("p8_note_cjk", out["p8_ed_note_cjk"])
print("abstract", out["abstract"])
print("images", out["images"])
