# GATE-LOG — 2026-w47-fr-ru 最终门禁复核（只读，未改源）
- 时间：2026-11-13 ~00:50 UTC；复核员：门禁工人（协调员 #4 派）
- 对象：~/workspace/weekly-git/production/2026-w47/2026-w47-fr-ru/（HEAD TOO WIDE 四处修后重建态）
- 日志与证据：本目录 scratch-gate-fr-ru-final/（p8-*.log/json、occlusion.log、boxtitle.log + .json、spill.log、edge.log、probe.log、census.log/json、freeze-diff.log/json）

## 当前磁盘 SHA-12
- 印 PDF La-Lucerna-VOL4-fr-ru.pdf：1aa7c71d7f2e / 17,222,306 B / mtime 2026-11-13 00:23 UTC
- 网 PDF La-Lucerna-VOL4-fr-ru-web.pdf：85c45f1cff46 / 1,773,870 B / mtime 2026-11-13 00:23 UTC
- text.md：028cb8c2d4b0 / 50,495 B / mtime 2026-11-13 00:42 UTC
- （均与 *-ru 重建工人 A 的 e2c48b75…/5387c82a… 不同：四处修后已重建）

## 逐项结果
1. p8 compare --total：PASS。compare vs core-fr：CLEAN，121/121 noted，missing=[] extra=0 uncertain=[]，keydiff=[150]（已知 Q150 读者语标签，前轮已裁定）。extract keys 150/150。
2. 几何遮挡扫描 occlusion_audit.py：FAIL — 1 flag。`[TEXTX] p1-une.svg 'ALCARAZ GAGNE PARIS, LE SÉNAT VOTE MERCREDI' — ink overlaps 'АЛЬКАРАС' by 108.2x19.8px`。实测复核：P1 深绿带内法文头条 x=118 y=524 Newsreader 46pt bold，PIL 实测宽 1292.7px → ink_r 1410.7；俄文 gloss 'АЛЬКАРАС' 同基线 y=524 起于 x=1302.5 → 重叠 108.2px，与 audit 数值逐位一致。真墨相撞，非误报。前态 r2 为 0 flags，属本次改道（拉丁改走较宽 Newsreader）新引入的回归，与 7 处 HEAD TOO WIDE 同一机制。
3. 三门禁：
   - boxtitle：FAIL — 4 DEFECT（53 titles / 549 body lines）：P3 'LES DATES EN CHIFFRES' over +7.6px right（core -9.8）；P4 'LES PHRASES DU COMMENTATEUR' +36.5px（core -1.5；ink_r 1448.0 越过栏右 1411.5，并越过下一栏左界 1439.5 共 8.5px，但无墨迹碰撞，overlap=None, clip=False）；P5 'КИНО' +21.3px（core -14.6）；P6 'TROIS DATES POUR COMPRENDRE' +24.5px（core -12.5）。前态 r2 为 0 DEFECT（43 titles / 358 lines），同为改道回归。四处已修标题均不在缺陷表内。
   - spill：PASS — 0 SPILL（33 boxes / 151 candidates / 151 OBSERVE，rc=0）。
   - edge：PASS — 8 pages，0 TOUCH，0 NEAR；各页最小边距 top 54.0 / bottom 53.6 / left 65.5–65.9 / right 45.0–66.2 pt。
4. D5 census：PASS。svglib.py 含 _D5_READER="ru"，第 140 行注明 former "ru" 分支已删（2026-11-12 fix-xru）。probe_xru：fr-ru runs=3123，LAT@NotoSans=0，LAT@Newsreader=23917，CYR@NotoSans=5246，CYR@Newsreader=0，CJK+LAT=0，CJK+CYR=89，curly={}。d5_census.py：D5_latin_in_cjk=0，D5_cyrillic_in_cjk=0，curly_in_cjk=0，CENSUS PASS。
5. 文本层 multiset 一致：PASS。三方一致：(a) 印 vs 网 PDF 文本层逐字节相同（plain 51,047 B，layout 103,650 B），multiset 相同（35,413 非空字符）；(b) p8 键 150/150 与 text.md 答案键逐字一致（注记剥离后 diff 0；Q25 'd'、Q150 'Открытый вопрос'）；(c) SVG 全文 multiset vs 印 PDF 文本层：表观差 12 字符，实为 `&amp;` ×3（p5/p6/p8 各 1）的 XML 转义假象，真实差 0。
6. freeze：PASS（按工具语义）。freeze.py diff vs core-fr rc=0；TOTAL added CJK 10（全 U+3000，与 r2 的 9、fix2 的 8 同量级），added Latin 203（r2 为 225、fix2 为 226；core-vs-edition 差分按工具文档必然 wholesale 添拉丁，--strict-latin 禁用于此，不作 FAIL 判据）。源↔PDF 同步：content56.py/content7.py 00:17、expl.py 00:18、svg/ 00:22–00:23、两 PDF 00:23——PDF 建于最后一次源码改动之后，无未同步源码改动；text.md 00:42 晚于 PDF，但 text.md 是导出物非 PDF 输入，其四处标题与 SVG/PDF 已逐处核对一致。git status：整版目录仍为 untracked（??），属插仓前正常态，非不同步。
7. 成品形态：PASS。印 PDF 8 页（pdfinfo Pages: 8，1462.5×2025 pts），网 PDF 8 页；VOL.4 共 12 处（'VOL.4' ×11 + 间隔体 'VOL. 4' ×1，合 §1.1 式）；网 PDF 1,773,870 B < 7 MB；文本层 51,047 B 非空。

## 四处 HEAD TOO WIDE 修后核验（附加）
- SVG 源 + 印/网 PDF 文本层：'LIRE CALENDRIER' 各 1、'COMPARATIF EN POLITIQUE' 各 1、'CLINIQUE'（P7，>CLINIQUE<）在、'CLINIQUE DES ERREURS' 0、'LIRE LE CALENDRIER' 0、'LE COMPARATIF EN POLITIQUE' 0；'МИНИ-ДРИЛЛЫ' 印/网各 1 次（P4，SVG 内为分 run 书写故整串 grep 为 0，属正常）；P6 MICRO-DRILLS 无 gloss（SVG 内 МИНИ-ДРИЛЛЫ 0）。
- text.md：L539 '### MICRO-DRILLS　МИНИ-ДРИЛЛЫ'（P4 gloss 保留）、L723 '### LIRE CALENDRIER　КАЛЕНДАРЬ'、L761 '### COMPARATIF EN POLITIQUE'、L771 '### MICRO-DRILLS'（P6 无 gloss）、L921 '### CLINIQUE　ОШИБКИ'。

## 结论
- PASS：p8、spill、edge、D5 census、文本层三方一致、freeze、成品形态（7 项中 5 项全绿，另 p8 计入则 6 项）。
- FAIL（2 项，均为改道回归，前态 r2 皆为 0）：occlusion 1 flag（P1 头条撞 gloss，108.2×19.8px）；boxtitle 4 DEFECT（P3 +7.6 / P4 +36.5 / P5 +21.3 / P6 +24.5px 右溢）。
- 未修：按任务只读复核，未动任何源。建议后续：与 HEAD TOO WIDE 裁定同一机制处理——P1 gloss 位置须随 Newsreader 头条宽度重算（或缩短头条），四处 boxtitle 标题须缩短措辞或降字号；修后单版重建 + 全套门禁重跑。另提示：同机制可能波及其他 *-ru 版，建议协调员抽查兄弟版的 occlusion/boxtitle（本次任务范围仅 fr-ru，未扩查）。
