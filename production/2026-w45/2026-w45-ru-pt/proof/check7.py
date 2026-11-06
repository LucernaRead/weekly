from xml.etree import ElementTree as ET
import re
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-pt/svg"
CORE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg"
def joined(base):
    parts=[]
    for pg in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
        t=ET.parse(f"{base}/{pg}.svg")
        parts.append(" ".join(''.join(el.itertext()) for el in t.iter() if el.tag.split('}')[-1]=='text'))
    return "\n".join(parts)
ed=joined(ED)
gold=[
 "В воскресенье, 8 ноября, — три матча",
 "Среда, 4 ноября, — выходной посреди рабочей недели",
 "Как жить неделю с праздником посреди недели",
 "Сначала — список: что вам правда нужно",
 "Во вторник, 3 ноября, рабочий день короче на час",
 "Многие берут отпуск в четверг и в пятницу",
 "В среду города устраивают ярмарки и концерты",
 "Пять дней — почти маленькие каникулы",
]
print("=== golden sentences (edition joined text; P7 list uses «» quotes, article plain) ===")
for g in gold:
    # count occurrences with or without guillemets
    n_plain=ed.count(g)
    print(f"  {n_plain}x :: {g}")
print("=== P7 readers corner: all texts y 1300-1800 + rects ===")
t=ET.parse(f"{ED}/p7-yazyk.svg")
for el in t.iter():
    tag=el.tag.split('}')[-1]
    if tag=='text':
        txt=''.join(el.itertext()).strip()
        try: y=float(el.get('y'))
        except: continue
        if 1250<=y<=1800 and txt: print(f"  TEXT y={y} x={el.get('x')} :: {txt}")
    if tag=='rect':
        try:
            y=float(el.get('y')); h=float(el.get('height'))
        except: continue
        if 1200<=y<=1800: print(f"  RECT x={el.get('x')} y={y} w={el.get('width')} h={h} fill={el.get('fill')}")
print("=== P7 core same region (disclosure lines) ===")
t=ET.parse(f"{CORE}/p7-yazyk.svg")
for el in t.iter():
    if el.tag.split('}')[-1]=='text':
        txt=''.join(el.itertext()).strip()
        try: y=float(el.get('y'))
        except: continue
        if 1650<=y<=1800 and txt: print(f"  TEXT y={y} x={el.get('x')} :: {txt}")
    if el.tag.split('}')[-1]=='rect':
        try: y=float(el.get('y')); h=float(el.get('height'))
        except: continue
        if 1200<=y<=1800: print(f"  RECT x={el.get('x')} y={y} w={el.get('width')} h={h} fill={el.get('fill')}")
