# FIX-LOG — 2026-W47 en-ru fix1 (proof1 (b) D1)

- 版：`2026-w47-en-ru`（英语目标语 × 俄语读者版），VOL.4，8 版，150 题
- 修复员：fix1 builder；日期：2026-11-11（UTC 约 13:21–14:50）
- 依据：proof1 (b) `scratch-proof-en-ru1/PROOF-NOTE.md` Defect 1（唯一缺陷）+ `GATE-LOG.md`；
  数字全部在盘上重测，不取信摘要。
- 范围：只改 `production/2026-w47/2026-w47-en-ru/` 内 2 个源文件 + `scratch-fanout-en/map-ru.json`
  （fan-out 源，与版内源须一致）；未碰 core-en、其他家庭、tools/、issues/；未跑 insert.py、
  lint --write；无任何 git 写操作（不 commit、不 push、不 reset、不 stash）。

## 0. 开工探针（双通）+ 对象核对

- `ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，成功。
- 在 `hidden_files/w47/scratch-fix-en-ru2/` 真实写文件成功（`probe.txt`）。
- 开工前三件 SHA 与任务书逐字节核对一致：

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf`（印） | 29,241,701 | `daf81d35cdf44e66dffaed2f2ab68da66251742a1be02cb1af95f8daeed9cdaf` |
| `The-Lucerna-VOL4-en-ru.web.pdf`（网） | 2,452,739 | `3fb58ae2e80f16460e7da5f5973cc5eb9ffc2687579b6fd88fb2d9eef41674fe` |
| `2026-w47-en-ru.text.md`（文） | 62,395 | `d59c98c0676f74352ce81557598641b91d4d17a4d033dbdd22e775199f0bbcf7` |

- 源行核对：`content12.py:85`
  `p.text(gx + 22, byy + 76, "Относительный интерес, не точные цифры.", 19, "sans", False, GREY)`；
  `scratch-fanout-en/map-ru.json:228`（`lit` 区）`"相对热度示意，非精确搜索量。" →
  `"Относительный интерес, не точные цифры."`。另 `text.md:87` 同句（重导覆盖）。

## 1. D1 在盘上核实属实（修前重测，与 proof1 一致）

- 框：P1 SEARCHES 框 cream rect x=1439.5, w=422.5 → 右缘 1862.0 SVG px；gloss 起点 x=1461.5。
- `svglib.text_w`（与 sweep 同一函数，Noto Sans CJK SC，Cyrillic 落在此字体）：
  旧句 409.0 px → 止于 1870.5 → **+8.5 px**。
- 归属：core 中文同位 gloss 同 x/字号只到 1725（余量 −134.5 px）；旧版 backup 同行同宽同为 +8.5
  （旧版已存在、非重建回归）。修法须在 19 px 下宽度 ≤ ~400 px（至少砍 ~10 px）。

## 2. 改动（只改两处，值一致）

候选实测（`svglib.text_w`, 19 px sans，框右缘 1862.0，起点 1461.5）：

| 候选 | 宽度 | 止于 | 余量 | 采用否 |
|---|---|---|---|---|
| 旧 `Относительный интерес, не точные цифры.` | 409.0 | 1870.5 | −8.5 | — |
| `Относительный интерес, неточные цифры.` | 404.6 | 1866.1 | −4.1 | 否（仍溢出） |
| `Относительный интерес, не точные числа.` | 398.4 | 1859.9 | +2.1 | 否（余量太薄） |
| `Относительный интерес, не цифры.` | 336.1 | 1797.6 | +64.4 | 否（丢了“精确”） |
| **`Относительный интерес, не точные.`** | **339.4** | **1800.9** | **+61.1** | **是** |

- 采用 `Относительный интерес, не точные.`：删 `цифры` 一词（复数形容词 `не точные` 仍指向省略的
  “цифры”，图表语境下所指明确），保留“相对热度、非精确数字”原意的两个实义成分（相对 + 不精确），
  余量 +61.1 px（≈ 旧溢出量的 7 倍）。
- 改动：
  - `scratch-fanout-en/map-ru.json:228`（`lit`）值 → `Относительный интерес, не точные.`
    （JSON 重载通过；旧串在该文件出现 0 次；其余 290 个键未动）。
  - `production/2026-w47/2026-w47-en-ru/content12.py:85` 同句 → `Относительный интерес, не точные.`
- 其余源文件零改动。

## 3. 重建（真版，全量）

```bash
cd production/2026-w47/2026-w47-en-ru
tools/venv/bin/python run.py        # exit 0，零 OVERFLOW / TOO WIDE；TOTAL exercises 150；MODEL words 82
tools/venv/bin/python render.py     # cards + print PDF
# gates.sh（scratch-fanout-en/ru/gates.sh）内：dump_reg.py、occlusion、p8 extract/compare、
# freeze baseline + diff、webpdf.py、print/web 文字层比对、make_textmd_w47.py
```

- SVG 快照比对（修前 `svg-before.sha256`）：**仅 `p1-front.svg` 变，其余 7 个 byte-identical**。
- 新 `p1-front.svg` gloss 元素：`<text x="1461.5" y="1244" font-family="Noto Sans CJK SC"
  font-size="19">Относительный интерес, не точные.</text>`；旧串在 p1 SVG 出现 0 次。

## 4. 新交付物（三件新 SHA）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf` | 29,241,529（修前 29,241,701，−172） | `fb849665c691cfb687f50d523a2f551ccc09cef806b942624e2f316395dab994` |
| `The-Lucerna-VOL4-en-ru.web.pdf` | 2,452,560（修前 2,452,739，−179；< 7 MB） | `5aac849d1b2d03bbf6838c4850a4c47d3df8fe5a01b726a306c8c1e3c5a28304` |
| `2026-w47-en-ru.text.md` | 62,384（修前 62,395，−11 = 删 "цифры " 恰 11 字节） | `bf3a9127b62eaec3a2aa53359a28ffdd2aa8f503df53c24fcec7d77ea1ef6de7` |

- 两 PDF 均为 8 页、1462.5 × 2025 pt。text.md 1305 行，第 87 行新 gloss，旧串 0 次；
  答案区 150 行与 registry 逐字一致（见 §5）。

## 5. D1 三重实测（修后，PIL 真墨 + 渲染像素双重复测）

| 方法 | 修前 | 修后 | 结论 |
|---|---|---|---|
| (a) SVG advance（`svglib.text_w`） | 409.0 px，止于 1870.5，**+8.5** | 339.4 px，止于 1800.9，余量 **+61.1 px** | PASS |
| (b) 印 PDF 真墨（PyMuPDF spans） | span 右 1403.5 pt vs 框 1396.5 pt，**+7.0 pt** | span x[1096.1, 1351.3] pt vs 框右 1396.5 pt，余量 **+45.2 pt** | PASS |
| (c) 150 dpi 渲染像素（`pdftoppm -r 150`，新渲染 `render/print-p1-1.png`） | 最右墨点 1401.6 pt，**+5.1 pt** | 最右墨点 1349.3 pt（px 2811），余量 **+47.2 pt**；cream→white 交界 1396.3 pt（proof 测 1396.5–1397 pt） | PASS |

- 目视：`render/p1-searches-gloss-new.png`（放大裁图）——尾部 `не точные.` 落在 cream 底上，
  右侧余白充足。脚本：`verify_fix.py`（日志 `verify_fix.log`）。

## 6. 全部门禁（重建后重跑，全部在新成品上）

| 门 | 要求 | 结果 | 日志 |
|---|---|---|---|
| run.py | rc=0，TOTAL 150 | exit 0，TOTAL 150，MODEL 82，OVERFLOW/TOO WIDE 0 次 | `run.log` |
| occlusion | 0 | 0 flags，selftest OK | `gates/occlusion.log` |
| p8 extract | 150/150 | 150/150；noted 60/150，与 core 同集 | `gates/p8-extract.log` |
| p8 compare | CLEAN，keydiff [137–140,150] | CLEAN，missing=[] extra=0，keydiff=[137, 138, 139, 140, 150]（预期） | `gates/p8-compare.json` |
| freeze baseline | 8/8 | 8/8 SVGs byte-identical；direct sha 8/8 | `gates/freeze.log`、`gates.log` |
| freeze diff | 新增 CJK 仅 U+3000 | TOTAL added CJK 9，全部 U+3000；无英文正文改动 | `gates/freeze-diff.log` |
| 印/网文字层 | 逐字节一致 | 各 47,649 字符（修前 47,655，−6 = 删 "цифры " 恰 6 字符），token-multiset diff 0/0，逐页 byte-identical 8/8 | `gates.log`、`verify_fix.log` |
| P8 最小字号 | ≥ 9.75 pt | 10.12 pt（P1 最小 11.62 pt） | `verify_fix.log`、`gates/verify.log` |
| creambox（canonical） | 0 真墨溢出 | RC=0，0 OVERFLOW | `gates/creambox.log` |
| h-containment | 全书 H-SPILL 0 | H-SPILL total: 0（V-SPILL 仅设计间距，同 proof1 模式） | `gates/h-containment.log` |
| boxtitle 源码 | 12/12 fit | 12/12，0 over budget（最紧 ODD SOCKS 398.3，+6.2） | `gates/boxtitle.log` |
| boxtitle SVG | 18/18 fit | 18/18，overflows 0 | `gates/boxtitle-svg.log` |
| check_s11 | ALL PASS | ALL §1.1/P8 CHECKS PASS | `gates/check_s11.log` |
| verify_ed | ALL PASS | VERIFY ALL PASS（22/22；Q39 a / Q40 d / Q125 A；P8 min 10.12 pt） | `gates/verify.log` |
| keycheck | 149/150 仅 #150 ✓ 例外 | registry-vs-P8extract exact 149/150，exc=[150]，mismatch=[] | `gates/keycheck.log` |
| 150 题三源逐题手验 | registry / P8 extract / text.md 答案逐题一致 | 150/150 exact（两两比对，0 差异；#150 为已知 short-label 例外） | `verify_3src.log` |
| 孤儿标点全版扫 | 0 | 0（视觉行定义：按 y 分组后的整行首尾标点；core-en 对照亦 0。注：按单个 `<text>` 元素扫会把字体分段残片误报为 23 处——非真孤儿，见 `verify_fix.log` 原始扫） | `verify_fix2.log` |
| 引号/禁词 | 201C=201D，2019=0，禁词 0 | text.md 201C=81 / 201D=81，SVG 82/82，U+2019=0，禁词 0 | `verify_fix.log` |
| D5 字体 | 只记录、不修 | 1798 个 `<text>`，26 种字号，与 proof1 记录逐项相同（13.5×75 … 196×1） | `verify_fix.log` |

## 7. 修建途中一桩既有门脚本破绽（已修通，附实录）

- 现象：`gates.sh` 跑完后 `make_textmd_w47.py` 失败：`AssertionError: key mismatch`
  （stub/real 各 150 条，5 键不同：Q39 a/d、Q40 d/a、Q52 hosted/hosts、Q55 won/sold、Q125 A/C）。
- 根因（与我改动无关）：`gates.sh` 注释称 `dump_reg.py` 会把新 registry 写到
  `scratch-fanout-en/ru/registry.json`，但 `dump_reg.py` 硬编码写到另一处
  `scratch-fanout-en2/fanout/ru/registry.json`；于是 `gates.sh` 的 `cp $S/registry.json
  $ED/registry.json` 拷的是 **04:39 的 stale 旧 registry**（refanout 前的键：Q39/40 互换、
  Q52 hosts、Q55 sold、Q125 C，另 Q46/82/83/84 四条 note 旧措辞——共 9 条差异），而 exporter
  以它为 real registry 校验即断言失败。旧 registry 与已发 text.md 答案不一致（text.md 早已是新键）。
- 处理：以刚跑出的 fresh dump（`scratch-fanout-en2/fanout/ru/registry.json`，与 stub 运行及
  P8 extract 逐键一致）覆盖 stale 的两处（`scratch-fanout-en/ru/registry.json` 与版内
  `registry.json`）；stale 旧文件原样保存为本目录 `registry-stale-0439.json`（备查）。
  之后 `make_textmd_w47.py` RC=0（`textmd.log`：stub 150 = real 150）。`gates.sh` 本身未改
  （工具归协调员；建议后续把 `dump_reg.py` 的写路径或 `gates.sh` 的拷路径对齐一处）。

## 8. 新发现（修门中发现，**未修**——超出本次 D1 范围，交协调员 / re-proof）

**Q73 键与题干不符（题干-答案错误，三源一致故一致性门禁查不出）。**

- 题干（core 与版内英文完全相同，`content56.py:49` 附近）：
  `Speak ___: tell a teacher.` —— 空格处须填小品词，正确答案是 **`up`**（speak up）。
- 版内三源一致地错：registry key `speak`、P8 extract `speak`、text.md 答案
  `73. [A2] Дополнить предложения — speak (speak up = говорить открыто)`。
  "Speak speak: tell a teacher." 不成句。
- core-en 现已是对的：key `up`（note `speak up = 大声说出来`）。proof1 当时的 keycheck (b)
  为 registry-vs-core 145/150（仅 5 个读者语键不同），说明 proof 时 core 也是 `speak`；
  core `content56.py` 在今天 14:28 被并行的 en-zh-cn 工作改过（`content56.py` mtime
  14:28:37，core `registry.json` 14:33:57 重生成），把 core 的 Q73 改成了 `up`，版内未同步。
  本次 keycheck (b) 为 144/150，除 5 个读者语键外仅 Q73 一处不同。
- 核查范围：已把 44 条含 `___` 的填空/改写题逐条对过题干与键——**仅 Q73 一处不符**，其余 43 条
  均正确（"Break the silence" ✓、"Democrats won the House" ✓ 等）。
- 处置：**本次未动**（任务范围 = D1 一项；改答案键属另一缺陷类，须协调员定）。请 re-proof
  复核并决定是否立 fix2（改版内 `content56.py:49` 的 key `speak`→`up` 即可，note 不变；
  之后须重建 + 重跑全部门禁 + 三件 SHA 再变）。

## 9. 未动项与说明

- 未动：core-en（我未写 core 任何文件；core `content56.py`/`registry.json` 在 14:28–14:33
  的改动是并行的 en-zh-cn 工作，我只读到它们）、其他 129 版、tools/、issues/、SOP。
  未跑 insert.py / lint --write；未 commit、未 push。
- `registry.json`（版内）被 `gates.sh` 的既有步骤 + §7 的 fresh-dump 覆盖刷新为当前真值
  （与已发 text.md 答案、P8 extract 一致）；`__pycache__`、cards/、svg/（8 个均重写，
  内容仅 p1 变化）为重建的常规写出。
- `WEEKLY-KIT.md`（版内）已更新：§2 三件新 SHA/字节、§3 fix1 重跑 gate 摘要、§5 增加
  fix1 记录（含 §7、§8 两观察）、§9 增加 fix1 产物目录。
- 观察项（proof1 的 8 条）：未动（本次只修 D1）。

## 10. 本目录产物

- `FIX-LOG.md`（本文件）、`GATE-LOG.md`（见下）、`run.log`、`render.log`、`gates.log`、
  `textmd.log`、`verify_fix.py` + `verify_fix.log`、`verify_3src.log`、`verify_fix2.log`、
  `gates/`（occlusion、p8-extract/compare、freeze log/diff、webpdf、check_s11、boxtitle、
  boxtitle-svg、verify、keycheck+keycheck.py、creambox、h-containment+h-containment.py）、
  `render/`（150 dpi print P1 + `p1-searches-gloss-new.png`）、`svg-before.sha256`、
  `registry-stale-0439.json`（§7 的 stale registry 原样保存）、`probe.txt`。
- `GATE-LOG.md`：机械门逐项记录（与本文件 §6 同源）。
