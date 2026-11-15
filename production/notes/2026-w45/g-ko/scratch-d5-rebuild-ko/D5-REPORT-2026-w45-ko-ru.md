# D5 重建报告 — 2026-w45-ko-ru（俄语读者版）

W45 ko 家 D5 + §1.1 合并重建（旧样式家族：D5 字体修复——讲解层拉丁字符由 Noto Sans CJK 改走 Newsreader；西里尔字符改走 Noto Sans）。施工 2026-11-14（builder v2；v1 于 21:50 UTC 被 runtime restart 杀死未出报告，v2 续用同一 scratch 完成）；**不 commit、不 push、不重校（另派他人）**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-ru-run2/`（`GATES-SUMMARY.txt` 为门禁总表，复本见本目录 `logs/2026-w45-ko-ru/GATES-SUMMARY.txt`）；家族报告：`hidden_files/d5-redo/FAMILY-W45-KO-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样复制为 `production/2026-w45/core-ko/svglib.py`——`apply_variant.py --patch-core ko` 按预期被拒（旧式 core svglib，无 `_char_font`）；`_D5_READER = "latin"`（L122）；`git diff --stat`：1 file，+333/−40。模板与 W47 `core-ko/svglib.py` diff 仅 `_D5_READER` 一行。
- 本版安装：移植模板原样装为版内 `svglib.py`，仅改写 `_D5_READER = "ru"`（`install-ko.sh`；未对模板跑 `apply_variant.py`——对 ja 读者它会错把 KR 下标改 JP，下标跟目标语（韩文）走，不跟读者走）。ko-ru 说明：模板 + `_D5_READER="ru"`，无 fix-xru（W43 已 commit 的 en-ru/es-ru 均保留旧 ru 分支，W43 重建标准以安装器/模板态为准；fix-xru 只进了 W47）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。fix2（U+201C/U+201D/U+2019 → serif）保留：`_QUOTE_CLS` 逐版核对在位；普查弯引号在 CJK 为 0（见 §四门 3）。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次跑，不可跳步；首渲前暖 fontconfig `fc-cache -f`）；text.md 由 `hidden_files/style-port-ko/textmd_ko.py`（AST 源码手稿路线，从 content*.py 字面量导出，绝不从 PDF/SVG 反提）导出，交付件为新建的 `.text.md`（W45 ko 11 版 issues 目录原无 `.text.md`，见 §五）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，警告 0。
- 印 PDF：基线重建 30,654,912 B、sha256 `a9c7c48286177b4b8d694110891aa20591bed14c4a71e290a3c26eec4f00d05d`；与 fanout 印 PDF **BYTE-IDENTICAL**。网 PDF（基线，`tools/webpdf.py`）2,209,459 B，与 `issues/2026-w45/2026-w45-ko-ru/` 已发网 PDF 文字层多重集差为分隔符类已知差（全家口径：印=网差 0 + 网-vs-issues 差 == fanout-vs-issues 差，零词字符丢失，见家族报告 §2）。
- 修前普查 `d5_census.py`：D5 拉丁 209、西里尔 253、弯引号在 CJK 0（>0 拉丁/西里尔，符合装机前提；ru 版西里尔 253 为俄语讲解层本身）。
- 基线 freeze（D2：freeze 门跟随该版实际构建解释器，D5 重建版用 venv）：门 9 已验 8/8（见 §四）。

## 三、缺陷与修复

- run1 门禁 17 PASS + 2 FAIL：门 12 boxtitle（标题越框，已修）、门 14 creambox（同一标题，已修）。run2 门禁 19 PASS + 0 FAIL，全绿。
- 修复：1 项（run1 → run2）：`patched/2026-w45-ko-ru/content12.py:56` 数字盒标题 `f.box("숫자로 보는 이번 주　Неделя в цифрах", …)` 加 `tsize=22`（默认 23；`# D5 fix run1` 注释已加）。23pt 下标题越过盒右缘 +14.7px——基线已 +10.5px（已发版即有），D5 因西里尔改走 Noto Sans 又加宽 4.2px；22pt 恢复约 +3.5px 余量。门 12 boxtitle 与门 14 creambox 报的是同一标题，**一修双清**，重跑两门均 **PASS**。
- 残留：门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）。P8 元素数约为他版 2 倍（基线 2746、重建 2851），基线与重建同状，系俄语版自身特性，非 D5 产物；抽取 150/150，比对 CLEAN。印 PDF 文字层 run1 32454 字、run2 32453 字，差 1 字为文本抽取口径噪声（text.md 逐字节一致，15c ADOPT）。
- R1（导出器待定项，不修只记录）：text.md 漏收已渲染的短拉丁串 'A2→B2'（P1 内容表 p7 级别格）、'D-17 ~ D-12'（P6 对照表）（导出器 is_prose 规则；本轮不修，见家族报告 §7）。
- P8：行数见 §四门 14（基线→重建）；p8 compare CLEAN（keydiff [137, 138]）；余量仍为正，无溢出，不处理。

## 四、门禁（run2，PASS=19 PASS + 0 FAIL）

- run TOTAL 150、警告 0；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（2,352,037 B <7MB）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff：新增 CJK 字符 TOTAL 0、新增拉丁 strings TOTAL 83（run 拆分计数，非新增内容）；spill 见 §三；boxtitle 0 DEFECT（73 titles、992 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（P8 行数 247→247，距页脚线余量 46.1px）；文字层 print=web 多重集差 0（印/网各 32453 字符）；census_quotes 0 defective；D18 刊头间距 GAP=343.2（>0，无缺陷）；D37 副刊头余量 65.7（y=394 俄文副刊头行）（>0，无缺陷）。
- 门 15b carryover RC=1（D27 已知 ko 工具缺口，仅记录）：如 'зиме'、'экзамен'；门 15 验收以 15a（print=web 差 0）+ 原生校验器 `verify_textexp_ko.py --edition`（ADOPT，0 UNEXPECTED，P8 tokens 930）+ 全文通读为准。
- 日志：`hidden_files/d5-redo/scratch-2026-w45-ko/logs/2026-w45-ko-ru-run2/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `Lucerna-VOL2-RU.pdf` `0dcafe7d13d952c407493bdf4e01a50ad5f3ce7a8590689250b1d384a2237f97`（30,794,411 B）；旧（基线）印 PDF `a9c7c48286177b4b8d694110891aa20591bed14c4a71e290a3c26eec4f00d05d`（30,654,912 B）。印 PDF 缩小系字体子集变化（拉丁/西里尔移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF（render）`Lucerna-VOL2-RU-web.pdf` `da6db92d29148b8697149cc3f01275385e85dd24efbb09b5f141b48d7c1fc225`（2,352,003 B，<7MB）；builder 网 PDF `2026-w45-ko-ru.web.pdf` `fe78ee3f3ef80dc5d72e94152dedc2c377844360340697eb1a5ff5d14c13fcaa`（2,352,037 B）——待 closer 拷原件换入 `issues/2026-w45/2026-w45-ko-ru/` 并更新 pin（已发版 pin 以 issues/ `.md` 现值为准），绝不重跑 webpdf。
- text.md：新建 `2026-w45-ko-ru.text.md` `2b959fcf1e8a565d5aefaa4ac601af1f3b903c8799b193b8d6de45d1c30c1278`（30,515 B），与 fanout `.text.md.new` **BYTE-IDENTICAL**；验收 `verify_textexp_ko.py --edition` 判 **ADOPT**（0 UNEXPECTED）。D5 不改文字内容。
- KIT：`production/2026-w45/2026-w45-ko-ru/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 D5 节；patched 侧复本逐字节一致）。
