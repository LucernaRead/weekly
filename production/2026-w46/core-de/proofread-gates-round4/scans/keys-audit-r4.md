# Keys audit log — Round 4 (P8 scope, de-zh-cn)

Method: every extracted key (p8.py extract, joined parse, 150/150) checked against the
issue's own prompt text on P1–P8 (shipped SVGs, read in full) — matching-block
option-by-option, cloze/fill keys vs German grammar and article facts, arithmetic recomputed.
p8.py compare is supplement only. Cross-checks: zh-cn vs EN fan-out (146/150 identical) and
zh-cn vs de-core duplicate (149/150 identical).

## Cross-edition diffs (measured, not claimed)
- zh-cn vs EN: differ ONLY 137, 138, 139 (Chinese translations of the same German/Chinese prompts — legitimate native-translation labels) and 150 (open-task label: zh '开放题' vs EN 'Open task'). Key 140 IDENTICAL to EN.
- zh-cn vs core duplicate: differ ONLY 140 — zh 'Am Sonntag schaue ich das NFL-Spiel.' vs core 'Am Sonntag schaue ich da sNFL-Spiel.' (the D-R2-1 rendering defect in the duplicate).

## All 150 keys (extracted) with prompt source
1. Länderspielpause
2. Belgrad
3. Karnevals
4. München
5. fünf
6. Volkstrauertag
7. B
8. C
9. A
10. A
11. 11.11
12. 10.30
13. 15.30
14. 11. November
15. Mittwoch
16. Der Karneval hat in Köln begonnen.
17. Die Kinder haben Martinslieder gesungen.
18. Wir haben eine Laterne gebastelt.
19. Martin hat seinen Mantel geteilt.
20. Viele Familien haben Martinsgans gegessen.
21. B
22. B
23. A
24. B
25. c
26. a
27. b
28. d
29. Richtig
30. Falsch
31. Richtig
32. Falsch
33. Richtig
34. Mantel
35. Laterne
36. Gans
37. Kostüm
38. Martinsfeuer
39. B
40. B
41. A
42. A
43. Martin teilte seinen Mantel mit einem Bettler.
44. Die Kinder basteln bunte Laternen aus Papier.
45. Am 11. November beginnt die Karnevalssession in Köln.
46. Am Martinsfeuer endet der Laternenumzug.
47. B
48. B
49. C
50. A
51. B
52. b
53. a
54. c
55. d
56. mehr
57. später
58. leiser
59. früher
60. A
61. B
62. C
63. A
64. B
65. A
66. B
67. B
68. B
69. A
70. Laterne
71. basteln
72. Lied
73. Kostüm
74. Umzug
75. Stern
76. Die Kinder freuen sich, weil St. Martin kommt.
77. Er bleibt zu Hause, weil es dunkel ist.
78. Sie geht in die Bibliothek, weil sie ein Buch lesen will.
79. Köln feiert, weil die Karnevalssession beginnt.
80. Richtig
81. Falsch
82. Richtig
83. A
84. B
85. B
86. B
87. A
88. B
89. B
90. A
91. B
92. B
93. wird
94. ob
95. geht
96. spricht
97. Kranzniederlegung
98. Versöhnung
99. Verbundenheit
100. gedenken
101. wird
102. werden
103. wird
104. A
105. länger
106. weil
107. Viele bleiben zu Hause, weil es dunkel ist.
108. A
109. ob
110. fraglich
111. Ich finde, dass das Gedenken Stille braucht.
112. B
113. A
114. B
115. A
116. B
117. A
118. B
119. B
120. A
121. A
122. B
123. C
124. A
125. B
126. B
127. A
128. C
129. A
130. B
131. A
132. B
133. Die Karnevalssession beginnt am Mittwoch.
134. Wir basteln eine Laterne aus Papier.
135. Die Kinder gehen am Montag wieder in die Schule.
136. Am Sonntag ist Volkstrauertag in ganz Deutschland.
137. 狂欢节11 点 11 分在科隆开幕。 [native-label diff vs EN]
138. 我周三做一个灯笼。 [native-label diff vs EN]
139. 学校 11 月 9 日又开学了。 [native-label diff vs EN]
140. Am Sonntag schaue ich das NFL-Spiel. [diff vs core only; == EN]
141. b
142. a
143. d
144. c
145. B
146. A
147. A
148. B
149. A
150. 开放题 [native-label diff vs EN]

## Group adjudications
1–10 (P1): 1 Länderspielpause (headline/Q1), 2 Belgrad (Fri in Belgrad), 3 Karnevals (genitive 'Session des Karnevals'), 4 München (NFL city), 5 fünf (5 Punkte), 6 Volkstrauertag (Sunday Gedenktag), 7 B Belgrad, 8 C 15.30, 9 A 11.11, 10 A Sonntag 15. Nov. — all match P1 article/quiz options.
11–15 (P2 times/dates): 11.11 / 10.30 / 15.30 / 11. November / Mittwoch (11 Nov 2026 = Wednesday) — all verbatim from P2 article.
16–20 (Perfekt): hat begonnen / haben gesungen / haben gebastelt / hat geteilt / haben gegessen — correct haben + Partizip II, verb-final.
21–24 (P2 comprehension): B ab 10.30, B Gebäck aus Hefeteig, A kein Feiertag, B Rotkohl und Klöße.
25–28 (matching): c Jeck, a Laterne, b Weckmann, d Martinsgans — each option text matches the P2 definitions list.
29–33 (Richtig/Falsch): Richtig (Roman soldier), Falsch (geese betrayed, did not hide), Richtig (11 Nov), Falsch (results NOT fest at deadline), Richtig (11.11).
34–38 (word box): Mantel, Laterne, Gans (Martinsgans), Kostüm, Martinsfeuer — each fits its sentence and the P3 word list.
39–42: B Bischof von Tours, B Umzüge auch vor/nach 11.11., A Gänsebraten, A VOL.4.
43–46 (sentence building): verb-second order correct in all four; 45/46 fronted adverbials with verb in 2nd position.
47–51: B fünf, B 5. Nov, C UEFA-Strafe, A 2:0, B ausverkauft — all verbatim from P4 article.
52–55 (matching): b Geisterspiel, a Hinspiel, c Ausrüster, d ausverkauft — match P4 definitions.
56–59 (comparatives): mehr (8>5), später (15:30>11:11), leiser (empty stadium), früher (5 Nov < 13 Nov) — forms and semantics correct.
60–64 (fixture times): A 20.45, B 15.30, C 20.45, A 20.30, B 17.30 — all read off the P4 Spielplan table.
65–69: A 9. Nov, B Laternen aus Papier, B Karneval Vormittag/St. Martin Abend, B NFL, A Nationalmannschaft in Belgrad.
70–75 (word box): Laterne, basteln (plural subject), Lied (Martinslied), Kostüm, Umzug, Stern — fit sentences + P5 word list.
76–79 (weil): verb-final kommt / ist / will / beginnt — all correct subordinate word order.
80–82: Richtig (Bayern Ferien vorbei), Falsch (Umzug am Abend, nicht Vormittag), Richtig (Martinslieder).
83–88 (diagram, recomputed): 83 A 46% max, 84 B 34% second, 85 B 46+34=80, 86 B Gedenken 20% smaller, 87 A 20%, 88 B 46+34+20=100. Arithmetic recomputed by proofreader: 80 and 100 correct.
89–92: B 15. Nov, A ZDF, B 2,05 Cent, B 27. Nov — verbatim P6 article.
93–96 (grammar): wird (passive), ob (indirect question), geht (Debatte geht weiter), spricht (3sg sprechen).
97–100: Kranzniederlegung, Versöhnung, Verbundenheit, gedenken (+ genitive 'der Opfer') — verbatim P6.
101–104: wird (passive sg), werden (plural 'zwei Feste'), wird (future), A Passiv.
105–108: länger, weil, 'Viele bleiben zu Hause, weil es dunkel ist.' (verb-final), A 'länger als sonst' = longer than usual.
109–112: ob, fraglich, 'Ich finde, dass das Gedenken Stille braucht.' (dass verb-final), B 'Meiner Meinung nach…'.
113–120 (P8 cloze, 3rd-person singular present): A beginnt, B bastelt, A geht, B singt, A schaut, B sieht (irregular sehen), B erzählt, A beginnt — subject-verb agreement checked against each sentence subject (die Schule / Lena / sie / der Karneval).
121–128: A 11.11, B Belgrad, C 15.30, A 15. Nov, B 2,05, B 5. Nov, A ZDF, C 22. Nov (Totensonntag; 18. Nov is Buß- und Bettag distractor).
129–132 (Berger text): A halb acht (= 7:30), B eine Laterne, A Deutschland in Belgrad, B Sonntag 15.30.
133–136 (sentence building): verb-second correct in all four.
137–139 (DE→ZH translations): accurate — 狂欢节11点11分在科隆开幕 / 我周三做一个灯笼 / 学校11月9日又开学了 (wieder begonnen = 又开学了).
140 (ZH→DE translation): 'Am Sonntag schaue ich das NFL-Spiel.' — time-fronted, verb second, correct; text-identical to EN fan-out.
141–144 (matching): b Mantel, a Laterne, d Geisterspiel, c Versöhnung — match P8 definitions a–d.
145–149 (dialogue agreement): B singst (du), A macht (ihr), A essen (wir), B machst (du), A schaue (ich) — each matches its pronoun; distractors are other persons.
150: open writing task, label '开放题' — no fixed key; legitimate native label (EN 'Open task').

Result: 150/150 verified. 0 wrong keys. 0 transpositions. sNFL 0 everywhere in the canonical edition.
