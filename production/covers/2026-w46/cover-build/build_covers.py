#!/usr/bin/env python3
"""Build W46 website cover blocks by cloning the matching W45 cover per
reader language and surgically replacing: header dates, each article's
headline (target language, from the W46 print covers) and teaser (reader
language, from teasers.json), plus the feature image/figcaption/alt.
CSS, structure, plates, slots and data-story-langs are carried over byte-identical.
"""
import base64
import html as htmllib
import json
import re
import sys

REPO = "/home/hatch/workspace/weekly-git"
BUILD = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/cover-build"
READERS = ["de", "fr", "es", "en", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]

HEADER_REPL = {
    "de": [("Woche vom 2. bis 8. November 2026", "Woche vom 9. bis 15. November 2026"),
           ("Montag, 2. November 2026", "Montag, 9. November 2026")],
    "fr": [("Semaine du 2 au 8 novembre 2026", "Semaine du 9 au 15 novembre 2026")],
    "es": [("Semana del 2 al 8 de noviembre de 2026", "Semana del 9 al 15 de noviembre de 2026")],
    "en": [("Week of November 2–8, 2026", "Week of November 9–15, 2026"),
           ("Monday, November 2, 2026", "Monday, November 9, 2026")],
    "it": [("Settimana dal 2 all'8 novembre 2026", "Settimana dal 9 al 15 novembre 2026")],
    "pt": [("2–8 de novembro de 2026", "9–15 de novembro de 2026")],
    "nl": [("Week van 2–8 november 2026", "Week van 9–15 november 2026")],
    "ru": [("Неделя со 2 по 8 ноября 2026 года", "Неделя со 9 по 15 ноября 2026 года")],
    "ja": [("2026年11月2日〜8日", "2026年11月9日〜15日"),
           ("2026年11月2日（月）", "2026年11月9日（月）")],
    "ko": [("2026년 11월 2일–8일 주간", "2026년 11월 9일–15일 주간"),
           ("2026년 11월 2일 월요일", "2026년 11월 9일 월요일")],
    "zh-cn": [("2026年11月2日—8日", "2026年11月9日—15日"),
              ("2026年11月2日，星期一", "2026年11月9日，星期一")],
    "zh-tw": [("2026年11月2日–8日這一週", "2026年11月9日–15日這一週"),
              ("2026年11月2日–8日", "2026年11月9日–15日"),
              ("2026年11月2日，星期一", "2026年11月9日，星期一")],
}

FIGCAP = {
    "en": "Two minutes of silence at eleven on 11 November.",
    "de": "Zwei Minuten Stille um elf Uhr am 11. November.",
    "fr": "Deux minutes de silence à onze heures, le 11 novembre.",
    "es": "Dos minutos de silencio a las once del 11 de noviembre.",
    "it": "Due minuti di silenzio alle undici dell'11 novembre.",
    "pt": "Dois minutos de silêncio às onze horas do dia 11 de novembro.",
    "nl": "Twee minuten stilte om elf uur op 11 november.",
    "ru": "Две минуты молчания в одиннадцать часов 11 ноября.",
    "ja": "11月11日11時の2分間の黙祷。",
    "ko": "11월 11일 11시의 2분간 묵념.",
    "zh-cn": "11月11日上午11点的两分钟默哀。",
    "zh-tw": "11月11日上午11點的兩分鐘默哀。",
}

ALT = {
    "en": "A field of red poppies in soft November morning light, three people standing quietly in the distance",
    "de": "Ein Feld mit rotem Mohn im weichen Novembermorgenlicht, drei Menschen stehen still in der Ferne",
    "fr": "Un champ de coquelicots rouges dans la douce lumière d'un matin de novembre, trois personnes debout, immobiles, au loin",
    "es": "Un campo de amapolas rojas bajo la suave luz de una mañana de noviembre, tres personas de pie y en silencio a lo lejos",
    "it": "Un campo di papaveri rossi nella tenue luce di un mattino di novembre, tre persone in piedi e silenziose in lontananza",
    "pt": "Um campo de papoulas vermelhas sob a luz suave de uma manhã de novembro, três pessoas de pé e em silêncio ao longe",
    "nl": "Een veld met rode klaprozen in het zachte licht van een novemberochtend, drie mensen die stil in de verte staan",
    "ru": "Поле красных маков в мягком свете ноябрьского утра, трое людей стоят молча вдали",
    "ja": "11月の朝の柔らかな光の中の赤いポピーの畑、遠くに静かに立つ3人の人々",
    "ko": "11월 아침의 부드러운 빛 속 붉은 양귀비 들판, 멀리 조용히 서 있는 세 사람",
    "zh-cn": "11月清晨柔和光线下的红色罂粟花田，远处静静站着三个人",
    "zh-tw": "11月清晨柔和光線下的紅色罌粟花田，遠處靜靜站著三個人",
}


def esc(t):
    return htmllib.escape(t, quote=False)


def parse_headlines(path):
    txt = open(path, encoding="utf-8").read()
    fm = txt.split("---", 2)[1]
    out = {}
    for m in re.finditer(r'- lang: (\S+)\n\s+headline: "(.*)"', fm):
        out[m.group(1)] = m.group(2)
    return out


def main():
    # headlines: verify identical across all 12 print covers
    base = None
    for r in READERS:
        hl = parse_headlines(f"{REPO}/covers/2026-w46/2026-w46-cover-{r}/2026-w46-cover-{r}.md")
        assert len(hl) == 12, (r, len(hl))
        if base is None:
            base = hl
        else:
            assert hl == base, f"headline mismatch in {r}"
    headlines = base
    print("headlines verified identical across 12 print covers")

    teasers = json.load(open(f"{BUILD}/teasers.json", encoding="utf-8"))["teasers"]
    for r in READERS:
        assert sorted(teasers[r]) == sorted(READERS), r

    en_hq = base64.b64encode(open(f"{BUILD}/en_hq.webp", "rb").read()).decode()
    data_uri = "data:image/webp;base64," + en_hq

    for r in READERS:
        src = open(f"{REPO}/covers/2026-w45/2026-w45-cover-{r}/2026-w45-cover-{r}.html",
                   encoding="utf-8").read()
        m = re.search(r'data-story-langs="([^"]*)"', src)
        order = m.group(1).split()
        assert sorted(order) == sorted(READERS), (r, order)
        parts = re.split(r'(?=<article)', src)
        assert len(parts) == 13, (r, len(parts))
        head, parts = parts[0], parts[1:]
        # header date replacements (header region only)
        for old, new in HEADER_REPL[r]:
            assert old in head, (r, old)
            head = head.replace(old, new)
        # split articles back out
        assert len(parts) == 12, (r, len(parts))
        out_arts = []
        for i, chunk in enumerate(parts):
            tgt = order[i]
            m = re.search(r'(<article[^>]*>)(.*?)(</article>)', chunk, flags=re.S)
            assert m, (r, tgt)
            opentag, inner, closetag, tail = m.group(1), m.group(2), m.group(3), chunk[m.end():]
            hs = re.findall(r'<h[23][^>]*>.*?</h[23]>', inner, flags=re.S)
            ps = re.findall(r'<p[^>]*>.*?</p>', inner, flags=re.S)
            assert len(hs) == 1 and len(ps) == 1, (r, tgt, len(hs), len(ps))
            inner = re.sub(r'(<h[23][^>]*>).*?(</h[23]>)',
                           lambda m: m.group(1) + esc(headlines[tgt]) + m.group(2),
                           inner, count=1, flags=re.S)
            inner = re.sub(r'(<p[^>]*>).*?(</p>)',
                           lambda m: m.group(1) + esc(teasers[r][tgt]) + m.group(2),
                           inner, count=1, flags=re.S)
            if "<img" in inner:
                assert tgt == "en", (r, tgt)
                inner = re.sub(r'src="[^"]*"', f'src="{data_uri}"', inner, count=1)
                inner = re.sub(r'alt="[^"]*"', f'alt="{esc(ALT[r])}"', inner, count=1)
                inner = re.sub(r'(<figcaption[^>]*>).*?(</figcaption>)',
                               lambda m: m.group(1) + esc(FIGCAP[r]) + m.group(2),
                               inner, count=1, flags=re.S)
            out_arts.append(opentag + inner + closetag + tail)
        out = head + "".join(out_arts)
        # assertions on output
        # assertions on output (strip base64 blobs: random substrings like
        # "W45" inside image data are not week references)
        check = re.sub(r'data:[^"]*', 'data:', out)
        assert "w45" not in check and "W45" not in check and "2026-w45" not in check, r
        for old, _ in HEADER_REPL[r]:
            assert old not in out, (r, old)
        assert out.count("<article") == 12, r
        for bad in ("<script", "<a ", "<a>", "<button", "<form", "<nav", "<footer",
                    "onclick", "javascript:"):
            assert bad not in out.lower(), (r, bad)
        assert 'data-story-langs="' + " ".join(order) + '"' in out, r
        dst = (f"{REPO}/covers/2026-w46/2026-w46-cover-{r}/"
               f"2026-w46-cover-{r}.html")
        with open(dst, "w", encoding="utf-8") as f:
            f.write(out)
        print(f"{r}: {len(out)} bytes, order={' '.join(order)}")
    print("OK")


if __name__ == "__main__":
    sys.exit(main())
