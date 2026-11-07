# -*- coding: utf-8 -*-
import re, glob, sys
from collections import Counter
sys.path.insert(0, "hidden_files/weekly-report-w46-zhtw-build")
from svglib import _font, _fw
from PIL import ImageFont
import xml.etree.ElementTree as ET

SVGDIR = "files/weekly-report-w46-zhtw-core/svg"
def texts(f):
    t = open(f, encoding="utf-8").read()
    return re.findall(r"<text[^>]*>(.*?)</text>", t, re.S)
alltext = ""
for f in sorted(glob.glob(SVGDIR + "/*.svg")):
    alltext += "".join(texts(f))
# phrases: 8 quotes verbatim, exactly 2x each (article + P7)
quotes = ["先列清單,再比價,最後才結帳","旅展四天,一次看完123個國家及城市","早晚溫差大,外套要隨身帶",
"金馬影展,就是一年一度的大電影課","保險箱裡,裝的是高雄的勞動記憶","穿上紅色衣服,一起上街為龍隊喝采",
"嘉年華不用門票,全家人都能來玩","回饋不是折價,實付金額才是真的"]
for q in quotes:
    print("PHRASE", alltext.count(q), q)
# simplified-only scan
simp_only = set("邮说国龙马发观欢对让认识语学读书报纸电话车门问间见风云气头")
cjk = set(ch for ch in alltext if "\u4e00" <= ch <= "\u9fff")
print("SIMP_ONLY_HITS", sorted(simp_only & cjk))
# chart geometry: P4 bars + P6 bars measured from rects
for f, expect in [("p4-sport.svg", [90.0, 450.0, 900.0]), ("p6-deep.svg", [220.0, 400.0, 300.0, 800.0])]:
    svg = open(f"{SVGDIR}/{f}", encoding="utf-8").read()
    widths = [float(m) for m in re.findall(r'<rect x="280\.0?" y="\d+\.?\d*" width="([\d.]+)" height="28"', svg)]
    widths6 = [float(m) for m in re.findall(r'<rect x="405\.0?" y="\d+\.?\d*" width="([\d.]+)" height="34"', svg)]
    print("CHART", f, widths or widths6, "expect", expect)
# same-baseline furniture scan: P1 top band texts (y 218/316/378/410) ink gaps
# use PIL getbbox at 4x like the audit: approximate via _font getlength + getbbox
print("DONE")
