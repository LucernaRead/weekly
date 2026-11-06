import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-build"))
from svglib import wrap, text_w
def show(label, rendered, w=398):
    lines = wrap(rendered, "sans", False, 20.5, w)
    print(f"--- {label} ({len(lines)} lines)")
    for ln in lines: print(f"  [{text_w(ln,'sans',False,20.5):6.1f}] {ln!r}")
P = "해설 — "
show("KO P3 current", P + "a miser 구두쇠 · a ghost 유령 · a heist 강도 사건 · yet to come 아직 오지 않은.")
show("KO P3 A 강도사건", P + "a miser 구두쇠 · a ghost 유령 · a heist 강도사건 · yet to come 아직 오지 않은.")
show("KO P3 C 않은 것", P + "a miser 구두쇠 · a ghost 유령 · a heist 강도 사건 · yet to come 아직 오지 않은 것.")
show("KO P3 F 유령(귀신)", P + "a miser 구두쇠 · a ghost 유령(귀신) · a heist 강도 사건 · yet to come 아직 오지 않은.")
show("KO P4 current", P + "a fixture 경기 일정 · a group 조 · a finale 결승전, 마지막 경기 · a star 스타 선수.")
show("KO P4 A 스타선수", P + "a fixture 경기 일정 · a group 조 · a finale 결승전, 마지막 경기 · a star 스타선수.")
show("KO P4 B 마지막경기", P + "a fixture 경기 일정 · a group 조 · a finale 결승전, 마지막경기 · a star 스타 선수.")
show("KO P4 E 경기일정", P + "a fixture 경기일정 · a group 조 · a finale 결승전, 마지막 경기 · a star 스타 선수.")
show("KO P4 A+E", P + "a fixture 경기일정 · a group 조 · a finale 결승전, 마지막 경기 · a star 스타선수.")
