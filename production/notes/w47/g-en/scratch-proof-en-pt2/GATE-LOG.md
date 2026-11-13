# GATE-LOG — 2026-W47 en-pt proof2（独立复校机械门 · Q73 delta 后）

复校员：独立复校员（与建版者/delta agent 非同一人）。日期：2026-11-11。
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-pt2/`
（`TMPDIR=<scratch>/tmp`；/tmp 未写。探针：`ls /dev/null` 存在 + `git hash-object -w` 成功 + scratch 写文件成功。
生产目录只读；网 PDF 重渲染在 `ed-copy/` 副本中做，未覆盖生产文件。
运行 Python 一律 `tools/venv/bin/python`；creambox canonical 用 `python3 ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`。）
全部命令见 `run-gates.sh`，逐门日志见本目录同名文件。

## 0. 对象核对（开工先验 + 收尾复测）

| 文件 | 字节 | SHA-256（完整） | 任务单 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-pt.pdf` | 29,345,708 | `52452731bc5988209215cb8f83548b14a7d1a933953dac09688e7f8d82a3b700` | ✓ 全等 |
| `The-Lucerna-VOL4-en-pt.web.pdf` | 2,418,222 | `467068e289700e570c5e2c55a9f6c372dc618a0fb4e8d49ccf277429151b7128` | ✓ 全等 |
| `2026-w47-en-pt.text.md` | 54,120 | `f85c55cef1cf7fe824fe59f3c9ff97bad8f4938d423bcc737a9afe60fbab7422` | ✓ 全等 |

核对方法：盘上 `sha256sum` + `stat`；收尾复测三件 SHA 与开工逐字一致（生产文件未动）。
核心 core-en 复核前后未变：盘上 core SVG 8 页哈希（`core-readonly-check.txt`）与 proof1/delta 所载逐个一致
（p1 `a9a8deaf…`、p2 `97974716…`、p3 `efb83ce7…`、p4 `aa6f395e…`、p5 `a6a515cd…`、p6 `76922564…`、p7 `da908af6…`、p8 `1066c475…`）。

### Delta 范围独立核实（vs delta 前状态，非采信自述）

- registry：`diff registry-pre.json registry.json` 恰好 1 行，第 583 行 `"key": "speak"` → `"key": "up"`。
- text.md：`diff text-pre.md 2026-w47-en-pt.text.md` 恰好 1 行，l.1151 `73. [A2] Completar frases — speak (…)` → `… — up (…)`。
- SVG：`sha256sum svg/*.svg` vs `svg-pre.sha256` 仅 `p8-test.svg` 变（`1365ad54…` → `d9ce301c…`）；其余 7 页字节一致。
  快照见 `svg-post.sha256`。

## 1. 遮挡审计 `tools/occlusion_audit.py` — 0 flags ✓

- 真实审计，未加 `--selftest`：`occlusion_audit.py production/2026-w47/2026-w47-en-pt --core production/2026-w47/core-en --json occlusion.json`
  → `production/2026-w47/2026-w47-en-pt/svg: 0 flags`；`core: 0 flags; NEW vs core: 0`。退出码 0。见 `occlusion.log`。
  （日志首行 `selftest OK: planted classes fired {...}; clean controls silent` 为工具内置自检输出，非本次所加旗标。）
- 盲区说明：该审计不检“盒内文字漫出盒底”。此类缺陷由第 6 门 creambox 全版扫查覆盖。

## 2. P8 `tools/p8.py` — extract 60/150，compare CLEAN ✓

- extract（本版与核心 p8-test.svg，total 150）：各 `noted set = 60 of 150`，集合相同
  `[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]`（`p8-extract.json` / `p8-extract-core.json`）。
- compare（显式 `--core-p8/--edition-p8` 路径）：
  `core 60 noted / edition 60 noted / status: CLEAN / missing=[] / extra_count=0 / uncertain=[] / keydiff=[137, 138, 139, 140, 150]`。
- keydiff 逐项说明（均属预期、非缺陷）：137–140 为读者语译文键（葡语 vs 中文，键义同）；150 为开放写作题说明句。
- Q73 提取键：`"73": "up"`（`p8-extract.json:140`）。

## 3. freeze `tools/freeze.py` — 核心 8/8 + 版 baseline 8/8 + core 只读对照 8/8 ✓

- 标准口径 baseline：`freeze.py baseline --build production/2026-w47/core-en --core-svg production/2026-w47/core-en/svg --out <scratch>/freeze-baseline`
  → `8/8 SVGs byte-identical (repointed files: none)`；`core integrity: shipped core SVGs unchanged by the run`。
  逐页（core == produced，前 16 位）：p1 `a9a8deaf76e61cb2`、p2 `979747160de01d67`、p3 `efb83ce76688554b`、p4 `aa6f395e4932ef8b`、
  p5 `a6a515cd5f734d0d`、p6 `7692256484f26289`、p7 `da908af644651793`、p8 `1066c475da8afe7e`。
- 更正口径版 baseline：`freeze.py baseline --build production/2026-w47/2026-w47-en-pt --core-svg production/2026-w47/2026-w47-en-pt/svg --out <scratch>/freeze-baseline-edition`
  → `8/8 SVGs byte-identical`；逐页：p1 `16be1b382d50fce9`、p2 `23d1d7c4b25f138f`、p3 `22aa9881ef4a36f4`、p4 `8151afbf5ace1638`、
  p5 `cbecfa6c325f84e8`、p6 `48167a629af0b2e3`、p7 `61007a0d7731f578`、p8 `d9ce301c945db86e`（与修后 svg 快照逐个一致）。
  注意：此口径下 freeze.log 的 “core” 列实为版 SVG 哈希（`--core-svg` 指向版 svg），不可误读为核心哈希。
- core 只读对照：`sha256sum core-en/svg/*.svg`（`core-readonly-check.txt`），8 页前 16 位与标准 baseline 所载核心哈希逐个一致 → 8/8。
- diff（core-en SVG vs en-pt SVG，`freeze-diff.json`）：
  p1 +34/−33、p2 +43/−54、p3 +27/−23、p4 +25/−22、p5 +25/−22、p6 +25/−21、p7 +65/−55、p8 +106/−100（proof1 为 +105/−99）；
  **新增 CJK 合计 9，全部为 U+3000 全角空格**（p1 2、其余每页 1）；删除的 CJK 为核心中文讲解层。p8 相对 proof1 的 +1/−1 恰为 Q73 键字符串改动。

## 4. 印/网文字层同一 — token 多重集差分 0/0，逐页字节一致 8/8 ✓

- `pdftotext -layout` 两版：各 108,091 字符、token 各 8,862、distinct 各 2,532；
  **print−web 0 token，web−print 0 token**。无 layout 口径：各 47,923 字符、token 各 8,879，差分 0/0。
- 逐页字节一致（layout 提取）：p1 12,540B、p2 13,634B、p3 11,212B、p4 12,542B、p5 10,715B、p6 11,128B、p7 14,182B、p8 23,483B，8/8 identical
  （p8 较 proof1 的 23,489B 少 6B，为答案区重排，与 delta 所述一致）。
- 网版重渲染（scratch 副本 `ed-copy/`，`webpdf.py <scratch>/ed-copy/svg The-Lucerna-VOL4-en-pt.web.pdf`，未动生产文件）：
  写出 2,418,223 B（发货 2,418,222 B，差 1 字节为 fontTools 子集改写 head.modified 墙钟 + cairo CreationDate，符合铁律预期）；
  **文字层逐字节一致**：发货网版 == 重渲染网版（`RERENDERED WEB TEXT == DELIVERED WEB TEXT`，见 `webpdf.log`）。
- 网版 P1/P8 渲染（`pdftoppm` 72dpi，`render/web-p-1.png` / `render/web-p-8.png`）目视与印版一致，无豆腐块、无缺字。

## 5. keycheck（150 题键核对，复校员脚本 `keycheck2.py` + 150 题手核）— 150/150 ✓

- text.md 答案区解析：150 行唯一题号，无缺号、无重号。
- 与 `registry.json` 逐题比对：key 0 不符、level 0 不符、type 0 不符（见 `keycheck-out.txt`）。
- 各页题数：P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39，合计 150；级别 A2 62 / B1 66 / B2 22；与 KIT §1 一致。
- registry vs P8 提取键：149/150 精确一致，唯一例外为 Q150 短标签（提取键 `Questão aberta`，registry 全句——p8.py 已知行为，预期）。
- registry 键 vs core-en registry：145/150，仅 137–140、150 五个读者语键不同（预期；见 `sweeps.txt`：`registry keydiff vs core: [137, 138, 139, 140, 150]`）。
- noted set == core noted set：True。
- **150 题 key-vs-stem 手核**（`fill-audit.py` + `fill-audit.txt`，逐项读题干）：
  - Q1–111：解析 `content*.py` 的 `f.ex`/`match_set`，源顺序与 registry 键 0 偏差，逐项读 stem 判 key 成句——全部适配。
    重点：Q7 B=254、Q8 A=Tue Nov 3、Q9 C=218、Q13 1、Q14 Thursday、Q15 27、Q16–19 will 句型、Q20 B Nov 10–Dec 18、Q22 A Thu Nov 26、
    Q24–27/38–41/56–59/74–77 五组配对（字母与定义逐组相符；Q39→a mentor、Q40→d arena 与 proof1 四方核对一致）、
    Q46 A（Fri Nov 21 2025 Perth）、Q47 C back、Q48 B、Q49 A 2010–11、Q50 C 12:30、Q51 B knee、Q52 hosted、Q53 lasts、Q54 eight、Q55 won、
    Q60–63 过去式、Q64–69 Anti-Bullying Week、Q70 silence、Q71 socks、Q72 rights、**Q73 up**、Q78–81 现在进行时（Q79 are speaking up，up 不动）、
    Q82–87 图表读数（254/19/33 of 35/7/5/435=254+162+19）、Q88–93、Q94 certify、Q95 call、Q96 changed、Q97 takes、Q98 differs、Q99 official、
    Q100 won、Q101 more、Q102 lost、Q103 will、Q104 published、Q105 whether、Q106 chose、Q107 win（标题现在时）、Q108–111 纠错句。
  - Q112–119 cloze：对 `content8.py:29` 段落 + 选项组逐项验算，均为唯一适配项——112 Tuesday（Nov 3 周二；选项 Mon/Tue/Fri）、
    113 call（a ___ is a news organisation's judgement）、114 continues（the counting ___）、115 will meet（in January）、
    116 writes（Maya ___ the dates，三单）、117 will certify（by December 18）、118 wears（she ___ odd socks）、119 will watch（on Friday）。
  - Q120–128 MC：120 B 254、121 A Tue Nov 3、122 C 7、123 B Fri Nov 20、124 A Mon Nov 16 9 p.m.、125 A 4–1、126 B “Break the Silence”、127 A Fri Nov 20、128 C Thu Nov 26。
  - Q129–132 阅读：129 B teacher in Manchester、130 A 254、131 C one red sock and one blue sock、132 B the American election。
  - Q133–136 D 句型：133 will meet、134 won、135 more、136 whether。
  - Q137–140 翻译：137 “Os democratas venceram a Câmara e o Senado.”、138 “A apuração continua.”、139 “O novo Congresso se reunirá em janeiro de 2027.”、140 “Quebre o silêncio.”——逐句与英文原句相符。
  - Q141–144 配对 F：a call→b（news organisation's judgement）、a runoff→c（a second vote）、to certify→d（to confirm a count officially）、a midterm→a（election in the middle of a term）。
  - Q145–149 对话：145 row（the front row）、146 film（about Haymitch）、147 popcorn（one large ___ and two drinks）、148 show（the next ___）、149 Friday（opens on ___, November 20? — Yes, Friday）。
  - Q150 开放写作题：键为说明句，预期例外。
  - 既存重复（proof1 已带）：Q6=Q12（January）、Q2=Q95（call）、Q5=Q96（changed），跨页/跨级别复用，非缺陷。

## 6. creambox 全版扫查（32 个奶油盒）— 除一处真墨紧余量外全部清 ✓

- canonical 扫查（`hidden_files/w47/tools/creambox.py`，`creambox.log`）：32 盒；inside-only 余量无负值；
  BELOW-WINDOW 全部为 +24.0~+37.0px 的下一栏头或下段正文（TRY IT NOW / THE WORD OF THE WEEK / WHAT IS ON THIS WEEK? / READ THE CHART / FIFTY ELECTIONS / READERS' CORNER 等），
  无 +12~+18px 整行漫出；P7-TOOLBOX 7 盒，最小 inside clearance +47.7px，最小 desc-clear +41.6px。
- PNG 条带扫查（proof1/delta 同款 `creambox.py`，`creambox-png.log`，读 `cards/*.png`）：23 处 SVG-OVERFLOW 启发式旗标，
  与 proof1 同集合，逐项裁定全为栏头/下段（+24~+37px）；唯一 PNG-SPILL 为 P1 的 406px，已查明为下一栏头 `THE WORD OF THE WEEK` 的字顶（与 proof1 同），非盒内漫出。
- creambox2（`creambox2.log`）：末行下行余量除下述三处外全部 ≥ +24px。
  - **P2 AND YOU? 盒（紧余量，非缺陷）**：盒 `y=1211`，底边 1544.9；末行 `para a redação.` 基线 1539.85，0.30em 启发式报 −1.0px；
    本轮 72dpi 渲染卡真墨复核（`pixel-truth.txt`）：墨水最末行 1157 PNG px（=1542.7 SVG），盒底 1158.7 PNG px（=1544.9 SVG），真墨余量约 +2.2px SVG
    （proof1 全分辨率卡测得 +0.9px SVG；两法同为正数）；其下 1168 PNG px 为盒下分隔线（SVG y≈1557），非盒内文字；
    裁片 `crops/p2-andyou-bottom.png` 目视 `p` 下行笔完整在奶油盒内。
  - **P1 SEARCHES 盒**：盒底 1256.0；末行 `Interesse relativo, não números exatos.` 基线 y=1244.0，下行余量 +6.3px。
  - **P2 DID YOU KNOW? 盒**：盒底 1185.4；末行 `November 3.` 基线 y=1171.1，下行余量 +7.9px。

## 7. P8 最小字号 — 10.12pt（PDF 实测），≥ 9.75pt 下限 ✓

- PyMuPDF（tools venv）实测：印版与网版 P8 最小字号均为 **10.12pt**；全版其余各页最小 11.62pt（见 `p8-font.txt`）。
- 换算：SVG 设定 13.5 单位 × 0.75 = 10.125pt，与实测一致；SOP §1.1 下限 9.75pt 为 PyMuPDF 口径，10.12 ≥ 9.75，门通过。
  KIT §3 所写 “13.5 pt”未注明是 SVG 单位（见 PROOF-NOTE 观察 1）。

## 8. boxtitle 宽度 — 源扫查 12/12、SVG 扫查 18/18，全 fit ✓

- 源扫查（`sweep_titles.py pt`，预算 404.5px；`boxtitle-src.log`）：12 个框题 0 超支；最紧 HOW LONG? 395.6（+8.9）、
  THE WEEK IN NUMBERS 390.9（+13.6）、SENATE IN NUMBERS 367.2（+37.3）、ODD SOCKS, IN NUMBERS　N.º 346.2（+58.2）。
- SVG 扫查（`sweep_svg_titles.py pt`，advance + 真墨；`boxtitle-svg.log`）：18 个框题 0 溢出；最紧 HOW LONG? advance +8.9 / **真墨 +8.5**、
  THE WEEK IN NUMBERS advance +13.6 / 真墨 +13.5；ODD SOCKS advance +58.2；其余余量 +37.3~+663.0。

## 9. 外部事实与星期核验（沿用 proof1，delta 未动正文）

- 本轮 delta 只改 Q73 一键，正文、数字、日期均未动（registry/text/SVG 三向 diff 已证）；Ashes 回顾体与星期核验沿用 proof1 的逐项网核与 `date -d` 核验，
  本轮未重核外部事实（无变动对象）。Q82–87 图表题已对 P6 图表数字逐项验算（254+162+19=435；Senate 20+13=33/35；7 翻转；5 州长）。

## 10. 其余扫查

- `check_s11.py pt`：ALL §1.1/P8 CHECKS PASS（colour set core 19 = edition 19；badge 色 A2 #5c6e30 / B1 #46581f / B2 #37402f；
  P8 Q113–120 options 行 [A2] tag；`Levels: 145–149 [A2]`；Q120 [A2] chip；P8 WRITING 头 `H　WRITING　Escrita [B1]`）。见 `check_s11.log`。
- `verify_ed.py pt`：**VERIFY ALL PASS**（Q39 key a / Q40 key d / Q46 A / Q52 hosted / Q55 won / Q125 A / registry 无陈旧 Ashes 措辞 /
  text.md 150 答案 / Ashes 回顾体在场 / P8 min PDF font 10.12pt ≥ 9.75pt / SVG 零真实 CJK）。见 `verify_ed.log`。
  （verify_ed.py 为各版通用的 per-edition 脚本，本轮自 `scratch-proof-en-es1/verify_ed.py` 取用，与 delta-es/ko2 副本逐字节相同；用法 `verify_ed.py pt`。）
- 家具：`tables.py furniture pt --target en --week 2026-W47` 输出 badge / footer / `Página {n} de 8` / `Nota — ` / `— Página {n} —` 与 SVG 逐字一致，VOL.4（见 `furniture.log`）。
- 引号/撇号：弯双引号 SVG 82/82、text.md 81/81；« » SVG 2/2、text.md 4/4；无直引号；U+2019 0；行首标点 0（见 `sweeps2.txt`）。
- 禁词：SOP / proofread / geometry audit / cover / lint / placeholder / TODO / XXX / Lorem 在 SVG 可见文本与 text.md 中均为 0。
- CJK：SVG 可见文本仅 U+3000 ×141（p1 22、p2 18、p3 13、p4 14、p5 13、p6 13、p7 24、p8 24）；text.md 0 处 CJK（见 `sweeps.txt`）。
  注：首轮 `sweeps.txt` 生成脚本漏 `from collections import Counter` 致 NameError，未出数；已重跑通过，见本节数值。
- 陈旧措辞：`Ashes begin`、`Perth is winning!`、`second week in Perth`、`Confirmado em`、`foram decididos`、旧标题 `THE SENATE, IN NUMBERS` /
  `SATURDAY, NOVEMBER 21` 在 text.md / 全部 SVG / registry 中均为 0 命中。`next Sunday` 无适用对象。
- D5 字体（只记录数量，不判）：`pdffonts` 印版 41 个字体对象、网版 41 个字体对象，全部 embedded + subset；
  字体族 NotoSansCJKsc（Regular/Bold）、NotoSerifCJKsc Regular、Newsreader（Regular/Italic/Bold）、UnifrakturMaguntia、DejaVuSans。
- ABSTRACT：未变动，沿用 proof1 核验（完整式，753 字符一行）。

## 11. 全文通读 + 目视

- `2026-w47-en-pt.text.md` 1,305 行：delta diff 仅 l.1151 一行；其余行与 proof1 已通读的本版逐字节相同（registry/text/SVG 三向 diff 已证）。
- 印版 8 页逐页渲染目视（`render/p-1.png` ~ `p-8.png`，72dpi）：除 §6 紧余量三处外，无溢出、重叠、压页脚、图片与出处问题；
  P5 Q73 题干在位，P8 答案块 `73. up` 在位、收尾在页脚之上；P7 栏头、工具盒、读者园地、示例信、NEXT WEEK 均干净；P8 MODEL + Reading Room 图干净。
- 网版 P1/P8 渲染目视（`render/web-p-1.png` / `render/web-p-8.png`）：与印版一致，无豆腐块、无缺字。
- 紧点裁片 3 张（`crops/`）：P2 AND YOU 盒底（`p2-andyou-bottom.png`）、P8 答案 73（`p8-answers-73.png`，SVG x=538.5 y=2276.83，
  印出 `· 73. up ·`）、P5 Q73 题干（`p5-q73-stem.png`，SVG x=538.5 y=1925.1，印出 `Speak ___: tell a teacher.`）；另 P6 HOW LONG 标题裁片（`p6-howlong-title.png`）。
- 本轮渲染 vs delta 渲染逐页像素对比（72dpi，阈值 30；`pixel-compare.log`）：p1–p8 全部 0px 全同——delta 后 PDF 与 delta 渲染件同一。

## 12. 结论

- 机械门：遮挡 0、P8 CLEAN、freeze 核心 8/8 + 版 baseline 8/8 + core 只读对照 8/8、印网 0/0、keycheck 150/150、
  creambox（除 P2 AND YOU 真墨约 +2.2px 紧余量外）清、P8 字号过、框题装得下、check_s11 与 verify_ed 全过——**全部通过**。
- 人工核对：delta 范围恰为一键（registry/text 各 1 行、仅 p8 SVG 变）；Q73 四源一致为 up；150 题 key-vs-stem 手核 150/150；
  8 页逐页目视 + 网版 P1/P8 目视零预期外变化。
- **结论 (a)：本版定稿，零缺陷。** 观察 1–4（KIT 两行旧文案、两处跨栏断行、freeze 口径读数、D5 字体记录）不构成定稿阻碍，报协调员裁定。
