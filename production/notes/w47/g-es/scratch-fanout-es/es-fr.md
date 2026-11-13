# es-fr — 逐版记录（2026-11-10/11）

## 覆盖预检

- fr-missing 136 项，0 未覆盖（MANUAL + harvest/fr.json 251 键 + 特殊处理）。
- fr-conflicts 0 行。

## 应用

- `apply_fanout.py fr`：leftover zh keys NONE；CJK in .py NONE。
- 5 处 manual-over-harvest：CULTURA→"Culture"、JUVENTUD→"Jeunesse"、VIDA→"Vie"（首字母大写非全大写）；"Après ___ (infinitif : envoyer)" 法语冒号前空格；"造句" 的 harvest "Former une phrase" → manual "Former des phrases"（复数，合指令体）。
- 总替换数未记录（apply JSON 的 `replacements` 是逐键 dict，与 en/de 相同）。

## 预修（量测后应用，全部 wrap 实测）

1. P1 gloss：原文 3 行 @19 → "« Débat » : des personnes discutent en public." 1 行 @19。
2. P7 word-box gloss：4 行 @20 → "debate = débat : une discussion publique ; l'élection a lieu le 29." 2 行 @20。
3. P7 F-MAIL ed note：6 行 @20/@19 → "Note de la rédaction : aucun vrai courrier ni meilleur texte avant le bouclage ; ce numéro publie une lettre d'exemple. La promesse vaut pour le VOL.5." 4 行 @19（保留 "ni meilleur texte" 与 "avant le bouclage"；删 "de la rédaction" 与 "Écrivez-nous !"）。
4. P7 ERRORES TÍPICOS 注释（**fr 新发现**）：2 条在 19.5 单位下各绕 2 行（"mejor est déjà un comparatif : pas de más."、"gente est un nom collectif singulier : verbe au singulier."），各加 26.5px → build1 P7 col3 达 2042.55（非 gloss/note 数学预测的 ~1989.5）。缩为 "mejor est un comparatif : pas de más." 与 "gente est singulier : verbe au singulier." 各 1 行。
5. P5 your-turn：4 行 @20 → "Voterais-tu par courrier ou en personne ? Qu'achèterais-tu le Black Friday ? Écris deux phrases et envoie-les." 3 行 @19。
6. P3 your-turn：3 行 @20（1600.75，仅 7px 余量）→ 改 @19（1594.75，13px 余量）。
7. P2 C-intro：2 行 → "Lis l'article et choisis la bonne réponse." 1 行 @20.5。
8. P5 B-bridge：3 行 → "Complète avec les mots de l'encadré ; conjugue si nécessaire." 2 行 @20.5。
9. P8 header：右注 737.7 单位 @19.5 → header 1302→1337、keys flow 1328→1363。
10. P6 band：补全 "Lire la campagne : débats, programmes et sondages"（959.2 单位 @18）。
11. 信件括号全角 → 半角 "(ejemplo, escrito por la redacción)"。
- P4 your-turn 5 行 @20（箱底 ~993.5，fixture 表 1140 起）、P2 your-turn 6 行 @20（col3 ~1051）：无需修。
- **预修脚本插曲**：第一轮只应用了 content12.py 两处即 abort——P7 gloss 替换用 U+2019（'）而文件用 ASCII 撇号；第二轮改用 ASCII 撇号重做，16 处替换均 count 校验通过。
- P7 col3 预算：gloss 2 行（Δ0）+ ed note 4 行 @19（Δ+21）+ error notes 各 1 行（Δ0）→ 1865.51，与 de 相同。

## Build 经过

- **build1**（仅 P1 gloss + C-intro 应用）：run rc=0，TOTAL 150；P3 col3 1600.75；P5 col3 **1609.55（超 y=1608 分隔线 1.55px）**；P7 col3 **2042.55**；P8-keys 3 处溢出，终 y=2590。
- **build2**（全部预修后）：run rc=0，0 溢出以外的几何全部到位（P3 1594.75，P5 1574.55，P7 1865.51）；P8-keys 仍 8 处溢出，终 y=2590。诊断：22 项多行（core 仅 #44、#139）。
- **build3（终版）**：19 条注释收至 1 行（§6.4 详见 KIT）；run rc=0，0 OVERFLOW/TOO WIDE，TOTAL 150，P8-keys 终 y=2521（39px 余量）。保留 2 行：#44/#139（core 一致）、#137（键本身占满一行，注释已是最简 "Cf. l'original."）。

## 门禁（build3）

- render rc=0：print 3,499,799 B；web 846,204 B，46,247 text bytes。
- occlusion 0 flags；sweep_de.py：bridge orphans 0，box-vs-hline 0。
- p8 extract 150/150；compare CLEAN，keydiff=[137, 138] 已裁定（重定向译题，W45/W46 判例）。
- freeze：工具 8 OK；直接 sha256 8/8。
- pdftotext print = web，46,247 B 字节一致。
- P8 最小字号 10.125pt（pypdf `Tm` 实测）。
- §1.1：paper #fbfaf6 ×8；VOL.4 ×9，VOL.5 ×3（均为合法下期指涉）；徽章 A2 11 / B1 21 / B2 3 = 35，Q113–150 齐全；金/砖红/近黑 0（moth 黄为品牌蛾）；masthead 196 单位。
- 全角标点 .py 与 SVG 文本中均为 0；CJK 仅 P1 moth title 三色蛾（继承自 core，不可见元数据）。
- gloss 词 token 数全部 ≥2（与 en/de 相同数值）。

## 目视（8 版 PNG 全部读过）

- P1：gloss 1 行；quiz 齐全；bridge 正常。
- P2：C-intro 1 行位于 col 2 底；¿Y TÚ? 箱 6 行法译在箱内。
- P3：¿Y TÚ? 箱底在 EJERCICIOS 分隔线上方；A-bridge 1 行；C-bridge 2 行同列。
- P4：¿Y TÚ? 箱在 fixture 表上方；A-bridge 2 行同列；D-bridge 2 行同列。
- P5：¿Y TÚ? 箱底在分隔线上方；A-bridge 1 行；B-bridge 2 行同列；C-bridge 2 行同列。
- P6：band 副标题全译 "Lire la campagne : débats, programmes et sondages"；A-bridge 2 行同列；D-bridge 2 行同列。
- P7：word-box gloss 2 行；信件半角括号；ed note 4 行在箱内；banner 远在 footer 上方；ERRORES 注释各 1 行。
- P8：RESPUESTAS header + 右注与天鹅图注无重叠；keys 终在 footer 上方；150 键可见；Q113–120、Q145–149 徽章齐全；#137 2 行、#44/#139 2 行均已裁定。

## 150 键复核

- 全量 REG 读完（`es-fr-keys.txt` 150 行）：键与 core 一致（p8 CLEAN），法语注释准确。
- 配对集逐字母核对：25–28（debate=débat c, mitin=meeting b, cartel=affiche d, escaño=siège au Parlement a）、52–55（jornada=journée c, derbi=derby b, liderato=première place a, fase liga=phase de ligue d）、141–144（sondeo=sondage c, muestra=échantillon d, margen de error=marge d'erreur b, junta electoral=commission électorale a）。

## 文本与交付

- `.text.md` 1,800 行，全文读完（法语层逐行；西班牙语冻结同 core）；数字 1–150 齐全；0 CJK；无 "12 de noviembre"。
- ABSTRACT.txt（法语一行，无 ASCII 双引号，504 字节）。
- WEEKLY-KIT.md（mirrors es-de KIT；裁定 §6.1–§6.12；3 轮自校记录；终轮零发现）。
- 8 SVG（`svg/`）+ 8 PNG（`cards/`）。
- print `La-Lucerna-VOL4-es-fr.pdf` 3,499,799 B，SHA-256 `c1c3ecdc326da7d91a4c55e8ad578e66d574db4436d6ec7a23164d653f54b168`；web 846,204 B，SHA-256 `e6e5abbf4f923e4dfbae62777b1cea88f863e444d5be2e61892609005a245065`。

## 自查结论

**零已知缺陷；待独立复校。**

## 本版文件

- `es-fr-build1.log` / `es-fr-build2.log` / `es-fr-build3.log`、`es-fr-render3.log`、`es-fr-freeze.log`、`freeze-es-fr-3/`、`es-fr-keys.txt`、`extract_text_es_fr.py`、`2026-w47-es-fr-apply.json`（apply 报告）。
