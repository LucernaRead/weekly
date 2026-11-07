# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 -> FR x KO edition transform. SINGLE SOURCE for all
explanation-layer edits (fix-round edits go here, never only into content
files). Every replacement is a whole line or a unique literal, asserted.
French target text is NEVER a replacement target. Registry type names
(Chinese internal metadata, never printed) are intentionally kept, per the
W43 FR x KO precedent and the W45 FR x EN precedent; they are the only
Han ideographs allowed to survive. Explanation style: polite haeyo form.
Furniture follows the shipped W43 FR x KO forms (badge y=574 22pt BRICK,
footer, page line, gloss prefix, P8 separator, half-width paren notes).
Run from this directory: ../../tools/venv/bin/python transform.py
It rewrites content12/34/56/7/8.py and bslib4.py in place. Re-running it
after a first run fails loudly (old strings gone) -- restore from the
core copy first; never run twice on the same tree.
"""
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))

# Fix rounds: ROUND=1 applies rename + initial translation; ROUND>=2
# applies only the fix sections (round-1 old strings are gone after round
# 1, so a full re-run would fail). Fresh rebuild: TRANSFORM_ROUND=1,
# then =2, =3...
ROUND = int(os.environ.get("TRANSFORM_ROUND", "2"))
_SECTION = [1]
def section(n):
    _SECTION[0] = n

# Core P8 noted set, measured from the shipped core P8 SVG with
# tools/p8.py extract --json (noted 97/150, parse: joined). This becomes
# the edition's explicit PRINT_NOTES set (W43 FR x KO precedent), so the
# Korean edition prints notes for exactly the same exercises even though
# Korean notes are longer than the core's <=10-char rule.
PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33,
               34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71,
               72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95,
               96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
               116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
               129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141,
               142, 143, 144, 145, 146, 147, 148, 149, 150]
assert len(PRINT_NOTES) == 97, len(PRINT_NOTES)
BARE = sorted(set(range(1, 151)) - set(PRINT_NOTES))
assert len(BARE) == 53, len(BARE)

def rep(text, old, new, count=1):
    n = text.count(old)
    assert n == count, f"expected {count}x {old[:60]!r}, found {n}x"
    return text.replace(old, new)

def apply_file(fname, pairs):
    if _SECTION[0] != ROUND:
        print(f"skip section {_SECTION[0]} for {fname} (ROUND={ROUND})")
        return
    path = os.path.join(HERE, fname)
    text = open(path, encoding="utf-8").read()
    for old, new, *rest in pairs:
        text = rep(text, old, new, rest[0] if rest else 1)
    open(path, "w", encoding="utf-8").write(text)
    print(f"{fname}: {len(pairs)} replacements applied")

# ---------------- step 0 (ROUND 1 only): explanation-function rename
# W43 FR x KO precedent: bridge() -> expl(). Definition 1x + calls 26x
# (content12 4, content34 9, content56 9, content7 3, content8 1).
if ROUND == 1:
    _ren = [("bslib4.py", "def bridge(self", "def expl(self", 1),
            ("content12.py", ".bridge(", ".expl(", 4),
            ("content34.py", ".bridge(", ".expl(", 9),
            ("content56.py", ".bridge(", ".expl(", 9),
            ("content7.py", ".bridge(", ".expl(", 3),
            ("content8.py", ".bridge(", ".expl(", 1)]
    for fname, old, new, cnt in _ren:
        path = os.path.join(HERE, fname)
        text = open(path, encoding="utf-8").read()
        text = rep(text, old, new, cnt)
        open(path, "w", encoding="utf-8").write(text)
        print(f"{fname}: rename {old!r} -> {new!r} ({cnt}x)")

section(1)
# ---------------- bslib4: footer + page line + gloss prefix (W43 FR x KO shipped forms)
apply_file("bslib4.py", [
    ('"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
     '"Le Lucerna · 프랑스어 주간지 VOL.3 · 텍스트는 프랑스어 · 해설은 한국어"'),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"제 {n} 면 / 총 {total} 면"'),
    ('("译注｜" + s', '("해설 — " + s'),
])

# ---------------- content12: P1 + P2
apply_file("content12.py", [
    ('# ================= P1 · 头版 (A2) =================',
     '# ================= P1 · 1면 (A2) ================='),
    ('"VOL. 3 · 总第 3 期"', '"VOL. 3 · 제3호"'),
    ('"HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语"',
     '"HEBDOMADAIRE EN FRANÇAIS · 매주 발행 · 프랑스가 읽는 프랑스어"'),
    ('"法 语 周 报 · VOL.3 · 决 赛 周 末"', '"프랑스어 주간지 · VOL.3 · 결승 주말"'),
    ('"周一开学 · 全法同步复课"', '"월요일 개학 · 프랑스 전역 동시 복교"'),
    ('"大师赛开赛 · 音乐节开幕 · 详见第 2 版"', '"마스터스 개막 · 음악제 개막 · 2면 참조"'),
    ('"法语正文 · 简体中文讲解 — 给简体中文读者的版本"',
     '"프랑스어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판"'),
    ('"SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末"',
     '"SPORT · CULTURE · GASTRONOMIE · LA UNE · 결승 주말"'),
    ('f.gloss("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。")',
     'f.gloss("se jouer 결판이 나다, 상연되다 · une finale 결승 · une demi-finale 준결승 · un quart de finale 8강전 · une nocturne 야간 행사 · un frisson 전율, 짜릿함 · la coquille Saint-Jacques 가리비.")'),
    ('f.box("LES DATES · 决赛周末日程"', 'f.box("LES DATES · 결승 주말 일정"'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · 해보기", 25)'),
    ('"周日 8 日举行决赛"', '"8일 일요일에 결승이 열려요"'),
    ('"周六 7 日晚是最后夜场"', '"7일 토요일 밤이 마지막 야간 행사예요"'),
    ('"波尔诺曼底卖扇贝"', '"포르엉베생에서 가리비를 팔아요"'),
    ('"周一 2 日全法复课"', '"2일 월요일에 프랑스 전역이 복교해요"'),
    ('"半决赛后才知道决赛选手"', '"준결승이 끝나야 결승 진출자를 알아요"'),
    ('"三个决赛：网球、刺激、美味"', '"세 가지 결승: 테니스, 짜릿함, 맛"'),
    ('"本周日程 · 11 月 2 日至 8 日"', '"이번 주 일정 · 11월 2–8일"'),
    ('"周末决赛结果周六晚、周日揭晓。"', '"주말 결승 결과는 토요일 밤과 일요일에 나와요."'),
    ('"DANS CE NUMÉRO · 本期目录"', '"DANS CE NUMÉRO · 이번 호 차례"'),
    ('"决出胜负；上演。本周末一切都将见分晓。"', '"결판이 나다, 상연되다. 이번 주말에 모든 게 결정돼요."'),
    ('"EN BREF · 快讯"', '"EN BREF · 단신"'),
    ('"QUIZ ÉCLAIR · 闪电问答"', '"QUIZ ÉCLAIR · 번개 퀴즈"'),
    ('"读头版，选出正确答案 · 答案见第 8 版"', '"1면을 읽고 정답을 고르세요 · 정답은 8면"'),
    ('"决赛在周日 8 日"', '"결승은 8일 일요일"'),
    ('"扇贝节在滨海波尔"', '"가리비 축제는 포르엉베생"'),
    ('"周一 2 日早上全区复课"', '"2일 월요일 아침 전 지역 복교"'),
    ('"最后夜场周六 7 日"', '"마지막 야간 행사는 7일 토요일"'),
    ('# ================= P2 · 生活 (A2) =================',
     '# ================= P2 · 생활 (A2) ================='),
    ('p.band("VIE QUOTIDIENNE · 生活", "Le Lucerna", "NIVEAU A2 · La rentrée · 开学复课")',
     'p.band("VIE QUOTIDIENNE · 생활", "Le Lucerna", "NIVEAU A2 · La rentrée · 개학")'),
    ('f.gloss("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。")',
     'f.gloss("la rentrée 개학, 복교 · reprendre 다시 시작하다, 복교하다 · un cartable 책가방 · un décalage 어긋남, 시차 · en revanche 반대로 · un rituel 습관, 의식.")'),
    ('f.expl("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。")',
     'f.expl("une valise 여행 가방 · une ambiance 분위기 · le bilan 결산, 정리.")'),
    ('"说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。"',
     '"월요일 아침 어디에 있었고, 방학 때 무슨 책을 읽었나요? 프랑스어 두 문장으로 보내 주세요."', 2),
    ('"ET VOUS ? · 说说你自己"', '"ET VOUS ? · 여러분은?"'),
    ('"DIRE LA DATE · 这样说日期"', '"DIRE LA DATE · 날짜 말하기"'),
    ('"lundi 2 novembre · 注意：1 日说 le premier，其余用基数词"',
     '"lundi 2 novembre · 주의: 1일은 le premier, 나머지는 기수를 써요"'),
    ('("lundi 2 novembre", "11 月 2 日星期一 · la rentrée")',
     '("lundi 2 novembre", "11월 2일 월요일 · la rentrée")'),
    ('("mardi 3 novembre", "11 月 3 日星期二 · votes à l\'Assemblée")',
     '("mardi 3 novembre", "11월 3일 화요일 · votes à l\'Assemblée")'),
    ('("mercredi 4 novembre", "11 月 4 日星期三 · sorties cinéma")',
     '("mercredi 4 novembre", "11월 4일 수요일 · sorties cinéma")'),
    ('("samedi 7 novembre", "11 月 7 日星期六 · nocturne et demis")',
     '("samedi 7 novembre", "11월 7일 토요일 · nocturne et demis")'),
    ('("dimanche 8 novembre", "11 月 8 日星期日 · les finales")',
     '("dimanche 8 novembre", "11월 8일 일요일 · les finales")'),
    ('"EXERCICES · 第 2 版练习"', '"EXERCICES · 2면 연습"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"정답은 8면 · 문제는 수준이 섞여 있어요, 번호로 정답을 찾으세요"'),
    ('e.expl("用法语补全日期（注意星期与数字）。")',
     'e.expl("프랑스어로 날짜를 완성하세요(요일과 숫자에 주의하세요).")'),
    ('"复课在星期一"', '"복교는 월요일"'),
    ('"11 月 1 日说 le premier"', '"11월 1일은 le premier"'),
    ('"最后夜场在星期六"', '"마지막 야간 행사는 토요일"'),
    ('"决赛在星期日"', '"결승은 일요일"'),
    ('instr="填空"', 'instr="빈칸 채우기"', 4),
    ('e.expl("用 aller + 动词原形改写（最近将来时）。")',
     'e.expl("aller + 동사 원형으로 바꿔 쓰세요(최근 미래).")'),
    ('e.expl("读第 2 版文章，选出正确答案。")',
     'e.expl("2면 글을 읽고 정답을 고르세요.")'),
    ('"三区同一周一早上复课"', '"세 지역이 같은 월요일 아침에 복교"'),
    ('"冬令时从 10 月 25 日开始"', '"겨울 시간은 10월 25일부터 시작"'),
    ('"11 月晚上天黑得早"', '"11월 밤에는 해가 일찍 져요"'),
    ('["rentrée=开学 a", "reprendre=重新开始 b", "cartable=书包 c", "rituel=习惯 d"]',
     '["rentrée=개학 a", "reprendre=다시 시작하다 b", "cartable=책가방 c", "rituel=습관 d"]'),
    ('instr="把词和释义配对"', 'instr="단어와 뜻 짝짓기"'),
    ('instr="改写"', 'instr="바꿔 쓰기"', 4),
])

# ---------------- content34: P3 + P4
apply_file("content34.py", [
    ('# ================= P3 · 文化 (A2→B1) =================',
     '# ================= P3 · 문화 (A2→B1) ================='),
    ('p.band("CULTURE · 文化", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣")',
     'p.band("CULTURE · 축제", "Le Lucerna", "NIVEAU A2 → B1 · Halloween, Toussaint · 핼러윈과 만성절")'),
    ('f.gloss("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。")',
     'f.gloss("se déguiser 변장하다 · un sort 마법, 장난 · une ambiance 분위기 · le souvenir 추억, 기념 · confondre 혼동하다 · discret 조용한, 차분한.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · 해보기", 25)', 2),
    ('f.expl("判断对错（Vrai / Faux）。")', 'f.expl("맞는지 틀린지 판단하세요(Vrai / Faux).")'),
    ('"万圣节在 10 月 31 日星期六"', '"핼러윈은 10월 31일 토요일"'),
    ('"诸圣节墓园摆满菊花"', '"만성절에는 묘지에 국화가 가득해요"'),
    ('"菊花绝不能当礼物送人"', '"국화는 선물로 주면 안 돼요"'),
    ('"11 月 2 日是 jour des morts，不是诸圣节"', '"11월 2일은 jour des morts, 만성절이 아니에요"'),
    ('"文中：le rire d\'abord, le souvenir ensuite"', '"본문: le rire d\'abord, le souvenir ensuite"'),
    ('f.expl("用 déguisement / tombe / citrouille / souvenir 填空。")',
     'f.expl("déguisement / tombe / citrouille / souvenir로 빈칸을 채우세요.")'),
    ('"万圣节穿变装服装"', '"핼러윈에는 변장 복장을 입어요"'),
    ('"花放在墓碑上"', '"꽃을 묘비에 놓아요"'),
    ('"南瓜是万圣节的象征"', '"호박은 핼러윈의 상징이에요"'),
    ('"诸圣节是纪念之日"', '"만성절은 추모의 날이에요"'),
    ('f.expl("改写句子（用 ne...jamais / ne...plus / ne...pas）。")',
     'f.expl("문장을 바꿔 쓰세요(ne...jamais / ne...plus / ne...pas 사용).")'),
    ('"jamais + de（无冠词变化）"', '"jamais + de(관사 변화 없음)"'),
    ('"ne...plus = 不再"', '"ne...plus = 더 이상 ~않다"'),
    ('"n\'est pas = 不是"', '"n\'est pas = ~이 아니다"'),
    ('instr="改写"', 'instr="바꿔 쓰기"', 3),
    ('f.expl("即学即练 · 公园万圣节小题。")',
     'f.expl("해보기 · 공원 핼러윈 작은 문제.")'),
    ('"周六 7 日是最后夜场"', '"7일 토요일이 마지막 야간 행사"'),
    ('"敏感儿童有免费驱怪徽章"', '"예민한 아이들에게는 무료 괴물 퇴치 배지가 있어요"'),
    ('"阿斯泰里克斯公园在 Plailly"', '"아스테릭스 공원은 Plailly에 있어요"'),
    ('"Peur sur le Parc 10 月 3 日至 11 月 8 日"', '"Peur sur le Parc는 10월 3일부터 11월 8일까지"'),
    ('"恐惧等级用颜色区分"', '"공포 등급은 색깔로 구분해요"'),
    ('"夜场从 19 点到凌晨 1 点"', '"야간 행사는 19시부터 새벽 1시까지"'),
    ('"LES MOTS DES FÊTES · 节日词表"', '"LES MOTS DES FÊTES · 축제 단어"'),
    ('"un saint — 圣人"', '"un saint — 성인"'),
    ('"un cimetière — 墓园"', '"un cimetière — 묘지"'),
    ('"une tombe — 坟墓"', '"une tombe — 무덤"'),
    ('"un jour férié — 公共假日"', '"un jour férié — 공휴일"'),
    ('"se souvenir — 纪念、想起"', '"se souvenir — 추모하다, 떠올리다"'),
    ('"un déguisement — 变装服装"', '"un déguisement — 변장 복장"'),
    ('"une citrouille — 南瓜"', '"une citrouille — 호박"'),
    ('"un bonbon — 糖果"', '"un bonbon — 사탕"'),
    ('"un fantôme — 幽灵"', '"un fantôme — 유령"'),
    ('"un sort — 魔法、诅咒"', '"un sort — 마법, 저주"'),
    ('"10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。"',
     '"10월 3일부터 11월 8일까지 야간 행사 12회, 마지막 야간 행사는 11월 7일, 낮에는 10시부터 19시까지 열어요."'),
    ('"DATES À RETENIR · 本周日历"', '"DATES À RETENIR · 기억할 날짜"'),
    ('"注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。"',
     '"주의: 디에프 가리비 시장은 11월 14–15일, 이번 주가 아니에요."'),
    ('# ================= P4 · 体育 (B1) =================',
     '# ================= P4 · 체육 (B1) ================='),
    ('p.band("SPORT · 体育", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")',
     'p.band("SPORT · 스포츠", "Le Lucerna", "NIVEAU B1 · Tennis · Masters de Paris")'),
    ('f.gloss("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。")',
     'f.gloss("un tournoi 대회, 토너먼트 · sur dur 하드코트에서 · en salle 실내에서 · un tableau principal 본선 대진표 · le tenant du titre 디펜딩 챔피언 · basculer 역전되다, 기울다 · les tribunes 관중석.")'),
    ('f.expl("读第 4 版文章，选出正确答案。")',
     'f.expl("4면 글을 읽고 정답을 고르세요.")'),
    ('"决赛在周日 8 日"', '"결승은 8일 일요일"'),
    ('"大师赛在室内硬地球场举行"', '"마스터스는 실내 하드코트에서 열려요"'),
    ('"2025 年卫冕冠军是辛纳"', '"2025년 디펜딩 챔피언은 시너예요"'),
    ('"法甲第十轮大场面：朗斯–马赛"', '"리그 1 10라운드 빅매치: 랑스–마르세유"'),
    ('"周日 8 日还有轮椅单打决赛（中午）"', '"8일 일요일에는 휠체어 단식 결승도 있어요(정오)"'),
    ('f.expl("把网球词和释义配对。")', 'f.expl("테니스 단어와 뜻을 짝지으세요.")'),
    ('["tournoi=赛事 a", "raquette=球拍 b", "tribunes=看台 c", "tenant=卫冕者 d"]',
     '["tournoi=대회 a", "raquette=라켓 b", "tribunes=관중석 c", "tenant=디펜딩 챔피언 d"]'),
    ('instr="配对"', 'instr="짝짓기"'),
    ('f.expl("用比较级完成句子（plus / moins）。")',
     'f.expl("비교급으로 문장을 완성하세요(plus / moins).")'),
    ('"室内球速更快"', '"실내에서는 공이 더 빨라요"'),
    ('"大师赛是仅次于大满贯的级别"', '"마스터스는 그랜드슬램 바로 아래 등급이에요"'),
    ('"室内赛季比室外短"', '"실내 시즌은 여름 시즌보다 짧아요"'),
    ('f.expl("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。")',
     'f.expl("un choc 빅매치 · recevoir 맞다, 맞이하다 · familier 익숙한.")'),
    ('"« Allez ! » — 加油！ · « Quelle action ! » — 好球！"',
     '"« Allez ! » — 힘내! · « Quelle action ! » — 멋진 플레이!"'),
    ('"« Il marque ! » — 他得分了！ · « C\'est gagné ! » — 赢了！"',
     '"« Il marque ! » — 득점했어요! · « C\'est gagné ! » — 이겼어요!"'),
    ('"« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！"',
     '"« Quel point ! » — 멋진 포인트!(테니스) · « Balle de match ! » — 매치 포인트!"'),
    ('"LES MOTS DU TENNIS · 网球词表"', '"LES MOTS DU TENNIS · 테니스 단어"'),
    ('"le tennis — 网球"', '"le tennis — 테니스"'),
    ('"une balle — 球"', '"une balle — 공"'),
    ('"un set — 一盘"', '"un set — 한 세트"'),
    ('"un match — 比赛"', '"un match — 경기"'),
    ('"un point — 一分"', '"un point — 1점"'),
    ('"la finale — 决赛"', '"la finale — 결승"'),
    ('"un adversaire — 对手"', '"un adversaire — 상대"'),
    ('"un titre — 冠军头衔"', '"un titre — 우승 타이틀"'),
    ('"À SUIVRE · 拭目以待"', '"À SUIVRE · 계속 지켜보기"'),
    ('mf.head("MICRO-DRILLS · 即学即练", 24)', 'mf.head("MICRO-DRILLS · 미니 연습", 24)'),
    ('mf.expl("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。")',
     'mf.expl("finale / quarts / demi-finales / tableau / fauteuil / choc으로 빈칸을 채우세요.")'),
    ('"四分之一决赛在周五"', '"8강전은 금요일"'),
    ('"半决赛在周六"', '"준결승은 토요일"'),
    ('"单打决赛在周日"', '"단식 결승은 일요일"'),
    ('"正赛签表从周一开始"', '"본선 대진표는 월요일부터 시작"'),
    ('"轮椅赛事周五至周日"', '"휠체어 대회는 금요일부터 일요일까지"'),
    ('"朗斯–马赛是周末焦点战"', '"랑스–마르세유는 주말 빅매치예요"'),
    ('p.text(ix + 22, db4 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, db4 + 40, "LE DÉBAT · 토론", 23, "sans", True, OLIVE)'),
    ('"事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。"',
     '"결승 진출자를 미리 모르는 게 더 짜릿할까요, 더 실망스러울까요? 찬성 두 문장, 반대 두 문장을 쓰세요."'),
])

# ---------------- content56: P5 + P6
apply_file("content56.py", [
    ('# ================= P5 · 青年 (B1) =================',
     '# ================= P5 · 청년 (B1) ================='),
    ('p.band("JEUNESSE & MUSIQUE · 青年", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 音乐节")',
     'p.band("JEUNESSE & MUSIQUE · 청년", "Le Lucerna", "NIVEAU B1 · Pitchfork Paris · 음악제")'),
    ('f.gloss("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。")',
     'f.gloss("un lieu 장소, 공연장 · une affiche 포스터 · les paroles 가사 · donner le ton 분위기를 정하다 · se promener 거닐다, 돌아다니다 · pile 정확히, 딱.")'),
    ('f.head("À VOUS ! · 即学即练", 25)', 'f.head("À VOUS ! · 해보기", 25)'),
    ('f.expl("读第 5 版文章，选出正确答案。")',
     'f.expl("5면 글을 읽고 정답을 고르세요.")'),
    ('"音乐节 11 月 2–8 日，整整一周"', '"음악제는 11월 2–8일, 꼬박 일주일"'),
    ('"15 届音乐节"', '"15회째 음악제"'),
    ('"Avant-Garde 在巴士底各场地，周四至周六"', '"Avant-Garde는 바스티유 일대 공연장, 목요일부터 토요일까지"'),
    ('"俱乐部之夜在周五、周六"', '"클럽 나이트는 금요일과 토요일"'),
    ('"开幕夜：Headache、Iceage、DIIV"', '"개막 밤: Headache, Iceage, DIIV"'),
    ('f.expl("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。")',
     'f.expl("lieux / paroles / affiche / ambiance / danse / découvre로 빈칸을 채우세요.")'),
    ('"10 个场地"', '"공연장 10곳"'),
    ('"歌词也是法语学习材料"', '"가사도 프랑스어 학습 자료예요"'),
    ('"海报上写着演出信息"', '"포스터에 공연 정보가 적혀 있어요"'),
    ('"每晚气氛各不相同"', '"매일 밤 분위기가 달라요"'),
    ('"音乐节上人们跳舞"', '"음악제에서는 사람들이 춤을 춰요"'),
    ('"发现不认识的乐队"', '"모르는 밴드를 발견해요"'),
    ('f.expl("把音乐词和释义配对。")', 'f.expl("음악 단어와 뜻을 짝지으세요.")'),
    ('["concert=音乐会 a", "scène=舞台 b", "groupe=乐队 c", "billet=门票 d"]',
     '["concert=콘서트 a", "scène=무대 b", "groupe=밴드 c", "billet=입장권 d"]'),
    ('instr="配对"', 'instr="짝짓기"', 2),
    ('f.expl("补全对话（音乐节门口）。")',
     'f.expl("대화를 완성하세요(음악제 입구).")'),
    ('"今晚演出的乐队"', '"오늘 밤 공연하는 밴드"'),
    ('"买两张票"', '"표 두 장 사기"'),
    ('"MOTS DE LA MUSIQUE · 音乐词表"', '"MOTS DE LA MUSIQUE · 음악 단어"'),
    ('"un festival — 音乐节"', '"un festival — 음악제"'),
    ('"un concert — 音乐会"', '"un concert — 콘서트"'),
    ('"une chanson — 歌曲"', '"une chanson — 노래"'),
    ('"un chanteur — 歌手"', '"un chanteur — 가수"'),
    ('"danser — 跳舞"', '"danser — 춤추다"'),
    ('"écouter — 聆听"', '"écouter — 듣다"'),
    ('"une salle — 演出厅"', '"une salle — 공연장"'),
    ('"le public — 观众"', '"le public — 관객"'),
    ('"PARIS CREATOR WEEK · 创作者周"', '"PARIS CREATOR WEEK · 크리에이터"'),
    ('"11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。"',
     '"11월 4–5일 라빌레트: 크리에이터 위크, 온라인 크리에이터와 관객이 직접 만나요."'),
    ('p.text(ix + 22, ty5 + 40, "LE DÉBAT · 讨论", 23, "sans", True, OLIVE)', 'p.text(ix + 22, ty5 + 40, "LE DÉBAT · 토론", 23, "sans", True, OLIVE)'),
    ('"十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？"',
     '"열 곳에서 열리는 음악제가 하나의 큰 공연장보다 나을까요? 프랑스어를 배우려고 어떤 음악을 들어요?"'),
    ('# ================= P6 · 时事 (B2) =================',
     '# ================= P6 · 시사 (B2) ================='),
    ('p.band("POLITIQUE & CHIFFRES · 时事", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 预算周")',
     'p.band("POLITIQUE & CHIFFRES · 시사", "Le Lucerna", "NIVEAU B2 · Budget 2027 · 예산 주간")'),
    ('f.gloss("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l\'unanimité 一致通过/否决 · un amendement 修正案。")',
     'f.gloss("un budget 예산 · une mission (예산) 항목 · un député 국회의원 · rejeter 부결하다 · à l\'unanimité 만장일치로 · un amendement 수정안.")'),
    ('"LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）"',
     '"LE CALENDRIER PRÉVU · 예정된 투표 일정(결과 미정)"'),
    ('"本页日程为计划安排，结果尚未产生，下期跟进。"',
     '"이 면의 일정은 계획일 뿐, 결과는 아직 없어요. 다음 호에서 다룹니다."'),
    ('e6.head("LIRE LE CALENDRIER · 读日程", 25)',
     'e6.head("LIRE LE CALENDRIER · 일정 읽기", 25)'),
    ('e6.expl("读上图日程，选出正确答案。")',
     'e6.expl("위 일정표를 읽고 정답을 고르세요.")'),
    ('"周二 3 日：文化与媒体"', '"화요일 3일: 문화와 미디어"'),
    ('"周三 4 日：农业"', '"수요일 4일: 농업"'),
    ('"周四 5 日：国土协调与科研"', '"목요일 5일: 국토 조정과 연구"'),
    ('"周五 6 日：公共财政与经济"', '"금요일 6일: 공공 재정과 경제"'),
    ('"10 月 23 日社保预算收入被 115–1 否决"', '"10월 23일 사회보장 예산 수입이 115–1로 부결"'),
    ('"参议院从 11 月 9 日起审议"', '"상원은 11월 9일부터 심의"'),
    ('e6.head("LES MOTS · 词汇", 25)', 'e6.head("LES MOTS · 단어", 25)'),
    ('["député=议员 a", "rejeter=否决 b", "vote=投票 c", "amendement=修正案 d"]',
     '["député=국회의원 a", "rejeter=부결하다 b", "vote=투표 c", "amendement=수정안 d"]'),
    ('"« Le texte part au Sénat. » — 法案送交参议院。"',
     '"« Le texte part au Sénat. » — 법안이 상원으로 넘어가요."'),
    ('"« Ce calendrier peut encore bouger. » — 日程仍可能变动。"',
     '"« Ce calendrier peut encore bouger. » — 일정은 아직 바뀔 수 있어요."'),
    ('"« Les résultats ne sont pas connus. » — 结果尚未揭晓。"',
     '"« Les résultats ne sont pas connus. » — 결과는 아직 알려지지 않았어요."'),
    ('g.expl("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。")',
     'g.expl("prévu 예정된, 계획된 · réaliser 이루다, 완성하다 · distinguer 구분하다.")'),
    ('g2.expl("用比较级完成句子。")', 'g2.expl("비교급으로 문장을 완성하세요.")'),
    ('"预算辩论比一场音乐会长"', '"예산 토론은 콘서트보다 길어요"'),
    ('"预算比时间表复杂"', '"예산은 일정표보다 복잡해요"'),
    ('"文化预算与农业预算同样重要"', '"문화 예산은 농업 예산만큼 중요해요"'),
    ('g2.head("MICRO-DRILLS · 即学即练", 25)', 'g2.head("MICRO-DRILLS · 미니 연습", 25)'),
    ('g2.expl("用 examine / ont rejeté / part / peut / connus 填空。")',
     'g2.expl("examine / ont rejeté / part / peut / connus로 빈칸을 채우세요.")'),
    ('"国民议会审议预算"', '"국민의회가 예산을 심의해요"'),
    ('"议员们否决收入部分"', '"의원들이 수입 부분을 부결했어요"'),
    ('"法案送交参议院"', '"법안이 상원으로 넘어가요"'),
    ('"日程仍可能变动"', '"일정은 아직 바뀔 수 있어요"'),
    ('"结果尚未揭晓"', '"결과는 아직 알려지지 않았어요"'),
    ('g2.head("LE DÉBAT · 讨论", 25)', 'g2.head("LE DÉBAT · 토론", 25)'),
    ('g2.expl("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。")',
     'g2.expl("결과가 나오기 전에 일정을 먼저 발표해야 할까요? prévu(계획)와 décidé(확정)를 구분하세요.")'),
])

# ---------------- content7: P7
apply_file("content7.py", [
    ('p.band("LANGUE EN MAIN · 精讲", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 本周金句")',
     'p.band("LANGUE EN MAIN · 정독", "Le Lucerna", "A2 → B2 · Les phrases de la semaine · 이번 주 문장")'),
    ('cA.head("NIVEAU A2 · 基础", 27)', 'cA.head("NIVEAU A2 · 기초", 27)'),
    ('cB.head("NIVEAU B1 · 进阶", 27)', 'cB.head("NIVEAU B1 · 중급", 27)'),
    ('cC.head("NIVEAU B2 · 挑战", 27)', 'cC.head("NIVEAU B2 · 고급", 27)'),
    ('cD.head("BOÎTE À OUTILS · 工具箱", 27)', 'cD.head("BOÎTE À OUTILS · 도구 상자", 27)'),
    ('cD.expl("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。")',
     'cD.expl("이번 호 주머니 문장 세 개, 수준별로 하나씩. 이번 주 문장은 모두 이번 호 글에서 왔어요. 원문을 다시 읽으면 가장 효과적이에요.")'),
    ('p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）", 27, "sans", True, OLIVE)',
     'p.text(MX, py + 26, "LES PHRASES DE LA SEMAINE · 이번 주 문장(모두 본문에서)", 27, "sans", True, OLIVE)'),
    ('p.text(RIGHT, py + 26, "每句一个语法点 + 一道小题 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")',
     'p.text(RIGHT, py + 26, "매 문장 문법 포인트 + 미니 문제 · 정답은 8면", 20, "sans", False, GREY, anchor="end")'),
    ('"语法点｜reprendre：复课、重新开始（pause 后）。"',
     '"문법 포인트 — reprendre: 복교, 다시 시작하기(pause 뒤)."'),
    ('"语法点｜ne...pas encore：尚未、还不。"',
     '"문법 포인트 — ne...pas encore: 아직 ~않다."'),
    ('"pas encore 尚未"', '"pas encore 아직 ~않다"'),
    ('"语法点｜passé composé 代动词：se + être + 过去分词。"',
     '"문법 포인트 — passé composé 대동사: se + être + 과거분사."'),
    ('"语法点｜comparatif：plus + 形容词，ou 对举。"',
     '"문법 포인트 — comparatif: plus + 형용사, ou 대조."'),
    ('"plus + 形容词"', '"plus + 형용사"'),
    ('"语法点｜se promener：代动词，漫步、穿梭。"',
     '"문법 포인트 — se promener: 대동사, 거닐다, 돌아다니다."'),
    ('"语法点｜pouvoir + 动词原形：可能、可以。"',
     '"문법 포인트 — pouvoir + 동사 원형: ~할 수 있다, ~해도 된다."'),
    ('"语法点｜se jouer：决出胜负、上演（代动词）。"',
     '"문법 포인트 — se jouer: 결판이 나다, 상연되다(대동사)."'),
    ('"语法点｜rencontrer：与观众见面；y 代指地点。"',
     '"문법 포인트 — rencontrer: 관객과 만나다, y는 장소를 가리킨다."'),
    ('cf.head("CLINIQUE DES ERREURS · 易错诊所", 25)',
     'cf.head("CLINIQUE DES ERREURS · 오류", 25)'),
    ('cf.expl("每句有一处错误：找出来并改正。")',
     'cf.expl("매 문장에 오류가 하나씩 있어요. 찾아서 고치세요.")'),
    ('"jamais + de：否定句中 des 变 de"', '"jamais + de: 부정문에서는 des가 de로 바뀌어요"'),
    ('"主谓一致：créateurs 复数 → rencontrent，不是 rencontre"',
     '"주어-동사 일치: créateurs는 복수 → rencontrent, rencontre가 아니에요"'),
    ('"虚拟式：il examine，不加 s"', '"가정법: il examine, s를 붙이지 않아요"'),
    ('"事实：决赛在 8 日，不是 7 日"', '"사실: 결승은 8일, 7일이 아니에요"'),
    ('instr="改错"', 'instr="오류 고치기"', 4),
    ('p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 读者园地", 24, "sans", True, OLIVE)',
     'p.text(rx + 24, by7 + 48, "LE COURRIER DES LECTEURS · 독자 마당", 24, "sans", True, OLIVE)'),
    # Reader's corner: labelled editorial example (FR, frozen) + Korean
    # comment WITH an explicit open-call imperative covering BOTH letters
    # and best P8 texts + Korean disclosure of the three facts (no real
    # letters, no VOL.2 best P8 text, both deferred to VOL.4).
    # Fixed-position box: comment 2 lines, disclosure 2 lines (measured
    # with wrap() before round 1) so nothing spills past the box into
    # the VOL.4 teaser strip.
    ('p.para(rx + 24, by7 + 196, "小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。", 20, "sans", False, GREY, rw - 48, 1.4)',
     'p.para(rx + 24, by7 + 196, "샤오모의 한마디 — passé composé가 안정적이고 세미콜론이 좋아요. VOL.4에 여러분의 편지와 최고의 P8 작문을 보내 주세요!", 20, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.para(rx + 24, by7 + 336, "编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。", 19.5, "sans", False, GREY, rw - 48, 1.4)',
     'p.para(rx + 24, by7 + 336, "편집부 알림: 인쇄 때까지 VOL.2 편지가 도착하지 않았고(W44 미발행), 최고의 P8 작문도 없어 예시를 싣습니다. VOL.4에서 실제 편지와 작문을 다룹니다.", 19.5, "sans", False, GREY, rw - 48, 1.4)'),
    ('p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 下周预告", 24, "sans", True, "#f3edda")',
     'p.text(rx + 24, ty7 + 46, "LA SEMAINE PROCHAINE · VOL.4 다음 주", 24, "sans", True, "#f3edda")'),
    ('p.para(rx + 24, ty7 + 196, "下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！", 20, "sans", False, "#b3a06a", rw - 48, 1.4)',
     'p.para(rx + 24, ty7 + 196, "다음 주: 상원 사회보장 예산 심의, 11월 11일 정전 기념일, 디에프 가리비 시장. 여러분의 편지도요!", 20, "sans", False, "#b3a06a", rw - 48, 1.4)'),
])

# ---------------- content8: P8
OLD_KEYS = '''for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):
            s += f"（{e['note']}）"
        parts.append(s)'''
NEW_KEYS = '''# Notes printed on this page = exactly the set printed in the core
# edition, measured from the shipped core P8 SVG with tools/p8.py
# extract (97 noted). Reproduced as an explicit set so the Korean
# edition shows the same notes for the same exercises.
PRINT_NOTES = {%s}
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 제 {pg} 면 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)''' % ", ".join(str(n) for n in PRINT_NOTES)
apply_file("content8.py", [
    ('p.band("EXERCICES & RÉPONSES · 练习与答案", "Le Lucerna", "综合评估 ÉVALUATION · 答案在本版下方")',
     'p.band("EXERCICES & RÉPONSES · 연습과 정답", "Le Lucerna", "종합 평가 ÉVALUATION · 정답은 이 면 아래에")'),
    ('"11 月 8 日 2026 是星期日"', '"2026년 11월 8일은 일요일"'),
    ('"去南泰尔看决赛"', '"낭테르에 결승 보러 가기"'),
    ('"决赛选手周六晚才揭晓"', '"결승 진출자는 토요일 밤에야 알려짐"'),
    ('"品尝语境（un régal）→ goûté"', '"맛보는 맥락（un régal）→ goûté"'),
    ('"se promener 漫步"', '"se promener 거닐다"'),
    ('"avoir + 过去分词 goûté（不配合）"', '"avoir + 과거분사 goûté(일치 없음)"'),
    ('"les finales 主语复数 → ont lieu"', '"les finales 주어 복수 → ont lieu"'),
    ('"elle écrit 她写"', '"elle écrit 그녀가 써요"'),
    ('bf.head("A · TEXTE À TROUS · 完形填空", 24)', 'bf.head("A · TEXTE À TROUS · 빈칸 채우기", 24)'),
    ('bf.expl("选项：")', 'bf.expl("선택지:")'),
    ('bf.head("B · CHOIX MULTIPLE · 单选", 24)', 'bf.head("B · CHOIX MULTIPLE · 객관식", 24)'),
    ('"7 nov. = samedi（最后夜场）"', '"7 nov. = samedi(마지막 야간 행사)"'),
    # Language-neutral French notes: kept byte-identical (not Chinese).
    ('"nous → allons"', '"nous → allons"'),
    ('"s\'intéresser aux（à+les）"', '"s\'intéresser aux（à+les）"'),
    ('"si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j\' 是 je 在元音前的省音"',
     '"si + imparfait → conditionnel; j\'은 je의 생략형"'),
    ('"主语 ce programme 三单 → semble"', '"주어 ce programme 3인칭 단수 → semble"'),
    ('"将来时 aura lieu（决赛在周日）"', '"미래형 aura lieu(결승은 일요일)"'),
    ('"三区同日复课"', '"세 지역 같은 날 복교"'),
    ('"扇贝节在 11 月 7–8 日"', '"가리비 축제는 11월 7–8일"'),
    ('bf.head("C · LECTURE · 阅读理解", 24)', 'bf.head("C · LECTURE · 읽기", 24)'),
    ('"夜场 19 点至凌晨 1 点"', '"야간 행사는 19시부터 새벽 1시까지"'),
    ('"小徽章给小 Léo 驱怪"', '"작은 배지는 꼬마 Léo의 괴물 퇴치용"'),
    ('"周日先看决赛再吃扇贝"', '"일요일에는 결승을 보고 가리비를 먹어요"'),
    ('"周日晚上早睡因为周一上学"', '"일요일 밤 일찍 자는 건 월요일에 학교가 있기 때문"'),
    ('"周一是上学日（复课后正常周一）"', '"월요일은 등교일(복교 후 정상적인 월요일)"'),
    ('bf.head("D · PHRASES · 完成句子与转换", 24)', 'bf.head("D · PHRASES · 문장 완성", 24)'),
    ('"aller + 原形（futur proche）"', '"aller + 원형(futur proche)"'),
    ('"si + 半过去时 venais"', '"si + 반과거 venais"'),
    ('"passé composé : a + 过去分词"', '"passé composé: a + 과거분사"'),
    ('"selon moi = 在我看来"', '"selon moi = 제 생각에는"'),
    ('"il est prévu que + 虚拟式"', '"il est prévu que + 가정법"'),
    ('bf.head("E · TRADUCTION · 翻译", 24)', 'bf.head("E · TRADUCTION · 번역", 24)'),
    # Translation items re-aimed for Korean readers (W43 precedent):
    # FR->reader key becomes the Korean translation; reader->FR items
    # print a Korean source sentence, French key unchanged.
    ('"读一份日程，本身就是在了解法国。"', '"일정을 읽는 것 자체가 이미 프랑스를 이해하는 거예요."'),
    ('"lire un programme = 读日程"', '"lire un programme = 일정 읽기"'),
    ('"Traduisez : « Lire un programme, c\'est déjà comprendre la France. »"',
     '"한국어로 번역하세요: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"比较级 plus vite + court"', '"비교급 plus vite + court"'),
    ('"Traduisez : 他跑得比他哥哥更快。"', '"프랑스어로 번역하세요: 그는 자기 형보다 더 빨리 달려요."'),
    ('"être en vacances + depuis"', '"être en vacances + depuis"'),
    ('"Traduisez : 学生们自 10 月 17 日起就在放假。"', '"프랑스어로 번역하세요: 학생들은 10월 17일부터 방학 중이에요."'),
    ('"futur proche + préparer"', '"futur proche + préparer"'),
    ('"Traduisez : 今晚，我们要准备书包。"', '"프랑스어로 번역하세요: 오늘 밤, 우리는 책가방을 챙길 거예요."'),
    ('"ne...pas encore = 尚未"', '"ne...pas encore = 아직 ~않다"'),
    ('"Traduisez : 人们尚不知道决赛选手是谁。"', '"프랑스어로 번역하세요: 사람들은 아직 결승 진출자가 누구인지 몰라요."'),
    ('bf.head("F · LES MOTS · 词汇配对", 24)', 'bf.head("F · LES MOTS · 단어 짝짓기", 24)'),
    ('["tournoi=赛事 a", "nocturne=夜场 b", "budget=预算 c", "coquille=扇贝 d", "festival=音乐节 e"]',
     '["tournoi=대회 a", "nocturne=야간 행사 b", "budget=예산 c", "coquille=가리비 d", "festival=음악제 e"]'),
    ('instr="配对"', 'instr="짝짓기"'),
    ('"11 月 7 日是星期六"', '"11월 7일은 토요일"'),
    ('"在市场买扇贝"', '"시장에서 가리비 사기"'),
    ('"goûter 品尝（原形）"', '"goûter 맛보다(원형)"'),
    ('"à la portaise 是一种做法"', '"à la portaise는 조리법의 일종"'),
    ('"Bon week-end ! 周末愉快"', '"Bon week-end! 즐거운 주말 보내세요"'),
    ('bf.head("G · DIALOGUE · 对话补全", 24)', 'bf.head("G · DIALOGUE · 대화 완성", 24)'),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "写作", "열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에", "기준에 따라 채점")'),
    ('p.text(wx, wy + 26, "H · ÉCRITURE · 写作", 25, "sans", True, OLIVE)',
     'p.text(wx, wy + 26, "H · ÉCRITURE · 쓰기", 25, "sans", True, OLIVE)'),
    ('p.para(wx, wy + 190, "用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。", 20, "sans", False, GREY, ww, 1.4)',
     'p.para(wx, wy + 190, "프랑스어로 80–100단어를 쓰세요: 저의 11월 7–8일 주말. 경기 하나, 축제 하나, 요리 하나를 분명히 쓰세요.", 20, "sans", False, GREY, ww, 1.4)'),
    ('p.text(mx2 + 22, wy + 38, "MODÈLE · 范文", 23, "sans", True, OLIVE)',
     'p.text(mx2 + 22, wy + 38, "MODÈLE · 모범 답안", 23, "sans", True, OLIVE)'),
    ('p.text(MX, ky + 26, "RÉPONSES · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)',
     'p.text(MX, ky + 26, "RÉPONSES · 모든 정답과 해설(1–8면)", 26, "sans", True, OLIVE)'),
    (OLD_KEYS, NEW_KEYS),
])

# ---------------- final gate: no Han ideographs outside the kept registry type names
ALLOWED = ["完成句子", "单选", "词汇配对", "阅读判断", "句型转换",
           "图表读数", "改错", "跟练", "完形填空", "阅读理解", "翻译",
           "对话补全", "写作"]
HAN = re.compile(r'[\u4e00-\u9fff]')
for fname in ["content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "bslib4.py"]:
    text = open(os.path.join(HERE, fname), encoding="utf-8").read()
    scrubbed = text
    for a in ALLOWED:
        scrubbed = scrubbed.replace(a, "")
    bad = HAN.findall(scrubbed)
    assert not bad, f"{fname}: surviving Han after transform: {bad[:10]}"
    print(f"{fname}: Han gate clean (only registry type names remain)")
print("TRANSFORM OK")

# ================= FIX ROUND 2 (round-1 gate findings) =================
# R1-1 P8 battery LINEX (canonical audit, 1 NEW flag): the last battery
# line crossed the writing-strip gold rule (battery end 1526 vs strip
# rule 1486; core battery max baseline 1455.8). Cause: the four
# reader->FR translation prompts wrapped to 2 lines each in Korean
# (Chinese: 1 line). Shortening three prompts to 1 line each saves 3
# wrapped lines; #137 stays 2 lines (tail 1 syllable, within standard).
# R1-2 P5 creator title ink right 1888 > box border 1885 (3 px): bare
# French form, FR x EN round-4 precedent.
# R1-3 Orphan SPLIT>=3 fixes (all measured with wrap() before applying):
# P2 expl, P3 gloss comma-strand, P5 gloss, P6 gloss, P6 quote, P7
# disclosure, P8 keys note. P6 TROIS DATES right-edge/frame flags are
# core-identical frozen French (x=1469 y=1367, same string) and are NOT
# touched; the four French line-start closers are likewise
# core-identical (same page, same y, same string).
section(2)
apply_file("content56.py", [
    ('"PARIS CREATOR WEEK · 크리에이터"', '"PARIS CREATOR WEEK"'),
    ('"« Le texte part au Sénat. » — 법안이 상원으로 넘어가요."',
     '"« Le texte part au Sénat. » — 법안, 상원으로 넘어가요."'),
    ('f.gloss("un lieu 장소, 공연장 · une affiche 포스터 · les paroles 가사 · donner le ton 분위기를 정하다 · se promener 거닐다, 돌아다니다 · pile 정확히, 딱.")',
     'f.gloss("un lieu 공연장 · une affiche 포스터 · les paroles 가사 · donner le ton 분위기를 정하다 · se promener 거닐다, 돌아다니다 · pile 정확히, 딱.")'),
    ('f.gloss("un budget 예산 · une mission (예산) 항목 · un député 국회의원 · rejeter 부결하다 · à l\'unanimité 만장일치로 · un amendement 수정안.")',
     'f.gloss("un budget 예산 · une mission 예산 항목 · un député 국회의원 · rejeter 부결하다 · à l\'unanimité 만장일치로 · un amendement 수정안.")'),
])
apply_file("content12.py", [
    ('e.expl("프랑스어로 날짜를 완성하세요(요일과 숫자에 주의하세요).")',
     'e.expl("프랑스어로 날짜를 완성하세요(요일과 숫자 주의).")'),
])
apply_file("content34.py", [
    ('f.gloss("se déguiser 변장하다 · un sort 마법, 장난 · une ambiance 분위기 · le souvenir 추억, 기념 · confondre 혼동하다 · discret 조용한, 차분한.")',
     'f.gloss("se déguiser 변장하다 · un sort 마법/장난 · une ambiance 분위기 · le souvenir 추억, 기념 · confondre 혼동하다 · discret 조용한, 차분한.")'),
])
apply_file("content7.py", [
    ('p.para(rx + 24, by7 + 336, "편집부 알림: 인쇄 때까지 VOL.2 편지가 도착하지 않았고(W44 미발행), 최고의 P8 작문도 없어 예시를 싣습니다. VOL.4에서 실제 편지와 작문을 다룹니다.", 19.5, "sans", False, GREY, rw - 48, 1.4)',
     'p.para(rx + 24, by7 + 336, "편집부 알림: 인쇄 때까지 VOL.2 편지가 오지 않았고(W44 미발행), 최고의 P8 작문도 없어 예시를 싣습니다. VOL.4에서 실제 편지와 작문을 다룹니다.", 19.5, "sans", False, GREY, rw - 48, 1.4)'),
])
apply_file("content8.py", [
    ('"한국어로 번역하세요: « Lire un programme, c\'est déjà comprendre la France. »"',
     '"한국어로: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"프랑스어로 번역하세요: 그는 자기 형보다 더 빨리 달려요."',
     '"프랑스어로: 그는 형보다 더 빨리 달려요."'),
    ('"프랑스어로 번역하세요: 학생들은 10월 17일부터 방학 중이에요."',
     '"프랑스어로: 학생들은 10월 17일부터 방학 중이에요."'),
    ('"프랑스어로 번역하세요: 오늘 밤, 우리는 책가방을 챙길 거예요."',
     '"프랑스어로: 오늘 밤 책가방을 챙길 거예요."'),
    ('"프랑스어로 번역하세요: 사람들은 아직 결승 진출자가 누구인지 몰라요."',
     '"프랑스어로: 아직 결승 진출자를 몰라요."'),
    ('"2일 월요일에 프랑스 전역이 복교해요"', '"2일 월요일 전역 복교"'),
])

# ================= FIX ROUND 3 (round-2 remainder) =================
# Round 2's content8 apply aborted on its last pair (the P1 #4 note
# lives in content12, not content8), so content8.py was left unwritten
# while the other round-2 files were already saved. This section
# applies exactly the remainder: the five E-prompt shortenings in
# content8 and the P1 #4 keys-note shortening in content12. Nothing
# from round 2 is repeated here (those old strings are gone).
section(3)
apply_file("content8.py", [
    ('"한국어로 번역하세요: « Lire un programme, c\'est déjà comprendre la France. »"',
     '"한국어로: « Lire un programme, c\'est déjà comprendre la France. »"'),
    ('"프랑스어로 번역하세요: 그는 자기 형보다 더 빨리 달려요."',
     '"프랑스어로: 그는 형보다 더 빨리 달려요."'),
    ('"프랑스어로 번역하세요: 학생들은 10월 17일부터 방학 중이에요."',
     '"프랑스어로: 학생들은 10월 17일부터 방학 중이에요."'),
    ('"프랑스어로 번역하세요: 오늘 밤, 우리는 책가방을 챙길 거예요."',
     '"프랑스어로: 오늘 밤 책가방을 챙길 거예요."'),
    ('"프랑스어로 번역하세요: 사람들은 아직 결승 진출자가 누구인지 몰라요."',
     '"프랑스어로: 아직 결승 진출자를 몰라요."'),
])
apply_file("content12.py", [
    ('"2일 월요일에 프랑스 전역이 복교해요"', '"2일 월요일 전역 복교"'),
])

# ================= FIX ROUND 4 (round-3 remainder) =================
# Round 3 left one lone fragment: the #137 prompt still wrapped to 2
# lines with a lone "요." on line 2 (the >=3 rule passes it, but a
# 1-character final line is bad craft). Shortening "방학 중이에요" to
# "방학이에요" (the depuis + present meaning survives via "부터") fits
# the prompt on 1 line, measured with wrap() before applying. Battery
# then ends one line earlier still (well clear of the strip rule).
section(4)
apply_file("content8.py", [
    ('"프랑스어로: 학생들은 10월 17일부터 방학 중이에요."',
     '"프랑스어로: 학생들은 10월 17일부터 방학이에요."'),
])

# ---------------- end gate: re-verify final state (all rounds applied)
for fname in ["content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "bslib4.py"]:
    text = open(os.path.join(HERE, fname), encoding="utf-8").read()
    scrubbed = text
    for a in ALLOWED:
        scrubbed = scrubbed.replace(a, "")
    bad = HAN.findall(scrubbed)
    assert not bad, f"{fname}: final Han gate failed: {bad[:10]}"
print("FINAL HAN GATE OK")
