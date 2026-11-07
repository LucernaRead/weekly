# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · TEST UND LÖSUNGEN", "A Lucerna", "SEITE 8 · A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "voltar às urnas = wählen gehen",
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "4.352 Wahllokale neu",
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "letzte Debatte am Freitag, 23.",
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Vasco ist ausgeschieden",
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "Gitarren-Suchen seit 2021 +53 %",
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "Enem-Prüfungen im November",
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "die meisten gültigen Stimmen gewinnen",
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "keine Sommerzeit, die Uhr bleibt",
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "Wahl 8–17 Uhr, Brasília-Zeit",
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", "单选", "B", "die 982 liegen in São Paulo",
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", "单选", "A", "Moderator: César Tralli",
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", "单选", "C", "Davi Lacerda pfeift Grêmio × Atlético-MG",
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", "单选", "B", "Prova do Fazendeiro am Mittwoch",
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", "单选", "A", "die Karte gehört zum Enem",
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", "单选", "B", "+900 % = Suchinteresse",
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", "单选", "B", "Finados am 2. November",
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Marina wohnt in São Paulo",
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", "单选", "A", "ihr Wahllokal hat eine neue Adresse",
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", "单选", "B", "sie sah es in der App e-Título",
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", "单选", "A", "der Titel fasst den Text zusammen",
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "Domingo é dia de decisão.", "Zeitangabe zuerst",
     "domingo / é / dia de decisão → ___", instr="Sätze bilden", size=14.5, gap=0)
f.ex("B1", "造句", "O eleitor confere o local no aplicativo.", "Subjekt + Verb + Objekt + Ort",
     "o eleitor / confere / o local / no aplicativo → ___", instr="Sätze bilden", size=14.5, gap=0)
f.ex("B1", "造句", "Que horas começa a votação?", "Fragewort am Anfang",
     "que horas / começa / a votação / ? → ___", instr="Sätze bilden", size=14.5, gap=0)
f.ex("B1", "造句", "O Vasco perdeu por 3 a 1.", "Subjekt + Verb + Ergebnis",
     "o Vasco / perdeu / por 3 a 1 → ___", instr="Sätze bilden", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻译", "Am Sonntag kehrt Brasilien an die Wahlurnen zurück.", "vgl. die Schlagzeile auf Seite 1",
     "Domingo, o Brasil volta às urnas. → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B1", "翻译", "Prüfen Sie Ihren Wahlort, bevor Sie losgehen.", "Confira = prüfen Sie",
     "Confira o seu local antes de sair de casa. → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B1", "翻译", "As buscas por guitarra cresceram 53%.", "cresceram = sind gestiegen",
     "Die Suchen nach «guitarra» sind um 53 % gestiegen. → ___", instr="Übersetzen", size=14.5, gap=0)
f.ex("B2", "翻译", "Quando você chegar, confira a seção.", "Futuro do Subjuntivo (chegar) + Imperativ confira",
     "Wenn Sie ankommen, prüfen Sie bitte Ihr Wahllokal. → ___", instr="Übersetzen", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ["segundo turno = Stichwahl der zwei Besten: b", "seção = der genaue Wahlort: d", "justificar = Abwesenheit begründen: a", "maioria absoluta = mehr als die Hälfte: c"],
            instr="Zuordnen")
f.head("G · DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "documento com foto = Ausweis mit Foto",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "seção = das konkrete Wahllokal (Raum)",
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "an der Urne: digita = Zahl eintippen",
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "grüne Taste = confirma",
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "obrigado = danke",
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
f.bridge(f"Schreibaufgabe (offen); Mustertext ({NWORDS} Wörter) unten.")
f.ex("B1", "写作", "(offene Aufgabe — Mustertext unten)", f"Mustertext in Bereich H auf dieser Seite ({NWORDS} Wörter)",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr="Schreiben", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · LÖSUNGEN — nach Seiten geordnet, nach Nummer suchen", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Jede Nummer mit kurzer deutscher Erklärung · ✓ = Aufgabe mit Mustertext", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
