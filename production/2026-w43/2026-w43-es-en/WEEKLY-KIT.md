# La Lucerna · 西班牙语周报 VOL.1 — 英语讲解版 (ES × EN) WEEKLY-KIT

> 本文件是 VOL.1 西班牙语核心的**英语母语读者版**说明:同一核心(西班牙语正文冻结),
> 讲解层全部改为英语。核心首发配对为中文讲解版(`weekly-report-es-vol1/`),
> 本版为矩阵展开的 ES × EN 单元格。母版 SOP 见 `files/weekly-report-SOP.md`。

## 0. 本版身份

- **配对:目标语 = 西班牙语 · 读者母语 = 英语**(one-to-one,无中间语言)。
- **刊头标识(P1,刊名下方,粗体橄榄色)**:
  `TEXT IN SPANISH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`
- **页脚**:`La Lucerna · Spanish Weekly VOL.1 · Text in Spanish · Explanations in English` / `Page n of 8`。
- 期次与周次与核心完全一致:VOL.1 · 周一 2026-10-19 至周日 2026-10-25;
  主题不变:周日凌晨换钟 + 国家德比 21:00 Camp Nou + F1 奥斯汀同撞一夜。

## 1. 与核心版的差异(仅讲解层)

- 全部讲解改英语:Notes 词汇注、栏目标题(西语 · English)、每题题型名、ABCD 分区说明、
  图表读法、常见错误注、读者来信说明、下期预告说明、**P8 全部 150 条答案简析**。
- 词汇注前缀:`注 |` → `Note |`;P8 答案注分隔:`——` → `—`。
- **裁定 1(P8 E 区翻译题方向)**:核心版 E 区为「西译中/中译西」。本版按读者母语重定向:
  第 137、138 题答案改为英文译文(`On Sunday we sleep one hour more.` /
  `Monday is a public holiday in nine communities.`);第 139、140 题题干改为英文源句
  (答案仍为西语,与核心一致)。其余 146 条答案与核心逐字一致(见 §4 核验)。
- **裁定 2(P7 示例信标点)**:信内全角括号 `（carta de ejemplo…）` 改为半角 ASCII 括号;
  信件内容、人名 Mei、地点 Pekín 不变(西语正文)。
- 图片、图注、署名与核心版**逐字节一致**(SVG 图片元素 href + 位置逐页比对相同);
  刊用图片与核心版同为 3 张(另有 1 张为核心素材库备用图,未刊用;署名见核心 KIT §8)。

## 2. 规模(与核心同口径实测:8 张 SVG 全部文本元素拼接长度)

- **全文可见字符 43,729**(核心中文讲解版 39,131;增量来自英语讲解普遍长于中文)。
- **练习 150 题**,与核心完全同构:分布 P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8(写作)38;
  级别 A2 52 · B1 70 · B2 28;题型 Sentence completion 48 · Multiple choice 47 · Cloze choice 13 ·
  Vocabulary matching 12 · Sentence transformation 10 · True or false 8 · Sentence building 7 ·
  Translation 4 · Writing 1(计数由注册表脚本实测,非手填)。
- 版式:8 页,1950×2700,零 FLOW OVERFLOW / HEAD TOO WIDE 警告。

## 3. 版式参数改动(仅本版构建副本 `hidden_files/weekly-report-es-en-build/`,核心构建目录未动)

1. P6 练习字号 19 → 18.5、行距微调:英语题型名更长,原参数下 P6 练习区溢出,改后归零。
2. P8 答案行距 1.21 → 1.16、字号 14 → 13.5(后微调 1.14):英语简析更长,防溢出;
   末行基线 2591.9,与核心版 2588 同量级(页脚线 2580、页脚文字 2624,版面观感一致)。
3. P1 黑带右行字号 24 → 20:英文行与左侧西语大标题在原字号下重叠。
4. P1「LA SEMANA EN CIFRAS · Numbers」与 P2「LA FRASE PARA RECORDAR · Remember」(tsize 19.5):
   英文小标题原案超盒宽,缩短并实测 ≤ 盒内宽。
5. P3 栏目标题「RECORDAR JUNTOS · Remembering」字号 23(原 24 标题过宽)。
6. **P7 右栏盒高公式修正(重要)**:核心构建代码的「常见错误」盒高公式系统性低估
   (按平均行高估算),导致盒内第 4 条内容被下方盒子盖住——**核心中文版 P7 实测同样中招**:
   其错误栏第 4 条《La gente son felices》在成报上不可见(被「本周生词」盒覆盖)。
   本版将公式换成与绘制循环逐项一致的精确模拟,并把 4 条英文注各压缩为 1 行、
   单词/来信两条英文注各压缩为 2 行、盒间距 26 → 16:三盒内容全部 containment 实测通过
   (内容末基线距盒底 42.5 / 4.4 / 4.4,与核心版设计留白一致),栏底 1664,距 FRASES 横线 22。
   **核心版该缺陷不在本任务冻结范围内,仅在此登记,待主线决定是否回补核心版。**

## 4. 零差异核验(脚本逐项比对 本版 SVG vs 核心版 SVG)

- **CJK 扫描:8 页全部 0 命中**——讲解层无任何中文残留。
- **图片:8 页逐页 href(MD5)与位置完全一致**。
- **文本元素逐条 diff**:全部差异块均属讲解层(标题/注/题型名/说明/答案注/页脚/刊头标识)
  与上述裁定项;西语文章、练习题干、选项、P7 金句 8 条逐字一致(同法计数两版相同,
  金句元素逐字节相同)。
- **答案注册表:两版各 150 条,P8 逐条比对仅 137/138 两条不同**(即裁定 1 的重定向),
  其余 148 条逐字一致。
- **40 球总账**:`una noche de 40 goles`(P4)与 `¡40 en toda Europa!`(题 57)在位;
  `38 goles` 两版均无。

## 5. 校对记录

- 构建者全量自校 + 逐页 PNG 目检(8/8):初版发现并修复 §3 所列 5 处版式问题
  (黑带重叠、两处盒标题超宽、P1 每周词条注压线、P6/P8 溢出、P7 错误栏遮挡),
  修复后重新渲染并复检 P1/P2/P7/P8,全部干净。
- 英语讲解逐条核读:语法、拼写、与西语原文对应关系无误;事实与日期未因翻译改变
  (03:00→02:00、21:00 Camp Nou、PSG 4–2、Alonso/Sainz 同为 7 分之差、F1 奥斯汀、
  11 月 2 日 9 个自治区假日、2027 年选举 5 月 23 日意向数据等与核心版一致)。
- 本版未经第二名独立校对员复核(与核心版流程的差别在此明示);上述机器核验 + 人工逐页
  目检为本版的出厂门槛记录。

## 6. 复现

```bash
cd hidden_files/weekly-report-es-en-build
/tmp/wp-venv/bin/python run.py     # 生成 svg/ 到 files/weekly-report-es-en/svg/
/tmp/wp-venv/bin/python render.py # 渲染 cards/ + 印刷版/网络版 PDF
```
(venv 需含 cairosvg、pillow、pypdf;构建代码由核心构建目录复制后改讲解层,核心目录未改动。)

## 7. 交付物(files/weekly-report-es-en/)

- `svg/` 8 张 · `cards/` 8 张 PNG(1950×2700)
- `La-Lucerna-VOL1-EN.pdf` 印刷版 4,552,819 B（D5 重建，2026-11-13；旧配方值 5,763,570 B 已过期，见末节 D5 记录）
- `La-Lucerna-VOL1-EN-web.pdf` 网络版 3,464,783 B（D5 重建，2026-11-13；旧配方值 3,875,443 B 已过期，见末节 D5 记录）
- 本 KIT

未投递 Discord(按任务要求,投递由主线执行)。

## 8. 独立校对记录(第二名校对员,2026-10-21)

> 本节为独立全量校对结论,取代 §5 中「未经第二名独立校对员复核」的声明。
> 方法:双版 SVG 全文提取逐页通读 + 逐词 diff 分类;两版构建源码各复跑一遍比对
> 注册表(题数/级别/分页/键);150 题全部独立重解并与英文简析逐条核对;P7 金句
> 程序化计数;图片逐页 MD5+坐标比对;8 页 PNG 全部目检;交付 SVG 由源码复跑
> 逐字节验证可复现。

### 8.1 发现并修复的缺陷(1 处,版式)

- **P8 答案区末行与页脚线碰撞。** 修复前实测:页脚线 y=2580;答案三栏末行
  基线分别为 2577.96(第 38 题行,字形下沿越线)/ **2591.89**(第 76 题注的
  续行单词「infinitive」,整行落在页脚线之下)/ 2576.32(第 115 题行,贴线)。
  渲染图上压线清晰可见。§3.2 以「末行基线与核心版同量级」判其可接受,本校对
  不采纳该判断:压线即缺陷。
- **修复**(仅改本版构建源 `content8.py`,核心源未动):答案流底界 2606 → 2552;
  答案字号 13.5 → 13.2、行距 1.14 → 1.12;分页标题行距 1.16 → 1.12。整期重渲染
  (构建日志零 FLOW OVERFLOW 警告)。修复后答案区最低基线 2538.7,距页脚线
  41 px;P8 文字总量与修复前逐字一致(11,471 字符),其余 7 页 SVG 与 cards
  逐字节未变。修复后完整复校一轮(见 8.2),零问题。
- 附带观察:核心中文版 P8 末行基线 2588.1,同类压线现象存在于冻结核心内,
  不在本任务修复范围,登记待主线决定(与 §3.6 的核心 P7 事项并列)。

### 8.2 核验通过(修复后完整一轮)

- **核心完整性**:P1–P8 全部文本差异逐项分类完毕——均为讲解层(标题/注/
  题型名/说明/答案注/页脚/刊头配对标识)与裁定 1(P8 E 区 137–140 重定向;
  键比对仅 137/138 为英文译文、150 为写作题占位注,其余 147 键与核心逐字
  一致)、裁定 2(P7 示例信全角括号改 ASCII,已核)。西语文章、题干、选项、
  金句零改动。
- **讲解语言**:8 页 CJK 扫描 = 0;全部 gloss/注/题干说明/诊所注/预告说明/
  150 条答案简析均为英文,语法与对应关系逐条核读无误;150 题独立重解全对
  (含 87 题 31.7+26.8+18.7=77.2、141–144 配对、写作范文 82 词与核心一致)。
- **注册表**:150 题;分页 10/18/18/18/18/18/12/38;级别 A2 52 · B1 70 · B2 28;
  题型分布与 §2 一致。
- **事实**:「una noche de 40 goles」(P4)与题 57「¡40 en toda Europa!」在位;
  「38 goles」全期零命中;日期、比分、民调两组数据与核心逐项一致。
- **金句**:P7 八条西语句与核心逐字相同,全期各恰出现 2 次。
- **图片**:刊用 3 张(P1/P3/P5)与核心版 MD5 及坐标逐页完全一致,图注署名
  与核心一致(§1 原文「4 张」表述已更正为刊用 3 张 + 备用 1 张)。
- **标识**:P1 刊头配对行在渲染图上清晰可见;8 页页脚均标注
  「Text in Spanish · Explanations in English」。
- **P7 错误栏**:4 条全部可见且完整落在盒内(含第 4 条《La gente son
  felices》及其英文注),构建者 §3.6 所述盒高修复在本版成立。
- **版面**:8 页 PNG 目检无溢出、无重叠、无压页脚(P8 修复后复检通过);
  P6 练习 18.5 号字、P1 黑带英文行在新参数下均清晰无碰撞。

### 8.3 §3.6 核心版事项的核实

构建者称核心中文版 P7 错误栏第 4 条在成报上不可见——**经查核心版 cards
属实**:核心版 P7 渲染图中错误栏只见 3 条,第 4 条文字仅存在于 SVG 文本流,
被下方「本周生词」盒覆盖。核心已冻结,本校对未改核心任何文件。

### 8.4 异常事件登记(核心版文件在校对期间被并发修改)

校对进行中(2026-10-21 13:33:50–59 UTC)发现:核心版构建源
`weekly-report-es-build/content7.py` 被修改(mtime),核心 8 张 SVG 随即被
重新生成。**非本校对员所为**:本校对员对核心目录全程只读;注册表复跑使用
/tmp 副本且输出已经重定向(复跑比对链可证:副本 OUT 指向 TMPTGT/TMPTGT2
并在该处生成了与交付件逐字节一致的文件)。重新生成后 7 张与交付件逐字节
一致,**P7 一张不同**(文本元素 156 → 152,可见字符 4,238 → 4,198)。
核心版的 cards 与两份 PDF 仍为原交付状态,与其现行 `svg/p7-lengua.svg`
已不一致,请主线核查该并发修改的来源与意图。本版的 P7 核心完整性核验
(§8.2)以变更前、即交付状态的核心 P7 为基准完成,结论不受影响。

### 8.5 最终裁定

修复后完整一轮全量校对**零问题**——ES × EN 版达到 SOP 出厂门槛,定稿。
构建者声明核验结论:注册表、CJK、金句、图片、标识、P7 盒高修复等均属实;
仅 §3.2 对 P8 末行压线的「可接受」判断被本校对推翻并已修复;
§2 的 PDF 尺寸已按修复后重渲染实测更新(§7)。

## 9. 事实订正（2026-10-21）：P5「jueves 23」→「viernes 23」

- **错误**：第 5 版西班牙语正文（与核心版逐字节相同）称 eFootball 球衣「desde el jueves 23」——2026 年 10 月 23 日实为**星期五**。ES×FR 独立校对发现；核心版与 EN/DE/FR 三个讲解版同日同步订正（本版改动在 `content56.py` 第 19 行，仅此一词）。
- **核验**：先证基线（未修改构建逐字节复现 8 张定稿 SVG）；渲染差异仅 `p5-juventud.svg` 一个文本元素、仅 P5 卡片重出，其余逐字节不变。注册表扫描无题目引用该星期说法；第 80 题（Verdadero，题干仅称「desde el 23 de octubre」）复解仍成立；P7 金句仅引「sábado 24」（正确）。几何：改动行墨迹右界 433→446px，距栏界余 53px；遮挡审计第 5 版 0 标记（第 1 版既有模型标记经像素实测非缺陷，与本次无关）。
- **产物（订正后）**：印刷 PDF 5,763,569 B（sha256 `9c387fa34b2b60098b54d4870548261db2ef3b0c39aead3167dcad0baf517803`）；网页版 PDF 3,875,591 B（sha256 `608ce4081f32a2188e5f05cc5a20dee0cce7a4e9426e54beb146378d398916d5`），均 8 版。GitHub 仓 `2026-w43-es-en` 已同步换 PDF 并更新 pin（附订正说明）。

## D5 重建记录（2026-11-13，W43/W45/W46 D5+§1.1 合并重修 Phase 1）

- **原因**：D5 缺陷——sans 层拉丁/西里尔字符落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者）。本版修前 census：D5 拉丁 492、西里尔 0、弯引号 CJK 0。
- **安装**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target es --reader en --week 2026-w43`（先 `--check` dry-run 通过）。`_D5_READER = "latin"`。路由单元测试 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号 0 个。
- **基线**：重建前先证基线干净——`run.py` TOTAL 150、0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与已发版逐字节相同。基线实测（已发版配方）：印 PDF `57a62c8f3e75124b6683f373825856914b5d4731474f60d585cc14ecf31a9acd`（5,150,124 B）、网 PDF（render）`5baadb685b06f32338917770eab12d60c870509d82dc9f6f7583b318d55ef3a8`（3,465,204 B）。本 KIT §7 旧值（5,763,570 / 3,875,443 B）为更旧配方，已过期，以上两值为准。
- **二次修复（只动字号，文字零改动；实测 advance，patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5）**：
  1. `content12.py:125` P1 头 `EL OTOÑO EMPIEZA DE VERDAD` 25→24（439.1→421.5）。
  2. `content34.py:23` P3 头 `RECORDAR JUNTOS　Remembering` 23→22（427.5→408.9；该头 D5 前已预缩至 23）。
  3. `content7.py:16` P7 头 `A2　DECIR LA HORA Y EL PRESENTE` 24→21（471.1→412.2；同时清除 P7 TEXTX 碰撞——该头压 `B1` 20.5×16.8px）。
  4. `content7.py:48` P7 头 `B2　CREO QUE… / NO CREO QUE…` 24→23（428.8→411.0）。
  5. `content12.py:47` P1 盒 `LA SEMANA EN CIFRAS　Numbers` tsize 23→22（414.8→396.8）。
  6. `content12.py:176` P2 盒 `LA FRASE PARA RECORDAR　Remember` tsize 19.5→18.5（412.2→391.1；该盒 D5 前已预缩至 19.5）。
- **P8**：行数 234→234，距页脚线余量 39.5px 不变；p8 compare CLEAN（keydiff [137, 138]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `La-Lucerna-VOL1-es-en.pdf` sha256 `e49a35d81676ef758bc7fac5cd82f51c45c7c4d3255e8144af2aa529fb71fabc`（4,552,819 B）；网 PDF（render）`La-Lucerna-VOL1-es-en-web.pdf` sha256 `40dfac21af7b8a5a75aac7ba93b1285cf922d63e17c010b1b10b8961ada6c322`（3,464,783 B）；issues 网 PDF（`tools/webpdf.py`）`2026-w43-es-en.web.pdf` sha256 `f5b8965b557ddba2c245d9fbb4f280d0bcdc367e80a8e43182df27525d2b1d1b`（1,064,057 B）——待 closer 换入 `issues/2026-w43/2026-w43-es-en/2026-w43-es-en.pdf` 并更新 pin（已发版 `5c486f00586a6a668e3bef40383e5cbbf950341db526da0bc33d54aa4b778dc6`，1,105,025 B）。印 PDF 缩小约 600KB 系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- **text.md**：D5 不改文字内容；重建后重出因字体宽度变化断行重排（26 REWRAP），交付件为已发版 `.text.md` 原样沿用（BYTE-IDENTICAL）；验收 `verify_textexp_es.py --edition` 判 ADOPT（0 UNEXPECTED；习题号 313/313 序列一致；8 页 token 全同）。
- **D5 门禁（17 门，run 2，全绿 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（1,064,057 B <7MB）；occlusion 0（含自检）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 个（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=399，中位 1.040）；文字层 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。日志：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-en/`（`GATES-SUMMARY.txt` 为总表；run1 日志归档于 `run1/` 子目录）。D5 报告：`production/notes/2026-w43/g-es/scratch-d5-rebuild-es/D5-REPORT-2026-w43-es-en.md`。
