# D5 重建报告 — 2026-w45-ko-de（德语读者版）

W45 ko 家 D5 + §1.1 合并重建（旧样式家族：D5 字体修复——讲解层拉丁字符由 Noto Sans CJK 改走 Newsreader；西里尔字符改走 Noto Sans）。施工 2026-11-14（builder v2；v1 于 21:50 UTC 被 runtime restart 杀死未出报告，v2 续用同一 scratch 完成）；**不 commit、不 push、不重校（另派他人）**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-de-run1/`（`GATES-SUMMARY.txt` 为门禁总表，复本见本目录 `logs/2026-w45-ko-de/GATES-SUMMARY.txt`）；家族报告：`hidden_files/d5-redo/FAMILY-W45-KO-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样复制为 `production/2026-w45/core-ko/svglib.py`——`apply_variant.py --patch-core ko` 按预期被拒（旧式 core svglib，无 `_char_font`）；`_D5_READER = "latin"`（L122）；`git diff --stat`：1 file，+333/−40。模板与 W47 `core-ko/svglib.py` diff 仅 `_D5_READER` 一行。
- 本版安装：移植模板原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`（`install-ko.sh`；未对模板跑 `apply_variant.py`——对 ja 读者它会错把 KR 下标改 JP，下标跟目标语（韩文）走，不跟读者走）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。fix2（U+201C/U+201D/U+2019 → serif）保留：`_QUOTE_CLS` 逐版核对在位；普查弯引号在 CJK 为 0（见 §四门 3）。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次跑，不可跳步；首渲前暖 fontconfig `fc-cache -f`）；text.md 由 `hidden_files/style-port-ko/textmd_ko.py`（AST 源码手稿路线，从 content*.py 字面量导出，绝不从 PDF/SVG 反提）导出，交付件为新建的 `.text.md`（W45 ko 11 版 issues 目录原无 `.text.md`，见 §五）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，警告 0。
- 印 PDF：基线重建 32,734,379 B、sha256 `c011252a43629786f88e016033581945d5b2f77aa19d6c8767214aca2837398b`；与 fanout 印 PDF **BYTE-IDENTICAL**。网 PDF（基线，`tools/webpdf.py`）2,280,937 B，与 `issues/2026-w45/2026-w45-ko-de/` 已发网 PDF 文字层多重集差为分隔符类已知差（全家口径：印=网差 0 + 网-vs-issues 差 == fanout-vs-issues 差，零词字符丢失，见家族报告 §2）。
- 修前普查 `d5_census.py`：D5 拉丁 426、西里尔 0、弯引号在 CJK 0（>0 拉丁/西里尔，符合装机前提；ru 版西里尔 253 为俄语讲解层本身）。
- 基线 freeze（D2：freeze 门跟随该版实际构建解释器，D5 重建版用 venv）：门 9 已验 8/8（见 §四）。

## 三、缺陷与修复

- run1 门禁 18 PASS + 1 FAIL，唯一 FAIL 为门 11（见 §三）。
- 修复：无（run1 无需改源）。
- 残留：门 11 残留（真缺陷，未修，提请协调员裁定）：P7 读者来信盒最后一行 'Ihren besten Text von Seite 8!' 溢出盒底 +26.50px——基线同值同行同量（已发版即有，D5 未引入也未加重；目检确认该行落在奶油盒外白地上，见家族报告 §5/§7）。盒高修复本身可行（P7 预告带余量 84.2px），但与 zh-cn/nl/pt 同类同因，留待协调员统一定夺是否修、怎么修。【F1 fix 已修好本项，见 §七；§四/§五已更新为 fix 值。】门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）。
- R1（导出器待定项，不修只记录）：text.md 漏收已渲染的短拉丁串 'A2→B2'（P1 内容表 p7 级别格）、'D-17 ~ D-12'（P6 对照表）、'IPDONG'（P1 主图题注）、'Alle'（P1 内容表 p8 级别格）（导出器 is_prose 规则；本轮不修，见家族报告 §7）。
- P8：行数见 §四门 14（基线→重建）；p8 compare CLEAN（keydiff [137, 138]）；余量仍为正，无溢出，不处理。

## 四、门禁（run1 + F1 fix，PASS=19 PASS + 0 FAIL）

- run TOTAL 150、警告 0；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（2,176,439 B <7MB）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff：新增 CJK 字符 TOTAL 0、新增拉丁 strings TOTAL 267（run 拆分计数，非新增内容）；spill 0 SPILL（F1 fix 后，见 §七）；boxtitle 0 DEFECT（73 titles、961 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（P8 行数 232→234，距页脚线余量 47.9px）；文字层 print=web 多重集差 0（印/网各 31552 字符）；census_quotes 0 defective；D18 刊头间距 GAP=276.7（>0，无缺陷）；D37 副刊头余量 46.8（y=394 行）（>0，无缺陷）。
- 门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）：如 'du'、'den'；门 15 验收以 15a（print=web 差 0）+ 原生校验器 `verify_textexp_ko.py --edition`（ADOPT，0 UNEXPECTED，P8 tokens 933）+ 全文通读为准。
- 日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-de-run1/GATES-SUMMARY.txt`；F1 fix 日志：`hidden_files/d5-redo/scratch-2026-w45-ko/fix/logs/2026-w45-ko-de-fix/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `Lucerna-VOL2-DE.pdf` `c9fbb78b82e6f5d63384865013107b4ef4449918f5804697536dd79a706bfb17`（30,615,632 B；F1 fix 值，D5 值已过期）；旧（基线）印 PDF `c011252a43629786f88e016033581945d5b2f77aa19d6c8767214aca2837398b`（32,734,379 B）。印 PDF 缩小系字体子集变化（拉丁/西里尔移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF（render）`Lucerna-VOL2-DE-web.pdf` `2da707260c4749e554ac09a2d10fcfdc2488817be7fb4631d23903becafaa7f0`（2,176,437 B，<7MB；F1 fix 值，D5 值已过期）；builder 网 PDF `2026-w45-ko-de.web.pdf` `5874cd38c5f1e4f40d05b3aa7523dc87edf3a2af03d45e3354233b99e06123bf`（2,176,439 B；F1 fix 值，D5 值已过期）——待 closer 拷原件换入 `issues/2026-w45/2026-w45-ko-de/` 并更新 pin（已发版 pin 以 issues/ `.md` 现值为准），绝不重跑 webpdf。
- text.md：新建 `2026-w45-ko-de.text.md` `a658cbf1802d2ba58541dac22ce466a2a7851077bee77d2b06b58fea3678eab0`（28,014 B），与 fanout `.text.md.new` **BYTE-IDENTICAL**；验收 `verify_textexp_ko.py --edition` 判 **ADOPT**（0 UNEXPECTED）。D5 不改文字内容。
- KIT：`production/2026-w45/2026-w45-ko-de/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 D5 节；patched 侧复本逐字节一致）。

## 七、F1 fix（2026-11-14，P7 读者来信盒溢出修复，D39 裁定）

- 修法：盒高修法。`content7.py:96` `lh` 末常数 +26→+59（+33px）。盒底 1737.82→1770.82，末行基线 1764.32，余量 6.5px；预告带底缘 2511.82→2544.82，距页脚线 2596 余量 51.2px；预告带正文 y=2510.82，不压线。文案零改动。
- 基线核实（fix 前实测）：patched 与基线同值同行同量——溢出 +26.50px（末行见 §三）；基线 spill_sweep 亦为 1 SPILL 同行同量（zh-cn/de/nl/pt 基线候选数 278/285/280/281，patched 408/418/413/425，候选数差仅为 D5 run 拆分）。D5 未引入也未加重。
- 门禁（fix 轮，全量重跑，17 门 + D18 + D37）：**19 PASS + 0 FAIL**（15b 仅记录）。G11 0 SPILL；G6 0 flags；G15a print=web 差 0 + text.md BYTE-IDENTICAL（与 builder 终轮逐字节一致，文案零改动）。P8 行数 232→234 / 余量 47.9px（与 builder run1 同值）；D18 gap 276.7、D37 binding 46.8（同值）。门 12 boxtitle 计数 960→961（P7 盒高变化所致 run 计数，0 DEFECT）。
- 新交付物（fix 原件，`fix/2026-w45-ko-de/`；§五已更新为 fix 值）：印 PDF / render 网 PDF / builder 网 PDF（closer 拷原件，绝不重跑 webpdf）/ text.md（与 builder 终轮逐字节一致）。
- 目检：P7 来信盒底裁切（`fix/work/pages/de-p7-fix-crop.png`）末行完整入框，盒底缘在其下可见。
- 同步：`content7.py` 三方一致（production == patched/ == fix/）；KIT 两处复本逐字节一致（含末尾 F1 fix 节）；本目录 `logs/2026-w45-ko-de/GATES-SUMMARY.txt` 已替换为 fix 门禁表（三方 `cmp` 一致，D29）；builder run1 表归档于 `fix/logs/run2-summaries/GATES-SUMMARY-de-builder.txt`。
- 待独立重校 v1（不同工人）：复核修法、重渲、门禁、P7 目检、§6 三方一致。
