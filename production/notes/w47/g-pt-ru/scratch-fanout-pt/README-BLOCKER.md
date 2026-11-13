# W47 PT fan-out — BLOCKER: Disk quota exceeded (STOPPED 2026-11-11 ~00:52 UTC)

## 阻断（按 brief：遇 Disk quota 立即停手，不硬锤重试）
- 三次 `Disk quota exceeded`（Errno 122）：① muse.write transform.py（后一次重试成功）；
  ② build_one.sh en 重建时 `tee` 写日志 + CairoSVG 写卡片同时失败（render 中断）；
  ③ python 写回 tables_en.py 时失败（文件未损坏，替换未生效）。
- 当时并行情况：production/2026-w47/ 下已有 de-en、en-de、es-en、it-en、fanout-zh-tw 等
  兄弟 agent 的在建目录，约 16 个并行 agent 同时写盘；`df` 仍显示 46G 空闲，
  `quota` 命令不存在，故配额为项目级/瞬时波动，非文件系统写满。
  小写（1MB 测试）随后成功，说明是临界波动而非彻底写满。
- 停手点：英文版 pt-en。以下 P7 修复值已决定但**未写入**表文件，恢复时先应用再重建：
  1. tables_en.py SEG：`官方答案到 11 月底才出，周日晚上只有非官方版` →
     `The official key comes only at the end of November.`
  2. tables_en.py SEG：`意识、良知；黑人意识日：铭记抗争与文化` →
     `awareness, conscience: the memory of the struggle and the culture`
  3. tables_en.py OVR + furniture.py disc_text：披露改为
     `Editor's note: no real letters or best texts for VOL.3 had arrived — the example stands; the promise carries to VOL.5.`
     （已量 wrap 19.5pt/378.5px = 3 行；旧版 4 行）
  4. furniture.py en 加 `"p7_geo": {"letters_pad": 22, "fy_gap": 30, "quote_step": 88}`；
     transform.py 加一步（content7.py）：`)) * 29 + 35`→`)) * 29 + {pad}`，
     `ly + lh + 36`→`ly + lh + {gap}`，`(i % 4) * 96`→`(i % 4) * {step}`。
     （P7 引用区撞下期预告框的根因：英文讲解比中文长约 146px，fy 被推到 2095，
     第 4 行引用落进 py=2404 的预告框；上述四项合计约省 106px + 行距收紧，
     fy≈1988，第 4 行末 ≈2374 < 2404。）

## 已完成（pt-en 英文版，截至停手）
- transform 机制已打通并验证：core-pt 复制 → transform.py（家具 + OVR 54 条 + SEG 221 条
  + 全角标点转 ASCII）→ make_gates.py → run.py → gates.py **16/16 PASS**，零 FLOW OVERFLOW，
  练习 150（A2 48 / B1 71 / B2 31；分版 10/18/18/18/18/18/12/38），源文件零 CJK。
- p8.py extract **150/150**；compare vs 核心 **CLEAN**，keydiff 仅 [137, 138]（翻译题键随读者语变，属正常）。
- freeze diff：added CJK 仅每页 1 个 U+3000 全角空格分隔符（家具 `　`），无新增汉字；
  P1 SVG 的 3 个“真汉字”是品牌蛾标 SVG 内部 `<title>Lucerna 三色蛾</title>`，核心版同样有，不渲染。
- gates 曾 1 FAIL 已修：P2 配对题 instr `Match the words to their meanings` 超页框 →
  SEG 改为 W46 用法 `Match the pairs`，重跑后 gates 16/16。
- P8 答案流曾溢出（y=2590）：已按 W46 英文先例在 transform 加 `p8_keys_small`
  （af.para 13.5→13，lh 1.16→1.12），重跑后 keys 流止于 y=2426。
- 待做（pt-en）：① 应用上方 P7 四项修复 → 重建 → occlusion 重跑至 0 flags；
  ② render.py（卡片 + 印刷 PDF，**当前目录内 PDF 仍是复制的核心版旧文件，不可作数；
  cards/p1、p2 为英文重渲，其余 6 张仍是核心版复制**）；③ webpdf.py + 文字层比对；
  ④ P8 字号实测；⑤ 8 版目视；⑥ 150 题逐题复核；⑦ .text.md + ABSTRACT.txt + WEEKLY-KIT.md。

## 其余 9 版状态
- 未开始。仅英文表（tables_en.py / furniture.py 仅 en 一项）已写；de/fr/es/it/nl/ru/ja/ko/zh-tw
  的翻译表、家具、gates 适配均未写。W46 各语 transform.py / bslib4.py / content12.py
  的家具先例已在分析中取到（见本 agent 工作记录下文“先例摘录”），恢复时可直接用。
- 机制文件位置：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-pt/`
  （transform.py、make_gates.py、build_one.sh、tables_en.py、furniture.py、
  cjk-literals/segments、classify2、en-build.log、en-occlusion.json、en-p8-*.json、en-freeze-diff.json、en-run2.log）。
- 核心版 core-pt 未动（freeze baseline 未跑；core SVG 哈希未变，目录只读使用）。

## 先例摘录（W46 pt-<lang>，VOL.3→VOL.4 换号即用）
- footer（bslib4 67行）/ page line（68行）/ gloss 前缀（194行）/ badge 372行 / 330行字号：
  en: footer `VOL.4　Text in Portuguese　Explanations in English`, page `Page {n} of {total}`,
    gloss `Note | `, badge `TEXT IN PORTUGUESE　EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS`, 330 `PORTUGUESE WEEKLY　VOL.4　…` 32pt
  de: footer `PORTUGIESISCHE WOCHENZEITUNG VOL.4　TEXT AUF PORTUGIESISCH　ERKLÄRUNGEN AUF DEUTSCH`,
    page `Seite {n} von {total}`, gloss `HINWEIS · `, badge `PORTUGIESISCHER TEXT　DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`, 330 28pt
  fr: footer `HEBDOMADAIRE PORTUGAIS VOL.4　TEXTE EN PORTUGAIS　EXPLICATIONS EN FRANÇAIS`,
    page `Page {n} sur {total}`, gloss `Note — `, badge `TEXTES EN PORTUGAIS　EXPLICATIONS EN FRANÇAIS — L’ÉDITION POUR LES LECTEURS FRANCOPHONES`, 330 32pt
  es: footer `SEMANARIO PORTUGUÉS VOL.4　TEXTO EN PORTUGUÉS　EXPLICACIONES EN ESPAÑOL`,
    page `Página {n} de {total}`, gloss `Nota — `, badge `TEXTOS EN PORTUGUÉS　EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES`, 330 30pt
  it: footer `SETTIMANALE PORTOGHESE VOL.4　TESTI IN PORTOGHESE　SPIEGAZIONI IN ITALIANO`,
    page `Pagina {n} di {total}`, gloss `Nota — `, badge `TESTI IN PORTOGHESE　SPIEGAZIONI IN ITALIANO — L’EDIZIONE PER I LETTORI ITALIANI`, 330 30pt
  nl: footer `PORTUGEES WEEKBLAD VOL.4　TEKSTEN IN HET PORTUGEES　UITLEG IN HET NEDERLANDS`,
    page `Pagina {n} van {total}`, gloss `Uitleg — `, badge `TEKSTEN IN HET PORTUGEES　UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`, 330 32pt
  ru: footer `ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.4　ТЕКСТЫ НА ПОРТУГАЛЬСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ`,
    page `Страница {n} из {total}`, gloss `Пояснение — `, badge `ТЕКСТЫ НА ПОРТУГАЛЬСКОМ　ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ`, 330 28pt
  ja: footer `ポルトガル語週刊 VOL.4　本文はポルトガル語　解説は日本語`, page `{n}ページ（全{total}ページ）`,
    gloss `解説 — `, badge `ポルトガル語テキスト　日本語の解説 — 日本語読者のための版`, 330 34pt；
    svglib 须整体复用 W46 pt-ja 版（禁则 kinsoku 补丁；W47 核心 svglib 与 W46 英版逐字节相同）
  ko: footer `포르투갈어 주간지 VOL.4　텍스트는 포르투갈어　해설은 한국어`, page `제 {n} 면 / 총 {total} 면`,
    gloss `해설 — `, badge `포르투갈어 텍스트　한국어 해설 — 한국어 독자를 위한 판`, 330 32pt
  zh-tw: footer `葡萄牙語週報 VOL.4　正文葡萄牙語　講解繁體中文`, page `第{n}版／共{total}版`,
    gloss `譯注｜`, badge `葡萄牙語正文　繁體中文講解 — 給繁體中文讀者的版本`, 330 34pt
- 330 行主题段各语相同：`CONSCIÊNCIA NEGRA　GABARITO DO ENEM　A FINAL DA COPA`（葡语冻结），
  前缀为各语周报名 + VOL.4。
- P8 band 各语（W46 12行）：en `AVALIAÇÃO E RESPOSTAS　TEST AND ANSWERS` / `PAGE 8　The big test of the week + all the answers`；
  de `TEST UND ANTWORTEN` / `SEITE 8　Die große Prüfung der Woche + alle Antworten`；
  fr `TEST ET RÉPONSES` / `PAGE 8　La grande épreuve de la semaine + toutes les réponses`；
  es `PRUEBA Y RESPUESTAS` / `PÁGINA 8　La gran prueba de la semana + todas las respuestas`；
  it `PROVA E RISPOSTE` / `PAGINA 8　La grande prova della settimana + tutte le risposte`；
  nl `TOETS EN ANTWOORDEN` / `PAGINA 8　De grote toets van de week + alle antwoorden`；
  ru `ТЕСТ И ОТВЕТЫ` / `СТРАНИЦА 8　Большой тест недели + все ответы`；
  ja `評価と解答` / `8ページ　今週の大テスト + すべての解答`；
  ko `평가와 정답` / `8면　이번 주의 큰 시험 + 모든 정답`；
  zh-tw `練習與答案` / `第8版　A grande prova da semana + todas as respostas`。
  （注：W47 核心 P8 band 子行是 `第8版　A grande prova…`，OVR 表已有英文版；其余语按上表译左段、
  子行保留葡语原文仅换版次词。）
- P8 分隔符 `— PÁGINA {pg} —` 各语均保留葡语（W46 全语一致）。
- 核心 KIT §6 说明：pt 核心版 KIT §6 仍为“[待重渲染后填写]”（字节数为第三轮值，滞后）；
  fan-out 版 KIT 写本版实测值，不照抄核心 KIT 滞后数字。
