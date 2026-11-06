import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-build"))
from svglib import wrap, text_w

def show(label, s, kind, bold, size, w):
    lines = wrap(s, kind, bold, size, w)
    print(f"--- {label} ({len(lines)} lines)")
    for ln in lines:
        print(f"  [{text_w(ln, kind, bold, size):7.1f}] {ln!r}")

# B4
show("B4 current", "B1 — « Dickens wrote the story in 1843. »", "serif", False, 22.5, 434)
show("B4 no-space-before-guillemet", "B1 — « Dickens wrote the story in 1843.»", "serif", False, 22.5, 434)
show("B4 NBSP", "B1 — « Dickens wrote the story in 1843.\u00a0»", "serif", False, 22.5, 434)
show("B4 A2 line (control)", "A2 — « At eleven o'clock — we stop. »", "serif", True, 22.5, 434)
show("B4 B2 line (control)", "B2 — « Nobody knows whether this year will be faster. »", "serif", True, 22.5, 434)

# B5 core
core_note = "编辑说明｜VOL.2 曾承诺 VOL.3 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.2 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.4 起刊登收到的真实来信。"
show("B5 core current", core_note, "sans", False, 20, 848)
show("B5 core -你的", core_note.replace("请把你的来信", "请把来信"), "sans", False, 20, 848)
show("B5 core -你的+的?", core_note.replace("请把你的来信与写作寄来", "请把来信与写作寄来"), "sans", False, 20, 848)
v = core_note.replace("故本期如实说明", "故本期如实说明")
show("B5 core +1char 来信们", core_note.replace("收到的真实来信。", "收到的真实来信们。"), "sans", False, 20, 848)

# B5 zh-tw
tw_note = "編輯說明｜VOL.2 曾承諾 VOL.3 刊登真實來信，但截至發稿編輯部未收到真實來信與 VOL.2 寫作投稿，故本期如實說明、不虛構來信；請把你的來信與寫作寄來，VOL.4 起刊登收到的真實來信。"
show("B5 tw current", tw_note, "sans", False, 20, 848)
show("B5 tw -你的", tw_note.replace("請把你的來信", "請把來信"), "sans", False, 20, 848)

# B6 zh-tw bridge
tw_bridge = "用 will + 動詞原形改寫（承諾與將要發生的事）。"
show("B6 tw current", tw_bridge, "sans", False, 20.5, 434)
show("B6 tw -原形", tw_bridge.replace("動詞原形", "動詞"), "sans", False, 20.5, 434)
show("B6 tw +來", tw_bridge.replace("動詞原形改寫", "動詞原形來改寫"), "sans", False, 20.5, 434)
show("B6 tw 事情", tw_bridge.replace("發生的事", "發生的事情"), "sans", False, 20.5, 434)
show("B6 core (control)", "用 will + 动词改写（承诺与将要发生的事）。", "sans", False, 20.5, 434)
