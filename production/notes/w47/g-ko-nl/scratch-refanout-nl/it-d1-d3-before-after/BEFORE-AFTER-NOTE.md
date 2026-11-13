# nl-it D1 + D3 改前改后渲染对比（2026-11-11，proof1 c53043f4 跟进）

上 = 改前（build 3，见 `../backup/2026-w47-nl-it/cards/`）；下 = 改后（build 4，见
`production/2026-w47/fanout-nl/2026-w47-nl-it/cards/`）。卡片均为 1950×2700，坐标 1:1。

## D1［major］P7 HET WOORD 框标题横向溢出 — `d1-p7-hetwoord.png`
- 改前：`HET WOORD　PAROLA DELLA SETTIMANA`，PIL 真墨右缘 1927.5（渲染像素 1927.9），
  超奶油盒右缘 1862 约 +66px；`SETTIMANA` 落在新闻纸上（图上可见奶油底色在词中截断）。
- 改后：`HET WOORD　PAROLA`，真墨右缘 1714，余量 +148px，居盒内。
- 机制层同步修正：`scratch-fanout-nl/trans_table.py` it 值
  `"HET WOORD　PAROLA DELLA SETTIMANA"` → `"HET WOORD　PAROLA"`（原值在表 1425 起的 dict 内），
  防后代 re-gen 回退。build 4 内容文件早已是短式；本次跟进只补表 + 真墨重测。

## D3［minor］4 处弯引号 U+2019 → 直引号 U+0027 — `d3-p7-unantica.png` / `d3-p8-lesercizio.png`
- 改前：P7 金句 `un’ antica`、P8 头注 `l’ esercizio`，Noto Sans CJK SC 里弯引号后有
  一整格空隙，读作错字（图上清晰可见）；另 2 处在 Newsreader 字体里（P8 注 126
  `all’Eredivisie`、注 140 `un’espressione`），放大亦紧密但为统一仍改直。
- 改后：`un'antica`、`l'esercizio` 紧密无空隙；全版 U+2019 扫查 = 0（content / svg /
  text.md / 印网双 PDF 文字层），其余 39 处直引号一致。
- 表源头同步修正（4 处）：trans_table.py 1524 `un’antica`、1616 `all’Eredivisie`、
  1726 `un’espressione`、1792 `l’esercizio` 一律改直。表内 U+2019 由 15 降至 11；
  余下 11 处为 fr（7）/ en（1）/ it 死条目 1436 `c’erano`（该 it 条目不在本版 content
  文件中——版内 BRIEVEN 注为改写短句，不含此串——故不动）及其他法语条目，均不在
  本次 nl-it 范围内，不碰。
- 与 es-it fix1（直→弯）方向冲突：根因为拉丁文在 CJK SC 字体里的渲染问题；
  nl-it 只按渲染实证改，不碰 es-it 方向。冲突已记入本说明，由协调员上报。

## 横向框标题真墨检查（本次新增，10 版 post-build 必查）
- 新工具 `../check_titles_h.py`：每版 56 个粗体/≥23pt 框内标题，真墨右缘 vs 自身框右缘。
- 9 版（en/de/fr/es/it/pt/ru/ja/ko）已跑：全部 ALL PASS，0 FAIL。
  最紧：es P6 `DE GRAFIEK　DATOS DE PRÁCTICA` 余量 +0（实墨 lum<90 最右 1861、框内 1px；
  lum<150 时 1862 仅为 1px 抗锯齿边缘触缘线，未越过——见 `es-p6-charthead-zoom.png`，
  末字 A 未落新闻纸；与 build 3 裁决一致，不修）；pt P7 `PALAVRA DA SEMANA` +1；
  ru P6 +10；en P7 / fr P6 / ja P2 各 +13。
- 初版脚本曾有串扰误报（P2 四栏表头、P1 数字框标题扫到同基线邻栏墨迹），已修为
  按文本自身 advance 跨度（anchor-aware，+3px 外延）限探针范围；重跑后 0 FAIL。
- zh-tw 待其 build 完成后补跑。
