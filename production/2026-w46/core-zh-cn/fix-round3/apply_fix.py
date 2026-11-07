#!/usr/bin/env python3
"""D5 fix: stem '我拿了一个___包裹。' -> '我拿了___包裹。' in content7.py:20, all 10 build dirs. Key unchanged."""
import os
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files")
DIRS = ["weekly-report-w46-zhcn-build",
 "weekly-report-w46-zh-cn-de-build","weekly-report-w46-zh-cn-es-build","weekly-report-w46-zh-cn-fr-build",
 "weekly-report-w46-zh-cn-it-build","weekly-report-w46-zh-cn-ja-build","weekly-report-w46-zh-cn-ko-build",
 "weekly-report-w46-zh-cn-nl-build","weekly-report-w46-zh-cn-pt-build","weekly-report-w46-zh-cn-ru-build"]
OLD="我拿了一个___包裹。"; NEW="我拿了___包裹。"
for d in DIRS:
    p=os.path.join(BASE,d,"content7.py")
    txt=open(p,encoding="utf-8").read()
    assert txt.count(OLD)==1,(d,txt.count(OLD))
    lines=txt.split("\n")
    assert OLD in lines[19],(d,lines[19])
    # key line directly above must be unchanged: key "个"
    assert '"个"' in lines[18],(d,lines[18])
    txt=txt.replace(OLD,NEW)
    assert txt.count(OLD)==0 and txt.count(NEW)==1
    open(p,"w",encoding="utf-8").write(txt)
    print(f"{d}/content7.py:20: {OLD} -> {NEW}; key line unchanged: {lines[18].strip()}")
print("ALL FIXES APPLIED")
