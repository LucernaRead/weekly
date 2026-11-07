# -*- coding: utf-8 -*-
"""Write ABSTRACT.txt (one line, no ASCII double quotes) for all 12 W46 DE editions."""
import os

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ABSTRACTS = {
"core": "Die Lucerna 德语周报 VOL.3：国家队欧国联关键一周（客场对阵塞尔维亚空场比赛、主场迎战荷兰）、NFL 慕尼黑赛（雄狮对阵爱国者）、圣马丁节与科隆狂欢季开幕、追思纪念日与电费税辩论；正文德语、讲解简体中文，A2–B2 分级，150 道练习，适合学德语的读者通过德国新闻学德语。",
"zh-cn": "Die Lucerna 德语周报 VOL.3：国家队欧国联关键一周（客场对阵塞尔维亚空场比赛、主场迎战荷兰）、NFL 慕尼黑赛（雄狮对阵爱国者）、圣马丁节与科隆狂欢季开幕、追思纪念日与电费税辩论；正文德语、讲解简体中文，A2–B2 分级，150 道练习，适合学德语的读者通过德国新闻学德语。",
"en": "Die Lucerna German Weekly VOL.3: Germany's Nations League decider week (a ghost game away in Serbia, the Netherlands at home), the NFL in Munich (Lions vs Patriots), St Martin's Day and the Cologne carnival opening, Remembrance Sunday and the electricity-tax debate; German text with explanations in English, A2 to B2, 150 exercises, for learners who want to learn German by reading real German news.",
"fr": "Die Lucerna hebdomadaire allemand VOL.3 : la semaine décisive de la Ligue des nations (un match fantôme en Serbie, les Pays-Bas à domicile), la NFL à Munich (Lions contre Patriots), la Saint-Martin et l'ouverture du carnaval de Cologne, le jour du Souvenir et le débat sur la taxe sur l'électricité ; textes en allemand avec explications en français, niveaux A2 à B2, 150 exercices, pour apprendre l'allemand en lisant les vraies nouvelles allemandes.",
"es": "Die Lucerna semanario alemán VOL.3: la semana decisiva de la Liga de Naciones (partido fantasma en Serbia, Países Bajos en casa), la NFL en Múnich (Lions contra Patriots), San Martín y la apertura del carnaval de Colonia, el día de Recuerdo y el debate sobre el impuesto de la electricidad; textos en alemán con explicaciones en español, niveles A2 a B2, 150 ejercicios, para aprender alemán leyendo noticias alemanas reales.",
"it": "Die Lucerna settimanale tedesco VOL.3: la settimana decisiva di Nations League (partita fantasma in Serbia, Olanda in casa), la NFL a Monaco (Lions contro Patriots), San Martino e l'apertura del carnevale di Colonia, il giorno del Ricordo e il dibattito sulla tassa sull'elettricità; testi in tedesco con spiegazioni in italiano, livelli A2–B2, 150 esercizi, per imparare il tedesco leggendo vere notizie tedesche.",
"pt": "Die Lucerna semanário alemão VOL.3: a semana decisiva da Liga das Nações (jogo fantasma na Sérvia, Países Baixos em casa), a NFL em Munique (Lions contra Patriots), São Martinho e a abertura do carnaval de Colónia, o dia de Recordação e o debate sobre o imposto da eletricidade; textos em alemão com explicações em português, níveis A2 a B2, 150 exercícios, para aprender alemão a ler notícias alemãs reais.",
"nl": "Die Lucerna Duits weekblad VOL.3: de beslissende Nations League-week (spookwedstrijd in Servië, Nederland thuis), de NFL in München (Lions tegen Patriots), Sint Maarten en de opening van het carnaval in Keulen, de herdenkingsdag en het debat over de stroomtaks; teksten in het Duits met uitleg in het Nederlands, niveaus A2 tot B2, 150 oefeningen, om Duits te leren door echt Duits nieuws te lezen.",
"ru": "Die Lucerna немецкий еженедельник VOL.3: решающая неделя Лиги наций (матч-призрак в Сербии, Нидерланды дома), NFL в Мюнхене (Лайонс против Пэтриотс), День святого Мартина и открытие карнавала в Кёльне, день памяти и дебаты о налоге на электричество; тексты на немецком с объяснениями на русском, уровни A2–B2, 150 упражнений, для тех, кто учит немецкий по настоящим немецким новостям.",
"ja": "Die Lucerna ドイツ語週刊 VOL.3：ネーションズリーグの決戦週間（セルビアでの無観客試合、ホームでオランダ戦）、ミュンヘンのNFL（ライオンズ対ペイトリオッツ）、聖マルティンの日とケルンのカーニバル開幕、追悼の日と電気税論争。ドイツ語の本文に日本語の解説、A2からB2まで、150問の練習問題。本物のドイツのニュースでドイツ語を学ぶ読者のために。",
"ko": "Die Lucerna 독일어 주간지 VOL.3: 네이션스리그 결전 주간(세르비아 원정 무관중 경기, 홈에서 네덜란드전), 뮌헨 NFL(라이온스 대 패트리어츠), 성 마르틴의 날과 쾰른 카니발 개막, 추모의 날과 전기세 논쟁. 독일어 본문에 한국어 해설, A2부터 B2까지, 연습문제 150개. 진짜 독일 뉴스로 독일어를 배우는 독자를 위해.",
"zh-tw": "Die Lucerna 德語週報 VOL.3：國家隊歐國聯關鍵一週（客場對陣塞爾維亞閉門比賽、主場迎戰荷蘭）、NFL 慕尼黑賽（雄獅對陣愛國者）、聖馬丁節與科隆狂歡季開幕、追思紀念日與電費稅辯論；正文德語、講解繁體中文，A2–B2 分級，150 道練習，適合學德語的讀者通過德國新聞學德語。",
}
for ed, text in ABSTRACTS.items():
    assert '"' not in text, ed
    assert "\n" not in text, ed
    p = os.path.join(GOAL, "files", f"weekly-report-w46-de-{ed}", "ABSTRACT.txt")
    open(p, "w", encoding="utf-8").write(text + "\n")
    print(ed, len(text))
