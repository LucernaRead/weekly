# -*- coding: utf-8 -*-
"""One-off fan-out transform: W45 NL core (Chinese explanations) -> NL x IT.
Line-literal replacements only, each counted. Dutch target text, keys
(except re-aimed E137/E138), facts, images: untouched.
Paths were repointed before this transform (sed core->nl-it on OUT/BASE,
grep-verified: zero core-dir references left in *.py).
Furniture follows the SHIPPED W43 NL x IT SVGs (measured, not README #20):
badge inserted at y=568, 20pt bold BRICK; footer SETTIMANALE OLANDESE VOL.2;
gloss prefix 'Nota — '; subtitle 36pt; top-strip centre OGNI SETTIMANA.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
R = []

def rep(f, old, new):
    R.append((f, old, new))

# ---------- bslib4: footer + page line + gloss prefix (W43 NL x IT measured) ----------
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.2 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · SETTIMANALE OLANDESE VOL.2 · TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"')
rep("bslib4.py", "译注｜", "Nota — ")

# ---------- render.py: PDF names ----------
rep("render.py", "De-Lucerna-VOL2.pdf", "De-Lucerna-VOL2-IT.pdf")
rep("render.py", "De-Lucerna-VOL2-web.pdf", "De-Lucerna-VOL2-IT-web.pdf")

# ---------- types + instr (global; E-item instrs handled per-line below) ----------
# order: instrs FIRST (else the bare type replacement would eat instr values),
# and cloze before plain choice.
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, 'instr="填空"', 'instr="Completa"')
    rep(f, 'instr="判断"', 'instr="Vero o falso?"')
    rep(f, 'instr="造句"', 'instr="Forma la frase"')
    rep(f, 'instr="写作"', 'instr="Scrivi"')
    rep(f, "完形单选", "Cloze")
    rep(f, "完成句子", "Completa la frase")
    rep(f, "词汇配对", "Abbinamento")
    rep(f, "判断对错", "Vero o falso")
    rep(f, "单选", "Scelta multipla")
    rep(f, "造句", "Forma la frase")
    rep(f, "翻译", "Traduzione")
    rep(f, "写作", "Scrittura")
# E-item directions (per body line, after the global type pass left instr="Traduzione")
rep("content8.py", '"De Klimaatweek duurt zeven dagen. → ___", instr="Traduzione"',
     '"De Klimaatweek duurt zeven dagen. → ___", instr="Traduci in italiano"')
rep("content8.py", '"Code oranje betekent: bereid je voor. → ___", instr="Traduzione"',
     '"Code oranje betekent: bereid je voor. → ___", instr="Traduci in italiano"')
rep("content8.py", '"博物馆之夜从晚上 19 点到凌晨 2 点。→ ___", instr="Traduzione"',
     '"La Notte dei musei dura dalle 19:00 alle 02:00. → ___", instr="Traduci in olandese"')
rep("content8.py", '"我参加气候周。→ ___", instr="Traduzione"',
     '"Io partecipo alla Settimana del clima. → ___", instr="Traduci in olandese"')

# ---------- content12: P1 ----------
rep("content12.py", "ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语",
     "ELKE WEEK IN HET NEDERLANDS · OGNI SETTIMANA IN OLANDESE")
rep("content12.py", 'p.text(975, 330, "荷 兰 语 周 报 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12", 40, "serif", True, INK, anchor="middle")',
     'p.text(975, 330, "SETTIMANALE OLANDESE · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12", 36, "serif", True, INK, anchor="middle")')
rep("content12.py", '"气候周"', '"SETTIMANA DEL CLIMA"')
rep("content12.py", '"本周全国气候周 · 详见第 2 版"', '"Tutta la nazione partecipa · vedi pagina 2"')
# pairing badge, W43 NL x IT slot: inserted at y=568, 20pt bold BRICK, centred.
rep("content12.py", "hy = 580",
     'p.text(975, 568, "TESTI IN OLANDESE · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 20, "sans", True, BRICK, anchor="middle")\nhy = 580')
rep("content12.py", '"HET NIEUWS · 头条"', '"HET NIEUWS · IN PRIMO PIANO"')
rep("content12.py", 'f.bridge("讲解｜de Klimaatweek 气候周 · de boom planten 种树 · besparen 节约 · de waarschuwing 警告、预警。")',
     'f.bridge("Nota — de Klimaatweek = Settimana del clima · de boom planten = piantare un albero · besparen = risparmiare · de waarschuwing = avviso, allarme.")')
rep("content12.py", '"DE WEEK IN CIJFERS · 数字看本周"', '"DE WEEK IN CIJFERS · IN CIFRE"')
rep("content12.py", "（气候周的天数）", "(i giorni della Settimana del clima)")
rep("content12.py", "（周六科弗登发放的树木和灌木）", "(gli alberi e gli arbusti che Coevorden regala sabato)")
rep("content12.py", "（博物馆之夜开放的博物馆，70 多家）", "(i musei aperti per la Notte dei musei, oltre 70)")
rep("content12.py", "（荷甲第 12 轮的比赛场数）", "(le partite della 12ª giornata di Eredivisie)")
rep("content12.py", '"NU JIJ · 即学即练"', '"NU JIJ · TOCCA A TE"')
rep("content12.py", '"气候周 11 月 2–8 日"', '"La Settimana del clima va dal 2 all\'8 novembre"')
rep("content12.py", '"科弗登发放 200 棵树木灌木"', '"Coevorden regala 200 alberi e arbusti"')
rep("content12.py", '"博物馆之夜在 11 月 7 日周六"', '"La Notte dei musei è sabato 7 novembre"')
rep("content12.py", '"海伦芬–费耶诺德 11:15 开球"', '"Heerenveen–Feyenoord inizia alle 11:15"')
rep("content12.py", '"特温特–阿贾克斯 13:30 开球"', '"Twente–Ajax inizia alle 13:30"')
rep("content12.py", '"veel mensen → planten"', '"Soggetto plurale, quindi planten"')
rep("content12.py", '"· 本周日程"', '"· QUESTA SETTIMANA"')
rep("content12.py", '"Agenda van de week · 本周大事"', '"Agenda van de week · GLI EVENTI DELLA SETTIMANA"')
rep("content12.py", '"本周日程见第 2–4 版文章"', '"Tutte le date e gli orari sono negli articoli alle pagine 2–4."')
rep("content12.py", '"IN DEZE EDITIE · 本期目录"', '"IN DEZE EDITIE · SOMMARIO"')
rep("content12.py", '"“气候”：我们周围长期的天气与自然。气候周讲的就是我们的气候。"',
     '"«Clima»: il tempo e la natura intorno a noi, per un lungo periodo. La Settimana del clima parla del nostro clima."')
rep("content12.py", '"IN HET KORT · 快讯"', '"IN HET KORT · IN BREVE"')
rep("content12.py", '"BLIKSEMQUIZ · 闪电问答"', '"BLIKSEMQUIZ · QUIZ LAMPO"')
rep("content12.py", '"读头版，选出正确答案 · 答案见第 8 版"', '"Leggi la prima pagina, scegli la risposta giusta · risposte a pagina 8"')
rep("content12.py", '"气候周共 7 天（11 月 2–8 日）"', '"La Settimana del clima dura 7 giorni (2–8 novembre)"')
rep("content12.py", '"博物馆之夜在阿姆斯特丹"', '"La Notte dei musei è ad Amsterdam"')

# ---------- content12: P2 ----------
rep("content12.py", 'p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · 一步一步讲气候周")',
     'p.band("LEVEN · VITA", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · La Settimana del clima, passo dopo passo")')
rep("content12.py", '"ZO ONTHOUD JE HET · 口诀"', '"ZO ONTHOUD JE HET · RICORDA"')
rep("content12.py", 'f.gloss("het klimaat 气候 · wortelen 生根 · besparen 节约 · de verwarming 暖气 · de waarschuwing 预警 · lokaal 当地的、本地的。")',
     'f.gloss("het klimaat = clima · wortelen = mettere radici · besparen = risparmiare · de verwarming = riscaldamento · de waarschuwing = avviso, allarme · lokaal = locale.")')
rep("content12.py", '"气候周你做什么？种树、节约能源还是骑车。写两句荷兰语寄给编辑部。"',
     '"Tu cosa fai nella Settimana del clima: pianti un albero, risparmi energia o vai in bici? Scrivi due frasi in olandese e mandale alla redazione."')
rep("content12.py", '"EN JIJ? · 说说你自己"', '"EN JIJ? · E TU?"')
rep("content12.py", '"DE CODES VAN HET KNMI · 气象预警颜色"', '"DE CODES VAN HET KNMI · I CODICI DEL KNMI"')
rep("content12.py", '"Wat betekent elke kleur? · 每种颜色是什么意思"', '"Che cosa significa ogni colore?"')
rep("content12.py", '"天气可能危险，要当心"', '"Il tempo potrebbe essere pericoloso: fai attenzione"')
rep("content12.py", '"危险，做好准备"', '"Pericoloso: preparati"')
rep("content12.py", '"非常危险，尽量待在室内"', '"Molto pericoloso: resta in casa se puoi"')
rep("content12.py", '"预警针对你所在的地区"', '"L\'avviso riguarda la tua zona"')
rep("content12.py", '"OEFENINGEN · 第 2 版练习"', '"OEFENINGEN · ESERCIZI A PAGINA 2"')
rep("content12.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Risposte a pagina 8 · i livelli sono misti; cerca il tuo numero"')
rep("content12.py", 'e.bridge("读第 2 版文章，选出正确答案。")', 'e.bridge("Leggi l\'articolo a pagina 2 e scegli la risposta giusta.")')
rep("content12.py", '"气候周不做：更多开车"', '"Non è un\'azione per la Settimana del clima: guidare di più"')
rep("content12.py", '"红色预警：非常危险，待在室内"', '"Codice rosso: molto pericoloso, resta in casa"')
rep("content12.py", '"预警针对本地，不针对整个省"', '"Gli avvisi sono locali, non per un\'intera provincia"')
rep("content12.py", '"节约能源：暖气调低一度"', '"Risparmiare energia: abbassare il riscaldamento di un grado"')
rep("content12.py", 'e.bridge("用第 2 版的词填空。")', 'e.bridge("Completa con le parole di pagina 2.")')
rep("content12.py", '"气候周 11 月 2–8 日共 7 天"', '"La Settimana del clima, 2–8 novembre, dura 7 giorni"')
rep("content12.py", '"wortelen = 生根（复数主语）"', '"wortelen = mettere radici (soggetto plurale)"')
rep("content12.py", '"besparen = 节约"', '"besparen = risparmiare"')
rep("content12.py", '"fiets = 自行车"', '"fiets = bicicletta"')
rep("content12.py", '"发放地点在兹韦洛"', '"Il luogo della distribuzione è Zweeloo"')
rep("content12.py", 'e.bridge("用颜色代码和日期填空。")', 'e.bridge("Completa con i codici colore e le date.")')
rep("content12.py", '"黄色代码：当心"', '"Codice giallo: attenzione"')
rep("content12.py", '"橙色代码：危险"', '"Codice arancione: pericolo"')
rep("content12.py", '"发放从 13:00 开始"', '"La distribuzione inizia alle 13:00"')
rep("content12.py", '"气候周 11 月 8 日周日结束"', '"La Settimana del clima finisce domenica 8 novembre"')
rep("content12.py", '["Klimaatweek=气候周 b", "besparen=节约 d", "waarschuwing=预警 a", "lokaal=本地的 c"]',
     '["Klimaatweek = Settimana del clima b", "besparen = risparmiare d", "waarschuwing = avviso a", "lokaal = locale c"]')
rep("content12.py", 'instr="把词和释义配对"', 'instr="Abbina la parola al significato"')

# ---------- content34: P3 ----------
rep("content34.py", 'p.band("CULTUUR · 文化", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · 博物馆之夜、书籍与艺术")',
     'p.band("CULTUUR · CULTURA", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · Notte dei musei, libri e arte")')
rep("content34.py", 'f.gloss("het museum 博物馆 · de rondleiding 导览 · het tijdslot 时间段 · tweedehands 二手的 · de beurs 展会、集市。")',
     'f.gloss("het museum = museo · de rondleiding = visita guidata · het tijdslot = fascia oraria · tweedehands = di seconda mano · de beurs = fiera, mercato.")')
rep("content34.py", '"OEFENINGEN · 第 3 版练习"', '"OEFENINGEN · ESERCIZI A PAGINA 3"')
rep("content34.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Risposte a pagina 8 · i livelli sono misti; cerca il tuo numero"')
rep("content34.py", 'e.bridge("读第 3 版文章，选出正确答案。")', 'e.bridge("Leggi l\'articolo a pagina 3 e scegli la risposta giusta.")')
rep("content34.py", '"博物馆之夜在 11 月 7 日周六"', '"La Notte dei musei è sabato 7 novembre"')
rep("content34.py", '"博物馆开放到凌晨 2 点"', '"I musei sono aperti fino alle 02:00"')
rep("content34.py", '"Crossing Border 在海牙"', '"Crossing Border è all\'Aia"')
rep("content34.py", '"Crossing Border 结合书籍与音乐"', '"Crossing Border unisce libri e musica"')
rep("content34.py", '"PAN 艺术博览会到 11 月 8 日"', '"La fiera d\'arte PAN dura fino all\'8 novembre"')
rep("content34.py", 'e.bridge("用方框里的词填空。注意：有的词要变成复数。")',
     'e.bridge("Completa con le parole nel riquadro. Attenzione: alcune parole devono diventare plurali.")')
rep("content34.py", '"museum 复数：musea"', '"Plurale di museum: musea"')
rep("content34.py", '"rondleiding = 导览"', '"rondleiding = visita guidata"')
rep("content34.py", '"tijdslot = 时间段"', '"tijdslot = fascia oraria"')
rep("content34.py", '"tweedehands = 二手的"', '"tweedehands = di seconda mano"')
rep("content34.py", '"beurs = 展会、集市"', '"beurs = fiera, mercato"')
rep("content34.py", 'e.bridge("用现在完成时补全，注意助动词 hebben/zijn。")',
     'e.bridge("Completa con il passato prossimo. Attenzione agli ausiliari hebben/zijn.")')
rep("content34.py", '"zijn 的 perfectum：zijn geweest"', '"Perfectum di zijn: zijn geweest"')
rep("content34.py", '"kopen 的 perfectum：hebben gekocht"', '"Perfectum di kopen: hebben gekocht"')
rep("content34.py", '"voorlezen 的 perfectum：hebben voorgelezen"', '"Perfectum di voorlezen: hebben voorgelezen"')
rep("content34.py", '"komen 用 zijn：zijn gekomen"', '"komen vuole zijn: zijn gekomen"')
rep("content34.py", 'e.bridge("算一算：用第 3 版的数字回答。")', 'e.bridge("Calcola: rispondi con i numeri di pagina 3.")')
rep("content34.py", '"19:00 到 02:00 共 7 小时"', '"Dalle 19:00 alle 02:00 sono 7 ore"')
rep("content34.py", '"11 月 1–8 日共 8 天"', '"Dall\'1 all\'8 novembre sono 8 giorni"')
rep("content34.py", '"11 月 3–8 日共 6 天"', '"Dal 3 all\'8 novembre sono 6 giorni"')
rep("content34.py", '"250 的一半是 125"', '"La metà di 250 è 125"')
# ---------- content34: P4 ----------
rep("content34.py", 'p.band("SPORT · 体育", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · 欧战周与第 12 轮")',
     'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · Settimana europea e 12ª giornata")')
rep("content34.py", 'f.gloss("de balans 成绩单、总结 · gelijkspelen 打平 · de speelronde 轮次 · de topper 焦点战 · de stand 积分榜。")',
     'f.gloss("de balans = il bilancio finale · gelijkspelen = pareggiare · de speelronde = giornata · de topper = il big match · de stand = la classifica.")')
rep("content34.py", '"OEFENINGEN · 第 4 版练习"', '"OEFENINGEN · ESERCIZI A PAGINA 4"')
rep("content34.py", 'e.bridge("读第 4 版文章，选出正确答案。")', 'e.bridge("Leggi l\'articolo a pagina 4 e scegli la risposta giusta.")')
rep("content34.py", '"阿贾克斯 2–0 赢亚特兰大"', '"L\'Ajax ha battuto l\'Atalanta 2–0"')
rep("content34.py", '"特温特 4–1 赢林肯红魔"', '"Il Twente ha battuto il Lincoln 4–1"')
rep("content34.py", '"NEC 2–4 输给萨格勒布迪纳摩"', '"Il NEC ha perso 2–4 contro la Dinamo Zagabria"')
rep("content34.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"Il Real Betis ha battuto il Feyenoord 1–0"')
rep("content34.py", '"10 轮后费耶诺德 24 分领跑"', '"Dopo 10 giornate il Feyenoord è primo con 24 punti"')
rep("content34.py", 'e.bridge("用方框里的词填空。注意动词形式。")',
     'e.bridge("Completa con le parole nel riquadro. Attenzione alle forme verbali.")')
rep("content34.py", '"balans = 成绩单、总结"', '"balans = il bilancio finale"')
rep("content34.py", '"gelijkspelen 过去时复数：speelden gelijk"', '"Passato plurale di gelijkspelen: speelden gelijk"')
rep("content34.py", '"topper = 焦点战"', '"topper = il big match"')
rep("content34.py", '"stand = 积分榜"', '"stand = la classifica"')
rep("content34.py", '"doelpunt = 进球"', '"doelpunt = gol"')
rep("content34.py", 'e.bridge("用过去时或完成时补全。")', 'e.bridge("Completa con il passato o con il passato prossimo.")')
rep("content34.py", '"winnen 过去时：won"', '"Passato di winnen: won"')
rep("content34.py", '"gaan 过去时：ging"', '"Passato di gaan: ging"')
rep("content34.py", '"verliezen 过去时：verloor"', '"Passato di verliezen: verloor"')
rep("content34.py", '"komen 的 perfectum 用 zijn"', '"Il perfectum di komen vuole zijn"')
rep("content34.py", '"对：阿贾克斯 2–0 获胜"', '"Vero: l\'Ajax ha vinto 2–0"')
rep("content34.py", '"错：NEC 2–4 输了"', '"Falso: il NEC ha perso 2–4"')
rep("content34.py", '"错：特温特–阿贾克斯 13:30；11:15 是海伦芬–费耶诺德"', '"Falso: Twente–Ajax è alle 13:30; alle 11:15 c\'è Heerenveen–Feyenoord"')
rep("content34.py", '"对：10 轮后费耶诺德 24 分第一"', '"Vero: dopo 10 giornate il Feyenoord è primo con 24 punti"')

# ---------- content56: P5 ----------
rep("content56.py", 'p.band("JONGEREN · 青年", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 荒岛节目开播、音乐节与设计周落幕")',
     'p.band("JONGEREN · GIOVANI", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · Robinson è iniziato, ADE e DDW sono finiti")')
rep("content56.py", "（周日晚 20:00 在 RTL 4 收看）", "(da vedere su RTL 4 domenica alle 20:00)")
rep("content56.py", "（注意比赛项目：分数在那里决出）", "(attenzione alle prove: è lì che si vincono i punti)")
rep("content56.py", "（和朋友猜谁能留到最后）", "(indovina con gli amici chi resiste più a lungo)")
rep("content56.py", "（下周这里继续报道进展）", "(la prossima settimana qui leggi come va avanti)")
rep("content56.py", 'f.gloss("het eiland 岛 · de proef 比赛项目、考验 · stemmen 投票 · de aflevering （一）集 · voorbij 过去了、结束了。")',
     'f.gloss("het eiland = isola · de proef = prova, sfida · stemmen = votare · de aflevering = puntata · voorbij = finito, passato.")')
rep("content56.py", '"你看《荒岛远征》吗，还是更爱自己出门活动？写两句荷兰语寄来。"',
     '"Guardi Expeditie Robinson, o preferisci fare qualcosa fuori tu stesso? Scrivi due frasi in olandese e mandale alla redazione."')
rep("content56.py", '"EN JIJ? · 说说你自己"', '"EN JIJ? · E TU?"')
rep("content56.py", '"OEFENINGEN · 第 5 版练习"', '"OEFENINGEN · ESERCIZI A PAGINA 5"')
rep("content56.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Risposte a pagina 8 · i livelli sono misti; cerca il tuo numero"')
rep("content56.py", 'e.bridge("读第 5 版文章，选出正确答案。")', 'e.bridge("Leggi l\'articolo a pagina 5 e scegli la risposta giusta.")')
rep("content56.py", '"Robinson 在 11 月 1 日周日开始"', '"Robinson è iniziato domenica 1º novembre"')
rep("content56.py", '"19 位参赛者"', '"19 concorrenti"')
rep("content56.py", '"ADE 今年 30 年"', '"L\'ADE compie 30 anni quest\'anno"')
rep("content56.py", '"设计周约 2.500 位设计师"', '"La Design Week ha mostrato circa 2.500 designer"')
rep("content56.py", '"ADE 与 DDW 在 10 月 25 日周日落幕"', '"ADE e DDW si sono chiusi domenica 25 ottobre"')
rep("content56.py", 'e.bridge("用方框里的词填空。")', 'e.bridge("Completa con le parole nel riquadro.")')
rep("content56.py", '"eiland = 岛（het）"', '"eiland = isola (het)"')
rep("content56.py", '"proef = 比赛项目、考验（de）"', '"proef = prova, sfida (de)"')
rep("content56.py", '"stemmen = 投票"', '"stemmen = votare"')
rep("content56.py", '"aflevering = （一）集"', '"aflevering = puntata"')
rep("content56.py", '"voorbij = 过去了、结束了"', '"voorbij = finito, passato"')
rep("content56.py", '"kandidaat 复数：kandidaten"', '"Plurale di kandidaat: kandidaten"')
rep("content56.py", 'e.bridge("用 gaan + 不定式说将来。")', 'e.bridge("Usa gaan + infinito per parlare del futuro.")')
rep("content56.py", '"gaat winnen = 会赢（只是猜测）"', '"gaat winnen = vincerà (solo un\'ipotesi)"')
rep("content56.py", '"wij → gaan + 不定式 kijken"', '"wij → gaan + infinito kijken"')
rep("content56.py", '"hij → gaat praten"', '"hij → gaat praten"')
rep("content56.py", '"zij (复数) → gaan zoeken"', '"zij (plurale) → gaan zoeken"')
rep("content56.py", '"对：11 月 1 日开始"', '"Vero: è iniziato il 1º novembre"')
rep("content56.py", '"错：ADE 今年 30 年"', '"Falso: l\'ADE compie 30 anni quest\'anno"')
rep("content56.py", '"错：10 月 25 日已落幕"', '"Falso: si è già chiuso il 25 ottobre"')
# ---------- content56: P6 ----------
rep("content56.py", 'p.band("VERDIEPING · 深读", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · 气象预警深度解读")',
     'p.band("VERDIEPING · APPROFONDIMENTO", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · I codici del KNMI in profondità")')
rep("content56.py", 'f.gloss("de meteoroloog 气象学家 · waarschuwingsmoeheid 预警疲劳 · vastzetten 固定好 · het advies 建议、忠告 · de voorstander 支持者。")',
     'f.gloss("de meteoroloog = meteorologo · waarschuwingsmoeheid = stanchezza da allarmi · vastzetten = fissare bene · het advies = consiglio · de voorstander = sostenitore.")')
rep("content56.py", '"练习数据：虚构数字，仅供练习，非真实调查。问题：橙色预警时你会怎么做？（100 名年轻人）"',
     '"Dati di esercitazione: numeri inventati solo per esercitarsi, non un vero sondaggio. Domanda: cosa fai con il codice arancione? (100 giovani)"')
rep("content56.py", '"DE GRAFIEK · 图表（练习数据）"', '"DE GRAFIEK · GRAFICO (DATI DI ESERCITAZIONE)"')
rep("content56.py", '"VOOR OF TEGEN? · 正方还是反方"', '"VOOR OF TEGEN? · A FAVORE O CONTRO?"')
rep("content56.py", '"OEFENINGEN · 第 6 版练习"', '"OEFENINGEN · ESERCIZI A PAGINA 6"')
rep("content56.py", 'e.bridge("看第 6 版图表（练习数据）回答。")', 'e.bridge("Rispondi dal grafico a pagina 6 (dati di esercitazione).")')
rep("content56.py", '"45 名年轻人选择待在家里"', '"45 giovani scelgono di restare a casa"')
rep("content56.py", '"25 人先看预警文字"', '"25 leggono prima il testo dell\'avviso"')
rep("content56.py", '"45 + 25 = 70"', '"45 + 25 = 70"')
rep("content56.py", '"10 人不知道"', '"10 non lo sanno"')
rep("content56.py", '"图表共 100 人：45+25+20+10"', '"Il grafico conta 100 persone: 45+25+20+10"')
rep("content56.py", 'e.bridge("读第 6 版文章，选出正确答案。")', 'e.bridge("Leggi l\'articolo a pagina 6 e scegli la risposta giusta.")')
rep("content56.py", '"以前预警针对整个省"', '"Un tempo gli avvisi riguardavano un\'intera provincia"')
rep("content56.py", '"如今预警是本地的"', '"Oggi gli avvisi sono locali"')
rep("content56.py", '"红色：非常危险，非必要不上路"', '"Codice rosso: molto pericoloso, non uscire se non devi"')
rep("content56.py", '"预警疲劳：警告太多导致不再注意"', '"Stanchezza da allarmi: troppi avvisi, così non si fa più attenzione"')
rep("content56.py", '"KNMI 说：看代码旁边的文字"', '"Il KNMI dice: leggi il testo accanto al codice"')
rep("content56.py", '"lokaal = 本地的"', '"lokaal = locale"')
rep("content56.py", '"waarschuwingsmoeheid = 预警疲劳"', '"waarschuwingsmoeheid = stanchezza da allarmi"')
rep("content56.py", '"vastzetten = 固定好"', '"vastzetten = fissare bene"')
rep("content56.py", '"advies = 建议（het）"', '"advies = consiglio (het)"')
rep("content56.py", 'e.bridge("把词组成正确的句子。")', 'e.bridge("Metti le parole nell\'ordine giusto per formare frasi.")')
rep("content56.py", '"主语 + 动词 + 地点"', '"Soggetto + verbo + luogo"')
rep("content56.py", '"祈使句：动词在首位"', '"Imperativo: il verbo viene per primo"')
rep("content56.py", '"weinig voor = 很少出现"', '"weinig voor = si presenta raramente"')
rep("content56.py", '"raakt + 宾语 + 方式"', '"raakt + oggetto + modo"')

# ---------- content7: P7 ----------
rep("content7.py", 'p.band("TAAL · 语言", "De Lucerna", "聚焦语言 · Drie niveaus, drie gereedschappen · 三个级别，三件工具")',
     'p.band("TAAL · LINGUA", "De Lucerna", "Focus sulla lingua · Drie niveaus, drie gereedschappen · Tre livelli, tre strumenti")')
rep("content7.py", 'a.bridge("het klimaat 气候（长期）；een boom planten 种树；besparen 节约；de waarschuwing 预警。")',
     'a.bridge("het klimaat = il clima (a lungo termine); een boom planten = piantare un albero; besparen = risparmiare; de waarschuwing = avviso, allarme.")')
rep("content7.py", '"气候是长期的天气与自然"', '"Il clima è il tempo e la natura a lungo termine"')
rep("content7.py", '"rood = blijf binnen"', '"rood = resta in casa"')
rep("content7.py", 'b.bridge("meedoen 参加：ik doe mee；opruimen 收拾：wij hebben opgeruimd；vastzetten 固定：zij zette vast。")',
     'b.bridge("meedoen = partecipare: ik doe mee; opruimen = riordinare: wij hebben opgeruimd; vastzetten = fissare: zij zette vast.")')
rep("content7.py", '"opruimen 的分词：opgeruimd"', '"Participio di opruimen: opgeruimd"')
rep("content7.py", '"vastzetten 过去时：zette vast"', '"Passato di vastzetten: zette vast"')
rep("content7.py", '"meedoen = 参加、参与"', '"meedoen = partecipare"')
rep("content7.py", 'c.bridge("Ik vind dat… 我认为；Volgens mij… 依我看；Het lijkt me dat… 在我看来。")',
     'c.bridge("Ik vind dat… = Penso che…; Volgens mij… = Secondo me…; Het lijkt me dat… = Mi sembra che…")')
rep("content7.py", '"Volgens mij… = 依我看"', '"Volgens mij… = Secondo me…"')
rep("content7.py", '"Ik vind dat… 表达看法"', '"Ik vind dat… esprime un\'opinione"')
rep("content7.py", '"Het lijkt me dat… = 在我看来"', '"Het lijkt me dat… = Mi sembra che…"')
rep("content7.py", '"气候是长期的天气自然，不是今天的天气。"', '"Il clima è il tempo e la natura a lungo termine, non il tempo di oggi."')
rep("content7.py", '"Klimaatweek 是专名，首字母大写。"', '"Klimaatweek è un nome proprio, quindi si scrive con la maiuscola."')
rep("content7.py", '"een 是单数：een boom；复数直接用 bomen。"', '"«Een» è singolare: «een boom» oppure «bomen»."')
rep("content7.py", '"omdat 从句后，主句动词在第二位：blijf ik thuis。"', '"Dopo «omdat» il verbo della frase principale va al secondo posto: «... blijf ik thuis»."')
rep("content7.py", '"PAS OP! · 易错诊所"', '"PAS OP! · ERRORI FREQUENTI"')
# HET WOORD box: the Dutch definition sentence wt stays VERBATIM (frozen);
# only the gloss line is localised (de-nl/de-pt standing ruling).
rep("content7.py", '"meedoen = 参加、参与：气候周全荷兰都参加。"',
     '"meedoen = partecipare, esserci: tutta l\'Olanda partecipa alla Settimana del clima."')
rep("content7.py", '"HET WOORD · 本周生词"', '"HET WOORD · LA PAROLA"')
# readers' corner: Dutch example + Dutch disclosure stay verbatim (frozen);
# the Chinese disclosure + invitation lines become Italian. The Italian
# disclosure carries all three facts (no real letters, no best P8 texts,
# example + VOL.3 promise); the invitation is an imperative with a
# publication promise.
rep("content7.py", 'dt_zh = "截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。"',
     'dt_it = "Al momento della stampa non erano arrivate lettere vere né i migliori testi di pagina 8: per questo pubblichiamo un esempio; la promessa vale per il VOL.3."')
rep("content7.py", 'len(wrap(dt_zh, "sans", False, 20, CW - 44))', 'len(wrap(dt_it, "sans", False, 20, CW - 44))')
rep("content7.py", 'p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
     'p.para(bx + 22, yy3 + 20, dt_it, 20, "sans", False, GREY, CW - 44, 1.42) + 10')
rep("content7.py", '"编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！"',
     '"Esempio della redazione, non una lettera vera. Mandaci la tua lettera vera e il tuo miglior testo di pagina 8: li pubblicheremo nel VOL.3!"')
rep("content7.py", '"ZINNEN VAN DE WEEK · 本周金句（逐字摘自本期文章）"',
     '"ZINNEN VAN DE WEEK · FRASI DELLA SETTIMANA (PAROLE TESTUALI DA QUESTO NUMERO)"')
rep("content7.py", '"从 11 月 2 日周一到 8 日周日，荷兰是气候周。"', '"Da lunedì 2 a domenica 8 novembre, in Olanda è la Settimana del clima."')
rep("content7.py", '"秋天是种树的最好时节。"', '"L\'autunno è il momento migliore per piantare."')
rep("content7.py", '"黄色意味着：当心，天气可能危险。"', '"Il giallo significa: attenzione, il tempo potrebbe essere pericoloso."')
rep("content7.py", '"70 多家博物馆从晚上 19 点开放到凌晨 2 点。"', '"Oltre 70 musei sono aperti dalle 19:00 di sera alle 02:00 di notte."')
rep("content7.py", '"阿贾克斯 10 月 22 日周四 2–0 战胜亚特兰大。"', '"Giovedì 22 ottobre l\'Ajax ha battuto l\'Atalanta 2–0."')
rep("content7.py", '"11 月 1 日周日，《荒岛远征》在 RTL 4 开播，20 点。"', '"Domenica 1º novembre Expeditie Robinson è iniziato su RTL 4, alle 20:00."')
rep("content7.py", '"预警代码不是禁令，而是一条建议。"', '"Un codice non è un divieto, ma un consiglio."')
rep("content7.py", '"天气属于我们所有人，但对每个人的影响各不相同。"', '"Il tempo è di tutti noi, ma ci tocca in modo diverso."')
rep("content7.py", '"VOLGENDE WEEK · 下期预告 (VOL.3)"', '"VOLGENDE WEEK · LA PROSSIMA SETTIMANA (VOL.3)"')
# ---------- content8: P8 ----------
rep("content8.py", 'p.band("TOETS EN ANTWOORDEN · 练习与答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")',
     'p.band("TOETS EN ANTWOORDEN · TEST E RISPOSTE", "De Lucerna", "Pagina 8 · De grote toets van de week + alle antwoorden")')
rep("content8.py", '"科弗登发放 200 棵树木灌木"', '"Coevorden regala 200 alberi e arbusti"')
rep("content8.py", '"特温特–阿贾克斯 13:30 开球"', '"Twente–Ajax inizia alle 13:30"')
rep("content8.py", '"阿贾克斯 2–0 赢亚特兰大"', '"L\'Ajax ha battuto l\'Atalanta 2–0"')
rep("content8.py", '"气候周到 11 月 8 日"', '"La Settimana del clima dura fino all\'8 novembre"')
rep("content8.py", '"博物馆之夜在 11 月 7 日"', '"La Notte dei musei è il 7 novembre"')
rep("content8.py", '"Robinson 在 11 月开始"', '"Robinson è iniziato a novembre"')
rep("content8.py", '"橙色预警：天气危险"', '"Codice arancione: il tempo è pericoloso"')
rep("content8.py", '"meedoen = 参加"', '"meedoen = partecipare"')
rep("content8.py", '"气候周 11 月 2 日周一开始"', '"La Settimana del clima inizia lunedì 2 novembre"')
rep("content8.py", '"发放地点在兹韦洛"', '"Il luogo della distribuzione è Zweeloo"')
rep("content8.py", '"Crossing Border 在海牙"', '"Crossing Border è all\'Aia"')
rep("content8.py", '"PAN 在 RAI 展览中心"', '"Il PAN è al RAI"')
rep("content8.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"Il Real Betis ha battuto il Feyenoord 1–0"')
rep("content8.py", '"10 轮后阿贾克斯 21 分"', '"Dopo 10 giornate l\'Ajax ha 21 punti"')
rep("content8.py", '"预警疲劳：警告太多导致不再注意"', '"Stanchezza da allarmi: troppi avvisi, così non si fa più attenzione"')
rep("content8.py", '"扎安丹旧货市场约 250 个摊位"', '"Il mercatino di Zaandam ha circa 250 bancarelle"')
rep("content8.py", '"Daan 住在科弗登"', '"Daan abita a Coevorden"')
rep("content8.py", '"他周六领了一棵免费灌木"', '"Sabato ritira un arbusto gratuito"')
rep("content8.py", '"周日特温特对阿贾克斯"', '"Domenica il Twente gioca contro l\'Ajax"')
rep("content8.py", '"气候周他每天骑车上学"', '"Durante la Settimana del clima va a scuola in bici ogni giorno"')
rep("content8.py", '"主语 + 动词 + 时间"', '"Soggetto + verbo + tempo"')
rep("content8.py", '"主语 + 动词 + 宾语 + 地点"', '"Soggetto + verbo + oggetto + luogo"')
rep("content8.py", '"主语 + 动词 + 时间 + 对手"', '"Soggetto + verbo + tempo + avversario"')
rep("content8.py", '"可分动词 mee 在句末"', '"Verbo separabile: mee va alla fine"')
# E137/E138 keys re-aim at Italian (translation items, W43 NL x IT precedent);
# E139/E140 keys stay Dutch, only their printed stems are Italian (above).
rep("content8.py", '"气候周持续七天。"', '"La Settimana del clima dura sette giorni."')
rep("content8.py", '"对照第 1 版头条"', '"Confronta con il titolo di pagina 1"')
rep("content8.py", '"橙色预警意味着：做好准备。"', '"Il codice arancione significa: preparati."')
rep("content8.py", '"第 2 版原句 · bereid je voor 做好准备"', '"Frase originale di pagina 2 · bereid je voor = preparati"')
rep("content8.py", '"注意时间表达 van...tot..."', '"Attenzione alla formula van...tot..."')
rep("content8.py", '"meedoen 是可分动词"', '"meedoen è un verbo separabile"')
rep("content8.py", '["klimaat=气候 c", "meedoen=参加 b", "waarschuwing=预警 a", "vastzetten=固定好 d"]',
     '["klimaat = clima c", "meedoen = partecipare b", "waarschuwing = avviso a", "vastzetten = fissare bene d"]')
rep("content8.py", 'instr="把词和释义配对"', 'instr="Abbina la parola al significato"')
rep("content8.py", '"boom = 树"', '"boom = albero"')
rep("content8.py", '"struik = 灌木"', '"struik = arbusto"')
rep("content8.py", '"planten = 种"', '"planten = piantare"')
rep("content8.py", '"zachte = 柔软的（土壤）"', '"zachte = morbido (terreno)"')
rep("content8.py", '"发放到 16:00 结束"', '"La distribuzione finisce alle 16:00"')
rep("content8.py", 'f.bridge(f"writing题（无唯一答案）；范文（{NWORDS} 词）见下。")',
     'f.bridge(f"Tema (nessuna risposta unica); testo modello ({NWORDS} parole) sotto.")')
rep("content8.py", '"（开放题，范文如下）"', '"(tema aperto, testo modello sotto)"')
rep("content8.py", 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"Vedi il testo modello nella sezione H ({NWORDS} parole)"')
rep("content8.py", '"ANTWOORDEN · 参考答案 — 按版面分页排列，找到题号即可"',
     '"ANTWOORDEN · RISPOSTE — in ordine di pagina: cerca il tuo numero"')
rep("content8.py", '"每题附一句中文简析 · 带 ✓ 的为范文题"',
     '"Ogni risposta ha una breve nota in italiano · ✓ indica il tema"')
# svglib code comment only (never rendered): keep the file CJK-free like W43 IT
rep("svglib.py", "for 重阳", "per la Festa del Doppio Nove")

# ---------- apply ----------
def main():
    zeros = []
    for f, old, new in R:
        path = os.path.join(HERE, f)
        txt = open(path, encoding="utf-8").read()
        n = txt.count(old)
        if n == 0:
            zeros.append((f, old[:70]))
        txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
        print(f"{f}: {n}x {old[:60]!r}")
    print("TOTAL replacements:", len(R))
    print("ZERO-COUNT replacements:", len(zeros))
    for f, old in zeros:
        print("  ZERO:", f, repr(old))

if __name__ == "__main__":
    main()
