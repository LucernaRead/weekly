# -*- coding: utf-8 -*-
"""Independent reproof checks for W45 zh-cn x pt. Read-only except writing
its own report output. Never imports a content module; sources are read
as text only."""
import re, json, hashlib, base64, glob, os, sys
from xml.etree import ElementTree as ET

B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_BUILD = f"{B}/hidden_files/weekly-report-w45-zhcn-build"
PT_BUILD = f"{B}/hidden_files/weekly-report-w45-zh-cn-pt-build"
ED = f"{B}/files/weekly-report-w45-zh-cn-pt"
CORE_ED = f"{B}/files/weekly-report-w45-zhcn-core"
W43 = f"{B}/files/weekly-report-zh-cn-pt"
TR = f"{B}/hidden_files/w45-zh-cn-pt-transform.py"
OUT = f"{B}/hidden_files/w45/zh-cn-pt-reproof/work/checks-out.txt"
log = open(OUT, "w", encoding="utf-8")
def p(*a):
    print(*a); print(*a, file=log)

def read(path):
    with open(path, encoding="utf-8") as fh: return fh.read()

def svg_texts(path):
    t = ET.parse(path); ns = "{http://www.w3.org/2000/svg}"
    out = []
    for el in t.iter():
        tag = el.tag.replace(ns, "")
        if tag == "text":
            txt = "".join(el.itertext())
            out.append((el.get("x"), el.get("y"), el.get("font-size"), el.get("font-weight"), el.get("font-family"), txt))
    return out

# --- Transform: 19 folded edits ---
tr = read(TR)
new19 = [
 "Vendas imediatas da JD.com: 12 de outubro.",
 "Pré-vendas do Taobao e do Tmall: 15 de outubro.",
 "Vendas imediatas do Taobao e do Tmall: 20 de outubro.",
 "A final: 15 de novembro, 03:00, hora de Pequim.",
 "24–25 de outubro: média de 2 espectadores por sessão.",
 "「最低价」 é propaganda, não dado medido.",
 "Dados e checkout primeiro; a manchete por último.",
 "Mercadorias imediatas: sem espera de sinal.",
 "Dia dos Jornalistas: 8 de novembro, não 7.",
 "shùzì — personagens digitais no filme de IA.",
 "Mercadorias imediatas: despacham na hora.",
 "Regra da página 6: dados primeiro.",
 "O tempo fica mais frio dia a dia depois do 立冬.",
 "Com o 直降 o preço do checkout é o que você paga.",
 "No 立冬 ela fez bolinhos com a mãe.",
 "tǎotài 淘汰 — eliminar, tirar do torneio · nèizhàn 内战 — um jogo entre dois times da mesma região · zhǐbù 止步 — parar aqui, não ir adiante.",
 "Datas e horas",
 "Foto: Based5290 — Domínio público (Wikimedia Commons)",
 "Cálculos",
]
old19 = [
 "As vendas imediatas da JD.com começaram em 12 de outubro.",
 "Horários e números", "Contas das cestas",
 "Depois do 立冬,", "Com o 直降,", "No 立冬, ela fez",
 "to knock out, to eliminate", "Public domain (Wikimedia Commons)",
]
p("== TRANSFORM folded edits ==")
for s in new19:
    p("NEW present:", s in tr, "|", s[:60])
for s in old19:
    p("OLD absent:", s not in tr, "|", s[:60])
p("transform sha:", hashlib.sha256(open(TR, "rb").read()).hexdigest())

# --- content8 lines 119-121 ---
for d, name in [(CORE_BUILD, "core"), (PT_BUILD, "pt")]:
    lines = read(f"{d}/content8.py").splitlines()
    p(f"content8 {name} L119-121:", [lines[i] for i in (118, 119, 120)])

# --- gloss split on · ---
def glosses(d):
    calls = []
    for fn in ["content12.py", "content34.py", "content56.py"]:
        src = read(f"{d}/{fn}")
        for m in re.finditer(r'\.gloss\("([^"]*)"\)', src):
            calls.append(m.group(1))
    return calls
gc, gp = glosses(CORE_BUILD), glosses(PT_BUILD)
p("== GLOSS == calls core/pt:", len(gc), len(gp))
pc = [len(s.split("·")) for s in gc]; pp = [len(s.split("·")) for s in gp]
p("per-call core:", pc, "total", sum(pc))
p("per-call pt:", pp, "total", sum(pp))
def heads(s):
    return [it.split(" — ")[0].strip() for it in s.split("·")]
p("headwords equal item-by-item:", all(heads(a) == heads(b) for a, b in zip(gc, gp)))
for a, b in zip(gc, gp):
    if heads(a) != heads(b): p("  HEAD MISMATCH:", heads(a), heads(b))
p("rendered Nota count in edition SVGs:", sum(read(f).count("Nota — ") for f in sorted(glob.glob(f"{ED}/svg/*.svg"))))
p("rendered 'Notes' count:", sum(read(f).count("Notes") for f in sorted(glob.glob(f"{ED}/svg/*.svg"))))

# --- P7 golden sentences ---
p("== P7 GOLDEN ==")
quotes = []
for m in re.finditer(r'\("([^"]+)", "([^"]+)", "([^"]+)"\)', read(f"{PT_BUILD}/content7.py")):
    if m.group(1).startswith("「"): quotes.append(m.groups())
p("PT quote rows:", len(quotes))
for q in quotes: p(" ", q)
core_src = "".join(read(f"{CORE_BUILD}/{fn}") for fn in ["content12.py", "content34.py", "content56.py"])
for zh, pt_tr, tag in quotes:
    bare = zh.strip("「」")
    p(" source-contiguous:", bare in core_src, "| rendered-in-P7-SVG:", bare.replace(",", "，") in read(f"{ED}/svg/p7-ciyu.svg") or bare in read(f"{ED}/svg/p7-ciyu.svg"), "|", bare, tag)
p(" P7 SVG contains all 8 PT translations:", all(t in read(f"{ED}/svg/p7-ciyu.svg") for _, t, _ in quotes))
p(" each phrase count in P7 SVG (joined text, comma-normalised):")
joined = "".join(t for *_, t in [(x, y, z, w, v, u) for x, y, z, w, v, u in svg_texts(f"{ED}/svg/p7-ciyu.svg")])
for zh, _, _ in quotes:
    bare = zh.strip("「」")
    p("  ", bare, "joined-count:", joined.count(bare) + joined.count(bare.replace(",", "，")))

# --- Images ---
p("== IMAGES ==")
credits_core = read(f"{CORE_BUILD}/assets/CREDITS.md")
p("core CREDITS.md:\n", credits_core[:2000])
for fn in ["locker.jpg", "valley.jpg", "frost.jpg", "dumplings.jpg", "lanparty.jpg", "popcorn.jpg"]:
    a = hashlib.md5(open(f"{CORE_BUILD}/assets/{fn}", "rb").read()).hexdigest()
    b = hashlib.md5(open(f"{PT_BUILD}/assets/{fn}", "rb").read()).hexdigest()
    p(f" asset {fn}: core==pt {a == b} md5 {a}")
# embedded payloads in edition SVGs vs core SVGs
def payloads(path):
    src = read(path); out = []
    for m in re.finditer(r'data:image/jpeg;base64,([A-Za-z0-9+/=]+)', src):
        out.append(hashlib.md5(base64.b64decode(m.group(1))).hexdigest())
    return out
for pg in ["p1-touiban", "p2-shenghuo", "p3-wenhua", "p4-tiyu", "p5-qingnian"]:
    ce = payloads(f"{CORE_ED}/svg/{pg}.svg"); ee = payloads(f"{ED}/svg/{pg}.svg")
    p(f" {pg}: core payloads {ce} edition payloads {ee} equal {ce == ee}")
for pg in ["p1-touiban", "p2-shenghuo", "p3-wenhua", "p4-tiyu", "p5-qingnian", "p6-shendu", "p7-ciyu", "p8-ceyan"]:
    src = read(f"{ED}/svg/{pg}.svg")
    creds = re.findall(r'Foto: [^<]*', src)
    if creds: p(f" {pg} credits:", creds)
p(" 'Public domain' occurrences in edition SVGs:", sum(read(f).count("Public domain") for f in sorted(glob.glob(f"{ED}/svg/*.svg"))))
p(" 'Domínio público' occurrences:", sum(read(f).count("Domínio público") for f in sorted(glob.glob(f"{ED}/svg/*.svg"))))

# --- Readers corner P7 ---
p("== READERS CORNER ==")
texts = svg_texts(f"{ED}/svg/p7-ciyu.svg")
disc = [t for t in texts if t[0] == "1473"]
p(" P7 x=1473 text nodes (count, y range):", len(disc), disc[0][1] if disc else None, disc[-1][1] if disc else None)
for t in disc: p("   ", t[1], repr(t[5][:80]))
inv = "Escreva-nos! Envie a sua carta em chinês — duas frases já bastam — e ela pode sair no próximo número."
joined7 = "".join(t[5] for t in texts)
p(" invitation verbatim in joined P7 text:", inv in joined7)
p(" 'Exemplo da redação' present:", "Exemplo da redação" in joined7)
p(" 'não é uma carta de verdade' present:", "não é uma carta de verdade" in joined7)
# col3/teaser rects: compare P7 svg rects core vs edition
def rects(path):
    return sorted(re.findall(r'<rect[^>]*>', read(path)))
rc, re_ = rects(f"{CORE_ED}/svg/p7-ciyu.svg"), rects(f"{ED}/svg/p7-ciyu.svg")
p(" P7 rect lists equal:", rc == re_)
if rc != re_:
    for a, b in zip(rc, re_):
        if a != b: p("   rect diff core:", a, " ed:", b)
    p("   rect counts:", len(rc), len(re_))

# --- Furniture badge measure ---
p("== FURNITURE BADGE ==")
def find_badge(path, needle):
    for t in svg_texts(path):
        if needle in t[5]: return t
    return None
core_badge = find_badge(f"{CORE_ED}/svg/p1-touiban.svg", "简体中文正文")
w43_badge = find_badge(f"{W43}/svg/p1-touiban.svg", "TEXTOS EM CHINÊS")
ed_badge = find_badge(f"{ED}/svg/p1-touiban.svg", "TEXTOS EM CHINÊS")
p(" core badge:", core_badge)
p(" W43 badge:", w43_badge)
p(" edition badge:", ed_badge)
p(" edition badge == W43 badge string:", ed_badge[5] == w43_badge[5] if ed_badge and w43_badge else False)
for label, path in [("core", CORE_ED), ("W43", W43), ("edition", ED)]:
    ts = svg_texts(f"{path}/svg/p1-touiban.svg")
    sub = [t for t in ts if t[1] == "330"]; strap = [t for t in ts if t[1] == "372"]; strip = [t for t in ts if t[1] == "92"]
    p(f" {label} y330:", sub); p(f" {label} y372:", strap); p(f" {label} y92:", strip)
    foot = sorted(set(t[5] for t in svg_texts(f"{path}/svg/p1-touiban.svg") if "Lucerna ·" in t[5] or "Lucerna·" in t[5]))
    p(f" {label} footer strings P1:", foot)
# footers all pages + page lines + P8 furniture
for pg in ["p1-touiban", "p2-shenghuo", "p3-wenhua", "p4-tiyu", "p5-qingnian", "p6-shendu", "p7-ciyu", "p8-ceyan"]:
    ts = svg_texts(f"{ED}/svg/{pg}.svg")
    foot = [t[5] for t in ts if t[1] == "2624"]
    p(f" {pg} y2624:", foot)
p(" edition P8 separators:", sorted(set(re.findall(r'— Página \d —', read(f"{ED}/svg/p8-ceyan.svg")))))
p(" edition P8 keys head present:", "答案 · Gabarito — por página, com uma nota em cada resposta" in read(f"{ED}/svg/p8-ceyan.svg"))
p(" edition P8 right line present:", "Todas as notas em português · ✓ = a tarefa de escrita" in read(f"{ED}/svg/p8-ceyan.svg"))
p(" W43 P8 separators:", sorted(set(re.findall(r'— Página \d —', read(f"{W43}/svg/p8-ceyan.svg")))))

# --- Non-blocking re-checks ---
p("== NON-BLOCKING RE-CHECKS ==")
for w in ["Complete a frase", "Escolha múltipla", "Escolha no contexto", "Associação", "Escrita"]:
    cnt = sum(read(f).count(w) for f in sorted(glob.glob(f"{ED}/svg/*.svg")))
    cnt43 = sum(read(f).count(w) for f in sorted(glob.glob(f"{W43}/svg/*.svg")))
    p(f" literal '{w}': edition {cnt} W43 {cnt43}")
# chip pattern: standalone chip texts like "25–28." ? count text nodes matching number patterns on P2-P6
for pg in ["p2-shenghuo", "p3-wenhua", "p4-tiyu", "p5-qingnian", "p6-shendu"]:
    for label, path in [("core", CORE_ED), ("W43", W43), ("ed", ED)]:
        ts = svg_texts(f"{path}/svg/{pg}.svg")
        chips = [t[5] for t in ts if re.fullmatch(r'\d+[–-]\d+\.', t[5].strip()) or re.fullmatch(r'\d+\.', t[5].strip())]
        p(f" {pg} {label} chip-like nodes: {len(chips)} {chips[:20]}")
        break
# P6 key-points box rect
for label, path in [("core", CORE_ED), ("ed", ED)]:
    src = read(f"{path}/svg/p6-shendu.svg")
    rects6 = re.findall(r'<rect x="527"[^>]*>', src)
    p(f" P6 x=527 rects {label}:", rects6)
    bars = re.findall(r'<rect x="325"[^>]*>', src)
    p(f" P6 x=325 bars {label}:", bars)
log.close()
print("WROTE", OUT)
