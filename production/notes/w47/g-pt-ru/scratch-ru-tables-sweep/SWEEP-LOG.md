# W47 ru 机制表弯引号扫尾 SWEEP-LOG

- 日期：2026-11-11（UTC 08:37 开工）
- 范围：仅 `hidden_files/w47/scratch-fanout-ru/` 内机制表与生成器（顶层 `*.json`、`*.py`）；未碰 `production/`、core-ru、其他家庭、`tools/`、`issues/`；未跑 insert.py / lint --write / 任何 apply/transform；无任何 git 写操作（不 commit、不 push、不 add）。
- 方法参考：ja 家庭扫尾记录 `hidden_files/w47/scratch-ja-tables-sweep/NOTE.md`（24 文件 71 处，纯文本字面替换、不重序列化 JSON）。
- 探针：开工前通过。`git hash-object -w` 返回 `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`；探针文件已真实写入 `hidden_files/w47/probe-ru-tables-sweep.txt`（内容 `ru-tables-sweep probe 2026-11-11T08:37:16Z`）。磁盘 `df`：45G 可用；全程无 EDQUOT。

## 0. 裁定依据（先核实再动手）

- 源头：ru-en proof1 D1。ru-en fix1（`scratch-fix-ru-en1/FIX-LOG.md` §1）实测裁定：P5 band 副标 `“Black Friday”` 在印版 PDF 里是 13.5pt、`NotoSansCJKsc-Regular` 字串；PIL 实测该字体 SC 面 18px 下 `“`/`”` 均为 18.00px = 恰好 1em，直引号 `"` 仅 8.53px；fix1 版内改为直引号，P7 `“чёрной пятнице”`（Newsreader）明确保留。
- 本次补测（同法，PIL 18px）：CJK 面 `’`（U+2019）同样 18.0px = 1em，ASCII `'` 仅 5.0px；Newsreader Regular 面 `’` 为 4.61px（正常窄字形）。结论：**凡落在 CJK 字体语境（band 副标等混合字串）的弯标点都是 1em 宽的缺陷；纯拉丁正文（Newsreader）的弯标点是正确排版**。
- en 版内现行排法佐证：已交付的 ru-en 版 band 副标用直撇号，如 `content12.py:157` 的 `Students' Day, Ded Moroz's birthday`；fix1 亦确认该版可见 SVG 文本里 U+2019 为 0。机制表里的 en 弯撇与已交付版的排法不一致，重 fan-out 会带回缺陷。
- 因此“误用”的界定：**英文读者语值里的英文式弯引号/弯撇**（`“ ”`、`’`）一律修为直引号/直撇号；各语自己的正确标点一律不动（见 §3 保留表）。

## 1. 改动的 4 个文件（共 17 值、19 字符）

替换方式：纯文本字面替换（不重序列化 JSON），其余字节不变；每处替换前均断言盘上旧形计数（脚本 `/tmp/ru-tables-sweep-apply.py`、`/tmp/ru-tables-sweep-apply2.py`）。改后逐文件用改前解析快照（`/tmp/ru-sweep-pre/`）做结构 diff：键集合完全一致，仅下列值变化，且每值仅差替换处。

说明：JSON 原文里值内的直引号须写作 `\"`，解析后的值即 `"Black Friday"`，与 fix1 版内字符串逐字一致（已断言）。

### map-en.json（6 值、7 字符）

| 行 | 键 | 改前 → 改后 |
|---|---|---|
| 109 | `УРОВЕНЬ B1　«Чёрная пятница»: скидки с 16 ноября　“黑色星期五”：11月16日开始打折`（键不动） | `…　“Black Friday”: sales from 16 November` → `…　"Black Friday": sales from 16 November` |
| 31 | `11 月 11 日经济学家日` | `11 November — Economists’ Day` → `11 November — Economists' Day` |
| 104 | `УРОВЕНЬ A2　День полиции, День экономиста и обычная неделя　警察节、经济学家日与平常的一周` | `…　Police Day, Economists’ Day and an ordinary week` → `…　Police Day, Economists' Day and an ordinary week` |
| 282 | `玛莎这周是平常的一周` | `Masha’s week is an ordinary one` → `Masha's week is an ordinary one` |
| 314 | `经济学家日 a` | `Economists’ Day a` → `Economists' Day a` |
| 322 | `莉莉·布里克是马雅可夫斯基的缪斯` | `Lilya Brik was Mayakovsky’s muse` → `Lilya Brik was Mayakovsky's muse` |

### tm-en.json（5 值、5 字符，均为 `’` → `'`）

| 行 | 键 | 改前 → 改后 |
|---|---|---|
| 10 | `11 月 11 日经济学家日` | `11 November — Economists’ Day` → `11 November — Economists' Day` |
| 60 | `УРОВЕНЬ A2　День полиции, День экономиста и обычная неделя　警察节、经济学家日与平常的一周` | `…　Police Day, Economists’ Day and an ordinary week` → `…　Police Day, Economists' Day and an ordinary week` |
| 180 | `玛莎这周是平常的一周` | `Masha’s week is an ordinary one` → `Masha's week is an ordinary one` |
| 200 | `经济学家日 a` | `Economists’ Day a` → `Economists' Day a` |
| 204 | `莉莉·布里克是马雅可夫斯基的缪斯` | `Lilya Brik was Mayakovsky’s muse` → `Lilya Brik was Mayakovsky's muse` |

### tm2-en.json（5 值、5 字符，均为 `’` → `'`）

| 行 | 键 | 改前 → 改后 |
|---|---|---|
| 27 | `11 月 11 日经济学家日` | `11 November — Economists’ Day` → `11 November — Economists' Day` |
| 76 | `УРОВЕНЬ A2　День полиции, День экономиста и обычная неделя　警察节、经济学家日与平常的一周` | `…　Police Day, Economists’ Day and an ordinary week` → `…　Police Day, Economists' Day and an ordinary week` |
| 186 | `玛莎这周是平常的一周` | `Masha’s week is an ordinary one` → `Masha's week is an ordinary one` |
| 205 | `经济学家日 a` | `Economists’ Day a` → `Economists' Day a` |
| 208 | `莉莉·布里克是马雅可夫斯基的缪斯` | `Lilya Brik was Mayakovsky’s muse` → `Lilya Brik was Mayakovsky's muse` |

### miss-tr-en.json（1 值、2 字符）

| 行 | 键 | 改前 → 改后 |
|---|---|---|
| 37 | `УРОВЕНЬ B1　«Чёрная пятница»: скидки с 16 ноября　“黑色星期五”：11月16日开始打折`（键不动） | `…　“Black Friday”: sales from 16 November` → `…　"Black Friday": sales from 16 November` |

SHA-256（改后）：map-en.json `6ef559d5d46a39b0f4a3212903614b061d16335a1329db7b4d0e2080c20c57b7`；tm-en.json `a8ac7ca4605688d4585ea846fde798b92800df70f208cd29c20402474eb9db2c`；tm2-en.json `59b921c2f5df6aac4bf31df717628c71c978cdd8a3e11100ded053707f1f5607`；miss-tr-en.json `54afc4c7a74706364034f8953ab01340af1a13b0fefb76017f60b302222b977f`。

## 2. 途中事故（已修复，无残留）

- 第一版替换脚本把 `“Black Friday”` 直换成裸直引号 `"Black Friday"`，未转义：写盘后 `json.load` 断言失败（`Expecting ',' delimiter: line 109`），脚本随即中止，tm-en.json / tm2-en.json / miss-tr-en.json 当时尚未触碰。map-en.json 当时一度为非法 JSON，随即原地修复为 JSON 转义形 `\"Black Friday\"`，验证：再次 `json.load` 通过，且解析值与 fix1 版内字符串逐字相等（已断言）。无他文件受影响（mtime 核查见 §4）。

## 3. 未动的有意保留（改后残留，逐项列理由）

### 3a. 键——绝对不动（40 行扫描命中 = 20 个键 × 2 字符）

- `map-*.json` 10 文件（de/en/es/fr/it/ja/ko/nl/pt/zh-tw）各 1 键、`miss-tr-*.json` 10 文件各 1 键：键内 `“黑色星期五”`（中文释义）是查找键，动了即断查找。已核实：改后解析 diff 键集合零变化。

### 3b. 各语正确标点（读者语译文值内，逐文件计数为改后全扫实测）

| 文件 | 残留 | 不动理由 |
|---|---|---|
| map-de.json 1、miss-tr-de.json 1 | `„Schwarzer Freitag“` 里的 U+201C（闭引号） | 德式引号，各语正确标点（任务明文） |
| map-fr.json 1（abstract `l’anniversaire`）、tm-fr.json 33、tm2-fr.json 32、miss-tr-fr.json 23（含 abstract `l’anniversaire`） | U+2019 法语省音撇号（`l’/d’/c’/s’` 等） | 法语正字法必需的省音撇号；法语版已 33/33 零问题定稿，Newsreader 正文语境 |
| tm-it.json 15、tm2-it.json 14 | U+2019 意大利语省音撇号（`l’/d’/un’/dall’` 等） | 意大利语正确标点，Newsreader 正文语境 |
| tm-nl.json 4、tm2-nl.json 4、map-nl.json 1（abstract `thema’s`）、miss-tr-nl.json 1（abstract `thema’s`） | U+2019 荷兰语属格/复数 `’s`（`thema’s`、`pagina’s`、`Masha’s`） | 荷兰语正确标点，Newsreader 正文语境 |
| map-zh-tw.json 2、miss-tr-zh-tw.json 2 | `“黑色星期五”` 里的 U+201C/U+201D | 中文全角引号，CJK 正确标点（绕中文文本的引号） |
| fr/ru-fr-occlusion.json 2 | 遮挡审计记录引用的法语版可见文本（`DONNÉES D’EXERCICE`、`CORRIGÉ — …`） | 审计证据原文，须逐字保留 |

### 3c. 源串记录——不是译文值

| 文件 | 残留 | 不动理由 |
|---|---|---|
| miss-*.json 10 文件各 2、miss2-*.json 10 文件各 2 | 列表元素即未译源串本身（即查找键） | 缺失清单，改了即篡改“缺什么”的记录 |
| w47-inventory.json 2 | `content56.py` 条目下引用的核心 band 源串 | 库存记录，须与核心源串逐字一致 |

### 3d. 子目录冻结件——不在本次机制表范围（111 行 PY 命中，全部未动）

| 位置 | 残留 | 不动理由 |
|---|---|---|
| 17 份 `*/freeze*/build-copy/check_core.py` 各 2（共 34） | `CLOSES = set("…」』”’")` 里的 `”`、`’` | 标点字符集定义（分类用），不是可见文本；改了即改审计工具行为 |
| 17 份 `*/freeze*/build-copy/content7.py` 各 2（共 34）+ fr/freeze/build-copy/content7.py 另 3 个 U+2019（L111 ×2、L116 ×1） | P7 `“чёрной пятнице”`（Newsreader，fix1 已裁定保留）+ 3 个法语 `’`（冻结的法语版 P7 练习串） | 冻结的已建版源副本；P7 对属 fix1 明确保留项 |
| en/freeze/build-copy/content56.py 2 | 冻结副本里仍带 `“Black Friday”`（fan-out 冻结时快照） | 冻结历史快照；live 源已由 fix1 在 `production/2026-w47/2026-w47-ru-en/content56.py` 修掉，本次修的是机制表源头 |
| de/freeze/build-copy/content56.py 1 | 冻结副本里 `„Schwarzer Freitag“` 的闭引号 | 德式引号（同 3b）+ 冻结副本 |
| zh-tw/freeze/build-copy/content56.py 2 | 冻结副本 band 调用里键串的 `“黑色星期五”` | 键（同 3a）+ 冻结副本 |
| fr/freeze/build-copy/content56.py 14、content12.py 9、content34.py 8、content8.py 4 | 冻结的法语版源副本里的法语 `’` | 法语省音撇号（同 3b）+ 冻结副本 |

（顶层 6 个生成器 `apply_ru.py`、`build_map.py`、`adjudicate_ru.py`、`tm_ru.py`、`tm_ru2.py`、`s11_check.py`：改前改后均 0 命中，无需改动。）

## 4. 改后验证

- **改后全扫**：递归扫描全目录（脚本 `/tmp/ru-sweep-scan.py`，逐 JSON 解析区分键/值）：改前 348 行命中（KEY 40 / VAL 197 / PY 111）→ 改后 329 行（KEY 40 / VAL 178 / PY 111）。差值恰为 19 行 = 本次修掉的 19 个字符（map-en 7、tm-en 5、tm2-en 5、miss-tr-en 2）。KEY、PY 零变化。
- **en 读者语值归零**：改后 map-en.json / tm-en.json / tm2-en.json / miss-tr-en.json 的值里 U+201C/U+201D/U+2019 共 0 处；四文件仅剩 4 行命中，全部是键里的 `“黑色星期五”`（map-en 2、miss-tr-en 2，见 3a）。
- **JSON 校验**：全目录递归 122 个 `*.json` 全部 `json.load` 通过（0 失败；与 ja 目录不同，本目录改前即无已坏 JSON）。
- **PY 校验**：`python3 -m compileall` 全过（RC=0）。注：compileall 写出的 `.pyc` 已清理——仅删 mtime 在本次运行窗口（08:38 UTC 之后）的新字节码，现存 34 个 `.pyc` 均为 08:38 之前、fan-out 阶段已有的；17 个 `__pycache__` 目录保留原状。
- **改动面核查**：`find -newermt '2026-11-11 08:35 UTC'`（非 `.pyc`）仅列出本次 4 个 JSON 文件；其余文件（含全部子目录冻结件、顶层生成器）mtime 未动。
- 顶层 `meta-*.json`、`w47-inventory.json`（除 3c 所列源串记录外）、`tm-de/es/pt/ja/ko/zh-tw.json`、`tm2-de/es/pt/ja/ko/zh-tw.json`、`miss-tr-es/it/ja/ko/pt.json`：0 处英文弯标点，无需改动。
