# D5 报告 — 2026-w45-ja-zh-cn（W45 ja，D5 + §1.1 合并重建）

## 一、装机

- 旧样式生产源 → §1.1 组装（`style-port-ja` fanout，MANIFEST-W45.md 逐文件 SHA 校验；
  svglib 另经 D1 波校验：反向还原 canonical §2a hunk 后 SHA 与 MANIFEST 一致，11/11；
  网 PDF 经 FIX-REPORT-ja-D1.md 表校验，11/11；`.text.md.new` 与 MANIFEST 逐字节一致）。
- D5 安装：移植模板 `svglib-ja-d5.py` 原样装为版内 `svglib.py`，仅改 `_D5_READER` 一行 → `"cjk"`。
  CJK 读者：与 W47 ja-ko svglib 逐字节相同。
  `test_d5_routing.py` FAILURES: 0；fix2 保留；kinsoku（`NO_START`）齐全。
  
- core 落盘：模板原样拷为 `production/2026-w45/core-ja/svglib.py`（`_D5_READER = "latin"`，
  与 W47 core-ja svglib 逐字节相同，28,392 B）；安装器 `--patch-core` 对旧式 core 拒单已实测
  （`FATAL: old-style svglib (no _char_font)`，rc=1）。

## 二、基线（组装后新样式源）

- run.py：TOTAL 150，FLOW 0，HEAD 0。
- SVG 8/8 与 fanout 逐字节相同；textexp 与 fanout `.text.md.new` 逐字节相同（44334 B）。
- 印 PDF 24944589 B，SHA `fc6364cdcdee5db341581fa72d34de4e3c970f7283e290f65867a3466147df41` 与 fanout 印 PDF 不一致，已裁定（ADJUDICATED）：fanout 印 PDF 是 60,458,528 B / 470 个独立字体名（1,667 条目）的子集膨胀件，基线印 PDF 24,944,589 B / 46 个独立字体名（49 条目），两者文字层字符多重集差 0（16,456 字符，不计空白；含空白 20,278 字符），8 页。
  网 PDF 2504774 B，SHA `ebda4f66b52f1c668869f79c9bc7c7f4bac812e8f2de6f13cb18d4f19f6cc48f`（与 fanout 网 PDF 字节不符为预期：
  `tools/webpdf.py` 2026-11-11 改版 commit `40963281`，D1 波用旧版；文字层一致为准）。
- 印/网文字层多重集差 0（印 16456 / 网 16456 字符）；
  网 PDF vs 已发网 PDF `pdf_text_diff_ja.py` IDENTICAL 8/8（词 trim `「ゆる」—` + it/nl/pt gloss trims 已应用）。
- 修前普查：d5_latin_in_cjk 206（>0 ✓），curly_in_cjk 0，
  curly_total 0。
- 导出器（step 0）：`style-port-ja/textexp_ja.py` 在 fanout 目录上试跑，11/11 BYTE-IDENTICAL，
  `verify_textexp_ja.py --edition` ADOPT（0 UNEXPECTED）。W45 ja 无已发 `.text.md`（issues/ 0/11），
  11 份 `.text.md` 均为新建（W43 ja 前例）。

## 三、缺陷与修法

- F1：P1 信用行（右栏奶油框内）——字号 18.5→18.0（只改该行，不改文案）（`content12.py:86`，18.5 → 18.0）；P8 boxtitle 1 DEFECT（P1 [BODY] over=+6.5px right；与 de 同行同几何，基线同报，pre-existing，非 D5 引入）→P8 1252 元素，boxtitle 0 DEFECT 行，页脚余量 76.0px。

## 四、门禁（16 门 + D18 + D37；门 17 N/A，本家无 gates.py）

**ALL-GREEN**

- 门 1 run：PASS
- 门 2 head_check：PASS
- 门 3 D5 census：PASS（D5 latin 0 / cyrillic 0 / curly-in-CJK 0；curly_total 0，其中 Newsreader 0；Noto Sans 元素 0）
- 门 4 render：PASS
- 门 5 webpdf：PASS
- 门 6 occlusion：PASS
- 门 7 p8 extract：PASS（noted 150/150）
- 门 8 p8 compare：PASS（CLEAN，keydiff []，预期 []）
- 门 9 freeze baseline：PASS
- 门 10 freeze diff：PASS（{"core_svg": "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w45-ja/baseline/2026-w45-ja-zh-cn/svg", "edition_svg": "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w45-ja/patched/2026-w45-ja-zh-cn/s）
- 门 11 spill：PASS（SPILL 0，OBSERVE None）
- 门 12 boxtitle：PASS（DEFECT 0，backup 已找到：True）
- 门 13 edge：PASS（TOUCH 0，NEAR 0）
- 门 14 creambox：PASS（DEFECT 0；P8 1252 元素，末行 y=2624.0（页脚栏，页脚线 2596 之下，设计如此），距页底余量 76.0px）
- 门 15a print=web：PASS（印 16456 字符 / 网 16456 字符，多重集差 0）
- 门 15b carryover：FAIL（D27：共享校验器对 ja 格式为已知工具口径差，基线亦 FAIL；不是 finding、不阻塞；验收见 15a + 15c）
- 门 15c native verify：PASS（ja 原生校验器，0 UNEXPECTED）
- 门 16 census_quotes：PASS
- 门 17 gates.py：PASS
- 门 D18 masthead：PASS（刊头标语/日期间距 327.2px）
- 门 D37 P1 y~612：PASS（副刊头行末尾 257.2pt vs 右栏奶油框左缘 1439.5pt，越过 -1182.3pt）

门 15b 补充（D27）：共享 `verify_textmd.py` carryover 模式对 ja 格式为已知工具口径差——
其表与 drop 规则按 pt 目标语家族标定；决定性对照：同一校验器跑基线（修前 port 期已验版）
同样 FAIL（W43 ja de：MD-only 1,696、SVG-only 3）。本家门 15 的权威证据是 15a（print=web 差 0）
+ 15c（ja 原生 `verify_textexp_ja.py --edition` ADOPT，0 UNEXPECTED）+ 全文通读（重校）。

## 五、新交付物（实测，scratch `patched/2026-w45-ja-zh-cn/`）

- 印 PDF：24914817 B，sha256 `9c9024090f6c4b30762361eca259444598261a74afb0335caac060221917986c`（49 个嵌入字体）。
- 网 PDF `2026-w45-ja-zh-cn.web.pdf`：2495330 B（< 7 MB），sha256 `ccd63963b19c43be4c7923f177d29ae695da9ed6aac131ade39f1f2d09d2492b`。
- `2026-w45-ja-zh-cn.text.md`（新建）：44334 B，sha256 `21ac3cc69fa0a408578575ea75f783b96e9990175cb94410f7cc9327342bf384`。
- P8：1252 个文本元素，末行 y=2624.0（页脚栏，页脚线 2596 之下，设计如此），
  距页底（2700）余量 76.0px。
- D18 刊头间距 327.2px；D37 副刊头行末尾 257.2pt，
  右栏奶油框左缘 1439.5pt。

## 六、KIT

- 生产 KIT（`production/2026-w45/core-ja/WEEKLY-KIT.md`）文末追加
  `## D5 rebuild (2026-11-14)` 一节（装机、基线、门禁、新交付物实测 SHA/字节；纯追加，
  不改上文旧 pin）。D19：节内全部 `content*.py:NNN` 引用已逐行核对 patched 文件。
- 生产源同步：本报告只写 KIT + 本文件；版内生产源（svglib/content/bslib/render）
  仍为 D5 前旧版，由 closer 按 `patched/` 同步（逐文件 `cmp` 核对）后再 commit。
  唯一已落盘的生产源是 `production/2026-w45/core-ja/svglib.py`（模板，见 §一）。

## 七、重校后修复 F1/F2（2026-11-15；本节追加，§一–§六为 builder 原文不动）

- 来源：独立重校 `FAMILY-W45-JA-REPROOF.md` §8，verdict NOT PASSED。F1（P8 答案区 31 条注释未译成中文，题号 11, 12, 13, 14, 15, 19, 21, 22, 23, 24, 27, 28, 61, 62, 63, 64, 76, 77, 78, 80, 83, 84, 85, 86, 87, 98, 99, 100, 111, 112, 119）与 F2（答案 45 繁体 並）均为基线既有、D5 零回归（31 条在 patched 与基线中逐字相同；修前核实见 fix 报告 §0）。
- 修法：按 de/ko/ru 对照措辞将 31 条注释逐条译成简体中文（27/28 的 ＝ 后释义亦译；80 补中文释义“＝遵守规则，让我们……吧”）；不改答案字母、题号与事实。改动只发生在答案注释参数：`content12.py:244`（题 11–15）、`:262`（题 19）、`:268`（题 21–24）、`:284`（题 27、28 注释表行）；`content34.py:209`（题 61–64）；`content56.py:88`（题 76–78、80）、`:174`（题 83–87）、`:210`（题 98–100）；`content7.py:56`（题 111、112）；`content8.py:28`（题 119）。F2：`content34.py:104`（题 45）`オーケストラ＝杉並 d` → `オーケストラ＝杉并 d`，仅改 並→并一字。patched/ 与 production（core-ja）同步改动，改后两边逐字一致（patched↔production 全文件 diff 与修前逐字节相同）。任务书“只改 content8.py”与源码实测不符（仅题 119 在 `content8.py`），以 REG 注册顺序模拟（150/150）核实的源码位置为准；逐条译文对照见 fix 报告 §1。
- 重渲：`run.py` → `render.py` → `webpdf.py` → `textexp_ja.py` 全链重跑（`tools/venv/bin/python`，首渲前 `fc-cache -f` 已暖）；run TOTAL 150、FLOW 0、HEAD 0；render/webpdf/textexp rc=0；印/网文字层多重集差 0。
- 门禁（fix 后重跑，`logs/2026-w45-ja-zh-cn/GATES-SUMMARY.txt`，复本见下）：
  - 除 15c 外与 builder 终表逐字段相同（门 1–14、15a、15b、16、17、D18、D37；门 5 仅网 PDF 字节变；门 9 仅因 ALL-GREEN=False 未删 freeze build-copy；门 10 freeze-diff 新增 CJK 字符 156 个恰为译文字符（含 F2 的 并 ×1），latin 90→92；门 14 P8 元素/末行 y/余量不变）。
  - 门 15a print=web：PASS，差 0（印/网各 16396 字符，修前 16456）。
  - 门 15c native verify：FAIL → HOLD（UNEXPECTED 13 块 = F1 的 31 行 + F2 的 1 行；P1–P7 tokens identical；REWRAP 12 与修前相同）。差值成分恰为 F1/F2 内容差本身，未为求绿改 text.md/SVG——内容修复的预期形态（fix verdict 天生带 15c 红；15b 仍为 D27 已知口径差 FAIL，不计）。
  - **ALL-GREEN=False，唯一原因即 15c HOLD**（修前 True）。其余门全 PASS。
- 新交付物（fix 后实测，scratch `patched/2026-w45-ja-zh-cn/`；以下 pin 取代 §五同名 pin）：
  - 印 PDF：24920717 B（修前 24914817 B），sha256 `cb2e82a2a335de7ccf4e6c381907ee74f25c81345c6aa76175ed4229d5ac999c`（修前 `9c9024090f6c4b30762361eca259444598261a74afb0335caac060221917986c`）。
  - 网 PDF `2026-w45-ja-zh-cn.web.pdf`：2507315 B（修前 2495330 B），sha256 `71a0fe0f0b5f048ada6ef558854a5c329258cd1ab164efb433833bd95952b2ba`（修前 `ccd63963b19c43be4c7923f177d29ae695da9ed6aac131ade39f1f2d09d2492b`）。
  - `2026-w45-ja-zh-cn.text.md`：44144 B（修前 44334 B），sha256 `e007d01deea5d08385a375a6ff5fdaab5609a1569cf87b312e364711d0880b30`（修前 `21ac3cc69fa0a408578575ea75f783b96e9990175cb94410f7cc9327342bf384`）；与 builder text.md 的 diff 恰为 F1 的 31 行 + F2 的 1 行（64 个 diff 行，无其他改动、无换行移动）。
  - P8：1252 个文本元素，末行 y=2624.0，距页底余量 76.0px（与修前相同）。
- KIT：生产 KIT `production/2026-w45/core-ja/WEEKLY-KIT.md` 文末追加 `## D5 fix — 重校 F1/F2 (2026-11-15)` 一节（本节 pin 为最新值）；门禁总表复本 `production/notes/2026-w45/g-ja/scratch-d5-rebuild-ja/logs/2026-w45-ja-zh-cn/GATES-SUMMARY.txt` 已同步为 fix 后总表（D29 `cmp` 逐字节验）。fix 报告 `hidden_files/d5-redo/FAMILY-W45-JA-FIX.md`。
