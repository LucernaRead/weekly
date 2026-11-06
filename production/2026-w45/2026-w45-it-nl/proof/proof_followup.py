#!/usr/bin/env python3
import html, os, re, sys
from PIL import ImageFont
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-nl-proof"))
from proof_audit import parse, ink, adv_right, font, fnum, ED, CO, D
def P(s): print(s, flush=True)

# --- 1. right-edge discrepancy: the 5 lines, both methods + ink ---
P("===== F1 right-edge lines: attrs + builder-advance + my-advance + ink-right =====")
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-it-nl-build"))
from svglib import _font as bfont
targets = [("p1-prima.svg", 1728.0), ("p1-prima.svg", 1758.0), ("p2-vita.svg", 1927.0), ("p2-vita.svg", 2195.0), ("p8-valutazione.svg", 663.0)]
for fn, yy in targets:
    els, _ = parse(os.path.join(ED, "svg", fn))
    for e in els:
        if e["kind"] == "text" and abs(fnum(e["a"], "y") - yy) < 0.01:
            a = e["a"]; t = e["text"]
            kind = 'serif' if 'Serif' in a.get("font-family", "") else 'sans'
            bold = a.get("font-weight", "") in ("700", "bold")
            b_adv = bfont(kind, bold, int(round(float(a.get("font-size", "20"))))).getlength(t)
            x = fnum(a, "x"); anc = a.get("text-anchor", "start")
            b_edge = x + b_adv if anc == "start" else (x if anc == "end" else x + b_adv/2)
            ib = ink(e)
            P(f"  {fn} y={yy} attrs={a} :: {t!r}")
            P(f"    builder-advance-right={b_edge:.1f} my-advance-right={adv_right(e):.1f} ink-right={ib[2]:.1f} ink-box={tuple(round(v,1) for v in ib[:4])}")

# --- 2. badge ink clearance ---
P("\n===== F2 badge ink clearance (ED) =====")
els, _ = parse(os.path.join(ED, "svg", "p1-prima.svg"))
for e in els:
    if e["kind"] == "text" and e["text"].startswith("TEKSTEN IN HET ITALIAANS"):
        b = ink(e); P(f"  badge ink={tuple(round(v,1) for v in b[:4])} adv={b[4]:.1f}")
        P(f"  clearance to rule y=392 (stroke 3 -> top edge 390.5): {390.5 - b[3]:.1f}px; to frame line 1885: right ink {b[2]:.1f}")
    if e["kind"] == "line" and fnum(e["a"], "y1") in (392.0, 401.0):
        P(f"  rule line: {e['a']}")

# --- 3. golden sentences proper ---
P("\n===== F3 golden sentences (FRASI block) =====")
els, _ = parse(os.path.join(ED, "svg", "p7-lingua.svg"))
texts = [(fnum(e["a"], "y"), e["text"]) for e in els if e["kind"] == "text"]
frasi_i = next(i for i, (y, t) in enumerate(texts) if t.startswith("FRASI DELLA SETTIMANA"))
P(f"  FRASI title at y={texts[frasi_i][0]}")
gold = []
for y, t in texts[frasi_i+1:]:
    if t.startswith("LA PROSSIMA") or t.startswith("LETTERE"): break
    if t.startswith("«") or (len(t) > 10 and "Pagina" not in t):
        gold.append(t)
for g in gold: P(f"  FRASI node: {g!r}")
# article pages: search P1..P6 joined text (space-joined + raw-concat variants) for stripped sentence
def stripq(s): return s.strip("«»").strip()
for g in gold:
    core_s = stripq(g)
    # also without trailing punctuation variants
    found = []
    for pg in range(1, 7):
        elsx, _ = parse(os.path.join(ED, "svg", sorted(os.listdir(os.path.join(ED, "svg")))[pg-1]))
        joined = " ".join(e["text"] for e in elsx if e["kind"] == "text")
        if core_s in joined: found.append(pg)
        elif core_s.rstrip(".!") in joined: found.append(f"{pg}(nopunct)")
    # total occurrences across all 8 pages (joined, stripped form)
    tot = 0
    for fn in sorted(os.listdir(os.path.join(ED, "svg"))):
        elsx, _ = parse(os.path.join(ED, "svg", fn))
        joined = " ".join(e["text"] for e in elsx if e["kind"] == "text")
        tot += joined.count(core_s)
    P(f"  GOLD {core_s!r} article-pages={found} total-occurrences(joined)={tot}")

# --- 4. definition sentence exact ---
P("\n===== F4 definition sentence exact =====")
def defonly(d):
    els, _ = parse(os.path.join(d, "svg", "p7-lingua.svg"))
    seq = [e["text"] for e in els if e["kind"] == "text"]
    txt = " ".join(seq)
    i = txt.find("« l'assaggio »")
    j = txt.find("alla finale del Panettone.", i)
    return txt[i:j+len("alla finale del Panettone.")]
dc, de = defonly(CO), defonly(ED)
P(f"  CORE: {dc!r}")
P(f"  ED  : {de!r}")
P(f"  identical: {dc == de}")

# --- 5. letter verbatim ---
P("\n===== F5 letter verbatim =====")
def letter(d):
    els, _ = parse(os.path.join(d, "svg", "p7-lingua.svg"))
    seq = [e["text"] for e in els if e["kind"] == "text"]
    txt = " ".join(seq)
    i = txt.find("«Ciao! Sono Li")
    j = txt.find("— Li", i)
    return txt[i:j+len("— Li")] if i >= 0 else "NOT-FOUND"
lc, le = letter(CO), letter(ED)
P(f"  CORE: {lc!r}")
P(f"  ED  : {le!r}")
P(f"  identical: {lc == le}")

# --- 6. exercise markers on P1-P7 ---
P("\n===== F6 exercise markers =====")
for d, label in [(CO, "CORE"), (ED, "EDITION")]:
    P(f"  -- {label} --")
    for fn in sorted(os.listdir(os.path.join(d, "svg"))):
        if not fn.endswith(".svg"): continue
        els, _ = parse(os.path.join(d, "svg", fn))
        # nodes that are pure level chips or number badges: 'A2'/'B1'/'B2' alone, or digits alone, or 'N.' 
        chips = [e["text"] for e in els if e["kind"] == "text" and e["text"].strip() in ("A2", "B1", "B2")]
        nums = [e["text"] for e in els if e["kind"] == "text" and re.fullmatch(r"\d+\.", e["text"].strip())]
        ndot = [e["text"] for e in els if e["kind"] == "text" and re.match(r"^\d+\.\s", e["text"])]
        P(f"    {fn}: level-chip-nodes={len(chips)} ({dict(__import__('collections').Counter(chips))}) bare-number-nodes={len(nums)} N.-lines={len(ndot)}")
