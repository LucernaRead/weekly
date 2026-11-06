import re, xml.etree.ElementTree as ET
F="/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
NS="{http://www.w3.org/2000/svg}"
HANGUL=re.compile(r"[\uac00-\ud7a3]")
def elements(ed,pg):
    tree=ET.parse(f"{F}/weekly-report-w46-nl-{ed}/svg/{pg}")
    out=[]
    for el in tree.getroot().iter(NS+"text"):
        out.append((float(el.get("x")), float(el.get("y")), float(el.get("font-size")), "".join(el.itertext()).strip()))
    return out
PAGES=["p1-voorpagina.svg","p2-leven.svg","p3-cultuur.svg","p4-sport.svg","p5-jongeren.svg","p6-verdieping.svg","p7-taal.svg","p8-toets.svg"]
print("===== KO: single-syllable final-line candidates (10-45 window analogue) =====")
print("Method: every <text> element whose stripped Korean content (letters+punct) has exactly 1 Hangul syllable,")
print("excluding exercise-number-only and level-tag elements; each adjudicated by neighbours (same x, y-step 10-45).")
for pi,pg in enumerate(PAGES,1):
    els=elements("ko",pg)
    for idx,(x,y,fs,t) in enumerate(els):
        syl=HANGUL.findall(t)
        core=t.strip()
        if len(syl)==1 and core not in ("A2","B1","B2") and not re.fullmatch(r"\d+\.", core):
            # neighbours
            prev=els[idx-1] if idx>0 else None
            nxt=els[idx+1] if idx+1<len(els) else None
            print(f"P{pi} x={x} y={y} fs={fs} {t!r} | prev={prev[3][:60]!r} y={prev[1]} | next={nxt[3][:60]!r} y={nxt[1]}")
print()
print("===== KO: line-START orphan punctuation (lines starting with ) . , etc after Korean wrap) =====")
for pi,pg in enumerate(PAGES,1):
    els=elements("ko",pg)
    for x,y,fs,t in els:
        if t.startswith((")", ")", ".", ",", "?", "!", ":", ";")) and HANGUL.search(t):
            print(f"P{pi} x={x} y={y} {t[:100]!r}")
print()
print("===== KO: mid-word splits with >=3-syllable tail (heuristic: line ends mid-word + next line starts with >=3 syllables before space/punct) =====")
# A wrapped Korean line ending without space/punct followed by next line (same col, y+10..45) starting with >=3 syllables then space/end
for pi,pg in enumerate(PAGES,1):
    els=sorted(elements("ko",pg), key=lambda e:(e[0],e[1]))
    for a,b in zip(els, els[1:]):
        if abs(a[0]-b[0])<3 and 10<=b[1]-a[1]<=45:
            ta, tb = a[3], b[3]
            if ta and not ta.endswith((" ",".",",","?","!",")","」","。","、","·","—","–",":",";")) and HANGUL.search(ta) and HANGUL.search(tb):
                # tail: syllables at start of tb before first space or punct
                m=re.match(r"^([\uac00-\ud7a3]+)", tb)
                if m and len(m.group(1))>=3:
                    print(f"P{pi} y={a[1]}->{b[1]} tail={m.group(1)!r} :: {ta[-30:]!r} / {tb[:40]!r}")
print()
print("===== JA kinsoku: lines starting with closers =====")
CLOSERS="、。」「』）》〉.,!?%:;\"'・"
for pi,pg in enumerate(PAGES,1):
    els=elements("ja",pg)
    for x,y,fs,t in els:
        if t and t[0] in CLOSERS:
            print(f"P{pi} x={x} y={y} {t[:110]!r}")
print("(end kinsoku scan)")
print()
print("===== ZH-TW: lines starting with closers (same kinsoku-style check) =====")
for pi,pg in enumerate(PAGES,1):
    els=elements("zh-tw",pg)
    for x,y,fs,t in els:
        if t and t[0] in CLOSERS:
            print(f"P{pi} x={x} y={y} {t[:110]!r}")
print("(end zh-tw scan)")
