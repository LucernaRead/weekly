# GATE-LOG — W47 ko-pt proof1 独立复校门禁记录

复校员 proof1；2026-11-11 UTC。工作区
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-pt/`；
TMPDIR 指到该目录下。对象
`~/workspace/weekly-git/production/2026-w47/2026-w47-ko-pt/`。
解释器锁：freeze / run.py / check_core / check_gloss / textmd 用 **/usr/bin/python3**
（Pillow 10.2.0 / FreeType 2.13.2）；render / webpdf / occlusion / p8 / p8font 用
`tools/venv/bin/python`。本目录证据：`freeze-baseline*.log`、`freeze-diff.log/json`、
`occlusion.log/json`、`p8-extract.log`、`p8-compare.log/json`、`p8.json`、`print-plain.txt` /
`web-plain.txt` / `print-layout.txt` / `web-layout.txt` / `textlayer-cmp.txt`、`p8font.log`、
`boxtitle.log`、`census.log`、`style11.log`、`textmd*.log` / `textmd-cmp.txt` /
`reexport-text.md`、`check-core*.log`、`check-gloss.log`、`keycheck.log`、`sweeps.log`、
`gloss-miss-verify.txt`、`three-source.py`、`pages/p-1.png`…`p-8.png`、
`web-p5-5.png` / `web-p8-8.png`、`core-sha-before/after.txt`、`next-sunday.txt`。
未 commit、未 push；未动生产目录任何文件。

## 探针
- `ls /dev/null` 存在（crw-rw-rw-）；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc 0。
- 工作区写 `probe.txt` 成功。全程无 EDQUOT。

## 成品核实（实测，开工前与复核后各一次）
- print `Lucerna-VOL4-KO-PT.pdf`：45,680,335 B，SHA-256
  `358303d15e17c8a2589f3edcad416368720a1f091a560b475180ade171131c74`，8 页，1462.5×2025 pt。
- web `Lucerna-VOL4-KO-PT-web.pdf`：4,033,877 B（< 7 MB），SHA-256
  `9abb351ca17918574a0f143a4486a8aa9deaaf8ff6e99495ca793c68500ac6da`，8 页，1462.5×2025 pt。
- `2026-w47-ko-pt.text.md`：35,080 B，449 items，SHA-256
  `80cc61ef7bc993f8e3681a971009a72969a4a42b612a6bdca9e8a6216c868ca0`。
- 三枚 SHA 与任务简报一致。核心 core-ko 复核前后未变：印
  `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`，text.md
  `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a`。

## 门 1 — freeze baseline/diff（系统 python3）
- baseline：`freeze.py baseline --build <ED> --core-svg <ED>/svg --out <S>/freeze-out`，
  `runtime: /usr/bin/python3 | Pillow 10.2.0 | FreeType 2.13.2`，rc=0，
  **8/8 SVGs byte-identical**，core integrity 8 文件重哈希未变（`freeze-baseline.log`）。
- venv 对照（预期 ABORT）：`tools/venv/bin/python freeze.py baseline …` rc=2，
  `ABORT: ko family builds on system python3 (Pillow 10.x) … Got Pillow 13.0.0`——ko 豁免已装好，
  不是失败（`freeze-baseline-venv.log`）。
- diff：`freeze.py diff --core-svg <CORE>/svg --edition-svg <ED>/svg` rc=0；
  p1 +17/−17，p2 +37/−35，p3 +30/−28，p4 +23/−22，p5 +33/−31，p6 +18/−15，p7 +39/−38，
  p8 +171/−167；**TOTAL 新增 CJK 7，全为 U+3000（每页 1 个，页脚）**（`freeze-diff.log/json`）。

## 门 2 — run.py（freeze 内重建）
- freeze baseline 内含 run.py 重建：exit 0；`FLOW OVERFLOW` / `HEAD TOO WIDE` 0 条；
  TOTAL 150（A2 51 / B1 72 / B2 27；每页 10/18/18/18/18/18/12/38）。

## 门 3 — occlusion_audit.py（venv，只读交付 SVG）
- `occlusion_audit.py --json occlusion.json <ED>/svg` rc=0；
  `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；
  `<svgdir>: 0 flags`；JSON `flag_count: 0`。→ **0 flags**。

## 门 4 — p8.py（venv，只读）
- extract：`p8.py extract --p8 <ED>/svg/p8-siheom.svg --total 150 --json p8.json` rc=0；
  `noted set = 150 of 150`，1–150 连续。→ **150/150**。
- compare：`p8.py compare --core-p8 <CORE>/svg/p8-siheom.svg --edition-p8 <ED>/svg/p8-siheom.svg --total 150` rc=0；
  `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`（E 组重定向，W46 先例）。

## 门 5 — 文字层一致
- `pdftotext`（plain）：print 51,790 B、web 51,790 B，`cmp` rc 0 → **逐字节一致**。
- `pdftotext -layout`：print 102,245 B、web 102,244 B，`cmp` 差 1 字节：仅第 7 行刊头 "Lucerna"
  缩进差 1 列（69 vs 70 空格）。根因实测：网 PDF 刊头 x0=501.7422 vs 印 502.1719
  （左移 0.43 pt = 0.15 mm，fontTools 子集化 UnifrakturMaguntia 字宽漂移）；ko-en 网 PDF 有
  **完全相同的 0.43 pt 位移**（x0 亦为 501.7422，ko-en layout 一致只因未落分列阈值），
  de/it/fr/es layout 均一致。内容与肉眼位置不受影响，**不判缺陷**（见 PROOF-NOTE §5(ii)）。
- 双 PDF 均为 8 页、1462.5×2025 pt。

## 门 6 — P8 最小字号
- `p8font.py`（venv，PyMuPDF）：`region spans 167, min 9.975pt, at-min 162, PASS >=9.75`。

## 门 7 — boxtitle（系统 python3，`boxtitle-ko.py` 独立重测）
- 8/8 within 386.5px：P1 349.8（숫자로 보는 이번 주 Em números）、P2 236.7（한능검 접수 Inscrição）、
  P3 371.1（김장 장보기 목록 Lista de compras）、P3 317.4（김치의 날에 알아 둘 것 A saber）、
  **P5 368.6（이번 주 청년 숫자 Números jovens，余量 17.9px）**、P7 286.8（실수 병원 Clínica de erros）、
  P7 265.0（이번 주의 틀 A estrutura）、P7 343.5（독자의 편지 Cartas dos leitores）。
- **最小余量 15.4 px（P3 371.1px）**；P5 修复后单行 fit，P5 渲染目视确认。

## 门 8 — keycheck（系统 python3，我自己的 p8 extract）
- `keycheck-proof.py`（ko3 `keycheck-ko.py` 改 p8.json 路径指向本目录）：rc=0；
  `REG 150, SVG keys 150, exact 149, trunc-ok 1, BAD 0`；#150 trunc-ok（svg='✓'）；
  每页 10/18/18/18/18/18/12/38 全对。→ **150/150**。

## 门 9 — census / style11（系统 python3）
- census：`ex/match items total: 166`，`missing from text.md: 0`；`D6 missing: 0`。
- style11：paper/VOL.4/`·`/颜色与核心逐页一致（·=13/21/20/14/20/31/17/38）；
  hanzi 0（核心 82/187/138/104/137/81/212/1122）；U+2019 0；
  P7 VOL.5 3→2 按设计。`style11: OK`。

## 门 10 — textmd 重导出（系统 python3，scratch 副本）
- 首次误传带 `# ` 的 title 行（textmd 自加 `# `），首行多一个 `# `；修正为裸 title 后重跑：
  `textmd.py . 2026-w47-ko-pt reexport-text.md 'Lucerna Korean Weekly VOL.4 — Korean text, Portuguese explanations (2026-W47)'`
  rc=0，`wrote … items: 449`；与交付件 `cmp` → **逐字节一致**（`textmd-cmp.txt`）。

## 门 11 — check_core / check_gloss（系统 python3，scratch 副本）
- check_core：首次副本缺 `assets/` 致 svglib 读 `assets/lucerna-moth.svg` 失败 rc=1（我的副本问题，
  非版问题）；补 assets 后 rc=0：gloss fails 0，P7 短语 8/8 verbatim，orphan 0，日期 D-3/D-1/D-day/김치의 날全对。
- check_gloss：连贯跑法（ED 与 BUILD 均指向 ko-pt，`check-gloss-pt/`）rc=0，**gloss fails: 0**。
  混合跑法（BUILD=pt、ED=core-ko）报 10 miss；对照实验：在 core-ko 自身原样跑未改动
  `check_gloss.py` 同样报这 10 个 miss——9 个词头在核心 SVG 当页跨 `<text>` 元素断行，
  检查的字符串包含逻辑看不见跨元素词（`gloss-miss-verify.txt`）。核心继承的工具 artifact，
  非本版引入（见 PROOF-NOTE §5(i)）。

## 门 12 — 专项扫描（`sweeps.py` / `sweeps.log`）
- 弯引号/弯撇 U+201C/U+201D/U+2019/U+2018：8 SVG + content py + text.md + ABSTRACT + 双 PDF 文字层，**全 0**。
- 孤标点：单独标点 `<text>` **0 个**；行首闭合标点候选 **7 行**，与核心**逐行相同**
  （同坐标同文本，均为选项分隔符 `· B./· C.` 换行，按设计）。
- creambox 真墨复核：cream rect（#fbfaf6/#f7f1e2/#f1e8d4/#efe6cf/#f5edd8/#faf6ea）14 个，
  **全部内含文字**，空盒 0。
- D5 字体（只记录）：SVG font-family：Noto Sans CJK KR 618、Noto Serif CJK KR 877、
  UnifrakturMaguntia 1；拉丁字母段：Sans KR **406**、Serif KR **345**、UnifrakturMaguntia 1；
  **Noto Sans CJK SC 0**（`pdffonts` 双 PDF 亦无 SC 字体，仅 NotoSansCJKkr/SerifCJKkr/UnifrakturMaguntia）。

## 门 13 — 150 题三源手验（`three-source.py`，系统 python3）
- REG（content*.py：题干 body + 键 + 注）→ 页 SVG（题干去空白前 40 字 + 全文）+ text.md（题干）
  + P8 SVG（键 via p8 extract，注前 25 字）：**0 失败**。
- 中间态说明：初版 77 个 STEM-NOT-IN-PAGE-SVG 系 `___` 空白在 SVG 中渲染为 U+00A0 空格串，
  归一化未处理所致；题干 `___` 归一为空后重跑，0 失败（全题干连续、无断行拆分）。
  键 0 失败；P8 注 0 缺失。→ **150/150 三源全过**。

## 门 14 — carry-forward 核查
- `Tudo` quirk：`content12.py:101` 目录行 `("8면", "시험과 답", "Tudo")`；
  P1 SVG 1 次（渲染目视：目录 8면 行右端 "Tudo" 正常）、印文字层 1 次、text.md 0 次——
  `is_prose` 剔除裸拉丁词，与 en All / fr Tout / it Tutto 同类。无实质影响。
- P5 box-title：见门 7（368.6px，余量 17.9px；全版最小余量 15.4px）。
- "next Sunday"：`grep -rn "next Sunday"` 于 core-ko/*.py、ko-pt/*.py、`tools/tables.py` **0 命中**——无适用对象。
- 继承裁定出处：#43/#123/#124 "previsão da Weatheri"（`content34.py:107,121`、`content8.py:39`，核心自有）；
  #150 `✓`（核心同）；P8 #81 注换行在栏内，compare CLEAN。
- 旧版对比：ko-pt 为 fan-out #3 首版，无旧版，不适用。

## 门 15 — 目视
- 印 PDF 100 dpi `pages/p-1.png`…`p-8.png` 逐页全读：无溢出/重叠/压页脚/豆腐块；5 图 + 图注齐全；
  页脚 `Lucerna　SEMANÁRIO COREANO VOL.4　Texto em coreano　Explicações em português` +
  `Página N de 8` 8/8 正确；P1 "Tudo"、P5 "Números jovens"、P7 frame 「〜 후에」+「」葡语行、P8 150 答案
  均目视确认。
- 网 PDF 渲染对照：`web-p5-5.png`、`web-p8-8.png` 与印版逐项一致，无豆腐块，葡语变音符号（ç/ã/õ/é）正常。
- text.md 全文通读：零问题。

## 结论
- 机械门：**全部通过**（freeze 8/8、occlusion 0、p8 150/150 + CLEAN、文字层 plain 一致、P8 字号 9.975pt、
  boxtitle 8/8、keycheck 150/150、textmd 逐字节一致、check_core/check_gloss 0、扫查全 0、
  三源 150/150、目视 8/8）。
- 内容：P5 缺陷类已在 map 源头修掉并重测通过；`Tudo` 仅为分类器 quirk；无新缺陷。
- **结论：(a) 零缺陷，可定稿。**
