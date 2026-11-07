import xml.etree.ElementTree as ET
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
ed=[]
for p in pages: ed+=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
joined="\n".join(ed)
panel=["桥接","bridge","译注","每周一期","韩语周报","答案见第","第 8 版","测验与答案","参考答案","对照第","泡菜季","红叶","过冬泡菜","腌过冬","登陆","温带气旋","头条","快讯","闪电问答","即学即练","本周词语","本期目录","数字看本周","这五个日期","读头版","选出正确答案","说说你自己","过冬清单","数日子的说法","用高考倒计时数日子的四个说法","秋季棒球消息","高考倒计时与万圣节","本周青年数字","深读","高考倒计时读法","本周与考试日一表看清","读者园地","易错诊所","语言","下期预告"]
for s in panel:
    hits=[t for t in ed if s in t]
    print(f"{s}: {len(hits)} {hits[:1]}")
