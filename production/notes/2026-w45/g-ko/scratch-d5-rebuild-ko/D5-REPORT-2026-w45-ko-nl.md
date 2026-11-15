# D5 重建报告 — 2026-w45-ko-nl（荷兰语读者版）

W45 ko 家 D5 + §1.1 合并重建（旧样式家族：D5 字体修复——讲解层拉丁字符由 Noto Sans CJK 改走 Newsreader；西里尔字符改走 Noto Sans）。施工 2026-11-14（builder v2；v1 于 21:50 UTC 被 runtime restart 杀死未出报告，v2 续用同一 scratch 完成）；**不 commit、不 push、不重校（另派他人）**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-nl-run2/`（`GATES-SUMMARY.txt` 为门禁总表，复本见本目录 `logs/2026-w45-ko-nl/GATES-SUMMARY.txt`）；家族报告：`hidden_files/d5-redo/FAMILY-W45-KO-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样复制为 `production/2026-w45/core-ko/svglib.py`——`apply_variant.py --patch-core ko` 按预期被拒（旧式 core svglib，无 `_char_font`）；`_D5_READER = "latin"`（L122）；`git diff --stat`：1 file，+333/−40。模板与 W47 `core-ko/svglib.py` diff 仅 `_D5_READER` 一行。
- 本版安装：移植模板原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`（`install-ko.sh`；未对模板跑 `apply_variant.py`——对 ja 读者它会错把 KR 下标改 JP，下标跟目标语（韩文）走，不跟读者走）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。fix2（U+201C/U+201D/U+2019 → serif）保留：`_QUOTE_CLS` 逐版核对在位；普查弯引号在 CJK 为 0（见 §四门 3）。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次跑，不可跳步；首渲前暖 fontconfig `fc-cache -f`）；text.md 由 `hidden_files/style-port-ko/textmd_ko.py`（AST 源码手稿路线，从 content*.py 字面量导出，绝不从 PDF/SVG 反提）导出，交付件为新建的 `.text.md`（W45 ko 11 版 issues 目录原无 `.text.md`，见 §五）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，警告 0。
- 印 PDF：基线重建 32,519,521 B、sha256 `19853e49eb917b124707c130b91f656ea92a1f9ff168556bc3725efe5dadbc24`；与 fanout 印 PDF **BYTE-IDENTICAL**。网 PDF（基线，`tools/webpdf.py`）2,266,377 B，与 `issues/2026-w45/2026-w45-ko-nl/` 已发网 PDF 文字层多重集差为分隔符类已知差（全家口径：印=网差 0 + 网-vs-issues 差 == fanout-vs-issues 差，零词字符丢失，见家族报告 §2）。
- 修前普查 `d5_census.py`：D5 拉丁 444、西里尔 0、弯引号在 CJK 0（>0 拉丁/西里尔，符合装机前提；ru 版西里尔 253 为俄语讲解层本身）。
- 基线 freeze（D2：freeze 门跟随该版实际构建解释器，D5 重建版用 venv）：门 9 已验 8/8（见 §四）。

## 三、缺陷与修复

- run1 门禁 17 PASS + 2 FAIL：门 6（LINEX，已修）、门 11（溢出残留，见 §三）。D18/D37 在修正量测脚本后复测均 PASS。run2 门禁 18 PASS + 1 FAIL。
- 修复：1 项（run1 → run2）：`patched/2026-w45-ko-nl/content7.py` P7 诊所盒高 `eh` 减 26.52px（一行 `r[2]` 行距；`# D5 fix run1` 注释已加）。Newsreader 下诊所第 2 项荷兰译文多绕一行（基线 Noto Sans CJK 下 1 行），`eh` 随之 +26.52，整列下移把 P7 预告带推上页脚线（门 6 LINEX，D5 引入）。盒内末行距盒底仍有 14.0px 余量，修后盒高 778.84 = 基线值，预告带底缘 2602.34 = 基线位置，门 6 **PASS**（基线同条件 0 flags）。文字内容未动。
- 残留：门 11 残留（真缺陷，未修，提请协调员裁定）：P7 读者来信盒最后一行 'op!' 溢出盒底 +13.50px——基线同值同行同量（已发版即有，D5 未引入也未加重；见家族报告 §5/§7）。另：基线 P7 预告带底缘已越过页脚线 6.3px（2602.34 vs 2596），D5 前即有，run2 修后恢复基线位置，不扩大。【F1 fix 已修好门 11 残留，见 §七；F2 fix2 已把预告带底缘修回 2602.34 基线态，见 §八；§四/§五已更新为 fix2 值。】门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）。
- R1（导出器待定项，不修只记录）：text.md 漏收已渲染的短拉丁串 'A2→B2'（P1 内容表 p7 级别格）、'D-17 ~ D-12'（P6 对照表）、'IPDONG'（P1 主图题注）、'Alle'（P1 内容表 p8 级别格）（导出器 is_prose 规则；本轮不修，见家族报告 §7）。
- P8：行数见 §四门 14（基线→重建）；p8 compare CLEAN（keydiff [137, 138]）；余量仍为正，无溢出，不处理。

## 四、门禁（run2 + F1 fix + F2 fix2，PASS=19 PASS + 0 FAIL）

- run TOTAL 150、警告 0；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（2,173,992 B <7MB）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff：新增 CJK 字符 TOTAL 0、新增拉丁 strings TOTAL 260（run 拆分计数，非新增内容）；spill 0 SPILL（F1 fix 后、F2 fix2 后仍 0 SPILL，见 §七/§八）；boxtitle 0 DEFECT（73 titles、993 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（P8 行数 214→216，距页脚线余量 61.0px）；文字层 print=web 多重集差 0（印/网各 31872 字符）；census_quotes 0 defective；D18 刊头间距 GAP=374.2（>0，无缺陷）；D37 副刊头余量 12.9（y=394 行）（>0，无缺陷）。
- 门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）：如 'dagelijks'、'leven'；门 15 验收以 15a（print=web 差 0）+ 原生校验器 `verify_textexp_ko.py --edition`（ADOPT，0 UNEXPECTED，P8 tokens 935）+ 全文通读为准。
- 日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-nl-run2/GATES-SUMMARY.txt`；F1 fix 日志：`hidden_files/d5-redo/scratch-2026-w45-ko/fix/logs/2026-w45-ko-nl-fix/GATES-SUMMARY.txt`；F2 fix2 日志：`hidden_files/d5-redo/scratch-2026-w45-ko/fix2/logs/2026-w45-ko-nl-fix2/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `Lucerna-VOL2-NL.pdf` `74793648bc7f1dae25e363e7023415c263aee92f3cfa7e6494eea680682760d5`（30,612,744 B；F2 fix2 值，F1 fix 值已过期）；旧（基线）印 PDF `19853e49eb917b124707c130b91f656ea92a1f9ff168556bc3725efe5dadbc24`（32,519,521 B）。印 PDF 缩小系字体子集变化（拉丁/西里尔移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF（render）`Lucerna-VOL2-NL-web.pdf` `6178d2f96b96a85a6a3c22daccc87088edb40b1717044472f9c77cc7b4d90a25`（2,173,987 B，<7MB；F2 fix2 值，F1 fix 值已过期）；builder 网 PDF `2026-w45-ko-nl.web.pdf` `86d642e92d255adecaf46356b19a9724c83378c3f1ea4c9f08b627dd89499959`（2,173,992 B；F2 fix2 值，F1 fix 值已过期）——待 closer 拷原件换入 `issues/2026-w45/2026-w45-ko-nl/` 并更新 pin（已发版 pin 以 issues/ `.md` 现值为准），绝不重跑 webpdf。
- text.md：新建 `2026-w45-ko-nl.text.md` `7b2e70c956acef1f98db8ae231e11de1a7d36d81d809fe72d3f1f5cdd441fc2a`（28,038 B），与 fanout `.text.md.new` **BYTE-IDENTICAL**；验收 `verify_textexp_ko.py --edition` 判 **ADOPT**（0 UNEXPECTED）。D5 不改文字内容。
- KIT：`production/2026-w45/2026-w45-ko-nl/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 D5 节；patched 侧复本逐字节一致）。

## 七、F1 fix（2026-11-14，P7 读者来信盒溢出修复，D39 裁定）

- 修法：盒高修法。`content7.py:96` `lh` 末常数 +36→+56（+20px）。盒底 1948.34→1968.34，末行基线 1961.84，余量 6.5px；预告带底缘 2602.34→2622.34，预告带正文 y=2588.34，距页脚线 2596 余量 7.7px，不压线（G6 PASS）。注意：预告带底缘本身越过页脚线 26.3px——基线即已越过 6.3px（带底缘盖线但带内正文不压线，门 6 不报），本次 +20px 使越线量加大，属先存形态的延续，非新增门禁项；页脚文字基线 2624 在带底 2622.34 之下，不受影响。文案零改动。
- 基线核实（fix 前实测）：patched 与基线同值同行同量——溢出 +13.50px（末行见 §三）；基线 spill_sweep 亦为 1 SPILL 同行同量（zh-cn/de/nl/pt 基线候选数 278/285/280/281，patched 408/418/413/425，候选数差仅为 D5 run 拆分）。D5 未引入也未加重。
- 门禁（fix 轮，全量重跑，17 门 + D18 + D37）：**19 PASS + 0 FAIL**（15b 仅记录）。G11 0 SPILL；G6 0 flags；G15a print=web 差 0 + text.md BYTE-IDENTICAL（与 builder 终轮逐字节一致，文案零改动）。P8 行数 214→216 / 余量 61.0px（与 builder run2 同值）；D18 gap 374.2、D37 binding 12.9（同值）。门 12 boxtitle 计数 992→993（P7 盒高变化所致 run 计数，0 DEFECT）。
- 新交付物（fix 原件，`fix/2026-w45-ko-nl/`；§五已更新为 fix 值）：印 PDF / render 网 PDF / builder 网 PDF（closer 拷原件，绝不重跑 webpdf）/ text.md（与 builder 终轮逐字节一致）。
- 目检：P7 来信盒底裁切（`fix/work/pages/nl-p7-fix-crop.png`）末行完整入框，盒底缘在其下可见。
- 同步：`content7.py` 三方一致（production == patched/ == fix/）；KIT 两处复本逐字节一致（含末尾 F1 fix 节）；本目录 `logs/2026-w45-ko-nl/GATES-SUMMARY.txt` 已替换为 fix 门禁表（三方 `cmp` 一致，D29）；builder run2 表归档于 `fix/logs/run2-summaries/GATES-SUMMARY-nl-builder.txt`。
- 待独立重校 v1（不同工人）：复核修法、重渲、门禁、P7 目检、§6 三方一致。

## 八、F2 fix2（2026-11-15，nl 预告带 F-NL-TEASER 修复，重校 v1 finding）

- 来源：重校 v1 唯一 finding F-NL-TEASER（家族重校报告 §3；协调员已亲自目检证据条 `reproof/logs/nl-p7-footerstrip-reproof.png` 确认属实）。fix 的 lh +20 把预告带底缘从基线 2602.34 推到 2622.34，越页脚线 26.34px，距页脚文字基线仅 1.66px，覆盖约 85% 字高（9.73/11.39px），对比度 1.95:1（白底 5.56:1），页脚文字上半压在深绿带 `#37402f` 上、肉眼难辨。D39(4) 只接受了基线越线（nl −6.3px），fix 报告"属 D39 已裁定的接受项"的说法不准确；G6 PASS 不能作证（页脚文字画在带之上，G6 对此盲区）。
- 修法：带高修法，不改文案。`content7.py:131` `p.rect(MX, py, RIGHT - MX, 118, ...)` → **98**（`# D5 fix2 F-NL-TEASER` 注释已加）；`:134` print `py + 118` → `py + 98`（保持 print 真实）。带底缘 2622.34→**2602.34**（= 基线态，D39(4) 已接受）；lh +20（F1）保持，盒底 1968.34、末行 'op!' 基线 1961.84、余量 6.50px 不变；预告带正文基线 y=2548.34/2588.34 均在带内。
- 门禁（fix2 轮，全量重跑，17 门 + D18 + D37）：**19 PASS + 0 FAIL**（15b 仅记录）。G11 0 SPILL；G6 0 flags；G15a print=web 差 0 + text.md BYTE-IDENTICAL（与 fix 轮逐字节一致，文案零改动）。P8 行数 214→216 / 余量 61.0px（与 fix 轮同值）；D18 gap 374.2、D37 binding 12.9（同值）。门 12 boxtitle 计数 993（与 fix 轮同值，0 DEFECT）。
- 新交付物（fix2 原件，`fix2/2026-w45-ko-nl/`；§五已更新为 fix2 值）：印 PDF 30,612,744 B，sha256 `74793648bc7f1dae25e363e7023415c263aee92f3cfa7e6494eea680682760d5`（F1 fix 值 `66a2b30e…` 30,612,743 B 已过期）；render 网 PDF 2,173,987 B，sha256 `6178d2f96b96a85a6a3c22daccc87088edb40b1717044472f9c77cc7b4d90a25`（F1 fix 值 `9665aed2…` 2,173,980 B 已过期）；builder 网 PDF 2,173,992 B，sha256 `86d642e92d255adecaf46356b19a9724c83378c3f1ea4c9f08b627dd89499959`（F1 fix 值 `392d71d9…` 2,173,980 B 已过期；closer 拷原件，绝不重跑 webpdf）；text.md 28,038 B，sha256 `7b2e70c956acef1f98db8ae231e11de1a7d36d81d809fe72d3f1f5cdd441fc2a`（与 fix 轮逐字节一致）。
- 目检：P7 页脚条（`fix2/logs/2026-w45-ko-nl-fix2/nl-p7-footerstrip-fix2.png`，y 2560–2660，同重校 v1 证据条口径）页脚文字全在白底、清晰可读；预告带裁切（`fix2/logs/2026-w45-ko-nl-fix2/nl-p7-teaser-fix2.png`）标题与正文完整在带内。探针实测（`fix2/logs/2026-w45-ko-nl-fix2/probe-p7.log`）：带 rect y=2504.34 h=98.0，底缘 2602.34；页脚线 y=2596.0，页脚文字基线 y=2624，字形顶缘 ~2612.61，净空约 10.3px 全白底；盒底余量 +6.50px 不变。
- 同步：`content7.py` 三方一致（production == patched/ == fix2/）；KIT 三处复本逐字节一致（含末尾 F2 fix2 节）；本目录 `logs/2026-w45-ko-nl/GATES-SUMMARY.txt` 已替换为 fix2 门禁表（三方 `cmp` 一致，D29）；fix 表归档于 `fix/logs/2026-w45-ko-nl-fix/GATES-SUMMARY.txt`。
- 待独立重校 v2（不同工人）：复核修法、重渲、门禁、P7 页脚目检、三方一致；改判后全家方可 PASS。
