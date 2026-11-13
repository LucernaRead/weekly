# HEAD TOO WIDE 裁定记录 — W47 *-ru 跨家修复后续

裁定工人：e1d9dc97（2026-11-12 ~23:50–00:27 UTC）；恢复协调员 #4 复核（2026-11-13 ~00:40 UTC，本人重跑 measure3.py 核实 + 裁图目视）。
最终清单以 11 版 run 日志为准：**15 处**（de×4、en×2、fr×7、it×1、pt×1），另 zh-cn×1 为修前已接受（KIT F8，422.7 vs 422.5px）。
量法说明：measure3.py 的 overhang_pixel_u 为 200dpi 像素实测；fix 工人的 SVG ink / PDF span advance 为另两种量法，同一处三数可差 1–2u，均属亚像素量级时以"无碰撞 + 不越栏 + 不越页边"为准。

## 已修复并重建（8 处）

| # | 版 | 页 | 原标题 | 修复 | 复测 overhang_pixel_u |
|---|---|---|---|---|---|
| 1 | de-ru | P1 | EINE WOCHE, ZWEI STIMMUNGEN | 删 EINE | −26.2（栏内） |
| 2 | de-ru | P8 | WISSENSFRAGEN | 字号 18→17.25pt | −8.9 |
| 3 | de-ru | P8 | WÖRTER PAAREN Подбор слов | gloss 缩为 Подбор | −34.4 |
| 4 | fr-ru | P6 | LIRE LE CALENDRIER | 删 LE | −28.6 |
| 5 | fr-ru | P6 | LE COMPARATIF EN POLITIQUE | 删 LE | −31.5 |
| 6 | fr-ru | P6 | MICRO-DRILLS（带 gloss） | 改用 gloss-less head_micro6 | −219.2 |
| 7 | fr-ru | P7 | CLINIQUE DES ERREURS | 缩为 CLINIQUE | −166.3 |
| 8 | pt-ru | P2 | COMPLETE COM OS NÚMEROS | 删 COM | −34.9 |

de-ru / fr-ru 的 text.md 已由协调员重导出同步（de-ru diff 恰 2 行、fr-ru diff 恰 4 行）；pt-ru 无需改。

## 量测在栏内，无需修复（2 处）

fr-ru P6 与 P7 的 `IL EST PRÉVU QUE + SUBJONCTIF` 均被 build 报 HEAD TOO WIDE，但 measure3 像素实测均为 −9.4u（栏内），未作改动。

## 接受（未修复，裁图 + 实测证据在案）

| # | 版 | 页 | 标题 | 实测 | 接受理由 |
|---|---|---|---|---|---|
| A1 | en-ru | P7 | AN EXAMPLE LETTER | +5.2u | 裁图干净，无碰撞，不越栏 |
| A2 | en-ru | P? | Понимание текста | +0.4u | 可忽略（亚像素） |
| A3 | it-ru | P6 | LE PAROLE DELLA MANOVRA | +27.8u | 裁图干净，墨迹止于规则线末端，无碰撞 |
| A4 | fr-ru | P7 | BOÎTE À OUTILS | +14.8u（像素） | 墨迹过规则线但 text_colliders 0、next_span 右侧无内容、距页边 70.9u；裁图确认空 gutter、无碰撞 |
| A5 | de-ru | P8 | SÄTZE BAUEN | +0.7u（像素）/+1.8u（SVG ink）/+2.9u（PDF span advance） | 三种量法均 <3u（约 6px @200dpi），无碰撞；fix-de-ru2 工人复测确认 occlusion 0 flags |

A1–A3 未重建（en/it 无 measure3 复测记录，以裁图为准）；A4/A5 的 HEAD TOO WIDE 警告仍会出现在 build 日志与 head_check 中——**属已接受项，不是未修项**；各版 KIT 须记接受记录（de-ru KIT §7 fix-de-ru2 条已记 A5 两数；fr-ru / en-ru / it-ru KIT 在 wave 2 补记）。

## 后续发现（裁定之后，*-ru 改道回归）

裁定只覆盖 build 警告的 HEAD TOO WIDE；occlusion / boxtitle 两门禁不在 build 日志里，fix-xru 重建工人只跑了 probe + multiset、未重跑这两门。后由门禁复核与扫查发现 **28 处改道回归**（fr 5、de 6、nl 4、es 1、en 3、it 5、pt 4），分布 7 版；干净 4 版（ja、ko、zh-cn、zh-tw）。7 版修复工人已全部派发并逐版重建 + 全套门禁重跑 + KIT 更新（见 run-log.md 2026-11-13 01:xx 条）。
