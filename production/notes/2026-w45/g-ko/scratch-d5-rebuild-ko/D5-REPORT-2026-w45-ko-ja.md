# D5 重建报告 — 2026-w45-ko-ja（日语读者版）

W45 ko 家 D5 + §1.1 合并重建（旧样式家族：D5 字体修复——讲解层拉丁字符由 Noto Sans CJK 改走 Newsreader；西里尔字符改走 Noto Sans）。施工 2026-11-14（builder v2；v1 于 21:50 UTC 被 runtime restart 杀死未出报告，v2 续用同一 scratch 完成）；**不 commit、不 push、不重校（另派他人）**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-ja-run1/`（`GATES-SUMMARY.txt` 为门禁总表，复本见本目录 `logs/2026-w45-ko-ja/GATES-SUMMARY.txt`）；家族报告：`hidden_files/d5-redo/FAMILY-W45-KO-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样复制为 `production/2026-w45/core-ko/svglib.py`——`apply_variant.py --patch-core ko` 按预期被拒（旧式 core svglib，无 `_char_font`）；`_D5_READER = "latin"`（L122）；`git diff --stat`：1 file，+333/−40。模板与 W47 `core-ko/svglib.py` diff 仅 `_D5_READER` 一行。
- 本版安装：移植模板原样装为版内 `svglib.py`，仅改写 `_D5_READER = "cjk"`（`install-ko.sh`；未对模板跑 `apply_variant.py`——对 ja 读者它会错把 KR 下标改 JP，下标跟目标语（韩文）走，不跟读者走）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。fix2（U+201C/U+201D/U+2019 → serif）保留：`_QUOTE_CLS` 逐版核对在位；普查弯引号在 CJK 为 0（见 §四门 3）。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次跑，不可跳步；首渲前暖 fontconfig `fc-cache -f`）；text.md 由 `hidden_files/style-port-ko/textmd_ko.py`（AST 源码手稿路线，从 content*.py 字面量导出，绝不从 PDF/SVG 反提）导出，交付件为新建的 `.text.md`（W45 ko 11 版 issues 目录原无 `.text.md`，见 §五）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，警告 0。
- 印 PDF：基线重建 36,218,554 B、sha256 `7cb982bf0974acc0a53866ee684a69321bdc23c3ec7408d149436f4a8783b916`；与 fanout 印 PDF **BYTE-IDENTICAL**。网 PDF（基线，`tools/webpdf.py`）2,614,289 B，与 `issues/2026-w45/2026-w45-ko-ja/` 已发网 PDF 文字层多重集差为分隔符类已知差（全家口径：印=网差 0 + 网-vs-issues 差 == fanout-vs-issues 差，零词字符丢失，见家族报告 §2）。
- 修前普查 `d5_census.py`：D5 拉丁 208、西里尔 0、弯引号在 CJK 0（>0 拉丁/西里尔，符合装机前提；ru 版西里尔 253 为俄语讲解层本身）。
- 基线 freeze（D2：freeze 门跟随该版实际构建解释器，D5 重建版用 venv）：门 9 已验 8/8（见 §四）。

## 三、缺陷与修复

- run1 门禁 19 PASS + 0 FAIL，全绿。
- 修复：无（run1 无需改源）。
- 残留：门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）。
- R1（导出器待定项，不修只记录）：text.md 漏收已渲染的短拉丁串 'A2→B2'（P1 内容表 p7 级别格）、'D-17 ~ D-12'（P6 对照表）（导出器 is_prose 规则；本轮不修，见家族报告 §7）。
- P8：行数见 §四门 14（基线→重建）；p8 compare CLEAN（keydiff [137, 138]）；余量仍为正，无溢出，不处理。

## 四、门禁（run1，PASS=19 PASS + 0 FAIL）

- run TOTAL 150、警告 0；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（2,602,952 B <7MB）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff：新增 CJK 字符 TOTAL 0、新增拉丁 strings TOTAL 87（run 拆分计数，非新增内容）；spill 见 §三；boxtitle 0 DEFECT（63 titles、1043 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（P8 行数 196→196，距页脚线余量 48.9px）；文字层 print=web 多重集差 0（印/网各 25832 字符）；census_quotes 0 defective；D18 刊头间距 GAP=383.9（>0，无缺陷）；D37 副刊头余量 263.3（y=372 行）（>0，无缺陷）。
- 门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）：如 'ャ'、'ニ'；门 15 验收以 15a（print=web 差 0）+ 原生校验器 `verify_textexp_ko.py --edition`（ADOPT，0 UNEXPECTED，P8 tokens 966）+ 全文通读为准。
- 日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-ja-run1/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `Lucerna-VOL2-JA.pdf` `b01da78582b551b6b8b54972d0269e5f9e16299e892a5ccb5d784a5a115406f1`（36,192,116 B）；旧（基线）印 PDF `7cb982bf0974acc0a53866ee684a69321bdc23c3ec7408d149436f4a8783b916`（36,218,554 B）。印 PDF 缩小系字体子集变化（拉丁/西里尔移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF（render）`Lucerna-VOL2-JA-web.pdf` `34fb0b3fb950c499fb5d99dfaa94178e8ac4765a0aa57b7becf56dc54e4e3b3c`（2,602,954 B，<7MB）；builder 网 PDF `2026-w45-ko-ja.web.pdf` `8d40f9e5c8072c5b5e439a6b76e4a0332384876df33276739693c429ad252033`（2,602,952 B）——待 closer 拷原件换入 `issues/2026-w45/2026-w45-ko-ja/` 并更新 pin（已发版 pin 以 issues/ `.md` 现值为准），绝不重跑 webpdf。
- text.md：新建 `2026-w45-ko-ja.text.md` `33b14f1cf96e25af3c2b4c67929b06fc820de79f62d0fbd7a9ee7cb6cb5346c3`（28,267 B），与 fanout `.text.md.new` **BYTE-IDENTICAL**；验收 `verify_textexp_ko.py --edition` 判 **ADOPT**（0 UNEXPECTED）。D5 不改文字内容。
- KIT：`production/2026-w45/2026-w45-ko-ja/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 D5 节；patched 侧复本逐字节一致）。
