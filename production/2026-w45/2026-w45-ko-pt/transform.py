# -*- coding: utf-8 -*-
"""W45 KO core -> KO x PT fan-out transform (assertion-checked literal replacements).

Method (tools/README #17/#18, W45 KO x DE precedent):
- Every round regenerates the build files from orig/ (pristine core copies),
  repoints OUT/BASE to the PT edition dir, then applies ALL pairs below.
  Fixes therefore only ever enter this file; re-running it + run.py +
  render.py reproduces the edition from scratch.
- Line-based / exact-literal splicing only, never AST byte offsets.
- Registry `type` arguments stay byte-identical (internal keys); only
  rendered strings (instr, notes, heads, boxes, gloss, band lines) change.
- P8 answer-generation code is NOT touched (dash family, Korean
  "— 제N면 —" group headings as shipped in W43 ko-pt).
- P1 masthead follows the W43 ko-pt shipped geometry exactly (measured
  from files/weekly-report-ko-pt/svg/p1-pyoji.svg, NOT from ko-en/ko-de):
  subtitle 372 -> 366, badge INSERTED at y=394, 20pt weight-700 BRICK
  #a4553a, rules +20, dark band +9; everything below y=606 unmoved
  (tools/README #20 KO case).
- P7 target-language definition prose stays Korean verbatim; only the
  explanation layer (glosslines, clinic notes, frame note, letters notes,
  phrase translations) becomes Portuguese. The P7 readers' letter itself is
  frozen verbatim; the disclosure apparatus (short note + Korean
  disclosure + Chinese disclosure) is replaced by Portuguese blocks
  carrying the same facts plus an explicit imperative solicitation
  (letters AND best P8 texts).
- Korean instruction glosslines on P2-P6/P8 (reader-language apparatus)
  become Portuguese, per the W43 ko-pt / KO x DE precedent.
Run (from this dir): tools/venv/bin/python transform.py
Then: tools/venv/bin/python run.py && tools/venv/bin/python render.py
"""
import os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ED_DIR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-pt")
CORE_ED = "weekly-report-w45-ko-core"
NEW_ED = "weekly-report-w45-ko-pt"

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

    apply_pairs("bslib4.py", [
        ('"Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY"',
         '"Lucerna · SEMANÁRIO COREANO VOL.2 · TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS"'),
        ('f"제 {n} 면 / 총 {total} 면"', 'f"Página {n} de {total}"'),
        ('"译注｜" + s', '"Nota — " + s'),
    ])

    # ---- P1 masthead geometry (W43 ko-pt shipped values) ----
    apply_pairs("content12.py", [
        ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
         'p.text(975, 394, "TEXTOS EM COREANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 20, "sans", True, BRICK, anchor="middle")'),
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
         '"매주 한국어로 · Toda semana · 한국 사람이 읽는 한국어를 읽어요"'),
        ('"立冬"', '"IPDONG"'),
        ('"立冬在 11 月 7 日周六 · 泡菜季开始"',
         '"Ipdong no sábado, 7 de novembro · Começa o kimjang"'),
        ('"톱 뉴스 · 头条"', '"톱 뉴스 · Manchete"'),
        ('"입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。"',
         '"입동 = Ipdong · 절정 = auge · 김장 = kimchi de inverno · 상륙하다 = chegar à costa · 온대저기압 = ciclone extratropical."'),
        ('"숫자로 보는 이번 주 · 数字看本周"', '"숫자로 보는 이번 주 · Em números"'),
        ('"지금 바로 연습 · 即学即练"', '"지금 바로 연습 · Pratique já"'),
        ('"这五个日期，是本期报纸的骨架。"',
         # 1 line at 18.5pt/390px: the 2-line form overprinted the fixed
         # source line at gy+636 in the DE build (round-3 NEW TEXTX flag).
         '"Estas cinco datas sustentam a edição."'),
        ('"이번 호의 내용 · 本期目录"', '"이번 호의 내용 · Índice"'),
        ('"全部"', '"Todos"'),
        ('"이번 주의 말 · 本周词语"', '"이번 주의 말 · A palavra da semana"'),
        ('"입동 ＝ 立冬、冬季开始的节气。"', '"입동 = Ipdong, o início do inverno."'),
        ('"짧은 소식 · 快讯"', '"짧은 소식 · Em resumo"'),
        ('"퀴즈 · 闪电问答"', '"퀴즈 · Quiz relâmpago"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Leia a primeira página e escolha a resposta certa · Respostas na pág. 8"'),
        # P2 band + furniture
        ('"생활 · 生活"', '"생활 · Vida cotidiana"'),
        ('"레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季与过冬准备、韩史考试报名"',
         '"레벨 A2 · 김장과 겨울 준비, 한능검 · Kimjang, preparação para o inverno e exame de história"'),
        ('"절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。"',
         '"절이다 = salgar · 버무리다 = misturar · 난방 = aquecimento · 식탁 = mesa."'),
        ('"산불 山火 · 벌금 罚款 · 불씨 火星。"',
         '"산불 = incêndio florestal · 벌금 = multa · 불씨 = faísca."'),
        ('"한능검 접수 · 韩史考试报名"', '"한능검 접수 · Inscrições"'),
        ('"아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。"',
         '"아삭하다 = crocante · 김 = vapor · 깊어지다 = aprofundar-se."'),
        ('"물려주다 传给 · 낡다 旧 · 두렵다 害怕。"',
         '"물려주다 = passar adiante · 낡다 = velho · 두렵다 = ter medo."'),
        ('"겨울 준비 목록 · 过冬清单"', '"겨울 준비 목록 · Lista"'),
        ('"묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。"',
         '"묵직하다 = pesado · 앞치마 = avental · 목록 = lista."'),
        ('"你呢？为过冬做的第一件事是什么？写两句韩语寄来。"',
         '"E você? Qual é a primeira coisa que você faz para o inverno? Escreva duas frases em coreano e envie."'),
        ('"당신은? · 说说你自己"', '"당신은? · E você?"'),
        ('"날짜 세는 말 · 数日子的说法"', '"날짜 세는 말 · Contando os dias"'),
        ('"수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒计时数日子的四个说法"',
         '"수능까지 남은 날로 날짜를 세는 네 가지 말 · Quatro formas de contar com a contagem regressiva"'),
        ('"11 月 2 日，还剩 17 天"', '"2 de novembro, faltam 17 dias"'),
        ('"11 月 7 日，还剩 12 天"', '"7 de novembro, faltam 12 dias"'),
        ('"11 月 18 日，就是明天"', '"18 de novembro, é amanhã"'),
        ('"11 月 19 日，就是今天"', '"19 de novembro, é hoje"'),
        ('"연습 · 第 2 版练习"', '"연습 · Exercícios pág. 2"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Respostas na pág. 8 · Os exercícios misturam os níveis: procure pelo número"'),
        # P2 exercise-section glosslines (Korean instruction apparatus -> Portuguese)
        ('e.glossline("2면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Leia os textos da pág. 2 e escolha a resposta certa.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Coloque a palavra certa no espaço.")'),
        ('e.glossline("1면과 2면의 숫자와 날짜로 답하세요.")',
         'e.glossline("Responda com os números e as datas das págs. 1 e 2.")'),
        ('instr="把词和说明配对"', 'instr="Associe"'),
    ])
    print("content12 done")

    # ---- Shared P8/exercise notes (applied wherever they occur) ----
    # Each literal must occur at least once across the five content files;
    # the trailing Han-zero check proves none was missed.
    # Order matters: longer forms before their substrings (see KO x DE §11c).
    NOTES = [
        ('"立冬在11月7日周六"', '"Ipdong no sábado, 7 de novembro"'),
        ('"泡菜季＝腌过冬泡菜"', '"Kimjang = conservar kimchi para o inverno"'),
        ('"高考在11月19日周四"', '"O exame é na quinta-feira, 19 de novembro"'),
        ('"11月2日是D-17"', '"2 de novembro é D-17"'),
        ('"台风没有在韩国本土登陆"', '"Sem chegada do tufão ao continente coreano"'),
        ('"首尔报名窗口11月6日10–12点"', '"Inscrição em Seul em 6 de novembro, das 10 às 12"'),
        ('"立冬＝冬季开始的节气"', '"Ipdong = o início do inverno"'),
        ('"内藏山两个预报：11月4日与11月11日"', '"Naejangsan: duas previsões, 4 e 11 de novembro"'),
        ('"10月25日首场比赛因雨推迟"', '"O jogo 1 de 25 de outubro foi adiado pela chuva"'),
        ('"山火注意期从11月1日开始"', '"Cuidado com incêndios a partir de 1.º de novembro"'),
        ('"带火进山最高罚30万韩元"', '"Levar fogo à montanha: multa de até 300.000 wons"'),
        ('"韩史考试在11月28日周六"', '"O exame de história é no sábado, 28 de novembro"'),
        ('"首尔报名10点至12点"', '"Inscrição em Seul das 10 às 12"'),
        ('"白菜用盐腌"', '"A couve-chinesa é salgada"'),
        ('"加入萝卜和调料拌匀"', '"Misturam-se nabo e temperos"'),
        ('"过冬准备＝为冬天做准备"', '"Preparação para o inverno = preparar-se para o inverno"'),
        ('"进山要小心火"', '"Na montanha, cuidado com o fogo"'),
        ('"11月3日起开始报名"', '"Inscrições a partir de 3 de novembro"'),
        ('"山火注意期到12月15日"', '"Cuidado com incêndios até 15 de dezembro"'),
        ('"最高罚款30万韩元"', '"Multa máxima de 300.000 wons"'),
        ('"深化考试费27,000韩元"', '"Taxa do nível avançado: 27.000 wons"'),
        ('"11月6日13点起全国报名剩余名额"', '"A partir das 13h de 6 de novembro: vagas restantes em todo o país"'),
        ('"김장=腌过冬泡菜 a"', '"김장=kimchi para o inverno a"'),
        ('"월동 준비=准备过冬 c"', '"월동 준비=preparação para o inverno c"'),
        ('"산불조심=进山小心火 d"', '"산불조심=cuidado com o fogo na montanha d"'),
        ('"한능검=韩国史考试简称 b"', '"한능검=forma curta do exame de história b"'),
        ('"内藏山林业厅预报峰值11月4日"', '"Naejangsan, Serviço Florestal: 4 de novembro"'),
        ('"内藏山公园公团预报峰值11月11日"', '"Naejangsan, Serviço de Parques: 11 de novembro"'),
        ('"内藏山公团预报峰值11月11日"', '"Naejangsan, Serviço de Parques: 11 de novembro"'),
        ('"雪岳山实际观测峰值10月16日"', '"Seoraksan, observado de fato: 16 de outubro"'),
        ('"青松现场庆典11月4日起"', '"Cheongsong no local a partir de 4 de novembro"'),
        ('"青松现场庆典11月4日至8日"', '"Cheongsong no local: de 4 a 8 de novembro"'),
        ('"没有官方的路段数值"', '"Sem valores oficiais por trecho"'),
        ('"红叶最美的时候叫절정"', '"O auge da folhagem chama-se 절정"'),
        ('"日期不同因为标准不同"', '"Datas diferentes porque os critérios diferem"'),
        ('"实际观测比预报早"', '"A observação veio antes da previsão"'),
        ('"现场庆典11月4日起"', '"Festa no local a partir de 4 de novembro"'),
        ('"青松以苹果闻名"', '"Cheongsong é famosa pelas maçãs"'),
        ('"内藏山林业厅预报4日"', '"Naejangsan, Serviço Florestal: dia 4."'),
        ('"内藏山公团预报11日"', '"Naejangsan, Serviço de Parques: dia 11."'),
        ('"月出山林业厅预报9日"', '"Wolchulsan, Serviço Florestal: dia 9."'),
        ('"雪岳山实际观测16日"', '"Seoraksan, observado: dia 16."'),
        ('"내장산=两个预报之间 b"', '"내장산=entre duas previsões b"'),
        ('"월출산=11月9日前夕 a"', '"월출산=véspera de 9 de novembro a"'),
        ('"북한산=11月4日之后、低路更晚 d"', '"북한산=depois de 4 de novembro, caminhos baixos mais tarde d"'),
        ('"설악산=实际观测10月16日 c"', '"설악산=observado em 16 de outubro c"'),
        ('"半决赛胜队是KIA"', '"O vencedor da semifinal é o KIA"'),
        ('"第3场比分13比1"', '"Jogo 3: 13 a 1"'),
        ('"第3场在蚕室举行"', '"O jogo 3 foi em Jamsil"'),
        ('"季后赛首场因雨推迟"', '"O jogo 1 do playoff foi adiado pela chuva"'),
        ('"公布的韩国大赛开始日11月2日"', '"Série Coreana, anunciada: 2 de novembro"'),
        ('"KIA三连胜晋级"', '"O KIA avançou com três vitórias seguidas"'),
        ('"三连胜晋级"', '"Três vitórias seguidas"'),
        ('"首场比赛因雨推迟"', '"O jogo 1 foi adiado pela chuva"'),
        ('"10月26日变为温带气旋"', '"Em 26 de outubro virou ciclone extratropical"'),
        ('"kt在韩国大赛等候"', '"O kt espera na Série Coreana"'),
        ('"이기다的过去式이겼어요"', '"O passado de 이기다 é 이겼어요"'),
        ('"열리다的过去式열렸어요"', '"O passado de 열리다 é 열렸어요"'),
        ('"미뤄지다的过去式미뤄졌어요"', '"O passado de 미뤄지다 é 미뤄졌어요"'),
        ('"바뀌다的过去式바뀌었어요"', '"O passado de 바뀌다 é 바뀌었어요"'),
        ('"준플레이오프=KIA三连胜 b"', '"준플레이오프=KIA com três vitórias b"'),
        ('"플레이오프=KIA对三星 d"', '"플레이오프=KIA contra o Samsung d"'),
        ('"한국시리즈=kt在等候 a"', '"한국시리즈=o kt espera a"'),
        ('"온대저기압=台风10月26日变化 c"', '"온대저기압=mudança do tufão em 26 de outubro c"'),
        ('"온대저기압=台风10月26日变化 d"', '"온대저기압=mudança do tufão em 26 de outubro d"'),
        ('"11月7日是D-12"', '"7 de novembro é D-12"'),
        ('"听力时段飞机不起降"', '"Durante a escuta, sem voos"'),
        ('"首尔万圣节安全人员3,271人"', '"Seul, Halloween: 3.271 agentes"'),
        ('"梨泰院路10月31日管制"', '"Itaewon-ro fechada em 31 de outubro"'),
        ('"全国为考生加油"', '"O país inteiro torce pelos candidatos"'),
        ('"倒计时仍在继续"', '"A contagem regressiva continua"'),
        ('"怀着祈愿合格的心意赠送糯米糕、饴糖"', '"Bolos de arroz glutinoso e doces de malte como presente de boa sorte"'),
        ('"首尔安全人员3,271人"', '"Seul: 3.271 agentes"'),
        ('"今年考生551,864人"', '"Este ano: 551.864 candidatos"'),
        ('"考场全国1,312处"', '"1.312 locais de prova em todo o país"'),
        ('"考试日机关10点上班"', '"No dia da prova, órgãos começam às 10"'),
        ('"梨泰院部署1,620人"', '"Itaewon: 1.620 agentes"'),
        ('"语序：主语+副词+动词"', '"Ordem: sujeito + advérbio + verbo"'),
        ('"主语+宾语+动词的语序"', '"Ordem: sujeito + objeto + verbo"'),
        ('"首尔管理14个地点"', '"Seul administra 14 locais"'),
        ('"本周倒计时D-17至D-12"', '"Esta semana: contagem D-17 a D-12"'),
        ('"考试日有特别措施"', '"No dia da prova há medidas especiais"'),
        ('"本周没有特别措施"', '"Esta semana, sem medidas especiais"'),
        ('"考试日就是D-day"', '"O dia da prova é o D-day"'),
        ('"本周氛围是倒计时"', '"Esta semana: clima de contagem regressiva"'),
        ('"氛围在现在、本周"', '"Clima: agora, esta semana"'),
        ('"特别措施只适用于11月19日"', '"Medidas só em 19 de novembro"'),
        ('"措施只适用于11月19日"', '"Medidas só em 19 de novembro"'),
        ('"听力时段13:10～13:35"', '"Escuta: 13h10–13h35"'),
        ('"倒计时氛围在本周"', '"Clima de contagem nesta semana"'),
        ('"特别措施只适用于考试日"', '"Medidas especiais só no dia da prova"'),
        ('"从D-17到D-12的一周"', '"Semana de D-17 a D-12"'),
        ('"大数字显示全国规模"', '"Números grandes mostram a escala nacional"'),
        ('"听力时段飞机受管制"', '"Voos restritos durante a escuta"'),
        ('"本周是倒计时氛围"', '"Esta semana é clima de contagem"'),
        ('"节气＝一年24个时节"', '"Jeolgi = as 24 estações do ano"'),
        ('"D-1＝明天"', '"D-1 = amanhã"'),
        ('"D-day就是当天"', '"O D-day é o próprio dia"'),
        ('"日期不同因标准不同（3版）"', '"Critérios diferentes, datas diferentes (pág. 3)"'),
        ('"林业厅标准是叶子50%"', '"Serviço Florestal: 50% das folhas"'),
        ('"实际观测10月16日"', '"Observado em 16 de outubro"'),
        ('"预报要标准日期一起看"', '"Leia a previsão com critério e data"'),
        ('"汉拿山三角峰降雨415.5毫米"', '"Hallasan, Samgakbong: 415,5 mm de chuva"'),
        ('"智敏周六去内藏山"', '"Jimin vai a Naejangsan no sábado"'),
        ('"周日帮忙腌泡菜"', '"No domingo ajuda no kimjang"'),
        ('"下周准备韩史考试"', '"Na próxima semana: preparação para o exame de história"'),
        ('"智敏喜欢韩国史"', '"Jimin gosta de história coreana"'),
        ('"语序：主语+时间+场所+动词"', '"Ordem: sujeito + tempo + lugar + verbo"'),
        ('"보러 가요 = 去看"', '"보러 가요 = ir ver"'),
        ('"动作场所用「에서」"', '"O lugar da ação leva «에서»"'),
        ('"月出山林业厅预报峰值11月9日"', '"Wolchulsan, Serviço Florestal: pico em 9 de novembro"'),
        ('"首尔报名窗口10点至12点"', '"Inscrição em Seul das 10 às 12"'),
        ('"周六去内藏山"', '"No sábado, a Naejangsan"'),
        ('"首尔报名10点开始"', '"Inscrição em Seul a partir das 10"'),
        ('"日期不同因标准不同"', '"Critérios diferentes, datas diferentes"'),
        ('"입동=冬季开始的节气 a"', '"입동=início do inverno a"'),
        ('"절정=最佳时期 b"', '"절정=auge, o melhor momento b"'),
        ('"김장=腌过冬泡菜 c"', '"김장=kimchi para o inverno c"'),
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
        ('"문화 · 文化"', '"문화 · Cultura"'),
        ('"레벨 A2→B1 · 단풍 마지막 주말 · 红叶最后一周"',
         '"레벨 A2→B1 · 단풍 마지막 주말 · O último fim de semana da folhagem"'),
        ('"기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。"',
         '"기관 = órgão · 기준 = critério · 관측 = observação · 구간별 = por trecho."'),
        ('"현장 现场 · 유명하다 有名 · 맛보다 品尝。"',
         '"현장 = no local · 유명하다 = famoso · 맛보다 = provar."'),
        ('"이용하다 利用 · 막히다 堵塞 · 예의 礼仪。"',
         '"이용하다 = usar · 막히다 = congestionado · 예의 = boas maneiras."'),
        ('"겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。"',
         '"겹쳐 입다 = vestir em camadas · 미끄러지다 = escorregar · 돌 = pedra."'),
        ('"단풍 구경 준비물 · 红叶观赏准备"', '"단풍 구경 준비물 · O que levar"'),
        ('"你呢？想去看红叶的山是哪座？写两句韩语寄来。"',
         '"E você? A qual montanha você quer ir ver a folhagem? Escreva duas frases em coreano e envie."'),
        ('"당신은? · 说说你自己"', '"당신은? · E você?"'),
        ('"연습 · 第 3 版练习"', '"연습 · Exercícios pág. 3"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Respostas na pág. 8 · Os exercícios misturam os níveis: procure pelo número"'),
        ('e.glossline("3면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Leia os textos da pág. 3 e escolha a resposta certa.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Coloque a palavra certa no espaço.")'),
        ('e.glossline("3면의 숫자와 날짜로 답하세요.")',
         'e.glossline("Responda com os números e as datas da pág. 3.")'),
        ('"스포츠 · 体育"', '"스포츠 · Esporte"'),
        ('"레벨 B1 · 가을야구 소식 · 秋季棒球消息"',
         '"레벨 B1 · 가을야구 소식 · Notícias do beisebol de outono"'),
        ('"연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。"',
         '"연승 = série de vitórias · 만루홈런 = grand slam · 미뤄지다 = ser adiado · 마감하다 = fechamento da edição."'),
        ('"흔들다 挥动 · 하나가 되다 融为一体。"',
         '"흔들다 = agitar · 하나가 되다 = tornar-se um só."'),
        ('"예상 预测。"', '"예상 = previsão."'),
        ('"한국시리즈까지의 길 · 通往韩国大赛之路"',
         '"한국시리즈까지의 길 · O caminho até a Série Coreana"'),
        ('"연습 · 第 4 版练习"', '"연습 · Exercícios pág. 4"'),
        ('e.glossline("4면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Leia os textos da pág. 4 e escolha a resposta certa.")'),
        ('e.glossline("문장을 과거형으로 바꾸세요. (바꾼 문장은 모두 이 신문에 나온 일이에요.)")',
         'e.glossline("Passe as frases para o passado. (Todas estão nesta edição.)")'),
        ('instr="把山和说明配对"', 'instr="Associe"'),
        ('instr="把词和说明配对"', 'instr="Associe"'),
        ('instr="改写"', 'instr="Reescreva"'),
    ])
    apply_pairs("content56.py", [
        ('"청년 · 青年"', '"청년 · Jovens"'),
        ('"레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒计时与万圣节"',
         '"레벨 B1 · 수능 카운트다운과 할로윈 · Contagem para o exame e Halloween"'),
        ('"정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。"',
         '"정리 = organizar, revisar · 끈끈하다 = pegajoso · 합격 = aprovação."'),
        ('"중점 重点 · 배치하다 部署 · 통제하다 管制。"',
         '"중점 = foco · 배치하다 = destacar · 통제하다 = controlar."'),
        ('"이번 주 청년 숫자 · 本周青年数字"', '"이번 주 청년 숫자 · Em números"'),
        ('"챙기다 准备好 · 졸리다 犯困 · 평소 平时。"',
         '"챙기다 = preparar · 졸리다 = estar com sono · 평소 = normalmente."'),
        ('"비다 祈愿 · 피하다 避开 · 미끄럽다 滑。"',
         '"비다 = pedir com fé · 피하다 = evitar · 미끄럽다 = escorregadio."'),
        ('"你呢？想对考生说的一句加油是什么？写两句韩语寄来。"',
         '"E você? Qual é a sua frase de incentivo para os candidatos? Escreva duas frases em coreano e envie."'),
        ('"당신은? · 说说你自己"', '"당신은? · E você?"'),
        ('"연습 · 第 5 版练习"', '"연습 · Exercícios pág. 5"'),
        ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
         '"Respostas na pág. 8 · Os exercícios misturam os níveis: procure pelo número"'),
        ('e.glossline("5면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Leia os textos da pág. 5 e escolha a resposta certa.")'),
        ('e.glossline("빈칸에 알맞은 말을 넣으세요.")',
         'e.glossline("Coloque a palavra certa no espaço.")'),
        ('e.glossline("5면의 숫자로 답하세요.")',
         'e.glossline("Responda com os números da pág. 5.")'),
        ('e.glossline("말을 바른 순서로 놓아 문장을 만드세요.")',
         'e.glossline("Coloque as palavras na ordem certa para formar uma frase.")'),
        ('"깊이 읽기 · 深读"', '"깊이 읽기 · Leitura aprofundada"'),
        ('"레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒计时读法"',
         '"레벨 B2 · 수능 카운트다운을 읽는 법 · Como ler a contagem para o exame"'),
        ('"짙어지다 变浓 · 규모 规模 · 섞다 混淆。"',
         '"짙어지다 = intensificar-se · 규모 = escala · 섞다 = confundir."'),
        ('"겁이 나다 害怕 · 중요하다 重要。"',
         '"겁이 나다 = ter medo · 중요하다 = importante."'),
        ('"예정 预定 · 확정 确定 · 믿다 相信。"',
         '"예정 = previsto · 확정 = confirmado · 믿다 = acreditar."'),
        ('"이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清"',
         '"이번 주와 시험 날, 한눈에 보기 · Esta semana e o dia da prova lado a lado"'),
        ('"연습 · 第 6 版练习"', '"연습 · Exercícios pág. 6"'),
        ('e.glossline("6면의 표를 보고 맞는 답을 고르세요.")',
         'e.glossline("Olhe a tabela da pág. 6 e responda.")'),
        ('e.glossline("6면의 글을 읽고 맞는 답을 고르세요.")',
         'e.glossline("Leia os textos da pág. 6 e escolha a resposta certa.")'),
        ('e.glossline("문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.")',
         'e.glossline("Se a frase estiver certa, escolha 맞다; se estiver errada, 틀리다.")'),
        ('instr="造句"', 'instr="Monte"'),
    ])
    apply_pairs("content7.py", [
        ('"말 공부 · 语言"', '"말 공부 · Língua"'),
        ('"언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三个级别，三个主题"',
         '"언어 포커스 · 세 가지 레벨, 세 가지 주제 · Três níveis, três temas"'),
        ('a.glossline("본격적 正式、全面 · 나다 度过。")',
         'a.glossline("본격적 = de verdade, pleno · 나다 = passar.")'),
        ('b.glossline("남다 剩下 · 바로 正是、恰恰。")',
         'b.glossline("남다 = restar, faltar · 바로 = exatamente.")'),
        ('c.glossline("짐작하다 推测 · 나누다 区分。")',
         'c.glossline("짐작하다 = supor · 나누다 = distinguir.")'),
        ('"去某地用「에」，不用「를」。"', '"Vai-se com «에»; «에서» é o lugar da ação."'),
        ('"「담그다」的过去式是「담갔어요」。"',
         '"O passado de «담그다» é «담갔어요»."'),
        ('"数字与前面要留空格。"', '"Números com espaço."'),
        ('"助词只用一个。"', '"Use uma só partícula: «서울에서 만났어요»."'),
        ('"실수 병원 · 易错诊所"', '"실수 병원 · A clínica dos erros"'),
        ('"句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」"',
         '"A estrutura: «de 〜 até 〜». Para perguntar: «〜부터 〜까지예요?»"'),
        ('"이번 주의 틀 · 本周句式"', '"이번 주의 틀 · A frase-modelo"'),
        ('"编辑部示例信，非真实来信。"', '"Exemplo da redação, não é uma carta de verdade."'),
        ('"알려요: 이 편지는 편집부가 쓴 예예요. 마감 때까지 진짜 독자 편지와 8면 쓰기 우수작이 도착하지 않았어요. 그래서 예가 실렸고, 지난 호의 약속은 VOL.3으로 이어져요."',
         '"Até o fechamento, não chegaram cartas de verdade nem os melhores textos da pág. 8. O exemplo fica; a promessa anterior vale para o VOL.3."'),
        ('"郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。"',
         # 2 lines at 20pt/390px, second line '8!' carries no descender:
         # the previous wording wrapped 'texto da pág. 8!' onto the
         # phrases rule (baseline only 4.2px above it), a NEW LINEX flag.
         '"Envie sua carta e seu melhor texto da pág. 8!"'),
        # Letters-box height: the core formula undercounts actual render
        # height by ~26px (core's own last line also sits below its box
        # border). +26 -> +34 threads THIS edition's box border through
        # the inter-line gap of the solicitation (line-1 ink bottom
        # 1741.3 < border 1746.9 < line-2 '8!' ink top ~1750.4), clearing
        # the BOXTITLE flag without moving any baseline; teaser stays
        # <2540 (2520.94).
        ('len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 26',
         'len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 34'),
        ('"독자의 편지 · 读者园地"', '"독자의 편지 · Cartas dos leitores"'),
        ('"이번 주의 문장 · 本周金句（逐字摘自本期文章）"',
         '"이번 주의 문장 · Frases da semana (ao pé da letra, desta edição)"'),
        ('"11 月 7 日是立冬。"', '"O dia 7 de novembro é Ipdong."'),
        ('"只能说是接近峰值的周末。"', '"Só se pode dizer: um fim de semana perto do auge."'),
        ('"泡菜季就是腌过冬泡菜。"', '"Kimjang é conservar kimchi para o inverno."'),
        ('"离高考还剩 17 天，今天是 D-17。"', '"Faltam 17 dias para o exame. Hoje é D-17."'),
        ('"低处的路红得更晚。"', '"Os caminhos baixos ficam vermelhos mais tarde."'),
        ('"KIA 虎三连胜战胜 LG 双子。"', '"O KIA venceu o LG Twins com três vitórias seguidas."'),
        ('"全国都在为考生加油。"', '"O país inteiro torce pelos candidatos."'),
        ('"先看日期。"', '"Olhe primeiro a data."'),
        ('"다음 주 · 下期预告 (VOL.3)"', '"다음 주 · Na próxima semana (VOL.3)"'),
    ])
    apply_pairs("content8.py", [
        ('"시험과 답 · 测验与答案"', '"시험과 답 · Teste e respostas"'),
        # E redirect: KO -> PT keys for 137/138, PT stems for 139/140, KO keys frozen
        ('f.ex("A2", "翻译", "11月7日是立冬。", "对照第 1 版"',
         'f.ex("A2", "翻译", "O dia 7 de novembro é Ipdong.", "Veja a pág. 1"'),
        ('f.ex("A2", "翻译", "离高考还剩 12 天。", "对照第 5 版"',
         'f.ex("A2", "翻译", "Faltam 12 dias para o exame.", "Veja a pág. 5"'),
        ('"特别措施只适用于11月19日。→ ___", instr="翻译"',
         '"Medidas especiais valem só no dia 19 de novembro. → ___", instr="翻译"'),
        ('"对照第 6 版"', '"Veja a pág. 6"'),
        ('"我周六去内藏山看红叶。→ ___", instr="翻译"',
         '"No sábado, vou a Naejangsan ver a folhagem de outono. → ___", instr="翻译"'),
        ('"对照第 3 版"', '"Veja a pág. 3"'),
        ('"(开放题，范文如下)"', '"(pergunta aberta — o modelo está abaixo)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"O modelo está na seção H desta página ({NCHARS} caracteres)"'),
        ('f.glossline(f"쓰기 문제예요 (정답은 하나가 아니에요). 아래에 {NCHARS}자의 예가 있어요.")',
         'f.glossline(f"É um exercício de escrita (não há uma única resposta certa). Abaixo há um exemplo de {NCHARS} caracteres.")'),
        ('"답 · 参考答案 — 按版面分页排列，找到题号即可"',
         '"답 · Respostas — ordenadas por página, procure o número"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Cada resposta com uma breve nota em português · ✓ = exercício com modelo"'),
        ('instr="把词和释义配对"', 'instr="Associe"'),
        ('instr="翻译"', 'instr="Traduza"'),
        ('instr="写作"', 'instr="Escreva"'),
        ('instr="造句"', 'instr="Monte"'),
    ])
    # instr="填空" counts per file (asserted, from the core inventory)
    for fname, want in [("content12.py", 9), ("content34.py", 14),
                        ("content56.py", 13), ("content7.py", 6)]:
        path = os.path.join(HERE, fname)
        src = open(path, encoding="utf-8").read()
        n = src.count('instr="填空"')
        assert n == want, f"{fname}: instr 填空 count {n} != {want}"
        open(path, "w", encoding="utf-8").write(src.replace('instr="填空"', 'instr="Complete"'))
        print(f"  {fname}: instr 填空 x{n} -> Complete")
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
        for bad in ("特别M", "KIATrês"):
            assert bad not in raw, f"{fname}: substring-order corruption {bad}"
    print("transform OK: all rendered strings Portuguese; only internal type keys keep Han")


if __name__ == "__main__":
    main()
