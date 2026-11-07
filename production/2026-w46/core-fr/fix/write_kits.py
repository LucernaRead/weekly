from pathlib import Path
ROOT = Path.home()/"workspace/goals/lucernaread-social-media-operations"
EVIDENCE = {
 "core":  ("23643162", "64007cac3b20", "2057423", "c90da50eed87", "46177", "45506"),
 "de":    ("9847768", "7fab3385e510", "1354604", "2dfa32df8ea2", "46640", "45812"),
 "en":    ("9842783", "be4e8f29ec80", "1347395", "1ed2b23b8840", "45928", "45250"),
 "es":    ("9804515", "8c2632c250e6", "1348845", "8937abb07cde", "46530", "45769"),
 "it":    ("9801621", "b601abbf636f", "1341501", "e639d3348f8e", "46258", "45503"),
 "ja":    ("23705891", "f591deb733ff", "2107641", "a20a1bc641fb", "47153", "46175"),
 "ko":    ("15503892", "fc4242e4dd0a", "1715537", "26e4d5b63abf", "46526", "45689"),
 "nl":    ("9805028", "a5ba002a7f64", "1346343", "d815908cff14", "46302", "45547"),
 "pt":    ("9806086", "6cf4dc11a008", "1350380", "6da9eb2eaa9a", "46380", "45570"),
 "ru":    ("9808194", "6b93351dedfc", "1393328", "53b45fe6a15b", "51372", "50050"),
 "zh-cn": ("23643162", "64007cac3b20", "2057424", "e56328087e18", "46177", "45503"),
 "zh-tw": ("23654837", "7f9ab3a51d93", "2400946", "8190272797d1", "44997", "44327"),
}
D2_FINAL = {
 "it": "Leggere un programma è capire la Francia.",
 "nl": "Een programma lezen is Frankrijk kennen.",
 "pt": "Ler um programa é compreender a França.",
 "ru": "Читая программу, понимаешь Францию.",
 "ja": "番組表を読むとフランスが分かる。",
 "ko": "프로그램표를 읽으면 프랑스를 이해한다.",
}
D2_OLD = {
 "it": "Un programma spiega la Francia.",
 "nl": "Een programma legt Frankrijk uit.",
 "pt": "Um programa explica a França.",
 "ru": "Программа объясняет Францию.",
 "ja": "番組がフランスを説明する。",
 "ko": "프로그램이 프랑스를 설명한다.",
}
D3 = {
 "ja": ("familier くだけた", "familier なじみのある"),
 "ko": ("familier 구어체", "familier 친숙한"),
 "ru": ("familier разговорное", "familier знакомый"),
 "zh-tw": ("familier 口語", "familier 熟悉的"),
}
ADDED_CJK = {"ja": "2,281", "ko": "2,460", "zh-tw": "1,010"}
KEYDIFF = {"zh-cn": "[]"}
for name in ["core","de","en","es","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    slug = "fr-zh-cn" if name=="core" else f"fr-{name}"
    ed_dir = "weekly-report-w46-fr-core" if name=="core" else f"weekly-report-w46-fr-{name}"
    kit = ROOT/"files"/ed_dir/"WEEKLY-KIT.md"
    ps, ph, ws, wh, tb, tm = EVIDENCE[name]
    added = ADDED_CJK.get(name, "0")
    kd = KEYDIFF.get(name, "[150]")
    lines = []
    lines.append("")
    lines.append("## 补记：独立校对 Round 1 缺陷修复（2026-11-03，本地修复工）")
    lines.append("")
    lines.append("独立校对 Round 1 结论见 `hidden_files/w46/fr-proofread-gates/proofreader-verdict-round1.md`（本版 FAIL，缺陷 D1" + ("、D2" if name in D2_FINAL else "") + ("、D3" if name in D3 else "") + "）。以下修复均改构建源码后整版重渲染，未手改 SVG/PDF。构建脚本与门禁输出见 `hidden_files/w46/fr-fix/`（`apply_fixes.py`、`shorten_d2.py`、`render*.log`、`gates-final/`）。")
    lines.append("")
    lines.append("### D1（全部 11 版 + 核心）——P3 第 37 题否定算子与事实冲突")
    lines.append("")
    lines.append("源码：`hidden_files/weekly-report-w46-fr-build/content34.py` 及各母语版构建目录的 `content34.py`（除 OUT 路径外字节相同，12 份同步改动）+ 各版 `expl.py`。")
    lines.append("改前题干：`(plus) La foire est à Paris. → ___`；P8 键：`La foire n'est plus à Paris.`——`ne...plus` 预设集市曾在巴黎，与本期通篇“集市在迪耶普”冲突。")
    lines.append("改后题干：`(pas) La foire est à Paris. → ___`；P8 键：`La foire n'est pas à Paris.`（事实正确的否定为 `ne...pas`）。连带一致性改动：各版 `expl.py` 的 `bridge_neg` 删去 `/ ne...plus`（现仅列 `ne...jamais / ne...pas`），`n_neg3` 注记改为与各版 `n_neg2` 相同的 `ne...pas` 释义（原 `ne...plus` 释义已无对应题）。改后全版 SVG 文本中已无 `n'est plus` / `(plus)` / `ne...plus`。")
    lines.append("")
    if name in D2_FINAL:
        lines.append("### D2（本版）——第 135 题题干与印刷法语键语义不符")
        lines.append("")
        lines.append(f"源码：本版构建目录 `expl.py` 的 `stem_e1`（法语键不变：`Lire un programme, c'est déjà comprendre la France.`）。改前题干：`{D2_OLD[name]}`（意为“一份节目介绍法国”，与键不符）。改后题干：`{D2_FINAL[name]}`。")
        lines.append("过程注记：首版较长译法（含 déjà 对应词）使 P8 电池流末端由 y=1502 增至 y=1552，对话末句 `Merci !` 被范文框覆盖 71%（`occlusion_audit.py` COVER 旗标，卡面目视证实）——与本版构建首轮已知的 P8 溢出同类。遂改为单行短译（与已通过的 EN/DE/ES 版省略 déjà 的译法一致），电池流末端回到 y=1502，遮挡清零。`n_e1` 注记（`lire un programme` = 读节目表）未动，与新题干一致。")
        lines.append("")
    if name in D3:
        old, new = D3[name]
        lines.append("### D3（本版）——P4 `familier` 词注取错义项")
        lines.append("")
        lines.append(f"源码：本版构建目录 `expl.py` 的 `bridge_treve`。正文句：`les noms des villes deviennent familiers`（“变得熟悉”）。改前：`{old}`（口语/随便义）；改后：`{new}`（熟悉义，与 DE `vertraut` / EN `familiar` / zh-cn `熟悉的` 一致）。卡面目视已验新词注完整可见、无溢出。")
        lines.append("")
    lines.append("### 重渲染与重验门禁（最终产物）")
    lines.append("")
    lines.append(f"- 整版重渲染：8 SVG + 8 PNG 卡片 + 大报版 PDF（8 页，{ps} 字节，SHA-256 前 12 位 `{ph}`）+ 网页版 PDF（`tools/webpdf.py`，8 页，{ws} 字节，SHA-256 前 12 位 `{wh}`，< 7 MB，带文字层）。`.text.md` 由源稿导出器从 `content*.py` 重生成（{tm} 字节，含新题干/新键，旧字符串已无），ABSTRACT.txt 未动（仍与本期主题相符）。")
    lines.append(f"- `tools/freeze.py diff` vs 核心：裁定通过——P1–P7 移除的非 CJK 字符串仅标点碎片（`。`/`）。`）；P8 移除碎片均为答案键重排断行，由 p8 比对裁定；新增 CJK 字符 {added} 个（讲解层固有）" + ("；本版与核心 0 差异。" if name=="zh-cn" else "。"))
    lines.append(f"- `tools/p8.py compare`：CLEAN，核心与本版印出注记集均为 121/150，missing=[]、extra=0、uncertain=[]，keydiff={kd}（仅 #150 写作题母语注记，属预期）。")
    lines.append("- `tools/occlusion_audit.py`：0 旗标（每次运行自检 OK）；PDF 校验：8 页，文字层齐全，网页版与大报版 pdftotext 字节相等（" + tb + " 字节）。")
    lines.append("- 改动页人工复核：P3 否定三题（题干/桥接语/ P8 键 37）逐项验过；" + ("第 135 题题干 + P8 对话区逐行验过，`Merci !` 完整可见；" if name in D2_FINAL else "") + ("P4 `familier` 词注及 surrounding 正文验过；" if name in D3 else "") + "未引入新缺陷。F-MAIL 旗标（读者来信邮箱核实）非文本缺陷，仍待协调员在入仓前核实，本次未动相关措辞。")
    lines.append("")
    old_text = kit.read_text(encoding="utf-8")
    assert "独立校对 Round 1 缺陷修复" not in old_text, kit
    kit.write_text(old_text.rstrip("\n") + "\n" + "\n".join(lines), encoding="utf-8")
    print("KIT updated:", kit)
print("ALL KITS DONE")
