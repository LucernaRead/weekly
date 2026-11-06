# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-pt-proof/work/repro-out")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Teste e gabarito", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · O teste da semana e todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Verdadeiro ou falso", 21, OLIVE, 5)
f.ex("A2", "Escolha no contexto", "A", "O Início do Inverno é em 7 de novembro.",
     "立冬在11月7日。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Escolha no contexto", "B", "立冬 é o 19º termo solar, não o 18º.",
     "立冬是第18个节气。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Escolha no contexto", "B", "As mercadorias imediatas despacham sem espera de sinal.",
     "现货要先付定金才能买。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "B", "A AL perdeu as três séries da fase suíça.",
     "AL赢了三场比赛。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "A", "As quartas de final começam às 06:00, hora de Pequim.",
     "四分之一决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "B", "O filme de IA não tem atores reais.",
     "《三星堆》电影里有真人演员。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "A", "O novo filme estreia em 7 de novembro.",
     "新片《我们仅有一次的人生》11月7日上映。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "B", "O Dia dos Jornalistas é em 8 de novembro, não em 7 de novembro.",
     "中国记者节在11月7日。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · O grande quiz", 21, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "B", "As vendas imediatas vão até 13 de novembro.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "O momento do termo solar é às 17h52.",
     "立冬交节在几点? A. 17点52分 · B. 18点52分 · C. 7点52分", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Primeira microestação: a água começa a congelar.",
     "立冬三候第一候是什么? A. 地始冻 · B. 水始冰 · C. 雉入大水为蜃", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "C", "A IG venceu a HLE em 26 de outubro.",
     "IG打赢了哪个队? A. G2 · B. KC · C. HLE", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "A TES venceu a G2 em 26 de outubro.",
     "TES打赢了哪个队? A. HLE · B. G2 · C. TL", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "Ao meio-dia de 26 de outubro, o Maoyan mostrava cerca de 1,192 milhão de yuan.",
     "AI电影票房约多少? A. 119.2万元 · B. 1192万元 · C. 11.92万元", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Huang Yan é funcionária de crematório.",
     "新片里黄燕是什么职业? A. 记者 · B. 火化师 · C. 老师", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "O evento da loja do WeChat dura 35 dias.",
     "微信小店活动多少天? A. 35天 · B. 13天 · C. 18天", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "A cesta A paga 270 yuan depois do corte.",
     "篮子A实付多少钱? A. 270元 · B. 320元 · C. 240元", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "A final começa às 03:00, hora de Pequim, em 15 de novembro.",
     "总决赛在北京时间哪天? A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=13.8, gap=0)
f.head("C · 完成句子 · Complete as frases", 21, OLIVE, 5)
f.ex("A2", "Complete a frase", "立冬", "O Início do Inverno é em 7 de novembro.",
     "11月7日是___。", instr="Complete", size=13.8, gap=0)
f.ex("A2", "Complete a frase", "直降", "zhíjiàng — o preço em si cai.",
     "价格直接变低,这叫___。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "艾伦", "Àilún — Allen, no Texas, sedia a fase suíça.",
     "瑞士轮在美国___市举行。", instr="Complete", size=13.8, gap=0)
f.ex("A2", "Complete a frase", "饺子", "jiǎozǐ — as famílias do norte comem estes no 立冬.",
     "北方立冬吃___。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "数字", "shùzì — os personagens do filme de IA são imagens digitais.",
     "AI电影的角色是___形象。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "票房", "piàofáng — a bilheteria.",
     "电影卖票的钱叫___。", instr="Complete", size=13.8, gap=0)
f.ex("B2", "Complete a frase", "结算", "jiésuàn — a página de checkout mostra o preço real.",
     "真正要付的钱,看___页。", instr="Complete", size=13.8, gap=0)
f.ex("A2", "Complete a frase", "补冬", "bǔdōng — comer bem antes do inverno.",
     "冬天以前吃点好的,这叫___。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "记者", "jìzhě — um jornalista entrevista e escreve notícias.",
     "采访和写新闻的人,叫___。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "立减", "lìjiǎn — desconto no checkout.",
     "结算时直接减掉的钱叫___。", instr="Complete", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Leia e responda", 21, OLIVE, 5)
f.para("小红住在北京。11月7日星期六是立冬,她早上和妈妈一起包饺子,中午吃了热热的饺子。下午,她在网上买了一条围巾,现货第二天就到了。11月8日星期日,她给奶奶打了电话,问奶奶冷不冷。奶奶说,家里很暖和,让她多穿衣服。", 15, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "A", "Xiao Hong mora em Pequim.",
     "小红住在哪里? A. 北京 · B. 上海 · C. 广州", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "No 立冬, ela fez bolinhos com a mãe.",
     "立冬那天她做了什么? A. 包饺子 · B. 看比赛 · C. 买毛衣", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Ela comprou um cachecol on-line.",
     "她买了什么? A. 毛衣 · B. 围巾 · C. 帽子", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Ela telefonou para a avó no domingo.",
     "她给谁打了电话? A. 妈妈 · B. 奶奶 · C. 老师", size=13.8, gap=0)
f.ex("B2", "Escolha múltipla", "A", "Ordem: bolinhos, depois compras, depois o telefonema.",
     "这段话的顺序是什么? A. 先包饺子,再买围巾,再打电话 · B. 先打电话,再包饺子 · C. 先买围巾,再包饺子", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "北京", "Xiao Hong mora em Pequim.",
     "小红住在___。", instr="Complete", size=13.8, gap=0)
f.head("E · 情景说话 · Em conversa", 21, OLIVE, 5)
f.ex("B1", "Escolha no contexto", "A", "As mercadorias imediatas despacham na hora, sem espera de pré-venda.",
     "— 现货几天能到? — 买了就能___,不用等预售。(A. 发货 · B. 退货)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "A", "As famílias do norte comem bolinhos no 立冬.",
     "— 立冬吃什么? — 北方吃___,南方吃法各不同。(A. 饺子 · B. 月饼)", size=13.8, gap=0)
f.ex("B2", "Escolha no contexto", "A", "A regra da página 6: dados primeiro, propaganda por último.",
     "— 这条新闻说最低价,可信吗? — 先看___,再看广告。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Escrita", 21, OLIVE, 5)
MODELO = ("这个周末是立冬。星期六早上,我和妈妈一起包饺子,吃了热热的饺子,身体很暖和。"
          "下午,我去买了一件毛衣,现货第二天就到了。星期日,我给奶奶打了电话,问她冷不冷。"
          "冬天来了,我想多陪陪家人,过一个暖和的冬天。"
          "晚上,我看了S16的比赛,早上6点开始,很好看。双11还没结束,我又买了一条围巾,直降以后便宜了不少。"
          "这个冬天,我要早点睡觉,多穿衣服,不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Escrita — não há uma única resposta certa. Segue um texto-modelo de {NCHARS} caracteres.")
f.ex("B1", "Escrita", "(开放题，范文如下)", f"Pergunta aberta — o modelo está na seção F acima ({NCHARS} caracteres)",
     "写一写《我的立冬周末》:立冬那天你做了什么?买了什么?冬天来了,你想做什么?写 120~180 字。", instr="Escreva", size=13.8, gap=0)
f.para("Texto-modelo: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Gabarito — por página, com uma nota em cada resposta", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Todas as notas em português · ✓ = a tarefa de escrita", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Página {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escrita":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ceyan.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
