# D5 重建报告 — 2026-w43-it-zh-cn（简体中文读者版（core-it，兼 zh-cn 读者版））

W43 it 家 D5 + §1.1 合并重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Noto Sans CJK 改走 Newsreader / Noto Sans；§1.1 组装：port fanout .py 集进仓内 core-it，旧样式→新样式）。施工 2026-11-13（一任 builder 至 run2 循环，二任 builder 接手核实 + gate 2 补跑 + 本报告）；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-zh-cn/`（`GATES-SUMMARY.txt` 为门禁总表，`run1/` 为修前日志归档，`run2/` 为修后日志归档）。

## 一、装机

- 本版即 core-it：生产 `core-it/svglib.py` 已落盘 `_D5_READER = "latin"`（L100）+ fix2 块 + D5 sans 块；scratch 内本版按 zh-cn 读者装，终值 `"cjk"`，与已落盘 core-it 仅差 `_D5_READER` 一行（与 en/es 家同款）。
- 本版安装：`apply_variant.py --svglib <版>/svglib.py --target it --reader zh-cn --week 2026-w43`（先 `--check` dry-run 通过）。装后 `_D5_READER = "cjk"`。fix2（U+201C/U+201D/U+2019 → serif）保留：本版弯引号修前在 CJK 3 个，fix2 后归 Newsreader。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由 `hidden_files/style-port-it/export_it.py`（源码 manuscript 路线）重出核验（见第五节）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；`render.py` + `webpdf.py` 产出与已发版文本层逐字一致（字符多重集差 0）；重建 SVG 8/8 与 fanout 逐字节相同；印 PDF 与 fanout 印 PDF SHA 逐字节一致（`73f91e8973ec…`，21422077 B）。
- 修前普查 `d5_census.py`：D5 拉丁 **347**、西里尔 **0**、弯引号在 CJK **3**（拉丁 >0，符合装机前提）。
- KIT 记录的印/网 SHA 为旧配方值，已过期（例：core-it KIT §14 仍记印 22,914,252 B / 网 3,460,204 B，§10 仅记 22.9 MB / 3.48 MB）；基线不以 KIT SHA 为准，KIT 更新时以实测发运值订正（见第五节）。

## 三、缺陷与修复（run 1 → 二次修复）

- run 1 门禁：head_check 缺陷 **1**（P3 `UNA GRANDE PITTRICE A FIRENZE` 25pt=470.9，超栏 422.5）；boxtitle/creambox 缺陷 **1**（P1 `LA SETTIMANA IN CIFRE　数字看本周` 右溢 +42.6px，tsize 23pt=447.1 vs 盒标题内宽 404.5）；occlusion 0；spill 0；刊头间距 415.2px PASS；P8 199 行、余量 57.4px。
- 二次修复（只动字号，文字零改动；脚本 `scratch-2026-w43-it/fix-it.py`，逐行断言式替换；量宽用 patched svglib `text_w`，sans bold；栏宽 CW=422.5，盒标题内宽 404.5，P7 p.text 标题内宽 400.5；盒修法行号指 tsize 行，D19）：
  1. `content34.py:22` P3 头 `UNA GRANDE PITTRICE A FIRENZE` 25→22（470.9→414.4，余 8.1px）。
  2. `content12.py:48` P1 盒 `LA SETTIMANA IN CIFRE　数字看本周` tsize 23→20（447.1→388.8，余 15.7px）。
- P8：行数 199→199，距页脚线余量 57.4 px 不变；p8 compare CLEAN（keydiff []）。

## 四、门禁（run 2，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0（弯引号总数 6，全在 Newsreader）；render RC=0；webpdf RC=0（1474552 B <7MB）；occlusion 0 flags（含自检）；p8 extract 150/150；p8 compare CLEAN（keydiff []）；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL **0**（无 U+3000，PLAN Amendments 定位步骤不适用；新增拉丁 strings TOTAL 229，run 拆分所致）；spill 0（80 OBSERVE）；boxtitle 0 DEFECT（28 titles、325 body lines）；edge 0 TOUCH、0 NEAR；creambox PASS 0 defects（ratios n=384，中位 1.04，粗体中位 1.057，常规中位 1.0）；文字层 print=web 多重集差 0（91921 字符）；text.md BYTE-IDENTICAL；census_quotes 0 defective；家族 gates.py N/A（it 家无）；刊头间距 415.2 px PASS（D18）。
- gate 2 补跑：原 run2 循环中 gate 2 判 BLOCKED（归档事故：基线期文件被误移，`base-run.log` 缺失；非内容缺陷）；二任拷回文件后单独重跑本版全部门禁（2026-11-13 23:03Z），gate 2 PASS，其余 17 门数值与原 run2 逐项一致。
- 日志：`hidden_files/d5-redo/scratch-2026-w43-it/logs/2026-w43-it-zh-cn/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `The-Lucerna-VOL1-it-zh-cn.pdf` `d8e6db8696db0ed1d9a19a761507588465fd13231d1c197145aa68914fc63156`（9325711 B；修前 `73f91e8973ec101059a56c8e8756446b50bf9bff03a9df4bff7d94189b11f333`，21422077 B）。印 PDF 缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。
- 新网 PDF（`tools/webpdf.py`）`0c918ba5dd1e19f4b2c4af703b463649871eae1bf6e9c0f60131d4f603c89a0d`（1474552 B）——待 closer 换入 `issues/2026-w43/2026-w43-it-zh-cn/2026-w43-it-zh-cn.pdf` 并更新 pin（已发版 `9247160a0440e713e4963bc3ee2a3a7a5768759982ed9483538b771e9c670a7c`，1844301 B）。
- text.md：D5 不改文字内容；重建后由 `export_it.py` 从 patched 源码重出，与 fanout `.text.md.new` **BYTE-IDENTICAL**（52417 B，SHA `30cdd55f7049fcef09ddb6657e35b6db834fe8cee6cdc00a8c20674357dddf78`）。W43 it 在 `issues/` 内无已发 `.text.md`（11 版目录均只有 `.md` + `.pdf`），closer 落仓时按 MANIFEST 把该文件补进 `issues/`（新建，非覆盖）。
- KIT：`production/2026-w43/core-it/WEEKLY-KIT.md`（交付物行已更新为 D5 新值 + 文末追加 D5 记录节）。
