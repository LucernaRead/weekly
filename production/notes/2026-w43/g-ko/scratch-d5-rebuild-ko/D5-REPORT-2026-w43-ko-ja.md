# D5 重建报告 — 2026-w43-ko-ja（Japanese读者版）

W43 ko 家 D5 + §1.1 合并重建（旧样式家族：§1.1 组装 port 自 `style-port-ko/` + D5 字体修复：讲解层拉丁/西里尔字符由 Noto Sans CJK 改走 Newsreader / Noto Sans）。施工 2026-11-13–14；**不 commit、不 push、不重校（另派他人）**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-ja-run2/`（`GATES-SUMMARY.txt` 为门禁总表）；run1 日志在 `logs/2026-w43-ko-ja-run1/`。家族报告：`hidden_files/d5-redo/FAMILY-W43-KO-BUILD.md`。

## 一、装机

- Core 落盘（全家共用一次）：移植模板 `tools/mechanism-w47/svglib-ko-d5.py`（539 行）原样复制为 `production/2026-w43/core-ko/svglib.py`——`apply_variant.py --patch-core ko` 按预期被拒（旧式 core svglib，无 `_char_font`）；`_D5_READER = "latin"`（L122）；`git diff --stat`：1 file，+333/−40。模板与 W47 `core-ko/svglib.py` diff 仅 `_D5_READER` 一行。
- 本版安装：移植模板原样装为版内 `svglib.py`，仅改写 `_D5_READER = "cjk"`（`install-ko.sh`；未对模板跑 `apply_variant.py`——对 ja 读者它会错把 KR 下标改 JP，下标跟目标语（韩文）走，不跟读者走）。ko-ru 说明：模板 + `_D5_READER="ru"`，无 fix-xru（W43 已 commit 的 en-ru/es-ru 均保留旧 ru 分支，W43 重建标准以安装器/模板态为准；fix-xru 只进了 W47）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。fix2（U+201C/U+201D/U+2019 → serif）保留：`_QUOTE_CLS` 逐版核对在位；普查弯引号在 CJK 为 0（见 §四门 3）。
- 重建：`run.py` → `render.py` → `webpdf.py`（依次跑，不可跳步）；text.md 由 `hidden_files/style-port-ko/textmd_ko.py`（AST 源码手稿路线，从 content*.py 字面量导出，绝不从 PDF/SVG 反提）导出，交付件为新建的 `.text.md`（W43 ko 11 版 issues 目录原无 `.text.md`，见 §五）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，基线 0 警告。
- 印 PDF：基线重建 `38,916,446 B`、sha256 `1fedcfc7bd0b8024dcccf62fde449da35270613ca0d1a6a84e8be4e535a31918`；与 fanout 印 PDF SHA 一致（it/ru 例外：fanout 文件事后被覆写，基线重建值与 port 期 `render-*.log` 载值逐字节量级一致，见家族报告 §1.3.1）。网 PDF（基线，`tools/webpdf.py`）与 `issues/2026-w43/2026-w43-ko-ja/` 已发 web PDF 文字层多重集差为分隔符类已知差（全家口径：印=网差 0 + 网-vs-issues 差 == fanout-vs-issues 差，零词字符丢失，见家族报告 §1.3.2）。
- 修前普查 `d5_census.py`：D5 拉丁 **215**、西里尔 **0**、弯引号在 CJK **0**（>0 拉丁/西里尔，符合装机前提；ru 版西里尔 242 为俄语讲解层本身）。
- 基线 freeze（系统 python3 / Pillow 10.2.0）：0/8 为“用错解释器”的结果（基线 svg 是 venv Pillow 13 构建，系统 python3 重跑度量漂移）；base-venv 对照不可跑（`freeze.py` ko 守卫按设计拒绝 pre-D5 版）；D5 后 freeze 本就走 venv，门 9 已验 8/8（见 §四）。详见家族报告 §1.3.3。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁：PASS=16 FAIL=3。run1 缺陷 1 项（真缺陷，已修；run2 已验）+ 门 17 缺脚本 SKIP，见 §三。
- run1 门 12 boxtitle 与门 14 creambox 同报 1 项：P2 box#2 y=724.79 `「D-데이」 사용법　「D-day」の使い方` 右越 **+9.8px**。
- 根因：D5 后拉丁 `D-day` 走 Newsreader 粗体变宽；实测 23pt advance **414.2px** > 框内宽 404.5（+9.7px，与门禁 +9.8 一致）。
- 修法（只动字号）：`patched/2026-w43-ko-ja/content12.py:186` 该 `f.box` 加 `tsize=22`（`# D5 fix run1` 注释已加；f.box 开行 :182）；22pt 实测 advance **396.2px**，余量 8.3px。文字内容未动。
- run2 复核：门 12 boxtitle 与门 14 creambox 均 0 DEFECT。
- P8：行数见 §四门 14（基线→重建）；p8 compare CLEAN（keydiff [137, 138]）；余量仍为正，无溢出，不处理。

## 四、门禁（run2，PASS=18 FAIL=1）

- run TOTAL 150、警告 0；head_check PASS 0 defects；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（2385938 B <7MB）；occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff [137, 138]）；freeze baseline 8/8；freeze diff vs base：p8 +138 strings / -46 strings、新增 CJK 字符 TOTAL 0、新增拉丁 strings TOTAL 99（run 拆分计数，非新增内容）；spill 0；boxtitle 0 DEFECT（57 titles、778 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（ratios n=357，中位 1.009，粗体中位 1.04，常规中位 1.0；P8 行数 196→197，距页脚线余量 48.9px）；文字层 print=web 多重集差 0（印/网各 22192 字符）；census_quotes 0 defective；D18 刊头间距 GAP=305.4（>0，无缺陷）。
- 门 17 家族 gates.py：SKIP（无 `audit_ko_ja.py` 脚本）。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-ko/logs/2026-w43-ko-ja-run2/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `Lucerna-VOL1-JA.pdf` `20dafa6557ba13c8738de12b71b8e460c68921641278a0d8957a4d107bf4d9b6`（36,837,019 B）；旧（基线）印 PDF `1fedcfc7bd0b8024dcccf62fde449da35270613ca0d1a6a84e8be4e535a31918`（38,916,446 B）。印 PDF 缩小系字体子集变化（拉丁/西里尔移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF `Lucerna-VOL1-JA-web.pdf` `c4235d170870b9360ac190ecf4d42631909cec542933d183e675c99c2c78845f`（2,385,938 B，<7MB）——待 closer 换入 `issues/2026-w43/2026-w43-ko-ja/2026-w43-ko-ja.pdf` 并更新 pin（已发版 pin 以 issues/ `.md` 现值为准）。
- text.md：新建 `2026-w43-ko-ja.text.md` `01f95134e72d7ebd165c68f7d0eaf3517b02aa4e7bdef00cc83b9fb0a3f3ef11`（21,593 B），与 fanout `.text.md.new` **BYTE-IDENTICAL**；验收 `verify_textexp_ko.py --edition` 判 **ADOPT**（0 UNEXPECTED）。D5 不改文字内容。
- KIT：`production/2026-w43/2026-w43-ko-ja/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 `## §10 D5 重建记录（2026-11-13）`）。
