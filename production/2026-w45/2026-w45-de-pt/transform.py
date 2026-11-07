# -*- coding: utf-8 -*-
"""DE x PT fan-out transform for W45 DE core build copy.
Rules: whole-line or exact-unique-literal replacements with count
assertions; value maps (types/instr) use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Run once from the build dir copy.
"""
import os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = []

def rep(fname, old, new, expect=None):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    else:
        assert n >= 1, f"{fname}: {old!r} not found"
    LOG.append(f"{fname}: {n}x {old!r} -> {new!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))

def rep_all(fname, pairs):
    for old, new in pairs:
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-de-core", "weekly-report-w45-de-pt", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "para o Festival do Duplo Nono.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 DE x PT shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · SEMANÁRIO ALEMÃO VOL.2 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Nota — " + s', 1)

# ---------- shared furniture strings ----------
SHARED = [
    ("UND SIE? · 说说你自己", "UND SIE? · E você?"),
    ("FERIENWECHSEL · 假期交接", "FERIENWECHSEL · Férias"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Respostas na página 8 · Os níveis misturam-se livremente — procure cada resposta pelo número"),
    ("BEISPIELE · 例句", "BEISPIELE · Exemplos"),
]
for f in ["content12.py", "content34.py", "content56.py"]:
    for old, new in SHARED:
        # only apply where present
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · TODA SEMANA · O ALEMÃO QUE OS ALEMÃES LEEM"),
    ("德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理",
     "SEMANÁRIO ALEMÃO · VOL.2 · FUTEBOL · DESCONTO · CUIDADOS"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 20pt bold olive
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 20, "sans", True, BRICK, anchor="middle")'),
    ("本周足球周 · 欧冠欧联德甲连轴转", "Semana de futebol"),
    ("详见第 4 版 · Seite 4", "Veja a página 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · Manchete"),
    ("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。",
     "Notes — die Englische Woche = semana inglesa · der Spieltag = rodada · empfangen = receber em casa · die Bundesliga = Bundesliga."),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · Números"),
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）",
     "9 — Spiele hat der 9. Spieltag der Bundesliga (9 jogos na 9ª rodada)"),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）",
     "6 — deutsche Teams spielen in Europa (6 times alemães jogam na Europa)"),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）",
     "14,04 — Cent pro Liter beträgt der Tankrabatt (14,04 centavos por litro)"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · Pratique agora"),
    ("一周双赛", "semana inglesa"),
    ("多特主场迎战贝蒂斯", "Dortmund recebe o Betis"),
    ("欧联在周四", "Liga Europa na quinta-feira"),
    ("周五汉堡–门兴开轮", "Hamburgo–Gladbach abrem na sexta-feira"),
    ("第 9 轮共 9 场", "9 jogos na 9ª rodada"),
    ("减税到 12 月 31 日", "desconto vai até 31 de dezembro"),
    ("拜仁周二客战马竞", "Bayern fora contra o Atlético na terça-feira"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim fora contra o Crystal Palace na Liga Europa"),
    ("本周大问题 · Die Fragen der Woche", "As grandes perguntas da semana"),
    ("德国本周最热议的五个问题。", "As cinco perguntas mais debatidas."),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · Sumário"),
    ("油价减税（加油折扣）。详见第 2 版。", "Desconto no combustível. Veja a página 2."),
    ("KURZ & GUT · 快讯", "KURZ & GUT · Em resumo"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · Quiz-relâmpago"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Leia a página 1 e escolha a resposta certa · Respostas na página 8"),
    # P2
    ("LEBEN · 生活", "LEBEN · Vida"),
    ("LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理",
     "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · Desconto no combustível, imposto sobre a eletricidade e cuidados"),
    ("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。",
     "der Tankrabatt = desconto no combustível · die Zapfsäule = bomba de gasolina · die Energiesteuer = imposto sobre a energia · die Mehrwertsteuer = IVA · der Angehörige = familiar."),
    ("AN DER ZAPFSÄULE · 加油机旁", "AN DER ZAPFSÄULE · Na bomba"),
    ("你开车吗？你那里的油价是多少？写两句德语寄来。",
     "Você dirige? Quanto custa a gasolina aí? Escreva duas frases em alemão!"),
    ("ZEW IN KÜRZE · ZEW 指数简讯", "ZEW IN KÜRZE · ZEW em resumo"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · Vamos calcular"),
    ("Die Zahlen der Woche · 本周数字", "Die Zahlen der Woche · Os números da semana"),
    ("注意：减的是税，定价的是油站。出发前比比价。",
     "Atenção: o imposto cai — mas o posto define o preço. Compare os preços antes de abastecer!"),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · Exercícios da página 2"),
    ("看第 2 版文章，用数字填空。", "Leia o artigo da página 2 e complete com os números."),
    ("每升减税 14.04 欧分", "14,04 centavos a menos de imposto por litro"),
    ("50 升省约 8.35 欧元", "cerca de 8,35 euros economizados em 50 litros"),
    ("减税到 2026 年底", "desconto vai até o fim de 2026"),
    ("国家少收约 25 亿欧元", "o Estado abre mão de cerca de 2,5 bilhões de euros"),
    ("加油机旁的实际降幅", "o corte na bomba, com IVA"),
    ("改成 Perfekt 现在完成时。", "Reescreva no Perfekt (pretérito perfeito)."),
    ("beschließen → beschlossen", "beschließen → beschlossen"),
    ("fallen 用 sein", "fallen usa sein"),
    ("tanken → getankt", "tanken → getankt"),
    ("weitergeben 可分动词", "weitergeben é separável"),
    ("ZEW 预期下降", "as expectativas do ZEW caíram"),
    ("读第 2 版文章，选出正确答案。", "Leia o artigo da página 2 e escolha a resposta certa."),
    ("减的是能源税", "é o imposto sobre a energia que cai"),
    ("油站定价", "o posto define o preço"),
    ("联盟党与社民党", "União e SPD"),
    ("家属居家护理", "familiares cuidam em casa"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = desconto no combustível b"),
    ("Zapfsäule=加油机 d", "Zapfsäule = bomba de gasolina d"),
    ("Mehrwertsteuer=增值税 a", "Mehrwertsteuer = IVA a"),
    ("Angehörige=亲属 c", "Angehörige = familiar c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · Cultura"),
    ("A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天",
     "A2 → B1 · Ferienwechsel & Herbst · Mudança de férias e outono"),
    ("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。",
     "der Ferienwechsel = mudança de férias · die Schülerin = aluna · der Ausflug = passeio · der Advent = Advento · die Lesung = leitura."),
    ("der Nebel — 雾", "der Nebel — neblina"),
    ("das Laub — 落叶", "das Laub — folhagem"),
    ("der Kürbis — 南瓜", "der Kürbis — abóbora"),
    ("die Kerze — 蜡烛", "die Kerze — vela"),
    ("der Spaziergang — 散步", "der Spaziergang — passeio a pé"),
    ("die Lesung — 朗读会", "die Lesung — leitura"),
    ("HERBSTWÖRTER · 秋天词汇", "HERBSTWÖRTER · Outono"),
    ("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。",
     "No outono você lê mais? Que livro está na sua cabeceira? Escreva duas frases!"),
    ("DER TIPP · 编辑部建议", "DER TIPP · Dica da redação"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · Exercícios da página 3"),
    ("读第 3 版文章，判断对错。", "Leia o artigo da página 3. Certo ou errado?"),
    ("BW 周一起复课", "Baden-Württemberg de volta na segunda-feira"),
    ("巴伐利亚本周仍在放假", "A Baviera ainda está de férias esta semana"),
    ("诸圣节 11 月 1 日", "O Dia de Todos os Santos é 1º de novembro"),
    ("10 月 31 日也是宗教改革日（九个州）", "31 de outubro também é o Dia da Reforma em nove estados"),
    ("诸圣节商店关门", "lojas fechadas no Dia de Todos os Santos"),
    ("用方框里的词填空。", "Complete com as palavras do quadro."),
    ("假期交接", "mudança de férias"),
    ("去山区短途出游", "um passeio nas montanhas"),
    ("图书馆的朗读会", "uma leitura na biblioteca"),
    ("将临期在 11 月筹划", "o Advento planejado em novembro"),
    ("湖面上的雾", "neblina sobre o lago"),
    ('e.bridge("选出正确答案。")', 'e.bridge("Escolha a resposta certa.")'),
    ("BW 假期已结束", "as férias de Baden-Württemberg acabaram"),
    ("安静的节日", "um feriado tranquilo"),
    ("诸圣节扫墓", "visitar túmulos no Dia de Todos os Santos"),
    ("白天短所以夜晚长", "dias curtos, por isso noites longas"),
    ("把词组成正确的句子。", "Forme uma frase correta com as palavras."),
    ("时间地点开头，动词第二位", "tempo e lugar primeiro, verbo em segundo"),
    ("数量时间状语，动词第二位", "expressão de tempo primeiro, verbo em segundo"),
    ("主谓宾顺序", "ordem sujeito–verbo–objeto"),
    ("bleiben + geschlossen", "bleiben + geschlossen"),
    # P4
    ("SPORT · 体育", "SPORT · Esporte"),
    ("LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲",
     "LEVEL B1 · Europapokal & Bundesliga · Taças europeias e Bundesliga"),
    ("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。",
     "die Englische Woche = semana inglesa · auswärts = fora de casa · empfangen = receber em casa · der Favorit = favorito · eröffnen = abrir."),
    ("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。",
     "Para quem você torce? Quem vence no sábado? Escreva duas frases!"),
    ("DER 9. SPIELTAG · 第 9 轮赛程", "DER 9. SPIELTAG · Jogos da 9ª rodada"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · Exercícios da página 4"),
    ("读第 4 版文章，选出正确答案。", "Leia o artigo da página 4 e escolha a resposta certa."),
    ("拜仁周二客战马竞", "Bayern fora contra o Atlético na terça-feira"),
    ("斯图加特 18:45 开球", "Stuttgart começa às 18:45"),
    ("多特主场迎战贝蒂斯", "Dortmund recebe o Betis"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim fora contra o Crystal Palace na Liga Europa"),
    ("周六焦点战斯图加特–不来梅", "O grande jogo de sábado é Stuttgart–Bremen"),
    ("Englische Woche=一周双赛 a", "Englische Woche = semana inglesa a"),
    ("auswärts=客场 b", "auswärts = fora de casa b"),
    ("Favorit=热门 c", "Favorit = favorito c"),
    ("eröffnen=揭开序幕 d", "eröffnen = abrir d"),
    ("用比较级完成句子（括号里是原级）。", "Complete com o comparativo (a palavra entre parênteses está no grau positivo)."),
    ("schwer → schwerer", "schwer → schwerer"),
    ("spät → später（19:30 最晚）", "spät → später (19:30 é o mais tarde)"),
    ("viel → mehr（球迷想要更多）", "viel → mehr (os torcedores querem mais)"),
    ("früh → früher（18:45 早于 21:00）", "früh → früher (18:45 é mais cedo que 21:00)"),
    ("看上面的赛程表，选出正确答案。", "Olhe a tabela de jogos acima e escolha a resposta certa."),
    ("汉堡–门兴周五 20:30", "Hamburgo–Gladbach na sexta-feira às 20:30"),
    ("斯图加特–不来梅周六 18:30", "Stuttgart–Bremen no sábado às 18:30"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke no domingo às 19:30"),
    ("弗赖堡–柏林联周日 17:30", "Freiburg–Union no domingo às 17:30"),
    ("欧联周四霍芬海姆 18:45", "Liga Europa na quinta-feira, Hoffenheim às 18:45"),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · Juventude"),
    ("LEVEL B1 · Zurück in die Schule · 重返校园",
     "LEVEL B1 · Zurück in die Schule · De volta à escola"),
    ("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。",
     "der Pausenhof = pátio da escola · die Klassenarbeit = prova de classe · das Referat = apresentação oral · ausschlafen = dormir até tarde · die Probe = ensaio."),
    ("der Pausenhof — 课间操场", "der Pausenhof — pátio da escola"),
    ("die Klassenarbeit — 课堂测验", "die Klassenarbeit — prova de classe"),
    ("das Referat — 课堂报告", "das Referat — apresentação oral"),
    ("der Rucksack — 书包", "der Rucksack — mochila"),
    ("ausschlafen — 睡懒觉", "ausschlafen — dormir até tarde"),
    ("die Probe — 排练", "die Probe — ensaio"),
    ("SCHULWÖRTER · 校园词汇", "SCHULWÖRTER · Escola"),
    ("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。",
     "Quando você voltou? Qual foi a sua primeira aula? Escreva duas frases!"),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划",
     "DER WOCHENPLAN DER REDAKTION · A semana da redação"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · Exercícios da página 5"),
    ("读第 5 版文章，选出正确答案。", "Leia o artigo da página 5 e escolha a resposta certa."),
    ("BW 11 月 2 日开学", "Baden-Württemberg de volta em 2 de novembro"),
    ("巴伐利亚假期未结束", "as férias da Baviera não acabaram"),
    ("开学周有课堂测验", "provas de classe já na primeira semana"),
    ("Referat = 课堂报告", "Referat = apresentação oral"),
    ("巴伐利亚学生周五可去球场", "os alunos bávaros podem ir ao estádio na sexta-feira"),
    ("课间操场上玩", "brincar no pátio da escola"),
    ("数学课堂测验", "uma prova de matemática"),
    ("报告要读三本书", "três livros para ler para a apresentação"),
    ("假期可以睡懒觉", "dormir até tarde nas férias"),
    ("圣诞演出的第一次排练", "o primeiro ensaio para o Natal"),
    ("书包里有本子铅笔", "mochila pronta: cadernos, canetas"),
    ("用 weil 连接两个句子（动词放句末）。", "Junte as duas frases com weil (o verbo vai para o fim)."),
    ("weil 句动词置尾", "na oração com weil, o verbo vai para o fim"),
    ("ist 置尾", "ist vai para o fim"),
    ("muss 置尾", "muss vai para o fim"),
    ("liegen 置尾", "liegen vai para o fim"),
    ("判断对错。", "Certo ou errado?"),
    ("BW 11 月 2 日复课", "Baden-Württemberg de volta em 2 de novembro"),
    ("全德假期并未都结束", "as férias não acabaram em toda a Alemanha"),
    ("开学周有测验与报告", "provas e apresentações na primeira semana"),
    # P6
    ("VERTIEFUNG · 深读", "VERTIEFUNG · Leitura aprofundada"),
    ("LEVEL B2 · Pflege & Stromsteuer · 护理与电力税",
     "LEVEL B2 · Pflege & Stromsteuer · Cuidados e imposto sobre a eletricidade"),
    ("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。",
     "der Angehörige = familiar · die Pflegeversicherung = seguro de cuidados · der Pflegedienst = serviço de cuidados · die Stagnation = estagnação · der Aufschwung = recuperação."),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · Números"),
    ("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。",
     "O cuidado em casa precisa de mais ajuda — ainda em debate. O corte no imposto sobre a eletricidade ainda está em aberto. Ambos custam dinheiro e afetam quase todas as famílias."),
    ("PRO & CONTRA · 正方与反方 — die Argumente der Debatte",
     "PRO & CONTRA · A favor e contra — os argumentos do debate"),
    ("WER PFLEGT ZU HAUSE? · 谁在家护理？", "WER PFLEGT ZU HAUSE? · Quem cuida em casa?"),
    ("家属护理", "em família"),
    ("专业上门", "serviço"),
    ("住养老院", "em lar"),
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · Dados de prática — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Exemplo de prática da redação, não uma pesquisa real.)"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · Exercícios da página 6"),
    ("看上面的练习图表，选出正确答案。", "Olhe o gráfico de prática acima e escolha a resposta certa."),
    ("serviço 20% 第二", "serviço de cuidados 20% é o segundo"),  # after chart-label rep
    ("68+20=88", "68 + 20 = 88"),
    ("养老院 12% 最小", "lar de idosos 12% é o menor"),
    ("养老院 12%", "lar de idosos 12%"),
    ("68+20+12=100", "68 + 20 + 12 = 100"),
    ("读第 6 版深读文章，选出正确答案。", "Leia o artigo aprofundado da página 6 e escolha a resposta certa."),
    ("10 月 26 日节目讨论居家护理", "o programa de 26 de outubro debateu o cuidado em casa"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "segundo o programa Hart aber fair da ARD, de 26 de outubro, mais de seis milhões de pessoas precisam de cuidados"),
    ("家属居家护理", "familiares cuidam em casa"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "segundo o programa Hart aber fair da ARD, de 26 de outubro, cerca de dez milhões de pessoas cuidam de familiares"),
    ("用括号里的形式填空。", "Complete com a forma entre parênteses."),
    ("被动：wird + Partizip II", "passiva: wird + Partizip II"),
    ("ob 引导间接疑问句", "ob introduz uma pergunta indireta"),
    ("steigen → steigt", "steigen → steigt"),
    ("sagen 过去时 sagte", "sagen no passado: sagte"),
    ("用方框里的词填空。", "Complete com as palavras do quadro."),
    ("护理保险出更多钱", "o seguro de cuidados deve pagar mais"),
    ("亲属居家护理", "familiares cuidam em casa"),
    ("走出停滞", "sair da estagnação"),
    ("复苏尚未自我维持", "a recuperação ainda não se sustenta sozinha"),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("SPRACHE · 语言", "SPRACHE · Língua"),
    ("BEISPIELE · 例句", "BEISPIELE · Exemplos"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · Frases da semana e clínica de erros"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "Esta página é toda sobre língua: três lições curtas, as frases da semana (todas citadas palavra por palavra dos artigos desta edição), a clínica de erros e as cartas dos leitores."),
    ("被动：wird + Partizip II", "passiva: wird + Partizip II"),
    ("复数：werden", "plural: werden"),
    ("werden + 原形表将来", "werden + infinitivo para o futuro"),
    ("被动语态", "voz passiva"),
    ("spät → später（19:30 最晚）", "spät → später (19:30 é o mais tarde)"),
    ("weil 引导原因", "weil introduz um motivo"),
    ("weil 句动词置尾", "na oração com weil, o verbo vai para o fim"),
    ("länger als = 比……更长", "länger als = mais longo que"),
    ("A. 比平时更长 · B. 和平时一样 · C. 比平时更短",
     "A. mais longo que o habitual · B. igual ao habitual · C. mais curto que o habitual"),
    ("ob 引导间接疑问", "ob introduz uma pergunta indireta"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = é duvidoso se ..."),
    ("dass 句动词置尾", "na oração com dass, o verbo vai para o fim"),
    ("礼貌表达观点", "uma forma educada de dar uma opinião"),
    ("14,04 Cent = 每升 14.04 欧分", "14,04 Cent = 14,04 centavos por litro"),
    ("rund 8,35 Euro = 大约省 8.35 欧元", "rund 8,35 Euro = cerca de 8,35 euros"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = Será jogado"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach ... = opinião"),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass ... = Acho que ..."),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob ... = é duvidoso se ..."),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · Úteis"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · Cartas dos leitores"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · Mais uma palavra"),
    ("«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 油价减税。",
     "«der Tankrabatt» (Seite 2): die gesenkte Steuer auf Benzin und Diesel. Desconto no combustível."),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · Frases da semana"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "Citadas palavra por palavra dos artigos desta edição"),
    ("连续四个足球之夜，然后是整周末联赛。", "Quatro noites de futebol seguidas, depois um fim de semana inteiro de liga."),
    ("汽油和柴油的能源税每升降低 14.04 欧分。", "O imposto sobre a energia da gasolina e do diesel cai 14,04 centavos por litro."),
    ("加 50 升油，大约省 8.35 欧元。", "Se abastecer 50 litros, você economiza cerca de 8,35 euros."),
    ("秋假过后，学校又开学了。", "A escola recomeçou depois das férias de outono."),
    ("白天短，夜晚长。", "Os dias são curtos, as noites longas."),
    ("德国球队的两场艰难客场之战。", "Dois jogos difíceis fora de casa para os times alemães."),
    ("德国经济正在缓慢走出停滞，但复苏还不能自我维持。",
     "A economia alemã deixa devagar a estagnação, mas a recuperação não se sustenta sozinha."),
    ("缓慢向好——但不会自动变好。", "As coisas melhoram devagar — mas não sozinhas."),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · Clínica de erros"),
    ("学习者最常犯的四个错 · 先自己改，再看答案",
     "Os quatro erros mais frequentes dos aprendizes · corrija primeiro, depois confira"),
    ("动词第二位：主语不在句首时，动词仍居第二。",
     "Verbo em segundo: mesmo que o sujeito não venha primeiro, o verbo fica em segundo lugar."),
    ("halb acht = 七点半（acht 之前）。", "halb acht = 7h30, meia hora antes das oito."),
    ("Perfekt 中 Partizip II 放句末。", "No Perfekt, o Partizip II vai para o fim."),
    ("ob 从句动词放句末。", "Na oração com ob, o verbo vai para o fim."),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.3)", "IN DER NÄCHSTEN AUSGABE · Próxima edição (VOL.3)"),
]
rep_all("content7.py", C7)

# P7 readers box: label + two Portuguese paras replacing the Chinese note.
# German defer / reader / invite strings are FROZEN and stay untouched.
rep("content7.py", 'label = "Ein Beispiel der Redaktion!"',
    'label = "Um exemplo da redação!"', 1)
# P7 readers box: whole rh assignment replaced (formula gains one para
# transition for the second Portuguese para; trailing +32 = fix1's +16
# plus another +16, as in the W45 DE x EN build).
rep("content7.py",
    'rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
    '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
    '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
    '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
    '    + len(wrap(chinese, "sans", False, 19.5, CW - 44)) * 28 + 40 + 16',
    'rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
    '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
    '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
    '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
    '    + len(wrap(note_pt, "sans", False, 19.5, CW - 44)) * 28 + 8 \\\n'
    '    + len(wrap(invite_pt, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32', 1)
rep("content7.py", "last Chinese line", "last Portuguese line", 1)
rep("content7.py",
    'chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"',
    'note_pt = "Sem cartas reais nem melhores textos da página 8; a promessa passa ao VOL.3."\n'
    'invite_pt = "Escreva-nos! Envie a sua carta real e o seu texto da página 8 para o VOL.3."', 1)
rep("content7.py",
    'p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(ix + 22, yy3 + 19.5, note_pt, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8\n'
    'p.para(ix + 22, yy3 + 20.5, invite_pt, 20.5, "serif", False, INK, CW - 44, 1.42)', 1)

# ================= content8 (P8) =================
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · Exercícios e respostas"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · Teste final · Todas as respostas estão no fim desta página"),
    ("spielt（第三人称单数）", "spielt (3ª pessoa do singular)"),
    ("beginnt（第三人称单数）", "beginnt (3ª pessoa do singular)"),
    ("kauft（第三人称单数）", "kauft (3ª pessoa do singular)"),
    ("schnitzt 雕刻南瓜", "schnitzt = esculpir uma abóbora"),
    ("schläft（第三人称单数）", "schläft (3ª pessoa do singular)"),
    ("Tankrabatt 油价减税", "Tankrabatt = desconto no combustível"),
    ("geht（第三人称单数）", "geht (3ª pessoa do singular)"),
    ("erzählt（第三人称单数）", "erzählt (3ª pessoa do singular)"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · Texto lacunar"),
    ("选项：", "Opções:"),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · Perguntas"),
    ("减税到 2026 年 12 月 31 日", "desconto vai até 31 de dezembro de 2026"),
    ("拜仁周二客战马竞", "Bayern fora contra o Atlético na terça-feira"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim fora contra o Crystal Palace na Liga Europa"),
    ("BW 假期已结束", "as férias de Baden-Württemberg acabaram"),
    ("ZEW 预期 28.1", "expectativas do ZEW em 28,1"),
    ("周五汉堡–门兴开轮", "Hamburgo–Gladbach abrem na sexta-feira"),
    ("10 月 26 日节目讨论居家护理", "o programa de 26 de outubro debateu o cuidado em casa"),
    ("诸圣节 11 月 1 日", "O Dia de Todos os Santos é 1º de novembro"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · Leitura"),
    ("halb acht = 7:30", "halb acht = 7:30"),
    ("周二看拜仁客战马竞", "ver o Bayern fora contra o Atlético na terça-feira"),
    ("周六买南瓜", "comprar uma abóbora no sábado"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke no domingo às 19:30"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · Construir frases"),
    ("时间状语，动词第二位", "expressão de tempo primeiro, verbo em segundo"),
    ("主谓宾顺序", "ordem sujeito–verbo–objeto"),
    ("时间状语开头，动词第二位", "expressão de tempo primeiro, verbo em segundo"),
    ("地点开头，动词第二位", "lugar primeiro, verbo em segundo"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · Tradução"),
    ("（译成中文）", ""),
    # E keys: DE->EN re-aimed (keys change language by definition);
    # the 140 key stays German, only its prompt/instr change (below).
    ('"油价减税持续到十二月。"', '"O desconto no combustível vai até dezembro."'),
    ('"我周二看足球。"', '"Vejo futebol na terça-feira."'),
    ('"学校又开学了。"', '"A escola recomeçou."'),
    ("laufen = 持续", "laufen = durar, continuar"),
    ("schauen = 看", "schauen = ver"),
    ("wieder begonnen = 又开始", "wieder begonnen = recomeçou"),
    ("多睡一小时 = eine Stunde länger schlafen", "dormir uma hora a mais = eine Stunde länger schlafen"),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · Associe"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = desconto no combustível b"),
    ("Pflege=护理 d", "Pflege = cuidados d"),
    ("Advent=将临期 a", "Advent = Advento a"),
    ("Pausenhof=课间操场 c", "Pausenhof = pátio da escola c"),
    ("G · DIALOG · 对话补全", "G · DIALOG · Diálogo"),
    ("schaust（第二人称单数）", "schaust (2ª pessoa do singular)"),
    ("siehst（第二人称单数）", "siehst (2ª pessoa do singular)"),
    ("kochen（第一人称复数）", "kochen (1ª pessoa do plural)"),
    ("machst（第二人称单数）", "machst (2ª pessoa do singular)"),
    ("gehe（第一人称单数）", "gehe (1ª pessoa do singular)"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Tarefa aberta — siga os pontos do quadro de escrita; o texto-modelo está no quadro desta página"),
    ("按要点给分", "Avaliação pelos pontos indicados"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · Escrita"),
    ("用德语写 80–100 词：《我的足球周》。写清看哪几场比赛、和谁一起、看球时吃什么，并写一句关于油价减税或护理的话。",
     "Escreva em alemão, 80–100 palavras: «Minha semana de futebol». Diga quais jogos você assiste, com quem e o que você come durante o jogo — e acrescente uma frase sobre o desconto no combustível ou os cuidados. Os melhores textos serão publicados no VOL.3 (página 7, «Cartas dos leitores»)."),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · Texto-modelo (84 palavras)"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)"),
]
rep_all("content8.py", C8)
# ---------- generic value maps (bare text) ----------
TYPEMAP = [("完成句子", "Completar frases"), ("单选", "Escolha múltipla"),
           ("句型转换", "Transformação de frases"), ("词汇配对", "Correspondência de palavras"),
           ("判断对错", "Verdadeiro ou falso"), ("完形填空", "Completar o texto"),
           ("造句", "Construir frases"), ("对话补全", "Completar o diálogo"),
           ("翻译", "Tradução"), ("写作", "Escrita")]
INSTRMAP = [('instr="填空"', 'instr="Complete"'),
            ('instr="改写"', 'instr="Reescreva"'),
            ('instr="判断"', 'instr="V ou F"'),
            ('instr="造句"', 'instr="Monte a frase"'),
            ('instr="翻译"', 'instr="Traduza para o português"'),
            ('instr="把词和释义配对"', 'instr="Associe as palavras"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:  # instr tokens first: TYPEMAP would corrupt instr="翻译"
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)
# P8 section E: first three are DE->PT (already Traduza para o português
# via the generic map); the fourth is reader->DE, fix its instr + prompt.
# (handled in the content8-specific block below)

# E item 140: prompt becomes Portuguese, instr becomes Traduza para o alemão.
# The generic INSTRMAP already turned instr="翻译" into Traduza para o
# português everywhere; fix ONLY the 140 line (unique prompt literal).
rep("content8.py", '"我周日多睡一小时。（译成德语）", instr="Traduza para o português"',
    '"Durmo uma hora a mais no domingo.", instr="Traduza para o alemão"', 1)
# P8 keys: W43 DE x PT shipped form — half-width parens, 13pt keys,
# Portuguese page separators.
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)', 1)

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
