# -*- coding: utf-8 -*-
"""Round 2 independent verification: text-layer checks on shipped SVGs. Read-only."""
import html, os, re, sys, json
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(BASE, "files")
OUT = os.path.join(BASE, "hidden_files/w46/it-proofread-gates-round2")
CODES = ["core","de","en","es","fr","ja","ko","nl","pt","ru","zh-tw"]
DIRMAP = {"core":"weekly-report-w46-it-core","de":"weekly-report-w46-it-de","en":"weekly-report-w46-it-en",
 "es":"weekly-report-w46-it-es","fr":"weekly-report-w46-it-fr","ja":"weekly-report-w46-it-ja",
 "ko":"weekly-report-w46-it-ko","nl":"weekly-report-w46-it-nl","pt":"weekly-report-w46-it-pt",
 "ru":"weekly-report-w46-it-ru","zh-tw":"weekly-report-w46-it-zh-tw"}
PAGES = ["p1-prima.svg","p2-vita.svg","p3-cultura.svg","p4-sport.svg","p5-giovani.svg","p6-approfondimento.svg","p7-lingua.svg","p8-valutazione.svg"]

def texts(eddir, fname):
    s = open(os.path.join(eddir,"svg",fname), encoding="utf-8").read()
    out=[]
    for m in re.finditer(r"<text[^>]*>(.*?)</text>", s, re.S):
        t = html.unescape(re.sub(r"<[^>]+>","", m.group(1))).strip()
        if t: out.append(t)
    return out, s

def joined(eddir, fname):
    t,_ = texts(eddir, fname); return " ".join(t)
def alljoined(eddir):
    return " ".join(joined(eddir,f) for f in PAGES)
def raw(eddir, fname):
    return open(os.path.join(eddir,"svg",fname), encoding="utf-8").read()

report=[]
def line(s): report.append(s); print(s)

for code in CODES:
    ed = os.path.join(FILES, DIRMAP[code])
    line(f"\n===== {code} ({DIRMAP[code]}) =====")
    p1,p2,p4,p7,p8 = (joined(ed,f) for f in [PAGES[0],PAGES[1],PAGES[3],PAGES[6],PAGES[7]])
    allt = alljoined(ed)
    # D1
    line(f"D1 P1 'Pagina 2' count={p1.count('Pagina 2')} 'Pagina 5' count={p1.count('Pagina 5')}")
    for t in texts(ed,PAGES[0])[0]:
        if "FESTIVAL" in t or "Pagina" in t or "86 film" in t: line(f"  P1-line: {t!r}")
    # D3
    line(f"D3 P2 chiuso='{ 'si è chiuso il Forum Cultura' in p2 }' aperte={ 'si sono aperte la finale del Panettone' in p2 } old-chiusi={ 'si sono chiusi' in p2 } old-aperti={ 'si sono aperti la finale' in p2 }")
    for t in texts(ed,PAGES[1])[0]:
        if "Forum Cultura" in t or "finale del Panettone" in t: line(f"  P2-line: {t!r}")
    # D2 stems + P8 notes 56/57 raw lines
    line(f"D2 P4 NON count={p4.count('NON cominciano')}")
    for t in texts(ed,PAGES[3])[0]:
        if "cominciano" in t: line(f"  P4-stem: {t!r}")
    for t in texts(ed,PAGES[7])[0]:
        if re.match(r"^(56|57)\.", t.strip()): line(f"  P8-56/57: {t!r}")
    # Q1 evidence: every Perugia / finale occurrence with page
    for i,f in enumerate(PAGES,1):
        for t in texts(ed,f)[0]:
            if "Perugia" in t or "finale" in t.lower(): line(f"  P{i} finale/Perugia: {t!r}")
    line(f"Q1 'la finale è a Perugia' present={ 'la finale è a Perugia' in allt } ; 'la Festa del Torrone è a Cremona' in P7={ 'la Festa del Torrone è a Cremona' in p7 }")
    # 20:45 facts
    for i,f in enumerate(PAGES,1):
        for t in texts(ed,f)[0]:
            if "20.45" in t or "20:45" in t: line(f"  P{i} 20.45: {t!r}")
    # F1
    fw = allt.count("\uff1a")
    line(f"F1 U+FF1A total={fw} (per page: {[joined(ed,f).count(chr(0xFF1A)) for f in PAGES]})")
    # D5: P8 items 145-148
    for t in texts(ed,PAGES[7])[0]:
        if re.match(r"^(145|146|147|148)\.", t.strip()): line(f"  P8-145..148: {t!r}")
    # ko checks
    if code=="ko":
        kata = [c for c in allt if "\u30a0" <= c <= "\u30ff"]
        line(f"KO katakana chars={len(kata)} unique={sorted(set(kata))}")
        line(f"KO U+3002 count={allt.count(chr(0x3002))} ; correct name count={allt.count('스크리토린치타')} ; bad name count={allt.count('스크리토리ンチ타')}")
        for i,f in enumerate(PAGES,1):
            for t in texts(ed,f)[0]:
                if "스크리토" in t: line(f"  P{i} name: {t!r}")
    # zh-tw
    if code=="zh-tw":
        rawall = "".join(raw(ed,f) for f in PAGES)
        # count on de-tagged text without spaces to avoid split-node artefacts
        detagged = "".join(html.unescape(re.sub(r"<[^>]+>","",m.group(1))) for f in PAGES for m in re.finditer(r"<text[^>]*>(.*?)</text>", raw(ed,f), re.S))
        line(f"ZHTW 未來時 raw={rawall.count('未來時')} detagged={detagged.count('未來時')} ; 將來時 raw={rawall.count('將來時')} detagged={detagged.count('將來時')}")
        # orphan line-starts: text elements starting with CJK punctuation
        orphans=[]
        for i,f in enumerate(PAGES,1):
            for t in texts(ed,f)[0]:
                if t and t[0] in "、，。）】」』；：！？": orphans.append((i,t))
        line(f"ZHTW orphan line-starts={len(orphans)} {orphans[:10]}")
    # badge / footer
    p1texts = texts(ed,PAGES[0])[0]
    line(f"P1 first 6 texts: {p1texts[:6]}")
    foot=[]
    s8 = raw(ed,PAGES[7])
    # footer: text elements with y>=2600 - parse y attr
    for m in re.finditer(r'<text[^>]*\by="([\d.]+)"[^>]*>(.*?)</text>', raw(ed,PAGES[0]), re.S):
        if float(m.group(1))>=2580: foot.append(html.unescape(re.sub(r"<[^>]+>","",m.group(2))).strip())
    line(f"P1 footer texts (y>=2580): {foot}")
    # golden sentences
    gold=["tre giorni di sole dopo il primo freddo","il sole tornò a splendere","Il cinema che sceglie da che parte stare","Due notti azzurre, alle 20.45","arriva anche il Treno Storico Arlecchino","le due partite di questa settimana sono decisive","un libro in mano, un film negli occhi","approvato dal governo non vuol dire già legge"]
    norm = re.sub(r"\s+"," ", allt)
    line(f"Golden counts={[norm.count(g) for g in gold]}")
    # P7 disclosure dump (LETTERE box lines containing redazione / letters words)
    for t in texts(ed,PAGES[6])[0]:
        if any(k in t for k in ["redazione","Пока","К моменту","letter","Letter","brieven","lettres","cartas","手紙","편지","信"]): line(f"  P7-disclosure-cand: {t!r}")

# P7 B2 context dump for Q1 pedagogy (core + one fan-out representative: all, P7 only, lines near Cremona/Perugia/congiuntivo)
line("\n===== P7 B2 column context (all editions) =====")
for code in CODES:
    ed = os.path.join(FILES, DIRMAP[code])
    ts = texts(ed,PAGES[6])[0]
    for j,t in enumerate(ts):
        if "Cremona" in t and "Festa del Torrone" in t:
            ctx = ts[max(0,j-3):j+4]
            line(f"{code} P7 ctx: {ctx}")
            break

open(os.path.join(OUT,"verify-round2-text.txt"),"w",encoding="utf-8").write("\n".join(report)+"\n")
print("WROTE verify-round2-text.txt")
