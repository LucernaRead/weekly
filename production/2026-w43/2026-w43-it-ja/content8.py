# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band('VALUTAZIONE E RISPOSTE · 演習と答え', "La Lucerna", '8 ページ · La grande prova della settimana + tutte le risposte')

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", '空所補充・選択', "B", 'tornare indietro = 戻す',
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "A", '時刻変更の夜は25時間',
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "A", 'incontrare = 対戦する',
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "A", 'ナポリ–ローマは土曜',
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "A", 'モンタイオーネはトリュフ祭り',
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "B", '映画祭は日曜に閉幕：chiude',
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "A", 'ルッカは10月28日に開幕：apre',
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "B", '10月28日は水曜日',
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", '選択肢', "B", '03:00 が 02:00 に戻る',
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", '選択肢', "B", '«meteo oggi» は検索第1位',
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", '選択肢', "A", '嵐の名前は Adam',
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", '選択肢', "B", '白トリュフ祭りはアルバ',
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", '選択肢', "C", 'アルテミジア展はフィレンツェ',
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", '選択肢', "A", 'DPB は10月15日に送られた',
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", '選択肢', "B", 'DPB の数字は予測',
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", '選択肢', "B", '諸聖人の日は今年11月1日の日曜日',
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", '選択肢', "B", 'Giulia がルッカ・コミックスへ行く',
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", '選択肢', "A", 'Paolo は日曜に映画祭へ',
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", '選択肢', "B", 'コスプレは Giulia のもの',
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", '選択肢', "A", 'タイトルは2つの町と2つの祭りをまとめている',
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", '文を作る', "Domenica dormiamo un'ora in più.", '時の言葉が前',
     "domenica / dormiamo / un'ora in più → ___", instr='文を作る', size=15.5, gap=1)
f.ex("B1", '文を作る', "La fiera è iniziata il 10 ottobre.", '主語 + essere + 分詞 + 日付',
     "la fiera / è iniziata / il 10 ottobre → ___", instr='文を作る', size=15.5, gap=1)
f.ex("B1", '文を作る', "A che ora comincia la partita?", '疑問詞句が文頭',
     "a che ora / comincia / la partita / ? → ___", instr='文を作る', size=15.5, gap=1)
f.ex("B1", '文を作る', "Il voto slitta a mercoledì.", '主語 + 動詞 + 前置詞句',
     "il voto / slitta / a mercoledì → ___", instr='文を作る', size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", '翻訳', '日曜日、私たちは1時間長く眠ります。', '原文と比べなさい',
     "Domenica dormiamo un'ora in più. → ___", instr='翻訳', size=15.5, gap=1)
f.ex("B1", '翻訳', '展覧会は4月までずっと開いています。', 'resta aperta = 開いたまま続く',
     "La mostra resta aperta fino ad aprile. → ___", instr='翻訳', size=15.5, gap=1)
f.ex("B1", '翻訳', "Sabato alle 18:00 si gioca Napoli–Roma.", 'si gioca = 試合が行われる',
     '土曜18時、ナポリ対ローマ。→ ___', instr='翻訳', size=15.5, gap=1)
f.ex("B2", '翻訳', "Ogni cifra deve avere una fonte.", 'dovere = 〜なければならない',
     'すべての数字には出典が必要です。→ ___', instr='翻訳', size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", '語と意味を結ぶ',
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ['manovra=国の予算法 b', 'rinvio=予定より遅れて届く c', 'miliardo=10億 d', 'previsione=未来を表す数字 a'],
            instr='語と意味を結ぶ')
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", '空所補充・選択', "B", 'tartufo = トリュフ',
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "A", 'castagne arrosto 焼き栗',
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "B", 'quanto costa? いくらですか',
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "A", 'pagare con carta カードで払う',
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", '空所補充・選択', "B", '食の祭りは日曜まで続く',
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"作文問題（答えは一つではありません）；模範文（{NWORDS} 語）は以下です。")
f.ex("B1", '作文', '（自由作文、模範文は以下）', f"模範文はこのページの H 欄（{NWORDS} 語）",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr='作文', size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, 'RISPOSTE · 全解答と解説（1–8ページ）', 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, '各問に日本語の短い解説つき · ✓ は模範文のある問題', 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == '作文':
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
