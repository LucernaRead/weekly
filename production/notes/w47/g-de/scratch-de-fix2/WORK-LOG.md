# W47 DE 第二轮返修工作日志（D6，2026-11-10，返修 builder 2）

任务：只修第二轮校对 D6（§8.1，轻）— 词汇框 3 个词未出现在当版文章里。
不改 D1–D5（已验证通过）、不改 O1（P8 字号，本次不修）、不改中文数字空格与选项折行。
不改 tools/p8.py；不跑 insert.py / lint --write / git push/add/reset/stash；不提交；不碰 W43/W45/W46。

## 读过
- SOP.md §1.1 全文、§8 全文；AGENTS.md；PROOF-NOTE.md（第二轮）全文；WORK-LOG.md（第一轮返修）全文。
- 基线核对：print PDF sha256 ea41866f…112801b、web PDF 7394de61…f522、.text.md e7ba369b…bae，与第二轮校对记录一致。

## D6 修复方案（已定：植入文章，不删框词）
- 任务书二选一，以改动最小为准。选**在文章里自然植入**，理由：
  1. 只删词汇框词会留下 P5 练习 B 的问题：练习 B 方框与 Q74/Q75 的答案正是 Kerze/Stern，
     标题仍是 `WÖRTER AUS DEM TEXT`——删框词治标不治本，下一轮校对仍会以标题主张复 flag；
     植入文章后，词汇框 + 练习 B 方框 + 标题三处同时成立。
  2. 改动量相同级：植入 = 2 句（P3 一句含 Adventskalender；P5 一句含 Kerze 与 Stern）；
     删词则须同时改 P5 练习 B 标题/方框/Q74/Q75，改动更多。
  3. 流余量充足（build10.log）：P3-main 止于 y=740（底 1560），P5-main 止于 y=857（底 1080，
     周计划框在 y=1120 固定位置），各加一句（约 1–2 行）无溢出风险。
- P3（content34.py）：Advent 段末加一句：
  `Viele Kinder haben ihren Adventskalender schon zu Hause — aber das erste Türchen öffnet sich erst am 1. Dezember.`
  与 P5“第一扇小门 12 月 1 日打开”一致；不引入新事实（降临节日历 12 月 1 日开第一扇为本期已有事实）。
- P5（content56.py）：课后段首句后加一句：
  `In vielen Familien brennt im Advent eine Kerze auf dem Tisch, und auf dem Kalender leuchtet ein Stern.`
  同时支撑 Q74（Im Advent brennt eine Kerze auf dem Tisch）与 Q75（Auf dem Adventskalender ist ein Stern）。
- 不动：词汇框词表、练习 B 方框与标题、Q74/Q75 题面与键、D1–D5 全部内容、P8 任何字号。

## 构建命令（基线 = build10）
- cd core-de && ~/workspace/weekly-git/tools/venv/bin/python run.py > scratch-de-fix2/build11.log 2>&1
- ~/workspace/weekly-git/tools/venv/bin/python render.py
- ~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/webpdf.py svg/ Die-Lucerna-VOL4-de-web.pdf
- W47_BUILD_DIR=<core-de> W47_OUT_MD=<core-de>/2026-w47-de-zh-cn.text.md ~/workspace/weekly-git/tools/venv/bin/python \
    ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-de/export_text.py
- ~/workspace/weekly-git/tools/venv/bin/python verify.py
- ~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/occlusion_audit.py
- ~/workspace/weekly-git/tools/venv/bin/python ~/workspace/weekly-git/tools/p8.py extract/compare
- freeze：整 core-de 复制到 scratch 副本跑 run.py，sha256 逐个比对 8 个 SVG。

## 构建与自查（build11，2026-11-10 晚）— 零发现
- 改动文件（仅）：content34.py（P3 Advent 段加 1 句）、content56.py（P5 课后段加 1 句）、
  WEEKLY-KIT.md（§5/§6/§7/§8 更新）；其余 .py 未动；未改 tools；未跑 insert.py / lint / git 操作。
- 构建：run.py exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE。P3-main 886/1560（图止 1378.2，
  练习线 1608）；P5-main 966/1080（周计划框 1120）；最紧仍 P6-ex 2523/2560（余 37px）。
  render.py + webpdf.py exit 0；export 150 题；verify.py exit 0。
- 交付物：print 22,963,678 bytes，sha256 a2630d5a…55f18；web 2,043,343 bytes（<7MB），
  sha256 b67be538…7936；.text.md 49,799 bytes，42,393 字符，591 entries，150 题，
  sha256 1c219c84…ce86。（build10 SHAs 已废）
- D6 回归（check_d6.py / check_d6.log）：正文段内计数——P3 6/6（Adventskalender 1）、
  P5 6/6（Kerze 1、Stern 1），12/12 框词均在文章；SVG 总量交叉核对 P3 Adventskalender 3×
  （文章+框+Q41 选项 C）、P5 Kerze/Stern 各 3×（文章+框+练习 B 方框）；两新句均在渲染 SVG 内。
  其余 9 词仍在文章（计数见日志）。
- 无附带改动证明：新 print 文字层 vs 第二轮校对的 build10 baseline（scratch-proof-de2/work/print.txt）
  词级多重集差 = 仅两新句 37 个 token 增加、0 个 token 减少（textdiff11.log）。
- 机械门：occlusion_audit 0 flags（自检 6 类全触发）；p8.py extract 150/150；compare CLEAN
  （missing=[] extra_count=0 uncertain=[] keydiff=[]）；freeze 副本重跑 run.py，直接 sha256 比对 8/8。
  （freeze 工具自报 0/8 为已知收集器假象，见 KIT §6。）
- 文字层：print/web 默认模式各 50,409 字节，词多重集相同；-raw 各 49,315 字节，归一化后完全相同。
  （优于 build10：默认模式的 P6 图表区顺序差已消失。）
- P8 最小字号：PyMuPDF 实测 P8 最小 span 10.12pt（≥9.75pt）；其余各版最小 11.62–12.75pt。
- D1–D5 重测（check_d1_d5.py / check_stems.py / check_final.py）：P1–P7 题干 22.0 单位=16.5pt
  全 124 题、P8 20 题 20.5 单位=15.375pt；D2 Ligaphase P4 内 2×、D3 Buße P6 内 3×、D4 P1 导语
  4 要素在位且旧句已无、P4/P5 无 Serbien、D5 Q42 新题干在位、旧题干已无、键 42=A；
  P7 工具箱整句去空白匹配通过。注：check_d1_d5.py 的 "vor fast leeren Rängen present P1: False"
  与第一轮日志完全相同——是未 join 文本的跨行匹配假阴性，check_final.py 的 join 文本核查为 True。
- §8.1 注释词：count_gloss.py——P4 5/5、P6 6/6 在文章。
- §1.1 逐项：verify.py 风格审计 True，旧式 hex []；纸色渲染像素 (251,250,246)=#fbfaf6（4 版抽测）；
  pdffonts 全部 embedded（Newsreader、UnifrakturMaguntia、Noto Sans/Serif CJK SC）；头条 40 字符≤56；
  页脚/页码行 8/8；P6 图柱 748/561/391；图表 44+33+23=100；MUSTER 84 词；金句 8 条各恰 2×。
- 全文精读：.text.md 1185 行逐行读完；150 题逐题复核——登记表与 build10 一致（上轮独立校对已逐题
  核过），且词级差分证明除两新句外无一题一字改动；Q74/Q75 现由文章直接支撑；Q103 与新句无冲突。
- 8 版目视：print PDF 110dpi 渲染 pg-1.png…pg-8.png 逐版看完——P3/P5 新句在位、无溢出重叠；
  其余 6 版与 build10 一致，无问题。**8/8 目检零发现。**
- O1 未动（P8 段落/选项行字号），已记入 KIT §8 待协调员裁定；D1–D5、中文数字空格、选项折行均未动。
- 待办：[x] D6 修复 [x] 重渲 print+web [x] 全部机械门 [x] §1.1 逐项 [x] 8 版目视
  [x] 150 题复核 [x] D6 回归 [x] KIT 更新 [x] 本日志更新 [x] 向 parent 汇报
- 写入过程无 EPERM / 磁盘配额 / ffmpeg 失败。
