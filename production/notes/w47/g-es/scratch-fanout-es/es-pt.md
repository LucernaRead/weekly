# es-pt 逐版记录（fan-out，2026-11-11）

## 覆盖预检

- pt-missing 129 项；pt-conflicts 11 行；pt.json 257 keys。
- pt-conflicts 全部裁定为 instruction-word 变体（非缺陷）：每个 `f.ex()` 调用同时带 type label（名词/不定式："Formar frases" / "Tradução" / "Escrita"，作徽章）与 `instr=`（命令式："Forme a frase" / "Traduza" / "Escreva"，作题干指令）；content8.py/content34.py grep 核实，与 W46 pt 结构一致。content8.py:134：`if e_["type"] == "Escrita": txt = f"{n}. ✓ {note}"`（#150 的 ✓ 形式）。

## Apply

- `apply_fanout.py pt`：476 字面替换；6 处 manual-over-harvest 覆盖（CULTURA→"Cultura"，JUVENTUD→"Juventude"，VIDA→"Vida"，首字母大写非全大写；"Después ___ (infinitivo: enviar)" 带冒号；"muchísims aficionados = muitíssimos adeptos"——manual 选 "adeptos" 而非 harvest "torcedores"；P8 表头 "PÁGINA 8" → manual "Página 8" 去大写）。
- 残留 zh keys：NONE；.py 内 CJK：NONE。

## 预修（全部 wrap 实测后才 build）

1. P1 gloss："«Debate»: duas ou mais pessoas discutem em público, por turnos e com perguntas."（2 行 @19）→ **"«Debate»: as pessoas discutem em público."**（1 行 @19）。
2. P7 word-box gloss："debate = debate: uma discussão pública, por turnos. Esta é a semana dos debates; a eleição é no dia 29."（3 行 @20）→ **"debate = debate: uma discussão pública; a eleição é no dia 29."**（2 行 @20）。
3. P7 F-MAIL editor's note："Nota da redação: até ao fecho, não tinham chegado cartas verdadeiras nem os melhores textos; esta edição publica uma carta de exemplo da redação. A promessa passa para o VOL.5. Escrevam-nos!"（6 行 @20，5 行 @19）→ **"Nota da redação: até ao fecho, não tinham chegado cartas verdadeiras nem melhores textos; esta edição publica uma carta de exemplo. A promessa passa para o VOL.5."**（4 行 @19；保留 "esta edição"，删 "da redação" 与 "Escrevam-nos!"）。
4. P7 ERRORES notes：4 条 @19.5 全是 1 行（无 fr 式 +53px）。
5. P5 your-turn："Votarias **pelo** correio ou em pessoa? O que comprarias na Black Friday: algo útil ou um capricho? Escreve duas frases e envia-as."（4 行 @20/@19）→ **"Votarias pelo correio ou em pessoa? O que comprarias na Black Friday? Escreve duas frases e envia-as."**（3 行 @19）。
6. P3 your-turn：3 行 @20（box 1600.75，距分隔线仅 7px）→ @19 渲染（1594.75，13px 边距）。
7. P2 your-turn：6 行 @20（col3 ~1051），P4 your-turn：5 行 @20（box ~993.5，分隔表 1140）——无需修。
8. P2 C-intro："Leia o artigo da página 2 e escolha a resposta certa."（2 行）→ **"Leia o artigo e escolha a resposta certa."**（1 行 @20.5）。
9. P5 B-bridge："Complete com as palavras do quadro. Atenção: algumas palavras mudam de forma."（3 行）→ **"Complete com as palavras do quadro; conjuga se necessário."**（2 行 @20.5）。
10. P6 band："Ler a campanha" → **"Ler a campanha: debates, programas e sondagens"**（943.8 units @18）。
11. P8 表头：右注 "Cada resposta traz uma breve nota　✓ marca a questão de redação" 606.5 units @19.5 → 表头 1302→1337，keys flow 1328→1363。
12. 信件括号全角→半角 "(ejemplo, escrito por la redacción)"（content7.py:99）。
- P7 col3 预算：gloss 2 行（Δ0）+ ed note 4 行 @19（Δ+21）→ 1865.51（与 de/fr/it 相同）。

## 预修脚本事故（pt）

- 第一遍 pre-fix 只应用了 P1 gloss、P2 C-intro、P7 gloss、P7 ed note、信件括号、P6 band，在 P5 your-turn 替换处 abort——count 0，因脚本写的是 "por correio"，文件实际是 "**pelo** correio"。build1 因此带部分修复跑（P3 1600.75、P5 1609.55——超分隔线 1.55px、P7 1865.51、P8-keys 5 溢出止于 y=2590）。第二遍用正确字符串 "pelo correio" 补齐其余 8 处替换，全部 count 核实。教训（fr 已有）：替换字符串一律从文件原样读出，绝不凭记忆重打；部分修复的 build 也能跑，其数值正好显示哪些修复已落地。

## Builds

- **Build 1**（部分预修）：run rc=0，TOTAL 150；P3 1600.75，P5 **1609.55（超 y=1608 分隔线 1.55px）**，P7 1865.51；P8-keys 5 溢出，止于 y=2590。
- **Build 2**（预修补齐）：run rc=0，TOTAL 150；P3 1594.75，P5 1574.55，P7 1865.51；P8-keys 仍 11 溢出，止于 y=2590。诊断：26 项多行 P8（core 仅 2 项）——拉丁版最多（de 21、fr 22、it 19）。
- **Build 3**：22 条 note 收至 1 行（13.5 units 下 wrap 核实）：#4/#21/#29 "Dia do Flamenco, segunda-feira, 16 de novembro"、#30 "UNESCO: flamenco no património desde 2010"、#31 "O flamenco: canto, guitarra e dança juntos"、#32 "Santa Cecília é a 22 de novembro"、#33 "Banda de Bilbau, domingo, 22, às 12h00"、#41 "O flamenco nasceu de várias culturas na Andaluzia"、#42 "Depois do Flamenco: a eleição de 29 de novembro"、#43 "Sujeito, verbo, predicativo"、#45 "O lugar antes"、#56 "más + importante (a luta pelo título)"、#68 "O MiDNI é a nova forma de provar a identidade"、#73 "documento de identidade"、#82 "Este ano pode-se votar com o MiDNI"、#86 "Sem sondagens durante 5 dias (24–28 de novembro)"、#88 "Só os minutos grátis, com a fonte"、#92 "Pesquisa: foto com margem de erro, num dia certo"、#133 "O tempo antes, depois o verbo"、#136 "Interrogativa no início"、#137/#138 "Cf. o original."（标准葡语缩写）、#149 "A que horas fecha?"。保留 2 行收尾（裁定）：#44/#139（core 一致）与 #137（键独占整行，任何 note 都变 2 行）及 #1（冻结键 + 完整句 note，本身就是答案，与 de 同裁定）。run rc=0，0 OVERFLOW / TOO WIDE，TOTAL 150，P8-keys y=2521（39px 余量）。**诊断要点：P8 诊断须用该版实际的 writing-type 名（pt "Escrita"，content8.py:134），"Schreiben" 会把 #150 误测为 key+note 形式而非实际渲染的 ✓ 形式。**
- **Build 4（终版）**：P2 日历标题 gloss 由 "O calendário da semana" 缩为 "O calendário"（§6.13）。run rc=0，0 溢出，TOTAL 150；P3 1594.75，P5 1574.55，P7 1865.51，P8-keys y=2521。

## 门禁（build 4）

- render rc=0：print 3,500,787 B；web 847,463 B（< 7 MB），45,996 text bytes。
- occlusion **0 flags**（build 3 为 1 flag，§6.13 修复后归零）；sweeps：bridge 孤行 0，box-vs-hline 0。
- p8 extract 150/150；compare CLEAN，keydiff=[137, 138] 已裁定（重定向：葡语句为键，"Cf. o original."；与 en/de/fr/it 同裁定）。
- freeze：工具 8 OK；直接 sha256 8/8（`freeze-es-pt-4/build-copy/svg` vs shipped `svg/`）。
- pdftotext print = web，45,996 B 逐字节一致。
- P8 最小字号 10.125pt：Tm d 最小值 106.5（150 条目），与 core 及 es-en 完全一致（core KIT 标称 10.125pt）。
- §1.1：paper #fbfaf6 ×8，VOL.4 ×9，VOL.5 ×3；chips A2 11 / B1 21 / B2 3 = 35（另有 #37402f 表头横条 1，与 core 相同）；Q113–150 全部带徽章；全角标点 .py 与 SVG 文本均为 0（118 个 U+3000 表意空格是标题分隔符，core 亦然）；CJK 仅蛾标 title（P1）。
- gloss token 计数全 ≥2（P1 reflexión 2；P2 mitin 2 / cartel 2 / escaño 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6；P4 parón 2 / liderato 3；P5 papeleta 2 / censo 3 / plazo 3）。

## 目视（8 张 PNG，全部干净）

- P1：gloss 1 行；配对行、数字框、quiz 正常。
- P2：C-intro 1 行在第 2 栏底；"EL CALENDARIO　O calendário" 标题完整、与 Note 框无交叠（§6.13 修复已验）；¿Y TÚ? 框 6 行在内。
- P3：¿Y TÚ? 框在分隔线上方；A-bridge 1 行，B-bridge 1 行，D-bridge 2 行同栏。
- P4：¿Y TÚ? 框 5 行在 fixture 表上方；A-bridge 2 行同栏。
- P5：¿Y TÚ? 框在分隔线上方；A-bridge 2 行同栏，B-bridge 2 行同栏，C-bridge 2 行同栏。
- P6：band 副标题完整 "Ler a campanha: debates, programas e sondagens"；A-bridge 1 行，D-bridge 2 行同栏。
- P7：word-box gloss 2 行；信件半角括号；ed note 4 行在框内；banner 远在 footer 上方；ERRORES 4 条全 1 行。
- P8：RESPUESTAS 表头 + 注远离天鹅图注；keys 止于 footer 上方；150 键全可见；Q113–120、Q145–149 徽章在；#1 2 行、#44/#139 2 行、#137 2 行（均已裁定）；#150 ✓ 形式。

## 150 键复核

- REG 全量 dump 读完（`es-pt-keys.txt`，150 行）；matching 组逐字母核实：25–28（debate=debate c、mitin=comício b、cartel=cartaz d、escaño=lugar no Parlamento a）、52–55（jornada=jornada c、derbi=dérbi b、liderato=primeiro lugar a、fase liga=fase de liga d）、141–144（sondeo=pesquisa c、muestra=amostra d、margen de error=margem de erro b、junta electoral=comissão eleitoral a）。
- #57 "muchísimos aficionados = muitíssimos adeptos"（manual 覆盖已落地）；#73 "documento de identidade"；#149 "A que horas fecha?" 1 行。

## .text.md

- 1,797 行，逐行读完（葡语层逐行；西班牙语冻结如 core）；数字 1–150 全在；0 CJK；无 "12 de noviembre"。
- 导出脚本 `extract_text_es_pt.py`（由 it 版复制，仅改 title slug；sed 换 es-it→es-pt 后 grep 验无残留）。

## 交付（全部位于 `~/workspace/weekly-git/production/2026-w47/2026-w47-es-pt/`）

- `La-Lucerna-VOL4-es-pt.pdf` — 3,500,787 B，SHA-256 `4793edeb87c2d6cd138906bbdeb0c2fc47088c91a11d99e75582b71daafde4e0`
- `La-Lucerna-VOL4-es-pt-web.pdf` — 847,463 B，SHA-256 `d7429fcb83d70735f38587527d0fcc1032389d891e94b12b7dba4ad4ee4776ef`
- `2026-w47-es-pt.text.md`（1,797 行）
- `ABSTRACT.txt`（葡语，一行，无 ASCII 双引号，469 字节）
- `WEEKLY-KIT.md`（裁定 §6.1–§6.13；4 轮自校记录；终轮零发现）
- 8 SVG（`svg/`）、8 PNG（`cards/`）
- **自查结论：零已知缺陷；待独立复校。**

## 新缺陷类（留给后续 nl/ru/ja/ko/zh-tw）

- **§6.13 P2 盒标题 gloss 过长**：葡语 "O calendário da semana" 使 "EL CALENDARIO" 标题宽 411.5 units（20 号粗体），尾巴越过盒边侵入邻侧 Note 框（TEXTX 22.8×15.2px，渲染中肉眼可见被截成 "O calendário da sem…"）。其余四拉丁版 gloss 均为短单字（THE WEEK / DIE WOCHE / LE CALENDRIER / IL CALENDARIO）。修：缩为 "O calendário"（300.5 units）。**后续版须逐个实测每个盒标题 gloss 的宽度**——栏宽看起来够，不等于标题不会越界撞进邻框。

## 记录文件

- `es-pt.md`（本文件）、`es-pt-build1/2/3/4.log`、`es-pt-render3/4.log`、`es-pt-freeze.log`、`freeze-es-pt-4/`、`es-pt-keys.txt`、`extract_text_es_pt.py`、`2026-w47-es-pt-apply.json`；`FANOUT-REPORT-es.md` 已更新（es-pt 行）。
- 注意：p8.py / freeze.py 的 CLI 须按 `--help` 用（extract 用 `--p8 … --total 150`；freeze 用 `baseline --build … --core-svg … --out …`）；凭记忆拼的参数会报 usage error（本次已纠正，未影响结果）。
