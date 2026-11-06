# -*- coding: utf-8 -*-
"""W45 zh-tw x pt fan-out transform (TRANSFORM-FIRST discipline).

Applies ONLY explanation-layer edits to a fresh copy of the W45 zh-tw core
build (hidden_files/weekly-report-w45-zhtw-build). Target Traditional
Chinese text is NEVER touched: every replacement below is an English
explanation string, a bilingual furniture head, or the P8 key typography
(dash -> paren style, per the W43 zh-tw-pt family's shipped build code,
which prints `N. key (note)` with half-width parens).

Differences vs the es sibling's map (same core, recorded here so the
proofreader does not mistake them for misses):
- EXTRA pair: "棒球詞卡 · Baseball words" -> "棒球詞卡 · Palavras"
  (both sibling maps missed it; it survives as English residue in the
  es/it renders. Measured 327.9 at 34pt bold, inside CW 434.)
- Match instructions: word<->definition matches -> "Associe palavra e
  definição"; the P4 term<->info match -> "Associe nome e informação".
- Currency: NT$ prefix with space ("NT$ 2.400"), per the W43 zh-tw-pt
  KIT's recorded PT-column convention ("HK$ 258" order).
- Thousands separator "." (Brazilian), ordinals 1.º / 8.ª.

Usage:
  python transform.py            # rebuild MY build dir from core + apply
  python transform.py --gate10   # fresh temp copy + apply + one-process
                                 # driver run + byte-compare vs delivered
                                 # SVGs (exit 0 only on 8/8 + 0 warnings)
NEVER import a content module inside the core build dir; this script only
copies files, edits text, and runs the copy's own one-process driver.
"""
import os, re, shutil, subprocess, sys, hashlib

HOME = os.path.expanduser("~")
GOAL = os.path.join(HOME, "workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")
MYBUILD = os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-pt-build")
DELIVERY = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-pt")
CORE_SVG_PATH = "files/weekly-report-w45-zhtw-core/svg"
MY_SVG_PATH = "files/weekly-report-w45-zh-tw-pt/svg"
PYFILES = ["bslib4.py", "svglib.py", "run.py", "render.py",
           "content12.py", "content34.py", "content56.py",
           "content7.py", "content8.py"]
PRESERVE = ("preflight-snap", "baseline", "inventory", "checks")


def fresh_copy(dest):
    if os.path.isdir(dest):
        for name in os.listdir(dest):
            if name.startswith(PRESERVE):
                continue
            path = os.path.join(dest, name)
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
    else:
        os.makedirs(dest)
    for f in PYFILES:
        shutil.copy2(os.path.join(CORE, f), os.path.join(dest, f))
    shutil.copytree(os.path.join(CORE, "assets"), os.path.join(dest, "assets"))


def rep(text, old, new, count, fname):
    got = text.count(old)
    assert got == count, f"{fname}: expected {count}x {old[:60]!r}, found {got}x"
    return text.replace(old, new)


def apply_file(dest, fname, pairs):
    path = os.path.join(dest, fname)
    text = open(path, encoding="utf-8").read()
    for old, new, count in pairs:
        text = rep(text, old, new, count, fname)
    open(path, "w", encoding="utf-8").write(text)


def repoint(dest, svg_dir, delivery_dir):
    # OUT lines in content*.py + BASE/PDF names in render.py.
    for fname in ["content12.py", "content34.py", "content56.py",
                  "content7.py", "content8.py"]:
        path = os.path.join(dest, fname)
        text = open(path, encoding="utf-8").read()
        assert CORE_SVG_PATH in text, f"{fname}: core OUT path missing"
        text = text.replace(CORE_SVG_PATH, svg_dir)
        open(path, "w", encoding="utf-8").write(text)
    path = os.path.join(dest, "render.py")
    text = open(path, encoding="utf-8").read()
    assert "weekly-report-w45-zhtw-core" in text
    text = text.replace("weekly-report-w45-zhtw-core", "weekly-report-w45-zh-tw-pt")
    text = text.replace('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-PT.pdf"')
    text = text.replace('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-PT-web.pdf"')
    open(path, "w", encoding="utf-8").write(text)


# ---------------------------------------------------------------- bslib4
BSLIB = [
    ("Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations",
     "Lucerna · SEMANÁRIO CHINÊS TRADICIONAL VOL.2 · TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS", 1),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1),
    ("Notes｜", "Nota — ", 1),
]

# ---------------------------------------------------------------- content12 (P1+P2)
C12 = [
    # P1 badge: in-place at y=378, size 21, BRICK (measured on the W45 core
    # P1: x=975 y=378 21pt w700 OLIVE #3e4c2a; measured on the W43 zh-tw-pt
    # P1: same slot x=975 y=378 21pt w700 BRICK #a4553a; tables.json PT
    # badge string verbatim, ink 1274.4 of the 1820 slot).
    ('p.text(975, 378, "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers", 21, "sans", True, OLIVE, anchor="middle")',
     'p.text(975, 378, "TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 21, "sans", True, BRICK, anchor="middle")', 1),
    ("Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
     "Reportagem da redação · Fonte: comunicado de imprensa dos organizadores (23 de outubro) e perguntas frequentes do evento", 1),
    ("Hong Kong FinTech Week x StartmeupHK 2026 opens Monday (Nov 2) and runs to Friday (Nov 6). The main conference and exhibition are at the Hong Kong Convention and Exhibition Centre on Nov 2-3, with 100+ community events through the week. Expect 45,000+ people from 120+ economies, 1,000+ speakers and 800+ exhibitors and start-ups.",
     "A Semana FinTech de Hong Kong x StartmeupHK 2026 abre na segunda-feira (2 de novembro) e vai até sexta-feira (6 de novembro). A conferência principal e a exposição acontecem no Centro de Convenções e Exposições de Hong Kong nos dias 2 e 3 de novembro, com mais de 100 eventos comunitários ao longo da semana. São esperadas mais de 45.000 pessoas de mais de 120 economias, mais de 1.000 palestrantes e mais de 800 expositores e startups.", 1),
    ("The Taipei International Travel Fair (ITF) opens Friday (Nov 6) at noon at the Nangang Exhibition Center and runs to Monday (Nov 9): 123 countries and cities, 1,600 booths, a daily 14:00 mascot parade and travel talks.",
     "A Feira Internacional de Viagens de Taipé (ITF) abre na sexta-feira (6 de novembro) ao meio-dia no Centro de Exposições de Nangang e vai até segunda-feira (9 de novembro): 123 países e cidades, 1.600 estandes, um desfile diário de mascotes às 14:00 e palestras de viagem.", 1),
    ("本週大事 · This week", "本週大事 · Esta semana", 1),
    ("本週一詞 · Word of the week", "本週一詞 · Palavra da semana", 1),
    ("「金融科技」 — fintech: using technology to run financial services, like paying by phone or scanning a code to pay.",
     "「金融科技」 — fintech: usar a tecnologia para gerir serviços financeiros, como pagar pelo celular ou escanear um código para pagar.", 1),
    ("快速測驗 · Quick quiz", "快速測驗 · Quiz rápido", 1),
    ("標題填空 · Headline words", "標題填空 · Palavras dos títulos", 1),
    ("FinTech Week opens on Monday, Nov 2.", "A Semana FinTech abre na segunda-feira, 2 de novembro.", 1),
    ("The main conference is at the Hong Kong Convention and Exhibition Centre.", "A conferência principal é no Centro de Convenções e Exposições de Hong Kong.", 1),
    ("More than 45,000 people are expected.", "São esperadas mais de 45.000 pessoas.", 1),
    ("The travel fair opens Friday, Nov 6, at noon.", "A feira de viagens abre na sexta-feira, 6 de novembro, ao meio-dia.", 1),
    ("Participants come from 120+ economies.", "Os participantes vêm de mais de 120 economias.", 1),
    ("More than 800 exhibitors and start-ups take part.", "Participam mais de 800 expositores e startups.", 1),
    ("The travel fair gathers 123 countries and cities.", "A feira de viagens reúne 123 países e cidades.", 1),
    ("The travel fair has 1,600 booths.", "A feira de viagens tem 1.600 estandes.", 1),
    ("Saturday, Nov 7 is the Start of Winter solar term.", "Sábado, 7 de novembro, é o termo solar do Início do Inverno.", 1),
    ("The travel fair runs to Monday, Nov 9.", "A feira de viagens vai até segunda-feira, 9 de novembro.", 1),
    # P2
    ("生活 · Life", "生活 · Vida cotidiana", 1),
    ("第 2 版 · 天氣、泡湯、旅展與雙11 · Weather, hot springs, the travel fair and 11.11",
     "第 2 版 · 天氣、泡湯、旅展與雙11 · Tempo, águas termais, a feira de viagens e o Duplo 11", 1),
    ("The northeast monsoon cools northern Taiwan, and Saturday (Nov 7) is Lidong, the Start of Winter: the day winter begins in the 24 solar terms. Many people mark it with a hot, nourishing pot meal.",
     "A monção do nordeste esfria o norte de Taiwan, e sábado (7 de novembro) é Lidong, o Início do Inverno: o dia em que o inverno começa nos 24 termos solares. Muita gente marca a data com uma refeição quente e nutritiva na panela.", 1),
    ("Autumn and winter are for hot springs and hiking. The travel fair's trail encyclopaedia collects 56 routes, and the 6 Greenways stamp challenge covers the Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous and Sugar-Rail trails.",
     "Outono e inverno são época de águas termais e trilhas. A enciclopédia de trilhas da feira de viagens reúne 56 rotas, e o desafio de carimbos das 6 Trilhas Verdes abrange as trilhas Tamsui-Kavalan, Raknus Selu, da Montanha ao Mar, do Centenário, Indígena e da Ferrovia do Açúcar.", 1),
    ("練習例子 · Practice example", "練習例子 · Exemplo prático", 1),
    ("Practice numbers: NT$2,400 + NT$1,600 = NT$4,000, exactly her budget — so she can buy both.",
     "Números do exemplo: NT$ 2.400 + NT$ 1.600 = NT$ 4.000, exatamente o orçamento dela — dá para comprar as duas coisas.", 1),
    ("讀懂了嗎? · Did you get it?", "讀懂了嗎? · Entendeu?", 1),
    ("填一填 · Fill in", "填一填 · Complete", 1),
    ("算一算 · Work it out", "算一算 · Faça as contas", 1),
    ("Lidong, the Start of Winter, is Saturday, Nov 7.", "Lidong, o Início do Inverno, é sábado, 7 de novembro.", 1),
    ("The northeast monsoon cools northern Taiwan.", "A monção do nordeste esfria o norte de Taiwan.", 1),
    ("The trail encyclopaedia collects 56 routes.", "A enciclopédia de trilhas reúne 56 rotas.", 1),
    ("The stamp challenge has 6 Greenways.", "O desafio de carimbos tem 6 Trilhas Verdes.", 1),
    ("Double 11 falls on Wednesday, Nov 11.", "O Duplo 11 cai na quarta-feira, 11 de novembro.", 1),
    ("Before paying, check tax, delivery and returns.", "Antes de pagar, confira impostos, entrega e devoluções.", 1),
    ("A hot pot meal marks Lidong: 進補.", "Uma refeição de panela quente marca o Lidong: 進補.", 1),
    ("Check the jacket: mornings and evenings are cool.", "Não esqueça o casaco: manhãs e noites estão frescas.", 1),
    ("Autumn and winter are good for hot springs.", "Outono e inverno são bons para águas termais.", 1),
    ("Collect stamps on the 6 Greenways.", "Colecione carimbos nas 6 Trilhas Verdes.", 1),
    ("Set a budget before Double 11 shopping.", "Defina um orçamento antes de comprar no Duplo 11.", 1),
    ("The Tamsui-Kavalan Trail is one of the 6 Greenways.", "A trilha Tamsui-Kavalan é uma das 6 Trilhas Verdes.", 1),
    ("2,400 + 1,600 = 4,000, exactly the budget.", "2.400 + 1.600 = 4.000, exatamente o orçamento.", 1),
    ("The budget is 4,000 and the total is 4,000: nothing over.", "O orçamento é 4.000 e o total é 4.000: nada acima.", 1),
    ("立冬 — the Start of Winter solar term.", "立冬 — o termo solar do Início do Inverno.", 1),
    ("進補 — eating nourishing hot food for winter.", "進補 — comer alimentos quentes e nutritivos para o inverno.", 1),
    ("泡湯 — soaking in a hot spring.", "泡湯 — banho em águas termais.", 1),
    ("集章 — collecting stamps at set points.", "集章 — colecionar carimbos em pontos determinados.", 1),
    ('instr="Match"', 'instr="Associe palavra e definição"', 1),
    ("事實框 · This week's facts", "事實框 · Dados da semana", 1),
    ("你呢? · Over to you", "你呢? · E você?", 1),
    # Shortened by wording (2 wrap lines, = the English para): the fuller
    # "O que há no seu carrinho do Duplo 11?" wrapped to 3 lines and its
    # last line crossed the fixed 230px box border (audit BOXTITLE).
    ("What hot pot would you eat for Lidong? What is in your Double 11 cart?", "Que panela quente você comeria no Lidong? E no seu carrinho do Duplo 11?", 1),
    ("封王優惠 · Champion deals", "封王優惠 · Ofertas de campeão", 1),
    ('instr="Fill in"', 'instr="Complete"', 12),
]

# ---------------------------------------------------------------- content34 (P3+P4)
C34 = [
    ("文化 · Culture", "文化 · Cultura", 1),
    ("第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, steel art and the sand festival finale",
     "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, arte em aço e o fim do festival de areia", 1),
    ("Lidong is the first solar term of winter: winter begins. People mark it with hot pot dishes like ginger duck, lamb hotpot and sesame chicken — warming food before the cold months.",
     "Lidong é o primeiro termo solar do inverno: o inverno começa. As pessoas marcam a data com pratos de panela quente como pato com gengibre, panela de carneiro e frango com gergelim — comida que aquece antes dos meses frios.", 1),
    ("Kaohsiung's International Steel Sculpture Festival (Oct 23-Nov 22) turns warehouses, factories, the harbour and streets into a stage — SUPER STAGE — with an international forum on making, design and art in daily life.",
     "O Festival Internacional de Escultura em Aço de Kaohsiung (23 de outubro a 22 de novembro) transforma armazéns, fábricas, o porto e as ruas em um palco — SUPER STAGE — com um fórum internacional sobre fazer, design e arte na vida cotidiana.", 1),
    ("The Fulong International Sand Sculpture Art Festival closed Oct 26 after its 19th season (May 29-Oct 26): 40+ sculptures by 15+ artists, built from Fulong's golden sand around film characters from Jurassic World, Shrek, Kung Fu Panda and Back to the Future.",
     "O Festival Internacional de Escultura em Areia de Fulong encerrou em 26 de outubro após sua 19.ª temporada (29 de maio a 26 de outubro): mais de 40 esculturas de mais de 15 artistas, construídas com a areia dourada de Fulong em torno de personagens de cinema de Jurassic World, Shrek, Kung Fu Panda e De Volta para o Futuro.", 1),
    ("Lidong means winter begins.", "Lidong significa que o inverno começa.", 1),
    ("Ginger duck is a typical Lidong dish.", "Pato com gengibre é um prato típico do Lidong.", 1),
    ("The steel festival runs Oct 23-Nov 22.", "O festival do aço vai de 23 de outubro a 22 de novembro.", 1),
    ("The venues include Pier-2's Penglai B3 warehouse.", "Entre as sedes está o armazém B3 de Penglai, no Pier-2.", 1),
    ("The sand festival closed on Oct 26.", "O festival de areia encerrou em 26 de outubro.", 1),
    ("The sand festival made 40+ sculptures.", "O festival de areia fez mais de 40 esculturas.", 1),
    ("Lidong is a solar term (節氣).", "Lidong é um termo solar (節氣).", 1),
    ("Sesame chicken is a Lidong dish.", "Frango com gergelim é um prato do Lidong.", 1),
    ("Steel is Kaohsiung's material and memory.", "O aço é o material e a memória de Kaohsiung.", 1),
    ("Hamasen Railway Park is a venue.", "O Parque Ferroviário de Hamasen é uma sede.", 1),
    ("Fulong's sand is golden.", "A areia de Fulong é dourada.", 1),
    ("Jurassic World is one of the film characters.", "Jurassic World é um dos personagens de cinema.", 1),
    ("May 29-31 (3) + Jun 30 + Jul 31 + Aug 31 + Sep 30 + Oct 26 = 151 days.", "29 a 31 de maio (3) + 30 de junho + 31 de julho + 31 de agosto + 30 de setembro + 26 de outubro = 151 dias.", 1),
    ("Oct 23-31 (9) + Nov 22 = 31 days.", "23 a 31 de outubro (9) + 22 de novembro = 31 dias.", 1),
    ("立冬 — the first solar term of winter.", "立冬 — o primeiro termo solar do inverno.", 1),
    ("進補 — nourishing food before winter.", "進補 — comida nutritiva antes do inverno.", 1),
    ("鋼雕 — sculpture made of steel.", "鋼雕 — escultura feita de aço.", 1),
    ("沙雕 — sculpture built from sand.", "沙雕 — escultura construída com areia.", 1),
    ("節氣小表 · Solar terms", "節氣小表 · Termos solares", 1),
    ("Have you seen the Fulong sand sculptures? Which film character would you most want to see in sand?", "Você já viu as esculturas de areia de Fulong? Que personagem de cinema você mais gostaria de ver em areia?", 1),
    ("鋼雕行程 · Plan your visit", "鋼雕行程 · Planeje sua visita", 1),
    # P4
    ("體育 · Sport", "體育 · Esporte", 1),
    ("第 4 版 · 台灣大賽封王 · The Taiwan Series is decided",
     "第 4 版 · 台灣大賽封王 · A Série de Taiwan está decidida", 1),
    ("Staff report · Source: TSNA sports news, Oct 26",
     "Reportagem da redação · Fonte: notícias esportivas da TSNA, 26 de outubro", 1),
    ("The Wei Chuan Dragons beat the CTBC Brothers 6-0 in Game 6 (Oct 26, Taipei Dome) to win the 2026 Taiwan Series 4-2 — the first-ever Dragons-Brothers final and the Dragons' 6th title. Starter C.C. Mercedes threw 8 shutout innings and was named Series MVP.",
     "Os Wei Chuan Dragons venceram os CTBC Brothers por 6 a 0 no 6.º jogo (26 de outubro, Domo de Taipé) e conquistaram a Série de Taiwan 2026 por 4 a 2 — a primeira final Dragons–Brothers da história e o 6.º título dos Dragons. O arremessador titular C.C. Mercedes lançou 8 entradas sem sofrer pontos e foi eleito o MVP da série.", 1),
    ("Four words: 完封 (shutout), 封王 (clinching the title), 全壘打 (home run), MVP (most valuable player).",
     "Quatro palavras: 完封 (jogo sem sofrer pontos), 封王 (conquistar o título), 全壘打 (home run), MVP (jogador mais valioso).", 1),
    ("第六戰得分走勢 · Game 6 runs by inning — bars drawn in proportion to runs",
     "第六戰得分走勢 · Pontos do 6.º jogo por entrada — barras proporcionais aos pontos", 1),
    ("Note: the Dragons did not bat in the bottom of the 9th — leading 6-0 after the top of the 9th, the game was over. 1 + 5 = 6.",
     "Nota: os Dragons não rebateram na parte baixa da 9.ª entrada — vencendo por 6 a 0 após a parte alta da 9.ª, o jogo estava encerrado. 1 + 5 = 6.", 1),
    ("The Dragons won Game 6, 6-0.", "Os Dragons venceram o 6.º jogo por 6 a 0.", 1),
    ("The series ended 4-2 to the Dragons.", "A série terminou 4 a 2 para os Dragons.", 1),
    ("Mercedes threw 8 shutout innings.", "Mercedes lançou 8 entradas sem sofrer pontos.", 1),
    ("Mercedes was named Series MVP.", "Mercedes foi eleito o MVP da série.", 1),
    ("The Dragons' 6th title in team history.", "O 6.º título dos Dragons na história do time.", 1),
    ("Three shutouts in one series is a first.", "Três jogos sem sofrer pontos em uma mesma série é algo inédito.", 1),
    ("Game 6 was played at the Taipei Dome.", "O 6.º jogo foi disputado no Domo de Taipé.", 1),
    ("A shutout: the other side scores zero.", "Um jogo sem sofrer pontos: o adversário marca zero.", 1),
    ("Winning the title is 封王.", "Conquistar o título é 封王.", 1),
    ("A ball hit out of the park is a home run.", "Uma bola rebatida para fora do campo é um home run.", 1),
    ("Mercedes allowed 1 run in 14 innings.", "Mercedes cedeu 1 ponto em 14 entradas.", 1),
    ("The Dragons scored 5 runs in the 8th inning.", "Os Dragons marcaram 5 pontos na 8.ª entrada.", 1),
    ("The 8th inning: 5 runs, the biggest bar.", "A 8.ª entrada: 5 pontos, a maior barra.", 1),
    ("1 + 5 = 6 runs in total.", "1 + 5 = 6 pontos no total.", 1),
    ("完封 — a shutout: the other side scores zero.", "完封 — jogo sem sofrer pontos: o adversário marca zero.", 1),
    ("封王 — clinching the championship.", "封王 — conquistar o campeonato.", 1),
    ("全壘打 — a home run.", "全壘打 — um home run.", 1),
    ("安打 — a base hit.", "安打 — uma rebatida.", 1),
    ("系列賽小檔 · Series file", "系列賽小檔 · Ficha da série", 1),
    ("Which team do you support? Have you ever watched a baseball game live?", "Para que time você torce? Você já assistiu a um jogo de beisebol ao vivo?", 1),
    ("讀懂了嗎? · Did you get it?", "讀懂了嗎? · Entendeu?", 2),
    ("填一填 · Fill in", "填一填 · Complete", 2),
    ("你呢? · Over to you", "你呢? · E você?", 2),
    ("看圖答題 · Read the chart", "看圖答題 · Leia o gráfico", 1),
    # EXTRA vs both sibling maps: the P4 word-card title (34pt flow title).
    # Measured 327.9 at 34pt bold, inside CW 434.
    ("棒球詞卡 · Baseball words", "棒球詞卡 · Palavras", 1),
    ('instr="Fill in"', 'instr="Complete"', 12),
    # Caught by the full-render residual-Latin sweep (bilingual-node +
    # English-word-blacklist scans of ALL rendered nodes, not just
    # freeze-diff added strings): the P3 算一算 head was still English.
    # The sibling inventory extraction had missed this C34 tail pair;
    # the sweep also confirmed it is the ONLY English residue in the
    # edition (all other blacklist hits are frozen credits, the
    # official Fintech Nexus theme name, the fintech loanword, or the
    # PT verb somar: "some/Some as taxas").
    ("算一算 · Work it out", "算一算 · Faça as contas", 1),
]
# content34 Match sets in file order: P3 -> palavra, P4 -> nome.
C34_MATCH_ORDERED = ['instr="Associe palavra e definição"', 'instr="Associe nome e informação"']


def apply34(dest):
    apply_file(dest, "content34.py", C34)
    path = os.path.join(dest, "content34.py")
    text = open(path, encoding="utf-8").read()
    assert text.count('instr="Match"') == 2, "content34 Match count"
    for new in C34_MATCH_ORDERED:
        text = text.replace('instr="Match"', new, 1)
    assert 'instr="Match"' not in text
    open(path, "w", encoding="utf-8").write(text)

# ---------------------------------------------------------------- content56 (P5+P6)
C56 = [
    ("青年 · Youth", "青年 · Juventude", 1),
    ("第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween recap and the travel-fair game plan",
     "第 5 版 · 天母萬聖節回顧、旅展攻略 · Retrospectiva de Halloween e o plano para a feira de viagens", 1),
    ("Tianmu's Halloween (Oct 25-26, postponed from Oct 24 by the typhoon): the Oct 25 night parade marched from Shin Kong Mitsukoshi Tianmu along Zhongcheng Road to Dayeh Takashimaya, and the Oct 26 main event ran 13:00-20:00 at Tianmu Sports Park, with 250 shops giving treats and 4,500 pumpkin buckets from three department stores.",
     "O Halloween de Tianmu (25 e 26 de outubro, adiado de 24 de outubro por causa do tufão): o desfile noturno de 25 de outubro marchou da Shin Kong Mitsukoshi Tianmu pela rua Zhongcheng até a Dayeh Takashimaya, e o evento principal de 26 de outubro durou das 13:00 às 20:00 no Parque Esportivo de Tianmu, com 250 lojas distribuindo doces e 4.500 baldes de abóbora de três lojas de departamento.", 1),
    ("Travel-fair game plan: watch the shows first (Yamagata flower-hat dance, Korea's JUMP taekwondo-comedy show, the daily 14:00 mascot parade), then compare prices — budget fares often exclude checked baggage, so add that cost before you decide.",
     "Plano para a feira de viagens: assista primeiro aos espetáculos (dança do chapéu de flores de Yamagata, espetáculo JUMP de taekwondo e comédia da Coreia, desfile diário de mascotes às 14:00) e depois compare os preços — tarifas econômicas muitas vezes excluem a bagagem despachada, por isso some esse custo antes de decidir.", 1),
    ("Practice numbers: NT$6,200 − NT$1,200 = NT$5,000, exactly his budget.",
     "Números do exemplo: NT$ 6.200 − NT$ 1.200 = NT$ 5.000, exatamente o orçamento dele.", 1),
    ("The night parade marched on Sunday, Oct 25, at 19:00.", "O desfile noturno marchou no domingo, 25 de outubro, às 19:00.", 1),
    ("The main event ran 13:00-20:00 at Tianmu Sports Park.", "O evento principal durou das 13:00 às 20:00 no Parque Esportivo de Tianmu.", 1),
    ("250 shops gave treats.", "250 lojas distribuíram doces.", 1),
    ("4,500 pumpkin buckets were given out.", "Foram distribuídos 4.500 baldes de abóbora.", 1),
    ("The mascot parade runs daily at 14:00.", "O desfile de mascotes acontece todos os dias às 14:00.", 1),
    ("Budget fares often exclude checked baggage.", "Tarifas econômicas muitas vezes excluem a bagagem despachada.", 1),
    ("The parade marched along Zhongcheng Road.", "O desfile marchou pela rua Zhongcheng.", 1),
    ("The Tamagotchi 30th anniversary collaboration.", "A colaboração do 30.º aniversário do Tamagotchi.", 1),
    ("The Yamagata flower-hat dance performs on stage.", "A dança do chapéu de flores de Yamagata se apresenta no palco.", 1),
    ("Set a budget before Double 11.", "Defina um orçamento antes do Duplo 11.", 1),
    ("Add baggage fees before comparing fares.", "Some as taxas de bagagem antes de comparar as tarifas.", 1),
    ("List your cart first, then delete what you do not need.", "Liste seu carrinho primeiro e depois apague o que você não precisa.", 1),
    ("6,200 − 1,200 = 5,000, exactly the budget.", "6.200 − 1.200 = 5.000, exatamente o orçamento.", 1),
    ("The parade starts at 19:00; the main event the next day at 13:00.", "O desfile começa às 19:00; o evento principal, no dia seguinte, às 13:00.", 1),
    ("討糖 — trick-or-treating.", "討糖 — pedir doces no Halloween.", 1),
    ("踩街 — parading through the streets in costume.", "踩街 — desfilar pelas ruas fantasiado.", 1),
    ("南瓜桶 — a pumpkin bucket for treats.", "南瓜桶 — um balde de abóbora para doces.", 1),
    ("打卡 — checking in with a photo on social media.", "打卡 — registrar-se com uma foto nas redes sociais.", 1),
    ('instr="Match"', 'instr="Associe palavra e definição"', 1),
    ("天母時間表 · Tianmu schedule", "天母時間表 · Horário de Tianmu", 1),
    ("Have you ever worn a Halloween costume? Which character would you most want to be?", "Você já usou uma fantasia de Halloween? Que personagem você mais gostaria de ser?", 1),
    ("旅展表演 · Stage shows", "旅展表演 · Espetáculos", 1),
    # P6
    ("深讀 · Deep read", "深讀 · Leitura a fundo", 1),
    ("第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in depth, and reading a chart",
     "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech a fundo e leitura de gráficos", 1),
    ("Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
     "Reportagem da redação · Fonte: comunicado de imprensa dos organizadores (23 de outubro) e perguntas frequentes do evento", 1),
    ("Three plus signs: Finance+ (finance plus technology), AI+ (artificial intelligence inside banks, investment and insurance) and global expansion (helping start-ups sell worldwide). The scale — 45,000+ people, 120+ economies, 1,000+ speakers, 800+ exhibitors and start-ups, 30+ delegations, 100+ community events — shows fintech is now a whole-city topic.",
     "Três sinais de mais: Finanças+ (finanças mais tecnologia), IA+ (inteligência artificial dentro de bancos, investimentos e seguros) e expansão global (ajudar startups a vender no mundo todo). A escala — mais de 45.000 pessoas, mais de 120 economias, mais de 1.000 palestrantes, mais de 800 expositores e startups, mais de 30 delegações, mais de 100 eventos comunitários — mostra que a fintech agora é um tema da cidade inteira.", 1),
    ("旅展每日開放時數 · ITF opening hours per day — bars drawn in proportion to hours",
     "旅展每日開放時數 · Horas de abertura da ITF por dia — barras proporcionais às horas", 1),
    ("Source: published fair hours (Nov 6: 12:00-18:00; Nov 7-9: 10:00-18:00). Total: 30 hours.",
     "Fonte: horários publicados da feira (6 de novembro: 12:00–18:00; 7 a 9 de novembro: 10:00–18:00). Total: 30 horas.", 1),
    ("Nov 6 is the shortest day: 6 hours.", "6 de novembro é o dia mais curto: 6 horas.", 1),
    ("Nov 8 runs 10:00-18:00: 8 hours.", "8 de novembro vai das 10:00 às 18:00: 8 horas.", 1),
    ("6 + 8 + 8 + 8 = 30 hours in total.", "6 + 8 + 8 + 8 = 30 horas no total.", 1),
    ("Nov 6 opens at noon, not 10:00.", "6 de novembro abre ao meio-dia, não às 10:00.", 1),
    ("Finance+ means finance plus technology.", "Finanças+ significa finanças mais tecnologia.", 1),
    ("AI helps read data, spot risks and answer clients.", "A IA ajuda a ler dados, detectar riscos e responder aos clientes.", 1),
    ("Global expansion means selling products worldwide.", "A expansão global significa vender produtos no mundo todo.", 1),
    ("More than 1,000 speakers take part.", "Participam mais de 1.000 palestrantes.", 1),
    ("The main conference runs Nov 2-3.", "A conferência principal dura os dias 2 e 3 de novembro.", 1),
    ("Community events number 100+ through the week.", "Os eventos comunitários são mais de 100 ao longo da semana.", 1),
    ("Payments is one of the main-conference topics.", "Pagamentos é um dos temas da conferência principal.", 1),
    ("Digital assets is a main-conference topic.", "Ativos digitais são um tema da conferência principal.", 1),
    ("Insurtech is a main-conference topic.", "Insurtech é um tema da conferência principal.", 1),
    ("The week connects start-ups with the world.", "A semana conecta startups com o mundo.", 1),
    ("Total opening hours: 30.", "Total de horas de abertura: 30.", 1),
    ("Nov 6 opens at noon (12:00).", "6 de novembro abre ao meio-dia (12:00).", 1),
    ("The travel fair has 1,600 booths.", "A feira de viagens tem 1.600 estandes.", 1),
    ("More than 45,000 people are expected.", "São esperadas mais de 45.000 pessoas.", 1),
    ("數字一覽 · By the numbers", "數字一覽 · Os números", 1),
    ("比價提醒 · Compare carefully", "比價提醒 · Compare com cuidado", 1),
    ("Example from press reports (Oct 20): Cathay Pacific Taipei-Tokyo return from NT$13,433 including tax, book by Nov 13. Always compare with baggage fees added — and check the live booking result, as prices vary by date.",
     "Exemplo de reportagens (20 de outubro): passagem de ida e volta Taipé–Tóquio da Cathay Pacific a partir de NT$ 13.433 com impostos incluídos, reserve até 13 de novembro. Compare sempre somando as taxas de bagagem — e confira o resultado da reserva ao vivo, pois os preços variam conforme a data.", 1),
    ("讀懂了嗎? · Did you get it?", "讀懂了嗎? · Entendeu?", 1),
    ("填一填 · Fill in", "填一填 · Complete", 2),
    ("算一算 · Work it out", "算一算 · Faça as contas", 1),
    ("看圖答題 · Read the chart", "看圖答題 · Leia o gráfico", 1),
    ("深讀測驗 · Deep-read quiz", "深讀測驗 · Quiz a fundo", 1),
    ("練習例子 · Practice example", "練習例子 · Exemplo prático", 1),
    ("你呢? · Over to you", "你呢? · E você?", 1),
    ('instr="Fill in"', 'instr="Complete"', 14),
]

# ---------------------------------------------------------------- content7 (P7)
C7 = [
    ("語言 · Language focus", "語言 · Foco linguístico", 1),
    ("語言聚焦 · 三個級別,三個主題 · Three levels, three topics",
     "語言聚焦 · 三個級別,三個主題 · Três níveis, três temas", 1),
    ("A2 · 展會的話 · Fair words", "A2 · 展會的話 · Palavras da feira", 1),
    ("This week's fairs give you four useful words: 旅展 (travel fair), 攤位 (booth), 集章 (stamp-collecting) and 吉祥物大遊行 (mascot parade). Learn them once, and the whole travel fair makes sense.",
     "As feiras desta semana trazem quatro palavras úteis: 旅展 (feira de viagens), 攤位 (estande), 集章 (colecionar carimbos) e 吉祥物大遊行 (desfile de mascotes). Aprenda-as uma vez e toda a feira de viagens fará sentido.", 1),
    ("Four fair words: 旅展, 攤位, 集章, 吉祥物大遊行.", "Quatro palavras da feira: 旅展, 攤位, 集章, 吉祥物大遊行.", 1),
    ("旅展 is short for 旅行展覽會 (travel exhibition). A 攤位 is one stall inside the fair; the Taipei fair has 1,600 of them. 集章 means collecting stamps at set points — collect all six Greenway stamps and you win a prize.",
     "旅展 é a forma curta de 旅行展覽會 (exposição de viagens). Um 攤位 é um estande dentro da feira; a feira de Taipé tem 1.600 deles. 集章 significa colecionar carimbos em pontos determinados — colecione os seis carimbos das Trilhas Verdes e você ganhará um prêmio.", 1),
    ("Practise: 「旅展幾點開門？」 ('What time does the fair open?') — Friday opens at noon, other days at 10:00.",
     "Pratique: 「旅展幾點開門？」 («A que horas a feira abre?») — sexta-feira abre ao meio-dia e nos outros dias às 10:00.", 1),
    ("A booth inside the fair is a 攤位.", "Um estande dentro da feira é um 攤位.", 1),
    ("The mascot parade runs daily at 14:00.", "O desfile de mascotes acontece todos os dias às 14:00.", 1),
    ("Collecting stamps at set points is 集章.", "Colecionar carimbos em pontos determinados é 集章.", 1),
    ("The travel fair is at the Nangang Exhibition Center.", "A feira de viagens é no Centro de Exposições de Nangang.", 1),
    ("B1 · 球賽與節氣 · Games & seasons", "B1 · 球賽與節氣 · Jogos e estações", 1),
    ("Sport and seasons share this week's headlines. Group the words and they stick: winning （封王、完封） and winter （立冬、進補）.",
     "Esporte e estações dividem as manchetes desta semana. Agrupe as palavras e elas fixam: vencer （封王、完封） e inverno （立冬、進補）.", 1),
    ("Group the words: winning (封王/完封), winter (立冬/進補).", "Agrupe as palavras: vencer (封王/完封), inverno (立冬/進補).", 1),
    ("封王 means clinching the championship; 完封 means shutting the other side out, 0 runs. 立冬 is the solar term that starts winter; 進補 is eating nourishing hot food before the cold months.",
     "封王 significa conquistar o campeonato; 完封 significa não deixar o adversário marcar, 0 pontos. 立冬 é o termo solar que inicia o inverno; 進補 é comer alimentos quentes e nutritivos antes dos meses frios.", 1),
    ("Memory trick: learn 封王 first, then the way it was won （完封）, then the season it happened in （立冬）.",
     "Truque de memória: aprenda 封王 primeiro, depois o jeito como foi vencido （完封） e depois a estação em que aconteceu （立冬）.", 1),
    ("Winning the title is 封王.", "Conquistar o título é 封王.", 1),
    ("完封 means the other side scores zero.", "完封 significa que o adversário marca zero.", 1),
    ("Lidong starts winter.", "Lidong inicia o inverno.", 1),
    ("Ginger duck is a Lidong dish.", "Pato com gengibre é um prato do Lidong.", 1),
    ("B2 · 港台說法 · Local talk", "B2 · 港台說法 · Jeito local de falar", 1),
    ("Taiwan and Hong Kong each have their own way of saying things. This week: 打卡 (check in with a photo), 討糖 (trick-or-treat), 踩街 (street parade in costume) and 泡湯 (soak in a hot spring).",
     "Taiwan e Hong Kong têm, cada um, seu jeito de dizer as coisas. Esta semana: 打卡 (registrar-se com uma foto), 討糖 (pedir doces no Halloween), 踩街 (desfile de rua fantasiado) e 泡湯 (banho em águas termais).", 1),
    ("Four local words from this issue: 打卡, 討糖, 踩街, 泡湯.", "Quatro palavras locais desta edição: 打卡, 討糖, 踩街, 泡湯.", 1),
    ("打卡 started as clocking in at work, but at a fair or festival it means posting a photo to say 'I was here'. 討糖 is what children say at shops at Halloween; 踩街 is the costumed parade itself; 泡湯 is the autumn pleasure of a hot-spring bath.",
     "打卡 começou como bater o ponto no trabalho, mas em uma feira ou festival significa postar uma foto para dizer 'estive aqui'. 討糖 é o que as crianças dizem nas lojas no Halloween; 踩街 é o próprio desfile fantasiado; 泡湯 é o prazer outonal de um banho em águas termais.", 1),
    ("You don't need many local sayings — learn four and every outing feels closer.", "Você não precisa de muitas expressões locais — aprenda quatro e cada passeio parecerá mais próximo.", 1),
    ("At a festival, 打卡 means posting a photo to say you were there.", "Em um festival, 打卡 significa postar uma foto para dizer que você esteve lá.", 1),
    ("Trick-or-treating is 討糖.", "Pedir doces no Halloween é 討糖.", 1),
    ("踩街 is a costumed street parade.", "踩街 é um desfile de rua fantasiado.", 1),
    ("Soaking in a hot spring is 泡湯.", "Banho em águas termais é 泡湯.", 1),
    ("易錯診所 · Error clinic", "易錯診所 · Clínica de erros", 1),
    ("完勝 means winning big; 完封 means the other side scored zero.", "完勝 significa vencer com folga; 完封 significa que o adversário marcou zero.", 1),
    ("Lidong starts winter; the Solstice is the shortest day. Different terms.", "Lidong inicia o inverno; o Solstício é o dia mais curto. Termos diferentes.", 1),
    ("Check the city: FinTech Week opens in Hong Kong, not Taipei.", "Confira a cidade: a Semana FinTech abre em Hong Kong, não em Taipé.", 1),
    ("本週句式 · Sentence frame", "本週句式 · Estrutura da semana", 1),
    # Substring pair (same mechanism as the es map): the sentence-frame
    # para's English tail, replaced inside the longer Chinese-led literal.
    (" — the frame 先…再… gives the order of two actions: first X, then Y. Make your own: 先比價，再結帳 (compare prices first, then pay).",
     " — a estrutura 先…再… indica a ordem de duas ações: primeiro X, depois Y. Crie a sua: 先比價，再結帳 (compare os preços primeiro e pague depois).", 1),
    ("Frame: 先…再… — first X, then Y. Make your own sentence with it.", "Estrutura: 先…再… — primeiro X, depois Y. Crie sua própria frase com ela.", 1),
    ("讀者園地 · Readers' corner", "讀者園地 · Cantinho do leitor", 1),
    ("An editor's example letter — not a real one. Deferral notice: VOL.1 promised real letters and best page-8 writing from this issue; none publishable had arrived by press time, so the example stays and the invitation stays open.",
     # Shortened by wording (6 wrap lines, = the English disclosure): the
     # fuller form wrapped to 7 lines and its last line crossed the
     # readers'-corner box border by 5.9px (audit BOXTITLE). Still states
     # no genuine letters arrived and the invitation stays open.
     "Carta de exemplo da redação, não uma carta real. Aviso: o VOL.1 prometeu cartas reais e a melhor redação da página 8 desde esta edição; até o fechamento nenhuma publicável chegou, por isso o exemplo fica e o convite continua aberto.", 1),
    ("本週金句 · Phrases of the week — word for word from this issue's articles",
     "本週金句 · Frases da semana — palavra por palavra dos artigos desta edição", 1),
    ("Pay by phone, scan to pay, buy insurance online — that is fintech.", "Pagar pelo celular, escanear para pagar, comprar seguro on-line — isso é fintech.", 1),
    ("123 countries and cities, 1,600 booths.", "123 países e cidades, 1.600 estandes.", 1),
    ("Buy what you need; don't buy a pile of things you won't use just for a discount.", "Compre o que você precisa; não compre um monte de coisas que não vai usar só por causa de um desconto.", 1),
    ("In Kaohsiung, even steel can become a stage.", "Em Kaohsiung, até o aço pode virar palco.", 1),
    ("Fulong's summer came to an end on October 26.", "O verão de Fulong chegou ao fim em 26 de outubro.", 1),
    ("A 6-0 shutout of the Brothers, and the Dragons threw the red ribbons.", "Um 6 a 0 sem sofrer pontos contra os Brothers, e os Dragons jogaram as fitas vermelhas.", 1),
    ("250 shops giving treats together.", "250 lojas distribuindo doces juntas.", 1),
    ("On the fair's first day the doors open only at noon.", "No primeiro dia da feira, as portas abrem só ao meio-dia.", 1),
    ("下期預告 · Next week (VOL.3)", "下期預告 · Na próxima semana (VOL.3)", 1),
    ('instr="Fill in"', 'instr="Complete"', 6),
]

# ---------------------------------------------------------------- content8 (P8)
C8 = [
    ("測驗與答案 · Test & keys", "測驗與答案 · Teste e respostas", 1),
    ("第 8 版 · 本週大測驗 + 全部答案 · This week's test and every answer key",
     "第 8 版 · 本週大測驗 + 全部答案 · O teste da semana e todas as respostas", 1),
    ("A · 判斷對錯 · True or false", "A · 判斷對錯 · Verdadeiro ou falso", 1),
    ("B · 本週大測驗 · The big quiz", "B · 本週大測驗 · O grande quiz", 1),
    ("C · 完成句子 · Fill in", "C · 完成句子 · Complete as frases", 1),
    ("D · 讀一讀,答一答 · Read and answer", "D · 讀一讀,答一答 · Leia e responda", 1),
    ("E · 情景說話 · Say it in context", "E · 情景說話 · Diga no contexto", 1),
    ("F · 寫一寫 · Writing", "F · 寫一寫 · Redação", 1),
    ("FinTech Week opens Monday, Nov 2.", "A Semana FinTech abre na segunda-feira, 2 de novembro.", 1),
    ("Lidong is Nov 7, not Nov 6.", "Lidong é em 7 de novembro, não em 6 de novembro.", 1),
    ("The Dragons won the series 4-2.", "Os Dragons venceram a série por 4 a 2.", 2),
    ("Game 6 ended 6-0, not 6-3.", "O 6.º jogo terminou 6 a 0, não 6 a 3.", 1),
    ("The sand festival closed Oct 26.", "O festival de areia encerrou em 26 de outubro.", 1),
    ("The travel fair opens at noon on Nov 6, not 10:00.", "A feira de viagens abre ao meio-dia em 6 de novembro, não às 10:00.", 1),
    ("The main conference is Nov 2-3.", "A conferência principal é nos dias 2 e 3 de novembro.", 1),
    ("The travel fair runs to Monday, Nov 9.", "A feira de viagens vai até segunda-feira, 9 de novembro.", 1),
    ("The steel festival runs to Nov 22.", "O festival do aço vai até 22 de novembro.", 1),
    ("The night parade marched Oct 25 at 19:00.", "O desfile noturno marchou em 25 de outubro às 19:00.", 1),
    ("Double 11 is Wednesday, Nov 11.", "O Duplo 11 é quarta-feira, 11 de novembro.", 1),
    ("Mercedes allowed 1 run in 14 innings.", "Mercedes cedeu 1 ponto em 14 entradas.", 1),
    ("The mascot parade runs daily at 14:00.", "O desfile de mascotes acontece todos os dias às 14:00.", 1),
    ("The trail encyclopaedia collects 56 routes.", "A enciclopédia de trilhas reúne 56 rotas.", 1),
    ("Total opening hours: 6 + 8 + 8 + 8 = 30.", "Total de horas de abertura: 6 + 8 + 8 + 8 = 30.", 1),
    ("The stamp challenge covers 6 Greenways.", "O desafio de carimbos abrange 6 Trilhas Verdes.", 1),
    ("Fintech: technology running financial services.", "Fintech: a tecnologia gerindo serviços financeiros.", 1),
    ("Lidong starts winter.", "Lidong inicia o inverno.", 1),
    ("A shutout: the other side scores zero.", "Um jogo sem sofrer pontos: o adversário marca zero.", 1),
    ("Winning the title is 封王.", "Conquistar o título é 封王.", 1),
    ("Trick-or-treating is 討糖.", "Pedir doces no Halloween é 討糖.", 1),
    ("Collecting stamps is 集章.", "Colecionar carimbos é 集章.", 1),
    ("The travel fair is at the Nangang Exhibition Center.", "A feira de viagens é no Centro de Exposições de Nangang.", 1),
    ("Pier-2 hosts the steel festival.", "O Pier-2 sedia o festival do aço.", 1),
    ("Global expansion: selling products worldwide.", "A expansão global significa vender produtos no mundo todo.", 1),
    # AI-variant form: SEPARATE string from the P6 gloss's AI+ explanation
    # (content56) — translated here on its own, never assumed covered.
    ("AI inside finance is 人工智慧＋.", "IA dentro das finanças é 人工智慧＋.", 1),
    ("He goes to the travel fair on Friday at noon.", "Ele vai à feira de viagens na sexta-feira ao meio-dia.", 1),
    ("The parade is at 14:00.", "O desfile é às 14:00.", 1),
    ("A set of 4 coupons costs 4,100 (list price 8,200).", "Um conjunto de 4 cupons custa 4.100 (preço de lista 8.200).", 1),
    ("He eats ginger duck for Lidong on Saturday.", "Ele come pato com gengibre no Lidong no sábado.", 1),
    ("Order: fair, then Lidong pot, then the coupon set for a buffet.", "Ordem: feira, depois panela do Lidong e depois o conjunto de cupons para um bufê.", 1),
    ("The travel fair opens Friday at noon.", "A feira de viagens abre na sexta-feira ao meio-dia.", 1),
    ("Lidong is the first solar term of winter.", "Lidong é o primeiro termo solar do inverno.", 1),
    ("A shutout means the other side scores zero.", "Um jogo sem sofrer pontos significa que o adversário marca zero.", 1),
    ("The mascot parade is at 14:00 daily.", "O desfile de mascotes é às 14:00 todos os dias.", 1),
    ("Compare prices first, then pay: 先比價，再結帳.", "Compare os preços primeiro e pague depois: 先比價，再結帳.", 1),
    ('f"Writing — there is no single right answer. A {NCHARS}-character model follows."',
     'f"Redação — não há uma única resposta certa. Segue um modelo de {NCHARS} caracteres."', 1),
    ('"(開放題,範文如下)"', '"(pergunta aberta — modelo abaixo)"', 1),
    ('f"Open task - the model answer is printed in section F above ({NCHARS} characters)"',
     'f"Pergunta aberta — o modelo está impresso acima, na seção F ({NCHARS} caracteres)"', 1),
    ('instr="Writing"', 'instr="Redação"', 1),
    ('"Model answer: " + MODELO', '"Resposta modelo: " + MODELO', 1),
    ("答案 · Answer keys — in page order, with a short English note for every item",
     "答案 · Respostas — em ordem de páginas, com uma nota breve em português para cada exercício", 1),
    ("All notes in English · ✓ = the writing model", "Todas as notas em português · ✓ = o modelo de redação", 1),
    ('f"— Page {pg} —"', 'f"— Página {pg} —"', 1),
    ('instr="Fill in"', 'instr="Complete"', 10),
]

# P8 key typography: paren style per the W43 zh-tw-pt family's shipped code
# (half-width parens with a space before the note parenthesis; key lines
# bypass svglib._fw's pair conversion, which would otherwise full-width the
# parens whenever the note contains a Chinese term). Core font/lh kept.
C8_KEYS_OLD = '''    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.8, "sans", False, INK, lh=1.12, gap=1, split=False)'''
C8_KEYS_NEW = '''    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} ({e_['note']})"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ ({e_['note']})"
        af.para(txt, 12.8, "sans", False, INK, lh=1.12, gap=1, split=False)'''


def apply7_fix(dest):
    # P7 readers'-corner interior gap fix (CORE FORMULA DEFECT, documented):
    # the core's lh formula underestimates this box by ~11px: the core
    # render itself (identical box y=1184.86 h=560.5, identical last-line
    # baseline 1751.63) has its last disclosure line struck through by
    # the box bottom border on the card crop, escaping the audit only
    # because its last line's ink CENTRE sits 0.15px outside the box.
    # Wording shortening CANNOT fix it: lh is computed from the same
    # wrap() line count, so one fewer line shrinks the box by 29px while
    # the text rises only 28.4px (verified: gap ~11px at every line
    # count). The fix moves ONLY this box's interior text: the two +10
    # inter-para gaps after the (frozen) letter and disclosure paras
    # become +0, so the disclosure block rises 20px inside the UNCHANGED
    # box; col3_end, the phrases rule and the teaser do not move at all
    # (their positions stay byte-identical to the core's).
    path = os.path.join(dest, "content7.py")
    text = open(path, encoding="utf-8").read()
    text = rep(text,
               "yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, \"serif\", False, INK, CW - 44, 1.42) + 10",
               "yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, \"serif\", False, INK, CW - 44, 1.42)",
               1, "content7.py readers-gap-lt")
    text = rep(text,
               "yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, \"serif\", False, INK, CW - 44, 1.42) + 10",
               "yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, \"serif\", False, INK, CW - 44, 1.42)",
               1, "content7.py readers-gap-lt2")
    open(path, "w", encoding="utf-8").write(text)


def apply_all(dest, svg_dir, delivery_dir):
    apply_file(dest, "bslib4.py", BSLIB)
    apply_file(dest, "content12.py", C12)
    apply34(dest)
    apply_file(dest, "content56.py", C56)
    apply_file(dest, "content7.py", C7)
    apply7_fix(dest)
    apply_file(dest, "content8.py", C8)
    path = os.path.join(dest, "content8.py")
    text = open(path, encoding="utf-8").read()
    text = rep(text, C8_KEYS_OLD, C8_KEYS_NEW, 1, "content8.py keys")
    # _fw bypass around the keys flow only (es-sibling precedent on this
    # core; W43 zh-tw-pt's own code prints paren style the same way).
    old_flow = "af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag=\"P8-keys\")"
    new_flow = ("import svglib as _sg, re as _re\n_orig_fw = _sg._fw\n"
                "def _fw_keys(s):\n"
                "    if _re.match(r\"^\\d+\\. \", s):\n"
                "        return s\n"
                "    return _orig_fw(s)\n"
                "_sg._fw = _fw_keys\n" + old_flow)
    text = rep(text, old_flow, new_flow, 1, "content8.py fw-bypass")
    text = rep(text, "af.end_report()\np.foot(8)",
               "af.end_report()\n_sg._fw = _orig_fw\np.foot(8)", 1, "content8.py fw-restore")
    open(path, "w", encoding="utf-8").write(text)
    repoint(dest, svg_dir, delivery_dir)


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    gate10 = "--gate10" in sys.argv
    if gate10:
        dest = os.path.join(GOAL, "hidden_files/w45-zh-tw-pt-gate10")
        svg_dir = os.path.join(dest, "svg")
        fresh_copy(dest)
        os.makedirs(svg_dir, exist_ok=True)
        apply_all(dest, MY_SVG_PATH, dest)
        # Repoint OUT to the temp svg dir by replacing the WHOLE
        # expanduser(...) expression with the absolute path. (A plain
        # substring swap of the relative svg path would splice the
        # absolute dir inside the ~/workspace/... prefix and write to a
        # nested junk path — the es template's gate10 has this latent
        # bug; it is fixed here, not copied.)
        for fname in ["content12.py", "content34.py", "content56.py",
                      "content7.py", "content8.py"]:
            path = os.path.join(dest, fname)
            text = open(path, encoding="utf-8").read()
            text2 = re.sub(r"os\.path\.expanduser\(\"[^\"]*\"\)",
                           f"\"{svg_dir}\"", text, count=1)
            assert text2 != text, f"{fname}: OUT expanduser not found"
            open(path, "w", encoding="utf-8").write(text2)
        venv = os.path.join(GOAL, "tools/venv/bin/python")
        r = subprocess.run([venv, os.path.join(dest, "run.py")],
                           cwd=dest, capture_output=True, text=True)
        print(r.stdout)
        print(r.stderr, file=sys.stderr)
        assert r.returncode == 0, "gate10 driver failed"
        warns = [ln for ln in (r.stdout + r.stderr).splitlines()
                 if "FLOW OVERFLOW" in ln or "HEAD TOO WIDE" in ln
                 or "TOO WIDE" in ln]
        names = ["p1-front.svg", "p2-life.svg", "p3-culture.svg", "p4-sport.svg",
                 "p5-youth.svg", "p6-deep.svg", "p7-lang.svg", "p8-test.svg"]
        ok = 0
        for n in names:
            a = sha(os.path.join(svg_dir, n))
            b = sha(os.path.join(DELIVERY, "svg", n))
            match = (a == b)
            ok += match
            print(f"gate10 {n}: {'IDENTICAL' if match else 'DIFF ' + a + ' vs ' + b}")
        print(f"GATE10: {ok}/8 byte-identical, warnings={len(warns)} {warns}")
        sys.exit(0 if ok == 8 and not warns else 1)
    else:
        fresh_copy(MYBUILD)
        apply_all(MYBUILD, MY_SVG_PATH, DELIVERY)
        print("transform applied to", MYBUILD)


if __name__ == "__main__":
    main()
