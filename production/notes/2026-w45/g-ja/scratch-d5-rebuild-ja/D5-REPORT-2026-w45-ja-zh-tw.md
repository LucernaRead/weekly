# D5 报告 — 2026-w45-ja-zh-tw（W45 ja，D5 + §1.1 合并重建）

## 一、装机

- 旧样式生产源 → §1.1 组装（`style-port-ja` fanout，MANIFEST-W45.md 逐文件 SHA 校验；
  svglib 另经 D1 波校验：反向还原 canonical §2a hunk 后 SHA 与 MANIFEST 一致，11/11；
  网 PDF 经 FIX-REPORT-ja-D1.md 表校验，11/11；`.text.md.new` 与 MANIFEST 逐字节一致）。
- D5 安装：移植模板 `svglib-ja-d5.py` 原样装为版内 `svglib.py`，仅改 `_D5_READER` 一行 → `"cjk"`。
  CJK 读者：与 W47 ja-ko svglib 逐字节相同。
  `test_d5_routing.py` FAILURES: 0；fix2 保留；kinsoku（`NO_START`）齐全。
  zh-tw 另剥离 face= plumbing（`bslib4.py` + `content*.py` 共 106 处，只改 plumbing，不改任何文字；剥离后 `face` 残留 0，`py_compile` 全过）。
- core 落盘：模板原样拷为 `production/2026-w45/core-ja/svglib.py`（`_D5_READER = "latin"`，
  与 W47 core-ja svglib 逐字节相同，28,392 B）；安装器 `--patch-core` 对旧式 core 拒单已实测
  （`FATAL: old-style svglib (no _char_font)`，rc=1）。

## 二、基线（组装后新样式源）

- run.py：TOTAL 150，FLOW 0，HEAD 0。
- SVG 8/8 与 fanout 逐字节相同；textexp 与 fanout `.text.md.new` 逐字节相同（44568 B）。
- 印 PDF 26004909 B，SHA 与 fanout 印 PDF 一致（`df60c47b2143a345ef69a18ccfbbbc136d4312d57fc60407dcb1a838c88ef3a9`）；
  网 PDF 2841221 B，SHA `0ebace35f0440f53facd53382aa36c5fd4ab93605b72d5276311e909a6620af6`（与 fanout 网 PDF 字节不符为预期：
  `tools/webpdf.py` 2026-11-11 改版 commit `40963281`，D1 波用旧版；文字层一致为准）。
- 印/网文字层多重集差 0（印 16416 / 网 16416 字符）；
  网 PDF vs 已发网 PDF `pdf_text_diff_ja.py` IDENTICAL 8/8（词 trim `「ゆる」—` + it/nl/pt gloss trims 已应用）。
- 修前普查：d5_latin_in_cjk 206（>0 ✓），curly_in_cjk 0，
  curly_total 0。
- 导出器（step 0）：`style-port-ja/textexp_ja.py` 在 fanout 目录上试跑，11/11 BYTE-IDENTICAL，
  `verify_textexp_ja.py --edition` ADOPT（0 UNEXPECTED）。W45 ja 无已发 `.text.md`（issues/ 0/11），
  11 份 `.text.md` 均为新建（W43 ja 前例）。

## 三、缺陷与修法

- F1：P1 信用行（右栏奶油框内）——字号 18.5→18.0（只改该行，不改文案）（`content12.py:87`，18.5 → 18.0）；P8 boxtitle 1 DEFECT（P1 [BODY] over=+6.5px right；与 de 同行同几何，基线同报，pre-existing，非 D5 引入）→P8 1251 元素，boxtitle 0 DEFECT 行，页脚余量 76.0px。

## 四、门禁（16 门 + D18 + D37；门 17 N/A，本家无 gates.py）

**ALL-GREEN**

- 门 1 run：PASS
- 门 2 head_check：PASS
- 门 3 D5 census：PASS（D5 latin 0 / cyrillic 0 / curly-in-CJK 0；curly_total 0，其中 Newsreader 0；Noto Sans 元素 0）
- 门 4 render：PASS
- 门 5 webpdf：PASS
- 门 6 occlusion：PASS
- 门 7 p8 extract：PASS（noted 150/150）
- 门 8 p8 compare：PASS（CLEAN，keydiff [138]，预期 [138]）
- 门 9 freeze baseline：PASS
- 门 10 freeze diff：PASS（{"core_svg": "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w45-ja/baseline/2026-w45-ja-zh-tw/svg", "edition_svg": "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w45-ja/patched/2026-w45-ja-zh-tw/s）
- 门 11 spill：PASS（SPILL 0，OBSERVE None）
- 门 12 boxtitle：PASS（DEFECT 0，backup 已找到：True）
- 门 13 edge：PASS（TOUCH 0，NEAR 0）
- 门 14 creambox：PASS（DEFECT 0；P8 1251 元素，末行 y=2624.0（页脚栏，页脚线 2596 之下，设计如此），距页底余量 76.0px）
- 门 15a print=web：PASS（印 16416 字符 / 网 16416 字符，多重集差 0）
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

## 五、新交付物（实测，scratch `patched/2026-w45-ja-zh-tw/`）

- 印 PDF：24935962 B，sha256 `592719d357886f2c43dfe6cdbcbda151e86b93e31a726ca3349c782a17f41109`（49 个嵌入字体）。
- 网 PDF `2026-w45-ja-zh-tw.web.pdf`：2628268 B（< 7 MB），sha256 `a0d804d943c16a01a064f16bd1707d2dbb377e4b12c3680cd4c2bf0cacb80181`。
- `2026-w45-ja-zh-tw.text.md`（新建）：44565 B，sha256 `d2c3475ded04eef0f3cf551223168bc583a4dc125fafad330ac3d2a36180dd59`。
- P8：1251 个文本元素，末行 y=2624.0（页脚栏，页脚线 2596 之下，设计如此），
  距页底（2700）余量 76.0px。
- D18 刊头间距 327.2px；D37 副刊头行末尾 257.2pt，
  右栏奶油框左缘 1439.5pt。

## 六、KIT

- 生产 KIT（`production/2026-w45/2026-w45-ja-zh-tw/WEEKLY-KIT.md`）文末追加
  `## D5 rebuild (2026-11-14)` 一节（装机、基线、门禁、新交付物实测 SHA/字节；纯追加，
  不改上文旧 pin）。D19：节内全部 `content*.py:NNN` 引用已逐行核对 patched 文件。
- 生产源同步：本报告只写 KIT + 本文件；版内生产源（svglib/content/bslib/render）
  仍为 D5 前旧版，由 closer 按 `patched/` 同步（逐文件 `cmp` 核对）后再 commit。
  唯一已落盘的生产源是 `production/2026-w45/core-ja/svglib.py`（模板，见 §一）。

## 七、重校后修复 F1/F2（2026-11-15；本节追加，§一–§六为 builder 原文不动）

- 来源：独立重校 `FAMILY-W45-JA-REPROOF.md` §8，verdict NOT PASSED。F1（P8 答案区 31 条注释未译成中文，题号 11, 12, 13, 14, 15, 19, 21, 22, 23, 24, 27, 28, 61, 62, 63, 64, 76, 77, 78, 80, 83, 84, 85, 86, 87, 98, 99, 100, 111, 112, 119）与 F2（本版无）均为基线既有、D5 零回归（31 条在 patched 与基线中逐字相同；修前核实见 fix 报告 §0）。
- 修法：按 de/ko/ru 对照措辞将 31 条注释逐条译成繁体中文（27/28 的 ＝ 后释义亦译；80 补中文释义“＝遵守規則，讓我們……吧”）；不改答案字母、题号与事实。改动只发生在答案注释参数：`content12.py:245`（题 11–15）、`:263`（题 19）、`:269`（题 21–24）、`:285`（题 27、28 注释表行）；`content34.py:209`（题 61–64）；`content56.py:88`（题 76–78、80）、`:174`（题 83–87）、`:210`（题 98–100）；`content7.py:56`（题 111、112）；`content8.py:28`（题 119）。patched/ 与 production 同步改动，改后两边逐字一致（patched↔production 全文件 diff 与修前逐字节相同）。任务书“只改 content8.py”与源码实测不符（仅题 119 在 `content8.py`），以 REG 注册顺序模拟（150/150）核实的源码位置为准；逐条译文对照见 fix 报告 §1。
- 重渲：`run.py` → `render.py` → `webpdf.py` → `textexp_ja.py` 全链重跑（`tools/venv/bin/python`，首渲前 `fc-cache -f` 已暖）；run TOTAL 150、FLOW 0、HEAD 0；render/webpdf/textexp rc=0；印/网文字层多重集差 0。
- 门禁（fix 后重跑，`logs/2026-w45-ja-zh-tw/GATES-SUMMARY.txt`，复本见下）：
  - 除 15c 外与 builder 终表逐字段相同（门 1–14、15a、15b、16、17、D18、D37；门 5 仅网 PDF 字节变；门 9 仅因 ALL-GREEN=False 未删 freeze build-copy；门 10 freeze-diff 新增 CJK 字符 145 个恰为译文字符，latin 82→84；门 14 P8 元素/末行 y/余量不变）。
  - 门 15a print=web：PASS，差 0（印/网各 16357 字符，修前 16416）。
  - 门 15c native verify：FAIL → HOLD（UNEXPECTED 12 块 = 仅 F1 的 31 行；P1–P7 tokens identical；REWRAP 30 与修前相同）。差值成分恰为 F1 内容差本身，未为求绿改 text.md/SVG——内容修复的预期形态（fix verdict 天生带 15c 红；15b 仍为 D27 已知口径差 FAIL，不计）。
  - **ALL-GREEN=False，唯一原因即 15c HOLD**（修前 True）。其余门全 PASS。
- 新交付物（fix 后实测，scratch `patched/2026-w45-ja-zh-tw/`；以下 pin 取代 §五同名 pin）：
  - 印 PDF：24942060 B（修前 24935962 B），sha256 `c780d0af0f2baa727d5148ed189e40a52d5472a2dc23d220545cea50ee02bfdc`（修前 `592719d357886f2c43dfe6cdbcbda151e86b93e31a726ca3349c782a17f41109`）。
  - 网 PDF `2026-w45-ja-zh-tw.web.pdf`：2642116 B（修前 2628268 B），sha256 `95de660c4b8a071471272a2e71376fb277a19f0f311b58475b64d0b80237c99d`（修前 `a0d804d943c16a01a064f16bd1707d2dbb377e4b12c3680cd4c2bf0cacb80181`）。
  - `2026-w45-ja-zh-tw.text.md`：44378 B（修前 44565 B），sha256 `9a894ff2ef476498d1f4bd158f3c0ee3cf8b46db0c727c07ca015f7d197872e5`（修前 `d2c3475ded04eef0f3cf551223168bc583a4dc125fafad330ac3d2a36180dd59`）；与 builder text.md 的 diff 恰为 F1 的 31 行（62 个 diff 行，无其他改动、无换行移动）。
  - P8：1251 个文本元素，末行 y=2624.0，距页底余量 76.0px（与修前相同）。
- KIT：生产 KIT `production/2026-w45/2026-w45-ja-zh-tw/WEEKLY-KIT.md` 文末追加 `## D5 fix — 重校 F1/F2 (2026-11-15)` 一节（本节 pin 为最新值）；门禁总表复本 `production/notes/2026-w45/g-ja/scratch-d5-rebuild-ja/logs/2026-w45-ja-zh-tw/GATES-SUMMARY.txt` 已同步为 fix 后总表（D29 `cmp` 逐字节验）。fix 报告 `hidden_files/d5-redo/FAMILY-W45-JA-FIX.md`。
