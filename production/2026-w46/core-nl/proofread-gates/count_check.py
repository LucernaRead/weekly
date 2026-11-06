import re, glob, os, json, collections
F="/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
PAGES=["p1-voorpagina.svg","p2-leven.svg","p3-cultuur.svg","p4-sport.svg","p5-jongeren.svg","p6-verdieping.svg","p7-taal.svg","p8-toets.svg"]
def svg_texts(path):
    data=open(path,encoding="utf-8").read()
    return [re.sub(r"<[^>]+>","",t).strip() for t in re.findall(r"<text[^>]*>(.*?)</text>", data, re.S)]
results={}
for ed in ["core","de","en","es","fr","it","ja","ko","pt","ru","zh-tw"]:
    D=f"{F}/weekly-report-w46-nl-{ed}"
    slug="2026-w46-nl-zh-cn" if ed=="core" else f"2026-w46-nl-{ed}"
    md=glob.glob(f"{D}/*.text.md")[0]
    lines=open(md,encoding="utf-8").read().splitlines()
    # per-page via Pagina headers
    cur=None; per_page=collections.Counter(); levels=collections.Counter(); nums=[]
    item_re=re.compile(r"^(\d+)\.\s*\[(A2|B1|B2)\s*[·•]\s*([^\]]+)\]")
    types=collections.Counter()
    for ln in lines:
        m=re.match(r"^## Pagina (\d+)\s*$", ln)
        if m: cur=int(m.group(1)); continue
        m=item_re.match(ln.strip())
        if m:
            n=int(m.group(1)); nums.append(n); levels[m.group(2)]+=1; types[m.group(3).strip()]+=1
            if cur: per_page[cur]+=1
    # SVG stem recount: exact "N." elements
    svg_per_page={}; svg_levels=collections.Counter(); svg_nums=[]
    for i,pg in enumerate(PAGES,1):
        ts=svg_texts(f"{D}/svg/{pg}")
        stems=[t for t in ts if re.fullmatch(r"\d+\.", t)]
        svg_per_page[i]=len(stems)
        svg_nums+= [int(s[:-1]) for s in stems]
        # level tags: bare A2/B1/B2 elements (exclude headings containing '·' and 'Leesniveau' lines and ranges like A2→B1)
        for t in ts:
            if t in ("A2","B1","B2"): svg_levels[t]+=1
    results[ed]={
      "slug":slug, "textmd_file": os.path.basename(md),
      "textmd_total": len(nums), "textmd_nums_sorted": sorted(nums)==list(range(1,151)),
      "textmd_missing": sorted(set(range(1,151))-set(nums)), "textmd_dupes": sorted([n for n,c in collections.Counter(nums).items() if c>1]),
      "textmd_per_page": dict(sorted(per_page.items())), "textmd_levels": dict(levels), "textmd_types": dict(types),
      "svg_stem_total": len(svg_nums), "svg_stem_sorted": sorted(svg_nums)==list(range(1,151)),
      "svg_missing": sorted(set(range(1,151))-set(svg_nums)), "svg_dupes": sorted([n for n,c in collections.Counter(svg_nums).items() if c>1]),
      "svg_per_page": svg_per_page, "svg_level_tags": dict(svg_levels),
    }
    print(f"== {slug} ==")
    print(" text.md total", len(nums), "contig1-150:", results[ed]["textmd_nums_sorted"], "missing:", results[ed]["textmd_missing"], "dupes:", results[ed]["textmd_dupes"])
    print("  per_page", dict(sorted(per_page.items())), "levels", dict(levels))
    print("  types", dict(types))
    print(" svg stems total", len(svg_nums), "contig:", results[ed]["svg_stem_sorted"], "missing:", results[ed]["svg_missing"], "dupes:", results[ed]["svg_dupes"])
    print("  svg per_page", svg_per_page, "level tags", dict(svg_levels))
json.dump(results, open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/nl-proofread-gates/counts.json","w"), ensure_ascii=False, indent=1)
print("WROTE counts.json")
