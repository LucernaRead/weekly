import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/weekly-git/production/2026-w47/core-ja"))
from svglib import text_w
# P1 top strip y=92: left, center (975 middle), right (end at RIGHT=1862)
left="VOL.4　第4号"; center="毎週、日本語で　每周一期　日本人が読んでいる日本語を読む"; right="2026年11月16日（月）〜22日（日）"
lw=text_w(left,"sans",True,23); cw=text_w(center,"sans",False,21); rw=text_w(right,"sans",False,23)
print("left ends",88+lw,"center",975-cw/2,975+cw/2,"right starts",1862-rw)
print("collisions:", "LEFT-CENTER" if 88+lw>=975-cw/2 else "ok", "CENTER-RIGHT" if 975+cw/2>=1862-rw else "ok")
# P6 chart labels (bars start at MX+250 = 338)
for name in ["京都","浅草","高尾山","家"]:
    print("chart label",name,"ink end",88+text_w(name,"serif",False,22),"bar start 338")
