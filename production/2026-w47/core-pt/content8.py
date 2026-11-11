# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　练习与答案", "A Lucerna", "第8版　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "A", "11 月 20 日周五是全国假日",
     "Sexta, 20 de novembro, é ___ no Brasil. (A. feriado nacional · B. dia útil)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "假日纪念祖比·帕尔马雷斯",
     "O feriado lembra a morte de ___ . (A. Zumbi dos Palmares · B. Deodoro da Fonseca)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "2026 年假日落在周五",
     "Em 2026, o feriado cai numa ___ . (A. segunda · B. sexta)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "巴西杯决赛在 12 月 6 日",
     "A final da Copa do Brasil é no dia ___ de dezembro. (A. 6 · B. 15)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "决赛：格雷米奥 × 帕尔梅拉斯",
     "Na final, jogam Grêmio e ___ . (A. Vasco · B. Palmeiras)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "官方答案 11 月底前公布",
     "O gabarito oficial sai até o ___ de novembro. (A. fim · B. dia 8)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "高考第二天在 11 月 15 日",
     "O segundo dia do Enem foi no domingo ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.ex("B1", "完形单选", "B", "第二天考试 5 小时",
     "No dia 15, a prova dura ___ horas. (A. três · B. cinco)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "2023 年法律将 11 月 20 日定为全国假日",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=14.5, gap=0)
f.ex("B1", "单选", "A", "格雷米奥总比分 3 比 1 晋级",
     "O Grêmio passou à final com... A. 3 a 1 no total · B. 2 a 2 no total · C. 1 a 0 no total", size=14.5, gap=0)
f.ex("B1", "单选", "B", "点球 5 比 4，帕尔梅拉斯晋级",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=14.5, gap=0)
f.ex("B1", "单选", "B", "诺里斯赢得圣保罗大奖赛",
     "O Grande Prêmio de São Paulo foi vencido por... A. Verstappen · B. Norris · C. Hadjar", size=14.5, gap=0)
f.ex("B1", "单选", "A", "第 36 轮帕尔梅拉斯 × 弗拉门戈在周六 21 日",
     "A rodada 36 tem Palmeiras × Flamengo no... A. sábado 21 · B. domingo 22 · C. dia 15", size=14.5, gap=0)
f.ex("A2", "单选", "B", "卡波耶拉是非洲裔巴西人的格斗与音乐艺术",
     "A capoeira é... A. um jogo de cartas · B. uma arte afro-brasileira de luta e música · C. um prato típico", size=14.5, gap=0)
f.ex("B2", "单选", "A", "10 是到官方答案为止的工作日天数",
     "O número 10, na página 6, mede... A. os dias úteis até o gabarito · B. os gols da final · C. os feriados", size=14.5, gap=0)
f.ex("B1", "单选", "A", "帕尔马雷斯在阿拉戈斯州",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Rafael mora em Salvador. Na sexta, 20, ele não trabalha: é feriado nacional. De manhã, ele vai a uma roda de capoeira no Pelourinho. À tarde, ele lê sobre Zumbi e Palmares e escreve duas frases em português. No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão. No domingo, 22, ele descansa e prepara a semana: na segunda, ele volta ao trabalho e confere o gabarito extraoficial do Enem.", 15.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "拉斐尔住在萨尔瓦多",
     "Onde mora Rafael? A. no Rio · B. em Salvador · C. em Brasília", size=14.5, gap=0)
f.ex("A2", "单选", "B", "周五他去参加卡波耶拉活动",
     "Na sexta, 20, Rafael... A. trabalha · B. vai a uma roda de capoeira · C. faz o Enem", size=14.5, gap=0)
f.ex("A2", "单选", "A", "周六他看帕尔梅拉斯 × 弗拉门戈",
     "No sábado, 21, Rafael assiste... A. a Palmeiras × Flamengo · B. ao Enem · C. a uma aula", size=14.5, gap=0)
f.ex("A2", "单选", "B", "周一他核对非官方答案",
     "Na segunda, Rafael confere... A. o gabarito oficial · B. o gabarito extraoficial · C. a nota final", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "Sexta é feriado nacional.", "时间词在前",
     "sexta / é / feriado nacional → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "O Grêmio empatou por 1 a 1.", "主语 + 动词 + 方式",
     "o grêmio / empatou / por 1 a 1 → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "Quando sair o gabarito, confira as respostas.", "时间从句 + 主句",
     "quando / sair / o gabarito / confira / as respostas → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "O Brasil lembra Zumbi em 20 de novembro.", "主语 + 动词 + 宾语 + 时间",
     "o brasil / lembra / zumbi / em 20 de novembro → ___", instr="造句", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻译", "11 月 20 日周五是全国假日。", "对照第 1 版头条",
     "Sexta, 20 de novembro, é feriado nacional. → ___", instr="翻译", size=14.5, gap=0)
f.ex("B1", "翻译", "帕尔梅拉斯在点球大战中 5 比 4 获胜。", "nos pênaltis = 在点球大战中",
     "O Palmeiras venceu nos pênaltis por 5 a 4. → ___", instr="翻译", size=14.5, gap=0)
f.ex("B1", "翻译", "O gabarito oficial sai até o fim de novembro.", "oficial = 官方的",
     "“官方答案在 11 月底前公布。” → ___", instr="翻译", size=14.5, gap=0)
f.ex("B2", "翻译", "Anote as suas respostas e confira quando sair o gabarito oficial.", "祈使式 anote/confira + quando 从句",
     "“把你的答案记下来，等官方答案出来再核对。” → ___", instr="翻译", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["a consciência", "o gabarito", "o feriadão", "o agregado"],
            ["o placar dos dois jogos somados",
             "um fim de semana de três dias com feriado",
             "o saber e a memória de uma história",
             "as respostas oficiais das questões objetivas"],
            ["c", "d", "b", "a"],
            ["consciência=知晓与记忆 c", "gabarito=客观题官方答案 d", "feriadão=带假日的三天周末 b", "agregado=两回合总比分 a"],
            instr="把词和释义配对")
f.head("G　DIÁLOGO NA BILHETERIA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "A", "马内·加林查体育场",
     "— O jogo é no ___ Garrincha. (A. Mané · B. Maracanã)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "格雷米奥冲击第六冠",
     "— O Grêmio busca o ___ título. (A. sexto · B. primeiro)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "帕尔梅拉斯冲击第五冠",
     "— E o Palmeiras busca o ___ . (A. quinto · B. décimo)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "门票在网上出售",
     "— Os ingressos estão à venda ___ internet. (A. na · B. no)", size=14.5, gap=0)
f.ex("B1", "完形单选", "A", "obrigado = 谢谢",
     "— Boa final! — Muito ___! (A. obrigado · B. tarde)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Sexta, 20 de novembro, acordo sem despertador: é feriado nacional. "
          "De manhã, leio sobre Zumbi e Palmares e escrevo duas frases em português. "
          "À tarde, vou a uma roda de capoeira no bairro e ouço histórias de resistência. "
          "No sábado, assisto a Palmeiras × Flamengo na televisão, com a família. "
          "No domingo, descanso, preparo a semana e confiro o gabarito extraoficial do Enem. "
          "Na segunda, volto ao trabalho com calma: o feriadão foi curto, mas a memória fica. "
          "O dia 20 lembra a luta e a cultura afro-brasileiras.")
NWORDS = len(MODELO.split())
f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")
f.ex("B1", "写作", "（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）",
     "«O seu feriadão de 20 a 22 de novembro» Escreva 80–100 palavras: o que você faz na sexta, no sábado e no domingo, e o que a data de 20 de novembro lembra.", instr="写作", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False, max_w=395)  # fix1 D7 (2026-11-11): wrap at 395, not the full 422.5 column — Cairo renders Newsreader ~3% wider than PIL measures, so two lines crossed the column edge 1862 (+2/+14px). Words, size (15) and 88-word count unchanged; worst line PIL 387.0, predicted rendered ink right ~1841.
f.end_report()
print("P8 exercises end y:", f.y, "col:", f.ci)

# ---- P8 image: the final stadium (col 3, below the exercises flow) ----
# The exercise flow fills cols 0-2 to the bottom; only its last column has
# free space below f.y, so the image goes there, positioned dynamically.
iy8 = (f.y + 12) if f.ci == 3 else 190
img_h = min(250, 1150 - iy8)
assert img_h >= 150, f"P8 image has no room: f.y={f.y} ci={f.ci}"
image(p, "garrincha.jpg", COLX[3], iy8, CW, img_h)
cap_end = caption(p, COLX[3], iy8 + img_h, CW,
        "O estádio Mané Garrincha, em Brasília: a final é no dia 6 de dezembro.",
        "Foto: Luis Dantas — Domínio público")
print("P8 image ends ~", cap_end)

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　参考答案 — 按版面分页排列，找到题号即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每题附一句中文简析　带 ✓ 的为范文题", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
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
