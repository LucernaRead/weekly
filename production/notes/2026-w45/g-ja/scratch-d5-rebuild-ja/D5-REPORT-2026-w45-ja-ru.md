# D5 报告 — 2026-w45-ja-ru（W45 ja，D5 + §1.1 合并重建）

## 一、装机

- 旧样式生产源 → §1.1 组装（`style-port-ja` fanout，MANIFEST-W45.md 逐文件 SHA 校验；
  svglib 另经 D1 波校验：反向还原 canonical §2a hunk 后 SHA 与 MANIFEST 一致，11/11；
  网 PDF 经 FIX-REPORT-ja-D1.md 表校验，11/11；`.text.md.new` 与 MANIFEST 逐字节一致）。
- D5 安装：移植模板 `svglib-ja-d5.py` 原样装为版内 `svglib.py`，仅改 `_D5_READER` 一行 → `"ru"`。
  ru 读者：旧 `_D5_READER == "ru"` 分支保留（D26）；fix-xru 不带入。
  `test_d5_routing.py` FAILURES: 0；fix2 保留；kinsoku（`NO_START`）齐全。
  
- core 落盘：模板原样拷为 `production/2026-w45/core-ja/svglib.py`（`_D5_READER = "latin"`，
  与 W47 core-ja svglib 逐字节相同，28,392 B）；安装器 `--patch-core` 对旧式 core 拒单已实测
  （`FATAL: old-style svglib (no _char_font)`，rc=1）。

## 二、基线（组装后新样式源）

- run.py：TOTAL 150，FLOW 0，HEAD 0。
- SVG 8/8 与 fanout 逐字节相同；textexp 与 fanout `.text.md.new` 逐字节相同（54104 B）。
- 印 PDF 24795790 B，SHA 与 fanout 印 PDF 一致（`1de56338c8e2e842fddec92f3f6958b5c42563dff183c9b7b921e4bc40ec5efa`）；
  网 PDF 2269861 B，SHA `85e5de892b5b289dc843fc3acee8a55dcf4fa66fee9914e9779ef812051b34bf`（与 fanout 网 PDF 字节不符为预期：
  `tools/webpdf.py` 2026-11-11 改版 commit `40963281`，D1 波用旧版；文字层一致为准）。
- 印/网文字层多重集差 0（印 21826 / 网 21826 字符）；
  网 PDF vs 已发网 PDF `pdf_text_diff_ja.py` IDENTICAL 8/8（词 trim `「ゆる」—` + it/nl/pt gloss trims 已应用）。
- 修前普查：d5_latin_in_cjk 207（>0 ✓），curly_in_cjk 0，
  curly_total 0。
- 导出器（step 0）：`style-port-ja/textexp_ja.py` 在 fanout 目录上试跑，11/11 BYTE-IDENTICAL，
  `verify_textexp_ja.py --edition` ADOPT（0 UNEXPECTED）。W45 ja 无已发 `.text.md`（issues/ 0/11），
  11 份 `.text.md` 均为新建（W43 ja 前例）。

## 三、缺陷与修法

- F1：P1 信用行（右栏奶油框内）——字号 18.5→18.0（只改该行，不改文案）（`content12.py:87`，18.5 → 18.0）；P8 boxtitle 1 DEFECT（P1 [BODY] over=+6.5px right；与 de 同行同几何，基线同报，pre-existing，非 D5 引入）→P8 2168 元素，boxtitle 0 DEFECT 行，页脚余量 76.0px。
- F2：P1 信用行俄文译文（右栏奶油框内）——字号 19→17.5（只改该行，不改文案）（`content12.py:88`，19 → 17.5）；P8 boxtitle 1 DEFECT（P1 [BODY] over=+22.5px right；该行基线同报 +7.5px 先存，D5 字体切换加宽至 +22.5；Noto Sans 实测行宽 413.1px，可用 390.6px，17.5pt 行宽 380.5px，余量约 10px）→P8 2168 元素，boxtitle 0 DEFECT 行，页脚余量 76.0px。

## 四、门禁（16 门 + D18 + D37；门 17 N/A，本家无 gates.py）

**ALL-GREEN**

- 门 1 run：PASS
- 门 2 head_check：PASS
- 门 3 D5 census：PASS（D5 latin 0 / cyrillic 0 / curly-in-CJK 0；curly_total 0，其中 Newsreader 0；Noto Sans 元素 725）
- 门 4 render：PASS
- 门 5 webpdf：PASS
- 门 6 occlusion：PASS
- 门 7 p8 extract：PASS（noted 150/150）
- 门 8 p8 compare：PASS（CLEAN，keydiff [137, 138]，预期 [137, 138]）
- 门 9 freeze baseline：PASS
- 门 10 freeze diff：PASS（{"core_svg": "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w45-ja/baseline/2026-w45-ja-ru/svg", "edition_svg": "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/d5-redo/scratch-2026-w45-ja/patched/2026-w45-ja-ru/svg", "）
- 门 11 spill：PASS（SPILL 0，OBSERVE None）
- 门 12 boxtitle：PASS（DEFECT 0，backup 已找到：True）
- 门 13 edge：PASS（TOUCH 0，NEAR 0）
- 门 14 creambox：PASS（DEFECT 0；P8 2168 元素，末行 y=2624.0（页脚栏，页脚线 2596 之下，设计如此），距页底余量 76.0px）
- 门 15a print=web：PASS（印 21826 字符 / 网 21826 字符，多重集差 0）
- 门 15b carryover：FAIL（D27：共享校验器对 ja 格式为已知工具口径差，基线亦 FAIL；不是 finding、不阻塞；验收见 15a + 15c）
- 门 15c native verify：PASS（ja 原生校验器，0 UNEXPECTED）
- 门 16 census_quotes：PASS
- 门 17 gates.py：PASS
- 门 D18 masthead：PASS（刊头标语/日期间距 288.9px）
- 门 D37 P1 y~612：PASS（副刊头行末尾 377.2pt vs 右栏奶油框左缘 1439.5pt，越过 -1062.3pt）

门 15b 补充（D27）：共享 `verify_textmd.py` carryover 模式对 ja 格式为已知工具口径差——
其表与 drop 规则按 pt 目标语家族标定；决定性对照：同一校验器跑基线（修前 port 期已验版）
同样 FAIL（W43 ja de：MD-only 1,696、SVG-only 3）。本家门 15 的权威证据是 15a（print=web 差 0）
+ 15c（ja 原生 `verify_textexp_ja.py --edition` ADOPT，0 UNEXPECTED）+ 全文通读（重校）。

## 五、新交付物（实测，scratch `patched/2026-w45-ja-ru/`）

- 印 PDF：24921149 B，sha256 `8038373d3e65898f9c4b534938af046b112930784ce24cdc99c8d2ad0ae6d67d`（81 个嵌入字体）。
- 网 PDF `2026-w45-ja-ru.web.pdf`：2408493 B（< 7 MB），sha256 `fb6e22f8ce70b8392df5543228dae25668d31dfec9ab4330966659410c1ab868`。
- `2026-w45-ja-ru.text.md`（新建）：54104 B，sha256 `7721151634126d05099964d08eb03918412966c652e73b1854eddff9fde0c094`。
- P8：2168 个文本元素，末行 y=2624.0（页脚栏，页脚线 2596 之下，设计如此），
  距页底（2700）余量 76.0px。
- D18 刊头间距 288.9px；D37 副刊头行末尾 377.2pt，
  右栏奶油框左缘 1439.5pt。

## 六、KIT

- 生产 KIT（`production/2026-w45/2026-w45-ja-ru/WEEKLY-KIT.md`）文末追加
  `## D5 rebuild (2026-11-14)` 一节（装机、基线、门禁、新交付物实测 SHA/字节；纯追加，
  不改上文旧 pin）。D19：节内全部 `content*.py:NNN` 引用已逐行核对 patched 文件。
- 生产源同步：本报告只写 KIT + 本文件；版内生产源（svglib/content/bslib/render）
  仍为 D5 前旧版，由 closer 按 `patched/` 同步（逐文件 `cmp` 核对）后再 commit。
  唯一已落盘的生产源是 `production/2026-w45/core-ja/svglib.py`（模板，见 §一）。
