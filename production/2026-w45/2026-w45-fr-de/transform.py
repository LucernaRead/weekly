# -*- coding: utf-8 -*-
"""FR x DE fan-out transform for W45 FR core build copy (VOL.3).

Rules (tools/README #17/#18): whole-string or exact-unique-literal
replacements with count assertions; value maps use bare text, never repr.
French target text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token, except the documented re-aimed P8 translation items
(E1 key/note/stem, E2-E5 stems) and the P8 printing rule (see below).
Furniture follows the SHIPPED W43 FR x DE edition
(files/weekly-report-fr-de/), which wins over any generic rule:
badge INSERTED at y=574, 22pt BRICK, centred, German form;
footer VOL.3 in the canonical DE template; gloss prefix "HINWEIS · ";
short bilingual heads (WÖRTER, TERMINE, DISKUSSION, SIE SIND DRAN,
ÜBUNGEN, AUFBAU, VERTIEFUNG, WERKZEUG, KLINIK, LESERECKE).

P8 printed-note set: the core's rule (page 8 always, or note <= 10 chars,
or clinic/chart types) cannot survive translation, because German notes
are longer. Following the W43 FR x DE precedent, the edition carries
the core's printed set EXPLICITLY (PRINT_NOTES, measured from the core
P8 with tools/p8.py extract --json: 97 numbers) so the same exercises
carry printed notes in both editions. Bare keys (53) are untouched.
Run once from the build dir copy. Idempotent? No — run once only.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = []


def rep(fname, old, new, expect=None):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    else:
        assert n >= 1, f"{fname}: {old!r} not found in {fname}"
    LOG.append(f"{fname}: {n}x {old!r} -> {new!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))


def rep_all(fname, pairs):
    # longest old first: avoids a short literal corrupting a longer one
    # that contains it (e.g. a note inside a longer note string).
    for old, new in sorted(pairs, key=lambda t: -len(t[0])):
        rep(fname, old, new)


# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-fr-core", "weekly-report-w45-fr-de", 1)

# ---------- bslib4: furniture + gloss prefix (W43 shipped forms, VOL.3) ----------
rep("bslib4.py",
    '"Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文"',
    '"Le Lucerna · FRANZÖSISCHE WOCHENZEITUNG VOL.3 · TEXT AUF FRANZÖSISCH · ERKLÄRUNGEN AUF DEUTSCH"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"HINWEIS · " + s', 1)

# ---------- content12: P1 + P2 ----------
rep_all("content12.py", [
    ("VOL. 3 · 总第 3 期", "VOL. 3 · AUSGABE NR. 3"),
    ("HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语",
     "HEBDOMADAIRE EN FRANÇAIS · JEDE WOCHE · FRANZÖSISCH, WIE FRANKREICH ES LIEST"),
    ("法 语 周 报 · VOL.3 · 决 赛 周 末", "FRANZÖSISCHE WOCHENZEITUNG · VOL.3 · FINALWOCHENENDE"),
    ("周一开学 · 全法同步复课", "MONTAG SCHULBEGINN · IN GANZ FRANKREICH"),
    ("大师赛开赛 · 音乐节开幕 · 详见第 2 版", "MASTERS-BEGINN · FESTIVAL-ERÖFFNUNG · SIEHE SEITE 2"),
    ("法语正文 · 简体中文讲解 — 给简体中文读者的版本",
     "FRANZÖSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"),
    ("SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末",
     "SPORT · CULTURE · GASTRONOMIE · LA UNE · FINALWOCHENENDE"),
    ("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。",
     "se jouer den Ausgang entscheiden, sich abspielen · une finale Endspiel, Finale · une demi-finale Halbfinale · un quart de finale Viertelfinale · une nocturne Nachtveranstaltung · un frisson Schauer, Nervenkitzel · la coquille Saint-Jacques Jakobsmuschel."),
    ("LES DATES · 决赛周末日程", "LES DATES · FINALWOCHENENDE"),
    ("À VOUS ! · 即学即练", "À VOUS ! · SIE SIND DRAN"),
    ("周日 8 日举行决赛", "Finale am Sonntag, 8. Nov."),
    ("周六 7 日晚是最后夜场", "Letzte Nachtveranstaltung am Samstag, 7. Nov."),
    ("波尔诺曼底卖扇贝", "In Port-en-Bessin gibt es Jakobsmuscheln"),
    ("周一 2 日全法复课", "Schulbeginn am Montag, 2. Nov., in ganz Frankreich"),
    ("半决赛后才知道决赛选手", "Finalisten erst nach den Halbfinals bekannt"),
    ("三个决赛：网球、刺激、美味", "Drei Finals: Tennis, Nervenkitzel, Genuss"),
    ("本周日程 · 11 月 2 日至 8 日", "WOCHENPLAN · 2. BIS 8. NOVEMBER"),
    ("周末决赛结果周六晚、周日揭晓。", "Finalergebnisse: Sa.-Abend und So."),
    ("DANS CE NUMÉRO · 本期目录", "DANS CE NUMÉRO · INHALT"),
    ("决出胜负；上演。本周末一切都将见分晓。",
     "Sich entscheiden; sich abspielen. An diesem Wochenende entscheidet sich alles."),
    ("EN BREF · 快讯", "EN BREF · KURZ GEMELDET"),
    ("QUIZ ÉCLAIR · 闪电问答", "QUIZ ÉCLAIR · BLITZQUIZ"),
    ("读头版，选出正确答案 · 答案见第 8 版",
     "Titelseite lesen, richtig antworten · Antworten auf Seite 8"),
    ("决赛在周日 8 日", "Finale am Sonntag, 8. November"),
    ("扇贝节在滨海波尔", "Muschelfest in Port-en-Bessin"),
    ("周一 2 日早上全区复课", "Schulbeginn am Montagmorgen, 2. November"),
    ("最后夜场周六 7 日", "Letzte Nachtveranstaltung am Samstag, 7. November"),
    ("VIE QUOTIDIENNE · 生活", "VIE QUOTIDIENNE · LEBEN"),
    ("NIVEAU A2 · La rentrée · 开学复课", "NIVEAU A2 · La rentrée · SCHULBEGINN"),
    ("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。",
     "la rentrée Schulbeginn, Wiederbeginn · reprendre wieder beginnen, wieder aufnehmen · un cartable Schultasche · un décalage Verschiebung, Zeitunterschied · en revanche dagegen, andererseits · un rituel Gewohnheit, Ritual."),
    ("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。",
     "HINWEIS · une valise Koffer · une ambiance Stimmung · le bilan Bilanz, Rückblick."),
    ("说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。",
     "Erzählen Sie von Ihrem Schulbeginn: Wo waren Sie am Montagmorgen? Welches Buch haben Sie in den Ferien gelesen? Schreiben Sie zwei Sätze auf Französisch an die Redaktion."),
    ("ET VOUS ? · 说说你自己", "ET VOUS ? · UND SIE?"),
    ("DIRE LA DATE · 这样说日期", "DIRE LA DATE · SO SAGT MAN DAS DATUM"),
    ("lundi 2 novembre · 注意：1 日说 le premier，其余用基数词",
     "lundi 2 novembre · Achtung: Am 1. sagt man le premier, sonst Grundzahlen"),
    ("11 月 2 日星期一 · la rentrée", "Montag, 2. November · la rentrée"),
    ("11 月 3 日星期二 · votes à l'Assemblée", "Dienstag, 3. November · votes à l'Assemblée"),
    ("11 月 4 日星期三 · sorties cinéma", "Mittwoch, 4. November · sorties cinéma"),
    ("11 月 7 日星期六 · nocturne et demis", "Samstag, 7. November · nocturne et demis"),
    ("11 月 8 日星期日 · les finales", "Sonntag, 8. November · les finales"),
    ("EXERCICES · 第 2 版练习", "EXERCICES · ÜBUNGEN SEITE 2"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Antworten auf Seite 8 · Niveaugemischt; suchen Sie nach der Nummer"),
    ("用法语补全日期（注意星期与数字）。",
     "Ergänzen Sie das Datum auf Französisch (Wochentag und Zahl beachten)."),
    ("复课在星期一", "Schulbeginn am Montag"),
    ("11 月 1 日说 le premier", "Am 1. November sagt man le premier"),
    ("最后夜场在星期六", "Letzte Nachtveranstaltung am Samstag"),
    ("决赛在星期日", "Finale am Sonntag"),
    ("用 aller + 动词原形改写（最近将来时）。",
     "Schreiben Sie mit aller + Infinitiv um (futur proche)."),
    ("读第 2 版文章，选出正确答案。",
     "Lesen Sie den Artikel auf Seite 2 und wählen Sie die richtige Antwort."),
    ("三区同一周一早上复课", "Alle drei Zonen beginnen am Montagmorgen"),
    ("冬令时从 10 月 25 日开始", "Winterzeit seit dem 25. Oktober"),
    ("11 月晚上天黑得早", "Im November wird es abends früh dunkel"),
    ("rentrée=开学 a", "rentrée=Schulbeginn a"),
    ("reprendre=重新开始 b", "reprendre=wieder beginnen b"),
    ("cartable=书包 c", "cartable=Schultasche c"),
    ("rituel=习惯 d", "rituel=Gewohnheit d"),
])

# ---------- content34: P3 + P4 ----------
rep_all("content34.py", [
    ("CULTURE · 文化", "CULTURE · KULTUR"),
    ("NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣",
     "NIVEAU A2 → B1 · Halloween, Toussaint · HALLOWEEN & TOUSSAINT"),
    ("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。",
     "se déguiser sich verkleiden · un sort Zauber, Streich · une ambiance Stimmung · le souvenir Erinnerung, Gedenken · confondre verwechseln · discret dezent, leise."),
    ("判断对错（Vrai / Faux）。", "Richtig oder falsch? (Vrai / Faux)"),
    ("万圣节在 10 月 31 日星期六", "Halloween war am Samstag, 31. Oktober"),
    ("诸圣节墓园摆满菊花", "An Toussaint sind die Friedhöfe voller Chrysanthemen"),
    ("菊花绝不能当礼物送人", "Chrysanthemen schenkt man nie"),
    ("11 月 2 日是 jour des morts，不是诸圣节", "2. November ist jour des morts, nicht Toussaint"),
    ("文中：le rire d'abord, le souvenir ensuite", "Im Text: le rire d'abord, le souvenir ensuite"),
    ("用 déguisement / tombe / citrouille / souvenir 填空。",
     "Ergänzen Sie mit déguisement / tombe / citrouille / souvenir."),
    ("万圣节穿变装服装", "An Halloween tragen Kinder Kostüme"),
    ("花放在墓碑上", "Blumen stehen auf dem Grab"),
    ("南瓜是万圣节的象征", "Der Kürbis ist das Symbol von Halloween"),
    ("诸圣节是纪念之日", "Toussaint ist ein Gedenktag"),
    ("改写句子（用 ne...jamais / ne...plus / ne...pas）。",
     "Schreiben Sie die Sätze um (mit ne...jamais / ne...plus / ne...pas)."),
    ("jamais + de（无冠词变化）", "jamais + de (ohne Artikeländerung)"),
    ("ne...plus = 不再", "ne...plus = nicht mehr"),
    ("n'est pas = 不是", "n'est pas = ist nicht"),
    ("即学即练 · 公园万圣节小题。", "Kurz üben · Fragen zu Halloween im Park."),
    ("周六 7 日是最后夜场", "Samstag, 7.: letzte Nachtveranstaltung"),
    ("敏感儿童有免费驱怪徽章", "Empfindsame Kinder erhalten ein kostenloses Monster-Abzeichen"),
    ("阿斯泰里克斯公园在 Plailly", "Der Parc Astérix liegt in Plailly"),
    ("Peur sur le Parc 10 月 3 日至 11 月 8 日", "Peur sur le Parc vom 3. Oktober bis 8. November"),
    ("恐惧等级用颜色区分", "Die Angststufen unterscheiden sich nach Farben"),
    ("夜场从 19 点到凌晨 1 点", "Die Nachtveranstaltung dauert von 19 bis 1 Uhr"),
    ("LES MOTS DES FÊTES · 节日词表", "LES MOTS DES FÊTES · WÖRTER"),
    ("un saint — 圣人", "un saint — Heiliger"),
    ("un cimetière — 墓园", "un cimetière — Friedhof"),
    ("une tombe — 坟墓", "une tombe — Grab"),
    ("un jour férié — 公共假日", "un jour férié — Feiertag"),
    ("se souvenir — 纪念、想起", "se souvenir — sich erinnern, gedenken"),
    ("un déguisement — 变装服装", "un déguisement — Kostüm"),
    ("une citrouille — 南瓜", "une citrouille — Kürbis"),
    ("un bonbon — 糖果", "un bonbon — Bonbon"),
    ("un fantôme — 幽灵", "un fantôme — Gespenst"),
    ("un sort — 魔法、诅咒", "un sort — Zauber, Fluch"),
    ("10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。",
     "Vom 3. Oktober bis 8. November: 12 Nachtveranstaltungen, die letzte am Samstag, 7. November. Tagsüber geöffnet von 10 bis 19 Uhr."),
    ("DATES À RETENIR · 本周日历", "DATES À RETENIR · TERMINE"),
    ("注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。",
     "Achtung: Dieppe erst am 14.–15. November, nicht diese Woche."),
    ("SPORT · 体育", "SPORT"),
    ("À VOUS ! · 即学即练", "À VOUS ! · SIE SIND DRAN"),
    ("决赛在周日 8 日", "Finale am Sonntag, 8. November"),
    ("LE DÉBAT · 讨论", "LE DÉBAT · DISKUSSION"),
    ("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。",
     "un tournoi Turnier, Wettkampf · sur dur auf Hartplatz · en salle in der Halle · un tableau principal Hauptfeld · le tenant du titre Titelverteidiger · basculer kippen, sich wenden · les tribunes Tribünen."),
    ("读第 4 版文章，选出正确答案。",
     "Lesen Sie den Artikel auf Seite 4 und wählen Sie die richtige Antwort."),
    ("大师赛在室内硬地球场举行", "Das Masters findet in der Halle auf Hartplatz statt"),
    ("2025 年卫冕冠军是辛纳", "Titelverteidiger 2025 ist Sinner"),
    ("法甲第十轮大场面：朗斯–马赛", "Topspiel der 10. Ligue-1-Runde: Lens – Marseille"),
    ("周日 8 日还有轮椅单打决赛（中午）", "Sonntag, 8.: auch Rollstuhl-Einzelfinale (mittags)"),
    ("把网球词和释义配对。", "Ordnen Sie die Tenniswörter ihren Bedeutungen zu."),
    ("tournoi=赛事 a", "tournoi=Wettkampf a"),
    ("raquette=球拍 b", "raquette=Schläger b"),
    ("tribunes=看台 c", "tribunes=Tribünen c"),
    ("tenant=卫冕者 d", "tenant=Titelverteidiger d"),
    ("用比较级完成句子（plus / moins）。", "Ergänzen Sie mit dem Komparativ (plus / moins)."),
    ("室内球速更快", "In der Halle ist der Ball schneller"),
    ("大师赛是仅次于大满贯的级别", "Ein Masters 1000 ist die Stufe unter den Grand Slams"),
    ("室内赛季比室外短", "Die Hallensaison ist kürzer als die Sommersaison"),
    ("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。",
     "HINWEIS · un choc Topspiel, Spitzenduell · recevoir empfangen, antreten gegen · familier vertraut."),
    ("« Allez ! » — 加油！ · « Quelle action ! » — 好球！",
     "« Allez ! » — Auf geht's! · « Quelle action ! » — Was für eine Aktion!"),
    ("« Il marque ! » — 他得分了！ · « C'est gagné ! » — 赢了！",
     "« Il marque ! » — Er trifft! · « C'est gagné ! » — Gewonnen!"),
    ("« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！",
     "« Quel point ! » — Was für ein Punkt! (Tennis) · « Balle de match ! » — Matchball!"),
    ("LES MOTS DU TENNIS · 网球词表", "LES MOTS DU TENNIS · WÖRTER"),
    ("le tennis — 网球", "le tennis — Tennis"),
    ("une balle — 球", "une balle — Ball"),
    ("un set — 一盘", "un set — Satz"),
    ("un match — 比赛", "un match — Spiel"),
    ("un point — 一分", "un point — Punkt"),
    ("la finale — 决赛", "la finale — Finale"),
    ("un adversaire — 对手", "un adversaire — Gegner"),
    ("un titre — 冠军头衔", "un titre — Titel"),
    ("À SUIVRE · 拭目以待", "À SUIVRE · FORTSETZUNG"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · ÜBUNGEN"),
    ("用 finale / quarts / demi-finales / tableau / fauteuil / choc 填空。",
     "Ergänzen Sie mit finale / quarts / demi-finales / tableau / fauteuil / choc."),
    ("四分之一决赛在周五", "Viertelfinals am Freitag"),
    ("半决赛在周六", "Halbfinals am Samstag"),
    ("单打决赛在周日", "Einzelfinale am Sonntag"),
    ("正赛签表从周一开始", "Das Hauptfeld beginnt am Montag"),
    ("轮椅赛事周五至周日", "Rollstuhlturnier von Freitag bis Sonntag"),
    ("朗斯–马赛是周末焦点战", "Lens – Marseille ist das Topspiel des Wochenendes"),
    ("事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。",
     "Finalisten vorab unbekannt: spannender oder frustrierender? Schreiben Sie je zwei Sätze dafür und dagegen."),
])

# ---------- content56: P5 + P6 ----------
rep_all("content56.py", [
    ("JEUNESSE & MUSIQUE · 青年", "JEUNESSE & MUSIQUE · JUGEND"),
    ("NIVEAU B1 · Pitchfork Paris · 音乐节", "NIVEAU B1 · Pitchfork Paris · MUSIKFESTIVAL"),
    ("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。",
     "un lieu Ort, Veranstaltungsort · une affiche Plakat · les paroles Liedtexte · donner le ton den Ton angeben · se promener spazieren, sich bewegen · pile genau, exakt."),
    ("À VOUS ! · 即学即练", "À VOUS ! · SIE SIND DRAN"),
    ("读第 5 版文章，选出正确答案。",
     "Lesen Sie den Artikel auf Seite 5 und wählen Sie die richtige Antwort."),
    ("音乐节 11 月 2–8 日，整整一周", "Festival vom 2.–8. November, eine ganze Woche"),
    ("15 届音乐节", "15. Ausgabe des Festivals"),
    ("Avant-Garde 在巴士底各场地，周四至周六", "Avant-Garde in Bastille, Donnerstag bis Samstag"),
    ("俱乐部之夜在周五、周六", "Clubnächte am Freitag und Samstag"),
    ("开幕夜：Headache、Iceage、DIIV", "Eröffnungsabend: Headache, Iceage, DIIV"),
    ("用 lieux / paroles / affiche / ambiance / danse / découvre 填空。",
     "Ergänzen Sie mit lieux / paroles / affiche / ambiance / danse / découvre."),
    ("10 个场地", "Zehn Veranstaltungsorte"),
    ("歌词也是法语学习材料", "Liedtexte helfen beim Französischlernen"),
    ("海报上写着演出信息", "Auf dem Plakat stehen die Gruppennamen"),
    ("每晚气氛各不相同", "Jeden Abend eine andere Stimmung"),
    ("音乐节上人们跳舞", "Auf dem Festival tanzt man"),
    ("发现不认识的乐队", "Unbekannte Gruppen entdecken"),
    ("把音乐词和释义配对。", "Ordnen Sie die Musikwörter ihren Bedeutungen zu."),
    ("concert=音乐会 a", "concert=Konzert a"),
    ("scène=舞台 b", "scène=Bühne b"),
    ("groupe=乐队 c", "groupe=Band c"),
    ("billet=门票 d", "billet=Eintrittskarte d"),
    ("补全对话（音乐节门口）。", "Ergänzen Sie den Dialog (am Festivaleingang)."),
    ("今晚演出的乐队", "Die Gruppe heute Abend"),
    ("买两张票", "Zwei Karten kaufen"),
    ("MOTS DE LA MUSIQUE · 音乐词表", "MOTS DE LA MUSIQUE · WÖRTER"),
    ("un festival — 音乐节", "un festival — Festival"),
    ("un concert — 音乐会", "un concert — Konzert"),
    ("une chanson — 歌曲", "une chanson — Lied"),
    ("un chanteur — 歌手", "un chanteur — Sänger"),
    ("danser — 跳舞", "danser — tanzen"),
    ("écouter — 聆听", "écouter — zuhören"),
    ("une salle — 演出厅", "une salle — Saal"),
    ("le public — 观众", "le public — Publikum"),
    ("PARIS CREATOR WEEK · 创作者周", "PARIS CREATOR WEEK · KREATIVE"),
    ("11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。",
     "4.–5. November in La Villette: Creator Week — Online-Kreative treffen ihr Publikum live."),
    ("LE DÉBAT · 讨论", "LE DÉBAT · DISKUSSION"),
    ("十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？",
     "Ein Festival an zehn Orten: besser als eine einzige große Halle? Welche Musik hören Sie, um Französisch zu lernen?"),
    ("POLITIQUE & CHIFFRES · 时事", "POLITIQUE & CHIFFRES · AKTUELLES"),
    ("NIVEAU B2 · Budget 2027 · 预算周", "NIVEAU B2 · Budget 2027 · HAUSHALTSWOCHE"),
    ("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l'unanimité 一致通过/否决 · un amendement 修正案。",
     "un budget Haushalt · une mission Haushaltsbereich · un député Abgeordneter · rejeter ablehnen · à l'unanimité einstimmig · un amendement Änderungsantrag."),
    ("LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）",
     "LE CALENDRIER PRÉVU · GEPLANT, OHNE ERGEBNISSE"),
    ("本页日程为计划安排，结果尚未产生，下期跟进。",
     "Dieser Plan ist vorläufig; Ergebnisse folgen in der nächsten Ausgabe."),
    ("LIRE LE CALENDRIER · 读日程", "LIRE LE CALENDRIER · LESEN"),
    ("读上图日程，选出正确答案。",
     "Lesen Sie den Kalender oben und wählen Sie die richtige Antwort."),
    ("周二 3 日：文化与媒体", "Dienstag, 3.: Kultur und Medien"),
    ("周三 4 日：农业", "Mittwoch, 4.: Landwirtschaft"),
    ("周四 5 日：国土协调与科研", "Donnerstag, 5.: Kohäsion und Forschung"),
    ("周五 6 日：公共财政与经济", "Freitag, 6.: Öffentliche Finanzen und Wirtschaft"),
    ("10 月 23 日社保预算收入被 115–1 否决",
     "Am 23. Oktober: Einnahmen des Sozialhaushalts mit 115 zu 1 abgelehnt"),
    ("参议院从 11 月 9 日起审议", "Der Senat prüft ab dem 9. November"),
    ("LES MOTS · 词汇", "LES MOTS · WORTSCHATZ"),
    ("député=议员 a", "député=Abgeordneter a"),
    ("rejeter=否决 b", "rejeter=ablehnen b"),
    ("vote=投票 c", "vote=Abstimmung c"),
    ("amendement=修正案 d", "amendement=Änderungsantrag d"),
    ("« Le texte part au Sénat. » — 法案送交参议院。",
     "« Le texte part au Sénat. » — Der Text geht an den Senat."),
    ("« Ce calendrier peut encore bouger. » — 日程仍可能变动。",
     "« Ce calendrier peut encore bouger. » — Der Kalender kann sich noch ändern."),
    ("« Les résultats ne sont pas connus. » — 结果尚未揭晓。",
     "« Les résultats ne sont pas connus. » — Die Ergebnisse sind noch nicht bekannt."),
    ("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。",
     "HINWEIS · prévu vorgesehen, geplant · réaliser verwirklichen, umsetzen · distinguer unterscheiden."),
    ("用比较级完成句子。", "Ergänzen Sie mit dem Komparativ."),
    ("预算辩论比一场音乐会长", "Eine Haushaltsdebatte ist länger als ein Konzert"),
    ("预算比时间表复杂", "Der Haushalt ist komplexer als ein Kalender"),
    ("文化预算与农业预算同样重要", "Kultur- und Agrarhaushalt sind gleich wichtig"),
    ("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · ÜBUNGEN"),
    ("用 examine / ont rejeté / part / peut / connus 填空。",
     "Ergänzen Sie mit examine / ont rejeté / part / peut / connus."),
    ("国民议会审议预算", "Die Nationalversammlung prüft den Haushalt"),
    ("议员们否决收入部分", "Die Abgeordneten lehnten die Einnahmen ab"),
    ("法案送交参议院", "Der Text geht an den Senat"),
    ("日程仍可能变动", "Der Kalender kann sich noch ändern"),
    ("结果尚未揭晓", "Die Ergebnisse sind noch nicht bekannt"),
    ("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。",
     "Diskussion: Soll man einen Plan ankündigen, bevor Ergebnisse vorliegen? Unterscheiden Sie prévu (geplant) und décidé (beschlossen)."),
])

# ---------- content7: P7 ----------
rep_all("content7.py", [
    ("LANGUE EN MAIN · 精讲", "LANGUE EN MAIN · SPRACHE"),
    ("A2 → B2 · Les phrases de la semaine · 本周金句",
     "A2 → B2 · Les phrases de la semaine · SÄTZE DER WOCHE"),
    ("NIVEAU A2 · 基础", "NIVEAU A2 · GRUNDLAGEN"),
    ("NIVEAU B1 · 进阶", "NIVEAU B1 · AUFBAU"),
    ("NIVEAU B2 · 挑战", "NIVEAU B2 · VERTIEFUNG"),
    ("BOÎTE À OUTILS · 工具箱", "BOÎTE À OUTILS · WERKZEUG"),
    ("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。",
     "Werkzeugkasten: Drei Sätze zum Mitnehmen, einer pro Niveau; alle Sätze stammen aus den Artikeln dieser Ausgabe — im Original nachlesen, dann bleiben sie hängen."),
    ("LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）",
     "LES PHRASES DE LA SEMAINE · SÄTZE DER WOCHE"),
    ("每句一个语法点 + 一道小题 · 答案见第 8 版",
     "Pro Satz ein Punkt + eine Aufgabe · Antworten Seite 8"),
    ("语法点｜reprendre：复课、重新开始（pause 后）。",
     "Grammatik: reprendre — nach einer Pause wieder beginnen."),
    ("语法点｜ne...pas encore：尚未、还不。", "Grammatik: ne...pas encore — noch nicht."),
    ("pas encore 尚未", "pas encore = noch nicht"),
    ("语法点｜passé composé 代动词：se + être + 过去分词。",
     "Grammatik: passé composé reflexiv — se + être + Partizip."),
    ("语法点｜comparatif：plus + 形容词，ou 对举。",
     "Grammatik: comparatif — plus + Adjektiv, ou stellt gegenüber."),
    ("plus + 形容词", "plus + Adjektiv"),
    ("语法点｜se promener：代动词，漫步、穿梭。",
     "Grammatik: se promener — reflexiv, spazieren, sich bewegen."),
    ("语法点｜pouvoir + 动词原形：可能、可以。",
     "Grammatik: pouvoir + Infinitiv — können, möglich sein."),
    ("语法点｜se jouer：决出胜负、上演（代动词）。",
     "Grammatik: se jouer — sich entscheiden, sich abspielen (reflexiv)."),
    ("语法点｜rencontrer：与观众见面；y 代指地点。",
     "Grammatik: rencontrer — das Publikum treffen; y steht für den Ort."),
    ("CLINIQUE DES ERREURS · 易错诊所", "CLINIQUE DES ERREURS · KLINIK"),
    ("每句有一处错误：找出来并改正。",
     "Jeder Satz enthält einen Fehler: Finden und korrigieren Sie ihn."),
    ("jamais + de：否定句中 des 变 de", "jamais + de: In der Verneinung wird des zu de"),
    ("主谓一致：créateurs 复数 → rencontrent，不是 rencontre",
     "Subjekt-Verb-Kongruenz: créateurs (Plural) → rencontrent, nicht rencontre"),
    ("虚拟式：il examine，不加 s", "Subjonctif: il examine, ohne s"),
    ("事实：决赛在 8 日，不是 7 日", "Fakt: Das Finale ist am 8., nicht am 7. November"),
    ("LE COURRIER DES LECTEURS · 读者园地", "LE COURRIER DES LECTEURS · LESERECKE"),
    ("小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。",
     "Xiao Mo kommentiert (Beispieltext): Das passé composé ist sicher; das Semikolon verbindet beide Tage."),
    ("编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。",
     "Anmerkung der Redaktion: Kein VOL.2-Text lag vor (W44 erschien nicht); hier ein Beispiel der Redaktion. VOL.4 bespricht echte Texte. Schicken Sie uns Ihren Text!"),
    ("LA SEMAINE PROCHAINE · VOL.4 下周预告", "LA SEMAINE PROCHAINE · NÄCHSTE WOCHE · VOL.4"),
    ("下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！",
     "Nächste Woche: Senat zum Sozialhaushalt, 11. November Waffenstillstandstag, 14.–15. November Muschelmarkt in Dieppe — und Ihre Briefe!"),
])

# ---------- content8: P8 ----------
# Printed-note set measured from the core P8 (tools/p8.py extract --json):
# 97 numbers; the other 53 are bare keys and stay bare.
PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
rep("content8.py",
    'for pg, grp in groupby(REG, key=lambda e: e["page"]):',
    'PRINT_NOTES = ' + repr(PRINT_NOTES) + '\nfor pg, grp in groupby(REG, key=lambda e: e["page"]):', 1)
rep("content8.py",
    'if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):',
    'if e["note"] and e["n"] in PRINT_NOTES:', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— SEITE {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep_all("content8.py", [
    ("EXERCICES & RÉPONSES · 练习与答案", "EXERCICES & RÉPONSES · ÜBUNGEN & ANTWORTEN"),
    ("综合评估 ÉVALUATION · 答案在本版下方",
     "GESAMTBEWERTUNG · ÉVALUATION · ANTWORTEN UNTEN AUF DIESER SEITE"),
    ("11 月 8 日 2026 是星期日", "8. November 2026 ist ein Sonntag"),
    ("去南泰尔看决赛", "Nach Nanterre zum Finale"),
    ("决赛选手周六晚才揭晓", "Finalisten erst Samstagabend bekannt"),
    ("品尝语境（un régal）→ goûté", "Verkostungskontext (un régal) → goûté"),
    ("se promener 漫步", "se promener = spazieren"),
    ("avoir + 过去分词 goûté（不配合）", "avoir + Partizip goûté (ohne Angleichung)"),
    ("les finales 主语复数 → ont lieu", "les finales (Plural) → ont lieu"),
    ("elle écrit 她写", "elle écrit = sie schreibt"),
    ("A · TEXTE À TROUS · 完形填空", "A · TEXTE À TROUS · LÜCKEN"),
    ("选项：", "Optionen:"),
    ("B · CHOIX MULTIPLE · 单选", "B · CHOIX MULTIPLE · AUSWAHL"),
    ("7 nov. = samedi（最后夜场）", "7. Nov. = Samstag (letzte Nachtveranstaltung)"),
    ("s'intéresser aux（à+les）", "s'intéresser aux (à + les)"),
    ("si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音",
     "si + imparfait → conditionnel présent; j' ist je vor Vokal (Elision)"),
    ("主语 ce programme 三单 → semble", "Subjekt ce programme (3. Person Singular) → semble"),
    ("将来时 aura lieu（决赛在周日）", "Futur aura lieu (Finale am Sonntag)"),
    ("三区同日复课", "Alle drei Zonen beginnen am selben Tag"),
    ("扇贝节在 11 月 7–8 日", "Muschelfest am 7.–8. November"),
    ("C · LECTURE · 阅读理解", "C · LECTURE · LESEN"),
    ("夜场 19 点至凌晨 1 点", "Nachtveranstaltung 19 bis 1 Uhr"),
    ("小徽章给小 Léo 驱怪", "Das Abzeichen ist für den kleinen Léo, gegen Monster"),
    ("周日先看决赛再吃扇贝", "Sonntag: erst Finale ansehen, dann Muscheln essen"),
    ("周日晚上早睡因为周一上学", "Sonntagabend früh ins Bett, weil Montag Schule ist"),
    ("周一是上学日（复课后正常周一）", "Montag ist ein Schultag (nach den Ferien normal)"),
    ("D · PHRASES · 完成句子与转换", "D · PHRASES · SÄTZE"),
    ("aller + 原形（futur proche）", "aller + Infinitiv (futur proche)"),
    ("si + 半过去时 venais", "si + imparfait (venais)"),
    ("passé composé : a + 过去分词", "passé composé: a + Partizip"),
    ("selon moi = 在我看来", "selon moi = meiner Meinung nach"),
    ("il est prévu que + 虚拟式", "il est prévu que + Subjonctif"),
    ("E · TRADUCTION · 翻译", "E · TRADUCTION · ÜBERSETZEN"),
    # Re-aimed translation items (W43 precedent): E1 flips to FR->DE;
    # E2-E5 stems become German, French keys unchanged.
    ("读一份日程，本身就是在了解法国。", "Ein Programm zu lesen heißt schon, Frankreich zu verstehen."),
    ("lire un programme = 读日程", "lire un programme = ein Programm lesen"),
    ("Traduisez : « Lire un programme, c'est déjà comprendre la France. »",
     "Übersetzen Sie ins Deutsche: « Lire un programme, c'est déjà comprendre la France. »"),
    ("比较级 plus vite + court", "Komparativ: plus vite + court"),
    ("Traduisez : 他跑得比他哥哥更快。",
     "Übersetzen Sie ins Französische: Er läuft schneller als sein Bruder."),
    ("Traduisez : 学生们自 10 月 17 日起就在放假。",
     "Übersetzen Sie ins Französische: Die Schüler haben seit dem 17. Oktober Ferien."),
    ("Traduisez : 今晚，我们要准备书包。",
     "Übersetzen Sie ins Französische: Heute Abend bereiten wir unsere Schultaschen vor."),
    ("ne...pas encore = 尚未", "ne...pas encore = noch nicht"),
    ("Traduisez : 人们尚不知道决赛选手是谁。",
     "Übersetzen Sie ins Französische: Man kennt die Finalisten noch nicht."),
    ("F · LES MOTS · 词汇配对", "F · LES MOTS · ZUORDNUNG"),
    ("tournoi=赛事 a", "tournoi=Wettkampf a"),
    ("nocturne=夜场 b", "nocturne=Nachtveranstaltung b"),
    ("budget=预算 c", "budget=Haushalt c"),
    ("coquille=扇贝 d", "coquille=Jakobsmuschel d"),
    ("festival=音乐节 e", "festival=Festival e"),
    ("G · DIALOGUE · 对话补全", "G · DIALOGUE · DIALOG"),
    ("11 月 7 日是星期六", "7. November ist ein Samstag"),
    ("在市场买扇贝", "Auf dem Markt Muscheln kaufen"),
    ("goûter 品尝（原形）", "goûter = kosten (Infinitiv)"),
    ("à la portaise 是一种做法", "à la portaise ist eine Zubereitungsart"),
    ("Bon week-end ! 周末愉快", "Bon week-end ! = Schönes Wochenende!"),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "写作", "Offene Aufgabe — Stichpunkte im Schreibrahmen; Mustertext im MODÈLE-Kasten auf dieser Seite", "Bewertung nach Stichpunkten")'),
    ("H · ÉCRITURE · 写作", "H · ÉCRITURE · SCHREIBEN"),
    ("用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。",
     "Schreiben Sie 80–100 Wörter auf Französisch: Mein Wochenende am 7.–8. November. Beschreiben Sie ein Spiel, ein Fest, ein Gericht. Die besten Texte erscheinen im VOL.4 (Seite 7, « Le courrier des lecteurs »)."),
    ("MODÈLE · 范文", "MODÈLE · MUSTERTEXT"),
    ("RÉPONSES · 全部答案与简析（第 1–8 版）",
     "RÉPONSES · ALLE ANTWORTEN MIT ANMERKUNGEN (SEITEN 1–8)"),
])

# ---------- shared type/instr tokens LAST (registry only, except instr) ----------
TYPE_MAP = [
    ("完成句子", "Satzergänzung"),
    ("单选", "Multiple Choice"),
    ("句型转换", "Umformung"),
    ("词汇配对", "Zuordnung"),
    ("跟练", "Anwendungsübung"),
    ("改错", "Fehlerkorrektur"),
    ("完形填空", "Lückentext"),
    ("阅读判断", "Richtig/Falsch"),
    ("阅读理解", "Leseverstehen"),
    ("对话补全", "Dialogergänzung"),
    ("翻译", "Übersetzung"),
    ("写作", "Schreiben"),
    ("图表读数", "Diagrammlesen"),
]
INSTR_MAP = [
    ('instr="把词和释义配对"', 'instr="Zuordnen"'),
    ('instr="填空"', 'instr="Ausfüllen"'),
    ('instr="改写"', 'instr="Umformen"'),
    ('instr="配对"', 'instr="Zuordnen"'),
    ('instr="改错"', 'instr="Korrigieren"'),
]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in TYPE_MAP:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)
    for old, new in INSTR_MAP:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done, replacements: {len(LOG)}")

# ---------- FIX ROUND 1 (2026-10-28, after round-1 render + gates) ----------
# R1 defects (all layout, no content change):
#  (a) P1 headline flow overflowed 127px into row B: the German P1 gloss
#      wrapped to 8 lines (core: 5). Shortened to single-word glosses
#      (6 lines, "Nachtevent" for une nocturne) and set the 5 frozen
#      French headline paras to 24pt / lh 1.45 (text byte-identical,
#      only presentation size/leading changes).
#  (b) P2 ET VOUS box bottom 1625.6 (core: 1538.6) collided with the
#      date-section rule at 1557: the German ET VOUS para wrapped to
#      6 lines (core Chinese: 2). Shortened to a 3-line German para;
#      box bottom returns to the core value.
#  (c) P8 battery overflowed 91px into the writing strip and the keys
#      flow crossed the footer rule (end 2666): the 3 long battery
#      paras (cloze / reading / dialogue) go 21pt -> 20pt, and the
#      keys area goes 15.5pt -> 14.5pt (EN x DE shipped 13.5pt for
#      all-notes printing, so 14.5pt for 97 notes stays readable).
rep("content12.py",
    "se jouer den Ausgang entscheiden, sich abspielen · une finale Endspiel, Finale · une demi-finale Halbfinale · un quart de finale Viertelfinale · une nocturne Nachtveranstaltung · un frisson Schauer, Nervenkitzel · la coquille Saint-Jacques Jakobsmuschel.",
    "se jouer entscheiden · une finale Finale · une demi-finale Halbfinale · un quart de finale Viertelfinale · une nocturne Nachtevent · un frisson Nervenkitzel · la coquille Saint-Jacques Jakobsmuschel.", 1)
for tail in [
    "avec trois finales en même temps.",
    "ils seront connus samedi soir, après les demi-finales.",
    "un badge gratuit contre les monstres.",
    "on goûte des recettes au bord de la mer.",
    "Suite en pages 3 et 4.",
]:
    rep("content12.py", tail + '")', tail + '", 24, "serif", False, INK, 1.45)', 1)
rep("content12.py",
    "Erzählen Sie von Ihrem Schulbeginn: Wo waren Sie am Montagmorgen? Welches Buch haben Sie in den Ferien gelesen? Schreiben Sie zwei Sätze auf Französisch an die Redaktion.",
    "Ihr Schulbeginn: Wo waren Sie am Montagmorgen? Welches Buch lasen Sie? Zwei Sätze an die Redaktion.", 2)
rep("content8.py", 'dans son cahier.", 21)', 'dans son cahier.", 20)', 1)
rep("content8.py", "c'est l'école.\", 21)", "c'est l'école.\", 20)", 1)
rep("content8.py", "— Merci !\", 21)", "— Merci !\", 20)", 1)
rep("content8.py",
    'kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)', 1)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix round 1), replacements: {len(LOG)}")

# ---------- FIX ROUND 2 (2026-10-28, after round-2 render) ----------
# Round-2 remaining defect: P8 battery still ends at y=1564 (limit 1485),
# so the dialogue tail ("Merci !" at y=1523, col 3) sits inside the
# MODÈLE box (top 1500) and crosses the writing-strip rule. The 21->20pt
# para change saved only 12px because column breaks absorbed the rest.
# Fix: tighten battery exercise spacing only (content8 call sites):
# ex gap 11 -> 6 (23 exercises x 5px = 115px) and the F match_set gap
# 14 -> 6 (8px). Battery target end <= 1485 with margin; keys flow is
# unaffected (it uses kf.para, not ex).
rep("content8.py", ", size=20)", ", size=20, gap=6)", 4)
rep("content8.py", 'instr="Zuordnen")', 'instr="Zuordnen", gap=6)', 1)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix rounds 1-2), replacements: {len(LOG)}")

# ---------- FIX ROUND 3 (2026-10-28, after round-3 render) ----------
# Round-3 remaining defect: P8 battery still ends at y=1516 (its own
# 1485 limit), because gap savings were absorbed by column breaks; the
# dialogue tail would sit 16px below the writing-strip rule (1486) and
# inside the MODÈLE box (top 1500). Fix: move the whole writing strip
# down 40px (wy 1500 -> 1540, one variable line; all strip positions
# derive from wy). New clearances: strip rule at 1526 (battery tail
# ink ~1500, gap ~26px), MODÈLE top at 1540; keys flow top moves to
# 1900, predicted keys end ~2420 < 2545 (round-3 keys content total
# 2455px over 4 columns of 645px capacity = ends 2420). Verified by
# re-render + occlusion audit, not by this arithmetic alone.
rep("content8.py", "wy = 1500", "wy = 1540", 1)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix rounds 1-3), replacements: {len(LOG)}")

# ---------- FIX ROUND 4 (2026-10-28, after round-4 render + audit) ----------
# Round-4 remaining defect (canonical audit: 1 NEW flag): the P2 ET VOUS
# box bottom is 1567.6, 10px past the date-section rule at 1557-1559,
# and its last German line sits below the rule. The German para wrapped
# to 3 lines (core Chinese: 2 lines, box bottom 1538.6). Shorten it to
# a 2-line German para; box bottom returns to 1538.6 (18px clear).
rep("content12.py",
    "Ihr Schulbeginn: Wo waren Sie am Montagmorgen? Welches Buch lasen Sie? Zwei Sätze an die Redaktion.",
    "Montagmorgen: Wo waren Sie, welches Buch? Zwei Sätze an die Redaktion!", 2)

with open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(LOG) + "\n")
print(f"transform done (with fix rounds 1-4), replacements: {len(LOG)}")
