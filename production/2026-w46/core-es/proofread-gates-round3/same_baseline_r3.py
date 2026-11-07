# Same-baseline ink-gap scan (README #10 supplementary): same-y text nodes, true ink boxes via PIL/FreeType like occlusion_audit.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/tools"))
from PIL import ImageFont
import xml.etree.ElementTree as ET, re, collections
# font resolution copied from occlusion_audit approach: use tables font paths
import json
tables=json.loads((pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/tools/tables.json").read_text())
print("tables font keys:", list(tables.get("fonts",{}).keys()) if isinstance(tables.get("fonts"),dict) else type(tables.get("fonts")))
