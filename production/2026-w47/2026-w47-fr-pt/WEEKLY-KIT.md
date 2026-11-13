# WEEKLY-KIT — Le Lucerna · 法语周报 VOL.4 · 葡萄牙语（pt）讲解版

- 目标语：法语（fr）；读者母语：葡萄牙语（pt）；期号 VOL.4，总第 4 期。
- 刊期：2026 年 11 月 16 日（周一）至 11 月 22 日（周日）；slug 周 `2026-w47`；frontmatter 周 `2026-W47`；weekStart `2026-11-16`，weekEnd `2026-11-22`。截稿：2026 年 11 月 10 日。
- 刊名：`Le Lucerna`。版式：8 版，1950×2700，4 栏，页脚配对标识每版可见，P1 配对徽章可见。
- 练习：150 道（P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42），分级 A2 53 · B1 75 · B2 22。级别徽章 134 枚（P1 10 · P2 12 · P3 18 · P4 15 · P5 14 · P6 15 · P7 12 · P8 38；150 题 − 16 道配对共享题）。P8 答案全部由登记表生成；印出注记 121/150（`tools/p8.py extract` 实测）。翻译题方向为“读者语言题干 → 法语键”（与核心版一致）。
- 词汇表：6 组 gloss（参议院/投票、儿童权利/新酒、采收/葡萄酒、网球、电影/二手、预算）+ 词表（葡萄酒、网球、电影）；金句 8 句，全部逐字出自本期 P1–P6 正文（核心版校验 8/8）；范文《Mon dimanche 22 novembre》96 词，在 80–100 词要求内。以上均与核心版相同；仅讲解层为葡萄牙语（pt）。
- 讲解层：`expl.py` 共 318 键：138 条复用 W46 葡萄牙语版、180 条本期新译（含 26 条因本期超长改写而由复用转为新译的注记）、14 条冻结法语键未动（`chart_sub`、`outils_intro`、`head_zoom` 等）。`note_wrap` 为 `half`（核心版为 `full`），译注前缀 `gloss_prefix` 为 `Nota — `（SOP §1.1：印刷层无 `·`，复用值中的 ` · ` 已归一为全角空格）。

## 一、内容

各版内容与核心版相同（P1 阿尔卡拉斯巴黎夺冠 + 参议院周三社保预算投票 + 博若莱新酒周四零点上市；P2 一周三段；P3 博若莱新酒 75 周年；P4 巴黎大师赛/都灵/蓝军；P5 周三电影 16 部新片 + 减废周；P6 参议院社保预算深读 + 自我更正；P7 精讲/金句/诊所/读者园地/VOL.5 预告；P8 综合评估）。事实来源与图片（6 张公共领域图）见核心版 KIT §三、§四，本版不再重复。

## 二、兑现 W46 承诺

与核心版 KIT §二相同：巴黎大师赛结果已兑现（阿尔卡拉斯 7-6(5), 7-5 胜谢尔顿，巴黎首冠）；预算投票自我更正（W46 预告的 11 月 3 日国民议会收入部分正式投票未发生，实际 11 月 4 日晚 458–0 否决）；博若莱新酒 11 月 19 日（周四）第 75 届；读者园地刊登标注明确的编辑部示例 + 法语说明 + 葡萄牙语说明（截至付印未收到 VOL.4 投稿，VOL.5 兑现点评真实投稿的承诺；投稿只认用户直接发来的，不查邮箱）。

## 三、构建与复现

构建目录：`production/2026-w47/2026-w47-fr-pt/`（由核心版 `core-fr` 复制 `*.py` + `assets/`，仅替换 `expl.py`；`content*.py`、`bslib4.py`、`svglib.py`、`run.py` 与核心版字节相同；`render.py` 仅改 BASE 路径与印刷 PDF 名）。构建与门禁解释器均为 `~/workspace/weekly-git/tools/venv/bin/python`（PIL 13.0.0；系统 python3 为 PIL 10.2.0，度量不同，禁用）。

复现：

```bash
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-fr-pt
~/workspace/weekly-git/tools/venv/bin/python run.py        # -> svg/*.svg
~/workspace/weekly-git/tools/venv/bin/python render.py      # -> cards/*.png + La-Lucerna-VOL4-fr-pt.pdf
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg La-Lucerna-VOL4-fr-pt-web.pdf
```

`.text.md` 由源稿导出器从 `content*.py` 源稿导出（非 PDF 反抽），见 scratch `export_lang.py`。

## 四、门禁输出（实测，2026-11-12，D5 重建 r2）

- `run.py` exit 0，零 `FLOW OVERFLOW` / `HEAD TOO WIDE`；TOTAL 150（按版 10/15/18/18/17/18/12/42；按级 A2 53 · B1 75 · B2 22）。终值：P6 深读 1288/1300、P6 练习 2527/2560、P8 答案流 2106/2560、P7 金句流 1778/1830。
- `tools/occlusion_audit.py`：**0 flags**（自检 OK：6 类阳性对照全部触发，干净对照静默）。
- `tools/p8.py extract --total 150`：键 150/150，印出注记 121/150。`p8.py compare`（对核心版 P8）：**CLEAN**，keydiff `[150]`（仅写作题键为读者语言说明，属预期）。
- 源码冻结：`content8.py`、`bslib4.py`、`run.py`、`content12.py` 与核心版字节相同；`svglib.py` 仅差 `_D5_READER` 一行（协调员落盘批复，见 §三）；`content34.py` 仅 1 行葡萄牙读者修复（`head_mots_tennis` 23→21）、`content56.py` 仅 2 行（`head_chart` 24→20、`head_lire` 25→23）、`content7.py` 仅 1 行（`head_outils` 27→25）；`render.py` 仅 BASE + PDF 名两处不同。
- 字符串冻结：核心版全部非 CJK 印刷字符串均在本版同页存活；核心版讲解层中文字符串 0 残留；1 条字符串因翻译豁免（P8 写作题干 `Traduisez : ` → 读者语译法）。
- 确定性：`run.py` 两次运行，8 个 SVG SHA-256 全同（D5 r2）：p1 `bb8ffdf8`、p2 `8b3d442f`、p3 `7ee87f1b`、p4 `ed6eff64`、p5 `84b27038`、p6 `23df0293`、p7 `9667cc32`、p8 `1da78777`（前 8 位；`freeze-r2.json`）。
- 印刷版 PDF：8 页，17,032,129 字节，SHA-256 `6aee0967dcfc9e21725948c38fe2bdfbbbb1671f68168a70d2c7e10b936883df`。
- 网页版 PDF（`tools/webpdf.py` 40963281 斜体修复版，命名 `-web.pdf`，fr 家庭惯例）：8 页，1,623,461 字节（< 7 MB），SHA-256 `88ece6e886a9c1f3802e0fc06a1b871c35c42136aa424d830fce06cd1a7edba8`；`pdftotext -layout` 提取印刷版/网页版各 101,013 字节、逐字节一致。
- `.text.md`：46,656 字节，SHA-256 `b61fe3b3189dbc323b2837389480f10a2a89547e278ce5936426f9f8e1c674f2`（与 §五同值）。
- P8 最小字号：11.62pt（PyMuPDF 实测，≥ 9.75pt 下限；D5 r2 重测，255 处此字号）。
- 扫描：U+2019 弯撇号 0、U+00B7 0、金色 #b49a4a 0、旧纸色 #f7f1e2 0、纸色 #fbfaf6 ×8。直撇号一律 U+0027。
- 徽章：134 枚（白字计数，P1 10 · P2 12 · P3 18 · P4 15 · P5 14 · P6 15 · P7 12 · P8 38）。
- 150 键复核（对 `core-fr/final-fr-p8.json`）：150 键逐项比对，仅 Q150 不同（写作题键为读者语言说明）；其余 149 键与核心版逐字相同；Q148 键为 `devant le`、题干为 `On se retrouve ___ cinéma ?`（核心 fix4 已修 `du`）。
- MCQ 完整性：45 个题体、1482 渲染行，0 缺陷、0 未定位。
- 单行宽度：31 条头条/框题/家具字符串全部在预算内；共行头条+副标 4 组联合检查全部通过（最大 1274.4/1757）。
- 奶油盒全版扫描（规范版 creambox.py）：P7 读者园地盒（y=1878，盒底 2258.0）末基线 2233.3，清除 +24.7；全版 BELOW-WINDOW 7 条，均为 +24.0/+37.0 下一栏目标题假阳性，无真溢出。
- 孤儿标点全扫：新增孤儿 0（核心既有 “—” 元素 0 处同位继承；字体分拆同基线标点 0 处，非视觉孤儿；zh-tw 另有 P4 残留 1 处，见 §五）。
- 孤行填空线（观察项，非缺陷）：Q130（P8）与 P3 Q36/Q37 三处均存在，与核心同位关系见本轮 FANOUT-REPORT-fr2.md。
- 8 版卡面目视（印刷版 PDF，100 dpi；改动页另行 200 dpi 裁切复核）：零问题。`.text.md` 全文通读：无中文残留、无错字，150 题答案注记逐条合理。

## 五、修正记录（重建 #2，2026-11-11）

- 重建原因：核心 core-fr 定稿 fix4（Q148 键 `devant`→`devant le`、题干删 `du`；P4 `chiffres_note` 删「决赛」二字去孤儿句号），#1 版由旧核心构建；本轮从 fix4 核心全量重建 10 个读者语版，#1 旧版已备份至 goals 侧 `hidden_files/w47/scratch-refanout-fr2/backup-old/`。
- 本版 proof1 遗留修复（重建时落地，wrap() 实测 + 门禁重验）：
- P7 读者园地奶油盒溢出修：`courrier_disclosure` 删中句 “esta edição publica um exemplo editorial marcado.”（该信息已由 P7 法文示例标注句覆盖），3 行→2 行；末基线 2260.6→2233.3、creambox 清除 -2.6→+24.7（desc-clear +18.8）；PIL 真墨实测：披露灰字末行墨至 svg y=2237.3，盒底 2258.0 之下 2258–2270 白纸间隙零墨（仅 P7 哈希变）。
- 核心 fix4 落地：Q148 键 `devant`→`devant le`、题干 `On se retrouve ___ du cinéma ?`→`On se retrouve ___ cinéma ?`（仅 P8 哈希变；P8 注记 148 亦随键变为 `devant le`）。
- 改动页（与 #1 版 SVG 哈希对比）：P7（ea3d710b→c3419d55）、P8（7d582103→34bf3311）；其余页与 #1 版字节相同。
- 核心三件（fix4，复核一致）：印 `La-Lucerna-VOL4.pdf` 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`；网 `La-Lucerna-VOL4-web.pdf` 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`；文 `2026-w47-fr-zh-cn.text.md` 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`。
- `.text.md`：46,656 字节，SHA-256 `b61fe3b3189dbc323b2837389480f10a2a89547e278ce5936426f9f8e1c674f2`，44,352 字符、542 条目、150 题（D5 r2 重出；见 §七。注意：`export47.py` 会把头两行写成 core-fr 简体中文头，重出后须恢复葡萄牙语头）。

## 五（续）、#1 构建史（2026-11-11，原文保留，见备份版 KIT）

## 五、修正记录

- 构建前诊断（`diag_reg.py` 复现答案流）：词干与核心版行数一致（1/1/2/1/1），答案流差 282px（上限 124px），为本家庭至今最长的一版（P1 +1 行、P2 +1 行、P3 +1 行、P4 +1 行、P5 +2 行、P6 +3 行、P8 +5 行）。批一缩短 54 处注记、26 条复用键转为新译（`n_comp4a`、`n_finale8`、`n_groupes`、`n_forfait`、`n_comp4b`、`n_comp4c`、`n_palais`、`n_comp6a`、`n_micro6b`、`n_micro6e`、`n_micro6a`、`n_comp6b`、`n_micro6c`、`n_micro6d`、`n_chart1`、`n_cloze6`、`n_read5`、`n_d4`、`n_d3`、`n_mcq_b5`、`n_d5`、`n_cloze4`、`n_cloze7`、`n_mcq_b6`、`n_mcq_b8`、`n_read4`；其中 Q70、Q41/Q30、Q6/Q10、Q32/Q40、Q145/Q77 等为两键/三键共用值，同步改写），差值 282px → 81px（P5 +1、P6 +1、P8 +2，均在上限内）。
- 构建前预扫（es/it 两版同一缺陷类）：`head_dieppe_ex` 440.8 > 422.5、`head_mots_fetes` 451.6 > 400.5、`head_mots_photo` 468.2 > 400.5，三处均在构建前改短（`BEAUJOLAIS　O QUIZ`、`LES MOTS DU VIN　O VINHO`、`MOTS DU CINÉMA　O CINEMA`）。`band_r1`（`ALCARAZ VENCE　SENADO VOTA QUARTA`）校正后预检模型起 x=1271.8，通过；`subtitle`（`SEMANÁRIO EM FRANCÊS　VOL.4　PARIS E O SENADO`）渲染宽 1558.4，起 x=195.8；`agenda_sub` 367.3 ≤ 378.5。
- run1：门禁 14/15。唯一实缺陷：`agenda_note` 400.4px > 378.5 预算（`Votação solene: quarta-feira 18 de novembro.`，19px 度量）。修复（run2）：`agenda_note` → `Votação solene: quarta 18 de novembro.`。run2 门禁 15/15。
- 诊断中断两次：第一次为 `/tmp` tmpfs 512MB 写满（姊妹家庭校对件占用，勿删他人文件），诊断工作目录由 `/tmp/diag-pt/` 移至 scratch 内 `diag-wd/pt/`；第二次为开发侧工具集变更通知打断正在跑的诊断命令，`pt/` 目录未建、`reg-pt.json` 未落盘，重建目录后重跑诊断，无损失。

- 独立重校补译注 fix1（2026-11-12）：P7 `head_clinic` 补 `CLINIQUE DES ERREURS　ERROS`（译注取自本版 `bridge_clinic`“错”的既有用词）。源头 `expl.py`；text.md 重出后与修前 diff 仅 1 行（L921）。门禁复核：occlusion 0、p8 CLEAN、boxtitle 0 DEFECT（36 titles）、spill 0、edge 0/0、census PASS、印/网文字层逐字节一致（99,282 字符）；零警告。三件 SHA：印 17,031,948 B `4a76ddaca94d…`、网 1,623,288 B `302da684a631…`、文 46,494 B `c7a3f3244476…`。详见 scratch-fix-fr/FIX-LOG.md。


## 六、沿用说明（非缺陷，记入此处）

- P3 `POUR OU CONTRE ?` 框无葡萄牙语行、P5 `debat5_note`（`Cinema ou casa? Uma peça de roupa velha encontra um novo dono, ou acaba no lixo?`）出现两次，均与核心版一致（核心版同）。
- P3 ZOOM 框内葡语行 `Venda antecipada desde 1951, terceira quinta-feira desde 1985, 75.º aniversário em 2026.` 与 P8 注记 Q26 `Venda antecipada em 1951` 用词不同：两者是不同 E 键（框内行为独立的 dates-box 注记），各按本位缩短，内容均正确，未统一。
- `head_lire` `LIRE LE CALENDRIER　HORÁRIO` 为 W46 葡萄牙语版复用值（W46 pt expl.py 第 68 行），沿用未改；`bridge_dieppe` `Minidrills　o quiz do Beaujolais.` 沿用 W46 pt 复数 `Minidrills` 用法（W46 pt expl.py 第 92 行 `Minidrills · o quiz de Dieppe.`，`·` 已归一为全角空格）。
- P8 答案注记中配对键的格式混用 `=` 与 ` = `（如 141 题 `vainqueur = vencedor　b` 与 140 题 `sénateur = senador　a`），为 W46 复用值与本期新译的格式差异，内容均正确，未统一。

## 七、D5 重建（2026-11-12，用户 B 档三周全修）

- 安装：`apply_variant.py --target fr --reader pt`（mode=latin），路由断言 20/20 PASS（含 fix2 三引号 → news）；`svglib.py` 与核心版仅差 `_D5_READER` 一行（协调员落盘批复 2026-11-12，见 §三）。
- r1 门禁：5 HEAD TOO WIDE（P6-ex `LIRE LE CALENDRIER　HORÁRIO`、P6-opinion 与 P7-B2 `IL EST PRÉVU QUE + SUBJONCTIF`、P6-micro `LE COMPARATIF EN POLITIQUE`、P7-outils `BOÎTE À OUTILS　UTENSÍLIOS`）、occlusion 3 flags（P1 头条 vs `ALCARAZ VENCE` 198.0×20.8px、P6 `CALENDÁRIO DO ORÇAMENTO (VOTO QUARTA-FEIRA)` LINEX 越框、P6 `LE COMPARATIF EN POLITIQUE` vs 该长标题 60.7×12.5px）、boxtitle/creambox 6 DEFECT（P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P4 `PALAVRAS` +27.3、P5 `CINEMA` +57.3、P6 `CALENDÁRIO DO ORÇAMENTO (VOTO QUARTA-FEIRA)` +88.7、P6 `TROIS DATES POUR COMPRENDRE` +24.5）；其余绿（文字层逐字节一致；p8 121/150 CLEAN，keydiff=[150] 与修前一致；freeze 8/8；spill 0；edge 0；census PASS）。观察项：creambox P8 slack 34.1→32.6（行数 196→196 不变，系 D5 重排后 P8 末行位置微移，非缺陷）。
- 修复 13 处（r1→r2）：与核心相同的 8 处原样同步（`head_zoom` 23→22、P4 框题 `tsize=21`、`head_cine` 23→20、语法头 25→23、`head_comp6` 25→24、P6 框题 `tsize=21`、P7 语法头 24→23、`head_clinic` 25→23——同步后 `content34.py`/`content56.py` 与核心版字节相同，`content7.py` 除 `head_outils` 外相同）；葡萄牙读者版特有 5 处（`text_w` 实测定量）：`band_r1` 删 `ALCARAZ VENCE　`（与正上方主头条重复；间隙约 −198→+87px）、`head_chart` `CALENDÁRIO DO ORÇAMENTO (VOTO QUARTA-FEIRA)`→`CALENDÁRIO`（第二段墨宽 703.0→176.3，24pt 下墨宽约 164 > 框内余量 141.8，故另降 24→20pt，墨宽约 137，与 de 的 `KALENDER` 同类处理）、`head_lire` 25→23（447.0→411.2 < CW 422.5）、`head_outils` 27→25（443.4→410.6）、`head_mots_tennis` 23→21（427.4→390.2；22pt 下墨宽约 380 仍擦边，故取 21）。
- r2 全套门禁（09:15–09:23 UTC）**全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE（`head_check.py` PASS）；render + webpdf 重渲；occlusion 0 flags；p8 121/150、CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；freeze baseline 8/8、diff vs 核心 +0 非分隔符 CJK（新增 CJK 全为 U+3000：vs 核心 12、vs 修前基线 1，系重排后折行分隔符存留数变化）；boxtitle 0 DEFECT（36 titles，289 body lines）；creambox PASS 0 defects；spill 0；edge 0；D5 census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；印/网文字层逐字节一致（各 100,788 字节）。印 PDF 17,031,944 字节 SHA-256 `8c01de5f…`、网 PDF 1,623,290 字节 SHA-256 `a62233ec…`（前 8 位；见 §四）。门禁日志：`hidden_files/w47/scratch-d5-rebuild-fr/2026-w47-fr-pt/logs-r2/`；工作日志：`hidden_files/w47/scratch-d5-fr/RUN-LOG.md`。

## fixfam1（2026-11-13，独立重校 A1/A2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-pt/logs-fixfam1/`）

- A1 P2 图注改写为城堡描述（`content12.py:184`）：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- A2 DIRE LA DATE 表补 ven. 20 与 sam. 21 两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`：Sexta-feira 20 de novembro　Dia das Crianças／Sábado 21 de novembro　Semifinais de Turim + começa a Semana anti-desperdício），行距 40→34、练习区块下移 36（`ey = dy + 356`）。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（36 titles）；creambox PASS 0 defects；spill 0（103 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 101,013 字节，99,502 字符，multiset 0）；text.md diff 仅 2 处（图注 1 行替换 + 日期表 8 行新增）；逐页 SVG 哈希比对：仅 p2-vie.svg 变，其余 7 页与修前字节相同（ru2/fix1 态为基准）。三件 SHA：印 17,032,129 B `6aee0967dcfc…`、网 1,623,461 B `88ece6e886a9…`、文 46,656 B `b61fe3b3189d…`。
