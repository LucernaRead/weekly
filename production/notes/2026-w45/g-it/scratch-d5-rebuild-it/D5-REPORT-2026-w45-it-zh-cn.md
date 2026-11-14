# D5 重建报告 — 2026-w45-it-zh-cn（简体中文读者版）

W45 it 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
施工分工：builder v1 完成第 0–5 步、run1 全部门禁、全部字号修复与 run2 前 6 版（zh-cn/de/en/es/fr/ja）；builder v2（接替 v1，v1 被 restart drain 杀死）完成 run2 余下 5 版（ko/nl/pt/ru/zh-tw）、KIT 更新与本报告。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-it/logs/2026-w45-it-zh-cn/`（`GATES-SUMMARY.txt` 为 run2 门禁总表，`run1/GATES-SUMMARY.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-zh-cn/GATES-SUMMARY.txt`（与 scratch run2 总表逐字节一致，`cmp` 已验）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core it --week 2026-w45` → `production/2026-w45/core-it/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-it-zh-cn/svglib.py --target it --reader zh-cn --week 2026-w45`（先 `--check` dry-run，mode=cjk 正确）。装后 `_D5_READER = "cjk"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `hidden_files/style-port-it/export_it.py` 导出（第 0 步已核实：scratch 试跑 vs issues 已发版 BYTE-IDENTICAL，11/11）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 19,518,204 字节（sha256 `279ca72a9ad1…`），与 fanout 原件逐字节一致；网 PDF 1,106,135 字节。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF 差 **0**。
- 修前普查 `d5_census.py`：D5 违规 **344**（>0，符合装机前提）。
- 基线 P8 口径：noted **150/150**。

## 三、缺陷与修法（run1 → run2）

run1 共 2 项，全部为 D5 字体加宽引起（讲解层粗体在 Noto Sans CJK 下比 Newsreader 宽，框标题右溢；P1 溢出的标题同时造成 occlusion 墨迹重叠）。修法只动字号，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | 6 occlusion / 12 boxtitle / 14 creambox | P1 框标题 `　数字看本周` | 右溢 +42.6px；墨迹与 P1 正文重叠 14.6×12.0px | `content12.py:49` 框标题 tsize →**20** |
| 2 | 10 freeze-diff（run1 读数 artifact） | freeze-diff JSON 缺顶层 totals 键 | 读数 new-CJK −1 / new-Latin None；boxtitle backup 查找返回 None；creambox totals 键缺失 → defects −1 | 无内容修复；run2 重新实测全部干净（new-CJK 0 / new-Latin 225；boxtitle 0 缺陷且 backup 找到；creambox 0 缺陷）。三者皆为同一 P1 标题溢出的 run1 测量读数问题，无独立缺陷。 |

P8 变化：210->210 行，距页脚线余量 57.6 → 57.6 px（正，无溢出）。

- 本版构建目录即 `production/2026-w45/core-it/`（zh-cn 读者版无自有目录；D10：W45 fanout vs 仓内 core-it 9/9 相同，无动作）。P8 compare 以本版 SVG 为 core，keydiff=[]（自身对照）。

## 四、门禁（run2，全套 17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 7,426,081 B |
| 5 webpdf | RC=0，网 PDF 885,896 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**，keydiff=[]，missing=[]，extra=[] |
| 9 freeze baseline | 8/8（patched 重建复现自身 SVG） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 225，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 spills |
| 12 boxtitle | 0 defects |
| 13 edge | 0 touches，0 nears |
| 14 creambox | 0 defects；P8 行数 210->210，页脚余量 57.6 px |
| 15 text layer | print=web=issues，字符多重集差 0 |
| 15a text.md | 导出 RC=0，**BYTE-IDENTICAL** vs issues 已发版 |
| 16 census_quotes | 0 defective |
| 18 masthead（D18） | slogan–date 间隙 127.3px，PASS（>0） |

**结论：run2 ALL-GREEN。**

## 五、新交付物 / KIT

- 印 PDF：`scratch-2026-w45-it/patched/2026-w45-it-zh-cn/The-Lucerna-VOL3.pdf` — 7,426,081 字节，sha256 `c71c23977abfd70346453e5f378e11779856b19de6c4f57dba2657466b9e76db`（文件名 VOL3 为 render.py 既有命名，基线同名，刊头 VOL.2 无误）。
- 网 PDF：`scratch-2026-w45-it/patched/2026-w45-it-zh-cn/2026-w45-it-zh-cn.web.pdf` — 885,896 字节，sha256 `80a779eb2335e81c32adc0f02834d4c8f2712be488aedb1c5435c5f70845a262`。网 PDF 跨次运行字节不确定，**closer 须拷 builder 原件，绝不重跑 webpdf**；KIT 记录的 builder SHA 即交付值。
- text.md：`scratch-2026-w45-it/logs/2026-w45-it-zh-cn/2026-w45-it-zh-cn.text.md.run2` — 52,462 字节，sha256 `5cdba24afde011be09844fc9516513a5a09c40e7e682d5e36eea0dd0aebf03ad`，与 issues 已发版 BYTE-IDENTICAL。
- KIT：`production/2026-w45/core-it/WEEKLY-KIT.md` 针脚行已更新为上述新值 + 文末 D5 节（§11（core-it KIT））。
