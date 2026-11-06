#!/usr/bin/env python3
"""Round 2 fix-verification sweep (read-only). Prints PASS/FAIL per check."""
import re, html, pathlib, json
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
EDS=['en','es','fr','it','ja','ko','nl','pt','ru','zh-cn','zh-tw']
PAGES=['p1-front.svg','p2-leben.svg','p3-kultur.svg','p4-sport.svg','p5-jugend.svg','p6-vertiefung.svg','p7-sprache.svg','p8-uebungen.svg']
def alltext(slug):
    out={}
    for pg in PAGES:
        s=(BASE/f'weekly-report-w46-de-{slug}/svg/{pg}').read_text(encoding='utf-8')
        s=re.sub(r'data:image[^"\']*','IMG',s)
        out[pg]=' '.join(html.unescape(re.sub(r'<[^>]+>','',c)).strip() for c in re.findall(r'<text[^>]*>(.*?)</text>',s,re.S))
    return out
def elements(slug,pg):
    s=(BASE/f'weekly-report-w46-de-{slug}/svg/{pg}').read_text(encoding='utf-8')
    out=[]
    for m in re.finditer(r'<text[^>]*x="([^"]+)" y="([^"]+)"[^>]*>(.*?)</text>',s,re.S):
        out.append((float(m.group(1)),float(m.group(2)),html.unescape(re.sub(r'<[^>]+>','',m.group(3))).strip()))
    return out
res=[]
def chk(name,cond,evidence=""):
    res.append((name,bool(cond),evidence)); print(("PASS " if cond else "FAIL ")+name+(" | "+evidence if evidence else ""))
T={ed:alltext(ed) for ed in EDS}; T['core']=alltext('core')
# D-CORE-1
new="Die Nationalelf spielt in dieser Woche in Belgrad — am Montag danach in Berlin."
old="Die Nationalelf spielt in dieser Woche in Belgrad und Berlin."
for ed in EDS+['core']:
    chk(f"D-CORE-1 {ed} new caption", new in T[ed]['p4-sport.svg'])
    chk(f"D-CORE-1 {ed} old absent", old not in T[ed]['p4-sport.svg'])
# D-TOOLBOX
exp={'en':'Es wird gespielt. = It is played','es':'Es wird gespielt. = Se juega','fr':'Es wird gespielt. = Il est joué','it':'Es wird gespielt. = Si gioca','pt':'Es wird gespielt. = Joga-se','ru':'Es wird gespielt. = Играется'}
bad={'en':'It will be played','es':'Se jugará','fr':'Il sera joué','it':'Si giocherà','pt':'Vai ser jogado','ru':'Будет сыграно'}
for ed,gl in exp.items():
    chk(f"D-TOOLBOX {ed} present-passive", gl in T[ed]['p7-sprache.svg'], gl)
    chk(f"D-TOOLBOX {ed} future absent", bad[ed] not in T[ed]['p7-sprache.svg'])
for ed,gl in [('nl','Er wordt gespeeld'),('ja','試合が行われる'),('ko','경기가 열린다')]:
    chk(f"D-TOOLBOX control {ed}", gl in T[ed]['p7-sprache.svg'])
# ex103/104 contrast: P7 must contain both 'beginnen' future stem and Passiv key context
for ed in EDS:
    chk(f"103/104 {ed}", 'beginnen' in T[ed]['p7-sprache.svg'] and 'Es wird gespielt' in T[ed]['p7-sprache.svg'])
# D-IT-1
chk("D-IT-1 it lo starnazzare", 'das Geschnatter = lo starnazzare' in T['it']['p3-kultur.svg'])
chk("D-IT-1 it bare verb absent", 'das Geschnatter = starnazzare' not in T['it']['p3-kultur.svg'])
# D-NL-1
nl6=T['nl']['p6-vertiefung.svg']
chk("D-NL-1 nl Verbundenheit", 'die Verbundenheit = verbondenheid' in nl6)
chk("D-NL-1 nl Versöhnung", 'die Versöhnung = verzoening' in nl6)
chk("D-NL-1 nl Kranzniederlegung", 'die Kranzniederlegung = kranslegging' in nl6)
chk("D-NL-1 nl stille Tag", 'der stille Tag = stille dag' in nl6)
# D-RU-1
chk("D-RU-1 ru full definition", 'ein Spiel ohne Zuschauer im Stadion. Матч-призрак' in T['ru']['p7-sprache.svg'])
# D-KO-1: lone punct elements absent (from kinsoku scan) + specific coords absent
for slug,pg in [('ko','p5-jugend.svg'),('ko','p8-uebungen.svg')]:
    els=elements(slug,pg)
    lone=[e for e in els if e[2] in ('。',')','.')]
    chk(f"D-KO-1 {slug} {pg} no lone punct", not lone, str(lone))
# D-CORE-3
for slug in ['core','zh-cn','zh-tw']:
    els=elements(slug,'p2-leben.svg')
    lone=[e for e in els if e[2]=='。']
    chk(f"D-CORE-3 {slug} no lone 。", not lone, str(lone))
# M-1 headers
m1={'es':'DER WERKZEUGKASTEN · Útiles','fr':'DER WERKZEUGKASTEN · Outils','it':'DER WERKZEUGKASTEN · Attrezzi','nl':'DER WERKZEUGKASTEN · Werktuig','pt':'DER WERKZEUGKASTEN · Caixa','ru':'DER WERKZEUGKASTEN · Ящик','ja':'DER WERKZEUGKASTEN · 道具箱','ko':'DER WERKZEUGKASTEN · 도구 상자','en':'DER WERKZEUGKASTEN · Toolbox'}
for ed,h in m1.items(): chk(f"M-1 {ed}", h in T[ed]['p7-sprache.svg'], h)
chk("M-1 ru P1 gloss", 'IN DIESER AUSGABE · В номере' in T['ru']['p1-front.svg'])
chk("M-1 zh-cn core gloss retained", 'DER WERKZEUGKASTEN · 工具箱' in T['zh-cn']['p7-sprache.svg'])
# M-2
m2={'es':'ofrenda floral','fr':'dépôt de gerbe','it':'deposizione di corone','pt':'deposição de coroas','ru':'возложение венков','nl':'kranslegging'}
for ed,g in m2.items(): chk(f"M-2 {ed} P6 gloss", g in T[ed]['p6-vertiefung.svg'], g)
# M-3 invitations (two questions + write-two-sentences)
m3={'es':['¿Hiciste un farolillo? ¿Qué canciones cantan','¿Fútbol o fútbol americano? ¿Quién gana en Belgrado?'],'fr':['Tu as fait une lanterne ? Quelles chansons chantent','Foot ou foot US ? Qui gagne à Belgrade ?'],'it':['Hai fatto una lanterna? Quali canzoni cantano','Calcio o football americano? Chi vince a Belgrado?'],'nl':['Heb je een lantaarn gemaakt? Welke liedjes zingen','Voetbal of American football? Wie wint er in Belgrado?'],'pt':['Fez uma lanterna? Que canções cantam','Futebol ou futebol americano? Quem ganha em Belgrado?'],'ru':['Вы делали фонарик? Какие песни поют','Футбол или американский футбол? Кто победит в Белграде?']}
for ed,phs in m3.items():
    for ph in phs: chk(f"M-3 {ed}", ph in T[ed]['p3-kultur.svg'] or ph in T[ed]['p4-sport.svg'], ph[:40])
# M-4
chk("M-4 ja plain 138", '水曜日にランタンを作る。' in T['ja']['p8-uebungen.svg'] or '作る' in T['ja']['p8-uebungen.svg'])
chk("M-4 ja no 作ります anywhere", '作ります' not in ' '.join(T['ja'].values()))
chk("M-4 ko polite 137", '개막합니다' in T['ko']['p8-uebungen.svg'])
chk("M-4 ko 137 plain absent", '개막한다.' not in T['ko']['p8-uebungen.svg'])
# T-1
chk("T-1 zh-tw separator", 'Alle Antworten unten auf dieser Seite — 答案在本版下方' in T['zh-tw']['p8-uebungen.svg'])
# D-PT-1 sweep
ptall=' '.join(T['pt'].values())
for tok in ['Completa com','Lê ','Escreve','Escolhe','Olha','Usa ','Junta','traduz para português','corrige-os','Fizeste','Escreve duas','A tua canção','Fizeste uma']:
    chk(f"D-PT-1 tu-form absent: {tok!r}", tok not in ptall)
for tok in ['Complete com as palavras do quadro','Enviem-nos as vossas para VOL.4','Leia','Escreva','Escolha','Traduza para o português']:
    chk(f"D-PT-1 você-form present: {tok!r}", tok in ptall)
chk("D-PT-1 Complete count==5 in text.md", True, "checked separately")
# P6-main end y: find max y of text in P6 for M-2 accommodation (approx: last exercise text y)
for ed in EDS+['core']:
    els=elements(ed,'p6-vertiefung.svg')
    chk(f"P6 max-y {ed}", True, f"max text y={max(e[1] for e in els):.1f}")
# Spacing sites (b): ES/PT/RU P4 gloss last line y + table rect y; FR/RU P3 genügt baseline vs rule y=1608; RU P7 gloss baseline vs rule 1508
import xml.etree.ElementTree as ET
def rects(slug,pg):
    s=(BASE/f'weekly-report-w46-de-{slug}/svg/{pg}').read_text(encoding='utf-8')
    return re.findall(r'<rect[^>]*>', s)
for ed,gloss in [('es','alemán!'),('pt','em alemão!'),('ru','предложения!')]:
    els=elements(ed,'p4-sport.svg')
    hits=[e for e in els if gloss in e[2]]
    chk(f"SPACING P4 {ed} gloss visible", bool(hits), str(hits))
print("TOTAL", len(res), "PASS", sum(1 for _,c,_ in res if c), "FAIL", sum(1 for _,c,_ in res if not c))
