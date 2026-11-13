# PROOF-NOTE — W47 fr-en proof2（独立校对，re-fanout #2 重建版）

- 版：`production/2026-w47/2026-w47-fr-en/`（法语目标、英语读者版，VOL.4）
- 校对员：独立校对 proof1（与重建者不同人）；只读生产文件，未改任何生产文件，未 commit/push。生产目录零写入；core-fr 只读（freeze 基线守卫复核核心 SVG 未变）。
- 日期：2026-11-11；工作目录：`hidden_files/w47/scratch-proof-fr-en2/`（专用，不与他 agent 共用）
- 构建/门禁解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 用自家 scratch/tmp（/tmp 只有 512M，未用）
- 探针：`echo test | git hash-object -w --stdin` 在 repo 内成功（`9daeafb9…`，rc=0）

## 结论：(a) 零缺陷，可定稿

全部机械门禁独立重跑通过（见 GATE-LOG.md），150 题逐题手验无错键，8 版逐版目视零问题。
#1 proof1 的唯一缺陷 D1（Q64 注记 `Dont`）已修复落地（见下「改动封闭性」），
Q148 核心 fix4 已落地，P7 披露框复测干净。

## 身份核对（磁盘实测，先于开工；三项全符预期）

| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `La-Lucerna-VOL4-fr-en.pdf`（印） | 17,418,996 | `7210b3e23c97ef4f683bf695ecc7484bc97fda5cf522abb94fb16ce17f675414` | 吻合 |
| `La-Lucerna-VOL4-fr-en-web.pdf`（网） | 1,700,436 | `ca7f8ae3a76fdbb70f8af1724f92bdb6269f8bbc48b41348457e3d6ddbf551a2` | 吻合 |
| `2026-w47-fr-en.text.md`（文） | 46,191 | `7b658ae24f265d145455798c39f158d504b39e8034022a06b1c809c8bd7a5c4c` | 吻合 |

## 改动封闭性（本次实测，非转述 KIT）

与 #1 备份（`scratch-refanout-fr2/backup-old/2026-w47-fr-en/svg/`）逐页 SHA 对比：

| 页 | #2 | #1 | 结论 |
|---|---|---|---|
| P1 | `d832422e` | `d832422e` | 相同 |
| P2 | `f200006f` | `f200006f` | 相同 |
| P3 | `4867f169` | `4867f169` | 相同 |
| P4 | `14690fda` | `14690fda` | 相同 |
| P5 | `8d7d907b` | `8d7d907b` | 相同 |
| P6 | `087ab1a5` | `087ab1a5` | 相同 |
| P7 | `5476d2d0` | `5476d2d0` | 相同 |
| P8 | `e027cc89` | `f310354a` | 仅 P8 变（Dhont 修 + Q148 核心 fix4 落地） |

## 缺陷清单

无。零缺陷。

## 观察项（记录，不判 (b)，不擅自修）

### O-D5 — 讲解层拉丁字符落在 Noto Sans CJK SC（已知全周级待定项，只记录不判）

- 实测：8 页 SVG 中 `font-family="Noto Sans CJK SC"` 的 `<text>` 共 692 处（P1 76 / P2 70 / P3 75 / P4 61 / P5 62 / P6 72 / P7 77 / P8 199）；`Newsreader` 945 处，`Noto Serif CJK SC` 74 处，`DejaVu Sans` 4 处，`UnifrakturMaguntia` 1 处。与 #1 计数分毫不差。
- 印刷 PDF 嵌入字体含多份 `NotoSansCJKsc-Regular/Bold` 子集（cid），证实该字体实际用于拉丁文字。
- SOP §1.1 字体表：讲解层拉丁读者语言用 Newsreader，并明文「不用思源宋体自带的拉丁字形排西文」。本版讲解层英文用 Noto Sans CJK SC，与该条不符。
- 按简报要求：如实记录，不因此单方面判 (b)，不擅自修；待用户定夺 scope。

### O-T1 — P1「DANS CE NUMÉRO　IN THIS ISSUE」盒标题右侧余量仅 1.0px（全版最紧，非缺陷）

- 实测（`boxtitle_overflow.py`，PIL 真墨，含 letter-spacing）：盒 `x=1439.5 y=1280.0 w=422.5`（右缘 1862.0），标题字号 24，真墨 `1461.5–1861.0`，右侧余量 **+1.0px**，左侧余量 +22.0px。27 个盒标题中最小值，其余均 ≥17.2px。
- 300 dpi 裁切渲染复核（`crop-p1-danscenumero.png`）+ 像素级量测：奶油盒右缘在 svg x=1862.0，标题带最右深色像素在 svg x=1860.4——末字母 E 完整印出，未被裁切，墨未越过可见边。
- 与 #1 备份同标题同余量，**无回归**。按简报缺陷定义（字形被裁 / 墨越过可见边 / 相对首轮备份回归），三项皆无，故不判缺陷，仅记录。

### O-Q130 — 孤行填空线三处（核心继承的观察项，不修版、不动已定稿核心）

- Q130（P8）：填空行 `___` 在 `(989.0, 843.0)`，与核心分毫不差。
- P3 Q36/Q37：填空行 x=538.5，y=1924.1 / 2056.8，相对核心（1864.7 / 1997.4）下移 **+59.5**（读者语练习流排版所致，与 #1 核查分毫不差，分三档中的一档：en/es/pt/nl +59.5；de/it/ru +30；ja/ko/zh-tw +0）。
- 目视：三处均为填空题的独立填空行，阅读无碍。

### O-VOL5 — P6 `chart_note` 的 VOL.5 显化（已裁定，非缺陷）

- `check_s11_fr` 初跑曾报 `p6-politique.svg: VOL.5 count core=0 ed=1`。核查：核心 `expl.py:129` 的 `chart_note` 为「本页日程为计划安排，18 日投票结果下期跟进。」；本版 `expl.py:128` 译为 "Planned programme only; the 18 Nov vote follows in VOL.5."——「下期」译作明确的 VOL.5，事实正确（下期即 VOL.5），属同一注记的读者语译法，非新增内容。其余各页 VOL.4/VOL.5 计数与核心全等，色集全等，徽章矩形全等。此项记为已裁定的检查适配，不判缺陷。

### O-BOX — P4「LES CHIFFRES DU SPORT」盒下半留白（核心同版式，非缺陷）

- 该奶油盒 `y=200 h=470`（底 670.0），末行基线 550.5，盒内下方约 120px 留白。`content*.py` 与核心字节相同，版式为核心原设计，非本版引入。

### O-SERD — P1 日历「sam. 21　Turin : demies　SERD」缩写未展开（核心原文，非缺陷）

- SERD = Semaine européenne de la réduction des déchets，P2 正文已展开全称；P1 用缩写为核心原文，冻结一致。

## 已裁定为非缺陷（实测证据）

- **D1 已修复**：P8 答案区 `64. B (Les Braves by Dhont)`——印刷/网页 PDF 文字层中 `Dhont` 各 4 处，`<text>` 元素中 `Dont`（不含 Dhont）0 处；P5 正文与 Q64 选项 B 均为 Lukas Dhont。200 dpi 目视：P8 答案区该行清晰。
- **Q148 落地**：五重核对全通——登记表 `reg-ed.json` 键 `devant le`；`content8.py` 含 `"devant le"` 与 `On se retrouve ({gnums[3]})___ cinéma ?`；P8 SVG 题干 `(148)___ cinéma ?`、答案 `148. devant le`；`p8.py extract` 提取键 148 = `devant le`；`.text.md` G 节题干 + 答案区 `148. devant le`。全版 `<text>` 中唯一的 `du cinéma` 是 P5 Méliès 图注「le premier grand trucage du cinéma」，与核心逐字相同，与 Q148 无关。
- **P7 披露框**：末基线 2233.3、creambox +24.7；PIL 真墨：末行 `…labelled editorial example; VOL.5 will honour the promise to comment on real submissions.` 真墨底 2237.8（距盒底 2258.0 有 20.2px），2258–2270 间隙零墨。目视：两行完整在奶油盒内，下方白纸间隙干净。
- **P1 Atget 照片白色小方块**：源照片本身内容（#1 已核实：嵌入图 xref 7 内同一白方块），P1 与 #1 字节相同。
- **P2 ET VOUS 盒末行 `in.`**：末基线 1332.6，盒底 1337.6，清除 +5.0；150 dpi 全页目视 `in.` 整行在奶油盒内，盒底边在其下清晰可见。
- **creambox BELOW-WINDOW 7 条**：全部为下一栏目标题假阳性（+24.0 `LE MOT DE LA SEMAINE` 1 处；+37.0 `LA SEMAINE EN CHIFFRES` / `À VOUS !　YOUR TURN` ×3 / `IL EST PRÉVU QUE + SUBJONCTIF` / `LE DÉBAT　DEBATE` 等）；33 盒 inside-only 清除全为正，最小 +5.0（即上条 P2 盒）。
- **`三色蛾`（3 个汉字在 SVG 内）**：仅 P1 一处，在蛾标矢量图的 `<title>Lucerna 三色蛾</title>` 内（无障碍标题，非渲染文字）；印刷/网页 PDF 文字层中为 0 次；核心版同文。非中文残留。
- **freeze diff 新增 CJK 仅 U+3000 ×9**（P6 1、P7 1、P8 7）：全角空格分隔符，非汉字；无新增汉字。
- **`vote=vote` 式注记（Q22、Q87）**：法语 `vote` 的英文即 `vote`，译法正确、仅简略，非错误。
- **Q120 徽章**：P8 `120.`（610.5, 332.0）旁有 B2 色 `#37402f` 徽章矩形，`check_s11_fr` 核实 OK。

## 机械门禁（独立重跑，见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| run.py（scratch 副本） | rc=0，TOTAL 150，0 溢出；重建 SVG 与现盘 8/8 字节一致 |
| freeze baseline（--build core-fr，--core-svg core-fr/svg） | **8/8 SVG 字节一致**，核心 SVG 未被改动 |
| freeze diff | 8 页；新增 CJK 仅 U+3000 ×9；无新增汉字 |
| occlusion_audit.py（真实审计，--core core-fr） | 0 flags，selftest OK；NEW vs core 0 |
| p8 extract --total 150 | keys 150/150，printed notes 121/150 |
| p8 compare vs core（直读 p8compare-proof2.json 本体） | CLEAN，keydiff [150]（gates.json 式 "?" 误读不适用） |
| source_freeze | PASS：content/bslib/svglib/run 与核心字节相同；render.py 仅 BASE+PDF 名不同 |
| string_freeze | PASS：核心非 CJK 串全存活；0 核心 E 残留；0 未入账 CJK；1 条豁免（翻译 E 值） |
| text_layer（印/网逐页 token 差） | PASS：8 页逐页 token 差 0，合计 105,574 B；网 1,700,436 B < 7MB |
| p8_font | PASS：P8 最小字号 11.625pt ≥ 10pt（简报阈值；亦 ≥ 9.75pt） |
| check_s11_fr（fr 适配版，自家 scratch 新写；en 原版未动） | PASS：纸色/色集/VOL 计数/徽章矩形/色集全等；P8 最小 SVG 字号 15.5；cloze (109)–(116)/(145)–(149)、Q120 B2 徽章、ÉCRITURE 头、Q148 全在；P6 VOL.5 一处已裁定（O-VOL5） |
| scans | PASS：U+2019=0，U+00B7=0，gold=0，旧纸=0，#fbfaf6 ×8；« » 74/74 成对；text.md 汉字 0 |
| chips | PASS：134 [10, 12, 18, 15, 14, 15, 12, 38] |
| keycheck vs core final-fr-p8.json | PASS：仅 Q150 不同（写作题键） |
| check_mcq.py | PASS：0 defects（bodies 45，rendered lines 1481） |
| widths（svglib.text_w，31 串 + 4 组共行） | PASS：全部在预算内 |
| band_spans（印刷版 PDF span 实测） | PASS：法文标题止 1236.9，band_r1 起 1252.1（净空 15.2px），法文副标题止 837.2，band_r2 起 1467.1 |
| creambox.py 全版扫描 | 33 盒，inside-only 全正（最小 +5.0）；P7 披露盒最小 desc-clear +18.8 |
| boxtitle 真墨（PIL，27 标题；本轮自写） | PASS：0 越边；最小右侧余量 1.0px（O-T1，已裁切复核）；与 #1 备份 0 回归 |
| overflow 横扫（本轮自写，绘图顺序版） | PASS：盒内横向溢出 0；基线在盒外的漏检行 0 |
| orphan sweep（check_extra2.py） | PASS：新增孤儿 0（全版孤儿元素 0；核心继承 "—" 2 处在本版因折行不同未分拆出）；检测器灵敏度已验：植入的隔离孤儿 。被判为 new |
| Q148 / Q130 / Q36/Q37 | PASS：见上文 |

## 目视（印刷版 PDF 150 dpi 全 8 页 + 网页版 P8 100 dpi + P1 盒标题 300 dpi 裁切）

- P1：干净。band 无重叠（band_r1 起 1252.1）；Atget 照已核实；DANS CE NUMÉRO 标题 E 完整；QUIZ ÉCLAIR Q7–10 四栏齐整；页脚 Page 1 of 8。
- P2：干净。ET VOUS 盒末行 `in.` 在盒内；DIRE LA DATE 表、EXERCICES Q11–21 齐整。
- P3：干净。NOTE 盒、ZOOM 盒、DATES 表、POUR OU CONTRE、LES MOTS DU VIN 齐整；Q26–43 齐整；Q36/Q37 填空行独立成行，阅读无碍。
- P4：干净。LES CHIFFRES、LES MOTS DU TENNIS、MICRO-DRILLS Q56–61、两处 LE DÉBAT 齐整；Q44–55 齐整。
- P5：干净。Méliès 图、REGARDER UN FILM、OÙ SORTIR、MOTS DU CINÉMA、LE CINÉMA DU MERCREDI 齐整；Q62–78 齐整。Q64 题干内 `Lukas Dhont` 拼写正确。
- P6：干净。LE CALENDRIER 表 7 行、LIRE LE CALENDRIER、LES PHRASES DES JOURNAUX、IL EST PRÉVU QUE、LE COMPARATIF、MICRO-DRILLS 齐整；P6 译注框为单 `NOTE`（无 `NOTE NOTE` 残留）；Q79–96 齐整。
- P7：干净。四栏 A2/B1/B2/TOOLBOX、Doré 图、LES PHRASES Q97–104、CLINIQUE Q105–108、读者来信、VOL.5 预告盒齐整；披露框两行完整在盒内。
- P8：干净。A–H 各节、MODÈLE 范文、Hiroshige 图、RÉPONSES 全 150 条齐整；`(148)___ cinéma ?` 无 `du`；`64. B (Les Braves by Dhont)` 拼写正确；`148. devant le` 正确。
- 网页版 P8 与印刷版同版式同内容（文字层逐页 token 差 0 已另验）。

## 150 题逐题手验

- 键表：p8.py extract 150/150；与核心 `final-fr-p8.json` 逐键比对，仅 Q150 不同（`开放题`→`Open question` 写作题键，预期内）。
- 键 vs text.md P8 答案区：150/150 一致。
- 逐题核对题干与答案：Q1–Q149 逐题对照正文/题干核实，无错键、无与正文矛盾的答案。核查要点：
  - 日期星期与题干一致：`date` 实测 2026-11-16 星期一至 11-22 星期日；Q109 `lundi 16`、Q48 键 A `vendredi 20`（P4 正文「11e journée se jouera du 20 au 22 novembre」）、Q84 `26 nov.`（50 天期限：10 月 7 日 + 50 天 = 11 月 26 日）、P7 预告「Vendredi 27 novembre : Black Friday」（2026-11-27 为星期五）均一致。
  - 数字：Q5 `12,7`（21,8→12,7）、Q38 `75 ans`（1951→2026）、Q42 `13`（8 月 13 日开摘）、Q80 `458–0` vs Q79 `115–1` 两处投票数不混淆、Q60 Bordeaux / Q61 Milan 主客场不颠倒。
  - 语法：Q107/Q134 虚拟式 `examine`（无 -s）、Q114 `aimé`（avoir 无配合）、Q115 `jouent`（Les Bleus 复数）、Q120 `irais`（si + 未完成过去时 → 条件式）、Q131 `venais`、Q103 `rejetée`（阴性配合）。
  - 翻译题 Q135–139（读者语→法语）：键分别为 `Regarder une finale, c'est déjà apprendre le français.` / `Il court plus vite que son frère.` / `Nous suivons le vote du Sénat depuis lundi.` / `Ce soir, nous allons préparer nos affaires.` / `On ne connaît pas encore les résultats.`，均与题干配对正确。
  - 配对题 Q22–25 / Q49–52 / Q73–76 / Q85–88 / Q140–144：左右项逐一核对，无串位。
- text.md 全文通读 1,088 行（44,136 字符）：无中文残留（汉字 0），无 U+2019/U+00B7，« » 74/74 成对；人名拼写与法文原文一致（Dhont、Ménochet、Fils、Lawrence、Smia、Meddour、Scott Thomas、Guiz、Méliès、Doré、Hiroshige、Atget、Moreau）。
- 8 句金句逐字出自本期 P1–P6 正文（抽查 8/8 与正文逐字一致）；范文《Mon dimanche 22 novembre》96 词，在 80–100 词要求内。
- 150 题计数：P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42；分级 A2 53 · B1 75 · B2 22。

## 其他核实

- ABSTRACT.txt：英文一行（Alcaraz / Senate / Beaujolais 梗概，150 题，A2–B2，16–22 November 2026）。
- 网 PDF 铁律：未重渲网 PDF（只比文字层）；生产网 PDF 未被覆盖。生产目录零写入（`git status` 无修改项；freeze 基线守卫复核核心 SVG 未变）。
- 字体审计（D5，只记录）：见 O-D5。
