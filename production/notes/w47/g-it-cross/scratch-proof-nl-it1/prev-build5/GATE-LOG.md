# GATE-LOG — 2026-W47 nl-it · proof1 机械门实跑记录

复校员：独立复校（proof1）· 2026-11-11
版目录：`production/2026-w47/fanout-nl/2026-w47-nl-it/` · 核心：`production/2026-w47/core-nl/`
工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与任务给定一致）
TMPDIR 全程设为本 scratch 的 `tmp/`（系统 /tmp 为 512M tmpfs 且常满，未使用）。

## §0 探针与身份（任务给定，磁盘复核一致）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → 正常返回对象哈希（`9daeafb9…`）；
  scratch 探针文件 `probe.txt` 写入成功。
- SHA（磁盘实测，见 PROOF-NOTE §0）：
  - 印 PDF `a05cc4be4048cc23b357d9f0d35e03725ff68a80f082ecec46249ee42175ab3c`，12,715,556 B
  - 网 PDF `072c7f2e808ad6c93cd5469f981b14688432cab0fc8794a1260e3d5c58301fe9`，1,575,654 B
  - text.md `7652632d685a400130b3da86a3f731b59badfe035424376cf32c269b884c85d4`，46,851 B
  - 结论：三者与任务给定完全一致。

## §1 occlusion 审计

命令（自仓库根）：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/fanout-nl/2026-w47-nl-it --core production/2026-w47/core-nl/svg`
（另跑 `--selftest` 予内建自检）。结果：**0 flags，0 new flags**（`gates/occlusion.json`）。
自测通过（自测失败时工具会拒绝出报告）。
⚠️ **盲区记录**：同一轮的 D1（P7 框标题超框 65.9px）未被报——BOXTITLE 仅覆盖带描边或
`#2c2822` 填充的盒子（源码 471–473 行），奶油盒（`#f0eee5` 无描边）不在检查内；
奶油框内溢出、框标题横向溢出、降部溢出本就标称盲项，已另行实测（§2、§7）。
0 旗 ≠ 无几何问题，本轮即是一例。

## §2 正典 creambox.py 全版扫描

命令：`tools/venv/bin/python <creambox.py> production/2026-w47/fanout-nl/2026-w47-nl-it/svg --window 45`
结果：**全部盒子 fit**（`gates/creambox-all.log`）。
- P7 toolbox（HET WOORD / PAS OP! / BRIEVEN VAN LEZERS）：3 盒，最小框内余量 +12.5px、最小降部余量 +6.5px。
- P1 IN DEZE EDITIE：框内 +16.0/+9.7；其下方 +24 处标题为已知误报（下一栏目的标题，非本框溢出）。
- 误报纠正（真墨迹实测，bbox 底 − ascent，分辨降部字母）：
  - P2 EN JIJ 末行 `olandese e mandale alla redazione.`：无降部字母，真余量 **+5.6px**（日志 −0.4 为误报）；
  - P5 EN JIJ 末行 `due frasi in olandese e mandale.`：无降部字母，真余量 **+5.7px**（日志 −0.3 为误报）；
  - P6 图表盒末行 `(100 giovani)`：含 `g` 降部，真余量 **+4.7px**；
  - P2 四词盒 `po' ironica`（`p` 降部）：+6.4px；P6 VOOR OF TEGEN `En jij?`（`j` 降部）：+9.0px。
- creambox 只量纵向 clearance，不量框标题横向溢出——D1 由 PIL/像素扫描发现（§7）。

## §3 p8 compare（显式双路，--total 150）

命令：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-nl/svg/p8-toets.svg --edition-p8 production/2026-w47/fanout-nl/2026-w47-nl-it/svg/p8-toets.svg --total 150`
结果：**CLEAN**，150/150。keydiff 仅两项（`gates/p8-compare.json`；抽取见 `gates/p8-extract-ed.json` / `gates/p8-extract-core.json`）：
- #137：核心键为中文 `Sinterklaasnieuws wordt elke dag uitgezonden om 18:00 uur.` 的中文释义；
  本版键为意大利语译句 `Il notiziario di Sinterklaas va in onda ogni giorno alle 18:00.` ——
  读者语重定向的正当翻译，非缺陷。
- #138：同前，核心为中文释义，本版键 `I primi due passano ai quarti di finale.` ——正当翻译，非缺陷。
- #139/#140：与核心键逐字一致（荷兰语句）。

## §4 freeze baseline / diff

- baseline（重建核心，逐字节比对）：**8/8 SVG 字节完全一致**（`gates/freeze-baseline.log`）——
  核心未被本轮改动，冻结状态确认。
- diff（`--core-svg` 指到 SVG 目录 `production/2026-w47/core-nl/svg`，未指版目录）：
  **RC 0**，added CJK = 7（`gates/freeze-diff.json`）——全部为 U+3000 全角空格分隔符（p2–p8 各 1 处，p1 0 处），
  非新增目标语文本。
- 方法备注（O3）：`tools/freeze.py` 仅有 `baseline` / `diff` 子命令，无 `freeze_direct`。
  任务已说明此情形记为方法备注，不作缺陷。

## §5 keycheck 150/150

逐题手验（题面＋正文/图表/算术复算＋text.md 答案＋P8 印刷键三方比对），结果见 `keycheck-150.json`：
**150/150 已验，键不一致 0**。唯一键面差异为 150 题（开放写作，P8 印 `✓`，范文 81 词已数，属设计如此）。
配对题选项内容（P2 D 与 P8 F 的 a–d）已从 SVG 核对原文，字母映射正确。
题面类型分布：A2 46 / B1 73 / B2 31（与 KIT 一致，合计 150）。

## §6 印/网文字层比对

方法：`pdftotext` 按页抽取印 PDF 与网 PDF，各页逐字节比对并比对 token 多重集。
结果（`gates/txt/print-p1..8.txt`、`gates/txt/web-p1..8.txt`）：**逐页字节数相等、token 多重集差为 0**。

| 页 | 印 PDF 字节 | token 数 | 网 PDF 字节 | token 数 | token 差 |
|---|---|---|---|---|---|
| P1 | 4819 | 817 | 4819 | 817 | 0 |
| P2 | 4839 | 828 | 4839 | 828 | 0 |
| P3 | 4322 | 731 | 4322 | 731 | 0 |
| P4 | 4189 | 725 | 4189 | 725 | 0 |
| P5 | 4675 | 806 | 4675 | 806 | 0 |
| P6 | 4374 | 754 | 4374 | 754 | 0 |
| P7 | 5711 | 924 | 5711 | 924 | 0 |
| P8 | 12556 | 2372 | 12556 | 2372 | 0 |

原始逐行 diff 仅为 pdftotext 抽取顺序差异，非内容差异。
网 PDF 唯一问题为 D2（斜体丢失）：印 P1 仅 1 个斜体 span（`«de groepswinst»`，Newsreader-Italic 16.1pt），
网 PDF 全 8 页 0 个斜体 span，字体表无 Italic face，`«de groepswinst»` 在网版为
`LucernaNewsreader-Regular` 16.12pt；其余三联症症状（丢空格、闭引号脱离）未复现。

## §7 几何实测（PIL 真墨迹 + 渲染像素扫描，以渲染像素为准）

版式常量（`tools/bslib4.py`）：页宽 1950，版心右缘 RIGHT = 1862（`MX 88, CW 422.5, GUT 28`；
代码内 `# 1885` 注释为过时数字，勿信）。扫描记录见 `gates/ink.log`；整版图见 `img/p1.png`–`p8.png`。
⚠️ PIL 读数在含 em-dash/✓/U+3000 的串上比 Cairo 渲染多量约 14–17px，
以下以 110dpi 打印渲染的像素扫描为准（放大图见 `img/crop-*.png`）：

| 位置 | PIL 读数 | 渲染像素读数 | 结论 |
|---|---|---|---|
| P7 HET WOORD 框标题（D1） | 墨右缘 1927.5（超框 +65.5） | 墨右缘 1927.9（超框 +65.9） | **缺陷 D1** |
| P1 日期行 | 1862.2（+0.2） | 1861.5（框内，余 0.5） | fits |
| P4 图片署名 | 1873.2（+11.2） | 1859.8（框内，余 2.2） | fits |
| P8 头注（含 ✓ 与 U+3000） | 1880.1（+18.1） | 1863.3（≈贴边，+1.3） | fits（按 `anchor="end"` 置于 RIGHT，见 `content8.py:133`） |
| P8 Q137 首行 | 1870.5（+8.5） | 1854.5（余 7.5） | fits |
| P8 Q133 | 1866.5（+4.5） | 1852.8（余 9.2） | fits |
| P2 D 选项 c `eten voor het paard van Sinterklaas` | 1872.9 | 1872.9（超版心 +10.9） | 核心逐字节相同，裁定非缺陷（O2） |
| P7 PAS OP! 框标题 | 墨右缘 478（框右 510.5） | — | fits，余 32px |
| P7 BRIEVEN 框标题 | 墨右缘 1701.5 | — | fits，余 160px |
| P1 DE WEEK IN CIJFERS 框标题 | 框内余量 21.5 | — | fits |

## §8 P8 最小字号实测

方法：PyMuPDF 读印 PDF P8 全部 span，按渲染字号统计。结果：**最小 10.12pt**（7,447 字符为该字号），
与 KIT 一致；≥ SOP §1.1 底线 9.75pt（目标 11.25pt，让步第 4 步范围内）。不作缺陷。

## §9 弯引号全版扫描

方法：统计 SVG `<text>` 节点内 U+201C/U+201D/U+2019/U+0027。
结果：**U+201C = 0、U+201D = 0**（本版用 « »，符合刊例；P1 `«de groepswinst»` 正常）；
**U+0027（直引号）= 39 处**；**U+2019（弯引号）= 4 处**（P7 ZINNEN `un’antica` ×1，P8 头注 `l’esercizio` ×1，
P8 注 126 `all’Eredivisie` ×1，P8 注 140 `un’espressione` ×1）。
放大渲染图：4 倍图显示前两处（Noto Sans CJK SC）的 ’ 后有一整格空隙（`un’ antica`、`l’ esercizio`），
后两处（Newsreader）紧密无空隙；同字体直引号对照（P6 通栏 `un'antica`）紧密无空隙——
缺陷 D3（U+2019 在 Noto Sans CJK SC 里带全角空隙，且版内混用两种省音撇号）。

## §10 必查项原文核实（任务 a–f，逐项取证）

- (a) P1 框标题/副标题：PIL＋像素双法，P1 全部 fits（§7）；同类缺陷在 P7 复现（D1）。
- (b) P3/P5 右栏 cream box 降部：真墨迹（§2 误报纠正），全部 fits。
- (c) P7 toolbox：creambox 全版扫描（§2），P7 三盒 fit。
- (d) text.md §E type 标签：`Traduzione`／`Traduci in italiano`／`Traduci in olandese`，
  全版标签均为意大利语，无中文「翻譯」残留。
  补充核查：text.md 中 `— 答案：` ×150 为全版共用的导出格式标记——
  已发 W46 nl-it（`issues/2026-w46/2026-w46-nl-it/2026-w46-nl-it.text.md`）与 nl-de 亦为 150 次，
  核心（zh-cn）162 次含 4 处「翻譯」（核心为中文版，属正常）；
  SVG 中 CJK 字符除 U+3000 分隔符（×118）外仅有 `三色蛾`（P1 刊头蛾标，核心同有），
  无中文正文残留。非缺陷。
- (e) 网 PDF 斜体三联症：仅斜体丢失复现（D2，§6）。
- (f) ABSTRACT.txt（`ABSTRACT.txt`，278 字符单行）：`Lucerna` ✓、`VOL.4` ✓、`olandese` ✓、
  `150 esercizi` ✓、`livelli A2–B2` ✓；无 ASCII 双引号。
  全文：`Settimanale olandese Lucerna VOL.4 (16–22 novembre 2026): Sinterklaas e Pakjesavond, l'Olanda contro la Germania in Nations League, Expeditie Robinson e l'evoluzione delle tradizioni di San Nicola — lettura in olandese con 150 esercizi, livelli A2–B2, e spiegazioni in italiano.`

## §11 外部事实来源（网页核实，2026-11-11）

- Grave 全国 intocht：2026-11-14 周六 12:00 Maaskade，12:00–16:00，NPO 3/Zapp，市长 Marieke Moorman，
  Merel Westrik 主持，马 Ozosnel，Pakjesavond 2026-12-05 周六 —— vandaagingrave.nl/sinterklaas-2026；
  holland-explorer.com/sinterklaas/
- Amsterdam intocht：2026-11-15 周日，第 88 届，De Omval 10:15，Scheepvaartmuseum 11:30，
  13:00 Stopera 巡游经 Rembrandtplein/Utrechtsestraat 至 Leidseplein，市长交钥匙 —— amsterdam.org 相关 arrival 页面
  （另一来源称 13:00 为巡游开始，与报道一致；88 届经多来源确认）
- 欧冠第 5 轮：2026-11-24 周二 Real Madrid–PSV、Feyenoord–Porto —— UEFA.com 2026/27 赛程页
- 荷甲第 12 轮后：PSV 26 分领跑；Cambuur–PSV 2–5、Heerenveen–Feyenoord 5–3（2026-11-08 周日）—— fr12.nl 积分页；
  Twente–Ajax 2–2（2026-11-08 周日）—— sportradar 赛报
- Expeditie Robinson 2026：19 名参演（10 荷＋9 弗拉芒），Nicolette Kluijver 与 Edson da Graça 主持，
  Camille Vanuxem 记者，马来西亚（兰卡威），34 天，周日 20:00 RTL 4 自 2026-11-01 —— nl.wikipedia.org 相关条目
  （一来源称「30 天」，以多数/官方来源的 34 天为准，版内 34 天成立）
- 日期校验：2026-11-16 周一、14 日周六、15 日周日、21 日周六、22 日周日、24 日周二、29 日周日、12 月 5 日周六。

## §12 判为非缺陷的项（附裁决依据）

1. P2 D 选项 c 墨右缘超版心 +10.9px（§7）：与冻结核心逐字节相同，属核心固有几何；无可见框线可越，
   目视为行尾参差。裁定：本版非缺陷，核心侧记录（O2）。
2. P8 头注/Q137/Q133/P4 署名/P1 日期行的 PIL 读数超标：PIL 对 ✓/U+3000/em-dash 串多量 14–17px，
   渲染像素扫描均在版心内。裁定：工具读数误报，非缺陷。
3. creambox desc-clear −0.4/−0.3（P2/P5 EN JIJ）：0.30em 一刀切余量误报，相关行无降部字母，
   真余量 +5.6/+5.7px。裁定：误报，非缺陷。
4. freeze diff added CJK = 7：全部为 U+3000 全角空格分隔符（p2–p8 各 1）。裁定：格式分隔符，非缺陷。
5. p8 keydiff #137/#138：读者语重定向的正当意大利语翻译。裁定：非缺陷。
6. P8 键 #150 为 `✓`：开放写作题，无唯一答案；范文 81 词已数。裁定：设计如此，非缺陷。
7. text.md 标题含 `2026-W47`：与冻结核心及已发 W46 全版一致的模板格式，需模板层决定（O1）。
8. P3/P6 中部留白：与核心版式一致（短文章所致），非缺陷。
9. 弯引号 P8 注 126/140（Newsreader 字体）：放大图紧密无空隙，本身无碍；但与直引号混用，
   随 D3 一并改为直引号。
10. P5 配图署名 `Elise lovenko / Unsplash`：属核心侧图片资产（图中为通用热带海湾，与马来西亚主题相关），
    本轮未独立核实该署名真实性；不作本版缺陷。
