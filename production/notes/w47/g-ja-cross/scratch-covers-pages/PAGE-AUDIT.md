# W47 封面页号核实（PAGE-AUDIT）

核实员：封面页号核实（subagent）。日期：2026-11-13。依据：SOP 附则五 §6a——版号以 PDF 为准，翻到文章看页脚「第 N 版」。

## 方法

- 核心 PDF：`production/2026-w47/core-<target>/` 下非 web 版（8 页）。先逐页抽页脚 `第N版／共8版`：12 份核心 PDF 的 PDF 页序与页脚版号全部一致（1–8），故页脚版号 = PDF 页码。
- 每项 `more[n].headline`：去空白+大小写折叠后在 8 页全文中做全文匹配；cover.json 标题为删词缩短版时，改做词序子序列匹配（全部词按序出现），并对多页匹配项逐页看上下文，区分正文标题与 P1 目录提及 / P8 练习·答案提及。
- 每项 `word.term`：先定位 P1「Word of the Week」框（12 份核心 P1 均有该框），核对框内词与 cover.term 是否一致、框在第几版；de 例外见注。
- 头条（第 1 版）与导读（第 i 行 = 第 i+2 版）按 §6a 不用写，不在 84 项内。

## 结果总览

- 84 项（12 目标语 × 6 条 more + 1 个 word）逐项核对完毕。
- **不符：0 项。**`more[n].page` 72 项全部与文章实际所在版一致；`word.page` 12 项全部与该词的词语讲解所在版一致。
- **cover.json 页号改动：0 处。**封面块无需重生成（仍按任务第 3/4 步在 scratch 复核 + 原目录跑 `cover.mjs` 确认 0 problems，见 COVER-REPORT 底稿）。
- ⚠️ 内容问题 1 项（不属页号，不管辖、只上报）：de 的 `word.term` 为 Totensonntag，但 de 核心 P1「DAS WORT DER WOCHE」框内词是 der Adventskalender。页号 6 本身与 P6 词语讲解文相符，故不改页号；term 是否应改为 der Adventskalender（页随之改 1）由父协调员定。

## en（核心 PDF：`core-en/The-Lucerna-VOL4-en-zh-cn.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | The Week After the Vote: What Happens Now? | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | Friday at the Movies: Haymitch Goes Back to the Arena | 3 | 3 | 一致 | 匹配页 [3]；全文词序匹配仅第 3 版 |
| more[2] | Perth, One Year On: How Australia Kept the Ashes | 4 | 4 | 一致 | 匹配页 [4]；全文词序匹配仅第 4 版 |
| more[3] | Break the Silence: Odd Socks and Loud Voices | 5 | 5 | 一致 | 匹配页 [5]；全文词序匹配仅第 5 版 |
| more[4] | The Map After November 3: Reading the Results | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | Phrases of the week | 7 | 7 | 一致 | 匹配页 [1, 7]；P1 仅目录提及（p.7 Phrases of the week），正文在 P7 |
| word | midterm | 1 | 1 | 一致 | 词出现页 [1, 6, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## de（核心 PDF：`core-de/Die-Lucerna-VOL4-de.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | Ein Mittwoch, der fast frei ist: Der Buß- und Bettag | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | Weihnachtsmärkte öffnen — aber am Sonntag bleiben sie zu | 3 | 3 | 一致 | 匹配页 [3]；全文词序匹配仅第 3 版 |
| more[2] | Die Woche der Ergebnisse — und die Rückkehr der Liga | 4 | 4 | 一致 | 匹配页 [4]；全文词序匹配仅第 4 版 |
| more[3] | Adventskalender basteln: 24 Türchen bis Weihnachten | 5 | 5 | 一致 | 匹配页 [5]；全文词序匹配仅第 5 版 |
| more[4] | Eine stille Woche: Was bedeuten Buß- und Bettag und Totensonntag? | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | Sätze der Woche & Fehlerklinik | 7 | 7 | 一致 | 匹配页 [7]；全文词序匹配仅第 7 版 |
| word | Totensonntag | 6 | 6 | 一致 | 词出现页 [1, 2, 3, 6, 8]；P6 深读文〈Eine stille Woche: Was bedeuten Buß- und Bettag und Totensonntag?〉即该词的词语讲解；⚠️ 但 P1「DAS WORT DER WOCHE」框内词为 der Adventskalender，与 cover.term 不符——属内容问题（见文末），页号本身与词语讲解页相符，不改 |

## fr（核心 PDF：`core-fr/La-Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | Lundi 16 novembre : une semaine en trois temps | 2 | 2 | 一致 | 匹配页 [2, 8]；P8 仅练习提及，正文在 P2 |
| more[1] | Le beaujolais nouveau a 75 ans | 3 | 3 | 一致 | 匹配页 [1, 2, 3, 8]；P1/P2/P8 仅练习·答案提及，正文在 P3（CULTURE 版头） |
| more[2] | Alcaraz gagne Paris, Turin commence | 4 | 4 | 一致 | 匹配页 [1, 4]；P1 仅练习提及，正文在 P4（SPORT 版头） |
| more[3] | Mercredi 18 novembre : le cinéma, et la seconde main | 5 | 5 | 一致 | 匹配页 [5]；全文词序匹配仅第 5 版 |
| more[4] | Au Sénat, mercredi 18 : le vote du budget de la Sécu | 6 | 6 | 一致 | 匹配页 [1, 6]；P1 仅练习提及，正文在 P6（POLITIQUE & CHIFFRES 版头） |
| more[5] | Les phrases de la semaine | 7 | 7 | 一致 | 匹配页 [1, 2, 6, 7, 8]；P1 仅目录提及（p.7），正文在 P7 |
| word | trancher | 1 | 1 | 一致 | 词出现页 [1]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## es（核心 PDF：`core-es/La-Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | La semana, día a día: del lunes 16 al domingo 22 | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | El flamenco cumple: del 16 de noviembre a Santa Cecilia | 3 | 3 | 一致 | 匹配页 [3]；全文词序匹配仅第 3 版 |
| more[2] | Vuelve la Liga: la jornada 13, del viernes al lunes | 4 | 4 | 一致 | 匹配页 [1, 2, 4]；P1/P2 仅目录·练习提及，正文在 P4（DEPORTE 版头） |
| more[3] | Votar por primera vez: el jueves 19 se cierra el plazo | 5 | 5 | 一致 | 匹配页 [5, 8]；P8 仅练习提及，正文在 P5（JUVENTUD 版头） |
| more[4] | Leer la campaña: debates, programas y encuestas | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | Frases de la semana | 7 | 7 | 一致 | 匹配页 [2, 4, 7]；全文精确匹配仅第 7 版 |
| word | el debate | 1 | 1 | 一致 | 词出现页 [1, 2, 6, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## it（核心 PDF：`core-it/La-Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | Venezia prega, l'Italia pianta alberi: il 21 novembre | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | Due feste dolci chiudono in bellezza: torrone e cioccolato | 3 | 3 | 一致 | 匹配页 [3]；全文词序匹配仅第 3 版 |
| more[2] | Lazio prima, Inter e Roma inseguono: i conti dell'11ª giornata | 4 | 4 | 一致 | 匹配页 [4]；全文词序匹配仅第 4 版 |
| more[3] | I giovani leggono: BookCity arriva, il cinema torna a Torino | 5 | 5 | 一致 | 匹配页 [5]；全文词序匹配仅第 5 版 |
| more[4] | La manovra va in Parlamento: audizioni, emendamenti, voto | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | Frasi della settimana | 7 | 7 | 一致 | 匹配页 [1, 7]；P1 仅目录提及（Pag. 7），正文在 P7 |
| word | la vetta | 1 | 1 | 一致 | 词出现页 [1, 4, 7]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## pt（核心 PDF：`core-pt/A-Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | Sexta, 20 de novembro: o feriado e o feriadão | 2 | 2 | 一致 | 匹配页 [1, 2, 7, 8]；P1 仅头条导读提及，正文在 P2（VIDA 版头） |
| more[1] | Zumbi e Palmares: a história do 20 de novembro | 3 | 3 | 一致 | 匹配页 [1, 3, 8]；P1/P8 仅练习提及，正文在 P3（CULTURA 版头） |
| more[2] | Grêmio e Palmeiras decidem a Copa do Brasil | 4 | 4 | 一致 | 匹配页 [4]；全文词序匹配仅第 4 版 |
| more[3] | Depois do Enem: a espera começa | 5 | 5 | 一致 | 匹配页 [1, 5, 6]；P1/P6 仅练习提及，正文在 P5（JOVENS 版头） |
| more[4] | O gabarito explicado: como funciona a espera | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | Frases da semana | 7 | 7 | 一致 | 匹配页 [1, 2, 3, 4, 7, 8]；P1 仅目录提及（Pág. 7），正文在 P7 |
| word | consciência | 1 | 1 | 一致 | 词出现页 [1, 2, 3, 5, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## nl（核心 PDF：`core-nl/De-Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | De schoen staat klaar: aftellen naar pakjesavond | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | Sinterklaas is er: Grave, Amsterdam en het journaal | 3 | 3 | 一致 | 匹配页 [3, 8]；P8 仅练习提及，正文在 P3（CULTUUR 版头） |
| more[2] | Oranje: de beslissing in Berlijn | 4 | 4 | 一致 | 匹配页 [1, 4]；P1 仅目录提及，正文在 P4（SPORT 版头） |
| more[3] | Robinson op zondag — en de surprises | 5 | 5 | 一致 | 匹配页 [1, 5]；P1 仅目录提及，正文在 P5（青年版头） |
| more[4] | Sinterklaas: oud feest, nieuwe wensen | 6 | 6 | 一致 | 匹配页 [1, 6]；P1 仅目录提及，正文在 P6（VERDIEPING 版头） |
| more[5] | Zinnen van de week | 7 | 7 | 一致 | 匹配页 [7]；全文词序匹配仅第 7 版 |
| word | de groepswinst | 1 | 1 | 一致 | 词出现页 [1, 4, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## ru（核心 PDF：`core-ru/Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | День студента, день рождения Деда Мороза | 2 | 2 | 一致 | 匹配页 [1, 2, 3, 4, 5, 6, 7, 8]；全文精确匹配仅第 2 版 |
| more[1] | Кино 19 ноября: пять премьер | 3 | 3 | 一致 | 匹配页 [1, 2, 3, 4, 6, 7, 8]；P1 仅目录提及，正文在 P3（КУЛЬТУРА 版头） |
| more[2] | 14-й тур: все восемь результатов | 4 | 4 | 一致 | 匹配页 [1, 2, 4, 5, 7, 8]；P1/P8 仅练习·答案提及，正文在 P4（СПОРТ 版头） |
| more[3] | «Чёрная пятница»: скидки с 16 ноября | 5 | 5 | 一致 | 匹配页 [1, 2, 3, 4, 5, 6, 8]；P1 仅目录提及，正文在 P5（МОЛОДЁЖЬ 版头） |
| more[4] | Неделя 16–22 ноября: как её прожить | 6 | 6 | 一致 | 匹配页 [1, 2, 4, 5, 6, 8]；P1/P8 仅练习·答案提及，正文在 P6（БОЛЬШОЙ РАЗБОР 版头） |
| more[5] | Фразы недели | 7 | 7 | 一致 | 匹配页 [1, 2, 3, 4, 5, 6, 7, 8]；P1 仅目录提及（Стр. 7），正文在 P7 |
| word | оттепель | 1 | 1 | 一致 | 词出现页 [1, 2, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## ja（核心 PDF：`core-ja/Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | 19日 — 夜通しの酉の市 | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | 新酒の夜 — 19日の0時 | 3 | 3 | 一致 | 匹配页 [1, 3]；P1 仅导读提及，正文在 P3（文化版头） |
| more[2] | 波乱の3日間 — 九州場所 | 4 | 4 | 一致 | 匹配页 [4]；全文词序匹配仅第 4 版 |
| more[3] | 今年のことば、30語 | 5 | 5 | 一致 | 匹配页 [5]；全文词序匹配仅第 5 版 |
| more[4] | 見頃を追いかけて京都へ | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | 今週のフレーズ | 7 | 7 | 一致 | 匹配页 [1, 7]；P1 仅导读提及，正文在 P7（今週のフレーズ） |
| word | 熊手 | 1 | 1 | 一致 | 词出现页 [1, 2, 3, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## ko（核心 PDF：`core-ko/Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | 김장비용이 내렸어요 — 김치의 날에는 김치를 나눠요 | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | 김치의 날이 와요 — 늦가을 단풍은 마무리에요 | 3 | 3 | 一致 | 匹配页 [3]；全文词序匹配仅第 3 版 |
| more[2] | 삼성이 12년 만에 우승했어요 — kt wiz를 4승 1패로 이겼어요 | 4 | 4 | 一致 | 匹配页 [1, 4]；P1 仅导读提及，正文在 P4 |
| more[3] | 수능 주간 — 예비소집부터 시험 날까지 | 5 | 5 | 一致 | 匹配页 [1, 5]；P1 仅导读提及，正文在 P5（青年版头） |
| more[4] | 예보에서 결과로 — 뉴스를 다시 읽는 법 | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | 실수 병원 | 7 | 7 | 一致 | 匹配页 [7]；全文词序匹配仅第 7 版 |
| word | 예비소집 | 1 | 1 | 一致 | 词出现页 [1, 5, 6, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## zh-cn（核心 PDF：`core-zh-cn/Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | 包裹到了吗？收、退、查 | 2 | 2 | 一致 | 匹配页 [1, 2]；P1 仅导读提及，正文在 P2（生活版头） |
| more[1] | 小雪到了，冬天真的来了 | 3 | 3 | 一致 | 匹配页 [1, 3]；P1 仅目录提及（3版），正文在 P3（文化版头） |
| more[2] | S16：四强打完，决赛见 | 4 | 4 | 一致 | 匹配页 [1, 4]；P1 仅目录提及（4版），正文在 P4（体育版头） |
| more[3] | 新电影《试探》，你去看吗？ | 5 | 5 | 一致 | 匹配页 [5]；全文词序匹配仅第 5 版 |
| more[4] | 今年的包裹，为什么没有爆掉？ | 6 | 6 | 一致 | 匹配页 [6]；全文词序匹配仅第 6 版 |
| more[5] | 易错诊所 | 7 | 7 | 一致 | 匹配页 [7]；全文词序匹配仅第 7 版 |
| word | 决赛 | 1 | 1 | 一致 | 词出现页 [1, 2, 4, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## zh-tw（核心 PDF：`core-zh-tw/Lucerna-VOL4.pdf`；页脚 1–8 与 PDF 页序一致）

| 项目 | 标题 / 词 | cover.json | 实测 | 结论 | 证据 |
|---|---|---|---|---|---|
| more[0] | 小雪快到了，保暖先做好 | 2 | 2 | 一致 | 匹配页 [2]；全文词序匹配仅第 2 版 |
| more[1] | 金馬獎本週日頒獎，誰會得獎？ | 3 | 3 | 一致 | 匹配页 [3]；全文词序匹配仅第 3 版 |
| more[2] | 本週日，封王遊行天母出發！ | 4 | 4 | 一致 | 匹配页 [1, 4, 7, 8]；P1/P7/P8 仅练习·答案提及，正文在 P4（體育版头） |
| more[3] | 香港迪士尼聖誕，11月17日開始 | 5 | 5 | 一致 | 匹配页 [5, 7, 8]；P7/P8 仅练习·答案提及，正文在 P5（版头「第5版 迪士尼聖誕」） |
| more[4] | 11月22日，一天四件大事 | 6 | 6 | 一致 | 匹配页 [6, 8]；P8 仅练习提及，正文在 P6（深讀版头） |
| more[5] | 易錯診所 | 7 | 7 | 一致 | 匹配页 [7]；全文词序匹配仅第 7 版 |
| word | 封王 | 1 | 1 | 一致 | 词出现页 [1, 4, 6, 7, 8]；P1「Word of the Week」框内词与 cover.term 一致，框在第 1 版 |

## 附：de word.term 内容不符（上报，不改）

- cover.json `stories.de.word`：term = Totensonntag，page = 6，gloss 各语均为“教会年最后的主日，新教徒缅怀逝者”。
- de 核心 P1「DAS WORT DER WOCHE」框：« der Adventskalender »（Ein Kalender mit 24 Türchen…）。
- de 核心 P6 深读文标题：〈Eine stille Woche: Was bedeuten Buß- und Bettag und Totensonntag?〉，正文解释 Totensonntag 为“der letzte Sonntag des Kirchenjahres”——与 cover gloss 一致。
- 判断：若词保持 Totensonntag，页号 6 正确（词语讲解在 P6）；若词应为 P1 框词 der Adventskalender，则 term 与 page（→1）须一起改。改 term 属内容决定，超出本次只改页号的授权，故只上报、不动手。

共核对 84 项，不符 0 项。