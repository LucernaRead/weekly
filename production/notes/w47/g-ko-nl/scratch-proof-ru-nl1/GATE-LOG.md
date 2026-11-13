# GATE-LOG — 2026-W47 ru-nl proof1（机械门实跑证据）

- 版：`2026-w47-ru-nl`（Russian × Dutch），VOL.4
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`；creambox 正典
  `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与任务一致）
- TMPDIR 全程指向 scratch 下 `tmp/`（未用系统 /tmp）

## §0 身份核对（磁盘为准）

| 文件 | 任务 SHA | 磁盘 SHA | 字节数 | 结论 |
|---|---|---|---|---|
| `Lucerna-VOL4-ru-nl.pdf`（印） | `59d16202…fa4352` | `59d16202fb04c4b912c6cb65c69052d160fee0d7e7a228d5a53d015ed8fa4352` | 21,285,839 | 一致 |
| `Lucerna-VOL4-ru-nl-web.pdf`（网） | `1c860fc7…504b4c` | `1c860fc77a9a1b2ad313bf6fdd846170fbf0850942595bfe6aaf19196a504b4c` | 3,348,435 | 一致 |
| `2026-w47-ru-nl.text.md` | `8a2d9ee6…bf7b50` | `8a2d9ee60083f503159f8de5a7df44ad38b4e61096149dc45ffa9f2307bf7b50` | 63,984 | 一致 |

探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…`，RC=0；
scratch 可写验证 `probe.txt` = `probe-ok`。版目录在 git 中为 untracked（`?? production/2026-w47/2026-w47-ru-nl/`），
未做任何 commit/push/改动。

## §1 Occlusion 审计（`tools/occlusion_audit.py`）

- 先跑 `--selftest`：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`。
- 全版实跑：`42 flags {'TEXTX': 42}`，0 COVER / 0 LINEX / 0 FOOTER / 0 EDGE / 0 BOXTITLE，RC=1（有标记故非零）。
- 逐条像素裁定：42 条全部裁图目视（`adj/` 11 张 contact sheet），均为相邻字形墨迹盒轻触
  （引号 `«»`、逗号、句号、`!`、`?`、`)` 与相邻词，3–5 px），渲染干净，无视觉缺陷。
  **42/42 CLEAR，0 真缺陷**。日志 `occlusion.log`，JSON `occlusion.json`。
- 盲区补充（审计对奶油框内溢出/框标题溢出/横向溢出/降部溢出失明，另行实测）：见 §2、§3、§6；
  其中横向溢出实测出 D1/D2（见 PROOF-NOTE）。

## §2 Creambox 全版扫描（正典 creambox.py，+45px 窗口 + 逐行 clearance）

- 命令：`creambox.py svg/p*.svg` → `creambox.log`，RC=0。共 32 个奶油框（inside-only 行）。
- P7 toolbox：`P7-TOOLBOX summary: 3 boxes, min inside clearance +11.9, min desc-clear +5.9`——通过。
- 14 个窗口 clearance 为负的框：逐个核对 inside-only 行，全部是框外标题误报
  （框内末行 clearance +15.9…+47.7、desc-clear +10.2…+41.6；下方标题在 +28…+37px），无真溢出。
- 唯一 inside-only desc-clear 为负：P2「А ВЫ?」框（y=795，bottom=1159.0），末基线 1154.0，
  clearance +5.0、desc-clear **−1.0**。PIL 真墨实测（Noto Sans CJK SC 20px）：
  末行 `één voor Grootvader Vorst.` 无降部字母，墨底 = 基线 +0 = 1153.98，框底上方 5.0px；
  卡片像素扫描：框 x 范围内 y≥1154 有 0 深色像素；2× 裁图 `p2-ayvy-boxbottom.png` 目视框内留白清晰。
  **结论：0.30 代理误报，非缺陷**。(b) 类未复现。
- 其余框最小 desc-clear 为 +10.2px（P2 词表框）。

## §3 横向溢出 / 框标题（PIL 真墨 + PDF span + 200dpi 像素扫描三法）

- 版心：左右 88px（绿带 rect x=88 w=1774，横线 x1=88 x2=1862），右边界 **1862.0**；页宽 1950。
- 全版 advance 扫描：仅 3 处 run 超 1862.5；PIL 真墨 + 像素扫描逐一核实：
  - **P1 y=1660 `СЛОВО НЕДЕЛИ WOORD VAN DE WEEK`**：墨迹最右 x=**1876**（y 1643–1659、x 1863–1876 计 137 深色像素），
    超右边界 **14px**，标题下横线止于 1862。→ **缺陷 D1**（本版，见 PROOF-NOTE）。
  - **P2 y=2162 `b. Международный день студента`**：墨迹最右 x=**1870**（y 2149–2161、x 1863–1870 计 51 深色像素），
    超右边界 **8px**。核心同基线 run 逐字节一致。→ **缺陷 D2**（核心预存）。
  - P8 y=1302 答案头右注：墨迹最右 x=1864，仅超 2px（抗锯齿量级），裁定非缺陷（O2）。
- 框标题（boxtitle）逐个实测：895 条框内文本，右缘超框者 **0**；最紧 clearance −18.9px（即框内余 18.9px）。
  见 `boxtitle.json`。
- 全卡片最右深色像素：P1 1876（D1）、P2 1870（D2）、P3–P7 1863、P8 1864；最左均为 88；最下深色 y=2627
  （页脚基线 2624 的降部，页脚带豁免）。

## §4 P8 compare（显式 --core-p8/--edition-p8）

- 命令：`tools/p8.py compare --core-p8 production/2026-w47/core-ru/svg/p8-test.svg --edition-p8 production/2026-w47/2026-w47-ru-nl/svg/p8-test.svg --total 150`
- 结果：`core: 150 noted; edition: 150 noted; status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`，RC=0。
- keydiff 裁决：137–140 恰为 E 节四道 RU→荷兰语翻译题的键，按设计译成荷兰语；其余 146 键与核心逐字节一致
  （另经 JSON 直接比对确认）。**通过**。
- `p8.py extract` 独立提取本版 P8：`noted set = 150 of 150`，键见 §8。

## §5 Freeze（baseline + diff）

- `tools/freeze.py baseline --build production/2026-w47/core-ru --core-svg production/2026-w47/core-ru/svg`：
  `baseline: 8/8 SVGs byte-identical`，RC=0；核心 SVG 跑前跑后重哈希无变化。**通过**。
- `freeze.py` 无 `freeze_direct` 子命令（仅 baseline/diff，`--help` 已核）：记为方法备注，非缺陷。
- `tools/freeze.py diff --core-svg production/2026-w47/core-ru/svg --edition-svg …/2026-w47-ru-nl/svg`，RC=0：
  - 新增西里尔字母：**8 页全部 0**——核心正文未被改动。
  - 新增 CJK：共 6 个，全部是 U+3000（全角空格，SOP §1.1 规定的分隔符）；逐页核查本版可见文本 CJK
    全部仅为 U+3000（P1 21、P2 16、P3 13、P4 16、P5 13、P6 15、P7 12、P8 15），0 汉字；
    P1 另有 `三色蛾` 仅在 moth `<title>` 元数据中（与核心一致）。
  - 删去的西里尔字母逐条裁定：P6（11 串）为图表免责句的俄语原文，被荷兰语译文替代，
    P6 SVG 中已核实荷兰语免责句存在（`Dit is een oefenenquête van de redactie — geen echte statistiek.`）；
    P7（4 串 `Три/темы/три/уровня`）为副标题「三级三主题」的俄语原文，被荷兰语 `Drie niveaus, drie thema's` 替代；
    P8（20 串）为核心 P8 的「Морозко」插图图注及 P8 栏目标题的俄语原文——插图按构建条件跳过（见 §9 非缺陷项）。
    全部属于讲解层替换，无核心正文丢失。

## §6 印/网文字层比对 + P1 斜体三联症

- `pdftotext`：印 57,771 字节，网 57,822 字节，均 >0；非空白字符多重集 **31,014 = 31,014，完全相等**；
  字级差异仅为 pdftotext 对窄空格连接处的切分噪声。
- 斜体三联症（ru-en D3 同类）：
  1. 斜体词 text layer 丢空格：**否**。网 PDF 中 `чёрная пятница` 10 次、0 次 `чёрнаяпятница`；印/网一致。
  2. 闭引号脱离：**否**。`»,` 印/网各 4 次，贴合。
  3. 斜体丢失：**是**。`pdffonts` 网 PDF 63 字体中 italic 为 **0**；印 PDF 含 `Newsreader16pt-Italic`、
     `NotoSerif-MediumItalic`。同坐标渲染并排对比 `italic-sidebyside.png`（上网/下印）：
     网 PDF 的 `«чёрная пятница»`（P1 本周词，SVG y=1712）为直立体，印 PDF 为斜体。→ **缺陷 D3**（机制）。
     网 PDF 建于 2026-11-11 05:15 UTC，早于修复提交 40963281（09:39 UTC）。
- 字体核查：网 PDF <7MB（3,348,435 字节），8 页。

## §7 P8 最小字号（PyMuPDF 实测，不信 KIT 数字）

- 印 PDF P8：最小字号 **9.75 pt**（393 个 span，`Newsreader16pt-Regular`），其余 10.35/10.88/11.25…pt。
  等于 SOP §1.1 下限 9.75pt，不低于。**通过**（KIT 的 9.75pt 数字与实测一致）。

## §8 Keycheck（150 题逐题手验）

- 见 `keycheck-150.json`：150/150 pass。方法：text.md 每题题干对照正文/表/图/日历手验；
  印刷键由 `p8.py extract` 提取，与 text.md 答案节逐题比对 0 不符（Q150 开放题表述同义，已注明）。
- 关键算术复核：P4 表 8 场进球 1+3+1+6+2+3+4+1=**21**；模型文逐词计数 **97 词**（brief 80–100）；
  匹配题逐对核对（P2 25–28、P3 39–42、P4 57–60、P5 75–78、P8 141–144）。

## §9 弯引号扫描

- SVG 可见文本：全版仅 1 对 U+201C/U+201D，在 P7 错误诊所 `«на “чёрной пятнице”»`——
  任务注明的故意保留；U+2019 全版 **0**。text.md 同样仅此 1 对。**通过**。

## §10 判为非缺陷的项

1. Occlusion 42 条 TEXTX：全部像素裁定 CLEAR（相邻字形轻触，见 §1）。
2. Creambox 14 个负窗口 clearance：全部为框外标题误报；P2「А ВЫ?」框 desc-clear −1.0 为代理误报（真墨无溢出，见 §2）。
3. P1 刊头副标题行 `ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ`：
   词间以 CJK 空格 run 排版，墨迹间隙 3–6px（像素列扫描实测，每处词界均有间隙），窄但存在；
   且与核心逐 run 一致（核心冻结）。非缺陷。
4. 正文窄空格（西里尔词间 CJK 空格 run，如 P2 `Профессиональные праздники` 墨迹间隙 6px）：系统性排版特征，
   核心同然；误读风险经像素实测排除。非缺陷。
5. P2 Yuon 图注 `Картина: Константин Юон — общественное достояние`：冒号后主格为正确的图注格式；
   低倍误读为 `Константина Юон` 已由 3× 裁图 `p2-credit-zoom.png` 与 SVG run 澄清。非缺陷。
6. `— СТРАНИЦА ? —`（text.md 答案节分隔符）：核心 `core-ru` 的 text.md 第 668 行同款，导出器共享格式。非缺陷。
7. `text.md` 末尾「Морозко」图注行：核心同款导出器格式。非缺陷。
8. P8「Морозко」插图缺失：构建条件跳过（键表末行 y=2374.10），与 W46 ru-nl 相同；键表完整到 Q150。非缺陷。
9. P6 图表俄语免责句被荷兰语替代、P7 副标题俄语被荷兰语替代：讲解层正常翻译（见 §5）。非缺陷。
10. P7 B2 gloss `синоптики обещают de weermannen beloven`：W46 TM 沿用值；`weerman` 为荷兰语实词（气象主播），
    非错误。非缺陷。
11. P8 右注 2px 超界（x=1864）：抗锯齿量级。非缺陷（O2）。
12. `freeze_direct` 无此子命令：工具现状，方法备注。非缺陷。

## §11 外部事实来源

- 第 14 轮 8 场比分、83 分钟扳平、90+1 制胜球、«Балтика» 20:45 开球、积分（31/31/29/26/26、15 名降级区）：
  Forbes.ru 2026-11-09 综述（`forbes.ru/sport/571957-zenit-ostupilsa-krasnodar-vydohnul-obzor-14-go-tura-rpl`）、
  sports.ru 14 轮赛程/结果页、rusfootball.info 2026/27 往绩中心——三处比分逐场一致；
  核心 KIT 亦引 sports.ru / Forbes / rusfootball.info 为来源。另经搜索核实 «Родина」为 2026/27 赛季俄超球队。
- 日期/星期：`TZ=Europe/Moscow date -d` 逐日核验（16 Mon、17 Tue、18 Wed、19 Thu、20 Fri、21 Sat、22 Sun、
  27 Fri、30 Mon、12 Thu、2026-11-01 Sun、2026-11-04 Wed）。
- 其余事实（学生日 17/11、Ded Moroz 生日 18/11 与 Великий Устюг、Татьянин день 1/25、电影 19/11 五首映与 26/11
  「Голодные игры」、11 月 4 日公众假、母亲节 11/29 周日）与正文内部及常识一致，未发现矛盾。

## §12 未跑 / 未覆盖

- 无。任务列出的 9 项机械门 + 5 项必查项全部实跑。未改动任何源文件，未 commit，未 push。
