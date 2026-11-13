# FIX-LOG — W47 core-zh-tw fix5：只修 D4（P4「你呢？」框末行溢出）

- **任务**：core-zh-tw fix5（只修 D4 一处；re-proof #3 另派，本次不做全量复校）
- **修复对象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（仅核心，不碰其他家庭、tools/、issues/）
- **缺陷**：D4（re-proof #2，`scratch-reproof-core-zh-tw2/PROOF-NOTE.md` §6）：P4 第 4 欄「你呢？ Over to you」奶油框末行 `exercise?` 溢出框底 4.4px
- **时间**：2026-11-11 10:11–10:21 UTC（05:11–05:21 EST）
- **日志目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-zh-tw5/`
- **先读**：re-proof #2 `PROOF-NOTE.md`（D4 一节，§6）与 `GATE-LOG.md`（门禁方法照此复现）；SOP §1.1、§8；fix4 `FIX-LOG.md`（构建命令与门禁方法）
- **未改**：不 commit、不 push、不跑 insert.py / lint --write

## §0 探针与基线（开工前实测）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`：rc=0（`9daeafb9…`）。探针写盘 scratch 真实文件成功；全程 `TMPDIR=<scratch>/tmp`，未写 /tmp；无 `Disk quota exceeded`。
- **基线三件 SHA 与任务值逐字一致**（动工前实测）：印刷 19,420,551 B / `97e896947fba550a0e4dd496e093a2cbafef88ed5cd0398052a3508aa77f11b0`；网页 2,324,051 B / `121cba14278ef1af117eff324b4ac9c2ec6837e0564186c3d91bd98148cd8d62`；text.md 49,798 B / `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`（fix4 落地态，与 KIT 登记一致）。
- 动手前已存修前 SVG 哈希（`svg-hashes-before.txt`，与 re-proof #2 登记的 fix4 交付哈希逐字一致：p4 `182d9301…`）、修前 text.md（`text-md-before.md`）、修前源文件副本（`content34-before.py`）于本目录。

## §1 唯一改动（diff 仅一行，文案一字不动）

`content34.py:210`（P4 第 4 欄「你呢？」框）：

```diff
- p.rect(rx, by + 488, CW, 230, fill=BOX)
+ p.rect(rx, by + 488, CW, 244, fill=BOX)
```

- 几何核对（改前实测，与 PROOF-NOTE §6 一致）：框 y=1128（by=640，`208+300+132`；`by+488`）、h=230、底 1358.0；末行 `<text x="1461.5" y="1362.2">exercise?</text>` 基线 1362.2、墨底 1362.4，溢出 4.4px。
- 改后：框底 1128+244=**1372.0**，末行墨底 1362.4 在框内，底距 **+9.6px**（见 §4 creambox 实测）。
- **框下冲突核对**：P4 第 4 欄该框之后无任何元素——源代码随后即 `p.foot(4)` + `p.save(...)`；SVG 实测：x≥1439.5、top 在 (1372, 2500) 区间内的元素 **0 个**（`perpage-text.log`）；页脚线 y=2596，距新框底 1224px。框下延 14px 零冲突。
- P3 同型框（`content34.py:85`，h=250）未动；其余任何文件、任何文字不动。

## §2 重建（工具 venv，日誌見本目錄）

- `run.py` RC=0（build.log；TOTAL 150，A2 44 / B1 74 / B2 32，分頁 10/18/18/18/18/18/12/38，与修前一致；0 FLOW OVERFLOW / 0 HEAD TOO WIDE）。
- `render.py` RC=0（render.log）；`tools/webpdf.py svg Lucerna-VOL4-web.pdf` RC=0（webpdf.log，8 頁，46,212 text bytes）；`export_zhtw_textmd.py svg 2026-w47-zh-tw-en.text.md "Lucerna Weekly — Traditional Chinese, English explanations"` RC=0（export.log，寫出 33,114 字符，与 fix4 相同）。
- **仅 p4-sport.svg 变化**（`svg-hashes-before.txt` vs `svg-hashes-after-run.txt` diff 仅此一行：p4 `182d9301…`→`ec781f9c…`，其余 7 页与 fix4 逐字节相同——本次修复只动 P4，无其他页回归）。
- 印刷 PDF 确定性验证：`render.py` 再跑一次（render2.log），印刷 SHA 仍为 `5ec35fe2…70d9a`，两跑相同；网页 PDF 未重跑（webpdf 每次 SHA 不同为已知特性，KIT 以本次交付文件为准）。

## §3 交付物（新双 PDF + text.md，以本次重建实测 SHA 为准）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 `Lucerna-VOL4.pdf` | 19,420,552 B | `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a` |
| 网页 `Lucerna-VOL4-web.pdf` | 2,324,042 B（< 7 MB） | `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240` |
| `2026-w47-zh-tw-en.text.md` | 49,798 B | `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` |

- 双 PDF 各 8 页、1462.5×2025 pt。
- **text.md 与 fix4 逐字节相同**（字节数与 SHA 皆不变：49,798 B / `09e083e1…`）——D4 只改框高，零文字变动；`text-md-before.md` 与新文件 `sha256sum` 一致。印刷 PDF 仅 +1 B（框高属性 `230`→`244` 的渲染差）。
- 修前基线（fix4）：print 19,420,551 B / `97e89694…77f11b0`；web 2,324,051 B / `121cba14…8d62`；text.md 49,798 B / `09e083e1…02f02b`。
- **KIT 已更新**：`WEEKLY-KIT.md` 仅三处——L53（双 PDF 字節數/SHA 改为本次交付值，标 fix5，括号内补记 fix4 旧值）、L129（text.md 标 fix5，注明与 fix4 逐字节相同）、Build history 末尾新增 fix5 条目（`WEEKLY-KIT-before.md` 存本目录，diff 仅此 5 行）。

## §4 门禁（全绿，逐门结果；日志文件见本目录）

| 门 | 结果 |
|---|---|
| creambox.py 全版扫描（36 盒，PIL 墨水实测） | **PASS：STRADDLE 0，CREAM-COVER 0**。D4 盒 `[1439.5, 1128.0, 1862.0, 1372.0]` 底距 **+9.6px**（修前末行墨底 1362.4 溢出框底 1358.0 达 −4.4px，清除量 **+14.0px ≥ 要求的 +5px**；左 22.0 / 右 28.0 / 上 22.5）。其余各页最小底距与 re-proof #2 的 creambox.json 逐值一致：P1 16.5、P2 37.1、P3 14.1、P5 4.4、P6 17.1、P7 7.7；P4 其余三盒（43.8 / 63.5 / 39.6）亦与修前逐值一致——无连带变化。（注：re-proof #2 GATE-LOG 写的「P4 17.1px」是 D4 盒内最后一行*未溢出*文字的底距，因溢出的 `exercise?` 不在 inner 集合内；本次 +9.6px 是末行墨底到新框底的真实距离。）`creambox.log` / `creambox.json` |
| occlusion_audit.py（正式审计，未加 --selftest） | **PASS：0 flags**（`occlusion.log`；工具内置自檢亦过，6 类皆触发、干净对照沉默） |
| p8.py extract --total 150 | **PASS：noted set = 150/150**（`p8-extract.log`） |
| p8.py compare（本核心 vs zh-tw-de） | **PASS：CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]（`p8-compare.log`） |
| freeze.py baseline（副本重建进 scratch） | **PASS：8/8 SVGs byte-identical**，core integrity 8 文件重哈希不变（`freeze-base.log` / `freeze-base/`） |
| freeze_direct（交付 SVG SHA vs fix4 交付哈希） | **PASS：仅 p4 变化**（`182d9301…`→`ec781f9c…`），其余 7 页逐字节相同（`svg-hashes-delivered.txt` vs re-proof #2 `svg-hashes-delivered.txt`） |
| keycheck（150 题逐题语义核对） | **PASS（继承 + 机械核验）**：text.md 与 fix4 逐字节相同，re-proof #2 的 150 题全量语义核对结论继续有效；p8 compare CLEAN 佐证键集合无变；Q34 键 `34. C — A Trip to the Moon was made in 1902.` 仍在 text.md L5772 同文。 |
| 印/网文字层逐页比对（PyMuPDF，逐页字符多重集） | **PASS：8/8 页 print-only=0、web-only=0**（`perpage-text.log`：P1 2228 / P2 2685 / P3 3128 / P4 2344 / P5 3165 / P6 2351 / P7 3596 / P8 8982 字符，双版逐页相等）。-layout 模式 print/web 各 101,461 B。`print.txt` / `web.txt` / `analysis.log` |
| boxtitle 全标题 text_w 实测 | **PASS：36 框标题／行右缘逾越 0**；最小标题右边距 26.2px（P2）、最小左邊距 18.0px；各页最小右边距 P1 61.8、P2 26.2、P3 47.5、P4 60.8、P5 47.8、P6 39.5、P7 107.2（`boxtitle.log` / `boxtitle.json`） |
| §1.1（PyMuPDF，`analysis.log`） | **PASS**：刊头 UnifrakturMaguntia（CairoFont-2-0 子集）147pt；拉丁 Newsreader；中文 Noto Serif CJK TC（标题/正文）／Noto Sans CJK TC（讲解层）。字号阶梯：头条 45pt、刊別 27pt、栏目条 34.5pt、次级标题 24pt、正文 18pt、练习题干 16.5–16.88pt、栏目小字 12.75pt、讲解层 11.25–13.5pt——皆在阶梯内。P8 最小字号双 PDF **9.75pt**（= §1.1 下限）；P8 最大 34.5pt。纸色 #fbfaf6（本脚本计数 `pages=0/8` 与 re-proof #2 `analysis.log` 完全相同，属同一脚本口径；re-proof #2 已用 get_drawings 实测 8/8 全幅填充）。金色系 fill（#b8860b/#d4af37/#c9a227/#8b4513/#a52a2a）**0**；"gold" 子串 9 处皆为英文 "Golden" 或字体子集随机 ID。P8 题干 10.35pt 为 KIT 已披露的预披露偏差，不计缺陷。`analysis.log` 与 re-proof #2 的 diff 仅一行：P4 奶油框 230.0→244.0。 |
| checks.py | **PASS**：本周金句 8 句各 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]（`checks.log`） |
| 54/54 填空键重验（check_fillin_keys.py） | **PASS：54/54，缺失 []**（`fillin-check.log`） |
| 弯撇／弯引号全扫（U+2018/U+2019/U+201C/U+201D） | **PASS：0 命中**（源 .py、8 个 SVG、text.md；`analysis.log`）。`松菸` text.md 5 处（皆 U+83F8 菸），`松煙` 0。 |
| 目视（P4 卡片裁切 `p4-d4-crop.png`，原尺寸裁切 2× 放大） | **PASS**：`exercise?` 一行完整在奶油框内，框底下方有明显余量；上方「遊行小檔」框无变化。 |

## §5 回归（D1/D2/D3，本次重建实测）

| 项 | 源 | text.md | SVG | 双 PDF 文字层（print / web） |
|---|---|---|---|---|
| D1 本週日 | 11 | 11（正文 11，keys 0） | 11 | 各 **11** |
| D1 下週日 | 0 | 0 | 0 | 各 **0** |
| D2 BABYMONSTER | 0 | 0 | 0 | 各 **0** |
| D3 取捨 | 2（文章 + 题目） | 2（正文 1 + keys 1） | 2 | 各 **2** |

- fix4 三句亦无回归：`小雪` 36、`夜間遊行` 25、`finish line` 0、`end point` 1（双 PDF 文字层与 text.md 一致）。
- 写作范文 142 字符（去标点后 126），落在 120–180 字带内。

## §6 未做事项与注意事项

- 未 commit、未 push，未跑 insert.py / lint --write（任务红线）。
- 本次为修复 + 门禁，不做独立全量复校：按 SOP §8.4，修后 re-proof #3 另派。
- 仓库 `git status` 显示 `issues/2026-w43/` 下多文件已修改——为其他并行 agent 的工作，非本次改动；`production/2026-w47/` 整体仍为未追踪（`??`），本次未改任何已追踪文件。
- 一次操作失误记录：逐页文字层核查后的一条 `grep -n 'y="1362"' svg/p4-sport.svg` 把整行 base64 SVG 打进了一次 exec 输出（文件本身未受影响；结果以 `perpage-text.log` 为准）。此后 grep SVG 一律用 `-o`。
