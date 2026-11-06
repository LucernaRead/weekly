# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Teste e gabarito", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · O teste da semana e todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Verdadeiro ou falso", 21, OLIVE, 5)
f.ex("A2", "Escolha no contexto", "A", "Chóngyáng é o dia 9 do 9º mês lunar.",
     "重阳节在农历九月初九。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Escolha no contexto", "B", "Shuāngjiàng (23/out) vem DEPOIS de Chóngyáng (18/out).",
     "霜降在重阳节以前。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Escolha no contexto", "A", "Numa pré-venda, você paga primeiro o sinal.",
     "预售的时候先付定金。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "B", "A final do S16 é em Nova York; LA sediou os play-ins.",
     "S16 总决赛在洛杉矶。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Escolha no contexto", "A", "Os pagamentos do saldo abriram em 20 de outubro às 20:00.",
     "付尾款的时间是10月20日晚上8点。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "B", "A queda medida foi de cerca de 25,8%, não 40%.",
     "大闸蟹的价格真的降了40%。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "A", "Os homens da China: bronze, com 249.193 pontos.",
     "中国体操男队拿到铜牌。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "A", "Foi o 10º desfile da Victoria's Secret de Liu Wen.",
     "刘雯第十次走上维密的舞台。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · O grande quiz", 21, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "B", "As vendas imediatas vão até 13 de novembro.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "Caquis são a comida do Shuāngjiàng.",
     "霜降吃的是什么? A. 柿子 · B. 月饼 · C. 粽子", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "C", "A final feminina é à 01:30 de 22/out, hora de Pequim.",
     "体操女团决赛在北京时间几点? A. 10月21日上午 · B. 10月22日晚上8点 · C. 10月22日凌晨1点30分", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "Produção prevista de Yangcheng: cerca de 10.100 toneladas.",
     "阳澄湖大闸蟹预计总产量是多少? A. 约1.01万吨 · B. 约10.1万吨 · C. 约101万吨", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "C", "Shuāngjiàng é sexta-feira, 23 de outubro.",
     "霜降在10月几日? A. 20日 · B. 7日 · C. 23日", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "AL é o cabeça de chave nº 1 da LPL no S16.",
     "LPL 的四支队里,哪支是一号种子? A. BLG · B. AL · C. IG", size=13.8, gap=0)
f.ex("B2", "Escolha múltipla", "B", "Os preços na porteira estão quase no nível dos últimos 3 anos.",
     "协会说出水价怎么样? A. 涨了很多 · B. 和最近三年差不多 · C. 只有去年的一半", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "jiǔyuè yuánqí — as fêmeas primeiro, no 9º mês lunar.",
     "农历九月先吃什么蟹? A. 母蟹 · B. 公蟹 · C. 小蟹", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "C", "LeBron estreou com a camisa dos 76ers.",
     "詹姆斯穿上哪支队的球衣? A. 尼克斯 · B. 凯尔特人 · C. 76人", size=13.8, gap=0)
f.ex("B2", "Escolha múltipla", "A", "yuánqí = a aba ventral redonda da fêmea do caranguejo.",
     "「九月圆脐十月尖」里,「圆脐」说的是: A. 母蟹的肚脐形状 · B. 月亮的形状 · C. 蟹的大小", size=13.8, gap=0)
f.head("C · 完成句子 · Complete as frases", 21, OLIVE, 5)
f.ex("A2", "Complete a frase", "尾款", "Hora do saldo: 20 de outubro, 20:00.",
     "10月20日晚上8点付___。", instr="Complete", size=13.8, gap=0)
f.ex("A2", "Complete a frase", "定金", "Primeiro o sinal na pré-venda, o saldo depois.",
     "预售先付___,后付尾款。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "满减", "mǎnjiǎn — gaste 300, economize 50.",
     "买满300减50,这叫___。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "鹿特丹", "O Mundial de ginástica foi em Roterdã.",
     "体操世锦赛在荷兰___举行。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "艾伦", "A fase suíça do S16 é em Allen, no Texas.",
     "S16 瑞士轮在美国___市举行。", instr="Complete", size=13.8, gap=0)
f.ex("A2", "Complete a frase", "柿子", "Caquis no Shuāngjiàng evitam que os lábios rachem.",
     "霜降吃___,嘴唇不会裂。", instr="Complete", size=13.8, gap=0)
f.ex("B2", "Complete a frase", "滞销", "zhìxiāo — vende devagar, só em áreas periféricas.",
     "少数外围产区的蟹有点___,卖得慢。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "直播", "zhíbō — o desfile foi transmitido ao vivo.",
     "维密秀在网上___,很多人在线看。", instr="Complete", size=13.8, gap=0)
f.ex("B2", "Complete a frase", "声明", "shēngmíng — a declaração oficial da associação.",
     "协会发表___,说「崩盘」不是真的。", instr="Complete", size=13.8, gap=0)
f.ex("B1", "Complete a frase", "通宵", "tōngxiāo — acordado a noite toda pelo jogo.",
     "比赛在凌晨,看比赛的人要___。", instr="Complete", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Leia e responda", 21, OLIVE, 5)
f.para("小林住在上海。他在网上看中了一件外套,先付了30元定金。10月20日晚上8点,他付了尾款。周五是霜降,他下班后去超市买了柿子。周六凌晨1点,他起来看 S16 的瑞士轮比赛,AL 打得很好。看完比赛,他睡了一个好觉。", 15, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "B", "Ele pagou um sinal de 30 yuan.",
     "小林先付了多少钱定金? A. 20元 · B. 30元 · C. 50元", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "No Shuāngjiàng (sexta), comprou caquis depois do trabalho.",
     "霜降那天他做了什么? A. 下班后买柿子 · B. 陪妈妈爬山 · C. 通宵看比赛", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "C", "Ele assistiu à 01:00 de sábado.",
     "他看比赛的时间是? A. 周五晚上8点 · B. 周六上午 · C. 周六凌晨1点", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Ele assistiu à fase suíça do S16.",
     "他看的是哪个比赛? A. NBA · B. S16 瑞士轮 · C. 体操世锦赛", size=13.8, gap=0)
f.ex("B2", "Escolha múltipla", "A", "Ordem: compras, depois o termo solar, depois o jogo.",
     "这段话的顺序是什么? A. 先购物,再过节气,再看比赛 · B. 先看比赛,再购物 · C. 先过节气,再看比赛,再购物", size=13.8, gap=0)
f.ex("B2", "Complete a frase", "上海", "Xiao Lin mora em Xangai.",
     "小林住在___。", instr="Complete", size=13.8, gap=0)
f.head("E · 情景说话 · Em conversa", 21, OLIVE, 5)
f.ex("B1", "Escolha no contexto", "B", "A entrega começa depois que o saldo (wěikuǎn) é pago.",
     "— 我的包裹到了吗? — 付完___,快递就开始送了。(A. 定金 · B. 尾款)", size=13.8, gap=0)
f.ex("B1", "Escolha no contexto", "A", "bǔdōng bùrú bǔ shuāngjiàng — coma bem no Shuāngjiàng.",
     "— 霜降要多穿点吗? — 要。___不如补霜降,先吃点好的。(A. 补冬 · B. 补夏)", size=13.8, gap=0)
f.ex("B2", "Escolha no contexto", "A", "Regra da página 6: dados primeiro, manchete por último.",
     "— 这条新闻说价格崩盘,可信吗? — 先看___,再看标题。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Escrita", 21, OLIVE, 5)
MODELO = ("我的双11购物车里有三样东西:一件外套、一条围巾和一盒柿子。"
          "外套260元,围巾60元,柿子40元,一共360元。"
          "今年有满300减50的活动,实付310元。"
          "我在预售时先付了30元定金,10月20日晚上8点付尾款280元。"
          "付完尾款,我就等快递了。霜降快到了,我想穿新外套、吃甜柿子,过一个暖和的秋天。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Escrita — não há uma única resposta certa. Segue um texto-modelo de {NCHARS} caracteres.")
f.ex("B1", "Escrita", "(pergunta aberta — texto-modelo a seguir)", f"Pergunta aberta — o modelo está na seção F acima ({NCHARS} caracteres)",
     "写一写《我的双11购物车》:你想买什么?先付多少定金?尾款多少?一共多少钱?写 120~180 字。", instr="Escreva", size=13.8, gap=0)
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
        txt = f"{e_['n']}. {e_['key']} ({e_['note']})"
        if e_["type"] == "Escrita":
            txt = f"{e_['n']}. ✓ ({e_['note']})"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ceyan.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
