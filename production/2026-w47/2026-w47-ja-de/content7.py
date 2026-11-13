# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7　ことば (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("ことば　Sprache", "Lucerna", "言語フォーカス　三つのレベル、三つのテーマ　Drei Stufen, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　酉の市と熊手のことば", 24)
a.para("酉の市のことばを覚えましょう。『酉の市』は、11月の酉の日に開くお祭りです。『熊手』は、商売繁盛の縁起物です。『手締め』は、熊手を買った時に打つ拍手です。", 21.5)
a.para("『一番太鼓』は、午前0時の太鼓です。『見頃』は、いちばん美しい時です。『解禁』は、売り始める日です。", 21.5)
a.bridge("酉の市 Tori-no-ichi　熊手 kumade　手締め Händeklatschen")
a.ex("A2", "Auswahl", "B", "熊手 = ein Glücksbringer für florierende Geschäfte",
     "『熊手』の意味は？ A. 食べ物の名前　B. 商売繁盛の縁起物　C. 服の名前", instr="Auswahl", size=20.5, gap=10)
a.ex("A2", "Ausfüllen", "一番太鼓", "一番太鼓 = die Mitternachtstrommel",
     "午前0時の太鼓を「___」と言います。", instr="Ausfüllen", size=20.5, gap=10)
a.ex("A2", "Auswahl", "C", "手締め = das Händeklatschen beim Kauf",
     "『手締め』とは？ A. 食べること　B. 寝る　C. 買った時に打つ拍手", instr="Auswahl", size=20.5, gap=10)
a.ex("A2", "Ausfüllen", "2", "2026 gibt es zwei Tori-no-ichi-Feste",
     "2026年の酉の市は、___ 回です。", instr="Ausfüllen", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　流行語のことば", 24)
b.para("流行語のことばを覚えましょう。『りくりゅう』は、フィギュアスケートのペアです。『ちいかわ』は、大ヒットした漫画の名前です。『酷暑日』は、とても暑い日のことです。", 21.5)
b.para("『好きすぎて滅！』は、M!LKの楽曲の名前です。『ノミネート』は、候補に選ばれることです。30語がノミネートされました。", 21.5)
b.bridge("りくりゅう Eiskunstlauf-Paar　ちいかわ Chiikawa")
b.bridge("ノミネート Nominierung")
b.ex("B1", "Auswahl", "B", "rikuryuu ist ein Eiskunstlauf-Paar",
     "『りくりゅう』の意味は？ A. シールの名前　B. フィギュアスケートのペア　C. お酒の名前", instr="Auswahl", size=20.5, gap=10)
b.ex("B1", "Ausfüllen", "ちいかわ", "Der Hit-Manga heißt Chiikawa",
     "大ヒットした漫画の名前は「___」です。", instr="Ausfüllen", size=20.5, gap=10)
b.ex("B1", "Auswahl", "C", "ノミネート = nominiert werden",
     "ノミネートとは？ A. 優勝　B. 買う　C. 候補に選ばれること", instr="Auswahl", size=20.5, gap=10)
b.ex("B1", "Ausfüllen", "30", "30 Wörter wurden nominiert",
     "ノミネートは ___ 語です。", instr="Ausfüllen", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　数字を読む", 24)
c.para("数字の読み方を練習しましょう。『2勝1敗』は、2回勝って1回負けたことです。『金星』は、前頭の力士が横綱に勝つことです。藤凌駕は、3日目に金星をあげました。", 21.5)
c.para("『11場所』は、初土俵から11回目の場所です。『7番目』は、7番目に速い、という意味です。年6場所になってから、7番目の速さだそうです。", 21.5)
c.bridge("〜勝〜敗 Sieg–Niederlage　金星 kinboshi　〜番目 Nr. 〜")
c.ex("B2", "Auswahl", "B", "2–1 = 2 Siege, 1 Niederlage",
     "『2勝1敗』の意味は？ A. 2回負けて1回勝つ　B. 2回勝って1回負ける　C. 2回引き分ける", instr="Auswahl", size=20.5, gap=10)
c.ex("B2", "Auswahl", "A", "金星 = ein unterer Ringer schlägt einen Yokozuna",
     "『金星』は、だれが横綱に勝つことですか。 A. 前頭の力士　B. 大関　C. 横綱", instr="Auswahl", size=20.5, gap=10)
c.ex("B2", "Ausfüllen", "11", "Fujiryōgas kinboshi: 11. Turnier seit dem Debüt",
     "藤凌駕の金星は、初土俵から ___ 場所目でした。（4面）", instr="Ausfüllen", size=20.5, gap=10)
c.ex("B2", "Ausfüllen", "7", "7.-schnellster kinboshi seit der Sechs-Turniere-Ära",
     "金星の速さは、年6場所になってから ___ 番目です。（4面）", instr="Ausfüllen", size=20.5, gap=10)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「昨日、友達と熊手を買います」", "→ 『昨日』があるので過去形：『熊手を買いました』。", "Mit 「昨日」 steht das Verb in der Vergangenheit."),
    ("「私の趣味は紅葉を見るです」", "→ 『こと』が必要です：『紅葉を見ることです』。", "Zum Substantivieren eines Verbs 「こと」 anhängen."),
    ("「浅草に熊手を買います」", "→ 買う場所は『で』：『浅草で熊手を買います』。", "Für den Ort des Kaufens steht 「で」."),
    ("「嵐山へ紅葉を見に行くです」", "→ 『行く』で終わります：『嵐山へ紅葉を見に行きます』。", "Das Verb in der ます-Form beenden."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "まちがい診療所　Fehlerklinik", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "『福をかき込む』 — 福（幸せ）＋かき込む（手前に集めること）。熊手で福を集める、という意味です。"
wcn = "Zerlegung: Glück mit einem kumade hereinharken."
wh = 89 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
# W47 gatefix (boxtitle): frame title + DE gloss overflowed the box by
# 36.5px on one line; split JP title (23) / gloss (19) onto two lines.
p.text(bx + 22, yy3 + 26, "今週のフレーム", 23, "sans", True, OLIVE)
p.text(bx + 22, yy3 + 53, "Satzmuster der Woche", 19, "sans", True, OLIVE)
yy3 += 79
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「こんにちは。私は中学生です。私の11月の1週間は、にぎやかな1週間です。19日には、浅草の酉の市へ行って、熊手を見ます。22日には、テレビで相撲の千秋楽を見ます。」— 読者の手紙の例"
ld_de = "Beispiel der Redaktion — kein echter Brief. Bis zum Redaktionsschluss kamen keine echten Briefe und keine besten Aufsätze an; beides erscheint in VOL.5. Schickt uns euren Brief auf Japanisch!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_de, "sans", False, 20, CW - 44)) * 29 + 26 + 16
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "読者の手紙　Leserecke", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, ld_de, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- tori image (spans cols 0-2, in the slack below the language columns) ----
image(p, "tori.jpg", MX, 1180, COLX[2] + CW - MX, 220)
caption(p, MX, 1400, COLX[2] + CW - MX,
        "花園神社の酉の市の熊手の店。2025年11月24日の写真です。今年の二の酉は19日（木）です。",
        "Foto: Mozzucu — CC0 (Wikimedia Commons)")

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 30)  # W47 gatefix: reclaim 14px so the two-line frame title (+27) keeps the teaser clear of the footer
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "今週のフレーズ　Sätze der Woche (wörtlich aus dieser Ausgabe)", 27, "sans", True, OLIVE)
quotes = [
    ("「19日（木よう日）は、酉の市・二の酉です。」", "Donnerstag, 19. November: Ni-no-tori bei Tori-no-ichi.", "S. 1"),
    ("「同じ19日（木よう日）は、ボジョレー・ヌーヴォーの解禁日です。」", "Derselbe Donnerstag, 19. November, ist auch der Tag der Beaujolais-Freigabe.", "S. 1"),
    ("「熊手は、商売繁盛の縁起物です。」", "Ein kumade ist ein Glücksbringer für florierende Geschäfte.", "S. 2"),
    ("「ボジョレー・ヌーヴォーは、フランスのボジョレー地方の新酒です。」", "Beaujolais Nouveau ist der neue Wein aus Frankreichs Beaujolais-Region.", "S. 3"),
    ("「3日目まで、大の里も豊昇龍も2勝1敗です。」", "Nach drei Tagen stehen Ōnosato und Hōshōryū beide 2–1.", "S. 4"),
    ("「『りくりゅう』は、フィギュアスケートのペアです。」", "rikuryuu ist ein Eiskunstlauf-Paar.", "S. 7"),
    ("「紅葉の見頃は、京都へ移っています。」", "Die beste Herbstlaubzeit zieht gerade nach Kyoto.", "S. 1"),
    ("「酉の市は、11月の酉の日に開くお祭りです。」", "Tori-no-ichi ist ein Fest an den Hahntagen im November.", "S. 2"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 132
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 132 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "来週　Nächste Ausgabe (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "相撲の千秋楽の結果をお知らせします。流行語のトップテンは、12月1日（火）に発表されます。紅葉の見頃は、東京と大阪へ移ります。読者の手紙と第8版の作文の優秀作も載せます。お楽しみに！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-kotoba.svg")
print("P7 saved, exercises so far:", len(REG))
