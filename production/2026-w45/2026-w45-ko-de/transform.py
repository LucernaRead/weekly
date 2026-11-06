# -*- coding: utf-8 -*-
"""W45 KO core -> KO x DE fan-out transform (assertion-checked literal replacements).

Method (tools/README #17/#18, W45 ES x DE precedent):
- Every round regenerates the build files from orig/ (pristine core copies),
  repoints OUT/BASE to the DE edition dir, then applies ALL pairs below.
  Fixes therefore only ever enter this file; re-running it + run.py +
  render.py reproduces the edition from scratch.
- Line-based / exact-literal splicing only, never AST byte offsets.
- Registry `type` arguments stay byte-identical (internal keys); only
  rendered strings (instr, notes, heads, boxes, gloss, band lines) change.
- P8 answer-generation code is NOT touched (dash family, Korean
  "— 제N면 —" group headings as shipped in W43 ko-de).
- P1 masthead follows the W43 ko-de shipped geometry exactly:
  subtitle 372 -> 366, badge INSERTED at y=394, 20pt BRICK, rules +20,
  dark band +9; everything below y=606 unmoved (tools/README #20 KO case).
- P7 target-language definition prose stays Korean verbatim; only the
  explanation layer (glosslines, clinic notes, frame note, letters notes,
  phrase translations) becomes German. The P7 readers' letter itself is
  frozen verbatim; the disclosure apparatus (short note + Korean
  disclosure + Chinese disclosure) is replaced by German blocks carrying
  the same facts plus an explicit imperative solicitation.
- Korean instruction glosslines on P2-P6/P8 (reader-language apparatus)
  become German, per the W43 ko-de / KO x EN precedent.
Run (from this dir): tools/venv/bin/python transform.py
Then: tools/venv/bin/python run.py && tools/venv/bin/python render.py
"""
import os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ED_DIR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-de")
CORE_ED = "weekly-report-w45-ko-core"
NEW_ED = "weekly-report-w45-ko-de"

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
    # Repoint outputs to the DE edition dir (content files + render.py).
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

    apply_pairs("bslib4.py", [
        ('"Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY"',
         '"Lucerna · KOREANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF KOREANISCH · ERKLÄRUNGEN AUF DEUTSCH"'),
        ('f"제 {n} 면 / 총 {total} 면"', 'f"Seite {n} von {total}"'),
        ('"译注｜" + s', '"HINWEIS · " + s'),
    ])

    # ---- P1 masthead geometry (W43 ko-de shipped values) ----
    apply_pairs("content12.py", [
        ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
         'p.text(975, 394, "KOREANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 20, "sans", True, BRICK, anchor="middle")'),
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
         '"매주 한국어로 · Jede Woche eine neue Ausgabe · 한국 사람이 읽는 한국어를 읽어요"'),
        ('"立冬"', '"IPDONG"'),
        ('"立冬在 11 月 7 日周六 · 泡菜季开始"',
         '"Ipdong am Samstag, dem 7. November · Kimjang beginnt"'),
        ('"톱 뉴스 · 头条"', '"톱 뉴스 · Topmeldung"'),
        ('"입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。"',
         # 3 wrap lines at 20.5pt/398px, same as the core box: a 4-line
         # gloss pushes the numbers box from col 1 to col 2 and overflows
         # the P1 headline flow (round-2 defect, fixed here).
         '"입동 = Ipdong, Winterbeginn · 절정 = Höhepunkt · 김장 = Winter-Kimchi · 상륙하다 = landen · 온대저기압 = Sturmtief."'),
        ('"숫자로 보는 이번 주 · 数字看本周"', '"숫자로 보는 이번 주 · Zahlen"'),
        ('"지금 바로 연습 · 即学即练"', '"지금 바로 연습 · Jetzt üben"'),
        ('"这五个日期，是本期报纸的骨架。"',
         # 1 line at 18.5pt/390px: the 2-line form overprinted the fixed
         # source line at gy+636 (round-3 NEW TEXTX flag). The box context
         # carries "dieser Ausgabe"; the Korean line above states it fully.
         '"Diese fünf Daten sind das Gerüst."'),
        ('"이번 호의 내용 · 本期目录"', '"이번 호의 내용 · Inhalt"'),
        ('"全部"', '"Alle"'),
        ('"이번 주의 말 · 本周词语"', '"이번 주의 말 · Wort der Woche"'),
        ('"입동 ＝ 立冬、冬季开始的节气。"', '"입동 = Ipdong, der Winterbeginn."'),
        ('"짧은 소식 · 快讯"', '"짧은 소식 · Kurznachrichten"'),
        ('"퀴즈 · 闪电问答"', '"퀴즈 · Blitzquiz"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lesen Sie die Titelseite und wählen Sie die richtige Antwort · Antworten auf Seite 8"'),
        # P2 band + furniture
        ('"생활 · 生活"', '"생활 · Leben"'),
        ('"레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季与过冬准备、韩史考试报名"',
         '"레벨 A2 · 김장과 겨울 준비, 한능검 · Kimjang, Wintervorbereitung, Geschichtsprüfung"'),
        ('"절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。"',
         '"절이다 = einsalzen · 버무리다 = mischen · 난방 = Heizung · 식탁 = Esstisch."'),
        ('"산불 山火 · 벌금 罚款 · 불씨 火星。"',
         '"산불 = Waldbrand · 벌금 = Geldstrafe · 불씨 = Funke."'),
        ('"한능검 접수 · 韩史考试报名"', '"한능검 접수 · Anmeldung"'),
        ('"아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。"',
         '"아삭하다 = knackig · 김 = Dampf · 깊어지다 = tiefer werden."'),
        ('"물려주다 传给 · 낡다 旧 · 두렵다 害怕。"',
         '"물려주다 = weitergeben · 낡다 = alt, abgetragen · 두렵다 = sich fürchten."'),
        ('"겨울 준비 목록 · 过冬清单"', '"겨울 준비 목록 · Checkliste"'),
        ('"묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。"',
         '"묵직하다 = schwer, gediegen · 앞치마 = Schürze · 목록 = Liste."'),
        ('"你呢？为过冬做的第一件事是什么？写两句韩语寄来。"',
         '"Und du? Was machst du zuerst für den Winter? Schreib zwei Sätze auf Koreanisch und schick sie uns."'),
        ('"당신은? · 说说你自己"', '"당신은? · Und du?"'),
        ('"날짜 세는 말 · 数日子的说法"', '"날짜 세는 말 · Tage zählen"'),
        ('"수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒计时数日子的四个说法"',
         '"수능까지 남은 날로 날짜를 세는 네 가지 말 · Vier Countdown-Wörter bis zur Suneung"'),
        ('"11 月 2 日，还剩 17 天"', '"2. November, noch 17 Tage"'),
        ('"11 月 7 日，还剩 12 天"', '"7. November, noch 12 Tage"'),
        ('"11 月 18 日，就是明天"', '"18. November, morgen"'),
        ('"11 月 19 日，就是今天"', '"19. November, heute"'),
        ('"연습 · 第 2 版练习"', '"연습 · Übungen Seite 2"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Antworten auf Seite 8 · Niveaus können gemischt sein; nach Nummer suchen"'),
        # P2 exercise-section glosslines (Korean instruction apparatus -> German)
        ('e.glossline("2면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lies Seite 2 und wähle richtig.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Setze das passende Wort ein.")'),
        ('e.glossline("1면과 2면의 숫자와 날짜로 답하세요.")',
         'e.glossline("Zahlen und Daten von Seite 1 und 2.")'),
        ('instr="把词和说明配对"', 'instr="Paare zuordnen"'),
    ])
    print("content12 done")

    # ---- Shared P8/exercise notes (applied wherever they occur) ----
    # Each literal must occur at least once across the five content files;
    # the trailing Han-zero check proves none was missed.
    NOTES = [
        ('"立冬在11月7日周六"', '"Ipdong am Samstag, dem 7. November"'),
        ('"泡菜季＝腌过冬泡菜"', '"Kimjang = Kimchi für den Winter"'),
        ('"高考在11月19日周四"', '"Suneung am Donnerstag, dem 19. November"'),
        ('"11月2日是D-17"', '"2. November ist D-17"'),
        ('"台风没有在韩国本土登陆"', '"Kein Landfall auf dem koreanischen Festland"'),
        ('"首尔报名窗口11月6日10–12点"', '"Anmeldung in Seoul am 6. November, 10–12 Uhr"'),
        ('"立冬＝冬季开始的节气"', '"Ipdong = Winterbeginn"'),
        ('"内藏山两个预报：11月4日与11月11日"', '"Naejangsan: zwei Prognosen, 4. und 11. November"'),
        ('"10月25日首场比赛因雨推迟"', '"Spiel 1 am 25. Oktober wegen Regen verschoben"'),
        ('"山火注意期从11月1日开始"', '"Waldbrandvorsicht ab 1. November"'),
        ('"带火进山最高罚30万韩元"', '"Feuer im Berg: bis zu 300.000 Won Strafe"'),
        ('"韩史考试在11月28日周六"', '"Geschichtsprüfung am Samstag, dem 28. November"'),
        ('"首尔报名10点至12点"', '"Anmeldung in Seoul 10–12 Uhr"'),
        ('"白菜用盐腌"', '"Chinakohl wird gesalzen"'),
        ('"加入萝卜和调料拌匀"', '"Rettich und Gewürze untermischen"'),
        ('"过冬准备＝为冬天做准备"', '"Wintervorbereitung = Vorbereitung auf den Winter"'),
        ('"进山要小心火"', '"Im Berg vorsichtig mit Feuer sein"'),
        ('"11月3日起开始报名"', '"Anmeldung ab 3. November"'),
        ('"山火注意期到12月15日"', '"Waldbrandvorsicht bis 15. Dezember"'),
        ('"最高罚款30万韩元"', '"Höchststrafe 300.000 Won"'),
        ('"深化考试费27,000韩元"', '"Gebühr für die höhere Stufe: 27.000 Won"'),
        ('"11月6日13点起全国报名剩余名额"', '"Ab 13 Uhr am 6. November: Restplätze im ganzen Land"'),
        ('"김장=腌过冬泡菜 a"', '"김장=Kimchi für den Winter a"'),
        ('"월동 준비=准备过冬 c"', '"월동 준비=Wintervorbereitung c"'),
        ('"산불조심=进山小心火 d"', '"산불조심=Vorsicht mit Feuer im Berg d"'),
        ('"한능검=韩国史考试简称 b"', '"한능검=Kurzform der Geschichtsprüfung b"'),
        ('"内藏山林业厅预报峰值11月4日"', '"Naejangsan, Forstbehörde: 4. November"'),
        ('"内藏山公园公团预报峰值11月11日"', '"Naejangsan, Parkbehörde: 11. November"'),
        ('"内藏山公团预报峰值11月11日"', '"Naejangsan, Parkbehörde: 11. November"'),
        ('"雪岳山实际观测峰值10月16日"', '"Seoraksan, tatsächlich beobachtet: 16. Oktober"'),
        ('"青松现场庆典11月4日至8日"', '"Cheongsong vor Ort: 4. bis 8. November"'),
        ('"没有官方的路段数值"', '"Keine offiziellen Werte je Abschnitt"'),
        ('"红叶最美的时候叫절정"', '"Schönste Laubzeit heißt 절정"'),
        ('"日期不同因为标准不同"', '"Andere Daten, weil andere Kriterien"'),
        ('"实际观测比预报早"', '"Beobachtung früher als Prognose"'),
        ('"现场庆典11月4日起"', '"Fest vor Ort ab 4. November"'),
        ('"青松以苹果闻名"', '"Cheongsong ist für Äpfel bekannt"'),
        ('"内藏山林业厅预报4日"', '"Naejangsan, Forstbehörde: 4."'),
        ('"内藏山公团预报11日"', '"Naejangsan, Parkbehörde: 11."'),
        ('"月出山林业厅预报9日"', '"Wolchulsan, Forstbehörde: 9."'),
        ('"雪岳山实际观测16日"', '"Seoraksan, beobachtet: 16."'),
        ('"내장산=两个预报之间 b"', '"내장산=Zwischen zwei Prognosen b"'),
        ('"월출산=11月9日前夕 a"', '"월출산=Kurz vor dem 9. November a"'),
        ('"북한산=11月4日之后、低路更晚 d"', '"북한산=Nach dem 4. November, tiefe Wege später d"'),
        ('"설악산=实际观测10月16日 c"', '"설악산=Beobachtet am 16. Oktober c"'),
        ('"半决赛胜队是KIA"', '"Sieger des Semi-Playoffs: KIA"'),
        ('"第3场比分13比1"', '"Spiel 3: 13 zu 1"'),
        ('"第3场在蚕室举行"', '"Spiel 3 in Jamsil"'),
        ('"季后赛首场因雨推迟"', '"Playoff-Spiel 1 wegen Regen verschoben"'),
        ('"公布的韩国大赛开始日11月2日"', '"Korean Series, angekündigt: 2. November"'),
        ('"KIA三连胜晋级"', '"KIA mit drei Siegen weiter"'),
        ('"三连胜晋级"', '"Drei Siege in Folge"'),
        ('"首场比赛因雨推迟"', '"Spiel 1 wegen Regen verschoben"'),
        ('"10月26日变为温带气旋"', '"Am 26. Oktober zum außertropischen Tief geworden"'),
        ('"kt在韩国大赛等候"', '"kt wartet in der Korean Series"'),
        ('"이기다的过去式이겼어요"', '"Vergangenheit von 이기다: 이겼어요"'),
        ('"열리다的过去式열렸어요"', '"Vergangenheit von 열리다: 열렸어요"'),
        ('"미뤄지다的过去式미뤄졌어요"', '"Vergangenheit von 미뤄지다: 미뤄졌어요"'),
        ('"바뀌다的过去式바뀌었어요"', '"Vergangenheit von 바뀌다: 바뀌었어요"'),
        ('"준플레이오프=KIA三连胜 b"', '"준플레이오프=KIA mit drei Siegen b"'),
        ('"플레이오프=KIA对三星 d"', '"플레이오프=KIA gegen Samsung d"'),
        ('"한국시리즈=kt在等候 a"', '"한국시리즈=kt wartet a"'),
        ('"온대저기압=台风10月26日变化 c"', '"온대저기압=Wandel des Sturms am 26. Oktober c"'),
        ('"온대저기압=台风10月26日变化 d"', '"온대저기압=Wandel des Sturms am 26. Oktober d"'),
        ('"11月7日是D-12"', '"7. November ist D-12"'),
        ('"听力时段飞机不起降"', '"Während des Hörtests keine Flüge"'),
        ('"首尔万圣节安全人员3,271人"', '"Seoul, Halloween: 3.271 Einsatzkräfte"'),
        ('"梨泰院路10月31日管制"', '"Itaewon-ro am 31. Oktober gesperrt"'),
        ('"全国为考生加油"', '"Das ganze Land feuert die Prüflinge an"'),
        ('"倒计时仍在继续"', '"Der Countdown läuft weiter"'),
        ('"怀着祈愿合格的心意赠送糯米糕、饴糖"', '"Klebreiskuchen und Malzbonbons als Glücksgeschenk"'),
        ('"首尔安全人员3,271人"', '"Seoul: 3.271 Einsatzkräfte"'),
        ('"今年考生551,864人"', '"Dieses Jahr 551.864 Prüflinge"'),
        ('"考场全国1,312处"', '"1.312 Prüfungsorte im ganzen Land"'),
        ('"考试日机关10点上班"', '"Am Prüfungstag: Behörden ab 10 Uhr"'),
        ('"梨泰院部署1,620人"', '"Itaewon: 1.620 Einsatzkräfte"'),
        ('"语序：主语+副词+动词"', '"Wortfolge: Subjekt + Adverb + Verb"'),
        ('"主语+宾语+动词的语序"', '"Wortfolge: Subjekt + Objekt + Verb"'),
        ('"首尔管理14个地点"', '"Seoul verwaltet 14 Orte"'),
        ('"本周倒计时D-17至D-12"', '"Diese Woche: Countdown D-17 bis D-12"'),
        ('"考试日有特别措施"', '"Am Prüfungstag gibt es Sondermaßnahmen"'),
        ('"本周没有特别措施"', '"Diese Woche keine Sondermaßnahmen"'),
        ('"考试日就是D-day"', '"Prüfungstag ist D-Day"'),
        ('"本周氛围是倒计时"', '"Diese Woche: Countdown-Stimmung"'),
        ('"氛围在现在、本周"', '"Stimmung: jetzt, diese Woche"'),
        ('"特别措施只适用于11月19日"', '"Maßnahmen nur am 19. November"'),
        ('"措施只适用于11月19日"', '"Maßnahmen nur am 19. November"'),
        ('"听力时段13:10～13:35"', '"Hörtest 13:10–13:35 Uhr"'),
        ('"倒计时氛围在本周"', '"Countdown-Stimmung diese Woche"'),
        ('"特别措施只适用于考试日"', '"Sondermaßnahmen nur am Prüfungstag"'),
        ('"从D-17到D-12的一周"', '"Woche von D-17 bis D-12"'),
        ('"大数字显示全国规模"', '"Große Zahlen zeigen das ganze Land"'),
        ('"听力时段飞机受管制"', '"Flüge während des Hörtests eingeschränkt"'),
        ('"本周是倒计时氛围"', '"Diese Woche ist Countdown-Stimmung"'),
        ('"节气＝一年24个时节"', '"Jeolgi = 24 Jahreszeiten"'),
        ('"D-1＝明天"', '"D-1 = morgen"'),
        ('"D-day就是当天"', '"D-Day ist der Tag selbst"'),
        ('"日期不同因标准不同（3版）"', '"Andere Daten, andere Kriterien (Seite 3)"'),
        ('"林业厅标准是叶子50%"', '"Forstbehörde: 50 % der Blätter"'),
        ('"实际观测10月16日"', '"Beobachtet am 16. Oktober"'),
        ('"预报要标准日期一起看"', '"Prognose: Kriterien und Datum zusammen lesen"'),
        ('"青松现场庆典11月4日起"', '"Cheongsong vor Ort ab 4. November"'),
        ('"汉拿山三角峰降雨415.5毫米"', '"Hallasan, Samgakbong: 415,5 mm Regen"'),
        ('"智敏周六去内藏山"', '"Jimin geht samstags nach Naejangsan"'),
        ('"周日帮忙腌泡菜"', '"Sonntags hilft sie beim Kimjang"'),
        ('"下周准备韩史考试"', '"Nächste Woche: Vorbereitung auf die Geschichtsprüfung"'),
        ('"智敏喜欢韩国史"', '"Jimin mag koreanische Geschichte"'),
        ('"语序：主语+时间+场所+动词"', '"Wortfolge: Subjekt + Zeit + Ort + Verb"'),
        ('"보러 가요 = 去看"', '"보러 가요 = gehen, um zu sehen"'),
        ('"动作场所用「에서」"', '"Ort der Handlung mit 에서"'),
        ('"月出山林业厅预报峰值11月9日"', '"Wolchulsan, Forstbehörde: Höhepunkt 9. November"'),
        ('"首尔报名窗口10点至12点"', '"Anmeldung in Seoul 10–12 Uhr"'),
        ('"周六去内藏山"', '"Samstags nach Naejangsan"'),
        ('"首尔报名10点开始"', '"Anmeldung in Seoul ab 10 Uhr"'),
        ('"日期不同因标准不同"', '"Andere Daten, andere Kriterien"'),
        ('"입동=冬季开始的节气 a"', '"입동=Winterbeginn a"'),
        ('"절정=最佳时期 b"', '"절정=Höhepunkt b"'),
        ('"김장=腌过冬泡菜 c"', '"김장=Kimchi für den Winter c"'),
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
        ('"문화 · 文化"', '"문화 · Kultur"'),
        ('"레벨 A2→B1 · 단풍 마지막 주말 · 红叶最后一周"',
         '"레벨 A2→B1 · 단풍 마지막 주말 · Letztes Herbstlaub-Wochenende"'),
        ('"기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。"',
         '"기관 = Behörde · 기준 = Kriterium · 관측 = Beobachtung · 구간별 = je Abschnitt."'),
        ('"현장 现场 · 유명하다 有名 · 맛보다 品尝。"',
         '"현장 = vor Ort · 유명하다 = berühmt · 맛보다 = kosten."'),
        ('"이용하다 利用 · 막히다 堵塞 · 예의 礼仪。"',
         '"이용하다 = nutzen · 막히다 = verstopft sein · 예의 = Anstand."'),
        ('"겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。"',
         '"겹쳐 입다 = in Schichten tragen · 미끄러지다 = rutschen · 돌 = Stein."'),
        ('"단풍 구경 준비물 · 红叶观赏准备"', '"단풍 구경 준비물 · Packliste"'),
        ('"你呢？想去看红叶的山是哪座？写两句韩语寄来。"',
         '"Und du? Auf welchen Berg willst du zum Herbstlaub? Schreib zwei Sätze auf Koreanisch und schick sie uns."'),
        ('"당신은? · 说说你自己"', '"당신은? · Und du?"'),
        ('"연습 · 第 3 版练习"', '"연습 · Übungen Seite 3"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Antworten auf Seite 8 · Niveaus können gemischt sein; nach Nummer suchen"'),
        ('e.glossline("3면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lies Seite 3 und wähle richtig.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Setze das passende Wort ein.")'),
        ('e.glossline("3면의 숫자와 날짜로 답하세요.")',
         'e.glossline("Zahlen und Daten von Seite 3.")'),
        ('"스포츠 · 体育"', '"스포츠 · Sport"'),
        ('"레벨 B1 · 가을야구 소식 · 秋季棒球消息"',
         '"레벨 B1 · 가을야구 소식 · Herbst-Baseball"'),
        ('"연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。"',
         '"연승 = Siegesserie · 만루홈런 = Grand Slam · 미뤄지다 = verschoben werden · 마감하다 = Redaktionsschluss."'),
        ('"흔들다 挥动 · 하나가 되다 融为一体。"',
         '"흔들다 = schwenken · 하나가 되다 = eins werden."'),
        ('"예상 预测。"', '"예상 = Prognose."'),
        ('"한국시리즈까지의 길 · 通往韩国大赛之路"',
         '"한국시리즈까지의 길 · Der Weg zur Korean Series"'),
        ('"연습 · 第 4 版练习"', '"연습 · Übungen Seite 4"'),
        ('e.glossline("4면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lies Seite 4 und wähle richtig.")'),
        ('e.glossline("문장을 과거형으로 바꾸세요. (바꾼 문장은 모두 이 신문에 나온 일이에요.)")',
         'e.glossline("Setze die Sätze in die Vergangenheit. (Alle Sätze stehen in dieser Ausgabe.)")'),
        ('instr="把山和说明配对"', 'instr="Paare zuordnen"'),
        ('instr="把词和说明配对"', 'instr="Paare zuordnen"'),
        ('instr="改写"', 'instr="Umformen"'),
    ])
    apply_pairs("content56.py", [
        ('"청년 · 青年"', '"청년 · Jugend"'),
        ('"레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒计时与万圣节"',
         '"레벨 B1 · 수능 카운트다운과 할로윈 · Suneung-Countdown und Halloween"'),
        ('"정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。"',
         '"정리 = Ordnung, Wiederholung · 끈끈하다 = klebrig · 합격 = Bestehen."'),
        ('"중점 重点 · 배치하다 部署 · 통제하다 管制。"',
         '"중점 = Schwerpunkt · 배치하다 = einsetzen · 통제하다 = sperren, regeln."'),
        ('"이번 주 청년 숫자 · 本周青年数字"', '"이번 주 청년 숫자 · Zahlen"'),
        ('"챙기다 准备好 · 졸리다 犯困 · 평소 平时。"',
         '"챙기다 = einpacken · 졸리다 = schläfrig sein · 평소 = gewöhnlich."'),
        ('"비다 祈愿 · 피하다 避开 · 미끄럽다 滑。"',
         '"비다 = erbitten · 피하다 = meiden · 미끄럽다 = glatt."'),
        ('"你呢？想对考生说的一句加油是什么？写两句韩语寄来。"',
         '"Und du? Was ist dein aufmunternder Satz für die Prüflinge? Schreib zwei Sätze auf Koreanisch und schick sie uns."'),
        ('"당신은? · 说说你自己"', '"당신은? · Und du?"'),
        ('"연습 · 第 5 版练习"', '"연습 · Übungen Seite 5"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Antworten auf Seite 8 · Niveaus können gemischt sein; nach Nummer suchen"'),
        ('e.glossline("5면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lies Seite 5 und wähle richtig.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Setze das passende Wort ein.")'),
        ('e.glossline("5면의 숫자로 답하세요.")',
         'e.glossline("Zahlen von Seite 5.")'),
        ('e.glossline("말을 바른 순서로 놓아 문장을 만드세요.")',
         'e.glossline("Bilde Sätze in richtiger Reihenfolge.")'),
        ('"깊이 읽기 · 深读"', '"깊이 읽기 · Vertiefung"'),
        ('"레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒计时读法"',
         '"레벨 B2 · 수능 카운트다운을 읽는 법 · Den Suneung-Countdown lesen"'),
        ('"짙어지다 变浓 · 규모 规模 · 섞다 混淆。"',
         '"짙어지다 = dichter werden · 규모 = Ausmaß · 섞다 = vermischen."'),
        ('"겁이 나다 害怕 · 중요하다 重要。"',
         '"겁이 나다 = Angst haben · 중요하다 = wichtig."'),
        ('"예정 预定 · 확정 确定 · 믿다 相信。"',
         '"예정 = geplant · 확정 = feststehend · 믿다 = glauben."'),
        ('"이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清"',
         '"이번 주와 시험 날, 한눈에 보기 · Woche und Prüfungstag im Überblick"'),
        ('"연습 · 第 6 版练习"', '"연습 · Übungen Seite 6"'),
        ('e.glossline("6면의 표를 보고 맞는 답을 고르세요.")',
         'e.glossline("Tabelle auf Seite 6: wähle richtig.")'),
        ('e.glossline("6면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Lies Seite 6 und wähle richtig.")'),
        ('e.glossline("문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.")',
         'e.glossline("Wähle 맞다 bei richtig, 틀리다 bei falsch.")'),
        ('instr="造句"', 'instr="Sätze bilden"'),
    ])
    apply_pairs("content7.py", [
        ('"말 공부 · 语言"', '"말 공부 · Sprache"'),
        ('"언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三个级别，三个主题"',
         '"언어 포커스 · 세 가지 레벨, 세 가지 주제 · Drei Niveaus, drei Themen"'),
        ('a.glossline("본격적 正式、全面 · 나다 度过。")',
         'a.glossline("본격적 = richtig, voll · 나다 = verbringen.")'),
        ('b.glossline("남다 剩下 · 바로 正是、恰恰。")',
         'b.glossline("남다 = übrig bleiben · 바로 = genau, eben.")'),
        ('c.glossline("짐작하다 推测 · 나누다 区分。")',
         'c.glossline("짐작하다 = vermuten · 나누다 = unterscheiden.")'),
        ('"去某地用「에」，不用「를」。"', '"Für das Ziel steht 에, nicht 를."'),
        ('"「담그다」的过去式是「담갔어요」。"',
         '"Vergangenheit von 담그다: 담갔어요."'),
        ('"数字与前面要留空格。"', '"Zahlen mit Abstand schreiben."'),
        ('"助词只用一个。"', '"Nur eine Partikel."'),
        ('"실수 병원 · 易错诊所"', '"실수 병원 · Fehlerklinik"'),
        ('"句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」"',
         '"„Von 〜 bis 〜“ · Frage: 〜부터 〜까지예요?"'),
        ('"이번 주의 틀 · 本周句式"', '"이번 주의 틀 · Satzmuster"'),
        ('"编辑部示例信，非真实来信。"', '"Beispiel der Redaktion, kein echter Brief."'),
        ('"알려요: 이 편지는 편집부가 쓴 예예요. 마감 때까지 진짜 독자 편지와 8면 쓰기 우수작이 도착하지 않았어요. 그래서 예가 실렸고, 지난 호의 약속은 VOL.3으로 이어져요."',
         '"Bis Redaktionsschluss kamen keine echten Briefe und keine besten Texte von Seite 8 an. Darum steht hier das Beispiel; unser Versprechen aus dem letzten Heft gilt für VOL.3."'),
        ('"郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。"',
         '"Schreiben Sie uns Ihren Brief — und Ihren besten Text von Seite 8!"'),
        ('"독자의 편지 · 读者园地"', '"독자의 편지 · Leserecke"'),
        ('"이번 주의 문장 · 本周金句（逐字摘自本期文章）"',
         '"이번 주의 문장 · Sätze der Woche (wörtlich aus dieser Ausgabe)"'),
        ('"11 月 7 日是立冬。"', '"Der 7. November ist Ipdong."'),
        ('"只能说是接近峰值的周末。"', '"Man kann nur sagen: ein Wochenende nahe dem Höhepunkt."'),
        ('"泡菜季就是腌过冬泡菜。"', '"Kimjang ist das Einlegen von Kimchi für den Winter."'),
        ('"离高考还剩 17 天，今天是 D-17。"', '"Bis zur Suneung sind es noch 17 Tage. Heute ist D-17."'),
        ('"低处的路红得更晚。"', '"Die tieferen Wege färben sich später."'),
        ('"KIA 虎三连胜战胜 LG 双子。"', '"Die KIA Tigers schlagen die LG Twins mit drei Siegen in Folge."'),
        ('"全国都在为考生加油。"', '"Das ganze Land feuert die Prüflinge an."'),
        ('"先看日期。"', '"Schau zuerst auf das Datum."'),
        ('"다음 주 · 下期预告 (VOL.3)"', '"다음 주 · Nächste Woche (VOL.3)"'),
    ])
    apply_pairs("content8.py", [
        ('"시험과 답 · 测验与答案"', '"시험과 답 · Test und Antworten"'),
        # E redirect: KO -> DE keys for 137/138, DE stems for 139/140, KO keys frozen
        ('f.ex("A2", "翻译", "11月7日是立冬。", "对照第 1 版"',
         'f.ex("A2", "翻译", "Der 7. November ist Ipdong.", "Siehe Seite 1"'),
        ('f.ex("A2", "翻译", "离高考还剩 12 天。", "对照第 5 版"',
         'f.ex("A2", "翻译", "Bis zur Suneung sind es noch 12 Tage.", "Siehe Seite 5"'),
        ('"特别措施只适用于11月19日。→ ___", instr="翻译"',
         '"Besondere Maßnahmen gelten nur am 19. November. → ___", instr="翻译"'),
        ('"对照第 6 版"', '"Siehe Seite 6"'),
        ('"我周六去内藏山看红叶。→ ___", instr="翻译"',
         '"Am Samstag fahre ich nach Naejangsan, um das Herbstlaub zu sehen. → ___", instr="翻译"'),
        ('"对照第 3 版"', '"Siehe Seite 3"'),
        ('"(开放题，范文如下)"', '"(offene Aufgabe — Mustertext unten)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Mustertext in Abschnitt H auf dieser Seite ({NCHARS} Zeichen)"'),
        ('f.glossline(f"쓰기 문제예요 (정답은 하나가 아니에요). 아래에 {NCHARS}자의 예가 있어요.")',
         'f.glossline(f"(Schreibaufgabe — es gibt keine einzige richtige Antwort). Unten steht ein Beispiel mit {NCHARS} Zeichen.")'),
        ('"답 · 参考答案 — 按版面分页排列，找到题号即可"',
         '"답 · Lösungen — nach Seiten geordnet; einfach die Nummer suchen"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Jede Aufgabe mit kurzer Anmerkung · ✓ = Schreibaufgabe mit Mustertext"'),
        ('instr="把词和释义配对"', 'instr="Wort–Bedeutung zuordnen"'),
        ('instr="翻译"', 'instr="Übersetzen"'),
        ('instr="写作"', 'instr="Schreiben"'),
        ('instr="造句"', 'instr="Sätze bilden"'),
    ])
    # instr="填空" counts per file (asserted, from the core inventory)
    for fname, want in [("content12.py", 9), ("content34.py", 14),
                        ("content56.py", 13), ("content7.py", 6)]:
        path = os.path.join(HERE, fname)
        src = open(path, encoding="utf-8").read()
        n = src.count('instr="填空"')
        assert n == want, f"{fname}: instr 填空 count {n} != {want}"
        open(path, "w", encoding="utf-8").write(src.replace('instr="填空"', 'instr="Ausfüllen"'))
        print(f"  {fname}: instr 填空 x{n} -> Ausfüllen")
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
        raw = open(os.path.join(HERE, fname), encoding="utf-8").read()
        for bad in ("特别M", "KIADrei"):
            assert bad not in raw, f"{fname}: substring-order corruption {bad}"
    print("transform OK: all rendered strings German; only internal type keys keep Han")


if __name__ == "__main__":
    main()
