# -*- coding: utf-8 -*-
# W47 zh-tw core self-checks: phrases 2x, simplified-only scan, chart geometry.
import re, glob, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SVGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")

def texts(f):
    t = open(f, encoding="utf-8").read()
    return re.findall(r"<text[^>]*>(.*?)</text>", t, re.S)

alltext = ""
for f in sorted(glob.glob(SVGDIR + "/*.svg")):
    alltext += "".join(texts(f))
# phrases: 8 quotes verbatim, exactly 2x each (article + P7)
quotes = ["封王遊行從天母棒球場出發", "夜間遊行晚上7點，最後一場不要錯過",
          "小雪之後，天氣一天比一天冷", "主燈秀每半小時一次，每次5分鐘",
          "頒獎典禮晚上6點30分開始", "保險箱裡，裝的是高雄的勞動記憶",
          "穿上紅色衣服，一起上街為龍隊喝采", "香港迪士尼聖誕，從11月17日開始"]
ok = True
for q in quotes:
    n = alltext.count(q)
    print("PHRASE", n, q)
    ok = ok and n == 2
# simplified-only scan
simp_only = set("邮说国龙马发观欢对让认识语学读书报纸电话车门问间见风云气头")
cjk = set(ch for ch in alltext if "\u4e00" <= ch <= "\u9fff")
print("SIMP_ONLY_HITS", sorted(simp_only & cjk))
ok = ok and not (simp_only & cjk)
# P4 bars: x=303 (MX+215), heights 28, widths 90/450/900
svg = open(f"{SVGDIR}/p4-sport.svg", encoding="utf-8").read()
widths = [float(m) for m in re.findall(r'<rect x="303" y="[\d.]+" width="([\d.]+)" height="28"', svg)]
print("CHART p4", widths, "expect [90.0, 450.0, 900.0]")
ok = ok and widths == [90.0, 450.0, 900.0]
# P6 timeline dots: X0=188, HOUR=(1371.5-188)/7, times 14/17/18.5/19/20
svg6 = open(f"{SVGDIR}/p6-deep.svg", encoding="utf-8").read()
cxs = [round(float(m), 2) for m in re.findall(r'<circle cx="([\d.]+)" cy="[\d.]+" r="9"', svg6)]
print("CHART p6 dots", cxs, "expect [188.0, 695.21, 948.82, 1033.36, 1202.43]")
ok = ok and cxs == [188.0, 695.21, 948.82, 1033.36, 1202.43]
print("CHECKS", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
