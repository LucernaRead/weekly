# -*- coding: utf-8 -*-
"""W45 KO core -> KO x NL fan-out transform (assertion-checked literal replacements).

Method (tools/README #17/#18, W45 KO x DE precedent):
- Every round regenerates the build files from orig/ (pristine core copies),
  repoints OUT/BASE to the NL edition dir, then applies ALL pairs below.
  Fixes therefore only ever enter this file; re-running it + run.py +
  render.py reproduces the edition from scratch.
- Line-based / exact-literal splicing only, never AST byte offsets.
- Registry `type` arguments stay byte-identical (internal keys); only
  rendered strings (instr, notes, heads, boxes, gloss, band lines) change.
- P8 answer-generation code is NOT touched (dash family, Korean
  "— 제N면 —" group headings as shipped in W43 ko-pt).
- P1 masthead follows the W43 ko-nl shipped geometry exactly (measured
  from files/weekly-report-ko-nl/svg/p1-pyoji.svg, NOT from ko-en/ko-de):
  subtitle 372 -> 366, badge INSERTED at y=394, 20pt weight-700 BRICK
  #a4553a, rules +20, dark band +9; everything below y=606 unmoved
  (tools/README #20 KO case).
- P7 target-language definition prose stays Korean verbatim; only the
  explanation layer (glosslines, clinic notes, frame note, letters notes,
  phrase translations) becomes Dutch. The P7 readers' letter itself and
  the Korean disclosure are frozen verbatim; the Chinese solemn statement
  (lcn2) becomes a Dutch block carrying the same 3 facts plus an explicit
  imperative solicitation (letters AND best P8 texts) — the ko-fr model.
  P8 group separators follow the W43 ko-nl shipped form
  ('— Pagina N —'), unlike ko-pt/ko-fr which kept the Korean form.
- Korean instruction glosslines on P2-P6/P8 (reader-language apparatus)
  become Portuguese, per the W43 ko-pt / KO x DE precedent.
Run (from this dir): tools/venv/bin/python transform.py
Then: tools/venv/bin/python run.py && tools/venv/bin/python render.py
"""
import os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ED_DIR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-nl")
CORE_ED = "weekly-report-w45-ko-core"
NEW_ED = "weekly-report-w45-ko-nl"

FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "svglib.py", "run.py", "render.py"]


def apply_pairs(fname, pairs):
    path = os.path.join(HERE, fname)
    src = open(path, encoding="utf-8").read()
    for old, new in pairs:
        n = src.count(old)
        assert n >= 1, f"{fname}: NOT FOUND (0x): {old[:60]!r}"
        src = src.replace(old, new)
        print(f"  {fname}: x{n} {old[:44]!r} -> {new[:44]!r}")
    open(path, "w", encoding="utf-8").write(src)


def main():
    for f in FILES:
        shutil.copy(os.path.join(HERE, "orig", f), os.path.join(HERE, f))
    # Repoint outputs to the PT edition dir (content files + render.py).
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(HERE, f)
        s = open(p, encoding="utf-8").read()
        assert s.count(CORE_ED) == 1, f
        open(p, "w", encoding="utf-8").write(s.replace(CORE_ED, NEW_ED))
    p = os.path.join(HERE, "render.py")
    s = open(p, encoding="utf-8").read()
    assert s.count(CORE_ED) == 1
    open(p, "w", encoding="utf-8").write(s.replace(CORE_ED, NEW_ED))
    print("repointed OUT/BASE to", NEW_ED)

    # PDF names follow the W43 ko-nl pattern (VOL2 + -NL suffix).
    apply_pairs("render.py", [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-NL.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-NL-web.pdf"'),
    ])

    apply_pairs("bslib4.py", [
        ('"Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY"',
         '"Lucerna · KOREAANS WEEKBLAD VOL.2 · TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS"'),
        ('f"제 {n} 면 / 총 {total} 면"', 'f"Pagina {n} van {total}"'),
        ('"译注｜" + s', '"Uitleg — " + s'),
    ])

    # ---- P1 masthead geometry (W43 ko-pt shipped values) ----
    apply_pairs("content12.py", [
        ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
         'p.text(975, 394, "TEKSTEN IN HET KOREAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 20, "sans", True, BRICK, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)'),
        ('p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)',
         'p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)'),
        ('p.text(MX + 30, 478,', 'p.text(MX + 30, 487,'),
        ('p.text(MX + 30, 522,', 'p.text(MX + 30, 531,'),
        ('p.text(RIGHT - 30, 478,', 'p.text(RIGHT - 30, 487,'),
        ('p.text(RIGHT - 30, 522,', 'p.text(RIGHT - 30, 531,'),
    ])

    apply_pairs("content12.py", [
        ('"매주 한국어로 · 每周一期 · 한국 사람이 읽는 한국어를 읽어요"',
         '"매주 한국어로 · Elke week · 한국 사람이 읽는 한국어를 읽어요"'),
        ('"立冬"', '"IPDONG"'),
        ('"立冬在 11 月 7 日周六 · 泡菜季开始"',
         '"Ipdong op zaterdag 7 november · Begin van het kimjangseizoen"'),
        ('"톱 뉴스 · 头条"', '"톱 뉴스 · Hoofdnieuws"'),
        ('"입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。"',
         '"입동 = Ipdong · 절정 = piek · 상륙하다 = landen · 김장 = winterkimchi · 온대저기압 = extratropische cycloon."'),
        ('"숫자로 보는 이번 주 · 数字看本周"', '"숫자로 보는 이번 주 · In cijfers"'),
        ('"지금 바로 연습 · 即学即练"', '"지금 바로 연습 · Meteen oefenen"'),
        ('"这五个日期，是本期报纸的骨架。"',
         # 1 line at 18.5pt/390px: the 2-line form overprinted the fixed
         # source line at gy+636 in the DE build (round-3 NEW TEXTX flag).
         '"Deze vijf data dragen dit nummer."'),
        ('"이번 호의 내용 · 本期目录"', '"이번 호의 내용 · Inhoud"'),
        ('"全部"', '"Alle"'),
        ('"이번 주의 말 · 本周词语"', '"이번 주의 말 · Woord van de week"'),
        ('"입동 ＝ 立冬、冬季开始的节气。"', '"입동 = Ipdong, het begin van de winter."'),
        ('"짧은 소식 · 快讯"', '"짧은 소식 · Kort nieuws"'),
        ('"퀴즈 · 闪电问答"', '"퀴즈 · Bliksemquiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lees de voorpagina en kies het juiste antwoord · Antwoorden op blz. 8"'),
        # P2 band + furniture
        ('"생활 · 生活"', '"생활 · Dagelijks leven"'),
        ('"레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季与过冬准备、韩史考试报名"',
         '"레벨 A2 · 김장과 겨울 준비, 한능검 · Kimjang, wintervoorbereiding en het examen Koreaanse geschiedenis"'),
        ('"절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。"',
         '"절이다 = inzouten · 버무리다 = mengen · 난방 = verwarming · 식탁 = tafel."'),
        ('"산불 山火 · 벌금 罚款 · 불씨 火星。"',
         '"산불 = bosbrand · 벌금 = boete · 불씨 = vonk."'),
        ('"한능검 접수 · 韩史考试报名"', '"한능검 접수 · Inschrijving"'),
        ('"아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。"',
         '"아삭하다 = knapperig · 김 = stoom · 깊어지다 = dieper worden."'),
        ('"물려주다 传给 · 낡다 旧 · 두렵다 害怕。"',
         '"물려주다 = doorgeven · 낡다 = oud · 두렵다 = bang zijn."'),
        ('"겨울 준비 목록 · 过冬清单"', '"겨울 준비 목록 · Lijst"'),
        ('"묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。"',
         '"묵직하다 = zwaar · 앞치마 = schort · 목록 = lijst."'),
        ('"你呢？为过冬做的第一件事是什么？写两句韩语寄来。"',
         '"En jij? Wat doe je als eerste voor de winter? Schrijf twee zinnen in het Koreaans en stuur ze op."'),
        ('"당신은? · 说说你自己"', '"당신은? · En jij?"'),
        ('"날짜 세는 말 · 数日子的说法"', '"날짜 세는 말 · Dagen tellen"'),
        ('"수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒计时数日子的四个说法"',
         '"수능까지 남은 날로 날짜를 세는 네 가지 말 · Vier manieren om te tellen met de aftelling"'),
        ('"11 月 2 日，还剩 17 天"', '"2 november, nog 17 dagen"'),
        ('"11 月 7 日，还剩 12 天"', '"7 november, nog 12 dagen"'),
        ('"11 月 18 日，就是明天"', '"18 november, dat is morgen"'),
        ('"11 月 19 日，就是今天"', '"19 november, dat is vandaag"'),
        ('"연습 · 第 2 版练习"', '"연습 · Oefeningen blz. 2"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Antwoorden op blz. 8 · Niveaus kunnen gemengd staan — zoek op nummer"'),
        # P2 exercise-section glosslines (Korean instruction apparatus -> Portuguese)
        ('e.glossline("2면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lees de teksten op blz. 2 en kies het juiste antwoord.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Vul het juiste woord in.")'),
        ('e.glossline("1면과 2면의 숫자와 날짜로 답하세요.")',
         'e.glossline("Antwoord met de getallen en datums van blz. 1 en 2.")'),
        ('instr="把词和说明配对"', 'instr="Koppel"'),
    ])
    print("content12 done")

    # ---- Shared P8/exercise notes (applied wherever they occur) ----
    # Each literal must occur at least once across the five content files;
    # the trailing Han-zero check proves none was missed.
    # Order matters: longer forms before their substrings (see KO x DE §11c).
    NOTES = [
        ('"立冬在11月7日周六"', '"Ipdong op zaterdag 7 november"'),
        ('"泡菜季＝腌过冬泡菜"', '"Kimjang = winterkimchi maken"'),
        ('"高考在11月19日周四"', '"Het examen is op donderdag 19 november"'),
        ('"11月2日是D-17"', '"2 november is D-17"'),
        ('"台风没有在韩国本土登陆"', '"Geen landing van de tyfoon op het Koreaanse vasteland"'),
        ('"首尔报名窗口11月6日10–12点"', '"Inschrijving in Seoul op 6 november van 10 tot 12 uur"'),
        ('"立冬＝冬季开始的节气"', '"Ipdong = het begin van de winter"'),
        ('"内藏山两个预报：11月4日与11月11日"', '"Naejangsan: twee voorspellingen, 4 en 11 november"'),
        ('"10月25日首场比赛因雨推迟"', '"Wedstrijd 1 van 25 oktober uitgesteld door regen"'),
        ('"山火注意期从11月1日开始"', '"Voorzichtig met vuur vanaf 1 november"'),
        ('"带火进山最高罚30万韩元"', '"Vuur meenemen de berg in: boete tot 300.000 won"'),
        ('"韩史考试在11月28日周六"', '"Examen Koreaanse geschiedenis: zaterdag 28 november"'),
        ('"首尔报名10点至12点"', '"Inschrijving in Seoul van 10 tot 12 uur"'),
        ('"白菜用盐腌"', '"De Chinese kool wordt ingezouten"'),
        ('"加入萝卜和调料拌匀"', '"Radijs en kruiden erdoor mengen"'),
        ('"过冬准备＝为冬天做准备"', '"Wintervoorbereiding = je voorbereiden op de winter"'),
        ('"进山要小心火"', '"In de bergen: pas op met vuur"'),
        ('"11月3日起开始报名"', '"Inschrijving vanaf 3 november"'),
        ('"山火注意期到12月15日"', '"Voorzichtig met vuur tot 15 december"'),
        ('"最高罚款30万韩元"', '"Maximale boete 300.000 won"'),
        ('"深化考试费27,000韩元"', '"Tarief gevorderd niveau: 27.000 won"'),
        ('"11月6日13点起全国报名剩余名额"', '"Vanaf 13 uur op 6 november: resterende plaatsen in het hele land"'),
        ('"김장=腌过冬泡菜 a"', '"김장=winterkimchi a"'),
        ('"월동 준비=准备过冬 c"', '"월동 준비=wintervoorbereiding c"'),
        ('"산불조심=进山小心火 d"', '"산불조심=pas op met vuur in de bergen d"'),
        ('"한능검=韩国史考试简称 b"', '"한능검=korte naam van het examen Koreaanse geschiedenis b"'),
        ('"内藏山林业厅预报峰值11月4日"', '"Naejangsan, Bosdienst: 4 november"'),
        ('"内藏山公园公团预报峰值11月11日"', '"Naejangsan, Parkendienst: 11 november"'),
        ('"内藏山公团预报峰值11月11日"', '"Naejangsan, Parkendienst: 11 november"'),
        ('"雪岳山实际观测峰值10月16日"', '"Seoraksan, echt waargenomen: 16 oktober"'),
        ('"青松现场庆典11月4日起"', '"Cheongsong ter plaatse vanaf 4 november"'),
        ('"青松现场庆典11月4日至8日"', '"Cheongsong ter plaatse: 4 tot 8 november"'),
        ('"没有官方的路段数值"', '"Geen officiële waarden per traject"'),
        ('"红叶最美的时候叫절정"', '"De mooiste herfstkleur heet 절정"'),
        ('"日期不同因为标准不同"', '"Andere data omdat de criteria verschillen"'),
        ('"实际观测比预报早"', '"De waarneming kwam vóór de voorspelling"'),
        ('"现场庆典11月4日起"', '"Feest ter plaatse vanaf 4 november"'),
        ('"青松以苹果闻名"', '"Cheongsong is beroemd om zijn appels"'),
        ('"内藏山林业厅预报4日"', '"Naejangsan, Bosdienst: dag 4."'),
        ('"内藏山公团预报11日"', '"Naejangsan, Parkendienst: dag 11."'),
        ('"月出山林业厅预报9日"', '"Wolchulsan, Bosdienst: dag 9."'),
        ('"雪岳山实际观测16日"', '"Seoraksan, waargenomen: dag 16."'),
        ('"내장산=两个预报之间 b"', '"내장산=tussen twee voorspellingen b"'),
        ('"월출산=11月9日前夕 a"', '"월출산=avond vóór 9 november a"'),
        ('"북한산=11月4日之后、低路更晚 d"', '"북한산=na 4 november, lagere paden later d"'),
        ('"설악산=实际观测10月16日 c"', '"설악산=waargenomen op 16 oktober c"'),
        ('"半决赛胜队是KIA"', '"De winnaar van de halve finale is KIA"'),
        ('"第3场比分13比1"', '"Wedstrijd 3: 13 tegen 1"'),
        ('"第3场在蚕室举行"', '"Wedstrijd 3 was in Jamsil"'),
        ('"季后赛首场因雨推迟"', '"Wedstrijd 1 van de play-off uitgesteld door regen"'),
        ('"公布的韩国大赛开始日11月2日"', '"Korean Series, aangekondigd: 2 november"'),
        ('"KIA三连胜晋级"', '"KIA ging door met drie zeges op rij"'),
        ('"三连胜晋级"', '"Drie zeges op rij"'),
        ('"首场比赛因雨推迟"', '"Wedstrijd 1 uitgesteld door regen"'),
        ('"10月26日变为温带气旋"', '"Op 26 oktober werd het een extratropische cycloon"'),
        ('"kt在韩国大赛等候"', '"kt wacht in de Korean Series"'),
        ('"이기다的过去式이겼어요"', '"De verleden tijd van 이기다 is 이겼어요"'),
        ('"열리다的过去式열렸어요"', '"De verleden tijd van 열리다 is 열렸어요"'),
        ('"미뤄지다的过去式미뤄졌어요"', '"De verleden tijd van 미뤄지다 is 미뤄졌어요"'),
        ('"바뀌다的过去式바뀌었어요"', '"De verleden tijd van 바뀌다 is 바뀌었어요"'),
        ('"준플레이오프=KIA三连胜 b"', '"준플레이오프=KIA met drie zeges b"'),
        ('"플레이오프=KIA对三星 d"', '"플레이오프=KIA tegen Samsung d"'),
        ('"한국시리즈=kt在等候 a"', '"한국시리즈=kt wacht a"'),
        ('"온대저기압=台风10月26日变化 c"', '"온대저기압=verandering van de tyfoon op 26 oktober c"'),
        ('"온대저기압=台风10月26日变化 d"', '"온대저기압=verandering van de tyfoon op 26 oktober d"'),
        ('"11月7日是D-12"', '"7 november is D-12"'),
        ('"听力时段飞机不起降"', '"Tijdens het luisterdeel geen vluchten"'),
        ('"首尔万圣节安全人员3,271人"', '"Seoul, Halloween: 3.271 medewerkers"'),
        ('"梨泰院路10月31日管制"', '"Itaewon-ro afgesloten op 31 oktober"'),
        ('"全国为考生加油"', '"Het hele land moedigt de kandidaten aan"'),
        ('"倒计时仍在继续"', '"De aftelling gaat door"'),
        ('"怀着祈愿合格的心意赠送糯米糕、饴糖"', '"Kleverige rijstkoek en moutsuiker als geluksgeschenk"'),
        ('"首尔安全人员3,271人"', '"Seoul: 3.271 medewerkers"'),
        ('"今年考生551,864人"', '"Dit jaar: 551.864 kandidaten"'),
        ('"考场全国1,312处"', '"1.312 examenlocaties in het hele land"'),
        ('"考试日机关10点上班"', '"Op de examendag beginnen diensten om 10 uur"'),
        ('"梨泰院部署1,620人"', '"Itaewon: 1.620 medewerkers"'),
        ('"语序：主语+副词+动词"', '"Volgorde: onderwerp + bijwoord + werkwoord"'),
        ('"主语+宾语+动词的语序"', '"Volgorde: onderwerp + lijdend voorwerp + werkwoord"'),
        ('"首尔管理14个地点"', '"Seoul beheert 14 locaties"'),
        ('"本周倒计时D-17至D-12"', '"Deze week: aftelling D-17 tot D-12"'),
        ('"考试日有特别措施"', '"Op de examendag zijn er bijzondere maatregelen"'),
        ('"本周没有特别措施"', '"Deze week geen bijzondere maatregelen"'),
        ('"考试日就是D-day"', '"De examendag is D-day"'),
        ('"本周氛围是倒计时"', '"Deze week: aftelsfeer"'),
        ('"氛围在现在、本周"', '"Sfeer: nu, deze week"'),
        ('"特别措施只适用于11月19日"', '"Maatregelen alleen op 19 november"'),
        ('"措施只适用于11月19日"', '"Maatregelen alleen op 19 november"'),
        ('"听力时段13:10～13:35"', '"Luisterdeel 13:10–13:35"'),
        ('"倒计时氛围在本周"', '"Aftelsfeer deze week"'),
        ('"特别措施只适用于考试日"', '"Bijzondere maatregelen alleen op de examendag"'),
        ('"从D-17到D-12的一周"', '"Week van D-17 tot D-12"'),
        ('"大数字显示全国规模"', '"Grote getallen tonen de landelijke schaal"'),
        ('"听力时段飞机受管制"', '"Vluchten beperkt tijdens het luisterdeel"'),
        ('"本周是倒计时氛围"', '"Deze week is aftelsfeer"'),
        ('"节气＝一年24个时节"', '"절기 = de 24 seizoenen van het jaar"'),
        ('"D-1＝明天"', '"D-1 = morgen"'),
        ('"D-day就是当天"', '"D-day is de dag zelf"'),
        ('"日期不同因标准不同（3版）"', '"Andere criteria, andere data (blz. 3)"'),
        ('"林业厅标准是叶子50%"', '"Bosdienst: 50% van de bladeren"'),
        ('"实际观测10月16日"', '"Waargenomen op 16 oktober"'),
        ('"预报要标准日期一起看"', '"Lees de voorspelling met criterium en datum"'),
        ('"汉拿山三角峰降雨415.5毫米"', '"Hallasan, Samgakbong: 415,5 mm regen"'),
        ('"智敏周六去内藏山"', '"Jimin gaat zaterdag naar Naejangsan"'),
        ('"周日帮忙腌泡菜"', '"Op zondag helpt ze met kimjang"'),
        ('"下周准备韩史考试"', '"Volgende week: voorbereiding op het examen Koreaanse geschiedenis"'),
        ('"智敏喜欢韩国史"', '"Jimin houdt van Koreaanse geschiedenis"'),
        ('"语序：主语+时间+场所+动词"', '"Volgorde: onderwerp + tijd + plaats + werkwoord"'),
        ('"보러 가요 = 去看"', '"보러 가요 = gaan kijken"'),
        ('"动作场所用「에서」"', '"Plaats van de handeling: «에서»"'),
        ('"月出山林业厅预报峰值11月9日"', '"Wolchulsan, Bosdienst: piek op 9 november"'),
        ('"首尔报名窗口10点至12点"', '"Inschrijving in Seoul van 10 tot 12 uur"'),
        ('"周六去内藏山"', '"Op zaterdag naar Naejangsan"'),
        ('"首尔报名10点开始"', '"Inschrijving in Seoul vanaf 10 uur"'),
        ('"日期不同因标准不同"', '"Andere criteria, andere data"'),
        ('"입동=冬季开始的节气 a"', '"입동=begin van de winter a"'),
        ('"절정=最佳时期 b"', '"절정=hoogtepunt, de mooiste tijd b"'),
        ('"김장=腌过冬泡菜 c"', '"김장=winterkimchi c"'),
    ]
    totals = {}
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        path = os.path.join(HERE, fname)
        src = open(path, encoding="utf-8").read()
        for old, new in NOTES:
            n = src.count(old)
            if n:
                src = src.replace(old, new)
                totals[old] = totals.get(old, 0) + n
        open(path, "w", encoding="utf-8").write(src)
    for old, _ in NOTES:
        assert totals.get(old, 0) >= 1, f"NOTE never applied: {old[:50]!r}"
    print(f"shared notes applied: {len(totals)} literals, {sum(totals.values())} occurrences")
    for old, n in sorted(totals.items()):
        if n > 1:
            print(f"  shared x{n} {old[:50]!r}")

    apply_pairs("content34.py", [
        ('"문화 · 文化"', '"문화 · Cultuur"'),
        ('"레벨 A2→B1 · 단풍 마지막 주말 · 红叶最后一周"',
         '"레벨 A2→B1 · 단풍 마지막 주말 · Het laatste herfstweekend"'),
        ('"기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。"',
         '"기관 = instantie · 기준 = criterium · 관측 = waarneming · 구간별 = per traject."'),
        ('"현장 现场 · 유명하다 有名 · 맛보다 品尝。"',
         '"현장 = ter plaatse · 유명하다 = beroemd · 맛보다 = proeven."'),
        ('"이용하다 利用 · 막히다 堵塞 · 예의 礼仪。"',
         '"이용하다 = gebruiken · 막히다 = vaststaan · 예의 = goede manieren."'),
        ('"겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。"',
         '"겹쳐 입다 = laagjes dragen · 미끄러지다 = uitglijden · 돌 = steen."'),
        ('"단풍 구경 준비물 · 红叶观赏准备"', '"단풍 구경 준비물 · Wat meenemen"'),
        ('"你呢？想去看红叶的山是哪座？写两句韩语寄来。"',
         '"En jij? Naar welke berg wil je om herfstkleur te zien? Schrijf twee zinnen in het Koreaans en stuur ze op."'),
        ('"당신은? · 说说你自己"', '"당신은? · En jij?"'),
        ('"연습 · 第 3 版练习"', '"연습 · Oefeningen blz. 3"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Antwoorden op blz. 8 · Niveaus kunnen gemengd staan — zoek op nummer"'),
        ('e.glossline("3면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lees de teksten op blz. 3 en kies het juiste antwoord.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Vul het juiste woord in.")'),
        ('e.glossline("3면의 숫자와 날짜로 답하세요.")',
         'e.glossline("Antwoord met de getallen en datums van blz. 3.")'),
        ('"스포츠 · 体育"', '"스포츠 · Sport"'),
        ('"레벨 B1 · 가을야구 소식 · 秋季棒球消息"',
         '"레벨 B1 · 가을야구 소식 · Herfsthonkbalnieuws"'),
        ('"연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。"',
         '"연승 = zegereeks · 만루홈런 = grand slam · 미뤄지다 = uitgesteld worden · 마감하다 = deadline van de redactie."'),
        ('"흔들다 挥动 · 하나가 되다 融为一体。"',
         '"흔들다 = zwaaien · 하나가 되다 = één worden."'),
        ('"예상 预测。"', '"예상 = voorspelling."'),
        ('"한국시리즈까지의 길 · 通往韩国大赛之路"',
         '"한국시리즈까지의 길 · De weg naar de Korean Series"'),
        ('"연습 · 第 4 版练习"', '"연습 · Oefeningen blz. 4"'),
        ('e.glossline("4면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lees de teksten op blz. 4 en kies het juiste antwoord.")'),
        ('e.glossline("문장을 과거형으로 바꾸세요. (바꾼 문장은 모두 이 신문에 나온 일이에요.)")',
         'e.glossline("Zet de zinnen in de verleden tijd. (Het staat allemaal in dit nummer.)")'),
        ('instr="把山和说明配对"', 'instr="Koppel"'),
        ('instr="把词和说明配对"', 'instr="Koppel"'),
        ('instr="改写"', 'instr="Herschrijf"'),
    ])
    apply_pairs("content56.py", [
        ('"청년 · 青年"', '"청년 · Jongeren"'),
        ('"레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒计时与万圣节"',
         '"레벨 B1 · 수능 카운트다운과 할로윈 · Aftelling naar het examen en Halloween"'),
        ('"정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。"',
         '"정리 = ordenen, herhalen · 끈끈하다 = kleverig · 합격 = slagen."'),
        ('"중점 重点 · 배치하다 部署 · 통제하다 管制。"',
         '"중점 = zwaartepunt · 배치하다 = inzetten · 통제하다 = controleren."'),
        ('"이번 주 청년 숫자 · 本周青年数字"', '"이번 주 청년 숫자 · In cijfers"'),
        ('"챙기다 准备好 · 졸리다 犯困 · 평소 平时。"',
         '"챙기다 = klaarmaken · 졸리다 = slaperig zijn · 평소 = normaal."'),
        ('"비다 祈愿 · 피하다 避开 · 미끄럽다 滑。"',
         '"비다 = bidden, wensen · 피하다 = vermijden · 미끄럽다 = glad."'),
        ('"你呢？想对考生说的一句加油是什么？写两句韩语寄来。"',
         '"En jij? Wat is jouw aanmoediging voor de kandidaten? Schrijf twee zinnen in het Koreaans en stuur ze op."'),
        ('"당신은? · 说说你自己"', '"당신은? · En jij?"'),
        ('"연습 · 第 5 版练习"', '"연습 · Oefeningen blz. 5"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Antwoorden op blz. 8 · Niveaus kunnen gemengd staan — zoek op nummer"'),
        ('e.glossline("5면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lees de teksten op blz. 5 en kies het juiste antwoord.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Vul het juiste woord in.")'),
        ('e.glossline("5면의 숫자로 답하세요.")',
         'e.glossline("Antwoord met de getallen van blz. 5.")'),
        ('e.glossline("말을 바른 순서로 놓아 문장을 만드세요.")',
         'e.glossline("Zet de woorden in de juiste volgorde en maak een zin.")'),
        ('"깊이 읽기 · 深读"', '"깊이 읽기 · Dieper lezen"'),
        ('"레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒计时读法"',
         '"레벨 B2 · 수능 카운트다운을 읽는 법 · De aftelling naar het examen leren lezen"'),
        ('"짙어지다 变浓 · 규모 规模 · 섞다 混淆。"',
         '"짙어지다 = sterker worden · 규모 = schaal · 섞다 = verwarren."'),
        ('"겁이 나다 害怕 · 중요하다 重要。"',
         '"겁이 나다 = bang zijn · 중요하다 = belangrijk."'),
        ('"예정 预定 · 확정 确定 · 믿다 相信。"',
         '"예정 = gepland · 확정 = bevestigd · 믿다 = geloven."'),
        ('"이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清"',
         '"이번 주와 시험 날, 한눈에 보기 · Deze week en de examendag naast elkaar"'),
        ('"연습 · 第 6 版练习"', '"연습 · Oefeningen blz. 6"'),
        ('e.glossline("6면의 표를 보고 맞는 답을 고르세요.")',
         'e.glossline("Bekijk de tabel op blz. 6 en antwoord.")'),
        ('e.glossline("6면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lees de teksten op blz. 6 en kies het juiste antwoord.")'),
        ('e.glossline("문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.")',
         'e.glossline("Klopt de zin, kies 맞다; klopt hij niet, kies 틀리다.")'),
        ('instr="造句"', 'instr="Bouw"'),
    ])
    apply_pairs("content7.py", [
        ('"말 공부 · 语言"', '"말 공부 · Taal"'),
        ('"언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三个级别，三个主题"',
         '"언어 포커스 · 세 가지 레벨, 세 가지 주제 · Drie niveaus, drie thema\'s"'),
        ('a.glossline("본격적 正式、全面 · 나다 度过。")',
         'a.glossline("본격적 = echt, volledig · 나다 = voorbijgaan.")'),
        ('b.glossline("남다 剩下 · 바로 正是、恰恰。")',
         'b.glossline("남다 = overblijven · 바로 = precies.")'),
        ('c.glossline("짐작하다 推测 · 나누다 区分。")',
         'c.glossline("짐작하다 = vermoeden · 나누다 = onderscheiden.")'),
        ('"去某地用「에」，不用「를」。"', '"Ga naar een plaats met «에», niet met «를»."'),
        ('"「담그다」的过去式是「담갔어요」。"',
         '"De verleden tijd van «담그다» is «담갔어요»."'),
        ('"数字与前面要留空格。"', '"Zet een spatie vóór het getal."'),
        ('"助词只用一个。"', '"Gebruik maar één partikel."'),
        ('"실수 병원 · 易错诊所"', '"실수 병원 · Foutenkliniek"'),
        ('"句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」"',
         '"Structuur: «van 〜 tot 〜». Vraag: «〜부터 〜까지예요?»"'),
        ('"이번 주의 틀 · 本周句式"', '"이번 주의 틀 · De zin van de week"'),
        ('"编辑部示例信，非真实来信。"', '"Voorbeeldbrief van de redactie, geen echte brief."'),
        ('"郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。"',
         # Combined disclosure + imperative solicitation (ko-fr model):
         # covers BOTH letters and best P8 texts; geometry measured after
         # the first render (slack +40 start, cf. ko-fr).
         '"Tot de deadline kwamen er geen echte brieven en geen beste teksten van blz. 8 binnen: het voorbeeld blijft staan en de belofte schuift door naar VOL.3. Stuur ons je brief en je beste tekst van blz. 8 op!"'),
        # Letters-box height: the core formula undercounts actual render
        # height by ~26-29px (core's own last line also sits below its box
        # border). Start slack +40 (total constant 66, ko-fr value);
        # re-measure after the first render and adjust to thread the
        # border with last ink inside and air before the phrases rule.
        ('len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 26',
         'len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 66'),
        ('"독자의 편지 · 读者园地"', '"독자의 편지 · Lezersbrieven"'),
        ('"이번 주의 문장 · 本周金句（逐字摘自本期文章）"',
         '"이번 주의 문장 · Zinnen van de week (letterlijk uit dit nummer)"'),
        ('"11 月 7 日是立冬。"', '"7 november is Ipdong."'),
        ('"只能说是接近峰值的周末。"', '"Je kunt alleen zeggen: een weekend dicht bij het hoogtepunt."'),
        ('"泡菜季就是腌过冬泡菜。"', '"Kimjang is winterkimchi maken."'),
        ('"离高考还剩 17 天，今天是 D-17。"', '"Nog 17 dagen tot het examen. Vandaag is het D-17."'),
        ('"低处的路红得更晚。"', '"Lagere paden kleuren later rood."'),
        ('"KIA 虎三连胜战胜 LG 双子。"', '"KIA versloeg LG Twins met drie zeges op rij."'),
        ('"全国都在为考生加油。"', '"Het hele land moedigt de kandidaten aan."'),
        ('"先看日期。"', '"Kijk eerst naar de datum."'),
        ('"다음 주 · 下期预告 (VOL.3)"', '"다음 주 · Volgende week (VOL.3)"'),
    ])
    # P7 phrases pitch 132 -> 102 (ko-fr precedent: col3 ends 1865.94
    # forces the teaser over 2540 at pitch 132; row content ~76px, so
    # pitch 102 keeps ~26px inter-row air; teaser then 2519.94).
    apply_pairs("content7.py", [
        ("(i % 4) * 132", "(i % 4) * 102"),
        ("py = fy + 66 + 4 * 132 + 18", "py = fy + 66 + 4 * 102 + 18"),
    ])
    apply_pairs("content8.py", [
        ('"시험과 답 · 测验与答案"', '"시험과 답 · Toets en antwoorden"'),
        # E redirect: KO -> PT keys for 137/138, PT stems for 139/140, KO keys frozen
        ('f.ex("A2", "翻译", "11月7日是立冬。", "对照第 1 版"',
         'f.ex("A2", "翻译", "7 november is Ipdong.", "Zie blz. 1"'),
        ('f.ex("A2", "翻译", "离高考还剩 12 天。", "对照第 5 版"',
         'f.ex("A2", "翻译", "Nog 12 dagen tot het examen.", "Zie blz. 5"'),
        ('"特别措施只适用于11月19日。→ ___", instr="翻译"',
         '"Bijzondere maatregelen gelden alleen op 19 november. → ___", instr="翻译"'),
        ('"对照第 6 版"', '"Zie blz. 6"'),
        ('"我周六去内藏山看红叶。→ ___", instr="翻译"',
         '"Op zaterdag ga ik naar Naejangsan om herfstkleur te zien. → ___", instr="翻译"'),
        ('"对照第 3 版"', '"Zie blz. 3"'),
        ('"(开放题，范文如下)"', '"(open vraag — het voorbeeld staat hieronder)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Het voorbeeld staat in deel H van deze pagina ({NCHARS} tekens)"'),
        ('f.glossline(f"쓰기 문제예요 (정답은 하나가 아니에요). 아래에 {NCHARS}자의 예가 있어요.")',
         'f.glossline(f"Schrijfopgave (niet één juist antwoord). Hieronder een voorbeeld van {NCHARS} tekens.")'),
        ('"답 · 参考答案 — 按版面分页排列，找到题号即可"',
         '"답 · Antwoorden — per pagina, zoek het nummer op"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Bij elk antwoord een korte notitie in het Nederlands · ✓ = opgave met voorbeeld"'),
        ('instr="把词和释义配对"', 'instr="Koppel"'),
        ('instr="翻译"', 'instr="Vertaal"'),
        ('instr="写作"', 'instr="Schrijf"'),
        ('instr="造句"', 'instr="Bouw"'),
    ])
    apply_pairs("content8.py", [
        ('f"— 제{pg}면 —"', 'f"— Pagina {pg} —"'),
    ])
    # instr="填空" counts per file (asserted, from the core inventory)
    for fname, want in [("content12.py", 9), ("content34.py", 14),
                        ("content56.py", 13), ("content7.py", 6)]:
        path = os.path.join(HERE, fname)
        src = open(path, encoding="utf-8").read()
        n = src.count('instr="填空"')
        assert n == want, f"{fname}: instr 填空 count {n} != {want}"
        open(path, "w", encoding="utf-8").write(src.replace('instr="填空"', 'instr="Vul in"'))
        print(f"  {fname}: instr 填空 x{n} -> Vul in")
    # Final completeness gates on the transformed sources.
    # Registry `type` args are internal keys and stay byte-identical by
    # design (W45 ES x DE precedent); they never render. Strip exactly
    # those 9 literals, then zero Han must remain.
    import re as _re
    TYPES = ["完成句子", "单选", "完形单选", "词汇配对", "造句",
             "句型转换", "判断", "翻译", "写作"]
    for fname in ["bslib4.py", "content12.py", "content34.py", "content56.py",
                  "content7.py", "content8.py"]:
        src = open(os.path.join(HERE, fname), encoding="utf-8").read()
        for t in TYPES:
            src = src.replace(f'"{t}"', '""')
        han = _re.findall(r"[\u4e00-\u9fff]", src)
        assert not han, f"{fname}: {len(han)} Han chars remain, e.g. {han[:10]}"
    print("transform OK: all rendered strings Dutch; only internal type keys keep Han")


if __name__ == "__main__":
    main()
