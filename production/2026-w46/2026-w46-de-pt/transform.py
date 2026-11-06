# -*- coding: utf-8 -*-
"""DE x PT fan-out transform for W46 DE core build copy.
Generated from the EN pair table + tr-pt.py. German body text is
NEVER touched: every `old` is a Chinese explanation-layer string,
a bilingual furniture string, or a generic type/instr token.
Run once from the build dir copy."""
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
        assert n >= 1, f"{fname}: {old!r} not found"
    LOG.append(f"{fname}: {n}x {old[:60]!r} -> {new[:60]!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))

def rep_all(fname, pairs):
    seen = set()
    for old, new in pairs:
        assert old not in seen, f"duplicate old in {fname}: {old!r}"
        seen.add(old)
    for old, new in sorted(pairs, key=lambda t: -len(t[0])):
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-pt", 1)

# ---------- svglib docstring comment only (not rendered) ----------
pth = os.path.join(BASE, "svglib.py")
s = open(pth, encoding="utf-8").read()
if "for \u91cd\u9633." in s:
    rep("svglib.py", "for \u91cd\u9633.", "for Double Ninth.", 1)
else:
    LOG.append("svglib.py: no Double Ninth comment (already adapted), skipped")

# ---------- bslib4: furniture + gloss prefix ----------
rep("bslib4.py",
    '"Die Lucerna · \u5fb7\u8bed\u5468\u62a5 VOL.3 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · SEMANÁRIO ALEMÃO VOL.3 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS"', 1)
rep("bslib4.py", 'f"\u7b2c {n} \u7248 / \u5171 {total} \u7248"', 'f"Página {n} de {total}"', 1)
rep("bslib4.py", '"\u8bd1\u6ce8\uff5c" + s', '"Nota — " + s', 1)

# ================= content12.py =================
C12 = [
    ('WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语', 'WÖCHENTLICH AUF DEUTSCH · TODA SEMANA · O ALEMÃO QUE OS ALEMÃES LEEM'),
    ('德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL', 'SEMANÁRIO ALEMÃO · VOL.3 · SELEÇÃO · SÃO MARTINHO · NFL'),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")', 'p.text(975, 372, "TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 20, "sans", True, BRICK, anchor="middle")'),
    ('本周国家队周 · 圣马丁节与 NFL', 'SEMANA DA SELEÇÃO · SÃO MARTINHO E NFL'),
    ('详见第 4 版 · Seite 4', 'Ver página 4'),
    ('DIE TOPMELDUNG · 头条', 'DIE TOPMELDUNG · Manchete'),
    ('讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。', 'Notas — die Länderspielpause = pausa das seleções · das Viertelfinale = quartos de final · ausverkauft = esgotado.'),
    ('DIE WOCHE IN ZAHLEN · 数字看本周', 'DIE WOCHE IN ZAHLEN · Números'),
    ('5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）', '5 — Punkte hat Deutschland nach vier Spielen in der Nations League (a Alemanha tem 5 pontos após quatro jogos)'),
    ('11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）', '11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (a sessão de carnaval começa às 11.11)'),
    ('15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）', '15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (o jogo da NFL começa domingo às 15.30)'),
    ('JETZT ÜBEN · 即学即练', 'JETZT ÜBEN · Agora pratica'),
    ('国家队比赛周', 'semana de pausa das seleções'),
    ('塞尔维亚首都', 'capital da Sérvia'),
    ('狂欢季 11 点 11 分开幕', 'o carnaval começa às 11.11'),
    ('NFL 在慕尼黑', 'a NFL em Munique'),
    ('四轮 5 分', '5 pontos após quatro jogos'),
    ('周日是纪念日', 'domingo é o dia de recordação'),
    ('圣马丁节 11 月 11 日', 'São Martinho é a 11 de novembro'),
    ('11 月 11 日是星期三', '11 de novembro é quarta-feira'),
    ('本周大问题 · Die Fragen der Woche', 'Grandes perguntas · Die Fragen der Woche'),
    ('德国本周最热议的五个问题。', 'As cinco perguntas que agitam a Alemanha.'),
    ('IN DIESER AUSGABE · 本期目录', 'IN DIESER AUSGABE · Sumário'),
    ('空场比赛（无观众）。详见第 4 版。', 'Um jogo sem espectadores. Ver página 4.'),
    ('KURZ & GUT · 快讯', 'KURZ & GUT · Em resumo'),
    ('BLITZQUIZ · 闪电问答', 'BLITZQUIZ · Quiz relâmpago'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lê a primeira página e escolhe a resposta certa · Respostas na página 8'),
    ('周五客战塞尔维亚', 'fora, na Sérvia, na sexta-feira'),
    ('NFL 下午 3 点半开球', 'a NFL começa às 15.30'),
    ('纪念日在周日', 'o dia de recordação é domingo'),
    ('LEBEN · 生活', 'LEBEN · A vida'),
    ('LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活', 'LEVEL A2 · Der 11. November & der Alltag · 11 de novembro e o dia a dia'),
    ('der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。', 'der Jeck = folião do carnaval (dialeto de Colónia) · die fünfte Jahreszeit = a quinta estação (carnaval) · die Laterne = lanterna · der Weckmann = boneco de pão · die Martinsgans = ganso de São Martinho.'),
    ('DER 11. NOVEMBER · 11 月 11 日', 'DER 11. NOVEMBER'),
    ('你过狂欢节还是圣马丁节？写两句德语寄来。', 'Carnaval ou São Martinho? Escreve duas frases em alemão!'),
    ('UND SIE? · 说说你自己', 'UND SIE? · E tu?'),
    ('MARTIN IN KÜRZE · 圣马丁简讯', 'MARTIN IN KÜRZE · Em breve'),
    ('RECHNEN WIR MAL · 算一算', 'RECHNEN WIR MAL · Vamos calcular'),
    ('Die Uhrzeiten der Woche · 本周时刻', 'Die Uhrzeiten der Woche · As horas da semana'),
    ('注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。', 'Nota: 11 de novembro é dia útil. Chega cedo a Colónia: a cidade velha está cheia e à noite as ruas são das crianças com as suas lanternas.'),
    ('ÜBUNGEN · 第 2 版练习', 'ÜBUNGEN · Exercícios página 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respostas na página 8 · Os níveis misturam-se: encontra cada resposta pelo seu número'),
    ('看第 2 版文章，用时间填空。', 'Lê o artigo da página 2 e completa as horas.'),
    ('WDR 10 点半直播', 'a WDR em direto desde as 10.30'),
    ('Weckmann 是面人面包', 'um Weckmann é um boneco de pão'),
    ('11 月 11 日不是法定假日', '11 de novembro não é feriado'),
    ('圣马丁鹅配红甘蓝和丸子', 'o ganso de São Martinho com couve roxa e bolinhos'),
    ('改成 Perfekt 现在完成时。', 'Reescreve no Perfekt (pretérito perfeito).'),
    ('读第 2 版文章，选出正确答案。', 'Lê o artigo da página 2 e escolhe a resposta certa.'),
    ('Jeck=狂欢者 c', 'Jeck=folião do carnaval c'),
    ('Laterne=灯笼 a', 'Laterne=lanterna a'),
    ('Weckmann=面人面包 b', 'Weckmann=boneco de pão b'),
    ('Martinsgans=圣马丁鹅 d', 'Martinsgans=ganso de São Martinho d'),
]
rep_all("content12.py", C12)

# ================= content34.py =================
C34 = [
    ('KULTUR · 文化', 'KULTUR · Cultura'),
    ('A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾', 'A2 → B1 · St. Martin, Karneval & Rückblick · São Martinho, carnaval e um olhar atrás'),
    ('der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。', 'der Bettler = mendigo · der Mantel = manto · das Geschnatter = grasnido · der Gänsestall = estábulo dos gansos · das Dreigestirn = triunvirato do carnaval.'),
    ('ST. MARTIN · 圣马丁', 'ST. MARTIN · São Martinho'),
    ('die Laterne — 灯笼', 'die Laterne — lanterna'),
    ('der Mantel — 斗篷', 'der Mantel — manto'),
    ('die Gans — 鹅', 'die Gans — ganso'),
    ('der Weckmann — 面人面包', 'der Weckmann — boneco de pão'),
    ('das Martinsfeuer — 圣马丁篝火', 'das Martinsfeuer — fogueira de São Martinho'),
    ('das Kostüm — 服装', 'das Kostüm — fato'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · São Martinho'),
    ('UND SIE? · 说说你自己', 'UND SIE? · E tu?'),
    ('你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。', 'Fizeste uma lanterna? Escreve duas frases em alemão!'),
    ('DER TIPP · 编辑部建议', 'DER TIPP · Conselho'),
    ('ÜBUNGEN · 第 3 版练习', 'ÜBUNGEN · Exercícios página 3'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respostas na página 8 · Os níveis misturam-se: encontra cada resposta pelo seu número'),
    ('读第 3 版文章，判断对错。', 'Lê o artigo da página 3. Verdadeiro ou falso?'),
    ('传说马丁是罗马士兵', 'a lenda diz que Martinho era soldado romano'),
    ('传说鹅叫声暴露了他', 'a lenda diz que os gansos o denunciaram'),
    ('纪念日 11 月 11 日', 'o dia de recordação é 11 de novembro'),
    ('截稿时 11 月 3–8 日结果未知', 'resultados de 3 a 8 de novembro desconhecidos no fecho'),
    ('狂欢季 11 点 11 分开幕', 'o carnaval começa às 11.11'),
    ('用方框里的词填空。', 'Completa com as palavras do quadro.'),
    ('斗篷分给乞丐', 'o manto partilhado com o mendigo'),
    ('纸灯笼', 'uma lanterna de papel'),
    ('圣马丁鹅', 'o ganso de São Martinho'),
    ('圣马丁鹅配红甘蓝和丸子', 'o ganso de São Martinho com couve roxa e bolinhos'),
    ('狂欢节服装', 'um fato de carnaval'),
    ('游行在篝火处结束', 'a procissão termina na fogueira'),
    ('选出正确答案。', 'Escolhe a resposta certa.'),
    ('马丁后来成为图尔主教', 'Martinho tornou-se depois bispo de Tours'),
    ('灯笼游行常在前后晚上举行', 'as procissões de lanternas são muitas vezes nas noites vizinhas'),
    ('VOL.4 报道 11 月 3–8 日结果', 'VOL.4 contará os resultados de 3 a 8 de novembro'),
    ('把词组成正确的句子。', 'Põe as palavras numa frase correta.'),
    ('主谓宾顺序', 'ordem sujeito–verbo–objeto'),
    ('时间状语开头，动词第二位', 'o tempo primeiro, o verbo em segundo'),
    ('地点开头，动词第二位', 'o lugar primeiro, o verbo em segundo'),
    ('SPORT · 体育', 'SPORT · Desporto'),
    ('LEVEL B1 · Nationalelf & NFL · 国家队与 NFL', 'LEVEL B1 · Nationalelf & NFL · Seleção e NFL'),
    ('das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。', 'das Geisterspiel = jogo fantasma · das Hinspiel = jogo da primeira mão · ausverkauft = esgotado · der Star = estrela · gewinnen = ganhar.'),
    ('你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。', 'Futebol ou futebol americano? Quem ganha? Duas frases!'),
    ('DER SPIELPLAN · 本周与下周赛程', 'DER SPIELPLAN · Esta semana e a próxima'),
    ('ÜBUNGEN · 第 4 版练习', 'ÜBUNGEN · Exercícios página 4'),
    ('读第 4 版文章，选出正确答案。', 'Lê o artigo da página 4 e escolhe a resposta certa.'),
    ('德国 5 分，荷兰希腊各 8 分', 'Alemanha 5 pontos, Países Baixos e Grécia 8 cada'),
    ('主教练 11 月 5 日公布名单', 'o selecionador anuncia a lista a 5 de novembro'),
    ('贝尔格莱德空场', 'estádio vazio em Belgrado'),
    ('首回合德国 2:0 胜塞尔维亚', 'a Alemanha ganhou a primeira mão 2-0 contra a Sérvia'),
    ('NFL 慕尼黑赛售罄', 'o jogo da NFL em Munique está esgotado'),
    ('Geisterspiel=空场比赛 b', 'Geisterspiel=jogo fantasma b'),
    ('Hinspiel=首回合 a', 'Hinspiel=jogo da primeira mão a'),
    ('Ausrüster=装备赞助商 c', 'Ausrüster=fornecedor de equipamento c'),
    ('ausverkauft=售罄 d', 'ausverkauft=esgotado d'),
    ('用比较级完成句子（括号里是原级）。', 'Completa com o comparativo (a palavra entre parênteses está no positivo).'),
    ('viel → mehr（荷兰 8 分多于德国 5 分）', 'viel → mehr (os Países Baixos têm 8 pontos, mais do que os 5 da Alemanha)'),
    ('spät → später（15:30 晚于 11:11）', 'spät → später (15.30 é mais tarde do que 11.11)'),
    ('leise → leiser（空场比主场安静）', 'leise → leiser (um estádio vazio é mais silencioso do que um jogo em casa)'),
    ('früh → früher（11 月 5 日早于 11 月 13 日）', 'früh → früher (5 de novembro é mais cedo do que 13 de novembro)'),
    ('看上面的赛程表，选出正确答案。', 'Olha para o calendário acima e escolhe a resposta certa.'),
    ('塞尔维亚–德国周五 20:45', 'Sérvia–Alemanha sexta-feira às 20.45'),
    ('NFL 周日 15:30', 'NFL domingo às 15.30'),
    ('德国–荷兰周一 20:45', 'Alemanha–Países Baixos segunda-feira às 20.45'),
    ('拜仁–科隆周五 20:30', 'Bayern–Colónia sexta-feira às 20.30'),
    ('沙尔克–斯图加特周六 17:30', 'Schalke–Estugarda sábado às 17.30'),
]
rep_all("content34.py", C34)

# ================= content56.py =================
C56 = [
    ('JUGEND · 青年', 'JUGEND · Juventude'),
    ('LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校', 'LEVEL B1 · Laternen, Lieder & Schule · Lanternas, canções e escola'),
    ('basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。', 'basteln = fazer, construir · der Pausenhof = recreio · sich verkleiden = disfarçar-se · die Stimmung = ambiente · der Pirat = pirata.'),
    ('SCHULWOCHE · 开学周', 'SCHULWOCHE · Volta à escola'),
    ('die Laterne — 灯笼', 'die Laterne — lanterna'),
    ('basteln — 制作', 'basteln — construir'),
    ('das Lied — 歌曲', 'das Lied — canção'),
    ('das Kostüm — 服装', 'das Kostüm — fato'),
    ('der Umzug — 游行', 'der Umzug — procissão'),
    ('der Stern — 星星', 'der Stern — estrela'),
    ('MARTINSWÖRTER · 圣马丁词汇', 'MARTINSWÖRTER · São Martinho'),
    ('UND SIE? · 说说你自己', 'UND SIE? · E tu?'),
    ('你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。', 'Uma lanterna em criança? A tua canção? Duas frases!'),
    ('DER WOCHENPLAN DER REDAKTION · 编辑部一周计划', 'DER WOCHENPLAN DER REDAKTION · A semana da redação'),
    ('ÜBUNGEN · 第 5 版练习', 'ÜBUNGEN · Exercícios página 5'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respostas na página 8 · Os níveis misturam-se: encontra cada resposta pelo seu número'),
    ('读第 5 版文章，选出正确答案。', 'Lê o artigo da página 5 e escolhe a resposta certa.'),
    ('11 月 9 日全德复课', 'a escola recomeça em todo o lado a 9 de novembro'),
    ('孩子们做纸灯笼', 'as crianças fazem lanternas de papel'),
    ('纸灯笼', 'uma lanterna de papel'),
    ('上午狂欢，下午圣马丁', 'carnaval de manhã, São Martinho à tarde'),
    ('NFL 周日在电视上', 'a NFL na TV domingo'),
    ('周五看国家队比赛', 'ver a seleção na sexta-feira'),
    ('用方框里的词填空。', 'Completa com as palavras do quadro.'),
    ('做灯笼', 'fazer lanternas'),
    ('唱圣马丁歌曲', 'cantar canções de São Martinho'),
    ('狂欢节服装', 'um fato de carnaval'),
    ('灯笼游行', 'uma procissão de lanternas'),
    ('灯笼上的星星', 'a estrela na lanterna'),
    ('用 weil 连接两个句子（动词放句末）。', 'Junta as duas frases com weil (o verbo vai para o fim).'),
    ('weil 句动词置尾', 'numa oração com weil o verbo vai para o fim'),
    ('ist 置尾', 'ist vai para o fim'),
    ('will 置尾', 'will vai para o fim'),
    ('beginnt 置尾', 'beginnt vai para o fim'),
    ('判断对错。', 'Verdadeiro ou falso?'),
    ('11 月 9 日巴伐利亚也复课', 'a Baviera também volta a 9 de novembro'),
    ('灯笼游行在晚上', 'a procissão de lanternas é à noite'),
    ('孩子们唱圣马丁歌曲', 'as crianças cantam canções de São Martinho'),
    ('VERTIEFUNG · 深读', 'VERTIEFUNG · Aprofundamento'),
    ('LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税', 'LEVEL B2 · Volkstrauertag & Stromsteuer · Dia de recordação e imposto sobre a eletricidade'),
    ('gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。', 'gedenken = comemorar · Kranzniederlegung = coroa · stille Tag = dia de silêncio · Verbundenheit = vínculo · Versöhnung = reconciliação.'),
    ('DIE ZAHLEN · 本周数字', 'DIE ZAHLEN · Os números'),
    ('纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。', 'Dia de recordação: recordar pede silêncio — quase todos concordam. Imposto sobre a eletricidade: quanto desce ainda está em aberto. Ambos afetam quase todas as famílias.'),
    ('ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日', 'ZWEI SONNTAGE IM NOVEMBER · Dois domingos de novembro'),
    ('WAS INTERESSIERT DIE LESER? · 读者最关心什么？', 'WAS INTERESSIERT DIE LESER? · O que interessa aos leitores?'),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "futebol")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "festas")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "memória")'),
    ('ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）', 'ÜBUNGSDATEN · Dados de exercício — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Dados de exercício, não um inquérito real.)'),
    ('ÜBUNGEN · 第 6 版练习', 'ÜBUNGEN · Exercícios página 6'),
    ('看上面的练习图表，选出正确答案。', 'Usa o gráfico de exercício acima.'),
    ('46% 足球最受关注', 'o futebol lidera com 46%'),
    ('节日 34% 第二', 'as festas em segundo com 34%'),
    ('纪念 20% 最小', 'a recordação a menor com 20%'),
    ('纪念 20%', 'a recordação 20%'),
    ('读第 6 版深读文章，选出正确答案。', 'Lê o artigo da página 6.'),
    ('11 月 15 日纪念日', 'o dia de recordação é 15 de novembro'),
    ('ZDF 13 点半直播纪念仪式', 'a ZDF em direto desde as 13.30'),
    ('家庭电力税 2.05 欧分', 'o imposto das famílias é de 2,05 cêntimos'),
    ('2027 年预算 11 月 27 日表决', 'votação do orçamento de 2027 a 27 de novembro'),
    ('用括号里的形式填空。', 'Completa com a forma entre parênteses.'),
    ('被动：wird + Partizip II', 'passiva: wird + particípio passado'),
    ('ob 引导间接疑问句', 'ob introduz uma pergunta indireta'),
    ('献花圈仪式', 'uma cerimónia de deposição de coroas'),
    ('为和平与和解', 'pela paz e a reconciliação'),
    ('德奥联系', 'a ligação alemã-austríaca'),
    ('纪念受害者', 'recordar as vítimas'),
]
rep_all("content56.py", C56)

# ================= content7.py =================
C7 = [
    ('SPRACHE · 语言', 'SPRACHE · A língua'),
    ('A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所', 'A2 → B2 · Sätze der Woche & Fehlerklinik · Frases da semana e clínica de erros'),
    ('本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。', 'Esta página é só língua: três lições curtas, as frases da semana (citadas palavra por palavra dos artigos deste número), a clínica de erros e as cartas dos leitores.'),
    ('BEISPIELE · 例句', 'BEISPIELE · Exemplos'),
    ('被动：wird + Partizip II', 'passiva: wird + particípio passado'),
    ('复数：werden', 'plural: werden'),
    ('werden + 原形表将来', 'werden + infinitivo para o futuro'),
    ('被动语态', 'voz passiva'),
    ('lang → länger（夜晚比白天长）', 'lang → länger (a noite é mais longa do que o dia)'),
    ('weil 引导原因', 'weil introduz uma causa'),
    ('weil 句动词置尾', 'numa oração com weil o verbo vai para o fim'),
    ('länger als = 比……更长', 'länger als = mais longo do que'),
    ('„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短', '„Länger als sonst“ significa... A. mais longo do que o habitual · B. o mesmo do que o habitual · C. mais curto do que o habitual'),
    ('ob 引导间接疑问', 'ob introduz uma pergunta indireta'),
    ('Es ist fraglich, ob ... = 是否还难说', 'Es ist fraglich, ob ... = é duvidoso se ...'),
    ('dass 句动词置尾', 'numa oração com dass o verbo vai para o fim'),
    ('礼貌表达观点', 'uma forma educada de dar uma opinião'),
    ('11.11 Uhr = 11 点 11 分', '11.11 Uhr = 11.11'),
    ('vor leeren Rängen = 空场，没有观众', 'vor leeren Rängen = estádio vazio'),
    ('Es wird gespielt. = 比赛将进行（被动）', 'Es wird gespielt. = Vai ser jogado'),
    ('Meiner Meinung nach ... = 在我看来……', 'Meiner Meinung nach = na minha opinião'),
    ('Ich finde, dass ... = 我觉得……', 'Ich finde, dass = acho que'),
    ('Es ist fraglich, ob ... = 是否……还难说', 'Es ist fraglich, ob ... = é duvidoso que'),
    ('DER WERKZEUGKASTEN · 工具箱', 'DER WERKZEUGKASTEN'),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "Um exemplo da redação!"'),
    ('编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。', 'Exemplo da redação, não uma carta real: nenhuma carta real tinha chegado até ao fecho. Enviem-nos as vossas para VOL.4!'),
    ('LESERBRIEFE · 读者来信', 'LESERBRIEFE · Cartas'),
    ('NOCH EIN WORT · 再学一词', 'NOCH EIN WORT · Mais uma palavra'),
    ('«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。', '«das Geisterspiel» (Seite 4) : ein Spiel ohne Zuschauer im Stadion. Jogo fantasma: um jogo sem espectadores.'),
    ('SÄTZE DER WOCHE · 本周金句', 'SÄTZE DER WOCHE · Frases da semana'),
    ('原文摘录，逐字引自本期文章 · 括号内为出处', 'Citado palavra por palavra dos artigos deste número · fonte entre parênteses'),
    ('德甲休战——但国家队要比赛。', 'A Bundesliga pausa — mas a seleção joga.'),
    ('11 点 11 分，科隆新一季狂欢季开幕。', 'Às 11.11 começa em Colónia a nova sessão de carnaval.'),
    ('他的纪念日是 11 月 11 日。', 'O seu dia de recordação é 11 de novembro.'),
    ('书包收拾好了，操场上又热闹起来。', 'As mochilas estão prontas, os recreios voltam a ser barulhentos.'),
    ('十一月黑暗，但并不安静：它歌唱、发光、庆祝。', 'Novembro é escuro, mas não silencioso: canta, brilha e festeja.'),
    ('比赛售罄，RTL 现场直播。', 'O jogo está esgotado; a RTL transmite em direto.'),
    ('这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。', 'Aqui, recordar significa: parar, lembrar — e defender a paz e a reconciliação.'),
    ('周日，全国一片安静。', 'Domingo o país está silencioso.'),
    ('FEHLERKLINIK · 纠错诊所', 'FEHLERKLINIK · A clínica de erros'),
    ('学习者最常犯的四个错 · 先自己改，再看答案', 'Quatro erros frequentes dos alunos · corrige-os primeiro, depois verifica'),
    ('动词第二位：主语不在句首时，动词仍居第二。', 'Verbo em segundo lugar: mesmo quando o sujeito não é o primeiro, o verbo fica em segundo.'),
    ('halb zwölf = 十一点半（zwölf 之前）。', 'halb zwölf = 11.30, meia hora antes de zwölf.'),
    ('Perfekt 中 Partizip II 放句末。', 'No Perfekt o particípio passado vai para o fim.'),
    ('ob 从句动词放句末。', 'Numa oração com ob o verbo vai para o fim.'),
    ('IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)', 'IN DER NÄCHSTEN AUSGABE · Próximo número (VOL.4)'),
]
rep_all("content7.py", C7)

# ================= content8.py =================
C8 = [
    ('ÜBUNGEN & ANTWORTEN · 练习与答案', 'ÜBUNGEN & ANTWORTEN · Exercícios e respostas'),
    ('SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方', 'SCHLUSSTEST · Teste final · Alle Antworten unten auf dieser Seite — todas as respostas no fim desta página'),
    ('beginnt（第三人称单数）', 'beginnt (3.ª pessoa do singular)'),
    ('bastelt（第三人称单数）', 'bastelt (3.ª pessoa do singular)'),
    ('geht（第三人称单数）', 'geht (3.ª pessoa do singular)'),
    ('singt（第三人称单数）', 'singt (3.ª pessoa do singular)'),
    ('schaut（第三人称单数）', 'schaut (3.ª pessoa do singular)'),
    ('sieht（第三人称单数）', 'sieht (3.ª pessoa do singular)'),
    ('erzählt（第三人称单数）', 'erzählt (3.ª pessoa do singular)'),
    ('A · LÜCKENTEXT · 完形填空', 'A · LÜCKENTEXT · Lacunas'),
    ('选项：', 'Opções:'),
    ('B · WISSENSFRAGEN · 综合问答', 'B · WISSENSFRAGEN · Quiz'),
    ('狂欢季 11 点 11 分开幕', 'o carnaval começa às 11.11'),
    ('周五客战塞尔维亚', 'fora, na Sérvia, na sexta-feira'),
    ('NFL 周日 15:30', 'NFL domingo às 15.30'),
    ('纪念日 11 月 15 日', 'o dia de recordação é 15 de novembro'),
    ('家庭电力税 2.05 欧分', 'o imposto das famílias é de 2,05 cêntimos'),
    ('主教练 11 月 5 日公布名单', 'o selecionador anuncia a lista a 5 de novembro'),
    ('ZDF 13 点半直播纪念仪式', 'a ZDF em direto desde as 13.30'),
    ('亡灵主日 11 月 22 日', 'Totensonntag é 22 de novembro'),
    ('C · LESEVERSTEHEN · 阅读理解', 'C · LESEVERSTEHEN · Leitura'),
    ('周三做灯笼', 'fazer uma lanterna na quarta-feira'),
    ('周五看德国队', 'ver a Alemanha na sexta-feira'),
    ('D · SÄTZE BAUEN · 造句', 'D · SÄTZE BAUEN · Frases'),
    ('时间状语，动词第二位', 'o tempo, o verbo em segundo'),
    ('主谓宾顺序', 'ordem sujeito–verbo–objeto'),
    ('时间状语开头，动词第二位', 'o tempo primeiro, o verbo em segundo'),
    ('地点时间开头，动词第二位', 'lugar e tempo primeiro, verbo em segundo'),
    ('E · ÜBERSETZEN · 翻译', 'E · ÜBERSETZEN · Tradução'),
    ('狂欢节 11 点 11 分在科隆开幕。', 'O carnaval começa às 11.11 em Colónia.'),
    ('beginnen = 开始', 'beginnen = começar'),
    ('Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）', 'Der Karneval beginnt um 11.11 Uhr in Köln. (traduz para português)'),
    ('我周三做一个灯笼。', 'Faço uma lanterna na quarta-feira.'),
    ('basteln = 制作', 'basteln = fazer, construir'),
    ('Ich bastle am Mittwoch eine Laterne.（译成中文）', 'Ich bastle am Mittwoch eine Laterne. (traduz para português)'),
    ('学校 11 月 9 日又开学了。', 'A escola recomeçou a 9 de novembro.'),
    ('wieder begonnen = 又开始', 'wieder begonnen = recomeçado'),
    ('Die Schule hat am 9. November wieder begonnen.（译成中文）', 'Die Schule hat am 9. November wieder begonnen. (traduz para português)'),
    ('看比赛 = das Spiel schauen', 'ver um jogo = das Spiel schauen'),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"', '"Vejo o jogo da NFL no domingo. (traduz para alemão)", instr="Traduza para o alemão"'),
    ('F · WÖRTER PAAREN · 词汇配对', 'F · WÖRTER PAAREN · Pares'),
    ('Mantel=斗篷 b', 'Mantel=manto b'),
    ('Laterne=灯笼 a', 'Laterne=lanterna a'),
    ('Geisterspiel=空场比赛 d', 'Geisterspiel=jogo fantasma d'),
    ('Versöhnung=和解 c', 'Versöhnung=reconciliação c'),
    ('singst（第二人称单数）', 'singst (2.ª pessoa do singular)'),
    ('macht（第二人称复数）', 'macht (2.ª pessoa do plural)'),
    ('essen（第一人称复数）', 'essen (1.ª pessoa do plural)'),
    ('machst（第二人称单数）', 'machst (2.ª pessoa do singular)'),
    ('schaue（第一人称单数）', 'schaue (1.ª pessoa do singular)'),
    ('G · DIALOG · 对话补全', 'G · DIALOG · Completar o diálogo'),
    ('开放题 — 要点见写作框，范文在第 8 版写作框内', 'Tarefa aberta — segue os pontos do quadro de escrita; o texto-modelo está no quadro desta página'),
    ('按要点给分', 'Avaliado segundo os pontos indicados'),
    ('H · SCHREIBEN · 写作', 'H · SCHREIBEN · Escrita'),
    ('用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。', 'Escreve em alemão, 80–100 palavras: «A minha semana de novembro». Diz o que fazes, que jogos vês e com quem — e acrescenta uma frase sobre o dia de São Martinho ou o dia de recordação.'),
    ('MUSTER · 范文（84 Wörter）', 'MUSTER · Texto-modelo (84 palavras)'),
    ('ANTWORTEN · 全部答案与简析（第 1–8 版）', 'ANTWORTEN · Todas as respostas com notas (páginas 1–8)'),
]
rep_all("content8.py", C8)

# ---------- P8 keys ----------
rep("content8.py", 'kf.para(f"— \u7b2c {pg} \u7248 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"\uff08{e[\'note\']}\uff09"',
    's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)', 1)

# ---------- generic value maps ----------
TYPEMAP = [('完成句子', 'Completar frases'), ('单选', 'Escolha múltipla'), ('句型转换', 'Transformação de frases'), ('词汇配对', 'Correspondência de palavras'), ('判断对错', 'Verdadeiro ou falso'), ('完形填空', 'Completar o texto'), ('造句', 'Construir frases'), ('对话补全', 'Completar o diálogo'), ('翻译', 'Tradução'), ('写作', 'Escrita')]
INSTRMAP = [('instr="填空"', 'instr="Complete"'), ('instr="改写"', 'instr="Reescreva"'), ('instr="判断"', 'instr="V ou F"'), ('instr="造句"', 'instr="Monte a frase"'), ('instr="翻译"', 'instr="Traduza para o português"'), ('instr="把词和释义配对"', 'instr="Associe as palavras"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)

# ---------- leak check: no original Chinese literal may remain ----------
import re
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
leaks = {}
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    for i, line in enumerate(open(os.path.join(BASE, f), encoding="utf-8"), 1):
        if CJK.search(line):
            leaks.setdefault(f, []).append((i, line.strip()[:80]))
print("CJK leaks:", leaks if leaks else "NONE")
assert not leaks, "CJK strings remain after transform"

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
