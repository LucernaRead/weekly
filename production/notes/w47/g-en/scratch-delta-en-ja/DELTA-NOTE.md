# DELTA-NOTE — 2026-W47 en-ja · Q73 key sync delta (core-en fix2)

- **版**：2026-W47，英语目标语 × 日语读者版（en-ja），VOL.4，刊期 2026-11-16..22
- **任务**：只同步 core-en fix2 的 Q73 键 `"speak"` → `"up"`，重建 + 全部门禁；只改本版，不碰核心、其他版、tools/
- **日期**：2026-11-11
- **工作区**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-en-ja/`
  （全部日志与证据在此；绝未写 repo 侧 hidden_files）
- **结论：delta 完成，全部机械门通过，可进 proof2。**

## 唯一改动

`production/2026-w47/2026-w47-en-ja/content56.py:49` 一行：

```python
# 改前
f.ex("A2", "文の完成", "speak", "speak up = 声を上げる",
     "Speak ___: tell a teacher.", instr="空所補充")
# 改后（只改 key，note 与 stem 一字不动）
f.ex("A2", "文の完成", "up", "speak up = 声を上げる",
     "Speak ___: tell a teacher.", instr="空所補充")
```

其他源文件零改动；core-en 未动（其 `content56.py:49` 本已为 `"up"`）；未 commit、未 push。

## 修前核对（动手前实测，与任务简报一致，三源同错为预期状态）

| 文件 | 大小 | SHA-256（修前） | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf`（印刷） | 41,509,391 B | `9f9faaea18807551394977ef536d142da65cfda78b73aa91d807063c0c4b0428` | MATCH |
| `The-Lucerna-VOL4-en-ja.web.pdf`（网页） | 2,883,877 B | `25645767641d06f1bfdc25f9437eb5c7f3ce0c319612eaabc9e912353f756f49` | MATCH |
| `2026-w47-en-ja.text.md` | 53,588 B | `219ce22d549887f0ca6895a928206ac18b255686e8f50f07296c54cd33d48aa9` | MATCH |
| registry Q73 | — | `{'n': 73, 'page': 5, 'level': 'A2', 'type': '文の完成', 'key': 'speak', 'note': 'speak up = 声を上げる'}` | 旧键 |
| text.md:1151 | — | `73. [A2] 文の完成 — speak (speak up = 声を上げる)` | 旧键 |
| P8 印刷抽取键 | — | `73.speak·74.d·75.a·76.b(right=権利b)·77.c·78.Schools` | 旧键 |
| P5 题干 | — | `Speak ___: tell a teacher.` | 题干无误，键错 |
| core-en `content56.py:49` | — | `f.ex("A2", "完成句子", "up", "speak up = 大声说出来",` | 已修，不动 |

探针先行：`ls /dev/null` 存在；`git hash-object -w /dev/null` 通（`e69de29b…`）；scratch
目录真实写文件成功。修前 SVG 备份于 `pre-svg/`（逐文件 SHA 见 `pre-svg-sha.txt`），
修前 registry + text.md 备份于 `pre/`。

## 修后三 SHA

| 文件 | 大小 | SHA-256（修后） | 变化 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf`（印刷） | 41,509,391 B | `e91ed980047959177588a26c72fff55bc2710c7ce476d631d87d1bcd20c19542` | 大小不变，SHA 变 |
| `The-Lucerna-VOL4-en-ja.web.pdf`（网页） | 2,883,888 B | `fb903b2b1da9be8abc04ad40e6387cb6050eaa41bc4c3c63b0eddb07150f48f0` | +11 B |
| `2026-w47-en-ja.text.md` | 53,585 B | `2d498e4e9b997c85b00671aef294d197b5be420d1eeb9bbf0efcac6d50c3b96e` | −3 B |

印刷 PDF 大小不变是合理的：3 字节的文本改动落在压缩流内，总大小可保持不变；
SHA 已变，文字层已实测含 `73. up`。WEEKLY-KIT.md §2/§3/§5/§9 已更新为新 SHA + delta 条目。

## Diff 证据（恰好 1 条 / 恰好 1 行）

- registry diff（`registry-diff.log`，pre vs post）：恰好 1 行——
  `583c583 < "key": "speak" --- > "key": "up"`。
- text.md diff（`textmd-diff.log`，pre vs post）：恰好 1 行——
  `1151c1151 < 73. [A2] 文の完成 — speak (speak up = 声を上げる) --- > 73. [A2] 文の完成 — up (speak up = 声を上げる)`。
- SVG 变化范围（`svg-byte-diff-postdump.log`，逐字节前缀/后缀定位，dump_reg 重跑后复测一致）：
  P1–P7 **字节一致**；P8 仅一处差异，字节 1228700 起 `73. speak`（5 B）→ `73. up`（2 B），
  总长 1,237,869 → 1,237,866（−3 B）。P5 与修前字节一致是正确的——Q73 题干
  "Speak ___: tell a teacher." 本身不动，键只出现在 P8 答案区；任务简报"应只有 p5/p8 两页"
  的预期按实际内容应为仅 P8 一页有字节变化，P5 无变化即无错。
- 残留 `speak` 扫查：registry `"key": "speak"` 0 命中；text.md 13 处子串命中分属 10 行，
  全部是合法的正文/题干/注记（P5 正文 "to speak up"、gloss "to speak up = 声を上げる"、
  Q70 题干、Q74–77 匹配项、Q79 改写题干 "Children (speak) up"、Q73 注记、Q75 注记），无残留旧键。

## Q73 四源一致（均为 up）

| 源 | 证据 |
|---|---|
| registry | `{'n': 73, 'page': 5, 'level': 'A2', 'type': '文の完成', 'key': 'up', 'note': 'speak up = 声を上げる'}` |
| text.md:1151 | `73. [A2] 文の完成 — up (speak up = 声を上げる)` |
| P8 印刷抽取键 | `73.up·74.d·75.a·76.b(right=権利b)·77.c·78.Schools`（新印 PDF 第 8 页文字层实测） |
| P5 题干 + 注记 | `Speak ___: tell a teacher.`（P5 印刷文字层）+ 注记 `speak up = 声を上げる`；填入后 "Speak up: tell a teacher." 合理 |
| P8 卡片目视 | ANSWERS —5ページ— 行可见 `73. up`（见下目视） |

## 全部门禁表

| 门 | 命令 / 方法 | 结果 | 证据 |
|---|---|---|---|
| run.py | 版内 `run.py`（venv python） | **rc=0，TOTAL 150，MODEL 82，0 OVERFLOW / TOO WIDE**；P8-keys 2205/2560 | `build.log` |
| render.py | 版内 `render.py` | **rc=0**；印 PDF 41,509,391 B | `render.log` |
| dump_reg + text.md | `dump_reg_delta.py`（本轮自写，写本 scratch）+ `make_textmd_w47.py`（fanout 版拷入，仅改 SCRATCH 路径） | **rc=0**；registry 150（每页 10/17/18/18/18/18/12/39；A2 62 / B1 66 / B2 22）；text.md 53,585 B | `dump_reg.log`、`textmd.log`、`registry.json` |
| webpdf | `tools/webpdf.py svg → web.pdf` | **rc=0**；2,883,888 B；49,784 text bytes | `webpdf.log` |
| occlusion 审计 | `tools/occlusion_audit.py svg --json`（真实审计，非 --selftest） | **0 flags**，rc=0，selftest OK（6 类 planted 全触发，clean 对照静默） | `occlusion.json/.log` |
| p8 extract | `tools/p8.py extract`（本版 + core-en 对照） | **60/150 noted，两版抽取集完全相同**（见诚实说明 1，不得谎称 150/150） | `p8-extract.json/.log`、`p8-extract-core.json/.log` |
| p8 compare | `tools/p8.py compare`（读本体） | **CLEAN**，missing=[]，extra_count=0，keydiff=**[137, 138, 139, 140, 150]**（预期内：4 个读者语翻译键 + 写作键） | `p8-compare.json/.log` |
| freeze baseline（版内 + 真核心） | `tools/freeze.py baseline --build 2026-w47-en-ja --core-svg 2026-w47-en-ja/svg`（版内 baseline）+ `--build core-en --core-svg core-en/svg`（核心只读对照） | **版 baseline 8/8**（重建 8 页与已发版逐文件 SHA 一致，独立 `sha256sum -c` 全 OK；p5 重建哈希 `cacd38b4…` = 修前哈希，p8 `b86fb714…` = 修后已发哈希）+ **核心对照 8/8**（direct sha256 重渲染 vs 盘上核心 SVG 8/8 MATCH；核心完整性未变） | `freeze-base-edition.log`、`freeze-base-edition/`、`freeze-base.log`、`freeze-base/`、`freeze-direct.log` |
| freeze diff | `tools/freeze.py diff --core-svg core-en/svg --edition-svg svg` | rc=0，新增 CJK 总计 **2,084**（逐页 182/273/159/168/145/156/435/566，与 proof1 完全一致） | `freeze-diff.json/.log` |
| 印/网文字层 | `pdftotext` 两版 + 词多重集 + 逐页字节比对 | **43,472 字符各**（修前 43,475，−3 = speak→up）；词多重集差 **0**；逐页字节一致 **8/8** | `printweb.log` |
| check_s11 | `check_s11.py ja` | **ALL §1.1/P8 CHECKS PASS**；P8 最小字号 13.5 | `check_s11.log` |
| keycheck | `keycheck_ed.py ja`（fanout 版拷入，仅改 SCRATCH 路径） | **registry vs P8 抽取 149/150 exact**，唯一不符 Q150 = 已知抽取截断 + 页脚泄漏（见诚实说明 2）；registry vs core 145/150，diff 仅 5 个读者语键 137–140、150（预期）；Q38–41 = b/a/d/c；noted set == core | `keycheck.log`、`keycheck_ed.py` |
| text.md 答案 150 | 答案行正则抽取 vs registry 逐项比对 | **150/150，0 差异**；Q73 = up | `answers-150.log`、`answers150.py` |
| P8 最小 PDF 字号 | fitz 逐 span（印 + 网） | **10.12 pt**（两版一致，≥ 10 pt 下限） | `p8font.log`、`p8font.py` |
| creambox 全版扫 | `creambox.py`（+45 px 窗口版） | 32 行 clearance 记录；全部负值均为盒下节头伪影（−35.5/−36/−37，与 proof1/core-en 同值） | `creambox.log` |
| creambox inside-only | `creambox_inside.py`（仅计盒内基线） | **0 真溢出**；每页最差 P1 +12.0、P2 +5.0、P3–P7 +47.7、P8 +92.4（与 proof1 逐页一致；P2 desc-clear −1.0 为假名行 heuristic 伪报，同 proof1） | `creambox-inside.log` |
| boxtitle 宽度（源） | `sweep_titles.py ja` | **12/12 全过**；最紧 THE WEEK IN NUMBERS +1.5 | `boxtitle.log` |
| boxtitle 宽度（SVG） | `sweep_svg_titles.py ja` | **18/18 全过，0 溢出** | `boxtitle-svg.log` |
| 填空/改写键适配抽查 | AST 抽取全部 `___`/`→` 题（53 项）逐项审键填空合理性 + 与 registry 1:1 映射 | **53/53 键合理**（含 Q73 "Speak up"）；映射 1:1 53 项，unmapped/multi 均为 0；Q6/Q12 同题干同键为既有复用（P1 试做 + P2 正文），两处一致 | `fill-rewrite.log`、`fill-rewrite-map.log`、`fill_rewrite.py`、`fill_rewrite_map.py` |
| D5 字体（只记录，不判） | SVG font-family 统计 | 5 种：Newsreader 1037、Noto Sans CJK JP 633、Noto Serif CJK JP 55、DejaVu Sans 4、UnifrakturMaguntia 1（与 proof1 计数完全一致） | （见本行） |
| 目视 | 印刷卡片 p1–p8 全 8 页（render.py 产出，1950 px） | **全部看过，干净**；P5 Q73 题干在位、D 节单行说明、ODD SOCKS 标题在盒内；P8 答案区 `73. up` 目视确认；其余 6 页与 proof1 描述一致，无新异常 | `cards/p1-front.png` … `cards/p8-test.png`（版目录内） |

## 诚实说明

1. **p8 extract 不是 150/150**：工具对本版返回 **60/150 noted**（P8 版式下仅 60 个键带印刷注记），
   与 proof1 相同。有意义的门是抽取集与 core-en 完全相同 + compare CLEAN——该门通过。不得谎称 150/150。
2. **keycheck 149/150 唯一不符 Q150**：抽取截断 + p8.py FOOTER_RE 已知 bug（混合大小写页脚漏进第 150 键），
   与 proof1 相同，非版面缺陷。本轮 keycheck_ed.py 的 rc=0（脚本本身不以 mismatch 退出），结果与 proof1 一致。
3. **P5 SVG 字节未变是正确且预期的**（简报更正 2026-11-11）：Q73 的键只出现在 P8 答案页，
   不出现在 P5 题干页（P5 只印 `Speak ___` 空白 + `speak up` 注记，键本身从不上 P5），
   因此只有 p8 变化、p5 与修前字节一致。en-es delta 已证实此点（p8 含 `73. up`，p5 不变）。
   本版亦然，且版内 baseline 重建的 p5 哈希（`cacd38b4…`）与修前哈希相同——p5 不变且可重现，
   不是异常，无需返工。
4. **首轮 SVG diff 循环误报**：第一次用 shell 循环比对时 8 页全报 DIFF，是该循环的取值 bug；
   已废弃，改用逐字节前缀/后缀定位脚本（`svg_byte_diff2.py`）两次实测（run.py 后、dump_reg 重跑后）
   均确认 P1–P7 字节一致、P8 仅 3 字节差异。另有一次多 heredoc 批量命令被中止未执行，
   已改写成脚本文件逐个重跑，全部命令均有日志在案。
5. **网 PDF SHA 必然不同**：`fb903b2b…` vs 修前 `25645767…`，符合铁律（fontTools 子集改写
   head.modified 为墙钟 + cairo 写 CreationDate）；内容以文字层为准（与印版逐页字节一致 8/8）。
6. **cards/ PNG 由 render.py 全部重写**：P1–P7 的 SVG 与修前字节一致，故对应卡片内容亦一致；
   未单独备份旧卡片做像素比对（SVG 字节一致是更强的证据）。
7. **未做**：未改核心、其他版、tools/；未动 ABSTRACT.txt / KIT 以外文件；未 commit、未 push。

## 结论

delta 完成：唯一改动 Q73 speak→up 已在 registry、text.md、P8 印刷键、P5 题干四源一致；
全部门禁绿灯；8 页目视干净；**可进 proof2**。
