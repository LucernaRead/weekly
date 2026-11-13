# GATE-LOG — 2026-W47 core-it 独立核心复校（D-2 fix 后从头全量）

- 复校员：独立核心复校（`scratch-reproof-core-it-d2`），与 fix 员不同人
- 对象：`~/workspace/weekly-git/production/2026-w47/core-it/`（只读；未写生产目录，未 commit，未 push）
- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 真实写文件通过
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0，见 freeze.log 首行）；`TMPDIR=<scratch>/tmp`，未写 /tmp
- 三 SHA（开工与完工两次实测一致）：印 `e1f89922a2b09e66d7d132eeab12b2638528e737685fa85d70f41bb8d2d1255d`（27,726,330 B）/ 网 `09f2ef6696ad67e92e57ba161c8ba2e6b35753634fa21b7ce68ea029283d71ef`（1,790,596 B）/ 文 `9eb9ee0662542e6ccf2814a2f2534fd64b62ad326de42e9cf83282092b5b6eed`（52,655 B，1317 行）

## 1. 独立重建（build.log、render.log、webpdf.log、export.log）

方法：生产构建源（`bslib4.py`、`svglib.py`、`content*.py`、`run.py`、`render.py`、`assets/`）整份拷到 `<scratch>/build/`；5 处 `OUT` 与 `render.py` 的 `BASE` 用 sed 改指 scratch（改后 grep 核对：无 `weekly-git/production` 残留路径）；生产 `run.py`/`render.py` 未直接跑。
- `run.py` rc=0：**0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE**；TOTAL 150；A2 47 / B1 70 / B2 33；页 10/18/18/18/18/18/12/38；范文 99 词；P7-a2 flow 末端 y=1124（底 1560），P7 col3 末端 1644.0。
- 重建 SVG 与发运版逐字节一致 **8/8**（`d301b886…` / `a744e5d2…` / `fe0a0e65…` / `12ddd86c…` / `08929554…` / `621054ee…` / `a7e6afa4…` / `779aa98c…`）。
- `render.py` rc=0：重建 cards 与发运版逐字节一致 **8/8**；重建印 PDF 27,726,330 B，SHA `e1f89922…`，与发运版逐字节一致。
- `tools/webpdf.py` rc=0：重建网 PDF 1,790,600 B（SHA `d5bc2d10abfa60a94e098fd74fc0eb26e059e1e5c69120b4e8b2ffd09686e6a3`），与发运版 1,790,596 B 差 4 字节——差异局限于 FontFile2 对象 20 的字体流压缩字节（`webpdf-diff.log`）；文字层 43,979 B 逐页一致；100 dpi 全页渲染逐像素一致（8 页 0 差异字节，`webpdf-pixels.log`）。见 PROOF-NOTE O1。
- text.md 自源码重导出（`export_it.py` 拷本，bdir 重指）：rc=0，150 题，52,655 B，SHA `9eb9ee06…`，与发运版**逐字节一致**。

## 2. freeze baseline（freeze.log）

`tools/freeze.py baseline --build production/2026-w47/core-it --core-svg production/2026-w47/core-it/svg --out <scratch>/freeze`：rc=0，**8/8 SVGs byte-identical**（P7 `a7e6afa4…` 精确复现）；shipped core SVGs 运行前后重哈希无变化。
build-copy 身份核实（任务项 3）：`freeze/build-copy/content7.py:17/:18` 含修复后新串；P7 含核心标志（`FRASI DELLA SETTIMANA` 等）；build-copy 确为 core-it 自身重建，非 edition 目录冒充。

## 3. occlusion audit（occlusion-selftest.log、occlusion.log、occlusion.json）

- selftest rc=0：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
- 生产 8 页：`0 flags`；`core: 0 flags; NEW vs core: 0`。

## 4. p8 extract + compare（三源 keycheck）

- `tools/p8.py extract --p8 …/svg/p8-valutazione.svg --total 150`：rc=0，**noted set = 150 of 150**（`p8-new.log` / `p8-new.json`）。
- `tools/p8.py compare`（修前 P8 SVG `scratch-fix-core-it1/freeze-baseline3/build-copy/svg/p8-valutazione.svg` vs 现版）：rc=0，**CLEAN，missing=[] extra_count=0 uncertain=[] keydiff=[]**（`p8-compare.log` / `p8-compare.json`）。
- 三源 keycheck（`keycheck.py` / `keycheck.log`）：登记表 150 / 印刷键 150 / 文本导出 Risposte 150；键 0 差异、注释 0 差异；Q101–104：101 `andremo`、102 `assaggeremo`、103 `guarderemo`、104 `B`，修前修后全等。
- P8 最小字号：SVG 最小 13.0 px = **9.75 pt**；印 PDF P8 实测最小 9.75 pt（534 个 span），恰达 SOP §1.1 下限。

## 5. D-2 回归实测（d2-rescan.log、d2-rescan2.log、d2-svg-pdf-p7.log、p7-wordorder.log、lettere-compare.log）

- 新串：L17 在 `content7.py:17`、p7 SVG（XML 文本节点归一化 1 处）、`text.md:775`；L18 在 `content7.py:18`、p7 SVG（1 处）、`text.md:777`、印/网 PDF 文字层（归一化各 1 处）。PDF 层 L17 因栏位交错断行，另以 PyMuPDF P7 词框核查：全部词在 A2 栏内按栏序出现。
- 旧串 `Le forme sono regolari: andare` / `irregolare al futuro: leggerò`：`content*.py` 0、8 SVG 0、`.text.md` 0、印/网 PDF 文字层 0。唯一残留 `WEEKLY-KIT.md:89`（§7 条目 18 Fix 历史行，任务指明的唯一合法残留）。
- `regolar`：`content*.py` 2 行、`text.md` 2 处、`svg/` 2 处（均为修复后的两行）。
- 文本导出 diff（基准：git HEAD 修前 `text.md`，SHA `d0c573b8…` 已验）：恰为 775/777 两行。
- 仅 P7 变化：SVG P1–P6/P8 与修前逐字节一致，P7 `3746030a…` → `a7e6afa4…`；cards P1–P6/P8 与修前（fix1 build-copy）逐字节一致，仅 p7 不同；P7 SVG 文本节点级 diff 仅 A2 未来时段落不同。
- STRADDLE 备份对照：修前 P7 备份 SHA `3746030a…` 已验；LETTERE 盒 3 个 cream rect 坐标修前修后相同，披露行节点（x=1461.5, y=1611.12/1639.52）相同——底沿偏紧非回归。

## 6. 文字层与文本导出校验（print-prod.txt、web-prod.txt、validate.log）

- `pdftotext` 印/网各 43,979 B、5,948 词（`wc -w`），`cmp` rc=0 字节一致；逐页比对 8/8 一致；P7 页文字层印/网一致。
- 旧 pdftotext（修前 `print-old.txt`，44,001 B）vs 新：归一化词级 diff 显示删除 `andare → andrò,` 与 `irregolare` → `regolare`，其余差异均为 P7 重排导致的栏位交错顺序变化。
- `validate_it.py`（拷本，bdir 重指）：rc=0，**forward-miss: 0 reverse-miss: 0**。

## 7. 横向漫出（h-scan.log、gutter-full.log、render-scan.log）

- PIL 全 8 页：越过页面边距 1862 的仅 2 条家具线，均为 **+0.0**（恰止于边距）；左越边距 **0**；P2 匹配块 b 余 31.1 px / d 余 40.3 px（D2 定稿值复现）。
- 200 dpi 渲染全 8 页：P1/P3/P4/P6/P7 无越边距墨迹；P2 +0.7 pt、P5 +0.7 pt、P8 +1.0 pt——与修前 fix3 实测值完全相同，非本次引入。
- “into-gutter 156 条”以跨栏同 y 合并伪影与全幅家具线为主，缺陷信号以“越过页边距”与 occlusion 审计为准（见 PROOF-NOTE O5）。

## 8. 其他扫描（misc-scans.log）

- 8 金句：归一化 `text.md` 中各恰 2 次。
- 禁词 Ucraina/Russia/Putin：0；`8 dicembre`：0；`20 novembre`：4 处均合法。
- 禁用色 14 个：`svg/` + `content*.py` + `bslib4.py` 0 处；`VOL.4 ·`：0 处。
- 范文 99 词（脚本实数）；头条 39 非空格字符 ≤ 56；星期以 `date` 核验 12 个日期全部正确。
- 外部事实抽查（公开来源）：意甲 MD11 10 场比分/24 球/积分榜、BookCity 全部数字与开幕信息、Torino Film Festival 44 届/日期/9 天——均吻合。
- ABSTRACT.txt：一行、287 B、无 ASCII 双引号；网 PDF 1,790,596 B < 7 MB。

## 结论

**（a）零缺陷，可定稿。** 观察项 O1–O5 见 PROOF-NOTE（均非缺陷，不拦定稿）。
