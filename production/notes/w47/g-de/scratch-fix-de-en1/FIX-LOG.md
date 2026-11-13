# FIX-LOG — 2026-W47 de-en fix1（D1/D2 弯引号 + D3 工具盒矮）

- 版：`production/2026-w47/2026-w47-de-en/`（德文目标语 × 英文读者语）
- 修复员：fix1 builder（与 proof2 复校员不同人；本轮只修、不复校）
- 时间：2026-11-11 09:0x–09:4x UTC（任务下发 04:21 EST；D3 追加）
- 目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-de-en1/`
  （FIX-LOG.md / GATE-LOG.md / PROBE.txt / measure-fix1*.log / build-fix1*.log /
  creambox.py / creambox_check.py / creambox*-after.log / freeze-direct.json /
  keycheck-150.json / p8extract.json / p8compare.json / render/ / tmp/）

## 0. 开工探针与复校对象核对（改前，与任务逐字节一致）

- 探针：每步写盘前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  → `9daeafb9…`，全部通过；`hidden_files/w47/scratch-fix-de-en1/` 真实写文件通过。
- 印刷 PDF `Die-Lucerna-VOL4-de-en.pdf` 10,966,409 B，
  SHA-256 `47aae035c9531818bce832e25b2aed6ed2557c18229c514bf32443fb6becd429` ✓
- 网页 PDF `Die-Lucerna-VOL4-de-en-web.pdf` 1,555,605 B，
  SHA-256 `37ba00d4fcf83f7dd78fe6427d5b0c1ae70c9035fbe8dd345dfde8de13d12875` ✓
- text.md `2026-w47-de-en.text.md` 49,665 B，
  SHA-256 `2eb0363202b8c9eacc8aaaf5008eedab614b8ddb0301082e92eb80cd25d6b7f5` ✓
- 改前全版计数（SVG + text.md）：U+201D 2 处（P8 两处），U+201C 35 / U+201E 33 /
  U+2019 0。P8 内：U+201C 3（D1 开引号、D2 开引号、德式闭引号 1）、U+201E 1。

## 1. D1 — content8.py:201，P8 H 写作框英文说明

- 改前：`Write in German, 80–100 words: “My week in November”. Say what you make, …`
- 改后：`Write in German, 80–100 words: „My week in November“. Say what you make, …`
- 改动：开引号 U+201C → U+201E，闭引号 U+201D → U+201C（德式 „ "，与 P5 同标题写法一致）。

## 2. D2 — P8 答案键 Q67 注（text.md:1173）

- 改前：`67. B (The 1903 calendar: “Im Lande des Christkinds”)`
- 改后：`67. B (The 1903 calendar: „Im Lande des Christkinds“)`
- **来源纠正（任务简报有误）**：该串的源不在 content8.py——content8.py 全文无
  "Christkind"（P8 键区只按 REG 打印 `f"{e['n']}. {e['key']}"`）。实际源是
  **content56.py:99**（P5 练习 Q67 的键注 `e.ex("B1", "multiple choice", "B",
  "The 1903 calendar: …"`，经 REG 印到 P8）。已修 content56.py:99。
  键值 `B` 未动；P5 同页 content56.py:100 选项 B 的 `„Im Lande des Christkinds“`
  本就是德式写法，改后与之完全一致。
- 其余 3 处 `„Im Lande des Christkinds“`（content56.py:19/30/66）本就是德式引号，未动；
  全版另 18 行合法德式 „ " 对已逐处 grep 核对上下文，只动 D1/D2 两串。

## 3. 机制层（与版内同步修，不留一处）

- `scratch-fanout-de/tr_en.py:279`（D1 值）与 `:141`（D2 值）同法改完；
  改后 tr_en.py U+201D 0 / 语法解析通过。
- 全盘扫描：含该两串的 transform 源只有这 4 处（版内 content8.py:201、
  content56.py:99；机制层 tr_en.py:141/279）。`vals_*.json`（其余 8 语）里
  两串只出现在 `values` 的**键**（英文源串作查表键），值是各语自己的译文
  （如 es 值用 «»），不含 U+201D——是他家机制数据，未动。`transform-en.log`、
  `en_keys.txt`、`en/print.txt`、`en/web.txt`、`en/freeze.json` 与
  `scratch-fanout-de-rebuild-A/` 内是重建 3 的历史记录，非现行源，未动。

## 4. D3 — P7 DER WERKZEUGKASTEN 奶油盒太矮（追加缺陷）

- 改前实测（已发货 SVG + creambox.py）：盒 rect y=330 h=453.5 → 盒底 783.5；
  末条 `Es ist fraglich, ob ... = Whether … is open` 基线 783.9，间隙 **−0.4**，
  `fraglich` 的 g 降部墨水至 ~788（约 4.7 单位落在盒外白纸上）。
- 根因（公式算错，非文案长）：content7.py 的盒高公式
  `tbh = 62 + Σ(lines*29.5 + 6) + 90` 漏算每个 `p.para` 调用的 +20.5 首基线偏移。
  实测复算：6 条共 9 行，模拟循环得末基线恰为 783.9（与 SVG 实测一致），
  公式值 453.5 只比末基线低 0.4。另：`p.para` 返回 `首基线 + 行数×20.5×1.42`，
  循环每条后再 +6——模拟公式与三者逐项一致。
- 修法（版内 content7.py，**未动共享 transform/box helper**）：不用魔法常数，
  改为按模拟墨水末端推导盒高——先模拟循环得末基线，再 `tbh = 末基线 − CTOP + 16`。
  16px 间隙落在其他奶油盒 +10.4…+47.7 的区间内（降部以下约留 11px）。
  改后：tbh 469.9，盒底 799.9，末基线间隙 **+16.0**；其下两盒自动下移同量：
  LESERBRIEFE 起 y=799.5 → 815.9（间隙仍 +10.4），NOCH EIN WORT y=1368 → 1384.4，
  止 1534.4，至 1548 Sätze 线余 13.6px。P7 其余内容（A2/B1/B2 流、图、Sätze、
  诊所、预告）一行未动。
- 目视：200 dpi 工具盒裁切（render/p7-toolbox-200dpi.png）6 条全在奶油盒内，
  末行下方有干净奶油余量；P7 全页 100 dpi（render/p7-100dpi.png）无重叠、无越线
  （`P7 col3 ends 1534.38`，见 build 日志）。

## 5. Helper 结论（报给协调员 / de-es fix1：盒高是否来自共享 helper）

- **不是共享 helper**：`tbh` 公式是 inline 写在每版各自的 content7.py 里的，
  transform.py 只替换字符串字面量，从不计算或改写 tbh。core-de 用 +110，
  10 个 de-* 版清一色 +90（注释写明"同 en/fr 的 pad 修复"，即把公式低估额
  靠 pad 硬补——补少了）。
- 因此不存在"改一处 helper 全家好"的修法。家庭级根治须改 core-de/content7.py
  的公式 + 10 个 de-* 版 content7.py 各自的公式（或在 transform 里加一补丁步），
  并全部 10 版重建重验。本轮只修 de-en 版内。
- 家庭只读扫描（creambox_check.py，仅 P7 工具盒，未改他版）：
  en/es/fr/it 盒底同为 783.5、末基线同为 783.9（几何逐字节同，−0.4）；
  ja/ko/zh-tw 盒底 754.0、末基线 754.8（−0.8，同类更差）；
  nl/pt/ru 盒底 813.0、末基线恰 813.0（基线间隙 +0.0，但降部约 4.7px 仍在盒外，
  同类边界情形）。de-es fix1 在并行研判 helper，本结论供其参考。

## 6. 重建事故：/tmp 写满致 webpdf 失败（已绕过，未删他人文件）

- 第一次重建（build-fix1.log）：run.py / render.py / verify / occlusion / p8 /
  freeze / chips / export 全过，但 `webpdf exit 0` 失败：
  `tools/webpdf.py:310 OSError: [Errno 28] No space left on device`。
  根因：webpdf 用 `tempfile.mkdtemp()` 写 /tmp，而 /tmp 是 512M tmpfs、
  当时 **100% 写满**（他 agent 的校对渲染残留：proof-es1 48M、freeze-pt-out 36M、
  各 proof 目录等；另有多个孤儿 /tmp/webpdf-*）。
  连带：print/web 文字层两门因网页 PDF 仍是旧版（08:15）而 FAIL——
  不是内容不一致，是网页 PDF 没生成。
- 处理：**未删 /tmp 任何他人文件**。重建改走 `TMPDIR=<scratch>/tmp`
 （build_edition.py 经环境变量透传给 webpdf），第二次重建
  （build-fix1b.log）**ALL GATES PASS**。/tmp 写满问题报给协调员处置。
- 另：本次网页 PDF 1,597,882 B（比 rebuild 3 的 1,555,605 B 大 42,277 B）——
  工作树 webpdf.py 现行版嵌 Newsreader-Bold/Italic 子集（rebuild-A 报告过的
  工具版本分裂，fc_match 改版所致），与内容无关；< 7 MB，文字层与印版一致。

## 7. 改后新交付物（重建 4，fix1）

- 印刷 PDF `Die-Lucerna-VOL4-de-en.pdf` — **10,966,406 B**，
  SHA-256 `4da8a84132d8e56e7bfe237f9515ae405b8c5b634f86e06f4ec993b8c4da345e`
- 网页 PDF `Die-Lucerna-VOL4-de-en-web.pdf` — **1,597,882 B**（< 7 MB），
  SHA-256 `2cdbe367df8fd2b57117b52dec3d25662e77ae9d4ecc1da3781a8b6e357b1b8a`
- text.md `2026-w47-de-en.text.md` — **49,665 B**（字节数与改前同，引号皆 3 字节），
  SHA-256 `f3f0c08455b647c9b8f2844fbf16c33008e2717f30c584d7a3b835f98cb8a53e`
- 解释器锁定：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）
  全程；未跑 transform.py——共享 tr_en.py 仍含 rebuild-A 的盒标题旧值
  （见 §8），重 transform 会**回退**盒标题修复，故只从版内源码重建
  （build_edition.py：run → render → webpdf → verify → occlusion → p8 →
  freeze → pdftotext → chips → export）。

## 8. 改动未回退的既有修复 + 预存不一致（报给协调员）

- Q34 新题干：源码 / text.md / P3 SVG / 印版文字层 / 网页文字层各 1×，
  旧题干 5 处 0×；content12.py:58（`Deutschland hat nach vier Spielen ___ Punkte.`）未动。
- P3 box-title `WEIHNACHTSWÖRTER　Words`（359.9px，7/7）未动。
- **预存不一致（fix1 未引入、未修，报协调员定）**：
  freeze_direct 源层级 FAIL：新增字面量 `WEIHNACHTSWÖRTER　Words` 在共享
  tr_en.py 里无账（共享版仍是 `Christmas words`，rebuild-A 的修复只进了
  rebuild-A 的 tr_en.py 副本与版内 content34.py:58）。渲染级冻结 8/8 通过，
  各页 frozen 数/sha 与 rebuild 3 **逐字节一致**（见 GATE-LOG），成品不受影响；
  但若将来有人用共享 tr_en.py 重 transform，盒标题修复会回退（D1/D2 在 fix1
  后已不会回退）。同理，`boxtitle.py en` 读共享 tr 得 6/7（`Christmas words`
  483.5px 超预算）；以发货 SVG 实测为 7/7。
- 诚实测量（D1/D2 的闭引号）：Noto Sans CJK SC 实测 advance（em=40）：
  U+201C 40.0 = U+201D 40.0（皆全角宽），U+201E 19.0，ASCII `"` 19.0。
  即德式闭引号 " 与英文闭引号 ” 在本字体里**同宽**—— fix1 达成的是任务已裁定的
  目标（全版 U+201D=0、引号统一为德式 „ "、与 P5 先例完全一致），
  开引号由宽变窄（40.0→19.0），闭引号的宽字形是德式 „ " 约定在本字体里的固有
  表现，与 P5 标题同一写法无异。未擅自改 ASCII 直引号（任务明令不改）。
  末行目视（render/p8-hbox-200dpi.png）：`„My week in November “.`——
  开引号紧贴，闭引号与句号间留有与 P5 标题相同的宽字形空隙。

## 9. 红线遵守

- 只改 D1/D2/D3：版内 content8.py:201、content56.py:99、content7.py（tbh 推导），
  机制层 tr_en.py:141/279。未动其他家庭、tools/、core-de、issues/。
- 未 commit、未 push、未跑 insert.py / lint --write；未做任何 git 写操作。
- proof2 由协调员另派。另：WEEKLY-KIT.md §5/§6/§7 已同步更新为 fix1 数值（见 KIT）。
