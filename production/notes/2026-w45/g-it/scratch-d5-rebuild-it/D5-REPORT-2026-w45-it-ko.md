# D5 重建报告 — 2026-w45-it-ko（韩语读者版）

W45 it 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
施工分工：builder v1 完成第 0–5 步、run1 全部门禁、全部字号修复与 run2 前 6 版（zh-cn/de/en/es/fr/ja）；builder v2（接替 v1，v1 被 restart drain 杀死）完成 run2 余下 5 版（ko/nl/pt/ru/zh-tw）、KIT 更新与本报告。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-it/logs/2026-w45-it-ko/`（`GATES-SUMMARY.txt` 为 run2 门禁总表，`run1/GATES-SUMMARY.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-ko/GATES-SUMMARY.txt`（与 scratch run2 总表逐字节一致，`cmp` 已验）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core it --week 2026-w45` → `production/2026-w45/core-it/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-it-ko/svglib.py --target it --reader ko --week 2026-w45`（先 `--check` dry-run，mode=cjk 正确）。装后 `_D5_READER = "cjk"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `hidden_files/style-port-it/export_it.py` 导出（第 0 步已核实：scratch 试跑 vs issues 已发版 BYTE-IDENTICAL，11/11）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 10,805,462 字节（sha256 `737024563c08…`），与 fanout 原件逐字节一致；网 PDF 922,724 字节。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF 差 **0**。
- 修前普查 `d5_census.py`：D5 违规 **337**（>0，符合装机前提）。
- 基线 P8 口径：noted **150/150**。

## 三、缺陷与修法（run1 → run2）

run1 共 2 项，全部为 D5 字体加宽引起（讲解层粗体在 Noto Sans CJK 下比 Newsreader 宽，框标题右溢；P1 溢出的标题同时造成 occlusion 墨迹重叠）。修法只动字号，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | 12 boxtitle / 14 creambox | P1 `IN QUESTO NUMERO　이번 호 차례`（`차례` 框） | 右溢 +15.7px | `content12.py:90` 24→**22**pt |
| 2 | 12 boxtitle / 14 creambox | P2 框标题 `LA FRASE PER RICORDARE　암기문장` | 右溢 +35.3px | `content12.py:181` tsize →**20** |

P8 变化：245->245 行，距页脚线余量 45.4 → 45.4 px（正，无溢出）。

## 四、门禁（run2，全套 17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 7,858,684 B |
| 5 webpdf | RC=0，网 PDF 814,520 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**，keydiff=[137, 138, 139]，missing=[]，extra=[] |
| 9 freeze baseline | 8/8（patched 重建复现自身 SVG） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 215，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 spills |
| 12 boxtitle | 0 defects |
| 13 edge | 0 touches，0 nears |
| 14 creambox | 0 defects；P8 行数 245->245，页脚余量 45.4 px |
| 15 text layer | print=web=issues，字符多重集差 0 |
| 15a text.md | 导出 RC=0，**BYTE-IDENTICAL** vs issues 已发版 |
| 16 census_quotes | 0 defective |
| 18 masthead（D18） | slogan–date 间隙 195.7px，PASS（>0） |

**结论：run2 ALL-GREEN。**

## 五、新交付物 / KIT

- 印 PDF：`scratch-2026-w45-it/patched/2026-w45-it-ko/The-Lucerna-VOL3.pdf` — 7,858,684 字节，sha256 `60298464bf9498d272e33149de6937ea54de4a39f5d4f6cbeee3b196149a5a38`（文件名 VOL3 为 render.py 既有命名，基线同名，刊头 VOL.2 无误）。
- 网 PDF：`scratch-2026-w45-it/patched/2026-w45-it-ko/2026-w45-it-ko.web.pdf` — 814,520 字节，sha256 `26b87dff3c25567a392c55b943042fa08078a05a33f247ffd1d90d8ea7adc92d`。网 PDF 跨次运行字节不确定，**closer 须拷 builder 原件，绝不重跑 webpdf**；KIT 记录的 builder SHA 即交付值。
- text.md：`scratch-2026-w45-it/logs/2026-w45-it-ko/2026-w45-it-ko.text.md.run2` — 57,272 字节，sha256 `14f60dc1cce7da3e5d91125d491f887dd0a5032c6301cbb84300f272753775f8`，与 issues 已发版 BYTE-IDENTICAL。
- KIT：`production/2026-w45/2026-w45-it-ko/WEEKLY-KIT.md` 针脚行已更新为上述新值 + 文末 D5 节（§14）。
