# es-it — 逐版记录（2026-11-11）

## 覆盖预检

- it-missing 135 项，类别与 de/fr 相同（MANUAL 表覆盖，如 "1 点用单数 Es" → it "Per l'una si usa il singolare Es"）；it-conflicts 0 行；it.json 251 键。

## 应用

- `apply_fanout.py it`：476 替换；5 处 manual-over-harvest：CULTURA→"Cultura"、JUVENTUD→"Giovani"、VIDA→"Vita"（首字母大写非全大写）；"Dopo ___ (infinito: enviar)" 冒号；"造句" harvest "Costruisci" → manual "Formare frasi"（不定式，合指令体）。leftover zh keys NONE；CJK in .py NONE。

## 预修（量测后应用，全部 wrap 实测）

1. P1 gloss：原文 2 行 @19 → "«Dibattito»: più persone discutono in pubblico." 1 行 @19。
2. P7 word-box gloss：3 行 @20 → "debate = dibattito: una discussione pubblica; le elezioni sono il 29." 2 行 @20。
3. P7 F-MAIL ed note：6 行 @20/@19 → "Nota della redazione: nessuna lettera vera né miglior testo prima della chiusura; questo numero pubblica una lettera di esempio. La promessa passa al VOL.5." 4 行 @19。
4. P7 ERRORES 注释：4 条在 19.5 单位下均 1 行（与 fr 不同，无 +53px 问题）。
5. P5 your-turn：4 行 @20/@19 → "Voteresti per posta o di persona? Cosa compreresti il Black Friday? Scrivi due frasi e mandale." 3 行 @19。
6. P3 your-turn：3 行 @20（1600.75，仅 7px 余量）→ 改 @19（1594.75，13px 余量）。
7. P2 C-intro：2 行 → "Leggi l'articolo e scegli la risposta giusta." 1 行 @20.5。
8. P5 B-bridge：**保持 harvest 原文**（与 de/fr 不同）——意大利语桥为 2 行，扫查验证两行同在 col 2，无孤儿；1 行备选 "Completa con le parole del riquadro." 已量测备用。
9. P8 header：右注 511.3 单位 @19.5 → header 1302→1337、keys flow 1328→1363。
10. P6 band：补全 "Leggere la campagna: dibattiti, programmi e sondaggi"（976.8 单位 @18）。
11. 信件括号全角 → 半角 "(ejemplo, escrito por la redacción)"。
- P4 your-turn 5 行 @20（箱底 ~993.5，fixture 表 1140 起）、P2 your-turn 5 行 @20（col3 ~1022）：无需修。
- P7 col3 预算：gloss 2 行（Δ0）+ ed note 4 行 @19（Δ+21）→ 1865.51，与 de/fr 相同。

## Build 经过

- **build1**（全部预修后）：run rc=0，TOTAL 150；P3 col3 1594.75，P5 col3 1574.55，P7 col3 1865.51；P8-keys 7 处溢出，终 y=2605（与 de build1 相同）。诊断：19 项多行（core 仅 #44、#139）。
- **build2（终版）**：16 条注释收至 1 行；run rc=0，0 OVERFLOW/TOO WIDE，TOTAL 150，P8-keys 终 y=2521（39px 余量）。保留 2 行：#44/#139（core 一致）、#137（键本身占满一行，注释已是最简 "Cfr. l'originale."）。
- 注：#150 诊断时用的 key+note 形式是量测假象（类型名 "Scrivi" ≠ "Schreiben"）；实际渲染为 ✓ 形式 "150. ✓ Vedi il modello, sezione H (97 parole)"，1 行。

## 门禁（build2）

- render rc=0：print 3,498,408 B；web 845,673 B，45,642 text bytes。
- occlusion 0 flags；sweep_de.py：bridge orphans 0，box-vs-hline 0。
- p8 extract 150/150；compare CLEAN，keydiff=[137, 138] 已裁定（重定向译题，W45/W46 判例）。
- freeze：工具 8 OK；直接 sha256 8/8。
- pdftotext print = web，45,642 B 字节一致。
- P8 最小字号 10.125pt（pypdf `Tm` 实测）。
- §1.1：paper #fbfaf6 ×8；VOL.4 ×9，VOL.5 ×3（均为合法下期指涉）；徽章 A2 11 / B1 21 / B2 3 = 35，Q113–150 齐全；金/砖红/近黑 0（moth 黄为品牌蛾）；masthead 196 单位。
- 全角标点 .py 与 SVG 文本中均为 0；CJK 仅 P1 moth title 三色蛾（继承自 core，不可见元数据）。
- gloss 词 token 数全部 ≥2（P1 reflexión 2；P2 mitin 2 / cartel 3 / escaño 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6；P4 parón 2 / liderato 3；P5 papeleta 2 / censo 3 / plazo 3）。

## 目视（8 版 PNG 全部读过）

- P1：gloss 1 行；quiz 齐全；bridge 无 "Notes —" 前缀（it harvest 体例）。
- P2：C-intro 1 行位于 col 2 底；¿Y TÚ? 箱 5 行意译在箱内；页头 "EJERCICIOS　ESERCIZI　PAGINA 2"（it harvest 的页码标，与 de "Übungen zu Seite 2" 同类）。
- P3：¿Y TÚ? 箱底在 EJERCICIOS 分隔线上方；A-bridge 1 行；B-bridge 1 行；D-bridge 2 行同列。
- P4：¿Y TÚ? 箱 5 行在 fixture 表上方；A-bridge 2 行同列。
- P5：¿Y TÚ? 箱底在分隔线上方；A-bridge 2 行同列；B-bridge 2 行同列；C-bridge 2 行同列。
- P6：band 副标题全译；A-bridge "Guarda i grafici e scegli." 1 行（it harvest 简写）；D-bridge 2 行同列。
- P7：word-box gloss 2 行；信件半角括号；ed note 4 行在箱内；banner 远在 footer 上方；ERRORES 注释各 1 行。
- P8：RESPUESTAS header + 右注与天鹅图注无重叠；keys 终在 footer 上方；150 键可见；Q113–120、Q145–149 徽章齐全；#137 2 行、#44/#139 2 行均已裁定。

## 150 键复核

- 全量 REG 读完（`es-it-keys.txt` 150 行）：键与 core 一致（p8 CLEAN），意大利语注释准确。
- 配对集逐字母核对：25–28（debate=dibattito c, mitin=comizio b, cartel=cartellone d, escaño=seggio in Parlamento a）、52–55（jornada=giornata c, derbi=derby b, liderato=primo posto a, fase liga=fase a girone d）、141–144（sondeo=sondaggio c, muestra=campione d, margen de error=margine d'errore b, junta electoral=commissione elettorale a）。

## 文本与交付

- `.text.md` 1,788 行，全文读完（意大利语层逐行；西班牙语冻结同 core）；数字 1–150 齐全；0 CJK；无 "12 de noviembre"。
- ABSTRACT.txt（意大利语一行，无 ASCII 双引号，471 字节）。
- WEEKLY-KIT.md（mirrors es-fr KIT；裁定 §6.1–§6.12；2 轮自校记录；终轮零发现）。
- 8 SVG（`svg/`）+ 8 PNG（`cards/`）。
- print `La-Lucerna-VOL4-es-it.pdf` 3,498,408 B，SHA-256 `d4eaaf2fd3f955c17140f3a648ccfef538fa21564a5dde28f71e5da1ee96a2a7`；web 845,673 B，SHA-256 `24bd25008151e3dd14d7e2d8769aa541781bd9dc3ffc2a0006aca5ba4e70a435`。

## 自查结论

**零已知缺陷；待独立复校。**

## 本版文件

- `es-it-build1.log` / `es-it-build2.log`、`es-it-render2.log`、`es-it-freeze.log`、`freeze-es-it-2/`、`es-it-keys.txt`、`extract_text_es_it.py`、`2026-w47-es-it-apply.json`（apply 报告）。
