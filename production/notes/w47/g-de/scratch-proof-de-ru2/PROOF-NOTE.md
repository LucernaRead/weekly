# PROOF-NOTE — Lucerna Weekly 2026-W47 `de-ru`（proof2，独立全量复校）

- 复校员：proof2（只读复校；未修版、未 commit、未 push、未派 subagent）
- 复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-ru/`
- 复校日期：2026-11-11
- 前情：proof1 为 (a)，但 proof1 未跑全版 creambox 扫描；本次重点为 P7 工具盒清除量独立重测 + P8 宽引号实测。

## 0. 对象核对（SHA 均与任务单/KIT 一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `Die-Lucerna-VOL4-de-ru.pdf` | 10,954,759 B | `d8f84e0500e23c19aed45e5eda095a37c8c55ca71c8e94aa43fdd0f0b5d4bf1e` |
| 网页 PDF `Die-Lucerna-VOL4-de-ru-web.pdf` | 1,647,527 B | `462f516d1087dc7d997f9b7be66ccd842b7225fed37601ffcbf7c54ee9407c41` |
| 文本导出 `2026-w47-de-ru.text.md` | 56,231 B | `dee6697b0ec3ff279ad4508dcc7d7402952d40fcc8670b1208a2de9158074958` |

- 三件 SHA 已用 `sha256sum` 与盘上文件及 KIT 核对一致；文本导出 SHA 与 fix 前相同（本次 fix 只改版式，不改文字）。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0（`9daeafb9…`）+ scratch 目录真实写文件通过。
- 阅读：SOP §1.1、§8、§9 全文；proof1 PROOF-NOTE 全文；FIX-LOG（家庭工具盒修）§4 de-ru 行全文；本版 KIT 全文。KIT 要点：150 题，A2 69 / B1 67 / B2 14；P8 键 9.94pt（楼层 9.75，目标 11.25——已披露的让步）；P8-keys 止于 y=2545/2560（余 15px，已披露）；chips 141；frozen shas `73347f49 / 689045ad / f356adcf / df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / 7016818d`。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-ru2/`（`TMPDIR=<scratch>/tmp`；未写 /tmp，未写 repo 的 `hidden_files/w47/`）。

## 1. 印刷版目视（8 页，100dpi 全页 + 重点 200dpi 裁切）

- **P1**：干净。头条 `Die Bundesliga kehrt zurück — Bayern gegen Köln`；20.30 Uhr 开球；塞尔维亚 Fri 13 Nov、荷兰 Mon 20.45；Q1–Q10 一致；`DIE WOCHE IN ZAHLEN` 5 очков / 20.30 / 30 голов 与 P4 一致。刊头、VOL.4 行、页脚 `Страница 1 из 8` 正确。
- **P2**：干净。18.11. Mittwoch / 22.11. Totensonntag / 29.11. 1. Advent；算术 18+11=29、15+7=22、16+6=22；1995 年废除；Q11–Q28 读过；Q22 键 B=1995。
- **P3**：干净。Q34 新题干目视确认：`Am Montag öffnet in Köln der erste ___.`；Q32 Falsch（Ritter 画的是 Nürnberg，不是 Köln）；Q39 B（Hafenweihnachtsmarkt 自 13 Nov）；Q40 B（至 23. Dezember）；Q41 A；Q42 A。
- **P4**：干净。成绩表与正文一致；MD10 赛程列出；Q47–Q64 读过一致（Q51 B=8 und 5；Q56 mehr；Q57 später；Q58 früher；Q59 mehr；Q60 A 20.45；Q61 B 20.30；Q62 C 18.30；Q63 A 17.30；Q64 B 3:1）。
- **P5**：干净。1903 Kepler 日历图 + 图注与 ÜBUNGEN 标题无遮挡；Q68 在第 1 栏；Q82 与页脚无遮挡；Wochenplan Mo 16.11–Fr 20.11 一致；Q65 A、Q66 B、Q67 B、Q68 B、Q69 A、Q70–75 词汇、Q76–79 weil 句末动词、Q80 Richtig、Q81 Falsch、Q82 Richtig。
- **P6**：干净。柱状图 44/33/23 和为 100；标签止于柱前；ÜBUNGSDATEN 免责声明在；2,05 Cent Stromsteuer；Haushalt 27.11.；Q83–Q100 读过一致（Q83 A、Q84 B、Q85 B 77%、Q86 B、Q87 A、Q88 B、Q89 B、Q90 A、Q91 B、Q92 B、Q93 wird、Q94 ob、Q95 geht、Q96 beginnt、Q97 Buße、Q98 Kirchenjahr、Q99 Friedhof、Q100 Einigung）。
- **P7**：干净。A2/B1/B2 课 + Fehlerklinik 德语全对（Halb neun = 8.30；动词第二位；Perfekt 分词句末；ob 从句动词句末）；编辑示例 + 俄语说明（无真实来信，符合 F-MAIL 规则）；VOL.5 预告与 KIT 一致。Q101–112 键核对无误（101 wird、102 werden、103 wird、104 A Passiv、105 stiller、106 weil、107 weil 从句、108 A、109 ob、110 fraglich、111 dass 从句、112 B）。工具盒见 §5。
- **P8**：干净。Battery A–H 齐全；MUSTER 84 词（程序重数）；150 键全部印在 ANTWORTEN 块；Fußball 1905 图 + 图注/出处。填空 113–120（schaut/bastelt/schreibt/sieht/beginnt/liest/denkt/ist）、Q121–132、造句 133–136、翻译 137–140（140：`Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.`）、配对 141–144（c/a/d/b）、对话 145–149（öffne/machst/schaue/schaue/lese → A/B/A/A/A）、写作 150。

## 2. 网页版目视

- 100dpi 像素比对（印 vs 网，`renders/p-*.png` vs `w-*.png`）：P2/P6 mean|Δ| 0.00（完全相同）；其余 0.10–0.53，frac>40 ≤0.0021——仅字体抗锯齿差异。
- 目视 `w-1.png`、`w-7.png`、`w-8.png`：与印刷版一致。w-7 工具盒、LESERBRIEFE、NOCH EIN WORT 干净；w-8 Q147/Q148 选项清晰可读（见 §10 假警报），1905 图注 `Fußball 1905: Schweiz gegen Frankreich. Foto: unbekannter Fotograf, 1905 — public domain` 清晰。
- 印/网 text layer：`pdftotext` 默认均为 57,607 B；`-raw` 均为 56,407 B；归一化后 raw 文本**字节相同**；词多重集相同（各 7,829 词）。（proof1 的 rebuild-B 数字为 57,610/57,613——本次 fix1 构建不同，两版现已相等；不是缺陷。）

## 3. 门禁表（全部通过）

日志均在 `gates/` 下。

| 门禁 | 结果 |
|---|---|
| creambox.py（canonical，8 页 SVG 全扫） | 全部盒内清除量为正；P7 工具盒 +20.0（见 §5）；无真溢出 |
| occlusion_audit.py | 自检 6/6 植入类触发；实跑 **0 flags**，rc=0 |
| p8.py extract | 150/150 |
| p8 compare（vs core-de） | `CLEAN`，missing=[]，extra_count=0，keydiff=[137, 138, 139, 150]（预期：137–139 为俄语正向翻译，150 为开放写作题） |
| freeze.py diff（core `core-de/svg`） | 新增 CJK 共 7 个，全为 U+3000，P2–P8 各 1 个，P1 为 0 |
| freeze_direct.py | source PASS（0 未 accounted 的增删；520 删 / 528 增全部 accounted）；rendered **8/8 PASS**；frozen 计数/SHA 与 KIT 相同（149/163/198/166/179/175/160/187）。首次跑 rc=1 仅因输出目录不存在，`mkdir -p` 后重跑 rc=0 |
| verify.py（本版） | rc=0；TOTAL 150；编号连续；style audit True；verbatim OK；P8 楼层 True（9.9375pt）；图表 44+33+23=100；日期算术 True（18 Nov +11d、15 Nov +7d、16 Nov +6d） |
| keycheck.py | **149/150 exact**；唯一不符 Q150（REG 键 `Свободное задание — следуйте пунктам из рамки письма`，提取器截断为 `Свободное задание`——预期行为） |
| boxtitle.py（按真墨迹量） | **7/7 fit**；最大 391.9px（LESERBRIEFE `Письма читателей`）vs 400.5 预算；工具盒 `Справка` 391.8 |
| d2scan.py（abutting） | 80 对检查，**0 个网页间隙 >0.5pt** |
| 最小字号（PyMuPDF，两版 PDF 每页相同） | P1 11.62、P2 12.75、P3 11.62、P4 11.62、P5 11.62、P6 12.75、P7 11.62、**P8 9.94pt**（≥9.75 楼层） |
| chips | `rx="2.7"` 共 **141** |

**方法偏差说明（非缺陷，记录在案）：** rebuild-A（`scratch-fanout-de-rebuild-A/`）没有 `tr_ru.py`、没有 `ru/` 目录（仅 en/es/fr/it/pt），故 freeze_direct / boxtitle / keycheck 用的是 `scratch-fanout-de/` 中的 `tr_ru.py`。FIX-LOG §5 指出该目录中仅 fr/it 副本过期，ru 副本为当前版。任务单要求“用 rebuild-A 的新副本跑”——对 ru 而言 rebuild-A 根本不存在该副本，故本次用的是唯一可用的当前 ru 副本。

## 4. 引号/弯引号扫描（P8，de-en D1/D2 方法）

- U+201D 在 text.md + 全部 8 个 SVG 中为 **0**；U+201C 33 / U+201E 33，全部为成对德语 `„…"` 开闭引号；`«`/`»` 各 31 个，平衡。de-en 的 D1/D2 缺陷类（无衬线体中的英文弯引号 U+201C/U+201D）在本版不存在。
- **H-box 指令**（`«Meine Novemberwoche»`，Newsreader 16.12pt，非无衬线）：200dpi 墨列测量，闭引号 `»` 前空隙 = **1.80pt = 0.11em**，后空隙同样 1.80pt（对称）→ **PASS**（≤0.2em）。裁切：`renders/crop-p8-hbox-200dpi.png`（源 `renders/p8-200-8.png`）。
- **Q67 键**（`«Im Lande des Christkinds»`，Noto Sans CJK SC 9.94pt；键跨两行，闭引号 `»` 在第 2 行 `Christkinds` 之后）：像素列显示**连续墨迹 501.48–510.12pt，无空白列**——闭引号前空隙 ≈ **0.00pt / 0.00em**（引号墨迹与 `s` 相接；首轮 `quote_pixel.py` 因前一字符与引号墨迹合并为同一墨段而返回空，改用直接列转储解决）。裁切 `renders/crop-p8-key67-200dpi.png` 目视确认 `Christkinds» (1903))` 紧贴，无可见空隙 → **PASS**。工具与测量点见 `gates/quote-pixel.log`、`gates/spots.json`（`quote_pixel.py` 自 `scratch-proof-de-zh-tw2/` 复制）。

## 5. P7 工具盒清除量独立重测（本次重点）

- canonical `creambox.py` 全版扫描（`gates/creambox-all.log`）：工具盒 y=310、bottom=813.0、末基线 793.0，**盒内清除 +20.0，下行字母清除 +13.9**——与修方宣称（+20.0）完全一致。
- 同页：LESERBRIEFE +10.4（下行清除 +4.5）、NOCH EIN WORT +42.9；P7 共 6 盒，最小盒内清除 +10.4，最小下行清除 +4.5。
- 其余各页盒内清除量最小 +14.0。BELOW-WINDOW 行全部裁定为已知假阳性：P1 +24.0 `DAS WORT DER WOCHE`（下一块标题）、P2 +44.9 `Die Daten der Woche`（下一块标题；该盒自身末行 +19.5 在盒内）、P7 BEISPIELE 盒 +34.0/+35.0（`A2/B1/B2`、`Вставьте`、`101./105./109.`——盒下方的习题号；盒内 +47.4 已确认）。**无 BELOW-WINDOW 落在 +12.7/+18.0 真溢出区间。无真溢出。**
- 200dpi 放大裁切（`renders/crop-p7-toolbox-200dpi.png`，源 `renders/p7-200-7.png`）：末条 `Es ist fraglich, ob... = ещё сомнительно` 完整在奶油盒内，下行字母下方有清晰奶油余量；盒顶上移后（y=310，比 A2/B1/B2 标题 330 高 20px）与上方引言间隙干净，无碰撞。

## 6. Q34 新题干

- 新题干 `Am Montag öffnet in Köln der erste ___.` 在 content34.py、text.md、P3 SVG、印刷 text layer、网页 text layer 中各出现 **1 次**。
- 旧带空题干 `die ersten ___` 在上述五处均为 **0 次**。
- 3 处 `öffnen in Köln die ersten`（无空）为合法冻结句（P3 正文、P5 引入、Q80 题干）。

## 7. 内容交叉核对（text.md 全文 1,185 行逐行读过）

- 德语正文 + 俄语讲解层逐句读过；150 键逐题与题干/正文/表格/图表语义核对（补充机器 keycheck 的 149/150）。未发现题干/键不符。
- **MUSTER**：程序重数正好 **84 词**。
- **P7 金句 8/8** 在 text.md 中逐字一致，页码归属正确（S.1×2、S.2、S.3、S.4、S.5、S.6×2）。
- **ABSTRACT.txt**：1 行，384 字符，0 个 ASCII 双引号，俄语，含 VOL.4、A2–B2、150 упражнений、真实刊期事实——符合 SOP §9。
- **星期核对**（`date`，Europe/Berlin）：3.11 Tue、4.11 Wed、5.11 Thu、6.11 Fri、7.11 Sat、8.11 Sun、13.11 Fri、16.11 Mon、17.11 Tue、18.11 Wed、20.11 Fri、22.11 Sun、27.11 Fri、29.11 Sun——全部与正文一致。
- 配对题导出呈现特点（非缺陷）：text.md 将分组配对题 25–28 / 52–55 / 141–144 呈现为术语按顺序配选项释义（例 `der Buß- und Bettag — ruhig und leise, ohne Lärm`）；正确配对在键块中（25 d、26 c、27 a、28 b；52 d、53 b、54 c、55 a；141 c、142 a、143 d、144 b），已逐题核对正确。与 proof1 所述同一呈现方式。

## 8. 外部事实核查（2026-11-11 网查，全部通过）

- **德甲 MD9（6–8 Nov 2026）**：Hamburg–Gladbach 3:1、Mainz–Bayern 1:2、Dortmund–Elversberg 2:1、Leipzig–Augsburg 5:2、Paderborn–Frankfurt 2:2、Köln–Leverkusen 1:2、Freiburg–Union 2:0、Hoffenheim–Schalke 2:1；**共 30 球**；Bayern 榜首（21 分，29:9）以净胜球压 Dortmund；**Köln 第 15**（9 分，10:14）。来源：bundesliga.com、fussballdaten.de、sportradar、stefan-jaekel.de、thesportsscout.com。
- **德甲 MD9 补**：Stuttgart–Bremen **1:0**（Sat 7 Nov，Mittelstädt 7'）——bundesliga.com。
- **德甲 MD10 赛程（9 场全核）**：Bayern–Köln Fri 20 Nov 20:30；周六 15:30 五场（Leverkusen–Paderborn、Frankfurt–Hoffenheim、Union–Leipzig、Gladbach–Dortmund、Elversberg–Freiburg）；Schalke–Stuttgart Sat 18:30；Augsburg–Mainz Sun 15:30；Bremen–Hamburg Sun 17:30。来源：fussballdaten.de、bundesliga.com。
- **欧冠 MD4（3–4 Nov 2026）**：Atlético–Bayern 0:2（**Karl 54'、Laimer 74'**）、Dortmund–Betis 2:1、Leipzig–Man City 2:3、Galatasaray–Stuttgart 2:0。来源：fcbayern.com、kicker。
- **欧冠/欧联 MD5（24–26 Nov 2026）**：Lille–Bayern Wed 25 Nov 21:00 CET、Inter–Stuttgart 25 Nov 21:00；Dinamo Zagreb–Leverkusen 26 Nov 18:45 CET、Hoffenheim–Sturm Graz 26 Nov 21:00 CET。来源：bundesliga.com 赛程页、UEFA。
- **欧联/欧协 MD4/3（5 Nov 2026）**：Leverkusen–Marseille 0:1、Crystal Palace–Hoffenheim 1:1、Trabzonspor–Freiburg 0:1。来源：UEFA、fussballnationalmannschaft.net。
- **塞尔维亚–德国，Fri 13 Nov 2026 20:45，贝尔格莱德 Rajko-Mitić-Stadion**：UEFA 因球迷歧视行为观众禁令；例外——15 岁以下儿童（带老师/教练）+ **50 名指定 DFB 球迷**获准，约 5,000 人预计到场。与正文完全一致。来源：kicker、bundesliga.com（2026-11-10 报道）。
- **欧国联 A2 组 4 轮后**：荷兰 8、希腊 8、德国 5、塞尔维亚 0；前两名进四分之一决赛；德国–荷兰 Mon 16 Nov 20:45 柏林（ARD），小组末战。与正文完全一致。来源：sportradar 积分榜、kicker。注：一家 wettbasis 表格列希腊 6 分，与多数来源（8 分）矛盾；正文未写希腊分数，无影响。
- **科隆圣诞市场 2026**：Dom 市场（Roncalliplatz）16 Nov–23 Dec，Sun 22 Nov（Totensonntag）关闭，官方开幕 Tue 17 Nov 19:00；Markt der Engel（Neumarkt）16 Nov–23 Dec；Hafen-Weihnachtsmarkt（Schokoladenmuseum）13 Nov–3 Jan。与正文完全一致。
- **亚琛（Aachener Weihnachtsmarkt）2026**：20 Nov–23 Dec。与正文一致。（来源另注其 Totensonntag 22 Nov 仅 18:00 起开放；正文未称亚琛关闭，无冲突。）
- **Wilhelm Ritter**（1860 年 8 月 24 日 Nürnberg – 1948）：作品含 *Weihnachtsmarkt auf der vorderen Insel Schütt*（1930）。与正文一致。
- **Richard Ernst Kepler**（1851–约 1930）：首部印刷降临节日历 `Im Lande des Christkinds`（1903，Reichhold & Lang，慕尼黑）设计者。与正文一致。
- **Totensonntag / 萨克森禁舞令**：SächsSFG §6——Buß- und Bettag 及纪念/哀悼日（含 Totensonntag，§2）公共舞会禁令 **3:00–24:00 Uhr**（Karfreitag 全天）。与正文逐字一致（revosax.sachsen.de 法律文本）。
- **Buß- und Bettag**：仅萨克森为法定假日；1995 年几乎全德废除（作为 Pflegeversicherung 的补偿）；恒为周三，1st Advent 前 11 天。与正文一致。
- **联邦预算 2027**：正文称“Er soll am Freitag, dem 27. November, verabschiedet werden”——bundestag.de 官方：“die Verabschiedung ist für Freitag, 27. November 2026, geplant”，当日在三读记名投票。12 Nov 仅为预算委员会 Bereinigungssitzung（Bundesrechnungshof：“Rund zwei Wochen später wird das Parlament abschließend über den Haushaltsentwurf abstimmen”）——**不构成矛盾**，已核实无冲突。
- **Stromsteuer**：家庭用户 **2.05 Cent/kWh**（自 2003 年未变）；总理 Friedrich Merz 推动为全体消费者降至欧盟最低；财长 Klingbeil 谨慎、尚无空间。与正文“Kanzler Friedrich Merz will sie für alle senken. Haushalte zahlen weiter 2,05 Cent pro Kilowattstunde. Ob eine Einigung gelingt, ist offen.”一致。
- **P8 1905 照片图注**（`Fußball 1905: Schweiz gegen Frankreich`）：瑞士首场官方国际赛，法国 1–0 瑞士，1905 年 2 月 12 日，巴黎王子公园（Cyprès 60'）。来源：Wikipedia、RSSSF。

## 9. 已查清的假警报（非缺陷）

- 100dpi 下 P8 Q148 选项 B/C 看似相同（`schaut`/`schaut`）。text layer + SVG 证实：**148. A. schaue · B. schaust · C. schaut**——B 是 `schaust`，C 是 `schaut`；空为 `Da ___ ich die Nationalelf`，键 A `schaue` 为唯一正确选项。Q147 同理（A. schaue · B. schaust · C. schaut）。网页版 w-8 放大亦可读清。

## 10. 继承的让步（非缺陷，已披露）

- P8 键 9.94pt（楼层 9.75，目标 11.25——SOP §1.1 让步第 4 步）；P8-keys 止于 y=2545/2560（余 15px，紧但通过）；P8 题干 15.375pt（core O1，协调员决定，待联合裁决）。

## 缺陷清单

**无。**

## Verdict

**(a) 零问题，可定稿。**

- 本次重点两项均实测通过：P7 工具盒清除 +20.0（下行清除 +13.9），与修方宣称完全一致，200dpi 裁切目视确认；P8 H-box 闭引号前空隙 0.11em、Q67 键 0.00em，均 ≤0.2em，de-en D1/D2 类缺陷未复现。
- 全套门禁全绿（creambox 全版无真溢出、occlusion 0 flags、extract 150/150、compare CLEAN、freeze_direct 8/8 PASS、verify rc=0、keycheck 149/150 唯一预期不符、boxtitle 7/7、d2scan 0 间隙超标）。
- 150 题键逐题核对无误；17 组外部事实全部网查通过（含原先存疑的预算 27 Nov 日期——12 Nov 仅为委员会会议，无冲突）；text.md 逐行读过；印/网两版像素与文本层一致。
