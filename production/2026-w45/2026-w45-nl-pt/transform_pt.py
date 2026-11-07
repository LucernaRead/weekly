# -*- coding: utf-8 -*-
"""NL x EN (W45) -> NL x PT (W45) transform.

Donor: the sibling W45 NL x EN build (same W45 NL core, same layout fixes:
P2 spacing, P8 13.0pt keys, P7 col-3 stack). This script rewrites ONLY the
explanation layer (English -> Brazilian Portuguese, following the shipped
W43 NL x PT furniture strings verbatim) plus the edition repointing.
Frozen Dutch text (articles, exercises, keys except the re-aimed
translation items 137/138, P7 word-box definition sentence, clinic
corrections, example letter, Dutch disclosure) is never touched: every
replacement below is an exact literal match on an English string, with
the post-run assertion that the old string no longer occurs anywhere
in the build code. Specific (longer) forms are replaced before their
shorter prefixes. Run from this directory: tools/venv/bin/python
transform_pt.py ; re-run is a no-op except the assertion pass.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "render.py", "rowcheck.py"]

# (old, new) — order matters: longer/specific forms first.
MAP = [
    # ---- repointing (all files) ----
    ("weekly-report-w45-nl-en", "weekly-report-w45-nl-pt"),
    ("De-Lucerna-VOL2-EN-web.pdf", "De-Lucerna-VOL2-PT-web.pdf"),
    ("De-Lucerna-VOL2-EN.pdf", "De-Lucerna-VOL2-PT.pdf"),
    # ---- bslib4 furniture (W43 NL x PT measured) ----
    ("De Lucerna · VOL.2 · Dutch text · English explanations · LUCERNA DUTCH WEEKLY",
     "De Lucerna · SEMANÁRIO NEERLANDÊS VOL.2 · TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS"),
    ('f"Page {n} of {total}"', 'f"Página {n} de {total}"'),
    ('"Note | " + s', '"Nota — " + s'),
    # ---- P1 badge: W43 slot y=372, 19.5pt BRICK ----
    ("TEXT IN DUTCH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS",
     "TEXTOS EM NEERLANDÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA"),
    ('", 20, "sans", True, OLIVE, anchor="middle")\n', '", 19.5, "sans", True, BRICK, anchor="middle")\n'),
    # ---- P1 ----
    ("ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH",
     "ELKE WEEK IN HET NEDERLANDS · O NEERLANDÊS QUE OS NEERLANDESES LEEM"),
    ("CLIMATE WEEK", "SEMANA DO CLIMA"),
    ("The whole country joins in · see page 2", "Todo o país participa · ver página 2"),
    ("Note | de Klimaatweek = Climate Week · de boom planten = to plant a tree · besparen = to save · de waarschuwing = warning.",
     "Nota — de Klimaatweek = Semana do Clima · de boom planten = plantar uma árvore · besparen = poupar · de waarschuwing = aviso."),
    ("DE WEEK IN CIJFERS · IN NUMBERS", "DE WEEK IN CIJFERS · Em números"),
    ("(the days of the Climate Week)", "(os dias da Semana do Clima)"),
    ("(the trees and shrubs Coevorden gives away on Saturday)", "(as árvores e arbustos que Coevorden distribui no sábado)"),
    ("(the museums open on Museum Night, 70+)", "(os museus abertos na Noite dos Museus, mais de 70)"),
    ("(the matches of Eredivisie matchday 12)", "(os jogos da 12.ª rodada da Eredivisie)"),
    ("NU JIJ · YOUR TURN", "NU JIJ · Agora você"),
    ("The Climate Week runs 2–8 November", "A Semana do Clima vai de 2 a 8 de novembro"),
    ("Museum Night is on Saturday 7 November", "A Noite dos Museus é no sábado, 7 de novembro"),
    ("Heerenveen–Feyenoord kicks off at 11:15", "Heerenveen–Feyenoord começa às 11h15"),
    ("Twente–Ajax kicks off at 13:30", "Twente–Ajax começa às 13h30"),
    ("Plural subject, so planten", "Sujeito no plural, por isso planten"),
    ('"· THIS WEEK"', '"· ESTA SEMANA"'),
    ("Agenda van de week · THIS WEEK'S EVENTS", "Agenda van de week · Eventos da semana"),
    ("See the articles on pages 2–4", "Veja os artigos das páginas 2–4"),
    ("for all dates and times.", "para todas as datas e horários."),
    ("IN DEZE EDITIE · IN THIS ISSUE", "IN DEZE EDITIE · Neste número"),
    ("«Climate»: the weather and nature around us, long-term. Climate Week is about our climate.",
     "«Clima»: o tempo e a natureza à nossa volta, a longo prazo. A Semana do Clima é sobre o nosso clima."),
    ("IN HET KORT · IN BRIEF", "IN HET KORT · Em resumo"),
    ("BLIKSEMQUIZ · LIGHTNING QUIZ", "BLIKSEMQUIZ · Quiz relâmpago"),
    ("Read page 1, choose the right answer · answers on page 8",
     "Leia a página 1 e escolha a resposta certa · respostas na página 8"),
    ("The Climate Week lasts 7 days (2–8 November)", "A Semana do Clima dura 7 dias (2–8 de novembro)"),
    ("Museum Night is in Amsterdam", "A Noite dos Museus é em Amsterdã"),
    # ---- P2 ----
    ("LEVEN · LIFE", "LEVEN · A vida"),
    ("NIVEAU A2 · De Klimaatweek, stap voor stap · The Climate Week, step by step",
     "NIVEAU A2 · De Klimaatweek, stap voor stap · A Semana do Clima, passo a passo"),
    ("ZO ONTHOUD JE HET · REMEMBER", "ZO ONTHOUD JE HET · A dica"),
    ("het klimaat = climate · wortelen = to take root · besparen = to save · de verwarming = heating · de waarschuwing = warning · lokaal = local.",
     "het klimaat = clima · wortelen = criar raízes · besparen = poupar · de verwarming = aquecimento · de waarschuwing = aviso · lokaal = local."),
    ('"EN JIJ? · AND YOU?"', '"EN JIJ? · E você?"'),
    ("What do you do in the Climate Week: plant a tree, save energy or cycle? Write two sentences in Dutch and send them to the editors.",
     "O que você faz na Semana do Clima: plantar uma árvore, poupar energia ou andar de bicicleta? Escreva duas frases em neerlandês e envie-as à redação."),
    ("DE CODES VAN HET KNMI · KNMI CODES", "DE CODES VAN HET KNMI · Códigos do KNMI"),
    ("What does each colour mean?", "O que significa cada cor?"),
    ("The weather may be dangerous: take care", "O tempo pode ser perigoso: tome cuidado"),
    ("Dangerous: be prepared", "Perigoso: prepare-se"),
    ("Very dangerous: stay indoors if you can", "Muito perigoso: fique em casa, se puder"),
    ("The warning is for your own area", "O aviso é para a sua região"),
    ("OEFENINGEN · EXERCISES ON PAGE 2", "OEFENINGEN · Exercícios da página 2"),
    ("Answers on page 8 · levels are mixed; find your number",
     "Respostas na página 8 · Níveis misturados: procure pelo número"),
    ("Read the article on page 2 and choose the right answer.", "Leia o artigo da página 2 e escolha a resposta certa."),
    ("Fill in with words from page 2.", "Complete com palavras da página 2."),
    ("Fill in the colour codes and dates.", "Complete com os códigos de cor e as datas."),
    ("Not a Climate Week action: driving more", "Não é uma ação da Semana do Clima: dirigir mais"),
    ("Code red: very dangerous, stay indoors", "Código vermelho: muito perigoso, fique em casa"),
    ("Warnings are local, not for a whole province", "Os avisos são locais, não para uma província inteira"),
    ("Saving energy: turning the heating down one degree", "Poupar energia: baixar o aquecimento em um grau"),
    ("The Climate Week, 2–8 November, lasts 7 days", "A Semana do Clima, de 2 a 8 de novembro, dura 7 dias"),
    ('"wortelen = to take root (plural subject)"', '"wortelen = criar raízes (sujeito no plural)"'),
    ('"besparen = to save",', '"besparen = poupar",'),
    ('"fiets = bicycle"', '"fiets = bicicleta"'),
    ("The giveaway place is Zweeloo", "O local da distribuição é Zweeloo"),
    ("Code yellow: take care", "Código amarelo: tome cuidado"),
    ("Code orange: dangerous", "Código laranja: perigoso"),
    ("The giveaway starts at 13:00", "A distribuição começa às 13h00"),
    ("The Climate Week ends on Sunday 8 November", "A Semana do Clima termina no domingo, 8 de novembro"),
    ('"Klimaatweek = Climate Week b"', '"Klimaatweek = Semana do Clima b"'),
    ('"besparen = to save d"', '"besparen = poupar d"'),
    ('"waarschuwing = warning a"', '"waarschuwing = aviso a"'),
    # ---- P3 ----
    ("CULTUUR · CULTURE", "CULTUUR · Cultura"),
    ("NIVEAU A2 → B1 · Museumnacht, boeken en kunst · Museum Night, books and art",
     "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · Noite dos Museus, livros e arte"),
    ("het museum = museum · de rondleiding = guided tour · het tijdslot = time slot · tweedehands = second-hand · de beurs = fair, market.",
     "het museum = museu · de rondleiding = visita guiada · het tijdslot = horário marcado · tweedehands = em segunda mão · de beurs = feira, mercado."),
    ("OEFENINGEN · EXERCISES ON PAGE 3", "OEFENINGEN · Exercícios da página 3"),
    ("Read the article on page 3 and choose the right answer.", "Leia o artigo da página 3 e escolha a resposta certa."),
    ("Fill in with the words from the box. Note: some words must become plural.",
     "Complete com as palavras do quadro. Nota: algumas palavras têm de ir para o plural."),
    ("Complete with the present perfect. Watch the auxiliary verbs hebben/zijn.",
     "Complete com o pretérito perfeito. Atenção aos verbos auxiliares hebben/zijn."),
    ("Work it out: answer with the numbers from page 3.", "Calcule: responda com os números da página 3."),
    ("The museums are open until 02:00", "Os museus ficam abertos até as 2h00"),
    ("Crossing Border is in The Hague", "O Crossing Border é em Haia"),
    ("Crossing Border combines books and music", "O Crossing Border combina livros e música"),
    ("The PAN art fair runs until 8 November", "A feira de arte PAN vai até 8 de novembro"),
    ("museum plural: musea", "plural de museum: musea"),
    ("rondleiding = guided tour", "rondleiding = visita guiada"),
    ("tijdslot = time slot", "tijdslot = horário marcado"),
    ("tweedehands = second-hand", "tweedehands = em segunda mão"),
    ("beurs = fair, market", "beurs = feira, mercado"),
    ("zijn perfectum: zijn geweest", "perfectum de zijn: zijn geweest"),
    ("kopen perfectum: hebben gekocht", "perfectum de kopen: hebben gekocht"),
    ("voorlezen perfectum: hebben voorgelezen", "perfectum de voorlezen: hebben voorgelezen"),
    ("komen takes zijn: zijn gekomen", "komen leva zijn: zijn gekomen"),
    ("19:00 to 02:00 is 7 hours", "De 19h00 às 2h00 são 7 horas"),
    ("1–8 November is 8 days", "De 1 a 8 de novembro são 8 dias"),
    ("3–8 November is 6 days", "De 3 a 8 de novembro são 6 dias"),
    ("Half of 250 is 125", "A metade de 250 é 125"),
    # ---- P4 ----
    ("NIVEAU B1 · Europese week en speelronde 12 · European week and matchday 12",
     "NIVEAU B1 · Europese week en speelronde 12 · Semana europeia e 12.ª rodada"),
    ("de balans = the final tally · gelijkspelen = to draw · de speelronde = matchday · de topper = the top match · de stand = the table.",
     "de balans = o balanço final · gelijkspelen = empatar · de speelronde = rodada · de topper = o grande jogo · de stand = a classificação."),
    ("OEFENINGEN · EXERCISES ON PAGE 4", "OEFENINGEN · Exercícios da página 4"),
    ("Read the article on page 4 and choose the right answer.", "Leia o artigo da página 4 e escolha a resposta certa."),
    ("Fill in with the words from the box. Watch the verb forms.",
     "Complete com as palavras do quadro. Atenção às formas verbais."),
    ("Complete with the past tense or the perfect tense.", "Complete com o pretérito ou o pretérito perfeito."),
    ("Ajax beat Atalanta 2–0", "O Ajax venceu o Atalanta por 2–0"),
    ("Twente beat Lincoln 4–1", "O Twente venceu o Lincoln por 4–1"),
    ("NEC lost 2–4 to Dinamo Zagreb", "O NEC perdeu por 2–4 para o Dínamo Zagreb"),
    ("Real Betis beat Feyenoord 1–0", "O Real Betis venceu o Feyenoord por 1–0"),
    ("After 10 rounds Feyenoord lead with 24 points", "Após 10 rodadas, o Feyenoord lidera com 24 pontos"),
    ("balans = the final tally", "balans = o balanço final"),
    ("gelijkspelen past tense plural: speelden gelijk", "pretérito plural de gelijkspelen: speelden gelijk"),
    ("topper = the top match", "topper = o grande jogo"),
    ("stand = the table", "stand = a classificação"),
    ("doelpunt = goal", "doelpunt = gol"),
    ("winnen past tense: won", "pretérito de winnen: won"),
    ("gaan past tense: ging", "pretérito de gaan: ging"),
    ("verliezen past tense: verloor", "pretérito de verliezen: verloor"),
    ("komen perfectum takes zijn", "perfectum de komen leva zijn"),
    ("True: Ajax won 2–0", "Verdadeiro: o Ajax venceu por 2–0"),
    ("False: NEC lost 2–4", "Falso: o NEC perdeu por 2–4"),
    ("False: Twente–Ajax is at 13:30; 11:15 is Heerenveen–Feyenoord",
     "Falso: Twente–Ajax é às 13h30; 11h15 é Heerenveen–Feyenoord"),
    ("True: after 10 rounds Feyenoord lead with 24 points",
     "Verdadeiro: após 10 rodadas, o Feyenoord lidera com 24 pontos"),
]

from transform_pt2 import MAP2
MAP = MAP + MAP2

# FIX1 (first-render defect, wording-only, explanation layer):
# P1 headline flow overflowed: the PT bridge runs 4 lines (EN 3), so the
# numbers box missed col 1 by ~5px and jumped to col 2 top, and exercise
# 6's tail line overprinted the col-2 mini-feature head. Shortening the
# P1 numbers-box item-4 parenthetical by one wrapped line (-27px) puts
# the box back in col 1 (box total 488 -> 461; 1333.2+461+12=1806.2 < 1828).
FIX1 = [
    ("(os jogos da 12.ª rodada da Eredivisie)", "(os jogos da rodada 12)"),
]
MAP = MAP + FIX1

# FIX2 (found by freeze-diff review of the fix1 render):
# (a) Two substring-order corruptions: a shorter MAP old was replaced
# inside a longer note/phrase before the longer entry ran, because the
# shorter entry precedes it in MAP order:
#  - 'ADE turned 30 this year' inside 'False: ADE turned 30 this year'
#    -> rendered 'False: O ADE fez 30 anos este ano' (EN 'False:' kept).
#  - 'Ajax beat Atalanta 2–0' inside the P7 phrase translation
#    'On Thursday 22 October Ajax beat Atalanta 2–0.'
#    -> rendered 'On Thursday 22 October O Ajax venceu o Atalanta por 2–0.'
# (b) Five missed strings: one P1 furniture head, one P8 note reused by
# three items, one P8 D-group note, and two f-string forms (NWORDS)
# whose literal '(87 words)' never matched the source.
FIX2 = [
    ("False: O ADE fez 30 anos este ano", "Falso: o ADE fez 30 anos este ano"),
    ("On Thursday 22 October O Ajax venceu o Atalanta por 2–0.",
     "Na quinta-feira, 22 de outubro, o Ajax venceu o Atalanta por 2–0."),
    ("HET NIEUWS · TOP STORY", "HET NIEUWS · Manchete"),
    ("Coevorden gives away 200 trees and shrubs", "Coevorden distribui 200 árvores e arbustos"),
    ("Subject + verb + time", "Sujeito + verbo + tempo"),
    ('f"Writing task (no single answer); model text ({NWORDS} words) below."',
     'f"Tarefa de escrita (sem resposta única); modelo ({NWORDS} palavras) abaixo."'),
    ('f"See the model text in section H ({NWORDS} words)"',
     'f"Ver o modelo na seção H ({NWORDS} palavras)"'),
]
MAP = MAP + FIX2

# FIX3 (occlusion audit on the fix2 render: 1 NEW flag):
# P1 word-of-the-week PT gloss ran 3 lines; its last line ('clima.',
# baseline 1897.6) sat inside the IN HET KORT box (y 1874-2304) and was
# 100% covered, and line 2 grazed the box top edge. Shortening the gloss
# to one measured line (393.1px < 434px column; the dropped second clause
# merely repeats the frozen Dutch sentence directly above it) clears
# both the y=1853 rule and the box top.
FIX3 = [
    ("«Clima»: o tempo e a natureza à nossa volta, a longo prazo. A Semana do Clima é sobre o nosso clima.",
     "«Clima»: o tempo e a natureza a longo prazo."),
]
MAP = MAP + FIX3

# FIX4 (KIT-review furniture catch): the donor's P4 band title is the
# bare word 'SPORT' (identical in English and Dutch), but the shipped
# W43 NL x PT band title reads 'SPORT · Esporte'. Furniture follows the
# W43 measured SVG, so the band title gains its PT second element.
FIX4 = [
    ('p.band("SPORT", "De Lucerna"', 'p.band("SPORT · Esporte", "De Lucerna"'),
]
MAP = MAP + FIX4

# FIX5 (B1, proof round W45 NL x PT: P2 D-section instruction overflow):
# the PT instruction at x=1647, 19.5pt measured 286.3px advance, ink
# right 1933.2px — past the inner frame 1910.6px and outer frame
# 1923.7px; the P2 card crop showed the final 'o' cut by both frame
# lines. Shortened single-line form 'Ligue palavra-significado'
# measures 227.2px advance, ink right 1874.2px (<= 1885px column bound,
# 36.4px clear of the inner frame). No question/answer touched.
# P2-ONLY by construction: the trailing 'e.end_report()' anchors the
# P2 match_set in content12.py; the identical P8 instruction in
# content8.py (followed by f.head("G ...")) is NOT matched, so P8
# stays byte-identical and the global MAP2 entry is left unchanged.
FIX5 = [
    ('instr="Associe a palavra ao significado")\ne.end_report()',
     'instr="Ligue palavra-significado")\ne.end_report()'),
]
MAP = MAP + FIX5

def main():
    total = 0
    for fname in FILES:
        path = os.path.join(HERE, fname)
        text = open(path, encoding="utf-8").read()
        for old, new in MAP:
            if old == new:
                continue
            n = text.count(old)
            if n:
                text = text.replace(old, new)
                total += n
        open(path, "w", encoding="utf-8").write(text)
    # assertion pass: no old (non-identity) string may survive anywhere
    missing = []
    for fname in FILES:
        text = open(os.path.join(HERE, fname), encoding="utf-8").read()
        for old, new in MAP:
            if old != new and old in text:
                missing.append((fname, old))
    if missing:
        print("SURVIVING OLD STRINGS:", len(missing))
        for f, o in missing:
            print(" ", f, repr(o))
        sys.exit(1)
    print(f"transform ok: {total} replacements across {len(FILES)} files; 0 old strings survive")

if __name__ == "__main__":
    main()

