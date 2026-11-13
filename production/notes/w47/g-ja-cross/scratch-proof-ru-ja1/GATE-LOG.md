# GATE-LOG — W47 ru-ja proof1 机械门实跑证据

校对员：独立 proofreader（proof1）。日期：2026-11-11。版目录：`production/2026-w47/2026-w47-ru-ja/`；核心：`production/2026-w47/core-ru/`。工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383` 已验）。全部日志与裁图在 scratch 目录（`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-ja1/`）；`TMPDIR` 全程指向 scratch 下 `tmp/`（系统 /tmp 512M 且常满，未用）。

## §0 身份核对

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0。可写探针已写 scratch `probe.txt`（2026-11-11T11:07:39Z）。
- 印 PDF `Lucerna-VOL4-ru-ja.pdf`：SHA-256 `929a5c4786f256cb194cdab9cd7aafd0db1b8331e73ed8b0d1c1dcaf44b2a06e`，27,404,856 字节，8 页，1462.5×2025 pt——**与任务一致**。
- 网 PDF `Lucerna-VOL4-ru-ja-web.pdf`：SHA-256 `fbfb35d3d34e7e196c43254db3995e78d84224f5da79fdeeb48fff7a0436d233`，3,683,942 字节（<7MB），8 页——**与任务一致**。
- text.md `2026-w47-ru-ja.text.md`：SHA-256 `c119d8f8e191f5760aa777f8e53517272654c30524ff5ef4116588603a5109c3`，64,451 字节，838 行——**SHA 与任务一致；字节数与 KIT §5 称的 58,308 不符（见 PROOF-NOTE O8）**。印/网字节数与 KIT 完全一致。
- KIT 内容摘要（仅作交叉核对，不作证据）：VOL.4，刊期 11 月 16–22 日；150 题（P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38；A2 50 / B1 76 / B2 24）；范文 97 词；金句 8 句；P8 Morozko 图按条件跳过；42 TEXTX 遮挡旗标称 all-clear。

## §1 Occlusion 审计

- 命令：`tools/occlusion_audit.py`（自测：全部植入类均触发、干净对照静默）。
- 结果：**42 flags，全部 TEXTX，0 LINEX / COVER / FOOTER / EDGE / BOXTITLE**——与 KIT 计数一致（`occlusion.log`、`occlusion.json`）。
- 逐一像素裁决（自写 `adjudicate_mine.py` + `adjudicate5.py`/`adjudicate5b.py`，1:1 映射、显式配对；fan-out 的 `adjudicate_ru.py` 假设卡片 1800 宽且按首 match 解析 run，不可盲用）：**42/42 CLEAR，0 真实**（`adjudicate-mine.txt`）。
  - 37 处由 gap 测试清除（gap 2–18px）。
  - 5 处初次脚本取错 B-run 后重裁，均 CLEAR：P4 `Россия` vs `,` gap 9px（裁图 `adj-p4-rossiya.png`）；P5 `смартфоны` vs `,` gap 12px（`adj-p5-smartfony.png`）；P7 `поступило` vs `:` gap 8px；P7/P8 栏目标题（`ЯЗЫК　ことば`、`ОТВЕТЫ　テストと答え`）——所谓“重叠”为行首 U+3000 全角空格使 gloss 墨水盒左缘外扩的幻影（PIL `ink_box('　ことば')` 左缘 = tspan x 251.0），裁图 `adj-p7-band.png` / `adj-p8-band.png` 显示宽阔净空。
  - 全部 42 处为已知的相邻 tspan 墨水盒误报类（逗号/句号/引号，盒重叠 3–5px，字形不相触）。

## §2 正典 creambox 全版扫描

- 命令：`tools/creambox.py`（直接传 SVG 路径；无 `--help`，`--help` 会被当作文件路径）。日志 `creambox-all.log`，32 盒。
- 结果：**无任何盒有真实框底溢出**。全部负余量盒均为 BELOW-WINDOW +28/+32/+34/+37——下一块标题或通栏行（P1 `А ВЫ?/СЛОВО НЕДЕЛИ` +37/+34；P2/P3/P5 节头 +37；P2 y=1618 盒 +32 为通栏行 `Запомните: в оттепель идёт мокрый снег…`，已在 SVG y=1800 核实；P6 y=1344 日带盒 +28 为图例行 `Светлое — рабочие дни (16–20 ноября) · жёлтое — выходные (21–22 ноября) · праздников посреди недели нет`）。
- P7 toolbox：**3 盒，最小内距 +11.9，最小降部余量 +5.9**（全部为正）。
- P2 y=795 盒（底 1159.0）：盒内余量 +5.0，desc-clear −1.0——**像素核实 CLEAR**：底边 +12px 内无墨水，无墨水触底边。−1.0 是 0.30em 降部余量作用于 CJK `の1文。`（20px Noto Sans CJK SC），该串无降部墨水。(b) 类未复现。
- P1 y=1874 盒「溢出 +8px」（`pixel_verify.py`）：实为设计的橄榄色横线 `<line y1=2312 stroke #46581f>`（裁图 `crop-p1-box1874-bottom.png`）——误报，非文字溢出。

## §3 p8 compare

- 命令：`p8.py compare --core-p8 core-ru/svg/p8-test.svg --edition-p8 … --total 150`（日志 `p8-compare.log/.json`）。
- 结果：**CLEAN，150/150，missing=[]，extra=0，keydiff=[137, 138, 139, 140]**——E 节翻译题 4 键，正确指向日语。`p8.py extract`：noted set 150/150（`p8-extract.log/.json`）。

## §4 freeze

- 命令：`freeze.py baseline --build core-ru --core-svg core-ru/svg`：**8/8 SVG 字节一致**（rc=0），core SVG 未改动（`freeze-baseline.log`，基线副本 `freeze/`）。
- 命令：`freeze.py diff --core-svg core-ru/svg --edition-svg ru-ja/svg`：新增 CJK 共 2,521（日语讲解层）；**新增含西里尔串 = 0（8 页全 0）**——无新增俄文目标文本。移除的西里尔串为讲解层替换（P6 `УЧЕБНЫЕ ДАННЫЕ` → 日语 `練習用データ`；P7 `Три темы, три уровня` → 日语；P8 Morozko 图注——见 O4）（`freeze-diff.log/.json`）。
- 方法备注：`tools/freeze.py` 无 `freeze_direct` 子命令（仅 baseline/diff），记为方法备注，非缺陷。`--strict-cjk` rc=1 为预期（读者为日语，目标非日语），非失败（`freeze-diff-strict.log`）。

## §5 keycheck 150/150

- 文件 `keycheck-150.json`：150 项，每项含题干、级别、节、行内键、答案附录键、印 P8 键、两项交叉核对、 verdict。
- 三源交叉：行内键 vs 答案附录 **0 差异**；行内键 vs 印 P8 键 **0 差异**（Q150 除外：印键为 `✓` 范文标记，依设计；其 text.md 键为自由写作说明）。
- 编号 1–150 在三源中连续无缺；配对组键核实：25–28 b/d/c/a、39–42 b/d/c/a、57–60 b/a/c/d、75–78 d/b/a/c、141–144 c/d/a/b。
- 级别重算：单题行 A2 46 / B1 64 / B2 20，加 5 组配对共 20 题（A2 +4、B1 +12、B2 +4）= **A2 50 / B1 76 / B2 24**，与 KIT 一致。
- 范文 H 逐词计数：**97 词**（空白分词），简报 80–100 ✓。
- Q21 1946、Q62 `будет`、Q92 `пять`、Q140 增 `みなさん` 均接受（核心原文/常规问候等效；ru-en1 O5 同类）。

## §6 boxtitle 逐个实测

- 方法：`boxtitle_scan.py`，PIL 真墨水（`occlusion_audit.ink_box`）。日志 `boxtitle_scan.py/.log`。
- 结果：全部奶油盒标题带贴合；最紧 P1 y=1296 盒、行 y=1378、墨水右缘 1840.0（距 1862 有 22px）；P7 y=992 盒、行 1838.5（23.5px 余量）。**(a) P1 框标题/副标题溢出未复现。**

## §7 框右缘与全页像素扫描

- `boxright_scan.py`：无任何盒内行距盒右缘 8px 以内，无超界。
- `pixel_verify.py` 全页最右墨水扫描：P1/P3/P4/P5/P6/P7 最右墨水 1861（界内）；**P2 最右 1869–1870、P8 最右 1869**（O1/O2）。`colspill_scan.py` 中栏溢出扫描有系统性误报（多栏流动行、通栏标题/注脚），唯一真实命中即 O1/O2 两行。

## §8 印/网文字层比对

- 方法：PyMuPDF 逐 span 比对 + `pdftotext` 全文比对 + 200dpi 裁图（`print.txt`、`web.txt`、`webcheck-*.png`）。
- 印/网文字层均 >0（pdftotext 58,347 vs 58,411 字节）；字符多重集仅差网版多 59 空格 + 5 换行（分割噪声），其余一致——**除 D1 斜体三联症**：
  - 印 P1 `«чёрная пятница»` 为 NotoSerif-MediumItalic 16.1pt，span `чёрная пятница`（词尾包围盒 x 1088.0–1222.8，`»` 紧贴于 1220.6）；网 PDF 同词 span 文字为 `чёрнаяпятница`、字体 LucernaNotoSerif-Regular、`»` 在 1220.6 而词末 1218.9（gap 1.7pt，pdftotext 读作 `«чёрная пятница »`）；网 PDF 全文档斜体 span 数 0、字体表无斜体面。裁图 `webcheck-print-word.png` vs `webcheck-web-word.png` 目视确认。
  - 复现 ru-en D3 exactly；程序先例（ru-en3 注）为 italic-patch 重建网 PDF。

## §9 P8 最小字号实测

- 方法：PyMuPDF 读印/网 PDF 全部 span 字号（不信 KIT 数字——KIT 的“P8 min font”是配置 px 不是渲染 pt）。
- 结果：**印/网均为 9.75pt** = SOP §1.1 下限（≥9.75）。KIT 的数字此次为真。

## §10 弯引号扫描

- U+201C/U+201D 恰 1 对，U+2019 = 0，全版无直引号。该对为 P7 y=552.64 `«на “чёрной пятнице”».`——与 core 一致的故意保留的内层引号例外。通过。

## §11 §1.1 目视抽查（8 版卡片逐版目视）

- 纸色：像素采样 (251, 250, 246) = **#fbfaf6 精确**（P1 两处采样一致）。
- 徽章：A2 #5c6e30（P2 16,379px）、B1 #46581f（30,402px，像素采样 (70,88,31) 精确）、B2 #37402f 均在版；金色设计色 #d4af37 = 0px、#c9a227 = 0px（P8 暖棕像素为照片/抗锯齿中间色，非金色设计色）。
- 刊头 `Lucerna`、页脚 `Lucerna ロシア語週刊 VOL.4 本文はロシア語 解説は日本語` + `Nページ（全8ページ）`：8 版齐全。
- 金句 8 句逐句出自正文、页码标注全对（P1×2、P2×1、P3×1、P4×1、P5×1、P6×2）；P6 图表 38/26/18/18=100%、柱长成比例（38%>26%>18%=18%），附日语「練習用データ、非真实统计」披露；P6 日带 16–20 浅色工作日、21–22 黄色周末，图例行完整；P7 纠错 4 条语法全对；读者来信栏编辑示例 + 俄日双语披露。
- P6 C 节标题位置核实：93–96 属 B 节（text.md 480 行 `## B · ПО ТЕКСТУ` 下、493 行 C 节头之前），印 P6 栏流与 text.md 节分组一致，非标题错位。

## §12 外部事实来源（2026-11-11 浏览器核实）

- **俄超第 14 轮 8 场比分**：Sport-Express、86.ru、sports.ru、championat.ru、mosregtoday.ru、Sportradar、MK Самара（samara.mk.ru）、moneyball-odds.com——8 场全部核实：Локомотив–Рубин 0:1、Факел–Динамо 1:2（久卡温 90+1 绝杀）、Ахмат–Родина 1:0、Краснодар–ЦСКА 4:2、Крылья Советов–Оренбург 2:0（拉赫曼诺维奇 4'、穆卡伊洛夫 70'）、Спартак–Акрон 2:1、Зенит–Ростов 2:2（科马罗夫 83' 扳平）、Балтика–Динамо Мх 0:1（8 日 20:45，收官战）。总进球 1+3+1+6+2+3+4+1 = **21** ✓。积分：Зенит 31（10-1-3, 32-15）、Динамо 31（10-1-3, 23-13）、Спартак 29、Краснодар与 ЦСКА 各 26、Локомотив 15 名降级区 ✓。
- **15 轮赛程**：core-ru 复校已与 sports.ru、rusfootball.info、Sport-Express 三家核对 8 场时间一致（20 日 19:30、21 日 13:00/15:15/17:30/19:45、22 日 14:00/16:30/19:00）；本轮未重复核对，采信该核实。
- **学生日**：calend.ru、BSTU（w.lzbtg.com）、kaznu.kz——1946 年 11 月 17 日布拉格世界学生大会确立（俄文通说）；更严格历史：1941 年伦敦首次宣布，1946 年布拉格确认。见 O9。
- **节日/日期**：11 月 18 日严寒老人生日（大乌斯秋格）、19 日高校教师日、20 日世界儿童日、21 日税务工作者日、22 日心理学家日、16 日国际宽容日、1 月 25 日塔季扬娜日——均为俄罗斯法定/国际纪念日；11 月 29 日母亲节为 11 月最后一个周日。
- **黑五**：core-ru 复校已核对 360.ru、raiffeisen-media、itzine、RIA Новости等多家口径——日历 27 日周五、网一 30 日周一、俄罗斯自 2013 年起办黑五、Ozon 11 月 13 日–12 月 2 日、Wildberries 11 月 16–30 日、М.Видео自 12 日、Яндекс Маркет预热 25–27 日、Lamoda 27–30 日、11.11 回顾（Ozon 10 月 22 日–11 月 12 日；2025 年 11 月 11 日单日超 1,440 万单，vc.ru 引 Retail.ru / Ozon 官方战报）一致；本轮采信该核实。
- **电影 11 月 19 日五部首映**：core-ru 复校已与 sobaka.ru、ngs22、kinoafisha.info、lifehacker、mk.ru 多家核对——«Рокки — это я»（史泰龙传记，彼得·法雷利）、«Бумажный тигр»（詹姆斯·格雷，刑侦剧，戛纳 2026）、«Увидеть всё»（A24，伊丽莎白·霍尔姆斯 / Theranos 纪录片）、«Дедмобиль»（尤里·斯托亚诺夫喜剧）、«Колотун и Волшебное королевство»（家庭奇幻）一致；本轮采信该核实。
- **星期**：`date`（Europe/Moscow）逐一核实——11 月 4 日周三、6 日周五、7 日周六、8 日周日、11 日周三、12 日周四、13 日周五、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、26 日周四、27 日周五、29 日周日、30 日周一、2025 年 11 月 11 日周二、2026 年 1 月 25 日周日。11 月工作日 20 天 / 休息日 10 天 ✓（4 日民族团结日假日 + 9 个周末日）。
- **VOL.3 更正属实**：已发 W46 俄文版 P4 为第 14 轮前瞻表，仅列 7 场赛程，无 «Балтика»–«Динамо» Мх 一行（core-ru 复校核实）；W47 P4 更正真实，承诺兑现。

## §13 判为非缺陷的项

- 42 occlusion TEXTX flags：§1，逐一像素裁决 42/42 CLEAR。
- Creambox 负余量盒（+28~+37）：§2，全部为下一块标题/通栏行/图例行，非溢出。
- P2 y=795 盒 desc-clear −1.0：§2，像素核实无墨水触底（CJK 无降部墨水）。
- P1 y=1874「+8px」：§2，设计橄榄色横线。
- P7 toolbox：§2，+11.9/+5.9 通过。
- 弯引号 1 对：§10，故意保留的内层引号例外（core 一致）。
- P8 最小字号 9.75pt：§9，等于下限。
- 窄词距（O3）：空格存在、字形不相触、core 像素一致。
- Morozko 图注行（O4）：导出器无条件输出、图片有条件跳过；图注事实无误。
- `— СТРАНИЦА? —`（O5）：导出器占位 artifact，印品为真实分隔。
- `·` 分隔符（O6）：冻结标点，家具合规。
- §1.1 (a)(c)(d)（O7）：无首字下沉、INK #302c28、Newsreader 混排——core-ru 复校同款文档注记，无读者可见损害。
- Q21 1946（O9）：俄文通说，核心原文。
- core-ru D-1（P4 `играет с ЦСКА`）：当前 core 与本版均为 `победил ЦСКА 4:2`，已在核心侧修复，本版不携带。
- P1 `От редакции Lucerna` 等词距：见 O3。

## §14 方法备注

- `creambox.py` 直接传 SVG 路径（无 `--help`）。
- `freeze.py` 无 `freeze_direct` 子命令（仅 baseline/diff）；`--strict-cjk` rc=1 为预期（读者日语）。
- `ink_box`（`occlusion_audit.py`）为超采样，且将行首 U+3000 计入墨水盒（左缘 = tspan x）——PIL/SVG 度量与渲染不一致时，以渲染卡片像素为准（如 O2）。
- fan-out 的 `adjudicate_ru.py` 假设卡片 1800 宽、按首 match 解析 run——未盲用；本次裁决用自写 1:1 映射 adjudicator。
- 两次 exec 调用中途被服务重启打断（网 PDF 检查渲染 + span dump）；PNG 已落盘，先核查落盘结果再重试，未重复执行。
- 严禁对含 base64 内嵌图片的 SVG 用 `grep -o`（或无界 dump）——此前两次命令向 transcript 灌入约 200KB base64；本次改用 `grep -c`、Python 截断、目标模式。
- 卡片为 builder 渲染图；像素检查均在 builder 卡片上进行。本轮未自行用 CairoSVG 重渲染（同源 siblings 有此额外检查；本次像素证据已充分）。
