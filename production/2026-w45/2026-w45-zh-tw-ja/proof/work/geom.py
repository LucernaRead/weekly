import xml.etree.ElementTree as ET, os, re
from PIL import Image, ImageFont
GOAL='/home/hatch/workspace/goals/lucernaread-social-media-operations'
def nodes(d, fn):
    t=ET.parse(os.path.join(d,fn)); out=[]
    for e in t.getroot().iter():
        if e.tag.endswith('text'): out.append(e)
    return out
ED=GOAL+'/files/weekly-report-w45-zh-tw-ja/svg'
# P7 letter box: find rects on p7, print all rects with y in 1100..1800
t=ET.parse(ED+'/p7-lang.svg'); print("P7 rects:")
for e in t.getroot().iter():
    if e.tag.endswith('rect'):
        print('  ', e.attrib)
