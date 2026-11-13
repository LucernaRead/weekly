# Gate log — W47 zh-tw × ko, proof2（机械门，全跑，输出留档；针对 fix1 重建版）

- 版：`production/2026-w47/2026-w47-zh-tw-ko/`（繁体中文 × 韩语读者语）
- 交付物 SHA（开工前核对，全部机械门跑完后复核未变）：
  - 印刷 `Lucerna-VOL4-KO.pdf` 16,838,020 B / `c04102a9a1ceef1cf25fc7f3df6e69266e5f3d8bb2fec8d4370a3f782217d3a6`
  - 网页 `Lucerna-VOL4-KO-web.pdf` 2,325,041 B / `ed9e11a5c8997eb6b09cd6fd1f9bad6b64d686e2280d4730eac3d48ff65bad61`
  - `2026-w47-zh-tw-ko.text.md` 53,916 B / `2af17f023ab203259aeeb294b04f31e4bbb766398a28ec5f7fd2f163622b06f7`
- 探针：开工前 `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0；目录 `scratch-proof2-zh-tw-ko2/` 真实写盘通过。`TMPDIR=<scratch>/tmp`，系统 /tmp 未用。解释器全程 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
- 工具来源：`gates.py`／`gtools/`／`keycheck.py` 自 `scratch-fix-zh-tw-ko1/` 复制，仅把其中硬编码的 scratch 路径改为本目录（`sed` 替换 `scratch-fix-zh-tw-ko1` → `scratch-proof2-zh-tw-ko2`，见 `gates.py:11`、`keycheck.py:11`）；`tools/creambox.py` 为 `hidden_files/w47/tools/` 共享 canonical 工具。未改任何工具逻辑。

## 1. Freeze — baseline 8/8，diff 8 页全覆盖 ✅

- baseline：`tools/venv/bin/python tools/freeze.py baseline --build . --core-svg svg --out gates/ko-proof2/freeze-base`（cwd=版目录，由 gates.py 调用；freeze 复制版目录到 scratch、重定向输出路径后重建，不写生产）
  → `baseline: 8/8 SVGs byte-identical`（`gates/ko-proof2/freeze.log`）：p1-front 2f021d71…、p2-life 050e53b0…、p3-culture 6b01d169…、p4-sport 80d4d8db…、p5-youth 96565ffd…、p6-deep 6301c38d…、p7-lang 31f7898a…、p8-test a390fcc6…；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。P1–P6 与 proof1 旧版逐字相同；P7/P8 与 fix1 FIX-LOG 记载的新值逐字相同。
- diff：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-zh-tw/svg --edition-svg …/svg --json gates/freeze-diff.json`（rc=0，`gates/freeze-diff.log`）
  - 逐页增／删：p1 +24/−25、p2 +35/−39、p3 +42/−47、p4 +36/−39、p5 +46/−47、p6 +31/−33、p7 +360/−120、p8 +188/−187
  - 新增 CJK 共 4,690 字（proof1 旧版 4,692，−2 恰为 K1-5「入圍이에요」→「入圍예요」×2 各少一字）；新增皆为韩文音节 + 家具标题／被注词汇／继承串；删除含汉字的串全部为双语家具（中文标题 + 英文注 → 中文 + 韩文）或含引词的英文答案注，无简体字、无意外新增中文。逐页 CJK 净增量已逐项核对（见 PROOF-NOTE §8）：P7 净增 入／集／圍／間／夜／市各 1 皆为韩语释义引用的中文词；各页「國」+1（P1 +2）为家具「韓國語講解」徽章，属任务书已指明的汉字假阳性。

## 2. run.py（副本重建）✅ —— 见 §10 过程事件

- `rebuild-run.log`：rc=0，`FLOW OVERFLOW` 命中 **0**，HEAD TOO WIDE 0；P7 col3 ends 1821.42、teaser ends 2575.42（与 fix1 构建值逐值相同）；150 题：A2 44 / B1 74 / B2 32；REGISTRY by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}；MODEL chars: 142。
- ⚠️ 该次运行因 content*.py 的 OUT 为指向生产目录的绝对路径，重写了生产 8 个 SVG；事后立即以 SHA-256 核实**逐字节未变**（8 个 SVG SHA 与开工记录完全一致，三交付物 SHA 与字节数未变），仅 mtime 刷新。副本目录已删，只留日志。教训：重建验证只走 freeze.py，见 PROOF-NOTE §10。

## 3. checks.py（本版自带）✅

- `tools/venv/bin/python production/2026-w47/2026-w47-zh-tw-ko/checks.py` → `CHECKS PASS`（`gates/ko-proof2/checks.log`）
- 8 条金句各恰出现 2 次、`SIMP_ONLY_HITS []`、P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]。

## 4. Occlusion 审计 — 0 flags ✅

- 命令：`tools/venv/bin/python tools/occlusion_audit.py --selftest` + `... --json gates/ko-proof2/occlusion.json …/svg`
- 输出（`gates/ko-proof2/occlusion.log`）：selftest rc=0，`production/2026-w47/2026-w47-zh-tw-ko/svg: 0 flags`。

## 5. P8 extract + compare — 150/150，CLEAN ✅

- extract：`tools/venv/bin/python tools/p8.py extract --p8 …/svg/p8-test.svg --total 150 --json gates/ko-proof2/p8-extract.json`
  → `noted set = 150 of 150`（`gates/ko-proof2/p8-extract.log`）
- compare：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-zh-tw/svg/p8-test.svg --edition-p8 …/svg/p8-test.svg --total 150 --json gates/ko-proof2/p8-compare.json`
  → `status: CLEAN  missing=[] extra=[] uncertain=[] keydiff=[]`（core 150 noted / edition 150 noted；`gates/ko-proof2/p8-compare.log`；注：gates.json 中 "extra": "?" 是 gates.py 取键名 `extra_count` 未取到所致，compare JSON 原文本身含 `"extra": []`，实为 0）。
- core extract 另存 `gates/p8-core-extract.json`（供 keycheck.py 三源交叉用）。

## 6. keycheck-150（三源交叉 + 全版扫查）✅

- 脚本：`keycheck.py`（本目录，沿用 proof1/fix1 版，仅改输出目录）；`gates/keycheck.log`、`keycheck-150.json`
- 结果：
  - B 解析 150 项，1–150 连续无缺；**三源一致 150/150，mismatches []**（Q150 归一化为「✓」）
  - SVG CJK 版独有 {韓}、核心独有 {英}；text.md 同然
  - 弯引号：版 SVG U+0022 0、U+0027 1（`Kanahei's Little Animals` 专名）、U+201C/U+201D/U+2018/U+2019 皆 0；text.md 同然
  - 英文星期／月份名、"next Sunday"／"Next Sunday"、"finish line"／"end point"、「下週日」、「下周日」、「다음 주 일요일」、BABYMONSTER、결승선、장소：版 SVG 与 text.md **皆 0**；「이번 주 일요일」版 SVG 2（字串计；第 3 处跨 SVG 节点「이번」＋「주 일요일」，已核实）、text.md 2（同理，第 3 处跨行折断）
  - P8 六节标头全为繁体中文 + 韩语对译；P8 标头「第8版　本週大測驗　全部答案　이번 주 큰 테스트와 모든 정답」
  - 写作范文：去空白计 **142 字**，CJK+数字计 126，在 120–180 区间内，与文内「142자」标注相符
- 填空键：`gtools/check_fillin_keys.py` → **54/54 在正文，缺失 []**（`gates/ko-proof2/fillin-check.log`）。

## 7. Creambox（canonical 全版扫描）+ boxtitle + creambox-pil ✅

- canonical：`python3 hidden_files/w47/tools/creambox.py production/2026-w47/2026-w47-zh-tw-ko/svg/*.svg`（`gates/ko-proof2/creambox.log`）
  - 36 盒（P1 5、P2 6、P3 7、P4 4、P5 8、P6 3、P7 工具盒 3）
  - 负清除 **0**；各页 inside-only 最小清除：P1 18.8、P2 41.8、P3 16.1、P4 35.8、P5 6.4、P6 19.9；P7 工具盒 inside +40.5／+12.5／+14.0，P7 汇总：3 盒、最小 inside +12.5
  - P5 最小盒（迪士尼小档）：inside-only +6.4、desc-clear −0.4——末行仅一字「日」，无下行笔画，系 0.30 系数公式伪影；PIL 真墨实测底清除 +4.4px（见 §8），目视在盒内
- boxtitle（gtools，真墨）：36 盒，**超框 0**，最小右余 18.5px（P1）、最小左余 18.0px（`gates/ko-proof2/boxtitle.log`、`boxtitle.json`）
- creambox-pil（gtools，真墨）：36 盒，**STRADDLE 0、CREAM-COVER 0**；各页最小底清除：P1 16.5、P2 39.8、P3 14.1、P4 33.8、P5 4.4、P6 17.1、P7 10.5（`gates/ko-proof2/creambox-pil.log`、`creambox.json`）

## 8. P6 abutting（真墨）+ P5 紧盒验证 ✅

- P6 18:30「頒獎典禮」墨右缘 990.8 → 19:00「夜間遊行」墨左缘 991.4，墨缝 **0.6px**，与核心先例完全一致（`gates.json` abutting 节）
- P5 紧盒 PIL 真墨：迪士尼小档盒末行「日」墨底至盒底 **4.4px**（creambox-pil 各页最小底清除 P5 4.4px）

## 9. 印／网文字层比对 + PDF 指标 ✅

- `pdftotext -layout` 印／网：各 95,029 字节（`gates/ko-proof2/print.txt`、`web.txt`）
- 字符多重集差：印刷独有 0、网页独有 0（逐字相同）；「本週日」各 11、「下週日」0、BABYMONSTER 0、「取捨」2、「end point」0、「小雪」36
- PyMuPDF（`gates.json` pdf 节）：印、网皆 8 页、1462.5 × 2025 pt；最小字号 9.75pt（整刊与 P8 皆然）、最大 147.0pt（P1）、P8 最大 34.5pt
- 网页 PDF 2,325,041 B（< 7 MB）；BABYMONSTER 印网文字层皆 0
- 英文泄漏扫描（`gates.json` leak_scan）：deny_hits {}；shared_ascii_long 仅「A. 12:00 · B. 14:00 · C. 19:00」时刻串，与核心共有

## 10. K1 回归 + K2 助词穷举（本轮新发现，见 PROOF-NOTE §6/§7）

- K1 旧形 5 串（入圍은／鋼雕은／入圍을／市集는／入圍이에요）：8 个 SVG + text.md 出现皆 **0**；新形（入圍는／鋼雕는／入圍를／市集은 各 SVG 1 处 + text.md 1 处；入圍예요 SVG 2 处 + text.md 2 处）各就其位；源行 content7.py:43/:44/:52/:60、content8.py:58 已逐行核对；`입니다`／`습니다` 全版 0。
- 助词穷举（CJK 引词 + 助词，26 例，与 proof1 同数）：错误仅 K2 一例（小雪는）；其余 25 例全部正确。纯韩语词空格消去后全版扫描：元音＋을 0、辅音＋를 0、元音＋은 0、元音＋이에요 0、辅音＋예요 0（元音＋이 命中皆为词内音节伪影，已逐一核对上下文排除）。
- K2 证据链：content7.py:60、tables.py:2215、SVG p7-lang 节点 x=989.0 y=458.42、text.md:4699、交付印 PDF 100 dpi 渲染放大 `render/zoom-k2-p7-b2.png`（「小雪는 스물네 절기 중 스무 번째」在版）；本版自标读音 소설（B2 段首「小雪(소설)」、P2「Xiaoxue(소설)」、P8 Q25「小雪 — 소설」）+ 同句三词对照（節氣는／燈秀는／市集은 皆按汉字音正确）。
- U+FFFD：8 个 SVG + text.md 按字节计 **0**。

## 11. 其余核查

- VOL：VOL.4 ×10、VOL.3 ×2（延期披露所指上期）、VOL.5 ×1（下期预告），均正确
- ABSTRACT.txt：韩语单行摘要，0 个 BABYMONSTER，含刊名／目标语／A2–B2／150 题与真实主题
- 页脚「제N면／전체 8면」8 页齐全
- 8 张渲染卡片（`render/p--1.png` … `p--8.png`，100 dpi 自印 PDF 渲染）逐版目视：无溢出、无重叠、无裁切、无页脚碰撞；另有放大证据 `render/zoom-k2-p7-b2.png`（K2）、`render/zoom-k1-p7-ruwei.png`（K1-1）、`render/zoom-k1-p7-b1b.png`（K1-2）、`render/zoom-k1-p7-memory2.png`（K1-3）、`render/zoom-k1-p8-q105b.png`（K1-5a）、`render/zoom-k1-p8-q132b.png`（K1-5b）
- 星期核对（`date -d`，Asia/Taipei）：11/6 五、11/13 五、11/16 一、11/17 二、11/19 四、11/21 六、11/22 日、11/24 二、12/27 日、2027/1/3 日、10/23 五，皆与版面标注相符
- 机械门跑完后复核：三交付物 SHA 与开工前一致，未改动任何源文件内容（§2 所述确定性重建仅刷新 8 个 SVG 的 mtime，SHA 逐字节未变）；两目录 `git status` 仍仅为 `??` 未提交状态

## 结论

机械门全绿；proof1 的 8 项缺陷 + K1 的 5 处 6 落版点已全部验证修复；但内容复校发现新缺陷 1 类（K2，韩语助词误用，1 处、2 个落版点，机制层，源头 tables.py:2215），本版按 SOP §8 **不可定稿**，需改 tables.py:2215 一字（小雪는 → 小雪은）→ 只重扩 ko 版 + 重渲染 + 从头再复校一轮。
