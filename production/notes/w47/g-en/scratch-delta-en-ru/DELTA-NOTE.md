# DELTA-NOTE — 2026-W47 en-ru Q73 键同步 delta（fix2）

- 版：`2026-w47-en-ru`（英语目标语 × 俄语读者版），VOL.4，8 版，150 题
- 修复员：en-ru delta agent；日期：2026-11-11
- 依据：core-en fix2 已定稿（Q73 键 `speak` → `up`），re-proof (a) 通过
- 范围：只改本版内 `content56.py:49` 一行 + 重建产物；未碰 core-en、其他 9 个 en-* 版、tools/、issues/；未 commit、未 push（由协调员统一做）

## 0. 开工探针 + 修前核对（全部一致才动手）

- `ls /dev/null` 存在；`git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`；scratch 目录真实写文件成功（`probe.txt`）。
- 修前三件 SHA 与任务书逐字节一致：

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf`（印） | 29,241,529 | `fb849665c691cfb687f50d523a2f551ccc09cef806b942624e2f316395dab994` |
| `The-Lucerna-VOL4-en-ru.web.pdf`（网） | 2,452,560 | `5aac849d1b2d03bbf6838c4850a4c47d3df8fe5a01b726a306c8c1e3c5a28304` |
| `2026-w47-en-ru.text.md`（文） | 62,384 | `bf3a9127b62eaec3a2aa53359a28ffdd2aa8f503df53c24fcec7d77ea1ef6de7` |

- 修前三源同错（预期状态）：registry Q73 key = `speak`；text.md:1151 =
  `73. [A2] Дополнить предложения — speak (speak up = говорить открыто)`；
  P8 SVG 答案段 `speak · 74. d · 75. a ·`；P5 题干 `Speak ___: tell a teacher.`。
- 核心对照（只读）：core-en `content56.py:49` 已为 `up`（note `speak up = 大声说出来`，
  俄语版 note 不同是读者语翻译，应有差异）。
- D1 修复态修前核实：`content12.py:85` =
  `p.text(gx + 22, byy + 76, "Относительный интерес, не точные.", 19, "sans", False, GREY)`；
  `scratch-fanout-en/map-ru.json:228` =
  `"相对热度示意，非精确搜索量。": "Относительный интерес, не точные."`；
  P1 SVG 同句在位。旧句 `не точные цифры` 三处均为 0 次。

## 1. 改动（只改一行）

`content56.py:49`：

```diff
-f.ex("A2", "Дополнить предложения", "speak", "speak up = говорить открыто",
+f.ex("A2", "Дополнить предложения", "up", "speak up = говорить открыто",
      "Speak ___: tell a teacher.", instr="Заполни")
```

note 与 stem 一字未动。`content12.py:85`（D1 修复）未动；map-ru.json 未动（只读核对，
未 re-fanout）。重建：版内 `run.py` → `render.py` → `dump_reg.py`（fresh dump 写入其
硬编码路径 `scratch-fanout-en2/fanout/ru/registry.json` 后拷回版内 `registry.json`；
未走有 stale-registry bug 的 `gates.sh` 拷路径）→ `make_textmd_w47.py` → `tools/webpdf.py`。

## 2. 新交付物（三件新 SHA）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-ru.pdf` | 29,241,520（修前 29,241,529，−9） | `a42edc0e0bd0b7bbcac0163ad70639a1b400cb2cf6df4584db4f544f76c5d594` |
| `The-Lucerna-VOL4-en-ru.web.pdf` | 2,452,562（修前 2,452,560，+2；< 7 MB） | `9e636240016e11c0b3738f9389d66f7b6f6729f1385c2cb0a379fe9f3f873a09` |
| `2026-w47-en-ru.text.md` | 62,381（修前 62,384，−3 = speak→up 恰 3 字节） | `78c1b137e66571faf5bc51366f05edebfde152e0b30d717b926d1c92505794a4` |

- 两 PDF 均为 8 页、1462.5 × 2025 pt。

## 3. Diff 证据（恰好一处）

- Registry diff（`registry-pre.json` vs `registry-new.json`）：恰 1 条，n=73
  `key: "speak"` → `"up"`，note `speak up = говорить открыто` 不变；其余 149 条逐字相同。
- text.md diff（`text-pre.md` vs 新件）：恰 1 行，1151 行
  `73. [A2] Дополнить предложения — speak (…)` → `… — up (…)`。
- SVG 变化范围（修前 `svg-pre.sha256` vs 修后 `svg-post.sha256`）：**仅 `p8-test.svg` 变，
  其余 7 页字节一致——这是正确且预期的**：Q73 键只出现在 P8 答案页，不出现在 P5 题干页
  （P5 只印 `Speak ___` 空白 + `speak up` 注记，键本身从不上 P5），所以 p5 与修前字节一致
  不是异常、无需返工。en-es delta 已证实此点（p8 含 `73. up`，p5 不变）；本版实测一致：
  p8 含 `73. up`，p5 不含 `73. up` 且哈希与修前相同。

## 4. Q73 四源一致（修后，`verify_delta.py` / `verify_delta.log`）

| 源 | 值 |
|---|---|
| registry n=73 | key `up`，note `speak up = говорить открыто` |
| text.md:1151 | `73. [A2] Дополнить предложения — up (speak up = говорить открыто)` |
| P8 印出键（p8-extract.json + SVG） | extract key 73 = `up`；SVG 答案段 `up · 74. d · 75. a ·`；P8 卡目视答案区 `73. up` |
| P5 题干 + 注释 | `Speak ___: tell a teacher.`；gloss `speak up = говорить открыто` 在位 |

## 5. D1 保留证据（重建前后三重核查，均为修复态）

| 处 | 修后值 |
|---|---|
| `content12.py:85` | `Относительный интерес, не точные.`（19 px sans） |
| `scratch-fanout-en/map-ru.json:228` | `"相对热度示意，非精确搜索量。": "Относительный интерес, не точные."`（文件未动） |
| P1 SVG | gloss `Относительный интерес, не точные.` 在位；旧句 `не точные цифры` 在 P1 SVG 与 content12.py 均为 0 次 |

重建流程未覆盖该 gloss（`content12.py` 自始至终未改；重建后 P1 SVG 字节与修前一致）。

## 6. 全部门禁（重建后新成品上重跑，全部通过）

| 门 | 要求 | 结果 | 日志 |
|---|---|---|---|
| run.py | rc=0，TOTAL 150，0 溢出 | exit 0，TOTAL 150，MODEL 82，OVERFLOW/TOO WIDE 0 次 | `run.log` |
| render.py | rc=0，印 PDF 写出 | exit 0，print PDF 29,241,520 B | `render.log` |
| dump_reg / text.md | 150 条，stub=real | registry 150（页 10/17/18/18/18/18/12/39；A2 62 / B1 66 / B2 22）；textmd RC=0，stub 150 = real 150 | `gates/dump_reg.log`、`textmd.log` |
| occlusion | 0 flags（真实审计，不用 --selftest） | 0 flags，selftest OK（6 类 planted 均触发，clean 对照静默） | `gates/occlusion.log`、`gates/occlusion.json` |
| p8 extract | 150/150 | 150/150；noted 60/150，与 core 同集（noted set == core noted: True） | `gates/p8-extract.log`、`gates/p8-extract.json` |
| p8 compare | CLEAN | **status CLEAN**，missing=[] extra=[]，keydiff=[137, 138, 139, 140, 150]（预期：读者语翻译键 + 写作题短标签）；已读 `p8-compare.json` 本体 | `gates/p8-compare.json`、`gates/p8-compare.log` |
| freeze baseline | 8/8（--build 指含 run.py 的构建目录、即 core-en，--core-svg 另指 core-en/svg 对照；另 direct-sha 只读对照 8/8，两者即合格） | 8/8 SVGs byte-identical；core integrity：shipped core SVGs unchanged；direct sha 8/8 | `gates/freeze.log`、`gates/freeze-direct.log` |
| freeze diff | 新增 CJK 仅 U+3000 | TOTAL added CJK 9，全部 U+3000 | `gates/freeze-diff.log`、`gates/freeze-diff.json` |
| 印/网文字层 | 逐页一致 | 各 47,646 字符（修前 47,649，−3 = speak→up），token-multiset diff 0/0，逐页 byte-identical 8/8 （5556/6621/5756/6182/5175/6110/7379/11947 B） | `gates/printweb.log` |
| webpdf | RC=0，< 7 MB | RC=0，2,452,562 B | `gates/webpdf.log` |
| P8 最小字号 | ≥ 9.75 pt | 10.12 pt（P1 最小 11.62 pt） | `gates/verify.log`（verify_ed） |
| creambox（canonical PIL 真墨） | 0 溢出 | RC=0，OVERFLOW 0 | `gates/creambox.log` |
| h-containment | H-SPILL 0 | H-SPILL total: 0 | `gates/h-containment.log` |
| boxtitle 源码 | 12/12 fit | PASS（最紧 ODD SOCKS 398.3，+6.2；SATURDAY 328.9，+75.6） | `gates/boxtitle.log` |
| boxtitle SVG | 18/18 fit | 18/18，overflows 0 | `gates/boxtitle-svg.log` |
| check_s11 | ALL PASS | ALL §1.1/P8 CHECKS PASS | `gates/check_s11.log` |
| verify_ed | ALL PASS | VERIFY ALL PASS（Q39 a / Q40 d / Q125 A；P8 min 10.12 pt；SVG zero real CJK） | `gates/verify.log` |
| keycheck | 149/150 + #150 例外；vs core 仅 5 读者键 | (a) registry-vs-P8extract exact 149/150，exc=[150]，mismatch=[]；(b) registry-vs-core **145/150**，diff 仅 137–140、150 —— **Q73 现与 core 一致**（fix1 时为 144/150，Q73 不同）；noted set == core noted True；extract keys 150，missing none | `gates/keycheck.log` |
| 150 题三源 | registry / P8 extract / text.md 答案逐题一致 | 150/150 exact，0 差异（#150 为已知 short-label 例外） | `verify_delta.log` |
| 孤儿标点全版扫 | 0 | 0（视觉行定义：按 y 分组后的整行首尾标点） | `verify_delta.log` |
| 引号/禁词 | 201C=201D，2019=0，禁词 0 | text.md 201C=81 / 201D=81，SVG 82/82，U+2019=0，禁词 0 | `verify_delta.log` |
| 8 页逐页目视 | 干净 | 8/8 卡目视干净；P5 Q73 题干在位，P8 答案区 `73. up`，P1 D1 gloss 在 cream 框内留白充足 | `cards/*.png`（版内） |
| D5 字体 | 只记录、不判、不修 | 1798 个 `<text>`，26 种字号，与 fix1 记录逐项相同 | `verify_delta.log` |

## 7. 150 题键与题干适配抽查（Q73 教训：三源一致不够）

用 stub 重跑内容源逐条提取（`keyfit2.py` / `keyfit.log`，n 与 registry 逐一对位，
key mismatches: NONE）：

- **57 条填空/改写题**（题干含 `___` 或 `→`）：逐条核对键填入空格/改写后成句——
  Q1 midterm、Q2 call、Q3 seats、Q4 majority、Q5 changed、Q6 January、Q11 November、
  Q12 January、Q13 1、Q14 Thursday、Q15 27、Q16–19 will 句型、Q34 opens、Q35 mentor、
  Q36 twice、Q37 jungle、Q42–45 过去时改写、Q52 hosted、Q53 lasts、Q54 eight、Q55 won、
  Q60–63 过去时改写、Q70 silence、Q71 socks、Q72 rights、**Q73 up（Speak up: tell a teacher.）**、
  Q78–81 现在进行时改写、Q94 certify、Q95 call、Q96 changed、Q97 takes、Q98 differs、
  Q99 official、Q100 won、Q101 more、Q102 lost、Q103 will、Q104 published、Q105 whether、
  Q106 chose、Q107 win、Q133 will meet、Q134 won、Q135 more、Q136 whether——**全部合理，0 不符**。
- **14 条 direct-reg 题**（cloze / 对话 / 写作，题干在 P8 段落中）：Q112 Tuesday
  （On Tuesday morning, November 3——11 月 3 日确为星期二）、Q113 call、Q114 continues、
  Q115 will meet、Q116 writes、Q117 will certify、Q118 wears、Q119 will watch；
  Q145 row（Which row? — The front row）、Q146 film、Q147 popcorn、Q148 show、
  Q149 Friday（film opens on Friday, November 20——11 月 20 日确为星期五）；
  Q150 开放写作题，无空格。——**全部合理，0 不符**。
- 星期核验（`date -d`，America/Toronto）：2026-11-03 星期二、2026-11-20 星期五、
  2026-11-26 星期四（Q14 Thanksgiving）、2026-11-27 星期五（Q15 Black Friday）。

## 8. 未动项与说明

- 未动：core-en（只读对照）、其他 9 个 en-* 读者版、tools/、issues/、SOP、map-ru.json。
  未跑 insert.py / lint --write；未 commit、未 push。仓库工作区另有其他并行 agent 的改动
  （W43、tools/、其他 W47 版），与本次无关；本版 production 源在 git 中尚为 untracked
  （待协调员统一提交），故以修前/修后文件快照（`registry-pre.json` / `registry-new.json` /
  `text-pre.md` / `svg-pre.sha256` / `svg-post.sha256`）为 diff 证据。
- `WEEKLY-KIT.md`（版内）已更新：§2 三件新 SHA/字节、§3 增加 delta 重跑 gate 摘要、
  §5 增加第 8 条 delta 记录（item 7 末尾加注“已由本次 delta fix2 执行”）。
- 过程注记：`gates.sh` 的 stale-registry 路径 bug（fix1 §7 已记）仍在，本次未走 `gates.sh`，
  手动按步骤跑并把 fresh dump 直接拷回版内；creambox 与 h-containment 首次调用传参有误
  （creambox 须传 SVG 文件列表、h-containment 须传印 PDF 路径），已按 build_lang.sh /
  proof 脚本的正确用法重跑通过。

## 9. 本目录产物

- `DELTA-NOTE.md`（本文件）、`probe.txt`、`run.log`、`render.log`、`textmd.log`、
  `registry-pre.json`、`registry-new.json`、`registry-post.json`、`text-pre.md`、
  `svg-pre.sha256`、`svg-post.sha256`、`verify_delta.py` + `verify_delta.log`、
  `keyfit.py`（旧版，解析不全，仅备查）+ `keyfit2.py` / `keyfit.log`、
  `gates/`（dump_reg、occlusion log/json、p8-extract-core/ed log/json、p8-compare log/json、
  freeze log/diff log/json、freeze-direct.log、freeze-final/、webpdf、printweb、check_s11、
  verify、boxtitle、boxtitle-svg、creambox、h-containment、keycheck + keycheck.py、
  h-containment.py、check_s11.py、sweep_titles.py、sweep_svg_titles.py、verify_ed.py）。

## 10. 结论

- Q73 键已同步为 `up`，四源一致；D1 修复完整保留；全部门禁绿；键-题干适配抽查 0 不符；
  8 页目视干净；改动范围最小（1 行源码 + 重建产物，仅 p8 SVG 变）。
- 更正（2026-11-11，协调员）：仅 p8 变化、p5 与修前字节一致是正确且预期的（键只印 P8，
  从不上 P5），不作异常、不返工；freeze baseline 的 `--build` 指含 run.py 的构建目录、
  `--core-svg` 另指对照路径，本次 baseline 8/8 + direct-sha 只读对照 8/8 即合格（已跑出）。
- **可进 proof2。**
