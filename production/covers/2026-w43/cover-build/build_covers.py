#!/usr/bin/env python3
"""Build 12 W43 website cover blocks from the W45 templates.

Method (proven by the W46 build): clone the matching W45 cover template per
reader language; surgical replacement only — header dates, each article's
headline (target language, from W43 print covers' frontmatter, verified
identical across all 12) and teaser (reader language, from teasers.json);
CSS/structure/plates/data-image-slot carried byte-identical; zero
interaction asserted. Feature slot in all 12 covers embeds the en story
image (en_hq.webp, base64) with per-reader figcaption + alt.
"""
import base64
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/home/hatch/workspace/weekly-git"
READERS = ["de", "fr", "es", "en", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]

teasers = json.load(open(os.path.join(HERE, "teasers.json"), encoding="utf-8"))["teasers"]
HEADLINES = {
    "de": "Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien",
    "fr": "Présidentielle 2027 : les Français regardent déjà les sondages",
    "es": "Este domingo: dormimos una hora más… ¡y se juega el Clásico!",
    "en": "First Votes, First Games : America's Biggest Week of the Autumn",
    "it": "Un'ora in più di sonno: domenica torna l'ora solare",
    "pt": "Domingo é dia de decisão: o Brasil volta às urnas",
    "nl": "Een volle week: vakantie, design, dance — en een uur extra slaap",
    "ru": "Первый снег — уже на этой неделе!",
    "ja": "土よう日、日本シリーズが始まる！",
    "ko": "태풍 참피가 오고 있어요",
    "zh-cn": "双11到了「付尾款」的这一周",
    "zh-tw": "強颱薔琵壓境！週五、週六風雨最大",
}
# W45 template header strings -> W43 strings (per reader language).
HEADER_REPL = {
    "de": [("Woche vom 2. bis 8. November 2026", "Woche vom 19. bis 25. Oktober 2026"),
           ("Montag, 2. November 2026", "Montag, 19. Oktober 2026")],
    "fr": [("Semaine du 2 au 8 novembre 2026", "Semaine du 19 au 25 octobre 2026")],
    "es": [("Semana del 2 al 8 de noviembre de 2026", "Semana del 19 al 25 de octubre de 2026")],
    "en": [("Week of November 2–8, 2026", "Week of October 19–25, 2026"),
           ("Monday, November 2, 2026", "Monday, October 19, 2026")],
    "it": [("Settimana dal 2 all'8 novembre 2026", "Settimana dal 19 al 25 ottobre 2026")],
    "pt": [("2–8 de novembro de 2026", "19–25 de outubro de 2026")],
    "nl": [("Week van 2–8 november 2026", "Week van 19–25 oktober 2026")],
    "ru": [("Неделя со 2 по 8 ноября 2026 года", "Неделя с 19 по 25 октября 2026 года")],
    "ja": [("2026年11月2日〜8日", "2026年10月19日〜25日"),
           ("2026年11月2日（月）", "2026年10月19日（月）")],
    "ko": [("2026년 11월 2일–8일 주간", "2026년 10월 19일–25일 주간"),
           ("2026년 11월 2일 월요일", "2026년 10월 19일 월요일")],
    "zh-cn": [("2026年11月2日—8日", "2026年10月19日—25日"),
              ("2026年11月2日，星期一", "2026年10月19日，星期一")],
    "zh-tw": [("2026年11月2日–8日這一週", "2026年10月19日–25日這一週"),
              ("2026年11月2日–8日", "2026年10月19日–25日"),
              ("2026年11月2日，星期一", "2026年10月19日，星期一")],
}
FIGCAP = {
    "en": "Early voting opens in the autumn's biggest week.",
    "de": "Die vorgezogene Stimmabgabe beginnt in der größten Woche des Herbstes.",
    "fr": "Le vote anticipé s'ouvre dans la plus grande semaine de l'automne.",
    "es": "La votación anticipada se abre en la mayor semana del otoño.",
    "it": "Il voto anticipato si apre nella settimana più importante dell'autunno.",
    "pt": "A votação antecipada começa na maior semana do outono.",
    "nl": "De vervroegde stemming begint in de grootste week van de herfst.",
    "ru": "Досрочное голосование открывается в самую насыщенную неделю осени.",
    "ja": "秋最大の週に期日前投票が始まる。",
    "ko": "가을 최대의 주간에 사전 투표가 시작된다.",
    "zh-cn": "秋天最重要的一周，提前投票开始了。",
    "zh-tw": "秋天最重要的一週，提前投票開始了。",
}
ALT = {
    "en": "People in autumn coats queueing outside a small polling place to vote early, an American flag above the door, leaves falling",
    "de": "Menschen in Herbstmänteln stehen vor einem kleinen Wahllokal Schlange, um vorzeitig zu wählen, eine amerikanische Flagge über der Tür, fallende Blätter",
    "fr": "Des gens en manteaux d'automne font la queue devant un petit bureau de vote pour voter par anticipation, un drapeau américain au-dessus de la porte, des feuilles qui tombent",
    "es": "Personas con abrigos de otoño hacen cola fuera de un pequeño colegio electoral para votar anticipadamente, una bandera estadounidense sobre la puerta, hojas cayendo",
    "it": "Persone in cappotti autunnali in fila fuori da un piccolo seggio elettorale per votare in anticipo, una bandiera americana sopra la porta, foglie che cadono",
    "pt": "Pessoas com casacos de outono em fila do lado de fora de um pequeno local de votação para votar antecipadamente, uma bandeira americana acima da porta, folhas caindo",
    "nl": "Mensen in herfstjassen staan in de rij buiten een klein stembureau om vervroegd te stemmen, een Amerikaanse vlag boven de deur, vallende bladeren",
    "ru": "Люди в осенних пальто стоят в очереди у небольшого избирательного участка, чтобы проголосовать досрочно, американский флаг над дверью, падающие листья",
    "ja": "秋のコートを着た人々が期日前投票のため小さな投票所の外に並び、ドアの上にアメリカ国旗、舞い落ちる葉",
    "ko": "가을 코트를 입은 사람들이 사전 투표를 위해 작은 투표소 밖에 줄을 서고, 문 위에 미국 국기, 떨어지는 낙엽",
    "zh-cn": "穿着秋装的人们排队在一间小型投票站外提前投票，门上挂着美国国旗，落叶飘飞",
    "zh-tw": "穿著秋裝的人們排隊在一間小型投票站外提前投票，門上掛著美國國旗，落葉飄飛",
}

en_b64 = base64.b64encode(open(os.path.join(HERE, "en_hq.webp"), "rb").read()).decode()
en_uri = "data:image/webp;base64," + en_b64

fails = []
for r in READERS:
    tpl_path = os.path.join(REPO, "covers/2026-w45",
                            f"2026-w45-cover-{r}", f"2026-w45-cover-{r}.html")
    src = open(tpl_path, encoding="utf-8").read()
    parts = re.split(r"(?=<article)", src)
    head, articles = parts[0], parts[1:]
    if len(articles) != 12:
        fails.append(f"{r}: template has {len(articles)} articles, expected 12")
        continue
    # Header: dates + week slug.
    for old, new in HEADER_REPL[r]:
        if old not in head:
            fails.append(f"{r}: header string not found in template head: {old!r}")
        head = head.replace(old, new)
    head = head.replace("2026-w45", "2026-w43")
    # Body: data-story-langs order is the template's own order — carry it.
    m = re.search(r'data-story-langs="([^"]+)"', head)
    if not m:
        fails.append(f"{r}: no data-story-langs in head")
        continue
    order = m.group(1).split()
    if sorted(order) != sorted(READERS):
        fails.append(f"{r}: order {order} is not the 12 reader codes")
        continue
    out_articles = []
    for idx, chunk in enumerate(articles):
        # Articles follow <body data-story-langs> document order: article i
        # is the story for order[i]. (Verified on the W45 en template: the
        # feature article with <img> sits at order index 3 = en, and every
        # article's topic matches its order language.)
        tgt = order[idx]
        h = re.search(r"<h[123][^>]*>(.*?)</h[123]>", chunk, flags=re.S)
        p = re.search(r"<p[^>]*>(.*?)</p>", chunk, flags=re.S)
        if not h or not p:
            fails.append(f"{r}/{tgt}: article lacks h or p tag")
            break
        chunk = chunk[:h.start(1)] + HEADLINES[tgt] + chunk[h.end(1):]
        # Re-find p after headline replacement (offsets shifted).
        p = re.search(r"<p[^>]*>(.*?)</p>", chunk, flags=re.S)
        chunk = chunk[:p.start(1)] + teasers[r][tgt] + chunk[p.end(1):]
        if tgt == "en":
            if "<img" not in chunk:
                fails.append(f"{r}: en article has no <img>")
                break
            chunk2, n = re.subn(r'src="data:image[^"]*"', f'src="{en_uri}"', chunk, count=1)
            if n != 1:
                fails.append(f"{r}: en img src replacement failed")
                break
            chunk2, n = re.subn(r'alt="[^"]*"', f'alt="{ALT[r]}"', chunk2, count=1)
            if n != 1:
                fails.append(f"{r}: en img alt replacement failed")
                break
            fc = re.search(r"<figcaption[^>]*>(.*?)</figcaption>", chunk2, flags=re.S)
            if not fc:
                fails.append(f"{r}: en article has no figcaption")
                break
            chunk2 = chunk2[:fc.start(1)] + FIGCAP[r] + chunk2[fc.end(1):]
            chunk = chunk2
        else:
            if "<img" in chunk:
                fails.append(f"{r}/{tgt}: non-en article carries an <img>")
                break
        out_articles.append(chunk)
    else:
        out = head + "".join(out_articles)
        # Assertions on the finished block.
        text = re.sub(r"data:image/[^\"']*", "DATAURI", out)
        # Zero interaction: no links-as-anchors, scripts, buttons, forms,
        # or handlers. (The W45 template head legitimately carries <link>
        # font references — byte-identical in landed W45 blocks and in the
        # W46 build — so bare href= is NOT flagged; only <a href is.)
        for bad in ("w45", "W45", "2026-w45", "<script", "<a ", "<a>", "<a href",
                    "<button", "<form", "onclick", "onload", "onerror",
                    "November 2", "11月2日", "11월 2일", "2. November"):
            if bad in text:
                fails.append(f"{r}: forbidden leftover {bad!r} in output")
        for old, _new in HEADER_REPL[r]:
            if old in text:
                fails.append(f"{r}: old header string remains: {old!r}")
        for _old, new in HEADER_REPL[r]:
            if new not in text:
                fails.append(f"{r}: new header string missing: {new!r}")
        if out.count("<article") != 12:
            fails.append(f"{r}: {out.count('<article')} articles in output")
        if out.count("<img") != 1:
            fails.append(f"{r}: {out.count('<img')} <img> in output (expected 1)")
        if FIGCAP[r] not in out or ALT[r] not in out:
            fails.append(f"{r}: figcaption/alt missing in output")
        dst_dir = os.path.join(REPO, "covers/2026-w43", f"2026-w43-cover-{r}")
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, f"2026-w43-cover-{r}.html")
        open(dst, "w", encoding="utf-8").write(out)
        print(f"{r}: OK order={' '.join(order)} slots={out.count('data-image-slot')} bytes={len(out.encode())}")

if fails:
    print("FAILURES:")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("ALL 12 BUILT")
