# GATE-LOG — 2026-W47 en-pt proof1（独立复校机械门 · re-fanout #2 重建版）

复校员：独立复校员（与建版者/fan-out agent 非同一人）。日期：2026-11-11。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-pt1/`
（`TMPDIR=<scratch>/tmp`；/tmp 未写。探针：`ls /dev/null` 存在 + `git hash-object -w` 成功 + scratch 写文件成功。
第一轮 proof1 的全部产物已归档至 `proof1-first-build/`，本日志只记录本次重跑。）
运行 Python 一律 `tools/venv/bin/python`。生产目录只读；网 PDF 重渲染在 `ed-copy/` 副本中做，未覆盖生产文件。

## 0. 对象核对（开工先验 + 收尾复测）

| 文件 | 字节 | SHA-256（完整） | 任务单 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-pt.pdf` | 29,345,708 | `3f6b415fa35195ca49605414b5a756a01f0457032cc5c6acc75075e49c221dad` | ✓ 全等 |
| `The-Lucerna-VOL4-en-pt.web.pdf` | 2,418,233 | `0252edc42a4981413c25067e8ed60bb5069994f86c10a4d25a0b8483e0846629` | ✓ 全等 |
| `2026-w47-en-pt.text.md` | 54,123 | `12b04ff13b12db5232d3114816f287c2d72a69df164e0273269409ef3148d545` | ✓ 全等 |

核对方法：盘上 `sha256sum` + `stat`；与 WEEKLY-KIT §2 所载 SHA 亦逐字一致。两 PDF 各 8 页（`pdfinfo`，1462.5×2025 pts）。
核心 core-en 复核前后各测一次，未变：印 `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`（41,407,278 B）、
网 `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`（2,804,271 B）、
text `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`（51,405 B），与 FANOUT-REPORT 一致。

## 1. 遮挡审计 `tools/occlusion_audit.py` — 0 flags ✓

- 自检：`--selftest` OK（6 类 planted flags 各命中 1 次，clean 对照静默）。
- 本版：`occlusion_audit.py production/2026-w47/2026-w47-en-pt --core production/2026-w47/core-en --json occlusion.json`
  → `0 flags`；core `0 flags`；NEW vs core `0`。退出码 0。见 `occlusion.log`。
- 盲区说明：该审计不检“盒内文字漫出盒底”（文字未被遮盖）。此类缺陷由第 6 门 creambox 全版扫查覆盖：
  P2 DID YOU KNOW 与 P1 SEARCHES 两处旧患均已在盒内（见 §6），无新增盒外行。

## 2. P8 `tools/p8.py` — extract 60/150，compare CLEAN ✓

- extract（本版与核心 p8-test.svg，total 150）：各 `noted set = 60 of 150`，集合相同
  `[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]`（`p8-extract.json` / `p8-extract-core.json`）。
- compare（显式 `--core-p8/--edition-p8` 路径；`--core-dir/--edition-dir` 形式如第一轮所记，因工具按 target 推导 p8 文件名而报错，不采用）：
  `core 60 noted / edition 60 noted / status: CLEAN / missing=[] / extra_count=0 / uncertain=[] / keydiff=[137, 138, 139, 140, 150]`。
- keydiff 逐项说明（均属预期、非缺陷）：137–140 为读者语译文键（葡语 vs 中文，键义同）；150 为开放写作题破折号体。
- 注意：p8.py compare 只比对“集合相等 + 有注键的键值”，Q39/Q40 的键值由人工四方核对发现确认（见 PROOF-NOTE D1），本次四方一致。

## 3. freeze `tools/freeze.py` — baseline 8/8（正确路径重跑），diff 仅 U+3000 ✓

- baseline：`freeze.py baseline --build production/2026-w47/core-en --core-svg production/2026-w47/core-en/svg --out <scratch>/freeze-baseline`
  → `8/8 SVGs byte-identical (repointed files: none)`；`core integrity: shipped core SVGs unchanged by the run`。
  逐页（core == produced，前 16 位）：p1 `a9a8deaf76e61cb2`、p2 `979747160de01d67`、p3 `efb83ce76688554b`、p4 `aa6f395e4932ef8b`、
  p5 `a6a515cd5f734d0d`、p6 `7692256484f26289`、p7 `da908af644651793`、p8 `2f9a0334d70e07ba`；并以 `sha256sum` 直接复核盘上 core-en SVG，逐个一致（见 `freeze.log`）。
- **与构建方日志的差异（已查明，见 PROOF-NOTE 观察 1）**：构建方 `scratch-fanout-en2/fanout/pt/freeze.log` 所载哈希
  （p1 `16be1b38…`、p2 `23d1d7c4…`、p3 `22aa9881…`、p4 `8151afbf…`、p5 `cbecfa6c…`、p6 `48167a62…`、p7 `61007a0d…`、p8 `1365ad54…`）
  与盘上 core-en SVG 实测哈希逐个不符；核查其 `freeze-final/build-copy/`，内为 **en-pt 版目录**（含 `The-Lucerna-VOL4-en-pt.pdf`、葡语 content），
  其 build-copy/svg 的哈希恰为上述 8 个值（含 `LIFE　Vida` / `SPORT　Desporto` 等葡语文本）。结论：构建方那轮 freeze 的 `--build` 指向了版目录，
  证明的是版自我复现，非核心复现；我方本次以正确路径重跑，8/8 真实通过。
- diff（core-en SVG vs en-pt SVG，`freeze-diff.json`，与构建方 `freeze-diff.log` 逐行一致）：
  p1 +34/−33、p2 +43/−54、p3 +27/−23、p4 +25/−22、p5 +25/−22、p6 +25/−21、p7 +65/−55、p8 +105/−99；
  **新增 CJK 合计 9，全部为 U+3000 全角空格**（p1 2、其余每页 1）；删除的 CJK 为核心中文讲解层。符合 en×pt 的换语预期。

## 4. 印/网文字层同一 — token 多重集差分 0/0，逐页字节一致 8/8 ✓

- `pdftotext -layout` 两版：各 108,097 字符（layout 口径）、token 各 8,862、distinct 各 2,532；
  **print−web 0 token，web−print 0 token**。无 layout 口径：各 49,271 字符（字节）——与构建方 `printweb.log` 的 47,926 字符一致
  （字符数 vs 字节数之差 1,345 为非 ASCII 字符的多字节部分）。两版各 8 页。
- 逐页字节一致（layout 提取）：p1 12,540B、p2 13,634B、p3 11,212B、p4 12,542B、p5 10,715B、p6 11,128B、p7 14,182B、p8 23,489B，8/8 identical。
- 网版重渲染（scratch 副本 `ed-copy/`，`webpdf.py <scratch>/ed-copy/svg <scratch>/ed-copy/*.web.pdf`，未动生产文件）：
  写出 2,418,228 B（发货 2,418,233 B，差 5 字节为 fontTools 子集改写 head.modified 墙钟 + cairo CreationDate，符合铁律预期）；
  **文字层逐字节一致**：发货网版 109,442 B == 重渲染网版 109,442 B。见 §4 末段输出。
- 网版 P1/P8 渲染（`pdftoppm` 72dpi，`render/web-p1-1.png` / `render/web-p8-8.png`）目视与印版一致，无豆腐块、无缺字。

## 5. keycheck（150 题键核对，复校员脚本 `keycheck2.py` + 补充比对）— 150/150 ✓

- text.md 答案区解析：150 行唯一题号，无缺号、无重号。
- 与 `registry.json` 逐题比对：key 0 不符、level 0 不符、type 0 不符（见 `keycheck-out.txt`）。
- 各页题数：P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39，合计 150；级别 A2 62 / B1 66 / B2 22；与 KIT §1 一致。
- registry vs P8 提取键：149/150 精确一致，唯一例外为 Q150 短标签（提取键 `Questão aberta`，registry 全句——p8.py 已知行为，与构建方一致，预期）。
- registry 键 vs core-en registry：145/150，仅 137–140、150 五个读者语键不同（预期）。
- noted set == core noted set：True。
- Q38–41 提取键：b / a / d / c；Q46=A、Q52=hosted、Q55=won、Q125=A（见 `keycheck-extra.txt`）。
- 答案内容逐题验算：变动的 8 题（Q39/40/46/52/55/82/84/125）对 SVG 题面逐项验算（见 §9 与 `changed-items.txt` / `q3940.txt`）；
  未变动题与第一轮已验备份逐字节相同（registry diff 仅上述 8 条；text.md diff 仅 31 处，见 §10），配对五组以 SVG 印刷字母逐组复核，
  图表题 Q82–87 对 P6 图表数字逐项验算（254+162+19=435；Senate 20+13=33/35；7 翻转；5 州长），Q47–Q51、Q60–Q63、Q100–Q111、Q112–Q119、Q120–Q132、
  Q133–Q136、Q137–Q140、Q145–Q149 均对题面与正文核对正确；Q60 一度疑似渲染小图误读，已以 SVG 原文复核（`60. England lost 4–0 in 2021–22.`），三源一致。

## 6. creambox 全版扫查（32 个奶油盒）— 旧患已清，仅一处真墨 +0.9px 紧余量 ✓

- 扫查脚本：沿用第一轮自写的 `creambox.py`（SVG 盒底下 40px 内文字 + PNG 盒底带墨水）与 `creambox2.py`（末行基线 + 0.30em 下行余量），
  另加真墨像素复核（阈值 200，`pixel-truth.txt` / `pixel-truth2.txt`）。结果见 `creambox.log` / `creambox2.log`。
- **P2 DID YOU KNOW? 盒（第一轮缺陷 2，已解决）**：盒 `x=1440, y=833, w=422, h=352.5`（旧 h=325.5），底边 1185.4；
  末行 `November 3.` 基线 y=1171.1，下行余量 +7.9px；像素实测末行墨水最末行 y=1170（距盒底 15.4px）；裁片 `crops/p2-didyouknow-bottom.png` 目视在盒内。
- **P1 SEARCHES 盒（第一轮观察 1，已解决）**：盒底 1256.0；末行 `Interesse relativo, não números exatos.` 基线 y=1244.0，下行余量 +6.3px；
  像素实测墨水最末行 y=1246（距盒底 10px）；裁片 `crops/p1-searches-bottom.png` 目视三行全在盒内。
- **P2 AND YOU? 盒（紧余量，非缺陷）**：盒 `y=1211`，底边 1544.9；末行 `para a redação.` 基线 1539.85，0.30em 启发式报 −1.0px；
  真墨像素复核（阈值 200）：该行墨水行 y=1524..1544，最末行 1544，**真墨余量 +0.9px**；其下 y=1557..1558 为盒下分隔线（满栏宽 422px），非盒内文字；
  裁片 `crops/p2-andyou-bottom.png` 目视 `p` 下行笔完整在奶油盒内。启发式为假警报（与 de 同款），不修复。
- **P7 工具盒干净**：盒 `x=1440, y=651, w=422, h=357.21`，底边 1008.21；末行 `apuração vai mudar de novo.` 基线 y=959.68，下行余量 42.1px；
  盒底带暗像素 0；下一栏头 READERS' CORNER 在盒底之下 37px，属正常栏距。
- **其余 27 盒**：盒下续行均为下一栏头（+35.5~37px 标准栏距）或下一段正文，无盒内句子跨底；v1 脚本的 BELOW-LINE 列表（23 处）经 v2 逐项裁定全为栏头/下段，
  末行下行余量除上述三处外全部 ≥ +24px。P1 IN THIS ISSUE 盒底带 389–406 暗像素已查明为下一栏头 `THE WORD OF THE WEEK` 的字顶（y=1659..1675，基线 1676），非盒内漫出。

## 7. P8 最小字号 — 10.12pt（PDF 实测），≥ 9.75pt 下限 ✓

- PyMuPDF（tools venv）实测：印版与网版 P8 最小字号均为 **10.12pt**；全版其余各页最小 11.62pt（见 `p8-font.txt`）。
- 换算：SVG 设定 13.5 单位 × 0.75（1950px→1462.5pt）= 10.125pt，与实测一致；SOP §1.1 下限 9.75pt 为 PyMuPDF 口径，10.12 ≥ 9.75，门通过。
  KIT §3 所写 “13.5 pt”未注明是 SVG 单位（见 PROOF-NOTE 观察 3）。

## 8. boxtitle 宽度 — 源扫查 12/12、SVG 扫查 18/18，全 fit ✓

- 源扫查（`sweep_titles.py pt`，预算 404.5px；`boxtitle-src.log`）：12 个框题 0 超支；最紧 HOW LONG? 395.6（+8.9）、
  THE WEEK IN NUMBERS 390.9（+13.6）、SENATE IN NUMBERS 367.2（+37.3）、HAYMITCH'S GAMES 348.1（+56.4）、
  **ODD SOCKS, IN NUMBERS　N.º 346.2（+58.2）**、WHY PERTH? 334.8（+69.7）、THE TOOLBOX 327.4（+77.1）、A PRACTICE BALLOT 325.7（+78.8）。
- SVG 扫查（`sweep_svg_titles.py pt`，advance + 真墨；`boxtitle-svg.log`）：18 个框题 0 溢出；最紧 HOW LONG? advance +8.9 / **真墨 +8.5**、
  THE WEEK IN NUMBERS advance +13.6 / 真墨 +13.5；ODD SOCKS advance +58.2；其余余量 +37.3~+663.0。
- 真墨独立复核（渲染卡，`pixel-truth`）：ODD SOCKS 标题墨至 x=449，盒右界 510.5，**真墨余量 +61.5px**（`crops/p5-odd-title.png` 目视）；
  HOW LONG? 标题墨至 x=1854，盒右界 1862.5，**真墨余量 +8.5px**（`crops/p6-howlong-title.png` 目视）。与扫查数一致。
- KIT §4 框题数字与本次实测逐项一致；KIT §6 自查行仍写旧标题 `THE SENATE, IN NUMBERS`（见 PROOF-NOTE 观察 2）。

## 9. 外部事实与星期核验（新 Ashes 回顾体 + 旧事实沿用）

- Ashes 回顾体（Wikipedia 2025–26 Ashes series 词条 / Sky Sports 第五 Test 报道，2026-11-11 检索）：
  系列 2025-11-21–2026-01-08 ✓；澳大利亚 4–1 ✓；首三 Test 珀斯/布里斯班/阿德莱德胜出、第三 Test 后已保 Ashes ✓；
  第四 Test 墨尔本英格兰 4 wickets 胜、近十五年首胜（词条：“ending an 18-match (14-year) losing streak”）✓；
  第五 Test 悉尼澳大利亚 5 wickets 胜 ✓；首 Test 珀斯 21–22 Nov 2025、8 wickets 胜 ✓；
  “首 Test 两日完赛、1888 年以来按球数最短”（词条：“first Ashes Test to be concluded inside two days since … 1921 and the shortest by balls bowled since 1888”）✓；
  珀斯体育场首办 Ashes Test、2021–22 未排珀斯 ✓；第四 Test 墨尔本亦为两日 ✓。
- 星期核验（`date -d`，America/Toronto）：2025-11-21 周五、2026-11-21 周六、2026-11-22 周日、2026-11-19 周四、2026-11-16 周一、
  2026-11-20 周五、2026-11-03 周二、2026-11-26 周四、2026-01-08 周四、2026-06-18 周四，全部正确。
- 其余事实沿用第一轮 proof1 的逐项网核（I'm a Celebrity、Anti-Bullying Week、Hunger Games、ATP Finals、英超、World Children's Day、
  选举数字内部自洽 435=254+162+19、多数 218、参议院 20+13=33/35、7 席翻转、5 州长翻转、图片授权 8 张 PD/CC0），相关正文与题面在本次 `diff` 中未变动。

## 10. 旧版逐页对比（备份 `scratch-fanout-en2/backup/2026-w47-en-pt/` → 新版）

- text.md `diff`：31 处，全部属于 fix1 集（P1 strip、SEARCHES #2、IN BRIEF、SENATE/SATURDAY 标题、P2 feature、P4 全文重写、Q46/52/55 题面、Q125 题面、
  ODD SOCKS 标题、P6 桥接、P7 try-it 与 NEXT WEEK、答案区 Q39/40/46/52/55/82/84/125）；无预期外行。见 §5 与 `old-new-diff.txt`。
- registry `diff`：仅 8 条（Q39/40/46/52/55/82/84/125），42 行 diff 输出；其余 142 条逐字节相同。Q7/Q83 注记新旧相同（map 补丁值与旧值一致，无变化）。
- SVG 文本 `diff`：P1（strip、lead 段、SEARCHES #2、IN BRIEF）、P2（SENATE 标题、WHAT IS ON THIS WEEK）、P4（全文重写）、P5（ODD 标题、THE JUNGLE, TOO）、
  P6（仅桥接词 confirmados→anunciados）、P7（Try-it、NEXT WEEK）、P8（Q125 题面 + 答案块 Q39/40/52/55/82/84/125）；**P3 SVG 逐字节相同**。
- 渲染像素对比（旧印 PDF vs 新印 PDF，72dpi，阈值 30）：P1 1.0%（SEARCHES/strip/IN BRIEF/lead）、P2 0.8%（SENATE 标题/WHAT IS ON/两盒加深）、
  **P3 0px 全同**、P4 11.3%（Ashes 重写）、P5 0.2%（仅 ODD 标题右部 + THE JUNGLE, TOO 两处）、P6 812px（仅桥接词）、
  P7 6.2%（Try-it 段落由 3 行增至 4 行，蛇形流下游 91 个文本元素统一下移 +35.7px；NEXT WEEK 原位改写，y=2221.37 未动；无溢出，P7-main flow 终点 1786/2560）、P8 1.4%（Q125 题面 + 答案块重排）。变化区域与 SVG 文本 diff 逐项对应，无预期外变化。
- ABSTRACT：旧短式整行 → 新完整式（见 PROOF-NOTE carry-forward 项）。
- content*.py 五个文件均已变（重 fan-out 复拷核心 + map，预期）。

## 11. 其余扫查

- `check_s11.py pt`：ALL §1.1/P8 CHECKS PASS（colour set core 19 = edition 19；badge 色 A2 #5c6e30 / B1 #46581f / B2 #37402f；
  P8 Q113–120 options 行 [A2] tag；`Levels: 145–149 [A2]`；Q120 [A2] chip；P8 WRITING 头 `H　WRITING　Escrita [B1]`）。见 `check_s11.log`。
- 家具：`tables.py furniture pt --target en --week 2026-W47` 输出与本版 badge / footer / `Página {n} de 8` / `Nota — ` / `— Página {n} —` 逐字一致，VOL.4。
- 引号/撇号：弯双引号 SVG 82/82、text.md 81/81；« » text.md 4/4、SVG 2/2；无直引号；撇号 ASCII（SVG 43、text.md 40）；
  U+2019 0；孤标点 0；单字符标点元素 0。见 `sweeps.txt`。
- 禁词：SOP / proofread / geometry audit / cover / lint / placeholder / TODO / XXX / Lorem 在 SVG 可见文本与 text.md 中均为 0。
- CJK：SVG 可见文本仅 U+3000 ×141；text.md 0 处 CJK。`next Sunday`：core-en / en-pt / tools/tables.py 均为 0 命中，无适用对象。
- 陈旧措辞：`Ashes begin`、`Perth is winning!`、`second week in Perth`、已确认、`Confirmado em`、`foram decididos`、旧标题 `THE SENATE, IN NUMBERS` /
  `SATURDAY, NOVEMBER 21` 在 text.md / 全部 SVG / registry 中均为 0 命中。
- D5 字体（只记录数量，不判）：`pdffonts` 印版 41 个字体对象、网版 41 个字体对象，全部 embedded + subset；
  字体族 NotoSansCJKsc（Regular/Bold）、UnifrakturMaguntia、Newsreader（Regular/Italic/Bold）、NotoSerifCJKsc Regular、DejaVuSans。
- ABSTRACT：753 字符一行，无 ASCII 双引号；Lucerna / VOL.4 / 150 / A2 / B2 / anunciados / certificação 10 de novembro a 18 de dezembro /
  16 de novembro / 20 de novembro / 21 de novembro / 4–1 全部命中。见 `q3940.txt` 末段。

## 12. 全文通读 + 目视

- `2026-w47-en-pt.text.md` 1,305 行：以 `diff` 覆盖全部 31 处变动 + keycheck 覆盖全部 150 答案；未变动行与第一轮已通读的备份逐字节相同。
- 印版 8 页逐页渲染目视（`render/p-1.png` ~ `p-8.png`）：除 §6 紧余量三处外，无溢出、重叠、压页脚、图片与出处问题；
  P7 栏头、工具盒、读者园地、示例信、NEXT WEEK 均干净；P8 答案块 150 键收尾在页脚之上，MODEL + Reading Room 图干净。
- 网版 P1/P8 渲染目视（`render/web-p1-1.png` / `render/web-p8-8.png`）：与印版一致，无豆腐块、无缺字。
- 紧点裁片 5 张（`crops/`）：P2 AND YOU、P1 SEARCHES、P2 DID YOU KNOW、P5 ODD 标题、P6 HOW LONG 标题，全部目视在内。

## 13. 结论

- 机械门：遮挡 0、P8 CLEAN、freeze 8/8（正确路径重跑）、印网 0/0、keycheck 150/150、creambox（除 +0.9px 真墨紧余量外）清、
  P8 字号过、框题装得下、check_s11 全过——**全部通过**。
- 人工核对：第一轮两项核心级缺陷均已解决并实测；carry-forward 三项（ODD 标题、ABSTRACT、Q39/40）均已落地；
  150 题三源手验（方法见 PROOF-NOTE）零不符；8 页逐页目视 + 旧版逐页对比零预期外变化。
- **结论 (a)：本版定稿，零缺陷。** 观察 1–6（构建方 freeze 路径、KIT 两行旧文案、P2 AND YOU +0.9px 紧余量等）不构成定稿阻碍，报协调员裁定。
