# PROOF-NOTE — 2026-W47 ko-de proof2（独立重校）

- 版：`production/2026-w47/2026-w47-ko-de/`（ko fan-out #3 重建版，未提交）
- 核心：`production/2026-w47/core-ko`（已定稿；本轮只读核查，未重建、未修改）
- 工作区：`hidden_files/w47/scratch-proof-ko-de2/`（下称 `$S`）
- 日期：2026-11-11（proof2，第二轮独立重校）
- 前置：proof1（`scratch-proof-ko-de1`，缺陷 D1–D6）、fix1（`scratch-fix-ko-de1`）、ko fan-out #3（`scratch-fanout-ko3/de`）

## 结论：(b) 不定稿 —— 缺陷全部在 WEEKLY-KIT.md，产品本身全门禁通过

本轮完整重校：全套门禁 16 项全部 PASS；150 题三源一致（REG = P8 SVG = 印版文字层）；8 页印版 + 4 页网版逐页目视零问题；text.md 全文 917 行通读零问题；核心 ko 未变。但 **WEEKLY-KIT.md（129 行重写本）有两处事实错误 + 两处缺失**（K1–K4），按任务书「KIT 缺失即记缺陷，非观察项」，判定为 (b) 不定稿。

**修复量极小**：仅改 `WEEKLY-KIT.md` 四处文字，不需重建、不需重渲、不需改三件交付物；修后只需 KIT-only 复核即可翻 (a)。产品文件（印/网 PDF、text.md）本身无任何缺陷。

---

## 缺陷清单（K1–K4，全部在 WEEKLY-KIT.md 内）

### K1 — KIT “Contents by page” P8 行：E 组 137/138 干题/答案方向写反（事实错误）

- 位置：`WEEKLY-KIT.md` “Contents by page” P8 行：`E 翻译 4 (stems 137/138 in German, keys stay Korean; stems 139/140 in German, keys stay Korean)`。
- 事实（已三源核实）：
  - #137/#138 干题是韩语、答案是德语：#137 干题 `11월 22일은 김치의 날이에요.`（`content8.py:70`），答案 `Der 22. Nov. ist der Kimchi-Tag.`；#138 干题 `삼성이 12년 만에 우승했어요.`（`content8.py:72`），答案 `Samsung gewann den Titel nach 12 Jahren.`。
  - #139/#140 干题是德语、答案留韩语：#139 `Der 18. Nov. ist die Vorversammlung.` → 答案 `11월 18일은 예비소집이에요.`；#140 `Am Sonntag teile ich Kimchi mit der Familie.` → 答案 `일요일에는 가족과 김치를 나눠 먹어요.`
  - 依据：REG 导出（`$S/reg-dump.json`）、P8 SVG 答案行（`$S/proof-keycheck.log` 150/150）、印版文字层（`$S/pdf-keycheck.log` 150/150）、P8 目视。
- KIT 自相矛盾：同一文件 “Fan-out mechanism” 节写的是正确的（`keys 137/138 translated to German; stems 139/140 translated, keys stay Korean`）。
- 风险：后人按错误行“纠正”本已正确的德语答案，会把对的改错。
- 修复：P8 行改为 `E 翻译 4 (stems 137/138 in Korean, keys translated to German; stems 139/140 in German, keys stay Korean)`。

### K2 — KIT “Mechanical gates” 行：SVG 足迹基线写错（事实错误）

- 位置：`WEEKLY-KIT.md` “Mechanical gates”：`SVG hashes de/sha-de-run1.txt (only P1/P4/P7 changed vs #2 run 2 — the core D2/D3/D4 fixes; P2/P3/P5/P6/P8 byte-identical to #2 run 2)`。
- 事实：vs #2 run 2（`scratch-fanout-ko/de/sha-de-run2.txt`），变化的是 **P1/P2/P4/P7** 四页；P2 的变化正是 fix1 的 D5（`92390ad4… → cfab7ef1…`，gloss `작황 = Ernteaussichten` 改动）；P3/P5/P6/P8 才与 run 2 字节一致。
- 正确表述是 vs fix1 后 SVGs（`scratch-fix-ko-de1/sha-svg-fix1.txt`）仅 P1/P4/P7 变化（核心 D2/D3/D4 流过）。KIT 把两个基线混在了一句里。
- 实质无碍（无未解释的变化），但字面错误；修复：改为 `only P1/P4/P7 changed vs the fix1 SVGs (core D2/D3/D4 flow-through); vs #2 run 2, P1/P2/P4/P7 changed (P2 = fix1 D5)`。

### K3 — KIT “Self-proofread record → History”：fix1 的网版与 text.md SHA/尺寸缺失

- 位置：同节仅记录了 fix1 印版 `45,682,367 B, SHA c19fe6c1…`（已作废），未记录 fix1 网版与 text.md。
- 缺失值（取自 fix1 `FIX-LOG.md` / `GATE-LOG.md`，本轮已复核与 fix1 记录一致）：
  - fix1 网版：`Lucerna-VOL4-KO-DE-web.pdf`，`4,036,008 B`，SHA-256 `375f0cf7a179e2ac4e5e0e7eb39724a41eb0a377bc3257da1ea17f58f641d9f4c`
  - fix1 text.md：`35,052 B`，SHA-256 `a7641374d6f3c190f98c4c4c107b36436fd8e74a63d06fb126a07bbebbc6ef68`
- 修复：在 History 段补记以上两行（注明已作废、现行 SHA 见 “Output files” 节）。

### K4 — KIT 未收 fix1 FIX-LOG 的 brief 路径注记（次要缺失）

- fix1 `FIX-LOG.md` “固定事实 / KIT” 段注明：任务书给的 brief 路径不存在，实际路径在 goals 侧 `hidden_files/w47/scratch-briefs/`，且“已记入 KIT fix1 节”。重写后的 129 行 KIT 未收此注。
- 修复：在 KIT fix1 历史或 “Fan-out mechanism” 相关处补一行（brief 路径以 goals 侧为准）。

---

## SHA 复核（开工前 + 收尾，全部一致）

| 文件 | 尺寸 | SHA-256 | 结果 |
|---|---|---|---|
| 印 `Lucerna-VOL4-KO-DE.pdf` | 45,682,430 B | `28dbc2e775883e64e4a6b482c9da37932d3c803264ba2d9e0ef76d4052cf7cc5` | ✓ 与任务单一致 |
| 网 `Lucerna-VOL4-KO-DE-web.pdf` | 4,035,158 B | `0b309527f4beb78272a969d153c285af77e5d65c27e520c28a5959fe4a8a45c7` | ✓ 与任务单一致 |
| `2026-w47-ko-de.text.md` | 35,162 B，449 项 | `a192156f3c49576611f4392b9c7883c8408dfa3da8519a811cbcbec0eb87917c` | ✓ 与任务单一致 |
| `ABSTRACT.txt` | 350 B | `2d7ba827b0d051ff1647668c108883dfca05deb7fd5e7f51174a5135a3f9a7c6` | ✓ 单行德语，无 ASCII 双引号，含刊名/目标/A2–B2/150 |

核心 ko 未变（只读核查）：印 46,232,227 B SHA `53bf14ed…`、网 4,232,878 B SHA `9592945a…`、text.md 34,606 B SHA `da1d3a32…`，均与 proof5 / fix-core2 记录完全一致；8 页 SVG 哈希与 proof5 逐页一致。核心 KIT 自记的旧 PDF SHA（`7b004b36…`/`e9c1ca0c…`）是 run 11 之前的值，已过期，非本次问题。

---

## 门禁逐项结果（全部 PASS；独立重跑，日志见 `$S`）

| # | 门禁 | 结果 | 日志 |
|---|---|---|---|
| 1 | run.py（系统 python3，独立重建） | rc=0，0 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；每页 10/18/18/18/18/18/12/38；类型 Satz ergänzen 48、Auswahl 52、Paare zuordnen 16、Umformen 4、Sätze bilden 8、Richtig oder falsch 4、Lückentext 13、Übersetzen 4、Schreiben 1）；P2-feature 末 1531（限 1540）、P8-keys 末 2457、P7 teaser 末 2539.22（页脚 2580，余 40.8px）；H 模型 169 字；重建 8 页 SVG 与生产版字节一致 | `rebuild.log`、`sha-svg-rebuild.txt` |
| 2 | freeze baseline（系统 python3） | **8/8 字节一致** | `freeze-baseline.log` |
| 3 | freeze diff（核心 vs 本版 SVG） | 新增 CJK **7 个，全部 U+3000**；逐页 P1: 0、P2–P8: 各 1；原始计数印证（核→版：P1 19→19，P2 17→18，P3 14→15，P4 13→14，P5 14→15，P6 13→14，P7 13→14，P8 14→15）；载体为页脚（版页脚 3×U+3000 vs 核 2×；P1 有一处抵消净 0）；新增/删除串全部是德语解释层，无新增韩语内容 | `freeze-diff.log`、`freeze-diff.json` |
| 4 | p8 extract | **150/150** 已注 | `p8-extract.log` |
| 5 | p8 compare vs 核心 | **CLEAN**；missing=[]、extra=0；keydiff=[137, 138]（E 组重定向，W46 ko-de 前例） | `p8-compare.log` |
| 6 | 独立 keycheck（自写脚本，REG vs P8 SVG 答案行） | **149 exact + #150 `✓`（预期，与核心一致）= 150/150，BAD 0** | `proof-keycheck.log`、`reg-dump.json` |
| 7 | PDF 文字层 keycheck（第三源：印版 `pdftotext` 文字层 vs REG） | **149 exact + #150 `✓` = 150/150，BAD 0**（初版 2 处 BAD 均为 checker 伪影：页脚行被误并入 #16 注、#150 未特殊处理；修 checker 后通过） | `pdf-keycheck.log` |
| 8 | check_core / check_gloss | gloss fails 0，orphan issues 0；P7 句 8/8 逐字（含新句 #7 `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` (1면)）；日期全对 | `check-core.log`、`check-gloss.log` |
| 9 | textmd 重导出 | 与发货 text.md **字节一致**，449 项 | `textmd.log`、`textmd-reexport.md` |
| 10 | 印/网文字层一致 | plain 各 **52,078 B、字节一致**；`-layout` 各 107,221 B、字节一致 | `print-plain.txt`、`web-plain.txt`、`print.txt`、`web.txt` |
| 11 | P8 最小字号（PyMuPDF，印版） | **9.975pt**（答案区 y≥1302/2700，173 spans，168 个在 9.975pt）≥ 9.75pt 阈值；P8 整体最小亦 9.975pt | 见 GATE-LOG |
| 12 | boxtitle | **8/8 ≤ 386.5px**（最大 345.7px P5 Jugendzahlen；P3 Wichtig 319.6、P7 Muster der Woche 341.3） | `boxtitle.log` |
| 13 | occlusion audit | **0 flags**；selftest 正常（6 类触发，干净对照静默） | `occlusion.log` |
| 14 | census | ex/match 166 项，0 缺失；D6 0 缺失 | `census.log` |
| 15 | §1.1 grep audit | 纸 `#fbfaf6`、VOL.4、`·` 计数与核心逐页一致；P7 VOL.5 3→2 系设计（去 `lko`/`lcn2`）；`<text>` 内汉字 0；U+2019 0；颜色集逐页一致 | `style11.log` |
| 16 | 孤儿标点全扫（8 页 SVG，`<text>` 内） | U+2019/U+201C/U+201D 各 0；独行 `。`/`”`/`：`/`–`/`—` 各 0；残留汉字 0 | 见 GATE-LOG |
| 17 | creambox 逐盒裁定 | 全部裁定；所有负数汇总间隙均为已记录的假阳性模式（BELOW-WINDOW 下一区块标题 +26…+44，盒内间隙为正）；P7 工具箱：3 盒，盒内最小 +12.5，desc 余 +6.5；三处紧 Und-du 盒（P2 +5.7/desc −0.3；P3/P5 +5.1/desc −0.9）比核心同类盒更宽松（核心 +4.5/desc −1.5）——继承几何、亚像素降部区，非缺陷；P2 购物清单盒末 1473.9（底 1518.9，盒内 +45.0），全在 D-day 条（y=1618）之上；D-day 条格内 +15.9、desc +10.2 | `creambox.log`、`creambox-core.log` |
| 18 | 150 题手验（三源） | 见上 #6/#7；REG、P8 SVG、印版文字层三源一致 | `reg-dump.json` |
| 19 | 8 页逐页目视（印版）+ 网版 P1/P2/P7/P8 | 零问题（见下） | `pages/p-*.png`、`webpages/w-*.png` |
| 20 | text.md 全文通读 | 917 行全读；日期/星期、百分比（199,456/219,071 = −9.0%；54,980/74,800 = −26.5%）、G1–G5 比分（8-7、3-2、5-1、10-5、12-1）、4승 1패、4연승、季后赛梯级、计数均与 proof1 核实事实及 KIT 一致；无新事实问题 | — |

注：creambox.py 规范版 md5 `ee7a55d8b2057cf4ad42a97bb1197383`，取自 `hidden_files/w47/tools/creambox.py`（不在 `~/workspace/weekly-git/tools/` 下，与整合文档措辞不符，工具位置注记）。

---

## 承接项逐项重验（D1 / D5 / freeze-CJK-7 / SVG 足迹 / KIT）

### D1 ✓
`content7.py:81` 恰为 `wcn = "Rahmen: 「nach ~」. Frag: 「〜 후에 뭐 해요?」"`；P7 SVG ×1、text.md 第 761 行 ×1；弯引号形 `“nach` 在两处均为 0。P7 目视可见该行。

### D5 ✓（内容）；D5 字体只记录、不计入判定
`content12.py:174` 恰为 `f.gloss("조사하다 = untersuchen · 작황 = Ernteaussichten · 이어지다 = weitergehen · 할인 = Rabatt")`；`Ernteaussichten` 在 P2 SVG 与 text.md 各 ×1；`die Ernte` 在两处均为 0。P2 目视 gloss 盒三行装得下（见 KIT 修复记录 #1 三行形式）。字体：任务书定“只记录、不计入判定（生产级待定项）”——本轮 8 页印版 + 4 页网版目视无缺字/豆腐块，文字层完整；生产级字体待定项本身无新证据可裁定，照任务书不计入判定。

### freeze CJK 7 ✓（逐个分类）
7 个新增 U+3000 全在页脚层：版页脚 `Lucerna　KOREANISCHE WOCHENZEITUNG VOL.4　Koreanischer Text　Erklärungen auf Deutsch` 含 3 个 U+3000，核心页脚含 2 个 → 每页 +1；P1 因带区副标一处 −1 抵消净 0。新增/删除串逐条核对：全部是德语解释层（`Nach der CSAT kommt der Kimchi-Tag. (1면)`、`Hinweis der Redaktion: …`、`Vor den Ergebnissen …` 等），无新增韩语内容。P2–P8 各 +1、P1 0，与原始计数逐页吻合。

### SVG 足迹
- vs #2 run 2：变化 **P1/P2/P4/P7**；P2 的变化正是 fix1 D5（`92390ad4… → cfab7ef1…`）；其余 4 页字节一致。无未解释变化。
- vs fix1 后 SVGs：仅 P1/P4/P7 变化（核心 D2/D3/D4 流过）。
- KIT “Mechanical gates” 行把上述两个基线混写（见缺陷 K2）。

### 核心 D2/D3/D4 流过 ✓
- ex 10（P1，`content12.py:157`）与 ex 47（P4，`content34.py:199`）均为 `한국시리즈에서 우승한 팀은 어느 팀이에요?`；ex 48（`content34.py:201`）为 `한국시리즈 전적은 어떻게 돼요?`（无重复 `시리즈`）。
- P7 句 #7（`content7.py:127`）为新句 + `(1면)`；框架例句（`content7.py:80`）为同一句。

### text.md D6 修复确认 ✓
P7 读者来信文本在场（第 765 行 `「안녕하세요. 저는 수험생이에요.…」 — 독자 편지의 예`），德语披露在场，框架例句 + `Rahmen:` 行在场（第 761 行）。proof1 的 D6 缺口（textmd.py 漏 `wt`/`wcn`/`lt`/`lcn`）已由 textmd fix2 修好；本版 `textmd.py` 与核心字节一致（md5 `bc6394a387d15d4726e194687320da20`）。

### H 模型 ✓
169 字（不计空格，`content8.py:109` 的 `NCHARS = len(MODELO.replace(" ", ""))`），在 150–200 范围内；P8 目视 H 区写明 “169자의 예가 있어요”。

---

## KIT 完整性核查（129 行 / 19,906 B 重写本，逐项）

逐项对照：fix1 `FIX-LOG.md` + `GATE-LOG.md`、ko3 `EDITION-RECORD.md`（含 150 题表）、#2 `EDITION-RECORD.md`、本轮独立重跑结果。

**核实无误的 KIT 断言**（抽样/全部重验）：
- 门禁表、SHA 与尺寸、修复记录 #1–#6（D1/D5/D2–D4/gloss 缩短/标题缩短/map 坑）、已裁定项（P8 字母重复、Weatheri-Prognose、#150 ✓、P7 VOL.5 3→2、text.md 449 vs 452 三处扣除、freeze CJK 7、P2 购物盒、#7 短注、KEYS_HALF/NOTE_WRAP、P8 10.35pt 干题字号、`___` 23 处）、occlusion 审计、输出文件、未决核查债；
- 数字核实：等级徽章 **138 个、P8 35 个**（按徽章尺寸矩形实测，逐页 10/15/15/15/18/18/12/35）；`svglib.py` 与核心 md5 一致（`1c94d836…`）；textmd.py md5 `bc6394a387…` 与核心一致；P7 teaser 余量 40.8px；H 模型 169 字；`___` 23 处；
- text.md 449 vs 核心 452 的三处扣除核实：`Alle`（P1 目录 8면 行等级，`is_prose` 滤掉的纯 3 字母拉丁词；SVG/PDF 正确渲染，P1 目视可见）+ `lko`/`lcn2`（`content7.py` 中 grep 0，已移除；单行德语 `lcn` 在场，第 91/98 行）；
- “Map hygiene: 216 值 0 双空格/边空格”——渲染层实测 8 页 SVG `<text>` 内 ASCII 双空格 0，实质性核对通过（map 文件本身不在版目录，属 builder scratch 资产）。

**有问题的 KIT 项**：即缺陷 K1–K4（上文）。除此之外无缺失。

---

## 目视记录（8 页印版 + 4 页网版）

- **P1**：干净。刊头、蛾标、头条带、首字下沉、数字盒、日历、目录、本周词、照片+图注、短讯、quiz 7–10；ex 10 干题正确；页脚正确。quiz 指示行无句号（`…Antwort　Antworten auf Seite 8`）为家族版式遗留，非缺陷。
- **P2**：干净。D5 gloss 可见 `작황 = Ernteaussichten`（3 行装盒）；购物清单盒末 1473.9，全在 D-day 条（y=1618）之上，间隙清晰；D-day 条 4 格干净；练习 11–28。
- **P3**：干净。第 2 栏顶 `않았어요.` 为第 1 栏段落的正常跨栏续行，非孤儿标点（check_core 孤儿扫描 0）；两图+图注正常；练习 29–46。
- **P4**：干净。ex 47 `어느 팀이에요`、ex 48 无重复 `시리즈`；梯级图干净；照片+图注正常；第 4 栏下半空白与核心同版式（feature 末 740，继承）。
- **P5**：干净。feature 末 881，下方空白与核心同版式；练习 65–82。
- **P6**：干净。对比表 3 行渲染正确；ex 92 C 项 `3,271명` 是核心原有（`content56.py:206`），本版继承，非本版问题；练习 83–100。
- **P7**：干净。D1 框架行可见；句 #7 为新句 + (1면)；读者来信盒 + 德语披露在场；Fehlerklinik 4 项；teaser 余量 40.8px；照片带正常。
- **P8**：干净。150 个答案全在；H 模型 + 照片在第 4 栏；#150 `✓` 行在场；E 组干题方向目视确认（137/138 韩语干题、139/140 德语干题）。
- **网版 P1/P2/P7/P8**：与印版一致，无缺字、无缺图、无豆腐块。

---

## 观察项（非缺陷，记录备查）

1. **textmd.py 去重行为**（共享工具，核心亦然）：按归一化文本去重，源文件 7 处重复 `.ex` 干题在 text.md 只出现一次（如 `어느 팀이에요` 干题：源 2×——P1 quiz #10 与 P4 ex 47——text.md 1×，第 149 行；text.md 的 P4 练习表从 ex 48 起）。核心 text.md 行为相同（1 处，第 151 行）。PDF/SVG/P8 答案完整；census（存在性检查）0 缺失。
2. **#2 EDITION-RECORD.md 文件节笔误**（builder 记录，非产品）：误贴 ko-en 版文件名/哈希；proof1 已注，fix1 已注“供协调员转达”；本轮未动他人 scratch 目录。
3. **creambox.py 位置注记**：规范版在 `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b…`），不在 `~/workspace/weekly-git/tools/` 下，与整合文档措辞不符。
4. **P3 栏顶续行**（见 P3 目视）、**P1 quiz 指示无句号**、**P4/P5/P6 栏下空白**、**ex 92 `3,271명`**：均为核心继承或家族版式，非本版缺陷。

---

## 清理

按本地存储规矩：可复现中间件已删（`$S/rebuild/` 11M、`$S/freeze/` 68M）；保留日志、PNG、脚本、`reg-dump.json`、`freeze-diff.json`、SHA 记录（现 $S 共 19M）。生产文件只读，未改、未 commit、未 push。
