import glob, re
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
gold=["11월 7일은 입동이에요","절정에 가까운 주말이라고만 말할 수 있어요","김장은 겨울 내내 먹는 김치를 담그는 일이에요","수능까지 17일 남았어요. 오늘이 D-17예요","낮은 길은 더 늦게 물들어요","KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요","온 나라가 수험생을 응원해요","날짜를 먼저 보세요"]
src=""
for f in ["content12","content34","content56","content7","content8"]:
    src+=open(f"{BASE}/hidden_files/weekly-report-w45-ko-build/{f}.py", encoding='utf-8').read()+"\n"
print("--- golden frequencies in CORE build source (pre-wrap, whole sentences) ---")
for g in gold: print(f"  {src.count(g)}  {g!r}")
# edition source should be identical for Korean target sentences
src2=""
for f in ["content12","content34","content56","content7","content8"]:
    src2+=open(f"{BASE}/hidden_files/weekly-report-w45-ko-ja-build/{f}.py", encoding='utf-8').read()+"\n"
print("--- golden frequencies in EDITION build source ---")
for g in gold: print(f"  {src2.count(g)}  {g!r}")
# essay char count (de-spaced) from SVG joined lines
lines=['나의 겨울 준비는 김장부터 시작해요. 토요일에는 가족과 함께','배추를 절이고 양념을 버무려요. 일요일에는 두꺼운 이불을 꺼내고','겨울옷을 정리해요. 단풍이 진 뒤에는 산보다 집이 좋아져요. 따뜻한','국을 끓여 가족과 함께 먹어요. 겨울이 와도 마음은 따뜻해요. 준비를','마치면 마음이 놓여요. 저녁에는 가족과 함께 따뜻한 차를 마셔요.','겨울 준비가 끝나면 마음이 든든해져요.']
essay=''.join(lines)
print(f"essay joined chars (incl spaces): {len(essay)}; de-spaced: {len(essay.replace(' ',''))}; de-spaced-nopunct: {len(re.sub(r'[ .]', '', essay))}")
print(f"essay text: {essay!r}")
