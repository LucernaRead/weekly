# WEEKLY-KIT — Le Lucerna · 法语周报 VOL.4 · 英语（en）讲解版

- 目标语：法语（fr）；读者母语：英语（en）；期号 VOL.4，总第 4 期。
- 刊期：2026 年 11 月 16 日（周一）至 11 月 22 日（周日）；slug 周 `2026-w47`；frontmatter 周 `2026-W47`；weekStart `2026-11-16`，weekEnd `2026-11-22`。截稿：2026 年 11 月 10 日。
- 刊名：`Le Lucerna`。版式：8 版，1950×2700，4 栏，页脚配对标识每版可见，P1 配对徽章可见。
- 练习：150 道（P1 10 · P2 15 · P3 18 · P4 18 · P5 17 · P6 18 · P7 12 · P8 42），分级 A2 53 · B1 75 · B2 22。级别徽章 134 枚（P1 10 · P2 12 · P3 18 · P4 15 · P5 14 · P6 15 · P7 12 · P8 38；150 题 − 16 道配对共享题）。P8 答案全部由登记表生成；印出注记 121/150（`tools/p8.py extract` 实测）。翻译题方向为“读者语言题干 → 法语键”（与核心版一致）。
- 词汇表：6 组 gloss（参议院/投票、儿童权利/新酒、采收/葡萄酒、网球、电影/二手、预算）+ 词表（葡萄酒、网球、电影）；金句 8 句，全部逐字出自本期 P1–P6 正文（核心版校验 8/8）；范文《Mon dimanche 22 novembre》96 词，在 80–100 词要求内。以上均与核心版相同；仅讲解层为英语（en）。
- 讲解层：`expl.py` 共 318 键：164 条复用 W46 英语版、154 条本期新译、14 条冻结法语键未动（`chart_sub`、`outils_intro`、`head_zoom` 等）。`note_wrap` 为 `half`（核心版为 `full`），译注前缀 `gloss_prefix` 为 `NOTE　`（全角空格，SOP §1.1：印刷层无 `·`）。

## 一、内容

各版内容与核心版相同（P1 阿尔卡拉斯巴黎夺冠 + 参议院周三社保预算投票 + 博若莱新酒周四零点上市；P2 一周三段；P3 博若莱新酒 75 周年；P4 巴黎大师赛/都灵/蓝军；P5 周三电影 16 部新片 + 减废周；P6 参议院社保预算深读 + 自我更正；P7 精讲/金句/诊所/读者园地/VOL.5 预告；P8 综合评估）。事实来源与图片（6 张公共领域图）见核心版 KIT §三、§四，本版不再重复。

## 二、兑现 W46 承诺

与核心版 KIT §二相同：巴黎大师赛结果已兑现（阿尔卡拉斯 7-6(5), 7-5 胜谢尔顿，巴黎首冠）；预算投票自我更正（W46 预告的 11 月 3 日国民议会收入部分正式投票未发生，实际 11 月 4 日晚 458–0 否决）；博若莱新酒 11 月 19 日（周四）第 75 届；读者园地刊登标注明确的编辑部示例 + 法语说明 + 英语说明（截至付印未收到 VOL.4 投稿，VOL.5 兑现点评真实投稿的承诺；投稿只认用户直接发来的，不查邮箱）。

## 三、构建与复现

构建目录：`production/2026-w47/2026-w47-fr-en/`（由核心版 `core-fr` 复制 `*.py` + `assets/`，仅替换 `expl.py`；`content*.py`、`bslib4.py`、`run.py` 与核心版字节相同，D5 后例外见下；`render.py` 仅改 BASE 路径与印刷 PDF 名）。构建与门禁解释器均为 `~/workspace/weekly-git/tools/venv/bin/python`（PIL 13.0.0；系统 python3 为 PIL 10.2.0，度量不同，禁用）。D5 后与核心版的差异（协调员落盘批复 2026-11-12：`svglib.py` 仅差 `_D5_READER` 一行，其余字节一致）：`svglib.py` 仅 `_D5_READER = "latin"`（核心为 `"cjk"`）一行不同；`content12.py` 1 行（`sommaire_title` 24→21，en 读者修复）、`content34.py` 2 行（`head_dieppe_ex` 25→23、`head_mots_fetes` 23→21）、`content56.py` 1 行（`head_mots_photo` 23→21）、`content7.py` 1 行（`head_clinic` 23→22，r2 后补修）；其余 `content*.py`、`bslib4.py`、`run.py` 与核心版字节相同。8 处核心修复（`head_zoom`/`head_cine`/语法头/`head_comp6`/两框题 `tsize=21`）已原样同步，见 §七。

复现：

```bash
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-fr-en
~/workspace/weekly-git/tools/venv/bin/python run.py        # -> svg/*.svg
~/workspace/weekly-git/tools/venv/bin/python render.py      # -> cards/*.png + La-Lucerna-VOL4-fr-en.pdf
~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg La-Lucerna-VOL4-fr-en-web.pdf
```

`.text.md` 由源稿导出器从 `content*.py` 源稿导出（非 PDF 反抽），见 scratch `export_lang.py`。

## 四、门禁输出（实测，2026-11-12 D5 重建 r3 全绿；2026-11-11 #2 值见 §五）

- `run.py` exit 0，零 `FLOW OVERFLOW` / `HEAD TOO WIDE`（`tools/head_check.py` PASS）；TOTAL 150（按版 10/15/18/18/17/18/12/42；按级 A2 53 · B1 75 · B2 22）。终值：P6 深读 1258/1300、P6 练习 2527/2560、P8 答案流 2146/2560、P7 金句流 1778/1830。
- `tools/occlusion_audit.py`：**0 flags**（自检 OK：6 类阳性对照全部触发，干净对照静默）。
- `tools/p8.py extract --total 150`：键 150/150，印出注记 121/150。`p8.py compare`（对核心版 P8）：**CLEAN**，keydiff `[150]`（仅写作题键为读者语言说明，属预期）。
- 源码冻结：`content8.py`、`bslib4.py`、`run.py` 与核心版字节相同；`svglib.py` 仅差 `_D5_READER` 一行（协调员落盘批复，见 §三）；`content12.py`/`content34.py`/`content56.py`/`content7.py` 各有 1–2 行 en 读者修复（见 §三、§七）；`render.py` 仅 BASE + PDF 名两处不同。
- 字符串冻结：核心版全部非 CJK 印刷字符串均在本版同页存活；核心版讲解层中文字符串 0 残留；1 条字符串因翻译豁免（P8 写作题干 `Traduisez : ` → 读者语译法）。
- 确定性：`run.py` 两次运行，8 个 SVG SHA-256 全同（D5 r3）：p1 `62b4b174`、p2 `b18e2801`、p3 `0a722c78`、p4 `cf8c9d8b`、p5 `60dd199a`、p6 `43c36a0f`、p7 `9a4dffd3`、p8 `e4a16d38`（前 8 位；`freeze-r3.json`）。
- 印刷版 PDF：8 页，17,031,843 字节，SHA-256 `8ffde4f87863b0a027b662e13f89375f2dd399bdc7dd4b1deed35c5e6008f674`。
- 网页版 PDF（`tools/webpdf.py` 40963281 斜体修复版，命名 `-web.pdf`，fr 家庭惯例）：8 页，1,623,186 字节（< 7 MB），SHA-256 `271926332039bd32fec073a891d363864dff14bda76acd57e95c026596944a54`；`pdftotext -layout` 提取印刷版/网页版各 101,484 字节、逐字节一致。
- `.text.md`：46,280 字节，SHA-256 `4029e89a87ecb4a7e8e010fecfb20fb39645c319d72eb8001fbd6bb1c51dbf9e`（与 §五同值）。
- P8 最小字号：11.62pt（PyMuPDF 实测，≥ 9.75pt 下限；D5 r3 重测，514 个 span，260 处此字号）。
- 扫描：U+2019 弯撇号 0、U+00B7 0、金色 #b49a4a 0、旧纸色 #f7f1e2 0、纸色 #fbfaf6 ×8。直撇号一律 U+0027。
- 徽章：134 枚（白字计数，P1 10 · P2 12 · P3 18 · P4 15 · P5 14 · P6 15 · P7 12 · P8 38）。
- 150 键复核（对 `core-fr/final-fr-p8.json`）：150 键逐项比对，仅 Q150 不同（写作题键为读者语言说明）；其余 149 键与核心版逐字相同；Q148 键为 `devant le`、题干为 `On se retrouve ___ cinéma ?`（核心 fix4 已修 `du`）。
- MCQ 完整性：45 个题体、1481 渲染行，0 缺陷、0 未定位。
- 单行宽度：31 条头条/框题/家具字符串全部在预算内；共行头条+副标 4 组联合检查全部通过（最大 1734.8/1757）。
- 奶油盒全版扫描（规范版 creambox.py）：P7 读者园地盒（y=1878，盒底 2258.0）末基线 2233.3，清除 +24.7；全版 BELOW-WINDOW 7 条，均为 +24.0/+37.0 下一栏目标题假阳性，无真溢出。
- 孤儿标点全扫：新增孤儿 0（核心既有 “—” 元素 0 处同位继承；字体分拆同基线标点 0 处，非视觉孤儿；zh-tw 另有 P4 残留 1 处，见 §五）。
- 孤行填空线（观察项，非缺陷）：Q130（P8）与 P3 Q36/Q37 三处均存在，与核心同位关系见本轮 FANOUT-REPORT-fr2.md。
- 8 版卡面目视（印刷版 PDF，100 dpi；改动页另行 200 dpi 裁切复核）：零问题。`.text.md` 全文通读：无中文残留、无错字，150 题答案注记逐条合理。

## 五、修正记录（重建 #2，2026-11-11）

- 重建原因：核心 core-fr 定稿 fix4（Q148 键 `devant`→`devant le`、题干删 `du`；P4 `chiffres_note` 删「决赛」二字去孤儿句号），#1 版由旧核心构建；本轮从 fix4 核心全量重建 10 个读者语版，#1 旧版已备份至 goals 侧 `hidden_files/w47/scratch-refanout-fr2/backup-old/`。
- 本版 proof1 遗留修复（重建时落地，wrap() 实测 + 门禁重验）：
- P8 Q64 注记人名拼错修：`n_photo3` “Les Braves by Dont”→“Les Braves by Dhont”（P5 正文与 Q64 选项 B 均为 Lukas Dhont；仅 P8 哈希变）。
- 核心 fix4 落地：Q148 键 `devant`→`devant le`、题干 `On se retrouve ___ du cinéma ?`→`On se retrouve ___ cinéma ?`（仅 P8 哈希变；P8 注记 148 亦随键变为 `devant le`）。
- P7 披露框：en 版披露段原先即 2 行、末基线 2233.3、清除 +24.7，重建后 creambox 重测仍干净（末行 `…labelled editorial example; VOL.5 will honou…`）。
- 改动页（与 #1 版 SVG 哈希对比）：P8（f310354a→e027cc89）；其余页与 #1 版字节相同。
- 核心三件（fix4，复核一致）：印 `La-Lucerna-VOL4.pdf` 30,446,975 B `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d`；网 `La-Lucerna-VOL4-web.pdf` 2,241,835 B `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141`；文 `2026-w47-fr-zh-cn.text.md` 46,471 B `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df`。
- `.text.md`：46,280 字节，SHA-256 `4029e89a87ecb4a7e8e010fecfb20fb39645c319d72eb8001fbd6bb1c51dbf9e`，44,226 字符、542 条目、150 题（D5 r3 重出；见 §七。注意：`export47.py` 会把头两行写成 core-fr 简体中文头，重出后须恢复英文头）。

## 五（续）、#1 构建史（2026-11-11，原文保留，见备份版 KIT）

## 五、修正记录

- run1：P6 深读 `FLOW OVERFLOW`（en 版 g6 译注 6 行，余量不足）→ g6 缩短至 5 行（`un projet de loi a bill … paritaire joint.`）。
- run2→run3：门禁 occlusion 报 P1 导读条英文行与法文标题重叠（TEXTX，78.7×20.8px）→ `band_r1` 由 `ALCARAZ CHAMPION　SENATE VOTES WEDNESDAY` 缩短为 `ALCARAZ CHAMPION　SENATE VOTES WED`（实测起 x=1294.7，法文标题止于 1244.98，净空约 50px）。同轮修 3 个门禁脚本缺陷：chips 改数白字（ band/strip 矩形与徽章同色，旧法误计）、string_freeze 改归一化子串比对（P3 词表法语词干在英文版中为更长词串的前缀）、source_freeze 接受 `core-fr` 行（`render.py` BASE 用 `~` 路径）。
- run3→run4：目视发现 P6 译注框印 `NOTE NOTE`（g6 值误含 `NOTE　` 前缀，渲染器另加 `gloss_prefix`）→ 删去 g6 值首的 `NOTE　`，重建后单 `NOTE`，P6 哈希变为 `087ab1a5`，其余 7 页不变。
- 偶发事件：2026-11-11 07:52 写盘一度报 `Disk quota exceeded`（磁盘 45G 空闲，瞬时配额故障；07:53 探针写成功，磁盘恢复，无数据丢失；gates run3 因此中断后重跑）。


## 六、沿用说明（非缺陷，记入此处）

- 刊头标语 `READ THE FRENCH THE FRENCH READ`（`strapline_mid`）为 W46 英语版复用值，未动。
- 写作题答案注记 `Marked on the points`（`writing_note`）为 W46 复用值，未动。
- P8 答案注记中配对键的格式混用 `=` 与 ` = `（如 22 题 `vote=vote a` 与 87 题 `vote = vote　c`），为 W46 复用值与本期新译的格式差异，内容均正确，未统一。

## 七、D5 重建（2026-11-12，用户 B 档三周全修）

- 安装：`apply_variant.py --target fr --reader en`（mode=latin），路由断言 20/20 PASS（含 fix2 三引号 → news）；`svglib.py` 与核心版仅差 `_D5_READER` 一行（协调员落盘批复 2026-11-12，见 §三）。
- r1 门禁（07:48–07:53 UTC）：6 HEAD TOO WIDE、occlusion 3 TEXTX（P1 头条 vs `ALCARAZ CHAMPION` 222.2×20.8px、P6 `TIMETABLE` vs `B1`、P7 金句头 vs 副标 86.3×18.2）、boxtitle/creambox 7 DEFECT（P1 `IN THIS ISSUE` +45.9、P3 `WINE WORDS` +12.9、P3 `LES DATES EN CHIFFRES` +7.6、P4 `LES PHRASES DU COMMENTATEUR` +36.5、P5 `FILM WORDS` +15.7、P5 `FILMS` +31.3、P6 `TROIS DATES POUR COMPRENDRE` +24.5）；其余绿（文字层逐字节一致；p8 121/150 CLEAN，keydiff=[150] 与修前一致；freeze 8/8；spill 0；edge 0；census PASS）。
- 修复 15 处（r1→r2）：与核心相同的 8 处原样同步（`head_zoom` 23→22、P4 框题 `tsize=21`、`head_cine` 23→20、语法头 25→23、`head_comp6` 25→24、P6 框题 `tsize=21`、P7 语法头 24→23、`head_clinic` 25→23）；英文读者版特有 7 处（`text_w` 实测定量）：`band_r1` 删 `ALCARAZ CHAMPION　`（与正上方主头条重复；间隙 −222.2→+122.7px）、`head_phrases` 删 `(ALL FROM THIS ISSUE)`（P7 上文已有同义法语段；间隙 −86.1→+261.9px）、`head_lire` `TIMETABLE`→`DATES`（406.2 < CW 422.5）、`sommaire_title` 24→21、`head_mots_fetes` 23→21、`head_mots_photo` 23→21、`head_dieppe_ex` 25→23。
- r2 余 1 处 HEAD TOO WIDE：P7 `CLINIQUE DES ERREURS　ERRORS` 在 23pt 下仍超 6.1px → `head_clinic` 23→22（409.9 < 422.5）。
- r3 全套门禁（08:04–08:09 UTC）**全绿**：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE（`head_check.py` PASS）；render + webpdf 重渲；occlusion 0 flags；p8 121/150、CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；freeze baseline 8/8、diff vs 核心 +0 非分隔符 CJK（新增 CJK 全为 U+3000：vs 核心 14、vs 修前基线 5，系重排后折行分隔符存留数变化，SVG 内 U+3000 总数 366→371）；boxtitle 0 DEFECT；creambox PASS 0 defects（n=522，中位 1.016、粗体 1.056、常规 0.998；P8 199→199 行、余量 38.1→38.1px）；spill 0；edge 0 TOUCH/NEAR；D5 census PASS（0/0/0）；`census_quotes.py` 弯引号缺陷 0；印/网文字层逐字节一致（各 100,705 字节）。印 PDF 17,031,641 字节 SHA-256 `0503cff0…`、网 PDF 1,622,982 字节 SHA-256 `11e5baba…`（前 8 位；见 §四）。门禁日志：`hidden_files/w47/scratch-d5-rebuild-fr/2026-w47-fr-en/logs-r3/`；工作日志：`hidden_files/w47/scratch-d5-fr/RUN-LOG.md`。

## fixfam1（2026-11-13，独立重校 A1/A2 返修；工作日志 `hidden_files/w47/scratch-fix-fr-family1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-en/logs-fixfam1/`）

- A1 P2 图注改写为城堡描述（`content12.py:184`）：`Châtillon, dans le Beaujolais : le château au-dessus du village, au cœur du vignoble.`
- A2 DIRE LA DATE 表补 ven. 20 与 sam. 21 两行（`content12.py` + `expl.py` 新增 `date_20`/`date_21`：Friday 20 November: Children's Day／Saturday 21 November: Turin semi-finals + Waste Week begins），行距 40→34、练习区块下移 36（`ey = dy + 356`）。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（34 titles）；creambox PASS 0 defects；spill 0（102 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 101,481 字节，100,259 字符，multiset 0）；text.md diff 仅 2 处（图注 1 行替换 + 日期表 8 行新增）；逐页 SVG 哈希比对：仅 p2-vie.svg 变，其余 7 页与修前字节相同（ru2/fix1 态为基准）。三件 SHA：印 17,031,841 B `b227430a9e54…`、网 1,623,184 B `167410e0620c…`、文 46,274 B `f03b13d44104…`。

## minor1（2026-11-13，全新一轮重校轻微项返修；工作日志 `hidden_files/w47/scratch-fix-fr-minor1/FIX-LOG.md`，门禁 `scratch-d5-rebuild-fr/2026-w47-fr-en/logs-minor1/`）

- 轻微 P5 `debat5_note`（`expl.py:128`）：`An old coat's new owner` 窄化（core "一件旧衣服"、法文原文 "un vieux pull"）→ `An old garment's new owner`（取单数 garment，与单数 pull / 一件旧衣服对应；未取 `Some old clothes'`）。同一源在 text.md 两处同源出现（L633 P5 讨论框、L673 LE DÉBAT 栏），均已改。
- 门禁：run.py TOTAL 150、0 FLOW OVERFLOW、0 HEAD TOO WIDE；occlusion 0 flags；p8 extract 121/150、compare CLEAN（vs 核心 keydiff=[150]，vs 修前基线 keydiff=[]）；boxtitle 0 DEFECT（34 titles）；creambox PASS 0 defects；spill 0（102 OBSERVE）；edge 0 TOUCH/NEAR；census PASS；印/网文字层逐字节一致（各 101,484 字节，100,262 字符，multiset 0）；text.md diff 仅 2 行（两处同源行）；逐页 SVG 哈希比对：仅 p5-jeunesse.svg 变；P5 卡面目视通过（两处 `An old garment's new owner — or the bin?` 均在栏内干净）；P8 最小字号重测仍 11.62pt（514 spans）。三件 SHA：印 17,031,843 B `8ffde4f87863…`、网 1,623,186 B `271926332039…`、文 46,280 B `4029e89a87ec…`。
