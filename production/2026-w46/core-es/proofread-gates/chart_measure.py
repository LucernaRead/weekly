import re, os, html, json, sys
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
from PIL import ImageFont
# font paths from tables.json
tabs=json.load(open(BASE+"/tools/tables.json"))
print("font table keys:", list(tabs.get("fonts",{}).keys()) if "fonts" in tabs else "no fonts key; top keys:", list(tabs.keys())[:20])
