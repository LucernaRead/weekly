# GATE-LOG — 2026-W47 nl → ja · proof1 机械门实跑证据

- scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-ja1/`
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383` 已验）
- `TMPDIR` 全程指向 scratch 下 `tmp/`（未用系统 /tmp）；源文件未改动

## §0 探针与身份

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`（通过）
- goals 侧 `hidden_files/w47/scratch-proof-nl-ja1/probe.txt` 可写（已写 `probe-ok 2026-11-11T11:27:02Z`）
- SHA/字节：印 `af010c1f…5361c1b1` / 26,049,268 B；网 `07243a6b…2dbd1d2f` / 2,119,188 B；text.md `6685d681…46d789` / 47,592 B——与任务一致

## §1 occlusion 审计（`tools/occlusion_audit.py svg/`）

- exit 0；自检阳性对照全过（`BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX` 各 1 命中，干净对照静默）
- 结果：`0 flags`
- 盲区说明：该审计对奶油框内溢出、框标题溢出、横向溢出、降部溢出是盲的——已另行用 creambox + PIL 真墨迹实测（§2、§3），不以 occlusion 0 为放过依据

## §2 正典 creambox.py 全版扫描（`creambox.log`）

- 命令：`creambox.py svg/p*.svg`；26 个奶油盒（P1 4、P2 8、P3 2、P4 2、P5 4、P6 3、P7 3、P8 0）
- P7-TOOLBOX：`3 boxes, min inside clearance +12.5, min desc-clear +6.5`——通过
- 下面两行（+24/+32）为窗外下一标题，系已知假阳性，已逐条裁决：
  - P1 `IN DEZE EDITIE` 盒：框内末基线 1636.0（内边 +16.0 / desc +9.7）；窗外 +24.0 为 `HET WOORD VAN DE WEEK` 下一栏目标题
  - P2 4 词盒：框内末基线 1731.9（内边 +36.1）；窗外 +32.0 为盒下正文 `Let op: schrijf je gedicht…`
- 其余盒内边最小值：P2 `EN JIJ?` +5.0、P5 `EN JIJ?` +5.1、P6 图表盒 +7.1、P4 `HET PROGRAMMA` +14.2——均为正
- 另：P2/P5 末行 desc-clear −1.0/−0.9（0.30×字号余量法）已转 §3 PIL 真墨迹裁决——实为框内

## §3 PIL 真墨迹全版扫描（自写 `ink.py`，`ink-report.txt`）

- 方法：解析全部 `<text>`（x/y/字号/字重/斜体/anchor），按 SVG 声明字体用 PIL `font.getbbox(anchor='ls')`（基线锚，`bb[3]` 为真降部）求真墨迹；凡墨迹越出奶油盒右/底边或页边（1950）即旗标
- 结果：**`!!` 旗标 0 个**；全卷最宽墨迹右缘 1873.8（P8 解答注）< 1950
- 逐盒末行真墨迹（over = 墨迹底 − 盒底，负=框内）：
  - P1：−47.0 / −162.0 / −16.0 / −53.0
  - P2：−52.1 / −46.7 / −7.3 / **−3.0**（`EN JIJ?` 末行 `ダ語で2文書いて編集部に送ろう。`，desc-clear 法 −1.0 为误报）/ −34.1 ×3 / −9.4
  - P3：−46.7 / −16.2；P4：−49.7 / −14.2；P5：−47.6 / −46.7 / −32.3 / **−3.1**（`EN JIJ?` 末行，desc-clear 法 −0.9 为误报）
  - P6：−49.7 / **−5.1**（图表盒末行 `れる？（若者100人）`）/ −9.0；P7：−15.4 / −10.5 / −25.5
- P1 36pt 副标题（`オランダ語週刊 VOL.4 ORANJE SINTERKLAAS PAKJESAVOND`，逐字 tspan，x=132.2 起）与 53pt 头条均在页内，无横向溢出
- P6 图表头 `DE GRAFIEK グラフ（練習データ）`：真墨迹在框内（KIT 的 403px/超边 2.5px 是 advance 宽算法，非真墨迹）
- 注：首版 ink.py 用默认锚（ascender 锚）曾误报多处 +7～+21px，已修正为基线锚 `anchor='ls'` 后复核为 0 旗；修正记录见本 log（方法备注）

## §4 p8 compare（`tools/p8.py`）

- `compare --core-p8 production/2026-w47/core-nl/svg/p8-toets.svg --edition-p8 …/svg/p8-toets.svg --total 150`：exit 0
- `core 150 noted / edition 150 noted / status: CLEAN / missing=[] extra_count=0 uncertain=[] / keydiff=[137, 138]`
- keydiff 裁决（`p8-extract.json` vs `p8-core-extract.json`）：
  - 137：版 `シンタクラース・ニュースは毎日18:00に放送される。` vs 核 `圣诞老人新闻每天 18:00 播出。`——同义日/中翻译重定向
  - 138：版 `上位2チームが準々決勝に進む。` vs 核 `前两名晋级四分之一决赛。`——同义重定向
  - 按 `p8.py` 说明，翻译题重定向属 informational，非失败；其余 148 键逐字一致。**非缺陷**
- `extract --p8 … --total 150`：`noted set = 150 of 150`；P8 印出键与 text.md 答案逐题比对：149 道一致，150 题作文印 `✓`（设计如此，见 keycheck-150.json）

## §5 freeze

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg`：**8/8 SVGs byte-identical**，核心 8 文件重哈希无改动
- `freeze.py diff --core-svg core-nl/svg --edition-svg …/svg`：exit 0；每页增减串均为讲解层中→日替换（如 P1 `De Lucerna 荷兰语周报 VOL.4 LUCERNA DUTCH WEEKLY` → `De Lucerna オランダ語週刊 VOL.4 本文はオランダ語 解説は日本語`）；新增 CJK 3315 字全为日语讲解字符；长拉丁串筛查无荷兰语目标句增减；P8 增减串仅为答案注语言替换与重排空格
- 方法备注：`tools/freeze.py` 无 `freeze_direct` 子命令，仅 `baseline`/`diff`——已用 baseline 8/8 代替 direct 核验，**不作缺陷**

## §6 keycheck 150/150（`keycheck-150.json`）

- text.md 全文通读 + 印 PDF 8 页逐页渲染目视（`render-p1.png`～`render-p8.png`，130dpi）
- 150/150 通过；分级 A2 46 / B1 73 / B2 31；按页 10/18/18/18/18/18/12/38；题号 1–150 无缺无重
- 模范文实数 81 词（80–100 范围内）；D/F 匹配题选项表已对 SVG 原文核实（P2 D：a 列表/b 小诗/c 马食/d 门口；P8 F：a 小诗/b 新闻节目/c 首位/d 门口）
- 26 个外部事实点中关键 3 项已以外源核验（§9）

## §7 boxtitle 逐个实测

- 见 §2–§3：全部 26 盒标题真墨迹无右溢/底溢；P1/P2/P6 重点标题（`DE WEEK IN CIJFERS 今週の数字`、`ZO ONTHOUD JE HET こう覚えよう`、`DE GRAFIEK グラフ（練習データ）`、`HET WOORD VAN DE WEEK`）目视 + 墨迹双重通过

## §8 印/网文字层比对

- `pdftotext -layout` 全卷：印 105,968 B / 网 105,976 B；逐页字节 P1 11694/11699、P2 11941/11941、P3 9231/9231、P4 8944/8944、P5 10390/10390、P6 10143/10146、P7 13196/13196、P8 30429/30429
- `diff` 仅 8 行、2 处纯空格差异：P1 `MA 16 Oranje…` 间距、P6 `DE GRAFIEK グラフ` 间距；文字零差异。**非缺陷**（与 KIT 的 `posdiff 0` 口径略有出入，属空格排版，非文字差）
- 斜体专项（D1，见 PROOF-NOTE）：印 P1 斜体 span 1 个（`Newsreader16pt-Italic 16.12pt`），网 0 个（`LucernaNewsreader-Regula`）；文字层 `«de groepswinst»` 前后空格与闭引号完整——三联症仅第 3 项复现

## §9 P8 最小字号实测（PyMuPDF，`fonts-italic.log`）

- 印 PDF P8 最小 span **10.12pt**（`Newsreader16pt-Regular`），网 PDF 同为 10.12pt；与 KIT（10.12，中位数 10.12）一致
- SOP §1.1：答案字号下限 9.75pt——10.12 ≥ 9.75，合规（未达 11.25pt 目标但在让步顺序内）

## §10 弯引号全版扫描

- U+201C/U+201D/U+2019：8 个 SVG + text.md 全部 **0**；`« »`（U+00AB/BB）为本周词/引用的界符（与核心一致）；`'s`（`'s avonds`/`'s Nachts`/`'s nachts`）用 ASCII `'`，与核心一致
- 核心 P1 唯一的 `“ ”` 在中文 gloss `“小组头名”` 内，本版已正确本地化为 `「グループ優勝」`——**非缺陷**
- SVG 文本节点内无直引号 `"`（3096 等计数均为属性引号）

## §11 必查项 (a)–(g) 逐项

- (a) P1 溢出：无（§3：最宽墨迹 1873.8；副标题/头条均在限内；P1 渲染目视干净）
- (b) P3/P5 右栏降部漫出：无（§3：全部末行真墨迹在框内；P5 `EN JIJ?` −3.1px）
- (c) P7 toolbox：通过（§2：最小内边 +12.5 / desc +6.5；渲染目视三盒完整，BRIEVEN 盒止于 ZINNEN 线之上）
- (d) E 节 type 标签：全日语——`翻訳`/`日本語に訳す`/`オランダ語に訳す`；中文残留扫描（`翻译/译注/讲解/练习/单词/单选/填空/阅读/周报/荷兰语`）仅命中 `判断` 7 次，均为日语 `正誤判断` 词内；SVG 内亦无中文残留。**未复现**
- (e) 网 PDF 斜体：(i)(ii) 未复现；(iii) 复现——D1
- (f) ABSTRACT 刊名：缺 `De Lucerna`——D2（全文：`オランダ語週刊 Lucerna VOL.4（2026年11月16日〜22日）：シンタクラースとパッケスアーフォント、ネーションズリーグのオランダ対ドイツ、エクスペディティ・ロビンソンとシンタクラースの伝統の変化——オランダ語の読解と150の練習問題、レベルA2〜B2、日本語の解説付き。`）
- (g) 日语时间误写：无。`日:` 零命中；`16:30`（2）、`18:00`（28）、`20:45`（17）、`20:00`（13）、`12:00`（16）等全部完整；`11月16日：` 为正常日期+全角冒号分隔，非碎片误译

## §12 其他核验

- 日期/星期（`date -d`，Europe/Amsterdam）：11/14 六、11/15 日、11/16 一、11/21 六、11/22 日、11/24 二、11/29 日、12/5 六——与版内星期表述全部一致
- 内部标签扫描：SVG 内无 `2026-w47`/`2026-W47`/`nl-ja` 等；`VOL.4` 为刊别（页眉/页脚/副标题），`VOL.5` 仅出现在 P2/P7「来週の予告/约稿」内容句内，属内容非内部标记
- 图表算术：35+30+20+15=100；35+30=65；12:00–16:00=4h；11/16→12/5=19d；2009→2026=17y；11/14→11/15=1d——全部正确

## §13 外部事实来源（2026-11-11 检索）

- **PSV 26 分领跑荷甲**（Q63/Q126）：VAVEL Eredivisie standings 2026/27（2026-11-08 更新）：`PSV 12 战 26 分`第 1；PitchLab：`PSV top the table as of 8 November, with 26 points from 12 games`；Sports Mole、TuringStats、BankoZeka 表格一致（12 战 8 胜 2 平 2 负 40:15 +25，26 分，领先 Feyenoord 1 分）；Cambuur–PSV 2–5（11 月 8 日）与第 13 轮 11 月 21 日 NEC–PSV 一致。URL：`https://www.vavel.com/en/data/eredivisie/standings/`、`https://pitchlabstats.com/league/ned-eredivisie`
- **阿姆斯特丹到着第 88 届**（Q32/Q123/Q139）：holland-explorer（2026-11-09 更新）：`Sun 15 Nov 2026, Amsterdam (88th edition)`；amsterdaminside：`the gemeente lists this one as the 88th edition`；desinterklaassite：`Zondag 15 november 2026, Boot De Omval 10.15 uur; landstoet Stopera 13.00 uur`；noordhollandnieuws：`11.30 aankomst Scheepvaartmuseum; 13.00 start Stopera`；与 P3 文章（10:15 出发、11:30 到敞篷船博物馆、13:00 Stopera、88e）逐项一致；全国到着 Grave 11 月 14 日、NPO 3 12:00 直播亦一致。URL：`https://holland-explorer.com/sinterklaas/`、`https://www.desinterklaassite.nl/intocht-sinterklaas-amsterdam.html`
- 其余事实（`Het diner` 2009、Merel Westrik、Marieke Moorman、Nations League 小组形势）属冻结核心原文，本次未另行外验；Q63/Q126 的 26 分注与 Q32 的 88 届注均已外验为真

## §14 判为非缺陷的项（裁决记录）

1. keydiff 137/138：翻译重定向，同义（§4）
2. creambox BELOW-WINDOW +24/+32：下一标题/盒下正文，假阳性（§2）
3. desc-clear −1.0/−0.9（P2/P5）：真墨迹框内 −3.0/−3.1px，余量法误报（§3）
4. P6 图表头 advance 宽超边 2.5px：真墨迹在框内（§3）
5. 弯引号 0：核心仅中文 gloss 有 `“ ”`，本版 `「」` 为正确本地化；`'s` ASCII 省略号与核心一致（§10）
6. 印/网 2 处纯空格差异：文字零差（§8）
7. `freeze_direct` 不存在：方法备注，已用 baseline 8/8 代替（§5）
8. Q78 `Zij` 单复数：P8 答案注已消歧，核心冻结原文——观察 O1，非缺陷
9. Q150 P8 印 `✓` 而 text.md 为自由课题指针：设计如此，非键差（§6）
10. KIT「P6 图表头超边 2.5px 渲染不可见」：真墨迹证实确不可见，属实
