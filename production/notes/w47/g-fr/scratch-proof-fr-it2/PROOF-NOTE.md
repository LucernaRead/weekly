# PROOF-NOTE — W47 fr-it proof2（独立复校，re-fanout #2 重建版）

- 版：`production/2026-w47/2026-w47-fr-it/`（法语核心、读者意大利语），re-fanout #2 从 core-fr fix4 全量重建（`r2run1`）
- 复校员：独立复校（与构建者不同人），2026-11-11
- 结论：**(a) 零缺陷，可定稿**
- 工作目录（本报告所在）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-it2/`
- 只读生产文件：复校前后重验印/网 PDF 与 text.md 的 SHA-256 未变（见 §0）；未改任何生产文件，未 commit、未 push。决定性重建（determinism）一律在 goals 侧副本 `build-copy/` 内跑，绝不在生产目录内重跑 `run.py`（proof1 前例）。
- 构建解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 为本 scratch 下 `tmp/`。

## §0 身份核对（磁盘实测，先验 SHA 6/6 一致，复校后重验未变）

| 文件 | 字节 | SHA-256（实测 = 任务给定） |
|---|---|---|
| 印刷 `La-Lucerna-VOL4-fr-it.pdf` | 17,415,873 | `2a47495b…e5632f6` ✓ |
| 网页 `La-Lucerna-VOL4-fr-it-web.pdf` | 1,696,726 | `8957acb6…cd58b3ab` ✓ |
| `2026-w47-fr-it.text.md` | 46,617 | `fac32b0b…ca25919` ✓ |
| 核心印 `core-fr/La-Lucerna-VOL4.pdf` | 30,446,975 | `a30af667…ce25a9d` ✓ |
| 核心网 `core-fr/La-Lucerna-VOL4-web.pdf` | 2,241,835 | `56f50ca8…d58e141` ✓ |
| 核心 `2026-w47-fr-zh-cn.text.md` | 46,471 | `52024e02…9d063df` ✓ |

探针：`git hash-object -w --stdin` 通（仓库内）；`/dev/null` 存在；goals 侧写文件通。

## §1 回归对照（#1 备份 → #2，KEEP/REVERT 盘点）

proof1 三项缺陷 **全部修好，无一丢失**，且改动面完全封闭：

| proof1 缺陷 | #2 落点 | 实测 |
|---|---|---|
| D1 P7 披露框漫出（末基线 2260.6，超盒底 2.6；实墨超 7.1） | `expl.py` `courrier_disclosure` 删中句，3 行→2 行 | 末基线 **2233.3**，clearance **+24.7**（见 §2.1） |
| D2 P5 `una attrice` | `expl.py:139` `mots_photo` 第 4 项 | `une actrice — attrice`（见 §2.2） |
| D3 P5 `una séance` | `expl.py:139` `mots_photo` 第 7 项 | `une séance — spettacolo`（见 §2.2） |

- SVG 页哈希 vs #1 备份：**仅 P5/P7/P8 变**（`a91995f1` / `12eb2907` / `64d1ba48`，与重建报告 §4 一致）；P1/P2/P3/P4/P6 逐字节相同。
- SVG 文本层行级 diff（逐 `<text>` 基线并联）：P5 恰 2 行变（una→une 两处）；P7 恰披露注记 3 行→2 行，其余 137 行全同；P8 恰 2 行变（题干删 `du`、键 `devant`→`devant le`）。
- 源码 diff vs #1 备份：`expl.py` 恰 2 行（`mots_photo`、`courrier_disclosure`）；`content8.py` 恰 2 行（Q148 键与题干）；`bslib4.py`、`content12/34/56/7.py`、`svglib.py`、`run.py`、`render.py` 全部逐字节相同；`ABSTRACT.txt` 逐字节相同。**无多余改动，无 hand patch 丢失。**

## §2 本版必查（重建报告 8 项中的相关项，逐项独立实测）

### 2.1 P7 披露框（D1 复测）

- 盒：`x=989.0, y=1878.0, h=380.0, 框底 2258.0`。
- creambox（规范版 `hidden_files/w47/tools/creambox.py`）：末基线 **2233.3**，clearance **+24.7**，desc-clear **+18.8**；P7-TOOLBOX 汇总：4 盒，最小 inside clearance +24.7，最小 desc-clear +18.8。
- PIL 真墨（`pil_p7.py` 复跑，200 dpi 印 PDF）：末行灰墨 svg y **2237.3**（与重建报告一致）；间隙 **2258–2270 零墨**（NONE clean）。
- 目视：300 dpi 盒底裁切 `png/p7-courrier-bottom-300dpi.png`——披露注记 2 行完整在奶油盒内，下方白纸间隙干净，绿带未被侵入。
- 结论：D1 已修好。另注：重建报告 §2 项 1 所引 it 删句原文（“questo numero pubblica un esempio editoriale marcato.”）**并非字面删句**——旧 `expl.py` 的删句实为 “per questo pubblichiamo un esempio della redazione chiaramente indicato;”（`marcato` 一词在新旧 `expl.py` 中均不存在）。报告措辞不准，但**版本身无误**（删句后文本、行数、基线均已实测），不作本版缺陷。

### 2.2 P5 词表（D2/D3 复测；`une actrice` vs 任务原文 `une attrice` 的裁定）

- `expl.py:139`：`"une actrice — attrice"`、`"une séance — spettacolo"`（整行已核）。
- P5 SVG 文本层（Python 解析 `<text>`）：两行确为 `une actrice — attrice`、`une séance — spettacolo`；全版 8 SVG、`text.md`、印 PDF 文字层中 **`una attrice` / `una séance` 残留均为 0**。
- 目视：300 dpi 词表裁切 `png/p5-wordlist-300dpi.png`，两行清晰。
- **裁定：以 `une actrice` 为准，任务原文的 `une attrice` 是误写。**理由：核心正文同键为 `"une actrice — 女演员"`（`core-fr/expl.py:152`）；`attrice` 不是法语词，`une attrice` 在法语中不存在；proof1 D2 与核心一致。重建报告 §8 待定项 1 就此关闭——无需改回。

### 2.3 Q148（三重核对）

- registry（`registry-proof2.json`，由 build-copy 的 `run.py` 导出）：Q148 键 `devant le`。
- `content8.py`：含 `"devant le"` 与 `On se retrouve ({gnums[3]})___ cinéma ?`（无 `du`）。
- P8 SVG 文本层：含 `On se retrouve` + `cinéma ?`，不含 `du cinéma`；题干渲染为 `(148)___ cinéma ?`（300 dpi 裁切 `png/p8-dialogue-300dpi.png` 目视确认）。
- `p8.py extract`：Q148 提取键 `devant le`。
- 答案区：`148. devant le (Davanti al cinema)`。四重一致。

### 2.4 孤儿标点全扫（新增 0）

- 用重建者修正后的 `check_extra.py`（同基线判定版）独立复跑：`orphan elements: total=0 new=0 inherited=0 remnant=0 shared_baseline=0`，**EXTRA PASS**。it 版无任何标点类 `<text>` 元素（无继承、无分拆），新增真孤儿 0。

### 2.5 孤行填空线 Q130 / P3 Q36 / Q37（观察类，核心继承）

- Q130（P8）：`(989.0, 843.0)`，与核心**分毫不差**。
- P3 Q36/Q37：`(538.5, 1894.4)` / `(538.5, 2027.1)`，x 与核心相同，y 为 **+30 档**（de/it/ru 档；ja/ko/zh-tw +0；en/es/pt/nl +59.5），与重建报告一致。
- 未修核心，未判 (b)。P8 目视：Q130 填空线 `___` 独行于题干末，形态与核心一致。

### 2.6 150 键逐项手核（key-vs-stem 适配，Q73 教训：三源一致也可能同错）

方法：不只比三源是否一致，而是逐题读题干判键是否适配——123 题取 `text.md` 题干行（`N. …`，含题内选项），5 组配对题（22–25 / 49–52 / 73–76 / 85–88 / 140–144）取 `content*.py` 的 `match_set` 左右列逐对验语义（`match_set` 按给定顺序以 a/b/c/d… 逐项编号，键即所匹配右列的字母），对话题 145–149 取 P8 SVG 对话全文逐句验，Q150 为写作题例外。结果：**150/150 适配，无一错配**。

- 配对题逐对验（左→键→右列定义）：22 `un vote`→a“la décision ensemble”✓；23 `un vin primeur`→b“un vin de l'année, très jeune”✓；24 `un déchet`→c“ce qu'on jette”✓；25 `une finale`→d“le dernier match d'un tournoi”✓；49 `un forfait`→a“ne pas jouer, à cause d'une blessure”✓；50 `un tableau`→b“la liste des matches d'un tournoi”✓；51 `un tirage`→c“le sort qui fait les groupes”✓；52 `la trêve`→d“la pause entre deux séries de matches”✓；73 `un prequel`→a“un film qui raconte l'avant d'une histoire”✓；74 `une bande-annonce`→b“la courte vidéo qui présente un film”✓；75 `la seconde main`→c“acheter des objets déjà utilisés”✓；76 `un atelier`→d“le lieu où l'on répare ensemble”✓；85 `un sénateur`→a“un élu du Sénat”✓；86 `rejeter`→b“dire non à un texte”✓；87 `un vote`→c“la décision ensemble”✓；88 `une commission`→d“le groupe qui prépare”✓；140 `un sénateur`→a✓；141 `un vainqueur`→b“le joueur qui a gagné le tournoi”✓；142 `un tirage`→c✓；143 `un vin primeur`→d✓；144 `un déchet`→e“ce qu'on jette”✓。
- 对话题：145“Tu as pris ___ ?”→`des billets`✓；146“—, ___ billets.”→`deux`✓；147“La séance est à ___ ?”→`quelle heure`✓（答“À 20 heures”）；148“On se retrouve ___ cinéma ?”→`devant le`✓；149“Bon ___ !”→`film`✓。
- 其余 123 题逐题核对表见 `key-stem-check.txt`（题干+键+注记全文）：单选、完形、判断、转换、比较级、改错、翻译（135–139 意→法逐句验）全部适配；抽查关键事实键与正文一致（Q7 A dimanche 8、Q42 13、Q46 C、Q64 B Dhont、Q79–84 投票数 115–1 / 458–0、Q109 A lundi、Q120 B irais）。
- 另：registry vs P8 extract **149/150**（仅 Q150 除外：registry 为长注记 `Domanda aperta — punti nel riquadro; …`，extract 为短键 `Domanda aperta`，为写作题固有形态）；registry vs core `final-fr-p8.json` 亦仅 Q150 不同（核心 `开放题` → it 读者语说明）。

## §3 门禁结果（独立复跑，15/15 PASS）

复跑工具：`gates.py`（builder 版的复刻；唯一改动：freeze_direct 改为 goals 侧副本重建，绝不在生产目录内重跑——proof1 前例；build 日志为本 scratch 的 `build-proof2.log`，实测 rc=0）。日志：`it/gates-proof2.log`、`it/gates-proof2.json`。

| # | 门 | 实测结果 |
|---|---|---|
| 1 | run | exit 0，零 overflow/wide/NOSPACE；TOTAL 150；A2 53 / B1 75 / B2 22；by page {1:10, 2:15, 3:18, 4:18, 5:17, 6:18, 7:12, 8:42} |
| 2 | occlusion | 0 flags，selftest OK（6 类 planted 全部触发，clean 对照静默） |
| 3 | p8_extract | keys 150/150，printed notes 121/150 |
| 4 | p8_compare | CLEAN，keydiff [150]（仅写作题键；137–139 翻译题键与核心逐字相同） |
| 5 | source_freeze | content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| 6 | string_freeze | 全部非 CJK 核心串每页存活；0 核心 E 残留；0 未入账 CJK；1 串豁免（翻译 E 值） |
| 7 | freeze_direct | goals 侧副本重建，SVG sha256 8/8 一致：`aa3ae078 f541b51c 52b4baf0 249b0d98 a91995f1 76cc6f87 12eb2907 64d1ba48` |
| 8 | text_layer | 印/网 pdftotext 逐字节一致（106,161 B）；网 1,696,726 B < 7 MB；印/网各 8 页 |
| 9 | p8_font | P8 最小字号 11.625 pt ≥ 9.75 pt |
| 10 | scans | U+2019=0，U+00B7=0，gold=0，旧纸色=0，`#fbfaf6` ×8 |
| 11 | chips | 134 枚 [10, 12, 18, 15, 14, 15, 12, 38] |
| 12 | keycheck | 150 键对 `core-fr/final-fr-p8.json`，仅 Q150 不同 |
| 13 | mcq | bodies 45，rendered lines 1478，0 缺陷 |
| 14 | widths | 31 单行串全部在预算内 |
| 15 | band_spans | 法标题止 1236.9，band_r1 起 1307.6（净空 70.7 px），法副标题止 837.2，band_r2 起 1481.2 |

另：`tools/freeze.py baseline --build core-fr --core-svg core-fr/svg` **8/8 byte-identical**（标准口径）；`freeze.py diff`：新增 CJK 仅 U+3000 ×10（p2 1 个、p8 9 个，均为意语串内结构分隔符），与 proof1 一致；`check_s11_it.py` **PASS**（36 项：纸色/色集与核心一致、无金色/旧纸色、VOL/徽章/P8 字号）；`verify_ed_it.py` **PASS**（24 项：D1/D2/D3/Q148/text.md 答案键全对——text.md 答案块解析出 150 键，与 registry 逐项一致，Q150 除外）。

## §4 creambox 全版扫描 + 溢出扫尾（spill sweep + 盒标题真墨）

- 规范版 creambox：exit 0；33 个奶油盒；7 处负 clearance **全部为已知假阳性**（盒内末行 clearance +47.7/+48.0/+48.5，负值行是下一栏目的粗体标题，位于盒底 +24/+37 px 处：`LE MOT DE LA SEMAINE`、`LA SEMAINE EN CHIFFRES`、`À VOUS !　TOCCA A TE!` ×3、`IL EST PRÉVU QUE + SUBJONCTIF`、`LE DÉBAT　DIBATTITO`）。
- spill sweep（自写 `spill_boxtitle.py`）：对每个奶油盒，查盒底 +60 px 内、盒 x 范围内、且**不在任何其他 rect 内**的整行——11 行命中，**全部为下一栏目的粗体标题**（`LE MOT DE LA SEMAINE`、`LA SEMAINE EN CHIFFRES`、`À VOUS !`、`POUR OU CONTRE ?`、`MICRO-DRILLS`、`LIRE LE CALENDRIER`、`IL EST PRÉVU QUE + SUBJONCTIF`、`LE DÉBAT`、练习号 `83.`），**正文续行溢出 0**。注：首版 sweep 曾因把整页纸底 rect 计入“其他 rect”而空转，已修正（排除 1950×2700 纸底）后重跑，结论为真阳性扫描（见 `spill-boxtitle-proof2.log`）。
- 盒标题真墨扫：33 盒的盒内首行粗体标题，逐一用 PIL 真墨（`svglib._pil`，按 run 取 `getbbox`）量墨宽/墨底 vs 盒内右沿/盒底——**溢出 0**（水平+垂直均无）。
- 纯填充无描边盒的溢出：奶油盒本身即无描边纯填充，以上三重扫描（baseline clearance + PIL 真墨 + 盒外行扫尾）均覆盖。

## §5 字体与 CJK（D5 只记录不判定）

- 8 SVG `<text>` 元素按 `font-family` 计数：`Noto Sans CJK SC` **690** 个、`Newsreader` 944 个、`Noto Serif CJK SC` 74 个（皆 U+3000 结构分隔 run，无中文内容）、`UnifrakturMaguntia` 1 个、`DejaVu Sans` 4 个（P7 诊所 `✗` 号）。
- 与 proof1 的 691 个相比少 1 个——删去的披露中句带走了一个 sans 元素，吻合。
- CJK：版内 SVG 全部 CJK 字符仅 U+3000（368 处，结构分隔符）；真实 CJK（中文）**0**；`text.md` CJK 0、U+2019 0、U+00B7 0。
- 拉丁讲解层落在 Noto Sans CJK SC 是已知全线待用户裁定的问题，本版不作缺陷、不修。

## §6 八字逐页目视（印刷 PDF 100 dpi + 300 dpi 重点）

渲染：`png/pg-1.png` … `png/pg-8.png`（100 dpi），`png/p7-courrier-bottom-300dpi.png`、`png/p5-wordlist-300dpi.png`、`png/p8-dialogue-300dpi.png`。
- P1：干净。导读条法标题与意语行净空 70.7 px；Atget 图、`LES DATES` 框、Q1–10 均正常。
- P2：干净。Nota 框、`LA SEMAINE EN CHIFFRES` 盒、`DIRE LA DATE` 表、22–25 配对块 + a/b/c/d 选项、Q11–25 均正常。
- P3：干净。ZOOM 框、DATES 表、`BEAUJOLAIS　IL QUIZ`、Q26–43 均正常；Q36/Q37 填空线独行（观察项，见 §2.5）。
- P4：干净。`LES MOTS DU TENNIS　PAROLE`、49–52 配对块、`LE DÉBAT` 盒、MICRO-DRILLS、Q44–61 均正常。
- P5：干净。除 D2/D3 已修复的两行外无问题（Méliès 图、电影词表其余 6 行、73–76 配对块、Q62–78 均正常）。
- P6：干净。`LE CALENDRIER` 表（标题 `CALENDARIO DEL BILANCIO (VOTO MERCOLEDÌ)` 无溢出）、比较级、MINIDRILL、85–88 配对块、Q79–96 均正常。
- P7：干净。披露框 2 行在盒内（见 §2.1）；Doré 图、`LA PHRASE EXEMPLE` 盒（3 处）、金句 Q97–104、诊所 Q105–108、`LA SEMAINE PROCHAINE` 黑底块均正常。
- P8：干净。H 写作框、`MODÈLE` 框、对话 G（148 已修）、答案流（含 `148. devant le`）、Hiroshige 图与图注均正常；无溢出。
- ABSTRACT.txt：意语一行，无 ASCII `"`，与 #1 备份逐字节相同，内容与本版一致。WEEKLY-KIT.md 在位，含 #2 记录与 `une actrice`。

### 目视所见、明确不判缺陷的继承项（均在 #1–#2 未变页上，proof1 已通过）

- P4 `LES PHRASES DU COMMENTATEUR` 盒内法语引文换行：`« C'est gagné` / `! » — Ha vinto!`——“!” 落行首。这是法语引文在盒宽内的正常断行（“!”与后文同属一个 `<text>` 元素，非孤儿标点元素），P4 与 #1 逐字节相同，非本次重建引入。
- P5 `LE CINÉMA DU MERCREDI` 盒内：行首为 `» (Francis Lawrence, 2 h 38), …`——同上，法语引文断行，P5 除词表两行外未变。
- P2 Nota 框：`les droits de l'enfant i` / `diritti dei bambini`——意语 `i diritti` 在行尾断开，单字母冠词 `i` 落行末；为 gloss 换行常态，非溢出、非孤儿。
- 以上三处均无 baseline/墨迹越界（creambox + spill sweep 已过），不构成缺陷，不修。

## 结论

**(a) 零缺陷，可定稿。** proof1 的 D1/D2/D3 全部修好且改动面封闭（仅 P5/P7/P8 的 6 行文本变）；15/15 机械门独立复跑全过；150 键逐项手核全部适配；孤儿标点新增 0；P7 披露框 PIL 真墨末行 2237.3、间隙零墨；印/网文本层逐字节一致；生产文件全程只读、SHA 未变。
