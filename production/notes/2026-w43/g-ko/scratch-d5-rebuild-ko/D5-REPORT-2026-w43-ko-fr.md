# D5 重建报告 — 2026-w43-ko-fr（French读者版）

W43 ko 家 D5 + §1.1 合并重建（旧样式家族：§1.1 组装 port 自 `style-port-ko/` + D5 字体修复：讲解层拉丁/西里尔字符由 Noto Sans CJK 改走 Newsreader / Noto Sans）。施工 2026-11-13–14；**不 commit、不 push、不重校（另派他人）**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-fr-run2/`（`GATES-SUMMARY.txt` 为门禁总表）；run1 日志在 `logs/2026-w43-ko-fr-run1/`。家族报告：`hidden_files/d5-redo/FAMILY-W43-KO-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样复制为 `production/2026-w43/core-ko/svglib.py`——`apply_variant.py --patch-core ko` 按预期被拒（旧式 core svglib，无 `_char_font`）；`_D5_READER = "latin"`（L122）；`git diff --stat`：1 file，+333/−40。模板与 W47 `core-ko/svglib.py` diff 仅 `_D5_READER` 一行。
- 本版安装：移植模板原样装为版内 `svglib.py`，仅改写 `_D5_READER = "latin"`（`install-ko.sh`；未对模板跑 `apply_variant.py`——对 ja 读者它会错把 KR 下标改 JP，下标跟目标语（韩文）走，不跟读者走）。ko-ru 说明：模板 + `_D5_READER="ru"`，无 fix-xru（W43 已 commit 的 en-ru/es-ru 均保留旧 ru 分支，W43 重建标准以安装器/模板态为准；fix-xru 只进了 W47）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。fix2（U+201C/U+201D/U+2019 → serif）保留：`_QUOTE_CLS` 逐版核对在位；普查弯引号在 CJK 为 0（见 §四门 3）。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次跑，不可跳步）；text.md 由 `hidden_files/style-port-ko/textmd_ko.py`（AST 源码手稿路线，从 content*.py 字面量导出，绝不从 PDF/SVG 反提）导出，交付件为新建的 `.text.md`（W43 ko 11 版 issues 目录原无 `.text.md`，见 §五）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，基线唯一警告：ko-fr `HEAD TOO WIDE [P1-headline]`（port 已知良性项，426.4px vs 栏 422.5px，+3.9px，仍在 28px 栏间隙内，occlusion 0）；D5 重建后该头已修（见 §三），run2 门 1 PASS。
- 印 PDF：基线重建 `33,996,123 B`、sha256 `f1f7eb3d365ae529585d9787537640a7d8a00b7c8e1ff8e68450b2ca9f6a7d0d`；与 fanout 印 PDF SHA 一致（it/ru 例外：fanout 文件事后被覆写，基线重建值与 port 期 `render-*.log` 载值逐字节量级一致，见家族报告 §1.3.1）。网 PDF（基线，`tools/webpdf.py`）与 `issues/2026-w43/2026-w43-ko-fr/` 已发 web PDF 文字层多重集差为分隔符类已知差（全家口径：印=网差 0 + 网-vs-issues 差 == fanout-vs-issues 差，零词字符丢失，见家族报告 §1.3.2）。
- 修前普查 `d5_census.py`：D5 拉丁 **428**、西里尔 **0**、弯引号在 CJK **0**（>0 拉丁/西里尔，符合装机前提；ru 版西里尔 242 为俄语讲解层本身）。
- 基线 freeze（系统 python3 / Pillow 10.2.0）：0/8 为“用错解释器”的结果（基线 svg 是 venv Pillow 13 构建，系统 python3 重跑度量漂移）；base-venv 对照不可跑（`freeze.py` ko 守卫按设计拒绝 pre-D5 版）；D5 后 freeze 本就走 venv，门 9 已验 8/8（见 §四）。详见家族报告 §1.3.3。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁：PASS=17 FAIL=2。run1 缺陷 1 项（真缺陷，已修）+ 门 2 基线残留 + 门 17 误报，见 §三。
- run1 门 1 `HEAD TOO WIDE [P1-headline]: 지금 바로 연습　Exercices immédiats`——与基线同头（§1.2 port 已知良性项，基线实测 426.4px vs 栏 422.5px，+3.9px）；D5 后拉丁走 Newsreader，patched 实测 25pt advance **425.4px**，仍超栏 2.9px。
- 修法（只动字号）：`patched/2026-w43-ko-fr/content12.py:53` `f.head(..., 25)` → **24**（`# D5 fix run1` 注释已加）；24pt 实测 advance **408.3px** ≤422.5，余量 14.2px。文字内容未动。重跑门 1 **PASS**（TOTAL 150、OVF=0、HDW=0）。
- 门 2 残留（**非 patched 缺陷，不修脚本、不改基线**）：`gates-ko.sh` 门 2 把 patched run.log 与 frozen baseline run.log 一并传给 `head_check.py`；patched 日志 0 defects，唯一 finding 是基线日志第 2 行的同一旧警告（基线冻前即有，D5 前发运态亦然）。门 2 因此报 FAIL（1 defect，全系基线侧）。**提请协调员裁定**（是否豁免基线侧 finding 或改门只扫 patched 日志）；run2 门 2 同样 FAIL，patched 侧始终 0 defects。
- 门 17（run1/run2 同）：4 flags，与 de 逐字相同——p1 刊头 `VOL. 1` / `　제` / `1` / `호`（4 run），p2–p8 均为 0；基线同条件 1 flag。按 §5.1 结论（`audit_ko_fr.py` 的 `path_bbox` 把 moth 路径 `d` 属性相对命令当绝对坐标，假 bbox 盖住刊头带；目检刊头无遮挡），**误报，不修**。
- P8：行数见 §四门 14（基线→重建）；p8 compare CLEAN（keydiff [137, 138]）；余量仍为正，无溢出，不处理。

## 四、门禁（run2，PASS=17 FAIL=2）

- run TOTAL 150、警告 0；head_check FAIL（1 defect，全系基线侧旧警告；patched 0 defects，提请协调员裁定，见 §三）；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（2013800 B <7MB）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff vs base：p8 +133 strings / -43 strings、新增 CJK 字符 TOTAL 0、新增拉丁 strings TOTAL 239（run 拆分计数，非新增内容）；spill 0；boxtitle 0 DEFECT（63 titles、760 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（ratios n=379，中位 1.007，粗体中位 1.04，常规中位 0.987；P8 行数 240→245，距页脚线余量 48.7px）；文字层 print=web 多重集差 0（印/网各 29524 字符）；census_quotes 0 defective；D18 刊头间距 GAP=321.1（>0，无缺陷）。
- 门 17 家族 gates.py：4 flags，全系 `path_bbox` 误报（§5.1 同类），不修。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-fr-run2/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `Lucerna-VOL1-FR.pdf` `b6bdc15de1b1cd2ae33594025ca678a44278fd843288ee80a6f4034642f6c4fe`（32,299,082 B）；旧（基线）印 PDF `f1f7eb3d365ae529585d9787537640a7d8a00b7c8e1ff8e68450b2ca9f6a7d0d`（33,996,123 B）。印 PDF 缩小系字体子集变化（拉丁/西里尔移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF `Lucerna-VOL1-FR-web.pdf` `0095e92a08e25ec37010d98a97a9e64a9e864b51fe9466db41a6331cd52d5e80`（2,013,800 B，<7MB）——待 closer 换入 `issues/2026-w43/2026-w43-ko-fr/2026-w43-ko-fr.pdf` 并更新 pin（已发版 pin 以 issues/ `.md` 现值为准）。
- text.md：新建 `2026-w43-ko-fr.text.md` `44a4cffc7f04b0f844fc56a3eea08c4342c4317316310d5217b501b6d3ce0f4c`（21,897 B），与 fanout `.text.md.new` **BYTE-IDENTICAL**；验收 `verify_textexp_ko.py --edition` 判 **ADOPT**（0 UNEXPECTED）。D5 不改文字内容。
- KIT：`production/2026-w43/2026-w43-ko-fr/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 `## 11. D5 rebuild (2026-11-13)`）。
