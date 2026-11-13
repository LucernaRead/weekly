# PROOF-NOTE — 2026-W47 ko-zh-tw proof1（独立复校）

- **版**：`2026-w47-ko-zh-tw`（target ko，reader 繁體中文），来自 ko fan-out #3 run 1 新版
- **复校员**：独立（与构建者/fan-out agent 不同人）；复校时间 2026-11-11 13:53–14:30 UTC
- **工作区**：`hidden_files/w47/scratch-proof-ko-zh-tw/`（只在 goals 侧写；生产目录零写入）
- **结论：(a) 定稿零缺陷** — 全部门禁独立重跑通过，150 题三源 0 不符，8 页逐页目视 0 问题

## 1. SHA 复核（三件，复核前后各测一次，均与任务书一致）

| 文件 | 字节 | SHA-256 | 结果 |
|---|---|---|---|
| 印 `Lucerna-VOL4-KO-ZH-TW.pdf` | 46,280,042 | `180d3ce0ef35f88aef9842e30835b29c77f0b7d5082e6529f9255f019610a949` | ✓ 一致 |
| 网 `Lucerna-VOL4-KO-ZH-TW-web.pdf` | 4,348,626 | `cfe20ece5a19f03e9ec7e3593c8fced61eae3f78d7eb19fdd09ba9d0729a78ab` | ✓ 一致 |
| text `2026-w47-ko-zh-tw.text.md` | 34,637 | `af183ae64f665c405f86a54edf1a76315f80901e9fac615f7ba9b7cd70c453e2` | ✓ 一致 |
| ABSTRACT.txt | 268 | `88f967a1267da0e6b6b352582fea454de11a31ce171b5a46c0d67311b34d7767` | ✓ 与 FANOUT-REPORT 一致 |

**core-ko 复核前后未变**（`core-sha-before.txt` / `core-sha-after.txt` 哈希相同）：
印 `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`（46,232,227 B）；
网 `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7`（4,232,878 B）；
text `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a`（`2026-w47-ko-zh-cn.text.md`，34,606 B，452 项）。

## 2. 本版 carry-forward：freeze diff +822 CJK 裁决（独立重算 ✓）

- freeze diff 用 **系统 python3（Pillow 10.2.0）独立重跑**（builder 用 venv 跑，结果逐字相同，证明 diff 与解释器无关）：
  p1 +47 / p2 +66 / p3 +49 / p4 +60 / p5 +56 / p6 +42 / p7 +97 / p8 +405，**合计 +822**；
  字符串 +267 / −268（p1 16/16、p2 23/23、p3 18/18、p4 17/17、p5 17/17、p6 12/11、p7 26/28、p8 138/138）。
- 用我自己写的 tracer（`trace-freeze-diff-proof1.py`，对我的 diff JSON 全量追踪；
  来源宇宙：`map-zh-tw.json` 的 map/instr 值、两版 `.py` 字符串字面量、页码行、
  譯注｜前缀、H 范文渲染串、`(N면)` 引用后缀、` — ` 答案行复合拆分）：
  **added 未解释 0，removed 未解释 0**。builder 原 verifier 在我的 diff JSON 上复跑亦为 0/0。
- 结论：+822 全部为简→繁脚本转换 + 繁体新增串，裁决成立，0 未解释。

## 3. 门禁汇总（全部独立重跑，证据见 GATE-LOG.md / 同目录日志）

| 门禁 | 结果 |
|---|---|
| run.py（系统 python3，工作区副本） | rc=0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；每页 10/18/18/18/18/18/12/38）；P8-keys 止 2351，P7 teaser 2425.7；8 张 SVG 与交付逐字节相同 |
| freeze baseline（系统 python3） | **8/8 逐字节相同**（rc=0；参照=本版自有 svg 目录。注：首跑误以 core-ko/svg 为参照得 0/8——那是参照取错，本版 SVG 与核心本就差 +822 CJK；纠正参照后 8/8。另见 GATE-LOG §注） |
| freeze venv 对照 | ABORT rc=2（ko 豁免生效，要求 Pillow 10.x）——符合任务书预期，不是失败 |
| occlusion audit | **0 flags**（NEW vs core 0；selftest 六类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 全触发，干净对照静默） |
| p8.py extract | 150/150 noted |
| p8.py compare vs core | **CLEAN**，missing=[]，extra=0，keydiff=**[138]**（#137 键 `11月22日是泡菜日。` 简繁同形故不 diff，#138 `三星時隔12年奪冠。` diff；与 builder 一致） |
| check_core（工作区副本） | rc=0：gloss fails 0，P7 phrases 8/8 verbatim，orphan issues 0；日期验算 11-16 Mon / 11-18 Wed / 11-19 Thu / 11-22 Sun / 11-28 Sat，与 D-3/D-1/D-day/泡菜日一致 |
| check_gloss | rc=0，gloss fails 0 |
| textmd 重导出（系统 python3） | 450 项，**与交付 text.md 逐字节相同**，SHA `af183ae6…` 一致 |
| 印/网文字层 | plain 提取各 49,645 字节，**逐字节相同**（-layout 提取各 92,239 字节，亦逐字节相同） |
| P8 最小字号 | **9.975pt**（region spans 163，at-min 158），≥9.75pt PASS；scratch 重渲染 PDF 同值 |
| creambox 真墨复核 | 49 盒：inside-only clearance 全 >0，最紧 +4.5；**真墨（PIL）clearance 最小 +2.5**（3 盒：P3/P5/P6 各一末行 `…韓語寄來。`），0 负值；P7 toolbox 3 盒 min inside +12.2 / min desc-clear +6.2；plain 扫描的负 clearance 全为框下 +24~+44 的次标题误报（已逐一归属） |
| boxtitle | **8/8 ≤386.5px**，最紧 P3 `김치의 날에 알아 둘 것　泡菜日須知` 349.3px |
| 孤标点 sweep | 真孤标点 **0**（SVG 8 页 + text.md；`·` 引导 11 处与 `—` 引导 13 处均为设计分隔符，已逐项归属，非孤标点） |
| 弯引号/U+2019 扫查 | U+201C/U+201D/U+2019/U+2018 = **0/0/0/0**（8 SVG + text.md）。直引号 `'` 54 处与 core-ko 逐页计数完全相同（6/4/4/0/2/8/30/0），为核心继承的韩文引号用法，非本版引入；P7 Frame 行用 「」：`句式拆解：「在〜之後」。提問：「〜 후에 뭐 해요?」`（content7.py:81） |
| keycheck（自写，REG vs p8 extract） | 149 exact + #150 `✓` trunc-ok = **150/150** |
| census | ex/match 166 项 0 missing，D6 missing 0 |
| §1.1 grep audit | paper(#fbfaf6)/VOL.4/VOL.5/`·` 逐页与 core 一致，仅 P7 VOL.5 3→2（by design，删 lko/lcn2 两行所致）；hanzi <text> 计数 94/199/148/114/151/91/250/1162，CJK 417/426 allowed、stray none；U+2019 0；未知颜色与 core 相同（仅 P1 一组图片色） |
| D5 字体（只记录数量，不判 (b)） | 印 PDF 全 8 页：Latin 脚本 span 落在 NotoSansCJK 者 **226** 个，NotoSansCJK span 总计 732 个 |
| 渲染可复现性 | scratch 重渲染印 PDF **SHA 与交付完全相同** `180d3ce0…`；scratch web PDF 同字节数 4,348,626、同文字层 49,645 字节逐字节相同，SHA 不同（`9a84569a…` vs `cfe20ece…`）——符合网 PDF 铁律（fontTools 子集改写 + cairo CreationDate），内容作数 |

## 4. 150 题逐题三源手验（自写 `verify-150-proof1.py`）

- 三源：(1) EDITION-RECORD 的 150 行 REG 表（键+注）；(2) P8 SVG 答案行直接解析（150 行）；
  (3) 交付印 PDF plain 文字层（空白归一化后检索）。
- **不符 0**：149 题键/注三源全等；#150 为 trunc-ok（SVG 键列 `✓ 本版H區範文（169字）`，与 core 同式；
  开放题 wording `（開放題，範文如下）` 与 H 注均在 PDF 文字层中）。
- 源码锚定：抽样 27 键（每 10 题 + #137–150 全数）在 `content*.py` 中全部找到出处，
  含 #137 `11月22日是泡菜日。`→content7.py、#138 `三星時隔12年奪冠。`→content7.py、
  #139 `11월 18일은 예비소집이에요.`→content8.py、#140→content7.py；#150 锚至 H 注。
- p8 extract keys 与 REG 逐键比对亦为 149 exact + #150 `✓`（见 keycheck）。

## 5. 8 页逐页渲染目视（交付印 PDF，100dpi，`pages/p-*.png`）

| 页 | 目视 |
|---|---|
| P1 头版 | 干净。 masthead、头条、数字盒、日历盒、照片、测验条、页脚 `Lucerna 韓語週報 VOL.4 正文韓語 講解繁體中文`、`第 1 版 / 共 8 版` 均完整，无溢出截断 |
| P2 生活 | 干净。特征盒、D-3/D-1/D-데이/泡菜日卡片、练习 A–D 收在页脚上方 |
| P3 文化 | 干净。注：中栏顶 `않았어요。` 为跨栏续句（`확인되지 않았어요` 断在栏间），freeze diff 证明该句两版共有、非本版引入；核心同式，不作缺陷 |
| P4 体育 | 干净。季后赛晋级图、照片、练习 A–D 完整 |
| P5 青年 | 干净。照片、数字盒、练习 A–D 完整 |
| P6 深读 | 干净。对照表、练习 A–D 完整 |
| P7 语言 | 干净。Pattern 框 「」引号正确；金句 8 条含新句 `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요`（1面）；读者来信框、下期预告 VOL.5 完整 |
| P8 测验与答案 | 干净。试题 A–H、答案键 1–150 全在页内；#137 `11月22日是泡菜日。 — 對照第2版`、#138 `三星時隔12年奪冠。 — 對照第4版`、#150 `✓ 本版H區範文（169字）` 目视确认；H 范文 + 照片完整 |

## 6. 旧版逐页对比

- W46 `2026-w46-ko-zh-tw/` 仓内**无 PDF、无 svg/**（仅源码 + text.md + ABSTRACT + KIT，见 `git ls-files`），
  故无旧版 PDF 可逐页对比。W46 text.md 为上周 VOL.3（699 行），与本周 VOL.4（919 行）属不同刊期，
  仅作刊期确认，不具逐页可比性。**本版为 ko-zh-tw 的 W47 新版，无同版旧 PDF。**

## 7. “next Sunday”冻结规则

- 在 core-ko 全目录、ko-zh-tw 全目录（含 SVG 与 text.md）、`tools/tables.py` 中
  grep `next Sunday`（不区分大小写）**0 命中**，`下個星期日/下个星期日/下週日/下周日` 亦 0 命中。
  **无适用对象，不适用本版**，未硬套旧行号。

## 8. 归属核对（缺陷归属：核心继承 / 本版引入 / fan-out 机制）

- 本轮**零缺陷**，无需修复路由。观察到的非缺陷项均已归属：
  - 直引号 `'` 54 处：核心继承（core-ko 逐页计数相同）；
  - P3 `않았어요。` 跨栏续句：核心继承（两版共有，freeze diff 无此串）；
  - P7 VOL.5 3→2：by design（删 lko/lcn2 两行）；
  - keydiff [138]：by design（#137 简繁同形）；#150 `✓`：核心同式；
  - text.md 450 vs core 452：by design（仅删 lcn2 + lko；`全部` 保留在 text.md 中）；
  - 网 PDF SHA 与重渲染不同：铁律预期（时间戳/子集改写），文字层逐字节相同；
  - freeze baseline 首跑 0/8：调用者参照取错（误指 core-ko/svg），纠正后 8/8，不属版本问题。

## 9. 缺陷清单

**零缺陷。** 无 (b) 项，无修复路由。

---
*注：复校全程未改动生产目录；三件交付 SHA 在复校前后复测一致，core-ko 三件 SHA 复测一致。
scratch 重渲染的印/网 PDF 已删（仅存日志与文字层提取；交付字节唯一来源仍为 builder 的 freeze build-copy）。
D5 字体仅记录数量 226，未作 (b) 判断（按任务书）。*
