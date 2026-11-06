# -*- coding: utf-8 -*-
"""Web-PDF vs cards comparison + independent Traditional-residue screens.
Part W: pypdf page counts/sizes; web PDF embedded JPEGs vs cards resized
  to 1400w (mean abs diff, % pixels differing >30).
Part R: (a) OpenCC s2t over edition visible text (changed pairs);
  (b) per-char s2t-invariance of the edition Han set;
  (c) builder-170 reproduction (transform MAPs + frozen strings) + scan;
  (d) W43-union + zhtw-core cross-check of edition-only chars;
  (e) mainland-vocab union scan; (f) P8-note residue scan."""
import re, os, json, io
from collections import Counter
from PIL import Image
from pypdf import PdfReader

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
EDD = os.path.join(GOAL, "files/weekly-report-w45-ko-zh-tw")
ED = os.path.join(EDD, "svg")
W43 = os.path.join(GOAL, "files/weekly-report-ko-zh-tw/svg")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ko-core/svg")
ZHTW_CORE = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")
PAGES = ["p1-pyoji", "p2-saenghwal", "p3-munhwa", "p4-seupocheu",
         "p5-cheongnyeon", "p6-gipi", "p7-mal", "p8-siheom"]
R = {}
# ---- W: PDFs ----
for name, path in (("print", os.path.join(EDD, "Lucerna-VOL2-ZHTW.pdf")),
                   ("web", os.path.join(EDD, "Lucerna-VOL2-ZHTW-web.pdf"))):
    rd = PdfReader(path)
    R[f"pdf_{name}"] = dict(pages=len(rd.pages),
        sizes=[(float(p.mediabox.width), float(p.mediabox.height)) for p in rd.pages],
        bytes=os.path.getsize(path))
web = PdfReader(os.path.join(EDD, "Lucerna-VOL2-ZHTW-web.pdf"))
comp = {}
for i, pg in enumerate(PAGES):
    page = web.pages[i]
    imgs = list(page.images)
    assert len(imgs) == 1, (pg, len(imgs))
    im = Image.open(io.BytesIO(imgs[0].data)).convert("RGB")
    card = Image.open(os.path.join(EDD, "cards", pg + ".png")).convert("RGB")
    card1400 = card.resize((1400, int(card.height * 1400 / card.width)), Image.LANCZOS)
    assert im.size == card1400.size, (pg, im.size, card1400.size)
    from PIL import ImageChops, ImageStat
    diff = ImageChops.difference(im, card1400)
    mean_abs = sum(ImageStat.Stat(diff).mean) / 3.0
    masks = [ch.point(lambda v: 255 if v > 30 else 0) for ch in diff.split()]
    m = masks[0]
    for mm in masks[1:]: m = ImageChops.lighter(m, mm)
    n = im.size[0] * im.size[1]
    pct = m.histogram()[255] / n * 100.0
    comp[pg] = dict(web_size=im.size, mean_abs_diff=round(float(mean_abs), 4),
                    pct_gt30_maxchannel=round(float(pct), 4))
R["web_vs_cards"] = comp

# ---- R: text helpers ----
import html
def parse_texts(path):
    s = open(path, encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
def han_set(d):
    s = set()
    for pg in PAGES:
        for t in parse_texts(os.path.join(d, pg + ".svg")):
            s |= set(ch for ch in t if "\u4e00" <= ch <= "\u9fff")
    return s
def visible_text(d):
    return "".join(t for pg in PAGES for t in parse_texts(os.path.join(d, pg + ".svg")))
E = han_set(ED); W = han_set(W43); C = han_set(CORE)
def han_set_any(d):
    s = set()
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            for t in parse_texts(os.path.join(d, fn)):
                s |= set(ch for ch in t if "\u4e00" <= ch <= "\u9fff")
    return s
Z = han_set_any(ZHTW_CORE) if os.path.isdir(ZHTW_CORE) else set()
R["han_sets"] = dict(edition=len(E), w43=len(W), core=len(C), zhtw_core=len(Z))
R["edition_only_vs_w43"] = sorted(E - W)
from opencc import OpenCC
cc = OpenCC("s2t")
ed_text = visible_text(ED)
conv = cc.convert(ed_text)
pairs = Counter()
for a, b in zip(ed_text, conv):
    if a != b: pairs[(a, b)] += 1
R["opencc_s2t_changed_pairs"] = {f"{a}->{b}": n for (a, b), n in pairs.items()}
# per-char s2t invariance over edition Han set
changed_chars = {}
for ch in sorted(E):
    out = cc.convert(ch)
    if out != ch: changed_chars[ch] = out
R["opencc_s2t_changed_edition_chars"] = changed_chars
# cross-check: edition-only chars attested in zhtw-core?
R["edition_only_attested_zhtw_core"] = sorted((E - W) & Z)
R["edition_only_unattested"] = sorted((E - W) - Z)
# builder-170 reproduction
import importlib.util as ilu
spec = ilu.spec_from_file_location("mytr", os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-zh-tw-build/transform.py"))
mytr = ilu.module_from_spec(spec); spec.loader.exec_module(mytr)
src_chars, dst_chars = set(), set()
for s_, d_ in mytr.MAP:
    src_chars |= set(s_); dst_chars |= set(d_)
w43_entries = None
try:
    spec2 = ilu.spec_from_file_location("w43map", os.path.join(GOAL, "hidden_files/weekly-report-ko-zh-tw-build/scratch/transform_map.py"))
    w43m = ilu.module_from_spec(spec2); spec2.loader.exec_module(w43m)
    for f_, s_, d_, c_ in w43m.MAP:
        src_chars |= set(s_); dst_chars |= set(d_)
    w43_entries = len(w43m.MAP)
except Exception as e:
    w43_entries = f"ERROR {e}"
frozen = set()
for pg in PAGES:
    cs = set(parse_texts(os.path.join(CORE, pg + ".svg"))); es = set(parse_texts(os.path.join(ED, pg + ".svg")))
    frozen |= set("".join(cs & es))
removed170 = {c for c in src_chars if "\u4e00" <= c <= "\u9fff" and c not in dst_chars and c not in frozen}
R["builder170"] = dict(n=len(removed170), chars=sorted(removed170), w43_map_entries=w43_entries)
hits = {}
for pg in PAGES:
    core_strings = set(parse_texts(os.path.join(CORE, pg + ".svg")))
    page_hits = []
    for t in parse_texts(os.path.join(ED, pg + ".svg")):
        bad = sorted(set(t) & removed170)
        if bad: page_hits.append(dict(text=t, chars=bad, frozen_in_core=t in core_strings))
    hits[pg] = page_hits
R["builder170_hits"] = hits
R["builder170_nonfrozen_hits"] = [h for pg in PAGES for h in hits[pg] if not h["frozen_in_core"]]
# mainland vocab union
MAIN = sorted(set(["视频", "软件", "硬件", "表情包", "老挝", "打印", "光盘", "宽带", "打车", "外卖", "质量",
    "服务器", "鼠标", "文件夹", "登录", "信息", "信号", "网络", "水平", "出租车", "土豆", "公交车",
    "自行车", "手机", "电脑", "互联网", "网购", "高铁", "地铁", "暖气", "方便面"]))
mh = {}
for pg in PAGES:
    allt = "".join(parse_texts(os.path.join(ED, pg + ".svg")))
    mh[pg] = [w for w in MAIN if w in allt]
R["mainland_hits"] = mh
# P8 notes: residue scan over edition P8 note parts
p8texts = parse_texts(os.path.join(ED, "p8-siheom.svg"))
keys = [t for t in p8texts if re.match(r"^\d+\.\s", t)]
# use proof1-style region: notes are after ' — ' in keys-region lines; approximate with all P8 numbered lines
note_res = []
for t in keys:
    if " — " in t:
        note = t.split(" — ", 1)[1]
        bad = sorted(set(note) & removed170)
        if bad: note_res.append(dict(line=t, chars=bad))
R["p8_note_builder170_hits"] = note_res
# final superset U = builder170 ∪ edition-only ∪ s2t-changed; disposition per char present in edition
U = removed170 | (E - W) | set(changed_chars)
in_ed = {}
for ch in sorted(U):
    present = ch in ed_text
    in_ed[ch] = dict(present_in_edition=present,
                     s2t=cc.convert(ch),
                     in_w43=ch in W, in_zhtw_core=ch in Z, in_builder170=ch in removed170)
R["superset_U"] = dict(n=len(U), chars=in_ed)
R["superset_present_in_edition"] = [ch for ch in sorted(U) if ch in ed_text]
json.dump(R, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "proof_web_residue.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("PDF print:", R["pdf_print"])
print("PDF web:", R["pdf_web"])
print("WEB vs CARDS:", json.dumps(comp, ensure_ascii=False, indent=1))
print("HAN:", R["han_sets"], "ed-only:", len(R["edition_only_vs_w43"]))
print("OpenCC s2t pairs over visible text:", R["opencc_s2t_changed_pairs"])
print("OpenCC s2t changed edition chars:", changed_chars)
print("ed-only attested in zhtw-core:", len(R["edition_only_attested_zhtw_core"]), "unattested:", len(R["edition_only_unattested"]))
print("builder170 n:", len(removed170), "nonfrozen hits:", R["builder170_nonfrozen_hits"])
print("builder170 hits total pages:", {k: len(v) for k, v in hits.items()})
print("mainland hits:", mh)
print("p8 note 170 hits:", note_res)
print("superset U n:", len(U), "present in edition:", len(R["superset_present_in_edition"]))
