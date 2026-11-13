# KIT 追加节草稿（W47 es 家庭独立重校修复，2026-11-12）——门禁行待 gates-all2.log 完成后填
# 每版追加到 WEEKLY-KIT.md 末尾，标题：## 独立重校修复记录（2026-11-12，F2/F3/F4）
# SHA/尺寸均为盘上实测（见 FIX-LOG「改后 SHA」节）；印/网文字层 pdftotext 字节数见各行。

## core-es（es-zh-cn）
- 修复：F2（P6 时间轴 `content56.py:137`）`"23 NOV. — Atresmedia convoca un debate a cuatro (sin el PSOE)."` → `"(sin el PSOE confirmado)."`，与同页正文 `:124` 一致。F1 首字下沉按协调员裁定不修（已知引擎偏差，见 FIX-LOG）。
- 新 PDF：印刷版 `La-Lucerna-VOL4.pdf` 4,317,615 B，SHA-256 `6089c0fa54208b73bb920076b0b001425e962d308cfa4bc003836f8184aae13f`；网页版 `La-Lucerna-VOL4-web.pdf` 1,162,042 B（< 7 MB），SHA-256 `f0f6ed1de57a12942d39ac864d1b74ac854301ddcba28e1c1a6e5b340424bd95`。`text.md` 1,803 行、43,782 字节，SHA-256 `e537146d733dbe8699fd887aba48fca07b4fbbe49f0dd495d170856530d6966f`（D5 工具重导出，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 44,562 字节，一致。
- 门禁：

## 2026-w47-es-de
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-de.pdf` 2,916,396 B，SHA-256 `3fdc2ce60e6a87f5b16526122c563a12656cf2a944ca1ccf313eab12890994de`；网页版 `La-Lucerna-VOL4-es-de-web.pdf` 806,895 B（< 7 MB），SHA-256 `fd7edd4b84152439dd4a7458646f609cefb7c0380ce5f1b4d503528dee1819e7`。`text.md` 1,802 行、45,322 字节，SHA-256 `c0838896276749128aeb4e0c63e5646b2dd64eb79cef2332ed4f5132998e574d`（手术式单行替换，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 46,258 字节，一致。
- 门禁：

## 2026-w47-es-en
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-en.pdf` 2,915,635 B，SHA-256 `a7d5aba8bd0ff869a4ceed41194589262c8c97d35dab201d9196ebe29be92fb4`；网页版 `La-Lucerna-VOL4-es-en-web.pdf` 806,124 B（< 7 MB），SHA-256 `bb690dd25b6c822b9dd846b02163c747a7432d28f0c57a8b07363847ba64d204`。`text.md` 1,797 行、44,994 字节，SHA-256 `cfdd39a9779d83ed59667049a01570d7fa719e7ac529ae4eeec4e9e54489a220`（手术式单行替换，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 45,867 字节，一致。
- 门禁：

## 2026-w47-es-fr
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`；F3（P1 刊头顶行 `content12.py:16`）副标 `CADA SEMANA EN ESPAÑOL　CHAQUE SEMAINE　L'ESPAGNOL DES ESPAGNOLS` → `CADA SEMANA EN ESPAÑOL　CHAQUE SEMAINE EN ESPAGNOL`——重渲染后实测副标右端与日期左端间隙 65.48pt（修前 1.28pt，粘连），P1 目视干净。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-fr.pdf` 2,914,957 B，SHA-256 `fd0e9f83a9897a6bc9bcde31784f6e8a9a2b348ceac12fc8687e603a95840815`；网页版 `La-Lucerna-VOL4-es-fr-web.pdf` 805,426 B（< 7 MB），SHA-256 `960de8cf8d3be5fda7e68e8bffef580f3733094a58e3b663817d8bef3aeb271a`。`text.md` 1,815 行、45,790 字节，SHA-256 `a9aed8190e839c531e5734d04a6f1c7d846d43f2a0a3f944140f3dfec8340e51`（手术式两行替换：F2 一行＋F3 副标一行，diff 恰为此两行）。印/网文字层 pdftotext 各 46,661 字节，一致。
- 门禁：

## 2026-w47-es-it
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`；F3（P1 刊头顶行 `content12.py:16`）副标 `CADA SEMANA EN ESPAÑOL　OGNI SETTIMANA　LO SPAGNOLO DEGLI SPAGNOLI` → `CADA SEMANA EN ESPAÑOL　OGNI SETTIMANA IN SPAGNOLO`——重渲染后实测副标右端与日期左端间隙 68.78pt（修前 −6.09pt，重叠），P1 目视干净。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-it.pdf` 2,913,352 B，SHA-256 `0cffc84e47c03b93b1c6fff8d750eaf9213d818eefc33820b7bbdefc138e8364`；网页版 `La-Lucerna-VOL4-es-it-web.pdf` 803,822 B（< 7 MB），SHA-256 `f533bb1aa13331a187ed26a4f7bf706b1db99ed7a1d79c3ed11689df345411a1`。`text.md` 1,806 行、45,170 字节，SHA-256 `ee56751564b3e04ec012fa5f8e02d3ef12016e16eb79285c55169cf21b117e74`（手术式两行替换：F2 一行＋F3 副标一行，diff 恰为此两行）。印/网文字层 pdftotext 各 46,034 字节，一致。
- 门禁：

## 2026-w47-es-ja
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-ja.pdf` 8,530,855 B，SHA-256 `6d89a8ddf67bc83b48c1c9650bc7daf0c1247e3eec8b943fb71bf60ec5fb726e`；网页版 `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,428 B（< 7 MB），SHA-256 `c2e0230bac8c17b7e06be61dfa981818ca433c73171f0de0af1eb705701bfae2`。`text.md` 1,820 行、46,565 字节，SHA-256 `998a9ac325003cde55ed13facad56b3b98e6802a5f64985da1211298c50fe4c6`（手术式单行替换，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 47,479 字节，一致。
- 门禁：

## 2026-w47-es-ko
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-ko.pdf` 5,229,281 B，SHA-256 `e2ae545b1462d436c68e9715a03e9fd2b3ec65f8a451a04f42d5423302466f34`；网页版 `La-Lucerna-VOL4-es-ko-web.pdf` 1,097,497 B（< 7 MB），SHA-256 `fad91509e34fdd2b2c41ac51737d728e328f2688a95064a8fdba6c39d28e7804`。`text.md` 1,823 行、47,396 字节，SHA-256 `981d43e9183762028d62283832c69866ec963ba7f8a94b1b0152a2da8b57d581`（手术式单行替换，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 48,250 字节，一致。
- 门禁：

## 2026-w47-es-nl
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-nl.pdf` 2,915,320 B，SHA-256 `c716ce60992a4dd70c0debf89636650fa073255d3fad4dd2a83b306e5011d288`；网页版 `La-Lucerna-VOL4-es-nl-web.pdf` 805,809 B（< 7 MB），SHA-256 `8be3118b5080e616f5f92b03a792f56327c2ab3272e5fe7a3daa17a96a6107a3`。`text.md` 1,835 行、45,295 字节，SHA-256 `225181a991b53c7d5babfaa277f0b8a847c9ca759a4e359eca95b16efe178034`（手术式单行替换，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 46,142 字节，一致。
- 门禁：

## 2026-w47-es-pt
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-pt.pdf` 2,914,546 B，SHA-256 `434d8d8fe9c67b41f4af3587fd9585e542baed4e2b0cc3297f194579408a1126`；网页版 `La-Lucerna-VOL4-es-pt-web.pdf` 805,017 B（< 7 MB），SHA-256 `50f4402a6a198863c215a4ec7648526019ed4857a21d80d4265de91090737fe7`。`text.md` 1,815 行、45,546 字节，SHA-256 `f9531af2c6387aa9bf9b0e5fea4379f278a8ce87f164014ecd73eb6e693ce6ad`（手术式单行替换，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 46,461 字节，一致。
- 门禁：

## 2026-w47-es-ru
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`；F4（P2 日历框 `content12.py` 俄语注释 5 处缩短：Lunes `(понедельник: Международный день фламенко; Народная партия предлагает дебаты Санчес — Фейхоо)` → `(понедельник: день фламенко; дебаты Санчес — Фейхоо)`；Martes `кампания едет по Испании` → `кампания по Испании`；Miércoles 删 `, PSOE против PP`；Jueves 删 `по почте`；Domingo `день святой Цецилии` → `св. Цецилия`；日历框 30→25 行）——重渲染后实测 `nunca «en las 21:00».` 行位于 (403.9, 1052.9)，回到 DECIR 标题 (403.9, 877.7) 正下方同栏（修前在 (741.8, 154.6) 页顶；对照 en/de 版 (403.9, 1095.8)），P2 目视干净；被删的俄语注释信息均仍在同条西语行内（日期/人名/党名/投票方式：`Día Internacional del Flamenco`、`el PP propone el cara a cara Sánchez–Feijóo`、`la campaña recorre España`、`Isabel Rodríguez (PSOE) y Juan Bravo (PP)`、`voto por correo`、`Santa Cecilia, patrona de la música`）。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-ru.pdf` 3,213,296 B，SHA-256 `0ca1beca6d7498103b7d36fc27c4946cfdc0276606935ad8b80c0ae9c796e32c`；网页版 `La-Lucerna-VOL4-es-ru-web.pdf` 1,061,817 B（< 7 MB），SHA-256 `2febbe24084bff7e022d937e506df8b1866d211a752936a268194623b09997ae`。`text.md` 1,888 行、52,347 字节，SHA-256 `dadb3e8478e5d06d970e60f62dbd9d958944e28b9b1bc64c541b77cca9571b5a`（词级手术：F2 一行＋F4 删词，词多重集核对仅差意改词）。印/网文字层 pdftotext 各 53,420 字节，一致。
- 门禁：

## 2026-w47-es-zh-tw
- 修复：F2（P6 时间轴 `content56.py:137`，与 core-es 同行同改）`(sin el PSOE).` → `(sin el PSOE confirmado).`。F1 按协调员裁定不修。
- 新 PDF：印刷版 `La-Lucerna-VOL4-es-zh-tw.pdf` 4,381,575 B，SHA-256 `fd3e65ef18402cf3889bfbf16321c451187a94dbc5cc208d90f8db955502bff0`；网页版 `La-Lucerna-VOL4-es-zh-tw-web.pdf` 1,265,861 B（< 7 MB），SHA-256 `8871073245fdb336f634013e365369388196b064a998d7e307b4423a2f9e574e`。`text.md` 1,803 行、43,811 字节，SHA-256 `4795332ea53a4a14bad8c5b558bc6b6ad172f6b1ee42e69423e6f2391ebb25e8`（手术式单行替换，diff 恰为 F2 一行）。印/网文字层 pdftotext 各 44,605 字节，一致。
- 门禁：
