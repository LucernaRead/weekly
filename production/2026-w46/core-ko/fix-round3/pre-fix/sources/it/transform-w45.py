# -*- coding: utf-8 -*-
"""One-off fan-out transform: W45 KO core (Chinese explanations) -> KO x IT.

Single source of truth for this edition's explanation-layer rewrite.
Idempotent: an entry whose OLD string is absent but whose NEW string is
present is skipped (already applied); an entry with neither present FAILS.
Fix rounds APPEND new entries at the end (old = current transformed text,
new = fixed text) and re-run this script, then re-render via run.py.

Rules honoured (tools README):
- #17: replacements are whole lines or exact unique literals, never AST
  byte offsets. No replacement touches Korean target text.
- #18: no repr literals; bare text values only.
- Geometry: KO x IT follows the W43 ko-it precedent (measured from the
  shipped W43 svg): subtitle 372 -> 366, badge INSERTED at y=394, 20pt
  weight-700 BRICK, rules +20 (412/421), dark band +9 (433, lines 487/531).
  Displacement stops at the masthead block (headline block starts y=580).
- This script is NOT imported by run.py/render.py (one-off, scratch only).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.dirname(HERE)
FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "svglib.py"]

# ---- geometry: exact full lines (P1 masthead, W43 ko-it precedent) ----
GEOMETRY = [
    ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
     'p.text(975, 394, "TESTI IN COREANO · SPIEGAZIONI IN ITALIANO — L\'EDIZIONE PER I LETTORI ITALIANI", 20, "sans", True, BRICK, anchor="middle")'),
    ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
     'p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)'),
    ('p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)',
     'p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)'),
    ('p.text(MX + 30, 478, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")',
     'p.text(MX + 30, 487, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")'),
    ('p.text(MX + 30, 522, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")',
     'p.text(MX + 30, 531, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")'),
    ('p.text(RIGHT - 30, 478, "立冬", 24, "sans", True, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 487, "L\'IPDONG", 24, "sans", True, "#b3a06a", anchor="end")'),
    ('p.text(RIGHT - 30, 522, "立冬在 11 月 7 日周六 · 泡菜季开始", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 531, "L\'ipdong è sabato 7 novembre · Inizia la stagione del kimchi", 21, "sans", False, "#b3a06a", anchor="end")'),
]

# ---- ordered literal replacements (longer/substring hosts FIRST) ----
R = []
def add(old, new):
    R.append((old, new))

# OUT repoint (baseline-out -> edition dir) + bslib furniture + method rename
add("hidden_files/weekly-report-w45-ko-it-build/baseline-out",
    "files/weekly-report-w45-ko-it/svg")
add("Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY",
    "Lucerna · SETTIMANALE COREANO VOL.2 · TESTI IN COREANO · SPIEGAZIONI IN ITALIANO")
add('f"제 {n} 면 / 총 {total} 면"', 'f"Pagina {n} di {total}"')
add("译注｜", "Nota — ")
add("def glossline(", "def expl(")
add("glossline(", "expl(")
add("for 重阳", "for the Double Ninth festival")

# P1 furniture + subtitle
add("매주 한국어로 · 每周一期 · 한국 사람이 읽는 한국어를 읽어요",
    "매주 한국어로 · Ogni settimana · 한국 사람이 읽는 한국어를 읽어요")
add("한국어판 · VOL.2 · 입동 · 단풍 · 김장",
    "SETTIMANALE COREANO · VOL.2 · 입동 · 단풍 · 김장")
add("톱 뉴스 · 头条", "톱 뉴스 · In primo piano")
add("숫자로 보는 이번 주 · 数字看本周", "숫자로 보는 이번 주 · In cifre")
add("지금 바로 연습 · 即学即练", "지금 바로 연습 · Pratica subito")
add("이번 호의 내용 · 本期目录", "이번 호의 내용 · Indice")
add("이번 주의 말 · 本周词语", "이번 주의 말 · La parola della settimana")
add("짧은 소식 · 快讯", "짧은 소식 · In breve")
add("퀴즈 · 闪电问答", "퀴즈 · Quiz lampo")
add("读头版，选出正确答案 · 答案见第 8 版",
    "Leggi la prima pagina e scegli la risposta giusta · Risposte a pag. 8")
add("答案见第 8 版 · 题目可跨级混排，按题号找答案",
    "Risposte a pag. 8 · Gli esercizi mescolano i livelli: cerca per numero")
add("연습 · 第 2 版练习", "연습 · Esercizi pag. 2")
add("연습 · 第 3 版练习", "연습 · Esercizi pag. 3")
add("연습 · 第 4 版练习", "연습 · Esercizi pag. 4")
add("연습 · 第 5 版练习", "연습 · Esercizi pag. 5")
add("연습 · 第 6 版练习", "연습 · Esercizi pag. 6")

# P8 E stems FIRST (they contain substrings of later note literals)
add("特别措施只适用于11月19日。→ ___",
    "Le misure speciali si applicano solo il 19 novembre. → ___")
add("我周六去内藏山看红叶。→ ___",
    "Sabato vado a Naejangsan a vedere le foglie d'autunno. → ___")
add("11月7日是立冬。", "Il 7 novembre è l'ipdong.")
add("离高考还剩 12 天。", "Mancano 12 giorni all'esame.")
add("对照第 1 版", "Confronta con pag. 1")
add("对照第 5 版", "Confronta con pag. 5")
add("对照第 6 版", "Confronta con pag. 6")
add("对照第 3 版", "Confronta con pag. 3")
add("(开放题，范文如下)", "(domanda aperta — il modello è qui sotto)")

# Long notes before their short substrings
add("特别措施只适用于11月19日", "Le misure speciali valgono solo il 19 novembre")
add("日期不同因标准不同（3版）", "Le date differiscono per il criterio (pag. 3)")
add("青松现场庆典11月4日起", "La festa di Cheongsong in presenza inizia il 4 novembre")
add("智敏周六去内藏山", "Jimin sabato va a Naejangsan")
add("措施只适用于11月19日", "Le misure valgono solo il 19 novembre")
add("日期不同因标准不同", "Le date differiscono per il criterio")
add("现场庆典11月4日起", "La festa in presenza inizia il 4 novembre")
add("周六去内藏山", "Sabato va a Naejangsan")

# Glosses (feature + P7 expl lines) — item counts preserved, "·" splits kept
add("입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。",
    "입동 = inizio dell'inverno · 절정 = il picco · 김장 = il kimchi invernale · 상륙하다 = toccare terra · 온대저기압 = ciclone extratropicale")
add("절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。",
    "절이다 = salare · 버무리다 = mescolare · 난방 = riscaldamento · 식탁 = tavola")
add("산불 山火 · 벌금 罚款 · 불씨 火星。",
    "산불 = incendio boschivo · 벌금 = multa · 불씨 = scintilla")
add("아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。",
    "아삭하다 = croccante · 김 = vapore · 깊어지다 = diventare profondo")
add("물려주다 传给 · 낡다 旧 · 두렵다 害怕。",
    "물려주다 = passare a qualcuno · 낡다 = vecchio · 두렵다 = avere paura")
add("묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。",
    "묵직하다 = pesante · 앞치마 = grembiule · 목록 = lista")
add("기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。",
    "기관 = ente · 기준 = criterio · 관측 = osservazione · 구간별 = per tratto")
add("현장 现场 · 유명하다 有名 · 맛보다 品尝。",
    "현장 = sul posto · 유명하다 = famoso · 맛보다 = assaggiare")
add("이용하다 利用 · 막히다 堵塞 · 예의 礼仪。",
    "이용하다 = usare · 막히다 = intasarsi · 예의 = buona educazione")
add("겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。",
    "겹쳐 입다 = vestirsi a strati · 미끄러지다 = scivolare · 돌 = pietra")
add("연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。",
    "연승 = vittorie consecutive · 만루홈런 = fuoricampo a basi piene · 미뤄지다 = essere rinviato · 마감하다 = chiudere (il numero)")
add("흔들다 挥动 · 하나가 되다 融为一体。",
    "흔들다 = agitare · 하나가 되다 = diventare una cosa sola")
add("예상 预测。", "예상 = previsione")
add("정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。",
    "정리 = ripasso · 끈끈하다 = appiccicoso · 합격 = superamento (dell'esame)")
add("중점 重点 · 배치하다 部署 · 통제하다 管制。",
    "중점 = prioritario · 배치하다 = disporre · 통제하다 = controllare")
add("챙기다 准备好 · 졸리다 犯困 · 평소 平时。",
    "챙기다 = preparare · 졸리다 = avere sonno · 평소 = di solito")
add("비다 祈愿 · 피하다 避开 · 미끄럽다 滑。",
    "비다 = pregare, augurare · 피하다 = evitare · 미끄럽다 = scivoloso")
add("짙어지다 变浓 · 규모 规模 · 섞다 混淆。",
    "짙어지다 = farsi intenso · 규모 = portata, scala · 섞다 = confondere")
add("겁이 나다 害怕 · 중요하다 重要。",
    "겁이 나다 = avere paura · 중요하다 = importante")
add("예정 预定 · 확정 确定 · 믿다 相信。",
    "예정 = previsto · 확정 = confermato · 믿다 = credere")
add("본격적 正式、全面 · 나다 度过。",
    "본격적 = in pieno, davvero · 나다 = passare (il tempo)")
add("남다 剩下 · 바로 正是、恰恰。",
    "남다 = restare, mancare · 바로 = proprio, esattamente")
add("짐작하다 推测 · 나누다 区分。",
    "짐작하다 = immaginare, intuire · 나누다 = distinguere")

# Box / band / section titles (Chinese half -> Italian; Korean half frozen)
add("한능검 접수 · 韩史考试报名", "한능검 접수 · Iscrizioni all'esame")
add("겨울 준비 목록 · 过冬清单", "겨울 준비 목록 · Lista invernale")
add("단풍 구경 준비물 · 红叶观赏准备", "단풍 구경 준비물 · Cosa portare")
add("이번 주 청년 숫자 · 本周青年数字", "이번 주 청년 숫자 · I numeri")
add("생활 · 生活", "생활 · Vita quotidiana")
add("레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季与过冬准备、韩史考试报名",
    "레벨 A2 · 김장과 겨울 준비, 한능검 · Kimchi, preparativi invernali e esame di storia")
add("문화 · 文化", "문화 · Cultura")
add("레벨 A2→B1 · 단풍 마지막 주말 · 红叶最后一周",
    "레벨 A2→B1 · 단풍 마지막 주말 · L'ultimo weekend delle foglie")
add("한국시리즈까지의 길 · 通往韩国大赛之路",
    "한국시리즈까지의 길 · La strada verso le Korean Series")
add("스포츠 · 体育", "스포츠 · Sport")
add("레벨 B1 · 가을야구 소식 · 秋季棒球消息",
    "레벨 B1 · 가을야구 소식 · Notizie dal baseball d'autunno")
add("청년 · 青年", "청년 · Giovani")
add("레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒计时与万圣节",
    "레벨 B1 · 수능 카운트다운과 할로윈 · Conto alla rovescia e Halloween")
add("깊이 읽기 · 深读", "깊이 읽기 · Lettura approfondita")
add("레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒计时读法",
    "레벨 B2 · 수능 카운트다운을 읽는 법 · Come leggere il conto alla rovescia")
add("이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清",
    "이번 주와 시험 날, 한눈에 보기 · Questa settimana e il giorno dell'esame, in una tabella")
add("말 공부 · 语言", "말 공부 · Lingua")
add("언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三个级别，三个主题",
    "언어 포커스 · 세 가지 레벨, 세 가지 주제 · Tre livelli, tre temi")
add("실수 병원 · 易错诊所", "실수 병원 · La clinica degli errori")
add("이번 주의 틀 · 本周句式", "이번 주의 틀 · La frase tipo")
add("독자의 편지 · 读者园地", "독자의 편지 · Lettere dei lettori")
add("이번 주의 문장 · 本周金句（逐字摘自本期文章）",
    "이번 주의 문장 · Frasi della settimana (testuali, da questo numero)")
add("다음 주 · 下期预告 (VOL.3)", "다음 주 · La prossima settimana (VOL.3)")
add("시험과 답 · 测验与答案", "시험과 답 · Test e risposte")
add("답 · 参考答案 — 按版面分页排列，找到题号即可",
    "답 · Risposte — ordinate per pagina, cerca il numero")
add("每题附一句中文简析 · 带 ✓ 的为范文题",
    "Ogni risposta con una breve nota in italiano · ✓ = esercizio con modello")

# D-day strip + calendar + word of the week
add("날짜 세는 말 · 数日子的说法", "날짜 세는 말 · Come contare i giorni")
add("수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒计时数日子的四个说法",
    "수능까지 남은 날로 날짜를 세는 네 가지 말 · Quattro modi per contare i giorni all'esame")
add("11 月 2 日，还剩 17 天", "2 novembre, mancano 17 giorni")
add("11 月 7 日，还剩 12 天", "7 novembre, mancano 12 giorni")
add("11 月 18 日，就是明天", "18 novembre, è domani")
add("11 月 19 日，就是今天", "19 novembre, è oggi")
add("这五个日期，是本期报纸的骨架。", "Queste cinque date sono l'ossatura di questo numero.")
add("입동 ＝ 立冬、冬季开始的节气。", "입동 = ipdong, l'inizio dell'inverno.")

# "Tocca a te" boxes (each Chinese string occurs twice: eh calc + para)
add("당신은? · 说说你自己", "당신은? · Tocca a te")
add("你呢？为过冬做的第一件事是什么？写两句韩语寄来。",
    "E tu? Qual è la prima cosa che fai per prepararti all'inverno? Scrivi due frasi in coreano e mandale.")
add("你呢？想去看红叶的山是哪座？写两句韩语寄来。",
    "E tu? In quale montagna vorresti vedere le foglie? Scrivi due frasi in coreano e mandale.")
add("你呢？想对考生说的一句加油是什么？写两句韩语寄来。",
    "E tu? Quale parola di incoraggiamento vorresti dire a un candidato? Scrivi due frasi in coreano e mandale.")

# Korean instruction glosslines -> Italian expl lines
add("2면의 글을 읽고 맞는 답을 고르세요.", "Leggi i testi di pag. 2 e scegli la risposta giusta.")
add("3면의 글을 읽고 맞는 답을 고르세요.", "Leggi i testi di pag. 3 e scegli la risposta giusta.")
add("4면의 글을 읽고 맞는 답을 고르세요.", "Leggi i testi di pag. 4 e scegli la risposta giusta.")
add("5면의 글을 읽고 맞는 답을 고르세요.", "Leggi i testi di pag. 5 e scegli la risposta giusta.")
add("6면의 글을 읽고 맞는 답을 고르세요.", "Leggi i testi di pag. 6 e scegli la risposta giusta.")
add("빈칸에 알맞은 말을 넣으세요.", "Inserisci la parola giusta nello spazio.")
add("1면과 2면의 숫자와 날짜로 답하세요.", "Rispondi con i numeri e le date delle pagg. 1 e 2.")
add("3면의 숫자와 날짜로 답하세요.", "Rispondi con i numeri e le date di pag. 3.")
add("5면의 숫자로 답하세요.", "Rispondi con i numeri di pag. 5.")
add("말을 바른 순서로 놓아 문장을 만드세요.", "Metti le parole nell'ordine giusto per formare una frase.")
add("문장을 과거형으로 바꾸세요. (바꾼 문장은 모두 이 신문에 나온 일이에요.)",
    "Metti le frasi al passato. (Sono tutte cose successe in questo numero.)")
add("6면의 표를 보고 맞는 답을 고르세요.", "Guarda la tabella di pag. 6 e scegli la risposta giusta.")
add("문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.",
    "Se la frase è giusta scegli «맞다», se è sbagliata «틀리다».")
add("쓰기 문제예요 (정답은 하나가 아니에요). 아래에 {NCHARS}자의 예가 있어요.",
    "È un esercizio di scrittura (non c'è un'unica risposta giusta). Qui sotto c'è un esempio di {NCHARS} caratteri.")
add("范文见本版 H 区（{NCHARS} 字）",
    "Il modello è nella sezione H di questa pagina ({NCHARS} caratteri)")

# P7 clinic / frame / letters (line counts preserved: clinic 1 line each,
# frame 2 lines, lcn 1 line, lcn2 3 lines — so P7 col3 height is unchanged)
add("去某地用「에」，不用「를」。", "Si va in un luogo con «에», non con «를».")
add("「담그다」的过去式是「담갔어요」。", "Il passato di «담그다» è «담갔어요».")
add("数字与前面要留空格。", "I numeri si scrivono separati.")
add("助词只用一个。", "Una sola particella per volta.")
add("句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」",
    "La struttura: «da ~ a ~». Per chiedere: «〜부터 〜까지예요?»")
add("编辑部示例信，非真实来信。", "Esempio della redazione, non vera.")
add("郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。",
    "Nessuna lettera vera né tema di pag. 8: resta l'esempio, la promessa passa al VOL.3. Mandateci la vostra lettera!")

# P7 phrases (translations only; Korean quotes + page tags frozen)
add("11 月 7 日是立冬。", "Il 7 novembre è l'ipdong.")
add("只能说是接近峰值的周末。", "Si può solo dire che è un weekend vicino al picco.")
add("泡菜季就是腌过冬泡菜。", "La stagione del kimchi è preparare il kimchi per l'inverno.")
add("离高考还剩 17 天，今天是 D-17。", "Mancano 17 giorni all'esame, oggi è D-17.")
add("低处的路红得更晚。", "I sentieri bassi si colorano più tardi.")
add("KIA 虎三连胜战胜 LG 双子。", "I KIA Tigers hanno battuto gli LG Twins con tre vittorie consecutive.")
add("全国都在为考生加油。", "Tutto il paese incoraggia i candidati.")
add("先看日期。", "Guarda prima la data.")

# ---- exercise notes (Chinese -> Italian; shared literals map once) ----
add("立冬在11月7日周六", "L'ipdong è sabato 7 novembre")
add("泡菜季＝腌过冬泡菜", "Kimchi invernale = preparare il kimchi")
add("高考在11月19日周四", "L'esame è giovedì 19 novembre")
add("11月2日是D-17", "Il 2 novembre è D-17")
add("台风没有在韩国本土登陆", "Il tifone non ha toccato terra in Corea")
add("首尔报名窗口11月6日10–12点", "Iscrizioni a Seul il 6 novembre, ore 10–12")
add("立冬＝冬季开始的节气", "Ipdong = inizio dell'inverno")
add("内藏山两个预报：11月4日与11月11日", "Naejangsan: due previsioni, 4 e 11 novembre")
add("10月25日首场比赛因雨推迟", "Gara 1 del 25 ottobre rinviata per pioggia")
add("山火注意期从11月1日开始", "Il periodo di attenzione inizia il 1º novembre")
add("带火进山最高罚30万韩元", "Portare fuoco in montagna: multa fino a 300.000 won")
add("韩史考试在11月28日周六", "L'esame di storia è sabato 28 novembre")
add("首尔报名10点至12点", "Iscrizioni a Seul dalle 10 alle 12")
add("白菜用盐腌", "Il cavolo si sala")
add("加入萝卜和调料拌匀", "Aggiungi ravanello e condimento e mescola")
add("过冬准备＝为冬天做准备", "Preparativi invernali = prepararsi per l'inverno")
add("进山要小心火", "In montagna attenzione al fuoco")
add("11月3日起开始报名", "Le iscrizioni iniziano il 3 novembre")
add("山火注意期到12月15日", "Il periodo di attenzione finisce il 15 dicembre")
add("最高罚款30万韩元", "Multa massima: 300.000 won")
add("深化考试费27,000韩元", "Tassa d'esame (livello avanzato): 27.000 won")
add("11月6日13点起全国报名剩余名额", "Dal 6 novembre ore 13: iscrizioni nazionali per i posti rimasti")
add("内藏山林业厅预报峰值11月4日", "Naejangsan, previsione forestale: picco il 4 novembre")
add("内藏山公园公团预报峰值11月11日", "Naejangsan, previsione dei parchi: picco l'11 novembre")
add("雪岳山实际观测峰值10月16日", "Seoraksan, osservazione reale: picco il 16 ottobre")
add("青松现场庆典11月4日至8日", "Cheongsong in presenza: dal 4 all'8 novembre")
add("没有官方的路段数值", "Nessun valore ufficiale per tratto")
add("红叶最美的时候叫절정", "Il momento più bello delle foglie si chiama 절정")
add("实际观测比预报早", "L'osservazione reale è prima della previsione")
add("青松以苹果闻名", "Cheongsong è famosa per le mele")
add("内藏山林业厅预报4日", "Naejangsan, previsione forestale: il 4")
add("内藏山公团预报11日", "Naejangsan, previsione dei parchi: l'11")
add("月出山林业厅预报9日", "Wolcchulsan, previsione forestale: il 9")
add("雪岳山实际观测16日", "Seoraksan, osservazione reale: il 16")
add("半决赛胜队是KIA", "La vincente della semifinale è la KIA")
add("第3场比分13比1", "Gara 3: 13 a 1")
add("第3场在蚕室举行", "Gara 3 a Jamsil")
add("季后赛首场因雨推迟", "Gara 1 dei playoff rinviata per pioggia")
add("公布的韩国大赛开始日11月2日", "Korean Series annunciate dal 2 novembre")
add("KIA三连胜晋级", "KIA, tre vittorie consecutive")
add("三连胜晋级", "Tre vittorie consecutive per avanzare")
add("首场比赛因雨推迟", "La prima gara rinviata per pioggia")
add("10月26日变为温带气旋", "Il 26 ottobre diventa ciclone extratropicale")
add("kt在韩国大赛等候", "kt aspetta nelle Korean Series")
add("汉拿山三角峰降雨415.5毫米", "Pioggia sul Samgakbong di Hallasan: 415,5 mm")
add("首尔万圣节安全人员3,271人", "Seul, personale di sicurezza per Halloween: 3.271")
add("11月7日是D-12", "Il 7 novembre è D-12")
add("听力时段飞机不起降", "Durante l'ascolto gli aerei non volano")
add("梨泰院路10月31日管制", "Itaewon-ro chiusa il 31 ottobre")
add("全国为考生加油", "Tutto il paese incoraggia i candidati")
add("倒计时仍在继续", "Il conto alla rovescia continua")
add("怀着祈愿合格的心意赠送糯米糕、饴糖", "Con l'augurio di superare l'esame si regalano tteok e yeot")
add("首尔安全人员3,271人", "Personale di sicurezza di Seul: 3.271")
add("今年考生551,864人", "Candidati quest'anno: 551.864")
add("考场全国1,312处", "Sedi d'esame in tutto il paese: 1.312")
add("考试日机关10点上班", "Il giorno dell'esame gli uffici iniziano alle 10")
add("梨泰院部署1,620人", "Personale disposto a Itaewon: 1.620")
add("首尔管理14个地点", "Seul gestisce 14 luoghi")
add("本周倒计时D-17至D-12", "Questa settimana: conto alla rovescia D-17–D-12")
add("考试日有特别措施", "Il giorno dell'esame ci sono misure speciali")
add("本周没有特别措施", "Questa settimana non ci sono misure speciali")
add("考试日就是D-day", "Il giorno dell'esame è il D-day")
add("本周氛围是倒计时", "L'atmosfera di questa settimana è il conto alla rovescia")
add("氛围在现在、本周", "L'atmosfera è adesso, questa settimana")
add("听力时段13:10～13:35", "Ascolto: dalle 13:10 alle 13:35")
add("倒计时氛围在本周", "Il conto alla rovescia è l'atmosfera di questa settimana")
add("从D-17到D-12的一周", "La settimana da D-17 a D-12")
add("大数字显示全国规模", "I grandi numeri mostrano la scala nazionale")
add("听力时段飞机受管制", "Il giorno dell'esame gli aerei non volano come al solito")
add("本周是倒计时氛围", "Questa settimana l'atmosfera è il conto alla rovescia")
add("节气＝一年24个时节", "절기 = i 24 periodi dell'anno")
add("D-1＝明天", "D-1 = domani")
add("D-day就是当天", "Il D-day è il giorno stesso")
add("林业厅标准是叶子50%", "Il criterio forestale: il 50% delle foglie")
add("설악산=实际观测10月16日 c", "설악산=osservazione reale del 16 ottobre c")
add("实际观测10月16日", "Osservazione reale: il 16 ottobre")
add("预报要标准日期一起看", "Leggi le previsioni insieme a criterio e data")
add("周日帮忙腌泡菜", "Domenica aiuta a preparare il kimchi")
add("下周准备韩史考试", "La prossima settimana prepara l'esame di storia")
add("智敏喜欢韩国史", "A Jimin piace la storia coreana")
add("语序：主语+时间+场所+动词", "Ordine: soggetto + tempo + luogo + verbo")
add("语序：主语+副词+动词", "Ordine: soggetto + avverbio + verbo")
add("主语+宾语+动词的语序", "Ordine: soggetto + oggetto + verbo")
add("보러 가요 = 去看", "보러 가요 = andare a vedere")
add("动作场所用「에서」", "Il luogo dell'azione vuole «에서»")
add("首尔报名10点开始", "Le iscrizioni a Seul iniziano alle 10")
add("이기다的过去式이겼어요", "Il passato di 이기다 è 이겼어요")
add("열리다的过去式열렸어요", "Il passato di 열리다 è 열렸어요")
add("미뤄지다的过去式미뤄졌어요", "Il passato di 미뤄지다 è 미뤄졌어요")
add("바뀌다的过去式바뀌었어요", "Il passato di 바뀌다 è 바뀌었어요")

# Match-set notes (core compact format kept: word=Italian letter)
add("김장=腌过冬泡菜 a", "김장=kimchi invernale a")
add("월동 준비=准备过冬 c", "월동 준비=prepararsi per l'inverno c")
add("산불조심=进山小心火 d", "산불조심=attenzione al fuoco in montagna d")
add("한능검=韩国史考试简称 b", "한능검=esame di storia coreana b")
add("내장산=两个预报之间 b", "내장산=tra le due previsioni b")
add("월출산=11月9日前夕 a", "월출산=alla vigilia del 9 novembre a")
add("북한산=11月4日之后、低路更晚 d", "북한산=dopo il 4 novembre, i sentieri bassi più tardi d")
add("준플레이오프=KIA三连胜 b", "준플레이오프=KIA, tre vittorie b")
add("플레이오프=KIA对三星 d", "플레이오프=KIA contro Samsung d")
add("한국시리즈=kt在等候 a", "한국시리즈=kt aspetta a")
add("온대저기압=台风10月26日变化 c", "온대저기압=il tifone cambia il 26 ottobre c")
add("입동=冬季开始的节气 a", "입동=inizio dell'inverno a")
add("절정=最佳时期 b", "절정=il momento migliore b")
add("김장=腌过冬泡菜 c", "김장=kimchi invernale c")
add("온대저기압=台风10月26日变化 d", "온대저기압=il tifone cambia il 26 ottobre d")

# Match-set instr + type labels + instr labels (instr FIRST, then types:
# "造句"/"翻译"/"写作" occur as both type and instr with different targets)
add("把词和说明配对", "Abbina")
add("把山和说明配对", "Abbina")
add("把词和释义配对", "Abbina")
add('instr="填空"', 'instr="Completa"')
add('instr="改写"', 'instr="Riscrivi"')
add('instr="造句"', 'instr="Costruisci"')
add('instr="翻译"', 'instr="Traduci"')
add('instr="写作"', 'instr="Scrivi"')
add("完形单选", "Cloze")
add("完成句子", "Completa la frase")
add("词汇配对", "Abbinamento")
add("句型转换", "Trasforma la frase")
add("造句", "Costruisci la frase")
add("判断", "Vero o falso")
add("翻译", "Traduzione")
add("写作", "Scrittura")
add("单选", "Scelta multipla")

# ---- fix round 1 (2026-10-27): literals missed in round 0 ----
# (A feared P7 "（3版）" corruption was checked and disproven: the long
# entry had applied first, so P7 already reads "(pag. 3)"; no entry needed.)
add("日期不同因为标准不同", "Le date differiscono per il criterio")
add("特别措施只适用于考试日", "Le misure speciali valgono solo il giorno dell'esame")
add("内藏山公团预报峰值11月11日", "Naejangsan, previsione dei parchi: picco l'11 novembre")
add("月出山林业厅预报峰值11月9日", "Wolcchulsan, previsione forestale: picco il 9 novembre")
add("首尔报名窗口10点至12点", "Iscrizioni a Seul dalle 10 alle 12")
add("全部", "Tutti")

# ---- fix round 2 (2026-10-27): gloss line counts WITH the "Nota — " prefix ----
# Round 1 overflowed P1-headline and P5-feature by one gloss line each
# (prefix-aware counts: core P1 gloss = 3 lines, round-1 Italian = 4;
# core P5 g1 = 2 lines, round-1 Italian = 3; the extra line pushed a later
# box across a column break). Both fixes restore the core line count.
# P1: "ipdong" transliteration follows the ko-en precedent; the P1
# word-of-the-week gloss explains ipdong in full. "ciclone extratropicale"
# is kept in full.
add("입동 = inizio dell'inverno · 절정 = il picco · 김장 = il kimchi invernale · 상륙하다 = toccare terra · 온대저기압 = ciclone extratropicale",
    "입동 = ipdong · 절정 = picco · 김장 = kimchi invernale · 상륙하다 = toccare terra · 온대저기압 = ciclone extratropicale")
add("정리 = ripasso · 끈끈하다 = appiccicoso · 합격 = superamento (dell'esame)",
    "정리 = ripasso · 끈끈하다 = appiccicoso · 합격 = superamento")

# ---- fix round 3 (2026-10-27): P1 TEXTX + P7 BOXTITLE (both NEW vs core) ----
# P1: the 2-line Italian calendar note's line 2 ("numero.", baseline
# 1215.08) sat on the fixed source line (baseline 1216.00) — a real
# same-baseline ink collision. One-line version sits at 1190.10, as the
# core's one-line Chinese note does.
add("Queste cinque date sono l'ossatura di questo numero.",
    "Cinque date: l'ossatura di questo numero.")
# P7: the inherited letter-box height formula undercounts the true
# content extent by ~26px (proven: the CORE's own last line sits 26px
# below its box; the core escapes the audit only because Chinese has no
# descenders, while the Italian line 2's descenders cross the border by
# 1.9px). Two-part fix, both in the edition's content7.py only:
# (1) disclosure shortened 3 lines -> 2 lines (79 chars, verified wrap;
# keeps no-real-letters, no-pag.-8-themes, VOL.3 deferral "la promessa
# passa al VOL.3", and the imperative solicitation "Scriveteci!" — the
# example-stands element stays covered by the "Esempio della redazione"
# label line and the frozen Korean disclosure);
# (2) letter-box trailing pad +26 -> +60 (+34px): with the 2-line
# disclosure the last line's measured ink bottom is 1740.83 (audit's own
# PIL metrics: baseline 1736.33 + 4.50 descent) and the new border is
# 1743.94 (margin 3.11px); teaser ends 2517.94 (< 2540).
add("Nessuna lettera vera né tema di pag. 8: resta l'esempio, la promessa passa al VOL.3. Mandateci la vostra lettera!",
    "Nessuna lettera vera né tema di pag. 8: la promessa passa al VOL.3. Scriveteci!")
add('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 12 + len(wrap(lko, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 26',
    'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 12 + len(wrap(lko, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 60')

# ---- render.py (NOT in FILES: different path/name targets) ----
RENDER = [
    ("files/weekly-report-w45-ko-core", "files/weekly-report-w45-ko-it"),
    ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-IT.pdf"'),
    ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-IT-web.pdf"'),
]

HAN = re.compile(r"[\u4e00-\u9fff]")

def apply_collective(file_list, pairs, label):
    """Apply each pair across the whole file set: an entry must occur in
    at least one file (or its NEW form must already be present); otherwise
    FAIL. This is what makes a missed literal loud instead of silent."""
    texts = {}
    for f in file_list:
        p = os.path.join(BUILD, f)
        with open(p, encoding="utf-8") as fh:
            texts[f] = fh.read()
    for idx, (old, new) in enumerate(pairs):
        total_old = sum(t.count(old) for t in texts.values())
        total_new = sum(t.count(new) for t in texts.values())
        if total_old == 0:
            if total_new > 0:
                print(f"  skip (applied): {label} :: {old[:50]!r}")
                continue
            # Superseded: a later fix entry consumes this entry's output
            # (its OLD == this entry's NEW), so the current text is already
            # past this entry — skip, the later entry will apply-or-skip.
            if any(pairs[j][0] == new for j in range(idx + 1, len(pairs))):
                print(f"  skip (superseded): {label} :: {old[:50]!r}")
                continue
            print(f"  FAIL: not found in any {label} file: {old[:80]!r}")
            sys.exit(1)
        for f in file_list:
            if old in texts[f]:
                texts[f] = texts[f].replace(old, new)
        print(f"  ok x{total_old}: {label} :: {old[:50]!r} -> {new[:50]!r}")
    for f in file_list:
        p = os.path.join(BUILD, f)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(texts[f])

def main():
    print("== geometry (content12 only) ==")
    apply_collective(["content12.py"], GEOMETRY, "geometry")
    print("== literals (operative files) ==")
    apply_collective(FILES, R, "literals")
    print("== render.py ==")
    apply_collective(["render.py"], RENDER, "render")
    print("== post-checks ==")
    bad = []
    for f in FILES + ["render.py", "run.py"]:
        p = os.path.join(BUILD, f)
        t = open(p, encoding="utf-8").read()
        hans = HAN.findall(t)
        if hans:
            bad.append((f, len(hans), "".join(sorted(set(hans)))[:40]))
        if "ko-core" in t:
            bad.append((f, "still references ko-core", ""))
        if "桥接" in t or "bridge" in t.lower():
            bad.append((f, "banned intermediary term", ""))
        # Full-width parens are banned in content/bslib/render (Chinese-note
        # residue) but LEGITIMATE in svglib.py's kinsoku NO_END set — excluded.
        if f != "svglib.py" and ("（" in t or "）" in t):
            bad.append((f, "full-width paren remnant (Chinese note residue)", ""))
    if bad:
        print("POST-CHECK FAILURES:", bad)
        sys.exit(1)
    print("post-checks OK: 0 Han ideographs, 0 ko-core refs, 0 banned terms in operative code")
    print("TRANSFORM DONE")

if __name__ == "__main__":
    main()
