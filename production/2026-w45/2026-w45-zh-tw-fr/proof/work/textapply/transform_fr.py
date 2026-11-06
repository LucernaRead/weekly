# -*- coding: utf-8 -*-
"""W45 zh-tw x FR fan-out transform. Runs IN the build copy dir (its own
directory): repoints OUT/BASE to the FR edition dir, then rewrites ONLY the
explanation layer (English -> French) with exact-count asserted literal
replacements. Target Traditional Chinese text is never touched. Follows
tools/README rules #17 (whole-literal splicing, never AST byte offsets)
and #18 (f-string fragments get bare text, placeholders preserved).
Usage: python transform_fr.py  (idempotent guard: aborts if already applied)
Gate 10: fresh core copy + this script alone + run.py + render.py must
reproduce the delivered SVGs 8/8 byte-identical."""
import os, sys

BUILD = os.path.dirname(os.path.abspath(__file__))
ED = "weekly-report-w45-zh-tw-fr"
CORE = "weekly-report-w45-zhtw-core"

def load(f):
    with open(os.path.join(BUILD, f), encoding="utf-8") as fh:
        return fh.read()

def save(f, s):
    with open(os.path.join(BUILD, f), "w", encoding="utf-8") as fh:
        fh.write(s)

def rep(f, old, new, n):
    s = load(f)
    c = s.count(old)
    assert c == n, f"{f}: {old[:60]!r} found {c}, expected {n}"
    save(f, s.replace(old, new))

def repoint():
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "render.py"]:
        rep(f, CORE, ED, 1)

def bslib():
    rep("bslib4.py",
        "Lucerna · 繁體中文週報 VOL.2 · 繁體中文正文 · 英語講解 · Traditional Chinese text · English explanations",
        "Lucerna · HEBDOMADAIRE CHINOIS VOL.2 · TEXTE EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS", 1)
    rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"', 1)
    rep("bslib4.py", '"Notes｜" + s', '"Note — " + s', 1)

R12 = [
    ('p.text(975, 378, "繁體中文正文 · 英語講解 — Traditional Chinese text · Explanations in English · the edition for English-speaking readers", 21, "sans", True, OLIVE, anchor="middle")',
     'p.text(975, 378, "TEXTES EN CHINOIS TRADITIONNEL · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES", 21, "sans", True, BRICK, anchor="middle")', 1),
    ("Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
     "Dépêche de la rédaction · Source : communiqué des organisateurs (23 oct.) et FAQ de l'événement", 1),
    ("Hong Kong FinTech Week x StartmeupHK 2026 opens Monday (Nov 2) and runs to Friday (Nov 6). The main conference and exhibition are at the Hong Kong Convention and Exhibition Centre on Nov 2-3, with 100+ community events through the week. Expect 45,000+ people from 120+ economies, 1,000+ speakers and 800+ exhibitors and start-ups.",
     "La Semaine FinTech de Hong Kong x StartmeupHK 2026 ouvre le lundi (2 nov.) et se poursuit jusqu'au vendredi (6 nov.). La conférence principale et l'exposition se tiennent au Centre des congrès et des expositions de Hong Kong les 2-3 nov., avec plus de 100 événements communautaires sur la semaine. Attendez-vous à plus de 45 000 personnes de plus de 120 économies, 1 000 intervenants et 800 exposants et jeunes entreprises.", 1),
    ("The Taipei International Travel Fair (ITF) opens Friday (Nov 6) at noon at the Nangang Exhibition Center and runs to Monday (Nov 9): 123 countries and cities, 1,600 booths, a daily 14:00 mascot parade and travel talks.",
     "Le Salon international du voyage de Taipei (ITF) ouvre le vendredi (6 nov.) à midi au Centre des expositions de Nangang et se poursuit jusqu'au lundi (9 nov.) : 123 pays et villes, 1 600 stands, un défilé quotidien des mascottes à 14 h 00 et des conférences de voyage.", 1),
    ("本週大事 · This week", "本週大事 · Cette semaine", 1),
    ("本週一詞 · Word of the week", "本週一詞 · Le mot de la semaine", 1),
    ("「金融科技」 — fintech: using technology to run financial services, like paying by phone or scanning a code to pay.",
     "「金融科技」 — la fintech : utiliser la technologie pour faire fonctionner les services financiers, comme payer par téléphone ou scanner un code pour payer.", 1),
    ("快速測驗 · Quick quiz", "快速測驗 · Quiz rapide", 1),
    ("標題填空 · Headline words", "標題填空 · Mots des titres", 1),
    ("FinTech Week opens on Monday, Nov 2.", "La Semaine FinTech ouvre le lundi 2 nov.", 1),
    ("The main conference is at the Hong Kong Convention and Exhibition Centre.", "La conférence principale se tient au Centre des congrès et des expositions de Hong Kong.", 1),
    ("More than 45,000 people are expected.", "Plus de 45 000 participants sont attendus.", 1),
    ("The travel fair opens Friday, Nov 6, at noon.", "Le salon du voyage ouvre le vendredi 6 nov. à midi.", 1),
    ("Participants come from 120+ economies.", "Les participants viennent de plus de 120 économies.", 1),
    ("More than 800 exhibitors and start-ups take part.", "Plus de 800 exposants et jeunes entreprises y participent.", 1),
    ("The travel fair gathers 123 countries and cities.", "Le salon du voyage réunit 123 pays et villes.", 1),
    ("The travel fair has 1,600 booths.", "Le salon du voyage compte 1 600 stands.", 1),
    ("Saturday, Nov 7 is the Start of Winter solar term.", "Le samedi 7 nov., c'est le début de l'hiver (Lidong).", 1),
    ("The travel fair runs to Monday, Nov 9.", "Le salon du voyage se poursuit jusqu'au lundi 9 nov.", 1),
    ("第 2 版 · 天氣、泡湯、旅展與雙11 · Weather, hot springs, the travel fair and 11.11",
     "第 2 版 · 天氣、泡湯、旅展與雙11 · Météo, sources chaudes, salon du voyage et Double 11", 1),
    ("The northeast monsoon cools northern Taiwan, and Saturday (Nov 7) is Lidong, the Start of Winter: the day winter begins in the 24 solar terms. Many people mark it with a hot, nourishing pot meal.",
     "La mousson du nord-est rafraîchit le nord de Taïwan, et le samedi (7 nov.) c'est Lidong, le début de l'hiver : le jour où l'hiver commence dans les 24 termes solaires. Beaucoup marquent ce jour par un repas de fondue chaud et nourrissant.", 1),
    ("Autumn and winter are for hot springs and hiking. The travel fair's trail encyclopaedia collects 56 routes, and the 6 Greenways stamp challenge covers the Tamsui-Kavalan, Raknus Selu, Mountain-to-Sea, Centenary, Indigenous and Sugar-Rail trails.",
     "L'automne et l'hiver sont faits pour les sources chaudes et la randonnée. L'encyclopédie des sentiers du salon du voyage réunit 56 itinéraires, et le défi des tampons des 6 voies vertes couvre les sentiers Tamsui-Kavalan, Raknus Selu, Montagne-à-Mer, Centenaire, Autochtone et Rail sucrier.", 1),
    ("練習例子 · Practice example", "練習例子 · Exemple d'exercice", 1),
    ("Practice numbers: NT$2,400 + NT$1,600 = NT$4,000, exactly her budget — so she can buy both.",
     "Chiffres de l'exercice : 2 400 NT$ + 1 600 NT$ = 4 000 NT$, exactement son budget — elle peut donc acheter les deux.", 1),
    ("讀懂了嗎? · Did you get it?", "讀懂了嗎? · Tout compris ?", 1),
    ("Lidong, the Start of Winter, is Saturday, Nov 7.", "Lidong, le début de l'hiver, tombe le samedi 7 nov.", 1),
    ("The northeast monsoon cools northern Taiwan.", "La mousson du nord-est rafraîchit le nord de Taïwan.", 1),
    ("The trail encyclopaedia collects 56 routes.", "L'encyclopédie des sentiers réunit 56 itinéraires.", 1),
    ("The stamp challenge has 6 Greenways.", "Le défi des tampons compte 6 voies vertes.", 1),
    ("Double 11 falls on Wednesday, Nov 11.", "Le Double 11 tombe le mercredi 11 nov.", 1),
    ("Before paying, check tax, delivery and returns.", "Avant de payer, vérifiez les taxes, la livraison et les retours.", 1),
    ("填一填 · Fill in", "填一填 · Complétez", 1),
    ("A hot pot meal marks Lidong: 進補.", "Un repas de fondue marque Lidong : 進補.", 1),
    ("Check the jacket: mornings and evenings are cool.", "Pensez à la veste : matins et soirs sont frais.", 1),
    ("Autumn and winter are good for hot springs.", "L'automne et l'hiver sont propices aux sources chaudes.", 1),
    ("Collect stamps on the 6 Greenways.", "Collectionnez les tampons sur les 6 voies vertes.", 1),
    ("Set a budget before Double 11 shopping.", "Fixez un budget avant les achats du Double 11.", 1),
    ("The Tamsui-Kavalan Trail is one of the 6 Greenways.", "Le sentier Tamsui-Kavalan est l'une des 6 voies vertes.", 1),
    ("算一算 · Work it out", "算一算 · À vos calculs", 1),
    ("2,400 + 1,600 = 4,000, exactly the budget.", "2 400 + 1 600 = 4 000, exactement le budget.", 1),
    ("The budget is 4,000 and the total is 4,000: nothing over.", "Le budget est de 4 000 et le total de 4 000 : aucun dépassement.", 1),
    ("立冬 — the Start of Winter solar term.", "立冬 — le début de l'hiver.", 1),
    ("進補 — eating nourishing hot food for winter.", "進補 — manger des plats chauds et nourrissants pour l'hiver.", 1),
    ("泡湯 — soaking in a hot spring.", "泡湯 — se baigner dans une source chaude.", 1),
    ("集章 — collecting stamps at set points.", "集章 — collectionner les tampons à des points précis.", 1),
    ("事實框 · This week's facts", "事實框 · Les faits de la semaine", 1),
    ("你呢? · Over to you", "你呢? · À vous", 1),
    ("What hot pot would you eat for Lidong? What is in your Double 11 cart?", "Quelle fondue mangeriez-vous pour Lidong ? Que contient votre panier du Double 11 ?", 1),
    ("封王優惠 · Champion deals", "封王優惠 · Offres champions", 1),
    ('instr="Fill in"', 'instr="Complétez"', 12),
    ('instr="Match"', 'instr="Associez"', 1),
]

R34 = [
    ("第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, steel art and the sand festival finale",
     "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, art de l'acier et finale du festival de sable", 1),
    ("Lidong is the first solar term of winter: winter begins. People mark it with hot pot dishes like ginger duck, lamb hotpot and sesame chicken — warming food before the cold months.",
     "Lidong est le premier terme solaire de l'hiver : l'hiver commence. On le marque avec des fondues chaudes comme le canard au gingembre, la fondue d'agneau et le poulet au sésame — des plats réchauffants avant les mois froids.", 1),
    ("Kaohsiung's International Steel Sculpture Festival (Oct 23-Nov 22) turns warehouses, factories, the harbour and streets into a stage — SUPER STAGE — with an international forum on making, design and art in daily life.",
     "Le Festival international de sculpture sur acier de Kaohsiung (23 oct.-22 nov.) transforme entrepôts, usines, port et rues en scène — SUPER STAGE — avec un forum international sur la fabrication, le design et l'art dans la vie quotidienne.", 1),
    ("The Fulong International Sand Sculpture Art Festival closed Oct 26 after its 19th season (May 29-Oct 26): 40+ sculptures by 15+ artists, built from Fulong's golden sand around film characters from Jurassic World, Shrek, Kung Fu Panda and Back to the Future.",
     "Le Festival international de sculpture sur sable de Fulong s'est terminé le 26 oct. après sa 19e saison (29 mai-26 oct.) : plus de 40 sculptures de plus de 15 artistes, construites avec le sable doré de Fulong autour de personnages de Jurassic World, Shrek, Kung Fu Panda et Retour vers le futur.", 1),
    ("讀懂了嗎? · Did you get it?", "讀懂了嗎? · Tout compris ?", 2),
    ("Lidong means winter begins.", "Lidong signifie que l'hiver commence.", 1),
    ("Ginger duck is a typical Lidong dish.", "Le canard au gingembre est un plat typique de Lidong.", 1),
    ("The steel festival runs Oct 23-Nov 22.", "Le festival de l'acier se tient du 23 oct. au 22 nov.", 1),
    ("The venues include Pier-2's Penglai B3 warehouse.", "Les lieux comprennent l'entrepôt B3 de Penglai, à Pier-2.", 1),
    ("The sand festival closed on Oct 26.", "Le festival de sable s'est terminé le 26 oct.", 1),
    ("The sand festival made 40+ sculptures.", "Le festival de sable a produit plus de 40 sculptures.", 1),
    ("填一填 · Fill in", "填一填 · Complétez", 2),
    ("Lidong is a solar term (節氣).", "Lidong est un terme solaire (節氣).", 1),
    ("Sesame chicken is a Lidong dish.", "Le poulet au sésame est un plat de Lidong.", 1),
    ("Steel is Kaohsiung's material and memory.", "L'acier est la matière et la mémoire de Kaohsiung.", 1),
    ("Hamasen Railway Park is a venue.", "Le parc ferroviaire de Hamasen est l'un des lieux.", 1),
    ("Fulong's sand is golden.", "Le sable de Fulong est doré.", 1),
    ("Jurassic World is one of the film characters.", "Jurassic World est l'un des personnages de film.", 1),
    ("算一算 · Work it out", "算一算 · À vos calculs", 1),
    ("May 29-31 (3) + Jun 30 + Jul 31 + Aug 31 + Sep 30 + Oct 26 = 151 days.", "29-31 mai (3) + 30 juin + 31 juil. + 31 août + 30 sept. + 26 oct. = 151 jours.", 1),
    ("Oct 23-31 (9) + Nov 22 = 31 days.", "23-31 oct. (9) + 22 nov. = 31 jours.", 1),
    ("立冬 — the first solar term of winter.", "立冬 — le premier terme solaire de l'hiver.", 1),
    ("進補 — nourishing food before winter.", "進補 — des plats nourrissants avant l'hiver.", 1),
    ("鋼雕 — sculpture made of steel.", "鋼雕 — une sculpture en acier.", 1),
    ("沙雕 — sculpture built from sand.", "沙雕 — une sculpture construite avec du sable.", 1),
    ("節氣小表 · Solar terms", "節氣小表 · Les termes solaires", 1),
    ("你呢? · Over to you", "你呢? · À vous", 2),
    ("Have you seen the Fulong sand sculptures? Which film character would you most want to see in sand?", "Avez-vous vu les sculptures de sable de Fulong ? Quel personnage de film aimeriez-vous le plus voir en sable ?", 1),
    ("鋼雕行程 · Plan your visit", "鋼雕行程 · Organisez votre visite", 1),
    ("第 4 版 · 台灣大賽封王 · The Taiwan Series is decided", "第 4 版 · 台灣大賽封王 · La Série de Taïwan est décidée", 1),
    ("Staff report · Source: TSNA sports news, Oct 26", "Dépêche de la rédaction · Source : TSNA, actualités sportives, 26 oct.", 1),
    ("The Wei Chuan Dragons beat the CTBC Brothers 6-0 in Game 6 (Oct 26, Taipei Dome) to win the 2026 Taiwan Series 4-2 — the first-ever Dragons-Brothers final and the Dragons' 6th title. Starter C.C. Mercedes threw 8 shutout innings and was named Series MVP.",
     "Les Dragons de Wei Chuan ont battu les Brothers de CTBC 6-0 lors du match 6 (26 oct., Dôme de Taipei) pour remporter la Série de Taïwan 2026 4-2 — la première finale Dragons-Brothers et le 6e titre des Dragons. Le partant C.C. Mercedes a lancé 8 manches sans encaisser de point et a été nommé MVP de la série.", 1),
    ("棒球詞卡 · Baseball words", "棒球詞卡 · Les mots du baseball", 1),
    ("Four words: 完封 (shutout), 封王 (clinching the title), 全壘打 (home run), MVP (most valuable player).",
     "Quatre mots : 完封 (blanchissage), 封王 (remporter le titre), 全壘打 (coup de circuit), MVP (joueur le plus utile).", 1),
    ("第六戰得分走勢 · Game 6 runs by inning — bars drawn in proportion to runs",
     "第六戰得分走勢 · Points du match 6 par manche — barres proportionnelles aux points", 1),
    ("Note: the Dragons did not bat in the bottom of the 9th — leading 6-0 after the top of the 9th, the game was over. 1 + 5 = 6.",
     "Note : les Dragons n'ont pas frappé en fin de 9e manche — menant 6-0 après le début de la 9e, le match était terminé. 1 + 5 = 6.", 1),
    ("The Dragons won Game 6, 6-0.", "Les Dragons ont gagné le match 6, 6-0.", 1),
    ("The series ended 4-2 to the Dragons.", "La série s'est terminée 4-2 pour les Dragons.", 1),
    ("Mercedes threw 8 shutout innings.", "Mercedes a lancé 8 manches sans encaisser de point.", 1),
    ("Mercedes was named Series MVP.", "Mercedes a été nommé MVP de la série.", 1),
    ("The Dragons' 6th title in team history.", "Le 6e titre de l'histoire de l'équipe des Dragons.", 1),
    ("Three shutouts in one series is a first.", "Trois blanchissages dans une même série, une première.", 1),
    ("Game 6 was played at the Taipei Dome.", "Le match 6 s'est joué au Dôme de Taipei.", 1),
    ("A shutout: the other side scores zero.", "Un blanchissage : l'adversaire ne marque aucun point.", 1),
    ("Winning the title is 封王.", "Remporter le titre, c'est 封王.", 1),
    ("A ball hit out of the park is a home run.", "Une balle frappée hors du terrain, c'est un coup de circuit.", 1),
    ("Mercedes allowed 1 run in 14 innings.", "Mercedes n'a concédé qu'1 point en 14 manches.", 1),
    ("The Dragons scored 5 runs in the 8th inning.", "Les Dragons ont marqué 5 points dans la 8e manche.", 1),
    ("看圖答題 · Read the chart", "看圖答題 · Lire le graphique", 1),
    ("The 8th inning: 5 runs, the biggest bar.", "La 8e manche : 5 points, la plus grande barre.", 1),
    ("1 + 5 = 6 runs in total.", "1 + 5 = 6 points au total.", 1),
    ("完封 — a shutout: the other side scores zero.", "完封 — un blanchissage : l'adversaire ne marque aucun point.", 1),
    ("封王 — clinching the championship.", "封王 — remporter le championnat.", 1),
    ("全壘打 — a home run.", "全壘打 — un coup de circuit.", 1),
    ("安打 — a base hit.", "安打 — un coup sûr.", 1),
    ("系列賽小檔 · Series file", "系列賽小檔 · La série en bref", 1),
    ("Which team do you support? Have you ever watched a baseball game live?", "Quelle équipe soutenez-vous ? Avez-vous déjà assisté à un match de baseball en direct ?", 1),
    ('instr="Fill in"', 'instr="Complétez"', 12),
    ('instr="Match"', 'instr="Associez"', 2),
]

R56 = [
    ("第 5 版 · 天母萬聖節回顧、旅展攻略 · Halloween recap and the travel-fair game plan",
     "第 5 版 · 天母萬聖節回顧、旅展攻略 · Retour sur Halloween à Tianmu et plan de jeu du salon du voyage", 1),
    ("Tianmu's Halloween (Oct 25-26, postponed from Oct 24 by the typhoon): the Oct 25 night parade marched from Shin Kong Mitsukoshi Tianmu along Zhongcheng Road to Dayeh Takashimaya, and the Oct 26 main event ran 13:00-20:00 at Tianmu Sports Park, with 250 shops giving treats and 4,500 pumpkin buckets from three department stores.",
     "Halloween à Tianmu (25-26 oct., reporté du 24 oct. à cause du typhon) : le défilé nocturne du 25 oct. a marché de Shin Kong Mitsukoshi Tianmu le long de la route Zhongcheng jusqu'à Dayeh Takashimaya, et l'événement principal du 26 oct. s'est tenu de 13 h 00 à 20 h 00 au parc sportif de Tianmu, avec 250 boutiques distribuant des friandises et 4 500 seaux citrouilles de trois grands magasins.", 1),
    ("Travel-fair game plan: watch the shows first (Yamagata flower-hat dance, Korea's JUMP taekwondo-comedy show, the daily 14:00 mascot parade), then compare prices — budget fares often exclude checked baggage, so add that cost before you decide.",
     "Plan de jeu du salon du voyage : regardez d'abord les spectacles (danse des chapeaux fleuris de Yamagata, spectacle de taekwondo-comédie JUMP de Corée, défilé quotidien des mascottes à 14 h 00), puis comparez les prix — les tarifs économiques excluent souvent les bagages en soute, ajoutez donc ce coût avant de décider.", 1),
    ("練習例子 · Practice example", "練習例子 · Exemple d'exercice", 1),
    ("Practice numbers: NT$6,200 − NT$1,200 = NT$5,000, exactly his budget.",
     "Chiffres de l'exercice : 6 200 NT$ − 1 200 NT$ = 5 000 NT$, exactement son budget.", 1),
    ("讀懂了嗎? · Did you get it?", "讀懂了嗎? · Tout compris ?", 1),
    ("The night parade marched on Sunday, Oct 25, at 19:00.", "Le défilé nocturne a eu lieu le dimanche 25 oct. à 19 h 00.", 1),
    ("The main event ran 13:00-20:00 at Tianmu Sports Park.", "L'événement principal s'est tenu de 13 h 00 à 20 h 00 au parc sportif de Tianmu.", 1),
    ("250 shops gave treats.", "250 boutiques ont distribué des friandises.", 1),
    ("4,500 pumpkin buckets were given out.", "4 500 seaux citrouilles ont été distribués.", 1),
    ("The mascot parade runs daily at 14:00.", "Le défilé des mascottes a lieu chaque jour à 14 h 00.", 1),
    ("Budget fares often exclude checked baggage.", "Les tarifs économiques excluent souvent les bagages en soute.", 1),
    ("填一填 · Fill in", "填一填 · Complétez", 2),
    ("The parade marched along Zhongcheng Road.", "Le défilé a suivi la route Zhongcheng.", 1),
    ("The Tamagotchi 30th anniversary collaboration.", "La collaboration pour le 30e anniversaire de Tamagotchi.", 1),
    ("The Yamagata flower-hat dance performs on stage.", "La danse des chapeaux fleuris de Yamagata se produit sur scène.", 1),
    ("Set a budget before Double 11.", "Fixez un budget avant le Double 11.", 1),
    ("Add baggage fees before comparing fares.", "Ajoutez les frais de bagages avant de comparer les tarifs.", 1),
    ("List your cart first, then delete what you do not need.", "Listez d'abord votre panier, puis supprimez ce dont vous n'avez pas besoin.", 1),
    ("算一算 · Work it out", "算一算 · À vos calculs", 1),
    ("6,200 − 1,200 = 5,000, exactly the budget.", "6 200 − 1 200 = 5 000, exactement le budget.", 1),
    ("The parade starts at 19:00; the main event the next day at 13:00.", "Le défilé part à 19 h 00 ; l'événement principal commence le lendemain à 13 h 00.", 1),
    ("討糖 — trick-or-treating.", "討糖 — la chasse aux bonbons.", 1),
    ("踩街 — parading through the streets in costume.", "踩街 — défiler dans les rues en costume.", 1),
    ("南瓜桶 — a pumpkin bucket for treats.", "南瓜桶 — un seau citrouille pour les friandises.", 1),
    ("打卡 — checking in with a photo on social media.", "打卡 — signaler sa présence avec une photo sur les réseaux sociaux.", 1),
    ("天母時間表 · Tianmu schedule", "天母時間表 · Le programme de Tianmu", 1),
    ("你呢? · Over to you", "你呢? · À vous", 1),
    ("Have you ever worn a Halloween costume? Which character would you most want to be?", "Avez-vous déjà porté un costume d'Halloween ? Quel personnage aimeriez-vous le plus incarner ?", 1),
    ("旅展表演 · Stage shows", "旅展表演 · Les spectacles", 1),
    ("第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech in depth, and reading a chart",
     "第 6 版 · 金融科技週深讀 + 讀圖表 · La fintech en profondeur, et lire un graphique", 1),
    ("Staff report · Source: event organisers' press release (Oct 23) and event FAQ",
     "Dépêche de la rédaction · Source : communiqué des organisateurs (23 oct.) et FAQ de l'événement", 1),
    ("Three plus signs: Finance+ (finance plus technology), AI+ (artificial intelligence inside banks, investment and insurance) and global expansion (helping start-ups sell worldwide). The scale — 45,000+ people, 120+ economies, 1,000+ speakers, 800+ exhibitors and start-ups, 30+ delegations, 100+ community events — shows fintech is now a whole-city topic.",
     "Trois signes plus : Finance+ (la finance plus la technologie), IA+ (l'intelligence artificielle dans les banques, l'investissement et l'assurance) et l'expansion mondiale (aider les jeunes entreprises à vendre dans le monde entier). L'ampleur — plus de 45 000 personnes, plus de 120 économies, plus de 1 000 intervenants, plus de 800 exposants et jeunes entreprises, plus de 30 délégations, plus de 100 événements communautaires — montre que la fintech est désormais un sujet pour toute la ville.", 1),
    ("旅展每日開放時數 · ITF opening hours per day — bars drawn in proportion to hours",
     "旅展每日開放時數 · Heures d'ouverture du salon par jour — barres proportionnelles aux heures", 1),
    ("Source: published fair hours (Nov 6: 12:00-18:00; Nov 7-9: 10:00-18:00). Total: 30 hours.",
     "Source : horaires publiés du salon (6 nov. : 12 h 00-18 h 00 ; 7-9 nov. : 10 h 00-18 h 00). Total : 30 heures.", 1),
    ("看圖答題 · Read the chart", "看圖答題 · Lire le graphique", 1),
    ("Nov 6 is the shortest day: 6 hours.", "Le 6 nov. est le jour le plus court : 6 heures.", 1),
    ("Nov 8 runs 10:00-18:00: 8 hours.", "Le 8 nov. se tient de 10 h 00 à 18 h 00 : 8 heures.", 1),
    ("6 + 8 + 8 + 8 = 30 hours in total.", "6 + 8 + 8 + 8 = 30 heures au total.", 1),
    ("Nov 6 opens at noon, not 10:00.", "Le 6 nov. ouvre à midi, pas à 10 h 00.", 1),
    ("深讀測驗 · Deep-read quiz", "深讀測驗 · Quiz de lecture approfondie", 1),
    ("Finance+ means finance plus technology.", "Finance+ signifie la finance plus la technologie.", 1),
    ("AI helps read data, spot risks and answer clients.", "L'IA aide à lire les données, à repérer les risques et à répondre aux clients.", 1),
    ("Global expansion means selling products worldwide.", "L'expansion mondiale signifie vendre ses produits dans le monde entier.", 1),
    ("More than 1,000 speakers take part.", "Plus de 1 000 intervenants y participent.", 1),
    ("The main conference runs Nov 2-3.", "La conférence principale se tient les 2-3 nov.", 1),
    ("Community events number 100+ through the week.", "Les événements communautaires sont plus de 100 sur la semaine.", 1),
    ("Payments is one of the main-conference topics.", "Les paiements sont l'un des sujets de la conférence principale.", 1),
    ("Digital assets is a main-conference topic.", "Les actifs numériques sont un sujet de la conférence principale.", 1),
    ("Insurtech is a main-conference topic.", "L'assurtech est un sujet de la conférence principale.", 1),
    ("The week connects start-ups with the world.", "La semaine met les jeunes entreprises en relation avec le monde.", 1),
    ("Total opening hours: 30.", "Durée totale d'ouverture : 30 heures.", 1),
    ("Nov 6 opens at noon (12:00).", "Le 6 nov. ouvre à midi (12 h 00).", 1),
    ("The travel fair has 1,600 booths.", "Le salon du voyage compte 1 600 stands.", 1),
    ("More than 45,000 people are expected.", "Plus de 45 000 participants sont attendus.", 1),
    ("數字一覽 · By the numbers", "數字一覽 · Les chiffres", 1),
    ("比價提醒 · Compare carefully", "比價提醒 · Comparez attentivement", 1),
    ("Example from press reports (Oct 20): Cathay Pacific Taipei-Tokyo return from NT$13,433 including tax, book by Nov 13. Always compare with baggage fees added — and check the live booking result, as prices vary by date.",
     "Exemple tiré de la presse (20 oct.) : aller-retour Cathay Pacific Taipei-Tokyo à partir de 13 433 NT$ taxes comprises, réservation avant le 13 nov. Comparez toujours en ajoutant les frais de bagages — et vérifiez le résultat de la réservation en direct, car les prix varient selon la date.", 1),
    ('instr="Fill in"', 'instr="Complétez"', 14),
    ('instr="Match"', 'instr="Associez"', 1),
]

R7 = [
    ("語言聚焦 · 三個級別,三個主題 · Three levels, three topics",
     "語言聚焦 · 三個級別,三個主題 · Trois niveaux, trois sujets", 1),
    ("A2 · 展會的話 · Fair words", "A2 · 展會的話 · Les mots des salons", 1),
    ("This week's fairs give you four useful words: 旅展 (travel fair), 攤位 (booth), 集章 (stamp-collecting) and 吉祥物大遊行 (mascot parade). Learn them once, and the whole travel fair makes sense.",
     "Les salons de cette semaine vous offrent quatre mots utiles : 旅展 (salon du voyage), 攤位 (stand), 集章 (collection de tampons) et 吉祥物大遊行 (défilé des mascottes). Apprenez-les une fois, et tout le salon du voyage devient clair.", 1),
    ("Four fair words: 旅展, 攤位, 集章, 吉祥物大遊行.", "Quatre mots des salons : 旅展, 攤位, 集章, 吉祥物大遊行.", 1),
    ("旅展 is short for 旅行展覽會 (travel exhibition). A 攤位 is one stall inside the fair; the Taipei fair has 1,600 of them. 集章 means collecting stamps at set points — collect all six Greenway stamps and you win a prize.",
     "旅展 est l'abréviation de 旅行展覽會 (exposition de voyage). Un 攤位 est un étal à l'intérieur du salon ; le salon de Taipei en compte 1 600. 集章 signifie collectionner des tampons à des points précis — collectionnez les six tampons des voies vertes et vous gagnez un prix.", 1),
    ("A booth inside the fair is a 攤位.", "Un stand à l'intérieur du salon, c'est un 攤位.", 1),
    ("The mascot parade runs daily at 14:00.", "Le défilé des mascottes a lieu chaque jour à 14 h 00.", 1),
    ("Collecting stamps at set points is 集章.", "Collectionner les tampons à des points précis, c'est 集章.", 1),
    ("The travel fair is at the Nangang Exhibition Center.", "Le salon du voyage se tient au Centre des expositions de Nangang.", 1),
    ("Practise: 「旅展幾點開門？」 ('What time does the fair open?') — Friday opens at noon, other days at 10:00.",
     "Entraînez-vous : 「旅展幾點開門？」 (« À quelle heure ouvre le salon ? ») — le vendredi ouvre à midi, les autres jours à 10 h 00.", 1),
    ("B1 · 球賽與節氣 · Games & seasons", "B1 · 球賽與節氣 · Matchs et saisons", 1),
    ("Sport and seasons share this week's headlines. Group the words and they stick: winning （封王、完封） and winter （立冬、進補）.",
     "Le sport et les saisons partagent les gros titres de cette semaine. Groupez les mots et ils restent : gagner （封王、完封） et l'hiver （立冬、進補）.", 1),
    ("Group the words: winning (封王/完封), winter (立冬/進補).", "Groupez les mots : gagner (封王/完封), l'hiver (立冬/進補).", 1),
    ("封王 means clinching the championship; 完封 means shutting the other side out, 0 runs. 立冬 is the solar term that starts winter; 進補 is eating nourishing hot food before the cold months.",
     "封王 signifie remporter le championnat ; 完封 signifie ne laisser aucun point à l'adversaire, 0 point. 立冬 est le terme solaire qui ouvre l'hiver ; 進補 consiste à manger des plats chauds et nourrissants avant les mois froids.", 1),
    ("Winning the title is 封王.", "Remporter le titre, c'est 封王.", 1),
    ("完封 means the other side scores zero.", "完封 signifie que l'adversaire ne marque aucun point.", 1),
    ("Lidong starts winter.", "Lidong marque le début de l'hiver.", 1),
    ("Ginger duck is a Lidong dish.", "Le canard au gingembre est un plat de Lidong.", 1),
    ("Memory trick: learn 封王 first, then the way it was won （完封）, then the season it happened in （立冬）.",
     "Astuce mémoire : apprenez d'abord 封王, puis la manière dont il a été gagné （完封）, puis la saison où cela s'est produit （立冬）.", 1),
    ("B2 · 港台說法 · Local talk", "B2 · 港台說法 · Parlers locaux", 1),
    ("Taiwan and Hong Kong each have their own way of saying things. This week: 打卡 (check in with a photo), 討糖 (trick-or-treat), 踩街 (street parade in costume) and 泡湯 (soak in a hot spring).",
     "Taïwan et Hong Kong ont chacun leur façon de dire les choses. Cette semaine : 打卡 (signaler sa présence avec une photo), 討糖 (chasse aux bonbons), 踩街 (défilé costumé dans les rues) et 泡湯 (bain dans une source chaude).", 1),
    ("Four local words from this issue: 打卡, 討糖, 踩街, 泡湯.", "Quatre mots locaux de ce numéro : 打卡, 討糖, 踩街, 泡湯.", 1),
    ("打卡 started as clocking in at work, but at a fair or festival it means posting a photo to say 'I was here'. 討糖 is what children say at shops at Halloween; 踩街 is the costumed parade itself; 泡湯 is the autumn pleasure of a hot-spring bath.",
     "打卡 signifiait d'abord pointer à l'arrivée au travail, mais lors d'un salon ou d'un festival, cela veut dire publier une photo pour dire « j'y étais ». 討糖 est ce que les enfants disent aux boutiques à Halloween ; 踩街 est le défilé costumé lui-même ; 泡湯 est le plaisir automnal d'un bain dans une source chaude.", 1),
    ("At a festival, 打卡 means posting a photo to say you were there.", "Lors d'un festival, 打卡 signifie publier une photo pour dire qu'on y était.", 1),
    ("Trick-or-treating is 討糖.", "La chasse aux bonbons, c'est 討糖.", 1),
    ("踩街 is a costumed street parade.", "踩街 est un défilé costumé dans les rues.", 1),
    ("Soaking in a hot spring is 泡湯.", "Se baigner dans une source chaude, c'est 泡湯.", 1),
    ("You don't need many local sayings — learn four and every outing feels closer.",
     "Pas besoin de beaucoup d'expressions locales — apprenez-en quatre et chaque sortie vous semblera plus proche.", 1),
    ("完勝 means winning big; 完封 means the other side scored zero.",
     "完勝 signifie gagner largement ; 完封 signifie que l'adversaire n'a marqué aucun point.", 1),
    ("Lidong starts winter; the Solstice is the shortest day. Different terms.",
     "Lidong ouvre l'hiver ; le solstice est le jour le plus court. Ce sont deux termes différents.", 1),
    ("Check the city: FinTech Week opens in Hong Kong, not Taipei.",
     "Vérifiez la ville : la Semaine FinTech ouvre à Hong Kong, pas à Taipei.", 1),
    ("易錯診所 · Error clinic", "易錯診所 · Clinique des erreurs", 1),
    ("「先去集章，再去看表演。」 — the frame 先…再… gives the order of two actions: first X, then Y. Make your own: 先比價，再結帳 (compare prices first, then pay).",
     "「先去集章，再去看表演。」 — la structure 先…再… donne l'ordre de deux actions : d'abord X, puis Y. Faites la vôtre : 先比價，再結帳 (comparez d'abord les prix, puis payez).", 1),
    ("Frame: 先…再… — first X, then Y. Make your own sentence with it.",
     "Structure : 先…再… — d'abord X, puis Y. Faites votre propre phrase avec elle.", 1),
    ("本週句式 · Sentence frame", "本週句式 · La phrase-modèle", 1),
    ("An editor's example letter — not a real one. Deferral notice: VOL.1 promised real letters and best page-8 writing from this issue; none publishable had arrived by press time, so the example stays and the invitation stays open.",
     "Lettre d'exemple de la rédaction — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucun texte publiable n'était arrivé à la mise sous presse, l'exemple reste donc et l'invitation reste ouverte — écrivez-nous, vos lettres paraîtront dans un prochain numéro !", 1),
    ("讀者園地 · Readers' corner", "讀者園地 · Le coin des lecteurs", 1),
    ("本週金句 · Phrases of the week — word for word from this issue's articles",
     "本週金句 · Phrases de la semaine — mot pour mot tirées des articles de ce numéro", 1),
    ("Pay by phone, scan to pay, buy insurance online — that is fintech.",
     "Payer par téléphone, scanner pour payer, acheter une assurance en ligne — c'est la fintech.", 1),
    ("123 countries and cities, 1,600 booths.", "123 pays et villes, 1 600 stands.", 1),
    ("Buy what you need; don't buy a pile of things you won't use just for a discount.",
     "Achetez ce dont vous avez besoin ; n'achetez pas un tas de choses dont vous ne vous servirez pas juste pour une réduction.", 1),
    ("In Kaohsiung, even steel can become a stage.", "À Kaohsiung, même l'acier peut devenir une scène.", 1),
    ("Fulong's summer came to an end on October 26.", "L'été de Fulong s'est terminé le 26 octobre.", 1),
    ("A 6-0 shutout of the Brothers, and the Dragons threw the red ribbons.",
     "Un blanchissage 6-0 contre les Brothers, et les Dragons ont lancé les rubans rouges.", 1),
    ("250 shops giving treats together.", "250 boutiques distribuant des friandises ensemble.", 1),
    ("On the fair's first day the doors open only at noon.", "Le premier jour du salon, les portes n'ouvrent qu'à midi.", 1),
    ("下期預告 · Next week (VOL.3)", "下期預告 · La semaine prochaine (VOL.3)", 1),
    ('instr="Fill in"', 'instr="Complétez"', 6),
]

R8 = [
    ("測驗與答案 · Test & keys", "測驗與答案 · Test et corrigés", 1),
    ("第 8 版 · 本週大測驗 + 全部答案 · This week's test and every answer key",
     "第 8 版 · 本週大測驗 + 全部答案 · Le test de la semaine et toutes les réponses", 1),
    ("A · 判斷對錯 · True or false", "A · 判斷對錯 · Vrai ou faux", 1),
    ("FinTech Week opens Monday, Nov 2.", "La Semaine FinTech ouvre le lundi 2 nov.", 1),
    ("Lidong is Nov 7, not Nov 6.", "Lidong tombe le 7 nov., pas le 6 nov.", 1),
    ("The Dragons won the series 4-2.", "Les Dragons ont remporté la série 4-2.", 2),
    ("Game 6 ended 6-0, not 6-3.", "Le match 6 s'est terminé 6-0, pas 6-3.", 1),
    ("The sand festival closed Oct 26.", "Le festival de sable s'est terminé le 26 oct.", 1),
    ("The travel fair opens at noon on Nov 6, not 10:00.", "Le salon du voyage ouvre à midi le 6 nov., pas à 10 h 00.", 1),
    ("B · 本週大測驗 · The big quiz", "B · 本週大測驗 · Le grand quiz", 1),
    ("The main conference is Nov 2-3.", "La conférence principale se tient les 2-3 nov.", 1),
    ("The travel fair runs to Monday, Nov 9.", "Le salon du voyage se poursuit jusqu'au lundi 9 nov.", 1),
    ("The steel festival runs to Nov 22.", "Le festival de l'acier se tient jusqu'au 22 nov.", 1),
    ("The night parade marched Oct 25 at 19:00.", "Le défilé nocturne a eu lieu le 25 oct. à 19 h 00.", 1),
    ("Double 11 is Wednesday, Nov 11.", "Le Double 11 tombe le mercredi 11 nov.", 1),
    ("Mercedes allowed 1 run in 14 innings.", "Mercedes n'a concédé qu'1 point en 14 manches.", 1),
    ("The mascot parade runs daily at 14:00.", "Le défilé des mascottes a lieu chaque jour à 14 h 00.", 1),
    ("The trail encyclopaedia collects 56 routes.", "L'encyclopédie des sentiers réunit 56 itinéraires.", 1),
    ("Total opening hours: 6 + 8 + 8 + 8 = 30.", "Durée totale d'ouverture : 6 + 8 + 8 + 8 = 30 heures.", 1),
    ("The stamp challenge covers 6 Greenways.", "Le défi des tampons couvre 6 voies vertes.", 1),
    ("C · 完成句子 · Fill in", "C · 完成句子 · Complétez les phrases", 1),
    ("Fintech: technology running financial services.", "La fintech : la technologie au service des services financiers.", 1),
    ("Lidong starts winter.", "Lidong marque le début de l'hiver.", 1),
    ("A shutout: the other side scores zero.", "Un blanchissage : l'adversaire ne marque aucun point.", 1),
    ("Winning the title is 封王.", "Remporter le titre, c'est 封王.", 1),
    ("Trick-or-treating is 討糖.", "La chasse aux bonbons, c'est 討糖.", 1),
    ("Collecting stamps is 集章.", "Collectionner les tampons, c'est 集章.", 1),
    ("The travel fair is at the Nangang Exhibition Center.", "Le salon du voyage se tient au Centre des expositions de Nangang.", 1),
    ("Pier-2 hosts the steel festival.", "Pier-2 accueille le festival de l'acier.", 1),
    ("Global expansion: selling products worldwide.", "L'expansion mondiale : vendre ses produits dans le monde entier.", 1),
    ("AI inside finance is 人工智慧＋.", "L'IA dans la finance, c'est 人工智慧＋.", 1),
    ("D · 讀一讀,答一答 · Read and answer", "D · 讀一讀,答一答 · Lisez et répondez", 1),
    ("He goes to the travel fair on Friday at noon.", "Il se rend au salon du voyage le vendredi à midi.", 1),
    ("The parade is at 14:00.", "Le défilé a lieu à 14 h 00.", 1),
    ("A set of 4 coupons costs 4,100 (list price 8,200).", "Un lot de 4 bons coûte 4 100 (prix affiché 8 200).", 1),
    ("He eats ginger duck for Lidong on Saturday.", "Il mange du canard au gingembre pour Lidong le samedi.", 1),
    ("Order: fair, then Lidong pot, then the coupon set for a buffet.", "Ordre : le salon, puis la fondue de Lidong, puis le lot de bons pour un buffet.", 1),
    ("E · 情景說話 · Say it in context", "E · 情景說話 · En situation", 1),
    ("The travel fair opens Friday at noon.", "Le salon du voyage ouvre le vendredi à midi.", 1),
    ("Lidong is the first solar term of winter.", "Lidong est le premier terme solaire de l'hiver.", 1),
    ("A shutout means the other side scores zero.", "Un blanchissage signifie que l'adversaire ne marque aucun point.", 1),
    ("The mascot parade is at 14:00 daily.", "Le défilé des mascottes a lieu chaque jour à 14 h 00.", 1),
    ("Compare prices first, then pay: 先比價，再結帳.", "Comparez d'abord les prix, puis payez : 先比價，再結帳.", 1),
    ("F · 寫一寫 · Writing", "F · 寫一寫 · À vos plumes", 1),
    ("Writing — there is no single right answer. A {NCHARS}-character model follows.",
     "Rédaction — il n'y a pas de réponse unique. Un modèle de {NCHARS} caractères suit.", 1),
    ("Open task - the model answer is printed in section F above ({NCHARS} characters)",
     "Tâche ouverte — le texte modèle est imprimé dans la section F ci-dessus ({NCHARS} caractères)", 1),
    ("Model answer: ", "Texte modèle : ", 1),
    ("答案 · Answer keys — in page order, with a short English note for every item",
     "答案 · Réponses — dans l'ordre des pages, avec une courte note en français pour chaque exercice", 1),
    ("All notes in English · ✓ = the writing model", "Toutes les notes en français · ✓ = le texte modèle", 1),
    ('instr="Fill in"', 'instr="Complétez"', 10),
    ('instr="Writing"', 'instr="Écrivez"', 1),
]

def render_names():
    rep("render.py", "Lucerna-VOL2-web.pdf", "Lucerna-VOL2-FR-web.pdf", 1)
    rep("render.py", "Lucerna-VOL2.pdf", "Lucerna-VOL2-FR.pdf", 1)

FIX2 = [
    ("content12.py", "生活 · Life", "生活 · Vie quotidienne", 1),
    ("content56.py", "青年 · Youth", "青年 · Jeunesse", 1),
    ("content56.py", "深讀 · Deep read", "深讀 · Lecture approfondie", 1),
    ("content56.py", "深讀測驗 · Quiz de lecture approfondie", "深讀測驗 · Quiz de lecture", 1),
    ("content7.py", "語言 · Language focus", "語言 · Focus langue", 1),
    # P7 col-3 compression: clinic (-3 lines) + frame (-2 lines) + letters (-2 lines)
    # brings col3_end back to core parity (~1745) so the teaser ends ~2543, not 2714.
    ("content7.py", "完勝 signifie gagner largement ; 完封 signifie que l'adversaire n'a marqué aucun point.",
     "完勝 = gagner largement ; 完封 = aucun point pour l'adversaire.", 1),
    ("content7.py", "Lidong ouvre l'hiver ; le solstice est le jour le plus court. Ce sont deux termes différents.",
     "Lidong ouvre l'hiver ; le solstice est le jour le plus court.", 1),
    ("content7.py", "Vérifiez la ville : la Semaine FinTech ouvre à Hong Kong, pas à Taipei.",
     "Vérifiez la ville : c'est Hong Kong, pas Taipei.", 1),
    ("content7.py", "「先去集章，再去看表演。」 — la structure 先…再… donne l'ordre de deux actions : d'abord X, puis Y. Faites la vôtre : 先比價，再結帳 (comparez d'abord les prix, puis payez).",
     "「先去集章，再去看表演。」 — 先…再… donne l'ordre : d'abord X, puis Y. Exemple : 先比價，再結帳 (comparez d'abord, puis payez).", 1),
    ("content7.py", "Structure : 先…再… — d'abord X, puis Y. Faites votre propre phrase avec elle.",
     "Structure : 先…再… — d'abord X, puis Y. À vous !", 1),
    ("content7.py", "Lettre d'exemple de la rédaction — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucun texte publiable n'était arrivé à la mise sous presse, l'exemple reste donc et l'invitation reste ouverte — écrivez-nous, vos lettres paraîtront dans un prochain numéro !",
     "Lettre d'exemple de la rédaction — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucun texte publiable n'était arrivé à la mise sous presse — l'exemple reste, et l'invitation reste ouverte : écrivez-nous !", 1),
    # P7 A2/B2 column tightening: back under the 1560 design bottom.
    ("content7.py", "Les salons de cette semaine vous offrent quatre mots utiles : 旅展 (salon du voyage), 攤位 (stand), 集章 (collection de tampons) et 吉祥物大遊行 (défilé des mascottes). Apprenez-les une fois, et tout le salon du voyage devient clair.",
     "Les salons de cette semaine vous offrent quatre mots utiles : 旅展 (salon du voyage), 攤位 (stand), 集章 (tampons) et 吉祥物大遊行 (défilé des mascottes). Apprenez-les une fois, et tout le salon devient clair.", 1),
    ("content7.py", "旅展 est l'abréviation de 旅行展覽會 (exposition de voyage). Un 攤位 est un étal à l'intérieur du salon ; le salon de Taipei en compte 1 600. 集章 signifie collectionner des tampons à des points précis — collectionnez les six tampons des voies vertes et vous gagnez un prix.",
     "旅展 abrège 旅行展覽會 (exposition de voyage). Un 攤位 est un étal du salon ; celui de Taipei en compte 1 600. 集章, c'est collectionner des tampons à des points précis — les six tampons des voies vertes, et vous gagnez un prix.", 1),
    ("content7.py", "Entraînez-vous : 「旅展幾點開門？」 (« À quelle heure ouvre le salon ? ») — le vendredi ouvre à midi, les autres jours à 10 h 00.",
     "Entraînez-vous : 「旅展幾點開門？」 (« À quelle heure ouvre le salon ? ») — vendredi à midi, les autres jours à 10 h 00.", 1),
    ("content7.py", "Taïwan et Hong Kong ont chacun leur façon de dire les choses. Cette semaine : 打卡 (signaler sa présence avec une photo), 討糖 (chasse aux bonbons), 踩街 (défilé costumé dans les rues) et 泡湯 (bain dans une source chaude).",
     "Taïwan et Hong Kong ont chacun leur façon de dire les choses. Cette semaine : 打卡 (photo de présence), 討糖 (chasse aux bonbons), 踩街 (défilé costumé) et 泡湯 (bain thermal).", 1),
    ("content7.py", "打卡 signifiait d'abord pointer à l'arrivée au travail, mais lors d'un salon ou d'un festival, cela veut dire publier une photo pour dire « j'y étais ». 討糖 est ce que les enfants disent aux boutiques à Halloween ; 踩街 est le défilé costumé lui-même ; 泡湯 est le plaisir automnal d'un bain dans une source chaude.",
     "打卡, c'était pointer au travail ; dans un salon ou un festival, c'est publier une photo pour dire « j'y étais ». 討糖, c'est ce que les enfants disent aux boutiques à Halloween ; 踩街, le défilé costumé lui-même ; 泡湯, le plaisir automnal d'un bain thermal.", 1),
    ("content7.py", "Pas besoin de beaucoup d'expressions locales — apprenez-en quatre et chaque sortie vous semblera plus proche.",
     "Quatre expressions locales suffisent — chaque sortie vous semblera plus proche.", 1),
]

def fix2():
    for f, old, new, n in FIX2:
        rep(f, old, new, n)
    print("transform_fr FIX2 applied OK")

# One-line trim of the P7 letters disclosure: brings col3_end to core parity.
FIX3 = [
    ("content7.py", "Lettre d'exemple de la rédaction — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de la page 8 dès ce numéro ; aucun texte publiable n'était arrivé à la mise sous presse — l'exemple reste, et l'invitation reste ouverte : écrivez-nous !",
     "Lettre d'exemple de la rédaction — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de page 8 ; aucun texte publiable n'était arrivé à la mise sous presse — l'exemple reste, et l'invitation reste ouverte : écrivez-nous !", 1),
]

def fix3():
    for f, old, new, n in FIX3:
        rep(f, old, new, n)
    print("transform_fr FIX3 applied OK")

# FIX4: (a) strict-CJK: svglib _fw() turns an ASCII comma placed right after
# a CJK term into full-width ， — 6 such commas in French P7 prose added 6
# net ， vs the core. Restructure so no punctuation follows a CJK term.
# (b) occlusion: P2 你呢 box +1 line, P5/P6 box titles too wide, P7 letters
# box last line 5.9px past its border (formula short by one line: cut the
# disclosure 7 -> 6 wrapped lines).
FIX4 = [
    ("content7.py", "集章, c'est collectionner des tampons à des points précis",
     "集章 veut dire collectionner des tampons à des points précis", 1),
    ("content7.py", "apprenez d'abord 封王, puis la manière dont il a été gagné",
     "apprenez d'abord 封王 puis la manière dont il a été gagné", 1),
    ("content7.py", "打卡, c'était pointer au travail ; dans un salon ou un festival, c'est publier une photo pour dire « j'y étais ». 討糖, c'est ce que les enfants disent aux boutiques à Halloween ; 踩街, le défilé costumé lui-même ; 泡湯, le plaisir automnal d'un bain thermal.",
     "Autrefois 打卡 voulait dire pointer au travail ; dans un salon ou un festival, c'est une photo pour dire « j'y étais ». 討糖 désigne ce que les enfants disent aux boutiques à Halloween ; 踩街 est le défilé costumé lui-même ; 泡湯 est le plaisir automnal d'un bain thermal.", 1),
    ("content7.py", "Lettre d'exemple de la rédaction — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de page 8 ; aucun texte publiable n'était arrivé à la mise sous presse — l'exemple reste, et l'invitation reste ouverte : écrivez-nous !",
     "Lettre d'exemple — pas une vraie lettre. Avis de report : VOL.1 avait promis de vraies lettres et les meilleurs textes de page 8 ; aucun texte publiable n'était arrivé — l'exemple reste, et l'invitation reste ouverte : écrivez-nous !", 1),
    ("content12.py", "Quelle fondue mangeriez-vous pour Lidong ? Que contient votre panier du Double 11 ?",
     "Quelle fondue pour Lidong ? Que contient votre panier du Double 11 ?", 1),
    ("content56.py", "天母時間表 · Le programme de Tianmu", "天母時間表 · Le programme", 1),
    ("content56.py", "比價提醒 · Comparez attentivement", "比價提醒 · Comparez", 1),
]

def fix4():
    for f, old, new, n in FIX4:
        rep(f, old, new, n)
    print("transform_fr FIX4 applied OK")

# FIX5: letters-box height formula runs one line short for the French
# disclosure (last ink 6.5px past the border even at 6 wrapped lines):
# raise its trailing constant 26 -> 56 (+30px). Col3_end then lands at
# core parity (~1745) and the teaser at ~2543.
FIX5 = [
    ("content7.py", 'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26',
     'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 56', 1),
]

def fix5():
    for f, old, new, n in FIX5:
        rep(f, old, new, n)
    print("transform_fr FIX5 applied OK")

def main():
    if CORE not in load("content12.py") and ED in load("content12.py"):
        try:
            fix2()
        except AssertionError as e:
            print("FIX2 already applied or not applicable:", e)
        try:
            fix3()
        except AssertionError as e:
            print("FIX3 already applied or not applicable:", e)
        try:
            fix4()
        except AssertionError as e:
            print("FIX4 already applied or not applicable:", e)
        try:
            fix5()
        except AssertionError as e:
            print("FIX5 already applied or not applicable:", e)
        return
    repoint()
    bslib()
    for f, rows in [("content12.py", R12), ("content34.py", R34), ("content56.py", R56),
                    ("content7.py", R7), ("content8.py", R8)]:
        for old, new, n in rows:
            rep(f, old, new, n)
    render_names()
    fix2()
    fix3()
    fix4()
    fix5()
    print("transform_fr applied OK")

if __name__ == "__main__":
    main()
