# 校对笔记 — 2026-W47 de-en（第一轮独立复校，叶子）

- 对象：`production/2026-w47/2026-w47-de-en/`（2026-w47-de-en，德文目标语 × 英文读者语）
- 校对员：叶子（第一轮独立复校；与 de-en builder 第 3 棒、de 核心 builder、各轮复校员不同人）
- 时间：2026-11-11 03:35–03:55 UTC
- 只检查、不改成品：未跑 insert.py / lint --write，未 git add/commit/push/reset/stash，
  未改 core-de、W43–W46、其他目标语家庭、tools/。verify.py 未在原版目录跑（它会重写 SVG），
  其全部检查项用只读脚本在副本/原版只读复现；run.py / render.py / webpdf / export 未重跑
  （重跑会改写成品；冻结证明改用直接 sha256 比对 + 副本重跑）。
- 笔记目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-en1/`
  （PROBE.txt / render_extract.py / scans.py / freeze_source_reg.py / keycheck_probe.py /
  verify_repro.py / render/ / text/ / gates/ / copy/）

## 结论：(a) 零问题，可定稿

本轮全量独立复校零缺陷。以下 3 项为观察项（不计缺陷，见末节），其中 O1、O3 为核心继承、
O2 为一处答案注措辞可斟酌。定稿决定权在协调员。

## 0. 开工探针与身份核对

- 探针 1：`echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8…`，成功。
- 探针 2：在 `hidden_files/w47/scratch-proof-de-en1/` 真实写文件成功。
- 印刷 PDF：`Die-Lucerna-VOL4-de-en.pdf` 10,966,416 字节，
  SHA-256 `a997c6cefe8467bdd37a71158e0f61ceff16d653039f50159b1608305b3a4b87` ✓ 与任务一致。
- 网页 PDF：`Die-Lucerna-VOL4-de-en-web.pdf` 1,555,614 字节，
  SHA-256 `62623cb5996644004ba48a6ed7246cdd0584bec3a2549123174db318384a3a90` ✓ 与任务一致。
- text.md：49,676 字节，SHA-256 `0749ad78f536883f8f3a484d7c93f026d0f7d7f433891861333f7a9a8fbf3830` ✓ 与 KIT 一致。
- 收尾复核：双 PDF SHA/字节/mtime 与开工时一致，未被改动。
  附：`git status` 显示 `tools/freeze.py` / `tools/p8.py` 有未提交修改，mtime 为
  2026-11-10 22:59 / 21:37 UTC（早于本轮开工 11-11 03:35 UTC，我未动过它们；
  与 builder 重建 2（11-11 02:53 UTC）所用为同一工具版本）。

## 1. 全文逐版复校（印刷 PDF 自行重渲染 100 dpi 逐版目视 + SVG 文本逐字精读）

- P1：干净。头条 40 字符（≤56）。日期/星期全对：13.11 周五、16.11 周一（20.45 荷兰）、
  18.11 周三 Buß- und Bettag、22.11 周日 Totensonntag、29.11 周日首个将临期、17.11 周二 19:00
  Dom 开幕。Q1–Q10 题钥与正文一致（Q7 B 荷兰、Q8 B 20.30、Q9 B 萨克森、Q10 B 16.11）。
  目录页码/级别与 KIT §1 一致；"Germany's" 直撇号紧贴（对照）。
- P2：干净。日期算术 18+11=29、15+7=22、16+6=22 全对；"Elf Tage vor dem ersten Advent:
  immer ein Mittwoch" 对。Perfekt 钥匙 Q16–Q20 全对（abgeschafft worden / geschlossen
  geblieben / gegangen / behalten / geschlossen geblieben）。配对 Q25–28（d/c/a/b）对。
  "Let's calculate"、"This week's dates" 250 dpi 放大裁切复核：撇号紧贴，无宽字形。
- P3：干净。市场日期全对（16.11 开、22.11 关、23.12 止、13.11 港口市场已开、17.11 19:00
  正式开幕、20.11 亚琛开）；"fast zwei Wochen früher"（16→29 日 = 13 天）对；1930 画
  "vor fast 100 Jahren"（96 年）对。Q29–Q46 逐题验算全对；"Editor's tip" 紧贴。
  配图在横线之上，图注无重叠。
- P4：干净。德甲第 9 轮 9 场进球逐场加总 4+3+3+7+4+1+3+2+3 = 30 ✓ 与正文"30 Tore"一致；
  最高比分 Leipzig–Augsburg 5:2 ✓；MD10 赛程（周五 20.30、周六 5 场 15.30 + Schalke 18.30、
  周日 Augsburg–Mainz 15.30、Bremen–Hamburg 17.30）与表注一致；24/25.11 欧冠、26.11 欧联
  星期（周二/周三/周四）对。Q47–Q64 逐题验算全对（Q51 B"8 und 5"、Q56–59 mehr/später/
  früher/mehr 均与比分/时间/积分吻合）。UND SIE? 盒与结果表边缘相接、无重叠（与核心一致）。
  "the league's return" 紧贴。见观察项 O1（一条正文赛果未进结果表，核心继承）。
- P5：干净。周计划日期/星期全对（16.11 周一、17.11 周二、18.11 周三、19.11 周四、
  20.11 周五）；1903 日历 „Im Lande des Christkinds"、"über 120 Jahre"（123 年）对。
  Q65–Q82 逐题验算全对。1903 图在位，图注与横线无重叠（11px 间隙）。
  "The editors' week"、"What's" 紧贴。
- P6：干净。图表 44+33+23=100 ✓；Q83–Q100 逐题验算全对（Q85 44+33=77、Q88 100%、
  Q93 wird、Q94 ob、Q95 geht、Q96 beginnt、Q98 Kirchenjahr）。图表标签与条形无交叠，
  条形宽度 748/561/391 与数值成比例。"editors' practice example" 紧贴。
- P7：干净。金句 8 条逐字比对正文见 §2；三课 Q101–Q112 逐题验算全对（Q102 werden
  与 werden-被动态课程设计一致、Q103 wird 未来时、Q110 fraglich、Q111 dass 句动词居末）。
  工具箱 6 条末条在盒内；读者来信含 3 行披露（Editor's example）；VOL.5 预告与 P4 欧战
  日期（24.–26.11）及第 11 轮一致。"Readers' letters"、"Learners'…"、"Editor's example"
  均紧贴（"Learners'" 250 dpi 放大裁切复核通过）。
- P8：干净。A 完形 113–120、B 121–128、C 129–132、D 133–136、E 137–140、F 141–144、
  G 145–149、H 写作逐题验算全对；MUSTER 84 词逐词数过（84，与标签一致），要点齐全
  （手工/比赛/同伴/Buß- und Bettag 或 Totensonntag 句）；答案末端在页脚之上（keys 末端
  2481，底边 2560，余 79px）；Q133 "Die Bundesliga kehrt…" 无粘连。
  网页版 P1/P8 与印刷版逐版比对一致，无豆腐块、无缺字。

## 2. 150 题逐题验算（独立复现，不采信 builder 的 keycheck 文件）

- 方法：把版目录复制到我方 scratch（`copy/`），在副本里 runpy 五个 content 模块重建 REG，
  再用 `tools/p8.py extract`（自跑）抽取 P8 印刷键，逐题比对；同时把我方 REG 与 builder 的
  `en/keycheck-150.json` 逐项比对。
- 副本重跑：REG 总数 150，编号连续 1–150；分版 10/18/18/18/18/18/12/38；
  级别 A2 69 / B1 67 / B2 14；题型 MC 52 / fill-in 41 / transformation 11 / true-false 8 /
  cloze 8 / sentence building 8 / matching 12 / translation 4 / dialogue 5 / writing 1——
  与 KIT 完全一致。副本 8 个 SVG 与原版 SVG 字节相同（8/8，构建确定性独立证实）。
- 我方 REG 与 builder keycheck-150.json：150/150 逐项一致（n/page/level/type/key），差异 0。
- REG 键 vs 我方 P8 抽取键：149/150 精确；唯一非精确为 Q150：抽取器把 REG 键
  "Open task — follow the points in the writing box" 截断为 "Open task"。
  该截断与 builder 所述一致，且 Q150 已在 keydiff 集合中；开放写作题无固定键，属预期内。
- 全部 150 个 REG 键另经人工逐题对照题面/原文/图表验算（见 §1 各版记录），无一错误。

## 3. p8 compare keydiff 逐条核实（自跑：CLEAN，keydiff [137, 138, 139, 150]）

- Q137：核心键 '德甲周五回归。' → 本版 'The Bundesliga returns on Friday.'——
  E 组正向翻译题答案键译成英文，预期内（题面德语句 "Die Bundesliga kehrt am Freitag zurück." 不变）。
- Q138：核心 '市场周日关闭。' → 'The markets are shut on Sunday.'——同上，预期内。
- Q139：核心 '我做一个降临节日历。' → 'I am making an Advent calendar.'——同上，预期内。
- Q140：核心与本版键完全相同（德语句 "Am Montag schaue ich zu Hause Deutschland gegen
  die Niederlande."）——反向题（英译德），键本就是德文目标语句，正确地不在 keydiff 中。
- Q150：核心 '开放题' → 'Open task'——开放写作题标签译成英文；抽取器截断见 §2。预期内。
- 结论：4 条 keydiff 无一为真缺陷。missing=[]，extra_count=0。

## 4. 金句 8 条（P7 Sätze der Woche，逐字比对正文）

8 句在全刊正文连接文本中各出现恰好 2 次（正文 1 次 + P7 引用 1 次），出处页/级别均正确：
1. "Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln."（P1·A2）
2. "Es geht ums Viertelfinale der Nations League."（P1·A2）
3. "Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag."（P2·A2）
4. "Die Märkte beginnen fast zwei Wochen früher."（P3·A2）
5. "Hinter jedem Türchen wartet eine kleine Überraschung."（P5·B1）
6. "Der FC Bayern gewann in Mainz mit 2:1."（P4·B1）
7. "Die stille Woche ist der Übergang: vom November in den Advent."（P6·B2）
8. "Am Sonntag ist es still im Land."（P6·B2）
英文译文逐句核对，均忠实（BrE "Bayern play" 等无误）。

## 5. 禁词 / VOL / 徽章 / 字号

- 禁词：verify.py 全部 18 项（桥接、Le Lucerna、The Lucerna、VOL.3、VOL.2、Geisterspiel、
  Karneval、Volkstrauertag、NFL、American Football、11.11、Tankrabatt、14,04、Hart aber fair、
  Klassiker、Allerheiligen、8,35、ZEW）8 个 SVG 全无。注：builder 称"17 项"为不含"桥接"的计数。
- VOL：VOL.4 出现 9 次（8 个页脚 + P1 刊别行），VOL.3/VOL.2 为 0；VOL.5 出现 6 次，
  均为下期预告/读者来信 VOL.5 引用，预期内；刊头 "Die Lucerna"、周头
  "WOCHE VOM 16. BIS 22. NOVEMBER 2026"、副标题 "TEXT IN GERMAN · EXPLANATIONS IN ENGLISH" 在位；
  页脚逐页 1 枚、页码行 Page 1–8 of 8 逐页在位；头条去空白 40 字符（≤56）。
- 徽章（rx="2.7" 矩形，自数）：逐页 10/15/18/15/18/18/12/35，全刊 141 ✓；
  P8 按级别 A2 22 / B1 13 / B2 0 ✓；Q113–120 完形选项各 1 枚 A2（共 8 枚，在位）；
  对话徽章条 Q145–149（145–147 A2、148 B1、149 A2，在位）；写作标题 "H SCHREIBEN" 带 B1 徽章（在位）。
  P8 各组徽章分布与 REG 级别逐组核对一致（A 8×A2；B 4×A2+4×B1；C 2×A2+2×B1；D 2×A2+2×B1；
  E 2×A2+2×B1；F 1×B1；G 4×A2+1×B1；H 1×B1；合计 A2 22 / B1 13）。
- 字号：P8 最小字号 9.94pt（PyMuPDF 实测印刷 PDF + SVG 13.25 单位 ×0.75 双重确认），
  ≥9.75pt 底线 ✓（低于 11.25pt 目标，属 SOP §1.1 让步第 4 步，KIT 已写明）；其余各版最小
  11.62–12.75pt。P8 题干 15.375pt（让步第 3 步）与 KIT 一致。
- 样式：PAPER #fbfaf6 / INK #302c28 / OLIVE #46581f / CLOTH #37402f，旧式金色/近黑底色值全无。

## 6. 翻译层专项（fan-out 特有）

- 讲解/界面语言确为英文：全部家具、桥接、说明、题干提示、答案简析均为英文；德文仅出现在
  目标语正文、题面、词表德语词与引用句（如 MUSTER、对话）中。
- 360 个 CJK 字面量：机制 + 结果双重核实。①渲染结果：8 个 SVG 的 `<text>` 中唯一 CJK 字符
  是全角空格 U+3000（家具分隔符，每版 12–16 处），无任何汉字/假名/韩字。②源码：版内字符串
  常量含汉字/假名/韩字的仅 2 处，均为不渲染内容——svglib.py 文档字符串
  'Mountains, sun, two stick climbers, chrysanthemums — for 重阳.'（核心同款原文）与
  verify.py 禁词表中的 '桥接'；核心 514 处含 CJK 的字符串常量已全部转写。
  ③冻结差分：新增 CJK 字符共 7 个，全部为 U+3000（P2–P8 各 1 个，P1 为 0）。④text.md：
  汉字/假名/韩字 0 个（U+3000 计 122 处，为家具分隔符）。
  结论：核心的中文讲解层已全数转写，无中文残留；无一处有意保留的中文原文引用（本版无此情形）。
- E 组：Q137–139 题面德语句不变、答案键已译成英文（见 §3）；Q140 题面英文句
  "On Monday I watch Germany against the Netherlands at home."、键为德语句，方向正确。
- 新增英文串抽查：新增无 CJK 字符串常量 449 处（230 个 distinct），抽查 61 条含非 ASCII 者——
  均为德语词 + 英文释义的词表/注释串（如 'die Kerze — candle'、'der Buß- und Bettag = day of
  repentance and prayer · …'），无新增德文正文句（冻结未破）。
- 冻结（源码级，AST 字符串常量多重集比对）：核心无 CJK 常量在 en 版中缺失的仅 5 处，
  均为预期 transform 产物——masthead 副标题 'DIE WOCHENZEITUNG FÜR LERNENDE — …'、
  全角括号 '（' '）'、间隔符 ' · '、PDF 文件名 'Die-Lucerna-VOL4-de.pdf'。
  （builder 称 8 处缺失为另一计数口径——含 verify.py 文档/路径串；实质缺失集一致，均为预期项。）

## 7. U+2019 缺陷类回归

- 8 个 SVG 全扫：U+2019 总数 0 ✓（逐页 0/0/0/0/0/0/0/0）。
- 直撇号 U+0027 逐页：P1 1、P2 2、P3 1、P4 1、P5 2、P6 1、P7 3、P8 0，共 11 处，
  与 KIT 所述 9 处修复 + P1 对照 1 处 + P5 "What's" 1 处一致。
- 目视抽查：P1 "Germany's five hot questions this week."（对照）紧贴；P2 "Let's calculate" /
  "This week's dates" 250 dpi 放大裁切紧贴；P3 "Editor's tip"、P4 "the league's return"、
  P5 "The editors' week" / "What's on your wish list?"、P6 "editors' practice example"、
  P7 "Readers' letters" / "Learners' four most common mistakes"（250 dpi 放大裁切紧贴）/
  "Editor's example" 全版目视均紧贴，无宽字形断裂。回归已清除。

## 8. 机械门（全部自跑，与构建相同的解释器）

构建解释器确认：`~/workspace/weekly-git/tools/venv/bin/python`，Pillow 13.0.0
（系统 python3 为 Pillow 10.2.0，未使用）。builder 门禁亦用该 venv，解释器一致。
详见 GATE-LOG.md。

| 门 | 自跑结果 |
|---|---|
| occlusion_audit.py（自检通过：6 类 planted 全触发，clean 对照静默） | 0 flags ✓ |
| p8.py extract | 150/150 ✓ |
| p8.py compare vs core | CLEAN，missing=[]，extra=0，keydiff=[137,138,139,150]（§3 已逐条核实为预期内）✓ |
| freeze.py diff | exit 0；新增 CJK 7 个，全为 U+3000（P2–P8 各 1，P1 0）✓ |
| freeze 直接 sha256（渲染级冻结交集，sorted + "\n" 连接） | 8/8：逐页 147/163/195/166/173/175/150/186，sha 前 8 位 083e2a2a / 689045ad / 093cf378 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7 与 builder 逐一吻合 ✓ |
| print/web 文字层（pdftotext） | default：print 50,445B / web 50,446B，词多重集相同；raw：均为 49,288B，归一化后完全相同；web 有真实文字层 ✓ |
| measure.py | 24/24 PASS，0 FAIL ✓ |
| verify.py 全部检查项（只读复现，未在原版目录跑） | verbatim 8 句各 2 次 ✓；样式审计 ✓；MUSTER 84 词 ✓；页脚/页码逐页 ✓；头条 40 字符 ✓；P8 底线 9.94pt ✓；图表 44+33+23=100 ✓；日期算术 3 组 ✓；星期全对 ✓；P6 条形 748/561/391 ✓；禁词全无 ✓ |
| chips | 141 枚（见 §5）✓ |
| P8 最小字号 | 9.94pt ✓ |

## 9. 观察项（不计缺陷）

- O1（继承自核心，非 fan-out 引入）：P4 正文提到 "der VfB Stuttgart verlor in Istanbul bei
  Galatasaray mit 0:2"（欧冠第 4 轮），但 "DIE ERGEBNISSE & DER SPIELPLAN" 表未列该场。
  核实：核心 core-de 的 P4 SVG 同样只有正文句、表内无此场；freeze P4 removed 串仅为中文讲解层，
  fan-out 未删任何德文赛果行。表内德甲 9 场齐全（30 球已验算），欧冠德甲球队 4 场中表列 3 场。
  无任何练习题依赖该场赛果。建议协调员裁定：接受为"表列精选赛果"，或在核心修表后重走 fan-out；
  本版不因此阻断。
- O2（措辞，可斟酌）：P8 答案 Q56 注 "(5–2 more goals than 2–1)" 表述压缩生硬，宜读作
  "5:2 一场进 5 球，多于 2:1 一场的 2 球"。键 "mehr" 正确，含义可还原；源自核心中文注
  "5:2 比 2:1 进球多"的直译。非事实错误，不计缺陷。
- O3（核心既有、KIT §8 已列为 honest shortfall）：P1 头条首段无首字下沉（与已接受的
  W46-FR 版相同情形）。fan-out 未引入，SOP §1.1 要求与既有接受状态之间的张力留待协调员。

## 附：未核查项

- 无。本任务全部核查点均已覆盖：8 版印刷目视 + 网页 P1/P8、150 题逐题验算、金句 8 条、
  禁词、VOL.4、徽章 141 枚、P8 字号、翻译层 360 字面量、U+2019 回归、机械门全套。
