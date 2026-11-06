# -*- coding: utf-8 -*-
"""One-off fan-out transform: W45 NL core (Chinese explanations) -> NL x DE.
Line-literal replacements only, each asserted (count printed; 0 = FAIL).
Dutch target text, keys (except re-aimed E137/E138), facts, images: untouched.
Furniture follows the SHIPPED W43 NL x DE edition (files/weekly-report-nl-de):
badge inserted at y=568, 20pt bold BRICK; footer canonical DE with VOL.2;
page line 'Seite N von 8'; gloss prefix 'Hinweis · ' (shipped, NOT the
tables.json 'HINWEIS · ' generic); bridge prefix 'Erklärung · ' (shipped).
P7 Dutch definition sentences, golden sentences and the readers' example
letter stay verbatim; only the explanation layer is localised to German.
Paths were already repointed (baseline step) before this transform runs.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = []

def rep(f, old, new):
    R.append((f, old, new))

def repopt(f, old, new):
    # global instr/type inventory: a file legitimately lacks some combos
    # (same as NL x EN transform's rep_opt); 0 hits there is not a failure.
    R.append((f, old, new, True))

# ---------- bslib4: footer + page line + gloss prefix (W43 NL x DE measured) ----------
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.2 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.2 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"')
rep("bslib4.py", "译注｜", "Hinweis · ")
rep("render.py", "Render the IT weekly", "Render the NL x DE weekly")
rep("run.py", "Run the IT weekly", "Run the NL x DE weekly")
rep("svglib.py", "for 重阳", "for Double Ninth")

# ---------- content8 specific reps FIRST (before global bare-type pass) ----------
# E translation items: NL->DE re-aim (keys 137/138 become German; notes German).
# 139/140 bodies become German prompts; their Dutch keys stay verbatim.
rep("content8.py", '"De Klimaatweek duurt zeven dagen. → ___", instr="翻译"',
     '"De Klimaatweek duurt zeven dagen. → ___", instr="Ins Deutsche übersetzen"')
rep("content8.py", '"Code oranje betekent: bereid je voor. → ___", instr="翻译"',
     '"Code oranje betekent: bereid je voor. → ___", instr="Ins Deutsche übersetzen"')
rep("content8.py", '"博物馆之夜从晚上 19 点到凌晨 2 点。→ ___", instr="翻译"',
     '"Die Museumsnacht dauert von 19:00 Uhr bis 02:00 Uhr. → ___", instr="Ins Niederländische übersetzen"')
rep("content8.py", '"我参加气候周。→ ___", instr="翻译"',
     '"Ich mache bei der Klimaatweek mit. → ___", instr="Ins Niederländische übersetzen"')
rep("content8.py", 'f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。"',
     'f"Schreibaufgabe (keine einzige richtige Antwort); Mustertext ({NWORDS} Wörter) unten."')
# E keys (registry keys, printed on P8): 137/138 re-aimed to German.
rep("content8.py", '"气候周持续七天。"', '"Die Klimaatweek dauert sieben Tage."')
rep("content8.py", '"橙色预警意味着：做好准备。"', '"Code Orange bedeutet: Bereite dich vor."')

# ---------- global types + instr (instrs FIRST, cloze before plain choice) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    repopt(f, 'instr="填空"', 'instr="Einsetzen"')
    repopt(f, 'instr="判断"', 'instr="Richtig oder falsch?"')
    repopt(f, 'instr="造句"', 'instr="Bilde den Satz"')
    repopt(f, 'instr="写作"', 'instr="Schreiben"')
    repopt(f, "完形单选", "Lückentext")
    repopt(f, "完成句子", "ergänzen")
    repopt(f, "词汇配对", "zuordnen")
    repopt(f, "判断对错", "richtig/falsch")
    repopt(f, "单选", "wählen")
    repopt(f, "造句", "Sätze bilden")
    repopt(f, "翻译", "übersetzen")
    repopt(f, "写作", "schreiben")
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    repopt(f, 'instr="把词和释义配对"', 'instr="Wörter und Bedeutungen zuordnen"')
    repopt(f, '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Antworten auf Seite 8 · die Stufen sind gemischt, suche deine Nummer"')
    repopt(f, '"EN JIJ? · 说说你自己"', '"EN JIJ? · UND DU?"')

# ---------- content12: P1 ----------
rep("content12.py", "ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语",
     "ELKE WEEK IN HET NEDERLANDS · JEDE WOCHE AUF NIEDERLÄNDISCH")
rep("content12.py", "荷 兰 语 周 报 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12",
     "NIEDERLÄNDISCH · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12")
# strapline at y=372 stays verbatim (Dutch). Badge INSERTED at y=568 (W43 geometry).
rep("content12.py", 'p.text(RIGHT - 30, 522, "本周全国气候周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 522, "Das ganze Land macht mit · siehe Seite 2", 21, "sans", False, "#b3a06a", anchor="end")\n# pairing badge (brick red, under the band) — W43 NL x DE measured: y=568, 20pt bold BRICK\np.text(975, 568, "NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 20, "sans", True, BRICK, anchor="middle")')
rep("content12.py", '"气候周"', '"KLIMAWOCHE"')
rep("content12.py", '"HET NIEUWS · 头条"', '"HET NIEUWS · SCHLAGZEILE"')
rep("content12.py", 'f.bridge("讲解｜de Klimaatweek 气候周 · de boom planten 种树 · besparen 节约 · de waarschuwing 警告、预警。")',
     'f.bridge("Erklärung · de Klimaatweek = Klimawoche · de boom planten = einen Baum pflanzen · besparen = sparen · de waarschuwing = Warnung.")')
rep("content12.py", '"DE WEEK IN CIJFERS · 数字看本周"', '"DE WEEK IN CIJFERS · IN ZAHLEN"')
rep("content12.py", "（气候周的天数）", "(die Tage der Klimaatweek)")
rep("content12.py", "（周六科弗登发放的树木和灌木）", "(die Bäume und Sträucher, die Coevorden am Samstag verteilt)")
rep("content12.py", "（博物馆之夜开放的博物馆，70 多家）", "(die Museen, die in der Museumsnacht offen sind, über 70)")
rep("content12.py", "（荷甲第 12 轮的比赛场数）", "(die Spiele des 12. Spieltags der Eredivisie)")
rep("content12.py", '"NU JIJ · 即学即练"', '"NU JIJ · JETZT BIST DU DRAN"')
rep("content12.py", '"气候周 11 月 2–8 日"', '"Die Klimaatweek dauert vom 2. bis 8. November"')
rep("content12.py", '"科弗登发放 200 棵树木灌木"', '"Coevorden verteilt 200 Bäume und Sträucher"')
rep("content12.py", '"博物馆之夜在 11 月 7 日周六"', '"Die Museumsnacht ist am Samstag, 7. November"')
rep("content12.py", '"海伦芬–费耶诺德 11:15 开球"', '"Heerenveen–Feyenoord beginnt um 11:15 Uhr"')
rep("content12.py", '"特温特–阿贾克斯 13:30 开球"', '"Twente–Ajax beginnt um 13:30 Uhr"')
rep("content12.py", '"veel mensen → planten"', '"Plural, also planten"')
rep("content12.py", '"· 本周日程"', '"· DIESE WOCHE"')
rep("content12.py", '"Agenda van de week · 本周大事"', '"Agenda van de week · TERMINE DER WOCHE"')
rep("content12.py", 'p.text(gx + 22, byy + 76, "本周日程见第 2–4 版文章", 19, "sans", False, GREY)',
     'p.text(gx + 22, byy + 76, "Alle Termine stehen auch in", 19, "sans", False, GREY)\np.text(gx + 22, byy + 102, "den Artikeln auf den Seiten 2–4.", 19, "sans", False, GREY)')
rep("content12.py", '"IN DEZE EDITIE · 本期目录"', '"IN DEZE EDITIE · INHALT"')
rep("content12.py", '"“气候”：我们周围长期的天气与自然。气候周讲的就是我们的气候。"',
     '"«Klima»: das Wetter und die Natur um uns herum, über lange Zeit. Die Klimaatweek handelt von unserem Klima."')
rep("content12.py", '"IN HET KORT · 快讯"', '"IN HET KORT · KURZ GEMELDET"')
rep("content12.py", '"BLIKSEMQUIZ · 闪电问答"', '"BLIKSEMQUIZ · BLITZQUIZ"')
rep("content12.py", '"读头版，选出正确答案 · 答案见第 8 版"', '"Lies Seite 1, wähle die richtige Antwort · Antworten auf Seite 8"')
rep("content12.py", '"气候周共 7 天（11 月 2–8 日）"', '"Die Klimaatweek dauert 7 Tage (2.–8. November)"')
rep("content12.py", '"博物馆之夜在阿姆斯特丹"', '"Die Museumsnacht ist in Amsterdam"')
# ---------- content12: P2 ----------
rep("content12.py", 'p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · 一步一步讲气候周")',
     'p.band("LEVEN · LEBEN", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · Die Klimaatweek, Schritt für Schritt")')
rep("content12.py", '"ZO ONTHOUD JE HET · 口诀"', '"ZO ONTHOUD JE HET · MERKSATZ"')
rep("content12.py", 'f.gloss("het klimaat 气候 · wortelen 生根 · besparen 节约 · de verwarming 暖气 · de waarschuwing 预警 · lokaal 当地的、本地的。")',
     'f.gloss("het klimaat = Klima · wortelen = Wurzeln schlagen · besparen = sparen · de verwarming = Heizung · de waarschuwing = Warnung · lokaal = lokal.")')
rep("content12.py", '"气候周你做什么？种树、节约能源还是骑车。写两句荷兰语寄给编辑部。"',
     '"Was machst du in der Klimaatweek: einen Baum pflanzen, Energie sparen oder Rad fahren? Schreib zwei Sätze auf Niederländisch und schicke sie an die Redaktion."')
rep("content12.py", '"DE CODES VAN HET KNMI · 气象预警颜色"', '"DE CODES VAN HET KNMI · KNMI-CODES"')
rep("content12.py", '"Wat betekent elke kleur? · 每种颜色是什么意思"', '"Was bedeutet jede Farbe?"')
rep("content12.py", '"天气可能危险，要当心"', '"Das Wetter kann gefährlich sein: pass auf"')
rep("content12.py", '"危险，做好准备"', '"Gefährlich: bereite dich vor"')
rep("content12.py", '"非常危险，尽量待在室内"', '"Sehr gefährlich: bleib lieber drinnen"')
rep("content12.py", '"预警针对你所在的地区"', '"Die Warnung gilt für deine eigene Umgebung"')
rep("content12.py", '"OEFENINGEN · 第 2 版练习"', '"OEFENINGEN · ÜBUNGEN ZU SEITE 2"')
rep("content12.py", 'e.bridge("读第 2 版文章，选出正确答案。")', 'e.bridge("Lies den Artikel auf Seite 2 und wähle die richtige Antwort.")')
rep("content12.py", '"气候周不做：更多开车"', '"Keine Klimaatweek-Aktion: mehr Auto fahren"')
rep("content12.py", '"红色预警：非常危险，待在室内"', '"Code Rot: sehr gefährlich, bleib drinnen"')
rep("content12.py", '"预警针对本地，不针对整个省"', '"Warnungen sind lokal, nicht für eine ganze Provinz"')
rep("content12.py", '"节约能源：暖气调低一度"', '"Energie sparen: die Heizung einen Grad niedriger stellen"')
rep("content12.py", 'e.bridge("用第 2 版的词填空。")', 'e.bridge("Ergänze mit Wörtern von Seite 2.")')
rep("content12.py", '"气候周 11 月 2–8 日共 7 天"', '"Die Klimaatweek vom 2. bis 8. November dauert 7 Tage"')
rep("content12.py", '"wortelen = 生根（复数主语）"', '"wortelen = Wurzeln schlagen (Plural)"')
rep("content12.py", '"besparen = 节约"', '"besparen = sparen"')
rep("content12.py", '"fiets = 自行车"', '"fiets = Fahrrad"')
rep("content12.py", '"发放地点在兹韦洛"', '"Der Verteilort ist Zweeloo"')
rep("content12.py", 'e.bridge("用颜色代码和日期填空。")', 'e.bridge("Ergänze die Farbcodes und Daten.")')
rep("content12.py", '"黄色代码：当心"', '"Code Gelb: pass auf"')
rep("content12.py", '"橙色代码：危险"', '"Code Orange: gefährlich"')
rep("content12.py", '"发放从 13:00 开始"', '"Die Verteilung beginnt um 13:00 Uhr"')
rep("content12.py", '"气候周 11 月 8 日周日结束"', '"Die Klimaatweek endet am Sonntag, 8. November"')
rep("content12.py", '["Klimaatweek=气候周 b", "besparen=节约 d", "waarschuwing=预警 a", "lokaal=本地的 c"]',
     '["Klimaatweek = Klimawoche b", "besparen = sparen d", "waarschuwing = Warnung a", "lokaal = lokal c"]')

# ---------- content34: P3 ----------
rep("content34.py", '"博物馆之夜在 11 月 7 日周六"', '"Die Museumsnacht ist am Samstag, 7. November"')
rep("content34.py", 'p.band("CULTUUR · 文化", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · 博物馆之夜、书籍与艺术")',
     'p.band("CULTUUR · KULTUR", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · Museumsnacht, Bücher und Kunst")')
rep("content34.py", 'f.gloss("het museum 博物馆 · de rondleiding 导览 · het tijdslot 时间段 · tweedehands 二手的 · de beurs 展会、集市。")',
     'f.gloss("het museum = Museum · de rondleiding = Führung · het tijdslot = Zeitfenster · tweedehands = gebraucht · de beurs = Messe, Markt.")')
rep("content34.py", '"OEFENINGEN · 第 3 版练习"', '"OEFENINGEN · ÜBUNGEN ZU SEITE 3"')
rep("content34.py", 'e.bridge("读第 3 版文章，选出正确答案。")', 'e.bridge("Lies den Artikel auf Seite 3 und wähle die richtige Antwort.")')
rep("content34.py", '"博物馆开放到凌晨 2 点"', '"Die Museen sind bis 02:00 Uhr geöffnet"')
rep("content34.py", '"Crossing Border 在海牙"', '"Crossing Border ist in Den Haag"')
rep("content34.py", '"Crossing Border 结合书籍与音乐"', '"Crossing Border verbindet Bücher und Musik"')
rep("content34.py", '"PAN 艺术博览会到 11 月 8 日"', '"Die Kunstmesse PAN läuft bis zum 8. November"')
rep("content34.py", 'e.bridge("用方框里的词填空。注意：有的词要变成复数。")',
     'e.bridge("Ergänze mit den Wörtern aus dem Kasten. Achtung: Manche Wörter werden Plural.")')
rep("content34.py", '"museum 复数：musea"', '"museum Plural: musea"')
rep("content34.py", '"rondleiding = 导览"', '"rondleiding = Führung"')
rep("content34.py", '"tijdslot = 时间段"', '"tijdslot = Zeitfenster"')
rep("content34.py", '"tweedehands = 二手的"', '"tweedehands = gebraucht"')
rep("content34.py", '"beurs = 展会、集市"', '"beurs = Messe, Markt"')
rep("content34.py", 'e.bridge("用现在完成时补全，注意助动词 hebben/zijn。")',
     'e.bridge("Ergänze im Perfekt. Achte auf die Hilfsverben hebben/zijn.")')
rep("content34.py", '"zijn 的 perfectum：zijn geweest"', '"zijn Perfekt: zijn geweest"')
rep("content34.py", '"kopen 的 perfectum：hebben gekocht"', '"kopen Perfekt: hebben gekocht"')
rep("content34.py", '"voorlezen 的 perfectum：hebben voorgelezen"', '"voorlezen Perfekt: hebben voorgelezen"')
rep("content34.py", '"komen 用 zijn：zijn gekomen"', '"komen mit zijn: zijn gekomen"')
rep("content34.py", 'e.bridge("算一算：用第 3 版的数字回答。")', 'e.bridge("Rechne: Antworte mit den Zahlen von Seite 3.")')
rep("content34.py", '"19:00 到 02:00 共 7 小时"', '"Von 19:00 bis 02:00 Uhr sind es 7 Stunden"')
rep("content34.py", '"11 月 1–8 日共 8 天"', '"Vom 1. bis 8. November sind es 8 Tage"')
rep("content34.py", '"11 月 3–8 日共 6 天"', '"Vom 3. bis 8. November sind es 6 Tage"')
rep("content34.py", '"250 的一半是 125"', '"Die Hälfte von 250 ist 125"')
# ---------- content34: P4 ----------
rep("content34.py", 'p.band("SPORT · 体育", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · 欧战周与第 12 轮")',
     'p.band("SPORT · SPORT", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · Europawoche und 12. Spieltag")')
rep("content34.py", 'f.gloss("de balans 成绩单、总结 · gelijkspelen 打平 · de speelronde 轮次 · de topper 焦点战 · de stand 积分榜。")',
     'f.gloss("de balans = Bilanz, Fazit · gelijkspelen = unentschieden spielen · de speelronde = Spieltag · de topper = Spitzenspiel · de stand = Tabelle.")')
rep("content34.py", '"OEFENINGEN · 第 4 版练习"', '"OEFENINGEN · ÜBUNGEN ZU SEITE 4"')
rep("content34.py", 'e.bridge("读第 4 版文章，选出正确答案。")', 'e.bridge("Lies den Artikel auf Seite 4 und wähle die richtige Antwort.")')
rep("content34.py", '"阿贾克斯 2–0 赢亚特兰大"', '"Ajax gewann mit 2–0 gegen Atalanta"')
rep("content34.py", '"特温特 4–1 赢林肯红魔"', '"Twente gewann mit 4–1 gegen Lincoln"')
rep("content34.py", '"NEC 2–4 输给萨格勒布迪纳摩"', '"NEC verlor mit 2–4 gegen Dinamo Zagreb"')
rep("content34.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"Real Betis gewann mit 1–0 gegen Feyenoord"')
rep("content34.py", '"10 轮后费耶诺德 24 分领跑"', '"Nach 10 Runden führt Feyenoord mit 24 Punkten"')
rep("content34.py", 'e.bridge("用方框里的词填空。注意动词形式。")',
     'e.bridge("Ergänze mit den Wörtern aus dem Kasten. Achte auf die Verbformen.")')
rep("content34.py", '"balans = 成绩单、总结"', '"balans = Bilanz, Fazit"')
rep("content34.py", '"gelijkspelen 过去时复数：speelden gelijk"', '"gelijkspelen Vergangenheit Plural: speelden gelijk"')
rep("content34.py", '"topper = 焦点战"', '"topper = Spitzenspiel"')
rep("content34.py", '"stand = 积分榜"', '"stand = Tabelle"')
rep("content34.py", '"doelpunt = 进球"', '"doelpunt = Tor"')
rep("content34.py", 'e.bridge("用过去时或完成时补全。")', 'e.bridge("Ergänze in der Vergangenheit oder im Perfekt.")')
rep("content34.py", '"winnen 过去时：won"', '"winnen Vergangenheit: won"')
rep("content34.py", '"gaan 过去时：ging"', '"gaan Vergangenheit: ging"')
rep("content34.py", '"verliezen 过去时：verloor"', '"verliezen Vergangenheit: verloor"')
rep("content34.py", '"komen 的 perfectum 用 zijn"', '"komen Perfekt mit zijn"')
rep("content34.py", '"对：阿贾克斯 2–0 获胜"', '"Richtig: Ajax gewann mit 2–0"')
rep("content34.py", '"错：NEC 2–4 输了"', '"Falsch: NEC verlor mit 2–4"')
rep("content34.py", '"错：特温特–阿贾克斯 13:30；11:15 是海伦芬–费耶诺德"', '"Falsch: Twente–Ajax ist um 13:30 Uhr; 11:15 Uhr ist Heerenveen–Feyenoord"')
rep("content34.py", '"对：10 轮后费耶诺德 24 分第一"', '"Richtig: Nach 10 Runden führt Feyenoord mit 24 Punkten"')

# ---------- content56: P5 ----------
rep("content56.py", 'p.band("JONGEREN · 青年", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 荒岛节目开播、音乐节与设计周落幕")',
     'p.band("JONGEREN · JUGEND", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · Robinson ist gestartet, ADE und DDW sind vorbei")')
rep("content56.py", "（周日晚 20:00 在 RTL 4 收看）", "(am Sonntag um 20:00 Uhr auf RTL 4 sehen)")
rep("content56.py", "（注意比赛项目：分数在那里决出）", "(achte auf die Prüfungen: dort werden die Punkte vergeben)")
rep("content56.py", "（和朋友猜谁能留到最后）", "(rate mit Freunden, wer am längsten bleibt)")
rep("content56.py", "（下周这里继续报道进展）", "(nächste Woche liest du hier, wie es weitergeht)")
rep("content56.py", 'f.gloss("het eiland 岛 · de proef 比赛项目、考验 · stemmen 投票 · de aflevering （一）集 · voorbij 过去了、结束了。")',
     'f.gloss("het eiland = Insel · de proef = Prüfung, Wettkampf · stemmen = abstimmen · de aflevering = Folge · voorbij = vorbei, zu Ende.")')
rep("content56.py", '"你看《荒岛远征》吗，还是更爱自己出门活动？写两句荷兰语寄来。"',
     '"Schaust du Expeditie Robinson oder machst du lieber selbst etwas draußen? Schreib zwei Sätze auf Niederländisch und schicke sie ein."')
rep("content56.py", '"OEFENINGEN · 第 5 版练习"', '"OEFENINGEN · ÜBUNGEN ZU SEITE 5"')
rep("content56.py", 'e.bridge("读第 5 版文章，选出正确答案。")', 'e.bridge("Lies den Artikel auf Seite 5 und wähle die richtige Antwort.")')
rep("content56.py", '"Robinson 在 11 月 1 日周日开始"', '"Robinson startete am Sonntag, 1. November"')
rep("content56.py", '"19 位参赛者"', '"19 Teilnehmer"')
rep("content56.py", '"ADE 今年 30 年"', '"ADE wurde dieses Jahr 30 Jahre alt"')
rep("content56.py", '"设计周约 2.500 位设计师"', '"Die Design Week zeigte etwa 2.500 Designer"')
rep("content56.py", '"ADE 与 DDW 在 10 月 25 日周日落幕"', '"ADE und DDW endeten am Sonntag, 25. Oktober"')
rep("content56.py", 'e.bridge("用方框里的词填空。")', 'e.bridge("Ergänze mit den Wörtern aus dem Kasten.")')
rep("content56.py", '"eiland = 岛（het）"', '"eiland = Insel (het)"')
rep("content56.py", '"proef = 比赛项目、考验（de）"', '"proef = Prüfung, Wettkampf (de)"')
rep("content56.py", '"stemmen = 投票"', '"stemmen = abstimmen"')
rep("content56.py", '"aflevering = （一）集"', '"aflevering = Folge"')
rep("content56.py", '"voorbij = 过去了、结束了"', '"voorbij = vorbei, zu Ende"')
rep("content56.py", '"kandidaat 复数：kandidaten"', '"kandidaat Plural: kandidaten"')
rep("content56.py", 'e.bridge("用 gaan + 不定式说将来。")', 'e.bridge("Sprich mit gaan + Infinitiv über die Zukunft.")')
rep("content56.py", '"gaat winnen = 会赢（只是猜测）"', '"gaat winnen = wird gewinnen (nur eine Vermutung)"')
rep("content56.py", '"wij → gaan + 不定式 kijken"', '"wij → gaan + Infinitiv kijken"')
rep("content56.py", '"zij (复数) → gaan zoeken"', '"zij (Plural) → gaan zoeken"')
rep("content56.py", '"对：11 月 1 日开始"', '"Richtig: Start am 1. November"')
rep("content56.py", '"错：ADE 今年 30 年"', '"Falsch: ADE wurde dieses Jahr 30 Jahre alt"')
rep("content56.py", '"错：10 月 25 日已落幕"', '"Falsch: schon am 25. Oktober zu Ende"')
# ---------- content56: P6 ----------
rep("content56.py", 'p.band("VERDIEPING · 深读", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · 气象预警深度解读")',
     'p.band("VERDIEPING · VERTIEFUNG", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · Die KNMI-Codes im Detail")')
rep("content56.py", 'f.gloss("de meteoroloog 气象学家 · waarschuwingsmoeheid 预警疲劳 · vastzetten 固定好 · het advies 建议、忠告 · de voorstander 支持者。")',
     'f.gloss("de meteoroloog = Meteorologe · waarschuwingsmoeheid = Warnmüdigkeit · vastzetten = befestigen · het advies = Rat, Empfehlung · de voorstander = Befürworter.")')
rep("content56.py", '"练习数据：虚构数字，仅供练习，非真实调查。问题：橙色预警时你会怎么做？（100 名年轻人）"',
     '"ÜBUNGSDATEN: erfundene Zahlen, nur zum Üben, keine echte Umfrage. Frage: Was machst du bei Code Orange? (100 junge Leute)"')
rep("content56.py", '"DE GRAFIEK · 图表（练习数据）"', '"DE GRAFIEK · ÜBUNGSDATEN"')
rep("content56.py", '"VOOR OF TEGEN? · 正方还是反方"', '"VOOR OF TEGEN? · DAFÜR ODER DAGEGEN?"')
rep("content56.py", '"OEFENINGEN · 第 6 版练习"', '"OEFENINGEN · ÜBUNGEN ZU SEITE 6"')
rep("content56.py", 'e.bridge("看第 6 版图表（练习数据）回答。")', 'e.bridge("Antworte anhand der Grafik auf Seite 6 (Übungsdaten).")')
rep("content56.py", '"45 名年轻人选择待在家里"', '"45 junge Leute bleiben zu Hause"')
rep("content56.py", '"25 人先看预警文字"', '"25 lesen zuerst den Warntext"')
rep("content56.py", '"10 人不知道"', '"10 wissen es nicht"')
rep("content56.py", '"图表共 100 人：45+25+20+10"', '"Die Grafik zählt 100 Leute: 45+25+20+10"')
rep("content56.py", 'e.bridge("读第 6 版文章，选出正确答案。")', 'e.bridge("Lies den Artikel auf Seite 6 und wähle die richtige Antwort.")')
rep("content56.py", '"以前预警针对整个省"', '"Früher galten Warnungen für eine ganze Provinz"')
rep("content56.py", '"如今预警是本地的"', '"Heute sind Warnungen lokal"')
rep("content56.py", '"红色：非常危险，非必要不上路"', '"Code Rot: sehr gefährlich, nur raus, wenn es sein muss"')
rep("content56.py", '"预警疲劳：警告太多导致不再注意"', '"Warnmüdigkeit: zu viele Warnungen, man passt nicht mehr auf"')
rep("content56.py", '"KNMI 说：看代码旁边的文字"', '"Das KNMI sagt: Lies den Text neben dem Code"')
rep("content56.py", '"lokaal = 本地的"', '"lokaal = lokal"')
rep("content56.py", '"waarschuwingsmoeheid = 预警疲劳"', '"waarschuwingsmoeheid = Warnmüdigkeit"')
rep("content56.py", '"vastzetten = 固定好"', '"vastzetten = befestigen"')
rep("content56.py", '"advies = 建议（het）"', '"advies = Rat (het)"')
rep("content56.py", 'e.bridge("把词组成正确的句子。")', 'e.bridge("Bringe die Wörter in die richtige Reihenfolge.")')
rep("content56.py", '"主语 + 动词 + 地点"', '"Subjekt + Verb + Ort"')
rep("content56.py", '"祈使句：动词在首位"', '"Imperativ: das Verb steht vorn"')
rep("content56.py", '"weinig voor = 很少出现"', '"weinig voor = selten vorkommen"')
rep("content56.py", '"raakt + 宾语 + 方式"', '"raakt + Objekt + Art und Weise"')

# ---------- content7: P7 ----------
rep("content7.py", 'p.band("TAAL · 语言", "De Lucerna", "聚焦语言 · Drie niveaus, drie gereedschappen · 三个级别，三件工具")',
     'p.band("TAAL · SPRACHE", "De Lucerna", "Sprachfokus · Drie niveaus, drie gereedschappen · Drei Stufen, drei Werkzeuge")')
rep("content7.py", 'a.bridge("het klimaat 气候（长期）；een boom planten 种树；besparen 节约；de waarschuwing 预警。")',
     'a.bridge("het klimaat = Klima (langfristig); een boom planten = einen Baum pflanzen; besparen = sparen; de waarschuwing = Warnung.")')
rep("content7.py", '"气候是长期的天气与自然"', '"Das Klima ist das Wetter und die Natur über lange Zeit"')
rep("content7.py", 'b.bridge("meedoen 参加：ik doe mee；opruimen 收拾：wij hebben opgeruimd；vastzetten 固定：zij zette vast。")',
     'b.bridge("meedoen = teilnehmen: ik doe mee; opruimen = aufräumen: wij hebben opgeruimd; vastzetten = befestigen: zij zette vast.")')
rep("content7.py", '"opruimen 的分词：opgeruimd"', '"opruimen Partizip: opgeruimd"')
rep("content7.py", '"vastzetten 过去时：zette vast"', '"vastzetten Vergangenheit: zette vast"')
rep("content7.py", '"meedoen = 参加、参与"', '"meedoen = teilnehmen, dabei sein"')
rep("content7.py", 'c.bridge("Ik vind dat… 我认为；Volgens mij… 依我看；Het lijkt me dat… 在我看来。")',
     'c.bridge("Ik vind dat… = Ich finde, dass…; Volgens mij… = Meiner Meinung nach…; Het lijkt me dat… = Mir scheint, dass…")')
rep("content7.py", '"Volgens mij… = 依我看"', '"Volgens mij… = Meiner Meinung nach…"')
rep("content7.py", '"Ik vind dat… 表达看法"', '"Ik vind dat… drückt eine Meinung aus"')
rep("content7.py", '"Het lijkt me dat… = 在我看来"', '"Het lijkt me dat… = Mir scheint, dass…"')
rep("content7.py", '"气候是长期的天气自然，不是今天的天气。"', '"Das Klima ist das Wetter über lange Zeit, nicht das Wetter von heute."')
rep("content7.py", '"Klimaatweek 是专名，首字母大写。"', '"Klimaatweek ist ein Name und schreibt sich groß."')
rep("content7.py", '"een 是单数：een boom；复数直接用 bomen。"', '"«Een» ist Singular: «een boom» oder «bomen»."')
rep("content7.py", '"omdat 从句后，主句动词在第二位：blijf ik thuis。"', '"Nach «omdat» steht das Verb im Hauptsatz an zweiter Stelle: «... blijf ik thuis»."')
rep("content7.py", '"PAS OP! · 易错诊所"', '"PAS OP! · FEHLERKLINIK"')
rep("content7.py", '"meedoen = 参加、参与：气候周全荷兰都参加。"', '"meedoen = teilnehmen, dabei sein: In der Klimaatweek macht ganz Holland mit."')
rep("content7.py", '"HET WOORD · 本周生词"', '"HET WOORD · WORT DER WOCHE"')
# readers' corner: Dutch example letter + Dutch disclosure stay verbatim (frozen);
# the Chinese disclosure + invitation lines become German. The German disclosure
# states all three facts (no real letters, no best P8 texts, example + VOL.3
# promise); the invitation is an explicit imperative with a print promise.
rep("content7.py", 'dt_zh = "截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。"',
     'dt_de = "Bei Redaktionsschluss waren noch keine echten Briefe und keine besten Seite-8-Texte eingegangen — darum dieses Beispiel; das Versprechen gilt für VOL.3."')
rep("content7.py", 'len(wrap(dt_zh, "sans", False, 20, CW - 44))', 'len(wrap(dt_de, "sans", False, 20, CW - 44))')
rep("content7.py", 'p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
     'p.para(bx + 22, yy3 + 20, dt_de, 20, "sans", False, GREY, CW - 44, 1.42) + 10')
rep("content7.py", '"编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！"',
     '"Beispielbrief der Redaktion, kein echter Brief. Schicke uns deinen echten Brief und deinen besten Text von Seite 8 — wir drucken sie in VOL.3!"')
rep("content7.py", '"ZINNEN VAN DE WEEK · 本周金句（逐字摘自本期文章）"',
     '"ZINNEN VAN DE WEEK · SÄTZE DER WOCHE (WÖRTLICH AUS DIESER AUSGABE)"')
rep("content7.py", '"从 11 月 2 日周一到 8 日周日，荷兰是气候周。"', '"Von Montag, 2. November, bis Sonntag, 8. November, ist in den Niederlanden Klimaatweek."')
rep("content7.py", '"秋天是种树的最好时节。"', '"Der Herbst ist die beste Zeit zum Pflanzen."')
rep("content7.py", '"黄色意味着：当心，天气可能危险。"', '"Gelb bedeutet: pass auf, das Wetter kann gefährlich sein."')
rep("content7.py", '"70 多家博物馆从晚上 19 点开放到凌晨 2 点。"', '"Mehr als 70 Museen sind von 19:00 Uhr abends bis 02:00 Uhr nachts geöffnet."')
rep("content7.py", '"阿贾克斯 10 月 22 日周四 2–0 战胜亚特兰大。"', '"Am Donnerstag, 22. Oktober, gewann Ajax mit 2–0 gegen Atalanta."')
rep("content7.py", '"11 月 1 日周日，《荒岛远征》在 RTL 4 开播，20 点。"', '"Am Sonntag, 1. November, startete Expeditie Robinson auf RTL 4 um 20:00 Uhr."')
rep("content7.py", '"预警代码不是禁令，而是一条建议。"', '"Ein Code ist kein Verbot, sondern ein Rat."')
rep("content7.py", '"天气属于我们所有人，但对每个人的影响各不相同。"', '"Das Wetter gehört uns allen, aber es trifft uns alle anders."')
rep("content7.py", '"VOLGENDE WEEK · 下期预告 (VOL.3)"', '"VOLGENDE WEEK · VORSCHAU (VOL.3)"')
# ---------- content8: P8 (remaining notes) ----------
rep("content8.py", '"发放地点在兹韦洛"', '"Der Verteilort ist Zweeloo"')
rep("content8.py", '"科弗登发放 200 棵树木灌木"', '"Coevorden verteilt 200 Bäume und Sträucher"')
rep("content8.py", '"特温特–阿贾克斯 13:30 开球"', '"Twente–Ajax beginnt um 13:30 Uhr"')
rep("content8.py", '"预警疲劳：警告太多导致不再注意"', '"Warnmüdigkeit: zu viele Warnungen, man passt nicht mehr auf"')
rep("content8.py", '"阿贾克斯 2–0 赢亚特兰大"', '"Ajax gewann mit 2–0 gegen Atalanta"')
rep("content8.py", '"Crossing Border 在海牙"', '"Crossing Border ist in Den Haag"')
rep("content8.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"Real Betis gewann mit 1–0 gegen Feyenoord"')
rep("content8.py", 'p.band("TOETS EN ANTWOORDEN · 练习与答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")',
     'p.band("TOETS EN ANTWOORDEN · TEST UND ANTWORTEN", "De Lucerna", "Seite 8 · De grote toets van de week + alle antwoorden")')
rep("content8.py", '"气候周到 11 月 8 日"', '"Die Klimaatweek dauert bis zum 8. November"')
rep("content8.py", '"博物馆之夜在 11 月 7 日"', '"Die Museumsnacht ist am 7. November"')
rep("content8.py", '"Robinson 在 11 月开始"', '"Robinson startete im November"')
rep("content8.py", '"橙色预警：天气危险"', '"Code Orange: das Wetter ist gefährlich"')
rep("content8.py", '"meedoen = 参加"', '"meedoen = teilnehmen"')
rep("content8.py", '"气候周 11 月 2 日周一开始"', '"Die Klimaatweek beginnt am Montag, 2. November"')
rep("content8.py", '"PAN 在 RAI 展览中心"', '"PAN ist in der RAI"')
rep("content8.py", '"10 轮后阿贾克斯 21 分"', '"Nach 10 Runden hat Ajax 21 Punkte"')
rep("content8.py", '"扎安丹旧货市场约 250 个摊位"', '"Der Flohmarkt in Zaandam hat etwa 250 Stände"')
rep("content8.py", '"Daan 住在科弗登"', '"Daan wohnt in Coevorden"')
rep("content8.py", '"他周六领了一棵免费灌木"', '"Am Samstag holt er einen kostenlosen Strauch ab"')
rep("content8.py", '"周日特温特对阿贾克斯"', '"Am Sonntag spielt Twente gegen Ajax"')
rep("content8.py", '"气候周他每天骑车上学"', '"In der Klimaatweek fährt er jeden Tag mit dem Rad zur Schule"')
rep("content8.py", '"主语 + 动词 + 时间"', '"Subjekt + Verb + Zeit"')
rep("content8.py", '"主语 + 动词 + 宾语 + 地点"', '"Subjekt + Verb + Objekt + Ort"')
rep("content8.py", '"主语 + 动词 + 时间 + 对手"', '"Subjekt + Verb + Zeit + Gegner"')
rep("content8.py", '"可分动词 mee 在句末"', '"Trennbares Verb: mee steht am Ende"')
rep("content8.py", '"对照第 1 版头条"', '"Vergleiche die Schlagzeile auf Seite 1"')
rep("content8.py", '"第 2 版原句 · bereid je voor 做好准备"', '"Originalsatz von Seite 2 · bereid je voor = bereite dich vor"')
rep("content8.py", '"注意时间表达 van...tot..."', '"Beachte die Zeitangabe van...tot..."')
rep("content8.py", '"meedoen 是可分动词"', '"meedoen ist ein trennbares Verb"')
rep("content8.py", '["klimaat=气候 c", "meedoen=参加 b", "waarschuwing=预警 a", "vastzetten=固定好 d"]',
     '["klimaat = Klima c", "meedoen = teilnehmen b", "waarschuwing = Warnung a", "vastzetten = befestigen d"]')
rep("content8.py", '"boom = 树"', '"boom = Baum"')
rep("content8.py", '"struik = 灌木"', '"struik = Strauch"')
rep("content8.py", '"planten = 种"', '"planten = pflanzen"')
rep("content8.py", '"zachte = 柔软的（土壤）"', '"zachte = weich (Boden)"')
rep("content8.py", '"发放到 16:00 结束"', '"Die Verteilung endet um 16:00 Uhr"')
rep("content8.py", '"（开放题，范文如下）"', '"(offene Aufgabe, Mustertext unten)"')
rep("content8.py", 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"Mustertext in Abschnitt H auf dieser Seite ({NWORDS} Wörter)"')
rep("content8.py", '"ANTWOORDEN · 参考答案 — 按版面分页排列，找到题号即可"',
     '"ANTWOORDEN · ANTWORTEN — nach Seiten geordnet, finde deine Nummer"')
rep("content8.py", '"每题附一句中文简析 · 带 ✓ 的为范文题"',
     '"Jede Antwort hat eine kurze Erklärung auf Deutsch · ✓ markiert die Schreibaufgabe"')

# ---------- apply ----------
def main():
    fails = []
    for item in R:
        f, old, new = item[0], item[1], item[2]
        opt = len(item) > 3
        path = os.path.join(HERE, f)
        txt = open(path, encoding="utf-8").read()
        n = txt.count(old)
        if n == 0 and not opt:
            fails.append((f, old[:70]))
        txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
        print(f"{f}: {n}x {old[:60]!r}")
    print("TOTAL replacements:", len(R))
    if fails:
        print("FAILED (0 hits):")
        for f, o in fails:
            print("  ", f, repr(o))
        sys.exit(1)

if __name__ == "__main__":
    main()
