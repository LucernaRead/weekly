# D5 重建报告 — 2026-w46-de-fr（法语读者版）

W46 de 家 D5-only 重建（新样式 + D5 字体修；D5 缺陷：讲解层拉丁/西里尔字母落入 Noto Sans CJK 而非 Newsreader（拉丁读者）/ Noto Sans（俄语读者），违反 SOP §1.1 字体表）。施工 2026-11-15；**不 commit、不 push、不清 scratch**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-fr/`（`GATES-SUMMARY.txt` 为门禁总表）。家族报告：`hidden_files/d5-redo/FAMILY-W46-DE-BUILD.md`。

## 一、装机

- 本版安装：`hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target de --reader fr --week 2026-w46`（先 `--check` dry-run 通过）。装后 `_D5_READER = "latin"`。fix2 保留（patched `svglib.py` 内 fix2 相关 5 处，`_QUOTE_CLS` 4 处）。core 模板 `patched/core-de/svglib.py` 以 latin reader 装机（与 `--patch-core` 等值；`--patch-core` 本身未跑，不写 production，见家族报告 §10）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**。
- 重建：`run.py` → `render.py` → `webpdf.py`；text.md 由已核实导出器 `hidden_files/style-port-de/export_de.py`（第 0 步试跑 BYTE-IDENTICAL）重出。

## 二、基线（修前，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 警告；render rc=0、webpdf rc=0、export rc=0。
- 修前普查 `d5_census.py`：D5 拉丁 633、西里尔 0、弯引号 CJK 0；花括号总量 30，全在 Newsreader 内、0 在 CJK 内。
- 基线实测：印 PDF `cc72bed80fbbe2b7d6ec98a76f93843526e765aa9c565e5fe85895eb5600aea7`（3,598,197 B）；网 PDF `3bcec24a81d4750be514f6e3a338f73bdab2243732c38decbd36bb8336e9dc03`（1,016,898 B）。基线网 PDF vs `issues/` 已发网 PDF 文字层 stripped-diff 0；export vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（49,140 B）。KIT 印/网 SHA 针脚已过期（已知 KIT SHA 滞后），基线以文字层/export 证据为准，不以 KIT SHA 为准。

## 三、缺陷与修复（run1 → 二次修复）

- run1 门禁 15/19：盒标题 4（En chiffres +32.8、Sommaire +7.5、Saint-Martin +21.0 ×2）+ 预告带 TEXTX 1（与 SEMAINE INTERNATIONALE 重叠 167.8px）+ D18 1（间隙 −2.9px）；其余门全绿。
- 二次修复（只动字号，文字零改动；探针 `bin/probe_fix.py` 量测在案，留 ≥2px 余量；盒标题 f.box `tsize=` / `p.text` 字号字面量）：
- `content12.py:25` P1 预告带左标题 46→38pt（TEXTX 与右标题 `SEMAINE INTERNATIONALE` 重叠 167.8px）
- `content12.py:15` 刊头标语 17→16pt + `content12.py:16` 刊头日期 17→16pt（D18 间隙 −2.9px）
- `content12.py:43–47` P1 数字盒 `f.box` 加 `tsize=21`（标题右越 32.8px，23pt；22pt 仍越 14.0px）
- `content12.py:89` P1 目录标题 24→22pt（右越 7.5px）
- `content34.py:46` + `content56.py:45` P3/P5 圣马丁词盒标题 24→22pt（右越 21.0px ×2）
- 注：run2 的 D18 修复曾因注释错位使两行的 `spacing=1.7` 失效（刊头无字距，间隙虚高 160.7px）；run3 已恢复 `spacing=1.7`（16pt 不变），间隙 42.5px PASS，其余门禁值与 run2 相同。
- P8：行数 230->230，距页脚线余量 40.3->40.3 px（y=2596 线、页底 2700）；p8 compare CLEAN（keydiff [137, 138, 139, 150]，预期读者键）。

## 四、门禁（run3，ALL-GREEN）

- run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里尔 0 / 弯引号 CJK 0；render RC=0；webpdf RC=0（932,346 B <7MB）；occlusion 0（含自检，6 类全触发）；p8 extract 150/150；p8 compare CLEAN；freeze 基线 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 0（新增 Latin 字符串 397，断 run 拆分，仅记录）；spill 0（32 boxes, 89 candidates, 0 SPILL）；boxtitle 0（48 titles, 242 body lines, 0 DEFECT）；edge 0 TOUCH 0 NEAR；creambox PASS 0 缺陷；文字层 print=web 多重集差 0（print=107650 web=107650）；census_quotes 0 defective；D18 刊头间距 42.5px（>0）；D37 副刊头余量 10.5px（>0）。
- 非门禁残留（D21/D22/D27 口径，仅记录）：15b carryover（2x 'auf'、2x 'semaine'）；按 D21/D22/D27 口径以 15a + native verifier ADOPT 验收。15c native verifier ADOPT（0 UNEXPECTED）。
- 日志：`hidden_files/d5-redo/scratch-2026-w46-de/logs/2026-w46-de-fr/GATES-SUMMARY.txt`。

## 五、新交付物与 KIT

- 新印 PDF `f71a5bdab39eea4fbbc836f74da7c3e3f35e282639763671db048a251d9ce37a`（2,985,676 B）；新网 PDF `be52a9b504caaebb4fe03b0c7ba514222560fc0f3a8d0d5f76e085d78caf791a`（932,346 B，<7MB）。印 PDF 较基线缩小系字体子集变化（拉丁文移出 CJK 字体），文字内容不变（文字层 print=web 多重集差 0）。网 PDF 非确定性（同源重建可差数 B），以最终实测值为准；closer 须拷 builder 终轮原件，绝不重跑 webpdf。
- 新版内 SVG SHA-256（run3，12 位前缀；完整值以 `sha256sum` 验 patched `svg/`）：

| SVG | SHA-256 |
|-----|---------|
| p1-front.svg | `e3baae91f116…` |
| p2-leben.svg | `10b89ee6afb9…` |
| p3-kultur.svg | `edf1fafe5c7d…` |
| p4-sport.svg | `e6c8c4599ffd…` |
| p5-jugend.svg | `9d66fa649458…` |
| p6-vertiefung.svg | `0e5bce07e5f8…` |
| p7-sprache.svg | `ea49eb5ed7d1…` |
| p8-uebungen.svg | `e1d49b296030…` |

- text.md：D5 不改文字内容；交付件为已核实导出器重出，vs `issues/` 已发 `.text.md` BYTE-IDENTICAL（49,140 B，SHA `8b9c39c0e03b16111283697312067b0888ccffe222cf680da66a6998bedd8426`）。
- KIT：`patched/2026-w46-de-fr/WEEKLY-KIT.md`（交付物针脚行已更新为 D5 最终实测值 + 末节 D5 记录；版内 SVG 针脚旧表已随 D5 重排过期，新值见上表）。
- 生产源同步待 closer（本 builder 未自拷；closer 须核实 production 源 == patched 源后再 commit，见家族报告 §8）。

