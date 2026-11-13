# 门禁日志 GATE-LOG — W47 zh-cn-ko（简体中文读者 × 韩语目标）独立 proof2（re-proof）

- **对象**：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ko/`（fix1 后新构建）
- **核心对照**：`production/2026-w47/core-zh-cn/`（已定稿）
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-zh-cn-ko1/`
- **解释器**：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；`TMPDIR` 一律指向本 scratch；`PYTHONDONTWRITEBYTECODE=1`

## §0 开工三 SHA（开工与收尾两次实测一致）

| 文件 | SHA-256 | 字节 |
|---|---|---|
| 印 `Lucerna-VOL4-KO.pdf` | `69744432ab7424ee8b1e8553d1e75e49c1601c34583e91a277bdb1030593ff30` | 36,966,247 |
| 网 `Lucerna-VOL4-KO-web.pdf` | `bbf0d14d05f2daab9437373b9082e127993dd7eb39eafd023efd60785d7fe02a` | 2,817,987 |
| 文 `2026-w47-zh-cn-ko.text.md` | `eb5fdedda37c2b9feec54c8b89098e1eeaff4f8760a3038507c728013b3063c0` | 52,725 |

与任务书开工三 SHA 逐字节一致。收尾 `snapshot-end.txt` 与开工 `snapshot-start.txt` diff 为空；生产 SVG sha256 开工=收尾（`svg-sha-start.txt` vs `svg-sha-end.txt` diff 空）。磁盘探针：`git hash-object -w /dev/null` 成功（`e69de29…`），scratch 真实写盘 `probe.txt` 成功，磁盘 57G 空闲。fix1 改动核对：与 proof1 修前快照对照，仅 p5 变（`557d7998…` → `9f22432094129549f127da31d2fc801c9395891800a36125aabec6ea6be0bd26`，与 fix1 声称的新 SHA 一致），其余 7 SVG 逐字节一致。

## §1 run.py scratch 重建（独立，OUT 已重定向）

- `rebuild/` 副本，`OUT` 重指向 `$SCRATCH/rebuild/svg`（绝对路径，先验为自己的 scratch；render.py 的 BASE 未动，本轮未跑 render.py）。
- **rc=0，TOTAL 150**（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38；类型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1）。
- **0 FLOW OVERFLOW，0 HEAD TOO WIDE**；P7 teaser 终值 2531.76；P8 keys flow 终值 2475.7（容量 2560，余 84.3）；P8 测验流 964.8；范文 138 字。
- 重建 SVG 与生产 SVG **sha256 8/8 字节一致**（`run-rebuild.log`）。
- 披露：第一轮重建时本人 sed 重定向丢了引号致 SyntaxError（仅 scratch 副本，生产未动）；修正引号后重跑成功，终值有效。

## §2 gates-zhcn.py 11/11 ALL PASS（`gates-ko.log` / `gates-ko.json`）

| 门 | 实测 |
|---|---|
| occlusion | rc=0 flags=0，`svg/: 0 flags` |
| img_overlap | hits=0 |
| p8_extract | rc=0 noted=150/150 |
| p8_compare | rc=0 verdict=**CLEAN** keydiffs=0 |
| freeze_sha256 | run rc=0 match=8/8 |
| print_web_text | pages 8/8 posdiff=0 msdiff=0（P1 253/253，P2 263/263，P3 205/205，P4 263/263，P5 208/208，P6 229/229，P7 280/280，P8 998/998） |
| pdftotext_nonempty | print=46,012 B web=46,012 B，web_size=2,817,987 |
| p8_fontsize | answer-zone min=**9.98 pt**（≥9.75），median 9.98 pt，spans=1000 |
| p8_chips | core={A2 11, B1 24, B2 3} = edition={A2 11, B1 24, B2 3} |
| u2019 | files_with_U+2019=[] |
| s11_svg | off-palette={}，gold/old=False，stroked_rects=0，VOL.5=1（core 1），paper_fills=8 |
| OVERALL | **ALL PASS** |

## §3 freeze baseline（核心）

- `tools/freeze.py baseline --build production/2026-w47/core-zh-cn --core-svg production/2026-w47/core-zh-cn/svg --out $SCRATCH/freeze-baseline`：**8/8 SVGs byte-identical**，`core integrity: shipped core SVGs unchanged by the run`（`freeze-baseline.log`）。build-copy 已核实确为核心版（`content56.py` 含 `Words of the week` 1 处，韩文串 0 处），绝非自比。

## §4 freeze diff + Hanzi 核算

- `freeze.py diff --strict-cjk`：TOTAL added CJK **4038**（p1 322，p2 323，p3 215，p4 264，p5 219，p6 306，p7 660，p8 1729）——p5 较修前 221 少 2（本次韩文净变：去 `자주 나오는`、加 `고빈도`）；其余 7 页与 proof1 逐值一致，全部为解释层 Hangul，**预期、已裁定**（rc=1 仅因此项）。
- Hanzi-added 核算（`hanzi_ko.py`，与 freeze 同口径 multiset，只计 U+4E00–U+9FFF）：**added Hanzi = 0，8 页全过**（p1 739→725，p2 913→909，p3 752→748，p4 647→643，p5 802→798，p6 787→783，p7 618→612，p8 962→944；与 proof1 逐值一致；`hanzi-ko.log`）。

## §5 occlusion 自检

- `--selftest`：**OK**，planted 六类全触发 `{BOXTITLE: 1, COVER: 1, EDGE: 1, FOOTER: 1, LINEX: 1, TEXTX: 1}`，clean 对照静默（`occlusion-selftest.log`）。
- 本版 0 flags，核心 0 flags。

## §6 D-01 三法独立重测（`measure_d01_reproof.py`，自写脚本，交付印 PDF 为准）

- 盒 rect（交付 SVG 实读）：`x=538.5 y=618.32 w=422.5 h=168.0`，盒右 961.0；标题（实读）：`x=556.5 y=655.32 size=23 weight=700 fill=#46581f`，`这一周的高频词　이번 주 고빈도 단어`。
- **A. PIL 真墨**：advance 372.6，ink_right **929.5**，**余 +31.5 px**。对照：旧串同法 advance 421.3、墨右 977.5、越 16.5 px（与 proof1 修前值逐值一致，口径有效）。
- **B. 交付印 PDF 渲染像素**（150 dpi，`render-p5-150-reproof.png`）：奶油右缘连续段实测 **960.0** svg 单位（盒右 961.0，差 1 单位舍入）；标题最右墨 **922.2** svg 单位，**余 +38.8**（对奶油实测缘 +37.8）。
- **C. PDF 文字层**（PyMuPDF，1462.5 pt → ×4/3）：韩文 run `이번주고빈도단어` 止于 694.1 pt = **925.4** svg 单位，**余 +35.6**。
- 三法余量均 ≥ +5 px 门槛（最低 +31.5）；B 法与 fix1 声称差 0.7 svg 单位，为光栅化取整口径差。
- 目视：`crop-p5-head-reproof.png`（2× 放大）——标题完整落在奶油盒内，右缘留白清晰。

## §7 奶油盒横向真墨扫（PIL，599 个盒内文本元）

- **OVERFLOW: 0**；tight (<8 px): 0。
- D-01 已修：P5 高频词盒标题余 +31.5 px（见 §6）。

## §8 奶油盒纵向真墨扫（PIL anchor='ls'，599 个盒内文本元）

- **V-OVERFLOW: 0**；tight (<8 px): 5（`cream-sweep-v.log` / `cream-sweep-v.json`）。
- 最紧：P2 y=1133.9 / P3 y=1293.4 / P6 y=1064.5 均为余 2.5 px（`…중국어로 두 문장 써 보세요.`），P5 y=1215.8 余 3.1 px（`세요.`），P7 y=1143.0 余 7.9 px。韩文无下行字母，墨底严格在盒内——记观察 O-1，不列缺陷。

## §9 绿字粗体标题横扫（251 个）

- 全版绿字（#46581f）粗体标题 PIL 真墨 vs 所在栏右缘：**越栏仅 4 处**，均为通栏设计——P1 刊头 `简体中文版`/`S16`（y=330 居中刊头）、P6 图表通栏标题 `快递量：22天总数和一天最高量…`（x=88，核心同位同 x）、P7 金句通栏带、P1 刊头副行；核心同形同位，不属溢出（`heads-scan.log`）。
- 其余最大墨右 1840.1（P1 目录 B2 行），< 1862。

## §10 spill 扫（版心 MX=88 / RIGHT=1862 / CONTENT_BOTTOM=2560）

- PIL 真墨：ko 19 flags，core 17 flags（`spill-orphan.log`）。
- 逐项核对：17 处与核心同位同量（页脚 `제N면／전체 8면` 右 1862.1、栏目标题左 87.0 等，均为 ≤0.5 px 的 bbox 舍入噪声）；ko 新增 2 处经 PDF 文字层逐项证伪——P1 `1쪽을 읽고 고르세요　答案见第8版` 文字层实测止于 1859.8；P2 `모든 쇼핑 앱에서 보게 될 네 단어` 文字层实测止于 1855.3。
- P8 `모든 설명은 한국어로　✓ = 작문 과제` PIL 1870.1，核心同位 `All notes in English　✓ = the writing task` PIL 1871.1（核心更大）；PDF 文字层实测 ko `✓= 작문과제` 止于 **1858.8**，在版心内。
- **结论：真实 spill 0 处**。

## §11 孤儿扫（行首闭合标点，精细口径：按栏分组取行首元，本轮自写 `orphan_refined.py`）

- ko **0 处**、core **0 处**；ko 新增孤儿 0 处（`orphan-refined.json` / `orphan-refined.log`）。
- 粗口径（逐元首字）ko 325 / core 107 均为行内碎片（P8 键流 `.` / `, a` 等），非行首孤儿，不作数。
- Q130/Q36/Q37 式孤儿填空行属核心继承、观察类，不修不报。

## §12 P8 打包

- `p8.py extract`：**150/150**（`p8extract.json` / `p8extract.log`）。
- `p8.py compare` vs 核心：**CLEAN**，missing=[] extra_count=0 uncertain=[] **keydiff=[]**（`p8compare.json` / `p8compare.log`）。任务书预期的 keydiff [137,138,139,140] 未出现——E 组 137–140 键为中文句（`7.77` / `14` / `GEN` / `冷`），与核心逐字一致；实测为准，记观察 O-3。
- keycheck（REG vs P8 抽取）：**149/150 精确**，唯一非精确为 Q150（REG 键 `(开放题，范文如下)` vs 印键 `✓`，开放写作题按设计；核心 P8 同为 `✓`，compare keydiff [] 佐证）（`keycheck-150.json` / `keycheck.log`）。
- Q150 P8 实印全键重组核实：F 部分范文与核心**逐字一致**（本轮独立重数：总长 138 字，CJK 107 字；标签仅 `모델 답안:` vs `Model answer:` 之差）。`138자/138 characters` 计数与 `writing model chars: 138` 一致。

## §13 150 题三方手验（registry vs text.md vs P8）

- 题干中文与核心：**150/150 字符串全等**；键 150/150 与核心同值；level/type/opts 0 差异（`stem-compare.txt`，`stems-ko.json` vs `stems-core.json`）。
- 配对题 5 组 20 键逐组核对选项原文**全对**：Q25–28 a/b/c/d（到货/退换货/价保/派送）；Q43–46 b/d/a/c（小雪=11月22日节气、三候=古人看天三变化、保暖=天冷多穿、着凉=冷到不舒服）；Q61–64 d/b/c/a（四强=最后四支队、止步=半决赛输了不往前、闹钟=到时间响、五局三胜=先赢三局）；Q79–82 c/b/d/a（试探=试着问、悬疑=猜不透发紧、失踪=人不见了、别墅=山里独栋）；Q97–100 c/d/a/b（说法=别人说的话、数据=量出来的数字、预报=还没发生先猜、预计=大概数字未数完）。
- 完形对错 Q113–Q120 全对（见 PROOF-NOTE §F）；Q90 键「二十二」为中文数词写法，REG 与 P8 抽取一致，不作缺陷。
- 注释 150 条均为韩文（Q150 注为 fstring 展开值 `자유 과제 — 모범 답안은 위 F 부분에 있습니다(138자)`；拉丁串仅队名 BLG/GEN/IG/TES/DK、拼音、Worlds BO5 等合法项）。

## §14 D4 / D5 措辞落地（核心继承，只核对存在性）

- **D4**：`全球总决赛的BO5`——P4 正文 `:695`、Q56 题干 `:817` 各 1 处；全文「第一次」仅此 2 处，均带限定；Q56 键注 `:1905` 韩文带 `Worlds BO5` 限定。**核心继承已落实**。
- **D5**：`GEN在S16一场没输，只丢了一小局`——P1 `:37`、P4 `:697`；`对LYON 2比1`——P4 `:697`；`淘汰赛一局没输`——P4 小日历 `:729`；假表述 `GEN今年一场没输` **0 处**。**核心继承已落实**。

## §15 日期星期全验（`date -d`，2026 年）

- 11月4日周三、5日周四、6日周五、7日周六、8日周日、9日周一、11日周三、14日周六、15日周日、21日周六、22日周日。
- 文中星期断言全相符：`11月8日星期日`（2 处）、`11月9日星期一`、`11月15日星期日`（3 处）、`11月22日星期日`（6 处）、`11月21日星期六`（2 处）、`11月11日星期三`、`11月14日星期六`；Q107 选项 A「11月22日星期日」✓。22 天口径：10月21日—11月11日含首尾共 22 天。
- 金句 8 条各出现 2 次（正文 + P7，机械计数）：`决赛对阵GEN`、`包裹都到了吗`、`小雪气寒而将雪矣`、`两支中国队进了四强`、`先看简介，再决定`、`无高峰，全高峰`、`先打开看一看，再确认收货`、`悦读深圳`。
- "next Sunday"：text.md 0 处，SVG 0 处（冻结核心，无此项）。

## §16 字号 / 徽章 / §1.1 / ABSTRACT

- 各页最小字号（交付印 PDF 文字层，印/网一致）：P1 10.50、P2–P5 11.62、P6 12.75、P7 11.62、**P8 9.98 pt ≥ 9.75 pt** ✓（`minfont.log`）。
- 徽章（P1 y=434，14 pt bold）：`중국어 간체 텍스트　한국어 해설 — 한국어 독자를 위한 판`，**0 汉字** ✓；页脚 ×8：`Lucerna　简体中文周报 VOL.4　LUCERNA — 간체 중국어 주간지` + `제{n}면／전체 8면` ✓；P8 分隔 `— {n}쪽 —`、P7 金句 `(p. N)` 在位；注释前缀 `참고｜`。
- §1.1：调色板干净（off-palette {}，无禁用色、无描边矩形），VOL.5 计数 = 核心（1 处，下期预告），纸色 #fbfaf6 ×8。
- ABSTRACT.txt：314 B，尾换行在位，与表值 + `\n` 一致。
- U+2019：0（SVG + text.md）。
- P1 截稿行：各行余 37.3–377.5 px，末行余 44.5 px（本轮直测；proof1 报 40.5 px，差 4 px 为 PIL 口径差，见 PROOF-NOTE O-5）。
- P8 答案头：墨右 504.0、栏右 510.5，余 6.5 px（本轮直测；proof1 报 2.5 px，差 4 px 为 PIL 口径差，见 PROOF-NOTE O-2）。

## §17 目视（交付印 PDF 110 dpi 全 8 页 + 网 P1）

- P1：徽章韩文-only、截稿段、数字盒、日历、目录、本周词均正；首段栏尾「每」为跨栏续接（次栏首「周，我们用简单的中文…」），非截句。
- P2：日历标题离照片、4 词卡、练习 A–D 齐全；「说说你自己」盒尾行贴盒底 2.5 px，目视在盒内（O-1）。
- P3：三候、读书月、日历、练习齐全；「小雪三候，怎么记」段栏尾「一候虹藏不」为跨栏续接（次栏首「见—雨少了，彩虹不见了；…」），与核心 P3 渲染逐项对照同位同形，非截句。
- P4：gloss、赛程表、D4/D5 措辞、图注「2003年」均正；脚注行通栏在位。
- P5：D-01 已修（标题落盒内，见 §6）；片单（撤档案在位）、高频词盒、C head `时间与数字　시간과 숫자`、电影小日历、练习齐全。
- P6：三波/139.38/7.77、图表、深读要点、三问齐全（图表两柱非等比为核心继承设计，O-4）。
- P7：诊所、句式框、金句 8 条、下期预告条底 2531.76 清页脚；读者园地为编辑部示例信（未收到真实来信，符合 F-MAIL 规则）。
- P8：A–F 齐全，keys 1–150 + 页脚清；Q150 范文 + 配图在位。
- 网 P1 与印 P1 目视一致（同 SVG 源；文字层 8/8 posdiff 0 msdiff 0）。

## 汇总

- **17 门全部通过；缺陷 0 项；观察 5 项（O-1～O-5，不计缺陷）。**
- 结论：**(a) 零缺陷，可定稿**，见 PROOF-NOTE.md。
