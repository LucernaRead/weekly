import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ja-build"))
from svglib import text_w
# P1 top strip y=92: left, center (975 middle), right (end at RIGHT=1885)
left="VOL. 3 · 第3号"; center="毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"; right="2026年11月9日（月）〜15日（日）"
lw=text_w(left,"sans",True,23); cw=text_w(center,"sans",False,21); rw=text_w(right,"sans",False,23)
print("left ends",65+lw,"center",975-cw/2,975+cw/2,"right starts",1885-rw)
print("collisions:", "LEFT-CENTER" if 65+lw>=975-cw/2 else "ok", "CENTER-RIGHT" if 975+cw/2>=1885-rw else "ok")
# P6 chart labels
for name in ["山","神社","公園","町"]:
    print("chart label",name,"ink end",65+text_w(name,"serif",False,22),"bar start 315")
