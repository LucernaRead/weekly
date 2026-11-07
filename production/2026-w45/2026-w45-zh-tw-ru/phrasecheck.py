import re, os
def texts(d):
    out = []
    for f in sorted(os.listdir(os.path.join(d, "svg"))):
        t = open(os.path.join(d, "svg", f), encoding="utf-8").read()
        out += re.findall(r"<text[^>]*>([^<]*)</text>", t)
    return out
ed = "".join(texts(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-ru")))
core = "".join(texts(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhtw-core")))
p7 = "".join(re.findall(r"<text[^>]*>([^<]*)</text>", open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-ru/svg/p7-lang.svg"), encoding="utf-8").read()))
def norm(s):
    return s.replace("，", ",").replace("、", ",")
quotes = [
 "用手機轉帳、掃碼付款、網上買保險，都是金融科技",
 "123個國家及城市、1,600個攤位",
 "需要才買，不要為了折扣買一堆用不到的東西",
 "在高雄，鋼鐵也能變成舞台",
 "福隆的夏天，在10月26日畫下句點",
 "6比0完封兄弟，龍隊拋下紅色彩帶",
 "250家店家一起討糖",
 "旅展首日中午12點才開門",
]
for q in quotes:
    print(f"edition={norm(ed).count(norm(q))} core={norm(core).count(norm(q))} p7only={norm(p7).count(norm(q))} :: {q[:24]}")
